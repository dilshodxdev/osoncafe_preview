# Dalillar manifesti

## Maqsad

Bu fayl hujjatlardagi xulosalar qaysi manbaga tayanganini ko‘rsatadi. Public repository private kodni ko‘chirmaydi; faqat audit qilingan faktlarning umumlashtirilgan natijasini beradi.

| ID | Manba | Audit qilingan qism | Hujjatlarda qo‘llanishi |
|---|---|---|---|
| EV-01 | Private implementation repository, `integration/v1`, read-only audit | Pilot arxitekturasi, route’lar, Prisma schema, UI va testlar | Implemented/Partial holatlari, current architecture, ERD |
| EV-02 | Private implementationdagi cloud evolution materiallari | Cloud/hybrid yo‘nalishidagi keyingi ishlar | Proposed evolyutsiya konteksti |
| EV-03 | osonCafe PRD | F01–F14, rollar, oqimlar, state machine va biznes qoidalar | Requirements, UML/BPMN semantikasi |
| EV-04 | ADR-001…ADR-005 | ORM, arxitektura, Hub-only pilot, session token va Argon2id | Architecture Decision Record sharhi |
| EV-05 | 2026-11-13 lokal production audit | 434 source file invariant scan; typecheck/lint/format; 269 test file va 1780/0; Hub/POS/Admin/domain/shared build | Test Report va release audit |
| EV-06 | Mavjud arxitektura PDF’i | Joriy modular monolith, proposed microservices, UI va deployment materiallari | Arxitektura taqqoslash va diagramma scope’i |
| EV-07 | `dr-dilshod/SDLCExample` va Wiki | O‘qituvchi namunasi strukturasi va topshiriq kutilmalari | SDLC bo‘limlari va taqdimot tartibi |
| EV-08 | [osoncafe.uz](https://osoncafe.uz) | Mahsulotning ommaviy pozitsiyalanishi | Loyiha konteksti |
| EV-09 | `04-Diagrams/` eksportlari | 27 Draw.io manbasi, 27 SVG, 27 PNG va vizual QA | UML/BPMN/ERD/architecture ilovalari |
| EV-10 | `05-UI/screenshots/` | 12 public-safe fixture screenshot | UI evidence va PDF ilovasi |
| EV-11 | Yakuniy PDF render auditi | 50/50 sahifa Poppler bilan render qilindi va contact-sheet orqali ko‘rildi | `Documentation/osonCafe-SDLC-Architecture.pdf` |

## Audit qoidalari

1. Implemented holati faqat kod, test yoki ishlaydigan route bilan tasdiqlansa beriladi.
2. Fizik qurilma talab qiladigan printer integratsiyasi to‘liq sinov dalilisiz **Partial** deb belgilanadi.
3. Besh xizmatli microservices modeli **Proposed** bo‘lib, joriy pilot sifatida ko‘rsatilmaydi.
4. Eski PDF’dagi 8 obyektli ERD konseptual; joriy implementation uchun Prisma’dagi 30 model asosiy dalildir.
5. Private repositorydan maxfiy qiymatlar, shaxsiy ma’lumotlar va to‘liq manba kodi public repositoryga ko‘chirilmaydi.

## Aniqlashtirilgan nomuvofiqliklar

| Mavzu | Manbalardagi holat | Qabul qilingan yechim |
|---|---|---|
| Guruh raqami | Birlamchi topshiriqda `S941-23Di`, eski PDF nomi va titulida `S942-23Di` | Barcha yakuniy public hujjat va yangi PDF’da `S941-23Di` |
| Printer | Arxitektura materialida mavjud, fizik qurilma to‘liq tekshirilmagan | `Partial` |
| Admin Dashboard/Reports | UI mavjud, real aggregation API’ga ulanish to‘liq emas | `Partial` |
| Arxitektura | Joriy modular monolith va kelajak microservices birga ko‘rsatilgan | Alohida `Current` va `Proposed` diagrammalar |

