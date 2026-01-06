# E-Mesh Clinical Build Specification
## Cluster Headache Novel Tryptamine Program

---

## EXECUTIVE SUMMARY

This document specifies the optimal E-Mesh configuration for Phase 1/2 clinical trials of a novel tryptamine for acute cluster headache abortion. The build prioritizes:

1. **Precision** — Temperature control for consistent vaporization
2. **Reproducibility** — Standardized configuration across all devices
3. **Safety** — Medical-grade materials, locked settings
4. **Simplicity** — Single-action patient operation
5. **Documentation** — Full traceability for regulatory submission

---

## HARDWARE SPECIFICATION

### Tier 1: RECOMMENDED BUILD (Clinical Grade)

| Component | Specification | Source | Unit Cost | Notes |
|-----------|---------------|--------|-----------|-------|
| **Mod** | Lost Vape Centaurus DNA 250C | VaporDNA, Element Vape | $140-180 | Best-in-class TC accuracy |
| **RDA** | Vandy Vape Mesh V2 (25mm) | VersedVaper, 3FVape | $30-50 | Wide deck, available 2025 |
| **Mesh** | VandyVape SS316L 150 (0.9Ω/ft) | 3FVape, FastTech | $10/roll | Medical-grade 316L |
| **Drip Tip** | 810 Borosilicate Glass | Wotofo, Amazon | $5-10 | Inert, visible vapor |
| **Battery** | Samsung 30Q 18650 (x2) | IMRbatteries | $8/pair | High drain, reliable |
| **Total** | — | — | **~$200-250** | Per patient device |

### Tier 2: BUDGET BUILD (Research Grade)

| Component | Specification | Source | Unit Cost | Notes |
|-----------|---------------|--------|-----------|-------|
| **Mod** | Geekvape Aegis Solo 2 (S100) | VaporDNA | $50-70 | Decent TC, durable |
| **RDA** | Wotofo Profile Clone | 3FVape, AliExpress | $15-25 | Works, less consistent |
| **Mesh** | VandyVape SS316L 150 | Same | $10 | Same mesh |
| **Drip Tip** | 810 Glass | Amazon | $5 | Same |
| **Battery** | Samsung 30Q 18650 | Same | $4 | Single cell |
| **Total** | — | — | **~$90-120** | Per patient device |

### Why DNA Chip is Preferred for Clinical Use

From [Vaping360](https://vaping360.com/best-vape-mods/dna-mods/):
> "Evolv didn't just invent the concept of temperature control, but is still considered the benchmark for TC performance."

| Feature | DNA 250C | Geekvape Aegis |
|---------|----------|----------------|
| TC Accuracy | ±5°C | ±15-25°C |
| Customization | Full via EScribe | Limited on-device |
| Profile Lock | Yes, via software | Partial |
| Replay Mode | Yes | No |
| Efficiency | 97% | ~85% |
| Documentation | Full export | None |

**Recommendation**: Use DNA 250C for Phase 1 (tighter control), consider Aegis for Phase 2 scale-up if cost is limiting.

---

## MESH SPECIFICATION

### Material: SS316L (Medical Grade)

From [CCELL](https://www.ccell.com/News/detail/Cartridge_Safety_Upgrade_316L_Stainless_Steel.html) and [FDA](https://www.fda.gov/media/165146/download):

| Property | SS316L Specification |
|----------|---------------------|
| Composition | Fe, 16-18% Cr, 10-14% Ni, 2-3% Mo, <0.03% C |
| Biocompatibility | ASTM F138 compliant |
| Corrosion Resistance | Excellent (pitting, crevice) |
| Nickel Release | Very low |
| Temperature Stability | Up to 800°C |
| FDA Status | Approved for medical devices |

### Mesh Options

| Type | Resistance | Recommended Wattage | Notes |
|------|------------|---------------------|-------|
| **SS316L 150** | 0.9Ω/ft | 35W limit | **RECOMMENDED** — optimal density |
| SS316L 200 | 1.2Ω/ft | 35W limit | Finer weave, slightly slower heating |
| SS316L 300 | 0.37Ω/ft | 60W limit | Lower resistance, harder to control |
| NexMesh SS316L | 0.15Ω (pre-cut) | 50-80W | Pre-cut strips, less customizable |

### Mesh Cutting Specification

```
Standard Cut:
- Length: 40mm (bent into mushroom shape)
- Width: 10-13mm (to fit RDA posts)
- Resistance: ~0.25-0.35Ω when installed

Pre-Use Preparation:
1. Torch mesh to orange glow (burn off manufacturing residue)
2. Cool completely
3. Install in RDA
4. Fire at 275°C for 10 seconds (final clean)
5. Lock resistance at room temperature
```

---

## TEMPERATURE CONTROL SETTINGS

### Optimal Settings for Tryptamine Vaporization

Based on [DMT-Nexus](https://forum.dmt-nexus.me/threads/direct-e-mesh-method-howto-step-by-step-with-images-and-video.361365/) and tryptamine physical properties:

| Parameter | Setting | Rationale |
|-----------|---------|-----------|
| **Mode** | Temperature Control (SS316L) | Prevents overheating/degradation |
| **TCR Value** | 0.00092-0.00110 (92-110 on device) | SS316L coefficient |
| **Temperature** | 190-210°C (374-410°F) | Above vaporization (~160°C), below degradation |
| **Wattage Limit** | 35W (40mm mesh) | Prevents overshoot |
| **Preheat** | Disabled | Smooth ramp preferred |
| **Resistance Lock** | Enabled at room temp | Prevents TC drift |

### Calibration Protocol

From [Minty Love](https://sites.google.com/view/mintylovesrue/emesh/technique-for-noobs):

```
CALIBRATION CHECK:
1. Load empty mesh (no compound)
2. Darken room
3. Fire at 200°C setting
4. Mesh should glow DIM RED (barely visible)
5. If bright orange → reduce temp or increase TCR
6. If no glow → increase temp or decrease TCR
7. Target: Faintest red glow = optimal vaporization temperature
```

### EScribe Profile (DNA Devices)

```
CLINICAL PROFILE SETTINGS:
- Profile Name: "CH-Tryptamine-v1"
- Material: SS316L
- TCR: 0.00092
- Temperature: 200°C
- Wattage: 35W max
- Preheat: None
- Boost: None
- Resistance Lock: Auto-lock enabled
- Screen Lock: Enabled after profile load

EXPORT: Save as .ecig file for batch programming
```

---

## PRE-LOADING PROTOCOL

### Pharmacy Preparation (GMP-Adjacent)

| Step | Action | Equipment | QC Check |
|------|--------|-----------|----------|
| 1 | Weigh compound | Analytical balance (0.01mg) | Record mass ± 0.05mg |
| 2 | Transfer to mesh | Microspatula, clean surface | Visual confirmation |
| 3 | Melt onto mesh | Mod at 7W, 2-3 pulses | Even distribution |
| 4 | Visual inspection | Magnification optional | No clumping, centered |
| 5 | Install in RDA | Standard procedure | Resistance check |
| 6 | Seal in packaging | Individual blister/pouch | Desiccant included |
| 7 | Label | Lot, dose, date, expiry | Barcode optional |

### Pre-Loading Technique Detail

From [DMT-Nexus](https://www.dmt-nexus.me/forum/default.aspx?g=posts&t=92213):

```
MELTING PROTOCOL:
1. Set mod to 7W power mode (NOT TC)
2. Place weighed compound on CENTER of mesh
3. Very brief pulse (0.5-1 sec) — observe melting
4. Repeat 2-3 times until fully absorbed
5. Compound should be evenly distributed, slightly glossy
6. No visible crystals remaining

CRITICAL: Never hold fire button >2 sec at low wattage
         Compound will vaporize and be lost
```

### Dose Layering for Higher Doses

For doses >20mg:

```
1. Load first half of dose (e.g., 15mg)
2. Melt as above
3. Load second half on top
4. Melt again
5. Result: Even distribution, no pooling
```

### Storage Considerations

| Factor | Specification |
|--------|---------------|
| Temperature | Room temp (15-25°C) |
| Humidity | <60% RH, use desiccant |
| Light | Opaque packaging (light-sensitive) |
| Oxygen | Nitrogen flush if possible |
| Shelf Life | Establish via stability study (target: 30 days) |
| Container | Individual sealed pouch per RDA |

**Oxidation risk**: Tryptamines can oxidize to N-oxides (yellow discoloration). Pre-loaded meshes should be used within stability window.

---

## PATIENT OPERATION PROTOCOL

### Device Delivery (Pre-Configured)

Patient receives:
1. Mod with locked settings (fire button only)
2. RDA pre-loaded with single dose
3. Charged battery installed
4. Instruction card

### Single-Use Operation

```
PATIENT INSTRUCTIONS:

1. PREPARE
   - Sit comfortably
   - Have timer/sitter ready
   - Device should show [locked] indicator

2. BREATHE
   - Exhale completely
   - Place glass tip to lips

3. ACTIVATE
   - Press and HOLD fire button
   - Inhale SLOWLY for 7-10 seconds
   - Vapor should be visible

4. HOLD
   - Release button
   - Hold breath for 10 seconds

5. EXHALE
   - Breathe out slowly
   - Effects begin within 30-60 seconds

6. RETURN
   - Power off device (5 clicks)
   - Return to study coordinator
```

### Clinical Monitoring Points

| Timepoint | Action |
|-----------|--------|
| T-5 min | Baseline vitals, device check |
| T0 | Dose administration |
| T+1 min | Onset confirmation |
| T+5 min | Peak effect assessment |
| T+15 min | Primary endpoint (attack abortion) |
| T+30 min | Safety check |
| T+60 min | Follow-up |

---

## QUALITY CONTROL

### Device Standardization

| QC Step | Method | Acceptance Criteria |
|---------|--------|---------------------|
| Resistance Check | Ohmmeter | 0.25-0.35Ω ± 10% |
| TC Calibration | Thermocouple reference | ±10°C of setpoint |
| Delivered Dose (subset) | Filter + HPLC | 85-115% of label |
| Visual Inspection | Trained operator | No defects, proper assembly |
| Battery Capacity | Full charge/discharge | >2800mAh |

### Batch Documentation

For each batch of pre-loaded devices:

```
BATCH RECORD:
- Batch Number: [e.g., CH-T-2026-001]
- Date Prepared:
- Preparer Initials:
- Compound Lot:
- Target Dose: ____ mg
- Actual Doses: [individual weights]
- Mean ± SD:
- CV%:
- Devices Passed QC: __/__
- Devices Failed QC: __/__
- Failure Reasons:
- Storage Location:
- Expiry Date:
```

### Calibration Schedule

| Item | Frequency | Method |
|------|-----------|--------|
| Analytical Balance | Daily | Calibration weights |
| Mod TC Accuracy | Per batch | Thermocouple test |
| HPLC (if used) | Per run | Standard curve |

---

## TROUBLESHOOTING

### Common Issues

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| No vapor | Battery dead | Check charge |
| | Resistance error | Recheck mesh installation |
| | Compound evaporated | Reload mesh |
| Weak vapor | TC too low | Increase to 210°C |
| | Poor mesh contact | Tighten clamps |
| Harsh vapor | TC too high | Reduce to 190°C |
| | Dry hit | Never fire empty mesh |
| Inconsistent hits | Resistance drift | Lock resistance at room temp |
| | Mesh deformed | Replace mesh |

### Mesh Replacement Indicators

- Visible discoloration (brown/black)
- Resistance changed >20% from baseline
- Physical damage (holes, bends)
- After 3-5 uses maximum

---

## COST ANALYSIS

### Per-Patient Cost (Phase 1)

| Item | Quantity | Unit Cost | Total |
|------|----------|-----------|-------|
| DNA Mod | 1 | $160 | $160 |
| Mesh V2 RDA | 1 | $40 | $40 |
| Glass Drip Tip | 1 | $8 | $8 |
| Batteries | 2 | $4 | $8 |
| Mesh strips | 10 | $1 | $10 |
| **Hardware Total** | — | — | **$226** |
| Compound (10 doses) | 10 | $5/dose | $50 |
| Packaging | 10 | $2 | $20 |
| QC Testing | 1 | $50 | $50 |
| **Consumables Total** | — | — | **$120** |
| **TOTAL/PATIENT** | — | — | **$346** |

### Phase 2 Scale-Up (50 patients)

| Approach | Device Cost | Notes |
|----------|-------------|-------|
| DNA 250C (premium) | $8,000 | Best precision |
| Aegis Solo 2 (budget) | $3,500 | Adequate for scale |
| Hybrid (10 DNA + 40 Aegis) | $4,600 | Recommended |

---

## REGULATORY CONSIDERATIONS

### Device Documentation Package

For NZ/AU regulatory submission:

1. **Device Description**
   - Commercial vaporizer (not custom)
   - Intended use: Delivery of investigational drug
   - Not seeking device approval (drug is IND)

2. **Materials Certification**
   - SS316L medical-grade documentation
   - Biocompatibility references
   - No novel materials

3. **Characterization Data**
   - Delivered dose uniformity (n=30)
   - Particle size distribution
   - Temperature profile
   - Degradation products

4. **Standard Operating Procedures**
   - Device preparation
   - Dose loading
   - Patient instructions
   - Cleaning/disposal

### Precedent

> "GH Research uses commercial Volcano Medic device for 5-MeO-DMT Phase 2 trials. Device is characterized but not separately approved."

---

## RECOMMENDED VENDORS

| Component | Primary Vendor | Backup Vendor | Notes |
|-----------|----------------|---------------|-------|
| DNA Mods | [VaporDNA](https://vapordna.com) | [Element Vape](https://elementvape.com) | US-based |
| Aegis Mods | [VaporDNA](https://vapordna.com) | [MyVpro](https://myvpro.com) | US-based |
| Mesh RDAs | [3FVape](https://3fvape.com) | [FastTech](https://fasttech.com) | China, 2-4 wk shipping |
| SS316L Mesh | [3FVape](https://3fvape.com) | [VandyVape direct](https://vandyvape.com) | Buy in bulk |
| Glass Tips | [Wotofo](https://wotofo.com) | Amazon | 810 size |
| Batteries | [IMRbatteries](https://imrbatteries.com) | [18650BatteryStore](https://18650batterystore.com) | Authentic cells only |

---

## APPENDIX A: ESCRIBE PROFILE EXPORT

```xml
<!-- CH-Tryptamine-v1.ecig profile settings (simplified) -->
<Profile>
  <Name>CH-Tryptamine-v1</Name>
  <Material>SS316L</Material>
  <TCR>0.00092</TCR>
  <Temperature>200</Temperature>
  <TemperatureUnit>C</TemperatureUnit>
  <Power>35</Power>
  <PowerUnit>W</PowerUnit>
  <PreheatType>None</PreheatType>
  <ResistanceLock>Auto</ResistanceLock>
</Profile>
```

Full .ecig file to be generated via EScribe software and version-controlled.

---

## APPENDIX B: QUICK REFERENCE CARD

```
╔══════════════════════════════════════════════════╗
║          E-MESH CLINICAL QUICK REFERENCE          ║
╠══════════════════════════════════════════════════╣
║  MOD: DNA 250C or Aegis Solo 2                   ║
║  RDA: Vandy Vape Mesh V2                         ║
║  MESH: SS316L 150 (0.9Ω/ft)                      ║
║  TIP: 810 Glass                                   ║
╠══════════════════════════════════════════════════╣
║  SETTINGS:                                        ║
║    Mode: TC-SS316L                                ║
║    TCR: 92-110                                    ║
║    Temp: 200°C (190-210 range)                    ║
║    Wattage: 35W limit                             ║
║    Resistance: Lock at room temp                  ║
╠══════════════════════════════════════════════════╣
║  PRE-LOAD:                                        ║
║    1. Weigh dose (analytical balance)             ║
║    2. Place on mesh center                        ║
║    3. Melt at 7W (2-3 short pulses)              ║
║    4. Seal in packaging with desiccant           ║
╠══════════════════════════════════════════════════╣
║  PATIENT USE:                                     ║
║    1. Exhale fully                                ║
║    2. Hold button + inhale 7-10 sec              ║
║    3. Hold breath 10 sec                          ║
║    4. Exhale                                      ║
║    5. Effects onset: 30-60 sec                    ║
╚══════════════════════════════════════════════════╝
```

---

*Specification Version: 1.0 | Date: January 2026*
*Sources: DMT-Nexus, Evolv, VandyVape, CCELL, FDA, GH Research precedent*
