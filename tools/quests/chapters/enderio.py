"""Ender IO in stage 3: grains of infinity, capacitors and the void chassis, the alloy smelter
and its alloys, the stirling generator, the SAG mill, conduits, and the soul line up to the
soul binder (Malum soul stained steel, kubejs/server_scripts/kronwerke/tech.js). The farming
station is an experimental feature pack of Ender IO that the server does not enable, so it
is only explained, never asked for. End steel needs end stone and is only mentioned."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "enderio"

quests = [
    # ---- Grundlagen ----------------------------------------------------------
    quest("grains", 0, 1, "&5&lEnder IO",
          subtitle="Alles fängt mit einem Feuer an.",
          description=[
              "&5Ender IO&r ist der Mod der Legierungen, Leitungen und Seelen. Seine Maschinen sind klein, sparsam und lassen sich mit Kondensatoren aufrüsten. Mit Stufe 3 ist der ganze Mod offen.",
              "",
              "Fast jedes Teil braucht &6Körner der Ewigkeit&r, und die bekommst du nur auf eine Art: Lass ein &cFeuer&r in der Oberwelt auf &8Grundgestein&r oder &8Tiefenschiefer&r eine Weile brennen. Wenn es ausgeht, bleiben die Körner liegen.",
              "",
              "&eGrundgestein:&r 80 Prozent Chance auf ein bis drei Körner, dazu ab und zu ein &6Verdächtiger Samen&r. Der Block bleibt natürlich, du kannst immer wieder anzünden.",
              "&eTiefenschiefer:&r 40 Prozent Chance auf ein Korn, danach wird der Block zu Bruchstein.",
              "",
              "&eTipp:&r Grab dich bis ganz nach unten, leg eine Reihe Grundgestein frei und zünde alles mit einem Feuerzeug an. Bleib in der Nähe, aber nicht im Feuer.",
          ],
          tasks=[task_item("enderio:grains_of_infinity", 8)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_table("s3_common")],
          icon="enderio:grains_of_infinity", size=2.0, shape="hexagon"),

    quest("capacitor", 2.6, 0, "&eEinfacher Kondensator",
          subtitle="Ohne ihn rührt sich keine Maschine.",
          description=[
              "Jede Maschine von Ender IO hat einen &eKondensatorslot&r. Ist er leer, tut sie gar nichts und sagt dir das auch im Fenster.",
              "",
              "&eRezept:&r ein Kupferbarren in der Mitte, vier Goldnuggets an den Seiten, zwei Körner der Ewigkeit in zwei gegenüberliegenden Ecken.",
              "",
              "&eAchtung, Übersetzung:&r Im deutschen Spiel heißt dieser Gegenstand fälschlich &6Einfache Kondensatorbank&r. Gemeint ist der kleine Kondensator, die richtige Bank ist ein Block.",
              "",
              "Bessere Kondensatoren machen eine Maschine schneller und geben ihr mehr Speicher. Der &6Doppelschichtkondensator&r (zwei einfache, Kohlestaub, zwei Energetische Legierungsbarren) und der &6Oktadische Kondensator&r (zwei doppelte, ein Glowsteinblock, zwei Strahlende Legierungsbarren) kommen später in diesem Kapitel in Reichweite.",
          ],
          tasks=[task_item("enderio:basic_capacitor", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 16), reward_item("minecraft:copper_ingot", 8)],
          deps=["grains"]),

    quest("chassis", 2.6, 2, "&7Gehäuse der Leere",
          subtitle="Der Rumpf der ersten Maschinen.",
          description=[
              "Das &6Gehäuse der Leere&r ist der Kern der einfachen Maschinen: vier Eisenbarren in die Ecken, vier Körner der Ewigkeit an die Seiten, die Mitte bleibt frei.",
              "",
              "Dazu brauchst du &6Unendlichkeitsbimetallzahnräder&r: ein Korn in der Mitte, vier Eisenbarren an den Seiten, vier Eisennuggets in den Ecken. Legierungsschmelze, Stirling Generator und Sägemühle wollen je zwei davon.",
              "",
              "Zwei Gehäuse und vier Zahnräder reichen für die Schmelze und den Generator.",
          ],
          tasks=[task_item("enderio:void_chassis", 2), task_item("enderio:iron_gear", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["grains"], icon="enderio:void_chassis"),

    quest("smelter", 5.2, 1, "&6&lLegierungsschmelze",
          subtitle="Drei Zutaten rein, ein Barren raus.",
          description=[
              "Die &6Legierungsschmelze&r ist die wichtigste Maschine von Ender IO. &eRezept:&r oben Zahnrad, Ofen, Zahnrad, in der Mitte Ofen, Gehäuse der Leere, Ofen, unten Eisenbarren, Obsidian, Eisenbarren.",
              "",
              "Sie hat drei Eingangsslots und legiert daraus die Metalle des Mods. Oben im Fenster stellst du den &eModus&r ein: Legieren und Schmelzen, nur Legieren oder nur Schmelzen. Im Schmelzmodus ist sie ein elektrischer Ofen.",
              "",
              "Vergiss den &eKondensator&r nicht. Strom bekommt sie vom Stirling Generator, Ender IO rechnet in µI, und das ist dasselbe wie FE.",
              "",
              "&eKronwerke:&r Die Schmelze macht aus einem Eisenbarren und einem &6Kohlestaub&r einen &6Stahlbarren&r. Der zählt am Obelisken wie jeder andere Stahl für das Ziel &6Der Ofen schläft nie&r. Kohlestaub kommt aus der Sägemühle.",
          ],
          tasks=[task_item("enderio:alloy_smelter", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["capacitor", "chassis"], icon="enderio:alloy_smelter", size=2.0, shape="gear"),

    quest("stirling", 2.6, 4, "&cStirling Generator",
          subtitle="Strom aus allem, was brennt.",
          description=[
              "Der &6Stirling Generator&r verbrennt alles, was auch im Ofen brennt, und macht daraus Strom. &eRezept:&r oben Zahnrad, Ofen, Zahnrad, in der Mitte Eisenbarren, Gehäuse der Leere, Eisenbarren, unten Obsidian, Tiefenschiefer, Obsidian.",
              "",
              "Auch er braucht einen Kondensator. Mit einem besseren holt er mehr aus jedem Stück Brennstoff heraus.",
              "",
              "Stell ihn direkt an die Legierungsschmelze, dann fließt der Strom ohne Leitung hinüber. Für mehr als zwei Maschinen lohnt sich eine &6Einfache Kondensatorbank&r als Puffer (Eisen in die Ecken, vier Kondensatoren an die Seiten, ein Redstoneblock in die Mitte). Sie speichert eine halbe Million µI.",
          ],
          tasks=[task_item("enderio:stirling_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(5)],
          deps=["smelter"]),

    # ---- Legierungen ---------------------------------------------------------
    quest("conductive", 8, -0.6, "&cLeitfähige Legierung",
          subtitle="Eisen und Kupfer, das Rückgrat jeder Leitung.",
          description=[
              "Ein &6Eisenbarren&r und ein &6Kupferbarren&r ergeben in der Schmelze zwei &6Leitfähige Legierungsbarren&r.",
              "",
              "Daraus werden Energieleitungen, und als Zutat steckt die Legierung in Gegenstands- und Flüssigkeitsleitungen und in der Energetischen Legierung. Ein Stapel ist schnell verbraucht.",
              "",
              img(item_texture("enderio:conductive_alloy_ingot"), 32, 32),
          ],
          tasks=[task_item("enderio:conductive_alloy_ingot", 16)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_item("minecraft:iron_ingot", 8)],
          deps=["smelter"]),

    quest("energetic", 10.6, -1.4, "&6Energetisch und Strahlend",
          subtitle="Die beiden Legierungen für Fortgeschrittene.",
          description=[
              "&eEnergetische Legierung:&r Redstone, ein Leitfähiger Legierungsbarren und ein Goldbarren ergeben zwei Barren. Sie steckt im &6Energetisierten Bimetallzahnrad&r, im Doppelschichtkondensator und in den schnelleren Leitungen.",
              "",
              "&eStrahlende Legierung:&r ein Energetischer Legierungsbarren, eine Enderperle und Glowsteinstaub ergeben zwei Barren. Aus ihren Nuggets und einem Smaragd wird der &6Strahlende Kristall&r.",
              "",
              "Das Zahnrad (Energetische Legierung um ein Unendlichkeitszahnrad) brauchst du für die Seelenmaschinen weiter rechts.",
          ],
          tasks=[task_item("enderio:energetic_alloy_ingot", 8), task_item("enderio:vibrant_alloy_ingot", 4)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_item("minecraft:gold_ingot", 8)],
          deps=["conductive"], icon="enderio:energetic_alloy_ingot"),

    quest("pulsating", 10.6, 0.2, "&bPulsierende Legierung",
          subtitle="Eisen mit einer Prise Ende.",
          description=[
              "Ein &6Eisenbarren&r und eine &6Enderperle&r ergeben zwei &6Pulsierende Legierungsbarren&r.",
              "",
              "Pulsierende Legierung ist die Mitte jeder &6Gegenstandsleitung&r. Acht Nuggets um einen Diamanten ergeben den &6Pulsierenden Kristall&r, den du für Vakuumkiste und Reiseanker brauchst.",
              "",
              "Daneben gibt es die &6Redstone-Legierung&r (Redstone und Kupfer), aus der Redstone-Leitungen und das Lackiergerät gebaut werden.",
          ],
          tasks=[task_item("enderio:pulsating_alloy_ingot", 8)],
          rewards=[reward_item("minecraft:ender_pearl", 4)],
          deps=["conductive"]),

    quest("dark_steel", 8, 1, "&8Dunkelstahl",
          subtitle="Eisen, Kohle und Obsidian.",
          description=[
              "Ein &6Eisenbarren&r, ein &6Kohlestaub&r und ein &6Obsidian&r ergeben zwei &6Dunkelstahlbarren&r. Hast du keinen Staub, gehen auch zwei normale Kohle statt des Staubs.",
              "",
              "Dunkelstahl ist hart und explosionsfest. Daraus werden Leitern, Türen, Gitter, das Schwert &6Der Ender&r (es lässt Mobs manchmal ihren Kopf fallen) und der &6Stab des Reisenden&r.",
              "",
              "&cAusblick:&r &6Endstahl&r braucht zusätzlich Endstein. Den gibt es erst, wenn das Ende offen ist, das kommt in Stufe 4.",
          ],
          tasks=[task_item("enderio:dark_steel_ingot", 8)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(5)],
          deps=["smelter"]),

    # ---- Mahlen und Leiten ---------------------------------------------------
    quest("sag_mill", 5.2, 7.8, "&7&lSägemühle",
          subtitle="Mehr Staub aus jedem Erz.",
          description=[
              "Die &6SAG Mill&r heißt im deutschen Spiel &6Sägemühle&r, sie mahlt aber, statt zu sägen. &eRezept:&r oben Zahnrad, Feuerstein, Zahnrad, in der Mitte Eisenbarren, Gehäuse der Leere, Eisenbarren, unten Obsidian, Kolben, Obsidian.",
              "",
              "&eWas sie kann:&r Ein &6Rohes Eisen&r wird zu einem Pulverisierten Eisen und mit 80 Prozent Chance zu einem zweiten, im Schnitt also fast zwei Barren statt einem. Ein Erzblock wird zu einem Rohen Erz und mit einem Drittel Chance zu einem zweiten. Kohle wird zu &6Pulverisierter Kohle&r, Sand mit 50 Prozent Chance zu &6Silikon&r.",
              "",
              "&eMahlkugeln:&r Fünf Barren als Plus gelegt ergeben 24 Mahlkugeln. Eine Kugel im eigenen Slot ändert Hauptausgabe, Bonus und Stromverbrauch und nutzt sich dabei ab. Der Tooltip jeder Kugel zeigt ihre Werte.",
              "",
              "&eKronwerke:&r Mehr Eisen aus jedem Erz heißt mehr Stahl für das Ziel von Stufe 3, und die Pulverisierte Kohle geht direkt in die Legierungsschmelze oder in die Infusionsanlage von Mekanism.",
          ],
          tasks=[task_item("enderio:sag_mill", 1), task_item("enderio:silicon", 8)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["smelter"], icon="enderio:sag_mill", size=1.75, shape="hexagon"),

    quest("binder", 7.8, 7, "&7Leitungsbindemittel",
          subtitle="Kies, Sand und Ton.",
          description=[
              "Jede Leitung besteht zu zwei Dritteln aus &6Leitungsbindemittel&r. Zuerst baust du den &6Leitungsbinder-Verbundstoff&r: Kies in die Ecken und die Mitte, Ton oben und unten, Sand links und rechts. Das ergibt acht Stück.",
              "",
              "Schmilz den Verbundstoff im Ofen oder in der Schmelze. Jedes Stück wird zu &6zwei Bindemitteln&r.",
          ],
          tasks=[task_item("enderio:conduit_binder", 16)],
          rewards=[reward_item("minecraft:gravel", 32), reward_item("minecraft:clay_ball", 16)],
          deps=["smelter"]),

    quest("conduits", 10.4, 7.8, "&9&lLeitungen",
          subtitle="Strom, Gegenstände und Flüssigkeiten in einem Block.",
          description=[
              "Sechs Bindemittel oben und unten, drei Barren in die Mitte: das ergibt acht Leitungen. Welche, hängt von der mittleren Reihe ab:",
              "&eEnergieleitung:&r drei Leitfähige Legierungen.",
              "&eGegenstandsleitung:&r Leitfähig, Pulsierend, Leitfähig.",
              "&eFlüssigkeitsleitung:&r Leitfähig, Klares Glas, Leitfähig. Klares Glas macht die Schmelze aus normalem Glas.",
              "&eRedstone-Leitung:&r drei Redstone-Legierungen.",
              "Für Energie, Gegenstände und Flüssigkeiten gibt es mit Energetischer Legierung eine schnellere Stufe.",
              "",
              "Das Beste: Verschiedene Leitungen teilen sich &eeinen Block&r. Ein Strang kann Strom, Gegenstände und Wasser gleichzeitig tragen, ohne dass sie sich mischen.",
              "",
              "Rechtsklick auf eine Verbindung zu einer Maschine öffnet ihre Einstellungen: ob dort eingefügt, herausgezogen oder beides wird, und welcher &6Filter&r gilt. Ein &6Einfacher Itemfilter&r ist ein Trichter mit vier Papier, im Schleichen benutzt stellst du ihn ein. Der &6Yeta-Schraubenschlüssel&r (drei Kupferbarren und ein Korn) ist das Werkzeug von Ender IO für Maschinen und Leitungen.",
          ],
          tasks=[task_item("enderio:conduit", 16), task_item("enderio:yeta_wrench", 1)],
          rewards=[reward_item("enderio:conduit_binder", 16), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["binder"], icon="enderio:conduit_binder", size=1.75, shape="gear"),

    quest("fluids", 13, 7, "&bTanks und Flüssigkeiten",
          subtitle="Wo das Wasser wartet.",
          description=[
              "Der &6Flüssigkeitsbehälter&r von Ender IO ist einfach: Eisen in die Ecken, Eisengitter an die Seiten, Glas in die Mitte.",
              "",
              "Im Fenster des Tanks kannst du Eimer und Flaschen füllen und leeren. Eine Flüssigkeitsleitung an der Tankseite pumpt heraus, wenn du die Verbindung auf Herausziehen stellst.",
              "",
              "Wer viel Wasser braucht, baut den &6Abfluss&r: Er saugt Flüssigkeit aus der Welt unter sich ab, er braucht also einen Quellblock darunter.",
          ],
          tasks=[task_item("enderio:fluid_tank", 1)],
          rewards=[reward_item("minecraft:bucket", 4)],
          deps=["conduits"]),

    # ---- Seelen --------------------------------------------------------------
    quest("soularium", 8, 2.6, "&6Soularium",
          subtitle="Gold, getränkt in Seelensand.",
          description=[
              "Ein &6Seelensand&r oder &6Seelenerde&r aus dem Nether und ein &6Goldbarren&r ergeben in der Schmelze einen &6Soulariumbarren&r.",
              "",
              "Soularium ist das Metall der Seelenmaschinen: Seelenampulle, Seelenkette, Versiegeltes Gerüst, Schlitz'und'Spleiß. Ein Ausflug ins Seelensandtal deckt dich für lange Zeit ein.",
          ],
          tasks=[task_item("enderio:soularium_ingot", 16)],
          rewards=[reward_item("minecraft:soul_sand", 32), reward_item("minecraft:gold_ingot", 8)],
          deps=["smelter"]),

    quest("vial", 10.6, 2.6, "&dSeelenampulle",
          subtitle="Ein Mob passt in eine Flasche.",
          description=[
              "Vier &6Netherquarz&r ergeben in der Schmelze ein &6Quarzglas&r. Drei Quarzglas als Schale und ein Soulariumbarren obendrauf ergeben die &6Seelenampulle&r.",
              "",
              "Rechtsklick auf einen Mob steckt ihn in die Ampulle, Rechtsklick auf den Boden lässt ihn wieder frei. Spieler und Bosse lassen sich nicht einfangen.",
              "",
              "Eine Ampulle mit Seele brauchst du für den Seelenbinder. Für dessen Rezept selbst brauchst du eine &eleere&r.",
          ],
          tasks=[task_item("enderio:soul_vial", 2)],
          rewards=[reward_item("minecraft:quartz", 16)],
          deps=["soularium"]),

    quest("ens_chassis", 10.6, 4.2, "&5Versiegeltes Gerüst",
          subtitle="Das Gehäuse für Maschinen mit Seele.",
          description=[
              "Das &6Ensouled Chassis&r heißt im deutschen Spiel &6Versiegeltes Gerüst&r. &eRezept:&r vier Seelenketten in die Ecken, vier Soulariumbarren an die Seiten, ein Netherquarz in die Mitte.",
              "",
              "Eine &6Seelenkette&r baust du aus einem Soulariumbarren, zwei Soulariumnuggets und zwei Quarzstaub, das ergibt zwei Ketten. Quarzstaub macht die Sägemühle.",
              "",
              "Schlitz'und'Spleiß, Seelenbinder, Seelenmotor und EP-Obelisk brauchen je ein Gerüst.",
          ],
          tasks=[task_item("enderio:ensouled_chassis", 2)],
          rewards=[reward_item("enderio:soularium_ingot", 4)],
          deps=["soularium"]),

    quest("slicer", 13.2, 4.2, "&cSchlitz'und'Spleiß",
          subtitle="Köpfe, Silikon und Soularium.",
          description=[
              "&eRezept:&r oben Soularium, ein Mobkopf, Soularium, in der Mitte Soularium, Versiegeltes Gerüst, Soularium, unten Energetisiertes Zahnrad, Eisengitter, Energetisiertes Zahnrad.",
              "",
              "Die Maschine braucht in ihren Werkzeugslots eine &6Axt&r und eine &6Schere&r. Sie schneidet aus sechs Zutaten ein Bauteil zusammen.",
              "",
              "Das wichtigste davon ist der &6Z-Logic Regler&r: oben Soularium, ein &6Zombiekopf&r, Soularium, unten Silikon, Redstone, Silikon. Zombieköpfe gibt es, wenn ein geladener Creeper einen Zombie erwischt, oder mit etwas Glück vom Schwert &6Der Ender&r.",
          ],
          tasks=[task_item("enderio:slice_and_splice", 1), task_item("enderio:z_logic_controller", 1)],
          rewards=[reward_item("enderio:energized_gear", 2), reward_xp(10)],
          deps=["ens_chassis"], icon="enderio:slice_and_splice"),

    quest("malum", 13.2, 2.6, "&5Seelenbefleckter Stahl",
          subtitle="Der Seelenbinder will Malum.",
          description=[
              "&eRezept auf Kronwerke:&r Der Seelenbinder bekommt statt Soularium vier &6Soulstained Steel Ingots&r aus &5Malum&r. Die Seelenseite von Ender IO läuft hier über Malum.",
              "",
              "Den Barren macht der &6Spirit Altar&r von Malum per Geistinfusion: ein Eisenbarren in der Mitte, vier &6Refined Soulstone&r als Beigabe, dazu drei &cWicked&r, ein &2Earthen&r und ein &dArcane Spirit&r. Geister bekommst du, wenn du Mobs mit einer Sense von Malum tötest.",
              "",
              "Kein Malum-Spieler in der Nähe? Frag im Chat. Vier Barren gegen einen Stapel Leitungen ist ein fairer Handel.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 4)],
          rewards=[reward_item("enderio:soularium_ingot", 4), reward_xp(5)],
          deps=["vial"], icon="malum:soul_stained_steel_ingot"),

    quest("soul_binder", 15.8, 3.4, "&5&lSeelenbinder",
          subtitle="Eine Seele, ein Gegenstand, ein Ergebnis.",
          description=[
              "&eRezept auf Kronwerke:&r oben Soulstained Steel, eine &eleere&r Seelenampulle, Soulstained Steel, in der Mitte Energetisiertes Zahnrad, Versiegeltes Gerüst, Energetisiertes Zahnrad, unten Soulstained Steel, Z-Logic Regler, Soulstained Steel.",
              "",
              "Der &6Seelenbinder&r nimmt eine gefüllte Seelenampulle und einen Gegenstand und bindet die Seele daran. Er braucht Strom und &aErfahrung als Flüssigkeit&r in seinem Tank. EP-Saft aus Ender IO passt, ebenso die &6Essenz&r aus Industrial Foregoing. JEI zeigt pro Rezept, wie viel Erfahrung es kostet.",
              "",
              "&eWas er macht:&r Ein Zombie im Z-Logic Regler wird zu &6Frank'N'Zombie&r, ein Dorfbewohner in einem Smaragd zum &6Verlockenden Kristall&r, ein Enderman im Strahlenden Kristall zum &6Enderkristall&r. Ein &6Kaputter Spawner&r (er fällt, wenn du einen Spawner abbaust) nimmt jede Seele auf und wird zum Herz des &6Energiebetriebenen Spawners&r.",
              "",
              "&eKronwerke:&r Der Seelenmotor, mit der Seele eines Lohe gebunden, verbrennt Lava zu Strom. Eine Lavaquelle aus dem Nether hält damit eine ganze Stahlstraße am Laufen.",
          ],
          tasks=[task_item("enderio:soul_binder", 1)],
          rewards=[reward_table("s3_rare"), reward_item("enderio:soul_vial", 2), reward_xp(20)],
          deps=["slicer", "malum"], icon="enderio:soul_binder", size=2.5, shape="gear"),

    quest("farming", 18.6, 4.4, "&2Die Ackerbaustation",
          subtitle="Warum es sie hier nicht gibt.",
          description=[
              "In JEI siehst du vielleicht die &6Ackerbaustation&r. Ender IO liefert sie in der aktuellen Version nur als &cexperimentelles Datenpaket&r mit, das ausdrücklich als unfertig markiert ist. Auf Kronwerke ist dieses Paket nicht aktiv, die Station lässt sich also weder bauen noch aufstellen.",
              "",
              "Felder und Bäume automatisierst du stattdessen mit &6Industrial Foregoing&r (Sämaschine, Erntemaschine, Düngemaschine) oder mit dem &6Baumschneider&r und dem Dünger Block von &6Oritech&r. Beide Kapitel findest du gleich neben diesem.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["soul_binder"], icon="minecraft:wheat", optional=True),
]

images = [
    banner("enderio/title", "Ender IO", 8, -4.4, height=1.75, kind="title", colour="end"),
    banner("enderio/basics", "Grundlagen", 2.6, -1.5, height=0.9, colour="stone"),
    banner("enderio/alloys", "Legierungen", 9.3, -2.8, height=0.9, colour="brass"),
    banner("enderio/souls", "Seelen", 13.6, 1.1, height=0.9, colour="magic"),
    banner("enderio/conduits", "Mahlen und Leiten", 9.1, 5.6, height=0.9, colour="water"),
]

chapter(C, "Ender IO", "enderio:alloy_smelter", "tech", quests, shape="square", order=21, stage=3,
        subtitle=["Stufe 3: Legierungen, Sägemühle, Leitungen und die Seelenmaschinen."], images=images)
