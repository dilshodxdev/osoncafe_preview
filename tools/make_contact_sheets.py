from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tmp" / "diagram-qa"
OUT.mkdir(parents=True, exist_ok=True)

files = sorted((ROOT / "04-Diagrams").glob("D*/D*.png"))
font = ImageFont.load_default(size=18)
for sheet_no in range(0, len(files), 9):
    page = Image.new("RGB", (1800, 1260), "white")
    draw = ImageDraw.Draw(page)
    for slot, path in enumerate(files[sheet_no:sheet_no + 9]):
        row, col = divmod(slot, 3)
        x, y = 20 + col * 590, 20 + row * 410
        image = Image.open(path).convert("RGB")
        image.thumbnail((550, 350), Image.Resampling.LANCZOS)
        ox = x + (550 - image.width) // 2
        oy = y + 32 + (350 - image.height) // 2
        page.paste(image, (ox, oy))
        draw.text((x, y), path.stem, fill="#17211D", font=font)
        draw.rectangle((x, y + 30, x + 550, y + 385), outline="#CBD5D1", width=2)
    target = OUT / f"diagram-contact-{sheet_no // 9 + 1}.png"
    page.save(target, optimize=True)
    print(target)
