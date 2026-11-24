#!/usr/bin/env python3
"""Render the news-image-20261123 entry: a 1024x1024 front-page infographic
summing up world news of Monday 23 November 2026.

Built from verified reporting (AP, The Guardian, Principia, Middle East Eye,
betabriefing). All text is drawn with PIL (no generated-image text, so every
word is legible and accurate). Deterministic: same bytes on every run.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (246, 241, 231)
INK = (20, 33, 61)
NAVY = (15, 31, 61)
GOLD = (201, 162, 39)
RED = (179, 38, 30)
CARD = (255, 255, 255)
BORDER = (216, 210, 196)
GREY = (90, 90, 86)
GREEN = (46, 125, 50)
BLUE = (29, 78, 158)
PURPLE = (123, 31, 162)
ORANGE = (230, 81, 0)
TEAL = (0, 105, 92)
SKY = (46, 134, 193)
SKY_LIGHT = (127, 179, 213)
LAND = (88, 160, 92)

FD = "/usr/share/fonts/truetype/dejavu/"
FN = "/usr/share/fonts/truetype/noto/"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF_B = font(FD + "DejaVuSerif-Bold.ttf", 62)
SERIF_B_SM = font(FD + "DejaVuSerif-Bold.ttf", 52)
SANS_B = font(FN + "NotoSans-Bold.ttf", 26)
SANS_B_SM = font(FN + "NotoSans-Bold.ttf", 22)
SANS_B_XS = font(FN + "NotoSans-Bold.ttf", 19)
SANS = font(FN + "NotoSans-Regular.ttf", 22)
SANS_SM = font(FN + "NotoSans-Regular.ttf", 20)
SANS_FOOT = font(FN + "NotoSans-Regular.ttf", 18)
TAG = font(FN + "NotoSans-Bold.ttf", 20)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(img, cx, cy, r):
    """Blue globe with graticule and a red NO DEAL sash."""
    layer = Image.new("RGBA", (2 * r + 20, 2 * r + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([10, 10, 10 + 2 * r, 10 + 2 * r], fill=SKY + (255,))
    mask = Image.new("L", (2 * r + 20, 2 * r + 20), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([10, 10, 10 + 2 * r, 10 + 2 * r], fill=255)
    # land blobs, clipped to the circle via the mask applied to alpha
    land = Image.new("RGBA", (2 * r + 20, 2 * r + 20), (0, 0, 0, 0))
    ld = ImageDraw.Draw(land)
    ld.ellipse([10 + int(r * 0.15), 10 + int(r * 0.15), 10 + int(r * 0.85), 10 + int(r * 0.55)], fill=LAND + (255,))
    ld.ellipse([10 + int(r * 0.55), 10 + int(r * 0.95), 10 + int(r * 1.25), 10 + int(r * 1.45)], fill=LAND + (255,))
    ld.ellipse([10 + int(r * 1.05), 10 + int(r * 0.35), 10 + int(r * 1.55), 10 + int(r * 0.75)], fill=LAND + (255,))
    alpha = land.split()[3]
    alpha = Image.composite(alpha, Image.new("L", alpha.size, 0), mask)
    land.putalpha(alpha)
    layer.alpha_composite(land)
    # graticule
    d.ellipse([10, 10, 10 + 2 * r, 10 + 2 * r], outline=(255, 255, 255, 160), width=3)
    d.ellipse([10 + r // 2, 10, 10 + 3 * r // 2, 10 + 2 * r], outline=(255, 255, 255, 130), width=2)
    d.line([10, 10 + r, 10 + 2 * r, 10 + r], fill=(255, 255, 255, 130), width=2)
    d.arc([10, 10 + r // 3, 10 + 2 * r, 10 + 5 * r // 3], 0, 180, fill=(255, 255, 255, 130), width=2)
    d.arc([10, 10 - r // 3, 10 + 2 * r, 10 + r], 180, 360, fill=(255, 255, 255, 130), width=2)
    # red sash
    sash = Image.new("RGBA", (2 * r + 60, 44), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sash)
    sd.rectangle([0, 0, 2 * r + 60, 44], fill=RED + (255,))
    sd.text((30, 6), "NO DEAL", font=font(FN + "NotoSans-Bold.ttf", 28), fill=(255, 255, 255, 255))
    sash = sash.rotate(-14, expand=True, resample=Image.BICUBIC)
    layer.alpha_composite(sash, (r - sash.width // 2 + 10, r - sash.height // 2 + 10))
    img.alpha_composite(layer, (cx - r - 10, cy - r - 10))


def main():
    img = Image.new("RGBA", (W, H), PAPER + (255,))
    d = ImageDraw.Draw(img, "RGBA")

    # ---- Masthead ----
    d.rectangle([0, 0, W, 132], fill=NAVY)
    d.text((W // 2, 22), "THE WORLD IN ONE DAY", font=SERIF_B, fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 92), "M O N D A Y ,  2 3  N O V E M B E R  2 0 2 6", font=SANS_B, fill=GOLD, anchor="ma")
    d.line([40, 132, W - 40, 132], fill=GOLD, width=4)

    # ---- Hero: COP31 ----
    d.rounded_rectangle([40, 152, 984, 402], radius=10, fill=CARD, outline=BORDER, width=2)
    d.text((64, 170), "CLIMATE  •  ANTALYA, TURKEY", font=TAG, fill=RED)
    d.text((64, 200), "CLIMATE TALKS", font=SERIF_B_SM, fill=INK)
    d.text((64, 258), "COLLAPSE", font=SERIF_B_SM, fill=INK)
    hero_body = ("COP31 ends with no deal — more than 90 nations reject a draft "
                 "that never mentions fossil fuels. The first total failure of a "
                 "UN climate summit since 2009.")
    y = 322
    for line in wrap(d, hero_body, SANS, 560):
        d.text((64, y), line, font=SANS, fill=(40, 40, 40))
        y += 28
    draw_globe(img, 830, 278, 92)

    # ---- Story cards ----
    cards = [
        ("WAR AT SEA  •  LIBYA", RED, "Ukraine sinks Russian warship",
         "Seven sea drones sink the corvette Merkury at Benghazi. The war reaches the Mediterranean."),
        ("UKRAINE  •  KYIV REGION", BLUE, "Strike kills 11 near Kyiv",
         "A Russian strike hits an apartment block in Dymer. A boy, 7, is pulled alive from the rubble."),
        ("MIDDLE EAST  •  IRAN", PURPLE, "Trump warns of new strikes",
         "The US president says strikes on Iran resume after the New Year if talks fail."),
        ("ASIA  •  INDONESIA", ORANGE, "Factory fire kills 24",
         "A blaze at a sweets factory in Banten leaves at least 24 dead and about 30 missing."),
    ]
    x0s = [40, 528]
    y0s = [422, 603]
    for i, (tag, color, head, body) in enumerate(cards):
        x0, y0 = x0s[i % 2], y0s[i // 2]
        d.rounded_rectangle([x0, y0, x0 + 456, y0 + 165], radius=10, fill=CARD, outline=BORDER, width=2)
        d.rectangle([x0, y0, x0 + 8, y0 + 165], fill=color)
        d.text((x0 + 24, y0 + 14), tag, font=TAG, fill=color)
        hy = y0 + 42
        for line in wrap(d, head, SANS_B_SM, 408):
            d.text((x0 + 24, hy), line, font=SANS_B_SM, fill=INK)
            hy += 28
        by = hy + 6
        for line in wrap(d, body, SANS_SM, 408):
            d.text((x0 + 24, by), line, font=SANS_SM, fill=(60, 60, 60))
            by += 25

    # ---- Bottom strip: markets + science ----
    d.rounded_rectangle([40, 788, 496, 906], radius=10, fill=CARD, outline=BORDER, width=2)
    d.rectangle([40, 788, 48, 906], fill=TEAL)
    d.text((64, 800), "MARKETS", font=TAG, fill=TEAL)
    d.text((64, 826), "Asian tech shares fall", font=SANS_B_SM, fill=INK)
    d.text((64, 856), "as the AI sell-off deepens.", font=SANS_SM, fill=(60, 60, 60))

    d.rounded_rectangle([528, 788, 984, 906], radius=10, fill=CARD, outline=BORDER, width=2)
    d.rectangle([528, 788, 536, 906], fill=GREEN)
    d.text((552, 800), "SCIENCE", font=TAG, fill=GREEN)
    d.text((552, 826), "BepiColombo reaches Mercury", font=SANS_B_SM, fill=INK)
    d.text((552, 856), "after an eight-year journey.", font=SANS_SM, fill=(60, 60, 60))

    # ---- Footer ----
    d.text((W // 2, 928), "Also: AI claims a proof of the Riemann hypothesis  •  Alcaraz wins the ATP Finals",
           font=SANS_FOOT, fill=GREY, anchor="ma")
    d.text((W // 2, 958), "Sources: AP  •  The Guardian  •  Principia  •  Middle East Eye  —  Events of Monday 23 November 2026",
           font=SANS_FOOT, fill=GREY, anchor="ma")

    img.convert("RGB").save(OUT, format="PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
