# Test strategiyasi va dalillar

## Test piramidasi

| Daraja | Maqsad | Misollar |
|---|---|---|
| Unit | Hisob, guard va state transition’ni izolyatsiyada tekshirish | Money total, role rule, status transition |
| Integration | Hub + Prisma + SQLite va HTTP boundary | Auth, menu, order, payment, shift, backup |
| Invariant | Cross-module business qoidalarini himoya qilish | Tenant scope, idempotency, bitta aktiv shift |
| UI/Responsive | POS/Admin route va viewport holatlari | Core flow, 375–1440 px |
| Smoke/E2E | Real deploymentga yaqin kritik yo‘l | Pair → login → shift → order → payment → close |
| Hardware | Fizik periferiyani tekshirish | Receipt/kitchen printer |

## Audit qilingan mavjud dalillar

- 2026-11-13 lokal read-only audit: invariant scan, typecheck, lint, format check, 1,780 automated test va production build PASS.
- Invariant scan 434 source file’ni tekshirdi; automated suite 269 test file’da 0 failure bilan yakunlandi.
- Production-smoke real business flow muvaffaqiyatli qayd etilgan.
- Alohida smoke suite’da 18/18 natija qayd etilgan.
- UI/responsive hisobotida 95/95 (32 core + 63 responsive) natija qayd etilgan.

18/18 smoke va 95/95 UI/responsive natijalari mavjud hisobot dalili. 1,780 automated test esa ushbu public hujjat tayyorlanayotgan paytda qayta ishga tushirildi.

## Ma’lum bo‘shliqlar

| Gap | Risk | Yopish mezoni |
|---|---|---|
| Fizik Xprinter E2E yo‘q | Receipt/ticket real muhitda ishlamasligi mumkin | Qo‘llab-quvvatlangan modelda print/retry/duplicate testi |
| Admin aggregation to‘liq emas | Dashboard demo yoki stale ma’lumot ko‘rsatishi mumkin | Real Hub API bilan AC-11 E2E |
| Performance target benchmark’i yo‘q | 500 ms p95 target tasdiqlanmagan | Pilot hardware’da reproducible load report |
| Production disaster-recovery time drill yo‘q | RTO/RPO real hardware’da noma’lum | Fresh production-like restore + health + business read + elapsed time |

## Release quality gate

1. Typecheck, lint, format check va build — pass.
2. Unit/integration/invariant test — pass.
3. Critical smoke flow — pass.
4. Secret/PII scan — clean.
5. Markdown link va diagram export audit — pass.
6. Known limitation’lar README/PDF’da bir xil ko‘rsatilgan.
7. Fizik sinovsiz printer “Implemented”ga ko‘tarilmaydi.
