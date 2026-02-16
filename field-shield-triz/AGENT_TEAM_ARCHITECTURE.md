# Field Shield TRIZ Innovation Engine — Agent Team Architecture (v2)

## Claude Desktop Optimized Multi-Agent System for Novel Concept Research

This document describes the agent team assembled to implement the Field Shield TRIZ Innovation Engine, optimized for Claude Desktop (Cowork mode). **Version 2** refocuses the entire system on novel concept research at $100/acre/year economics.

---

## Design Philosophy

### v1 → v2 Paradigm Shift

| Aspect | v1 (Deprecated) | v2 (Current) |
|--------|-----------------|--------------|
| **Goal** | Optimize existing architecture | Invent fundamentally new approaches |
| **Architecture** | Locked to solar/battery/Jetson/acoustic | Architecture-agnostic |
| **Cost target** | $2,500 BOM per unit | $100/acre/year at 50-acre scale |
| **Power** | Solar/battery constrained (≤15W) | Mains power available |
| **Primary constraint** | Thermal management of Jetson | Economics ($100/acre/year) |
| **Research method** | Domain engineering within existing arch | Cross-domain inspiration + TRIZ |
| **Anti-habituation** | Secondary concern | Primary technical challenge |

---

## Architectural Translation

### Original (LangGraph) → Claude Desktop Optimized

| Original (LangGraph) | Claude Desktop Optimized | Advantage |
|---|---|---|
| LangGraph `StateGraph` orchestration | Claude main thread as Project Manager | No Python runtime dependency, natural conversation flow |
| `create_agent_node()` + `call_agent_model()` | `Task` tool subagent dispatch | Built-in parallelism, automatic context isolation |
| LangChain `@tool` wrappers for TRIZ | Python CLI scripts via `Bash` tool | Simpler, no LangChain dependency, directly testable |
| `TavilySearch` LangChain tool | Built-in `WebSearch` / `WebFetch` tools | Native integration, no API key management |
| No HITL gates | `AskUserQuestion` tool at 3 gate points | Built-in human approval workflow |
| `hub.pull()` external prompts | Local markdown files in `prompts/` | Full control, no LangChain Hub dependency |
| `delete_messages` context management | Subagent natural isolation via Task tool | Each agent runs in its own context window |

---

## Agent Team Roster (14 Agents)

### Tier 1: Orchestration

#### Project Manager (Claude Main Thread)
- **Implementation**: Claude's primary conversation thread
- **Function**: Orchestrates innovation sessions, dispatches specialists, enforces $100/acre/year economics, manages HITL gates
- **Tools**: All tools (Task dispatch, AskUserQuestion, Bash, Read, Write, WebSearch)
- **Workflow guide**: `SKILL.md`
- **Prompt**: `prompts/project_manager.md`

### Tier 2: TRIZ Core + Domain Grounding

#### TRIZ Specialist
- **Function**: Applies TRIZ methodology — identifies contradictions, maps inventive principles, drives cross-domain solution generation
- **Tools**: Bash (triz_toolkit.py), WebSearch, Read
- **Prompt**: `prompts/triz_specialist.md`
- **Dispatch trigger**: Phase 1 (Problem Framing), Phase 2 (Concept Development)

#### AgTech Domain Expert
- **Function**: Wildlife behavior, habituation science, crop economics, farmer needs, regulatory landscape
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/agtech_domain_expert.md`
- **Dispatch trigger**: Phase 1 (grounds analysis in agricultural reality), Phase 2 (evaluates anti-habituation)

### Tier 3: Domain Engineers (Architecture-Agnostic)

#### Mechanical Engineer
- **Function**: Physical systems, field structures, mounting, materials, installation, infrastructure reuse
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/mechanical_engineer.md`
- **Dispatch trigger**: Phase 2 (physical/structural concepts)

#### Electrical Engineer
- **Function**: Mains power distribution, sensor/actuator electronics, field infrastructure
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/electrical_engineer.md`
- **Dispatch trigger**: Phase 2 (power/electrical concepts)

#### Control Systems Engineer
- **Function**: Anti-habituation algorithms, multi-node coordination, adaptive deterrent scheduling
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/control_systems_engineer.md`
- **Dispatch trigger**: Phase 2 (automation/adaptation concepts)

#### Embedded Systems Architect
- **Function**: Compute platform selection, edge AI, sensor fusion, distributed architectures
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/embedded_systems_architect.md`
- **Dispatch trigger**: Phase 2 (compute/AI concepts)

#### Thermal Management Engineer
- **Function**: Outdoor electronics thermal design, heat dissipation, environmental loading
- **Tools**: WebSearch, Bash (constraint_validator.py), Read
- **Prompt**: `prompts/thermal_management_engineer.md`
- **Dispatch trigger**: Phase 2 (thermal aspects of any concept)

#### Safety Engineer
- **Function**: Risk assessment, regulatory compliance, human/livestock safety, FMEA
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/safety_engineer.md`
- **Dispatch trigger**: Phase 3 (all concepts require safety review)

#### Operations Specialist
- **Function**: Deployment logistics, field maintenance, manufacturing, supply chain
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/operations_specialist.md`
- **Dispatch trigger**: Phase 2-3 (deployability/serviceability assessment)

### Tier 4: Validation & Economics

#### Cost Analyst
- **Function**: System-level economic modeling, per-acre cost validation, grant alignment, ROI analysis
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/cost_analyst.md`
- **Dispatch trigger**: Phase 3 (economic validation — the binding gate)

#### Validation Engineer
- **Function**: Hard constraint verification, economics-first pass/fail gates, HOTL proxy
- **Tools**: Bash (constraint_validator.py), Read
- **Prompt**: `prompts/validation_engineer.md`
- **Dispatch trigger**: Phase 3 (validates all concepts before human review)

### Tier 5: Documentation & Reporting

#### Documentation Specialist
- **Function**: Phase documentation, IP traceability, decision logging
- **Tools**: Write, Read
- **Prompt**: `prompts/documentation_specialist.md`
- **Dispatch trigger**: End of each phase

#### Final Report Maker
- **Function**: Compiles all documentation into final innovation report
- **Tools**: Write, Read
- **Prompt**: `prompts/final_report_maker.md`
- **Template**: `templates/innovation_report_template.md`
- **Dispatch trigger**: Phase 4 (after all validation complete)

---

## Agent Dispatch Matrix (v2)

Which agents are dispatched for which type of concept:

| Concept Type | Primary Agents | Supporting Agents |
|---|---|---|
| Infrastructure repurposing (irrigation, fencing) | Mechanical Eng, Electrical Eng | AgTech Expert, Operations Specialist |
| Behavioral/sensory deterrence | AgTech Expert, Control Systems Eng | Safety Engineer, Embedded Sys Architect |
| Distributed sensor/actuator networks | Embedded Sys Architect, Electrical Eng | Control Systems Eng, Thermal Mgmt Eng |
| Physical barrier systems | Mechanical Eng, Operations Specialist | Safety Engineer, Cost Analyst |
| Chemical/olfactory systems | AgTech Expert, Safety Engineer | Operations Specialist, Cost Analyst |
| Multi-modal adaptive systems | Control Systems Eng, Embedded Sys Architect | AgTech Expert, Safety Engineer |
| Economics / cost optimization | Cost Analyst, Operations Specialist | All relevant domain engineers |

---

## HITL Gates (Human-in-the-Loop)

| Gate | Location | Purpose | Implementation |
|---|---|---|---|
| Gate 1 | After Phase 1 | Approve contradictions + cross-domain research directions | `AskUserQuestion` with contradiction summary |
| Gate 2 | After Phase 3 | Approve concept direction + economics | `AskUserQuestion` with ranked concept table |
| Gate 3 | After Phase 4 | Final review & IP sign-off | `AskUserQuestion` with report summary |

---

## Tool Infrastructure

### TRIZ Toolkit (`tools/triz_toolkit.py`)
- `features` — List 39 engineering parameters
- `matrix` — Contradiction matrix lookup (39×39)
- `principles` — Inventive principle details (40 principles)
- `field-shield` — Pre-mapped Field Shield contradictions (10 challenges)
- `all-principles` — Quick reference for all 40 principle names

### Constraint Validator v2 (`tools/constraint_validator.py`)
- `constraints` — Display all 21 hard/soft constraints with limits
- `template` — JSON template for solution proposals
- `check` — Automated pass/fail validation against all constraints
- **NEW**: Derived per-acre economics calculation (capex amortization + opex ÷ acres)

### TRIZ Data Files (`tools/data/`)
- `triz_matrix.xls` — 39×39 contradiction matrix (Excel)
- `triz_principles.json` — 40 inventive principles with sub-principles and examples
- `triz_features.txt` — 39 engineering parameters list

### Field Shield Context (`field_shield_context/`)
- `system_overview.md` — Architecture-agnostic innovation platform description
- `hard_constraints.md` — Economics-first constraint structure (v2)
- `known_contradictions.md` — Economic-performance nexus contradictions (v2)

### Report Templates (`templates/`)
- `innovation_report_template.md` — Full report structure with cross-domain research + economics
- `ip_documentation_template.md` — USPTO-compliant IP trail documentation

---

## Session Execution Flow (v2)

```
┌─────────────────────────────────────────────────────────┐
│                    USER INPUT                            │
│     "Research novel concepts for wildlife deterrence"    │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│              PHASE 0: SETUP                              │
│  • Read SKILL.md, context files, constraints             │
│  • Create session directory                              │
│  • Clarify challenge scope (AskUserQuestion)             │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│    PHASE 1: PROBLEM FRAMING & CROSS-DOMAIN RESEARCH      │
│  ┌──────────────┐  ┌──────────────┐                     │
│  │TRIZ Specialist│  │AgTech Expert │  (parallel)         │
│  │Contradictions │  │Wildlife/farm │                     │
│  └──────┬───────┘  └──────┬───────┘                     │
│         ▼                 ▼                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │Biomimicry    │  │Military/     │  │Behavioral    │   │
│  │Researcher    │  │Security      │  │Psychology    │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
│         └──────────┬──────┴──────────┬──────┘           │
│                    ▼                                     │
│          🔴 HITL GATE 1                                  │
│       "Approve contradictions + research directions?"    │
└─────────────────┬───────────────────────────────────────┘
                  │ (human approves)
                  ▼
┌─────────────────────────────────────────────────────────┐
│      PHASE 2: NOVEL CONCEPT DEVELOPMENT                  │
│  Concept development teams dispatched by concept type:   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │Concept Team A│ │Concept Team B│ │Concept Team C│     │
│  │(domain engrs)│ │(domain engrs)│ │(domain engrs)│     │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘     │
│         └──────────┬─────┴──────────┬─────┘             │
│                    ▼                                     │
│         3-5 Novel Concept Families                       │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│        PHASE 3: VALIDATION & COST ANALYSIS               │
│  ┌─────────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │Validation Engr  │  │Cost Analyst   │  │Safety Engr │  │
│  │constraints      │  │$100/ac/yr    │  │FMEA        │  │
│  └────────┬────────┘  └──────┬───────┘  └──────┬─────┘  │
│           └──────────┬───────┴──────────┬──────┘        │
│                      ▼                                   │
│            🔴 HITL GATE 2                                │
│         "Approve concepts + economics?"                  │
└─────────────────┬───────────────────────────────────────┘
                  │ (human approves)
                  ▼
┌─────────────────────────────────────────────────────────┐
│        PHASE 4: DOCUMENTATION & REPORT                   │
│  ┌───────────────────┐  ┌───────────────────┐           │
│  │Documentation Spec  │  │Final Report Maker │           │
│  │Phase write-ups     │  │Complete report     │          │
│  └─────────┬─────────┘  └─────────┬─────────┘           │
│            └──────────┬────────────┘                     │
│                       ▼                                  │
│             🔴 HITL GATE 3                               │
│         "Approve for prototyping?"                       │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│              OUTPUT DELIVERY                              │
│  • Innovation report (Markdown + DOCX)                   │
│  • IP documentation trail                                │
│  • Constraint validation results                         │
│  • Cross-domain research findings                        │
│  • computer:// links for all deliverables                │
└─────────────────────────────────────────────────────────┘
```

---

## Key Optimizations

### 1. Economics-First Validation
Every concept must pass the $100/acre/year gate before detailed engineering. The constraint validator v2 computes derived per-acre economics automatically.

### 2. Cross-Domain Research Phase
New Phase 1 activity dispatches parallel researchers across biomimicry, military/security, behavioral science, and infrastructure domains — ensuring concepts draw from diverse inspiration.

### 3. Architecture-Agnostic Design
All agent prompts are generalized beyond the original solar/battery/Jetson/acoustic architecture. Engineers evaluate concepts on their merits, not against a fixed platform.

### 4. Anti-Habituation as Primary Differentiator
The AgTech Domain Expert and Control Systems Engineer specifically evaluate every concept's anti-habituation mechanism, since this is the #1 reason existing deterrents fail.

### 5. System-Level Economics
The Cost Analyst models costs at the 50-acre block level (not per-unit BOM), because novel concepts may involve distributed infrastructure, shared resources, or repurposed equipment.

---

## Getting Started

To run an innovation session:

1. **Open Claude Desktop** with this folder selected
2. **Describe your challenge**: e.g., "Research novel concepts for deer deterrence at $100/acre/year"
3. **Claude reads SKILL.md** and begins orchestrating the session
4. **Approve at each gate**: Review contradictions, concepts, and final report
5. **Receive deliverables**: Innovation report + IP documentation in your session folder

The system is ready. Describe your wildlife deterrence challenge to begin.
