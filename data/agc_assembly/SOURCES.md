# agc_assembly corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `apollo-11` | 12 | https://github.com/chrislgarry/Apollo-11 | `247dd7d0d1b0e7f9f270750ec08983e0a72e73e1` | Public Domain | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `apollo-11_comanche055_cm` | 11 | https://github.com/chrislgarry/Apollo-11 | `247dd7d0d1b0e7f9f270750ec08983e0a72e73e1` | Public Domain | Apollo 11 command-module flight software (Comanche055), ten further programs: `BANK` / `SETLOC` / `EBANK=` fixed-bank layout in 10 of 10, plus interpretive-language code (`DLOAD`, `VLOAD`, `CALL`, `RTB`) in 10 of 10 (orbital integration, conic subroutines, RCS autopilot, entry control). Same upstream and commit as `apollo-11`. |
| `apollo-11_luminary099_lm` | 13 | https://github.com/chrislgarry/Apollo-11 | `247dd7d0d1b0e7f9f270750ec08983e0a72e73e1` | Public Domain | Apollo 11 lunar-module flight software (Luminary099): bank / `SETLOC` layout in 12 of 12, interpretive code in 10 of 12 (ascent guidance, SERVICER, Kalman filter, P-axis RCS autopilot, throttle control, landing displays). The LM counterpart to `apollo-11_comanche055_cm`. |

**Total: 36 files across 3 repo folder(s)** (2 exact, 1 content-verified).
