# sqlite corpus sources

New category, added 2026-08-30. GitGalaxy treats `sqlite` as a language
distinct from generic `sql` — its own detection rules for `WITH RECURSIVE`,
`STRICT`/`WITHOUT ROWID`, JSONB / `->>` / `json_extract`, `RETURNING`,
`ON CONFLICT DO UPDATE`, `GENERATED ALWAYS AS`, window functions, FTS5
(`bm25`/`snippet`/`highlight`/`MATCH`), R-Tree, `PRAGMA journal_mode=WAL`,
`sqlite_master`, `CREATE TRIGGER`, `ATTACH DATABASE`, and the `.`-prefixed CLI
dot-commands (`.testcase`, `.load`, `.import`, `.output`, `.read`, `.shell`).
This folder set is real, unmodified `.sql` exercising those rules.

Every folder was copied directly from a same-named clone in the
`gitgalaxy/data` pool at the commit below, at copy time — all `exact`. See the
root `SOURCES.md` for the methodology and confidence levels.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `sqlite_cli_scripts` | 12 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | SQLite's own `test/*.sql` and `ext/wasm/sql/*` — `#!sqlite3` shebang, `#`-comment scripts, `.testcase`/`.open`/`.mode`/`.import`/`.load` dot-commands, plus the canonical recursive-CTE Mandelbrot and Sudoku solvers. |
| `mediawiki_sqlite_tables` | 11 | https://github.com/wikimedia/mediawiki | `8863834e673e4f297bfbc40cd4d54ee9027ad876` | GNU GPL v2.0 | The generated SQLite schema (`tables-generated.sql`) plus FTS3/no-FTS search-index variants and core `CREATE TABLE` patches. Dense DDL: constraints, `AUTOINCREMENT`, partial indexes. |
| `mediawiki_sqlite_alterpatches` | 19 | https://github.com/wikimedia/mediawiki | `8863834e673e4f297bfbc40cd4d54ee9027ad876` | GNU GPL v2.0 | `ALTER TABLE` / `ADD COLUMN` / `DROP` migration patches and index rebuilds — SQLite's limited-ALTER idioms (rebuild-and-swap), `PRAGMA` toggles around schema changes. |
| `sqitch_sqlite_engine` | 5 | https://github.com/sqitchers/sqitch | `0ab857e3bb5060e6feda0dd3e05ebb04f7aac85b` | MIT License | Sqitch's SQLite registry DDL and version-upgrade scripts: `PRAGMA foreign_keys=ON`, triggers, `BEGIN`/`COMMIT`, `CREATE VIEW`, schema-versioned migrations. |
| `prisma_sqlite_migrations` | 5 | https://github.com/prisma/prisma | `ada077ba32b5801d00d32f1434a45aaae7bc09a9` | Apache License 2.0 | Prisma-generated SQLite `migration.sql` fixtures: `PRAGMA foreign_keys`, `CREATE TABLE`/`CREATE UNIQUE INDEX`, the rename-table migration dance. |
| `prisma_typed_sql` | 17 | https://github.com/prisma/prisma | `ada077ba32b5801d00d32f1434a45aaae7bc09a9` | Apache License 2.0 | One-line parameterized queries (`SELECT \`col\` FROM \`TestModel\` WHERE id = ?`) — minimal files that isolate the `args` rule's `?`/`:name` positional/named-parameter detection and backtick-quoted identifiers. |
| `yii2_sqlite_schema` | 7 | https://github.com/yiisoft/yii2 | `9265980e089733f657609a37a95ab86176cb6c00` | BSD 3-Clause License | Yii2's SQLite migration schemas for its log / i18n / cache / RBAC / session subsystems, plus a test-fixture DB. `drop table if exists`, quoted identifiers, composite PKs. |
| `dancer2_sqlite` | 3 | https://github.com/PerlDancer/Dancer2 | `25176c5b860493b4a6dcda5bc12ecbefa67df716` | Perl 5 terms (Artistic-1.0-or-GPL-1.0-or-later) | The Dancer2 tutorial skeleton's `entries`/`users` table definitions — small, canonical `CREATE TABLE ... INTEGER PRIMARY KEY AUTOINCREMENT ... DEFAULT CURRENT_TIMESTAMP`. |
| `flask_tutorial_sqlite` | 3 | https://github.com/pallets/flask | `7ef2946fb5151b745df30201b8c27790cac53875` | BSD 3-Clause License | Flaskr tutorial `schema.sql` + test `data.sql`: `DROP TABLE IF EXISTS`, `FOREIGN KEY`, seed `INSERT`s. |

**Total: 82 files across 9 repo folder(s)** (9 exact).
