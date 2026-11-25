# fortran corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `wrf` | 15 | https://github.com/wrf-model/WRF | `f15568ccc1447780e3bd664b9f0196edd784bf33` | Public Domain | Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `wrf_physics` | 11 | https://github.com/wrf-model/WRF | `f15568ccc1447780e3bd664b9f0196edd784bf33` | Public Domain | WRF physics modules (phys/, `.F` files): `MODULE` in 8 of 10 files, `SUBROUTINE` in 8, `USE` statements in 7, and C-preprocessor directives in 6. Fixed/free-form Fortran with CPP, a physics counterpart to `wrf`. Capped by the pool: no other licensed Fortran repo is in it. |
| `fpm_fortran` | 13 | https://github.com/fortran-lang/fpm | `ffe90aeea703820596bc58149f76f3c50a668819` | MIT License | Fortran Package Manager sources (`.f90`): `use` statements in 8 of 12 files, `program` units in 10, and `module` / derived `type` definitions in 3; modern Fortran application code. |
| `stdlib_fortran` | 13 | https://github.com/fortran-lang/stdlib | `7a87e3e23f44fb9ec3b4532d22c2c101950e4a6b` | MIT License | Fortran stdlib example programs (`.f90`; the library itself is `.fypp` templates, which are not Fortran source): `program` and `use` statements in 12 of 12 files. Small main-program Fortran, unlike the module-heavy WRF code. |

**Total: 52 files across 4 repo folder(s)** (3 exact, 1 content-verified).
