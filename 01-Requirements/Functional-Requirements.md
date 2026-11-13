# Funksional talablar

## Holat belgisi

- **Implemented** — joriy `integration/v1` dalili mavjud.
- **Partial** — qisman mavjud yoki tashqi/fizik tekshiruv kerak.
- **Proposed** — kelajak scope’i; joriy pilot va’dasi emas.

| ID | Talab | Asosiy aktor | Holat | Prioritet |
|---|---|---|---|---|
| FR-01 | Tizim yangi POS/Admin/TV qurilmasini bir martalik pairing code orqali ro‘yxatdan o‘tkazishi kerak. | Texnik xodim, OWNER | Implemented | Must |
| FR-02 | Xodim POS’ga shaxsiy PIN orqali kirishi, noto‘g‘ri urinishlar esa cheklanishi kerak. | MANAGER, CASHIER, WAITER | Implemented | Must |
| FR-03 | OWNER Admin panelga login/parol bilan kirishi va majburiy password change holati qo‘llanishi kerak. | OWNER | Implemented | Must |
| FR-04 | Session yaratish, lock, revoke va expiry holatlari server tomonidan boshqarilishi kerak. | Barcha foydalanuvchilar | Implemented | Must |
| FR-05 | POS aktiv kategoriya, mahsulot, variant, modifier, narx va mavjudlikni ko‘rsatishi kerak. | MANAGER, CASHIER, WAITER | Implemented | Must |
| FR-06 | OWNER menyu kategoriya, mahsulot, variant, modifier group va modifier’larni boshqarishi kerak. | OWNER | Implemented | Must |
| FR-07 | Savdo boshlanishidan oldin vakolatli xodim opening cash bilan smena ochishi kerak. | MANAGER, CASHIER | Implemented | Must |
| FR-08 | Xodim buyurtma yaratishi, item qo‘shishi/o‘chirishi, miqdor va izohni o‘zgartirishi kerak. | MANAGER, CASHIER, WAITER | Implemented | Must |
| FR-09 | Buyurtma item’i variant, modifier va maxsus izohni saqlashi, narx snapshot’ini muzlatishi kerak. | POS, Hub | Implemented | Must |
| FR-10 | Tasdiqlangan buyurtma oshxona/print job navbatiga yuborilishi kerak. | CASHIER, Hub | Partial | Must |
| FR-11 | Buyurtma draft, confirmed, preparing, ready, completed va cancelled holatlari bo‘yicha boshqarilishi kerak. | POS, oshxona | Implemented | Must |
| FR-12 | Tizim naqd, karta, QR va split payment’ni qabul qilishi hamda to‘lov yig‘indisini tekshirishi kerak. | CASHIER | Implemented | Must |
| FR-13 | Muvaffaqiyatli to‘lovdan so‘ng receipt ma’lumoti va print job yaratilishi kerak. | CASHIER, Hub | Partial | Should |
| FR-14 | Vakolatli rol chegirmani belgilangan limit va audit talabi bilan qo‘llashi kerak. | MANAGER, CASHIER | Implemented | Should |
| FR-15 | MANAGER vaqtincha mavjud bo‘lmagan variant/modifier’ni stop-listga qo‘shishi va olib tashlashi kerak. | MANAGER | Implemented | Must |
| FR-16 | Buyurtma holatiga mos ravishda cancel sababi va vakolat tekshiruvi bilan bekor qilinishi kerak. | MANAGER, CASHIER | Implemented | Must |
| FR-17 | Yakunlangan savdo refund/void qilinsa, asl operatsiyaga bog‘lanishi, sabab va tasdiqlovchi saqlanishi kerak. | MANAGER | Implemented | Must |
| FR-18 | Limitdan tashqari yoki xavfli operatsiya manager approval talab qilishi kerak. | MANAGER | Implemented | Must |
| FR-19 | Smena davomida cash-in/cash-out operatsiyalari sabab va foydalanuvchi bilan qayd etilishi kerak. | MANAGER, CASHIER | Implemented | Must |
| FR-20 | Smena yopilganda expected/actual cash, farq va Z-report qayd etilishi kerak. | MANAGER, CASHIER | Implemented | Must |
| FR-21 | Vakolatli rol kunlik savdo, to‘lov turi, refund va smena natijalarini ko‘rishi kerak. | MANAGER, OWNER | Implemented | Must |
| FR-22 | TV ekran aktiv buyurtmalarni polling orqali olib, tayyor bo‘lgan order’larni ko‘rsatishi kerak. | Mijoz, oshxona | Implemented | Should |
| FR-23 | OWNER xodim yaratishi, rol biriktirishi, PIN reset qilishi va aktivligini boshqarishi kerak. | OWNER | Implemented | Must |
| FR-24 | OWNER biznes, branch, printer, qurilma va xavfsizlik sozlamalarini boshqarishi kerak. | OWNER | Implemented | Should |
| FR-25 | Texnik/owner foydalanuvchi database backup yaratishi va nazoratli restore jarayonini bajarishi kerak. | OWNER, texnik xodim | Implemented | Must |
| FR-26 | Tizim autentifikatsiya, menyu, buyurtma, to‘lov, smena va sozlama o‘zgarishlarini audit log’da qayd etishi kerak. | Hub, auditor | Implemented | Must |
| FR-27 | Hub Windows’da installer, service/autostart va lokal URL’lar bilan ishga tushirilishi kerak. | Texnik xodim | Implemented | Should |
| FR-28 | Admin Dashboard va Reports real Hub aggregation endpoint’laridan ma’lumot olishi kerak. | OWNER | Partial | Should |
| FR-29 | Kelajakda cloud markaz bir nechta branch ma’lumotini xavfsiz sinxronlashtirishi kerak. | OWNER, cloud service | Proposed | Could |
| FR-30 | Kelajakda Identity, Catalog, Sales, Operations va Reporting mustaqil service sifatida ajratilishi kerak. | Platform team | Proposed | Could |

## Scope qoidasi

FR-29 va FR-30 akademik evolyutsiya dizayniga kiradi, ammo joriy pilotning acceptance mezonini bloklamaydi. FR-10, FR-13 va FR-28 public taqdimotda tugallangan imkoniyat sifatida ko‘rsatilmaydi.
