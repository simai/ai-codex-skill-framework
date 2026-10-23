# Источники SIMAI Framework

> Источник: github.com/simai/ui-source, github.com/simai/ui (README, contracts/releases) · Проверено: 2026-10-23 · Версия: ui-source aa81305b14f1, ui 3d9bf903a590 (выпуск ui-720203c5b5e5)

Какой репозиторий считать истиной на какой вопрос и как обновлять снимок
источников навыка. Продукты и пакеты семейства — в
[framework-family.md](framework-family.md).

## Модель «источник → выпуск»

- `simai/ui-source` — **редактируемый источник** Framework: Core, Loader (один
  модуль внутри, бывший `simai/ui-loader`, имя сохранено редиректом GitHub),
  утилиты, компоненты, Smart Components, их контракты и тесты. Папки:
  `src/core`, `src/utility`, `src/component`, `src/smart`, `contracts/`.
  Лицензия Apache-2.0 (код до смены лицензии остаётся под MIT).
- `simai/ui-builder` — воспроизводимая сборка (Webpack) из ui-source в ui.
- `simai/ui` — **сгенерированный выпуск**, руками не правится: `distr/core`,
  `distr/component`, `distr/utility`, `distr/smart`, `distr/rule`. Выпуск — это
  коммит `Build: …`, имя `ui-<12 hex>`; тегов и номеров версий больше нет
  (последний тег `v5.6.4`). Что из чего собрано —
  `contracts/releases/ui-<id>.lock.json`. Подключать только закреплённый коммит,
  не `main`. Apache-2.0.
- `simai/ui-smart` — **архив** (только чтение): был зеркалом `ui/distr/smart`,
  пока потребители переезжали. `window.sfSmartPath` нужен только страницам,
  которые всё ещё грузят Smart из архива.
- `simai/ui-doc` — публичная документация https://ui.simai.io/ (Docara,
  исходник — `content/ru`, английский — перевод по мере приёмки).
- `simai/ui-play` — playground и живые примеры (`examples/`, ветка `main`).
- `simai/ui-vscode` — расширение VS Code (подсказки классов и `sf-*`), MIT.
- `simai/ui-components` — пустая заглушка; `ui-doc-core`, `ui-doc-template` —
  бывшие тема и шаблон документации, для новой работы не используются.

## Кому верить

| Вопрос | Источник |
|---|---|
| Как это работает и как поменять | `ui-source` (`src/…`, `contracts/`, `tests/`) |
| Что реально поставляется в выпуске | `ui/distr/…` на закреплённом коммите |
| Есть ли такой Smart Component | `ui/distr/smart/<имя>` (не `ui-smart`) |
| Из каких ревизий собран выпуск | `ui/contracts/releases/ui-<id>.lock.json` |
| Что изменилось | `ui/CHANGELOG.md`, журнал `ui-source/contracts/changes/journal.json` |
| Как описано для людей | `ui-doc/content/ru` |
| Рабочий пример разметки | `ui-play/examples` |
| Компонент продукта (sf-table и т. п.) | репозиторий-владелец пакета, см. [framework-family.md](framework-family.md) |

Старое имя или значение работает через псевдоним до даты удаления; чистка —
1-го числа месяца (решение владельца 2026-10-09, `ui-control`
`control/FRAMEWORK-LIFECYCLE.md`). Поэтому сверяйте имена по журналу
изменений, а не по памяти.

## Снимок навыка

Навык держит машинный снимок источников для подбора компонентов, рецептов и
проверки классов:

- список источников — `references/vendor/source-repos.json`;
- ревизии последнего снимка — `references/vendor/source-repos.lock.json`;
- производные: `references/vendor/source-inventory.json`,
  `references/source-inventory.md`, `references/vendor/component-smart-catalog.json`,
  `references/component-smart-catalog.md`, `references/ui-doc-manifest.json` и
  атласы `ui-doc-*`.

Снимок от 2026-10-23: 72 компонента, 55 Smart Components, 228 групп утилит в
выпуске. С июльского снимка из свободного выпуска ушли Smart `table` и
`admin-menu` (теперь `sf-table`, `sf-admin-menu` в SIMAI Pro), появились
`button-group`, `copy-button`, `empty-state`, `page-header`, `popover`,
`theme-generator` и другие. Таблица в конвертере Tailwind поэтому остаётся
статической разметкой.

`references/vendor/source/catalog-lite.sf-only.json` (каталог CSS-классов)
генератора в навыке не имеет и этим обновлением не пересобран.

## Обновление снимка

Зеркало лежит в игнорируемой папке `source/simai/` репозитория навыка.

1. Получить источники: `python3 skills/framework/scripts/sync_source_repos.py`
   (клонирует или обновляет репозитории из `source-repos.json`). Если рядом
   есть свежие локальные копии, можно скопировать в зеркало только нужные
   папки (`ui/distr`, `ui/contracts`, `ui-source/src`, `ui-play/examples`,
   `ui-play/packages`, `ui-doc/content`) и записать ревизии в lock вручную —
   так сделан снимок 2026-10-23.
2. Пересобрать производные:

```bash
python3 skills/framework/scripts/build_source_inventory.py --repo-root . --skill-root skills/framework
python3 skills/framework/scripts/build_component_smart_catalog.py --repo-root . --skill-root skills/framework
python3 skills/framework/scripts/build_ui_doc_atlas.py --docs-root source/simai/ui-doc/content/ru --skill-root skills/framework
```

3. Проверить: `bash skills/framework/scripts/run_local_checks.sh`. Ссылки
   рецептов на страницы документации лежат в
   `references/vendor/working-set.section-variants.json`; если страницы
   переехали, проверка `validate_working_set_sources.py` их назовёт.

## Быстрый поиск в зеркале

```bash
find source/simai/ui/distr/component -mindepth 1 -maxdepth 1 -type d | sort
find source/simai/ui/distr/smart -mindepth 1 -maxdepth 1 -type d | sort
find source/simai/ui-source/src/utility -mindepth 1 -maxdepth 1 -type d | sort
rg -n "sf-button|sf-code" source/simai/ui-play/examples
```
