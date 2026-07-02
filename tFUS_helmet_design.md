# Transcranial Focused Ultrasound (tFUS) Helmet Array — Design Document

**Status:** Working draft (iteration 1)
**Scope:** System-level design of a conformal, multi-element phased-array
"helmet" that delivers electronically steered focused ultrasound to
arbitrary intracranial targets through the intact skull.

---

## 0. Assumptions (state and revisit these)

The design space forks sharply by intended use, so this draft commits to a
**primary use case** and notes where the design diverges for others:

- **Primary (this draft):** research-grade, low-intensity **neuromodulation**
  — reversible modulation of neural activity, no tissue destruction.
- **Extensible to:** blood–brain-barrier (BBB) opening with microbubbles
  (still low-pressure, adds cavitation control), and — with major changes to
  power, cooling, and dosimetry — **thermal ablation** (the clinical
  MRgFUS regime, e.g. essential-tremor thalamotomy).

If the actual target is ablation or BBB opening, sections 4 (power), 8
(cooling), and 9 (monitoring) change materially — flagged inline as
**[ABLATION]** / **[BBB]**.

---

## 1. Objectives & intended use

Deliver an acoustic focus of controllable size, position, and intensity to
any point within the adult human brain, non-invasively, correcting for the
phase distortion introduced by the skull, with real-time monitoring of dose
and cavitation, and with electronic (no mechanical) target steering.

Success = the ability to place a focus at a prescribed target (cortical or
deep) with known pressure and location, verified against simulation and
bench measurement, within safety limits.

---

## 2. Top-level requirements

| ID | Requirement | Target (neuromodulation) | Notes |
|----|-------------|--------------------------|-------|
| R1 | Center frequency | 250–650 kHz (baseline **500 kHz**) | Trade-off in §4.1 |
| R2 | Focal spot (lateral FWHM) | 2–5 mm | Scales with λ·F# |
| R3 | Electronic steering volume | Whole brain (±≥60 mm from geometric center) | No mechanical motion |
| R4 | Peak focal pressure (in situ) | up to ~1 MPa | ISPPA/ISPTA within FDA/ITRUSST limits |
| R5 | Skull aberration correction | Per-element phase (+ amplitude) | CT-driven, §7 |
| R6 | Elements | 128–1024 (baseline **256**) | Steering & aberration budget, §5 |
| R7 | Real-time monitoring | Passive cavitation detection; thermal estimate | §9 |
| R8 | Registration | To subject MRI/CT, <1.5 mm | Neuronavigation |
| R9 | Duty cycle / thermal | Skull & scalp heating within limits | §8 |
| R10 | Safety | Mechanical Index & thermal within regulatory bounds | §11 |

---

## 3. System architecture (blocks)

```
Subject CT/MRI ──► Skull model ──► Acoustic sim (k-Wave) ──► Per-element phase/amp
                                                                   │
Neuronavigation / registration ───────────────────────────────────┤
                                                                   ▼
   Helmet transducer array ◄── Coupling (degassed water/gel) ── Driving electronics
        │  (N elements, hemispherical shell)                    (N-channel Tx/Rx,
        │                                                        phase+amp control, HV)
        ├── Passive cavitation receivers ──► Acquisition ──► Cavitation dose
        └── Thermocouples / thermal model ──► Safety monitor ──► Interlock
```

Subsystems: (A) transducer array + housing, (B) acoustic coupling &
cooling, (C) N-channel driving/receiving electronics, (D) treatment-planning
& aberration-correction software, (E) monitoring & safety, (F)
registration/neuronavigation.

---

## 4. Acoustic design

### 4.1 Frequency selection (R1)
Lower frequency → less skull attenuation and aberration, deeper penetration,
but a **larger** focal spot; higher frequency → tighter focus but far worse
skull loss and phase distortion.

- Skull attenuation rises steeply with frequency (roughly ∝ f^1.x–2).
- Wavelength in water: λ = c/f → **6 mm @250 kHz, 3 mm @500 kHz, 2.3 mm
  @650 kHz, 1.5 mm @1 MHz** (c ≈ 1500 m/s).
- **Baseline 500 kHz**: focal spot a few mm, tolerable skull loss, mature
  transducer tech. 650 kHz mirrors clinical MRgFUS ablation; 250–350 kHz
  favored for deep neuromodulation with minimal aberration.

### 4.2 Focal spot & steering
- Lateral FWHM ≈ λ · F#; axial ≈ ~7 · λ · F#² (F# = focal length / aperture).
- A hemispherical helmet gives a low F# (~0.7–1) → near-λ lateral resolution
  (~3 mm at 500 kHz) and a cigar-shaped focus a few mm long.
- **Electronic steering** by per-element delay/phase; steering range and
  grating-lobe behavior are set by element pitch and layout (§5).

### 4.3 Pressure & dosimetry (R4) [ABLATION]/[BBB]
- Neuromodulation: keep in situ ISPPA/ISPTA and Mechanical Index within
  ITRUSST / FDA diagnostic-adjacent guidance; pressures ≲1 MPa, low duty
  cycle, sonication trains (e.g. 300 ms bursts).
- **[BBB]** microbubble-mediated: sub-inertial-cavitation pressures with
  closed-loop control on harmonic/broadband emissions.
- **[ABLATION]** continuous high-intensity sonication to raise focal T >
  55–60 °C; requires MR thermometry, aggressive skull cooling, and
  full clinical dosimetry — out of scope for the baseline.

---

## 5. Array architecture (R6)

### 5.1 Geometry
- **Hemispherical / conformal shell** enclosing the skull; inner radius
  ~14–16 cm; elements tile the inner surface, all geometrically focused
  toward the center, then electronically re-steered to the target.
- Full-head coverage maximizes usable aperture from many angles → better
  aberration correction and access to deep targets.

### 5.2 Element count, pitch, and layout
- **Grating lobes:** a regular grid needs pitch < λ/2 for wide grating-lobe-
  free steering — impractical over a whole helmet (element count explodes).
  Instead use a **quasi-random / spiral element layout**, which spreads
  grating-lobe energy into a low, diffuse background rather than discrete
  hot spots. This is the standard approach in clinical helmet arrays.
- **Baseline 256 elements**, ~8–12 mm elements on a ~15 cm shell, randomized
  placement. Scale to 512–1024 for finer steering, stronger aberration
  correction, and lower secondary-lobe levels (at the cost of channel count
  and $$). 128 is a viable low-cost entry build.
- **Aberration-correction budget:** more independent elements = more degrees
  of freedom to invert the skull's phase screen (§7). This, not focal size,
  is often what drives element count upward.

### 5.3 Element technology
| Option | Pros | Cons |
|--------|------|------|
| PZT (1-3 piezocomposite) | High output, mature, cost-effective | Moderate bandwidth |
| PMN-PT / PIN-PMN-PT single crystal | High coupling, sensitivity | Cost, temperature sensitivity |
| CMUT | Wide bandwidth, batch fabrication, integration | Lower pressure output |
| **Baseline: 1-3 PZT piezocomposite** | Good output + bandwidth, conformable | — |

Each element: matching layer(s) for water loading, air/composite backing for
efficiency (neuromodulation favors efficiency/narrowband over bandwidth),
individually wired and shielded.

---

## 6. Coupling (R-coupling)
- **Degassed, deionized water** bath or bladder between array and scalp,
  with acoustic gel at the scalp interface; degassing prevents spurious
  cavitation and attenuation from bubbles.
- Conformable membrane/bladder to accommodate head shape and hold coupling
  without large standoff. Scalp hair management (parted/clipped or coupling
  aids) matters for transmission.

---

## 7. Skull aberration correction (R5) — the core scientific problem

The skull is a lossy, fast (c≈2500–3000 m/s), variable-thickness layer that
**dephases** contributions from different elements; without correction the
focus degrades and shifts.

**Method (baseline — CT-driven, non-invasive):**
1. Acquire subject **CT** → derive skull geometry and, via Hounsfield-unit
   → porosity mapping, local speed of sound and attenuation.
2. Register CT/MRI to the helmet coordinate frame (§12 registration).
3. **Simulate** propagation from each element to the target through the
   skull model (full-wave, e.g. **k-Wave** pseudospectral, or hybrid
   ray/angular-spectrum for speed).
4. Extract per-element **phase and amplitude corrections** (time-reversal /
   phase conjugation) that co-focus all elements at the target.
5. Apply corrections in the driving electronics; re-simulate to verify focal
   position/pressure before sonication.

**Alternatives / refinements:**
- **Time-reversal from an implanted/virtual source** (research; invasive).
- **MR-ARFI** (acoustic radiation force imaging) or MR thermometry to
  measure and iteratively refine the focus in situ.
- **Passive/hydrophone-based** calibration on ex-vivo skulls for benchtop.

Aberration correction quality is the primary determinant of focal fidelity
and is where element count (§5) pays off.

---

## 8. Driving electronics & cooling

### 8.1 N-channel transmit/receive (R6)
- One channel per element: independent **phase (delay) and amplitude**
  control, class-D or linear RF amplifier per channel, HV supply sized to
  target pressure and element impedance.
- FPGA-based delay generation for μs-level phase precision at 500 kHz
  (period 2 µs → sub-degree phasing needs ~ns timing).
- Impedance matching network per element; per-channel current monitoring.
- A subset of channels (or dedicated receivers) switch to **Rx** for passive
  cavitation detection (§9).

### 8.2 Thermal management (R9) [ABLATION]
- Neuromodulation duty cycles are low; scalp/skull heating is modest but
  still bounded — model skull heating and cap ISPTA.
- **[ABLATION]** requires actively **circulated chilled degassed water** over
  the scalp to remove skull-absorbed heat, plus MR thermometry.

---

## 9. Monitoring & safety (R7) [BBB]
- **Passive Cavitation Detection (PCD):** receive elements listen for
  sub-/ultra-harmonic (stable cavitation) and broadband (inertial
  cavitation) emissions; used as the closed-loop control signal for **[BBB]**
  and as a safety interlock for neuromodulation.
- **Thermal safety:** real-time estimate from a thermal model (and MR
  thermometry when in-magnet); hard interlock on limits.
- **Focus verification:** pre-sonication simulation check; optional MR-ARFI.

---

## 10. Treatment planning & software (subsystem D)
- Pipeline: import CT/MRI → segment skull/brain → register to helmet →
  select target → simulate & compute per-element phase/amp → predict focal
  pressure/location/heating → operator review → export drive table.
- Simulation core: **k-Wave** (MATLAB/Python/C++/CUDA) for full-wave, with a
  faster angular-spectrum path for interactive planning.
- Store every plan + measured outcome for the reproducibility/eval record.

---

## 11. Regulatory, ethics & safety
- Non-significant-risk vs significant-risk device determination; **IRB/ethics
  approval** for any human use; likely IDE pathway for clinical work.
- Acoustic output limits: adhere to **ITRUSST** neuromodulation safety
  consensus and FDA diagnostic-ultrasound MI/TI reference points as the
  conservative envelope for the neuromodulation baseline.
- Electrical safety (IEC 60601), biocompatible patient-contacting materials,
  emergency stop / interlocks tied to §9.

---

## 12. Registration & neuronavigation (R8)
- Optical or frame-based tracking of helmet ↔ subject; fuse with the
  planning CT/MRI so the simulated target maps to real anatomy < ~1.5 mm.
- Re-check registration if the head moves; consider a bite-bar or frame for
  deep targets where sub-mm matters.

---

## 13. Verification & validation plan (the falsifiable part)

| Stage | Test | Pass criterion |
|-------|------|----------------|
| V1 Free-field | Raster-scan focus with a **calibrated hydrophone** in a water tank; no skull. | Focus at commanded location; pressure within X% of sim. |
| V2 Steering | Command a grid of targets; measure focal shift & secondary-lobe level. | Steering error < 1–2 mm; secondary lobes below spec across the steering volume. |
| V3 Aberration | Insert **ex-vivo human skull**; apply CT-derived correction. | Corrected focus restores >Y% of free-field pressure and <Z mm shift vs. uncorrected. |
| V4 Phantom | Tissue-mimicking / thermochromic phantom; measure focal heating & shape. | Matches simulated focus size/position. |
| V5 Monitoring | Induce controlled cavitation (microbubble phantom). | PCD detects and interlock fires within budget. |
| V6 Reproducibility | Repeat V1/V3 N times. | Focal position/pressure stable within tolerance. |

Every stage compares **measurement vs. k-Wave simulation** — the simulation
is only trusted once V1–V3 validate it, after which it drives planning.

---

## 14. Development roadmap (milestones)

- **M0 — Modeling foundation.** Stand up the k-Wave pipeline; simulate a
  hemispherical array + skull; explore frequency/element-count/layout
  trade-offs *in silico*. **Exit:** simulated design meets R1–R3, R6.
- **M1 — Single-element & small-cluster bench.** Fabricate/procure a few
  elements; validate output, matching, and hydrophone measurement (V1 at
  small scale). **Exit:** measured element matches modeled response.
- **M2 — Sub-array prototype (e.g. 32–64 ch).** Build partial helmet +
  multichannel driver; demonstrate electronic steering & phasing (V1–V2).
  **Exit:** steered focus verified vs. sim.
- **M3 — Aberration correction through ex-vivo skull.** CT→correction→
  refocus (V3). **Exit:** hypothesis H-aberration accepted with data.
- **M4 — Full helmet (baseline 256 ch) + monitoring.** Integrate PCD, safety
  interlocks, planning software, registration (V4–V6). **Exit:** end-to-end
  bench-validated system.
- **M5 — Toward biological/clinical use.** Ethics/IRB, dosimetry
  qualification, and (if pursued) [BBB]/[ABLATION] extensions.

---

## 15. Key hypotheses to falsify

| # | Hypothesis | Falsification test |
|---|-----------|--------------------|
| H1 | A 256-element, 500 kHz quasi-random helmet can place a <5 mm focus anywhere in the brain via electronic steering alone. | V2 across the steering volume. |
| H2 | CT-derived per-element phase correction restores the through-skull focus to within a specified pressure/position tolerance of free-field. | V3 on multiple ex-vivo skulls. |
| H3 | PCD provides a reliable closed-loop safety/cavitation signal within the interlock time budget. | V5. |
| H4 | Simulation (once validated in V1–V3) predicts focal pressure/position within tolerance, enabling simulation-only planning. | Blind sim-vs-measurement comparison. |

---

## 16. Major risks

| Risk | Mitigation |
|------|-----------|
| Skull aberration correction under-performs (dominant technical risk). | Higher element count; better CT→property mapping; MR-ARFI in-situ refinement. |
| Grating/secondary lobes deposit off-target energy. | Quasi-random layout; sub-λ effective pitch; monitor in V2. |
| Skull/scalp heating limits duty cycle. | Lower frequency; active cooling; ISPTA caps; thermal modeling. |
| Channel-count cost & complexity. | Phased build (32→64→256); commercial multichannel platforms. |
| Registration error moves the focus. | Frame/bite-bar for deep targets; re-verify on motion. |
| Regulatory/ethical delay. | Engage IRB and ITRUSST/FDA guidance early; conservative dosimetry. |

---

## 17. Open decisions (need input to lock)

1. **Primary use case** — neuromodulation (assumed) vs BBB vs ablation? Drives
   power, cooling, monitoring, and regulatory path.
2. **Frequency** — 500 kHz baseline vs 250–350 kHz (deep/low-aberration) vs
   650 kHz (clinical-analog).
3. **Element count / budget** — 128 (entry) / 256 (baseline) / 512–1024
   (clinical-grade).
4. **MR-compatibility** — is in-magnet operation (MR thermometry / MR-ARFI)
   required? Adds materials and shielding constraints.
5. **Build vs buy** electronics — custom N-channel driver vs commercial
   research ultrasound platform.

---

*This is iteration 1: a system-level design and validation plan. Next step is
M0 — stand up the k-Wave modeling pipeline and run the frequency / element-
count / layout trade study to turn the baselines above into locked numbers.*
