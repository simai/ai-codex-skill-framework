# SIMAI Framework Roadmap: Future Specialties and Tailwind Conversion

This roadmap captures useful follow-up work that should not be mixed into current implementation batches.

## Coordinator Maturity

- Run several real SIMAI Framework tasks through the coordinator, working-set, and validation flow.
- Use those field tests to prune weak fixtures and add practical route cases.
- Keep expanding specialist/activity context only when a new surface has stable ownership and its own validation path.

## Candidate Specialist Expansion

- `loader-runtime`: SIMAI Framework loader, boot order, idempotency, cache behavior, runtime init contracts.
- `utilities-catalog`: utility groups, tokens, vendor-safe class policy, docs-to-class mapping.
- `components-catalog`: shipped presentational components, source examples, component reuse rules.
- `smart-components-catalog`: `ui-smart`, `sf-code`, smart props/events/contracts, smart examples.
- `playground-examples`: `ui-play` examples, drift detection, source-backed snippet quality.
- `bundle-contract`: working-set manifest, sections, source refs, upstream extracts.
- `regression-architect`: fixture strategy, gate validators, machine-readable contracts.

## Tailwind CSS to SIMAI Framework Converter

Detailed learning plan:

- `roadmap/tailwind-to-framework-learning-plan.md`
- Stage 1-2 executable TZ: `roadmap/tailwind-to-framework-stage-1-2-tz.md`

Goal:

- make migration from Tailwind-heavy markup to SIMAI Framework utilities/components repeatable;
- reuse accumulated Tailwind UI examples as source material for SIMAI Framework examples;
- support controlled conversion of current projects into the SIMAI Framework design/runtime system.

Initial scope:

- convert class-level Tailwind utility patterns into SIMAI Framework utility equivalents where a known mapping exists;
- preserve semantic HTML and interaction hooks;
- flag unmapped classes and design decisions instead of guessing;
- prefer SIMAI Framework components and smart-components when a Tailwind block clearly represents a known SIMAI Framework component family;
- produce conversion reports with assumptions, unmapped tokens, and recommended follow-up checks.

Primary source candidates:

- existing project markup that uses Tailwind CSS;
- Tailwind Plus Application UI examples as inspiration/source material, subject to licensing and manual review;
- SIMAI Framework source mirrors and docs as the target truth.

Not in first scope:

- blindly copying commercial Tailwind Plus examples into distributable SIMAI Framework examples without license review;
- pixel-perfect conversion without an explicit design QA pass;
- automatic JS behavior migration from arbitrary Tailwind/headless examples;
- project-specific backend integration.

Suggested first batches:

1. Add `tailwind-converter` specialist and `tailwind-conversion` activity.
2. Build a vendor mapping manifest for common Tailwind -> SIMAI Framework class groups.
3. Add fixtures for known layouts: utility card, form row, toolbar, behavior-adjacent negative cases.
4. Add a converter script that accepts HTML and emits SIMAI Framework HTML plus a conversion report.
5. Add validation gates: SIMAI Framework strict class validation plus unmapped Tailwind report thresholds.
