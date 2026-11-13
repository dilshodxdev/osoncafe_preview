# Data Dictionary

Joriy Prisma schema 30 ta modeldan iborat. Quyidagi jadval public hujjatlashtirish uchun asosiy vazifa, scope va relation’larni beradi; private schema source code ko‘chirilmagan.

| Model | Domain | Vazifasi | Asosiy relation |
|---|---|---|---|
| Business | Core | Tenant/biznes ildizi | Branch, catalog, settings |
| Branch | Core | Filial scope’i | Business, User, Device, Shift, Order |
| User | Identity | Xodim va rol | Branch, Session, AuditLog |
| Device | Identity | Pairing qilingan client | Branch, pairing/session context |
| Session | Identity | Server-side opaque session | User, Device |
| PairingCode | Identity | Bir martalik device code | Branch, creator, expiry |
| PairingAttempt | Security | Pairing urinish auditi/limit | Code/device context |
| TechnicalCode | Security | Nazoratli texnik amal kodi | Scope, expiry, consumed state |
| Category | Catalog | Menu kategoriyasi | Business, Product |
| Product | Catalog | Sotiladigan mahsulot | Category, ProductVariant |
| ProductVariant | Catalog | Narx va sotuv varianti | Product, Modifier, StopListItem |
| ModifierGroup | Catalog | Modifier guruh qoidasi | Product/variant va Modifier |
| Modifier | Catalog | Qo‘shimcha tanlov/narx | ModifierGroup, OrderItemModifier |
| StopListItem | Catalog | Vaqtincha sotilmaydigan element | Branch, variant/modifier |
| OrderCounter | Sales | Branch order raqami generatori | Branch, sequence |
| Order | Sales | Buyurtma aggregate root | Shift, User, OrderItem, Payment |
| OrderItem | Sales | Buyurtma qatori va price snapshot | Order, variant, modifiers |
| OrderItemModifier | Sales | Tanlangan modifier snapshot’i | OrderItem, Modifier |
| Payment | Sales | To‘lov qismi/usuli | Order, Refund |
| Refund | Sales | Asl payment’ga bog‘langan reversal | Payment, actor, reason |
| Discount | Sales | Chegirma qoidasi/qo‘llanishi | Order, approver |
| Membership | Sales | Mijoz/member konteksti | Business/order context |
| Shift | Operations | Kassa ochilish-yopilish davri | Branch, User, Order, CashMovement |
| CashMovement | Operations | Cash-in/cash-out | Shift, actor, reason |
| ZReport | Operations | Yopilgan smena xulosasi | Shift (1:1) |
| Printer | Operations | Printer konfiguratsiyasi | Branch, PrintJob |
| PrintJob | Operations | Receipt/kitchen chop navbati | Printer, Order, status/attempt |
| TvToken | Operations | TV read-only access | Branch, expiry/revoke |
| AuditLog | Audit | Append-only kritik amal izi | Actor, entity, before/after context |
| IdempotencyRecord | Reliability | Duplicate write’ni oldini olish | Scope, key, request/result hash |

## Ma’lumot turlari va invariantlar

- Identifier: ULID/string.
- Money: integer minor unit; `float` emas.
- Time: UTC timestamp; UI’da lokal format.
- Status: shared enum va ruxsat etilgan state transition.
- Credential: faqat hash/opaque token; raw qiymat database yoki log’da saqlanmaydi.
- Har bir transactional query Business/Branch scope bilan cheklanadi.
- Tarixiy OrderItem nomi va narxi snapshot bo‘lib, menu tahriridan o‘zgarmaydi.
- AuditLog va moliyaviy yozuvlar oddiy UI orqali o‘chirilmaydi.

ERD: [D19 Database ERD](../04-Diagrams/D19-Database-ERD/D19-Database-ERD.svg)
