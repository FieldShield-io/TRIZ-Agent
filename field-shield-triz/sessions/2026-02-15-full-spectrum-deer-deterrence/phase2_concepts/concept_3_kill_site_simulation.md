# CONCEPT 3: KILL-SITE ECOLOGY SIMULATION
## Phase 2 Engineering Proposal — Field Shield Platform

**Concept Family**: D (Kill-Site Ecology Simulation)
**Origin**: B2 (KILL ZONE MIRAGE) — Biomimicry Researcher, Phase 1
**Date**: 2026-02-15
**Engineering Team**: AgTech Domain Expert + Safety Engineer + Operations Specialist
**Phase 1 AgTech Reality Score**: 7/10
**Phase 1 Weighted Rank**: #6 of 12 concept families (Score: 7.05)
**Estimated Cost**: $23/acre/year (Phase 1 estimate; refined below)

---

## Executive Summary

Kill-Site Ecology Simulation deploys rotating artificial "kill site" stations at field perimeters that emit predator scat compounds, decomposition volatiles (cadaverine, putrescine), and visual "remains" cues (synthetic fur tufts, simulated blood stains, ground disturbance) to simulate the aftermath of predation. This exploits one of the strongest innate spatial avoidance behaviors in white-tailed deer: avoidance of locations where predation has recently occurred. Unlike the banned Hunting Ghost concept (which simulated a LIVE predator with thermal decoys and infrasound), Kill-Site Simulation creates evidence that a predator HAS ALREADY killed in this area. The deterrent cue is "something died here recently" -- not "a predator is here now."

Stations rotate spatially every 3-7 days to mimic natural predator kill frequency. Compound blends rotate across predator species (wolf, coyote, bobcat) to prevent olfactory adaptation. At $19-27/acre/year, this is one of the most cost-effective concepts in the Field Shield portfolio. However, the Phase 1 assessment correctly identified the core vulnerability: olfactory-only deterrence habituates in 2-6 weeks without consequence pairing. This proposal addresses that vulnerability through a reinforcement integration protocol with the distributed mesh deterrent network (Family B).

**GO/NO-GO recommendation after this analysis**: CONDITIONAL GO as an integrated subsystem. Kill-Site Simulation should NOT be developed as a standalone product. It should be developed as a modular scent-dispensing peripheral that plugs into the mesh network platform (Concept 1), with consequence reinforcement from water jets, capsaicinoid ground treatment, or shock pads at 15-25% of encounters.

---

## 1. Biological Rationale: Why Kill-Site Avoidance Works

### 1.1 The Landscape of Fear and Kill-Site Ecology

In natural ecosystems, predator kill sites represent the highest-risk locations on the "landscape of fear" (Laundre et al., 2001). Prey animals maintain cognitive spatial maps in the hippocampus where specific locations are tagged with emotional valence by the basolateral amygdala. Kill sites receive the strongest negative valence tags because they represent confirmed evidence that predation has occurred at that exact location.

Key behavioral evidence:

- **Elk-wolf systems (Yellowstone)**: After wolf reintroduction, elk showed persistent avoidance of confirmed wolf kill sites for 1-3 weeks after the kill, even after all carcass remains were removed (Mech et al., 2001; Fortin et al., 2005). Avoidance radius extended 200-400m from the kill site center.
- **Deer-predator systems**: White-tailed deer in areas with established predator populations (wolves in Minnesota/Wisconsin, cougars in the Black Hills) show strong spatial avoidance of areas with concentrated predator scat and kill evidence (Nelson & Mech, 1986). The avoidance response is strongest during the first 5-7 days after fresh sign is deposited, declining to baseline by 14-21 days.
- **Multi-sensory integration**: Kill sites present a coherent multi-modal signal: predator scat odor (indicating the predator was here) + decomposition volatiles (indicating something died here) + visual remains (fur, bone, blood stains, disturbed ground). The combination of these cues is far more compelling than any single cue alone. Phase 1 behavioral science research ranked the predator odor + decomposition odor combination as the #2 most habituation-resistant cue combination (6-12 weeks), behind only physical contact + predator odor + variable timing.
- **Conspecific death avoidance**: Wisman & Shrira (2015) demonstrated that putrescine elicits innate threat management mechanisms across mammalian species. Deer encountering decomposition volatiles of conspecifics show heightened vigilance, reduced foraging, and spatial displacement lasting 3-7 days at natural concentrations.

### 1.2 Why This Is NOT Hunting Ghost

| Feature | Hunting Ghost (BANNED) | Kill-Site Simulation |
|---------|----------------------|---------------------|
| What is simulated | A live predator actively hunting | The aftermath of a past kill event |
| Primary sensory channel | Thermal signature + infrasound | Olfactory (scat + decomposition) + visual (remains) |
| Temporal framing | "A predator is here NOW" | "A predator killed here RECENTLY" |
| Energy signature | Active: thermal decoy, speaker | Passive: chemical wicking, static props |
| Deer behavioral response | Flight (immediate escape from predator) | Spatial avoidance (do not enter this area) |
| Hardware complexity | Thermal IR emitter, infrasound generator, controller | Scent reservoir, wick, visual props |
| Power requirement | Continuous (thermal + acoustic) | Near-zero (passive chemical release) |

The distinction is fundamental: Kill-Site Simulation creates a spatial avoidance zone ("this area is dangerous, do not enter") rather than triggering an acute flight response ("run away now"). Spatial avoidance is the more operationally useful outcome for crop protection because it deters deer from entering the field perimeter, rather than startling deer that have already entered.

---

## 2. Chemical Compound Specification

### 2.1 Predator Scat Compounds

Predator feces contain characteristic volatile organic compounds (VOCs) that prey species detect via both the main olfactory epithelium (MOE) and the vomeronasal organ (VNO). The following compounds are the primary active constituents for deer deterrence:

| Compound | Chemical Name | CAS # | Role | Detection Pathway | Vapor Pressure (25C) | Effective Conc. (air) | Source | Cost/kg | Regulatory Status |
|----------|--------------|-------|------|-------------------|----------------------|----------------------|--------|---------|-------------------|
| **TMT** | 2,4,5-Trimethylthiazoline | 13678-58-5 | Fox anal gland secretion; universal predator alarm | Grueneberg ganglion -> dPAG (freezing/flight) | ~0.5 mmHg | 10-100 ppb | Sigma-Aldrich, TCI Chemicals | $150-300/g (research grade); ~$50-80/g (bulk synthesis) | Not EPA-regulated; research chemical; no FIFRA listing |
| **PEA** | 2-Phenylethylamine | 64-04-0 | Universal carnivore urinary marker | TAAR4 receptor in MOE | 0.23 mmHg | 50-500 ppb | Sigma-Aldrich, Fisher Scientific, bulk from amino acid suppliers | $15-30/kg (bulk) | FDA GRAS (naturally in chocolate, cheese); not restricted |
| **Skatole** | 3-Methylindole | 83-34-1 | Fecal odor compound; present in all mammalian feces, concentrated in carnivores | MOE, general olfactory | 0.012 mmHg | 1-10 ppm | Sigma-Aldrich, TCI, bulk fragrance suppliers | $15-25/kg (bulk) | FDA GRAS (used in fragrance industry at trace levels); OSHA PEL not established |
| **Indole** | Indole | 120-72-9 | Fecal/decomposition marker; also found in plant VOCs | MOE, general olfactory | 0.012 mmHg | 0.5-5 ppm | Sigma-Aldrich, TCI, bulk fragrance suppliers | $20-35/kg (bulk) | FDA GRAS (used in perfumery); not restricted |
| **Isovaleric acid** | 3-Methylbutanoic acid | 503-74-2 | Branched-chain fatty acid in wolf/coyote feces | VNO (V2R receptors) -> medial amygdala | 0.44 mmHg | 10-100 ppb | Sigma-Aldrich, bulk organic acid suppliers | $10-20/kg (bulk) | FDA GRAS (naturally in cheese, fermented foods); not restricted |
| **Sulfated steroids** | Various (e.g., androsterone sulfate) | Various | Predator fecal steroid markers; VNO-specific | VNO -> accessory olfactory bulb -> medial amygdala | Very low (non-volatile; contact detection) | Contact/near-field only | Steraloids Inc., Sigma-Aldrich | $200-500/g (research grade) | Not regulated as pesticides; research chemicals |

**Primary blend recommendation** (balancing cost, efficacy, and availability):
- **Coyote scat simulant**: PEA (50 mg/station) + skatole (200 mg/station) + indole (100 mg/station) + isovaleric acid (150 mg/station)
- **Wolf scat simulant**: PEA (75 mg/station) + skatole (300 mg/station) + TMT (5 mg/station) + isovaleric acid (200 mg/station)
- **Bobcat scat simulant**: PEA (40 mg/station) + skatole (150 mg/station) + indole (150 mg/station) + 3-mercapto-3-methylbutan-1-ol (felid-specific sulfur compound, 10 mg/station)

Note: TMT is included in the wolf blend only because of its high cost. PEA and skatole are the workhorses for cost-effective deployment.

### 2.2 Decomposition Volatiles

| Compound | Chemical Name | CAS # | Role | Effective Conc. (air) | Vapor Pressure (25C) | Source | Cost/kg | Safety Profile |
|----------|--------------|-------|------|-----------------------|---------------------|--------|---------|----------------|
| **Cadaverine** | 1,5-Diaminopentane | 462-94-2 | Primary decomposition amine; "death odor" | 1-50 ppm | 2.89 mmHg | Sigma-Aldrich, TCI, Alfa Aesar; bulk from chemical distributors | $25-40/kg (bulk technical grade) | Irritant (skin, eyes, respiratory). LD50 oral rat: 270 mg/kg. OSHA: no specific PEL; treat as amine (general TWA 5 ppm recommended). Not carcinogenic. Biodegradable. |
| **Putrescine** | 1,4-Diaminobutane | 110-60-1 | Primary decomposition amine; synergistic with cadaverine | 1-50 ppm | 3.93 mmHg | Sigma-Aldrich, TCI, Alfa Aesar; bulk from chemical distributors | $30-50/kg (bulk technical grade) | Irritant (skin, eyes, respiratory). LD50 oral rat: 474 mg/kg. Similar safety profile to cadaverine. Biodegradable. |
| **Dimethyl trisulfide** | DMTS | 3658-80-8 | Sulfur-based decomposition volatile; extremely pungent | 0.01-1 ppm | 3.1 mmHg | Sigma-Aldrich, flavor/fragrance suppliers | $30-60/kg | Strong irritant at high concentration. Very low odor threshold (0.01 ppb for humans). Handle with care. |

**Decomposition blend per station loading**: Cadaverine (500 mg) + putrescine (500 mg) + dimethyl trisulfide (5 mg). This produces an olfactory signal detectable by deer at 50-100m downwind in moderate conditions (5-10 mph wind), fading to undetectable at 150-200m.

### 2.3 Deer Alarm Pheromone Compounds

The tarsal gland and interdigital gland secretions of alarmed white-tailed deer contain volatile compounds that signal danger to conspecifics. However, the complete alarm pheromone blend has NOT been fully characterized and synthesized. This remains a research gap.

Known components include:
- **Lactones** (gamma-dodecalactone and related compounds from tarsal gland)
- **Isovaleric acid** (already included in predator scat blend)
- **Formic acid** and **butyric acid** from interdigital glands

**Recommendation**: Do NOT include deer alarm pheromone in the initial prototype. The incomplete characterization means any synthetic blend would be a rough approximation. Focus on the predator scat + decomposition compound combinations, which are better characterized and have stronger supporting evidence.

### 2.4 Compound Summary Table

| Compound | Per-Station Loading | Stations per Refill Cycle (8) | Monthly Consumption (50-acre) | Monthly Cost | Annual Cost |
|----------|-------------------|------------------------------|------------------------------|-------------|-------------|
| PEA | 50-75 mg | 400-600 mg | 1.2-1.8 g | $0.04 | $0.48 |
| Skatole | 150-300 mg | 1.2-2.4 g | 3.6-7.2 g | $0.11 | $1.32 |
| Indole | 100-150 mg | 800 mg - 1.2 g | 2.4-3.6 g | $0.08 | $0.96 |
| Isovaleric acid | 150-200 mg | 1.2-1.6 g | 3.6-4.8 g | $0.05 | $0.60 |
| TMT | 5 mg (wolf only) | 40 mg | 120 mg | $8.00 | $96.00 |
| Cadaverine | 500 mg | 4 g | 12 g | $0.42 | $5.04 |
| Putrescine | 500 mg | 4 g | 12 g | $0.50 | $6.00 |
| DMTS | 5 mg | 40 mg | 120 mg | $0.005 | $0.06 |
| **TOTAL (without TMT)** | | | | **~$1.20/month** | **~$14.46/year** |
| **TOTAL (with TMT)** | | | | **~$9.20/month** | **~$110.46/year** |

**Critical cost finding**: TMT is the only expensive compound. Without TMT, the entire annual compound cost for a 50-acre deployment is approximately $15/year. With TMT used in 1 of 3 blend rotations, annual compound cost rises to approximately $45-50/year. TMT should be used sparingly (wolf blend only, every 3rd rotation) to keep costs down.

---

## 3. Station Hardware Design

### 3.1 Design Requirements

- Hold 3 scent compound reservoirs (one per predator species blend)
- Release compounds via passive wicking with optional wind-assisted dispersion
- Include visual props (synthetic fur tufts, UV-stable "blood stain" material)
- Weatherproof (rain does not wash away compounds for at least 48 hours)
- Animal-proof (raccoons, birds, rodents cannot disturb or consume compounds)
- Relocatable by one person in under 2 minutes per station
- Unpowered (passive) for the base version; optional active dispensing for mesh-integrated version
- Per-station BOM target: less than $80

### 3.2 Station Design: Passive Version (Base)

**Form factor**: Ground-level platform, approximately 12" x 12" x 8" (30 cm x 30 cm x 20 cm), constructed from UV-stabilized HDPE (same material as agricultural chemical tanks). Weight: 3-5 lbs loaded.

**Components**:

| Component | Description | Qty | Unit Cost | Extended |
|-----------|-------------|-----|-----------|----------|
| HDPE enclosure | 12"x12"x8" injection-molded box with hinged lid, rain shield overhangs, ventilation slots on 2 sides | 1 | $12.00 | $12.00 |
| Scent reservoir cartridges | 50 mL HDPE bottles with press-fit wicking caps (cotton wick protrudes 2 cm through cap) | 3 | $1.50 | $4.50 |
| Wicking assemblies | Cotton rope wicks (6mm dia, 15 cm length) with HDPE holders; wind-exposed tips | 3 | $0.75 | $2.25 |
| Rain shield / drip cover | HDPE overhang above wick exposure zone; prevents direct rain contact while allowing wind-driven VOC dispersion | 1 | $3.00 | $3.00 |
| Ground stake mount | 12" galvanized steel stake with top plate; drives into soil; station clips onto plate | 1 | $4.00 | $4.00 |
| Visual props - fur tufts | Synthetic deer-colored fur (acrylic fiber, UV-stable) on 8" flexible wire stalks; 3 per station | 3 | $1.00 | $3.00 |
| Visual props - "blood stain" mat | 6"x6" UV-stable red-brown silicone mat placed on ground adjacent to station; simulates dried blood | 1 | $2.00 | $2.00 |
| Locking clip | Stainless steel clip securing lid against raccoon tampering | 1 | $1.50 | $1.50 |
| Mesh screen | Stainless steel mesh (1/4" opening) over ventilation slots; prevents insect/rodent entry | 2 | $1.25 | $2.50 |
| Labeling/instructions | Weatherproof adhesive label with handling instructions and compound identification | 1 | $0.50 | $0.50 |
| **TOTAL per station** | | | | **$35.25** |

**Operating principle**: Compound solutions are loaded into reservoir cartridges. Cotton wicks draw liquid to exposed tips inside ventilated slots protected by rain shields. Natural wind flow across the wick tips carries VOCs downwind. The effective dispersion radius depends on wind speed: approximately 30-50m in calm conditions (less than 3 mph), 50-100m in moderate wind (5-10 mph), and 100-200m in stronger wind (more than 10 mph). Temperature increases compound volatility, so hot summer conditions (when deer pressure is highest) produce the strongest signal.

### 3.3 Station Design: Active Version (Mesh-Integrated)

For integration with the distributed mesh deterrent network (Concept 1), an active dispensing variant adds:

| Component | Description | Qty | Unit Cost | Extended |
|-----------|-------------|-----|-----------|----------|
| Passive station (base) | As above | 1 | $35.25 | $35.25 |
| Micro-fan | 30mm axial fan (5V, 0.1W) behind wick exposure zone; activates on command to force-disperse VOCs | 1 | $3.00 | $3.00 |
| LoRa radio module | RFM95W or equivalent; receives activation commands from mesh network | 1 | $5.00 | $5.00 |
| Microcontroller | ATtiny85 or equivalent; manages fan activation timing and compound rotation (solenoid valve selects which reservoir wick is wind-exposed) | 1 | $2.00 | $2.00 |
| Mini solenoid valve | 3-way valve to expose/seal individual wick channels; allows compound blend rotation without manual intervention | 1 | $6.00 | $6.00 |
| LiFePO4 battery | 3.2V, 6000 mAh; sufficient for 6+ months at 2-3 activations per night, 30 seconds each | 1 | $8.00 | $8.00 |
| Solar cell | 2W monocrystalline panel on lid surface; maintains battery | 1 | $4.00 | $4.00 |
| Weatherproof connectors | JST connectors for battery, fan, solenoid | 3 | $0.50 | $1.50 |
| **TOTAL per active station** | | | | **$64.75** |

**Active dispensing protocol**: When the mesh network detects deer approaching a sector (via PIR, seismic, or camera node), it signals the nearest kill-site station to activate. The micro-fan runs for 30-60 seconds, actively pushing a concentrated plume of VOCs toward the approach vector. The solenoid valve can select which predator blend to dispense based on the rotation schedule stored in the microcontroller. Between activations, the station operates in passive wicking mode.

### 3.4 Visual Props Specification

| Prop | Material | Specifications | Purpose | Replacement Interval |
|------|----------|---------------|---------|---------------------|
| Fur tufts | Acrylic fiber, UV-stabilized, dyed to match white-tailed deer pelage (gray-brown summer, gray winter) | 3 tufts per station on 8" flexible galvanized wire; snagged appearance suggesting torn-out fur | Visual "remains" cue; movement in wind adds realism | 6 months (UV degradation) |
| Blood stain mat | UV-stable silicone sheet, pigmented dark red-brown; textured surface retains scent compounds applied to it | 6"x6" placed on ground adjacent to station | Visual "fresh kill" cue; also serves as secondary scent surface for decomposition volatiles | 12 months |
| Ground disturbance template | Lightweight aluminum rake (3-tine, 8" wide) included with station kit | Farmer rakes a 2'x3' area of disturbed soil adjacent to station during placement | Simulates predator dragging/feeding activity on ground; provides visual cue of recent disturbance | N/A (reusable tool) |
| Feather scatter | Synthetic feathers (chicken/turkey equivalent, dyed) in small bag; scatter 5-10 around station | Lightweight scattered debris around station perimeter | Secondary visual cue suggesting predation on birds (predators often kill multiple species) | Monthly (weather displacement) |

---

## 4. Spatial Rotation Protocol

### 4.1 Perimeter Layout for 50-Acre Block

A 50-acre block (approximately 1,476 ft x 1,476 ft if square, or more commonly a rectangular shape such as 2,200 ft x 990 ft) has a perimeter of approximately 5,900 linear feet (1,800 m).

**Station count determination**:
- Effective passive dispersion radius: 50-100m downwind (conservative: 50m in low wind)
- Required overlap for continuous perimeter coverage: stations spaced at 80-100m
- Perimeter / spacing = 1,800m / 90m = **20 station positions**
- But only 6-8 stations are active at any time (rotating among positions)

**Recommended configuration**:
- **20 marked station positions** around the perimeter (ground stakes installed permanently)
- **8 station units** that rotate among the 20 positions
- At any given time: 4-5 stations active (freshly loaded, wicks exposed), 3-4 stations dormant (wicks sealed, in storage or transit)
- Rotation moves each station to a new position every 3-5 days

### 4.2 Rotation Schedule

**Rotation philosophy**: Mimic natural predator kill frequency. In eastern US ecosystems, a resident coyote makes approximately one deer-sized kill every 7-14 days. A pack of coyotes or a cougar kills more frequently (every 3-7 days). The rotation schedule should create 1-2 new "fresh kill sites" every 3-5 days along the perimeter.

**Weekly rotation protocol**:

| Day | Action | Time Required | Who |
|-----|--------|--------------|-----|
| Monday | Move 2 stations to new positions. Refresh compound cartridges on 2 stations. Rake ground disturbance at new positions. Scatter feathers. | 20 minutes | Farm worker |
| Thursday | Move 2 different stations to new positions. Refresh compound cartridges on 2 stations. Re-apply "blood" compound to stain mats. | 20 minutes | Farm worker |
| **Weekly total** | 4 station moves, 4 cartridge refreshes | 40 minutes | Farm worker |

**Rotation rules**:
1. Never place a station in the same position two cycles in a row
2. Alternate predator species blend each time a station is refreshed (coyote -> wolf -> bobcat -> coyote)
3. Prioritize placement at identified deer entry corridors (from trail camera data) with 60% of stations near known trails and 40% distributed along remaining perimeter
4. When trail camera data shows deer testing a specific perimeter segment, move 1-2 stations to that segment within 24 hours (adaptive placement)

### 4.3 Can One Farmer Do This?

**Yes.** The protocol requires approximately 40 minutes per week total, split across two visits. Each station weighs 3-5 lbs and clips onto a pre-installed ground stake. Cartridge swaps are tool-free (press-fit). The farmer carries 2 stations and a bag of fresh cartridges in an ATV/UTV that is already used for field perimeter checks.

The key operational consideration is that handling decomposition compounds (cadaverine, putrescine) is unpleasant. The compounds have a strong foul odor even at low concentrations. Workers should wear nitrile gloves during cartridge handling. Pre-loaded sealed cartridges minimize direct exposure -- the worker simply removes the old cartridge (sealed in a zip-lock bag for disposal) and inserts a new one.

**Monthly cartridge preparation**: Cartridges can be pre-loaded in a batch once per month in a ventilated area (garage, barn with open doors). Loading 32 cartridges (8 stations x 4 weekly refreshes) takes approximately 30 minutes with a measuring syringe and pre-mixed compound solutions.

---

## 5. Anti-Habituation Analysis

### 5.1 The Core Vulnerability

The Phase 1 assessment rated Kill-Site Simulation as **MODERATE** for anti-habituation, with the critical caveat: "olfactory-only deterrence habituates in 2-6 weeks without consequence pairing." This is the single most important engineering challenge for this concept.

**Evidence on kill-site avoidance duration**:

| Study System | Avoidance Duration | Conditions | Notes |
|-------------|-------------------|------------|-------|
| Elk at wolf kill sites (Yellowstone) | 1-3 weeks post-kill | Real predator, real kill, predator periodically returns to feed | Avoidance strongest when predator scent is fresh; fades as scent dissipates |
| Deer in wolf territories (MN/WI) | Persistent spatial shift (months-years) | Ongoing predation pressure | Avoidance is maintained by occasional real predation events |
| Deer responding to predator urine stations | 2-4 weeks initial avoidance | Commercial predator urine dispensers (Plotwatcher studies) | Habituation occurs when deer encounter urine repeatedly without any aversive outcome |
| Lab rodents to TMT exposure | 2-6 weeks (continuous); 8-12 weeks (intermittent) | Blanchard et al., 2003 | Intermittent exposure with recovery periods dramatically slows habituation |
| Predator odor + decomposition odor combination | 6-12 weeks estimated | Phase 1 behavioral science ranking; multi-compound subcortical activation | Longer than single compound because of multi-pathway activation |

**Key finding**: Real kill-site avoidance in nature is maintained by the occasional reality that predation DOES occur. The kill site is not a bluff -- it is genuine evidence of a genuine threat. For an artificial kill-site system, the deer will eventually test the bluff if no real consequence ever occurs. The timeline before deer begin testing is estimated at 3-6 weeks for the most motivated (hungry, habituated) individuals, and 6-12 weeks for the average deer.

### 5.2 Compound Rotation to Delay Habituation

Rotating predator species blends exploits stimulus-specificity of olfactory habituation. Habituation to coyote scat odor does NOT generalize fully to wolf scat odor because the compound profiles are partially distinct (different ratios of PEA, TMT, skatole, and species-specific markers). Each switch resets the habituation clock partially.

**Rotation protocol**:
- Cycle through 3 predator species blends (coyote, wolf, bobcat) on a 9-day rotation (3 days per species)
- Within each species, vary the concentration by +/- 30% across stations to prevent adaptation to a specific intensity
- Every 4th cycle, introduce a "novel" blend (e.g., bear scat simulant using trimethylamine + picolines, or fisher scat simulant) to create a completely new olfactory experience

**Estimated effect**: Compound rotation extends the habituation timeline from 3-6 weeks (single compound) to 8-14 weeks (3-species rotation). This covers approximately half a growing season.

### 5.3 Concentration Escalation Protocol

The behavioral science literature on sensitization (Rescorla & Wagner, 1972; McNally et al., 2011) demonstrates that escalating stimulus intensity produces sensitization rather than habituation because each encounter exceeds the animal's prediction.

**Escalation schedule**:
- Weeks 1-3: Standard concentration (1x)
- Weeks 4-6: Elevated concentration (1.5x)
- Weeks 7-9: High concentration (2x)
- Week 10: Return to standard (1x) -- the reduction after escalation creates a "relief" period that resets the baseline
- Repeat cycle

**Estimated effect**: Concentration escalation adds 2-4 weeks to the habituation timeline by maintaining positive prediction error.

### 5.4 Consequence Pairing: The Essential Integration

**This is the most critical section of the entire proposal.**

Without consequence pairing, Kill-Site Simulation will fail as a standalone deterrent within 6-14 weeks under the most optimistic projections (and possibly within 3-4 weeks under high deer pressure). The behavioral science is unambiguous on this point: any signal-based deterrent that is never backed by genuine aversive consequences will eventually be extinguished through the prediction error learning mechanism.

**Reinforcement protocol (integrated with mesh network)**:

When Kill-Site Simulation is deployed alongside the distributed mesh deterrent network (Concept 1), consequences can be delivered at kill-site locations:

| Consequence Type | Mechanism | Cost per Event | Integration Requirement |
|-----------------|-----------|---------------|----------------------|
| Water jet (if HYDRA available) | Irrigation solenoid + directional nozzle at kill-site station | $0.01-0.05 (water + valve actuation) | Requires irrigation line within 50m of station |
| Compressed air burst | Small CO2 cartridge (paintball-size) with solenoid valve; produces loud hiss + cold blast | $0.50 per actuation | CO2 cartridge replacement monthly |
| Capsaicinoid ground pellet | Microencapsulated capsaicin pellets scattered on ground near station; rupture under hoof pressure | $0.10-0.25 per station refresh | Part of ground treatment (Concept family C) |
| Mesh node startle | Nearest mesh network nodes activate simultaneously: buzzer, LED strobe, ultrasonic | $0 (uses existing mesh hardware) | Requires Concept 1 mesh network |

**Reinforcement ratio and schedule**:

Based on the behavioral science literature (Bouton, 2004; Capaldi, 1966):

| Phase | Duration | Reinforcement Ratio | Schedule | Purpose |
|-------|----------|--------------------|---------|---------|
| Acquisition | Weeks 1-2 | 70-80% of deer encounters at kill-site stations receive a consequence | Continuous (every encounter at reinforced stations) | Establish strong CS-US association: kill-site odor = danger |
| Transition | Weeks 3-4 | 40-50% | Variable ratio (VR-2 to VR-3) | Begin partial reinforcement; activate PREE (Partial Reinforcement Extinction Effect) |
| Maintenance | Weeks 5+ | 15-25% | Variable ratio (VR-4 to VR-6) | Maintain conditioned avoidance at minimum reinforcement cost |
| Reinstatement boosts | Every 4-6 weeks | Single high-intensity event | Unpredictable | Fully restore any partially extinguished fear via the reinstatement effect (Rescorla, 2004) |

**The reinstatement effect is the key to long-term effectiveness.** Even after partial habituation to kill-site odor, a single unexpected high-intensity aversive event (e.g., water jet + full mesh node activation + compressed air burst simultaneously) at a kill-site station fully restores the conditioned fear response. This means the system only needs one strong reinforcement event every 4-6 weeks per active station to maintain effectiveness indefinitely.

### 5.5 Projected Anti-Habituation Timeline

| Configuration | Estimated Effective Duration | Confidence |
|--------------|----------------------------|------------|
| Kill-Site standalone, single compound, no rotation | 2-4 weeks | HIGH (consistent with published data) |
| Kill-Site standalone, 3-species rotation | 6-10 weeks | MODERATE |
| Kill-Site standalone, rotation + escalation | 8-14 weeks | MODERATE-LOW (extrapolated) |
| Kill-Site + mesh network startle (15-25% reinforcement) | 4-6+ months (full growing season) | MODERATE (supported by VR schedule literature) |
| Kill-Site + mesh network + water jet consequence (15-25%) | 6+ months (potentially multi-season) | MODERATE-HIGH (nociceptive pairing produces sensitization) |

**Bottom line**: Kill-Site Simulation alone is a 2-3 month deterrent. With mesh network integration and consequence pairing, it becomes a full-season deterrent component.

---

## 6. Safety and Regulatory Assessment

### 6.1 Compound Regulatory Status

| Compound | EPA Regulated? | FIFRA Registered? | OSHA PEL | FDA Status | State Wildlife Regs |
|----------|---------------|-------------------|----------|------------|-------------------|
| PEA (2-phenylethylamine) | NO | NO | None established | GRAS (naturally occurring in food) | Not regulated |
| Skatole (3-methylindole) | NO | NO | None established (treat as nuisance odor) | GRAS (fragrance use) | Not regulated |
| Indole | NO | NO | None established | GRAS (fragrance use) | Not regulated |
| Isovaleric acid | NO | NO | None established | GRAS (naturally in cheese) | Not regulated |
| TMT (trimethylthiazoline) | NO | NO | None established | Not FDA-reviewed; research chemical | Not regulated |
| Cadaverine | NO | NO | None specific; general amine guidelines (~5 ppm TWA suggested) | Not FDA-reviewed; naturally occurring | Not regulated |
| Putrescine | NO | NO | None specific; general amine guidelines (~5 ppm TWA suggested) | Not FDA-reviewed; naturally occurring | Not regulated |
| DMTS (dimethyl trisulfide) | NO | NO | None specific | GRAS (naturally in food) | Not regulated |

**Critical regulatory finding**: NONE of these compounds are regulated as pesticides under FIFRA because they are not applied to or near crops with the intent to kill or repel pests on crops. They are deployed at the field PERIMETER as area deterrents. However, if any compound were marketed with explicit pesticide claims ("repels deer from crops"), EPA could assert FIFRA jurisdiction and require registration as a biopesticide (Category 25b exemption may apply for naturally-occurring compounds).

**Recommended regulatory strategy**:
1. Deploy compounds at field perimeter only (minimum 50 ft from crop rows)
2. Market as "wildlife management scent stations" rather than "pesticide" or "repellent"
3. Seek a formal EPA 25(b) exemption opinion for the compound blend (25(b) exempts minimum-risk pesticides made from naturally-occurring ingredients from FIFRA registration)
4. Consult state departments of agriculture in target markets (many states have their own pesticide registration requirements)

### 6.2 Worker Safety

| Hazard | Exposure Route | Risk Level | Mitigation |
|--------|---------------|-----------|------------|
| Cadaverine/putrescine inhalation | Respiratory during cartridge loading | LOW-MODERATE | Load cartridges in ventilated area. Use nitrile gloves. Pre-sealed cartridge design minimizes open-air handling. |
| Cadaverine/putrescine skin contact | Dermal during cartridge handling | LOW | Nitrile gloves. Compounds are irritants but not absorbed through intact skin at relevant concentrations. |
| TMT inhalation | Respiratory during cartridge loading | LOW | Very low per-station quantity (5 mg). Even full vial spill in enclosed space is below hazardous threshold. |
| Eye irritation (any compound) | Splash during mixing/loading | LOW | Safety glasses during batch preparation. Pre-mixed solutions reduce risk. |
| Allergic sensitization | Repeated skin contact without gloves | VERY LOW | PEA and diamines can cause contact sensitization in rare cases. Glove use eliminates risk. |

**PPE requirements for cartridge preparation**: Nitrile gloves + safety glasses. Outdoors or in ventilated area. No respirator required at the concentrations used.

**PPE requirements for field station handling**: Nitrile gloves only (sealed cartridge design prevents exposure during installation/removal).

### 6.3 Crop and Soil Safety

| Concern | Assessment | Mitigation |
|---------|-----------|------------|
| Compound drift to crop rows | At 50+ ft setback from crops, airborne VOC concentrations at crop level are below 1 ppb for all compounds -- undetectable analytically and biologically insignificant | Maintain minimum 50 ft perimeter setback |
| Soil contamination from station drip | Station design includes rain shield to prevent washout. Any ground-level drip is confined to the 1 sq ft station footprint. Cadaverine and putrescine are naturally produced during all organic matter decomposition and are rapidly metabolized by soil microbes (half-life in soil: 2-6 hours) | Station base tray collects drip; natural biodegradation handles any soil contact |
| Groundwater contamination | All compounds are rapidly biodegradable. Concentrations per station are in milligrams. Even total spill of all 8 stations (approximately 10g total compound) into soil would be below detection within 24 hours due to microbial metabolism | No concern at deployment concentrations |
| Crop quality / taste effects | Zero. Compounds are deployed at perimeter, not on or near crops. Volatile concentrations at crop distance are below the limits of human detection | N/A |

### 6.4 Livestock Safety

| Animal | Exposure Pathway | Risk Assessment |
|--------|-----------------|----------------|
| Cattle on adjacent land | Airborne VOC drift across fence line | NEGLIGIBLE. Cattle are not prey species for the predators simulated; they do not have innate fear responses to coyote/wolf scat odor at the concentrations used. Cattle may show mild investigative interest but no distress. |
| Horses on adjacent land | Airborne VOC drift | LOW. Horses have stronger neophobic responses than cattle. Some individuals may show increased vigilance near stations for 1-2 days, then habituate. No physical risk. |
| Farm dogs | Direct investigation of station | LOW-MODERATE. Dogs may be attracted to predator scat compounds (investigative behavior) and could attempt to chew on station. The locking clip and mesh screen prevent ingestion. At the concentrations used, oral exposure to station compounds is non-toxic (all compounds have oral LD50 > 250 mg/kg; a 20 kg dog would need to consume >5g to reach any toxicity threshold). Visual inspection and simple training redirect dogs away from stations. |
| Farm cats | Direct investigation | NEGLIGIBLE. Cats may investigate but the compounds are non-toxic at these concentrations. |

### 6.5 Non-Target Wildlife Effects

| Species Group | Expected Effect | Concern Level |
|--------------|----------------|--------------|
| Small mammals (rabbits, voles, mice) | May show temporary avoidance of station vicinity (5-10m). Some species (voles, mice) are prey of the simulated predators and will show genuine fear response. This is a POSITIVE side effect -- small mammal deterrence reduces crop damage from rodents. | BENEFICIAL |
| Raccoons, opossums | May investigate station; locking clip prevents tampering. May show mild avoidance of decomposition volatiles. | NEGLIGIBLE |
| Birds | Negligible effect. Birds do not rely on mammalian predator kairomones for predation risk assessment (different sensory ecology). | NONE |
| Wild canids (coyotes, foxes) | May show territorial response to competing predator scat odor (scent-marking behavior). Could result in increased coyote activity at perimeter as coyotes investigate and counter-mark. This is a POTENTIAL BENEFIT -- real coyote presence reinforces the kill-site signal for deer. | POTENTIALLY BENEFICIAL |
| Turkey, pheasant | May show mild avoidance of decomposition volatiles. Effect is minor. | NEGLIGIBLE |
| Pollinator insects | No documented effect of mammalian scat compounds on bee/butterfly behavior at these concentrations. | NONE |

### 6.6 Odor Drift and Neighbor Complaints

**This is the most likely source of conflict in real-world deployment.**

Cadaverine and putrescine have extremely low human odor detection thresholds:
- Cadaverine: approximately 2 ppm (human threshold)
- Putrescine: approximately 3 ppm (human threshold)
- Skatole: approximately 0.001 ppm (human threshold -- extremely low)

**Odor dispersion modeling** (Gaussian plume approximation, open field, 5 mph wind):

| Distance from Station | Estimated Concentration (worst case, downwind) | Human Detection? | Deer Detection? |
|----------------------|------------------------------------------------|-------------------|-----------------|
| 5 m | 10-50 ppm (cadaverine+putrescine); 0.1-1 ppm (skatole) | YES -- strongly unpleasant | YES -- strong signal |
| 25 m | 1-5 ppm (cadaverine+putrescine); 0.01-0.1 ppm (skatole) | YES -- detectable, unpleasant | YES -- moderate signal |
| 50 m | 0.1-0.5 ppm (cadaverine+putrescine); 0.001-0.01 ppm (skatole) | BORDERLINE -- faint odor | YES -- detectable |
| 100 m | 0.01-0.05 ppm | NO -- below human threshold | BORDERLINE |
| 200 m | <0.005 ppm | NO | NO (for most compounds) |

**Assessment**: At 100m+ (approximately 330 ft), the odor is below human detection thresholds under most conditions. However, during temperature inversions (still, cool evening air that traps VOCs near the ground), odor can travel 200-400m before dispersing. If a neighbor's house or outdoor living area is within 200m of the field perimeter, complaints are possible during inversion events.

**Mitigation strategies**:
1. Do not place stations on the property boundary nearest occupied residences
2. Concentrate stations on the perimeter sides facing woodland/forest (where deer enter), not sides facing residences
3. Use lower concentrations of skatole (the most offensive compound to humans) near residential boundaries
4. Inform immediate neighbors before deployment; provide contact information for complaint resolution
5. Active stations (mesh-integrated) can be programmed to deactivate wind-assisted dispersion when wind direction shifts toward residences

---

## 7. Cost Model: 50-Acre Deployment

### 7.1 Standalone Deployment

| Category | Item | Qty | Unit Cost | Total | Amortization | Annual Cost |
|----------|------|-----|-----------|-------|-------------|-------------|
| **Capital - Stations** | Passive kill-site stations | 8 | $35.25 | $282.00 | 5 years | $56.40 |
| **Capital - Position Stakes** | Ground stakes for all positions | 20 | $4.00 | $80.00 | 5 years | $16.00 |
| **Capital - Tools** | Cartridge loading kit (syringes, measuring cups, mixing bottles) | 1 | $25.00 | $25.00 | 5 years | $5.00 |
| **Capital - Storage** | Lockable chemical storage box (ventilated) | 1 | $40.00 | $40.00 | 5 years | $8.00 |
| **Consumables - Compounds** | Monthly compound cartridge refills (without TMT) | 12 months | $1.20 | $14.46 | Annual | $14.46 |
| **Consumables - TMT** | TMT for wolf blend (1/3 of rotations) | 12 months | $2.67 | $32.00 | Annual | $32.00 |
| **Consumables - Props** | Fur tufts replacement (2x/year) | 48 tufts | $1.00 | $48.00 | Annual | $48.00 |
| **Consumables - Props** | Blood stain mats replacement (1x/year) | 8 mats | $2.00 | $16.00 | Annual | $16.00 |
| **Consumables - Props** | Feather scatter bags | 12 bags | $2.00 | $24.00 | Annual | $24.00 |
| **Labor** | Station rotation and maintenance (40 min/week x 26 weeks at $15/hr) | 17.3 hrs | $15.00 | $260.00 | Annual | $260.00 |
| **Labor** | Monthly cartridge preparation (30 min/month x 6 months) | 3 hrs | $15.00 | $45.00 | Annual | $45.00 |
| | | | | | | |
| **Year 1 Total** | | | | **$834.46** | | |
| **Annual Total (Yr 2-5)** | | | | | | **$524.86** |
| **5-Year TCO** | | | | | | **$2,934.00** |
| **Annual Average (5yr)** | | | | | | **$586.80** |
| **Per Acre Per Year** | | | | | | **$11.74** |

### 7.2 Mesh-Integrated Deployment (Active Stations)

| Category | Item | Qty | Unit Cost | Total | Amortization | Annual Cost |
|----------|------|-----|-----------|-------|-------------|-------------|
| **Capital - Stations** | Active kill-site stations (mesh-integrated) | 8 | $64.75 | $518.00 | 5 years | $103.60 |
| **Capital - Position Stakes** | Ground stakes for all positions | 20 | $4.00 | $80.00 | 5 years | $16.00 |
| **Capital - Tools & Storage** | (same as standalone) | - | - | $65.00 | 5 years | $13.00 |
| **Consumables** | Compounds + TMT + props (same as standalone) | - | - | $134.46 | Annual | $134.46 |
| **Consumables** | Battery replacement (every 2 years) | 4 batteries | $8.00 | $32.00 | 2 years | $16.00 |
| **Labor** | Station rotation (reduced: active stations auto-rotate compound blend, so only physical moves needed -- 25 min/week x 26 weeks) | 10.8 hrs | $15.00 | $162.50 | Annual | $162.50 |
| **Labor** | Monthly cartridge preparation | 3 hrs | $15.00 | $45.00 | Annual | $45.00 |
| | | | | | | |
| **Year 1 Total** | | | | **$1,036.96** | | |
| **Annual Total (Yr 2-5)** | | | | | | **$490.56** |
| **5-Year TCO** | | | | | | **$2,999.20** |
| **Annual Average (5yr)** | | | | | | **$599.84** |
| **Per Acre Per Year** | | | | | | **$12.00** |

### 7.3 Cost Comparison

| Configuration | $/acre/year | Within $100 Budget? | Notes |
|--------------|-------------|--------------------|----- |
| Kill-Site standalone (passive) | $11.74 | YES (88% margin) | Budget-friendly; but limited anti-habituation |
| Kill-Site standalone (active, mesh-integrated) | $12.00 | YES (88% margin) | Slightly higher capital, lower labor |
| Kill-Site + Mesh Network (Concept 1) combined | $23-35 | YES (65-77% margin) | Recommended configuration |
| Kill-Site + Mesh + one consequence mechanism | $35-55 | YES (45-65% margin) | Full anti-habituation solution |
| Full multi-layer system (Kill-Site + Mesh + Seismic + Cover Crop) | $55-80 | YES (20-45% margin) | Maximum effectiveness |

**Key insight**: Kill-Site Simulation is so inexpensive that it leaves substantial budget headroom for integration with other deterrent layers. At $12/acre/year, it consumes only 12% of the $100/acre/year budget, making it an ideal supplementary component.

---

## 8. Prototype Design and Field Trial Plan

### 8.1 Minimum Viable Prototype

The simplest version that can test the core hypothesis: "Do artificial kill-site scent stations reduce deer activity at field perimeters?"

**Prototype BOM**:

| Component | Description | Qty | Unit Cost | Total |
|-----------|-------------|-----|-----------|-------|
| HDPE containers | Repurposed 500 mL food storage containers with drilled ventilation holes | 4 | $2.00 | $8.00 |
| Cotton wicks | Cotton rope (6mm) cut to 15 cm lengths | 12 | $0.25 | $3.00 |
| Rain guards | Cut sections of corrugated plastic (yard signs) | 4 | $1.00 | $4.00 |
| Ground stakes | 12" steel tent stakes | 4 | $2.00 | $8.00 |
| PEA compound | 2-phenylethylamine, 25g bottle (Sigma-Aldrich or Amazon lab supply) | 1 | $15.00 | $15.00 |
| Skatole | 3-methylindole, 10g bottle | 1 | $12.00 | $12.00 |
| Indole | Indole, 25g bottle | 1 | $10.00 | $10.00 |
| Cadaverine | 1,5-diaminopentane, 25g bottle | 1 | $20.00 | $20.00 |
| Putrescine | 1,4-diaminobutane, 25g bottle | 1 | $25.00 | $25.00 |
| Isovaleric acid | 3-methylbutanoic acid, 100 mL bottle | 1 | $10.00 | $10.00 |
| Synthetic fur tufts | Craft store acrylic fur scraps | 1 pack | $5.00 | $5.00 |
| Red-brown fabric paint | For "blood stain" simulation on ground cloth | 1 | $5.00 | $5.00 |
| Trail cameras | Budget cellular or SD-card trail cameras for monitoring | 6 | $40.00 | $240.00 |
| SD cards + batteries | For trail cameras | 6 sets | $10.00 | $60.00 |
| Solvent (mineral oil) | Carrier solvent for compound dilution to extend evaporation time | 1 L | $5.00 | $5.00 |
| Nitrile gloves | Box of 100 | 1 | $8.00 | $8.00 |
| Zip-lock bags | For cartridge handling | 1 box | $3.00 | $3.00 |
| **TOTAL** | | | | **$441.00** |

### 8.2 Test Protocol

**Design**: Paired comparison, 2 treatment plots vs. 2 control plots.

**Site selection**: Identify a farm field with documented deer damage and trail camera evidence of regular deer activity. Select 4 segments of the field perimeter (each 200m long) with comparable deer activity levels (based on 2 weeks of pre-treatment trail camera data).

**Layout**:
- **Treatment plots** (2 segments, 200m each): Install 2 kill-site prototype stations per segment (1 station per 100m). Deploy predator scat + decomposition volatile blend. Include visual props. Rotate stations between 4 pre-marked positions within each segment every 5 days.
- **Control plots** (2 segments, 200m each): Install identical containers with wicks but filled with mineral oil only (no active compounds). Include identical visual props. Same rotation schedule (to control for disturbance effects).
- **Trail cameras**: 1 camera per 100m segment (6 cameras total -- 3 per treatment, 3 per control), positioned to monitor deer activity in a 50m band inside the field perimeter.

**Duration**: 8 weeks minimum (2 weeks pre-treatment baseline + 6 weeks treatment).

**Data collection**:
- Trail camera images reviewed daily
- Count: number of deer detections per camera per night
- Record: deer behavior at each detection (feeding, passing through, vigilance/alarm, retreat)
- Weekly: record compound cartridge consumption (weigh before and after) to verify dispensing rate

**Compound rotation**: Switch predator species blend every 5 days (coyote weeks 1-2, wolf weeks 3-4, bobcat weeks 5-6).

### 8.3 Success Criteria

| Metric | STRONG GO | CONDITIONAL GO | NO-GO |
|--------|----------|----------------|-------|
| Deer detection reduction (treatment vs. control) | >50% reduction sustained through week 6 | 30-50% reduction, OR >50% reduction in weeks 1-3 with decline to 30-50% by week 6 | <30% reduction, OR reduction drops below 20% by week 4 (rapid habituation) |
| Deer feeding behavior reduction | >60% reduction in feeding events | 35-60% reduction | <35% reduction |
| Vigilance/alarm behavior increase | >100% increase in vigilance behaviors at treatment plots | 50-100% increase | <50% increase |
| Habituation timeline | No significant decline in effectiveness through week 6 | Decline begins at week 4-5 but remains >30% reduction | Decline begins before week 3 |
| Compound consumption rate | Cartridges last 5-7 days as designed | 3-5 days (higher consumption = higher annual cost) | <3 days (cost-prohibitive evaporation rate) |

**Interpretation guidelines**:
- STRONG GO: Proceed to full 50-acre pilot with mesh network integration
- CONDITIONAL GO: Proceed to a second trial with consequence pairing (add mesh network startle at 2 of 4 treatment stations) to test whether reinforcement extends effectiveness
- NO-GO: Abandon Kill-Site Simulation as a primary concept; consider retaining cadaverine/putrescine as a supplementary scent layer for other concepts (e.g., ground treatment, mesh node scent dispensers)

### 8.4 Field Trial Timeline

| Week | Activity |
|------|----------|
| Week -2 to 0 | Site selection; install trail cameras at all 4 segments; collect baseline deer activity data |
| Week 0 | Build 4 prototype stations; prepare compound solutions; deploy treatment and control stations |
| Week 1-2 | Coyote scat blend active; refresh cartridges day 5 and day 10; collect trail camera data daily |
| Week 3-4 | Switch to wolf scat blend; refresh cartridges day 15 and day 20; analyze weeks 1-2 data |
| Week 5-6 | Switch to bobcat scat blend; refresh cartridges day 25 and day 30; analyze weeks 3-4 data |
| Week 7 | Data analysis; prepare preliminary results |
| Week 8 | Final report; GO/NO-GO decision |

---

## 9. Risk Register

### Top 5 Risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| **R1** | **Rapid habituation (< 3 weeks)**: Deer learn that kill-site stations are "bluffs" and resume normal feeding patterns before the growing season ends | MEDIUM-HIGH | HIGH (concept failure) | (1) Compound rotation protocol slows habituation. (2) Consequence pairing with mesh network is the primary mitigation -- mandatory for production deployment. (3) Field trial at week 4 checkpoint determines if standalone viability is sufficient. |
| **R2** | **Neighbor odor complaints**: Decomposition volatiles drift to adjacent properties during temperature inversions, causing nuisance complaints or regulatory action | MEDIUM | MEDIUM (operational disruption, potential cease-and-desist) | (1) Minimum 200m setback from residential structures. (2) Do not place stations on residential-facing perimeter segments. (3) Reduce skatole concentration near boundaries. (4) Proactive neighbor notification. (5) Active stations can wind-direction-gate dispersion. |
| **R3** | **Non-target attraction of real predators**: Coyotes or foxes attracted to predator scat scent stations may increase predator density at field perimeter, causing unintended livestock losses on adjacent land | LOW-MEDIUM | MEDIUM (liability, neighbor conflict) | (1) Communicate with neighboring livestock operators before deployment. (2) Monitor trail cameras for increased predator activity. (3) Station scent concentrations are below the level that would attract predators from long range (>500m). (4) If predator attraction occurs, it reinforces the kill-site signal for deer (secondary benefit), but livestock safety takes priority -- remove stations near livestock if complaints arise. |
| **R4** | **Regulatory reclassification**: EPA determines that the compound blend constitutes a "pesticide" under FIFRA, requiring registration that takes 2-3 years and costs $50,000-200,000 | LOW | HIGH (product launch delay, significant cost) | (1) Seek 25(b) exemption opinion before commercialization. (2) All primary compounds are naturally occurring and potentially qualify for minimum-risk exemption. (3) Do not make explicit "pesticide" or "repellent" claims in marketing materials. (4) Engage regulatory counsel early in the development process. |
| **R5** | **Compound degradation in field conditions**: UV exposure, rain, or temperature extremes degrade active compounds faster than anticipated, requiring unsustainable cartridge replacement frequency | MEDIUM | MEDIUM (cost overrun, labor increase) | (1) Rain shield design protects wicks from direct precipitation. (2) Mineral oil carrier solvent slows evaporation rate. (3) UV-shielded HDPE enclosure protects reservoir cartridges. (4) Field trial will measure actual consumption rate vs. design target. (5) Microencapsulation of compounds in wax or polymer beads (Phase 3 refinement) can extend cartridge life to 14+ days. |

### Additional Risks (Monitoring)

| # | Risk | Likelihood | Impact | Notes |
|---|------|-----------|--------|-------|
| R6 | Worker refusal to handle malodorous compounds | LOW-MEDIUM | LOW | Pre-sealed cartridge design minimizes exposure. Farm workers routinely handle manure, fertilizer, and pesticides. Compound odor is unpleasant but familiar to agricultural workers. |
| R7 | Raccoon/wildlife tampering with stations | MEDIUM | LOW | Locking clips and mesh screens prevent access. Heavy-gauge HDPE resists chewing. Stakes prevent tipping. Monitor during field trial. |
| R8 | Compound sourcing disruption | LOW | MEDIUM | All primary compounds have multiple suppliers. PEA, skatole, indole, and isovaleric acid are commodity chemicals with global production. TMT has fewer suppliers but is optional (wolf blend only). |
| R9 | Seasonal ineffectiveness in cold weather | MEDIUM | LOW | Reduced VOC volatility in cold temperatures (<0C) limits dispersion radius. However, deer pressure is also reduced in winter when fields are bare. System is designed for growing-season deployment (May-November). |
| R10 | Dogs consuming station compounds | LOW | LOW | Non-toxic at deployment concentrations. Locking clip prevents access. Simple owner training. |

---

## 10. Integration Architecture: Kill-Site in the Full Field Shield Stack

Kill-Site Ecology Simulation is designed as a **modular peripheral** in the Field Shield platform, not a standalone product. Its position in the full deterrent stack:

```
LAYER 4 (Consequence):  Water jets / Shock pads / Capsaicinoid ground treatment
                         |
                         | Reinforces (15-25% of encounters)
                         v
LAYER 3 (Active Alert):  Distributed Mesh Network (Concept 1)
                         - PIR/seismic detection
                         - Coordinated startle (buzzer, LED, ultrasonic)
                         - Triggers kill-site active dispersion
                         |
                         | Activates and coordinates
                         v
LAYER 2 (Olfactory):    KILL-SITE ECOLOGY SIMULATION (this concept)
                         - Passive background scent (always on)
                         - Active burst dispersion (mesh-triggered)
                         - Visual props (always visible)
                         - Spatial rotation (weekly)
                         |
                         | Supplements
                         v
LAYER 1 (Passive):      Biological Perimeter / Cover Crop Border (Concept 4)
                         - Aromatic plant barrier (wormwood, catmint)
                         - Physical thorny hedge (Osage orange, long-term)
                         - Always present, zero energy
```

**Data flow for integrated operation**:
1. Deer approaches field perimeter (detected by mesh network PIR/seismic node)
2. Mesh network identifies approach vector and nearest kill-site station
3. Kill-site station receives LoRa command: activate fan for 60 seconds, select compound blend based on rotation schedule
4. Concentrated VOC plume directed toward approaching deer
5. Variable-ratio schedule determines whether to also activate consequence layer:
   - 75-85% of encounters: scent + mesh startle only (buzzer, LED, ultrasonic from nearest nodes)
   - 15-25% of encounters: scent + mesh startle + consequence (water jet, capsaicinoid, or compressed air burst)
6. Trail camera and PIR data logged; system records whether deer retreated (success) or continued (failure)
7. If failure rate exceeds 30% over a 7-day window, system automatically increases consequence reinforcement ratio by 10%

---

## 11. Conclusion and Recommendations

### Summary Assessment

Kill-Site Ecology Simulation is a scientifically grounded, exceptionally cost-effective ($12/acre/year), and operationally simple concept that exploits one of the strongest innate spatial avoidance behaviors in deer. It is the highest novelty-to-cost ratio concept in the Field Shield portfolio.

However, it has a fundamental limitation that cannot be engineered away: **olfactory deterrence without consequence pairing habituates within weeks.** This is not a design flaw -- it is a biological reality that applies to ALL signal-based deterrents. The kill-site compound combination delays habituation longer than most olfactory deterrents (estimated 6-12 weeks vs. 2-4 weeks for simple predator urine), but it cannot maintain season-long effectiveness alone.

### Recommendations

1. **DO build and field-test the prototype** ($441 budget). The core hypothesis is testable within 6 weeks. Even a CONDITIONAL GO result justifies integration with the mesh network.

2. **DO NOT develop as a standalone product.** Kill-Site Simulation should be a module/peripheral within the distributed mesh network platform (Concept 1). The mesh network provides detection, coordination, and consequence delivery that Kill-Site cannot provide alone.

3. **Prioritize the consequence pairing protocol.** The reinforcement schedule (15-25% VR pairing with genuine aversive consequence) is what transforms Kill-Site from a 6-week deterrent into a season-long deterrent. Without it, the concept is a temporary measure.

4. **Use TMT sparingly.** TMT is the only expensive compound. The wolf scat blend (containing TMT) should be used in only 1 of every 3 rotation cycles. PEA, skatole, indole, and the diamines (cadaverine, putrescine) are all cheap commodity chemicals.

5. **Address the neighbor odor issue proactively.** This is the most likely source of real-world problems. Proactive communication, strategic station placement (away from residences), and wind-direction gating (active stations) mitigate the risk.

6. **Seek EPA 25(b) exemption opinion early.** The regulatory status of the compound blend as a non-pesticide should be formally confirmed before commercial launch.

7. **Consider microencapsulation in Phase 3.** Encapsulating compounds in wax or polymer microspheres that slowly release VOCs over 14-21 days would reduce cartridge replacement frequency from weekly to biweekly, cutting labor costs by 40-50%.

---

## References

- Babikova, Z., et al. (2013). Underground signals carried through common mycelial networks warn neighbouring plants of aphid attack. *Ecology Letters*, 16(7), 835-843.
- Blanchard, D.C., et al. (2003). Risk assessment as an evolved threat detection and analysis process. *Neuroscience & Biobehavioral Reviews*, 27(7), 585-610.
- Bouton, M.E. (2004). Context and behavioral processes in extinction. *Learning & Memory*, 11(5), 485-494.
- Capaldi, E.J. (1966). Partial reinforcement: A hypothesis of sequential effects. *Psychological Review*, 73(5), 459-477.
- Ferrero, D.M., et al. (2011). Detection and avoidance of a carnivore odor by prey. *Proceedings of the National Academy of Sciences*, 108(27), 11235-11240.
- Fortin, D., et al. (2005). Wolves influence elk movements: behavior shapes a trophic cascade in Yellowstone National Park. *Ecology*, 86(5), 1320-1330.
- Garcia, J. & Koelling, R.A. (1966). Relation of cue to consequence in avoidance learning. *Psychonomic Science*, 4(1), 123-124.
- Kobayakawa, K., et al. (2007). Innate versus learned odour processing in the mouse olfactory bulb. *Nature*, 450(7169), 503-508.
- Laundre, J.W., et al. (2001). Wolves, elk, and bison: reestablishing the "landscape of fear" in Yellowstone National Park. *Canadian Journal of Zoology*, 79(8), 1401-1409.
- Mech, L.D., et al. (2001). *Wolves: Behavior, Ecology, and Conservation*. University of Chicago Press.
- McNally, G.P., et al. (2011). Placing prediction into the fear circuit. *Trends in Neurosciences*, 34(6), 283-292.
- Nelson, M.E. & Mech, L.D. (1986). Deer population in the central Superior National Forest, 1967-1985. *USDA Forest Service Research Paper NC-271*.
- Rescorla, R.A. (2004). Spontaneous recovery. *Learning & Memory*, 11(5), 501-509.
- Rescorla, R.A. & Wagner, A.R. (1972). A theory of Pavlovian conditioning: variations in the effectiveness of reinforcement and nonreinforcement. In *Classical Conditioning II*, pp. 64-99.
- Wisman, A. & Shrira, I. (2015). The smell of death: evidence that putrescine elicits threat management mechanisms. *Frontiers in Psychology*, 6, 1274.
- Woolf, C.J. & Salter, M.W. (2000). Neuronal plasticity: increasing the gain in pain. *Science*, 288(5472), 1765-1768.

---

*Phase 2 Engineering Proposal: Concept 3 -- Kill-Site Ecology Simulation*
*Field Shield Innovation Engine -- Full-Spectrum Deer Deterrence*
*Session: 2026-02-15*
*Engineering Team: AgTech Domain Expert + Safety Engineer + Operations Specialist*
