#!/usr/bin/env python3
"""Connected textures for the obelisk, through Athena (client side in the pack).

Athena's ctm loader takes four 16 px tiles per face and picks a quarter of each for every
corner of a block face, depending on which neighbours are the same block. The names say
what the tile shows, not where it is used: "particle" is the lone block with edges all
round (it is also the particle), "center" the inner corner, "horizontal" a horizontal run
(edges top and bottom), "vertical" a vertical run (edges left and right) and "empty" has
no edges, for the inside of a surface. With these, the 9x9 steps of the plinth read as one slab with a
brass edge, and the 3x3 trunk as one monolith with a brass seam only at its outline.

The models have to override Kronwerke Core's, and kubejs/assets sits below the mods in the
resource pack order, so they are written by a client script into KubeJS's "last" virtual
pack (ClientEvents.generateAssets('last', ...)), which sits above every mod. Core itself
keeps its plain models and still works without Athena. Same input, same file.
"""
import json
import os
import random

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "..", "kubejs", "assets", "kronwerke")

SLATE = (31, 27, 36)
SLATE_DARK = (22, 19, 26)
SLATE_LIGHT = (44, 39, 52)
BRASS = (212, 162, 74)
BRASS_DARK = (138, 100, 32)
BRASS_LIGHT = (240, 206, 130)


def stone(seed, base=SLATE, amount=4):
    rnd = random.Random(seed)
    im = Image.new("RGBA", (16, 16))
    px = im.load()
    for y in range(16):
        for x in range(16):
            n = rnd.randint(-amount, amount)
            px[x, y] = (base[0] + n, base[1] + n, base[2] + n, 255)
    return im


def detail(im, kind, seed):
    """What the inside of a surface shows, so a nine block slab is not nine blocks of noise:
    the top of the plinth is laid in slabs with a grout cross, its sides run in two courses,
    the trunk carries a few chisel marks. Every tile of a set gets the same pattern, so the
    quarters Athena picks always join."""
    rnd = random.Random(seed)
    px = im.load()

    def shade(x, y, t):
        c = px[x, y][:3]
        px[x, y] = tuple(max(0, min(255, round(c[i] + t))) for i in range(3)) + (255,)

    if kind == "slabs":
        for i in range(16):
            shade(7, i, -14)
            shade(i, 7, -14)
            if i != 7:
                shade(8, i, 6)
                shade(i, 8, 6)
    elif kind == "courses":
        for i in range(16):
            shade(i, 5, 7)
            shade(i, 6, -12)
            shade(i, 11, 7)
            shade(i, 12, -12)
    for _ in range(4 if kind == "chisel" else 2):
        x, y = rnd.randint(1, 13), rnd.randint(1, 13)
        shade(x, y, 9)
        shade(x + 1, y + 1, -12)
    return im


def edges(im, top, bottom, left, right, trim):
    """Draws the edge treatment on the sides that are open: a brass line with a dark seam."""
    d = ImageDraw.Draw(im)
    if trim == "brass":
        if top:
            d.line((0, 0, 15, 0), fill=BRASS_DARK + (255,))
            d.line((0, 1, 15, 1), fill=BRASS + (255,))
            d.line((0, 2, 15, 2), fill=SLATE_DARK + (255,))
        if bottom:
            d.line((0, 15, 15, 15), fill=BRASS_DARK + (255,))
            d.line((0, 14, 15, 14), fill=BRASS + (255,))
            d.line((0, 13, 15, 13), fill=SLATE_DARK + (255,))
        if left:
            d.line((0, 0, 0, 15), fill=BRASS_DARK + (255,))
            d.line((1, 0, 1, 15), fill=BRASS + (255,))
            d.line((2, 0, 2, 15), fill=SLATE_DARK + (255,))
        if right:
            d.line((15, 0, 15, 15), fill=BRASS_DARK + (255,))
            d.line((14, 0, 14, 15), fill=BRASS + (255,))
            d.line((13, 0, 13, 15), fill=SLATE_DARK + (255,))
        # a light point where two brass edges meet
        if top and left:
            d.point((1, 1), fill=BRASS_LIGHT + (255,))
        if top and right:
            d.point((14, 1), fill=BRASS_LIGHT + (255,))
        if bottom and left:
            d.point((1, 14), fill=BRASS_LIGHT + (255,))
        if bottom and right:
            d.point((14, 14), fill=BRASS_LIGHT + (255,))
    else:
        # a plain bevel: light on top and left, dark on bottom and right
        if top:
            d.line((0, 0, 15, 0), fill=SLATE_LIGHT + (255,))
        if left:
            d.line((0, 0, 0, 15), fill=SLATE_LIGHT + (255,))
        if bottom:
            d.line((0, 15, 15, 15), fill=SLATE_DARK + (255,))
        if right:
            d.line((15, 0, 15, 15), fill=SLATE_DARK + (255,))
    return im


def tile_set(folder, seed, base, trim, kind):
    """empty, horizontal, vertical, center for one surface."""
    out = os.path.join(ASSETS, "textures", "block", "ctm", folder)
    os.makedirs(out, exist_ok=True)
    edges(detail(stone(seed, base), kind, seed), True, True, True, True, trim).save(os.path.join(out, "center.png"))
    edges(detail(stone(seed + 1, base), kind, seed + 1), True, True, False, False, trim).save(os.path.join(out, "horizontal.png"))
    edges(detail(stone(seed + 2, base), kind, seed + 2), False, False, True, True, trim).save(os.path.join(out, "vertical.png"))
    edges(detail(stone(seed + 3, base), kind, seed + 3), False, False, False, False, trim).save(os.path.join(out, "empty.png"))
    return "kronwerke:block/ctm/" + folder


MODELS = {}


def model(name, particle, faces):
    """faces: {"default": set, "up": set, ...} with set = texture folder prefix."""
    def tiles(prefix):
        t = {k: f"{prefix}/{k}" for k in ("center", "empty", "horizontal", "vertical")}
        t["particle"] = f"{prefix}/center"
        return t

    m = {"loader": "athena:athena", "athena:loader": "athena:ctm"}
    if list(faces) == ["default"]:
        # the same tiles on every face: Athena takes the five entries directly
        m["ctm_textures"] = tiles(faces["default"])
    else:
        m["ctm_textures"] = {face: tiles(prefix) for face, prefix in faces.items()}
    MODELS[name] = m


def write_script():
    out = os.path.join(ASSETS, "..", "..", "client_scripts")
    os.makedirs(out, exist_ok=True)
    lines = ["// Connected textures for the obelisk through Athena. Written by tools/textures/ctm.py:",
             "// the models must sit above Kronwerke Core's in the resource pack order, which only",
             "// the 'last' virtual pack does. The tiles are in assets/kronwerke/textures/block/ctm.",
             "ClientEvents.generateAssets('last', event => {"]
    for name, m in MODELS.items():
        lines.append(f"    event.json('kronwerke:models/block/{name}', {json.dumps(m)})")
    lines.append("})")
    with open(os.path.join(out, "obelisk_ctm.js"), "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    plinth_top = tile_set("plinth_top", 10, SLATE, "brass", "slabs")
    plinth_side = tile_set("plinth_side", 20, SLATE_DARK, "plain", "courses")
    trunk = tile_set("trunk", 30, SLATE, "brass", "chisel")
    model("obelisk_plinth", "kronwerke:block/obelisk_plinth_top", {"up": plinth_top, "down": plinth_side, "default": plinth_side})
    model("obelisk_trunk", "kronwerke:block/obelisk_trunk", {"default": trunk})
    write_script()
    print("ok", os.path.abspath(ASSETS))
