"""Mod items in the world's loot: chests of every structure and the drops of hostile mobs.

Writes NeoForge global loot modifiers (neoforge:add_table) into kubejs/data, so every chest
table keeps what it had and gets one of our pools on top. Lootr fills its chests from the same
tables, so each player's copy gets them too. Items of later stages are allowed in loot on
purpose: they can be carried and stored, not used, until their stage opens.

Usage: python3 tools/loot/build.py DUMP_DIR   (the /kwdump of the test mod: loot.json, items.json, entities.json)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "kubejs", "data")

# Namespaces whose chest tables are structures in the world.
STRUCTURES = {"minecraft", "dungeons_arise", "nova_structures", "betterstrongholds", "betterdeserttemples", "betterfortresses",
              "betterdungeons", "betterjungletemples", "betterwitchhuts", "betteroceanmonuments", "cataclysm", "aether",
              "deeperdarker", "undergarden", "eternal_starlight", "mowziesmobs", "eidolon_repraised", "irons_spellbooks",
              "forbidden_arcanus", "hexerei", "botania"}
RARE = re.compile(r"treasure|boss|reward|vault|rare|secret|library|temple|pyramid|stronghold|mansion|ancient_city|end_city|bastion_treasure|elite|throne|king|lord")
NETHER = re.compile(r"nether|fortress|bastion|blaze|soul|crimson|warped")
END = re.compile(r"end_city|end_|ender|void|chorus")
SKIP = re.compile(r"inject|additional|additions/|dispenser|spawn_bonus|farm_drop|supply$|/supply|kitchen|wool|map_chest|ice_box")

E = lambda item, w, lo=1, hi=1: (item, w, lo, hi)  # noqa: E731

POOLS = {
    "common": {"rolls": [1, 2], "empty": 30, "entries": [
        E("create:andesite_alloy", 10, 2, 6), E("create:zinc_ingot", 6, 1, 3), E("create:cogwheel", 6, 1, 4),
        E("ars_nouveau:source_gem", 8, 1, 3), E("naturesaura:gold_leaf", 6, 1, 4), E("irons_spellbooks:arcane_essence", 6, 1, 4),
        E("mysticalagriculture:inferium_essence", 8, 2, 8), E("silentgear:blueprint_paper", 4, 2, 6),
        E("botania:mana_powder", 5, 1, 4), E("occultism:silver_ingot", 4, 1, 3), E("sophisticatedbackpacks:upgrade_base", 3),
        E("create:brass_ingot", 2, 1, 3), E("mekanism:ingot_osmium", 2, 1, 3),
    ]},
    "rare": {"rolls": [1, 3], "empty": 10, "entries": [
        E("create:brass_ingot", 8, 2, 6), E("create:precision_mechanism", 3), E("create:electron_tube", 4, 1, 3),
        E("mekanism:ingot_osmium", 6, 2, 6), E("mekanism:basic_control_circuit", 4, 1, 2),
        E("botania:manasteel_ingot", 6, 1, 4), E("botania:mana_pearl", 3), E("naturesaura:infused_iron", 6, 2, 5),
        E("irons_spellbooks:arcane_essence", 6, 3, 8), E("mysticalagriculture:prosperity_shard", 5, 2, 5),
        E("forbidden_arcanus:arcane_crystal", 4, 1, 3), E("occultism:spirit_attuned_gem", 3),
        E("ae2:certus_quartz_crystal", 4, 2, 5), E("eidolon_repraised:soul_shard", 3, 1, 3),
        E("malum:raw_soulstone", 3, 1, 3), E("draconicevolution:draconium_dust", 1, 1, 2),
    ]},
    "nether": {"rolls": [1, 2], "empty": 15, "entries": [
        E("create:brass_ingot", 6, 1, 4), E("evilcraft:dark_gem", 6, 1, 4), E("forbidden_arcanus:arcane_crystal", 5, 1, 3),
        E("justdirethings:raw_blazegold", 5, 1, 3), E("create:blaze_cake", 2), E("powah:uraninite", 3, 2, 5),
        E("mekanism:ingot_refined_glowstone", 2, 1, 2),
    ]},
    "end": {"rolls": [1, 2], "empty": 10, "entries": [
        E("draconicevolution:draconium_dust", 6, 2, 6), E("mekanism:ingot_refined_obsidian", 4, 1, 3),
        E("botania:pixie_dust", 4, 1, 3), E("ae2:singularity", 1), E("justdirethings:celestigem", 3, 1, 2),
    ]},
}

# Drops of hostile mobs, killed by a player: (entity table pattern, item, chance, looting extra per level).
DROPS = [
    ("monsters", "irons_spellbooks:arcane_essence", 0.04, 0.02),
    ("minecraft:entities/witch", "hexerei:mandrake_root", 0.25, 0.1),
    ("minecraft:entities/zombie", "create:zinc_nugget", 0.10, 0.05),
    ("minecraft:entities/husk", "create:zinc_nugget", 0.12, 0.05),
    ("minecraft:entities/zombie", "create:copper_nugget", 0.12, 0.05),
    ("minecraft:entities/enderman", "ae2:certus_quartz_dust", 0.06, 0.03),
    ("minecraft:entities/wither_skeleton", "evilcraft:dark_gem", 0.12, 0.05),
    ("minecraft:entities/blaze", "justdirethings:raw_blazegold", 0.08, 0.04),
    ("minecraft:entities/drowned", "aquaculture:neptunium_nugget", 0.03, 0.02),
]


def entry(item, w, lo, hi):
    e = {"type": "minecraft:item", "name": item, "weight": w}
    if hi > 1:
        e["functions"] = [{"function": "minecraft:set_count", "count": {"type": "minecraft:uniform", "min": lo, "max": hi}}]
    return e


def pool_table(p):
    entries = [entry(*x) for x in p["entries"]]
    if p["empty"]:
        entries.append({"type": "minecraft:empty", "weight": p["empty"]})
    return {"type": "minecraft:chest", "pools": [{"rolls": {"type": "minecraft:uniform", "min": p["rolls"][0], "max": p["rolls"][1]}, "entries": entries}]}


def drop_table(item, chance, looting):
    return {"type": "minecraft:entity", "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": item}],
            "conditions": [{"condition": "minecraft:killed_by_player"},
                           {"condition": "minecraft:random_chance_with_enchanted_bonus", "enchantment": "minecraft:looting",
                            "unenchanted_chance": chance, "enchanted_chance": {"type": "minecraft:linear", "base": chance + looting, "per_level_above_first": looting}}]}]}


def glm(tables, table):
    return {"type": "neoforge:add_table", "conditions": [{"condition": "minecraft:any_of", "terms": [
        {"condition": "neoforge:loot_table_id", "loot_table_id": t} for t in sorted(tables)]}], "table": table}


def write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


def main(dump):
    loot = json.load(open(os.path.join(dump, "loot.json")))
    items = {i["id"] for i in json.load(open(os.path.join(dump, "items.json")))}
    entities = json.load(open(os.path.join(dump, "entities.json")))
    bad = [x[0] for p in POOLS.values() for x in p["entries"] if x[0] not in items] + [d[1] for d in DROPS if d[1] not in items]
    if bad:
        print("unknown items:", bad)
        sys.exit(1)

    tiers = {"common": set(), "rare": set(), "nether": set(), "end": set()}
    for t in loot:
        ns, path = t.split(":", 1)
        if ns not in STRUCTURES or "chests/" not in path or SKIP.search(path):
            continue
        if END.search(path) and ns != "minecraft" or "end_city" in path:
            tiers["end"].add(t)
        elif NETHER.search(path):
            tiers["nether"].add(t)
        if RARE.search(path):
            tiers["rare"].add(t)
        elif not (END.search(path) or NETHER.search(path)):
            tiers["common"].add(t)

    names = []
    for tier, tables in tiers.items():
        write(os.path.join(DATA, "kronwerke", "loot_table", "inject", f"{tier}.json"), pool_table(POOLS[tier]))
        write(os.path.join(DATA, "kronwerke", "loot_modifiers", f"chests_{tier}.json"), glm(tables, f"kronwerke:inject/{tier}"))
        names.append(f"kronwerke:chests_{tier}")
        print(f"{tier}: {len(tables)} chest tables")

    monsters = {e["loot"] for e in entities if e["category"] == "monster" and e["loot"] in loot}
    for i, (target, item, chance, looting) in enumerate(DROPS):
        name = f"drop_{i}_{item.split(':')[1]}"
        tables = monsters if target == "monsters" else {target}
        write(os.path.join(DATA, "kronwerke", "loot_table", "inject", f"{name}.json"), drop_table(item, chance, looting))
        write(os.path.join(DATA, "kronwerke", "loot_modifiers", f"{name}.json"), glm(tables, f"kronwerke:inject/{name}"))
        names.append(f"kronwerke:{name}")
    print(f"drops: {len(DROPS)}, monster tables {len(monsters)}")
    write(os.path.join(DATA, "neoforge", "loot_modifiers", "global_loot_modifiers.json"), {"replace": False, "entries": names})


if __name__ == "__main__":
    main(sys.argv[1])
