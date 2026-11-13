# Repository va version control jarayoni

## Private implementation

- Source code, PRD, ADR, task va CI private repository’da qoladi.
- Public repository private source’ni mirror qilmaydi.
- Branch va commit auditidan faqat maxfiy bo‘lmagan xulosalar chiqariladi.

## Public academic repository

- Requirements, diagramma, screenshot, test xulosasi, SDLC va PDF artefaktlari.
- Mantiqiy commitlar bo‘limlar bo‘yicha ajratiladi.
- Secret/PII/link audit’dan keyin `main`ga push qilinadi.

## Commit konvensiyasi

```text
docs: add project overview and requirements
docs: add UML and system design diagrams
docs: add database and UI design materials
docs: add implementation and deployment documentation
test: add test plan cases and verified report
docs: add SDLC lifecycle and maintenance
docs: finalize README PDF and audit
```

## Definition of Done

- Talab ID va RTM to‘liq.
- `.drawio` ochiladi; SVG/PNG o‘sha source’dan export qilingan.
- Link va image reference ishlaydi.
- Test natijasi real command yoki `NOT RUN`.
- Current va Proposed aralashmagan.
- Public fayllarda token, parol, private source yoki email yo‘q.
