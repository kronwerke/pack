#!/usr/bin/env python3
"""Builds the 32x32 textures of the Kronwerke milestone items from the CC0 sheets in
tools/items/sources/ (see CREDITS.md there).

    python3 tools/items/compose.py

Output: kubejs/assets/kronwerke/textures/item/<name>.png
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "sources")
OUT = os.path.join(os.path.dirname(os.path.dirname(HERE)), "kubejs", "assets", "kronwerke", "textures", "item")


def load(name):
    return Image.open(os.path.join(SRC, name)).convert("RGBA")


def cell(name, col, row, size=32):
    return load(name).crop((col * size, row * size, col * size + size, row * size + size))


def centred(img):
    out = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    out.paste(img, ((32 - img.size[0]) // 2, (32 - img.size[1]) // 2), img)
    return out


def shrink(img, longest):
    img = img.crop(img.getbbox())
    k = longest / max(img.size)
    return img.resize((max(1, round(img.size[0] * k)), max(1, round(img.size[1] * k))), Image.NEAREST)


def inlay(base, gem, dy=0):
    out = base.copy()
    out.paste(gem, ((32 - gem.size[0]) // 2, (32 - gem.size[1]) // 2 + dy), gem)
    return out


ITEMS = {
    "stone_gearbox": lambda: centred(load("cog-big-21.png")),
    "source_keystone": lambda: cell("rune-dcss.png", 2, 1),
    "brass_heart": lambda: inlay(centred(load("cog-big-30.png")), shrink(cell("gem-ettingrinder.png", 0, 2), 18), 1),
    "rune_core": lambda: cell("rune-dcss.png", 4, 3),
    "steel_core": lambda: inlay(centred(load("cog-big-32.png")), shrink(cell("gem-ettingrinder.png", 1, 0), 12)),
    "elven_star": lambda: cell("gem-7soul1_1.png", 0, 2),
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, make in ITEMS.items():
        make().save(os.path.join(OUT, name + ".png"))
        print("built", name)
