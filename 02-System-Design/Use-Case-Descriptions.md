# Asosiy Use Case tavsiflari

## UC-01 — Qurilmani pairing qilish

| Maydon | Tavsif |
|---|---|
| Actor | OWNER yoki texnik xodim |
| Precondition | Hub ishga tushgan; yaroqli, muddati tugamagan pairing code mavjud |
| Main Flow | 1. Qurilmada pairing ekrani ochiladi. 2. Code Hub’ga yuboriladi. 3. Hub code, branch va device type’ni tekshiradi. 4. Device yaratiladi. 5. Scope’langan credential beriladi. 6. Code consumed qilinadi. |
| Alternative Flow | Code noto‘g‘ri, muddati tugagan yoki oldin ishlatilgan bo‘lsa pairing rad etiladi va urinish audit qilinadi. |
| Postcondition | Qurilma aktiv va branch’ga bog‘langan; code qayta ishlamaydi. |
| Bog‘liq talab | FR-01, AC-01, D01/D02/D06 |

## UC-02 — PIN orqali kirish

| Maydon | Tavsif |
|---|---|
| Actor | MANAGER, CASHIER yoki WAITER |
| Precondition | Pairing qilingan aktiv qurilma va aktiv xodim mavjud |
| Main Flow | 1. Actor PIN kiritadi. 2. Hub rate limit va user scope’ni tekshiradi. 3. PIN argon2id hash bilan solishtiriladi. 4. Opaque server session yaratiladi. 5. Rolga mos POS route ochiladi. |
| Alternative Flow | Noto‘g‘ri PIN generic xato beradi; limitdan so‘ng vaqtinchalik lockout. Deaktiv user yoki revoked device rad etiladi. |
| Postcondition | Aktiv session va audit izi mavjud. |
| Bog‘liq talab | FR-02–FR-04, AC-02, D06/D17 |

## UC-03 — Smena ochish

| Maydon | Tavsif |
|---|---|
| Actor | MANAGER yoki CASHIER |
| Precondition | Actor login qilgan; branch’da aktiv smena yo‘q |
| Main Flow | 1. Opening cash kiritiladi. 2. Hub vakolat va branch lock’ni tekshiradi. 3. Shift `OPEN` holatida yaratiladi. 4. POS aktiv smena kontekstini oladi. |
| Alternative Flow | Parallel aktiv smena mavjud bo‘lsa conflict qaytariladi. Noto‘g‘ri summa yoki rol rad etiladi. |
| Postcondition | Bitta aktiv shift mavjud va keyingi order/payment shu shift’ga bog‘lanadi. |
| Bog‘liq talab | FR-07, AC-03, BR-01/02, D10/D15/D18 |

## UC-04 — Buyurtma yaratish

| Maydon | Tavsif |
|---|---|
| Actor | MANAGER, CASHIER yoki WAITER |
| Precondition | Aktiv session, device va shift; menyuda aktiv variant mavjud |
| Main Flow | 1. Item, variant, modifier, quantity va note tanlanadi. 2. Request idempotency key bilan yuboriladi. 3. Hub stop-list va narxni qayta tekshiradi. 4. Server total hisoblaydi. 5. Narx/name snapshot bilan order transaction saqlanadi. 6. Order number qaytariladi. |
| Alternative Flow | Stop-list, inactive item, soxta narx, invalid modifier yoki duplicate key alohida nazorat qilinadi. |
| Postcondition | Buyurtma item’lari, total va audit bilan saqlangan. |
| Bog‘liq talab | FR-05, FR-08/09/14/15, AC-04, D07/D12/D25 |

## UC-05 — To‘lovni qabul qilish

| Maydon | Tavsif |
|---|---|
| Actor | CASHIER yoki MANAGER |
| Precondition | Aktiv shift ichida payable order mavjud |
| Main Flow | 1. CASH/CARD/QR yoki split qismlar tanlanadi. 2. Hub method va summalarni tekshiradi. 3. Summa payable total’ga tengligi tekshiriladi. 4. Payment va order status atomic transaction’da yoziladi. 5. Receipt print job yaratiladi. |
| Alternative Flow | Under/overpayment, duplicate key, closed shift va invalid method rad etiladi. Printer xatosi payment commit’ni bekor qilmaydi, job retry holatiga o‘tadi. |
| Postcondition | Payment persisted, order paid/completed; receipt job Partial hardware statusida. |
| Bog‘liq talab | FR-12/13, AC-05/06/12, D09/D14/D17/D26 |

## UC-06 — Cancel yoki refund

| Maydon | Tavsif |
|---|---|
| Actor | CASHIER so‘rovchi; MANAGER tasdiqlovchi |
| Precondition | Order/payment mavjud; holat revers operatsiyaga ruxsat beradi |
| Main Flow | 1. Sabab kiritiladi. 2. Policy status, rol va limitni tekshiradi. 3. Zarur bo‘lsa manager approval olinadi. 4. Refund asl payment’ga bog‘lanadi. 5. Audit yoziladi. |
| Alternative Flow | Unauthorized, already-refunded, invalid transition yoki ortiqcha summa rad etiladi. |
| Postcondition | Reversal traceable; tarixiy order tahrirlanmagan. |
| Bog‘liq talab | FR-16–FR-18, AC-07, D11/D16/D17/D26 |

## UC-07 — Smenani yopish va Z-report

| Maydon | Tavsif |
|---|---|
| Actor | MANAGER yoki vakolatli CASHIER |
| Precondition | Aktiv shift mavjud; actor login qilgan |
| Main Flow | 1. Open order va cash movement’lar tekshiriladi. 2. Expected cash hisoblanadi. 3. Actual cash kiritiladi. 4. Difference aniqlanadi. 5. Shift closed qilinadi va Z-report yaratiladi. |
| Alternative Flow | Reconciliation tugamasa yoki parallel close bo‘lsa operatsiya rad etiladi. Kassa farqi manager acknowledgement talab qilishi mumkin. |
| Postcondition | Shift immutable closed state’da; Z-report va audit mavjud. |
| Bog‘liq talab | FR-19–FR-21, AC-08, D10/D15/D18/D27 |

## UC-08 — Backup va restore

| Maydon | Tavsif |
|---|---|
| Actor | OWNER yoki texnik xodim |
| Precondition | Hub database mavjud; actor vakolatli |
| Main Flow | 1. On-demand backup yaratiladi. 2. Archive yaxlitligi tekshiriladi. 3. Restore so‘ralganda joriy DB safety backup qilinadi. 4. Tanlangan archive restore qilinadi. 5. Health va business read tekshiriladi. |
| Alternative Flow | Invalid archive, insufficient space yoki health failure’da restore to‘xtaydi va rollback/safety backup saqlanadi. |
| Postcondition | Tekshirilgan backup yoki tiklangan Hub holati mavjud. |
| Bog‘liq talab | FR-25, AC-09, BR-20, D20/D23 |
