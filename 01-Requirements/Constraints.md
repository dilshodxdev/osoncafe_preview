# Cheklovlar

| ID | Cheklov | Ta’siri |
|---|---|---|
| CON-01 | Pilot Windows host va lokal tarmoqqa mo‘ljallangan | Deployment, service/autostart va port diagnostikasi Windows’da tekshiriladi |
| CON-02 | Internet doimiy bo‘lishi kafolatlanmaydi | Asosiy savdo Hub-only va LAN ichida ishlashi kerak |
| CON-03 | Database joriy pilotda SQLite | Bir hostli write modeli va ishonchli backup/restore talab qilinadi |
| CON-04 | Private source code public repositoryga ko‘chirilmaydi | Public hujjatlarda faqat umumlashtirilgan stack, diagramma va xavfsiz screenshotlar mavjud |
| CON-05 | Fizik printer barcha muhitlarda mavjud emas | Printer va receipt E2E holati hardware sinovigacha Partial |
| CON-06 | Admin Dashboard/Reports real aggregation’i yakunlanmagan | Visual UI mavjud, real ko‘rsatkichlar Implemented deb belgilanmaydi |
| CON-07 | Pul UZS integer minor unit’da yuritiladi | Floating-point hisob-kitob taqiqlanadi |
| CON-08 | Har bir client Hub orqali ishlaydi | Client database’ga bevosita ulanmaydi va server total/role’ni qayta tekshiradi |
| CON-09 | Universitet topshirig‘i o‘zbek tilida | Asosiy matn o‘zbekcha, standard texnik terminlar inglizcha |
| CON-10 | Eski PDF’da guruh `S942-23Di` yozilgan | Yakuniy hujjatda explicit topshiriq bo‘yicha `S941-23Di` ishlatiladi |

## Farazlar

- Kafe ichidagi LAN Hub va client’lar o‘rtasida barqaror.
- OWNER yoki texnik xodim backup va pairing vazifalarini bajarishga vakolatli.
- Screenshotlardagi ism, buyurtma va summalar test fixture bo‘lib, real mijoz ma’lumoti emas.
- Proposed microservices modeli joriy pilot acceptance mezoniga kirmaydi.
