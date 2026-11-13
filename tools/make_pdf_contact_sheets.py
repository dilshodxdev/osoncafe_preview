from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "pdfs"
OUT = ROOT / "tmp" / "pdf-qa"
OUT.mkdir(parents=True, exist_ok=True)

pages = sorted(SOURCE.glob("osoncafe-page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
font = ImageFont.load_default(size=20)
for offset in range(0, len(pages), 10):
    sheet = Image.new("RGB", (1800, 2400), "white")
    draw = ImageDraw.Draw(sheet)
    for slot, page_path in enumerate(pages[offset:offset + 10]):
        row, col = divmod(slot, 2)
        x, y = 30 + col * 880, 30 + row * 470
        page = Image.open(page_path).convert("RGB")
        page.thumbnail((820, 410), Image.Resampling.LANCZOS)
        px = x + (820 - page.width) // 2
        py = y + 30 + (410 - page.height) // 2
        sheet.paste(page, (px, py))
        draw.text((x, y), f"Page {offset + slot + 1}", fill="#17211D", font=font)
        draw.rectangle((x, y + 28, x + 820, y + 445), outline="#CBD5D1", width=2)
    target = OUT / f"pdf-contact-{offset // 10 + 1}.png"
    sheet.save(target, optimize=True)
    print(target)
