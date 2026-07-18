# ARCHITECTURAL_BRIEF: data
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope v6.2.0 (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/all_language_repo/data` |
| **Timestamp** | `2026-07-18T14:23:53.772297+00:00` |
| **Scan Duration** | `14.37s` |
| **Git Branch** | `main` |
| **Git Commit** | `717bd4aaee536e81b798c2b8b05c89f325e24215` |
| **Git Remote** | `https://github.com/squid-protocol/language-crucible.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 765 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1093 |
| Analyzed Artifacts (Scanned) | 924 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 169 |
| Total LOC | 677864 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 84.5% |
| Dominant Lang | SCHEME |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.809 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1026 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7614 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 37 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 268 | 74314 | 29.0% |
| GO | 46 | 27740 | 5.0% |
| PLAINTEXT | 45 | 0 | 4.9% |
| C | 44 | 85526 | 4.8% |
| RUST | 43 | 36769 | 4.7% |
| PHP | 36 | 5243 | 3.9% |
| COBOL | 34 | 8698 | 3.7% |
| CPP | 33 | 48671 | 3.6% |
| ZIG | 32 | 68359 | 3.5% |
| MARKDOWN | 25 | 0 | 2.7% |
| TYPESCRIPT | 24 | 57622 | 2.6% |
| PERL | 22 | 37906 | 2.4% |
| JAVASCRIPT | 19 | 29036 | 2.1% |
| JCL | 15 | 919 | 1.6% |
| JAVA | 14 | 7262 | 1.5% |
| HTML | 13 | 664 | 1.4% |
| RUBY | 13 | 3799 | 1.4% |
| XML | 11 | 0 | 1.2% |
| AGC_ASSEMBLY | 10 | 10077 | 1.1% |
| JSON | 9 | 442 | 1.0% |
| ASSEMBLY | 8 | 2718 | 0.9% |
| POWERSHELL | 8 | 7215 | 0.9% |
| M4 | 8 | 15291 | 0.9% |
| CSHARP | 8 | 22647 | 0.9% |
| SHELL | 8 | 7129 | 0.9% |
| ABAP | 7 | 3052 | 0.8% |
| APEX | 7 | 1198 | 0.8% |
| DART | 7 | 37818 | 0.8% |
| HASKELL | 7 | 2130 | 0.8% |
| SCALA | 7 | 11171 | 0.8% |
| SOLIDITY | 7 | 1616 | 0.8% |
| SQLITE | 7 | 181 | 0.8% |
| YAML | 7 | 121 | 0.8% |
| FORTRAN | 6 | 22137 | 0.6% |
| SWIFT | 6 | 3766 | 0.6% |
| BLP | 5 | 447 | 0.5% |
| DOCKERFILE | 5 | 1016 | 0.5% |
| KOTLIN | 5 | 520 | 0.5% |
| MATLAB | 5 | 4704 | 0.5% |
| NIX | 5 | 416 | 0.5% |
| CSV | 5 | 26 | 0.5% |
| CSS | 4 | 305 | 0.4% |
| PROTO | 4 | 323 | 0.4% |
| SCHEME | 4 | 19021 | 0.4% |
| TD | 4 | 1493 | 0.4% |
| BATCH | 3 | 327 | 0.3% |
| HLO | 3 | 64 | 0.3% |
| MLIR | 3 | 241 | 0.3% |
| LIVECODE | 2 | 2531 | 0.2% |
| TCL | 2 | 3023 | 0.2% |
| YACC | 1 | 2170 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.166`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 553 | 59.8% |
| file_cluster_13 | 163 | 17.6% |
| file_cluster_0 | 50 | 5.4% |
| file_cluster_4 | 45 | 4.9% |
| file_cluster_16 | 20 | 2.2% |
| file_cluster_17 | 14 | 1.5% |
| file_cluster_12 | 2 | 0.2% |
| file_cluster_2 | 2 | 0.2% |
| file_cluster_7 | 2 | 0.2% |
| file_cluster_9 | 1 | 0.1% |
| file_cluster_6 | 1 | 0.1% |
| file_cluster_1 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 70 | 7.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 169*

**Composition by Extension & Reason:**
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Monolithic Amalgamation: 36288 LOC exceeds safe regex boundaries)
- `.go`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tar`: 7x Excluded (Explicitly Denied Extension: '.tar')
- `.test`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 37746 LOC exceeds safe regex boundaries), 1x Excluded (Machine-Generated Source Code Signature: 8582 LOC)
- `.ts`: 1x Excluded (Lexical Monotony: High structural repetition detected in 11395 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 6379 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 10824 LOC)
- `.y`: 3x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus), 1x Excluded (Machine-Generated Source Code Signature: 2161 LOC)
- `.toml`: 3x Excluded (Unsupported Extension: '.toml')
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 96 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1695 LOC)
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2342 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1541 LOC)
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xaml`: 3x Excluded (Unsupported Extension: '.xaml')
- `.cmd`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 25.0 | 11.2 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 27.3 | 6.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.8 | 31.0 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.3 | 4.8 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 95.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 34.1 | 15.6 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 43.6 | 14.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 94.5 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `fortran/wrf/regtest_hwrf.csh` (Hits: 1277)
- `fortran/wrf/regtest_nmmnest.csh` (Hits: 1216)
- `perl/exiftool/exiftool` (Hits: 344)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.

1. **os.asm** (`assembly/bootos/os.asm`) — 32 inbound connections
2. **io.ss** (`scheme/racket/io.ss`) — 17 inbound connections
3. **types.py** (`python/fastapi/fastapi/types.py`) — 7 inbound connections
4. **string.lcb** (`livecode/core/string.lcb`) — 7 inbound connections
5. **doomdef.h** (`c/doom/doomdef.h`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **editor_node.cpp** (`cpp/godot/editor_node.cpp`) — 156 outbound dependencies
2. **bevy_ecs_world.rs** (`rust/bevy/bevy_ecs_world.rs`) — 151 outbound dependencies
3. **Nodes.js** (`javascript/threejs/Nodes.js`) — 139 outbound dependencies
4. **DefaultProject.java** (`groovy/gradle/DefaultProject.java`) — 132 outbound dependencies
5. **WebMvcAutoConfiguration.java** (`java/springboot/WebMvcAutoConfiguration.java`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `lsm_mosaic` (@ `fortran/wrf/module_sf_noahdrv.F`) -> Impact: **52282.5** | LOC: 2598
- `lsm` (@ `fortran/wrf/module_sf_noahdrv.F`) -> Impact: **25993.0** | LOC: 1750
- `init_domain_rk` (@ `fortran/wrf/module_initialize_real.F`) -> Impact: **23553.3** | LOC: 4881
- `bl_init` (@ `fortran/wrf/module_physics_init.F`) -> Impact: **11718.2** | LOC: 1462
- `phy_init` (@ `fortran/wrf/module_physics_init.F`) -> Impact: **10439.6** | LOC: 1714
- `DoAutoLoad` (@ `perl/exiftool/ExifTool.pm`) -> Impact: **8710.7** | LOC: 1320
  * *Intent:* #------------------------------------------------------------------------------ # Utility to load our write routines if required (called via AUTOLOAD)...
- `vert_interp` (@ `fortran/wrf/module_initialize_real.F`) -> Impact: **7994.9** | LOC: 713
- `Anonymous_Block_[Truncated]` (@ `fortran/wrf/regtest_hwrf.csh`) -> Impact: **6310.0** | LOC: 3545
- `bz_alter_column` (@ `perl/bugzilla/DB.pm`) -> Impact: **6079.6** | LOC: 1909
- `Anonymous_Block_[Truncated]` (@ `fortran/wrf/regtest_nmmnest.csh`) -> Impact: **5974.4** | LOC: 3367

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `ape_grub_entry` (@ `assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `ape_macho` (@ `assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
  * *Intent:* Processor Supplement, Version 1.0, December 5th, 2018 */
- `netbsd.ident` (@ `assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif /* SupportsOpenbsd() */
- `ape_disk` (@ `assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `gc_sweep_free_blocks` (@ `c/micropython/gc.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Free unmarked heads and their tails
- `PyObject_Repr` (@ `c/cpython/object.c`) -> **O(2^N) [Recursive]**
- `PyObject_CallFinalizerFromDealloc` (@ `c/cpython/object.c`) -> **O(2^N) [Recursive]**
- `mp_obj_class_lookup` (@ `c/micropython/objtype.c`) -> **O(2^N) [Recursive]**
- `subtype_dealloc` (@ `c/cpython/typeobject.c`) -> **O(2^N) [Recursive]**
- `type_modified_unlocked` (@ `c/cpython/typeobject.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `fortran/wrf/regtest_hwrf.csh`) -> DB Complexity: **3767**
- `Anonymous_Block_[Truncated]` (@ `fortran/wrf/regtest_nmmnest.csh`) -> DB Complexity: **3574**
- `DoAutoLoad` (@ `perl/exiftool/ExifTool.pm`) -> DB Complexity: **1745**
  * *Intent:* #------------------------------------------------------------------------------ # Utility to load our write routines if required (called via AUTOLOAD)...
- `init_domain_rk` (@ `fortran/wrf/module_initialize_real.F`) -> DB Complexity: **1499**
- `lsm_mosaic` (@ `fortran/wrf/module_sf_noahdrv.F`) -> DB Complexity: **845**
- `ScanDir` (@ `perl/exiftool/exiftool`) -> DB Complexity: **841**
  * *Intent:* #------------------------------------------------------------------------------ # Scan directory for image files # Inputs: 0) ExifTool ref, 1) directo...
- `new` (@ `perl/spamassassin/Message.pm`) -> DB Complexity: **513**
- `lsm` (@ `fortran/wrf/module_sf_noahdrv.F`) -> DB Complexity: **454**
- `ReportTable` (@ `c/sqlite/lemon.c`) -> DB Complexity: **350**
  * *Intent:* /* Generate C source code for the parser */
- `vert_interp` (@ `fortran/wrf/module_initialize_real.F`) -> DB Complexity: **278**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scheme/racket` | 7 | 272552.62 | 34.96% | 5.8% |
| `fortran/wrf` | 14 | 210056.26 | 70.17% | 18.93% |
| `livecode/core` | 11 | 191596.75 | 32.74% | 22.84% |
| `zig/zig` | 5 | 56135.76 | 24.92% | 9.41% |
| `perl/exiftool` | 6 | 54048.14 | 51.92% | 14.37% |
| `csharp/roslyn` | 7 | 43732.48 | 17.47% | 30.29% |
| `c/cpython` | 7 | 38015.6 | 74.17% | 29.64% |
| `perl/spamassassin` | 8 | 37977.28 | 72.17% | 42.91% |
| `python/cython` | 4 | 29865.54 | 30.19% | 43.24% |
| `zig/zls` | 6 | 28215.58 | 34.96% | 7.19% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `python/cython/CodeGeneration.py` -> **100.0%** Exposure
- `python/wtfpython/2_tricky_strings.py` -> **100.0%** Exposure
- `python/wtfpython/noxfile.py` -> **100.0%** Exposure
- `cpp/NVDA/nvdaControllerInternal.cpp` -> **100.0%** Exposure
- `dockerfile/moby/builder/dockerfile/builder_unix.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `agc_assembly/apollo-11/EXECUTIVE.agc` -> **100.0%** Exposure
- `agc_assembly/apollo-11/INTERPRETER.agc` -> **100.0%** Exposure
- `assembly/cosmopolitan/loader.c` -> **100.0%** Exposure
- `c/doom/d_main.c` -> **100.0%** Exposure
- `c/cpython/compile.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `rust/wasmtime/wasmtime_pulley_interp.rs` -> **150** Orphaned Functions | **0** Duplicates
- `livecode/core/foundation-string.cpp` -> **87** Orphaned Functions | **0** Duplicates
- `python/fastapi/tests/test_path.py` -> **75** Orphaned Functions | **0** Duplicates
- `csharp/roslyn/CSharpCompilation.cs` -> **75** Orphaned Functions | **0** Duplicates
- `go/core/syscall_linux.go` -> **66** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`abap/abapGit/zabapgit.prog.abap`** -> AI Confidence: **0.0%**
2. **`abap/abapGit/zcl_abapgit_xml_output.clas.abap`** -> AI Confidence: **0.0%**
3. **`abap/abapGit/zcl_abapgit_http_client.clas.abap`** -> AI Confidence: **0.0%**
4. **`abap/abapGit/zcl_abapgit_persistence_db.clas.abap`** -> AI Confidence: **0.0%**
5. **`abap/abapGit/zcl_abapgit_git_porcelain.clas.abap`** -> AI Confidence: **0.0%**
6. **`abap/abapGit/zcl_abapgit_ajson.clas.abap`** -> AI Confidence: **0.0%**
7. **`abap/abapGit/zcl_abapgit_objects.clas.abap`** -> AI Confidence: **0.0%**
8. **`apex/apex-recipes/AuraEnabledRecipes_Tests.cls`** -> AI Confidence: **0.0%**
9. **`apex/apex-recipes/QueueableRecipes.cls`** -> AI Confidence: **0.0%**
10. **`apex/apex-recipes/SOQLRecipes.cls`** -> AI Confidence: **0.0%**
11. **`apex/apex-recipes/SOQLRecipes_Tests.cls`** -> AI Confidence: **0.0%**
12. **`xml/apex/CanTheUser_Tests.cls`** -> AI Confidence: **0.0%**
13. **`xml/apex/IterationRecipes_Tests.cls`** -> AI Confidence: **0.0%**
14. **`xml/apex/ListSortingRecipes_Tests.cls`** -> AI Confidence: **0.0%**
15. **`batch/cpython/Tools/buildbot/clean.bat`** -> AI Confidence: **0.0%**
16. **`batch/cpython/Tools/msi/build.bat`** -> AI Confidence: **0.0%**
17. **`batch/cpython/Tools/msi/buildrelease.bat`** -> AI Confidence: **0.0%**
18. **`blueprint/ghostty/imgui-widget.blp`** -> AI Confidence: **0.0%**
19. **`blueprint/ghostty/split-tree-split.blp`** -> AI Confidence: **0.0%**
20. **`blueprint/ghostty/command-palette.blp`** -> AI Confidence: **0.0%**
21. **`blueprint/ghostty/split-tree.blp`** -> AI Confidence: **0.0%**
22. **`blueprint/ghostty/window.blp`** -> AI Confidence: **0.0%**
23. **`assembly/cosmopolitan/loader.c`** -> AI Confidence: **0.0%**
24. **`c/doom/d_main.c`** -> AI Confidence: **0.0%**
25. **`c/cpython/compile.c`** -> AI Confidence: **0.0%**
26. **`c/cpython/frameobject.c`** -> AI Confidence: **0.0%**
27. **`c/doom/m_fixed.c`** -> AI Confidence: **0.0%**
28. **`c/doom/m_fixed.h`** -> AI Confidence: **0.0%**
29. **`c/doom/i_system.c`** -> AI Confidence: **0.0%**
30. **`c/doom/doomdef.h`** -> AI Confidence: **0.0%**
31. **`c/doom/p_mobj.h`** -> AI Confidence: **0.0%**
32. **`c/doom/r_defs.h`** -> AI Confidence: **0.0%**
33. **`c/doom/r_bsp.c`** -> AI Confidence: **0.0%**
34. **`c/micropython/compile.h`** -> AI Confidence: **0.0%**
35. **`c/doom/w_wad.c`** -> AI Confidence: **0.0%**
36. **`c/doom/z_zone.c`** -> AI Confidence: **0.0%**
37. **`c/doom/p_mobj.c`** -> AI Confidence: **0.0%**
38. **`c/micropython/gc.h`** -> AI Confidence: **0.0%**
39. **`c/micropython/modmachine.c`** -> AI Confidence: **0.0%**
40. **`c/micropython/modmachine.h`** -> AI Confidence: **0.0%**
41. **`c/micropython/objtype.h`** -> AI Confidence: **0.0%**
42. **`c/cpython/gc.c`** -> AI Confidence: **0.0%**
43. **`c/micropython/gc.c`** -> AI Confidence: **0.0%**
44. **`c/micropython/vfs.c`** -> AI Confidence: **0.0%**
45. **`c/micropython/vfs.h`** -> AI Confidence: **0.0%**
46. **`c/cpython/object.c`** -> AI Confidence: **0.0%**
47. **`c/cpython/ceval.c`** -> AI Confidence: **0.0%**
48. **`c/micropython/vm.c`** -> AI Confidence: **0.0%**
49. **`c/micropython/objtype.c`** -> AI Confidence: **0.0%**
50. **`c/micropython/emitnative.c`** -> AI Confidence: **0.0%**
51. **`c/micropython/compile.c`** -> AI Confidence: **0.0%**
52. **`cobol/gnucobol_internals/numeric.c`** -> AI Confidence: **0.0%**
53. **`c/cpython/dictobject.c`** -> AI Confidence: **0.0%**
54. **`c/sqlite/lemon.c`** -> AI Confidence: **0.0%**
55. **`cpp/godot/object.h`** -> AI Confidence: **0.0%**
56. **`cobol/gnucobol_internals/fileio.c`** -> AI Confidence: **0.0%**
57. **`c/cpython/typeobject.c`** -> AI Confidence: **0.0%**
58. **`lua/redis/function_lua.c`** -> AI Confidence: **0.0%**
59. **`lua/redis/script_lua.h`** -> AI Confidence: **0.0%**
60. **`lua/redis/eval.c`** -> AI Confidence: **0.0%**
61. **`lua/redis/script_lua.c`** -> AI Confidence: **0.0%**
62. **`objective-c/worldwideweb/HText.c`** -> AI Confidence: **0.0%**
63. **`lua/redis/server.h`** -> AI Confidence: **0.0%**
64. **`python/numpy/lapack_litemodule.c`** -> AI Confidence: **0.0%**
65. **`scheme/racket/eval.c`** -> AI Confidence: **0.0%**
66. **`scheme/racket/fun.c`** -> AI Confidence: **0.0%**
67. **`cobol/che-che4z-lsp-for-cobol/SQLCA_DB2.cpy`** -> AI Confidence: **0.0%**
68. **`cobol/che-che4z-lsp-for-cobol/SQLCA_DATACOM.cpy`** -> AI Confidence: **0.0%**
69. **`cobol/che-che4z-lsp-for-cobol/SQLDA.cpy`** -> AI Confidence: **0.0%**
70. **`cobol/cics-banking-sample-application-cbsa/ACCOUNT.cpy`** -> AI Confidence: **0.0%**
71. **`cobol/cics-genapp/lgacdb01.cbl`** -> AI Confidence: **0.0%**
72. **`cobol/cics-genapp/lgacdb02.cbl`** -> AI Confidence: **0.0%**
73. **`cobol/cics-genapp/lgacus01.cbl`** -> AI Confidence: **0.0%**
74. **`cobol/cics-genapp/lgacvs01.cbl`** -> AI Confidence: **0.0%**
75. **`cobol/cics-genapp/lgapvs01.cbl`** -> AI Confidence: **0.0%**
76. **`cobol/cics-genapp/lgapol01.cbl`** -> AI Confidence: **0.0%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `abap/abapGit/zcl_abapgit_git_porcelain.clas.abap` -> **100.0%** Exposure
- `apex/apex-recipes/SOQLRecipes.cls` -> **100.0%** Exposure
- `apex/apex-recipes/SOQLRecipes_Tests.cls` -> **100.0%** Exposure
- `cobol/gnucobol_internals/scanner.l` -> **100.0%** Exposure
- `fortran/wrf/configure_reader.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `python/fastapi/tests/test_default_response_class.py` -> **100.0%** Exposure
- `python/fastapi/tests/test_default_response_class_router.py` -> **100.0%** Exposure
- `python/fastapi/tests/test_dependency_yield_scope_websockets.py` -> **100.0%** Exposure
- `python/fastapi/fastapi/routing.py` -> **100.0%** Exposure
- `python/fastapi/tests/test_response_model_as_return_annotation.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `c/cpython/compile.c` -> **10.0%** Exposure
- `c/cpython/gc.c` -> **10.0%** Exposure
- `c/micropython/vfs.c` -> **10.0%** Exposure
- `c/micropython/emitnative.c` -> **10.0%** Exposure
- `c/micropython/compile.c` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `cobol/cics-genapp/lgacdb01.cbl` -> **94.5213%** Exposure
- `python/twisted/transport.py` -> **10.4094%** Exposure
### Algorithmic DoS Exposure
- `assembly/bootos/os.asm` -> **100.0%** Exposure
- `assembly/cosmopolitan/loader.c` -> **100.0%** Exposure
- `c/doom/d_main.c` -> **100.0%** Exposure
- `c/cpython/compile.c` -> **100.0%** Exposure
- `c/cpython/frameobject.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7273` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `typescript/playwright/frames.ts` (TYPESCRIPT) -> Cumulative Risk: **944.16**
- **Archetype:** `file_cluster_4` (Distance: 13.138 IQR)
- **Magnitude:** 424.01 | **LOC:** 1823 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `action` (Impact: 186.8), `waitForSelector` (Impact: 174.7), `expect` (Impact: 171.1)

### 2. `fortran/wrf/gen_be_wrapper.ksh` (SHELL) -> Cumulative Risk: **830.43**
- **Archetype:** `file_cluster_0` (Distance: 14.229 IQR)
- **Magnitude:** 136.52 | **LOC:** 95 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Cognitive Load (96.5296%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 63.9), `__global_context__` (Impact: 18.9)

### 3. `typescript/playwright/bidiConnection.ts` (TYPESCRIPT) -> Cumulative Risk: **828.89**
- **Archetype:** `file_cluster_4` (Distance: 13.85 IQR)
- **Magnitude:** 40.6 | **LOC:** 261 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_dispatchMessage` (Impact: 83.7), `dispatchMessage` (Impact: 32.3), `send` (Impact: 11.0)

### 4. `groovy/gradle/DefaultPluginManager.java` (JAVA) -> Cumulative Risk: **823.81**
- **Archetype:** `file_cluster_13` (Distance: 10.563 IQR)
- **Magnitude:** 623.88 | **LOC:** 369 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `doApply` (Impact: 104.1), `pluginsForId` (Impact: 81.2), `addPluginInternal` (Impact: 61.0)

### 5. `typescript/playwright/dispatcher.ts` (TYPESCRIPT) -> Cumulative Risk: **819.8**
- **Archetype:** `file_cluster_4` (Distance: 13.619 IQR)
- **Magnitude:** 75.02 | **LOC:** 415 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `dispatch` (Impact: 122.5), `_disposeRecursively` (Impact: 43.1), `_tChannelImplFromWire` (Impact: 27.4)

### 6. `csharp/roslyn/MethodCompiler.cs` (CSHARP) -> Cumulative Risk: **810.2**
- **Archetype:** `file_cluster_8` (Distance: 11.298 IQR)
- **Magnitude:** 7350.54 | **LOC:** 2528 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9886%)
- **Heaviest Functions:** `BindMethodBody` (Impact: 2993.7), `CompileMethod` (Impact: 916.0), `GenerateMethodBody` (Impact: 571.2)

### 7. `csharp/roslyn/CSharpCompilation.cs` (CSHARP) -> Cumulative Risk: **804.87**
- **Archetype:** `file_cluster_8` (Distance: 11.94 IQR)
- **Magnitude:** 8963.6 | **LOC:** 5286 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.7745%)
- **Heaviest Functions:** `CommonCreateBuiltinOperator` (Impact: 433.9), `FindEntryPoint` (Impact: 425.1), `GetDiagnosticsForMethodBodiesInTree` (Impact: 373.1)

### 8. `perl/exiftool/RandomAccess.pm` (PERL) -> Cumulative Risk: **804.76**
- **Archetype:** `file_cluster_0` (Distance: 15.542 IQR)
- **Magnitude:** 2057.32 | **LOC:** 448 | **CtrlFlow:** 63.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Close` (Impact: 135.9), `Seek` (Impact: 28.6), `SeekTest` (Impact: 21.4)

### 9. `perl/spamassassin/Message.pm` (PERL) -> Cumulative Risk: **799.53**
- **Archetype:** `file_cluster_0` (Distance: 15.935 IQR)
- **Magnitude:** 7354.82 | **LOC:** 1504 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `new` (Impact: 4586.9), `_parse_normal` (Impact: 481.2), `split_into_array_of_short_paragraphs` (Impact: 17.6)

### 10. `python/fastapi/fastapi/routing.py` (PYTHON) -> Cumulative Risk: **797.4**
- **Archetype:** `file_cluster_16` (Distance: 10.135 IQR)
- **Magnitude:** 849.16 | **LOC:** 4957 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Concurrency (99.9997%)
- **Heaviest Functions:** `_keepalive_inserter` (Impact: 42.7), `app` (Impact: 36.6), `matches` (Impact: 34.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `livecode/core/revsaveasstandalone.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.872 IQR)
- **Top Global Matches:** file_cluster_17: 10.872, file_cluster_2: 11.62, file_cluster_4: 11.622
- **Magnitude:** 170906.31 | **LOC:** 2675 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (86.9542%), Tech Debt (57.3145%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1374`, `structural_boundaries: 654`, `args: 150`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 19`, `state_mutation: 707`, `dead_code: 29`, `fragile_debt: 42`
* *Architecture:* `io: 7`, `api: 14`, `concurrency: 27`, `import: 9`
* *Defense:* `safety: 75`, `sync_locks: 20`, `immutability_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scheme/racket/io.ss` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.288 IQR)
- **Top Global Matches:** file_cluster_8: 7.288, file_cluster_7: 8.026, file_cluster_1: 8.171
- **Magnitude:** 113501.14 | **LOC:** 6399 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.4802%), Tech Debt (8.0299%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1296`, `structural_boundaries: 571`, `args: 71`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 287`, `planned_debt: 5`
* *Architecture:* `io: 88`
* *Defense:* `safety: 17`, `doc: 86`, `sync_locks: 1`, `immutability_locks: 37`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022128
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `scheme/racket/cpnanopass.ss` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.503 IQR)
- **Top Global Matches:** file_cluster_8: 8.503, file_cluster_17: 9.047, file_cluster_7: 9.199
- **Magnitude:** 108569.23 | **LOC:** 10910 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.3314%), Tech Debt (8.8006%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1484`, `structural_boundaries: 976`, `args: 46`, `func_start: 40`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 1218`, `dead_code: 5`, `planned_debt: 23`, `fragile_debt: 3`
* *Architecture:* `io: 59`, `import: 11`
* *Defense:* `safety: 76`, `doc: 15`, `immutability_locks: 311`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fortran/wrf/module_sf_noahdrv.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.45 IQR)
- **Top Global Matches:** file_cluster_17: 14.45, file_cluster_8: 14.676, file_cluster_13: 14.729
- **Magnitude:** 84793.62 | **LOC:** 5355 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 845
- **Risk Profile:** Cognitive Load (66.8127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lsm_mosaic` (Impact: 52282.5 | O(2^N) | DB: 845)
  * `lsm` (Impact: 25993.0 | O(2^N) | DB: 454)
  * `LSMINIT` (Impact: 2532.4 | O(2^N) | DB: 53)
    * *Intent:* #if defined(wrfmodel)
  * `lsm_mosaic_init` (Impact: 521.5 | O(N^6) | DB: 23)
  * `SOIL_VEG_GEN_PARM` (Impact: 60.7 | O(N^5) | DB: 55)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 746`, `args: 404`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3303`, `dead_code: 42`
* *Architecture:* `io: 105`, `api: 5`, `import: 47`
* *Defense:* `safety: 48`, `doc: 1`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001079
  * `Imports (Out-Degree: 0):` module_sf_urban, mpas_atmphys_utilities, module_sf_noahlsm, module_wrf_error, module_sf_noahlsm_glacial_only, module_sf_bep, module_sf_bep_bem, mpas_atmphys_date_time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `fortran/wrf/module_initialize_real.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.227 IQR)
- **Top Global Matches:** file_cluster_8: 15.227, file_cluster_13: 15.255, file_cluster_17: 15.304
- **Magnitude:** 54736.72 | **LOC:** 9207 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1499
- **Risk Profile:** Cognitive Load (98.1298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_domain_rk` (Impact: 23553.3 | O(N^6) | DB: 1499)
  * `vert_interp` (Impact: 7994.9 | O(N^6) | DB: 278)
  * `rh_to_mxrat1` (Impact: 2309.8 | O(2^N) | DB: 56)
  * `rh_to_mxrat2` (Impact: 1963.7 | O(2^N) | DB: 65)
  * `fillitup` (Impact: 1654.8 | O(2^N) | DB: 37)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3344`, `structural_boundaries: 658`, `args: 226`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 9`, `state_mutation: 7280`, `dead_code: 49`
* *Architecture:* `io: 26`, `api: 38`, `concurrency: 1`, `import: 85`
* *Defense:* `safety: 176`, `sync_locks: 1`, `immutability_locks: 80`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` module_domain, module_date_time, module_dm, module_model_constants, module_bc, module_timing, module_polarfft, module_configure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fortran/wrf/module_physics_init.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.714 IQR)
- **Top Global Matches:** file_cluster_13: 13.714, file_cluster_8: 13.764, file_cluster_17: 13.962
- **Magnitude:** 40612.14 | **LOC:** 5751 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 247
- **Risk Profile:** Cognitive Load (67.0045%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bl_init` (Impact: 11718.2 | O(2^N) | DB: 71)
  * `phy_init` (Impact: 10439.6 | O(2^N) | DB: 247)
  * `ra_init` (Impact: 4430.8 | O(2^N) | DB: 48)
  * `landuse_init` (Impact: 3301.4 | O(2^N) | DB: 169)
  * `mp_init` (Impact: 2412.3 | O(2^N) | DB: 154)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 897`, `structural_boundaries: 1111`, `args: 708`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 2121`, `dead_code: 31`
* *Architecture:* `io: 44`, `api: 19`, `import: 158`
* *Defense:* `safety: 78`, `doc: 3`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` module_sf_pxsfclay, module_model_constants, module_cu_g3, module_wrf_error, module_bl_boulac, module_bl_shinhong, module_wind_mav, module_ra_sw...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `perl/exiftool/ExifTool.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.135 IQR)
- **Top Global Matches:** file_cluster_0: 16.135, file_cluster_17: 16.269, file_cluster_13: 16.289
- **Magnitude:** 35447.46 | **LOC:** 10227 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1745
- **Risk Profile:** Cognitive Load (98.4775%), Tech Debt (9.3693%)
**Top Internal Functions/Classes:**
  * `DoAutoLoad` (Impact: 8710.7 | O(2^N) | DB: 1745)
    * *Intent:* #------------------------------------------------------------------------------ # Utility to load ou...
  * `Options` (Impact: 3547.4 | O(2^N) | DB: 171)
    * *Intent:* #------------------------------------------------------------------------------ # Get/set ExifTool o...
  * `IsSameID` (Impact: 1069.1 | O(2^N) | DB: 217)
    * *Intent:* #------------------------------------------------------------------------------ # Does group name ma...
  * `ProcessJPEG` (Impact: 344.4 | O(N^5) | DB: 40)
    * *Intent:* #------------------------------------------------------------------------------ # Extract metadata f...
  * `DoProcessTIFF` (Impact: 89.1 | O(N^4) | DB: 12)
    * *Intent:* #------------------------------------------------------------------------------ # Process TIFF data ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5397`, `structural_boundaries: 1833`, `args: 397`, `func_start: 237`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 11`, `state_mutation: 20935`, `dead_code: 13`, `fragile_debt: 8`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 5`, `concurrency: 17`, `import: 158`
* *Defense:* `safety: 20`, `test: 1`, `cleanup: 276`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Time::Piece, Image::ExifTool::Validate, Win32API::File, Require, SystemTimeRes, character, recognized, Cwd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python/cython/Nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.525 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.962 IQR)
- **Top Global Matches:** file_cluster_8: 11.525, file_cluster_13: 11.696, file_cluster_0: 11.838
- **Magnitude:** 29212.8 | **LOC:** 10867 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (59.4878%), Tech Debt (10.8836%)
**Top Internal Functions/Classes:**
  * `generate_execution_code` (Impact: 2191.2 | O(2^N) | DB: 16)
  * `generate_execution_code` (Impact: 1848.8 | O(2^N) | DB: 49)
  * `__deepcopy__` (Impact: 1639.5 | O(N^6) | DB: 24)
    * *Intent:* # Any references to objects further up the tree should not be deep-copied. # However, if they're in ...
  * `align_argument_type` (Impact: 1633.6 | O(N^6) | DB: 2)
  * `declare_generator_body` (Impact: 1500.4 | O(2^N) | DB: 23)
    * *Intent:* # Main code body of a generator implemented as a DefNode. # is_generator_body = True is_inlined = Fa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3131`, `structural_boundaries: 2012`, `args: 486`, `func_start: 478`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 2`, `state_mutation: 1182`, `dead_code: 63`, `planned_debt: 16`, `fragile_debt: 18`
* *Architecture:* `io: 1`, `api: 562`, `concurrency: 15`, `import: 79`
* *Defense:* `safety: 170`, `doc: 92`, `test: 26`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .PyrexTypes, .StringEncoding, of, itertools, copy, enum, the, ..Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `csharp/roslyn/LanguageParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.71 IQR)
- **Top Global Matches:** file_cluster_8: 11.71, file_cluster_17: 12.035, file_cluster_7: 12.135
- **Magnitude:** 23132.82 | **LOC:** 14680 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (30.0687%), Tech Debt (9.5119%)
**Top Internal Functions/Classes:**
  * `ParseMemberDeclarationOrStatementCore` (Impact: 968.4 | O(N^6) | DB: 44)
    * *Intent:* /// <summary> /// Changes in this function around member parsing should be mirrored in <see cref="Pa...
  * `ParseVariableDeclarator` (Impact: 896.8 | O(N^6) | DB: 6)
  * `ParseNamespaceBodyWorker` (Impact: 773.4 | O(N^6) | DB: 71)
  * `TryEatNullableQualifierIfApplicable` (Impact: 674.8 | O(N^6) | DB: 1)
  * `ScanPossibleTypeArgumentList` (Impact: 506.4 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4122`, `structural_boundaries: 2202`, `args: 786`, `func_start: 1655`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 10`, `state_mutation: 1525`, `dead_code: 54`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 17`
* *Architecture:* `api: 58`, `concurrency: 131`, `import: 11`
* *Defense:* `safety: 932`, `doc: 187`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, Microsoft.CodeAnalysis.Syntax.InternalSyntax, System.Diagnostics.CodeAnalysis, Roslyn.Utilities, System.Threading, System.Diagnostics, Microsoft.CodeAnalysis.Text, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zig/zls/analysis.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.664 IQR)
- **Top Global Matches:** file_cluster_8: 13.664, file_cluster_0: 13.966, file_cluster_7: 13.972
- **Magnitude:** 18268.36 | **LOC:** 7016 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (63.413%), Tech Debt (8.8116%)
**Top Internal Functions/Classes:**
  * `resolveTypeOfNodeUncached` (Impact: 3928.3 | O(N^6) | DB: 46)
  * `getFieldAccessType` (Impact: 2291.2 | O(2^N) | DB: 13)
  * `resolveExpressionTypeFromAncestors` (Impact: 1813.0 | O(N^6) | DB: 9)
  * `resolveType` (Impact: 1255.9 | O(2^N) | DB: 1)
  * `eql` (Impact: 926.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3279`, `structural_boundaries: 1181`, `args: 201`, `func_start: 197`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 581`, `dead_code: 9`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 193`, `concurrency: 2`
* *Defense:* `safety: 1443`, `doc: 111`, `test: 1`, `immutability_locks: 913`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.167
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002157
  * `Imports (Out-Degree: 2):` DocumentStore.zig, references.zig, version_data, tracy, std, builtin, Uri.zig, InternPool.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scheme/racket/fun.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.108 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.894 IQR)
- **Top Global Matches:** file_cluster_8: 13.108, file_cluster_7: 13.43, file_cluster_13: 13.456
- **Magnitude:** 17171.5 | **LOC:** 10416 | **CtrlFlow:** 76.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 137
- **Risk Profile:** Cognitive Load (93.6092%), Tech Debt (15.8931%)
**Top Internal Functions/Classes:**
  * `call_with_prompt` (Impact: 585.8 | O(N^6) | DB: 78)
  * `internal_call_cc` (Impact: 530.9 | O(N^6) | DB: 71)
  * `do_chaperone_procedure` (Impact: 381.6 | O(N^6) | DB: 26)
  * `chaperone_do_control` (Impact: 338.3 | O(N^6) | DB: 28)
  * `restore_continuation` (Impact: 336.4 | O(N^6) | DB: 137)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2416`, `structural_boundaries: 738`, `args: 229`, `func_start: 263`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 262`, `high_risk_execution: 2`, `state_mutation: 6879`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 3`, `orphaned_logic: 44`
* *Architecture:* `io: 14`, `api: 1767`, `import: 10`
* *Defense:* `safety: 1`, `test: 7`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mzmark_fun.inc, schpriv.h, schmach.h, mzstkchk.h, schmap.inc, schrktio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zig/zig/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.498 IQR)
- **Top Global Matches:** file_cluster_8: 12.498, file_cluster_7: 12.93, file_cluster_17: 12.996
- **Magnitude:** 16825.94 | **LOC:** 7530 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (58.6156%), Tech Debt (8.4568%)
**Top Internal Functions/Classes:**
  * `buildOutputType` (Impact: 5015.8 | O(N^6) | DB: 125)
  * `createModule` (Impact: 2200.6 | O(2^N) | DB: 6)
  * `cmdBuild` (Impact: 1862.7 | O(N^6) | DB: 39)
  * `cmdFetch` (Impact: 777.2 | O(N^6) | DB: 20)
    * *Intent:* ;
  * `runOrTest` (Impact: 647.8 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2696`, `structural_boundaries: 571`, `args: 69`, `func_start: 66`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 96`, `high_risk_execution: 2`, `state_mutation: 765`, `dead_code: 6`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 32`, `concurrency: 20`
* *Defense:* `safety: 953`, `doc: 32`, `test: 12`, `sync_locks: 2`, `immutability_locks: 685`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007139
  * `Imports (Out-Degree: 2):` dev.zig, bindings.zig, llvm.zig, IncrementalDebugServer.zig, mingw.zig, Zcu.zig, build_options, DarwinPosixSpawn.zig...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `perl/exiftool/exiftool` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.129 IQR)
- **Top Global Matches:** file_cluster_17: 15.129, file_cluster_0: 15.181, file_cluster_13: 15.272
- **Magnitude:** 16493.72 | **LOC:** 8151 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 841
- **Risk Profile:** Cognitive Load (79.1592%), Tech Debt (8.8001%)
**Top Internal Functions/Classes:**
  * `ScanDir` (Impact: 3834.7 | O(2^N) | DB: 841)
    * *Intent:* #------------------------------------------------------------------------------ # Scan directory for...
  * `EscapeJSON` (Impact: 706.4 | O(2^N) | DB: 104)
    * *Intent:* #------------------------------------------------------------------------------ # Escape string for ...
  * `FormatXML` (Impact: 272.3 | O(2^N) | DB: 12)
    * *Intent:* #------------------------------------------------------------------------------ # Format value for X...
  * `ReadStayOpen` (Impact: 215.3 | O(N^6) | DB: 32)
    * *Intent:* #------------------------------------------------------------------------------ # Read arguments fro...
  * `AddGroups` (Impact: 87.5 | O(2^N) | DB: 2)
    * *Intent:* #------------------------------------------------------------------------------ # Add tag groups fro...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4334`, `structural_boundaries: 1081`, `args: 202`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 28`, `state_mutation: 10760`, `dead_code: 21`, `fragile_debt: 7`
* *Architecture:* `io: 344`, `api: 1`, `concurrency: 2`, `import: 156`
* *Defense:* `safety: 12`, `doc: 236`, `cleanup: 247`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Time::Piece, sense, Win32API::File, Cwd, our, Term::ReadKey, real, destination...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scheme/racket/thread.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.401 IQR)
- **Top Global Matches:** file_cluster_8: 6.401, file_cluster_7: 7.531, file_cluster_1: 7.611
- **Magnitude:** 16161.1 | **LOC:** 1323 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.2169%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 28`, `args: 57`, `func_start: 52`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `concurrency: 2`, `import: 1`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `c/sqlite/lemon.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.291 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.393 IQR)
- **Top Global Matches:** file_cluster_8: 14.291, file_cluster_13: 14.516, file_cluster_7: 14.578
- **Magnitude:** 14277.16 | **LOC:** 6076 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 350
- **Risk Profile:** Cognitive Load (91.9345%), Tech Debt (7.7089%)
**Top Internal Functions/Classes:**
  * `parseonetoken` (Impact: 1479.0 | O(N^5) | DB: 249)
    * *Intent:* /* Parse a single token */
  * `ReportTable` (Impact: 1220.2 | O(N^4) | DB: 350)
    * *Intent:* /* Generate C source code for the parser */
  * `Parse` (Impact: 663.7 | O(2^N) | DB: 108)
    * *Intent:* /* In spite of its name, this function is really a scanner. It read ** in the entire input file (all...
  * `eval_preprocessor_boolean` (Impact: 365.0 | O(2^N) | DB: 38)
    * *Intent:* /* The text in the input is part of the argument to an %ifdef or %ifndef. ** Evaluate the text as a ...
  * `translate_code` (Impact: 325.7 | O(N^4) | DB: 66)
    * *Intent:* /* ** Write and transform the rp->code string so that symbols are expanded. ** Populate the rp->code...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1838`, `structural_boundaries: 761`, `args: 200`, `func_start: 130`, `class_start: 253`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 5911`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 27`, `api: 938`, `import: 7`
* *Defense:* `safety: 37`, `doc: 23`, `test: 32`, `immutability_locks: 108`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, assert.h, stdarg.h, unistd.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `perl/bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.7 IQR)
- **Top Global Matches:** file_cluster_8: 13.7, file_cluster_17: 13.72, file_cluster_13: 13.724
- **Magnitude:** 14156.38 | **LOC:** 5124 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 273
- **Risk Profile:** Cognitive Load (77.4793%), Tech Debt (99.4317%)
**Top Internal Functions/Classes:**
  * `match` (Impact: 4022.1 | O(2^N) | DB: 217)
  * `modify_keywords` (Impact: 3762.6 | O(N^6) | DB: 273)
  * `_check_groups` (Impact: 3184.1 | O(N^6) | DB: 193)
  * `_check_bug_status` (Impact: 621.7 | O(N^3) | DB: 57)
  * `ValidateDependencies` (Impact: 48.2 | O(N^2) | DB: 21)
    * *Intent:* # # Field Validation # # Validate and return a hash of dependencies
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1625`, `structural_boundaries: 1402`, `args: 151`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 2295`, `dead_code: 6`, `fragile_debt: 215`
* *Architecture:* `io: 4`, `api: 1`, `import: 75`
* *Defense:* `safety: 10`, `doc: 140`, `cleanup: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bugs, Bugzilla::Comment, Bugzilla::FlagType, privileges, longer, QA, set_all, Bugzilla::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zig/zig/Type.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.367 IQR)
- **Top Global Matches:** file_cluster_8: 11.367, file_cluster_7: 11.657, file_cluster_16: 11.725
- **Magnitude:** 12778.3 | **LOC:** 4357 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (14.4992%), Tech Debt (8.7722%)
**Top Internal Functions/Classes:**
  * `print` (Impact: 2032.7 | O(2^N))
    * *Intent:* /// Prints a name suitable for `@typeName`. /// TODO: take an `opt_sema` to pass to `fmtValue` when ...
  * `abiSizeInner` (Impact: 1553.5 | O(2^N) | DB: 1)
    * *Intent:* /// If you pass `eager` you will get back `scalar` and assert the type is resolved. /// In this case...
  * `abiAlignmentInner` (Impact: 1438.8 | O(2^N) | DB: 1)
    * *Intent:* /// If you pass `eager` you will get back `scalar` and assert the type is resolved. /// In this case...
  * `onePossibleValue` (Impact: 1077.5 | O(2^N) | DB: 5)
    * *Intent:* /// During semantic analysis, instead call `Sema.typeHasOnePossibleValue` which /// resolves field t...
  * `hasRuntimeBitsInner` (Impact: 1058.6 | O(2^N))
    * *Intent:* /// true if and only if the type takes up space in memory at runtime. /// There are two reasons a ty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1438`, `structural_boundaries: 717`, `args: 194`, `func_start: 189`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 143`, `state_mutation: 83`, `dead_code: 1`, `planned_debt: 10`
* *Architecture:* `api: 379`
* *Defense:* `safety: 429`, `doc: 187`, `immutability_locks: 516`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.911
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006068
  * `Imports (Out-Degree: 2):` std, Value.zig, builtin, InternPool.zig, Zcu.zig, Sema.zig, target.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `zig/zig/Compilation.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.209 IQR)
- **Top Global Matches:** file_cluster_8: 12.209, file_cluster_7: 12.461, file_cluster_1: 12.671
- **Magnitude:** 12628.14 | **LOC:** 8171 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (23.4019%), Tech Debt (10.6851%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 1327.4 | O(2^N) | DB: 4)
    * *Intent:* /// Detect changes to source files, perform semantic analysis, and update the output files.
  * `addCommonCCArgs` (Impact: 989.2 | O(N^6) | DB: 1)
    * *Intent:* /// Add common C compiler args between translate-c and C object compilation.
  * `updateCObject` (Impact: 897.5 | O(N^6) | DB: 7)
  * `addCCArgs` (Impact: 768.1 | O(N^6) | DB: 2)
    * *Intent:* /// Add common C compiler args and Clang specific args.
  * `performAllTheWork` (Impact: 687.9 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2285`, `structural_boundaries: 664`, `args: 182`, `func_start: 182`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 408`, `dead_code: 4`, `planned_debt: 35`, `fragile_debt: 6`
* *Architecture:* `io: 1`, `api: 173`, `concurrency: 6`
* *Defense:* `safety: 1138`, `doc: 385`, `test: 15`, `sync_locks: 77`, `immutability_locks: 817`, `cleanup: 163`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006742
  * `Imports (Out-Degree: 4):` glibc.zig, dev.zig, Air.zig, llvm.zig, Value.zig, Builtin.zig, musl.zig, c.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `c/cpython/typeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.822 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.623 IQR)
- **Top Global Matches:** file_cluster_8: 12.822, file_cluster_13: 13.101, file_cluster_7: 13.162
- **Magnitude:** 12395.04 | **LOC:** 12874 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (75.2584%), Tech Debt (16.175%)
**Top Internal Functions/Classes:**
  * `PyType_FromMetaclass` (Impact: 448.4 | O(N^6) | DB: 90)
  * `subtype_dealloc` (Impact: 281.4 | O(2^N) | DB: 24)
  * `type_modified_unlocked` (Impact: 115.8 | O(2^N) | DB: 8)
  * `type_call` (Impact: 115.2 | O(2^N) | DB: 9)
  * `object_getstate_default` (Impact: 114.7 | O(N^6) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2369`, `structural_boundaries: 1293`, `args: 31`, `func_start: 386`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 197`, `state_mutation: 4803`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 15`, `orphaned_logic: 40`
* *Architecture:* `io: 8`, `api: 2182`, `import: 30`
* *Defense:* `safety: 280`, `doc: 1`, `test: 276`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pycore_lock.h, pycore_function.h, pycore_interpframe.h, pycore_weakref.h, pycore_tuple.h, pycore_pystate.h, pycore_abstract.h, pycore_memoryobject.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scheme/racket/schemify.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.621 IQR)
- **Top Global Matches:** file_cluster_8: 5.621, file_cluster_7: 6.819, file_cluster_1: 6.932
- **Magnitude:** 12297.89 | **LOC:** 1127 | **CtrlFlow:** 85.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.3367%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 35`, `args: 31`, `func_start: 30`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python/numpy/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.029 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.242 IQR)
- **Top Global Matches:** file_cluster_8: 11.029, file_cluster_7: 11.23, file_cluster_13: 11.389
- **Magnitude:** 12169.82 | **LOC:** 8995 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (25.6433%), Tech Debt (9.7379%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 1731.7 | O(2^N) | DB: 6)
  * `round` (Impact: 1452.4 | O(2^N) | DB: 4)
  * `resize` (Impact: 1345.1 | O(2^N) | DB: 1)
  * `__new__` (Impact: 1249.2 | O(N^6) | DB: 11)
  * `fill_value` (Impact: 1069.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 836`, `args: 269`, `func_start: 268`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 206`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 185`, `import: 19`
* *Defense:* `safety: 181`, `doc: 410`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy._core.numeric, numpy._utils, problems, re, copy, time., numpy._core.umath, numpy._core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `livecode/core/foundation-string.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_8: 13.494, file_cluster_7: 13.611, file_cluster_1: 13.782
- **Magnitude:** 11961.54 | **LOC:** 7360 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (35.5427%), Tech Debt (73.9145%)
**Top Internal Functions/Classes:**
  * `MCStringFormatV` (Impact: 838.2 | O(N^6) | DB: 110)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringConvertToBytes` (Impact: 296.4 | O(N^6) | DB: 26)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `MCStringDelimitedOffset` (Impact: 237.1 | O(N^6) | DB: 24)
  * `MCStringReplaceChars` (Impact: 205.0 | O(2^N) | DB: 8)
  * `MCStringSplit` (Impact: 202.3 | O(N^4) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1296`, `structural_boundaries: 663`, `args: 303`, `func_start: 222`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 8`, `state_mutation: 3753`, `dead_code: 7`, `planned_debt: 5`, `fragile_debt: 34`, `orphaned_logic: 87`
* *Architecture:* `import: 12`
* *Defense:* `safety: 1`, `doc: 883`, `immutability_locks: 118`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foundation-auto.h, errno.h, foundation-unicode.h, foundation.h, foundation-chunk.h, langinfo.h, foundation-private.h, foundation-string-native.cpp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `powershell/core/packaging.psm1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.558 IQR)
- **Top Global Matches:** file_cluster_0: 12.558, file_cluster_8: 12.725, file_cluster_15: 12.897
- **Magnitude:** 11513.58 | **LOC:** 5824 | **CtrlFlow:** 80.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 212
- **Risk Profile:** Cognitive Load (84.1172%), Tech Debt (18.2072%)
**Top Internal Functions/Classes:**
  * `Start-PSPackage` (Impact: 4424.6 | O(2^N) | DB: 99)
  * `New-MSIXPackage` (Impact: 1779.2 | O(N^5) | DB: 187)
    * *Intent:* #>
  * `New-UnixPackage` (Impact: 1481.3 | O(N^6) | DB: 212)
  * `Test-Bom` (Impact: 254.3 | O(N^5) | DB: 48)
    * *Intent:* # Verify a folder based on a BOM json. # Use -Fix to update the BOM, Please review the file types.
  * `Get-PEInfo` (Impact: 213.6 | O(2^N) | DB: 12)
    * *Intent:* # Get the PE information for a file
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1006`, `structural_boundaries: 239`, `args: 68`, `func_start: 104`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 1`, `state_mutation: 1867`, `dead_code: 16`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 29`
* *Architecture:* `io: 27`, `api: 457`, `import: 5`
* *Defense:* `safety: 61`, `doc: 68`, `test: 10`, `immutability_locks: 5`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $PSScriptRoot\..\Xml, $PSScriptRoot\..\buildCommon\startNativeExecution.ps1, .\build.psm1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `perl/spamassassin/PerMsgStatus.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.918 IQR)
- **Top Global Matches:** file_cluster_0: 13.918, file_cluster_17: 14.042, file_cluster_13: 14.115
- **Magnitude:** 11342.64 | **LOC:** 3742 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (72.4533%), Tech Debt (62.7238%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 4323.3 | O(2^N) | DB: 75)
    * *Intent:* # optimized for speed # $_[0] is self # $_[1] is request # $_[2] is defval
  * `check_timed` (Impact: 1745.3 | O(N^6) | DB: 62)
  * `_process_header` (Impact: 873.9 | O(N^6) | DB: 54)
  * `all_to_addrs` (Impact: 528.4 | O(2^N) | DB: 8)
  * `add_uri_detail_list` (Impact: 446.0 | O(2^N) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1689`, `structural_boundaries: 677`, `args: 121`, `func_start: 80`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 1934`, `dead_code: 19`, `planned_debt: 8`, `fragile_debt: 33`, `orphaned_logic: 6`
* *Architecture:* `io: 13`, `api: 1`, `concurrency: 2`, `import: 60`
* *Defense:* `safety: 8`, `doc: 132`, `cleanup: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.874
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Encode, domains, Mail::SpamAssassin::AsyncLoop, trailing, of, re, Mail::SpamAssassin::Constants, meta...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fortran/wrf/module_domain.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.978 IQR)
- **Top Global Matches:** file_cluster_13: 13.978, file_cluster_8: 14.093, file_cluster_17: 14.112
- **Magnitude:** 11010.58 | **LOC:** 2988 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 232
- **Risk Profile:** Cognitive Load (59.4757%), Tech Debt (9.7188%)
**Top Internal Functions/Classes:**
  * `ensure_space_field` (Impact: 1620.7 | O(2^N) | DB: 4)
  * `wrf_patch_domain` (Impact: 1134.1 | O(N^6) | DB: 91)
  * `domain_clock_get` (Impact: 779.9 | O(2^N) | DB: 47)
  * `alloc_and_configure_domain` (Impact: 640.7 | O(2^N) | DB: 232)
  * `alloc_space_field` (Impact: 494.9 | O(2^N) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 385`, `args: 264`, `func_start: 53`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2445`, `dead_code: 15`, `fragile_debt: 4`
* *Architecture:* `io: 6`, `api: 52`, `import: 39`
* *Defense:* `safety: 158`, `doc: 46`, `immutability_locks: 4`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.864
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003236
  * `Imports (Out-Degree: 1):` module_domain, module_domain_type, module_configure, module_machine, module_wrf_error, module_utility, module_driver_constants
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `python/fastapi/tests/test_empty_router.py` (PYTHON) | Magnitude: 22.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 11, test: 8, branch: 4
- `cpp/NVDA/ensureuv.ps1` (POWERSHELL) | Magnitude: 98.82 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 89, branch: 31, state_mutation: 31, closures: 21
- `perl/exiftool/RandomAccess.pm` (PERL) | Magnitude: 2057.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1818, indent_spaces: 297, branch: 148, pointers: 121
- `rust/bevy/bevy_ecs_macros.rs` (RUST) | Magnitude: 645.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 494, structural_boundaries: 217, doc: 132, state_mutation: 78
- `python/fastapi/tests/test_required_noneable.py` (PYTHON) | Magnitude: 35.34 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 20, test: 17, api: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `solidity/openzeppelin/AccessControl.sol` (SOLIDITY) | Magnitude: 127.38 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, structural_boundaries: 43, branch: 32, doc: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `livecode/core/config.sh` (SHELL) | Magnitude: 3.68 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: safety: 2, reflection_metaprogramming: 2, structural_boundaries: 1, args: 1
- `fortran/wrf/run_convert_e2c.ksh` (SHELL) | Magnitude: 37.44 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 36, reflection_metaprogramming: 31, api: 23, indent_spaces: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `python/fastapi/tests/utils.py` (PYTHON) | Magnitude: 7.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: test: 5, indent_spaces: 4, structural_boundaries: 3, io: 3
- `python/fastapi/tests/test_response_model_invalid.py` (PYTHON) | Magnitude: 42.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 19, api: 13, test: 9
- `python/fastapi/tests/test_swagger_ui_init_oauth.py` (PYTHON) | Magnitude: 11.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, test: 7, safety: 5
- `rust/syn/data.rs` (RUST) | Magnitude: 449.3 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 342, structural_boundaries: 121, doc: 64, branch: 63
- `python/fastapi/tests/test_pydantic_v1_error.py` (PYTHON) | Magnitude: 70.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 36, api: 24, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `python/fastapi/tests/test_router_events.py` (PYTHON) | Magnitude: 148.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 174, test: 109, safety: 97
- `php/laravel_core/Collection.php` (PHP) | Magnitude: 586.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 578, doc: 388, structural_boundaries: 174, state_mutation: 125
- `python/fastapi/fastapi/exceptions.py` (PYTHON) | Magnitude: 93.82 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 41, doc: 22, encapsulation: 19
- `rust/bevy/bevy_ecs_table.rs` (RUST) | Magnitude: 166.68 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 379, doc: 146, args: 36, structural_boundaries: 33
- `python/fastapi/fastapi/routing.py` (PYTHON) | Magnitude: 849.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2515, doc: 474, structural_boundaries: 285, branch: 246

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dart/flutter/editable_text.dart` (DART) | Magnitude: 5643.76 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5764, branch: 1826, doc: 1641, encapsulation: 1072
- `cobol/cics-genapp/lgacus01.cbl` (COBOL) | Magnitude: 93.42 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 156, state_mutation: 43, branch: 13, structural_boundaries: 12
- `matlab/eeglab/pop_loadset.m` (MATLAB) | Magnitude: 301.8 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 266, indent_spaces: 182, indent_tabs: 118, branch: 102
- `perl/exiftool/exiftool` (PERL) | Magnitude: 16493.72 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 10760, indent_spaces: 4384, branch: 4334, structural_boundaries: 1081
- `cobol/cics-genapp/lgapol01.cbl` (COBOL) | Magnitude: 90.92 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 39, branch: 13, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `zig/zls/mach/testing.zig` (ZIG) | Magnitude: 253.58 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, doc: 57, branch: 36, immutability_locks: 29
- `perl/mojo/Template.pm` (PERL) | Magnitude: 1060.22 | Delta: **0.203 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 425, indent_spaces: 340, branch: 250, ui_framework: 150

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `typescript/playwright/connection.ts` (TYPESCRIPT) | Magnitude: 58.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, state_mutation: 140, structural_boundaries: 119, branch: 118
- `python/fastapi/tests/test_dependency_contextmanager.py` (PYTHON) | Magnitude: 349.96 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 158, test: 116, safety: 93
- `agc_assembly/apollo-11/RCS_FAILURE_MONITOR.agc` (AGC_ASSEMBLY) | Magnitude: 54.56 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 32, state_mutation: 18, args: 15
- `python/fastapi/tests/test_dependency_class.py` (PYTHON) | Magnitude: 119.68 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 65, indent_spaces: 56, api: 34, concurrency: 30
- `swift/alamofire/ParameterEncoder.swift` (SWIFT) | Magnitude: 511.62 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 136, doc: 58, branch: 54, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `python/numpy/cfuncs.py` (PYTHON) | Magnitude: 648.14 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 140, indent_spaces: 132, branch: 61, dead_code: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `php/magento2/AbstractBlock.php` (PHP) | Magnitude: 50.08 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 257, indent_spaces: 157, safety_bypasses: 37, structural_boundaries: 29
- `php/wordpress/class-wp-query.php` (PHP) | Magnitude: 1135.61 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 444, safety_bypasses: 125, state_mutation: 118, indent_tabs: 117

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dart/flutter/semantics.dart` (DART) | Magnitude: 4305.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6223, doc: 2495, branch: 1861, safety: 1432
- `zig/tigerbeetle/constants.zig` (ZIG) | Magnitude: 118.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 328, indent_spaces: 173, globals: 113, immutability_locks: 112
- `csharp/roslyn/CSharpSyntaxTree.cs` (CSHARP) | Magnitude: 1424.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 778, branch: 205, doc: 194, structural_boundaries: 110
- `solidity/openzeppelin/Proxy.sol` (SOLIDITY) | Magnitude: 34.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, reflection_metaprogramming: 14, structural_boundaries: 12, branch: 10
- `rust/holylang/parser.rs` (RUST) | Magnitude: 1331.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 666, structural_boundaries: 251, branch: 227, safety: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `c/doom/m_fixed.h` (C) | Magnitude: 292.8 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 273, macros: 6, api: 4, branch: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `dockerfile/moby/builder/dockerfile/copy.go` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `lua/redis/server.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 98.7569%)
- `go/core/value.go` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zig/zig/Zcu.zig` -> **Severity: 1912.185** (Blast Radius: 22.365 * Doc Risk: 85.499%)
- `zig/zig/InternPool.zig` -> **Severity: 1275.379** (Blast Radius: 15.637 * Doc Risk: 81.5616%)
- `zig/zig/Compilation.zig` -> **Severity: 987.88** (Blast Radius: 13.29 * Doc Risk: 74.3326%)
- `zig/tigerbeetle/constants.zig` -> **Severity: 957.897** (Blast Radius: 12.346 * Doc Risk: 77.5876%)
- `zig/zig/Type.zig` -> **Severity: 569.747** (Blast Radius: 5.911 * Doc Risk: 96.3876%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
