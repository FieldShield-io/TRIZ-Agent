"""Evaluation utilities for TRIZ Agents experiments.

Features:
- Load experiment artifacts (JSON or Markdown) and extract the solution text.
- Harsh evaluator prompts for multiple metrics (clarity, coherence, coverage, novelty,
  feasibility, TRIZ adherence, expert-solution alignment).
- Multi-judge orchestration: run a set of evaluator LLMs, average scores per metric.
- Batch processing of all runs for a given agent model.

Requirements:
  - langchain, pydantic, numpy
  - Provider libs depending on judge models (see triz_agents.llm)

Usage (script):
  python -m triz_agents.evaluation
"""

from __future__ import annotations

import glob
import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import numpy as np
from pydantic import BaseModel, Field

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser

from .llm import get_llm, ModelName


# ============================================================================
# Simple helpers from the notebook (tidied)
# ============================================================================
def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Load a JSON dict from disk; return None with a clear message if missing/invalid."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from file {file_path}")
    return None


def get_final_step_value(data: Dict[str, Any]) -> Optional[Any]:
    """Return the value from the highest-numbered key named 'step_X' in a dict."""
    highest = -1
    final_key = None
    for key in data.keys():
        if key.startswith("step_"):
            try:
                n = int(key.split("_")[1])
                if n > highest:
                    highest, final_key = n, key
            except ValueError:
                pass
    return data.get(final_key) if final_key else None


def load_json_content(filepath: str) -> str:
    """Load JSON and return the 'content' field if present, else pretty JSON string."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("content", json.dumps(data))
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return ""


def load_md_content(filepath: str) -> str:
    """Load UTF-8 markdown file content."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return ""


# ============================================================================
# Evaluation schema & chain factory
# ============================================================================
class DetailedEvaluation(BaseModel):
    """Detailed evaluation including a numeric score and feedback."""
    score: int = Field(description="Score from 1 to 10.")
    reasoning: str = Field(description="Detailed summary of reasoning for the score.")
    critique: str = Field(description="Constructive, actionable improvement suggestions.")


_parser = JsonOutputParser(pydantic_object=DetailedEvaluation)


def create_evaluator(llm, prompt_template: PromptTemplate) -> LLMChain:
    """Factory to create an evaluation chain with a JSON parser."""
    return LLMChain(llm=llm, prompt=prompt_template, output_parser=_parser)
    # return prompt_template | llm | _parser


# ============================================================================
# Evaluator prompts (harsh, detailed)
# ============================================================================
def get_clarity_evaluator() -> PromptTemplate:
    template = """
You are a Principal Engineer reviewing a technical proposal. Be strict.

Task: Assess the **Clarity** (1–10). Clarity = unambiguous, precise, well-structured.

Scoring:
- 10: flawless, precise terminology, every sentence purposeful
- 7–9: minor verbosity/jargon
- 4–6: understandable but with ambiguity/structure issues
- 1–3: confusing, disorganized

Your Critique Must:
1) Quote unclear phrasing
2) Provide concrete rewrites
3) Comment on structure

Text:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_coherence_evaluator() -> PromptTemplate:
    template = """
You are a technical editor. Be critical of logical gaps.

Task: Assess **Coherence** (1–10). Coherence = logical flow, no contradictions.

Scoring:
- 10: flawless logic, seamless flow
- 7–9: minor gaps
- 4–6: noticeable leaps/contradictions
- 1–3: incoherent

Your Critique Must:
1) Pinpoint inconsistencies/unsupported claims
2) Explain weak transitions
3) Suggest restructuring

Text:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_coverage_evaluator() -> PromptTemplate:
    template = """
You are the client. Check solution vs. original problem.

Task: Assess **Coverage** (1–10).

Scoring:
- 10: addresses every explicit/implicit aspect
- 7–9: covers major aspects, minor superficial gaps
- 4–6: partial coverage
- 1–3: poor coverage

Your Critique Must:
1) Checklist of requirements from the problem
2) Mark each: fully / partially / ignored
3) Point out biggest gaps

Original Problem:
{input_problem}

Solution:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["input_problem", "prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_novelty_evaluator() -> PromptTemplate:
    template = """
You are a patent examiner.

Task: Assess **Novelty** (1–10).

Scoring:
- 10: groundbreaking, non-obvious
- 7–9: inventive combination
- 4–6: derivative but correct
- 1–3: obvious/cliché

Your Critique Must:
1) Distinguish standard vs. novel parts
2) Cite prior art/common knowledge resemblance
3) Identify most/least original ideas

Text:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_feasibility_evaluator() -> PromptTemplate:
    template = """
You are a CTO. Be pragmatic.

Task: Assess **Feasibility** (1–10).

Scoring:
- 10: practical, grounded, integration considered
- 7–9: feasible but challenging
- 4–6: questionable feasibility
- 1–3: unfeasible hand-waving

Your Critique Must:
1) Challenge claims; are they substantiated?
2) Biggest technical/operational risk
3) Consider cost/maintenance/user adoption

Text:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_triz_adherence_evaluator() -> PromptTemplate:
    template = """
You are a TRIZ Master.

Task: Assess **TRIZ Adherence** (1–10).

Strictly evaluate:
- Correct contradiction type & formulation
- Principle selection relevance
- Solution genuinely derived from principle

Text:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


def get_expert_solution_evaluator() -> PromptTemplate:
    """Compare AI solution to expert benchmark (your long benchmark text kept)."""
    template = """
You are an expert panelist. Compare AI's solution to the expert benchmark.

Task: **Expert Solution Alignment** (1–10).

Benchmark key concepts:
1) Sway control: Sliding Mode Control + input shaping
2) Overload/short circuit: intelligent circuit breaker w/ microcontroller + sensors (Mechanics Substitution)
3) Overheating: smart ventilation w/ self-cleaning filters & sealed bearings (Porous material)

Scoring:
- 10: independently identifies all three with comparable technical detail
- 8–9: matches two; reasonable alternative for the third
- 6–7: matches one; others relevant but miss expert approach
- 3–5: generic, not aligned to expert approaches
- 1–2: no match

Your Critique Must:
1) Checklist: matched / partially matched / missed (quote AI where relevant)
2) Technical accuracy vs. benchmark
3) If missed, what AI proposed and why it falls short

AI Solution:
{prediction}

{format_instructions}
"""
    return PromptTemplate(
        template=template,
        input_variables=["prediction"],
        partial_variables={"format_instructions": _parser.get_format_instructions()},
    )


# ============================================================================
# Multi-judge orchestration
# ============================================================================
def _normalize_eval_output(output: Any) -> Optional[DetailedEvaluation]:
    """Handle LC chain outputs that may be dict/obj/string; return DetailedEvaluation or None."""
    # Already parsed object
    if isinstance(output, DetailedEvaluation):
        return output
    # Some LLMChain.invoke returns dict with 'text'
    if isinstance(output, dict) and "text" in output:
        try:
            data = json.loads(output["text"])
            return DetailedEvaluation(**data)
        except Exception:
            return None
    # Raw JSON string possibly
    if isinstance(output, str):
        try:
            data = json.loads(output)
            return DetailedEvaluation(**data)
        except Exception:
            return None
    return None


def run_multi_judge_evaluation(
    evaluator_models: List[ModelName] | List[str],
    input_problem: str,
    prediction: str,
    *,
    metrics: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Run a suite of evaluators with an ensemble of judge models; average per-metric scores."""
    # Choose metrics (default: just expert_solution like your notebook; expand if desired)
    available = {
        "clarity": get_clarity_evaluator(),
        "coherence": get_coherence_evaluator(),
        "coverage": get_coverage_evaluator(),
        "novelty": get_novelty_evaluator(),
        "feasibility": get_feasibility_evaluator(),
        "triz_adherence": get_triz_adherence_evaluator(),
        "expert_solution": get_expert_solution_evaluator(),
    }
    use_metrics = list(metrics) if metrics else ["expert_solution"]

    metric_prompts = {m: available[m] for m in use_metrics if m in available}
    all_judges_evaluations: Dict[str, List[DetailedEvaluation]] = defaultdict(list)

    for model_name in evaluator_models:
        try:
            judge_llm = get_llm(model_name)
        except Exception as e:
            print(f"Could not instantiate judge model {model_name}. Skipping. Error: {e}")
            continue

        print(f"  --- Evaluating with Judge: {model_name} ---")

        for metric, prompt in metric_prompts.items():
            try:
                evaluator_chain = create_evaluator(judge_llm, prompt)
                input_data = {"prediction": prediction}
                if metric == "coverage":
                    input_data["input_problem"] = input_problem

                result = evaluator_chain.invoke(input_data)
                all_judges_evaluations[metric].append(result['text'])

            except Exception as e:
                print(f"    ! Error running '{metric}' with judge '{model_name}': {e}")

    # Average the scores from all judges for each metric
    final_averaged_evaluation = {}
    for metric, evaluations in all_judges_evaluations.items():
        if not evaluations: continue
        avg_score = np.mean([e['score'] for e in evaluations if 'score' in e and e['score'] != -1])
        final_averaged_evaluation[metric] = {
            "average_score": avg_score,
            "individual_judge_evals": evaluations # Keep details for analysis
        }

    return final_averaged_evaluation


# ============================================================================
# Batch processing of experiment artifacts (Markdown files)
# ============================================================================
def process_all_experiments(
    directory: str,
    agent_model_name: str,
    input_problem: str,
    evaluator_models: List[ModelName] | List[str],
    *,
    metrics: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    """Process all experiment files (.md) for a given agent, evaluate, and aggregate."""
    print(f"\n===== Processing experiments for AGENT: {agent_model_name} =====")
    filepath_pattern = os.path.join(directory, f"{agent_model_name}_*.md")
    experiment_files = glob.glob(filepath_pattern)

    if not experiment_files:
        print(f"No experiment files found for pattern: {filepath_pattern}")
        return {}

    all_runs_evaluations: List[Dict[str, Any]] = []
    for filepath in experiment_files:
        print(f"\n--- Evaluating file: {filepath} ---")
        solution_output = load_md_content(filepath)
        if solution_output:
            eval_result = run_multi_judge_evaluation(
                evaluator_models, input_problem, solution_output, metrics=metrics
            )
            all_runs_evaluations.append(eval_result)

    if not all_runs_evaluations:
        print("No evaluations were generated for the found files.")
        return {
            "agent_model_name": agent_model_name,
            "run_count": 0,
            "evaluator_models_used": evaluator_models,
            "final_average_scores": {},
            "individual_runs_evaluations": [],
        }

    # Aggregate metric averages across runs
    per_metric_scores: Dict[str, List[float]] = defaultdict(list)
    for run_eval in all_runs_evaluations:
        for metric, data in run_eval.items():
            per_metric_scores[metric].append(float(data.get("average_score", -1.0)))

    final_averages = {m: float(np.mean(s)) for m, s in per_metric_scores.items() if s}

    return {
        "agent_model_name": agent_model_name,
        "run_count": len(all_runs_evaluations),
        "evaluator_models_used": evaluator_models,
        "final_average_scores": final_averages,
        "individual_runs_evaluations": all_runs_evaluations,
    }

