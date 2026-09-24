# CSD — Z-SMS-Gateway

Source: https://github.com/philhp/Z-SMS-Gateway (Apache-2.0) @ `37fe29d4802817791357c026b7713edb30e01afc`
File: `cics/ZSMSCSD.csd` (copied unmodified; the `cics/` prefix is dropped)

A hand-written DFHCSDUP deck (`DELETE GROUP` + `DEFINE`) for a COBOL REST gateway
on CICS TS: `DEFINE PROGRAM` / `DEFINE TRANSACTION` plus **`DEFINE URIMAP ...
USAGE(SERVER) PATH(/messages)`** — the HTTP endpoint → transaction → program
routing that makes a CICS program part of an estate's API surface
(gitgalaxy#3512). The programs it names are in `data/cobol/Z-SMS-Gateway`.
