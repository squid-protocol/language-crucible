# csharp corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `roslyn` | 7 | https://github.com/dotnet/roslyn | `849bed61024b171e673b9a1fac565b30e3ae1934` | MIT | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `powershell_commands_utility` | 13 | https://github.com/PowerShell/PowerShell | `a17f1761eca57d90856062e35add0f013a1c703f` | MIT License | PowerShell's utility cmdlets (Microsoft.PowerShell.Commands.Utility): `[Cmdlet(...)]` / `[Parameter]` attribute-driven classes in 8 of 12 files; attribute-heavy declarative C#. |
| `powertoys_common` | 13 | https://github.com/microsoft/PowerToys | `4ce451edd0a66ba4fe1366ff6a912c30be59feb3` | MIT License | PowerToys shared libraries (src/common): `namespace` / `struct` declarations in 12 of 12 files, Windows-app utility code. A desktop-app C# style distinct from `roslyn` and the runtime. |
| `runtime_linq` | 13 | https://github.com/dotnet/runtime | `aba46e33ea5ddd45d90e5c6a8b46bba6744ddc9a` | MIT License | .NET runtime System.Linq (src/libraries): generic `IEnumerable<T>` / `Func<>` code in 8 of 12 files, static extension-method classes and `yield return` iterators in 6. Library-internal C# with heavy generics, unlike the compiler code in `roslyn`. |

**Total: 46 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
