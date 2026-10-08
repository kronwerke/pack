"""Powah in stage 3: dielectric paste, rods and casing, capacitors, the energizing orb (Kronwerke:
mana diamond) and its rods, charged certus (Kronwerke: 2 per craft), energized steel and the
crystals up to spirited, dry ice and the ender core, every furnator tier from starter to
spirited, magmator, solar panel and thermo generator, the reactor step by step (uraninite,
blocks, fuel and cooling, upgrade), cables, wrench, energy cells, ender cells and the player
transmitter. Nitro is stage 4 and only mentioned. Numbers follow the server's
config/powah.json5 and the Powah 6.2.10 data maps; the orb recipe follows
kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "powah"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Grundlagen -----------------------------------------------------------------
    quest("welcome", 0, 1.5, "&b&lRühr Dielectric Paste an",
          subtitle="Die Grundmasse von allem in Powah.",
          description=[
              "Drei &6Kohle&r oder Holzkohle, zwei &6Ton&r und ein &6Lavaeimer&r ergeben &e24&r Paste. Mit &6Lohenstaub&r statt Lava (zwei Kohle, ein Ton, ein Lohenstaub) sind es 16, ganz ohne Eimer.",
              "",
              pic("powah:dielectric_paste"),
              "",
              "&6Powah&r öffnet mit Stufe 3. Alles kommt in Stufen: &7Starter&r, &fBasic&r, &8Hardened&r, &6Blazing&r, &bNiotic&r, &aSpirited&r. &cNitro&r kommt in Stufe 4.",
          ],
          tasks=[task_item("powah:dielectric_paste", 32)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_table("s3_common"), reward_xp(5)],
          icon="powah:dielectric_paste", size=2.0, shape="hexagon"),

    quest("casing", 2.75, 0, "&7Bau ein Dielectric Casing",
          subtitle="Das Gerippe jeder Powah-Maschine.",
          description=[
              "Paste und &6Eisengitter&r: drei Gitter in einer Spalte, Paste links und rechts, gibt acht senkrechte &6Dielectric Rods&r. Als Reihe mit Paste oben und unten gibt es acht waagerechte.",
              "",
              "&6Casing:&r Eisenbarren in die Ecken, waagerechte Stäbe oben und unten, senkrechte links und rechts, Mitte leer.",
              "",
              "Fast jeder Powah-Block hat ein Casing im Rezept. Bau gleich vier.",
          ],
          tasks=[task_item("powah:dielectric_casing", 4)],
          rewards=[reward_item("minecraft:iron_bars", 16)],
          deps=["welcome"], icon="powah:dielectric_casing"),

    quest("capacitors", 2.75, 3, "&7Bau Kondensatoren",
          subtitle="Die Stufe steckt im Kondensator.",
          description=[
              "Vier &6Eisenbarren&r, zwei Paste und ein &6Redstoneblock&r ergeben vier &6Basic Capacitors&r. Einer zerfällt an der Werkbank in zwei &6Tiny&r, zwei ergeben einen &6Large&r.",
              "",
              "Starter-Blöcke nehmen Tiny, Basic die normalen. Ab Hardened baust du je einen eigenen: ein Large in der Mitte, Paste in die Ecken, an die Seiten das Material der Stufe. Hardened und Blazing geben zwei, Niotic und Spirited einen.",
              "",
              "Eine höhere Maschine entsteht fast immer aus der Maschine darunter. Beim Aufrüsten verlierst du nichts.",
          ],
          tasks=[task_item("powah:capacitor_basic", 4), task_item("powah:capacitor_basic_tiny", 2)],
          rewards=[reward_item("minecraft:redstone_block", 4)],
          deps=["welcome"], icon="powah:capacitor_basic"),

    quest("orb", 5.5, 1.5, "&d&lBau die Energizing Orb",
          subtitle="Ohne Mana kein Strom.",
          description=[
              "&eRezept auf Kronwerke:&r oben Glas, ein &bManadiamant&r, Glas. In der Mitte Glas, &6Dielectric Casing&r, Glas. Unten drei waagerechte Dielectric Rods. Im Original sitzt oben nur Glas.",
              "",
              "Den Manadiamanten macht jeder Botaniker im Manabecken aus einem Diamanten. Kein Becken? Frag im Chat.",
              "",
              "Die Kugel lädt Gegenstände mit Strom, bis sie sich verwandeln. Öffne sie und leg die Zutaten hinein, JEI zeigt unter &eEnergizing&r alle Rezepte mit FE-Bedarf.",
          ],
          tasks=[task_item("powah:energizing_orb", 1)],
          rewards=[reward_item("botania:mana_diamond", 1), reward_table("s3_common"), reward_xp(10)],
          deps=["casing"], icon="powah:energizing_orb", size=2.0, shape="gear"),

    quest("rods", 8.25, 1.5, "&eStell Energizing Rods auf",
          subtitle="Die Stäbe bringen den Strom.",
          description=[
              "&6Energizing Rod (Starter):&r Netherquarz oben, zwei Tiny links und rechts vom Casing, ein senkrechter Dielectric Rod unten.",
              "",
              "Stell die Stäbe im Umkreis von &e4 Blöcken&r um die Kugel und gib jedem Strom von unten: Kabel, Zelle oder Generator. Arbeitet ein Stab nicht mit, verbinde ihn mit dem &6Wrench&r im Modus &eLink&r.",
              "",
              "Ein Starter-Stab schiebt &e100 FE/t&r. Mehrere Stäbe arbeiten zusammen.",
          ],
          tasks=[task_item("powah:energizing_rod_starter", 2)],
          rewards=[reward_item("powah:capacitor_basic", 4), reward_xp(5)],
          deps=["orb"], icon="powah:energizing_rod_starter"),

    quest("rod_upgrade", 8.25, 3.5, "&8Rüste die Stäbe auf",
          subtitle="Mehr FE pro Tick an der Kugel.",
          description=[
              "Jeder höhere Stab: ein &6Quarzblock&r oben, die Kondensatoren der neuen Stufe links und rechts vom Casing, unten der alte Stab.",
              "",
              "&eFE/t je Stab:&r Starter 100, Basic 400, Hardened 1 000, Blazing 4 000, Niotic 10 000, Spirited 40 000. Bei Kristallen ab 120 000 FE macht das aus Minuten Sekunden. Die Leitung zu den Stäben muss das tragen.",
          ],
          tasks=[task_item("powah:energizing_rod_basic", 2), task_item("powah:energizing_rod_hardened", 1)],
          rewards=[reward_item("minecraft:quartz_block", 4), reward_xp(5)],
          deps=["rods", "steel"], icon="powah:energizing_rod_hardened"),

    # ---- Energetisieren -------------------------------------------------------------
    quest("certus", 11, -1, "&bLade Certus-Quarz",
          subtitle="Der Einstieg in AE2, zwei auf einmal.",
          description=[
              "&eRezept auf Kronwerke:&r ein &6Certus-Quarzkristall&r und ein &6Redstone&r ergeben für &e20 000 FE&r zwei Geladene Certus-Quarzkristalle. Der Auflader von AE2 und alle anderen Wege sind entfernt.",
              "",
              "Der zweite Weg ist die Imbuement-Kammer von Ars Nouveau: 2 000 Quelle, Redstone und Glowstone auf den Sockeln, nur einer pro Durchgang.",
              "",
              "Geladener Certus ist der Anfang jedes ME-Netzwerks. Wer eine Kugel hat, nimmt den Lagerbauern viel Arbeit ab.",
          ],
          tasks=[task_item("ae2:charged_certus_quartz_crystal", 16)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 16), reward_xp(5)],
          deps=["rods"], icon="ae2:charged_certus_quartz_crystal"),

    quest("steel", 11, 1, "&7Lade Energiestahl",
          subtitle="Eisen und Gold, aufgeladen.",
          description=[
              "Ein &6Eisenbarren&r und ein &6Goldbarren&r werden für &e10 000 FE&r zwei &6Energized Steel&r.",
              "",
              pic("powah:steel_energized"),
              "",
              "Das Material der &8Hardened&r-Stufe: Kondensatoren, Kabel, Zellen, Generatoren. Mach dir einen Stapel.",
          ],
          tasks=[task_item("powah:steel_energized", 16)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:iron_ingot", 8)],
          deps=["rods"], icon="powah:steel_energized"),

    quest("blazing", 13.5, 1, "&6Lade Blazing-Kristalle",
          subtitle="Eine Lohenrute voller Strom.",
          description=[
              "Eine &6Lohenrute&r oder vier &6Lohenstaub&r ergeben für &e120 000 FE&r einen &6Blazing Crystal&r. Ein einzelner Starter-Stab braucht dafür eine Minute.",
              "",
              pic("powah:crystal_blazing"),
              "",
              "Das Material der &6Blazing&r-Stufe. Neun Kristalle ergeben einen Block, der als Wärmequelle unter dem Thermo Generator &e2 800 Grad&r hat.",
          ],
          tasks=[task_item("powah:crystal_blazing", 8)],
          rewards=[reward_item("minecraft:blaze_rod", 8), reward_xp(5)],
          deps=["steel"], icon="powah:crystal_blazing"),

    quest("niotic", 16, 1, "&bLade Niotic-Kristalle",
          subtitle="Ein Diamant, dreihunderttausend FE.",
          description=[
              "Ein &bDiamant&r ergibt für &e300 000 FE&r einen &6Niotic Crystal&r. Spätestens jetzt lohnen sich Hardened-Stäbe.",
              "",
              pic("powah:crystal_niotic"),
              "",
              "Niotic-Kondensatoren gibt es nur einen pro Rezept. Plan ein paar Diamanten mehr ein.",
          ],
          tasks=[task_item("powah:crystal_niotic", 4)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(10)],
          deps=["blazing"], icon="powah:crystal_niotic"),

    quest("spirited", 18.5, 1, "&aLade Spirited-Kristalle",
          subtitle="Das obere Ende in Stufe 3.",
          description=[
              "Ein &aSmaragd&r ergibt für &e1 000 000 FE&r einen &6Spirited Crystal&r.",
              "",
              "&cKommt in Stufe 4:&r Nitro. Ein Netherstern, zwei Redstoneblöcke und ein Blazing-Kristallblock geben für 20 Millionen FE sechzehn Nitro-Kristalle.",
          ],
          tasks=[task_item("powah:crystal_spirited", 2)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(10)],
          deps=["niotic"], icon="powah:crystal_spirited"),

    quest("rod_spirited", 21, 1, "&aBau einen Spirited-Stab",
          subtitle="40 000 FE pro Tick an der Kugel.",
          description=[
              "Der Weg geht Stufe für Stufe: ein &6Quarzblock&r oben, zwei Kondensatoren der neuen Stufe links und rechts vom Casing, unten der Stab darunter. Erst Blazing, dann Niotic, dann &aSpirited&r.",
              "",
              "Ein &6Spirited Capacitor&r sind vier Spirited-Kristalle um einen Large Capacitor, mit Paste in den Ecken. Für den Stab brauchst du zwei, also acht Smaragde und acht Millionen FE.",
              "",
              "Ein Spirited-Stab schiebt &e40 000 FE/t&r. Vier davon laden einen Spirited-Kristall in wenigen Sekunden. Die Leitung zu den Stäben muss das tragen: Blazing-Kabel schaffen 20 000 FE/t, Niotic 50 000.",
          ],
          tasks=[task_item("powah:energizing_rod_spirited", 1)],
          rewards=[reward_item("powah:crystal_spirited", 2), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["spirited", "rod_upgrade"], icon="powah:energizing_rod_spirited", optional=True),

    quest("snowball", 18.5, -1, "&bLade einen Schneeball",
          subtitle="Ein Blitz zum Werfen.",
          description=[
              "Ein &6Schneeball&r in der Energizing Orb wird für &e500 000 FE&r zum &6Charged Snowball&r.",
              "",
              "Geworfen schlägt dort, wo er auftrifft, ein &eBlitz&r ein. Damit machst du aus einem Creeper einen geladenen Creeper, aus einem Schwein einen Zombifizierten Piglin und aus einem Dorfbewohner eine Hexe, ganz ohne Gewitter.",
              "",
              "&cVorsicht:&r Der Blitz zündet, was brennen kann. Nicht im Holzhaus werfen.",
          ],
          tasks=[task_item("powah:charged_snowball", 4)],
          rewards=[reward_item("minecraft:snowball", 16), reward_xp(5)],
          deps=["blazing"], icon="powah:charged_snowball", optional=True),

    quest("dry_ice", 13.5, -1, "&bMach Trockeneis",
          subtitle="Das beste Kühlmittel für den Reaktor.",
          description=[
              "Zwei &6Blaueis&r ergeben für &e10 000 FE&r ein &6Trockeneis&r. Es liegt auch als Ader im Stein unter &eY 64&r, mit Behutsamkeit abbauen.",
              "",
              "Im Reaktor kühlt Trockeneis mit -32 Grad und 712 Einheiten. Zum Vergleich: Blaueis -17 Grad und 568, normales Eis -5 Grad und 48.",
          ],
          tasks=[task_item("powah:dry_ice", 8)],
          rewards=[reward_item("minecraft:blue_ice", 8)],
          deps=["certus"], icon="powah:dry_ice", optional=True),

    quest("ender_core", 16, -1, "&5Lade einen Ender Core",
          subtitle="Der Kern der kabellosen Zellen.",
          description=[
              "Ein &6Enderauge&r, ein &6Dielectric Casing&r und ein Tiny-Kondensator ergeben für &e50 000 FE&r einen &6Ender Core&r.",
              "",
              "Daraus baust du Ender Cells und Ender Gates, unten im Abschnitt Speichern.",
          ],
          tasks=[task_item("powah:ender_core", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 4)],
          deps=["dry_ice"], icon="powah:ender_core"),

    # ---- Strom erzeugen -------------------------------------------------------------
    quest("furnator", 0, 7.5, "&6Bau einen Furnator",
          subtitle="Kohle rein, Strom raus.",
          description=[
              "Drei Paste oben, zwei Tiny links und rechts vom Casing, unten Paste, &6Ofen&r, Paste.",
              "",
              "Jeder Brennstoff gibt &e30 FE&r pro Brennzeit-Tick, eine Kohle also 48 000 FE in jeder Stufe. Höhere Stufen verbrennen nur schneller. Der Starter macht &e20 FE/t&r.",
          ],
          tasks=[task_item("powah:furnator_starter", 1)],
          rewards=[reward_item("minecraft:coal_block", 4), reward_xp(3)],
          deps=["capacitors", "casing"], icon="powah:furnator_starter", size=1.5, shape="hexagon"),

    quest("furnator_basic", 2.5, 7.5, "&fRüste auf Basic",
          subtitle="Vierfacher Strom aus Eisen.",
          description=[
              "Drei &6Eisen&r oben, zwei Basic-Kondensatoren links und rechts vom Casing, unten Eisen, der &6Starter-Furnator&r, Eisen.",
              "",
              "Ein Basic Furnator macht &e80 FE/t&r.",
          ],
          tasks=[task_item("powah:furnator_basic", 1)],
          rewards=[reward_item("minecraft:coal_block", 6), reward_xp(4)],
          deps=["furnator"], icon="powah:furnator_basic"),

    quest("gen_tiers", 5, 7.5, "&8Rüste auf Hardened",
          subtitle="Energiestahl aus der Kugel.",
          description=[
              "Wie Basic, nur mit &6Energized Steel&r statt Eisen, zwei &6Hardened-Kondensatoren&r und dem Basic Furnator unten.",
              "",
              "Ein Hardened Furnator macht &e200 FE/t&r, zehnmal so viel wie der Starter.",
          ],
          tasks=[task_item("powah:furnator_hardened", 1)],
          rewards=[reward_item("powah:steel_energized", 8), reward_xp(5)],
          deps=["furnator_basic", "steel"], icon="powah:furnator_hardened"),

    quest("power_plant", 7.5, 7.5, "&6&lBau ein Blazing-Kraftwerk",
          subtitle="800 FE pro Tick aus Holzkohle.",
          description=[
              "&6Blazing Furnator:&r Blazing-Kristalle, Blazing-Kondensatoren, Casing und der Hardened Furnator. Dazu eine &6Blazing Energy Cell&r als Puffer.",
              "",
              "Der Blazing Furnator macht &e800 FE/t&r, vierzigmal so viel wie der Starter. Füttere ihn mit Kohleblöcken aus einer Baumfarm oder bau gleich Reaktoren.",
              "",
              "&eKronwerke:&r &6Der Ofen schläft nie&r will tausende Stahlbarren und Fortschrittliche Steuerschaltkreise. Hinter jeder Stahlstraße steht ein Kraftwerk. Übrigen Strom gibst du per Kabel an den Nachbarn.",
          ],
          tasks=[task_item("powah:furnator_blazing", 1), task_item("powah:energy_cell_blazing", 1)],
          rewards=[reward_table("s3_rare"), reward_item("powah:crystal_blazing", 8), reward_xp(20)],
          deps=["gen_tiers", "blazing", "cells"], icon="powah:furnator_blazing", size=2.0, shape="gear"),

    quest("furnator_niotic", 10, 7.5, "&bRüste auf Niotic",
          subtitle="2 000 FE pro Tick.",
          description=[
              "Niotic-Kristalle, zwei Niotic-Kondensatoren, Casing und der &6Blazing Furnator&r unten.",
              "",
              "Ein Niotic Furnator macht &e2 000 FE/t&r und puffert 2 Millionen FE.",
          ],
          tasks=[task_item("powah:furnator_niotic", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(10)],
          deps=["power_plant", "niotic"], icon="powah:furnator_niotic", optional=True),

    quest("furnator_spirited", 12.5, 7.5, "&aRüste auf Spirited",
          subtitle="8 000 FE pro Tick.",
          description=[
              "Spirited-Kristalle, zwei Spirited-Kondensatoren, Casing und der &6Niotic Furnator&r unten.",
              "",
              "Ein Spirited Furnator macht &e8 000 FE/t&r. Nitro mit 40 000 FE/t kommt in Stufe 4.",
          ],
          tasks=[task_item("powah:furnator_spirited", 1)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(12)],
          deps=["furnator_niotic", "spirited"], icon="powah:furnator_spirited", optional=True),

    quest("magmator", 2.5, 9.5, "&cBau einen Magmator",
          subtitle="Lava statt Kohle.",
          description=[
              "Wie der Furnator, nur mit einem &6Eimer&r statt dem Ofen. Ein Eimer Lava gibt &e10 000 FE&r.",
              "",
              "Leistung in jeder Stufe wie beim Furnator: Starter 20 bis Spirited 8 000 FE/t. Neben einer Lavapumpe aus dem Nether läuft er ohne Pause.",
          ],
          tasks=[task_item("powah:magmator_starter", 1)],
          rewards=[reward_item("minecraft:lava_bucket", 1)],
          deps=["furnator"], icon="powah:magmator_starter", optional=True),

    quest("solar", 5, 9.5, "&eLeg ein Solar Panel aus",
          subtitle="Strom vom Himmel, nur bei Tag.",
          description=[
              "Drei &6Photoelectric Panes&r oben (Glasscheibe mit Lapis und Paste), zwei Tiny links und rechts vom Casing, drei Paste unten.",
              "",
              "&eFE/t:&r Starter 20, Basic 60, Hardened 100, Blazing 200, Niotic 400, Spirited 800. Mit einer &6Lens of Ender&r darauf sieht es durch Blöcke.",
          ],
          tasks=[task_item("powah:solar_panel_starter", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16)],
          deps=["furnator"], icon="powah:solar_panel_starter", optional=True),

    quest("thermo", 7.5, 9.5, "&cStell einen Thermo Generator auf",
          subtitle="Hitze unten, Wasser hinein.",
          description=[
              "Drei Paste oben, zwei Tiny links und rechts vom Casing, unten drei &6Thermoelectric Plates&r (Lohenstaub und Redstone um einen Tiny).",
              "",
              "Er steht auf einer Wärmequelle: &6Magmablock&r 800 Grad, &6Lava&r 1 000, Blazing-Kristallblock 2 800. Als Kühlmittel nimmt er Wasser. Leistung wie das Solar Panel, aber rund um die Uhr.",
          ],
          tasks=[task_item("powah:thermo_generator_starter", 1)],
          rewards=[reward_item("minecraft:magma_block", 4)],
          deps=["furnator"], icon="powah:thermo_generator_starter", optional=True),

    # ---- Reaktor --------------------------------------------------------------------
    quest("uraninite", 0, 12.5, "&aGrab Uraninit",
          subtitle="Der Brennstoff des Reaktors.",
          description=[
              "Uraninit-Erz gibt es in drei Sorten: arm unter &eY 64&r, normal unter &eY 20&r, dicht unter &eY 0&r. &6Rohes Uraninit&r gibt in der Kugel für 2 000 FE zwei &6Uraninit&r. Ein Erzblock mit Behutsamkeit gibt dort 3, 5 oder 10, je nach Sorte.",
              "",
              "Auch ein &6Uranbarren&r aus Mekanism wird in der Kugel zu Uraninit, für 30 000 FE.",
          ],
          tasks=[task_item("powah:uraninite", 36)],
          rewards=[reward_item("powah:dielectric_paste", 16), reward_xp(5)],
          deps=["rods"], icon="powah:uraninite"),

    quest("reactor", 2.5, 12.5, "&a&lBau einen Reaktor",
          subtitle="36 Blöcke, und er baut sich selbst.",
          description=[
              "&6Reaktor (Starter):&r Uraninit in die Ecken, Tiny an die Seiten, Casing in die Mitte, gibt vier. Du brauchst &e36&r.",
              "",
              "Nimm alle 36 in die Hand und setz einen ab. Auf einer freien Fläche von &e3 mal 3&r, &e4 Blöcke&r hoch, baut sich der Reaktor selbst auf. Fehlen Blöcke, sagt der Chat wie viele.",
          ],
          tasks=[task_item("powah:reactor_starter", 36)],
          rewards=[reward_item("powah:uraninite", 16), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["uraninite", "furnator"], icon="powah:reactor_starter", size=1.75, shape="hexagon"),

    quest("reactor_fuel", 5, 12.5, "&aZünde und kühl den Reaktor",
          subtitle="Uraninit, Kohle, Redstone, Eis.",
          description=[
              "&6Uraninit&r in den Brennstoffslot. &6Kohle&r und &6Redstone&r in den Nebenslots heben die Leistung. Kühl mit Wasser und festen Kühlmitteln: Eis, Packeis, Blaueis oder Trockeneis.",
              "",
              "Im &eAuto-Modus&r hält er an, wenn er voll ist, und startet unter 70 Prozent wieder. So verbrennt er kein Uraninit für nichts.",
              "",
              "Ein Starter-Reaktor macht bis &e250 FE/t&r.",
          ],
          tasks=[task_item("minecraft:packed_ice", 16)],
          rewards=[reward_item("minecraft:blue_ice", 8), reward_xp(8)],
          deps=["reactor"], icon="minecraft:packed_ice"),

    quest("reactor_upgrade", 7.5, 12.5, "&8Rüste den Reaktor auf",
          subtitle="Vier alte Blöcke, vier neue.",
          description=[
              "Vier Reaktorblöcke der Stufe darunter in die Ecken, vier Kondensatoren der neuen Stufe an die Seiten (Basic: Large), ein &6Uraninit&r in die Mitte, gibt vier. Für einen Reaktor wieder 36.",
              "",
              "&eFE/t:&r Starter 250, Basic 1 000, Hardened 2 500, Blazing 10 000, Niotic 25 000, Spirited 100 000. Nitro mit 500 000 kommt in Stufe 4.",
          ],
          tasks=[task_item("powah:reactor_basic", 36)],
          rewards=[reward_item("powah:uraninite", 32), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["reactor_fuel"], icon="powah:reactor_basic"),

    quest("reactor_blazing", 10, 12.5, "&6&lBau einen Blazing-Reaktor",
          subtitle="Zehntausend FE pro Tick.",
          description=[
              "Zwei Schritte: 36 Basic-Reaktoren werden mit Hardened-Kondensatoren und Uraninit zu 36 &8Hardened&r (2 500 FE/t), die dann mit Blazing-Kondensatoren zu 36 &6Blazing&r. Das Muster ist immer dasselbe: vier alte Blöcke in die Ecken, vier Kondensatoren an die Seiten, Uraninit in die Mitte.",
              "",
              "Ein Blazing-Reaktor macht bis &e10 000 FE/t&r, mehr als zwölf Blazing Furnators. Kühl ihn mit Trockeneis und füttere Kohle und Redstone nach.",
              "",
              "&eKabel nicht vergessen:&r Ab hier reichen Basic-Kabel (2 000 FE/t) nicht mehr.",
          ],
          tasks=[task_item("powah:reactor_blazing", 36)],
          rewards=[reward_item("powah:uraninite", 32), reward_table("s3_rare"), reward_xp(25)],
          deps=["reactor_upgrade", "blazing"], icon="powah:reactor_blazing", optional=True),

    # ---- Leiten und Speichern -------------------------------------------------------
    quest("cables", 0, 16.5, "&eLeg Energiekabel",
          subtitle="Zwölf Kabel aus Stäben und Nuggets.",
          description=[
              "Sechs waagerechte &6Dielectric Rods&r oben und unten, in der Mitte Eisennugget, Tiny, Eisennugget: zwölf &6Starter-Kabel&r. Basic: Eisen statt Nuggets und ein Basic-Kondensator.",
              "",
              "&eFE/t:&r Starter 500, Basic 2 000, Hardened 5 000, Blazing 20 000, Niotic 50 000, Spirited 200 000.",
          ],
          tasks=[task_item("powah:energy_cable_basic", 12)],
          rewards=[reward_item("powah:dielectric_paste", 16)],
          deps=["furnator"], icon="powah:energy_cable_basic"),

    quest("wrench", 2.5, 15.5, "&7Bau den Wrench",
          subtitle="Drei Modi für Kabel, Kugel und Blöcke.",
          description=[
              "Zwei &6Eisenbarren&r und drei Paste, schräg gelegt.",
              "",
              "&eConfig&r stellt an einer Kabelseite ein, ob sie zieht, schiebt oder nichts tut. &eLink&r verbindet Stäbe mit der Kugel. &eRotate&r dreht Blöcke. Der aktuelle Modus steht im Tooltip.",
          ],
          tasks=[task_item("powah:wrench", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 4)],
          deps=["cables"], icon="powah:wrench"),

    quest("cells", 2.5, 17.5, "&aBau Energiezellen",
          subtitle="Ein Puffer für die ganze Basis.",
          description=[
              "&6Energy Cell (Basic):&r Eisen in die Ecken, Basic-Kondensatoren an die Seiten, Casing in die Mitte. Höhere Zellen: Material der Stufe, zwei neue Kondensatoren, Casing und die Zelle darunter.",
              "",
              "&eSpeicher:&r Starter 1, Basic 4, Hardened 10, Blazing 40, Niotic 100, Spirited 400 Millionen FE.",
          ],
          tasks=[task_item("powah:energy_cell_basic", 1)],
          rewards=[reward_item("powah:capacitor_basic", 4), reward_xp(5)],
          deps=["cables"], icon="powah:energy_cell_basic"),

    quest("ender_cell", 5, 17.5, "&5Teil Strom ohne Kabel",
          subtitle="Ender Cells auf einem Kanal.",
          description=[
              "&6Ender Cell (Starter):&r Obsidian in die Ecken, Eisennuggets an die Seiten, ein &6Ender Core&r in die Mitte. Basic mit Eisenbarren.",
              "",
              "Alle Ender Cells auf demselben Kanal teilen einen Speicher, egal wo sie stehen. Shift-Klick mit einer Energiezelle oder Batterie im Fenster vergrößert ihn. Starter hat einen Kanal, Spirited neun.",
              "",
              "&6Ender Gates&r (Kabel statt Nuggets, gibt vier) machen das Gleiche kleiner, wie ein Kabelende.",
          ],
          tasks=[task_item("powah:ender_cell_starter", 2)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(8)],
          deps=["cells", "ender_core"], icon="powah:ender_cell_starter"),

    quest("transmitter", 7.5, 17.5, "&dLad dein Werkzeug überall",
          subtitle="Der Player Transmitter.",
          description=[
              "&6Aerial Pearl&r: Enderperle in der Mitte, Paste und Eisengitter drumherum. Rechtsklick damit auf einen &6Zombie&r oder &6Wüstenzombie&r macht eine &6Player Aerial Pearl&r. Transmitter: die Perle oben, Tiny, Casing, Tiny, ein senkrechter Rod unten.",
              "",
              "Dazu eine &6Binding Card&r (zwei Rods zur Blank Card, mit Redstone und Verrottetem Fleisch). Rechtsklick bindet sie an dich, sie kommt in den Transmitter.",
              "",
              "Er lädt dann die Stromgeräte in deinem Inventar, Starter mit &e500 FE/t&r. Benutz die Karte auf einem Enderman oder Endermite, dann wird sie zur &6Dimensional&r-Karte.",
          ],
          tasks=[task_item("powah:player_transmitter_starter", 1), task_item("powah:binding_card", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_table("s3_common"), reward_xp(10)],
          deps=["ender_cell"], icon="powah:player_transmitter_starter"),

    quest("ender_hunt", 10, 16.5, "&5Geh auf Endermanjagd",
          subtitle="Zwei Teile gibt es nur vom Enderman.",
          description=[
              "Rechtsklick mit einer &6Photoelectric Pane&r auf einen &5Enderman&r oder eine Endermite macht daraus die &6Lens Of Ender&r. Rechtsklick mit einer &6Binding Card&r macht die &6Binding Card (Dimensional)&r.",
              "",
              "&eDie Linse:&r Rechtsklick damit auf ein Solar Panel, und es sieht den Himmel auch durch Blöcke darüber. So bauen sich Solarfelder unter dem Dach oder unter der Erde.",
              "",
              "&eDie Karte:&r Im Player Transmitter lädt sie dich auch, wenn du in einer anderen Dimension bist.",
          ],
          tasks=[task_item("powah:lens_of_ender", 1), task_item("powah:binding_card_dim", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(10)],
          deps=["transmitter"], icon="powah:lens_of_ender", optional=True),

    quest("battery", 0, 18.75, "&aBau eine Battery",
          subtitle="Eine Million FE für die Tasche.",
          description=[
              "&6Battery (Starter):&r Paste in die Ecken, vier Basic Capacitors an die Seiten, ein &6Redstoneblock&r in die Mitte. Sie fasst &e1 000 000 FE&r, höhere Stufen bis 400 Millionen.",
              "",
              "&eSchleichen und Rechtsklick&r schaltet das Laden ein: Dann gibt sie ihren Strom an die anderen Stromgeräte in deinem Inventar ab. Eine volle Battery in der Tasche hält Werkzeug und Jetpack auf langen Ausflügen am Leben.",
              "",
              "Im Fenster einer Ender Cell macht eine Battery per Shift-Klick den Speicher größer.",
          ],
          tasks=[task_item("powah:battery_starter", 1)],
          rewards=[reward_item("powah:capacitor_basic", 4), reward_xp(5)],
          deps=["cells"], icon="powah:battery_starter", optional=True),

    quest("hopper", 2.5, 19.75, "&eLade eine ganze Kiste",
          subtitle="Der Energy Hopper.",
          description=[
              "&6Energy Hopper (Starter):&r drei Paste oben, Tiny links und rechts vom Casing, unten Paste, ein &6Trichter&r, Paste.",
              "",
              "Er zeigt wie ein Trichter in eine Richtung und lädt alle Stromgeräte in der Kiste oder dem Behälter davor, Starter mit &e500 FE/t&r. Strom bekommt er per Kabel.",
              "",
              "Eine Kiste voller Batteries, Tabletts und Werkzeug, ein Hopper dran, und alles ist am nächsten Morgen voll.",
          ],
          tasks=[task_item("powah:energy_hopper_starter", 1)],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(5)],
          deps=["battery"], icon="powah:energy_hopper_starter", optional=True),

    quest("discharger", 5, 19.75, "&eEntlade Batteries",
          subtitle="Der Energy Discharger.",
          description=[
              "&6Energy Discharger (Starter):&r Paste in die Ecken und an die Seiten, Tiny oben und unten in der Mitte, das Casing in die Mitte.",
              "",
              "Er zieht den Strom aus den Gegenständen in seinen Plätzen und gibt ihn an Kabel und Maschinen daneben ab. Das Gegenstück zum Energy Hopper.",
              "",
              "So trägst du Strom ohne Kabel: Batteries am Kraftwerk mit dem Hopper laden, zur Baustelle tragen, im Discharger leeren.",
          ],
          tasks=[task_item("powah:energy_discharger_starter", 1)],
          rewards=[reward_item("powah:dielectric_paste", 16), reward_xp(5)],
          deps=["battery"], icon="powah:energy_discharger_starter", optional=True),

    quest("cable_up", 10, 18.5, "&6Leg Blazing-Kabel",
          subtitle="Die Leitung muss mit dem Reaktor wachsen.",
          description=[
              "Sechs waagerechte Dielectric Rods oben und unten, in der Mitte Blazing-Kristall, &6Blazing Capacitor&r, Blazing-Kristall: zwölf &6Blazing-Kabel&r mit &e20 000 FE/t&r. Hardened-Kabel gehen genauso mit Energized Steel, 5 000 FE/t.",
              "",
              "Ein Kabel ist so stark wie sein schwächstes Stück. Ein Basic-Kabel (2 000 FE/t) zwischen Blazing-Reaktor und Zelle bremst alles auf ein Fünftel.",
          ],
          tasks=[task_item("powah:energy_cable_blazing", 12)],
          rewards=[reward_item("powah:crystal_blazing", 4), reward_xp(5)],
          deps=["cables", "blazing"], icon="powah:energy_cable_blazing", optional=True),

    quest("cell_niotic", 2.5, 21, "&bBau eine Niotic Energy Cell",
          subtitle="100 Millionen FE in einem Block.",
          description=[
              "Vier Niotic-Kristalle in die Ecken, zwei &6Niotic Capacitors&r oben und unten, zwei &6Blazing Energy Cells&r links und rechts, das Casing in die Mitte.",
              "",
              "Sie speichert &e100 Millionen FE&r, mehr als die beiden Blazing-Zellen zusammen (80 Millionen). Stell sie hinter den Reaktor, dann verpufft im Auto-Modus nichts.",
          ],
          tasks=[task_item("powah:energy_cell_niotic", 1)],
          rewards=[reward_item("powah:crystal_niotic", 2), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["cells", "niotic"], icon="powah:energy_cell_niotic", optional=True),
]

images = [
    head("title", "Powah", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 3: Stahlwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("energizing", "Energetisieren", 10.4, -2.4, colour="magic"),
    head("generators", "Strom erzeugen", 0.9, 5.4, colour="fire"),
    head("reactor", "Reaktor", 0.9, 10.9, colour="nature"),
    head("storage", "Leiten und Speichern", 0.9, 14.2, colour="water"),
]

chapter(C, "Powah", "powah:energizing_orb", "tech", quests, shape="circle", order=20, stage=3,
        subtitle=["Stufe 3: Energizing Orb, Kristalle bis Spirited, alle Generatorstufen, der Reaktor, Kabel und Zellen."],
        images=images)
