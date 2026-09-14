# SIMAI Framewok 5 Skill

Codex skill for SIMAI Framework (SIMAI Framework):
- coordinator-driven skill architecture with activities, specialists, and gatekeeping
- frontend-first architecture work (`core`, `loader`, `utilities`, `components`, `smart-components`, `blocks`)
- Tailwind CSS to SIMAI Framework conversion planning and specialist ownership
- page layout scaffolding and recipe routing
- unified task routing from request -> scenario -> recipe -> pattern playbooks
- vendor-strict class/state/smart validation
- real template validation for HTML/PHP snippets
- staged backend planning references for Bitrix and Laravel

Repository layout:
- `skills/framework/SKILL.md`
- `skills/framework/kernel/`
- `skills/framework/rules/`
- `skills/framework/activities/`
- `skills/framework/specialists/`
- `skills/framework/quality/`
- `skills/framework/knowledge-packs/`
- `skills/framework/agents/openai.yaml`
- `skills/framework/references/`
- `skills/framework/references/vendor/`
- `skills/framework/scripts/`
- `source/simai/` (ignored local mirror of upstream SIMAI Framework repositories)
- `.github/workflows/framework-skill-checks.yml`
- root files: `README.md`, `.gitattributes`, `.git/`

Install target:
- macOS/Linux: `~/.codex/skills/framework`
- Windows: `%USERPROFILE%\.codex\skills\framework`

## 1) Install (macOS/Linux)

Copy:

```bash
SRC="/path/to/ai-codex-skill-framework/skills/framework"
DST="$HOME/.codex/skills/framework"
mkdir -p "$HOME/.codex/skills"
rm -rf "$DST"
cp -R "$SRC" "$DST"
```

Symlink (recommended for active development):

```bash
SRC="/path/to/ai-codex-skill-framework/skills/framework"
DST="$HOME/.codex/skills/framework"
mkdir -p "$HOME/.codex/skills"
rm -rf "$DST"
ln -s "$SRC" "$DST"
```

## 2) Install (Windows, PowerShell)

Copy:

```powershell
$src = "C:\path\to\ai-codex-skill-framework\skills\framework"
$dstRoot = "$env:USERPROFILE\.codex\skills"
$dst = "$dstRoot\framework"
New-Item -ItemType Directory -Force $dstRoot | Out-Null
if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
Copy-Item -Recurse -Force $src $dst
```

Symlink (recommended for active development, may require admin/developer mode):

```powershell
$src = "C:\path\to\ai-codex-skill-framework\skills\framework"
$dstRoot = "$env:USERPROFILE\.codex\skills"
$dst = "$dstRoot\framework"
New-Item -ItemType Directory -Force $dstRoot | Out-Null
if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
New-Item -ItemType SymbolicLink -Path $dst -Target $src
```

## 3) Restart Codex

After install or update, restart Codex so skills are reloaded.

## 4) Verify install

Expected files:
- `~/.codex/skills/framework/SKILL.md`
- `~/.codex/skills/framework/references/`
- `~/.codex/skills/framework/references/vendor/`
- `~/.codex/skills/framework/scripts/`
- `~/.codex/skills/framework/agents/openai.yaml`

Quick check:

```bash
ls -la ~/.codex/skills/framework
python3 ~/.codex/skills/framework/scripts/run_local_checks.sh
python3 ~/.codex/skills/framework/scripts/generate_page_scaffold.py --type landing --snippet-only
python3 ~/.codex/skills/framework/scripts/generate_component_scaffold.py --kind smart --smart-code cards --snippet-only
```

Windows:

```powershell
Get-ChildItem "$env:USERPROFILE\.codex\skills\framework"
```

## 5) How to use in prompts

The skill now works best as a coordinator:
- it selects an activity such as source refresh, routing maintenance, working-set maintenance, validation hardening, or skill architecture update
- it engages the minimum relevant specialists instead of treating SIMAI Framework as one monolithic expert
- it keeps source sync, routing, scaffold generation, working-set extraction, validation, and docs in separate responsibility zones

Call explicitly:

```text
$framework Build landing page skeleton with hero, benefits, CTA, and footer in vendor-safe classes
$framework Refactor current SIMAI Framework layout from flex to grid while preserving behavior
$framework Validate page recipes in strict vendor mode and report unknown classes
$framework Generate smart-component scaffold for cards with sf-code mapping
$framework Review loader init flow and check cache/idempotency risks
```

## 6) Local development checks

Run all checks:

```bash
bash skills/framework/scripts/run_local_checks.sh
```

Sync upstream SIMAI Framework source mirrors:

```bash
python3 skills/framework/scripts/sync_source_repos.py
```

Machine-readable source-refresh entrypoints:

```bash
python3 skills/framework/scripts/sync_source_repos.py --format json
python3 skills/framework/scripts/build_source_inventory.py \
  --repo-root "$PWD" \
  --skill-root "$PWD/skills/framework" \
  --format json
```

Rebuild docs atlas from synced `ui-doc`:

```bash
python3 skills/framework/scripts/build_ui_doc_atlas.py \
  --docs-root "$PWD/source/simai/ui-doc/source/docs/ru" \
  --skill-root "$PWD/skills/framework"
```

Top-level task route:

```bash
python3 skills/framework/scripts/recommend_framework_route.py "profile settings page with avatar upload and notification toggles"
```

Coordinator activity route:

```bash
python3 skills/framework/scripts/recommend_framework_activity.py \
  "working set сломан после обновления ui-play, нужно поправить upstream extracts и manifest"
```

Machine-readable route:

```bash
python3 skills/framework/scripts/recommend_framework_route.py \
  "checkout page with customer form, delivery, payment and summary" \
  --format json
```

Lower-level machine-readable routers with coordinator hints:

```bash
python3 skills/framework/scripts/recommend_page_recipe.py \
  --manifest skills/framework/references/ui-doc-manifest.json \
  --format json \
  "profile settings page with avatar upload and notification toggles"
python3 skills/framework/scripts/recommend_product_scenario.py \
  --format json \
  "profile settings page with avatar upload and notification toggles"
python3 skills/framework/scripts/recommend_ui_pattern.py \
  --format json \
  "checkout page with customer form, delivery, payment and summary"
python3 skills/framework/scripts/generate_page_scaffold.py \
  --type profile --snippet-only --format json
python3 skills/framework/scripts/generate_component_scaffold.py \
  --kind smart --smart-code cards --snippet-only --format json
```

Validate route regressions:

```bash
python3 skills/framework/scripts/validate_route_fixtures.py
```

Validate activity regressions:

```bash
python3 skills/framework/scripts/validate_activity_fixtures.py
```

Validate coordinator contracts:

```bash
python3 skills/framework/scripts/validate_activity_manifests.py
python3 skills/framework/scripts/validate_source_refresh_contract.py
python3 skills/framework/scripts/validate_source_refresh_gate.py
python3 skills/framework/scripts/validate_tailwind_conversion_contract.py
python3 skills/framework/scripts/validate_validation_contract.py
python3 skills/framework/scripts/validate_validation_hardening_gate.py
python3 skills/framework/scripts/validate_router_hints.py
python3 skills/framework/scripts/validate_scaffold_hints.py
```

Validate end-to-end route-to-bundle regressions:

```bash
python3 skills/framework/scripts/validate_e2e_fixtures.py
```

Prepare a working task bundle:

```bash
python3 skills/framework/scripts/prepare_framework_task.py \
  "profile settings page with avatar upload and notification toggles" \
  --scaffold-out /tmp/profile-settings.html
```

Generate a ready working directory:

```bash
python3 skills/framework/scripts/generate_framework_working_set.py \
  "dashboard with KPI cards, activity table and filters" \
  --out-dir /tmp/framework-dashboard-working-set
```

The generated working set can include `sections/*.html` snippets for quick block-level replacement.
It also includes `sources.md` so each generated section can be traced back to upstream `ui-play` or `ui-doc`.
For supported section types it can also include `upstream/*.html` with normalized snippets extracted from real upstream examples.
Upstream extraction now supports single-block selectors, `range` extracts for adjacent multi-block fragments, and `ancestor` extracts for stable parent containers around a child component.
The working set coverage itself is now data-driven via `skills/framework/references/vendor/working-set.section-variants.json`.
Current section/extraction coverage can be inspected in `skills/framework/references/working-set-coverage.md`.

Install pre-commit hook (runs checks only when `skills/framework` changes are staged):

```bash
bash skills/framework/scripts/install_pre_commit_hook.sh
```

Validate real templates/snippets:

```bash
python3 skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict /path/to/template.html
python3 skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict \
  --glob "/path/to/templates/**/*.html" \
  --glob "/path/to/templates/**/*.php"
```

## 7) Update workflow

1. Update skill files under `skills/framework/`.
2. Sync upstream mirrors with `python3 skills/framework/scripts/sync_source_repos.py`.
3. Rebuild atlas if docs changed.
4. Run `bash skills/framework/scripts/run_local_checks.sh`.
5. Restart Codex (or reopen session).
6. Verify trigger via prompt with `$framework`.

## 8) Daily Workflow

For a concrete SIMAI Framework page task:

1. Start from `skills/framework/SKILL.md` and let the coordinator choose the activity and specialist set.
2. For page-level work, route the task with `python3 skills/framework/scripts/recommend_framework_route.py "<task>"`.
3. If the task is ready to start, prepare the bundle with `python3 skills/framework/scripts/prepare_framework_task.py "<task>" --scaffold-out /tmp/page.html`.
4. Read the suggested scenario doc, page recipe, and pattern playbooks from the prepared output.
5. Adapt the scaffold or working set to the target project.
6. Validate with `python3 skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict <file>`.
7. Run `bash skills/framework/scripts/run_local_checks.sh` before delivery.
