**Hardware Architecture - Overview**

---

**Project Hardware Architecture: Autonomous Edge AI Animal Detection and Deterrence System**

**1. Introduction**

This document details the hardware architecture for the autonomous edge AI animal detection and deterrence system. It outlines the major subsystems, specific components selected, their primary functions, and key interconnections. This architecture is designed to support autonomous operation deployed on a commercial irrigation system with dedicated mains power.

**2. System Overview Diagram (Conceptual)**

The system comprises several interconnected subsystems:

* **Power Subsystem:** Receives dedicated AC power from the commercial irrigation system's mains supply and distributes appropriate DC power to all other components via conversion and distribution hardware.
* **Compute Subsystem (Jetson):** Executes the AI models, control logic, and microservices.
* **Sensing/Ranging/Targeting Subsystem (Aeron LRF):** Performs environmental sensing (Thermal/Visual), measures target distance (LRF), and positions sensors (PTZ).
* **Aerial Surveillance Subsystem (Autel EVO Max 4T V2):** Provides deployable aerial thermal/visual surveillance and reconnaissance capability for extended area coverage and deployment of repellents.
* **Deterrent Positioning Subsystem (MPT90):** Aims the acoustic deterrent based on commands from Compute.
* **Deterrent Actuation Subsystem (HyperSpike HS-18):** Emits highly directional acoustic signals based on commands from Compute.
* **Connectivity Subsystem (AirLink XR60):** Provides ruggedized 5G cellular and Wi-Fi 6 WAN connectivity.
* **Networking Subsystem (Switch):** Facilitates local communication between Ethernet-based devices.
* **Enclosures & Mounting:** Protects components and provides physical structure integrated with the irrigation infrastructure.

**3. Compute Subsystem**

* **Component:** Syslogic NVIDIA Jetson Orin Nano (on appropriate carrier board).
* **Function:** Central processing unit. Executes the containerized microservices (AI inference via DeepStream/TensorRT, hardware control, system orchestration, communication management).
* **Interfaces:**
  * Ethernet: Connects to the local network switch for communication with other devices.
  * Power Input: Receives regulated DC power from the Power Distribution unit.
  * (Potentially USB/Serial if needed for direct hardware connection, though current plan uses Ethernet).

**4. Sensing, Ranging & Targeting Subsystem**

* **Component:** Silent Sentinel Aeron LRF.
* **Function:** Primary sensor suite. Provides thermal video, HD visual video (30x zoom), precise distance measurement via Laser Range Finder (LRF), and integrated Pan-Tilt-Zoom (PTZ) for scanning and sensor aiming.
* **Interfaces:**
  * Ethernet: Connects to the switch for sending video/LRF data and receiving PTZ control commands from the Jetson.
  * Power Input: Requires 24-32VDC (nominal 28V) from Power Distribution.

**5. Aerial Surveillance Subsystem**

* **Component:** Autel Robotics EVO Max 4T V2 Rugged Bundle.
* **Function:** Deployable aerial surveillance platform providing multi-sensor reconnaissance over the coverage area. Extends detection capability beyond the fixed Aeron LRF field of view. Equipped with four integrated sensors: wide-angle camera (50MP, 1/1.28" CMOS, 85° FOV), zoom camera (48MP, 10x optical / 160x hybrid zoom), thermal camera (640×512 uncooled VOx microbolometer, 42° FOV, temperature measurement -20°C to 550°C), and laser range finder (±1m accuracy, 1.2km range). Supports multi-target recognition and tracking (people, wildlife, vehicles; up to 64 simultaneous targets, >85% accuracy). Includes 720° obstacle avoidance and GNSS navigation (GPS+Galileo+BeiDou+GLONASS).

Deployment of reppellent in real-time for deterence.

* **Key Specifications:**
  * Max Flight Time: 42 minutes.
  * Max Transmission Distance: 20km (FCC) / 7km (CE) via Smart Controller V3.
  * Max Wind Resistance: 27 mph (12 m/s).
  * Operating Temperature: -4°F to 122°F (-20°C to 50°C).
  * IP Rating: IP43.
  * Service Ceiling: 23,000 ft.
  * Internal Storage: 128GB.
  * Operating Frequency: 2.4GHz / 5.2GHz / 5.8GHz / 900MHz (FCC).
* **Bundle Contents:** EVO Max 4T V2 aircraft, ABX41-D intelligent battery, battery charger, Smart Controller V3 (7.9" 2000-nit display), propellers (3 pairs), rugged carrying case, cables, and accessories.
* **Interfaces:**
  * RF Link: SkyLink communication to Smart Controller V3 for live video and telemetry.
  * Smart Controller V3: Wi-Fi Direct / 802.11a/b/g/n/ac (2×2 MIMO) for integration with the Jetson or AirLink XR60 network.
  * Power: Battery-powered (onboard intelligent LiPo); charges via included charger connected to AC mains through the Power Distribution subsystem.

**6. Deterrent Positioning Subsystem**

* **Component:** Quickset MPT90 PTU.
* **Function:** Precisely positions the HyperSpike HS-18 based on aiming coordinates received from the Jetson.
* **Interfaces:**
  * Ethernet: Connects to the switch for receiving control commands from the Jetson.
  * Power Input: Requires 24-32VDC from Power Distribution.
  * Payload Mount: Mechanical interface for mounting the HyperSpike HS-18.
  * (Payload Communication Ports available if needed, but HS-18 control is planned via separate connection).

**7. Deterrent Actuation Subsystem**

* **Component:** HyperSpike HS-18 Acoustic Hailing Device.
* **Function:** Emits highly directional acoustic signals (voice commands, alert tones) to deter animals at long range with exceptional clarity. Features a narrow beam width for precise targeting and an integrated Opti-Port equipment bay for optional sensors (camera, searchlight).
* **Key Specifications:**
  * Sound Pressure Level: 156 dB peak (A-weighted) at 1 meter.
  * Communication Range: Up to 3,000 meters.
  * Beam Width: ±5° (10° conical at 2 kHz / -3 dB).
  * Frequency Response: 245 Hz – 10 kHz, optimized for human voice.
  * Speech Transmission Index (STI): 0.96 out of 1.0.
  * Built-in high-frequency alert tone.
  * Dimensions (Emitter Head): 20" diameter × 18.3" depth (50.8 cm × 46.5 cm).
  * Dimensions (Opti-Port Bay): 5.75" diameter × 5.5" depth (14.6 cm × 14.0 cm).
  * Weight (Emitter Head): 90 lbs (40.8 kg).
  * Housing: Carbon fiber construction; available in Navy Gray, Desert Tan, or custom.
  * Environmental: MIL-STD-810F rated (temperature, vibration, shock, rain, humidity, salt fog).
* **Interfaces:**
  * Audio Input: Dynamic mic level (600–1kΩ, balanced twisted pair); integrated record/play microphone; integrated MP3 player; HS Audio App (Google Play / Apple Store) for configuration.
  * Power Input: 100-250 VAC, 50/60 Hz (2.4A typical voice / 4.0A max tone at 110V). Powered from AC mains via the Power Distribution subsystem.
  * Mounting Interface: Saddle bracket (included) attaches to the MPT90 PTU.

**8. Connectivity Subsystem**

* **Component:** Semtech AirLink® XR60 Ultra-Compact Rugged 5G and Wi-Fi 6 Cellular Router.
* **Function:** Provides Wide Area Network (WAN) connectivity via 5G cellular for remote communication between the management-service on the Jetson and the cloud backend. Enables remote monitoring, management, and over-the-air updates. Optional Wi-Fi 6 (2×2 MIMO) for local wireless connectivity. Runs AirLink OS with secure remote management via AirLink Management Service (ALMS).
* **Key Specifications:**
  * Cellular: 5G Sub-6 and mmWave.
  * Wi-Fi: 802.11ax (Wi-Fi 6), 2×2 MIMO (optional module).
  * Ethernet: Single Ethernet (1 Gbps) or Dual Ethernet (1 Gbps + 5 Gbps) depending on configuration.
  * Firewall Throughput: 800 Mbps TCP.
  * GNSS: Dual-band.
  * IP Rating: IP64.
  * Networking Features: IPv4/IPv6 routing, NAT, port forwarding, DHCP, IP passthrough, LAN segmentation, policy-based routing, static routing, WAN Ethernet, QoS.
  * Security: Stateful firewall, WPA2/3, 802.1x/RADIUS, VPN support, secure firmware update.
  * Management: AirLink Complete — 5-year hardware warranty, technical support, and ALMS remote management included.
* **Interfaces:**
  * Ethernet: Connects to the local network switch (1 Gbps or 5 Gbps port).
  * Cellular Antenna: External 5G antenna connections.
  * GNSS Antenna: External GNSS antenna connection.
  * Power Input: DC power from Power Distribution (specific voltage per datasheet).

**9. Power Subsystem**

* **Source:**
  * The system is deployed on a commercial irrigation infrastructure with dedicated AC power from the electrical mains. No solar generation or battery storage is required.
* **Distribution/Conversion:**
  * Component: AC-DC Power Supply, DC-DC Converters, Circuit Breakers/Fuses, Busbars, Wiring. *Specific models TBD.*
  * Function: Receives AC mains power and converts it to the specific voltages required by each component. Provides regulated 24-32VDC for the Aeron LRF and MPT90 PTU, regulated DC for the Jetson carrier board, DC for the AirLink XR60 router, DC for the Ethernet switch, and AC passthrough (100-250 VAC) for the HyperSpike HS-18. Also provides AC power for the Autel drone battery charger. Includes overcurrent protection on all circuits. Housed within the main equipment enclosure.

**10. Networking Subsystem**

* **Component:** Industrial Ethernet Switch. *Specific model TBD.* (Consider managed switch for diagnostics; PoE optional if any device supports it, but likely not needed based on specs).
* **Function:** Provides local network connectivity, interconnecting the Jetson, Aeron LRF, MPT90 PTU, AirLink XR60 router, and Smart Controller V3 (when connected via Ethernet/Wi-Fi bridge).
* **Interfaces:** Multiple Ethernet ports (RJ45), Power Input (DC from Power Distribution).

**11. Enclosures & Mounting**

* **Main Equipment Enclosure:** NEMA-rated outdoor enclosure to house the Jetson system, Ethernet Switch, Power Distribution/Conversion components, and AirLink XR60 router. Provides environmental protection and physical security. Mounted to existing irrigation infrastructure or adjacent permanent structure.
* **Sensor/Deterrent Mast:** Structure to mount the Aeron LRF, MPT90/HS-18 assembly, and cellular/GNSS antennas at the required height. Integrated with or adjacent to the irrigation system infrastructure.
* **Drone Station:** Designated storage and charging area for the Autel EVO Max 4T V2 in its rugged case, with AC power access for the battery charger. Located within or adjacent to the main equipment enclosure.

**12. Interconnections Summary**

* **Data/Control:** All primary wired components (Jetson, Aeron, MPT90, AirLink XR60, Smart Controller V3) connect via Ethernet cables to the central Ethernet Switch. The HyperSpike HS-18 receives audio signals via wired audio input. The Autel EVO Max 4T V2 communicates via RF link to the Smart Controller V3, which bridges to the local network.
* **Power:** The Power Distribution unit, fed by the commercial irrigation system's AC mains, provides individual, voltage-converted, and protected power lines to each component (Jetson, Aeron, MPT90, AirLink XR60, Switch). The HyperSpike HS-18 receives AC power directly through the distribution unit. The Autel drone battery charger receives AC power from the distribution unit.
* **Mechanical:** The HyperSpike HS-18 mounts to the MPT90 via the included saddle bracket. The Aeron LRF and MPT90/HS-18 assembly mount to the sensor/deterrent mast. Enclosures mount to existing irrigation infrastructure or adjacent permanent structures. Cellular and GNSS antennas mount to the mast or enclosure as required.
