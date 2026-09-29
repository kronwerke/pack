"""The Nether: opened on stream at the start of stage 2. What to bring back and why."""
from ftbq import chapter, quest, task_item, task_dimension, task_kill, reward_item, reward_table, reward_xp

C = "nether"

quests = [
    quest("welcome", 0, 0, "The Nether",
          subtitle="Lit on stream. Now it is everyone's.",
          description=[
              "The portal at spawn was lit when the first community goal was filled. From now on anyone can build their own portal, or walk through the one at spawn.",
              "",
              "Bring fire resistance, a shield and blocks you do not mind losing. Ghasts break wood and cobblestone, not cobbled deepslate.",
              "",
              "Almost everything in stage 2 needs something from down here: blaze rods for Create, quartz for electron tubes, glowstone and more.",
          ],
          tasks=[task_dimension("minecraft:the_nether")],
          rewards=[reward_item("minecraft:fire_charge", 4), reward_table("s2_common")],
          icon="minecraft:netherrack", size=2.0, shape="hexagon"),

    quest("quartz", 3, -2, "Nether Quartz",
          subtitle="Everywhere in the walls, and Create wants it.",
          description=[
              "Quartz ore is all over the Nether. Craft quartz with redstone for &6Rose Quartz&r, polish it with sandpaper, and you have what Create's &6Electron Tubes&r are made of.",
          ],
          tasks=[task_item("minecraft:quartz", 32)],
          rewards=[reward_item("minecraft:redstone", 32)],
          deps=["welcome"]),

    quest("glowstone", 3, 2, "Glowstone",
          subtitle="Hanging from the ceiling, over the lava.",
          description=[
              "Glowstone hangs from the Nether ceiling. Silk touch keeps the block, anything else gives dust. Bring a block to stand on.",
          ],
          tasks=[task_item("minecraft:glowstone_dust", 16)],
          rewards=[reward_item("minecraft:glowstone_dust", 16)],
          deps=["welcome"]),

    quest("fortress", 6, 0, "Blaze Rods",
          subtitle="Find a fortress and its spawners.",
          description=[
              "Nether fortresses are the long bridges and halls of dark brick. Blazes spawn from spawners inside. Kill a few for rods.",
              "",
              "Leave one spawner standing. Create's &6Blaze Burner&r needs a live blaze: right click one with an &6Empty Blaze Burner&r and it goes into the cage.",
          ],
          tasks=[task_kill("minecraft:blaze", 5), task_item("minecraft:blaze_rod", 4)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_table("s2_uncommon")],
          deps=["quartz", "glowstone"], icon="minecraft:blaze_rod", size=1.5),

    quest("wart", 9, -2, "Nether Wart",
          subtitle="The base of every potion.",
          description=[
              "Nether Wart grows on soul sand in fortress stairwells. Plant it at home and you can brew. Fire resistance first.",
          ],
          tasks=[task_item("minecraft:nether_wart", 8)],
          rewards=[reward_item("minecraft:brewing_stand", 1), reward_item("minecraft:glass_bottle", 6)],
          deps=["fortress"], optional=True),

    quest("debris", 9, 2, "Ancient Debris",
          subtitle="Deep down, blast resistant, worth it.",
          description=[
              "Ancient Debris sits low in the Nether, around Y 15. It does not glow and does not burn. Beds explode in the Nether, which is one way to dig. TNT is another.",
              "Four scraps and four gold make one netherite ingot.",
          ],
          tasks=[task_item("minecraft:ancient_debris", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_table("s2_rare"), reward_xp(10)],
          deps=["fortress"], icon="minecraft:ancient_debris", size=1.5, shape="diamond"),
]

chapter(C, "The Nether", "minecraft:netherrack", "world", quests, shape="circle", order=8, stage=2,
        subtitle=["Stage 2. Quartz, blaze rods and the rest of what the machines need."])
