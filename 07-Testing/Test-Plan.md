# Test Plan

## Maqsad

osonCafe’ning domain qoidalari, API contract, tenant/role xavfsizligi, UI oqimlari, deployment va recovery xususiyatlarini tekshirish. Test natijasi faqat real command, mavjud CI/smoke dalili yoki aniq `NOT RUN` statusiga asoslanadi.

## Scope

### In scope

- invariants, unit, contract va integration testlar;
- Hub HTTP va real SQLite testlari;
- POS/Admin component va responsive testlari;
- build, typecheck, lint, format check;
- mavjud smoke/visual dalillar;
- requirements traceability.

### Alohida muhit talab qiladi

- real ESC/POS printer;
- pilot Windows installer/service smoke;
- p95 performance benchmark;
- productionga o‘xshash Admin aggregation E2E;
- disaster recovery vaqtini o‘lchash.

## Muhit

| Element | Qiymat |
|---|---|
| Audit sana | 2026-11-13 |
| Node.js | 22.22.0 |
| pnpm | 10.18.3 |
| OS | Windows |
| Database | Test isolation’dagi SQLite |
| Branch | Audit qilingan pilot implementation branch |

## Entry criteria

- Dependency lockfile o‘zgarmagan.
- Private source faqat read-only audit clone’da.
- Secret yoki production database ishlatilmaydi.
- Node/pnpm repository engine talabiga mos.

## Exit criteria

- Check, automated test va build exit code 0.
- 0 failed automated test.
- Critical FR test case bilan bog‘langan.
- Bajarilmagan hardware/performance test `NOT RUN`.
- Known limitation README, Test Report va Audit’da bir xil.

## Severity

| Daraja | Ta’rif |
|---|---|
| Blocker | Moliyaviy xato, tenant leak, auth bypass yoki data loss |
| High | Critical flow ishlamaydi, idempotency/audit buziladi |
| Medium | Recovery, responsive yoki non-critical flow nuqsoni |
| Low | Kosmetik/imlo va workaround mavjud muammo |
