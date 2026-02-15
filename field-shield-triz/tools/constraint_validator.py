#!/usr/bin/env python3
"""
Field Shield Constraint Validator
===================================
Validates proposed solutions against Field Shield's hard engineering constraints.
Returns PASS/FAIL with detailed explanations.

Usage:
    python constraint_validator.py validate                # Interactive mode
    python constraint_validator.py check <json_file>       # Validate from JSON
    python constraint_validator.py constraints              # Show all constraints
    python constraint_validator.py template                 # Output blank JSON template
"""

import json
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path


@dataclass
class Constraint:
    name: str
    description: str
    unit: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    category: str = "general"
    severity: str = "hard"  # hard = must pass, soft = warning
    notes: str = ""


# ─────────────────────────────────────────────────────────────
# Field Shield Hard Constraints
# ─────────────────────────────────────────────────────────────
CONSTRAINTS = [
    # Power & Energy
    Constraint(
        name="average_power",
        description="Maximum average power consumption (solar/battery budget)",
        unit="W",
        max_value=15.0,
        category="power",
        severity="hard",
        notes="System runs on 100W solar panel + 12V 100Ah battery. 15W average ensures 24hr operation with 5hr effective sun.",
    ),
    Constraint(
        name="peak_power",
        description="Maximum peak power draw (inverter/regulator limit)",
        unit="W",
        max_value=60.0,
        category="power",
        severity="hard",
        notes="Peak during deterrent activation + AI inference + pan-tilt movement.",
    ),
    Constraint(
        name="standby_power",
        description="Standby power during idle surveillance",
        unit="W",
        max_value=8.0,
        category="power",
        severity="soft",
        notes="Target for nighttime operation when solar is unavailable.",
    ),

    # Weight & Size
    Constraint(
        name="total_weight",
        description="Maximum total system weight (including mount)",
        unit="lbs",
        max_value=25.0,
        category="physical",
        severity="hard",
        notes="Must be installable by single person on standard T-post or tripod.",
    ),
    Constraint(
        name="payload_weight",
        description="Maximum sensor/electronics payload weight",
        unit="lbs",
        max_value=12.0,
        category="physical",
        severity="hard",
        notes="Pan-tilt mechanism rated for 12 lbs max payload.",
    ),

    # Environmental
    Constraint(
        name="operating_temp_min",
        description="Minimum operating temperature",
        unit="°C",
        min_value=-20.0,
        category="environmental",
        severity="hard",
        notes="Must operate in northern US winter conditions.",
    ),
    Constraint(
        name="operating_temp_max",
        description="Maximum operating temperature",
        unit="°C",
        max_value=60.0,
        category="environmental",
        severity="hard",
        notes="Direct sun exposure in summer agricultural fields.",
    ),
    Constraint(
        name="ip_rating",
        description="Minimum IP ingress protection rating",
        unit="IP",
        min_value=65.0,
        category="environmental",
        severity="hard",
        notes="IP65 minimum: dust-tight + protected against water jets. IP67 preferred.",
    ),
    Constraint(
        name="wind_resistance",
        description="Maximum wind speed for stable operation",
        unit="mph",
        min_value=50.0,
        category="environmental",
        severity="soft",
        notes="Must survive gusts; stable imaging up to 30mph.",
    ),

    # Performance
    Constraint(
        name="detection_range",
        description="Minimum detection range for deer-sized targets",
        unit="m",
        min_value=200.0,
        category="performance",
        severity="hard",
        notes="Thermal camera must detect deer-sized (1.5m tall) targets at 200m minimum.",
    ),
    Constraint(
        name="response_time",
        description="Maximum time from detection to deterrent activation",
        unit="s",
        max_value=2.0,
        category="performance",
        severity="hard",
        notes="Includes AI classification + pan-tilt slew + deterrent trigger.",
    ),
    Constraint(
        name="classification_accuracy",
        description="Minimum target classification accuracy",
        unit="%",
        min_value=90.0,
        category="performance",
        severity="hard",
        notes="Must distinguish deer/hog from humans, vehicles, livestock.",
    ),
    Constraint(
        name="false_positive_rate",
        description="Maximum false positive rate",
        unit="%",
        max_value=5.0,
        category="performance",
        severity="hard",
        notes="Farmer tolerance threshold. Higher causes system distrust and disablement.",
    ),

    # Cost
    Constraint(
        name="unit_bom_cost",
        description="Maximum bill-of-materials cost per unit",
        unit="USD",
        max_value=2500.0,
        category="cost",
        severity="hard",
        notes="Target retail price $4,000-$5,000 with 40-50% gross margin.",
    ),
    Constraint(
        name="annual_operating_cost",
        description="Maximum annual operating cost (connectivity, maintenance)",
        unit="USD/year",
        max_value=200.0,
        category="cost",
        severity="soft",
        notes="Cellular connectivity + replacement parts budget.",
    ),

    # Compute
    Constraint(
        name="jetson_tdp",
        description="NVIDIA Jetson thermal design power limit",
        unit="W",
        max_value=15.0,
        category="compute",
        severity="hard",
        notes="Jetson Orin Nano: 7-15W configurable. Must run within selected power mode.",
    ),
    Constraint(
        name="inference_fps",
        description="Minimum AI inference framerate",
        unit="fps",
        min_value=5.0,
        category="compute",
        severity="hard",
        notes="5 FPS minimum for reliable tracking; 10+ FPS preferred.",
    ),

    # Acoustic Deterrent
    Constraint(
        name="deterrent_spl",
        description="Sound pressure level at target distance",
        unit="dB SPL @ 100m",
        min_value=70.0,
        category="deterrent",
        severity="soft",
        notes="Must be audible and startling to deer at 100m.",
    ),
    Constraint(
        name="deterrent_frequency_range",
        description="Acoustic deterrent frequency range",
        unit="Hz",
        min_value=200.0,
        max_value=8000.0,
        category="deterrent",
        severity="soft",
        notes="Deer hearing sensitivity range. Below 200Hz less effective, above 8kHz attenuates rapidly outdoors.",
    ),
]


@dataclass
class ValidationResult:
    constraint_name: str
    status: str  # PASS, FAIL, WARN, SKIP
    message: str
    proposed_value: Optional[float] = None
    limit_value: Optional[float] = None
    severity: str = "hard"


def validate_solution(proposed: Dict[str, float]) -> List[ValidationResult]:
    """Validate a proposed solution against all constraints."""
    results = []

    for c in CONSTRAINTS:
        if c.name not in proposed:
            results.append(ValidationResult(
                constraint_name=c.name,
                status="SKIP",
                message=f"Not specified in proposal. Constraint: {c.description} ({c.unit})",
                severity=c.severity,
            ))
            continue

        value = proposed[c.name]
        passed = True
        messages = []

        if c.min_value is not None and value < c.min_value:
            passed = False
            messages.append(f"Below minimum: {value} < {c.min_value} {c.unit}")

        if c.max_value is not None and value > c.max_value:
            passed = False
            messages.append(f"Exceeds maximum: {value} > {c.max_value} {c.unit}")

        if passed:
            margin = ""
            if c.max_value is not None:
                pct = ((c.max_value - value) / c.max_value) * 100
                margin = f" (margin: {pct:.0f}%)"
            elif c.min_value is not None:
                pct = ((value - c.min_value) / c.min_value) * 100
                margin = f" (margin: +{pct:.0f}%)"
            status = "PASS"
            msg = f"✅ {c.description}: {value} {c.unit}{margin}"
        else:
            status = "FAIL" if c.severity == "hard" else "WARN"
            icon = "❌" if status == "FAIL" else "⚠️"
            msg = f"{icon} {c.description}: {'; '.join(messages)}"

        results.append(ValidationResult(
            constraint_name=c.name,
            status=status,
            message=msg,
            proposed_value=value,
            limit_value=c.max_value or c.min_value,
            severity=c.severity,
        ))

    return results


def format_results(results: List[ValidationResult]) -> str:
    """Format validation results as a readable report."""
    lines = [
        "=" * 70,
        "FIELD SHIELD CONSTRAINT VALIDATION REPORT",
        "=" * 70,
        "",
    ]

    # Summary
    hard_fails = sum(1 for r in results if r.status == "FAIL")
    soft_warns = sum(1 for r in results if r.status == "WARN")
    passes = sum(1 for r in results if r.status == "PASS")
    skips = sum(1 for r in results if r.status == "SKIP")

    if hard_fails > 0:
        lines.append(f"🔴 OVERALL: FAIL — {hard_fails} hard constraint(s) violated")
    elif soft_warns > 0:
        lines.append(f"🟡 OVERALL: PASS WITH WARNINGS — {soft_warns} soft constraint(s) exceeded")
    else:
        lines.append(f"🟢 OVERALL: PASS — All specified constraints met")

    lines.append(f"   ({passes} pass, {hard_fails} fail, {soft_warns} warn, {skips} not specified)")
    lines.append("")

    # Group by category
    categories = {}
    for r in results:
        c = next((c for c in CONSTRAINTS if c.name == r.constraint_name), None)
        cat = c.category if c else "other"
        categories.setdefault(cat, []).append(r)

    for cat, cat_results in categories.items():
        lines.append(f"\n--- {cat.upper()} ---")
        for r in cat_results:
            lines.append(f"  {r.message}")

    lines.append("\n" + "=" * 70)
    return "\n".join(lines)


def show_constraints() -> str:
    """Display all constraints in a readable format."""
    lines = [
        "FIELD SHIELD HARD ENGINEERING CONSTRAINTS",
        "=" * 60,
    ]

    categories = {}
    for c in CONSTRAINTS:
        categories.setdefault(c.category, []).append(c)

    for cat, constraints in categories.items():
        lines.append(f"\n{'─'*40}")
        lines.append(f"  {cat.upper()}")
        lines.append(f"{'─'*40}")
        for c in constraints:
            sev = "🔴 HARD" if c.severity == "hard" else "🟡 SOFT"
            limit = ""
            if c.min_value is not None and c.max_value is not None:
                limit = f"{c.min_value}–{c.max_value} {c.unit}"
            elif c.min_value is not None:
                limit = f"≥ {c.min_value} {c.unit}"
            elif c.max_value is not None:
                limit = f"≤ {c.max_value} {c.unit}"

            lines.append(f"\n  {sev} {c.name}")
            lines.append(f"    {c.description}")
            lines.append(f"    Limit: {limit}")
            if c.notes:
                lines.append(f"    Notes: {c.notes}")

    return "\n".join(lines)


def generate_template() -> str:
    """Generate a blank JSON template for solution validation."""
    template = {}
    for c in CONSTRAINTS:
        template[c.name] = None
    return json.dumps(template, indent=2)


def main():
    if len(sys.argv) < 2:
        print("""
Field Shield Constraint Validator
===================================

Commands:
  constraints       Show all constraints with limits and notes
  template          Output a blank JSON template for proposals
  check <file.json> Validate a proposal from a JSON file
  validate          Interactive validation mode

Example JSON:
  {
    "average_power": 12.5,
    "total_weight": 22.0,
    "detection_range": 250.0,
    "response_time": 1.5,
    "unit_bom_cost": 2200.0
  }
        """)
        return

    cmd = sys.argv[1].lower()

    if cmd == "constraints":
        print(show_constraints())

    elif cmd == "template":
        print(generate_template())

    elif cmd == "check":
        if len(sys.argv) < 3:
            print("Usage: python constraint_validator.py check <file.json>")
            return
        json_path = Path(sys.argv[2])
        if not json_path.exists():
            print(f"ERROR: File not found: {json_path}")
            return
        with open(json_path, "r") as f:
            proposed = json.load(f)
        # Filter out None values
        proposed = {k: v for k, v in proposed.items() if v is not None}
        results = validate_solution(proposed)
        print(format_results(results))

    elif cmd == "validate":
        print("Interactive validation mode. Enter values (blank to skip):\n")
        proposed = {}
        for c in CONSTRAINTS:
            limit = ""
            if c.min_value is not None:
                limit += f"min={c.min_value}"
            if c.max_value is not None:
                limit += f" max={c.max_value}"
            val = input(f"  {c.name} ({c.unit}, {limit.strip()}): ").strip()
            if val:
                try:
                    proposed[c.name] = float(val)
                except ValueError:
                    print(f"    Skipping (not a number)")
        results = validate_solution(proposed)
        print(format_results(results))

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
