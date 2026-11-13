# Test Report

## Yakuniy natija

Audit qilingan private implementation branch’ida 2026-11-13 kuni clean dependency install’dan so‘ng lokal command’lar bajarildi.

| Tekshiruv | Natija | Dalil |
|---|---|---|
| Invariant scan | PASS | 434 source file; invariant script OK |
| Typecheck | PASS | Domain, shared types, Hub, POS, Admin |
| Lint | PASS | `--max-warnings 0` |
| Format check | PASS | Prettier check |
| Automated tests | PASS | 269 test file; 1,780 passed; 0 failed |
| Production build | PASS | Domain, shared types, Hub, POS, Admin |
| Existing browser smoke | PASS | 18/18 audit qilingan hisobot |
| Existing visual/responsive | PASS | 95/95 audit qilingan hisobot |
| Physical printer | NOT RUN | Hardware ulanmagan |
| Performance benchmark | NOT RUN | Reproducible pilot hardware/load run yo‘q |
| Admin real aggregation E2E | NOT RUN | Integration to‘liq tasdiqlanmagan |

## Automated test taqsimoti

- Invariants: 153.
- Domain: 112.
- Shared types/contracts: 150.
- POS Web: 617.
- Admin Web: 230.
- Hub/API/SQLite: 518.
- Jami: **1,780 passed, 0 failed**.

## Warninglar

1. Ayrim React tests stderr’da test environment `act(...)` warning chiqardi; suite exit code 0 va barcha assertion pass. Bu test harness cleanup sifatida kuzatiladi.
2. Vite build POS/Admin bundle’lari 500 kB’dan katta ekanini ogohlantirdi. Build muvaffaqiyatli, ammo route-level code splitting performance qarzi sifatida qayd etildi.
3. Printer worker/hardware real qurilmada tekshirilmagan; receipt/kitchen funksiyasi Partial.
4. Admin Dashboard/Reports UI mavjud, real aggregate endpoint bilan to‘liq E2E dalil yo‘q; Partial.

## Xulosa

Joriy Hub-only pilotning domain, contract, API, SQLite, POS/Admin UI va build bazasi avtomatik testlar bo‘yicha barqaror. Release claim printer, performance va Admin aggregation cheklovlarini yashirmasligi kerak.
