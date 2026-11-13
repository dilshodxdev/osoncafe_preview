# SDLC rejalashtirish

## Yondashuv

Loyiha iterativ SDLC asosida hujjatlashtiriladi. Joriy implementation qayta yozilmaydi; avval dalillar muzlatiladi, so‘ng talablar, dizayn va test natijalari orasida traceability o‘rnatiladi.

| Bosqich | Asosiy natija | Sifat darvozasi |
|---|---|---|
| 1. Evidence freeze | Manbalar va branch holatlari manifesti | Har bir fakt manbaga bog‘langan |
| 2. Requirements | FR, NFR, US, BR, AC va RTM | ID’lar yagona, ziddiyatlar qayd etilgan |
| 3. System design | Current/proposed arxitektura va DB modeli | Joriy va kelajak holati aralashmagan |
| 4. Diagram production | 27 diagramma, 81 fayl | Complete — Draw.io CLI export va visual QA |
| 5. UI/Implementation | Ekranlar va implementatsiya dalillari | Fake screen real funksiya sifatida ko‘rsatilmagan |
| 6. Testing | Test strategiyasi va natijalar | Complete — 1,780 automated PASS; hardware/performance gap ochiq |
| 7. Packaging | README, SDLC, PDF va ZIP | Link, format, imlo va maxfiylik auditi |
| 8. Release | Public repository’ga push | Faqat foydalanuvchining yakuniy tasdig‘i bilan |

## Definition of Done

Repository quyidagilar bajarilganda akademik preview sifatida tayyor hisoblanadi:

- barcha talablar noyob ID va acceptance criteria’ga ega;
- barcha kritik FR kamida bitta diagramma va test daliliga bog‘langan;
- 27 diagrammaning tahrirlanadigan va eksport formatlari mavjud;
- implementation, partial va proposed holatlari aniq ajratilgan;
- Markdown linklari va diagramma yo‘llari tekshirilgan;
- public fayllarda secret yoki shaxsiy email yo‘q;
- PDF titulidagi guruh raqami yakuniy tasdiqlangan;
- GitHub push uchun alohida final approval olingan.
