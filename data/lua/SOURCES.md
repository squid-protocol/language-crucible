# Lua corpus sources

Expanded on 2026-08-28, same methodology as the COBOL/JCL and shell/PowerShell
passes: real, unmodified source from full clones in the `gitgalaxy/data` pool,
selected with a directory-diverse sampler, scanned for GitGalaxy-forge
contamination markers (none found).

The `gitgalaxy/data` pool has comparatively little dedicated Lua content —
no large standalone Lua project (Neovim, OpenResty, LÖVE, etc.) was in the
pool — so this pass prioritized quality and genuine diversity of *use case*
over repo count: two different eras of the official Lua language test suite
(5.1 vendored in Redis, 5.4 vendored in Cosmopolitan), real production
scripting (Pandoc document filters, a Redbean web server), and a genuinely
unusual embedding (Lua running pre-kernel-boot as a BIOS/UEFI loader menu
system).

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `redis` | 22 | https://github.com/redis/redis | `2ba0194fbe5820cab8602bfa633a7d27e97cabdd` | MIT License (vendored) | **Replaces prior mislabeled content** — this folder previously held only `eval.c`/`script_lua.c`/etc., Redis's C-side *embedding* of the Lua VM, not a single line of actual Lua. Now holds the real Lua 5.1-era reference test/demo suite (`fib.lua`, `sieve.lua`, `life.lua`, `sort.lua`, coroutine/closure tests) plus `etc/strict.lua`. |
| `cosmopolitan` | 46 | https://github.com/jart/cosmopolitan | `eedf7d2db6e5ee0e228862690339c166a3f003a7` | ISC License | New. Official Lua 5.4 language conformance suite (`goto.lua`, `utf8.lua`, `bitwise.lua`, `coroutine.lua`, `gc.lua` — a newer dialect era than `redis`, exercising syntax that didn't exist in 5.1) plus real Redbean web-server demo scripts (routing, SQLite, crypto, HTTP). |
| `pandoc` | 27 | https://github.com/jgm/pandoc | `7777de6adb166d92b4c9ee4b24054637ab8477b7` | GNU GPL v2.0-or-later | New. Pandoc's Lua filter/writer engine test fixtures and module API bindings (`pandoc.list`, `pandoc.path`, `pandoc.template`, etc.) plus top-level filter examples — real production document-processing Lua. |
| `freebsd-src` | 17 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD (multiple clauses) | New. The actual FreeBSD boot loader — `menu.lua`, `config.lua`, `loader.lua`, `cli.lua`, `drawer.lua`, `gfx-*.lua` — executed by `lualoader(8)` before the kernel is even running. All available `.lua` files included (man-page `.8`/`.5` files in the same directory were excluded, not Lua source). |
| `darwin-xnu` | 8 | https://github.com/apple/darwin-xnu | `2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32` | Apple Public Source License 2.0 | New. All available Lua files: kernel `dtrace`/`ktrace` scripting tools (`tools/trace/`) and VM/counter benchmark scripts (`tests/`). |

**Total: 120 files across 5 repo folder(s)** (5 exact).

Commits above are the exact `HEAD` of the corresponding clone in the
`gitgalaxy/data` pool at the moment these files were copied (2026-08-28).
Note `freebsd-src` and `darwin-xnu` share the same clones (and therefore the
same commit hashes) as their entries in `../shell/SOURCES.md` — the same
pool checkout, with different subdirectories selected for each language.
