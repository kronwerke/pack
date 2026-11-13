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
    def __init__(self, fn, w, d, h=0):
        self.fn, self.w, self.d, self.h = fn, w, d, h      # h: walls at least this high


def scene(*keys, w=9, d=9, h=0):
    def deco(fn):
        for k in keys:
            SCENES[k] = Spec(fn, w, d, h)
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
    # a tall one needs room in front of it for the camera, and walls that stay behind it
    d = d or max(9, size[2] + 4, size[1] + 6)

    def fn(b):
        ie(b, name, (b.w - size[0]) // 2, 2)
    SCENES[key] = Spec(fn, w, d, h=size[1] + 12)


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
                if y == -1:
                    if ground is False:
                        continue                 # the book's ground is only for show
                    block = ground or block
                if "chalk_glyph" in block:
                    block = f"{block}[facing=south,sign={sign % 13}]"
                    sign += 5
                elif block.endswith("_skull"):
                    block += "[rotation=8]"            # looks south
                b.b(x + rx, y, z + rz, block)
    return len(pattern[0]), len(pattern[0][0])


def pentacle(b, name, cx, cz, bowls=4):
    """A pentacle exactly as the Dictionary of Spirits defines it, with the sacrificial bowls a
    ritual needs standing around it."""
    import structs
    n = len(structs.modonomicon("occultism", f"data/occultism/modonomicon/multiblocks/{name}.json")[0][0])
    half = n // 2
    # a dark, even floor: white chalk on the pale otherstone of the book's preview is lost
    stage(b, cx - half - 1, cz - half - 1, cx + half + 1, cz + half + 1, "minecraft:smooth_basalt")
    modonomicon(b, name, cx - half, cz - half, ground=False)
    if bowls:
        r = half + 1
        for dx, dz in ((0, -r), (r, 0), (0, r), (-r, 0))[:bowls]:
            b.b(cx + dx, 0, cz + dz, "occultism:sacrificial_bowl[facing=up]")
    b.pitch = 58.0                          # from above, the way the book shows it
    return n


def pentacle_scene(key, name, bowls=4):
    import structs
    n = len(structs.modonomicon("occultism", f"data/occultism/modonomicon/multiblocks/{name}.json")[0][0])
    size = n + 4

    def fn(b):
        pentacle(b, name, b.w // 2, b.d // 2, bowls)
    SCENES[key] = Spec(fn, size, size)


# ===================================================================================
# Start

@scene("start_here/o_feeder", w=15, d=17, h=30)
def _(b):
    # the Zubringer block within 10 blocks of the obelisk, a hopper pushing a chest's stone into it
    obelisk(b, 7, 7)
    b.b(7, 0, 14, "kronwerke:obelisk_intake")
    b.b(7, 1, 14, "minecraft:hopper[facing=down]")
    b.c(7, 2, 14, [("minecraft:cobblestone", 64)] * 3, frame=True)
    b.focus(4, 0, 10, 10, 4, 15)


@scene("start_here/m_goldleaf", h=20)
def _(b):
    # an oak whose leaves have all turned golden (golden_leaves at its last stage)
    b.b(4, -1, 4, "minecraft:dirt")
    b.f(4, 0, 4, 4, 4, 4, "minecraft:oak_log[axis=y]")
    for y, r in ((3, 2), (4, 2), (5, 1), (6, 1)):
        for dx in range(-r, r + 1):
            for dz in range(-r, r + 1):
                if (dx, dz) != (0, 0) or y > 4:
                    if abs(dx) == r and abs(dz) == r and (y in (4, 6)):
                        continue                      # the corners an oak leaves out
                    b.b(4 + dx, y, 4 + dz, "naturesaura:golden_leaves[stage=3,persistent=true]")


# Multiblocks of Nature's Aura as its own class has them (blocks/multi/Multiblocks)
TREE_RITUAL = ["    W    ", " W     W ", "   GGG   ", "  GG GG  ", "W G 0 G W", "  GG GG  ", "   GGG   ", " W     W ", "    W    "]
ALTAR = [   # from the top layer down; the last one lies in the ground
    ["    M    ", "         ", "         ", "         ", "M       M", "         ", "         ", "         ", "    M    "],
    ["    B    ", "         ", "         ", "         ", "B       B", "         ", "         ", "         ", "    B    "],
    ["    B    ", "         ", "  M   M  ", "         ", "B   0   B", "         ", "  M   M  ", "         ", "    B    "],
    ["         ", "   WBW   ", "   WBW   ", " WWCWCWW ", " BBW WBB ", " WWCWCWW ", "   WBW   ", "   WBW   ", "         "],
]


@scene("start_here/m_ritual", w=11, d=11)
def _(b):
    # the Ritual of the Forest: sixteen gold powder around the sapling, eight wooden stands outside
    blocks = {"W": "naturesaura:wood_stand", "G": "naturesaura:gold_powder", "0": "minecraft:oak_sapling"}
    for z, row in enumerate(TREE_RITUAL):
        for x, ch in enumerate(row):
            if ch != " ":
                b.b(1 + x, 0, 1 + z, blocks[ch])
    b.b(5, -1, 5, "minecraft:grass_block")
    # what the Natural Altar takes, on four of the stands
    for (x, z), item in {(5, 1): "botania:livingrock", (9, 5): "naturesaura:gold_leaf", (5, 9): "minecraft:gold_ingot", (1, 5): "naturesaura:token_joy"}.items():
        b.use(x, 0, z, "up", item)
    b.pitch = 48.0


@scene("start_here/m_altar", w=11, d=11)
def _(b):
    # the Natural Altar in its building: four pillars of stone bricks with a golden stone brick
    # on top, four golden stone bricks around the altar, the floor of planks and bricks
    blocks = {"M": "naturesaura:gold_brick", "B": "minecraft:stone_bricks", "W": "minecraft:oak_planks",
              "C": "minecraft:chiseled_stone_bricks", "0": "naturesaura:nature_altar"}
    for li, layer in enumerate(ALTAR):
        y = len(ALTAR) - 2 - li
        for z, row in enumerate(layer):
            for x, ch in enumerate(row):
                if ch != " ":
                    b.b(1 + x, y, 1 + z, blocks[ch])
    b.pitch = 42.0


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
    b.focus(3, 0, 3, 5, 1, 5)


@scene("occultism_afrit/storage", w=13, d=13)
def _(b):
    # the book's own demo: the actuator in the middle, four stabilizers on otherstone posts facing it
    modonomicon(b, "storage_stabilizer_demo", 2, 2, ground=False)


# ===================================================================================
# Immersive Engineering

@scene("immersive/hammer")
def _(b):
    # the bricks stacked and not yet formed, the hammer that will do it in front
    ie(b, "coke_oven", 3, 2, formed=False)
    b.show(4, 0, 6, "immersiveengineering:hammer", scale=1.2)


ie_scene("immersive/coke_oven", "coke_oven")
ie_scene("immersive/blast_furnace", "blast_furnace")
ie_scene("immersive/improved_form", "improved_blast_furnace")
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
    b.pitch = 62.0                          # over the ring, or the front row hides the flower


# ===================================================================================
# Create
#
# Positions and states follow Create's own Ponder scenes (assets/create/ponder); a creative
# motor behind the scene drives what has to turn.

def motor(b, x, y, z, facing, speed=32):
    """A creative motor; facing is where its shaft points. It is never part of the picture:
    it sits in the floor or behind a wall."""
    n = len(b.pts)
    b.b(x, y, z, f"create:creative_motor[facing={facing}]", f"{{ScrollValue:{speed}}}")
    del b.pts[n:]


def drive_from_behind(b, x, y, z):
    """Turns what stands at x, y, z and takes a shaft from the north: a wall of andesite casing
    behind it, the shaft through the wall encased, the motor behind the wall."""
    b.f(x - 1, 0, z - 1, x + 1, y + 1, z - 1, "create:andesite_casing")
    b.b(x, y, z - 1, "create:andesite_encased_shaft[axis=z]")
    motor(b, x, y, z - 2, "south")


def drive_from_below(b, x, y, z):
    """Turns what stands at x, y, z and takes a shaft from below: a shaft up from a motor in the floor."""
    for yy in range(-1, y):
        b.b(x, yy, z, "create:shaft[axis=y]")      # through a hole in the floor
    motor(b, x, -2, z, "up")


@scene("create/depot")
def _(b):
    # Ponder mechanical_press/pressing: the press two above what it presses, one block of air between
    b.b(4, 0, 4, "create:depot")
    b.b(4, 2, 4, "create:mechanical_press[facing=south]")
    drive_from_behind(b, 4, 2, 4)
    b.use(4, 0, 4, "up", "minecraft:iron_ingot")


@scene("create/mixer")
def _(b):
    # Ponder mechanical_mixer/mixing: mixer two above the basin, a cogwheel beside it drives it
    b.b(4, 0, 4, "create:basin[facing=down]")
    b.b(4, 2, 4, "create:mechanical_mixer")
    b.b(5, 2, 4, "create:cogwheel[axis=y]")
    drive_from_below(b, 5, 2, 4)
    b.drop(4, 1, 4, "minecraft:andesite", 16)
    b.drop(4, 1.3, 4, "minecraft:iron_nugget", 16)


@scene("create/compacting")
def _(b):
    # Ponder mechanical_press/compacting: the press over a basin
    b.b(4, 0, 4, "create:basin[facing=down]")
    b.b(4, 2, 4, "create:mechanical_press[facing=south]")
    drive_from_behind(b, 4, 2, 4)
    b.drop(4, 1, 4, "minecraft:flint", 8)
    b.drop(4, 1.3, 4, "minecraft:gravel", 8)
    b.use(4, 0, 4, "up", "minecraft:lava_bucket")


def housed_motor(b, x, y, z, facing, speed=32):
    """A creative motor boxed in andesite casing on every side but the one its shaft leaves by:
    what shows is a casing block with a shaft coming out of it."""
    step = {"east": (1, 0, 0), "west": (-1, 0, 0), "south": (0, 0, 1), "north": (0, 0, -1), "up": (0, 1, 0), "down": (0, -1, 0)}
    motor(b, x, y, z, facing, speed)
    for name, (dx, dy, dz) in step.items():
        if name != facing and y + dy >= 0:
            b.b(x + dx, y + dy, z + dz, "create:andesite_casing")


@scene("create/windmill", w=13, d=13, h=24)
def _(b):
    # a windmill bearing on a post, 32 sails in four arms of two by four around a hub, assembled
    # with a click on the bearing so it turns
    cx, cy, z = 6, 6, 5
    b.f(cx, 0, z, cx, cy - 1, z, "minecraft:spruce_log[axis=y]")
    b.b(cx, cy, z, "create:windmill_bearing[facing=south]")
    sail = "create:white_sail[facing=south]"
    b.b(cx, cy, z + 1, sail)
    b.f(cx, cy + 1, z + 1, cx + 1, cy + 4, z + 1, sail)          # up
    b.f(cx + 1, cy - 1, z + 1, cx + 4, cy, z + 1, sail)          # right
    b.f(cx - 1, cy - 4, z + 1, cx, cy - 1, z + 1, sail)          # down
    b.f(cx - 4, cy, z + 1, cx - 1, cy + 1, z + 1, sail)          # left
    b.use(cx, cy, z, "south", "minecraft:air")
    b.later(cx, cy + 4, z + 1, "block @ create:white_sail", unless=True)     # the sails left the world: it turns


@scene("create/cobble_gen")
def _(b):
    # the classic generator in a row: water, a hole that swallows it, the stone, lava. The
    # drill sits behind the stone and breaks it as it forms.
    for x in range(1, 8):
        b.b(x, 0, 3, "minecraft:stone_bricks")
        b.b(x, 0, 5, "minecraft:glass")
    b.b(1, 0, 4, "minecraft:stone_bricks")
    b.b(7, 0, 4, "minecraft:stone_bricks")
    b.b(2, 0, 4, "minecraft:water")
    b.b(4, -1, 4, "minecraft:air")                     # the water falls in here and goes no further
    b.b(5, 0, 4, "minecraft:cobblestone")
    b.b(6, 0, 4, "minecraft:lava")
    b.b(5, 0, 3, "create:mechanical_drill[facing=south]")
    drive_from_behind(b, 5, 0, 3)


@scene("create_brass/crafter")
def _(b):
    # Ponder mechanical_crafter/setup: three by three, the top rows hand down, the bottom row to
    # the right, a cogwheel beside one of them turns them all
    for x in range(3):
        for y in range(3):
            b.b(3 + x, y, 4, f"create:mechanical_crafter[facing=south,pointing={'right' if y == 0 else 'down'}]")
    b.b(6, 0, 4, "create:depot")
    b.b(2, 0, 4, "create:cogwheel[axis=z]")
    drive_from_behind(b, 2, 0, 4)


@scene("create_brass/crushing_wheel", w=11)
def _(b):
    # Ponder crushing_wheel: two wheels a block apart turning against each other; the gap
    # between them crushes what falls in
    b.b(4, 1, 4, "create:crushing_wheel[axis=z]")
    b.b(6, 1, 4, "create:crushing_wheel[axis=z]")
    b.f(3, 0, 3, 7, 2, 3, "create:andesite_casing")
    for x, speed in ((4, 32), (6, -32)):
        b.b(x, 1, 3, "create:andesite_encased_shaft[axis=z]")
        motor(b, x, 1, 2, "south", speed)
    b.drop(5, 3, 4, "minecraft:raw_iron", 8)
    b.later(5, 1, 4, "block @ create:crushing_wheel_controller")


@scene("create/belt")
def _(b):
    # two parallel shafts, clicked one after the other with the belt in hand. It runs toward
    # the camera, so the shaft in its end shows; ingots lie on it.
    b.b(4, 0, 2, "create:shaft[axis=x]")
    b.b(4, 0, 6, "create:shaft[axis=x]")
    b.use(4, 0, 2, "up", "create:belt_connector")
    b.use(4, 0, 6, "up", "create:belt_connector")
    b.changed(4, 0, 4, "minecraft:air")              # the belt runs between them
    for z in (3, 4, 5):
        b.drop(4, 1, z, "minecraft:iron_ingot")


@scene("create/washing")
def _(b):
    # Ponder fan/processing: a fan blowing through water turns its stream into a washing
    # stream. The stream ends in the first thing that is not air, so the belt runs across it
    # and carries the gravel through. The water sits between the fan, the belt and two panes
    # of glass.
    b.b(3, 0, 2, "create:shaft[axis=x]")
    b.b(3, 0, 6, "create:shaft[axis=x]")
    b.use(3, 0, 2, "up", "create:belt_connector")
    b.use(3, 0, 6, "up", "create:belt_connector")
    b.changed(3, 0, 4, "minecraft:air")
    b.b(4, 0, 3, "minecraft:glass")
    b.b(4, 0, 5, "minecraft:glass")
    b.b(4, 0, 4, "minecraft:water")
    b.b(5, 0, 4, "create:encased_fan[facing=west]")
    housed_motor(b, 6, 0, 4, "west", 64)
    b.drop(3, 1, 4, "minecraft:gravel", 8)
    b.later(3, 0, 5, "block @ create:belt")                # the water has not washed the belt away
    b.later(4, 0, 4, "block @ minecraft:water")


@scene("create/water_wheel", w=10)
def _(b):
    # Four wheels on one shaft across a stream: the water runs in a trench in the floor, from
    # four sources at the back toward the camera, and passes under the wheels. Water that
    # flows past a wheel turns it, as in Ponder water_wheel.
    for x in range(3, 7):
        b.b(x, -1, 1, "minecraft:water")                       # the sources
        for z in range(2, 8):
            b.b(x, -1, z, "minecraft:air")                     # the trench they run down
        b.b(x, 0, 4, "create:water_wheel[facing=east]")
    for x in (2, 7):
        b.b(x, 0, 4, "create:andesite_encased_shaft[axis=x]")
    b.later(3, 0, 4, "data block @ {Speed:0.0f}", unless=True)       # it turns
    b.later(4, -1, 6, "block @ minecraft:water")
    b.focus(2, 0, 2, 7, 2, 7)                              # the wheels are larger than their blocks


# ===================================================================================
# Mekanism

def mek_box(b, x0, z0, w, h, d, casing, glass="mekanism:structural_glass", special=None, front_glass=True,
            glass_only_front=False):
    """A hollow Mekanism multiblock: casing on every edge and in the floor, glass in the other
    faces (or only in the front, for a look inside), and what special names at its place
    ({(x, y, z): block}, counted from the corner)."""
    special = special or {}
    for x in range(w):
        for y in range(h):
            for z in range(d):
                on = [x in (0, w - 1), y in (0, h - 1), z in (0, d - 1)]
                if not any(on):
                    continue                                   # the hollow inside
                block = casing
                if sum(on) == 1 and y != 0 and (front_glass or z != d - 1) and (not glass_only_front or z == d - 1):
                    block = glass
                block = special.get((x, y, z), block)
                b.b(x0 + x, y, z0 + z, block)


@scene("mekanism/dynamic_tank")
def _(b):
    # hollow, casing on every edge, glass or valves in the faces; the valve in the front
    mek_box(b, 2, 3, 4, 3, 3, "mekanism:dynamic_tank", special={(2, 1, 2): "mekanism:dynamic_valve"})
    b.formed(4, 1, 5)


@scene("mekanism_advanced/teleporter")
def _(b):
    # TileEntityTeleporter.hasFrame: the teleporter at the bottom centre, frames beside it on
    # four levels and one on top: 3 wide, 4 high, an opening of 1 by 2
    b.b(4, 0, 4, "mekanism:teleporter")
    for y in range(4):
        b.b(3, y, 4, "mekanism:teleporter_frame")
        b.b(5, y, 4, "mekanism:teleporter_frame")
    b.b(4, 3, 4, "mekanism:teleporter_frame")


@scene("mekanism_advanced/evap", h=20)
def _(b):
    # Thermal Evaporation Plant: 4 by 4, a full floor, hollow walls, the top a rim open to the
    # sky; controller and valve sit in a wall, not on an edge
    x0, z0, height = 3, 2, 6
    for y in range(height):
        for x in range(4):
            for z in range(4):
                rim = x in (0, 3) or z in (0, 3)
                if y > 0 and not rim:
                    continue
                b.b(x0 + x, y, z0 + z, "mekanism:thermal_evaporation_block")
    b.b(x0 + 1, 2, z0 + 3, "mekanism:thermal_evaporation_controller[facing=south,active=false]")
    b.b(x0 + 2, 1, z0 + 3, "mekanism:thermal_evaporation_valve")
    b.b(x0 + 3, 1, z0 + 2, "mekanism:thermal_evaporation_valve")
    b.formed(x0 + 1, 2, z0 + 3)


@scene("mekanism_advanced/boiler", w=11, d=11)
def _(b):
    # Thermoelectric Boiler, cut open by a front of structural glass: superheating elements on
    # the floor, the water space, one full layer of pressure dispersers, the steam space
    inside = {}
    for x in range(1, 4):
        for z in range(1, 4):
            inside[(x, 1, z)] = "mekanism:superheating_element[active=false]"
            inside[(x, 4, z)] = "mekanism:pressure_disperser"
    walls = {(4, 2, 2): "mekanism:boiler_valve[mode=input]", (4, 6, 2): "mekanism:boiler_valve[mode=output_steam]"}
    mek_box(b, 3, 3, 5, 8, 5, "mekanism:boiler_casing", special=walls, front_glass=True, glass_only_front=True)
    for (x, y, z), block in inside.items():
        b.b(3 + x, y, 3 + z, block)
    b.formed(7, 2, 5)


@scene("mekanism_advanced/turbine", w=11, d=11)
def _(b):
    # Industrial Turbine, cut open by a front of structural glass: the rotor shaft with its
    # blades, the rotational complex in a full layer of pressure dispersers, a coil on the
    # complex, condensers beside it, vents in the walls from the complex up
    walls = {(4, 2, 2): "mekanismgenerators:turbine_valve", (0, 2, 2): "mekanismgenerators:turbine_valve"}
    for y in (5, 6, 7):
        for k in (1, 2, 3):
            walls[(0, y, k)] = "mekanismgenerators:turbine_vent"
            walls[(4, y, k)] = "mekanismgenerators:turbine_vent"
            walls[(k, y, 0)] = "mekanismgenerators:turbine_vent"
    mek_box(b, 3, 3, 5, 9, 5, "mekanismgenerators:turbine_casing", special=walls, front_glass=True, glass_only_front=True)
    for y in range(1, 5):
        b.b(5, y, 5, "mekanismgenerators:turbine_rotor", "{blades:2}")
    b.b(5, 5, 5, "mekanismgenerators:rotational_complex")
    for x in range(1, 4):
        for z in range(1, 4):
            if (x, z) != (2, 2):
                b.b(3 + x, 5, 3 + z, "mekanism:pressure_disperser")
                b.b(3 + x, 6, 3 + z, "mekanismgenerators:saturating_condenser")
    b.b(5, 6, 5, "mekanismgenerators:electromagnetic_coil")
    b.formed(7, 2, 5)


@scene("mekanism_elite/induction_matrix", w=11, d=11)
def _(b):
    # Induction Matrix: the shell closed, cells and providers inside, ports in the wall
    walls = {(4, 1, 2): "mekanism:induction_port[active=false]", (4, 3, 2): "mekanism:induction_port[active=true]"}
    mek_box(b, 3, 3, 5, 5, 5, "mekanism:induction_casing", special=walls)
    for x in range(1, 4):
        for y in range(1, 4):
            for z in range(1, 4):
                b.b(3 + x, y, 3 + z, "mekanism:basic_induction_provider" if y == 1 and z == 2 else "mekanism:basic_induction_cell")
    b.formed(7, 1, 5)


# ===================================================================================
# Ars Nouveau

@scene("ars_nouveau/apparatus")
def _(b):
    b.b(4, 0, 4, "ars_nouveau:arcane_core[facing=up]")
    b.b(4, 1, 4, "ars_nouveau:enchanting_apparatus[facing=up]")
    for dx, dz in ((-2, -2), (0, -3), (2, -2), (-3, 0), (3, 0), (-2, 2), (2, 2)):
        b.b(4 + dx, 0, 4 + dz, "ars_nouveau:arcane_pedestal[facing=up]")
    b.b(7, 0, 1, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("ars_nouveau/imbuement")
def _(b):
    # the chamber with an amethyst shard in it, and a jar of source within two blocks so it works fast
    b.b(4, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    b.use(4, 0, 4, "south", "minecraft:amethyst_shard")
    b.b(6, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("ars_nouveau/earth_essence")
def _(b):
    # three pedestals one block from the chamber with iron, seeds and dirt, a source gem in the chamber
    b.b(4, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    for (x, z), item in (((3, 4), "minecraft:iron_ingot"), ((5, 4), "minecraft:wheat_seeds"), ((4, 3), "minecraft:dirt")):
        b.b(x, 0, z, "ars_nouveau:arcane_pedestal[facing=up]")
        b.use(x, 0, z, "south", item)
    b.use(4, 0, 4, "south", "ars_nouveau:source_gem")
    b.b(6, 0, 3, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


# ===================================================================================
# Botania: pools and what stands at them

def spreader(b, x, y, z, to="east", mana=1000):
    """A mana spreader that shoots to one side (Botania keeps the direction as an angle in its data)."""
    angle = {"west": 0, "south": 90, "east": 180, "north": 270}[to]
    b.b(x, y, z, "botania:mana_spreader", f"{{rotationX:{angle}f,rotationY:0f,mana:{mana}}}")


@scene("botania/pool")
def _(b):
    # a full pool, and a spreader that shoots at it
    pool(b, 5, 0, 4)
    spreader(b, 2, 0, 4, "east")


@scene("botania/mana_void")
def _(b):
    # the void sits under the pool and swallows what no longer fits
    b.b(4, 0, 4, "botania:mana_void")
    pool(b, 4, 1, 4)


@scene("botania/manastar")
def _(b):
    stage(b, 2, 2, 6, 6, "minecraft:grass_block")
    pool(b, 4, 0, 4, mana=400000)
    b.b(5, 0, 4, "botania:manastar")


@scene("botania_runes/mana_pearl")
def _(b):
    # the pack's rule: a pearl only forms in a pool that stands on a brass casing
    b.b(4, 0, 4, "create:brass_casing")
    pool(b, 4, 1, 4)
    b.drop(4, 2, 4, "minecraft:ender_pearl")


@scene("botania_runes/runic_altar")
def _(b):
    # a pool feeds the spreader next to it, the spreader shoots at the altar with the ingredients on it
    pool(b, 1, 0, 4)
    spreader(b, 2, 0, 4, "east")
    b.b(6, 0, 4, "botania:runic_altar")
    for item in ("botania:manasteel_ingot", "botania:mana_powder", "minecraft:bone_meal", "minecraft:sugar_cane"):
        b.use(6, 0, 4, "up", item)


# ===================================================================================
# The ways into the other worlds: every one a frame like the Nether portal's, four wide and
# five high, without corners (ten blocks), as the quests say.

def gate(b, frame, inside):
    x, z = 2, 4
    for dx in range(4):
        for y in range(5):
            side, end = dx in (0, 3), y in (0, 4)
            if side != end:
                b.b(x + dx, y, z, frame)
    if inside:
        b.f(x + 1, 1, z, x + 2, 3, z, inside)
        b.expect(x + 1, 2, z, inside.split("[")[0])
    return x, z


@scene("nether/welcome", w=8)
def _(b):
    gate(b, "minecraft:obsidian", "minecraft:nether_portal[axis=x]")


@scene("aether/portal", w=8)
def _(b):
    gate(b, "minecraft:glowstone", "aether:aether_portal[axis=x]")


@scene("deeper_darker/portal", w=8)
def _(b):
    gate(b, "minecraft:reinforced_deepslate", "deeperdarker:otherside_portal[axis=x]")


@scene("undergarden/arrival", w=8)
def _(b):
    gate(b, "minecraft:stone_bricks", "undergarden:undergarden_portal[axis=x]")


@scene("list_dimensions/d_mining", w=8)
def _(b):
    # lit the way a player lights it: a source gem on the inside of the frame
    x, z = gate(b, "kronwerke:grubenrahmen", None)
    b.use(x + 1, 0, z, "up", "ars_nouveau:source_gem")
    b.later(x + 1, 2, z, "block @ kronwerke:minenportal")


# ===================================================================================
# Powah

@scene("powah/orb")
def _(b):
    # the orb with four rods around it, each within four blocks
    b.b(4, 0, 4, "powah:energizing_orb[facing=down]")
    for dx, dz in ((-2, 0), (2, 0), (0, -2)):
        b.b(4 + dx, 0, 4 + dz, "powah:energizing_rod_starter[facing=down]")


# ===================================================================================
# Second batch: what a reader has to lay out by a plan

@scene("immersive/list_mb", w=18, d=12, h=20)
def _(b):
    # the seven structures of stage 2, each formed: the tall ones behind, the low ones in front
    x = 1
    for name in ("sheetmetal_tank", "silo", "improved_blast_furnace", "shelf"):
        x += ie(b, name, x, 1)[0] + 1
    x = 3
    for name in ("coke_oven", "blast_furnace", "alloy_smelter"):
        x += ie(b, name, x, 7)[0] + 2


@scene("immersive/thermoelectric")
def _(b):
    # hot on one side, cold on the opposite one: magma and blue ice, an LV connector on top
    b.b(3, 0, 4, "minecraft:magma_block")
    b.b(4, 0, 4, "immersiveengineering:thermoelectric_generator")
    b.b(5, 0, 4, "minecraft:blue_ice")
    b.use(4, 0, 4, "up", "immersiveengineering:connector_lv")


@scene("immersive/connectors", w=11)
def _(b):
    # two capacitors with a connector each, a relay on a post between them, copper wire from
    # one to the next: connectors and wire placed and strung the way a player does it
    b.b(2, 0, 4, "immersiveengineering:capacitor_lv")
    b.b(8, 0, 4, "immersiveengineering:capacitor_lv")
    b.f(5, 0, 4, 5, 2, 4, "immersiveengineering:treated_fence")
    b.use(2, 0, 4, "up", "immersiveengineering:connector_lv")
    b.use(8, 0, 4, "up", "immersiveengineering:connector_lv")
    b.use(5, 2, 4, "up", "immersiveengineering:connector_lv_relay")
    for x1, y1, x2, y2 in ((2, 1, 5, 3), (5, 3, 8, 1)):
        b.use(x1, y1, 4, "south", "immersiveengineering:wirecoil_copper")
        b.use(x2, y2, 4, "south", "immersiveengineering:wirecoil_copper")


@scene("immersive/dynamo", w=15, d=11, h=26)
def _(b):
    # the dynamo on a post of treated wood, the windmill set against its shaft side
    b.f(7, 0, 3, 7, 6, 3, "immersiveengineering:treated_wood_horizontal")
    b.b(7, 7, 3, "immersiveengineering:dynamo[facing=south]")
    b.use(7, 7, 3, "south", "immersiveengineering:windmill")
    b.changed(7, 7, 4, "minecraft:air")
    b.focus(3, 0, 3, 11, 11, 5)                            # the blades reach four blocks out


@scene("create_brass/brass_mixing")
def _(b):
    # from the bottom: lit blaze burner, basin, a block of air, mixer; a cogwheel beside the
    # mixer turns it. In the basin what brass takes on Kronwerke.
    b.b(4, 0, 4, "create:blaze_burner[blaze=smouldering]")
    b.use(4, 0, 4, "south", "create:creative_blaze_cake")
    b.b(4, 1, 4, "create:basin[facing=down]")
    b.b(4, 3, 4, "create:mechanical_mixer")
    b.b(5, 3, 4, "create:cogwheel[axis=y]")
    drive_from_below(b, 5, 3, 4)
    for item, n in (("minecraft:copper_ingot", 64), ("create:zinc_ingot", 32), ("minecraft:blaze_powder", 32)):
        b.drop(4, 2.2, 4, item, n)


@scene("storage/vault_big", w=10)
def _(b):
    # vaults set side by side merge into one: three by three, six long
    b.f(2, 0, 3, 7, 2, 5, "create:item_vault[axis=x,large=false]")
    b.later(2, 0, 3, "block @ create:item_vault[large=true]")
    b.focus(1, 0, 2, 8, 3, 6)


def mek_shell(b, x0, z0, grid, frame, other, special=None):
    """A Mekanism multiblock whose faces follow the grid of its validator (0 nothing, 1 the
    frame, 2 frame, glass or a port): the fusion reactor and the SPS. The grids are the
    ALLOWED_GRID of FusionReactorValidator and SPSValidator, read from the jars."""
    n = len(grid)
    special = special or {}
    for x in range(n):
        for y in range(n):
            for z in range(n):
                need = 0
                if x in (0, n - 1):
                    need = max(need, grid[z][y])
                if y in (0, n - 1):
                    need = max(need, grid[x][z])
                if z in (0, n - 1):
                    need = max(need, grid[x][y])
                if need:
                    b.b(x0 + x, y, z0 + z, special.get((x, y, z), frame if need == 1 else other))


FUSION = [[0, 0, 1, 0, 0], [0, 1, 2, 1, 0], [1, 2, 2, 2, 1], [0, 1, 2, 1, 0], [0, 0, 1, 0, 0]]
SPS = [[0, 0, 1, 1, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 2, 2, 2, 2, 2, 1], [1, 2, 2, 2, 2, 2, 1],
       [1, 2, 2, 2, 2, 2, 1], [0, 1, 2, 2, 2, 1, 0], [0, 0, 1, 1, 1, 0, 0]]


@scene("mekanism_elite/fusion", w=13, d=11, h=18)
def _(b):
    # the controller in the middle of the top, ports in two faces, the laser focus matrix in
    # the east face; the amplifier fires at the matrix, the laser charges the amplifier
    x0, z0 = 2, 3
    mek_shell(b, x0, z0, FUSION, "mekanismgenerators:fusion_reactor_frame", "mekanismgenerators:reactor_glass", {
        (2, 4, 2): "mekanismgenerators:fusion_reactor_controller[active=false]",
        (4, 2, 2): "mekanismgenerators:laser_focus_matrix",
        (0, 2, 2): "mekanismgenerators:fusion_reactor_port[active=false]",
        (2, 0, 2): "mekanismgenerators:fusion_reactor_port[active=true]"})
    for dx, block in ((6, "mekanism:laser_amplifier[facing=west]"), (8, "mekanism:laser[facing=west]")):
        b.f(x0 + dx, 0, z0 + 2, x0 + dx, 1, z0 + 2, "mekanism:steel_casing")
        b.b(x0 + dx, 2, z0 + 2, block)
    b.formed(x0 + 2, 4, z0 + 2)


@scene("antimatter/sps", w=13, d=13, h=20)
def _(b):
    # casing on the rim of every face, glass and ports inside it; the supercharged coil sits
    # on the port in the front
    x0, z0 = 3, 3
    mek_shell(b, x0, z0, SPS, "mekanism:sps_casing", "mekanism:structural_glass", {
        (3, 3, 6): "mekanism:sps_port[active=false]", (6, 3, 3): "mekanism:sps_port[active=true]",
        (0, 3, 3): "mekanism:sps_port[active=false]"})
    b.use(x0 + 3, 3, z0 + 6, "south", "mekanism:supercharged_coil")
    b.changed(x0 + 3, 3, z0 + 7, "minecraft:air")
    b.formed(x0 + 3, 3, z0 + 6)


@scene("pneumaticcraft/chamber")
def _(b):
    # a hollow cube of three: walls on every edge, glass in the faces, the valve and an
    # interface each in the middle of a face. The last wall goes in by hand: a chamber forms
    # when a player closes the shell.
    x0, z0 = 3, 3
    special = {(2, 1, 1): "pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]",
               (0, 1, 1): "pneumaticcraft:pressure_chamber_interface[facing=west]"}
    for x in range(3):
        for y in range(3):
            for z in range(3):
                on = sum((x != 1, y != 1, z != 1))
                if on == 0 or (x, y, z) == (0, 2, 2):
                    continue
                block = "pneumaticcraft:pressure_chamber_wall[wall_state=none]" if on > 1 else "pneumaticcraft:pressure_chamber_glass"
                b.b(x0 + x, y, z0 + z, special.get((x, y, z), block))
    b.use(x0, 1, z0 + 2, "up", "pneumaticcraft:pressure_chamber_wall")
    b.expect(x0 + 2, 1, z0 + 1, "pneumaticcraft:pressure_chamber_valve[formed=true]")


@scene("draconic/injectors", w=11, d=11)
def _(b):
    # eight injectors on four sides of the fusion crafting core, every tip toward the core,
    # three blocks away (two at least)
    cx, cz = 5, 5
    b.b(cx, 0, cz, "draconicevolution:crafting_core")
    for side in (-1, 1):
        for k in (-3, 3):
            b.b(cx + k, 0, cz + side, f"draconicevolution:basic_crafting_injector[facing={'west' if k > 0 else 'east'}]")
            b.b(cx + side, 0, cz + k, f"draconicevolution:basic_crafting_injector[facing={'north' if k > 0 else 'south'}]")
    b.pitch = 44.0


def malum_altar(b, cx, cz):
    """The spirit altar with runewood planks on it and two item stands with hallowed gold within four blocks."""
    b.b(cx, 0, cz, "malum:spirit_altar")
    b.use(cx, 0, cz, "south", "malum:runewood_planks")
    for dx in (-2, 2):
        b.b(cx + dx, 0, cz, "malum:runewood_planks")
        b.b(cx + dx, 1, cz, "malum:runewood_item_stand[facing=up,waterlogged=false]")
        b.use(cx + dx, 1, cz, "south", "malum:hallowed_gold_ingot")


@scene("malum/altar")
def _(b):
    malum_altar(b, 4, 4)


@scene("malum/obelisk", w=11)
def _(b):
    # up to four runewood obelisks near the altar quicken every infusion
    malum_altar(b, 5, 4)
    for dx, dz in ((-3, -2), (3, -2), (-3, 2), (3, 2)):
        b.use(5 + dx, -1, 4 + dz, "up", "malum:runewood_obelisk")
        b.changed(5 + dx, 0, 4 + dz, "minecraft:air")
    b.focus(1, 0, 1, 9, 2, 7)


@scene("powah/reactor", h=18)
def _(b):
    # the reactor builds itself around its core, three by three and four high. Powah lets no
    # machine hand place it, so the core block is set and its own builder does the rest.
    b.b(4, 0, 4, "powah:reactor_starter[core=true]")
    b.later(5, 3, 5, "block @ powah:reactor_starter")
    b.focus(3, 0, 3, 5, 3, 5)


@scene("occultism_afrit/mineshaft")
def _(b):
    # the mineshaft on a hopper that empties it into a chest
    b.b(4, 0, 4, "minecraft:hopper[facing=east]")
    b.b(4, 1, 4, "occultism:dimensional_mineshaft[rotation=0]")
    b.c(5, 0, 4, [], frame=True)


@scene("ars_nouveau/chamber_auto")
def _(b):
    # a hopper above feeds amethyst, a hopper below takes the gems into a chest; the jar of
    # source within two blocks
    b.c(4, 3, 4, [("minecraft:amethyst_shard", 64)], frame=True)
    b.b(4, 2, 4, "minecraft:hopper[facing=down]")
    b.b(4, 1, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    b.b(4, 0, 4, "minecraft:hopper[facing=east]")
    b.c(5, 0, 4, [], frame=True)
    b.b(2, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("gaia/dandelifeon", w=27, d=27)
def _(b):
    # the field of 25 by 25 around the flower, marked in the floor, with a few cells laid out:
    # a glider on its way to the middle and two blinkers
    stage(b, 1, 1, 25, 25, "minecraft:smooth_stone")
    b.b(13, -1, 13, "minecraft:grass_block")
    b.b(13, 0, 13, "botania:dandelifeon")
    for dx, dz in ((0, 0), (1, 1), (2, 1), (0, 2), (1, 2)):
        b.b(6 + dx, 0, 6 + dz, "botania:cellular_block")
    for x in (18, 19, 20):
        b.b(x, 0, 8, "botania:cellular_block")
    for z in (17, 18, 19):
        b.b(7, 0, z, "botania:cellular_block")
    b.pitch = 55.0


# ===================================================================================
# Third batch

@scene("eidolon/altar")
def _(b):
    # three wooden altars in a row, the straw effigy on the middle one, a candle and a skull beside it
    b.f(3, 0, 4, 5, 0, 4, "eidolon_repraised:wooden_altar")
    b.b(4, 1, 4, "eidolon_repraised:straw_effigy[facing=south]")
    b.b(3, 1, 4, "eidolon_repraised:candle")
    b.b(5, 1, 4, "minecraft:skeleton_skull[rotation=8]")


@scene("eidolon/brazier")
def _(b):
    # the brazier, stone hands around it for what a ritual takes besides
    b.b(4, 0, 4, "eidolon_repraised:brazier")
    for (dx, dz), facing in (((-2, 0), "east"), ((2, 0), "west"), ((0, -2), "south")):
        b.b(4 + dx, 0, 4 + dz, f"eidolon_repraised:stone_hand[facing={facing}]")


@scene("eidolon/crucible")
def _(b):
    # the crucible over a campfire, filled with water
    b.b(4, 0, 4, "minecraft:campfire[facing=south,lit=true]")
    b.b(4, 1, 4, "eidolon_repraised:crucible")
    b.use(4, 1, 4, "up", "minecraft:water_bucket")


@scene("botania/farm", w=13)
def _(b):
    # four endoflames in two pairs, each pair with a spreader that shoots at the pool in the
    # middle; the manastar at the pool shows whether the farm keeps up
    stage(b, 1, 2, 11, 6, "minecraft:grass_block")
    pool(b, 6, 0, 4, mana=200000)
    b.b(6, 0, 5, "botania:manastar")
    spreader(b, 3, 0, 4, "east")
    spreader(b, 9, 0, 4, "west")
    for x in (2, 10):
        for z in (3, 5):
            b.b(x, 0, z, "botania:endoflame")


@scene("ars_nouveau/fill_jar", w=11)
def _(b):
    # the volcanic sourcelink with logs thrown beside it, the jar within five blocks of it, the
    # chamber within two of the jar
    b.b(2, 0, 4, "ars_nouveau:volcanic_sourcelink")
    for dx, dz in ((1, 1), (0, 1), (-1, 1), (1, 0)):
        b.drop(2 + dx, 0.2, 4 + dz, "minecraft:oak_log", 64)
    b.b(6, 0, 4, "ars_nouveau:source_jar[fill=5]", "{source:5000}")
    b.b(8, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    b.use(8, 0, 4, "south", "minecraft:amethyst_shard")


@scene("ars_nouveau/drygmy")
def _(b):
    # the charm on mossy cobblestone makes the henge; chest and jar beside it, animals around
    b.b(4, 0, 4, "minecraft:mossy_cobblestone")
    b.use(4, 0, 4, "up", "ars_nouveau:drygmy_charm")
    b.changed(4, 0, 4, "minecraft:mossy_cobblestone")
    b.c(5, 0, 4, [], frame=True)
    b.b(3, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")
    b.m("minecraft:cow", 6, 0, 6)
    b.m("minecraft:sheep", 2, 0, 6)


@scene("ars_apprentice/brazier")
def _(b):
    # a tablet on the brazier, the jar it draws from beside it (the empty hand that starts it is a player's)
    b.b(4, 0, 4, "ars_nouveau:ritual_brazier")
    b.use(4, 0, 4, "up", "ars_nouveau:ritual_flight")
    b.b(6, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("draconic/stabilizer", w=11, d=11)
def _(b):
    # the core of tier 3 in its cube of 26 draconium blocks, four stabilizers in one plane on
    # four sides, in line with the core's middle and outside its blocks
    cx, cz = 5, 5
    b.f(cx - 1, 0, cz - 1, cx + 1, 2, cz + 1, "draconicevolution:draconium_block")
    b.b(cx, 1, cz, "draconicevolution:energy_core")
    for dx, dz in ((-4, 0), (4, 0), (0, -4), (0, 4)):
        b.b(cx + dx, 0, cz + dz, "minecraft:polished_deepslate")
        b.b(cx + dx, 1, cz + dz, "draconicevolution:energy_core_stabilizer")


@scene("hexerei/herbs")
def _(b):
    # the four herbs, grown: mandrake, belladonna, mugwort and yellow dock
    stage(b, 2, 3, 6, 5, "minecraft:grass_block")
    for z in (3, 4, 5):
        b.b(2, 0, z, "hexerei:mandrake_plant[age=3]")
        b.b(3, 0, z, "hexerei:belladonna_plant[age=3]")
        for x, bush in ((5, "mugwort_bush"), (6, "yellow_dock_bush")):
            b.b(x, 0, z, f"hexerei:{bush}[half=lower,age=3]")
            b.b(x, 1, z, f"hexerei:{bush}[half=upper,age=3]")


# ===================================================================================
# Fourth batch

def forest_ritual(b, items):
    """The Ritual of the Forest of Nature's Aura: gold powder around an oak sapling, eight
    wooden stands outside, one item on each stand (in the order the pattern is read)."""
    blocks = {"W": "naturesaura:wood_stand", "G": "naturesaura:gold_powder", "0": "minecraft:oak_sapling"}
    stands = []
    for z, row in enumerate(TREE_RITUAL):
        for x, ch in enumerate(row):
            if ch != " ":
                b.b(1 + x, 0, 1 + z, blocks[ch])
                if ch == "W":
                    stands.append((1 + x, 1 + z))
    b.b(5, -1, 5, "minecraft:grass_block")
    for (x, z), item in zip(stands, items):
        b.use(x, 0, z, "up", item)
    b.pitch = 48.0


@scene("botania/manasteel_prep", w=11, d=11)
def _(b):
    # manasteel on Kronwerke: four infused iron, two livingwood twigs, a mana diamond and a gold leaf
    forest_ritual(b, ["naturesaura:infused_iron", "botania:livingwood_twig", "naturesaura:infused_iron", "botania:mana_diamond",
                      "naturesaura:gold_leaf", "naturesaura:infused_iron", "botania:livingwood_twig", "naturesaura:infused_iron"])


@scene("mekanism_elite/mekasuit")
def _(b):
    # the whole suit on a stand beside the modification station
    b.stand(3, 0, 4, armor=("mekanism:mekasuit_helmet", "mekanism:mekasuit_bodyarmor", "mekanism:mekasuit_pants", "mekanism:mekasuit_boots"))
    b.b(5, 0, 4, "mekanism:modification_station[facing=south]")


@scene("ars_epic/el_armor")
def _(b):
    # a whole robe set of one school: fire
    b.stand(4, 0, 4, armor=("ars_elemental:fire_hat", "ars_elemental:fire_robes", "ars_elemental:fire_leggings", "ars_elemental:fire_boots"))


@scene("storage/drawers_4")
def _(b):
    # a wall of drawers, three by three, four kinds in each. An upright drawer is facing=down
    # in Functional Storage, and subfacing says where its front looks (seen on the server,
    # 13.11.2026: every other facing lays the model down). The contents are written the way
    # the drawer itself stores them: a hand cannot aim at one of the four compartments.
    kinds = ["iron_ingot", "copper_ingot", "gold_ingot", "raw_iron", "raw_copper", "raw_gold", "coal", "charcoal", "redstone",
             "lapis_lazuli", "diamond", "emerald", "quartz", "amethyst_shard", "flint", "clay_ball", "bone", "string", "gunpowder",
             "rotten_flesh", "leather", "feather", "wheat", "sugar_cane", "red_dye", "blue_dye", "green_dye", "yellow_dye",
             "white_dye", "black_dye", "slime_ball", "ender_pearl", "blaze_rod", "glowstone_dust", "nether_wart", "paper"]
    for i in range(9):
        x, y = 3 + i % 3, i // 3
        b.b(x, y, 4, "functionalstorage:oak_4[facing=down,subfacing=south]")
        slots = ",".join(f'{k}:{{Stack:{{id:"minecraft:{kinds[i * 4 + k]}",count:1}},Amount:{64 * (k + 2)}}}' for k in range(4))
        b.cmd(f"data merge block {b._p(x, y, 4)} {{handler:{{BigItems:{{{slots}}}}}}}")


@scene("antimatter/waste", w=11)
def _(b):
    # a row of solar neutron activators under the open sky, a tube along their backs brings the waste
    for x in (2, 4, 6, 8):
        b.b(x, 0, 4, "mekanism:solar_neutron_activator[facing=south,active=false]")
    b.f(2, 0, 3, 8, 0, 3, "mekanism:basic_pressurized_tube")


@scene("mekanism_ores/line2", w=10)
def _(b):
    # chest, transporter, enrichment chamber, transporter, smelter, transporter, chest; a
    # universal cable behind both machines from an energy cube
    z = 4
    b.c(1, 0, z, [], frame=True)
    b.b(3, 0, z, "mekanism:enrichment_chamber[facing=south,active=false]")
    b.b(5, 0, z, "mekanism:energized_smelter[facing=south,active=false]")
    b.c(7, 0, z, [], frame=True)
    for x in (2, 4, 6):
        b.b(x, 0, z, "mekanism:basic_logistical_transporter")
    b.f(3, 0, z - 1, 6, 0, z - 1, "mekanism:basic_universal_cable")
    b.b(7, 0, z - 1, "mekanism:basic_energy_cube[facing=south]")


@scene("immersive/watermill", w=13, h=22)
def _(b):
    # the water wheel set against the dynamo's shaft side, a stream running under it
    b.f(6, 0, 2, 6, 3, 2, "immersiveengineering:treated_wood_horizontal")
    b.b(6, 4, 2, "immersiveengineering:dynamo[facing=south]")
    b.use(6, 4, 2, "south", "immersiveengineering:watermill")
    b.changed(6, 4, 3, "minecraft:air")
    b.b(1, -1, 3, "minecraft:water")
    for x in range(2, 9):
        b.b(x, -1, 3, "minecraft:air")
    b.focus(1, 0, 2, 11, 8, 4)                             # the wheel is seven across


@scene("the_end/arrival")
def _(b):
    # the End portal as it stands in a stronghold: twelve frames with their eyes around the open portal
    for i in range(3):
        b.b(3 + i, 0, 2, "minecraft:end_portal_frame[eye=true,facing=south]")
        b.b(3 + i, 0, 6, "minecraft:end_portal_frame[eye=true,facing=north]")
        b.b(2, 0, 3 + i, "minecraft:end_portal_frame[eye=true,facing=east]")
        b.b(6, 0, 3 + i, "minecraft:end_portal_frame[eye=true,facing=west]")
    b.f(3, 0, 3, 5, 0, 5, "minecraft:end_portal")
    b.pitch = 50.0


@scene("finale/tech", w=11, d=11)
def _(b):
    # seven wyvern injectors around the fusion crafting core, on them what awakened draconium
    # takes: four draconium cores, two Gaia spirit ingots and the dragon heart
    cx, cz = 5, 5
    b.b(cx, 0, cz, "draconicevolution:crafting_core")
    spots = [(-3, -1, "east"), (-3, 1, "east"), (3, -1, "west"), (3, 1, "west"), (-1, -3, "south"), (1, -3, "south"), (0, 3, "north")]
    items = ["draconicevolution:draconium_core"] * 4 + ["botania:gaia_ingot"] * 2 + ["draconicevolution:dragon_heart"]
    for (dx, dz, facing), item in zip(spots, items):
        b.b(cx + dx, 0, cz + dz, f"draconicevolution:wyvern_crafting_injector[facing={facing}]")
        b.use(cx + dx, 0, cz + dz, "up", item)
    b.pitch = 44.0


# ===================================================================================
# Fifth batch

@scene("eidolon/stone_altar")
def _(b):
    # three stone altars in a row, the unholy effigy on the middle one, goblet and candle beside it
    b.f(3, 0, 4, 5, 0, 4, "eidolon_repraised:stone_altar")
    b.b(4, 1, 4, "eidolon_repraised:unholy_effigy[facing=south]")
    b.b(3, 1, 4, "eidolon_repraised:goblet")
    b.b(5, 1, 4, "eidolon_repraised:candle")


@scene("hexerei/cauldron")
def _(b):
    # two mixing cauldrons with water; the right one is heated, it stands over lava set into the floor
    b.b(3, 0, 4, "hexerei:mixing_cauldron")
    b.b(5, -1, 4, "minecraft:lava")
    b.b(5, 0, 4, "hexerei:mixing_cauldron")
    b.use(3, 0, 4, "up", "minecraft:water_bucket")
    b.use(5, 0, 4, "up", "minecraft:water_bucket")


@scene("food/f_pot")
def _(b):
    # the cooking pot on a lit stove, a cutting board on the counter beside it
    b.b(4, 0, 4, "farmersdelight:stove[facing=south,lit=true]")
    b.b(4, 1, 4, "farmersdelight:cooking_pot[facing=south,support=none]")
    b.b(5, 0, 4, "minecraft:oak_planks")
    b.b(5, 1, 4, "farmersdelight:cutting_board[facing=south]")


@scene("powah/thermo")
def _(b):
    # the thermo generator stands on its heat source
    b.b(4, 0, 4, "minecraft:magma_block")
    b.b(4, 1, 4, "powah:thermo_generator_starter")


@scene("storage/controller")
def _(b):
    # the controller, and barrels that touch it or each other: one store
    b.b(4, 0, 4, "sophisticatedstorage:controller")
    for x, y in ((2, 0), (3, 0), (5, 0), (3, 1), (4, 1), (5, 1)):
        b.b(x, y, 4, "sophisticatedstorage:barrel[facing=south,flat_top=false]")


@scene("list_power/steam_engine", w=10)
def _(b):
    # four blaze burners, the tank on them, a steam engine on the tank's front with its shaft
    for x in (3, 4):
        for z in (3, 4):
            b.b(x, 0, z, "create:blaze_burner[blaze=smouldering]")
            b.use(x, 0, z, "up", "create:creative_blaze_cake")
    b.f(3, 1, 3, 4, 3, 4, "create:fluid_tank[bottom=false,shape=window,top=false]")
    b.b(3, 2, 6, "create:shaft[axis=x]")
    b.b(3, 2, 5, "create:steam_engine[face=wall,facing=south,waterlogged=false]")


@scene("mekanism_ores/tripling", w=10)
def _(b):
    # purification chamber, crusher, enrichment chamber and smelter side by side, each handing
    # on to the next; behind the purification chamber the separator with its oxygen tube, the
    # pump over water beside the separator; a cable behind the other three from an energy cube
    z = 5
    b.c(1, 0, z, [], frame=True)
    for x, name in ((2, "purification_chamber"), (3, "crusher"), (4, "enrichment_chamber"), (5, "energized_smelter")):
        b.b(x, 0, z, f"mekanism:{name}[facing=south,active=false]")
    b.c(6, 0, z, [], frame=True)
    b.b(2, 0, z - 1, "mekanism:basic_pressurized_tube")
    b.b(2, 0, z - 2, "mekanism:electrolytic_separator[facing=south]")
    b.b(3, 0, z - 2, "mekanism:basic_mechanical_pipe")
    b.b(4, -1, z - 2, "minecraft:water")
    b.b(4, 0, z - 2, "mekanism:electric_pump[facing=south]")
    b.f(3, 0, z - 1, 5, 0, z - 1, "mekanism:basic_universal_cable")
    b.b(6, 0, z - 1, "mekanism:basic_energy_cube[facing=south]")


# ===================================================================================
# Sixth batch

@scene("ae2/network", w=10)
def _(b):
    # energy acceptor, glass cable laid from block to block the way a player lays it, a terminal
    # on the cable and a drive at its end. A creative cell under the floor gives the power the
    # acceptor would get from a generator.
    b.b(2, -1, 4, "ae2:creative_energy_cell")
    b.b(2, 0, 4, "ae2:energy_acceptor")
    for x in (2, 3, 4):
        b.use(x, 0, 4, "east", "ae2:fluix_glass_cable")
    b.changed(5, 0, 4, "minecraft:air")
    b.b(6, 0, 4, "ae2:drive[facing=south,spin=0]")
    b.use(4, 0, 4, "south", "ae2:terminal")


@scene("ae2/controller", w=10)
def _(b):
    # a controller of three blocks, a smart cable from it past a terminal to two drives: the
    # stripes on the cable count the channels in use
    b.b(3, -1, 4, "ae2:creative_energy_cell")
    b.f(3, 0, 4, 3, 2, 4, "ae2:controller")
    # one click more than cables: the click on the controller itself placed nothing when the
    # machine hand did it (13.11.2026), and a cable too many ends where the drive goes anyway
    for x in (3, 4, 5, 6):
        b.use(x, 0, 4, "east", "ae2:fluix_smart_cable")
    b.changed(6, 0, 4, "minecraft:air")
    b.b(7, 0, 4, "ae2:drive[facing=south,spin=0]")
    b.b(6, 1, 4, "ae2:drive[facing=south,spin=0]")
    b.use(4, 0, 4, "south", "ae2:terminal")


def endo_feeder(b, x, z):
    """Chest, hopper and open crate over the drop point x, z, and the pressure plate on it that
    locks the hopper while a piece of coal still lies there: its signal climbs a stair of
    redstone dust north and east of the plate to the block beside the hopper. Seen to hold on
    the real server (13.11.2026): plate powered, hopper off, the chest loses a coal at a time."""
    b.b(x, 0, z, "minecraft:oak_pressure_plate")
    b.b(x, 2, z, "botania:open_crate")
    b.b(x, 3, z, "minecraft:hopper[facing=down]")
    b.c(x, 4, z, [("minecraft:coal", 64)], frame=True)
    stair = "minecraft:stone_bricks"
    b.b(x, 0, z - 1, "minecraft:redstone_wire")
    b.b(x, 0, z - 2, stair)
    b.b(x, 1, z - 2, "minecraft:redstone_wire")
    b.b(x + 1, 1, z - 2, stair)
    b.b(x + 1, 2, z - 2, "minecraft:redstone_wire")
    b.b(x + 1, 2, z - 1, stair)
    b.b(x + 1, 3, z - 1, "minecraft:redstone_wire")
    b.b(x + 1, 3, z, stair)


@scene("botania/endo_auto")
def _(b):
    # the feeder over the drop point, endoflames around it
    stage(b, 3, 4, 5, 5, "minecraft:grass_block")
    b.b(4, -1, 4, "minecraft:light_gray_concrete")
    for x, z in ((3, 4), (5, 4), (3, 5), (4, 5), (5, 5)):
        b.b(x, 0, z, "botania:endoflame")
    endo_feeder(b, 4, 4)


@scene("farms/mana_endoflame", w=11)
def _(b):
    # seven endoflames around a spreader that shoots at the pool, the feeder at the bed's edge
    # within three blocks of every flower
    stage(b, 3, 2, 7, 6, "minecraft:grass_block")
    pool(b, 9, 0, 4, mana=300000)
    spreader(b, 6, 0, 4, "east")
    for x, z in ((4, 3), (5, 3), (6, 3), (4, 5), (5, 5), (6, 5), (5, 4)):
        b.b(x, 0, z, "botania:endoflame")
    endo_feeder(b, 3, 4)


@scene("list_transport/create_tank")
def _(b):
    # fluid tanks set together merge into one: three by three, four high
    b.f(3, 0, 3, 5, 3, 5, "create:fluid_tank[bottom=false,shape=window,top=false]")



# ===================================================================================
# Seventh batch

def mek_row(b, names, x0, z):
    """Mekanism machines side by side, fronts to the camera: each hands on to the next."""
    for i, name in enumerate(names):
        b.b(x0 + i, 0, z, f"mekanism:{name}[facing=south]")


@scene("mekanism_ores/shards", w=10)
def _(b):
    # the line of five from the injection chamber to the smelter. Behind the injection chamber
    # the chemical infuser that makes its hydrogen chloride, a separator on either side of the
    # infuser: the one for water also stands behind the purification chamber and gives it oxygen
    z = 5
    b.c(1, 0, z, [], frame=True)
    mek_row(b, ["chemical_injection_chamber", "purification_chamber", "crusher", "enrichment_chamber", "energized_smelter"], 2, z)
    b.c(7, 0, z, [], frame=True)
    mek_row(b, ["electrolytic_separator", "chemical_infuser", "electrolytic_separator"], 1, z - 1)


@scene("mekanism_ores/quintupling", w=12)
def _(b):
    # the whole ladder of eight, from the dissolution chamber to the smelter; a tube over the
    # first three carries the slurry on
    z = 5
    b.c(1, 0, z, [], frame=True)
    mek_row(b, ["chemical_dissolution_chamber", "chemical_washer", "chemical_crystallizer", "chemical_injection_chamber",
                "purification_chamber", "crusher", "enrichment_chamber", "energized_smelter"], 2, z)
    b.c(10, 0, z, [], frame=True)
    b.f(2, 1, z, 4, 1, z, "mekanism:basic_pressurized_tube")


@scene("immersive_heavy/hv", w=13, h=20)
def _(b):
    # two steel posts, an HV connector on each, steel wire between them: hung high, it cannot be insulated
    for x in (2, 10):
        b.use(x, -1, 4, "up", "immersiveengineering:steel_post")
        b.changed(x, 3, 4, "minecraft:air")
        b.use(x, 3, 4, "up", "immersiveengineering:connector_hv")
    b.use(2, 4, 4, "south", "immersiveengineering:wirecoil_steel")
    b.use(10, 4, 4, "south", "immersiveengineering:wirecoil_steel")
    b.focus(1, 0, 3, 11, 5, 5)


@scene("ars_apprentice/relay", w=11)
def _(b):
    # full jar, relay, relay, empty jar, linked with the dominion wand in that order (closer
    # together than the thirty blocks a link reaches, so that all four fit a picture)
    b.b(2, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")
    b.b(4, 0, 4, "ars_nouveau:relay")
    b.b(6, 0, 4, "ars_nouveau:relay")
    b.b(8, 0, 4, "ars_nouveau:source_jar[fill=0]")
    for a, c in ((2, 4), (4, 6), (6, 8)):
        b.use(a, 0, 4, "south", "ars_nouveau:dominion_wand")
        b.use(c, 0, 4, "south", "ars_nouveau:dominion_wand")


@scene("flux_networks/dust")
def _(b):
    # redstone on bedrock, a block of air, obsidian over it: a hit on the obsidian turns the redstone into flux dust
    b.b(4, 0, 4, "minecraft:bedrock")
    b.drop(4, 1.1, 4, "minecraft:redstone", 64)
    b.b(4, 2, 4, "minecraft:obsidian")
    b.focus(3, 0, 3, 5, 2, 5)


@scene("flux_networks/first_link", w=10)
def _(b):
    # a plug on the generator, a point on the machine, and no cable between them
    b.b(2, 0, 4, "powah:furnator_starter[facing=south]")
    b.b(2, 1, 4, "fluxnetworks:flux_plug")
    b.b(7, 0, 4, "mekanism:enrichment_chamber[facing=south]")
    b.b(7, 1, 4, "fluxnetworks:flux_point")


@scene("nuclearcraft/reactor", w=11, d=11)
def _(b):
    # the first fission reactor, opened by a front of glass: a fuel cell in the middle, graphite
    # on two sides of it, water heat sinks on the other four; controller and port in the wall
    x0, z0 = 3, 3
    for x in range(5):
        for y in range(5):
            for z in range(5):
                on = sum((x in (0, 4), y in (0, 4), z in (0, 4)))
                if on == 0:
                    continue
                front = on == 1 and z == 4
                b.b(x0 + x, y, z0 + z, "nuclearcraft:fission_reactor_glass" if front else "nuclearcraft:fission_reactor_casing")
    b.b(x0 + 1, 1, z0 + 4, "nuclearcraft:fission_reactor_controller[facing=south]")
    b.b(x0 + 3, 1, z0 + 4, "nuclearcraft:fission_reactor_port")
    b.b(x0 + 2, 2, z0 + 2, "nuclearcraft:fission_reactor_solid_fuel_cell")
    for dx in (-1, 1):
        b.b(x0 + 2 + dx, 2, z0 + 2, "nuclearcraft:graphite_block")
    for dy, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        b.b(x0 + 2, 2 + dy, z0 + 2 + dz, "nuclearcraft:water_heat_sink")



# ===================================================================================
# Eighth batch: the first farms

@scene("farms/cobble_drill")
def _(b):
    # the generator one block up: water, the hole that swallows it, the stone, lava. The drill
    # sits behind the stone, a belt under the stone carries what it breaks toward the camera.
    for x in range(1, 8):
        b.b(x, 0, 3, "minecraft:stone_bricks")
        b.b(x, 1, 3, "minecraft:stone_bricks")
        b.b(x, 1, 5, "minecraft:glass")
        if x != 5:
            b.b(x, 0, 5, "minecraft:stone_bricks")
            b.b(x, 0, 4, "minecraft:stone_bricks")
    b.b(1, 1, 4, "minecraft:stone_bricks")
    b.b(7, 1, 4, "minecraft:stone_bricks")
    b.b(4, 0, 4, "minecraft:air")
    b.b(4, -1, 4, "minecraft:air")                     # the water falls in here and goes no further
    b.b(5, 0, 4, "create:shaft[axis=x]")
    b.b(5, 0, 7, "create:shaft[axis=x]")
    b.use(5, 0, 4, "up", "create:belt_connector")
    b.use(5, 0, 7, "up", "create:belt_connector")
    b.changed(5, 0, 5, "minecraft:air")
    motor(b, 6, 0, 4, "west", 16)                      # in the base under the lava, out of sight
    b.b(2, 1, 4, "minecraft:water")
    b.b(5, 1, 4, "minecraft:cobblestone")
    b.b(6, 1, 4, "minecraft:lava")
    b.b(5, 1, 3, "create:mechanical_drill[facing=south,waterlogged=false]")
    drive_from_behind(b, 5, 1, 3)


@scene("farms/crops_essence")
def _(b):
    # cut open at the front: two growth accelerators under every block of inferium farmland,
    # the grown inferium on top, the water that keeps the field wet in its middle
    for x in range(2, 7):
        for z in range(3, 6):
            b.f(x, 0, z, x, 1, z, "mysticalagriculture:inferium_growth_accelerator")
            if (x, z) == (4, 4):
                b.b(x, 2, z, "minecraft:water")
            else:
                b.b(x, 2, z, "mysticalagriculture:inferium_farmland[moisture=7]")
                b.b(x, 3, z, "mysticalagriculture:inferium_crop[age=7]")


@scene("farms/source_berries", w=11)
def _(b):
    # two rows of sourceberry bushes, the agronomic sourcelink and a jar between them, the
    # imbuement chamber within two blocks of the jar, a Starbuncle for the harvest
    stage(b, 1, 2, 9, 6, "minecraft:grass_block")
    for x in range(2, 9):
        b.b(x, 0, 3, "ars_nouveau:sourceberry_bush[age=3]")
        b.b(x, 0, 5, "ars_nouveau:sourceberry_bush[age=3]")
    b.b(4, 0, 4, "ars_nouveau:agronomic_sourcelink")
    b.b(6, 0, 4, "ars_nouveau:source_jar[fill=8]", "{source:7000}")
    b.b(8, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    b.m("ars_nouveau:starbuncle", 2, 0, 4)



# ===================================================================================
# Ninth batch

@scene("ae2/cpu")
def _(b):
    # a crafting CPU: a full box of two by two by two, storage and a monitor in the front, a
    # co-processor beside the monitor, plain units behind. A creative cell under the floor
    # stands in for the network it would hang on.
    b.b(3, -1, 5, "ae2:creative_energy_cell")
    b.f(3, 0, 4, 4, 1, 4, "ae2:crafting_unit[formed=false]")
    b.f(3, 0, 5, 4, 0, 5, "ae2:1k_crafting_storage[formed=false]")
    b.b(3, 1, 5, "ae2:crafting_monitor[facing=south,formed=false]")
    b.b(4, 1, 5, "ae2:crafting_accelerator[formed=false]")
    b.later(3, 0, 5, "block @ ae2:1k_crafting_storage[formed=true]")


@scene("ae2/autocraft")
def _(b):
    # the pattern provider with molecular assemblers set directly against it
    b.b(4, -1, 4, "ae2:creative_energy_cell")
    b.b(4, 0, 4, "ae2:pattern_provider[push_direction=all]")
    b.b(3, 0, 4, "ae2:molecular_assembler")
    b.b(5, 0, 4, "ae2:molecular_assembler")
    b.b(4, 1, 4, "ae2:molecular_assembler")


@scene("enderio/cap_bank")
def _(b):
    # capacitor banks set side by side are one store
    b.f(3, 0, 4, 5, 2, 4, "enderio:basic_capacitor_bank")


@scene("pneumaticcraft/refinery", d=13, h=20)
def _(b):
    # the refinery's controller, four outputs stacked on it: the lighter the product, the higher its output.
    # It stands at the back of a deep cell: a tall thing needs the camera far off.
    b.b(4, 0, 3, "pneumaticcraft:refinery[facing=south]")
    for y in range(1, 5):
        b.b(4, y, 3, "pneumaticcraft:refinery_output[facing=south]")
    b.focus(3, 0, 2, 5, 5, 4)


@scene("list_power/mek_heat")
def _(b):
    # a heat generator in a basin of lava: lava on every side of it but the one with the window
    for x in range(2, 7):
        for z in range(2, 7):
            edge = x in (2, 6) or z in (2, 6)
            if edge:
                b.b(x, 0, z, "minecraft:glass" if z == 6 else "minecraft:stone_bricks")
            elif (x, z) == (4, 4):
                b.b(x, 0, z, "mekanismgenerators:heat_generator[facing=south]")
            elif (x, z) == (4, 5):
                b.b(x, 0, z, "minecraft:glass")
            else:
                b.b(x, 0, z, "minecraft:lava")



@scene("hostile_networks/data_center", w=11, d=11, h=20)
def _(b):
    # the shell as DataCenterShell checks it: seven by seven by seven, the whole bottom layer
    # obsidian, walls and the whole top layer black glass, hollow inside; the controller takes
    # the place of a wall block in the row above the floor and looks out
    x0, z0 = 2, 2
    b.f(x0, 0, z0, x0 + 6, 0, z0 + 6, "minecraft:obsidian")
    b.f(x0, 6, z0, x0 + 6, 6, z0 + 6, "minecraft:black_stained_glass")
    for x in range(7):
        for z in range(7):
            if x in (0, 6) or z in (0, 6):
                b.f(x0 + x, 1, z0 + z, x0 + x, 5, z0 + z, "minecraft:black_stained_glass")
    b.b(x0 + 3, 1, z0 + 6, "hostilenetworks:data_center[facing=south]")



# ===================================================================================
# Tenth batch

def totem(b, x, z, wood, spirits):
    """A Malum totem: the base, a log of its wood for every rune, each rune carved with a click
    of its arcanum on the log, from the bottom up."""
    b.b(x, 0, z, f"malum:{wood}_totem_base")
    for i, spirit in enumerate(spirits):
        b.b(x, 1 + i, z, f"malum:{wood}_log[axis=y]")
        b.use(x, 1 + i, z, "south", f"malum:{spirit}_spirit")
        b.changed(x, 1 + i, z, f"malum:{wood}_log")


@scene("malum/healing_rite")
def _(b):
    # the Rite of Healing: runewood on the base, one arcane and two sacred runes
    totem(b, 4, 4, "runewood", ["arcane", "sacred", "sacred"])


@scene("malum/quickening", d=13, h=20)
def _(b):
    # the Rite of Quickening: the same kind of totem of soulwood, eldritch, arcane and two infernal runes
    totem(b, 4, 3, "soulwood", ["eldritch", "arcane", "infernal", "infernal"])
    b.focus(3, 0, 2, 5, 5, 4)


@scene("pneumaticcraft/elevator", d=13, h=20)
def _(b):
    # the elevator base, four frames stacked on it, a caller at the upper floor
    b.b(4, 0, 3, "pneumaticcraft:elevator_base")
    b.f(4, 1, 3, 4, 4, 3, "pneumaticcraft:elevator_frame")
    b.f(5, 0, 3, 5, 3, 3, "minecraft:stone_bricks")
    b.b(5, 4, 3, "pneumaticcraft:elevator_caller[facing=south]")
    b.focus(3, 0, 2, 6, 5, 4)


@scene("list_gear/mek_jetpack")
def _(b):
    b.stand(4, 0, 4, armor=(None, "mekanism:jetpack"), rot=20)   # its back to the camera: the jetpack is worn there


@scene("list_power/nc_passive", w=11)
def _(b):
    # the four solar panels under the open sky and the four RTGs, weakest on the left
    for i, name in enumerate(("solar_panel_basic", "solar_panel_advanced", "solar_panel_du", "solar_panel_elite")):
        b.b(2 + 2 * i, 0, 3, f"nuclearcraft:{name}")
    for i, name in enumerate(("uranium_rtg", "americium_rtg", "plutonium_rtg", "californium_rtg")):
        b.b(2 + 2 * i, 0, 5, f"nuclearcraft:{name}")


@scene("list_power/alternator")
def _(b):
    # a shaft into the alternator's back makes current; the motor that turns the shaft stands in for a water wheel
    b.b(4, 0, 4, "createaddition:alternator[facing=east]")
    b.b(3, 0, 4, "create:shaft[axis=x]")
    housed_motor(b, 2, 0, 4, "east", 64)


# ===================================================================================
# Eleventh batch: Powah's small machines, Ender IO, AE2 beyond the first network, Hostile
# Neural Networks, and what the list chapters still lacked

@scene("powah/furnator")
def _(b):
    # the furnator burns, the cell beside it takes the current
    b.b(3, 0, 4, "powah:furnator_starter[facing=south]")
    b.b(4, 0, 4, "powah:energy_cell_starter")
    b.c(5, 0, 4, ["minecraft:coal"] * 3)


@scene("powah/power_plant")
def _(b):
    # two blazing furnators feed the blazing cell between them
    b.b(3, 0, 4, "powah:furnator_blazing[facing=south]")
    b.b(4, 0, 4, "powah:energy_cell_blazing")
    b.b(5, 0, 4, "powah:furnator_blazing[facing=south]")
    b.b(4, 1, 4, "powah:furnator_blazing[facing=south]")


@scene("powah/ender_cell", w=11)
def _(b):
    # two ender cells on one channel: one at the generator, one far off at the machine
    b.b(2, 0, 4, "powah:furnator_starter[facing=south]")
    b.b(3, 0, 4, "powah:ender_cell_starter")
    b.b(7, 0, 4, "powah:ender_cell_starter")
    b.b(8, 0, 4, "minecraft:redstone_lamp[lit=true]")


@scene("powah/transmitter")
def _(b):
    # the player transmitter stands two blocks high on a cell
    b.b(4, 0, 4, "powah:energy_cell_starter")
    b.b(4, 1, 4, "powah:player_transmitter_starter[top=false]")
    b.b(4, 2, 4, "powah:player_transmitter_starter[top=true]")


@scene("enderio/smelter", w=10)
def _(b):
    # the three first machines side by side, lit: alloy smelter, SAG mill, and a chest for what comes out
    b.b(3, 0, 4, "enderio:alloy_smelter[facing=south,powered=true]")
    b.b(5, 0, 4, "enderio:sag_mill[facing=south,powered=true]")
    b.show(7, 0, 4, "enderio:basic_capacitor")


@scene("enderio/soul_binder")
def _(b):
    b.b(3, 0, 4, "enderio:soul_binder[facing=south,powered=true]")
    b.show(5, 0, 4, "enderio:soul_vial")


@scene("enderio/vacuum_chest")
def _(b):
    # what lies near the vacuum chest flies to it
    b.b(4, 0, 4, "enderio:vacuum_chest")
    for x, z, item in ((2, 5, "minecraft:rotten_flesh"), (6, 5, "minecraft:bone"), (3, 6, "minecraft:gunpowder"), (5, 3, "minecraft:string")):
        b.drop(x, 0.2, z, item, 8)
    b.focus(2, 0, 3, 6, 1, 6)


@scene("enderio/enchanter")
def _(b):
    b.b(4, 0, 4, "enderio:enchanter[facing=south]")


@scene("list_dimensions/r_enderio")
def _(b):
    # two travel anchors: sneak on one, look at the other
    b.b(2, 0, 5, "enderio:travel_anchor")
    b.f(6, 0, 3, 6, 2, 3, "minecraft:stone_bricks")
    b.b(6, 3, 3, "enderio:travel_anchor")


@scene("list_dimensions/r_plates")
def _(b):
    # two warp plates tuned to each other
    b.b(2, 0, 4, "waystones:warp_plate[status=idle]")
    b.b(6, 0, 4, "waystones:warp_plate[status=idle]")
    b.focus(1, 0, 3, 7, 1, 5)


@scene("ae2/meteorite")
def _(b):
    # the heart of a meteorite: sky stone around the mysterious cube, certus growing on budding quartz
    b.f(1, -1, 1, 7, -1, 7, "ae2:sky_stone_block")
    b.f(1, 0, 1, 7, 1, 1, "ae2:sky_stone_block")
    b.f(1, 0, 2, 1, 1, 4, "ae2:sky_stone_block")
    b.f(7, 0, 2, 7, 1, 4, "ae2:sky_stone_block")
    b.f(1, 0, 5, 1, 0, 6, "ae2:sky_stone_block")
    b.f(7, 0, 5, 7, 0, 6, "ae2:sky_stone_block")
    b.b(4, 0, 4, "ae2:mysterious_cube")
    b.b(2, 0, 2, "ae2:flawless_budding_quartz")
    b.b(2, 1, 2, "ae2:quartz_cluster[facing=up,waterlogged=false]")
    b.b(2, 0, 3, "ae2:quartz_cluster[facing=south,waterlogged=false]")
    b.b(6, 0, 2, "ae2:flawless_budding_quartz")
    b.b(6, 1, 2, "ae2:quartz_cluster[facing=up,waterlogged=false]")
    b.b(5, 0, 2, "ae2:quartz_cluster[facing=west,waterlogged=false]")


@scene("ae2/presses", w=10)
def _(b):
    # the four presses out of the mysterious cube
    for i, name in enumerate(("silicon_press", "logic_processor_press", "calculation_processor_press", "engineering_processor_press")):
        b.show(2 + 2 * i, 0, 4, f"ae2:{name}")


@scene("ae2/inscriber")
def _(b):
    # the inscriber on the network's cable, a charger beside it
    b.b(3, -1, 4, "ae2:creative_energy_cell")
    b.b(3, 0, 4, "ae2:inscriber[facing=south,spin=0]")
    b.b(5, 0, 4, "ae2:charger[facing=south,spin=0]")
    b.use(3, 0, 4, "east", "ae2:fluix_glass_cable")


@scene("ae2_advanced/bridge", w=13)
def _(b):
    # both ends of a quantum bridge: eight rings around the link chamber, the cable on a side ring
    for cx in (3, 9):
        b.f(cx - 1, 0, 4, cx + 1, 2, 4, "ae2:quantum_ring")
        b.b(cx, 1, 4, "ae2:quantum_link")
    b.formed(3, 1, 4)


@scene("ae2_advanced/spatial", w=11, d=11)
def _(b):
    # a cage of spatial pylons: every edge of the space that is cut out, and the port that does it
    x1, y1, z1, x2, y2, z2 = 3, 0, 3, 7, 4, 7
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                if (x in (x1, x2)) + (y in (y1, y2)) + (z in (z1, z2)) >= 2:
                    b.b(x, y, z, "ae2:spatial_pylon")
    b.b(2, 0, 7, "ae2:spatial_io_port[facing=south,spin=0,powered=false]")


@scene("ae2_advanced/reaction")
def _(b):
    b.b(4, 0, 4, "advanced_ae:reaction_chamber[working=true]")


@scene("ae2_advanced/matrix", w=10)
def _(b):
    # four by three by three: frame on the edges, glass in front, wall elsewhere, a pattern core and a craft core inside
    x1, y1, z1, x2, y2, z2 = 3, 0, 3, 6, 2, 5
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                n = (x in (x1, x2)) + (y in (y1, y2)) + (z in (z1, z2))
                if n >= 2:
                    b.b(x, y, z, "extendedae:assembler_matrix_frame")
                elif n == 1:
                    b.b(x, y, z, "extendedae:assembler_matrix_glass" if z == z2 else "extendedae:assembler_matrix_wall")
    b.b(4, 1, 4, "extendedae:assembler_matrix_pattern")
    b.b(5, 1, 4, "extendedae:assembler_matrix_crafter")


@scene("hostile_networks/sim_chamber")
def _(b):
    # the two machines of the mod: the simulation chamber makes predictions, the loot fabricator turns them into drops
    b.b(3, 0, 4, "hostilenetworks:sim_chamber[facing=south]")
    b.b(5, 0, 4, "hostilenetworks:loot_fabricator[facing=south]")


@scene("hostile_networks/scaling", w=11)
def _(b):
    # one model per chamber: more output means more chambers in a row
    for x in range(2, 9):
        b.b(x, 0, 4, "hostilenetworks:sim_chamber[facing=south]")
    b.b(5, 0, 6, "hostilenetworks:loot_fabricator[facing=south]")


@scene("list_transport/packages")
def _(b):
    # the packager sits on the barrel it empties and hands its packages to the belt in front
    b.b(4, 0, 3, "minecraft:barrel[facing=up]")
    b.b(4, 0, 4, "create:packager[facing=south,linked=false,powered=false]")
    b.b(2, 0, 5, "create:shaft[axis=z]")
    b.b(6, 0, 5, "create:shaft[axis=z]")
    b.use(2, 0, 5, "up", "create:belt_connector")
    b.use(6, 0, 5, "up", "create:belt_connector")
    b.changed(4, 0, 5, "minecraft:air")
    b.drop(4, 1, 5, "create:cardboard_package_10x12")
    b.drop(5, 1, 5, "create:cardboard_package_10x8")


@scene("list_transport/hose_pulley", h=14)
def _(b):
    # a gantry over a pond: the pulley lets its hose down into the water
    b.f(3, -2, 3, 5, -1, 5, "minecraft:water")
    b.f(1, 0, 4, 1, 2, 4, "minecraft:spruce_log[axis=y]")
    b.f(7, 0, 4, 7, 2, 4, "minecraft:spruce_log[axis=y]")
    b.f(1, 3, 4, 7, 3, 4, "minecraft:spruce_planks")
    b.b(4, 3, 4, "create:hose_pulley[facing=south]")     # its shaft runs east to west then (HosePulleyBlock.getRotationAxis)
    housed_motor(b, 3, 3, 4, "east", 32)


@scene("list_power/mekmm_large", w=13)
def _(b):
    # the large heat generator and the large gas burning generator, set down the way a player sets
    # them. (The large wind generator is a tower no picture of this size holds.)
    b.use(3, -1, 4, "up", "mekmm:large_heat_generator")
    b.use(9, -1, 4, "up", "mekmm:large_gas_burning_generator")
    b.focus(1, 0, 3, 11, 3, 5)


@scene("list_gear/wyvern")
def _(b):
    b.stand(3, 0, 4, armor=(None, "draconicevolution:wyvern_chestpiece"), hand="draconicevolution:wyvern_sword")
    b.stand(5, 0, 4, hand="draconicevolution:wyvern_pickaxe")


@scene("list_gear/sg_end")
def _(b):
    # azure silver ore in end stone, and the two alloys forged from it
    b.f(3, 0, 3, 5, 1, 3, "minecraft:end_stone")
    b.b(4, 0, 3, "silentgear:azure_silver_ore")
    b.b(5, 1, 3, "silentgear:azure_silver_ore")
    b.show(3, 0, 5, "silentgear:azure_electrum_ingot")
    b.show(5, 0, 5, "silentgear:tyrian_steel_ingot")



# ===================================================================================
# Twelfth batch: the Aether's three stations, Silent Gear's benches, the kitchen, Theurgy,
# quarries

@scene("aether/altar")
def _(b):
    # altar, freezer and incubator on holystone
    stage(b, 2, 3, 6, 5, "aether:holystone")
    b.b(2, 0, 4, "aether:altar")
    b.b(4, 0, 4, "aether:freezer")
    b.b(6, 0, 4, "aether:incubator")


@scene("undergarden/infuser")
def _(b):
    stage(b, 3, 3, 5, 5, "undergarden:depthrock")
    b.b(4, 0, 4, "undergarden:infuser[state=infusing_utherium]")


@scene("deeper_darker/resonarium")
def _(b):
    b.stand(4, 0, 4, armor=("deeperdarker:resonarium_helmet", "deeperdarker:resonarium_chestplate",
                            "deeperdarker:resonarium_leggings", "deeperdarker:resonarium_boots"))


@scene("silent_gear/stone_anvil")
def _(b):
    b.b(3, 0, 4, "silentgear:stone_anvil")
    b.show(5, 0, 4, "silentgear:hammer")


@scene("silent_gear/crude_mixer")
def _(b):
    b.b(4, 0, 4, "silentgear:crude_mixer[facing=south,lit=true]")


@scene("silent_gear/alloy_forge")
def _(b):
    # the forge for the alloys, the starlight charger under the open sky beside it
    b.b(3, 0, 4, "silentgear:alloy_forge[facing=south,lit=true]")
    b.b(5, 0, 4, "silentgear:starlight_charger")


@scene("food/f_cutting_board")
def _(b):
    # a kitchen: the cutting board on a cabinet, the stove with the cooking pot on it
    b.b(3, 0, 4, "farmersdelight:oak_cabinet[facing=south,open=false]")
    b.b(3, 1, 4, "farmersdelight:cutting_board[facing=south]")
    b.b(4, 0, 4, "farmersdelight:stove[facing=south,lit=true]")
    b.b(4, 1, 4, "farmersdelight:cooking_pot[facing=south,support=tray]")
    b.b(5, 0, 4, "farmersdelight:oak_cabinet[facing=south,open=false]")


@scene("food/f_rice")
def _(b):
    # rice stands in water one block deep with earth under it, the panicles grow above
    b.f(2, -2, 3, 6, -2, 5, "minecraft:dirt")
    b.f(2, -1, 3, 6, -1, 5, "minecraft:water")
    for x in range(2, 7):
        for z in (3, 4, 5):
            if (x + z) % 4 != 1:
                b.b(x, -1, z, "farmersdelight:rice[age=3,supporting=true]")
                b.b(x, 0, z, "farmersdelight:rice_panicles[age=3]")
    b.focus(2, -1, 3, 6, 1, 5)


@scene("food/f_rich_soil")
def _(b):
    # compost on its way, with mushrooms around it that hurry it up, and the rich soil it becomes
    stage(b, 2, 3, 6, 5, "minecraft:podzol[snowy=false]")
    b.b(3, -1, 4, "farmersdelight:organic_compost[composting=2]")
    b.b(4, -1, 4, "farmersdelight:organic_compost[composting=6]")
    b.b(5, -1, 4, "farmersdelight:rich_soil")
    b.b(5, 0, 4, "farmersdelight:brown_mushroom_colony[age=3]")
    b.b(2, 0, 3, "minecraft:brown_mushroom")
    b.b(6, 0, 5, "minecraft:red_mushroom")
    b.focus(2, -1, 3, 6, 1, 5)


@scene("food/f_feast")
def _(b):
    # a feast is a block on the table
    b.f(3, 0, 4, 5, 0, 4, "minecraft:spruce_slab[type=top]")
    b.b(4, 1, 4, "farmersdelight:roast_chicken_block[facing=south,servings=4]")
    b.focus(3, 0, 3, 5, 2, 5)


@scene("food/f_market")
def _(b):
    b.b(4, 0, 4, "farmingforblockheads:market[facing=south,half=lower]")
    b.b(4, 1, 4, "farmingforblockheads:market[facing=south,half=upper]")


@scene("theurgy/sal_tank")
def _(b):
    # the accumulator stands on the tank
    b.b(4, 0, 4, "theurgy:sal_ammoniac_tank")
    b.b(4, 1, 4, "theurgy:sal_ammoniac_accumulator")


@scene("theurgy/liquefaction")
def _(b):
    # the cauldron on a lit brazier
    b.b(4, 0, 4, "theurgy:pyromantic_brazier[lit=true]")
    b.b(4, 1, 4, "theurgy:liquefaction_cauldron[half=lower,lit=true]")
    b.b(4, 2, 4, "theurgy:liquefaction_cauldron[half=upper,lit=true]")


@scene("theurgy/vessels")
def _(b):
    # the incubator on its brazier, salt, sulfur and mercury vessels right beside it
    b.b(4, 0, 4, "theurgy:pyromantic_brazier[lit=true]")
    b.b(4, 1, 4, "theurgy:incubator[half=lower]")
    b.b(4, 2, 4, "theurgy:incubator[half=upper]")
    for x, z, name in ((3, 4, "salt"), (5, 4, "sulfur"), (4, 3, "mercury")):
        b.b(x, 0, z, "minecraft:stone_bricks")
        b.b(x, 1, z, f"theurgy:incubator_{name}_vessel")


@scene("theurgy/array")
def _(b):
    # the emitter looks at the target pedestal, source and result stand close by
    b.b(2, 0, 4, "theurgy:reformation_source_pedestal")
    b.b(4, 0, 3, "theurgy:reformation_target_pedestal")
    b.b(6, 0, 4, "theurgy:reformation_result_pedestal")
    b.b(4, 0, 6, "minecraft:stone_bricks")
    b.b(4, 1, 6, "theurgy:sulfuric_flux_emitter[facing=up]")


@scene("theurgy/fermentation")
def _(b):
    b.b(4, 0, 4, "theurgy:fermentation_vat[facing=south,has_output=false,open=true]")


@scene("malum/crucible")
def _(b):
    # the crucible, set down by hand so its upper half stands
    b.use(4, -1, 4, "up", "malum:spirit_crucible")
    b.focus(3, 0, 3, 5, 2, 5)


@scene("storage/trash")
def _(b):
    # whatever the hopper drops into the trash can is gone
    b.b(4, 0, 4, "trashcans:item_trash_can")
    b.b(4, 1, 4, "minecraft:hopper[facing=down]")


@scene("storage/copper_tier")
def _(b):
    # the same barrel before and after the upgrade
    b.b(3, 0, 4, "sophisticatedstorage:barrel[facing=south,flat_top=false]")
    b.b(5, 0, 4, "sophisticatedstorage:copper_barrel[facing=south,flat_top=false]")


@scene("storage/welcome")
def _(b):
    b.b(4, 0, 4, "sophisticatedbackpacks:backpack[facing=south]")


@scene("quarries/first_dig")
def _(b):
    # the builder with the chest it fills
    b.b(4, 0, 4, "rftoolsbuilder:builder[facing=south]")
    b.b(4, 1, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")


@scene("quarries/quarry")
def _(b):
    # three markers span the area, the quarry stands beside the first
    b.b(3, 0, 5, "quarryplus:quarry[facing=south,working=false]")
    b.b(4, 0, 5, "quarryplus:marker[facing=up]")
    b.b(6, 0, 5, "quarryplus:marker[facing=up]")
    b.b(4, 0, 3, "quarryplus:marker[facing=up]")


@scene("quarries/destroyer")
def _(b):
    b.b(3, 0, 4, "quarryplus:adv_quarry[facing=south,working=false]")
    b.b(5, 0, 4, "quarryplus:chunk_marker")


@scene("quarries/coe_netherite")
def _(b):
    # the three drills, iron to netherite
    for i, name in enumerate(("drill", "diamond_drill", "netherite_drill")):
        b.show(2 + 2 * i, 0, 4, f"createoreexcavation:{name}")


@scene("draconic/dust")
def _(b):
    # draconium ore in end stone
    b.f(3, 0, 3, 5, 1, 4, "minecraft:end_stone")
    b.b(4, 0, 4, "draconicevolution:end_draconium_ore")
    b.b(5, 1, 4, "draconicevolution:end_draconium_ore")
    b.b(3, 1, 3, "draconicevolution:end_draconium_ore")


# ===================================================================================
# Thirteenth batch: PneumaticCraft's later machines, Oritech, Productive Trees, logistics

@scene("pneumaticcraft/vortex")
def _(b):
    # the vortex tube at the end of a pressure tube: one end gets hot, the other cold
    b.b(3, 0, 4, "pneumaticcraft:pressure_tube")
    b.b(4, 0, 4, "pneumaticcraft:pressure_tube")
    b.b(5, 0, 4, "pneumaticcraft:vortex_tube[facing=east]")


@scene("pneumaticcraft/plastic")
def _(b):
    # the thermopneumatic plant over magma: the heat is all it needs for plastic
    b.b(4, 0, 4, "minecraft:magma_block")
    b.b(4, 1, 4, "pneumaticcraft:thermopneumatic_processing_plant[facing=south]")


@scene("pneumaticcraft/etching")
def _(b):
    b.b(4, 0, 4, "pneumaticcraft:etching_tank")


@scene("pneumaticcraft_advanced/first_run")
def _(b):
    # the assembly line: the platform in the middle, drill and laser beside it, the two IO units on
    # the free sides with a chest behind each, the controller at the end of the row
    b.b(4, 0, 4, "pneumaticcraft:assembly_platform")
    b.b(3, 0, 4, "pneumaticcraft:assembly_drill")
    b.b(5, 0, 4, "pneumaticcraft:assembly_laser")
    b.b(4, 0, 3, "pneumaticcraft:assembly_io_unit_import")
    b.b(4, 0, 5, "pneumaticcraft:assembly_io_unit_export")
    b.b(4, 0, 2, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.b(4, 0, 6, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.b(6, 0, 4, "pneumaticcraft:assembly_controller")


@scene("pneumaticcraft_advanced/adv_air")
def _(b):
    b.b(4, 0, 4, "pneumaticcraft:advanced_air_compressor[facing=south,on=true]")


@scene("pneumaticcraft_advanced/thermal")
def _(b):
    # hot on one side, cold on the other: the thermal compressor between magma and ice
    b.b(3, 0, 4, "minecraft:magma_block")
    b.b(4, 0, 4, "pneumaticcraft:thermal_compressor")
    b.b(5, 0, 4, "minecraft:blue_ice")


@scene("pneumaticcraft_advanced/electrostatic")
def _(b):
    # the electrostatic compressor under a lightning rod on a mast of iron bars
    b.b(4, 0, 4, "pneumaticcraft:electrostatic_compressor")
    b.f(4, 1, 4, 4, 4, 4, "minecraft:iron_bars")
    b.b(4, 5, 4, "minecraft:lightning_rod[facing=up,powered=false]")


@scene("pneumaticcraft_advanced/security_station")
def _(b):
    b.b(4, 0, 4, "pneumaticcraft:security_station[facing=south]")


@scene("pneumaticcraft_advanced/spawner_extractor")
def _(b):
    # the extractor sits on the spawner it drains
    b.b(4, 0, 4, "minecraft:spawner")
    b.b(4, 1, 4, "pneumaticcraft:spawner_extractor")


@scene("pneumaticcraft_advanced/pressurized_spawner")
def _(b):
    b.b(4, 0, 4, "pneumaticcraft:pressurized_spawner")


@scene("oritech/cores")
def _(b):
    b.b(3, 0, 4, "oritech:machine_core_1")
    b.b(5, 0, 4, "oritech:machine_core_2")


@scene("oritech/laser", h=14)
def _(b):
    b.use(4, -1, 4, "up", "oritech:laser_arm_block")
    b.focus(4, 0, 4, 4, 1, 4)


@scene("oritech/atomic_forge")
def _(b):
    b.use(4, -1, 4, "up", "oritech:atomic_forge_block")
    b.focus(4, 0, 4, 4, 0, 4)


@scene("oritech/fragment_forge")
def _(b):
    b.use(4, -1, 4, "up", "oritech:fragment_forge_block")
    b.focus(4, 0, 4, 4, 0, 4)


@scene("oritech/destroyer", w=11, d=11)
def _(b):
    # a rectangle of machine frames over a field, the destroyer at its corner
    stage(b, 2, 2, 8, 8, "minecraft:farmland[moisture=7]")
    b.f(2, 0, 2, 8, 0, 8, "minecraft:wheat[age=7]")
    for x in range(2, 9):
        for z in range(2, 9):
            if x in (2, 8) or z in (2, 8):
                b.b(x, 2, z, "oritech:machine_frame_block")
    b.f(1, 0, 8, 1, 1, 8, "minecraft:stone_bricks")
    b.b(1, 2, 8, "oritech:destroyer_block[facing=south,machine_assembled=false]")


@scene("oritech/exo")
def _(b):
    b.stand(4, 0, 4, armor=("oritech:exo_helmet", "oritech:exo_chestplate", "oritech:exo_leggings", "oritech:exo_boots"))


@scene("productive_trees/sawmill_run")
def _(b):
    # sawmill and stripper, a hopper feeds the sawmill
    b.b(3, 0, 4, "productivetrees:sawmill")
    b.b(3, 1, 4, "minecraft:hopper[facing=down]")
    b.b(5, 0, 4, "productivetrees:stripper")


@scene("productive_trees/first_tree", h=14)
def _(b):
    # a walnut tree: the trunk, and a crown in which more than half the leaves bear fruit
    b.f(4, 0, 4, 4, 4, 4, "productivetrees:walnut_log[axis=y]")
    for y, r in ((3, 2), (4, 2), (5, 1), (6, 1)):
        for x in range(4 - r, 5 + r):
            for z in range(4 - r, 5 + r):
                if (x, z) == (4, 4) and y <= 4:
                    continue
                if r == 2 and abs(x - 4) == 2 and abs(z - 4) == 2:
                    continue
                leaf = "productivetrees:walnut_fruit[age=7]" if (x * 7 + y * 3 + z * 5) % 5 < 3 else "productivetrees:walnut_leaves"
                b.b(x, y, z, leaf)
    b.b(2, 0, 6, "productivetrees:walnut_sapling")


@scene("logistics/menril")
def _(b):
    # a menril trunk, the squeezer and the drying basin its resin runs into
    b.f(2, 0, 3, 2, 2, 3, "integrateddynamics:menril_log[axis=y]")
    b.b(4, 0, 4, "integrateddynamics:squeezer[axis=x,height=1]")
    b.b(5, 0, 4, "integrateddynamics:drying_basin")


@scene("logistics/programmer")
def _(b):
    b.b(3, 0, 4, "integrateddynamics:logic_programmer[facing=south]")
    b.b(5, 0, 4, "integrateddynamics:variablestore[facing=south]")


@scene("logistics/xnet_connectors", w=10)
def _(b):
    # a connector at the chest, cable from there to the controller, a connector at the furnace beyond
    b.b(2, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.b(8, 0, 4, "minecraft:furnace[facing=south,lit=false]")
    b.b(5, 0, 5, "xnet:controller[facing=south,error=false]")
    b.use(3, -1, 4, "up", "xnet:connector_blue")
    b.use(7, -1, 4, "up", "xnet:connector_blue")
    for x in (4, 5, 6):
        b.use(x, -1, 4, "up", "xnet:netcable_blue")
    b.focus(2, 0, 3, 8, 1, 5)


# ===================================================================================
# Fourteenth batch: Industrial Foregoing at work, two Create lines, a few single machines

@scene("industrial/extractor")
def _(b):
    # fluid extractors on both sides of an acacia trunk, each looking at a log
    b.f(4, 0, 4, 4, 3, 4, "minecraft:acacia_log[axis=y]")
    for y in (0, 1):
        b.b(3, y, 4, "industrialforegoing:fluid_extractor[subfacing=east]")
        b.b(5, y, 4, "industrialforegoing:fluid_extractor[subfacing=west]")


@scene("industrial/latex_unit")
def _(b):
    # the latex processing unit takes the latex of the extractors, the dissolution chamber stands for later
    b.b(3, 0, 4, "industrialforegoing:latex_processing_unit[subfacing=south]")
    b.b(5, 0, 4, "industrialforegoing:dissolution_chamber[subfacing=south]")


@scene("industrial/sower")
def _(b):
    # a field on posts: the sower under its middle plants it, the gatherer behind it reaps it
    for x, z in ((3, 3), (5, 3), (3, 5), (5, 5)):
        b.b(x, 0, z, "minecraft:oak_log[axis=y]")
    b.b(4, 0, 4, "industrialforegoing:plant_sower[subfacing=south]")
    b.f(3, 1, 3, 5, 1, 5, "minecraft:farmland[moisture=7]")
    b.f(3, 2, 3, 5, 2, 5, "minecraft:wheat[age=7]")
    b.f(4, 0, 2, 4, 1, 2, "minecraft:stone_bricks")
    b.b(4, 2, 2, "industrialforegoing:plant_gatherer[subfacing=south]")


@scene("industrial/crusher")
def _(b):
    # a pen of cows: the duplicator makes them, the crusher behind the pen kills them for their drops
    for x in range(2, 7):
        for z in (3, 6):
            b.b(x, 0, z, "minecraft:oak_fence")
    for z in (4, 5):
        b.b(2, 0, z, "minecraft:oak_fence")
        b.b(6, 0, z, "minecraft:oak_fence")
    b.m("minecraft:cow", 3, 0, 4)
    b.m("minecraft:cow", 5, 0, 5)
    b.b(4, 0, 2, "industrialforegoing:mob_crusher[subfacing=south]")
    b.b(7, 0, 4, "industrialforegoing:mob_duplicator")


@scene("industrial/bio")
def _(b):
    b.b(4, 0, 4, "industrialforegoing:bioreactor[subfacing=south]")


@scene("industrial/laser")
def _(b):
    # the ore laser base, a laser drill on every side looking at it across one block of air
    b.b(4, 0, 4, "industrialforegoing:ore_laser_base")
    b.b(2, 0, 4, "industrialforegoing:laser_drill[facing=east]")
    b.b(6, 0, 4, "industrialforegoing:laser_drill[facing=west]")
    b.b(4, 0, 2, "industrialforegoing:laser_drill[facing=south]")


@scene("industrial/washing", w=10)
def _(b):
    # the three machines of the ore meat line side by side
    for i, name in enumerate(("washing_factory", "fermentation_station", "fluid_sieving_machine")):
        b.b(3 + 2 * i, 0, 4, f"industrialforegoing:{name}[subfacing=south]")


@scene("industrial/conveyor", w=10)
def _(b):
    # a conveyor line with what it carries
    for x in range(2, 8):
        b.b(x, 0, 4, "industrialforegoing:conveyor[facing=east,type=flat]")
    for x in (3, 5, 6):
        b.drop(x, 0.4, 4, "minecraft:raw_iron")
    b.focus(2, 0, 3, 7, 1, 5)


@scene("mekanism/ethene")
def _(b):
    b.b(4, 0, 4, "mekanism:pressurized_reaction_chamber[facing=south]")


@scene("antimatter/wind", d=13, h=20)
def _(b):
    # the wind generator, set down the way a player sets it: five blocks high with its rotor
    b.use(4, -1, 3, "up", "mekanismgenerators:wind_generator")
    b.focus(3, 0, 2, 5, 5, 4)


@scene("botania_runes/thermalily")
def _(b):
    # the thermalily drinks the lava beside it
    stage(b, 2, 3, 6, 5, "minecraft:grass_block[snowy=false]")
    b.b(5, -1, 4, "minecraft:lava")
    b.b(4, 0, 4, "botania:thermalily")
    b.focus(3, -1, 3, 6, 1, 5)


@scene("botania_runes/gourmaryllis")
def _(b):
    # the gourmaryllis eats what lies near it, and wants a different food every time
    stage(b, 2, 3, 6, 5, "minecraft:grass_block[snowy=false]")
    b.b(4, 0, 4, "botania:gourmaryllis")
    for x, z, item in ((3, 5, "minecraft:bread"), (5, 5, "minecraft:cooked_beef"), (3, 3, "minecraft:apple"), (5, 3, "minecraft:baked_potato")):
        b.drop(x, 0.2, z, item)
    b.focus(3, 0, 3, 5, 1, 5)


@scene("productive_trees/mega")
def _(b):
    # four saplings in a square: the pecan only grows like this
    stage(b, 3, 3, 6, 6, "minecraft:grass_block[snowy=false]")
    for x in (4, 5):
        for z in (4, 5):
            b.b(x, 0, z, "productivetrees:pecan_sapling")
    b.focus(3, 0, 3, 6, 1, 6)


@scene("create_brass/blaze_cake", w=11)
def _(b):
    # two steps: the press over a basin of egg, sugar and cinder flour makes the base,
    # the spout over the depot fills it with lava
    b.b(3, 0, 4, "create:basin[facing=down]")
    b.b(3, 2, 4, "create:mechanical_press[facing=south]")
    drive_from_behind(b, 3, 2, 4)
    b.drop(3, 1, 4, "minecraft:egg")
    b.drop(3, 1.2, 4, "minecraft:sugar")
    b.drop(3, 1.4, 4, "create:cinder_flour")
    b.b(7, 0, 4, "create:depot")
    b.b(7, 2, 4, "create:spout")
    b.b(7, 3, 4, "create:fluid_tank[bottom=true,shape=window,top=true]")
    b.use(7, 0, 4, "up", "create:blaze_cake_base")


@scene("create_brass/incomplete", w=11)
def _(b):
    # sequenced assembly: the plate rides the belt under three deployers, each holding its part, and a press
    b.b(2, 0, 4, "create:shaft[axis=z]")
    b.b(8, 0, 4, "create:shaft[axis=z]")
    b.use(2, 0, 4, "up", "create:belt_connector")
    b.use(8, 0, 4, "up", "create:belt_connector")
    b.changed(5, 0, 4, "minecraft:air")
    for x, item in ((3, "create:cogwheel"), (4, "create:large_cogwheel"), (5, "minecraft:iron_nugget")):
        b.b(x, 2, 4, "create:deployer[facing=down,axis_along_first=true]", f'{{HeldItem:{{id:"{item}",count:1}}}}')
    b.b(7, 2, 4, "create:mechanical_press[facing=south]")
    b.f(3, 3, 4, 7, 3, 4, "create:andesite_casing")
    b.drop(6, 1, 4, "create:incomplete_precision_mechanism")


# ===================================================================================
# Fifteenth batch: farms that turn

def turning_arm(b, cx, cz, reach, speed=8):
    """A mechanical bearing in the floor, looking up, with an arm of linear chassis across it:
    reach blocks to either side. The motor sits under the bearing. The arm is put together with
    a click on the bearing, after whatever rides on it has been set."""
    b.b(cx, -1, cz, "create:mechanical_bearing[facing=up]")
    motor(b, cx, -2, cz, "up", speed)
    for x in range(cx - reach, cx + reach + 1):
        ends = "true" if abs(x - cx) == reach else "false"
        b.b(x, 0, cz, f"create:linear_chassis[axis=x,sticky_bottom={ends},sticky_top={ends}]")


@scene("farms/crops_harvester", w=11, d=11)
def _(b):
    # a round wheat field, the arm sweeps it: harvesters on the arm's sides, blades forward
    cx = cz = 5
    for x in range(1, 10):
        for z in range(1, 10):
            r2 = (x - cx) ** 2 + (z - cz) ** 2
            if r2 <= 13:
                b.b(x, -1, z, "minecraft:farmland[moisture=7]")
                b.b(x, 0, z, "minecraft:wheat[age=7]")
    for x, z in ((cx - 4, cz), (cx + 4, cz), (cx, cz - 4), (cx, cz + 4)):
        b.b(x, -1, z, "minecraft:water")
    turning_arm(b, cx, cz, 2)
    for x in (cx + 1, cx + 2):
        b.b(x, 0, cz + 1, "create:mechanical_harvester[facing=south,waterlogged=false]")
    for x in (cx - 1, cx - 2):
        b.b(x, 0, cz - 1, "create:mechanical_harvester[facing=north,waterlogged=false]")
    b.use(cx, -1, cz, "up", "minecraft:air")
    b.later(cx + 2, 0, cz, "block @ create:linear_chassis", unless=True)     # the arm left the world: it turns
    b.focus(1, 0, 1, 9, 1, 9)


@scene("farms/wood_saw", w=11, d=11)
def _(b):
    # a ring of saplings, the arm's saws pass through where their trunks will stand
    cx = cz = 5
    for x in range(0, 11):
        for z in range(0, 11):
            if (x - cx) ** 2 + (z - cz) ** 2 <= 22:
                b.b(x, -1, z, "minecraft:grass_block[snowy=false]")
    for x, z in ((cx, cz - 4), (cx, cz + 4), (cx + 3, cz + 3), (cx - 3, cz - 3), (cx + 3, cz - 3), (cx - 3, cz + 3)):
        b.b(x, 0, z, "minecraft:oak_sapling")
    turning_arm(b, cx, cz, 3)
    b.b(cx + 4, 0, cz, "create:mechanical_saw[facing=south,axis_along_first=false,flipped=false]")
    b.b(cx - 4, 0, cz, "create:mechanical_saw[facing=north,axis_along_first=false,flipped=false]")
    b.use(cx, -1, cz, "up", "minecraft:air")
    b.later(cx + 3, 0, cz, "block @ create:linear_chassis", unless=True)
    b.focus(1, 0, 1, 9, 1, 9)


# ===================================================================================
# Sixteenth batch: more Ars Nouveau, Flux Networks in place, two IE singles

@scene("ars_master/wilden_ritual")
def _(b):
    # the wilden summon on the brazier, spike, horn and wing on pedestals around it
    b.b(4, 0, 4, "ars_nouveau:ritual_brazier")
    b.use(4, 0, 4, "up", "ars_nouveau:ritual_wilden_summon")
    for (x, z), item in (((2, 4), "ars_nouveau:wilden_spike"), ((6, 4), "ars_nouveau:wilden_horn"), ((4, 2), "ars_nouveau:wilden_wing")):
        b.b(x, 0, z, "ars_nouveau:arcane_pedestal[facing=up]")
        b.use(x, 0, z, "south", item)


@scene("ars_master/charged_certus")
def _(b):
    # redstone and glowstone on pedestals beside the chamber, the certus crystal in it
    b.b(4, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    for (x, z), item in (((3, 4), "minecraft:redstone"), ((5, 4), "minecraft:glowstone_dust")):
        b.b(x, 0, z, "ars_nouveau:arcane_pedestal[facing=up]")
        b.use(x, 0, z, "south", item)
    b.use(4, 0, 4, "south", "ae2:certus_quartz_crystal")
    b.b(6, 0, 3, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("ars_master/alteration")
def _(b):
    # the alteration table, set down by hand so both its halves stand, and a robe to work on
    b.use(3, -1, 4, "up", "ars_nouveau:alteration_table")
    b.stand(6, 0, 4, armor=("ars_nouveau:arcanist_hood", "ars_nouveau:arcanist_robes", "ars_nouveau:arcanist_leggings", "ars_nouveau:arcanist_boots"))
    b.focus(2, 0, 3, 6, 2, 5)


@scene("ars_apprentice/potions")
def _(b):
    # potion jars beside the wixie cauldron, the alchemical sourcelink that drinks from them
    b.b(4, 0, 4, "ars_nouveau:wixie_cauldron[converted=true,filled=true]")
    b.b(2, 0, 4, "ars_nouveau:potion_jar[fill=11]")
    b.b(3, 0, 4, "ars_nouveau:potion_jar[fill=6]")
    b.b(6, 0, 4, "ars_nouveau:alchemical_sourcelink")


@scene("ars_apprentice/turret")
def _(b):
    # a spell turret looking at the block a cobblestone generator keeps making
    b.b(4, 0, 5, "ars_nouveau:basic_spell_turret")
    b.b(4, 0, 3, "minecraft:cobblestone")
    b.b(3, 0, 3, "minecraft:water")
    b.b(5, 0, 3, "minecraft:lava")
    b.f(2, 0, 2, 6, 0, 2, "minecraft:stone_bricks")
    b.b(2, 0, 3, "minecraft:stone_bricks")
    b.b(6, 0, 3, "minecraft:stone_bricks")
    b.b(3, 0, 4, "minecraft:glass")
    b.b(5, 0, 4, "minecraft:glass")


@scene("ars_apprentice/source_motor")
def _(b):
    # the source motor turns a shaft from the jar beside it
    b.b(3, 0, 4, "ars_technica:source_motor[facing=east]")
    b.f(4, 0, 4, 6, 0, 4, "create:shaft[axis=x]")
    b.b(3, 0, 3, "ars_nouveau:source_jar[fill=11]", "{source:10000}")


@scene("flux_networks/setup_reactor")
def _(b):
    # a plug on the reactor takes all it makes into the network
    b.b(4, 0, 4, "powah:reactor_starter[core=true]")
    b.b(4, 4, 4, "fluxnetworks:flux_plug")
    b.focus(3, 0, 3, 5, 4, 5)


@scene("flux_networks/setup_mek", w=10)
def _(b):
    # a row of machines without a single cable: a flux point on each
    mek_row(b, ["enrichment_chamber", "crusher", "energized_smelter", "metallurgic_infuser"], 3, 4)
    for x in range(3, 7):
        b.b(x, 1, 4, "fluxnetworks:flux_point")


@scene("immersive_heavy/survey", h=14)
def _(b):
    # the core sample drill, set down by hand: three blocks high
    b.use(4, -1, 4, "up", "immersiveengineering:sample_drill")
    b.focus(3, 0, 3, 5, 3, 5)


@scene("immersive/bench", w=10)
def _(b):
    # the engineer's workbench is two blocks wide
    b.use(4, -1, 4, "up", "immersiveengineering:workbench")
    b.focus(3, 0, 3, 6, 1, 5)


@scene("create_brass/arm")
def _(b):
    # the mechanical arm takes coal from the depot and feeds the blaze burner: where it takes
    # and where it gives is what a player clicks before setting the arm down
    b.b(2, 0, 4, "create:depot")
    b.use(2, 0, 4, "up", "minecraft:coal")
    b.b(6, 0, 4, "create:blaze_burner[blaze=smouldering]")
    b.b(4, 0, 4, "create:mechanical_arm[ceiling=false]",
        '{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}')
    drive_from_below(b, 4, 0, 4)


# ===================================================================================
# Seventeenth batch: things set and filled by hand

@scene("immersive/cloche", h=14)
def _(b):
    # the garden cloche, set down by hand (three blocks high), with earth, a hemp seed, water and
    # power in it: the plant grows under the glass
    b.use(4, -1, 4, "up", "immersiveengineering:cloche")
    b.cmd(f"data merge block {b._p(4, 0, 4)} {{Items:[{{Slot:0b,id:\"minecraft:dirt\",count:1}},"
          f"{{Slot:1b,id:\"immersiveengineering:seed\",count:1}}],energy:16000,tank:{{Fluid:{{id:\"minecraft:water\",amount:4000}}}}}}")
    b.focus(3, 0, 3, 5, 3, 5)


@scene("ae2/p2p", w=10)
def _(b):
    # a P2P tunnel at each end of a dense cable: the dense cable's channels travel through one channel
    b.b(1, -1, 4, "ae2:creative_energy_cell")
    b.b(1, 0, 4, "ae2:energy_acceptor")
    b.use(1, 0, 4, "east", "ae2:fluix_glass_cable")
    b.use(2, 0, 4, "east", "ae2:me_p2p_tunnel")
    for x in (3, 4, 5, 6):
        b.use(x, -1, 4, "up", "ae2:fluix_covered_dense_cable")
    b.use(7, -1, 4, "up", "ae2:fluix_glass_cable")
    b.use(7, 0, 4, "west", "ae2:me_p2p_tunnel")
    b.focus(1, 0, 3, 7, 1, 5)


@scene("pneumaticcraft/safety")
def _(b):
    # a pressure tube with a safety valve and a gauge clicked onto it
    b.f(3, 0, 4, 5, 0, 4, "pneumaticcraft:pressure_tube")
    b.use(3, 0, 4, "up", "pneumaticcraft:safety_tube_module")
    b.use(5, 0, 4, "up", "pneumaticcraft:pressure_gauge_module")
    b.focus(3, 0, 3, 5, 1, 5)


@scene("pneumaticcraft_advanced/frames")
def _(b):
    # a provider frame on one chest, a requester frame on the other: drones carry between them
    b.b(2, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.b(6, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.use(2, 0, 4, "south", "pneumaticcraft:logistics_frame_passive_provider")
    b.use(6, 0, 4, "south", "pneumaticcraft:logistics_frame_requester")


@scene("pneumaticcraft_advanced/first_program")
def _(b):
    b.b(3, 0, 4, "pneumaticcraft:programmer[facing=south]")
    b.show(5, 0, 4, "pneumaticcraft:drone")


@scene("productive_trees/pots")
def _(b):
    # a hopper botany pot on a chest, earth and a walnut sapling in it
    b.b(4, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")
    b.b(4, 1, 4, "botanypots:terracotta_hopper_botany_pot")
    # slot 0 is the soil, slot 1 the seed (the machine hand's clicks put nothing in: seen 13.11.2026)
    b.cmd(f"data merge block {b._p(4, 1, 4)} {{Items:[{{Slot:0b,id:\"minecraft:dirt\",count:1}},"
          f"{{Slot:1b,id:\"productivetrees:walnut_sapling\",count:1}}]}}")


@scene("logistics/laser_node")
def _(b):
    # a laser node on each chest, joined with two clicks of the laser wrench
    for x in (2, 6):
        b.b(x, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")
        b.b(x, 1, 4, "laserio:laser_node")
    b.use(2, 1, 4, "south", "laserio:laser_wrench")
    b.use(6, 1, 4, "south", "laserio:laser_wrench")


# ===================================================================================
# Eighteenth batch: a pen, a breeding station, the steel line, channels, a chain

@scene("farms/animals_thorn")
def _(b):
    # a pen with a dreadthorne in it and the mana pool it drinks from: grown animals die, calves stay
    stage(b, 2, 2, 6, 6, "minecraft:grass_block[snowy=false]")
    for x in range(2, 7):
        for z in (2, 6):
            b.b(x, 0, z, "minecraft:oak_fence")
    for z in (3, 4, 5):
        b.b(2, 0, z, "minecraft:oak_fence")
        b.b(6, 0, z, "minecraft:oak_fence")
    b.b(4, 0, 4, "botania:dreadthorne")
    b.m("minecraft:cow", 3, 0, 5)
    b.m("minecraft:cow", 5, 0, 3, nbt="Age:-24000")
    pool(b, 7, 0, 4, mana=200000)


@scene("alfheim/pure_essence")
def _(b):
    # end stone around the pure daisy: it becomes cobbled deepslate and gives off the essence
    b.b(4, -1, 4, "minecraft:grass_block[snowy=false]")
    b.b(4, 0, 4, "botania:pure_daisy")
    for dx in (-1, 0, 1):
        for dz in (-1, 0, 1):
            if dx or dz:
                b.b(4 + dx, 0, 4 + dz, "minecraft:cobbled_deepslate" if (dx, dz) in ((0, -1), (1, 1)) else "minecraft:end_stone")
    b.pitch = 62.0


def small_tree(b, x, z, wood):
    """A young Productive Trees tree: three logs and a crown."""
    b.f(x, 0, z, x, 2, z, f"productivetrees:{wood}_log[axis=y]")
    for y, r in ((2, 1), (3, 1), (4, 0)):
        for xx in range(x - r, x + r + 1):
            for zz in range(z - r, z + r + 1):
                if (xx, zz) != (x, z) or y > 2:
                    b.b(xx, y, zz, f"productivetrees:{wood}_leaves")


@scene("productive_trees/station", w=11, h=14)
def _(b):
    # a beehive between an aspen and a beech, flowers beside it: each bee that comes home may cross the two
    stage(b, 1, 2, 9, 6, "minecraft:grass_block[snowy=false]")
    small_tree(b, 2, 4, "aspen")
    small_tree(b, 8, 4, "beech")
    b.b(5, 0, 4, "minecraft:oak_fence")
    b.b(5, 1, 4, "minecraft:beehive[facing=south,honey_level=0]")
    for x, z, flower in ((4, 5, "minecraft:poppy"), (6, 5, "minecraft:dandelion"), (5, 6, "minecraft:cornflower")):
        b.b(x, 0, z, flower)


@scene("mekanism/ore_line", w=12)
def _(b):
    # the steel line: chest, infusing factory (enriched iron), infusing factory (steel dust),
    # smelting factory, chest, a transporter between each and a cable behind them
    z = 4
    b.c(1, 0, z, [], frame=True)
    b.b(3, 0, z, "mekanism:basic_infusing_factory[facing=south,active=false]")
    b.b(5, 0, z, "mekanism:basic_infusing_factory[facing=south,active=false]")
    b.b(7, 0, z, "mekanism:basic_smelting_factory[facing=south,active=false]")
    b.c(9, 0, z, [], frame=True)
    for x in (2, 4, 6, 8):
        b.b(x, 0, z, "mekanism:basic_logistical_transporter")
    b.f(3, 0, z - 1, 8, 0, z - 1, "mekanism:basic_universal_cable")
    b.b(9, 0, z - 1, "mekanism:basic_energy_cube[facing=south]")


@scene("ae2/channels", w=11)
def _(b):
    # a tree: dense cable is the branch from the controller, smart cable the twigs, a drive at each twig's end
    b.b(2, -1, 4, "ae2:creative_energy_cell")
    b.b(2, 0, 4, "ae2:controller")
    for x in (2, 2, 3, 4, 5, 6):
        b.use(x, 0, 4, "east", "ae2:fluix_covered_dense_cable")
    for x in (4, 7):
        b.use(x, 0, 4, "south", "ae2:fluix_smart_cable")
        b.use(x, 0, 5, "south", "ae2:fluix_smart_cable")
        b.b(x, 0, 7, "ae2:drive[facing=south,spin=0]")
        b.use(x, 0, 4, "north", "ae2:fluix_smart_cable")
        b.b(x, 0, 2, "ae2:drive[facing=south,spin=0]")
    b.focus(1, 0, 1, 8, 2, 8)      # a block more on every side: the front drives were cut at the picture's edge


@scene("create/frogport", w=11, h=14)
def _(b):
    # two chain conveyors on turning shafts, a chain between them, a frogport beside the chain
    for x, other in ((2, 6), (8, -6)):
        b.b(x, 2, 4, "create:chain_conveyor", f"{{Connections:[[I;{other},0,0]]}}")
        drive_from_below(b, x, 2, 4)
    b.f(5, 0, 5, 5, 1, 5, "minecraft:stone_bricks")
    b.b(5, 2, 5, "create:package_frogport")


# ===================================================================================
# Nineteenth batch: creatures, a station, a reactor shell

@scene("create_brass/blaze_burner")
def _(b):
    # a blaze, and the empty burner you catch it with
    b.m("minecraft:blaze", 3, 0, 4)
    b.show(6, 0, 4, "create:empty_blaze_burner")


@scene("occultism/djinni_familiars", w=11)
def _(b):
    # three of the familiars a djinni ritual can bind
    for x, name in ((2, "dragon_familiar"), (5, "greedy_familiar"), (8, "deer_familiar")):
        b.m(f"occultism:{name}", x, 0, 4)


@scene("occultism/foliot_crusher")
def _(b):
    # the foliot stands by the ore thrown to it; dust is what it leaves
    b.m("occultism:foliot", 3, 0, 4)
    b.drop(5, 0.2, 4, "minecraft:raw_iron", 8)
    b.drop(6, 0.2, 5, "occultism:iron_dust", 16)
    b.focus(2, 0, 3, 6, 2, 5)


@scene("occultism_afrit/unbound_afrit")
def _(b):
    b.m("occultism:afrit_wild", 4, 0, 4)


@scene("occultism_afrit/iesnium")
def _(b):
    # iesnium ore sits in netherrack and looks like it until the rod or the goggles show it
    b.f(3, 0, 3, 5, 1, 4, "minecraft:netherrack")
    b.b(4, 0, 4, "occultism:iesnium_ore")
    b.b(3, 1, 4, "occultism:iesnium_ore")


@scene("ars_master/tribute", w=11, d=11)
def _(b):
    # the Wilden Chimera: bigger than anything else in the book, so its cell and its frame are too
    b.m("ars_nouveau:wilden_boss", 5, 0, 5, rot=0)      # it showed the camera its back the other way round
    b.focus(2, 0, 2, 8, 4, 8)


@scene("ars_nouveau/starbuncle_work")
def _(b):
    # a starbuncle between the chamber it empties and the chest it fills
    b.b(2, 0, 4, "ars_nouveau:imbuement_chamber[facing=up]")
    b.m("ars_nouveau:starbuncle", 4, 0, 4)
    b.b(6, 0, 4, "minecraft:chest[facing=south,type=single,waterlogged=false]")


@scene("alfheim/elementium_armor")
def _(b):
    # elementium armour, and one of the pixies it calls when you are hit
    b.stand(3, 0, 4, armor=("botania:elementium_helmet", "botania:elementium_chestplate", "botania:elementium_leggings", "botania:elementium_boots"))
    b.m("botania:pixie", 6, 1, 4)


@scene("industrial/frame_simple", w=11)
def _(b):
    # the four machine frames in the order you build them: pity, simple, advanced, supreme
    for i, name in enumerate(("pity", "simple", "advanced", "supreme")):
        b.b(2 + 2 * i, 0, 4, f"industrialforegoing:machine_frame_{name}")


@scene("create_trains/station", w=11)
def _(b):
    # a stretch of track, the station beside it, two bogeys set on the track: what a train is assembled from
    b.f(1, 0, 4, 9, 0, 4, "create:track[shape=xo,turn=false,waterlogged=false]")
    b.b(5, 0, 6, "create:track_station")
    b.b(3, 1, 4, "create:small_bogey[axis=x,waterlogged=false]")
    b.b(7, 1, 4, "create:small_bogey[axis=x,waterlogged=false]")
    b.f(3, 2, 4, 7, 2, 4, "create:railway_casing")


@scene("create_trains/postbox", w=11)
def _(b):
    # a postbox at the platform: trains that stop here take its packages along
    b.f(1, 0, 4, 9, 0, 4, "create:track[shape=xo,turn=false,waterlogged=false]")
    b.b(5, 0, 6, "create:track_station")
    b.b(7, 0, 6, "create:white_postbox[facing=south,open=false,waterlogged=false]")


@scene("oritech/reactor", h=14)
def _(b):
    # the reactor's shell: walls as a box, the controller in the front wall, a fuel port in the
    # roof over the rod inside, the energy port outside
    b.f(3, 0, 3, 5, 3, 5, "oritech:reactor_wall")
    b.b(4, 1, 4, "oritech:reactor_rod[lit=false]")
    b.b(4, 2, 4, "minecraft:air")
    b.b(4, 3, 4, "oritech:reactor_fuel_port")
    b.b(4, 1, 5, "oritech:reactor_controller[facing=south]")
    b.b(6, 1, 4, "oritech:reactor_energy_port[facing=west]")


@scene("immersive/transformer", h=14)
def _(b):
    # the transformer between a low voltage and a medium voltage capacitor
    b.b(2, 0, 4, "immersiveengineering:capacitor_lv")
    b.use(4, -1, 4, "up", "immersiveengineering:transformer")
    b.b(6, 0, 4, "immersiveengineering:capacitor_mv")
    b.focus(2, 0, 3, 6, 2, 5)


# ===================================================================================
# Twentieth batch: a wood set, pipes, candles

@scene("productive_trees/wood_set")
def _(b):
    # what one new wood gives: planks, stairs, slab, fence, a door and a bookshelf of walnut
    b.f(2, 0, 4, 3, 1, 4, "productivetrees:walnut_planks")
    b.b(4, 0, 4, "productivetrees:walnut_stairs[facing=east,half=bottom,shape=straight]")
    b.b(5, 0, 4, "productivetrees:walnut_slab[type=bottom]")
    b.b(6, 0, 4, "productivetrees:walnut_bookshelf")
    b.b(6, 1, 4, "productivetrees:walnut_bookshelf")
    b.b(2, 0, 5, "productivetrees:walnut_fence")
    b.b(3, 0, 5, "productivetrees:walnut_fence")
    b.b(5, 0, 6, "productivetrees:walnut_door[facing=south,half=lower,hinge=left,open=false]")
    b.b(5, 1, 6, "productivetrees:walnut_door[facing=south,half=upper,hinge=left,open=false]")


@scene("oritech/pipes", w=10)
def _(b):
    # an energy pipe and an item pipe laid by hand between two machines
    b.b(2, 0, 4, "oritech:pulverizer_block")
    b.b(7, 0, 4, "oritech:pulverizer_block")
    for x in (3, 4, 5, 6):
        b.use(x, -1, 4, "up", "oritech:energy_pipe")
    for x in (3, 4, 5, 6):
        b.use(x, -1, 5, "up", "oritech:item_pipe")
    b.focus(2, 0, 3, 7, 1, 5)


@scene("hexerei/candles")
def _(b):
    # the candle dipper over a mixing cauldron of tallow
    b.b(4, 0, 4, "hexerei:mixing_cauldron")
    b.b(4, 1, 4, "hexerei:candle_dipper[facing=south]")


@scene("ars_master/ritual_awakening")
def _(b):
    b.m("ars_nouveau:cascading_weald_walker", 4, 0, 4)


# ===================================================================================
# Twenty-first batch

@scene("farms/lava_seeds")
def _(b):
    # a field of fire seeds around its water, and the item drain on a tank that turns their lava buckets into lava
    b.f(2, -1, 3, 6, -1, 5, "minecraft:farmland[moisture=7]")
    b.b(4, -1, 4, "minecraft:water")
    for x in range(2, 7):
        for z in (3, 4, 5):
            if (x, z) != (4, 4):
                b.b(x, 0, z, "mysticalagriculture:fire_crop[age=7]")
    b.b(7, 0, 4, "create:fluid_tank[bottom=true,shape=window,top=true]")
    b.b(7, 1, 4, "create:item_drain")
    b.focus(2, 0, 3, 7, 1, 5)


@scene("create_trains/unprocessed_sheet")
def _(b):
    # powdered obsidian on a depot under a spout: lava makes the unprocessed sheet
    b.b(4, 0, 4, "create:depot")
    b.b(4, 2, 4, "create:spout")
    b.b(4, 3, 4, "create:fluid_tank[bottom=true,shape=window,top=true]")
    b.use(4, 0, 4, "up", "create:powdered_obsidian")


@scene("productive_trees/time_traveller")
def _(b):
    b.b(4, 0, 4, "productivetrees:time_traveller_display[axis=y]")


@scene("nuclearcraft/irradiation")
def _(b):
    # the irradiation chamber that goes into the reactor, and the irradiator that works on its own
    b.b(3, 0, 4, "nuclearcraft:fission_reactor_irradiation_chamber")
    b.b(5, 0, 4, "nuclearcraft:irradiator[facing=south,powered=false]")


@scene("mekanism/configurator")
def _(b):
    # the configurator, and a machine whose sides it sets
    b.b(3, 0, 4, "mekanism:metallurgic_infuser[facing=south]")
    b.show(5, 0, 4, "mekanism:configurator")


@scene("hexerei/sage_plate")
def _(b):
    # a dried sage bundle on the burning plate, lit with flint and steel: monsters stay away while it smokes
    b.b(4, 0, 4, "hexerei:sage_burning_plate[facing=south]")
    b.use(4, 0, 4, "up", "hexerei:dried_sage_bundle")
    b.use(4, 0, 4, "up", "minecraft:flint_and_steel")
    b.focus(3, 0, 3, 5, 1, 5)


@scene("create_trains/cargo", d=11)
def _(b):
    # a wagon's portable storage interface and the platform's, face to face across one block of
    # air: where they meet, cargo changes sides. The track runs toward the camera so both show.
    b.f(4, 0, 1, 4, 0, 9, "create:track[shape=zo,turn=false,waterlogged=false]")
    b.b(4, 1, 3, "create:small_bogey[axis=z,waterlogged=false]")
    b.b(4, 1, 7, "create:small_bogey[axis=z,waterlogged=false]")
    b.f(4, 2, 3, 4, 2, 7, "create:railway_casing")
    b.b(4, 3, 4, "minecraft:barrel[facing=up]")
    b.b(4, 3, 5, "create:portable_storage_interface[facing=east]")
    b.b(4, 3, 6, "minecraft:barrel[facing=up]")
    b.f(7, 0, 5, 7, 2, 5, "minecraft:stone_bricks")
    b.b(7, 3, 5, "minecraft:barrel[facing=up]")
    b.b(6, 3, 5, "create:portable_storage_interface[facing=west]")


# ===================================================================================
# Ponder scenes of the mods themselves: what their authors built to explain a part, placed
# as it is, its checkered floor plate set into the floor

def ponder(key, jar, path, deep=0, pad=0):
    """pad widens the frame by that many blocks on every side: a wide, deep structure comes
    closer to the camera at its front than the framing reckons with."""
    import structs
    (sx, sy, sz), _, _, _ = structs.load(jar, path)

    @scene(key, w=sx + 2 + 2 * pad, d=sz + 2 + deep + 2 * pad, h=sy + 6)
    def _(b):
        b.nbt(jar, path, 1 + pad, -1, 1 + pad)
        if pad:
            b.focus(1, 0, 1, sx + 2 * pad, sy - 1, sz + 2 * pad)


ponder("create_trains/first_train", "create-1", "assets/create/ponder/train_controls.nbt")
ponder("create_trains/conductor", "create-1", "assets/create/ponder/train_schedule.nbt")
ponder("create_trains/junction", "create-1", "assets/create/ponder/train_signal/signaling.nbt")
ponder("create/stock_ticker", "create-1", "assets/create/ponder/high_logistics/stock_ticker.nbt")
ponder("create_brass/boiler", "create-1", "assets/create/ponder/steam_engine.nbt", deep=6)
ponder("create_brass/pg_winding", "powergrid", "assets/powergrid/ponder/generator/generator_1.nbt")
ponder("create_brass/pg_generator", "powergrid", "assets/powergrid/ponder/generator/generator_3.nbt", deep=4)
ponder("create_brass/pg_magnet", "powergrid", "assets/powergrid/ponder/electromagnet.nbt")
ponder("list_gear/drilling", "createoreexcavation", "assets/createoreexcavation/ponder/drilling_machine.nbt")
ponder("mekanism_ores/foundry", "productivemetalworks", "assets/productivemetalworks/ponder/foundry_molten.nbt", deep=6, pad=2)   # room around it: it was cut at two edges
ponder("farms/s2_xp", "create-enchantment", "assets/create_enchantment_industry/ponder/grindstone/basic.nbt")
ponder("create_trains/schedule", "create-1", "assets/create/ponder/train_station/schedule.nbt")
ponder("create_brass/alternator", "createaddition", "assets/createaddition/ponder/alternator.nbt")


# ===================================================================================
# What a quest asks you to hold, on show: for quests whose subject is an item and no build

def shelf(key, items, scale=None):
    n = len(items)
    if scale is None:
        scale = 2.0 if n == 1 else 1.0      # one thing alone is shown twice its size, or the picture is mostly floor

    @scene(key, w=max(9, 2 * n + 3))
    def _(b):
        x0 = (max(9, 2 * n + 3) - (2 * n - 1)) // 2
        for i, item in enumerate(items):
            b.show(x0 + 2 * i, 0, 4, item, scale)


shelf("nuclearcraft/geiger", ["nuclear_radiation:geiger_counter", "nuclear_radiation:dosimeter"])
shelf("enderio/filter", ["enderio:yeta_wrench", "enderio:basic_item_filter"])
shelf("malum/spirits", ["malum:sacred_spirit", "malum:wicked_spirit", "malum:arcane_spirit"])
shelf("ae2_advanced/mega_4m", ["megacells:item_storage_cell_4m"])
shelf("hostile_networks/deep_learner", ["hostilenetworks:deep_learner"])
shelf("logistics/mg_gadget", ["mininggadgets:mininggadget_simple"])
shelf("food/f_rod", ["aquaculture:iron_fishing_rod"])
shelf("silent_gear/repair_kit", ["silentgear:crude_repair_kit"])
shelf("botania_runes/rune_core", ["kronwerke:rune_core"])


@scene("storage/config_tool")
def _(b):
    # the configuration tool, and a drawer to lock with it
    b.b(3, 0, 4, "functionalstorage:oak_1[facing=down,subfacing=south]")
    b.show(5, 0, 4, "functionalstorage:configuration_tool")


@scene("productive_trees/amber")
def _(b):
    # the brown amber only grows from nine saplings in a square
    stage(b, 2, 2, 6, 6, "minecraft:grass_block[snowy=false]")
    for x in (3, 4, 5):
        for z in (3, 4, 5):
            b.b(x, 0, z, "productivetrees:brown_amber_sapling")
    b.focus(2, 0, 2, 6, 1, 6)


# ===================================================================================
# The bosses and beasts of the other worlds, standing still for their portrait

def creature(key, entity, big=False, tall=False, nbt=""):
    @scene(key, w=11, d=11)
    def _(b):
        b.m(entity, 5, 0, 5, nbt=nbt, rot=0)
        if tall:
            b.focus(3, 0, 3, 7, 3, 7)      # the stalker and the monstrosity reach higher than four blocks: the wide frame holds them
        elif big:
            b.focus(4, 0, 4, 6, 3, 6)      # three blocks wide, four high: five wide left the others small in the picture


creature("aether/slider", "aether:slider", big=True)
creature("aether/queen", "aether:valkyrie_queen")
creature("aether/ride", "aether:moa")
creature("undergarden/guardian", "undergarden:forgotten_guardian", big=True)
creature("deeper_darker/stalker", "deeperdarker:stalker", tall=True)
creature("eternal_starlight/golem", "eternal_starlight:starlight_golem", big=True)
creature("eternal_starlight/monstrosity", "eternal_starlight:lunar_monstrosity", tall=True)
creature("eternal_starlight/orb", "eternal_starlight:the_gatekeeper")

shelf("aether/gloves", ["aether:zanite_gloves"])
shelf("undergarden/forgotten", ["undergarden:forgotten_pickaxe"])
shelf("eternal_starlight/starfire", ["eternal_starlight:starfire"])
shelf("deeper_darker/echo_shard", ["deeperdarker:reinforced_echo_shard", "deeperdarker:ancient_compass"])
shelf("exploration/e_compass", ["naturescompass:naturescompass"])
