# Field Shield TRIZ Innovation Engine — Claude Desktop Skill

## Overview
This skill orchestrates TRIZ-based innovation sessions for the Field Shield autonomous wildlife deterrence system. It replaces a LangGraph/Python multi-agent system with a Claude Desktop-native architecture using subagent Task dispatching, built-in web research, HITL (Human-in-the-Loop) gates via AskUserQuestion, and local TRIZ tooling.

## Architecture: Supervisor-Dispatched Agent Team
Claude acts as the **Project Manager (orchestrator)**, dispatching work to specialist subagents via the Task tool. This mirrors the original TRIZ Agents' supervisor-routed pattern but runs natively in Claude Desktop without LangChain or LangGraph dependencies.

```
USER → Claude (PM/Orchestrator)
         ├─ dispatches → Task: TRIZ Specialist
         ├─ dispatches → Task: Domain Engineers (Mechanical, Electrical, Embedded, Thermal)
         ├─ dispatches → Task: Field Shield Specialists (AgTech, Cost, Validation)
         ├─ dispatches → Task: Safety / Operations / Control Systems
         ├─ dispatches → Task: Documentation Specialist
         ├─ dispatches → Task: Final Report Maker
         └─ HITL gates → AskUserQuestion at key decision points
```

## Session Workflow

### PHASE 0: Session Setup
1. Read this SKILL.md file
2. Read the Field Shield context files:
   - `field_shield_context/system_overview.md`
   - `field_shield_context/hard_constraints.md`
   - `field_shield_context/known_contradictions.md`
3. Ask the user to define the specific design challenge for this session
4. Create a session directory: `sessions/YYYY-MM-DD-<challenge-slug>/`

### PHASE 1: Problem Framing (TRIZ Analysis)
**Agents**: TRIZ Specialist + AgTech Domain Expert

1. **Dispatch TRIZ Specialist** (Task tool, subagent_type: "general-purpose"):
   - Prompt includes: the user's challenge + Field Shield context + TRIZ specialist prompt from `prompts/triz_specialist.md`
   - Agent runs `python tools/triz_toolkit.py field-shield` to see pre-mapped contradictions
   - Agent runs `python tools/triz_toolkit.py matrix "<improving>" "<worsening>"` for contradiction lookup
   - Agent runs `python tools/triz_toolkit.py principles <nums>` for principle details
   - Agent performs web search for prior art
   - Returns: contradiction pairs + recommended principles + prior art notes

2. **Dispatch AgTech Domain Expert** (Task tool, subagent_type: "general-purpose"):
   - Prompt includes: TRIZ findings + AgTech prompt from `prompts/agtech_domain_expert.md`
   - Agent validates contradiction framing against real agricultural conditions
   - Agent researches wildlife behavior relevant to the specific challenge
   - Returns: validated contradictions + agricultural context + deployment constraints

3. **HITL Gate 1** (AskUserQuestion):
   - Present the contradiction framing to the user
   - Options: "Approve and proceed" / "Modify contradictions" / "Add additional contradictions"
   - Wait for human approval before solution generation

### PHASE 2: Solution Generation (Domain Engineers)
**Agents**: Varies by contradiction type — dispatch 2-4 relevant specialists

For each approved contradiction, dispatch relevant domain engineers in parallel:

4. **Dispatch Domain Engineers** (multiple Task tools in parallel):
   - Each agent gets: contradiction details + relevant TRIZ principles + their role prompt + Field Shield context
   - Each agent proposes 2-3 concrete solutions applying the TRIZ principles
   - Agents may use web search for component research, material properties, etc.

   **Agent selection by contradiction type:**
   - Thermal issues → Thermal Management Engineer + Embedded Systems Architect
   - Power issues → Electrical Engineer + Embedded Systems Architect
   - Mechanical issues → Mechanical Engineer + Operations Specialist
   - Detection/AI issues → Embedded Systems Architect + Control Systems Engineer
   - Deterrent issues → AgTech Expert + Control Systems Engineer + Safety Engineer
   - Cost issues → Cost Analyst + Operations Specialist

5. **Consolidate solutions**: Collect all candidate solutions, merge overlapping concepts, identify synergies.

### PHASE 3: Validation & Cost Analysis
**Agents**: Validation Engineer + Cost Analyst

6. **Dispatch Validation Engineer** (Task tool):
   - Prompt includes: all candidate solutions + validation prompt + hard constraints
   - Agent runs `python tools/constraint_validator.py check <solution.json>` for each candidate
   - Returns: PASS/FAIL/WARN for each solution with margin analysis

7. **Dispatch Cost Analyst** (Task tool):
   - Prompt includes: surviving solutions + cost analyst prompt + baseline BOM
   - Agent estimates BOM impact, manufacturing cost, and farmer ROI
   - Returns: cost analysis for each viable solution

8. **HITL Gate 2** (AskUserQuestion):
   - Present validated + costed solutions in a ranked table
   - Options: "Approve top solution(s)" / "Request deeper analysis" / "Reject and re-generate" / "Combine solutions"

### PHASE 4: Documentation & Final Report
**Agents**: Documentation Specialist + Final Report Maker

9. **Dispatch Documentation Specialist** (Task tool):
   - Compile all phase outputs into structured documentation
   - Mark human contribution points for IP trail

10. **Dispatch Final Report Maker** (Task tool):
    - Compile the complete innovation report following the template in `prompts/final_report_maker.md`
    - Write to `sessions/<session-dir>/innovation_report.md`

11. **HITL Gate 3** (AskUserQuestion):
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

### Constraint Validator (Python CLI)
Location: `field-shield-triz/tools/constraint_validator.py`
```bash
python field-shield-triz/tools/constraint_validator.py constraints  # Show all constraints
python field-shield-triz/tools/constraint_validator.py template     # Blank JSON template
python field-shield-triz/tools/constraint_validator.py check solution.json  # Validate proposal
```

### Web Research
Use built-in WebSearch and WebFetch tools for:
- Prior art research
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
    [Field Shield system overview]
    [Current challenge description]
    [TRIZ analysis results so far]

    YOUR TASK:
    [Specific assignment for this phase]

    TOOLS AVAILABLE:
    - Run bash commands for TRIZ toolkit and constraint validator
    - Use web search for research
    - Read files from field-shield-triz/ directory

    OUTPUT:
    [Expected deliverable format]
```

### Parallel Dispatch (multiple agents simultaneously)
When dispatching domain engineers in Phase 2, launch multiple Task tools in a single message to run agents concurrently. Each agent works independently on the same contradiction from their domain perspective.

## Key Differences from Original TRIZ Agents

| Feature | Original (LangGraph) | Claude Desktop Optimized |
|---------|----------------------|--------------------------|
| Orchestrator | LangGraph StateGraph + PM agent | Claude main thread as PM |
| Agent dispatch | Graph node routing | Task tool subagents |
| TRIZ tools | LangChain @tool wrappers | Python CLI scripts (bash) |
| Web search | Tavily LangChain tool | Built-in WebSearch/WebFetch |
| HITL gates | Not implemented | AskUserQuestion tool |
| Memory management | delete_messages + steps_documentation | Subagent isolation (natural) |
| LLM provider | OpenAI/Gemini/DeepSeek via langchain | Claude (native, no API key) |
| Prompt management | LangChain Hub (external) | Local markdown files |
| Cross-agent consult | Not possible (hub-and-spoke only) | Task tool with combined prompts |
| Output | Text files via write_document | Markdown/DOCX with file links |
| Evaluation | Multi-judge LLM scoring | Constraint validator + human review |

## Session Output Structure
```
sessions/YYYY-MM-DD-<challenge>/
├── session_log.md              # Chronological log of all agent dispatches
├── phase1_triz_analysis.md     # Contradiction analysis + principles
├── phase1_agtech_context.md    # Agricultural grounding
├── phase2_solutions/
│   ├── solution_1.md           # Per-solution write-ups
│   ├── solution_2.md
│   └── solution_3.md
├── phase3_validation.md        # Constraint validation results
├── phase3_cost_analysis.md     # Cost analysis
├── innovation_report.md        # Final comprehensive report
├── ip_documentation.md         # IP trail documentation
└── constraint_checks/
    ├── solution_1.json         # Constraint validator input/output
    ├── solution_2.json
    └── solution_3.json
```
