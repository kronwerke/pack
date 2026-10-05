#!/usr/bin/env python3
"""
Writes FTB Quests SNBT files from Python definitions.

Every chapter lives in its own module under tools/quests/chapters/ and calls
chapter(...) at import time. build.py imports them all and writes
config/ftbquests/quests/. Ids are derived from names, so a rebuild never
changes an id and player progress survives.

The structure (ids, positions, tasks, rewards) goes into quests/chapters/, all text into
quests/lang/<locale>.snbt, the way FTB Quests keeps it since 1.21. The text is German and is
written for de_de and for en_us, which FTB Quests falls back to for every other language.

Lettering on the canvas (chapter titles, section headings) is rendered by banners.py into
kubejs/assets/kronwerke/textures/quests/, see banner().
"""
import hashlib
import os
import shutil

LOCALES = ("de_de", "en_us")
FILE_TITLE = "Kronwerke Season 2"

class F(float):
    """A float written with the f suffix (float32 in SNBT)."""


_chapters = []
_groups = []
_tables = {}
_banners = {}   # texture path -> (text, kind, colour)


def qid(*parts):
    """Stable 16 hex character id from a path of names.

    FTB Quests parses ids with Long.parseLong, so the value has to fit a signed
    long: the first hex digit is kept in 1..7. An id outside that range is
    silently replaced with a random one on load, which breaks every lang key
    and dependency that points at it."""
    h = hashlib.sha1("/".join(parts).encode()).hexdigest()
    first = "1234567"[int(h[0], 16) % 7]
    return (first + h[1:16]).upper()


# ---- building blocks ------------------------------------------------------

def item(id, count=1, **components):
    d = {"id": id, "count": count}
    if components:
        d["components"] = components
    return d


def task_item(id, count=1, consume=False, title=None):
    t = {"type": "item", "item": item(id), "count": int(count)}
    if consume:
        t["consume_items"] = True
    if title:
        t["title"] = title
    return t


def task_checkmark(title):
    return {"type": "checkmark", "title": title}


def task_advancement(advancement, title=None):
    t = {"type": "advancement", "advancement": advancement, "criterion": ""}
    if title:
        t["title"] = title
    return t


def task_kill(entity, count=1):
    return {"type": "kill", "entity": entity, "value": int(count)}


def task_dimension(dimension):
    return {"type": "dimension", "dimension": dimension}


def task_stage(stage):
    return {"type": "stage", "stage": stage}


def reward_item(id, count=1):
    return {"type": "item", "item": item(id), "count": int(count)}


def reward_xp(levels):
    return {"type": "xp_levels", "xp_levels": int(levels)}


def reward_table(name):
    return {"type": "loot", "table": name}


def reward_command(cmd, player_command=False):
    return {"type": "command", "command": cmd, "player_command": player_command}


def reward_stage(stage):
    return {"type": "stage", "stage": stage}


def loot_table(name, title, entries, stage=1, loot_size=1, icon="ftbquests:lootcrate"):
    """entries: list of (item_id, count, weight) or (item_id, count, weight, random_bonus).
    stage: the first stage the table is handed out in; its items must not be locked later."""
    _tables[name] = {"title": title, "entries": entries, "loot_size": loot_size, "icon": icon, "stage": stage}


# ---- text and pictures ----------------------------------------------------

def img(texture, width, height, align="center"):
    """A picture inside a quest text, on a line of its own. width and height in GUI pixels."""
    return "{image:%s width:%d height:%d align:%s}" % (texture, width, height, align)


def item_texture(id):
    """The inventory texture of a plain item, for img() or canvas(): minecraft:diamond ->
    minecraft:textures/item/diamond.png. Blocks usually have no such texture; check with
    check_images.py."""
    ns, path = id.split(":", 1)
    return f"{ns}:textures/item/{path}.png"


def canvas(texture, x, y, width, height, rotation=0.0, order=0):
    """A picture on the chapter canvas, centred on x, y, in quest grid units."""
    return {"image": texture, "x": x, "y": y, "width": width, "height": height,
            "rotation": rotation, "order": order}


def banner(name, text, x, y, height=1.0, kind="section", colour="brass"):
    """Lettering on the chapter canvas: kind is title, section or note; colour one of
    banners.COLOURS. name is the file under textures/quests/, like "create/power"."""
    import banners
    texture = f"kronwerke:textures/quests/{name}.png"
    _banners[texture] = (text, kind, colour)
    w, h = banners.measure(text, kind)
    if kind == "title":
        # the plate around a title takes a third of its height, so the letters keep their size
        height = round(height * 1.4, 2)
    return canvas(texture, x, y, round(height * w / h, 2), height, order=1)


def group(name, title):
    _groups.append((name, title))


def quest(name, x, y, title, tasks, subtitle="", description=(), rewards=(), deps=(), icon=None,
          size=None, shape=None, optional=False, hide=False, min_width=None):
    return {"name": name, "x": x, "y": y, "title": title, "subtitle": subtitle,
            "description": list(description), "tasks": list(tasks), "rewards": list(rewards),
            "deps": list(deps), "icon": icon, "size": size, "shape": shape, "optional": optional,
            "hide": hide, "min_width": min_width}


def chapter(name, title, icon, group, quests, subtitle=(), shape="circle", order=None,
            hide_dependency_lines=False, stage=1, images=()):
    """stage: the stage the chapter belongs to. Nothing in it may be locked until a later stage.
    images: canvas() and banner() pictures on the chapter canvas."""
    _chapters.append({"name": name, "title": title, "icon": icon, "group": group, "quests": quests,
                      "subtitle": list(subtitle), "shape": shape, "order": order,
                      "hide_dependency_lines": hide_dependency_lines, "stage": stage,
                      "images": list(images)})


# ---- SNBT writer ----------------------------------------------------------

class L(int):
    """A long tag (written with the L suffix)."""

def _s(v, ind=0):
    pad = "\t" * ind
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, L):
        return f"{int(v)}L"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, F):
        return f"{float(v)}f"
    if isinstance(v, float):
        return f"{v}d"
    if isinstance(v, str):
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if isinstance(v, list):
        if not v:
            return "[]"
        inner = "\n".join(pad + "\t" + _s(x, ind + 1) for x in v)
        return "[\n" + inner + "\n" + pad + "]"
    if isinstance(v, dict):
        if not v:
            return "{}"
        inner = "\n".join(f"{pad}\t{k}: {_s(x, ind + 1)}" for k, x in v.items())
        return "{\n" + inner + "\n" + pad + "}"
    raise TypeError(type(v))


def _float(v):
    return float(v)


def _build_chapter(ch, order_index, lang):
    """The chapter file, and its text into lang (key -> value)."""
    import layout
    layout.layout(ch, lambda tex: _banners.get(tex, ("", "section", ""))[1])
    cid = qid("chapter", ch["name"])
    # a hub with many children, or a goal that needs many quests, draws no web of lines;
    # the big packs do the same for their lists, the position tells the story
    children = {}
    for q in ch["quests"]:
        for d in q["deps"]:
            children[d] = children.get(d, 0) + 1
    quests_out = []
    for q in ch["quests"]:
        quest_id = qid("quest", ch["name"], q["name"])
        qd = {
            "id": quest_id,
            "x": _float(q["x"]), "y": _float(q["y"]),
        }
        lang[f"quest.{quest_id}.title"] = q["title"]
        if q["subtitle"]:
            lang[f"quest.{quest_id}.quest_subtitle"] = q["subtitle"]
        if q["description"]:
            lang[f"quest.{quest_id}.quest_desc"] = list(q["description"])
        if q["icon"]:
            qd["icon"] = item(q["icon"])
        if q["size"]:
            qd["size"] = _float(q["size"])
        if q["shape"]:
            qd["shape"] = q["shape"]
        if q["optional"]:
            qd["optional"] = True
        if q["hide"]:
            qd["hide"] = True
        if q.get("hide_lines") or len(q["deps"]) > 3:
            qd["hide_dependency_lines"] = True
        if children.get(q["name"], 0) > 4:
            qd["hide_dependent_lines"] = True
        if q["min_width"]:
            qd["min_width"] = int(q["min_width"])
        if q["deps"]:
            qd["dependencies"] = [qid("quest", ch["name"], d) for d in q["deps"]]
        qd["tasks"] = []
        for i, t in enumerate(q["tasks"]):
            t = dict(t)
            task_id = qid("task", ch["name"], q["name"], str(i))
            if "title" in t:
                lang[f"task.{task_id}.title"] = t.pop("title")
            t = {"id": task_id, **t}
            qd["tasks"].append(t)
        qd["rewards"] = []
        for i, r in enumerate(q["rewards"]):
            r = dict(r)
            if r["type"] == "loot":
                # FTB Quests reads table_id with getLong: a hex string reads as 0,
                # which leaves the reward without a table (empty "Loot Reward").
                r["table_id"] = L(int(qid("table", r.pop("table")), 16))
            r = {"id": qid("reward", ch["name"], q["name"], str(i)), **r}
            qd["rewards"].append(r)
        quests_out.append(qd)
    images_out = []
    for i, im in enumerate(ch["images"]):
        d = {"id": qid("image", ch["name"], str(i)), "image": im["image"],
             "x": _float(im["x"]), "y": _float(im["y"]),
             "width": _float(im["width"]), "height": _float(im["height"]),
             "rotation": _float(im["rotation"])}
        if im["order"]:
            d["order"] = int(im["order"])
        images_out.append(d)
    lang[f"chapter.{cid}.title"] = ch["title"]
    if ch["subtitle"]:
        lang[f"chapter.{cid}.chapter_subtitle"] = ch["subtitle"]
    out = {
        "id": cid,
        "filename": ch["name"],
        "icon": item(ch["icon"]),
        "group": qid("group", ch["group"]),
        "order_index": order_index,
        "default_quest_shape": ch["shape"],
        "default_hide_dependency_lines": ch["hide_dependency_lines"],
        "quests": quests_out,
    }
    if images_out:
        out["images"] = images_out
    return out


def _write_lang(qdir, entries):
    """One file per locale; FTB Quests 2101.1 reads lang/<locale>.snbt."""
    os.makedirs(os.path.join(qdir, "lang"), exist_ok=True)
    for loc in LOCALES:
        with open(os.path.join(qdir, "lang", loc + ".snbt"), "w") as f:
            f.write(_s(dict(sorted(entries.items()))) + "\n")


def write(out_dir, pack_icon="create:large_cogwheel", assets_dir=None):
    """assets_dir: where the kronwerke:textures/quests/ lettering goes (kubejs/assets)."""
    qdir = os.path.join(out_dir, "quests")
    if os.path.isdir(qdir):
        shutil.rmtree(qdir)
    os.makedirs(os.path.join(qdir, "chapters"))
    os.makedirs(os.path.join(qdir, "reward_tables"))

    data = {
        "default_autoclaim_rewards": "disabled",
        "default_consume_items": False,
        "default_quest_disable_jei": False,
        "default_quest_shape": "circle",
        "default_reward_team": False,
        "detection_delay": 20,
        "disable_gui": False,
        "drop_loot_crates": False,
        "emergency_items_cooldown": 300,
        "grid_scale": 0.5,
        "icon": item(pack_icon),
        "lock_message": "",
        "loot_crate_no_drop": {"boss": 0, "monster": 600, "passive": 4000},
        "pause_game": False,
        "progression_mode": "flexible",
        "show_lock_icons": True,
        "version": 13,
    }
    with open(os.path.join(qdir, "data.snbt"), "w") as f:
        f.write(_s(data) + "\n")

    with open(os.path.join(qdir, "chapter_groups.snbt"), "w") as f:
        f.write(_s({"chapter_groups": [{"id": qid("group", g)} for g, t in _groups]}) + "\n")
    lang = {f"chapter_group.{qid('group', g)}.title": t for g, t in _groups}
    lang["file.0000000000000001.title"] = FILE_TITLE

    for i, (name, tbl) in enumerate(_tables.items()):
        rewards = []
        for j, e in enumerate(tbl["entries"]):
            iid, count, weight = e[0], e[1], e[2]
            r = {"id": qid("tableentry", name, str(j)), "item": item(iid, count), "weight": F(weight)}
            if len(e) > 3:
                r["random_bonus"] = int(e[3])
            rewards.append(r)
        # the crate itself: without this block the "loot" reward hands out a crate that opens to nothing
        colours = {"common": 0x9d9d9d, "uncommon": 0x4a9bd4, "rare": 0xd4a24a}
        kind = name.split("_")[-1]
        out = {"id": qid("table", name), "icon": item(tbl["icon"]),
               "loot_size": tbl["loot_size"], "order_index": i, "rewards": rewards,
               "loot_crate": {"string_id": name, "item_name": tbl["title"], "color": colours.get(kind, 0xffffff),
                             "glow": kind == "rare", "drops": {"passive": 0, "monster": 0, "boss": 0}}}
        with open(os.path.join(qdir, "reward_tables", name + ".snbt"), "w") as f:
            f.write(_s(out) + "\n")

    lang.update({f"reward_table.{qid('table', n)}.title": t["title"] for n, t in _tables.items()})

    for i, ch in enumerate(_chapters):
        out = _build_chapter(ch, ch["order"] if ch["order"] is not None else i, lang)
        with open(os.path.join(qdir, "chapters", ch["name"] + ".snbt"), "w") as f:
            f.write(_s(out) + "\n")
    _write_lang(qdir, lang)

    if assets_dir and _banners:
        import banners
        for texture, (text, kind, colour) in sorted(_banners.items()):
            ns, path = texture.split(":", 1)
            banners.write(os.path.join(assets_dir, ns, path), text, kind, colour)

    return len(_chapters), sum(len(c["quests"]) for c in _chapters), len(_tables)
