# MCC22: Design of a Bivalent MOR–CCR5 Ligand

*A research/design document synthesizing the published literature on the bivalent
ligand MCC22.*

> **Scope and disclaimer.** This is a literature-based design and pharmacology
> review assembled for educational and research purposes. It summarizes published,
> peer-reviewed work; it is **not** a synthesis protocol and does not contain
> experimental procedures. Quantitative values are reproduced from the cited
> primary sources and carry the usual uncertainty of preclinical (mouse) data.
> Where the literature is incomplete or sources disagree, this is flagged
> explicitly.

---

## 1. Summary

MCC22 is a **bivalent ligand** — a single molecule carrying two distinct
pharmacophores joined by a spacer — designed to engage a putative
**mu-opioid receptor / chemokine receptor 5 (MOR–CCR5) heteromer**. One end is a
**MOR agonist** (oxymorphone-derived); the other is a **CCR5 antagonist**
(derived from the small-molecule CCR5 antagonist TAK-220); the two are connected
through a **22-atom spacer** (the "22" in the name).

The design exploits a specific piece of pain biology: during inflammation,
chemokine signaling through CCR5 drives **heterologous desensitization** of the
opioid receptor, blunting opioid analgesia and contributing to tolerance. By
simultaneously **agonizing MOR and antagonizing CCR5 within one complex**, MCC22
is hypothesized to deliver opioid analgesia precisely where inflammation has
sensitized the system, while neutralizing the chemokine-driven cross-talk that
normally degrades it.

In mouse models, the payoff is dramatic: MCC22 is reported as roughly
**2,000–3,000-fold more potent than morphine** in inflammatory pain and up to
**~6,000-fold more potent intrathecally** in neuropathic pain, with **no
antinociceptive tolerance** over 9 days of dosing (where morphine tolerance is
complete by day 3) and **no conditioned place preference** (no reward signal).
Critically, the effect is **abolished in CCR5-knockout mice** and is ~3,500-fold
greater than an equimolar *mixture* of the two separate pharmacophores —
evidence that the bivalent design itself, not either component alone, produces
the effect.

---

## 2. Design rationale

### 2.1 The problem: chemokines sabotage opioid analgesia

Inflammatory and neuropathic pain states are accompanied by chemokine release.
Chemokines acting on receptors such as **CCR5, CCR2, CCR7 and CXCR4** cause
**heterologous desensitization** of the mu- and delta-opioid receptors — i.e.,
activation of the chemokine receptor blunts signaling through the *opioid*
receptor, even though they are different receptors. Administering the CCR5/CCR1
ligand RANTES/CCL5 into the periaqueductal gray (a pain-modulating region)
*increases* pain and *blocks* opioid analgesia.[^pnas2002] Pro-inflammatory
chemokines such as CCL3 (MIP-1α) drive internalization of MOR on dorsal root
ganglion neurons and impair MOR-mediated inhibition of cAMP — a candidate
mechanism for inflammation-induced hyperalgesia and for the reduced efficacy of
morphine in chronic pain.[^drg2004]

CCR5 itself is a driver of the neuroinflammation that maintains pathological
pain: CCR5 is expressed and up-regulated on **microglia**, recruits inflammatory
cells to sites of injury, and **CCR5-knockout mice show reduced responses to
chemical, inflammatory and nerve-injury (CCI) pain.**[^ccr5micro][^ccr5ko]
Opioids additionally provoke pro-inflammatory glial signaling (e.g., via TLR4),
a process implicated in tolerance and opioid-induced hyperalgesia.[^neuroinflam]

### 2.2 The hypothesis: a MOR–CCR5 heteromer

MOR and CCR5 can physically associate. A **co-immunoprecipitation** study showed
HA-tagged MOR pulls down FLAG-tagged CCR5 when co-expressed in the same cell
(but not when separately-expressing cells are mixed), and that the two receptors
**cross-desensitize** one another.[^heterodimer2004] The two receptors are
co-expressed in pain-relevant populations — spinal dorsal-horn neurons,
microglia, peripheral immune cells, and dorsal root ganglion
neurons.[^heterodimer2004][^drg2004][^ccr5micro]

**Important caveat — "putative."** The primary literature consistently describes
the MOR–CCR5 heteromer as **putative**. Physical association (co-IP) and
functional cross-talk are documented, and molecular-simulation work supports a
specific **TM5–TM6 association interface** that a bivalent ligand could bridge.
But a definitive structure of the *native* heteromer (e.g., by cryo-EM) is not
claimed in this literature. The potency of MCC22 is consistent with — and is
used as pharmacological evidence *for* — the heteromer, but it is not independent
structural proof.[^jmc2015][^obc2012]

### 2.3 The bivalent solution and the "message–address" logic

Bridging both protomers of the heteromer with one molecule is proposed to
**avoid the cross-desensitization** that otherwise degrades opioid signaling and
to **localize** opioid action to inflamed/sensitized tissue where CCR5 is
engaged. The architecture follows Portoghese's adaptation of Schwyzer's
**message–address** concept: the **"message"** (the oxymorphone-derived agonist)
delivers the pharmacological signal, while the **"address"** (the CCR5 ligand
plus the geometry of the spacer) directs and anchors it at the
heteromer.[^lectureship]

---

## 3. Molecular design

| Element | Identity | Notes |
|---|---|---|
| MOR pharmacophore | **Oxymorphone-derived agonist** | Provides opioid agonism ("message") |
| CCR5 pharmacophore | **TAK-220-derived antagonist** | CCR5 antagonist ("address") |
| Spacer | **22 atoms** | Length is the key SAR variable; "22" names the compound |
| Approx. molecular weight | **~1,255 g/mol** | Reported figure; large by small-molecule standards, reflecting two pharmacophores + spacer |

### 3.1 Spacer length is the critical design variable

The spacer length was optimized empirically, and the optimum is sharp. In the
cisplatin neuropathic-pain model, analogs differing only in spacer length were
far weaker:

| Compound | Spacer length | Intrathecal ED₅₀ (approx.) |
|---|---|---|
| **MCC22** | **22 atoms** | **~0.004 pmol** (optimal) |
| MCC14 | 14 atoms | ~53 pmol |
| MCC24 | 24 atoms | ~40 pmol |

A swing of just two atoms in either direction collapses potency by roughly four
orders of magnitude — strong evidence that the molecule must span a specific
distance to bridge the two protomers, exactly as a heteromer-bridging mechanism
would predict.[^jpet2019][^jmc2015]

### 3.2 Known unknown: exact spacer chemistry

The publicly accessible abstracts and full texts reviewed **do not fully
disclose the atom-by-atom chemistry of the 22-atom spacer** (e.g., the exact
count of glycyl/amide units versus alkyl or glycol segments, and any rigid
elements). This detail appears to reside in supplementary materials and patent
filings rather than in the open-access summaries. Treat the "22-atom" figure as
the reliable, repeatedly-cited design parameter and the internal composition as
**not established from open sources here.** A 2012 *prototype* from a different
group (see §3.3) used a diglycolic-anhydride-based linker, which is suggestive
but not necessarily identical to MCC22's spacer.

### 3.3 Lineage: the 2012 prototype

The first bivalent ligand built to probe the MOR–CCR5 heteromer predates MCC22
and came from **Yan Zhang's group (Virginia Commonwealth University)**, not the
Portoghese lab: Yuan, Arnatt, Li, Haney, Ding, Jacob, Selley & Zhang, *"Design
and synthesis of a bivalent ligand to explore the putative heterodimerization of
the mu opioid receptor and the chemokine receptor CCR5,"* **Org. Biomol. Chem.**
2012, 10(13):2633–46. It paired **naltrexone** (MOR) with **maraviroc** (CCR5)
via a roughly 21-atom, diglycolic-anhydride-derived spacer and established
feasibility of the concept.[^obc2012] MCC22 — with an oxymorphone-derived
*agonist* and a TAK-220-derived antagonist — is the optimized, pharmacologically
active descendant of that idea.

---

## 4. In vivo pharmacology

> All data below are from mouse models. Potency ratios versus morphine vary by
> pain model and route of administration; the intrathecal (spinal) ratios are
> the most mechanism-relevant because they probe direct CNS action.

### 4.1 Potency versus morphine

| Pain model | Route | MCC22 vs. morphine | Source |
|---|---|---|---|
| LPS-induced inflammatory pain | intrathecal | **~2,000–2,400-fold** more potent | [^jmc2015] |
| Inflammatory arthritis (K/B.g7) | i.p. | **~3,000-fold** more potent | [^arth2018] |
| Cisplatin neuropathic pain | intrathecal | **~6,360-fold** more potent (ED₅₀ ~0.004 pmol vs ~25 pmol) | [^jpet2019] |
| Cisplatin neuropathic pain | i.p. | ~4–5-fold more potent | [^jpet2019] |

A telling control: in **naïve (non-inflamed) mice**, MCC22's advantage over
morphine shrinks to only ~4-fold. Its extraordinary potency is **conditional on
the inflammatory state** — precisely what a CCR5-targeted mechanism predicts.[^jmc2015]

### 4.2 No tolerance

Across models (sickle-cell, cisplatin neuropathy, inflammatory arthritis), over
**9 days of repeated dosing**, MCC22 produced **no antinociceptive tolerance**,
whereas **morphine tolerance was complete by ~day 3** and effect was lost by day
9. Strikingly, **mice rendered tolerant to morphine retained full sensitivity to
MCC22**, indicating a mechanism distinct from a conventional mu-agonist.
[^scd2018][^jpet2019][^arth2018]

### 4.3 No reward signal

In the cisplatin neuropathic-pain study, MCC22 **did not produce conditioned
place preference** and did not impair motor function — i.e., no detectable
reward-related behavior, in contrast to morphine.[^jpet2019]

### 4.4 The bivalent design is necessary (mechanistic controls)

- **CCR5-knockout:** In CCR5-deficient (K/B.g7) mice, MCC22 gave **no analgesia**,
  while morphine remained active — the effect requires CCR5.[^arth2018]
- **Monovalent mixture:** MCC22 was **~3,500-fold more potent than an equimolar
  mixture** of the separate MOR-agonist and CCR5-antagonist pharmacophores —
  tethering them together, not just co-administering them, is what matters.[^jmc2015]
- **Microglial dependence:** Co-treatment with the microglial inhibitor
  **minocycline** reduced MCC22 potency by ~67-fold, implicating microglial
  signaling in its action; MCC22 also **lowered the spinal microglial
  inflammatory response** in neuropathic pain.[^jmc2015][^jpet2019]

### 4.5 Models tested (and not)

| Model | Strain | Route(s) | Source |
|---|---|---|---|
| LPS-induced inflammatory pain | C57BL/6 | i.t. | [^jmc2015] |
| Inflammatory arthritis | K/B.g7 TCR-transgenic | i.p. | [^arth2018] |
| Sickle cell disease pain | Townes HbSS transgenic | i.p. | [^scd2018] |
| Cisplatin neuropathic pain | C57BL/6 | i.t. and i.p. | [^jpet2019] |

**Not found** in the MCC22 primary literature reviewed: classic **complete
Freund's adjuvant (CFA)** and **bone-cancer** pain models. (Bone-cancer pain has
been studied with *other* bivalent ligands, e.g., MOR–mGluR5 heteromer ligands,
but not with MCC22 in the sources surveyed.) Earlier informal mentions of a
"CFA" arthritis model appear to be a conflation with the K/B.g7 autoimmune
arthritis model and should not be relied on.

---

## 5. Significance and open questions

**Why it matters.** MCC22 is a proof-of-concept that **GPCR-heteromer-targeted
bivalent ligands** can decouple opioid analgesia from two of its defining
liabilities — **tolerance** and **reward** — at least in mice. By routing
analgesia through an inflammation-gated MOR–CCR5 mechanism, it suggests a path to
analgesics that are potent specifically in pathological pain states (sickle-cell
crisis, chemotherapy-induced neuropathy, inflammatory arthritis) while sparing
the reward and tolerance circuitry that makes conventional opioids dangerous.

**Open questions / limitations.**

1. **Heteromer is still "putative."** Functional and co-IP evidence exists, and
   the spacer-length SAR is compelling, but a native-tissue structure is not
   established. Alternative explanations (e.g., effects at two separate receptor
   populations brought into proximity) are not fully excluded.
2. **Spacer chemistry undisclosed here.** The exact 22-atom composition is not
   recoverable from the open sources reviewed (§3.2).
3. **Preclinical only.** All efficacy/safety data are from mice. Pharmacokinetics,
   CNS penetration of a ~1,255 Da bivalent molecule, oral bioavailability, and
   human translation remain to be demonstrated.
4. **Quantitative spread.** Reported potency ratios versus morphine range widely
   (≈4-fold to ≈6,000-fold) depending on model and route — context matters when
   citing a single "fold" number.

---

## 6. Key references

- **[Primary MCC22 paper]** Akgün E, Javed MI, Lunzer MM, Powers MD, Sham YY,
  Watanabe Y, Portoghese PS. *Inhibition of Inflammatory and Neuropathic Pain by
  Targeting a Mu Opioid Receptor/Chemokine Receptor5 Heteromer (MOR-CCR5).*
  **J. Med. Chem.** 2015;58(21):8647–8657.
  https://pubmed.ncbi.nlm.nih.gov/26451468/
- **[2012 prototype]** Yuan Y, Arnatt CK, Li G, Haney KM, Ding D, Jacob JC, Selley
  DE, Zhang Y. *Design and synthesis of a bivalent ligand to explore the putative
  heterodimerization of the mu opioid receptor and the chemokine receptor CCR5.*
  **Org. Biomol. Chem.** 2012;10(13):2633–2646.
  https://pubmed.ncbi.nlm.nih.gov/22354464/
- **[Inflammatory arthritis]** *A bivalent compound targeting CCR5 and the mu
  opioid receptor treats inflammatory arthritis pain in mice without inducing
  pharmacologic tolerance.* **Arthritis Res. Ther.** 2018.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6062996/
- **[Sickle cell pain]** *Bivalent ligand MCC22 potently attenuates nociception
  in a murine model of sickle cell disease.* 2018.
  https://pubmed.ncbi.nlm.nih.gov/29578946/
- **[Cisplatin neuropathy]** *The bivalent ligand MCC22 potently attenuates
  hyperalgesia in a mouse model of cisplatin-evoked neuropathic pain without
  tolerance or reward.* 2019. https://pubmed.ncbi.nlm.nih.gov/30970233/
- **[Heterodimer / cross-desensitization]** *Heterodimerization and
  cross-desensitization between the mu-opioid receptor and the chemokine CCR5
  receptor.* **J. Biol. Chem.** 2004. https://pubmed.ncbi.nlm.nih.gov/14729105/
- **[Chemokine desensitization of opioid receptors]** *Heterologous
  desensitization of opioid receptors by chemokines inhibits chemotaxis and
  enhances the perception of pain.* **PNAS** 2002.
  https://pubmed.ncbi.nlm.nih.gov/12130663/
- **[CCL3 desensitizes MOR on DRG]** *Proinflammatory chemokines, such as CCL3,
  desensitize mu-opioid receptors on dorsal root ganglia neurons.* 2004.
  https://pubmed.ncbi.nlm.nih.gov/15210821/
- **[CCR5 / microglia]** *Relationship between the chemokine receptor CCR5 and
  microglia in neurological disorders.* https://pubmed.ncbi.nlm.nih.gov/24047524/
- **[CCR5 knockout pain]** *Decreased pain responses of C–C chemokine receptor 5
  knockout mice to chemical or inflammatory stimuli.*
  https://www.sciencedirect.com/science/article/abs/pii/S0028390812005345
- **[Neuroinflammation & tolerance]** *The role of neuroinflammation in the
  transition of acute to chronic pain and opioid-induced hyperalgesia and
  tolerance.* 2024. https://pubmed.ncbi.nlm.nih.gov/38161698/
- **[Design philosophy]** Portoghese bivalent-ligand lectureship review.
  https://pubmed.ncbi.nlm.nih.gov/31499001/

[^jmc2015]: Akgün et al., *J. Med. Chem.* 2015;58(21):8647–8657. PMID 26451468.
[^obc2012]: Yuan et al., *Org. Biomol. Chem.* 2012;10(13):2633–2646. PMID 22354464.
[^arth2018]: *Arthritis Res. Ther.* 2018, PMC6062996.
[^scd2018]: Sickle cell disease model, 2018. PMID 29578946.
[^jpet2019]: Cisplatin neuropathic pain model, 2019. PMID 30970233.
[^heterodimer2004]: *J. Biol. Chem.* 2004. PMID 14729105.
[^pnas2002]: *PNAS* 2002. PMID 12130663.
[^drg2004]: *J. Neurosci.* 2004. PMID 15210821.
[^ccr5micro]: CCR5/microglia review. PMID 24047524.
[^ccr5ko]: CCR5-knockout pain study. ScienceDirect S0028390812005345.
[^neuroinflam]: Neuroinflammation/tolerance review, 2024. PMID 38161698.
[^lectureship]: Portoghese bivalent-ligand design review. PMID 31499001.
