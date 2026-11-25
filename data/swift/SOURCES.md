# swift corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `alamofire` | 8 | https://github.com/Alamofire/Alamofire | `36f1747e31305e0cfda27864091318950c66a5b1` | MIT | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `ghostty_macos` | 13 | https://github.com/ghostty-org/ghostty | `debcffbadb75221a030319c075fae12cfe114176` | MIT License | Ghostty's macOS app sources: AppKit and SwiftUI view code (`SwiftUI` views in 3 of 12 files, `@MainActor` / `@Published` in 2). Files with spaces in their paths were skipped. |
| `vapor_sources` | 13 | https://github.com/vapor/vapor | `ff88583e10f02aa47be49e632d5179f89e855e03` | MIT License | Vapor server framework (Sources/Vapor): `protocol` / `extension` declarations in 10 of 12 files and `async` / `await` code in 4; server-side Swift, a different domain from `alamofire`. |
| `swift_argument_parser` | 13 | https://github.com/apple/swift-argument-parser | `d225b6fe8aed45478d1e36e770bf269c5d48d3a9` | Apache License 2.0 | swift-argument-parser sources: `@Argument` / `@Option` / `@Flag` / `ParsableCommand` property-wrapper code in 7 of 12 files and `protocol` / `extension` in 9; a property-wrapper-driven library style. |
| `swift_nio_core` | 13 | https://github.com/apple/swift-nio | `b003027fc38b649a43e9aad77c3d4e4a2c5b6997` | Apache License 2.0 | SwiftNIO sources sampled across the package: `protocol` / `extension` declarations in 8 of 12 files, `async` / `Sendable` concurrency in 7, and `@inlinable` / `public struct` API surface in 7. Low-level networking Swift. |

**Total: 60 files across 5 repo folder(s)** (4 exact, 1 pool-reference).
