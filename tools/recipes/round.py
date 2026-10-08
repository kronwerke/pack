"""The 2026-10 recipe round: every mod leans on another, the first route is slow, a later one is fast.

Each change has a reason. `python3 tools/recipes/round.py DUMP_DIR` checks every change against a
dump of the running pack (the recipe exists and has the input that is swapped, every item exists,
nothing new is from a later stage than what it makes) and writes
kubejs/server_scripts/kronwerke/round.js and the table in docs/RECIPES.md.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph  # noqa: E402

ROOT = graph.ROOT
OUT_JS = os.path.join(ROOT, "kubejs", "server_scripts", "kronwerke", "round.js")
DOC = os.path.join(ROOT, "docs", "RECIPES.md")


def swap(recipe, frm, to, why, rebuild=False):
    """rebuild: KubeJS cannot replace inputs in this recipe's type, so it is removed and written again
    from the dump with the input swapped (same type, so special serializers keep working)."""
    return {"kind": "swap", "recipe": recipe, "from": frm, "to": to, "why": why, "rebuild": rebuild}


def custom(rid, out, ins, json_, why):
    """A new recipe of any type; `out` and `ins` are what the stage check reads."""
    return {"kind": "custom", "id": rid, "out": out, "in": ins, "json": json_, "why": why}


def mixing(rid, ins, out, count, heat, why):
    js = {"type": "create:mixing", "ingredients": [{"tag": i[1:]} if i.startswith("#") else {"item": i} for i in ins],
          "results": [{"id": out, "count": count}]}
    if heat:
        js["heat_requirement"] = heat
    return custom(rid, [out], ins, js, why)


def imbuement(rid, inp, pedestals, out, count, source, why):
    js = {"type": "ars_nouveau:imbuement", "input": {"item": inp}, "output": {"id": out, "count": count},
          "source": source, "pedestalItems": [{"item": p} for p in pedestals]}
    return custom(rid, [out], [inp] + pedestals, js, why)


def shaped(rid, out, count, pattern, key, why):
    js = {"type": "minecraft:crafting_shaped", "pattern": pattern,
          "key": {k: ({"tag": v[1:]} if v.startswith("#") else {"item": v}) for k, v in key.items()},
          "result": {"id": out, "count": count}}
    return custom(rid, [out], list(key.values()), js, why)


def alloy(rid, ins, out, count, energy, why):
    """EnderIO alloy smelter; ins are (id or #tag, count)."""
    js = {"type": "enderio:alloy_smelting", "energy": energy, "experience": 0.3,
          "inputs": [dict(({"tag": i[1:]} if i.startswith("#") else {"item": i}), count=n) for i, n in ins],
          "output": {"id": out, "count": count}}
    return custom(rid, [out], [i for i, _ in ins], js, why)


def pressing(material, plate, why):
    js = {"type": "create:pressing", "ingredients": [{"tag": f"c:ingots/{material}"}], "results": [{"id": plate}]}
    return custom(f"kronwerke:round/press_{material}", [plate], [f"#c:ingots/{material}"], js, why)


# Plates that only NuclearCraft's own machines could make; a Create press makes them too.
NC_PLATES = ["thorium", "boron", "tin", "magnesium", "lithium", "cobalt", "platinum", "zirconium",
             "beryllium", "bronze", "tough_alloy", "palladium", "hard_carbon", "thermoconducting", "extreme",
             "manganese", "sic_sic_cmc", "hsla_steel", "ferroboron", "lithium_manganese_dioxide", "graphite"]


CHANGES = {
    "Stage 1: the first machines of every mod need a part from another": [
        swap("ars_nouveau:imbuement_chamber", "#c:ingots/gold", "create:golden_sheet",
             "The first Ars machine needs a press: magic starts with a little tech."),
        swap("ars_nouveau:enchanting_apparatus", "#c:ingots/gold", "naturesaura:infused_iron",
             "The apparatus runs on aura iron from the Natural Altar."),
        swap("botania:mana_spreader", "#c:ingots/copper", "create:copper_sheet",
             "Pressed copper for the spreader; Botania meets Create on day one."),
        swap("naturesaura:tree_ritual/nature_altar", "minecraft:stone", "botania:livingrock",
             "The Natural Altar stands on livingrock from a Pure Daisy: the two nature mods lean on each other.", rebuild=True),
        swap("mysticalagriculture:infusion_altar", "#c:ingots/gold", "ars_nouveau:source_gem",
             "Growing resources starts with source."),
        swap("mysticalagriculture:infusion_pedestal", "#c:ingots/gold", "create:golden_sheet",
             "Pressed gold for the pedestals."),
        swap("waystones:warp_stone", "minecraft:amethyst_shard", "ars_nouveau:source_gem",
             "Travel is a spell: every waystone costs four source gems."),
        swap("irons_spellbooks:inscription_table", "#minecraft:wooden_slabs", "ars_nouveau:archwood_slab",
             "Spell books are written on archwood."),
        swap("irons_spellbooks:arcane_anvil", "minecraft:amethyst_block", "ars_nouveau:source_gem_block",
             "The arcane anvil binds source."),
        imbuement("kronwerke:round/arcane_essence", "minecraft:book", ["minecraft:lapis_lazuli", "minecraft:glowstone_dust"],
                  "irons_spellbooks:arcane_essence", 3, 300,
                  "Arcane essence came only from loot and bees, which stalled Iron's Spells. A book imbued with lapis and glowstone gives three."),
        swap("occultism:crafting/golden_sacrificial_bowl", "#c:ingots/gold", "create:golden_sheet",
             "The golden bowl is pressed gold."),
        swap("silentgear:material_grader", "#c:gems/quartz", "ars_nouveau:source_gem",
             "The grader reads materials with source."),
        swap("ironfurnaces:furnaces/copper_furnace", "#c:ingots/copper", "create:copper_sheet",
             "Furnaces are clad in pressed sheets."),
        swap("ironfurnaces:furnaces/iron_furnace", "#c:ingots/iron", "create:iron_sheet",
             "Furnaces are clad in pressed sheets."),
        swap("ironfurnaces:furnaces/iron_furnace2", "#c:ingots/iron", "create:iron_sheet",
             "Furnaces are clad in pressed sheets."),
        swap("sophisticatedbackpacks:iron_backpack", "#c:ingots/iron", "create:iron_sheet",
             "Backpack tiers are plated with Create sheets.", rebuild=True),
        swap("sophisticatedbackpacks:iron_backpack_from_copper", "#c:ingots/iron", "create:iron_sheet",
             "Backpack tiers are plated with Create sheets.", rebuild=True),
        swap("sophisticatedbackpacks:gold_backpack", "#c:ingots/gold", "create:golden_sheet",
             "Backpack tiers are plated with Create sheets.", rebuild=True),
        swap("sophisticatedstorage:basic_to_iron_tier_upgrade", "#c:ingots/iron", "create:iron_sheet",
             "Storage tiers are plated with Create sheets."),
        swap("functionalstorage:compacting_drawer", "minecraft:piston", "create:mechanical_press",
             "A drawer that compacts has a press in it."),
        swap("functionalstorage:simple_compacting_drawer", "minecraft:piston", "create:mechanical_press",
             "A drawer that compacts has a press in it."),
        swap("functionalstorage:storage_controller", "minecraft:comparator", "create:andesite_casing",
             "The drawer network has a Create casing at its heart."),
    ],
    "Stage 1 to 2: slow by hand, fast with heat": [
        mixing("kronwerke:round/infused_iron_mixing", ["#c:ingots/iron", "#c:ingots/iron", "ars_nouveau:source_gem"],
               "naturesaura:infused_iron", 2, "heated",
               "The altar makes one infused iron at a time with a lot of aura. A heated mixer with source makes two from a gem."),
        mixing("kronwerke:round/source_gem_mixing", ["minecraft:amethyst_shard", "minecraft:amethyst_shard", "minecraft:glowstone_dust"],
               "ars_nouveau:source_gem", 3, "heated",
               "Imbuing makes one gem for 500 source. A heated mixer makes three from two shards and glowstone."),
    ],
    "Stage 2: the witch, blood and relic mods join the rest": [
        swap("hexerei:mixing_cauldron", "minecraft:iron_ingot", "naturesaura:infused_iron",
             "The witch's cauldron is bound with aura iron."),
        swap("reliquary:fertile_essence", "#c:dyes/green", "hexerei:mandrake_root",
             "Fertility comes from the mandrake."),
        swap("reliquary:alkahestry_altar", "minecraft:redstone_lamp", "occultism:spirit_attuned_gem",
             "Alkahestry is spirit work."),
        swap("reliquary:apothecary_cauldron", "minecraft:cauldron", "hexerei:mixing_cauldron",
             "The apothecary brews in a witch's cauldron."),
        swap("evilcraft:crafting/blood_infuser", "#c:cobblestones", "forbidden_arcanus:darkstone",
             "Blood work in darkstone."),
        swap("evilcraft:crafting/dark_tank", "#c:ingots/iron", "born_in_chaos_v1:dark_metal_ingot",
             "The dark tank is forged from the dark metal of Born in Chaos."),
        swap("forbidden_arcanus:clibano_core", "minecraft:blast_furnace", "create:blaze_burner",
             "The clibano burns with a blaze."),
        mixing("kronwerke:round/deorum_heated", ["minecraft:gold_ingot", "forbidden_arcanus:arcane_crystal_dust", "forbidden_arcanus:arcane_crystal_dust"],
               "forbidden_arcanus:deorum_ingot", 1, "heated",
               "Deorum without mundabitur dust, in a heated mixer."),
        mixing("kronwerke:round/deorum_superheated", ["minecraft:gold_ingot", "forbidden_arcanus:arcane_crystal_dust"],
               "forbidden_arcanus:deorum_ingot", 2, "superheated",
               "A superheated mixer doubles deorum."),
        swap("pneumaticcraft:air_compressor", "minecraft:furnace", "create:blaze_burner",
             "Compressed air is heated by a blaze."),
        swap("pneumaticcraft:pressure_tube", "#c:glass_blocks", "create:fluid_pipe",
             "Pressure tubes start from Create's pipes."),
        swap("justdirethings:gooblock_tier1", "minecraft:dirt", "mysticalagriculture:inferium_essence",
             "Goo grows from inferium."),
        swap("create_jetpack:jetpack", "create:chute", "aether:zanite_gemstone",
             "The jetpack's nozzles are zanite from the Aether.", rebuild=True),
    ],
    "Stage 3 and 4: deep magic and the far mods": [
        swap("malum:spirit_altar", "#c:ingots/gold", "eidolon_repraised:arcane_gold_ingot",
             "Malum's altar stands on Eidolon's arcane gold."),
        swap("eidolon_repraised:worktable", "#minecraft:planks", "malum:runewood_planks",
             "Eidolon's worktable is runewood."),
        mixing("kronwerke:round/pewter_mixing", ["#c:ingots/lead", "#c:ingots/iron"],
               "eidolon_repraised:pewter_blend", 3, None,
               "Pewter blend by hand gives two, a mixer three."),
        swap("integrateddynamics:crafting/squeezer", "#c:storage_blocks/iron", "create:mechanical_press",
             "The squeezer is a press."),
        swap("laserio:laser_connector", "#c:ingots/iron", "ae2:fluix_crystal",
             "Lasers carry what fluix carries."),
        swap("xnet:controller", "minecraft:comparator", "ae2:logic_processor",
             "The network controller thinks with AE2's logic."),
        swap("rftoolsbase:machine_frame", "#c:ingots/iron", "mekanism:ingot_steel",
             "RFTools machines start from steel."),
        swap("ae2:network/blocks/inscribers", "minecraft:piston", "create:mechanical_press",
             "The inscriber is a press."),
        swap("industrialforegoing:dissolution_chamber", "minecraft:bucket", "create:fluid_tank",
             "Dissolution in Create tanks."),
        swap("quarryplus:quarry", "#c:ingots/iron", "eternal_starlight:deepsilver_ingot",
             "The quarry's frame is deepsilver from Eternal Starlight."),
        swap("mahoutsukai:attuner", "minecraft:gold_ingot", "botania:terrasteel_ingot",
             "Mahou Tsukai attunes to terrasteel."),
        swap("draconicevolution:components/draconium_core", "#c:ingots/gold", "eternal_starlight:deepsilver_ingot",
             "Draconium cores are set in deepsilver."),
        swap("aquaculture:iron_fishing_rod", "#c:ingots/iron", "create:iron_sheet",
             "The iron rod is pressed sheet."),
        swap("oritech:crafting/cooler", "minecraft:ice", "undergarden:froststeel_ingot",
             "Oritech's cooler holds the Undergarden's froststeel."),
        swap("powah:crafting/thermo_generator_basic", "minecraft:iron_ingot", "undergarden:froststeel_ingot",
             "A thermoelectric generator needs a cold side: froststeel."),
        swap("ae2:network/wireless_part", "ae2:fluix_pearl", "deeperdarker:sculk_transmitter",
             "AE2's wireless receiver listens through a sculk transmitter from the Otherside."),
        swap("eidolon_repraised:lesser_soul_gem", "#c:gems/quartz", "deeperdarker:soul_crystal",
             "Eidolon's soul gem is cut from a soul crystal of the Otherside.", rebuild=True),
        swap("draconicevolution:tools/dislocator", "minecraft:ender_eye", "deeperdarker:reinforced_echo_shard",
             "The dislocator remembers places with a reinforced echo shard."),
    ],
    "Boss and treasure loot opens shortcuts": [
        shaped("kronwerke:round/netherite_furnace_ignitium", "ironfurnaces:netherite_furnace", 1,
               ["I#I", "#X#", "I#I"], {"I": "cataclysm:ignitium_ingot", "#": "minecraft:magma_cream", "X": "#c:furnaces/obsidian"},
               "Who beat Ignis gets the netherite furnace without netherite: four ignitium."),
        shaped("kronwerke:round/neptunium_diving_helmet", "create:netherite_diving_helmet", 1,
               [" N ", "NHN", " N "], {"N": "aquaculture:neptunium_ingot", "H": "create:copper_diving_helmet"},
               "Neptunium from the sea's treasure makes the diving helmet that also survives lava."),
        shaped("kronwerke:round/neptunium_diving_boots", "create:netherite_diving_boots", 1,
               [" N ", "NHN", " N "], {"N": "aquaculture:neptunium_ingot", "H": "create:copper_diving_boots"},
               "The same for the diving boots."),
    ],
    "Fast later: bulk for the stage goals once their stage is past": [
        mixing("kronwerke:round/andesite_alloy_superheated", ["minecraft:andesite", "minecraft:andesite", "#c:nuggets/iron"],
               "create:andesite_alloy", 4, "superheated",
               "Stage 1 hands out two per mixer run; from stage 2 a superheated mixer gives four from two andesite and one nugget."),
        alloy("kronwerke:round/brass_alloy_smelter", [("#c:ingots/copper", 3), ("#c:ingots/zinc", 1)], "create:brass_ingot", 4, 4000,
              "Brass is the stage 2 goal; from stage 3 the EnderIO alloy smelter makes four from three copper and a zinc."),
    ],
    "Every plate on the press": [
        pressing(m, f"nuclearcraft:{m}_plate", "NuclearCraft plates came only from its own machines; a Create press makes them one to one.")
        for m in NC_PLATES
    ] + [pressing("hop_graphite", "immersiveengineering:plate_hop_graphite", "Immersive's graphite plate on the Create press too.")],
}


def check(dump):
    items, recipes, stage, tags, makes, uses = graph.build(dump)
    known = {it["id"] for it in items}
    by_id = {r["id"]: r for r in recipes}
    st = lambda i: stage.get(i, 1)  # noqa: E731

    def stage_of_input(x):
        if x.startswith("#"):
            members = tags.get(x[1:], set())
            return min((st(m) for m in members), default=99)
        return st(x)

    def exists(x):
        return bool(tags.get(x[1:])) if x.startswith("#") else x in known

    errors, notes = [], []
    for family, changes in CHANGES.items():
        for c in changes:
            if c["kind"] == "swap":
                r = by_id.get(c["recipe"])
                if r is None or "json" not in r:
                    errors.append(f"{c['recipe']}: no such recipe")
                    continue
                text = json.dumps(r["json"])
                frm = c["from"]
                needle = f'"tag": "{frm[1:]}"' if frm.startswith("#") else f'"{frm}"'
                if needle not in text:
                    errors.append(f"{c['recipe']}: does not use {frm}")
                if not exists(c["to"]):
                    errors.append(f"{c['recipe']}: {c['to']} does not exist")
                outs = graph.refs(r["json"], tags)["out"] & known
                out_stage = min((st(o) for o in outs), default=1)
                if stage_of_input(c["to"]) > out_stage:
                    errors.append(f"{c['recipe']}: {c['to']} (stage {stage_of_input(c['to'])}) is later than what it makes (stage {out_stage})")
                if not c["to"].startswith("#") and not makes.get(c["to"]):
                    notes.append(f"{c['to']} has no recipe (a drop or world item)")
            else:
                for x in c["out"] + c["in"]:
                    if not exists(x):
                        errors.append(f"{c['id']}: {x} does not exist")
                out_stage = min((stage_of_input(o) for o in c["out"]), default=1)
                for x in c["in"]:
                    if exists(x) and stage_of_input(x) > out_stage:
                        errors.append(f"{c['id']}: {x} (stage {stage_of_input(x)}) is later than what it makes (stage {out_stage})")
                if c["id"] in by_id and not c["id"].startswith("kronwerke:round/"):
                    errors.append(f"{c['id']}: id taken")
    return errors, notes


def swapped(node, frm, to):
    """The recipe json with every ingredient `frm` replaced by `to`."""
    want = {"tag": frm[1:]} if frm.startswith("#") else {"item": frm}
    new = {"tag": to[1:]} if to.startswith("#") else {"item": to}
    if isinstance(node, dict):
        if node == want or (not frm.startswith("#") and node.get("item") == frm and len(node) == 1):
            return dict(new)
        return {k: swapped(v, frm, to) for k, v in node.items()}
    if isinstance(node, list):
        return [swapped(v, frm, to) for v in node]
    return node


def js(by_id):
    lines = ["// The recipe round of 2026-10: every mod leans on another, the first route is slow, a later one fast.",
             "// Generated by tools/recipes/round.py; the reasons are in docs/RECIPES.md.", "",
             "ServerEvents.recipes(event => {"]
    for family, changes in CHANGES.items():
        lines.append(f"  // {family}")
        for c in changes:
            if c["kind"] == "swap" and c["rebuild"]:
                j = swapped(by_id[c["recipe"]]["json"], c["from"], c["to"])
                new_id = "kronwerke:round/" + c["recipe"].replace(":", "_").replace("/", "_")
                lines.append(f"  event.remove({{ id: '{c['recipe']}' }})")
                lines.append(f"  event.custom({json.dumps(j)}).id('{new_id}')")
            elif c["kind"] == "swap":
                lines.append(f"  event.replaceInput({{ id: '{c['recipe']}' }}, '{c['from']}', '{c['to']}')")
            else:
                lines.append(f"  event.custom({json.dumps(c['json'])}).id('{c['id']}')")
        lines.append("")
    lines[-1] = "})"
    return "\n".join(lines) + "\n"


def name(i):
    return i.lstrip("#")


def doc():
    out = ["## The round of October 2026", "",
           "Every mod leans on at least one other, and key materials get a slow first route and a fast later one. "
           "Generated from `tools/recipes/round.py`, which also checks every change against a dump of the running pack.", ""]
    for family, changes in CHANGES.items():
        out += [f"### {family}", "", "| Recipe | Change | Why |", "| --- | --- | --- |"]
        for c in changes:
            if c["kind"] == "swap":
                out.append(f"| `{c['recipe']}` | `{name(c['from'])}` becomes `{name(c['to'])}` | {c['why']} |")
            else:
                out.append(f"| `{c['id']}` | new: {', '.join('`' + name(i) + '`' for i in c['in'])} to `{c['out'][0]}` | {c['why']} |")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    errors, notes = check(sys.argv[1])
    by_id = {r["id"]: r for r in json.load(open(os.path.join(sys.argv[1], "recipes.json")))}
    for n in sorted(set(notes)):
        print("note:", n)
    for e in errors:
        print("ERROR:", e)
    if errors and "--force" not in sys.argv:
        sys.exit(1)
    open(OUT_JS, "w").write(js(by_id))
    text = open(DOC).read()
    mark = "## The round of October 2026"
    if mark in text:
        text = text[:text.index(mark)].rstrip() + "\n"
    open(DOC, "w").write(text.rstrip() + "\n\n" + doc())
    print("written", OUT_JS, "and", DOC)
