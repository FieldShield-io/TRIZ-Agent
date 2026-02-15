# Field Shield TRIZ Innovation Engine — Agent Team Architecture

## Claude Desktop Optimized Multi-Agent System

This document describes the complete agent team assembled to implement the Field Shield TRIZ Innovation Engine, optimized for Claude Desktop (Cowork mode) rather than the original LangGraph/LangChain architecture.

---

## Architectural Translation

### Original → Optimized

| Original (LangGraph) | Claude Desktop Optimized | Advantage |
|---|---|---|
| LangGraph `StateGraph` orchestration | Claude main thread as Project Manager | No Python runtime dependency, natural conversation flow |
| `create_agent_node()` + `call_agent_model()` | `Task` tool subagent dispatch | Built-in parallelism, automatic context isolation |
| LangChain `@tool` wrappers for TRIZ | Python CLI scripts via `Bash` tool | Simpler, no LangChain dependency, directly testable |
| `TavilySearch` LangChain tool | Built-in `WebSearch` / `WebFetch` tools | Native integration, no API key management |
| No HITL gates | `AskUserQuestion` tool at 3 gate points | Built-in human approval workflow |
| `hub.pull()` external prompts | Local markdown files in `prompts/` | Full control, no LangChain Hub dependency |
| `delete_messages` context management | Subagent natural isolation via Task tool | Each agent runs in its own context window |
| OpenAI/Gemini via langchain providers | Claude (native) | Zero API key cost, runs locally |
| `ToolNode` per agent | Bash commands within subagent Tasks | Agents can run any tool without pre-binding |
| Linear hub-and-spoke routing only | Parallel Task dispatch + combined prompts | Cross-domain consultation via prompt composition |
| `write_document` file output | `Write` tool + computer:// links | Direct file delivery to user |
| Multi-judge LLM evaluation | Constraint validator + human review | Objective validation + subjective judgment |

---

## Agent Team Roster (14 Agents)

### Tier 1: Orchestration

#### 🎯 Project Manager (Claude Main Thread)
- **Implementation**: Claude's primary conversation thread
- **Function**: Orchestrates the entire innovation session, dispatches specialists, synthesizes findings, manages HITL gates
- **Tools**: All tools (Task dispatch, AskUserQuestion, Bash, Read, Write, WebSearch)
- **Workflow guide**: `SKILL.md`
- **Prompt**: `prompts/project_manager.md`

### Tier 2: TRIZ Core

#### 🔬 TRIZ Specialist
- **Implementation**: Task subagent (general-purpose)
- **Function**: Applies TRIZ methodology — identifies contradictions, looks up matrix, maps inventive principles to Field Shield
- **Tools**: Bash (triz_toolkit.py), WebSearch, Read
- **Prompt**: `prompts/triz_specialist.md`
- **Key capability**: Contradiction matrix lookup, principle-to-solution mapping
- **Dispatch trigger**: Phase 1 (Problem Framing)

### Tier 3: Domain Engineers (Original + Extended)

#### ⚙️ Mechanical Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Enclosure design, pan-tilt mechanisms, mounting, weatherproofing, DFM
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/mechanical_engineer.md`
- **Dispatch trigger**: Phase 2 (mechanical/structural contradictions)

#### ⚡ Electrical Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Solar/battery power systems, power distribution, sensor interfaces
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/electrical_engineer.md`
- **Dispatch trigger**: Phase 2 (power/energy contradictions)

#### 🎛️ Control Systems Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Pan-tilt servo control, autonomous behavior, adaptive deterrent algorithms
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/control_systems_engineer.md`
- **Dispatch trigger**: Phase 2 (automation/tracking contradictions)

#### 🛡️ Safety Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Risk assessment, regulatory compliance, FMEA, field safety
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/safety_engineer.md`
- **Dispatch trigger**: Phase 2-3 (all solutions require safety review)

#### 🔧 Operations Specialist
- **Implementation**: Task subagent (general-purpose)
- **Function**: Deployment logistics, field maintenance, manufacturing, supply chain
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/operations_specialist.md`
- **Dispatch trigger**: Phase 2-3 (manufacturability/serviceability assessment)

### Tier 4: Field Shield Extensions (NEW — not in original TRIZ Agents)

#### 🌾 AgTech Domain Expert
- **Implementation**: Task subagent (general-purpose)
- **Function**: Agricultural technology, wildlife behavior, crop economics, farmer needs
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/agtech_domain_expert.md`
- **Dispatch trigger**: Phase 1 (grounds TRIZ analysis in agricultural reality)
- **NEW**: Not present in original — fills critical agricultural knowledge gap

#### 🌡️ Thermal Management Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Jetson thermal constraints, sealed enclosure cooling, solar thermal loading
- **Tools**: WebSearch, Bash (constraint_validator.py), Read
- **Prompt**: `prompts/thermal_management_engineer.md`
- **Dispatch trigger**: Phase 2 (thermal/reliability contradictions — the #1 constraint)
- **NEW**: Not present in original — addresses the most critical Field Shield challenge

#### 🖥️ Embedded Systems Architect
- **Implementation**: Task subagent (general-purpose)
- **Function**: Jetson optimization, TensorRT, ZeroMQ, edge AI pipeline, power modes
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/embedded_systems_architect.md`
- **Dispatch trigger**: Phase 2 (compute/AI performance contradictions)
- **NEW**: Replaces disabled SoftwareEngineer — specialized for Jetson edge AI

#### 💰 Cost Analyst
- **Implementation**: Task subagent (general-purpose)
- **Function**: BOM estimation, manufacturing cost, grant alignment, farmer ROI
- **Tools**: WebSearch, Read
- **Prompt**: `prompts/cost_analyst.md`
- **Dispatch trigger**: Phase 3 (cost validation of surviving solutions)
- **NEW**: Not present in original — keeps innovation grounded in commercial viability

#### ✅ Validation Engineer
- **Implementation**: Task subagent (general-purpose)
- **Function**: Hard constraint verification, pass/fail gates, HOTL proxy
- **Tools**: Bash (constraint_validator.py), Read
- **Prompt**: `prompts/validation_engineer.md`
- **Dispatch trigger**: Phase 3 (validates all solutions before human review)
- **NEW**: Not present in original — automated constraint checking

### Tier 5: Documentation & Reporting

#### 📝 Documentation Specialist
- **Implementation**: Task subagent (general-purpose)
- **Function**: Phase documentation, IP traceability, decision logging
- **Tools**: Write, Read
- **Prompt**: `prompts/documentation_specialist.md`
- **Dispatch trigger**: End of each phase

#### 📄 Final Report Maker
- **Implementation**: Task subagent (general-purpose)
- **Function**: Compiles all documentation into final innovation report
- **Tools**: Write, Read
- **Prompt**: `prompts/final_report_maker.md`
- **Template**: `templates/innovation_report_template.md`
- **Dispatch trigger**: Phase 4 (after all validation complete)

---

## Agent Dispatch Matrix

Which agents are dispatched for which type of contradiction:

| Contradiction Type | Primary Agents | Supporting Agents |
|---|---|---|
| Thermal / Reliability | Thermal Mgmt Engineer, Embedded Sys Architect | Mechanical Engineer, Electrical Engineer |
| Power / Energy | Electrical Engineer, Embedded Sys Architect | Thermal Mgmt Engineer, Cost Analyst |
| Weight / Structural | Mechanical Engineer, Operations Specialist | Electrical Engineer, Cost Analyst |
| Detection / AI Performance | Embedded Sys Architect, Control Systems Eng | Thermal Mgmt Engineer, Safety Engineer |
| Deterrent Effectiveness | AgTech Domain Expert, Control Systems Eng | Safety Engineer, Electrical Engineer |
| Autonomy / Maintainability | Control Systems Eng, Operations Specialist | Embedded Sys Architect, Safety Engineer |
| Cost / Manufacturing | Cost Analyst, Operations Specialist | Mechanical Engineer, Electrical Engineer |

---

## HITL Gates (Human-in-the-Loop)

| Gate | Location | Purpose | Implementation |
|---|---|---|---|
| Gate 1 | After Phase 1 | Approve contradiction framing | `AskUserQuestion` with contradiction summary |
| Gate 2 | After Phase 3 | Approve solution direction | `AskUserQuestion` with ranked solution table |
| Gate 3 | After Phase 4 | Final review & IP sign-off | `AskUserQuestion` with report summary |

---

## Tool Infrastructure

### TRIZ Toolkit (`tools/triz_toolkit.py`)
- `features` — List 39 engineering parameters
- `matrix` — Contradiction matrix lookup (39×39)
- `principles` — Inventive principle details (40 principles)
- `field-shield` — Pre-mapped Field Shield contradictions (10 challenges)
- `all-principles` — Quick reference for all 40 principle names

### Constraint Validator (`tools/constraint_validator.py`)
- `constraints` — Display all 19 hard/soft constraints with limits
- `template` — JSON template for solution proposals
- `check` — Automated pass/fail validation against all constraints

### TRIZ Data Files (`tools/data/`)
- `triz_matrix.xls` — 39×39 contradiction matrix (Excel)
- `triz_principles.json` — 40 inventive principles with sub-principles and examples
- `triz_features.txt` — 39 engineering parameters list

### Field Shield Context (`field_shield_context/`)
- `system_overview.md` — Complete system architecture and subsystem descriptions
- `hard_constraints.md` — All engineering constraints in table format
- `known_contradictions.md` — Pre-analyzed TRIZ contradiction mappings

### Report Templates (`templates/`)
- `innovation_report_template.md` — Full report structure with all sections
- `ip_documentation_template.md` — USPTO-compliant IP trail documentation

---

## Session Execution Flow

```
┌─────────────────────────────────────────────────────────┐
│                    USER INPUT                            │
│          "Solve the thermal-power nexus"                 │
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
│           PHASE 1: PROBLEM FRAMING                       │
│  ┌──────────────────┐  ┌──────────────────┐             │
│  │  TRIZ Specialist  │  │  AgTech Expert   │  (parallel) │
│  │  Matrix lookup    │  │  Wildlife context│             │
│  │  Principles       │  │  Field conditions│             │
│  └────────┬─────────┘  └────────┬─────────┘             │
│           └──────────┬───────────┘                       │
│                      ▼                                   │
│            🔴 HITL GATE 1                                │
│         "Approve contradictions?"                        │
└─────────────────┬───────────────────────────────────────┘
                  │ (human approves)
                  ▼
┌─────────────────────────────────────────────────────────┐
│        PHASE 2: SOLUTION GENERATION                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │Thermal   │ │Embedded  │ │Mechanical│ │Electrical│   │
│  │Mgmt Eng  │ │Sys Arch  │ │Engineer  │ │Engineer  │   │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘   │
│       └──────┬──────┴──────┬─────┴──────┬──────┘        │
│              ▼             ▼            ▼                │
│        Solution A    Solution B    Solution C            │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│          PHASE 3: VALIDATION & COSTING                   │
│  ┌───────────────────┐  ┌───────────────────┐           │
│  │Validation Engineer │  │  Cost Analyst     │ (parallel) │
│  │constraint_validator│  │  BOM + ROI        │           │
│  └─────────┬─────────┘  └─────────┬─────────┘           │
│            └──────────┬────────────┘                     │
│                       ▼                                  │
│             🔴 HITL GATE 2                               │
│          "Approve solutions?"                            │
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
│  • Innovation report (Markdown)                          │
│  • IP documentation trail                                │
│  • Constraint validation results                         │
│  • Session log with all agent interactions               │
│  • computer:// links for all deliverables                │
└─────────────────────────────────────────────────────────┘
```

---

## Key Optimizations Over Original

### 1. Memory Management → Natural Isolation
The original system needed `delete_messages` to trim context and `steps_documentation` to persist findings. In Claude Desktop, each Task subagent runs in its own context — the orchestrator only receives the final output. This is naturally memory-efficient without any custom trimming logic.

### 2. Hub-and-Spoke → Parallel + Cross-Domain
The original PM-routing pattern forced all communication through the PM. Claude Desktop's Task tool allows launching multiple agents simultaneously AND composing prompts that combine domain knowledge from multiple roles for cross-domain problems.

### 3. No API Keys Required
The original system required API keys for OpenAI/Gemini, Tavily, and LangChain Hub. The Claude Desktop version runs entirely on the native Claude model with built-in web search — zero external API dependencies.

### 4. Human-in-the-Loop Built In
The original had no HITL gates. The `AskUserQuestion` tool provides structured multiple-choice approval gates at three critical decision points, ensuring human inventorship is documented.

### 5. Constraint Automation
The new `constraint_validator.py` provides automated pass/fail checking against 19 quantitative constraints — something the original system lacked entirely (it only had LLM-based opinion on feasibility).

### 6. IP Documentation Native
The templates and documentation workflow ensure every session produces USPTO-compliant inventorship documentation — critical for Field Shield's patent strategy.

---

## Getting Started

To run an innovation session:

1. **Open Claude Desktop** with this folder selected
2. **Describe your challenge**: "I want to solve the thermal management problem for the sealed Jetson enclosure"
3. **Claude reads SKILL.md** and begins orchestrating the session
4. **Approve at each gate**: Review contradictions, solutions, and final report
5. **Receive deliverables**: Innovation report + IP documentation in your session folder

The system is ready. Just describe your Field Shield design challenge.
