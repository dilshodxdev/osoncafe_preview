from __future__ import annotations

from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "04-Diagrams"

GREEN = "#0F7A55"
LIGHT_GREEN = "#E8F5EE"
TEXT = "#17211D"
BORDER = "#CBD5D1"
MUTED = "#52615B"
WHITE = "#FFFFFF"
PARTIAL = "#B7791F"
PARTIAL_BG = "#FFF8E7"
PROPOSED = "#64748B"
PROPOSED_BG = "#F1F5F9"
RED = "#B42318"
RED_BG = "#FEF3F2"
BLUE = "#2563EB"
BLUE_BG = "#EFF6FF"


def slug(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-")


class Canvas:
    def __init__(self, did: str, title: str, notation: str, status: str, width: int = 1600, height: int = 900):
        self.did = did
        self.title = title
        self.notation = notation
        self.status = status
        self.width = width
        self.height = height
        self.mxfile = ET.Element("mxfile", host="Electron", agent="osonCafe SDLC", version="32.4.1")
        self.diagram = ET.SubElement(self.mxfile, "diagram", id=did.lower(), name=f"{did} {title}")
        self.model = ET.SubElement(
            self.diagram,
            "mxGraphModel",
            dx="1600",
            dy="900",
            grid="1",
            gridSize="10",
            guides="1",
            tooltips="1",
            connect="1",
            arrows="1",
            fold="1",
            page="1",
            pageScale="1",
            pageWidth=str(width),
            pageHeight=str(height),
            math="0",
            shadow="0",
            background=WHITE,
        )
        self.root = ET.SubElement(self.model, "root")
        ET.SubElement(self.root, "mxCell", id="0")
        ET.SubElement(self.root, "mxCell", id="1", parent="0")
        self._counter = 2
        self.nodes: dict[str, str] = {}
        self._header()

    def _id(self) -> str:
        value = str(self._counter)
        self._counter += 1
        return value

    def _header(self) -> None:
        self.node(
            "title",
            f"<b>{self.did} · {self.title}</b><br><font color='{MUTED}'>{self.notation} · osonCafe SDLC</font>",
            40,
            25,
            self.width - 300,
            70,
            kind="title",
        )
        status_color = GREEN if "Current" in self.status else PROPOSED
        status_bg = LIGHT_GREEN if "Current" in self.status else PROPOSED_BG
        if "Partial" in self.status:
            status_color, status_bg = PARTIAL, PARTIAL_BG
        self.node("status", f"<b>{self.status}</b>", self.width - 235, 38, 190, 38, kind="badge", stroke=status_color, fill=status_bg, font=status_color)
        self.node(
            "footer",
            "Yashil = Current/Implemented  ·  Sariq = Partial  ·  Kulrang uzilgan = Proposed  ·  Generated from audited requirements",
            40,
            self.height - 42,
            self.width - 80,
            24,
            kind="note",
        )

    def node(
        self,
        key: str,
        label: str,
        x: float,
        y: float,
        w: float,
        h: float,
        *,
        kind: str = "box",
        parent: str = "1",
        stroke: str = BORDER,
        fill: str = WHITE,
        font: str = TEXT,
        dashed: bool = False,
        extra: str = "",
    ) -> str:
        cell_id = self._id()
        styles = {
            "box": "rounded=1;arcSize=14;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;spacing=8;",
            "title": "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;fontSize=23;strokeColor=none;fillColor=none;",
            "badge": "rounded=1;arcSize=30;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=13;",
            "note": "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;fontSize=11;strokeColor=none;fillColor=none;",
            "actor": "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;align=center;fontSize=13;",
            "usecase": "ellipse;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=13;",
            "decision": "rhombus;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=12;",
            "event": "ellipse;aspect=fixed;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=11;strokeWidth=2;",
            "end": "ellipse;aspect=fixed;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=11;strokeWidth=4;",
            "database": "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=12;align=center;verticalAlign=middle;fontSize=13;",
            "component": "shape=component;align=left;spacingLeft=35;whiteSpace=wrap;html=1;verticalAlign=middle;fontSize=13;",
            "class": "swimlane;fontStyle=1;startSize=30;horizontal=1;whiteSpace=wrap;html=1;align=center;verticalAlign=top;spacingTop=5;fontSize=12;",
            "lane": "swimlane;horizontal=0;startSize=38;whiteSpace=wrap;html=1;align=center;verticalAlign=top;fontStyle=1;fontSize=13;",
            "state": "rounded=1;arcSize=25;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontSize=13;",
            "participant": "rounded=1;arcSize=12;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontStyle=1;fontSize=13;",
            "table": "swimlane;fontStyle=1;startSize=28;horizontal=1;whiteSpace=wrap;html=1;align=left;spacingLeft=8;verticalAlign=top;fontSize=11;",
        }
        style = styles[kind]
        style += f"strokeColor={stroke};fillColor={fill};fontColor={font};fontFamily=Inter;strokeWidth=2;"
        if dashed:
            style += "dashed=1;dashPattern=7 5;"
        style += extra
        cell = ET.SubElement(self.root, "mxCell", id=cell_id, value=label, style=style, vertex="1", parent=parent)
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})
        self.nodes[key] = cell_id
        return cell_id

    def edge(
        self,
        source: str,
        target: str,
        label: str = "",
        *,
        color: str = GREEN,
        dashed: bool = False,
        arrow: str = "block",
        width: int = 2,
        extra: str = "",
    ) -> str:
        cell_id = self._id()
        style = (
            "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
            f"strokeColor={color};fontColor={TEXT};fontFamily=Inter;fontSize=11;strokeWidth={width};"
            f"endArrow={arrow};endFill=1;labelBackgroundColor={WHITE};"
        )
        if dashed:
            style += "dashed=1;dashPattern=7 5;"
        style += extra
        cell = ET.SubElement(
            self.root,
            "mxCell",
            id=cell_id,
            value=label,
            style=style,
            edge="1",
            parent="1",
            source=self.nodes[source],
            target=self.nodes[target],
        )
        ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
        return cell_id

    def save(self) -> Path:
        folder = OUT / f"{self.did}-{slug(self.title)}"
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{self.did}-{slug(self.title)}.drawio"
        ET.indent(self.mxfile, space="  ")
        ET.ElementTree(self.mxfile).write(path, encoding="utf-8", xml_declaration=True)
        return path


def context() -> Canvas:
    c = Canvas("D01", "System Context", "C4 Context", "Current + Proposed", 1600, 950)
    actors = [("owner", "OWNER", 55, 180), ("manager", "MANAGER", 55, 340), ("cashier", "CASHIER / WAITER", 55, 500), ("customer", "Mijoz", 55, 660)]
    for k, l, x, y in actors:
        c.node(k, l, x, y, 95, 110, kind="actor", stroke=GREEN)
    c.node("boundary", "<b>osonCafe Hub ekotizimi</b>", 260, 135, 930, 650, kind="lane", stroke=GREEN, fill="#FBFDFC", extra="horizontal=1;startSize=36;")
    c.node("pos", "<b>POS Web</b><br>Buyurtma · To‘lov · Smena", 330, 230, 220, 95, fill=LIGHT_GREEN, stroke=GREEN)
    c.node("admin", "<b>Admin Web</b><br>Menyu · Xodim · Sozlama", 330, 420, 220, 95, fill=LIGHT_GREEN, stroke=GREEN)
    c.node("tv", "<b>TV Screen</b><br>Navbat · Tayyor holati", 330, 610, 220, 95, fill=LIGHT_GREEN, stroke=GREEN)
    c.node("hub", "<b>Node.js Hub</b><br>Business rules · REST API<br>Auth · Orders · Payments · Shifts", 675, 325, 285, 170, fill=LIGHT_GREEN, stroke=GREEN)
    c.node("db", "<b>SQLite</b><br>Prisma", 760, 570, 120, 110, kind="database", fill=WHITE, stroke=GREEN)
    c.node("printer", "<b>Receipt / Kitchen Printer</b><br><font color='#B7791F'>Partial hardware validation</font>", 1285, 240, 245, 95, fill=PARTIAL_BG, stroke=PARTIAL)
    c.node("cloud", "<b>Future Cloud</b><br>Multi-branch sync<br><font color='#64748B'>Proposed</font>", 1285, 530, 245, 110, fill=PROPOSED_BG, stroke=PROPOSED, dashed=True)
    for a, t, lbl in [("owner", "admin", "boshqaradi"), ("manager", "pos", "ishlaydi"), ("cashier", "pos", "buyurtma/to‘lov"), ("customer", "tv", "holatni ko‘radi")]:
        c.edge(a, t, lbl)
    for s in ["pos", "admin", "tv"]:
        c.edge(s, "hub", "LAN HTTP")
    c.edge("hub", "db", "Prisma")
    c.edge("hub", "printer", "print job", color=PARTIAL)
    c.edge("hub", "cloud", "future secure sync", color=PROPOSED, dashed=True)
    return c


def use_case() -> Canvas:
    c = Canvas("D02", "Use Case", "UML Use Case", "Current + Partial", 1800, 1200)
    for k, l, x, y in [("owner", "OWNER", 40, 190), ("manager", "MANAGER", 40, 430), ("cashier", "CASHIER", 40, 670), ("waiter", "WAITER", 40, 910), ("tech", "Texnik xodim", 1640, 210), ("kitchen", "Oshxona", 1640, 540), ("customer", "Mijoz", 1640, 850)]:
        c.node(k, l, x, y, 100, 120, kind="actor", stroke=GREEN)
    c.node("system", "<b>osonCafe</b>", 210, 130, 1370, 970, kind="lane", stroke=GREEN, fill="#FBFDFC", extra="horizontal=1;startSize=40;")
    cases = [
        ("pair", "Qurilmani pairing qilish", 260, 210), ("pin", "PIN orqali kirish", 260, 360), ("shift", "Smena ochish/yopish", 260, 510),
        ("order", "Buyurtma yaratish", 650, 210), ("stop", "Stop-list boshqarish", 650, 360), ("kflow", "Order holatini yangilash", 650, 510),
        ("pay", "To‘lov / split payment", 1030, 210), ("refund", "Cancel / refund", 1030, 360), ("approve", "Manager approval", 1030, 510),
        ("menu", "Menyu boshqarish", 450, 720), ("staff", "Xodimlarni boshqarish", 450, 870), ("report", "Kunlik / Z-report", 840, 720),
        ("backup", "Backup / restore", 840, 870), ("print", "Chek / kitchen ticket", 1210, 720), ("tv", "TV navbatini ko‘rish", 1210, 870),
    ]
    for k, l, x, y in cases:
        partial = k == "print"
        c.node(k, l + ("<br><font color='#B7791F'>Partial</font>" if partial else ""), x, y, 260, 92, kind="usecase", stroke=PARTIAL if partial else GREEN, fill=PARTIAL_BG if partial else WHITE)
    for a, targets in {
        "owner": ["menu", "staff", "report", "backup", "pair"], "manager": ["pin", "shift", "order", "stop", "refund", "approve", "report"],
        "cashier": ["pin", "shift", "order", "pay", "refund", "print"], "waiter": ["pin", "order", "kflow"], "tech": ["pair", "backup"],
        "kitchen": ["kflow", "print"], "customer": ["tv"],
    }.items():
        for t in targets:
            c.edge(a, t, "", arrow="none", width=1)
    c.edge("refund", "approve", "«include»", dashed=True, color=PROPOSED)
    c.edge("pay", "print", "«extend»", dashed=True, color=PARTIAL)
    return c


def class_box(c: Canvas, key: str, name: str, fields: list[str], x: int, y: int, w: int = 235, h: int = 165, color: str = GREEN) -> None:
    body = "<br>".join([f"{f}" for f in fields])
    c.node(key, f"<b>{name}</b><hr>{body}", x, y, w, h, kind="class", stroke=color, fill=WHITE)


def domain_class() -> Canvas:
    c = Canvas("D03", "Domain Class", "UML Class", "Current", 1900, 1250)
    specs = [
        ("business", "Business", ["+ id: ULID", "+ name: string", "+ active: boolean"], 80, 160),
        ("branch", "Branch", ["+ id: ULID", "+ businessId: FK", "+ name: string"], 380, 160),
        ("user", "User", ["+ id: ULID", "+ branchId: FK", "+ role: Role", "- pinHash: string"], 680, 160),
        ("product", "Product", ["+ id: ULID", "+ categoryId: FK", "+ name: string"], 80, 440),
        ("variant", "ProductVariant", ["+ id: ULID", "+ priceMinor: int", "+ active: boolean"], 380, 440),
        ("modifier", "Modifier", ["+ id: ULID", "+ groupId: FK", "+ priceMinor: int"], 680, 440),
        ("shift", "Shift", ["+ id: ULID", "+ status: ShiftStatus", "+ openingCash: int", "+ closedAt: datetime?"], 980, 160),
        ("order", "Order", ["+ id: ULID", "+ number: int", "+ status: OrderStatus", "+ totalMinor: int"], 980, 440),
        ("item", "OrderItem", ["+ id: ULID", "+ quantity: int", "+ unitPriceMinor: int", "+ nameSnapshot: string"], 1280, 440),
        ("payment", "Payment", ["+ id: ULID", "+ method: PaymentMethod", "+ amountMinor: int", "+ status: PaymentStatus"], 980, 750),
        ("cash", "CashMovement", ["+ id: ULID", "+ shiftId: FK", "+ type: CashType", "+ amountMinor: int"], 1280, 160),
        ("print", "PrintJob", ["+ id: ULID", "+ type: PrintType", "+ status: PrintStatus", "+ attempts: int"], 1580, 440, 235, 165, PARTIAL),
        ("audit", "AuditLog", ["+ id: ULID", "+ actorId: FK?", "+ action: string", "+ payload: JSON"], 1580, 750),
        ("refund", "Refund", ["+ id: ULID", "+ paymentId: FK", "+ amountMinor: int", "+ reason: string"], 1280, 750),
    ]
    for s in specs:
        class_box(c, *s)
    relations = [
        ("business", "branch", "1 owns 1..*"), ("branch", "user", "1 employs 0..*"), ("business", "product", "1 catalogs 0..*"),
        ("product", "variant", "1 composes 1..*"), ("variant", "modifier", "0..* allows 0..*"), ("branch", "shift", "1 has 0..*"),
        ("shift", "order", "1 groups 0..*"), ("order", "item", "1 composes 1..*"), ("order", "payment", "1 has 0..*"),
        ("shift", "cash", "1 records 0..*"), ("payment", "refund", "1 has 0..*"), ("order", "print", "1 queues 0..*"),
        ("user", "audit", "0..1 actor 0..*"),
    ]
    for s, t, l in relations:
        c.edge(s, t, l, color=PARTIAL if t == "print" else GREEN, arrow="open", extra="startArrow=none;")
    c.node("money", "<b>«value object» Money</b><br>minor: integer<br>currency: UZS", 80, 850, 240, 120, fill=LIGHT_GREEN, stroke=GREEN)
    c.edge("money", "variant", "type", dashed=True, color=PROPOSED)
    c.edge("money", "payment", "type", dashed=True, color=PROPOSED)
    return c


def detailed_model() -> Canvas:
    c = Canvas("D04", "Detailed Model", "UML Model Mapping", "Current", 1700, 1050)
    columns = [
        ("dto", "API DTO / Zod", 80, ["CreateOrderRequest", "PaymentRequest", "ShiftCloseRequest", "Public response DTO"]),
        ("domain", "Domain Model", 450, ["Order aggregate", "Payment rules", "Shift rules", "Money value object"]),
        ("prisma", "Prisma Model", 820, ["Order / OrderItem", "Payment / Refund", "Shift / CashMovement", "AuditLog"]),
        ("db", "SQLite", 1190, ["PK / FK", "Unique constraints", "Transaction boundary", "Indexes"]),
    ]
    for key, title, x, items in columns:
        c.node(key, f"<b>{title}</b>", x, 160, 290, 65, fill=LIGHT_GREEN, stroke=GREEN)
        last = key
        for i, item in enumerate(items):
            k = f"{key}{i}"
            c.node(k, item, x, 270 + i * 130, 290, 78, stroke=GREEN, fill=WHITE)
            if i:
                c.edge(f"{key}{i-1}", k, "", color=BORDER, arrow="none", width=1)
    for s, t, l in [("dto0", "domain0", "validate + map"), ("domain0", "prisma0", "repository map"), ("prisma0", "db0", "persist"), ("dto1", "domain1", "server total"), ("domain1", "prisma1", "transaction"), ("prisma1", "db1", "FK/unique")]:
        c.edge(s, t, l)
    c.node("scope", "<b>Cross-cutting invariants</b><br>Business/Branch scope · integer money · no secret in response · timestamps · audit metadata", 250, 830, 1200, 95, fill=BLUE_BG, stroke=BLUE)
    return c


def controller_design() -> Canvas:
    c = Canvas("D05", "Controller Service Repository API", "UML Component / Layered Design", "Current", 1800, 1100)
    layers = [
        ("client", "Clients", 80, ["POS Web", "Admin Web", "TV"]),
        ("api", "HTTP/API", 390, ["Express route", "Zod validation", "Authorization", "Error mapping"]),
        ("service", "Application Service", 730, ["AuthService", "OrderService", "PaymentService", "ShiftService"]),
        ("repo", "Repository", 1080, ["AuthRepository", "OrderRepository", "PaymentRepository", "ShiftRepository"]),
        ("infra", "Infrastructure", 1420, ["Prisma/SQLite", "Print adapter", "Backup adapter", "Pino logger"]),
    ]
    for group, title, x, items in layers:
        c.node(group, f"<b>{title}</b>", x, 150, 250, 65, fill=LIGHT_GREEN, stroke=GREEN)
        for i, item in enumerate(items):
            c.node(f"{group}{i}", item, x, 260 + i * 135, 250, 78, kind="component", stroke=PARTIAL if item == "Print adapter" else GREEN, fill=PARTIAL_BG if item == "Print adapter" else WHITE)
    for i in range(3): c.edge(f"client{i}", f"api{min(i,3)}", "HTTPS/LAN")
    for i in range(4):
        c.edge(f"api{i}", f"service{i}", "validated command")
        c.edge(f"service{i}", f"repo{i}", "port")
        c.edge(f"repo{i}", "infra0", "Prisma")
    c.edge("service1", "infra1", "print job", color=PARTIAL)
    c.edge("service3", "infra2", "backup/restore")
    c.node("cross", "<b>Middleware / policies</b><br>Opaque session · branch scope · idempotency · audit append-only · correlation ID · structured error", 260, 860, 1320, 95, fill=BLUE_BG, stroke=BLUE)
    return c


def sequence(did: str, title: str, status: str, participants: list[str], messages: list[tuple[int, int, str, str]]) -> Canvas:
    c = Canvas(did, title, "UML Sequence", status, 1800, 1100)
    margin, gap = 100, 285
    for i, p in enumerate(participants):
        x = margin + i * gap
        c.node(f"p{i}", f"<b>{p}</b>", x, 135, 210, 62, kind="participant", fill=LIGHT_GREEN if "DB" not in p else WHITE, stroke=GREEN)
        c.node(f"life{i}", "", x + 103, 210, 4, 745, kind="box", stroke=BORDER, fill=BORDER, extra="dashed=1;dashPattern=5 5;")
    y = 245
    for n, (src, dst, label, kind) in enumerate(messages, 1):
        color = RED if kind == "error" else PARTIAL if kind == "partial" else PROPOSED if kind == "proposed" else GREEN
        dashed = kind in {"return", "partial", "proposed"}
        c.node(f"m{n}s", "", margin + src * gap + 97, y, 16, 16, kind="event", stroke=color, fill=color)
        c.node(f"m{n}t", "", margin + dst * gap + 97, y, 16, 16, kind="event", stroke=color, fill=WHITE)
        c.edge(f"m{n}s", f"m{n}t", f"{n}. {label}", color=color, dashed=dashed, arrow="block", width=2, extra="edgeStyle=none;")
        y += 78
    return c


def activity(did: str, title: str, lanes: list[str], steps: list[tuple[int, str, str]], status: str = "Current") -> Canvas:
    c = Canvas(did, title, "UML Activity", status, 1700, 1100)
    lane_w = 500
    for i, lane in enumerate(lanes):
        c.node(f"lane{i}", f"<b>{lane}</b>", 70 + i * lane_w, 130, lane_w, 850, kind="lane", stroke=BORDER, fill="#FBFDFC", extra="horizontal=1;startSize=36;")
    prior = None
    for i, (lane, label, kind) in enumerate(steps):
        x = 130 + lane * lane_w
        y = 190 + i * 68
        k = f"s{i}"
        if kind == "start":
            c.node(k, "", x + 105, y, 36, 36, kind="event", fill=TEXT, stroke=TEXT)
        elif kind == "end":
            c.node(k, "", x + 105, y, 36, 36, kind="end", fill=WHITE, stroke=TEXT)
        elif kind == "decision":
            c.node(k, label, x + 75, y - 10, 100, 72, kind="decision", fill=PARTIAL_BG, stroke=PARTIAL)
        else:
            color = PARTIAL if kind == "partial" else GREEN
            c.node(k, label, x, y, 250, 48, kind="box", fill=PARTIAL_BG if kind == "partial" else WHITE, stroke=color)
        if prior is not None:
            c.edge(prior, k, "", color=PARTIAL if kind == "partial" else GREEN)
        prior = k
    return c


def state_machine(did: str, title: str, states: list[tuple[str, str, int, int, str]], transitions: list[tuple[str, str, str, str]], status: str = "Current") -> Canvas:
    c = Canvas(did, title, "UML State Machine", status, 1700, 1000)
    c.node("start", "", 80, 440, 34, 34, kind="event", fill=TEXT, stroke=TEXT)
    for key, label, x, y, kind in states:
        color = RED if kind == "terminal" else PARTIAL if kind == "partial" else GREEN
        fill = RED_BG if kind == "terminal" else PARTIAL_BG if kind == "partial" else LIGHT_GREEN
        c.node(key, label, x, y, 230, 80, kind="state", stroke=color, fill=fill)
    c.edge("start", states[0][0], "create/open/authenticate")
    for s, t, l, kind in transitions:
        c.edge(s, t, l, color=RED if kind == "error" else PARTIAL if kind == "partial" else GREEN, dashed=kind == "partial")
    c.node("guard", "<b>Guard qoidalari</b><br>Faqat ruxsat etilgan transition · actor role tekshiruvi · invalid transition = 409 · audit log", 360, 790, 980, 90, fill=BLUE_BG, stroke=BLUE)
    return c


def component() -> Canvas:
    c = Canvas("D20", "Component", "UML Component", "Current + Partial", 1750, 1050)
    nodes = [
        ("pos", "POS Web<br>React 19 + Vite", 90, 210, GREEN, LIGHT_GREEN), ("admin", "Admin Web<br>React 19 + Vite", 90, 430, GREEN, LIGHT_GREEN), ("tv", "TV Screen<br>HTTP polling", 90, 650, GREEN, LIGHT_GREEN),
        ("hub", "Hub API<br>Express + TypeScript", 470, 330, GREEN, LIGHT_GREEN), ("domain", "Domain package<br>Money · Order · Shift", 800, 210, GREEN, WHITE),
        ("types", "Shared Types<br>DTO · enums · errors", 800, 470, GREEN, WHITE), ("prisma", "Prisma ORM", 1130, 330, GREEN, WHITE),
        ("db", "SQLite", 1430, 330, GREEN, WHITE), ("printer", "Printer adapter<br>Physical validation", 1130, 650, PARTIAL, PARTIAL_BG),
        ("backup", "Backup/restore<br>ZIP + retention", 1430, 650, GREEN, WHITE),
    ]
    for k, l, x, y, st, fi in nodes:
        kind = "database" if k == "db" else "component"
        c.node(k, l, x, y, 240, 100, kind=kind, stroke=st, fill=fi)
    for s in ["pos", "admin", "tv"]: c.edge(s, "hub", "REST / polling")
    c.edge("hub", "domain", "uses")
    c.edge("hub", "types", "contracts")
    c.edge("hub", "prisma", "repositories")
    c.edge("prisma", "db", "SQL")
    c.edge("hub", "printer", "print jobs", color=PARTIAL)
    c.edge("hub", "backup", "archive")
    c.edge("backup", "db", "copy/restore")
    return c


def architecture(did: str, title: str, proposed: bool) -> Canvas:
    status = "Proposed" if proposed else "Current"
    c = Canvas(did, title, "Architecture", status, 1800, 1100)
    if not proposed:
        for i, (k, l) in enumerate([("pos", "POS Web"), ("admin", "Admin Web"), ("tv", "TV Screen")]):
            c.node(k, l, 90, 220 + i * 220, 250, 95, kind="component", stroke=GREEN, fill=LIGHT_GREEN)
        c.node("hub", "<b>Single Deployable Hub</b><br>Node.js · Express · TypeScript", 520, 250, 430, 120, kind="component", stroke=GREEN, fill=LIGHT_GREEN)
        modules = [("auth", "Auth / Devices"), ("menu", "Menu"), ("orders", "Orders / Payments"), ("ops", "Shifts / Reports"), ("infra", "Print / Backup / Audit")]
        for i, (k, l) in enumerate(modules):
            c.node(k, l, 500 + (i % 2) * 270, 450 + (i // 2) * 135, 230, 72, stroke=PARTIAL if k == "infra" else GREEN, fill=PARTIAL_BG if k == "infra" else WHITE)
            c.edge("hub", k, "module")
        c.node("db", "SQLite<br>single local database", 1180, 360, 250, 130, kind="database", stroke=GREEN, fill=WHITE)
        c.node("lan", "<b>Offline-first LAN</b><br>Internet talab qilinmaydi", 1160, 650, 500, 100, fill=BLUE_BG, stroke=BLUE)
        for s in ["pos", "admin", "tv"]: c.edge(s, "hub", "HTTP")
        for m in ["auth", "menu", "orders", "ops", "infra"]: c.edge(m, "db", "Prisma")
    else:
        c.node("gateway", "API Gateway", 700, 145, 320, 82, kind="component", stroke=PROPOSED, fill=PROPOSED_BG, dashed=True)
        services = [("identity", "Identity Service"), ("catalog", "Catalog Service"), ("sales", "Sales Service"), ("operations", "Operations Service"), ("reporting", "Reporting Service")]
        for i, (k, l) in enumerate(services):
            x = 90 + i * 335
            c.node(k, l, x, 340, 260, 88, kind="component", stroke=PROPOSED, fill=PROPOSED_BG, dashed=True)
            c.node(f"{k}db", f"{l.split()[0]} DB", x + 30, 700, 200, 110, kind="database", stroke=PROPOSED, fill=WHITE, dashed=True)
            c.edge("gateway", k, "REST", color=PROPOSED, dashed=True)
            c.edge(k, f"{k}db", "owns", color=PROPOSED, dashed=True)
        c.node("broker", "Message Broker<br>domain events", 650, 510, 420, 85, kind="component", stroke=PROPOSED, fill=PROPOSED_BG, dashed=True)
        for k, _ in services: c.edge(k, "broker", "event", color=PROPOSED, dashed=True)
        c.node("note", "<b>Migration tamoyili</b><br>Modular boundary’dan bosqichma-bosqich extract; bu joriy production emas.", 420, 870, 960, 80, fill=PARTIAL_BG, stroke=PARTIAL)
    return c


def deployment(did: str, title: str, proposed: bool) -> Canvas:
    c = Canvas(did, title, "UML Deployment", "Proposed" if proposed else "Current + Partial", 1800, 1100)
    if not proposed:
        c.node("hubhost", "<b>«device» Windows Hub Host</b>", 560, 150, 680, 650, kind="lane", stroke=GREEN, fill="#FBFDFC", extra="horizontal=1;startSize=40;")
        c.node("hub", "«artifact» Hub service<br>Node.js/Express", 650, 260, 300, 100, kind="component", stroke=GREEN, fill=LIGHT_GREEN)
        c.node("db", "SQLite database", 710, 470, 180, 120, kind="database", stroke=GREEN, fill=WHITE)
        c.node("backup", "Backup storage", 970, 470, 180, 110, kind="component", stroke=GREEN, fill=WHITE)
        c.node("router", "«device» LAN Router", 90, 420, 260, 100, kind="component", stroke=GREEN, fill=LIGHT_GREEN)
        for i, (k, l) in enumerate([("pos", "POS terminal"), ("admin", "Admin device"), ("tv", "TV display")]):
            c.node(k, f"«device» {l}", 90, 150 + i * 250, 260, 100, kind="component", stroke=GREEN, fill=WHITE)
            c.edge(k, "router", "Wi-Fi/LAN")
        c.node("printer", "«device» ESC/POS Printer<br><font color='#B7791F'>Partial hardware QA</font>", 1390, 330, 300, 120, kind="component", stroke=PARTIAL, fill=PARTIAL_BG)
        c.edge("router", "hub", "HTTP : local port")
        c.edge("hub", "db", "Prisma")
        c.edge("db", "backup", "scheduled/on-demand")
        c.edge("hub", "printer", "TCP/adapter", color=PARTIAL)
    else:
        nodes = [("branch", "Branch Edge Hub", 90, 330), ("internet", "TLS Internet", 420, 330), ("gateway", "Cloud API Gateway", 750, 180), ("cluster", "Service Cluster", 1080, 180), ("broker", "Message Broker", 1080, 480), ("obs", "Observability", 1430, 180), ("backup", "Cloud Backup", 1430, 480)]
        for k, l, x, y in nodes:
            c.node(k, l, x, y, 250, 100, kind="component", stroke=PROPOSED, fill=PROPOSED_BG, dashed=True)
        c.node("dbs", "Database per Service", 1080, 730, 250, 120, kind="database", stroke=PROPOSED, fill=WHITE, dashed=True)
        for s, t, l in [("branch", "internet", "offline queue / TLS"), ("internet", "gateway", "sync"), ("gateway", "cluster", "route"), ("cluster", "broker", "events"), ("cluster", "dbs", "owns"), ("cluster", "obs", "metrics/logs"), ("dbs", "backup", "replication")]:
            c.edge(s, t, l, color=PROPOSED, dashed=True)
        c.node("note", "Conflict resolution, multi-branch sync va cloud operating model — Proposed", 420, 900, 960, 70, fill=PARTIAL_BG, stroke=PARTIAL)
    return c


def erd() -> Canvas:
    c = Canvas("D19", "Database ERD", "Entity Relationship Diagram", "Current", 2400, 1550)
    groups = [
        ("identity", "Core / Identity", 40, 130, 720, 540, GREEN, LIGHT_GREEN, ["Business", "Branch", "User", "Device", "Session", "PairingCode", "PairingAttempt", "TechnicalCode"]),
        ("catalog", "Catalog", 800, 130, 720, 420, BLUE, BLUE_BG, ["Category", "Product", "ProductVariant", "ModifierGroup", "Modifier", "StopListItem"]),
        ("sales", "Sales", 40, 720, 1100, 620, GREEN, LIGHT_GREEN, ["OrderCounter", "Order", "OrderItem", "OrderItemModifier", "Payment", "Discount", "Membership", "Refund"]),
        ("ops", "Operations", 1180, 620, 780, 720, PARTIAL, PARTIAL_BG, ["Shift", "CashMovement", "Printer", "PrintJob", "ZReport", "TvToken"]),
        ("security", "Security / Reliability", 1560, 130, 760, 420, PROPOSED, PROPOSED_BG, ["AuditLog", "IdempotencyRecord"]),
    ]
    positions: dict[str, tuple[int, int]] = {}
    for gk, gl, gx, gy, gw, gh, color, fill, entities in groups:
        c.node(gk, f"<b>{gl}</b>", gx, gy, gw, gh, kind="lane", stroke=color, fill="#FCFDFD", extra="horizontal=1;startSize=34;")
        cols = 3 if gw > 900 else 2
        cell_w = 280 if cols == 3 else 300
        for i, name in enumerate(entities):
            x = gx + 35 + (i % cols) * (cell_w + 35)
            y = gy + 70 + (i // cols) * 130
            key = f"e{name}"
            positions[name] = (x, y)
            c.node(key, f"<b>{name}</b><hr>PK id: ULID<br>FK scopeId · timestamps", x, y, cell_w, 95, kind="table", stroke=color, fill=WHITE)
    relations = [
        ("Business", "Branch", "1:N"), ("Branch", "User", "1:N"), ("Branch", "Device", "1:N"), ("User", "Session", "1:N"),
        ("Business", "Category", "1:N"), ("Category", "Product", "1:N"), ("Product", "ProductVariant", "1:N"), ("ProductVariant", "StopListItem", "1:N"),
        ("Branch", "Shift", "1:N"), ("Shift", "Order", "1:N"), ("Order", "OrderItem", "1:N"), ("OrderItem", "OrderItemModifier", "1:N"),
        ("Order", "Payment", "1:N"), ("Payment", "Refund", "1:N"), ("Shift", "CashMovement", "1:N"), ("Shift", "ZReport", "1:1"),
        ("Order", "PrintJob", "1:N"), ("Printer", "PrintJob", "1:N"), ("User", "AuditLog", "0..1:N"), ("Order", "IdempotencyRecord", "logical")
    ]
    for a, b, l in relations:
        c.edge(f"e{a}", f"e{b}", l, color=PARTIAL if "Print" in b else GREEN, arrow="open", width=1)
    return c


def bpmn(did: str, title: str, lanes: list[str], flow: list[tuple[int, str, str]], status: str) -> Canvas:
    c = Canvas(did, title, "BPMN 2.0", status, 1900, 1200)
    lane_h = 270
    for i, lane in enumerate(lanes):
        c.node(f"lane{i}", f"<b>{lane}</b>", 60, 135 + i * lane_h, 1770, lane_h, kind="lane", stroke=BORDER, fill="#FBFDFC")
    prev = None
    for i, (lane, label, kind) in enumerate(flow):
        x = 180 + i * 145
        y = 215 + lane * lane_h
        k = f"f{i}"
        if kind == "start": c.node(k, "", x, y, 42, 42, kind="event", fill=WHITE, stroke=GREEN)
        elif kind == "end": c.node(k, "", x, y, 42, 42, kind="end", fill=WHITE, stroke=GREEN)
        elif kind == "gateway": c.node(k, label, x - 10, y - 12, 76, 66, kind="decision", fill=PARTIAL_BG, stroke=PARTIAL)
        else: c.node(k, label, x - 35, y - 12, 125, 66, kind="box", fill=PARTIAL_BG if kind == "partial" else WHITE, stroke=PARTIAL if kind == "partial" else GREEN)
        if prev is not None: c.edge(prev, k, "", color=PARTIAL if kind == "partial" else GREEN)
        prev = k
    return c


def diagrams() -> list[Canvas]:
    result: list[Canvas] = [context(), use_case(), domain_class(), detailed_model(), controller_design()]
    result.extend([
        sequence("D06", "PIN Login Session", "Current", ["Employee", "POS", "Hub API", "Auth Service", "Repository", "SQLite DB"], [
            (0,1,"PIN kiritadi","normal"),(1,2,"POST /auth/pin + device","normal"),(2,3,"Zod + rate limit","normal"),(3,4,"user/session lookup","normal"),(4,5,"scoped query","normal"),(5,4,"user + hash","return"),(3,3,"argon2id verify","normal"),(3,4,"opaque session yaratish","normal"),(4,5,"transaction + audit","normal"),(2,1,"session cookie + role","return")]),
        sequence("D07", "Create Order", "Current", ["Waiter", "POS", "Orders API", "Order Service", "Repository", "SQLite DB"], [
            (0,1,"item/variant/modifier tanlaydi","normal"),(1,2,"POST /orders + idempotency","normal"),(2,3,"auth + schema validation","normal"),(3,4,"menu/stop-list lookup","normal"),(4,5,"scoped read","normal"),(3,3,"server total + price snapshot","normal"),(3,4,"create transaction","normal"),(4,5,"order/items/audit","normal"),(5,4,"committed order","return"),(2,1,"201 order + number","return")]),
        sequence("D08", "Kitchen Flow", "Current + Partial", ["Cashier", "POS", "Order Service", "Print Service", "Printer/Kitchen", "TV"], [
            (0,1,"buyurtmani tasdiqlaydi","normal"),(1,2,"confirm order","normal"),(2,3,"kitchen PrintJob yaratish","normal"),(3,4,"ESC/POS yuborish","partial"),(2,5,"confirmed queue","normal"),(4,2,"preparing / ready","normal"),(2,5,"polling response","return"),(2,1,"status update","return")]),
        sequence("D09", "Payment", "Current + Partial", ["Cashier", "POS", "Payment API", "Payment Service", "Repository", "SQLite DB"], [
            (0,1,"method / split amounts","normal"),(1,2,"POST /payments + key","normal"),(2,3,"auth + schema","normal"),(3,4,"order + idempotency lookup","normal"),(4,5,"transaction read","normal"),(3,3,"sum = payable total","normal"),(3,4,"payment + order complete","normal"),(4,5,"atomic commit + audit","normal"),(3,3,"receipt PrintJob queue","partial"),(2,1,"payment result","return")]),
        sequence("D10", "Shift Close Z Report", "Current", ["Manager", "POS", "Shift API", "Report Service", "Repository", "SQLite DB"], [
            (0,1,"actual cash kiritadi","normal"),(1,2,"POST /shift/close","normal"),(2,3,"authorization","normal"),(3,4,"orders/payments/cash movements","normal"),(4,5,"aggregate query","normal"),(3,3,"expected vs actual","normal"),(3,4,"close shift + ZReport","normal"),(4,5,"atomic commit + audit","normal"),(2,1,"closed shift + difference","return")]),
        sequence("D11", "Cancel Refund Approval", "Current", ["Cashier", "Manager", "POS", "Policy Service", "Payment Service", "SQLite DB"], [
            (0,2,"cancel/refund so‘rovi","normal"),(2,3,"role + status + limit","normal"),(3,1,"manager approval talab","normal"),(1,2,"approval credential","normal"),(2,4,"refund command + reason","normal"),(4,5,"original payment lookup","normal"),(4,5,"refund + audit transaction","normal"),(4,2,"refund result","return"),(2,0,"success receipt","return")]),
    ])
    result.extend([
        activity("D12", "Order Activity", ["Staff", "POS", "Hub"], [(0,"", "start"),(0,"PIN login", "task"),(2,"Session va aktiv shift", "decision"),(1,"Menyu / item tanlash", "task"),(1,"Variant, modifier, note", "task"),(2,"Stop-list va narx", "decision"),(2,"Server total / snapshot", "task"),(0,"Tasdiqlash", "task"),(2,"Order yaratish", "task"),(0,"", "end")]),
        activity("D13", "Preparation Activity", ["Hub", "Kitchen/Printer", "Staff/TV"], [(0,"", "start"),(0,"Confirmed order", "task"),(0,"PrintJob / queue", "partial"),(1,"Ticket yoki ekran", "partial"),(1,"Preparing", "task"),(1,"Ready", "task"),(2,"TV yangilanadi", "task"),(2,"Mijozga topshirish", "task"),(0,"Completed", "task"),(0,"", "end")], "Current + Partial"),
        activity("D14", "Payment Activity", ["Cashier", "POS", "Hub"], [(0,"", "start"),(0,"Method/split tanlash", "task"),(1,"Summalarni kiritish", "task"),(2,"Total tengmi?", "decision"),(2,"Idempotency tekshiruvi", "task"),(2,"Atomic payment commit", "task"),(2,"Receipt job", "partial"),(1,"Success ko‘rsatish", "task"),(0,"", "end")], "Current + Partial"),
        activity("D15", "Shift Activity", ["Manager/Cashier", "POS", "Hub"], [(0,"", "start"),(2,"Aktiv shift bormi?", "decision"),(0,"Opening cash", "task"),(2,"Shift open", "task"),(1,"Sales/cash movement loop", "task"),(0,"Close request + actual", "task"),(2,"Open order / reconcile", "decision"),(2,"ZReport + close", "task"),(0,"", "end")]),
    ])
    result.extend([
        state_machine("D16", "Order State Machine", [("draft","Draft",200,180,"normal"),("confirmed","Confirmed",560,180,"normal"),("preparing","Preparing",920,180,"normal"),("ready","Ready",1280,180,"normal"),("completed","Completed",1280,520,"terminal"),("cancelled","Cancelled",560,520,"terminal")], [("draft","confirmed","confirm [active shift]","normal"),("confirmed","preparing","start preparation","normal"),("preparing","ready","mark ready","normal"),("ready","completed","handoff / paid","normal"),("draft","cancelled","cancel [reason]","error"),("confirmed","cancelled","cancel [approval]","error")]),
        state_machine("D17", "Payment Session State Machine", [("pending","Payment: Pending",200,180,"normal"),("succeeded","Payment: Succeeded",560,180,"normal"),("partial","Partially Refunded",920,180,"partial"),("refunded","Refunded",1280,180,"terminal"),("active","Session: Active",200,520,"normal"),("locked","Locked",560,520,"partial"),("expired","Expired",920,520,"terminal"),("revoked","Revoked",1280,520,"terminal")], [("pending","succeeded","commit","normal"),("succeeded","partial","partial refund","partial"),("partial","refunded","remaining refund","normal"),("active","locked","lockout/manual lock","partial"),("active","expired","TTL reached","error"),("active","revoked","deactivate/logout","error"),("locked","active","authorized unlock","normal")]),
        state_machine("D18", "Shift State Machine", [("none","No Active Shift",200,320,"normal"),("open","Open",580,320,"normal"),("closing","Closing / Reconcile",960,320,"partial"),("closed","Closed + ZReport",1340,320,"terminal")], [("none","open","open [no active shift]","normal"),("open","closing","close request","partial"),("closing","open","validation fails","error"),("closing","closed","reconciled + commit","normal")]),
    ])
    result.extend([erd(), component(), architecture("D21", "Current Modular Monolith", False), architecture("D22", "Proposed Microservices", True), deployment("D23", "Current Hub Only Deployment", False), deployment("D24", "Proposed Microservices Deployment", True)])
    result.extend([
        bpmn("D25", "Order Lifecycle", ["Customer", "Waiter/Cashier", "POS / Hub", "Kitchen"], [(0,"","start"),(0,"Buyurtma beradi","task"),(1,"Buyurtmani kiritadi","task"),(2,"Mavjudmi?","gateway"),(2,"Validate va confirm","task"),(3,"Tayyorlash","task"),(3,"Ready","task"),(1,"Topshirish","task"),(0,"","end")], "Current"),
        bpmn("D26", "Payment Receipt", ["Customer", "Cashier", "Hub", "Payment / Printer adapter"], [(0,"","start"),(1,"Method/split","task"),(2,"Summa to‘g‘rimi?","gateway"),(2,"Idempotent commit","task"),(3,"Receipt print","partial"),(1,"Natijani beradi","task"),(0,"","end")], "Current + Partial"),
        bpmn("D27", "Shift Reporting", ["Manager/Cashier", "Hub", "Owner"], [(0,"","start"),(0,"Shift open","task"),(1,"Sales/cash loop","task"),(0,"Close + actual","task"),(1,"Reconcile","gateway"),(1,"ZReport","task"),(2,"Daily report","task"),(2,"Admin aggregation","partial"),(2,"","end")], "Current + Partial"),
    ])
    return result


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    produced = []
    for diagram in diagrams():
        produced.append(diagram.save())
    print(f"Generated {len(produced)} editable Draw.io files")
    for path in produced:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
