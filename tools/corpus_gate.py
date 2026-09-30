#!/usr/bin/env python3
"""Corpus gate: enforces the rules in README.md, "Adding to the corpus".

Three checks, each a subcommand. CI runs all three on every pull request.

  policy     Every data/<category>/<folder>/ has a provenance entry, a recorded
             upstream source, a license this repo accepts, a license file in the
             folder, and a SOURCES.md row. Offline.

  immutable  Corpus files are never edited. Under data/, a change may only add,
             delete, or move a file unchanged, or replace it with another
             upstream version (verified by the upstream check). Offline;
             needs --base.

  upstream   Every file added under data/ is identical, apart from line
             endings, to a file in the upstream repository at the commit its
             folder records. Uses the GitHub API; needs --base (or --all to
             audit the whole corpus).

Folders that predate the gate and still break a policy rule are listed in
tools/corpus_gate_baseline.json. That list can only shrink: a new violation
fails, a fixed one must be removed from the list, and CI rejects additions.

Standard library only, so it runs in CI with no install step.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PROVENANCE = DATA / "PROVENANCE.json"
POLICY = ROOT / "tools" / "license_policy.json"
BASELINE = ROOT / "tools" / "corpus_gate_baseline.json"
BASELINE_REL = "tools/corpus_gate_baseline.json"

# The only paths under data/ that may be edited in place: generated metadata.
METADATA_RX = re.compile(
    r"^data/(PROVENANCE\.json|[^/]+/(SOURCES|PROVENANCE)\.md|[^/]+/[^/]+/PROVENANCE\.md)$"
)
LICENSE_FILE_RX = re.compile(r"licen[sc]e|copying|copyright|notice|unlicense", re.I)
COMMIT_RX = re.compile(r"^[0-9a-f]{40}$")
GITHUB_RX = re.compile(r"github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$")
POOL_SUFFIX_RX = re.compile(r" \(from pool clone's .*\)$")
ORIGINAL = "original"
REPO_WIDE = "*"  # stands in for a commit in waived no-source folders
CATEGORY_DOCS = ("SOURCES.md", "PROVENANCE.md")


def git(*args):
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True
    ).stdout


def load_provenance():
    return {e["path"]: e for e in json.loads(PROVENANCE.read_text())}


def load_policy():
    policy = json.loads(POLICY.read_text())
    labels = {k: v for k, v in policy["labels"].items() if not k.startswith("_")}
    return policy["accepted"], policy["rejected"], labels


def resolve_license(label, accepted, rejected, labels):
    """Return (status, spdx) where status is accepted / rejected / unknown."""
    if not label:
        return "unknown", None
    label = POOL_SUFFIX_RX.sub("", label)
    spdx = labels.get(label, label)
    parts = [p.strip() for p in spdx.split(" OR ")]
    if any(p in accepted for p in parts):
        return "accepted", spdx
    if any(p in rejected for p in parts):
        return "rejected", spdx
    return "unknown", spdx


def corpus_folders():
    """Yield (category, folder) for every data/<category>/<folder>/ directory."""
    for cat in sorted(p for p in DATA.iterdir() if p.is_dir()):
        for folder in sorted(p for p in cat.iterdir() if p.is_dir()):
            yield cat.name, folder.name


# --------------------------------------------------------------------------
# policy
# --------------------------------------------------------------------------

def policy_violations():
    prov = load_provenance()
    accepted, rejected, labels = load_policy()
    root_license = any(
        p.is_file() and LICENSE_FILE_RX.search(p.name) for p in ROOT.iterdir()
    )
    out = []
    seen = set()

    for cat in sorted(p for p in DATA.iterdir() if p.is_dir()):
        for loose in sorted(p for p in cat.iterdir() if p.is_file()):
            if loose.name not in CATEGORY_DOCS:
                out.append(("loose-file", f"data/{cat.name}/{loose.name}",
                            "corpus files must live in a source folder"))

    for cat, folder in corpus_folders():
        path = f"data/{cat}/{folder}"
        seen.add(path)
        entry = prov.get(path)
        if entry is None:
            out.append(("missing-entry", path, "no entry in data/PROVENANCE.json"))
            continue

        files = [p for p in (DATA / cat / folder).rglob("*") if p.is_file()]
        if entry.get("files") != len(files):
            out.append(("file-count", path,
                        f"entry says {entry.get('files')} files, folder has {len(files)}"))

        original = entry.get("origin") == ORIGINAL
        if not original and not (
            entry.get("url") and COMMIT_RX.match(entry.get("commit") or "")
        ):
            out.append(("no-source", path, "upstream url and 40-character commit required"))

        status, spdx = resolve_license(entry.get("license"), accepted, rejected, labels)
        if status == "unknown":
            out.append(("license-unknown", path,
                        f"license {entry.get('license')!r} is not a recognized SPDX id"))
        elif status == "rejected":
            out.append(("license-rejected", path, f"{spdx}: {rejected.get(spdx, 'not accepted')}"))

        has_file = any(LICENSE_FILE_RX.search(p.name) for p in files)
        if not has_file and not (original and root_license):
            out.append(("no-license-file", path, "no license file in the folder"))

        docs = [DATA / cat / name for name in CATEGORY_DOCS]
        if not (DATA / cat / folder / "PROVENANCE.md").is_file() and not any(d.is_file() and re.search(rf"`{re.escape(folder)}/?`", d.read_text(errors="ignore"))
                   for d in docs):
            out.append(("no-sources-row", path,
                        f"no row in data/{cat}/SOURCES.md and no PROVENANCE.md in the folder"))

    for path in sorted(set(prov) - seen):
        out.append(("stale-entry", path, "entry in PROVENANCE.json has no folder"))
    return out


def baseline_keys(text):
    return set(json.loads(text)["waived"]) if text.strip() else set()


def cmd_policy(args):
    violations = policy_violations()
    current = {f"{rule} {path}": msg for rule, path, msg in violations}

    if args.init_baseline:
        if BASELINE.exists():
            sys.exit("baseline already exists; it can only shrink (--prune-baseline)")
        write_baseline(sorted(current))
        print(f"wrote {len(current)} waivers to {BASELINE_REL}")
        return 0

    waived = baseline_keys(BASELINE.read_text()) if BASELINE.exists() else set()

    if args.prune_baseline:
        keep = sorted(waived & set(current))
        write_baseline(keep)
        print(f"baseline: {len(waived)} -> {len(keep)} waivers")
        waived = set(keep)

    failures = []
    for key in sorted(set(current) - waived):
        failures.append(f"{key}: {current[key]}")
    for key in sorted(waived - set(current)):
        failures.append(f"{key}: fixed, remove it from {BASELINE_REL} (--prune-baseline)")

    if args.base:
        try:
            base = baseline_keys(git("show", f"{args.base}:{BASELINE_REL}"))
        except subprocess.CalledProcessError:
            base = None  # the baseline is being introduced by this change
        if base is not None:
            for key in sorted(waived - base):
                failures.append(f"{key}: new waiver; the baseline may only shrink")

    print(f"policy: {len(list(corpus_folders()))} folders, "
          f"{len(current)} violations, {len(waived & set(current))} waived")
    return report("policy", failures)


def write_baseline(keys):
    BASELINE.write_text(json.dumps({
        "_about": "Folders that predate tools/corpus_gate.py and still break a policy "
                  "rule. This list may only shrink. Fix the folder, then run "
                  "`python3 tools/corpus_gate.py policy --prune-baseline`.",
        "waived": keys,
    }, indent=2) + "\n")


# --------------------------------------------------------------------------
# immutable
# --------------------------------------------------------------------------

def raw_diff(base):
    """Yield (status, dst_mode, dst_sha, old_path, new_path) for data/ changes."""
    out = git("diff", "--raw", "-z", "--no-abbrev", "-M100%", f"{base}...HEAD", "--", "data")
    fields = out.split("\0")
    i = 0
    while i < len(fields) and fields[i]:
        meta = fields[i].lstrip(":").split()
        dst_mode, dst_sha, status = meta[1], meta[3], meta[4]
        if status[0] in "RC":
            yield status, dst_mode, dst_sha, fields[i + 1], fields[i + 2]
            i += 3
        else:
            yield status, dst_mode, dst_sha, fields[i + 1], fields[i + 1]
            i += 2


def cmd_immutable(args):
    failures = []
    counts = {"added": 0, "deleted": 0, "moved": 0, "replaced": 0}
    for status, mode, _sha, old, new in raw_diff(args.base):
        if METADATA_RX.match(new) and METADATA_RX.match(old):
            continue
        if status == "D":
            counts["deleted"] += 1
        elif status == "A":
            counts["added"] += 1
            if mode != "100644":
                failures.append(f"{new}: mode {mode}; corpus files must be plain, "
                                "non-executable files")
        elif status in ("R100", "C100"):
            counts["moved"] += 1
        elif status == "M" and mode == "100644":
            # Replacing a file with another upstream version is allowed. The
            # upstream check then requires the new content to match upstream,
            # so an edited file still fails there.
            counts["replaced"] += 1
        elif status[0] in "RC":
            failures.append(f"{old} -> {new}: moved and edited; corpus files may only "
                            "be moved unchanged")
        else:
            failures.append(f"{new}: edited in place ({status}); corpus files are "
                            "read-only. Add, move or delete files instead")
    print(f"immutable: {counts['added']} added, {counts['deleted']} deleted, "
          f"{counts['moved']} moved, {counts['replaced']} replaced (checked by upstream)")
    return report("immutable", failures)


# --------------------------------------------------------------------------
# upstream
# --------------------------------------------------------------------------

class GitHub:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    def _request(self, path, method):
        """Return the response body for 200, None for 404. Anything else raises."""
        req = urllib.request.Request(f"https://api.github.com/{path}", method=method)
        req.add_header("Accept", "application/vnd.github+json")
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        error = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return resp.read()
            except urllib.error.HTTPError as e:
                if e.code in (404, 409, 422):
                    return None
                error = f"HTTP {e.code}"
                if e.code < 500:
                    break  # auth or rate limit: retrying will not help
            except (urllib.error.URLError, TimeoutError) as e:
                error = str(e)
            time.sleep(2 ** attempt)
        raise RuntimeError(f"GitHub API {error} for {path}")

    def blob_exists(self, repo, sha):
        return self._request(f"repos/{repo}/git/blobs/{sha}", "HEAD") is not None

    def tree(self, repo, commit):
        """Blob hashes at a commit: (set, complete). None if the commit is missing."""
        body = self._request(f"repos/{repo}/git/trees/{commit}?recursive=1", "GET")
        if body is None:
            return None
        data = json.loads(body)
        shas = {t["sha"] for t in data.get("tree", []) if t.get("type") == "blob"}
        return shas, not data.get("truncated", False)


def added_files(base):
    for status, _mode, sha, _old, new in raw_diff(base):
        if status in ("A", "M") or status[0] in "RC":
            if not METADATA_RX.match(new):
                yield new, sha


def all_files():
    """Every corpus file, hashed as it is on disk (so uncommitted work counts)."""
    paths = [p for p in git("ls-files", "--", "data").splitlines() if not METADATA_RX.match(p)]
    paths = [p for p in paths if (ROOT / p).is_file()]
    hashes = subprocess.run(
        ["git", "-C", str(ROOT), "hash-object", "-w", "--stdin-paths"],
        input="\n".join(paths) + "\n", capture_output=True, text=True, check=True,
    ).stdout.split()
    return list(zip(paths, hashes))


def candidate_hashes(sha):
    """The file's hash as stored, plus its hash with LF line endings.

    Upstreams that check out with CRLF give copies that differ from the stored
    blob only in line endings. That is still an unmodified copy.
    """
    raw = subprocess.run(["git", "-C", str(ROOT), "cat-file", "blob", sha],
                         capture_output=True, check=True).stdout
    if b"\r\n" not in raw:
        return [sha]
    lf = subprocess.run(["git", "hash-object", "--stdin"],
                        input=raw.replace(b"\r\n", b"\n"),
                        capture_output=True, check=True).stdout.decode().strip()
    return [sha, lf]


def cmd_upstream(args):
    prov = load_provenance()
    gh = GitHub()
    waived = baseline_keys(BASELINE.read_text()) if BASELINE.exists() else set()
    failures = []
    by_repo = {}  # (owner/repo, commit) -> [(path, sha)]

    for path, sha in (all_files() if args.all else added_files(args.base)):
        parts = path.split("/")
        if len(parts) < 4:
            continue  # loose files are reported by the policy check
        folder = "/".join(parts[:3])
        if args.only and not any(folder == o or folder.startswith(o + "/") for o in args.only):
            continue
        entry = prov.get(folder)
        if entry is None:
            failures.append(f"{path}: folder has no entry in data/PROVENANCE.json")
            continue
        if entry.get("origin") == ORIGINAL:
            continue
        m = GITHUB_RX.search(entry.get("url") or "")
        if not m:
            failures.append(f"{path}: upstream {entry.get('url')!r} is not a GitHub "
                            "repository, so it cannot be verified")
            continue
        commit = entry.get("commit") or ""
        if not COMMIT_RX.match(commit):
            if f"no-source {folder}" not in waived:
                failures.append(f"{path}: folder records no 40-character commit")
                continue
            commit = REPO_WIDE  # waived legacy folder: match anywhere in the repo
        by_repo.setdefault((f"{m.group(1)}/{m.group(2)}", commit), []).append((path, sha))

    # Strict: anything that cannot be verified counts as a failure.
    def check_repo(item):
        (repo, commit), files = item
        out = []
        try:
            if commit == REPO_WIDE:
                for path, sha in files:
                    if not any(gh.blob_exists(repo, h) for h in candidate_hashes(sha)):
                        out.append(f"{path}: not identical to any file in {repo}")
                return out
            tree = gh.tree(repo, commit)
            if tree is None:
                return [f"{repo}: recorded commit {commit} not found upstream"]
            at_commit, complete = tree
            for path, sha in files:
                hashes = candidate_hashes(sha)
                if any(h in at_commit for h in hashes):
                    continue
                if any(gh.blob_exists(repo, h) for h in hashes):
                    if complete:
                        out.append(f"{path}: in {repo}, but not at the recorded commit "
                                   f"{commit[:12]}; record the commit it was copied from")
                    continue  # tree too large to list: repository-wide match accepted
                out.append(f"{path}: not identical to any file in {repo}")
        except RuntimeError as e:
            out.append(f"{repo}: could not verify {len(files)} file(s): {e}")
        return out

    with ThreadPoolExecutor(4) as ex:
        for result in ex.map(check_repo, sorted(by_repo.items())):
            failures.extend(result)

    n = sum(len(v) for v in by_repo.values())
    print(f"upstream: {n} files checked against {len(by_repo)} upstream commits")
    return report("upstream", failures)


def report(name, failures):
    if not failures:
        print(f"{name}: OK")
        return 0
    for f in failures:
        print(f"  FAIL {f}")
    print(f"{name}: {len(failures)} failure(s)")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("policy", help="provenance and license rules (offline)")
    p.add_argument("--base", help="git ref; reject waivers not present there")
    p.add_argument("--init-baseline", action="store_true", help="create the baseline once")
    p.add_argument("--prune-baseline", action="store_true", help="drop fixed waivers")
    p.set_defaults(func=cmd_policy)

    p = sub.add_parser("immutable", help="no edits to corpus files (offline)")
    p.add_argument("--base", required=True, help="git ref to diff against")
    p.set_defaults(func=cmd_immutable)

    p = sub.add_parser("upstream", help="added files match upstream at the recorded commit")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--base", help="git ref; check files added since it")
    g.add_argument("--all", action="store_true", help="audit every corpus file")
    p.add_argument("--only", nargs="*", help="limit to these data/<category>[/<folder>] paths")
    p.set_defaults(func=cmd_upstream)

    args = ap.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
