# Nofunksional talablar

| ID | Sifat atributi | O‘lchanadigan talab | Tekshirish usuli |
|---|---|---|---|
| NFR-01 | Offline-first | Internet uzilganda Hub va bir lokal tarmoqdagi client’lar asosiy savdo oqimini davom ettirishi kerak. | Network isolation smoke test |
| NFR-02 | Tenant isolation | Har bir business/branch query’si tegishli kontekst bilan cheklanishi, boshqa tenant ma’lumoti qaytmasligi kerak. | Authorization/invariant test |
| NFR-03 | Moliyaviy aniqlik | Pul qiymatlari integer minor unit’da saqlanishi; floating-point orqali hisoblanmasligi kerak. | Schema va unit test |
| NFR-04 | Idempotency | Critical write so‘rovi bir xil idempotency key bilan takrorlansa duplicate order/payment yaratmasligi kerak. | Replay integration test |
| NFR-05 | Xavfsizlik | PIN/parol argon2id bilan hash qilinishi, raw credential log yoki response’da chiqmasligi kerak. | Security review va HTTP test |
| NFR-06 | Session security | Token server-side opaque session’ga bog‘lanishi, expiry/revocation darhol kuchga kirishi kerak. | Auth integration test |
| NFR-07 | Ishlash tezligi | Lokal tarmoqda oddiy read/write API’larning 95-persentili pilot hardware’da 500 ms’dan oshmasligi maqsad qilinadi. | Load/performance test |
| NFR-08 | Barqarorlik | Hub restart’dan so‘ng committed order/payment ma’lumoti yo‘qolmasligi va xizmat avtomatik tiklanishi kerak. | Restart/recovery smoke test |
| NFR-09 | Backup/recovery | On-demand backup yaratilishi, yaxlitligi tekshirilishi va hujjatlashtirilgan restore drill’dan o‘tishi kerak. | Backup/restore test |
| NFR-10 | Auditability | Critical amal actor, vaqt, branch, entity va old/new context bilan izlanadigan audit izi qoldirishi kerak. | Audit log test |
| NFR-11 | Observability | Strukturali log correlation/request ID va xato kontekstini saqlashi, secret’larni redaction qilishi kerak. | Log inspection |
| NFR-12 | Usability | Asosiy POS oqimi 375, 768, 1024 va 1440 px kengliklarda funksional bo‘lishi, keyboard focus ko‘rinishi kerak. | Responsive/accessibility review |
| NFR-13 | Accessibility | Oddiy matn kontrasti kamida 4.5:1 bo‘lishi, rang yagona holat signali bo‘lmasligi kerak. | Automated va manual a11y review |
| NFR-14 | Maintainability | Typecheck, lint, format, unit/integration test va build CI’da avtomatik ishlashi kerak. | CI pipeline |
| NFR-15 | Compatibility | Pilot Windows deployment’da Hub, Chromium-based client va belgilangan printer protokoli bilan ishlashi kerak. | Deployment/hardware matrix |
| NFR-16 | Privacy | Public artefaktlarda token, parol, private endpoint, real mijoz ma’lumoti va shaxsiy email bo‘lmasligi kerak. | Secret/PII scan |

## Qayd

NFR-07 hozircha target hisoblanadi; yakuniy hardware benchmark protokoli bilan tasdiqlanishi lozim. NFR-15’ning printer qismi fizik qurilma sinovisiz **Partial** bo‘lib qoladi.
