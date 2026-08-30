# html corpus sources

Provenance for this category is mixed. The seven folders at the top of the
table predate the issue #4 audit (squid-protocol/language-crucible#4 — full
per-repo attribution across `data/`) and are `unknown`: no same-named clone
could be confidently matched in the `gitgalaxy/data` pool, so no upstream
commit is asserted. The eight folders below them were added 2026-08-30 as a
deliberate HTML-coverage expansion, copied directly from same-named clones in
the pool at a known commit — those are `exact`. See the root `SOURCES.md` for
the full methodology and what each confidence level means.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `baseline` | 2 | unknown | unknown | unknown | No confidently-matched pool clone found. No local license file either. |
| `cpython_jinja` | 4 | unknown | unknown | present but unrecognized (see file) | No confidently-matched pool clone found. Local license file detected (LICENSE.txt). |
| `odoo_mako` | 4 | unknown | unknown | GNU LGPL | No confidently-matched pool clone found. Local license file detected (LICENSE.txt). |
| `polyglot_emscripten` | 2 | unknown | unknown | present but unrecognized (see file) | No confidently-matched pool clone found. Local license file detected (LICENSE.txt). |
| `polyglot_odoo` | 2 | unknown | unknown | GNU LGPL | No confidently-matched pool clone found. Local license file detected (LICENSE.txt). |
| `polyglot_vscode` | 1 | unknown | unknown | unknown | No confidently-matched pool clone found. No local license file either. |
| `wordpress_blocks` | 4 | unknown | unknown | GNU GPL v2.0 | No confidently-matched pool clone found. Local license file detected (LICENSE.txt). |
| `angular_adev_templates` | 6 | https://github.com/angular/angular | `9d76ac82290e047f1481fb38bd95233e951a77de` | MIT License | Component templates from the angular.dev app (`adev/`). Not valid standalone HTML: `@if`/`@for` control-flow blocks, `{{ }}` interpolation, `[prop]`/`(event)`/`[(ngModel)]` binding attributes, `*`-structural directives, custom elements with no DTD. Tests whether tag/attribute structure survives framework microsyntax. |
| `cesium_sandcastle` | 5 | https://github.com/CesiumGS/cesium | `0becdbfc17b1015c338e147103876e2ac049f91e` | Apache License 2.0 | Single-file CesiumJS demo apps (HelloWorld, CesiumViewer, a Sandcastle gallery entry) plus a Sandcastle `bucket.html` template with `<!-- ... -->` placeholder markers. Large inline `<script>` + `<style>` in one document — HTML/JS/CSS polyglot in a flat file. |
| `html5_boilerplate` | 5 | https://github.com/h5bp/html5-boilerplate | `ce8ad3c32e1744da4adecb978797168d5ee7df51` | MIT License | The canonical h5bp `src/` templates and their built `dist/` counterparts (index + 404). A near-baseline, well-formed control point: the delta between hand-authored source and build output of the same document. |
| `jquery_test_fixtures` | 7 | https://github.com/jquery/jquery | `b43c8046f5196186fcba0860dae1680f42797f93` | MIT License | QUnit fixtures from jQuery's `test/data/`: CSP-nonce `<script>` blocks, `<iframe>`, Trusted-Types attribute payloads, deliberately partial fragments, offset-layout tables. Unstructured legacy markup meant to be injected, not rendered whole. |
| `playwright_dom_fixtures` | 7 | https://github.com/microsoft/playwright | `ff6d41b3cb7bbf31f8d5b75793fec38c0151ca44` | Apache License 2.0 | Browser-automation test assets: out-of-process `<iframe>` trees, `history.pushState` shims, CSP `<meta>` headers, `window.stop()` mid-parse documents, huge-overflow layout pages, heading-hierarchy fixtures. Edge-case DOM designed to break crawlers. |
| `revealjs_decks` | 6 | https://github.com/hakimel/reveal.js | `8bbbcf83104b817f5882a0e04772b9f9e26b265b` | MIT License | Presentation HTML: deeply nested `<section>` slide trees, `data-*` attributes driving transitions, a 500-slide stress deck, `<script>`-driven `Reveal.initialize()`, Markdown embedded in `<section data-markdown>`. Structure-as-state. |
| `threejs_shader_examples` | 6 | https://github.com/mrdoob/three.js | `f04b082d40e8104ea3003c13fdf9dd6db8f88971` | MIT License | WebGL examples that embed GLSL in `<script type="x-shader/x-vertex">` / `x-fragment` blocks alongside `<script type="module">` import maps. Three languages (HTML, JS, GLSL) in one file, none referencing the others by import. |
| `vscode_webviews` | 6 | https://github.com/microsoft/vscode | `a8d7dcd8683eef847562052b722d477b5134ef76` | MIT License | Workbench and webview host shells: `Content-Security-Policy` `<meta>` with `{{ }}`/`nonce` substitution tokens, the `webWorkerExtensionHostIframe.html` sandbox bootstrap, OAuth `callback` and auth-media pages. Server-substituted templates that are only valid post-render. |

**Total: 67 files across 15 repo folder(s)** (7 unknown, 8 exact).
