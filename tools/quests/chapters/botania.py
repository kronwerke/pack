"""Botania: flowers, the Pure Daisy and a first mana pool. Manasteel and the runic altar open in stage 2."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "botania"

quests = [
    quest("welcome", 0, 0, "Botania",
          subtitle="Magic from flowers, no machines, no power cables.",
          description=[
              "Botania is technology made of plants. Special flowers make &bmana&r, Mana Spreaders shoot it across the base, Mana Pools store it and turn items into better items.",
              "",
              "The &6Lexica Botania&r is the whole manual. A book and a sapling, shapeless.",
          ],
          tasks=[task_item("botania:lexica_botania", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_table("s1_common")],
          icon="botania:lexica_botania", size=2.0, shape="hexagon"),

    quest("petals", 3, 0, "Mystical Petals",
          subtitle="Sixteen colours of flowers that only grow here.",
          description=[
              "Mystical Flowers grow in patches on grass in most biomes. Craft a flower into two petals. &6Floral Fertilizer&r on grass makes new ones grow.",
              "Collect every colour you find. Almost every Botania recipe is a list of petals.",
          ],
          tasks=[task_item("botania:white_mystical_petal", 8)],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["welcome"], icon="botania:white_mystical_flower"),

    quest("apothecary", 6, 0, "Petal Apothecary",
          subtitle="Where special flowers are made.",
          description=[
              "Fill the apothecary with a water bucket, throw in the petals of a recipe, then throw in a seed to finish it. The Lexica lists what each flower needs.",
          ],
          tasks=[task_item("botania:petal_apothecary", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 16)],
          deps=["petals"], icon="botania:petal_apothecary"),

    quest("pure_daisy", 9, 0, "Pure Daisy",
          subtitle="Turns stone and wood into their living versions.",
          description=[
              "Four white petals. Place the Pure Daisy and put stone or logs in the eight blocks around it. After a short while stone becomes &6Livingrock&r and logs become &6Livingwood&r.",
              "Make two or three daisies, you will need a lot of both.",
          ],
          tasks=[task_item("botania:pure_daisy", 1)],
          rewards=[reward_item("minecraft:stone", 32), reward_item("minecraft:oak_log", 16)],
          deps=["apothecary"], icon="botania:pure_daisy", size=1.5),

    quest("living", 12, 0, "Livingwood and Livingrock",
          subtitle="The building blocks of Botania.",
          description=["Everything that moves or holds mana is made of these two."],
          tasks=[task_item("botania:livingwood_log", 16), task_item("botania:livingrock", 32)],
          rewards=[reward_table("s1_common")],
          deps=["pure_daisy"], icon="botania:livingrock"),

    quest("wand", 15, -2, "Wand of the Forest",
          subtitle="Links, rotates and reads everything in Botania.",
          description=[
              "Livingwood twigs and petals. Look at a spreader, pool or flower with the wand to see its mana. Sneak and click a spreader, then click a pool or another spreader, to aim it there.",
          ],
          tasks=[task_item("botania:wand_of_the_forest", 1)],
          rewards=[reward_xp(5)],
          deps=["living"], icon="botania:wand_of_the_forest"),

    quest("endoflame", 15, 2, "Endoflame",
          subtitle="Burns fuel into mana.",
          description=[
              "Drop coal, charcoal, logs or any furnace fuel next to an Endoflame and it burns it for mana. Slow but steady, and it runs all night.",
              "Mana-making flowers only work when a spreader is close to collect their mana.",
          ],
          tasks=[task_item("botania:endoflame", 1)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["living"], icon="botania:endoflame"),

    quest("hydroangeas", 18, 3.5, "Hydroangeas",
          subtitle="Drinks still water for mana.",
          description=["Place it next to still water source blocks. It slowly drinks them and turns them into mana. Two infinite water sources keep it fed forever."],
          tasks=[task_item("botania:hydroangeas", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1)],
          deps=["endoflame"], optional=True),

    quest("spreader", 18, 0, "Mana Spreader",
          subtitle="Shoots mana from flowers to where it is needed.",
          description=[
              "Livingwood, a copper ingot and a petal. Place it near your flowers, it collects their mana automatically. Aim it at a pool with the wand.",
          ],
          tasks=[task_item("botania:mana_spreader", 1)],
          rewards=[reward_item("botania:livingwood_log", 8)],
          deps=["wand", "endoflame"], icon="botania:mana_spreader"),

    quest("pool", 21, 0, "Mana Pool",
          subtitle="Stores mana and changes items thrown into it.",
          description=[
              "Five livingrock in a U. A full pool holds a lot of mana. Throw an item in and, if the pool has enough mana, it comes back as something else. This is called &bmana infusion&r.",
              "A &6Diluted Mana Pool&r made from slabs is cheaper but much smaller.",
          ],
          tasks=[task_item("botania:mana_pool", 1)],
          rewards=[reward_table("s1_uncommon")],
          deps=["spreader"], icon="botania:mana_pool", size=1.5),

    quest("managlass", 24, -2, "Mana Infusion",
          subtitle="Your first infused item.",
          description=["Throw glass into a pool with mana. It comes back as &6Managlass&r, which lets mana bursts pass through."],
          tasks=[task_item("botania:managlass", 8)],
          rewards=[reward_item("minecraft:glass", 32)],
          deps=["pool"], icon="botania:managlass"),

    quest("mana_diamond", 24, 2, "Mana Diamond",
          subtitle="A diamond soaked in mana.",
          description=["A diamond in a full pool becomes a Mana Diamond. It costs a lot of mana, so make sure your flowers keep up."],
          tasks=[task_item("botania:mana_diamond", 1)],
          rewards=[reward_item("minecraft:diamond", 1)],
          deps=["pool"], optional=True),

    quest("farm", 27, 0, "A Mana Farm",
          subtitle="Enough flowers to keep a pool full.",
          description=[
              "Four Endoflames, two spreaders, one pool, and a hopper or a Create belt feeding them fuel. When it runs without you, you are ready for the next stage.",
              "Stage 2 opens the &6Runic Altar&r and &6Manasteel&r, and both drink a lot of mana. Start filling pools now.",
          ],
          tasks=[task_item("botania:endoflame", 4), task_item("botania:mana_spreader", 2)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["managlass"], icon="botania:mana_spreader", size=1.75, shape="gear"),
]

chapter(C, "Botania", "botania:pure_daisy", "magic", quests, shape="circle", order=3,
        subtitle=["Flowers, mana and the first pool."])
