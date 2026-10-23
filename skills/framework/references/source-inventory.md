# SIMAI Framework Source Inventory

> Источник: github.com/simai/ui, github.com/simai/ui-source, github.com/simai/ui-doc, github.com/simai/ui-play, github.com/simai/ui-vscode · Проверено: 2026-10-23 · Версия: ui 3d9bf903a590, ui-source aa81305b14f1, ui-doc ae2c38b8b1ab, ui-play e062a00367aa, ui-vscode 352cd897bb63

Generated from synced upstream repositories under `source/simai`.

## Source Revisions

- `ui`: `main` @ `3d9bf903a590fc7c21e5ea14983742b0225edbe7`
- `ui-source`: `main` @ `aa81305b14f103def02dead1ffc0b0451c877f0f`
- `ui-doc`: `main` @ `ae2c38b8b1abcc56a62221cbbf3b19679475542a`
- `ui-play`: `main` @ `e062a00367aa5ee1af6266d6416b8ba59c2ca21f`
- `ui-vscode`: `main` @ `352cd897bb63711ff600dbd06dbea923c14dfe6a`

## Summary

- Shipped components in `ui`: `72`
- Shipped smart-components in `ui/distr/smart`: `55`
- Shipped utility groups in `ui`: `228`
- Utility source groups in `ui-source`: `229`
- Component example groups in `ui-play`: `38`
- Smart example groups in `ui-play`: `44`
- Shipped components without direct component example groups: `36`
- Shipped smart-components without direct smart example groups: `18`

## Practical Reading Order

- For utility/layout work: start with the `ui-doc` atlas, validate shipped groups in `ui`, then inspect rule and state semantics in `ui-source/src/utility`.
- For presentational components: start with `ui-play/examples/components`, then confirm shipping in `ui/distr/component`.
- For smart-components: start with `ui-play/examples/smart-components`, then confirm runtime presence in `ui/distr/smart`.
- For loader/runtime assumptions: confirm actual boot paths in `ui-play/packages/*/setup-sf.ts` and shipped paths in `ui/distr/core`.

## Component Coverage

- `accordion`: `components/accordion/default`
- `admin-menu`: `components/admin-menu/default`
- `alerts`: `alert`
- `avatars`: `avatar`
- `badges`: `components/badges/all`
- `breadcrumbs`: `components/breadcrumbs/default`
- `button-group`: `components/button-group/default`
- `buttons`: `components/buttons/all, components/buttons/segments, components/buttons/tightness`
- `checkbox`: `components/checkbox/all`
- `close`: `components/close/default`
- `context-menu`: `components/context-menu/all`
- `datepicker`: `components/datepicker/default`
- `download-file`: `components/download-file/default`
- `dropdown`: `components/dropdown/dropdown, components/dropdown/list, components/dropdown/list-item`
- `featured-icon`: `components/featured-icon/all`
- `file-preview`: `components/file-preview/default`
- `file-upload`: `components/file-upload/default, components/file-upload/interactive`
- `icon-buttons`: `components/icon-buttons/icon-buttons`
- `inputs`: `components/inputs/all, components/inputs/country-code, components/inputs/quantity, components/inputs/textarea, components/inputs/verification`
- `menu`: `components/menu/default`
- `modal`: `components/modal/all`
- `outline`: `examples/outline`
- `pagination`: `components/pagination/default, components/pagination/page-number`
- `placeholder`: `components/placeholder/default`
- `range-slider`: `components/range-slider/default`
- `reference-link`: `components/reference-link/default`
- `skeleton`: `components/skeleton/default`
- `slider`: `components/slider/default`
- `spinner`: `components/spinner/default`
- `step`: `components/step/default`
- `switch`: `components/switch/default`
- `tabs`: `components/tabs/default`
- `tags`: `components/tags/all`
- `toast`: `components/toast/default`
- `toggle`: `components/toggle/default`
- `tooltip`: `components/tooltip/all`

Direct component-example gaps:

- `ajax`
- `ajaxload`
- `carousel`
- `clipboard`
- `contentDivider`
- `country-code`
- `doc`
- `dot`
- `emoji`
- `fab`
- `flag`
- `hideShow`
- `highlight`
- `icons`
- `kbd`
- `lazy-load`
- `link`
- `overbox`
- `overcard`
- `progress-bar`
- `progress-scale`
- `quantity`
- `radio`
- `scrollbar`
- `sf-system`
- `share`
- `special`
- `swiper`
- `tab`
- `textarea`
- `theme`
- `tree`
- `tree-item`
- `verification`
- `viewbox`
- `wow`

## Smart-Component Coverage

- `alert`: `smart-components/alert/default`
- `avatar`: `smart-components/avatar/element, smart-components/avatar/group`
- `avatars`: `avatar/group`
- `badges`: `smart-components/badges/element`
- `breadcrumbs`: `smart-components/breadcrumbs/default`
- `button-group`: `smart-components/button-group/default`
- `buttons`: `smart-components/buttons/element, smart-components/buttons/events`
- `checkbox`: `smart-components/checkbox/all`
- `context-menu`: `smart-components/context-menu/default`
- `country-code`: `inputs/country-code`
- `download-file`: `smart-components/download-file/element`
- `dropdown`: `smart-components/dropdown/element`
- `file-upload`: `smart-components/file-upload/element`
- `gallery`: `smart-components/gallery/default, smart-components/gallery/images`
- `icon-buttons`: `smart-components/icon-buttons/element`
- `icons`: `smart-components/icons/default`
- `inputs`: `smart-components/inputs/country-code, smart-components/inputs/element, smart-components/inputs/password`
- `list-item`: `smart-components/list-item/element`
- `modal`: `smart-components/modal/element`
- `pagination`: `smart-components/pagination/default`
- `progress-bar`: `progress/progress-bar`
- `progress-scale`: `progress/progress-scale`
- `radio`: `smart-components/radio/all`
- `range-slider`: `smart-components/range-slider/default`
- `reference-link`: `smart-components/reference-link/default`
- `skeleton`: `smart-components/skeleton/default`
- `slider`: `smart-components/slider/default`
- `spinner`: `smart-components/spinner/default`
- `steps`: `smart-components/steps/default`
- `switch`: `smart-components/switch/default`
- `tabs`: `smart-components/tabs/default`
- `tags`: `smart-components/tags/element`
- `textarea`: `smart-components/textarea/element`
- `toast`: `smart-components/toast/default`
- `toggle`: `smart-components/toggle/default`
- `tooltip`: `smart-components/tooltip/element`
- `tree`: `smart-components/tree/default, smart-components/tree/item`

Direct smart-example gaps:

- `close`
- `color`
- `composition-overlay`
- `copy-button`
- `datepicker`
- `drawer`
- `empty-state`
- `field-renderers`
- `file-preview`
- `help-mark`
- `inline-editor`
- `page-header`
- `popover`
- `profile-picker`
- `resizer`
- `sortable`
- `theme-generator`
- `tree-item`

## Utility Example Groups

- `animation`
- `backdrop-filter`
- `background`
- `border`
- `divider`
- `filters`
- `flex`
- `forms`
- `grid`
- `grid-and-flexbox-utilities`
- `indents`
- `interactivity`
- `layout`
- `layout-break`
- `links`
- `mask`
- `objects`
- `outline`
- `overscroll`
- `print`
- `shadows`
- `sizes`
- `stripes`
- `svg`
- `tables`
- `text-formatting`
- `transform`
- `typography`
- `utilities`
