# PR body template

```markdown
<!-- If stacked on an open coverage PR: -->
**Stacks on #<N>** (`<branch>`) — review/merge that first; this PR's diff
collapses to just the <lang> content once #<N> lands. Retarget to `main` if
#<N> is closed.

### ⚠️ Quarantine Protocol
- [x] Zero execution — additions are `<.ext .ext …>` source + upstream `LICENSE` files only. No build steps.
- [x] Pure structure — every folder targets specific parser detection rules (below).
- [x] No malicious payloads.
- [x] Permission bits — new files carry none.

### Why

<1–3 sentences: what state the category was in (empty / N folders / M files),
what the language's standard in gitgalaxy/standards/language_standards.py
actually detects, and why the pool material was chosen to exercise it. If the
language has a confusable sibling (sql/sqlite, assembly/agc_assembly), say which
you filled and why.>

### `data/<lang>/` — <new category | 3 → 16 folders, 15 → 253 files>

| Folder | Boundary it tests | Source (license) |
|---|---|---|
| `<folder>` | <markers / dialect quirk> | <repo> (<license>) |
| ... | | |

<If capped below the requested size:> The pool holds ~<N> real `.<ext>` files
for this language total — the category is capped there. **No synthetic files
were added.**

### Source & License

All <K> new folders were copied directly from the same-named clone in the
`gitgalaxy/data` pool at a pinned `HEAD`, so recorded `exact` in
`EXACT_PROVENANCE` (`tools/independent_data_auditor.py`) — full table in
`data/<lang>/SOURCES.md`. Licenses: <list>. <Any `unknown`/KNOWN_UNKNOWN folder
+ why.>

- **`data/<lang>/SOURCES.md` row(s) added:** yes; root `SOURCES.md` updated.

### Provenance regen

`data/PROVENANCE.json` regenerated with
`python3 tools/independent_data_auditor.py data --provenance` (stable on
re-run). <If an unrelated folder's count changed: name it and say it's
pre-existing drift between the committed JSON and tree, corrected here.>

### Golden master

Not touched. Regenerating `gitgalaxy`'s `golden_master_*` fixtures and bumping
the `LANGUAGE_CRUCIBLE_REF` pin is the separate coordinated step in
`RELEASING.md`, for when this lands and a tag is cut.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Commit message footer (per the crucible repo's convention):

```
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```
