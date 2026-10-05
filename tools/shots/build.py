#!/usr/bin/env python3
"""Builds the screenshot world from docs/SCREENSHOTS.md.

Every line of the list becomes a grey concrete box in kronwerke:testworld; a line with
several quest ids gets one cell per id inside its box. A cell holds the scene for that
shot: the machines and multiblocks placed (mod templates where a mod ships one), mobs
standing still, a chest with what the shot still needs by hand, and signs that face the
path. Scenes without a hand written entry in scenes.py fall back to the quest's task
items and icon.

Output, all under kubejs/data/kronwerke:
  function/shots/row_NN.mcfunction   one per row of boxes
  function/shots/box/NNN.mcfunction  one per box, so a bad line only costs its own box
  shots/rows.json                    the rows with their area, read by /kw testworld

Usage: build.py [--check]   (--check also validates block, item and entity ids against
                             a catalog made from the server's mod jars, when present)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "quests"))

FLOOR_Y = 63
CELL = 9          # default cell size, interior
GAP = 4           # path between boxes
ROW_GAP = 6
ROW_WIDTH = 420   # wrap a section row after this many blocks
WALL_H = 8
PAD = (-4, -4)

OUT_FN = os.path.join(ROOT, "kubejs", "data", "kronwerke", "function", "shots")
OUT_DATA = os.path.join(ROOT, "kubejs", "data", "kronwerke", "shots")


def quest_index():
    """chapter/quest -> title, task items, kills, dimensions, icon."""
    import importlib
    import ftbq
    for f in sorted(os.listdir(os.path.join(ROOT, "tools", "quests", "chapters"))):
        if f.endswith(".py") and not f.startswith("_"):
            importlib.import_module("chapters." + f[:-3])
    idx = {}
    for ch in ftbq._chapters:
        for q in ch["quests"]:
            idx[ch["name"] + "/" + q["name"]] = {
                "title": re.sub(r"&.", "", q["title"]),
                "items": [t["item"]["id"] for t in q["tasks"] if t.get("type") == "item"],
                "kill": [t["entity"] for t in q["tasks"] if t.get("type") == "kill"],
                "dim": [t["dimension"] for t in q["tasks"] if t.get("type") == "dimension"],
                "icon": q.get("icon"),
            }
    return idx


def parse_list():
    """docs/SCREENSHOTS.md -> [(section, chapter, [quest ids], description)]."""
    section = ""
    out = []
    for line in open(os.path.join(ROOT, "docs", "SCREENSHOTS.md"), encoding="utf-8"):
        line = line.rstrip()
        if line.startswith("## "):
            section = line[3:]
            continue
        m = re.match(r"- ([a-z0-9_]+)/([^:]+?)(?:: (.*))?$", line)
        if m:
            out.append((section, m[1], [q.strip() for q in m[2].split(",")], m[3] or ""))
            continue
        m = re.match(r"- ([a-z0-9_]+): (.*)$", line)
        if m:
            out.append((section, m[1], [], m[2]))
    return out


# ---- text on signs -----------------------------------------------------------

def wrap(text, width=15):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def sign_text(lines):
    lines = (list(lines) + ["", "", "", ""])[:4]
    # JSON inside a single quoted SNBT string: backslashes and single quotes need escaping
    esc = [json.dumps({"text": s}, ensure_ascii=False).replace("\\", "\\\\").replace("'", "\\'") for s in lines]
    return "{front_text:{messages:['" + "','".join(esc) + "']}}"


# ---- the builder a scene draws with ---------------------------------------------

class Cell:
    """Coordinates are relative to the cell: x east, z south, y 0 the first layer on the floor."""

    def __init__(self, ox, oz, w, d):
        self.ox, self.oz, self.w, self.d = ox, oz, w, d
        self.cmds = []
        self.notes = []

    def _p(self, x, y, z):
        return f"{self.ox + x} {FLOOR_Y + 1 + y} {self.oz + z}"

    def b(self, x, y, z, block, nbt=""):
        self.cmds.append(f"setblock {self._p(x, y, z)} {block}{nbt}")

    def f(self, x1, y1, z1, x2, y2, z2, block):
        self.cmds.append(f"fill {self._p(x1, y1, z1)} {self._p(x2, y2, z2)} {block}")

    def t(self, template, x, y, z, rot="none"):
        self.cmds.append(f"place template {template} {self._p(x, y, z)} {rot}")

    def m(self, entity, x, y, z, nbt="", ai=False, rot=180):
        extra = "NoAI:1b," if not ai else ""
        tag = "{" + extra + f"PersistenceRequired:1b,Silent:1b,Tags:[\"kw_shot\"],Rotation:[{rot}f,0f]" + ("," + nbt if nbt else "") + "}"
        self.cmds.append(f"summon {entity} {self.ox + x + .5} {FLOOR_Y + 1 + y} {self.oz + z + .5} {tag}")

    def c(self, x, y, z, items, block="minecraft:chest[facing=south]"):
        slots = []
        for i, it in enumerate(items[:27]):
            iid, n = (it, 1) if isinstance(it, str) else it
            slots.append(f'{{Slot:{i}b,id:"{iid}",count:{n}}}')
        self.b(x, y, z, block, "{Items:[" + ",".join(slots) + "]}")

    def fr(self, x, y, z, facing, item):
        f = {"down": 0, "up": 1, "north": 2, "south": 3, "west": 4, "east": 5}[facing]
        self.cmds.append(f"summon item_frame {self._p(x, y, z)} {{Facing:{f}b,Fixed:1b,Tags:[\"kw_shot\"],Item:{{id:\"{item}\",count:1}}}}")

    def stand(self, x, y, z, armor=(), hand=None, rot=180):
        a = list(armor) + [None] * (4 - len(armor))   # head, chest, legs, feet
        def it(i):
            return f'{{id:"{i}",count:1}}' if i else "{}"
        arm = f"ArmorItems:[{it(a[3])},{it(a[2])},{it(a[1])},{it(a[0])}]"
        h = f",HandItems:[{it(hand)},{{}}]" if hand else ""
        self.cmds.append(f"summon armor_stand {self.ox + x + .5} {FLOOR_Y + 1 + y} {self.oz + z + .5} "
                         f"{{{arm}{h},ShowArms:1b,NoBasePlate:1b,Tags:[\"kw_shot\"],Rotation:[{rot}f,0f]}}")

    def note(self, text):
        """An extra line on the cell's sign: what is left to do by hand."""
        self.notes.append(text)

    def cmd(self, raw):
        self.cmds.append(raw)


# ---- layout ------------------------------------------------------------------------

def build(check=False):
    import scenes
    idx = quest_index()
    lines = parse_list()
    blocks_cat = None
    if check:
        catp = os.environ.get("KW_CATALOG", "/tmp/claude-0/cat/catalog.json")
        if os.path.exists(catp):
            blocks_cat = json.load(open(catp))

    os.makedirs(os.path.join(OUT_FN, "box"), exist_ok=True)
    for f in os.listdir(os.path.join(OUT_FN, "box")):
        os.remove(os.path.join(OUT_FN, "box", f))
    for f in os.listdir(OUT_FN):
        if f.endswith(".mcfunction"):
            os.remove(os.path.join(OUT_FN, f))
    os.makedirs(OUT_DATA, exist_ok=True)

    rows = []           # [{fn, x0, z0, x1, z1, boxes}]
    x, z = 0, 0
    row_depth = 0
    cur_section = None
    row_boxes = []
    problems = []

    def close_row():
        nonlocal x, z, row_depth, row_boxes
        if row_boxes:
            rows.append({"boxes": row_boxes, "z0": z - 2, "z1": z + row_depth + 2,
                         "x0": -8, "x1": max(b["x1"] for b in row_boxes) + 2})
        z += row_depth + ROW_GAP
        x, row_depth, row_boxes = 0, 0, []

    n = 0
    for section, ch, qs, desc in lines:
        if section != cur_section:
            close_row()
            cur_section = section
            row_boxes.append({"label": section, "x0": -8, "x1": -8, "z": z, "cmds": [], "is_label": True})
        keys = [f"{ch}/{q}" for q in qs] or [ch]
        cells = []
        for k in keys:
            spec = scenes.SCENES.get(k)
            w, d = (spec.w, spec.d) if spec else (CELL, CELL)
            cells.append((k, spec, w, d))
        bw = sum(c[2] for c in cells) + (len(cells) - 1) + 2
        bd = max(c[3] for c in cells) + 2 + 2      # +2 for the sign strip at the south edge
        if x and x + bw > ROW_WIDTH:
            close_row()
        n += 1
        box = {"n": n, "x0": x, "x1": x + bw, "z": z, "cmds": []}
        cmds = box["cmds"]
        cmds.append(f"# {n:03d} {ch}/{', '.join(qs)}")
        cmds.append(f"fill {x} {FLOOR_Y} {z} {x + bw} {FLOOR_Y} {z + bd} minecraft:light_gray_concrete")
        cmds.append(f"fill {x} {FLOOR_Y + 1} {z} {x + bw} {FLOOR_Y + WALL_H} {z} minecraft:light_gray_concrete")
        cmds.append(f"fill {x} {FLOOR_Y + 1} {z} {x} {FLOOR_Y + WALL_H} {z + bd} minecraft:light_gray_concrete")
        cx = x + 1
        for i, (k, spec, w, d) in enumerate(cells):
            cell = Cell(cx, z + 1, w, d)
            info = idx.get(k, {"title": "", "items": [], "kill": [], "dim": [], "icon": None})
            if spec:
                spec.fn(cell)
            else:
                scenes.auto(cell, info)
            # signs along the south edge of the cell, facing south toward the path
            sz = z + bd - 1
            sign_lines = [f"{n:03d}" + (f".{i + 1}" if len(cells) > 1 else ""), ch, k.split("/")[-1] if "/" in k else ""]
            texts = [sign_lines + [""]]
            body = wrap(desc) if i == 0 and desc else []
            body += [l for t in cell.notes for l in wrap(t)]
            if not body and info.get("title"):
                body = wrap(info["title"])
            for j in range(0, len(body), 4):
                texts.append(body[j:j + 4])
            for j, t in enumerate(texts[: max(1, w)]):
                sx = cx + j
                cmds.append(f"setblock {sx} {FLOOR_Y + 1} {sz} minecraft:air")
                cmds.append(f"setblock {sx} {FLOOR_Y + 1} {sz} minecraft:oak_sign[rotation=0]{sign_text(t)}")
            cmds.extend(cell.cmds)
            cx += w + 1
        row_boxes.append(box)
        row_depth = max(row_depth, bd)
        x += bw + GAP
    close_row()

    # the pad, and a sign per section at the west end of its row
    first = [
        "# the landing pad; /kw testworld puts you here",
        f"fill {PAD[0] - 2} {FLOOR_Y} {PAD[1] - 2} {PAD[0] + 2} {FLOOR_Y} {PAD[1] + 2} minecraft:smooth_stone",
    ]
    out_rows = []
    for r, row in enumerate(rows):
        body = list(first) if r == 0 else []
        first = []
        for b in row["boxes"]:
            if b.get("is_label"):
                body.append(f"setblock -6 {FLOOR_Y} {b['z'] + 1} minecraft:smooth_stone")
                body.append(f"setblock -6 {FLOOR_Y + 1} {b['z'] + 1} minecraft:oak_sign[rotation=0]{sign_text(wrap(b['label']))}")
                continue
            path = os.path.join(OUT_FN, "box", f"{b['n']:03d}.mcfunction")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(b["cmds"]) + "\n")
            body.append(f"function kronwerke:shots/box/{b['n']:03d}")
        fn = f"row_{r:02d}"
        with open(os.path.join(OUT_FN, fn + ".mcfunction"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(body) + "\n")
        out_rows.append({"function": f"kronwerke:shots/{fn}", "x0": row["x0"], "z0": row["z0"], "x1": row["x1"], "z1": row["z1"]})
    with open(os.path.join(OUT_DATA, "rows.json"), "w") as fh:
        json.dump({"pad": [PAD[0] + 0.5, FLOOR_Y + 1, PAD[1] + 0.5], "rows": out_rows}, fh, indent=1)

    if blocks_cat:
        problems += validate(blocks_cat)
    total_cells = sum(max(1, len(l[2])) for l in lines)
    hand = sum(1 for l in lines for q in (l[2] or [None]) if (f"{l[1]}/{q}" if q else l[1]) in scenes.SCENES)
    print(f"{n} boxes, {total_cells} cells ({hand} hand made), {len(rows)} rows")
    for p in problems:
        print("  " + p)
    return not problems


VANILLA_ENTITIES = {"item_frame", "armor_stand", "villager", "blaze", "wither", "ender_dragon", "zombie",
                    "skeleton", "cow", "sheep", "pig", "chicken", "iron_golem", "warden", "ghast",
                    "piglin", "piglin_brute", "hoglin", "wither_skeleton", "enderman", "end_crystal",
                    "allay", "parrot", "horse", "wolf", "cat", "fox", "bee", "strider", "magma_cube",
                    "slime", "creeper", "spider", "witch", "glow_item_frame", "item_display", "block_display",
                    "text_display", "lightning_bolt", "area_effect_cloud", "chest_minecart", "minecart"}


def validate(cat):
    blocks, items, ents, structs = cat["blocks"], set(cat["items"]), set(cat["entities"]), set(cat["structures"])
    probs = []
    for f in sorted(os.listdir(os.path.join(OUT_FN, "box"))):
        for ln, line in enumerate(open(os.path.join(OUT_FN, "box", f), encoding="utf-8"), 1):
            line = line.strip()
            where = f"box/{f}:{ln}"
            for bid in re.findall(r"(?:setblock -?\d+ -?\d+ -?\d+|fill -?\d+ -?\d+ -?\d+ -?\d+ -?\d+ -?\d+) ([a-z0-9_.-]+:[a-z0-9_/.-]+)(\[[^\]]*\])?", line):
                name, props = bid
                if name not in blocks:
                    probs.append(f"{where}: unknown block {name}")
                    continue
                known = blocks[name]
                for kv in props.strip("[]").split(",") if props else []:
                    k, _, v = kv.partition("=")
                    if known and k in known and v not in known[k]:
                        probs.append(f"{where}: {name} {k}={v} not in {known[k]}")
            for iid in re.findall(r'id:"([a-z0-9_.-]+:[a-z0-9_/.-]+)"', line):
                if iid not in items and iid not in blocks:
                    probs.append(f"{where}: unknown item {iid}")
            m = re.match(r"summon ([a-z0-9_.-]+:)?([a-z0-9_/.-]+)", line)
            if m:
                full = (m[1] or "minecraft:") + m[2]
                if full.startswith("minecraft:"):
                    if m[2] not in VANILLA_ENTITIES:
                        probs.append(f"{where}: check vanilla entity {full}")
                elif full not in ents:
                    probs.append(f"{where}: unknown entity {full}")
            m = re.match(r"place template ([a-z0-9_.-]+:[a-z0-9_/.-]+)", line)
            if m and m[1] not in structs:
                probs.append(f"{where}: unknown template {m[1]}")
    return probs


if __name__ == "__main__":
    ok = build(check="--check" in sys.argv)
    sys.exit(0 if ok or "--check" not in sys.argv else 1)
