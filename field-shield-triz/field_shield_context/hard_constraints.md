# Field Shield — Hard Engineering Constraints

## Power Budget
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Average power | ≤ 15W | Solar/battery budget for 24hr operation |
| Peak power | ≤ 60W | During deterrent + AI + pan-tilt simultaneous |
| Standby power | ≤ 8W (target) | Nighttime idle surveillance |

## Physical
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Total weight | ≤ 25 lbs | Single-person installation |
| Payload weight | ≤ 12 lbs | Pan-tilt mechanism limit |

## Environmental
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Operating temp | -20°C to 60°C | Continental US four-season |
| IP rating | ≥ IP65 | Dust-tight + water jet protection |
| Wind survival | ≥ 50 mph gusts | Agricultural field conditions |

## Performance
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Detection range | ≥ 200m | Deer-sized (1.5m) targets |
| Response time | ≤ 2s | Detection → deterrent activation |
| Classification accuracy | ≥ 90% | Deer/hog vs. human/vehicle/livestock |
| False positive rate | ≤ 5% | Farmer tolerance threshold |

## Compute
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Jetson TDP | ≤ 15W | Orin Nano max power mode |
| Inference FPS | ≥ 5 fps | Minimum for reliable tracking |

## Cost
| Parameter | Limit | Notes |
|-----------|-------|-------|
| Unit BOM cost | ≤ $2,500 | Target retail $4,000-$5,000 |
| Annual operating | ≤ $200/yr | Connectivity + maintenance |

## Acoustic Deterrent
| Parameter | Limit | Notes |
|-----------|-------|-------|
| SPL at 100m | ≥ 70 dB | Audible/startling to deer |
| Frequency range | 200-8,000 Hz | Deer hearing sensitivity |
