# Backend Architecture

## Stack

- Node.js + Express 5 + TypeScript.
- Zod schema validation.
- Prisma 6.19.3 + SQLite.
- Pino structured logging.
- Argon2id credential hashing.
- ULID identifiers.

## Modul tuzilmasi

Har bir business modul route, service va repository mas’uliyatlariga ajratiladi. Route transport va validation’ni; service use case/invariant’ni; repository esa scoped persistence’ni bajaradi.

| Modul | Asosiy mas’uliyat |
|---|---|
| Auth/Devices | Pairing, PIN/owner login, session, role, lockout |
| Menu | Category, product, variant, modifier, stop-list |
| Orders | Order lifecycle, totals, snapshot, cancellation |
| Payments | Method/split, idempotency, refund/void |
| Shifts | Open/close, cash movement, expected cash, Z-report |
| Reports | Daily operational data va aggregation boundary |
| Settings | Branch, payment QR, brand va operational settings |
| Print | Printer/PrintJob queue; hardware status Partial |
| Backup | Archive, retention, restore safety |
| Audit | Append-only critical event izi |

## Error contract

Business error stable code, human-readable Uzbek message, optional field/details va correlation ID bilan qaytariladi. Raw stack trace, hash, token yoki database detail client’ga chiqmaydi.
