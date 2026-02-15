# Field Shield — Known TRIZ Contradictions

## Pre-Mapped Contradiction Analysis

Each row maps a real Field Shield engineering challenge to the TRIZ 39-feature framework.

| # | Challenge | Improving Feature | Worsening Feature | TRIZ Tension | Priority |
|---|-----------|-------------------|-------------------|--------------|----------|
| 1 | Longer detection range requires bigger/heavier thermal optics | Measurement accuracy (#28) | Weight of stationary object (#2) | Range vs. Weight | HIGH |
| 2 | Faster pan-tilt response draws more power from battery | Speed (#9) | Use of energy by moving object (#19) | Speed vs. Energy | HIGH |
| 3 | Louder acoustic deterrent increases power draw and causes habituation | Force/Intensity (#10) | Loss of Energy (#22), Adaptability (#35) | Effectiveness vs. Sustainability | HIGH |
| 4 | Weatherproof sealed enclosure traps heat from electronics | Reliability (#27) | Temperature (#17) | Durability vs. Thermals | CRITICAL |
| 5 | Faster AI inference on Jetson increases power consumption and heat | Productivity (#39) | Temperature (#17), Use of energy (#20) | Throughput vs. Thermal Budget | CRITICAL |
| 6 | More autonomous operation adds complexity and repair difficulty | Extent of automation (#38) | Ease of repair (#34), Device complexity (#36) | Autonomy vs. Maintainability | MEDIUM |
| 7 | Higher classification accuracy requires larger ML models = more compute | Measurement accuracy (#28) | Use of energy by stationary object (#20) | Accuracy vs. Power | HIGH |
| 8 | Solar power requires large panel area = wind loading on mount | Power (#21) | Area of stationary object (#6), Strength (#14) | Power Generation vs. Structural | MEDIUM |
| 9 | Longer battery life = more weight on mounting system | Duration of action by stationary object (#16) | Weight of stationary object (#2) | Runtime vs. Weight | MEDIUM |
| 10 | Wider deterrent coverage = more speakers = more weight + power | Area of moving object (#5) | Weight of stationary object (#2), Power (#21) | Coverage vs. System Budget | LOW |

## Contradiction Categories

### Thermal-Power Nexus (Contradictions #4, #5, #7)
These three contradictions are deeply coupled — solving one often worsens another. The Jetson's thermal dissipation is the binding constraint. Any solution must address the thermal-power nexus holistically rather than in isolation.

### Detection-Weight Tradeoff (Contradictions #1, #8, #9)
Optical performance, structural integrity, and runtime all compete for the weight and volume budget. Solutions here often involve material science or novel optical architectures.

### Effectiveness-Sustainability Loop (Contradiction #3)
The deterrent habituation problem is unique to wildlife applications — louder/more frequent deterrence works short-term but fails long-term. This requires solutions from behavioral science as much as engineering.

## Unexplored Contradiction Opportunities

The following tensions have not yet been formally analyzed but represent potential innovation areas:

- **Connectivity reliability vs. power budget**: Cellular modem draws significant standby power
- **Manufacturing simplicity vs. field adaptability**: Standard enclosure vs. mounting flexibility for different crops/terrains
- **Data privacy vs. connectivity**: Farmer data transmitted over cellular vs. edge-only processing
- **Cost vs. multi-species effectiveness**: Supporting deer + hog + bird deterrence with minimal additional hardware
