# crystal corpus sources

Generated from `data/PROVENANCE.json` by `tools/generate_sources.py`.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `crystal_stdlib_http` | 19 | https://github.com/crystal-lang/crystal | `48118b0e8f564567495228e273ef6a88d563d15f` | Apache License 2.0 | Crystal standard-library HTTP client, server, cookies and form-data code (src/http): `@[...]` annotations in 4 of 18 files, `abstract def` / `def self.` in 8, a little generic code. |
| `kemal_framework` | 13 | https://github.com/kemalcr/kemal | `da9841225d8e7968763668ac8e8dd218cfdb1882` | MIT License | Crystal web framework (src/): `def`-heavy classes and modules, with `macro` definitions or `@[...]` annotations in 4 of 12 files. Flattened names. First Crystal category, so the tree-sitter accuracy audit can measure Crystal. |

**Total: 32 files across 2 repo folder(s)** (2 exact).
