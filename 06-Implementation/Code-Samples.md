# Tasdiqlangan pattern namunalari

Quyidagi bloklar private source code nusxasi emas. Ular audit qilingan implementation pattern’ini ommaga xavfsiz **pseudocode** shaklida ko‘rsatadi.

## Route → Service → Repository

```text
request = validateWithSchema(http.body)
session = requireSession(http.cookie)
requirePermission(session, "ORDER_CREATE")

result = orderService.create({
  branchId: session.branchId,
  actorId: session.userId,
  idempotencyKey: http.header["idempotency-key"],
  request
})

return created(publicOrderDto(result))
```

## Integer money

```text
subtotalMinor = sum(item.unitPriceMinor * item.quantity)
modifierMinor = sum(selectedModifier.priceMinor * item.quantity)
discountMinor = validatedDiscount(subtotalMinor + modifierMinor)
totalMinor = subtotalMinor + modifierMinor - discountMinor
```

## Idempotent payment

```text
existing = idempotencyRepository.find(scope, key)
if existing.requestHash differs:
  reject KEY_REUSED_WITH_DIFFERENT_REQUEST
if existing.completed:
  return existing.savedResult

transaction:
  validate payable order and active shift
  create payment parts
  mark order paid/completed
  append audit event
  persist idempotent result
```

Aniq API field va implementation source private repository’da qoladi.
