# API Structure

API Hub ichida `/api/v1` namespace ostida REST uslubida tashkil qilingan. Quyidagi jadval public contract darajasidagi umumlashtirishdir; private source yoki credential ko‘chirilmagan.

| Guruh | Endpoint yo‘nalishi | Asosiy amallar |
|---|---|---|
| Health/Bootstrap | health, bootstrap, brand | Hub health va client bootstrap |
| Devices | devices, pairing, TV token | Code yaratish, pair, list/revoke, TV access |
| Auth | auth, sessions | PIN/OWNER login, logout, activity, password change |
| Menu | menu, categories, products, variants, modifiers | POS read va OWNER CRUD |
| Stop-list | stop-list | Variant/modifier availability |
| Shifts | shifts, cash movements | Open, status, cash-in/out, close |
| Orders | orders, items, status | Create/edit, kitchen send, cancel, ready/complete |
| Payments | payments, refunds/void | CASH/CARD/QR/split, reversal |
| Reports | daily, Z-report | Operational summary va shift snapshot |
| Settings | branch, payment QR, brand | OWNER operational settings |
| Backup | menu archive, full backup, restore | Export/import, staged restore va status |
| Printing | printers, print jobs | Queue/status; physical device validation Partial |

## Contract qoidalari

- Request body/query/params Zod schema bilan tekshiriladi.
- Protected route opaque cookie/session va role permission talab qiladi.
- Business/Branch ID client’dan source of truth sifatida olinmaydi.
- Critical mutation idempotency key ishlatadi.
- Error envelope stable code, message va optional details beradi.
- Secret, hash, stack trace yoki raw database error response’ga chiqmaydi.

## Status code tamoyili

| Kod | Mazmuni |
|---:|---|
| 200/201 | Muvaffaqiyatli read/create |
| 400 | Schema yoki business input xatosi |
| 401 | Session/credential yaroqsiz |
| 403 | Role/scope ruxsati yo‘q |
| 404 | Scoped entity topilmadi |
| 409 | State transition, idempotency yoki active-shift conflict |
| 413 | Archive/upload limitdan katta |
| 429 | PIN/pairing rate limit/lockout |
| 500 | Sanitized internal error; correlation ID bilan log |
