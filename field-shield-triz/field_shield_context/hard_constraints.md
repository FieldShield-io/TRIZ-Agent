# Field Shield — Engineering & Economic Constraints

## Primary Economic Constraint (BINDING)
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Cost per acre per year | ≤ $100/acre/year | The single most important constraint. ALL designs must meet this. |
| Standard block size | 50 acres | Primary design unit for costing and coverage |
| Annual block cost | ≤ $5,000/year | 50 acres × $100/acre |

## Capital & Operating Budget
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Capital equipment (5yr amortization) | ≤ $15,000 total | $3,000/year × 5 years for a 50-acre block |
| Capital equipment (3yr amortization) | ≤ $9,000 total | $3,000/year × 3 years for a 50-acre block |
| Annual operating cost | ≤ $2,000/year | Maintenance, consumables, connectivity, power |
| Installation cost | ≤ $2,000 one-time | Professional or farmer-installed |
| Farmer ROI payback | ≤ 2 years | Based on crop damage prevented vs. total cost |

## Scalability
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Cost scaling | Sub-linear preferred | Adding 50 more acres should cost < 2× first 50 |
| Coverage completeness | ≥ 90% of block area | Gaps in coverage will be exploited by wildlife |
| Node/unit density | Minimize | Fewer nodes = lower maintenance burden |

## Environmental
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Operating temp range | -20°C to 50°C | Continental US four-season agriculture |
| Weather resistance | Rain, snow, dust, UV | Multi-year outdoor deployment |
| Wind survival | ≥ 50 mph gusts | Open agricultural field conditions |

## Performance — Detection
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Detection range | ≥ 100m per node (soft) | Longer range = fewer nodes = lower cost |
| Response time | ≤ 5s detection to deterrent | Slower acceptable if deterrent is highly effective |
| Classification accuracy | ≥ 85% | Distinguish target species from humans/livestock/vehicles |
| False positive rate | ≤ 10% | Farmer tolerance for nuisance activations |

## Performance — Deterrent
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Anti-habituation duration | ≥ 1 full growing season | Minimum 4-6 months effective without performance decay |
| Species coverage | Deer + hogs minimum | Birds as bonus capability |
| Human/livestock safety | Zero harm | System must never injure people or farm animals |
| Regulatory compliance | No restricted chemicals/frequencies | Must comply with EPA, FIFRA, FCC, state wildlife regs |

## Power & Infrastructure
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Power source | Mains/grid preferred | Commercial farms have grid power available |
| Solar/battery acceptable | Yes, if cost target met | Not excluded, but not required |
| Infrastructure dependency | Document clearly | If solution requires irrigation/fencing, state it |

## Maintenance & Operations
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Maintenance frequency | ≤ quarterly | Farmer time is scarce during growing season |
| Maintenance skill level | General farm worker | No specialized technician required |
| System lifetime | ≥ 5 years | Minimum for amortization model to work |
| Seasonal deployment | Acceptable | System can be deployed/removed seasonally if needed |

## Manufacturing & Supply Chain
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Component availability | No sole-source critical parts | Supply chain resilience |
| Manufacturing complexity | Contract-manufacturable | Standard PCB assembly, injection molding, etc. |
| Volume target | 100-1000 unit runs initially | Must be economical at relatively low volumes |
