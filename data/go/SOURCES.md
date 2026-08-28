# go corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `core` | 9 | https://github.com/golang/go | `d247ed00e498e9717fb7c80d126bee5a8afdb4e8` | BSD License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. Automated matcher found two wrong same-depth 'core' candidates (vuejs/core, home-assistant/core); contents (proc.go, mgc.go, syscall_linux.go) are unmistakably Go's own runtime source. |
| `kubernetes` | 8 | https://github.com/kubernetes/kubernetes.git | `da663405beb487d66c27a0220ea4073305ae9077` | Apache License 2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |

**Total: 17 files across 2 repo folder(s)** (2 pool-reference).
