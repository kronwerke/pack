#!/usr/bin/env python3
"""Progression checker for Kronwerke Season 2.

Usage: check_progression.py <recipes.json> <mods dir> <stages dir>
           [--quests <built ftbquests dir>] [--goals <goals.json>] [--report <out.md>]
           [--vanilla <minecraft jar>] [--neoforge <neoforge universal jar>]

Model
- Every recipe in the dump becomes inputs (a list of groups; a group is satisfied by any one
  of its nodes), machines (groups like inputs, not consumed) and outputs (a set of nodes).
  Nodes are items ("ns:path"), fluids ("fluid:ns:path"), Mekanism chemicals
  ("chem:ns:path"), Productive Bees bees ("bee:ns:type") and dimensions ("dim:ns:path"). An
  item tag in an ingredient is the group of all its members.
- MACHINES maps a recipe type to the blocks it needs; an unlisted type whose id is also an
  item id needs that item; other unknown types need nothing and are listed in the report.
  EXTRA_RECIPES and a few implicit rules add mechanics that are not recipes: buckets,
  breaking a block for its loot table drops, copper weathering, bee spawn eggs.
- Raw materials: items that no recipe makes (recipe types in WORLD_TYPES do not count), mob
  and fishing drops (a modded mob only for items of its own mod), blocks placed by world
  generation, items in WORLD_TAGS and WORLD_ITEMS, and items only made from themselves or
  from their own storage block. Raw fluids and chemicals are free unless their whole mod is
  locked. DIMENSION_ITEMS and the namespace of a locked modded dimension delay raw items to
  the stage that opens the dimension.
- Locks: an item is locked until the first stage file that lists its id; if none does, until
  the first stage that lists "@namespace"; otherwise it is open from stage 1.
- Stage S is a fixed point: a node is usable if it is reached and not locked after S. A
  recipe fires when every input group and machine group has a usable node. Crafting grid
  recipes (CRAFTING) do not fire while their output is locked. Machine recipes do: their
  locked outputs are reached (a leak) but stay unusable until they open.
- A tag output (IE, NuclearCraft, Theurgy...) gives one member: from the recipe's own mod if
  possible, then minecraft, then the first id in sorted order.
- Quest chapters and crates take their stage from tools/quests next to this script.

Limits
- Amounts, chances, energy, mana, source, heat, aura and biomes are ignored. A 5 percent
  byproduct counts as a full output. Mob drops count as free even for rare mobs.
- Chest loot, loot modifiers, trades and structure blocks are not sources. World generation
  is not split by dimension except for DIMENSION_ITEMS and modded dimension namespaces.
- Tags changed at runtime (KubeJS tag events) are not seen; only jar data is used. Recipes
  added by KubeJS are only seen if the dump has them (zzz_kw_dump.js writes addedRecipes).
- Ingredients of custom types without item ids (Silent Gear parts, Apotheosis gems, some
  spirits) are ignored, so they count as always there.
- Multiblocks are reduced to key blocks (IE engineering blocks, the chalks and bowls of an
  Occultism pentacle). Component data is ignored except the Productive Bees bee type.
"""
import argparse
import collections
import glob
import importlib
import io
import json
import os
import re
import sys
import zipfile

# Recipe type -> machines. "a + b" needs a and b, "a|b" a or b, "#tag" any member of an item tag,
# "*" is a wildcard over item ids. A type that is not listed but is also an item id (ae2:inscriber,
# nuclearcraft:melter) needs that item. Sequenced assembly takes the machines of its steps;
# Occultism rituals take their pentacle and spirit jobs the ritual that summons the spirit.
APPARATUS = ("ars_nouveau:enchanting_apparatus + ars_nouveau:arcane_core + ars_nouveau:arcane_pedestal"
             " + ars_nouveau:source_jar")
POOL = "botania:mana_pool|botania:diluted_mana_pool|botania:fabulous_mana_pool"


def _ns(ns, **types):
    """Entries for one mod: requirements split by " + ", ids without a namespace get ns."""
    fix = lambda x: x if ":" in x or x.startswith("#") else ns + ":" + x
    return {ns + ":" + t: ["|".join(fix(a) for a in req.split("|")) for req in v.split(" + ") if req]
            for t, v in types.items()}


MACHINES = {
    **_ns("minecraft", smelting="furnace", blasting="blast_furnace", smoking="smoker",
        campfire_cooking="campfire|soul_campfire", stonecutting="stonecutter", smithing_transform="smithing_table",
        smithing_trim="smithing_table"),
    **_ns("create", mixing="mechanical_mixer + basin", compacting="mechanical_press + basin",
        pressing="mechanical_press", cutting="mechanical_saw", milling="millstone", crushing="crushing_wheel",
        deploying="deployer", filling="spout", emptying="item_drain", splashing="encased_fan",
        haunting="encased_fan + minecraft:soul_campfire|minecraft:soul_sand|minecraft:soul_soil",
        sandpaper_polishing="sand_paper|red_sand_paper",
        mechanical_crafting="mechanical_crafter", item_application="", sequenced_assembly=""),
    **_ns("create_dragons_plus", ending="create:encased_fan + minecraft:dragon_head|minecraft:dragon_breath",
        freezing="create:encased_fan + minecraft:powder_snow_bucket"),
    **_ns("create_enchantment_industry", grinding="mechanical_grindstone", infusing="infuser"),
    **_ns("createaddition", charging="tesla_coil", rolling="rolling_mill"),
    **_ns("createdieselgenerators", basin_fermenting="create:basin + basin_lid", bulk_fermenting="bulk_fermenter",
        distillation="distillation_controller", hammering="create:mechanical_press",
        compression_molding="create:mechanical_press + create:basin", wire_cutting="create:deployer",
        casting="create:basin"),
    **_ns("createoreexcavation", drilling="drilling_machine", extracting="extractor", vein=""),
    **_ns("create_mechanical_spawner", spawner="mechanical_spawner"),
    **_ns("mekanism", enriching="enrichment_chamber", crushing="crusher", sawing="precision_sawmill",
        combining="combiner", injecting="chemical_injection_chamber", purifying="purification_chamber",
        compressing="osmium_compressor", metallurgic_infusing="metallurgic_infuser", painting="painting_machine",
        pigment_extracting="pigment_extractor", pigment_mixing="pigment_mixer", oxidizing="chemical_oxidizer",
        chemical_conversion="metallurgic_infuser|chemical_injection_chamber|purification_chamber|osmium_compressor",
        dissolution="chemical_dissolution_chamber", washing="chemical_washer", crystallizing="chemical_crystallizer",
        chemical_infusing="chemical_infuser", reaction="pressurized_reaction_chamber",
        separating="electrolytic_separator",
        evaporating="thermal_evaporation_controller + thermal_evaporation_valve",
        activating="solar_neutron_activator", centrifuging="isotopic_centrifuge",
        nucleosynthesizing="antiprotonic_nucleosynthesizer", rotary="rotary_condensentrator", energy_conversion=""),
    **_ns("mekmm", planting="planting_station", stamper="cnc_stamper", lathe="cnc_lathe",
        rolling_mill="cnc_rolling_mill", pressing="presser"),
    **_ns("botania", mana_infusion=POOL + " + mana_spreader", petal_apothecary="petal_apothecary|*_petal_apothecary",
        runic_altar="runic_altar + mana_spreader", runic_altar_head="runic_altar + mana_spreader",
        terrestrial_agglomeration_plate="terrestrial_agglomeration_plate + mana_spreader",
        elven_trade="elven_gateway_core + natura_pylon + " + POOL,
        elven_trade_lexicon="elven_gateway_core + natura_pylon + " + POOL,
        pure_daisy="pure_daisy|floating_pure_daisy",
        brew="botanical_brewery"),
    **_ns("ars_nouveau", enchanting_apparatus=APPARATUS, enchantment=APPARATUS, armor_upgrade=APPARATUS,
        reactive_enchantment=APPARATUS, spell_write=APPARATUS, imbuement="imbuement_chamber + source_jar",
        glyph="scribes_table", crush="glyph_crush", budding_conversion="glyph_intangible|glyph_crush",
        summon_ritual="ritual_brazier", dispel_entity="glyph_dispel", alakarkinos_conversion="alakarkinos_charm"),
    **_ns("sauce", armor_upgrade=APPARATUS),
    **_ns("ars_elemental", netherite_upgrade=APPARATUS),
    **_ns("ars_additions", charm_charging="ars_nouveau:enchanting_apparatus + ars_nouveau:arcane_core"),
    **_ns("occultism", ritual="", crystallize="", spirit_trade="", spirit_fire="datura + minecraft:flint_and_steel",
        miner="dimensional_mineshaft",
        crushing="|".join("ritual_dummy/summon_%s_crusher" % s for s in ("foliot", "djinni", "afrit", "marid"))),
    **_ns("naturesaura", altar="nature_altar", tree_ritual="wood_stand", offering="offering_table"),
    **_ns("theurgy", calcination="calcination_oven", liquefaction="liquefaction_cauldron", distillation="distiller",
        incubation="incubator", digestion="digestion_vat", fermentation="fermentation_vat",
        accumulation="sal_ammoniac_accumulator", catalysation="mercury_catalyst",
        reformation="reformation_target_pedestal + reformation_source_pedestal + reformation_result_pedestal"),
    **_ns("malum", spirit_infusion="spirit_altar", spirit_focusing="spirit_crucible",
        spirit_repair="spirit_crucible + repair_pylon", runeworking="runic_workbench",
        soul_binding="soulbinding_brazier", void_favor="void_conduit",
        node_smelting="spirit_catalyzer|spirit_crucible", node_blasting="spirit_catalyzer|spirit_crucible"),
    **_ns("eidolon_repraised", ritual_brazier="brazier",
        ritual_brazier_crafting="brazier", ritual_brazier_summoning="brazier", athame_foraging="athame"),
    **_ns("hexerei", mixingcauldron="mixing_cauldron", fluid_mixing="mixing_cauldron",
        cauldron_filling="mixing_cauldron", cauldron_emptying="mixing_cauldron", dipper="candle_dipper",
        drying_rack="herb_drying_rack|*_drying_rack"),
    **_ns("forbidden_arcanus", clibano_combustion="clibano_core"),
    **_ns("irons_spellbooks", alchemist_cauldron_brew="alchemist_cauldron",
        alchemist_cauldron_fill="alchemist_cauldron", alchemist_cauldron_empty="alchemist_cauldron"),
    **_ns("reliquary", alkahestry_crafting="alkahestry_tome"),
    **_ns("eternal_starlight", alloy="alloy_furnace", drying="drying_rack", ether_conversion="ether_bucket"),
    **_ns("undergarden", infuser_conversion="infuser", item_infusing="infuser"),
    **_ns("mysticalagriculture", infusion="infusion_altar + infusion_pedestal",
        awakening="awakening_altar + awakening_pedestal", reprocessor="seed_reprocessor|*_reprocessor",
        soul_extraction="soul_extractor|*_soul_extractor", farmland_till=""),
    **_ns("ae2", entropy="entropy_manipulator", transform="", storage_cell_disassembly=""),
    **_ns("advanced_ae", reaction="reaction_chamber"),
    **_ns("powah", energizing="energizing_orb + #powah:energizing_rods|energizing_rod_starter"),
    **_ns("draconicevolution", fusion_crafting="crafting_core + basic_crafting_injector"),
    **_ns("immersiveengineering", metal_press="heavy_engineering + hammer", crusher="light_engineering + hammer",
        sawmill="light_engineering + heavy_engineering + hammer",
        arc_furnace="heavy_engineering + rs_engineering + graphite_electrode + hammer", alloy="alloybrick + hammer",
        blast_furnace="blastbrick + hammer", coke_oven="cokebrick + hammer",
        bottling_machine="light_engineering + hammer", mixer="light_engineering + hammer",
        squeezer="light_engineering + hammer", fermenter="light_engineering + hammer",
        refinery="heavy_engineering + hammer", hammer_crushing="hammer",
        mineral_mix="heavy_engineering + rs_engineering + hammer", blueprint="workbench"),
    **_ns("enderio", sag_milling="sag_mill", alloy_smelting="alloy_smelter", slicing="slice_and_splice",
        soul_binding="soul_binder", vat_fermenting="vat", painting="painting_machine", enchanting="enchanter",
        tank="fluid_tank|pressurized_fluid_tank", fire_crafting="minecraft:flint_and_steel"),
    **_ns("industrialforegoing", laser_drill_ore="ore_laser_base + laser_drill",
        laser_drill_fluid="fluid_laser_base + laser_drill", stonework_generate="material_stonework_factory",
        crusher="material_stonework_factory"),
    **_ns("oritech", pulverizer="pulverizer_block", grinder="fragment_forge_block", centrifuge="centrifuge_block",
        centrifuge_fluid="centrifuge_block", foundry="foundry_block", assembler="assembler_block",
        atomic_forge="atomic_forge_block", refinery="refinery_block", deep_drill="deep_drill_block",
        particle_collision="particle_collector_block", laser="laser_arm_block", cooler="reactor_controller"),
    **_ns("nuclearcraft", fission_reactor="fission_reactor_controller", fusion_reactor="fusion_reactor_core",
        target_chamber="target_chamber_controller", collision_chamber="collision_chamber_controller",
        decay_chamber="decay_chamber_controller", kugelblitz_chamber="ring_accelerator_controller",
        heat_exchanger="heat_exchanger_controller", turbine="turbine_controller", nc_ore_veins="",
        fusion_coolant="fusion_reactor_core", accelerator_coolant="linear_accelerator_controller",
        fission_boiling="fission_reactor_controller"),
    **_ns("productivemetalworks", item_melting="*_foundry_controller", fluid_alloying="*_foundry_controller",
        item_casting="casting_table", block_casting="casting_basin"),
    **_ns("productivebees", centrifuge="centrifuge|powered_centrifuge|heated_centrifuge",
        advanced_beehive="#productivebees:advanced_beehives|advanced_oak_beehive", bee_breeding="",
        bee_conversion="", bee_spawning="", bee_fishing=""),
    **_ns("justdirethings", goospread="gooblock_tier1|gooblock_tier2|gooblock_tier3|gooblock_tier4",
        goospread_tag="gooblock_tier1|gooblock_tier2|gooblock_tier3|gooblock_tier4", fluiddrop=""),
    **_ns("silentgear", salvaging="salvager",
        **{"alloy_making/metal": "alloy_forge", "alloy_making/gem": "recrystallizer",
           "pressing/material": "metal_press",
           "salvaging/gear": "salvager", "salvaging/compound_part": "salvager",
           "smithing/upgrade": "minecraft:smithing_table", "smithing/coating": "minecraft:smithing_table"}),
    **_ns("ironfurnaces", generator_blasting="*_furnace"),
    **_ns("farmersdelight", cutting="cutting_board", cooking="cooking_pot"),
    **_ns("apotheosis", salvaging="salvaging_table", reforging="reforging_table|simple_reforging_table"),
    **_ns("apothic_enchanting", infusion="minecraft:enchanting_table|apothic_enchanting_table",
        keep_nbt_infusion="minecraft:enchanting_table|apothic_enchanting_table"),
    **_ns("cataclysm", weapon_fusion="mechanical_fusion_anvil"),
    **_ns("powergrid", boost_recipe="basin_heater"),
}

# Types that run in a crafting grid: Chapters blocks them while their output is locked. Types
# not in MACHINES whose name has one of CRAFTING_WORDS count as crafting grid types too.
CRAFTING = {
    "mekanism:mek_data", "refinedstorage:recoloring", "silentgear:gear_crafting", "silentgear:conversion",
    "silentgear:compound_part", "ars_nouveau:dye", "mekanismtools:paxel", "silentgear:tool_action",
    "immersiveengineering:turn_and_copy", "sophisticatedstorage:shulker_box_from_chest",
    "sophisticatedstorage:generic_wood_storage", "theurgy:divination_rod", "supplementaries:sus_crafting",
    "supplementaries:add_charges", "hexerei:add_to_candle", "eidolon_repraised:dye", "ars_nouveau:potion_flask",
    "justdirethings:paxel", "sophisticatedbackpacks:basic_backpack", "reliquary:mob_charm",
    "reliquary:fragment_to_spawn_egg", "immersiveengineering:revolver_assembly", "ae2:quartz_cutting",
}
CRAFTING_WORDS = ("crafting_", "shaped", "shapeless", "copy_components", "_dye", "upgrade", "clear")

# Recipe types that stand for the world, farms or spawners. Their outputs can still be raw
# materials; the recipes still fire when their machine is there.
WORLD_TYPES = {
    "occultism:miner", "occultism:spirit_trade", "immersiveengineering:cloche", "immersiveengineering:mineral_mix",
    "industrialforegoing:laser_drill_ore", "industrialforegoing:laser_drill_fluid",
    "industrialforegoing:stonework_generate", "mekmm:planting", "createoreexcavation:drilling",
    "createoreexcavation:extracting", "oritech:deep_drill", "botania:orechid", "botania:orechid_ignem",
    "botania:marimorphosis", "farmingforblockheads:market", "create_mechanical_spawner:spawner",
    "naturesaura:animal_spawner", "productivebees:bee_spawning", "productivebees:block_conversion",
    "mysticalagriculture:soulium_spawner", "ars_nouveau:alakarkinos_conversion",
    "eidolon_repraised:athame_foraging", "nuclearcraft:nc_ore_veins", "ae2:entropy",
    "evilcraft:environmental_accumulator", "ars_nouveau:summon_ritual",
}

# Keys that hold outputs; every other key that names items is an input.
OUTPUT_KEYS = {
    "result", "results", "output", "outputs", "result_item", "item_output", "item_outputs", "fluid_output",
    "fluid_outputs", "chemical_output", "left_chemical_output", "right_chemical_output", "main_output",
    "secondary_output", "secondaryOutput", "secondaryOutputs", "secondaries", "slag", "output_item",
    "output_items", "output_fluid", "outputFluid", "fluidOutputs", "liquidOutput", "byproduct", "result_cell",
    "result_component", "cell_disassembly_items", "spoils", "ores", "stripped", "strippingSecondaries",
    "upgraded_block", "to", "residue", "bonus",
}
IGNORE_KEYS = {"type", "id", "icon", "pattern", "ritual_dummy", "render", "target", "sound", "conditions",
               "neoforge:conditions", "fabric:load_conditions", "neoforge:load_conditions", "entity_to_sacrifice",
               "sample_background", "spell", "spellData", "biome_predicates", "rarity", "components", "category",
               "group"}
TYPE_OUTPUTS = {"immersiveengineering:fermenter": {"fluid"}, "immersiveengineering:squeezer": {"fluid"},
                "irons_spellbooks:alchemist_cauldron_fill": {"fluid"}, "hexerei:cauldron_filling": {"fluid"}}
# Singular keys whose list value means "any of", not "all of".
OR_KEYS = {"ingredient", "input", "tool", "base", "addition", "template", "reagent", "catalyst", "mold", "cast",
           "sapling", "start_item", "soil", "item", "activation_item", "input_item", "main_input", "extra_input"}
MEK_FAMILY = ("mekanism", "mekanismgenerators", "mekmm", "appmek")

# Vanilla items that only come from a dimension that opens later (Chapters locks the
# dimension, not the item).
DIMENSION_ITEMS = {
    2: "netherite_ingot netherite_scrap netherite_block ancient_debris blaze_rod blaze_powder nether_wart ghast_tear "
       "nether_star wither_skeleton_skull magma_cream quartz nether_quartz_ore glowstone_dust glowstone netherrack "
       "soul_sand soul_soil basalt blackstone gilded_blackstone magma_block nether_gold_ore crimson_stem warped_stem "
       "crimson_nylium warped_nylium crimson_fungus warped_fungus shroomlight nether_wart_block warped_wart_block "
       "weeping_vines twisting_vines crimson_roots warped_roots netherite_upgrade_smithing_template piglin_head "
       "wither_rose music_disc_pigstep",
    4: "elytra shulker_shell shulker_box dragon_breath dragon_egg dragon_head end_crystal chorus_fruit chorus_flower "
       "end_stone purpur_block end_rod",
}
# Tags and items that always count as world materials, even if a recipe also makes them.
WORLD_TAGS = ["c:ores", "c:raw_materials", "minecraft:logs", "minecraft:saplings", "minecraft:leaves", "c:seeds",
              "c:crops", "minecraft:flowers", "c:cobblestones", "c:stones", "c:sands", "c:gravels", "minecraft:dirt",
              "minecraft:fishes", "c:obsidians", "c:netherracks", "c:end_stones"]
WORLD_ITEMS = ["minecraft:water_bucket", "minecraft:lava_bucket", "minecraft:milk_bucket", "minecraft:clay_ball",
               "minecraft:ice", "minecraft:snowball", "minecraft:ender_pearl", "minecraft:egg", "minecraft:honeycomb",
               "minecraft:amethyst_shard", "minecraft:budding_amethyst", "minecraft:sugar_cane", "minecraft:bamboo",
               "apotheosis:gem", "bee:minecraft:bee", "draconicevolution:chaos_shard"]  # last: Chaos Guardian drop

# Game mechanics that are not recipes: (inputs, machines, outputs); an entry may be "a|b".
EXTRA_RECIPES = [(["occultism:book_of_binding_%s" % s, "occultism:dictionary_of_spirits"], [],
                  ["occultism:book_of_binding_bound_%s" % s]) for s in ("foliot", "djinni", "afrit", "marid")] + [
    (["chem:mekanism:polonium"], ["mekanism:sps_casing", "mekanism:sps_port", "mekanism:supercharged_coil"],
     ["chem:mekanism:antimatter"]),
    (["chem:mekanism:fissile_fuel"], ["mekanismgenerators:fission_reactor_casing",
                                      "mekanismgenerators:fission_fuel_assembly",
                                      "mekanismgenerators:control_rod_assembly"], ["chem:mekanism:nuclear_waste"]),
    (["hexerei:blood_sigil"], ["hexerei:mixing_cauldron"], ["fluid:hexerei:blood_fluid"]),
    (["apotheosis:gem"], ["minecraft:anvil|minecraft:chipped_anvil|minecraft:damaged_anvil"],
     ["apotheosis:gem_dust"]),
    (["evilcraft:dark_gem", "fluid:evilcraft:blood"], [], ["evilcraft:dark_power_gem"]),
    (["create:empty_blaze_burner", "minecraft:blaze_rod"], [], ["create:blaze_burner"]),   # catch a blaze
]

# Sanity targets: each must be reachable in its stage.
SANITY = {1: ["create:andesite_alloy", "ars_nouveau:source_gem", "minecraft:cobblestone"],
          2: ["create:brass_ingot", "botania:mana_pearl", "botania:terrasteel_ingot"],
          3: ["mekanism:ingot_steel", "mekanism:advanced_control_circuit", "botania:elementium_ingot"],
          4: ["draconicevolution:draconium_ingot", "botania:gaia_spirit"],
          5: ["draconicevolution:awakened_draconium_ingot"]}

STAGES = [1, 2, 3, 4, 5]
FLUID, CHEM, BEE, DIM = "fluid:", "chem:", "bee:", "dim:"
VIRTUAL = (FLUID, CHEM, BEE, DIM)


def norm_type(t):
    return t if ":" in t else "minecraft:" + t


def is_crafting(t):
    return t in CRAFTING or (t not in MACHINES and any(w in t.split(":")[-1] for w in CRAFTING_WORDS))


def mod_of(node):
    return node.split(":")[1] if node.startswith(VIRTUAL) else node.split(":")[0]


class Data:
    """Items, tags, drops, world generation and names read from the jars."""

    def __init__(self):
        self.items, self.names, self.worldgen = set(), {}, set()
        self.tags = {"item": {}, "fluid": {}, "block": {}, "chem": {}}
        self.drops, self.block_drops, self.multiblocks = set(), {}, {}

    def load_jar(self, z, depth=0):
        for n in z.namelist():
            if n.startswith("META-INF/jarjar/") and n.endswith(".jar") and depth < 2:
                self.load_jar(zipfile.ZipFile(io.BytesIO(z.read(n))), depth + 1)
            if not n.endswith(".json"):
                continue
            m = re.match(r"assets/([^/]+)/models/item/([^/]+)\.json$", n)
            if m:
                self.items.add(m.group(1) + ":" + m.group(2))
            elif re.match(r"assets/[^/]+/lang/en_us\.json$", n):
                for k, v in self.read(z, n).items():
                    mm = re.match(r"(item|block)\.([a-z0-9_.-]+)\.([a-z0-9_./-]+)$", k)
                    if mm and isinstance(v, str):
                        self.names.setdefault(mm.group(2) + ":" + mm.group(3), v)
            elif re.match(r"data/[^/]+/tags/", n):
                m = re.match(r"data/([^/]+)/tags/(items?|fluids?|blocks?|mekanism/chemical)/(.+)\.json$", n)
                if m:
                    kind = {"items": "item", "fluids": "fluid", "blocks": "block", "mekanism/chemical": "chem"}
                    self.add_tag(kind.get(m.group(2), m.group(2)), m.group(1) + ":" + m.group(3), self.read(z, n))
            elif re.match(r"data/[^/]+/loot_tables?/(entities|gameplay)/", n):
                ns, found = n.split("/")[1], set()
                self.loot_items(self.read(z, n), found)
                # A modded mob counts only for its own mod's items (some mobs are built by players).
                self.drops |= {i for i in found if ns == "minecraft" or i.lstrip("#").split(":")[0] == ns}
            elif re.match(r"data/[^/]+/loot_tables?/blocks/", n):
                m = re.match(r"data/([^/]+)/loot_tables?/blocks/(.+)\.json$", n)
                self.loot_items(self.read(z, n), self.block_drops.setdefault(m.group(1) + ":" + m.group(2), set()))
            elif re.match(r"data/[^/]+/worldgen/configured_feature/", n):
                self.worldgen |= set(re.findall(r'"Name"\s*:\s*"([^"]+)"', z.read(n).decode("utf-8", "replace")))
            elif n.startswith("data/occultism/modonomicon/multiblocks/"):
                self.multiblocks["occultism:" + n.rsplit("/", 1)[1][:-5]] = self.read(z, n)

    @staticmethod
    def read(z, n):
        try:
            d = json.loads(z.read(n))
            return d if isinstance(d, dict) else {}
        except ValueError:
            return {}

    def add_tag(self, kind, name, d):
        vals = {v.get("id") if isinstance(v, dict) else v for v in d.get("values", [])}
        t = self.tags[kind]
        t[name] = vals if d.get("replace") else t.get(name, set()) | vals

    def loot_items(self, d, out):
        if isinstance(d, dict) and isinstance(d.get("name"), str):
            t = d.get("type", "").replace("minecraft:", "")
            out |= {d["name"]} if t == "item" else {"#" + d["name"]} if t == "tag" else set()
        for v in (d.values() if isinstance(d, dict) else d if isinstance(d, list) else []):
            self.loot_items(v, out)

    def expand(self, nodes):
        return set().union(*[self.members("item", n[1:]) if n.startswith("#") else {n} for n in nodes])

    def members(self, kind, name, seen=None):
        """All items (or fluids, blocks, chemicals) of a tag, nested tags resolved."""
        seen = seen if seen is not None else set()
        if name in seen:
            return set()
        seen.add(name)
        vals = [v for v in self.tags[kind].get(name, ()) if v]
        return {v for v in vals if v[0] != "#"}.union(*[self.members(kind, v[1:], seen) for v in vals if v[0] == "#"])


class Recipe:
    __slots__ = ("id", "type", "ins", "mach", "outs", "grid", "world")

    def __init__(self, rid, rtype, ins=(), mach=(), outs=()):
        self.id, self.type = rid, rtype
        self.ins, self.mach, self.outs = list(ins), list(mach), set(outs)
        self.grid, self.world = is_crafting(rtype), rtype in WORLD_TYPES


class Parser:
    """Turns raw recipe JSON into Recipe objects."""

    def __init__(self, data):
        self.d = data
        self.opaque = collections.Counter()   # custom ingredient types that name no item
        self.empty = collections.Counter()    # tags that resolve to nothing
        self.job_dummy = {}                   # occultism spirit job -> ritual dummy item
        self.memo = {}

    def tag(self, name, kind):
        name = name if ":" in name else "minecraft:" + name
        if (name, kind) not in self.memo:
            k = {"item": "item", FLUID: "fluid", CHEM: "chem"}[kind]
            mem = self.d.members(k, name) or (self.d.members("block", name) if k == "item" else set())
            self.memo[(name, kind)] = {("" if kind == "item" else kind) + m for m in mem
                                       if not (k == "fluid" and re.search(r":flowing_|_flowing$", m))}
        if not self.memo[(name, kind)]:
            self.empty[("#" if kind == "item" else kind + "#") + name] += 1
        return self.memo[(name, kind)]

    def refs(self, v, kind, mek=False):
        """All nodes that one ingredient or output spec can be."""
        out = set()
        if isinstance(v, str):
            if re.match(r"#[a-z0-9_.-]+(:[a-z0-9_./-]+)?$", v):
                return set(self.tag(v[1:], kind))
            if ":" in v and (kind != "item" or v in self.d.items):
                out.add(("" if kind == "item" else kind) + v)
            return out
        if isinstance(v, list):
            for x in v:
                out |= self.refs(x, kind, mek)
            return out
        if not isinstance(v, dict):
            return out
        t = str(v.get("type", ""))
        if t == "neoforge:difference":
            return self.refs(v.get("base"), kind, mek)
        if t == "neoforge:intersection":
            sets = [self.refs(c, kind, mek) for c in v.get("children", [])]
            return set.intersection(*sets) if sets else out
        comp = v.get("components") if isinstance(v.get("components"), dict) else {}
        bee = comp.get("productivebees:bee_type") or (comp.get("minecraft:entity_data") or {}).get("type")
        if isinstance(bee, str) and bee.startswith("productivebees:"):
            base = self.refs({k: x for k, x in v.items() if k not in ("components", "type")}, kind, mek)
            return {b + "[" + bee + "]" for b in base}
        if "fluid" in t:
            kind = FLUID
        k2 = kind
        if kind == "item" and "amount" in v and "count" not in v:
            k2 = CHEM if mek else FLUID
        for key, val in v.items():
            if key in ("id", "item") and isinstance(val, str) and ":" in val:
                out.add(val if k2 == "item" or key == "item" else k2 + val)
            elif key == "tag" and isinstance(val, str):
                out |= self.tag(val, k2)
            elif key == "fluid_tag" and isinstance(val, str):
                out |= self.tag(val, FLUID)
            elif key in ("fluid", "fluids"):
                out |= self.refs(val, FLUID, mek)
            elif key in ("chemical", "gas", "infuse_type", "pigment", "slurry") and isinstance(val, str):
                out.add(CHEM + val)
            elif key == "items" and isinstance(val, (str, list)):
                out |= self.refs(val, kind, mek)
            elif key in ("block", "Name") and isinstance(val, str):
                out.add(FLUID + val[:-6] if val.endswith("_fluid_block") else val)
            elif key == "state" and isinstance(val, dict) and "Name" in val:
                out.add(val["Name"])
            elif key in ("item", "tag", "block", "stack", "ingredient", "basePredicate", "base", "children",
                         "ingredients", "output", "result"):
                out |= self.refs(val, kind, mek)
        return out

    def groups(self, key, v, kind, mek, rtype):
        """Input groups of one top level key."""
        if isinstance(v, list):
            parts = [v] if key in OR_KEYS else v
        elif isinstance(v, dict):
            ref_keys = {"item", "items", "tag", "fluid", "fluids", "fluid_tag", "chemical", "id", "type", "block",
                        "ingredient", "basePredicate", "base", "stack", "children", "Name"}
            parts = [v] if ref_keys & set(v) else list(v.values())
        elif isinstance(v, str) and ":" in v:
            parts = [v]
        else:
            return []
        out = []
        for p in parts:
            r = self.refs(p, kind, mek)
            if r:
                out.append(frozenset(r))
            elif isinstance(p, dict) and ("tag" in p or "fluid_tag" in p):
                out.append(frozenset())   # empty tag: never satisfied
            elif isinstance(p, dict) and "type" in p:
                self.opaque[rtype] += 1
        return out

    def outputs(self, v, kind, mek, rid, rtype):
        """Output nodes. A tag output gives one member: the recipe's mod first, then minecraft."""
        out, pref = set(), [rtype.split(":")[0], rid.split(":")[0], "minecraft"]
        for p in (v if isinstance(v, list) else [v]):
            nodes = self.refs(p, kind, mek)
            if len(nodes) > 1 and '"tag"' in json.dumps(p):
                rank = lambda n: (pref.index(n.split(":")[-2]) if n.split(":")[-2] in pref else 9, n)
                nodes = {min(nodes, key=rank)}
            out |= nodes
        return out

    def parse(self, rid, j):
        rtype = norm_type(str(j.get("type", "?")))
        r = Recipe(rid, rtype)
        mek = rtype.split(":")[0] in MEK_FAMILY
        if rtype == "create:sequenced_assembly":
            return self.sequenced(r, j)
        if rtype == "eidolon_repraised:crucible":
            j = dict(j, steps=[i for s in j.get("steps", []) for i in s.get("items", [])])
        for key, v in j.items():
            if key in IGNORE_KEYS:
                continue
            kl = key.lower()
            kind = FLUID if "fluid" in kl else CHEM if ("chemical" in kl or "gas" in kl) else "item"
            if rtype in ("mekanism:separating", "mekanism:evaporating") and key == "input":
                kind = FLUID
            if key in OUTPUT_KEYS or key in TYPE_OUTPUTS.get(rtype, ()):
                r.outs |= self.outputs(v, kind, mek, rid, rtype)
            elif key == "spirits" and isinstance(v, list):
                r.ins += [frozenset([s["type"] + "_spirit"]) for s in v if isinstance(s, dict) and "type" in s]
            else:
                r.ins += self.groups(key, v, kind, mek, rtype)
        self.special(r, j)
        return r

    def special(self, r, j):
        bee = lambda b: BEE + re.sub(r"_bee$", "", b)
        t = r.type
        if t == "immersiveengineering:coke_oven" and j.get("creosote"):
            r.outs.add(FLUID + "immersiveengineering:creosote")
        elif t == "occultism:ritual":
            dummy = (j.get("ritual_dummy") or {}).get("id")
            if j.get("spirit_job_type") and dummy:
                self.job_dummy[j["spirit_job_type"]] = dummy
            if j.get("entity_to_summon") and dummy:
                r.outs.add(dummy)
        elif t == "mekanism:rotary":   # works both ways: either input gives the other form
            r.ins = [frozenset().union(*r.ins)]
        elif t == "reliquary:alkahestry_crafting":
            r.outs |= self.refs(j.get("ingredient"), "item")
        elif t.startswith("justdirethings:") and isinstance(j.get("id"), str):
            r.outs.add(FLUID + j["id"])
        elif t == "productivebees:advanced_beehive" and isinstance(j.get("ingredient"), str):
            r.ins.append(frozenset([bee(j["ingredient"])]))
        elif t == "productivebees:bee_conversion":
            r.ins.append(frozenset([bee(j.get("source", "?"))]))
            r.outs.add(bee(j.get("result", "?")))
        elif t == "productivebees:bee_breeding":
            r.ins += [frozenset([bee(j.get("parent1", "?"))]), frozenset([bee(j.get("parent2", "?"))])]
            r.outs.add(bee(j.get("offspring", "?")))
        elif t == "productivebees:bee_spawning":
            r.outs |= {bee(b) for b in j.get("results", []) if isinstance(b, str)}
        elif t == "productivebees:bee_fishing":
            r.outs.add(bee(j.get("bee", "?")))
        for o in list(r.outs):
            m = re.match(r"productivebees:spawn_egg_configurable_bee\[(.+)\]$", o)
            if m:
                r.outs.add(bee(m.group(1)))
        if r.world:
            s = json.dumps(j)
            for dim, rx in (("minecraft:the_nether", r"is_nether|whitelist\": \[[^\]]*the_nether"),
                            ("minecraft:the_end", r"is_end\b|whitelist\": \[[^\]]*the_end")):
                if re.search(rx, s):
                    r.mach.append(frozenset([DIM + dim]))

    def sequenced(self, r, j):
        trans = self.refs(j.get("transitional_item"), "item")
        r.ins += self.groups("ingredient", j.get("ingredient"), "item", False, r.type)
        for step in j.get("sequence", []):
            r.mach += self.machine_groups(norm_type(step.get("type", "")), step)
            r.ins += [g for g in self.groups("ingredients", step.get("ingredients", []), "item", False, r.type)
                      if not g & trans]
        r.outs |= self.outputs(j.get("results"), "item", False, r.id, r.type) | trans
        return r

    def machine_groups(self, rtype, j):
        reqs = list(MACHINES.get(rtype, [rtype] if rtype in self.d.items and not is_crafting(rtype) else []))
        heat = j.get("heat_requirement") or j.get("heatRequirement")
        if rtype in ("create:mixing", "create:compacting") and heat in ("heated", "superheated"):
            reqs += ["create:blaze_burner"] + (["create:blaze_cake"] if heat == "superheated" else [])
        out = [self.alts(q) for q in reqs]
        if rtype == "occultism:ritual":
            out += self.pentacle(j.get("pentacle_id", ""))
        return [g for g in out if g]

    def alts(self, req):
        out = set()
        for a in req.split("|"):
            if a.startswith("#"):
                out |= self.tag(a[1:], "item")
            elif "*" in a:
                rx = re.compile(re.escape(a).replace(r"\*", ".*") + "$")
                out |= {i for i in self.d.items if rx.match(i)}
            else:
                out.add(a)
        return frozenset(out)

    def pentacle(self, pid):
        """Chalks, candles and bowls of an Occultism pentacle, from its multiblock file."""
        mb = self.d.multiblocks.get(pid)
        if not mb:
            return [frozenset(["occultism:golden_sacrificial_bowl"])]
        used = set(json.dumps(mb.get("pattern", [])))
        groups = [frozenset(["occultism:sacrificial_bowl"])]
        for ch, m in mb.get("mapping", {}).items():
            if ch not in used or m.get("type") == "modonomicon:display":
                continue
            blocks = {m["block"]} if "block" in m else self.d.members("block", m.get("tag", "").lstrip("#"))
            items = {re.sub(r"chalk_glyph_", "chalk_", b) for b in blocks} & self.d.items
            if items:
                groups.append(frozenset(items))
        return groups

    def finish(self, r, j):
        """Machines, some of which depend on other recipes (Occultism spirit jobs)."""
        r.mach = self.machine_groups(r.type, j) + r.mach
        if r.type == "occultism:spirit_trade":
            d = self.job_dummy.get(j.get("trader_id"))
            r.mach.append(frozenset([d] if d else []))
        if r.type == "occultism:crystallize":
            tier = int(j.get("min_tier", 1))
            r.mach.append(frozenset(d for job, d in self.job_dummy.items()
                                    if re.search(r"crystal_tier(\d)$", job) and int(job[-1]) >= tier))


def load_locks(sdir):
    item_lock, mod_lock, dims = {}, {}, {}
    for f in sorted(glob.glob(os.path.join(sdir, "stage*.json")), key=lambda p: int(re.findall(r"\d+", p)[-1])):
        n = int(re.findall(r"\d+", os.path.basename(f))[0])
        d = json.load(open(f))
        for it in d.get("items", []):
            (mod_lock if it.startswith("@") else item_lock).setdefault(it.lstrip("@"), n)
        for dim in d.get("dimensions", []):
            dims.setdefault(dim, n)
    return item_lock, mod_lock, dims


class Checker:
    def __init__(self, data, recipes, locks):
        self.d, self.recipes = data, recipes
        self.item_lock, self.mod_lock, self.dims = locks
        self.raw_stage = {}

    def lock(self, node):
        if node.startswith((BEE, DIM)):
            return 1
        if node.startswith((FLUID, CHEM)):
            return self.mod_lock.get(mod_of(node), 1)
        base = node.split("[")[0]
        return self.item_lock.get(base, self.mod_lock.get(mod_of(base), 1))

    def compute_raw(self):
        self.produced, self.world_made = collections.defaultdict(list), collections.defaultdict(list)
        nodes = set(self.d.items)
        for r in self.recipes:
            for o in r.outs:
                (self.world_made if r.world else self.produced)[o].append(r)
            nodes |= r.outs
            for g in r.ins + r.mach:
                nodes |= g
        world = set(WORLD_ITEMS) | self.d.expand(self.d.drops) | (self.d.worldgen & self.d.items)
        for t in WORLD_TAGS:
            world |= self.d.members("item", t)
        # Items only made from themselves, or from a partner only made from them (block and ingot
        # pairs with no other source), must come from the world.
        loops = lambda n, rs: all(any(g == {n} for g in r.ins) for r in rs)
        self_only = {n for n, rs in self.produced.items() if loops(n, rs) or all(
            r.ins and all(self.produced.get(m) and loops(n, self.produced[m]) for g in r.ins for m in g) for r in rs)}
        raw = {n for n in nodes if n not in self.produced or n in world or n in self_only}
        dim_ns = {d.split(":")[0]: n for d, n in self.dims.items() if not d.startswith("minecraft:")}
        for n in raw:
            self.raw_stage[n] = dim_ns.get(mod_of(n), 1)
        for s, ids in DIMENSION_ITEMS.items():
            for i in ids.split():
                if "minecraft:" + i in self.raw_stage:
                    self.raw_stage["minecraft:" + i] = max(s, self.raw_stage["minecraft:" + i])
        for d in ("minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"):
            self.raw_stage[DIM + d] = self.dims.get(d, 1)

    def run(self, S):
        """Fixed point for stage S: (reached nodes, usable nodes, first recipe of each leak)."""
        index, need = collections.defaultdict(list), []
        for ri, r in enumerate(self.recipes):
            groups = r.ins + r.mach
            need.append(len(groups))
            for gi, g in enumerate(groups):
                for n in g:
                    index[n].append((ri, gi))
        done = [set() for _ in self.recipes]
        reached, usable, leaks, stack = set(), set(), {}, []

        def reach(n, r=None):
            if n in reached:
                return
            reached.add(n)
            if self.lock(n) <= S:
                usable.add(n)
                stack.append(n)
            elif r is not None:
                leaks[n] = r

        def fire(r):
            if r.grid and any(self.lock(o) > S for o in r.outs):
                return
            for o in r.outs:
                if not (r.world and not r.mach and self.lock(o) > S):   # world gen of a locked item
                    reach(o, r)

        for n, s in self.raw_stage.items():
            if s <= S and self.lock(n) <= S:
                reach(n)
        for ri, r in enumerate(self.recipes):
            if need[ri] == 0:
                fire(r)
        while stack:
            for ri, gi in index.get(stack.pop(), ()):
                if gi not in done[ri]:
                    done[ri].add(gi)
                    need[ri] -= 1
                    if need[ri] == 0:
                        fire(self.recipes[ri])
        return reached, usable, leaks

    def why(self, item, S, usable):
        """The recipe for an item with the fewest missing groups in stage S, and those groups."""
        best = None
        for r in self.produced.get(item, []) + self.world_made.get(item, []):
            miss = [g for g in r.ins + r.mach if not g & usable]
            if r.grid and self.lock(item) > S:
                miss.append(frozenset([item]))
            if best is None or len(miss) < len(best[1]):
                best = (r, miss)
        return best


def snbt(text):
    """FTB Quests SNBT as written by tools/quests: quote keys, drop number suffixes, add commas."""
    t = re.sub(r'^(\s*)([\w.+-]+): ', r'\1"\2": ', text, flags=re.M)
    t = re.sub(r'(?<=[\s:\[])(-?\d+(?:\.\d+)?)[bdfLs]\b', r'\1', t)
    t = re.sub(r'([}\]"\w])(\s*\n\s*)(?=["{\[\w-])', r'\1,\2', re.sub(r'\[[BIL];', '[', t))
    return json.loads(t)


def quest_checks(qdir, lock):
    """(where, item, stage) for each item task, item reward and crate entry of the built book.
    Chapter and crate stages come from tools/quests next to this script; otherwise the highest
    lock among the items is used."""
    qdir = os.path.join(qdir, "quests") if os.path.isdir(os.path.join(qdir, "quests")) else qdir
    chapter_stage, table_stage = {}, {}
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quests")
    if os.path.exists(os.path.join(src, "ftbq.py")):
        sys.path.insert(0, src)
        import ftbq
        for f in sorted(os.listdir(os.path.join(src, "chapters"))):
            if f.endswith(".py") and not f.startswith("_"):
                importlib.import_module("chapters." + f[:-3])
        chapter_stage = {c["name"]: c["stage"] for c in ftbq._chapters}
        table_stage = {n: t["stage"] for n, t in ftbq._tables.items()}
    out = []
    for f in sorted(glob.glob(os.path.join(qdir, "reward_tables", "*.snbt"))):
        d, name = snbt(open(f, encoding="utf-8").read()), os.path.basename(f)[:-5]
        items = [e["item"]["id"] for e in d.get("rewards", []) if isinstance(e.get("item"), dict)]
        st = table_stage.get(name) or max([lock(i) for i in items] + [1])
        out += [("crate " + name, i, st) for i in items]
    for f in sorted(glob.glob(os.path.join(qdir, "chapters", "*.snbt"))):
        d = snbt(open(f, encoding="utf-8").read())
        found = []
        for q in d.get("quests", []):
            found += [("task", t["item"]["id"]) for t in q.get("tasks", [])
                      if t.get("type") == "item" and isinstance(t.get("item"), dict)]
            found += [("reward", t["item"]["id"]) for t in q.get("rewards", [])
                      if t.get("type") == "item" and isinstance(t.get("item"), dict)]
        name = d.get("filename") or os.path.basename(f)[:-5]
        st = chapter_stage.get(name) or max([lock(i) for _, i in found] + [1])
        out += [("chapter %s %s" % (name, w), i, st) for w, i in found]
    return out


def build(a):
    """Read jars and recipes; returns data, recipes, parser and parse failures."""
    data = Data()
    nf = a.neoforge or next(iter(sorted(glob.glob(os.path.join(
        a.mods, "..", "libraries", "net", "neoforged", "neoforge", "*", "neoforge-*-universal.jar")))), None)
    for j in [a.vanilla, nf] + sorted(glob.glob(os.path.join(a.mods, "*.jar"))):
        if j and os.path.exists(j):
            try:
                data.load_jar(zipfile.ZipFile(j))
            except zipfile.BadZipFile:
                print("bad jar:", j)
    parser, parsed, failures = Parser(data), [], []
    for e in json.load(open(a.recipes))["recipes"]:
        try:
            parsed.append((parser.parse(e["id"], e["json"]), e["json"]))
        except Exception as ex:  # a report tool: list the recipe and go on
            failures.append("%s: %r" % (e.get("id"), ex))
    for r, j in parsed:
        parser.finish(r, j)
    recipes = [r for r, _ in parsed]
    for k, (ins, mach, outs) in enumerate(EXTRA_RECIPES):
        recipes.append(Recipe("extra:%d/%s" % (k, outs[0]), "extra:mechanic",
                              [parser.alts(x) for x in ins], [parser.alts(x) for x in mach], outs))
    # Buckets: "ns:x_bucket" empties into fluid "ns:x" and fills back from it.
    fluids = {n[len(FLUID):] for r in recipes for g in r.ins + [r.outs] for n in g if n.startswith(FLUID)}
    for fl in sorted(fluids):
        if fl + "_bucket" in data.items:
            b = fl + "_bucket"
            empty = Recipe("implicit:empty/" + b, "implicit:bucket", [frozenset([b])], [],
                           [FLUID + fl, "minecraft:bucket"])
            empty.world = True   # emptying a bucket does not make the fluid non-raw
            recipes += [empty, Recipe("implicit:fill/" + b, "implicit:bucket",
                                      [frozenset([FLUID + fl]), frozenset(["minecraft:bucket"])], [], [b])]
    # Breaking a block gives its loot table drops; a crop block also grows from the seeds it drops.
    seeds = data.members("item", "c:seeds")
    for b, drops in sorted(data.block_drops.items()):
        drops = data.expand(drops) - {b}
        if drops and (b in data.items or drops & seeds):
            src = frozenset({b} & data.items | {d for d in drops if d in seeds or "seed" in d})
            recipes.append(Recipe("implicit:mining/" + b, "implicit:mining", [src], [], drops))
    # Copper blocks weather in the world: x -> exposed_x -> weathered_x -> oxidized_x.
    for i in sorted(data.items):
        ns, path = i.split(":", 1)
        for new, old in (("exposed_", ""), ("weathered_", "exposed_"), ("oxidized_", "weathered_")):
            src = {ns + ":" + old + path[len(new):] + x for x in ("", "_block")} & data.items   # copper_block
            if path.startswith(new) and "copper" in path and src:
                recipes.append(Recipe("implicit:weathering/" + i, "implicit:weathering", [frozenset(src)], [], [i]))
    return data, recipes, parser, failures


def show(g, lock=None, S=None):
    xs = sorted(g)
    if not xs:
        return "(nothing matches)"
    s = xs[0] + (" or %d more" % (len(xs) - 1) if len(xs) > 1 else "")
    if lock and S is not None and min(lock(x) for x in xs) > S:
        s += " [locked until %d]" % min(lock(x) for x in xs)
    return s


def main():
    ap = argparse.ArgumentParser(description="Kronwerke progression checker (see the module docstring).")
    for arg in ("recipes", "mods", "stages", "--quests", "--goals", "--report", "--neoforge"):
        ap.add_argument(arg)
    ap.add_argument("--vanilla", default="/root/.gradle/caches/neoformruntime/artifacts/minecraft_1.21.1_client.jar")
    a = ap.parse_args()

    data, recipes, parser, failures = build(a)
    ck = Checker(data, recipes, load_locks(a.stages))
    ck.compute_raw()
    results = {S: ck.run(S) for S in STAGES}
    first = {}
    for S in reversed(STAGES):
        for n in results[S][1]:
            first[n] = S
    known = data.items | {n for r in recipes for n in r.outs}
    all_items = {n for n in known if not n.startswith(VIRTUAL) and "[" not in n}

    def usable_in(node, S):
        if node.startswith("#"):
            return bool(data.members("item", node[1:]) & results[S][1])
        return node in results[S][1]

    def name(n):
        return "%s (%s)" % (n, data.names[n]) if n in data.names else n

    out, summary = ["# Kronwerke progression check", ""], []

    # e. counts per stage
    out += ["## Counts per stage", "", "| Stage | Items reachable | Items locked | Locked items made by machines |",
            "| --- | --- | --- | --- |"]
    for S in STAGES:
        reached, usable, leaks = results[S]
        ok = len([n for n in usable if n in all_items])
        locked = len([i for i in all_items if ck.lock(i) > S])
        nleak = len([n for n in leaks if n in all_items])
        out.append("| %d | %d | %d | %d |" % (S, ok, locked, nleak))
        summary.append("stage %d: %d items reachable, %d locked, %d locked items made early" % (S, ok, locked, nleak))
    out.append("")

    # sanity targets and goal pillars
    checks = [(S, i, "sanity") for S, ids in SANITY.items() for i in ids]
    if a.goals and os.path.exists(a.goals):
        for g in json.load(open(a.goals)):
            m = re.search(r"(\d+)$", g.get("id", ""))
            for p in g.get("pillars", []) if m else []:
                checks += [(int(m.group(1)), it["item"], "goal %s %s" % (g["id"], p["id"]))
                           for it in p.get("items", [])]
    out += ["## Sanity targets and goal pillars", ""]
    for S, it, what in checks:
        ok = usable_in(it, S)
        out.append("- %s %s, stage %d: %s%s" % ("OK" if ok else "FAIL", what, S, name(it),
                                                "" if ok else ", first reachable: %s" % first.get(it, "never")))
        if not ok:
            summary.append("FAIL %s: %s not reachable in stage %d" % (what, it, S))
    failed = sum(not usable_in(i, S) for S, i, _ in checks)
    summary.append("sanity and goal checks: %d, failed: %d" % (len(checks), failed))
    out.append("")

    # c. quests
    if a.quests:
        qs = quest_checks(a.quests, ck.lock)
        bad = sorted({q for q in qs if not usable_in(q[1], q[2])}, key=lambda q: (q[2], q[0], q[1]))
        out += ["## Quest items not reachable in their stage", "",
                "%d task, reward and crate items checked, %d not reachable." % (len(qs), len(bad)), ""]
        out += ["- stage %d, %s: %s (first reachable: %s)%s" % (s, w, name(i), first.get(i, "never"),
                                                              "" if i in known else ", UNKNOWN ITEM, mod missing?")
                for w, i, s in bad] + [""]
        summary.append("quest items: %d checked, %d not reachable in their stage" % (len(qs), len(bad)))

    # a. unreachable open items, and b2. locked inputs that hold them back
    unreach = collections.defaultdict(lambda: collections.defaultdict(list))
    blockers, locked_by = collections.Counter(), collections.defaultdict(list)
    for it in sorted(all_items):
        s0 = ck.lock(it)
        if "creative" in it or it in ck.raw_stage or it not in ck.produced or first.get(it, 99) <= s0:
            continue
        r, miss = ck.why(it, s0, results[s0][1])
        miss = list(dict.fromkeys(miss))
        unreach[s0][it.split(":")[0]].append((it, r, miss))
        blockers.update(show(g) for g in miss)
        for g in miss:
            if g and min(ck.lock(x) for x in g) > s0:
                locked_by[(show(g), min(ck.lock(x) for x in g), s0)].append(it)
    never = sum(1 for m in unreach.values() for v in m.values() for x in v if x[0] not in first)
    total = sum(len(v) for m in unreach.values() for v in m.values())
    summary.append("open items not reachable in their stage: %d (%d never, %d only later)" % (
        total, never, total - never))
    out += ["## Most common missing pieces", "",
            "How often a node is missing in the best recipe of an item that is open but not reachable.", ""]
    out += ["- %d x %s" % (c, b) for b, c in blockers.most_common(40)] + [""]
    out += ["## Open items that are not reachable", "",
            "Open in the stage shown, made by some recipe, but no recipe fires in that stage. Each line shows the "
            "recipe with the fewest missing pieces. Items that are never reachable come first.", ""]
    for S in STAGES:
        if unreach[S]:
            out += ["### Stage %d" % S, ""]
        for mod in sorted(unreach[S]):
            rows = sorted(unreach[S][mod], key=lambda x: (x[0] in first, first.get(x[0], 9), x[0]))
            out += ["**%s** (%d)" % (mod, len(rows)), ""]
            out += ["- %s, first reachable %s; %s needs %s" % (
                name(it), first.get(it, "never"), r.id, "; ".join(show(g, ck.lock, S) for g in miss[:4]))
                for it, r, miss in rows] + [""]

    # b. leaks
    out += ["## Leaks: locked items that machines make before they open", ""]
    seen = set()
    for S in STAGES:
        for it, r in sorted(results[S][2].items()):
            if it in all_items and it not in seen:
                seen.add(it)
                out.append("- %s: locked until %d, made in stage %d by %s (%s)" % (
                    name(it), ck.lock(it), S, r.id, r.type))
    summary.append("leaks: %d locked items can be made before they open" % len(seen))
    out += ["", "## Locked inputs that hold back open items", "",
            "A locked node in the best recipe of items that are already open.", ""]
    for (g, until, s0), its in sorted(locked_by.items(), key=lambda kv: -len(kv[1])):
        out.append("- %s (locked until %d) blocks %d items open in stage %d: %s%s" % (
            g, until, len(its), s0, ", ".join(its[:8]), " ..." if len(its) > 8 else ""))
    out.append("")

    # d. recipe types without machine and parse problems
    types = collections.Counter(r.type for r in recipes)
    makes = {r.type for r in recipes if r.outs}
    unmapped = sorted(t for t in makes if t not in MACHINES and not is_crafting(t)
                      and t.split(":")[0] not in ("implicit", "extra"))
    unknown, same_id = [t for t in unmapped if t not in data.items], [t for t in unmapped if t in data.items]
    bad_ids = sorted({x for reqs in MACHINES.values() for q in reqs for x in q.split("|")
                      if x[0] != "#" and "*" not in x and x not in known}
                     | {x for e in EXTRA_RECIPES for q in e[0] + e[1] for x in q.split("|")
                        if not x.startswith(VIRTUAL) and x not in known})
    out += ["## Recipe types without a machine mapping", "", "Types that produce something; counted as needing "
            "nothing.", ""] + ["- %s (%d)" % (t, types[t]) for t in unknown]
    out += ["", "Not listed but need the item of the same id: " + ", ".join(same_id), "", "## Parse problems", ""]
    out += ["- id in MACHINES or EXTRA_RECIPES not found in any jar: %s" % m for m in bad_ids]
    out += ["- failed: %s" % f for f in failures]
    out += ["- %d recipes of type %s have no output" % (c, t)
            for t, c in collections.Counter(r.type for r in recipes if not r.outs).most_common()]
    out += ["- %d ingredients of type %s name no item (ignored)" % (c, t) for t, c in parser.opaque.most_common()]
    out += ["- tag with no members: %s (%d uses)" % (t, c) for t, c in parser.empty.most_common(40)] + [""]
    summary.append("recipes: %d of %d types; types without machine: %d (%d more use the item of the same id); "
                   "parse failures: %d" % (len(recipes), len(types), len(unknown), len(same_id), len(failures)))

    # 3. raw materials by mod
    raw_by_mod = collections.defaultdict(list)
    for n, s in ck.raw_stage.items():
        if n in data.items:
            raw_by_mod[mod_of(n)].append(n if s == 1 else "%s (stage %d)" % (n, s))
    out += ["## Raw materials by mod", "", "Items that no recipe makes, or known world drops. Review for items "
            "that should not be free.", ""]
    out += ["- **%s** (%d): %s" % (m, len(v), ", ".join(sorted(v))) for m, v in sorted(raw_by_mod.items())] + [""]

    if a.report:
        with open(a.report, "w", encoding="utf-8") as f:
            f.write("\n".join(out) + "\n")
    print("\n".join(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
