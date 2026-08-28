# JCL corpus sources

This folder was substantially expanded on 2026-08-28 — previously it held a
single repo (`cics-genapp`) with only 3 sample JCL members. JCL was the
weakest-covered category in the Crucible relative to its importance for
CICS/mainframe interpretation, so this pass prioritized real, licensed,
production-style JCL: compile/link-edit decks, DB2 bind/DDL, VSAM
`IDCAMS DEFINE`, CICS resource definition (`DFHCSDUP`), and RACF setup.

All files are unmodified real source pulled from full clones held in the
`gitgalaxy/data` pool. See `../cobol/SOURCES.md` for the parallel COBOL
expansion (several of these repos contribute to both folders) and for the
forged-content exclusion this pass had to account for.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `cics-genapp` | 29 | https://github.com/cicsdev/cics-genapp | `63eca1b670d9199637bdc2ca7df6e4189a58c892` | Eclipse Public License 2.0 | Expanded from 3 to the complete `base/cntl` JCL deck: region/CICS resource defs, DB2 bind/create/drop, VSAM defs, CICS install. |
| `cics-banking-sample-application-cbsa` | 100 unique | https://github.com/cicsdev/cics-banking-sample-application-cbsa | `46cbda52051d5cded017d72ad653df68b8ec1b60` | Eclipse Public License 2.0 | New. Combines `etc/install/base/buildjcl` (per-program compile/link-edit JCL), `db2jcl` (table/tablespace/index create+drop, BIND), and `installjcl` (CSD update, RACF, VSAM, CICS/z/OS Connect start-stop). **Deliberately excludes `src/base/cobol_src/*.jcl`** — verified synthetic/forged output from a prior GitGalaxy run (see `../cobol/SOURCES.md` caveats), not real upstream JCL. |
| `cobol-programming-course` | 43 | https://github.com/openmainframeproject/cobol-programming-course | `11aca51998e11181925ff16c20b32c220360ff66` | CC-BY-4.0 | New. Open Mainframe Project course JCL: compile/link/go procs (`IGYWCL`/`IGYWCLG`), Db2 precompile/bind (`DB2CBL`, `DSNUPROC`), batch run JCL. |
| `zopeneditor-sample` | 10 | https://github.com/IBM/zopeneditor-sample | `41f70551d85233829a90f7891af2b56092b471c3` | Apache License 2.0 | New. IBM z/OS Explorer/Editor sample JCL (allocate, compile procs, run JCL) matching the COBOL programs in `../cobol/zopeneditor-sample`. |
| `cash-account-cobol` | 3 | https://github.com/IBMStockTrader/cash-account-cobol | `c35db0d1f283367109bcd5dfadd76560cf53b2dc` | Apache License 2.0 | New. DB2 bind/DDL and VSAM KSDS define JCL for IBM Stock Trader's cash-account service. |

**Total: ~185 real JCL files across 5 repos** (up from 5 files / 1 repo, a ~37x increase).

Commits above are the exact `HEAD` of the corresponding clone in the
`gitgalaxy/data` pool at the moment these files were copied (2026-08-28).

## Caveat

`cics-banking-sample-application-cbsa`'s `etc/install/base/buildjcl` and
`db2jcl` directories each contained one filename collision with another
selected subdirectory (`BANKDATA.jcl`, `DEFAULT.jcl`); the later copy in
directory-listing order silently overwrote the earlier one on disk, so the
folder holds 100 unique files rather than the 102 originally selected. Not
a correctness issue for the corpus — both variants were legitimate real
JCL — just a minor loss of duplicate-name diversity.
