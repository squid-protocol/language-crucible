# ruby corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `rails` | 8 | https://github.com/rails/rails.git | `afd103d69abb7441da3d2ac5c737f8de3e678779` | MIT | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `rails_http_token_auth` | 2 | https://github.com/rails/rails | `afd103d69abb7441da3d2ac5c737f8de3e678779` | MIT | Security-signal coverage (gitgalaxy#4108). HTTP token-authentication tests: `before_action :authenticate` (Auth Middleware) and literal test tokens (Embedded Credentials & Keys / Hardcoded Payload Artifacts). |
| `homebrew_ruby` | 13 | https://github.com/Homebrew/brew | `ff29aa966b3127a32e5637bde7d5c0195186d6d4` | BSD 2-Clause License | Homebrew (Library/Homebrew), sampled across the tree: Sorbet type annotations (`sig {`, `T::Sig`, `# typed:`) in 5 of 12 files and `module` / `class` in 8. Typed Ruby, unlike `rails`. |
| `selenium_ruby` | 13 | https://github.com/SeleniumHQ/selenium | `549261ba1cccb1d3bfa662d35d7b144607abf51c` | Apache License 2.0 | Selenium Ruby bindings (rb/lib): `module` / `class` in 11 of 12 files, with `attr_*`, `define_method` or `def self.` metaprogramming in 6. |

**Total: 36 files across 4 repo folder(s)** (3 exact, 1 pool-reference).
