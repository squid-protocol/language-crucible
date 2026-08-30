# GitGalaxy Language Crucible — Source Attribution Index

This is the root attribution index [issue #4](https://github.com/squid-protocol/language-crucible/issues/4) asked for: one row per `data/` language category, pointing at that category's own `SOURCES.md` for the per-repo-folder detail (upstream URL, commit, license). It replaces a root `SOURCES.md` referenced in that issue as "added alongside this issue" but which, on investigation, was never actually committed to this repository — this is a from-scratch file, not a restoration.

## Confidence levels

Every repo-folder entry across all `data/<language>/SOURCES.md` files is tagged with one of three confidence levels. This distinction is the whole point of doing this audit honestly rather than just filling in a table:

- **`exact`** — verified by the person who copied the files in, against the specific pool commit they copied from, at copy time. This only exists for categories built with source tracking already in place (`cobol`, `jcl`, `shell`, `powershell`, `lua`, `livecode` — see "Curated" below). There's no way to derive `exact` after the fact for older content; it can only be recorded honestly when the copy happens.

- **`pool-reference`** — a same-named directory was found in the `gitgalaxy/data` full-repo pool (the same pool the curated categories were built from), and its *current* `HEAD` commit and license are recorded. This is a strong signal, not a proof: nobody has verified that pool clone's current state is the exact snapshot the `data/` files were originally copied from, and in a couple of cases (`go/core`, `zig/zig`) the automated name-match initially found the wrong same-named repo entirely and had to be hand-corrected by inspecting file contents — see `tools/independent_data_auditor.py`'s `MANUAL_OVERRIDE` for exactly which two and why. Treat every `pool-reference` license as a strong indicator to verify before relying on it for anything beyond internal benchmarking.

- **`unknown`** — no confidently-matched pool clone and/or no local license file. Recorded as unknown deliberately, per the issue's own guidance: "an honest 'unknown' is better than an asserted-but-wrong attribution." Don't treat these as safe to redistribute.

## Regenerating this audit

`data/PROVENANCE.json` is the machine-readable source of truth this index and every `data/<language>/SOURCES.md` table were generated from. To reproduce or extend it:

```bash
python3 tools/independent_data_auditor.py data --provenance
```

This re-walks every `data/<language>/<repo>` folder, re-detects local licenses, and re-matches against the pool (set `GITGALAXY_POOL_PATH` if the pool isn't at the hardcoded default). It prints a coverage summary and flags any genuinely ambiguous matches (same-named git clones at the same pool depth) for human review — there are currently none. Adding a new category or repo folder and re-running this picks it up automatically as `pool-reference` or `unknown`; upgrading an entry to `exact` requires manually adding it to the `EXACT_PROVENANCE` dict in that script (that's deliberate — `exact` should only ever be asserted by whoever did the actual copy).

## Categories

| Category | Repo folders | Files | Confidence | Status | Details |
|---|---|---|---|---|---|
| `abap` | 1 | 8 | 1 pool-reference | Audited | [`data/abap/SOURCES.md`](data/abap/SOURCES.md) |
| `agc_assembly` | 1 | 12 | 1 pool-reference | Audited | [`data/agc_assembly/SOURCES.md`](data/agc_assembly/SOURCES.md) |
| `apex` | 1 | 8 | 1 pool-reference | Audited | [`data/apex/SOURCES.md`](data/apex/SOURCES.md) |
| `assembly` | 16 | 253 | 12 exact, 3 pool-reference, 1 unknown | Audited | [`data/assembly/SOURCES.md`](data/assembly/SOURCES.md) |
| `batch` | 2 | 7 | 2 pool-reference | Audited | [`data/batch/SOURCES.md`](data/batch/SOURCES.md) |
| `blueprint` | 1 | 6 | 1 pool-reference | Audited | [`data/blueprint/SOURCES.md`](data/blueprint/SOURCES.md) |
| `c` | 4 | 39 | 4 pool-reference | Audited | [`data/c/SOURCES.md`](data/c/SOURCES.md) |
| `cobol` | 15 | 589 | 13 exact, 2 unknown | Curated | [`data/cobol/SOURCES.md`](data/cobol/SOURCES.md) |
| `cpp` | 4 | 47 | 3 pool-reference, 1 unknown | Audited | [`data/cpp/SOURCES.md`](data/cpp/SOURCES.md) |
| `csharp` | 1 | 7 | 1 pool-reference | Audited | [`data/csharp/SOURCES.md`](data/csharp/SOURCES.md) |
| `css` | 11 | 49 | 8 exact, 3 pool-reference | Audited | [`data/css/SOURCES.md`](data/css/SOURCES.md) |
| `dart` | 1 | 8 | 1 pool-reference | Audited | [`data/dart/SOURCES.md`](data/dart/SOURCES.md) |
| `dockerfile` | 1 | 71 | 1 pool-reference | Audited | [`data/dockerfile/SOURCES.md`](data/dockerfile/SOURCES.md) |
| `fortran` | 1 | 15 | 1 unknown | Audited | [`data/fortran/SOURCES.md`](data/fortran/SOURCES.md) |
| `go` | 2 | 17 | 2 pool-reference | Audited | [`data/go/SOURCES.md`](data/go/SOURCES.md) |
| `groovy` | 16 | 329 | 14 exact, 2 pool-reference | Audited | [`data/groovy/SOURCES.md`](data/groovy/SOURCES.md) |
| `haskell` | 1 | 12 | 1 pool-reference | Audited | [`data/haskell/SOURCES.md`](data/haskell/SOURCES.md) |
| `hlo` | 1 | 4 | 1 unknown | Audited | [`data/hlo/SOURCES.md`](data/hlo/SOURCES.md) |
| `html` | 15 | 67 | 8 exact, 7 unknown | Audited | [`data/html/SOURCES.md`](data/html/SOURCES.md) |
| `java` | 1 | 8 | 1 pool-reference | Audited | [`data/java/SOURCES.md`](data/java/SOURCES.md) |
| `javascript` | 3 | 23 | 3 pool-reference | Audited | [`data/javascript/SOURCES.md`](data/javascript/SOURCES.md) |
| `jcl` | 6 | 193 | 6 exact | Curated | [`data/jcl/SOURCES.md`](data/jcl/SOURCES.md) |
| `json` | 2 | 5 | 1 unknown, 1 pool-reference | Audited | [`data/json/SOURCES.md`](data/json/SOURCES.md) |
| `kotlin` | 1 | 7 | 1 pool-reference | Audited | [`data/kotlin/SOURCES.md`](data/kotlin/SOURCES.md) |
| `livecode` | 1 | 99 | 1 exact | Curated | [`data/livecode/SOURCES.md`](data/livecode/SOURCES.md) |
| `lua` | 5 | 119 | 5 exact | Curated | [`data/lua/SOURCES.md`](data/lua/SOURCES.md) |
| `m4` | 2 | 11 | 2 pool-reference | Audited | [`data/m4/SOURCES.md`](data/m4/SOURCES.md) |
| `makefile` | 1 | 2 | 1 unknown | Audited | [`data/makefile/SOURCES.md`](data/makefile/SOURCES.md) |
| `matlab` | 1 | 9 | 1 pool-reference | Audited | [`data/matlab/SOURCES.md`](data/matlab/SOURCES.md) |
| `mlir` | 1 | 4 | 1 pool-reference | Audited | [`data/mlir/SOURCES.md`](data/mlir/SOURCES.md) |
| `nix` | 2 | 9 | 2 pool-reference | Audited | [`data/nix/SOURCES.md`](data/nix/SOURCES.md) |
| `objective-c` | 1 | 7 | 1 pool-reference | Audited | [`data/objective-c/SOURCES.md`](data/objective-c/SOURCES.md) |
| `perl` | 4 | 29 | 4 pool-reference | Audited | [`data/perl/SOURCES.md`](data/perl/SOURCES.md) |
| `php` | 5 | 40 | 5 pool-reference | Audited | [`data/php/SOURCES.md`](data/php/SOURCES.md) |
| `plaintext` | 4 | 8 | 4 pool-reference | Audited | [`data/plaintext/SOURCES.md`](data/plaintext/SOURCES.md) |
| `powershell` | 5 | 129 | 5 exact | Curated | [`data/powershell/SOURCES.md`](data/powershell/SOURCES.md) |
| `proto` | 1 | 4 | 1 pool-reference | Audited | [`data/proto/SOURCES.md`](data/proto/SOURCES.md) |
| `protobuf` | 1 | 1 | 1 unknown | Audited | [`data/protobuf/SOURCES.md`](data/protobuf/SOURCES.md) |
| `python` | 7 | 295 | 6 pool-reference, 1 unknown | Audited | [`data/python/SOURCES.md`](data/python/SOURCES.md) |
| `ruby` | 1 | 8 | 1 pool-reference | Audited | [`data/ruby/SOURCES.md`](data/ruby/SOURCES.md) |
| `rust` | 6 | 49 | 6 pool-reference | Audited | [`data/rust/SOURCES.md`](data/rust/SOURCES.md) |
| `scala` | 1 | 8 | 1 pool-reference | Audited | [`data/scala/SOURCES.md`](data/scala/SOURCES.md) |
| `scheme` | 1 | 8 | 1 pool-reference | Audited | [`data/scheme/SOURCES.md`](data/scheme/SOURCES.md) |
| `shell` | 13 | 282 | 13 exact | Curated | [`data/shell/SOURCES.md`](data/shell/SOURCES.md) |
| `solidity` | 1 | 8 | 1 unknown | Audited | [`data/solidity/SOURCES.md`](data/solidity/SOURCES.md) |
| `sql` | 4 | 10 | 3 unknown, 1 pool-reference | Audited | [`data/sql/SOURCES.md`](data/sql/SOURCES.md) |
| `sqlite` | 9 | 82 | 9 exact | Audited | [`data/sqlite/SOURCES.md`](data/sqlite/SOURCES.md) |
| `swift` | 1 | 8 | 1 pool-reference | Audited | [`data/swift/SOURCES.md`](data/swift/SOURCES.md) |
| `tabular` | 4 | 9 | 4 unknown | Audited | [`data/tabular/SOURCES.md`](data/tabular/SOURCES.md) |
| `tcl` | 9 | 156 | 8 exact, 1 pool-reference | Audited | [`data/tcl/SOURCES.md`](data/tcl/SOURCES.md) |
| `td` | 1 | 5 | 1 pool-reference | Audited | [`data/td/SOURCES.md`](data/td/SOURCES.md) |
| `text` | 1 | 1 | 1 unknown | Audited | [`data/text/SOURCES.md`](data/text/SOURCES.md) |
| `typescript` | 6 | 46 | 5 pool-reference, 1 unknown | Audited | [`data/typescript/SOURCES.md`](data/typescript/SOURCES.md) |
| `xml` | 5 | 24 | 4 pool-reference, 1 unknown | Audited | [`data/xml/SOURCES.md`](data/xml/SOURCES.md) |
| `yacc` | 1 | 3 | 1 unknown | Audited | [`data/yacc/SOURCES.md`](data/yacc/SOURCES.md) |
| `yaml` | 1 | 8 | 1 pool-reference | Audited | [`data/yaml/SOURCES.md`](data/yaml/SOURCES.md) |
| `zig` | 4 | 41 | 4 pool-reference | Audited | [`data/zig/SOURCES.md`](data/zig/SOURCES.md) |

Five additional `data/` directories currently hold no content and so have no `SOURCES.md`: `blp`, `csv`, `glsl`, `markdown`, `pbtxt`.

## Contributing new content

If you're adding a new repo folder under `data/`, add a row to that category's `SOURCES.md` (create one if it doesn't exist yet, matching the table format above) with `exact` confidence — you know exactly what you copied and from where, so record it at copy time rather than leaving it for a future audit. The pull request template asks for this same information; filling it in there is usually the easiest place to draft it before copying it into `SOURCES.md`.
