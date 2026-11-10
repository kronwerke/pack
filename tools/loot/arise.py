"""Tones down the loot of When Dungeons Arise's chests.

Dungeons Arise fills its chests far beyond the rest of the pack (a bandit tower gave stacks of
iron and up to 16 diamonds, some towers netherite armor), which skips most of the early
progression. This reads the mod's chest tables from its jar and writes overrides to
kubejs/data/dungeons_arise/loot_table: the counts of ingots, gems, their blocks, netherite scrap,
experience bottles and golden apples are halved (at least 1 where the mod gives at least 1,
netherite ingots at most 1), the weight of diamond and netherite gear and of enchanted golden
apples is halved. Everything else stays as the mod has it.

    python3 tools/loot/arise.py path/to/DungeonsArise.jar
"""
import json
import math
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "kubejs", "data")

HALF_COUNT = {
    "minecraft:iron_ingot", "minecraft:gold_ingot", "minecraft:diamond", "minecraft:emerald",
    "minecraft:iron_block", "minecraft:gold_block", "minecraft:diamond_block", "minecraft:emerald_block",
    "minecraft:raw_iron_block", "minecraft:raw_gold_block", "minecraft:netherite_scrap",
    "minecraft:experience_bottle", "minecraft:golden_apple",
}
ONE = {"minecraft:netherite_ingot"}
HALF_WEIGHT_PREFIX = ("minecraft:diamond_", "minecraft:netherite_")
HALF_WEIGHT = {"minecraft:enchanted_golden_apple"}
GEAR = ("helmet", "chestplate", "leggings", "boots", "sword", "pickaxe", "axe", "shovel", "hoe")


def half(v, keep_one):
    if isinstance(v, (int, float)):
        return max(1 if keep_one and v >= 1 else 0, math.floor(v / 2)) if v > 1 else v
    return v


def scale_count(count):
    if isinstance(count, (int, float)):
        return half(count, True)
    if isinstance(count, dict) and "min" in count and "max" in count and count.get("type", "minecraft:uniform") == "minecraft:uniform":
        c = dict(count)
        c["min"] = half(count["min"], True)
        c["max"] = max(c["min"], half(count["max"], True))
        return c
    return count


def is_gear(name):
    return name.startswith(HALF_WEIGHT_PREFIX) and name.rsplit("_", 1)[-1] in GEAR


def tone(table):
    changed = False
    for pool in table.get("pools", []):
        for e in pool.get("entries", []):
            name = e.get("name")
            if not name:
                continue
            if name in HALF_COUNT or name in ONE:
                for fn in e.get("functions", []):
                    if fn.get("function", "").endswith("set_count") and "count" in fn:
                        new = scale_count(fn["count"]) if name in HALF_COUNT else 1
                        if new != fn["count"]:
                            fn["count"] = new
                            changed = True
            if (is_gear(name) or name in HALF_WEIGHT) and e.get("weight", 1) > 1:
                e["weight"] = max(1, e["weight"] // 2)
                changed = True
    return changed


def main(jar):
    written = 0
    with zipfile.ZipFile(jar) as z:
        for n in sorted(z.namelist()):
            if not (n.startswith("data/dungeons_arise/loot_table/chests/") and n.endswith(".json")):
                continue
            table = json.loads(z.read(n))
            if not tone(table):
                continue
            path = os.path.join(OUT, n[len("data/"):])
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                json.dump(table, f, indent=2)
                f.write("\n")
            written += 1
    print(f"{written} Dungeons Arise chest tables toned down")


if __name__ == "__main__":
    main(sys.argv[1])
