#!/usr/bin/env python3
"""Draws the 16x16 textures of the Kronwerke milestone items.

    python3 tools/items/draw.py

Each item is a character grid; every character is a palette colour, "." is transparent.
Output: kubejs/assets/kronwerke/textures/item/<name>.png
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "kubejs", "assets", "kronwerke", "textures", "item")

ITEMS = {
    # grey andesite gear around a wooden axle
    "stone_gearbox": ({
        "o": "#2b2b2e", "g": "#8d8f8a", "h": "#b9bbb5", "s": "#65675f", "w": "#9c6b3c", "d": "#5e3d20", "c": "#c8a15a",
    }, [
        "......oooo......",
        "......ohho......",
        "..oo..oggo..oo..",
        "..ohooogggooho..",
        "...ogggggggggo..",
        "..oggsssssshgo..",
        "oooggsowwosggooo",
        "ohgggswcdwsgggho",
        "osgggswddwsgggso",
        "oooggsowwosggooo",
        "..oggsssssssgo..",
        "...oggggggggso..",
        "..osooogggooso..",
        "..oo..oggo..oo..",
        "......osso......",
        "......oooo......",
    ]),
    # a purple source gem set in a stone frame
    "source_keystone": ({
        "o": "#252329", "s": "#7a7680", "h": "#a9a5ad", "p": "#8a3fd1", "l": "#c792f2", "w": "#f3e3ff", "d": "#4f1f82",
    }, [
        "................",
        ".......oo.......",
        "......ohso......",
        ".....ohssso.....",
        "....ohsooss o...",
        "...ohsoplposs o.",
        "..ohsoplwlposso.",
        ".ohsoplwwllpo so",
        ".osoplllllpddoso",
        "..osopllppddoso.",
        "...osoppdddoso..",
        "....osoddd oso..",
        ".....osoooso....",
        "......ossso.....",
        ".......oso......",
        "........o.......",
    ]),
    # a brass heart with a gear in its middle
    "brass_heart": ({
        "o": "#3a2408", "b": "#c7902b", "h": "#f2d27a", "d": "#8a5a14", "g": "#5b4a3a", "r": "#e2542a",
    }, [
        "................",
        "..oooo....oooo..",
        ".ohhbbo..obbbbo.",
        "ohhbbbbooobbbbdo",
        "ohbbbbbbbbbbbbdo",
        "ohbbbbgggbbbbbdo",
        "ohbbbgggggbbbbdo",
        "obbbbggrggbbbddo",
        ".obbbgggggbbbdo.",
        ".obbbbgggbbbddo.",
        "..obbbbbbbbbdo..",
        "...obbbbbbbddo..",
        "....obbbbbddo...",
        ".....obbbddo....",
        "......obddo.....",
        ".......oo.......",
    ]),
    # an orb split into the four element colours, bound by a terrasteel ring
    "rune_core": ({
        "o": "#123015", "t": "#4fbf3a", "l": "#9cf07e", "b": "#3f7de0", "r": "#e0483f", "y": "#e6c84a", "e": "#7a5a2e", "w": "#ffffff",
    }, [
        "................",
        ".....oooooo.....",
        "...oottllttoo...",
        "..otbbbbrrrrto..",
        "..otbbbbrrrrto..",
        ".otbbbbbrrrrrto.",
        ".olbbbbbrrrrrlo.",
        ".olbbbbwwrrrrlo.",
        ".oleeeewwyyyylo.",
        ".oleeeeeyyyyylo.",
        ".oteeeeeyyyyyto.",
        "..oteeeeyyyyto..",
        "..oteeeeyyyyto..",
        "...oottllttoo...",
        ".....oooooo.....",
        "................",
    ]),
    # a steel block with cyan circuit lines around a glowing core
    "steel_core": ({
        "o": "#15171b", "s": "#5a6270", "h": "#8e98a8", "d": "#3a404b", "c": "#39d0e6", "w": "#d9fbff",
    }, [
        "................",
        ".oooooooooooooo.",
        ".ohhhhhhhhhhhso.",
        ".ohssssssssssdo.",
        ".ohscccssscccdo.",
        ".ohscssssssscdo.",
        ".ohscsooooscsdo.",
        ".ohsssowwosssdo.",
        ".ohsssowwosssdo.",
        ".ohscsooooscsdo.",
        ".ohscssssssscdo.",
        ".ohscccssscccdo.",
        ".ohssssssssssdo.",
        ".osdddddddddddo.",
        ".oooooooooooooo.",
        "................",
    ]),
    # a four pointed star of elven metal with a green heart
    "elven_star": ({
        "o": "#3b1435", "p": "#e27fd0", "l": "#ffc3f0", "d": "#a2449a", "g": "#58d67a", "w": "#eaffea",
    }, [
        ".......oo.......",
        ".......olo......",
        "......olpdo.....",
        "......olpdo.....",
        "..o..olppdo..o..",
        "...ooolpppoooo..",
        "....olppgppdo...",
        ".oollppgwgppddo.",
        "oolllppwwgppddoo",
        ".oolppppgppddoo.",
        "....odppppddo...",
        "...oooppppdooo..",
        "..o..odppdo..o..",
        "......odddo.....",
        ".......odo......",
        "........o.......",
    ]),
}


def draw(name, palette, rows):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y, row in enumerate(rows):
        row = row.ljust(16, ".")[:16]
        for x, ch in enumerate(row):
            if ch in ". ":
                continue
            h = palette[ch].lstrip("#")
            img.putpixel((x, y), (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255))
    img.save(os.path.join(OUT, name + ".png"))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (palette, rows) in ITEMS.items():
        draw(name, palette, rows)
        print("drew", name)
