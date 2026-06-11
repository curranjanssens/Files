# Catalog of Bivalent Ligands Targeting Receptor Dimers

*Compiled June 2026. Scope: bivalent ligands (two pharmacophores joined by a defined spacer)
designed to engage a receptor **dimer or oligomer** — homodimers and heteromers. Organized by target
pair. For each series the table records the linker chemistry and **full range of lengths tested**, the
**optimum**, the **extent of testing** (in vitro / in vivo), and **potency versus the monovalent
pharmacophore(s) and/or the monomer mixture**. A dedicated section (§8) collects the
linker-length-varied series, which are the field's strongest evidence.*

**How to read the potency column.** "Fold vs monovalent" compares the bivalent to one matched
monovalent pharmacophore; "fold vs mixture" compares it to an equimolar mixture of the two separate
monomers (the more stringent test of true bivalency). Super-additivity over the *mixture* is the key
signature.

**Data-quality flags.** Entries marked ⚠ rest on paywalled full text, abstract-only data, secondary
citations, or qualitative ("increased potency") claims without published numbers; treat those numbers
as provisional. Where the literature disputes whether a compound truly bridges two protomers (vs.
binding one protomer plus a membrane/secondary pocket, or simply gaining avidity), that is flagged too.

---

## 1. Opioid receptor heteromers

| Series | Target pair | Pharmacophores (A + B) | Linker: range tested → optimum | In vitro | In vivo | Potency vs monovalent / mixture | Source |
|---|---|---|---|---|---|---|---|
| **MDAN-16…21** | MOR–DOR (μ–δ) | oxymorphone (μ agonist) + naltrindole (δ antagonist) | glycyl/oligo spacers, **16–21 atoms → 21 (MDAN-21)**; sharp **threshold ≥19 atoms** | binding in MOR/DOR-CHO; GTPγS; immunofluorescence — MDAN-21 prevents internalization (bridging evidence) | mice (tail-flick), rhesus monkey; **≥19 atoms devoid of tolerance/dependence** | MDAN-21 ~**100× more potent than morphine** (i.v.); tolerance abolished above the threshold length | Daniels *PNAS* 2005; Aceto *Int J Med Chem* 2012 — [PMC1323165](https://pmc.ncbi.nlm.nih.gov/articles/PMC1323165/), [PMC4412046](https://pmc.ncbi.nlm.nih.gov/articles/PMC4412046/) |
| **MMG10/19/20/22/24** | MOR–mGluR5 | oxymorphone (μ agonist) + M-MPEP (mGluR5 antagonist) | spacer **10–24 atoms → 22 (MMG22)**; **knife-edge** optimum | (in vivo-focused; Ki not in primary paper); later BRET "heteromer-induction" work | mice, intrathecal; LPS-inflammatory, CFA, bone-cancer, neuropathic, cisplatin pain | MMG22 i.t. **ED50 ≈ 9 fmol**; **~37,700× vs the monomer mixture**; ±1-atom homologues ~3 orders weaker | Akgün *PNAS* 2013 — [PMC3710855](https://pmc.ncbi.nlm.nih.gov/articles/PMC3710855/) |
| **MCC22** | MOR–CCR5 | oxymorphone (μ agonist) + CCR5 antagonist | PEG-type, **22 atoms** (optimum reported) | binding/functional; TM5,6 interface model | mice; inflammatory, neuropathic, cisplatin, sickle-cell, arthritis pain | **~3,500× vs monomer mixture; ~3,000× vs morphine**; no tolerance | Akgün *J Med Chem* 2015 — [PMC6745246](https://pmc.ncbi.nlm.nih.gov/articles/PMC6745246/) |
| **Le Naour cpds 1–5** | MOP–CB1 | oxymorphone (μ agonist) + rimonabant-derived CB1 antagonist | varied; **cpd 5 = 20 atoms** = optimum (only member to bridge by immunofluorescence) | HEK293 co-expressing MOP+CB1 | mice; antinociception | cpd 5 most potent; **notable negative finding — neither bivalents nor mixture produced tolerance**, so MOP–CB1 appears *not* to drive tolerance | Le Naour *J Med Chem* 2013 — [PMC3849126](https://pmc.ncbi.nlm.nih.gov/articles/PMC3849126/) |
| **KDN-21** | KOR–DOR (κ–δ) | 5′-guanidinonaltrindole (κ antagonist) + naltrindole (δ antagonist) | glycyl spacer series, **21 atoms** optimal | HEK293: δ-only, κ-only, co-expressed, mixed; binding + MAPK | mouse spinal (intrathecal) | **Ki ~0.3 nM at co-expressed δ–κ vs ~63 nM in mixed cells (~200×)** — hallmark bridging; revealed δ₁/κ₂ phenotypes | Bhushan/Xie/Portoghese *J Med Chem* 2004; *Mol Pharmacol* 2005 — [doi 10.1021/jm0342358](https://pubs.acs.org/doi/abs/10.1021/jm0342358), [Mol Pharmacol 68:1079](https://molpharm.aspetjournals.org/content/68/4/1079) |
| **KDAN-18** | KOR–DOR (κ–δ) | ICI-199,441 (κ agonist) + naltrindole (δ antagonist) | glycyl spacer, **18 atoms** optimum | binding (δ₂–κ₁ bridging) | mice, i.t.; potency **reduced in DOR-1 knockout** (genetic bridging evidence) | κ-agonist antinociception requiring intact δ–κ organization | Daniels *J Med Chem* 2005 — [PMID 15771416](https://pubmed.ncbi.nlm.nih.gov/15771416/) |
| **KMN-21** | MOR–KOR (μ–κ) | μ antagonist + κ antagonist | 21-atom spacer | HEK293 Ca²⁺ (DAMGO/U69,593) | none | selectively antagonizes μ–κ heteromer activation | Zhang *Bioorg Med Chem Lett* 2009 — [PMID 19892550](https://pubmed.ncbi.nlm.nih.gov/19892550/) |
| **MOP–CCK2 (Zheng 3a–c)** | MOR–CCK2 | oxymorphone (μ agonist) + L-365,260 (CCK2 antagonist) | diglycolic, **9–22 atoms → 18 (3b)**; 9-atom gives no association | COS BRET (induced MOP-CCK2 association); CHO binding/Ca²⁺; MOP Ki 5.7 nM, CCK2 71 nM | mice — only monovalent caused tolerance; bivalents did not | 3b **4.8× vs monovalent** functionally; tolerance-sparing | Zheng *J Med Chem* 2009 — [PMC2650857](https://pmc.ncbi.nlm.nih.gov/articles/PMC2650857/) |
| **D24M** | MOR–DOR (antagonist bivalent) | peptidic μ antagonist + δ antagonist (Tyr-Tic) | **15–41 atoms → 24** | MOR 0.85 nM, DOR 0.63 nM, ≥89× selective | mice — reduced acute/chronic morphine withdrawal | dual antagonist; withdrawal tool | review [PMC7856001](https://pmc.ncbi.nlm.nih.gov/articles/PMC7856001/) |
| **MQ-12d** | MOR–D2-like | hydromorphone (μ agonist) + DPAT (D2-like) | PEG, **18–24 atoms → 18** | β-arrestin-2 (MOR) + MAPK (D4R) | none | high-efficacy dual signaling | review [PMC7856001](https://pmc.ncbi.nlm.nih.gov/articles/PMC7856001/) |
| **MOR–A1** | MOR–adenosine A1 | μ antagonist + A1 antagonist | hetero-bivalent conjugate (length n/a) ⚠ | MOR Ki 0.7 µM, A1 0.8 µM; cAMP antagonism | reversed both μ- and A1-agonist antinociception | dual sub-µM antagonist; **no MOR–A2A bivalent exists** | Mathew *Bioorg Med Chem Lett* 2009 — [PMID 19836950](https://pubmed.ncbi.nlm.nih.gov/19836950/) |
| **MOR–CXCR4 (3 series)** | MOR–CXCR4 | naltrexone *or* oxymorphone (MOR) + **IT1t** (CXCR4 antagonist) | diglycolic/alkyldiamine, **18–22 atoms → 18**; little effect on CXCR4 binding | MOR Ki ~2–25 nM; CXCR4 affinity **lost 100–3,000×** on conjugation; 100-ns MD supports dual engagement | none for pain (one series: mice, lactic-acid writhing, **n.s.**, p=0.11) | HIV-entry series **~150× vs CXCR4 monovalent** and beat the monomer mixture under morphine; antinociception series not significant | Zhang lab (VCU): RSC Med Chem 2020, ACS Med Chem Lett 2020, Bioorg Chem 2022 — [PMC7451026](https://pmc.ncbi.nlm.nih.gov/articles/PMC7451026/), [PMID 33214847](https://pubmed.ncbi.nlm.nih.gov/33214847/), [PMC9187593](https://pmc.ncbi.nlm.nih.gov/articles/PMC9187593/) |
| **6′-GNTI** | KOR–DOR (heteromer-selective agonist; **not a tethered bivalent**) | single guanidino-naltrindole pharmacophore | n/a | KOR/DOR co-expression raises potency; G-protein-biased | spinal antinociception | ~10–40× heteromer selectivity — **contested**; also a biased KOR agonist | [PMC3411045](https://pmc.ncbi.nlm.nih.gov/articles/PMC3411045/) |

**True bivalents vs. bifunctional monomers.** A large parallel "opioid–X" literature builds dual
pharmacology into a *single overlapping pharmacophore with no spacer* — these are **bifunctional
monomers, not bivalent ligands**, and are excluded from the bridging analysis: the opioid–NK1 peptides
(NP30, TY027/TY038, SBCHM1/RCCHM6), most opioid–CCK peptides (SNF-9007 lineage), opioid–NPFF
compounds (KGFF09, BN-9), and the rimonabant–opioid and VF-13 (cannabinoid–NPFF) hybrids. They achieve
dual targeting but lack the linker-length-dependent heteromer-bridging mechanism. Separately, MOR–
galanin and DOR–CB1 are documented heteromers studied by *crosstalk/BRET*, not by tethered bivalents,
and a fentanyl–Dmt-Tic spacer series and sub-nanomolar "bivalent butorphan" morphinans appeared with
headline numbers I could not fully verify — treat those as provisional.

---

## 2. Dopamine / adenosine heteromers and homodimers

| Series | Target pair | Pharmacophores (A + B) | Linker: range → optimum | In vitro | In vivo | Potency vs monovalent / mixture | Source |
|---|---|---|---|---|---|---|---|
| **Cpd 26 "KDB1"** | A2A–D2 | A2A antagonist + D2 agonist (PPHT) | PEG-polyamide, **25–43 atoms → 43**; shorter ones bind one protomer only | Ki A2A 2.1 nM, D2 0.13 nM; BRET; **TM5-TAT peptide disruption confirms true bivalent mode** | none | ~5× per receptor vs each monovalent; the only A2A–D2 with verified simultaneous bridging | Pulido *J Med Chem* 2022 — [PMC11915710](https://pmc.ncbi.nlm.nih.gov/articles/PMC11915710/) |
| **Soriano/Franco series** | A2A–D2 | D2 agonist + A2A antagonist | Lys-PEG backbone, **26–118 atoms** | striatal membrane binding; higher affinity in co-expressing cells | none | shorter spacers enhance heteromerization; first A2A–D2 tools | Soriano *J Med Chem* 2009 — [doi 10.1021/jm900298c](https://pubs.acs.org/doi/10.1021/jm900298c) |
| **Cpds 20a/20b** | A1–D1 | xanthine (A1 antagonist) + SKF-81297 (D1 agonist) | PEG, 4–6 EG units (~48 Å) | rat-brain binding; **FRET in HEK293 confirms heterodimer** | none | 20b A1 **111× vs monovalent**; 20a 12.6× | *Acta Pharmacol Sin* 2012 — [PMC4002486](https://pmc.ncbi.nlm.nih.gov/articles/PMC4002486) |
| **Hübner D2–NTS1** | D2–NTS1 | D2 antagonist + NT(8–13) (NTS1 agonist) | PEG, **22–88 atoms**, designed for **~55 Å**; ~44–88 optimal | D2/NTS1-HEK293; **functional switch** (cAMP inhibition→stimulation only in heteromer); biphasic striatal binding | rat-brain autoradiography | **87 pM**; 76–4,700× selectivity over D2-only cells | Hübner *Nat Commun* 2016 — [PMC4963535](https://pmc.ncbi.nlm.nih.gov/articles/PMC4963535/) |
| **D3–NTSR1 (1d/2d)** | D3–NTS1 | D3 ligand + NT(8–13) | PEG, **22–88 atoms**; short favors D3 | D3/NTS1-HEK293; β-arrestin; endosomal trafficking imaging | rat-brain tissue colocalization | **4.8–6.1 pM; ~1,460× over monomers** | *Commun Biol* 2021 — [PMC8433439](https://pmc.ncbi.nlm.nih.gov/articles/PMC8433439/) |
| **5-OH-DPAT homobivalents (11d,14b)** | D2–D3 homodimer | two 5-OH-DPAT agonists | methylene, **4–14 → 9–10** (bell-shaped); matches ~13.5–22.6 Å | [³H]spiperone; GTPγS; **Hill slope 1.3–1.4 = cooperative** | none | Ki **23× vs monomer**; functional **up to 94×** | *J Med Chem* 2012 — [PMC3530844](https://pmc.ncbi.nlm.nih.gov/articles/PMC3530844/) |
| **D2 homobivalent (~92-atom)** | D2–D2 homodimer | two D2 ligands | very long, **~92 atoms** favors homodimer over D2–NTS1 | equilibrium-shift binding | none | shifts monomer/homomer/heteromer balance | *ACS Chem Biol* 2021 — [PMID 33435665](https://pubmed.ncbi.nlm.nih.gov/33435665/) |
| Clozapine / haloperidol / ropinirole / apomorphine / sumanirole homobivalents | D2 (homo) | two identical antipsychotic/agonist units | various alkyl, **~14–30 atoms**; clozapine **16–18**, Hill ~1.8–2.0 (cooperative) | [³H]spiperone; GTPγS; G-protein-biased (sumanirole >1000× bias) | none | clozapine-dimer Ki **75–79× vs clozapine**; ropinirole-dimer **20–80×** functional | multiple — [PMID 22243698](https://pubmed.ncbi.nlm.nih.gov/22243698/), [PMC7594663](https://pmc.ncbi.nlm.nih.gov/articles/PMC7594663/) |
| **Cpd 22a** | D2–mGluR5 | D2 agonist (DPAT) + mGluR5 antagonist | 20-atom "Type 3" bridging TM5–TM6 | DMR in co-expressing HEK293; modeling | none | 4–5× affinity gain in co-expressing vs single cells | *J Med Chem* 2018 — [doi 10.1021/acs.jmedchem.8b00671](https://pubs.acs.org/doi/10.1021/acs.jmedchem.8b00671) |
| A1–β2AR; A1–A3; covalent A1 homodimer | adenosine heteromers/homodimer | adenosine + salbutamol; A1+A3 agonists; A1-antagonist + sulfonyl-fluoride warhead | alkyl/PEG, length-dependent | binding + co-IP; covalent dual-site labeling | none | linker-dependent affinity; covalent dimer more A1-selective | [doi 10.1021/jm800613s](https://pubs.acs.org/doi/10.1021/jm800613s); [ChemBioChem 2024](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cbic.202400242) |

---

## 3. Serotonin receptors (mostly homodimers)

| Series | Target | Pharmacophores | Linker: range → optimum | In vitro | In vivo | Potency vs monovalent | Source |
|---|---|---|---|---|---|---|---|
| **Halazy "serotonin dimers" (4g,4j)** | 5-HT1B/1D homodimer | two 5-HT units (5-OH-linked) | piperazide spacers (atom range not fully disclosed) | human 1B/1D/1A binding; cAMP full agonists; rabbit saphenous vein | ex vivo tissue only | saphenous vein **pD2 7.6 vs 5.8 sumatriptan** (~60×); ↑1B/1D-over-1A selectivity | Halazy *J Med Chem* 1996 — [PMID 8960551](https://pubmed.ncbi.nlm.nih.gov/8960551/) |
| **Sumatriptan dimer** | 5-HT1B/1D | two sumatriptan | spacer (range not specified) ⚠ | GTPγS; saphenous vein | ex vivo | **~10× affinity** + selectivity vs monomer | [PMID 10101238](https://pubmed.ncbi.nlm.nih.gov/10101238/) |
| **LY-334370 dimer** | 5-HT1F→**1D** switch | two LY-334370 | spacer ⚠ | binding | none | dimerization **reverses subtype selectivity** to 1D (Ki ~0.3 nM) — contested/notable | review [PMC3788847](https://pmc.ncbi.nlm.nih.gov/articles/PMC3788847/) |
| **Soto 6a–6g (M100907)** ★ | 5-HT2A homodimer | two M100907 antagonists | ethylene-glycol, **5,8,11,14,17,20,23 atoms → 8–14** (bell-shaped) | h5-HT2A-CHO; ERK1/2; Ca²⁺; ≥10× selective over 2B/2C | rats, i.p., cocaine hyperlocomotion (cpd 6c effective) | **bell-shaped; but bivalent ~22× *worse* than the matched monovalent in ERK** — no avidity gain | Soto *ACS Chem Neurosci* 2017 — [PMC5862780](https://pmc.ncbi.nlm.nih.gov/articles/PMC5862780/) |
| **Russo bivalent ML10302** ★ | 5-HT4 homodimer | two ML10302 agonists | spacer, **~12–24 → 20–24 atoms** (longer than 5-HT2A) | **BRET confirms one ligand engages both protomers** (clearest direct bridging proof in the field) | none | affinity retained but **agonism lost** (functional switch) | Russo 2007 — [PMID 17676726](https://pubmed.ncbi.nlm.nih.gov/17676726/) |
| Pergolide / terguride dimers | 5-HT2A | two ergoline partial agonists | N,N′-spacers | rat tail artery | none | **negative result — reduced affinity, lost agonism** | review [PMC3788847](https://pmc.ncbi.nlm.nih.gov/articles/PMC3788847/) |

For the **5-HT1A heteromers** (5-HT1A–FGFR1, 5-HT1A–5-HT7, 5-HT1A–GalR1) there are **no genuine tethered
bivalents** — they are probed by co-administered separate ligands or by pharmacophore-merged
dual-target single molecules (not dimer-bridging). Flagged as a gap.

---

## 4. Melatonin, oxytocin, cannabinoid, and other GPCR families

| Series | Target | Pharmacophores | Linker: range → optimum | In vitro | In vivo | Potency vs monovalent | Source |
|---|---|---|---|---|---|---|---|
| **S26131** | MT1 homodimer | two agomelatine | polymethylene (length not disclosed) ⚠ | 2-[¹²⁵I]iodomelatonin binding | none | **>200× MT1 affinity** (clearest melatonin avidity gain); functional selectivity only ~20× | Audinot *Bioorg Med Chem* 2003 — [PMID 12646022](https://pubmed.ncbi.nlm.nih.gov/12646022/) |
| **N1-linked / O-linked melatonin dimers** | MT1/MT2 homo+heterodimer | two melatonin | **15–24 atoms**; N1: 16 & 24; O-linked: **20 (cpd 3c)**; "bridging" at 22–24 | binding + **BRET (~3× signal)**; O-linked 3c is cAMP-biased (arrestin-sparing) | none | modest affinity gain; value is conformational/pathway-biased probing, **not** large avidity | *Bioorg Chem* 2019 [PMID 30658234](https://pubmed.ncbi.nlm.nih.gov/30658234/); MedChemComm 2014 |
| **Pala 14a–14d** | MT1/MT2 × **H3** | melatonin-like + imidazole H3 | imidazolyl-alkyloxy, **0–3 CH₂ → hexyl (14d)** | binding + GTPγS (antagonist) | none | **~100–1,000× *lower* affinity** than optimized monovalents — deliberate dual-target compromise | *IJMS* 2014 — [PMC4200786](https://pmc.ncbi.nlm.nih.gov/articles/PMC4200786/) |
| **Busnelli OT bivalents** ★ | oxytocin receptor homodimer | two OT-peptide mimetics | alkyl diacid, **~25 Å (≈C8–C10) optimum** fitting a TMH1–TMH2 channel | Gq BRET; mutagenesis + TM-peptide interference (bridging evidence) | **mice & zebrafish** (social behavior) | **~1,000× in vitro; 40–100× in vivo** vs monovalent; mixture does not reproduce it | Busnelli *J Med Chem* 2016 — [PMID 27420737](https://pubmed.ncbi.nlm.nih.gov/27420737/) |
| **CB2 chromenopyrazole homobivalent** ★ | CB2 homodimer | two chromenopyrazole agonists | methylene, **~8–16 → 14 CH₂**; MD shows orthosteric + TM1/TM7 pocket | HEK293 Gi-cAMP + β-arrestin; MD + mutagenesis (V6.35M, A7.36M) | none | enhanced Gi + β-arrestin vs monovalent ⚠ (qualitative; no published EC50) | Morales/Jagerovic *Chem Eur J* 2020; *Pharmacol Res* 2024 — [PMID 39179054](https://pubmed.ncbi.nlm.nih.gov/39179054/) |
| **CB1 homobivalent (5d/6b)** | CB1 homodimer (disputed) | two rimonabant units | alkyl-triamine, **5–23 atoms → 15**; PEG linkers failed | binding + GTPγS (bivalent > monovalent) but **Ca²⁺ assay shows no gain** | mice, tail-flick (antagonize CP55,940) | only **~4× vs monovalent**; authors call it "modest" — **bridging contested** | *J Med Chem* 2010 — [PMC3076737](https://pmc.ncbi.nlm.nih.gov/articles/PMC3076737/) |
| **CB1–OX1 (cpd 20)** | CB1–orexin-1 heterodimer | rimonabant + almorexant | alkyl, length-varied ⚠ | potency jumps in co-expressing vs single-expressing cells (heteromer signature) | none | "robust" coexpression-dependent gain ⚠ (no published fold) | *ACS Med Chem Lett* 2014 — [PMID 24944734](https://pubmed.ncbi.nlm.nih.gov/24944734/) |
| **Muscarinic dualsteric (Mohr/Holzgrabe); methoctramine** | M2 (M1/M3) | orthosteric tropane + allosteric phthalimide; or tetraamine | hexamethonium-type / polymethylene | binding; M2 selectivity; first antagonist bitopic proof | methoctramine: cardiac M2 selectivity | subtype-selective; bitopic mechanism | [PMID 25051097](https://pubmed.ncbi.nlm.nih.gov/25051097/); [PMID 2909747](https://pubmed.ncbi.nlm.nih.gov/2909747/) |
| **MAM03055A** | σ2/TMEM97 (putative homodimer) | two CM571 units | thiourea (atom count not disclosed) ⚠ | σ2 Ki 55.9 nM (~60× over σ1); **pseudo-irreversible**; depletes σ2 protein | none | monomer is reversible/non-depleting — bivalent gains a distinct mechanism | [PMC8736263](https://pmc.ncbi.nlm.nih.gov/articles/PMC8736263/) |
| **NPY UR-MK177/188** | Y1/Y4 | two argininamide (BIBP3226/BIBO3304) antagonists | **31–41 atoms** | Y1/Y4 Ki 130–290 nM; Y4 Kb 20 nM; Y4 no stereo-discrimination | none | **selectivity *lost* vs monovalent** (1:1 Y1/Y4 vs >10:1) — a cautionary case | *Bioorg Med Chem* 2013 — [PMID 24074877](https://pubmed.ncbi.nlm.nih.gov/24074877/) |
| **Somatostatin SST2 / GRPR oligoproline** | SST2 / GRPR homodimers | two agonist motifs on rigid (Pro-Gly)ₙ | **rigid 10/20/30 Å → 20 Å**; 10 Å too short to dimerize | internalization; dimer-induction; Gq-biased | imaging potential | rigid-scaffold distance control; 20 Å optimum for uptake | *PNAS* 2021 — [PMC8640787](https://pmc.ncbi.nlm.nih.gov/articles/PMC8640787/) |
| **Melanocortin MC4R (CJL-1-87)** | MC4R homodimer | two Ac-His-DPhe-Arg-Trp | PEDG20 (**20 atoms**), (Pro-Gly)₆ (36) | binding **6–23× gain**; cAMP 3–5× gain | **mice i.c.v. — ~50% feeding reduction** at 5 nmol (first MC bivalent in vivo) | binding ≫ functional gain | [PMC5679017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5679017/) |
| **Histamine H2 dimers** | H2R homodimer (putative) | two hetarylpropylguanidine agonists | alkyl, **C3–C12 → C12** | hH2R binding; gpH2R atrium | none | cpd 63 (C12) **pEC50 8.56 ≈ 250× histamine potency** | *ACS Omega* 2018 — [PMC6130797](https://pmc.ncbi.nlm.nih.gov/articles/PMC6130797/) |

Documented heteromers **without** a genuine tethered bivalent: MT1–GPR50, MT2–5HT2C (agomelatine is an
untethered dual ligand), CB1–A2A and CB1–D2 (probed by ligand mixtures), galanin, mGluR (obligate
dimers engaged allosterically, not by orthosteric bridging).

---

## 5. Non-GPCR cell-surface receptor dimers

| Series | Target | Pharmacophores | Linker: range → optimum | In vitro | In vivo | Potency vs monovalent | Source |
|---|---|---|---|---|---|---|---|
| **RGD multimers** (E[c(RGDyK)]₂ → tetramer/octamer; 3G3-, 3PEG4-dimers) | integrin αvβ3 (clustered) | 2–8 cyclic-RGD units | Glu-dendritic, Gly₃ (24 bonds), **PEG₄ (38 bonds ≈ 13 Å)**; too-long EG₆ is detrimental | U87MG binding: monomer 329 nM → dimer 64 nM → tetramer 26 nM | tumor xenograft PET/SPECT — dimer best uptake-vs-clearance balance | **~5× (dimer), ~8× (trimer), ~12–13× (tetramer)** vs monomer; avidity/clustering | [PMC2795072](https://pmc.ncbi.nlm.nih.gov/articles/PMC2795072/), [PMC8005094](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005094/) |
| **S961; Ins-AC-S2; H2C dimers** | insulin receptor (homodimer; site 1 + site 2) | site-1 peptide + site-2 peptide | peptide; H2C series **6 aa > 9 aa** | IC50 2.4–7.4 nM (HEK293-hIR) | blocks IR signaling in vivo | **~100× over the site-1 monovalent**; order determines antagonist vs agonist | Menting *Nat Commun* 2013 — [PMC3531387](https://pmc.ncbi.nlm.nih.gov/articles/PMC3531387/) |
| **TrkA 1-ss series** | TrkA (NGF receptor) homodimer | two D3 peptidomimetic agonists | triazine/alkyl, **short ~15 Å ≪ medium ≪ long** | TrkA binding Kd ~105 nM; freezes inactive conformation | blocks NGF-dependent activation | **~100× over monovalent D3** (~10 µM → ~105 nM); agonist→antagonist by dimerizing | *Growth Factors* 2010 — [PMC2943489](https://pmc.ncbi.nlm.nih.gov/articles/PMC2943489/) |
| **Xli-093 series** | GABA-A α5 (benzodiazepine site) | two imidazobenzodiazepines | **(CH₂)₃ (linear) optimum**; (CH₂)₅ weaker; **ether linker folds → no binding** | α5 Ki 0.49 nM, >100× subtype-selective | mice — cognition enhancement | linker **conformation** (linear vs folded) is decisive | Atack 2012 — [PMC3703926](https://pmc.ncbi.nlm.nih.gov/articles/PMC3703926/) |
| **OHT bivalent series** | estrogen receptor (nuclear) homodimer | two 4-hydroxytamoxifen | oligo-EG, **7–47 Å; two maxima ~14.4 Å & ~28.8 Å** (intramolecular vs intermolecular) | RBA two-peak profile | MCF-7 growth inhibition (more potent than OHT monomer) | OHT-bivalent ≫ DES-bivalent (agonist scaffold fails) | Katzenellenbogen *ACS Chem Biol* 2013 — [PMC3631453](https://pmc.ncbi.nlm.nih.gov/articles/PMC3631453/) |
| **TLR2/1 & TLR2/6 lipopeptides** (Pam₃Cys, Pam₂Cys, mini-UPam) | TLR2 heterodimers | acylated lipopeptide(s) | acyl-chain count + PEG₃ tail | NF-κB; cytokine assays | adjuvant use | acylation/linker set TLR1- vs TLR6-selectivity (receptor heterodimerization is ligand-induced, **not** tethered bivalency) | Jin *Immunity* 2009; [PMC11610712](https://pmc.ncbi.nlm.nih.gov/articles/PMC11610712/) |
| **bis-quaternary** (hexamethonium C6, decamethonium C10, tubocurarine) | nicotinic AChR (subunit-interface pair) | two quaternary ammonium heads | polymethylene, **C6 ganglionic vs C10 neuromuscular** | competitive antagonism | classic neuromuscular/ganglionic blockers | chain length sets tissue selectivity (classic bivalent pharmacology) | [PMC4110698](https://pmc.ncbi.nlm.nih.gov/articles/PMC4110698/) |
| **AMPA dimer-interface PAMs** (CMPDA/CMPDB; HJC0122/24; bis-pyrimidines) | AMPA (GluA2) LBD-dimer interface | two PAM arms on a symmetric core | rigid p-phenylene / p-dioxyphenylene | patch-clamp; PDB 3RN8/3RNN; bis-pyrimidine +170% at 1 nM | HJC0122: rat neuroapoptosis model | bis-pyrimidine ~**10⁶× more concentration-efficient** than monovalent cyclothiazide | *Mol Pharmacol* 2011 [PMC3141890](https://pmc.ncbi.nlm.nih.gov/articles/PMC3141890/); MedChemComm 2019 [PMC6837176](https://pmc.ncbi.nlm.nih.gov/articles/PMC6837176/) |

**Important "not a bivalent" flags.** NMDA GluN1/GluN2B **ifenprodil/traxoprodil** are single-site
interface NAMs, not tethered bivalents; no genuine bivalent NMDA ligand exists. AMPA **cyclothiazide/
ampakines** and **philanthotoxins** are likewise single-site modulators / pore blockers, not bivalents
(the genuine AMPA bivalents target the allosteric dimer interface, never the orthosteric glutamate
site — and **no orthosteric bivalent AMPA/kainate ligand exists**). **Glycine receptor/gephyrin** is a
protein–protein scaffold, not a small-molecule bivalent. **RXR** heterodimer selectivity is driven by
monovalent rexinoids allosterically, not by tethering. **Trastuzumab** (anti-HER2) is a bivalent
antibody, not a small molecule.

---

## 6. Therapeutic testing depth — at a glance

Most dimer-targeting bivalents never leave the test tube. The ones with **in vivo** data:

- **Opioid analgesics (rodent, several models):** MDAN-21 (also rhesus monkey), the MMG series,
  MCC22, Le Naour MOP–CB1, CB1 homobivalents, MOR–CXCR4 (writhing, non-significant). MDAN-21, MMG22 and
  MCC22 are the standouts — extraordinary potency and tolerance-sparing.
- **Oxytocin bivalents:** mice and zebrafish social behavior (40–100× in vivo gain).
- **Melanocortin MC4R (CJL-1-87):** mouse i.c.v., ~50% feeding reduction.
- **5-HT2A bivalent 6c:** rat cocaine-hyperlocomotion.
- **GABA-A Xli-093:** mouse cognition.
- **RGD multimers:** extensive tumor-xenograft imaging (their actual purpose).
- **TrkA / insulin-receptor antagonists:** cell-based, with in vivo signaling readouts.

**No classical dimer-targeting bivalent ligand has entered clinical trials.** The translational
barriers are the same ones in the main survey: molecular weight typically >700–1000 Da, "beyond
rule-of-5" space, poor oral PK and blood-brain-barrier penetration.

---

## 7. When the potency gain is real vs. an artifact

A potency optimum at one spacer length is suggestive but **not proof** of two-protomer bridging. The
discriminators the literature actually trusts:

1. **Super-additivity over the monomer mixture** (not just over a single monovalent). MMG22 (~37,700×)
   and MCC22 (~3,500×) are the strongest cases.
2. **A sharp length optimum matching the modelled inter-protomer distance** (MMG22's knife-edge at 22
   atoms; D2–NTS1 at ~55 Å; oxytocin at ~25 Å).
3. **Dependence on co-expression of both partners** (D2–NTS1 functional switch; CB1–OX1; A1–D1 FRET).
4. **Direct biophysical evidence** — BRET that one ligand occupies both protomers (5-HT4/ML10302), the
   TM5-TAT peptide-disruption test (A2A–D2 KDB1), internalization block (MDAN-21).

Counter-signals that argue **against** simple bridging, all documented here: the CB1 homobivalent's
gain vanishes in the Ca²⁺ assay and is only ~4×; the 5-HT2A bivalent is *worse* than its monovalent in
ERK; NPY bivalents *lose* selectivity; pergolide/terguride and huprine homodimers are flat-out weaker
than monomers. Glass and colleagues' critique — that cannabinoid bivalents may be too short to span two
orthosteric sites and that lengthening the linker may not help because the ligands enter via the
membrane — applies to several of these systems. In several cases (CB2, oxytocin) the "second site" is
explicitly **not** the partner's orthosteric pocket but a membrane-facing TM1/TM7 pocket or an
inter-protomer channel, so "bivalent" does not always mean "two orthosteric sites bridged."

---

## 8. Linker-length-varied series (the core evidence)

These are the series where multiple spacer lengths were synthesized and compared — the data you most
wanted. Two response shapes recur: a **sharp threshold** (activity switches on above a length) and a
**bell/knife-edge optimum** (a single best length, with sharp falloff either side).

| Series | Target | Linker chemistry | Lengths compared | Optimum | Shape | Behaviour off-optimum |
|---|---|---|---|---|---|---|
| **MMG10–24** | MOR–mGluR5 | alkyl/glycol | 10, 19, 20, 22, 24 atoms | **22** | knife-edge | ±1 atom ≈ 3 orders of magnitude weaker |
| **MDAN-16–21** | MOR–DOR | glycyl | 16, 17, 18, 19, 20, 21 atoms | **≥19** | threshold | tolerance/dependence appears below 19 |
| **5-OH-DPAT homobivalents** | D2–D3 | methylene | 2–14 units | **9–10** | bell | 12-unit drops back to 2-unit affinity |
| **5-HT2A 6a–6g** | 5-HT2A | ethylene glycol | 5, 8, 11, 14, 17, 20, 23 atoms | **8–14** | bell | 20–23 atoms ~10× weaker binding |
| **Russo ML10302** | 5-HT4 | spacer arms | ~12–24 atoms | **20–24** | optimum | shorter loses dual-protomer BRET |
| **A2A–D2 (KDB1)** | A2A–D2 | PEG-polyamide | 25, 35, 43 atoms | **43** | threshold | <43 atoms bind one protomer only |
| **MOP–CCK2 (Zheng)** | MOR–CCK2 | diglycolic | 9, 16, 18, 22 atoms | **18** | threshold | 9 atoms gives no receptor association |
| **D2–NTS1 (Hübner)** | D2–NTS1 | PEG | 22–88 atoms | **~44–88 (≈55 Å)** | optimum | too short cannot span the modelled 55 Å |
| **CB2 chromenopyrazole** | CB2 | methylene | ~8–16 CH₂ | **14 CH₂** | optimum (MD) | 10–12 CH₂ don't span both sites |
| **CB1 rimonabant homobivalent** | CB1 | alkyl-triamine | 5, 7, 11, 15, 19, 23 atoms | **15** | bell (modest) | gain only ~4×, absent in Ca²⁺ |
| **Oxytocin (Busnelli)** | OTR | alkyl diacid | length series | **~25 Å (C8–C10)** | sharp | off-length loses the ~1000× boost |
| **Histamine H2 dimers** | H2R | alkyl | C3, C8, C10, C12 | **C12** | monotonic↑ | shorter chains less potent |
| **GABA-A Xli** | α5 BzR | alkyl vs ether | (CH₂)₃, (CH₂)₅, ether | **(CH₂)₃ linear** | conformation | ether linker folds → no binding |
| **Estrogen-receptor OHT** | ER | oligo-EG | 7–47 Å | **~14.4 & ~28.8 Å** | two maxima | intramolecular vs intermolecular modes |
| **RGD multimers** | αvβ3 | Glu/Gly₃/PEG₄ | 6–38 bonds + valency 2–8 | **PEG₄ dimer (~38 bonds)** | optimum + valency | EG₆ detrimental; octamer no better than tetramer |
| **D2 homobivalent** | D2–D2 | very long | up to ~92 atoms | **~92** | special | long spacer needed to favour homodimer |

**Take-aways.**
- **No universal optimum.** Opioid heteromers cluster at ~19–22 atoms; A2A–D2 needs 43; D2–NTS1 needs
  ~55 Å; D2 homodimer favours ~92; AMPA/ER/integrin use rigid cores instead. The optimum is dictated by
  each dimer's interface geometry and the pharmacophore attachment vectors.
- **Rigidity and composition matter as much as length.** Flexible PEG/alkyl usually wins, but ether
  oxygens can fold a GABA-A linker into inactivity, and rigid oligoproline/phenylene cores are used
  precisely to *fix* a distance (somatostatin/GRPR, AMPA, ER).
- **Bell-shape/threshold is the signature.** A monotonic length–activity relationship (e.g. histamine
  H2) is weaker evidence of true bridging than a sharp optimum matching a modelled inter-protomer
  distance (MMG22, oxytocin, D2–NTS1).
- **Dimerization frequently does *not* help.** 5-HT2A, NPY, pergolide, huprine, and the CB1
  homobivalent all show flat or negative results — a useful corrective to the assumption that tethering
  two pharmacophores must improve potency.
