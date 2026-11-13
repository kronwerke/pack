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
    b.focus(1, 0, 2, 8, 2, 7)                              # the wheels are larger than their blocks


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


@scene("aether/portal", "list_dimensions/d_aether", w=8)
def _(b):
    gate(b, "minecraft:glowstone", "aether:aether_portal[axis=x]")


@scene("deeper_darker/portal", "list_dimensions/d_otherside", w=8)
def _(b):
    gate(b, "minecraft:reinforced_deepslate", "deeperdarker:otherside_portal[axis=x]")


@scene("undergarden/arrival", "list_dimensions/d_undergarden", w=8)
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


@scene("immersive/connectors", "immersive/capacitor", w=11)
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


@scene("immersive/dynamo", "immersive/windmill", w=15, d=11, h=26)
def _(b):
    # the dynamo on a post of treated wood, the windmill set against its shaft side
    b.f(7, 0, 3, 7, 6, 3, "immersiveengineering:treated_wood_horizontal")
    b.b(7, 7, 3, "immersiveengineering:dynamo[facing=south]")
    b.use(7, 7, 3, "south", "immersiveengineering:windmill")
    b.changed(7, 7, 4, "minecraft:air")
    b.focus(1, 0, 3, 13, 13, 5)                            # the blades reach six blocks out


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
    # the crucible over a campfire (no water: a bucket used on it by the machine hand sets a
    # source on top of it, which floods the box)
    b.b(4, 0, 4, "minecraft:campfire[facing=south,lit=true]")
    b.b(4, 1, 4, "eidolon_repraised:crucible")


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


@scene("draconic/stabilizer", "draconic/tiers", w=11, d=11)
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


@scene("botania/manasteel_prep", "botania_runes/ritual", w=11, d=11)
def _(b):
    # manasteel on Kronwerke: four infused iron, two livingwood twigs, a mana diamond and a gold leaf
    forest_ritual(b, ["naturesaura:infused_iron", "botania:livingwood_twig", "naturesaura:infused_iron", "botania:mana_diamond",
                      "naturesaura:gold_leaf", "naturesaura:infused_iron", "botania:livingwood_twig", "naturesaura:infused_iron"])


@scene("mekanism_elite/mekasuit", "list_gear/mekasuit")
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
    # a wall of drawers, three by three, set against planks so every one looks out, something in each
    b.f(3, 0, 3, 5, 2, 3, "minecraft:oak_planks")
    items = ["minecraft:iron_ingot", "minecraft:copper_ingot", "minecraft:gold_ingot", "minecraft:redstone", "minecraft:coal",
             "minecraft:lapis_lazuli", "minecraft:diamond", "minecraft:quartz", "minecraft:bone"]
    for i, item in enumerate(items):
        x, y = 3 + i % 3, i // 3
        b.use(x, y, 3, "south", "functionalstorage:oak_4")
        b.changed(x, y, 4, "minecraft:air")
        b.use(x, y, 4, "south", item)


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


@scene("botania/endo_auto")
def _(b):
    # chest, hopper and open crate over the drop point, endoflames around it. The pressure plate
    # under the drop point locks the hopper while a piece of coal still lies there: its signal
    # climbs a stair of redstone dust to the block beside the hopper.
    stage(b, 3, 4, 5, 5, "minecraft:grass_block")
    b.b(4, -1, 4, "minecraft:light_gray_concrete")
    b.b(4, 0, 4, "minecraft:oak_pressure_plate")
    for x, z in ((3, 4), (5, 4), (3, 5), (4, 5), (5, 5)):
        b.b(x, 0, z, "botania:endoflame")
    b.b(4, 2, 4, "botania:open_crate")
    b.b(4, 3, 4, "minecraft:hopper[facing=down]")
    b.c(4, 4, 4, [("minecraft:coal", 64)], frame=True)
    stair = "minecraft:stone_bricks"
    b.b(4, 0, 3, "minecraft:redstone_wire")
    b.b(4, 0, 2, stair)
    b.b(4, 1, 2, "minecraft:redstone_wire")
    b.b(5, 1, 2, stair)
    b.b(5, 2, 2, "minecraft:redstone_wire")
    b.b(5, 2, 3, stair)
    b.b(5, 3, 3, "minecraft:redstone_wire")
    b.b(5, 3, 4, stair)


@scene("draconic_chaos/reactor", w=11, d=11, h=22)
def _(b):
    # the core in the air, four stabilizers in one plane on four sides and the energy injector
    # above, each set by hand against a block (taken away again) so that it looks at the core
    cx, cy, cz = 5, 3, 5
    b.b(cx, cy, cz, "draconicevolution:reactor_core")
    helper = "minecraft:stone"
    for hx, hz, face in ((0, cz, "east"), (10, cz, "west"), (cx, 0, "south"), (cx, 10, "north")):
        b.b(hx, cy, hz, helper)
        b.use(hx, cy, hz, face, "draconicevolution:reactor_stabilizer")
        b.b(hx, cy, hz, "minecraft:air")
    b.b(cx, cy + 5, cz, helper)
    b.use(cx, cy + 5, cz, "down", "draconicevolution:reactor_injector")
    b.b(cx, cy + 5, cz, "minecraft:air")
    b.expect(1, cy, cz, "draconicevolution:reactor_stabilizer")
    b.expect(cx, cy + 4, cz, "draconicevolution:reactor_injector")
    b.focus(1, 0, 1, 9, cy + 4, 9)


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


@scene("ars_apprentice/relay", w=17)
def _(b):
    # full jar, relay, relay, empty jar, linked with the dominion wand in that order
    b.b(1, 0, 4, "ars_nouveau:source_jar[fill=11]", "{source:10000}")
    b.b(6, 0, 4, "ars_nouveau:relay")
    b.b(10, 0, 4, "ars_nouveau:relay")
    b.b(15, 0, 4, "ars_nouveau:source_jar[fill=0]")
    for a, c in ((1, 6), (6, 10), (10, 15)):
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
    b.b(x0 + 4, 1, z0 + 2, "nuclearcraft:fission_reactor_controller[facing=east]")
    b.b(x0 + 4, 3, z0 + 2, "nuclearcraft:fission_reactor_port")
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
    housed_motor(b, 6, 0, 7, "west", 16)
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


# what a list chapter shows again from the chapter that explains it
for _again, _first in (("list_transport/belt", "create/belt"), ("list_transport/vault", "storage/vault_big"),
                       ("list_transport/drawers", "storage/drawers_4"), ("list_power/powah_reactor", "powah/reactor"),
                       ("list_power/ie_thermo", "immersive/thermoelectric"), ("list_dimensions/r_mekanism", "mekanism_advanced/teleporter")):
    SCENES[_again] = SCENES[_first]
