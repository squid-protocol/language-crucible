# AGENTS.md — language-crucible

Vendor-neutral guidance for any coding agent working in this repo. Repo-specific rules live
here; the multi-repo picture lives in the gitgalaxy engine repo's **`docs/ecosystem.md`**
(canonical constellation map — repos, skills inventory, cross-repo workflow merge ordering, PR
conventions). Read that before cross-repo work.

## What this repo is

The **GitGalaxy Language Crucible**: a zero-execution structural-parser benchmark corpus —
`data/<language>/<repo-folder>/<files>` copied from licensed sources, per-category `SOURCES.md`
tables, and machine-readable `data/PROVENANCE.json`. The gitgalaxy engine's CI pins this corpus
to a **release tag** (`LANGUAGE_CRUCIBLE_REF` GH Actions variable + `tests/_crucible_pin.py`)
and diffs its golden masters against it.

## Hard rules

1. **Adding corpus content does NOT update gitgalaxy's fixtures.** That is a separate,
   cross-repo release step — `RELEASING.md` here, then gitgalaxy's
   `docs/self_scan/BUMPING_THE_CRUCIBLE_PIN.md`. Never assume a data PR alone changes what CI
   tests against.
2. **Provenance is not optional.** Every `data/` folder needs a `SOURCES.md` row and a
   `PROVENANCE.json` entry; regenerate with
   `GITGALAXY_POOL_PATH=<pool> python3 tools/independent_data_auditor.py data --provenance`.
   Unlicensed sources are recorded `unknown` (via `KNOWN_UNKNOWN`), never silently included.
3. **Content comes from the source pool** (`gitgalaxy/data/` on the dev machine, a local-only
   directory of full clones) — not from ad-hoc downloads.
4. **Cross-repo PRs carry a "Cross-repo" note** (companion PR links, merge order, what re-runs
   after) — see the ecosystem doc's PR convention.

## Skills

Skills live in `.claude/skills/` (`.agents/skills` is a symlink to the same directory):
**`expand-language-coverage`** — the 10-step workflow for filling a `data/<lang>/` category from
the pool (`tools/survey_pool.py` to mine candidates, `tools/stage_folder.py` to copy + license +
flatten + size-cap + draft provenance).
