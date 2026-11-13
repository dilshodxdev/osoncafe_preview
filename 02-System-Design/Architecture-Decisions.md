# Architecture Decision Records sharhi

| ADR | Qaror | Status | Oqibat |
|---|---|---|---|
| ADR-001 | Hub persistence Prisma ORM orqali | Accepted/Current | Typed schema va repository boundary; raw DB access cheklanadi |
| ADR-002 | Pilot modular monolith | Accepted/Current | Bitta deployable, lekin modul chegaralari saqlanadi |
| ADR-003 | Hub-only pilot | Accepted/Current | Internet uzilishida LAN savdosi davom etadi; cloud sync pilot scope’da emas |
| ADR-004 | Server-side opaque session | Accepted/Current | Revoke/expiry va device/user active holati Hub’da nazorat qilinadi |
| ADR-005 | OWNER password/PIN Argon2id hash | Accepted/Current | Raw credential saqlanmaydi; lockout va audit talab qilinadi |

## Proposed qarorlar

Microservices, API Gateway, message broker va database-per-service mavjud PDF konsepsiyasidan kelib chiqadi, lekin accepted current ADR emas. Shu sababli barcha diagrammada **Proposed** badge va uzilgan kulrang chiziq bilan ko‘rsatilgan.

## Architecture fitness functions

- Database access repository boundary’dan tashqariga chiqmasligi.
- Money floating-point ishlatmasligi.
- Mutation validation’siz qolmasligi.
- Audit append-only bo‘lishi.
- Business/Branch scope request’dan emas, trusted session’dan olinishi.
- Public response secret/hash field’larini o‘z ichiga olmasligi.

Bu qoidalar invariant script va automated tests bilan tekshiriladi.
