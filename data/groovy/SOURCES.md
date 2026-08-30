# groovy corpus sources

Provenance is mixed. The two folders at the top (`gradle`, `spock`) predate the
issue #4 audit and are `pool-reference` — and they contain only `.java`
(Groovy-*adjacent* code: Spock's AST-transform implementation, Gradle's Java API
that the Groovy DSL wraps), not a single file the `groovy` standard would
actually classify. The 14 folders below them were added 2026-08-30 and are real
Groovy — `.groovy` sources, `.gradle` build scripts, a `Jenkinsfile` — copied
directly from same-named pool clones at a known commit, so `exact`.

GitGalaxy's `groovy` standard covers `.groovy/.gradle/.gvy/.gy/.gsh` +
`Jenkinsfile`; the folders below spread across its major dialects: the Gradle
build DSL (closure-as-configuration), Gradle plugin authoring (`@CompileStatic`
typed Groovy), Spock specs (`given:/when:/then:/where:` label blocks + power
asserts + data tables), and the Jenkins view builder-DSL (undefined-method
dynamic dispatch). See the root `SOURCES.md` for methodology and confidence
levels.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `gradle` | 4 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Pre-existing. `.java` only (`DefaultProject`, `DefaultTask` — the API the Groovy DSL configures). Provenance by pool name-match during the issue #4 audit; see root `SOURCES.md`. |
| `spock` | 5 | https://github.com/spockframework/spock | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` | Apache License 2.0 | Pre-existing. `.java` only (`SpockTransform`, `SpecRewriter` — the compile-time AST transform). Provenance by pool name-match during the issue #4 audit; see root `SOURCES.md`. |
| `gradle_dsl_snippets` | 26 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Curated `.gradle` build scripts from the docs snippet corpus, one per topic (java-library, publishing, plugins, native, code-quality…). `plugins { id '…' }`, `dependencies {}`, `tasks.named(…) {}`, extension blocks — closure-as-configuration, no explicit types. |
| `gradle_buildlogic_groovy` | 25 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Gradle's own convention plugins in Groovy (`build-logic/`): `@CompileStatic`, `abstract class X extends DefaultTask`, `@TaskAction`, `@Input`/`@OutputFile`. Statically-compiled Groovy, the opposite end from the DSL scripts. |
| `gradle_integtest_specs` | 31 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Spock functional tests: `class … extends AbstractIntegrationSpec`, `buildFile <<`, `succeeds`/`fails`, `def "feature name"()`, `where:` blocks driving parameterised runs. |
| `gradle_sample_task_classes` | 21 | https://github.com/gradle/gradle | `db62c2f2b404217cb6a7eef2598c6e84ab08fa27` | Apache License 2.0 | Small custom `Task`/`Plugin` classes from the docs snippets: `class GreetingTask extends DefaultTask`, `@TaskAction def greet()`, GString interpolation, `project.property(…)`. |
| `spock_specs` | 31 | https://github.com/spockframework/spock | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` | Apache License 2.0 | The Spock framework's own spec suite: `extends Specification`, `def "…"()` feature methods, `given:/when:/then:/expect:/cleanup:/where:` labels, power-assert expressions, data tables `a | b || c`, `Mock()`/`Stub()`/`Spy()`, `@Unroll`. |
| `spock_core_groovy` | 18 | https://github.com/spockframework/spock | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` | Apache License 2.0 | Spock's runtime implemented in Groovy: metaclass work, `@groovy.transform.*`, closure/AST helpers. |
| `spock_smoke_specs` | 25 | https://github.com/spockframework/spock | `b71e3d7590dae28d608aa92f90b45bef33aaeda8` | Apache License 2.0 | Minimal one-behaviour specs each targeting a single language edge (array initializers, closures in `where:`, `@NotYetImplemented`) — dense feature-method-per-file. |
| `spring_boot_gradle` | 29 | https://github.com/spring-projects/spring-boot | `5cecd3922fce651f13d16a85d8a29efaa7f44cfd` | Apache License 2.0 | Spring Boot's multi-module `build.gradle` conventions: `plugins { id 'org.springframework.boot.*' }`, `optional` / `dependencyManagement`, `tasks.withType(…)`. |
| `flutter_android_gradle` | 25 | https://github.com/flutter/flutter | `75910740753c13a858bb39c3686afb71675e8dc4` | BSD 3-Clause License | Auto-generated Android `build.gradle`/`settings.gradle`: `allprojects {}`, `subprojects {}`, `dependencyLocking {}`, `rootProject.layout.buildDirectory`, `evaluationDependsOn(':app')`. |
| `kotlin_build_gradle` | 25 | https://github.com/JetBrains/kotlin | `bcdc78880f23dd07f10607332e8a89a5e72d4e9a` | Apache License 2.0 | Groovy build scripts for the Kotlin monorepo: `buildscript {}`, `apply plugin:`, `ext {}` property bags, conditional configuration. |
| `godot_android_gradle` | 10 | https://github.com/godotengine/godot | `4a919adccf8e398aceca75399c539078c54fe97f` | MIT License | Godot's Android platform Gradle: shared `config.gradle` property files, `android {}` blocks, `publish-module.gradle` script plugins applied via `apply from:`. |
| `retrofit_gradle` | 15 | https://github.com/square/retrofit | `77e6ba21d9ba372d1b23ef29881912910da23347` | Apache License 2.0 | A small library's per-module `build.gradle`: `apply plugin:`, `dependencies { api / implementation }`, `tasks.named('jar')`, a BOM module. |
| `jenkins_view_groovy` | 30 | https://github.com/jenkinsci/jenkins | `bc6a2222ce5a9e104a4f5a96653f0e879461936b` | MIT License | Jenkins Groovy **view scripts** (the Jelly alternative): builder-DSL markup where undefined method calls (`f.entry`, `l.layout`, `t.summary`) are dynamic dispatch into a `GroovyObject` builder, plus `namespace(…)` and `_(…)` i18n. Includes a declarative `Jenkinsfile`. |
| `fineract_gradle_plugin` | 9 | https://github.com/apache/fineract | `e6e5a4b6eec5a33d327546c640e6b7f281b5ae42` | Apache License 2.0 | A full Gradle plugin authored in Groovy: `class FineractPlugin implements Plugin<Project>`, extension objects, nested service classes, `project.tasks.register(…)`. |

**Total: 329 files across 16 repo folder(s)** (14 exact, 2 pool-reference).
