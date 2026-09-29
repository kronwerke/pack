"""Ars Nouveau: from a book and four iron tools to Source, glyphs and the first Starbuncle."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "ars_nouveau"

quests = [
    quest("welcome", 0, 0, "Ars Nouveau",
          subtitle="Build your own spells, one glyph at a time.",
          description=[
              "In Ars Nouveau you write spells yourself. A spell is a form (how it is cast), then effects (what it does), then augments (how strong, how wide).",
              "",
              "Everything runs on &dSource&r, the magic energy of the mod. Source Gems are also half of the first community goal, so every mage on the server helps the whole server move on.",
              "",
              "The &6Worn Notebook&r explains every block and glyph in detail.",
          ],
          tasks=[task_checkmark("Open the notebook")],
          rewards=[reward_item("ars_nouveau:worn_notebook", 1), reward_table("s1_common")],
          icon="ars_nouveau:novice_spell_book", size=2.0, shape="hexagon"),

    quest("archwood", 3, -2, "Archwood",
          subtitle="The wood of every Ars block.",
          description=[
              "Archwood trees grow in their own forests: red, blue, green and purple leaves, easy to spot from far away. Every colour works for planks.",
              "Take saplings home. Blazing (red) Archwood logs are the best fuel for a Volcanic Sourcelink later.",
          ],
          tasks=[task_item("ars_nouveau:archwood_planks", 32)],
          rewards=[reward_item("ars_nouveau:blue_archwood_log", 16)],
          deps=["welcome"], icon="ars_nouveau:blue_archwood_log"),

    quest("book", 3, 2, "Novice Spell Book",
          subtitle="A book and a full set of iron tools.",
          description=[
              "Craft a book with an iron sword, pickaxe, axe and shovel. The book holds your spells; switch between them with the spell radial menu (the key is under Controls, Ars Nouveau).",
              "Right click to cast. Your mana bar shows how much you have left.",
          ],
          tasks=[task_item("ars_nouveau:novice_spell_book", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["welcome"], icon="ars_nouveau:novice_spell_book"),

    quest("scribes_table", 6, 0, "Scribe's Table",
          subtitle="Where new glyphs are made.",
          description=[
              "Use your spell book on the table to see every glyph you can learn. Pick one, throw the listed items onto the table, and it scribes the glyph for you. Each glyph also costs experience.",
          ],
          tasks=[task_item("ars_nouveau:scribes_table", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8)],
          deps=["archwood", "book"], icon="ars_nouveau:scribes_table"),

    quest("first_glyph", 9, -2, "Let There Be Light",
          subtitle="Your first glyph of your own.",
          description=[
              "Scribe the &6Light&r glyph and put it in a spell: Projectile, then Light. Cast it at a cave wall and you have a torch that never needs placing.",
              "Every novice glyph costs the same experience, so learn the ones you will use every day first.",
          ],
          tasks=[task_item("ars_nouveau:glyph_light", 1)],
          rewards=[reward_xp(10)],
          deps=["scribes_table"], icon="ars_nouveau:glyph_light"),

    quest("harvest_glyph", 12, -3.5, "Harvest",
          subtitle="Crops in one cast.",
          description=["Touch, Harvest, then an area augment: a whole field harvested in one click. Worth it on day one."],
          tasks=[task_item("ars_nouveau:glyph_harvest", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 32)],
          deps=["first_glyph"], optional=True),

    quest("imbuement", 9, 2, "Imbuement Chamber",
          subtitle="Turns amethyst into Source Gems.",
          description=[
              "Put an &6Amethyst Shard&r or &6Lapis&r into the chamber and wait. On its own it gathers Source slowly; with a filled Source Jar within two blocks it works much faster.",
              "Amethyst geodes are common underground and in the Mining Dimension. Take a Budding Amethyst home if you can.",
          ],
          tasks=[task_item("ars_nouveau:imbuement_chamber", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 32)],
          deps=["scribes_table"], icon="ars_nouveau:imbuement_chamber", size=1.5),

    quest("source_gems", 12, 2, "Source Gems",
          subtitle="The magic half of the first community goal.",
          description=[
              "Source Gems go into almost every Ars block, and the server needs &e1 500&r of them (scaled to the number of players) for the next stage.",
              "Make a few for yourself, then set up chambers and put the rest in with &e/kw deposit&r.",
          ],
          tasks=[task_item("ars_nouveau:source_gem", 16)],
          rewards=[reward_table("s1_uncommon")],
          deps=["imbuement"], icon="ars_nouveau:source_gem"),

    quest("source_jar", 15, 0, "Source Jar",
          subtitle="Stores Source for everything around it.",
          description=[
              "A Source Jar holds Source made by Sourcelinks nearby and hands it to machines close to it. A comparator reads how full it is.",
          ],
          tasks=[task_item("ars_nouveau:source_jar", 2)],
          rewards=[reward_item("minecraft:glass", 16)],
          deps=["source_gems"], icon="ars_nouveau:source_jar"),

    quest("volcanic", 18, -2, "Volcanic Sourcelink",
          subtitle="Burns fuel into Source.",
          description=[
              "Put burnable items next to it or on a pedestal and it turns them into Source for the jars nearby. Archwood logs give more, Blazing Archwood the most.",
              "It also heats the ground: stone around it slowly turns into magma and lava. Build it on something that may melt.",
          ],
          tasks=[task_item("ars_nouveau:volcanic_sourcelink", 1)],
          rewards=[reward_item("ars_nouveau:red_archwood_log", 16)],
          deps=["source_jar"], icon="ars_nouveau:volcanic_sourcelink"),

    quest("agronomic", 18, 2, "Agronomic Sourcelink",
          subtitle="Crops that grow make Source.",
          description=[
              "Every crop and tree that grows within 15 blocks gives Source. Magical plants like Mageblooms, Sourceberries and Archwood saplings give more. Bonemeal does not count.",
          ],
          tasks=[task_item("ars_nouveau:agronomic_sourcelink", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["source_jar"], icon="ars_nouveau:agronomic_sourcelink", optional=True),

    quest("sourcestone", 21, 0, "Sourcestone",
          subtitle="Stone with a gem in it. The base of every altar.",
          description=["Eight stone around one Source Gem. You need it for pedestals and the Arcane Core, and it looks good in a mage tower."],
          tasks=[task_item("ars_nouveau:sourcestone", 16)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["volcanic"], icon="ars_nouveau:sourcestone"),

    quest("apparatus", 24, 0, "Enchanting Apparatus",
          subtitle="The crafting altar of Ars Nouveau.",
          description=[
              "Place the &6Enchanting Apparatus&r on top of an &6Arcane Core&r, and &6Arcane Pedestals&r around it. The item in your hand goes into the apparatus, the rest onto the pedestals.",
              "Most of the good Ars items are made here: charms, trinkets, enchanted tools.",
          ],
          tasks=[task_item("ars_nouveau:enchanting_apparatus", 1), task_item("ars_nouveau:arcane_core", 1),
                 task_item("ars_nouveau:arcane_pedestal", 4)],
          rewards=[reward_table("s1_uncommon"), reward_xp(10)],
          deps=["sourcestone"], icon="ars_nouveau:enchanting_apparatus", size=1.5),

    quest("starbuncle", 27, -2, "Starbuncle",
          subtitle="A small helper that carries items for you.",
          description=[
              "Wild Starbuncles live in forests and love gold nuggets. Hold one out, let a Starbuncle take it, and it leaves a &6Starbuncle Token&r behind.",
              "Put the token in the apparatus with four gold ingots on the pedestals to get a &6Starbuncle Charm&r. Use the charm on the ground and your Starbuncle moves items from chest to chest, set up with the Dominion Wand.",
          ],
          tasks=[task_item("ars_nouveau:starbuncle_charm", 1)],
          rewards=[reward_item("minecraft:gold_nugget", 32), reward_xp(10)],
          deps=["apparatus"], icon="ars_nouveau:starbuncle_charm"),

    quest("trinkets", 27, 2, "Mage Trinkets",
          subtitle="More mana, faster mana.",
          description=[
              "A &6Ring of Potential&r raises your maximum mana. Later rings and amulets from the apparatus add more mana and faster regeneration.",
          ],
          tasks=[task_item("ars_nouveau:ring_of_potential", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8)],
          deps=["apparatus"], icon="ars_nouveau:ring_of_potential", optional=True),

    quest("dowsing", 24, 3.5, "Dowsing Rod",
          subtitle="Find amethyst through walls.",
          description=["Use it and nearby Budding Amethyst lights up through the stone for a while. Ideal before a mining trip for Source Gems."],
          tasks=[task_item("ars_nouveau:dowsing_rod", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 16)],
          deps=["apparatus"], optional=True),

    quest("mage", 30, 0, "A Proper Mage",
          subtitle="Source running, altar built, gems for the server.",
          description=[
              "You have a working Source setup and an altar. Put the extra gems into the community goal, and keep a stack for yourself: the next stage opens the Mage's Spell Book, Source Relays and rituals, and they all want gems.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 4)],
          rewards=[reward_table("s1_rare"), reward_xp(15)],
          deps=["starbuncle"], icon="ars_nouveau:source_gem_block", size=1.75, shape="gear"),
]

chapter(C, "Ars Nouveau", "ars_nouveau:novice_spell_book", "magic", quests, shape="circle", order=2,
        subtitle=["Glyphs, Source and the first familiar."])
