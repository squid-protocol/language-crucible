# HLASM — IBM High Level Assembler

Sources:
* `che4z_hlasm/` — https://github.com/eclipse-che4z/che-che4z-lsp-for-hlasm (EPL-2.0).
  Test fixtures from Eclipse's HLASM language server: real macro, CSECT,
  conditional-assembly and copybook source.
* `zopeneditor_sample/` — https://github.com/IBM/zopeneditor-sample (Apache-2.0).
  `ASAM1.asm` (a CICS-era assembler program) and `ASMCOPY/REGISTRS.asm`.

**`REGISTRS.asm` is gitgalaxy#3110's reproduction case**: a 19-line register-equate
copybook (`R0 EQU 0` … `R15 EQU 15`) that carries none of hlasm's
internal_discriminator tokens, so ecosystem gravity classifies it `assembly`.
It is included deliberately — before this corpus existed, that bug was invisible
to every gate.
