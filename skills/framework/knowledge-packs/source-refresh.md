# Knowledge Pack: Source Refresh

> Источник: github.com/simai/ui-source, github.com/simai/ui · Проверено: 2026-10-23 · Версия: ui-source aa81305b14f1, ui 3d9bf903a590

Use this pack when the activity is `source-refresh`.

Focus:

- sync `source/simai/*` mirrors safely;
- detect upstream path drift in `ui`, `ui-source`, `ui-play` and `ui-doc` (`ui-smart` is archived, `ui-loader` is now `ui-source`);
- rebuild source-backed inventories and docs atlases only where needed;
- keep derived manifests aligned with real upstream layout.

Default artifacts:

- `scripts/sync_source_repos.py`
- `scripts/build_source_inventory.py`
- `scripts/validate_source_refresh_contract.py`
- `references/vendor/source-repos.lock.json`
- `references/vendor/source-repos.json`
- `references/vendor/source-inventory.json`
- `references/source-inventory.md`
- source-path updates inside working-set manifests when upstream examples moved

Execution contract:

- `sync_source_repos.py --format json` is the machine-readable mirror sync entrypoint;
- `build_source_inventory.py --format json` is the machine-readable derived inventory entrypoint;
- `source-repos.lock.json` must stay aligned with `source-repos.json`;
- `source-inventory.json` must stay aligned with both the lock file and the actual `source/simai/*` tree.

Common failure classes:

- upstream branch drift such as `main` vs `master`;
- `ui-play` path moves that break working-set extracts;
- source inventory counts falling to zero because a mirror path changed;
- optional repos like `ui-components` failing sync without blocking primary truth.

Minimum verification:

- source paths exist after sync;
- source inventory rebuild succeeds;
- required primary repos are `ok` in the lock file;
- inventory counts for shipped components, smart-components, and example groups stay non-zero;
- `validate_source_refresh_contract.py` stays green;
- local checks still pass when source-backed contracts changed.
