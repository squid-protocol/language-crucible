# ARCHITECTURAL_BRIEF: language-crucible
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/home/joe/nyx_projects/language-crucible` |
| **Timestamp** | `2026-08-03T12:50:20.203246+00:00` |
| **Scan Duration** | `27.62s` |
| **Git Branch** | `main` |
| **Git Commit** | `2ee029370c5fa6a43cb8b81a0d2a00bcf78c2865` |
| **Git Remote** | `https://github.com/squid-protocol/language-crucible` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

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
| Total Artifacts | 1125 |
| Analyzed Artifacts (Scanned) | 944 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 181 |
| Total LOC | 452540 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 83.9% |
| Dominant Lang | SCHEME |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7106 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3489 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9511 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 66 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 269 | 69826 | 28.5% |
| PLAINTEXT | 46 | 0 | 4.9% |
| GO | 46 | 11610 | 4.9% |
| C | 44 | 39353 | 4.7% |
| RUST | 43 | 22519 | 4.6% |
| PHP | 36 | 18919 | 3.8% |
| COBOL | 34 | 6649 | 3.6% |
| CPP | 33 | 19443 | 3.5% |
| ZIG | 32 | 68347 | 3.4% |
| MARKDOWN | 29 | 0 | 3.1% |
| TYPESCRIPT | 24 | 21446 | 2.5% |
| PERL | 22 | 32191 | 2.3% |
| JAVASCRIPT | 19 | 14859 | 2.0% |
| JCL | 15 | 919 | 1.6% |
| JAVA | 14 | 4895 | 1.5% |
| HTML | 13 | 606 | 1.4% |
| RUBY | 13 | 2901 | 1.4% |
| JSON | 12 | 425 | 1.3% |
| XML | 11 | 0 | 1.2% |
| AGC_ASSEMBLY | 10 | 7708 | 1.1% |
| ASSEMBLY | 8 | 2320 | 0.8% |
| M4 | 8 | 13014 | 0.8% |
| POWERSHELL | 8 | 4560 | 0.8% |
| CSHARP | 8 | 10899 | 0.8% |
| SHELL | 8 | 6195 | 0.8% |
| ABAP | 7 | 2717 | 0.7% |
| APEX | 7 | 879 | 0.7% |
| DART | 7 | 9681 | 0.7% |
| HASKELL | 7 | 1732 | 0.7% |
| SCALA | 7 | 4264 | 0.7% |
| SOLIDITY | 7 | 779 | 0.7% |
| SQLITE | 7 | 152 | 0.7% |
| YAML | 7 | 121 | 0.7% |
| FORTRAN | 6 | 18540 | 0.6% |
| MATLAB | 6 | 3669 | 0.6% |
| SWIFT | 6 | 1454 | 0.6% |
| MAKEFILE | 5 | 3109 | 0.5% |
| BLP | 5 | 422 | 0.5% |
| DOCKERFILE | 5 | 764 | 0.5% |
| KOTLIN | 5 | 197 | 0.5% |
| NIX | 5 | 367 | 0.5% |
| OBJECTIVE-C | 5 | 704 | 0.5% |
| CSV | 5 | 26 | 0.5% |
| CSS | 4 | 295 | 0.4% |
| PROTO | 4 | 76 | 0.4% |
| SCHEME | 4 | 16755 | 0.4% |
| TD | 4 | 1074 | 0.4% |
| BATCH | 3 | 321 | 0.3% |
| HLO | 3 | 48 | 0.3% |
| MLIR | 3 | 132 | 0.3% |
| LIVECODE | 2 | 903 | 0.2% |
| TCL | 2 | 2213 | 0.2% |
| YACC | 1 | 1542 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.638`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 489 | 51.8% |
| file_cluster_13 | 208 | 22.0% |
| file_cluster_0 | 72 | 7.6% |
| file_cluster_4 | 27 | 2.9% |
| file_cluster_16 | 20 | 2.1% |
| file_cluster_11 | 18 | 1.9% |
| file_cluster_17 | 9 | 1.0% |
| file_cluster_12 | 7 | 0.7% |
| file_cluster_15 | 6 | 0.6% |
| file_cluster_9 | 4 | 0.4% |
| file_cluster_2 | 4 | 0.4% |
| file_cluster_6 | 2 | 0.2% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 75 | 7.9% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 181*

**Composition by Extension & Reason:**
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Monolithic Amalgamation: 36288 LOC exceeds safe regex boundaries)
- `.go`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tar`: 7x Excluded (Explicitly Denied Extension: '.tar')
- `.test`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 37746 LOC exceeds safe regex boundaries), 1x Excluded (Machine-Generated Source Code Signature: 8582 LOC)
- `.ts`: 1x Excluded (Lexical Monotony: High structural repetition detected in 11395 LOC), 1x Excluded (Monolithic Amalgamation: 54435 LOC exceeds safe regex boundaries), 1x Excluded (Lexical Monotony: High structural repetition detected in 6379 LOC)
- `.json`: 1x Excluded (Monolithic Amalgamation: 269621 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 300555 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 315951 LOC exceeds safe regex boundaries)
- `.y`: 3x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus), 1x Excluded (Machine-Generated Source Code Signature: 2161 LOC)
- `.toml`: 3x Excluded (Unsupported Extension: '.toml')
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 96 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1695 LOC)
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2342 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1541 LOC)
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xaml`: 3x Excluded (Unsupported Extension: '.xaml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 26.0 | 11.4 | 0.0 |
| Error & Exception Exposure | 0.0 | 98.8 | 22.8 | 4.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 81.7 | 31.2 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.3 | 4.7 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 40.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.8 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 86.1 | 58.9 | 34.9 | 34.9 |
| Volatility Exposure | 0.0 | 73.4 | 26.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.5 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 43.6 | 11.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 28.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `data/fortran/wrf/regtest_hwrf.csh` (Hits: 1221)
- `data/fortran/wrf/regtest_nmmnest.csh` (Hits: 1165)
- `data/perl/exiftool/exiftool` (Hits: 333)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **testclient.py** (`data/python/fastapi/fastapi/testclient.py`) — 185 inbound connections
2. **os.asm** (`data/assembly/bootos/os.asm`) — 33 inbound connections
3. **exceptions.py** (`data/python/fastapi/fastapi/exceptions.py`) — 33 inbound connections
4. **responses.py** (`data/python/fastapi/fastapi/responses.py`) — 26 inbound connections
5. **types.py** (`data/python/fastapi/fastapi/types.py`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wp-settings.php** (`data/php/wordpress/wp-settings.php`) — 338 outbound dependencies
2. **editor_node.cpp** (`data/cpp/godot/editor_node.cpp`) — 156 outbound dependencies
3. **bevy_ecs_world.rs** (`data/rust/bevy/bevy_ecs_world.rs`) — 156 outbound dependencies
4. **ReplicaManager.scala** (`data/scala/kafka/ReplicaManager.scala`) — 144 outbound dependencies
5. **Nodes.js** (`data/javascript/threejs/Nodes.js`) — 139 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `lsm_mosaic` (@ `data/fortran/wrf/module_sf_noahdrv.F`) -> Impact: **44966.3** | LOC: 2205
- `lsm` (@ `data/fortran/wrf/module_sf_noahdrv.F`) -> Impact: **22558.3** | LOC: 1402
  * *Intent:* #endif
- `init_domain_rk` (@ `data/fortran/wrf/module_initialize_real.F`) -> Impact: **20032.3** | LOC: 4586
- `phy_init` (@ `data/fortran/wrf/module_physics_init.F`) -> Impact: **10120.1** | LOC: 1601
- `bl_init` (@ `data/fortran/wrf/module_physics_init.F`) -> Impact: **9581.3** | LOC: 1368
- `vert_interp` (@ `data/fortran/wrf/module_initialize_real.F`) -> Impact: **7689.2** | LOC: 703
- `generate_function_header` (@ `data/python/cython/Nodes.py`) -> Impact: **6516.9** | LOC: 1067
  * *Intent:* # this will also analyse the default values and the function name assignment self.py_func_stat = self.py_func_stat.analyse_expressions(env) elif self....
- `Anonymous_Block_[Truncated]` (@ `data/fortran/wrf/regtest_hwrf.csh`) -> Impact: **6259.2** | LOC: 3717
  * *Intent:* # These need to be changed for your particular set of runs. This is # where email gets sent.
- `_ensure_ti_has_dag_version_id` (@ `data/python/airflow/scheduler_job_runner.py`) -> Impact: **6053.4** | LOC: 2909
- `Anonymous_Block_[Truncated]` (@ `data/fortran/wrf/regtest_nmmnest.csh`) -> Impact: **5943.4** | LOC: 3539
  * *Intent:* # These need to be changed for your particular set of runs. This is # where email gets sent.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `ape_grub_entry` (@ `data/assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `ape_macho` (@ `data/assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `netbsd.ident` (@ `data/assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `ape_disk` (@ `data/assembly/cosmopolitan/ape.S`) -> **O(2^N) [Recursive]**
- `compiler_set_qualname` (@ `data/c/cpython/compile.c`) -> **O(2^N) [Recursive]**
- `insertdict` (@ `data/c/cpython/dictobject.c`) -> **O(2^N) [Recursive]**
- `PyFrame_GetLineNumber` (@ `data/c/cpython/frameobject.c`) -> **O(2^N) [Recursive]**
- `refchain_init` (@ `data/c/cpython/object.c`) -> **O(2^N) [Recursive]**
- `translate_code` (@ `data/c/sqlite/lemon.c`) -> **O(2^N) [Recursive]**
- `scheme_do_eval` (@ `data/scheme/racket/eval.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `data/fortran/wrf/regtest_hwrf.csh`) -> DB Complexity: **3743**
  * *Intent:* # These need to be changed for your particular set of runs. This is # where email gets sent.
- `Anonymous_Block_[Truncated]` (@ `data/fortran/wrf/regtest_nmmnest.csh`) -> DB Complexity: **3563**
  * *Intent:* # These need to be changed for your particular set of runs. This is # where email gets sent.
- `init_domain_rk` (@ `data/fortran/wrf/module_initialize_real.F`) -> DB Complexity: **1511**
- `lsm_mosaic` (@ `data/fortran/wrf/module_sf_noahdrv.F`) -> DB Complexity: **772**
- `translate_code` (@ `data/c/sqlite/lemon.c`) -> DB Complexity: **658**
- `PrintTagList` (@ `data/perl/exiftool/exiftool`) -> DB Complexity: **529**
  * *Intent:* #------------------------------------------------------------------------------ # Print list of tags # Inputs: 0) message, 1-N) list of tag names
- `compileTopLevelStatement` (@ `data/typescript/assemblyscript/compiler.ts`) -> DB Complexity: **487**
- `lsm` (@ `data/fortran/wrf/module_sf_noahdrv.F`) -> DB Complexity: **413**
  * *Intent:* #endif
- `__MCStringCantBeEqualToNative` (@ `data/livecode/core/foundation-string.cpp`) -> DB Complexity: **386**
- `ConvertBitrate` (@ `data/perl/exiftool/ExifTool.pm`) -> DB Complexity: **373**
  * *Intent:* #------------------------------------------------------------------------------ # Print conversion for bitrate values # Inputs: 0) bitrate in bits per...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `data/scheme/racket` | 7 | 214427.61 | 31.46% | 3.73% |
| `data/fortran/wrf` | 14 | 185169.76 | 70.41% | 31.2% |
| `data/zig/zig` | 5 | 48995.7 | 26.57% | 37.39% |
| `data/livecode/core` | 11 | 41634.92 | 31.83% | 25.04% |
| `data/perl/exiftool` | 6 | 36047.26 | 49.51% | 19.39% |
| `data/python/cython` | 4 | 35974.46 | 24.6% | 87.17% |
| `data/zig/zls` | 6 | 28672.86 | 33.41% | 29.88% |
| `data/c/cpython` | 8 | 25225.14 | 79.67% | 19.27% |
| `data/perl/spamassassin` | 8 | 24711.0 | 71.46% | 59.32% |
| `data/csharp/roslyn` | 7 | 24457.94 | 23.87% | 51.8% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `data/apex/apex-recipes/QueueableRecipes.cls` -> **100.0%** Exposure
- `data/python/cython/CodeGeneration.py` -> **100.0%** Exposure
- `data/python/wtfpython/2_tricky_strings.py` -> **100.0%** Exposure
- `data/python/wtfpython/noxfile.py` -> **100.0%** Exposure
- `data/cpp/NVDA/nvdaControllerInternal.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `data/agc_assembly/apollo-11/AGC_BLOCK_TWO_SELF-CHECK.agc` -> **100.0%** Exposure
- `data/agc_assembly/apollo-11/EXECUTIVE.agc` -> **100.0%** Exposure
- `data/agc_assembly/apollo-11/INTERPRETER.agc` -> **100.0%** Exposure
- `data/agc_assembly/apollo-11/PINBALL_GAME_BUTTONS_AND_LIGHTS.agc` -> **100.0%** Exposure
- `data/agc_assembly/apollo-11/WAITLIST.agc` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `data/rust/wasmtime/wasmtime_pulley_interp.rs` -> **177** Orphaned Functions | **28** Duplicates
- `data/python/cython/Nodes.py` -> **0** Orphaned Functions | **137** Duplicates
- `data/groovy/gradle/DefaultProject.java` -> **61** Orphaned Functions | **69** Duplicates
- `data/typescript/vscode/async.ts` -> **31** Orphaned Functions | **97** Duplicates
- `data/rust/serde/serde_core_de_impls.rs` -> **5** Orphaned Functions | **113** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `data/c/cpython/ceval.c` -> **0.0002%** Exposure
- `data/csharp/roslyn/MethodCompiler.cs` -> **0.0001%** Exposure
### Exploit Generation Surface
- `data/abap/abapGit/zcl_abapgit_git_porcelain.clas.abap` -> **100.0%** Exposure
- `data/apex/apex-recipes/SOQLRecipes_Tests.cls` -> **100.0%** Exposure
- `data/cpp/NVDA/braille.py` -> **100.0%** Exposure
- `data/fortran/wrf/configure_reader.py` -> **100.0%** Exposure
- `data/fortran/wrf/sourcetree.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `data/cobol/cics-genapp/sampcma.jcl` -> **100.0%** Exposure
- `data/cobol/cics-genapp/sampncs.jcl` -> **100.0%** Exposure
- `data/cobol/cics-genapp/samptsq.jcl` -> **100.0%** Exposure
- `data/cobol/cics-genapp/sampwui.jcl` -> **100.0%** Exposure
- `data/jcl/cics-genapp/base/cntl/itpentr.jcl` -> **100.0%** Exposure
### Raw Memory Manipulation
- `data/c/cpython/compile.c` -> **10.0%** Exposure
- `data/c/cpython/gc.c` -> **10.0%** Exposure
- `data/c/cpython/object.c` -> **10.0%** Exposure
- `data/c/micropython/compile.c` -> **10.0%** Exposure
- `data/c/micropython/emitnative.c` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `data/cobol/cics-genapp/lgacdb01.cbl` -> **99.0093%** Exposure
- `data/python/twisted/transport.py` -> **24.6284%** Exposure
### Algorithmic DoS Exposure
- `data/assembly/cosmopolitan/loader.c` -> **100.0%** Exposure
- `data/c/cpython/compile.c` -> **100.0%** Exposure
- `data/c/cpython/dictobject.c` -> **100.0%** Exposure
- `data/c/cpython/frameobject.c` -> **100.0%** Exposure
- `data/c/cpython/gc.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8404` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `data/php/laravel_core/Router.php` (PHP) -> Cumulative Risk: **1019.08**
- **Archetype:** `file_cluster_13` (Distance: 13.302 IQR)
- **Magnitude:** 1163.62 | **LOC:** 1530 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `toResponse` (Impact: 157.4), `view` (Impact: 49.5), `resolveMiddleware` (Impact: 38.3)

### 2. `data/groovy/gradle/DefaultPluginManager.java` (JAVA) -> Cumulative Risk: **976.4**
- **Archetype:** `file_cluster_13` (Distance: 11.234 IQR)
- **Magnitude:** 629.58 | **LOC:** 369 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `doApply` (Impact: 104.1), `pluginsForId` (Impact: 81.2), `addPluginInternal` (Impact: 61.0)

### 3. `data/fortran/wrf/gen_be_wrapper.ksh` (SHELL) -> Cumulative Risk: **975.8**
- **Archetype:** `file_cluster_0` (Distance: 15.714 IQR)
- **Magnitude:** 105.06 | **LOC:** 95 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Cognitive Load (97.5076%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 47.9), `__global_context__` (Impact: 3.9)

### 4. `data/perl/mojo/IOLoop.pm` (PERL) -> Cumulative Risk: **970.64**
- **Archetype:** `file_cluster_4` (Distance: 14.512 IQR)
- **Magnitude:** 1893.86 | **LOC:** 552 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `client` (Impact: 1251.4), `acceptor` (Impact: 6.4)

### 5. `data/php/symfony/ContainerBuilder.php` (PHP) -> Cumulative Risk: **952.1**
- **Archetype:** `file_cluster_13` (Distance: 14.356 IQR)
- **Magnitude:** 2963.8 | **LOC:** 1837 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `createService` (Impact: 1066.3), `doResolveServices` (Impact: 395.2), `resolveEnvPlaceholders` (Impact: 338.9)

### 6. `data/php/magento2/AbstractBlock.php` (PHP) -> Cumulative Risk: **947.01**
- **Archetype:** `file_cluster_13` (Distance: 13.785 IQR)
- **Magnitude:** 727.86 | **LOC:** 1233 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getChildChildHtml` (Impact: 31.1), `setChild` (Impact: 28.6), `_loadCache` (Impact: 27.8)

### 7. `data/php/guzzle/Pool.php` (PHP) -> Cumulative Risk: **945.77**
- **Archetype:** `file_cluster_4` (Distance: 13.812 IQR)
- **Magnitude:** 133.28 | **LOC:** 126 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__construct` (Impact: 49.4), `cmpCallback` (Impact: 15.7), `promise` (Impact: 5.4)

### 8. `data/groovy/gradle/DefaultProject.java` (JAVA) -> Cumulative Risk: **941.37**
- **Archetype:** `file_cluster_0` (Distance: 10.853 IQR)
- **Magnitude:** 1689.2 | **LOC:** 1568 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `defaultTasks` (Impact: 56.5), `configure` (Impact: 34.9), `getAllTasks` (Impact: 30.4)

### 9. `data/php/magento2/Mysql.php` (PHP) -> Cumulative Risk: **933.0**
- **Archetype:** `file_cluster_13` (Distance: 14.738 IQR)
- **Magnitude:** 7214.94 | **LOC:** 4388 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `showTableStatus` (Impact: 4279.5), `prepareColumnValue` (Impact: 190.9), `dropColumn` (Impact: 110.2)

### 10. `data/csharp/roslyn/CSharpCompilation.cs` (CSHARP) -> Cumulative Risk: **928.34**
- **Archetype:** `file_cluster_8` (Distance: 13.303 IQR)
- **Magnitude:** 4103.26 | **LOC:** 5286 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetDiagnosticsForMethodBodiesInTree` (Impact: 1426.6), `FindEntryPoint` (Impact: 340.9), `AppendSymbolsWithName` (Impact: 170.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `data/scheme/racket/cpnanopass.ss` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.625 IQR)
- **Top Global Matches:** file_cluster_8: 11.625, file_cluster_17: 12.151, file_cluster_15: 12.226
- **Magnitude:** 97214.62 | **LOC:** 10910 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (20.5424%), Tech Debt (8.8948%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1339`, `structural_boundaries: 934`, `args: 45`, `func_start: 45`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 1160`, `dead_code: 7`, `planned_debt: 23`, `fragile_debt: 3`
* *Architecture:* `io: 57`, `import: 10`
* *Defense:* `safety: 72`, `doc: 15`, `immutability_locks: 305`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/scheme/racket/io.ss` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.51 IQR)
- **Top Global Matches:** file_cluster_8: 10.51, file_cluster_7: 11.127, file_cluster_15: 11.216
- **Magnitude:** 86770.48 | **LOC:** 6399 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.7219%), Tech Debt (8.1334%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1032`, `structural_boundaries: 488`, `args: 65`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `state_mutation: 271`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `io: 38`
* *Defense:* `safety: 14`, `doc: 86`, `sync_locks: 1`, `immutability_locks: 34`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.895
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024909
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `data/fortran/wrf/module_sf_noahdrv.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.499 IQR)
- **Top Global Matches:** file_cluster_11: 16.499, file_cluster_17: 16.549, file_cluster_0: 16.57
- **Magnitude:** 73055.76 | **LOC:** 5355 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 772
- **Risk Profile:** Cognitive Load (68.3262%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lsm_mosaic` (Impact: 44966.3 | O(2^N) | DB: 772)
  * `lsm` (Impact: 22558.3 | O(2^N) | DB: 413)
    * *Intent:* #endif
  * `LSMINIT` (Impact: 1754.0 | O(2^N) | DB: 45)
  * `lsm_mosaic_init` (Impact: 521.4 | O(N^6) | DB: 22)
  * `SOIL_VEG_GEN_PARM` (Impact: 59.5 | O(N^5) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 723`, `structural_boundaries: 685`, `args: 648`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3116`, `dead_code: 42`
* *Architecture:* `io: 100`, `api: 5`, `import: 22`
* *Defense:* `safety: 410`, `doc: 1`, `immutability_locks: 159`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.914
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001057
  * `Imports (Out-Degree: 0):` module_sf_noahlsm, module_ra_gfdleta, module_sf_bep_bem, module_data_gocart_dust, module_sf_noahlsm_glacial_only, module_sf_urban, module_sf_bep, module_wrf_error...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `data/fortran/wrf/module_initialize_real.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.927 IQR)
- **Top Global Matches:** file_cluster_11: 15.927, file_cluster_13: 16.045, file_cluster_0: 16.089
- **Magnitude:** 49921.48 | **LOC:** 9207 | **CtrlFlow:** 84.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1511
- **Risk Profile:** Cognitive Load (98.3091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init_domain_rk` (Impact: 20032.3 | O(N^6) | DB: 1511)
  * `vert_interp` (Impact: 7689.2 | O(N^6) | DB: 242)
  * `rh_to_mxrat1` (Impact: 2270.8 | O(2^N) | DB: 61)
  * `rh_to_mxrat2` (Impact: 1885.9 | O(2^N) | DB: 65)
  * `fillitup` (Impact: 1654.5 | O(2^N) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3165`, `structural_boundaries: 591`, `args: 216`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6920`, `dead_code: 49`
* *Architecture:* `io: 64`, `api: 38`, `import: 47`
* *Defense:* `safety: 253`, `doc: 2`, `immutability_locks: 173`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` module_polarfft, module_bc, module_comm_dm, module_optional_input, module_model_constants, module_domain, module_io_domain, module_llxy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/fortran/wrf/module_physics_init.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.797 IQR)
- **Top Global Matches:** file_cluster_13: 15.797, file_cluster_11: 15.944, file_cluster_17: 15.971
- **Magnitude:** 36210.84 | **LOC:** 5751 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 260
- **Risk Profile:** Cognitive Load (67.0098%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `phy_init` (Impact: 10120.1 | O(2^N) | DB: 260)
  * `bl_init` (Impact: 9581.3 | O(2^N) | DB: 63)
  * `ra_init` (Impact: 4208.4 | O(2^N) | DB: 40)
  * `landuse_init` (Impact: 2593.9 | O(2^N) | DB: 143)
  * `mp_init` (Impact: 2353.8 | O(2^N) | DB: 152)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 804`, `structural_boundaries: 1059`, `args: 1090`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1911`, `dead_code: 31`
* *Architecture:* `io: 38`, `api: 19`, `import: 150`
* *Defense:* `safety: 695`, `doc: 3`, `immutability_locks: 244`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` module_mp_morr_two_moment, module_ra_rrtmg_swf, module_bl_mrf, module_cu_nsas, module_bl_mynnedmf_driver, module_ra_rrtmg_sw, module_mp_fer_hires, module_bl_gfsedmf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/python/cython/Nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.2 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.924 IQR)
- **Top Global Matches:** file_cluster_8: 13.2, file_cluster_13: 13.241, file_cluster_0: 13.312
- **Magnitude:** 35244.84 | **LOC:** 10867 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (62.0599%), Tech Debt (99.2359%)
**Top Internal Functions/Classes:**
  * `generate_function_header` (Impact: 6516.9 | O(2^N) | DB: 58)
    * *Intent:* # this will also analyse the default values and the function name assignment self.py_func_stat = sel...
  * `_analyse_template_types` (Impact: 5342.4 | O(2^N) | DB: 38)
    * *Intent:* # After parsing: # positional_args [ExprNode] List of positional arguments # keyword_args DictNode K...
  * `analyse` (Impact: 3098.6 | O(2^N) | DB: 20)
    * *Intent:* # base CDeclaratorNode
  * `generate_execution_code` (Impact: 1757.8 | O(2^N) | DB: 47)
    * *Intent:* # from ... import statement # # module ImportNode # items [(string, NameNode)] # interned_items [(st...
  * `generate_function_body` (Impact: 1641.6 | O(2^N) | DB: 38)
    * *Intent:* # Generator function node that creates a new generator instance when called. # # gbody GeneratorBody...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2562`, `structural_boundaries: 1693`, `args: 480`, `func_start: 478`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 1`, `state_mutation: 1162`, `dead_code: 63`, `planned_debt: 16`, `fragile_debt: 18`, `duplicate_logic: 137`
* *Architecture:* `api: 557`, `concurrency: 7`, `import: 73`
* *Defense:* `safety: 147`, `doc: 92`, `test: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .ExprNodes, .., .Errors, cython, types, .PyrexTypes, .Code, .Pythran...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/livecode/core/revsaveasstandalone.livecodescript` (LIVECODE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.644 IQR)
- **Top Global Matches:** file_cluster_17: 13.644, file_cluster_0: 14.361, file_cluster_11: 14.362
- **Magnitude:** 32211.72 | **LOC:** 2675 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.121%), Tech Debt (63.4024%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 560`, `structural_boundaries: 256`, `args: 30`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 531`, `dead_code: 14`, `fragile_debt: 16`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 6`
* *Defense:* `safety: 26`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pStack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/perl/exiftool/ExifTool.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.353 IQR)
- **Top Global Matches:** file_cluster_0: 15.353, file_cluster_8: 15.558, file_cluster_13: 15.628
- **Magnitude:** 26302.94 | **LOC:** 10227 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 373
- **Risk Profile:** Cognitive Load (98.2155%), Tech Debt (13.2729%)
**Top Internal Functions/Classes:**
  * `ConvertBitrate` (Impact: 3989.5 | O(N^6) | DB: 373)
    * *Intent:* #------------------------------------------------------------------------------ # Print conversion f...
  * `IsSameID` (Impact: 3228.9 | O(2^N) | DB: 173)
    * *Intent:* #------------------------------------------------------------------------------ # Does group name ma...
  * `ProcessBinaryData` (Impact: 2455.4 | O(2^N) | DB: 142)
    * *Intent:* #------------------------------------------------------------------------------ # Process binary dat...
  * `DoProcessTIFF` (Impact: 2196.8 | O(N^6) | DB: 147)
    * *Intent:* #------------------------------------------------------------------------------ # Process TIFF data ...
  * `GetGroup` (Impact: 1890.2 | O(2^N) | DB: 87)
    * *Intent:* #------------------------------------------------------------------------------ # Get group name for...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4054`, `structural_boundaries: 1607`, `args: 301`, `func_start: 237`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 4`, `state_mutation: 6055`, `dead_code: 11`, `fragile_debt: 8`, `orphaned_logic: 21`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 10`, `import: 81`
* *Defense:* `safety: 56`, `cleanup: 231`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ListSplit, File::RandomAccess, value, Image::ExifTool::Geotag, alternate, Image::ExifTool::HTML, chance, POSIX...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/zig/zls/analysis.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.526 IQR)
- **Top Global Matches:** file_cluster_8: 14.526, file_cluster_0: 14.71, file_cluster_11: 14.71
- **Magnitude:** 18254.66 | **LOC:** 7016 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (63.6568%), Tech Debt (48.8264%)
**Top Internal Functions/Classes:**
  * `resolveTypeOfNodeUncached` (Impact: 3928.3 | O(N^6) | DB: 46)
  * `getFieldAccessType` (Impact: 2239.8 | O(2^N) | DB: 13)
  * `resolveExpressionTypeFromAncestors` (Impact: 1813.0 | O(N^6) | DB: 9)
  * `resolveType` (Impact: 1255.9 | O(2^N) | DB: 1)
  * `eql` (Impact: 926.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3276`, `structural_boundaries: 1181`, `args: 201`, `func_start: 197`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 581`, `dead_code: 9`, `planned_debt: 15`, `fragile_debt: 1`, `duplicate_logic: 37`
* *Architecture:* `api: 193`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 1442`, `doc: 111`, `test: 1`, `immutability_locks: 913`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002378
  * `Imports (Out-Degree: 3):` tracy, DocumentStore.zig, InternPool.zig, references.zig, Uri.zig, version_data, error_msg.zig, builtin...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `data/csharp/roslyn/LanguageParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.608 IQR)
- **Top Global Matches:** file_cluster_8: 13.608, file_cluster_11: 13.763, file_cluster_13: 13.856
- **Magnitude:** 17414.52 | **LOC:** 14680 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 167
- **Risk Profile:** Cognitive Load (65.2025%), Tech Debt (13.4466%)
**Top Internal Functions/Classes:**
  * `ParseMemberName` (Impact: 4720.3 | O(2^N) | DB: 95)
  * `ParseSwitchStatement` (Impact: 3022.7 | O(N^6) | DB: 85)
  * `ParseNamespaceDeclarationCore` (Impact: 1611.8 | O(N^6) | DB: 167)
  * `ScanExplicitlyTypedLambda` (Impact: 1581.4 | O(N^6) | DB: 60)
  * `TryParseConversionOperatorDeclaration` (Impact: 1403.4 | O(N^6) | DB: 133)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1737`, `structural_boundaries: 1186`, `args: 484`, `func_start: 1022`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 8`, `state_mutation: 1769`, `dead_code: 37`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 21`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 161`, `doc: 143`, `immutability_locks: 12`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, Microsoft.CodeAnalysis.Text, Microsoft.CodeAnalysis.Syntax.InternalSyntax, Microsoft.CodeAnalysis.CSharp.Symbols, Roslyn.Utilities, System.Diagnostics.CodeAnalysis, System.Threading, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/zig/zig/Compilation.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.859 IQR)
- **Top Global Matches:** file_cluster_8: 13.859, file_cluster_7: 14.068, file_cluster_13: 14.147
- **Magnitude:** 13373.24 | **LOC:** 8171 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (24.3848%), Tech Debt (31.7731%)
**Top Internal Functions/Classes:**
  * `addCommonCCArgs` (Impact: 1475.8 | O(N^6) | DB: 1)
    * *Intent:* /// Add common C compiler args between translate-c and C object compilation.
  * `update` (Impact: 1315.3 | O(2^N) | DB: 4)
    * *Intent:* /// Detect changes to source files, perform semantic analysis, and update the output files.
  * `addCCArgs` (Impact: 1081.2 | O(N^6) | DB: 2)
    * *Intent:* /// Add common C compiler args and Clang specific args.
  * `updateCObject` (Impact: 897.5 | O(N^6) | DB: 7)
  * `performAllTheWork` (Impact: 687.9 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2282`, `structural_boundaries: 664`, `args: 183`, `func_start: 183`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 266`, `state_mutation: 402`, `dead_code: 4`, `planned_debt: 35`, `fragile_debt: 6`, `duplicate_logic: 23`
* *Architecture:* `io: 1`, `api: 171`, `concurrency: 6`, `import: 35`
* *Defense:* `safety: 1138`, `doc: 385`, `test: 16`, `sync_locks: 76`, `immutability_locks: 817`, `cleanup: 163`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.02
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.003759
  * `Imports (Out-Degree: 3):` glibc.zig, libcxx.zig, freebsd.zig, mingw.zig, Type.zig, Config.zig, introspect.zig, libunwind.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `data/zig/zig/Type.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.676 IQR)
- **Top Global Matches:** file_cluster_8: 12.676, file_cluster_7: 12.928, file_cluster_16: 12.987
- **Magnitude:** 12907.8 | **LOC:** 4357 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (14.7704%), Tech Debt (19.6514%)
**Top Internal Functions/Classes:**
  * `abiSizeInner` (Impact: 1899.7 | O(2^N) | DB: 1)
    * *Intent:* /// If you pass `eager` you will get back `scalar` and assert the type is resolved. /// In this case...
  * `abiAlignmentInner` (Impact: 1759.7 | O(2^N) | DB: 1)
    * *Intent:* /// If you pass `eager` you will get back `scalar` and assert the type is resolved. /// In this case...
  * `hasRuntimeBitsInner` (Impact: 1250.8 | O(2^N))
    * *Intent:* /// true if and only if the type takes up space in memory at runtime. /// There are two reasons a ty...
  * `onePossibleValue` (Impact: 1077.5 | O(2^N) | DB: 5)
    * *Intent:* /// During semantic analysis, instead call `Sema.typeHasOnePossibleValue` which /// resolves field t...
  * `bitSizeInner` (Impact: 1007.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1436`, `structural_boundaries: 717`, `args: 194`, `func_start: 189`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 83`, `dead_code: 1`, `planned_debt: 10`, `duplicate_logic: 9`
* *Architecture:* `api: 379`, `import: 7`
* *Defense:* `safety: 429`, `doc: 187`, `immutability_locks: 516`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006765
  * `Imports (Out-Degree: 2):` target.zig, Zcu.zig, InternPool.zig, Sema.zig, Value.zig, builtin, std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `data/c/sqlite/lemon.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.564 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.665 IQR)
- **Top Global Matches:** file_cluster_8: 15.564, file_cluster_11: 15.62, file_cluster_13: 15.649
- **Magnitude:** 11310.5 | **LOC:** 6076 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 658
- **Risk Profile:** Cognitive Load (91.7266%), Tech Debt (8.7521%)
**Top Internal Functions/Classes:**
  * `translate_code` (Impact: 4837.7 | O(2^N) | DB: 658)
  * `eval_preprocessor_boolean` (Impact: 365.0 | O(2^N) | DB: 38)
    * *Intent:* /* Insert transaction set at index i. */ #if 0
  * `Parse` (Impact: 335.7 | O(N^3) | DB: 105)
  * `FindStates` (Impact: 185.2 | O(N^3) | DB: 31)
  * `acttab_insert` (Impact: 168.8 | O(N^6) | DB: 34)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 939`, `structural_boundaries: 478`, `args: 135`, `func_start: 78`, `class_start: 150`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 3669`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 21`, `api: 599`, `import: 7`
* *Defense:* `safety: 17`, `doc: 15`, `test: 12`, `immutability_locks: 69`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdarg.h, stdio.h, string.h, unistd.h, stdlib.h, assert.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/scheme/racket/thread.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.105 IQR)
- **Top Global Matches:** file_cluster_8: 9.105, file_cluster_7: 10.009, file_cluster_1: 10.241
- **Magnitude:** 10239.71 | **LOC:** 1323 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.0315%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 25`, `args: 52`, `func_start: 52`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `concurrency: 2`, `import: 1`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/scheme/racket/schemify.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.322 IQR)
- **Top Global Matches:** file_cluster_8: 8.322, file_cluster_7: 9.261, file_cluster_1: 9.494
- **Magnitude:** 10027.56 | **LOC:** 1127 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.9451%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 29`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/python/numpy/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.574 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 12.574, file_cluster_7: 12.671, file_cluster_13: 12.756
- **Magnitude:** 9960.0 | **LOC:** 8995 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (27.3977%), Tech Debt (62.7219%)
**Top Internal Functions/Classes:**
  * `tofile` (Impact: 3017.2 | O(2^N) | DB: 14)
  * `_check_fill_value` (Impact: 893.2 | O(N^6) | DB: 19)
  * `__new__` (Impact: 637.8 | O(N^6))
  * `var` (Impact: 379.3 | O(2^N))
    * *Intent:* # Case 1. : no mask in input. # Erase the current mask ? # With a reduced version if shrink: _data._...
  * `__getitem__` (Impact: 309.0 | O(2^N))
    * *Intent:* # Bas les masques !
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 773`, `args: 269`, `func_start: 268`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 204`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 20`
* *Architecture:* `api: 187`, `import: 16`
* *Defense:* `safety: 177`, `doc: 410`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` textwrap, numpy._core.umath, inspect, functools, numpy, time., numpy._core, times....
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/perl/bugzilla/Bug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.454 IQR)
- **Top Global Matches:** file_cluster_0: 14.454, file_cluster_8: 14.523, file_cluster_13: 14.552
- **Magnitude:** 9861.86 | **LOC:** 5124 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 317
- **Risk Profile:** Cognitive Load (73.8361%), Tech Debt (99.8742%)
**Top Internal Functions/Classes:**
  * `_check_groups` (Impact: 4495.1 | O(N^6) | DB: 317)
  * `DB_COLUMNS` (Impact: 2050.9 | O(N^6) | DB: 260)
    * *Intent:* # This is a sub because it needs to call other subroutines.
  * `_check_bug_status` (Impact: 166.1 | O(N^3) | DB: 14)
  * `check_can_change_field` (Impact: 107.9 | O(N^2) | DB: 18)
    * *Intent:* # can add code here for site-specific policy changes, according to the # instructions given in the B...
  * `get_activity` (Impact: 105.8 | O(N^6) | DB: 20)
    * *Intent:* # Get the activity of a bug, starting from $starttime (if given). # This routine assumes Bugzilla::B...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1349`, `structural_boundaries: 1327`, `args: 151`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 2234`, `dead_code: 5`, `fragile_debt: 215`
* *Architecture:* `api: 1`, `import: 40`
* *Defense:* `safety: 10`, `doc: 140`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Bugzilla::FlagType, Bugzilla::Milestone, bugs, Bugzilla::Comment, comment, more, List::Util, comments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/fortran/wrf/module_domain.F` (FORTRAN | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.815 IQR)
- **Top Global Matches:** file_cluster_11: 15.815, file_cluster_13: 15.823, file_cluster_0: 15.856
- **Magnitude:** 9510.36 | **LOC:** 2988 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 213
- **Risk Profile:** Cognitive Load (57.7009%), Tech Debt (10.3465%)
**Top Internal Functions/Classes:**
  * `ensure_space_field` (Impact: 1571.1 | O(2^N) | DB: 1)
  * `wrf_patch_domain` (Impact: 705.4 | O(N^6) | DB: 67)
  * `domain_clock_get` (Impact: 690.5 | O(2^N) | DB: 37)
  * `alloc_and_configure_domain` (Impact: 499.4 | O(2^N) | DB: 213)
  * `get_ijk_from_grid1` (Impact: 374.3 | O(2^N) | DB: 144)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 338`, `args: 273`, `func_start: 52`, `class_start: 4`
* *Risk/State:* `state_mutation: 2198`, `dead_code: 15`, `fragile_debt: 4`
* *Architecture:* `io: 32`, `api: 51`, `import: 19`
* *Defense:* `safety: 274`, `doc: 46`, `immutability_locks: 105`, `cleanup: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.52
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003171
  * `Imports (Out-Degree: 1):` module_driver_constants, module_domain, module_utility, module_machine, module_domain_type, module_wrf_error, module_configure
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `data/perl/exiftool/exiftool` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.054 IQR)
- **Top Global Matches:** file_cluster_0: 15.054, file_cluster_17: 15.236, file_cluster_13: 15.267
- **Magnitude:** 8964.2 | **LOC:** 8151 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 529
- **Risk Profile:** Cognitive Load (77.2439%), Tech Debt (8.9265%)
**Top Internal Functions/Classes:**
  * `Printable` (Impact: 1704.7 | O(N^5) | DB: 232)
    * *Intent:* #------------------------------------------------------------------------------ # Get the printable ...
  * `PrintTagList` (Impact: 1404.9 | O(N^4) | DB: 529)
    * *Intent:* #------------------------------------------------------------------------------ # Print list of tags...
  * `FilterArgfileLine` (Impact: 306.5 | O(2^N) | DB: 37)
    * *Intent:* #------------------------------------------------------------------------------ # Filter argfile lin...
  * `FormatXML` (Impact: 241.2 | O(2^N) | DB: 12)
    * *Intent:* #------------------------------------------------------------------------------ # Format value for X...
  * `EscapeJSON` (Impact: 76.5 | O(N^2) | DB: 7)
    * *Intent:* #------------------------------------------------------------------------------ # Escape string for ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3632`, `structural_boundaries: 982`, `args: 177`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 20`, `state_mutation: 4723`, `dead_code: 21`, `fragile_debt: 7`
* *Architecture:* `io: 333`, `api: 1`, `concurrency: 2`, `import: 109`
* *Defense:* `safety: 26`, `doc: 236`, `cleanup: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` absolute, Escape, Image::ExifTool::HTML, metadata, Image::ExifTool::TagInfoXML, information, permission, undocumented...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/powershell/core/packaging.psm1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.642 IQR)
- **Top Global Matches:** file_cluster_0: 13.642, file_cluster_15: 13.701, file_cluster_11: 13.75
- **Magnitude:** 8749.74 | **LOC:** 5824 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 238
- **Risk Profile:** Cognitive Load (81.0507%), Tech Debt (21.1499%)
**Top Internal Functions/Classes:**
  * `New-UnixPackage` (Impact: 3690.5 | O(N^6) | DB: 238)
  * `Start-PSPackage` (Impact: 1154.7 | O(2^N) | DB: 99)
  * `New-MSIXPackage` (Impact: 1148.5 | O(N^5) | DB: 113)
  * `New-TarballPackage` (Impact: 201.8 | O(N^4) | DB: 10)
  * `Update-PSSignedBuildFolder` (Impact: 179.4 | O(N^5) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 671`, `structural_boundaries: 155`, `args: 51`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 1439`, `dead_code: 8`, `fragile_debt: 1`, `orphaned_logic: 23`
* *Architecture:* `io: 18`, `api: 346`, `import: 1`
* *Defense:* `safety: 32`, `doc: 63`, `test: 1`, `immutability_locks: 5`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $PSScriptRoot\..\buildCommon\startNativeExecution.ps1, .\build.psm1, $PSScriptRoot\..\Xml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/c/micropython/emitnative.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.817 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.966 IQR)
- **Top Global Matches:** file_cluster_8: 12.817, file_cluster_0: 13.118, file_cluster_13: 13.148
- **Magnitude:** 8726.64 | **LOC:** 3123 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.487%), Tech Debt (11.8177%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 364`, `structural_boundaries: 133`, `args: 3`, `func_start: 87`
* *Risk/State:* `state_mutation: 455`, `dead_code: 10`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `api: 123`, `import: 7`
* *Defense:* `safety: 33`, `test: 29`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, emit.h, string.h, objfun.h, nativeglue.h, objstr.h, assert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/scheme/racket/eval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.64 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.677 IQR)
- **Top Global Matches:** file_cluster_8: 14.64, file_cluster_13: 14.868, file_cluster_7: 14.903
- **Magnitude:** 8282.5 | **LOC:** 4146 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 356
- **Risk Profile:** Cognitive Load (94.5359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scheme_do_eval` (Impact: 4297.0 | O(2^N) | DB: 356)
  * `intersect_dw` (Impact: 338.6 | O(2^N) | DB: 68)
    * *Intent:* /* Continue normal escape: */
  * `scheme_set_global_bucket` (Impact: 167.4 | O(N^6) | DB: 5)
    * *Intent:* #endif #ifdef USE_STACK_BOUNDARY_VAR
  * `define_values_execute` (Impact: 103.6 | O(N^6) | DB: 36)
  * `do_eval_string_all` (Impact: 73.2 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 621`, `structural_boundaries: 147`, `args: 25`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 113`, `high_risk_execution: 2`, `state_mutation: 2240`
* *Architecture:* `io: 5`, `api: 576`, `import: 8`
* *Defense:* `doc: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Memory.h, future.h, signal.h, windows.h, schapp.inc, malloc.h, schmach.h, mzstkchk.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/c/cpython/dictobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.406 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.824 IQR)
- **Top Global Matches:** file_cluster_8: 14.406, file_cluster_11: 14.567, file_cluster_13: 14.574
- **Magnitude:** 8163.56 | **LOC:** 8326 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 322
- **Risk Profile:** Cognitive Load (92.9154%), Tech Debt (21.8647%)
**Top Internal Functions/Classes:**
  * `insertdict` (Impact: 2463.2 | O(2^N) | DB: 322)
  * `_Py_dict_lookup_threadsafe` (Impact: 251.9 | O(2^N) | DB: 16)
  * `dictiter_iternext_threadsafe` (Impact: 99.8 | O(N^6) | DB: 20)
  * `store_instance_attr_lock_held` (Impact: 88.8 | O(N^6) | DB: 10)
  * `dictreviter_iter_lock_held` (Impact: 81.5 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 957`, `structural_boundaries: 540`, `args: 4`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 130`, `state_mutation: 2529`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 35`
* *Architecture:* `io: 2`, `api: 1033`, `import: 19`
* *Defense:* `safety: 196`, `doc: 5`, `test: 198`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eq.h, stdbool.h, pycore_call.h, pycore_pystate.h, pycore_object.h, pycore_bitutils.h, pycore_pyatomic_ft_wrappers.h, pycore_critical_section.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/c/micropython/gc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.52 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.275 IQR)
- **Top Global Matches:** file_cluster_11: 14.52, file_cluster_13: 14.538, file_cluster_0: 14.555
- **Magnitude:** 8162.58 | **LOC:** 1408 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (82.1453%), Tech Debt (8.9548%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 76`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 419`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 77`, `import: 6`
* *Defense:* `safety: 43`, `test: 10`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, string.h, memcheck.h, runtime.h, assert.h, gc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/zig/zig/Zcu.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.817 IQR)
- **Top Global Matches:** file_cluster_8: 13.817, file_cluster_7: 13.887, file_cluster_13: 13.96
- **Magnitude:** 8110.38 | **LOC:** 4802 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (23.6473%), Tech Debt (48.1576%)
**Top Internal Functions/Classes:**
  * `findOutdatedToAnalyze` (Impact: 3172.9 | O(2^N) | DB: 36)
  * `span` (Impact: 2129.3 | O(N^6) | DB: 39)
  * `formatDependee` (Impact: 714.1 | O(N^5) | DB: 4)
  * `markPoDependeeUpToDate` (Impact: 140.8 | O(2^N) | DB: 1)
  * `renderFullyQualifiedDebugName` (Impact: 111.2 | O(2^N))
    * *Intent:* /// This renders e.g. "std/fs.zig:Dir.OpenOptions"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1135`, `structural_boundaries: 443`, `args: 128`, `func_start: 128`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 156`, `high_risk_execution: 76`, `state_mutation: 327`, `dead_code: 3`, `planned_debt: 9`, `duplicate_logic: 26`
* *Architecture:* `io: 12`, `api: 219`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 495`, `doc: 598`, `test: 8`, `sync_locks: 7`, `immutability_locks: 625`, `cleanup: 97`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.253
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005638
  * `Imports (Out-Degree: 3):` Compilation.zig, target.zig, PerThread.zig, Air.zig, build_options, InternPool.zig, link.zig, Type.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `data/rust/serde/serde_core_macros.rs` (RUST) | Magnitude: 17.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 108, doc: 107, generics: 12, immutability_locks: 9
- `data/python/fastapi/tests/test_json_type.py` (PYTHON) | Magnitude: 31.76 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 37, indent_spaces: 24, api: 12, test: 12
- `data/python/fastapi/tests/test_strict_content_type_app_level.py` (PYTHON) | Magnitude: 20.74 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 13, test: 11, safety: 7
- `data/python/fastapi/tests/test_dependency_after_yield_streaming.py` (PYTHON) | Magnitude: 107.04 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 52, indent_spaces: 49, api: 24, args: 20
- `data/python/fastapi/tests/test_dependency_wrapped.py` (PYTHON) | Magnitude: 364.02 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 171, indent_spaces: 154, concurrency: 98, api: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `data/cobol/cics-genapp/lgicdb01.cbl` (COBOL) | Magnitude: 130.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 61, branch: 18, structural_boundaries: 13
- `data/cobol/cics-genapp/lgipdb01.cbl` (COBOL) | Magnitude: 854.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 739, state_mutation: 341, branch: 117, safety: 34
- `data/javascript/threejs/Editor.js` (JAVASCRIPT) | Magnitude: 717.36 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 433, state_mutation: 405, memory_alloc: 77, branch: 63
- `data/fortran/wrf/module_domain.F` (FORTRAN) | Magnitude: 9510.36 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 2198, indent_spaces: 2091, branch: 340, structural_boundaries: 338
- `data/cobol/cics-genapp/lgapol01.cbl` (COBOL) | Magnitude: 75.98 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 34, structural_boundaries: 11, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `data/fortran/wrf/regtest_hwrf.csh` (SHELL) | Magnitude: 6354.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 1588, branch: 1226, io: 1221, safety_bypasses: 1120
- `data/go/core/value.go` (GO) | Magnitude: 2064.34 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 914, state_mutation: 544, branch: 335, doc: 226
- `data/shell/brew/brew` (SHELL) | Magnitude: 406.86 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 202, indent_spaces: 125, state_mutation: 97, safety: 79
- `data/fortran/wrf/cleanCMake.sh` (SHELL) | Magnitude: 70.5 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 45, indent_spaces: 34, branch: 19, io: 14
- `data/zig/tigerbeetle/download.sh` (SHELL) | Magnitude: 110.22 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 53, indent_spaces: 51, branch: 24, io: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `data/python/fastapi/tests/test_security_scopes.py` (PYTHON) | Magnitude: 17.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 19, test: 10, api: 8
- `data/cobol/cics-genapp/lgacdb02.cbl` (COBOL) | Magnitude: 104.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 126, state_mutation: 46, branch: 16, structural_boundaries: 13
- `data/python/fastapi/tests/test_response_model_default_factory.py` (PYTHON) | Magnitude: 18.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 16, safety: 10, test: 8
- `data/cpp/godot/main.cpp` (CPP) | Magnitude: 1706.72 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1369, indent_tabs: 1343, branch: 482, pointers: 363
- `data/sql/baseline/schema.php` (PHP) | Magnitude: 205.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 144, indent_tabs: 116, doc: 31, branch: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `data/dart/flutter/navigator.dart` (DART) | Magnitude: 1394.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1191, doc: 817, func_start: 423, encapsulation: 404
- `data/dockerfile/moby/builder/remotecontext/internal/tarsum/fileinfosums.go` (GO) | Magnitude: 132.96 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 55, state_mutation: 40, structural_boundaries: 27, branch: 18
- `data/go/core/server.go` (GO) | Magnitude: 2288.22 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1040, state_mutation: 714, encapsulation: 327, branch: 291
- `data/dockerfile/moby/builder/dockerfile/buildargs.go` (GO) | Magnitude: 211.22 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 107, indent_tabs: 91, structural_boundaries: 39, pointers: 28
- `data/dart/flutter/object.dart` (DART) | Magnitude: 2289.32 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1800, doc: 824, func_start: 568, encapsulation: 523

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `data/scala/kafka/Partition.scala` (SCALA) | Magnitude: 980.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 733, branch: 160, args: 136, closures: 112
- `data/swift/alamofire/ParameterEncoder.swift` (SWIFT) | Magnitude: 326.04 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 58, indent_spaces: 51, branch: 28, immutability_locks: 14
- `data/zig/zls/mach/module.zig` (ZIG) | Magnitude: 2387.88 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 811, branch: 190, doc: 136, globals: 130
- `data/scala/kafka/ReplicaManager.scala` (SCALA) | Magnitude: 101.44 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 95, doc: 82, immutability_locks: 58
- `data/rust/wasmtime/wasmtime_pulley_interp.rs` (RUST) | Magnitude: 2878.32 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 4256, structural_boundaries: 1652, state_mutation: 1250, generics: 809

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `data/tcl/sqlite/tester.tcl` (TCL) | Magnitude: 1555.62 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1556, state_mutation: 1381, branch: 394, structural_boundaries: 183
- `data/matlab/eeglab/pop_loadset.m` (MATLAB) | Magnitude: 2067.81 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 270, indent_spaces: 153, indent_tabs: 111, branch: 94
- `data/dockerfile/moby/builder/dockerfile/internals_linux.go` (GO) | Magnitude: 69.98 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 30, structural_boundaries: 14, branch: 13
- `data/matlab/eeglab/runica.m` (MATLAB) | Magnitude: 1145.04 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1110, indent_spaces: 966, branch: 359, structural_boundaries: 218
- `data/matlab/eeglab/eeglab.m` (MATLAB) | Magnitude: 1303.78 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1204, indent_spaces: 1179, branch: 468, structural_boundaries: 288

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `data/zig/zls/mach/testing.zig` (ZIG) | Magnitude: 230.68 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, doc: 57, branch: 36, immutability_locks: 29
- `data/html/wordpress_blocks/search.html` (HTML) | Magnitude: 0.01 | Delta: **0.231 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 6, structural_boundaries: 3, ui_framework: 3, indent_tabs: 3
- `data/html/wordpress_blocks/index.html` (HTML) | Magnitude: 0.01 | Delta: **0.321 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 5, structural_boundaries: 3, ui_framework: 3, indent_tabs: 3
- `data/html/wordpress_blocks/page.html` (HTML) | Magnitude: 0.01 | Delta: **0.335 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 3, structural_boundaries: 2, ui_framework: 2, indent_tabs: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `data/python/fastapi/tests/test_http_connection_injection.py` (PYTHON) | Magnitude: 26.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 11, api: 6, concurrency: 6
- `data/php/guzzle/Pool.php` (PHP) | Magnitude: 133.28 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 43, structural_boundaries: 27, doc: 15
- `data/agc_assembly/apollo-11/RCS_FAILURE_MONITOR.agc` (AGC_ASSEMBLY) | Magnitude: 60.16 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 77, indent_tabs: 70, structural_boundaries: 30, state_mutation: 24
- `data/python/fastapi/tests/test_dependency_yield_except_httpexception.py` (PYTHON) | Magnitude: 49.46 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, safety: 29, structural_boundaries: 28, test: 19
- `data/rust/tokio/blocking.rs` (RUST) | Magnitude: 57.04 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, concurrency: 27, generics: 27, structural_boundaries: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `data/python/numpy/cfuncs.py` (PYTHON) | Magnitude: 27.74 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 140, indent_spaces: 129, branch: 49, dead_code: 40
- `data/rust/serde/serde_core_de_mod.rs` (RUST) | Magnitude: 25.48 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 1654, indent_spaces: 235, generics: 174, structural_boundaries: 97

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `data/swift/alamofire/Session.swift` (SWIFT) | Magnitude: 479.58 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 484, indent_spaces: 203, branch: 87, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `data/fortran/wrf/regtest_nmmnest.csh` (SHELL) | Magnitude: 6031.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1497, io: 1165, branch: 1164, safety_bypasses: 1038
- `data/python/twisted/transport.py` (PYTHON) | Magnitude: 1231.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 941, state_mutation: 228, structural_boundaries: 203, encapsulation: 177
- `data/perl/bugzilla/DB.pm` (PERL) | Magnitude: 2846.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 857, state_mutation: 521, doc: 464, branch: 436
- `data/python/fastapi/tests/test_no_swagger_ui_redirect.py` (PYTHON) | Magnitude: 11.1 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 11, test: 9, safety: 6
- `data/python/fastapi/tests/test_serialize_response.py` (PYTHON) | Magnitude: 24.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 19, api: 10, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `data/ruby/rails/routing.rb` (RUBY) | Magnitude: 5.28 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, sec_dead_code: 5, dead_code: 4, structural_boundaries: 3
- `data/c/micropython/objtype.h` (C) | Magnitude: 23.36 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 8, pointers: 8, macros: 6, structural_boundaries: 3
- `data/c/micropython/vfs.h` (C) | Magnitude: 54.82 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 44, api: 38, macros: 29, safety: 17
- `data/c/doom/m_fixed.h` (C) | Magnitude: 19.24 | Delta: **0.496 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: macros: 6, api: 4, structural_boundaries: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `data/agc_assembly/apollo-11/AGC_BLOCK_TWO_SELF-CHECK.agc` -> Churn: **56.04%** | Cog Load: 57.0412% | Debt: 52.4559%
- `data/agc_assembly/apollo-11/ALARM_AND_ABORT.agc` -> Churn: **56.04%** | Cog Load: 59.4848% | Debt: 98.3698%
- `data/agc_assembly/apollo-11/BURN_BABY_BURN--MASTER_IGNITION_ROUTINE.agc` -> Churn: **56.04%** | Cog Load: 71.6625% | Debt: 33.2961%
- `data/agc_assembly/apollo-11/EXECUTIVE.agc` -> Churn: **56.04%** | Cog Load: 69.8101% | Debt: 68.1542%
- `data/agc_assembly/apollo-11/INTERPRETER.agc` -> Churn: **56.04%** | Cog Load: 65.8645% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `data/fortran/wrf/module_sf_noahdrv.F` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 73055.76
- `data/fortran/wrf/module_initialize_real.F` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 49921.48
- `data/fortran/wrf/module_physics_init.F` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 36210.84
- `data/livecode/core/revsaveasstandalone.livecodescript` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 32211.72
- `data/perl/exiftool/ExifTool.pm` -> **squid-protocol** (100.0% isolated ownership) | Magnitude: 26302.94

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `data/python/twisted/http.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.9045%)
- `data/python/numpy/genapi.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9728%)
- `data/python/twisted/defer.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 94.646%)
- `data/ruby/rails/base.rb` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.2972%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `data/python/fastapi/fastapi/exceptions.py` -> **Severity: 2.991** (Embedded: 0.0424 * Error Risk: 70.5405%)
- `data/python/fastapi/fastapi/types.py` -> **Severity: 2.357** (Embedded: 0.0295 * Error Risk: 80.0%)
- `data/python/fastapi/fastapi/datastructures.py` -> **Severity: 0.902** (Embedded: 0.0113 * Error Risk: 80.0%)
- `data/python/fastapi/fastapi/sse.py` -> **Severity: 0.787** (Embedded: 0.0162 * Error Risk: 48.6916%)
- `data/dockerfile/moby/builder/dockerfile/metrics.go` -> **Severity: 0.512** (Embedded: 0.0063 * Error Risk: 80.779%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `data/python/fastapi/fastapi/exceptions.py` -> **Severity: 1514.039** (Blast Radius: 15.2 * Doc Risk: 99.6078%)
- `data/python/fastapi/fastapi/responses.py` -> **Severity: 1196.656** (Blast Radius: 12.393 * Doc Risk: 96.559%)
- `data/zig/zig/Zcu.zig` -> **Severity: 1039.671** (Blast Radius: 14.253 * Doc Risk: 72.944%)
- `data/zig/zig/Type.zig` -> **Severity: 829.784** (Blast Radius: 8.552 * Doc Risk: 97.0281%)
- `data/zig/zig/InternPool.zig` -> **Severity: 785.188** (Blast Radius: 9.741 * Doc Risk: 80.6065%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
