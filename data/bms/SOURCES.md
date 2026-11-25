# bms corpus sources

CICS Basic Mapping Support (BMS) map definitions. Recorded 2026-09-30.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `cbsa` | 12 | https://github.com/cicsdev/cics-banking-sample-application-cbsa | `46cbda52051d5cded017d72ad653df68b8ec1b60` | EPL-2.0 | IBM CICS Bank Sample Application maps. Upstream files are identical apart from Windows line endings. Verified by content 2026-09-30 (`tools/corpus_gate.py upstream --all`). Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `genapp` | 2 | https://github.com/cicsdev/cics-genapp | `63eca1b670d9199637bdc2ca7df6e4189a58c892` | EPL-2.0 | `ssmap.bms` from IBM CICS GenApp, previously filed by mistake under `cbsa/`. Verified by content 2026-09-30 (`tools/corpus_gate.py upstream --all`). Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `carddemo_bms` | 22 | https://github.com/aws-samples/aws-mainframe-modernization-carddemo | `59cc6c2fd7ebd7ef7925cad552a01a4b8b6e4d5e` | Apache License 2.0 | CardDemo's BMS map sources (burned estate): `DFHMSD` / `DFHMDF` macro definitions in 21 of 21 files. The first CardDemo folder in `bms`, which held only `cbsa` and `genapp`. |
| `dbb_mortgage_bms` | 3 | https://github.com/IBM/dbb | `ce2c1be58eb049e000c6627bd8273263fef0c606` | Apache License 2.0 | DBB MortgageApplication's two BMS maps (burned estate): `DFHMDI` map definitions, a third BMS source alongside `cbsa`, `genapp` and `carddemo_bms`. |

**Total: 39 files across 4 repo folder(s)** (2 exact, 2 content-verified).
