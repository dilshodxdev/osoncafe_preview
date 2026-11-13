# Diagrammalar katalogi

Har bir diagramma uch formatda yetkaziladi: tahrirlanadigan `.drawio`, vektor `.svg` va raster `.png`. Yakuniy scope: **27 diagramma × 3 format = 81 artefakt**.

| ID | Nomi | Notatsiya | Holat | Bog‘liq talablar |
|---|---|---|---|---|
| D01 | System Context | C4 Context | Current + Proposed boundary | Project scope |
| D02 | Use Case | UML Use Case | Current | FR-01–FR-28 |
| D03 | Domain Class | UML Class | Current | FR-05–FR-26 |
| D04 | Detailed Model | UML Class | Current | NFR-02/03/10 |
| D05 | Controller–Service–Repository–API | UML Component/Class hybrid | Current | NFR-04/10/11/14 |
| D06 | PIN Login & Session | UML Sequence | Current | FR-01–FR-04 |
| D07 | Create Order | UML Sequence | Current | FR-05, FR-08/09/14 |
| D08 | Kitchen Flow | UML Sequence | Current + Partial print | FR-10/11 |
| D09 | Payment | UML Sequence | Current + Partial receipt | FR-12/13 |
| D10 | Shift Close & Z-report | UML Sequence | Current | FR-20/21 |
| D11 | Cancel / Refund / Approval | UML Sequence | Current | FR-16–FR-18 |
| D12 | Order Activity | UML Activity | Current | FR-08/09/14/15 |
| D13 | Preparation Activity | UML Activity | Current | FR-10/11 |
| D14 | Payment Activity | UML Activity | Current | FR-12/13/17 |
| D15 | Shift Activity | UML Activity | Current | FR-07/19/20 |
| D16 | Order State Machine | UML State | Current | FR-11/16 |
| D17 | Payment/Session State Machine | UML State | Current | FR-04/12/17 |
| D18 | Shift State Machine | UML State | Current | FR-07/20 |
| D19 | Database ERD | Crow’s Foot ERD | Current | FR-01–FR-26 |
| D20 | Software Components | UML Component | Current | FR-01–FR-28 |
| D21 | Current Modular Monolith | Architecture | Current | ADR-001–005 |
| D22 | Proposed Microservices | Architecture | Proposed | FR-29/30 |
| D23 | Current Hub-only Deployment | UML Deployment | Current | FR-27, NFR-01/08/09/15 |
| D24 | Proposed Cloud Deployment | UML Deployment | Proposed | FR-29/30 |
| D25 | Order Lifecycle | BPMN 2.0 | Current | FR-08–FR-11 |
| D26 | Payment & Receipt | BPMN 2.0 | Current + Partial print | FR-12/13/17 |
| D27 | Shift & Reporting | BPMN 2.0 | Current + Partial admin report | FR-07/19–FR-21/28 |

## Fayl nomlash

Masalan, D01 quyidagicha saqlanadi:

- `04-Diagrams/D01-System-Context/D01-System-Context.drawio`
- `04-Diagrams/D01-System-Context/D01-System-Context.svg`
- `04-Diagrams/D01-System-Context/D01-System-Context.png`

Fayl nomida bo‘sh joy va locale’ga bog‘liq belgi ishlatilmaydi. Diagramma maqsadi, legendasi, statusi va bog‘liq talablar ushbu registry hamda `Diagram-Specifications.md` da markazlashgan holda yuritiladi.
