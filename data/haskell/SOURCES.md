# haskell corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `pandoc` | 12 | https://github.com/jgm/pandoc.git | `7777de6adb166d92b4c9ee4b24054637ab8477b7` | GNU GPL v2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `pandoc_writers` | 11 | https://github.com/jgm/pandoc | `7777de6adb166d92b4c9ee4b24054637ab8477b7` | GPL-2.0-or-later | Pandoc's output writers (src/Text/Pandoc/Writers): `module` / `LANGUAGE` pragmas in 10 of 10 files, `OverloadedStrings` in 9, and typed function signatures (`::` with `->`) in 9. Recorded GPL-2.0-or-later (file headers say "GNU GPL, version 2 or above"). |
| `aeson_core` | 13 | https://github.com/haskell/aeson | `aafea1f4c2d4dfb5a0f068fab50bf8254256f25f` | BSD-3-Clause | aeson JSON library sampled across the package: `LANGUAGE` pragmas in 11 of 12 files, `instance` / `class` declarations in 4, and extension-heavy code (`TemplateHaskell`, `DeriveGeneric`, `GADTs`, `TypeFamilies`) in 5. |
| `xmonad_core` | 13 | https://github.com/xmonad/xmonad | `1ed7242e2b05dc1a5e2c88e7ef130288680e89c3` | BSD-3-Clause | xmonad window manager sampled across the package: `module` / `LANGUAGE` headers in 12 of 12 files and `data` / `newtype` / `class` / `instance` declarations in 4; compact application Haskell, a second repo beside `pandoc`. |

**Total: 49 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
