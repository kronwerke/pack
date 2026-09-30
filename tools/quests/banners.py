#!/usr/bin/env python3
"""Renders the lettering of the quest book: chapter titles and section headings.

FTB Quests draws images on a chapter's canvas and inside quest texts. Everything here is
text in Big Shoulders Display (the website's type, SIL Open Font Licence, see fonts/) on
a transparent background, written into kubejs/assets/kronwerke/textures/quests/, which
KubeJS hands to every client as a resource pack. Same input, same file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = {
    "title": os.path.join(HERE, "fonts", "BigShouldersDisplay-800.ttf"),
    "section": os.path.join(HERE, "fonts", "BigShouldersDisplay-800.ttf"),
    "note": os.path.join(HERE, "fonts", "BigShouldersDisplay-600.ttf"),
}
SIZE = {"title": 96, "section": 56, "note": 40}
COLOURS = {
    # top, bottom of the letters
    "brass": ((246, 214, 140), (196, 140, 58)),
    "magic": ((226, 206, 255), (150, 110, 214)),
    "nature": ((200, 236, 160), (104, 168, 72)),
    "stone": ((236, 230, 220), (160, 150, 138)),
    "fire": ((255, 196, 120), (206, 86, 52)),
    "water": ((180, 226, 255), (72, 140, 214)),
    "end": ((236, 214, 255), (120, 86, 170)),
}
OUTLINE = (22, 16, 10, 255)


def render(text, kind="section", colour="brass"):
    """The lettering as an RGBA image."""
    font = ImageFont.truetype(FONT[kind], SIZE[kind])
    text = text.upper()
    pad = max(6, SIZE[kind] // 10)
    left, top, right, bottom = font.getbbox(text)
    w, h = right - left + 2 * pad, bottom - top + 2 * pad
    ox, oy = pad - left, pad - top

    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((ox, oy), text, font=font, fill=255)

    # vertical gradient in the letters
    top_c, bottom_c = COLOURS[colour]
    grad = Image.new("RGBA", (w, h))
    px = grad.load()
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(round(top_c[i] + (bottom_c[i] - top_c[i]) * t) for i in range(3))
        for x in range(w):
            px[x, y] = c + (255,)

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # outline and a small shadow, then the letters
    stroke = max(2, SIZE[kind] // 24)
    edge = Image.new("L", (w, h), 0)
    ImageDraw.Draw(edge).text((ox, oy), text, font=font, fill=255, stroke_width=stroke, stroke_fill=255)
    shadow = Image.new("L", (w, h), 0)
    shadow.paste(edge, (stroke, stroke))
    out.paste(Image.new("RGBA", (w, h), (0, 0, 0, 150)), (0, 0), shadow)
    out.paste(Image.new("RGBA", (w, h), OUTLINE), (0, 0), edge)
    out.paste(grad, (0, 0), mask)
    if kind == "title":
        # a thin rule under chapter titles
        d = ImageDraw.Draw(out)
        y = h - pad // 2
        d.rectangle((pad, y - 2, w - pad, y), fill=bottom_c + (255,))
    return out


def write(path, text, kind, colour):
    """Renders into path (creating folders) and answers (width, height) in pixels."""
    img = render(text, kind, colour)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, optimize=True)
    return img.size


def measure(text, kind):
    """The size render() would produce, without drawing."""
    font = ImageFont.truetype(FONT[kind], SIZE[kind])
    pad = max(6, SIZE[kind] // 10)
    left, top, right, bottom = font.getbbox(text.upper())
    return right - left + 2 * pad, bottom - top + 2 * pad
