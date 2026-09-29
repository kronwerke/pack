"""Storage: a backpack, drawers and better chests. Iron backpacks and compacting drawers open in stage 2."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp

C = "storage"

quests = [
    quest("welcome", 0, 0, "Storage",
          subtitle="Less time in chests, more time playing.",
          description=[
              "Three mods keep your things in order: &6Sophisticated Backpacks&r for what you carry, &6Functional Storage&r drawers for bulk items, and &6Sophisticated Storage&r for chests and barrels that grow with you.",
              "",
              "Start with a backpack: leather around a chest.",
          ],
          tasks=[task_item("sophisticatedbackpacks:backpack", 1)],
          rewards=[reward_item("minecraft:leather", 8), reward_table("s1_common")],
          icon="sophisticatedbackpacks:backpack", size=2.0, shape="hexagon"),

    quest("upgrade_base", 3, -2, "Upgrade Base",
          subtitle="Every backpack upgrade starts here.",
          description=["Backpacks take upgrades in the slots on the left of their screen. Each upgrade is crafted from an &6Upgrade Base&r."],
          tasks=[task_item("sophisticatedbackpacks:upgrade_base", 2)],
          rewards=[reward_item("minecraft:string", 16)],
          deps=["welcome"], icon="sophisticatedbackpacks:upgrade_base"),

    quest("pickup", 6, -3.5, "Pickup Upgrade",
          subtitle="Items go straight into the backpack.",
          description=["With a Pickup Upgrade, anything you pick up lands in the backpack first. Add a filter so only the things you want end up there."],
          tasks=[task_item("sophisticatedbackpacks:pickup_upgrade", 1)],
          rewards=[reward_xp(5)],
          deps=["upgrade_base"], icon="sophisticatedbackpacks:pickup_upgrade"),

    quest("magnet", 9, -3.5, "Magnet Upgrade",
          subtitle="Pulls nearby items to you.",
          description=["Everything that drops near you flies into the backpack. Perfect with Ultimine."],
          tasks=[task_item("sophisticatedbackpacks:magnet_upgrade", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["pickup"], optional=True),

    quest("crafting", 6, -0.5, "Crafting Upgrade",
          subtitle="A crafting grid you always carry.",
          description=["Adds a crafting grid to the backpack screen. You will never walk home for a table again."],
          tasks=[task_item("sophisticatedbackpacks:crafting_upgrade", 1)],
          rewards=[reward_item("minecraft:crafting_table", 1)],
          deps=["upgrade_base"], optional=True),

    quest("drawers", 3, 2, "Drawers",
          subtitle="Thousands of one item in one block.",
          description=[
              "A &6Drawer&r holds one kind of item per slot, far more than a chest. Right click to put in what you hold, double click to put in all of it, left click to take a stack.",
              "They come in 1, 2 and 4 slot versions and every wood type.",
          ],
          tasks=[task_item("functionalstorage:oak_1", 4)],
          rewards=[reward_item("minecraft:oak_log", 32)],
          deps=["welcome"], icon="functionalstorage:oak_1"),

    quest("four_drawers", 6, 2, "Four at Once",
          subtitle="Four items per block, smaller stacks each.",
          description=["The 4 slot drawer is the best for many different ores and ingots in a small space."],
          tasks=[task_item("functionalstorage:oak_4", 4)],
          rewards=[reward_item("minecraft:chest", 4)],
          deps=["drawers"], icon="functionalstorage:oak_4"),

    quest("barrel", 3, 5, "Sophisticated Barrel",
          subtitle="A barrel that you can upgrade instead of replace.",
          description=[
              "Sophisticated barrels and chests take tier upgrades: basic, copper, iron, gold, diamond, netherite. Each tier adds slots without breaking the block, so nothing inside has to move.",
              "They also take the same kind of upgrades as backpacks.",
          ],
          tasks=[task_item("sophisticatedstorage:barrel", 1)],
          rewards=[reward_item("minecraft:barrel", 4)],
          deps=["welcome"], icon="sophisticatedstorage:barrel"),

    quest("iron_tier", 6, 5, "Iron Tier",
          subtitle="More room, same barrel.",
          description=["Use a tier upgrade on the barrel in the world. Everything stays inside."],
          tasks=[task_item("sophisticatedstorage:basic_to_iron_tier_upgrade", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["barrel"], icon="sophisticatedstorage:basic_to_iron_tier_upgrade"),

    quest("trash", 9, 5, "Trash Can",
          subtitle="Deletes what you put into it.",
          description=["For the cobblestone you really do not need. Pipes and funnels can feed it too. Better: put cobblestone into the community goal first."],
          tasks=[task_item("trashcans:item_trash_can", 1)],
          rewards=[reward_xp(3)],
          deps=["iron_tier"], optional=True),

    quest("organised", 9, 2, "Organised",
          subtitle="A base where you find things.",
          description=[
              "A wall of drawers for bulk items, a few barrels for everything else, and a backpack for the trip.",
              "Stage 2 opens iron and copper backpacks, compacting drawers (nuggets to ingots to blocks, all in one) and drawer upgrades.",
          ],
          tasks=[task_item("functionalstorage:oak_4", 8), task_item("sophisticatedstorage:barrel", 4)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["four_drawers", "iron_tier"], icon="functionalstorage:oak_4", size=1.5, shape="gear"),
]

chapter(C, "Storage", "sophisticatedbackpacks:backpack", "storage", quests, shape="circle", order=5,
        subtitle=["Backpacks, drawers and chests that grow with you."])
