# Bivalent Ligands: A Survey of Design, Mechanism, Targets, and Translation

*A research survey compiled June 2026. Every substantive claim is cited inline; sources are
peer-reviewed primary literature and reviews unless otherwise noted. Where the field is
genuinely unsettled, the disagreement is flagged rather than smoothed over.*

---

## 1. Scope and definition

A **bivalent ligand** is a single molecule that contains **two discrete pharmacophores joined
by a spacer (linker)**, designed so that the two pharmacophores can engage two binding sites —
classically the two protomers of a receptor dimer — at the same time. When the two pharmacophores
are identical the molecule is **homobivalent**; when they differ it is **heterobivalent**.[^huang2021]

The title premise of this survey — cataloguing *every* bivalent ligand ever made — is not literally
achievable: the class spans four decades and thousands of compounds across opioid, dopamine,
serotonin, adenosine, cannabinoid, chemokine, oxytocin, and many other targets, plus adjacent
modalities (PROTACs, SMAC mimetics, multivalent glycoconjugates). What follows is instead a
structured map of the field: the founding ideas, the canonical compounds, the contested mechanism,
the adjacent modalities, and the reasons so few classical bivalents have reached patients.

A closely related but **mechanistically distinct** class is the **bitopic (dualsteric) ligand**, which
links an **orthosteric** and an **allosteric** pharmacophore on a **single** receptor protomer — versus a
bivalent ligand, which links two orthosteric pharmacophores to **bridge two** protomers.[^kamal2009]
The distinction matters for the rest of this document and is a frequent source of confusion.

---

## 2. Origin and the message–address concept

Bivalent ligands aimed at opioid receptors were **first introduced by Philip S. Portoghese in 1982**,
using a 6-amino derivative of naltrexone (naltrexamine) joined by polyethylene-glycol linkers of
varying length; the seminal paper presented evidence for simultaneous occupation of proximal
recognition sites.[^portoghese1982][^stoddart2021] In Portoghese's original framework the two
pharmacophores were joined by a "connecting chain" or "spanner," terminology that later became
"linker."[^stoddart2021]

Portoghese (1931–) was a medicinal chemist at the University of Minnesota and Editor-in-Chief of
the *Journal of Medicinal Chemistry* from 1972 to 2012; he designed several selective opioid
antagonists still used as research tools, including β-funaltrexamine, naltrindole, norbinaltorphimine,
and naltriben.[^portoghese_bio]

His design logic borrowed Schwyzer's **"message–address" concept**, originally describing the
recognition elements of peptide hormones: the **"message"** is the pharmacophore that binds the
orthosteric site, and the **"address"** is a recognition unit that confers subtype selectivity.[^portoghese1989]
Antagonist selectivity could be tuned predictably by simulating part of the peptide address with a
rigid nonpeptide moiety — the approach that produced the κ-selective **norbinaltorphimine** (two
naltrexone-derived units fused through a pyrrole ring) and the δ-selective **naltrindole**.[^portoghese1989][^stoddart2021]

---

## 3. Design principles

### 3.1 Pharmacophore selection
Ideal monomeric leads bind the target selectively with low-nanomolar potency, carry a
functionalizable attachment point for the spacer, and have low-to-medium molecular weight
(~300–400 Da) so the assembled bivalent does not become impossibly large.[^huang2021]

### 3.2 Spacer length — target-specific, not universal
The single most important — and most misunderstood — design variable is spacer length. There is
**no universal optimal length**; it is set by the geometry of the particular two-site target.

- In the original 1986 opioid series, both mu-agonist (oxymorphamine-based) and mu-antagonist
  (naltrexamine-based) activity peaked at a four-glycyl-unit spacer, kappa antagonism peaked at the
  *shortest* spacer, and delta selectivity rose with increasing length.[^portoghese1986]
- For **opioid-type heteromers**, optimal spacers cluster around **~18–22 atoms** (e.g., MDAN-21 at
  21 atoms / ~25 Å; MMG22 at 22 atoms; a MOP–CB1 bivalent at 20 atoms).[^aceto2012][^akgun2013][^lenaour2013]
- Other geometries demand far longer spacers: ~55 Å for a D2R–NTS1R heterodimer, **43 atoms** for an
  A2A–D2 heterobivalent, and **~92 atoms** for a D2 homodimer-fostering ligand.[^huang2021][^pulido2022][^d2homo]

So the often-quoted "~18–22 atoms" figure is **specific to opioid-type heteromers** and should not be
generalized.

### 3.3 Spacer composition and rigidity
The most common spacer chemistries are **polyethylene-glycol repeats and peptidic chains**;
methylene units and 1,2,3-triazole-containing linkers are also widely used, the latter growing
popular because copper-catalyzed azide–alkyne "click" chemistry assembles them efficiently.[^huang2021]
**Constrained or rigid spacers usually reduce affinity and potency, whereas flexible spacers let each
pharmacophore find a favorable pose.**[^huang2021]

---

## 4. Mechanism and the avidity question

### 4.1 Why two tethered pharmacophores can bind better than one
Once the first pharmacophore binds, the tethered second pharmacophore is held at high **effective
local concentration** near its site, so it binds and rebinds far more readily than a free molecule
would. Heterodivalent avidity is modeled as *K*<sub>div</sub> = *K*<sub>A</sub> · *K*<sub>B</sub> · *C*<sub>eff</sub>,
where the effective molarity *C*<sub>eff</sub> is set by linker statistics; the optimal linker is the one
whose most-probable end-to-end distance matches the inter-site spacing.[^kane2010] The linker's
thermodynamic contribution is **essentially entropic** — calorimetry shows negligible enthalpic
linker–protein interaction — though the precise weight of conformational-entropy loss has been
contested.[^krishnamurthy2007][^kane2010]

Avidity also **prolongs target residence time**: while one pharmacophore stays bound, the other is
forced to remain nearby and rebind, so dissociation slows.[^vauquelin2013] The magnitude can be
dramatic — model bivalent systems reach low-picomolar *K*<sub>d</sub> (3–40 pM) where the monovalent
analogue binds at ~16 nM,[^krishnamurthy2011] linked nanobodies gained up to 27-fold apparent
affinity for CXCR4,[^vauquelin2013] and polyvalent sialic-acid inhibitors were reported ~10⁹-fold
more potent than monovalent.[^kane2010] Effective molarity is lowest when the linker is too short to
span the sites without strain, highest near optimal, and falls only weakly past optimal — which is
why choosing a flexible linker **somewhat longer** than the inter-site distance is a defensible
strategy.[^krishnamurthy2007]

### 4.2 The unresolved question: does the potency gain actually come from bridging?
This is the central open controversy of the field. Pharmacological enhancement is well established,
but it does **not by itself prove** that both orthosteric sites are simultaneously occupied. The gain
could instead arise from one receptor being bound while the second pharmacophore is "parked" in the
membrane or a secondary pocket, raising its local concentration without true bridging.

- Direct structural proof of two-protomer occupancy is scarce; evidence "has relied mainly on
  pharmacological data," prompting attempts at immunocytochemical corroboration in mu–delta opioid
  heteromers.[^yekkirala2013]
- **Contrary view:** Glass and colleagues argue that cannabinoid bivalent ligands are likely too
  short to reach both CB1 protomers, and — critically — that simply lengthening the linker may not
  help, because CB1 ligands enter through the lipid bilayer and a linker is unlikely to exit the
  receptor's external face to reach the partner.[^glass2016]
- **Alternative geometries:** in some designs the second pharmacophore is proposed to engage a
  **membrane-oriented pocket between TM1 and TM7** of the partner protomer, or to thread an
  inter-protomer "channel," rather than the partner's orthosteric site.[^oxytocin2016][^cb2_2024]

Because GPCR dimers are largely **constitutive (pre-formed)**, bivalent ligands are in most cases
expected to **stabilize pre-existing dimers** rather than induce dimerization.[^berque2008] Dimer
pharmacology is commonly modeled with **cooperativity across the dimer** (binding at one protomer
alters affinity at the other); negative cooperativity is well documented, e.g. for the EGF receptor
dimer.[^cooperativity]

The rationale for targeting heteromers at all is that they have **distinct biochemistry** from their
constituent monomers — altered ligand recognition, G-protein coupling, trafficking, and the
possibility of heteromer-selective biased agonism — making them, in effect, novel drug targets.[^ferre2022]

---

## 5. Canonical compounds by target class

### 5.1 Opioid receptors (the founding class)
- **MDAN-21** — an oxymorphone-derived mu-agonist linked to a naltrindole-related delta-antagonist
  by a 21-atom (~25.4 Å) spacer.[^aceto2012] Across the MDAN-16…21 series, **tolerance and dependence
  were a function of spacer length**: shorter spacers gave morphine-like tolerance, while spacers of
  **≥19 atoms were essentially devoid of tolerance and dependence** in mice, implicating a physical
  mu–delta heteromer interaction.[^daniels2005] MDAN-21 was ~50-fold more potent than morphine
  intravenously and still reached the CNS despite its size.[^daniels2005][^huang2021]
- **KDN-21** — a kappa/delta antagonist bivalent that provided evidence for spinal δ–κ opioid
  heterodimers.[^kdn21]
- **6′-Guanidinonaltrindole (6′-GNTI)** — a naltrindole derivative whose potency improved on
  KOR/DOR co-expression, consistent with heteromer activity (though its heteromer-selectivity is
  contested, and it is also a G-protein-biased KOR agonist).[^gnti]
- **Biphalin** — a homodimer of two enkephalin units, regarded as a foundational bivalent opioid
  ligand acting through message–address interactions.[^biphalin]

### 5.2 Opioid × non-opioid heteromers
- **MMG22** — a mu-opioid agonist joined to the mGluR5 antagonist M-MPEP by a 22-atom spacer. Its
  intrathecal ED₅₀ in inflammatory-pain mice was ~9 fmol/mouse and it was **~48,000× more potent than
  a mixture of the two monovalent ligands**, with the 22-atom optimum supporting a putative MOR–mGluR5
  heteromer; it also reduces neuropathic and chemotherapy-induced pain without classic opioid side
  effects.[^akgun2013][^mmg22_neuro]
- **MOP–CB1 bivalents** — combining a mu-opioid agonist with a CB1 antagonist; the 20-atom member
  was the most potent antinociceptive and the series produced no tolerance.[^lenaour2013]
- **MOR–CXCR4 bivalent** — a dual antagonist designed against putative MOR–CXCR4 dimers implicated
  in opioid-enhanced HIV-1 entry.[^morcxcr4]

### 5.3 Dopamine receptors
- **Homobivalent D2 ligands** with a ~92-atom spacer can foster D2 homodimerization while reducing
  D2–NTSR1 interaction, shifting the monomer/homomer/heteromer equilibrium.[^d2homo]
- **D1–D2 heteromer** signaling (Gq/11-coupled, calcium) requires agonist at both receptors;
  SKF83959 acts as a heteromer-selective agonist.[^d1d2]
- **D3R–NTSR1 bivalents** bind with picomolar affinity and high selectivity over the monomers and
  promote endosomal trafficking of the heterodimer — relevant to addiction and neuropsychiatric
  disease.[^d3nts1][^d3nts1_apps]

### 5.4 Adenosine receptors
- **A2A–D2 heterobivalent ("KDB1", compound 26)** — an A2A antagonist linked to a D2 antagonist by
  a 43-atom spacer (2.1 nM at A2A, 0.13 nM at D2), used as a tool to detect A2A–D2 heteromers central
  to the adenosine–dopamine antagonism in striatopallidal neurons (a Parkinson's target).[^pulido2022][^a2a_d2_tool]
- **A1–D1 heterobivalents** have also been designed and evaluated.[^a1d1]

### 5.5 Serotonin, cannabinoid, chemokine, oxytocin
- **Serotonin "dimers"** were used to design potent, selective 5-HT1B/1D agonists; one dimerized
  5-HT1B agonist crossed the blood–brain barrier despite high molecular weight.[^serotonin][^huang2021]
- **CB2 homobivalent** (two chromenopyrazoles + 14 methylenes) bridges one orthosteric site and one
  TM1/TM7 membrane pocket, enhancing Gi signaling and β-arrestin recruitment.[^cb2_2024]
- **DV1-dimer / CXCR4 bivalents** probe CXCR4 dimerization and inhibit HIV-1 entry.[^cxcr4]
- **Oxytocin-receptor bivalents** were proposed to bind via an inter-protomer "channel-like"
  structure rather than two orthosteric sites — one of the clearest cases of an alternative binding
  geometry.[^oxytocin2016]

### 5.6 Non-GPCR bivalent small molecules
- **Bivalent kinase inhibitors (Type V / bisubstrate)** tether an ATP-competitive moiety to a ligand
  binding outside the ATP cleft, gaining selectivity and avidity against the highly homologous kinase
  ATP sites.[^kinase]
- **Bivalent BET inhibitor MT1** (two JQ1-derived warheads) is >100-fold more potent in cells than
  monovalent JQ1 and outperformed it in mouse leukemia models — an **occupancy-driven** bivalent,
  distinct from event-driven degraders.[^mt1]
- **Bivalent SMAC mimetics** (two AVPI-like motifs) are 2–3 orders of magnitude more potent than
  monovalent in inducing apoptosis; **birinapant (TL32711)** and **APG-1387** reached clinical trials,
  though birinapant's HBV program was terminated for adverse effects.[^smac][^birinapant]
- **Bivalent/"palindromic" amyloid ligands** cross-link fibrils by binding two surfaces at once.[^amyloid]

---

## 6. Adjacent modality: PROTACs and induced-proximity degraders

PROTACs share the bivalent architecture (two binding moieties + a linker) but differ **fundamentally**
in pharmacology, and are worth distinguishing carefully.

A **PROTAC (PROteolysis-TArgeting Chimera)** links a ligand for the target protein to a ligand that
recruits an **E3 ubiquitin ligase**; forming the ternary complex (E3 : PROTAC : target) drives target
polyubiquitination and proteasomal degradation.[^protac_def] Crucially this is **event-driven and
catalytic** — one PROTAC can degrade many target copies and is then released — versus the
**occupancy-driven** pharmacology of classical bivalent ligands, which must stay bound to act.[^protac_event][^protac_age]
The two most-used E3 ligases are **cereblon (CRBN)** and **von Hippel-Lindau (VHL)**.[^crbn_vhl]

Milestones:
- **First PROTAC** — Sakamoto, Crews & Deshaies, *PNAS* 2001, targeting MetAP-2 via ovalicin linked to a
  phosphopeptide.[^sakamoto2001]
- **First all-small-molecule PROTAC** — Schneekloth et al., 2008 (nutlin-based E3 recruiter,
  androgen-receptor warhead).[^schneekloth2008]
- **dBET1 / ARV-825** (2015) — BET-degrading PROTACs; ARV-825's ~1 nM DC₅₀ vs dBET1's ~430 nM
  illustrated how strongly linker length governs potency.[^dbet]
- **ARV-110 (bavdegalutamide, AR)** and **ARV-471 (vepdegestrant, ER)** were among the first PROTACs in
  human trials.[^arvinas]
- **Vepdegestrant (VEPPANU)** became the **first FDA-approved PROTAC**, approved **May 1, 2026** for
  ER-positive, HER2-negative, *ESR1*-mutated advanced/metastatic breast cancer, supported by the
  Phase 3 VERITAC-2 trial (median PFS 5.0 vs 2.1 months for fulvestrant in the *ESR1*-mutant
  population).[^fda_veppanu][^veritac2]

**Molecular glues** (e.g., the thalidomide analogue lenalidomide, which redirects CRBN to neosubstrates
IKZF1/IKZF3) achieve the same degradation outcome but are **monovalent** — no linker, no two-warhead
architecture.[^glues][^lenalidomide] Other induced-proximity bifunctionals include **LYTACs**
(lysosome-targeting, Bertozzi lab, *Nature* 2020) and **AUTACs** (autophagy-targeting, Arimoto group,
2019).[^lytac][^autac] Among biologics, **bispecific antibodies** are the conceptual parallel —
**catumaxomab** (EMA 2009, later withdrawn) and **blinatumomab** (FDA 2014, CD19×CD3) being the
landmark approvals.[^bsab_cat][^blina]

---

## 7. Therapeutic applications, advantages, and challenges

### 7.1 Where bivalency helps
- **Analgesia with reduced liabilities** — the MDAN/MMG series suggest heteromer-targeted opioids can
  separate analgesia from tolerance and dependence.[^daniels2005][^akgun2013]
- **Selectivity and avidity** — heteromer- or clustered-target-selective binding, picomolar affinities,
  the "cluster glycoside effect" in multivalent glycoconjugates.[^d3nts1][^cluster]
- **Hard targets** — kinase selectivity via bivalency, apoptosis induction via bivalent SMAC mimetics,
  fibril cross-linking for amyloid.[^kinase][^smac][^amyloid]
- **Approved multivalent class** — **trivalent GalNAc–siRNA conjugates** (three clustered GalNAc ligands
  binding the hepatocyte ASGPR) are the clearest clinically successful multivalent design, underlying
  givosiran, lumasiran, **inclisiran**, and vutrisiran.[^galnac]

### 7.2 Why so few classical bivalents reach the clinic
- **Size / molecular weight** — bivalent GPCR ligands are commonly **>700 Da and often >1000 Da**,
  placing them in **"beyond rule of 5" (bRo5)** chemical space.[^huang2021][^bro5]
- **ADME and bioavailability** — large size undermines oral absorption and metabolic stability; these
  are the primary translational barriers.[^huang2021]
- **Blood–brain barrier** — bivalents are generally not expected to cross the BBB, a serious limit for
  CNS targets — **though not absolute**: MDAN-21 and a dimerized 5-HT1B agonist both reached the CNS,
  apparently via active transport, so BBB penetration is not reliably predictable from size alone.[^huang2021]
- **Bottom line on classical bivalents:** per a 2021 review, **no classical small-molecule bivalent GPCR
  ligand had entered clinical trials** — the clinic-reaching bivalent/multivalent classes are the
  distinct paradigms of PROTACs, bivalent SMAC mimetics, and GalNAc–siRNA conjugates.[^huang2021]

### 7.3 Future directions
- **Bitopic molecules** retain bivalency-like benefits at lower molecular weight by pairing orthosteric
  and allosteric pharmacophores on one protomer.[^stoddart2019]
- **Modular / templated assembly** (e.g., DNA-templated construction) to tune spacer length and geometry
  precisely.[^dna_template]
- Continued use of bivalents as **pharmacological tools** to detect and characterize specific receptor
  heteromers, independent of whether they themselves become drugs.[^a2a_d2_tool]

---

---

## 8. Theoretical foundations of multivalency

Bivalent design rests on a body of polyvalency theory that predates and underlies it. The
field-defining review is **Mammen, Choi & Whitesides, "Polyvalent Interactions in Biological
Systems," *Angew. Chem. Int. Ed.* 1998** — a ~40-page treatment that became the most-cited
theoretical anchor of the field.[^mammen1998] It formalized the distinction between monovalent
**affinity** and polyvalent **avidity (functional affinity)** and decomposed enhancement into
**statistical, chelate (entropic), subsite, and receptor-clustering** effects, while stressing that
**negative cooperativity** also occurs (each successive binding event weaker than the last).[^mammen1998]

A recurring theoretical claim is that a flexible linker costs roughly **~RT·ln3 of conformational
entropy per freely rotating single bond** on binding; later work by the Whitesides group showed the
dependence of binding free energy on linker length can nonetheless be weak, partially reconciling the
"rigid vs. flexible linker" debate through the effective-concentration (*C*<sub>eff</sub>) model — a
**genuine historical controversy**, not settled dogma.[^kane2010][^krishnamurthy_multivalency]

The most dramatic avidity demonstration is **trivalent vancomycin** binding a trivalent D-Ala-D-Ala
ligand, with *K*<sub>d</sub> ≈ **4 × 10⁻¹⁷ M** — tighter than the avidin·biotin pair, among the tightest
synthetic receptor–ligand systems known.[^vanco_tri] In **glycobiology**, the **"cluster glycoside
effect"** (nonlinear avidity from clustered carbohydrates) traces to **Y. C. Lee's** work in the 1970s,
and **Laura Kiessling's** group extended multivalency from affinity to *function*, showing multivalent
glycopolymers cluster L-selectin and trigger its proteolytic shedding, with avidity scaling with
valency.[^cluster][^kiessling]

---

## 9. Bivalent and dimeric enzyme inhibitors

A large, often-overlooked branch of the field targets enzymes with two engageable sites — either two
sub-sites of one active-site cleft, or the two halves of a homodimeric enzyme.

**Acetylcholinesterase (AChE) dual-binding-site inhibitors** are the canonical example. AChE has a
~20 Å gorge with a **catalytic anionic site (CAS)** at the base and a **peripheral anionic site (PAS)**
at the rim; bivalent ligands of the right tether length sandwich both. **Bis(7)-tacrine** — two tacrine
units joined by a 7-carbon chain (Pang, Quinn et al., *J. Biol. Chem.* 1996) — was reported up to
~1,000-fold more potent than tacrine, with the heptamethylene tether identified as optimal.[^bis7tacrine]
A crystal structure (*Torpedo* AChE, PDB 2CMF) confirmed that a 5-carbon analogue is too short to reach
the PAS while the 7-carbon analogue bridges CAS and PAS — a direct structural test of the
tether-length hypothesis.[^bistacrine_struct] The optimum is **enzyme-specific** (10 carbons for
*Drosophila*, 8 for *Blattella*), not universal.[^bistacrine_insect] Bis(7)-tacrine is also **not
clean** — it is a potent GABA(A) antagonist and blocks NMDA and K⁺ currents, a caution against the
"selective dimer" narrative.[^bis7_offtarget] Related work produced subnanomolar **huprine–tacrine
heterodimers**,[^huprine_hetero] **donepezil–tacrine hybrids** that displace the PAS marker propidium
(direct evidence of two-site binding),[^donepezil_tacrine] and **memoquin**, which bridged from
dual-site AChE inhibitor toward a multi-target-directed ligand also hitting amyloid-β aggregation.[^memoquin]
Notably, **huprine homodimers were ~29-fold *weaker* than the monomer** — a reminder that dimerization
can hurt.[^huprine_homo]

**Homodimeric enzymes** invite symmetry-matched inhibitors. **HIV-1 protease** is a C2-symmetric
homodimer, which inspired symmetry-based inhibitors matching its dyad; the natural product
**hinnuliquinone**, a C2-symmetric bis-indolyl quinone, inhibits it at *K*<sub>i</sub> ≈ 0.97 µM.[^hiv_sym][^hinnuliquinone]
A distinct strategy uses crosslinked peptoids to block **dimerization** of the protease's interface
rather than its active site.[^hiv_dimerization]

**Glycopeptide antibiotic dimers** exploit cooperative D-Ala-D-Ala binding: natural **eremomycin**
dimerizes "back-to-back" to enhance affinity ~10-fold,[^eremomycin] and synthetic **"shapeshifting"
vancomycin dimers** built on a fluxional bullvalene core reached MICs up to 64-fold below vancomycin
against VRE and slowed resistance emergence.[^bullvalene] A **covalent carbonic anhydrase II dimer**
binding bivalent sulfonamides served as a clean thermodynamic model, reaching 3–40 pM avidity vs.
16 nM monovalent.[^ca_model]

The unifying concept is the **bisubstrate (multisubstrate adduct) inhibitor** — one molecule embodying
features of both substrates of a two-substrate enzyme, binding both sub-sites and gaining both potency
and specificity.[^bisubstrate] All protein kinases, having separate ATP and protein-substrate sites,
are natural targets: the milestone is **Parang & Cole's** ATPγS–peptide bisubstrate inhibitor of the
insulin-receptor kinase (*Nat. Struct. Biol.* 2001).[^parang2001] For **Abl/Bcr-Abl**, bivalent
strategies span the ATP site and the allosteric **myristate pocket** (GNF-2 class), suppressing
resistance mutations including the **T315I** gatekeeper.[^abl] An early **5′-FSBA–tyrosine** Abl
conjugate that bound only the ATP site is an instructive negative result.[^abl_fail] Bisubstrate/NAD
cofactor mimics (e.g., **EM-1745** for 17β-HSD; NNMT bisubstrate analogues) round out the class.[^nad]

---

## 10. The wider GPCR / neuro bivalent toolbox

Beyond the famous opioid and dopamine compounds, bivalent design has reached many receptor families,
often as **pharmacological tools** rather than drug candidates:

- **Muscarinic** — Mohr/Holzgrabe **dualsteric antagonist hybrids** (tropane orthosteric + phthalimide
  allosteric, hexamethonium linker) gave the first proof of a bitopic binding mode for antagonists, with
  tropane orientation controlling M2-vs-M5 selectivity.[^musc_dualsteric] **Methoctramine** (Melchiorre)
  was an early homobivalent M2-selective antagonist predating modern dualsteric design.[^methoctramine]
- **Oxytocin** — superpotent bivalent agonists with a **~25 Å** spacer fit a channel-like passage at the
  OTR dimer's TMH1–TMH2 interface, boosting G-protein signaling ~1000-fold in vitro and 40–100-fold in
  vivo.[^oxytocin2016]
- **Melatonin** — N1- and O-linked dimers (22–24-atom spacers) raise MT1 BRET signals ~3-fold; bitopic
  series tune MT1 selectivity (up to ~112-fold); **S26131**, an agomelatine dimer, reportedly shows
  >200-fold higher MT1 affinity.[^melatonin]
- **Melatonin–histamine H3** — the first melatonergic/histaminergic heterobivalents (Pala et al.) bound
  MT1/MT2 and H3 in one molecule.[^mel_h3]
- **Sigma** — **MAM03055A**, the first homobivalent σ2/TMEM97-selective ligand (~60-fold over σ1), binds
  pseudo-irreversibly and depletes σ2/TMEM97 protein, an effect absent for its monomer.[^sigma]
- **Neuropeptide Y** — dimeric argininamide antagonists (Keller/Buschauer) hit Y1/Y4 at nanomolar Ki,
  with Y1 (but not Y4) showing stereochemical discrimination; the dimeric peptide **1229U91** is a Y4
  agonist.[^npy]
- **Somatostatin / GRP** — rigid **oligoproline** scaffolds fixing 10/20/30 Å inter-pharmacophore
  distances showed a 20 Å optimum for cellular internalization.[^oligoproline]
- **Integrins** — cyclic **RGD dimers/tetramers** bind αvβ3 bivalently for higher tumor uptake than
  monomers, widely used in radiotracer design.[^rgd]
- **Specialized probe types** — **photoswitchable** bivalent/dualsteric ligands use azobenzene units for
  millisecond optical control (e.g., H3R ligands VUF14738/VUF14862 shift affinity >10-fold on
  illumination); **covalent/disulfide-linked** dimers (the DV1-dimer CXCR4 probe) lock two protomers
  together.[^photoswitch][^dv1]

A few apparent **gaps** are worth recording: no genuine linked-pharmacophore H1/H4 bivalent surfaced,
and "bivalent NMDA-receptor ligands" resolve only to interface-binding negative allosteric modulators
like **ifenprodil** (which binds the GluN1/GluN2B N-terminal-domain interface), not true tethered
bivalents.[^nmda]

---

## 11. The induced-proximity "TAC zoo"

PROTACs (Section 6) opened a now-sprawling family of bifunctional, induced-proximity molecules. They
share the two-binder-plus-linker architecture but differ in **what they recruit** and **what happens to
the target**:

| Modality | First report | Recruits | Effect on target |
|---|---|---|---|
| **RIBOTAC** | Disney lab, *JACS* 2018 | RNase L | Catalytically degrade a target **RNA**[^ribotac] |
| **DUBTAC** | Nomura lab, *Nat. Chem. Biol.* 2022 | Deubiquitinase OTUB1 | **Stabilize/rescue** a protein (inverse of PROTAC)[^dubtac] |
| **PHICS** | Choudhary lab, *JACS* 2020 | A kinase (AMPK, PKC) | **Phosphorylate** a target[^phics] |
| **PhoRC / PhosTAC** | Yamazoe 2020 (PP1); Crews 2021 (PP2A) | A phosphatase | **Dephosphorylate** a target[^phorc][^phostac] |
| **RIPTAC** | Halda, bioRxiv 2023 / *Cell Chem. Biol.* 2024 | A pan-essential survival protein | **Proximity-based cell death**, no degradation[^riptac] |
| **ATTEC** | B. Lu lab, *Nature* 2019 | LC3 (autophagosome) | **Autophagic** degradation (e.g., mutant huntingtin)[^attec] |
| **AUTOTAC** | Y.T. Kwon lab, *Nat. Commun.* 2022 | p62/SQSTM1 ZZ domain | **Autophagic-lysosomal** degradation[^autotac] |
| **TRAFTAC** | Crews lab, *Nat. Commun.* 2021 | VHL (via dCas9-HaloTag) | Degrade a **transcription factor**[^traftac] |
| **AbTAC** | Wells lab, *JACS* 2021 | Membrane E3 RNF43 (bispecific Ab) | **Lysosomal** degradation of a surface protein[^abtac] |
| **PROTAB** | Genentech, *Nature* 2022 | Transmembrane E3 (ZNRF3/RNF43) | Degrade a **cell-surface receptor**[^protab] |
| **GlueTAC** | *JACS* 2021 | Covalent nanobody + lysosomal sorting | Degrade a **surface protein**[^gluetac] |

Distinct again are **molecular glue degraders** — monovalent, no linker. **Lenalidomide** reprograms
CRBN-CRL4 to degrade IKZF1/IKZF3 (Science 2014);[^lenalidomide_glue] **indisulam** glues splicing factor
RBM39 to CUL4-DDB1;[^indisulam] and the CDK inhibitor **CR8** glues CDK12-cyclin K to DDB1 with no
canonical substrate receptor.[^cr8]

(Attribution notes worth flagging: **PHICS is the Choudhary lab, not Crews** — a common misattribution;
PhosTAC and TRAFTAC are Crews lab; PhoRC (PP1, 2020) predates PhosTAC (PP2A, 2021) as the first
phosphatase-recruiting chimera. Several of these have a preprint year preceding the journal year.)

---

## 12. Caveats on this survey

- **The bridging mechanism is not settled** (Section 4.2). Pharmacological potency gains are robust, but
  whether they reflect true simultaneous two-protomer occupancy — versus avidity from membrane/secondary-
  site anchoring — remains debated, and likely varies by target system.
- **"Optimal spacer length" does not generalize** across target classes (Section 3.2).
- A few sources were paywalled at retrieval time (e.g., the 2024 *Med. Res. Rev.* opioid bivalent/bitopic
  review by Hovah et al., doi:10.1002/med.22050); claims drawing on them were corroborated through
  open-access PMC/PubMed records where possible and are flagged in the source notes.
- The vepdegestrant FDA approval date (May 1, 2026) reflects reporting current as of this survey and is
  cited to the FDA approval page and corroborating trade press.
- **Dimerization can hurt:** several "bivalent" attempts were worse than their monomers (huprine
  homodimers ~29-fold weaker; the 5′-FSBA–tyrosine Abl conjugate bound only one site) — the design is not
  automatically beneficial.
- **Terminology is genuinely contested:** "bivalent," "bitopic," "dualsteric," and "multivalent" are used
  inconsistently and sometimes interchangeably across the GPCR literature.
- **Coverage gap:** a planned sub-survey of multivalent bacterial-toxin and lectin inhibitors (e.g., the
  "STARFISH" Shiga-toxin inhibitor, pentameric AB5-toxin blockers, anti-adhesion glycoclusters) was not
  completed because that biology-adjacent topic was withheld by automated safety filtering during
  research; the general multivalency theory that underpins those designs is still captured in Section 8.
- A number of obscure numeric values (e.g., the S26131 ">200-fold MT1" figure, some muscarinic
  heterodimer Ki values) rest on secondary/review citations or abstracts where full text was paywalled,
  and are flagged as such inline.

---

## References

[^huang2021]: Huang B, St Onge CM, Ma H, Zhang Y. "Design of bivalent ligands targeting putative GPCR dimers." *Drug Discovery Today* 2021;26(1). https://pmc.ncbi.nlm.nih.gov/articles/PMC7856001/
[^portoghese1982]: Erez M, Takemori AE, Portoghese PS. "Opioid antagonist potency of bivalent ligands containing β-naltrexamine." *J Med Chem* 1982. https://pubmed.ncbi.nlm.nih.gov/6292615/
[^stoddart2021]: Stoddart LA, et al. "2016 Philip S. Portoghese Lectureship: Designing Bivalent or Bitopic Molecules for G-protein Coupled Receptors." *J Med Chem* 2019/2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8281448/
[^portoghese_bio]: "Philip S. Portoghese." Wikipedia. https://en.wikipedia.org/wiki/Philip_S._Portoghese
[^portoghese1989]: Portoghese PS. "Bivalent ligands and the message-address concept in the design of selective opioid receptor antagonists." *Trends Pharmacol Sci* 1989;10(6):230–235. https://pubmed.ncbi.nlm.nih.gov/2549665/
[^portoghese1986]: Portoghese PS, et al. "Opioid agonist and antagonist bivalent ligands. The relationship between spacer length and selectivity at multiple opioid receptors." *J Med Chem* 1986;29(10). https://pubmed.ncbi.nlm.nih.gov/3020244/
[^kamal2009]: Kamal M, Jockers R. "Bitopic ligands: all-in-one orthosteric and allosteric." *F1000 Biol Rep* 2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC2948289/
[^kane2010]: Kane RS. "Thermodynamics of Multivalent Interactions: Influence of the Linker." *Langmuir* 2010;26(11):8636–8640. https://pmc.ncbi.nlm.nih.gov/articles/PMC2877167/
[^krishnamurthy2007]: Krishnamurthy VM, Semetey V, et al. "Dependence of Effective Molarity on Linker Length for an Intramolecular Protein–Ligand System." *J Am Chem Soc* 2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2535942/
[^krishnamurthy2011]: "Dependence of Avidity on Linker Length for a Bivalent Ligand–Bivalent Receptor Model System." *J Am Chem Soc* 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3272676/
[^vauquelin2013]: Vauquelin G, Charlton SJ. "Exploring avidity: understanding the potential gains in functional affinity and target residence time of bivalent and heterobivalent ligands." *Br J Pharmacol* 2013;168(8):1771–1785. https://pmc.ncbi.nlm.nih.gov/articles/PMC3623049/
[^yekkirala2013]: Yekkirala AS, Kalyuzhny AE, Portoghese PS. *ACS Chem Biol* 2013. https://pubmed.ncbi.nlm.nih.gov/23675763/
[^glass2016]: "One for the Price of Two… Are Bivalent Ligands Targeting Cannabinoid Receptor Dimers Capable of Simultaneously Binding to both Receptors?" *Trends Pharmacol Sci* 2016. https://pubmed.ncbi.nlm.nih.gov/26917061/
[^oxytocin2016]: "Design and Characterization of Superpotent Bivalent Ligands Targeting Oxytocin Receptor Dimers via a Channel-Like Structure." *J Med Chem* 2016. https://pubs.acs.org/doi/10.1021/acs.jmedchem.6b00564
[^cb2_2024]: "Homodimerization of CB2 cannabinoid receptor triggered by a bivalent ligand." *Pharmacological Research* 2024. https://pubmed.ncbi.nlm.nih.gov/39179054/
[^berque2008]: Berque-Bestel I, Lezoualc'h F, Jockers R. "Bivalent ligands as specific pharmacological tools for GPCR dimers." 2008. https://pubmed.ncbi.nlm.nih.gov/19075611/
[^cooperativity]: "Membrane Interaction of Bound Ligands Contributes to Negative Binding Cooperativity of the EGF Receptor." https://pmc.ncbi.nlm.nih.gov/articles/PMC4109842/ ; "Ligand Binding Dynamics for Pre-dimerised GPCR Homodimers." https://pmc.ncbi.nlm.nih.gov/articles/PMC6722261/
[^ferre2022]: "GPCR heteromers: classification, function and physiological relevance." https://pmc.ncbi.nlm.nih.gov/articles/PMC9468249/ ; "Pharmacological targeting of GPCR heteromers." *Biomed Pharmacother* 2022. https://www.sciencedirect.com/science/article/pii/S1043661822004224
[^aceto2012]: Aceto MD, et al. "MDAN-21..." *Int J Med Chem* 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC4412046/
[^daniels2005]: Daniels DJ, et al. "Opioid-induced tolerance and dependence in mice is modulated by the distance between pharmacophores in a bivalent ligand series." *PNAS* 2005. https://pmc.ncbi.nlm.nih.gov/articles/PMC1323165/
[^kdn21]: Portoghese lab. "A Bivalent Ligand (KDN-21) Reveals Spinal δ and κ Opioid Receptors Are Organized as Heterodimers." https://www.researchgate.net/publication/8543641
[^gnti]: *J Biol Chem.* https://pmc.ncbi.nlm.nih.gov/articles/PMC3411045/ ; "6′-Guanidinonaltrindole." Wikipedia. https://en.wikipedia.org/wiki/6'-Guanidinonaltrindole
[^biphalin]: Cowell SM, Lee YS. "Biphalin: The Foundation of Bivalent Ligands." *Curr Med Chem* 2016;23(29):3267–3284. https://pubmed.ncbi.nlm.nih.gov/27160537/
[^akgun2013]: Akgün E, et al. "Ligands that interact with putative MOR–mGluR5 heteromer in mice with inflammatory pain produce potent antinociception." *PNAS* 2013;110(28):11595–11599. https://pmc.ncbi.nlm.nih.gov/articles/PMC3710855/
[^mmg22_neuro]: MMG22 neuropathic/cisplatin pain. https://pubmed.ncbi.nlm.nih.gov/32345918/ ; https://www.sciencedirect.com/science/article/abs/pii/S0306452223000775
[^lenaour2013]: Le Naour M, Akgün E, et al. "Bivalent Ligands That Target μ Opioid (MOP) and Cannabinoid1 (CB1) Receptors." *J Med Chem* 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3849126/
[^morcxcr4]: MOR–CXCR4 bivalent. https://pubmed.ncbi.nlm.nih.gov/33214847/
[^d2homo]: "Homobivalent Dopamine D2 Receptor Ligands Modulate the Dynamic Equilibrium of D2 Monomers and Homo- and Heterodimers." https://pubmed.ncbi.nlm.nih.gov/33435665/
[^d1d2]: Rashid AJ, et al. "D1–D2 dopamine receptor heterooligomers..." *PNAS* 2007. https://www.pnas.org/doi/10.1073/pnas.0604049104
[^d3nts1]: "Bivalent ligands promote endosomal trafficking of the dopamine D3 receptor–neurotensin receptor 1 heterodimer." *Commun Biol* 2021. https://www.nature.com/articles/s42003-021-02574-4
[^d3nts1_apps]: D3R–NTSR1 heterodimer, addiction/neuropsychiatric context. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8433439/
[^pulido2022]: Pulido D, et al. "Heterobivalent Ligand for the Adenosine A2A–Dopamine D2 Receptor Heteromer." *J Med Chem* 2022;65(1):616–632. https://pmc.ncbi.nlm.nih.gov/articles/PMC11915710/
[^a2a_d2_tool]: A2A-antagonist/D2-agonist bivalent tools for A2A–D2 heteromers. *J Med Chem* 2009. https://pubs.acs.org/doi/10.1021/jm900298c
[^a1d1]: A1–D1 adenosine–dopamine heteromer bivalents. *Acta Pharmacol Sin* 2012. https://www.nature.com/articles/aps2012151
[^serotonin]: "Serotonin dimers": potent selective 5-HT1B/1D agonists (1996). https://pubmed.ncbi.nlm.nih.gov/8960551/ ; "Functional Significance of Serotonin Receptor Dimerization." https://pmc.ncbi.nlm.nih.gov/articles/PMC3788847/
[^cxcr4]: CXCR4 bivalent / HIV-1 entry. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3476724/
[^kinase]: Bivalent/bisubstrate kinase inhibitors. https://pubmed.ncbi.nlm.nih.gov/24564382/ ; https://pubmed.ncbi.nlm.nih.gov/22571662/
[^mt1]: "Design and Characterization of Bivalent BET Inhibitors" (MT1). https://pmc.ncbi.nlm.nih.gov/articles/PMC5117811/
[^smac]: "Future Therapeutic Directions for Smac-Mimetics." *Cells* 2020;9(2):406. https://www.mdpi.com/2073-4409/9/2/406
[^birinapant]: Condon SM, et al. "Birinapant, a Smac-Mimetic..." *J Med Chem* 2014. https://pubs.acs.org/doi/10.1021/jm500176w
[^amyloid]: Bivalent/dual Aβ–tau aggregation inhibitors. *ACS Chem Neurosci* 2021. https://pubs.acs.org/doi/10.1021/acschemneuro.1c00235
[^protac_def]: Sakamoto KM, et al. (foundational) and review "PROTACs come of age." https://pmc.ncbi.nlm.nih.gov/articles/PMC8190915/
[^protac_event]: "Structural basis of PROTAC cooperative recognition." https://pmc.ncbi.nlm.nih.gov/articles/PMC5392356/
[^protac_age]: "PROTACs come of age." https://pmc.ncbi.nlm.nih.gov/articles/PMC8190915/
[^crbn_vhl]: "Cereblon versus VHL." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6561380/
[^sakamoto2001]: Sakamoto KM, Kim KB, Kumagai A, Mercurio F, Crews CM, Deshaies RJ. "Protacs: chimeric molecules that target proteins to the Skp1-Cullin-F box complex for ubiquitination and degradation." *PNAS* 2001;98(15):8554–8559. https://en.wikipedia.org/wiki/Proteolysis_targeting_chimera
[^schneekloth2008]: Schneekloth AR, et al. "Targeted intracellular protein degradation induced by a small molecule." 2008. https://pubmed.ncbi.nlm.nih.gov/18752944/
[^dbet]: dBET1 / ARV-825 linker-length potency. *ACS Cent Sci.* https://pubs.acs.org/doi/10.1021/acscentsci.6b00280
[^arvinas]: Arvinas / Pfizer disclosures on ARV-110 and ARV-471. https://ir.arvinas.com/ ; https://www.pfizer.com/news/announcements/arvinas-and-pfizers-vepdegestrant-arv-471-receives-fda-fast-track-designation
[^fda_veppanu]: FDA. "FDA approves vepdegestrant for ER-positive, HER2-negative, ESR1-mutated advanced or metastatic breast cancer." https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-vepdegestrant-er-positive-her2-negative-esr1-mutated-advanced-or-metastatic-breast ; Arvinas. https://ir.arvinas.com/news-releases/news-release-details/arvinas-announces-fda-approval-veppanu-vepdegestrant-treatment
[^veritac2]: VERITAC-2 (NCT05654623) PFS results. https://www.onclive.com/view/vepdegestrant-hits-pfs-end-point-in-esr1-mutated-er-her2-metastatic-breast-cancer
[^glues]: Molecular glues vs PROTACs. *Biochemistry* (ACS). https://pubs.acs.org/doi/10.1021/acs.biochem.2c00245
[^lenalidomide]: "Cancer therapies based on targeted protein degradation — lessons learned with lenalidomide." https://pmc.ncbi.nlm.nih.gov/articles/PMC8903027/
[^lytac]: Banik SM, et al. (Bertozzi lab). "Lysosome-targeting chimaeras for degradation of extracellular proteins." *Nature* 2020. https://www.nature.com/articles/s41586-020-2545-9
[^autac]: AUTAC (Takahashi et al., *Mol Cell* 2019) and AUTOTAC follow-up. https://www.nature.com/articles/s41467-022-28520-4
[^bsab_cat]: Catumaxomab, first approved bispecific antibody (EMA 2009). *Front Immunol* review. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1020003/full
[^blina]: Blinatumomab (CD19×CD3), FDA 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC8147062/
[^cluster]: "Cluster glycoside effect." *JACS* 2024. https://pubs.acs.org/doi/10.1021/jacs.4c08818
[^galnac]: Trivalent GalNAc–siRNA conjugates (givosiran, lumasiran, inclisiran, vutrisiran). *Front Pharmacol* 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9794871/
[^bro5]: "Drug discovery beyond the rule of 5." *Expert Opin Drug Discov* 2017. https://www.tandfonline.com/doi/full/10.1080/17460441.2017.1264385 ; "Oral Druggable Space beyond the Rule of 5." *Cell Chem Biol* 2014. https://www.cell.com/cell-chemical-biology/fulltext/S1074-5521(14)00289-0
[^stoddart2019]: "2016 Philip S. Portoghese Lectureship: Designing Bivalent or Bitopic Molecules for GPCRs." *J Med Chem* 2019. https://pubmed.ncbi.nlm.nih.gov/31499001/
[^dna_template]: "DNA-modularized construction of bivalent ligands." *Chem* 2022. https://www.cell.com/chem/fulltext/S2451-9294(22)00645-3

<!-- Deep-dive / obscure additions (Sections 8–11) -->
[^mammen1998]: Mammen M, Choi S-K, Whitesides GM. "Polyvalent Interactions in Biological Systems: Implications for Design and Use of Multivalent Ligands and Inhibitors." *Angew Chem Int Ed* 1998;37:2754–2794. https://www.gmwgroup.harvard.edu/publications/polyvalent-interactions-biological-systems-implications-design-and-use
[^krishnamurthy_multivalency]: Krishnamurthy VM, et al. "Multivalency in Ligand Design." In *Fragment-based Approaches in Drug Discovery*, Wiley 2006. https://onlinelibrary.wiley.com/doi/10.1002/3527608761.ch2
[^vanco_tri]: Rao J, Lahiri J, Isaacs L, Weis RM, Whitesides GM. "A trivalent system from vancomycin·D-Ala-D-Ala with higher affinity than avidin·biotin." *Science* 1998;280(5364):708–711. https://www.science.org/doi/10.1126/science.280.5364.708
[^cluster]: "Cluster glycoside effect" (Y.C. Lee). See also *JACS* 2024. https://pubs.acs.org/doi/10.1021/jacs.4c08818
[^kiessling]: Kiessling LL, et al. "Synthetic multivalent ligands as probes of signal transduction." https://pubmed.ncbi.nlm.nih.gov/16557636/ ; *Chem Soc Rev* 2016. https://pubs.rsc.org/en/content/articlehtml/2016/cs/c6cs00165c
[^bis7tacrine]: Pang Y-P, Quinn DM, et al. "Highly potent, selective, and low cost bis-tetrahydroaminacrine inhibitors of acetylcholinesterase." *J Biol Chem* 1996;271:23646–23649. https://pubmed.ncbi.nlm.nih.gov/10208549/
[^bistacrine_struct]: RCSB PDB 2CMF (Torpedo californica AChE with bis-tacrine). https://www.rcsb.org/structure/2CMF
[^bistacrine_insect]: Kim et al. "Bis(n)-tacrines and insect AChE." *NeuroToxicology*. https://pmc.ncbi.nlm.nih.gov/articles/PMC4739519/
[^bis7_offtarget]: Li Y, et al. "Bis(7)-tacrine, off-target GABA(A)/NMDA/K+ channel activity." 1999. https://pubmed.ncbi.nlm.nih.gov/10208550/
[^huprine_hetero]: Camps P, Formosa X, Muñoz-Torrero D, et al. "Huprine-tacrine heterodimers as anti-AChE agents." *J Med Chem* 2005. https://pubmed.ncbi.nlm.nih.gov/15771413/
[^donepezil_tacrine]: Alonso D, et al. "Donepezil-tacrine hybrids; propidium displacement (PAS binding)." *Bioorg Med Chem* 2005. https://pubmed.ncbi.nlm.nih.gov/16230018/
[^memoquin]: Bolognesi ML, et al. "Monomeric derivatives probing memoquin's bivalent interactions." 2011. https://pubmed.ncbi.nlm.nih.gov/22054058/
[^huprine_homo]: Review of structural hybrids of AChE inhibitors (huprine homodimers weaker than monomer). https://www.heraldopenaccess.us/openaccess/the-structural-hybrids-of-acetylcholinesterase-inhibitors-in-the-treatment-of-alzheimer-s-disease-a-review
[^hiv_sym]: "Symmetry-based inhibitors of HIV-1 protease" (review). https://www.sciencedirect.com/science/article/abs/pii/S0223523400800343
[^hinnuliquinone]: Singh SB, et al. "Hinnuliquinone, a C2-symmetric HIV-1 protease inhibitor." *Biochem Biophys Res Commun* 2004. https://www.sciencedirect.com/science/article/abs/pii/S0006291X04020091
[^hiv_dimerization]: Bowman AL, et al. "Crosslinked Peptoid-Based Dimerization Inhibitors of HIV-1 Protease." https://pmc.ncbi.nlm.nih.gov/articles/PMC4441096/
[^eremomycin]: Solution-NMR characterization of eremomycin "back-to-back" dimerization. https://pubmed.ncbi.nlm.nih.gov/7994574/
[^bullvalene]: Ottonello A, et al. "Shapeshifting bullvalene-linked vancomycin dimers against VRE/VRSA." *PNAS* 2023;120:e2208737120. https://pmc.ncbi.nlm.nih.gov/articles/PMC10104512/
[^ca_model]: Krishnamurthy VM, et al. "Bivalent carbonic anhydrase II dimer model of avidity." *JACS* 2011. https://pubmed.ncbi.nlm.nih.gov/22088143/
[^bisubstrate]: Lavogina D, Enkvist E, Uri A. "Bisubstrate analog inhibitors." Review. https://www.sciencedirect.com/science/article/abs/pii/S0163725802001845
[^parang2001]: Parang K, Till JH, Ablooglu AJ, Kohanski RA, Hubbard SR, Cole PA. "Mechanism-based design of a protein kinase inhibitor." *Nat Struct Biol* 2001;8:37–41. https://pubmed.ncbi.nlm.nih.gov/11135668/
[^abl]: Zhang J, et al. "Targeting Bcr-Abl by combining allosteric (myristate pocket) and ATP-site inhibitors." *Nature* 2010;463:501–506. https://www.nature.com/articles/nature08675
[^abl_fail]: "Covalent bivalent ABL/SRC inhibitors; 5′-FSBA–tyrosine negative result." https://pmc.ncbi.nlm.nih.gov/articles/PMC3268058/
[^nad]: Bisubstrate/NAD-cofactor mimics (EM-1745 for 17β-HSD; NNMT bisubstrate analogues). https://www.tandfonline.com/doi/full/10.1080/14756360601051423 ; https://pubs.acs.org/doi/10.1021/acs.jmedchem.9b00413
[^musc_dualsteric]: Bock A, Mohr K, Holzgrabe U, et al. "Dualsteric muscarinic antagonist hybrids." *J Med Chem* 2014. https://pubmed.ncbi.nlm.nih.gov/25051097/
[^methoctramine]: Methoctramine as early homobivalent M2 antagonist; see Portoghese Lectureship review. https://pmc.ncbi.nlm.nih.gov/articles/PMC8281448/
[^melatonin]: O-linked melatonin dimers. *Bioorg Chem* 2019. https://pubmed.ncbi.nlm.nih.gov/30658234/ ; bitopic MT1 series. https://pubmed.ncbi.nlm.nih.gov/21775151/ ; S26131 in Jockers review. https://pubs.acs.org/doi/10.1021/jm401343c
[^mel_h3]: Pala D, et al. "Melatonergic/histaminergic H3 bivalent ligands." *Int J Mol Sci* 2014;15:16114–16133. https://pmc.ncbi.nlm.nih.gov/articles/PMC4200786/
[^sigma]: "MAM03055A, first homobivalent σ2/TMEM97-selective ligand." ~2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8736263/
[^npy]: Keller M, Kaske M, Holzammer T, Bernhardt G, Buschauer A. "Dimeric argininamide-type NPY Y1/Y4 antagonists." *Bioorg Med Chem* 2013;21:6303–6322. https://pubmed.ncbi.nlm.nih.gov/24074877/ ; 1229U91 (Y4 agonist). https://www.sciencedirect.com/science/article/pii/S0143417924000155
[^oligoproline]: Oligoproline-scaffold homobivalent GRP-R / SST2 ligands. *PNAS* 2021. https://www.pnas.org/doi/10.1073/pnas.2108776118
[^rgd]: Cyclic RGD dimers/tetramers for αvβ3 (radiotracer bivalency). https://pmc.ncbi.nlm.nih.gov/articles/PMC2795072/
[^photoswitch]: Photoswitchable allosteric/dualsteric GPCR ligands (review). https://www.sciencedirect.com/science/article/pii/S0165614725000999 ; bidirectional photoswitchable H3R ligands. *JACS* 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5879491/
[^dv1]: Choi W-T, et al. "DV1-dimer: disulfide-linked covalent bivalent CXCR4 probe." 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3476724/
[^nmda]: Ifenprodil as GluN1/GluN2B NTD-interface NAM (not a tethered bivalent). https://pmc.ncbi.nlm.nih.gov/articles/PMC4859819/
[^ribotac]: Costales MG, Matsumoto Y, Velagapudi SP, Disney MD. "RIBOTAC: small molecule recruits RNase L to degrade pre-miR-96." *JACS* 2018;140:6741–6744. https://pubs.acs.org/doi/10.1021/jacs.8b01233
[^dubtac]: Henning NJ, Nomura DK, et al. "DUBTACs stabilize proteins via OTUB1 recruitment." *Nat Chem Biol* 2022;18:412–421. https://www.nature.com/articles/s41589-022-00971-2
[^phics]: Siriwardena SU, Choudhary A, et al. "Phosphorylation-inducing chimeric small molecules (PHICS)." *JACS* 2020;142:14052–14057. https://pubs.acs.org/doi/10.1021/jacs.0c05537
[^phorc]: Yamazoe S, et al. "Phosphatase-recruiting chimeras (PhoRC) dephosphorylating AKT/EGFR via PP1." *J Med Chem* 2020;63:2807. https://pubs.acs.org/doi/abs/10.1021/acs.jmedchem.9b01167
[^phostac]: Hu Z, Crews CM, et al. "PhosTAC: PP2A recruitment for targeted dephosphorylation." *ACS Chem Biol* 2021. https://pubs.acs.org/doi/abs/10.1021/acschembio.1c00693
[^riptac]: Halda Therapeutics. "RIPTACs: regulated induced proximity targeting chimeras." bioRxiv 2023; *Cell Chem Biol* 2024. https://www.cell.com/cell-chemical-biology/fulltext/S2451-9456(24)00307-6
[^attec]: Li Z, Lu B, et al. "ATTECs tether mutant huntingtin to LC3 for autophagic degradation." *Nature* 2019;575:203–209. https://www.nature.com/articles/s41586-019-1722-1
[^autotac]: Ji CH, Kwon YT, et al. "AUTOTAC: p62/SQSTM1-targeting autophagy degraders." *Nat Commun* 2022;13:904. https://www.nature.com/articles/s41467-022-28520-4
[^traftac]: Samarasinghe KTG, Crews CM, et al. "TRAFTACs degrade transcription factors via VHL." *Nat Commun* 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8524358/
[^abtac]: Cotton AD, Wells JA, et al. "AbTACs: bispecific antibodies recruiting RNF43 to degrade PD-L1." *JACS* 2021;143:593. https://pubs.acs.org/doi/10.1021/jacs.0c10008
[^protab]: Marei H, et al. (Genentech). "PROTABs: antibody-based transmembrane-E3 degraders." *Nature* 2022;609:1012. https://www.nature.com/articles/s41586-022-05235-6
[^gluetac]: "GlueTAC: covalent nanobody surface-protein degrader." *JACS* 2021. https://pubs.acs.org/doi/abs/10.1021/jacs.1c08521
[^lenalidomide_glue]: Krönke J, et al. "Lenalidomide causes CRBN-dependent degradation of IKZF1/IKZF3." *Science* 2014. https://www.science.org/doi/10.1126/science.1244851
[^indisulam]: Han T, et al. "Anticancer sulfonamides glue RBM39 to DCAF15." *Science* 2017;356:eaal3755. https://www.science.org/doi/10.1126/science.aal3755
[^cr8]: Slabicki M, et al. "CR8 glues CDK12-cyclin K to DDB1." *Nature* 2020;585:293. https://www.nature.com/articles/s41586-020-2374-x
