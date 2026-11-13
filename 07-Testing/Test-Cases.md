# Test Cases

Statuslar: **PASS** — real automated yoki mavjud smoke dalili; **NOT RUN** — kerakli muhit/hardware’da bajarilmagan.

| Test ID | Requirement | Description | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|---|
| TC-01 | FR-01, BR-14 | Pairing code bir martalik | Hub, valid code | Code bilan pair; shu code’ni qayta yuborish | Birinchi request device yaratadi; replay rad | Hub auth testlari pairing va re-pair lifecycle’ni tasdiqladi | PASS |
| TC-02 | FR-02, NFR-05 | PIN login va lockout | Active user/device | 5 noto‘g‘ri PIN; to‘g‘ri PIN; lock vaqtini tekshirish | 5 urinishdan keyin lock; raw PIN log’da yo‘q | Auth HTTP testlari restartdan keyingi persisted lockout bilan o‘tdi | PASS |
| TC-03 | FR-03/04 | OWNER password change/session revoke | Temporary owner password | Login; password change; revoke/deactivate | Majburiy change; eski session rad | Owner auth/session testlari o‘tdi | PASS |
| TC-04 | NFR-02, BR-11 | Tenant/branch isolation | Ikki tenant fixture | Boshqa branch session/entity bilan request | Foreign data qaytmaydi; 403/404 | Cross-tenant auth/order tests o‘tdi | PASS |
| TC-05 | FR-05/15 | Menu va stop-list | Active menu variant | Menu read; stop-list add; qayta order tanlash | Stop item sotilmaydi; audit yoziladi | Menu HTTP/repository testlari o‘tdi | PASS |
| TC-06 | FR-07, BR-01 | Bitta aktiv shift | Branch’da shift yo‘q | Ikki parallel open request | Faqat bitta shift OPEN | Shift invariant testlari o‘tdi | PASS |
| TC-07 | FR-08/09, BR-03 | Order snapshot va server total | Active shift/menu | Client soxta price yuboradi; valid request yuboradi | Soxta price rad; valid price snapshot saqlanadi | Order HTTP suite forged/stale price holatlarini o‘tkazdi | PASS |
| TC-08 | FR-08, NFR-04 | Order idempotency | Unique client request ID | Bir xil payload/key ikki marta | Bitta order; bir xil result | Replay va key conflict testlari o‘tdi | PASS |
| TC-09 | FR-11, BR-18 | Order state transition | Confirmed order | Invalid va valid transition yuborish | Invalid 409; valid state audit bilan o‘tadi | Order/status suites o‘tdi | PASS |
| TC-10 | FR-12, BR-06 | Cash/card/QR/split payment | Payable order | Split parts totalini teng va noto‘g‘ri yuborish | Faqat exact total commit qilinadi | Payment/domain/UI suites o‘tdi | PASS |
| TC-11 | FR-12, NFR-04 | Payment replay | Completed payment key | Shu key bilan request replay | Duplicate payment yaratilmaydi | Payment idempotency tests o‘tdi | PASS |
| TC-12 | FR-16–18 | Cancel/refund va manager approval | Sent/paid order | Sabab, approval, wrong PIN, replay | Vakolat/limit guard; refund asl payment’ga bog‘lanadi | Void/refund HTTP suite va POS flow o‘tdi | PASS |
| TC-13 | FR-19/20 | Shift close/Z-report | Open shift, sales, cash movement | Actual cash bilan close | Expected/actual/difference va Z-report atomic | Shift-close suite audit rollback holati bilan o‘tdi | PASS |
| TC-14 | FR-21 | Daily operational report | Bugungi sales fixture | Daily report endpoint/UI | Gross, methods, VOID/refund/net mos | Daily report HTTP testlari o‘tdi | PASS |
| TC-15 | FR-22 | TV queue/token | Valid TV token | Token rotate/revoke; queue polling | Old token rad; minimal read scope | Auth/TV/POS tests o‘tdi | PASS |
| TC-16 | FR-25, BR-20 | Backup/restore safety | Isolated test DB | Export; staged restore; invalid archive | Valid round-trip; traversal/unsafe archive rad | Backup-admin va DB backup testlari o‘tdi | PASS |
| TC-17 | NFR-12/13 | Responsive/accessibility | UI fixture | 360/390/768 va keyboard/touch audit | No horizontal scroll; core target ≥44 px | Mavjud final visual report: 95/95 | PASS |
| TC-18 | FR-10/13, NFR-15 | Fizik printer E2E | Supported ESC/POS printer | Kitchen/receipt print; offline; retry; duplicate | To‘g‘ri chop; retry va duplicate nazorati | Real printer ushbu auditda ulanmagan | NOT RUN |
| TC-19 | NFR-07 | p95 API performance | Pilot hardware/load script | Typical read/write load | p95 ≤500 ms target | Reproducible benchmark bajarilmadi | NOT RUN |
| TC-20 | FR-28 | Admin real aggregation | Real aggregate endpoints | Dashboard/Reports’ni DB facts bilan solishtirish | Demo/static emas; totals DB bilan teng | UI mavjud, endpoint integration to‘liq tasdiqlanmagan | NOT RUN |

## Automated suite mapping

| Package/suite | Test file | Test | Natija |
|---|---:|---:|---|
| Invariant script | 1 | 153 | PASS |
| Domain | 9 | 112 | PASS |
| Shared types | 10 | 150 | PASS |
| POS Web | 174 | 617 | PASS |
| Admin Web | 37 | 230 | PASS |
| Hub | 38 | 518 | PASS |
| **Jami** | **269** | **1,780** | **PASS** |
