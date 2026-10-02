# GitGalaxy Language Crucible — Source Attribution Index

This is the root attribution index [issue #4](https://github.com/squid-protocol/language-crucible/issues/4) asked for: one row per `data/` language category, pointing at that category's own `SOURCES.md` for the per-repo-folder detail (upstream URL, commit, license). It replaces a root `SOURCES.md` referenced in that issue as "added alongside this issue" but which, on investigation, was never actually committed to this repository — this is a from-scratch file, not a restoration.

## Confidence levels

Every repo-folder entry across all `data/<language>/SOURCES.md` files is tagged with one of three confidence levels. This distinction is the whole point of doing this audit honestly rather than just filling in a table:

- **`exact`** — verified by the person who copied the files in, against the specific pool commit they copied from, at copy time. This only exists for categories built with source tracking already in place (`cobol`, `jcl`, `shell`, `powershell`, `lua`, `livecode` — see "Curated" below). There's no way to derive `exact` after the fact for older content; it can only be recorded honestly when the copy happens.

- **`pool-reference`** — a same-named directory was found in the `gitgalaxy/data` full-repo pool (the same pool the curated categories were built from), and its *current* `HEAD` commit and license are recorded. This is a strong signal, not a proof: nobody has verified that pool clone's current state is the exact snapshot the `data/` files were originally copied from, and in a couple of cases (`go/core`, `zig/zig`) the automated name-match initially found the wrong same-named repo entirely and had to be hand-corrected by inspecting file contents — see `tools/independent_data_auditor.py`'s `MANUAL_OVERRIDE` for exactly which two and why. Treat every `pool-reference` license as a strong indicator to verify before relying on it for anything beyond internal benchmarking.

- **`unknown`** — no confidently-matched pool clone and/or no local license file. Recorded as unknown deliberately, per the issue's own guidance: "an honest 'unknown' is better than an asserted-but-wrong attribution." Don't treat these as safe to redistribute.

Two more levels were added by the upstream verification pass of 2026-09-30, which compared every corpus file against its upstream repository by content (`tools/corpus_gate.py upstream --all`):

- **`content-verified`** — every file in the folder is identical, apart from line endings, to a file in the recorded repository at the recorded commit. The commit is one at which all the files exist, which is not necessarily the one they were first copied from. This is a machine check, so it holds regardless of how the folder was originally sourced. See `CONTENT_VERIFIED` in `tools/independent_data_auditor.py`.

- **`original`** — written for this repository rather than copied (the `baseline` control files and a few purpose-built payloads). There is no upstream; the repository's own license covers them.

The same pass confirmed the license of every folder previously recorded as having none or an unrecognized one (`VERIFIED_LICENSE` in the same file). `data/PROVENANCE.json` carries those results. The per-category `SOURCES.md` tables and the table below are generated from it by `tools/generate_sources.py`, and CI fails if they drift.

## Regenerating this audit

`data/PROVENANCE.json` is the machine-readable source of truth this index and every `data/<language>/SOURCES.md` table were generated from. To reproduce or extend it:

```bash
python3 tools/independent_data_auditor.py data --provenance
```

This re-walks every `data/<language>/<repo>` folder, re-detects local licenses, and re-matches against the pool (set `GITGALAXY_POOL_PATH` if the pool isn't at the hardcoded default). It prints a coverage summary and flags any genuinely ambiguous matches (same-named git clones at the same pool depth) for human review — there are currently none. Adding a new category or repo folder and re-running this picks it up automatically as `pool-reference` or `unknown`; upgrading an entry to `exact` requires manually adding it to the `EXACT_PROVENANCE` dict in that script (that's deliberate — `exact` should only ever be asserted by whoever did the actual copy).

## Categories

| Category | Repo folders | Files | Confidence | Status | Details |
|---|---|---|---|---|---|
| `abap` | 1 | 9 | 1 pool-reference | Audited | [`data/abap/SOURCES.md`](data/abap/SOURCES.md) |
| `ada` | 2 | 52 | 2 content-verified | Audited | [`data/ada/SOURCES.md`](data/ada/SOURCES.md) |
| `agc_assembly` | 1 | 12 | 1 pool-reference | Audited | [`data/agc_assembly/SOURCES.md`](data/agc_assembly/SOURCES.md) |
| `apex` | 1 | 8 | 1 pool-reference | Audited | [`data/apex/SOURCES.md`](data/apex/SOURCES.md) |
| `assembly` | 16 | 248 | 13 exact, 3 pool-reference | Audited | [`data/assembly/SOURCES.md`](data/assembly/SOURCES.md) |
| `batch` | 2 | 7 | 2 pool-reference | Audited | [`data/batch/SOURCES.md`](data/batch/SOURCES.md) |
| `blueprint` | 1 | 6 | 1 pool-reference | Audited | [`data/blueprint/SOURCES.md`](data/blueprint/SOURCES.md) |
| `bms` | 2 | 14 | 2 content-verified | Audited | [`data/bms/SOURCES.md`](data/bms/SOURCES.md) |
| `c` | 6 | 44 | 2 exact, 4 pool-reference | Audited | [`data/c/SOURCES.md`](data/c/SOURCES.md) |
| `cobol` | 17 | 609 | 15 exact, 2 content-verified | Curated | [`data/cobol/SOURCES.md`](data/cobol/SOURCES.md) |
| `cpp` | 5 | 50 | 1 exact, 1 content-verified, 3 pool-reference | Audited | [`data/cpp/SOURCES.md`](data/cpp/SOURCES.md) |
| `csd` | 3 | 14 | 3 content-verified | Audited | [`data/csd/SOURCES.md`](data/csd/SOURCES.md) |
| `csharp` | 1 | 7 | 1 pool-reference | Audited | [`data/csharp/SOURCES.md`](data/csharp/SOURCES.md) |
| `css` | 11 | 49 | 8 exact, 3 pool-reference | Audited | [`data/css/SOURCES.md`](data/css/SOURCES.md) |
| `dart` | 1 | 8 | 1 pool-reference | Audited | [`data/dart/SOURCES.md`](data/dart/SOURCES.md) |
| `db2_sql` | 1 | 12 | 1 content-verified | Audited | [`data/db2_sql/SOURCES.md`](data/db2_sql/SOURCES.md) |
| `dockerfile` | 1 | 71 | 1 pool-reference | Audited | [`data/dockerfile/SOURCES.md`](data/dockerfile/SOURCES.md) |
| `embedded_python` | 1 | 14 | 1 original | Audited | [`data/embedded_python/SOURCES.md`](data/embedded_python/SOURCES.md) |
| `fortran` | 1 | 15 | 1 content-verified | Audited | [`data/fortran/SOURCES.md`](data/fortran/SOURCES.md) |
| `go` | 4 | 21 | 2 exact, 2 pool-reference | Audited | [`data/go/SOURCES.md`](data/go/SOURCES.md) |
| `groovy` | 16 | 329 | 14 exact, 2 pool-reference | Audited | [`data/groovy/SOURCES.md`](data/groovy/SOURCES.md) |
| `haskell` | 1 | 12 | 1 pool-reference | Audited | [`data/haskell/SOURCES.md`](data/haskell/SOURCES.md) |
| `hlasm` | 3 | 24 | 3 content-verified | Audited | [`data/hlasm/SOURCES.md`](data/hlasm/SOURCES.md) |
| `hlo` | 1 | 4 | 1 content-verified | Audited | [`data/hlo/SOURCES.md`](data/hlo/SOURCES.md) |
| `html` | 15 | 68 | 8 exact, 6 content-verified, 1 original | Audited | [`data/html/SOURCES.md`](data/html/SOURCES.md) |
| `java` | 4 | 15 | 3 exact, 1 pool-reference | Audited | [`data/java/SOURCES.md`](data/java/SOURCES.md) |
| `javascript` | 7 | 37 | 4 exact, 3 pool-reference | Audited | [`data/javascript/SOURCES.md`](data/javascript/SOURCES.md) |
| `jcl` | 6 | 193 | 6 exact | Curated | [`data/jcl/SOURCES.md`](data/jcl/SOURCES.md) |
| `json` | 2 | 5 | 1 pool-reference, 1 original | Audited | [`data/json/SOURCES.md`](data/json/SOURCES.md) |
| `kotlin` | 1 | 7 | 1 pool-reference | Audited | [`data/kotlin/SOURCES.md`](data/kotlin/SOURCES.md) |
| `livecode` | 1 | 99 | 1 exact | Curated | [`data/livecode/SOURCES.md`](data/livecode/SOURCES.md) |
| `lua` | 5 | 120 | 5 exact | Curated | [`data/lua/SOURCES.md`](data/lua/SOURCES.md) |
| `m4` | 2 | 11 | 2 pool-reference | Audited | [`data/m4/SOURCES.md`](data/m4/SOURCES.md) |
| `makefile` | 1 | 2 | 1 content-verified | Audited | [`data/makefile/SOURCES.md`](data/makefile/SOURCES.md) |
| `markdown` | 2 | 5 | 2 exact | Audited | [`data/markdown/SOURCES.md`](data/markdown/SOURCES.md) |
| `matlab` | 1 | 9 | 1 pool-reference | Audited | [`data/matlab/SOURCES.md`](data/matlab/SOURCES.md) |
| `mlir` | 1 | 4 | 1 pool-reference | Audited | [`data/mlir/SOURCES.md`](data/mlir/SOURCES.md) |
| `nix` | 2 | 10 | 2 pool-reference | Audited | [`data/nix/SOURCES.md`](data/nix/SOURCES.md) |
| `objective-c` | 1 | 7 | 1 pool-reference | Audited | [`data/objective-c/SOURCES.md`](data/objective-c/SOURCES.md) |
| `perl` | 5 | 31 | 1 exact, 1 content-verified, 3 pool-reference | Audited | [`data/perl/SOURCES.md`](data/perl/SOURCES.md) |
| `php` | 7 | 44 | 2 exact, 1 content-verified, 4 pool-reference | Audited | [`data/php/SOURCES.md`](data/php/SOURCES.md) |
| `plaintext` | 4 | 11 | 4 pool-reference | Audited | [`data/plaintext/SOURCES.md`](data/plaintext/SOURCES.md) |
| `pli` | 2 | 17 | 2 content-verified | Audited | [`data/pli/SOURCES.md`](data/pli/SOURCES.md) |
| `powershell` | 5 | 129 | 5 exact | Curated | [`data/powershell/SOURCES.md`](data/powershell/SOURCES.md) |
| `proto` | 1 | 4 | 1 pool-reference | Audited | [`data/proto/SOURCES.md`](data/proto/SOURCES.md) |
| `protobuf` | 1 | 1 | 1 original | Audited | [`data/protobuf/SOURCES.md`](data/protobuf/SOURCES.md) |
| `python` | 19 | 328 | 13 exact, 6 pool-reference | Audited | [`data/python/SOURCES.md`](data/python/SOURCES.md) |
| `rexx` | 3 | 28 | 3 content-verified | Audited | [`data/rexx/SOURCES.md`](data/rexx/SOURCES.md) |
| `ruby` | 2 | 10 | 1 exact, 1 pool-reference | Audited | [`data/ruby/SOURCES.md`](data/ruby/SOURCES.md) |
| `rust` | 8 | 60 | 2 exact, 2 content-verified, 4 pool-reference | Audited | [`data/rust/SOURCES.md`](data/rust/SOURCES.md) |
| `scala` | 1 | 8 | 1 pool-reference | Audited | [`data/scala/SOURCES.md`](data/scala/SOURCES.md) |
| `scheme` | 1 | 8 | 1 pool-reference | Audited | [`data/scheme/SOURCES.md`](data/scheme/SOURCES.md) |
| `shell` | 14 | 286 | 14 exact | Curated | [`data/shell/SOURCES.md`](data/shell/SOURCES.md) |
| `solidity` | 1 | 8 | 1 content-verified | Audited | [`data/solidity/SOURCES.md`](data/solidity/SOURCES.md) |
| `sql` | 6 | 14 | 4 content-verified, 1 pool-reference, 1 original | Audited | [`data/sql/SOURCES.md`](data/sql/SOURCES.md) |
| `sqlite` | 9 | 82 | 9 exact | Audited | [`data/sqlite/SOURCES.md`](data/sqlite/SOURCES.md) |
| `swift` | 1 | 8 | 1 pool-reference | Audited | [`data/swift/SOURCES.md`](data/swift/SOURCES.md) |
| `tabular` | 4 | 9 | 2 content-verified, 2 original | Audited | [`data/tabular/SOURCES.md`](data/tabular/SOURCES.md) |
| `tcl` | 9 | 157 | 8 exact, 1 pool-reference | Audited | [`data/tcl/SOURCES.md`](data/tcl/SOURCES.md) |
| `td` | 1 | 5 | 1 pool-reference | Audited | [`data/td/SOURCES.md`](data/td/SOURCES.md) |
| `text` | 1 | 1 | 1 original | Audited | [`data/text/SOURCES.md`](data/text/SOURCES.md) |
| `typescript` | 12 | 60 | 6 exact, 2 content-verified, 4 pool-reference | Audited | [`data/typescript/SOURCES.md`](data/typescript/SOURCES.md) |
| `xml` | 5 | 26 | 1 content-verified, 4 pool-reference | Audited | [`data/xml/SOURCES.md`](data/xml/SOURCES.md) |
| `yacc` | 1 | 3 | 1 content-verified | Audited | [`data/yacc/SOURCES.md`](data/yacc/SOURCES.md) |
| `yaml` | 7 | 51 | 6 exact, 1 pool-reference | Audited | [`data/yaml/SOURCES.md`](data/yaml/SOURCES.md) |
| `zig` | 6 | 47 | 1 exact, 1 content-verified, 3 pool-reference, 1 unknown | Audited | [`data/zig/SOURCES.md`](data/zig/SOURCES.md) |

Four additional `data/` directories currently hold no content and so have no `SOURCES.md`: `blp`, `csv`, `glsl`, `pbtxt`.

## Contributing new content

If you're adding a new repo folder under `data/`, record it in `tools/independent_data_auditor.py` with `exact` confidence, update `data/PROVENANCE.json`, then run `python3 tools/generate_sources.py` to write its table row (the tool creates the category's `SOURCES.md` if needed; add your own description in the Notes column afterwards). Record `exact` confidence — you know exactly what you copied and from where, so record it at copy time rather than leaving it for a future audit. The pull request template asks for this same information; filling it in there is usually the easiest place to draft it before copying it into `SOURCES.md`.

## Security-signal coverage (gitgalaxy#4108)

Added 2026-10-02 so the golden master exercises GitGalaxy's security and low-level signals,
which read 0 (or nearly 0) on the rest of the corpus. Every file is real upstream code, copied
unmodified with `exact` provenance; the per-category `SOURCES.md` Notes name the shape each
file carries. Credentials are upstream test fixtures and dummy values only. Worm-pattern and
invisible-Unicode files are benign: self-copying test and build scripts, and emoji
subdivision-flag tag sequences.

The invisible-Unicode folders turned out to carry only emoji subdivision flags (U+1F3F4, a
lowercase TAG-letter subdivision id, U+E007F CANCEL TAG), which the engine now exempts
(gitgalaxy#4135). They stay as **negative controls**: Invisible Unicode Payload Smuggling must
read 0 on them, so a regression that loses the exemption shows up in the golden master. The
corpus carries no positive example of that signal; real tag-block smuggling is malware and is
not added here (Quarantine Protocol). The engine's unit tests cover the positive shapes.

| Signal | Folders |
|---|---|
| Invisible Unicode Payload Smuggling (negative control, must read 0) | `javascript/node_tls_security_tests` (V8 test), `typescript/excalidraw_text_wrapping`, `java/flutter_android_editing_tests`, `php/symfony_emoji_data` |
| Self-Referential File Copy/Overwrite (Worm Pattern) | `javascript/node_tls_security_tests` (test-fs-lchown.js), `javascript/react_error_codes`, `perl/ack3_tests`, `shell/freebsd_sysbuild` |
| Low-Level Bitwise / Cryptographic Math | `javascript/javascript_algorithms_bits`, `rust/tokio_util_rand`, `cpp/serenity_ak_siphash_cpu`, `go/go_runtime_rand` |
| Safety & Constraint Bypasses | `javascript/node_tls_security_tests`, `python/homeassistant_ble_integrations` |
| Hardware Bridge | `python/homeassistant_ble_integrations`, `python/micropython_usb_tls` |
| Non-Standard / Steganographic Imports | `rust/bevy_asset_examples`, `typescript/pixijs_examples` |
| Embedded Credentials & Keys, Hardcoded Payload Artifacts | `javascript/node_tls_security_tests`, `go/kubernetes_kubectl_tls`, `ruby/rails_http_token_auth`, `python/airflow_opsgenie_tests` |
| Global Environment Mutation | `javascript/cesium_particle_emitters`, `typescript/angular_zonejs_mocha`, `python/pip_vendored_requests` |
| Public API Declared Near Raw DB Sink | `python/django_db_tests`, `java/selenium_grid_session_queue` |
| Auth Middleware | `c/freebsd_openpam`, `java/jenkins_cli`, `php/laravel_validation_rules`, `ruby/rails_http_token_auth` |
| Cryptography | `javascript/node_tls_security_tests`, `python/micropython_usb_tls` |
| Inline Assembly Blocks | `c/cosmopolitan_intrin`, `cpp/serenity_ak_siphash_cpu`, `zig/zig_std_linux_mips` |

## AI/ML and diagram signal coverage (gitgalaxy#4108, 2026-10-02)

Added so the golden master exercises signals that fired on zero crucible files: Cloud LLM API
Integrations, AI Orchestration Frameworks, Vector Databases (RAG), Local Inference & Tensor Math,
Deep Learning, Traditional ML, Architectural Diagrams (Mermaid), plus more Vectorized Math
(including its first TypeScript hits). All are `exact`, copied unmodified from the pool, each
folder ships its upstream licence (and Apache `NOTICE` where upstream has one):

- `python/`: `airflow_ai_providers`, `homeassistant_anthropic`, `langchain_agents`,
  `tensorflow_ml_ops`, `tensorflow_model_fixtures`, `opencv_dnn_conversion`,
  `thealgorithms_machine_learning`, `scikit-learn_examples`
- `typescript/`: `nx_util_ai`, `effect_ai_anthropic`, `excalibur_math`
- `markdown/` (new category): `airflow_job_lifecycle`, `kubernetes_client_go`

These signals are only defined for Python, JavaScript and TypeScript (and Markdown for diagrams),
so no other language can carry them. `tensorflow_model_fixtures` holds two tiny real binary model
files on purpose: Local Inference & Tensor Math is produced only by the engine's model-weight
scanner, which is keyed on model-file extensions.
