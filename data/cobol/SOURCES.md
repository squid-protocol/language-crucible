# COBOL corpus sources

First built out 2026-08-28 to deepen CICS/mainframe coverage for the GitGalaxy
blAST engine's structural-signature benchmarks; **roughly doubled on 2026-08-30**
(308 → 589 files, 1.9x) in a breadth-first pass — see "2026-08-30 expansion" below.
Every file is real, unmodified source pulled from a full clone of the named
upstream (held in the `gitgalaxy/data` full-repo pool), never generated or
rewritten. Tool-generated artifacts from prior GitGalaxy runs (forged JCL,
`*_gitgalaxy_clean_*` output, compiler `compileListing/` output) were identified
by header/marker inspection and excluded — see Caveats.

All rows are `exact` (copied at a known pool commit) except the two noted
`unknown`. File counts include each folder's copied `LICENSE`/`COPYING` file and
match `data/PROVENANCE.json`.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `cics-genapp` | 46 | https://github.com/cicsdev/cics-genapp | `63eca1b670d9199637bdc2ca7df6e4189a58c892` | Eclipse Public License 2.0 | IBM Hursley CICS TS "GenApp" insurance demo — the complete COBOL/copybook program set. `EXEC CICS`, `EXEC SQL`, VSAM. |
| `cics-banking-sample-application-cbsa` | 67 | https://github.com/cicsdev/cics-banking-sample-application-cbsa | `46cbda52051d5cded017d72ad653df68b8ec1b60` | Eclipse Public License 2.0 | IBM CBSA — full CICS/DB2/VSAM bank teller app: the complete `cobol_src` + `cobol_copy` set. |
| `CICS-Cobol` | 51 | https://github.com/mainframe-projects/CICS-Cobol | `3fd4d46cabc39079ab198c52c235e58ab017beb7` | GNU GPL v2.0 | Numbered CICS/COBOL language-feature demos (INSPECT, PERFORM, tables, VSAM, `EXEC CICS`). |
| `cobol-programming-course` | 8 | https://github.com/openmainframeproject/cobol-programming-course | `11aca51998e11181925ff16c20b32c220360ff66` | CC-BY-4.0 | Open Mainframe Project training labs, incl. Db2 embedded SQL. All 7 `.cbl` the pool clone holds. |
| `zopeneditor-sample` | 9 | https://github.com/IBM/zopeneditor-sample | `41f70551d85233829a90f7891af2b56092b471c3` | Apache License 2.0 | IBM z/OS Explorer/Editor sample COBOL programs + copybooks. |
| `cash-account-cobol` | 4 | https://github.com/IBMStockTrader/cash-account-cobol | `c35db0d1f283367109bcd5dfadd76560cf53b2dc` | Apache License 2.0 | IBM Stock Trader's CICS/DB2/VSAM cash-account microservice back end. |
| `aws-mainframe-modernization-carddemo` | 72 | https://github.com/aws-samples/aws-mainframe-modernization-carddemo | unknown (see Caveats) | MIT (upstream) — **not verified in this copy** | Full CardDemo online (`COxxx`) CICS transactions + batch (`CBxxx`) programs and copybooks. Recorded `unknown` — see `KNOWN_UNKNOWN` in `tools/independent_data_auditor.py`. |
| `cobrix` | 36 | https://github.com/AbsaOSS/cobrix | `7200b77cdebb4244137f88b48e908acfc4ccbee1` | Apache License 2.0 | ABSA Cobrix Spark-COBOL reader's copybook / data-layout test fixtures — packed/zoned decimal, OCCURS DEPENDING ON, REDEFINES. |
| `gnucobol` | 10 | https://github.com/paulsmith/gnucobol | `d139d06201cf0aba9d143e0f675f446c19603b36` | GNU GPL v3.0 (LGPL for library parts) | Official GnuCOBOL tutorial/test programs, **plus the 5 library copybooks** (`screenio.cpy`, `sqlca.cpy`, `sqlda.cpy`, `xfhfcd*.cpy`) added 2026-08-30. Distinct from `gnucobol_internals` (C source). |
| `gnucobol_internals` | 7 | (pre-existing) | unknown (see root `SOURCES.md`) | — | Unchanged — GnuCOBOL compiler internals (C source), not application COBOL. |
| `che-che4z-lsp-for-cobol` | 3 | https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol | `dd1133952579575082914476fa699667b8790e1d` | Eclipse Public License 2.0 | Unchanged — DB2/DataCom `SQLCA`/`SQLDA` copybooks. The `che-che4z_nist_ccvs85` and `che-che4z_lsp_project_fixtures` folders below draw from other parts of the same clone. |
| `che-che4z_nist_ccvs85` | 151 | https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol | `dd1133952579575082914476fa699667b8790e1d` | Eclipse Public License 2.0 | **New (2026-08-30).** The NIST COBOL-85 CCVS positive-conformance suite (`tests/test_files/Cobol85PositiveTestsSuite/positive/`), 150 programs sampled round-robin across every language module for breadth — Nucleus (NC), Inter-Program Comm (IC), sequential/indexed I/O (IF/IX/RL), Debug (DB), Sort-Merge (SM/SG), obsolete features (OB*). Fixed-format cols 1-6 sequence + cols 73-80 program-id. `compileListing/` (IBM compiler listing output, not source) and files >60 KB excluded. |
| `che-che4z_lsp_project_fixtures` | 76 | https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol | `dd1133952579575082914476fa699667b8790e1d` | Eclipse Public License 2.0 | **New (2026-08-30).** The LSP's own `tests/test_files/project/` parser fixtures — Broadcom EPL-headered edge cases: XML PARSE/GENERATE, JSON PARSE, `EXEC SQL`/`EXEC CICS` embedded blocks, dialect keywords, deliberately-partial programs. |
| `cobol-check` | 46 | https://github.com/openmainframeproject/cobol-check | `e372dd7f436c471883bd58ac71aab49861a57e5d` | Apache License 2.0 | **New (2026-08-30).** Open Mainframe Project's COBOL unit-test tool — its `src/` COBOL, `copybooks/`, and `testfiles/` (programs that exercise DB2 instructions, file I/O, PERFORM, string handling). |
| `cics-java-jcics-samples` | 3 | https://github.com/cicsdev/cics-java-jcics-samples | `11e86326f2600220cc610bdf4bee9afa77c206c0` | Apache License 2.0 | **New (2026-08-30).** IBM's JCICS Java↔COBOL interop samples — `EC01.cbl` / `EDUCHAN.cbl` (CICS channels & containers from the COBOL side). Matching JCL in `data/jcl/cics-java-jcics-samples`. |

**Total: 589 files across 15 repo folders** (13 exact, 2 unknown) — up from 308 / 11.

## 2026-08-30 expansion

Goal was to double the category. Approach: **breadth over one big repo** — the
one repo that could have supplied it all (`che-che4z-lsp-for-cobol`, ~1073
`.cbl/.cpy` in its clone) was capped at ~225 files in two purpose-named folders
(the NIST CCVS suite + the LSP's own feature fixtures), and the rest came from
`cobol-check` and top-ups to `gnucobol`. Two additional che-che4z folders
(`analysis_client`, `engine`) were staged then dropped — they were ~95 files of
sub-15-line control-flow-graph fixtures, real but too thin to count as coverage.

- **Not achievable from real source:** every *unlicensed* COBOL repo in the pool
  stayed excluded (`Cobol-Projects` 180, `cobol-samples`, `COBOL_Tutorial`,
  `learning-cobol`) — see the pre-existing caveat below. `cics-genapp`,
  `cics-banking-cbsa`, `CICS-Cobol`, `cobrix`, `zopeneditor-sample`,
  `cobol-programming-course` were already at their pool clones' full extent.
- che-che4z's NIST `copybooks/` are extensionless PDS members (`K1PRA`, `KP007`)
  — the `cobol` standard classifies on `.cbl/.cob/.cpy/...`, so they were not
  included.

## Caveats

- **`aws-mainframe-modernization-carddemo`**: not cloned from AWS's repo — found
  as an embedded fixture inside `che-che4z-lsp-for-cobol/tests/test_files/`. No
  `LICENSE` in that embedded copy and no independent commit; the recorded commit
  is che-che4z's, i.e. when the fixture was captured, not a CardDemo commit.
  AWS's CardDemo is publicly MIT but that is unverified against this copy —
  confirm upstream before any external redistribution.
- **`cics-banking-sample-application-cbsa`**: the clone's `src/base/cobol_src/*.jcl`
  and `src/base/cobol_src_gitgalaxy_clean_*/` carry
  `AUTOGENERATED BY GITGALAXY ZERO-TRUST FORGE` / `GITGJOB` headers — synthetic
  output from a prior GitGalaxy run. Excluded from both `cobol/` and `jcl/`. The
  `.cbl` in the same directory is genuine IBM source (header-verified) and kept.
- Repos without a discoverable upstream `LICENSE` file are deliberately **not**
  added, to keep this corpus's licensing well-documented, even where real code
  was available (`Cobol-Projects`, `cobol-samples`, `COBOL_Tutorial`,
  `learning-cobol`).
