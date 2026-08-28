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

| Repo folder | Files | Upstream | License | Notes |
|---|---|---|---|---|
| `redis` | 20 | https://github.com/redis/redis (`deps/lua`) | MIT License (Lua's own upstream license, vendored) | **Replaces prior mislabeled content** — this folder previously held only `eval.c`/`script_lua.c`/etc., Redis's C-side *embedding* of the Lua VM, not a single line of actual Lua. Now holds the real Lua 5.1-era reference test/demo suite (`fib.lua`, `sieve.lua`, `life.lua`, `sort.lua`, coroutine/closure tests) plus `etc/strict.lua`. |
| `cosmopolitan` | 45 | https://github.com/jart/cosmopolitan | ISC License (Cosmopolitan itself); vendored `third_party/lua` test suite carries Lua's own upstream copyright notice in-file (see e.g. `goto.lua`: "See Copyright Notice in file all.lua") | New. Official Lua 5.4 language conformance suite (`goto.lua`, `utf8.lua`, `bitwise.lua`, `coroutine.lua`, `gc.lua` — a newer dialect era than `redis`, exercising syntax that didn't exist in 5.1) plus real Redbean web-server demo scripts (routing, SQLite, crypto, HTTP). |
| `pandoc` | 25 | https://github.com/jgm/pandoc | GNU GPL v2.0-or-later | New. Pandoc's Lua filter/writer engine test fixtures and module API bindings (`pandoc.list`, `pandoc.path`, `pandoc.template`, etc.) plus top-level filter examples — real production document-processing Lua. |
| `freebsd-src` | 16 | https://github.com/freebsd/freebsd-src (`stand/lua`) | BSD (multiple clauses; see repo `LICENSE`) | New. The actual FreeBSD boot loader — `menu.lua`, `config.lua`, `loader.lua`, `cli.lua`, `drawer.lua`, `gfx-*.lua` — executed by `lualoader(8)` before the kernel is even running. All available `.lua` files included (man-page `.8`/`.5` files in the same directory were excluded, not Lua source). |
| `darwin-xnu` | 7 | https://github.com/apple/darwin-xnu | Apple Public Source License 2.0 | New. All available Lua files: kernel `dtrace`/`ktrace` scripting tools (`tools/trace/`) and VM/counter benchmark scripts (`tests/`). |

**Total: ~113 real Lua files across 5 repos** (up from 0 real Lua files — the prior `redis` folder was entirely mislabeled C).
