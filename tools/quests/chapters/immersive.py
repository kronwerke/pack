"""Immersive Engineering in stage 2, one step per quest: hammer, manual and plates, the coke
oven and creosote, treated wood, the crude and the improved blast furnace with steel, the alloy
kiln and its alloys, the engineer's workbench with blueprints and vacuum tubes, kinetic power
with dynamo, windmill and water wheel, LV and MV wiring with accumulators and transformers,
the thermoelectric generator, the external heater, conveyors, the fluid pump, tank, silo and crate shelf,
and a checklist of the stage 2 multiblocks with their sizes. Block counts come from the
multiblock structure files in the jar, numbers from the recipes and
immersiveengineering-server.toml. The engineering blocks and the big machines are stage 3
(chapter immersive_heavy)."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item, reward_table,
                  reward_xp, banner, img)

C = "immersive"


def tex(name):
    """An Immersive Engineering item texture by its file name (they differ from the ids)."""
    return img(f"immersiveengineering:textures/item/{name}.png", 32, 32)


def mb(name, title):
    """The advancement IE grants for forming one of its multiblocks."""
    return task_advancement(f"immersiveengineering:multiblocks/{name}", title)


quests = [
    # ---- Grundlagen ----------------------------------------------------------
    quest("welcome", 0, 6.5, "&6&lHol dir das Ingenieurshandbuch",
          subtitle="Ein Buch, das dir jeden Multiblock Schicht für Schicht zeigt.",
          description=[
              "Ein &6Buch&r und ein &6Hebel&r an der Werkbank ergeben das &6Ingenieurshandbuch&r. Rechtsklick öffnet es.",
              "",
              "&6Immersive Engineering&r baut seine Maschinen als &eMultiblöcke&r: Blöcke in der richtigen Form aufstellen, mit dem &6Ingenieurshammer&r draufschlagen, fertig. Im Handbuch kannst du jede Struktur drehen und Schicht für Schicht ansehen.",
              "",
              "&eStufe 2:&r Koksofen, Hochofen, Legierungsofen, Windmühle, Drähte, Tank und Silo. Die Ingenieursbausteine und alle großen Maschinen kommen in &6Stufe 3&r, siehe Kapitel &6Immersive Engineering: Schwerindustrie&r.",
              "",
              tex("tool_manual"),
          ],
          tasks=[task_item("immersiveengineering:manual", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s2_common")],
          icon="immersiveengineering:manual", size=2.0, shape="hexagon"),

    quest("hammer", 2.5, 6.5, "&7Bau einen Ingenieurshammer",
          subtitle="Der Schlüssel zu jedem Multiblock.",
          description=[
              "Zwei &6Eisenbarren&r, ein &6Faden&r und zwei &6Stöcke&r ergeben den &6Ingenieurshammer&r.",
              "",
              "&eSo formst du einen Multiblock:&r Struktur genau wie im Handbuch bauen, dann Rechtsklick mit dem Hammer auf den Block, den das Handbuch nennt. Stimmt ein Block nicht, passiert einfach nichts.",
              "",
              "Der Hammer hält &e100&r Anwendungen. Er macht auch Bleche und stellt die Seiten von Kondensatoren ein, also bau gleich einen zweiten.",
              "",
              tex("tool_hammer"),
          ],
          tasks=[task_item("immersiveengineering:hammer", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["welcome"], icon="immersiveengineering:hammer", size=1.5),

    quest("plates", 2.5, 9.2, "&7Hämmer Barren zu Blechen",
          subtitle="Ein Barren und der Hammer geben ein Blech.",
          description=[
              "Ein &6Barren&r und der &6Ingenieurshammer&r zusammen in die Werkbank ergeben ein &6Blech&r. Der Hammer verliert dabei einen Punkt Haltbarkeit.",
              "",
              "&6Eisenbleche&r brauchst du für Komponenten und Rohre, &6Kupferbleche&r für Kupferkabel, &6Bleibleche&r für den Kondensator. In Stufe 3 übernimmt die Metallpresse das.",
          ],
          tasks=[task_item("immersiveengineering:plate_iron", 4), task_item("immersiveengineering:plate_copper", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_item("minecraft:copper_ingot", 8)],
          deps=["hammer"], icon="immersiveengineering:plate_iron"),

    quest("wirecutter", 0, 9.2, "&7Bau einen Kabelschneider",
          subtitle="Er schneidet Bleche zu Kabeln und Drähte ab.",
          description=[
              "Zwei &6Stöcke&r und ein &6Eisenbarren&r ergeben den &6Ingenieurskabelschneider&r. Er hält &e250&r Schnitte.",
              "",
              "Mit einem Blech in der Werkbank schneidet er daraus ein Kabel. Rechtsklick auf einen Anschluss nimmt alle Drähte ab, die daran hängen.",
              "",
              tex("tool_wirecutter"),
          ],
          tasks=[task_item("immersiveengineering:wirecutter", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8)],
          deps=["welcome"]),

    quest("hemp", 0, 3.8, "&2Bau Industriehanf an",
          subtitle="Fasern für Segel, Gewebe und Pflanzenöl.",
          description=[
              "&6Industriehanfsamen&r fallen beim Abbauen von hohem Gras. Pflanz sie auf Ackerboden, der obere Block gibt beim Ernten &6Industriehanffasern&r.",
              "",
              "Acht Fasern um einen Stock ergeben &6Robustes Gewebe&r. Daraus werden Windmühlensegel, Sprungkissen und Ballons. Die Samen sind in Stufe 3 der beste Rohstoff für Pflanzenöl.",
          ],
          tasks=[task_item("immersiveengineering:seed", 4), task_item("immersiveengineering:hemp_fiber", 16)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["welcome"], icon="immersiveengineering:hemp_fiber"),

    quest("ores", 2.5, 3.8, "&7Grab nach Blei, Silber und Nickel",
          subtitle="Die drei Metalle, die du in Stufe 2 brauchst.",
          description=[
              "&6Blei&r Y -32 bis 80, &6Silber&r Y -48 bis 32, &6Nickel&r unter Y 24. Dazu &6Bauxit&r (Aluminium) Y 32 bis 112 und &6Uran&r Y -64 bis -16.",
              "",
              "Silber geht in Elektrum, Nickel in Constantan und Vakuumröhren, Blei in den Kondensator. Rohe Erze schmilzt du im Ofen oder schickst sie durch die Anreicherungskammer von Mekanism.",
          ],
          tasks=[task_item("immersiveengineering:ingot_lead", 4), task_item("immersiveengineering:ingot_silver", 4), task_item("immersiveengineering:ingot_nickel", 4)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["welcome"], icon="immersiveengineering:raw_silver"),

    # ---- Koks und Kreosot ----------------------------------------------------
    quest("cokebrick", 5, 0, "&6Brenn 27 Koksziegel",
          subtitle="Genug für einen Koksofen.",
          description=[
              "Vier &6Ton&r in die Ecken, vier &6Ziegel&r an die Seiten, ein &6Sandstein&r in die Mitte ergeben drei &6Koksziegel&r.",
              "",
              "Für einen Ofen sind das neun Rezepte: &e36 Ton, 36 Ziegel, 9 Sandstein&r. Ton gibt es in Flüssen und Sümpfen, Ziegel brennst du im Ofen aus Tonklumpen.",
          ],
          tasks=[task_item("immersiveengineering:cokebrick", 27)],
          rewards=[reward_item("minecraft:clay_ball", 32), reward_item("minecraft:sandstone", 8)],
          deps=["hammer"]),

    quest("coke_oven", 7.5, 0, "&8&lForm einen Koksofen",
          subtitle="3x3x3, 27 Koksziegel, Kohle rein, Koks und Kreosot raus.",
          description=[
              "Stell die &627 Koksziegel&r als &e3x3x3-Würfel&r auf und schlag mit dem Hammer auf die Mitte einer Seite.",
              "",
              "&eRein:&r bis zu &e16 Kohle&r oder &e8 Stämme&r pro Ladung. &eRaus:&r Koks oder Holzkohle, dazu &bKreosotöl&r im Tank: 500 mB pro Ladung Kohle (5 Minuten), 250 mB pro Ladung Stämme.",
              "",
              "&eTipp:&r Zwei &6Kohleblöcke&r geben einen Koksblock und gleich &e5 000 mB&r Kreosot. Für Kreosot sind Kohleblöcke also viel besser als lose Kohle.",
          ],
          tasks=[task_advancement("immersiveengineering:main/mb_cokeoven", "Einen Koksofen formen")],
          rewards=[reward_item("minecraft:coal", 32), reward_table("s2_common"), reward_xp(10)],
          deps=["cokebrick"], icon="immersiveengineering:cokebrick", size=1.75, shape="hexagon"),

    quest("coal_coke", 10, -1, "&8Mach Koks auf Vorrat",
          subtitle="Der Brennstoff für jeden Stahlbarren.",
          description=[
              "Leg &6Kohle&r in den Koksofen und nimm &6Koks für Kohle&r heraus.",
              "",
              "Im Roh-Hochofen reicht &eein Koks für einen Stahlbarren&r. Holzkohle geht auch, brennt dort aber nur ein Viertel so lang. Jede Kohle, die du jetzt findest, ist später ein Stahlbarren.",
              "",
              tex("material_coal_coke"),
          ],
          tasks=[task_item("immersiveengineering:coal_coke", 32)],
          rewards=[reward_item("minecraft:coal_block", 8)],
          deps=["coke_oven"]),

    quest("coke_block", 10, -2.6, "&8Pack Koks in Blöcke",
          subtitle="Neun Koks, ein Block.",
          description=[
              "Neun &6Koks&r ergeben einen &6Koksblock&r, und er wird wieder zu neun.",
              "",
              "Der Koksofen macht aus zwei Kohleblöcken direkt einen Koksblock, mit zehnmal so viel Kreosot wie eine Ladung loser Kohle.",
          ],
          tasks=[task_item("immersiveengineering:coke", 4)],
          rewards=[reward_item("minecraft:coal", 16)],
          deps=["coal_coke"], icon="immersiveengineering:coke", optional=True),

    quest("creosote", 10, 1, "&bZapf Kreosotöl ab",
          subtitle="Eimer ins Fenster, voller Eimer zurück.",
          description=[
              "Leg einen &6leeren Eimer&r in den Platz im Fenster des Koksofens, darunter nimmst du einen &6Kreosotöleimer&r heraus.",
              "",
              "Kreosot wird zu Behandeltem Holz und brennt zur Not im Dieselgenerator. Leer den Tank regelmäßig, sonst steht der Ofen, wenn er voll ist.",
          ],
          tasks=[task_item("immersiveengineering:creosote_bucket", 1)],
          rewards=[reward_item("minecraft:bucket", 2)],
          deps=["coke_oven"]),

    quest("pump", 7.5, 2.2, "&bPump das Kreosot ab",
          subtitle="Flüssigkeitspumpe und Rohre statt Eimer.",
          description=[
              "Sechs &6Eisenbleche&r ergeben acht &6Flüssigkeitsrohre&r. Eisenblech oben, Blech, &6Mechanische Eisenkomponente&r, Blech in der Mitte und drei Rohre unten ergeben die &6Flüssigkeitspumpe&r.",
              "",
              "Der Ofen gibt sein Kreosot nicht selbst ab, die Pumpe zieht es heraus. Mit Strom pumpt sie viel schneller. Seiten stellst du mit dem Hammer auf Eingang, Ausgang oder zu.",
          ],
          tasks=[task_item("immersiveengineering:fluid_pump", 1), task_item("immersiveengineering:fluid_pipe", 8)],
          rewards=[reward_item("immersiveengineering:plate_iron", 8), reward_xp(5)],
          deps=["creosote", "component"], icon="immersiveengineering:fluid_pump", optional=True),

    quest("treated_wood", 12.5, 1, "&6Tränk Bretter in Kreosot",
          subtitle="Behandeltes Holz, das Baumaterial des Mods.",
          description=[
              "Acht beliebige &6Holzbretter&r um einen &6Kreosotöleimer&r ergeben acht &6Behandelte Holzbretter&r. Der Eimer kommt leer zurück.",
              "",
              "Windmühle, Wasserrad, Werkbank, Pfosten und Fässer brauchen es. Rechne mit drei oder vier Eimern für den Anfang.",
          ],
          tasks=[task_item("immersiveengineering:treated_wood_horizontal", 32)],
          rewards=[reward_item("minecraft:oak_planks", 32)],
          deps=["creosote"], icon="immersiveengineering:treated_wood_horizontal"),

    quest("sticks", 15, 1, "&6Schnitz Behandelte Stöcke",
          subtitle="Für Blätter, Segmente und Zäune.",
          description=[
              "Zwei &6Behandelte Holzbretter&r übereinander ergeben vier &6Behandelte Stöcke&r.",
              "",
              "Aus ihnen und Behandeltem Holz entstehen Windmühlenblätter, Wasserradsegmente, Behandelte Holzzäune und die Pfosten für deine Drähte.",
              "",
              tex("material_stick_treated"),
          ],
          tasks=[task_item("immersiveengineering:stick_treated", 16)],
          rewards=[reward_item("minecraft:stick", 32)],
          deps=["treated_wood"]),

    quest("workbench", 12.5, 2.8, "&6Bau eine Ingenieurswerkbank",
          subtitle="Eine Werkbank, die ihre Zutaten behält.",
          description=[
              "Drei &6Behandelte Holzstufen&r oben, &6Behandelte Stöcke&r links und rechts, eine normale &6Werkbank&r in der Mitte ergeben die &6Ingenieurswerkbank&r.",
              "",
              "Sie behält die Zutaten im Raster, wenn du sie schließt, und hat eine Schublade. Sie ist außerdem die Zutat für den Ingenieursarbeitstisch.",
          ],
          tasks=[task_item("immersiveengineering:craftingtable", 1)],
          rewards=[reward_item("immersiveengineering:treated_wood_horizontal", 16)],
          deps=["treated_wood"]),

    quest("basic_engineering", 15, 2.8, "&6Bau Einfache Ingenieursbausteine",
          subtitle="Der Rahmen für Kondensatoren und Gartenglocke.",
          description=[
              "Vier &6Eisenbarren&r in die Ecken und vier &6Behandelte Holzbretter&r an die Seiten, Mitte frei, ergeben vier &6Einfache Ingenieursbausteine&r.",
              "",
              "Sie stecken in jedem Kondensator, in der Gartenglocke und in den Routern. Die Leichten und Schweren Bausteine sind etwas anderes, die öffnen erst in Stufe 3.",
          ],
          tasks=[task_item("immersiveengineering:basic_engineering", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 8)],
          deps=["treated_wood"], icon="immersiveengineering:basic_engineering"),

    # ---- Stahl ---------------------------------------------------------------
    quest("blastbrick", 18, -1, "&cBrenn 27 Sprengziegel",
          subtitle="Zutaten aus dem Nether.",
          description=[
              "Vier &6Netherziegel&r in die Ecken, vier &6Ziegel&r an die Seiten, ein &6Magmablock&r in die Mitte ergeben drei &6Sprengziegel&r.",
              "",
              "Für einen Hochofen: &e36 Netherziegel, 36 Ziegel, 9 Magmablöcke&r. Magmablöcke liegen an Lavaseen im Nether, oder du baust sie aus vier Magmacreme. Den Weg dorthin zeigt das Nether-Kapitel.",
          ],
          tasks=[task_item("immersiveengineering:blastbrick", 27)],
          rewards=[reward_item("minecraft:magma_block", 4), reward_item("minecraft:brick", 16)],
          deps=["coal_coke"]),

    quest("blast_furnace", 20.5, -1, "&c&lForm einen Roh-Hochofen",
          subtitle="3x3x3, 27 Sprengziegel, Eisen rein, Stahl raus.",
          description=[
              "Stell die &627 Sprengziegel&r als &e3x3x3-Würfel&r auf und schlag mit dem Hammer auf die Mitte einer Seite.",
              "",
              "&eRein:&r oben &6Eisen&r, darunter &6Koks&r. &eRaus:&r ein &6Stahlbarren&r pro Minute, dazu &6Schlacke&r. Ein Koks brennt genau eine Minute, Holzkohle ein Viertel davon.",
              "",
              "&cDer Roh-Hochofen lässt sich nicht automatisieren.&r Trichter greifen nicht, alles geht übers Fenster. Nimm die Schlacke heraus, sonst bleibt er stehen.",
          ],
          tasks=[task_advancement("immersiveengineering:main/mb_blastfurnace", "Einen Roh-Hochofen formen")],
          rewards=[reward_item("immersiveengineering:coal_coke", 16), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["blastbrick"], icon="immersiveengineering:blastbrick", size=1.75, shape="hexagon"),

    quest("steel", 23, -1, "&8&lSchmilz deine ersten 16 Stahlbarren",
          subtitle="Stahl, ein Barren pro Minute.",
          description=[
              "Lass den Roh-Hochofen mit &6Eisen&r und &6Koks&r laufen, bis &e16 Stahlbarren&r fertig sind.",
              "",
              "Ein voller Stapel Eisen und Koks ist in gut einer Stunde durch. Stahl aus Immersive Engineering und aus Mekanism ist derselbe Barren, du kannst ihn in beiden Mods verwenden.",
              "",
              tex("metal_ingot_steel"),
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 32)],
          deps=["blast_furnace"], icon="immersiveengineering:ingot_steel", size=1.5),

    quest("slag", 23, 1, "&7Heb die Schlacke auf",
          subtitle="Abfall mit Nutzen.",
          description=[
              "Sammle &e16 Schlacke&r aus dem Hochofen.",
              "",
              "Im Ofen wird sie zu &6Schlackeglas&r, das auch HV-Relais nehmen. In Stufe 3 geht sie in Industriedünger und Beton. Also in eine Kiste damit, nicht in die Lava.",
          ],
          tasks=[task_item("immersiveengineering:slag", 16)],
          rewards=[reward_xp(5)],
          deps=["steel"], optional=True),

    quest("improved", 20.5, 1.2, "&cVerstärk 27 Sprengziegel",
          subtitle="Das Baumaterial des Verbesserten Hochofens.",
          description=[
              "Ein &6Sprengziegel&r und ein &6Stahlblech&r formlos in der Werkbank ergeben einen &6Verstärkten Sprengziegel&r.",
              "",
              "Du brauchst &e27&r Stück, also 27 Stahlbleche. Den Stahl dafür liefert dein Roh-Hochofen.",
          ],
          tasks=[task_item("immersiveengineering:blastbrick_reinforced", 27)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 8), reward_xp(5)],
          deps=["steel"], icon="immersiveengineering:blastbrick_reinforced"),

    quest("improved_form", 20.5, 2.4, "&c&lForm einen Verbesserten Hochofen",
          subtitle="3x4x3, 27 Verstärkte Sprengziegel und ein Trichter.",
          description=[
              "Stell die &627 Verstärkten Sprengziegel&r als 3x3x3-Würfel auf, setz einen &6Trichter&r oben in die Mitte und schlag mit dem Hammer auf den Block, den das Handbuch zeigt.",
              "",
              "&eRein:&r Eisen und Koks von oben durch den Trichter. &eRaus:&r Stahl vorne, Schlacke hinten, direkt in Kisten oder auf Förderbänder. Das ist die erste Stahlstraße, die ohne dich läuft.",
          ],
          tasks=[mb("mb_improvedblastfurnace", "Einen Verbesserten Hochofen formen")],
          rewards=[reward_item("immersiveengineering:coal_coke", 32), reward_table("s2_uncommon"), reward_xp(15)],
          deps=["improved"], icon="immersiveengineering:blastbrick_reinforced", size=1.5, shape="hexagon"),

    quest("preheater", 23, 3.2, "&cHäng Vorwärmer an den Hochofen",
          subtitle="Heiße Luft macht ihn schneller.",
          description=[
              "Vier &6Eisenblechblöcke&r oben, darunter ein &6Flüssigkeitsrohr&r und ein &6Externer Heizer&r ergeben den &6Hochofen-Vorwärmer&r.",
              "",
              "Bis zu &ezwei&r Vorwärmer an die Seiten des Verbesserten Hochofens, jeder zieht &d32 FE/t&r. Ohne Strom geht es auch, nur langsamer.",
          ],
          tasks=[task_item("immersiveengineering:blastfurnace_preheater", 2)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 8), reward_xp(10)],
          deps=["improved_form", "external_heater"], icon="immersiveengineering:blastfurnace_preheater", optional=True),

    quest("engineer", 26, -1, "&6&lLeg 64 Stahlbarren auf Vorrat",
          subtitle="Ein Stapel Stahl für Stufe 3.",
          description=[
              "Sammle &e64 Stahlbarren&r. Roh-Hochofen, Verbesserter Hochofen oder Mekanism, alles zählt.",
              "",
              "&eKronwerke:&r Das Obelisk-Ziel von &6Stufe 3&r will &e4 000 Stahlbarren&r. Zwei, drei Hochöfen, die jetzt schon laufen, machen das später entspannt. Eine Kiste neben dem Obelisken nimmt alles an, was du hineinschickst.",
              "",
              "Damit sitzen die Grundlagen: Multiblöcke, Koks, Kreosot, Legierungen und Stahl.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 64)],
          rewards=[reward_table("s2_rare"), reward_item("immersiveengineering:coal_coke", 32), reward_xp(20)],
          deps=["steel"], icon="immersiveengineering:storage_steel", size=2.5, shape="gear"),

    quest("steel_tools", 26, 1.4, "&7Schmied eine Stahlspitzhacke",
          subtitle="Hält deutlich länger als Eisen.",
          description=[
              "&6Stahlbarren&r und &6Behandelte Stöcke&r ergeben Stahlwerkzeuge wie bei Eisen. Stahlbleche und Behandeltes Holz um einen Schild ergeben das &6Schwere Schild&r.",
              "",
              "Genau richtig für die langen Grabungen nach Nickel und Silber.",
              "",
              tex("tool_pickaxe_steel"),
          ],
          tasks=[task_item("immersiveengineering:pickaxe_steel", 1)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 4)],
          deps=["engineer"], optional=True),

    # ---- Legierungen ---------------------------------------------------------
    quest("kilnbrick", 6, 6.5, "&6Brenn 8 Legierungsziegel",
          subtitle="Genug für einen Legierungsofen.",
          description=[
              "Zwei &6Sandstein&r und zwei &6Ziegel&r über Kreuz ergeben zwei &6Legierungsziegel&r. Für den Ofen reichen &e8&r.",
              "",
              "Der Legierungsofen ist der billigste Multiblock des Mods und verschmilzt zwei Metalle zu einem.",
          ],
          tasks=[task_item("immersiveengineering:alloybrick", 8)],
          rewards=[reward_item("minecraft:sandstone", 8)],
          deps=["hammer"]),

    quest("kiln", 8.5, 6.5, "&6&lForm einen Legierungsofen",
          subtitle="2x2x2, 8 Legierungsziegel, zwei Metalle rein, Legierung raus.",
          description=[
              "Stell die &68 Legierungsziegel&r als &e2x2x2-Würfel&r auf und schlag mit dem Hammer auf einen der Blöcke.",
              "",
              "&eRein:&r zwei Metalle in die beiden Eingänge, darunter Brennstoff wie Kohle oder Koks. &eRaus:&r Elektrum, Constantan, Bronze und Isolierglas. Messing macht er auf Kronwerke nicht.",
          ],
          tasks=[task_checkmark("Legierungsofen gebaut und geformt")],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["kilnbrick"], icon="immersiveengineering:alloybrick", size=1.75, shape="hexagon"),

    quest("brass", 11, 6.5, "&6Lies, warum es hier kein Messing gibt",
          subtitle="Messing kommt nur aus dem Mixer von Create.",
          description=[
              "Messing macht auf Kronwerke nur der &6Mechanische Mixer&r von Create: zwei Kupfer, ein Zink und ein &6Lohenstaub&r erhitzt ergeben einen Barren, &cüberhitzt&r zwei Barren ohne Staub. Siehe Kapitel &6Create: Messing&r.",
              "",
              "&eRezept auf Kronwerke:&r Der &6Leichte Ingenieursbaustein&r braucht ein &6Messingblech&r statt eines Kupferbarrens, der &6Schwere Ingenieursbaustein&r einen &6Präzisionsmechanismus&r statt einer Stahlkomponente. Beide öffnen in Stufe 3.",
              "",
              "Wer jetzt Messingbleche und Präzisionsmechanismen beiseitelegt, baut in Stufe 3 sofort die großen Maschinen. Tausch deinen Koks und Stahl gegen das Messing der Create-Spieler.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("create:zinc_ingot", 16), reward_item("minecraft:copper_ingot", 16)],
          deps=["kiln"], icon="create:brass_ingot"),

    quest("bronze", 13.5, 6.5, "&6Leg Bronze im Legierungsofen",
          subtitle="Drei Kupfer und ein Zinn geben vier Bronze.",
          description=[
              "Drei &6Kupferbarren&r und ein &6Zinnbarren&r ergeben im Legierungsofen &e4 Bronzebarren&r. Zinn bringt Mekanism mit.",
              "",
              "Bronze braucht der Werkzeugsatz von Mekanism Tools und einige Rezepte anderer Mods.",
          ],
          tasks=[task_item("mekanism:ingot_bronze", 8)],
          rewards=[reward_item("minecraft:copper_ingot", 16)],
          deps=["kiln"], icon="mekanism:ingot_bronze", optional=True),

    quest("electrum", 11, 4.6, "&eLeg Elektrum",
          subtitle="Gold und Silber, das Metall der Mittelspannung.",
          description=[
              "Ein &6Goldbarren&r und ein &6Silberbarren&r ergeben im Legierungsofen &e2 Elektrumbarren&r.",
              "",
              "Aus Elektrum werden MV-Draht und MV-Anschlüsse, und in Stufe 3 steckt es in jedem Schweren Ingenieursbaustein.",
              "",
              tex("metal_ingot_electrum"),
          ],
          tasks=[task_item("immersiveengineering:ingot_electrum", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["kiln", "ores"]),

    quest("constantan", 11, 8.4, "&6Leg Constantan",
          subtitle="Kupfer und Nickel für Thermoelemente.",
          description=[
              "Ein &6Kupferbarren&r und ein &6Nickelbarren&r ergeben im Legierungsofen &e2 Constantanbarren&r.",
              "",
              "Constantanbleche gehen in den Thermoelektrischen Generator und in Stufe 3 in die Kühlerblöcke des Dieselgenerators.",
              "",
              tex("metal_ingot_constantan"),
          ],
          tasks=[task_item("immersiveengineering:ingot_constantan", 4)],
          rewards=[reward_item("minecraft:copper_ingot", 8)],
          deps=["kiln", "ores"]),

    # ---- Arbeitstisch --------------------------------------------------------
    quest("bench", 16, 5.0, "&6Bau einen Ingenieursarbeitstisch",
          subtitle="Der Tisch für Blaupausen.",
          description=[
              "Ein &6Eisenbarren&r und zwei &6Behandelte Holzstufen&r oben, darunter die &6Ingenieurswerkbank&r und ein &6Behandelter Holzzaun&r ergeben den &6Ingenieursarbeitstisch&r.",
              "",
              "&6Blaupause Komponenten:&r Kupfer, Blei und Eisen oben, drei blaue Farbstoffe, drei Papier. Blaupause links ins Fenster, Zutaten in die Mitte, rechts siehst du, was du daraus machen kannst.",
          ],
          tasks=[task_item("immersiveengineering:workbench", 1), task_item("immersiveengineering:blueprint", 1)],
          rewards=[reward_item("minecraft:paper", 16), reward_item("minecraft:blue_dye", 8), reward_xp(5)],
          deps=["workbench", "ores"], icon="immersiveengineering:workbench"),

    quest("electron_tube", 18.5, 5.0, "&dMach Vakuumröhren",
          subtitle="Drei Röhren pro Rezept, am Arbeitstisch.",
          description=[
              "Mit der Blaupause Komponenten: &6Glas&r, ein &6Nickelblech&r, ein &6Kupferkabel&r und &6Redstone&r ergeben drei &6Vakuumröhren&r.",
              "",
              "Sie stecken in der Ladestation und in Stufe 3 in der Fortgeschrittenen Elektronikkomponente. Die Elektronenröhre von Create ist ein anderes Teil.",
              "",
              tex("material_electron_tube"),
          ],
          tasks=[task_item("immersiveengineering:electron_tube", 6)],
          rewards=[reward_item("immersiveengineering:ingot_nickel", 4), reward_xp(5)],
          deps=["bench"], icon="immersiveengineering:electron_tube"),

    quest("cloche", 16, 8.4, "&2Stell eine Gartenglocke auf",
          subtitle="Eine Pflanze, die sich selbst erntet.",
          description=[
              "Glas, &6Glühbirne&r, Glas oben, Glas, &6Mechanische Eisenkomponente&r, Glas in der Mitte, ein &6Einfacher Ingenieursbaustein&r unten. Glühbirnen: Blaupause Komponenten, Glas, drei Papier, ein Kupfer, gibt drei.",
              "",
              "Erde und Samen in die Mitte, Wasser hinein, &d8 FE/t&r Strom. Die Ernte kommt vorne heraus. Sie zieht auch Hanf, Blumen, Netherwarzen und Chorusfrüchte.",
          ],
          tasks=[task_item("immersiveengineering:cloche", 1)],
          rewards=[reward_item("immersiveengineering:seed", 8), reward_xp(5)],
          deps=["bench", "basic_engineering"], icon="immersiveengineering:cloche", optional=True),

    # ---- Wind und Draht ------------------------------------------------------
    quest("component", 6, 12, "&7Bau Mechanische Eisenkomponenten",
          subtitle="Zahnräder und Wellen in einem Teil.",
          description=[
              "Vier &6Eisenbleche&r in die Ecken, ein &6Kupferbarren&r in die Mitte ergeben eine &6Mechanische Eisenkomponente&r.",
              "",
              "Sie steckt im Dynamo, in der Pumpe, der Gartenglocke und in Stufe 3 in jedem Leichten Ingenieursbaustein. Mach gleich ein paar mehr.",
              "",
              tex("material_component_iron"),
          ],
          tasks=[task_item("immersiveengineering:component_iron", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["plates"]),

    quest("wire", 6, 14, "&6Schneid Kupferkabel",
          subtitle="Ein Blech, ein Kabel.",
          description=[
              "Ein &6Kupferblech&r und der &6Kabelschneider&r in der Werkbank ergeben ein &6Kupferkabel&r.",
              "",
              "Kupferkabel sind der Rohstoff für LV-Drahtspulen und für Vakuumröhren.",
              "",
              tex("material_wire_copper"),
          ],
          tasks=[task_item("immersiveengineering:wire_copper", 8)],
          rewards=[reward_item("minecraft:copper_ingot", 16)],
          deps=["wirecutter", "plates"]),

    quest("wirecoil", 8.5, 14, "&6Wickel LV-Drahtspulen",
          subtitle="Niederspannung zum Aufhängen.",
          description=[
              "Vier &6Kupferkabel&r um einen &6Stock&r ergeben vier &6LV-Drahtspulen&r.",
              "",
              "Spule in die Hand, erst einen Anschluss anklicken, dann den nächsten. Ein Stück darf höchstens &e16 Blöcke&r lang sein, und kein Block darf im Weg stehen.",
              "",
              tex("wirecoil_copper"),
          ],
          tasks=[task_item("immersiveengineering:wirecoil_copper", 8)],
          rewards=[reward_item("minecraft:stick", 16)],
          deps=["wire"]),

    quest("coil_lv", 11, 14, "&6Bau einen Kupferspulenblock",
          subtitle="Das Innere des Dynamos.",
          description=[
              "Acht &6LV-Drahtspulen&r um einen &6Eisenbarren&r ergeben einen &6Kupferspulenblock&r.",
              "",
              "Er steckt im Kinetischen Dynamo, im Thermoelektrischen Generator und in der Ladestation.",
          ],
          tasks=[task_item("immersiveengineering:coil_lv", 1)],
          rewards=[reward_item("immersiveengineering:wirecoil_copper", 4)],
          deps=["wirecoil"]),

    quest("dynamo", 13.5, 13, "&e&lStell einen Kinetischen Dynamo auf",
          subtitle="Drehung wird zu Strom.",
          description=[
              "Zwei &6Redstone&r und eine &6Mechanische Eisenkomponente&r oben, &6Eisenbarren&r, &6Kupferspulenblock&r, Eisenbarren darunter ergeben den &6Kinetischen Dynamo&r.",
              "",
              "Er nimmt nur Drehung von &6Windmühle&r oder &6Wasserrad&r aus Immersive Engineering an, keine Wellen von Create. &eErst den Dynamo stellen&r, dann Windmühle oder Rad an seine Wellenseite.",
          ],
          tasks=[task_item("immersiveengineering:dynamo", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_table("s2_common")],
          deps=["component", "coil_lv"], icon="immersiveengineering:dynamo", size=1.5, shape="hexagon"),

    quest("windmill", 16, 13, "&b&lSetz eine Windmühle an den Dynamo",
          subtitle="Strom aus der Luft.",
          description=[
              "Drei &6Behandelte Holzbretter&r und vier &6Behandelte Stöcke&r ergeben ein &6Windmühlenblatt&r. Acht Blätter um einen &6Eisenbarren&r ergeben die &6Windmühle&r.",
              "",
              "Sie braucht viel freien Raum vor sich, jeder Block im Weg bremst. Ganz frei und ohne Segel macht sie etwa &d17 FE/t&r. Über dem Ozean dreht sie 15 Prozent schneller, bei Regen und Gewitter auch.",
              "",
              tex("material_windmill_blade"),
          ],
          tasks=[task_item("immersiveengineering:windmill", 1)],
          rewards=[reward_item("immersiveengineering:treated_wood_horizontal", 16), reward_item("immersiveengineering:stick_treated", 16), reward_xp(10)],
          deps=["dynamo", "sticks"], icon="immersiveengineering:windmill", size=1.75, shape="gear"),

    quest("sails", 16, 11, "&bSpann Segel auf die Windmühle",
          subtitle="Mehr Fläche, mehr Strom.",
          description=[
              "Sechs &6Robustes Gewebe&r ergeben ein &6Windmühlensegel&r. Rechtsklick mit dem Segel auf die Windmühle spannt es auf ein Blatt.",
              "",
              "Mit allen acht Segeln liefert eine freie Windmühle rund &d50 FE/t&r, im Gewitter etwa das Doppelte.",
              "",
              tex("material_windmill_sail"),
          ],
          tasks=[task_item("immersiveengineering:windmill_sail", 8)],
          rewards=[reward_item("immersiveengineering:hemp_fiber", 16)],
          deps=["windmill", "hemp"], optional=True),

    quest("watermill", 16, 15.2, "&9Bau ein Wasserrad",
          subtitle="Gleichmäßig, Tag und Nacht.",
          description=[
              "Vier &6Wasserradsegmente&r (Behandeltes Holz und Behandelte Stöcke) um einen &6Stahlbarren&r ergeben das &6Wasserrad&r.",
              "",
              "Je mehr fließendes Wasser um das Rad läuft, desto schneller dreht es. Bis zu drei Räder hintereinander treiben eine gemeinsame Welle. Das Wetter ist ihm egal.",
              "",
              tex("material_waterwheel_segment"),
          ],
          tasks=[task_item("immersiveengineering:watermill", 1)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 4)],
          deps=["dynamo", "steel"], optional=True),

    quest("connectors", 18.5, 13, "&cSpann deinen ersten Draht",
          subtitle="Anschlüsse auf Maschinen, Relais dazwischen.",
          description=[
              "Ein &6Kupferbarren&r oben, darunter zweimal Terrakotta, Kupfer, Terrakotta ergeben vier &6LV-Kabelanschlüsse&r. Die oberen zwei Reihen davon ergeben acht &6LV-Kabelrelais&r.",
              "",
              "&eAnschlüsse&r nehmen bis zu &d256 FE/t&r auf oder geben sie ab. &eRelais&r sind nur Knoten. Ein Kupferdraht trägt &d2 048 FE/t&r, hängen mehr Anschlüsse dran, brennt er durch.",
              "",
              "Pro 16 Blöcke Kupferdraht gehen 1,25 Prozent verloren. Unisolierte Drähte unter Strom verletzen jeden, der sie berührt.",
          ],
          tasks=[task_item("immersiveengineering:connector_lv", 4), task_item("immersiveengineering:connector_lv_relay", 4),
                 task_advancement("immersiveengineering:main/connect_wire", "Einen Draht spannen")],
          rewards=[reward_item("minecraft:terracotta", 16), reward_item("immersiveengineering:wirecoil_copper", 8)],
          deps=["windmill"], icon="immersiveengineering:connector_lv"),

    quest("redstone_acid", 18.5, 11, "&cMisch Redstonesäure",
          subtitle="Der Elektrolyt für jeden Kondensator.",
          description=[
              "Vier &6Redstone&r und ein &6Wassereimer&r formlos in der Werkbank ergeben einen &6Eimer Redstonesäure&r.",
              "",
              "Jeder Kondensator braucht einen. In Stufe 3 mischt der Mischer die Säure aus einem Redstone pro 250 mB Wasser, also viel billiger.",
          ],
          tasks=[task_item("immersiveengineering:redstone_acid_bucket", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["connectors"], icon="immersiveengineering:redstone_acid_bucket"),

    quest("capacitor", 21, 13, "&c&lBau einen LV-Kondensator",
          subtitle="100 000 FE Puffer für windstille Tage.",
          description=[
              "Kupfer, &6Redstonesäureeimer&r, Kupfer oben, &6Bleiblech&r, &6Einfacher Ingenieursbaustein&r, Bleiblech unten ergeben den &6LV-Kondensator&r.",
              "",
              "Er speichert &e100 000 FE&r, je Seite &d256 FE/t&r. Rechtsklick mit dem Hammer stellt eine Seite auf &9blau&r (Eingang), &6orange&r (Ausgang) oder aus, schleichend die Gegenseite.",
          ],
          tasks=[task_item("immersiveengineering:capacitor_lv", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(15)],
          deps=["connectors", "redstone_acid", "basic_engineering"], icon="immersiveengineering:capacitor_lv", size=1.5, shape="hexagon"),

    quest("voltmeter", 21, 15, "&7Bau ein Ingenieursvoltmeter",
          subtitle="Wie viel Strom ist noch drin?",
          description=[
              "Ein &6Kompass&r oben, darunter Stock, &6Kupferbarren&r, Stock ergeben das &6Ingenieursvoltmeter&r.",
              "",
              "Rechtsklick auf einen Speicher zeigt den Füllstand. Schleichend auf zwei Anschlüsse geklickt zeigt es den Verlust auf der Strecke dazwischen.",
              "",
              tex("tool_voltmeter"),
          ],
          tasks=[task_item("immersiveengineering:voltmeter", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8)],
          deps=["connectors"], optional=True),

    quest("thermoelectric", 13.5, 15.5, "&cBau einen Thermoelektrischen Generator",
          subtitle="Strom aus heiß und kalt, ohne bewegte Teile.",
          description=[
              "Drei &6Stahlbarren&r oben, &6Constantanblech&r, &6Kupferspulenblock&r, Constantanblech in der Mitte, drei Constantanbleche unten ergeben den Generator.",
              "",
              "Heiß auf eine Seite, kalt auf die gegenüberliegende. Der Unterschied zählt: &6Magmablock&r 1 300 Kelvin gegen &6Blaueis&r 200 Kelvin ist ein gutes Paar. Lava und Wasser gehen auch.",
          ],
          tasks=[task_item("immersiveengineering:thermoelectric_generator", 1)],
          rewards=[reward_item("minecraft:magma_block", 4), reward_item("minecraft:packed_ice", 8), reward_xp(10)],
          deps=["coil_lv", "constantan", "steel"], icon="immersiveengineering:thermoelectric_generator", optional=True),

    quest("external_heater", 11, 16, "&cHeiz einen Ofen mit Strom",
          subtitle="Der Externe Heizer ersetzt die Kohle.",
          description=[
              "&6Kupferbleche&r in die Ecken, &6LV-Drahtspulen&r an die Seiten, ein &6Eisenblechblock&r in die Mitte, &6Redstone&r unten in der Mitte ergeben den &6Externen Heizer&r.",
              "",
              "Neben einem normalen Ofen heizt er mit &d8 FE/t&r, ist der Ofen ganz heiß, mit bis zu &d32 FE/t&r für doppeltes Tempo. Er steckt auch im Hochofen-Vorwärmer.",
          ],
          tasks=[task_item("immersiveengineering:furnace_heater", 1)],
          rewards=[reward_item("immersiveengineering:plate_copper", 4), reward_xp(5)],
          deps=["wirecoil"], icon="immersiveengineering:furnace_heater"),

    # ---- Mittelspannung --------------------------------------------------------
    quest("wire_mv", 8.5, 18.5, "&eWickel MV-Drahtspulen",
          subtitle="Viermal so viel Strom wie Kupfer.",
          description=[
              "&6Elektrumblech&r plus Kabelschneider gibt &6Elektrumkabel&r, vier davon um einen Stock ergeben vier &6MV-Drahtspulen&r. &6MV-Anschlüsse&r wie LV, nur mit Elektrumbarren.",
              "",
              "MV-Draht trägt &d8 192 FE/t&r über 16 Blöcke, ein MV-Anschluss &d1 024 FE/t&r. Der Verlust pro Strecke ist viermal kleiner als bei Kupfer.",
              "",
              tex("wirecoil_electrum"),
          ],
          tasks=[task_item("immersiveengineering:wirecoil_electrum", 8), task_item("immersiveengineering:connector_mv", 4)],
          rewards=[reward_item("immersiveengineering:ingot_electrum", 4), reward_xp(5)],
          deps=["electrum", "connectors"], icon="immersiveengineering:wirecoil_electrum"),

    quest("transformer", 11, 18.5, "&eBau einen Trafo",
          subtitle="LV und MV in einem Netz.",
          description=[
              "LV- und MV-Anschluss oben, &6Elektronikkomponente&r und &6Elektrumspulenblock&r in der Mitte, zwei Eisenbarren unten. Die Komponente: Blaupause Komponenten, Behandelte Holzstufe, Quarz, Redstone, Elektrumkabel.",
              "",
              "Anschlüsse und Relais nehmen nur Draht ihrer Spannung. Der Trafo verbindet einen LV- und einen MV-Draht und passt auch auf einen Holzpfosten.",
          ],
          tasks=[task_item("immersiveengineering:transformer", 1)],
          rewards=[reward_item("minecraft:quartz", 8), reward_xp(10)],
          deps=["wire_mv", "bench"], icon="immersiveengineering:transformer"),

    quest("capacitor_mv", 13.5, 18.5, "&e&lBau einen MV-Kondensator",
          subtitle="Eine Million FE.",
          description=[
              "Elektrum, &6Redstonesäureeimer&r, Elektrum oben, &6Nickelblech&r, &6Einfacher Ingenieursbaustein&r, &6Eisenblech&r unten ergeben den &6MV-Kondensator&r.",
              "",
              "Er speichert &e1 000 000 FE&r, je Seite &d1 024 FE/t&r. Seiten stellst du wie beim LV-Kondensator mit dem Hammer ein.",
          ],
          tasks=[task_item("immersiveengineering:capacitor_mv", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(15)],
          deps=["transformer", "capacitor"], icon="immersiveengineering:capacitor_mv", size=1.5, shape="hexagon"),

    # ---- Lager und Transport ---------------------------------------------------
    quest("conveyor", 6, 21.5, "&7Leg Förderbänder",
          subtitle="Transport ohne Strom.",
          description=[
              "Drei &6Leder&r oben, &6Eisen&r, &6Redstone&r, Eisen darunter ergeben acht &6Förderbänder&r.",
              "",
              "Sie tragen Gegenstände und Tiere und schieben am Ende in jedes Inventar. Der Hammer dreht sie, schleichend stellt er die Steigung ein. Weitere Bänder siehe Kapitel &6Transport&r.",
          ],
          tasks=[task_item("immersiveengineering:conveyor_basic", 16), task_advancement("immersiveengineering:main/place_conveyor", "Ein Förderband legen")],
          rewards=[reward_item("minecraft:leather", 8)],
          deps=["plates"], icon="immersiveengineering:conveyor_basic"),

    quest("tank", 8.5, 21.5, "&9Form einen Flüssigkeitstank",
          subtitle="3x5x3, 34 Blechblöcke und 4 Zäune, 512 Eimer.",
          description=[
              "&634 Eisenblechblöcke&r (vier Eisenbleche geben vier) und &64 Behandelte Holzzäune&r als Beine, Form wie im Handbuch, dann Hammer drauf.",
              "",
              "&eRein:&r jede Flüssigkeit, oben oder unten. &eRaus:&r nur unten in der Mitte, mit Redstone-Signal pumpt er selbst ab. Ein Komparator dort zeigt den Füllstand. Jedes Blech geht, nicht nur Eisen.",
          ],
          tasks=[mb("mb_tank", "Einen Tank formen")],
          rewards=[reward_item("immersiveengineering:sheetmetal_iron", 16), reward_xp(10)],
          deps=["conveyor", "treated_wood"], icon="immersiveengineering:sheetmetal_iron"),

    quest("silo", 11, 21.5, "&9Form ein Elementsilo",
          subtitle="3x7x3, 50 Blechblöcke und 4 Zäune, 41 472 Gegenstände.",
          description=[
              "&650 Eisenblechblöcke&r und &64 Behandelte Holzzäune&r, Form wie im Handbuch, dann Hammer drauf.",
              "",
              "&eRein:&r eine einzige Sorte Gegenstand, oben durchs Gitter oder unten. &eRaus:&r unten, mit Redstone-Signal von selbst. Es fasst so viel wie &e24 Kisten&r, gut für Bruchstein, Samen oder Schlacke.",
          ],
          tasks=[mb("mb_silo", "Ein Silo formen")],
          rewards=[reward_item("immersiveengineering:sheetmetal_iron", 16), reward_xp(10)],
          deps=["tank"], icon="immersiveengineering:treated_fence"),

    quest("shelf", 13.5, 21.5, "&9Form ein Kistenregal",
          subtitle="4x4x2, 24 Stahllaufstege und 4 Stahlzäune, zwölf Kisten an einem Ort.",
          description=[
              "Fünf &6Stahlstäbe&r und drei &6Stahlgerüststufen&r ergeben sechs &6Stahllaufstege&r. &e24&r davon und &64 Stahlzäune&r in der Form aus dem Handbuch, dann Hammer drauf.",
              "",
              "&eRein:&r Holzlagerkisten (acht Behandelte Holzbretter im Kreis), Verstärkte Kisten oder Shulkerkisten per Rechtsklick. Jede Ebene hat ein eigenes Fenster. Ein Trichter vorne füllt zwei Kisten, an der Seite eine Reihe aus vier, von oben eine Säule aus drei.",
          ],
          tasks=[task_item("immersiveengineering:steel_catwalk", 24), task_checkmark("Kistenregal geformt")],
          rewards=[reward_item("immersiveengineering:crate", 4), reward_xp(10)],
          deps=["silo", "steel"], icon="immersiveengineering:crate", optional=True),

    quest("list_mb", 16.5, 21.5, "&6&lHak die Multiblöcke von Stufe 2 ab",
          subtitle="Sieben Strukturen, ein Hammer.",
          description=[
              "&6Koksofen:&r 3x3x3, 27 Koksziegel. Kohle rein, Koks und Kreosot raus.",
              "&6Roh-Hochofen:&r 3x3x3, 27 Sprengziegel. Eisen und Koks rein, Stahl und Schlacke raus.",
              "&6Legierungsofen:&r 2x2x2, 8 Legierungsziegel. Zwei Metalle rein, Legierung raus.",
              "&6Verbesserter Hochofen:&r 3x4x3, 27 Verstärkte Sprengziegel, ein Trichter.",
              "&6Tank:&r 3x5x3, 34 Blechblöcke, 4 Zäune. &6Silo:&r 3x7x3, 50 Blechblöcke, 4 Zäune.",
              "&6Kistenregal:&r 4x4x2, 24 Stahllaufstege, 4 Stahlzäune.",
              "",
              "Die großen Multiblöcke aus Ingenieursbausteinen folgen in Stufe 3.",
          ],
          tasks=[task_advancement("immersiveengineering:main/mb_cokeoven", "Koksofen"),
                 task_advancement("immersiveengineering:main/mb_blastfurnace", "Roh-Hochofen"),
                 task_checkmark("Legierungsofen"),
                 mb("mb_improvedblastfurnace", "Verbesserter Hochofen"),
                 mb("mb_tank", "Tank"),
                 mb("mb_silo", "Silo"),
                 task_checkmark("Kistenregal")],
          rewards=[reward_table("s2_uncommon"), reward_item("immersiveengineering:hammer", 1), reward_xp(15)],
          deps=["silo", "improved_form", "kiln"], icon="immersiveengineering:hammer", size=1.75, shape="gear"),

    # ---- neue Quests: Stahl ----------------------------------------------------
    quest("steel_armor", 28.5, 1.4, "&7Schmied eine Stahlrüstung",
          subtitle="Vier Teile aus 24 Stahlblechen.",
          description=[
              "&6Stahlbleche&r in der Form der Eisenrüstung ergeben &6Stahlhelm&r, &6Stahlharnisch&r, &6Stahlbeinschutz&r und &6Stahlstiefel&r. Für alle vier brauchst du &e24 Bleche&r.",
              "",
              "Sie hält mehr aus als Eisen und kostet dich nur Stahl aus dem Hochofen. Gut für die Zeit, bevor du an Diamanten oder bessere Rüstung kommst.",
          ],
          tasks=[task_item("immersiveengineering:armor_steel_helmet", 1), task_item("immersiveengineering:armor_steel_chestplate", 1),
                 task_item("immersiveengineering:armor_steel_leggings", 1), task_item("immersiveengineering:armor_steel_boots", 1)],
          rewards=[reward_item("immersiveengineering:plate_steel", 8), reward_xp(10)],
          deps=["steel_tools"], icon="immersiveengineering:armor_steel_chestplate", optional=True),

    # ---- neue Quests: Arbeitstisch ---------------------------------------------
    quest("charging_station", 18.5, 7.0, "&dBau eine Ladestation",
          subtitle="Strom rein, volle Werkzeuge raus.",
          description=[
              "Glas, &6Eisenblech&r, Glas oben, drei &6Vakuumröhren&r in der Mitte, &6Behandeltes Holz&r, &6Kupferspulenblock&r, Behandeltes Holz unten ergeben die &6Ladestation&r.",
              "",
              "Sie lädt jeden Gegenstand, der Strom speichert, mit bis zu &d256 FE/t&r. Strom kommt von unten oder von hinten, den Gegenstand legst du per Rechtsklick hinein oder schiebst ihn mit einem Trichter.",
              "",
              "Die Röhren vorne leuchten je nach Ladestand. Ein Komparator daneben gibt den Ladestand als Redstone-Signal aus.",
          ],
          tasks=[task_item("immersiveengineering:charging_station", 1)],
          rewards=[reward_item("immersiveengineering:electron_tube", 3), reward_xp(10)],
          deps=["electron_tube", "coil_lv"], icon="immersiveengineering:charging_station"),

    # ---- neue Quests: Wind und Draht -------------------------------------------
    quest("wire_insulated", 18.5, 15.0, "&6Isolier deine LV-Drähte",
          subtitle="Strom, der niemanden mehr verletzt.",
          description=[
              "Vier &6LV-Drahtspulen&r an die Seiten, fünf &6Robustes Gewebe&r in die Ecken und die Mitte ergeben vier &6Isolierte LV-Drahtspulen&r.",
              "",
              "Isolierter Draht trägt Strom wie Kupferdraht, verletzt aber niemanden, der ihn berührt. Nimm ihn überall, wo Spieler oder Tiere hinkommen: in der Basis, an Wegen, über der Weide.",
              "",
              "Er hängt an denselben LV-Anschlüssen und Relais, eine Strecke darf ebenfalls höchstens &e16 Blöcke&r lang sein.",
          ],
          tasks=[task_item("immersiveengineering:wirecoil_copper_ins", 8)],
          rewards=[reward_item("immersiveengineering:hemp_fiber", 16), reward_xp(5)],
          deps=["connectors", "hemp"], icon="immersiveengineering:wirecoil_copper_ins"),

    quest("post", 21, 11, "&6Stell Holzpfosten für deine Leitungen",
          subtitle="Vier Blöcke hoch, mit Arm für den Draht.",
          description=[
              "Zwei &6Behandelte Holzzäune&r übereinander auf einem &6Steinziegel&r ergeben einen &6Holzpfosten&r.",
              "",
              "Ein Pfosten ist &e4 Blöcke&r hoch, also brauchst du so viel Platz darüber. Hammer auf eine Seite des obersten Blocks setzt einen Arm an. Daran hängst du Anschlüsse, Relais, Trafos oder Lampen.",
              "",
              "So läuft dein Netz über Köpfe und Wege hinweg, statt quer durch die Basis.",
          ],
          tasks=[task_item("immersiveengineering:treated_post", 4)],
          rewards=[reward_item("immersiveengineering:treated_fence", 8), reward_item("immersiveengineering:connector_lv_relay", 4)],
          deps=["connectors"], icon="immersiveengineering:treated_post"),

    quest("electric_lantern", 23.5, 13, "&eHäng Angetriebene Laternen auf",
          subtitle="Licht, und keine Monster im Umkreis.",
          description=[
              "Ein &6Eisenblech&r oben, Glasscheibe, &6Glühbirne&r, Glasscheibe in der Mitte, ein &6Kupferkabel&r unten ergeben die &6Angetriebene Laterne&r. Glühbirnen macht der Arbeitstisch mit der Blaupause Komponenten.",
              "",
              "Sie hängt direkt an einem LV-Draht und reicht den Strom weiter, du kannst also mehrere hintereinander verbinden. Sie zieht nur &d1 FE/t&r.",
              "",
              "&eDas Beste:&r Solange sie Strom hat, spawnen im Umkreis von &e32 Blöcken&r keine feindlichen Monster. Ein paar davon schützen eine ganze Basis.",
          ],
          tasks=[task_item("immersiveengineering:electric_lantern", 4)],
          rewards=[reward_item("immersiveengineering:wirecoil_copper", 8), reward_table("s2_common"), reward_xp(10)],
          deps=["connectors", "bench"], icon="immersiveengineering:electric_lantern"),

    quest("skyhook", 23.5, 15.2, "&bFahr mit dem Skyhook am Draht",
          subtitle="Deine Leitungen werden zur Seilbahn.",
          description=[
              "Drei &6Stahlbarren&r, eine &6Mechanische Eisenkomponente&r und zwei &6Holzgriffe&r ergeben den &6Ingenieursskyhook&r. Holzgriff: fünf Behandelte Stöcke und ein Kupferklumpen.",
              "",
              "Halt Rechtsklick gedrückt nahe einem Draht, und du hängst daran. Abwärts rollst du von selbst, aufwärts mit den Bewegungstasten. An Kreuzungen fährt er dorthin, wohin du schaust. Schleichen lässt dich los.",
              "",
              "&cAchtung:&r Unisolierte Drähte unter Strom verletzen dich auch am Skyhook. Für reine Seilbahnen nimm &6Hanfseile&r: vier Hanffasern um einen Stock ergeben vier Hanfdrahtspulen, ein Stück darf &e32 Blöcke&r lang sein.",
          ],
          tasks=[task_item("immersiveengineering:skyhook", 1), task_item("immersiveengineering:wirecoil_structure_rope", 8)],
          rewards=[reward_item("immersiveengineering:hemp_fiber", 16), reward_xp(10)],
          deps=["connectors", "steel"], icon="immersiveengineering:skyhook", optional=True),

    quest("glider", 13.5, 11, "&bBau einen Faltgleiter",
          subtitle="Flügel aus Hanf und Aluminium.",
          description=[
              "Ein &6Robustes Gewebe&r oben, &6Aluminiumstab&r, &6Lederjacke&r, Aluminiumstab in der Mitte, Gewebe, Stab, Gewebe unten ergeben den &6Faltgleiter&r. Aluminium kommt aus &6Bauxit&r, zwei Barren übereinander ergeben vier Stäbe.",
              "",
              "Er gleitet wie eine Elytra, hält aber weniger aus und nimmt keine Verzauberungen. Sturzflüge und Raketen schaden ihm stärker. Repariert wird er mit Robustem Gewebe.",
          ],
          tasks=[task_item("immersiveengineering:glider", 1)],
          rewards=[reward_item("immersiveengineering:hemp_fabric", 4), reward_xp(10)],
          deps=["sails"], icon="immersiveengineering:glider", optional=True),

    # ---- neue Quests: Lager und Transport --------------------------------------
    quest("conveyor_special", 6, 23.5, "&7Bau Spezialförderbänder",
          subtitle="Aufteilen, fallen lassen, herausziehen.",
          description=[
              "&6Spaltförderband:&r drei Förderbänder und ein Eisenbarren ergeben drei. Es schickt Gegenstände abwechselnd nach links und rechts.",
              "&6Dropper-Förderband:&r ein Förderband über einem Eisenblech. Durch die Klappe fällt alles nach unten, auch in ein Inventar darunter. Redstone schließt die Klappe.",
              "&6Extrahierendes Förderband:&r ein &6Streifenvorhang&r, ein Einfacher Ingenieursbaustein und ein Förderband. Es zieht wie ein Trichter aus dem Inventar dahinter. Das Tempo stellst du mit dem &6Schraubendreher&r ein (Eisenstab und Stock).",
              "",
              "Ein Förderband über einer &6Redstonefackel&r bleibt bei Redstone-Signal stehen.",
          ],
          tasks=[task_item("immersiveengineering:conveyor_splitter", 3), task_item("immersiveengineering:conveyor_dropper", 1),
                 task_item("immersiveengineering:conveyor_extract", 1)],
          rewards=[reward_item("immersiveengineering:conveyor_basic", 8), reward_xp(5)],
          deps=["conveyor", "basic_engineering"], icon="immersiveengineering:conveyor_splitter"),

    quest("sorter", 8.5, 23.5, "&9Sortier mit dem Element-Router",
          subtitle="Sechs Seiten, jede mit eigenem Filter.",
          description=[
              "Eine &6Mechanische Eisenkomponente&r oben, ein &6Einfacher Ingenieursbaustein&r, ein &6Förderband&r unten ergeben den &6Element-Router&r.",
              "",
              "Jede Seite hat eine Farbe und eigene Filterplätze. Was hineinkommt, geht an eine Seite, deren Filter passt, sonst an eine Seite ohne Filter. Passt gar nichts, nimmt er es nicht an.",
              "",
              "Knöpfe über jedem Filter: nach Tag filtern (alle Erze, alle Barren), Haltbarkeit ignorieren, Verzauberungen beachten. Der &6Flüssigkeitsrouter&r macht dasselbe mit Flüssigkeiten, mit einem Flüssigkeitsrohr statt des Förderbands.",
          ],
          tasks=[task_item("immersiveengineering:sorter", 1)],
          rewards=[reward_item("immersiveengineering:basic_engineering", 2), reward_xp(5)],
          deps=["conveyor", "basic_engineering"], icon="immersiveengineering:sorter"),

    quest("barrel", 11, 23.5, "&9Stell Fässer für Flüssigkeiten auf",
          subtitle="12 Eimer in einem Block.",
          description=[
              "&6Holzfass:&r drei Behandelte Holzstufen über fünf Behandelten Holzbrettern, die Mitte frei. Es fasst &e12 Eimer&r, aber keine heißen Flüssigkeiten und keine Gase.",
              "&6Metallfass:&r drei Eisenblechstufen über fünf Eisenblechblöcken. Gleich groß, nimmt aber auch heiße Flüssigkeiten und Gase, und ein Redstone-Signal schaltet seine Ausgabe ab.",
              "",
              "Mit dem Hammer stellst du die Seiten auf Eingang oder Ausgang. Gut als Puffer neben Koksofen, Pumpe und Maschinen, wenn ein ganzer Tank zu groß ist.",
          ],
          tasks=[task_item("immersiveengineering:wooden_barrel", 1), task_item("immersiveengineering:metal_barrel", 1)],
          rewards=[reward_item("immersiveengineering:treated_wood_horizontal", 16), reward_xp(5)],
          deps=["tank"], icon="immersiveengineering:wooden_barrel"),
]

images = [
    banner("immersive/title", "Immersive Engineering", 13, -5, height=1.5, kind="title", colour="brass"),
    banner("immersive/basics", "Grundlagen", 1.2, 1.8, height=0.9, colour="stone"),
    banner("immersive/coke", "Koks und Kreosot", 6.0, -2.3, height=0.9, colour="brass"),
    banner("immersive/steel", "Stahl", 22, -2.8, height=0.9, colour="fire"),
    banner("immersive/alloys", "Legierungen", 8, 3.6, height=0.9, colour="brass"),
    banner("immersive/bench", "Arbeitstisch", 17.2, 3.85, height=0.9, colour="stone"),
    banner("immersive/power", "Wind und Draht", 10, 10.4, height=0.9, colour="water"),
    banner("immersive/mv", "Mittelspannung", 10.5, 17.2, height=0.9, colour="water"),
    banner("immersive/storage", "Lager und Transport", 10, 20.3, height=0.9, colour="stone"),
]

chapter(C, "Immersive Engineering", "immersiveengineering:hammer", "tech", quests, shape="square", order=14, stage=2,
        subtitle=["Stufe 2: Koksofen, Stahl, Legierungen, Wind und Draht, Tank und Silo."],
        images=images)
