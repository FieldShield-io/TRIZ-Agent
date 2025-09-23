"""TRIZ Agents

Public modules:
- llm, agents, graph, state, experiments, evaluation, prompt_templates
- tools (submodule with: triz_tools, rag_tools, other_tools)

Top-level re-exports (convenience):
- get_llm, ModelName
- create_workflow_app
- run_experiment, run_batch
- run_multi_judge_evaluation, process_all_experiments
"""

from __future__ import annotations

import importlib
from typing import Any, Dict, Tuple

__version__ = "0.1.0"

# --- Public submodules exposed at package level ---
# Users can: `import triz_agents; triz_agents.llm.get_llm(...)`, etc.
from . import llm as llm           # noqa: F401
from . import agents as agents     # noqa: F401
from . import graph as graph       # noqa: F401
from . import state as state       # noqa: F401
from . import experiments as experiments   # noqa: F401
from . import evaluation as evaluation     # noqa: F401
from . import prompt_templates as prompt_templates  # noqa: F401
from . import tools as tools       # noqa: F401  # subpackage (with triz_tools, rag_tools, other_tools)

# --- Top-level convenience re-exports (lazy via __getattr__) ---
# Map attribute name -> (module_path, attr_name)
_REEXPORTS: Dict[str, Tuple[str, str]] = {
    # llm
    "get_llm": (".llm", "get_llm"),
    "ModelName": (".llm", "ModelName"),

    # graph
    "create_workflow_app": (".graph", "create_workflow_app"),

    # experiments
    "run_experiment": (".experiments", "run_experiment"),
    "run_batch": (".experiments", "run_batch"),

    # evaluation
    "run_multi_judge_evaluation": (".evaluation", "run_multi_judge_evaluation"),
    "process_all_experiments": (".evaluation", "process_all_experiments"),
}

# Also allow importing tool modules directly at top-level if desired
# e.g., `from triz_agents import triz_tools`
_TOOL_EXPORTS: Dict[str, str] = {
    "triz_tools": ".tools.triz_tools",
    "rag_tools": ".tools.rag_tools",
    "other_tools": ".tools.other_tools",
}

def __getattr__(name: str) -> Any:
    """Lazy attribute loader for top-level re-exports and tool modules."""
    if name in _REEXPORTS:
        mod_path, attr = _REEXPORTS[name]
        mod = importlib.import_module(mod_path, __package__)
        val = getattr(mod, attr)
        globals()[name] = val
        return val
    if name in _TOOL_EXPORTS:
        mod_path = _TOOL_EXPORTS[name]
        mod = importlib.import_module(mod_path, __package__)
        globals()[name] = mod
        return mod
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    """Nice autocomplete in REPLs/IDEs."""
    return sorted(list(globals().keys()) + list(_REEXPORTS.keys()) + list(_TOOL_EXPORTS.keys()))

# What `from triz_agents import *` should bring in
__all__ = [
    "__version__",
    # submodules
    "llm", "agents", "graph", "state", "experiments", "evaluation", "prompt_templates", "tools",
    # tools submodules (convenience)
    "triz_tools", "rag_tools", "other_tools",
    # re-exported callables
    "get_llm", "ModelName",
    "create_workflow_app",
    "run_experiment", "run_batch",
    "run_multi_judge_evaluation", "process_all_experiments",
]
