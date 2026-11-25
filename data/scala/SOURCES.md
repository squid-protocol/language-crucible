# scala corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `kafka` | 8 | https://github.com/apache/kafka | `eb111f6695ef30889e7367bbad759f7e772d65ea` | Apache License 2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `cobrix_scala` | 13 | https://github.com/AbsaOSS/cobrix | `7200b77cdebb4244137f88b48e908acfc4ccbee1` | Apache License 2.0 | Cobrix COBOL data-source library sampled across its modules: `case class` / `trait` / `object` in 6 of 12 files; Spark-oriented Scala, and a COBOL-adjacent code base. |
| `gradle_scala` | 11 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Gradle's own Scala sources: `class` declarations in 8 of 10 files, `case class` / `trait` / `object` in 3; build-tooling Scala unlike `kafka` and `cobrix_scala`. |

**Total: 32 files across 3 repo folder(s)** (2 exact, 1 pool-reference).
