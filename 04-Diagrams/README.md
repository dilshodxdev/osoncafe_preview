# Diagramma artefaktlari

Bu papkada 27 ta arxitektura, UML, ERD va BPMN diagrammasi mavjud. Har bir diagramma alohida papkada uch formatda saqlanadi.

## Formatlar

- `.drawio` — tahrirlanadigan source of truth;
- `.svg` — GitHub va web uchun asosiy vektor preview;
- `.png` — PDF va universal raster fallback.

Jami: **27 `.drawio` + 27 `.svg` + 27 `.png` = 81 artefakt**.

Diagrammalar [Diagram Registry](../02-System-Design/Diagram-Registry.md), [Diagram Specifications](../02-System-Design/Diagram-Specifications.md) va [Visual Standard](../09-References/Visual-Standard.md) bilan bog‘langan. `Current`, `Partial` va `Proposed` statuslari diagramma sarlavhasi yoki legendasida ko‘rsatiladi.

## Qayta ishlab chiqarish

`tools/generate_diagrams.py` editable Draw.io manbalarini yaratadi. SVG va PNG eksportlari rasmiy Draw.io desktop CLI orqali manbalardan olingan. Eksportdan keyin barcha PNG renderlar contact-sheet ko‘rinishida vizual tekshirildi.

Fayl nomlash namunasi:

- `D01-System-Context/D01-System-Context.drawio`
- `D01-System-Context/D01-System-Context.svg`
- `D01-System-Context/D01-System-Context.png`

