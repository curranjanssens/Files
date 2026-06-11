# The Razor-Sharp Dose Window: A First-Principles Investigation

*Educational pharmacology / receptor-theory synthesis. Mechanism and published
evidence only. Compiled June 2026.*

The puzzle: how can a drug potentiate an opioid in a window so narrow that *doubling*
the dose abolishes the effect, and a further 50–100× leaves it at **zero — flat, not
reversed** (not an opponent process). Reasoned up from fundamentals across four axes.

---

## The shape is the fingerprint

"Flat at zero, not negative" is far more informative than "biphasic," and the four
first-principles axes converge on what it rules in and out.

### 1. Mathematics (mass action / difference-of-sigmoids)
- Net = beneficial(dose) − opposing(dose) settles at **exactly zero** at high dose **only
  if the two opposing saturating magnitudes are equal (a = b)** — a knife-edge,
  codimension-1 condition, NOT generic. a>b → keeps working; a<b → reverses (ordinary
  inverted-U). Flat-zero sits *between* them.
- ⇒ The equality must be **structural**, not tuned: either the two arms push-pull one
  conserved quantity (identical maxima by construction), or zero arises "for free" via
  negative cooperativity / substrate-inhibition / feedback.
- Peak at the **geometric mean √(K_A·K_B)**; window width set by affinity ratio r = K_B/K_A.
- A **2× shutoff requires Hill cooperativity n ≳ log₂(r)** — not just two nearby affinities.
- Frameworks: van den Brink 1973; [Mackay 1981, PMC2071862](https://pmc.ncbi.nlm.nih.gov/articles/PMC2071862/).

### 2. Precedents — what actually produces "vanish, not reverse"
Across all pharmacology this exact shape comes cleanly from only two families:
- **Stoichiometric/lattice saturation** — the **prozone/hook effect**: the productive
  complex can no longer form, so signal floors at zero *by construction*. Cleanest match.
- **High-occupancy recruited inhibition** — FcεRI/mast cell, where supra-optimal antigen
  recruits a SHIP1 brake ([PMC3598417](https://pmc.ncbi.nlm.nih.gov/articles/PMC3598417/)).
- The **two-opposing-receptor** route (apomorphine, hormesis) almost always **reverses
  past baseline** — matches only at the fine-tuned equal-maxima limit.
- ⇒ "Flat, not reversed" points AWAY from "two graded receptor curves" and TOWARD a
  **discrete state transition**.

### 3. Biophysics — is the two-mode substrate real?
- Two co-existing receptor populations with a ~2-fold affinity gap and lipid-biased Gs/Gi
  coupling is **ordinary** GPCR behavior: ternary-complex high/low-affinity states, raft vs
  non-raft partitioning, cholesterol shifting CCR3 affinity 2–14 fold AND its coupling
  ([PMC8417553](https://pmc.ncbi.nlm.nih.gov/articles/PMC8417553/)).
- Only the **extreme** version (femtomolar affinity, GM1 as specific trigger) is unsupported
  single-lab.

### 4. Keystone — a single receptor flipping coupling SIGN is textbook-real
- **The dose-driven precedent (the right match): α2-adrenoceptor** flips **Gi (cAMP-down) at
  low agonist concentration → Gs (cAMP-up) at high** — a genuine *concentration*-dependent
  sign flip, PTX-confirmed, ~60–85-fold separation, driven by efficacy + receptor reserve
  ([PMC9471048](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9471048/)). This is the precedent
  that matches a razor *dose* window, because it switches with concentration.
- **The cleanest-proven precedent, but state- not dose-triggered: β2-adrenergic Gs→Gi switch
  via PKA phosphorylation** (Daaka/Lefkowitz 1997, [Nature](https://www.nature.com/articles/36362)),
  reproduced in a **purified reconstituted system** (Zamah 2002,
  [PMID 12063255](https://pubmed.ncbi.nlm.nih.gov/12063255/)). The phosphorylation-dead mutant
  is fully occupied yet cannot switch — proving the trigger is a **state change
  (phosphorylation / lipid-raft context), NOT occupancy**. This is a *tension* with a sharp
  dose window: the best-proven sign-switch is gated by the wrong variable.
- **Opioid-specific anchor (fraud-independent):** the MOR Gi→Gs switch on chronic opioid is
  real, with the adenylyl-cyclase-driving βγ originating from **Gs not Gi**
  (Chakrabarti & Gintzler, [PMID 16967511](https://pubmed.ncbi.nlm.nih.gov/16967511/)),
  and is raft/caveolin-dependent — again **context-gated, not pure occupancy.**
- Caveat (ternary-complex math): an occupancy-driven switch needs added structure (two
  active conformations / receptor reserve), so it is *permitted, not forced*.

## Convergent answer

A razor-sharp, vanish-on-doubling, **flat-at-zero** window is the **signature of a discrete
coupling-state switch**, not a balance of two graded receptor curves. The substrate — a
single receptor flipping Gi↔Gs with occupancy — is independently documented (α2-adrenoceptor),
and the opioid Gs-switch is independently confirmed (Gintzler). **So the phenomenon is
mechanistically respectable in principle, and does not depend on anything retracted.** What
was fraudulent (filamin-A, femtomolar site) or single-lab/unreplicated (GM1 as trigger — never independently replicated, distinct from the retracted filamin-A layer) is only the
*specific quantitative apparatus* — not the existence of the switch.

## The honest gap (the real finding)

**Nobody has ever mapped the full bell-shaped curve with its crossover.** The literature
documents the *potentiating arm* and asserts a sharp window; the geometry that would tell
you whether it is truly **a = b (flat at zero)** vs **a < b (reverses into antagonism)** has
never been cleanly measured. If "flat at zero" is real, it is a *more constraining,
untested* condition than anyone has reported — it would force the excitatory-block and
inhibitory-block magnitudes to be structurally matched, pointing to a **single-effector
push-pull** (e.g., both arms converging on the same cAMP pool), the one configuration that
yields flat-zero for free.

## Cross-system test of the "same-receptor → sharp cliff" law (added after verification)

A wider-lens hypothesis was tested: that the sudden-dropout cliff appears *iff* the
ultra-low antagonist hits the SAME receptor as the agonist (MOR, CB1, D2 = cliff;
DOR, α2 = smooth). Verified across all five legs. **The strong law did NOT survive.**

| Leg | Potentiation real? | Sharp cliff actually measured? | Independent of Crain/Wang/Bear lineage? |
|---|---|---|---|
| MOR | yes, multi-lab | asserted (Oxytrex 2µg vs 4µg; buprenorphine 166:1) — **full curve never mapped** | mixed (Cahill glial = independent; Gs-switch = Wang, retracted) |
| CB1 | yes (Dehpour independent) | **NO — broad window over several log units, not a cliff** | behavioral yes; Gs-switch = Wang |
| DOR | yes | **never measured (single-dose studies)** | no (Queen's lineage; framed as *same* biphasic mechanism) |
| α2 | yes | never measured; inverts to blockade at higher dose | no (Queen's lineage) |
| D2 | **patent-only (Bear/Kessler, n=5 RLS, abandoned)** | **no — asserted, derivative of retracted filamin-A** | **no — cites the retracted opioid work** |

**What survives:** ULD-antagonist *potentiation* of a co-applied agonist is a real,
multi-system, partly-independently-replicated behavioral phenomenon (Dehpour/CB1,
Cahill/MOR-glial, Levine 1988).

**What did NOT survive:** (1) the *sharp cliff* itself was never cleanly dose-mapped
in ANY system — it is an opioid-only, single-lineage clinical observation (Oxytrex 2-vs-4µg;
buprenorphine 166:1 ratio). (2) The one same-receptor case with real dose-ranging (CB1)
shows a BROAD window, contradicting "same-receptor → sudden." (3) The cross-system
"pattern" is substantially **one contaminated lineage** (Wang did the CB1 Gs-switch assays;
the D2 patent cites the retracted opioid filamin-A work) generalizing its own model — not
five independent systems. (4) Crain himself **denied** the generalization, calling opioid
bimodality "in sharp contrast" to monoaminergic systems that use distinct receptor subtypes.

**The robust nearby reality (and it breaks the law):** the one genuinely independent,
replicated sharp biphasic dopamine window is the **D2 autoreceptor** mechanism (low-dose
blocks presynaptic autoreceptors → more dopamine; higher dose hits postsynaptic → reverses) —
a **two-different-receptor-population** mechanism, the *opposite* of intra-receptor mode-switching.

**Net:** the Oxytrex "two countering sites, benefit vanishes on doubling" is a real clinical
observation whose proposed mechanism is fraudulent (filamin-A, retracted), whose dose-response
was never properly characterized by anyone independent, and whose claimed generalization to
CB1/D2 traces to the same discredited source.

## Key sources

Difference-of-sigmoids / functional antagonism ([Mackay 1981](https://pmc.ncbi.nlm.nih.gov/articles/PMC2071862/)) ·
α2-adrenoceptor Gi→Gs concentration switch ([PMC9471048](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9471048/)) ·
opioid MOR–Gsα independent co-IP ([Gintzler 2005, PMID 15857684](https://pubmed.ncbi.nlm.nih.gov/15857684/)) ·
ternary-complex two-transducer model ([Kenakin & Morgan 1989, PMID 2537459](https://pubmed.ncbi.nlm.nih.gov/2537459/)) ·
lipid-biased GPCR coupling ([cholesterol/CCR3, PMC8417553](https://pmc.ncbi.nlm.nih.gov/articles/PMC8417553/)) ·
prozone/hook + FcεRI vanish-not-reverse precedents ([PMC3598417](https://pmc.ncbi.nlm.nih.gov/articles/PMC3598417/)) ·
filamin-A retraction (fraudulent apparatus) ([PMC8967022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8967022/)).
