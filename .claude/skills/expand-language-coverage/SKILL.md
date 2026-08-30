---
name: expand-language-coverage
description: >-
  Add or grow a language category in the GitGalaxy Language Crucible corpus
  (all_language_repo / squid-protocol/language-crucible). Use when asked to
  "add <language> to the crucible", "expand <language> coverage", "populate
  data/<lang>/", "get more <lang> test examples into all_language_repo", or to
  seed a new empty category. Pulls real, unmodified source from the
  gitgalaxy/data pool, records exact provenance, regenerates PROVENANCE.json,
  updates every SOURCES.md, and opens a PR. Presents a scope plan for approval
  before copying anything.
---

# Expand language coverage in the Language Crucible

The crucible (`all_language_repo`, GitHub `squid-protocol/language-crucible`) is
a **zero-execution structural-parser benchmark corpus**. Each `data/<language>/`
category holds folders of real, unmodified source snippets from notable OSS
repos, deliberately disconnected from their build systems. GitGalaxy's engine
scans it and diffs the output against golden-master fixtures.

Your job with this skill: take one language, fill or grow `data/<lang>/` with
files that **exercise that language's detection rules**, record where every
file came from, and open a reviewable PR — without ever writing a synthetic
source file.

## Non-negotiables

- **Real source only.** Every file is copied verbatim from a clone in the
  `gitgalaxy/data` pool. Never hand-write or synthesize a `.sql`/`.s`/etc.
  file to pad a category. If the pool can't support the size you want, cap the
  category and say so.
- **Every file's origin is recorded** as `exact` provenance (you are doing the
  copy, from a known commit) — or `unknown` with a written reason if the
  upstream ships no license.
- **Don't touch golden-master fixtures.** Regenerating `gitgalaxy`'s
  `tests/golden_master_*.json` and bumping the tag pin is a separate,
  cross-repo step (`RELEASING.md`). This skill stops at an open PR.
- **Size discipline.** Skip files larger than ~60 KB and multi-MB
  auto-generated blobs — they bloat the golden master and can trip CI's 15 s
  ReDoS timeout, causing local/CI diffs. `stage_folder.py` enforces this.
- **Commit only relevant files.** Never `git add -A` here.

## Environment

| Thing | Default | Override |
|---|---|---|
| Crucible checkout | current dir (walks up for `data/PROVENANCE.json`) | `--repo` |
| Full-repo pool | `/srv/storage_16tb/projects/gitgalaxy/data` | `GITGALAXY_POOL_PATH` |
| Language standards | `/srv/storage_16tb/projects/gitgalaxy/v6/gitgalaxy/standards/language_standards.py` | `GITGALAXY_STANDARDS` |

The two helper scripts live in `tools/` next to this file:
`survey_pool.py` (discovery) and `stage_folder.py` (copy + provenance draft).

## Workflow

### 1. Read the language's detection standard

The corpus exists to exercise `LANGUAGE_DEFINITIONS["<lang>"]` in
`language_standards.py`. Before anything else, look at that entry:

```
python3 .claude/skills/expand-language-coverage/tools/survey_pool.py <lang> --standard-only
```

This prints the language's `extensions`, `exact_matches`, `shebangs`, and the
**signature markers** it mined from the `rules` regexes (e.g. for `sqlite`:
`WITH RECURSIVE`, `STRICT`, `json_extract`, `bm25`, `PRAGMA journal_mode`, the
`.`-dot-commands…). Those markers are what "dialect-correct" means — a folder
of files that only hit `SELECT`/`FROM` isn't testing `sqlite`, it's testing
generic `sql`. Also note extension collisions (`.test` is Tcl-by-anchor, not by
extension; `.inc` is assembly *and* others).

If the standard has a distinct sibling (`sql` vs `sqlite`, `assembly` vs
`agc_assembly`), decide which category you're actually filling and why.

### 2. Check the current state of the category

- `data/<lang>/` — exists? how many folders / files? Read
  `data/<lang>/SOURCES.md` if present.
- Root `SOURCES.md` — the category's row (or its listing in the "hold no
  content" line if empty).
- Skim `README.md` and `RELEASING.md` for current conventions.
- Compare category sizes: look at what "small" (`makefile` 2, `protobuf` 1) vs
  "large" (`cobol` 308, `shell` 282, `python` ~295) look like, and pick a
  target band.

### 3. Survey the pool

```
python3 .claude/skills/expand-language-coverage/tools/survey_pool.py <lang>
```

For every top-level repo clone **and** every `corpus_*/<repo>` sub-clone, this
reports: files matching the language's extensions, how many of those also
contain ≥2 signature markers (dialect-correct candidates), the repo's `HEAD`
commit, remote URL, and a classified license. It writes a JSON manifest
scaffold to `.crucible-survey-<lang>.json` in the repo root (gitignored-safe
name — delete it when done).

Then dig by hand into the top candidates — `find`, `grep` for the markers,
read a few files. You are looking for repos where the target language appears
*in its natural dialect*, ideally several repos covering different
sub-dialects / eras / architectures / frameworks.

### 4. Design the folder set — and get it approved

Draft a plan: one folder per upstream repo (or per subsystem of a big one),
each named `<project>_<flavor>` (see `references/conventions.md`), each chosen
to stress a **distinct parsing boundary**. For each folder note: source repo,
~how many files, which markers/boundary it covers, license.

Present this to the user with `AskUserQuestion` (options: proceed as scoped /
adjust size / different sources). **Do not copy anything before approval.**
After approval, run the rest autonomously through to an open PR — only stop for
an unexpected failure.

### 5. Stage each folder

For every approved folder:

```
python3 .claude/skills/expand-language-coverage/tools/stage_folder.py \
  --lang <lang> --folder <folder_name> \
  --src <pool-path-to-repo-or-subdir> \
  --license <pool-path-to-that-repo's-LICENSE> \
  --find "-name '*.ext' -size -60k"   # or: --files a.ext sub/b.ext ...
  [--limit 22]
```

It copies the curated files into `data/<lang>/<folder>/` (flattening nested
paths into `_`-joined names, deduping basenames, skipping >60 KB and binaries),
copies the LICENSE file verbatim, strips exec bits, and prints:

- the file list actually copied,
- a ready-to-paste `EXACT_PROVENANCE` line (URL + commit resolved from the
  repo's `.git`), and
- a skeleton `SOURCES.md` table row.

Repos with **no** license file: `stage_folder.py` still copies the source, and
prints a `KNOWN_UNKNOWN` skeleton instead — fill in the reason.

Spot-check: open 2–3 copied files per folder. Confirm they're dialect-correct
(hit the markers), not truncated, not binary.

### 6. Record provenance

- Paste the `EXACT_PROVENANCE` / `KNOWN_UNKNOWN` lines into
  `tools/independent_data_auditor.py` (keep them grouped under a dated
  comment, as prior expansions did).
- Regenerate the machine-readable index:
  ```
  GITGALAXY_POOL_PATH=<pool> python3 tools/independent_data_auditor.py data --provenance
  ```
- Run it **twice** — the second run must leave `git status` clean for
  `data/PROVENANCE.json` (stable output).
- Diff `data/PROVENANCE.json` against `HEAD`: the only changes should be your
  new rows. If an *unrelated* folder's `files` count changed, that's
  pre-existing drift between the committed JSON and the committed tree — note
  it in the PR (as the fastapi 446→240 correction was noted), don't try to
  hide it.

### 7. Update the SOURCES.md files

- **`data/<lang>/SOURCES.md`** — create it if the category is new (match the
  format in `references/sources-md-template.md`). One row per folder:
  `folder | files | upstream URL | commit | license | notes`. The **notes**
  column is the point — one or two sentences naming the *specific parsing
  boundary* that folder tests (which markers, which dialect quirk). Preamble
  states the confidence mix; end with the `**Total: N files across M repo
  folder(s)** (…)` line.
- **Root `SOURCES.md`** — update the category's row (folder count, file count,
  confidence breakdown). If it was empty: remove it from the "hold no content"
  sentence and insert a table row in alphabetical position.

### 8. Verify

- Auditor stable (step 6 re-run).
- `git status` — only your new folders + the 4 expected file edits
  (`SOURCES.md`, `data/PROVENANCE.json`, `data/<lang>/SOURCES.md`,
  `tools/independent_data_auditor.py`).
- No exec bits: `find data/<lang> -type f -perm -u+x` → empty.
- Largest new file well under 60 KB (LICENSE files excepted).

### 9. Branch, commit, PR

- Branch `feature/<lang>-coverage` off `main`. If a prior coverage PR is still
  open and this builds on it, stack on that branch and set the PR base
  accordingly (note the stacking in the PR body).
- Commit only the relevant paths (list them explicitly).
- Commit message: summary line + per-folder one-liners + the provenance-regen
  note + "golden master not touched — separate step per RELEASING.md".
  Footer:
  ```
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
  ```
- `gh pr create` — body follows `references/pr-body-template.md`: the
  Quarantine Protocol checklist, the per-folder boundary table, a Source &
  License section, the provenance-regen note, and the golden-master note.

### 10. Hand off

Tell the user: PR link, folder/file counts, any category cap you hit and why,
any provenance drift you surfaced, and the reminder that the maintainer runs
the `gitgalaxy` golden-master regen + tag-pin bump when it lands
(`RELEASING.md`).

## Reference files

- `references/conventions.md` — folder naming, sizing bands, what to exclude
  (vendored copies, generated blobs, ambiguous provenance).
- `references/license-classification.md` — the exact license strings this repo
  uses, and how to read a LICENSE header to pick one.
- `references/sources-md-template.md` — the per-category `SOURCES.md` format.
- `references/pr-body-template.md` — the PR description structure.
