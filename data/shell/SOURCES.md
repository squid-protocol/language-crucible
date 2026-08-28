# Shell corpus sources

This folder was substantially expanded on 2026-08-28 (same pass methodology
as `../cobol/SOURCES.md` / `../jcl/SOURCES.md`): every file below is real,
unmodified source pulled from a full clone of the named upstream repository
in the `gitgalaxy/data` full-repo pool, selected with a directory-diverse
sampler (round-robins across subdirectories so each repo's sample spans
build/CI/test/tooling subsystems instead of clustering alphabetically), and
scanned for GitGalaxy-forge contamination markers before inclusion (none
found in any shell candidate — see `../cobol/SOURCES.md` for the JCL case
where contamination *was* found and excluded).

Where a repo contributed many files that share a basename across different
subdirectories (e.g. `runme.sh`, `build.sh`), the destination filename was
disambiguated with a `<parentdir>__<name>` prefix rather than silently
overwriting — this was caught and fixed mid-pass (an initial flat-copy run
silently dropped up to a third of some repos' intended sample to basename
collisions).

| Repo folder | Files | Upstream | License | Notes |
|---|---|---|---|---|
| `kubernetes` | 28 | https://github.com/kubernetes/kubernetes | Apache License 2.0 | New. `hack/`, `build/`, `test/` shell tooling from the canonical container-orchestration project. |
| `freebsd-src` | 28 | https://github.com/freebsd/freebsd-src | BSD (multiple clauses; see repo `LICENSE`) | New. Classic BSD userland/kernel build & release-engineering scripts. |
| `linux` | 28 | https://github.com/torvalds/linux | GNU GPL v2.0 | New. `scripts/` build tooling from the Linux kernel. |
| `serenity` | 25 | https://github.com/SerenityOS/serenity | BSD 2-Clause License | New. Modern hobby-OS `Meta/` build/packaging scripts. |
| `illumos-gate` | 25 | https://github.com/illumos/illumos-gate | CDDL-1.0 (per-file headers; no single top-level LICENSE in this clone) | New. Solaris-lineage enterprise Unix — strong `ksh`/Bourne-shell idiom diversity. |
| `haiku` | 22 | https://github.com/haiku/haiku | MIT License | New. |
| `darwin-xnu` | 20 | https://github.com/apple/darwin-xnu | Apple Public Source License 2.0 | New. All available shell scripts included. |
| `reactos` | 14 | https://github.com/reactos/reactos | GNU GPL v2.0 (LGPL for some library components, see `COPYING.LIB`) | New. All available shell scripts included. |
| `curl` | 22 | https://github.com/curl/curl | curl license (OSI-approved MIT/X derivative) | New. |
| `ansible` | 20 | https://github.com/ansible/ansible | GNU GPL v3.0 | New. |
| `moby` | 17 | https://github.com/moby/moby | Apache License 2.0 | New. All available shell scripts included. |
| `sqlite` | 13 | https://github.com/sqlite/sqlite | Public Domain (see repo `LICENSE.md` "blessing") | New. All available shell scripts included. |
| `brew` | 10 | https://github.com/Homebrew/brew | BSD 2-Clause License | Pre-existing folder, unchanged. Note: most files here (`brew.rb`, `cask.rb`, `formula.rb`, etc.) are Ruby, not shell — only `brew` and `brew_completion.bash` are actually shell script. Left as-is rather than pruned in this pass; flagged here for future cleanup. |

**Total: ~272 real shell files across 13 repos** (up from 10 files / 1 repo, most of which weren't even shell).

## Licenses deliberately avoided

`elasticsearch` and current-generation `redis` were considered and dropped:
both have moved off purely-OSI licensing to source-available/tri-license
schemes (Elastic License 2.0 / SSPL / AGPL for Elasticsearch; RSALv2 / SSPLv1
/ AGPLv3 for Redis 8+) that would complicate this corpus's licensing story.
Simpler, unambiguously-licensed repos were used instead.
