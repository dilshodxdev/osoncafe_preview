# Maintenance Plan

## Operatsion monitoring

- Hub health, fatal error va restart event’larini structured log’da kuzatish.
- Request/correlation ID bilan xatoni route va actor context’iga bog‘lash.
- Disk space, database/backup size va failed PrintJob count’ini tekshirish.
- Secret va shaxsiy ma’lumotni log redaction policy bilan himoya qilish.

## Backup va recovery

| Faoliyat | Tavsiya |
|---|---|
| On-demand backup | Muhim menu/settings yoki upgrade oldidan |
| Scheduled backup | Kafe ish rejimiga mos, kamida kunlik |
| Retention | Bir nechta rotation; bitta diskka bog‘lanmaslik |
| Restore drill | Production-like nusxada davriy |
| Verification | Archive integrity + Hub health + auth/menu/order read |

## Change management

1. Talab yoki muammo issue/task sifatida raqamlanadi.
2. Architecture yoki security qarori ADR bilan qayd qilinadi.
3. Feature branch’da minimal change va tests.
4. Check/test/build gate’dan keyin review.
5. Migration/deployment va rollback plan bilan release.
6. Public hujjat Current/Partial/Proposed statusiga mos yangilanadi.

## Prioritet texnik qarz

1. Fizik ESC/POS printer matrix, retry va duplicate print E2E.
2. Admin Dashboard/Reports real aggregation endpoint integratsiyasi.
3. POS/Admin bundle code-splitting va performance benchmark.
4. React test harness’dagi `act(...)` warning’larini tozalash.
5. Production-like restore RTO/RPO drill.

## Microservices evolyutsiyasi uchun trigger

Faqat multi-branch scale, mustaqil deployment ehtiyoji va service ownership xarajati modular monolith soddaligidan ustun bo‘lganda extract boshlanadi. Database-per-service va event contract tayyor bo‘lmasdan data split qilinmaydi.
