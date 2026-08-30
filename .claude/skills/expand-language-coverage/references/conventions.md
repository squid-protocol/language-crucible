# Crucible content conventions

## Folder naming

`data/<lang>/<folder>/` where `<folder>` is `<project>_<flavor>`:

- `<project>` — the upstream repo (lowercased, `.`/`-` ok): `threejs`, `revealjs`,
  `mediawiki`, `cosmopolitan`, `nasm`.
- `<flavor>` — the sub-dialect / subsystem / boundary: `_shader_examples`,
  `_test_fixtures`, `_syscalls`, `_aarch64`, `_css_modules`, `_generated_asm`.

One folder ≈ one upstream repo. A big repo may become several folders, one per
subsystem (`cosmopolitan_syscalls`, `cosmopolitan_runtime`; `mediawiki_sqlite_tables`,
`mediawiki_sqlite_alterpatches`). Don't merge two upstreams into one folder —
provenance is per-folder.

To keep flattened filenames short, point `--src` at the deepest common
directory (`--src corpus_perl/sqitch/lib/App/Sqitch/Engine`), not the repo root.
`stage_folder.py` flattens the path *relative to `--src`*, so a shallow `--src`
over a deep `--find` produces long `a_b_c_d_Thing.groovy` names. When several
matching files live under `.../src/main/groovy/<pkg>/`, aim `--src` at that
`groovy/` (or `<pkg>/`) directory and use `--find "-name '*.groovy'"`.

## Sizing bands (files per category, for calibration)

| Band | Examples | Aim for |
|---|---|---|
| tiny | `protobuf` 1, `makefile` 2, `text` 1 | only if the pool truly has nothing |
| small | `csharp` 7, `ruby` 8, `kotlin` 7 | a first pass at a niche language |
| medium | `rust` 49, `typescript` 46, `xml` 24 | a solid category |
| large | `python` ~295, `cobol` 308, `shell` 282 | "very large" / flagship coverage |

Per-folder: ~5–25 files is typical. Existing folders range 1–70.

## What to exclude

- **Anything you'd hand-write.** No synthetic files, ever. If the pool can't
  reach the target size with real files, cap the category and say so in the PR.
- **Files > ~60 KB** and multi-MB auto-generated blobs (`window3.test` was 5 MB).
  `stage_folder.py` drops them; don't override without reason.
- **Vendored third-party copies** inside a repo when the real upstream is also
  in the pool (e.g. `corpus_php/WordPress` vs top-level `wordpress`). Exception:
  a folder that is *deliberately* about vendored code (`cytoscape_docs` = a repo
  carrying CSS it didn't author) — call that out in the notes.
- **Binaries, minified bundles you don't want, lockfiles, generated maps**
  unless the folder's whole point is "machine-generated output" (say so).
- **Ambiguous provenance:** if `survey_pool.py` / the auditor flags two
  same-named git clones at the same depth, pick by reading file contents and
  record which and why (see `MANUAL_OVERRIDE` in the auditor for prior cases).

## Extension gotchas

- `.test` is Tcl by *content anchor*, not extension — it lives in `data/tcl/`.
- `.inc` is in the `assembly` extension list and several others.
- `.s` vs `.S` (cpp-preprocessed) both count as assembly.
- `.sql` is claimed by both `sql` and `sqlite` — the `sqlite` standard
  disambiguates on dialect markers + neighbouring `.db`/`.sqlite` files.
- `.vp` (ChrysaLisp), `.cs` (Capstone test format) etc. are **not** in any
  standard's extension list — the engine won't classify them, skip them.

## Licensing

Copy the upstream's `LICENSE`/`COPYING` file **verbatim** into the folder,
under its original name. Classify it with one of the exact strings in
`license-classification.md`. No license file in the upstream at all →
`KNOWN_UNKNOWN` with a one-sentence reason, never a guess.
