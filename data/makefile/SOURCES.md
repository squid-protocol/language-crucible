# makefile corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `freebsd` | 2 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD License | Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `cosmopolitan_build_mk` | 7 | https://github.com/jart/cosmopolitan | `eedf7d2db6e5ee0e228862690339c166a3f003a7` | ISC License | Cosmopolitan libc's per-directory `BUILD.mk` files: make rules built on `$(...)` package variables and `.PHONY` targets in 6 of 6, a generated-package style distinct from hand-written Makefiles. |
| `micropython_make` | 11 | https://github.com/micropython/micropython | `2dc2e30d98ee225070e990586526f8e43b3c95a2` | MIT License | MicroPython build files: top-level and example `Makefile`s plus the shared `.mk` includes (`py.mk`, `mkrules.mk`, `mkenv.mk`, `dynruntime.mk`, `extmod.mk`); `include`, `$(call ...)` or `.PHONY` constructs in 9 of 10 files. |

**Total: 20 files across 3 repo folder(s)** (2 exact, 1 content-verified).
