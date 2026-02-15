# Field Shield System Overview

## Product Description
Field Shield is an autonomous wildlife deterrence system designed for agricultural crop protection. It combines AI-powered thermal imaging, motorized pan-tilt scanning, and multi-modal acoustic deterrents on NVIDIA Jetson edge computing hardware to detect and deter crop-damaging wildlife (primarily white-tailed deer and wild hogs) without lethal means.

## Core Architecture

### Sensor Stack
- **Primary sensor**: Uncooled LWIR thermal camera (640×512 or 320×256 resolution, 8-14μm spectral range)
- **Secondary sensor**: Optional visible-light camera for daytime classification enhancement
- **Field of view**: 24° HFOV thermal lens on pan-tilt for 360° coverage via scanning

### Compute Platform
- **Processor**: NVIDIA Jetson Orin Nano (7-15W configurable TDP)
- **AI framework**: TensorRT-optimized YOLO-based detector + custom wildlife classifier
- **Messaging**: ZeroMQ inter-process communication between sensor acquisition, AI inference, tracking, and deterrent control
- **Storage**: microSD for model weights + optional NVMe for recording

### Actuation
- **Pan-tilt**: Dual-axis motorized gimbal (360° continuous pan, ±90° tilt)
- **Acoustic deterrent**: Weather-rated horn speaker array (100dB SPL @ 1m, 200-8000Hz)
- **Deterrent modes**: Species-specific sound sequences, random timing to prevent habituation

### Power System
- **Primary**: 100W monocrystalline solar panel
- **Storage**: 12V 100Ah LiFePO4 battery
- **Regulation**: MPPT charge controller with load management
- **Target**: 24/7 autonomous operation in 5+ hours effective sun

### Connectivity
- **Primary**: 4G LTE cellular modem (alerts, telemetry, remote management)
- **Fallback**: Local WiFi AP for field configuration
- **Protocol**: MQTT for telemetry, HTTPS REST API for management

### Enclosure
- **Rating**: IP65 minimum (IP67 target)
- **Material**: UV-stabilized ASA or polycarbonate housing
- **Mounting**: Universal T-post bracket + tripod adapter
- **Thermal management**: Passive heat sinks + optional thermostatically controlled fan

## Deployment Context
- **Environment**: Open agricultural fields (row crops, orchards, vineyards)
- **Climate**: USDA hardiness zones 3-9 (continental US primary market)
- **Installation**: Single person, no specialized tools, <30 minutes
- **Maintenance**: Seasonal lens cleaning, annual battery health check
- **Target users**: Commercial farmers, farm managers, agricultural cooperatives

## Key Design Tensions
The fundamental engineering challenges arise from competing requirements that map directly to TRIZ contradictions:

1. **Range vs. Weight**: Longer detection requires larger optics → heavier payload
2. **Speed vs. Energy**: Faster pan-tilt response requires more power
3. **Effectiveness vs. Sustainability**: Louder deterrents → more power + animal habituation
4. **Durability vs. Thermals**: Sealed weatherproof enclosure → internal heat buildup
5. **Throughput vs. Thermal Budget**: Faster AI inference → higher Jetson power/heat
6. **Autonomy vs. Maintainability**: More automation → more complexity → harder to repair
