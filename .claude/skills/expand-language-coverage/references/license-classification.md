# License classification

Use these **exact strings** in `EXACT_PROVENANCE` and the `SOURCES.md` tables —
they must match what `tools/independent_data_auditor.py`'s `LICENSE_SIGNATURES`
and the rest of the repo already use, so the audit stays consistent.

| String to use | Recognise it by (in the LICENSE header) |
|---|---|
| `MIT License` | "MIT License" / "Permission is hereby granted, free of charge, to any person obtaining a copy" |
| `Apache License 2.0` | "Apache License" + "Version 2.0, January 2004" |
| `BSD 3-Clause License` | "Redistribution and use…" + a 3rd clause "Neither the name of … may be used to endorse" |
| `BSD 2-Clause License` | "Redistribution and use…" with only 2 clauses; often says "BSD 2-Clause" / "simplified BSD" |
| `BSD License` | BSD-family text you can't confidently pin to 2- vs 3-clause; also the multi-file BSD case |
| `BSD (multiple clauses)` | a repo (freebsd-src) whose tree mixes 2/3/4-clause BSD across files |
| `GNU GPL v2.0` | "GNU GENERAL PUBLIC LICENSE" + "Version 2, June 1991" |
| `GNU GPL v3.0` | "GNU GENERAL PUBLIC LICENSE" + "Version 3, 29 June 2007" |
| `GNU LGPL` | "GNU LESSER GENERAL PUBLIC LICENSE" |
| `GNU AGPL v3.0` | "GNU AFFERO GENERAL PUBLIC LICENSE" |
| `ISC License` | "ISC License" / "Permission to use, copy, modify, and/or distribute" |
| `Mozilla Public License 2.0` | "Mozilla Public License Version 2.0" |
| `Eclipse Public License 2.0` | "Eclipse Public License - v 2.0" |
| `Public Domain` | "The author disclaims copyright to this source code" (SQLite blessing), CC0, "public domain" |
| `The Unlicense` | "This is free and unencumbered software released into the public domain" + unlicense.org |
| `present but unrecognized (see file)` | a LICENSE file exists but matches none of the above — don't guess |
| `Perl 5 terms (Artistic-1.0-or-GPL-1.0-or-later)` | "the same terms as the Perl 5 programming language system itself" |

## Rules

- **Read the actual header**, don't infer from the repo name. `stage_folder.py`
  prints its best classification; sanity-check it.
- If the classifier says `present but unrecognized`, open the file and either
  match it to a string above or keep `present but unrecognized (see file)`.
- **No LICENSE file at all** in the upstream → do not assign a license.
  Use `KNOWN_UNKNOWN` in the auditor with a reason, and `unknown` in the
  SOURCES row. (Example: `assembly/raspberrypi_baremetal` — PeterLemon/RaspberryPi
  ships nothing.)
- A "(from pool clone's LICENSE, not found locally)" suffix is what the auditor
  writes automatically when the folder itself has no LICENSE but the pool clone
  does — avoid that: always copy the LICENSE into the folder yourself.
- AGPL / SSPL / source-available / "tri-license" repos (e.g. modern redis):
  prefer a cleaner-licensed alternative from the pool if one covers the same
  boundary. If you must use it, record the license precisely and flag it in the
  PR body.
