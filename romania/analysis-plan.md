# Romanian Education System — Analysis Plan

**Output format:** Policy brief / report
**Scope:** Dropout-centered, with pipeline view into universities and the tech industry
**Date drafted:** 2026-05-27
**Owner:** Mihai Gociu

---

## 1. Framing and Central Question

Romania's education system displays a stark paradox that any honest analysis must confront head-on:

- **The failure**: One of the highest rates of early school leaving (părăsire timpurie a școlii / abandon școlar) in the EU — consistently above the EU-27 average, with rural areas, Roma communities, and vocational tracks bearing the brunt. Functional illiteracy on PISA is near or above 40%.
- **The success**: A globally recognised pipeline of STEM talent. Top *colegii naționale* (Tudor Vianu, Mihai Viteazul, Gheorghe Lazăr, Emil Racoviță, Internat C. Negruzzi etc.), strong Olympiad performance in math/physics/informatics, and universities (Politehnica București, UTCN Cluj, UBB, "Al. I. Cuza" Iași) whose graduates populate Google, Microsoft, Amazon, UiPath, Bitdefender, and Romania's >7% GDP IT sector.

**Central research question:**
> *Why does the same national system simultaneously produce mass educational failure and globally competitive technical elites — and what does that two-track reality mean for policy?*

**Sub-questions:**
1. What are the **direct and structural drivers** of abandon școlar in Romania?
2. Where in the pipeline (preșcolar → primar → gimnazial → liceal → universitar) does the system **lose the most students**, and who are they?
3. What **mechanisms** (family, school, geography, curriculum, governance, financing) produce the elite STEM track?
4. To what extent is the elite track **dependent on or compensating for** the failures of the mass system (private tutoring / *meditații*, parental capital, self-selection)?
5. What is the **economic and social cost** of the current equilibrium, and what reforms have been tried / are credibly on the table?

---

## 2. Methodology

A **mixed-methods desk review**, structured as follows:

| Layer | Method | Purpose |
|---|---|---|
| Quantitative | Time-series and cross-country comparison of indicators (dropout, PISA, enrolment, financing, teacher-pupil ratios) | Establish the size and shape of the problem |
| Comparative | Benchmark Romania vs. EU-27, vs. peer post-communist states (PL, HU, BG, CZ), and vs. EU leaders (FI, EE) | Distinguish "post-communist legacy" from "Romanian specificity" |
| Qualitative | Synthesis of NGO field reports, Court of Auditors reviews, academic literature, journalism | Capture mechanisms and lived experience that numbers hide |
| Case study | 3–5 deep-dives (see §5.7) | Test causal hypotheses against concrete settings |
| Policy review | Map of reforms 2011 (Legea 1/2011) → *România Educată* → Legile Deca (2023) | Distinguish announced reforms from implemented ones |

**Analytical lenses** to apply across each workstream:
- **Equity lens** (urban/rural, income, ethnicity, disability, gender)
- **Geographic lens** (județ-level disparities; the București / Cluj / Iași / Timișoara cluster vs. the rest)
- **Institutional lens** (governance, financing per capita, ARACIP/ARACIS quality assurance)
- **Pipeline lens** (where students are lost vs. where they accelerate)

### 2.1 Tooling and Reproducibility

All quantitative work is done in Python, in the project virtual environment at `./.venv`, so that every chart and table in the brief can be regenerated from raw sources.

- **Data wrangling**: `pandas` for tabular data (Eurostat, INS, MoE, OECD downloads); `pyjstat` or `eurostat` package for Eurostat JSON-stat pulls; `requests` for ad-hoc downloads.
- **Numerical / stats**: `numpy`, `scipy.stats` for trend tests, confidence intervals on rates.
- **Charts**: `matplotlib` for the static charts in the brief; `seaborn` where it improves readability (heatmaps, distribution plots). Map visualisations (județ-level choropleths) via `geopandas` + `matplotlib`, using SIRUTA / NUTS-3 shapefiles.
- **Notebooks**: `jupyter` for exploratory work; final charts produced by versioned `.py` scripts so the data annex is reproducible.
- **Project layout** (to set up alongside this plan):
  ```
  romania/
    analysis-plan.md
    data/
      raw/        # untouched downloads, named with source + date
      processed/  # cleaned, analysis-ready
    notebooks/    # exploration
    scripts/      # final chart-producing scripts
    figures/      # output PNG/SVG used in the brief
  ```
- **Dependencies** pinned in `requirements.txt` at the project root once the first scripts land.
- **Python version**: Python 3.12.8 (Homebrew), in `./.venv`. Comfortably ahead of current pinning floors for `pandas`, `geopandas`, `scipy`, `matplotlib`.

---

## 3. Indicators to Track (Minimum Set)

Quantitative spine of the report. Each should be reported as **latest value + 10-year trend + EU comparison + intra-Romania disaggregation** where possible.

**Access & retention**
- Early leavers from education and training, 18–24 (Eurostat `edat_lfse_14`)
- NEET rate, 15–24 and 15–29 (Eurostat)
- Net enrolment rate by ISCED level (UNESCO UIS, INS)
- Preschool participation, ages 3–6 (Eurostat `educ_uoe_enra10`)

**Achievement**
- PISA mean scores (reading, math, science) and % below Level 2 ("functional illiteracy") — OECD PISA 2018, 2022, and the upcoming 2025 cycle
- TIMSS / PIRLS results where Romania participates
- Bacalaureat pass rate, national and by județ (Ministerul Educației / Edupedu)
- *Evaluare Națională* (cls. VIII) score distribution

**System inputs**
- Public expenditure on education as % of GDP (Eurostat, World Bank) — Romania has been below the legal 6% target for ~15 years
- Spending per pupil, PPP-adjusted
- Teacher salaries relative to GDP per capita and to OECD average (OECD *Education at a Glance*)
- Pupil-teacher ratio by level
- Share of schools with adequate sanitary facilities (a Romania-specific scandal — many rural schools still have outdoor toilets)

**Pipeline / outcomes**
- Tertiary attainment 25–34 (Eurostat) — Romania is among the EU's lowest
- Share of STEM graduates
- Share of ICT specialists in workforce (Eurostat `isoc_sks_itspt`)
- Emigration of recent graduates (brain drain proxies)

---

## 4. Named Data Sources

Concrete sources, grouped by type. Where a URL is not stable, the institution + dataset name is given.

### 4.1 Romanian official
- **Raportul QX (David, mai 2025)** — *Raport de diagnostic al educației și cercetării din România. Realizări prezente și implicații pentru noi reforme în domeniu*, by Prof. Daniel David in his capacity as Minister of Education and Research (Dec 2024 – May 2025). Local copy: `romania/Daniel_David_Raport_QX.pdf`. **Treat as the spine for the diagnosis chapter and the reforms map** — it is the most recent ministerial-level synthesis, written by a serious academic, and explicitly integrates WB / EC / OECD / UNESCO / UNICEF findings. Note David's analytical move: he treats *fragmentation* of the CDI and HE systems not as the problem but as a *cause* of the performance problem — a useful lens for our §5.2.
- **INS — Institutul Național de Statistică**: *Tempo Online* database; annual *Sistemul educațional din România* yearbook.
- **Ministerul Educației**: *Raport privind starea învățământului preuniversitar / universitar* (annual).
- **ARACIP** (preuniv.) and **ARACIS** (universitar) — quality assurance evaluation reports.
- **Edupedu.ro** — single best Romanian-language journalism on education data; aggregates Bac and Evaluare Națională results.
- **Court of Accounts (Curtea de Conturi)** — audit reports on education spending and infrastructure programs (e.g. *România Educată*, PNRR education components).
- **Camera Deputaților / Senat** — texts of Legea Educației Naționale 1/2011 and the 2023 *Legile Deca* (Legea învățământului preuniversitar 198/2023 + Legea învățământului superior 199/2023).
- **Administrația Prezidențială** — *România Educată* strategic project documents (2016–2021).

### 4.2 International / comparative
- **Eurostat** — education domain (`educ_*`, `edat_*`, `trng_*`).
- **OECD** — PISA reports, *Education at a Glance*, *Education Policy Outlook: Romania*.
- **OECD (2025), *Education and Skills in Romania* — Reviews of National Policies for Education** — 238 pages, DOI [10.1787/594cbb5d-en](https://doi.org/10.1787/594cbb5d-en). Local copy: `romania/OECD_2025_Education_Skills_Romania.pdf`. Structured summary: `romania/sources/oecd-2025-summary.md`. **The second diagnostic spine alongside QX.** Organises everything under three pillars (Quality / Equity / Governance) applied at every level (ECEC / school / tertiary / skills) and offers 9 numbered policy messages with named OECD-country exemplars (Chile, Scotland, Ontario, Portugal, Norway, Austria, Germany, Ireland, Spain, France, UK). Strongest single source on the urban-rural divide and on Roma exclusion — areas where QX is thin.
- **UNESCO Institute for Statistics (UIS)**.
- **World Bank** — *Romania Systematic Country Diagnostic*; education public expenditure reviews; the SABER framework reports.
- **European Commission** — annual *Education and Training Monitor: Romania* (the single most useful one-stop annual diagnostic).
- **UNICEF Romania** — reports on out-of-school children, Roma inclusion, early childhood.

### 4.3 NGOs and think tanks
- **Salvați Copiii România** — *Abandonul școlar* annual reports; school-meal program evaluations.
- **World Vision Romania** — *Bunăstarea copilului din mediul rural* (longitudinal). Local copies: `romania/WVR_2024_rural_welfare.pdf` and `romania/WVR_2024_invatamant_simultan.pdf` (simultaneous-classroom evaluation — the basis for the rural case study in §5.7).
- **BRIO / AVE România — Iliescu & Iancu (2025), *Alfabetizarea numerică în România***. Local copy: `romania/BRIO_2025_alfabetizare_numerica.pdf` (86 pages). **The source of QX's 25%/36%/46% functional-illiteracy pyramid.** Also reports rural-urban split: **58% rural vs 22% major-urban** numeric illiteracy — this is the equivalent of the OECD's rural-urban PISA gap measured against the Romanian curriculum rather than PISA.
- **Fundația Roma Education Fund**.
- **Centrul de Evaluare și Analize Educaționale (CEAE)**.
- **Asociația Vatra** / **Teach for Romania** — operational data on teacher placement in disadvantaged schools.
- **Expert Forum (EFOR)** — governance and PNRR monitoring.

### 4.4 Industry & pipeline (success-side data)
- **ANIS** (Asociația Patronală a Industriei de Software și Servicii) — IT sector reports.
- **Brainspotting / eJobs / BestJobs** — IT salary and demand reports.
- **ARIES Transilvania** — Cluj tech ecosystem data.
- University career-office reports from **UPB, UTCN, UBB, UAIC**.
- **IUF / IOI / IMO / IPhO** national team results — proxy for elite STEM pipeline.

### 4.5 Academic literature
- Search **Web of Science / Scopus / Google Scholar** for: `"early school leaving" Romania`, `"abandon școlar"`, `"Roma education" Romania`, `"rural education" Romania`, `"functional illiteracy" Romania`.
- Romanian Journal of Sociology, Sociologie Românească, Revista de Pedagogie.

---

## 5. Workstreams (Report Structure)

Each workstream maps to a chapter of the final brief.

### 5.1 The Shape of the Failure — Sizing Abandon Școlar
- Definition reconciliation: EU "early leavers" (18–24, no upper-sec, not in training) vs. Romanian MoE "abandon școlar" (annual leaving within a cycle). These produce very different numbers; the report must explicitly disambiguate.
- 15–20 year trend, EU comparison, intra-Romania (urban vs. rural, by județ, by ethnicity where data allow).
- Who drops out, when, and why they say they do (qualitative).
- **Headline data point** (OECD 2025): share of PISA students below Level 2 has been **flat since 2006** in all three domains. The single most powerful "nothing has worked" finding — lead with it.
- **Headline data point** (QX): functional-illiteracy pyramid 25% primar → 36% gimnaziu → **46% liceu** — the system *worsens* literacy as students progress.

### 5.2 Root Causes — A Layered Diagnosis
Organised from proximate to structural:
1. **Household-level**: poverty, seasonal agricultural work, early marriage (esp. in some Roma communities), parental migration abroad ("copiii lăsați acasă" / *euro-orphans*), domestic responsibilities for girls.
2. **Roma-specific** (new sub-layer added after OECD review): segregation (~50% of Roma 6-15 in majority-Roma schools per FRA 2021), pre-existing exclusion compounding through every cycle, school-mediator programme as partial intervention since 2001. **OECD 2025 is the primary source here**; QX treats this only obliquely.
3. **Demand-side barriers** (OECD framing): financial costs, administrative complexity of admissions, information/awareness gap (only ~33% of parents understand the concept of early education).
4. **School-level**: distance and transport, dilapidated infrastructure (the outdoor-toilets scandal as symptom), teacher absenteeism, lack of remedial support, bullying.
5. **Curricular**: overloaded, encyclopaedic curriculum poorly matched to slow learners; high-stakes Evaluare Națională as a filtering rather than diagnostic instrument.
6. **System-level**: chronic underfinancing (<6% GDP); the regressive funding tilt within education (tertiary ~2x ECEC, ~3x primary per student — OECD 2025); per-capita financing formula that penalises small rural schools; weak vocational track (post-2009 dismantling of *școlile de arte și meserii*); uneven inspectorate capacity.
7. **Political economy**: 30+ ministers in 35 years; reform whiplash; capture of textbook market; politicised inspectorate appointments; PISA share-below-Level-2 stable since 2006 *despite* the whiplash.

### 5.3 Geography of Inequality
- Heat-map of dropout and Bac-pass rates by județ.
- The "two Romanias" thesis: a București–Cluj–Timișoara–Iași belt vs. the south/east (Teleorman, Călărași, Vaslui, Botoșani).
- Case of *liceul comasat / desființat* — closure of village schools and its second-order effects.
- **Lead statistic** (OECD 2025): **Romania has the largest rural-urban PISA math gap of any country in PISA** — 119 points before SES controls. Gap disappears after SES controls → confirms it is *poverty geography*, not geography per se.
- Other defining numbers: 27.5% rural vs 3.3% urban early leaving; 60% vs 90% upper-sec completion; 45% population rural but only 24% tertiary enrolment from rural areas and only 10% of nurseries.

### 5.4 The Other Track — How the Elite System Works
- Profile of the top 20 *colegii naționale* by Bac and Olympiad results.
- The role of **admission filtering** (Evaluare Națională cutoffs) in concentrating high-capital students.
- The shadow education system: ***meditațiile*** (private tutoring). Estimated household spend, normalisation, and its role as a *de facto* parallel system that those who can pay use to compensate for the public system's weaknesses.
- The Olympiad infrastructure: centres of excellence, summer camps, the role of specific teachers and informal mentor networks.
- Why informatics in particular: heritage of strong math tradition + low capital requirements + clear international benchmarks (IOI) + IT industry pull from the late 1990s onward.

### 5.5 From Top Liceu to Big Tech — The Pipeline Working
- Funnel: top liceu → UPB/UTCN/UBB CS or *Automatică* → internship in multinational or startup → senior role / emigration.
- Quantify (where possible): number of CS graduates/year; share entering IT; share emigrating within 5 years.
- The role of multinational R&D centres opening in Romania from ~2005 (Microsoft, Oracle, IBM, Amazon, Continental, Bosch) and of homegrown successes (UiPath, Bitdefender, eMAG, FintechOS).
- The dependency question: does the success story require a small, self-selected elite — meaning scaling it would change its nature?

### 5.6 Higher Education — Strengths, Sores, and Stagnation
- The polytechnic strength (UPB, UTCN) vs. the chronic weakness of social sciences and humanities at most institutions.
- Diploma mills and the post-2000 expansion of private universities; ARACIS evaluation history.
- The plagiarism crises (Ponta, Oprea, etc.) and what they reveal about doctoral oversight.
- Brain drain: medical doctors and engineers; remittance flows; recent partial return.

### 5.7 Case Studies (3–5, to be selected)
Suggested mix:
- **One success**: e.g. *Colegiul Național de Informatică "Tudor Vianu"* — what is reproducible, what isn't.
- **One systemic intervention**: the *Masă caldă în școli* (hot meal) pilot — evidence on attendance and dropout impact.
- **One failure mode**: a rural commune where the gymnasium closed; track student outcomes.
- **One Roma-focused programme**: e.g. school mediators, *A doua șansă*.
- **One industry-pipeline organisation**: e.g. *Asociația Techsoup* / *Școala Informală de IT* / *Bursele Merito*.

### 5.8 Reforms — What's Been Tried
Chronological map:
- 1995 Legea 84
- 2011 Legea 1/2011 (Funeriu) — landmark, partially implemented
- 2016–2021 *România Educată* — strategic vision, weak follow-through
- 2020–2026 PNRR education component — €3.6bn, focus on infrastructure, digitalisation, and dropout reduction (PROGRES, *Programul Național de Reducere a Abandonului Școlar*)
- 2023 *Legile Deca* (198/2023 and 199/2023) — current framework
- Dec 2024 – May 2025 David ministry — short-term measures under fiscal constraint, plus the **Raportul QX** diagnosis-and-reform package for the medium/long term (see §4.1)
- Bacalaureat reform pending; Evaluare Națională under revision
- For each: what was promised, what was implemented, what the evidence says about results.

### 5.9 Recommendations

Structured under the **OECD 2025 three-pillar taxonomy** (Quality / Equity / Governance) for international legibility, then tiered by horizon and political cost within each pillar.

Tiered by horizon and political cost:
- **Quick wins (12 months, low cost)**: universal hot meals; transport vouchers; expand *A doua șansă*; mandatory diagnostic literacy assessment in grade 2.
- **Medium-term (2–5 years)**: dual vocational track expansion with industry co-investment (use the 29 PNRR campuses as integrated hubs); teacher salary reform + housing for rural placements; per-school financing floor; curriculum slimming.
- **Structural (5–10 years)**: depoliticised inspectorate; serious early childhood (preșcolar) expansion in disadvantaged areas; Bac and Evaluare Națională redesigned as diagnostic not gatekeeping; sustained 6% GDP financing (and where it should go).

**Open debates to surface explicitly in the brief** (where QX and OECD diverge):
- *More money* vs *better allocation*: QX wants overall budget to 6% GDP; OECD argues for **reallocation from tertiary toward ECEC and primary** within the current envelope. Both can be true; the brief should pick a position.
- *Compliance QA* vs *enhancement QA*: QX wants ARACIP modelled on ARACIS (stronger compliance teeth); OECD wants a shift toward enhancement and institutional capacity building.
- *Teacher reform lever*: QX prioritises salary + career structure + new licensing exam; OECD prioritises pedagogical leadership + mentorship + collaboration. Complementary but emphasis differs.

**International benchmarks** to anchor recommendations (from OECD 2025): Chile (school leadership professionalisation), Scotland (Collaborative Improvement among local authorities), Ontario (peer collaboration), Portugal (regional network planning), Norway (adaptive QA), Austria/Germany (dual VET ecosystems), Ireland/Spain (mature-student tertiary admissions), France (*1000 premiers jours*), UK (Sure Start).

Each recommendation tagged with: estimated cost, lead agency, evidence base, political feasibility, and *whose view it follows* (QX, OECD, brief's own).

---

## 6. Deliverables

1. **Executive summary** (2 pages) — for ministerial / journalist / donor audience.
2. **Full policy brief** (~40–60 pages) — workstreams 5.1–5.9.
3. **Data annex** — all charts and tables reproducible from named sources, with CSVs.
4. **One-pager visuals** — the dropout heat-map, the pipeline funnel, the financing-vs-EU chart.

---

## 7. Timeline (Indicative — 12 Weeks)

| Week | Focus |
|---|---|
| 1 | Source acquisition; finalise indicator list; set up data folder |
| 2–3 | Quantitative spine: pull Eurostat / INS / PISA, build core charts |
| 4–5 | Workstream 5.1–5.3 (failure side) |
| 6–7 | Workstream 5.4–5.6 (success side and HE) |
| 8 | Case studies (5.7) — desk research + 3–5 expert interviews if feasible |
| 9 | Workstream 5.8 — reforms review |
| 10 | Workstream 5.9 — recommendations |
| 11 | Internal review; revise |
| 12 | Final formatting, executive summary, visuals |

---

## 8. Risks, Caveats, Biases to Pre-Empt

- **Definition drift**: "abandon școlar" in Romanian media often conflates annual dropout with EU early-leaver rate. Be explicit each time.
- **Data lag**: INS and MoE data run 1–2 years behind; PISA every 3 years. Note vintage of each figure.
- **Selection bias on the success side**: Olympiad and big-tech narratives over-sample București/Cluj. Resist generalising.
- **Roma data**: ethnicity is self-declared and under-reported; estimates from NGOs (REF, UNICEF) often diverge from INS. Triangulate, don't pick one.
- **Survivorship bias in interviews**: people who succeeded in the system are easier to reach than those who dropped out. Budget effort for the latter.
- **Reform-cycle fatigue**: every minister announces "the reform". Distinguish announced from legislated from implemented from evaluated.
- **Author's perspective**: declare it. If you are writing as someone who succeeded *through* the elite track, name the standpoint.

---

## 9. Open Questions to Resolve Before Drafting

- [ ] Will this brief have a named publisher / sponsor, or is it independent?
- [ ] Audience priority: Romanian policymakers, EU institutions, the public, or the diaspora?
- [ ] Are expert interviews in scope (adds 2–3 weeks but transforms case studies)?
- [ ] Romanian, English, or bilingual?
- [ ] Is there appetite for a public-facing summary (op-ed / Substack) alongside the brief?
