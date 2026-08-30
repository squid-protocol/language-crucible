# assembly corpus sources

Provenance for this category is mixed. The three folders at the top predate the
issue #4 audit (squid-protocol/language-crucible#4) and are `pool-reference`: a
same-named clone was found in the `gitgalaxy/data` pool and its *current*
commit recorded, not verified as the exact snapshot copied. The folders below
them were added 2026-08-30 as a large assembly-coverage expansion, copied
directly from same-named pool clones at a known commit — `exact`, except
`raspberrypi_baremetal` whose upstream ships no license (`unknown` by design).
See the root `SOURCES.md` for the methodology and confidence levels.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `bootos` | 4 | https://github.com/nanochess/bootOS.git | `766f7011a951b29f4e9c87ff6f30f9bab03b4574` | BSD License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `cosmopolitan` | 6 | https://github.com/jart/cosmopolitan.git | `eedf7d2db6e5ee0e228862690339c166a3f003a7` | ISC License (from pool clone's LICENSE, not found locally) | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `hellosilicon` | 5 | https://github.com/below/HelloSilicon.git | `29170b7e69970e8bfb74e5f210bfe20fa2229d8a` | MIT License | Pre-existing corpus content. Provenance identified during the issue #4 audit (2026-08-28) by matching this folder's name against the `gitgalaxy/data` pool — see root `SOURCES.md` for what 'pool-reference' confidence does and doesn't guarantee. |
| `blst_generated_asm` | 14 | https://github.com/supranational/blst | `f62244ef50ad1a603decdb8f215e982d2a467bb6` | Apache License 2.0 | Machine-generated (perlasm) x86-64 field-arithmetic and SHA-256 assembly from `build/elf/`. `.cfi_*` directives, `.byte` opcode literals, huge unrolled macro expansions — GAS output no human wrote. |
| `cosmopolitan_runtime` | 17 | https://github.com/jart/cosmopolitan | `eedf7d2db6e5ee0e228862690339c166a3f003a7` | ISC License | `libc/nexgen32e/` runtime: `setjmp`/`longjmp`, `mcount`, AVX2 sort, TLS bootstrap. GAS `.S` with cpp macros, mixed 16/32/64-bit, APE polyglot idioms. |
| `cosmopolitan_syscalls` | 15 | https://github.com/jart/cosmopolitan | `eedf7d2db6e5ee0e228862690339c166a3f003a7` | ISC License | `libc/sysv/` syscall thunks — many are 2–3 lines (`.S` files that are almost pure directive), stressing func/label detection on minimal bodies. |
| `cpm65_6502` | 21 | https://github.com/davidgiven/cpm65 | `ff7f5f938607195c562e53f0a4558086aab4663a` | BSD 2-Clause License | 6502 assembly for a modern CP/M port. `zproc`/`zendproc` macros, `.label`/`.include`, `<`/`>` byte selectors, `\` line comments — a non-x86, non-ARM dialect. |
| `freebsd_kernel_arch` | 17 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD (multiple clauses) | `sys/amd64` + `sys/arm64` kernel assembly: `locore`, exception vectors, `support.S`, atomic primitives. `ENTRY`/`END` macros, `.cfi`, cross-architecture. |
| `freebsd_libc_string` | 25 | https://github.com/freebsd/freebsd-src | `c70755bc0d8f703dbaa1520c15e8213a95847dd5` | BSD (multiple clauses) | `lib/libc/amd64` — hand-tuned SIMD `memcpy`/`strcmp`/`memset`/`timingsafe_*`. Dense SSE/AVX, `.arch` directives, per-CPU dispatch. |
| `hellosilicon_aarch64` | 21 | https://github.com/below/HelloSilicon | `29170b7e69970e8bfb74e5f210bfe20fa2229d8a` | MIT License | Apple-Silicon AArch64 tutorial code: Darwin syscall ABI, `.macro`/`.endmacro`, NEON matrix math, `adrp`/`adr` addressing. Deeper than the pre-existing `hellosilicon` folder. |
| `linux_1_0_kernel` | 19 | https://github.com/kalamangga-net/linux-1.0 | `733a0282d6e855c5eee87c86733dca8c0f3e1a42` | GNU GPL v2.0 | Linux 1.0 (1994) `boot/`, `kernel/`, `zBoot/`, `FPU-emu/` assembly: 16-bit real-mode bootsector, `as86` and GAS mixed, software FPU. Historical dialect. |
| `nasm_testsuite` | 19 | https://github.com/netwide-assembler/nasm | `3cb6231581679a9ab1a8eeb0342375eb7002cebe` | BSD 2-Clause License | NASM's own `test/*.asm`: Intel syntax, `%macro`/`%rep`/`%assign` preprocessor torture, `struc`/`istruc`, every SSE/AVX/AVX-512/AMX extension, RIP-relative and absolute addressing regression cases. |
| `os_tutorial_x86` | 23 | https://github.com/cfenollosa/os-tutorial | `8002382ee56f876119f77217220b8a5034e9bac1` | BSD 3-Clause License | Numbered lessons: bootsector print routines, disk load via BIOS `int 0x13`, GDT setup, real→protected-mode switch. NASM, 16- and 32-bit in the same tree. |
| `raspberrypi_baremetal` | 16 | https://github.com/PeterLemon/RaspberryPi | `5783e31ba16353413a9248431da464e37a5619d1` | unknown | ARMv7/ARMv8 bare-metal `.asm` (`kernel7`/`kernel8` pairs, framebuffer, DMA, V3D init). Upstream ships **no license file** — kept for ARM bare-metal dialect coverage, recorded `unknown` by design (see `KNOWN_UNKNOWN` in `tools/independent_data_auditor.py`). |
| `x86_bare_metal` | 23 | https://github.com/cirosantilli/x86-bare-metal-examples | `528ab2becc4992218ca0b7e297f3e1f1674268de` | GNU GPL v3.0 | GAS-syntax (`.code16`, AT&T) bootsector examples: IDT/PIT/RTC, paging, zero-divide interrupt, BIOS teletype. Contrast to `os_tutorial_x86`'s NASM/Intel take on the same problems. |
| `xv6_x86_kernel` | 8 | https://github.com/mit-pdos/xv6-public | `eeb7b415dbcb12cc362d0783e41c3d1f44066b17` | MIT License | The complete `.S` set from MIT's teaching OS: `bootasm.S`, `entry.S`, `swtch.S`, `trapasm.S`, `usys.S`. Small, heavily commented, canonical. |

**Total: 253 files across 16 repo folder(s)** (12 exact, 3 pool-reference, 1 unknown).
