"""TRIZ utilities: 39 features, 40 principles, and the contradiction matrix.

This module exposes three LangChain tools:
- triz_contradiction_matrix(improving_feature, worsening_feature) -> str
- triz_principles(principle_numbers: list[int|str]) -> dict
- triz_features() -> str

Data files are expected under `triz_agents/tools/sources/`:
- triz_matrix.xls
- triz_principles.json
- triz_features.txt

The loader resolves files both in a source checkout and when installed as a package.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable

import pandas as pd
from langchain_core.tools import tool

# ---------------------------------------------------------------------
# Paths & resource resolution
# ---------------------------------------------------------------------

# In dev (editable install) these will exist on disk; in a packaged install we also try importlib.resources.
_SOURCES_DIR = Path(__file__).resolve().parent / "sources"


def _resource_path(filename: str) -> Path:
    """Return a readable path to `filename` inside the local `sources/` folder.

    Falls back to importlib.resources if needed (works after packaging).
    """
    candidate = _SOURCES_DIR / filename
    if candidate.exists():
        return candidate

    # Fallback for packaged installs
    try:
        from importlib.resources import files

        return files(__package__.rsplit(".", 1)[0] + ".tools").joinpath("sources", filename)
    except Exception:
        # Last resort: return the original candidate (will raise on open if missing)
        return candidate


# ---------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------
def load_triz_matrix(file_path: str | Path) -> pd.DataFrame:
    """Load the TRIZ contradiction matrix from an Excel file (XLS)."""
    file_path = Path(file_path)
    # xlrd is the typical engine for .xls; if it's not installed, pandas will raise a helpful error.
    df = pd.read_excel(file_path, index_col=1, engine="xlrd")
    # Normalize headers & index (case-insensitive, trimmed)
    df.columns = df.columns.astype(str).str.strip().str.lower()
    df.index = df.index.astype(str).str.strip().str.lower()
    return df


# ---------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------
@tool
def triz_contradiction_matrix(improving_feature: str, worsening_feature: str) -> str:
    """Use the TRIZ contradiction matrix to retrieve recommended inventive principles.

    Args:
        improving_feature: TRIZ feature being improved (case-insensitive).
        worsening_feature: TRIZ feature that gets worse (case-insensitive).

    Returns:
        A human-readable string listing the recommended principles, or a clear message if none found.
    """
    improving = improving_feature.strip().lower()
    worsening = worsening_feature.strip().lower()

    # Load the matrix once per call (fast enough & keeps the tool stateless)
    matrix_path = _resource_path("triz_matrix.xls")
    try:
        triz_matrix = load_triz_matrix(matrix_path)
    except Exception as e:
        return (
            "Could not load TRIZ matrix. Ensure 'triz_matrix.xls' is present and that the 'xlrd' "
            f"dependency is installed. Details: {e}"
        )

    try:
        principles = triz_matrix.loc[improving, worsening]
    except KeyError:
        return (
            f"Contradiction not found for improving '{improving_feature}' and worsening "
            f"'{worsening_feature}'. Please verify the feature names."
        )

    if pd.isna(principles):
        result = "No inventive principles available for this contradiction."
    else:
        result = str(principles)

    return (
        f"Inventive principles for improving '{improving_feature}' while worsening "
        f"'{worsening_feature}': {result}"
    )


@tool
def triz_principles(principle_numbers: Iterable[int | str]) -> Dict[Any, Any]:
    """Retrieve multiple TRIZ principles by their numbers.

    Args:
        principle_numbers: Iterable of principle identifiers (ints or strings).

    Returns:
        Dict mapping the input number to its data (or a not-found message).
    """
    json_file = _resource_path("triz_principles.json")

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            triz_data = json.load(f)
    except Exception as e:
        return {"error": f"Could not load triz_principles.json: {e}"}

    result: Dict[Any, Any] = {}
    for number in principle_numbers:
        try:
            key = str(int(number))  # normalize 1 -> "1", "01" -> "1"
        except Exception:
            key = str(number)

        if key in triz_data:
            result[number] = triz_data[key]
        else:
            result[number] = f"Principle {number} not found in the TRIZ data."

    return result


@tool
def triz_features() -> str:
    """Retrieve the list of 39 TRIZ features (parameters) from a text file."""
    txt_file = _resource_path("triz_features.txt")
    try:
        with open(txt_file, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Could not load triz_features.txt: {e}"
