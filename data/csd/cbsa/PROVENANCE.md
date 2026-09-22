# CSD — CICS resource definitions (CBSA)

Source:
* https://github.com/cicsdev/cics-banking-sample-application-cbsa
  (EPL-2.0) @ `46cbda52051d5cded017d72ad653df68b8ec1b60` — 1 CSD deck

Real CICS System Definition source from IBM's CICS Banking Sample Application,
unmodified:

* `BANK.csd` — a hand-written DFHCSDUP **SYSIN** member
  (`etc/install/base/installjcl/BANK.csd`): `*` column-1 comments, a leading
  `DELETE GROUP(BANK)`, quoted `DESCRIPTION(...)` operands and the `DEFINE
  TRANSACTION(...) PROGRAM(...)` records installed as the `BANK` group — CSD
  syntax surface #2 (the input-deck form, distinct from CardDemo's EXTRACT
  dump). Its `.bms` mapsets already ship under `../../bms/cbsa/`.
