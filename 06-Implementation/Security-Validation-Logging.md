# Authentication, validation, error handling va logging

## Authentication

- Employee PIN va OWNER paroli argon2id bilan hash qilinadi.
- Token opaque; permission ma’lumoti client token payload’iga ishonib olinmaydi.
- Session server-side expiry, revoke va user/device active holatini tekshiradi.
- Pairing code va TV token minimal scope, expiry va revoke lifecycle’iga ega.

## Authorization

- Role + Business/Branch scope har bir protected request’da tekshiriladi.
- Refund, discount, kassa farqi kabi xavfli amallar manager approval talab qiladi.
- SUPERADMIN normal web UI actor’i emas; nazoratli CLI orqali ishlaydi.

## Validation

- Transport payload Zod schema bilan tekshiriladi.
- Business invariant application/domain qatlamida qayta tekshiriladi.
- Client yuborgan narx, total, status va role source of truth emas.
- Integer money va idempotency invariant’lari CI script bilan ham nazorat qilinadi.

## Logging va audit

- Pino JSON structured log; request/correlation ID.
- Credential, token, raw PIN/password va customer-sensitive payload redaction qilinadi.
- AuditLog actor, action, entity va old/new context’ni append-only saqlaydi.
- Operational log va business audit bir xil maqsad emas: log diagnostika, audit javobgarlik uchun.
