# bms corpus sources

CICS Basic Mapping Support (BMS) map definitions. Recorded 2026-09-30.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `cbsa` | 12 | https://github.com/cicsdev/cics-banking-sample-application-cbsa | `46cbda52051d5cded017d72ad653df68b8ec1b60` | EPL-2.0 | IBM CICS Bank Sample Application maps. Upstream files are identical apart from Windows line endings. Verified by content 2026-09-30 (`tools/corpus_gate.py upstream --all`). |
| `genapp` | 2 | https://github.com/cicsdev/cics-genapp | `63eca1b670d9199637bdc2ca7df6e4189a58c892` | EPL-2.0 | `ssmap.bms` from IBM CICS GenApp, previously filed by mistake under `cbsa/`. Verified by content 2026-09-30 (`tools/corpus_gate.py upstream --all`). |
