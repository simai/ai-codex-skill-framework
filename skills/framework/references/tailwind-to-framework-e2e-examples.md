# Tailwind to SIMAI Framework E2E Examples

These examples are original Tailwind-inspired fixtures for the converter pipeline. They are not copied from Tailwind Plus source.

## Covered Examples

- `auth-form`: `references/vendor/tailwind-to-framework.e2e-auth.framework.html`
- `card`: `references/vendor/tailwind-to-framework.e2e-card.framework.html`
- `data-table`: `references/vendor/tailwind-to-framework.e2e-table.framework.html`
- `toolbar`: `references/vendor/tailwind-to-framework.e2e-toolbar.framework.html`

## Validation

```bash
python3 skills/framework/scripts/validate_framework_html_files.py \
  --strict \
  --catalog-strict \
  skills/framework/references/vendor/tailwind-to-framework.e2e-auth.framework.html \
  skills/framework/references/vendor/tailwind-to-framework.e2e-card.framework.html \
  skills/framework/references/vendor/tailwind-to-framework.e2e-table.framework.html \
  skills/framework/references/vendor/tailwind-to-framework.e2e-toolbar.framework.html
```

## Current Pipeline

1. Convert safe utility classes with `convert_tailwind_to_framework.py`.
2. Read `report.validationHints` before marking output SIMAI Framework-ready.
3. Use `report.componentRecipes` for starter SIMAI Framework structure.
4. Treat `report.smartHints` as advisory until behavior is confirmed.
5. Validate final SIMAI Framework snippets with strict catalog validation.

## Next Practical Use

Use Tailwind Plus/Application UI blocks as source inspiration only after license review. Convert the pattern into an original SIMAI Framework example, then validate it through this pipeline.
