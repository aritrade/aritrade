"""
Generates a sleek monogram avatar (assets/avatar.png) for the profile README.

Output: 480x480 PNG with a soft dark-emerald gradient, a thin emerald ring,
and the initials "AD" set in HelveticaNeue. Drop in a real LinkedIn photo
at the same path to override.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = Path(__file__).resolve().parent / "avatar.png"
SIZE = 480

BG_TOP = (11, 17, 23)
BG_BOTTOM = (16, 24, 35)
ACCENT = (16, 185, 129)
ACCENT_SOFT = (16, 185, 129, 70)
TEXT = (244, 244, 245)

FONT_PATH = "/System/Library/Fonts/HelveticaNeue.ttc"


def vertical_gradient(size: int, top, bottom) -> Image.Image:
    img = Image.new("RGB", (size, size), top)
    pixels = img.load()
    for y in range(size):
        t = y / (size - 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        for x in range(size):
            pixels[x, y] = (r, g, b)
    return img


def main() -> None:
    base = vertical_gradient(SIZE, BG_TOP, BG_BOTTOM).convert("RGBA")

    glow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([(SIZE * 0.15, SIZE * 0.15), (SIZE * 0.85, SIZE * 0.85)], fill=ACCENT_SOFT)
    glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
    base = Image.alpha_composite(base, glow)

    draw = ImageDraw.Draw(base)
    ring_inset = 14
    draw.ellipse(
        [(ring_inset, ring_inset), (SIZE - ring_inset, SIZE - ring_inset)],
        outline=ACCENT,
        width=4,
    )

    try:
        fnt = ImageFont.truetype(FONT_PATH, 220)
    except Exception:
        fnt = ImageFont.load_default()

    text = "AD"
    bbox = draw.textbbox((0, 0), text, font=fnt, anchor="lt")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (SIZE - text_w) // 2 - bbox[0]
    text_y = (SIZE - text_h) // 2 - bbox[1] - 8
    draw.text((text_x, text_y), text, font=fnt, fill=TEXT)

    underline_y = SIZE - SIZE * 0.22
    underline_w = SIZE * 0.18
    underline_x0 = (SIZE - underline_w) / 2
    draw.line(
        [(underline_x0, underline_y), (underline_x0 + underline_w, underline_y)],
        fill=ACCENT,
        width=4,
    )

    base.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
