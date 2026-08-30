# `data/<lang>/SOURCES.md` format

Match the existing category files (`data/css/SOURCES.md`,
`data/assembly/SOURCES.md`, …). Structure:

```markdown
# <lang> corpus sources

<Preamble: one paragraph. State the confidence mix. If the category predates
the issue #4 audit, the older folders are `pool-reference` (pool name-match,
current commit recorded, not verified as the copied snapshot); folders you add
now are `exact` (you did the copy, from the commit below). If it's a brand-new
category, say so and that everything is `exact`. Link the root SOURCES.md for
methodology.>

<For a language with a non-obvious standard (sqlite vs sql, tcl's .test anchor),
add a sentence naming what the category actually targets and pointing at
gitgalaxy's language_standards.py.>

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `<folder>` | <N> | https://github.com/owner/repo | `<full 40-char sha>` | <exact license string> | <1–2 sentences: the SPECIFIC parsing boundary this folder tests — which markers / dialect quirk / era / architecture. This column is the reason the folder exists; make it concrete.> |
| ... | | | | | |

**Total: <N> files across <M> repo folder(s)** (<breakdown, e.g. "8 exact, 3 pool-reference, 1 unknown">).
```

## Notes-column examples (good)

- *"GLSL embedded in `<script type="x-shader/x-vertex">` blocks alongside
  `<script type="module">` import maps. Three languages in one file, none
  referencing the others by import."*
- *"`ALTER TABLE` / `ADD COLUMN` / `DROP` migration patches — SQLite's
  limited-ALTER idioms (rebuild-and-swap), `PRAGMA` toggles around schema
  changes."*
- *"6502 assembly for a modern CP/M port. `zproc`/`zendproc` macros,
  `.label`/`.include`, `<`/`>` byte selectors, `\` line comments — a non-x86,
  non-ARM dialect."*

## Notes-column anti-examples (too vague)

- ~~"Assembly files from nasm."~~
- ~~"Pre-existing corpus content."~~ (only OK verbatim on genuinely
  pre-existing `pool-reference` rows you're not touching)

## Preserving pre-existing rows

When growing an existing category, **keep the old rows verbatim** (including
their exact commit and "Pre-existing corpus content…" notes) and add yours
below them. Only bump the file count on an old row if the auditor's regenerated
`PROVENANCE.json` shows it changed — and then note the correction in the row and
the PR (as `python/fastapi` 446→240 was handled).

## Root `SOURCES.md`

One row: `| \`<lang>\` | <folders> | <files> | <confidence breakdown> | Audited | [\`data/<lang>/SOURCES.md\`](data/<lang>/SOURCES.md) |`
in alphabetical position. If the category was empty, also remove `<lang>` from
the "…additional `data/` directories currently hold no content…" sentence and
fix its count.
