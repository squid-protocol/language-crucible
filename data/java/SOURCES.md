# java corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `springboot` | 8 | https://github.com/spring-projects/spring-boot | `5cecd3922fce651f13d16a85d8a29efaa7f44cfd` | Apache License 2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `flutter_android_editing_tests` | 2 | https://github.com/flutter/flutter | `75910740753c13a858bb39c3686afb71675e8dc4` | BSD-3-Clause | Security-signal coverage (gitgalaxy#4108). Cursor-movement tests over an England subdivision-flag emoji tag sequence: a negative control for Invisible Unicode Payload Smuggling since gitgalaxy#4135, which exempts well-formed U+1F3F4 + tag + U+E007F flag sequences: the signal must read 0 here. |
| `jenkins_cli` | 2 | https://github.com/jenkinsci/jenkins | `bc6a2222ce5a9e104a4f5a96653f0e879461936b` | MIT | Security-signal coverage (gitgalaxy#4108). `checkPermission(Run.UPDATE)` in a CLI command: Auth Middleware. |
| `selenium_grid_session_queue` | 3 | https://github.com/SeleniumHQ/selenium | `549261ba1cccb1d3bfa662d35d7b144607abf51c` | Apache-2.0 | Security-signal coverage (gitgalaxy#4108). Public methods next to `client.execute(...)` calls: Public API Declared Near Raw DB Sink (the sink regex is receiver-anchored `.execute(`; here it is an HTTP client). |

**Total: 15 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
