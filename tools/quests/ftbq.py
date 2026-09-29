#!/usr/bin/env python3
"""
Writes FTB Quests SNBT files from Python definitions.

Every chapter lives in its own module under tools/quests/chapters/ and calls
chapter(...) at import time. build.py imports them all and writes
config/ftbquests/quests/. Ids are derived from names, so a rebuild never
changes an id and player progress survives.
"""
import hashlib
import os
import shutil

class F(float):
    """A float written with the f suffix (float32 in SNBT)."""


_chapters = []
_groups = []
_tables = {}


def qid(*parts):
    """Stable 16 hex character id from a path of names."""
    h = hashlib.sha1("/".join(parts).encode()).hexdigest()
    return h[:16].upper()


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


def loot_table(name, title, entries, loot_size=1, icon="ftbquests:lootcrate"):
    """entries: list of (item_id, count, weight) or (item_id, count, weight, random_bonus)."""
    _tables[name] = {"title": title, "entries": entries, "loot_size": loot_size, "icon": icon}


def group(name, title):
    _groups.append((name, title))


def quest(name, x, y, title, tasks, subtitle="", description=(), rewards=(), deps=(), icon=None,
          size=None, shape=None, optional=False, hide=False, min_width=None):
    return {"name": name, "x": x, "y": y, "title": title, "subtitle": subtitle,
            "description": list(description), "tasks": list(tasks), "rewards": list(rewards),
            "deps": list(deps), "icon": icon, "size": size, "shape": shape, "optional": optional,
            "hide": hide, "min_width": min_width}


def chapter(name, title, icon, group, quests, subtitle=(), shape="circle", order=None,
            hide_dependency_lines=False):
    _chapters.append({"name": name, "title": title, "icon": icon, "group": group, "quests": quests,
                      "subtitle": list(subtitle), "shape": shape, "order": order,
                      "hide_dependency_lines": hide_dependency_lines})


# ---- SNBT writer ----------------------------------------------------------

def _s(v, ind=0):
    pad = "\t" * ind
    if isinstance(v, bool):
        return "true" if v else "false"
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


def _build_chapter(ch, order_index):
    cid = qid("chapter", ch["name"])
    quests_out = []
    for q in ch["quests"]:
        qd = {
            "id": qid("quest", ch["name"], q["name"]),
            "x": _float(q["x"]), "y": _float(q["y"]),
            "title": q["title"],
        }
        if q["subtitle"]:
            qd["subtitle"] = q["subtitle"]
        if q["description"]:
            qd["description"] = q["description"]
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
        if q["min_width"]:
            qd["min_width"] = int(q["min_width"])
        if q["deps"]:
            qd["dependencies"] = [qid("quest", ch["name"], d) for d in q["deps"]]
        qd["tasks"] = []
        for i, t in enumerate(q["tasks"]):
            t = dict(t)
            t = {"id": qid("task", ch["name"], q["name"], str(i)), **t}
            qd["tasks"].append(t)
        qd["rewards"] = []
        for i, r in enumerate(q["rewards"]):
            r = dict(r)
            if r["type"] == "loot":
                r["table_id"] = qid("table", r.pop("table"))
            r = {"id": qid("reward", ch["name"], q["name"], str(i)), **r}
            qd["rewards"].append(r)
        quests_out.append(qd)
    out = {
        "id": cid,
        "filename": ch["name"],
        "title": ch["title"],
        "icon": item(ch["icon"]),
        "group": qid("group", ch["group"]),
        "order_index": order_index,
        "default_quest_shape": ch["shape"],
        "default_hide_dependency_lines": ch["hide_dependency_lines"],
        "subtitle": ch["subtitle"],
        "quests": quests_out,
    }
    return out


def write(out_dir, pack_icon="create:large_cogwheel"):
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
        f.write(_s({"chapter_groups": [{"id": qid("group", g), "title": t} for g, t in _groups]}) + "\n")

    for i, (name, tbl) in enumerate(_tables.items()):
        rewards = []
        for j, e in enumerate(tbl["entries"]):
            iid, count, weight = e[0], e[1], e[2]
            r = {"id": qid("tableentry", name, str(j)), "item": item(iid, count), "weight": F(weight)}
            if len(e) > 3:
                r["random_bonus"] = int(e[3])
            rewards.append(r)
        out = {"id": qid("table", name), "title": tbl["title"], "icon": item(tbl["icon"]),
               "loot_size": tbl["loot_size"], "order_index": i, "rewards": rewards}
        with open(os.path.join(qdir, "reward_tables", name + ".snbt"), "w") as f:
            f.write(_s(out) + "\n")

    for i, ch in enumerate(_chapters):
        out = _build_chapter(ch, ch["order"] if ch["order"] is not None else i)
        with open(os.path.join(qdir, "chapters", ch["name"] + ".snbt"), "w") as f:
            f.write(_s(out) + "\n")

    return len(_chapters), sum(len(c["quests"]) for c in _chapters), len(_tables)
