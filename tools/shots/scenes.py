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
    b.focus(2, 0, 2, 6, 2, 6)


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
    # two parallel shafts, clicked one after the other with the belt in hand
    b.b(2, 0, 4, "create:shaft[axis=z]")
    b.b(6, 0, 4, "create:shaft[axis=z]")
    b.use(2, 0, 4, "up", "create:belt_connector")
    b.use(6, 0, 4, "up", "create:belt_connector")
    b.changed(4, 0, 4, "minecraft:air")              # the belt runs between them


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
    # Four wheels on one shaft, a sheet of water falling past their backs into a trench:
    # falling water beside a wheel turns it, as in Ponder water_wheel. A source spreads to
    # every side even while it falls, so the flume is closed all round and open below.
    for x in range(3, 7):
        b.b(x, 1, 4, "create:water_wheel[facing=east]")
        b.b(x, -1, 3, "minecraft:air")                    # the trench the water falls into
    for x in (2, 7):
        b.b(x, 0, 4, "create:andesite_casing")
        b.b(x, 1, 4, "create:andesite_encased_shaft[axis=x]")
    b.f(2, 2, 2, 7, 2, 3, "minecraft:spruce_planks")
    # the front of the flume is a row of raised trapdoors: they hold the water and leave the
    # wheels in view
    b.f(3, 2, 4, 6, 2, 4, "minecraft:spruce_trapdoor[facing=south,half=bottom,open=true]")
    b.f(3, 2, 3, 6, 2, 3, "minecraft:water")
    b.pitch = 24.0
    b.later(3, 1, 4, "data block @ {Speed:0.0f}", unless=True)       # it turns
    b.later(4, 0, 5, "block @ minecraft:air")              # nothing spills to the front


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
    b.b(7, 0, 7, "ars_nouveau:source_jar[fill=11]", "{source:10000}")
