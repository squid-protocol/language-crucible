# PowerShell corpus sources

Expanded on 2026-08-28, same pass and methodology as `../shell/SOURCES.md`.
All files are real, unmodified source from full clones held in the
`gitgalaxy/data` pool, selected with a directory-diverse sampler and
scanned for GitGalaxy-forge contamination markers (none found).

| Repo folder | Files | Upstream | License | Notes |
|---|---|---|---|---|
| `core` | 28 unique | https://github.com/PowerShell/PowerShell | MIT License | Expanded from 7. Full available set is 552 files, but ~430 of those are near-uniform Pester `test/**/*.tests.ps1` fixtures — capped at a directory-diverse sample of 28 to stay proportionate with the rest of this pass rather than let one repo dominate the corpus. |
| `PowerToys` | 25 | https://github.com/microsoft/PowerToys | MIT License | New. Build/CI/packaging/signing PowerShell scripts. |
| `roslyn` | 25 | https://github.com/dotnet/roslyn | MIT License | New. .NET Compiler Platform build/test/release automation. |
| `runtime` | 25 | https://github.com/dotnet/runtime | MIT License | New. .NET runtime build/toolset scripts. |
| `nvda` | 14 unique | https://github.com/nvaccess/nvda | GNU GPL v2.0 | New. All available CI/build/test PowerShell scripts included. |

**Total: ~117 real PowerShell files across 5 repos** (up from 7 files / 1 repo).
