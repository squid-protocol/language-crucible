# dart corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `flutter` | 8 | https://github.com/flutter/flutter | `75910740753c13a858bb39c3686afb71675e8dc4` | BSD License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `dart_sdk_analyzer` | 13 | https://github.com/dart-lang/sdk | `eb59896079d9cda5351c2f713a22be89b9f9562c` | BSD-3-Clause | Dart SDK analyzer sources (pkg/analyzer/lib), sampled across the package: `Future` / `async` in 3 of 12 files and `abstract class` / `mixin` / `extension` in 2; compiler-tooling Dart, not Flutter widgets. |
| `dart_sdk_language_tests` | 13 | https://github.com/dart-lang/sdk | `eb59896079d9cda5351c2f713a22be89b9f9562c` | BSD-3-Clause | Dart SDK language tests (tests/language, files under 20 KB): a `main()` entry point in 11 of 12 files, and newer-syntax constructs (`abstract`, `mixin`, `extension`, `sealed`, `record`, `enum`) in 5. Small, syntax-focused programs. |

**Total: 34 files across 3 repo folder(s)** (2 exact, 1 pool-reference).
