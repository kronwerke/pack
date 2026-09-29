"""Create in stage 2: zinc, the blaze burner, brass and the precision mechanism."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "create_brass"

quests = [
    quest("welcome", 0, 0, "Brass",
          subtitle="Create's second half starts with one alloy.",
          description=[
              "Everything with a brass casing does something smarter than the andesite machines: filters, sorts, counts, builds. Brass is copper and zinc mixed in a heated basin.",
              "",
              "The obelisk wants &64 000 brass ingots&r and &6300 precision mechanisms&r for this stage. Every factory in this chapter helps with that.",
          ],
          tasks=[task_item("create:brass_ingot", 1)],
          rewards=[reward_item("create:brass_ingot", 8), reward_table("s2_common")],
          icon="create:brass_ingot", size=2.0, shape="hexagon"),

    quest("zinc", 3, -2, "Zinc",
          subtitle="In the overworld stone, deepslate too.",
          description=[
              "Zinc ore sits in the overworld, in stone and deepslate. Mine it by hand, or put raw zinc through a millstone or crushing wheels for crushed zinc, which washes into extra nuggets.",
          ],
          tasks=[task_item("create:zinc_ingot", 16)],
          rewards=[reward_item("create:zinc_ingot", 16)],
          deps=["welcome"]),

    quest("burner", 3, 2, "Blaze Burner",
          subtitle="Heat for the basin. Needs a mage and a blaze.",
          description=[
              "The &6Empty Blaze Burner&r takes iron sheets, netherrack and, on this server, two &6Source Gems&r from Ars Nouveau. Ask a mage, or become one.",
              "",
              "Take it into the Nether and right click a blaze with it. Place the burner under a basin and feed it any furnace fuel. A &6Blaze Cake&r makes it superheated for the hottest recipes.",
          ],
          tasks=[task_item("create:blaze_burner", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_table("s2_common")],
          deps=["welcome"], icon="create:blaze_burner", size=1.5),

    quest("mixing", 6, 0, "Mixing Brass",
          subtitle="Copper and zinc, heated, stirred.",
          description=[
              "Mixer on top, basin in the middle, lit blaze burner at the bottom. One copper and one zinc ingot make two brass ingots. Funnels in and out and it runs by itself.",
          ],
          tasks=[task_item("create:brass_ingot", 64)],
          rewards=[reward_item("minecraft:copper_ingot", 32), reward_item("create:zinc_ingot", 32)],
          deps=["zinc", "burner"]),

    quest("casing", 9, -2, "Brass Casing",
          subtitle="The frame of every smart machine.",
          description=[
              "Right click a stripped log with a brass ingot. Botania players will ask you for two of these: the Terrestrial Agglomeration Plate needs them on this server.",
          ],
          tasks=[task_item("create:brass_casing", 16)],
          rewards=[reward_item("minecraft:stripped_oak_log", 16)],
          deps=["mixing"]),

    quest("tube", 9, 2, "Electron Tube",
          subtitle="Rose quartz, polished, on an iron sheet.",
          description=[
              "Craft nether quartz with redstone for &6Rose Quartz&r, polish it with sandpaper, then combine it with an iron sheet. Every brass machine with logic in it uses these.",
          ],
          tasks=[task_item("create:electron_tube", 8)],
          rewards=[reward_item("minecraft:redstone", 32), reward_item("create:polished_rose_quartz", 4)],
          deps=["mixing"]),

    quest("funnels", 12, -3, "Brass Funnels and Tunnels",
          subtitle="Filters on everything.",
          description=[
              "A &6Brass Funnel&r takes a filter and a stack size. A &6Brass Tunnel&r on a belt splits items evenly between belts, or sends them where you tell it.",
          ],
          tasks=[task_item("create:brass_funnel", 4), task_item("create:brass_tunnel", 4)],
          rewards=[reward_item("create:brass_ingot", 16)],
          deps=["casing"]),

    quest("deployer", 12, 0, "Deployer",
          subtitle="A hand that uses whatever it holds.",
          description=[
              "The &6Deployer&r does what a player would do with the item in it: place, use, attack. On a belt it applies items to whatever passes under it.",
              "It is the heart of sequenced assembly, which comes next.",
          ],
          tasks=[task_item("create:deployer", 2)],
          rewards=[reward_item("create:andesite_alloy", 32), reward_table("s2_common")],
          deps=["casing", "tube"]),

    quest("crafter", 12, 3, "Mechanical Crafters",
          subtitle="Big recipes, done by machines.",
          description=[
              "Place crafters in a grid, connect them with the wrench so they point at each other, put the ingredients in, and give them rotation. Some recipes are larger than 3x3 and only work here.",
          ],
          tasks=[task_item("create:mechanical_crafter", 9)],
          rewards=[reward_item("create:electron_tube", 4)],
          deps=["tube"], optional=True),

    quest("precision", 15, 0, "Precision Mechanism",
          subtitle="Your first sequenced assembly line.",
          description=[
              "A gold sheet goes on a belt. A deployer adds a cogwheel, the next a large cogwheel, the next an iron nugget. Five rounds of that and it becomes a &6Precision Mechanism&r. Sometimes it fails and you get scrap.",
              "",
              "Loop the belt back so unfinished pieces go round again. JEI shows every step.",
          ],
          tasks=[task_item("create:precision_mechanism", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 16), reward_table("s2_uncommon")],
          deps=["deployer"], icon="create:precision_mechanism", size=1.5, shape="gear"),

    quest("arm", 18, -2, "Mechanical Arm",
          subtitle="Picks up here, puts down there.",
          description=[
              "Hold the arm and click the blocks it should take from and put into before placing it. It only reaches a few blocks, so build compact.",
          ],
          tasks=[task_item("create:mechanical_arm", 1)],
          rewards=[reward_item("create:brass_ingot", 16)],
          deps=["precision"]),

    quest("crushing", 18, 2, "Crushing Wheels",
          subtitle="More out of every ore.",
          description=[
              "Two crushing wheels spinning towards each other. Raw ore dropped between them comes out as crushed ore plus a chance of extras. Wash it with a fan through water for nuggets on top.",
          ],
          tasks=[task_item("create:crushing_wheel", 2)],
          rewards=[reward_item("minecraft:raw_iron", 32)],
          deps=["precision"]),

    quest("steam", 21, 0, "Steam Engine",
          subtitle="Serious stress capacity.",
          description=[
              "Blaze burners under a fluid tank, water pumped in, steam engines on the side of the tank, a shaft on each engine. The bigger the tank and the more burners, the more power.",
              "The goggles show how much heat and water the boiler has. Aim for a level where both are balanced.",
          ],
          tasks=[task_item("create:steam_engine", 2), task_item("create:fluid_tank", 4)],
          rewards=[reward_item("minecraft:coal_block", 16), reward_table("s2_uncommon")],
          deps=["arm", "crushing"], icon="create:steam_engine", size=1.5),

    quest("engine", 24, 0, "The Brass Engine",
          subtitle="Feed the obelisk.",
          description=[
              "A brass line and a precision line that run without you. Bring what they make to the obelisk and the whole server moves.",
          ],
          tasks=[task_item("create:brass_ingot", 256), task_item("create:precision_mechanism", 32)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["steam"], icon="create:precision_mechanism", size=1.75, shape="gear"),
]

chapter(C, "Create: Brass", "create:brass_casing", "tech", quests, shape="gear", order=9, stage=2,
        subtitle=["Stage 2. Blaze burners, brass and the first real automation."])
