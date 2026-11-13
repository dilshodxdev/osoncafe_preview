# Loyiha tavsifi

## Muammo

Kafe va kichik restoranlarda buyurtma, kassa, oshxona, smena va hisobot jarayonlari ko‘pincha alohida vositalar yoki qo‘lda yuritiladi. Internet uzilishi, qurilma almashishi va xodim rollarining noto‘g‘ri boshqarilishi xizmat tezligi hamda moliyaviy nazoratga salbiy ta’sir qiladi.

## Yechim

osonCafe — lokal tarmoqda ishlaydigan, bitta Hub server orqali POS, Admin va TV interfeyslarini taqdim etadigan restoran boshqaruv tizimi. Joriy pilot **Hub-only modular monolith**; kelajakda markaziy cloud va microservices evolyutsiyasi alohida **Proposed** arxitektura sifatida ko‘rsatiladi.

## Stakeholderlar

| Stakeholder | Ehtiyoj |
|---|---|
| Biznes egasi (OWNER) | Menyu, xodim, qurilma, sozlama va umumiy nazorat |
| Menejer (MANAGER) | Smena, stop-list, bekor qilish, kunlik hisobot va tasdiqlar |
| Kassir (CASHIER) | Buyurtma, to‘lov, chek, kassa kirim-chiqimi |
| Ofitsiant (WAITER) | Tez buyurtma yaratish va holatini kuzatish |
| Oshxona xodimi | Tayyorlanadigan buyurtmalarni aniq navbatda ko‘rish |
| Administrator/texnik xodim | Hub, backup, qurilma pairing va diagnostika |
| Mijoz | To‘g‘ri buyurtma, tez xizmat va tushunarli hisob |

## Scope

### In scope — joriy pilot

- xodim PIN autentifikatsiyasi va owner login;
- device pairing va session boshqaruvi;
- menyu, variant, modifier va stop-list;
- buyurtma lifecycle’i;
- naqd, karta, QR va split payment;
- smena, cash movement, Z-report va kunlik hisobot;
- TV queue va lokal tarmoqda offline ishlash;
- audit log, backup/restore va Windows deployment;
- POS, Admin va TV web interfeyslari.

### Partial

- fizik printer bilan end-to-end tekshiruv;
- Admin Dashboard/Reports’ning real agregatsiya API’lari bilan to‘liq integratsiyasi.

### Out of scope — joriy pilot

- multi-branch cloud synchronization’ning production varianti;
- besh mustaqil microservice’ga production migratsiya;
- bank acquiring yoki fiskal operator bilan real production integratsiyasi;
- mijoz mobil ilovasi va delivery marketplace integratsiyasi.

## Muvaffaqiyat mezonlari

1. Internet bo‘lmaganda lokal tarmoqda asosiy savdo oqimi davom etadi.
2. Har bir moliyaviy operatsiya smena, foydalanuvchi va audit izi bilan bog‘lanadi.
3. Bir xil so‘rov qayta yuborilganda idempotency duplicate moliyaviy natijani oldini oladi.
4. Rollar faqat ruxsat etilgan amallarni bajaradi.
5. Backup va restore jarayoni hujjatlashtirilgan hamda tekshiriladigan bo‘ladi.
6. Hujjatlardagi har bir kritik funksiya talab, diagramma va test daliliga bog‘lanadi.
