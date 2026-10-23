# Семейство SIMAI Framework

> Источник: README и LICENSE репозиториев simai/ui-control, ui-source, ui, ui-pro, ui-admin, ui-chat, ui-mail, larena-ui, ui-doc · Проверено: 2026-10-23 · Версия: ui-control 12fce7ad6712, ui-pro f827be81dda4, ui-admin 3326a35cab2b, ui-chat c491ea82b740 (0.2.5), ui-mail f337133a754d (0.7.0), larena-ui 51cf18f40a76

Публичное имя — **SIMAI Framework** (SIMAI всегда заглавными, решение
владельца 2026-10-19), технический префикс — `sf`. `sf5` и написание «Simai» (не заглавными)
в новых текстах, идентификаторах и коде не используются.

Навык `framework` приносит знание о Framework; репозитории ему не
принадлежат. Работу в конкретном репозитории ведёт тред этого репозитория
(организует `dev` или `teamlead`), а навык подсказывает, как правильно.

## Координация: ui-control

`simai/ui-control` — хаб семейства: здесь живут треды Framework и диспетчер,
который раскладывает цель по репозиториям-владельцам и принимает результат.
В нём хранятся роли репозиториев, межрепозиторные решения, очередь работ,
Compatibility BOM, release train, readiness и handoff-пакеты; исходников
продуктов там нет. Начало треда — `START.md`, правила диспетчера — `AGENTS.md`,
порядок работы — `control/ROADMAP.md`, решения — `control/*.md` с датой.

Цикл задачи: замечание или задача заводится в репозитории-владельце (для
Framework — issue в `simai/ui-source`), диспетчер ui-control готовит
ограниченное поручение (цель, Done When, границы записи, гейты, откат), тред
владельца делает, ui-control принимает доказательства отдельно от отчёта и
обновляет совместимость. Один писатель на репозиторий одновременно.

`control/CURRENT.yaml` обновлялся 2026-09-13 и часть фактов в нём (например,
лицензии) устарела: сверяйтесь с README и LICENSE самих репозиториев.

## Ядро

| Репозиторий | Роль | Лицензия |
|---|---|---|
| `ui-source` | редактируемый источник Core, Loader, утилит, компонентов, Smart | Apache-2.0 |
| `ui-builder` | воспроизводимая сборка | Apache-2.0 |
| `ui` | сгенерированный выпуск `distr/`, руками не правится | Apache-2.0 |
| `ui-smart` | архив бывшего Smart-зеркала, только чтение | — |
| `ui-doc` | документация https://ui.simai.io/ (Docara, `content/ru`) | Apache-2.0, тексты — отдельная лицензия `LICENSE-CONTENT.md` |
| `ui-play` | playground и примеры | не указана |
| `ui-studio` | лаборатория и реестр Smart Components, экспорт рецепта в HTML или пакет для Larena | не указана |
| `ui-vscode` | расширение VS Code | MIT |
| `ui-effects` | фоновые эффекты (каталог https://effects.simai.io/) вне Framework | Apache-2.0 |
| `ui-icons` | сервис подмножеств иконок https://icons.simai.io | Apache-2.0 |

Подробно об источниках и снимке навыка — [source-repositories.md](source-repositories.md).

## Пакеты компонентов: компонент живёт у владельца

Framework расширяется пакетами компонентов (стандарт `simai.component-package`,
`ui-source/docs/developer/component-packages.md`). Пакет собирается
`ui-builder` против одного закреплённого выпуска Framework и подключается
страницей:

```html
<script>window.SF_BOOT_CONFIG = {packages: {larena: {base: '/distr-larena/'}}};</script>
```

Первый пакет — `larena`: `sf-table`, `sf-data-view`, `sf-property-view`,
`sf-admin-menu`. Владелец исходника менялся: `larena-ui` → `ui-admin`
(2026-10-22) → **`simai/ui-pro`** (2026-10-23, продукт SIMAI Pro). Архив
пакета с sha256 и квитанцией публикуется в релизах `simai/larena-ui`, откуда
его берут установщик и проверки Larena. Лицензия SIMAI Pro: бесплатно малому
бизнесу (PolyForm Small Business 1.0.0) и некоммерческому использованию
(PolyForm Noncommercial 1.0.0), остальным — коммерческая лицензия SIMAI; в
составе Larena покрывается лицензией Larena.

README `ui-source` на 2026-10-23 ещё называет владельцем пакета `larena-ui` —
актуальнее README `ui-pro` и `ui-admin`. Перед работой с этими компонентами
проверьте README владельца заново.

## Продукты на Framework

| Репозиторий | Что это | Как связан с Framework |
|---|---|---|
| `ui-admin` | SIMAI Admin: эталонное приложение для компонентов SIMAI Pro и полигон (120 записей, mock API) | читает соседние `../ui` и `../ui-pro`, закрепляет пару; лицензия PolyForm/коммерческая |
| `ui-chat` | SIMAI Chat: окно чата Mirai на компонентах `sf-chat-*`, без React; сборки `staff`, `widget` (Shadow DOM, без ядра), `embed` | берёт закреплённый выпуск из `../ui` с проверкой sha256; данные только по API-договору Mirai24 |
| `ui-mail` | SIMAI — редактор писем: блоки, браузерный и локальный режим с CLI и MCP | `framework.lock.json` с хэшами; приватный до приёмки (M7); Apache-2.0 |
| `larena-ui` | UI-пакет Larena (PHP): `SmartRegistry`, `ui.dataview`, рендер Smart-манифестов в элементы Framework | закреплённые элементы Framework; релизы несут архив пакета `larena`; Apache-2.0 |

Общее правило для продуктов: продукт закрепляет конкретный выпуск `ui`
(lock с хэшами), не тянет `main`, не копирует CSS Framework к себе и не чинит
дефект компонента локальным override — дефект уходит задачей в `ui-source`.
Сложный интерфейс (админка, чат, редактор) собирается из компонентов и
утилит Framework; чего не хватает — оформляется как `no_fit` и задача
владельцу компонента, а не как свой примитив в продукте.

## Чего здесь нет

- Концепция «профилей» комплексных интерфейсов в исходниках на 2026-10-23 не
  описана — не выдумывать, спрашивать у треда ui-control.
- Аудит смежных продуктов (например, `ui-vscode`) против текущего выпуска
  делается по снимку из [source-repositories.md](source-repositories.md):
  сравнить их списки компонентов и классов с `ui/distr` закреплённого выпуска.
