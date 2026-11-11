"""The scenes of the screenshot world, one entry per quest id in docs/SCREENSHOTS.md.

Each entry draws into a Cell (see build.py): x runs east, z south, y 0 is the first layer
above the floor. The camera stands south of the cell and looks north, so the front of
everything faces south.

Rules a scene keeps:
  * Its layout comes from the mod's own files wherever the mod ships one: Ponder scenes of
    Create, the multiblock templates of Immersive Engineering, the pentacles of Occultism.
    Nothing is laid out from memory when the jar has the answer.
  * A multiblock stands formed, the way the quest's reader will see it once it works.
  * Every block that can be turned says which way it looks.
  * One quest, one scene. A quest whose picture would need a hand, a screen or a fight gets
    no scene, and so no picture.
"""
import json

SCENES = {}


class Spec:
    def __init__(self, fn, w, d):
        self.fn, self.w, self.d = fn, w, d


def scene(*keys, w=9, d=9):
    def deco(fn):
        for k in keys:
            SCENES[k] = Spec(fn, w, d)
        return fn
    return deco


# ===================================================================================
# Helpers

def obelisk(b, cx, cz):
    """The whole obelisk the way Core places it: core, stepped plinth, trunk with rune bands, cap, tip, four pedestals."""
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


def stage(b, x1, z1, x2, z2, block):
    """A floor of its own under a scene, set into the grey one."""
    b.f(x1, -1, z1, x2, -1, z2, block)


# ---- Immersive Engineering ----------------------------------------------------------
#
# The multiblock templates of the jar, as they are: their front is their south side. The
# block the hammer has to hit was found by trying every block of every template on a test
# server (see docs/SCREENSHOTS.md), x, y, z from the template's corner.

IE = {
    "alloy_smelter": ((2, 2, 2), (1, 1, 1)), "arcfurnace": ((5, 5, 5), (2, 0, 4)), "assembler": ((3, 3, 3), (1, 1, 2)),
    "auto_workbench": ((3, 2, 3), (1, 1, 2)), "blast_furnace": ((3, 3, 3), (1, 1, 2)),
    "bottling_machine": ((3, 3, 2), (1, 1, 1)), "bucket_wheel": ((7, 7, 1), (3, 3, 0)),
    "coke_oven": ((3, 3, 3), (1, 1, 2)), "crusher": ((5, 3, 3), (2, 1, 2)), "diesel_generator": ((3, 3, 5), (1, 1, 4)),
    "excavator": ((3, 3, 6), (1, 1, 5)), "fermenter": ((3, 3, 3), (1, 1, 1)),
    "improved_blast_furnace": ((3, 4, 3), (1, 1, 2)), "lightning_rod": ((3, 3, 3), (1, 1, 2)),
    "metal_press": ((3, 3, 1), (1, 1, 0)), "mixer": ((3, 3, 3), (1, 1, 1)), "radio_tower": ((5, 19, 6), (2, 1, 5)),
    "refinery": ((5, 3, 3), (2, 1, 2)), "sawmill": ((5, 3, 3), (2, 0, 2)), "sheetmetal_tank": ((3, 5, 3), (1, 1, 2)),
    "shelf": ((4, 4, 2), (1, 1, 1)), "silo": ((3, 7, 3), (1, 1, 2)), "squeezer": ((3, 3, 3), (1, 1, 1)),
}


def ie(b, name, x, z, formed=True):
    """An Immersive Engineering multiblock from its template, front to the camera, formed with the hammer."""
    import structs
    size, trigger = IE[name]
    b.t(f"immersiveengineering:multiblocks/{name}", x, 0, z, size)
    if formed:
        tx, ty, tz = x + trigger[0], trigger[1], z + trigger[2]
        _, palette, blocks, _ = structs.load("ImmersiveEngineering", f"data/immersiveengineering/structure/multiblocks/{name}.nbt")
        before = next(palette[p] for bx, by, bz, p, _ in blocks if (bx, by, bz) == trigger).split("[")[0]
        b.use(tx, ty, tz, "south", "immersiveengineering:hammer")
        b.changed(tx, ty, tz, before)
    return size


def ie_scene(key, name, w=None, d=None):
    size = IE[name][0]
    w = w or max(9, size[0] + 4)
    d = d or max(9, size[2] + 4)

    def fn(b):
        ie(b, name, (b.w - size[0]) // 2, max(1, b.d - size[2] - 3))
    SCENES[key] = Spec(fn, w, d)


# ---- Occultism ------------------------------------------------------------------------

def modonomicon(b, name, x, z, ground=None):
    """A multiblock of the Dictionary of Spirits, as the book defines it: the layers of its
    pattern from the top down, each row running along x and each character along z (the
    stabilizer demo, whose stabilizers face the controller, shows which way round). The lowest
    layer is the ground it stands on and goes into the floor. Returns its size along x and z."""
    import structs
    pattern, mapping = structs.modonomicon("occultism", f"data/occultism/modonomicon/multiblocks/{name}.json")
    sign = 0
    for li, layer in enumerate(pattern):
        y = len(pattern) - 2 - li               # the last layer is the ground: y -1
        for rx, row in enumerate(layer):
            for rz, ch in enumerate(row):
                if ch in "_ ":
                    continue
                m = mapping[ch]
                block = m.get("display") or m.get("block")
                if block is None:
                    block = {"#minecraft:candles": "minecraft:white_candle[candles=1,lit=true]"}.get(m["tag"])
                    if block is None:
                        raise ValueError(f"{name}: no block for {ch} {m}")
                if y == -1 and ground:
                    block = ground
                if "chalk_glyph" in block:
                    block = f"{block}[facing=south,sign={sign % 13}]"
                    sign += 5
                elif block.endswith("_skull"):
                    block += "[rotation=8]"            # looks south
                b.b(x + rx, y, z + rz, block)
    return len(pattern[0]), len(pattern[0][0])


def pentacle(b, name, cx, cz, bowls=4):
    """A pentacle exactly as the Dictionary of Spirits defines it, on otherstone so the chalk
    reads, with the sacrificial bowls a ritual needs standing around it."""
    import structs
    n = len(structs.modonomicon("occultism", f"data/occultism/modonomicon/multiblocks/{name}.json")[0][0])
    half = n // 2
    stage(b, cx - half - 1, cz - half - 1, cx + half + 1, cz + half + 1, "occultism:otherstone")
    modonomicon(b, name, cx - half, cz - half, ground="occultism:otherstone")
    if bowls:
        r = half + 1
        for dx, dz in ((-r, -r), (r, -r), (-r, r), (r, r))[:bowls]:
            b.b(cx + dx, 0, cz + dz, "occultism:sacrificial_bowl[facing=up]")
    return n


def pentacle_scene(key, name, bowls=4):
    import structs
    n = len(structs.modonomicon("occultism", f"data/occultism/modonomicon/multiblocks/{name}.json")[0][0])
    size = n + 4

    def fn(b):
        pentacle(b, name, b.w // 2, b.d // 2, bowls)
    SCENES[key] = Spec(fn, size, size)


# ===================================================================================
# Occultism

pentacle_scene("occultism/aviar", "summon_foliot")
pentacle_scene("occultism/hedyrin", "possess_foliot")
pentacle_scene("occultism/ophyx", "summon_djinni")
pentacle_scene("occultism/strigeor", "craft_djinni")
pentacle_scene("occultism_afrit/kandar", "summon_unbound_afrit")
pentacle_scene("occultism_afrit/marid_crusher", "summon_marid")


@scene("occultism/spirit_fire")
def _(b):
    # spirit fire on the floor, andesite thrown in comes out as otherstone
    b.b(4, 0, 4, "occultism:spirit_fire[color=white]")
    b.drop(4, 1.5, 4, "minecraft:andesite", 8)
    b.drop(5, 0.2, 5, "occultism:otherstone", 4)
    b.focus(2, 0, 2, 6, 2, 6)


@scene("occultism_afrit/storage", w=13, d=13)
def _(b):
    # the book's own demo: the actuator in the middle, four stabilizers on otherstone posts facing it
    modonomicon(b, "storage_stabilizer_demo", 2, 2)


# ===================================================================================
# Immersive Engineering

@scene("immersive/hammer")
def _(b):
    # the bricks stacked and not yet formed, the hammer that will do it in front
    ie(b, "coke_oven", 3, 2, formed=False)
    b.show(4, 0, 6, "immersiveengineering:hammer", scale=1.2)


ie_scene("immersive/coke_oven", "coke_oven")
ie_scene("immersive/kiln", "alloy_smelter")
ie_scene("immersive/tank", "sheetmetal_tank")
ie_scene("immersive/silo", "silo")
ie_scene("immersive/shelf", "shelf")
for _key, _name in [("crusher", "crusher"), ("press", "metal_press"), ("squeezer", "squeezer"), ("fermenter", "fermenter"),
                    ("mixer", "mixer"), ("bottling", "bottling_machine"), ("arc", "arcfurnace"), ("refinery", "refinery"),
                    ("diesel", "diesel_generator"), ("sawmill", "sawmill"), ("assembler", "assembler"),
                    ("auto_workbench", "auto_workbench"), ("excavator", "excavator"), ("lightning_rod", "lightning_rod"),
                    ("radio_tower", "radio_tower")]:
    ie_scene(f"immersive_heavy/{_key}", _name)


# ===================================================================================
# Botania

def pool(b, x, y, z, mana=1000000, spark=False):
    b.b(x, y, z, "botania:mana_pool", f"{{mana:{mana}}}" if mana else "")
    if spark:
        b.e("botania:mana_spark", x, y + 1.25, z)


def terra_plate(b, cx, cz):
    """TerrestrialAgglomerationPlateBlockEntity: RLR / L0L / RLR under the plate, R and 0 livingrock, L lapis."""
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            b.b(cx + dx, 0, cz + dz, "minecraft:lapis_block" if abs(dx) + abs(dz) == 1 else "botania:livingrock")
    b.b(cx, 1, cz, "botania:terrestrial_agglomeration_plate")


@scene("botania_runes/plate_base")
def _(b):
    terra_plate(b, 4, 4)


@scene("botania_runes/terrasteel", w=11)
def _(b):
    # the plate with its three ingredients on it, sparks on the plate and on two full pools
    terra_plate(b, 5, 4)
    b.e("botania:mana_spark", 5, 2.25, 4)
    pool(b, 1, 0, 4, spark=True)
    pool(b, 9, 0, 4, spark=True)
    for item in ("botania:manasteel_ingot", "botania:mana_pearl", "botania:mana_diamond"):
        b.drop(5, 1.3, 4, item)


def gateway(b, x, y, z):
    """AlfheimPortalBlockEntity: a 5 by 5 frame along x. Bottom _w0w_, sides W G W, top _wgw_;
    w and W livingwood, g and G glimmering livingwood, 0 the gateway core."""
    b.b(x + 2, y, z, "botania:elven_gateway_core")
    for dx in (1, 3):
        b.b(x + dx, y, z, "botania:livingwood_log[axis=x]")
        b.b(x + dx, y + 4, z, "botania:livingwood_log[axis=x]")
    b.b(x + 2, y + 4, z, "botania:glimmering_livingwood_log[axis=x]")
    for dx in (0, 4):
        b.b(x + dx, y + 1, z, "botania:livingwood_log[axis=y]")
        b.b(x + dx, y + 2, z, "botania:glimmering_livingwood_log[axis=y]")
        b.b(x + dx, y + 3, z, "botania:livingwood_log[axis=y]")


@scene("alfheim/frame", w=11)
def _(b):
    # the frame, and the two pools with a natura pylon over each that opening it needs
    gateway(b, 3, 0, 3)
    for x in (1, 9):
        pool(b, x, 0, 5)
        b.b(x, 1, 5, "botania:natura_pylon")


@scene("alfheim/open", w=11)
def _(b):
    gateway(b, 3, 0, 3)
    for x in (1, 9):
        pool(b, x, 0, 5)
        b.b(x, 1, 5, "botania:natura_pylon")
    b.use(5, 0, 3, "south", "botania:wand_of_the_forest")
    b.changed(5, 0, 3, "botania:elven_gateway_core[state=off]")


@scene("gaia/arena", w=15, d=15)
def _(b):
    # GaiaGuardianEntity.PYLON_OFFSETS: four gaia pylons 4 out and 1 up from the beacon
    b.f(6, -1, 6, 8, -1, 8, "minecraft:iron_block")
    b.b(7, 0, 7, "minecraft:beacon")
    for dx in (-4, 4):
        for dz in (-4, 4):
            b.b(7 + dx, 0, 7 + dz, "minecraft:quartz_block")
            b.b(7 + dx, 1, 7 + dz, "botania:gaia_pylon")


@scene("botania/pure_daisy")
def _(b):
    # the daisy turns the eight blocks around it: stone to livingrock, logs to livingwood
    b.b(4, -1, 4, "minecraft:grass_block")
    b.b(4, 0, 4, "botania:pure_daisy")
    ring = {(-1, -1): "minecraft:stone", (0, -1): "botania:livingrock", (1, -1): "minecraft:stone",
            (-1, 0): "minecraft:oak_log[axis=y]", (1, 0): "botania:livingwood_log[axis=y]",
            (-1, 1): "botania:livingrock", (0, 1): "minecraft:stone", (1, 1): "botania:livingrock"}
    for (dx, dz), block in ring.items():
        b.b(4 + dx, 0, 4 + dz, block)


# ===================================================================================
# Create
#
# Positions and states follow Create's own Ponder scenes (assets/create/ponder); a creative
# motor behind the scene drives what has to turn.

def motor(b, x, y, z, facing, speed=32):
    """A creative motor; facing is where its shaft points."""
    b.b(x, y, z, f"create:creative_motor[facing={facing}]", f"{{ScrollValue:{speed}}}")


@scene("create/depot")
def _(b):
    # Ponder mechanical_press/pressing: the press two above what it presses, one block of air between
    b.b(4, 0, 4, "create:depot")
    b.b(4, 2, 4, "create:mechanical_press[facing=south]")
    b.b(4, 2, 3, "create:shaft[axis=z]")
    motor(b, 4, 2, 2, "south")
    b.use(4, 0, 4, "up", "minecraft:iron_ingot")


@scene("create/mixer")
def _(b):
    # Ponder mechanical_mixer/mixing: mixer two above the basin, a cogwheel beside it drives it
    b.b(4, 0, 4, "create:basin[facing=down]")
    b.b(4, 2, 4, "create:mechanical_mixer")
    b.b(4, 2, 3, "create:cogwheel[axis=y]")
    motor(b, 4, 3, 3, "down")
    b.drop(4, 1, 4, "minecraft:andesite", 16)
    b.drop(4, 1.3, 4, "minecraft:iron_nugget", 16)


@scene("create/compacting")
def _(b):
    # Ponder mechanical_press/compacting: the press over a basin
    b.b(4, 0, 4, "create:basin[facing=down]")
    b.b(4, 2, 4, "create:mechanical_press[facing=south]")
    b.b(4, 2, 3, "create:shaft[axis=z]")
    motor(b, 4, 2, 2, "south")
    b.drop(4, 1, 4, "minecraft:flint", 8)
    b.drop(4, 1.3, 4, "minecraft:gravel", 8)
    b.use(4, 0, 4, "up", "minecraft:lava_bucket")


@scene("create/water_wheel", w=10)
def _(b):
    # four wheels on one shaft; a flume behind them, the water runs over their tops and falls
    # in front into a trench, as in Ponder water_wheel (source beside, flow over the top)
    for x in range(3, 7):
        b.b(x, 1, 4, "create:water_wheel[facing=east]")
        b.b(x, 1, 3, "minecraft:spruce_planks")           # under the flume
        b.b(x, 2, 2, "minecraft:spruce_planks")           # its back wall
        b.b(x, -1, 5, "minecraft:air")                    # the trench the water falls into
    for z in (2, 3, 4):
        b.b(2, 2, z, "minecraft:spruce_planks")
        b.b(7, 2, z, "minecraft:spruce_planks")
    b.f(2, 1, 3, 2, 1, 3, "minecraft:spruce_planks")
    b.f(7, 1, 3, 7, 1, 3, "minecraft:spruce_planks")
    b.b(2, 1, 4, "create:shaft[axis=x]")
    b.b(7, 1, 4, "create:shaft[axis=x]")
    b.f(3, 2, 3, 6, 2, 3, "minecraft:water")


# ===================================================================================
# Mekanism

@scene("mekanism/dynamic_tank")
def _(b):
    # a hollow 3x3x3: casing on every edge, structural glass or a valve in the faces
    for x in range(3):
        for y in range(3):
            for z in range(3):
                edge = sum(v in (0, 2) for v in (x, y, z))
                if edge == 0:
                    continue                                   # the hollow middle
                block = "mekanism:dynamic_tank"
                if edge == 1:
                    block = "mekanism:structural_glass"
                    if y == 0:
                        block = "mekanism:dynamic_tank"
                    if (x, y, z) == (2, 1, 1):
                        block = "mekanism:dynamic_valve"
                b.b(3 + x, y, 3 + z, block)


# ===================================================================================
# Ars Nouveau

@scene("ars_nouveau/apparatus")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:arcane_core[facing=up]")
    b.b(4, 1, 4, "ars_nouveau:enchanting_apparatus[facing=up]")
    for dx, dz in ((-2, -2), (0, -3), (2, -2), (-3, 0), (3, 0), (-2, 2), (2, 2)):
        b.b(4 + dx, 0, 4 + dz, "ars_nouveau:arcane_pedestal[facing=up]")
    b.b(7, 0, 7, "ars_nouveau:source_jar[fill=11]", "{source:10000}")
