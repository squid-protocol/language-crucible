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

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `kubernetes` | 28 | https://github.com/kubernetes/kubernetes | `da663405beb487d66c27a0220ea4073305ae9077` | Apache License 2.0 | New. `hack/`, `build/`, `test/` shell tooling from the canonical container-orchestration project. |
| `freebsd-src` | 28 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD (multiple clauses; see repo `LICENSE`) | New. Classic BSD userland/kernel build & release-engineering scripts. |
| `linux` | 28 | https://github.com/torvalds/linux | `3aae9383f42f687221c011d7ee87529398e826b3` | GNU GPL v2.0 | New. `scripts/` build tooling from the Linux kernel. |
| `serenity` | 25 | https://github.com/SerenityOS/serenity | `c224a9b0d6c1ae4868d2b34f0bdc7e7c2cd9e1c9` | BSD 2-Clause License | New. Modern hobby-OS `Meta/` build/packaging scripts. |
| `illumos-gate` | 25 | https://github.com/illumos/illumos-gate | `bb22c2af5c5ffa416f82a7b13a92d58240c65a83` | CDDL-1.0 (per-file headers; no single top-level LICENSE in this clone) | New. Solaris-lineage enterprise Unix — strong `ksh`/Bourne-shell idiom diversity. |
| `haiku` | 22 | https://github.com/haiku/haiku | `040fad1a4ab88eae509a1e098fe373b3041a03cf` | MIT License | New. |
| `darwin-xnu` | 20 | https://github.com/apple/darwin-xnu | `2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32` | Apple Public Source License 2.0 | New. All available shell scripts included. |
| `reactos` | 14 | https://github.com/reactos/reactos | `1ae75e00ae1e785aa8b89ef56afab36b3ad9d27c` | GNU GPL v2.0 (LGPL for some library components, see `COPYING.LIB`) | New. All available shell scripts included. |
| `curl` | 22 | https://github.com/curl/curl | `8f3f470baec57f5e53e11fc2ecaa749201ca9c0c` | curl license (OSI-approved MIT/X derivative) | New. |
| `ansible` | 20 | https://github.com/ansible/ansible | `8d24f0d32ffbc135cd1890c494ffa6730b994c8f` | GNU GPL v3.0 | New. |
| `moby` | 17 | https://github.com/moby/moby | `d74daf1afe932c3579fc98ffc8f4378e5357c2a0` | Apache License 2.0 | New. All available shell scripts included. |
| `sqlite` | 13 | https://github.com/sqlite/sqlite | `f270460366134e350ad6e1509957f812c9700d2b` | Public Domain (see repo `LICENSE.md` "blessing") | New. All available shell scripts included. |
| `brew` | 10 | https://github.com/Homebrew/brew | `ff29aa966b3127a32e5637bde7d5c0195186d6d4` | BSD 2-Clause License | Pre-existing folder, unchanged. Note: most files here (`brew.rb`, `cask.rb`, `formula.rb`, etc.) are Ruby, not shell — only `brew` and `brew_completion.bash` are actually shell script. Left as-is rather than pruned in this pass; flagged here for future cleanup. |

**Total: ~272 real shell files across 13 repos** (up from 10 files / 1 repo, most of which weren't even shell).

Commits above are the exact `HEAD` of the corresponding clone in the
`gitgalaxy/data` pool at the moment these files were copied (2026-08-28),
including `brew`'s, backfilled retroactively during the issue #4 provenance
pass since its clone was still present in the pool.

## Licenses deliberately avoided

`elasticsearch` and current-generation `redis` were considered and dropped:
both have moved off purely-OSI licensing to source-available/tri-license
schemes (Elastic License 2.0 / SSPL / AGPL for Elasticsearch; RSALv2 / SSPLv1
/ AGPLv3 for Redis 8+) that would complicate this corpus's licensing story.
Simpler, unambiguously-licensed repos were used instead.
