from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from svglib.svglib import svg2rlg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "Documentation" / "osonCafe-SDLC-Architecture.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

GREEN = colors.HexColor("#0F7A55")
LIGHT_GREEN = colors.HexColor("#E8F5EE")
TEXT = colors.HexColor("#17211D")
BORDER = colors.HexColor("#CBD5D1")
MUTED = colors.HexColor("#52615B")
PARTIAL = colors.HexColor("#B7791F")
PROPOSED = colors.HexColor("#64748B")


def register_fonts() -> None:
    fonts = {
        "TimesNewRoman": Path("C:/Windows/Fonts/times.ttf"),
        "TimesNewRoman-Bold": Path("C:/Windows/Fonts/timesbd.ttf"),
        "TimesNewRoman-Italic": Path("C:/Windows/Fonts/timesi.ttf"),
        "TimesNewRoman-BoldItalic": Path("C:/Windows/Fonts/timesbi.ttf"),
    }
    for name, path in fonts.items():
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "TimesNewRoman",
        normal="TimesNewRoman",
        bold="TimesNewRoman-Bold",
        italic="TimesNewRoman-Italic",
        boldItalic="TimesNewRoman-BoldItalic",
    )


register_fonts()


class AcademicDoc(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=2 * cm,
            rightMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm,
            title="osonCafe - SDLC, UML va dasturiy ta'minot arxitekturasi",
            author="Matyaqubov Dilshodbek",
            subject="Urganch davlat universiteti, S941-23Di, 2026",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self._header_footer))

    @staticmethod
    def _header_footer(canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        canvas.setStrokeColor(BORDER)
        canvas.setLineWidth(0.5)
        canvas.line(2 * cm, A4[1] - 1.35 * cm, A4[0] - 2 * cm, A4[1] - 1.35 * cm)
        canvas.setFont("TimesNewRoman", 9)
        canvas.setFillColor(MUTED)
        canvas.drawString(2 * cm, A4[1] - 1.1 * cm, "osonCafe - SDLC, UML va dasturiy ta'minot arxitekturasi")
        canvas.line(2 * cm, 1.35 * cm, A4[0] - 2 * cm, 1.35 * cm)
        canvas.drawCentredString(A4[0] / 2, 0.85 * cm, str(doc.page))
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="AcademicBody",
    fontName="TimesNewRoman",
    fontSize=14,
    leading=21,
    alignment=TA_JUSTIFY,
    firstLineIndent=1.25 * cm,
    textColor=TEXT,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="AcademicNoIndent",
    parent=styles["AcademicBody"],
    firstLineIndent=0,
))
styles.add(ParagraphStyle(
    name="Chapter",
    fontName="TimesNewRoman-Bold",
    fontSize=18,
    leading=24,
    alignment=TA_CENTER,
    textColor=TEXT,
    spaceBefore=10,
    spaceAfter=18,
))
styles.add(ParagraphStyle(
    name="Section",
    fontName="TimesNewRoman-Bold",
    fontSize=15,
    leading=20,
    alignment=TA_LEFT,
    textColor=GREEN,
    spaceBefore=12,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Caption",
    fontName="TimesNewRoman-Italic",
    fontSize=10,
    leading=13,
    alignment=TA_CENTER,
    textColor=MUTED,
    spaceBefore=6,
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name="Small",
    fontName="TimesNewRoman",
    fontSize=10,
    leading=13,
    textColor=TEXT,
))
styles.add(ParagraphStyle(
    name="TitleLarge",
    fontName="TimesNewRoman-Bold",
    fontSize=23,
    leading=29,
    alignment=TA_CENTER,
    textColor=TEXT,
    spaceAfter=18,
))


def P(text: str, style: str = "AcademicBody") -> Paragraph:
    return Paragraph(text, styles[style])


def heading(text: str, chapter: bool = False) -> Paragraph:
    return Paragraph(text, styles["Chapter" if chapter else "Section"])


def table(data, widths=None, font_size=9, header=True):
    cooked = []
    for row in data:
        cooked.append([Paragraph(str(cell), styles["Small"]) for cell in row])
    t = Table(cooked, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("FONTNAME", (0, 0), (-1, -1), "TimesNewRoman"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
    ]
    if header:
        commands += [
            ("BACKGROUND", (0, 0), (-1, 0), LIGHT_GREEN),
            ("FONTNAME", (0, 0), (-1, 0), "TimesNewRoman-Bold"),
            ("TEXTCOLOR", (0, 0), (-1, 0), GREEN),
        ]
    t.setStyle(TableStyle(commands))
    return t


def scaled_svg(path: Path, max_width=17 * cm, max_height=19 * cm):
    # Draw.io PNG exports are used when available because they preserve the
    # exact diagrams.net rendering; svglib does not support every draw.io SVG
    # filter/foreignObject construct on Windows.
    png = path.with_suffix(".png")
    if png.exists():
        image = Image(str(png))
        factor = min(max_width / image.imageWidth, max_height / image.imageHeight)
        image.drawWidth = image.imageWidth * factor
        image.drawHeight = image.imageHeight * factor
        return image
    drawing = svg2rlg(str(path))
    if drawing is None or not drawing.width or not drawing.height:
        png = path.with_suffix(".png")
        image = Image(str(png))
        factor = min(max_width / image.imageWidth, max_height / image.imageHeight)
        image.drawWidth = image.imageWidth * factor
        image.drawHeight = image.imageHeight * factor
        return image
    factor = min(max_width / drawing.width, max_height / drawing.height)
    drawing.scale(factor, factor)
    drawing.width *= factor
    drawing.height *= factor
    return drawing


def scaled_image(path: Path, max_width=17 * cm, max_height=18 * cm):
    image = Image(str(path))
    factor = min(max_width / image.imageWidth, max_height / image.imageHeight)
    image.drawWidth = image.imageWidth * factor
    image.drawHeight = image.imageHeight * factor
    return image


diagram_meta = [
    ("D01", "System Context", "Tizim chegarasi, actorlar, Hub, SQLite, printer va future cloud."),
    ("D02", "Use Case", "OWNER, MANAGER, CASHIER, WAITER, texnik xodim, oshxona va mijoz use case'lari."),
    ("D03", "Domain Class", "Identity, catalog, sales, operations va audit aggregate'lari."),
    ("D04", "Detailed Model", "API DTO, domain model, Prisma model va SQLite mapping chegaralari."),
    ("D05", "Controller Service Repository API", "Validation, authorization, service, repository va infrastructure qatlamlari."),
    ("D06", "PIN Login Session", "PIN login, lockout, argon2id va opaque session oqimi."),
    ("D07", "Create Order", "Menu validation, price snapshot, idempotency va atomic order creation."),
    ("D08", "Kitchen Flow", "Confirmed order, kitchen queue, preparing/ready va Partial printer."),
    ("D09", "Payment", "Cash/card/QR/split payment, idempotency va receipt job."),
    ("D10", "Shift Close Z Report", "Expected/actual cash, difference, Z-report va audit."),
    ("D11", "Cancel Refund Approval", "Reason, manager approval, refund va original payment linkage."),
    ("D12", "Order Activity", "Order qabul qilish swimlane faoliyat oqimi."),
    ("D13", "Preparation Activity", "Oshxona tayyorlash, TV va printer exception oqimi."),
    ("D14", "Payment Activity", "Payment method, total validation va atomic commit."),
    ("D15", "Shift Activity", "Shift open, sales loop, reconciliation va close."),
    ("D16", "Order State Machine", "Draft, Confirmed, Preparing, Ready, Completed va Cancelled."),
    ("D17", "Payment Session State Machine", "Payment refund lifecycle va session lock/expiry/revoke."),
    ("D18", "Shift State Machine", "No Active Shift, Open, Closing va Closed holatlari."),
    ("D19", "Database ERD", "Prisma schema'dagi 30 model va asosiy cardinality."),
    ("D20", "Component", "POS, Admin, TV, Hub, packages, Prisma, SQLite va adapters."),
    ("D21", "Current Modular Monolith", "Joriy Hub-only modular monolith va offline-first LAN."),
    ("D22", "Proposed Microservices", "Identity, Catalog, Sales, Operations va Reporting service konsepsiyasi."),
    ("D23", "Current Hub Only Deployment", "Windows Hub, LAN devices, SQLite, backup va Partial printer."),
    ("D24", "Proposed Microservices Deployment", "Edge Hub, cloud gateway, cluster, broker va database-per-service."),
    ("D25", "Order Lifecycle", "Customerdan completed ordergacha BPMN jarayoni."),
    ("D26", "Payment Receipt", "Payment va receipt exception'lari BPMN jarayoni."),
    ("D27", "Shift Reporting", "Shift open/close, Z-report va Partial Admin aggregation."),
]


def diagram_path(did: str, title: str) -> Path:
    slug = "-".join([part for part in title.replace("/", " ").split()])
    return ROOT / "04-Diagrams" / f"{did}-{slug}" / f"{did}-{slug}.svg"


story = []

# Title page
story += [Spacer(1, 1.3 * cm), P("O'ZBEKISTON RESPUBLIKASI OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI", "AcademicNoIndent"), Spacer(1, 0.5 * cm)]
story += [P("URGANCH DAVLAT UNIVERSITETI", "TitleLarge"), Spacer(1, 1.5 * cm)]
logo = ROOT / "assets" / "logo" / "osoncafe-logo.svg"
if logo.exists():
    story += [scaled_svg(logo, 8 * cm, 3 * cm), Spacer(1, 1 * cm)]
story += [P("osonCafe", "TitleLarge"), P("SDLC, UML VA DASTURIY TA'MINOT ARXITEKTURASI", "TitleLarge"), Spacer(1, 1.4 * cm)]
story += [table([
    ["Talaba", "Matyaqubov Dilshodbek"],
    ["Guruh", "S941-23Di"],
    ["O'qituvchi", "Kuryazov D. A."],
    ["Loyiha", "osonCafe restoran POS tizimi"],
], [5 * cm, 10 * cm], font_size=12, header=False), Spacer(1, 2 * cm)]
story += [P("Urganch - 2026", "AcademicNoIndent"), PageBreak()]

# Abstract and contents
story += [heading("ANNOTATSIYA", True), P("Ushbu hujjat osonCafe restoran POS tizimining Software Development Life Cycle jarayonini, requirements engineering natijalarini, joriy Hub-only modular monolith arxitekturasini, database modelini, UML va BPMN diagrammalarini, UI/UX materiallarini, implementatsiya hamda test dalillarini birlashtiradi. Hujjat joriy implementation, qisman tekshirilgan imkoniyat va kelajak taklifini qat'iy ajratadi."), P("Joriy pilot Node.js, Express, TypeScript, Prisma va SQLite asosida lokal tarmoqda ishlaydi. POS, Admin va TV React interfeyslari bitta Hub orqali xizmat oladi. Kelajakdagi besh xizmatli microservices modeli alohida Proposed arxitektura sifatida berilgan."), P("Kalit so'zlar: SDLC, UML, BPMN, modular monolith, offline-first, POS, Prisma, SQLite, requirements traceability, software testing."), PageBreak()]

story += [heading("MUNDARIJA", True)]
contents = [
    ["1", "Loyiha va muammo tavsifi"], ["2", "Requirements Engineering"], ["3", "Joriy system architecture"],
    ["4", "UML detailed design"], ["5", "Database design va ERD"], ["6", "UI/UX design"],
    ["7", "Implementation documentation"], ["8", "Software testing"], ["9", "Deployment"],
    ["10", "SDLC va maintenance"], ["11", "Taklif etilayotgan microservices"], ["12", "Xulosa"],
    ["Ilova A", "27 ta Draw.io diagramma"], ["Ilova B", "UI screenshotlar"],
]
story += [table([["Bo'lim", "Nomi"]] + contents, [3 * cm, 13.5 * cm], font_size=11), PageBreak()]

# Project overview
story += [heading("1. LOYIHA VA MUAMMO TAVSIFI", True)]
story += [P("Kafe va kichik restoranlarda buyurtma, kassa, oshxona, smena va hisobot jarayonlari ko'pincha alohida vositalar yoki qo'lda yuritiladi. Internet uzilishi, qurilma almashishi va rol nazoratining yetarli emasligi xizmat tezligi hamda moliyaviy javobgarlikka salbiy ta'sir qiladi."), P("osonCafe bitta lokal Hub orqali POS, Admin va TV interfeyslarini taqdim etadi. Asosiy savdo internet bo'lmaganda ham LAN ichida ishlashi, har bir moliyaviy amal smena, actor va audit iziga bog'lanishi, duplicate request esa idempotency bilan nazorat qilinishi kerak.")]
story += [heading("1.1 Stakeholderlar"), table([
    ["Stakeholder", "Asosiy ehtiyoj"], ["OWNER", "Menyu, xodim, sozlama, backup va umumiy nazorat"],
    ["MANAGER", "Smena, stop-list, approval, refund va kunlik hisobot"], ["CASHIER", "Buyurtma, to'lov, receipt va kassa harakati"],
    ["WAITER", "Tez order entry va holat kuzatuvi"], ["Oshxona", "Aniq navbat va tayyor holati"],
    ["Texnik xodim", "Pairing, deployment, backup va diagnostika"], ["Mijoz", "To'g'ri buyurtma va tez xizmat"],
], [4 * cm, 12.5 * cm])]
story += [heading("1.2 Scope va status"), table([
    ["Status", "Ta'rif", "Misol"], ["Current", "Kod/test dalili mavjud", "Hub-only modular monolith, POS order/payment"],
    ["Partial", "Qisman yoki hardware/E2E tasdiq kerak", "Printer, Admin real aggregation"],
    ["Proposed", "Kelajak konsepsiyasi", "Cloud sync va microservices"],
], [3 * cm, 7 * cm, 6.5 * cm]), PageBreak()]

# Requirements
story += [heading("2. REQUIREMENTS ENGINEERING", True), P("Talablar PRD, ADR, implementation va test dalillari orasidagi ziddiyatlarni ajratgan holda raqamlandi. Public to'plam 30 funksional talab, 16 nofunksional talab, 18 user story va 22 biznes qoidani o'z ichiga oladi.")]
story += [heading("2.1 Funksional talablar xulosasi"), table([
    ["Guruh", "Talablar", "Holat"], ["Auth va devices", "FR-01 - FR-04", "Current"], ["Menu va order", "FR-05 - FR-11", "Current; printer Partial"],
    ["Payment va reversal", "FR-12 - FR-18", "Current; receipt hardware Partial"], ["Shift/report", "FR-19 - FR-21", "Current"],
    ["TV, staff, settings, backup, audit", "FR-22 - FR-27", "Current"], ["Admin aggregation", "FR-28", "Partial"],
    ["Cloud/microservices", "FR-29 - FR-30", "Proposed"],
], [4.8 * cm, 6 * cm, 5.7 * cm])]
story += [heading("2.2 Nofunksional talablar"), table([
    ["ID", "Sifat atributi", "Asosiy mezon"], ["NFR-01", "Offline-first", "Internet uzilganda LAN savdosi davom etadi"],
    ["NFR-02", "Isolation", "Business/Branch scope"], ["NFR-03", "Moliyaviy aniqlik", "Integer minor unit"],
    ["NFR-04", "Idempotency", "Replay duplicate side effect yaratmaydi"], ["NFR-05/06", "Security", "Argon2id va opaque session"],
    ["NFR-09", "Recovery", "Backup/restore"], ["NFR-10/11", "Audit/observability", "Append-only audit va structured log"],
    ["NFR-14", "Maintainability", "CI check/test/build"],
], [2.2 * cm, 4.5 * cm, 9.8 * cm])]
story += [P("To'liq FR, NFR, acceptance criteria, constraints va Requirements Traceability Matrix GitHub hujjatlarida berilgan."), PageBreak()]

# Current architecture
story += [heading("3. JORIY SYSTEM ARCHITECTURE", True), P("Joriy pilot bitta Node.js/Express/TypeScript Hub atrofida qurilgan modular monolith. Hub POS, Admin va TV client'lariga REST/polling xizmatlarini beradi; Prisma orqali SQLite'ga yozadi. Client narx, total, role yoki state transition uchun source of truth emas."), P("Hub-only qarori internetga qaramlikni kamaytiradi, Windows deployment va backup'ni soddalashtiradi. Modular boundary kelajakda service extract qilish uchun tayanch bo'lib qoladi.")]
for did, title in [("D01", "System Context"), ("D21", "Current Modular Monolith"), ("D23", "Current Hub Only Deployment")]:
    path = diagram_path(did, title)
    story += [scaled_svg(path, 17 * cm, 17 * cm), P(f"{did}. {title}", "Caption"), Spacer(1, 0.2 * cm)]
story += [PageBreak()]

# Database
story += [heading("5. DATABASE DESIGN VA ERD", True), P("Joriy SQLite schema Prisma 6.19.3 bilan boshqariladi va 30 modeldan iborat. Business va Branch tenant scope'ining ildizi; Order va Shift moliyaviy transaction markazi; AuditLog va IdempotencyRecord xavfsizlik hamda ishonchlilikni qo'llab-quvvatlaydi.")]
story += [table([
    ["Domain", "Modellar"], ["Core/Identity", "Business, Branch, User, Device, Session, PairingCode, PairingAttempt, TechnicalCode"],
    ["Catalog", "Category, Product, ProductVariant, ModifierGroup, Modifier, StopListItem"],
    ["Sales", "OrderCounter, Order, OrderItem, OrderItemModifier, Payment, Refund, Discount, Membership"],
    ["Operations", "Shift, CashMovement, Printer, PrintJob, ZReport, TvToken"],
    ["Reliability", "AuditLog, IdempotencyRecord"],
], [4 * cm, 12.5 * cm])]
story += [scaled_svg(diagram_path("D19", "Database ERD"), 17 * cm, 17 * cm), P("D19. Joriy Prisma schema asosidagi ERD", "Caption"), PageBreak()]

# UI
story += [heading("6. UI/UX DESIGN", True), P("POS va Admin React 19/Vite asosida, Inter typography va osonCafe yashil brand tokenlari bilan ishlab chiqilgan. Screenshotlardagi qiymatlar test fixture bo'lib, real mijoz ma'lumoti emas. Owner Dashboard/Reports ko'rinishi mavjud, ammo real aggregation E2E Partial statusida.")]
ui_pairs = [
    ("03-pos-order-react.png", "POS order"), ("05-payment-react.png", "Payment"), ("11-tv-react.png", "TV queue"),
    ("13-owner-dashboard-react.png", "Owner Dashboard"), ("14-owner-menu-react.png", "Owner Menu"), ("17-owner-settings-react.png", "Owner Settings"),
]
for i in range(0, len(ui_pairs), 2):
    row = []
    for name, caption in ui_pairs[i:i+2]:
        img = scaled_image(ROOT / "05-UI" / "screenshots" / name, 8 * cm, 8.5 * cm)
        row.append([img, Paragraph(caption, styles["Caption"])])
    gallery = Table([row], colWidths=[8.2 * cm] * len(row), hAlign="CENTER")
    gallery.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story += [gallery, Spacer(1, 0.4 * cm)]
story += [PageBreak()]

# Implementation
story += [heading("7. IMPLEMENTATION DOCUMENTATION", True), P("Monorepo apps/hub, apps/pos-web, apps/admin-web, packages/domain va packages/shared-types qismlaridan iborat. Express route transport va validation'ni, application service use case'ni, repository esa Prisma transaction'ni boshqaradi.")]
story += [table([
    ["Qatlam", "Texnologiya", "Mas'uliyat"], ["Hub", "Node.js, Express, TypeScript", "API, business service, repository va adapters"],
    ["Data", "Prisma 6.19.3, SQLite", "Schema, migration, scoped transaction"], ["POS/Admin", "React 19, Vite", "Order/payment/shift va owner boshqaruvi"],
    ["Contracts", "Zod, shared-types", "Request/response, enum va error"], ["Security", "Argon2id, opaque session", "Credential va revoke/expiry"],
    ["Logging", "Pino", "Structured log va correlation ID"],
], [3.4 * cm, 5 * cm, 8.1 * cm])]
story += [scaled_svg(diagram_path("D05", "Controller Service Repository API"), 17 * cm, 16 * cm), P("D05. Request lifecycle va qatlamlar", "Caption"), PageBreak()]

# Testing
story += [heading("8. SOFTWARE TESTING", True), P("2026-11-13 kuni audit qilingan private implementation branch'ida repository engine talabiga mos Node.js 22.22.0 va pnpm 10.18.3 bilan check, test va build command'lari bajarildi. Production yoki customer database ishlatilmadi.")]
story += [table([
    ["Suite", "Test file", "Test", "Natija"], ["Invariants", "1", "153", "PASS"], ["Domain", "9", "112", "PASS"],
    ["Shared types", "10", "150", "PASS"], ["POS Web", "174", "617", "PASS"], ["Admin Web", "37", "230", "PASS"],
    ["Hub", "38", "518", "PASS"], ["Jami", "269", "1,780", "0 failed"],
], [5 * cm, 3.5 * cm, 3.5 * cm, 4.5 * cm])]
story += [P("Invariant scan 434 source file'ni tekshirdi; typecheck, lint va format check PASS; Hub, POS va Admin production build PASS. Build vaqtida bundle size warning va ayrim React testlarda act(...) warning qayd etildi, ammo command exit code 0."), heading("8.1 Bajarilmagan testlar"), table([
    ["Test", "Status", "Sabab"], ["Fizik printer E2E", "NOT RUN", "Supported ESC/POS hardware ulanmagan"],
    ["p95 performance benchmark", "NOT RUN", "Reproducible pilot hardware/load run yo'q"],
    ["Admin real aggregation E2E", "NOT RUN", "Endpoint integration to'liq tasdiqlanmagan"],
], [6 * cm, 3.5 * cm, 7 * cm]), PageBreak()]

# Deployment and SDLC
story += [heading("9. DEPLOYMENT", True), P("Current deployment Windows Hub host, SQLite, backup storage va LAN'dagi POS/Admin/TV qurilmalaridan iborat. Printer adapter mavjud, lekin fizik hardware QA Partial. Proposed deployment Edge Hub va cloud service cluster'ni ko'rsatadi, ammo joriy capability emas.")]
story += [scaled_svg(diagram_path("D24", "Proposed Microservices Deployment"), 17 * cm, 17 * cm), P("D24. Proposed cloud deployment", "Caption"), PageBreak()]

story += [heading("10. SDLC VA MAINTENANCE", True), table([
    ["Bosqich", "Asosiy artefakt", "Holat"], ["Planning", "PRD, roadmap, tasklar", "Current"],
    ["Requirements", "FR/NFR/US/BR/AC/RTM", "Complete"], ["Design", "27 Draw.io, ERD, architecture", "Complete"],
    ["Implementation", "Hub/POS/Admin/packages", "Current pilot"], ["Testing", "1,780 automated + reports", "PASS with gaps"],
    ["Deployment", "Windows Hub-only", "Current; printer Partial"], ["Maintenance", "Logging, backup, ADR, CI", "Continuous"],
], [4 * cm, 8 * cm, 4.5 * cm])]
story += [P("Maintenance prioritetlari: fizik printer matrix, Admin aggregation, route-level code splitting, React test harness warning'lari va production-like restore RTO/RPO drill. Microservice extract faqat scale va mustaqil deployment ehtiyoji operatsion murakkablikdan ustun bo'lganda boshlanadi."), PageBreak()]

# Proposed architecture
story += [heading("11. TAKLIF ETILAYOTGAN MICROSERVICES", True), P("Taklif etilayotgan model Identity, Catalog, Sales, Operations va Reporting service'larini API Gateway va message broker orqali bog'laydi. Database-per-service data ownership'ni aniq qiladi. Bu model PDF konsepsiyasi va kelajak evolyutsiyasidir; joriy pilot modular monolith bo'lib qoladi.")]
story += [scaled_svg(diagram_path("D22", "Proposed Microservices"), 17 * cm, 17 * cm), P("D22. Proposed microservices architecture", "Caption")]
story += [heading("11.1 Migratsiya tamoyili"), P("Big-bang rewrite tavsiya qilinmaydi. Avval modular boundary, event contract, service ownership, observability, offline sync conflict policy va operating model tayyorlanadi. So'ng o'lchanadigan ehtiyojga qarab service bosqichma-bosqich extract qilinadi."), PageBreak()]

# Conclusion
story += [heading("12. XULOSA", True), P("osonCafe uchun SDLC hujjatlari o'qituvchi namunasidagi requirements, overall/detailed design, implementation, testing va version control kutilmalarini bajaradi hamda traceability, BPMN, state machine, deployment va audit materiallari bilan kengaytiradi."), P("Joriy Hub-only modular monolith 1,780 avtomatik test va production build bilan qayta tekshirildi. Printer hardware, performance benchmark va Admin real aggregation E2E bajarilmagan deb aniq ko'rsatildi. Taklif etilayotgan microservices arxitekturasi joriy tizimdan ajratildi."), P("Natijada universitet topshirig'i uchun tahrirlanadigan Draw.io source'lar, SVG/PNG eksportlar, database va UI materiallari, test report, SDLC lifecycle, professional README hamda ushbu akademik PDF bitta public repository'ga jamlandi.")]
story += [heading("FOYDALANILGAN MANBALAR"), table([
    ["#", "Manba"], ["1", "osonCafe PRD, ADR, roadmap, task, code va test auditlari"], ["2", "dr-dilshod/SDLCExample repository va Wiki"],
    ["3", "Prisma schema va package manifests"], ["4", "Mavjud 25 betlik osonCafe architecture PDF"], ["5", "Draw.io Desktop 32.4.1 exportlari"],
], [1 * cm, 15.5 * cm]), PageBreak()]

# Appendix: all diagrams
story += [heading("ILOVA A. UML, ERD, ARCHITECTURE VA BPMN DIAGRAMMALARI", True), P("Quyidagi 27 diagrammaning har biri public repository'da tahrirlanadigan .drawio, vektor .svg va raster .png formatida mavjud. Current, Partial va Proposed holatlari rang hamda sarlavha bilan ajratilgan."), PageBreak()]
for did, title, description in diagram_meta:
    path = diagram_path(did, title)
    story += [heading(f"{did}. {escape(title)}"), P(escape(description), "AcademicNoIndent"), Spacer(1, 0.2 * cm), scaled_svg(path, 17 * cm, 20 * cm), P(f"{did}. {escape(title)}", "Caption"), PageBreak()]

# Appendix UI
story += [heading("ILOVA B. UI SCREENSHOTLAR", True), P("Rasmlar actual React implementation'dan olingan va synthetic test fixture ma'lumotlaridan foydalanadi."), PageBreak()]
for name, caption in [
    ("01-device-pairing-react.png", "Device pairing"), ("02-employee-pin-react.png", "Employee PIN"),
    ("06-order-list-detail-react.png", "Orders list/detail"), ("09-daily-report-react.png", "Daily report"),
    ("10-shift-react.png", "Shift screen"), ("15-owner-employees-react.png", "Owner employees"),
]:
    story += [heading(caption), scaled_image(ROOT / "05-UI" / "screenshots" / name, 17 * cm, 20 * cm), P(caption, "Caption"), PageBreak()]

doc = AcademicDoc(str(OUTPUT))
doc.build(story)
print(OUTPUT)
