# matlab corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `eeglab` | 9 | https://github.com/sccn/eeglab | `514a923047228fe24bfd9564c587e8a6b1cf56bb` | BSD License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `fieldtrip_core` | 11 | https://github.com/fieldtrip/fieldtrip | `2f3917526e6a01d37fbb224a02618f4fc61d47d9` | GPL-3.0-or-later | FieldTrip's top-level `ft_*.m` functions: `function` headers in 10 of 10 files and `varargin` option handling in 8 (the toolbox's cfg-struct style). GPL-3.0-or-later per the files' headers. Files from FieldTrip's `external/` tree (third-party code under other licenses) are excluded. |
| `fieldtrip_plotting_utils` | 13 | https://github.com/fieldtrip/fieldtrip | `2f3917526e6a01d37fbb224a02618f4fc61d47d9` | GNU GPL v3.0 | FieldTrip plotting and utility functions (`plotting/`, `utilities/`): `function` files in 11 of 12 plus one `classdef` (`ft_plot_mesh_interactive`), so it exercises both MATLAB shapes. Recorded GPL-3.0-only (the repo's COPYING): the classdef file carries a copyright line but no license notice. |

**Total: 33 files across 3 repo folder(s)** (2 exact, 1 pool-reference).
