# Implementatsiya sharhi

## Joriy stack

| Qatlam | Texnologiya / yondashuv |
|---|---|
| Hub | Node.js, Express, TypeScript |
| Validation | Zod |
| Database | Prisma 6.x, SQLite |
| POS/Admin | React 19, Vite |
| Logging | Pino, structured logs |
| Credential hashing | argon2id |
| Identifikator | ULID |
| TV yangilanishi | HTTP polling |
| Deployment | Windows installer/service/autostart scripts |

## Modul chegaralari

- `auth` — login, PIN, session, role va lockout;
- `devices` — pairing, device lifecycle va TV token;
- `menu` — category, product, variant, modifier va stop-list;
- `orders` — order/item, total, state transition va cancellation;
- `payments` — payment, split, refund va idempotency;
- `shifts` — shift, cash movement va Z-report;
- `reports` — operational daily data va aggregation;
- `settings` — business/branch va operational konfiguratsiya;
- `backup` — backup/restore lifecycle;
- `printing` — printer va print job queue;
- `audit` — critical event izi.

## Public preview chegarasi

Ushbu repository manba kodini dublyaj qilmaydi. Implementatsiya faktlari private repository’dagi branch, schema, route va test auditidan kelib chiqadi. Secret, private remote, real credential yoki production ma’lumoti chiqarilmaydi.

## Ma’lum texnik qarz

- Admin Dashboard/Reports real aggregation API’ga to‘liq ulanishi yakuniy E2E dalil talab qiladi.
- Fizik printer integratsiyasi real qurilmada retry/duplicate/hardware matrix bo‘yicha tekshirilishi kerak.
- Current modular monolith va cloud/microservices kelajak ishlari bitta “tayyor” tizim sifatida aralashtirilmasligi kerak.
