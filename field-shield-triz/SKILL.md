# Field Shield TRIZ Innovation Engine — Claude Desktop Skill

## Overview
This skill orchestrates TRIZ-based novel concept research sessions for the Field Shield scalable wildlife deterrence platform. The primary mission is to **invent new, novel deterrent concepts** that meet a $100/acre/year cost target at 50-acre block scale, with built-in anti-habituation.

The system uses a Claude Desktop-native architecture with subagent Task dispatching, built-in web research, HITL (Human-in-the-Loop) gates via AskUserQuestion, and local TRIZ tooling. Inspired by the TRIZ Agents project (Szczepanik et al.).

## Architecture: Supervisor-Dispatched Agent Team
Claude acts as the **Project Manager (orchestrator)**, dispatching work to specialist subagents via the Task tool.

```
USER → Claude (PM/Orchestrator)
         ├─ dispatches → Task: TRIZ Specialist
         ├─ dispatches → Task: Cross-Domain Researchers (Novel concept exploration)
         ├─ dispatches → Task: Domain Engineers (Feasibility assessment)
         ├─ dispatches → Task: Field Shield Specialists (AgTech, Cost, Validation)
         ├─ dispatches → Task: Safety / Operations
         ├─ dispatches → Task: Documentation Specialist
         ├─ dispatches → Task: Final Report Maker
         └─ HITL gates → AskUserQuestion at key decision points
```

## Key Constraints (Memorize These)
- **$100/acre/year** maximum total cost (amortized capex + opex)
- **50-acre blocks** as the standard design unit ($5,000/year per block)
- **Anti-habituation**: Must work for a full growing season (4-6 months) without decay
- **Scalable**: Sub-linear cost scaling to hundreds of acres
- **Mains power available**: Commercial farms have grid power — no solar/battery constraint
- **Novel concepts**: The goal is INVENTION, not optimization of existing architectures

## Session Workflow

### PHASE 0: Session Setup
1. Read this SKILL.md file
2. Read the Field Shield context files:
   - `field_shield_context/system_overview.md`
   - `field_shield_context/hard_constraints.md`
   - `field_shield_context/known_contradictions.md`
3. Ask the user to define the specific design challenge or research direction for this session
4. Create a session directory: `sessions/YYYY-MM-DD-<challenge-slug>/`

### PHASE 1: Problem Framing & Cross-Domain Research
**Agents**: TRIZ Specialist + AgTech Domain Expert + Cross-Domain Researchers

1. **Dispatch TRIZ Specialist** (Task tool, subagent_type: "general-purpose"):
   - Prompt includes: the user's challenge + Field Shield context + TRIZ specialist prompt from `prompts/triz_specialist.md`
   - Agent runs `python tools/triz_toolkit.py field-shield` to see pre-mapped contradictions
   - Agent runs `python tools/triz_toolkit.py matrix "<improving>" "<worsening>"` for contradiction lookup
   - Agent runs `python tools/triz_toolkit.py principles <nums>` for principle details
   - Agent performs web search for prior art in ADJACENT FIELDS (not just ag-tech)
   - Returns: contradiction pairs + recommended principles + cross-domain inspiration

2. **Dispatch Cross-Domain Researchers** (multiple Task tools in parallel):
   Research novel approaches from adjacent fields that could inspire new deterrent concepts:
   - **Biomimicry researcher**: How do ecosystems and natural predator-prey dynamics deter herbivores? What biological mechanisms prevent habituation?
   - **Military/security researcher**: What non-lethal deterrence and area denial technologies exist? How do perimeter security systems handle large areas cheaply?
   - **Behavioral science researcher**: What is known about animal learning, fear conditioning, and habituation resistance? What stimuli never habituate?
   - **Infrastructure systems researcher**: What existing farm systems (irrigation, fencing, lighting, power grid) could be repurposed as deterrent delivery mechanisms?

3. **Dispatch AgTech Domain Expert** (Task tool):
   - Validates findings against real agricultural conditions
   - Grounds cross-domain inspiration in farmer operational reality
   - Assesses which approaches would actually work in open fields

4. **HITL Gate 1** (AskUserQuestion):
   - Present the contradiction framing + cross-domain research findings
   - Present 3-5 novel concept directions identified
   - Options: "Approve directions and proceed" / "Modify focus areas" / "Add research directions"

### PHASE 2: Novel Concept Development
**Agents**: Varies by concept direction — dispatch 2-4 relevant specialists per concept

For each approved concept direction, dispatch relevant agents in parallel:

5. **Dispatch Concept Development Teams** (multiple Task tools in parallel):
   - Each team gets: concept direction + relevant TRIZ principles + Field Shield context + constraints
   - Each team develops the concept into a concrete, costed proposal
   - Teams must address: detection method, deterrent mechanism, anti-habituation strategy, infrastructure requirements, cost estimate for 50-acre block

   **Agent selection by concept type:**
   - Physical deterrent (water, air, etc.) → Mechanical Engineer + Electrical Engineer + AgTech Expert
   - Sensory deterrent (visual, olfactory, electromagnetic) → Control Systems Engineer + Safety Engineer + AgTech Expert
   - Behavioral/AI deterrent → Embedded Systems Architect + Control Systems Engineer + AgTech Expert
   - Infrastructure-integrated → Electrical Engineer + Operations Specialist + Cost Analyst
   - Biological/ecological → AgTech Expert + Safety Engineer + Operations Specialist

6. **Consolidate concepts**: Collect all developed concepts, identify synergies, merge overlapping ideas.

### PHASE 3: Validation & Cost Analysis
**Agents**: Validation Engineer + Cost Analyst + Safety Engineer

7. **Dispatch Validation Engineer** (Task tool):
   - Prompt includes: all developed concepts + validation prompt + constraints
   - Agent runs `python tools/constraint_validator.py check <solution.json>` for each concept
   - KEY FOCUS: Does this hit $100/acre/year? Does it scale? Does it resist habituation?
   - Returns: PASS/FAIL/WARN for each concept with margin analysis

8. **Dispatch Cost Analyst** (Task tool):
   - Prompt includes: surviving concepts + cost analyst prompt
   - Agent estimates: capital cost per 50-acre block, annual operating cost, cost per acre per year
   - Agent calculates: amortization over 3yr and 5yr, scaling cost for 100+ acres
   - Returns: detailed cost analysis for each viable concept

9. **Dispatch Safety Engineer** (Task tool):
   - Reviews all concepts for human/livestock safety, regulatory compliance
   - Flags any concepts with regulatory barriers (FIFRA, EPA, FCC, state wildlife regs)

10. **HITL Gate 2** (AskUserQuestion):
    - Present validated + costed concepts in a ranked table
    - Show cost/acre/year for each concept
    - Options: "Approve top concept(s)" / "Request deeper analysis" / "Reject and explore new directions" / "Combine concepts"

### PHASE 4: Documentation & Final Report
**Agents**: Documentation Specialist + Final Report Maker

11. **Dispatch Documentation Specialist** (Task tool):
    - Compile all phase outputs into structured documentation
    - Mark human contribution points for IP trail

12. **Dispatch Final Report Maker** (Task tool):
    - Compile the complete innovation report following the template
    - Write to `sessions/<session-dir>/innovation_report.md`

13. **HITL Gate 3** (AskUserQuestion):
    - Present the final report summary
    - Options: "Approve for prototyping" / "Send back for iteration" / "Archive for future reference"

### PHASE 5: Output Delivery
- Save all artifacts to the session directory
- Generate a summary for the user
- Provide links to all output files

## Tool Reference

### TRIZ Toolkit (Python CLI)
Location: `field-shield-triz/tools/triz_toolkit.py`
```bash
python field-shield-triz/tools/triz_toolkit.py features                     # List 39 features
python field-shield-triz/tools/triz_toolkit.py matrix "Speed" "Loss of Energy"  # Matrix lookup
python field-shield-triz/tools/triz_toolkit.py principles 1 15 35           # Principle details
python field-shield-triz/tools/triz_toolkit.py field-shield                  # All FS contradictions
python field-shield-triz/tools/triz_toolkit.py field-shield detection_range  # Specific challenge
python field-shield-triz/tools/triz_toolkit.py all-principles               # List all 40 principles
```

### Constraint Validator (Python CLI) — v2
Location: `field-shield-triz/tools/constraint_validator.py`
```bash
python field-shield-triz/tools/constraint_validator.py constraints  # Show all constraints
python field-shield-triz/tools/constraint_validator.py template     # Blank JSON template
python field-shield-triz/tools/constraint_validator.py check solution.json  # Validate proposal
```

Key constraints validated:
- cost_per_acre_year (≤$100)
- capital_cost_50acre (≤$15,000)
- annual_operating_cost (≤$2,000/year)
- anti_habituation_months (≥4 months)
- coverage_completeness (≥90%)
- system_lifetime (≥5 years)
- Plus environmental, detection, deterrent, and operations constraints

### Web Research
Use built-in WebSearch and WebFetch tools for:
- Cross-domain technology scouting (military, security, biomimicry, behavioral science)
- Prior art and patent landscape research
- Component datasheets and pricing
- Wildlife behavior studies
- Agricultural technology benchmarks

## Agent Dispatch Patterns

### Standard Specialist Dispatch
```
Task tool:
  subagent_type: "general-purpose"
  prompt: |
    You are the [ROLE] on the Field Shield product team.
    [Read and include contents of prompts/<role>.md]

    CONTEXT:
    [Field Shield system overview — architecture-agnostic, $100/acre/year target]
    [Current challenge description]
    [TRIZ analysis results so far]

    YOUR TASK:
    [Specific assignment for this phase]

    KEY CONSTRAINTS:
    - $100/acre/year maximum (50-acre blocks = $5,000/year)
    - Anti-habituation: must work full growing season
    - Scalable to 100+ acres with sub-linear cost
    - Mains power available (no solar/battery constraint)
    - NOVEL CONCEPTS: invent new approaches, don't optimize old ones

    TOOLS AVAILABLE:
    - Run bash commands for TRIZ toolkit and constraint validator
    - Use web search for research
    - Read files from field-shield-triz/ directory

    OUTPUT:
    [Expected deliverable format]
```

### Parallel Dispatch (multiple agents simultaneously)
When dispatching researchers in Phase 1 or concept developers in Phase 2, launch multiple Task tools in a single message to run agents concurrently.

### Cross-Domain Research Dispatch
New in v2 — Phase 1 now includes parallel research across adjacent fields:
- Biomimicry / natural deterrence mechanisms
- Military / security area denial
- Behavioral science / habituation research
- Agricultural infrastructure repurposing

## Session Output Structure
```
sessions/YYYY-MM-DD-<challenge>/
├── session_log.md              # Chronological log of all agent dispatches
├── phase1_triz_analysis.md     # Contradiction analysis + principles
├── phase1_cross_domain_research.md  # Findings from adjacent fields
├── phase1_agtech_context.md    # Agricultural grounding
├── phase2_concepts/
│   ├── concept_1.md            # Per-concept detailed write-ups
│   ├── concept_2.md
│   └── concept_3.md
├── phase3_validation.md        # Constraint validation results
├── phase3_cost_analysis.md     # Cost analysis per concept
├── phase3_safety_review.md     # Safety and regulatory review
├── innovation_report.md        # Final comprehensive report
├── ip_documentation.md         # IP trail documentation
└── constraint_checks/
    ├── concept_1.json          # Constraint validator input/output
    ├── concept_2.json
    └── concept_3.json
```

## Design Principles

- **Invention over optimization**: The goal is to discover fundamentally new deterrent approaches, not refine existing ones
- **Economics-first validation**: Every concept must pass the $100/acre/year gate before detailed engineering
- **Cross-domain inspiration**: Phase 1 research spans biomimicry, military/security, behavioral science, and infrastructure systems
- **Anti-habituation as primary differentiator**: Existing deterrents fail because wildlife habituates in 2-4 weeks — novel concepts must resist this
- **Architecture-agnostic**: Not locked to any hardware platform — mains power available, concepts evaluated on their merits
