# sql corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `baseline` | 1 | unknown | unknown | unknown | No confidently-matched pool clone found. No local license file either. |
| `mysql` | 3 | unknown | unknown | unknown | No confidently-matched pool clone found. No local license file either. |
| `postgresql` | 3 | unknown | unknown | unknown | No confidently-matched pool clone found. No local license file either. |
| `sqlite` | 3 | https://github.com/sqlite/sqlite.git | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain (from pool clone's LICENSE.md, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |

**Total: 10 files across 4 repo folder(s)** (1 pool-reference, 3 unknown).
