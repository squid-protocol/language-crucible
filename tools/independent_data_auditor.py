import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

def audit_physical_disk(target_path):
    root = Path(target_path).resolve()

    total_files = 0
    ext_counts = defaultdict(int)

    # Explicitly blind the auditor to Git noise and your output telemetry
    IGNORED_DIRS = {'.git', 'raw output', 'tools', 'telemetry'}

    for dirpath, dirnames, filenames in os.walk(root):
        # In-place modification to instantly prune ignored directories from the walk
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]

        for file in filenames:
            total_files += 1

            # Extract extension, grouping extensionless files explicitly
            ext = Path(file).suffix.lower()
            if not ext:
                ext = '<no_extension>'

            ext_counts[ext] += 1

    return total_files, ext_counts


# ---------------------------------------------------------------------------
# Provenance audit (squid-protocol/language-crucible issue #4)
#
# Walks every data/<language>/<repo> folder and tries to establish where it
# came from: a local LICENSE/COPYING file (if any), and a name-matched clone
# in the gitgalaxy/data full-repo pool (if the pool is present on this
# machine -- it won't be in CI, and that's fine, matching just gets skipped).
#
# This does NOT replace human review. Confidence levels exist precisely so
# nobody downstream mistakes an automated name-match for a verified fact:
#   - "exact"          verified by the person who copied the files in, against
#                       the specific pool commit they copied from. Hardcoded
#                       below for the repos this was true for -- there is no
#                       way to derive "exact" after the fact, only to record it
#                       honestly when it happens.
#   - "pool-reference"  a same-named directory was found in the pool, and its
#                       *current* HEAD commit is recorded, but nobody has
#                       verified that's the commit the data/ files actually
#                       came from (they may predate this tool, or the pool
#                       clone may have moved on since).
#   - "unknown"         no confident pool match and/or no local license file.
#                       Recorded as unknown deliberately -- per issue #4,
#                       an honest "unknown" beats an asserted-but-wrong guess.
# ---------------------------------------------------------------------------

DEFAULT_POOL_PATH = os.environ.get(
    "GITGALAXY_POOL_PATH", "/srv/storage_16tb/projects/gitgalaxy/data"
)

# Repos personally curated (2026-08-28, cobol/jcl/shell/powershell/lua/livecode
# passes) where the commit below is verified against the exact copy operation,
# not just a same-named pool directory found after the fact. Keep this in sync
# with the Commit columns in the corresponding data/<language>/SOURCES.md --
# this dict is the single source of truth those tables were written from.
EXACT_PROVENANCE = {
    ("cobol", "cics-genapp"): ("https://github.com/cicsdev/cics-genapp", "63eca1b670d9199637bdc2ca7df6e4189a58c892", "Eclipse Public License 2.0"),
    ("cobol", "cics-banking-sample-application-cbsa"): ("https://github.com/cicsdev/cics-banking-sample-application-cbsa", "46cbda52051d5cded017d72ad653df68b8ec1b60", "Eclipse Public License 2.0"),
    ("cobol", "CICS-Cobol"): ("https://github.com/mainframe-projects/CICS-Cobol", "3fd4d46cabc39079ab198c52c235e58ab017beb7", "GNU GPL v2.0"),
    ("cobol", "cobol-programming-course"): ("https://github.com/openmainframeproject/cobol-programming-course", "11aca51998e11181925ff16c20b32c220360ff66", "CC-BY-4.0"),
    ("cobol", "zopeneditor-sample"): ("https://github.com/IBM/zopeneditor-sample", "41f70551d85233829a90f7891af2b56092b471c3", "Apache License 2.0"),
    ("cobol", "cash-account-cobol"): ("https://github.com/IBMStockTrader/cash-account-cobol", "c35db0d1f283367109bcd5dfadd76560cf53b2dc", "Apache License 2.0"),
    ("cobol", "cobrix"): ("https://github.com/AbsaOSS/cobrix", "7200b77cdebb4244137f88b48e908acfc4ccbee1", "Apache License 2.0"),
    ("cobol", "gnucobol"): ("https://github.com/paulsmith/gnucobol", "d139d06201cf0aba9d143e0f675f446c19603b36", "GNU GPL v3.0"),
    ("cobol", "che-che4z-lsp-for-cobol"): ("https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol", "dd1133952579575082914476fa699667b8790e1d", "Eclipse Public License 2.0"),
    # cobol 2x pass (2026-08-30). Same convention: curated subsets copied from
    # the pool clone at the commit below, at copy time -> exact.
    ("cobol", "che-che4z_nist_ccvs85"): ("https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol", "dd1133952579575082914476fa699667b8790e1d", "Eclipse Public License 2.0"),
    ("cobol", "che-che4z_lsp_project_fixtures"): ("https://github.com/eclipse-che4z/che-che4z-lsp-for-cobol", "dd1133952579575082914476fa699667b8790e1d", "Eclipse Public License 2.0"),
    ("cobol", "cobol-check"): ("https://github.com/openmainframeproject/cobol-check", "e372dd7f436c471883bd58ac71aab49861a57e5d", "Apache License 2.0"),
    ("cobol", "cics-java-jcics-samples"): ("https://github.com/cicsdev/cics-java-jcics-samples", "11e86326f2600220cc610bdf4bee9afa77c206c0", "Apache License 2.0"),
    ("jcl", "cics-java-jcics-samples"): ("https://github.com/cicsdev/cics-java-jcics-samples", "11e86326f2600220cc610bdf4bee9afa77c206c0", "Apache License 2.0"),
    ("jcl", "cics-genapp"): ("https://github.com/cicsdev/cics-genapp", "63eca1b670d9199637bdc2ca7df6e4189a58c892", "Eclipse Public License 2.0"),
    ("jcl", "cics-banking-sample-application-cbsa"): ("https://github.com/cicsdev/cics-banking-sample-application-cbsa", "46cbda52051d5cded017d72ad653df68b8ec1b60", "Eclipse Public License 2.0"),
    ("jcl", "cobol-programming-course"): ("https://github.com/openmainframeproject/cobol-programming-course", "11aca51998e11181925ff16c20b32c220360ff66", "CC-BY-4.0"),
    ("jcl", "zopeneditor-sample"): ("https://github.com/IBM/zopeneditor-sample", "41f70551d85233829a90f7891af2b56092b471c3", "Apache License 2.0"),
    ("jcl", "cash-account-cobol"): ("https://github.com/IBMStockTrader/cash-account-cobol", "c35db0d1f283367109bcd5dfadd76560cf53b2dc", "Apache License 2.0"),
    ("shell", "kubernetes"): ("https://github.com/kubernetes/kubernetes", "da663405beb487d66c27a0220ea4073305ae9077", "Apache License 2.0"),
    ("shell", "freebsd-src"): ("https://github.com/freebsd/freebsd-src", "c70755bc0d8f703dbaa1520c15e8213a95847dd5", "BSD (multiple clauses)"),
    ("shell", "linux"): ("https://github.com/torvalds/linux", "3aae9383f42f687221c011d7ee87529398e826b3", "GNU GPL v2.0"),
    ("shell", "serenity"): ("https://github.com/SerenityOS/serenity", "c224a9b0d6c1ae4868d2b34f0bdc7e7c2cd9e1c9", "BSD 2-Clause License"),
    ("shell", "illumos-gate"): ("https://github.com/illumos/illumos-gate", "bb22c2af5c5ffa416f82a7b13a92d58240c65a83", "CDDL-1.0"),
    ("shell", "haiku"): ("https://github.com/haiku/haiku", "040fad1a4ab88eae509a1e098fe373b3041a03cf", "MIT License"),
    ("shell", "darwin-xnu"): ("https://github.com/apple/darwin-xnu", "2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32", "Apple Public Source License 2.0"),
    ("shell", "reactos"): ("https://github.com/reactos/reactos", "1ae75e00ae1e785aa8b89ef56afab36b3ad9d27c", "GNU GPL v2.0"),
    ("shell", "curl"): ("https://github.com/curl/curl", "8f3f470baec57f5e53e11fc2ecaa749201ca9c0c", "curl license"),
    ("shell", "ansible"): ("https://github.com/ansible/ansible", "8d24f0d32ffbc135cd1890c494ffa6730b994c8f", "GNU GPL v3.0"),
    ("shell", "moby"): ("https://github.com/moby/moby", "d74daf1afe932c3579fc98ffc8f4378e5357c2a0", "Apache License 2.0"),
    ("shell", "sqlite"): ("https://github.com/sqlite/sqlite", "f270460366134e350ad6e1509957f812c9700d2b", "Public Domain"),
    ("shell", "brew"): ("https://github.com/Homebrew/brew", "ff29aa966b3127a32e5637bde7d5c0195186d6d4", "BSD 2-Clause License"),
    ("powershell", "core"): ("https://github.com/PowerShell/PowerShell", "a17f1761eca57d90856062e35add0f013a1c703f", "MIT License"),
    ("powershell", "PowerToys"): ("https://github.com/microsoft/PowerToys", "4ce451edd0a66ba4fe1366ff6a912c30be59feb3", "MIT License"),
    ("powershell", "roslyn"): ("https://github.com/dotnet/roslyn", "849bed61024b171e673b9a1fac565b30e3ae1934", "MIT License"),
    ("powershell", "runtime"): ("https://github.com/dotnet/runtime", "aba46e33ea5ddd45d90e5c6a8b46bba6744ddc9a", "MIT License"),
    ("powershell", "nvda"): ("https://github.com/nvaccess/nvda", "a94c7f85bd2e8e3e290b314244ea921c4cd01b4c", "GNU GPL v2.0"),
    ("lua", "redis"): ("https://github.com/redis/redis", "2ba0194fbe5820cab8602bfa633a7d27e97cabdd", "MIT License (vendored)"),
    ("lua", "cosmopolitan"): ("https://github.com/jart/cosmopolitan", "eedf7d2db6e5ee0e228862690339c166a3f003a7", "ISC License"),
    ("lua", "pandoc"): ("https://github.com/jgm/pandoc", "7777de6adb166d92b4c9ee4b24054637ab8477b7", "GNU GPL v2.0-or-later"),
    ("lua", "freebsd-src"): ("https://github.com/freebsd/freebsd-src", "c70755bc0d8f703dbaa1520c15e8213a95847dd5", "BSD (multiple clauses)"),
    ("lua", "darwin-xnu"): ("https://github.com/apple/darwin-xnu", "2ff845c2e033bd0ff64b5b6aa6063a1f8f65aa32", "Apple Public Source License 2.0"),
    ("livecode", "livecode"): ("https://github.com/livecode/livecode", "4606a10ea10b16d5071d0f9f263ccdd7ede8b31d", "GNU GPL v3.0 (with ATL/OpenSSL exception)"),
    # html / css expansion (2026-08-30). Each folder is a curated subset copied
    # from the same-named clone in the gitgalaxy/data pool at the commit below --
    # recorded exact because this is the copy operation, not a later name-match.
    ("html", "threejs_shader_examples"): ("https://github.com/mrdoob/three.js", "f04b082d40e8104ea3003c13fdf9dd6db8f88971", "MIT License"),
    ("html", "revealjs_decks"): ("https://github.com/hakimel/reveal.js", "8bbbcf83104b817f5882a0e04772b9f9e26b265b", "MIT License"),
    ("html", "html5_boilerplate"): ("https://github.com/h5bp/html5-boilerplate", "ce8ad3c32e1744da4adecb978797168d5ee7df51", "MIT License"),
    ("html", "jquery_test_fixtures"): ("https://github.com/jquery/jquery", "b43c8046f5196186fcba0860dae1680f42797f93", "MIT License"),
    ("html", "vscode_webviews"): ("https://github.com/microsoft/vscode", "a8d7dcd8683eef847562052b722d477b5134ef76", "MIT License"),
    ("html", "angular_adev_templates"): ("https://github.com/angular/angular", "9d76ac82290e047f1481fb38bd95233e951a77de", "MIT License"),
    ("html", "playwright_dom_fixtures"): ("https://github.com/microsoft/playwright", "ff6d41b3cb7bbf31f8d5b75793fec38c0151ca44", "Apache License 2.0"),
    ("html", "cesium_sandcastle"): ("https://github.com/CesiumGS/cesium", "0becdbfc17b1015c338e147103876e2ac049f91e", "Apache License 2.0"),
    ("css", "bootstrap_dist"): ("https://github.com/twbs/bootstrap", "060ff24924a2be67feb309b121b32559a549d02c", "MIT License"),
    ("css", "bootstrap_minified"): ("https://github.com/twbs/bootstrap", "060ff24924a2be67feb309b121b32559a549d02c", "MIT License"),
    ("css", "tailwindcss_atrules"): ("https://github.com/tailwindlabs/tailwindcss", "d7fc281a0e678bf92f0e82f4ab1b8edfd7cb1675", "MIT License"),
    ("css", "mediawiki_resources"): ("https://github.com/wikimedia/mediawiki", "8863834e673e4f297bfbc40cd4d54ee9027ad876", "GNU GPL v2.0"),
    ("css", "threejs_app_ui"): ("https://github.com/mrdoob/three.js", "f04b082d40e8104ea3003c13fdf9dd6db8f88971", "MIT License"),
    ("css", "gutenberg_css_modules"): ("https://github.com/WordPress/gutenberg", "4af0efd09488abc25e84933c634230ac884cc2f8", "GNU GPL v2.0"),
    ("css", "cytoscape_docs"): ("https://github.com/cytoscape/cytoscape.js", "816e98077a6447f491efec81b22cab19e5a56f25", "MIT License"),
    ("css", "revealjs_themes"): ("https://github.com/hakimel/reveal.js", "8bbbcf83104b817f5882a0e04772b9f9e26b265b", "MIT License"),
    # groovy expansion (2026-08-30). Curated subsets copied from the pool clone
    # at the commit below, at copy time -> exact. (The pre-existing `gradle` and
    # `spock` folders hold only .java and stay pool-reference.)
    ("groovy", "gradle_dsl_snippets"): ("https://github.com/gradle/gradle", "db62c2f2b404217cb6a7eef2598c6e84ab08fa27", "Apache License 2.0"),
    ("groovy", "gradle_buildlogic_groovy"): ("https://github.com/gradle/gradle", "db62c2f2b404217cb6a7eef2598c6e84ab08fa27", "Apache License 2.0"),
    ("groovy", "gradle_integtest_specs"): ("https://github.com/gradle/gradle", "db62c2f2b404217cb6a7eef2598c6e84ab08fa27", "Apache License 2.0"),
    ("groovy", "gradle_sample_task_classes"): ("https://github.com/gradle/gradle", "db62c2f2b404217cb6a7eef2598c6e84ab08fa27", "Apache License 2.0"),
    ("groovy", "spock_specs"): ("https://github.com/spockframework/spock", "b71e3d7590dae28d608aa92f90b45bef33aaeda8", "Apache License 2.0"),
    ("groovy", "spock_core_groovy"): ("https://github.com/spockframework/spock", "b71e3d7590dae28d608aa92f90b45bef33aaeda8", "Apache License 2.0"),
    ("groovy", "spock_smoke_specs"): ("https://github.com/spockframework/spock", "b71e3d7590dae28d608aa92f90b45bef33aaeda8", "Apache License 2.0"),
    ("groovy", "spring_boot_gradle"): ("https://github.com/spring-projects/spring-boot", "5cecd3922fce651f13d16a85d8a29efaa7f44cfd", "Apache License 2.0"),
    ("groovy", "flutter_android_gradle"): ("https://github.com/flutter/flutter", "75910740753c13a858bb39c3686afb71675e8dc4", "BSD 3-Clause License"),
    ("groovy", "kotlin_build_gradle"): ("https://github.com/JetBrains/kotlin", "bcdc78880f23dd07f10607332e8a89a5e72d4e9a", "Apache License 2.0"),
    ("groovy", "godot_android_gradle"): ("https://github.com/godotengine/godot", "4a919adccf8e398aceca75399c539078c54fe97f", "MIT License"),
    ("groovy", "retrofit_gradle"): ("https://github.com/square/retrofit", "77e6ba21d9ba372d1b23ef29881912910da23347", "Apache License 2.0"),
    ("groovy", "jenkins_view_groovy"): ("https://github.com/jenkinsci/jenkins", "bc6a2222ce5a9e104a4f5a96653f0e879461936b", "MIT License"),
    ("groovy", "fineract_gradle_plugin"): ("https://github.com/apache/fineract", "e6e5a4b6eec5a33d327546c640e6b7f281b5ae42", "Apache License 2.0"),
}

# Hand-corrected matches for generically-named repo folders (e.g. "core",
# "zig") where automated name-matching found a same-named-but-wrong pool
# candidate. Verified by inspecting file contents against the pool clone
# (e.g. data/go/core/proc.go, mgc.go match golang/go's src/runtime/, not
# either of the automated matcher's two "core"-named candidates). Confidence
# stays "pool-reference", not "exact" -- this confirms the pool clone is
# plausibly the source by content inspection, not that it's the verified
# exact commit the original copy came from.
MANUAL_OVERRIDE = {
    ("go", "core"): ("https://github.com/golang/go", "d247ed00e498e9717fb7c80d126bee5a8afdb4e8",
                      "Automated matcher found two wrong same-depth 'core' candidates "
                      "(vuejs/core, home-assistant/core); contents (proc.go, mgc.go, "
                      "syscall_linux.go) are unmistakably Go's own runtime source."),
    ("zig", "zig"): ("https://github.com/ziglang/zig", "738d2be9d6b6ef3ff3559130c05159ef53336224",
                      "Automated matcher found a case-variant 'Zig' candidate "
                      "(TheAlgorithms/Zig, an algorithms-teaching repo); contents "
                      "(Compilation.zig, Sema.zig, InternPool.zig) are unmistakably the "
                      "self-hosting Zig compiler's own source."),
}

# Repo folders known to have real content but deliberately no license/commit
# to assert -- recorded as unknown by design, not by oversight.
KNOWN_UNKNOWN = {
    ("cobol", "aws-mainframe-modernization-carddemo"):
        "Embedded fixture inside che-che4z-lsp-for-cobol/tests/test_files/, not a standalone "
        "clone; upstream is publicly MIT-licensed but that has not been independently verified "
        "against this exact copy. See data/cobol/SOURCES.md caveats.",
    ("cobol", "gnucobol_internals"):
        "Pre-existing folder from before this audit tooling existed; original source clone/commit "
        "was not recorded at the time and cannot be reconstructed with confidence.",
    ("python", "meow_turtle"):
        "Original embedded-firmware content from the repo owner's personal LEGO-sorter project "
        "(\"Ninelives\"): RP2040/RP2350 MicroPython with PIO assembly embedded in Python via "
        "@rp2.asm_pio. Contributed directly, not cloned -- no upstream repo and no license file. "
        "Recorded unknown by design, not oversight.",
}

LICENSE_SIGNATURES = [
    ("MIT License", re.compile(r"\bMIT License\b", re.I)),
    ("Apache License 2.0", re.compile(r"Apache License,?\s*Version 2\.0", re.I)),
    ("GNU GPL v3.0", re.compile(r"GNU GENERAL PUBLIC LICENSE\s*\n?\s*Version 3", re.I)),
    ("GNU GPL v2.0", re.compile(r"GNU GENERAL PUBLIC LICENSE\s*\n?\s*Version 2", re.I)),
    ("GNU LGPL", re.compile(r"GNU LESSER GENERAL PUBLIC LICENSE", re.I)),
    ("BSD License", re.compile(r"Redistribution and use in source and binary forms", re.I)),
    ("ISC License", re.compile(r"\bISC License\b", re.I)),
    ("Mozilla Public License 2.0", re.compile(r"Mozilla Public License,?\s*v\.?\s*2\.0", re.I)),
    ("Eclipse Public License 2.0", re.compile(r"Eclipse Public License\s*-?\s*v\.?\s*2\.0", re.I)),
    ("Eclipse Public License 1.0", re.compile(r"Eclipse Public License\s*-?\s*v\.?\s*1\.0", re.I)),
    ("Creative Commons", re.compile(r"Creative Commons", re.I)),
    ("CDDL", re.compile(r"Common Development and Distribution License", re.I)),
    ("Public Domain", re.compile(r"public domain", re.I)),
]


def normalize(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def detect_license(repo_dir):
    for pattern in ("LICENSE*", "COPYING*", "COPYRIGHT*", "license*"):
        for f in repo_dir.glob(pattern):
            if f.is_file():
                try:
                    text = f.read_text(errors="ignore")[:4000]
                except Exception:
                    continue
                for label, rx in LICENSE_SIGNATURES:
                    if rx.search(text):
                        return label, f.name
                return "present but unrecognized (see file)", f.name
    return None, None


def find_pool_matches(pool_root, repo_name, max_depth=3):
    pool_root = Path(pool_root)
    if not pool_root.exists():
        return []
    target = normalize(repo_name)
    matches = []
    base_depth = len(pool_root.parts)
    for dirpath, dirnames, _ in os.walk(pool_root):
        depth = len(Path(dirpath).parts) - base_depth
        if depth >= max_depth:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in (".git", ".gitgalaxy")]
        for d in list(dirnames):
            if normalize(d) == target:
                matches.append(Path(dirpath) / d)
    # Shallowest path first: os.walk's traversal order is filesystem-dependent,
    # not depth-ordered, so without this a nested vendored copy could easily
    # win over the genuine top-level clone by luck of directory-entry order.
    matches.sort(key=lambda p: len(p.parts))
    return matches


def git_info(repo_path):
    if not (repo_path / ".git").exists():
        return None, None
    try:
        url = subprocess.run(
            ["git", "-C", str(repo_path), "remote", "get-url", "origin"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip() or None
        commit = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip() or None
        return url, commit
    except Exception:
        return None, None


def audit_provenance(data_root, pool_root=DEFAULT_POOL_PATH):
    data_root = Path(data_root).resolve()
    entries = []
    pool_available = Path(pool_root).exists()
    if not pool_available:
        print(f"NOTE: pool path {pool_root} not found on this machine -- "
              f"skipping pool name-matching, only local LICENSE detection + "
              f"hardcoded exact/known-unknown entries will be used.\n")

    for lang_dir in sorted(p for p in data_root.iterdir() if p.is_dir()):
        category = lang_dir.name
        repo_dirs = sorted(p for p in lang_dir.iterdir() if p.is_dir())
        for repo_dir in repo_dirs:
            repo_name = repo_dir.name
            file_count = sum(1 for _ in repo_dir.rglob("*") if _.is_file())
            key = (category, repo_name)

            if key in EXACT_PROVENANCE:
                url, commit, license_name = EXACT_PROVENANCE[key]
                entries.append({
                    "category": category, "repo": repo_name, "path": str(repo_dir.relative_to(data_root.parent)),
                    "files": file_count, "url": url, "commit": commit,
                    "license": license_name, "confidence": "exact", "note": None,
                })
                continue

            if key in MANUAL_OVERRIDE:
                url, commit, note = MANUAL_OVERRIDE[key]
                license_name, _ = detect_license(repo_dir)
                entries.append({
                    "category": category, "repo": repo_name, "path": str(repo_dir.relative_to(data_root.parent)),
                    "files": file_count, "url": url, "commit": commit,
                    "license": license_name, "confidence": "pool-reference", "note": note,
                })
                continue

            if key in KNOWN_UNKNOWN:
                license_name, _ = detect_license(repo_dir)
                entries.append({
                    "category": category, "repo": repo_name, "path": str(repo_dir.relative_to(data_root.parent)),
                    "files": file_count, "url": None, "commit": None,
                    "license": license_name, "confidence": "unknown", "note": KNOWN_UNKNOWN[key],
                })
                continue

            license_name, license_file = detect_license(repo_dir)
            candidates = find_pool_matches(pool_root, repo_name) if pool_available else []

            # Not every same-named directory is a usable git clone -- e.g. a
            # pypi_top_200/<pkg> snapshot is a flat pip-installed package with no
            # .git at all. Only candidates that actually resolve to a remote URL
            # are real matches; try shallowest-first among *those*.
            git_candidates = []
            for c in candidates:
                url, commit = git_info(c)
                if url:
                    git_candidates.append((c, url, commit))

            if git_candidates:
                chosen_path, url, commit = git_candidates[0]
                if not license_name:
                    # Fall back to the matched pool clone's own LICENSE -- still not
                    # proof this exact governs these specific copied files, but a
                    # reasonable inference worth surfacing rather than leaving blank.
                    pool_license, pool_license_file = detect_license(chosen_path)
                    if pool_license:
                        license_name = f"{pool_license} (from pool clone's {pool_license_file}, not found locally)"
                note = None
                min_depth = len(chosen_path.parts)
                tied = [gc for gc in git_candidates if len(gc[0].parts) == min_depth]
                if len(tied) > 1:
                    # Genuine ambiguity: multiple *valid git* candidates at the same
                    # (shallowest) depth, so "prefer shallowest" doesn't disambiguate.
                    note = (f"AMBIGUOUS: {len(tied)} same-named git clones at the same depth "
                            f"({', '.join(str(gc[0]) for gc in tied)}); using the first "
                            f"arbitrarily. Needs human review.")
                elif len(git_candidates) > 1:
                    note = (f"{len(git_candidates) - 1} deeper same-named git clone(s) also found "
                            f"(likely vendored copies within other projects, not used): "
                            f"{', '.join(str(gc[0]) for gc in git_candidates[1:])}.")
                entries.append({
                    "category": category, "repo": repo_name, "path": str(repo_dir.relative_to(data_root.parent)),
                    "files": file_count, "url": url, "commit": commit,
                    "license": license_name, "confidence": "pool-reference", "note": note,
                })
                continue

            entries.append({
                "category": category, "repo": repo_name, "path": str(repo_dir.relative_to(data_root.parent)),
                "files": file_count, "url": None, "commit": None,
                "license": license_name,
                "confidence": "unknown",
                "note": "No confidently-matched pool clone found." + (
                    f" Local license file detected ({license_file})." if license_file else " No local license file either."
                ),
            })

    return entries


def print_provenance_summary(entries):
    by_confidence = defaultdict(int)
    for e in entries:
        by_confidence[e["confidence"]] += 1
    print("--- PROVENANCE COVERAGE ---")
    print(f"Total repo-folders audited: {len(entries)}")
    for level in ("exact", "pool-reference", "unknown"):
        print(f"  {level:>15}: {by_confidence.get(level, 0)}")
    ambiguous = [e for e in entries if e.get("note") and "AMBIGUOUS" in e["note"]]
    if ambiguous:
        print(f"\n  {len(ambiguous)} entries flagged AMBIGUOUS -- needs human review before trusting:")
        for e in ambiguous:
            print(f"    - {e['path']}: {e['note']}")


if __name__ == "__main__":
    # Smart Path Resolution
    script_dir = Path(__file__).parent.resolve()

    args = sys.argv[1:]
    provenance_mode = "--provenance" in args
    args = [a for a in args if a != "--provenance"]

    # 1. Did the user provide a specific path?
    if args:
        target = Path(args[0]).resolve()
    # 2. Is the script being run from inside the 'tools' directory?
    elif script_dir.name == "tools":
        target = script_dir.parent / "data"
    # 3. Otherwise, look for the 'data' folder in the current directory
    else:
        target = Path.cwd() / "data"
        if not target.exists():
            target = Path.cwd()

    if not target.exists():
        print(f"Error: Target path '{target}' does not exist.")
        sys.exit(1)

    if provenance_mode:
        print(f"=== PROVENANCE AUDIT: {target} ===\n")
        entries = audit_provenance(target)
        out_path = target / "PROVENANCE.json"
        out_path.write_text(json.dumps(entries, indent=2))
        print(f"Wrote {len(entries)} entries to {out_path}\n")
        print_provenance_summary(entries)
        sys.exit(0)

    print(f"=== PHYSICAL DISK AUDIT: {target} ===\n")

    total, exts = audit_physical_disk(target)

    print(f"--- ABSOLUTE TOTAL FILES: {total} ---\n")

    print("--- COMPOSITION BY EXTENSION (Complete) ---")
    sorted_exts = sorted(exts.items(), key=lambda x: x[1], reverse=True)
    for ext, count in sorted_exts:
        print(f"{count:>7}  {ext}")
