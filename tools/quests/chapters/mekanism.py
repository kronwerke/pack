"""Mekanism in stage 2: osmium, the metallurgic infuser, steel and the basic machines."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp

C = "mekanism"

quests = [
    quest("welcome", 0, 0, "Mekanism",
          subtitle="Machines that run on power and do it well.",
          description=[
              "Mekanism is the big tech mod of this pack. It starts with one ore, osmium, and one machine, the Metallurgic Infuser, and ends with fusion reactors in stage 4.",
              "",
              "In stage 2 the basic tier is open: the first machines, steel, cables and power. The ore tripling machines, the digital miner and the elite tier wait for stage 3.",
          ],
          tasks=[task_item("mekanism:raw_osmium", 8)],
          rewards=[reward_item("mekanism:raw_osmium", 16), reward_table("s2_common")],
          icon="mekanism:ingot_osmium", size=2.0, shape="hexagon"),

    quest("osmium", 3, 0, "Osmium Ingots",
          subtitle="Smelt it. You will need a lot.",
          description=[
              "Osmium ore is common in the overworld stone. Every Mekanism machine and circuit has osmium in it somewhere.",
          ],
          tasks=[task_item("mekanism:ingot_osmium", 32)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["welcome"]),

    quest("infuser", 6, 0, "Metallurgic Infuser",
          subtitle="The first machine, and it needs mana.",
          description=[
              "On this server the &6Metallurgic Infuser&r takes two &6Manasteel Ingots&r from a Botania mana pool. Find someone with a pool, or build one.",
              "",
              "The infuser pushes an infusion type into an item: coal gives carbon, redstone gives redstone. Put power in and it works on its own.",
          ],
          tasks=[task_item("mekanism:metallurgic_infuser", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_table("s2_common")],
          deps=["osmium"], icon="mekanism:metallurgic_infuser", size=1.5),

    quest("power", 6, 3.5, "Heat Generator",
          subtitle="Power from anything that burns.",
          description=[
              "The &6Heat Generator&r burns fuel and gets a little extra from lava next to it. Enough for the first two or three machines. Wind and solar come after.",
          ],
          tasks=[task_item("mekanismgenerators:heat_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8)],
          deps=["osmium"]),

    quest("cables", 9, 3.5, "Universal Cables",
          subtitle="Power from here to there.",
          description=[
              "Cables carry power between generators and machines. The &6Basic Energy Cube&r stores it for when the generator is off.",
          ],
          tasks=[task_item("mekanism:basic_universal_cable", 16), task_item("mekanism:basic_energy_cube", 1)],
          rewards=[reward_item("mekanism:basic_universal_cable", 16)],
          deps=["power"]),

    quest("circuit", 9, -2, "Basic Control Circuit",
          subtitle="Osmium infused with redstone.",
          description=[
              "Infuse osmium with redstone. Every machine past the infuser needs a circuit.",
          ],
          tasks=[task_item("mekanism:basic_control_circuit", 4)],
          rewards=[reward_item("mekanism:ingot_osmium", 16)],
          deps=["infuser"]),

    quest("steel", 9, 0, "Steel",
          subtitle="Iron, carbon, carbon again.",
          description=[
              "Infuse iron with carbon and you get &6Enriched Iron&r. Infuse that with carbon again for &6Steel Dust&r. Smelt it.",
              "Steel goes into the casing of every Mekanism machine, and stage 3 asks the obelisk for thousands of it. Start early.",
          ],
          tasks=[task_item("mekanism:ingot_steel", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 32), reward_table("s2_uncommon")],
          deps=["infuser"], icon="mekanism:ingot_steel", size=1.5),

    quest("casing", 12, 0, "Steel Casing",
          subtitle="The body of the machines.",
          description=[
              "Steel, glass and osmium. From here on each machine is a casing plus whatever makes it special.",
          ],
          tasks=[task_item("mekanism:steel_casing", 4)],
          rewards=[reward_item("minecraft:glass", 16)],
          deps=["steel", "circuit", "cables"]),

    quest("enrichment", 15, -2, "Enrichment Chamber",
          subtitle="More dust out of every ore.",
          description=[
              "An ore block mined with silk touch becomes two dusts. Raw ore gives a third more than smelting it would. Smelt the dusts.",
              "It also turns coal into enriched carbon for the infuser, which is much faster than raw coal.",
          ],
          tasks=[task_item("mekanism:enrichment_chamber", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s2_uncommon")],
          deps=["casing"], icon="mekanism:enrichment_chamber", size=1.5),

    quest("smelter", 15, 2, "Energized Smelter",
          subtitle="A furnace that runs on power.",
          description=[
              "Faster than a furnace and no fuel. Put it right after the enrichment chamber and your ores come out as ingots.",
          ],
          tasks=[task_item("mekanism:energized_smelter", 1)],
          rewards=[reward_item("mekanism:basic_control_circuit", 2)],
          deps=["casing"]),

    quest("crusher", 18, 2, "Crusher",
          subtitle="Ingots to dust, and more.",
          description=[
              "The &6Crusher&r grinds ingots back into dust and gravel into sand. Some recipes need dust instead of ingots.",
          ],
          tasks=[task_item("mekanism:crusher", 1)],
          rewards=[reward_item("mekanism:ingot_osmium", 16)],
          deps=["smelter"], optional=True),

    quest("line", 18, -2, "An Ore Line",
          subtitle="Chest, enrichment chamber, smelter, chest.",
          description=[
              "Connect them with the side configuration of each machine (the coloured tabs in the GUI) and a few &6Logistical Transporters&r. Drop ore into the first chest and collect the ingots at the end.",
          ],
          tasks=[task_item("mekanism:basic_logistical_transporter", 8), task_item("mekanism:ingot_steel", 64)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["enrichment"], icon="mekanism:basic_logistical_transporter", size=1.75, shape="gear"),
]

chapter(C, "Mekanism", "mekanism:metallurgic_infuser", "tech", quests, shape="square", order=10, stage=2,
        subtitle=["Stage 2. Osmium, steel and the basic machines."])
