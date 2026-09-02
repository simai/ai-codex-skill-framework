# Change Gates

Use these gates when the task changes one of the critical SF5 coordinator surfaces.

## Source Refresh Gate

Apply when the batch touches upstream mirrors, `source/simai/*`, source-backed inventory, or mirrored example paths.

Required before `approved`:

- verify that new upstream paths really exist in the local mirror;
- rebuild source-backed artifacts that depend on the changed mirrors;
- update source-backed references when paths or coverage changed;
- run the relevant regression or local checks after the refresh.

Do not close the batch if mirror refresh changed source structure but left stale manifests or stale docs behind.

## Working-Set Gate

Apply when the batch touches:

- `generate_sf5_working_set.py`
- `working-set.section-variants.json`
- section snippets
- upstream extracts
- working-set manifest contract

Required before `approved`:

- verify that every changed `source_ref` and upstream extract path exists;
- generate at least one real working set for the touched recipe or scenario;
- confirm that generated bundle files and manifest fields still match contract;
- run e2e and local checks when extraction or manifest logic changed.

Do not close the batch if generated snippets exist only synthetically while upstream source-backed snippets are now broken.

## Validation Hardening Gate

Apply when the batch touches validators, fixture sets, smoke checks, or bundle assertions.

Required before `approved`:

- add or update the narrowest fixture set that proves the behavior;
- run the specific validator directly before relying on the full local suite;
- keep validator output machine-readable where fixtures depend on it;
- update docs only after the new validator contract is confirmed green.

Do not close the batch if validation logic changed but there is no regression proof for the new behavior.

## Component Design Evolution Gate

Apply when creating a Component, changing its public scenarios/variants, or
adding/changing a Smart Component projection.

Required before `approved`:

- authoritative source, registry/manifests, tests, distribution and current
  documentation were inspected;
- component brief, scenario matrix, target contract and gap matrix exist;
- token map follows the hierarchy Component semantic token -> Framework role
  token -> profile scale -> base size; changed first-party Component/Smart CSS
  introduces no raw design sizes or colors and records every allowed legacy,
  third-party or Core-definition exception;
- typography uses typography roles or a verified size/line-height pair, spacing
  uses spacing/content-spacing roles, and colors use semantic role tokens;
- surface geometry matrix distinguishes `--sf-radius--ui` for compact controls,
  `--sf-radius-default` for large surfaces and paired space/radius scale levels
  for actual nested visual shells rather than arbitrary DOM depth;
- Component structure map records Block, Elements, Modifiers, composition
  ownership and every Element promoted to an independent Block; Smart does not
  duplicate the visual class tree of its base Component;
- public `data-*` contract uses class scope plus short property names, keeps one
  independent property per attribute, uses values for mutually exclusive
  variants, prefers native/ARIA state and records public/private and
  compatibility boundaries; Smart inherits the base vocabulary;
- state geometry matrix covers interactive and domain states, including the
  boundary between the active control and adjacent content;
- focus contract names the perceived focus owner, uses `:focus-visible` for
  new visual focus, selects outer `--sf-ui-focus` or joined/clipped
  `--sf-ui-focus-inset` geometry, preserves DOM focus after pointer input and
  covers forced-colors plus keyboard, pointer and programmatic transitions;
- a compound wrapper may use `:has(:focus-visible)`, while bare
  `:focus-within` does not qualify as an input-modality-aware indicator;
- hover, focus and active states do not become the only cue that separates an
  interactive control from adjacent non-interactive content; any persistent
  separator or surface boundary is layout-neutral and token-based;
- visual hierarchy uses the minimum sufficient combination of size, weight,
  color, spacing and surface contrast; semantic heading rank is not treated as
  an automatic visual-size requirement inside compact controls;
- every surface modifier has a repeated surrounding-layout scenario and a
  complete surface matrix; `outline` and `flush` keep their distinct meanings,
  use semantic tokens and share the base behavior instead of duplicating it;
- state indicators have one explicit semantic model across states, with
  accessibility, LTR/RTL and reduced-motion behavior recorded;
- default and every modifier correspond to a verified scenario;
- base Component is implemented and verified before Smart projection;
- Smart projection reuses the base visual contract and contains only justified
  data, state and side effects;
- live examples and documentation reflect the verified source contract;
- browser, keyboard/accessibility, responsive, theme and visual-coherence
  evidence includes computed spacing and geometry rather than screenshots only;
- compatibility, deprecation and technology-quality feedback are explicit.

Do not close the batch on screenshots alone, with duplicated Component/Smart
styles, or when a new modifier is only an unverified visual preference.
