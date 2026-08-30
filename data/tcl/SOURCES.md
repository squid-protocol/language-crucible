# tcl corpus sources

Provenance is mixed. The `sqlite` folder at the top predates the issue #4 audit
(squid-protocol/language-crucible#4) and is `pool-reference`. The eight folders
below it were added 2026-08-30 as a Tcl-coverage expansion — copied directly
from same-named pool clones at a known commit, so `exact`.

Tcl here means the `.test` / `.tcl` files themselves: GitGalaxy's `tcl`
standard drops `.test` from its extension list but keeps it as a content
*anchor*, and carries a "SQLite mega-sensor" (`do_test`, `do_execsql_test`,
`do_catchsql_test`, `finish_test`, `tcltest::`). The SQLite test suite is the
canonical stress case for that; `macports_*` adds real application Tcl
(TclOO-ish `port` API, `registry` layer) that isn't a test harness at all. See
the root `SOURCES.md` for methodology and confidence levels.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `sqlite` | 13 | https://github.com/sqlite/sqlite.git | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain (from pool clone's LICENSE.md, not found locally) | Pre-existing corpus content — fuzz harnesses, `tester.tcl`, `all.test`. Provenance identified during the issue #4 audit (2026-08-28) by pool name-match; see root `SOURCES.md` for what 'pool-reference' does and doesn't guarantee. |
| `macports_port_api` | 20 | https://github.com/macports/macports-base | `81fb1d2acda818f1075dd2196b650466dbd35117` | BSD 3-Clause License | `src/port1.0/` — the MacPorts `Portfile` DSL implementation: `namespace eval`, `proc`, `option`/`options` metaprogramming, `ui_*` callbacks, heavy `eval`/`uplevel`/`upvar`. Real Tcl, no test harness. |
| `macports_registry` | 10 | https://github.com/macports/macports-base | `81fb1d2acda818f1075dd2196b650466dbd35117` | BSD 3-Clause License | `src/registry2.0/` — the installed-port registry/receipts layer: SQLite-backed state via Tcl bindings, file-tracking, dependency graph walks. |
| `sqlite_core_dml` | 21 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `select`/`insert`/`update`/`delete`/`join` regression `.test` files: `do_test name { db eval { ...SQL... } } {expected}` — Tcl harness wrapping SQL string blocks, the polyglot boundary. |
| `sqlite_query_planner` | 18 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `where*.test`, `analyze*.test`, `autoindex*.test` — `do_eqp_test` (EXPLAIN QUERY PLAN assertions), `optimization_control`, planner-cost fixtures. |
| `sqlite_cte_window` | 15 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `with*.test` and `window*.test` — recursive CTEs and window-function tests (the multi-megabyte auto-generated `window3.test`/`window8.test` were excluded as corpus bloat). |
| `sqlite_json_triggers` | 19 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `json*.test`, `trigger*.test`, `view.test` — `json_extract`/`->>`, `json_each`/`json_tree` in `db eval`, `CREATE TRIGGER ... BEGIN ... END` inside Tcl strings. |
| `sqlite_fts5` | 23 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `ext/fts5/test/fts5*.test` — full-text-search: `MATCH`, `bm25()`, `snippet()`, `highlight()`, custom tokenizers, `do_faultsim_test`. |
| `sqlite_rtree` | 17 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | `ext/rtree/*.test` — R-Tree virtual tables, `geopoly_*`, spatial-join fixtures, `do_ioerr_test`. |

**Total: 156 files across 9 repo folder(s)** (8 exact, 1 pool-reference).
