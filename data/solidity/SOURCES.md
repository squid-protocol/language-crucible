# solidity corpus sources

Provenance recorded 2026-08-28 as part of the issue #4 audit (squid-protocol/language-crucible#4 — full per-repo attribution across `data/`). This category predates that audit, so most entries below are `pool-reference` confidence: a same-named clone was found in the `gitgalaxy/data` full-repo pool and its *current* commit is recorded, but that has not been verified as the exact snapshot these files were originally copied from. See the root `SOURCES.md` for the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `openzeppelin` | 8 | https://github.com/OpenZeppelin/openzeppelin-contracts | `9cfdccd35350f7bcc585cf2ede08cd04e7f0ec10` | MIT License | Verified by content on 2026-09-30: every file is identical, apart from line endings, to a file in this repository at this commit. |
| `openzeppelin_tokens` | 11 | https://github.com/OpenZeppelin/openzeppelin-contracts | `9cfdccd35350f7bcc585cf2ede08cd04e7f0ec10` | MIT License | OpenZeppelin token contracts (contracts/token): `abstract contract` / `interface` / `library` in 9 of 10 files, `modifier` / `event` / `error` in 4, and a `pragma` line in all 10. The token subsystem, beside the access-control, governance and proxy files in `openzeppelin`. |
| `solady_utils` | 13 | https://github.com/Vectorized/solady | `258f67cc71e39cff307b726939ade17e9d8bcf5c` | MIT License | Solady gas-optimised contracts (src/): inline `assembly` blocks in 11 of 12 files, `library` / `abstract contract` / `interface` in 11, `pragma` in all 12. Assembly-heavy Solidity unlike OpenZeppelin's style. |

**Total: 32 files across 3 repo folder(s)** (2 exact, 1 content-verified).
