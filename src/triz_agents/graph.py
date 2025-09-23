"""LangGraph workflow for TRIZ Agents.

This module wires up:
- Role agent nodes (ProjectManager, TRIZSpecialist, etc.)
- Per-role ToolNodes
- Routers (supervisor + per-agent tool routing)
- A cleanup node (delete_messages)
- The public factory: create_workflow_app(llm_model, temperature)

Assumptions:
- `create_agent_node`, `call_agent_model`, and `call_project_manager_model`
  exist in `.agents` with signatures compatible with how they're used below.
- Prompts are provided by `.prompt_templates`.
- Tools are provided by `.tools.*`.
"""
from __future__ import annotations

import functools
from typing import Dict, Any, List

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

from langchain_core.messages import RemoveMessage
from langchain.schema import HumanMessage  # used in delete_messages

from .agents import create_agent_node, call_agent_model, call_project_manager_model
from .state import AgentState

# ---- Prompts ----
from .prompt_templates import (
    project_manager_prompt,
    mechanical_engineer_prompt,
    electrical_engineer_prompt,
    control_systems_engineer_prompt,
    safety_engineer_prompt,
    triz_specialist_prompt,
    software_engineer_prompt,
    operations_specialist_prompt,
    documentation_specialist_prompt,
    final_report_maker_prompt,
)

# ---- Tools ----
from .tools.other_tools import (
    tavily_tool,
    wikipedia,
    scrape_webpages,
    default_answer,
    write_document,
    # python_repl,   # enable if/when used
    write_note,
    read_note,
)
from .tools.triz_tools import (
    triz_principles,
    triz_contradiction_matrix,
    triz_features,
)
from .tools.rag_tools import rag_triz_tool


# =========================
# Tool bundles per role
# =========================
project_manager_tools: List[Any] = [write_note, read_note]
mechanical_engineer_tools: List[Any] = [tavily_tool]
electrical_engineer_tools: List[Any] = [tavily_tool]
control_systems_engineer_tools: List[Any] = [tavily_tool]
safety_engineer_tools: List[Any] = [tavily_tool]
triz_specialist_tools: List[Any] = [
    rag_triz_tool,
    triz_principles,
    triz_contradiction_matrix,
    triz_features,
    tavily_tool,
    wikipedia,
]
software_engineer_tools: List[Any] = [tavily_tool]
operations_specialist_tools: List[Any] = [tavily_tool]
documentation_specialist_tools: List[Any] = [write_document]
final_report_maker_tools: List[Any] = [write_document]


# =========================
# Utility / housekeeping nodes
# =========================
def delete_messages(state: AgentState) -> Dict[str, Any]:
    """Trim conversation to keep memory light and append the latest doc step to steps_documentation.

    Behavior:
    - Appends the content of the last tool call args["content"] (from DocumentationSpecialist) to steps_documentation.
    - Removes most previous messages (except the first and last) using RemoveMessage placeholders.
    """
    steps_documentation = state.get("steps_documentation", [])

    # Attempt to grab the content the DocumentationSpecialist just produced
    try:
        last_tool_args = state["messages"][-3].tool_calls[0]["args"]  # as in the original notebook
        steps_documentation.append(
            HumanMessage(content=last_tool_args.get("content", ""), name="DocumentationSpecialist")
        )
    except Exception:
        # Be permissive—if the above structure isn't present, just keep steps as-is
        pass

    messages = state.get("messages", [])
    if len(messages) > 3:
        # Keep the very first and very last message; mark the middle ones for removal
        messages = [RemoveMessage(id=m.id) for m in messages[1:-1] if hasattr(m, "id")]

    return {"messages": messages, "steps_documentation": steps_documentation}


# =========================
# Agent nodes (default model/temperature set later by factory)
# =========================
project_manager_node = create_agent_node(
    project_manager_prompt, "ProjectManager", call_project_manager_model, tools=project_manager_tools
)
mechanical_engineer_node = create_agent_node(
    mechanical_engineer_prompt, "MechanicalEngineer", call_agent_model, tools=mechanical_engineer_tools
)
electrical_engineer_node = create_agent_node(
    electrical_engineer_prompt, "ElectricalEngineer", call_agent_model, tools=electrical_engineer_tools
)
control_systems_engineer_node = create_agent_node(
    control_systems_engineer_prompt, "ControlSystemsEngineer", call_agent_model, tools=control_systems_engineer_tools
)
safety_engineer_node = create_agent_node(
    safety_engineer_prompt, "SafetyEngineer", call_agent_model, tools=safety_engineer_tools
)
triz_specialist_node = create_agent_node(
    triz_specialist_prompt, "TRIZSpecialist", call_agent_model, tools=triz_specialist_tools
)
software_engineer_node = create_agent_node(
    software_engineer_prompt, "SoftwareEngineer", call_agent_model, tools=software_engineer_tools
)
operations_specialist_node = create_agent_node(
    operations_specialist_prompt, "OperationsSpecialist", call_agent_model, tools=operations_specialist_tools
)
documentation_specialist_node = create_agent_node(
    documentation_specialist_prompt, "DocumentationSpecialist", call_agent_model, tools=documentation_specialist_tools
)
final_report_maker_node = create_agent_node(
    final_report_maker_prompt, "FinalReportMaker", call_agent_model, tools=final_report_maker_tools
)

# =========================
# Tool nodes
# =========================
triz_specialist_tool_node = ToolNode(tools=triz_specialist_tools)
mechanical_engineer_tool_node = ToolNode(tools=mechanical_engineer_tools)
electrical_engineer_tool_node = ToolNode(tools=electrical_engineer_tools)
control_systems_engineer_tool_node = ToolNode(tools=control_systems_engineer_tools)
safety_engineer_tool_node = ToolNode(tools=safety_engineer_tools)
software_engineer_tool_node = ToolNode(tools=software_engineer_tools)
operations_specialist_tool_node = ToolNode(tools=operations_specialist_tools)
documentation_specialist_tool_node = ToolNode(tools=documentation_specialist_tools)
final_report_maker_tool_node = ToolNode(tools=final_report_maker_tools)


# =========================
# Routers
# =========================
def supervisor_router(state: AgentState) -> str:
    """Route to the next role based on `state['next']`."""
    return {
        "TRIZSpecialist": "TRIZSpecialist",
        "MechanicalEngineer": "MechanicalEngineer",
        "ElectricalEngineer": "ElectricalEngineer",
        "ControlSystemsEngineer": "ControlSystemsEngineer",
        "SafetyEngineer": "SafetyEngineer",
        "SoftwareEngineer": "SoftwareEngineer",
        "OperationsSpecialist": "OperationsSpecialist",
        "DocumentationSpecialist": "DocumentationSpecialist",
        "FinalReportMaker": "FinalReportMaker",
        "ProjectManager": "ProjectManager",
        "FINISH": "FinalReportMaker",
    }.get(state.get("next", ""), "FinalReportMaker")


def agent_router(state: AgentState, tool_key: str, fallback_agent: str) -> str:
    """If the last message has tool calls, go to the tool node; otherwise, back to fallback_agent."""
    messages = state.get("messages", [])
    if not messages:
        return fallback_agent
    last_message = messages[-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return tool_key
    return fallback_agent


triz_specialist_router = functools.partial(
    agent_router, tool_key="triz_specialist_tools", fallback_agent="ProjectManager"
)
mechanical_engineer_router = functools.partial(
    agent_router, tool_key="mechanical_engineer_tools", fallback_agent="ProjectManager"
)
electrical_engineer_router = functools.partial(
    agent_router, tool_key="electrical_engineer_tools", fallback_agent="ProjectManager"
)
control_systems_engineer_router = functools.partial(
    agent_router, tool_key="control_systems_engineer_tools", fallback_agent="ProjectManager"
)
safety_engineer_router = functools.partial(
    agent_router, tool_key="safety_engineer_tools", fallback_agent="ProjectManager"
)
software_engineer_router = functools.partial(
    agent_router, tool_key="software_engineer_tools", fallback_agent="ProjectManager"
)
operations_specialist_router = functools.partial(
    agent_router, tool_key="operations_specialist_tools", fallback_agent="ProjectManager"
)
documentation_specialist_router = functools.partial(
    agent_router, tool_key="documentation_specialist_tools", fallback_agent="delete_messages"
)
final_report_maker_router = functools.partial(
    agent_router, tool_key="final_report_maker_tools", fallback_agent="ProjectManager"
)


# =========================
# Public factory
# =========================
def create_workflow_app(llm_model: str = "gpt-4o", temperature: float = 0):
    """Return a compiled workflow app using the specified LLM model and temperature."""

    # Re-create agent nodes with the specified model settings
    project_manager_node = create_agent_node(
        project_manager_prompt,
        "ProjectManager",
        call_project_manager_model,
        tools=project_manager_tools,
        model=llm_model,
        temperature=temperature,
    )
    mechanical_engineer_node = create_agent_node(
        mechanical_engineer_prompt,
        "MechanicalEngineer",
        call_agent_model,
        tools=mechanical_engineer_tools,
        model=llm_model,
        temperature=temperature,
    )
    electrical_engineer_node = create_agent_node(
        electrical_engineer_prompt,
        "ElectricalEngineer",
        call_agent_model,
        tools=electrical_engineer_tools,
        model=llm_model,
        temperature=temperature,
    )
    control_systems_engineer_node = create_agent_node(
        control_systems_engineer_prompt,
        "ControlSystemsEngineer",
        call_agent_model,
        tools=control_systems_engineer_tools,
        model=llm_model,
        temperature=temperature,
    )
    safety_engineer_node = create_agent_node(
        safety_engineer_prompt,
        "SafetyEngineer",
        call_agent_model,
        tools=safety_engineer_tools,
        model=llm_model,
        temperature=temperature,
    )
    triz_specialist_node = create_agent_node(
        triz_specialist_prompt,
        "TRIZSpecialist",
        call_agent_model,
        tools=triz_specialist_tools,
        model=llm_model,
        temperature=temperature,
    )
    # software_engineer_node = create_agent_node(
    #     software_engineer_prompt, "SoftwareEngineer", call_agent_model,
    #     tools=software_engineer_tools, model=llm_model, temperature=temperature
    # )
    operations_specialist_node = create_agent_node(
        operations_specialist_prompt,
        "OperationsSpecialist",
        call_agent_model,
        tools=operations_specialist_tools,
        model=llm_model,
        temperature=temperature,
    )
    documentation_specialist_node = create_agent_node(
        documentation_specialist_prompt,
        "DocumentationSpecialist",
        call_agent_model,
        tools=documentation_specialist_tools,
        model=llm_model,
        temperature=temperature,
    )
    final_report_maker_node = create_agent_node(
        final_report_maker_prompt,
        "FinalReportMaker",
        call_agent_model,
        tools=final_report_maker_tools,
        model=llm_model,
        temperature=temperature,
    )

    memory = MemorySaver()
    workflow = StateGraph(AgentState)

    # Agent nodes
    workflow.add_node("ProjectManager", project_manager_node)
    workflow.add_node("TRIZSpecialist", triz_specialist_node)
    workflow.add_node("MechanicalEngineer", mechanical_engineer_node)
    workflow.add_node("ElectricalEngineer", electrical_engineer_node)
    workflow.add_node("ControlSystemsEngineer", control_systems_engineer_node)
    workflow.add_node("SafetyEngineer", safety_engineer_node)
    # workflow.add_node("SoftwareEngineer", software_engineer_node)
    workflow.add_node("OperationsSpecialist", operations_specialist_node)
    workflow.add_node("DocumentationSpecialist", documentation_specialist_node)
    workflow.add_node("FinalReportMaker", final_report_maker_node)

    # Tool nodes
    workflow.add_node("triz_specialist_tools", triz_specialist_tool_node)
    workflow.add_node("mechanical_engineer_tools", mechanical_engineer_tool_node)
    workflow.add_node("electrical_engineer_tools", electrical_engineer_tool_node)
    workflow.add_node("control_systems_engineer_tools", control_systems_engineer_tool_node)
    workflow.add_node("safety_engineer_tools", safety_engineer_tool_node)
    # workflow.add_node("software_engineer_tools", software_engineer_tool_node)
    workflow.add_node("operations_specialist_tools", operations_specialist_tool_node)
    workflow.add_node("documentation_specialist_tools", documentation_specialist_tool_node)
    workflow.add_node("final_report_maker_tools", final_report_maker_tool_node)

    # Cleanup node
    workflow.add_node("delete_messages", delete_messages)

    # Edges
    workflow.add_edge(START, "ProjectManager")
    workflow.add_conditional_edges(
        "ProjectManager",
        supervisor_router,
        [
            "TRIZSpecialist",
            "MechanicalEngineer",
            "ElectricalEngineer",
            "ControlSystemsEngineer",
            "SafetyEngineer",
            "OperationsSpecialist",
            "DocumentationSpecialist",
            "ProjectManager",
            "FinalReportMaker",
        ],
    )

    workflow.add_conditional_edges(
        "TRIZSpecialist", triz_specialist_router, ["triz_specialist_tools", "ProjectManager"]
    )
    workflow.add_edge("triz_specialist_tools", "TRIZSpecialist")

    workflow.add_conditional_edges(
        "MechanicalEngineer", mechanical_engineer_router, ["mechanical_engineer_tools", "ProjectManager"]
    )
    workflow.add_edge("mechanical_engineer_tools", "MechanicalEngineer")

    workflow.add_conditional_edges(
        "ElectricalEngineer", electrical_engineer_router, ["electrical_engineer_tools", "ProjectManager"]
    )
    workflow.add_edge("electrical_engineer_tools", "ElectricalEngineer")

    workflow.add_conditional_edges(
        "ControlSystemsEngineer",
        control_systems_engineer_router,
        ["control_systems_engineer_tools", "ProjectManager"],
    )
    workflow.add_edge("control_systems_engineer_tools", "ControlSystemsEngineer")

    workflow.add_conditional_edges(
        "SafetyEngineer", safety_engineer_router, ["safety_engineer_tools", "ProjectManager"]
    )
    workflow.add_edge("safety_engineer_tools", "SafetyEngineer")

    # workflow.add_conditional_edges(
    #     "SoftwareEngineer", software_engineer_router, ["software_engineer_tools", "ProjectManager"]
    # )
    # workflow.add_edge("software_engineer_tools", "SoftwareEngineer")

    workflow.add_conditional_edges(
        "OperationsSpecialist", operations_specialist_router, ["operations_specialist_tools", "ProjectManager"]
    )
    workflow.add_edge("operations_specialist_tools", "OperationsSpecialist")

    workflow.add_conditional_edges(
        "DocumentationSpecialist", documentation_specialist_router, ["documentation_specialist_tools", "delete_messages"]
    )
    workflow.add_edge("documentation_specialist_tools", "DocumentationSpecialist")
    workflow.add_edge("delete_messages", "ProjectManager")

    # Final report maker goes straight to tools then END
    # workflow.add_conditional_edges(
    #     "FinalReportMaker", final_report_maker_router, ["final_report_maker_tools", "ProjectManager"]
    # )
    workflow.add_edge("FinalReportMaker", "final_report_maker_tools")
    workflow.add_edge("final_report_maker_tools", END)

    return workflow.compile(checkpointer=memory)
