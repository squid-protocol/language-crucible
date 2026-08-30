#!/usr/bin/env python3
"""Stage one Language Crucible folder: copy a curated file set + LICENSE from a
pool repo into data/<lang>/<folder>/, then print provenance + SOURCES.md drafts.

Usage:
    stage_folder.py --lang sqlite --folder sqitch_sqlite_engine \
        --src corpus_perl/sqitch \
        --files lib/App/Sqitch/Engine/sqlite.sql lib/App/Sqitch/Engine/Upgrade/sqlite-1.0.sql

    stage_folder.py --lang assembly --folder nasm_testsuite \
        --src corpus_assembly/nasm --find "-path '*/test/*.asm' -size -60k" --limit 20

Rules enforced: skips files > --max-bytes (LICENSE excepted) and binary files;
flattens nested paths into '_'-joined names; dedupes basenames; strips exec bits.
Never modifies anything outside data/<lang>/<folder>/.

Env: GITGALAXY_POOL_PATH (default /srv/storage_16tb/projects/gitgalaxy/data)
"""
import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

POOL = Path(os.environ.get("GITGALAXY_POOL_PATH", "/srv/storage_16tb/projects/gitgalaxy/data"))

_LICENSE_SIGNATURES = [
    ("MIT License", re.compile(r"\bMIT License\b", re.I)),
    ("Apache License 2.0", re.compile(r"Apache License,?\s*Version 2\.0", re.I)),
    ("GNU GPL v3.0", re.compile(r"GENERAL PUBLIC LICENSE\s*\n?\s*Version 3", re.I)),
    ("GNU GPL v2.0", re.compile(r"GENERAL PUBLIC LICENSE\s*\n?\s*Version 2", re.I)),
    ("GNU LGPL", re.compile(r"LESSER GENERAL PUBLIC LICENSE", re.I)),
    ("GNU AGPL v3.0", re.compile(r"AFFERO GENERAL PUBLIC LICENSE", re.I)),
    ("BSD 3-Clause License", re.compile(r"BSD 3-Clause", re.I)),
    ("BSD 2-Clause License", re.compile(r"BSD 2-Clause", re.I)),
    ("BSD License", re.compile(r"Redistribution and use in source and binary forms", re.I)),
    ("ISC License", re.compile(r"\bISC License\b", re.I)),
    ("Mozilla Public License 2.0", re.compile(r"Mozilla Public License,?\s*v\.?\s*2\.0", re.I)),
    ("Eclipse Public License 2.0", re.compile(r"Eclipse Public License\s*-?\s*v?\.?\s*2\.0", re.I)),
    ("The Unlicense", re.compile(r"\bunlicense\b", re.I)),
    ("Public Domain", re.compile(r"public domain|disclaims copyright", re.I)),
    # Fallback: the bare MIT permission grant with no "MIT License" title
    # (godot, jQuery, and others ship the body only). Ordered last so an
    # explicit title above always wins.
    ("MIT License", re.compile(
        r"Permission is hereby granted,\s+free of charge,\s+to any person "
        r"obtaining\s+a\s+copy\s+of\s+this\s+software\s+and\s+associated\s+"
        r"documentation\s+files", re.I)),
]


def find_repo(start: str) -> Path:
    p = Path(start).resolve()
    for c in [p, *p.parents]:
        if (c / "data" / "PROVENANCE.json").exists():
            return c
    sys.exit(f"error: no crucible checkout found from {start}")


def resolve_pool_path(s: str) -> Path:
    p = Path(s)
    cand = p if p.is_absolute() else POOL / p
    if not cand.exists():
        sys.exit(f"error: not found in pool: {cand}")
    return cand.resolve()


def git_root(path: Path) -> Path | None:
    for c in [path, *path.parents]:
        if (c / ".git").exists():
            return c
    return None


def git_info(root: Path):
    def run(*a):
        try:
            return subprocess.run(["git", "-C", str(root), *a], capture_output=True,
                                  text=True, timeout=15).stdout.strip() or None
        except Exception:
            return None
    url = run("remote", "get-url", "origin")
    if url:
        url = re.sub(r"\.git$", "", url)
    return url, run("rev-parse", "HEAD")


def classify_license(path: Path):
    try:
        t = path.read_text(errors="ignore")[:6000]
    except OSError:
        return "present but unrecognized (see file)"
    for label, rx in _LICENSE_SIGNATURES:
        if rx.search(t):
            return label
    return "present but unrecognized (see file)"


def autodetect_license(repo_root: Path):
    for pat in ("LICENSE*", "COPYING*", "COPYRIGHT*", "UNLICENSE*", "licence*"):
        for f in sorted(repo_root.glob(pat)):
            if f.is_file():
                return f
    return None


def is_binary(fp: Path) -> bool:
    try:
        return b"\0" in fp.read_bytes()[:65536]
    except OSError:
        return True


def flat_name(rel: Path) -> str:
    n = "_".join(rel.parts)
    return re.sub(r"[^A-Za-z0-9._-]", "_", n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True)
    ap.add_argument("--folder", required=True)
    ap.add_argument("--src", required=True, help="pool-relative or absolute path to repo/subdir")
    ap.add_argument("--license", help="pool-relative/abs path to that repo's LICENSE file")
    ap.add_argument("--files", nargs="*", default=[], help="paths relative to --src")
    ap.add_argument("--find", help="find(1) expression, applied under --src")
    ap.add_argument("--limit", type=int, default=25)
    ap.add_argument("--max-bytes", type=int, default=61440)
    ap.add_argument("--repo", default=".")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo = find_repo(args.repo)
    src = resolve_pool_path(args.src)
    groot = git_root(src)
    url, commit = git_info(groot) if groot else (None, None)

    # collect candidate files
    cands: list[Path] = []
    if args.files:
        for f in args.files:
            fp = (src / f).resolve()
            if not fp.is_file():
                sys.exit(f"error: not a file: {fp}")
            cands.append(fp)
    elif args.find:
        out = subprocess.run(
            f"find {shlex.quote(str(src))} -type f {args.find}",
            shell=True, capture_output=True, text=True,
        ).stdout.split("\n")
        cands = [Path(x) for x in sorted(out) if x.strip()]
    else:
        sys.exit("error: pass --files or --find")

    # filter
    kept, skipped = [], []
    for fp in cands:
        sz = fp.stat().st_size
        if sz > args.max_bytes:
            skipped.append((fp, f"{sz} B > max"))
            continue
        if is_binary(fp):
            skipped.append((fp, "binary"))
            continue
        kept.append(fp)
        if len(kept) >= args.limit:
            break

    if not kept:
        sys.exit("error: no files survived filtering")

    dest = repo / "data" / args.lang / args.folder
    print(f"# staging  data/{args.lang}/{args.folder}/   <-  {src.relative_to(POOL) if src.is_relative_to(POOL) else src}")
    if skipped:
        for fp, why in skipped:
            print(f"  skip  {fp.name}  ({why})")

    # license
    lic_src = None
    if args.license:
        lic_src = resolve_pool_path(args.license)
    elif groot:
        lic_src = autodetect_license(groot)
    lic_label = classify_license(lic_src) if lic_src else None

    used = {}
    copied = []
    for fp in kept:
        try:
            rel = fp.relative_to(src)
        except ValueError:
            rel = Path(fp.name)
        name = flat_name(rel)
        if name in used:
            used[name] += 1
            stem, ext = os.path.splitext(name)
            name = f"{stem}-{used[name]}{ext}"
        else:
            used[name] = 1
        copied.append((fp, name))

    if args.dry_run:
        print(f"\n  (dry run) would copy {len(copied)} files:")
        for _, n in copied:
            print(f"    {n}")
    else:
        dest.mkdir(parents=True, exist_ok=True)
        for fp, name in copied:
            d = dest / name
            shutil.copyfile(fp, d)
            os.chmod(d, 0o644)
        if lic_src:
            d = dest / lic_src.name
            shutil.copyfile(lic_src, d)
            os.chmod(d, 0o644)
        print(f"\n  copied {len(copied)} files + "
              f"{'LICENSE (' + lic_src.name + ')' if lic_src else 'NO LICENSE'}")
        for _, n in copied:
            print(f"    {n}")

    n_files = len(copied) + (1 if lic_src else 0)
    print("\n# ---- paste into tools/independent_data_auditor.py ----")
    if lic_src:
        print(f'    ("{args.lang}", "{args.folder}"): ('
              f'"{url or "FIXME_URL"}", "{commit or "FIXME_COMMIT"}", "{lic_label}"),')
    else:
        print(f'    ("{args.lang}", "{args.folder}"):\n'
              f'        "FIXME: why this has real content but no license/commit to assert '
              f'(upstream {url or "?"} @ {commit or "?"} ships no LICENSE file). Recorded unknown by design.",')

    print("\n# ---- SOURCES.md row skeleton ----")
    commit_cell = f"`{commit}`" if commit else "n/a"
    lic_cell = lic_label or "unknown"
    print(f"| `{args.folder}` | {n_files} | {url or 'unknown'} | {commit_cell} | {lic_cell} | "
          f"FIXME: name the specific parsing boundary this folder tests (which markers / dialect quirk). |")


if __name__ == "__main__":
    main()
