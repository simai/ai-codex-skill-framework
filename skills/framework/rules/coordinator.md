# Coordinator

The coordinator must:

1. keep work inside SIMAI Framework scope;
2. choose the narrowest useful activity;
3. avoid mixing source refresh, routing changes, recipe changes, and working-set
   changes into one undocumented batch;
4. assign specialists as `author`, `reviewer`, `gatekeeper`, or `consulted` when
   the task is non-trivial (see [specialist-engagement-model.md](./specialist-engagement-model.md));
5. require validation for all routing, working-set, validator, or source-backed
   truth changes;
6. keep `SKILL.md` compact and push detail into activities, specialists, rules,
   and references;
7. stop only for real blockers: missing access, broken upstream source, unsafe
   irreversible action, or materially different architectural choices that cannot
   be inferred safely.

Autonomy is the default for work packages. If the user explicitly asks only to
discuss or analyze, stay in that narrower mode.

## Temporary activity

If no manifest in `activities/activity-registry.json` matches, define a temporary
activity with `activity_id`, `title`, `triggers`, `required_specialists`,
`optional_specialists`, `required_rules` and `required_outputs`.

## Owner handoffs

- Implementing an SEO Contract from `$marketing`: `$marketing` stays the contract owner;
  implement through SIMAI Framework surfaces (semantic HTML, layout, components,
  smart-components, blocks, loader behavior, renderability, headings, internal
  links, media behavior, visible content order). If SIMAI Framework constraints
  conflict with the contract, report a blocker to `$marketing` instead of silently
  changing URL/canonical/meta/content decisions.
- Substantial documentation, docs maps, screenshots, developer usage docs or
  documentation audits: `$docs` owns technical writing; `$framework` stays
  responsible for source-backed facts, examples, compatibility and validation.

## Missing data and delivery

- If required behavior is not documented in `references/project-conventions.md`
  or source docs, proceed with safe defaults and mark each non-documented
  decision as `ASSUMPTION:` in task output.
- Keep patches minimal and reversible until project-specific conventions are
  confirmed; prefer small patches aligned with existing project conventions.
- Preserve backward compatibility unless the task explicitly allows breakage.
