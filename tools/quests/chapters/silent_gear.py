"""Silent Gear: tools built from parts, iron tier. Crimson iron and the good alloys open in stage 2."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "silent_gear"

quests = [
    quest("welcome", 0, 0, "Silent Gear",
          subtitle="Tools made from parts. The material decides everything.",
          description=[
              "A Silent Gear tool is a head and a rod, plus extras like a binding or a grip. Every material gives its own stats and traits, and you can mix them.",
              "",
              "It starts with dirt and cobblestone. Craft &6Crude Tool Parts&r: cobblestone, dirt and a stick.",
          ],
          tasks=[task_item("silentgear:crude_tool_parts", 4)],
          rewards=[reward_item("minecraft:cobblestone", 32), reward_table("s1_common")],
          icon="silentgear:pickaxe", size=2.0, shape="hexagon"),

    quest("stone_anvil", 3, -2, "Stone Anvil",
          subtitle="A workbench for knives.",
          description=["Cobblestone and dirt. Place a log on it and cut it with a knife."],
          tasks=[task_item("silentgear:stone_anvil", 1)],
          rewards=[reward_item("minecraft:oak_log", 16)],
          deps=["welcome"], icon="silentgear:stone_anvil"),

    quest("knife", 3, 2, "Crude Knife",
          subtitle="Cuts logs into template boards.",
          description=["Cobblestone and Crude Tool Parts. It breaks after a while, so make two."],
          tasks=[task_item("silentgear:crude_knife", 1)],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="silentgear:crude_knife"),

    quest("boards", 6, 0, "Template Boards",
          subtitle="Six boards from one log.",
          description=["Put a log on the Stone Anvil and use the knife on it. Boards become templates, templates become tool heads."],
          tasks=[task_item("silentgear:template_board", 12)],
          rewards=[reward_item("minecraft:oak_log", 16)],
          deps=["stone_anvil", "knife"], icon="silentgear:template_board"),

    quest("rods", 9, -2, "Rods",
          subtitle="The handle of every tool.",
          description=["A &6Rod Template&r and two sticks make four rods. Better rods (iron, bone, blaze) add their own stats later."],
          tasks=[task_item("silentgear:rod", 4)],
          rewards=[reward_item("minecraft:stick", 32)],
          deps=["boards"], icon="silentgear:rod"),

    quest("pickaxe_head", 9, 2, "Pickaxe Head",
          subtitle="A template and three of the same material.",
          description=[
              "Craft a &6Pickaxe Template&r from boards and sticks, then put it in the grid with three ingots or gems of one material. Iron is a good start.",
              "Templates are used up. A &6Blueprint&r made from Blueprint Paper does the same and can be used forever.",
          ],
          tasks=[task_item("silentgear:pickaxe_head", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8)],
          deps=["boards"], icon="silentgear:pickaxe_head"),

    quest("pickaxe", 12, 0, "Your Own Pickaxe",
          subtitle="Head plus rod.",
          description=[
              "Put the head and a rod in the crafting grid. Hover over the pickaxe to see its stats and traits. When it breaks, it does not vanish: it stays broken until you repair it.",
          ],
          tasks=[task_item("silentgear:pickaxe", 1)],
          rewards=[reward_table("s1_uncommon")],
          deps=["rods", "pickaxe_head"], icon="silentgear:pickaxe", size=1.5),

    quest("repair", 15, 2, "Repair Kit",
          subtitle="Fix your gear without losing it.",
          description=["Fill a repair kit with materials, then combine it with the damaged tool in the grid. The material should match what the tool is made of for the best result."],
          tasks=[task_item("silentgear:crude_repair_kit", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8)],
          deps=["pickaxe"], icon="silentgear:crude_repair_kit"),

    quest("blueprint", 15, -2, "Blueprints",
          subtitle="Reusable templates.",
          description=["Blueprint Paper makes blueprints that are never used up. Worth it for the tools you make again and again."],
          tasks=[task_item("silentgear:pickaxe_blueprint", 1)],
          rewards=[reward_item("minecraft:paper", 16)],
          deps=["pickaxe"], optional=True),

    quest("kit", 18, 0, "A Full Kit",
          subtitle="Sword and axe, your way.",
          description=[
              "Same idea, other templates: a sword blade and an axe head. Try different materials and compare the traits.",
              "Stage 2 opens &6Crimson Iron&r, &6Crimson Steel&r and &6Blaze Gold&r, the first materials that make Silent Gear really strong.",
          ],
          tasks=[task_item("silentgear:sword", 1), task_item("silentgear:axe", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(10)],
          deps=["repair"], icon="silentgear:sword", size=1.5, shape="gear"),
]

chapter(C, "Silent Gear", "silentgear:pickaxe", "storage", quests, shape="circle", order=6,
        subtitle=["Tools built from parts."])
