# python corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). Every entry is `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

> The `fastapi` count was `446` in v1.1.0's `PROVENANCE.json` / root `SOURCES.md` — a bookkeeping error in the issue-#4 audit (the folder has only ever held 240 tracked files; `git ls-tree v1.1.0 -- data/python/fastapi` confirms). No files were lost; the v1.2.0 regen simply made the number honest, taking the category total from a claimed 487 to the real 281. See the `fastapi` row's note.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `airflow` | 3 | https://github.com/apache/airflow.git | `f391942b90f2347272c321bcdd092c7b109cdc9e` | Apache License 2.0 (from pool clone's LICENSE, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `cython` | 4 | https://github.com/cython/cython.git | `72cfcf80e8aca6b200fac4c08027447a52291055` | Apache License 2.0 (from pool clone's LICENSE.txt, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `fastapi` | 240 | https://github.com/tiangolo/fastapi.git | `1f442c454f2f74c7419f83c203e6333955399528` | MIT License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. (File count corrected 446 → 240 on 2026-08-30 to match the committed tree; PROVENANCE.json had drifted.) |
| `numpy` | 23 | https://github.com/numpy/numpy.git | `5bceafeb63c6049a579d8163bd9d6b54171731a8` | BSD License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `twisted` | 4 | https://github.com/twisted/twisted.git | `3d84863915f8b6ec8a11be2132ebb2bd0b3d0c03` | Public Domain (from pool clone's LICENSE, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `wtfpython` | 7 | https://github.com/satwikkansal/wtfpython.git | `9323b863218670404405e0a0b9f54d2841a7452e` | present but unrecognized (see file) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |

**Total: 281 files across 6 repo folder(s)** (6 pool-reference).

`meow_turtle` (added 2026-08-30) was briefly filed here, then moved to
[`data/embedded_python/`](../embedded_python/SOURCES.md) — it's MicroPython
(`import machine`, `boot.py`, `@rp2.asm_pio`), which GitGalaxy's
`embedded_python` standard classifies separately from CPython.
