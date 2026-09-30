# REXX

Sources:
* `ibm_z_zos/` — https://github.com/IBM/IBM-Z-zOS (Apache-2.0). IBM's official
  z/OS sample collection: TSO/E REXX execs using ADDRESS TSO/ISPEXEC, EXECIO,
  PARSE and the stack.
* `hercules_hyperion/` — https://github.com/SDL-Hercules-390/hyperion
  (QPL-1.0, per the upstream `COPYRIGHT` file; corrected 2026-09-30). The Hercules emulator's REXX test and scripting suite, including
  `hexecio.rexx`, `hcommand.rexx` and `hrecurs.rexx`.
* `hercules_390_hyperion/` — https://github.com/hercules-390/hyperion (QPL-1.0).
  `sample.rexx` from the original Hercules repository, previously filed under
  `hercules_hyperion/`.

Covers the classic/TSO dialect. `.rexx` and `.exec` are uncontested; `.cmd` IS a
registered collision with `batch` (gitgalaxy#2504).
