# Frontend Architecture

## POS va Admin

- React 19 + Vite.
- React Router orqali route-based screen composition.
- TanStack Query orqali server state/cache.
- Zustand orqali lokal UI/cart/bootstrap state.
- Shared API DTO va enum’lar `shared-types` contract’iga tayanadi.
- Lucide SVG icon’lari; emoji structural icon sifatida ishlatilmaydi.
- i18next integratsiyasi text layer’ni UI logic’dan ajratadi.

## State ownership

| State | Owner |
|---|---|
| Order/payment/shift truth | Hub database va API |
| Query cache | TanStack Query |
| Savat draft’i | POS local store; submit’da Hub qayta validatsiya qiladi |
| Session/role | Hub opaque session response |
| UI modal/filter | Screen/component local state |
| TV queue | Periodic Hub polling |

## Resilience

- Loading, empty, error va retry holatlari alohida.
- Route guard role va session’ga mos redirect qiladi.
- Network/HUB xatosi foydalanuvchiga action bilan tushuntiriladi.
- Duplicate submit idempotency key bilan himoyalanadi; button loading paytida disabled.
