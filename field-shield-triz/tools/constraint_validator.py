#!/usr/bin/env python3
"""
Field Shield Constraint Validator (v2 — Novel Concept Research)
================================================================
Validates proposed solutions against Field Shield's economic and engineering
constraints for scalable wildlife deterrence at $100/acre/year.

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
# Field Shield Constraints — Novel Concept Research (v2)
# Target: $100/acre/year, 50-acre blocks, scalable, anti-habituation
# ─────────────────────────────────────────────────────────────
CONSTRAINTS = [
    # Economics (PRIMARY — the binding constraints)
    Constraint(
        name="cost_per_acre_year",
        description="Maximum annual cost per acre (amortized capex + opex)",
        unit="USD/acre/year",
        max_value=100.0,
        category="economics",
        severity="hard",
        notes="THE binding constraint. Capex amortized over system lifetime + annual operating costs.",
    ),
    Constraint(
        name="block_size",
        description="Standard coverage block size",
        unit="acres",
        min_value=50.0,
        category="economics",
        severity="hard",
        notes="The primary design unit. Solution must cover at least 50 contiguous acres.",
    ),
    Constraint(
        name="capital_cost_50acre",
        description="Total capital equipment cost for a 50-acre block",
        unit="USD",
        max_value=15000.0,
        category="economics",
        severity="hard",
        notes="At 5-year amortization: $3,000/year. At 3-year: max $9,000 total.",
    ),
    Constraint(
        name="annual_operating_cost",
        description="Annual operating cost per 50-acre block",
        unit="USD/year",
        max_value=2000.0,
        category="economics",
        severity="hard",
        notes="Maintenance, consumables, power, connectivity. Must leave room for capex amortization within $5K/year total.",
    ),
    Constraint(
        name="installation_cost",
        description="One-time installation cost per 50-acre block",
        unit="USD",
        max_value=2000.0,
        category="economics",
        severity="soft",
        notes="Professional or farmer-installed. Added to capex for amortization.",
    ),
    Constraint(
        name="roi_payback_years",
        description="Farmer ROI payback period",
        unit="years",
        max_value=2.0,
        category="economics",
        severity="soft",
        notes="Based on crop damage prevented vs. total cost. Farmers need fast payback.",
    ),

    # Scalability
    Constraint(
        name="cost_scaling_factor",
        description="Cost multiplier for doubling acreage (1.0 = linear, <1.0 = sub-linear)",
        unit="ratio",
        max_value=2.0,
        category="scalability",
        severity="soft",
        notes="Sub-linear scaling (<2.0) means adding 50 more acres costs less than the first 50. Target <1.7.",
    ),
    Constraint(
        name="coverage_completeness",
        description="Percentage of block area effectively protected",
        unit="%",
        min_value=90.0,
        category="scalability",
        severity="hard",
        notes="Gaps in coverage will be exploited by wildlife. 90% minimum.",
    ),
    Constraint(
        name="node_count_50acre",
        description="Number of nodes/units required per 50-acre block",
        unit="nodes",
        max_value=50.0,
        category="scalability",
        severity="soft",
        notes="Fewer nodes = lower maintenance. Target <25. Hard limit 50 (1 per acre).",
    ),

    # Environmental
    Constraint(
        name="operating_temp_min",
        description="Minimum operating temperature",
        unit="°C",
        min_value=-20.0,
        category="environmental",
        severity="hard",
        notes="Continental US winter conditions.",
    ),
    Constraint(
        name="operating_temp_max",
        description="Maximum operating temperature",
        unit="°C",
        max_value=50.0,
        category="environmental",
        severity="hard",
        notes="Summer agricultural field conditions.",
    ),
    Constraint(
        name="wind_resistance",
        description="Minimum wind survival speed",
        unit="mph",
        min_value=50.0,
        category="environmental",
        severity="hard",
        notes="Open agricultural field wind conditions.",
    ),

    # Detection Performance
    Constraint(
        name="detection_range",
        description="Detection range per node for deer-sized targets",
        unit="m",
        min_value=50.0,
        category="detection",
        severity="soft",
        notes="Longer range = fewer nodes needed. 50m minimum, 100m+ preferred.",
    ),
    Constraint(
        name="response_time",
        description="Time from detection to deterrent activation",
        unit="s",
        max_value=5.0,
        category="detection",
        severity="soft",
        notes="5s acceptable if deterrent is highly effective. <2s preferred.",
    ),
    Constraint(
        name="classification_accuracy",
        description="Target species classification accuracy",
        unit="%",
        min_value=85.0,
        category="detection",
        severity="hard",
        notes="Must distinguish deer/hogs from humans, livestock, vehicles.",
    ),
    Constraint(
        name="false_positive_rate",
        description="Maximum false positive rate",
        unit="%",
        max_value=10.0,
        category="detection",
        severity="hard",
        notes="Farmer tolerance for nuisance activations. <5% preferred.",
    ),

    # Deterrent Effectiveness
    Constraint(
        name="anti_habituation_months",
        description="Minimum months of sustained deterrent effectiveness",
        unit="months",
        min_value=4.0,
        category="deterrent",
        severity="hard",
        notes="Must last one full growing season (4-6 months) without performance decay.",
    ),
    Constraint(
        name="human_safety",
        description="Human safety rating (0=harmful, 10=completely safe)",
        unit="score",
        min_value=9.0,
        category="deterrent",
        severity="hard",
        notes="Must never injure people. Score 9+ required (minor startle acceptable).",
    ),
    Constraint(
        name="livestock_safety",
        description="Livestock safety rating (0=harmful, 10=completely safe)",
        unit="score",
        min_value=8.0,
        category="deterrent",
        severity="hard",
        notes="Must not harm or unduly stress farm animals.",
    ),

    # Maintenance & Operations
    Constraint(
        name="maintenance_visits_per_year",
        description="Maximum maintenance visits per year per 50-acre block",
        unit="visits/year",
        max_value=4.0,
        category="operations",
        severity="soft",
        notes="Quarterly maximum. Farmers are busy during growing season.",
    ),
    Constraint(
        name="system_lifetime",
        description="Minimum system operational lifetime",
        unit="years",
        min_value=5.0,
        category="operations",
        severity="hard",
        notes="Required for amortization model. 5-year minimum.",
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
            elif c.min_value is not None and c.min_value != 0:
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
        "Target: $100/acre/year | 50-acre blocks | Scalable",
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

    # Per-acre cost check (derived)
    capex = next((r for r in results if r.constraint_name == "capital_cost_50acre" and r.proposed_value), None)
    opex = next((r for r in results if r.constraint_name == "annual_operating_cost" and r.proposed_value), None)
    lifetime = next((r for r in results if r.constraint_name == "system_lifetime" and r.proposed_value), None)

    if capex and opex and lifetime and lifetime.proposed_value > 0:
        annual_total = (capex.proposed_value / lifetime.proposed_value) + opex.proposed_value
        per_acre = annual_total / 50.0
        status_icon = "✅" if per_acre <= 100 else "❌"
        lines.append(f"\n--- DERIVED: PER-ACRE ECONOMICS ---")
        lines.append(f"  Capex amortized: ${capex.proposed_value / lifetime.proposed_value:,.0f}/year")
        lines.append(f"  + Opex: ${opex.proposed_value:,.0f}/year")
        lines.append(f"  = Total annual: ${annual_total:,.0f}/year for 50 acres")
        lines.append(f"  {status_icon} Per-acre cost: ${per_acre:,.0f}/acre/year (target: ≤$100)")

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
        "FIELD SHIELD CONSTRAINTS — NOVEL CONCEPT RESEARCH (v2)",
        "Target: $100/acre/year | 50-acre blocks | Scalable | Anti-habituation",
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
Field Shield Constraint Validator (v2 — Novel Concept Research)
================================================================

Commands:
  constraints       Show all constraints with limits and notes
  template          Output a blank JSON template for proposals
  check <file.json> Validate a proposal from a JSON file
  validate          Interactive validation mode

Target: $100/acre/year | 50-acre blocks | Scalable | Anti-habituation

Example JSON:
  {
    "cost_per_acre_year": 85.0,
    "block_size": 50.0,
    "capital_cost_50acre": 12000.0,
    "annual_operating_cost": 1500.0,
    "coverage_completeness": 95.0,
    "anti_habituation_months": 6.0,
    "system_lifetime": 5.0
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
