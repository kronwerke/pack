"""Create trains in stage 2: track, stations, a first train and a schedule."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "create_trains"

quests = [
    quest("welcome", 0, 0, "Trains",
          subtitle="The fastest way across a big map is a railway.",
          description=[
              "Create trains are real contraptions that drive on their own track, carry blocks, chests and tanks, and follow a timetable without anyone on board.",
              "",
              "Place track with right click on the start and right click on the end. It curves and climbs by itself.",
          ],
          tasks=[task_item("create:track", 32)],
          rewards=[reward_item("create:track", 32), reward_table("s2_common")],
          icon="create:track", size=2.0, shape="hexagon"),

    quest("casing", 3, -2, "Railway Casing",
          subtitle="Bogeys are made of this.",
          description=[
              "Apply a &6Sturdy Sheet&r to a brass casing. Right click the track with railway casing to place a bogey, the wheels a train stands on.",
          ],
          tasks=[task_item("create:railway_casing", 4)],
          rewards=[reward_item("create:brass_casing", 4)],
          deps=["welcome"]),

    quest("station", 3, 2, "Train Station",
          subtitle="Where trains are built and where they stop.",
          description=[
              "Place the &6Train Station&r next to the track. Everything a train needs is assembled in front of it, and its screen names the stop.",
          ],
          tasks=[task_item("create:track_station", 2)],
          rewards=[reward_item("minecraft:compass", 2)],
          deps=["welcome"]),

    quest("controls", 6, 0, "Train Controls",
          subtitle="The driver's seat.",
          description=[
              "Put bogeys on the track at the station, build your train on top of them, glue it together with &6Super Glue&r, and place the &6Train Controls&r facing the way it should drive. Then open the station and assemble.",
          ],
          tasks=[task_item("create:controls", 1)],
          rewards=[reward_item("create:super_glue", 1), reward_table("s2_common")],
          deps=["casing", "station"], icon="create:controls", size=1.5),

    quest("first_train", 9, 0, "Your First Train",
          subtitle="All aboard.",
          description=[
              "Assemble it, sit at the controls and drive it to another station. Disassemble it there if you like, it keeps its shape.",
          ],
          tasks=[task_checkmark("Assemble a train and drive it")],
          rewards=[reward_item("create:track", 64), reward_xp(10)],
          deps=["controls"], shape="diamond"),

    quest("schedule", 12, -2, "Train Schedule",
          subtitle="It drives while you are elsewhere.",
          description=[
              "Write stops and conditions into a &6Train Schedule&r: go to this station, wait until the cargo is full, go to that one. Hand it to a conductor sitting at the controls, a mob or even a blaze in a blaze burner.",
          ],
          tasks=[task_item("create:schedule", 1)],
          rewards=[reward_item("minecraft:lead", 2), reward_table("s2_uncommon")],
          deps=["first_train"]),

    quest("signals", 12, 2, "Signals",
          subtitle="More than one train, no crashes.",
          description=[
              "Signals split the track into sections. A train waits at a red signal until the section ahead is free. You need them as soon as two trains share a line.",
          ],
          tasks=[task_item("create:track_signal", 2)],
          rewards=[reward_item("create:electron_tube", 4)],
          deps=["first_train"]),

    quest("cargo", 15, -2, "Cargo",
          subtitle="Load and unload at every stop.",
          description=[
              "A &6Portable Storage Interface&r on the train and one at the station swap items whenever the train stops there. That is how a mine in one corner of the map feeds a factory in the other.",
          ],
          tasks=[task_item("create:portable_storage_interface", 2)],
          rewards=[reward_item("create:andesite_casing", 8)],
          deps=["schedule"], optional=True),

    quest("line", 15, 0, "A Line That Runs Itself",
          subtitle="Two stations, one schedule, no driver.",
          description=[
              "A train on a schedule between two bases, with signals where lines meet. The obelisk is at spawn: a line there makes feeding it easy.",
          ],
          tasks=[task_item("create:track", 256), task_item("create:track_station", 2)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["schedule", "signals"], icon="create:track_station", size=1.75, shape="gear"),
]

chapter(C, "Create: Trains", "create:controls", "tech", quests, shape="gear", order=15, stage=2,
        subtitle=["Stage 2. Track, stations and trains that drive themselves."])
