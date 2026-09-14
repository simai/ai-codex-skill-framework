# UX Implementation Contract

Use this reference when `$framework` implements an interface designed or reviewed by `$ux`.

## Rule

Do not treat `$ux` output as generic layout advice. Convert it into SIMAI Framework layer, component, smart-component, block, recipe, and validation contracts.

## Required Mapping

- `Scenario`: user, primary action, success state.
- `Layer mapping`: utilities, components, smart-components, blocks, page recipe.
- `Component contract`: props, slots, events, visual states, validation states.
- `Smart-component contract`: data loading, persistence, permissions, side effects, state orchestration.
- `Recipe/pattern`: page recipe and pattern playbooks to use before custom composition.
- `State contract`: empty, loading, error, success, disabled, partial.
- `Validation`: SIMAI Framework catalog/manifest checks, recipe checks, local browser/screenshot checks.
- `Acceptance`: `$tester` usability gate, responsive checks, focus/keyboard where interactive.

## Output Back To `$ux`

If SIMAI Framework constraints change the design, report:

```markdown
UX deviation:
SIMAI Framework layer/component reason:
Alternative:
Retest point:
```
