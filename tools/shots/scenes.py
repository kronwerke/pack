"""The scenes of the screenshot world, one entry per quest id in docs/SCREENSHOTS.md.

Each entry draws into a Cell (see build.py): x runs east, z south, y 0 is the first layer
above the floor, and the camera stands south of the cell. Multiblocks come from the mod's
own structure templates where it ships one (Immersive Engineering, Botania, NuclearCraft,
Create's test scenes), the rest is placed block by block. Whatever can only happen by hand
(forming with a hammer, opening a GUI, a fight) gets the parts and a chest with the tools,
and a note on the sign.
"""

SCENES = {}
FLOOR_Y = 63


class Spec:
    def __init__(self, fn, w, d):
        self.fn, self.w, self.d = fn, w, d


def scene(*keys, w=9, d=9):
    def deco(fn):
        for k in keys:
            SCENES[k] = Spec(fn, w, d)
        return fn
    return deco


def kit(*keys, blocks=(), items=(), mobs=(), note=None, w=9, d=9):
    """A quick scene: blocks on plinths in a row, a chest with items, mobs in front."""
    def fn(b):
        for i, bl in enumerate(blocks):
            x = 1 + (i % 4) * 2
            z = 2 + (i // 4) * 3
            b.b(x, 0, z, bl)
        if items:
            b.c(b.w - 1, 0, b.d - 1, list(items))
        for i, mob in enumerate(mobs):
            ent, nbt = (mob, "") if isinstance(mob, str) else mob
            b.m(ent, 2 + i * 3, 0, b.d - 3, nbt)
        if note:
            b.note(note)
    for k in keys:
        SCENES[k] = Spec(fn, w, d)


def auto(b, info):
    """No hand made scene: a small stage with the quest's task items, blocks standing on it,
    other items in glowing frames on a backdrop wall, mobs to kill standing in front."""
    import json
    import os
    cat = None
    p = os.environ.get("KW_CATALOG", "/tmp/claude-0/cat/catalog.json")
    if os.path.exists(p):
        cat = json.load(open(p))["blocks"]
    things = list(dict.fromkeys(info["items"] + ([info["icon"]] if info.get("icon") else [])))[:6]
    w = b.w
    # the stage: a raised deepslate platform with a gold trim, a backdrop wall behind it
    b.f(1, -1, 1, w - 2, -1, 4, "minecraft:polished_deepslate")
    b.f(1, 0, 1, w - 2, 3, 1, "minecraft:deepslate_tiles")
    b.f(1, 0, 1, w - 2, 0, 1, "minecraft:polished_blackstone")
    b.f(1, 3, 1, w - 2, 3, 1, "minecraft:polished_blackstone")
    b.b(1, 0, 4, "minecraft:lantern")
    b.b(w - 2, 0, 4, "minecraft:lantern")
    blocks = [t for t in things if cat is not None and t in cat]
    items = [t for t in things if t not in blocks]
    # blocks stand on the stage, spaced out
    start = max(2, (w - 2 * len(blocks)) // 2) if blocks else 2
    for i, bl in enumerate(blocks):
        b.b(start + i * 2, 0, 3, bl)
    # items hang in glow frames on the wall, centred
    fx = max(2, (w - 2 * len(items)) // 2) if items else 2
    for i, it in enumerate(items):
        x = min(w - 2, fx + i * 2)
        b.cmd(f"summon glow_item_frame {b.ox + x} {FLOOR_Y + 1 + 2} {b.oz + 2} {{Facing:3b,Fixed:1b,Tags:[\"kw_shot\"],Item:{{id:\"{it}\",count:1}}}}")
    for i, e in enumerate(info["kill"][:3]):
        b.m(e, 2 + i * 3, 0, 6)
    for d in info["dim"]:
        b.note("Aufnahme in " + d.split(":")[-1].replace("_", " "))


# ---- helpers ---------------------------------------------------------------------

def basin(b, x, y, z, fluid, wall="minecraft:glass"):
    """One fluid source block with a ring of wall around it and a floor under it, so nothing runs out."""
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            if dx or dz:
                b.b(x + dx, y, z + dz, wall)
    b.b(x, y - 1, z, wall)
    b.b(x, y, z, fluid)


def cobble_generator(b, x, y, z, wall="minecraft:glass"):
    """Water at x-1, lava at x+1, cobblestone between, all in glass; z is the row."""
    for dx in range(-2, 3):
        for dz in (-1, 1):
            b.b(x + dx, y, z + dz, wall)
    b.b(x - 2, y, z, wall)
    b.b(x + 2, y, z, wall)
    b.f(x - 2, y - 1, z - 1, x + 2, y - 1, z + 1, wall)
    b.b(x - 1, y, z, "minecraft:water")
    b.b(x, y, z, "minecraft:cobblestone")
    b.b(x + 1, y, z, "minecraft:lava")


def obelisk(b, cx, cz):
    """The whole obelisk build the way Core places it: core, stepped plinth, trunk with rune bands, cap, tip, crystal, four pedestals."""
    b.b(cx, 0, cz, "kronwerke:obelisk")
    for dx in range(-4, 5):
        for dz in range(-4, 5):
            r = max(abs(dx), abs(dz))
            if r > 0:
                b.b(cx + dx, 0, cz + dz, "kronwerke:obelisk_plinth")
            if r <= 3:
                b.b(cx + dx, 1, cz + dz, "kronwerke:obelisk_plinth")
            if r <= 2:
                b.b(cx + dx, 2, cz + dz, "kronwerke:obelisk_plinth")
            if r <= 1:
                for y in range(3, 15):
                    b.b(cx + dx, y, cz + dz, "kronwerke:obelisk_runes" if (y == 5 or y == 12) and r == 1 else "kronwerke:obelisk_trunk")
                b.b(cx + dx, 15, cz + dz, "kronwerke:obelisk_plinth")
    b.b(cx, 16, cz, "kronwerke:obelisk_shaft")
    b.b(cx, 17, cz, "kronwerke:obelisk_top")
    for dx, dz in ((-6, -6), (6, -6), (-6, 6), (6, 6)):
        b.b(cx + dx, 0, cz + dz, "kronwerke:obelisk_plinth")
        b.b(cx + dx, 1, cz + dz, "kronwerke:obelisk_pedestal")

def motor(b, x, y, z, facing="east", speed=64):
    b.b(x, y, z, f"create:creative_motor[facing={facing}]", f"{{ScrollValue:{speed}}}")


def gold_ring(b, cx, cz, r=2):
    for dx in range(-r, r + 1):
        for dz in range(-r, r + 1):
            if max(abs(dx), abs(dz)) == r:
                b.b(cx + dx, 0, cz + dz, "naturesaura:gold_powder")


# ===================================================================================
# Start

@scene("start_here/o_handin", "start_here/o_obelisk", w=15, d=15)
def _(b):
    obelisk(b, 7, 7)
    b.c(1, 0, 13, [("minecraft:cobblestone", 64)] * 6)


@scene("start_here/o_feeder", w=15, d=15)
def _(b):
    obelisk(b, 7, 7)
    b.b(7, 0, 12, "kronwerke:obelisk_intake")
    b.b(7, 1, 12, "minecraft:hopper[facing=down]")
    b.c(7, 2, 12, [("minecraft:cobblestone", 64)] * 3)


kit("start_here/s_locked", blocks=["minecraft:crafting_table"],
    items=["mekanism:steel_casing", "botania:terrasteel_ingot", "ae2:controller"],
    note="Gesperrte Items im Inventar zeigen, JEI offen")


@scene("start_here/m_goldleaf")
def _(b):
    b.f(3, 0, 3, 3, 4, 3, "minecraft:oak_log")
    b.f(1, 3, 1, 5, 4, 5, "naturesaura:golden_leaves")
    b.f(2, 5, 2, 4, 5, 4, "naturesaura:golden_leaves")
    b.b(3, 3, 3, "minecraft:oak_log")
    b.b(3, 4, 3, "minecraft:oak_log")


@scene("start_here/m_ritual")
def _(b):
    gold_ring(b, 4, 4, 2)
    for x, z in [(2, 2), (6, 2), (2, 6), (6, 6)]:
        b.b(x, 0, z, "naturesaura:wood_stand")
    b.b(4, 0, 4, "minecraft:oak_sapling")
    b.c(8, 0, 8, ["naturesaura:gold_leaf", "minecraft:oak_sapling", ("minecraft:stone", 4), ("minecraft:cobblestone", 2)])


kit("start_here/m_altar", blocks=["naturesaura:nature_altar"])
kit("start_here/m_gearbox", "start_here/m_keystone", blocks=["minecraft:crafting_table"],
    items=["create:gearbox", "kronwerke:obelisk"], note="Rezept in JEI zeigen")
kit("start_here/v_claim", blocks=["minecraft:lectern"], note="Karte mit M, Claim-Ansicht")


# ===================================================================================
# Erste Farmen

@scene("farms/cobble_drill", w=11)
def _(b):
    cobble_generator(b, 4, 0, 4)
    b.b(4, 0, 5, "minecraft:air")
    b.b(4, 0, 6, "create:mechanical_drill[facing=north]")
    b.b(4, 0, 7, "create:shaft[axis=z]")
    motor(b, 4, 0, 8, "north")
    b.b(5, 0, 6, "create:andesite_funnel[facing=north]")
    b.c(9, 0, 8, ["create:belt_connector"])


@scene("farms/wood_saw", w=11, d=11)
def _(b):
    for x, z in [(1, 5), (9, 5), (5, 1), (5, 9), (2, 2), (8, 2), (2, 8), (8, 8)]:
        b.b(x, 0, z, "minecraft:oak_sapling")
    b.b(5, 0, 5, "create:mechanical_bearing[facing=up]")
    b.b(5, -1, 5, "create:shaft[axis=y]")
    b.f(5, 1, 5, 9, 1, 5, "create:andesite_casing")
    b.b(9, 1, 6, "create:mechanical_saw[facing=south]")
    b.b(6, 1, 6, "minecraft:chest")
    b.b(6, 1, 4, "create:portable_storage_interface[facing=north]")
    b.c(10, 0, 10, ["create:super_glue", "create:portable_storage_interface"])
    b.note("Lager mit Motor drunter, Kleber setzen, Lager starten")


@scene("farms/crops_harvester", w=11, d=11)
def _(b):
    b.f(1, -1, 1, 9, -1, 9, "minecraft:farmland")
    b.f(1, 0, 1, 9, 0, 9, "minecraft:wheat[age=7]")
    b.b(5, -2, 5, "minecraft:stone")
    b.b(5, -1, 5, "minecraft:water")
    b.b(5, 0, 5, "create:mechanical_bearing[facing=up]")
    b.f(5, 1, 5, 8, 1, 5, "create:andesite_casing")
    b.b(6, 1, 6, "create:mechanical_harvester[facing=south]")
    b.b(8, 1, 6, "create:mechanical_harvester[facing=south]")
    b.b(7, 1, 4, "minecraft:chest")


@scene("farms/crops_essence")
def _(b):
    b.f(1, -1, 2, 7, -1, 4, "mysticalagriculture:inferium_farmland")
    b.f(1, 0, 2, 7, 0, 4, "mysticalagriculture:iron_crop[age=7]")
    b.f(1, -2, 2, 7, -2, 4, "mysticalagriculture:inferium_growth_accelerator")
    b.note("Seitlich anschneiden: Beschleuniger unter dem Acker")


@scene("farms/animals_thorn", w=11, d=11)
def _(b):
    for x in range(1, 10):
        b.b(x, 0, 1, "minecraft:oak_fence")
        b.b(x, 0, 9, "minecraft:oak_fence")
    for z in range(1, 10):
        b.b(1, 0, z, "minecraft:oak_fence")
        b.b(9, 0, z, "minecraft:oak_fence")
    b.f(2, -1, 2, 8, -1, 8, "minecraft:hopper")
    b.b(5, 0, 5, "botania:hopperhock")
    b.b(3, 0, 3, "farmingforblockheads:feeding_trough")
    b.b(7, 0, 7, "botania:mana_pool")
    for i, a in enumerate(["minecraft:cow", "minecraft:sheep", "minecraft:pig", "minecraft:chicken"]):
        b.m(a, 3 + i, 0, 6)
    b.c(10, 0, 10, ["botania:dreadthorne", ("minecraft:wheat", 32)])


@scene("farms/mobs_dark", w=9, d=9)
def _(b):
    b.f(0, 0, 0, 8, 6, 8, "minecraft:cobblestone")
    b.f(1, 5, 1, 7, 5, 7, "minecraft:air")
    b.f(4, 0, 4, 4, 4, 4, "minecraft:air")
    b.b(4, 0, 4, "minecraft:hopper")
    b.f(0, 0, 8, 8, 6, 8, "minecraft:glass")
    for x in (1, 7):
        b.b(x, 5, 4, "minecraft:oak_trapdoor[half=top,open=true,facing=east]")
    b.note("Querschnitt: Raum oben, Schacht in der Mitte (Original 22 Blöcke)")


@scene("farms/lava_seeds")
def _(b):
    b.f(1, -1, 2, 5, -1, 4, "mysticalagriculture:inferium_farmland")
    b.f(1, 0, 2, 5, 0, 4, "mysticalagriculture:fire_crop[age=7]")
    b.b(7, 0, 3, "create:item_drain")
    b.b(7, 0, 5, "create:fluid_tank")
    b.b(7, 1, 5, "create:fluid_tank")


@scene("farms/source_berries", w=11)
def _(b):
    b.f(1, 0, 2, 7, 0, 3, "ars_nouveau:sourceberry_bush[age=3]")
    b.b(4, 0, 5, "ars_nouveau:agronomic_sourcelink")
    b.b(6, 0, 5, "ars_nouveau:source_jar")
    b.b(8, 0, 5, "ars_nouveau:imbuement_chamber")
    b.m("ars_nouveau:starbuncle", 3, 0, 6)


@scene("farms/mana_endoflame", "botania/endo_auto", w=11)
def _(b):
    for x, z in [(3, 3), (5, 3), (3, 5), (5, 5)]:
        b.b(x, 0, z, "botania:endoflame")
    b.b(4, 0, 4, "botania:open_crate")
    b.b(4, 1, 4, "minecraft:hopper[facing=down]")
    b.c(4, 2, 4, [("minecraft:coal_block", 16)])
    b.b(4, -1, 4, "minecraft:stone_pressure_plate")
    b.b(8, 0, 4, "botania:mana_spreader")
    b.b(8, 0, 7, "botania:mana_pool")


@scene("farms/s2_xp")
def _(b):
    b.b(3, 0, 4, "create:fluid_tank")
    b.b(3, 1, 4, "create:fluid_tank")
    b.b(3, 2, 4, "create_enchantment_industry:experience_hatch")
    b.b(5, 0, 4, "create:millstone")
    b.c(7, 0, 7, ["create_enchantment_industry:grindstone_drain", "create_enchantment_industry:experience_hatch"])
    b.note("Schleifstein-Abfluss auf den Tank setzen")


# ===================================================================================
# Create

kit("create/welcome", blocks=["create:cogwheel[axis=y]"], note="W gedrückt halten über dem Zahnrad")


@scene("create/water_wheel", w=11)
def _(b):
    for i in range(4):
        b.b(2 + i, 1, 4, "create:water_wheel[facing=east]")
    b.f(1, 0, 3, 7, 0, 5, "minecraft:stone")
    # a trough of water above the wheels, closed on every side
    b.f(1, 3, 3, 6, 3, 5, "minecraft:stone")
    b.f(1, 4, 3, 6, 4, 5, "minecraft:stone")
    b.f(2, 4, 4, 5, 4, 4, "minecraft:water")
    b.b(6, 1, 4, "create:shaft[axis=x]")


@scene("create/windmill", w=17, d=9)
def _(b):
    b.f(8, 0, 6, 8, 4, 6, "create:andesite_casing")
    b.b(8, 5, 6, "create:windmill_bearing[facing=north]")
    # four arms of sails in front of the bearing
    b.f(8, 6, 5, 8, 11, 5, "create:white_sail[facing=north]")
    b.f(8, 0, 5, 8, 4, 5, "create:white_sail[facing=north]")
    b.f(9, 5, 5, 14, 5, 5, "create:white_sail[facing=north]")
    b.f(2, 5, 5, 7, 5, 5, "create:white_sail[facing=north]")
    b.note("Lager anklicken zum Starten (32 Segel im Original)")


@scene("create/stress", w=11)
def _(b):
    motor(b, 1, 0, 4, "east", 16)
    b.f(2, 0, 4, 8, 0, 4, "create:shaft[axis=x]")
    for x in (3, 5, 7):
        b.b(x, 0, 5, "create:millstone")
    b.c(10, 0, 8, ["create:goggles"])
    b.note("Brille auf, Netz ist überlastet")


@scene("create/depot")
def _(b):
    b.b(4, 0, 4, "create:depot")
    b.b(4, 2, 4, "create:mechanical_press[facing=east]")
    b.b(5, 2, 4, "create:shaft[axis=x]")
    motor(b, 6, 2, 4, "west")
    b.c(8, 0, 8, [("minecraft:iron_ingot", 32)])


@scene("create/mixer")
def _(b):
    b.b(4, 0, 4, "create:basin")
    b.b(4, 2, 4, "create:mechanical_mixer")
    b.b(5, 2, 4, "create:shaft[axis=x]")
    motor(b, 6, 2, 4, "west")


@scene("create/alloy_mixing", w=13)
def _(b):
    b.t("create:gametest/processing/brass_mixing", 1, 0, 1)
    b.note("Andesitlegierung: Andesit und Eisennugget ins Becken")
    b.c(12, 0, 8, [("minecraft:andesite", 64), ("minecraft:iron_nugget", 64)])


@scene("create/compacting")
def _(b):
    b.b(4, 0, 4, "create:basin")
    b.b(4, 2, 4, "create:mechanical_press[facing=east]")
    b.b(5, 2, 4, "create:shaft[axis=x]")
    motor(b, 6, 2, 4, "west")
    b.c(8, 0, 8, [("minecraft:flint", 32), ("minecraft:gravel", 32), ("minecraft:lava_bucket", 1)])


@scene("create/washing", w=11)
def _(b):
    b.t("create:gametest/processing/sand_washing", 1, 0, 1)


kit("create/belt", blocks=["create:shaft[axis=x]", "create:shaft[axis=x]"], items=["create:belt_connector"],
    note="Riemen zwischen die zwei Wellen ziehen")


@scene("create/frogport", w=13)
def _(b):
    b.b(2, 0, 4, "create:shaft[axis=y]")
    b.b(2, 1, 4, "create:chain_conveyor")
    b.b(10, 0, 4, "create:shaft[axis=y]")
    b.b(10, 1, 4, "create:chain_conveyor")
    b.b(4, 0, 6, "create:package_frogport")
    b.c(12, 0, 8, ["minecraft:chain", "create:package_frogport", "create:cardboard_block"])
    b.note("Kette zwischen den Förderern ziehen, Frosch anhängen")


@scene("create/stock_ticker")
def _(b):
    b.b(4, 0, 4, "create:stock_ticker[facing=south]")
    b.b(3, 0, 4, "create:red_seat")
    b.m("minecraft:villager", 3, 0, 4)
    b.b(5, 0, 4, "create:item_vault")


@scene("create/cobble_gen")
def _(b):
    cobble_generator(b, 4, 0, 4)
    b.b(4, 0, 5, "create:mechanical_drill[facing=north]")
    b.b(4, 0, 6, "create:shaft[axis=z]")
    motor(b, 4, 0, 7, "north")


@scene("create/tree_farm", w=13)
def _(b):
    for x in range(3, 11, 2):
        b.f(x, 0, 2, x, 3, 2, "minecraft:oak_log")
        b.f(x - 1, 3, 1, x + 1, 4, 3, "minecraft:oak_leaves[persistent=true]")
    b.f(2, 0, 4, 10, 0, 4, "create:radial_chassis[axis=x]")
    for x in range(3, 11, 2):
        b.b(x, 0, 3, "create:mechanical_saw[facing=north]")
    b.note("Lager oder Kolben davor, Kleber auf das Chassis")


@scene("create/factory", w=27, d=15)
def _(b):
    obelisk(b, 7, 7)
    b.b(7, 0, 12, "kronwerke:obelisk_intake")
    b.t("create:gametest/processing/brass_mixing", 15, 0, 2)


kit("create_brass/blaze_burner", blocks=["create:blaze_burner"], mobs=["minecraft:blaze"],
    note="Leeren Brenner auf die Lohe")


@scene("create_brass/brass_mixing", w=11)
def _(b):
    b.t("create:gametest/processing/brass_mixing_2", 1, 0, 1)


@scene("create_brass/incomplete", w=13)
def _(b):
    b.t("create:gametest/processing/precision_mechanism_crafting", 1, 0, 1)


@scene("create_brass/precision", w=13)
def _(b):
    b.t("create:gametest/processing/precision_mechanism_crafting", 1, 0, 1)
    b.note("Schleife: Riemen zurück zum Anfang")


@scene("create_brass/crafter", w=9)
def _(b):
    for x in range(3):
        for y in range(3):
            b.b(3 + x, y, 4, "create:mechanical_crafter[facing=south,pointing=" + ("right" if x < 2 else "down") + "]")


@scene("create_brass/crushing_wheel", w=11)
def _(b):
    b.t("create:gametest/processing/crushing_wheel_crafting", 1, 0, 1)


@scene("create_brass/blaze_cake", w=11)
def _(b):
    b.b(2, 0, 4, "create:basin")
    b.b(2, 2, 4, "create:mechanical_press[facing=east]")
    b.b(6, 0, 4, "create:depot")
    b.b(6, 2, 4, "create:spout")
    b.b(6, 3, 4, "create:fluid_tank")
    motor(b, 3, 2, 4, "west")


@scene("create_brass/boiler", w=11, d=11)
def _(b):
    b.f(3, 0, 3, 5, 2, 5, "create:fluid_tank")
    b.f(3, 0, 2, 5, 0, 2, "create:blaze_burner")
    for x, z in [(4, 2), (4, 6)]:
        b.b(x, 1, z, "create:steam_engine[face=wall,facing=" + ("north" if z == 2 else "south") + "]")
        b.b(x, 1, z - 1 if z == 2 else z + 1, "create:shaft[axis=z]")
    b.c(10, 0, 10, ["create:steam_engine", "create:steam_engine", "create:goggles", ("create:blaze_cake", 8)])
    b.note("Brenner unter den Tank, vier Motoren, Brille")


@scene("create_brass/arm")
def _(b):
    b.b(3, 0, 4, "create:mechanical_arm")
    b.b(5, 0, 4, "create:blaze_burner")
    b.c(1, 0, 4, [("minecraft:coal", 64)])
    b.note("Arm: Truhe als Eingang, Brenner als Ziel")


kit("create_brass/pg_winding", "create_brass/pg_generator", "create_brass/pg_rheostat", "create_brass/pg_magnet",
    blocks=["powergrid:generator_induction_rotor", "powergrid:generator_housing", "powergrid:rheostat", "powergrid:electromagnet"],
    items=["powergrid:copper_coil", "powergrid:wire_cutter"], note="Power Grid Teile, Lampe dran")


@scene("create_brass/alternator", w=11)
def _(b):
    b.b(2, 0, 4, "create:steam_engine[face=floor,facing=east]")
    b.f(3, 0, 4, 4, 0, 4, "create:shaft[axis=x]")
    b.b(5, 0, 4, "createaddition:alternator[facing=west]")
    b.b(5, 1, 4, "createaddition:connector")


@scene("create_trains/welcome", w=13)
def _(b):
    b.t("create:gametest/processing/track_crafting", 1, 0, 1)


@scene("create_trains/unprocessed_sheet")
def _(b):
    b.b(4, 0, 4, "create:depot")
    b.b(4, 2, 4, "create:spout")
    b.b(4, 3, 4, "create:creative_fluid_tank")
    b.c(8, 0, 8, [("create:powdered_obsidian", 16), ("minecraft:lava_bucket", 1)])


@scene("create_trains/station", "create_trains/first_train", "create_trains/drive", "create_trains/conductor",
       "create_trains/schedule", w=15)
def _(b):
    track(b, 4, 0, 14)
    b.b(7, 0, 5, "create:track_station")
    b.c(14, 0, 8, [("create:track", 32), "create:railway_casing", ("create:small_bogey", 1), "create:controls",
                    "create:schedule", "create:blaze_burner", ("create:andesite_casing", 16), "create:wrench"])
    b.note("Gleis entlang Z ziehen, Station im Montagemodus, Drehgestelle")


@scene("create_trains/junction", w=13)
def _(b):
    b.c(12, 0, 8, [("create:track", 64), ("create:track_signal", 4), "create:goggles"])
    b.note("Weiche legen, Ketten- und Einfahrtssignale")


@scene("create_trains/cargo")
def _(b):
    track(b, 4, 0, 8)
    b.b(4, 0, 6, "create:portable_storage_interface[facing=north]")
    b.b(4, 0, 7, "minecraft:chest")


@scene("create_trains/postbox")
def _(b):
    track(b, 3, 0, 8)
    b.b(4, 0, 4, "create:track_station")
    b.b(5, 0, 4, "create:white_postbox")


@scene("create_trains/obelisk_line", w=15, d=21)
def _(b):
    obelisk(b, 7, 7)
    b.b(7, 0, 12, "kronwerke:obelisk_intake")
    track(b, 17, 0, 14)
    b.b(7, 0, 16, "create:track_station")
    b.b(7, 0, 14, "create:portable_storage_interface[facing=north]")


# ===================================================================================
# Mekanism

def mek_row(b, machines, z=4, x0=1):
    for i, m in enumerate(machines):
        b.b(x0 + i, 0, z, m)


kit("mekanism/infuser", blocks=["mekanism:metallurgic_infuser"], items=[("minecraft:coal", 16), "create:electron_tube"],
    note="GUI offen mit Kohle-Balken")
kit("mekanism/configurator", blocks=["mekanism:enrichment_chamber"], items=["mekanism:configurator"],
    note="Seitenkonfiguration, Auto-Eject")


@scene("mekanism/dynamic_tank")
def _(b):
    b.f(3, 0, 3, 5, 2, 5, "mekanism:dynamic_tank")
    b.f(4, 1, 3, 4, 1, 5, "mekanism:structural_glass")
    b.f(3, 1, 4, 5, 1, 4, "mekanism:structural_glass")
    b.b(4, 1, 5, "mekanism:dynamic_valve")
    b.f(4, 1, 4, 4, 1, 4, "minecraft:air")


kit("mekanism/ethene", blocks=["mekanism:pressurized_reaction_chamber"],
    items=[("mekanism:substrate", 16), "mekanism:configurator"])


@scene("mekanism/ore_line", "mekanism_ores/line2", w=13)
def _(b):
    b.b(1, 0, 4, "minecraft:chest")
    mek_row(b, ["mekanism:enrichment_chamber", "mekanism:energized_smelter"], x0=3)
    b.b(6, 0, 4, "minecraft:chest")
    b.f(1, 1, 4, 6, 1, 4, "mekanism:basic_logistical_transporter")
    b.f(2, 0, 5, 5, 0, 5, "mekanism:basic_universal_cable")
    b.b(1, 0, 6, "mekanism:creative_energy_cube")


@scene("mekanism_ores/layout", "mekanism_ores/tripling", w=13)
def _(b):
    mek_row(b, ["mekanism:purification_chamber", "mekanism:crusher", "mekanism:enrichment_chamber",
                "mekanism:energized_smelter"], x0=2)
    b.b(2, 0, 6, "mekanism:electrolytic_separator")
    b.b(4, 0, 6, "mekanism:electric_pump")
    b.f(2, 1, 4, 5, 1, 4, "mekanism:basic_logistical_transporter")
    b.f(2, 0, 5, 5, 0, 5, "mekanism:basic_universal_cable")
    b.f(3, 0, 6, 3, 0, 6, "mekanism:basic_pressurized_tube")


@scene("mekanism_ores/shards", "mekanism_ores/quintupling", w=15)
def _(b):
    mek_row(b, ["mekanism:chemical_dissolution_chamber", "mekanism:chemical_washer", "mekanism:chemical_crystallizer",
                "mekanism:chemical_injection_chamber", "mekanism:purification_chamber", "mekanism:crusher",
                "mekanism:enrichment_chamber", "mekanism:energized_smelter"], x0=1)
    b.b(2, 0, 6, "mekanism:electrolytic_separator")
    b.b(4, 0, 6, "mekanism:electrolytic_separator")
    b.b(6, 0, 6, "mekanism:chemical_infuser")
    b.f(1, 0, 5, 8, 0, 5, "mekanism:basic_pressurized_tube")


kit("mekanism_ores/full", blocks=["mekanism:enrichment_chamber"],
    items=[("mekanism:upgrade_speed", 8), ("mekanism:upgrade_energy", 8)], note="GUI mit 8 und 8 Upgrades")
kit("mekanism_ores/foundry", blocks=["productivemetalworks:gray_foundry_controller", "productivemetalworks:gray_foundry_tank",
                                     "productivemetalworks:casting_table"],
    items=[("mekanism:raw_osmium", 16)], note="Gießerei formen, Erz hinein")


@scene("mekanism_advanced/teleporter")
def _(b):
    b.f(3, 0, 4, 5, 4, 4, "mekanism:teleporter_frame")
    b.f(4, 1, 4, 4, 3, 4, "minecraft:air")
    b.b(4, 0, 5, "mekanism:teleporter")
    b.b(3, 0, 5, "mekanism:creative_energy_cube")


kit("mekanism_advanced/miner", blocks=["mekanism:digital_miner"], note="GUI mit Filtern und Radius")


@scene("mekanism_advanced/evap", w=9)
def _(b):
    b.f(3, 0, 3, 6, 9, 6, "mekanism:thermal_evaporation_block")
    b.f(4, 1, 4, 5, 9, 5, "minecraft:air")
    b.f(4, 9, 3, 5, 9, 6, "mekanism:thermal_evaporation_block")
    b.b(4, 0, 6, "mekanism:thermal_evaporation_controller")
    b.b(5, 0, 6, "mekanism:thermal_evaporation_valve")
    b.f(4, 2, 6, 5, 8, 6, "mekanism:structural_glass")


@scene("mekanism_advanced/boiler", w=9)
def _(b):
    b.f(2, 0, 2, 6, 4, 6, "mekanism:boiler_casing")
    b.f(3, 1, 3, 5, 3, 5, "minecraft:air")
    b.f(3, 1, 3, 5, 1, 5, "mekanism:superheating_element")
    b.f(3, 2, 3, 5, 2, 5, "mekanism:pressure_disperser")
    b.f(2, 1, 6, 6, 3, 6, "mekanism:structural_glass")
    b.b(4, 0, 6, "mekanism:boiler_valve")
    b.note("Schnitt: Front aus Glas")


@scene("mekanism_advanced/turbine", w=9)
def _(b):
    b.f(2, 0, 2, 6, 8, 6, "mekanismgenerators:turbine_casing")
    b.f(3, 1, 3, 5, 7, 5, "minecraft:air")
    b.f(4, 1, 4, 4, 3, 4, "mekanismgenerators:turbine_rotor")
    b.b(4, 4, 4, "mekanismgenerators:rotational_complex")
    b.f(3, 4, 3, 5, 4, 5, "mekanism:pressure_disperser")
    b.b(4, 4, 4, "mekanismgenerators:rotational_complex")
    b.f(3, 5, 3, 5, 5, 5, "mekanismgenerators:electromagnetic_coil")
    b.b(4, 5, 4, "mekanismgenerators:saturating_condenser")
    b.f(2, 1, 6, 6, 7, 6, "mekanism:structural_glass")
    b.b(4, 0, 6, "mekanismgenerators:turbine_valve")
    b.c(8, 0, 8, [("mekanismgenerators:turbine_blade", 6)])
    b.note("Rotorblätter auf die Rotoren setzen")


kit("mekanism_advanced/cnc_stamper", blocks=["mekmm:cnc_stamper"], items=["ae2:silicon_press"])


@scene("mekanism_elite/induction_matrix", w=9)
def _(b):
    b.f(2, 0, 2, 6, 4, 6, "mekanism:induction_casing")
    b.f(3, 1, 3, 5, 3, 5, "mekanism:basic_induction_cell")
    b.b(4, 2, 4, "mekanism:basic_induction_provider")
    b.f(2, 1, 6, 6, 3, 6, "mekanism:structural_glass")
    b.b(4, 0, 6, "mekanism:induction_port")


kit("mekanism_elite/qio_dashboard", blocks=["mekanism:qio_dashboard", "mekanism:qio_drive_array"],
    items=["mekanism:qio_drive_base"])
kit("mekanism_elite/polonium", blocks=["nuclearcraft:irradiator", "mekanism:isotopic_centrifuge"],
    note="Bestrahlungskette NuclearCraft")


@scene("mekanism_elite/fusion", w=11, d=11)
def _(b):
    b.f(2, 0, 2, 6, 4, 6, "mekanismgenerators:fusion_reactor_frame")
    b.f(3, 1, 3, 5, 3, 5, "minecraft:air")
    b.b(4, 4, 4, "mekanismgenerators:fusion_reactor_controller")
    b.b(4, 2, 7, "mekanism:laser")
    b.b(4, 2, 9, "mekanism:laser_amplifier")


@scene("mekanism_elite/mekasuit")
def _(b):
    b.b(4, 0, 3, "mekanism:modification_station")
    b.stand(4, 0, 5, ["mekanism:mekasuit_helmet", "mekanism:mekasuit_bodyarmor", "mekanism:mekasuit_pants",
                      "mekanism:mekasuit_boots"], hand="mekanism:meka_tool")


@scene("antimatter/reactor", w=9)
def _(b):
    b.f(2, 0, 2, 6, 4, 6, "mekanismgenerators:fission_reactor_casing")
    b.f(3, 1, 3, 5, 3, 5, "minecraft:air")
    for x, z in [(3, 3), (5, 3), (3, 5), (5, 5)]:
        b.f(x, 1, z, x, 3, z, "mekanismgenerators:fission_fuel_assembly")
        b.b(x, 4, z, "mekanismgenerators:control_rod_assembly")
    b.f(2, 1, 6, 6, 3, 6, "mekanismgenerators:reactor_glass")
    b.b(4, 0, 6, "mekanismgenerators:fission_reactor_port")
    b.note("GUI mit Brennstäben und Steuerstäben")


@scene("antimatter/waste", w=11)
def _(b):
    for x in range(1, 10, 2):
        b.b(x, 0, 4, "mekanism:solar_neutron_activator")


@scene("antimatter/sps", w=11)
def _(b):
    b.f(1, 0, 1, 7, 6, 7, "mekanism:sps_casing")
    b.f(2, 1, 2, 6, 5, 6, "minecraft:air")
    b.b(4, 3, 4, "mekanism:supercharged_coil")
    b.b(4, 3, 7, "mekanism:sps_port")
    b.b(1, 3, 4, "mekanism:sps_port")
    b.note("Vereinfachte Hülle: im Spiel nach Buildguide vervollständigen")


@scene("antimatter/wind", d=9)
def _(b):
    b.b(4, 0, 4, "mekanismgenerators:wind_generator")


# ===================================================================================
# Ars Nouveau

@scene("ars_nouveau/imbuement", "ars_nouveau/first_gem")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:imbuement_chamber")
    b.b(2, 0, 4, "ars_nouveau:source_jar")
    b.c(8, 0, 8, [("minecraft:amethyst_shard", 16), ("ars_nouveau:source_gem", 4)])


@scene("ars_nouveau/fill_jar")
def _(b):
    b.b(3, 0, 4, "ars_nouveau:volcanic_sourcelink")
    b.b(5, 0, 4, "ars_nouveau:source_jar")
    b.b(7, 0, 4, "ars_nouveau:imbuement_chamber")
    b.f(1, 0, 6, 4, 0, 6, "minecraft:oak_log[axis=x]")


@scene("ars_nouveau/chamber_auto")
def _(b):
    b.b(4, 2, 4, "minecraft:hopper[facing=down]")
    b.b(4, 1, 4, "ars_nouveau:imbuement_chamber")
    b.b(4, 0, 4, "minecraft:hopper[facing=south]")
    b.b(4, 0, 5, "minecraft:chest")
    b.b(2, 1, 4, "ars_nouveau:source_jar")


kit("ars_nouveau/first_spell", blocks=["ars_nouveau:scribes_table"], items=["ars_nouveau:novice_spell_book"],
    note="Buch offen: Projectile und Break")
kit("ars_nouveau/scribes_table", blocks=["ars_nouveau:scribes_table"],
    items=["ars_nouveau:novice_spell_book", ("ars_nouveau:blank_parchment", 8)])


@scene("ars_nouveau/apparatus", "ars_master/charged_certus")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:arcane_core")
    b.b(4, 2, 4, "ars_nouveau:enchanting_apparatus")
    for x, z in [(2, 2), (6, 2), (2, 6), (6, 6), (4, 1), (4, 7)]:
        b.b(x, 0, z, "ars_nouveau:arcane_pedestal")
    b.b(1, 0, 4, "ars_nouveau:source_jar")


@scene("ars_nouveau/earth_essence")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:imbuement_chamber")
    for x, z in [(2, 4), (6, 4), (4, 6)]:
        b.b(x, 0, z, "ars_nouveau:arcane_pedestal")
    b.b(4, 0, 2, "ars_nouveau:source_jar")


@scene("ars_nouveau/starbuncle_work")
def _(b):
    b.b(2, 0, 4, "ars_nouveau:imbuement_chamber")
    b.b(6, 0, 4, "minecraft:chest")
    b.m("ars_nouveau:starbuncle", 4, 0, 5)
    b.c(8, 0, 8, ["ars_nouveau:dominion_wand"])


@scene("ars_nouveau/drygmy")
def _(b):
    for x, z in [(3, 3), (5, 3), (3, 5), (5, 5)]:
        b.b(x, 0, z, "minecraft:mossy_cobblestone")
    b.b(4, 0, 4, "ars_nouveau:drygmy_stone[converted=true]")
    b.b(6, 0, 6, "minecraft:chest")
    b.b(2, 0, 6, "ars_nouveau:source_jar")
    b.m("minecraft:cow", 7, 0, 3)


kit("ars_nouveau/mana", note="Mana-Leiste im HUD")


@scene("ars_apprentice/relay", w=21)
def _(b):
    b.b(1, 0, 4, "ars_nouveau:source_jar")
    b.b(2, 0, 4, "ars_nouveau:relay")
    b.b(18, 0, 4, "ars_nouveau:relay")
    b.b(19, 0, 4, "ars_nouveau:source_jar")


kit("ars_apprentice/collector", blocks=["ars_nouveau:relay_collector", "ars_nouveau:relay_deposit"],
    items=["ars_nouveau:dominion_wand"])


@scene("ars_apprentice/brazier", "ars_master/wilden_ritual", "ars_master/ritual_awakening", "ars_apprentice/ritual_scrying")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:ritual_brazier")
    b.c(8, 0, 8, ["ars_nouveau:ritual_scrying", "ars_nouveau:ritual_awakening", "ars_nouveau:wilden_spike",
                   "ars_nouveau:wilden_horn", "ars_nouveau:wilden_wing", ("ars_nouveau:source_gem", 8)])
    b.note("Tafel auf die Kohlenpfanne")


@scene("ars_apprentice/wixie", "ars_apprentice/potions")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:wixie_cauldron")
    b.b(2, 0, 4, "minecraft:chest")
    b.b(6, 0, 4, "minecraft:chest")
    b.b(4, 0, 6, "ars_nouveau:alchemical_sourcelink")
    b.b(2, 0, 2, "ars_nouveau:potion_jar")
    b.b(6, 0, 2, "ars_nouveau:potion_jar")


@scene("ars_apprentice/turret")
def _(b):
    cobble_generator(b, 4, 0, 4)
    b.b(4, 0, 5, "minecraft:air")
    b.b(4, 0, 6, "ars_nouveau:basic_spell_turret[facing=north]")


@scene("ars_apprentice/source_motor")
def _(b):
    b.b(3, 0, 4, "ars_technica:source_motor")
    b.b(3, 1, 4, "ars_nouveau:source_jar")
    b.f(4, 0, 4, 6, 0, 4, "create:shaft[axis=x]")
    b.b(7, 0, 4, "create:millstone")


kit("ars_master/tribute", "ars_epic/phases", mobs=["ars_nouveau:wilden_boss"], note="Chimäre steht still (NoAI)")


@scene("ars_master/golem_bookwyrm")
def _(b):
    b.f(1, 0, 1, 3, 2, 3, "minecraft:amethyst_block")
    b.b(2, 3, 2, "minecraft:budding_amethyst")
    b.m("ars_nouveau:amethyst_golem", 4, 0, 4)
    b.b(7, 0, 4, "ars_nouveau:storage_lectern")


kit("ars_master/alteration", blocks=["ars_nouveau:alteration_table"])
kit("ars_epic/breath", blocks=["minecraft:dragon_head"], items=[("minecraft:glass_bottle", 16)],
    note="Im End: Drachenatem abfüllen")
kit("ars_epic/linger", mobs=["minecraft:zombie", "minecraft:skeleton"], items=["ars_nouveau:novice_spell_book"],
    note="Linger-Zauber auf die Mobs")


@scene("ars_epic/elevator")
def _(b):
    b.c(8, 0, 8, ["ars_nouveau:novice_spell_book"])
    b.note("Slipstream-Aufzug im Spiel zaubern")


@scene("ars_epic/el_armor")
def _(b):
    for i, el in enumerate(["fire", "aqua", "earth", "air"]):
        b.stand(1 + i * 2, 0, 4, [f"ars_elemental:{el}_hat", f"ars_elemental:{el}_robes",
                                  f"ars_elemental:{el}_leggings", f"ars_elemental:{el}_boots"])


# ===================================================================================
# Botania

@scene("botania/pure_daisy", "alfheim/pure_essence")
def _(b):
    b.b(4, 0, 4, "botania:pure_daisy")
    for i, (x, z) in enumerate([(3, 3), (4, 3), (5, 3), (3, 4), (5, 4), (3, 5), (4, 5), (5, 5)]):
        b.b(x, 0, z, "botania:livingrock" if i % 2 else "minecraft:stone")
    b.f(6, -1, 6, 8, -1, 8, "minecraft:end_stone")


@scene("botania/pool", "botania/manastar", "botania/mana_void")
def _(b):
    b.b(4, 1, 4, "botania:mana_pool")
    b.b(4, 0, 4, "botania:mana_void")
    b.b(4, 1, 1, "botania:mana_spreader")
    b.b(6, 1, 4, "botania:manastar")
    b.b(2, 0, 4, "botania:endoflame")
    b.c(8, 0, 8, ["botania:wand_of_the_forest"])


@scene("botania/farm", w=13)
def _(b):
    for x in range(2, 11, 2):
        b.b(x, 0, 3, "botania:endoflame")
    b.b(4, 0, 6, "botania:mana_spreader")
    b.b(8, 0, 6, "botania:mana_spreader")
    b.b(6, 0, 8, "botania:mana_pool")
    b.b(6, 0, 2, "botania:open_crate")


@scene("botania/manasteel_prep", "botania_runes/ritual")
def _(b):
    gold_ring(b, 4, 4, 2)
    for x, z in [(2, 2), (6, 2), (2, 6), (6, 6)]:
        b.b(x, 0, z, "naturesaura:wood_stand")
    b.b(4, 0, 4, "minecraft:oak_sapling")


@scene("botania_runes/mana_pearl")
def _(b):
    b.b(4, 0, 4, "create:brass_casing")
    b.b(4, 1, 4, "botania:mana_pool")
    b.b(4, 1, 1, "botania:mana_spreader")


@scene("botania_runes/runic_altar")
def _(b):
    b.b(4, 0, 4, "botania:runic_altar")
    b.b(4, 0, 1, "botania:mana_spreader")
    b.b(4, 0, 7, "botania:mana_pool")
    b.c(8, 0, 8, ["botania:wand_of_the_forest", ("botania:manasteel_ingot", 4), ("botania:mana_powder", 4), "botania:livingrock"])


@scene("botania_runes/thermalily")
def _(b):
    b.b(4, 0, 4, "botania:thermalily")
    b.b(4, 2, 4, "create:hose_pulley[facing=south]")
    b.b(4, 0, 2, "botania:mana_spreader")


@scene("botania_runes/gourmaryllis", w=11)
def _(b):
    b.b(4, 0, 4, "botania:gourmaryllis")
    b.c(10, 0, 8, [("minecraft:bread", 16), ("minecraft:cooked_beef", 16), ("minecraft:baked_potato", 16),
                    ("farmersdelight:tomato", 16), "create:belt_connector"])
    b.note("Riemen über die Blume, verschiedene Essen")


@scene("botania_runes/plate_base", "botania_runes/terrasteel")
def _(b):
    b.t("botania:terra_plate", 2, 0, 2)
    b.c(8, 0, 8, [("botania:mana_spark", 4), ("botania:manasteel_ingot", 1), ("botania:mana_pearl", 1), ("botania:mana_diamond", 1)])


kit("botania_runes/baubles_rings", items=["botania:band_of_mana", "botania:band_of_aura", "botania:ring_of_magnetization"],
    note="Curios-Fenster mit Ringen")
kit("botania_runes/rune_core", blocks=["minecraft:crafting_table"], items=["botania:rune_of_mana"])


@scene("gaia/arena", "gaia/fight", w=13, d=13)
def _(b):
    b.t("botania:gaia_ritual", 1, 0, 1)
    b.c(12, 0, 12, ["botania:gaia_spirit", ("botania:terrasteel_ingot", 1)])
    b.note("Von oben: Leuchtfeuer mit vier Pylonen")


kit("gaia/tiara", items=["botania:flugel_tiara"], note="Fliegen mit Flugleiste")


@scene("gaia/dandelifeon", w=27, d=27)
def _(b):
    b.b(13, 0, 13, "botania:dandelifeon")
    b.f(1, -1, 1, 25, -1, 25, "minecraft:grass_block")
    import random
    r = random.Random(25)
    for x in range(1, 26):
        for z in range(1, 26):
            if (x, z) != (13, 13) and r.random() < 0.18:
                b.b(x, 0, z, "botania:cellular_block")


@scene("gaia/goal", w=15, d=15)
def _(b):
    obelisk(b, 7, 7)
    b.c(1, 0, 13, [("botania:gaia_spirit", 64)])


@scene("alfheim/frame", "alfheim/open", "alfheim/elementium_line", w=13, d=11)
def _(b):
    b.t("botania:alfheim_portal", 3, 0, 3)
    b.b(1, 0, 8, "botania:mana_pool")
    b.b(10, 0, 8, "botania:mana_pool")
    b.b(1, 1, 8, "botania:natura_pylon")
    b.b(10, 1, 8, "botania:natura_pylon")
    b.c(12, 0, 10, ["botania:wand_of_the_forest", ("botania:manasteel_block", 8), ("botania:livingwood", 8)])


kit("alfheim/corporea_index", blocks=["botania:corporea_index"], items=[("botania:corporea_spark", 2)])
kit("alfheim/elementium_armor", mobs=["minecraft:zombie"], items=["botania:elementium_chestplate"],
    note="Elementium-Rüstung an, Mob angreifen lassen")


# ===================================================================================
# Occultism and Hexerei

@scene("occultism/spirit_fire")
def _(b):
    b.b(4, -1, 4, "minecraft:netherrack")
    b.b(4, 0, 4, "occultism:spirit_fire")
    b.c(8, 0, 8, [("minecraft:andesite", 32)])


def pentacle(b):
    b.b(4, 0, 4, "occultism:golden_sacrificial_bowl")
    for x in range(1, 8):
        for z in range(1, 8):
            if (x, z) != (4, 4) and (abs(x - 4) == 3 or abs(z - 4) == 3 or (x == z or x + z == 8)):
                b.b(x, 0, z, "occultism:chalk_glyph_white")
    for x, z in [(1, 1), (7, 1), (1, 7), (7, 7)]:
        b.b(x, 0, z, "occultism:sacrificial_bowl")
    for x, z in [(4, 0), (0, 4), (8, 4), (4, 8)]:
        b.b(x, 0, z, "occultism:large_candle_white")


@scene("occultism/aviar", "occultism/hedyrin", "occultism/ophyx", "occultism/strigeor", "occultism/satchel",
       "occultism_afrit/kandar", "occultism_afrit/marid_crusher")
def _(b):
    pentacle(b)
    b.note("Kreideglyphen sind Platzhalter: im Buch das Pentakel ansehen")


kit("occultism/foliot_crusher", mobs=["occultism:foliot"], items=[("occultism:iron_dust", 32)])
kit("occultism/foliot_janitor", blocks=["minecraft:chest", "minecraft:chest"], mobs=["occultism:foliot", "occultism:foliot"])
kit("occultism/djinni_familiars", mobs=["occultism:greedy_familiar", "occultism:beholder_familiar"])
kit("occultism_afrit/iesnium", blocks=["occultism:iesnium_ore", "minecraft:netherrack"], items=["occultism:divination_rod"],
    note="Im Nether aufnehmen")
kit("occultism_afrit/unbound_afrit", mobs=["occultism:afrit_wild"])


@scene("occultism_afrit/mineshaft")
def _(b):
    b.b(4, 1, 4, "occultism:dimensional_mineshaft")
    b.b(4, 0, 4, "minecraft:hopper")
    b.b(5, 0, 4, "minecraft:chest")


@scene("occultism_afrit/storage")
def _(b):
    b.b(4, 0, 4, "occultism:storage_controller")
    for x, z in [(4, 1), (4, 7), (1, 4), (7, 4)]:
        b.b(x, 0, z, "occultism:storage_stabilizer_tier1")


kit("occultism_afrit/reinforced_deepslate", blocks=["minecraft:crafting_table", "minecraft:reinforced_deepslate"])


@scene("hexerei/herbs")
def _(b):
    b.f(1, -1, 2, 7, -1, 5, "minecraft:farmland")
    for x, plant in zip([1, 3], ["mandrake_plant", "belladonna_plant"]):
        b.f(x, 0, 2, x, 0, 5, f"hexerei:{plant}[age=3]")
    for x, bush in zip([5, 7], ["mugwort_bush", "yellow_dock_bush"]):
        b.f(x, 0, 2, x, 0, 5, f"hexerei:{bush}[age=3,half=lower]")
        b.f(x, 1, 2, x, 1, 5, f"hexerei:{bush}[age=3,half=upper]")


@scene("hexerei/cauldron", "hexerei/blood", "hexerei/potion_brew")
def _(b):
    basin(b, 2, -1, 4, "minecraft:lava", "minecraft:stone_bricks")
    b.b(2, 0, 4, "hexerei:mixing_cauldron")
    b.b(6, 0, 4, "hexerei:mixing_cauldron")
    b.b(4, 0, 2, "hexerei:candle_dipper")


kit("hexerei/candles", blocks=["hexerei:candle_dipper", "hexerei:mixing_cauldron"], items=[("hexerei:tallow_impurity", 16)])
kit("hexerei/sage_plate", blocks=["hexerei:sage_burning_plate"], items=[("hexerei:dried_sage_bundle", 4)])
kit("hexerei/willow_broom", items=["hexerei:willow_broom"], note="Auf dem Besen fliegen")
kit("hexerei/crow", mobs=["hexerei:crow"], items=["hexerei:crow_flute"])


@scene("hexerei/witch_house", w=21, d=21)
def _(b):
    b.t("hexerei:coven/dark_coven/houses/witch_house_1", 1, 0, 1)


# ===================================================================================
# Immersive Engineering and Industrial Foregoing

IE = "immersiveengineering:multiblocks/"


def ie(keys, template, w=9, d=9, note="Mit dem Hammer formen"):
    def fn(b):
        b.t(IE + template, 1, 0, 1)
        b.c(b.w - 1, 0, b.d - 1, ["immersiveengineering:hammer", "immersiveengineering:manual"])
        b.note(note)
    for k in keys:
        SCENES[k] = Spec(fn, w, d)


kit("immersive/welcome", items=["immersiveengineering:manual"], note="Handbuch auf einer Multiblock-Seite")
ie(["immersive/hammer", "immersive/coke_oven", "immersive/creosote", "immersive/treated_wood"], "coke_oven")
ie(["immersive/blast_furnace"], "blast_furnace")
ie(["immersive/improved_form"], "improved_blast_furnace")
ie(["immersive/kiln"], "alloy_smelter")
kit("immersive/pump", blocks=["immersiveengineering:fluid_pump", "immersiveengineering:fluid_pipe"])
kit("immersive/bench", blocks=["immersiveengineering:workbench"], items=["immersiveengineering:blueprint"])
kit("immersive/cloche", blocks=["immersiveengineering:cloche"], items=[("immersiveengineering:seed", 4)])


@scene("immersive/dynamo", "immersive/windmill", w=11)
def _(b):
    b.f(4, 0, 4, 4, 5, 4, "immersiveengineering:treated_wood_horizontal")
    b.b(4, 6, 4, "immersiveengineering:dynamo")
    b.b(4, 6, 3, "immersiveengineering:windmill")
    b.note("Windrad vor den Dynamo")


@scene("immersive/watermill", w=13)
def _(b):
    # a channel of water: stone on both sides and under it
    b.f(0, 0, 3, 11, 0, 3, "minecraft:stone")
    b.f(0, 0, 5, 11, 0, 5, "minecraft:stone")
    b.f(0, -1, 3, 11, -1, 5, "minecraft:stone")
    b.b(0, 0, 4, "minecraft:stone")
    b.b(11, 0, 4, "minecraft:stone")
    b.f(1, 0, 4, 10, 0, 4, "minecraft:water")
    for x in (3, 6, 9):
        b.b(x, 2, 4, "immersiveengineering:watermill")
    b.b(11, 2, 4, "immersiveengineering:dynamo")


@scene("immersive/connectors", "immersive/capacitor", "immersive/thermoelectric", "immersive/transformer", w=13)
def _(b):
    for x in (1, 6):
        b.f(x, 0, 3, x, 2, 3, "immersiveengineering:treated_post")
        b.b(x, 3, 3, "immersiveengineering:connector_lv")
    b.b(9, 0, 3, "immersiveengineering:capacitor_lv")
    b.b(9, 0, 6, "minecraft:magma_block")
    b.b(10, 0, 6, "immersiveengineering:thermoelectric_generator")
    b.b(11, 0, 6, "minecraft:blue_ice")
    b.b(4, 0, 6, "immersiveengineering:transformer")
    b.c(12, 0, 8, [("immersiveengineering:wirecoil_copper", 8), ("immersiveengineering:wirecoil_electrum", 8)])


ie(["immersive/tank"], "sheetmetal_tank")
ie(["immersive/silo"], "silo", w=9, d=9)
ie(["immersive/shelf"], "shelf")


@scene("immersive/list_mb", w=40, d=9)
def _(b):
    for i, t in enumerate(["coke_oven", "blast_furnace", "alloy_smelter", "improved_blast_furnace", "sheetmetal_tank",
                           "silo", "shelf"]):
        b.t(IE + t, 1 + i * 5, 0, 1)


kit("immersive_heavy/light", "immersive_heavy/heavy", blocks=["minecraft:crafting_table"],
    items=["immersiveengineering:light_engineering", "immersiveengineering:heavy_engineering"])
for name, tpl, w, d in [("crusher", "crusher", 9, 9), ("press", "metal_press", 9, 9), ("squeezer", "squeezer", 9, 9),
                        ("fermenter", "fermenter", 9, 9), ("mixer", "mixer", 9, 9), ("bottling", "bottling_machine", 9, 9),
                        ("arc", "arcfurnace", 11, 11), ("refinery", "refinery", 11, 9), ("diesel", "diesel_generator", 11, 9),
                        ("sawmill", "sawmill", 11, 9), ("assembler", "assembler", 9, 9), ("auto_workbench", "auto_workbench", 9, 9),
                        ("excavator", "excavator", 13, 11), ("lightning_rod", "lightning_rod", 9, 9),
                        ("radio_tower", "radio_tower", 9, 9)]:
    ie([f"immersive_heavy/{name}"], tpl, w, d)
kit("immersive_heavy/resonanz", blocks=["immersiveengineering:tesla_coil"])


@scene("immersive_heavy/hv", w=15)
def _(b):
    for x in (1, 12):
        b.f(x, 0, 4, x, 3, 4, "immersiveengineering:steel_post")
        b.b(x, 4, 4, "immersiveengineering:connector_hv")
    b.c(14, 0, 8, [("immersiveengineering:wirecoil_steel", 8)])


ie(["immersive_heavy/duroplast"], "bottling_machine")
kit("immersive_heavy/survey", items=["immersiveengineering:coresample"], note="Kernprobe auf den Boden legen")


@scene("immersive_heavy/list_big", w=40, d=13)
def _(b):
    for i, t in enumerate(["crusher", "metal_press", "arcfurnace", "excavator"]):
        b.t(IE + t, 1 + i * 10, 0, 1)


kit("industrial/welcome", "industrial/frame_simple", "industrial/frame_adv", "industrial/frame_supreme",
    blocks=["minecraft:crafting_table"],
    items=["industrialforegoing:machine_frame_pity", "industrialforegoing:machine_frame_simple",
           "industrialforegoing:machine_frame_advanced", "industrialforegoing:machine_frame_supreme"])


@scene("industrial/extractor", "industrial/latex_unit", "industrial/plastic")
def _(b):
    b.f(4, 0, 4, 4, 4, 4, "minecraft:oak_log")
    for y in range(0, 4):
        b.b(3, y, 4, "industrialforegoing:fluid_extractor[subfacing=east]")
    b.b(6, 0, 4, "industrialforegoing:latex_processing_unit")
    b.b(7, 0, 6, "minecraft:furnace")


kit("industrial/dissolution", blocks=["industrialforegoing:dissolution_chamber"])
kit("industrial/addons", blocks=["industrialforegoing:plant_sower"],
    items=["industrialforegoing:speed_addon_tier_1", "industrialforegoing:efficiency_addon_tier_1"])


@scene("industrial/sower", "industrial/gatherer")
def _(b):
    b.f(1, -1, 1, 7, -1, 7, "minecraft:farmland")
    b.f(1, 0, 1, 7, 0, 7, "minecraft:wheat[age=7]")
    b.b(4, 0, 4, "industrialforegoing:plant_sower")
    b.b(4, 1, 4, "industrialforegoing:plant_gatherer")


kit("industrial/bio", blocks=["industrialforegoing:bioreactor", "industrialforegoing:biofuel_generator"])
kit("industrial/slaughter", blocks=["industrialforegoing:mob_slaughter_factory"], mobs=["minecraft:cow", "minecraft:pig"])
kit("industrial/crusher", blocks=["industrialforegoing:mob_crusher"], mobs=["minecraft:zombie"])
kit("industrial/duplicator", blocks=["industrialforegoing:mob_duplicator"])


@scene("industrial/laser", "industrial/lens", w=11, d=11)
def _(b):
    b.b(5, 0, 5, "industrialforegoing:ore_laser_base")
    for x, z in [(3, 3), (7, 3), (3, 7), (7, 7)]:
        b.b(x, 0, z, "industrialforegoing:laser_drill")
    b.c(10, 0, 10, ["industrialforegoing:white_laser_lens", "industrialforegoing:blue_laser_lens"])


@scene("industrial/fluid_laser", w=11, d=11)
def _(b):
    b.b(5, 0, 5, "industrialforegoing:fluid_laser_base")
    for x, z in [(3, 3), (7, 3), (3, 7), (7, 7)]:
        b.b(x, 0, z, "industrialforegoing:laser_drill")
    b.b(5, 0, 8, "minecraft:soul_sand")
    b.b(5, 1, 8, "minecraft:soul_sand")
    b.b(5, 2, 8, "minecraft:wither_skeleton_skull[rotation=0]")
    b.note("Wither dort selbst beschwören, dann Laser drauf")


kit("industrial/washing", blocks=["industrialforegoing:washing_factory", "industrialforegoing:fermentation_station",
                                  "industrialforegoing:fluid_sieving_machine"])


@scene("industrial/conveyor", "industrial/transporters", w=11)
def _(b):
    b.f(1, 0, 4, 9, 0, 4, "industrialforegoing:conveyor[facing=east]")
    b.c(10, 0, 8, ["industrialforegoing:conveyor_insertion_upgrade", "industrialforegoing:conveyor_extraction_upgrade",
                    "industrialforegoing:conveyor_detection_upgrade"])


# ===================================================================================
# Oritech, Powah, Ender IO (auto from the quest items, a few by hand)

@scene("oritech/atomic_forge", w=9)
def _(b):
    b.b(4, 0, 4, "oritech:atomic_forge_block")
    for x, z in [(3, 3), (4, 3), (5, 3), (3, 4), (5, 4), (3, 5), (4, 5), (5, 5)]:
        b.b(x, 0, z, "oritech:machine_core_2")
    b.b(4, 0, 7, "oritech:laser_arm_block")


@scene("powah/reactor", w=9)
def _(b):
    b.f(3, 0, 3, 5, 3, 5, "powah:reactor_starter")
    b.note("Ein Starter setzen baut den Reaktor; hier gefüllt als Platzhalter")


@scene("enderio/conduits", w=9)
def _(b):
    b.b(1, 0, 4, "enderio:stirling_generator")
    b.c(8, 0, 8, [("enderio:conduit", 32)])
    b.note("Leitungen zur Maschine legen")


# ===================================================================================
# AE2

@scene("ae2/channels", "ae2/controller", "ae2/network", w=13)
def _(b):
    b.f(1, 0, 4, 2, 1, 5, "ae2:controller")
    b.c(12, 0, 8, [("ae2:fluix_covered_dense_cable", 16), ("ae2:fluix_smart_cable", 32), ("ae2:drive", 2), "ae2:terminal"])
    b.note("Dichte Kabel vom Controller, dann Smart-Kabel mit Kanalstreifen")


@scene("ae2/cpu", w=9)
def _(b):
    b.f(3, 0, 3, 5, 2, 5, "ae2:crafting_unit")
    b.b(4, 1, 5, "ae2:crafting_accelerator")
    b.b(3, 0, 5, "ae2:1k_crafting_storage")


@scene("ae2/meteorite", w=11, d=11)
def _(b):
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(0, 5):
                if (x - 5) ** 2 + (z - 5) ** 2 + (y - 2) ** 2 <= 9:
                    b.b(x, y, z, "ae2:sky_stone_block")
    b.b(5, 2, 5, "ae2:mysterious_cube")


@scene("ae2_advanced/spatial", w=11)
def _(b):
    b.f(2, 0, 2, 8, 0, 2, "ae2:spatial_pylon")
    b.f(2, 0, 2, 2, 6, 2, "ae2:spatial_pylon")
    b.f(2, 6, 2, 8, 6, 2, "ae2:spatial_pylon")
    b.b(5, 0, 6, "ae2:spatial_io_port")


@scene("ae2_advanced/matrix", w=9)
def _(b):
    b.f(2, 0, 2, 6, 4, 6, "extendedae:assembler_matrix_wall")
    b.note("Assembler-Matrix: Hülle, innen Muster und Kerne")


# ===================================================================================
# Power, flux and new tech

@scene("flux_networks/dust", w=9)
def _(b):
    b.b(4, 0, 4, "minecraft:bedrock")
    b.b(4, 2, 4, "minecraft:obsidian")
    b.c(8, 0, 8, [("minecraft:redstone", 64)])
    b.note("Redstone in die Lücke, Obsidian anklicken")


@scene("flux_networks/first_link", "flux_networks/sides", "flux_networks/wireless", "flux_networks/stats",
       "flux_networks/setup_mek", "flux_networks/whole_base", w=13)
def _(b):
    b.b(2, 0, 4, "mekanism:creative_energy_cube")
    b.b(3, 0, 4, "fluxnetworks:flux_plug")
    b.b(9, 0, 4, "fluxnetworks:flux_point")
    b.b(10, 0, 4, "mekanism:enrichment_chamber")
    b.c(12, 0, 8, ["fluxnetworks:flux_configurator", "fluxnetworks:flux_controller"])


@scene("flux_networks/setup_reactor", w=9)
def _(b):
    b.f(3, 0, 3, 5, 3, 5, "powah:reactor_starter")
    b.b(6, 0, 4, "fluxnetworks:flux_plug")


@scene("list_power/steam_engine", w=11)
def _(b):
    b.t("create:gametest/fluids/steam_engine", 1, 0, 1)


# ===================================================================================
# Dimensions: portals and the arrival, the rest is shot in the dimension itself

@scene("nether/welcome")
def _(b):
    b.f(3, 0, 4, 6, 4, 4, "minecraft:obsidian")
    b.f(4, 1, 4, 5, 3, 4, "minecraft:nether_portal[axis=x]")


@scene("nether/blaze_burner")
def _(b):
    b.m("minecraft:blaze", 4, 1, 4)
    b.c(8, 0, 8, ["create:blaze_burner"])


@scene("the_end/egg", "the_end/respawn")
def _(b):
    b.f(2, 0, 2, 6, 0, 6, "minecraft:bedrock")
    b.b(4, 1, 4, "minecraft:dragon_egg")
    for x, z in [(4, 1), (4, 7), (1, 4), (7, 4)]:
        b.b(x, 0, z, "minecraft:obsidian")
        b.b(x, 1, z, "minecraft:bedrock")
        b.m("minecraft:end_crystal", x, 2, z, "ShowBottom:0b", ai=True)


kit("the_end/elytra", items=["minecraft:elytra"], note="Mit Elytra fliegen")


@scene("aether/portal")
def _(b):
    b.f(3, 0, 4, 6, 4, 4, "minecraft:glowstone")
    b.f(4, 1, 4, 5, 3, 4, "aether:aether_portal[axis=x]")


kit("aether/altar", "aether/freezer", "aether/incubator", blocks=["aether:altar", "aether:freezer", "aether:incubator"])


@scene("deeper_darker/portal", w=11)
def _(b):
    b.f(1, 0, 4, 8, 6, 4, "minecraft:reinforced_deepslate")
    b.f(2, 1, 4, 7, 5, 4, "deeperdarker:otherside_portal[axis=x]")


@scene("eternal_starlight/portal", w=11, d=11)
def _(b):
    b.t("eternal_starlight:portal_ruins/common", 1, 0, 1)


@scene("productive_trees/mega", w=15, d=15)
def _(b):
    b.t("productivetrees:brown_amber_mega_1", 1, 0, 1)


@scene("productive_trees/time_traveller", w=13, d=13)
def _(b):
    b.t("productivetrees:time_traveller_1", 1, 0, 1)


# ===================================================================================
# Late game

@scene("draconic/injectors", "draconic/tiers", w=11, d=11)
def _(b):
    b.b(5, 0, 5, "draconicevolution:crafting_core")
    for x, z in [(5, 1), (5, 9), (1, 5), (9, 5), (2, 2), (8, 8)]:
        b.b(x, 0, z, "draconicevolution:basic_crafting_injector")


@scene("draconic/stabilizer", "list_power/draconic_core", w=15, d=15)
def _(b):
    b.b(7, 2, 7, "draconicevolution:energy_core")
    for x, z in [(7, 1), (7, 13), (1, 7), (13, 7)]:
        b.b(x, 2, z, "draconicevolution:energy_core_stabilizer")
    b.c(14, 0, 14, [("draconicevolution:draconium_block", 16), ("minecraft:redstone_block", 16)])
    b.note("Build Guide im Kern zeigt die Hülle")


@scene("draconic_chaos/reactor", w=15, d=15)
def _(b):
    b.b(7, 2, 7, "draconicevolution:reactor_core")
    for x, z in [(7, 2), (7, 12), (2, 7), (12, 7)]:
        b.b(x, 2, z, "draconicevolution:reactor_stabilizer")
    b.b(7, 7, 7, "draconicevolution:reactor_injector")


@scene("nuclearcraft/reactor", w=11, d=11)
def _(b):
    b.f(2, 0, 2, 8, 6, 8, "nuclearcraft:fission_reactor_casing")
    b.f(3, 1, 3, 7, 5, 7, "nuclearcraft:graphite_block")
    for x in (4, 6):
        for z in (4, 6):
            b.f(x, 1, z, x, 5, z, "nuclearcraft:fission_reactor_solid_fuel_cell")
    b.f(3, 1, 8, 7, 5, 8, "nuclearcraft:fission_reactor_glass")
    b.b(5, 0, 8, "nuclearcraft:fission_reactor_controller[facing=south]")
    b.b(2, 3, 5, "nuclearcraft:fission_reactor_port")


@scene("finale/fight_info", "finale/f_crystals", "draconic_chaos/guardian")
def _(b):
    b.note("Im Chaos-Turm aufnehmen: Kristalle, Wächter")


@scene("food/f_feast")
def _(b):
    b.f(2, 0, 3, 6, 0, 5, "minecraft:oak_planks")
    b.b(3, 1, 4, "farmersdelight:roast_chicken_block")
    b.b(5, 1, 4, "farmersdelight:shepherds_pie_block")
    b.c(8, 0, 8, [("minecraft:bowl", 8)])


@scene("malum/healing_rite", "malum/quickening")
def _(b):
    b.b(4, 0, 4, "malum:runewood_totem_base")
    b.f(4, 1, 4, 4, 3, 4, "malum:runewood_log")
    b.c(8, 0, 8, ["malum:totemic_staff", ("malum:arcane_spirit", 4), ("malum:sacred_spirit", 8)])


@scene("malum/altar", "malum/spirits")
def _(b):
    b.b(4, 0, 4, "malum:spirit_altar")
    for x, z in [(2, 2), (6, 2), (2, 6), (6, 6)]:
        b.b(x, 0, z, "malum:runewood_item_pedestal")
    b.c(8, 0, 8, [("malum:sacred_spirit", 16), ("malum:arcane_spirit", 16)])


@scene("eidolon/altar", "eidolon/prayer", "eidolon/stone_altar")
def _(b):
    b.f(3, 0, 4, 5, 0, 4, "eidolon_repraised:stone_altar")
    b.b(4, 1, 4, "eidolon_repraised:goblet")
    b.b(3, 1, 4, "minecraft:candle[lit=true]")
    b.b(5, 1, 4, "minecraft:candle[lit=true]")


kit("eidolon/brazier", blocks=["eidolon_repraised:brazier"])
kit("eidolon/crucible", blocks=["eidolon_repraised:crucible"])


@scene("theurgy/array")
def _(b):
    b.b(4, 0, 4, "theurgy:incubator")
    for x, z in [(4, 2), (2, 4), (6, 4), (4, 6)]:
        b.b(x, 0, z, "theurgy:incubator_mercury_vessel")


@scene("silent_gear/stone_anvil", "silent_gear/pickaxe", "silent_gear/repair_kit")
def _(b):
    b.b(4, 0, 4, "silentgear:stone_anvil")
    b.b(6, 0, 4, "silentgear:starlight_charger")
    b.c(8, 0, 8, [("silentgear:pickaxe_blueprint", 1), ("minecraft:flint", 16), ("minecraft:stick", 8)])


@scene("list_gear/mek_jetpack", "list_gear/mekasuit", "list_gear/wyvern", "list_gear/sg_end", "list_gear/drilling")
def _(b):
    b.stand(2, 0, 4, [None, "mekanism:jetpack"])
    b.stand(4, 0, 4, ["mekanism:mekasuit_helmet", "mekanism:mekasuit_bodyarmor", "mekanism:mekasuit_pants",
                      "mekanism:mekasuit_boots"])
    b.stand(6, 0, 4, [None, "draconicevolution:wyvern_chestpiece"], hand="draconicevolution:wyvern_pickaxe")


@scene("refined_storage")
def _(b):
    b.b(1, 0, 4, "refinedstorage:controller")
    b.f(2, 0, 4, 6, 0, 4, "refinedstorage:cable")
    b.b(3, 0, 3, "refinedstorage:disk_drive")
    b.b(5, 0, 5, "refinedstorage:grid[direction=south]")
    b.b(7, 0, 4, "refinedstorage:autocrafter[direction=south]")
    b.b(1, 0, 5, "mekanism:creative_energy_cube")


def track(b, z, x0, x1):
    """A straight east-west line of Create track on gravel."""
    b.f(x0, -1, z, x1, -1, z, "minecraft:gravel")
    b.f(x0, 0, z, x1, 0, z, "create:track[shape=xo]")
