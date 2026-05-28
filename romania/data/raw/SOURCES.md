# Data sources

Each raw file is paired with an entry here documenting its provenance.

## `pisa_2022_math_low_top.csv`

**What:** Share of PISA 2022 students in mathematics at the bottom (below Level 2, "low achievers") and top (Level 5 or 6, "top performers") for selected European/CEE countries and the OECD average.

**Source:** OECD (2025), *Education and Skills in Romania* (Reviews of National Policies for Education), Figure 1.1 panels A. Underlying data: OECD PISA 2022 Database. The same numbers appear in the OECD PISA 2022 Country Note for Romania for the Romania row.

**Cross-check:** Romania row (49% / 4%) matches the PISA 2022 Country Note for Romania ("49% of low performers in mathematics", "4% top performers in mathematics").

**Vintage:** PISA 2022, published December 2023.

**Notes:**
- "Low achievers" = below proficiency Level 2 in math (score < 420.07).
- "Top performers" = Level 5 or 6 in math (score ≥ 606.99).
- The OECD report rounds figures to whole percentage points in this panel.
- Countries are ordered as in the OECD figure (ascending low-achiever share).

## `brio_2025_illiteracy_by_cycle_environment.csv`

**What:** Share of Romanian students classified as functionally numerically illiterate (BRIO categories D+E) by school cycle and environment of origin. Cycles: Primar (grades 1-4), Gimnaziu (grades 5-8), Liceu (grades 9-12). Environments: Rural, Urban mic, Metropolitan, Urban mare, plus the national Total.

**Source:** Iliescu, D. & Iancu, D. (2025), *Alfabetizarea numerică în România: Raport național pentru clasele I-XII*, BRIO / Asociația pentru Valori în Educație. Local copy: `romania/BRIO_2025_alfabetizare_numerica.pdf`. Specifically Tables 12 and 25 (pages 38 and 47 of the report).

**Vintage:** Published February 2025. Normative sample n=9,719 students across grades 1-12.

**Notes:**
- "Functional illiteracy" = BRIO category D + E (the bottom two of five score bands A-E).
- The Total row matches QX's "25/36/46% pyramid" (rounded).
- The Rural row's liceu value (72.56%) is the headline finding — nearly 3 in 4 rural high-school students are functionally numerically illiterate.
- "Urban mare" = cities with population >200,000; "Metropolitan" = surrounding metro areas; "Urban mic" = smaller towns; "Rural" = rural localities.
