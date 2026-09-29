"""Exploration: getting around, the Mining Dimension, structures and their loot."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, reward_item,
                  reward_table, reward_xp)

C = "exploration"
MINING = "ultimate_mining_dimension:ultimate_mining_dimension"

quests = [
    quest("welcome", 0, 0, "Exploration",
          subtitle="The world is bigger and stranger than vanilla.",
          description=[
              "New terrain, new biomes, and a lot of new structures: villages, towers, dungeons, ruins and a few places you should not visit alone.",
              "",
              "Loot is per player. Every chest in a structure has its own loot for each person who opens it, so arriving second is not a loss.",
          ],
          tasks=[task_checkmark("Let's go outside")],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_table("s1_common")],
          icon="minecraft:filled_map", size=2.0, shape="hexagon"),

    quest("compass", 3, -2, "Nature's Compass",
          subtitle="Points you to any biome.",
          description=["Pick a biome from the list and the compass points to the nearest one. Archwood Forests for Ars Nouveau are the classic first search."],
          tasks=[task_item("naturescompass:naturescompass", 1)],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["welcome"], icon="naturescompass:naturescompass"),

    quest("warp_stone", 3, 2, "Warp Stone",
          subtitle="Travel between the waystones you have found.",
          description=[
              "Waystones stand in villages and along the roads. Right click one to activate it, and from then on you can travel to it from any other waystone.",
              "A &6Warp Stone&r lets you do that from anywhere, with a cooldown.",
          ],
          tasks=[task_item("waystones:warp_stone", 1)],
          rewards=[reward_item("waystones:return_scroll", 2)],
          deps=["welcome"], icon="waystones:warp_stone"),

    quest("waystone", 6, 2, "Your Own Waystone",
          subtitle="Put one at your base.",
          description=["A waystone at home means one click back from anywhere you have been. Name it so everyone can find you."],
          tasks=[task_item("waystones:waystone", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["warp_stone"], icon="waystones:waystone"),

    quest("mining_pickaxe", 6, -2, "The Enchanted Pickaxe",
          subtitle="The key to the Mining Dimension.",
          description=[
              "A second world made for digging: the same ores and geodes as the overworld, and nobody minds the holes. Keep the overworld pretty and strip mine down there.",
              "",
              "Craft the &6Enchanted Pickaxe&r from two diamonds, a gold block and two sticks. Build a frame of &6Iron Blocks&r shaped like a Nether portal and use the pickaxe on the inside of the frame.",
          ],
          tasks=[task_item(MINING, 1)],
          rewards=[reward_item("minecraft:iron_block", 4)],
          deps=["compass"], icon=MINING),

    quest("mining_dimension", 9, -2, "Into the Mine",
          subtitle="Step through.",
          description=[
              "Bring torches, food and a way home. Cobblestone from down here counts for the community goal just the same.",
              "&cDeath in the Mining Dimension leaves your body down there.&r Note where the portal is.",
          ],
          tasks=[task_dimension(MINING)],
          rewards=[reward_table("s1_uncommon")],
          deps=["mining_pickaxe"], icon="minecraft:iron_pickaxe", size=1.5),

    quest("salvaging", 9, 2, "Loot with Affixes",
          subtitle="Named gear from mobs, and what to do with it.",
          description=[
              "Mobs and chests drop gear with random &6affixes&r: extra damage, life steal, faster mining. The rarer the colour of the name, the stronger the affixes.",
              "Gear you do not want goes into a &6Salvaging Table&r and comes out as materials. Some drops carry &6Gems&r you can socket into your own gear.",
          ],
          tasks=[task_item("apotheosis:salvaging_table", 1)],
          rewards=[reward_item("apotheosis:gem_dust", 8)],
          deps=["waystone"], icon="apotheosis:salvaging_table"),

    quest("mimic", 12, 3.5, "Not a Chest",
          subtitle="Some chests bite back.",
          description=["Every now and then a chest in a structure is a &6Mimic&r. It hits hard, and it drops an artifact: a trinket with a special effect that you wear."],
          tasks=[task_kill("artifacts:mimic", 1)],
          rewards=[reward_table("s1_uncommon")],
          deps=["salvaging"], optional=True),

    quest("explorer", 12, 0, "Explorer",
          subtitle="Out there and back again.",
          description=[
              "You know how to find biomes, travel between waystones and mine in a world made for it.",
              "The Nether opens with stage 2, on stream, through the portal at spawn. Save a few iron blocks for the trip.",
          ],
          tasks=[task_checkmark("I have been around")],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["mining_dimension", "salvaging"], icon="minecraft:map", size=1.5, shape="gear"),
]

chapter(C, "Exploration", "minecraft:filled_map", "world", quests, shape="circle", order=7,
        subtitle=["Biomes, waystones, the Mining Dimension and loot."])
