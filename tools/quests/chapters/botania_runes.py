"""Botania in stage 2: manasteel, the runic altar, runes and terrasteel."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp

C = "botania_runes"

quests = [
    quest("welcome", 0, 0, "Manasteel",
          subtitle="Iron, soaked in mana.",
          description=[
              "Stage 2 opens what the mana pool can really do. Throw an iron ingot into a full enough pool and it comes out as &6Manasteel&r.",
              "",
              "The obelisk wants &61 500 mana pearls&r and &6100 terrasteel ingots&r for this stage. That is a lot of mana: build more flowers now.",
          ],
          tasks=[task_item("botania:manasteel_ingot", 8)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s2_common")],
          icon="botania:manasteel_ingot", size=2.0, shape="hexagon"),

    quest("pearl", 3, -2, "Mana Pearl",
          subtitle="An ender pearl, infused.",
          description=[
              "Ender pearl into the pool. Mana pearls go into the terrasteel recipe and straight into the obelisk.",
              "An enderman farm pays for itself here.",
          ],
          tasks=[task_item("botania:mana_pearl", 8)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["welcome"]),

    quest("gear", 3, 2, "Manasteel Tools",
          subtitle="Repair themselves with mana.",
          description=[
              "Manasteel tools and armour draw mana from a &6Mana Tablet&r or ring in your inventory to repair themselves. Mekanism engineers need your manasteel too: their first machine takes two ingots.",
          ],
          tasks=[task_item("botania:manasteel_pickaxe", 1)],
          rewards=[reward_item("botania:manasteel_ingot", 4)],
          deps=["welcome"], optional=True),

    quest("altar", 6, 0, "Runic Altar",
          subtitle="Where runes are made.",
          description=[
              "The &6Runic Altar&r takes mana from a spreader. Throw in the ingredients of a rune, then a block of &6Livingrock&r, then right click it with the Wand of the Forest.",
              "The Lexica Botania and JEI show every rune recipe.",
          ],
          tasks=[task_item("botania:runic_altar", 1)],
          rewards=[reward_item("botania:livingrock", 32), reward_table("s2_common")],
          deps=["pearl"], icon="botania:runic_altar", size=1.5),

    quest("elements", 9, -2, "The Four Elements",
          subtitle="Water, fire, earth, air.",
          description=[
              "The four elemental runes. Almost every rune after these is made from them.",
          ],
          tasks=[task_item("botania:rune_of_water", 1), task_item("botania:rune_of_fire", 1),
                 task_item("botania:rune_of_earth", 1), task_item("botania:rune_of_air", 1)],
          rewards=[reward_item("minecraft:sugar_cane", 16), reward_item("minecraft:nether_wart", 8)],
          deps=["altar"], icon="botania:rune_of_fire"),

    quest("mana_rune", 9, 2, "Rune of Mana",
          subtitle="Pure mana, set in stone.",
          description=[
              "Manasteel and a mana pearl on the altar. It goes into the terrestrial plate and many later recipes.",
          ],
          tasks=[task_item("botania:rune_of_mana", 1)],
          rewards=[reward_item("botania:mana_pearl", 2)],
          deps=["altar"]),

    quest("seasons", 12, -3.5, "The Seasons",
          subtitle="Spring, summer, autumn, winter.",
          description=[
              "Seasonal runes combine two elemental runes each. Several functional flowers and items need them.",
          ],
          tasks=[task_item("botania:rune_of_spring", 1), task_item("botania:rune_of_summer", 1),
                 task_item("botania:rune_of_autumn", 1), task_item("botania:rune_of_winter", 1)],
          rewards=[reward_table("s2_uncommon")],
          deps=["elements"], optional=True),

    quest("plate", 12, 0, "Terrestrial Agglomeration Plate",
          subtitle="Needs runes, and an engineer.",
          description=[
              "Four elemental runes, a rune of mana, mana quartz, lapis, and on this server two &6Brass Casings&r from Create. Find someone with a brass line, or build one.",
              "",
              "The plate sits on a pattern of livingrock and lapis blocks. The Lexica page shows it.",
          ],
          tasks=[task_item("botania:terrestrial_agglomeration_plate", 1)],
          rewards=[reward_item("minecraft:lapis_block", 4), reward_table("s2_uncommon")],
          deps=["elements", "mana_rune"], icon="botania:terrestrial_agglomeration_plate", size=1.5),

    quest("terrasteel", 15, 0, "Terrasteel",
          subtitle="The strongest thing Botania makes in this stage.",
          description=[
              "Drop a manasteel ingot, a mana diamond and a mana pearl on the plate and point spreaders at it. One ingot eats about half of a full mana pool.",
          ],
          tasks=[task_item("botania:terrasteel_ingot", 2)],
          rewards=[reward_item("botania:mana_diamond", 2), reward_table("s2_uncommon")],
          deps=["plate"], icon="botania:terrasteel_ingot", size=1.5, shape="diamond"),

    quest("tablet", 15, -3, "Mana Tablet",
          subtitle="A mana pool you can carry.",
          description=[
              "Fill it in a pool, keep it in your inventory. Manasteel tools repair from it, and many rods and rings run on it.",
          ],
          tasks=[task_item("botania:mana_tablet", 1)],
          rewards=[reward_item("botania:manasteel_ingot", 4)],
          deps=["terrasteel"], optional=True),

    quest("gateway", 15, 3, "The Gateway",
          subtitle="A door to Alfheim, not open for trade yet.",
          description=[
              "The &6Gateway Core&r and &6Natura Pylons&r can be built now. What the elves trade (dreamwood, elementium) opens with stage 3, so this is preparation.",
          ],
          tasks=[task_item("botania:elven_gateway_core", 1), task_item("botania:natura_pylon", 2)],
          rewards=[reward_item("botania:livingwood", 32)],
          deps=["terrasteel"], optional=True),

    quest("engine", 18, 0, "Mana for the Obelisk",
          subtitle="Pearls and terrasteel by the stack.",
          description=[
              "Enough flowers that the pools refill on their own, pearls from an enderman farm, a plate that is never idle. Bring it to the obelisk.",
          ],
          tasks=[task_item("botania:mana_pearl", 64), task_item("botania:terrasteel_ingot", 8)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["terrasteel"], icon="botania:terrasteel_block", size=1.75),
]

chapter(C, "Botania: Runes", "botania:rune_of_mana", "magic", quests, shape="circle", order=11, stage=2,
        subtitle=["Stage 2. Manasteel, runes and terrasteel."])
