# Arxitektura sharhi

## Joriy holat — Current

osonCafe pilot versiyasi bitta Node.js/Express/TypeScript Hub atrofida qurilgan modular monolith. Hub lokal tarmoqda POS (`/`), Admin (`/admin`) va TV (`/tv`) client’larini taqdim etadi. Business ma’lumotlari Prisma orqali SQLite’da saqlanadi.

```text
POS / Admin / TV
        │ HTTP polling
        ▼
Node.js + Express + TypeScript Hub
        │ Prisma ORM
        ▼
      SQLite
```

Modullar: auth, devices/pairing, menu, orders, payments, shifts/cash, reporting, settings, backup, print jobs va audit. Joriy pilotda Hub business truth manbai hisoblanadi.

## Kelajak holati — Proposed

Akademik evolyutsiya modeli quyidagi mustaqil xizmatlarni ko‘zda tutadi:

1. **Identity Service** — user, role, device, session va pairing;
2. **Catalog Service** — category, product, variant, modifier va stop-list;
3. **Sales Service** — order, order item, payment, discount va refund;
4. **Operations Service** — shift, cash movement, print job va operational workflow;
5. **Reporting Service** — read model, dashboard, audit va analitika.

API Gateway va message broker xizmatlararo integratsiyani boshqaradi; har bir service o‘z database scope’iga ega bo‘ladi. Bu model ishlab chiqarilgan joriy pilot emas.

## Asosiy arxitektura qarorlari

| ADR | Qaror | Sabab |
|---|---|---|
| ADR-001 | Hub database’ga Prisma ORM orqali murojaat qiladi | Typed schema, migration va query nazorati |
| ADR-002 | Pilot modular monolith sifatida quriladi | Lokal deployment va operatsion soddalik |
| ADR-003 | Pilot Hub-only, internetdan mustaqil | Kafe savdosi internet uzilishida davom etishi kerak |
| ADR-004 | Opaque token server-side session’ga bog‘lanadi | Revoke/expiry nazoratini markazlashtirish |
| ADR-005 | Credential argon2id bilan hash qilinadi | Offline cracking xavfini kamaytirish |

## Chegaralar

- Client narx, total, rol yoki state transition bo‘yicha ishonchli manba emas; Hub qayta tekshiradi.
- Har bir query business/branch scope’ga bog‘lanadi.
- Moliyaviy write idempotent bo‘lishi kerak.
- Current va Proposed diagrammalar bir-biridan rang, sarlavha va boundary bilan ajratiladi.
