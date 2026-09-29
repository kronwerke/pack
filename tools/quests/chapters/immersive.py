"""Immersive Engineering in stage 2: coke, treated wood, the blast furnace and the first wires."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp

C = "immersive"

quests = [
    quest("welcome", 0, 0, "Immersive Engineering",
          subtitle="Big machines you walk around in.",
          description=[
              "Immersive Engineering builds its machines as multiblocks: stack the right blocks in the right shape, hit them with the &6Engineer's Hammer&r, and they become one machine.",
              "",
              "The &6Engineer's Manual&r shows every structure layer by layer. Read it before you build.",
          ],
          tasks=[task_item("immersiveengineering:manual", 1), task_item("immersiveengineering:hammer", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s2_common")],
          icon="immersiveengineering:hammer", size=2.0, shape="hexagon"),

    quest("coke_oven", 3, 0, "Coke Oven",
          subtitle="Twenty seven bricks, one machine.",
          description=[
              "Build a 3x3x3 cube of &6Coke Bricks&r and hit the middle of one side with the hammer. Coal goes in, &6Coal Coke&r and &6Creosote Oil&r come out. Put a bucket in the oven to take the creosote.",
          ],
          tasks=[task_item("immersiveengineering:cokebrick", 27)],
          rewards=[reward_item("minecraft:clay_ball", 32), reward_item("minecraft:coal", 32)],
          deps=["welcome"], icon="immersiveengineering:cokebrick", size=1.5),

    quest("coke", 6, -2, "Coal Coke",
          subtitle="Hotter than coal, and it makes steel.",
          description=[
              "Coal coke burns longer than coal and is what the blast furnace wants. Start stockpiling.",
          ],
          tasks=[task_item("immersiveengineering:coal_coke", 32)],
          rewards=[reward_item("minecraft:coal_block", 8)],
          deps=["coke_oven"]),

    quest("treated_wood", 6, 2, "Treated Wood",
          subtitle="Planks that do not rot.",
          description=[
              "Craft planks with a bucket of creosote oil. Treated wood is in half the machines of this mod, and the sticks go into the windmill.",
          ],
          tasks=[task_item("immersiveengineering:treated_wood_horizontal", 16)],
          rewards=[reward_item("minecraft:oak_planks", 32)],
          deps=["coke_oven"]),

    quest("blast_furnace", 9, -2, "Blast Furnace",
          subtitle="Iron in, steel out.",
          description=[
              "Another 3x3x3 cube, this time of &6Blast Bricks&r, which need things from the Nether. Iron and coal coke go in, &6Steel&r comes out, slowly.",
              "Steel from here counts for the stage 3 goal exactly like Mekanism steel.",
          ],
          tasks=[task_item("immersiveengineering:blastbrick", 27)],
          rewards=[reward_item("minecraft:iron_ingot", 32), reward_table("s2_uncommon")],
          deps=["coke"], icon="immersiveengineering:blastbrick", size=1.5),

    quest("steel", 12, -2, "Steel",
          subtitle="The first ingots.",
          description=[
              "Run the blast furnace. It takes a while per ingot, so build two and keep them fed.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 16)],
          rewards=[reward_item("immersiveengineering:coal_coke", 16)],
          deps=["blast_furnace"]),

    quest("windmill", 9, 2, "Windmill and Kinetic Dynamo",
          subtitle="Rotation to power.",
          description=[
              "A &6Windmill&r or &6Water Wheel&r turns a &6Kinetic Dynamo&r, which puts out power. Windmills work better high up with open space around them.",
          ],
          tasks=[task_item("immersiveengineering:windmill", 1), task_item("immersiveengineering:dynamo", 1)],
          rewards=[reward_item("immersiveengineering:treated_wood_horizontal", 16)],
          deps=["treated_wood"], icon="immersiveengineering:windmill", size=1.5),

    quest("wires", 12, 2, "Copper Wire",
          subtitle="Power on poles, across the base.",
          description=[
              "Place &6LV Wire Connectors&r on the dynamo and the machines, then right click them one after the other with a &6Copper Wire Coil&r. Wires hang in the air and can span long distances.",
          ],
          tasks=[task_item("immersiveengineering:wirecoil_copper", 4), task_item("immersiveengineering:connector_lv", 4)],
          rewards=[reward_item("minecraft:copper_ingot", 32)],
          deps=["windmill"]),

    quest("capacitor", 15, 2, "LV Capacitor",
          subtitle="Keep the power for later.",
          description=[
              "Stores power for when the wind drops. Put it between the dynamo and the machines.",
          ],
          tasks=[task_item("immersiveengineering:capacitor_lv", 1)],
          rewards=[reward_table("s2_common")],
          deps=["wires"], optional=True),

    quest("engineer", 15, -2, "An Engineer",
          subtitle="Steel by the stack.",
          description=[
              "The stage 3 goal asks for thousands of steel. Two or three blast furnaces running now make that a lot less painful later.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 64)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["steel"], icon="immersiveengineering:ingot_steel", size=1.75, shape="gear"),
]

chapter(C, "Immersive Engineering", "immersiveengineering:hammer", "tech", quests, shape="square", order=14, stage=2,
        subtitle=["Stage 2. Coke, treated wood, steel and wires."])
