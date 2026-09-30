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
   The `SOURCES.md` tables are generated from `PROVENANCE.json` by
   `python3 tools/generate_sources.py`; never hand-edit a table row except its Notes cell.
   Unlicensed sources are **not added**: the license must be on the accept list in
   `tools/license_policy.json`, and the upstream license file is copied into the folder.
   (`KNOWN_UNKNOWN` holds only the folders that predate this rule.)
3. **Content comes from the source pool** (`gitgalaxy/data/` on the dev machine, a local-only
   directory of full clones) — not from ad-hoc downloads.
4. **Cross-repo PRs carry a "Cross-repo" note** (companion PR links, merge order, what re-runs
   after) — see the ecosystem doc's PR convention.
5. **Never edit a file under `data/`.** Corpus files are add / delete / move-unchanged / replace-with-upstream only,
   and every added or replaced file must be identical (line endings aside) to a file in the
   upstream repo at the commit its folder records.
   Only `data/PROVENANCE.json` and the per-category `SOURCES.md` / `PROVENANCE.md` are editable.
6. **The corpus gate must pass** — `python3 tools/corpus_gate.py policy`, `immutable --base
   origin/main` and `upstream --base origin/main` (README, "Adding to the corpus"). Never add a
   line to `tools/corpus_gate_baseline.json`; it only shrinks.

## Skills

Skills live in `.claude/skills/` (`.agents/skills` is a symlink to the same directory):
**`expand-language-coverage`** — the 10-step workflow for filling a `data/<lang>/` category from
the pool (`tools/survey_pool.py` to mine candidates, `tools/stage_folder.py` to copy + license +
flatten + size-cap + draft provenance).
