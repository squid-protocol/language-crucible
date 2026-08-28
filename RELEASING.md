# Releasing / tagging this repo

This repo has exactly one git tag, `v1.0` (cut 2026-07-03). That tag matters
more than a normal "version number" would: **GitGalaxy's own CI pins to it by
name.** This document exists so cutting the next tag is a deliberate,
informed decision — not something that happens accidentally, and not
something that silently breaks GitGalaxy's CI when it does happen.

## Why this isn't automatic

Two workflows in the separate `squid-protocol/gitgalaxy` repo hardcode
`--branch v1.0` when cloning this corpus:

- **`.github/workflows/golden-crucible.yml`** — the `crucible-audit` job that
  runs on every GitGalaxy PR, matrixed across full-precision and
  zero-dependency modes. It clones this repo at `v1.0` and diffs the scan
  output against two checked-in fixtures,
  `tests/golden_master_audit.json` and `tests/golden_master_zero_dep_audit.json`.
- **`.github/workflows/release-crucible-archive.yml`** — runs on a GitGalaxy
  release, clones this repo at `v1.0` (same string, same comment: "same as
  CI"), scans it, and opens an automated PR back into this repo archiving the
  scan output under `raw_output/<release-tag>/`.

**Cutting a new tag here does nothing on its own.** There is no dynamic
"latest tag" resolution — both workflows have to be edited to point at the
new tag, in that other repo, or GitGalaxy's CI keeps testing against `v1.0`
forever regardless of what lands on this repo's `main`.

## The full checklist, in order

Skipping the order below is the failure mode to avoid: bump the pin before
regenerating the fixtures, and GitGalaxy's own `crucible-audit` job breaks on
the very next PR that touches the parsing engine.

1. **Batch, don't tag per-PR.** A tag bump is a checkpoint, not a changelog
   entry. Let multiple content-addition PRs land on `main` first.
2. **In `gitgalaxy`**, with a local checkout of this repo's `main` at the
   commit you intend to tag: regenerate both golden-master fixtures against
   it —
   ```bash
   python3 tests/tools/update_golden_master.py --yes
   # or, per tests/README.md's documented shortcut:
   python3 tests/tools/crucible_check.py --update --yes
   ```
   Do this once per dependency mode (full-precision / zero-dependency) —
   `update_golden_master.py` only updates whichever fixture matches your
   currently-installed packages. Review the diff it prints before confirming;
   `golden-master-guard.yml` will flag (non-blockingly) that these fixtures
   changed on the resulting PR, and the PR description needs to explain why.
3. **Here**, cut the tag against the commit that was just blessed:
   ```bash
   git tag -a vX.Y -m "..." <commit>
   git push origin vX.Y
   ```
   Write real release notes: summarize what's new since the last tag by
   category, and link the relevant `data/<language>/SOURCES.md` rows as the
   audit trail (see root [`SOURCES.md`](SOURCES.md)).
4. **In `gitgalaxy`**, bump both hardcoded `--branch v1.0` strings (in
   `golden-crucible.yml` and `release-crucible-archive.yml`) to `vX.Y`, in a
   PR that references the fixture-regeneration PR from step 2.

Steps 2 and 4 happen in a different repository than this one — treat them as
a coordinated cross-repo change, not something to do unilaterally from this
side.

## Where things stand right now

`v1.0` → `main` is currently 16 commits behind, including:

- The security-perimeter/PR-template chores (`75ce1f6`, `285b997`, `344448b`).
- Two README rewrites (`433e7be`, `f71a531`) explaining the golden-master
  mechanism and repositioning why this repo exists.
- Two automated `raw_output/` baseline archives from GitGalaxy releases
  (`9d37ebc` v2.4.5, `dbcc23a` v2.4.6) — these came from
  `release-crucible-archive.yml` and don't themselves require a tag bump
  here, since they're read-only artifacts about a past scan, not corpus
  content GitGalaxy's tests scan against.
- Three large real-content additions: COBOL/JCL (`b0703a7`), shell/PowerShell
  (`e184f7b`), and Lua/LiveCode (`4ded4fe`) — plus this provenance-audit pass.

That's a substantial, coherent batch — a reasonable point to consider cutting
`v1.1`, but that's a call for whoever owns this repo to make deliberately,
following the checklist above, not something done as a side effect of a
content PR.

## A known limitation worth a future issue

The pin being a literal hardcoded string in two workflow files, with no
"latest release" resolution, means this checklist has to be followed by hand
every time. A future improvement in `gitgalaxy` — e.g. reading the pinned tag
from a single config value, or resolving "latest tag" at CI time with an
explicit opt-out for pinning to a specific one — would remove step 4 from
this list entirely. That's out of scope for this repo to implement; noting
it here so it isn't lost.
