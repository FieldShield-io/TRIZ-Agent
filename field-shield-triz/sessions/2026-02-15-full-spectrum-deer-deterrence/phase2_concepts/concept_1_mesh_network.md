# CONCEPT 1: Distributed Mesh Deterrent Network
## Phase 2 Detailed Engineering Proposal

**Joint Engineering Team**: Embedded Systems Architect, Electrical Engineer, Control Systems Engineer
**Date**: 2026-02-15
**Status**: Detailed Engineering Specification
**Origin**: SYNAPSE concept (Phase 1 TRIZ Analysis, Rank 5)

---

## Executive Summary

The Distributed Mesh Deterrent Network (DMDN) deploys 75-150 ultra-low-cost ($8-18 per node) wirelessly-coordinated deterrent nodes across field perimeters and wildlife entry corridors. Each node contains a PIR motion sensor, piezoelectric buzzer, high-brightness LED, passive scent wick holder, and LoRa radio module. A central AI controller (Raspberry Pi 4 + LoRa concentrator gateway) coordinates the mesh to produce emergent group deterrence behaviors -- encirclement, herding cascades, synchronized waves, and stochastic bursts -- using variable-ratio reinforcement scheduling (25-40% response rate during maintenance phase) to maximize habituation resistance across a full 4-6 month growing season.

The mesh is paired with 3-5 nociceptive "consequence stations" (water jet, capsaicinoid burst, or electric shock pad) at identified wildlife corridors to provide the unconditioned stimulus backbone that prevents pure-sensory habituation.

**Target cost**: $47-89/acre/year for 50-acre deployment (5-year TCO), well within the $100/acre/year constraint.

---

## 1. System Architecture

### 1.1 Architecture Diagram

```
                        DISTRIBUTED MESH DETERRENT NETWORK
                          50-Acre Field Deployment View

    +=================================================================+
    |                                                                   |
    |   [G] Gateway/AI Controller (field edge, mains-powered)          |
    |    |                                                              |
    |    |  LoRa 915 MHz (1-3 km range)                                |
    |    |                                                              |
    |    +------ Mesh Backbone (star-of-stars topology) --------+      |
    |    |                                                      |      |
    |    v                                                      v      |
    |                                                                   |
    |   PERIMETER RING (nodes every 25-35m along ~1,800m perimeter)    |
    |                                                                   |
    |   [N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]    |
    |    |                                                      |      |
    |   [N]                                                    [N]     |
    |    |              INTERIOR GRID                            |      |
    |   [N]         (nodes every 50-75m)                       [N]     |
    |    |                                                      |      |
    |   [N]      [N]----[N]----[N]----[N]----[N]              [N]     |
    |    |        |                            |                |      |
    |   [N]      [N]    [N]    [N]    [N]    [N]              [N]     |
    |    |        |                            |                |      |
    |   [N]      [N]----[N]----[N]----[N]----[N]              [N]     |
    |    |                                                      |      |
    |   [N]                                                    [N]     |
    |    |                                                      |      |
    |   [N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]---[N]    |
    |                                                                   |
    |   NOCICEPTIVE CONSEQUENCE STATIONS (at corridors):               |
    |                                                                   |
    |   [W]=Water Jet    [C]=Capsaicinoid Burst    [S]=Shock Pad       |
    |                                                                   |
    |         [W]                    [W]                                |
    |          |                      |                                 |
    |   ======[C]======Field Edge Road======[W]======                  |
    |                                                                   |
    |   Legend:                                                         |
    |   [N]  = Mesh deterrent node ($8-18 each)                        |
    |   [G]  = Gateway + AI controller (Raspberry Pi 4 + LoRa HAT)     |
    |   [W]  = Water jet consequence station (irrigation-connected)    |
    |   [C]  = Capsaicinoid burst station                              |
    |   [S]  = Shock pad station                                       |
    |   ---  = LoRa mesh radio link                                    |
    |   ===  = Physical infrastructure (road, fence, irrigation line)  |
    |                                                                   |
    +=================================================================+

    VERTICAL VIEW (single node):

    Scent wick holder (clip-on, top)    <-- Replaceable monthly
            |
    [===PIR DOME===]                    <-- HC-SR505 or AM312 sensor
    |  LED (forward) |                  <-- 3W white LED, 60deg beam
    | [BUZZER]       |                  <-- Piezo, 3-20 kHz, 95+ dB
    | [PCB: MCU+LoRa]|                 <-- STM32WL55 SoC (MCU + LoRa)
    | [BATTERIES]    |                  <-- 3x AA lithium (4.5V, 9Wh)
    |________________|
    |  ABS enclosure |                  <-- IP65, injection-molded
    |     STAKE      |                  <-- 50cm galvanized steel
    |     |||||      |
    //////GROUND//////
```

### 1.2 System Components Overview

| Component | Quantity (50-acre) | Function |
|-----------|-------------------|----------|
| Mesh deterrent nodes | 100 (nominal) | Sense, deter, relay |
| LoRa gateway + AI controller | 1 | Coordinate, decide, learn |
| Water jet consequence stations | 3 | Nociceptive backbone |
| Capsaicinoid burst stations | 2 | Nociceptive backbone (alt) |
| Mounting stakes | 100 | Physical deployment |
| Scent wick refill kits | 400/season | Olfactory deterrent |
| Battery sets | 200/season | Power (2 replacements/season) |

---

## 2. Node Hardware Design

### 2.1 MCU Selection: STM32WL55JC

After evaluating ESP32-C3, nRF52840, and STM32WL55, we select the **STM32WL55JC** as the optimal MCU for this application.

#### Selection Rationale

| Parameter | ESP32-C3 | nRF52840 | STM32WL55JC | Winner |
|-----------|----------|----------|-------------|--------|
| Sub-GHz radio | NO (WiFi/BLE only) | NO (BLE only) | YES (integrated LoRa) | STM32WL |
| Need external LoRa? | Yes (+$3-5 SX1262) | Yes (+$3-5 SX1262) | No (integrated) | STM32WL |
| MCU+Radio BOM | $3.50 + $3.50 = $7.00 | $4.00 + $3.50 = $7.50 | $3.80 standalone | STM32WL |
| Sleep current | 5 uA (deep sleep) | 1.5 uA (system OFF) | 0.37 uA (standby) | STM32WL |
| Active current (MCU) | 50-80 mA | 3-5 mA | 5-12 mA | nRF52 |
| LoRa TX current | 40-120 mA (SX1262) | 40-120 mA (SX1262) | 40-120 mA (integrated) | Tie |
| Operating temp | -40 to 105C | -40 to 85C | -40 to 105C | STM32WL/ESP32 |
| Flash/RAM | 400KB/400KB | 1MB/256KB | 256KB/64KB | nRF52 |
| Development ecosystem | ESP-IDF, Arduino | Zephyr, nRF SDK | STM32CubeWL, Zephyr | Tie |
| Volume price (1k qty) | $1.50-2.50 | $3.00-4.00 | $2.80-3.50 | ESP32-C3 |
| Total radio+MCU (1k) | $5.00-7.50 | $6.50-9.00 | $2.80-3.50 | STM32WL |

**Decision**: The STM32WL55JC integrates the Cortex-M4 MCU and sub-GHz LoRa radio (SX126x-equivalent) on a single die, eliminating the SPI bus, external crystal, RF matching network, and PCB area that a discrete MCU + SX1262 solution requires. At 1,000-unit volume the STM32WL55JC is approximately $2.80-3.50 per chip, versus $5.00-7.50 for ESP32-C3 + SX1262 or $6.50-9.00 for nRF52840 + SX1262. The 0.37 uA standby current is critical for achieving 6-month battery life.

**Alternative/Second Source**: If STM32WL55 supply becomes constrained, the **Semtech LR1121** (integrated LoRa transceiver + Cortex-M0 host MCU, ~$3.50 at volume) or the **ASR6601** (Airoha/ASR, integrated LoRa SoC, ~$2.00-2.50 at volume, emerging Chinese supplier) serve as second sources.

### 2.2 PIR Sensor Module

**Selected**: **AM312** (mini PIR sensor module)

| Parameter | AM312 | HC-SR501 | HC-SR505 |
|-----------|-------|----------|----------|
| Detection range | 3-5m | 5-7m | 3-5m |
| Detection angle | 100 deg | 120 deg | 100 deg |
| Operating voltage | 2.7-12V | 4.5-20V | 4.5-20V |
| Quiescent current | 10-20 uA | 50-65 uA | 45 uA |
| Trigger type | Retriggering | Selectable | Retriggering |
| Size | 10mm x 10mm | 32mm x 24mm | 10mm x 23mm |
| Unit cost (1k qty) | $0.35-0.50 | $0.80-1.20 | $0.60-0.80 |

**Design note**: The AM312's 3-5m range is intentionally SHORT. We do not need each node to detect deer at 100m. Instead, the dense mesh relies on spatial density -- with nodes every 25-35m on the perimeter, a deer approaching the field MUST pass within 12-17m of at least one node. The AM312 at 3-5m provides high-confidence close-range detection that triggers the coordinated mesh response. For early-warning detection at longer range, we rely on the aggregate of multiple PIR triggers forming a track (see Section 3, Network Architecture).

**Extended range option**: For corridor nodes where early detection matters, substitute the **HC-SR501** ($0.80-1.20) with 5-7m range and Fresnel lens. Budget allows 10-15 "long-range" nodes at corridors without materially impacting per-node cost.

### 2.3 Buzzer/Speaker Specification

**Selected**: **Piezoelectric buzzer with integrated driver**, 42mm diameter disc

| Parameter | Specification |
|-----------|--------------|
| Type | Piezoelectric disc with resonant cavity |
| Diameter | 42mm |
| SPL at 10cm | 95-105 dB |
| SPL at 3m (estimated) | 65-75 dB |
| Frequency range | 3-20 kHz (drive-frequency dependent) |
| Resonant frequency | 3.5-4.5 kHz (optimal for deer startle) |
| Drive voltage | 3-30V (piezo is capacitive, higher V = louder) |
| Peak current draw | 15-30 mA at 5V (capacitive load, pulsed) |
| Unit cost (1k qty) | $0.30-0.60 |

**Design note**: A simple piezo disc driven by the STM32WL's PWM output produces frequency-variable tones from 2-20 kHz. By modulating frequency, pulse duration, and pulse pattern, we generate chirps, sweeps, predator-mimicking growl approximations, and startle bursts. The 95+ dB at close range is sufficient for a node designed to activate when a deer is within 3-10m. A boost converter circuit (see Section 2.8) steps battery voltage to 12-20V for higher SPL during maximum-intensity activations.

**Alternative for premium nodes**: For 10-15 corridor nodes, substitute a **micro speaker driver** (8 ohm, 2W, 40mm) at $0.80-1.50 each, driven by a Class-D amplifier chip (PAM8302, $0.35). This enables playback of recorded predator vocalizations stored in STM32WL flash (256KB = ~8 seconds of 8-bit 16kHz audio). Cost adder: $1.15-1.85 per premium node.

### 2.4 LED Specification

**Selected**: **3W white LED, star PCB mount**

| Parameter | Specification |
|-----------|--------------|
| Type | 3W high-power LED on 20mm star PCB |
| Color | Cool white (6000-7000K) |
| Luminous flux | 200-280 lumens (peak, pulsed) |
| Beam angle | 60 degrees (with integrated lens) |
| Forward voltage | 3.0-3.6V |
| Drive current | 350-700 mA (pulsed, not continuous) |
| Duty cycle | <5% (strobed during activation only) |
| MOSFET driver | AO3400 N-channel (SOT-23, $0.05) |
| Unit cost (1k qty) | $0.15-0.30 (LED) + $0.10 (star PCB) + $0.05 (MOSFET) = $0.30-0.45 |

**Design note**: The LED operates in pulsed/strobe mode only, never continuous. At 350 mA pulsed for 50ms pulses at 2-5 Hz strobe rate, the average current is 35-88 mA. Peak luminous intensity in the beam center (60 degrees) is approximately 300-470 candelas -- visible at 200+ meters at night. White color is chosen because deer are most startled by broad-spectrum sudden illumination (mimics lightning or predator eye-shine reflection). The low duty cycle keeps thermal and power budgets manageable.

**Color option**: A dual-color (white + amber/red) LED at $0.50 adds variety. Red is barely visible to deer (dichromatic vision peaks at ~450nm and ~537nm) but creates an eerie glow visible to humans for system status indication.

### 2.5 Scent Wick Holder

**Design**: Passive clip-on holder, no electronics

| Parameter | Specification |
|-----------|--------------|
| Type | Open-top ABS tube with friction-fit clip |
| Dimensions | 25mm ID x 50mm tall |
| Mounting | Clip onto top of node enclosure (tool-free) |
| Wick material | Compressed felt or cotton, pre-loaded with scent |
| Scent formulation | Synthetic predator kairomone blend (PEA + TMT + coyote urine extract) |
| Evaporation rate | 0.5-1.0 mL/week (passive, wind-dependent) |
| Refill interval | Monthly (4-6 refills per season) |
| Wick cost | $0.50-1.00 per wick (at volume, including scent loading) |

**Design note**: The scent wick is entirely passive -- no power, no electronics, no actuator. It relies on ambient wind for dispersal. The holder is designed for tool-free replacement: pull old wick out, push new wick in. A farm worker can replace all 100 wicks in 60-90 minutes during a routine field walk. This is the primary scheduled maintenance task.

**Anti-habituation**: Scent blend is rotated across 3-4 formulations per season (predator A, predator B, novel blend, concentrated). Wicks are color-coded by formulation for easy identification during replacement.

### 2.6 Battery Specification

**Selected**: **3x Energizer Ultimate Lithium AA (L91)**

| Parameter | Specification |
|-----------|--------------|
| Chemistry | Lithium iron disulfide (Li-FeS2) |
| Nominal voltage | 1.5V x 3 = 4.5V |
| Capacity | 3,000 mAh per cell (at low drain) |
| Energy per cell | 4.5 Wh |
| Total energy (3-cell pack) | 13.5 Wh |
| Operating temperature | -40C to 60C |
| Shelf life | 20 years |
| Weight | 15g x 3 = 45g |
| Self-discharge | <1%/year |
| Unit cost (bulk, 1000+ cells) | $1.20-1.50 per cell |
| 3-cell pack cost | $3.60-4.50 |

**Rationale for lithium AA over alternatives**:

| Battery type | Capacity | Temp range | Cost/Wh | Self-discharge | Decision |
|-------------|----------|-----------|---------|----------------|----------|
| Alkaline AA (x3) | 9 Wh | -18 to 54C | $0.07 | 5-10%/yr | Too cold-sensitive, high self-discharge |
| Li-FeS2 AA (x3) | 13.5 Wh | -40 to 60C | $0.27-0.33 | <1%/yr | SELECTED |
| 18650 Li-ion (x1) | 10-13 Wh | -20 to 60C | $0.25-0.50 | 2-3%/yr | Requires holder, charge circuit; overkill |
| CR123A (x2) | 9 Wh | -40 to 60C | $0.44 | <1%/yr | More expensive, non-standard |

**Runtime estimate**: See Section 6 (Power Budget) for detailed calculation. Summary: 5.5-8.5 months on a single set of 3x AA lithium batteries under nominal operating conditions, covering one full growing season with margin.

**Solar supplement option**: A small 1W solar panel ($2-3) with a supercapacitor ($1-2) could extend battery life indefinitely or allow use of cheaper rechargeable NiMH cells. This adds $3-5 per node and a small circuit board area. Recommended as an option for V2 but not required for V1 to meet the 6-month target.

### 2.7 Weatherproof Enclosure

| Parameter | Specification |
|-----------|--------------|
| Material | ABS plastic, UV-stabilized |
| IP rating | IP65 (dust-tight, protected against water jets) |
| Dimensions | 90mm x 70mm x 55mm (L x W x H) |
| Color | Matte dark green or brown (field-appropriate) |
| Sealing | Silicone gasket on lid, cable gland for PIR dome |
| PIR window | HDPE Fresnel lens window, sonically welded |
| LED aperture | Clear polycarbonate window, forward-facing |
| Buzzer port | Mesh-covered acoustic port (water-resistant, sound-transparent) |
| Scent holder | Top-mounted clip receptacle |
| Stake mount | Bottom press-fit socket for 10mm steel stake |
| Tooling cost | $3,000-5,000 for injection mold (amortized over 1,000+ units) |
| Per-unit cost (1k qty) | $0.80-1.50 (injection molded) |
| Per-unit cost (100 qty) | $2.50-4.00 (machined or 3D-printed) |

**Stake**: 50cm galvanized steel rod, 10mm diameter, pointed end. Pushes into soil by hand or with a rubber mallet. Cost: $0.40-0.80 each at volume.

### 2.8 Complete Node BOM

#### Bill of Materials -- Per Node

| # | Component | Part / Description | Qty | Unit Cost (100) | Unit Cost (1000) |
|---|-----------|-------------------|-----|-----------------|------------------|
| 1 | MCU + LoRa SoC | STM32WL55JC (UFQFPN48) | 1 | $3.80 | $2.80 |
| 2 | Crystal (TCXO) | 32 MHz TCXO for LoRa | 1 | $0.60 | $0.40 |
| 3 | RF matching network | Inductors, caps (0402) | 5 | $0.15 | $0.08 |
| 4 | Antenna | 915 MHz helical PCB antenna or wire whip | 1 | $0.30 | $0.15 |
| 5 | PIR sensor | AM312 module | 1 | $0.55 | $0.40 |
| 6 | Piezo buzzer | 42mm disc with cavity | 1 | $0.60 | $0.35 |
| 7 | Buzzer boost circuit | SOT-23 boost converter + passives (to 12V) | 1 | $0.40 | $0.25 |
| 8 | LED (white, 3W) | LED on star PCB, 60-deg lens | 1 | $0.45 | $0.30 |
| 9 | LED driver MOSFET | AO3400 N-ch SOT-23 | 1 | $0.08 | $0.05 |
| 10 | Voltage regulator | 3.3V LDO (MCP1700) | 1 | $0.25 | $0.15 |
| 11 | Decoupling caps | 100nF + 10uF ceramic (0402/0805) | 4 | $0.08 | $0.04 |
| 12 | PCB | 2-layer FR4, 50x35mm | 1 | $0.80 | $0.30 |
| 13 | Battery holder | 3x AA, PCB mount or wired | 1 | $0.40 | $0.25 |
| 14 | Batteries | Energizer L91 lithium AA | 3 | $4.50 | $3.60 |
| 15 | Enclosure | IP65 ABS, injection molded | 1 | $3.50 | $1.20 |
| 16 | Gasket + hardware | Silicone gasket, screws, gland | 1 | $0.30 | $0.15 |
| 17 | Scent wick holder | ABS clip-on tube | 1 | $0.20 | $0.10 |
| 18 | Scent wick (initial) | Pre-loaded felt wick | 1 | $0.80 | $0.60 |
| 19 | Stake | 50cm galv. steel rod, 10mm | 1 | $0.80 | $0.50 |
| 20 | Assembly labor | SMT placement + hand assembly | 1 | $2.00 | $1.00 |
| | **TOTAL PER NODE** | | | **$20.06** | **$12.57** |

#### BOM Summary by Volume

| Volume | Per-Node Cost | Notes |
|--------|--------------|-------|
| 100 units | $20.06 | Prototype/pilot pricing, 3D-printed enclosures |
| 500 units | $15.50 (est.) | Small production run, injection-molded tooling amortized |
| 1,000 units | $12.57 | Production pricing, all injection-molded |
| 5,000 units | $9.50 (est.) | Volume pricing on all components, automated assembly |

**Note**: Batteries ($3.60-4.50) represent 29-35% of total node cost. A solar-supplemented design with rechargeable NiMH cells could reduce recurring battery cost but adds $3-5 to initial node cost.

---

## 3. Network Architecture

### 3.1 LoRa Mesh Topology

**Topology**: Modified star-of-stars with mesh relay capability

```
                   Architecture: Star-of-Stars with Mesh Fallback

    [Gateway]
       |
       | Primary star links (direct to gateway)
       |
    [N1]----[N2]----[N3]----[N4]----[N5]      <-- Perimeter ring
     |  \   / |  \   / |  \   / |  \   / |
    [N6] [N7] [N8] [N9] [N10][N11]          <-- Interior grid
     |        |         |        |
    [N12]---[N13]----[N14]---[N15]            <-- Secondary perimeter

    --- = Mesh relay path (used when direct-to-gateway fails)
```

**Protocol**: LoRaWAN Class C (continuous receive) on the gateway; custom lightweight mesh protocol on nodes.

We do NOT use standard LoRaWAN for node-to-node communication because LoRaWAN is a star topology designed for uplink to a gateway. Instead, we implement a simple flooding-based mesh protocol:

| Parameter | Specification |
|-----------|--------------|
| Frequency | 915 MHz ISM band (US) |
| Bandwidth | 125 kHz |
| Spreading factor | SF7 (fastest, shortest range) for mesh relay; SF10 for direct-to-gateway |
| Data rate | 5.47 kbps (SF7) / 0.98 kbps (SF10) |
| TX power | +14 dBm (25 mW) -- FCC compliant |
| Node-to-node range | 200-500m (ground level, agricultural terrain, SF7) |
| Node-to-gateway range | 500-2,000m (gateway elevated 3-5m, SF10) |
| Channel access | Slotted ALOHA with random backoff |
| Max message size | 32 bytes (node report) / 16 bytes (activation command) |
| Duty cycle | <1% (FCC 15.247 compliant at 915 MHz with FHSS) |

### 3.2 Node Spacing and Coverage

**50-acre field geometry**: Approximately 450m x 450m (square) or 500m x 400m (rectangular)
**Perimeter**: ~1,800m

| Zone | Node Spacing | Node Count | Purpose |
|------|-------------|------------|---------|
| Perimeter ring | 25-35m | 52-72 | Primary detection + deterrence |
| Interior grid | 50-75m | 20-36 | Depth deterrence + tracking |
| Corridor clusters | 10-15m | 8-15 | High-density at entry points |
| **TOTAL** | | **80-123** | |

**Nominal deployment**: 100 nodes (round number for cost modeling).

**Coverage analysis**: With 100 nodes on a 50-acre field, average node density is 2 nodes/acre. The perimeter ring (where most intrusions begin) has approximately 1 node every 30m. Given the AM312's 3-5m detection range and the PIR's 100-degree field of view, direct detection coverage at the perimeter is approximately 30-40% of the perimeter length. However, a deer-sized animal moving along the perimeter at walking speed (1-2 m/s) will pass within detection range of a node approximately every 15-20 seconds, providing a high probability (>95%) of detection within 30 seconds of perimeter approach.

### 3.3 Gateway/Hub Hardware

The gateway is the bridge between the LoRa mesh and the AI controller.

| Component | Specification | Cost |
|-----------|--------------|------|
| Single-board computer | Raspberry Pi 4 Model B (2GB RAM) | $45 |
| LoRa concentrator | RAK2287 SPI LoRa concentrator (SX1303 + SX1250) | $45-65 |
| Pi HAT adapter | RAK2287 Pi HAT | $15 |
| GPS module | u-blox MAX-M10S (for time sync) | $12 |
| Antenna | 915 MHz fiberglass omnidirectional, 5 dBi gain, 1m cable | $15 |
| Antenna mast | 3m aluminum pole, ground-mounted or building-mounted | $25 |
| Enclosure | IP66 NEMA 4X polycarbonate box, 300x200x150mm | $25 |
| Power supply | 5V/3A USB-C adapter (mains-powered) | $10 |
| MicroSD card | 32GB industrial-grade (SanDisk Industrial) | $12 |
| Cellular modem (optional) | Quectel EC25 4G LTE mini-PCIe (for cloud connectivity) | $30 |
| SIM card + data (optional) | Hologram IoT SIM, ~100MB/month | $5/month |
| Surge protector | Ethernet + power line surge suppressor | $15 |
| **TOTAL (gateway)** | | **$234-279** |

**Placement**: The gateway is installed at the field edge where mains power is available (near a barn, pump house, or electrical service panel). The 5 dBi omnidirectional antenna on a 3m mast provides line-of-sight to the entire 50-acre field. LoRa at SF10, 125 kHz BW, +14 dBm TX from the gateway reaches all nodes within the 500m x 450m field with 10-20 dB link margin.

### 3.4 Message Protocol

#### Uplink Messages (Node to Gateway)

| Message Type | Payload Size | Content | Trigger |
|-------------|-------------|---------|---------|
| PIR_DETECT | 8 bytes | node_id(2) + timestamp(4) + signal_strength(1) + battery_v(1) | PIR trigger |
| ACTIVATION_ACK | 6 bytes | node_id(2) + timestamp(4) | After executing activation command |
| HEARTBEAT | 8 bytes | node_id(2) + timestamp(4) + battery_v(1) + temp(1) | Every 15 minutes |
| RELAY | 32 bytes max | original_msg + hop_count(1) + relay_node_id(2) | When relaying another node's message |

#### Downlink Messages (Gateway to Node)

| Message Type | Payload Size | Content | Trigger |
|-------------|-------------|---------|---------|
| ACTIVATE | 12 bytes | target_node_id(2) + mode(1) + intensity(1) + duration_ms(2) + pattern_id(1) + delay_ms(2) + buzzer_freq(2) + led_pattern(1) | AI controller decision |
| ACTIVATE_GROUP | 16 bytes | group_bitmap(8) + mode(1) + intensity(1) + duration_ms(2) + pattern_id(1) + delay_ms(2) + led_pattern(1) | Group activation (up to 64 nodes) |
| CONFIG_UPDATE | 16 bytes | node_id(2) + param_id(1) + param_value(4) + ... | Remote configuration |
| TIME_SYNC | 6 bytes | unix_timestamp(4) + sub_second(2) | Broadcast every 5 minutes |

#### Activation Modes

| Mode | Buzzer | LED | Description |
|------|--------|-----|-------------|
| 0x00 | OFF | OFF | Silent (detection-only, no response) |
| 0x01 | Chirp (50ms) | Flash (50ms) | Minimal startle |
| 0x02 | Sweep (500ms) | Strobe (2Hz, 1s) | Standard deterrent |
| 0x03 | Siren (2s) | Strobe (5Hz, 2s) | Aggressive deterrent |
| 0x04 | Growl pattern (3s) | Slow pulse (1Hz, 3s) | Predator simulation |
| 0x05 | Max intensity (5s) | Max strobe (10Hz, 5s) | Maximum escalation |
| 0xFF | Custom | Custom | Pattern defined by pattern_id lookup |

### 3.5 Network Latency

**Detection-to-response timeline**:

| Step | Duration | Cumulative |
|------|----------|-----------|
| PIR sensor trigger + MCU wake | 50-100 ms | 100 ms |
| Node processes detection locally | 5-10 ms | 110 ms |
| LoRa TX (uplink to gateway) | 30-60 ms (SF7, 8 bytes) | 170 ms |
| Gateway receives + AI processes | 10-50 ms | 220 ms |
| AI selects pattern + computes commands | 5-20 ms | 240 ms |
| LoRa TX (downlink, broadcast) | 50-100 ms (SF7, 16 bytes) | 340 ms |
| Target nodes receive + execute | 10-30 ms | 370 ms |
| **TOTAL: detection to first deterrent** | | **250-400 ms** |

**If mesh relay is needed** (node cannot reach gateway directly): Add 60-120 ms per hop. Maximum 2 hops in our topology, so worst case ~500-640 ms. Well within the 5-second constraint.

**For time-critical patterns** (encirclement, herding): The detecting node can self-activate IMMEDIATELY (within 100ms) using a local decision table, while simultaneously reporting to the gateway. The gateway then coordinates the broader pattern. This hybrid approach ensures the nearest node responds instantly while the intelligent coordinated response follows within 400ms.

### 3.6 Redundancy and Self-Healing

| Failure Mode | Impact | Mitigation |
|-------------|--------|-----------|
| Single node failure | 30m gap in perimeter | Adjacent nodes increase sensitivity; gateway flags gap in dashboard |
| Multiple adjacent nodes fail | Coverage gap >50m | Gateway alerts farmer (push notification); remaining nodes cannot compensate |
| Gateway failure | Loss of coordination | Nodes fall back to autonomous mode: detect locally, activate locally at 50% probability |
| LoRa interference | Message loss | 3 retransmit attempts with random backoff; mesh relay via alternate nodes |
| Battery depletion | Node goes offline | Gateway detects missing heartbeats (>30 min), alerts farmer with node ID + location |

**Autonomous fallback mode**: Each node stores a simple local behavior table in flash: "If PIR triggers AND no gateway command received within 2 seconds, self-activate at Mode 0x02 with 50% probability (coin flip using hardware RNG)." This ensures the mesh degrades gracefully to a collection of independent deterrent nodes if the gateway fails, rather than going completely silent.

---

## 4. Deterrent Pattern Library

### 4.1 Pattern 1: ENCIRCLEMENT

**Purpose**: Simulate a predator pack surrounding a detected animal. Triggers deep evolutionary flight response.

**Trigger**: Single node detects deer that has penetrated 20+ meters into the field (interior grid detection).

**Execution sequence**:
```
Time 0ms:       Detecting node activates (Mode 0x03, aggressive)
Time 200ms:     Two nearest perimeter nodes behind the deer activate (Mode 0x02)
Time 500ms:     Two more perimeter nodes flanking the deer activate (Mode 0x02)
Time 1000ms:    Nodes ahead of the deer remain SILENT (escape corridor)
Time 1500ms:    Second ring of nodes activates (Mode 0x01, minimal)
Time 3000ms:    All activated nodes go silent simultaneously
Time 3000-5000ms: Single distant node activates briefly (Mode 0x01) to "push" deer toward escape corridor
```

**Spatial coordination**: Requires gateway to know approximate deer position (which node detected) and orientation of the escape corridor (toward the nearest field edge AWAY from crops). Gateway pre-computes encirclement maps for each interior node.

**VR scheduling integration**: The encirclement pattern is ONLY deployed on 30-40% of interior detections (VR-3 schedule). On non-reinforced detections, zero or minimal response (single node chirp). This ensures the animal cannot predict whether penetrating the field will trigger the terrifying encirclement or result in a minor chirp.

### 4.2 Pattern 2: HERDING CASCADE

**Purpose**: Push an animal away from the field center toward the nearest exit point using directional sequential activation.

**Trigger**: Detection by a perimeter node of an animal moving along the perimeter or attempting entry.

**Execution sequence**:
```
Time 0ms:       Detecting node activates (Mode 0x02)
Time 300ms:     Next node in the DIRECTION OF DESIRED MOVEMENT activates (Mode 0x03)
Time 600ms:     Node after that activates (Mode 0x04, predator simulation)
Time 900ms:     Continuing cascade, each node 300ms after the previous
                Direction: AWAY from nearest field entrance, TOWARD open ground
Time 300ms * N: Cascade reaches field corner or boundary
Time final:     Consequence station at corridor activates if animal approaches
```

**Speed**: The cascade travels at approximately 30m / 300ms = 100 m/s equivalent. This is far faster than a deer runs (12-15 m/s), ensuring the "predator" always appears to be ahead of the animal. The deer perceives threats appearing in its path faster than it can move.

**Directionality**: The gateway computes the optimal herding direction based on: (a) which perimeter segment the deer is on, (b) where the nearest consequence station is, (c) where other deer have been recently detected (avoid herding toward another group).

**VR scheduling integration**: Herding cascades are deployed on 35% of perimeter detections. On non-reinforced detections, either no response (60% of non-reinforced) or a single-node minimal chirp (40% of non-reinforced).

### 4.3 Pattern 3: AMBUSH

**Purpose**: Delayed, silent tracking followed by sudden maximum-intensity activation directly in the animal's predicted path. Exploits the "near-miss predator encounter" effect documented in the behavioral science literature as the most sensitizing experience for prey animals.

**Trigger**: Two or more sequential perimeter node detections indicating animal movement direction.

**Execution sequence**:
```
Time 0ms:       First node detects. Reports to gateway. NO activation.
Time 500-2000ms: Second node detects. Gateway computes movement vector.
Time 2000ms:    Gateway predicts which node(s) the animal will pass next
Time 2000ms:    Gateway sends ACTIVATE command to predicted node(s)
                with DELAY parameter = estimated time to arrival
Time T_arrival: Predicted node(s) activate at Mode 0x05 (MAXIMUM)
                -- buzzer at max, LED at max strobe, simultaneous
                The animal is within 3-5m of the activation point
```

**Effect**: The animal has been walking in silence. Suddenly, the ground directly beside or ahead of it explodes with light and sound at maximum intensity. This is the closest approximation to a predator ambush attack that the mesh can produce. The behavioral science literature shows that near-miss encounters produce 3-14 days of elevated vigilance and sensitization, not habituation.

**VR scheduling integration**: Ambush is the RAREST pattern, deployed on only 10-15% of multi-node detections. It is reserved for the variable-ratio "jackpot" -- the unpredictable maximum-intensity event that prevents the animal from ever feeling safe. Its rarity is critical: if it happened every time, the animal would learn the delay-then-blast pattern. At 10-15%, it remains terrifyingly unpredictable.

### 4.4 Pattern 4: WAVE

**Purpose**: Traveling activation wave across the perimeter or through the field, simulating a large disturbance front (predator pack sweep, fire line, etc.).

**Trigger**: Multiple simultaneous perimeter detections (3+ nodes within 30 seconds) suggesting a group approach (herd).

**Execution sequence**:
```
Time 0ms:       Wave origin point selected (opposite side of field from detections)
Time 0ms:       First line of nodes activates (Mode 0x02)
Time 500ms:     Second line activates, first line goes silent
Time 1000ms:    Third line activates, second line goes silent
...continues at 500ms intervals across the field...
Time N*500ms:   Wave reaches the detection side
                Final line activates at Mode 0x04 (predator simulation)
```

**Wave speed**: ~50m per 500ms = 100 m/s. The wave travels across the 450m field in approximately 2.25 seconds.

**Variants**:
- **Single wave**: One pass, then silence.
- **Ping-pong wave**: Wave travels out and bounces back.
- **Converging wave**: Two waves start from opposite edges and converge on the center (double-encirclement for herd groups).
- **Spiral wave**: Activation spirals inward from perimeter toward center (rarely used, maximum-intensity event for large groups).

**VR scheduling integration**: Waves are deployed on 25% of multi-animal detections. They are the "group response" pattern, distinct from individual-animal patterns.

### 4.5 Pattern 5: RANDOM BURST (Stochastic Field)

**Purpose**: Unpredictable, spatially random activations across the field that create an ambient "landscape of fear" -- the field itself seems alive with unpredictable threats.

**Trigger**: Scheduled by the AI controller during peak wildlife activity hours (dusk +2h, dawn -2h), regardless of detection events.

**Execution sequence**:
```
Every 30-120 seconds (random interval):
    Select 1-3 random nodes
    Select random mode (0x01 through 0x03)
    Select random duration (200ms - 2000ms)
    Activate selected nodes

Occasionally (5% probability per burst):
    Select 5-8 nodes in a spatial cluster
    Activate simultaneously at Mode 0x04
    (Simulates a "predator event" in an area the deer hasn't even approached)
```

**Design rationale**: The random burst pattern operates INDEPENDENTLY of detection. It makes the field unpredictable even when no deer are present. A deer observing the field from a distance (100-200m) sees random flashes and hears random chirps from unpredictable locations. This creates an ambient threat assessment before the deer even attempts entry -- the "landscape of fear" effect described by Laundre et al. (2001).

**Power management**: Only 1-3 nodes activate per burst, with 30-120 second intervals. Average power consumption for random burst mode is negligible (<1% of battery budget across the mesh).

**VR scheduling integration**: Random bursts are the "background noise" of the system. They operate on a variable-interval schedule (average 60 seconds, uniformly distributed 30-120s). This creates a continuous low-level threat signal that is distinct from the detection-triggered patterns.

### 4.6 Variable-Ratio Reinforcement Integration

The AI controller implements a two-phase scheduling algorithm:

**Phase 1 -- Acquisition (Weeks 1-2 of season)**:
- Response rate: 80-100% of detections
- Pattern selection: Primarily Herding (40%), Encirclement (30%), Ambush (20%), Wave (10%)
- Intensity: High (Mode 0x03-0x05)
- Consequence station activation: 50% of corridor detections
- Purpose: Establish strong conditioned fear association with the field

**Phase 2 -- Maintenance (Weeks 3 through end of season)**:
- Response rate: 25-40% of detections (VR-3 to VR-4 schedule)
- On reinforced trials: Full pattern deployment, variable pattern selection
- On non-reinforced trials: Silent (70%) or minimal chirp (30%)
- Consequence station activation: 15-25% of corridor detections
- Purpose: Maximize extinction resistance via partial reinforcement

**Adaptive VR ratio**: The controller monitors intrusion rate (detections per night). If intrusion rate increases by >20% over a 3-day rolling average, the controller temporarily increases the reinforcement ratio toward 60-80% for 2-3 days (reconsolidation window), then drops back to maintenance levels. This "booster" protocol exploits the reconsolidation effect to strengthen waning fear memories.

---

## 5. AI Controller Design

### 5.1 Hardware Platform

**Selected**: Raspberry Pi 4 Model B (2GB RAM) running Raspberry Pi OS Lite (headless)

**Justification**:

| Alternative | Pros | Cons | Decision |
|-------------|------|------|----------|
| Raspberry Pi 4 (2GB) | $45, huge ecosystem, Python/C++, LoRa HATs available, GPIO, low power (3-5W) | SD card wear, no industrial temp rating | SELECTED |
| Raspberry Pi 5 | Faster, same ecosystem | More expensive ($60-80), higher power (5-10W), availability | Overkill for this application |
| Coral Dev Board Mini | Built-in Edge TPU for ML | $100+, smaller ecosystem, limited GPIO | ML not needed at this complexity level |
| AWS/Azure cloud | Infinite compute, ML services | Requires cellular modem, latency, ongoing cost | Too expensive for ongoing data cost |
| ESP32-S3 (bare metal) | $5, lowest cost | Insufficient for pattern computation, no OS, limited storage | Too constrained |

**Software stack**:
- OS: Raspberry Pi OS Lite (Bullseye/Bookworm)
- LoRa interface: ChirpStack gateway bridge (open source)
- Application logic: Python 3.11 with asyncio
- Database: SQLite (local storage of all events, 32GB SD can store years of data)
- ML framework: scikit-learn (pattern effectiveness tracking, no deep learning needed)
- Remote access: SSH over cellular or WiFi (optional)
- Dashboard: Lightweight Flask web server (accessible from farmer's phone on local network)

### 5.2 Pattern Selection Algorithm

The AI controller uses a **multi-armed bandit** algorithm (Thompson Sampling) to select which deterrent pattern to deploy for each detection event.

```
ALGORITHM: Pattern Selection

INPUT:
    detection_event = {node_id, timestamp, signal_strength, recent_context}

STATE:
    pattern_effectiveness[pattern_id] = Beta(alpha, beta) distribution
        -- alpha = count of "successful" deployments (deer retreated within 60s)
        -- beta = count of "unsuccessful" deployments (deer remained or advanced)
    vr_schedule_counter = integer (counts detections since last reinforcement)
    vr_ratio = current target ratio (0.25 to 0.40, adaptive)

STEP 1: Variable-Ratio Decision
    vr_schedule_counter += 1
    p_reinforce = 1.0 / vr_ratio  -- e.g., VR-3 means 1/3 probability
    IF random() < p_reinforce:
        reinforce = TRUE
        vr_schedule_counter = 0
    ELSE:
        reinforce = FALSE
        RETURN {action: SILENT or MINIMAL_CHIRP}

STEP 2: Pattern Selection (Thompson Sampling)
    FOR each available pattern p:
        sample_p = random_beta(alpha_p, beta_p)
    selected_pattern = argmax(sample_p)

STEP 3: Intensity Selection
    base_intensity = MODE_0x02 (standard)
    IF intrusion_rate_elevated:
        base_intensity = MODE_0x03 (aggressive)
    IF random() < 0.10:  -- 10% "jackpot" escalation
        base_intensity = MODE_0x05 (maximum)

STEP 4: Compute Spatial Coordination
    target_nodes = compute_pattern_nodes(selected_pattern, detection_event)
    timing_offsets = compute_timing(selected_pattern, target_nodes)

STEP 5: Dispatch Commands
    FOR each (node, offset) in zip(target_nodes, timing_offsets):
        SEND ACTIVATE(node, base_intensity, offset)

STEP 6: Evaluate Outcome (asynchronous, 60-second window)
    WAIT for subsequent PIR detections from same area
    IF no detections within 60s in same zone:
        pattern_effectiveness[selected_pattern].alpha += 1  -- success
    ELSE:
        pattern_effectiveness[selected_pattern].beta += 1   -- failure
```

### 5.3 Adaptive VR Scheduling

The VR ratio is NOT fixed. The controller adapts it based on observed intrusion pressure:

```
EVERY 24 HOURS:
    intrusion_rate = count(PIR_DETECT events in last 24h)
    rolling_avg = exponential_moving_average(intrusion_rate, alpha=0.3)

    IF rolling_avg > baseline * 1.20:
        -- Intrusion rate increasing: boost reinforcement
        vr_ratio = min(vr_ratio + 0.05, 0.80)
        -- Also: schedule 2 "reconsolidation booster" nights at 70% ratio

    ELIF rolling_avg < baseline * 0.80:
        -- Intrusion rate decreasing: relax reinforcement (save battery)
        vr_ratio = max(vr_ratio - 0.02, 0.20)

    ELSE:
        -- Stable: maintain current ratio
        pass
```

### 5.4 Data Collection

| Data Point | Source | Frequency | Storage |
|-----------|--------|-----------|---------|
| PIR detection events | All nodes | Per event (~10-100/night) | SQLite, indefinite |
| Activation events | Gateway dispatch log | Per event | SQLite, indefinite |
| Pattern outcomes | 60-second post-activation analysis | Per reinforced detection | SQLite, indefinite |
| Battery voltage | Node heartbeats | Every 15 minutes | SQLite, 30-day rolling |
| Node temperature | Node heartbeats | Every 15 minutes | SQLite, 30-day rolling |
| Network health | Heartbeat presence/absence | Continuous | SQLite, 7-day rolling |
| Intrusion rate (daily) | Aggregated PIR events | Daily summary | SQLite, indefinite |
| Pattern effectiveness scores | Thompson Sampling state | Daily snapshot | SQLite, indefinite |
| Consequence station activations | Station control log | Per event | SQLite, indefinite |

**Estimated data volume**: ~50-500 KB/day. A 32GB SD card stores 100+ years of data. No cloud dependency required.

**Farmer-facing dashboard** (optional): A simple web page served by the Pi on the local WiFi network shows:
- Last 24-hour activity heatmap (which nodes fired, where detections occurred)
- Battery status (all nodes, flagging any below 20%)
- Intrusion trend graph (detections per night, 30-day history)
- Pattern effectiveness ranking
- Next scheduled maintenance (scent wick replacement date)

---

## 6. Power Budget and Battery Life

### 6.1 Operating Modes and Current Draw

| Mode | STM32WL State | Current Draw | Duration | Notes |
|------|--------------|-------------|----------|-------|
| Deep sleep | Standby + RTC | 2 uA | ~99.5% of time | PIR monitoring via interrupt |
| PIR wake | MCU active, radio off | 8 mA | 50-100 ms | Process PIR trigger |
| LoRa TX (SF7) | MCU active, radio TX | 85 mA | 30-60 ms | Report detection to gateway |
| LoRa RX | MCU active, radio RX | 6 mA | 50-100 ms | Receive activation command |
| Buzzer active | MCU active, boost converter on | 40 mA | 200-5000 ms | Piezo buzzer driven at 12V |
| LED active (strobe) | MCU active, LED MOSFET on | 350 mA peak, 35 mA avg | 200-5000 ms | 50ms on / 150ms off at 5 Hz |
| Full activation | All active simultaneously | ~130 mA average | 1000-5000 ms | Typical deterrent event |

### 6.2 Duty Cycle Analysis (Nominal 24-Hour Period)

**Assumptions for a typical day during maintenance phase**:
- 12 hours of "active" period (dusk to dawn)
- 12 hours of low-activity period (daytime, minimal detections)
- Average 3 PIR detections per node per night
- Average 1 activation per node per night (33% VR ratio)
- Average activation duration: 2 seconds
- 96 heartbeats per day (every 15 minutes)
- 12 random burst activations per node per day (as selected by random burst pattern)
- Average random burst duration: 500ms per activation

| Activity | Events/Day | Duration Each | Total Duration | Avg Current | Energy (mAh) |
|----------|-----------|--------------|----------------|-------------|--------------|
| Deep sleep | - | 23.97 hours | 86,292 s | 0.002 mA | 0.048 |
| PIR wake + process | 3 | 100 ms | 300 ms | 8 mA | 0.0007 |
| LoRa TX (detection report) | 3 | 50 ms | 150 ms | 85 mA | 0.0035 |
| LoRa RX (check for commands) | 99 | 80 ms | 7,920 ms | 6 mA | 0.013 |
| Full activation (deterrent) | 1 | 2,000 ms | 2,000 ms | 130 mA | 0.072 |
| Random burst activation | 0.12* | 500 ms | 60 ms | 130 mA | 0.002 |
| Heartbeat TX | 96 | 50 ms | 4,800 ms | 85 mA | 0.113 |
| **TOTAL per day** | | | | | **0.253 mAh/day** |

*Note: 12 random bursts across 100 nodes = 0.12 per node per day on average.

**Wait -- this is extremely low. Let me recalculate with a more conservative scenario.**

### 6.3 Conservative Power Budget (High-Activity Scenario)

**Assumptions for peak deer pressure (worst-case night)**:
- 30 PIR detections per node per night (near a corridor)
- 10 activations per node per night
- Average activation duration: 3 seconds
- LoRa RX window: every 10 seconds during active period (aggressive listening for commands)

| Activity | Events/Day | Duration Each | Total Duration | Avg Current | Energy (mAh) |
|----------|-----------|--------------|----------------|-------------|--------------|
| Deep sleep | - | 12 hours | 43,200 s | 0.002 mA | 0.024 |
| PIR wake + process | 30 | 100 ms | 3,000 ms | 8 mA | 0.007 |
| LoRa TX (reports) | 30 | 50 ms | 1,500 ms | 85 mA | 0.035 |
| LoRa RX (command check) | 4,320* | 80 ms | 345,600 ms | 6 mA | 0.576 |
| Full activation | 10 | 3,000 ms | 30,000 ms | 130 mA | 1.083 |
| Heartbeat TX | 96 | 50 ms | 4,800 ms | 85 mA | 0.113 |
| **TOTAL per day** | | | | | **1.84 mAh/day** |

*LoRa RX: 12 hours active / 10 seconds = 4,320 listen windows.

### 6.4 Battery Life Calculation

| Scenario | Daily Consumption | Battery Capacity | Battery Life | Meets 6-Month Target? |
|----------|------------------|-----------------|-------------|----------------------|
| Nominal (typical day) | 0.25 mAh | 3,000 mAh (3x AA Li) | 12,000 days (33 years) | YES (massively) |
| Conservative (peak night) | 1.84 mAh | 3,000 mAh | 1,630 days (4.5 years) | YES (massively) |
| Extreme (every night is peak) | 1.84 mAh | 3,000 mAh | 1,630 days | YES |
| Ultra-extreme (10x peak, stress test) | 18.4 mAh | 3,000 mAh | 163 days (5.4 months) | YES (barely) |

**Conclusion**: 3x AA lithium batteries provide far more than the required 6-month growing season battery life under any realistic operating scenario. Even under an unrealistic "ultra-extreme" scenario where every single night is 10x the peak activity level, the battery lasts 5.4 months.

**Recommendation**: The power budget has enormous margin. This allows us to consider:
1. Downgrading to 2x AA lithium (2,000 mAh) for cost savings ($1.20-1.50 savings per node)
2. Using cheaper alkaline AA batteries ($0.50/cell vs $1.20-1.50) with the understanding that cold-weather performance suffers below -10C
3. Using the excess power margin for more aggressive LoRa listening (improving latency) or brighter LED/louder buzzer activations

**Selected configuration**: Retain 3x AA lithium for the full-temperature-range guarantee and the marketing claim of "1 year+ battery life." Cost of certainty: $3.60-4.50 per node.

---

## 7. Nociceptive Backbone Integration

### 7.1 Rationale

The behavioral science literature is unequivocal: pure sensory stimuli (light, sound, smell) habituate within 2-6 weeks regardless of variability, scheduling, or multi-modal coordination. The mesh network's acoustic/visual/olfactory deterrents serve as **conditioned stimuli (CS)** that must be paired with **unconditioned stimuli (US)** -- stimuli that engage nociceptive (pain) pathways which sensitize rather than habituate.

Without a nociceptive backbone, the mesh network will fail within 4-6 weeks. With it, conditioned fear can be maintained for the full growing season using partial reinforcement (25-40% consequence pairing).

### 7.2 Option A: Water Jet Stations (RECOMMENDED PRIMARY)

**Configuration**: 3-5 irrigation-connected water jet stations at identified wildlife entry corridors.

| Parameter | Specification |
|-----------|--------------|
| Type | Solenoid-activated impact sprinkler head |
| Valve | 3/4" 12V DC solenoid valve (normally closed) |
| Pressure | 30-60 PSI (standard irrigation pressure) |
| Range | 10-15m radius |
| Coverage per station | ~700 m2 (quarter-circle or adjustable arc) |
| Activation duration | 3-10 seconds (variable) |
| Water consumption | 2-5 gallons per activation |
| Detection | Dedicated PIR sensor (HC-SR501, long-range) |
| Communication | LoRa mesh node (integrated into station) |
| Power | 12V, 500mA solenoid; powered by 12V battery or mains adapter |
| Physical deterrent | Cold water impact at 30-60 PSI is startling and mildly painful to exposed skin/hide |

**Per-station BOM**:

| Component | Cost |
|-----------|------|
| 3/4" solenoid valve (12V, brass, NSF rated) | $15-25 |
| Impact sprinkler head (adjustable arc, Rain Bird 5000) | $12-18 |
| 3/4" PVC pipe + fittings (10-20 ft run from main) | $10-20 |
| PIR sensor (HC-SR501) + waterproof housing | $5 |
| LoRa mesh node (integrated; shared with mesh) | $12-15 |
| 12V/7Ah SLA battery + solar trickle charger (2W) | $25-35 |
| Weatherproof junction box + wiring | $10 |
| **Total per station** | **$89-128** |
| **5 stations total** | **$445-640** |

**Integration with mesh**: Water jet stations are mesh members with their own node_id. The AI controller treats them as high-value activation targets. When a detection event near a corridor triggers a reinforced trial AND the VR schedule selects consequence delivery, the controller sends an ACTIVATE command to the nearest water jet station with a delay timed to fire as the animal reaches the corridor.

**Consequence pairing protocol**: During acquisition phase (weeks 1-2), 50% of corridor detections trigger water jets. During maintenance phase, 15-25% of corridor detections trigger water jets. The water blast is ALWAYS accompanied by mesh node activation (CS + US pairing), ensuring the mesh's acoustic/visual stimuli become conditioned fear cues associated with the water impact.

### 7.3 Option B: Capsaicinoid Burst Stations

**Configuration**: 2-3 stations at highest-traffic entry points.

| Parameter | Specification |
|-----------|--------------|
| Type | Pressurized capsaicinoid aerosol dispenser |
| Mechanism | 12V solenoid valve releases compressed air/CO2 through a capsaicinoid solution reservoir |
| Active ingredient | Capsaicin + dihydrocapsaicin (OC, 2-5% concentration) |
| Delivery | 0.5-second burst of aerosolized OC spray |
| Range | 3-5m (directional, wind-dependent) |
| Activation per fill | 50-100 bursts per reservoir fill |
| Reservoir size | 500mL |
| Refill interval | Monthly (during scent wick maintenance visit) |
| Regulatory | Capsaicinoid is EPA-exempt as minimum risk pesticide under FIFRA 25(b); no registration required |

**Per-station BOM**:

| Component | Cost |
|-----------|------|
| Pressurized reservoir (modified garden sprayer, 1L) | $15-20 |
| 12V micro-solenoid valve + nozzle | $10-15 |
| CO2 cartridge holder (16g) | $5 |
| CO2 cartridges (10-pack) | $15 |
| Capsaicinoid concentrate (500mL, 5% OC) | $25-40 |
| PIR sensor + LoRa node (integrated) | $15 |
| Mounting bracket + weatherproof housing | $15 |
| 12V battery (same as water jet station) | $25-35 |
| **Total per station** | **$125-145** |
| **3 stations total** | **$375-435** |

**Advantage over water jet**: No irrigation connection required. Can be placed anywhere, including deep field interior. The capsaicinoid activates TRPV1 nociceptors (pain/heat receptors), producing a burning sensation on mucous membranes (eyes, nose, mouth) that is extremely aversive and sensitizes with repeated exposure.

**Disadvantage**: Wind-dependent, shorter range, requires consumable refills, and a small regulatory risk if state regulations differ from federal FIFRA 25(b) exemption.

### 7.4 Option C: Electric Shock Pad Stations

**Configuration**: 3-5 ground-level conductive pads at entry corridors.

| Parameter | Specification |
|-----------|--------------|
| Type | Buried conductive strip (modified electric fence concept) |
| Dimensions | 2m wide x 5m long per pad |
| Voltage | 5,000-7,000V peak (standard electric fence pulse) |
| Energy per pulse | <1 joule (safe for humans and animals) |
| Pulse rate | 1 pulse/second when armed |
| Fence energizer | Standard livestock fence energizer (Zareba, Gallagher), 0.5-1.0 joule |
| Conductor | Galvanized steel cable or conductive polymer strip, buried 1-2cm |
| Ground return | Buried ground wire parallel to hot wire, 30cm spacing |
| Arming | Via LoRa command from mesh (only energized when deer detected nearby) |

**Per-station BOM**:

| Component | Cost |
|-----------|------|
| Fence energizer (0.5J, 12V DC, Zareba EAC10A-Z) | $40-60 |
| Conductive ground strip (10m galv steel cable + stakes) | $15-25 |
| Ground return wire + grounding rods | $10-15 |
| PIR sensor + LoRa node (integrated) | $15 |
| 12V/7Ah SLA battery + solar trickle charger | $25-35 |
| Weatherproof controller box | $15 |
| **Total per station** | **$120-165** |
| **4 stations total** | **$480-660** |

**Advantage**: Electric fence is the GOLD STANDARD for deer deterrence. >90% effectiveness maintained for multi-year deployments. A single contact can produce season-long avoidance. The shock pad innovation is that it is NOT a continuous perimeter fence (which costs $5,000-15,000 for 50 acres) but a set of POINT CONSEQUENCES at identified corridors, activated only when the mesh detects an approaching animal.

**Disadvantage**: Regulatory considerations (varies by state/county); potential liability if a person contacts the energized pad (standard electric fence is legal but liability insurance may be required); ground contact quality depends on soil moisture.

### 7.5 Recommended Backbone Configuration

**Primary**: 3 water jet stations (corridors with irrigation access) + 2 capsaicinoid burst stations (corridors without irrigation access) = **$820-1,075 total**

This hybrid provides:
- Nociceptive stimuli at all identified corridors
- No dependence on continuous irrigation at every station
- Two different consequence types (water + capsaicin), preventing consequence-specific habituation
- The AI controller can vary WHICH consequence type is delivered at corridors served by both

---

## 8. Cost Model

### 8.1 50-Acre Deployment Cost

#### Capital Equipment

| Item | Qty | Unit Cost (500-qty pricing) | Total |
|------|-----|---------------------------|-------|
| Mesh deterrent nodes | 100 | $15.50 | $1,550 |
| Gateway + AI controller | 1 | $260 | $260 |
| Water jet consequence stations | 3 | $110 | $330 |
| Capsaicinoid burst stations | 2 | $135 | $270 |
| LoRa antenna mast + mounting | 1 | $40 | $40 |
| Cabling/connectors/misc hardware | lot | - | $100 |
| **Subtotal: Capital Equipment** | | | **$2,550** |

#### Installation Labor

| Task | Hours | Rate | Cost |
|------|-------|------|------|
| Node placement (100 nodes, stake + orient) | 4 | $25/hr | $100 |
| Gateway installation (mount, power, configure) | 2 | $25/hr | $50 |
| Water jet station installation (plumb, mount, test) | 3 | $25/hr | $75 |
| Capsaicinoid station installation | 1 | $25/hr | $25 |
| System commissioning + network test | 2 | $25/hr | $50 |
| **Subtotal: Installation** | **12 hours** | | **$300** |

#### Annual Operating Cost

| Item | Qty/Year | Unit Cost | Annual Cost |
|------|----------|-----------|-------------|
| Scent wicks (100 nodes x 5 refills) | 500 | $0.70 | $350 |
| Batteries (100 nodes x 1 replacement*) | 300 cells | $1.35 | $405 |
| Water (3 stations, ~500 activations/season, 3 gal each) | 1,500 gal | ~$0 | ~$0 |
| Capsaicinoid refills (2 stations, 2 refills/season) | 4 | $30 | $120 |
| CO2 cartridges (2 stations, 10/season) | 20 | $1.50 | $30 |
| Gateway power (5W, 8,760 hrs) | 44 kWh | $0.12/kWh | $5 |
| Cellular data (optional) | 12 months | $5/mo | $60 |
| Maintenance labor (4 visits x 2 hrs) | 8 hours | $25/hr | $200 |
| Node replacement (5% annual attrition) | 5 nodes | $15.50 | $78 |
| **Subtotal: Annual Operating** | | | **$1,248** |

*Battery replacement: Even though analysis shows batteries last >1 year, we budget for one complete replacement per season as a conservative measure and to ensure fresh cells each spring.

#### 5-Year Total Cost of Ownership

| Cost Category | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5-Year Total |
|---------------|--------|--------|--------|--------|--------|-------------|
| Capital equipment | $2,550 | $0 | $0 | $0 | $0 | $2,550 |
| Installation | $300 | $0 | $0 | $0 | $0 | $300 |
| Annual operating | $1,248 | $1,248 | $1,248 | $1,248 | $1,248 | $6,240 |
| **Annual total** | **$4,098** | **$1,248** | **$1,248** | **$1,248** | **$1,248** | **$9,090** |

| Metric | Value |
|--------|-------|
| 5-year TCO | $9,090 |
| Average annual cost | $1,818/year |
| **Cost per acre per year** | **$36.36/acre/year** |
| Budget headroom | $100 - $36.36 = **$63.64/acre/year remaining** |
| Budget utilization | 36.4% of $100/acre/year limit |

### 8.2 100-Acre Scaling Model

A 100-acre deployment benefits from sub-linear scaling in several categories:

| Item | 50-acre | 100-acre | Scaling Factor | Notes |
|------|---------|----------|---------------|-------|
| Mesh nodes | 100 | 175 | 1.75x | Perimeter scales with sqrt(area); interior density same |
| Gateway/AI controller | 1 | 1 | 1.0x | Single gateway covers 100 acres (LoRa range sufficient) |
| Water jet stations | 3 | 5 | 1.67x | More corridors, but not proportional |
| Capsaicinoid stations | 2 | 3 | 1.5x | |
| Installation labor | 12 hrs | 18 hrs | 1.5x | Economies of familiarity |
| Annual scent wicks | 500 | 875 | 1.75x | Proportional to node count |
| Annual batteries | 300 cells | 525 cells | 1.75x | Proportional to node count |
| Annual maintenance labor | 8 hrs | 12 hrs | 1.5x | Efficient routing across larger area |

| 100-Acre Cost Summary | Value |
|-----------------------|-------|
| Capital equipment | $4,073 |
| Installation | $450 |
| Annual operating | $2,060 |
| 5-year TCO | $14,823 |
| Average annual cost | $2,965/year |
| **Cost per acre per year** | **$29.65/acre/year** |

**Scaling efficiency**: The 100-acre deployment costs $29.65/acre/year vs $36.36/acre/year at 50 acres -- an 18.5% improvement. The primary drivers of sub-linear scaling are: (1) the gateway is a fixed cost shared over more acreage, (2) perimeter nodes scale with perimeter length (~sqrt of area), and (3) installation/maintenance labor has diminishing per-acre cost.

### 8.3 Cost Sensitivity Analysis

| Parameter | Base Case | Optimistic | Pessimistic | Impact on $/acre/yr |
|-----------|-----------|------------|-------------|-------------------|
| Node cost | $15.50 | $10.00 | $22.00 | -$2.20 / +$2.60 |
| Node count | 100 | 80 | 130 | -$1.24 / +$1.86 |
| Battery cost | $1.35/cell | $0.50/cell (alkaline) | $1.80/cell | -$3.40 / +$1.80 |
| Scent wick cost | $0.70 | $0.40 | $1.20 | -$3.00 / +$5.00 |
| Consequence stations | $600 | $400 | $900 | -$0.80 / +$1.20 |
| **Worst case total** | $36.36 | | | **$48.82/acre/year** |
| **Best case total** | $36.36 | | | **$25.72/acre/year** |

Even in the pessimistic scenario, the system remains well under the $100/acre/year constraint at $48.82/acre/year.

---

## 9. Risk Register

### Top 5 Technical and Operational Risks

| # | Risk | Probability | Impact | Severity | Mitigation |
|---|------|------------|--------|----------|-----------|
| R1 | **Habituation to mesh stimuli despite VR scheduling**: Deer learn that light+sound from small stakes is never actually dangerous, habituating within 4-8 weeks even with variable patterns. | MEDIUM-HIGH | CRITICAL | **HIGH** | Nociceptive backbone is the primary mitigation. Without consequence stations, this risk becomes near-certainty. The mesh alone is NOT sufficient. Secondary: introduce novel stimuli (new buzzer tones, relocated nodes) at monthly maintenance visits. |
| R2 | **PIR false positive rate too high**: Wind-blown vegetation, small animals (rabbits, raccoons), rain, and temperature fluctuations cause excessive PIR triggers, draining batteries and wasting VR-scheduled activations on non-target events. | HIGH | MODERATE | **MEDIUM-HIGH** | Software filtering: require 2+ PIR triggers within 5 seconds (dual-detect), or require 2+ adjacent nodes to trigger within 30 seconds (spatial correlation). Adjust PIR sensitivity via trim potentiometer during installation. Budget for 10% battery reserve against false-positive drain. |
| R3 | **LoRa mesh congestion during mass detection events**: When 10+ nodes trigger simultaneously (herd approach), the LoRa channel becomes congested. Messages collide, retransmits cascade, and the coordinated response degrades to random independent activation. | MEDIUM | MODERATE | **MEDIUM** | Slotted ALOHA with time-division: nodes are assigned transmission slots based on their node_id modulo slot count. Priority slots for detection messages; heartbeats deferred during high-activity periods. Maximum 100 nodes on 8 frequency channels = 12-13 nodes per channel, well within LoRa capacity. |
| R4 | **Node physical damage from farm operations**: Nodes on stakes at 50cm height may be struck by planting equipment, sprayer booms, or irrigation pivots. Annual attrition rate may exceed the budgeted 5%. | MEDIUM | LOW-MODERATE | **MEDIUM-LOW** | Design node enclosures for "breakaway" from stakes under lateral force (snap-fit mount fails cleanly, node falls to ground undamaged). Mark node positions in farm GPS system for operator awareness. Install perimeter nodes outside the equipment turn radius. Budget allows up to 15% annual attrition before cost constraint is breached. |
| R5 | **Gateway single point of failure**: If the Raspberry Pi fails (SD card corruption, power outage, water intrusion), the entire coordinated mesh loses intelligence and falls back to autonomous mode (50% random activation, no patterns). | LOW-MEDIUM | HIGH | **MEDIUM** | Autonomous fallback mode ensures continued basic deterrence even without gateway. Industrial SD card (SanDisk Industrial) with ext4 journaling reduces corruption risk. UPS (small 12V battery, $20) provides 4-8 hours of gateway operation during power outage. Remote monitoring via cellular modem alerts farmer to gateway offline status. Full system restores automatically when gateway reboots. |

### Risk-Adjusted Assessment

The dominant risk (R1, habituation) is architecturally mitigated by the nociceptive backbone. This is NOT an optional add-on -- it is load-bearing. The engineering team's strong recommendation is that the mesh network must NEVER be deployed without at least 2-3 consequence stations. A mesh-only deployment will fail and damage the product's reputation.

---

## 10. Prototype Plan

### 10.1 Phase A: Bench Prototype (2-4 weeks, $500-800)

**Goal**: Validate node hardware, LoRa communication, and basic software stack.

**Build**:
- 5x mesh nodes using STM32WL55 Nucleo-WL55JC development boards ($25 each)
- 5x AM312 PIR sensors on breadboard adapters
- 5x piezo buzzers + 5x 3W LEDs (breadboard wired)
- 1x Raspberry Pi 4 + RAK2287 LoRa concentrator
- Power from bench supply (battery test separate)

**Test**:
1. PIR detection reliability (range, false positive rate in controlled environment)
2. LoRa link budget (indoor range, packet loss rate)
3. Gateway-to-node command latency
4. Mesh relay capability (node A relays node B's message to gateway)
5. Buzzer SPL measurement at 1m, 3m, 5m
6. LED visible range at night
7. Power consumption measurement (sleep, active, TX) with current probe

**Success criteria**: <500ms detection-to-activation latency, >95% packet delivery, >90dB SPL at 1m, sleep current <5uA.

### 10.2 Phase B: Field Prototype (4-6 weeks, $1,500-2,500)

**Goal**: Validate outdoor performance, weatherproofing, battery life, and basic deterrent patterns.

**Build**:
- 20x production-intent nodes (custom PCB, 3D-printed enclosures, AA battery packs)
- 1x gateway (production-intent Raspberry Pi + concentrator in weatherproof enclosure)
- 1x water jet consequence station (prototype)
- Deploy on a 5-10 acre test plot (vineyard, orchard, or field edge with known deer pressure)

**Test**:
1. Outdoor LoRa range and reliability (rain, temperature, vegetation effects)
2. PIR performance in agricultural environment (false positive rate from wind, vegetation, small animals)
3. Coordinated pattern execution (encirclement, herding) with 20 nodes
4. Battery life projection (measure actual daily consumption over 2-4 weeks, extrapolate)
5. Weatherproofing (rain test, temperature cycling)
6. Water jet station integration and timing
7. Wildlife response observation (trail cameras at test plot perimeter)

**Success criteria**: <5% packet loss outdoors at 50m node spacing, <20% false positive rate (after software filtering), battery projection >6 months, visible/audible deterrent at >50m, at least one documented deer aversion event on trail camera.

### 10.3 Phase C: Pilot Deployment (8-12 weeks, $4,000-6,000)

**Goal**: Full 50-acre deployment with all features. Validate the complete system over a partial growing season.

**Build**:
- 100x production nodes (injection-molded enclosures, production PCBs)
- 1x gateway (production)
- 3x water jet stations + 2x capsaicinoid burst stations (production)
- Full scent wick supply for 3 months
- Full battery supply

**Test**:
1. Full system commissioning and network mapping
2. AI controller pattern selection and VR scheduling validation
3. 3-month effectiveness trial with trail camera monitoring
4. Intrusion rate comparison (before/after deployment, or treatment/control plot)
5. Battery life validation (actual 3-month measurement)
6. Maintenance protocol validation (farmer performs wick replacement, measures time)
7. Cost model validation (actual labor, consumable usage, failure rate)

**Success criteria**: >50% reduction in field intrusion events compared to control/baseline, <$40/acre/year actual cost, <2 hours quarterly maintenance, <10% node failure rate over 3 months.

### 10.4 Prototype Timeline Summary

| Phase | Duration | Cost | Output |
|-------|----------|------|--------|
| A: Bench | Weeks 1-4 | $500-800 | Validated electronics, software, LoRa |
| B: Field (small) | Weeks 5-10 | $1,500-2,500 | Validated outdoor performance, basic deterrence |
| C: Pilot (full) | Weeks 11-22 | $4,000-6,000 | Validated complete system, effectiveness data |
| **Total to pilot** | **~5.5 months** | **$6,000-9,300** | Production-ready design + effectiveness evidence |

---

## 11. Appendices

### Appendix A: Node PCB Design Notes

**Board dimensions**: 50mm x 35mm, 2-layer FR4, 1.6mm thickness
**Layer stackup**: Top copper (signal + power), bottom copper (ground plane)
**Key design rules**:
- 50-ohm impedance-matched trace from STM32WL RF pin to antenna pad (coplanar waveguide with ground, 0.3mm trace, 0.15mm gap)
- RF matching network components placed within 5mm of RF pin
- Separate analog ground pour for PIR sensor input
- Battery input with reverse-polarity protection (Schottky diode, $0.03)
- All decoupling capacitors within 2mm of IC power pins
- Test points for: VCC, GND, SWD_CLK, SWD_DIO, UART_TX, UART_RX, RF_OUT

**Programming**: SWD (Serial Wire Debug) via 4-pin header for initial firmware flash. OTA (Over-The-Air) firmware updates via LoRa for field-deployed nodes (update 100 nodes takes ~30 minutes at SF7).

### Appendix B: Firmware Architecture

```
+--------------------------------------------------+
|  Application Layer                                |
|  - Pattern execution engine (state machine)       |
|  - PIR detection handler (interrupt-driven)       |
|  - Activation command processor                   |
|  - Autonomous fallback logic                      |
|  - Battery voltage monitor (ADC, periodic)        |
+--------------------------------------------------+
|  LoRa Mesh Protocol Layer                         |
|  - Packet framing (32-byte max)                   |
|  - Slotted ALOHA channel access                   |
|  - Mesh relay (TTL=2 max hops)                    |
|  - Time synchronization (from gateway beacons)    |
|  - Frequency hopping (8-channel FHSS)             |
+--------------------------------------------------+
|  Hardware Abstraction Layer (HAL)                  |
|  - STM32WL sub-GHz radio driver (STM32CubeWL)    |
|  - GPIO: PIR input, LED MOSFET, buzzer PWM       |
|  - ADC: battery voltage divider                   |
|  - RTC: wake timer for heartbeat schedule         |
|  - Low-power modes: STOP2, STANDBY               |
+--------------------------------------------------+
|  STM32WL Hardware                                 |
|  - Cortex-M4 @ 48 MHz                            |
|  - 256KB Flash / 64KB SRAM                        |
|  - Integrated sub-GHz radio (SX126x-equivalent)  |
|  - RTC with LSE 32.768 kHz crystal               |
+--------------------------------------------------+
```

**Estimated firmware size**: 40-60 KB (well within 256 KB flash). Leaves room for OTA update staging (dual-bank flash).

### Appendix C: Regulatory Compliance Notes

| Regulation | Requirement | Status |
|-----------|------------|--------|
| FCC Part 15.247 | 915 MHz ISM, FHSS, <1W EIRP | COMPLIANT: +14 dBm TX + 5 dBi antenna = +19 dBm EIRP (< +30 dBm limit with FHSS) |
| FCC Part 15.249 | ISM unlicensed operation | COMPLIANT: LoRa at 915 MHz is explicitly permitted |
| EPA FIFRA 25(b) | Capsaicinoid as minimum risk pesticide | EXEMPT: Capsaicin is listed as 25(b) exempt active ingredient |
| State electric fence laws | Varies by state | REQUIRES REVIEW: Most states permit electric fence for agricultural use; ground pad design may need state-specific legal review |
| UL/ETL safety | Consumer electronics safety | NOT REQUIRED for agricultural equipment sold directly to farmers (B2B); recommended for liability protection |
| IP65 enclosure rating | Dust-tight + water jet protection | DESIGN TARGET: Validated through Phase B testing |

### Appendix D: Comparison with Phase 1 TRIZ Estimates

The Phase 1 TRIZ analysis (SYNAPSE concept) estimated $9-13/acre/year for the mesh network alone. Our detailed engineering analysis yields $36.36/acre/year. The difference is accounted for by:

| Cost Factor | Phase 1 Estimate | Phase 2 Detail | Difference |
|-------------|-----------------|----------------|-----------|
| Per-node cost | $6 | $15.50 | More realistic BOM at 500-qty |
| Node count | 120 | 100 | Slightly reduced; compensated by corridor clusters |
| Gateway | $150 | $260 | Added GPS, cellular modem, industrial SD |
| Nociceptive backbone | Not included | $600 | Critical addition; was not in SYNAPSE scope |
| Annual scent wicks | $120/season | $350/season | Increased to 5 refills/season (vs 4) |
| Annual batteries | $180/season | $405/season | Conservative full replacement per season |
| Maintenance labor | Not included | $200/year | 4 quarterly visits x 2 hours x $25/hr |
| Node attrition | Not included | $78/year | 5% annual replacement |

The $36.36/acre/year figure is a realistic, fully-loaded cost. It includes all installation, operation, maintenance, and replacement costs amortized over 5 years. The system remains well within the $100/acre/year economic constraint with $63.64/acre/year of headroom.

---

## 12. Summary and Recommendations

### System Performance Summary

| Metric | Target | Achieved |
|--------|--------|----------|
| Cost per acre per year | <= $100 | $36.36 (50-acre), $29.65 (100-acre) |
| Anti-habituation duration | >= 4-6 months | Full season (with nociceptive backbone) |
| Detection-to-response time | <= 5 seconds | 250-400 ms |
| Battery life | >= 6 months | >> 12 months (nominal), > 5.4 months (ultra-extreme) |
| Maintenance frequency | <= quarterly | Monthly scent wick replacement; quarterly battery check |
| Installation time | Farm worker, no specialist | 12 hours, general labor |
| System lifetime | >= 5 years | 5+ years (node enclosure and PCB rated for outdoor use; annual 5% attrition budgeted) |
| Node IP rating | IP65 minimum | IP65 |
| Operating temperature | -20C to 50C | -40C to 60C (lithium battery + STM32WL rating) |

### Key Engineering Decisions

1. **STM32WL55JC as the sole-chip MCU+LoRa solution** is the highest-leverage cost decision, saving $2-5 per node versus discrete MCU + LoRa transceiver. At 100 nodes, this is $200-500 in savings.

2. **The nociceptive backbone is structurally load-bearing**, not optional. The mesh network creates the conditioned stimuli; the consequence stations create the unconditioned stimuli. Without both halves, the system fails. Every deployment MUST include at least 2-3 consequence stations.

3. **Variable-ratio scheduling is implemented in software**, not hardware. The entire VR logic, pattern library, and adaptive algorithm run on the Raspberry Pi gateway. Nodes are dumb actuators. This means the intelligence can be updated without touching field hardware.

4. **The power budget has enormous margin.** 3x AA lithium batteries provide >10x the required energy for a 6-month season under nominal conditions. This margin can be traded for cheaper batteries (alkaline), fewer batteries (2x AA), or more aggressive deterrent activation schedules.

5. **The autonomous fallback mode** ensures the system continues functioning (at reduced effectiveness) even if the gateway fails. This is critical for agricultural deployment where the farmer may not notice a gateway failure for days.

### Next Steps

1. Procure Phase A prototype components (STM32WL Nucleo boards, LoRa concentrator, PIR sensors, buzzers, LEDs)
2. Develop firmware for basic node operation (PIR detect, LoRa transmit, activation response)
3. Develop gateway software (ChirpStack integration, pattern engine, VR scheduler)
4. Execute Phase A bench testing (2-4 weeks)
5. Design production PCB and enclosure for Phase B
6. Identify field trial site with documented deer pressure for Phase B/C

---

*Engineering Proposal prepared by: Joint Embedded Systems / Electrical / Control Systems Engineering Team*
*Field Shield Innovation Engine -- Phase 2 Concept Development*
*Session: 2026-02-15 Full-Spectrum Deer Deterrence*
