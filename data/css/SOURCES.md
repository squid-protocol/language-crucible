# css corpus sources

Provenance for this category is mixed. The three folders at the top of the
table predate the issue #4 audit (squid-protocol/language-crucible#4 — full
per-repo attribution across `data/`) and are `pool-reference`: a same-named
clone was found in the `gitgalaxy/data` pool and its *current* commit is
recorded, but that has not been verified as the exact snapshot these files
were originally copied from. The eight folders below them were added
2026-08-30 as a deliberate CSS-coverage expansion, copied directly from
same-named clones in the pool at a known commit — those are `exact`. See the
root `SOURCES.md` for the full methodology and what each confidence level
means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `element` | 3 | https://github.com/ElemeFE/element.git | `c345bb453bf11badb4831a6a3f600c9372b3a336` | MIT License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `odoo` | 3 | https://github.com/odoo/odoo.git | `93095e1e9507fde18aefe91aac8c9cb53cadc2f3` | GNU LGPL | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `wordpress` | 3 | https://github.com/WordPress/WordPress.git | `5f913088f4a04816043be019737a6e4590eae845` | GNU GPL v2.0 | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool and reading that clone's current commit — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. 1 deeper same-named git clone(s) also found (likely vendored copies within other projects, not used): /srv/storage_16tb/projects/gitgalaxy/data/corpus_php/WordPress. |
| `bootstrap_dist` | 4 | https://github.com/twbs/bootstrap | `060ff24924a2be67feb309b121b32559a549d02c` | MIT License | Bootstrap's compiled `dist/css` — reboot, grid and full RTL sheets. Machine-generated CSS: exhaustive selector lists, logical-property RTL mirrors, `/*# sourceMappingURL */` trailers. High selector density, zero preprocessor syntax. |
| `bootstrap_minified` | 4 | https://github.com/twbs/bootstrap | `060ff24924a2be67feb309b121b32559a549d02c` | MIT License | The same build, minified: everything on one line, no whitespace between rules. Tests rule/selector boundary detection with no newlines to anchor on. |
| `cytoscape_docs` | 4 | https://github.com/cytoscape/cytoscape.js | `816e98077a6447f491efec81b22cab19e5a56f25` | MIT License | Vendored third-party CSS shipped inside the cytoscape.js docs site — a highlight.js syntax theme, a CSS reset, and the hand-written docs stylesheet. A repo carrying stylesheets it didn't author. |
| `gutenberg_css_modules` | 5 | https://github.com/WordPress/gutenberg | `4af0efd09488abc25e84933c634230ac884cc2f8` | GNU GPL v2.0 | CSS Modules (`*.module.css`) from Gutenberg's component library: `composes:` inheritance, `:global(...)` escape hatches, `var(--wp--*)` custom-property theming, plus a WordPress theme `style.css` that's mostly a metadata comment header. CSS that only resolves through a bundler. |
| `mediawiki_resources` | 6 | https://github.com/wikimedia/mediawiki | `8863834e673e4f297bfbc40cd4d54ee9027ad876` | GNU GPL v2.0 | Small, old-school hand-authored MediaWiki module stylesheets (history diff, API sandbox, TOC, print). Terse, single-purpose, decades of accreted browser-compatibility idiom. |
| `revealjs_themes` | 7 | https://github.com/hakimel/reveal.js | `8bbbcf83104b817f5882a0e04772b9f9e26b265b` | MIT License | Compiled reveal.js theme sheets (dracula, night, blood, simple, serif) plus `reveal.css` and `reset.css`. Heavy `:root` custom-property blocks, `@media` print rules, long transition/transform declaration lists. |
| `tailwindcss_atrules` | 6 | https://github.com/tailwindlabs/tailwindcss | `d7fc281a0e678bf92f0e82f4ab1b8edfd7cb1675` | MIT License | Tailwind v4 source CSS: `@theme`, `@tailwind`, `@layer`, `@utility`, `@import "..." layer(...)` — a stylesheet that's really a DSL of custom at-rules. Includes one-line files (`@import 'tailwindcss';`) that are almost pure directive. |
| `threejs_app_ui` | 4 | https://github.com/mrdoob/three.js | `f04b082d40e8104ea3003c13fdf9dd6db8f88971` | MIT License | Hand-written application CSS from the three.js editor and examples/manual UI: flexbox panels, dat.GUI overrides, CodeMirror skinning. Ordinary authored CSS as a contrast to the generated/preprocessed folders. |

**Total: 49 files across 11 repo folder(s)** (3 pool-reference, 8 exact).
