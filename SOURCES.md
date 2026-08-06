# Sources

Every paradigm in this corpus is real, unmodified code pulled from an existing open-source
project — not synthetic or hand-written test fixtures. This file is the attribution record:
which project each paradigm came from, and where to find that project's own license.

**This is a first pass, not a complete audit.** It covers the ten paradigms named in
[`README.md`](README.md#the-paradigms) at the project level. It does not yet pin an exact
commit or file path per paradigm the way `gitgalaxy-raw-output`'s
[`corpus/v1/manifest.json`](https://github.com/squid-protocol/gitgalaxy-raw-output/blob/main/corpus/v1/manifest.json)
does for its own corpus — see the tracking issue linked at the bottom for closing that gap
across all 56 language/format directories under `data/`.

| Paradigm | Language | Source Project | License |
|---|---|---|---|
| The Metaprogramming Minefield | Ruby | [rails/rails](https://github.com/rails/rails) | MIT |
| The Orchestration Giant | Go | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | Apache-2.0 |
| The Enterprise OOP Labyrinth | Java | [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | Apache-2.0 |
| The Homoiconic Trap | Scheme | [racket/racket](https://github.com/racket/racket) | see upstream `LICENSE` |
| The Pure Functional Trap | Haskell | [jgm/pandoc](https://github.com/jgm/pandoc) | GPL-2.0-or-later |
| The Reactive Mobile Tree | Dart | [flutter/flutter](https://github.com/flutter/flutter) | BSD-3-Clause |
| The Self-Hosting Compiler | C# | [dotnet/roslyn](https://github.com/dotnet/roslyn) | MIT |
| The Immutable Ledger | Solidity | [OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | MIT |
| The Legacy Regex Trap | JavaScript | [jquery/jquery](https://github.com/jquery/jquery) | MIT |
| The Legacy Regex Trap | Perl | *not yet recorded* | *not yet recorded* |
| The Embedded Hardware Boundary | C | [id-Software/DOOM](https://github.com/id-Software/DOOM) | see upstream `LICENSE` |
| The Embedded Hardware Boundary | C++ | [godotengine/godot](https://github.com/godotengine/godot) | MIT |

## What's still missing

- Exact commit/file provenance for every paradigm above, plus the other 44 language/format
  directories under `data/` that aren't in this table yet (Apollo-11's AGC flight software,
  curl, and dozens more referenced in `README.md` and `tests/README.md` but not yet itemized
  here individually).
- A source/license entry for the Perl side of the Legacy Regex Trap paradigm.

Tracked in [#4](https://github.com/squid-protocol/language-crucible/issues/4). If you're
contributing a new paradigm, add its row here in the same PR — see
[`README.md`'s Contributing section](README.md#contributing) for the full process.
