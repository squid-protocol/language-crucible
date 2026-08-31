# The GitGalaxy Language Crucible

## Why This Exists

Most static-analysis benchmarks test a parser against clean, compilable, single-language code
— exactly the condition real repositories almost never meet. [GitGalaxy](https://github.com/squid-protocol/gitgalaxy)
claims to parse 50+ languages without an AST or a working build, on code that's disconnected,
uncompilable, and polyglot. That claim needs a corpus that's actually hostile to prove itself
against, not a curated one that's secretly easy — this repo is that corpus, and the mechanism
that turns it into a continuously-checked claim rather than a one-time demo.

## Overview

This repository is a benchmark and stress-test corpus for the GitGalaxy engine's structural
signature extraction and language detection. It is not a functional software project and
**it will never compile.** It's a collection of real, unmodified source snippets pulled
directly from significant, historically notable open-source repositories, spanning 56
languages and formats — deliberately left disconnected from their original build systems, the
same broken state a real enterprise monorepo is in more often than not.

## The Problem: Compiler-Dependent Tooling Breaks on Real Repos

Traditional static analysis tools, Language Server Protocols (LSPs), and AST parsers need a
clean environment: dependencies resolved, syntax homogeneous, code that actually compiles. A
missing import or an unrecognized macro is often enough to make them fail outright or fall back
to degraded results.

This corpus is built to expose exactly that fragility. By presenting a disconnected,
multi-paradigm directory structure with no working build for any of it, it tests whether a
tool's parsing is actually independent of compilation — or only claims to be.

## The Approach: Structural Signatures, Not an AST

GitGalaxy doesn't build an AST or execute code against this corpus. It reads the physical
structure of the source text directly — function and class boundaries, control flow, I/O,
state mutation — via bounded regex rules, then rolls those counts up into per-file and
per-repo risk and complexity metrics. Scanning this corpus is the check that this approach
holds up on real, adversarially-formatted code, not just on the synthetic strings a rule's
own unit test was written against.

## The Paradigms

The corpus contains raw extractions from the following paradigms, each chosen to stress a
specific parsing boundary:

* **The Metaprogramming Minefield (Ruby / Rails):** Tests mapping dynamic execution and `method_missing` routing where explicit definitions don't exist.
* **The Orchestration Giant (Go / Kubernetes):** Tests structural subtyping (implicit interfaces) and channel-based concurrency.
* **The Enterprise OOP Labyrinth (Java / Spring Boot):** Tests Inversion of Control, dependency injection, and annotation-driven metadata execution.
* **The Homoiconic Trap (Scheme / Racket):** Tests Lisp macro-expanders, where the AST and the execution tree are structurally identical.
* **The Pure Functional Trap (Haskell / Pandoc):** Tests execution mapping in an environment without mutable state or traditional loops.
* **The Reactive Mobile Tree (Dart / Flutter):** Tests deep UI tree reconciliation and cross-platform state lifecycles.
* **The Self-Hosting Compiler (C# / Roslyn):** Tests differentiating logic that *executes* code from logic that *represents* code (AST generation).
* **The Immutable Ledger (Solidity / OpenZeppelin):** Tests financial transaction modifiers and raw `yul` EVM inline assembly.
* **The Legacy Regex Trap (JavaScript / jQuery & Perl):** Tests unstructured string manipulation, prototype pollution, and high cyclomatic complexity.
* **The Embedded Hardware Boundary (C / Doom & C++ / Godot):** Tests raw pointer math, manual memory allocation, and OS-level I/O abstractions.
* **The Mainframe Batch/Online Split (COBOL / JCL / CICS):** Tests the engine's ability to correlate two disjoint languages describing one system — job-control decks (`JCL`) that compile, bind, and schedule the very `EXEC CICS`/`EXEC SQL`-laden COBOL programs and copybooks they never textually reference by import. See `data/cobol/SOURCES.md` and `data/jcl/SOURCES.md` for the full provenance and license of every mainframe repo included.
* **The Glue-Script Substrate (Shell / PowerShell):** Tests parsing across the two dialects that actually build, install, and operate every other paradigm here — POSIX/Bourne/ksh scripts from four decades of Unix-lineage kernels (BSD, illumos, Linux, Darwin XNU, Haiku, SerenityOS, ReactOS) plus Windows-native PowerShell build/CI tooling from the .NET and PowerShell projects themselves — with heavy dynamic dispatch (`eval`, sourcing, indirect variable expansion, cmdlet pipelines) and near-zero static import structure. See `data/shell/SOURCES.md` and `data/powershell/SOURCES.md` for full provenance and license.
* **The Embedded Scripting Host (Lua / LiveCode):** Tests two languages defined entirely by the C/C++ host that embeds them, with no standalone toolchain of their own — Lua running everywhere from a document-filter API (Pandoc) to a web server (Redbean) to a boot loader executing *before the kernel exists* (FreeBSD's `lualoader`), across two dialect eras (5.1 vs. 5.4) of the same reference test suite; and LiveCode's HyperCard-descended `.livecodescript` alongside its newer typed module language `.lcb`, both meaningless without the engine that interprets them. See `data/lua/SOURCES.md` and `data/livecode/SOURCES.md` for full provenance and license.

## Golden-Master Verification: How GitGalaxy Actually Uses This Repo

Beyond being a stress test, this repository is the empirical backbone of GitGalaxy's own test
suite — the check that the whole engine, wired together, produces the *right* answer on real
code, not just on synthetic strings a test author thought to write. This is the mechanism
behind the "Proof, Not Just Claims" section of
[GitGalaxy's own README](https://github.com/squid-protocol/gitgalaxy#proof-not-just-claims).

GitGalaxy pins this repo to a tagged release (currently `v1.0`) and checks two deterministic
snapshots into its own repo: `tests/golden_master_audit.json` and
`tests/golden_master_zero_dep_audit.json`, one for each of the engine's two dependency modes.
On every pull request that touches GitGalaxy's parsing engine, its `crucible-audit` CI job
clones this exact tagged corpus fresh and re-runs a full scan, then diffs the output against
those checked-in snapshots — field by field, down to individual structural-signature counts
per file. That's a true golden diff, not a smoke test: a failing diff means GitGalaxy's output
changed on this real, unmodified code, and it has to be explained — either a regression that
gets fixed, or a deliberate improvement whose new baseline gets explicitly re-blessed (never a
blind overwrite).

This is why the paradigms above aren't just adversarial-formatting exercises — every one of
them has caught, and continues to guard against, real regressions in GitGalaxy's
structural-signature regexes. See GitGalaxy's own
[`tests/README.md`](https://github.com/squid-protocol/gitgalaxy/blob/main/tests/README.md#5-golden-master-differential-testing-the-language-crucible)
for the full mechanism, and [epic #518](https://github.com/squid-protocol/gitgalaxy/issues/518)
for the audit that used this corpus to verify every one of ~40 real regex bugs found across 6
languages before merging.

Cutting a new tag doesn't update that pin by itself — see [`RELEASING.md`](RELEASING.md) for
the full checklist, including the two hardcoded references in GitGalaxy's own workflows that
also need to move. And every file's upstream source, commit, and license is tracked in the
root [`SOURCES.md`](SOURCES.md) — see that file's "Confidence levels" section for what's been
independently verified versus what's a best-effort match against the source pool.

## Running a Scan

```bash
galaxyscope /path/to/all_language_repo --output /tmp
```

The engine parses without a compile step and produces a dependency graph, structural risk
report, and complexity map regardless of whether any of the code in this corpus can build.

## The GitGalaxy constellation

This repo is one strand of the web of repos that build, prove, and showcase
[GitGalaxy](https://github.com/squid-protocol/gitgalaxy). This is the **accuracy leg** — real,
hostile, multi-language code the engine must parse correctly, release after release; the
**consistency leg** (does it measure identical intent identically across languages?) is
keyword-rosetta:

- [gitgalaxy](https://github.com/squid-protocol/gitgalaxy) — the engine this corpus stress-tests (pinned via `LANGUAGE_CRUCIBLE_REF`)
- **language-crucible** — *you are here*: the adversarial benchmark corpus
- [keyword-rosetta](https://github.com/squid-protocol/keyword-rosetta) — one planted program in 46 languages, measuring cross-language measurement consistency
- [gitgalaxy-raw-output](https://github.com/squid-protocol/gitgalaxy-raw-output) — unedited scans of real repos + speed telemetry (proves it *runs* at scale; this repo proves it's *correct*)
- [gitgalaxy-population-analyses](https://github.com/squid-protocol/gitgalaxy-population-analyses) — statistics over the scan population
- [cobol_to_java_examples](https://github.com/squid-protocol/cobol_to_java_examples) — 10 COBOL repos auto-translated to compiling Spring Boot architectures (several sources also live in this corpus's cobol/jcl categories)
- [squid-telemetry](https://github.com/squid-protocol/squid-telemetry) — public distribution/adoption metrics
- Docs: [architecture & methodology site](https://squid-protocol.github.io/gitgalaxy/) · [Museum of Code](https://squid-protocol.github.io/gitgalaxy/museum-of-code/) · [gitgalaxy.io](https://gitgalaxy.io/) · [PyPI](https://pypi.org/project/gitgalaxy/)
