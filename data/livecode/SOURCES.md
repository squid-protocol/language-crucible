# LiveCode corpus sources

Expanded on 2026-08-28, same methodology as the other passes in this repo's
history: real, unmodified source from a full clone in the `gitgalaxy/data`
pool, selected with a directory-diverse sampler, scanned for GitGalaxy-forge
contamination markers (none found).

| Repo folder | Files | Upstream | License | Notes |
|---|---|---|---|---|
| `livecode` | 98 | https://github.com/livecode/livecode | GNU GPL v3.0 — LiveCode Community Edition, **with a special exception** granted for combining with ATL/OpenSSL on Windows/Linux builds; see the included `LICENSE` for the full carve-out | Replaces the prior `core` folder, which mixed a couple of real LiveCode-language files in with the engine's own C++ implementation (`drawing.cpp`, `Parser.cpp`, `script-execute.cpp`), build scripts (`.gyp`/`.sh`), and other non-LiveCode-language files. This folder is scoped to just the two actual LiveCode scripting languages: **`.livecodescript`** (the classic HyperCard-descended language — language-conformance tests from `tests/lcs/core/{engine,field,interface,strings,chunks,math,files,array,execution}` plus real IDE/installer/standalone-builder application scripts from `builder/`, `ide-support/`, and `engine/src/environment/`) and **`.lcb`** ("LiveCode Builder" — the newer, typed module-extension language — real standard-library modules from `libscript/src` plus its own test suite from `tests/lcb`). |

**Total: ~98 real LiveCode files** (63 `.livecodescript` + 35 `.lcb`), up from
2 genuine LiveCode-language files (the rest of the prior 13-file folder was
unrelated C++ engine source, now correctly excluded from this category).
