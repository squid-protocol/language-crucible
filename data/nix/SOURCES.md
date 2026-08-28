# nix corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `bun` | 3 | https://github.com/oven-sh/bun | `1cc837687b1d1f8d558a40110fbe3e61cc41fbcd` | MIT License (from pool clone's LICENSE.md, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. 1 deeper same-named git clone(s) also found (likely vendored copies within other projects, not used): /srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/bun. |
| `ghostty` | 6 | https://github.com/ghostty-org/ghostty | `debcffbadb75221a030319c075fae12cfe114176` | MIT License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |

**Total: 9 files across 2 repo folder(s)** (2 pool-reference).
