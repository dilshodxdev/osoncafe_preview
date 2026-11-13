# Biznes qoidalari

| ID | Qoida |
|---|---|
| BR-01 | Bitta branch’da bir vaqtning o‘zida faqat bitta aktiv smena bo‘lishi mumkin. |
| BR-02 | Aktiv smenasiz moliyaviy order/payment yakunlanmaydi. |
| BR-03 | Order item narxi buyurtma yaratilgan paytda snapshot qilinadi; keyingi menu narx o‘zgarishi tarixiy order’ni o‘zgartirmaydi. |
| BR-04 | Pul qiymatlari integer minor unit’da saqlanadi. |
| BR-05 | Stop-list’dagi variant yoki modifier yangi order’ga qo‘shilmaydi. |
| BR-06 | Payment yig‘indisi order payable total’iga teng bo‘lmasa order paid/completed bo‘lmaydi. |
| BR-07 | Critical write endpoint’lari idempotency key bilan qayta bajarishga chidamli bo‘ladi. |
| BR-08 | Completed order’ni oddiy edit qilib bo‘lmaydi; tuzatish refund/void orqali amalga oshiriladi. |
| BR-09 | Cancel/refund/void sabab matni va actor auditi majburiy. |
| BR-10 | Manager approval talab qiladigan amal approver va executor’ni alohida qayd etadi. |
| BR-11 | Foydalanuvchi faqat o‘z roli va branch scope’iga ruxsat etilgan endpoint’dan foydalanadi. |
| BR-12 | SUPERADMIN kundalik UI foydalanuvchisi emas; bootstrap/texnik boshqaruv nazoratli CLI orqali bajariladi. |
| BR-13 | PIN va parol raw ko‘rinishda saqlanmaydi yoki log qilinmaydi. |
| BR-14 | Pairing code bir martalik, muddatli va ishlatilgach yaroqsiz bo‘lishi kerak. |
| BR-15 | Session revoke yoki foydalanuvchi deaktivatsiyasi keyingi himoyalangan so‘rovni rad etadi. |
| BR-16 | Cash movement faqat aktiv smena ichida va sabab bilan yaratiladi. |
| BR-17 | Shift close expected cash, actual cash va difference’ni saqlaydi. |
| BR-18 | Order state transition faqat ruxsat etilgan state machine yo‘li bo‘yicha bajariladi. |
| BR-19 | Audit log oddiy business UI orqali tahrirlanmaydi yoki o‘chirilmaydi. |
| BR-20 | Backup restore amali oldidan joriy ma’lumotning safety backup’i olinishi kerak. |
| BR-21 | TV token faqat TV uchun kerakli minimal read scope’ga ega bo‘ladi. |
| BR-22 | Public artefaktga secret, private URL yoki real mijoz ma’lumoti kiritilmaydi. |

## Rollar matritsasi

| Amal | OWNER | MANAGER | CASHIER | WAITER |
|---|:---:|:---:|:---:|:---:|
| Admin login va sozlamalar | ✓ | — | — | — |
| Menyu/xodim boshqaruvi | ✓ | — | — | — |
| Smena ochish/yopish | Kuzatish | ✓ | ✓ | — |
| Order yaratish | — | ✓ | ✓ | ✓ |
| Payment | — | ✓ | ✓ | — |
| Stop-list | — | ✓ | Cheklangan | — |
| Refund/void tasdiqlash | Kuzatish | ✓ | So‘rov | — |
| Kunlik hisobot | ✓ | ✓ | Cheklangan | — |

Aniq endpoint ruxsatlari implementatsiya authorization policy’si bilan yakuniy tekshiriladi; jadval akademik business-level ko‘rinishdir.
