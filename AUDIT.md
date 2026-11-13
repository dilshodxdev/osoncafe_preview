# Yakuniy public release auditi

Audit sanasi: 2026-11-13  
Target: `dilshodxdev/osoncafe_preview`, `main` branch  
Scope: SDLC, requirements, UML/BPMN, database, UI, implementation, testing, deployment va akademik PDF

## Natija

Public release paketi tayyor. Joriy imkoniyatlar, qisman tasdiqlangan qismlar va taklif etilayotgan arxitektura hujjatlarda alohida belgilangan.

| Tekshiruv | Status | Dalil |
|---|---|---|
| Project identity | PASS | Matyaqubov Dilshodbek, S941-23Di, Kuryazov D.A., 2026 |
| Scope va stakeholderlar | PASS | Project Overview, Scope and Stakeholders |
| Functional requirements | PASS | FR-01…FR-30 |
| Non-functional requirements | PASS | NFR-01…NFR-16 |
| User stories | PASS | US-01…US-18 |
| Business rules | PASS | BR-01…BR-22 |
| Acceptance va traceability | PASS | 12 kritik acceptance scenario, RTM |
| Diagram source | PASS | 27 editable `.drawio` |
| Diagram exports | PASS | 27 `.svg` va 27 `.png`; jami 81 artefakt |
| Diagram visual QA | PASS | Barcha renderlar contact-sheet orqali ko‘rib chiqildi |
| UI evidence | PASS | 12 public-safe screenshot |
| Database documentation | PASS | 30 model, ERD va data dictionary |
| Implementation documentation | PASS | Frontend, backend, API, security, logging va code sample |
| Automated checks | PASS | invariant, typecheck, lint, format, build |
| Test suite | PASS | 269 file, 1780 passed, 0 failed |
| Existing smoke/visual evidence | PASS | 18/18 smoke, 95/95 visual |
| PDF | PASS | 50 bet, A4, S941-23Di, 27 diagramma va UI ilovalari |
| Current/Partial/Proposed ajratilishi | PASS | README va barcha tegishli hujjatlarda izchil |
| Public credential scan | PASS | Token, parol va obvious secret assignment topilmadi |
| Private source code isolation | PASS | Private repositorydan source kod ko‘chirilmagan |

## Ataylab Partial / Not run qolgan qismlar

| Qism | Holat | Sabab |
|---|---|---|
| Fizik printer E2E | Partial / Not run | Real printer qurilmasi va operatsion muhit talab qilinadi |
| Performance p95 benchmark | Not run | Reprezentativ production yuk profili talab qilinadi |
| Admin real aggregation E2E | Partial / Not run | Real aggregation API bilan yakuniy integratsiya tekshiruvi kerak |

Bu uch band release’ni bloklamaydi, chunki ular Implemented sifatida da’vo qilinmagan va requirements, test hamda deployment hujjatlarida ochiq qayd etilgan.

## Sanoq

- 27 diagramma × 3 format = 81 diagramma artefakti;
- 12 public-safe UI screenshot;
- 30 FR, 16 NFR, 18 user story, 22 business rule;
- 20 hujjatlashtirilgan test case;
- 269 automated test file, 1780 passed, 0 failed;
- 50 betlik akademik PDF.

## Release qarori

**PASS.** Public preview repository `main` branch’ga chiqarishga tayyor. Private repository read-only audit manbasi bo‘lib qoladi.

