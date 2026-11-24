# postgresql corpus sources

Generated from `data/PROVENANCE.json` by `tools/generate_sources.py`.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `pgvector_extension` | 9 | https://github.com/pgvector/pgvector | `305e756a31e467fb5741ec997882c0f623300dce` | PostgreSQL License | pgvector extension upgrade scripts (sql/): every file opens with a psql `\echo ... \quit` guard line; `CREATE FUNCTION` appears in 3 of 8. |
| `pgvector_tests` | 8 | https://github.com/pgvector/pgvector | `305e756a31e467fb5741ec997882c0f623300dce` | PostgreSQL License | pgvector regression tests (test/sql). Only the 7 files the engine classifies as postgresql were kept; 7 plain-SQL test files that it classifies as db2_sql were left out. |

**Total: 17 files across 2 repo folder(s)** (2 exact).
