#!/usr/bin/env python3
"""
TRIZ Toolkit for Field Shield — Claude Desktop Optimized
=========================================================
Standalone TRIZ tools that can be called from the command line.
Direct CLI interfaces for TRIZ analysis — no external dependencies required.

Usage:
    python triz_toolkit.py features                          # List 39 TRIZ features
    python triz_toolkit.py matrix "Speed" "Use of energy by moving object"  # Matrix lookup
    python triz_toolkit.py principles 1 2 35                 # Look up principles
    python triz_toolkit.py analyze "problem description"     # Auto-identify contradictions
"""

import json
import sys
from pathlib import Path
from typing import List, Optional, Dict, Any

# Resolve data directory
DATA_DIR = Path(__file__).resolve().parent / "data"


# ─────────────────────────────────────────────────────────────
# TRIZ Features (39 Engineering Parameters)
# ─────────────────────────────────────────────────────────────
FEATURES = [
    "Weight of moving object",
    "Weight of stationary object",
    "Length of moving object",
    "Length of stationary object",
    "Area of moving object",
    "Area of stationary object",
    "Volume of moving object",
    "Volume of stationary object",
    "Speed",
    "Force (Intensity)",
    "Stress or pressure",
    "Shape",
    "Stability of the object's composition",
    "Strength",
    "Duration of action of moving object",
    "Duration of action by stationary object",
    "Temperature",
    "Illumination intensity",
    "Use of energy by moving object",
    "Use of energy by stationary object",
    "Power",
    "Loss of Energy",
    "Loss of substance",
    "Loss of Information",
    "Loss of Time",
    "Quantity of substance/the matter",
    "Reliability",
    "Measurement accuracy",
    "Manufacturing precision",
    "Object-affected harmful factors",
    "Object-generated harmful factors",
    "Ease of manufacture",
    "Ease of operation",
    "Ease of repair",
    "Adaptability or versatility",
    "Device complexity",
    "Difficulty of detecting and measuring",
    "Extent of automation",
    "Productivity",
]

# Field Shield v2 — Novel Concept Research challenge mappings
# These map high-level Field Shield design tensions to TRIZ feature pairs
# for quick contradiction matrix lookups.
#
# Primary tensions: economics vs. performance, anti-habituation vs. simplicity,
# scalability vs. coverage quality
FIELD_SHIELD_FEATURE_MAP = {
    # Economics–Performance Nexus
    "cost_vs_coverage": ("Area of stationary object", "Ease of manufacture"),
    "cost_vs_detection": ("Measurement accuracy", "Ease of manufacture"),
    "cost_vs_deterrent_strength": ("Force (Intensity)", "Ease of manufacture"),
    "scalability": ("Area of stationary object", "Device complexity"),

    # Anti-Habituation Challenge
    "anti_habituation": ("Adaptability or versatility", "Device complexity"),
    "deterrent_unpredictability": ("Adaptability or versatility", "Reliability"),
    "multi_modal_deterrence": ("Force (Intensity)", "Device complexity"),
    "response_adaptation": ("Extent of automation", "Loss of Information"),

    # Detection & Response
    "detection_range": ("Measurement accuracy", "Loss of Energy"),
    "response_time": ("Speed", "Measurement accuracy"),
    "false_positive_rate": ("Measurement accuracy", "Productivity"),
    "night_detection": ("Difficulty of detecting and measuring", "Use of energy by stationary object"),

    # Field Deployment
    "installation_simplicity": ("Ease of operation", "Area of stationary object"),
    "maintenance_burden": ("Ease of repair", "Extent of automation"),
    "weatherproofing": ("Reliability", "Temperature"),
    "infrastructure_reuse": ("Ease of manufacture", "Adaptability or versatility"),
}


def get_features() -> str:
    """Return the 39 TRIZ features as a numbered list."""
    lines = []
    for i, feat in enumerate(FEATURES, 1):
        lines.append(f"  {i:2d}. {feat}")
    return "TRIZ 39 Engineering Parameters:\n" + "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# TRIZ Contradiction Matrix
# ─────────────────────────────────────────────────────────────
def load_matrix():
    """Load the TRIZ contradiction matrix from the Excel file."""
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas is required. Install with: pip install pandas xlrd", file=sys.stderr)
        sys.exit(1)

    matrix_path = DATA_DIR / "triz_matrix.xls"
    if not matrix_path.exists():
        print(f"ERROR: Matrix file not found at {matrix_path}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_excel(matrix_path, index_col=1, engine="xlrd")
    df.columns = df.columns.astype(str).str.strip().str.lower()
    df.index = df.index.astype(str).str.strip().str.lower()
    return df


def matrix_lookup(improving: str, worsening: str) -> str:
    """Look up the contradiction matrix for two features."""
    df = load_matrix()
    imp = improving.strip().lower()
    wors = worsening.strip().lower()

    try:
        result = df.loc[imp, wors]
    except KeyError:
        # Try fuzzy matching
        imp_matches = [idx for idx in df.index if imp in idx]
        wors_matches = [col for col in df.columns if wors in col]

        if imp_matches and wors_matches:
            result = df.loc[imp_matches[0], wors_matches[0]]
            improving = imp_matches[0]
            worsening = wors_matches[0]
        else:
            return (
                f"❌ Features not found in matrix.\n"
                f"  Improving: '{improving}' → matches: {imp_matches or 'none'}\n"
                f"  Worsening: '{worsening}' → matches: {wors_matches or 'none'}\n"
                f"\nUse 'python triz_toolkit.py features' to see valid feature names."
            )

    import pandas as pd
    if pd.isna(result):
        return f"No inventive principles listed for: improving '{improving}' / worsening '{worsening}'"

    principles_str = str(result).strip()
    return (
        f"TRIZ Contradiction Matrix Result:\n"
        f"  Improving: {improving}\n"
        f"  Worsening: {worsening}\n"
        f"  Recommended Principles: {principles_str}\n"
    )


# ─────────────────────────────────────────────────────────────
# TRIZ Inventive Principles (40 Principles)
# ─────────────────────────────────────────────────────────────
def load_principles() -> Dict[str, Any]:
    """Load all 40 TRIZ principles from JSON."""
    json_path = DATA_DIR / "triz_principles.json"
    if not json_path.exists():
        print(f"ERROR: Principles file not found at {json_path}", file=sys.stderr)
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_principles(numbers: List[str]) -> str:
    """Look up specific TRIZ principles by number."""
    data = load_principles()
    results = []

    for num in numbers:
        key = str(int(num)) if num.isdigit() else num
        if key in data:
            entry = data[key]
            result_lines = [f"\n{'='*60}", f"Principle {key}: {entry['Principle']}", f"{'='*60}"]
            for sub_name, examples in entry.get("Sub-Principles", {}).items():
                result_lines.append(f"\n  ▸ {sub_name}")
                for ex in examples:
                    result_lines.append(f"    - {ex}")
            results.append("\n".join(result_lines))
        else:
            results.append(f"\n❌ Principle {num} not found (valid range: 1-40)")

    return "\n".join(results)


# ─────────────────────────────────────────────────────────────
# Field Shield Contradiction Analyzer
# ─────────────────────────────────────────────────────────────
def analyze_field_shield_challenge(challenge_key: Optional[str] = None) -> str:
    """Map a Field Shield challenge to its TRIZ contradiction and look up principles."""
    if challenge_key and challenge_key in FIELD_SHIELD_FEATURE_MAP:
        improving, worsening = FIELD_SHIELD_FEATURE_MAP[challenge_key]
        result = f"Field Shield Challenge: {challenge_key}\n"
        result += matrix_lookup(improving, worsening)
        return result

    # Show all pre-mapped challenges
    lines = ["Field Shield Pre-Mapped TRIZ Contradictions:", "=" * 60]
    for key, (imp, wors) in FIELD_SHIELD_FEATURE_MAP.items():
        lines.append(f"\n  {key}:")
        lines.append(f"    Improving: {imp}")
        lines.append(f"    Worsening: {wors}")

    lines.append(f"\n\nUsage: python triz_toolkit.py field-shield <challenge_key>")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
# CLI Interface
# ─────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("""
TRIZ Toolkit for Field Shield — Claude Desktop Optimized
=========================================================

Commands:
  features                              List all 39 TRIZ engineering parameters
  matrix <improving> <worsening>        Look up the contradiction matrix
  principles <num1> [num2] ...          Look up inventive principles by number
  field-shield [challenge_key]          Show Field Shield contradictions / analyze one
  all-principles                        List all 40 principle names

Examples:
  python triz_toolkit.py features
  python triz_toolkit.py matrix "Speed" "Use of energy by moving object"
  python triz_toolkit.py principles 1 15 35
  python triz_toolkit.py field-shield detection_range
  python triz_toolkit.py field-shield
        """)
        return

    cmd = sys.argv[1].lower()

    if cmd == "features":
        print(get_features())

    elif cmd == "matrix":
        if len(sys.argv) < 4:
            print("Usage: python triz_toolkit.py matrix <improving_feature> <worsening_feature>")
            return
        print(matrix_lookup(sys.argv[2], sys.argv[3]))

    elif cmd == "principles":
        if len(sys.argv) < 3:
            print("Usage: python triz_toolkit.py principles <num1> [num2] ...")
            return
        print(get_principles(sys.argv[2:]))

    elif cmd == "field-shield":
        key = sys.argv[2] if len(sys.argv) > 2 else None
        print(analyze_field_shield_challenge(key))

    elif cmd == "all-principles":
        data = load_principles()
        print("TRIZ 40 Inventive Principles:")
        print("=" * 50)
        for key in sorted(data.keys(), key=lambda x: int(x)):
            print(f"  {key:>2}. {data[key]['Principle']}")

    else:
        print(f"Unknown command: {cmd}")
        print("Run without arguments to see usage.")


if __name__ == "__main__":
    main()
