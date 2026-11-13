# osonCafe Software Development Life Cycle

## 1. Planning

| Element | Tavsif |
|---|---|
| Maqsad | Internetdan mustaqil, lokal Hub asosidagi kafe POS pilotini yaratish |
| Kirish | Biznes muammosi, foydalanuvchi rollari, qurilma va offline cheklovlar |
| Bajarilgan ish | PRD scope, roadmap, task decomposition, branch va review oqimi |
| Artefakt | PRD, roadmap, task hujjatlari, planning va evidence manifest |
| Dalil | `docs/tasks`, PRD/roadmap audit, Git history |
| Holat | Current; public hujjatga umumlashtirilgan |

## 2. Requirements Analysis

| Element | Tavsif |
|---|---|
| Maqsad | Business flow va system constraint’larni tekshiriladigan talabga aylantirish |
| Kirish | PRD F01–F14, rollar, state transition, owner qarorlari |
| Bajarilgan ish | 30 FR, 16 NFR, 18 US, 22 BR, 12 acceptance scenario |
| Artefakt | `01-Requirements/` va RTM |
| Dalil | PRD, code route/schema va tests o‘rtasidagi reconciliation |
| Holat | Complete for academic documentation |

## 3. System Design

| Element | Tavsif |
|---|---|
| Maqsad | Current va Proposed arxitekturani, data va business flow’larni aniqlash |
| Kirish | ADR-001…005, Prisma schema, API/route/module structure, eski arxitektura PDF |
| Bajarilgan ish | 27 UML/C4/BPMN/ERD diagramma va 81 eksport artefakti |
| Artefakt | `02-System-Design/`, `03-Database/`, `04-Diagrams/` |
| Dalil | Draw.io source + direct SVG/PNG export; visual QA |
| Holat | Complete; printer/admin aggregation Partial belgisi saqlangan |

## 4. Implementation

| Element | Tavsif |
|---|---|
| Maqsad | Hub-only modular monolith pilotini ishlaydigan package sifatida yetkazish |
| Kirish | Approved PRD, ADR, typed contracts va tasklar |
| Bajarilgan ish | Hub, POS, Admin, domain/shared packages, SQLite, installer/deployment scripts |
| Artefakt | Private implementation source; public’da xavfsiz architecture/pseudocode documentation |
| Dalil | Route/module/schema/package audit va production build |
| Holat | Current pilot; printer va Admin aggregate gap’lari ochiq |

## 5. Testing

| Element | Tavsif |
|---|---|
| Maqsad | Domain, API, database, UI va invariant’larni regressiyadan himoya qilish |
| Kirish | Acceptance criteria, RTM, test fixtures |
| Bajarilgan ish | 1,780 automated test, check pipeline, build; mavjud 18/18 smoke va 95/95 visual report |
| Artefakt | Test Plan, 20 test case, Test Report |
| Dalil | 2026-11-13 local read-only run: 0 failed |
| Holat | Automated gate PASS; hardware/performance/Admin aggregate NOT RUN |

## 6. Deployment

| Element | Tavsif |
|---|---|
| Maqsad | Pilotni Windows Hub va LAN client’lar bilan takrorlanuvchi o‘rnatish |
| Kirish | Built Hub/POS/Admin, SQLite, environment config |
| Bajarilgan ish | Windows package/service/autostart, port check, backup/restore workflow |
| Artefakt | Current va Proposed deployment docs/diagrams |
| Dalil | Deployment scripts, pilot smoke report |
| Holat | Current Hub-only; physical printer validation Partial |

## 7. Maintenance

| Element | Tavsif |
|---|---|
| Maqsad | Pilot barqarorligi, security, backup, observability va evolyutsiyani boshqarish |
| Kirish | Audit log, incident, test report, performance/usage metric |
| Bajarilgan ish | Structured logging, backup/restore, test gates, task/ADR workflow |
| Artefakt | Maintenance plan, known limitations, proposed cloud architecture |
| Dalil | CI, ADR, reports va operational modules |
| Holat | Continuous; microservices faqat future proposal |

## Traceability oqimi

```text
PRD / ADR / Code evidence
          ↓
FR · NFR · BR · US
          ↓
Acceptance Criteria
          ↓
UML / ERD / BPMN
          ↓
Implementation evidence
          ↓
Test Case / Result
          ↓
Release audit
```
