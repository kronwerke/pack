#!/usr/bin/env python3
"""Item icons for the web quest book, drawn from the item models in the jars.

Usage: icons.py ITEMS_JSON OUT_DIR MODS_DIR [MINECRAFT_JAR] [CORE_JAR]

For each item of ITEMS_JSON (written by web.py) writes OUT_DIR/<ns>/<path>.webp, 64 x 64:
  - a flat item (model with layer0, layer1 ...): the layers on top of each other, scaled up
    without smoothing, like the game draws it in the inventory;
  - a block item: a small cube in the inventory's three quarter view, top, front and side
    from the block model (cube_all, cube_column, cube_bottom_top, orientable and anything
    else that names top/side/front/end/all textures), the sides darker like the game shades them;
  - anything else (custom renderers, entities): the model's particle texture, flat.
Tints (grass, leaves, potions, spawn eggs) are applied for the few common cases only. Items
whose model cannot be read get no file; the website then shows a plain frame.
"""
import io
import json
import os
import re
import sys
import zipfile

from PIL import Image, ImageEnhance

SIZE = 64
TINTS = {"grass": (124, 189, 107), "foliage": (89, 174, 48), "water": (63, 118, 228)}


class Assets:
    def __init__(self, jars):
        self.files = {}
        for p in jars:
            try:
                z = zipfile.ZipFile(p)
            except (zipfile.BadZipFile, OSError):
                continue
            for n in z.namelist():
                if n.startswith("assets/") and (n.endswith(".json") or n.endswith(".png")):
                    self.files.setdefault(n, z)
        pack = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "kubejs", "assets")
        self.local = pack

    def read(self, path):
        lp = os.path.join(self.local, path[len("assets/"):])
        if os.path.exists(lp):
            with open(lp, "rb") as f:
                return f.read()
        z = self.files.get(path)
        return z.read(path) if z else None

    def model(self, ref, kind="item"):
        """The model json for ns:path (or ns:item/path), with its parents' textures merged in."""
        if ":" not in ref:
            ref = "minecraft:" + ref
        ns, path = ref.split(":", 1)
        data = self.read(f"assets/{ns}/models/{path}.json")
        if data is None:
            return None
        try:
            m = json.loads(data.decode("utf-8", "replace"))
        except ValueError:
            return None
        chain = [ref]
        textures = dict(m.get("textures", {}))
        parent = m.get("parent")
        elements = m.get("elements")
        loader = m.get("loader")
        depth = 0
        while parent and depth < 12:
            chain.append(parent)
            p = parent if ":" in parent else "minecraft:" + parent
            pns, ppath = p.split(":", 1)
            pdata = self.read(f"assets/{pns}/models/{ppath}.json")
            if pdata is None:
                break
            try:
                pm = json.loads(pdata.decode("utf-8", "replace"))
            except ValueError:
                break
            for k, v in pm.get("textures", {}).items():
                textures.setdefault(k, v)
            if elements is None:
                elements = pm.get("elements")
            parent = pm.get("parent")
            depth += 1
        # resolve #references
        for _ in range(6):
            for k, v in list(textures.items()):
                if isinstance(v, str) and v.startswith("#"):
                    textures[k] = textures.get(v[1:], v)
        return {"chain": chain, "textures": textures, "elements": elements, "loader": loader}

    def texture(self, ref):
        if not isinstance(ref, str) or ref.startswith("#"):
            return None
        if ":" not in ref:
            ref = "minecraft:" + ref
        ns, path = ref.split(":", 1)
        data = self.read(f"assets/{ns}/textures/{path}.png")
        if data is None:
            return None
        try:
            im = Image.open(io.BytesIO(data)).convert("RGBA")
        except OSError:
            return None
        w, h = im.size
        if h > w and h % w == 0:   # animated strip: first frame
            im = im.crop((0, 0, w, w))
        return im


def tint_for(iid, chain):
    s = " ".join(chain) + " " + iid
    if "leaves" in s and "cherry" not in s and "azalea" not in s:
        return TINTS["foliage"]
    if re.search(r"grass_block|(^|[:/_])grass($|_)|fern|vine|lily_pad", s):
        return TINTS["grass"]
    return None


def tinted(im, rgb):
    """multiplies the colours, like the game's tint."""
    r, g, b, a = im.split()
    px = [tuple(c1 * c2 // 255 for c1, c2 in zip(p, rgb)) for p in Image.merge("RGB", (r, g, b)).getdata()]
    out = Image.new("RGB", im.size)
    out.putdata(px)
    out.putalpha(a)
    return out


def flat(layers):
    base = Image.new("RGBA", layers[0].size, (0, 0, 0, 0))
    for l in layers:
        if l.size != base.size:
            l = l.resize(base.size, Image.NEAREST)
        base.alpha_composite(l)
    return base.resize((SIZE, SIZE), Image.NEAREST)


def cube(top, left, right):
    """Three quarter view: top as a rhombus, left and right faces below it."""
    n = 16
    top, left, right = (t.resize((n, n), Image.NEAREST) for t in (top, left, right))
    S = SIZE
    out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    # geometry of the inventory block: width 64, top rhombus height 32, sides 36 tall
    cx, ty, hw, hh, side = S / 2, 2, 29, 15, 33

    def warp(src, quad):
        # quad: target corners for src (0,0),(n,0),(n,n),(0,n); inverse mapping per pixel
        import numpy as np
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = quad
        A = np.array([[x1 - x0, x3 - x0], [y1 - y0, y3 - y0]], dtype=float)
        inv = np.linalg.inv(A)
        sp = src.load()
        op = out.load()
        xs = [x0, x1, x2, x3]
        ys = [y0, y1, y2, y3]
        for y in range(int(min(ys)), int(max(ys)) + 1):
            for x in range(int(min(xs)), int(max(xs)) + 1):
                if not (0 <= x < S and 0 <= y < S):
                    continue
                u, v = inv @ np.array([x + 0.5 - x0, y + 0.5 - y0])
                if 0 <= u < 1 and 0 <= v < 1:
                    c = sp[int(u * n), int(v * n)]
                    if c[3]:
                        op[x, y] = c

    warp(top, [(cx, ty), (cx + hw, ty + hh), (cx, ty + 2 * hh), (cx - hw, ty + hh)])
    l = ImageEnhance.Brightness(left).enhance(0.8)
    r = ImageEnhance.Brightness(right).enhance(0.62)
    warp(l, [(cx - hw, ty + hh), (cx, ty + 2 * hh), (cx, ty + 2 * hh + side), (cx - hw, ty + hh + side)])
    warp(r, [(cx, ty + 2 * hh), (cx + hw, ty + hh), (cx + hw, ty + hh + side), (cx, ty + 2 * hh + side)])
    return out


def pick(tex, *names):
    for n in names:
        if n in tex and isinstance(tex[n], str) and not tex[n].startswith("#"):
            return tex[n]
    return None


def icon(assets, iid):
    ns, path = iid.split(":", 1)
    m = assets.model(f"{ns}:item/{path}")
    if m is None:
        # some mods only ship a block model and a blockstate
        m = assets.model(f"{ns}:block/{path}")
        if m is None:
            return None
    tex = m["textures"]
    chain = m["chain"]
    tint = tint_for(iid, chain)
    layers = [k for k in sorted(tex) if re.match(r"layer\d+$", k)]
    is_block = any("block/" in c or c.endswith("cube") or "cube_" in c for c in chain[1:]) or m["elements"] is not None
    if layers and not any("block/" in c for c in chain[1:2]):
        ims = [assets.texture(tex[k]) for k in sorted(layers, key=lambda k: int(k[5:]))]
        ims = [i for i in ims if i is not None]
        if ims:
            if tint and len(ims) == 1:
                ims = [tinted(ims[0], tint)]
            return flat(ims)
    if is_block:
        top = pick(tex, "top", "end", "up", "all", "texture", "particle", "side")
        front = pick(tex, "front", "north", "side", "all", "texture", "particle", "end")
        side = pick(tex, "side", "east", "all", "texture", "particle", "front", "end")
        t, f, s = (assets.texture(x) for x in (top, front, side))
        if t is not None and f is not None and s is not None:
            if tint:
                t = tinted(t, tint)
                if "leaves" in iid or "grass_block" not in iid:
                    f, s = tinted(f, tint), tinted(s, tint)
            return cube(t, f, s)
    p = pick(tex, "particle", "layer0", "all", "texture", "side")
    im = assets.texture(p) if p else None
    return flat([im]) if im is not None else None


def main():
    items = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    jars = sorted(os.path.join(sys.argv[3], f) for f in os.listdir(sys.argv[3]) if f.endswith(".jar")) + sys.argv[4:]
    assets = Assets(jars)
    done, failed = 0, []
    for iid in items:
        try:
            im = icon(assets, iid)
        except Exception as e:  # a broken model must not stop the rest
            im = None
        if im is None:
            failed.append(iid)
            continue
        ns, path = iid.split(":", 1)
        dst = os.path.join(out, ns, path + ".webp")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im.save(dst, lossless=True, method=6)
        done += 1
    print(f"{done} icons, {len(failed)} without: {' '.join(failed[:40])}")
    with open(os.path.join(out, "missing.txt"), "w") as f:
        f.write("\n".join(failed) + "\n")


if __name__ == "__main__":
    main()
