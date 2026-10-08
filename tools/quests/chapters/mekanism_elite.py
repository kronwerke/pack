"""Mekanism in stage 4: the elite control circuit (draconium dust from the End), the ultimate
circuit, elite and ultimate installers, transmitters and storage, the combiner, the induction
matrix (lithium dust from the crystallizer, elite circuit in the port), the quantum
entangloporter, QIO, the dimensional stabilizer, the fusion reactor (laser, deuterium,
tritium, D-T fuel, hohlraum, the Kronwerke laser focus matrix with a source gem block,
polonium pellets from NuclearCraft), HDPE, MekaSuit, modules and Meka-Tool, and the stage 4
machines of Mekanism MoreMachine. Ore 4x and 5x live in mekanism_ores.py; SPS, antimatter
and fission in antimatter.py (stage 5). Recipes follow kubejs/server_scripts/kronwerke/tech.js,
numbers the jars and config/Mekanism (FE = J / 2.5)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mekanism_elite"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Elite und Ultimativ -----------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lBau einen Elite-Schaltkreis",
          subtitle="Ein Schaltkreis mit Drachenstaub.",
          description=[
              "&eRezept auf Kronwerke:&r oben Fortgeschrittener Schaltkreis, &5Draconiumstaub&r, Fortgeschrittener Schaltkreis. Darunter links und rechts je eine &6Verstärkte Legierung&r, Mitte frei.",
              "",
              img(item_texture("mekanism:elite_control_circuit"), 32, 32),
              "",
              "Draconium-Erz gibt es auf Kronwerke nur im &5End&r, es lässt 2 bis 4 Staub fallen. Mit &6Stufe 4, dem Sternwerk&r, öffnen Elite und Ultimativ, Induktionsmatrix, QIO, Fusion und MekaSuit.",
              "",
              "&cStufe 5:&r SPS, Antimaterie und Spaltreaktor, siehe Kapitel &5Mekanism: Antimaterie&r.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 1)],
          rewards=[reward_item("mekanism:alloy_reinforced", 8), reward_table("s4_common"), reward_xp(10)],
          icon="mekanism:elite_control_circuit", size=2.0, shape="hexagon"),

    quest("elite_stock", 2.75, 0.5, "&aLeg 16 Elite-Schaltkreise auf Vorrat",
          subtitle="Der Obelisk zählt jeden einzelnen.",
          description=[
              "Pro Stück zwei Fortgeschrittene Schaltkreise, zwei Verstärkte Legierungen, ein Draconiumstaub. Mach &e16&r.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 4 will &e150 Elite-Schaltkreise&r (20 Punkte pro Stück) und 1 000 Draconiumbarren.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_item("draconicevolution:draconium_dust", 8), reward_item("mekanism:alloy_reinforced", 16)],
          deps=["welcome"]),

    quest("ultimate", 5.25, 1.5, "&d&lBau einen Ultimativen Schaltkreis",
          subtitle="Elite in der Mitte, Atom außen.",
          description=[
              "Eine Reihe: &6Atomlegierung&r, Elite-Schaltkreis, Atomlegierung. Der Weg über die Infusionsanlage ist auf Kronwerke entfernt.",
              "",
              img(item_texture("mekanism:ultimate_control_circuit"), 32, 32),
              "",
              "Ultimative Schaltkreise stecken in QIO, Quantenverschränkungsporter, Fusion, MekaSuit und den Maschinen der Erzverfünffachung. Mach gleich mehr.",
          ],
          tasks=[task_item("mekanism:ultimate_control_circuit", 4)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="mekanism:ultimate_control_circuit", size=1.75, shape="hexagon"),

    quest("installers", 7.75, 0.5, "&aStuf eine Fabrik auf Elite",
          subtitle="Sieben Plätze.",
          description=[
              "&6Elite-Installateur:&r Verstärkte Legierung in die Ecken, Elite-Schaltkreise oben und unten, Gold links und rechts, ein Brett. Rechtsklick auf eine Fortschrittliche Fabrik.",
              "",
              "Eine Elite-Fabrik arbeitet an &esieben&r Gegenständen. Das geht auch für die Fabriken von MoreMachine.",
          ],
          tasks=[task_item("mekanism:elite_tier_installer", 1)],
          rewards=[reward_item("mekanism:alloy_reinforced", 4), reward_table("s4_common"), reward_xp(5)],
          deps=["elite_stock"], icon="mekanism:elite_tier_installer"),

    quest("ultimate_installer", 10.25, 0.5, "&dStuf eine Fabrik auf Ultimativ",
          subtitle="Neun Plätze, die letzte Stufe.",
          description=[
              "&6Ultimativ-Installateur:&r Atomlegierung in die Ecken, Ultimative Schaltkreise oben und unten, Diamanten links und rechts, ein Brett.",
              "",
              "Eine Ultimative Fabrik hat &eneun&r Plätze. Stell die langsamste Maschine deiner Straße zuerst um, dort staut es.",
          ],
          tasks=[task_item("mekanism:ultimate_tier_installer", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["installers", "ultimate"], icon="mekanism:ultimate_tier_installer"),

    quest("transmit", 7.75, 2.5, "&eLeg Ultimative Leitungen",
          subtitle="Eine Legierung, acht Leitungen.",
          description=[
              "Acht fortschrittliche Leitungen um eine &6Verstärkte Legierung&r geben Elite, acht Elite um eine &6Atomlegierung&r geben Ultimativ.",
              "",
              "&eUltimativ:&r Kabel &d3 276 800 FE/t&r, Transporter 64 Stück pro Zug, Druckschlauch 256 000 mB, Rohr 32 000 mB pro Zug.",
          ],
          tasks=[task_item("mekanism:ultimate_universal_cable", 16), task_item("mekanism:ultimate_logistical_transporter", 16)],
          rewards=[reward_item("mekanism:alloy_atomic", 2), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:ultimate_universal_cable", optional=True),

    quest("ult_storage", 10.25, 2.5, "&bStuf Würfel und Tanks auf Ultimativ",
          subtitle="Der größte Speicher pro Block.",
          description=[
              "Energie-Würfel, Tanks und Tonnen stufst du mit Verstärkter, dann Atomlegierung hoch. &6Ultimativer Würfel&r &d102,4 Millionen FE&r, &6Tank&r 256 000 mB, &6Chemikalienbehälter&r 8 192 000 mB, &6Tonne&r 262 144 Stück.",
          ],
          tasks=[task_item("mekanism:ultimate_energy_cube", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 4), reward_xp(5)],
          deps=["transmit"], icon="mekanism:ultimate_energy_cube", optional=True),

    quest("combiner", 12.75, 1.5, "&7Bau einen Kombinierer",
          subtitle="Rohes Erz wird wieder Erzblock.",
          description=[
              "Verstärkte Legierung in die Ecken, Elite-Schaltkreise oben und unten, Stein links und rechts, Stahlgehäuse in die Mitte.",
              "",
              "Er setzt zwei Gegenstände zu einem zusammen, etwa Rohes Erz und Bruchstein zu einem Erzblock. Mit dem &6Steingenerator-Upgrade&r braucht er keinen Bruchstein.",
          ],
          tasks=[task_item("mekanism:combiner", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(5)],
          deps=["elite_stock"], icon="mekanism:combiner", optional=True),

    quest("security_desk", 12.75, 3, "&8Stell ein Sicherheitspult auf",
          subtitle="Alle Maschinen auf einen Schlag sichern.",
          description=[
              "Oben Stahl, Glas, Stahl, Mitte &6Elite-Schaltkreis&r, &6Stahlgehäuse&r, Elite-Schaltkreis, unten Stahl, &6Netzwerklesegerät&r, Stahl. Das Lesegerät ist Glas, Infundierte Legierung, ein Energietablett und Stahl.",
              "",
              "Das Pult ist die Zentrale für alles, was dir gehört: Hier trägst du &evertraute Spieler&r ein und setzt die Sicherheit aller deiner Maschinen auf einmal, statt jede einzeln umzustellen.",
              "",
              "Auf einem Server mit vielen Spielern ist das der schnellste Weg, Teleporter, QIO und Fabrik vor fremden Händen zu schützen und Freunden trotzdem Zugang zu geben.",
          ],
          tasks=[task_item("mekanism:security_desk", 1)],
          rewards=[reward_item("mekanism:elite_control_circuit", 2), reward_xp(5)],
          deps=["elite_stock"], icon="mekanism:security_desk", optional=True),

    # ---- Induktionsmatrix --------------------------------------------------------------
    quest("lithium_dust", 0, 6.5, "&fKristallisier Lithiumstaub",
          subtitle="Aus Lithiumgas wird Staub.",
          description=[
              "Lithium aus der Wärmeverdampfungsanlage (Stufe 3) in den &6Chemischen Kristallisator&r: &e100 mB&r werden ein &6Lithiumstaub&r.",
              "",
              "Den Kristallisator kennst du aus der Erzverfünffachung im Kapitel &5Mekanism: Erz Schritt für Schritt&r. Jede Induktionszelle braucht vier Staub.",
          ],
          tasks=[task_item("mekanism:dust_lithium", 8)],
          rewards=[reward_item("mekanism:block_salt", 16), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:dust_lithium"),

    quest("induction_casing", 2.5, 6.5, "&9Bau Induktionsgehäuse und Anschluss",
          subtitle="Die Hülle des größten Akkus.",
          description=[
              "&6Induktionsgehäuse:&r vier Stahl um ein Energietablett, gibt vier. &6Induktionsanschluss:&r vier Gehäuse um einen &6Elite-Schaltkreis&r, gibt zwei.",
              "",
              "Die Hülle ist ein hohler Quader aus Gehäuse und Strukturglas, mindestens 3 mal 3 mal 3. Ein Anschluss nimmt Strom an, einen zweiten stellst du mit dem Konfigurator auf Ausgabe.",
          ],
          tasks=[task_item("mekanism:induction_casing", 24), task_item("mekanism:induction_port", 2)],
          rewards=[reward_item("mekanism:ingot_steel", 32), reward_xp(5)],
          deps=["lithium_dust"], icon="mekanism:induction_port"),

    quest("induction_cell", 5, 5.75, "&9Bau eine Induktionszelle",
          subtitle="3,2 Milliarden FE pro Block.",
          description=[
              "Lithiumstaub in die Ecken, Energietabletts an die Seiten, ein Einfacher Energie-Würfel in die Mitte. Eine &6Einfache Induktionszelle&r speichert &d3,2 Milliarden FE&r.",
              "",
              "Zellen stehen innen. Die höheren Stufen entstehen aus vier Zellen der Stufe darunter um einen Würfel, die fortschrittliche speichert achtmal so viel.",
          ],
          tasks=[task_item("mekanism:basic_induction_cell", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 4), reward_xp(5)],
          deps=["induction_casing"], icon="mekanism:basic_induction_cell"),

    quest("induction_provider", 5, 7.25, "&9Bau einen Induktionsanbieter",
          subtitle="Bestimmt, wie schnell Strom fließt.",
          description=[
              "Lithiumstaub in die Ecken, Schaltkreise an die Seiten, ein Einfacher Energie-Würfel in die Mitte. Ein &6Einfacher Anbieter&r schafft &d102 400 FE/t&r.",
              "",
              "Anbieter addieren sich. Ist die Matrix voll, aber deine Maschinen hungern, fehlen Anbieter, nicht Zellen.",
          ],
          tasks=[task_item("mekanism:basic_induction_provider", 1)],
          rewards=[reward_item("mekanism:basic_control_circuit", 4), reward_xp(5)],
          deps=["induction_casing"], icon="mekanism:basic_induction_provider"),

    quest("induction_matrix", 7.5, 6.5, "&9&lSetz die Induktionsmatrix zusammen",
          subtitle="Milliarden FE in einem Würfel.",
          description=[
              "Hülle schließen, innen Zellen und Anbieter, Anschlüsse in der Wand. Rechtsklick auf einen Anschluss zeigt Inhalt, Ein- und Ausgang.",
              "",
              "Häng Turbine und Fusion an den Eingang, die Fabriken an den Ausgang. In Stufe 5 frisst das SPS sie leer.",
          ],
          tasks=[task_checkmark("Die Matrix steht und lädt")],
          rewards=[reward_item("mekanism:basic_induction_cell", 1), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["induction_cell", "induction_provider"], icon="mekanism:induction_casing", size=1.75, shape="gear"),

    quest("adv_induction", 10, 6.5, "&9Stuf die Matrix hoch",
          subtitle="Achtmal Speicher, achtmal Durchsatz.",
          description=[
              "&6Fortgeschrittene Induktionszelle:&r vier Einfache Zellen und vier Energietabletts im Wechsel um einen &6Fortschrittlichen Energie-Würfel&r. Sie fasst &d25,6 Milliarden FE&r.",
              "",
              "&6Fortschrittlicher Induktionsanbieter:&r vier Einfache Anbieter und vier Fortgeschrittene Schaltkreise um einen Fortschrittlichen Würfel. Er schafft &d819 200 FE/t&r.",
              "",
              "Die Elite-Stufe macht das noch einmal achtmal: 204,8 Milliarden FE pro Zelle, gut 6,5 Millionen FE/t pro Anbieter. Tausch alte Zellen einfach aus, die Hülle bleibt stehen.",
          ],
          tasks=[task_item("mekanism:advanced_induction_cell", 1), task_item("mekanism:advanced_induction_provider", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["induction_matrix"], icon="mekanism:advanced_induction_cell", optional=True),

    # ---- Quanten und QIO ---------------------------------------------------------------
    quest("entangloporter", 0, 11.5, "&5Bau zwei Quantenverschränkungsporter",
          subtitle="Ohne Kabel ans andere Ende der Welt.",
          description=[
              "Ein &6Teleportationskern&r in der Mitte, Atomlegierung links und rechts, Ultimative Schaltkreise oben und unten, Raffiniertes Obsidian in die Ecken.",
              "",
              "Zwei Porter auf derselben &eFrequenz&r teilen einen Puffer: Strom, Gegenstände, Flüssigkeiten, Gase und Wärme, auch zwischen Dimensionen. Mit dem Konfigurator legst du jede Seite fest.",
          ],
          tasks=[task_item("mekanism:quantum_entangloporter", 2)],
          rewards=[reward_item("mekanism:teleportation_core", 2), reward_table("s4_common"), reward_xp(10)],
          deps=["ultimate"], icon="mekanism:quantum_entangloporter", size=1.5),

    quest("qio", 2.5, 11.5, "&d&lBau ein QIO-Lager",
          subtitle="Mekanisms Lagernetz ohne Kabel.",
          description=[
              "&6QIO Laufwerk Reihe:&r Teleportationskerne in die Ecken, Glasscheibe oben, Ultimative Schaltkreise links und rechts, Persönliche Truhe in der Mitte, Enderperle unten. &6QIO-Laufwerk:&r Blei in die Ecken, vier Ultimative Schaltkreise, eine Enderperle.",
              "",
              "Ein Laufwerk fasst &e16 000 Gegenstände&r in &e128 Sorten&r. Alle QIO-Blöcke auf derselben Frequenz sind ein Netz. Die großen Laufwerke brauchen Plutonium und Antimaterie aus Stufe 5.",
          ],
          tasks=[task_item("mekanism:qio_drive_array", 1), task_item("mekanism:qio_drive_base", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["entangloporter"], icon="mekanism:qio_drive_array", size=1.75, shape="hexagon"),

    quest("qio_dashboard", 5, 10.75, "&dStell ein QIO-Dashboard auf",
          subtitle="Deine Konsole mit Werkbank.",
          description=[
              "Blei in die Ecken, Enderperlen an die Seiten, oben eine Glasscheibe, unten ein Teleportationskern.",
              "",
              "Es zeigt alles im Netz, mit Suchfeld und Werkbankfenstern. Gib ihm dieselbe Frequenz wie der Laufwerk Reihe.",
          ],
          tasks=[task_item("mekanism:qio_dashboard", 1)],
          rewards=[reward_item("mekanism:ingot_lead", 16), reward_xp(5)],
          deps=["qio"], icon="mekanism:qio_dashboard"),

    quest("qio_io", 5, 12.25, "&dHäng Importeur und Exporteur an",
          subtitle="Maschinen ans Lager.",
          description=[
              "Blei, Teleportationskern, Enderperlen, ein Ultimativer Schaltkreis und ein Klebriger Kolben. Der &6Importeur&r zieht aus einem Block ins Netz, der &6Exporteur&r schiebt nach Filter hinein.",
              "",
              "Ein Exporteur mit Kohle-Filter an der Anreicherungskammer, ein Importeur am Ausgang, und die Kammer läuft aus dem Lager.",
          ],
          tasks=[task_item("mekanism:qio_importer", 1), task_item("mekanism:qio_exporter", 1)],
          rewards=[reward_item("minecraft:sticky_piston", 2), reward_xp(5)],
          deps=["qio"], icon="mekanism:qio_importer", optional=True),

    quest("qio_redstone", 7.5, 13, "&dLass das Lager Redstone geben",
          subtitle="Der QIO Redstone-Adapter.",
          description=[
              "Oben Enderperle, Redstonefackel, Enderperle, Mitte Ultimativer Schaltkreis, Redstone, Ultimativer Schaltkreis, unten Enderperle, &6Teleportationskern&r, Enderperle.",
              "",
              "Er hängt an deiner QIO-Frequenz und überwacht eine Sorte: Gib ihm einen Gegenstand und eine Menge, dann leuchtet sein Signal, sobald so viel davon im Lager liegt.",
              "",
              "So schaltet sich die Stahlstraße ab, wenn 10 000 Barren da sind, und wieder an, wenn das Lager schrumpft.",
          ],
          tasks=[task_item("mekanism:qio_redstone_adapter", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_xp(5)],
          deps=["qio"], icon="mekanism:qio_redstone_adapter", optional=True),

    quest("portable_qio", 7.5, 11.5, "&dNimm dein Lager mit",
          subtitle="Das Portable QIO Dashboard.",
          description=[
              "Ein QIO-Dashboard umringt von sieben &6Polonium Pellets&r und einem Teleportationskern unten. Damit hast du das Netz in der Tasche.",
              "",
              "Die Pellets kommen aus NuclearCraft, siehe Abschnitt Fusion.",
          ],
          tasks=[task_item("mekanism:portable_qio_dashboard", 1)],
          rewards=[reward_item("mekanism:teleportation_core", 1), reward_xp(10)],
          deps=["qio_dashboard", "polonium"], icon="mekanism:portable_qio_dashboard", optional=True),

    quest("stabilizer", 10, 11.5, "&7Bau einen Dimensionsstabilisator",
          subtitle="Hält Chunks geladen.",
          description=[
              "Raffiniertes Obsidian in die Ecken, Ultimative Schaltkreise oben und unten, Atomlegierung links und rechts, ein Diamantblock in die Mitte.",
              "",
              "Er hält die Chunks um sich herum geladen, welche, wählst du im Fenster. Für ganze Fabrikhallen besser als ein Ankerupgrade pro Maschine.",
          ],
          tasks=[task_item("mekanism:dimensional_stabilizer", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 2), reward_xp(5)],
          deps=["entangloporter"], icon="mekanism:dimensional_stabilizer", optional=True),

    # ---- Fusion ------------------------------------------------------------------------
    quest("laser", 0, 16.5, "&cBau Laser und Laser-Verstärker",
          subtitle="Das Zündholz des Reaktors.",
          description=[
              "&6Laser:&r links drei Verstärkte Legierungen, Mitte Energietablett, Stahlgehäuse, Energietablett, rechts ein Diamant. &6Verstärker:&r Stahl rundherum, Einfacher Energie-Würfel in der Mitte, rechts ein Diamant.",
              "",
              "Der Laser zieht &d4 000 FE/t&r und brennt alles weg, auch dich. Laser schießen in den Verstärker, der sammelt und feuert auf die Laser-Fokusmatrix, gesteuert mit Redstone und einem Schwellwert im Fenster.",
          ],
          tasks=[task_item("mekanism:laser", 1), task_item("mekanism:laser_amplifier", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:laser"),

    quest("deuterium", 2.5, 15.5, "&bPump Deuterium",
          subtitle="Schweres Wasser, gespalten.",
          description=[
              "Eine &6Elektrische Pumpe&r mit &6Filter-Upgrade&r holt &e10 mB Schweres Wasser&r pro Wasserblock. Der Elektrolyseur macht aus 2 mB davon &e2 mB Deuterium&r und 1 mB Sauerstoff.",
              "",
              "Zum Beweis ein Eimer flüssiges Deuterium aus dem Rotationskondensator.",
          ],
          tasks=[task_item("mekanismgenerators:deuterium_bucket", 1)],
          rewards=[reward_item("mekanism:upgrade_filter", 1), reward_xp(5)],
          deps=["laser"], icon="mekanismgenerators:deuterium_bucket"),

    quest("tritium", 2.5, 17.5, "&bAktivier Tritium",
          subtitle="Lithium unter der Sonne.",
          description=[
              "&6Solarneutronenaktivator:&r Verstärkte Legierung, HDPE Platte, Elite-Schaltkreise, Stahlgehäuse, Bronze. Bei Sonne macht er aus &e1 mB Lithium 1 mB Tritium&r.",
              "",
              "Er braucht freien Himmel und ruht nachts. Stell mehrere auf, einer allein ist langsam.",
          ],
          tasks=[task_item("mekanism:solar_neutron_activator", 1), task_item("mekanismgenerators:tritium_bucket", 1)],
          rewards=[reward_item("mekanism:dust_lithium", 8), reward_xp(5)],
          deps=["laser", "lithium_dust"], icon="mekanismgenerators:tritium_bucket"),

    quest("fuel", 5, 16.5, "&bFüll einen Hohlraum mit D-T-Treibstoff",
          subtitle="Deuterium und Tritium zusammen.",
          description=[
              "Chemischer Injektor: &e1 mB Deuterium + 1 mB Tritium = 2 mB D-T-Treibstoff&r. &6Hohlraum:&r vier Goldstaub mit 10 mB Kohlenstoff in der Infusionsanlage.",
              "",
              "Leg den Hohlraum in einen Chemikalienbehälter mit D-T-Treibstoff, er fasst &e10 mB&r. Gefüllt kommt er in den Reaktor-Controller und zündet.",
          ],
          tasks=[task_item("mekanismgenerators:hohlraum", 1)],
          rewards=[reward_item("mekanism:dust_gold", 8), reward_item("mekanism:enriched_carbon", 16), reward_xp(5)],
          deps=["deuterium", "tritium"], icon="mekanismgenerators:hohlraum"),

    quest("focus", 5, 18.5, "&dBau Laser-Fokusmatrizen",
          subtitle="Fusion braucht Magie zum Start.",
          description=[
              "&eRezept auf Kronwerke:&r oben links ein &dQuellenedelsteinblock&r von Ars Nouveau, Reaktorglas oben, links, rechts und unten in der Mitte, ein Redstoneblock in die Mitte. Gibt &ezwei&r.",
              "",
              "&6Reaktorglas:&r vier Angereichertes Eisen in die Ecken, vier Blei an die Seiten, Glas in die Mitte, gibt vier. Den Quellenedelsteinblock hat jeder Magier im Lager.",
          ],
          tasks=[task_item("mekanismgenerators:laser_focus_matrix", 1), task_item("mekanismgenerators:reactor_glass", 8)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 1), reward_xp(5)],
          deps=["laser"], icon="mekanismgenerators:laser_focus_matrix"),

    quest("polonium", 0, 19, "&a&lHol Polonium aus NuclearCraft",
          subtitle="Ein Umweg über den Spaltreaktor.",
          description=[
              "Thoriumstaub im &6Irradiator&r zu TBP, dann zu Protactinium-233. Der &6Decay Hastener&r macht Uran-233, dann &6Bismutstaub&r. Bismut im Irradiator gibt &6Poloniumstaub&r. Der &6Melter&r macht 90 mB pro Staub, der &6Crystallizer&r aus 1 000 mB ein &6Polonium Pellet&r.",
              "",
              "Rund elf Staub pro Pellet. Der Irradiator braucht einen laufenden Spaltreaktor, siehe Kapitel &aNuclearCraft&r. Mekanisms eigener Weg über Atommüll kommt erst in Stufe 5.",
              "",
              "&cVorsicht:&r Alles auf diesem Weg strahlt. Lager es weit weg von dir.",
          ],
          tasks=[task_item("mekanism:pellet_polonium", 4)],
          rewards=[reward_item("nuclearcraft:raw_thorium", 32), reward_table("s4_common"), reward_xp(15)],
          deps=["laser"], icon="mekanism:pellet_polonium", size=1.5, shape="hexagon"),

    quest("fusion_frame", 2.5, 19.5, "&6Bau Fusionsreaktorrahmen",
          subtitle="Vier Pellets, vier Rahmen.",
          description=[
              "Ein Stahlgehäuse in der Mitte, &6Atomlegierung&r in die Ecken, &6Polonium Pellets&r oben, unten, links und rechts. Gibt vier Rahmen.",
              "",
              "Vier Rahmen um einen Ultimativen Schaltkreis geben zwei &6Fusionsreaktor-Schnittstellen&r. Rechne mit ein paar Dutzend Rahmen.",
          ],
          tasks=[task_item("mekanismgenerators:fusion_reactor_frame", 32), task_item("mekanismgenerators:fusion_reactor_port", 2)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_xp(10)],
          deps=["polonium"], icon="mekanismgenerators:fusion_reactor_frame"),

    quest("fusion", 7.75, 17.5, "&6&lZünd den Fusionsreaktor",
          subtitle="Eine kleine Sonne im Keller.",
          description=[
              "&6Steuerung:&r Ultimative Schaltkreise oben links und rechts, Glasscheibe dazwischen, Chemikalienbehälter in der Mitte, Rahmen rundherum. Sie sitzt in der Mitte der Oberseite.",
              "",
              "&eForm:&r 5 mal 5 mal 5, jede Seite eine Raute (1, 3, 5, 3, 1 Blöcke). Außen Rahmen, im Plus jeder Seite Rahmen, Reaktorglas, Schnittstellen, Logikadapter oder die Fokusmatrix.",
              "",
              "&eZünden:&r Hohlraum in die Steuerung, Verstärker auf die Matrix feuern. Danach braucht er laufend D-T-Treibstoff über die Schnittstellen. Mit Wasser macht er Dampf für die Turbine.",
          ],
          tasks=[task_item("mekanismgenerators:fusion_reactor_controller", 1)],
          rewards=[reward_item("mekanismgenerators:reactor_glass", 16), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["fuel", "focus", "fusion_frame"], icon="mekanismgenerators:fusion_reactor_controller", size=2.0, shape="gear"),

    quest("fusion_logic", 10.25, 17.5, "&cBau einen Fusions-Logikadapter",
          subtitle="Der Reaktor meldet sich per Redstone.",
          description=[
              "Ein &6Fusionsreaktorrahmen&r mit vier Redstone im Kreuz. Er sitzt im Plus einer Seite, wie Glas und Schnittstellen.",
              "",
              "Im Fenster wählst du, wann er ein Signal gibt: &eBereit zur Zündung&r, sobald der Kern heiß genug ist, oder &eZu wenig Brennstoff&r, wenn der D-T-Treibstoff ausgeht. Ein Signal auf eine Lampe oder an den Laser-Verstärker, und du musst nicht danebenstehen.",
          ],
          tasks=[task_item("mekanismgenerators:fusion_reactor_logic_adapter", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_xp(5)],
          deps=["fusion"], icon="mekanismgenerators:fusion_reactor_logic_adapter", optional=True),

    quest("laser_tractor", 2.5, 20.5, "&cBohr mit dem Laser",
          subtitle="Der Laser-Traktorstrahl sammelt ein.",
          description=[
              "Eine &6Persönliche Truhe&r oder ein Persönliches Fass über einem &6Laser-Verstärker&r ergibt den &6Laser-Traktorstrahl&r.",
              "",
              "Laser zerstören Blöcke in ihrem Weg. Schieß sie in den Traktorstrahl: Er bündelt und lenkt sie wie ein Verstärker, und alles, was sein Strahl abbaut, landet in seinem Inventar statt auf dem Boden.",
              "",
              "&cVorsicht:&r Der Strahl trifft auch dich. Stell dich nie davor.",
          ],
          tasks=[task_item("mekanism:laser_tractor_beam", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2), reward_xp(5)],
          deps=["laser"], icon="mekanism:laser_tractor_beam", optional=True),

    # ---- MekaSuit ----------------------------------------------------------------------
    quest("hdpe", 0, 24, "&fPress HDPE Platten",
          subtitle="Kunststoff aus Ethen.",
          description=[
              "Druckreaktionskammer: &6Substrat&r mit 50 mB flüssigem Ethen und 10 mB Sauerstoff gibt ein &6HDPE-Pellet&r. Drei Pellets in der Anreicherungskammer geben eine &6HDPE Platte&r.",
              "",
              "Substrat vermehrt sich in derselben Kammer mit Wasser und Ethen, eins wird zu acht. Wie Ethen entsteht, steht im Kapitel &5Mekanism&r.",
          ],
          tasks=[task_item("mekanism:hdpe_sheet", 16)],
          rewards=[reward_item("mekanism:substrate", 16), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:hdpe_sheet"),

    quest("modstation", 2.5, 24, "&bBau eine Modifikationsstation",
          subtitle="Hier kommen die Module rein.",
          description=[
              "HDPE Platten in die Ecken, eine Truhe oben, Ultimative Schaltkreise links und rechts, Stahlgehäuse in der Mitte, ein Polonium Pellet unten.",
              "",
              "Leg Rüstung oder Werkzeug hinein, dann das Modul. Im Fenster der Station schaltest du jedes Modul ein und aus und stellst es ein.",
          ],
          tasks=[task_item("mekanism:modification_station", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_xp(5)],
          deps=["hdpe", "polonium"], icon="mekanism:modification_station"),

    quest("module_base", 5, 23.25, "&bBau Basismodule",
          subtitle="Der Rohling jedes Moduls.",
          description=[
              "Bronzenuggets in die Ecken, Zinn an die Seiten, eine HDPE Platte in die Mitte, gibt zwei.",
              "",
              "Jedes Modul ist ein Basismodul plus Legierungen und das Teil, das es nachahmt: ein Jetpack, ein Geigerzähler, eine Spitzhacke.",
          ],
          tasks=[task_item("mekanism:module_base", 4)],
          rewards=[reward_item("mekanism:ingot_bronze", 8), reward_xp(3)],
          deps=["modstation"], icon="mekanism:module_base"),

    quest("modules", 7.5, 23.25, "&bBau Energie- und Jetpack-Modul",
          subtitle="Das Wichtigste zuerst.",
          description=[
              "&6Energieeinheit:&r Infundierte Legierung, Basismodul, eine Einfache Induktionszelle, HDPE. Mehr Akku für alles. &6Jetpack-Einheit:&r Verstärkte Legierung, Basismodul, ein Jetpack, Polonium.",
              "",
              "&eFaustregel:&r einfache Module (Energie, Geigerzähler, Strahlenschutz) brauchen HDPE, starke (Jetpack, Servomotor, Nachtsicht, Magnet) Polonium.",
          ],
          tasks=[task_item("mekanism:module_energy_unit", 1), task_item("mekanism:module_jetpack_unit", 1)],
          rewards=[reward_item("mekanism:pellet_polonium", 2), reward_xp(10)],
          deps=["module_base"], icon="mekanism:module_jetpack_unit", optional=True),

    quest("mekasuit", 5, 25, "&b&lZieh die MekaSuit an",
          subtitle="Netherit, aufgerüstet.",
          description=[
              "&eJedes Teil:&r oben HDPE, Ultimativer Schaltkreis, HDPE, Mitte HDPE, das &6Netheritteil&r, HDPE, unten Polonium Pellet, Einfache Induktionszelle, Polonium Pellet.",
              "",
              "Die Rüstung läuft mit Strom statt Haltbarkeit und wächst mit Modulen. Acht Polonium Pellets und vier Induktionszellen für den vollen Satz.",
          ],
          tasks=[task_item("mekanism:mekasuit_helmet", 1), task_item("mekanism:mekasuit_bodyarmor", 1),
                 task_item("mekanism:mekasuit_pants", 1), task_item("mekanism:mekasuit_boots", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["module_base"], icon="mekanism:mekasuit_helmet", size=1.75, shape="hexagon"),

    quest("meka_tool", 7.5, 25, "&bBau das Meka-Werkzeug",
          subtitle="Ein Werkzeug für alles.",
          description=[
              "Oben Ultimativer Schaltkreis, Konfigurator, Ultimativer Schaltkreis, Mitte HDPE, &6Atomic Disassembler&r, HDPE, unten Polonium, Induktionszelle, Polonium.",
              "",
              "Spitzhacke, Axt, Schaufel, Hacke und Schwert mit Strom. Module für Abbautempo, Behutsamkeit, Glück und Aderabbau. Das Teleportationsmodul braucht Antimaterie aus Stufe 5.",
          ],
          tasks=[task_item("mekanism:meka_tool", 1)],
          rewards=[reward_item("mekanism:pellet_polonium", 2), reward_xp(15)],
          deps=["mekasuit"], icon="mekanism:meka_tool"),

    quest("mod_tools", 10, 25, "&bRüste das Meka-Werkzeug auf",
          subtitle="Schneller graben, ganze Adern auf einmal.",
          description=[
              "&6Abbaubeschleunigung:&r oben Infundierte Legierung, &6Eisenspitzhacke&r, Infundierte Legierung, Mitte Legierung, Basismodul, Legierung, unten drei HDPE Platten. Mehrere hintereinander machen das Werkzeug immer schneller.",
              "",
              "&6Aderabbau:&r oben Verstärkte Legierung, &6Diamantspitzhacke&r, Verstärkte Legierung, Mitte Diamantaxt, Basismodul, Diamantschaufel, unten drei Polonium Pellets. Er baut ganze Erzadern und Bäume mit einem Schlag ab. &eKronwerke:&r Der erweiterte Modus, der jeden Block der Ader nimmt, ist an.",
              "",
              "Dazu gibt es die Erzveredelung (Glück) und Behutsamkeit als eigene Module.",
          ],
          tasks=[task_item("mekanism:module_excavation_escalation_unit", 1), task_item("mekanism:module_vein_mining_unit", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_xp(10)],
          deps=["meka_tool"], icon="mekanism:module_vein_mining_unit", optional=True),

    quest("mod_move", 0, 26.25, "&bBau Bein- und Stiefelmodule",
          subtitle="Höher springen, schneller rennen.",
          description=[
              "&6Hydraulischer Antrieb:&r aus &6Freiläufern&r, Verstärkter Legierung, Energietabletts, Basismodul und Polonium. Du steigst höhere Stufen ohne Springen und springst selbst höher.",
              "",
              "&6Fortbewegungsverstärker:&r oben Verstärkte Legierung, &6Diamanthose&r, Verstärkte Legierung, Mitte Energietablett, Basismodul, Energietablett, unten drei Polonium Pellets. Er macht dich beim Sprinten schneller und lässt dich weiter springen.",
              "",
              "In der Modifikationsstation stellst du ein, wie stark jedes Modul wirkt. Volle Stufe kostet mehr Strom.",
          ],
          tasks=[task_item("mekanism:module_hydraulic_propulsion_unit", 1), task_item("mekanism:module_locomotive_boosting_unit", 1)],
          rewards=[reward_item("mekanism:pellet_polonium", 1), reward_xp(10)],
          deps=["mekasuit"], icon="mekanism:module_locomotive_boosting_unit", optional=True),

    quest("mod_life", 2.5, 26.25, "&bAtme und iss aus dem Anzug",
          subtitle="Sauerstoff aus Wasser, Essen aus der Paste.",
          description=[
              "&6Elektrolytische Atmung:&r oben Infundierte Legierung, &6Elektrolytischer Kern&r, Infundierte Legierung, Mitte Legierung, Basismodul, Legierung, unten drei HDPE Platten. Unter Wasser macht sie aus dem Wasser Sauerstoff zum Atmen und füllt nebenbei die Jetpack-Einheit mit Wasserstoff.",
              "",
              "&6Nährstoffinjektion:&r Verstärkte Legierung, eine &6Feldflasche&r, Basismodul und Polonium. Sie füttert dich mit Nährstoffpaste, sobald du Hunger hast. Die Paste macht der Nährstoffverflüssiger aus Stufe 3.",
          ],
          tasks=[task_item("mekanism:module_electrolytic_breathing_unit", 1), task_item("mekanism:module_nutritional_injection_unit", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_xp(10)],
          deps=["mekasuit"], icon="mekanism:module_electrolytic_breathing_unit", optional=True),

    quest("mod_sight", 5, 26.25, "&bSieh im Dunkeln, zieh Beute an",
          subtitle="Nachtsicht und Magnet.",
          description=[
              "&6Sichtverbesserung:&r oben Verstärkte Legierung, ein &6Smaragd&r, Verstärkte Legierung, Mitte Legierung, Basismodul, Legierung, unten drei Polonium Pellets. Sie hellt die Umgebung auf, mehrere davon wirken stärker.",
              "",
              "&6Magnetische Anziehung:&r oben Verstärkte Legierung, Eisengitter, Verstärkte Legierung, Mitte Elite-Schaltkreis, Basismodul, Elite-Schaltkreis, unten drei Polonium Pellets. Sie zieht Gegenstände in der Nähe zu dir, mehrere vergrößern die Reichweite.",
          ],
          tasks=[task_item("mekanism:module_vision_enhancement_unit", 1), task_item("mekanism:module_magnetic_attraction_unit", 1)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(10)],
          deps=["mekasuit"], icon="mekanism:module_vision_enhancement_unit", optional=True),

    quest("mod_power", 7.5, 26.25, "&eLade den Anzug unterwegs",
          subtitle="Sonne auf dem Helm, Hitze an den Beinen.",
          description=[
              "&6Solar-Ladeeinheit:&r Verstärkte Legierung, ein &6Erweiterter Solargenerator&r, Basismodul und Polonium. Bei Sonne lädt sie die MekaSuit, mehrere laden schneller.",
              "",
              "&6Geothermische Einheit:&r dasselbe mit einem &6Wärmegenerator&r. Sie lädt aus Hitze, Lava zählt laut Config fünfmal so viel wie Feuer, und mit voller Zahl Einheiten schluckt die Hose bis zu &e80 Prozent&r Schaden von Hitze.",
              "",
              "Mit beiden kommst du ohne Ladepad durch einen langen Tag im Nether.",
          ],
          tasks=[task_item("mekanismgenerators:module_solar_recharging_unit", 1), task_item("mekanismgenerators:module_geothermal_generator_unit", 1)],
          rewards=[reward_item("mekanismgenerators:advanced_solar_generator", 1), reward_xp(10)],
          deps=["mekasuit"], icon="mekanismgenerators:module_solar_recharging_unit", optional=True),

    # ---- MoreMachine -------------------------------------------------------------------
    quest("presser", 0, 29, "&3Bau einen Presser",
          subtitle="AE2-Prozessoren in einem Schritt.",
          description=[
              "Die CNC Stamper in die Mitte, Elite-Schaltkreise links und rechts, Kolben oben und unten, Verstärkte Legierung in die Ecken.",
              "",
              "Er presst drei Zutaten zu einem Teil: gedruckte Schaltung, Redstone und Gedrucktes Silizium werden zum fertigen &6AE2-Prozessor&r. Auch für Applied Flux und Advanced AE.",
          ],
          tasks=[task_item("mekmm:presser", 1)],
          rewards=[reward_item("ae2:engineering_processor", 2), reward_table("s4_common"), reward_xp(10)],
          deps=["elite_stock"], icon="mekmm:presser"),

    quest("planting", 2.5, 29, "&3Bau eine Pflanzstation",
          subtitle="Ernte ohne Feld.",
          description=[
              "Stahlgehäuse in der Mitte, Elite-Schaltkreise oben und unten, Bio-Brennstoff links und rechts, Verstärkte Legierung in die Ecken.",
              "",
              "Ein Samen mit &6Nährlösung&r gibt laufend Ernte, Weizen fünf pro Durchgang. Nährlösung macht die Auflösungskammer aus Bio-Brennstoff und Nährstoffpaste (Nährstoffverflüssiger, Stufe 3).",
          ],
          tasks=[task_item("mekmm:planting_station", 1)],
          rewards=[reward_item("mekanism:bio_fuel", 32), reward_xp(5)],
          deps=["presser"], icon="mekmm:planting_station", optional=True),

    quest("large", 5, 29, "&3Bau eine große Maschine",
          subtitle="Robit in der Mitte, Stahlblöcke drumherum.",
          description=[
              "Der &6Large C. Infuser&r: Robit in der Mitte, Ultimative Max-Chemikalientanks links und rechts, Ultimative Schaltkreise oben und unten, Stahlblöcke in die Ecken.",
              "",
              "Ebenso gibt es den großen Elektrolyseur, Rotationskondensator, Solarneutronenaktivator, Wärme- und Gasgenerator. Schau dir die Rezepte in JEI an. Der große Windgenerator kommt in Stufe 5.",
          ],
          tasks=[task_item("mekmm:large_chemical_infuser", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["planting"], icon="mekmm:large_chemical_infuser", optional=True),

    # ---- Das Ziel ----------------------------------------------------------------------
    quest("gas_stage5", 0, 33, "&fDie Gase von Stufe 5",
          subtitle="Was der Spaltreaktor mitbringt.",
          description=[
              "Uranoxid, Uranhexafluorid, Flusssäure, Spaltbrennstoff, Atommüll, Polonium, Plutonium, Antimaterie und überhitztes Natrium kommen mit Stufe 5.",
              "",
              "Wer sie macht und wofür: Kapitel &5Mekanism: Antimaterie&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(3)],
          deps=["fusion"], icon="mekanism:pellet_polonium", optional=True, section="goal"),

    quest("outlook", 2.5, 33, "&5Schau auf Stufe 5",
          subtitle="Was Plutonium und Antimaterie öffnen.",
          description=[
              "In Stufe 5 öffnen Spaltreaktor, SPS und Antimaterie im Kapitel &5Mekanism: Antimaterie&r.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 5 will &e100 Antimaterie-Pellets&r. Das SPS frisst Polonium und Strom, eine Fusionsanlage und eine volle Induktionsmatrix, die jetzt schon stehen, tragen es dann.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["fusion"], icon="mekanismgenerators:fusion_reactor_frame", optional=True, section="goal"),

    quest("goal", 5.5, 33, "&5&lBring Licht des Drachen zum Obelisken",
          subtitle="Schaltkreise für den Obelisken.",
          description=[
              "Leite Elite-Schaltkreise und Draconiumbarren in eine Kiste am Obelisken. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eTechnik-Pfeiler von Stufe 4:&r &6150 Elite-Steuerschaltkreise&r und &61 000 Draconiumbarren&r. Der Magie-Pfeiler will Gaia-Geister und Mystische Stäbe, beide müssen voll werden.",
              "",
              "Draconiumstaub, der nicht in Schaltkreise geht, wird im Ofen zum Barren und zählt dort.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 64)],
          rewards=[reward_table("s4_rare"), reward_item("mekanism:ultimate_control_circuit", 4), reward_xp(25)],
          deps=["elite_stock", "fusion"], icon="mekanism:elite_control_circuit", size=2.5, shape="gear"),
]

images = [
    head("title", "Mekanism: Elite", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("tiers", "Elite und Ultimativ", 5, -0.6, colour="brass"),
    head("induction", "Induktionsmatrix", 0, 4.4, colour="water"),
    head("quantum", "Quanten und QIO", 0, 9.4, colour="end"),
    head("fusion", "Fusion", 0, 14.2, colour="fire"),
    head("mekasuit", "MekaSuit", 0, 21.8, colour="water"),
    head("mekmm", "MoreMachine", 0, 27.2, colour="stone"),
    head("goal", "Das Ziel", 0, 31.2, colour="brass"),
]

chapter(C, "Mekanism: Elite", "mekanism:ultimate_control_circuit", "tech", quests, shape="square",
        order=34, stage=4,
        subtitle=["Stufe 4: Elite und Ultimativ, Induktionsmatrix, QIO, Fusion und MekaSuit."],
        images=images)
