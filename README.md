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

See [`SOURCES.md`](SOURCES.md) for the attribution record — which upstream project each
paradigm came from, and that project's own license.

## How the Corpus Is Selected

The selection process changed over time, and it's worth being explicit about both phases
rather than presenting the current corpus as if it were always built the same way.

**Early on, files were chosen essentially at random** from within each target project —
whatever looked structurally representative of the paradigm at a glance. That was enough to
get the corpus off the ground, but "looks representative" is a weak signal for what actually
stresses a structural parser.

**Later additions switched to using GitGalaxy itself to guide selection.** Instead of picking
files by eye, a candidate project gets scanned first, and the files GitGalaxy's own risk and
complexity scoring ranks highest — the highest structural-signature density, the largest
blast radius, the most tangled control flow — are the ones pulled into the corpus. This is
deliberately circular in a useful way: the files most likely to break a structural parser are,
almost by definition, the files with the most structural signal for a structural parser to
misread. Using the engine to find its own hardest cases produces a corpus that's harder to
pass than one assembled by hand, and the golden-master mechanism below means any resulting
regression gets caught, not silently absorbed.

## Golden-Master Verification: How GitGalaxy Actually Uses This Repo

Beyond being a stress test, this repository is the empirical backbone of GitGalaxy's own test
suite — the check that the whole engine, wired together, produces the *right* answer on real
code, not just on synthetic strings a test author thought to write. This is the mechanism
behind the "Proof, Not Just Claims" section of
[GitGalaxy's own README](https://github.com/squid-protocol/gitgalaxy#proof-not-just-claims).

GitGalaxy's CI pins this repo to a specific tagged release — currently `v1.0`, via a literal
`git clone --branch v1.0 --depth 1` in
[`golden-crucible.yml`](https://github.com/squid-protocol/gitgalaxy/blob/main/.github/workflows/golden-crucible.yml)
(the same pin is referenced in gitgalaxy's `tests/test_golden_crucible.py` and
`tests/tools/crucible_check.py`). It checks two deterministic snapshots into its own repo:
`tests/golden_master_audit.json` and `tests/golden_master_zero_dep_audit.json`, one for each of
the engine's two dependency modes. On every pull request that touches GitGalaxy's parsing
engine, its `crucible-audit` CI job clones this exact tagged corpus fresh and re-runs a full
scan, then diffs the output against those checked-in snapshots — field by field, down to
individual structural-signature counts per file. That's a true golden diff, not a smoke test: a
failing diff means GitGalaxy's output changed on this real, unmodified code, and it has to be
explained — either a regression that gets fixed, or a deliberate improvement whose new baseline
gets explicitly re-blessed (never a blind overwrite).

**The tag is frozen on purpose.** Merging a PR to this repo's `main` branch does not change
what GitGalaxy's CI scans — it only affects a future tagged release. This means new paradigms
can be merged and made available immediately for anyone testing against `main` directly,
without any risk of silently shifting the ground under GitGalaxy's own golden-master snapshots
mid-cycle. When enough has accumulated on `main` to justify it, a new tag gets cut (`v1.1`,
`v2.0`, ...), and a separate, deliberate PR in the gitgalaxy repo bumps the pin in all three
places above together with a re-blessed golden-master snapshot — the same explicit
re-blessing discipline described above, just applied to moving the pin itself.

This is why the paradigms above aren't just adversarial-formatting exercises — every one of
them has caught, and continues to guard against, real regressions in GitGalaxy's
structural-signature regexes. See GitGalaxy's own
[`tests/README.md`](https://github.com/squid-protocol/gitgalaxy/blob/main/tests/README.md#5-golden-master-differential-testing-the-language-crucible)
for the full mechanism, and [epic #518](https://github.com/squid-protocol/gitgalaxy/issues/518)
for the audit that used this corpus to verify every one of ~40 real regex bugs found across 6
languages before merging.

## See It In Action

`raw_output/` holds the actual, unedited output of scanning this corpus at past engine
versions — a sample of what GitGalaxy's output looks like before you run it yourself:

* [`raw_output/v4.3.1/data_galaxy_llm.md`](raw_output/v4.3.1/data_galaxy_llm.md) — the
  human-readable summary brief, the easiest one to skim.
* The same directory also has the full machine-readable artifacts from that run: `_galaxy_audit.json`
  (findings), `_galaxy_sarif.json` (CI-standard format), `_galaxy_sbom.json` (dependency
  manifest), `_galaxy_master.db` (queryable SQLite), and `_galaxy_graph.sqlite` (the dependency
  graph backing the 3D visualizer).

For a much larger sample — real-world-scale output across hundreds of independently-chosen
repositories, not just this curated adversarial corpus — see
[`gitgalaxy-raw-output`](https://github.com/squid-protocol/gitgalaxy-raw-output). This repo
and that one answer different questions: this one proves GitGalaxy's output is *correct* on a
small, deliberately hostile corpus; `gitgalaxy-raw-output` is the evidence it also *runs*, the
same way, at scale.

## Contributing

Missing a language, a file type, or a paradigm you think would break the parser in a new way?
Contributions are welcome, and there's an explicit path for them:

1. **Add your file(s)** under `data/<language>/<short-name>/`, matching the existing structure.
2. **Add a row to [`SOURCES.md`](SOURCES.md)** naming the upstream project, a link to it, and
   its license. Code must come from a genuinely open-source project — no proprietary or
   unlicensed snippets. If you wrote the snippet yourself specifically to stress a parsing
   boundary rather than pulling it from a real project, say so in `SOURCES.md` and in the PR
   instead of attributing it to a project it didn't come from.
3. **Open a PR** using the existing [PR template](.github/PULL_REQUEST_TEMPLATE.md) — it
   already covers the zero-execution / no-malicious-payload constraints this repo requires,
   since nothing here is ever compiled or run.
4. Describe what parsing boundary the addition tests, the same way the existing entries in
   "The Paradigms" above do.

**What happens after merge:** your addition lands on `main` immediately and is available to
anyone testing against this repo directly. It reaches GitGalaxy's own CI once a new version
tag is cut — see "The tag is frozen on purpose" above for why that's a deliberate, separate
step rather than automatic.

## Running a Scan

```bash
galaxyscope /path/to/all_language_repo --output /tmp
```

The engine parses without a compile step and produces a dependency graph, structural risk
report, and complexity map regardless of whether any of the code in this corpus can build.
