# Requirements Traceability Matrix

`Dxx` diagrammalar `02-System-Design/Diagram-Registry.md` bilan bir xil ID’dan foydalanadi. Test dalili public repo’da kod yo‘lini oshkor qilmaydigan, audit darajasidagi nom bilan berilgan.

| Talab | User story / qoida | Diagramma | Acceptance / test dalili | Holat |
|---|---|---|---|---|
| FR-01 | US-12, BR-14 | D02, D06, D20 | AC-01; pairing HTTP test | Implemented |
| FR-02 | US-02, BR-13 | D02, D06, D20 | AC-02; auth/lockout test | Implemented |
| FR-03 | US-10, BR-13 | D02, D20 | Owner auth/password-change test | Implemented |
| FR-04 | BR-15 | D06, D17 | Session revoke/expiry test | Implemented |
| FR-05 | US-02 | D02, D07 | Menu read/availability test | Implemented |
| FR-06 | US-10 | D02, D20 | Menu admin HTTP test | Implemented |
| FR-07 | US-01, BR-01 | D02, D10, D15, D18 | AC-03; shift invariant test | Implemented |
| FR-08 | US-02 | D07, D12 | AC-04; order HTTP test | Implemented |
| FR-09 | US-03, BR-03 | D03, D07, D19 | AC-04; price snapshot test | Implemented |
| FR-10 | US-13 | D08, D20 | AC-12; physical print E2E pending | Partial |
| FR-11 | US-13, BR-18 | D08, D13, D16 | Order transition test | Implemented |
| FR-12 | US-04, BR-06 | D09, D14, D17 | AC-05/06; payment test | Implemented |
| FR-13 | US-05 | D09, D20, D26 | AC-12; physical receipt E2E pending | Partial |
| FR-14 | BR-10 | D07, D12 | Discount/approval test | Implemented |
| FR-15 | US-06, BR-05 | D02, D12 | Stop-list HTTP test | Implemented |
| FR-16 | US-07, BR-09 | D11, D16 | AC-07; cancellation test | Implemented |
| FR-17 | US-07, BR-08/09 | D11, D17, D26 | AC-07; refund/void test | Implemented |
| FR-18 | US-07, BR-10 | D11 | Approval authorization test | Implemented |
| FR-19 | US-08, BR-16 | D15, D19 | Cash movement test | Implemented |
| FR-20 | US-01/09, BR-17 | D10, D15, D18, D27 | AC-08; shift close/Z test | Implemented |
| FR-21 | US-18 | D20, D27 | Daily report test | Implemented |
| FR-22 | US-14, BR-21 | D08, D20 | AC-10; TV token/queue test | Implemented |
| FR-23 | US-11, BR-11 | D02, D20 | Employee admin/RBAC test | Implemented |
| FR-24 | US-12 | D20, D23 | Settings/device HTTP test | Implemented |
| FR-25 | US-15, BR-20 | D20, D23 | AC-09; backup/restore test | Implemented |
| FR-26 | US-16, BR-19 | D04, D05, D19 | Audit log test | Implemented |
| FR-27 | US-17 | D23 | Windows deployment smoke | Implemented |
| FR-28 | US-18 | D20 | AC-11; real aggregation E2E pending | Partial |
| FR-29 | — | D22, D24 | Architecture review only | Proposed |
| FR-30 | — | D22, D24 | Architecture review only | Proposed |

## NFR traceability

| NFR | Diagram/dalil | Tekshiruv |
|---|---|---|
| NFR-01 | D21, D23 | Internet isolation smoke |
| NFR-02 | D04, D19 | Tenant invariant tests |
| NFR-03 | D03, D19 | Schema/unit tests |
| NFR-04 | D05, D09 | Replay integration tests |
| NFR-05/06 | D06, D17 | Auth/security tests |
| NFR-07/08 | D21, D23 | Benchmark va restart smoke |
| NFR-09 | D23 | Backup/restore drill |
| NFR-10/11 | D05, D20 | Audit/log inspection |
| NFR-12/13 | UI artefaktlari | Responsive va accessibility review |
| NFR-14 | SDLC/CI | Typecheck, lint, test, build |
| NFR-15 | D23 | Deployment/hardware matrix |
| NFR-16 | Release audit | Secret/PII scan |
