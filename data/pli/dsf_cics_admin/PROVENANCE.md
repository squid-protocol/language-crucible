# PL/I — DSF (Det Sentrale Folketrygdsystemet), CICS administration subsystem

Source: https://github.com/navikt/DSF (MIT) @ `faade4961e316c89e8c312456bae411c63f1c482`
Files: `src/R0010420.pli`, `src/R0010421.pli` … `src/R0010427.pli`, `src/R0010301.pli`,
`src/R001TK62.pli` (10 programs, copied unmodified; the `src/` prefix is dropped)

Real production CICS/PL/I from Norway's national insurance system (NAV), written
from 1983 on — the first **PL/I CICS** content in the corpus (gitgalaxy#3491).
A connected slice rather than a sample: `R0010420` is the administration
subsystem's control program and `XCTL`s to `R0010421`–`R0010427` (each a
`SEND MAP` / `RECEIVE MAP` table-maintenance transaction) and back to the main
menu `R0010301`. `R001TK62` transfers with `EXEC CICS XCTL PROGRAM(PROGRAM_ID)`
— a program name held in a variable. Uses `HANDLE CONDITION`, `RETURN
TRANSID`, `READ`/`WRITE`/`REWRITE`/`DELETE DATASET` and browses (`STARTBR` /
`READNEXT` / `READPREV`), `OPTIONS(MAIN)` entry
procedures and `%INCLUDE` of commarea/map members.

**The upstream repository publishes only the `R*` programs.** Every `%INCLUDE`
member (`P0019906`, `P0019908`, the `S001A*` symbolic maps, `DFHBMSCA`) is
absent upstream, so it is absent here. This is deliberate and realistic: an
estate export with missing members is the case GitGalaxy's completeness report
has to surface. Comments are in Norwegian (with `ÆØÅ`), and columns 73-80 carry
sequence numbers in places.
