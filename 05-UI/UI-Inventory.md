# UI inventarizatsiyasi

## POS route’lari

| Route | Vazifa | Holat |
|---|---|---|
| `/pair`, `/pairing` | Qurilmani Hub bilan pairing qilish | Implemented |
| `/pin` | Xodim PIN login | Implemented |
| `/lock` | Session lock/unlock | Implemented |
| `/pos` | Menyu va buyurtma tuzish | Implemented |
| `/orders` | Buyurtmalar ro‘yxati va holati | Implemented |
| `/payment` | Payment/split payment | Implemented |
| `/stoplist` | Mavjud bo‘lmagan item’lar | Implemented |
| `/shift` | Smena ochish/yopish | Implemented |
| `/daily` | Operatsion kunlik hisobot | Implemented |
| `/tv` | Buyurtma navbati/tayyor holati | Implemented |

## Admin route’lari

| Route | Vazifa | Holat |
|---|---|---|
| `/admin/login` | OWNER login | Implemented |
| `/admin/change-password` | Majburiy parol almashtirish | Implemented |
| `/admin` / `/admin/dashboard` | Dashboard | Partial — real aggregation tekshiruvi kerak |
| `/admin/menu` | Menu boshqaruvi | Implemented |
| `/admin/employees` | Xodimlar boshqaruvi | Implemented |
| `/admin/reports` | Hisobotlar | Partial — real aggregation tekshiruvi kerak |
| `/admin/settings` | Biznes, qurilma va tizim sozlamalari | Implemented |

## UI sifat mezonlari

- 375, 768, 1024 va 1440 px breakpointlarda kritik oqimlar ishlaydi.
- Normal matn kontrasti kamida 4.5:1.
- Keyboard focus ko‘rinadi; dialog focus trap va Escape bilan yopilishni qo‘llaydi.
- Touch target kamida 44×44 px.
- Loading, empty, validation, offline va recoverable error holatlari ko‘rsatiladi.
- Demo/static ko‘rsatkich real business ma’lumoti sifatida taqdim etilmaydi.
- Money, vaqt va status formatlari barcha ekranlarda bir xil.
