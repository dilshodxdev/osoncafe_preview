# 27 diagrammaning semantik spetsifikatsiyasi

Ushbu hujjat vizual chizishdan oldingi audit shartnomasidir. Diagramma chiroyli ko‘rinishi bilan birga quyidagi obyekt va munosabatlarni aynan ifodalashi kerak.

## Kontekst va strukturaviy diagrammalar

### D01 — System Context

- **Boundary:** osonCafe Hub ecosystem.
- **Actorlar:** OWNER, MANAGER, CASHIER, WAITER, oshxona xodimi, texnik xodim, mijoz.
- **Ichki client’lar:** POS, Admin, TV; markazda Hub va SQLite.
- **Tashqi obyektlar:** printer va ixtiyoriy future cloud.
- **Muhim belgi:** internet majburiy emas; future cloud uzilgan chiziqda.

### D02 — Use Case

- Actor generalization emas, real rollar ko‘rsatiladi.
- Use case guruhlari: Authentication & Devices, Menu, Orders, Payments, Shifts, Reports, Operations.
- `Refund` va `Discount beyond limit` use case’lari `Manager approval`ni include/extend qiladi.
- `Print receipt` va `Admin analytics` yonida Partial status belgisi bo‘ladi.

### D03 — Domain Class

- Aggregate’lar: Identity, Catalog, Sales, Operations, Reporting/Audit.
- Asosiy relation’lar: Business→Branch→User/Device/Shift/Order; Product→Variant; Order→Item→Modifier; Order→Payment; Shift→CashMovement/ZReport.
- Money value object integer minor unit sifatida qayd etiladi.
- Enum’lar: Role, OrderStatus, PaymentMethod/Status, ShiftStatus, PrintJobStatus.

### D04 — Detailed Model

- Controller DTO’dan domain service input’iga mapping ko‘rsatiladi.
- Prisma model, domain object va response DTO bir xil narsa emasligi ajratiladi.
- Tenant/branch scope, audit metadata, timestamps va soft/active flags ko‘rsatiladi.
- Secret hash va token’lar response DTO’dan chiqarib tashlanadi.

### D05 — Controller–Service–Repository–API

- Request oqimi: Route → validation/Zod → authorization → service → Prisma transaction → response.
- Cross-cutting: idempotency, audit, structured logging, error mapping.
- Client total yoki role’ga ishonilmasligi server validation blokida belgilanadi.
- Print/backup kabi operational adapter’lar alohida interface orqali ko‘rsatiladi.

## Sequence diagrammalar

### D06 — PIN Login & Session

Lifeline’lar: User, POS, Hub/Auth controller, Rate limiter, User repository, Argon2 verifier, Session store, Audit log. Oqim: device check → PIN lookup/verify → lockout decision → opaque session → role-scoped response. Invalid, locked va revoked alternativlari mavjud.

### D07 — Create Order

Lifeline’lar: Staff, POS, Order API, Auth policy, Menu/Stop-list service, Pricing service, Order repository, Counter, Audit. Server price/availability’ni qayta tekshiradi; transaction ichida order number, items va totals saqlanadi; idempotent replay alternativ oqimda.

### D08 — Kitchen Flow

Lifeline’lar: POS, Order service, PrintJob service, Printer adapter, Kitchen/TV, Staff. Confirm → kitchen ticket job → preparing → ready → completed. Printer offline/retry **Partial** sifatida belgilanadi; order state print muvaffaqiyatiga noto‘g‘ri bog‘lanmaydi.

### D09 — Payment

Lifeline’lar: CASHIER, POS, Payment API, Order service, Idempotency store, Payment repository, Receipt service, Audit. Total validation → payment parts → transaction → order completion → receipt job. Duplicate key, under/overpayment va failure rollback alternativlari.

### D10 — Shift Close & Z-report

Lifeline’lar: MANAGER/CASHIER, POS, Shift API, Order/Payment repository, CashMovement repository, Report service, Audit. Open order check → totals → actual cash → difference → closed shift/ZReport. Parallel close va new-sale-after-close rad etiladi.

### D11 — Cancel / Refund / Approval

Lifeline’lar: CASHIER, MANAGER, POS, Approval policy, Order/Payment service, Audit. Order status va amount bo‘yicha approval qarori; sabab majburiy; refund asl payment’ga reference qiladi; unauthorized va already-refunded alternativlari.

## Activity diagrammalar

### D12 — Order Activity

Swimlane’lar: Staff, POS, Hub. Login/shift check → menu → item/variant/modifier → stop-list va price validation → draft → confirm. Validation failure loop’i va cancel exit’i mavjud.

### D13 — Preparation Activity

Swimlane’lar: Hub, Printer/Kitchen, Staff, TV. Confirmed order → ticket/queue → preparing → ready → handoff → completed. Printer failure parallel exception sifatida, state machine’ni soxtalashtirmasdan ko‘rsatiladi.

### D14 — Payment Activity

Swimlane’lar: CASHIER, POS, Hub. Method/parts → amount validation → transaction → receipt job → success. Split payment loop’i, duplicate idempotency va refund branch’i mavjud.

### D15 — Shift Activity

Swimlane’lar: MANAGER/CASHIER, Hub. No active shift → open → sales/cash movement loop → reconcile → close → Z-report. Open order va difference acknowledgement decision node’lari.

## State machine diagrammalar

### D16 — Order State Machine

State’lar: Draft → Confirmed → Preparing → Ready → Completed. Cancelled terminal state’iga faqat ruxsat etilgan holatlardan o‘tish. Completed’dan oddiy edit/cancel yo‘q; refund alohida moliyaviy oqim.

### D17 — Payment/Session State Machine

Ikki region: Payment (`Pending → Succeeded | Failed`, `Succeeded → PartiallyRefunded → Refunded`) va Session (`Active → Locked/Expired/Revoked`). Guard va trigger’lar aniq yoziladi.

### D18 — Shift State Machine

State’lar: Closed/None → Open → Closing → Closed. Open guard: boshqa aktiv shift yo‘q. Closing guard: reconciliation yakunlangan. Invalid parallel transition rad etiladi.

## Data va komponent diagrammalari

### D19 — Database ERD

30 ta joriy model besh rangli domain guruhiga ajratiladi: core/identity, catalog, sales, operations, security/audit. PK/FK, cardinality va muhim unique constraint’lar ko‘rsatiladi. PDF’dagi 8 obyektli konseptual ERD bilan almashtirilmaydi.

### D20 — Software Components

Client’lar: POS React/Vite, Admin React/Vite, TV web. Hub’da auth, menu, order, payment, shift, reporting, settings, backup, print va audit modullari. Infrastructure: Express, Prisma, SQLite, filesystem/printer adapters. Admin real aggregation gap’i Partial badge bilan.

## Arxitektura va deployment

### D21 — Current Modular Monolith

Bitta process ichidagi modul chegaralari, bitta SQLite database va lokal client’lar ko‘rsatiladi. Tashqi internetga critical dependency yo‘q. Module coupling faqat service/interface yo‘nalishida ko‘rsatiladi.

### D22 — Proposed Microservices

API Gateway ortida Identity, Catalog, Sales, Operations, Reporting; message broker va database-per-service. Migration birdaniga emas, modular boundary’dan bosqichma-bosqich extract qilish sifatida legend’da ko‘rsatiladi.

### D23 — Current Hub-only Deployment

Node’lar: Windows Hub host, SQLite/backup storage, LAN router, POS terminal, Admin device, TV display, printer. Protocol/port darajasida HTTP LAN va printer adapter ko‘rsatiladi. Internet optional; printer hardware validation Partial.

### D24 — Proposed Cloud Deployment

Branch edge Hub, secure sync channel, cloud gateway, service cluster, broker, databases, observability va backup. Offline queue/conflict handling proposed ekanligi aniq yoziladi.

## BPMN diagrammalar

### D25 — Order Lifecycle

Pool/lane’lar: Customer, Waiter/Cashier, POS/Hub, Kitchen. Start: customer order; tasks: capture, validate, confirm, prepare, ready, handoff; gateways: availability va cancellation; end: completed/cancelled.

### D26 — Payment & Receipt

Pool/lane’lar: Customer, Cashier, Hub, Payment/Printer adapter. Gateway: payment method/split; service task: validate/idempotent commit; boundary error: payment/print failure; compensation: refund. Receipt hardware step Partial.

### D27 — Shift & Reporting

Pool/lane’lar: Manager/Cashier, Hub, Owner. Open shift → sales/cash movements → close request → reconcile → Z-report → daily report. Admin aggregation step Partial; manager operational daily report Current.

## Ishlab chiqarishdan oldingi audit checklist

- Har bir diagrammada sarlavha, ID, Current/Partial/Proposed badge va legend bor.
- Arrow direction va cardinality ma’noli, kesishmalar minimal.
- Aktor va system boundary aralashmaydi.
- Sequence diagramda request/response va alt/opt fragment’lar mavjud.
- State diagramda terminal va invalid transition ko‘rsatilgan.
- BPMN’da event, task, gateway, pool/lane semantikasi to‘g‘ri.
- Barcha matn 100% zoom’da o‘qiladi va rang kontrasti kamida 4.5:1.
- `.drawio`, `.svg`, `.png` bir xil semantik versiyani ifodalaydi.
