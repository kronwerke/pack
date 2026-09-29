"""Create: from a pile of andesite to a working mechanical press."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "create"

quests = [
    quest("welcome", 0, 0, "Create",
          subtitle="Rotational power, no wires needed.",
          description=[
              "Create is about spinning things. Water wheels and windmills make rotation, shafts and cogwheels carry it, and machines use it to crush, press, mix and move.",
              "",
              "Everything in this chapter works from the first day of the season. The deeper machines (brass, trains, electron tubes) open with a later stage.",
              "",
              "&6Tip:&r Hold &eW&r on any Create block to open its Ponder screen. It shows you how the block works, step by step.",
          ],
          tasks=[task_checkmark("Read this")],
          rewards=[reward_item("minecraft:andesite", 32), reward_table("common")],
          icon="create:large_cogwheel", size=2.0, shape="hexagon"),

    quest("andesite_alloy", 3, 0, "Andesite Alloy",
          subtitle="The stuff every Create block starts with.",
          description=[
              "Craft &6Andesite&r with &6Iron Nuggets&r or &6Zinc Nuggets&r in the crafting table. Two alloy per craft.",
              "You will need hundreds of these. Andesite is common under y=0 and in the Mining Dimension.",
          ],
          tasks=[task_item("create:andesite_alloy", 16)],
          rewards=[reward_item("create:andesite_alloy", 16)],
          deps=["welcome"]),

    quest("shaft", 6, -1.5, "Shafts",
          subtitle="Carries rotation in a straight line.",
          description=["A shaft passes rotation from one block to the next. Chain as many as you like, they lose nothing along the way."],
          tasks=[task_item("create:shaft", 8)],
          rewards=[reward_item("create:shaft", 8)],
          deps=["andesite_alloy"]),

    quest("cogwheel", 6, 1.5, "Cogwheels",
          subtitle="Turns corners and changes speed.",
          description=[
              "Two cogwheels next to each other pass rotation sideways and flip the direction.",
              "A small cogwheel driving a large one halves the speed and doubles the stress capacity. The other way round doubles the speed.",
          ],
          tasks=[task_item("create:cogwheel", 4), task_item("create:large_cogwheel", 2)],
          rewards=[reward_item("create:cogwheel", 4), reward_item("create:large_cogwheel", 2)],
          deps=["andesite_alloy"]),

    quest("water_wheel", 9, 0, "Water Wheel",
          subtitle="Your first source of rotation.",
          description=[
              "Place a &6Water Wheel&r with flowing water on its blades. Each wheel gives 8 RPM and a little stress capacity.",
              "Two wheels on one shaft add their capacity, not their speed. Stack a few for your first machines.",
              "",
              "The &6Large Water Wheel&r (3x3) gives 4 RPM but much more capacity.",
          ],
          tasks=[task_item("create:water_wheel", 1)],
          rewards=[reward_item("create:water_wheel", 2), reward_item("minecraft:water_bucket", 1)],
          deps=["shaft", "cogwheel"], icon="create:water_wheel", size=1.5),

    quest("goggles", 9, 3, "Engineer's Goggles",
          subtitle="See stress and speed on any block.",
          description=["Wear the goggles and look at a shaft or machine. The overlay tells you the speed and how much stress capacity the network has left."],
          tasks=[task_item("create:goggles", 1)],
          rewards=[reward_xp(5)],
          deps=["water_wheel"], optional=True),

    quest("millstone", 12, -2, "Millstone",
          subtitle="Grinds things. Slowly. Your first machine.",
          description=[
              "Put rotation into the &6Millstone&r from below or the side, drop items in from the top. It grinds wheat into flour, cobblestone into gravel, and gravel into flint and sand.",
              "Right click to take the output, or let a hopper or chute pull it out.",
          ],
          tasks=[task_item("create:millstone", 1)],
          rewards=[reward_item("minecraft:wheat", 32), reward_table("common")],
          deps=["water_wheel"]),

    quest("mechanical_press", 12, 2, "Mechanical Press",
          subtitle="Ingots to plates, and the door to the rest of Create.",
          description=[
              "Place the &6Mechanical Press&r one block above a &6Depot&r or a belt. Rotation from the top. Drop an ingot on the depot and it becomes a sheet.",
              "Sheets are in almost every Create recipe from here on. Iron, copper, gold and brass all press.",
          ],
          tasks=[task_item("create:mechanical_press", 1), task_item("create:depot", 1)],
          rewards=[reward_item("create:iron_sheet", 16), reward_table("uncommon")],
          deps=["water_wheel"], icon="create:mechanical_press", size=1.5),

    quest("belt", 15, 0, "Mechanical Belt",
          subtitle="Moves items and rotation at the same time.",
          description=[
              "Craft belts from &6Dried Kelp&r. Place two shafts up to 20 blocks apart and right click both with the belt.",
              "The belt carries items along it and also passes rotation between the two shafts. Put a Mechanical Press over a belt and you have a sheet factory.",
          ],
          tasks=[task_item("create:belt_connector", 4)],
          rewards=[reward_item("create:belt_connector", 8), reward_item("minecraft:dried_kelp", 16)],
          deps=["mechanical_press"]),

    quest("encased_fan", 15, -3, "Encased Fan",
          subtitle="Wash, smelt and smoke with air.",
          description=[
              "Point an &6Encased Fan&r through water and drop items into the stream: gravel washes into flint and iron nuggets, sand into clay, soul sand into quartz.",
              "Through lava it smelts, through fire it smokes. No fuel needed, just rotation.",
          ],
          tasks=[task_item("create:encased_fan", 1)],
          rewards=[reward_item("minecraft:gravel", 64), reward_table("common")],
          deps=["millstone"]),

    quest("mixer", 18, 0, "Mechanical Mixer",
          subtitle="Mixes items, fluids, and the way to brass.",
          description=[
              "The &6Mechanical Mixer&r sits above a &6Basin&r. Put ingredients in the basin and give the mixer rotation from the top.",
              "Some recipes need heat: put a &6Blaze Burner&r under the basin. Brass needs exactly that, and brass is where the next stage begins.",
          ],
          tasks=[task_item("create:mechanical_mixer", 1), task_item("create:basin", 1)],
          rewards=[reward_item("create:brass_ingot", 4), reward_table("uncommon")],
          deps=["belt"], icon="create:mechanical_mixer", size=1.5),

    quest("first_factory", 21, 0, "A Working Line",
          subtitle="Wheel, belt, press, chest. That is a factory.",
          description=[
              "Build one line that takes iron ingots from a chest, presses them on a belt and drops the sheets into another chest. Use &6Chutes&r or &6Funnels&r at both ends.",
              "When it runs on its own, you are done with the basics. Everything after this is bigger versions of the same idea.",
          ],
          tasks=[task_item("create:andesite_funnel", 2), task_item("create:chute", 2), task_item("create:iron_sheet", 32)],
          rewards=[reward_table("rare"), reward_xp(10)],
          deps=["mixer"], icon="create:andesite_funnel", size=1.75, shape="gear"),
]

chapter(C, "Create", "create:large_cogwheel", "tech", quests, shape="gear",
        subtitle=["Rotation, belts and the first machines."])
