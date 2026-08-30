# embedded_python corpus sources

New category, seeded 2026-08-30. GitGalaxy's `embedded_python` standard is
separate from `python`: extensions `.py` / `.mpy`, exact-match `boot.py`,
shebangs `micropython` / `mpy-cross`, and rules keyed on the MicroPython /
CircuitPython surface — `import machine`, `UART` / `I2C` / `SPI` / `WLAN` /
`RTC` / `ADC`, `@micropython.native` / `viper`, `alloc_emergency_exception_buf`,
`_thread`, `uasyncio`, `utime` / `ujson` / `ustruct`, and (RP2-specific)
`@rp2.asm_pio` PIO assembly.

| Repo folder | Files | Upstream | Commit | License | Notes |
|---|---|---|---|---|---|
| `meow_turtle` | 14 | none (original content) | n/a | unknown / unspecified | Original embedded firmware from the repo owner's personal LEGO-sorter project ("Ninelives"). RP2040 / RP2350 MicroPython: `boot.py` + dual-core `_thread` event loop, `machine.WDT` / `Pin` / `ADC`, I²C sensor drivers (`mpu6050`, `tsl2591`), BLDC / vibration motor drivers, an OTA updater, and `pio_programs.py` — **PIO assembly embedded in Python via `@rp2.asm_pio` decorators**, a second language living inside function bodies that never execute as Python. Contributed directly, not cloned — no upstream repo, no license file. Recorded `unknown` by design, not oversight (see `KNOWN_UNKNOWN` in `tools/independent_data_auditor.py`). Do not treat as safe to redistribute. |

**Total: 14 files across 1 repo folder** (1 unknown).
