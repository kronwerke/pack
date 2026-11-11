#!/usr/bin/env python3
"""Builds the screenshot world from docs/SCREENSHOTS.md.

Every line of the list becomes a grey concrete box in kronwerke:testworld; a line with
several quest ids gets one cell per id inside its box. A cell holds the scene for that
shot: the machines and multiblocks placed (mod templates where a mod ships one), mobs
standing still, a chest with what the shot still needs by hand, and signs that face the
path. Scenes without a hand written entry in scenes.py fall back to the quest's task
items and icon.

Output, into $KW_SHOTS_OUT (the shots-world branch of the pack repository, which the server
fetches with /kw testworld pull and builds with /kw testworld apply; the pack itself carries
nothing of the test world):
  000_pad.mcfunction        the landing pad and the section signs
  box_NNN.mcfunction        one per box: its space cleared, floor, walls, the scenes
  structures/**.nbt         structures taken from the mod jars (Ponder scenes and the like)
  shots.json                one camera position per cell, read by /kw cam run

Usage: build.py [--check]   (--check also validates block, item and entity ids against the
                             catalog catalog.py makes from the mod jars)
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
WALL_H = 16       # tall enough that the camera sees grey behind the scene, not sky
PAD = (-4, -4)

OUT = os.environ.get("KW_SHOTS_OUT", "/home/claude/kw/shots-world")
CATALOG = os.environ.get("KW_CATALOG", "/tmp/claude-0/cat/catalog.json")
_catalog = None


def catalog():
    """Blocks with their state properties, items, entities and templates of the mod jars (catalog.py)."""
    global _catalog
    if _catalog is None:
        with open(CATALOG) as fh:
            _catalog = json.load(fh)
    return _catalog


# which way a block looks, for the blocks that have a front: the camera stands south
FACING_PROPS = ("facing", "horizontal_facing")


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
        self.checks = []   # for verify.py
        self.pts = []      # what the camera has to frame, relative (x, y, z) corners
        self.focused = False
        self.yaw = 165.0   # where the camera looks: 180 is straight north
        self.pitch = 35.0  # how steeply it looks down, at least (a pentacle wants to be seen from above)

    def focus(self, x1, y1, z1, x2, y2, z2):
        """Frame only this part of the scene (a barrel at the foot of a tall obelisk)."""
        self.pts = [(x1, y1, z1), (x2, y2, z2)]
        self.focused = True

    def _see(self, x1, y1, z1, x2=None, y2=None, z2=None):
        if self.focused:
            return
        self.pts.append((x1, y1, z1))
        self.pts.append((x1 if x2 is None else x2, y1 if y2 is None else y2, z1 if z2 is None else z2))

    def _p(self, x, y, z):
        return f"{self.ox + x} {FLOOR_Y + 1 + y} {self.oz + z}"

    @staticmethod
    def front(block):
        """A block with a front and no direction given looks south, at the camera."""
        name, _, props = block.partition("[")
        known = catalog()["blocks"].get(name)
        if not known:
            return block
        given = {kv.split("=")[0] for kv in props.rstrip("]").split(",") if kv}
        for p in FACING_PROPS:
            if p in known and sorted(known[p]) == ["east", "north", "south", "west"] and p not in given:
                rest = props.rstrip("]")
                return f"{name}[{p}=south{',' + rest if rest else ''}]"
        return block

    def b(self, x, y, z, block, nbt=""):
        if not block.startswith("minecraft:air"):
            self._see(x, y, z)
        self.cmds.append(f"setblock {self._p(x, y, z)} {self.front(block)}{nbt}")

    def f(self, x1, y1, z1, x2, y2, z2, block):
        if not block.startswith("minecraft:air"):
            self._see(x1, y1, z1, x2, y2, z2)
        self.cmds.append(f"fill {self._p(x1, y1, z1)} {self._p(x2, y2, z2)} {block}")

    ROT = {"none": lambda x, z: (x, z), "clockwise_90": lambda x, z: (-z, x),
           "180": lambda x, z: (-x, -z), "counterclockwise_90": lambda x, z: (z, -x)}

    def _origin(self, x, z, size, rot):
        """Where a template's origin goes so that, turned, its box starts at x, z. -> (ox, oz, w, d)"""
        sx, _, sz = size
        f = self.ROT[rot]
        corners = [f(0, 0), f(sx - 1, 0), f(0, sz - 1), f(sx - 1, sz - 1)]
        minx, minz = min(c[0] for c in corners), min(c[1] for c in corners)
        maxx, maxz = max(c[0] for c in corners), max(c[1] for c in corners)
        return x - minx, z - minz, maxx - minx + 1, maxz - minz + 1

    def t(self, template, x, y, z, size, rot="none"):
        """A structure template a mod ships as data, its box starting at x, y, z."""
        ox, oz, w, d = self._origin(x, z, size, rot)
        self._see(x, y, z, x + w - 1, y + size[1] - 1, z + d - 1)
        self.cmds.append(f"place template {template} {self._p(ox, y, oz)} {rot}")
        return w, d

    def nbt(self, jar, path, x, y, z, rot="none", see=True):
        """A structure file from a mod jar that is no data template (a Ponder scene): it is
        copied into the world's own structures and placed by /kw testworld place."""
        import structs
        name = jar.lower().split("-")[0] + "/" + os.path.splitext(path.split("/ponder/")[-1].split("/structure/")[-1])[0]
        dest = os.path.join(OUT, "structures", name + ".nbt")
        if name not in self.vendored:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as fh:
                fh.write(structs.raw(jar, path))
            size, palette, blocks, _ = structs.load(jar, path)
            self.vendored[name] = (size, palette, blocks)
        size, palette, blocks = self.vendored[name]
        ox, oz, w, d = self._origin(x, z, size, rot)
        if see:
            f = self.ROT[rot]
            for bx, by, bz, p, _ in blocks:
                if by == 0 or palette[p].startswith("minecraft:air"):
                    continue       # the bottom layer is the scene's floor plate
                rx, rz = f(bx, bz)
                self._see(ox + rx, y + by, oz + rz)
        self.cmds.append(f"kw testworld place shots:{name} {self._p(ox, y, oz)} {rot}")
        return w, d

    vendored = {}

    def e(self, entity, x, y, z, nbt=""):
        """An entity that is part of a build (a spark over a pool), at the middle of that block."""
        self._see(x, int(y), z)
        tag = "{Tags:[\"kw_shot\"]" + ("," + nbt if nbt else "") + "}"
        self.cmds.append(f"summon {entity} {self.ox + x + .5} {FLOOR_Y + 1 + y} {self.oz + z + .5} {tag}")

    def drop(self, x, y, z, item, count=1):
        """An item lying or falling there (into a basin, onto a belt)."""
        self.cmds.append(f"summon item {self.ox + x + .5} {FLOOR_Y + 1 + y} {self.oz + z + .5} "
                         f"{{Item:{{id:\"{item}\",count:{count}}},PickupDelay:32767,Age:-32768,Tags:[\"kw_shot\"]}}")

    def use(self, x, y, z, face, item, sneak=False):
        """A tool used on a block the way a player would (the hammer that forms a multiblock)."""
        self.cmds.append(f"kw testworld use {self._p(x, y, z)} {face} {item}{' sneak' if sneak else ''}")

    def later(self, x, y, z, test, unless=False):
        """A check that only holds once the world has ticked (a multiblock that forms by itself):
        verify.py runs these on the test server. test is what follows "execute if" (or unless)."""
        self.checks.append(f"execute in kronwerke:testworld {'unless' if unless else 'if'} " + test.replace("@", self._p(x, y, z)))

    def formed(self, x, y, z):
        """A Mekanism multiblock has formed when its blocks share an inventory id."""
        self.later(x, y, z, "data block @ inventory_id")

    def changed(self, x, y, z, block):
        """Fails in the build log when the block there is still this one: the hammer did nothing."""
        self.cmds.append(f"execute unless block {self._p(x, y, z)} {block}")

    def expect(self, x, y, z, block):
        """Fails in the build log when the block there is not this one: has the multiblock formed?"""
        self.cmds.append(f"execute if block {self._p(x, y, z)} {block}")

    def m(self, entity, x, y, z, nbt="", ai=False, rot=180):
        self._see(x, y, z, x, y + 2, z)
        extra = "NoAI:1b," if not ai else ""
        tag = "{" + extra + f"PersistenceRequired:1b,Silent:1b,Tags:[\"kw_shot\"],Rotation:[{rot}f,0f]" + ("," + nbt if nbt else "") + "}"
        self.cmds.append(f"summon {entity} {self.ox + x + .5} {FLOOR_Y + 1 + y} {self.oz + z + .5} {tag}")

    def c(self, x, y, z, items, block=None, frame=None):
        """A chest. On the floor (y 0) it holds the materials for what is left to build by hand:
        a trapped chest, which the camera does not draw and does not frame. A chest that is part
        of the scene (an arm's input, a chest on a hopper) passes frame=True."""
        if frame is None:
            frame = y != 0
        if block is None:
            block = "minecraft:chest[facing=south]" if frame else "minecraft:trapped_chest[facing=south]"
        slots = []
        for i, it in enumerate(items[:27]):
            iid, n = (it, 1) if isinstance(it, str) else it
            slots.append(f'{{Slot:{i}b,id:"{iid}",count:{n}}}')
        n_pts = len(self.pts)
        self.b(x, y, z, block, "{Items:[" + ",".join(slots) + "]}")
        if not frame:           # a chest of materials for the hand work, not part of the picture
            del self.pts[n_pts:]

    def fr(self, x, y, z, facing, item):
        f = {"down": 0, "up": 1, "north": 2, "south": 3, "west": 4, "east": 5}[facing]
        self._see(x, y, z)
        self.cmds.append(f"summon item_frame {self._p(x, y, z)} {{Facing:{f}b,Fixed:1b,Tags:[\"kw_shot\"],Item:{{id:\"{item}\",count:1}}}}")

    def show(self, x, y, z, item, scale=1.0, plinth="minecraft:smooth_stone_slab"):
        """An item on show: a slab with the item floating above it, turned to the camera."""
        if plinth:
            self.b(x, y, z, plinth)
        self._see(x, y, z, x, y + 1, z)
        s = f"{scale}f"
        self.cmds.append(
            f"summon item_display {self.ox + x + .5} {FLOOR_Y + 1 + y + .5 + .45 * scale} {self.oz + z + .5} "
            f"{{item:{{id:\"{item}\",count:1}},item_display:\"fixed\",billboard:\"vertical\","
            f"transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],"
            f"scale:[{s},{s},{s}]}},brightness:{{sky:15,block:15}},Tags:[\"kw_shot\"]}}")

    def stand(self, x, y, z, armor=(), hand=None, rot=180):
        self._see(x, y, z, x, y + 2, z)
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


# ---- the camera ----------------------------------------------------------------------

SCREEN_WORDS = ("JEI", "tooltip", "view", "overlay", "boss bar", "Ponder", "screen", "menu", "GUI", "HUD",
                "chat", "inventory", "window", "terminal", "book", "keybind")


def needs_screen(desc):
    """Shots of a screen (JEI, a menu, the claim map) need someone at the keyboard, not the camera."""
    return any(w.lower() in desc.lower() for w in SCREEN_WORDS)


def camera(key, cell, south_limit, yaw=165.0, fov=60, pitch=35.0):
    """Where the camera stands for a cell: south of what the scene built (the boxes are open
    to the south), a little east, looking down at it. The distance is what that content needs
    to fill the frame (fov is Minecraft's vertical field of view; at 16:9 the horizontal one
    is about 92 degrees), but never beyond the next row's wall: then it looks down more
    steeply. A cell that built nothing is framed whole."""
    import math
    pts = cell.pts or [(0, 0, 0), (cell.w - 1, 2, cell.d - 1)]
    xs, ys, zs = [p[0] for p in pts], [p[1] for p in pts], [p[2] for p in pts]
    x1, x2 = cell.ox + min(xs), cell.ox + max(xs) + 1
    y1, y2 = FLOOR_Y + 1 + min(ys), FLOOR_Y + 1 + max(ys) + 1
    z1, z2 = cell.oz + min(zs), cell.oz + max(zs) + 1
    W, H, D = max(2.0, x2 - x1), max(1.5, y2 - y1), max(2.0, z2 - z1)
    tx, ty, tz = (x1 + x2) / 2, y1 + H * 0.4, (z1 + z2) / 2
    vt = math.tan(math.radians(fov / 2))
    ht = vt * 16 / 9
    yr = math.radians(yaw)
    room = south_limit - tz
    for _ in range(40):
        pr = math.radians(pitch)
        # what has to fit: the width across, and depth and height as seen from this angle
        across = W * abs(math.cos(yr)) + D * abs(math.sin(yr))
        tall = D * math.sin(pr) + H * math.cos(pr)
        dist = max(3.5, 1.12 * max(across / 2 / ht, tall / 2 / vt) + max(W, D) * 0.18)
        horiz = dist * math.cos(pr)
        if horiz * -math.cos(yr) <= room or pitch >= 70:
            break
        pitch += 2.5
    pr = math.radians(pitch)
    horiz = dist * math.cos(pr)
    ex, ey, ez = tx + math.sin(yr) * horiz, ty + dist * math.sin(pr), tz - math.cos(yr) * horiz
    # stay between the cell's dividers, turned toward the scene
    lo, hi = cell.ox + 0.3, cell.ox + cell.w - 0.3
    if ex < lo or ex > hi:
        ex = min(hi, max(lo, ex))
        yaw = round(math.degrees(math.atan2(-(tx - ex), tz - ez)) % 360, 1)
        horiz = math.hypot(tx - ex, tz - ez)
        pitch = round(math.degrees(math.atan2(ey - ty, horiz)), 1)
    # a run's tag in front of the name keeps its pictures apart from older ones on the server:
    # /kw cam bundle <tag> then holds exactly this run
    return {"name": os.environ.get("KW_SHOTS_TAG", "") + key.replace("/", "_"), "dim": "kronwerke:testworld",
            "pos": [round(ex, 2), round(ey - 1.62, 2), round(ez, 2)], "yaw": yaw, "pitch": round(pitch, 1),
            "fov": fov, "width": 640, "height": 360}


# ---- layout ------------------------------------------------------------------------

def clear(x0, z0, x1, z1, top):
    """fill commands that empty a space, in pieces the fill limit allows."""
    out = []
    span = max(1, 32768 // ((z1 - z0 + 1) * (top - FLOOR_Y)))
    for cx0 in range(x0, x1 + 1, span):
        out.append(f"fill {cx0} {FLOOR_Y + 1} {z0} {min(x1, cx0 + span - 1)} {top} {z1} minecraft:air")
    return out


def build(check=False):
    import scenes
    idx = quest_index()
    lines = parse_list()

    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".mcfunction") or f == "shots.json":
            os.remove(os.path.join(OUT, f))
    import shutil
    shutil.rmtree(os.path.join(OUT, "structures"), ignore_errors=True)
    Cell.vendored.clear()

    shots = []          # camera positions for /kw cam run
    checks = []         # (scene, command) for verify.py
    files = {}          # name -> commands
    pad = [
        "# the landing pad; /kw testworld puts you here",
        f"#area {PAD[0] - 2} {PAD[1] - 2} {PAD[0] + 2} {PAD[1] + 2}",
        f"fill {PAD[0] - 2} {FLOOR_Y} {PAD[1] - 2} {PAD[0] + 2} {FLOOR_Y} {PAD[1] + 2} minecraft:smooth_stone",
    ]
    x, z = 0, 0
    row_depth = 0
    cur_section = None
    row_shots = []
    problems = []
    top = FLOOR_Y + WALL_H + 12

    def close_row():
        nonlocal x, z, row_depth, row_shots
        # the camera stands in the path south of the row, in front of the next row's north wall
        for k, cell_ in row_shots:
            shots.append(camera(k, cell_, south_limit=z + row_depth + ROW_GAP - 0.7, yaw=cell_.yaw, pitch=cell_.pitch))
        row_shots = []
        if row_depth:
            z += row_depth + ROW_GAP
        x, row_depth = 0, 0

    n = 0
    for section, ch, qs, desc in lines:
        keys = [k for k in ([f"{ch}/{q}" for q in qs] or [ch]) if k in scenes.SCENES]
        if not keys:
            continue            # no scene of its own: no box and no picture
        if section != cur_section:
            close_row()
            cur_section = section
            pad.append(f"#area -8 {z} -6 {z + 2}")
            pad.append(f"setblock -6 {FLOOR_Y} {z + 1} minecraft:smooth_stone")
            pad.append(f"setblock -6 {FLOOR_Y + 1} {z + 1} minecraft:oak_sign[rotation=0]{sign_text(wrap(section))}")
        cells = [(k, scenes.SCENES[k]) for k in keys]
        bw = sum(c[1].w for c in cells) + (len(cells) - 1) + 2
        bd = max(c[1].d for c in cells) + 2 + 2      # +2 for the sign strip at the south edge
        wall = max([WALL_H] + [getattr(c[1], "h", 0) for c in cells])
        top = FLOOR_Y + wall + 12
        if x and x + bw > ROW_WIDTH:
            close_row()
        n += 1
        cmds = [f"# {n:03d} {ch}/{', '.join(k.split('/')[-1] for k in keys)}",
                f"#area {x - GAP} {z - ROW_GAP} {x + bw + GAP} {z + bd + ROW_GAP}"]
        # the box's space and the paths around it: nothing of an older layout stays in view
        cmds += clear(x - GAP, z - ROW_GAP, x + bw + GAP, z + bd + ROW_GAP, top)
        cmds.append(f"fill {x - GAP} {FLOOR_Y - 3} {z - ROW_GAP} {x + bw + GAP} {FLOOR_Y - 1} {z + bd + ROW_GAP} minecraft:stone")
        cmds.append(f"fill {x - GAP} {FLOOR_Y} {z - ROW_GAP} {x + bw + GAP} {FLOOR_Y} {z + bd + ROW_GAP} minecraft:light_gray_concrete")
        # the north wall runs on over the gap to the next box, so no sky shows between boxes
        cmds.append(f"fill {x} {FLOOR_Y + 1} {z} {x + bw + GAP} {FLOOR_Y + wall} {z} minecraft:light_gray_concrete")
        cmds.append(f"fill {x} {FLOOR_Y + 1} {z} {x} {FLOOR_Y + wall} {z + bd} minecraft:light_gray_concrete")
        cx = x + 1
        for i, (k, spec) in enumerate(cells):
            w, d = spec.w, spec.d
            cell = Cell(cx, z + 1, w, d)
            info = idx.get(k, {"title": "", "items": [], "kill": [], "dim": [], "icon": None})
            spec.fn(cell)
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
                cmds.append(f"setblock {cx + j} {FLOOR_Y + 1} {sz} minecraft:oak_sign[rotation=0]{sign_text(t)}")
            # a grey divider east of every cell, as deep as the box: the camera sees this scene
            # against grey, not the next scene beside it, even from far back in a deep cell
            cmds.append(f"fill {cx + w} {FLOOR_Y + 1} {z} {cx + w} {FLOOR_Y + wall} {z + bd} minecraft:light_gray_concrete")
            cmds.extend(cell.cmds)
            row_shots.append((k, cell))
            checks += [(k, c) for c in cell.checks]
            cx += w + 1
        files[f"box_{n:03d}"] = cmds
        row_depth = max(row_depth, bd)
        x += bw + GAP
    close_row()

    files["000_pad"] = pad
    for name, cmds in files.items():
        with open(os.path.join(OUT, name + ".mcfunction"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(cmds) + "\n")
    with open(os.path.join(OUT, "shots.json"), "w") as fh:
        json.dump({"shots": shots}, fh, indent=1)
    with open(os.path.join(HERE, "verify.json"), "w") as fh:
        json.dump({"area": [-8, -8, ROW_WIDTH + 8, z + 8], "checks": checks}, fh, indent=1)

    if check:
        problems += validate(catalog(), files)
    print(f"{n} boxes, {len(shots)} scenes, {len(Cell.vendored)} structures -> {OUT}")
    for p in problems:
        print("  " + p)
    return not problems


VANILLA_ENTITIES = {"item_frame", "armor_stand", "villager", "blaze", "wither", "ender_dragon", "zombie",
                    "skeleton", "cow", "sheep", "pig", "chicken", "iron_golem", "warden", "ghast",
                    "piglin", "piglin_brute", "hoglin", "wither_skeleton", "enderman", "end_crystal",
                    "allay", "parrot", "horse", "wolf", "cat", "fox", "bee", "strider", "magma_cube",
                    "slime", "creeper", "spider", "witch", "glow_item_frame", "item_display", "block_display",
                    "text_display", "item", "lightning_bolt", "area_effect_cloud", "chest_minecart", "minecart"}


def validate(cat, files):
    blocks, items, ents, structs = cat["blocks"], set(cat["items"]), set(cat["entities"]), set(cat["structures"])
    probs = []
    for f, cmds in sorted(files.items()):
        for ln, line in enumerate(cmds, 1):
            line = line.strip()
            where = f"{f}:{ln} ({cmds[0][2:]})"
            for bid in re.findall(r"(?:setblock -?\d+ -?\d+ -?\d+|fill -?\d+ -?\d+ -?\d+ -?\d+ -?\d+ -?\d+) ([a-z0-9_.-]+:[a-z0-9_/.-]+)(\[[^\]]*\])?", line):
                name, props = bid
                if name not in blocks:
                    probs.append(f"{where}: unknown block {name}")
                    continue
                known = blocks[name]
                given = set()
                for kv in props.strip("[]").split(",") if props else []:
                    k, _, v = kv.partition("=")
                    given.add(k)
                    if known and k not in known:
                        probs.append(f"{where}: {name} has no property {k} (has {sorted(known)})")
                    elif known and v not in known[k]:
                        probs.append(f"{where}: {name} {k}={v} not in {known[k]}")
                # a block that can be turned has to say which way: the default is rarely right
                for k in ("facing", "horizontal_facing", "axis", "horizontal_axis"):
                    if known and k in known and len(known[k]) > 1 and k not in given:
                        probs.append(f"{where}: {name} needs {k} (one of {known[k]})")
            for iid in re.findall(r'id:"([a-z0-9_.-]+:[a-z0-9_/.-]+)"', line):
                if iid not in items and iid not in blocks:
                    probs.append(f"{where}: unknown item {iid}")
            m = re.match(r"kw testworld use \S+ \S+ \S+ \S+ ([a-z0-9_.-]+:[a-z0-9_/.-]+)", line)
            if m and m[1] not in items and m[1] not in blocks:
                probs.append(f"{where}: unknown item {m[1]}")
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
