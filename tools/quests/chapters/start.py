"""Start here: what Kronwerke is, how stages work, and the handful of things everyone needs on day one."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "start_here"

quests = [
    quest("welcome", 0, 0, "Welcome to Kronwerke",
          subtitle="One world, many streamers, and a server that grows together.",
          description=[
              "Kronwerke Season 2 is a tech and magic pack where nothing important is unlocked by a single player. The whole server works on one goal at a time, and when it is reached, the next stage opens for everyone.",
              "",
              "This book walks you through all of it. Each chapter is one mod or one theme. Quests show you what to do next, and most of them pay out in crates.",
              "",
              "&6Tip:&r Crates open with a right click. Stone, Iron and Gold crates get better in that order.",
          ],
          tasks=[task_checkmark("Let's go")],
          rewards=[reward_item("minecraft:bread", 16), reward_table("s1_common")],
          icon="ftbquests:book", size=2.0, shape="hexagon"),

    quest("stages", 3, -2, "Stages",
          subtitle="Five stages, opened by the whole server, one after another.",
          description=[
              "The season has five stages: &6Steinwerk&r, &6Messingwerk&r, &6Stahlwerk&r, &6Sternwerk&r and &6Chaoswerk&r. Right now you are in Steinwerk: stone, water wheels and your first spells.",
              "",
              "Items that belong to a later stage are locked until the server opens that stage. Look them up in JEI and plan ahead.",
              "",
              "Type &e/kw goals&r to see what the server needs for the next stage.",
          ],
          tasks=[task_checkmark("Got it")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="minecraft:stone_bricks"),

    quest("obelisk", 6, -2, "The Community Goal",
          subtitle="Everyone pays in. When it is full, the next stage opens.",
          description=[
              "Each goal has a &btech&r half and a &dmagic&r half, and both have to fill. The first one also wants cobblestone from everyone. Hold the item and type &e/kw deposit&r, or &e/kw deposit all&r to put in everything that fits.",
              "",
              "At 98 percent the goal stops. The team sets a date, every streamer goes live, and the last items go in together on stream. That is when the next stage opens.",
              "",
              "&e/kw top&r shows who has put in the most so far.",
          ],
          tasks=[task_checkmark("I know how to deposit")],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(5)],
          deps=["stages"], icon="minecraft:lodestone"),

    quest("origin", 3, 2, "Your Origin",
          subtitle="Pick who you are. It changes how you play.",
          description=[
              "When you joined, you picked an origin. Each one has strengths and weaknesses, and some of them change which parts of the pack come easy to you.",
              "",
              "If you are not sure yet, play a few evenings with it. Streamers and team can help you if you really picked something that does not fit.",
          ],
          tasks=[task_checkmark("I picked my origin")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="minecraft:player_head"),

    quest("claim", 6, 2, "Claim Your Base",
          subtitle="Protect the place you build.",
          description=[
              "Open the FTB Chunks map (&eM&r by default) and drag over the chunks you want to claim. Nobody outside your team can break or open anything in them.",
              "",
              "Everyone gets a small number of claims, so claim your base, not the whole valley.",
          ],
          tasks=[task_checkmark("My base is claimed")],
          rewards=[reward_table("s1_common")],
          deps=["origin"], icon="minecraft:filled_map"),

    quest("sleep", 9, 2, "A Place to Sleep",
          subtitle="Sleep anywhere without resetting your spawn.",
          description=[
              "A &6Sleeping Bag&r lets you skip the night on a trip without moving your spawn point. A &6Hammock&r does the same for the day.",
              "Both are made from wool and string. Any colour works.",
          ],
          tasks=[task_checkmark("I have one")],
          rewards=[reward_item("minecraft:cooked_beef", 16)],
          deps=["claim"], icon="comforts:sleeping_bag_red", optional=True),

    quest("death", 9, -2, "When You Die",
          subtitle="Your things wait for you where you fell.",
          description=[
              "When you die, your body stays where you fell, with everything you carried. Walk back and open it to get your things back.",
              "",
              "The Mining Dimension, the deep caves and the new structures are dangerous. Write down coordinates before you go down.",
          ],
          tasks=[task_checkmark("Understood")],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["obelisk"], icon="minecraft:skeleton_skull"),

    quest("ultimine", 12, -2, "Ultimine",
          subtitle="Mine a whole vein at once.",
          description=[
              "Hold the Ultimine key (&e`&r, the key left of 1, by default) while you break a block, and every matching block around it goes with it: whole ore veins, whole trees, a row of stone.",
              "It costs hunger, so bring food.",
          ],
          tasks=[task_checkmark("Tried it")],
          rewards=[reward_item("minecraft:iron_pickaxe", 1)],
          deps=["death"], icon="minecraft:iron_pickaxe"),

    quest("voice", 12, 2, "Talk to People",
          subtitle="Proximity voice chat is on.",
          description=[
              "Players near you can hear you, players far away cannot. Press &eV&r for the voice chat settings, pick your microphone and set push to talk if you prefer.",
              "",
              "The Discord is still where the season is organised. Events, dates and the community goal are announced there first.",
          ],
          tasks=[task_checkmark("Set up")],
          rewards=[reward_xp(5)],
          deps=["sleep"], icon="minecraft:note_block", optional=True),

    quest("paths", 15, 0, "Pick a Path",
          subtitle="Tech, magic, or both. The server needs both.",
          description=[
              "You are ready. Three chapters are the backbone of this stage:",
              "",
              "&6Create&r for rotation, belts and the first machines. The tech half of the goal needs Andesite Alloy.",
              "&dArs Nouveau&r for spells and Source. The magic half of the goal needs Source Gems.",
              "&aBotania&r for flowers and mana. It is the start of a long road that pays off in later stages.",
              "",
              "Pick one to start. You will want all three before long.",
          ],
          tasks=[task_checkmark("On my way")],
          rewards=[reward_table("s1_uncommon")],
          deps=["ultimine"], icon="minecraft:compass", size=1.5, shape="gear"),
]

chapter(C, "Start Here", "ftbquests:book", "start", quests, shape="circle", order=0,
        subtitle=["What Kronwerke is and what everyone needs on day one."])
