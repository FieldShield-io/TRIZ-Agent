"""Experiment helpers for TRIZ Agents.

Run the full workflow on a fixed prompt and save the results to JSON.
Designed to work in plain Python and (optionally) Google Colab.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

from langchain.schema import HumanMessage

from .graph import create_workflow_app


_DEFAULT_PROMPT = (
    "Solve the following problem: Gantry cranes find extensive application across various "
    "industries, employed to move hefty loads and dangerous substances within shipping docks, "
    "building sites, steel plants, storage facilities, and similar industrial settings. "
    "The crane should move the load fast without causing any unnecessary excessive swing at "
    "the final position. Moreover, gantry cranes which always lift excessive load may result "
    "in sudden stop of the crane. The crane operators' attempt to lift heavier loads at a "
    "faster pace has led to recurrent malfunctions, including overheating, and the increased "
    "speed has caused excessive swinging or swaying of the lifted load, posing a safety hazard."
)


def _is_colab() -> bool:
    """Detect if running in Google Colab."""
    try:  # type: ignore[attr-defined]
        import google.colab  # noqa: F401
        return True
    except Exception:
        return False


def _ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def run_experiment(
    model_name: str = "gpt-4o",
    thread_id: str = "exp-0001",
    *,
    prompt: str = _DEFAULT_PROMPT,
    temperature: float = 0.0,
    recursion_limit: int = 250,
    out_dir: str | Path = "experiments",
    download: bool = False,
) -> Dict[str, Any]:
    """Run a single workflow experiment and save results to JSON.

    Args:
        model_name: Chat model to use (e.g., 'gpt-4o', 'gemini-1.5-pro', etc.).
        thread_id: Identifier for the conversation thread (used by LangGraph checkpointing).
        prompt: Task prompt to seed the workflow.
        temperature: LLM temperature (some reasoning models may ignore this).
        recursion_limit: Safety cap for graph recursion.
        out_dir: Directory to save JSON results.
        download: If True (or running in Colab), trigger file download at the end.

    Returns:
        A dict with metadata and extracted steps.
    """
    app = create_workflow_app(llm_model=model_name, temperature=temperature)
    cfg = {"configurable": {"thread_id": thread_id}, "recursion_limit": recursion_limit}

    # Kick off the workflow
    input_msg = HumanMessage(content=prompt)
    app.invoke({"messages": [input_msg]}, cfg, stream_mode="values")

    # Snapshot state
    state = app.get_state(cfg)
    values = getattr(state, "values", {}) or {}

    # Extract steps
    steps = []
    for i, msg in enumerate(values.get("steps_documentation", []) or []):
        # msg may be a BaseMessage; keep content + name if present
        content = getattr(msg, "content", str(msg))
        name = getattr(msg, "name", "DocumentationSpecialist")
        steps.append({"index": i + 1, "author": name, "content": content})

    # Build result dict
    result: Dict[str, Any] = {
        "metadata": {
            "model": model_name,
            "temperature": temperature,
            "thread_id": thread_id,
            "recursion_limit": recursion_limit,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        },
        "prompt": prompt,
        "num_steps": len(steps),
        "steps": steps,
    }

    # Save
    out_path = Path(out_dir)
    _ensure_dir(out_path)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    safe_model = model_name.replace("/", "_")
    file_path = out_path / f"{safe_model}_thread-{thread_id}_{ts}.json"

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"[experiments] Results saved to {file_path}")

    # Optional download (useful in Colab)
    if download or _is_colab():
        try:
            from google.colab import files  # type: ignore
            files.download(str(file_path))  # pragma: no cover
        except Exception as e:  # pragma: no cover
            print(f"[experiments] Could not trigger download: {e}")

    return result


def run_batch(
    models: Iterable[str],
    *,
    base_thread_id: str = "batch",
    **kwargs: Any,
) -> Dict[str, Dict[str, Any]]:
    """Run `run_experiment` over a list of models and return results keyed by model.

    Args:
        models: Iterable of model names.
        base_thread_id: Prefix for thread IDs (each model gets its own suffix).
        **kwargs: Forwarded to `run_experiment` (e.g., prompt=..., temperature=...).

    Returns:
        Dict mapping model name -> experiment result dict.
    """
    results: Dict[str, Dict[str, Any]] = {}
    for idx, model in enumerate(models, start=1):
        thread_id = f"{base_thread_id}-{idx:02d}"
        print(f"[experiments] Running {model} (thread: {thread_id}) ...")
        results[model] = run_experiment(model, thread_id, **kwargs)
    return results
