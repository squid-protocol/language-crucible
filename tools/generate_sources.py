#!/usr/bin/env python3
"""Rebuild the SOURCES.md tables from data/PROVENANCE.json.

data/PROVENANCE.json is the source of truth. This rewrites, from it:

  - the table and the "**Total: ...**" line in every data/<category>/SOURCES.md
    (creating the file for a category that has none), and
  - the "## Categories" table in the root SOURCES.md.

Everything else in those files is hand-written and left alone: the prose above
and below each table, the history after each Total line, and the Notes column
of every existing row. The one exception is the generated "No
confidently-matched pool clone found" note, which is replaced once a folder's
source has been verified.

  python3 tools/generate_sources.py           rewrite the files
  python3 tools/generate_sources.py --check   exit 1 if any file is out of date (CI)
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
HEADER = "| Repo folder | Files | Upstream | Commit | License | Notes |"
SEPARATOR = "|---|---|---|---|---|---|"
ROW_RX = re.compile(r"^\| `([^`]+)` \| ")
TOTAL_RX = re.compile(r"^\*\*Total: [^*]*\*\*(?: \([^)]*\))?(.*)$")
STALE_NOTE_RX = re.compile(r"^No confidently-matched pool clone found\.")
LEVELS = ("exact", "content-verified", "pool-reference", "original", "unknown")
ROOT_ROW_RX = re.compile(r"^\| `([^`]+)` \| .*\| ([^|]+) \| \[`data/")


def load():
    by_cat = collections.defaultdict(list)
    for e in json.loads((DATA / "PROVENANCE.json").read_text()):
        by_cat[e["category"]].append(e)
    for entries in by_cat.values():
        entries.sort(key=lambda e: e["repo"])
    return dict(sorted(by_cat.items()))


def summary(entries):
    counts = collections.Counter(e["confidence"] for e in entries)
    parts = [f"{counts[k]} {k}" for k in LEVELS if counts[k]]
    return ", ".join(parts)


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def row(e, notes):
    if e.get("origin") == "original":
        upstream, commit = "none (original work)", "n/a"
    else:
        upstream = e["url"] or "unknown"
        commit = f"`{e['commit']}`" if e["commit"] else "not recorded"
    return (f"| `{e['repo']}` | {e['files']} | {upstream} | {commit} | "
            f"{cell(e['license'] or 'unknown')} | {notes} |")


def existing_notes(lines):
    notes = {}
    for line in lines:
        m = ROW_RX.match(line)
        if m:
            cells = line.strip()[2:-2].split(" | ", 5)
            if len(cells) == 6:
                notes[m.group(1)] = cells[5].strip()
    return notes


def render_category(cat, entries, old_text):
    lines = old_text.splitlines() if old_text else []
    notes = existing_notes(lines)
    # Keep the table's existing (curated) row order; new folders go last.
    order = {repo: i for i, repo in enumerate(notes)}
    entries = sorted(entries, key=lambda e: (order.get(e["repo"], len(order)), e["repo"]))
    rows = []
    for e in entries:
        note = notes.get(e["repo"], "")
        verified = e["confidence"] in ("content-verified", "original")
        if (not note or STALE_NOTE_RX.match(note)) and e.get("note"):
            note = cell(e["note"])
        elif verified and e.get("note") and cell(e["note"]) not in note:
            note = f"{note} {cell(e['note'])}".strip()
        rows.append(row(e, note))
    files = sum(e["files"] for e in entries)
    total = (f"**Total: {files} files across {len(entries)} repo folder(s)** "
             f"({summary(entries)}).")
    table = [HEADER, SEPARATOR, *rows]

    if not lines:
        return "\n".join([
            f"# {cat} corpus sources", "",
            "Generated from `data/PROVENANCE.json` by `tools/generate_sources.py`.", "",
            *table, "", total, "",
        ])

    try:
        start = lines.index(HEADER)
    except ValueError:
        return "\n".join(lines + ["", *table, "", total]) + "\n"
    end = start + 1
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    tail = lines[end:]
    # Replace the Total line that follows the table, keeping any history after it.
    for i, line in enumerate(tail):
        if not line.strip():
            continue
        m = TOTAL_RX.match(line)
        if m:
            tail[i] = total[:-1] + (m.group(1) if m.group(1).strip(" .") else ".")
        else:
            tail[:i] = ["", total]
        break
    else:
        tail = ["", total]
    out = lines[:start] + table + tail
    return "\n".join(out) + ("\n" if old_text.endswith("\n") else "")


def render_root(by_cat, old_text):
    lines = old_text.splitlines()
    status = {}
    for line in lines:
        m = ROOT_ROW_RX.match(line)
        if m:
            status[m.group(1)] = m.group(2).strip()
    start = lines.index("| Category | Repo folders | Files | Confidence | Status | Details |")
    end = start + 2
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    rows = [
        f"| `{cat}` | {len(es)} | {sum(e['files'] for e in es)} | {summary(es)} | "
        f"{status.get(cat, 'Audited')} | [`data/{cat}/SOURCES.md`](data/{cat}/SOURCES.md) |"
        for cat, es in by_cat.items()
    ]
    out = lines[:start + 2] + rows + lines[end:]
    return "\n".join(out) + ("\n" if old_text.endswith("\n") else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if any file is out of date")
    args = ap.parse_args()

    by_cat = load()
    targets = {}
    for cat, entries in by_cat.items():
        path = DATA / cat / "SOURCES.md"
        old = path.read_text() if path.exists() else ""
        targets[path] = (old, render_category(cat, entries, old))
    root = ROOT / "SOURCES.md"
    old = root.read_text()
    targets[root] = (old, render_root(by_cat, old))

    stale = [p for p, (old, new) in targets.items() if old != new]
    if args.check:
        for p in stale:
            print(f"  FAIL {p.relative_to(ROOT)} is out of date with data/PROVENANCE.json")
        print(f"sources: {len(targets)} files, {len(stale)} out of date")
        if stale:
            print("run `python3 tools/generate_sources.py` and commit the result")
        return 1 if stale else 0
    for p in stale:
        p.write_text(targets[p][1])
    print(f"sources: rewrote {len(stale)} of {len(targets)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
