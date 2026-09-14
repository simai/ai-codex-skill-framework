# Knowledge Pack: Tailwind CSS to SIMAI Framework Conversion

Use this pack when the activity is `tailwind-conversion`.

Focus:

- converting Tailwind utility-heavy markup into SIMAI Framework-safe markup;
- using Tailwind UI examples as inspiration or source input for SIMAI Framework examples;
- preserving semantic structure while replacing styling and component contracts.

Default artifacts:

- `specialists/tailwind-converter/profile.md`
- `roadmap/tailwind-to-framework-learning-plan.md`
- `roadmap/tailwind-to-framework-stage-1-2-tz.md`
- `roadmap/future-specialties-and-tailwind-conversion.md`
- `references/vendor/tailwind-to-framework.class-groups.json`
- `references/vendor/tailwind-to-framework.utility-map.json`
- `references/vendor/tailwind-to-framework.fixtures.json`
- `references/vendor/tailwind-to-framework.component-hints.json`
- `references/vendor/tailwind-to-framework.component-recipes.json`
- `references/vendor/tailwind-to-framework.component-renderers.json`
- `references/vendor/tailwind-to-framework.smart-hints.json`
- `references/vendor/component-smart-catalog.json`
- `references/vendor/tailwind-to-framework.inventory-source.html`
- `references/component-smart-catalog.md`
- `references/tailwind-to-framework-e2e-examples.md`
- `references/tailwind-to-framework-e2e-toolbar-example.md`
- `scripts/convert_tailwind_to_framework.py`
- `scripts/capture_html_screenshot.py`
- `scripts/probe_html_runtime.py`
- `scripts/run_tailwind_conversion_lab.py`
- `scripts/run_tailadmin_page_examples.py`
- `scripts/build_component_smart_catalog.py`
- `scripts/score_lab_visual.py`
- `scripts/validate_tailwind_mapping_artifacts.py`
- `scripts/validate_tailwind_converter.py`

Learning route:

- use `roadmap/tailwind-to-framework-learning-plan.md` as the staged development plan for this specialist;
- move from utility taxonomy and direct class mapping to responsive/state handling, component recognition, smart-component recognition, full project migration, and converter tooling;
- each stage must leave a reusable artifact: mapping manifest, fixture, recipe, validator, or conversion report template.

Conversion policy:

- map known Tailwind utilities to verified SIMAI Framework utilities only when the target class exists in vendor data;
- prefer SIMAI Framework components or smart-components when a source block clearly matches an SIMAI Framework component family;
- preserve `aria-*`, form semantics, links, buttons, and useful data hooks;
- remove Tailwind-only state/group syntax only when the equivalent SIMAI Framework state or component behavior is defined;
- produce a report for unmapped classes, behavior assumptions, and manual design QA needs.

Converter usage:

- use `scripts/convert_tailwind_to_framework.py "<class string>"` for class-string conversion;
- use `scripts/convert_tailwind_to_framework.py --html-string '<div class="..."></div>'` for HTML snippet conversion;
- add `--render-recipe --format text` to print the first detected recipe starter markup;
- add `--render-recipe <recipe-id> --format json` to request a specific recipe and keep the full conversion report.
- add `--render-component --format text` to print source-backed component starter markup for the first detected component recipe;
- concrete component renderers currently cover `button`, `dropdown`, `input`, `pagination`, and `modal`; treat their output as starter markup with manual behavior checks, not as a blind replacement;
- add `--render-smart <smart-id-or-sf-code> --format json` to print an advisory smart starter, registry match, source refs, and manual checks;
- read `report.validationHints` before marking converted output as SIMAI Framework-ready;
- read `report.smartHints` as advisory only; do not insert `sf-code` automatically without confirming behavior.
- use `--gate-tailwind-residue` when output is expected to be SIMAI Framework-ready;
- use `--inventory <file-or-dir>` to scan real Tailwind-heavy projects before migration.
- inventory mode counts only files with Tailwind-specific evidence and ignores SIMAI Framework-native vendor catalog classes, so SIMAI Framework source mirrors should not be treated as Tailwind projects.
- use `scripts/run_tailwind_conversion_lab.py` to generate an ignored visual/QA lab under `output/tailwind-to-framework-lab/` with original source-inspired snippets, raw conversion reports, finished SIMAI Framework snippets, inventory, and strict validation evidence.
- use `scripts/run_tailadmin_page_examples.py` to generate ignored TailAdmin page examples under `output/tailwind-to-framework-tailadmin-pages/` from the local MIT-licensed TailAdmin clone, including source excerpt, raw conversion report, finished SIMAI Framework markup, screenshot, and visual score per page.
- TailAdmin page examples also generate `framework-componentized.html` and `componentized-index.html` per page; use these to compare source-backed component/smart replacements against the manually finished SIMAI Framework variant before promoting componentized output.
- TailAdmin page examples also generate `runtime-index.html`, `runtime-screenshot.png`, `runtime-visual-score.json`, and `runtime-probe.json`; use these to verify real source-backed custom elements before promoting `sf-button`, `sf-input`, `sf-pagination`, or `sf-modal` into final output.
- treat `runtimePromotionStatus: candidate` as the only automatic promotion candidate state; `blocked` means the runtime asset or behavior contract is not yet source-backed.
- runtime component previews currently cover `sf-dropdown`, `sf-pagination`, and `sf-modal` under `output/tailwind-to-framework-tailadmin-pages/runtime-components/`.
- `sf-pagination` promotion is source-backed only for the full SIMAI Framework pagination contract: selected count, numeric page list, page-size control, last-page control, and explicit `current`/`total`. Compact previous/next-only pagers should stay as static markup or a manual recipe until a separate compact contract exists.
- Do not compare pagination against handcrafted approximations. The runtime lab must record the exact ui-play source path, load source-backed component CSS, and keep promotion blocked when the real source/runtime preview is visually broken or clipped.
- `sf-code="table"` is currently registry-only in the source mirror: use static semantic `<table class="table ...">` utilities for SIMAI Framework-ready output, and keep smart-table auto-promotion blocked until a real `ui-smart` runtime/data contract is found.
- use `scripts/build_component_smart_catalog.py` after source sync to refresh the source-backed component/smart-component catalog used by component and smart rendering decisions.
- use `scripts/capture_html_screenshot.py <html> --output <png>` as a local Chrome/Chromium screenshot fallback when browser-use screenshot capture times out.
- use `scripts/probe_html_runtime.py <html> --output <json>` to verify that runtime-aware preview pages actually define expected custom elements through real JS assets, not CSS fallbacks.
- use `scripts/score_lab_visual.py <png>` for a lightweight screenshot-based source/SIMAI Framework similarity score; it now fails on near-black, blank, or zero-variance screenshots so loader/empty-page captures cannot produce a false high score.
- when using `--render-component`, pass `--runtime-promotion-status`, `--runtime-visual-delta`, and `--max-runtime-visual-delta` to get a converter-level `promotionGate`; without those runtime inputs the gate must stay blocked.

Source policy:

- project-owned Tailwind markup can be converted directly;
- third-party examples can be analyzed and transformed into original SIMAI Framework examples;
- Tailwind Plus examples require licensing review before copying source markup into distributable artifacts.

Minimum verification:

- converted output passes `validate_framework_html_files.py --strict --catalog-strict` when it is marked as SIMAI Framework-ready;
- unmapped Tailwind classes are reported;
- component substitutions are traceable to SIMAI Framework source docs, shipped components, or `ui-play` examples;
- runtime-backed component substitutions have a passing `runtime-probe.json` and an acceptable visual delta before final promotion;
- converter `promotionGate.ok` is required before promoting source-backed custom elements into final output; gate pass still means candidate, not final acceptance.
- promotion gate regression fixtures must cover all decision branches: `candidate`, `blocked-by-runtime`, `blocked-by-visual-delta`, and `blocked-by-missing-checklist`.
- any copied external source material has a documented license status.

Future implementation batches:

1. Add source-backed recipes that can consume converted examples into working-set sections.
2. Add real project migration reports from representative Tailwind-heavy repositories.
3. Add stricter residue patterns as real Tailwind examples reveal gaps.
4. Add source-backed SIMAI Framework examples from Tailwind Plus/Application UI inspiration after license review.
