# Field Shield TRIZ Innovation Engine

A Claude Desktop skill for TRIZ-based novel concept research applied to scalable wildlife deterrence.

## What This Does

This system orchestrates structured innovation sessions using the TRIZ (Theory of Inventive Problem Solving) methodology to invent new wildlife deterrence concepts for commercial agriculture. It combines cross-domain research, systematic contradiction analysis, and multi-specialist validation to generate novel, economically viable solutions.

**Target**: $100/acre/year at 50-acre block scale, with built-in anti-habituation.

## How It Works

The system runs as a Claude Desktop (Cowork mode) skill. Claude acts as the Project Manager, dispatching 14 specialist subagents through a structured 5-phase workflow:

1. **Problem Framing** — TRIZ contradiction analysis + cross-domain research
2. **Concept Development** — Domain engineers develop novel solution families
3. **Validation** — Economic, safety, and constraint verification
4. **Documentation** — Innovation report + IP trail
5. **Delivery** — All artifacts saved to session directory

Human-in-the-loop gates at three decision points ensure the inventor retains control over the creative direction.

## Getting Started

1. Open Claude Desktop with this folder selected
2. Describe your challenge (e.g., "Research novel concepts for deer deterrence at $100/acre/year")
3. Claude reads the skill files and orchestrates the session
4. Approve at each gate: contradictions, concepts, and final report
5. Receive deliverables: innovation report + IP documentation

## Repository Structure

```
field-shield-triz/
├── SKILL.md                      # Skill entry point and workflow guide
├── AGENT_TEAM_ARCHITECTURE.md    # Agent team design and dispatch matrix
├── field_shield_context/         # Domain context files
│   ├── system_overview.md
│   ├── hard_constraints.md
│   └── known_contradictions.md
├── prompts/                      # 14 specialist agent prompts
├── templates/                    # Report and IP documentation templates
└── tools/
    ├── triz_toolkit.py           # TRIZ contradiction matrix + principles CLI
    ├── constraint_validator.py   # Hard constraint validation CLI
    └── data/                     # TRIZ reference data (matrix, principles, features)
```

## Key Design Decisions

- **Architecture-agnostic**: Not locked to any hardware platform. Novel concepts are evaluated on their merits.
- **Economics-first**: Every concept must pass the $100/acre/year gate before detailed engineering.
- **Anti-habituation focus**: The primary technical challenge — existing deterrents fail because wildlife habituates in 2-4 weeks.
- **Mains power available**: Commercial farms have grid power, removing the solar/battery constraint.
- **Cross-domain research**: Solutions draw inspiration from military/security, biomimicry, behavioral science, and infrastructure systems.

## Acknowledgments

This project was inspired by the [TRIZ Agents](https://github.com/Szczepanik/triz-agents) framework by Szczepanik et al. ([arXiv:2506.18783](https://arxiv.org/abs/2506.18783)), which demonstrated multi-agent TRIZ methodology using LangGraph. The Field Shield implementation adapts the core TRIZ approach to a Claude Desktop-native architecture.

## Author

Dylan Baribeault — [Field Shield](https://fieldshield.io)
