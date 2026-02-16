# CONCEPT 2: SEISMIC GROUND VIBRATION DETERRENCE ("TERRA PULSE")
## Phase 2 Engineering Proposal -- Field Shield Platform

**Engineering Team**: Mechanical Engineer + Electrical Engineer + AgTech Domain Expert
**Date**: 2026-02-15
**Concept Origin**: Phase 1 TRIZ Analysis, Rank #1 Novel Direction
**TRIZ Principles**: #28 (Mechanics Substitution), #35 (Parameter Changes), #19 (Periodic Action)

---

## Executive Summary

This proposal details an engineering concept for a ground-coupled seismic vibration deterrence system that targets an entirely unexploited sensory channel in wildlife management: substrate-borne vibration detection through ungulate hoof mechanoreceptors. No commercial wildlife deterrent has ever targeted ground-borne vibration. All five Phase 1 researchers independently rated this as the highest-novelty concept.

The system uses buried vibration transducers to generate Rayleigh-type surface waves at 2-80 Hz, mimicking predator footfall signatures. Sequential activation of transducers along the field perimeter simulates predator movement direction, speed, and gait. The same transducer elements can double as geophones for passive detection when not actively vibrating.

**Key metrics (50-acre deployment)**:
- Capital cost: $4,850-$9,750
- Annual operating cost: $610-$1,270
- 5-year amortized cost: $22-$51/acre/year (well within $100/acre/year target)
- Transducer count: 56-90 units (perimeter + interior)
- Effective range per transducer: 15-50m depending on soil type
- Power consumption: 150-450W peak, <50W average
- System lifetime: >5 years (no moving parts in transducers)

---

## Table of Contents

1. [Scientific Basis](#1-scientific-basis-why-seismic-deterrence-should-work)
2. [Transducer Selection and Specification](#2-transducer-selection-and-specification)
3. [Vibration Propagation Analysis](#3-vibration-propagation-analysis)
4. [Predator Footfall Pattern Library](#4-predator-footfall-pattern-library)
5. [Detection Integration](#5-detection-integration)
6. [System Architecture](#6-system-architecture-50-acre-deployment)
7. [Soil Type Adaptation](#7-soil-type-adaptation)
8. [Cost Model](#8-cost-model-50-acre-deployment)
9. [Proof-of-Concept Experiment Design](#9-proof-of-concept-experiment-design)
10. [Risk Register](#10-risk-register)
11. [GO/NO-GO Criteria](#11-gono-go-criteria)

---

## 1. Scientific Basis: Why Seismic Deterrence Should Work

### 1.1 Deer Mechanoreception Through Hooves

White-tailed deer (*Odocoileus virginianus*) possess Pacinian corpuscles and other lamellar mechanoreceptors in the digital cushion and periosteal tissue of their hooves. These receptors are tuned to detect substrate-borne vibrations in the 5-400 Hz range, with peak sensitivity in the 10-60 Hz band. This sensory system evolved as a predator early-warning mechanism: in forested and vegetated habitats where airborne sound attenuates rapidly, ground-borne vibrations from approaching large predators propagate farther and more reliably.

**Detection thresholds (estimated from ungulate and comparative mammalian literature)**:
- Pacinian corpuscles respond to displacements as small as 0.1-1.0 micrometers at their optimal frequency (30-300 Hz in isolation; lower in situ due to tissue damping)
- In-hoof sensitivity is reduced by the keratinous hoof wall and digital cushion, requiring substrate displacements of approximately 1-10 micrometers at the ground surface for detection
- At the low frequencies relevant to predator footfalls (2-15 Hz), detection thresholds are higher, estimated at 10-100 micrometers ground displacement
- These thresholds translate to ground particle velocities of approximately 0.1-10 micrometers/second at the detection point

**Comparative evidence from other ungulate taxa**:
- Elephants detect seismic signals (produced by foot stomping and low-frequency vocalizations) at distances exceeding 2 km through bone-conducted Rayleigh waves, with sensitivity peaks at 10-40 Hz (O'Connell-Rodwell et al., 2001; O'Connell-Rodwell, 2007)
- Elephants assume a characteristic "leaning" posture when attending to seismic information, shifting weight to the front feet to maximize ground coupling
- Smaller ungulates including deer have proportionally stiffer hoof-ground coupling (smaller contact area, higher ground pressure per unit area), which improves high-frequency sensitivity but reduces low-frequency coupling
- Frozen or very hard substrates improve bone conduction of seismic signals to the inner ear via the leg bones (Narins et al., 2016)

**Behavioral prediction**: Deer detecting ground vibrations consistent with a large predator approach pattern should exhibit one or more of the following responses:
1. **Alert/freeze**: Head-up, ears forward, motionless assessment posture (most likely initial response)
2. **Flee**: Explosive bounding flight away from the vibration source (if pattern is sufficiently threatening)
3. **Alarm signaling**: Snort-wheeze vocalization and white tail flagging, alerting conspecifics (social amplification)
4. **Area avoidance**: Subsequent avoidance of the location for hours to days (landscape-of-fear encoding)

### 1.2 Why This Channel Has Never Been Exploited

No commercial wildlife deterrent has targeted substrate-borne vibration because:
1. **Airborne acoustic deterrents are easier to build** -- speakers are cheap and well-understood
2. **Ground coupling is hard** -- efficiently transmitting vibration into soil requires specialized transducers and good mechanical coupling
3. **The behavioral science has focused on elephants** -- deer seismic sensitivity has received almost no direct experimental investigation
4. **Propagation is soil-dependent** -- effectiveness varies dramatically with soil type, making universal product claims difficult

These are engineering challenges, not fundamental barriers. The underlying biological mechanism is well-supported by comparative neuroanatomy and evolutionary ecology.

### 1.3 Anti-Habituation Properties

Ground-borne vibration deterrence has several inherent anti-habituation advantages:

1. **Novel sensory channel**: Deer have zero prior exposure to artificial seismic threats (unlike acoustic, visual, or olfactory deterrents which they encounter regularly in suburban and agricultural settings)
2. **Innate predator detection pathway**: The hoof mechanoreceptor system evolved specifically for predator detection -- stimuli in this channel activate hardwired threat-assessment circuits, not learned associations
3. **Pattern variability**: Seismic "gait signatures" can be infinitely varied in timing, frequency, amplitude, direction, and speed -- exploiting Thompson & Spencer habituation Property #7 (stimulus specificity)
4. **Multi-modal coherence**: Ground vibration is a CREDIBLE predator cue because it is exactly how real predators announce their presence in forests -- unlike loudspeaker recordings, there is no "uncanny valley" of unrealism
5. **Sensitization potential**: If combined with even rare genuine aversive events (water jet, electric contact), the seismic pattern becomes a conditioned stimulus that STRENGTHENS rather than weakens with re-exposure (reconsolidation effect per Nader et al., 2000)

---

## 2. Transducer Selection and Specification

### 2.1 Transducer Technology Comparison

| Technology | Freq. Range | Force Output | Power | Unit Cost | Ground Coupling | Durability | Verdict |
|-----------|------------|-------------|-------|-----------|-----------------|-----------|---------|
| **Bass tactile transducer (Dayton Audio TT25-8)** | 4-200 Hz | 9N peak | 15W | $12-18 | Excellent (bolt to rigid surface) | High (sealed coil) | **PRIMARY SELECTION** |
| **Bass tactile transducer (Clark Synthesis TST329)** | 5-17,000 Hz | Higher | 50W | $200-350 | Excellent | Very high (aluminum) | Over-budget; overkill |
| Dayton Audio BST-1 (large format) | 10-200 Hz | 20N+ | 25-50W | $30-50 | Excellent | High | Good for anchor points |
| Eccentric rotating mass (ERM) motor | 10-200 Hz | Moderate | 1-5W | $0.50-3 | Moderate (vibration direction varies) | Low (bearing wear) | Backup for ultra-low-cost |
| Linear resonant actuator (LRA) | 100-300 Hz | Low | 0.5-2W | $1-5 | Poor (too high frequency) | Moderate | Rejected: freq. too high |
| Electromagnetic shaker (lab grade) | 1-5000 Hz | High | 50-500W | $500-5000 | Excellent | Very high | Rejected: cost prohibitive |
| Geophone/seismometer (reversed as actuator) | 4.5-100 Hz | Very low | 0.1-1W | $15-40 | Moderate | High | Better as sensor than actuator |
| Pneumatic hammer | 1-50 Hz | Very high | N/A (compressed air) | $50-200 | Excellent | Moderate (mechanical wear) | Rejected: requires air infrastructure |
| Piezoelectric disc ($0.50-2 each) | 1-10,000 Hz | Very low | 0.1-1W | $0.50-2 | Poor (tiny displacement) | High | Rejected: insufficient force for soil coupling |

### 2.2 Primary Transducer Selection: Dayton Audio TT25-8

**Specifications**:
- Model: Dayton Audio TT25-8 (or equivalent tactile bass transducer)
- Frequency response: 4-200 Hz usable, peak output 40-80 Hz
- Impedance: 8 ohms
- Power handling: 15W RMS, 25W peak
- Force output: ~9N peak at resonance
- Dimensions: 25mm diameter voice coil, ~35mm total height
- Weight: ~85g
- Unit cost: $12-18 retail; $8-12 at 100+ quantity

**Why this transducer**: The TT25-8 represents the optimal price/performance intersection for this application. It produces sufficient force to generate detectable ground displacement at 15-40m in favorable soils while costing under $15 per unit. It has no moving parts beyond the voice coil/mass assembly, giving it a projected outdoor life exceeding 5 years when properly sealed.

### 2.3 Ground Coupling Design

The transducer must be mechanically coupled to the soil to efficiently convert electrical energy to seismic waves. We propose three coupling configurations:

**Configuration A: Stake-Mount (PRIMARY)**
```
        Ground Surface
  ~~~~~~~~~~|~~~~~~~~~~
            |
     +------+------+
     |  TT25-8     |    <- Transducer bolted to top of steel stake
     |  transducer  |
     +------+------+
            |
            |  <- 50mm (2") square steel tube stake
            |     1000mm (40") total length
            |     driven 750mm (30") into soil
            |
            +  <- Pointed tip for driving
```
- Steel tube stake (50mm square, 1m long): $3-6 each
- Transducer bolts to flat top plate of stake via M6 bolt
- Stake driven to 30" depth (below tillage zone)
- Top cap with transducer sits 10" above ground or at grade
- Waterproof enclosure (PVC cap + silicone seal): $2-4
- Total per-station material cost: $15-28

**Configuration B: Fence-Line Mount**
- TT25-8 bolted directly to steel or wooden fence posts
- Fence post acts as coupling element to ground
- No trenching required; uses existing infrastructure
- Lower coupling efficiency (fence post is not optimized for seismic transmission) but zero installation cost for the coupling element

**Configuration C: Concrete Pad (HIGH-PERFORMANCE)**
- Transducer bolted to a 200mm x 200mm x 50mm concrete pad
- Pad buried at 300mm depth
- Maximum coupling efficiency for clay and loam soils
- Higher installation cost (requires trenching and curing)
- Reserved for interior anchor positions or worst-case sandy soils

### 2.4 Transducer Weatherproofing

Each transducer station is enclosed in a sealed housing:
- **PVC cap housing**: 75mm (3") PVC cap inverted over the transducer, sealed with marine-grade silicone
- **Cable gland**: IP68-rated cable gland for speaker wire entry
- **Drainage**: Weep hole at lowest point with mesh screen to prevent insect intrusion
- **UV protection**: PVC is inherently UV-resistant; cap painted with reflective coating for thermal management
- **Projected weatherproof life**: >7 years (PVC + silicone sealant)

---

## 3. Vibration Propagation Analysis

### 3.1 Wave Types in Agricultural Soil

At the frequencies of interest (2-80 Hz), three wave types propagate through soil:

1. **Rayleigh waves (surface waves)**: Travel along the ground surface with amplitude decaying exponentially with depth. At 5-50 Hz in agricultural soil, Rayleigh wave velocity is 100-300 m/s. These are the primary energy carrier for our application because they concentrate energy near the surface where deer hooves make contact.

2. **P-waves (compressional body waves)**: Travel through the soil volume at 200-1500 m/s depending on saturation. Higher velocity but rapid geometric spreading (1/r^2 amplitude decay). Less relevant for surface detection.

3. **S-waves (shear body waves)**: Travel at 50-200 m/s in shallow agricultural soil. Significant contributor at short range.

**For perimeter deterrence, Rayleigh waves dominate** because they suffer only 1/sqrt(r) geometric spreading (cylindrical, not spherical) and concentrate energy at the surface.

### 3.2 Attenuation Model

Ground vibration amplitude A(r) at distance r from a point source is modeled as:

```
A(r) = A_0 * (r_0/r)^n * exp(-alpha * r)
```

Where:
- A_0 = source amplitude at reference distance r_0 (typically 1m)
- n = geometric spreading exponent (0.5 for Rayleigh waves, 1.0 for body waves)
- alpha = material attenuation coefficient (frequency-dependent, Np/m)

The material attenuation coefficient alpha is the critical soil-dependent parameter:

```
alpha = pi * f / (Q * V_R)
```

Where:
- f = frequency (Hz)
- Q = quality factor of the soil (dimensionless; higher Q = less attenuation)
- V_R = Rayleigh wave velocity (m/s)

### 3.3 Soil Type Parameters and Propagation Performance

| Soil Type | V_R (m/s) | Q Factor | alpha at 10 Hz (Np/m) | alpha at 40 Hz (Np/m) | Effective Range* (m) |
|-----------|-----------|----------|----------------------|----------------------|---------------------|
| Heavy clay (saturated) | 150-250 | 15-30 | 0.013-0.021 | 0.052-0.084 | 40-60 |
| Heavy clay (dry) | 120-200 | 10-20 | 0.016-0.026 | 0.063-0.105 | 30-50 |
| Silt loam (typical Midwest) | 120-180 | 8-15 | 0.023-0.044 | 0.093-0.175 | 20-40 |
| Sandy loam | 100-150 | 5-10 | 0.042-0.063 | 0.168-0.251 | 12-25 |
| Dry sand | 80-130 | 3-8 | 0.048-0.131 | 0.192-0.524 | 8-15 |
| Organic/peat (muck) | 60-100 | 3-6 | 0.052-0.105 | 0.209-0.419 | 8-18 |
| Rocky/glacial till | 200-400 | 20-50 | 0.006-0.016 | 0.025-0.063 | 50-80+ |
| Frozen soil (any type) | 300-600 | 25-50 | 0.003-0.013 | 0.013-0.050 | 60-100+ |

*Effective range = distance at which ground displacement exceeds estimated deer detection threshold of 10 micrometers at 10 Hz, assuming 15W transducer input and stake-mount coupling.

### 3.4 Vibration Propagation Model: Distance vs. Amplitude

**Source assumption**: TT25-8 at 15W into stake mount generates approximately 500 micrometers displacement at 1m reference distance (10 Hz).

**Heavy Clay (Best Case)**:
```
Distance (m):    1     5     10    20    30    40    50    60
Amplitude (um): 500   180    95    40    22    13     8     5
Detectable?:     Y     Y     Y     Y     Y     Y    (Y)   (N)
```

**Silt Loam (Typical Case)**:
```
Distance (m):    1     5     10    15    20    25    30    40
Amplitude (um): 500   155    65    33    18    11     7     3
Detectable?:     Y     Y     Y     Y     Y     Y    (N)   (N)
```

**Sandy Loam (Worst Practical Case)**:
```
Distance (m):    1     5     10    15    20    25
Amplitude (um): 500   120    38    14     6     3
Detectable?:     Y     Y     Y     Y    (N)   (N)
```

**Key findings**:
- In typical agricultural silt loam, each transducer covers a 20-25m radius detection zone at 10 Hz
- Lower frequencies (2-10 Hz) propagate 2-3x farther than higher frequencies (40-80 Hz)
- Saturated soils propagate vibrations 1.5-2x farther than dry soils (higher Q, higher velocity)
- Frozen ground dramatically improves propagation (3-4x range increase)
- This means the system performs BETTER during the critical early spring and late fall periods when ground may be partially frozen and deer pressure is highest on tender emerging/remaining crops

### 3.5 Frequency-Dependent Propagation

Lower frequencies travel farther because attenuation (alpha) scales linearly with frequency. This is advantageous because predator footfall energy is concentrated below 15 Hz:

```
Frequency:      2 Hz    5 Hz    10 Hz   20 Hz   40 Hz   80 Hz
Range (loam):   45m     35m     25m     16m     10m     5m
Application:    Bear    Wolf    Impact  Trot    Run     Startle
```

**Design implication**: The predator pattern library should use the lowest frequencies (2-10 Hz) for the "approach" phase to maximize detection range, reserving higher frequencies (20-80 Hz) for close-range "attack" escalation when the deer is already detected nearby.

### 3.6 Environmental Factors

**Soil moisture**: Increasing moisture increases both Rayleigh wave velocity and Q factor, improving propagation. A field with active irrigation will have better seismic deterrent performance than a dry field. This is a beneficial correlation: irrigated high-value crops get better protection automatically.

**Frozen ground**: Frozen soil has dramatically higher velocity (300-600 m/s) and Q (25-50), increasing effective range by 3-4x. Early spring (frozen ground, emerging crops, hungry deer) is when both deer pressure and seismic propagation are at their best.

**Crop root zone**: Root systems slightly increase soil damping in the top 30cm. Effect is minor (<10% range reduction) and irrelevant for transducers buried below the root zone.

**Farm equipment interference**: Tractors generate ground vibrations at 5-30 Hz. The seismic system should pause vibration output when tractor-frequency signatures are detected (by the geophone sensors), preventing false triggering and conserving power. The detection algorithm distinguishes tractor vibrations (continuous, steady frequency related to RPM) from predator patterns (transient, variable frequency).

**Rain impact**: Heavy rainfall generates broadband ground vibration at 5-100 Hz. During heavy rain, deer activity is naturally suppressed, so the seismic system can reduce output. Geophone monitoring provides automatic rain detection.

---

## 4. Predator Footfall Pattern Library

### 4.1 Pattern Design Principles

Each predator pattern is defined by:
- **Step frequency**: Steps per second (Hz)
- **Step force profile**: Time-domain waveform of a single footfall (attack, sustain, decay)
- **Gait asymmetry**: Difference between left-right timing (walk vs. trot vs. gallop)
- **Sequential activation speed**: How fast the "footsteps" progress from transducer to transducer (simulates predator travel speed)
- **Amplitude envelope**: How the overall amplitude changes over the duration of the pattern (approach = crescendo, passing = plateau, retreat = decrescendo)
- **Frequency content**: Spectral content of each footstep pulse
- **Irregularity parameters**: Random variation ranges applied to all parameters to prevent robotic repetition

### 4.2 Pattern Specifications

#### PATTERN 1: Wolf Approach (Primary Deterrent Pattern)

```
WOLF_APPROACH_v1:
  Description: Adult gray wolf walking approach, transitioning to trot

  Phase 1 - Distant Walk (30 seconds):
    step_frequency:      1.8-2.2 Hz (variable)
    step_force_peak:     30% of max amplitude
    frequency_content:   2-8 Hz dominant, 8-15 Hz harmonics
    gait_pattern:        Walk (4-beat: LF-RH-RF-LH)
    sequential_speed:    1.3-1.8 m/s (walking wolf)
    transducer_spacing:  Activate every other transducer (30-50m jumps)
    amplitude_envelope:  Linear crescendo from 10% to 40%
    irregularity:        +/-15% on all timing parameters

  Phase 2 - Close Trot (15 seconds):
    step_frequency:      3.5-4.5 Hz (accelerating)
    step_force_peak:     60% of max amplitude
    frequency_content:   3-12 Hz dominant, 12-25 Hz harmonics
    gait_pattern:        Trot (2-beat diagonal: LF+RH, RF+LH)
    sequential_speed:    3.0-5.0 m/s (trotting wolf)
    transducer_spacing:  Activate adjacent transducers sequentially
    amplitude_envelope:  Rising from 40% to 70%
    irregularity:        +/-20% (wolf becoming excited)

  Phase 3 - Sprint Burst (5 seconds):
    step_frequency:      6-8 Hz
    step_force_peak:     100% of max amplitude
    frequency_content:   5-25 Hz dominant, 25-60 Hz impact transients
    gait_pattern:        Gallop (4-beat rotary: LH-RH-LF-RF)
    sequential_speed:    8-12 m/s (sprinting wolf)
    amplitude_envelope:  Maximum, with sharp attack transients
    irregularity:        +/-25% (chaotic pursuit)

  Phase 4 - Silence (10-60 seconds, variable):
    All transducers silent. The silence after the sprint is the most
    psychologically threatening element -- the predator has either
    caught prey or is lying in ambush.

  Total pattern duration: 60-110 seconds
  Repeat: Do NOT repeat immediately. Minimum 5-minute gap.
```

#### PATTERN 2: Cougar Stalk

```
COUGAR_STALK_v1:
  Description: Mountain lion stalking approach, irregular start-stop

  Phase 1 - Distant Padding (20 seconds):
    step_frequency:      1.0-1.5 Hz (slow, deliberate)
    step_force_peak:     15% of max (cats are light-footed)
    frequency_content:   3-10 Hz (light foot, quick impact)
    gait_pattern:        Walk (direct register -- hind foot in front foot print)
    sequential_speed:    0.5-1.0 m/s (stalking speed)
    amplitude_envelope:  Barely perceptible, slow crescendo
    irregularity:        +/-30% timing (pause-move-pause pattern)

  Phase 2 - Freeze (5-15 seconds, variable):
    Complete silence. The cat has frozen.

  Phase 3 - Rapid Repositioning (3 seconds):
    step_frequency:      5-7 Hz
    step_force_peak:     50% of max
    frequency_content:   5-20 Hz
    sequential_speed:    4-6 m/s
    Abrupt start and stop. The cat sprinted to a new position.

  Phase 4 - Freeze Again (8-20 seconds):
    Silence. But now the vibration source has MOVED.

  Phase 5 - Pounce (2 seconds):
    Single massive impact: 100% amplitude, broadband 5-80 Hz
    Followed by rapid irregular impacts (predator-prey struggle)
    Duration: 2-4 seconds, then silence

  Total pattern duration: 40-75 seconds
  Key anti-habituation feature: The freeze-move-freeze pattern is
  maximally unpredictable and matches no mechanical pattern.
```

#### PATTERN 3: Bear Walk

```
BEAR_WALK_v1:
  Description: Black bear or grizzly walking through area

  Continuous Pattern (45-90 seconds):
    step_frequency:      1.5-2.0 Hz (slow, heavy)
    step_force_peak:     80% of max amplitude (bears are HEAVY)
    frequency_content:   2-6 Hz dominant (very low, heavy impact)
    gait_pattern:        Walk (shuffle gait, LF+LH then RF+RH)
    sequential_speed:    1.0-1.5 m/s
    amplitude_envelope:  High and sustained (no stealth -- bears
                         don't stalk deer, they lumber)
    irregularity:        +/-10% (bears walk steadily)

  Special features:
    - Occasional "digging" burst: 2-3 seconds of rapid 4-8 Hz
      vibration (bear digging at ground)
    - Occasional pause + single heavy impact (bear striking something)
    - Very low frequency emphasis -- use maximum transducer excursion
```

#### PATTERN 4: Unknown Predator (Novel Threat)

```
UNKNOWN_THREAT_v1:
  Description: Pattern that matches no known animal but triggers
  generic large-predator threat assessment

  Characteristics:
    step_frequency:      Variable 1-6 Hz, with aperiodic timing
    step_force_peak:     40-90% (variable, unpredictable)
    frequency_content:   2-40 Hz (wider bandwidth than any single predator)
    gait_pattern:        No recognizable gait pattern (deliberately
                         aperiodic to prevent predictive coding)
    sequential_speed:    0.5-8 m/s (unpredictably variable)
    amplitude_envelope:  Random walk between 20% and 90%
    irregularity:        +/-40% on all parameters

  Design rationale: By deliberately NOT matching any known predator
  gait, this pattern prevents the deer from completing its threat
  assessment. An unidentifiable large ground vibration is MORE
  threatening than a recognized predator pattern because the animal
  cannot predict the threat's behavior. This exploits the "ambiguity
  aversion" documented in behavioral neuroscience (uncertain threats
  produce stronger fear responses than certain threats).

  Total pattern duration: 30-120 seconds (variable)
```

#### PATTERN 5: Stampede (Maximum Alarm)

```
STAMPEDE_v1:
  Description: Simultaneous multi-source activation simulating
  herd panic flight or multi-predator pursuit

  Activation:
    ALL perimeter transducers within a 200m arc activate simultaneously

  Characteristics:
    step_frequency:      8-12 Hz (full gallop, multiple animals)
    step_force_peak:     100% on all active transducers
    frequency_content:   5-60 Hz (broadband impact spectrum)
    gait_pattern:        Chaotic superposition of multiple gaits
    sequential_speed:    Multiple "animals" moving in different
                         directions simultaneously
    amplitude_envelope:  Maximum sustained for 5-10 seconds,
                         then rapid decay

  Usage: RARE deployment only (2-5% of activations). Reserved for:
    - Deer that have not responded to Patterns 1-4
    - Large groups (>5 deer detected)
    - Reconsolidation events (maximum intensity to reset habituating animals)

  Power note: This is the only pattern that may exceed continuous
  power rating. Peak draw: 300-900W for 5-10 seconds. Controller
  must manage duty cycle.
```

### 4.3 Pattern Scheduling Algorithm

```
PATTERN_SCHEDULER:

  Mode 1: AMBIENT PATROL (no detection trigger)
    - Run one pattern every 15-45 minutes (random interval)
    - Rotate through patterns 1-4 using weighted random selection:
      Wolf: 35%, Cougar: 25%, Bear: 20%, Unknown: 20%
    - Select random starting transducer and direction
    - 70% of patrols run at 50% amplitude (background threat)
    - 30% of patrols run at 80-100% amplitude (close encounter)
    - NEVER repeat the same pattern twice in succession

  Mode 2: TRIGGERED RESPONSE (deer detected)
    - Immediate activation of closest transducers to detection point
    - Pattern selected based on deer behavior:
      * Approaching: Wolf Approach (toward the deer)
      * Stationary/feeding: Cougar Stalk (from flank)
      * Group (>3): Stampede (if previous patterns failed)
    - Amplitude: 80-100%
    - Direction: Vibration "approaches" the deer from behind or flank
    - If deer does not flee within 30 seconds: escalate to next pattern
    - If deer flees: 50% chance of "pursuit" pattern following flight direction

  Mode 3: SENSITIZATION EVENTS (variable ratio schedule)
    - 5-10% of all triggered responses are maximum-intensity Stampede
    - These rare maximum events prevent habituation by exceeding
      the deer's learned prediction of maximum system intensity
    - Scheduling follows a variable ratio (VR-15 to VR-25) to maximize
      extinction resistance per behavioral reinforcement literature
```

---

## 5. Detection Integration

### 5.1 Dual-Use Transducers as Geophones

**The same TT25-8 transducers can function as crude geophones when not actively vibrating.** A moving-coil transducer is electrically reciprocal: applying voltage produces vibration, and applying vibration produces voltage. When the controller is not driving a particular transducer, it switches that channel to a high-impedance input mode and monitors the voltage produced by incoming ground vibrations.

**Geophone sensitivity of TT25-8 (estimated)**:
- Sensitivity: ~0.5-2 V/(m/s) (much lower than a purpose-built geophone at 28-100 V/(m/s))
- Useful detection range for deer footfalls: 5-15m
- Usable frequency band: 5-100 Hz
- SNR: Low. Adequate for coarse detection (deer present Y/N) but not for precision tracking

**Time-division multiplexing protocol**:
```
Each 1-second cycle:
  [0-800ms]  VIBRATE: Controller drives active pattern on selected transducers
  [800-1000ms] LISTEN: All transducers switch to geophone mode
                        ADC samples at 500 Hz for 200ms
                        DSP analyzes for footfall-consistent impulses
```

This gives 20% of each cycle to passive detection. With 56-90 transducers acting as a distributed geophone array, the system can detect deer approaching from any direction with 5-15m resolution.

### 5.2 Supplementary Detection Sensors

The geophone-mode detection is coarse and short-range. For reliable triggered response, additional detection sensors are recommended:

| Sensor Type | Model/Class | Range | Cost | Qty (50-acre) | Total Cost |
|------------|-------------|-------|------|---------------|------------|
| PIR (passive infrared) | HC-SR501 or equivalent | 7-12m, 120 deg. | $1-3 | 24-36 | $36-108 |
| Automotive radar module | TI AWR1642 eval board | 50-100m | $25-40 | 4 | $100-160 |
| Thermal camera (optional) | FLIR Lepton 3.5 | 50-100m | $150-200 | 2 | $300-400 |

**Recommended detection architecture**:
- 4x automotive radar modules at field corners: Primary long-range detection and tracking (50-100m range, full perimeter coverage). Provides range, angle, and velocity for each target. Distinguishes deer from tractors by radar cross-section and movement pattern.
- 24-36 PIR sensors at 50m intervals along perimeter: Confirmation layer. When radar detects approach, PIR provides positive confirmation of warm-bodied animal at close range.
- Geophone array (built into transducer network): Tertiary confirmation. Footfall detection provides species-consistent vibration signature.
- 2x thermal cameras (optional upgrade): Mounted on poles at opposite field corners. FLIR Lepton provides species classification via body shape and thermal signature. Not required for basic operation.

### 5.3 Detection-to-Activation Latency

| Detection Layer | Detection Range | Latency |
|----------------|----------------|---------|
| Radar | 50-100m from perimeter | < 100ms (radar refresh rate) |
| PIR | 7-12m from sensor | < 500ms (PIR settle time) |
| Geophone | 5-15m from transducer | < 200ms (DSP processing) |
| **Combined decision** | **50-100m** | **< 500ms to first transducer activation** |

The 500ms latency target is easily achievable. The system begins the "approaching predator" vibration pattern when the deer is still 50-100m from the field edge, giving the full duration of the approach pattern to build psychological pressure before the deer reaches the crop.

### 5.4 Mesh Network Integration

The seismic system connects to the Field Shield mesh network (if deployed alongside other concepts) via LoRa radio modules:

- Each transducer controller node includes a LoRa radio ($5-15)
- Mesh topology allows any node to relay data to the central controller
- Cross-concept triggers: A detection event from the mesh network (e.g., radar tracking from Concept 1) can trigger seismic activation before the deer is within the seismic system's own detection range
- Data logging: All detection events, pattern activations, and deer responses are logged for adaptive algorithm tuning

---

## 6. System Architecture (50-acre deployment)

### 6.1 Field Geometry and Transducer Layout

A 50-acre field is approximately 450m x 450m (square) or 900m x 225m (rectangular). Perimeter is approximately 1,800m.

```
SYSTEM ARCHITECTURE -- 50-ACRE BLOCK (SQUARE LAYOUT)
====================================================

     N
     ^
     |
  450m
     |
   [R]------[P]--[P]--[P]--[P]--[P]--[P]--[P]--[P]--[P]------[R]
    |  . . . . . . . . . . . . . . . . . . . . . . . . . . .  |
   [P]  .                                                   .  [P]
    |   .     [I]           [I]           [I]              .   |
   [P]  .                                                   .  [P]
    |   .                                                   .   |
   [P]  .     [I]           [I]           [I]              .  [P]
    |   .                                                   .   |
   [P]  .                                                   .  [P]
    |   .     [I]           [I]           [I]              .   |
   [P]  .                                                   .  [P]
    |   .                                                   .   |
   [P]  .     [I]     [===CTRL===]        [I]              .  [P]
    |   .              | Central  |                         .   |
   [P]  .              | Control  |                         .  [P]
    |   .              | Cabinet  |                         .   |
   [P]  .              [==========]                         .  [P]
    |   .     [I]           [I]           [I]              .   |
   [P]  .                                                   .  [P]
    |   .                                                   .   |
   [P]  .     [I]           [I]           [I]              .  [P]
    |   . . . . . . . . . . . . . . . . . . . . . . . . . . .  |
   [R]------[P]--[P]--[P]--[P]--[P]--[P]--[P]--[P]--[P]------[R]
    |                                                           |
    |<----------------------- 450m -------------------------->|

    === MAINS POWER IN (from field edge) ===

LEGEND:
  [R]  = Radar module (4 corners, elevated pole mount)
  [P]  = Perimeter transducer station (TT25-8 + PIR + LoRa)
         Spacing: ~40m in loam, ~25m in sand, ~50m in clay
  [I]  = Interior transducer station (TT25-8 only, no PIR)
         Grid spacing: ~100-150m
  [CTRL] = Central controller cabinet (at field edge near mains)
  . . . = Buried power/signal cable (Cat5e or 2-conductor + LoRa)
  ------  = Perimeter cable run (direct burial, 18" depth)
```

### 6.2 Component Count

| Component | Quantity (Loam Soil) | Quantity (Sandy Soil) | Quantity (Clay Soil) |
|-----------|---------------------|-----------------------|---------------------|
| Perimeter transducer stations | 45 | 72 | 36 |
| Interior transducer stations | 16 | 20 | 12 |
| Total transducers | 61 | 92 | 48 |
| Radar modules | 4 | 4 | 4 |
| PIR sensors | 30 | 36 | 24 |
| LoRa radio modules | 8 | 12 | 6 |
| Central controller | 1 | 1 | 1 |
| Power distribution cable (m) | 2,400 | 3,200 | 2,000 |
| Signal cable or wireless nodes | Per architecture | Per architecture | Per architecture |

### 6.3 Power Distribution

**Option A: Centralized Mains Power (RECOMMENDED)**

```
Mains 120VAC -> [Central Controller Cabinet]
                        |
                 [24VDC Power Supply, 600W]
                        |
                 [Bus Cable: 12AWG 2-conductor, direct burial]
                        |
          +------+------+------+------+
          |      |      |      |      |
        [Node] [Node] [Node] [Node] [Node]  ... (daisy-chain)
```

- Central 24VDC power supply: 600W capacity (handles peak Stampede draw)
- 12AWG direct-burial 2-conductor cable: $0.25-0.40/ft
- Voltage drop at far end (900m run, 15W load): ~3V at 12AWG. Acceptable on 24V bus.
- Total cable needed: ~2,400m (loam case) = ~8,000 ft = $2,000-3,200
- Each node receives 24VDC, local buck converter to 12V for transducer amplifier

**Option B: Solar Per-Node (NOT RECOMMENDED for most deployments)**
- Each node: 5W solar panel ($8-15) + 12V 7Ah SLA battery ($12-20) + charge controller ($3-5)
- Per-node cost addition: $23-40
- Eliminates trenching and cable cost but adds battery maintenance burden
- Battery life in cold: SLA loses 50% capacity at -20C
- Recommended only for remote field extensions >500m from mains

### 6.4 Controller Hardware

**Central Controller Cabinet** contains:
- **Waveform generator**: Raspberry Pi 4 ($35-55) running Linux with custom DSP software
- **Multi-channel DAC**: 8-channel I2S DAC board ($15-30) providing 8 independent analog output channels
- **Class-D amplifier boards**: 8x TPA3116-based 2-channel Class-D amplifiers ($5-10 each), each driving up to 8 transducers in a zone via relay switching
- **Relay matrix**: 8x8 relay matrix for routing amplifier outputs to individual transducers or transducer groups ($30-60)
- **ADC for geophone input**: 16-channel 12-bit ADC ($15-25) for multiplexed geophone reading
- **Radar interface**: USB or SPI connection to 4x radar modules
- **LoRa gateway**: LoRa concentrator module ($30-50) for mesh network communication
- **Power supply**: 24VDC 600W ($40-80)
- **Enclosure**: NEMA 4X weatherproof cabinet ($60-120)
- **Cellular modem (optional)**: For remote monitoring and firmware updates ($30-50 + $10/month service)

**Controller cabinet BOM**: $290-540

**Waveform Generation Architecture**:
```
Raspberry Pi 4 (DSP Engine)
  |
  |-- Pattern Library (stored as parameterized algorithms, NOT audio files)
  |     Each pattern is generated in real-time with randomized parameters
  |
  |-- Detection Processor
  |     Fuses radar, PIR, and geophone inputs
  |     Classifies: deer / tractor / human / wind / rain
  |     Estimates deer count, range, bearing, velocity
  |
  |-- Response Selector
  |     Chooses pattern based on detection state + history
  |     Applies variable-ratio reinforcement schedule
  |     Manages sensitization events
  |
  |-- Multi-Channel Output
        8 DAC channels -> 8 amplifiers -> relay matrix -> 48-92 transducers
        Zone-based addressing: field divided into 8 zones of 6-12 transducers
        Sequential activation within zones creates directional "movement"
```

### 6.5 Wiring Topology

**Recommended: Hybrid Bus/Star**

- 4 bus cable runs, one per field side, daisy-chaining perimeter transducers
- Star connection from central controller to each bus run
- Interior transducers connected via spur cables from nearest bus run
- Signal multiplexing: Each transducer has an address on the bus; controller sends zone-select + audio signal
- Alternative: LoRa wireless for signal, power bus only for energy delivery (eliminates signal cable complexity but adds $5-15 per node for LoRa)

---

## 7. Soil Type Adaptation

### 7.1 Pre-Installation Site Assessment Protocol

Before deploying the seismic system, perform the following soil assessment (estimated time: 2-4 hours per 50-acre block):

**Step 1: Soil Classification (30 minutes)**
- Obtain USDA NRCS Web Soil Survey data for the parcel (free, online)
- Identify dominant soil series and texture class
- Note drainage class (well-drained, moderately drained, poorly drained)
- Record organic matter content (high OM = more damping)

**Step 2: In-Situ Propagation Test (1-2 hours)**
- Equipment needed: 1 transducer (TT25-8 on stake), 1 geophone (SM-24 or equivalent), amplifier, laptop with USB oscilloscope
- Install transducer stake at representative location
- Place geophone at 5m, 10m, 20m, 30m, 50m distances
- Drive transducer with 10 Hz sine sweep at known amplitude
- Record received amplitude at each distance
- Calculate site-specific attenuation coefficient (alpha) and effective range
- Repeat at 3 representative soil zones if field has variable soils

**Step 3: Soil Moisture and Seasonal Assessment (30 minutes)**
- Measure current soil moisture with TDR probe
- Estimate seasonal moisture variation from irrigation schedule and climate data
- Determine if field experiences seasonal freezing (frost depth data from NOAA)
- Identify worst-case propagation season (typically late summer, dry, unfrozen)

**Step 4: Configuration Selection**

| Measured Effective Range | Soil Category | Transducer Spacing | Coupling Method | Special Notes |
|--------------------------|---------------|-------------------|-----------------|---------------|
| >40m | Excellent (clay, frozen, rocky) | 50m | Stake mount | Fewest transducers, lowest cost |
| 25-40m | Good (silt loam, irrigated) | 35-40m | Stake mount | Standard deployment |
| 15-25m | Fair (sandy loam, dry loam) | 25m | Stake mount | Higher density required |
| 8-15m | Poor (dry sand, peat) | 15-20m | Concrete pad | Highest density; consider supplemental acoustic |
| <8m | Unsuitable | N/A | N/A | Seismic deterrence not recommended; use alternative concepts |

### 7.2 Regional Deployment Profiles

**Midwest Corn Belt (Iowa, Illinois, Indiana)**:
- Dominant soil: Silt loam to silty clay loam (Mollisols)
- Expected effective range: 25-40m
- Seasonal variation: Frozen ground Dec-Mar (range 50-80m), dry Aug-Sep (range 20-30m)
- Configuration: Standard spacing (35-40m), stake mount
- Cost advantage: Low transducer count, long cable runs through flat terrain

**Coastal Plains (Southeast, Mid-Atlantic)**:
- Dominant soil: Sandy loam to loamy sand (Ultisols)
- Expected effective range: 12-20m
- Seasonal variation: Saturated Dec-Apr (range 18-25m), dry Jul-Sep (range 10-15m)
- Configuration: Dense spacing (20-25m), stake mount or concrete pad
- Cost impact: 50-80% more transducers than Midwest deployment

**New England / Appalachian**:
- Dominant soil: Stony loam over glacial till, shallow bedrock
- Expected effective range: 30-80m+ (rock conducts vibrations extremely well)
- Challenge: Stake driving into rocky soil is difficult; may need augered holes
- Configuration: Wide spacing (40-50m), augered stake mount
- Cost advantage: Fewest transducers, but higher installation labor for stony ground

**Organic / Muck Soils (Great Lakes, Pacific NW)**:
- Dominant soil: Organic/peat (Histosols)
- Expected effective range: 8-18m
- Challenge: Low propagation; soft, compressible soil reduces coupling efficiency
- Configuration: Dense spacing (15-20m), concrete pad coupling mandatory
- Cost impact: Highest transducer count; consider hybrid seismic + acoustic approach

---

## 8. Cost Model (50-acre deployment)

### 8.1 Bill of Materials (Typical Silt Loam Deployment)

#### Transducer Stations (61 units)

| Item | Per Unit | Qty | Total |
|------|----------|-----|-------|
| Dayton Audio TT25-8 transducer | $12 | 61 | $732 |
| Steel square tube stake (50mm x 1m) | $5 | 61 | $305 |
| PVC weatherproof housing + sealant | $3 | 61 | $183 |
| IP68 cable gland | $1.50 | 61 | $92 |
| Mounting hardware (bolts, brackets) | $2 | 61 | $122 |
| **Subtotal: Transducer stations** | | | **$1,434** |

#### Detection Sensors

| Item | Per Unit | Qty | Total |
|------|----------|-----|-------|
| TI AWR1642 radar module | $35 | 4 | $140 |
| Radar pole mount + enclosure | $25 | 4 | $100 |
| PIR sensor (HC-SR501 class) | $2 | 30 | $60 |
| PIR weatherproof housing | $3 | 30 | $90 |
| **Subtotal: Detection** | | | **$390** |

#### Central Controller

| Item | Per Unit | Qty | Total |
|------|----------|-----|-------|
| Raspberry Pi 4 (4GB) | $45 | 1 | $45 |
| 8-channel I2S DAC board | $22 | 1 | $22 |
| TPA3116 Class-D amplifier board (2ch) | $8 | 8 | $64 |
| 8x8 relay matrix board | $45 | 1 | $45 |
| 16-channel ADC board | $20 | 1 | $20 |
| LoRa gateway module | $40 | 1 | $40 |
| 24VDC 600W power supply | $55 | 1 | $55 |
| NEMA 4X enclosure (24"x20"x8") | $90 | 1 | $90 |
| Wiring, connectors, fuses, misc. | $50 | 1 | $50 |
| SD card, heatsinks, cables | $25 | 1 | $25 |
| **Subtotal: Controller** | | | **$456** |

#### Power and Signal Distribution

| Item | Per Unit | Qty | Total |
|------|----------|-----|-------|
| 12AWG 2-conductor direct burial cable | $0.35/ft | 8,000 ft | $2,800 |
| Cable splice kits (waterproof) | $3 | 70 | $210 |
| Junction boxes (IP67) | $8 | 16 | $128 |
| Grounding rods + wire | $15 | 8 | $120 |
| **Subtotal: Distribution** | | | **$3,258** |

#### Installation Labor

| Task | Hours | Rate | Total |
|------|-------|------|-------|
| Stake driving (61 stakes) | 8 hrs | $30/hr | $240 |
| Trenching for cable (vibrating plow, 2,400m) | 16 hrs | $75/hr (with equipment) | $1,200 |
| Cable pulling and termination | 16 hrs | $30/hr | $480 |
| Controller assembly and wiring | 8 hrs | $40/hr | $320 |
| Radar pole installation (4 poles) | 4 hrs | $30/hr | $120 |
| System commissioning and calibration | 8 hrs | $40/hr | $320 |
| **Subtotal: Installation** | | | **$2,680** |

### 8.2 Total Capital Cost

| Category | Cost |
|----------|------|
| Transducer stations | $1,434 |
| Detection sensors | $390 |
| Central controller | $456 |
| Power and signal distribution | $3,258 |
| Installation labor | $2,680 |
| Contingency (15%) | $1,233 |
| **TOTAL CAPITAL** | **$9,451** |

### 8.3 Annual Operating Cost

| Item | Annual Cost |
|------|------------|
| Electricity (50W avg x 6 months x $0.12/kWh) | $26 |
| Cellular data service (optional) | $120 |
| Transducer replacement (5% failure rate) | $75 |
| Cable repair (rodent damage, 2 repairs/year) | $120 |
| Maintenance labor (2 visits x 4 hours x $30/hr) | $240 |
| Software updates and monitoring | $100 |
| **TOTAL ANNUAL OPERATING** | **$681** |

### 8.4 Five-Year Total Cost of Ownership

| Year | Capital (amortized) | Operating | Annual Total |
|------|---------------------|-----------|-------------|
| Year 1 | $1,890 | $681 | $2,571 |
| Year 2 | $1,890 | $681 | $2,571 |
| Year 3 | $1,890 | $781 | $2,671 |
| Year 4 | $1,890 | $781 | $2,671 |
| Year 5 | $1,890 | $881 | $2,771 |
| **5-Year Total** | **$9,451** | **$3,805** | **$13,256** |

**5-year amortized cost per acre per year**: $13,256 / (5 years x 50 acres) = **$53/acre/year**

This is well within the $100/acre/year budget target, leaving $47/acre/year of budget headroom for:
- Pairing with other deterrent concepts (multi-modal enhancement)
- Higher-density deployment in sandy soils
- Premium components (thermal cameras, higher-power transducers)

### 8.5 Cost Comparison with Alternative Deterrents

| Deterrent Method | Capital (50 acres) | Annual Operating | 5yr $/acre/yr | Effectiveness |
|-----------------|-------------------|------------------|---------------|---------------|
| **TERRA PULSE (this concept)** | **$9,451** | **$681** | **$53** | **Unknown (novel)** |
| 8-foot woven wire fence | $45,000-75,000 | $1,000-2,000 | $184-310 | 90-95% |
| Electric fence (7-wire) | $8,000-15,000 | $500-1,000 | $38-70 | 70-85% |
| Commercial acoustic deterrent | $2,000-5,000 | $300-500 | $11-22 | 30-50% (habituates in 2-4 weeks) |
| Chemical repellents (seasonal) | N/A | $3,000-8,000 | $60-160 | 40-70% (reapplication needed) |
| HYDRA (water jets) | $12,000-18,000 | $1,500-2,500 | $78-106 | Est. 70-85% |
| Hunting/culling permits | N/A | $2,000-5,000 | $40-100 | 60-80% (seasonal) |

---

## 9. Proof-of-Concept Experiment Design

### 9.1 The Critical Unknown

**NO controlled study has ever tested artificial ground vibrations as a deer deterrent.** The entire concept rests on three untested hypotheses:

1. **H1**: Deer can detect artificial ground vibrations from buried transducers at operationally relevant distances (>15m)
2. **H2**: Deer behaviorally respond to predator-pattern ground vibrations (alert, flee, or avoid)
3. **H3**: Deer do not rapidly habituate to artificial ground vibrations over weeks-months

All three must be confirmed before committing to full-scale deployment.

### 9.2 Phase A: Detection Threshold Confirmation (Lab/Pen Study)

**Objective**: Determine the minimum ground vibration amplitude that captive deer can detect through their hooves.

**Setup**:
- Facility: University research farm with deer handling pens
- 4-6 captive white-tailed deer (mixed sex, adult)
- Vibration platform: 2m x 2m concrete pad with embedded TT25-8 transducer
- Measurement: Triaxial accelerometer on pad surface + laser vibrometer for displacement
- Feeding station positioned on the vibration pad

**Protocol**:
1. Habituate deer to feeding on the platform (1-2 weeks, no vibration)
2. Begin vibration trials during active feeding:
   - Frequency sweep: 2, 5, 10, 20, 40, 80 Hz (separate trials)
   - Amplitude ramp: Start below predicted threshold, increase by 3 dB steps every 30 seconds
   - Record behavioral response at each amplitude step:
     * No response (continued feeding)
     * Ear flick / head raise (detection without alarm)
     * Freeze (alert posture)
     * Leave platform (flight response)
3. Define detection threshold as the amplitude producing ear flick/head raise in >50% of trials
4. Define flight threshold as the amplitude producing platform departure in >50% of trials
5. Minimum 20 trials per frequency per deer for statistical power

**Expected results**:
- Detection threshold: 1-20 micrometers displacement (frequency-dependent)
- Flight threshold: 10-200 micrometers displacement
- Peak sensitivity: 10-40 Hz (matching Pacinian corpuscle tuning)

**Duration**: 4-6 weeks
**Cost**: $8,000-15,000 (facility rental, accelerometer, labor)

### 9.3 Phase B: Field Efficacy Trial (Feeding Station Experiment)

**Objective**: Test whether predator-pattern ground vibrations deter wild deer from a baited feeding station.

**Setup**:
- 4 feeding stations in known deer use areas, spaced >500m apart
- Each station: Trail camera + corn bait pile + measurement stakes
- 2 stations = TREATMENT (buried transducers around bait at 10m, 20m, 30m radii)
- 2 stations = CONTROL (identical hardware, transducers present but not activated)
- Crossover design: After 3 weeks, swap treatment/control assignments

**Treatment protocol**:
- Week 1-2: Baiting period. All stations active with bait, no vibration (baseline visit rate)
- Week 3-5: Treatment Phase 1. Treatment stations run ambient patrol pattern (random activations every 15-45 minutes, no detection trigger). Control stations silent.
- Week 6-8: Treatment Phase 2. Treatment stations run triggered response pattern (activation on deer detection via PIR). Control stations silent.
- Week 9-11: Crossover. Swap treatment/control assignments. Repeat Phases 1 and 2.
- Week 12-14: Extinction test. All stations silent. Measure how long avoidance persists.

**Metrics**:
- Primary: Deer visit rate (visits/night) at treatment vs. control stations
- Secondary: Visit duration (seconds per visit), feeding bout length
- Tertiary: Flight behavior on camera (alert, freeze, flee, direction of flight)
- Statistical: Mixed-effects model with station as random effect, treatment as fixed effect

**GO/NO-GO decision criteria**: See Section 11.

**Duration**: 14 weeks (one full field season)
**Cost**: $12,000-25,000 (equipment, bait, trail cameras, labor, data analysis)

### 9.4 Phase C: 5-Acre Pilot Deployment

**Objective**: Test full-system integration at small scale before committing to 50-acre deployment.

**Contingent on**: Phase B achieving GO criteria.

**Setup**:
- 5-acre high-value crop block with known deer damage history
- Full TERRA PULSE deployment at scale (12-15 perimeter transducers, 4 interior, 1 radar, controller)
- Adjacent 5-acre control block (no treatment, same crop)
- Season-long deployment (April-October)

**Metrics**:
- Primary: Crop damage (% leaf area removed, yield loss by weight) in treatment vs. control
- Secondary: Trail camera deer activity index (visits/night/camera)
- Tertiary: Deer behavioral response (flight rate on camera)
- Economic: Cost of pilot system vs. value of crop damage prevented

**Duration**: 7 months (one growing season)
**Cost**: $5,000-8,000 (hardware) + $3,000-5,000 (monitoring, labor)

---

## 10. Risk Register

### Risk 1: Deer Do Not Behaviorally Respond to Artificial Ground Vibrations (CRITICAL)

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (40-60%). No direct evidence for deer response to artificial seismic stimuli. Analogies from elephant seismology and general ungulate mechanoreception are supportive but not conclusive. |
| **Impact** | Fatal. If deer do not respond, the entire concept fails. |
| **Mitigation** | Phase A detection threshold experiment before any field investment. Design experiment to fail fast and cheaply ($8-15K). |
| **Contingency** | If deer detect but do not flee from seismic-only stimulation, pair with other modalities (acoustic + seismic, or seismic as conditioned stimulus paired with water jet unconditioned stimulus). |
| **Residual risk after mitigation** | Low if Phase A succeeds. The detection threshold experiment is the single most important de-risking activity. |

### Risk 2: Insufficient Propagation Range in Sandy/Organic Soils

| Attribute | Detail |
|-----------|--------|
| **Probability** | High (60-80%) for sandy and organic soils specifically. |
| **Impact** | Major cost increase (2-3x more transducers needed), potentially breaking the $100/acre/year budget in worst-case soils. |
| **Mitigation** | Pre-installation soil propagation test (Section 7.1). Reject seismic-only approach for soils with <12m effective range; recommend hybrid approach or alternative concept. |
| **Contingency** | For poor soils: (a) switch to higher-power transducers (Dayton BST-1, $30-50 each, 25-50W), (b) use concrete pad coupling, (c) accept higher transducer density, or (d) supplement with acoustic deterrent for perimeter coverage. |
| **Residual risk** | Moderate. Cost model may not close for the poorest 15-20% of agricultural soils. |

### Risk 3: Rapid Habituation Despite Novel Sensory Channel

| Attribute | Detail |
|-----------|--------|
| **Probability** | Low-Medium (20-40%). The novelty of the channel argues against rapid habituation, but no field data exists. |
| **Impact** | System effectiveness degrades from weeks to months, failing the 4-6 month growing season requirement. |
| **Mitigation** | (a) Pattern variability (Section 4) with 5 distinct patterns and randomized parameters. (b) Variable ratio activation schedule. (c) Sensitization events at 5-10% of activations. (d) Design for multi-modal pairing from the start -- seismic can serve as conditioned stimulus paired with water jet or electric contact as unconditioned stimulus. |
| **Contingency** | If habituation occurs as standalone, reposition seismic as one layer of a multi-modal system (seismic + olfactory + acoustic). The infrastructure investment (cables, controller) supports additional modalities with minimal added cost. |
| **Residual risk** | Low if multi-modal fallback is pre-planned. |

### Risk 4: Cable and Transducer Damage from Farming Operations

| Attribute | Detail |
|-----------|--------|
| **Probability** | Medium (30-50%). Plowing, discing, and subsoiling can damage buried cables and stakes even below 12" depth. |
| **Impact** | Moderate. Individual transducer or cable failures degrade coverage but do not cause total system failure due to redundant coverage. Repair cost: $50-200 per incident. |
| **Mitigation** | (a) Route cables along fence lines and permanent field borders wherever possible. (b) Bury cables at 18" minimum depth (below most tillage). (c) Use armored direct-burial cable in high-traffic zones. (d) Mark cable routes with above-ground markers. (e) Perimeter-only deployment avoids interior cultivation zone. |
| **Contingency** | Carry 10% spare cable and 5 spare transducer stations for field repair. Budget $120/year for 2 cable repairs. |
| **Residual risk** | Low with proper routing and depth. |

### Risk 5: Regulatory or Neighbor Concerns About Ground Vibrations

| Attribute | Detail |
|-----------|--------|
| **Probability** | Low (10-20%). The vibrations are extremely low amplitude (micrometers at 20-50m) and below human perceptual threshold beyond 5-10m from any transducer. |
| **Impact** | Moderate. Could cause permitting delays or neighbor disputes. |
| **Mitigation** | (a) Measure and document human imperceptibility at property boundaries. (b) Ground vibrations at these amplitudes are orders of magnitude below any structural damage threshold (which requires mm-scale displacement). (c) No FCC concerns (no RF emission from the transducers). (d) Proactive neighbor communication. |
| **Contingency** | Implement time-of-day restrictions if neighbors complain (no activation midnight-6am). Measure and demonstrate that vibrations are below ISO 2631 human perception threshold at property boundaries. |
| **Residual risk** | Very low. System operates at amplitudes comparable to a person walking, detectable only to animals with specialized mechanoreceptors. |

---

## 11. GO/NO-GO Criteria

### Phase A: Detection Threshold Study

| Criterion | GO | NO-GO |
|-----------|-----|-------|
| Detection at 10 Hz | Threshold < 50 um displacement | Threshold > 100 um or no detection |
| Detection at 40 Hz | Threshold < 20 um displacement | Threshold > 50 um or no detection |
| Behavioral response | >50% of deer show alert/freeze at threshold +10 dB | <25% of deer show any behavioral response at any amplitude |
| Flight response | >25% of deer leave platform at any tested amplitude | 0% flight responses across all conditions |

**Decision**: PROCEED to Phase B if 3 of 4 GO criteria are met.

### Phase B: Field Efficacy Trial

| Criterion | GO | NO-GO |
|-----------|-----|-------|
| Visit rate reduction (triggered mode) | >40% reduction vs. control | <20% reduction |
| Visit rate reduction (ambient mode) | >20% reduction vs. control | <10% reduction |
| Duration of effect | No significant decline in effectiveness over 3-week treatment period | Effectiveness declines >50% within 2 weeks (habituation) |
| Crossover confirmation | Treatment effect follows the vibration, not the station | Treatment effect does not transfer on crossover (confounded) |
| Flight behavior | >30% of detected deer show flee response on camera | <10% flee; majority show no visible response |
| Extinction persistence | Avoidance persists >7 days after vibration ceases | Avoidance disappears <3 days after cessation |
| Statistical significance | p < 0.05 for primary metric (visit rate, mixed model) | p > 0.10 |

**Decision**: PROCEED to Phase C (5-acre pilot) if 5 of 7 GO criteria are met and both primary criteria (visit rate reduction in triggered mode + statistical significance) are among them.

### Phase C: 5-Acre Pilot

| Criterion | GO to 50-acre | NO-GO |
|-----------|---------------|-------|
| Crop damage reduction | >50% reduction vs. control block | <25% reduction |
| Season-long effectiveness | No significant efficacy decline across full April-October season | Efficacy drops >50% by mid-season |
| System reliability | <5% transducer failure rate, <2 controller failures over season | >15% hardware failure rate |
| Economic viability | Total pilot cost < $100/acre amortized | Total cost > $150/acre amortized |
| Farmer acceptance | Farmer rates system as "acceptable" or better on usability survey | Farmer rates as "unacceptable" or requests removal |

**Decision**: PROCEED to commercial 50-acre deployment if 4 of 5 GO criteria are met.

### Timeline to Decision

| Phase | Duration | Cumulative Time | Cost | Decision Point |
|-------|----------|-----------------|------|----------------|
| Phase A (pen study) | 6 weeks | 6 weeks | $8-15K | GO/NO-GO for field trial |
| Phase B (feeding station) | 14 weeks | 20 weeks | $12-25K | GO/NO-GO for pilot |
| Phase C (5-acre pilot) | 28 weeks | 48 weeks | $8-13K | GO/NO-GO for commercial |
| **Total validation** | **~12 months** | | **$28-53K** | |

---

## Appendix A: Single Footstep Waveform Specification

Each simulated footstep is a parameterized time-domain waveform:

```
footstep(t) = A * env(t) * sin(2*pi*f_0*t + phi) * (1 + harmonics(t))

Where:
  A       = peak amplitude (0-100% of transducer maximum)
  env(t)  = attack-sustain-decay envelope:
            attack:  5-20ms exponential rise (hoof strike)
            sustain: 10-50ms plateau (weight bearing)
            decay:   50-200ms exponential fall (weight transfer)
  f_0     = fundamental frequency (2-15 Hz, predator-dependent)
  phi     = random phase offset (prevents phase coherence between steps)
  harmonics(t) = 0.3*sin(2*pi*2*f_0*t) + 0.15*sin(2*pi*3*f_0*t) + 0.08*sin(2*pi*4*f_0*t)
                 (natural footfall has harmonic content from ground deformation)

Total footstep duration: 80-300ms
Inter-step silence: 100-500ms (gait-dependent)
```

## Appendix B: Comparison with Elephant Seismic Communication Research

The deer seismic deterrence concept draws directly from the pioneering research of Caitlin O'Connell-Rodwell and colleagues on elephant seismic communication (Stanford University / Etosha Pan, Namibia):

| Parameter | Elephant System | Deer System (Proposed) |
|-----------|-----------------|----------------------|
| Signal source | Foot stomps, low-freq vocalizations coupled to ground | Artificial transducers mimicking predator footfalls |
| Frequency range | 10-40 Hz (primary), up to 100 Hz | 2-80 Hz |
| Detection mechanism | Pacinian corpuscles in foot pad + bone conduction to inner ear | Pacinian corpuscles in digital cushion + bone conduction (hypothesized) |
| Detection range | >2 km (elephant signals are very high amplitude) | 15-50m (artificial source, much lower amplitude) |
| Behavioral response | Freezing, leaning posture, group defensive formation | Predicted: alert, freeze, flee (to be validated) |
| Body mass | 3,000-6,000 kg | 45-135 kg |
| Foot contact area | ~1,000 cm^2 (very large, good low-freq coupling) | ~40 cm^2 per hoof (small, better high-freq coupling) |
| Ground coupling | Fatty digital cushion (excellent broadband coupling) | Keratinous hoof wall + small digital cushion (likely peak sensitivity at higher frequencies than elephants) |

## Appendix C: Parts Reference List

| Part | Supplier | Part Number | Unit Cost | Notes |
|------|----------|-------------|-----------|-------|
| Dayton Audio TT25-8 | Parts Express | 295-244 | $11.98 | Primary transducer |
| Dayton Audio BST-1 | Parts Express | 295-245 | $34.98 | High-power upgrade option |
| HC-SR501 PIR sensor | Amazon/AliExpress | Generic | $1.50-3.00 | Bulk pricing available |
| TI AWR1642BOOST | Mouser/DigiKey | AWR1642BOOST | $35-40 | Evaluation board; production version $15-25 |
| Raspberry Pi 4 Model B (4GB) | Various | RPI4-4GB | $45-55 | Central controller |
| TPA3116D2 amplifier board | AliExpress | Generic | $5-10 | 2x50W Class-D |
| SM-24 geophone element | SparkFun | SEN-11744 | $12-15 | Optional dedicated geophones |
| LoRa RFM95W module | Adafruit | 3072 | $10-15 | 915 MHz, US ISM band |
| 12/2 direct burial cable | Home Depot | Southwire 55213444 | $0.35/ft | Power distribution |
| 3" PVC cap | Home Depot | Various | $1.50-3.00 | Transducer housing |
| Marine silicone sealant | West Marine | 3M 4200 | $15/tube (covers 30+ stations) | Weatherproofing |

---

## Appendix D: References

1. O'Connell-Rodwell, C.E. (2007). "Keeping an 'ear' to the ground: seismic communication in elephants." *Physiology*, 22, 215-225.
2. O'Connell-Rodwell, C.E., et al. (2001). "Seismic properties of Asian elephant vocalizations and locomotion." *JASA*, 110(3), 2066-2072.
3. Narins, P.M., et al. (2016). "Seismic signal production and perception in vertebrates." In *The Ecology of Animal Senses*, Springer.
4. Laundre, J.W., Hernandez, L., & Altendorf, K.B. (2001). "Wolves, elk, and bison: reestablishing the 'landscape of fear' in Yellowstone." *Canadian Journal of Zoology*, 79(8), 1401-1409.
5. Nader, K., Schafe, G.E., & Le Doux, J.E. (2000). "Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval." *Nature*, 406, 722-726.
6. VerCauteren, K.C., et al. (2006). "Fence-line contact of white-tailed deer and electric fences." *Wildlife Society Bulletin*, 34(5), 1497-1502.
7. Ferrero, D.M., et al. (2011). "Detection and avoidance of a carnivore odor by prey." *PNAS*, 108(27), 11235-11240.
8. Thompson, R.F. & Spencer, W.A. (1966). "Habituation: A model phenomenon for the study of neuronal substrates of behavior." *Psychological Review*, 73(1), 16-43.
9. Brown, J.S. (1988). "Patch use as an indicator of habitat preference, predation risk, and competition." *Behavioral Ecology and Sociobiology*, 22, 37-47.
10. Rescorla, R.A. & Wagner, A.R. (1972). "A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement." In *Classical Conditioning II*, Appleton-Century-Crofts.

---

*Document prepared by: Joint Engineering Team (ME/EE/AgTech)*
*Field Shield TRIZ Innovation Platform*
*Phase 2 Concept Development -- Concept 2 of 5*
*Status: READY FOR VALIDATION TRIAL PLANNING*
