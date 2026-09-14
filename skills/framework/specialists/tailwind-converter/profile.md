# Specialist: tailwind-converter

Owns Tailwind CSS to SIMAI Framework conversion strategy, mapping quality, and conversion reports.

Learning plan:

- follow `roadmap/tailwind-to-framework-learning-plan.md` when developing this specialty from basic utility mapping to complex project migration and smart-component conversion.

Use when:

- user wants to convert Tailwind-based markup or project screens to SIMAI Framework;
- Tailwind UI or Tailwind Plus examples are used as source material for SIMAI Framework examples;
- a migration requires class-level mapping, component recognition, or unmapped token reporting.

Focus:

- preserve semantic HTML and useful interaction hooks;
- map only known Tailwind patterns to verified SIMAI Framework utilities or components;
- escalate unmapped classes and behavior gaps instead of guessing;
- keep licensing-sensitive third-party examples as source material, not automatically copied deliverables.

Gate bias:

- conversion output must pass SIMAI Framework strict validation when intended as SIMAI Framework-ready markup;
- conversion reports must list unmapped classes and assumptions;
- source snippets from commercial libraries require explicit license review before redistribution.
