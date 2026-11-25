# abap corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `abapGit` | 9 | https://github.com/abapGit/abapGit | `951e2243efbf0dbbfb4978a4ffa182b77e2ee939` | MIT License (from pool clone's LICENSE, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `abap2xlsx` | 18 | https://github.com/abap2xlsx/abap2xlsx | `f33b94c8efbe3f5228aa6bdb85ecedf25e0b5def` | Apache License 2.0 | abap2xlsx (Excel writer library, `src/` and `test/`): global `CLASS ... DEFINITION` in 13 of 17 files, `INTERFACE` in 3, and `FOR TESTING` local test classes in 2; includes `.clas.locals_def` / `.locals_imp` include files and `.intf.abap` interfaces. |
| `abapgit_objects_core` | 11 | https://github.com/abapGit/abapGit | `951e2243efbf0dbbfb4978a4ffa182b77e2ee939` | MIT License | abapGit object-handling core (src/objects/core): classes in 6 of 10 files, `FOR TESTING` test-class includes in 3, and function-group sources (`.fugr.*` top include, `SAPL...`, function modules) in 4, the procedural ABAP shape the class-only folders lack. |
| `abapgit_ui_pages` | 11 | https://github.com/abapGit/abapGit | `951e2243efbf0dbbfb4978a4ffa182b77e2ee939` | MIT License | abapGit GUI page classes (src/ui/pages): `CLASS ... DEFINITION` in 10 of 10 files, with a `.clas.locals_imp.abap` local-implementation include; HTML-rendering and event-routing class bodies. |

**Total: 49 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
