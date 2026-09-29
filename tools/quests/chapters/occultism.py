"""Occultism in stage 2: spirit fire, chalk, the first rituals, Foliot and Djinni."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "occultism"

quests = [
    quest("welcome", 0, 0, "Occultism",
          subtitle="Spirits, bound into service.",
          description=[
              "Occultism summons spirits from the Other Place and puts them to work. The &6Dictionary of Spirits&r is the manual and walks you through everything here.",
              "",
              "Start with &6Demon's Dream Seeds&r from grass. Throw a &6Demon's Dream Fruit&r on the ground and light it with flint and steel: that is &6Spiritfire&r. Throw impure white chalk into it and it comes out pure.",
          ],
          tasks=[task_item("occultism:chalk_white", 1)],
          rewards=[reward_item("occultism:datura_seeds", 8), reward_table("s2_common")],
          icon="occultism:dictionary_of_spirits", size=2.0, shape="hexagon"),

    quest("bowls", 3, -2, "Sacrificial Bowls",
          subtitle="The ingredients of a ritual go here.",
          description=[
              "A ritual needs at least four &6Sacrificial Bowls&r within eight blocks of its centre. Where exactly does not matter. Put the ingredients in them.",
          ],
          tasks=[task_item("occultism:sacrificial_bowl", 4)],
          rewards=[reward_item("occultism:otherstone", 16)],
          deps=["welcome"]),

    quest("golden_bowl", 3, 2, "Golden Ritual Bowl",
          subtitle="The centre of every pentacle.",
          description=[
              "Draw the pentacle around the &6Golden Ritual Bowl&r with chalk. Only the colour and position of the marks count, not the glyph shown.",
              "Right click the golden bowl with the activation item to start. A hopper or pipe into the bowl works too.",
          ],
          tasks=[task_item("occultism:golden_sacrificial_bowl", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["welcome"]),

    quest("foliot_book", 6, 0, "Book of Binding: Foliot",
          subtitle="A name, written down, is a leash.",
          description=[
              "Craft the book of binding, then craft it again with the Dictionary of Spirits to write the Foliot's name in. The Dictionary is not used up. The bound book starts the ritual.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_foliot", 1)],
          rewards=[reward_table("s2_common")],
          deps=["bowls", "golden_bowl"], icon="occultism:book_of_binding_bound_foliot", size=1.5),

    quest("crusher", 9, 0, "The Foliot Crusher",
          subtitle="Your first ritual: a spirit that grinds ore.",
          description=[
              "The Dictionary's first ritual summons a Foliot that crushes ore into dust, more dust than the ore would give as ingots. Draw Aviar's Circle in white chalk, fill the bowls, right click the golden bowl with the bound book.",
              "Drop ore near the crusher and collect the dust.",
          ],
          tasks=[task_checkmark("Summon a Foliot Crusher")],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s2_uncommon")],
          deps=["foliot_book"], icon="occultism:book_of_binding_foliot", size=1.5, shape="diamond"),

    quest("silver", 12, -2, "Silver",
          subtitle="The metal spirits respect.",
          description=[
              "Silver ore is in the overworld. The crusher turns it into dust like any other ore. Many Occultism recipes and bowls use it.",
          ],
          tasks=[task_item("occultism:silver_ingot", 16)],
          rewards=[reward_item("occultism:silver_ingot", 8)],
          deps=["crusher"]),

    quest("djinni_book", 12, 2, "Book of Binding: Djinni",
          subtitle="A stronger spirit, a stronger circle.",
          description=[
              "Djinni are the next rank. Their rituals need better chalk and a different pentacle, all in the Dictionary. The Djinni crusher is faster than the Foliot.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_djinni", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["crusher"], icon="occultism:book_of_binding_bound_djinni", size=1.5),

    quest("occultist", 15, 0, "An Occultist",
          subtitle="Spirits at work while you sleep.",
          description=[
              "A crusher that never stops, fed by a hopper or a belt. Afrit, Marid and the storage and mining spirits wait for stage 3.",
          ],
          tasks=[task_item("occultism:chalk_white", 16), task_item("occultism:sacrificial_bowl", 8)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["silver", "djinni_book"], icon="occultism:golden_sacrificial_bowl", size=1.75),
]

chapter(C, "Occultism", "occultism:dictionary_of_spirits", "magic", quests, shape="circle", order=13, stage=2,
        subtitle=["Stage 2. Spiritfire, chalk and the first spirits."])
