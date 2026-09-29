"""Food and farming: Farmer's Delight, Farming for Blockheads and Aquaculture."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "food"

quests = [
    quest("welcome", 0, 0, "Food and Farming",
          subtitle="Better food keeps you going longer.",
          description=[
              "Farmer's Delight adds real cooking: new crops, a cutting board, a cooking pot and meals that feed you for a long time and give useful effects.",
              "",
              "Start with a knife. A &6Flint Knife&r is flint and a stick, and it also cuts &6Straw&r from grass and wheat.",
          ],
          tasks=[task_item("farmersdelight:flint_knife", 1)],
          rewards=[reward_item("minecraft:bread", 16), reward_table("s1_common")],
          icon="farmersdelight:cooking_pot", size=2.0, shape="hexagon"),

    quest("cutting_board", 3, -2, "Cutting Board",
          subtitle="Place an item, click with a knife, get more out of it.",
          description=["Put food on the board and use a knife on it to slice it. With an axe it strips logs and gives bark, with a pickaxe it breaks blocks down."],
          tasks=[task_item("farmersdelight:cutting_board", 1)],
          rewards=[reward_item("minecraft:beef", 8)],
          deps=["welcome"], icon="farmersdelight:cutting_board"),

    quest("wild_crops", 3, 2, "Wild Crops",
          subtitle="Tomatoes, onions and cabbage grow wild.",
          description=[
              "Wild crops grow in small patches all over the world. Break them for the crop and plant it at home. Cabbage and beets like the coast, tomatoes like it warm.",
          ],
          tasks=[task_item("farmersdelight:tomato", 4), task_item("farmersdelight:onion", 4),
                 task_item("farmersdelight:cabbage", 4)],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["welcome"], icon="farmersdelight:tomato"),

    quest("rice", 6, 4, "Rice",
          subtitle="Grows in water.",
          description=["Wild rice grows in shallow water in swamps and along rivers. Plant it in water one block deep."],
          tasks=[task_item("farmersdelight:rice", 8)],
          rewards=[reward_item("minecraft:water_bucket", 1)],
          deps=["wild_crops"], optional=True),

    quest("cooking_pot", 6, 0, "Cooking Pot",
          subtitle="Soups, stews and meals that last.",
          description=[
              "The pot needs heat underneath: a campfire, a &6Stove&r, or fire. Put the ingredients in, and a bowl in the container slot to serve.",
              "Meals give &6Nourishment&r (your food bar does not drop while it lasts) or &6Comfort&r (you regenerate however hungry you are).",
          ],
          tasks=[task_item("farmersdelight:cooking_pot", 1)],
          rewards=[reward_item("minecraft:bowl", 16), reward_item("minecraft:campfire", 1)],
          deps=["cutting_board", "wild_crops"], icon="farmersdelight:cooking_pot", size=1.5),

    quest("soup", 9, 0, "A Proper Meal",
          subtitle="Your first soup.",
          description=["A Vegetable Soup is easy and filling. Try the other recipes in JEI, they get better as you go."],
          tasks=[task_item("farmersdelight:vegetable_soup", 4)],
          rewards=[reward_table("s1_common")],
          deps=["cooking_pot"], icon="farmersdelight:vegetable_soup"),

    quest("rich_soil", 9, -3.5, "Rich Soil",
          subtitle="Crops grow faster on it.",
          description=[
              "&6Organic Compost&r slowly turns into &6Rich Soil&r. Sun, water and mushrooms nearby make it go faster. Crops on Rich Soil grow faster, and mushrooms grow into colonies on it.",
          ],
          tasks=[task_item("farmersdelight:rich_soil", 8)],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["cooking_pot"], optional=True),

    quest("market", 12, 0, "The Market",
          subtitle="Buy seeds and saplings for emeralds.",
          description=["A &6Market&r sells seeds, saplings and flowers from all over the world. Handy for crops you cannot find nearby."],
          tasks=[task_item("farmingforblockheads:market", 1)],
          rewards=[reward_item("minecraft:emerald", 8)],
          deps=["soup"], icon="farmingforblockheads:market"),

    quest("fishing", 12, 3.5, "Better Fishing",
          subtitle="New fish, new rods.",
          description=["Aquaculture adds fish for every biome, better rods and a tackle box. An iron rod is enough to start."],
          tasks=[task_item("aquaculture:iron_fishing_rod", 1)],
          rewards=[reward_item("minecraft:cod", 16)],
          deps=["soup"], optional=True),

    quest("pantry", 15, 0, "A Full Pantry",
          subtitle="Cook for the whole base.",
          description=[
              "A pot of stew for everyone who plays with you. Later, with Create's brass machines, Create Central Kitchen lets you automate the cooking.",
          ],
          tasks=[task_item("farmersdelight:vegetable_soup", 16)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["market"], icon="farmersdelight:vegetable_soup", size=1.5, shape="gear"),
]

chapter(C, "Food and Farming", "farmersdelight:cooking_pot", "world", quests, shape="circle", order=4,
        subtitle=["Crops, cooking and meals that last."])
