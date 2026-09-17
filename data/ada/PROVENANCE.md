# Ada

Ada was a registered language in gitgalaxy with **zero** corpus representation,
so the detection-accuracy harness (gitgalaxy#3117) never measured it.

Sources:
* `functional/` — https://github.com/abitofhelp/functional (**BSD-3-Clause**).
  An Ada 2022 functional-programming library: generic packages, contracts
  (`Pre`/`Post` aspects), and matching `.ads` spec / `.adb` body pairs.
* `alire/` — https://github.com/alire-project/alire (**GPL-3.0**, flagged as
  db2unit is). The Alire package manager, written in Ada — real application
  code rather than library surface, which is the idiom a library alone does
  not represent.

Ada's three extensions (`.adb`, `.ads`, `.ada`) are all uncontested, so these
files auto-label by extension in the harness. Ada routes through the engine's
Mode A label slicer (`is ... begin ... end;`, no braces — gitgalaxy#2648).
