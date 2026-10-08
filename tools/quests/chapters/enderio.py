"""Ender IO in stage 3: grains of infinity, the basic capacitor, infinity gear and void chassis,
the alloy smelter and stirling generator, the three capacitor tiers and the capacitor bank, the
alloys as a checklist (conductive, redstone, energetic, vibrant, pulsating, dark steel, Oritech
steel, fused quartz), the SAG mill and grinding balls, conduit binder, conduits (one item id,
the type is a component, so one task), filters, the fluid tank, the soul line (soularium, soul
vial, ensouled chassis, slice'n'splice, Malum soul stained steel, soul binder, soul binding),
the enchanter and the vacuum chest. The farming station is an experimental datapack of Ender IO
that the server does not enable, so it is only explained. End steel needs end stone (stage 4)
and is only named. Recipes from the Ender IO 8.2.12 jar, numbers from config/enderio/;
Kronwerke recipes from kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "enderio"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def alloy(name, x, y, title, subtitle, recipe, use, item, count, reward, deps=("smelter",), icon=None, section=None):
    """One alloy smelter recipe as a checklist quest."""
    return quest(name, x, y, title, subtitle=subtitle, description=[recipe, "", use],
                 tasks=[task_item(item, count)], rewards=reward, deps=list(deps), icon=icon or item, section=section)


quests = [
    # ---- Grundlagen ----------------------------------------------------------
    quest("grains", 0, 1, "&5&lBrenn Grundgestein an",
          subtitle="Körner der Ewigkeit aus einem Feuer.",
          description=[
              "Zünde in der Oberwelt ein &cFeuer&r auf &8Grundgestein&r an und lass es ausbrennen. Danach liegen &6Körner der Ewigkeit&r da: 80 Prozent Chance auf ein bis drei, dazu manchmal ein &6Verdächtiger Samen&r.",
              "",
              "Auf &8Tiefenschiefer&r gibt es mit 40 Prozent ein Korn, danach wird der Block Bruchstein. Grundgestein bleibt, du kannst es immer wieder anzünden.",
              "",
              "&5Ender IO&r öffnet mit Stufe 3: Legierungen, Leitungen in einem Block und Maschinen mit Seele. Fast jedes Teil braucht diese Körner.",
          ],
          tasks=[task_item("enderio:grains_of_infinity", 8)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_table("s3_common")],
          icon="enderio:grains_of_infinity", size=2.0, shape="hexagon"),

    quest("capacitor", 2.5, -0.5, "&eBau einen Einfachen Kondensator",
          subtitle="Ohne ihn rührt sich keine Maschine.",
          description=[
              "Ein &6Kupferbarren&r in der Mitte, vier &6Goldnuggets&r an den Seiten, zwei &6Körner&r in zwei gegenüberliegenden Ecken.",
              "",
              "Jede Ender-IO-Maschine hat einen &eKondensatorslot&r. Ist er leer, tut sie nichts und sagt das im Fenster.",
              "",
              "&eAchtung, Übersetzung:&r Im deutschen Spiel heißt das Teil fälschlich &6Einfache Kondensatorbank&r. Die echte Bank ist ein Block, weiter unten.",
          ],
          tasks=[task_item("enderio:basic_capacitor", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 16), reward_item("minecraft:copper_ingot", 8)],
          deps=["grains"]),

    quest("gear", 2.5, 1.5, "&7Bau Unendlichkeitszahnräder",
          subtitle="Zwei pro Maschine.",
          description=[
              "Ein &6Korn&r in die Mitte, vier &6Eisenbarren&r an die Seiten, vier &6Eisennuggets&r in die Ecken ergeben ein &6Unendlichkeitsbimetallzahnrad&r.",
              "",
              "Legierungsschmelze, Stirling Generator und Sägemühle wollen je zwei.",
          ],
          tasks=[task_item("enderio:iron_gear", 4)],
          rewards=[reward_item("minecraft:iron_nugget", 16)],
          deps=["grains"], icon="enderio:iron_gear"),

    quest("chassis", 5, -0.5, "&7Bau ein Gehäuse der Leere",
          subtitle="Der Rumpf der einfachen Maschinen.",
          description=[
              "Vier &6Eisenbarren&r in die Ecken, vier &6Körner&r an die Seiten, die Mitte bleibt frei.",
              "",
              "Zwei Gehäuse reichen für Schmelze und Generator.",
          ],
          tasks=[task_item("enderio:void_chassis", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["grains"], icon="enderio:void_chassis"),

    quest("smelter", 5, 1.5, "&6&lBau die Legierungsschmelze",
          subtitle="Drei Zutaten rein, ein Barren raus.",
          description=[
              "&eRezept auf Kronwerke:&r Oben Zahnrad, &6Ofen&r, Zahnrad. Mitte Ofen, &6Gehäuse der Leere&r, Ofen. Unten Eisenbarren, ein &6Messinggehäuse&r von Create, Eisenbarren. Kondensator in den Slot.",
              "",
              "Oben im Fenster wählst du den Modus: Legieren und Schmelzen, nur Legieren, nur Schmelzen. Im Schmelzmodus ist sie ein elektrischer Ofen. Sie zieht &e20 µI/t&r, µI ist dasselbe wie FE.",
          ],
          tasks=[task_item("enderio:alloy_smelter", 1)],
          rewards=[reward_item("create:brass_casing", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["capacitor", "gear", "chassis"], icon="enderio:alloy_smelter", size=2.0, shape="gear"),

    quest("stirling", 5, 4, "&cStell einen Stirling Generator auf",
          subtitle="Strom aus allem, was brennt.",
          description=[
              "Oben Zahnrad, &6Ofen&r, Zahnrad. Mitte Eisen, &6Gehäuse der Leere&r, Eisen. Unten Obsidian, &6Tiefenschiefer&r, Obsidian. Kondensator rein.",
              "",
              "Mit dem einfachen Kondensator macht er &e40 µI/t&r und puffert 64 000. Bessere Kondensatoren holen mehr aus jedem Stück Brennstoff. Stell ihn direkt an die Schmelze, dann fließt der Strom ohne Leitung.",
          ],
          tasks=[task_item("enderio:stirling_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(5)],
          deps=["smelter"]),

    quest("cap_bank", 7.5, 4, "&eBau eine Kondensatorbank",
          subtitle="Eine halbe Million µI Puffer.",
          description=[
              "Eisen in die Ecken, vier &6Einfache Kondensatoren&r an die Seiten, ein &6Redstoneblock&r in die Mitte.",
              "",
              "Die &6Einfache Kondensatorbank&r fasst &e500 000 µI&r. Mehrere nebeneinander werden ein Speicher. Fortgeschritten 2 Millionen, Strahlend 4 Millionen, beide auch als Aufrüstung der Bank darunter.",
          ],
          tasks=[task_item("enderio:basic_capacitor_bank", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_xp(5)],
          deps=["stirling"], icon="enderio:basic_capacitor_bank"),

    quest("cap_double", 10, 4, "&eBau einen Doppelschichtkondensator",
          subtitle="Die zweite Stufe für jede Maschine.",
          description=[
              "Zwei &6Einfache Kondensatoren&r links und rechts, ein &6Kohlestaub&r in die Mitte, ein &6Energetischer Legierungsbarren&r oben und unten.",
              "",
              "Im Slot macht er die Maschine schneller und gibt ihr mehr Speicher. Er steckt außerdem in der Fortgeschrittenen Kondensatorbank.",
          ],
          tasks=[task_item("enderio:double_layer_capacitor", 2)],
          rewards=[reward_item("enderio:energetic_alloy_ingot", 2), reward_xp(8)],
          deps=["cap_bank", "energetic"], icon="enderio:double_layer_capacitor"),

    quest("cap_octadic", 12.5, 3.5, "&6Bau einen Oktadischen Kondensator",
          subtitle="Die höchste gebaute Stufe.",
          description=[
              "Zwei &6Doppelschichtkondensatoren&r links und rechts, ein &6Glowsteinblock&r in die Mitte, ein &6Strahlender Legierungsbarren&r oben und unten.",
              "",
              "Der beste Kondensator, den du bauen kannst. In Truhen findest du manchmal &6Beutekondensatoren&r mit eigenen Werten, der Tooltip zeigt sie.",
          ],
          tasks=[task_item("enderio:octadic_capacitor", 1)],
          rewards=[reward_item("minecraft:glowstone", 4), reward_table("s3_common"), reward_xp(10)],
          deps=["cap_double", "vibrant"], icon="enderio:octadic_capacitor"),

    # ---- Legierungen ---------------------------------------------------------
    alloy("conductive", 8, -1, "&cLegier Leitfähige Legierung", "Eisen und Kupfer.",
          "Ein &6Eisenbarren&r und ein &6Kupferbarren&r geben zwei &6Leitfähige Legierungsbarren&r.",
          "Die Grundlage aller Leitungen und der Energetischen Legierung. Ein Stapel ist schnell weg.",
          "enderio:conductive_alloy_ingot", 16,
          [reward_item("minecraft:copper_ingot", 16)]),
    alloy("redstone_alloy", 10.5, -1, "&4Legier Redstone-Legierung", "Redstone und Kupfer.",
          "Ein &6Redstone&r und ein &6Kupferbarren&r geben einen &6Redstone-Legierungsbarren&r.",
          "Daraus werden &6Redstone-Leitungen&r, die Lackiermaschine und der Impulstrichter.",
          "enderio:redstone_alloy_ingot", 8,
          [reward_item("minecraft:redstone", 16)], section="alloys"),
    alloy("energetic", 13, -1, "&6Legier Energetische Legierung", "Redstone, Leitfähig, Gold.",
          "Ein &6Redstone&r, ein &6Leitfähiger Legierungsbarren&r und ein &6Goldbarren&r geben zwei Barren.",
          "Steckt im &6Energetisierten Bimetallzahnrad&r (Legierung um ein Unendlichkeitszahnrad), im Doppelschichtkondensator und in den schnellen Leitungen.",
          "enderio:energetic_alloy_ingot", 8,
          [reward_item("minecraft:gold_ingot", 8)], deps=("conductive",)),
    alloy("vibrant", 15.5, -1, "&aLegier Strahlende Legierung", "Energetisch, Enderperle, Glowstone.",
          "Ein &6Energetischer Legierungsbarren&r, eine &6Enderperle&r und ein &6Glowsteinstaub&r geben zwei Barren.",
          "Acht Nuggets um einen &6Smaragd&r ergeben den &6Strahlenden Kristall&r. Die Legierung trägt die schnellsten Leitungen und den Oktadischen Kondensator.",
          "enderio:vibrant_alloy_ingot", 4,
          [reward_item("minecraft:glowstone_dust", 16)], deps=("energetic",)),
    alloy("pulsating", 8, 1, "&bLegier Pulsierende Legierung", "Eisen mit einer Prise Ende.",
          "Ein &6Eisenbarren&r und eine &6Enderperle&r geben zwei &6Pulsierende Legierungsbarren&r.",
          "Die Mitte jeder Gegenstandsleitung. Acht Nuggets um einen &6Diamanten&r ergeben den &6Pulsierenden Kristall&r für Vakuumkiste und Reiseanker.",
          "enderio:pulsating_alloy_ingot", 8,
          [reward_item("minecraft:ender_pearl", 4)]),
    alloy("dark_steel", 10.5, 1, "&8Legier Dunkelstahl", "Eisen, Kohlestaub, Obsidian.",
          "Ein &6Eisenbarren&r, ein &6Kohlestaub&r und ein &6Obsidian&r geben zwei &6Dunkelstahlbarren&r. Ohne Staub gehen zwei normale Kohle.",
          "Hart und explosionsfest: Leitern, Türen, der Verzauberer und das Schwert &6Der Ender&r, das Mobs manchmal den Kopf abnimmt. &6Endstahl&r braucht Endstein und kommt in Stufe 4.",
          "enderio:dark_steel_ingot", 8,
          [reward_item("minecraft:obsidian", 8), reward_xp(3)]),
    alloy("steel_alloy", 13, 1, "&7Legier Stahl", "Eisen und Kohlestaub, ein Barren.",
          "Ein &6Eisenbarren&r und ein &6Kohlestaub&r geben einen &6Stahlbarren&r von Oritech.",
          "&eKronwerke:&r Jeder Stahlbarren zählt am Obelisken für &6Der Ofen schläft nie&r. Sägemühle für Kohlestaub davor, Kiste am Obelisken dahinter: eine kleine Stahlstraße.",
          "oritech:steel_ingot", 32,
          [reward_item("minecraft:iron_ingot", 16), reward_xp(5)], section="alloys"),
    alloy("fused_quartz", 15.5, 1, "&fSchmelz Quarzglas und Klares Glas", "Durchsichtig, und manches leuchtet.",
          "Vier &6Netherquarz&r oder ein Quarzblock geben ein &6Quarzglas&r. Ein &6Glas&r allein wird &6Klares Glas&r.",
          "Klares Glas steckt in der Flüssigkeitsleitung, Quarzglas in der Seelenampulle und den schnellen Flüssigkeitsleitungen. Mit Glowstone dazu leuchtet es, mit Amethyst wird es dunkel.",
          "enderio:fused_quartz", 8,
          [reward_item("minecraft:quartz", 16)]),

    # ---- Mahlen und Leiten ---------------------------------------------------
    quest("sag_mill", 0, 8, "&7&lBau eine Sägemühle",
          subtitle="Mehr Staub aus jedem Erz.",
          description=[
              "&eRezept auf Kronwerke:&r Oben Zahnrad, &6Feuerstein&r, Zahnrad. Mitte Eisen, &6Gehäuse der Leere&r, Eisen. Unten Obsidian, ein &6Mahlwerkrad&r von Create, Obsidian. Sie heißt &6SAG Mill&r und mahlt, statt zu sägen.",
              "",
              "Ein Rohes Eisen wird ein &6Pulverisiertes Eisen&r und mit 80 Prozent ein zweites. Kohle wird &6Pulverisierte Kohle&r, Sand mit 50 Prozent &6Silikon&r.",
              "",
              "&eKronwerke:&r Mehr Eisen aus jedem Erz heißt mehr Stahl, und die Kohle geht direkt in die Schmelze.",
          ],
          tasks=[task_item("enderio:sag_mill", 1), task_item("enderio:silicon", 8)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["smelter"], icon="enderio:sag_mill", size=1.75, shape="hexagon"),

    quest("grinding_ball", 2.5, 7, "&7Leg eine Mahlkugel ein",
          subtitle="Mehr Ausbeute, weniger Strom, oder beides.",
          description=[
              "Fünf Barren einer Legierung als Plus gelegt ergeben &e24&r Mahlkugeln. Eine Kugel kommt in den eigenen Slot der Sägemühle.",
              "",
              "Jede Sorte ändert Hauptausgabe, Bonus und Verbrauch anders und nutzt sich dabei ab. Der Tooltip der Kugel zeigt ihre Werte.",
          ],
          tasks=[task_item("enderio:conductive_alloy_grinding_ball", 24)],
          rewards=[reward_item("enderio:conductive_alloy_ingot", 5)],
          deps=["sag_mill", "conductive"], icon="enderio:conductive_alloy_grinding_ball"),

    quest("binder", 2.5, 9, "&7Mach Leitungsbindemittel",
          subtitle="Kies, Sand und Ton.",
          description=[
              "Kies in Ecken und Mitte, &6Ton&r oben und unten, &6Sand&r links und rechts: acht &6Leitungsbinder-Verbundstoff&r. Im Ofen wird jedes Stück zu &6zwei Bindemitteln&r.",
              "",
              "Jede Leitung besteht zu zwei Dritteln aus Bindemittel.",
          ],
          tasks=[task_item("enderio:conduit_binder", 32)],
          rewards=[reward_item("minecraft:gravel", 32), reward_item("minecraft:clay_ball", 16)],
          deps=["sag_mill"]),

    quest("conduits", 5, 9, "&9&lLeg Leitungen",
          subtitle="Strom, Gegenstände, Flüssigkeit in einem Block.",
          description=[
              "Bindemittel oben und unten, drei Barren in die Mitte, gibt acht. &eStrom:&r drei Leitfähige. &eGegenstände:&r Leitfähig, Pulsierend, Leitfähig. &eFlüssigkeit:&r Leitfähig, Klares Glas, Leitfähig. &eRedstone:&r drei Redstone-Legierung.",
              "",
              "Verschiedene Leitungen teilen sich &eeinen Block&r, ohne sich zu mischen. Mit Energetischer oder Strahlender Legierung gibt es schnellere Stufen. Die Werte stehen in der Checkliste &eTransport&r.",
              "",
              "&eGut zu wissen:&r Alle Sorten sind derselbe Gegenstand, die Quest zählt jede.",
          ],
          tasks=[task_item("enderio:conduit", 16)],
          rewards=[reward_item("enderio:conduit_binder", 16), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["binder", "pulsating"], icon="enderio:conduit_binder", size=1.75, shape="gear"),

    quest("filter", 7.5, 8, "&9Stell eine Verbindung ein",
          subtitle="Yeta-Schlüssel und Filter.",
          description=[
              "&6Yeta-Schraubenschlüssel:&r drei Kupferbarren und ein Korn. &6Einfacher Itemfilter:&r Trichter mit Papier, im Schleichen benutzt stellst du ihn ein.",
              "",
              "Rechtsklick auf eine Verbindung zur Maschine öffnet sie: Einfügen, Herausziehen, Kanal, Priorität, Rundlauf und ein Filterslot für jede Richtung.",
          ],
          tasks=[task_item("enderio:yeta_wrench", 1), task_item("enderio:basic_item_filter", 1)],
          rewards=[reward_item("minecraft:paper", 16)],
          deps=["conduits"], icon="enderio:yeta_wrench"),

    quest("fluids", 7.5, 10, "&bStell einen Flüssigkeitsbehälter auf",
          subtitle="Wo das Wasser wartet.",
          description=[
              "Eisen in die Ecken, &6Eisengitter&r an die Seiten, &6Glas&r in die Mitte.",
              "",
              "Im Fenster füllst und leerst du Eimer. Eine Flüssigkeitsleitung auf Herausziehen pumpt ab. Der &6Abfluss&r saugt Flüssigkeit aus einem Quellblock unter sich.",
          ],
          tasks=[task_item("enderio:fluid_tank", 1)],
          rewards=[reward_item("minecraft:bucket", 4)],
          deps=["conduits"]),

    # ---- Seelen --------------------------------------------------------------
    quest("soularium", 10.5, 7, "&6Legier Soularium",
          subtitle="Gold, getränkt in Seelensand.",
          description=[
              "Ein &6Seelensand&r oder &6Seelenerde&r und ein &6Goldbarren&r geben in der Schmelze einen &6Soulariumbarren&r.",
              "",
              "Das Metall der Seelenmaschinen: Ampulle, Seelenkette, Versiegeltes Gerüst, Schlitz'und'Spleiß. Ein Ausflug ins Seelensandtal reicht lange.",
          ],
          tasks=[task_item("enderio:soularium_ingot", 16)],
          rewards=[reward_item("minecraft:soul_sand", 32)],
          deps=["smelter"], section="souls"),

    quest("vial", 13, 6, "&dFang einen Mob in die Ampulle",
          subtitle="Ein Mob passt in eine Flasche.",
          description=[
              "Drei &6Quarzglas&r als Schale, ein &6Soulariumbarren&r oben: die &6Seelenampulle&r.",
              "",
              "Rechtsklick auf einen Mob steckt ihn hinein, Rechtsklick auf den Boden lässt ihn frei. Spieler und Bosse gehen nicht.",
          ],
          tasks=[task_item("enderio:soul_vial", 2)],
          rewards=[reward_item("minecraft:quartz", 16)],
          deps=["soularium", "fused_quartz"]),

    quest("ens_chassis", 13, 8, "&5Bau ein Versiegeltes Gerüst",
          subtitle="Das Gehäuse für Maschinen mit Seele.",
          description=[
              "Vier &6Seelenketten&r in die Ecken, vier &6Soulariumbarren&r an die Seiten, ein &6Netherquarz&r in die Mitte. Seelenkette: ein Soularium, zwei Soulariumnuggets, zwei Quarzstaub, gibt zwei.",
              "",
              "Schlitz'und'Spleiß, Seelenbinder, Seelenmotor und EP-Obelisk brauchen je eins.",
          ],
          tasks=[task_item("enderio:ensouled_chassis", 2)],
          rewards=[reward_item("enderio:soularium_ingot", 4)],
          deps=["soularium"]),

    quest("slicer", 15.5, 8, "&cBau Schlitz'und'Spleiß",
          subtitle="Köpfe, Silikon und Soularium.",
          description=[
              "Oben Soularium, ein &6Mobkopf&r, Soularium. Mitte Soularium, &6Versiegeltes Gerüst&r, Soularium. Unten &6Energetisiertes Zahnrad&r, Eisengitter, Energetisiertes Zahnrad. In die Werkzeugslots eine &6Axt&r und eine &6Schere&r.",
              "",
              "&6Z-Logic Regler:&r Soularium, &6Zombiekopf&r, Soularium, unten Silikon, Redstone, Silikon. Zombieköpfe gibt es vom geladenen Creeper oder vom Schwert Der Ender.",
          ],
          tasks=[task_item("enderio:slice_and_splice", 1), task_item("enderio:z_logic_controller", 1)],
          rewards=[reward_item("enderio:energized_gear", 2), reward_xp(10)],
          deps=["ens_chassis", "energetic"], icon="enderio:slice_and_splice"),

    quest("malum", 15.5, 6, "&5Hol Soul Stained Steel",
          subtitle="Der Seelenbinder will Malum.",
          description=[
              "&eRezept auf Kronwerke:&r Der Seelenbinder braucht vier &6Soul Stained Steel&r aus &5Malum&r statt Soularium. Die Seelenseite von Ender IO läuft über Malum.",
              "",
              "Spirit Altar: ein Eisenbarren, vier Refined Soulstone, drei &cWicked&r, ein &2Earthen&r, ein &dArcane Spirit&r. Siehe Kapitel &5Malum&r.",
              "",
              "Kein Malum-Spieler in der Nähe? Frag im Chat. Vier Barren gegen einen Stapel Leitungen ist ein fairer Handel.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 4)],
          rewards=[reward_item("enderio:soularium_ingot", 4), reward_xp(5)],
          deps=["vial"], icon="malum:soul_stained_steel_ingot"),

    quest("soul_binder", 18.5, 7, "&5&lBau den Seelenbinder",
          subtitle="Eine Seele, ein Gegenstand, ein Ergebnis.",
          description=[
              "&eRezept auf Kronwerke:&r oben Soul Stained Steel, eine &eleere&r Seelenampulle, Soul Stained Steel. Mitte Energetisiertes Zahnrad, Versiegeltes Gerüst, Energetisiertes Zahnrad. Unten Soul Stained Steel, Z-Logic Regler, Soul Stained Steel.",
              "",
              "Er bindet die Seele aus einer vollen Ampulle an einen Gegenstand. Dafür braucht er Strom und &aflüssige Erfahrung&r im Tank: EP-Saft aus Ender IO oder Essenz aus Industrial Foregoing.",
              "",
              "&eKronwerke:&r Der Seelenmotor mit der Seele einer Lohe verbrennt Lava zu Strom, &e800 µI&r je mB.",
          ],
          tasks=[task_item("enderio:soul_binder", 1)],
          rewards=[reward_table("s3_rare"), reward_item("enderio:soul_vial", 2), reward_xp(20)],
          deps=["slicer", "malum"], icon="enderio:soul_binder", size=2.5, shape="gear"),

    quest("soul_binding", 21, 7, "&dBinde deine erste Seele",
          subtitle="Frank'N'Zombie und seine Freunde.",
          description=[
              "&6Zombie&r in einen Z-Logic Regler gibt &6Frank'N'Zombie&r. &6Dorfbewohner&r in einen Smaragd gibt den &6Verlockenden Kristall&r. &6Enderman&r in einen Strahlenden Kristall gibt den &6Enderkristall&r für den Stab des Reisenden.",
              "",
              "Ein &6Kaputter Spawner&r (fällt beim Abbau eines Spawners) nimmt jede Seele und wird Herz des &6Energiebetriebenen Spawners&r.",
              "",
              "&eKronwerke:&r Ein Dubioser Behälter aus Oritech mit der Seele eines Allays, Phantoms oder Plagegeists wird &6Unheilige Intelligenz&r, die Oritech für späte Addons braucht.",
          ],
          tasks=[task_item("enderio:frank_n_zombie", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(10)],
          deps=["soul_binder"], icon="enderio:frank_n_zombie"),

    # ---- Nützliches ----------------------------------------------------------
    quest("enchanter", 10.5, 12, "&dBau den Verzauberer",
          subtitle="Bücher nach Rezept statt nach Glück.",
          description=[
              "Ein &6Buch&r oben, &6Diamant&r, &6Lesepult&r, Diamant in der Mitte, drei &6Dunkelstahl&r unten.",
              "",
              "Leg ein Buch, eine Zutat und Lapis hinein und zahl Erfahrungsstufen: heraus kommt ein Verzaubertes Buch. Redstone gibt Effizienz, Schleim Behutsamkeit, Smaragd Glück, Obsidian Haltbarkeit. Mehr Zutat heißt höhere Stufe, JEI zeigt die Mengen.",
          ],
          tasks=[task_item("enderio:enchanter", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 32), reward_xp(10)],
          deps=["dark_steel"], icon="enderio:enchanter", section="useful"),

    quest("vacuum_chest", 13, 12, "&9Stell eine Vakuumkiste auf",
          subtitle="Herumliegendes landet von selbst darin.",
          description=[
              "Sieben &6Eisenbarren&r um eine &6Truhe&r, unten in der Mitte ein &6Pulsierender Kristall&r.",
              "",
              "Sie saugt Gegenstände in ihrer Nähe ein. Die Reichweite stellst du im Fenster ein und lässt sie dir anzeigen. Gut unter einer Mobfarm oder am Ende einer Erntemaschine.",
          ],
          tasks=[task_item("enderio:vacuum_chest", 1)],
          rewards=[reward_item("minecraft:hopper", 2)],
          deps=["pulsating"], icon="enderio:vacuum_chest"),

    quest("farming", 15.5, 12, "&2Lies: Die Ackerbaustation",
          subtitle="Warum es sie hier nicht gibt.",
          description=[
              "In JEI siehst du vielleicht die &6Ackerbaustation&r. Ender IO liefert sie in dieser Version nur als &cexperimentelles Datenpaket&r, das als unfertig markiert ist. Auf Kronwerke ist es nicht aktiv, die Station geht weder zu bauen noch aufzustellen.",
              "",
              "Felder automatisierst du mit &6Industrial Foregoing&r oder dem Zerstörer mit Ernte-Filter von &6Oritech&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["smelter"], icon="minecraft:wheat", optional=True, section="useful"),

    # ---- neue Quests: Kondensatoren --------------------------------------------
    quest("solar", 15, 3.5, "&eBau Fotovoltaikmodule",
          subtitle="Strom aus Sonnenlicht, ohne Brennstoff.",
          description=[
              "&6Pulverisiertes Lapislazuli&r, &6Pulverisierte Kohle&r und &6Silikon&r formlos ergeben einen &6Fotovoltaik Verbundstoff&r. Zwei davon in der Legierungsschmelze ergeben eine &6Fotovoltaikplatte&r. Staub und Silikon liefert die Sägemühle.",
              "",
              "&6Energetisches Fotovoltaikmodul:&r Gold, Glas, Gold oben, drei Fotovoltaikplatten in der Mitte, Einfacher Kondensator, Redstone, Einfacher Kondensator unten.",
              "",
              "Es liefert bei Tageslicht bis zu &d4 µI/t&r und braucht freie Sicht zum Himmel. Wenig, aber für immer und ohne Wartung. Gut, um eine Kondensatorbank tagsüber nachzufüllen.",
          ],
          tasks=[task_item("enderio:energetic_photovoltaic_module", 2)],
          rewards=[reward_item("enderio:silicon", 8), reward_xp(10)],
          deps=["cap_bank", "sag_mill"], icon="enderio:energetic_photovoltaic_module"),

    quest("solar_pulsating", 17.5, 3.5, "&bRüste auf Pulsierende Fotovoltaik auf",
          subtitle="Viermal so viel Sonne.",
          description=[
              "Pulsierende Legierung, &6Erleuchtetes Quarzglas&r, Pulsierende Legierung oben, Fotovoltaikplatte, &6Pulverisierte Kohle&r, Fotovoltaikplatte in der Mitte, &6Doppelschichtkondensator&r, ein &6Energetisches Fotovoltaikmodul&r, Doppelschichtkondensator unten.",
              "",
              "Es liefert bei Tageslicht bis zu &d16 µI/t&r. Das &6Strahlende Fotovoltaikmodul&r als nächste Stufe schafft &d64 µI/t&r.",
              "",
              "Erleuchtetes Quarzglas schmilzt du in der Legierungsschmelze aus Quarzglas und einem Glowsteinblock oder vier Glowsteinstaub.",
          ],
          tasks=[task_item("enderio:pulsating_photovoltaic_module", 1)],
          rewards=[reward_item("enderio:pulsating_alloy_ingot", 4), reward_xp(10)],
          deps=["solar", "cap_double", "pulsating"], icon="enderio:pulsating_photovoltaic_module", optional=True),

    # ---- neue Quests: Mahlen und Leiten ----------------------------------------
    quest("painting", 0, 10, "&9Versteck deine Leitungen",
          subtitle="Lackiergerät und Leitungs-Fassade.",
          description=[
              "&6Lackiergerät:&r roter, grüner und blauer Farbstoff oben, Leitfähige Legierung, &6Gehäuse der Leere&r, Leitfähige Legierung in der Mitte, Zahnrad, Redstone-Legierung, Zahnrad unten. &6Leitungs-Fassade:&r acht Bindemittel im Kreis.",
              "",
              "Leg die Fassade und einen beliebigen Block ins Lackiergerät: die Fassade nimmt dessen Aussehen an, für &d2 400 µI&r. Rechtsklick damit auf eine Leitung verkleidet sie.",
              "",
              "So verschwinden deine Leitungen in Wand und Boden und laufen trotzdem weiter. Der Yeta-Schraubenschlüssel kommt weiter an sie heran.",
          ],
          tasks=[task_item("enderio:painting_machine", 1), task_item("enderio:conduit_facade", 4)],
          rewards=[reward_item("enderio:conduit_binder", 16), reward_xp(5)],
          deps=["conduits"], icon="enderio:painting_machine", optional=True),

    # ---- neue Quests: Seelen ---------------------------------------------------
    quest("xp_obelisk", 18.5, 9, "&aSpeicher Erfahrung im EP-Obelisken",
          subtitle="Deine Level auf Vorrat, verlustfrei.",
          description=[
              "&6Erfahrungsstab:&r zwei Soularium, zwei &6Verdächtige Samen&r und ein Strahlender Legierungsbarren. Der Stab oben, ein Soularium darunter, Soularium, &6Versiegeltes Gerüst&r, Soularium unten ergeben den &6EP-Obelisken&r.",
              "",
              "Im Fenster legst du 1, 10 oder alle Level ab und holst sie genauso wieder. Er speichert sie als flüssige Erfahrung, die auch der Seelenbinder trinkt.",
              "",
              "Verdächtige Samen fallen manchmal, wenn du Grundgestein für Körner der Ewigkeit anzündest.",
          ],
          tasks=[task_item("enderio:xp_obelisk", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(15)],
          deps=["ens_chassis", "vibrant"], icon="enderio:xp_obelisk"),

    quest("powered_spawner", 21, 9, "&cBau einen Energiebetriebenen Spawner",
          subtitle="Ein Spawner, der mit Strom läuft.",
          description=[
              "Soularium, &6Kaputter Spawner&r, Soularium oben, Soularium, &6Versiegeltes Gerüst&r, Soularium in der Mitte, &6Strahlender Kristall&r, &6Z-Logic Regler&r, Strahlender Kristall unten. Im Seelenbinder bekommt er mit einer vollen Seelenampulle seinen Mob.",
              "",
              "Er hat zwei Modi: &eMobs spawnen&r oder &eMobs einfangen&r. Stehen zu viele Mobs oder zu viele Spawner in der Nähe, hält er an und zeigt den Grund im Fenster.",
              "",
              "Mit einer Vakuumkiste und dem Schwert Der Ender oder einem Monsterschnetzler daneben wird daraus eine Farm.",
          ],
          tasks=[task_item("enderio:powered_spawner", 1)],
          rewards=[reward_item("enderio:soularium_ingot", 4), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["soul_binder"], icon="enderio:powered_spawner", optional=True),

    quest("aversion", 23.5, 9, "&5Stell einen Abweisenden Obelisken auf",
          subtitle="Keine Monster rund um die Basis.",
          description=[
              "Ein &6Endermankopf&r oben, Energetische Legierung, Soularium, Energetische Legierung in der Mitte, Soularium, &6Versiegeltes Gerüst&r, Soularium unten. Endermanköpfe nimmt das Schwert &6Der Ender&r manchmal mit.",
              "",
              "Mit Strom, &d20 µI/t&r, verhindert er im Umkreis von &e16 Blöcken&r das Spawnen der Mobs, die du im Seelenfilter einträgst. Ohne Seelenfilter tut er nichts.",
              "",
              "&6Einfacher Seelen-Filter:&r vier Papier um eine &6Seelenampulle&r. Welche Mobs er meint, stellst du im Filter selbst ein.",
          ],
          tasks=[task_item("enderio:aversion_obelisk", 1), task_item("enderio:basic_soul_filter", 1)],
          rewards=[reward_item("enderio:soul_vial", 2), reward_xp(10)],
          deps=["vial", "ens_chassis", "energetic"], icon="enderio:aversion_obelisk", optional=True),

    # ---- neue Quests: Nützliches -----------------------------------------------
    quest("travel", 18, 12, "&dReise mit Ankern und Stab",
          subtitle="Teleport von Anker zu Anker.",
          description=[
              "&6Reiseanker:&r Eisen in die Ecken, Bindemittel an die Seiten, ein &6Pulsierender Kristall&r in die Mitte. &6Stab des Reisenden:&r zwei Dunkelstahlbarren schräg und ein &6Enderkristall&r an der Spitze. Den Enderkristall bindet der Seelenbinder aus einem Enderman und einem Strahlenden Kristall.",
              "",
              "Mit dem Stab teleportierst du dich zu einem Anker, auf den du schaust, bis &e192 Blöcke&r weit. Von Anker zu Anker sind es &e96 Blöcke&r. Ohne Anker im Blick springt der Stab bis zu &e24 Blöcke&r weit.",
              "",
              "Jeder Sprung kostet &d1 000 µI&r aus dem Stab, er speichert 100 000. Laden geht im Kabelgebundenen Ladegerät.",
          ],
          tasks=[task_item("enderio:travel_anchor", 2), task_item("enderio:staff_of_travelling", 1)],
          rewards=[reward_item("enderio:pulsating_crystal", 1), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["vacuum_chest", "soul_binding"], icon="enderio:staff_of_travelling"),

    quest("charger", 20.5, 12, "&eLad Werkzeuge am Ladegerät",
          subtitle="Volle Akkus für Stab und Co.",
          description=[
              "Acht &6Leitfähige Legierungsbarren&r um ein &6Gehäuse der Leere&r ergeben das &6Kabelgebundene Ladegerät&r. Gegenstand hinein, Strom dran, voll wieder heraus.",
              "",
              "Das &6Drahtlose Ladegerät&r (ein &6Enderresonator&r unten statt einer Legierung) lädt die Gegenstände aller Spieler im Umkreis von &e16 Blöcken&r, ohne dass du sie hineinlegst. Den Enderresonator macht Schlitz'und'Spleiß aus Endermankopf, Soularium, Silikon und Strahlender Legierung.",
          ],
          tasks=[task_item("enderio:wired_charger", 1)],
          rewards=[reward_item("enderio:conductive_alloy_ingot", 8), reward_xp(5)],
          deps=["conduits"], icon="enderio:wired_charger", section="useful"),

    quest("crafter", 23, 12, "&7Lass den Fertiger arbeiten",
          subtitle="Eine Werkbank, die allein baut.",
          description=[
              "Drei &6Silikon&r oben, Eisen, &6Gehäuse der Leere&r, Eisen in der Mitte, Zahnrad, &6Werkbank&r, Zahnrad unten ergeben den &6Fertiger&r.",
              "",
              "Im Fenster legst du ein Rezept fest. Zutaten kommen per Leitung oder Trichter hinein, das Ergebnis geht hinaus, solange Strom da ist.",
              "",
              "Ideal für Dinge, die du ständig brauchst: Leitungsbinder-Verbundstoff, Bindemittel zu Leitungen, Nuggets zu Barren.",
          ],
          tasks=[task_item("enderio:crafter", 1)],
          rewards=[reward_item("enderio:silicon", 8), reward_xp(5)],
          deps=["conduits"], icon="enderio:crafter", section="useful"),
]

images = [
    banner("enderio/title", "Ender IO", 7, -4.4, height=1.75, kind="title", colour="end"),
    banner("enderio/basics", "Grundlagen", 2.5, -2.2, height=0.9, colour="stone"),
    banner("enderio/alloys", "Legierungen", 11.75, -2.6, height=0.9, colour="brass"),
    banner("enderio/power", "Kondensatoren", 10, 2.9, height=0.7, colour="brass"),
    banner("enderio/conduits", "Mahlen und Leiten", 3.75, 5.6, height=0.9, colour="water"),
    banner("enderio/souls", "Seelen", 16.5, 4.5, height=0.9, colour="magic"),
    banner("enderio/useful", "Nützliches", 13, 10.6, height=0.9, colour="nature"),
]

chapter(C, "Ender IO", "enderio:alloy_smelter", "tech", quests, shape="square", order=21, stage=3,
        subtitle=["Stufe 3: Legierungen, Kondensatoren, Sägemühle, Leitungen und die Seelenmaschinen."], images=images)
