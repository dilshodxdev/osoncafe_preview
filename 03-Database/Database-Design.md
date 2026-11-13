# Ma’lumotlar bazasi dizayni

## Joriy texnologiya

- ORM: Prisma 6.x
- Database: SQLite
- Arxitektura: Hub-only modular monolith
- Pul: integer minor unit
- Scope: Business va Branch context

## Model katalogi

| Domain | Modellar |
|---|---|
| Core / Identity | Business, Branch, User, Device, Session, PairingCode, PairingAttempt, TechnicalCode |
| Catalog | Category, Product, ProductVariant, ModifierGroup, Modifier, StopListItem |
| Sales | OrderCounter, Order, OrderItem, OrderItemModifier, Payment, Discount, Membership, Refund |
| Operations | Shift, CashMovement, Printer, PrintJob, ZReport, TvToken |
| Security / Reliability | AuditLog, IdempotencyRecord |

## Asosiy invariantlar

1. Business → Branch → transaction entity scope’i uzilmaydi.
2. User, session va device aktivligi authorization’da tekshiriladi.
3. Order number branch/counter doirasida nazorat qilinadi.
4. Order item narxi va nomi tarixiy snapshot sifatida saqlanadi.
5. Payment va refund asl order/payment bilan bog‘lanadi.
6. Bir branch’da bitta aktiv shift qoidasi transaction darajasida himoyalanadi.
7. Idempotency record critical write natijasini replay uchun saqlaydi.
8. Audit log critical entity/action kontekstini saqlaydi.

## ERD scope’i

D19 barcha 30 modelni ko‘rsatadi. O‘qiluvchanlik uchun bir sahifada besh domain cluster, markazda `Business`, `Branch`, `Shift` va `Order` joylashadi. PK/FK nomlari qisqartirilmaydi; non-critical field’lar yashirilishi mumkin, ammo cardinality va unique constraint’lar saqlanadi.
