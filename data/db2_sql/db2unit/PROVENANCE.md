# IBM DB2 SQL / SQL PL

Source: https://github.com/angoca/db2unit — **GPL-3.0**, noted explicitly: the
corpus otherwise skews permissive, though it already carries GPL-2 material
(linux, doom). Included as an aggregation of unmodified third-party test
material; each file retains its own licence and header.

A unit-testing framework written in DB2 SQL PL: `CREATE PROCEDURE`/`FUNCTION`
bodies, `DECLARE`/`SET`, condition handlers, and `--#SET TERMINATOR @` on line 1
— which is exactly db2_sql's `internal_discriminator`, so these files exercise
the `.sql` collision with sqlite (gitgalaxy#2511) in the db2 direction. The
corpus previously had only sqlite-side `.sql` files.
