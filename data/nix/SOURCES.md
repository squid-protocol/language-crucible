# nix corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `bun` | 4 | https://github.com/oven-sh/bun | `1cc837687b1d1f8d558a40110fbe3e61cc41fbcd` | MIT License (from pool clone's LICENSE.md, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. 1 deeper same-named git clone(s) also found (likely vendored copies within other projects, not used): /srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/bun. |
| `ghostty` | 6 | https://github.com/ghostty-org/ghostty | `debcffbadb75221a030319c075fae12cfe114176` | MIT License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `angular_nix` | 8 | https://github.com/angular/angular | `9d76ac82290e047f1481fb38bd95233e951a77de` | MIT License | Angular's Nix files: `pkgs` / `mkShell` / `stdenv`-style expressions in 7 of 7 files, a dev-shell and packaging use of Nix unlike `bun` and `ghostty`. |

**Total: 18 files across 3 repo folder(s)** (1 exact, 2 pool-reference).
