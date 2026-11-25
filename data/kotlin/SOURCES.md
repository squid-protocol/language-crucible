# kotlin corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `okhttp` | 7 | https://github.com/square/okhttp | `c396b08f7a06e412c4cc8f5c83b0d7ed19f7fa6c` | Apache License 2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `gradle_kotlin` | 13 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Gradle build-logic and subproject `src/main` Kotlin: class / interface / object declarations in 3 of 12 files and the rest top-level functions and DSL-style code, a build-tooling dialect unlike the library code in `okhttp` and `retrofit_kotlin`. |
| `retrofit_kotlin` | 17 | https://github.com/square/retrofit | `77e6ba21d9ba372d1b23ef29881912910da23347` | Apache License 2.0 | Retrofit's Kotlin sources and tests: `suspend` functions in 5 of 16 files, plus extension functions (`KotlinExtensions.kt`) and `inline` / reified helpers. Small library-style Kotlin, a second repo beside `okhttp`. |
| `spring_boot_kotlin` | 15 | https://github.com/spring-projects/spring-boot | `5cecd3922fce651f13d16a85d8a29efaa7f44cfd` | Apache License 2.0 | Spring Boot's Kotlin sources outside the docs tree (core, modules and the coroutines smoke test): annotations in 14 of 14 files, with Kotlin classes, objects and `data class` declarations driven by Spring annotations. |

**Total: 52 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
