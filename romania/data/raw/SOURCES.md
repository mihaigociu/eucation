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

## `eurostat_2024_ict_specialists_share.csv`

**What:** Share of ICT specialists in total employment, EU-27 member states, 2024. Includes the EU-27 average as a separate row tagged `is_eu=EU_AVG`.

**Source:** Eurostat (dataset `isoc_sks_itspt`), via the Statistics Explained accompanying file *ICT specialists in employment* (ICT05_2025.xlsx), Figure 1. Article: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=ICT_specialists_in_employment

**Cross-check:** EU news release 2025-07-08 (https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250708-2) cites the same headline figures (Romania 2.8%, EU 5.0%, Sweden 8.6% top, Greece 2.5% bottom).

**Vintage:** 2024 reference year, published July 2025.

**Notes:**
- ICT specialist = ISCO classification of workers whose main job is the development, operation or maintenance of ICT systems (broader than just developers).
- Spain and France use slightly different definitions per the source metadata.
- Non-EU countries (CH, NO, IS, RS, BA, TR) are excluded from this CSV — the EU-27 comparison is the analytically clean cut.

## `eurostat_2023_early_leavers_urbanisation.csv`

**What:** Share of 18-24 year olds who are early leavers from education and training (left school without completing upper secondary and not currently in education), broken down by degree of urbanisation, 2023. EU-27 member states with data + EU-27 average. Includes the rural-cities gap in percentage points.

**Source:** Eurostat dataset `edat_lfse_30`, dimensions: `unit=PC, wstatus=POP, sex=T, age=Y18-24, deg_urb in (DEG1, DEG3)`. Downloaded via SDMX TSV from https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/edat_lfse_30/?format=TSV

**Vintage:** 2023 reference year (most recent fully-reported cycle as of the OECD 2025 report).

**Notes:**
- `DEG1` = Cities; `DEG3` = Rural areas; `DEG2` (towns/suburbs) excluded from this CSV for clarity but available in the raw TSV.
- Romania's gap (24.2 pp) is the largest in the EU by ~10 pp; Bulgaria is second at 14.6 pp.
- Some countries (NL, IE, SI, BE, IT, DE, CZ, AT) have *negative* gaps — rural rates are lower than city rates. Mostly reflects urban concentration of disadvantaged migrant populations in those countries.
- `wstatus=POP` (denominator = full population) is the headline early-leaver indicator. `EMP` and `NEMP` are alternative slices.
- Romania's headline values (3.3% cities, 27.5% rural) exactly match the OECD 2025 *Education and Skills in Romania* report.

## `imo_medals_population.csv`

**What:** All-time cumulative IMO medal counts (gold, silver, bronze, total) for the top 23 countries (by gold-medal count) plus current population in millions, to compute per-capita medal rates.

**Sources:**
- Medal counts: Wikipedia, *List of countries by medal count at International Mathematical Olympiad* (https://en.wikipedia.org/wiki/List_of_countries_by_medal_count_at_International_Mathematical_Olympiad), accessed 2026-05. Wikipedia in turn sources from the official IMO results at https://www.imo-official.org. Defunct teams (USSR, East Germany, Czechoslovakia, Yugoslavia, CIS) are listed separately on Wikipedia; here only currently-competing successor states are included.
- Population: approximate mid-2024 figures from public sources (UN Population Division order of magnitude). Used only as a normaliser — small variations have no effect on per-capita ranking among top performers.

**Notes:**
- IMO ran from 1959 onward (Romania hosted the first). 65 editions through 2024.
- The Romania row reflects the *current Romanian team* — does not include Romania's 1959-1989 communist-era performance separately; those years are folded in.
- Top per-capita performers in this list: Singapore, Bulgaria, Hungary, Romania, Israel — all small countries that punch far above their weight. Big countries naturally cannot lead per-capita.
- Per-capita figure should not be quoted without context: it normalises against current population, not 65-year average population.
