"""Ars Nouveau in stage 2: the Mage's Spell Book, moving Source, rituals and turrets."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp

C = "ars_apprentice"

quests = [
    quest("welcome", 0, 0, "Mage's Spell Book",
          subtitle="The second book: more slots, stronger glyphs.",
          description=[
              "Stage 2 opens the apprentice glyphs and the book that can hold them. Craft the &6Mage's Spell Book&r from your novice book, JEI shows the rest. The glyphs you know stay known.",
              "",
              "Ars is also where Create gets its heat on this server: every Empty Blaze Burner needs two Source Gems. Engineers will come knocking.",
          ],
          tasks=[task_item("ars_nouveau:apprentice_spell_book", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 16), reward_table("s2_common")],
          icon="ars_nouveau:apprentice_spell_book", size=2.0, shape="hexagon"),

    quest("relay", 3, -2, "Source Relay",
          subtitle="Source over distance, no jars in a row.",
          description=[
              "A &6Source Relay&r pulls Source from one place and sends it to another. Link them with the &6Dominion Wand&r: click the source, then the relay, then the target.",
              "Put your sourcelinks at the farm and the jars where you work.",
          ],
          tasks=[task_item("ars_nouveau:relay", 2)],
          rewards=[reward_item("ars_nouveau:source_gem", 8)],
          deps=["welcome"]),

    quest("splitter", 6, -3.5, "Relay: Splitter",
          subtitle="One source, many targets.",
          description=[
              "The splitter shares its Source evenly between everything it is linked to. Useful when the imbuement chamber and the apparatus both need feeding.",
          ],
          tasks=[task_item("ars_nouveau:relay_splitter", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8)],
          deps=["relay"], optional=True),

    quest("brazier", 3, 2, "Ritual Brazier",
          subtitle="Where rituals burn.",
          description=[
              "Place a ritual tablet on the &6Ritual Brazier&r and right click it to start. Many rituals draw Source from jars nearby while they run.",
          ],
          tasks=[task_item("ars_nouveau:ritual_brazier", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          deps=["welcome"], icon="ars_nouveau:ritual_brazier", size=1.5),

    quest("harvest", 6, 1, "Ritual of Harvest",
          subtitle="The crops harvest themselves.",
          description=[
              "Harvests the crops around the brazier and costs a little Source each time. Put a chest next to the brazier and the harvest goes straight in.",
          ],
          tasks=[task_item("ars_nouveau:ritual_harvest", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 32), reward_item("minecraft:bone_meal", 32)],
          deps=["brazier"]),

    quest("scrying", 6, 3.5, "Ritual of Scrying",
          subtitle="See one block through all the others.",
          description=[
              "Give the ritual a block, and for a while you see every block of that kind through the ground. White particles are close, green further, blue far away. Good for zinc and osmium.",
          ],
          tasks=[task_item("ars_nouveau:ritual_scrying", 1)],
          rewards=[reward_table("s2_common")],
          deps=["brazier"], optional=True),

    quest("turret", 9, 0, "Basic Spell Turret",
          subtitle="A spell, cast by redstone.",
          description=[
              "Inscribe a spell into the turret with your book and give it a redstone pulse. It casts from its front, using Source from jars nearby. Break and harvest spells make simple farms.",
          ],
          tasks=[task_item("ars_nouveau:basic_spell_turret", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_table("s2_uncommon")],
          deps=["relay", "harvest"], icon="ars_nouveau:basic_spell_turret", size=1.5),

    quest("warp", 12, -2, "Warp Scroll",
          subtitle="Home, once.",
          description=[
              "Set a location on the scroll, use it later to go back there. It is used up. The &6Stabilized Warp Scroll&r can be used again and again.",
          ],
          tasks=[task_item("ars_nouveau:warp_scroll", 2)],
          rewards=[reward_item("ars_nouveau:warp_scroll", 2)],
          deps=["turret"], optional=True),

    quest("mage", 12, 2, "A Proper Mage",
          subtitle="Source for the whole server.",
          description=[
              "A Source farm big enough that you never think about it, relays that bring it where it is needed, and gems to spare for the engineers who need blaze burners.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 16)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["turret"], icon="ars_nouveau:source_gem_block", size=1.75),
]

chapter(C, "Ars Nouveau: Mage", "ars_nouveau:apprentice_spell_book", "magic", quests, shape="circle", order=12, stage=2,
        subtitle=["Stage 2. The second book, relays, rituals and turrets."])
