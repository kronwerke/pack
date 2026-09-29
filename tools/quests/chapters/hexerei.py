"""Hexerei in stage 2: the witch's workshop, sage, brooms and crows."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp

C = "hexerei"

quests = [
    quest("welcome", 0, 0, "Hexerei",
          subtitle="Herbs, a cauldron and a broom.",
          description=[
              "Hexerei is witchcraft the old way: gather herbs, dry them, grind them, mix them in a cauldron. The &6Book of Shadows&r is its manual. Put it on an altar to read it standing up.",
              "",
              "Belladonna, mandrake, mugwort, sage and yellow dock grow wild. Look in swamps and forests.",
          ],
          tasks=[task_item("hexerei:book_of_shadows", 1)],
          rewards=[reward_item("hexerei:sage_seed", 8), reward_table("s2_common")],
          icon="hexerei:book_of_shadows", size=2.0, shape="hexagon"),

    quest("mortar", 3, -2, "Pestle and Mortar",
          subtitle="Grind it first.",
          description=[
              "Right click to put items in. The recipe starts on its own once everything is inside. Crouch and right click with an empty hand to take things out.",
              "Herbs dry on a drying rack before most recipes want them.",
          ],
          tasks=[task_item("hexerei:pestle_and_mortar", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["welcome"]),

    quest("cauldron", 3, 2, "Mixing Cauldron",
          subtitle="Where every Hexerei recipe ends.",
          description=[
              "Fill it with the right liquid and add the ingredients. The Book of Shadows lists what goes in. Most brooms, brushes and sigils are made here.",
          ],
          tasks=[task_item("hexerei:mixing_cauldron", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_table("s2_common")],
          deps=["welcome"], icon="hexerei:mixing_cauldron", size=1.5),

    quest("jar", 6, -2, "Herb Jar",
          subtitle="1024 of one herb, on a shelf.",
          description=[
              "A jar holds up to 1024 of a single item. Punch the front to take one out, right click another side for the full view.",
          ],
          tasks=[task_item("hexerei:herb_jar", 4)],
          rewards=[reward_item("minecraft:glass", 16)],
          deps=["mortar"], optional=True),

    quest("sage", 6, 2, "Burning Sage",
          subtitle="No monsters at home.",
          description=[
              "A lit bundle of dried sage on a &6Sage Burning Plate&r stops monsters from spawning in a wide radius around it. The bundle burns down slowly, keep a few spare.",
          ],
          tasks=[task_item("hexerei:sage_burning_plate", 1), task_item("hexerei:dried_sage_bundle", 2)],
          rewards=[reward_item("hexerei:sage_seed", 16), reward_table("s2_uncommon")],
          deps=["cauldron"], icon="hexerei:sage_burning_plate", size=1.5),

    quest("broom", 9, 0, "A Broom",
          subtitle="Fly.",
          description=[
              "The &6Willow Broom&r is the easy one, good for building. The &6Mahogany Broom&r is faster and does not burn. Crouch and right click a broom to open its inventory, where brushes, tips and satchels go.",
          ],
          tasks=[task_item("hexerei:willow_broom", 1)],
          rewards=[reward_item("minecraft:feather", 16), reward_table("s2_uncommon")],
          deps=["cauldron"], icon="hexerei:willow_broom", size=1.5, shape="diamond"),

    quest("crow", 9, -3.5, "Crows",
          subtitle="Small, black, helpful.",
          description=[
              "Tamed crows follow you, sit on your shoulder, and with a &6Crow Flute&r you can tell them to gather items into a coffer, harvest and replant crops, or pick villagers' pockets.",
          ],
          tasks=[task_item("hexerei:crow_flute", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 32)],
          deps=["mortar"], optional=True),

    quest("witch", 12, 0, "A Witch's House",
          subtitle="Candles, herbs, a broom by the door.",
          description=[
              "Dip candles from tallow in the cauldron with the &6Candle Dipper&r, fill the jars, keep the sage burning. Then fly off and help the Botania and Ars players fill the obelisk.",
          ],
          tasks=[task_item("hexerei:candle", 8), task_item("hexerei:mahogany_broom", 1)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["broom", "sage"], icon="hexerei:mahogany_broom", size=1.75),
]

chapter(C, "Hexerei", "hexerei:mixing_cauldron", "magic", quests, shape="circle", order=16, stage=2,
        subtitle=["Stage 2. Herbs, the mixing cauldron, sage and brooms."])
