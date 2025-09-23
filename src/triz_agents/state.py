"""State types for the agent graph."""
from typing import Annotated, List, TypedDict
from langgraph.graph.message import add_messages
from langchain.schema import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    next: str
    problem_description: str
    steps_documentation: Annotated[List[BaseMessage], add_messages]
