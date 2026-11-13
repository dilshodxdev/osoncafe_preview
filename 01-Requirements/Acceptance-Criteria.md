# Acceptance criteria

Quyidagi ssenariylar kritik oqimlarning minimal qabul mezonidir. Barcha holatlarda tenant/branch izolatsiyasi va audit talablari qo‘llanadi.

## AC-01 — Qurilmani pairing qilish

- **Given** yaroqli va muddati tugamagan bir martalik code mavjud;
- **When** yangi qurilma code’ni Hub’ga yuboradi;
- **Then** qurilma ro‘yxatdan o‘tadi, faqat kerakli scope’li credential oladi va code qayta ishlatilmaydi.

## AC-02 — PIN login

- **Given** aktiv xodim va ro‘yxatdan o‘tgan POS qurilmasi mavjud;
- **When** xodim to‘g‘ri PIN kiritadi;
- **Then** server-side session yaratiladi va foydalanuvchi roliga mos route ochiladi.
- Noto‘g‘ri PIN xodim mavjudligini oshkor qilmaydi; belgilangan limitdan keyin urinish cheklanadi.

## AC-03 — Smena ochish

- **Given** branch’da aktiv smena yo‘q va actor vakolatli;
- **When** actor opening cash bilan smena ochadi;
- **Then** bitta aktiv shift yaratiladi va parallel ikkinchi open so‘rovi rad etiladi.

## AC-04 — Buyurtma yaratish

- **Given** aktiv smena va mavjud menu item bor;
- **When** actor item, variant, modifier, quantity va note bilan order’ni tasdiqlaydi;
- **Then** server total’ni qayta hisoblaydi, price snapshot saqlaydi va order number beradi.
- Stop-list’dagi item yoki client yuborgan soxta narx qabul qilinmaydi.

## AC-05 — Payment va idempotency

- **Given** to‘lanmagan valid order mavjud;
- **When** to‘lovlar yig‘indisi payable total’ga teng va unique idempotency key yuboriladi;
- **Then** bitta payment natijasi yaratiladi va order paid/completed holatiga o‘tadi.
- Shu key bilan replay yangi payment yaratmaydi, oldingi natijani qaytaradi.

## AC-06 — Split payment

- **Given** valid order mavjud;
- **When** CASHIER naqd/karta/QR qismlarini kiritadi;
- **Then** barcha qismlar musbat, method’lar valid va umumiy summa payable total’ga teng bo‘lsa transaction qabul qilinadi.

## AC-07 — Cancel/refund

- **Given** order holati cancel yoki refund’ga ruxsat beradi;
- **When** vakolatli actor sabab va zarur approval bilan amalni tasdiqlaydi;
- **Then** revers operatsiya asl order/payment’ga bog‘lanadi va audit log yoziladi.

## AC-08 — Smena yopish

- **Given** aktiv shift va yopishga vakolatli actor mavjud;
- **When** actual cash kiritilib shift yopiladi;
- **Then** expected, actual, difference va Z-report saqlanadi; yangi savdo eski smenaga yozilmaydi.

## AC-09 — Backup/restore

- **Given** Hub database ishlayapti;
- **When** authorized actor backup yaratadi;
- **Then** timestamp’li, yaxlitligi tekshiriladigan backup olinadi.
- Restore oldidan safety backup olinadi; muvaffaqiyatli restore’dan so‘ng health va asosiy read flow tekshiriladi.

## AC-10 — TV queue

- **Given** yaroqli TV token mavjud;
- **When** TV client polling endpoint’ni chaqiradi;
- **Then** faqat display uchun kerakli aktiv order raqamlari va holatlari qaytadi; moliyaviy yoki shaxsiy ma’lumot chiqmaydi.

## AC-11 — Admin Dashboard/Reports

- **Given** real Hub aggregation endpoint mavjud;
- **When** OWNER davr/branch filter bilan Dashboard yoki Reports’ni ochadi;
- **Then** ko‘rsatkichlar database’dagi yakunlangan operatsiyalardan hisoblanadi, demo/static qiymat ishlatilmaydi.
- Ushbu mezon bajarilmaguncha FR-28 holati **Partial** bo‘lib qoladi.

## AC-12 — Printer/receipt

- **Given** qo‘llab-quvvatlangan fizik printer sozlangan;
- **When** receipt yoki kitchen ticket print job’i yaratiladi;
- **Then** job muvaffaqiyatli chop etiladi yoki retryable xato holatiga o‘tadi, duplicate nusxa nazorat qilinadi.
- Fizik hardware dalili olinmaguncha FR-10 va FR-13 **Partial**.
