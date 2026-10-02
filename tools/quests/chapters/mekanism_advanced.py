"""Mekanism in stage 3: the advanced control circuit (AE2 printed silicon), diamond infusion,
reinforced alloy, the osmium compressor, refined obsidian and glowstone, atomic alloy, the
teleporter, the robit, the digital miner and the atomic disassembler, the advanced tier
(installer, factory, transmitters, cube, tanks), the thermal evaporation plant (brine,
lithium), the thermoelectric boiler with resistive heaters (steam), the industrial turbine,
the advanced solar generator, the nutritional liquifier, and the stage 3 machines of
Mekanism MoreMachine. Ore tripling lives in mekanism_ores.py. Numbers come from the jars and
config/Mekanism (FE = J / 2.5). Recipes follow kubejs/server_scripts/kronwerke/tech.js and
milestones.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mekanism_advanced"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Der Schaltkreis ---------------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lBau einen Fortgeschrittenen Schaltkreis",
          subtitle="Ein Schaltkreis, der Silizium braucht.",
          description=[
              "&eRezept auf Kronwerke:&r oben Infundierte Legierung, Einfacher Steuerschaltkreis, Infundierte Legierung, darunter in der Mitte ein &6Gedrucktes Silizium&r aus dem AE2-Inscriber mit der Silizium-Presse. Andere Wege gibt es nicht.",
              "",
              img(item_texture("mekanism:advanced_control_circuit"), 32, 32),
              "",
              "Mit &6Stufe 3, dem Stahlwerk&r, öffnet Mekanism seine zweite Ebene: Teleporter, Digitaler Miner, Turbine, Wärmeverdampfung, die fortschrittliche Stufe. Die Erzverdreifachung steht im Kapitel &5Mekanism: Erz Schritt für Schritt&r.",
              "",
              "&cSpäter:&r Elite, Ultimativ, QIO, Induktionsmatrix und Fusion in Stufe 4, Antimaterie in Stufe 5.",
          ],
          tasks=[task_item("mekanism:advanced_control_circuit", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_table("s3_common"), reward_xp(10)],
          icon="mekanism:advanced_control_circuit", size=2.0, shape="hexagon"),

    quest("circuits", 2.75, 0.5, "&aLeg 16 Schaltkreise auf Vorrat",
          subtitle="Jede neue Maschine will zwei.",
          description=[
              "Mach &e16 Fortgeschrittene Steuerschaltkreise&r. Der Engpass ist das Gedruckte Silizium: tausch mit einem AE2-Spieler oder bau die CNC Stamper weiter unten.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 3 &e250 Fortgeschrittene Schaltkreise&r, jeder zählt acht Punkte. Ein Vorrat lohnt sich doppelt.",
          ],
          tasks=[task_item("mekanism:advanced_control_circuit", 16)],
          rewards=[reward_item("mekanism:basic_control_circuit", 8), reward_item("mekanism:alloy_infused", 16)],
          deps=["welcome"]),

    # ---- Diamant und Obsidian ----------------------------------------------------------
    quest("diamond", 5.5, 1.5, "&bReichere Diamanten an",
          subtitle="Ein Diamant, 80 mB.",
          description=[
              "Ein &6Diamant&r durch die Anreicherungskammer wird zum &6Angereicherten Diamanten&r, der in der Infusionsanlage &e80 mB&r Diamant gibt. Diamantstaub gibt nur 10 mB.",
              "",
              "Ein Diamant reicht damit für vier Verstärkte Legierungen oder acht Raffinierten Obsidianstaub.",
          ],
          tasks=[task_item("mekanism:enriched_diamond", 4)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["welcome"], icon="mekanism:enriched_diamond"),

    quest("reinforced", 8, 0.5, "&bMach Verstärkte Legierung",
          subtitle="Infundierte Legierung, getränkt in Diamant.",
          description=[
              "Eine &6Infundierte Legierung&r mit &e20 mB Diamant&r gibt eine &6Verstärkte Legierung&r.",
              "",
              "Der Meilenstein der Magier, der &6Elfenstern&r, braucht eine. Die Magier können sie nicht selbst machen, bring ihnen welche. In Stufe 4 steckt sie im Elite-Schaltkreis.",
          ],
          tasks=[task_item("mekanism:alloy_reinforced", 8)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_table("s3_common")],
          deps=["diamond"]),

    quest("compressor", 8, 2.5, "&7Bau einen Osmium-Kompressor",
          subtitle="Presst Staub mit Osmium zu Barren.",
          description=[
              "Legierung in die Ecken, Fortgeschrittene Schaltkreise oben und unten, Eimer links und rechts, Stahlgehäuse in die Mitte.",
              "",
              "Leg &6Osmiumbarren&r in den Chemikalien-Slot, jeder gibt &e200 mB&r Osmium. Die Maschine verbraucht es, solange sie presst.",
          ],
          tasks=[task_item("mekanism:osmium_compressor", 1)],
          rewards=[reward_item("mekanism:ingot_osmium", 16), reward_xp(5)],
          deps=["diamond"], icon="mekanism:osmium_compressor"),

    quest("refined_obsidian", 10.5, 3, "&5Mach Raffiniertes Obsidian",
          subtitle="Obsidian, Diamant, Osmium.",
          description=[
              "Zerkleinerer: ein Obsidian gibt &evier Obsidianstaub&r. Infusionsanlage: Staub mit &e10 mB Diamant&r gibt &6Raffinierten Obsidianstaub&r. Kompressor: Staub mit Osmium gibt den &6Barren&r.",
              "",
              "Raffiniertes Obsidian ist das stärkste Material von Mekanism Tools und steckt im Teleporter-Rahmen und im Robit.",
          ],
          tasks=[task_item("mekanism:dust_refined_obsidian", 8), task_item("mekanism:ingot_refined_obsidian", 8)],
          rewards=[reward_item("minecraft:obsidian", 16), reward_table("s3_common"), reward_xp(5)],
          deps=["compressor"], icon="mekanism:ingot_refined_obsidian"),

    quest("refined_glowstone", 10.5, 1.5, "&eMach Raffiniertes Glowstone",
          subtitle="Glowstonestaub im Kompressor.",
          description=[
              "&6Glowstonestaub&r in den Osmium-Kompressor: ein &6Raffinierter Glowstonebarren&r.",
              "",
              "Ein Barren davon sitzt in der Mitte jedes Rezepts für Teleporter-Rahmen. Glowstone kommt aus dem Nether.",
          ],
          tasks=[task_item("mekanism:ingot_refined_glowstone", 4)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_xp(3)],
          deps=["compressor"], icon="mekanism:ingot_refined_glowstone"),

    quest("atomic", 13, 1.5, "&5&lMach Atomlegierung",
          subtitle="Verstärkte Legierung, getränkt in Obsidian.",
          description=[
              "Eine &6Verstärkte Legierung&r mit &e40 mB Raffiniertem Obsidian&r gibt eine &6Atomlegierung&r.",
              "",
              "Der Staub gibt nur 10 mB. Schick ihn erst durch die Anreicherungskammer, &6Angereichertes Obsidian&r gibt 80 mB, genug für zwei Legierungen.",
              "",
              "Atomlegierung steckt im Teleportationskern, im Robit und in allem, was in Stufe 4 ultimativ heißt.",
          ],
          tasks=[task_item("mekanism:alloy_atomic", 4)],
          rewards=[reward_item("mekanism:alloy_reinforced", 4), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["reinforced", "refined_obsidian"], icon="mekanism:alloy_atomic", size=1.5, shape="hexagon"),

    # ---- Teleporter und Miner ----------------------------------------------------------
    quest("teleport_core", 0, 7, "&dBau einen Teleportationskern",
          subtitle="Das Herz von Teleporter und Miner.",
          description=[
              "&eRezept auf Kronwerke:&r &6Manaperlen&r von Botania in die Ecken, &6Atomlegierung&r oben und unten, Gold links und rechts, ein Diamant in die Mitte.",
              "",
              "Teleporter, Tragbarer Teleportierer und Digitaler Miner brauchen einen, der Miner sogar zwei. In Stufe 4 kommen Quantenverschränkungsporter und QIO dazu.",
          ],
          tasks=[task_item("mekanism:teleportation_core", 2)],
          rewards=[reward_item("botania:mana_pearl", 8), reward_xp(5)],
          deps=["atomic"], icon="mekanism:teleportation_core"),

    quest("teleporter", 2.5, 6.25, "&d&lStell zwei Teleporter auf",
          subtitle="Von Basis zu Basis in einem Schritt.",
          description=[
              "&6Teleporter:&r der Kern in der Mitte, Stahlgehäuse an den Seiten, Schaltkreise in die Ecken. &6Rahmen:&r acht Raffinierte Obsidianbarren um einen Raffinierten Glowstonebarren geben neun.",
              "",
              "Bau einen Rahmen &e4 breit und 5 hoch&r mit einer Öffnung von 2 mal 3, der Teleporter ist einer der Rahmenblöcke. Gib beiden dieselbe &eFrequenz&r und Strom.",
              "",
              "Jeder Sprung kostet Strom, je weiter, desto mehr, in eine andere Dimension deutlich mehr.",
          ],
          tasks=[task_item("mekanism:teleporter", 1), task_item("mekanism:teleporter_frame", 13)],
          rewards=[reward_item("mekanism:ingot_refined_obsidian", 8), reward_item("minecraft:ender_pearl", 4), reward_xp(10)],
          deps=["teleport_core", "refined_glowstone"], icon="mekanism:teleporter", size=1.5, shape="hexagon"),

    quest("portable_teleporter", 5, 6.25, "&dSteck einen Teleporter ein",
          subtitle="Der Tragbare Teleportierer.",
          description=[
              "Ein Teleportationskern, zwei Energietabletts, zwei Schaltkreise. Er springt zu jedem Teleporter auf deinen Frequenzen.",
              "",
              "Lade ihn vorher auf. Ein Sprung nach Hause aus der Mine spart den Rückweg.",
          ],
          tasks=[task_item("mekanism:portable_teleporter", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2), reward_xp(5)],
          deps=["teleporter"], icon="mekanism:portable_teleporter", optional=True),

    quest("robit", 2.5, 8, "&eBau einen Robit",
          subtitle="Ein Helfer auf Rädern.",
          description=[
              "Oben Stahl, Mitte Energietablett, &6Atomlegierung&r, Energietablett, unten Raffiniertes Obsidian, Persönliche Truhe, Raffiniertes Obsidian.",
              "",
              "Der Robit folgt dir, sammelt Gegenstände auf und lädt sich an einem Ladepad. Vor allem ist er das Herz des Digitalen Miners.",
          ],
          tasks=[task_item("mekanism:robit", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2), reward_xp(5)],
          deps=["teleport_core"], icon="mekanism:robit"),

    quest("miner", 5, 8, "&6&lStell einen Digitalen Miner auf",
          subtitle="Er baut ab, was du ihm sagst.",
          description=[
              "Oben Atomlegierung, Schaltkreis, Atomlegierung. Mitte &6Logistischer Sortierer&r, &6Robit&r, Sortierer. Unten Teleportationskern, Stahlgehäuse, Teleportationskern.",
              "",
              "Radius bis &e32 Blöcke&r, Y-Bereich und Filter (zum Beispiel ein Erz-Tag) einstellen, Start. &e80 Ticks&r pro Block ohne Upgrades, &d400 FE/t&r. Behutsamkeit kostet zwölfmal so viel Strom.",
              "",
              "Kiste oder Transporter an die Rückseite, Auto-Auswurf an, ein Ankerupgrade hinein, dann läuft er auch, wenn du weg bist.",
          ],
          tasks=[task_item("mekanism:digital_miner", 1)],
          rewards=[reward_item("mekanism:upgrade_speed", 2), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["robit"], icon="mekanism:digital_miner", size=1.75, shape="gear"),

    quest("disassembler", 7.5, 8, "&cBau einen Atomic Disassembler",
          subtitle="Ein elektrisches Werkzeug für alles.",
          description=[
              "Oben Legierung, Energietablett, Legierung. Mitte Legierung, &6Atomlegierung&r, Legierung. Unten ein Raffinierter Obsidianbarren.",
              "",
              "Er baut, gräbt und schlägt mit Strom statt Haltbarkeit, mit Modi für mehr Tempo. In Stufe 4 wird er in der Mitte des &6Meka-Werkzeugs&r verbaut.",
          ],
          tasks=[task_item("mekanism:atomic_disassembler", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_xp(5)],
          deps=["atomic"], icon="mekanism:atomic_disassembler", optional=True),

    # ---- Fortschrittliche Stufe --------------------------------------------------------
    quest("installer", 10.5, 7, "&a&lStuf eine Fabrik auf Fortschrittlich",
          subtitle="Aus drei Plätzen werden fünf.",
          description=[
              "&6Fortgeschrittener Stufen Installateur:&r Legierung in die Ecken, Fortgeschrittene Schaltkreise oben und unten, Osmium links und rechts, ein Brett. Rechtsklick auf eine Einfache Fabrik.",
              "",
              "Eine Fortschrittliche Fabrik arbeitet an &efünf&r Gegenständen gleichzeitig. Elite (7) und Ultimativ (9) kommen in Stufe 4.",
          ],
          tasks=[task_item("mekanism:advanced_tier_installer", 1)],
          rewards=[reward_item("mekanism:advanced_control_circuit", 2), reward_table("s3_common")],
          deps=["circuits"], icon="mekanism:advanced_tier_installer", size=1.5, shape="hexagon"),

    quest("adv_factory", 13, 6.25, "&dBau eine Fortschrittliche Reinigungsfabrik",
          subtitle="Fünf Erze auf einmal in die Klärkammer.",
          description=[
              "Klärkammer mit dem Einfachen, dann dem Fortgeschrittenen Installateur, oder an der Werkbank: die Einfache Reinigungsfabrik in die Mitte, Osmium, Schaltkreise, Legierung.",
              "",
              "Zerkleinerer und Anreicherungskammer dahinter brauchen dasselbe Tempo, sonst staut es. Die Straße dazu: Kapitel &5Mekanism: Erz Schritt für Schritt&r.",
          ],
          tasks=[task_item("mekanism:advanced_purifying_factory", 1)],
          rewards=[reward_item("minecraft:raw_gold", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["installer"], icon="mekanism:advanced_purifying_factory"),

    quest("adv_transmit", 13, 8, "&eStuf deine Leitungen hoch",
          subtitle="Mehr Durchsatz für die größere Straße.",
          description=[
              "Acht einfache Kabel, Transporter, Rohre oder Schläuche um eine &6Infundierte Legierung&r geben acht fortschrittliche. Oder Rechtsklick mit der Legierung auf eine liegende Leitung.",
              "",
              "&eWerte:&r Kabel &d51 200 FE/t&r, Transporter 16 Stück pro Zug und doppelt so schnell, Druckschlauch 2 000 mB pro Zug, Rohr 1 000 mB.",
          ],
          tasks=[task_item("mekanism:advanced_universal_cable", 16), task_item("mekanism:advanced_logistical_transporter", 16)],
          rewards=[reward_item("mekanism:alloy_infused", 8)],
          deps=["installer"], icon="mekanism:advanced_universal_cable"),

    quest("adv_cube", 15.5, 8, "&aBau einen Fortschrittlichen Energie-Würfel",
          subtitle="6,4 Millionen FE.",
          description=[
              "Der Einfache Würfel in die Mitte, Osmium links und rechts, Energietabletts oben und unten, Legierung in die Ecken. &d6,4 Millionen FE&r, &d6 400 FE/t&r Abgabe.",
              "",
              "Die Induktionsmatrix für Milliarden FE braucht Elite-Schaltkreise und Lithium und kommt in Stufe 4.",
          ],
          tasks=[task_item("mekanism:advanced_energy_cube", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2)],
          deps=["adv_transmit"], optional=True),

    quest("adv_tanks", 15.5, 6.25, "&bStuf Tanks und Tonnen hoch",
          subtitle="Doppelt, vierfach, doppelt so viel.",
          description=[
              "Jeder einfache Speicher mit Legierung und Osmium drumherum wird fortschrittlich. &6Flüssigkeitstank&r 64 000 mB, &6Chemikalienbehälter&r 256 000 mB, &6Tonne&r 8 192 Stück.",
              "",
              "Der Inhalt bleibt beim Hochstufen an der Werkbank erhalten.",
          ],
          tasks=[task_item("mekanism:advanced_chemical_tank", 1), task_item("mekanism:advanced_fluid_tank", 1)],
          rewards=[reward_item("mekanism:ingot_osmium", 16), reward_xp(5)],
          deps=["adv_factory"], icon="mekanism:advanced_chemical_tank", optional=True),

    # ---- Wärme und Dampf ---------------------------------------------------------------
    quest("evap_blocks", 0, 12, "&6Bau Wärmeverdampfungsblöcke",
          subtitle="Kupfer in Stahl.",
          description=[
              "Vier Stahl um einen Kupferbarren geben vier &6Wärmeverdampfungsblöcke&r. Für einen kleinen Turm brauchst du rund drei Dutzend.",
              "",
              "Vier Blöcke um einen Fortgeschrittenen Schaltkreis geben ein &6Ventil&r.",
          ],
          tasks=[task_item("mekanism:thermal_evaporation_block", 32), task_item("mekanism:thermal_evaporation_valve", 2)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(5)],
          deps=["welcome"], icon="mekanism:thermal_evaporation_block"),

    quest("evap", 2.5, 12, "&6&lBau die Wärmeverdampfungsanlage",
          subtitle="Wasser wird Sole, Sole wird Lithium.",
          description=[
              "&6Controller:&r oben Schaltkreis, Glasscheibe, Schaltkreis, Mitte Block, Eimer, Block, unten drei Blöcke. Bau einen Turm mit &e4 mal 4&r Grundfläche, hohl, &e3 bis 18&r hoch, Controller und Ventile in die Wand.",
              "",
              "Wasser durchs Ventil hinein: &e10 mB Wasser&r werden &e1 mB Sole&r, und Sole ein zweites Mal hinein gibt Lithium, ebenfalls 10 zu 1. Je höher der Turm und je wärmer es ist, desto schneller.",
          ],
          tasks=[task_item("mekanism:thermal_evaporation_controller", 1), task_item("mekanism:brine_bucket", 1)],
          rewards=[reward_item("mekanism:block_salt", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["evap_blocks"], icon="mekanism:thermal_evaporation_controller", size=1.5, shape="hexagon"),

    quest("gas_lithium", 5, 12, "&fLithium",
          subtitle="Sole, noch einmal verdampft.",
          description=[
              "&eMacht es:&r die Wärmeverdampfungsanlage aus Sole, 10 zu 1, als Flüssigkeit. Der Rotationskondensator macht Gas daraus.",
              "",
              "&eBraucht es:&r in Stufe 4 der Solarneutronenaktivator für Tritium, und der Kristallisator macht Lithiumstaub für die Induktionszellen.",
          ],
          tasks=[task_checkmark("Abgehakt")],
          rewards=[reward_xp(3)],
          deps=["evap"], icon="mekanism:lithium_bucket", optional=True),

    quest("heater", 0, 14, "&cBau einen Widerstandsheizer",
          subtitle="Strom wird Wärme.",
          description=[
              "Zinn, Redstone, ein Stahlgehäuse und ein Energietablett. Er macht aus Strom Wärme, laut Server-Config mit &e60 Prozent&r Wirkungsgrad.",
              "",
              "&6Wärmeleiter&r (Thermodynamic Conductor) tragen die Wärme zum Kessel. Der Brennholz-Heizer tut dasselbe mit Brennstoff.",
          ],
          tasks=[task_item("mekanism:resistive_heater", 1), task_item("mekanism:basic_thermodynamic_conductor", 8)],
          rewards=[reward_item("mekanism:dust_tin", 8), reward_xp(5)],
          deps=["welcome"], icon="mekanism:resistive_heater"),

    quest("boiler", 2.5, 14, "&6&lBau einen Thermoelektrischen Dampfkessel",
          subtitle="Wasser rein, Dampf raus.",
          description=[
              "&6Kesselgehäuse:&r vier Stahl um Eisen, gibt vier. &6Kesselventil:&r vier Gehäuse um einen Fortgeschrittenen Schaltkreis, gibt zwei. Innen &6Überhitzungselemente&r unten, eine Ebene &6Druckventile&r darüber trennt Wasser und Dampf.",
              "",
              "Wasser durch ein Ventil hinein, Wärme dazu, &bDampf&r aus einem anderen Ventil heraus, das du mit dem Konfigurator auf Ausgabe stellst. Der Dampf treibt die Industrieturbine.",
          ],
          tasks=[task_item("mekanism:boiler_casing", 24), task_item("mekanism:boiler_valve", 2), task_item("mekanism:superheating_element", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["heater"], icon="mekanism:boiler_valve", size=1.5, shape="hexagon"),

    quest("gas_steam", 5, 14, "&fDampf",
          subtitle="Der Brennstoff der Turbine.",
          description=[
              "&eMacht ihn:&r der Thermoelektrische Dampfkessel aus Wasser und Wärme. Dampf aus anderen Mods macht der Rotationskondensator zu Mekanism-Dampf. In Stufe 5 der Spaltreaktor.",
              "",
              "&eBraucht ihn:&r die Industrieturbine. Der Abdampf wird im Sammlerkondensator wieder Wasser.",
          ],
          tasks=[task_checkmark("Abgehakt")],
          rewards=[reward_xp(3)],
          deps=["boiler"], icon="mekanism:steam_bucket", optional=True),

    # ---- Industrieturbine --------------------------------------------------------------
    quest("turbine_rotor", 8.5, 12, "&7Bau Rotoren und Blätter",
          subtitle="Das Innere der Turbine.",
          description=[
              "&6Rotor:&r drei Reihen Stahl, Legierung, Stahl. &6Rotorblatt:&r vier Stahl um Legierung. &6Rotationskomplex:&r Stahl, Legierung und zwei Fortgeschrittene Schaltkreise.",
              "",
              "Die Rotoren stehen als Säule in der Mitte, jeder trägt bis zu zwei Blätter (Rechtsklick), der Komplex sitzt oben drauf.",
          ],
          tasks=[task_item("mekanismgenerators:turbine_rotor", 2), task_item("mekanismgenerators:turbine_blade", 4),
                 task_item("mekanismgenerators:rotational_complex", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 32)],
          deps=["welcome"], icon="mekanismgenerators:turbine_blade"),

    quest("turbine_shell", 11, 12, "&7Bau die Turbinenhülle",
          subtitle="Ein quadratischer Turm.",
          description=[
              "&6Turbinengehäuse:&r vier Stahl um Osmium, gibt vier. Die Hülle ist quadratisch mit &eungerader Kantenlänge&r, fang mit 5 mal 5 an. Strukturglas darf in die Wände.",
              "",
              "Jeder Block Volumen gibt laut Config &d6,4 Millionen FE&r Puffer dazu.",
          ],
          tasks=[task_item("mekanismgenerators:turbine_casing", 48), task_item("mekanism:structural_glass", 8)],
          rewards=[reward_item("mekanism:ingot_osmium", 16), reward_xp(5)],
          deps=["turbine_rotor"], icon="mekanismgenerators:turbine_casing"),

    quest("turbine_coils", 13.5, 12, "&7Bau Druckventile und Spulen",
          subtitle="Die Ebene um den Komplex.",
          description=[
              "&6Druckventil:&r Stahl in die Ecken, Eisengitter an die Seiten, Legierung in die Mitte. Sie füllen die ganze Ebene um den Rotationskomplex, jedes lässt &e1 280 mB&r Dampf pro Tick durch.",
              "",
              "&6Elektromagnetische Spule:&r Stahl, Gold und ein Energietablett. Spulen sitzen über dem Komplex, berühren ihn und einander, &eeine Spule für je vier Blätter&r.",
          ],
          tasks=[task_item("mekanism:pressure_disperser", 8), task_item("mekanismgenerators:electromagnetic_coil", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["turbine_shell"], icon="mekanismgenerators:electromagnetic_coil"),

    quest("turbine", 16, 12, "&6&lSetz die Industrieturbine zusammen",
          subtitle="Dampf rein, Strom raus.",
          description=[
              "&6Turbinenventile&r (Gehäuse und Fortgeschrittener Schaltkreis) in die Hülle für Dampf rein und Strom raus. &6Turbinenabzüge&r (Gehäuse und Eisengitter) auf Höhe des Komplexes oder darüber. &6Sammlerkondensatoren&r über den Druckventilen machen Abdampf zu Wasser.",
              "",
              "Dampf kommt aus dem Kessel. Die Leistung hängt von Blättern, Spulen und Dampfmenge ab, die Turbine wächst mit deinem Kraftwerk bis zur Fusion und zum Spaltreaktor.",
          ],
          tasks=[task_item("mekanismgenerators:turbine_valve", 2), task_item("mekanismgenerators:turbine_vent", 4),
                 task_item("mekanismgenerators:saturating_condenser", 2)],
          rewards=[reward_item("mekanismgenerators:turbine_casing", 16), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["turbine_coils", "boiler"], icon="mekanismgenerators:turbine_valve", size=2.0, shape="gear"),

    # ---- Mehr Maschinen ----------------------------------------------------------------
    quest("adv_solar", 0, 17.5, "&eBau einen Erweiterten Solargenerator",
          subtitle="Vier kleine werden ein großer.",
          description=[
              "Vier &6Solargeneratoren&r, zwei Legierungen, drei Eisen. Er liefert &d120 FE/t&r bei Tag, sechsmal so viel wie ein einzelner.",
              "",
              "Er braucht Platz um sich und freien Himmel. Ein Würfel dazwischen fängt die Nacht ab.",
          ],
          tasks=[task_item("mekanismgenerators:advanced_solar_generator", 1)],
          rewards=[reward_item("mekanismgenerators:solar_generator", 2), reward_xp(5)],
          deps=["welcome"], optional=True),

    quest("liquifier", 2.5, 17.5, "&aBau einen Nährstoffverflüssiger",
          subtitle="Essen aus dem Schlauch.",
          description=[
              "Redstone, Schaltkreise, Schüsseln und ein Stahlgehäuse. Er macht aus jedem Essen &6Nährstoffpaste&r, &e50 mB&r pro Hungerpunkt.",
              "",
              "Die &6Feldflasche&r (Zinn um eine Schüssel) füllst du damit und trinkst unterwegs. Später gibt es ein MekaSuit-Modul dafür.",
          ],
          tasks=[task_item("mekanism:nutritional_liquifier", 1), task_item("mekanism:canteen", 1)],
          rewards=[reward_item("minecraft:bread", 16), reward_xp(3)],
          deps=["welcome"], icon="mekanism:nutritional_liquifier", optional=True),

    quest("flamethrower", 5, 17.5, "&cBau einen Flammenwerfer",
          subtitle="Wasserstoff als Waffe.",
          description=[
              "Zinn, ein Chemikalienbehälter, ein Feuerzeug, Bronze und ein Fortgeschrittener Schaltkreis. Er verschießt brennenden &bWasserstoff&r.",
              "",
              "Füll ihn wie das Jetpack in einem Chemikalienbehälter. Einer seiner Modi schmilzt, was er trifft.",
          ],
          tasks=[task_item("mekanism:flamethrower", 1)],
          rewards=[reward_item("mekanism:ingot_bronze", 8), reward_xp(3)],
          deps=["welcome"], optional=True),

    # ---- MoreMachine -------------------------------------------------------------------
    quest("cnc_stamper", 8.5, 17.5, "&3&lBau eine CNC Stamper",
          subtitle="Silizium drucken ohne Inscriber.",
          description=[
              "&6Mekanism MoreMachine:&r Stahlgehäuse in die Mitte, Kolben links und rechts, Schaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Sie presst mit einer Form im Formslot. Mit der &6Silizium-Presse&r aus AE2 macht sie aus Silizium &6Gedrucktes Silizium&r, mit den anderen Pressen die Prozessorteile, mit Formen von Immersive Engineering Bleche, Stangen und Drähte.",
          ],
          tasks=[task_item("mekmm:cnc_stamper", 1), task_item("ae2:printed_silicon", 16)],
          rewards=[reward_item("ae2:silicon", 16), reward_table("s3_common"), reward_xp(5)],
          deps=["circuits"], icon="mekmm:cnc_stamper", size=1.5, shape="hexagon"),

    quest("stamping_factory", 11, 16.75, "&3Mach eine Stanzfabrik",
          subtitle="Drei Pressen in einem Block.",
          description=[
              "Die CNC Stamper in die Mitte des Installateur-Musters (Redstone, Schaltkreise, Eisen) gibt die &6Einfache Stanzfabrik&r. Mit Fortgeschrittenen Schaltkreisen wird sie fortschrittlich.",
              "",
              "Jede MoreMachine-Maschine hat eigene Fabriken. Elite und Ultimativ kommen in Stufe 4.",
          ],
          tasks=[task_item("mekmm:basic_stamping_factory", 1)],
          rewards=[reward_item("mekanism:basic_control_circuit", 4), reward_xp(5)],
          deps=["cnc_stamper"], icon="mekmm:basic_stamping_factory", optional=True),

    quest("rolling_mill", 11, 18.25, "&3Walz Drähte",
          subtitle="Die CNC Rolling Mill.",
          description=[
              "Stahlgehäuse in die Mitte, Stahl links und rechts, Schaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Sie walzt Barren zu Drähten von Immersive Engineering: Kupfer, Stahl, Blei, Aluminium, &ezwei&r pro Barren.",
          ],
          tasks=[task_item("mekmm:cnc_rolling_mill", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(3)],
          deps=["cnc_stamper"], icon="mekmm:cnc_rolling_mill", optional=True),

    quest("lathe", 13.5, 18.25, "&3Dreh Stangen",
          subtitle="Die CNC Lathe.",
          description=[
              "Stahlgehäuse in die Mitte, zwei &6Robits&r links und rechts, Schaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Sie dreht Stangen: Stahl und Aluminium für Immersive Engineering, Kupfer, Gold, Messing und Elektrum für Create Crafts & Additions, &ezwei&r pro Barren.",
          ],
          tasks=[task_item("mekmm:cnc_lathe", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 8), reward_xp(3)],
          deps=["rolling_mill", "robit"], icon="mekmm:cnc_lathe", optional=True),

    quest("recycler", 13.5, 16.75, "&3Bau einen Recycler",
          subtitle="Stein wird Schrott.",
          description=[
              "Ein Zerkleinerer in die Mitte, Osmium links und rechts, Fortgeschrittene Schaltkreise oben und unten, Legierung in die Ecken.",
              "",
              "Stein und Erde werden zu &e17 Prozent&r &6Schrott&r, Substrat zu 43 Prozent. Schrott ist der Rohstoff für die Replikatoren, die erst in Stufe 5 öffnen. Bis dahin ist er ein Mülleimer mit Bonus.",
          ],
          tasks=[task_item("mekmm:recycler", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["stamping_factory"], icon="mekmm:recycler", optional=True),

    quest("mid_tank", 16, 17.5, "&3Bau einen Mittleren Chemikalientank",
          subtitle="Mehr Gas auf einem Block.",
          description=[
              "Fünf Dynamische Tanks um zwei Einfache Chemikalienbehälter geben den &6Basic Mid Chemical Tank&r. Mit fünf weiteren Dynamischen Tanks um ihn wird er zum &6Max&r-Tank.",
              "",
              "Beide stufst du mit Legierungen hoch wie normale Behälter. Die großen MoreMachine-Maschinen in Stufe 4 brauchen ultimative Max-Tanks.",
          ],
          tasks=[task_item("mekmm:basic_mid_chemical_tank", 1)],
          rewards=[reward_item("mekanism:dynamic_tank", 8), reward_xp(3)],
          deps=["recycler"], icon="mekmm:basic_mid_chemical_tank", optional=True),

    # ---- Das Ziel ----------------------------------------------------------------------
    quest("steel_core", 0, 22, "&6Bau einen Stahlkern",
          subtitle="Der Meilenstein des Stahlwerks.",
          description=[
              "&eRezept:&r oben Schwerer Technikblock, &6Fortgeschrittener Schaltkreis&r, Schwerer Technikblock. Mitte Technikprozessor, &6Stahlgehäuse&r, Technikprozessor. Unten Schwerer Technikblock, &aElementiumbarren&r, Schwerer Technikblock.",
              "",
              img("kronwerke:textures/item/steel_core.png", 32, 32),
              "",
              "Technikblöcke aus Immersive Engineering (mit Präzisionsgetriebe), Prozessoren aus AE2 oder der CNC Stamper, Elementium von einem Botaniker. Der Obelisk will &e8 Stahlkerne&r.",
          ],
          tasks=[task_item("kronwerke:steel_core", 1)],
          rewards=[reward_table("s3_uncommon"), reward_xp(10)],
          deps=["circuits"], icon="kronwerke:steel_core", size=1.75, shape="gear"),

    quest("goal", 3, 22, "&5&lFütter den Obelisken",
          subtitle="Der Ofen schläft nie.",
          description=[
              "Stell eine Kiste an den Obelisken und leite Stahl und Schaltkreise hinein. Er holt sich alle zwei Sekunden, was er brauchen kann. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eTechnik-Pfeiler von Stufe 3:&r &64 000 Stahlbarren&r, &6250 Fortgeschrittene Schaltkreise&r, &68 Stahlkerne&r. Der Magie-Pfeiler will Elementium, Afrit-Essenz und Elfensterne, und beide müssen voll werden.",
              "",
              "Die Magier brauchen deine Verstärkte Legierung für die Elfensterne, du ihr Elementium für die Stahlkerne.",
          ],
          tasks=[task_item("mekanism:ingot_steel", 256), task_item("mekanism:advanced_control_circuit", 32)],
          rewards=[reward_table("s3_rare"), reward_item("mekanism:advanced_control_circuit", 4), reward_xp(20)],
          deps=["steel_core"], icon="mekanism:ingot_steel", size=2.5, shape="gear"),
]

images = [
    head("title", "Mekanism: Fortgeschritten", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 3: Stahlwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("obsidian", "Diamant und Obsidian", 5, -0.6, colour="water"),
    head("teleport", "Teleporter und Miner", 0, 4.6, colour="magic"),
    head("advanced", "Fortschrittliche Stufe", 9.8, 4.6, colour="brass"),
    head("heat", "Wärme und Dampf", 0, 10.2, colour="fire"),
    head("turbine", "Industrieturbine", 8, 10.2, colour="fire"),
    head("more", "Mehr Maschinen", 0, 15.6, colour="stone"),
    head("mekmm", "MoreMachine", 8, 15.2, colour="stone"),
    head("goal", "Das Ziel", 0, 20.2, colour="brass"),
]

chapter(C, "Mekanism: Fortgeschritten", "mekanism:advanced_control_circuit", "tech", quests, shape="square",
        order=19, stage=3,
        subtitle=["Stufe 3: Schaltkreise mit Silizium, Teleporter, Digitaler Miner, Turbine und Wärmeverdampfung."],
        images=images)
