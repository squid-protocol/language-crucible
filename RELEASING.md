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
   commit you intend to tag: work through
   [`docs/self_scan/BUMPING_THE_CRUCIBLE_PIN.md`](https://github.com/squid-protocol/gitgalaxy/blob/main/docs/self_scan/BUMPING_THE_CRUCIBLE_PIN.md)
   end to end. That single checklist — not this document — is the source of
   truth for the `gitgalaxy`-side steps; it covers five separate things that
   need regenerating together (golden masters, tri-comparison chart/ledger,
   tree-sitter-accuracy chart/history, and any stale tree-sitter-accuracy
   baselines), the prerequisites that have caused real CI failures when
   skipped (a differently-named local checkout baking a wrong `corpus_path`
   into a baseline; an untracked cache directory poisoning a fixture; the
   Arduino-ctags shadowing trap), and stops with the golden masters blessed
   but the pin not yet flipped — do not skip ahead to step 4 below before
   that checklist says so.
3. **Here**, cut the tag against the commit that was just blessed:
   ```bash
   git tag -a vX.Y.Z -m "..." <commit>
   git push origin vX.Y.Z
   ```
   Write real release notes (`gh release create vX.Y.Z --notes-file ...`,
   not just an annotated tag message — the release notes are what's publicly
   visible): summarize what's new since the last tag by category, and link
   the relevant `data/<language>/SOURCES.md` rows as the audit trail (see
   root [`SOURCES.md`](SOURCES.md)). Use proper three-part semver
   (`vX.Y.Z`) — a two-part tag was tried once and had to be corrected before
   it stuck (see the footnote below).
4. **Back in `gitgalaxy`**, finish `BUMPING_THE_CRUCIBLE_PIN.md`'s remaining
   steps: bump `LANGUAGE_CRUCIBLE_REF` and `tests/_crucible_pin.py`'s
   `PINNED_TAG` together, grep for the old tag string as a final check, push,
   and confirm CI actually passes before merging.

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
