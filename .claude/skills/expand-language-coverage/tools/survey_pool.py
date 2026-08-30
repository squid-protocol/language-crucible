#!/usr/bin/env python3
"""Survey the gitgalaxy/data pool for material to expand a Language Crucible category.

Usage:
    survey_pool.py <lang> [--standard-only] [--repo PATH] [--min-markers N]
                          [--max-depth 2] [--top 40]

Reads the language's detection standard (extensions / shebangs / signature
markers mined from its regex rules), then walks the pool reporting which repos
carry dialect-correct files for that language, with per-repo HEAD / remote /
license. Writes a JSON manifest scaffold to <repo>/.crucible-survey-<lang>.json.

Env: GITGALAXY_POOL_PATH (default /srv/storage_16tb/projects/gitgalaxy/data)
     GITGALAXY_STANDARDS  (default .../gitgalaxy/v6/gitgalaxy/standards/language_standards.py)
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

POOL = os.environ.get("GITGALAXY_POOL_PATH", "/srv/storage_16tb/projects/gitgalaxy/data")
STANDARDS = os.environ.get(
    "GITGALAXY_STANDARDS",
    "/srv/storage_16tb/projects/gitgalaxy/v6/gitgalaxy/standards/language_standards.py",
)

# Tokens that show up in regexes but are not language keywords worth grepping.
_REGEX_NOISE = {
    "re", "compile", "DOTALL", "MULTILINE", "IGNORECASE", "VERBOSE", "None",
    "true", "false", "null", "GLOBAL_PLANNED_DEBT", "GLOBAL_FRAGILE_DEBT",
    "and", "the", "for", "with", "not", "def", "self", "str", "pattern",
    "group", "match", "search", "findall", "sub", "span", "text", "name",
}
_LICENSE_SIGNATURES = [
    ("MIT License", re.compile(r"\bMIT License\b", re.I)),
    ("Apache License 2.0", re.compile(r"Apache License,?\s*Version 2\.0", re.I)),
    ("GNU GPL v3.0", re.compile(r"GENERAL PUBLIC LICENSE\s*\n?\s*Version 3", re.I)),
    ("GNU GPL v2.0", re.compile(r"GENERAL PUBLIC LICENSE\s*\n?\s*Version 2", re.I)),
    ("GNU LGPL", re.compile(r"LESSER GENERAL PUBLIC LICENSE", re.I)),
    ("GNU AGPL v3.0", re.compile(r"AFFERO GENERAL PUBLIC LICENSE", re.I)),
    ("BSD 3-Clause License", re.compile(r"BSD 3-Clause|Redistribution.*?3\. Neither", re.I | re.S)),
    ("BSD 2-Clause License", re.compile(r"BSD 2-Clause", re.I)),
    ("BSD License", re.compile(r"Redistribution and use in source and binary forms", re.I)),
    ("ISC License", re.compile(r"\bISC License\b", re.I)),
    ("Mozilla Public License 2.0", re.compile(r"Mozilla Public License,?\s*v\.?\s*2\.0", re.I)),
    ("Eclipse Public License 2.0", re.compile(r"Eclipse Public License\s*-?\s*v?\.?\s*2\.0", re.I)),
    ("Creative Commons", re.compile(r"Creative Commons", re.I)),
    ("The Unlicense", re.compile(r"\bunlicense\b", re.I)),
    ("Public Domain", re.compile(r"public domain|disclaims copyright", re.I)),
    ("MIT License", re.compile(
        r"Permission is hereby granted, free of charge, to any person obtaining a\s+"
        r"copy of this software and associated documentation files", re.I)),
]


def find_repo(start: str) -> Path:
    p = Path(start).resolve()
    for c in [p, *p.parents]:
        if (c / "data" / "PROVENANCE.json").exists():
            return c
    sys.exit(f"error: no crucible checkout found from {start} (looked for data/PROVENANCE.json)")


def slice_lang_block(text: str, lang: str) -> str:
    # LANGUAGE_DEFINITIONS entries are 4-space-indented keys. A brace counter is
    # unreliable here because the rule regexes are full of literal { } (Tcl proc
    # braces, `{0,2000}` quantifiers), so slice key-to-next-key instead.
    lines = text.splitlines(keepends=True)
    key_rx = re.compile(r'^\s{4}"([a-z0-9_]+)"\s*:\s*\{')
    start = None
    for idx, ln in enumerate(lines):
        m = key_rx.match(ln)
        if m and m.group(1) == lang:
            start = idx
        elif m and start is not None:
            return "".join(lines[start:idx])
    if start is not None:
        return "".join(lines[start:])
    sys.exit(f"error: language '{lang}' not found as a top-level key in {STANDARDS}")


def _str_list(block: str, key: str) -> list[str]:
    m = re.search(re.escape(key) + r'"\s*:\s*\[(.*?)\]', block, re.S)
    if not m:
        return []
    return re.findall(r'["\']([^"\']+)["\']', m.group(1))


def parse_standard(lang: str) -> dict:
    text = Path(STANDARDS).read_text(errors="ignore")
    block = slice_lang_block(text, lang)
    exts = _str_list(block, 'extensions')
    exact = _str_list(block, 'exact_matches')
    shebangs = _str_list(block, 'shebangs')

    # Signature markers: literal word-ish tokens that appear inside the rules'
    # raw-string regexes. Heuristic, for guiding grep -- not exhaustive.
    rules_start = block.find('"rules"')
    rules_txt = block[rules_start:] if rules_start >= 0 else block
    raw = re.findall(r'r"(?:[^"\\]|\\.)*"|r\'(?:[^\'\\]|\\.)*\'', rules_txt)
    markers: dict[str, int] = {}
    for lit in raw:
        body = lit[2:-1]
        # multi-word phrases like WITH\s+RECURSIVE, PRAGMA\s+journal_mode
        for phrase in re.findall(r'[A-Za-z_]{3,}(?:\\s\+[A-Za-z_]{3,}){1,3}', body):
            key = re.sub(r'\\s\+', ' ', phrase)
            markers[key] = markers.get(key, 0) + 1
        for tok in re.findall(r'[A-Za-z_][A-Za-z0-9_]{2,}', body):
            if tok in _REGEX_NOISE or len(tok) < 3:
                continue
            markers[tok] = markers.get(tok, 0) + 1
    # dot-commands (SQLite / CLI style)
    for dot in re.findall(r'\\\.\(\?:([a-z|]+)\)', rules_txt):
        for d in dot.split("|"):
            markers["." + d] = markers.get("." + d, 0) + 1

    ranked = sorted(markers, key=lambda k: (-markers[k], k))
    strong = [
        k for k in ranked
        if (k.isupper() or " " in k or k.startswith(".")
            or re.match(r'[a-z]+_[a-z0-9_]+$', k)
            or (k.islower() and len(k) >= 4 and markers[k] >= 2))
    ][:50]
    return {
        "language": lang,
        "extensions": exts,
        "exact_matches": exact,
        "shebangs": shebangs,
        "markers": strong or ranked[:40],
    }


def classify_license(repo: Path) -> tuple[str | None, str | None]:
    for pat in ("LICENSE*", "COPYING*", "COPYRIGHT*", "UNLICENSE*", "licence*"):
        for f in sorted(repo.glob(pat)):
            if f.is_file():
                try:
                    t = f.read_text(errors="ignore")[:6000]
                except OSError:
                    continue
                for label, rx in _LICENSE_SIGNATURES:
                    if rx.search(t):
                        return label, f.name
                return "present but unrecognized (see file)", f.name
    return None, None


def git_info(repo: Path) -> tuple[str | None, str | None]:
    if not (repo / ".git").exists():
        return None, None
    def run(*a):
        try:
            return subprocess.run(["git", "-C", str(repo), *a], capture_output=True,
                                  text=True, timeout=15).stdout.strip() or None
        except Exception:
            return None
    return run("remote", "get-url", "origin"), run("rev-parse", "HEAD")


def iter_pool_repos(max_depth: int):
    root = Path(POOL)
    if not root.is_dir():
        sys.exit(f"error: pool not found at {POOL} (set GITGALAXY_POOL_PATH)")
    for top in sorted(p for p in root.iterdir() if p.is_dir()):
        if top.name.startswith("corpus_"):
            # the corpus_* dir itself is just a bucket -- yield its member repos
            if max_depth >= 2:
                for sub in sorted(p for p in top.iterdir() if p.is_dir()):
                    yield sub
        else:
            yield top


def scan_repo(repo: Path, exts: set[str], marker_rx: re.Pattern, min_markers: int):
    hits, dialect = 0, 0
    for dirpath, dirnames, files in os.walk(repo):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".gitgalaxy", "node_modules")]
        for fn in files:
            if os.path.splitext(fn)[1].lower() not in exts:
                continue
            hits += 1
            if dialect < 999:
                fp = os.path.join(dirpath, fn)
                try:
                    with open(fp, "rb") as fh:
                        chunk = fh.read(65536)
                    if b"\0" in chunk:
                        continue
                    if len(marker_rx.findall(chunk.decode("utf-8", "ignore"))) >= min_markers:
                        dialect += 1
                except OSError:
                    pass
    return hits, dialect


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lang")
    ap.add_argument("--standard-only", action="store_true")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--min-markers", type=int, default=2)
    ap.add_argument("--max-depth", type=int, default=2)
    ap.add_argument("--top", type=int, default=40)
    args = ap.parse_args()

    std = parse_standard(args.lang)
    print(f"# {args.lang}  —  detection standard\n")
    print(f"extensions   : {std['extensions']}")
    print(f"exact_matches: {std['exact_matches']}")
    print(f"shebangs     : {std['shebangs']}")
    print(f"markers ({len(std['markers'])}): {', '.join(std['markers'])}\n")
    if args.standard_only:
        return

    repo_root = find_repo(args.repo)
    exts = {e.lower() for e in std["extensions"] if e.startswith(".")}
    if not exts:
        sys.exit("error: standard lists no dotted extensions; survey by extension not possible")
    words = [re.escape(m).replace(r"\ ", r"\s+") for m in std["markers"]]
    marker_rx = re.compile("|".join(rf"(?:{w})" for w in words), re.I)

    rows = []
    for repo in iter_pool_repos(args.max_depth):
        hits, dialect = scan_repo(repo, exts, marker_rx, args.min_markers)
        if hits == 0:
            continue
        url, commit = git_info(repo)
        lic, licfile = classify_license(repo)
        rows.append({
            "repo": str(repo.relative_to(POOL)),
            "ext_files": hits,
            "dialect_files": dialect,
            "commit": commit,
            "url": url,
            "license": lic,
            "license_file": licfile,
        })

    rows.sort(key=lambda r: (-r["dialect_files"], -r["ext_files"]))
    print(f"# pool candidates for '{args.lang}'  (ext files / >= {args.min_markers} markers)\n")
    print(f"{'dialect':>7} {'ext':>6}  {'license':<28} {'commit':<12} repo")
    for r in rows[: args.top]:
        print(f"{r['dialect_files']:>7} {r['ext_files']:>6}  "
              f"{(r['license'] or '—'):<28} {(r['commit'] or '—')[:12]:<12} {r['repo']}")

    out = repo_root / f".crucible-survey-{args.lang}.json"
    out.write_text(json.dumps({"standard": std, "candidates": rows}, indent=2))
    print(f"\nwrote {out}  ({len(rows)} candidate repos) — delete when done")


if __name__ == "__main__":
    main()
