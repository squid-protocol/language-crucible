# CSD — CICS resource definitions (CardDemo)

Source:
* https://github.com/aws-samples/aws-mainframe-modernization-carddemo
  (Apache-2.0) @ `59cc6c2fd7ebd7ef7925cad552a01a4b8b6e4d5e` — 4 CSD decks

Real CICS System Definition source from AWS's CardDemo reference application,
unmodified:

* `CARDDEMO.CSD` — a CEDA/DFHCSDUP **EXTRACT** dump of the `CARDDEMO` group
  (`app/csd/CARDDEMO.CSD`): 18 `DEFINE TRANSACTION`, 18 `DEFINE PROGRAM` and 8
  `DEFINE FILE` records with the full CEDA audit trailers
  (`DEFINETIME`/`CHANGETIME`/`CHANGEAGENT`), continued across indented lines
  with no continuation character — CSD syntax surface #1.
* `CRDDEMOD.csd`, `CRDDEMOM.csd`, `CRDDEMO2.csd` — the DB2 transaction-type,
  VSAM/MQ and IMS-DB2-MQ variant decks
  (`app/app-transaction-type-db2/csd`, `app/app-vsam-mq/csd`,
  `app/app-authorization-ims-db2-mq/csd`), each a smaller `DEFINE
  TRANSACTION(...) PROGRAM(...)` group.

The `.CSD` extension is uppercase here (as shipped); GitGalaxy's detector
lowercases the suffix, so it classifies as `csd` regardless.
