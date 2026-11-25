# yacc corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `freebsd` | 3 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD License | Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `freebsd_yacc_lex` | 13 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD License | FreeBSD base-system yacc/lex pairs (devd, hastd, setkey, m4, ar, libipsec): `%%` sections in 12 of 12 files, `%union` in 5, and flex start-condition / `%option` declarations in 9. Complements `freebsd` (config.y, jailparse.y). |
| `gnucobol_cobc` | 4 | https://github.com/paulsmith/gnucobol | `d139d06201cf0aba9d143e0f675f446c19603b36` | GPL-3.0-or-later | GnuCOBOL compiler front end: the preprocessor grammar (`ppparse.y`) and the two flex scanners (`pplex.l`, `scanner.l`). bison `%union` / `%token` in 1 of 3 and flex `%option` / start conditions in 3 of 3. `parser.y` is omitted (about 400 KB, over the 60 KB cap). GPL-3.0-or-later. |
| `prometheus_goyacc` | 4 | https://github.com/prometheus/prometheus | `cb3382314d63ed457279c9582cd6db63d0a06631` | Apache License 2.0 | Prometheus PromQL goyacc grammar (`generated_parser.y`) plus two lexer `.l` files (`promlex.l`, `openmetricslex.l`): a Go-embedded yacc grammar with `%union` / `%token`, and lexers with `%option` / start conditions. |
| `sqlite_lemon` | 3 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain | SQLite Lemon grammars (`fts5parse.y`, `lemon-test01.y`): the Lemon dialect (`%token_type`, `%syntax_error`, `%extra_argument`, `%type`) in 2 of 2 files, a different grammar syntax from bison/yacc. Public domain. |

**Total: 27 files across 5 repo folder(s)** (4 exact, 1 content-verified).
