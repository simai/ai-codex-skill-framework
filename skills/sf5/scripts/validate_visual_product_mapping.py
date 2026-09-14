#!/usr/bin/env python3
"""Fail closed when an SF5 visual delivery bypasses inventory or platform mapping."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("mapping"); p.add_argument("--json",action="store_true"); a=p.parse_args(); issues=[]
    try:d=json.loads(Path(a.mapping).read_text(encoding="utf-8-sig"))
    except (OSError,json.JSONDecodeError) as exc:d={}; issues.append(f"mapping_unreadable:{exc}")
    for key in ("platform","platform_version","inventory_ref","selected_layer","selected_capability_ref","visual_grammar_ref","candidate_identity"):
        if not d.get(key): issues.append(f"required_field_missing:{key}")
    if str(d.get("platform") or "").lower() != "sf5": issues.append("sf5_platform_required")
    if d.get("delivery_kind") == "standalone_html": issues.append("standalone_html_for_sf5_forbidden")
    if d.get("creates_new") and not d.get("no_fit"):
        issues.append("new_capability_without_no_fit")
    if d.get("creates_new") and not (d.get("tests") and d.get("documentation_ref") and d.get("compatibility_boundary")):
        issues.append("new_capability_evidence_incomplete")
    if d.get("unmapped_visual_literals"): issues.append("visual_literals_not_mapped")
    result={"status":"fail" if issues else "success","issues":sorted(set(issues))}
    print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else ("PASS" if not issues else "FAIL: "+", ".join(result["issues"])))
    return 1 if issues else 0
if __name__=="__main__": raise SystemExit(main())
