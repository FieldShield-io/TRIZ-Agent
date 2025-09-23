"""Agent constructors and orchestration helpers for TRIZ Agents."""

from __future__ import annotations

from functools import partial
from typing import Any, Dict, Iterable, List, Optional

from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate

from .llm import get_llm


# ----------------------------------------------------------------------
# Factory: create_agent_node
# ----------------------------------------------------------------------
def create_agent_node(
    prompt: ChatPromptTemplate,
    name: str,
    call_model_func,
    *,
    tools: Optional[Iterable[Any]] = None,
    model: str = "gpt-4o",
    temperature: float = 0.0,
):
    """
    Create a callable "node" for a role agent.

    Binds:
      - a ChatPromptTemplate (role-specific prompt)
      - an LLM with optional tools
      - the role's model-calling function (e.g., call_agent_model)

    Returns:
      functools.partial that accepts a single `state` argument and returns a
      state delta (Dict[str, Any]) compatible with LangGraph.
    """
    # Build LLM
    llm = get_llm(model=model, temperature=temperature)

    # Bind tools if provided
    tool_list = list(tools) if tools else []
    if tool_list:
        llm = llm.bind_tools(tool_list)

    # Chain: prompt -> llm
    agent = prompt | llm

    # The graph will call: node(state)
    return partial(call_model_func, agent=agent, name=name, tools=tool_list)


# ----------------------------------------------------------------------
# Model-call functions
# ----------------------------------------------------------------------
def call_project_manager_model(
    state: Dict[str, Any],
    *,
    agent,
    name: str,
    tools: List[Any],
) -> Dict[str, Any]:
    """
    Supervisor/PM node:
      - Invokes the agent with team context and steps so far.
      - Expects the LLM to return a mapping with keys: {"next": str, "message": str}.
      - Translates to {"next": ..., "messages": [HumanMessage(...)]}.
    """
    members = [
        "ProjectManager",
        "MechanicalEngineer",
        "ElectricalEngineer",
        "ControlSystemsEngineer",
        "SafetyEngineer",
        "TRIZSpecialist",
        "OperationsSpecialist",
        "DocumentationSpecialist",
    ]

    messages = state["messages"]
    steps_documentation = state["steps_documentation"]

    # Exclude self from member list string
    members = [m for m in members if m != name]
    members_names = ", ".join(members)

    response = agent.invoke(
        {
            "members_names": members_names,
            "messages": messages,
            "steps_documentation": steps_documentation,
        }
    )

    # Expect a dict-like response from the PM prompt (as per notebook logic)
    next_role = response.get("next", "FinalReportMaker")
    # If PM wants PM again while state also had PM, flip to FINISH
    if state.get("next") == "ProjectManager" and next_role == "ProjectManager":
        next_role = "FINISH"

    message_text = response.get("message", "")
    return {
        "next": next_role,
        "messages": [HumanMessage(content=message_text, name=name)],
    }


def call_agent_model(
    state: Dict[str, Any],
    *,
    agent,
    name: str,
    tools: List[Any],
) -> Dict[str, Any]:
    """
    Generic role node:
      - Invokes the agent with team & tools context.
      - If the model returns tool calls, emit them (optionally with any assistant text).
      - Otherwise emit a plain HumanMessage from this role.
    """
    messages = state["messages"]
    steps_documentation = state["steps_documentation"]

    members = [
        "ProjectManager",
        "MechanicalEngineer",
        "ElectricalEngineer",
        "ControlSystemsEngineer",
        "SafetyEngineer",
        "TRIZSpecialist",
        "OperationsSpecialist",
        "DocumentationSpecialist",
        "FinalReportMaker",
    ]
    members = [m for m in members if m != name]
    members_names = ", ".join(members)

    def _tool_display_name(t: Any) -> str:
        # Prefer LangChain tool.name, fall back to __name__, else type name
        return getattr(t, "name", None) or getattr(t, "__name__", None) or type(t).__name__

    tools_names = ", ".join(_tool_display_name(t) for t in tools)

    response = agent.invoke(
        {
            "members_names": members_names,
            "tools": tools_names,
            "messages": messages,
            "steps_documentation": steps_documentation,
        }
    )

    # When the LLM returns a tool-use message (AIMessage with tool_calls)
    # we mirror that out so the graph routes to ToolNode.
    if hasattr(response, "tool_calls") and response.tool_calls:
        # If the assistant produced both text and tool_calls, keep both.
        if getattr(response, "content", None):
            return {
                "messages": [
                    HumanMessage(content=response.content, name=name),
                    AIMessage(content="", name=name, tool_calls=response.tool_calls),
                ]
            }
        # Tool calls only
        return {"messages": [AIMessage(content="", name=name, tool_calls=response.tool_calls)]}

    # Plain text response
    return {"messages": [HumanMessage(content=getattr(response, "content", str(response)), name=name)]}
