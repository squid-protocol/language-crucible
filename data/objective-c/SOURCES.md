# objective-c corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `worldwideweb` | 7 | https://github.com/simonw/1991-WWW-NeXT-Implementation.git | `032807bfe9b77b434c638667cba051be50047b23` | LicenseRef-Public-Domain | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `afnetworking` | 16 | https://github.com/AFNetworking/AFNetworking | `d9f589cc2c1fe9d55eb5eea00558010afea7a41e` | MIT | AFNetworking library sources (tests and examples excluded): `@implementation` in 15 of 15 files and `@interface` in 14, with blocks and category-heavy networking code. MIT, verified from the license text. |
| `godot_ios` | 7 | https://github.com/godotengine/godot | `4a919adccf8e398aceca75399c539078c54fe97f` | MIT | Godot Engine's iOS platform layer: `.mm` Objective-C++ in all 6 files, mixing C++ with Objective-C (`@interface` / `@implementation` in 3 of 6). MIT, verified from the license text. |
| `tensorflow_lite_objc` | 11 | https://github.com/tensorflow/tensorflow | `c21c40c048e9b35d032d31ce41809c2cadeb8fca` | Apache License 2.0 | TensorFlow Lite's Objective-C API: `@implementation` in 8 of 10 files, `NS_ASSUME_NONNULL` annotations, and 2 `.mm` Objective-C++ files; includes a small test app. Apache-2.0. |

**Total: 41 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
