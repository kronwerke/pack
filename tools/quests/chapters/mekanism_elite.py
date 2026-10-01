"""Mekanism in stage 4: the elite control circuit (draconium dust from the End), the ultimate
circuit, elite and ultimate tier installers and transmitters, ore quadrupling with the chemical
injection chamber, ore quintupling with dissolution chamber, washer and crystallizer, the quantum
entangloporter, QIO, the fusion reactor (laser, D-T fuel, hohlraum, the Kronwerke laser focus
matrix) and the stage 4 machines of Mekanism MoreMachine. Continues mekanism_advanced.py.
Polonium pellets open in stage 4 and come from NuclearCraft (bismuth irradiated in a fission
reactor), so the fusion frame, MekaSuit, Meka-Tool and the polonium modules are quests here.
Antimatter, SPS, Mekanism fission, plutonium and the big QIO drives stay stage 5 and are text only.
Recipes follow kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mekanism_elite"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Elite und Ultimativ ------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lMekanism: Elite",
          subtitle="Ein Schaltkreis mit Drachenstaub.",
          description=[
              "Mit &6Stufe 4, dem Sternwerk&r, öffnet Mekanism seine obersten Stufen. Alles beginnt mit dem &6Elitären Steuerschaltkreis&r, hier kurz Elite-Schaltkreis.",
              "",
              "&eRezept auf Kronwerke:&r oben Fortschrittlicher Steuerschaltkreis, &5Draconiumstaub&r, Fortschrittlicher Steuerschaltkreis. Darunter links und rechts je eine &6Verstärkte Legierung&r, die Mitte bleibt frei. Alle anderen Wege zu diesem Schaltkreis gibt es nicht mehr.",
              "",
              img(item_texture("mekanism:elite_control_circuit"), 32, 32),
              "",
              "&eWoher der Staub kommt:&r Draconium-Erz gibt es auf Kronwerke nur noch im &5End&r. Abgebaut lässt es &e2 bis 4 Draconiumstaub&r fallen, mit Glück mehr. Mekanisms Erzstraßen kennen Draconium nicht, also nimm eine gute Spitzhacke mit Glück mit.",
              "",
              "&eWas jetzt offen ist:&r Elite- und Ultimativ-Stufe, Vervierfachung und Verfünffachung der Erze, der Quantenverschränkungsporter, QIO, der Fusionsreaktor, MekaSuit und Meka-Werkzeug und die großen Maschinen von Mekanism MoreMachine.",
              "",
              "&cWas noch wartet:&r Antimaterie, SPS, Plutonium und der Spaltreaktor von Mekanism kommen in Stufe 5. Das &6Polonium&r für Fusion und MekaSuit holst du dir in Stufe 4 aus &aNuclearCraft&r.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 1)],
          rewards=[reward_item("mekanism:alloy_reinforced", 8), reward_table("s4_common"), reward_xp(10)],
          icon="mekanism:elite_control_circuit", size=2.0, shape="hexagon"),

    quest("elite_stock", 2.75, 0, "&aElite-Schaltkreise auf Vorrat",
          subtitle="Der Obelisk zählt jeden einzelnen.",
          description=[
              "Injektionskammer, Elite-Installateur, Elite-Fabriken und der Ultimative Schaltkreis: fast alles in diesem Kapitel will Elite-Steuerschaltkreise.",
              "",
              "Pro Schaltkreis brauchst du zwei Fortschrittliche, zwei Verstärkte Legierungen und einen Draconiumstaub. Die Fortschrittlichen kommen weiter aus deiner Linie mit Gedrucktem Silizium aus Stufe 3, die Legierungen aus der Infusionsanlage mit Diamant.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 4 heißt &6Licht des Drachen&r. Im Technik-Pfeiler will es &e150 Elite-Steuerschaltkreise&r, jeder zählt 20 Punkte, dazu 1 000 Draconiumbarren. Ein Vorrat lohnt sich also doppelt.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_item("draconicevolution:draconium_dust", 8), reward_item("mekanism:alloy_reinforced", 16)],
          deps=["welcome"]),

    quest("ultimate", 5.25, 1.5, "&d&lUltimativer Steuerschaltkreis",
          subtitle="Elite in der Mitte, Atom außen.",
          description=[
              "Der &6Ultimative Steuerschaltkreis&r ist die letzte Stufe. &eRezept:&r eine Reihe aus Atomlegierung, Elite-Steuerschaltkreis, Atomlegierung. Der Weg über die Infusionsanlage ist auf Kronwerke entfernt, es bleibt nur dieses Rezept.",
              "",
              img(item_texture("mekanism:ultimate_control_circuit"), 32, 32),
              "",
              "Die Atomlegierung kennst du aus Stufe 3: Verstärkte Legierung mit 40 mB Raffiniertem Obsidian in der Infusionsanlage.",
              "",
              "Ultimative Schaltkreise stecken in den Maschinen der Verfünffachung, im Quantenverschränkungsporter, in allen QIO-Teilen und im Fusionsreaktor. Mach gleich ein paar mehr.",
          ],
          tasks=[task_item("mekanism:ultimate_control_circuit", 4)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="mekanism:ultimate_control_circuit", size=1.75, shape="hexagon"),

    quest("installers", 7.75, 0.5, "&aElite- und Ultimativ-Installateur",
          subtitle="Sieben Plätze, dann neun.",
          description=[
              "Die Stufen-Installateure heben eine Fabrik eine Stufe höher, ohne dass sie ihren Inhalt verliert. Klick den Installateur einfach auf die stehende Fabrik.",
              "",
              "&6Elite-Installateur:&r Verstärkte Legierung in die Ecken, Elite-Schaltkreise oben und unten, Gold links und rechts, ein Brett in die Mitte. Eine Elite-Fabrik arbeitet an &esieben&r Gegenständen gleichzeitig.",
              "&6Ultimativ-Installateur:&r Atomlegierung in die Ecken, Ultimative Schaltkreise oben und unten, Diamanten links und rechts, ein Brett in die Mitte. Eine Ultimative Fabrik hat &eneun&r Plätze.",
              "",
              "Fabriken kannst du auch direkt an der Werkbank hochstufen, die Rezepte sind gleich aufgebaut, nur mit der Fabrik der Stufe darunter in der Mitte.",
          ],
          tasks=[task_item("mekanism:elite_tier_installer", 1), task_item("mekanism:ultimate_tier_installer", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["ultimate"], icon="mekanism:ultimate_tier_installer"),

    quest("transmit", 7.75, 2.5, "&eUltimative Leitungen",
          subtitle="Eine Legierung, acht Kabel.",
          description=[
              "Acht fortschrittliche Kabel, Transporter, Rohre oder Druckschläuche um eine &6Verstärkte Legierung&r ergeben acht der Elite-Sorte. Acht Elite-Leitungen um eine &6Atomlegierung&r ergeben acht ultimative.",
              "",
              "Eine Straße mit neun Plätzen pro Fabrik zieht viel mehr Strom und schiebt viel mehr Gegenstände und Chemikalien als vorher. Wenn eine Fabrik mit vollem Puffer auf Nachschub wartet, liegt es fast immer an einer zu schwachen Leitung.",
              "",
              "&eTipp:&r Bei Energie hilft eine &6Induktionsmatrix&r mit Elite- oder Ultimativ-Zellen und Anbietern. Die sind jetzt auch offen.",
          ],
          tasks=[task_item("mekanism:ultimate_universal_cable", 16), task_item("mekanism:ultimate_logistical_transporter", 16)],
          rewards=[reward_item("mekanism:alloy_atomic", 2), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:ultimate_universal_cable", optional=True),

    # ---- Vervierfachung -------------------------------------------------------------
    quest("hcl", 0, 6.5, "&bChlorwasserstoff",
          subtitle="Sole, Wasser, zwei Gase.",
          description=[
              "Die Injektionskammer braucht &bChlorwasserstoff&r. Den macht der &6Chemische Injektor&r aus &bWasserstoff&r und &bChlor&r, je 1 mB.",
              "",
              "&eWasserstoff:&r ein Elektrolyseur mit Wasser, wie für den Sauerstoff aus Stufe 3. Der Wasserstoff, den du dort abgelassen hast, wird jetzt gebraucht.",
              "&eChlor:&r ein zweiter Elektrolyseur mit &6Sole&r. Er spaltet sie in Natrium und Chlor. Sole bekommst du aus einer &6Wärmeverdampfungsanlage&r (aus 10 mB Wasser wird 1 mB Sole), oder aus Salz: Salzstaub im &6Chemischen Oxidierer&r gibt 15 mB Sole als Gas, die &6Rotationskondensator&r macht sie flüssig.",
              "",
              "Das Salz, das du dir seit Stufe 2 aufgehoben hast, kommt hier zum Einsatz.",
          ],
          tasks=[task_item("mekanism:chemical_infuser", 1), task_item("mekanism:electrolytic_separator", 2)],
          rewards=[reward_item("mekanism:basic_pressurized_tube", 16), reward_xp(5)],
          deps=["welcome"], icon="mekanism:chemical_infuser"),

    quest("injection", 2.75, 6.5, "&d&lChemische Injektionskammer",
          subtitle="Vier Splitter aus einem Erz.",
          description=[
              "&eRezept:&r die Klärkammer aus Stufe 3 in der Mitte, Gold links und rechts, Elite-Steuerschaltkreise oben und unten, Verstärkte Legierung in die Ecken.",
              "",
              "Sie nimmt ein Erz und Chlorwasserstoff und macht daraus &6Splitter&r. Wie die Klärkammer verbraucht sie in jedem Tick Gas, solange sie arbeitet.",
              "",
              "&eWas herauskommt:&r",
              "Ein Erzblock ergibt &e4 Splitter&r.",
              "Drei Rohe Erze ergeben &e8 Splitter&r.",
              "",
              "&eNebenbei:&r Schießpulver in der Injektionskammer wird zu &6Schwefelstaub&r. Den brauchst du gleich für die Verfünffachung.",
          ],
          tasks=[task_item("mekanism:chemical_injection_chamber", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s4_common"), reward_xp(10)],
          deps=["hcl"], icon="mekanism:chemical_injection_chamber", size=1.75, shape="hexagon"),

    quest("quadrupling", 5.25, 6.5, "&d&lErzvervierfachung",
          subtitle="Injektion, dann die alte Straße.",
          description=[
              "Splitter laufen durch deine Straße aus Stufe 3: Die &6Klärkammer&r macht aus jedem Splitter einen Klumpen, danach Zerkleinerer, Anreicherungskammer und Schmelzer wie gehabt.",
              "",
              img(item_texture("mekanism:shard_gold"), 32, 32),
              "",
              "&eDie Vierfach-Straße:&r Injektionskammer, Klärkammer, Zerkleinerer, Anreicherungskammer, Energiegeladener Schmelzer. Die Injektionskammer kommt einfach vor deine Dreifach-Straße.",
              "",
              "&eGlück oder Behutsamkeit?&r Ein Erzblock gibt vier Barren. Mit &6Glück III&r fallen im Schnitt etwa 2,2 Rohe Erze, und drei Rohe Erze geben acht Splitter. Das sind rund sechs Barren pro Erz. Glück bleibt also die bessere Wahl.",
              "",
              "Elite-Fabriken gibt es auch für die Injektionskammer, sieben Erze auf einmal.",
          ],
          tasks=[task_item("mekanism:shard_iron", 32), task_item("mekanism:shard_gold", 16)],
          rewards=[reward_item("minecraft:raw_gold", 32), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["injection"], icon="mekanism:shard_gold", size=2.0, shape="gear"),

    # ---- Verfünffachung -------------------------------------------------------------
    quest("acid", 0, 11.5, "&eSchwefelsäure",
          subtitle="Drei Schritte zur Säure.",
          description=[
              "Die Auflösungskammer löst Erz in &eSchwefelsäure&r. So entsteht sie:",
              "",
              "&e1.&r &6Schwefelstaub&r in den &6Chemischen Oxidierer&r, das gibt 100 mB &eSchwefeldioxid&r.",
              "&e2.&r Im &6Chemischen Injektor&r: 2 mB Schwefeldioxid und 1 mB Sauerstoff ergeben 2 mB &eSchwefeltrioxid&r.",
              "&e3.&r Ein &6Rotationskondensator&r macht aus Wasser &bWasserdampf&r. Im zweiten Injektor ergeben Schwefeltrioxid und Wasserdampf zu gleichen Teilen &eSchwefelsäure&r.",
              "",
              "Den Schwefel bekommst du aus Schießpulver in der Injektionskammer. Schwefelstaub aus anderen Mods geht genauso, der Oxidierer nimmt alles, was als Schwefelstaub gilt.",
          ],
          tasks=[task_item("mekanism:chemical_oxidizer", 1), task_item("mekanism:rotary_condensentrator", 1),
                 task_item("mekanism:dust_sulfur", 16)],
          rewards=[reward_item("minecraft:gunpowder", 32), reward_xp(5)],
          deps=["injection"], icon="mekanism:dust_sulfur"),

    quest("dissolution", 2.75, 11.5, "&d&lChemische Auflösungskammer",
          subtitle="Aus Erz wird Schlamm.",
          description=[
              "&eRezept:&r ein Stahlgehäuse in der Mitte, Ultimative Steuerschaltkreise links und rechts, einfache Chemikalientanks oben und unten, Raffinierte Obsidianbarren in die Ecken.",
              "",
              "Sie löst ein Erz in Schwefelsäure und macht daraus &6Schmutzigen Schlamm&r, ein Gas, das du in Tanks und Druckschläuchen bewegst.",
              "",
              "&eWas herauskommt:&r",
              "Ein Erzblock ergibt &e1 000 mB&r Schlamm.",
              "Drei Rohe Erze ergeben &e2 000 mB&r.",
              "",
              "Auch sie verbraucht Säure in jedem Tick, solange sie arbeitet. Plan die Säureproduktion also großzügig.",
          ],
          tasks=[task_item("mekanism:chemical_dissolution_chamber", 1)],
          rewards=[reward_item("mekanism:ingot_refined_obsidian", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["acid", "ultimate"], icon="mekanism:chemical_dissolution_chamber", size=1.75, shape="hexagon"),

    quest("crystals", 5.25, 11.5, "&bWaschanlage und Kristallisator",
          subtitle="Sauberer Schlamm, harte Kristalle.",
          description=[
              "&6Chemische Waschanlage:&r Stahlgehäuse in der Mitte, Ultimative Schaltkreise links und rechts, oben ein einfacher Flüssigkeitstank, unten ein einfacher Chemikalientank, Raffiniertes Obsidian in die Ecken. Er wäscht mit 5 mB Wasser je 1 mB Schmutzigen Schlamm zu &6Sauberem Schlamm&r. Wasser braucht er viel, eine Elektrische Pumpe in einer Wasserquelle reicht.",
              "",
              "&6Chemischer Kristallisator:&r Stahlgehäuse in der Mitte, Ultimative Schaltkreise links und rechts, &6Fluorit&r oben und unten, Raffiniertes Obsidian in die Ecken. Aus 200 mB Sauberem Schlamm macht er einen &6Kristall&r.",
              "",
              img(item_texture("mekanism:crystal_iron"), 32, 32),
          ],
          tasks=[task_item("mekanism:chemical_washer", 1), task_item("mekanism:chemical_crystallizer", 1),
                 task_item("mekanism:crystal_iron", 16)],
          rewards=[reward_item("mekanism:fluorite_gem", 16), reward_xp(10)],
          deps=["dissolution"], icon="mekanism:chemical_crystallizer"),

    quest("quintupling", 7.75, 11.5, "&d&lErzverfünffachung",
          subtitle="Fünf Barren aus einem Erz.",
          description=[
              "1 000 mB Schlamm aus einem Erzblock werden zu fünf Kristallen. Die Kristalle gehen in die &6Injektionskammer&r und werden zu Splittern, ab da läuft alles wie bei der Vervierfachung.",
              "",
              "&eDie ganze Straße:&r Auflösungskammer, Waschanlage, Kristallisator, Injektionskammer, Klärkammer, Zerkleinerer, Anreicherungskammer, Schmelzer. Acht Maschinen und vier Gase: Schwefelsäure, Wasser, Chlorwasserstoff, Sauerstoff.",
              "",
              "&eLohnt sich das?&r Ein Erzblock gibt fünf Barren statt vier. Drei Rohe Erze werden zu zehn Barren statt acht, mit Glück III also gut sieben Barren pro abgebautem Erz. Für die großen Mengen an Eisen, Kupfer und Gold, die Stufe 4 und 5 schlucken, lohnt es sich.",
          ],
          tasks=[task_item("mekanism:crystal_copper", 32), task_item("mekanism:crystal_gold", 16)],
          rewards=[reward_item("minecraft:raw_copper", 64), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["crystals", "quadrupling"], icon="mekanism:crystal_gold", size=2.0, shape="gear"),

    # ---- Quanten und QIO ------------------------------------------------------------
    quest("entangloporter", 0, 16, "&5Quantenverschränkungsporter",
          subtitle="Ohne Kabel ans andere Ende der Welt.",
          description=[
              "&eRezept:&r ein &6Teleportationskern&r in der Mitte, Atomlegierung links und rechts, Ultimative Schaltkreise oben und unten, Raffiniertes Obsidian in die Ecken.",
              "",
              "Zwei Porter auf derselben &6Frequenz&r teilen sich einen Puffer. Was du in einen hineinschickst, kommt am anderen heraus: &eStrom, Gegenstände, Flüssigkeiten, Chemikalien und Wärme&r. Das geht auch zwischen Dimensionen.",
              "",
              "Im Fenster legst du die Frequenz an und stellst sie öffentlich, privat oder für vertraute Spieler ein. Mit dem Konfigurator legst du für jede Seite fest, was hinein und was heraus geht.",
              "",
              "&eTipp:&r Ein Porter am Kraftwerk, einer an der Erzstraße. So bleibt der Lärm weg von deiner Basis.",
          ],
          tasks=[task_item("mekanism:quantum_entangloporter", 2)],
          rewards=[reward_item("mekanism:teleportation_core", 2), reward_table("s4_common"), reward_xp(10)],
          deps=["ultimate"], icon="mekanism:quantum_entangloporter", size=1.5),

    quest("qio", 2.75, 16, "&d&lQIO",
          subtitle="Mekanisms eigenes Lagernetz.",
          description=[
              "&6Quantum Item Orchestration&r ist ein Lager über Frequenzen, ganz ohne Kabel. Jeder QIO-Block mit derselben Frequenz gehört zum selben Netz.",
              "",
              "&6QIO Laufwerk Reihe:&r Teleportationskerne oben und unten in den Ecken, Glasscheibe oben in der Mitte, Ultimative Schaltkreise links und rechts, eine Persönliche Truhe oder ein Persönliches Fass in der Mitte, eine Enderperle unten. Darin stecken die Laufwerke.",
              "&6QIO-Laufwerk:&r Blei in die Ecken, vier Ultimative Schaltkreise, eine Enderperle in der Mitte. Es fasst &e16 000 Gegenstände&r in &e128 Sorten&r.",
              "&6QIO-Dashboard:&r Blei, Enderperlen, eine Glasscheibe und ein Teleportationskern. Das ist deine Konsole, mit Werkbankfenstern.",
              "",
              "&6Importer&r und &6Exporter&r (Blei, Teleportationskern, Enderperlen, ein Ultimativer Schaltkreis und ein klebriger oder normaler Kolben) holen aus Maschinen und schieben hinein.",
              "",
              "&eUnterwegs:&r Das &6Portable QIO Dashboard&r ist ein Dashboard mit sieben Polonium Pellets und einem Teleportationskern drumherum. Damit hast du dein Lager in der Tasche.",
              "",
              "&cGrößere Laufwerke:&r Das hyperdichte Laufwerk und alle darüber brauchen Plutonium oder Antimaterie und kommen erst in Stufe 5.",
          ],
          tasks=[task_item("mekanism:qio_drive_array", 1), task_item("mekanism:qio_drive_base", 2),
                 task_item("mekanism:qio_dashboard", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["entangloporter"], icon="mekanism:qio_drive_array", size=1.75, shape="hexagon"),

    # ---- Fusion ---------------------------------------------------------------------
    quest("laser", 0, 20.5, "&cLaser und Laser-Verstärker",
          subtitle="Das Zündholz des Reaktors.",
          description=[
              "&6Laser:&r drei Verstärkte Legierungen links in einer Reihe, zwei Energietabletts, ein Stahlgehäuse in der Mitte, ein Diamant rechts. Mit Strom schießt er einen Strahl in Blickrichtung. Der Strahl baut Blöcke ab und verbrennt alles, was im Weg steht, auch dich.",
              "",
              "&6Laser-Verstärker:&r Stahl rundherum, ein einfacher Energie-Würfel in der Mitte, ein Diamant rechts. Er sammelt Laserenergie und gibt sie gebündelt wieder ab, gesteuert über Redstone und Schwellenwerte im Fenster.",
              "",
              "Für den Fusionsreaktor schießen ein oder mehrere Laser in einen Verstärker, und der Verstärker feuert auf die &6Laser-Fokusmatrix&r in der Reaktorwand.",
          ],
          tasks=[task_item("mekanism:laser", 1), task_item("mekanism:laser_amplifier", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2), reward_xp(5)],
          deps=["ultimate"], icon="mekanism:laser"),

    quest("fuel", 2.75, 20.5, "&bD-T-Treibstoff und Hohlraum",
          subtitle="Deuterium und Tritium.",
          description=[
              "&eDeuterium:&r Eine &6Elektrische Pumpe&r mit &6Filter-Upgrade&r holt aus jedem Wasserblock 10 mB &bSchweres Wasser&r. Der Elektrolyseur spaltet es in Deuterium und Sauerstoff.",
              "&eTritium:&r &6Lithium&r aus der Wärmeverdampfungsanlage (aus Sole wird flüssiges Lithium, der Rotationskondensator macht es zum Gas) oder Lithiumstaub im Chemischen Oxidierer. Der &6Solarneutronenaktivator&r macht daraus bei Sonne Tritium.",
              "&eD-T-Treibstoff:&r Im Chemischen Injektor ergeben 1 mB Deuterium und 1 mB Tritium 2 mB Treibstoff.",
              "",
              "&6Hohlraum:&r In der Metallurgischen Infusionsanlage ergeben vier Goldstaub und 10 mB Kohlenstoff einen Hohlraum. Füll ihn in einem Chemikalientank mit D-T-Treibstoff. Gefüllt kommt er in den Reaktor-Controller und liefert den Brennstoff für die Zündung.",
          ],
          tasks=[task_item("mekanism:solar_neutron_activator", 1), task_item("mekanismgenerators:hohlraum", 1)],
          rewards=[reward_item("mekanism:dust_gold", 8), reward_item("mekanism:enriched_carbon", 16), reward_xp(5)],
          deps=["laser"], icon="mekanismgenerators:hohlraum"),

    quest("focus", 2.75, 22.5, "&dLaser-Fokusmatrix",
          subtitle="Fusion braucht Magie zum Start.",
          description=[
              "Die &6Laser-Fokusmatrix&r sitzt in der Reaktorwand und nimmt den Laserstrahl auf.",
              "",
              "&eRezept auf Kronwerke:&r oben links ein &dQuellenedelsteinblock&r von Ars Nouveau, &6Reaktorglas&r oben in der Mitte, links, rechts und unten in der Mitte, ein &cRedstoneblock&r in die Mitte. Das gibt &ezwei&r Matrizen.",
              "",
              "&6Reaktorglas:&r vier Angereichertes Eisen in die Ecken, vier Blei an die Seiten, Glas in die Mitte, das gibt vier Stück.",
              "",
              "Den Quellenedelsteinblock hat jeder Magier im Lager. Frag einfach.",
          ],
          tasks=[task_item("mekanismgenerators:laser_focus_matrix", 1), task_item("mekanismgenerators:reactor_glass", 8)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 1), reward_xp(5)],
          deps=["laser"], icon="mekanismgenerators:laser_focus_matrix"),

    quest("polonium", 0, 22.5, "&a&lPolonium Pellets",
          subtitle="Ein Umweg über NuclearCraft.",
          description=[
              "Mekanism selbst macht Polonium nur aus Atommüll seines Spaltreaktors, und der kommt erst in Stufe 5. In Stufe 4 kommen die &6Polonium Pellets&r aus &aNuclearCraft&r. Du brauchst dafür einen laufenden Spaltreaktor mit Bestrahlungslinie, siehe Kapitel NuclearCraft.",
              "",
              "&eDer Weg vom Thorium zum Pellet:&r",
              "&e1.&r Thoriumstaub im &6Irradiator&r wird zu TBP-Staub, TBP im Irradiator zu Protactinium-233.",
              "&e2.&r Der &6Decay Hastener&r macht aus Protactinium-233 Uran-233 und aus Uran-233 &6Bismutstaub&r.",
              "&e3.&r Bismutstaub im Irradiator wird zu &6Poloniumstaub&r.",
              "&e4.&r Der &6Melter&r macht aus jedem Poloniumstaub 90 mB geschmolzenes Polonium. Der &6Crystallizer&r von NuclearCraft macht aus 1 000 mB ein &6Polonium Pellet&r von Mekanism.",
              "",
              "Ein Pellet kostet also gut elf Poloniumstaub. Lass die Kette ruhig laufen, Rahmen, MekaSuit und Module wollen viele davon.",
              "",
              "&cVorsicht:&r Alles auf diesem Weg strahlt. Lager es in Kisten weit weg von dir.",
          ],
          tasks=[task_item("mekanism:pellet_polonium", 4)],
          rewards=[reward_item("nuclearcraft:raw_thorium", 32), reward_table("s4_common"), reward_xp(15)],
          deps=["laser"], icon="mekanism:pellet_polonium", size=1.5, shape="hexagon"),

    quest("fusion", 5.5, 21.5, "&6&lFusionsreaktor",
          subtitle="Eine kleine Sonne im Keller.",
          description=[
              "&eDie Form:&r 5 mal 5 mal 5 Blöcke, aber kein voller Würfel. Jede der sechs Seiten ist eine Raute: ein Block in der obersten Reihe, drei in der zweiten, fünf in der mittleren, dann wieder drei und einer. Die äußeren Blöcke jeder Raute sind &6Reaktorrahmen&r. In das Plus aus fünf Blöcken in der Mitte jeder Seite kommen Reaktorrahmen, &6Reaktorglas&r, &6Fusionsreaktor-Schnittstellen&r, &6Logikadapter&r oder die &6Laser-Fokusmatrix&r.",
              "",
              "Die &6Fusionsreaktorsteuerung&r (der Controller) sitzt genau in der Mitte der Oberseite. &eRezept:&r Ultimative Schaltkreise oben links und rechts, eine Glasscheibe dazwischen, ein einfacher Chemikalientank in der Mitte, Rahmen rundherum.",
              "",
              "&eZünden:&r Leg den gefüllten Hohlraum in den Controller und feuere mit dem Laser-Verstärker auf die Matrix, bis das Plasma heiß genug ist. Danach braucht der Reaktor laufend Deuterium und Tritium oder fertigen D-T-Treibstoff über die Anschlüsse. Strom gibt er über die Anschlüsse ab, mit Wasser macht er Dampf für die Industrieturbine.",
              "",
              "&6Fusionsreaktorrahmen:&r ein Stahlgehäuse in der Mitte, Atomlegierung in die Ecken, &6Polonium Pellets&r oben, unten, links und rechts. Das gibt vier Rahmen. Für die &6Fusionsreaktor-Schnittstellen&r kommen vier Rahmen um einen Ultimativen Schaltkreis, das gibt zwei. Rechne mit ein paar Dutzend Rahmen, also mit einigen Polonium Pellets.",
          ],
          tasks=[task_item("mekanismgenerators:fusion_reactor_frame", 32), task_item("mekanismgenerators:fusion_reactor_controller", 1),
                 task_item("mekanismgenerators:fusion_reactor_port", 2)],
          rewards=[reward_item("mekanismgenerators:reactor_glass", 16), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["fuel", "focus", "polonium"], icon="mekanismgenerators:fusion_reactor_controller", size=2.0, shape="gear"),

    # ---- Mekanism MoreMachine -------------------------------------------------------
    quest("presser", 0, 26, "&3Presser und Pflanzstation",
          subtitle="Zwei Maschinen mit Elite-Schaltkreisen.",
          description=[
              "Zwei Maschinen aus &6Mekanism MoreMachine&r brauchen Elite-Schaltkreise und gehen deshalb erst jetzt:",
              "",
              "&6Presser:&r die CNC Stamper in der Mitte, Elite-Schaltkreise links und rechts, Kolben oben und unten, Verstärkte Legierung in die Ecken. Er presst drei Zutaten zu einem Teil. Damit baust du die &6AE2-Prozessoren&r in einem Schritt: gedruckte Schaltung, Redstone und Gedrucktes Silizium. Das geht auch für die Prozessoren von Extended AE, Applied Flux, MEGA und Advanced AE.",
              "",
              "&6Planting Station&r (Pflanzstation): Stahlgehäuse in der Mitte, Elite-Schaltkreise oben und unten, Bio-Brennstoff links und rechts, Verstärkte Legierung in die Ecken. Sie zieht aus Samen und Setzlingen Ernte, mit &6Nährlösung&r (Nutrient Solution). Die macht die Auflösungskammer aus Bio-Brennstoff und Nährpaste. Die Nährpaste kommt aus dem Nährstoffverflüssiger, der Rotationskondensator macht sie zum Gas. Auch Samen von Mystical Agriculture wachsen darin.",
          ],
          tasks=[task_item("mekmm:presser", 1), task_item("mekmm:planting_station", 1)],
          rewards=[reward_item("mekanism:bio_fuel", 32), reward_table("s4_common"), reward_xp(10)],
          deps=["elite_stock"], icon="mekmm:presser"),

    quest("large", 2.75, 26, "&3Große Maschinen",
          subtitle="Robit inklusive.",
          description=[
              "MoreMachine hat für Stufe 4 außerdem Elite- und Ultimativ-Fabriken für seine eigenen Maschinen (Stamper, Walzwerk, Drehbank und mehr) und eine Reihe &6großer Maschinen&r.",
              "",
              "Alle großen Maschinen haben einen &6Robit&r in der Mitte und Stahlblöcke drumherum. Der &6Large Chemical Infuser&r (Großer Chemischer Injektor) zum Beispiel: Robit in der Mitte, zwei Ultimative Max-Chemikalientanks links und rechts, Ultimative Schaltkreise oben und unten, Stahlblöcke in die Ecken.",
              "",
              "Ebenso gibt es den Großen Elektrolyseur, den Großen Rotationskondensator, den Großen Solarneutronenaktivator sowie große Wärme-, Gas- und Windgeneratoren. Schau dir die Rezepte in JEI an, bevor du Material sammelst.",
              "",
              "&cAusnahme:&r Der Große Antiprotonische Nukleosynthetisierer und die Replikatoren kommen in Stufe 5.",
          ],
          tasks=[task_item("mekmm:large_chemical_infuser", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["presser"], icon="mekmm:large_chemical_infuser", optional=True),

    # ---- MekaSuit -------------------------------------------------------------------
    quest("mekasuit", 0, 30, "&b&lMekaSuit",
          subtitle="Netherit, aufgerüstet.",
          description=[
              "Die &6MekaSuit&r ist die Rüstung von Mekanism. Sie läuft mit Strom und wird über Module erweitert.",
              "",
              "&eRezept für jedes Teil:&r das passende Netheritteil in der Mitte, oben eine HDPE Platte, ein Ultimativer Schaltkreis, eine HDPE Platte, links und rechts HDPE Platten, unten zwei &6Polonium Pellets&r mit einer Einfachen Induktionszelle dazwischen. HDPE Platten macht die Druckreaktionskammer aus HDPE-Pellets.",
              "",
              "&6Modifikationsstation:&r HDPE Platten in die Ecken, eine Truhe oben, Ultimative Schaltkreise links und rechts, ein Stahlgehäuse in der Mitte, ein Polonium Pellet unten. Hier baust du Module in Rüstung und Werkzeug ein.",
              "",
              "&eModule:&r Alle bauen auf einem &6Basismodul&r auf (Zinn, Bronzenuggets, HDPE). Die einfachen brauchen nur Legierungen und HDPE, etwa Energie, Strahlenschutz oder Geigerzähler. Die starken wie Jetpack, Nachtsicht, Servomotor oder Magnet brauchen Polonium.",
          ],
          tasks=[task_item("mekanism:mekasuit_helmet", 1), task_item("mekanism:mekasuit_bodyarmor", 1),
                 task_item("mekanism:mekasuit_pants", 1), task_item("mekanism:mekasuit_boots", 1),
                 task_item("mekanism:modification_station", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["polonium"], icon="mekanism:mekasuit_helmet", size=1.75, shape="hexagon"),

    quest("meka_tool", 2.75, 30, "&bMeka-Werkzeug",
          subtitle="Ein Werkzeug für alles.",
          description=[
              "Das &6Meka-Werkzeug&r ist Spitzhacke, Axt, Schaufel, Hacke und Schwert in einem, betrieben mit Strom.",
              "",
              "&eRezept:&r Ultimative Schaltkreise oben links und rechts, ein Konfigurator dazwischen, HDPE Platten links und rechts, ein &6Atomic Disassembler&r in der Mitte, unten zwei Polonium Pellets mit einer Einfachen Induktionszelle dazwischen.",
              "",
              "In der Modifikationsstation bekommt es Module wie Abbaubeschleunigung, Behutsamkeit oder Glück, Aderabbau und Teleportation. Behutsamkeit, Glück und Aderabbau brauchen Polonium, das Teleportationsmodul Antimaterie aus Stufe 5.",
          ],
          tasks=[task_item("mekanism:meka_tool", 1)],
          rewards=[reward_item("mekanism:pellet_polonium", 2), reward_xp(15)],
          deps=["mekasuit"], icon="mekanism:meka_tool"),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("outlook", 5.5, 26, "&5Ausblick auf Stufe 5",
          subtitle="Was Plutonium und Antimaterie öffnen.",
          description=[
              "Einiges in Mekanism wartet noch: Der &6Spaltreaktor&r von Mekanism, das &6SPS&r und &6Antimaterie&r kommen in &eStufe 5&r, ebenso &6Plutonium&r und die Superaufgeladene Spule.",
              "",
              "&6Plutonium&r und &6Antimaterie&r stecken in den großen QIO-Laufwerken. Antimaterie braucht auch das Elytra-Modul, das Gravitationsmodul und das Teleportationsmodul der MekaSuit.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 5 will im Technik-Pfeiler &e100 Antimaterie-Pellets&r. Jedes Pellet kommt aus dem SPS, und das SPS frisst Polonium. Eine Fusionsanlage, die jetzt schon steht, liefert dann den Strom dafür.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["fusion"], icon="mekanismgenerators:fusion_reactor_frame", optional=True),

    quest("goal", 2.75, 34, "&5&lLicht des Drachen",
          subtitle="Schaltkreise für den Obelisken.",
          description=[
              "Das Obelisk-Ziel von Stufe 4 heißt &6Licht des Drachen&r. Der Technik-Pfeiler will &6150 Elite-Steuerschaltkreise&r und &61 000 Draconiumbarren&r. Im Magie-Pfeiler warten Gaia-Geister und Mystische Stäbe, und beide Pfeiler müssen voll werden.",
              "",
              "&eWas das heißt:&r Draconium aus dem End, eine Linie für Fortschrittliche Schaltkreise und eine für Verstärkte Legierung. Der Draconiumstaub, der nicht in Schaltkreise geht, wird im Ofen zu Barren und zählt dort.",
              "",
              "&eKronwerke:&r Stell eine Kiste oder ein Fass direkt an den Obelisken und leite deine Ausgabe hinein. Der Obelisk holt sich alle zwei Sekunden, was er brauchen kann, und schreibt es dir gut. Den Stand zeigt &e/kw goals&r.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 64)],
          rewards=[reward_table("s4_rare"), reward_item("mekanism:ultimate_control_circuit", 4), reward_xp(25)],
          deps=["elite_stock", "quintupling"], icon="mekanism:elite_control_circuit", size=2.5, shape="gear"),
]

images = [
    head("title", "Mekanism: Elite", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("tiers", "Elite und Ultimativ", 5, -0.6, colour="brass"),
    head("quad", "Vervierfachung", 0, 4.6, colour="magic"),
    head("quint", "Verfünffachung", 0, 9.6, colour="water"),
    head("quantum", "Quanten und QIO", 0, 14.2, colour="end"),
    head("fusion", "Fusion", 0, 18.8, colour="fire"),
    head("mekmm", "MoreMachine", 0, 24.3, colour="stone"),
    head("mekasuit", "MekaSuit", 0, 28.2, colour="water"),
    head("goal", "Das Ziel", 0, 32.1, colour="brass"),
]

chapter(C, "Mekanism: Elite", "mekanism:ultimate_control_circuit", "tech", quests, shape="square",
        order=34, stage=4,
        subtitle=["Stufe 4: Elite- und Ultimativ-Stufe, Erzvervierfachung und -verfünffachung, QIO und der Fusionsreaktor."],
        images=images)
