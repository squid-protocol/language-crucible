# Releasing / tagging this repo

This repo is currently tagged at `v1.1.0` (`v1.0` was cut 2026-07-03,
`v1.1.0` on 2026-08-28).<sup>†</sup> The tag matters more than a normal
"version number" would:
**GitGalaxy's own CI pins to it.** This document exists so cutting the next
tag is a deliberate, informed decision — not something that happens
accidentally, and not something that silently breaks GitGalaxy's CI when it
does happen.

## How the pin works (updated 2026-08-28)

Bumping `v1.0` → `v1.1.0` found the pin hardcoded in **eleven** separate
places across the `gitgalaxy` repo: six workflow files' `git clone --branch`
steps (not the two this document originally described — `tri-comparison-
audit.yml`, `tri-comparison-history.yml`, `tree-sitter-accuracy-audit.yml`,
and `tree-sitter-accuracy-history.yml` also clone this corpus and had drifted
onto the same literal, undocumented anywhere), plus ~7 purely-informational
mentions in docs and script error messages. That's now been consolidated
into two sources of truth in `gitgalaxy`, not eleven:

- **`LANGUAGE_CRUCIBLE_REF`** — a GitHub Actions repository variable on
  `squid-protocol/gitgalaxy`. Every workflow that clones this corpus reads
  `${{ vars.LANGUAGE_CRUCIBLE_REF }}` instead of a literal tag.
- **`tests/_crucible_pin.py`**'s `PINNED_TAG` constant — mirrors the variable
  for local tooling and human-facing messages (a GitHub Actions variable
  isn't importable from a local pytest run or a docstring).

**Cutting a new tag here still does nothing on its own.** Nothing
auto-detects a new release of this repo; both of the above still have to be
updated by hand in `gitgalaxy`. What's changed is that it's now exactly two
edits instead of potentially eleven silently-missed ones.

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
   currently-installed packages. Review the diff it prints before confirming.
   **Before running either command**, check `git status` (and, if a local
   sibling `../language-crucible` checkout is what `LANGUAGE_CRUCIBLE_PATH`
   resolves to, check that checkout's `git status` too) — untracked or
   ignored artifacts sitting in the corpus checkout get scanned and can
   silently poison the fixture (see `gitgalaxy`'s
   `.claude/rules/golden-master-guidelines.md`). `golden-master-guard.yml`
   will flag (non-blockingly) that these fixtures changed on the resulting
   PR, and the PR description needs to explain why.
3. **Here**, cut the tag against the commit that was just blessed:
   ```bash
   git tag -a vX.Y -m "..." <commit>
   git push origin vX.Y
   ```
   Write real release notes: summarize what's new since the last tag by
   category, and link the relevant `data/<language>/SOURCES.md` rows as the
   audit trail (see root [`SOURCES.md`](SOURCES.md)).
4. **In `gitgalaxy`**, in a PR that references the fixture-regeneration PR
   from step 2:
   ```bash
   gh variable set LANGUAGE_CRUCIBLE_REF --body vX.Y --repo squid-protocol/gitgalaxy
   ```
   and update `tests/_crucible_pin.py`'s `PINNED_TAG` to match. Grep that
   repo for the old tag string as a final check — a new workflow could always
   have hardcoded a fresh literal since the last bump instead of using the
   variable.

Steps 2 and 4 happen in a different repository than this one — treat them as
a coordinated cross-repo change, not something to do unilaterally from this
side.

## Where things stand right now

`v1.1.0` was cut 2026-08-28 against `main`, covering everything through the
COBOL/JCL, shell/PowerShell, Lua/LiveCode corpus expansions and the
issue-#4 provenance audit — see the
[release notes](https://github.com/squid-protocol/language-crucible/releases/tag/v1.1.0)
and root [`SOURCES.md`](SOURCES.md) for the full breakdown. `gitgalaxy`'s pin
has been bumped to match (PR
[squid-protocol/gitgalaxy#2398](https://github.com/squid-protocol/gitgalaxy/pull/2398)),
along with the source-of-truth consolidation described above.

<sup>†</sup> A `v1.10` tag briefly existed for a few hours the same day,
before any GitHub Release was published against it — a two-part-version
naming slip, corrected to proper three-part semver before it was consumed
anywhere beyond the still-open gitgalaxy PR above (which was updated to
match). Deleted rather than kept around as a real prior release.

## A known limitation worth a future issue

The pin is still a value someone has to update by hand in two places in
`gitgalaxy` — a GitHub Actions variable and a Python constant, not
automatically discovered. A future improvement there — e.g. resolving
"latest tag" at CI time with an explicit opt-out for pinning to a specific
one — would remove step 4 from this list entirely. That's out of scope for
this repo to implement; noting it here so it isn't lost.
