#!/usr/bin/env python3
"""Validate the executable SIMAI Framework Component design/evolution technology."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "technologies" / "component-design-evolution.json"
FIXTURES = ROOT / "quality" / "component-design-evolution-fixtures.json"
REFERENCE = ROOT / "references" / "component-design-evolution.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    contract = load(CONTRACT)
    fixtures = load(FIXTURES)

    required_operations = [
        "operation.discover", "operation.design", "operation.compare",
        "operation.implement_component", "operation.project_smart",
        "operation.document", "operation.accept",
    ]
    operations = contract.get("operations", [])
    stages = [item.get("id") for item in operations]
    if stages != required_operations:
        failures.append(f"operation order mismatch: {stages!r}")
    operation_ids = set(stages)
    for operation in operations:
        for field in ("input_refs", "output_refs", "check_refs", "stop_condition_refs", "source_refs"):
            if field != "stop_condition_refs" and not operation.get(field):
                failures.append(f"{operation.get('id')}: {field} is empty")
        for prerequisite in operation.get("prerequisites", []):
            if prerequisite not in operation_ids:
                failures.append(f"{operation.get('id')}: unknown prerequisite {prerequisite}")
    scenarios = contract.get("scenarios", [])
    expected_scenarios = {
        "scenario.create_component", "scenario.evolve_component",
        "scenario.create_smart_projection", "scenario.evolve_component_and_smart_projection",
    }
    if {item.get("id") for item in scenarios} != expected_scenarios:
        failures.append("scenario set mismatch")
    for scenario in scenarios:
        unknown = [item for item in scenario.get("operation_ids", []) if item not in operation_ids]
        if unknown:
            failures.append(f"{scenario.get('id')}: unknown operations {unknown}")
        if "operation.accept" not in scenario.get("operation_ids", []):
            failures.append(f"{scenario.get('id')}: must end with acceptance")

    required_evidence = {
        "component_brief", "scenario_matrix", "target_contract", "gap_matrix",
        "token_map_and_design_literal_audit", "surface_geometry_matrix",
        "component_structure_map",
        "public_data_attribute_contract",
        "state_geometry_matrix",
        "focus_contract",
        "indicator_semantics_contract_when_applicable",
        "base_component_verification", "smart_projection_decision",
        "documentation_and_machine_contract",
        "browser_accessibility_responsive_theme_evidence",
        "technology_quality_feedback",
    }
    evidence = {
        ref.removeprefix("evidence.")
        for operation in operations
        for ref in operation.get("output_refs", [])
    }
    missing = sorted(required_evidence - evidence)
    if missing:
        failures.append(f"missing evidence: {', '.join(missing)}")

    if contract.get("id") != "technology.framework.component-design-evolution":
        failures.append("id must be technology.framework.component-design-evolution")
    if contract.get("owner") != "skill.framework":
        failures.append("owner must be skill.framework")
    if contract.get("parent_process_model_id") != "framework_frontend_delivery":
        failures.append("parent_process_model_id must reuse framework_frontend_delivery")
    if contract.get("lifecycle_curator_skill") != "teamlead":
        failures.append("lifecycle_curator_skill must be teamlead")
    if contract.get("canonical_write_allowed") is not False:
        failures.append("canonical_write_allowed must be false")
    if contract.get("owner_review_required") is not True:
        failures.append("owner_review_required must be true")
    if contract.get("technology_quality_feedback_policy", {}).get("required") is not True:
        failures.append("technology quality feedback must be required")

    reference = REFERENCE.read_text(encoding="utf-8")
    required_reference_contracts = {
        "token hierarchy": "#### Иерархия токенов и запрет случайных литералов",
        "component semantic token": "локальный семантический токен Component",
        "raw literal policy": "Raw `px`, `rem`, `em`, hex/RGB",
        "control radius zone": "`--sf-radius--ui`",
        "surface radius zone": "`--sf-radius-default`",
        "nested surface scale": "`space-4` сочетается с `radius-4`",
        "bem responsibility": "#### Структура Component по БЭМ-семантике",
        "element promotion": "Element становится отдельным Block/Component",
        "public data attributes": "#### Публичные `data-*`-атрибуты",
        "short data grammar": "Основная грамматика — `data-<property>=\"<value>\"`",
        "one property per data attribute": "Один атрибут описывает одно независимое свойство",
        "native state priority": "Нативный HTML и ARIA имеют приоритет над `data-*`",
        "focus ownership": "Focus owner — фактический воспринимаемый control",
        "focus modality": "показывает авторский focus indicator через\n  `:focus-visible`",
        "joined focus geometry": "`--sf-ui-focus-inset`",
        "compound focus wrapper": "`:has(:focus-visible)`",
        "focus within restriction": "`:focus-within` не является достаточным условием",
        "forced colors": "forced-colors/high-contrast",
    }
    for label, needle in required_reference_contracts.items():
        if needle not in reference:
            failures.append(f"reference misses {label}: {needle}")

    cases = fixtures.get("cases", [])
    kinds = {case.get("kind") for case in cases}
    if kinds != {"component", "smart_component"}:
        failures.append("fixtures must cover component and smart_component")
    for case in cases:
        if not case.get("required_scenarios"):
            failures.append(f"{case.get('id')}: required_scenarios is empty")
        if not case.get("required_decisions"):
            failures.append(f"{case.get('id')}: required_decisions is empty")
        if case.get("smart_projection") not in {"implemented", "not_needed", "deferred"}:
            failures.append(f"{case.get('id')}: invalid smart_projection")

    component_case = next((case for case in cases if case.get("kind") == "component"), {})
    component_decisions = set(component_case.get("required_decisions", []))
    required_component_decisions = {
        "token_hierarchy", "surface_geometry", "bem_structure",
        "public_data_attribute_contract", "focus_contract",
    }
    if missing_decisions := sorted(required_component_decisions - component_decisions):
        failures.append(f"component fixture misses decisions: {', '.join(missing_decisions)}")

    smart_case = next((case for case in cases if case.get("kind") == "smart_component"), {})
    smart_decisions = set(smart_case.get("required_decisions", []))
    required_smart_decisions = {
        "token_hierarchy_inherited", "surface_geometry_inherited",
        "bem_structure_projection", "public_data_attribute_contract_inherited",
        "focus_contract_inherited",
    }
    if missing_decisions := sorted(required_smart_decisions - smart_decisions):
        failures.append(f"smart fixture misses decisions: {', '.join(missing_decisions)}")

    payload = {
        "ok": not failures,
        "technology_id": contract.get("id"),
        "operation_count": len(stages),
        "fixture_count": len(cases),
        "failures": failures,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
