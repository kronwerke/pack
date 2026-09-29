#!/usr/bin/env python3
"""Checks that no quest hands out or asks for an item that is still locked in its stage.

A chapter with stage=N may only use items that are open by stage N: its tasks, rewards
and icons, and the crates it gives. A crate with stage=N may only contain such items.
Locks come from the Chapters stage files (items and @mod entries).
Usage: check_quest_stages.py <stages dir>   (run from the pack root)"""
import glob
import importlib
import json
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import ftbq  # noqa: E402

for f in sorted(os.listdir(os.path.join(here, "chapters"))):
    if f.endswith(".py") and not f.startswith("_"):
        importlib.import_module("chapters." + f[:-3])

locks_item, locks_mod = {}, {}
for f in sorted(glob.glob(os.path.join(sys.argv[1], "stage*.json"))):
    n = int(re.search(r"stage(\d+)\.json$", f).group(1))
    for it in json.load(open(f)).get("items", []):
        if it.startswith("@"):
            locks_mod.setdefault(it[1:], n)
        else:
            locks_item.setdefault(it, n)


# Vanilla items that only come from a locked dimension. Chapters does not lock them as
# items, so a quest or crate must not hand them out early.
DIMENSION_ITEMS = {
    2: ["minecraft:netherite_ingot", "minecraft:netherite_scrap", "minecraft:netherite_block",
        "minecraft:ancient_debris", "minecraft:blaze_rod", "minecraft:blaze_powder", "minecraft:nether_wart",
        "minecraft:ghast_tear", "minecraft:nether_star", "minecraft:wither_skeleton_skull",
        "minecraft:magma_cream", "minecraft:quartz", "minecraft:glowstone_dust", "minecraft:glowstone"],
    4: ["minecraft:elytra", "minecraft:shulker_shell", "minecraft:shulker_box", "minecraft:dragon_breath",
        "minecraft:dragon_egg", "minecraft:end_crystal", "minecraft:chorus_fruit", "minecraft:end_stone"],
}
for n, items in DIMENSION_ITEMS.items():
    for it in items:
        locks_item.setdefault(it, n)


def opens(item_id):
    """The stage an item opens in (1 when nothing locks it)."""
    if item_id in locks_item:
        return locks_item[item_id]
    return locks_mod.get(item_id.split(":", 1)[0], 1)


problems = []
for name, t in ftbq._tables.items():
    for e in t["entries"]:
        if opens(e[0]) > t["stage"]:
            problems.append(f"crate {name} (stage {t['stage']}): {e[0]} opens in stage {opens(e[0])}")

for ch in ftbq._chapters:
    s = ch["stage"]
    for q in ch["quests"]:
        where = f"{ch['name']}/{q['name']} (stage {s})"
        used = [q["icon"]] if q["icon"] else []
        for t in q["tasks"]:
            if t["type"] == "item":
                used.append(t["item"]["id"])
        for r in q["rewards"]:
            if r["type"] == "item":
                used.append(r["item"]["id"])
            if r["type"] == "loot":
                tbl = ftbq._tables.get(r["table"])
                if tbl is None:
                    problems.append(f"{where}: unknown crate {r['table']}")
                elif tbl["stage"] > s:
                    problems.append(f"{where}: crate {r['table']} is for stage {tbl['stage']}")
        for d in q["deps"]:
            if d not in {x["name"] for x in ch["quests"]}:
                problems.append(f"{where}: depends on unknown quest {d}")
        for i in used:
            if opens(i) > s:
                problems.append(f"{where}: {i} opens in stage {opens(i)}")

names = [c["name"] for c in ftbq._chapters]
for n in set(names):
    if names.count(n) > 1:
        problems.append(f"chapter name {n} used twice")

quests = sum(len(c["quests"]) for c in ftbq._chapters)
print(f"{len(ftbq._chapters)} chapters, {quests} quests, {len(ftbq._tables)} crates checked against {len(locks_item)} locked items and {len(locks_mod)} locked mods")
for p in problems:
    print("  ", p)
sys.exit(1 if problems else 0)
