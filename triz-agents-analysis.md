# TRIZ Agents Architecture Analysis & Field Shield Extension Plan

## 1. Repository Overview

**Repo:** [github.com/kamil-szczepanik/TRIZ-Agents](https://github.com/kamil-szczepanik/TRIZ-Agents)
**Paper:** ICAART 2025 — [arxiv.org/abs/2506.18783](https://arxiv.org/abs/2506.18783)
**License:** MIT (fully permissive — fork freely, modify, commercial use)
**Version:** 0.1.0 (prototype maturity)
**Python:** ≥ 3.10

---

## 2. Architecture Breakdown

### 2.1 Core Pattern: Supervisor-Routed Multi-Agent Graph

The system implements a **supervisor orchestration pattern** using LangGraph's `StateGraph`. A single Project Manager agent acts as the router, deciding which specialist agent handles each step. This is _not_ a peer-to-peer or blackboard architecture — all routing decisions flow through the PM.

```
START → ProjectManager → [routes to specialist] → specialist does work → returns to PM → PM routes next → ... → FinalReportMaker → END
```

The flow includes a memory management mechanism: after the DocumentationSpecialist writes up each completed step, a `delete_messages` node trims the conversation history (keeping only first and last messages) and appends the documentation to a separate `steps_documentation` list. This prevents context window overflow on long runs.

### 2.2 State Schema

```python
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]      # Active conversation
    next: str                                                   # Next agent to route to
    problem_description: str                                    # Original problem statement
    steps_documentation: Annotated[List[BaseMessage], add_messages]  # Accumulated step docs
```

Key insight: `steps_documentation` is the persistent memory across the entire run. When `delete_messages` fires, it trims `messages` but preserves `steps_documentation`. This is how the system maintains coherence across many agent turns without blowing context.

### 2.3 Agent Roster & Tool Assignments

| Agent | Role | Tools | Routing |
|-------|------|-------|---------|
| **ProjectManager** | Supervisor/orchestrator. Reads all messages + step docs, decides who goes next. | `write_note`, `read_note` | Routes to any specialist or FINISH |
| **TRIZSpecialist** | Applies TRIZ methodology — identifies contradictions, looks up principles, uses contradiction matrix | `rag_triz_tool`, `triz_principles`, `triz_contradiction_matrix`, `triz_features`, `tavily_tool`, `wikipedia` | → PM |
| **MechanicalEngineer** | Mechanical design domain expertise | `tavily_tool` (web search) | → PM |
| **ElectricalEngineer** | Electrical/power systems domain expertise | `tavily_tool` | → PM |
| **ControlSystemsEngineer** | Control theory, automation, feedback systems | `tavily_tool` | → PM |
| **SafetyEngineer** | Safety analysis, risk assessment, compliance | `tavily_tool` | → PM |
| **SoftwareEngineer** | (Defined but commented out in graph build) | `tavily_tool` | → PM |
| **OperationsSpecialist** | Operations, maintenance, deployment | `tavily_tool` | → PM |
| **DocumentationSpecialist** | Writes up completed steps | `write_document` | → `delete_messages` → PM |
| **FinalReportMaker** | Compiles all step docs into final deliverable | `write_document` | → END |

### 2.4 TRIZ-Specific Tools (The Core IP)

**triz_features()** — Returns the 39 TRIZ engineering parameters (Weight of moving object, Speed, Force, Temperature, Reliability, Adaptability, etc.). These are the vocabulary for framing contradictions.

**triz_contradiction_matrix(improving_feature, worsening_feature)** — Looks up the 39×39 contradiction matrix from a local Excel file. Given two features in tension, returns the recommended inventive principles (by number). This is the canonical TRIZ lookup.

**triz_principles(principle_numbers)** — Returns detailed descriptions of specific TRIZ principles by number. All 40 principles are stored in a local JSON file with sub-principles and descriptions.

**rag_triz_tool(question)** — RAG pipeline over local TRIZ PDFs (3 included: PDMA ToolBook TRIZ article, TRIZ Wikipedia dump, "Innovative Problem Solving" textbook). Uses Chroma/FAISS + OpenAI embeddings. Lazy-initialized on first call.

### 2.5 LLM Provider Architecture

The `llm.py` module maps model names to LangChain provider classes via `MODEL_PROVIDER_MAP`. Currently supports: OpenAI (GPT-4o family, o1, o3, o4-mini), Google Gemini (1.5/2.5), DeepSeek, xAI Grok. Adding Anthropic requires adding `langchain-anthropic` and mapping Claude model strings.

### 2.6 Evaluation Framework

Multi-judge evaluation across 7 metrics: clarity, coherence, coverage, novelty, feasibility, TRIZ-adherence, and expert-solution alignment. Each metric has a harshly-worded evaluator prompt (role-played as Principal Engineer, Patent Examiner, CTO, TRIZ Master, etc.). Multiple judge LLMs score independently, results are averaged.

### 2.7 Prompt Management

All agent prompts are pulled from **LangChain Hub** (`hub.pull("kamilsz/triz-agents-*")`). This means you need a `LANGCHAIN_API_KEY` to run as-is, and prompts are externally managed. For a Field Shield fork, you'd want to either pull these once and localize them, or replace entirely with custom prompts.

---

## 3. Strengths

1. **Clean separation of concerns.** Each agent is a pure function: `(state) → state_delta`. Adding/removing agents requires minimal wiring changes.

2. **Memory management.** The `delete_messages` + `steps_documentation` pattern is clever — it lets the system run for many cycles without OOM-ing the context window.

3. **TRIZ tools are self-contained.** The contradiction matrix, principles, and features are loaded from local files (Excel, JSON, TXT). No external API dependency for core TRIZ reasoning.

4. **Model-agnostic.** Swapping the LLM is a one-line change (`create_workflow_app(llm_model="claude-sonnet-4-5-20250929")`). Adding providers is ~5 lines in `llm.py`.

5. **Built-in evaluation.** The multi-judge framework means you can benchmark improvements systematically.

6. **MIT licensed.** No restrictions on commercial use or modification.

---

## 4. Weaknesses & Gaps

1. **Domain agents are underpowered.** The MechanicalEngineer, ElectricalEngineer, etc. only have `tavily_tool` (web search). They have no specialized knowledge bases, simulation capabilities, or domain-specific reasoning tools. They're essentially "LLM + Google" which limits depth.

2. **No simulation or physics validation.** Solutions are generated but never validated against physical constraints. A "feasibility" evaluation exists but it's LLM-based opinion, not physics simulation.

3. **No component database or bill-of-materials reasoning.** Agents can search the web but can't query component catalogs, datasheets, or check real-world availability/pricing.

4. **Prompts are externally hosted.** Dependency on LangChain Hub means you can't inspect or modify prompts without pulling them. For a production system, you'd want full control.

5. **No human-in-the-loop gates.** The workflow runs start-to-finish without pause points for human review. For Field Shield, you'd want approval gates before the system commits to a solution direction.

6. **Linear routing (PM hub-and-spoke).** Agents can't directly consult each other — everything routes back through the PM. This prevents rich cross-domain collaboration (e.g., the MechanicalEngineer asking the ElectricalEngineer a direct question about thermal dissipation).

7. **SoftwareEngineer is commented out.** Likely disabled during debugging and never re-enabled.

8. **No persistent state across runs.** Each experiment is a fresh start. There's no concept of building on previous innovation sessions.

---

## 5. Field Shield Extension Plan

### 5.1 Problem Statement Mapping

Field Shield's core design challenges map directly to TRIZ contradictions:

| Field Shield Challenge | Improving Feature | Worsening Feature | TRIZ Tension |
|----------------------|------------------|-------------------|--------------|
| Longer detection range → bigger/heavier thermal camera | Measurement accuracy | Weight of stationary object | Range vs. Weight |
| Faster pan-tilt response → more power draw | Speed | Use of energy by moving object | Speed vs. Energy |
| Louder acoustic deterrent → more power, animal habituation | Force (Intensity) | Loss of Energy, Adaptability | Effectiveness vs. Sustainability |
| Weatherproof enclosure → thermal buildup | Reliability | Temperature | Durability vs. Thermals |
| AI inference speed → Jetson power/thermal limits | Productivity | Temperature, Use of energy | Throughput vs. Thermal Budget |
| Autonomous operation → complexity, repair difficulty | Extent of automation | Ease of repair, Device complexity | Autonomy vs. Maintainability |

### 5.2 New Agents to Add

#### AgTechDomainExpert
**Purpose:** Agricultural technology specialist with knowledge of crop protection, wildlife behavior patterns, field deployment conditions, seasonal considerations.
**Tools:** Web search + RAG over USDA wildlife damage management publications, agricultural extension service data, crop damage economic models.
**Why:** The existing agents have no agricultural context. Solutions need to be grounded in real field conditions (weather, terrain, animal behavior, farmer operational constraints).

#### ThermalManagementEngineer
**Purpose:** Specialist in thermal design for outdoor electronics. NVIDIA Jetson thermal constraints, passive/active cooling in sealed enclosures, solar thermal loading.
**Tools:** Web search + thermal calculation tools (simplified analytical models), component datasheet lookup.
**Why:** Thermal management is the #1 constraint for Jetson-based outdoor deployments and none of the existing agents specialize in it.

#### EmbeddedSystemsArchitect
**Purpose:** Edge AI hardware architecture — Jetson platform optimization, ZeroMQ messaging, sensor integration, power budgeting for solar/battery systems.
**Tools:** Web search + NVIDIA Jetson documentation RAG, ZeroMQ architecture patterns database.
**Why:** The SoftwareEngineer agent (currently disabled) is too generic. Field Shield needs an agent that understands the specific constraints of edge AI on constrained hardware.

#### CostAnalyst
**Purpose:** Bill-of-materials estimation, manufacturing cost analysis, target price validation, grant/subsidy alignment.
**Tools:** Component pricing APIs or curated cost databases, manufacturing cost models.
**Why:** Novel solutions that cost 10x the budget are useless. This agent keeps innovation grounded in commercial viability.

#### ValidationEngineer
**Purpose:** Reviews proposed solutions against hard constraints (power budget, weight limits, environmental ratings, FCC compliance for acoustic deterrents).
**Tools:** Constraint checklist tool, specification database, pass/fail validation logic.
**Why:** Acts as a HOTL (Human-on-the-Loop) proxy — catches physically impossible or commercially impractical solutions before they reach human review.

### 5.3 Enhanced Tool Set

#### Field Shield Specification RAG
Build a RAG corpus from your existing PRDs, technical specifications, and hardware datasheets. Every agent should be able to query this to ground their reasoning in actual system constraints.

```python
field_shield_rag = build_rag_tool(
    data_dir="field_shield_specs/",
    collection_name="field-shield-specs",
    description="Search Field Shield PRDs, hardware specs, and design constraints"
)
```

#### Component Lookup Tool
A structured tool that queries component databases (DigiKey, Mouser APIs, or a curated local database) to validate that referenced components exist, are in stock, and meet specifications.

#### Constraint Validator Tool
Programmable hard-constraint checker:
```python
@tool
def validate_constraints(solution_description: str) -> str:
    """Check a proposed solution against Field Shield's hard constraints:
    - Max power budget: 15W average (solar/battery)
    - Max weight: 25 lbs total system
    - Operating temp: -20°C to 60°C
    - IP rating: minimum IP65
    - Detection range: minimum 200m for deer-sized targets
    - Response time: <2s from detection to deterrent activation
    """
```

### 5.4 Architecture Modifications

#### Add Anthropic/Claude Support to llm.py

```python
try:
    from langchain_anthropic import ChatAnthropic
except Exception:
    ChatAnthropic = None

MODEL_PROVIDER_MAP.update({
    "claude-sonnet-4-5-20250929": ChatAnthropic,
    "claude-opus-4-6": ChatAnthropic,
    "claude-haiku-4-5-20251001": ChatAnthropic,
})
```

#### Add Human-in-the-Loop Gates

Insert approval nodes at key decision points:

```
PM → TRIZSpecialist → PM → [HITL: Approve contradiction framing?] → domain agents → PM → [HITL: Approve solution direction?] → FinalReportMaker → END
```

Implement as LangGraph interrupt nodes that pause execution and wait for human input.

#### Enable Cross-Agent Consultation

Modify the routing to allow agent-to-agent handoffs for specific questions, not just PM routing. For example, when the ThermalManagementEngineer identifies a cooling solution, they should be able to directly query the EmbeddedSystemsArchitect about Jetson thermal interfaces before routing back to PM.

#### Localize Prompts

Pull all prompts from LangChain Hub once, save locally, and modify for Field Shield context. Each prompt should include Field Shield-specific context:

```
You are a Mechanical Engineer on the Field Shield product team. Field Shield is an 
autonomous wildlife deterrence system for agricultural use that combines AI-powered 
thermal cameras, pan-tilt mechanisms, and acoustic deterrents on NVIDIA Jetson hardware.

Your expertise is in mechanical design for outdoor electronic enclosures, pan-tilt 
mechanisms, mounting systems, and weatherproofing for agricultural environments.

When evaluating solutions, always consider:
- Outdoor deployment in agricultural fields (dust, moisture, temperature extremes)
- Solar/battery power constraints
- Farmer-serviceable design (no specialized tools for maintenance)
- Deer and wild hog behavioral patterns
```

### 5.5 Workflow for Field Shield Innovation Sessions

**Phase 1: Problem Framing (TRIZ Specialist + AgTechDomainExpert)**
- Input: Specific Field Shield design challenge from PRD
- TRIZ Specialist identifies contradictions using the 39 features
- AgTech expert grounds in real agricultural deployment constraints
- Output: Validated contradiction pairs + context

**Phase 2: Solution Generation (Domain Engineers)**
- PM routes to relevant specialists based on contradiction type
- Each specialist proposes solutions using TRIZ principles + domain expertise
- Cross-consultation enabled for interdisciplinary solutions
- Output: 3-5 candidate solutions per contradiction

**Phase 3: Validation (ValidationEngineer + CostAnalyst)**
- Each candidate checked against hard constraints (power, weight, temp, cost)
- Infeasible solutions filtered with documented reasons
- Cost estimates attached to survivors
- Output: Ranked feasible solutions with cost/benefit analysis

**Phase 4: Documentation (DocumentationSpecialist + FinalReportMaker)**
- Step-by-step reasoning documented for patent trail
- Human contribution points explicitly called out (inventorship documentation)
- Final report with recommended solutions, TRIZ principle traceability, and implementation roadmap

**Phase 5: Human Review (HITL Gate)**
- Human reviews final report
- Approves solutions for prototyping or sends back for iteration
- All human decisions documented for IP trail

---

## 6. Implementation Roadmap

### Week 1: Fork & Foundation
- Fork TRIZ Agents repo
- Add ChatAnthropic to `llm.py`
- Pull and localize all prompts from LangChain Hub
- Modify prompts with Field Shield context
- Verify end-to-end run with Claude on the gantry crane example

### Week 2: Custom Agents & Tools
- Build Field Shield Specification RAG from existing PRDs
- Implement AgTechDomainExpert agent
- Implement ThermalManagementEngineer agent
- Implement EmbeddedSystemsArchitect agent
- Add constraint validator tool

### Week 3: Workflow Enhancement
- Add HITL interrupt nodes
- Implement CostAnalyst and ValidationEngineer agents
- Build Field Shield-specific evaluation prompts (replace gantry crane benchmark)
- Test full workflow against 2-3 real Field Shield design challenges

### Week 4: Optimization & Documentation
- Tune prompts based on output quality
- Run multi-judge evaluation with multiple LLMs
- Document inventorship contribution points
- Build repeatable experiment pipeline for ongoing innovation sessions

---

## 7. Cost Estimation

Per innovation session (one design challenge through full pipeline):

| Component | Estimated Token Usage | Cost (Claude Sonnet) |
|-----------|----------------------|---------------------|
| PM routing (10-15 turns) | ~50K tokens | ~$0.75 |
| TRIZ Specialist (2-3 turns) | ~30K tokens | ~$0.45 |
| Domain agents (4-6 turns total) | ~60K tokens | ~$0.90 |
| Validation agents (2-3 turns) | ~30K tokens | ~$0.45 |
| Documentation + Final Report | ~40K tokens | ~$0.60 |
| **Total per session** | **~210K tokens** | **~$3.15** |

Multi-judge evaluation adds ~$1-2 per run depending on judge count. Running 10 innovation sessions across major Field Shield challenges: approximately $30-50 total.

---

## 8. IP Documentation Strategy

For every innovation session, the system should automatically generate:

1. **Problem Statement** — Authored by human (you), documenting the specific Field Shield challenge
2. **TRIZ Analysis** — AI-generated contradiction identification and principle selection
3. **Human Decision Points** — Every place where you selected, modified, rejected, or combined AI suggestions
4. **Reduction to Practice Notes** — How you translated the AI-suggested concept into a buildable design
5. **Prior Art Search Results** — What the agents found in web search (timestamps, sources)

This documentation chain establishes your "significant contribution" under the February 2024 USPTO guidance. The AI is a tool; you are the inventor who framed the problem, selected the approach, validated against real constraints, and reduced to practice.
