# PowerShell corpus sources

Expanded on 2026-08-28, same pass and methodology as `../shell/SOURCES.md`.
All files are real, unmodified source from full clones held in the
`gitgalaxy/data` pool, selected with a directory-diverse sampler and
scanned for GitGalaxy-forge contamination markers (none found).

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `core` | 28 unique | https://github.com/PowerShell/PowerShell | `a17f1761eca57d90856062e35add0f013a1c703f` | MIT License | Expanded from 7. Full available set is 552 files, but ~430 of those are near-uniform Pester `test/**/*.tests.ps1` fixtures — capped at a directory-diverse sample of 28 to stay proportionate with the rest of this pass rather than let one repo dominate the corpus. |
| `PowerToys` | 25 | https://github.com/microsoft/PowerToys | `4ce451edd0a66ba4fe1366ff6a912c30be59feb3` | MIT License | New. Build/CI/packaging/signing PowerShell scripts. |
| `roslyn` | 25 | https://github.com/dotnet/roslyn | `849bed61024b171e673b9a1fac565b30e3ae1934` | MIT License | New. .NET Compiler Platform build/test/release automation. |
| `runtime` | 25 | https://github.com/dotnet/runtime | `aba46e33ea5ddd45d90e5c6a8b46bba6744ddc9a` | MIT License | New. .NET runtime build/toolset scripts. |
| `nvda` | 14 unique | https://github.com/nvaccess/nvda | `a94c7f85bd2e8e3e290b314244ea921c4cd01b4c` | GNU GPL v2.0 | New. All available CI/build/test PowerShell scripts included. |

**Total: ~117 real PowerShell files across 5 repos** (up from 7 files / 1 repo).

Commits above are the exact `HEAD` of the corresponding clone in the
`gitgalaxy/data` pool at the moment these files were copied (2026-08-28).
