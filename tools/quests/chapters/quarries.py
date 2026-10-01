"""Quarries in stage 4, one step per quest: the RFTools Builder with its shape cards (base,
quarry, clearing, fortune, silk, void, pump) and the machine infuser, Quarry Plus (Additional
Enchanted Miner, mod id quarryplus) with markers, Y setter, enchantment mover, modules and the
Chunk Destroyer, pointers to the other area miners (Mekanism digital miner, Create Ore
Excavation with its stage 4 netherite drill, the Oritech destroyer), chunk loading and power.
Builder numbers from config/rftoolsbuilder-server.toml, recipes from the jars."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner)

C = "quarries"


def head(name, text, left, y, height=0.9, kind="section", colour="stone"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- RFTools Builder ----------------------------------------------------------
    quest("welcome", 0, 2, "&6&lBau einen Builder",
          subtitle="Graben, ohne selbst zu graben.",
          description=[
              "Ein &6Machine Frame&r von RFTools Base in die Mitte, &6Ziegelblöcke&r in die Ecken, oben eine &6Enderperle&r, an den Seiten und unten &6Redstone&r.",
              "",
              "Mit &6Stufe 4&r öffnen zwei Mods, die ganze Gebiete abbauen: der &6Builder&r von RFTools und &6Quarry Plus&r. Der Builder ist ein Werkzeugkasten: mit einer Formkarte baut er ab, pumpt, räumt oder setzt Blöcke.",
              "",
              "&eStrom:&r Er speichert 1 000 000 RF und nimmt bis zu &d20 000 RF/t&r an. Ein abgebauter Block kostet ab 300 RF, je nach Härte mehr.",
          ],
          tasks=[task_item("rftoolsbuilder:builder", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_table("s4_common"), reward_xp(10)],
          icon="rftoolsbuilder:builder", size=2.0, shape="hexagon"),

    quest("shape_card", 2.5, 2, "&7Bau eine Formkarte",
          subtitle="Sag dem Builder, wo.",
          description=[
              "&6Papier&r in die Ecken, &6Ziegel&r oben und unten, &6Redstone&r links und rechts, &6Eisen&r in die Mitte.",
              "",
              "Im Fenster der Karte stellst du Form, Größe und Abstand ein. Schneller: Karte in der Hand, Schleich-Rechtsklick auf den Builder, dann Rechtsklick auf zwei gegenüberliegende Ecken. Bis &e512&r Blöcke pro Seite, bis &e260&r Blöcke vom Builder weg.",
              "",
              "Die leere Karte baut nichts ab. Sie ist die Grundlage aller anderen.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_def", 2)],
          rewards=[reward_item("minecraft:paper", 16), reward_xp(5)],
          deps=["welcome"], icon="rftoolsbuilder:shape_card_def"),

    quest("quarry_card", 5, 2, "&6&lBau eine Steinbruchkarte",
          subtitle="Der Builder wird zum Bagger.",
          description=[
              "Die &6Formkarte&r in die Mitte, oben eine &6Diamantspitzhacke&r, unten eine &6Diamantschaufel&r, &6Eisen&r links und rechts, &6Redstone&r in die Ecken.",
              "",
              "Damit baut der Builder alles im Bereich ab und setzt an jede Stelle Erde, damit kein riesiges Loch bleibt.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_table("s4_common"), reward_xp(10)],
          deps=["shape_card"], icon="rftoolsbuilder:shape_card_quarry", size=1.5, shape="hexagon"),

    quest("first_dig", 7.5, 2, "&6Lass den Builder graben",
          subtitle="Karte rein, Truhe dran, Strom an.",
          description=[
              "Steck die Steinbruchkarte in den Builder, stell eine Truhe oder einen Importbus von AE2 direkt daran und gib ihm Strom.",
              "",
              "Grundwert: &e8 Blöcke pro Tick&r, solange der Strom reicht. Er lädt den Chunk, in dem er gerade gräbt, selbst. Sein eigener Chunk muss geladen sein.",
              "",
              "&cAchtung:&r Er baut auch Truhen, Maschinen und Spawner ab. Bereich prüfen, nie in fremden Basen graben.",
          ],
          tasks=[task_checkmark("Mein Builder gräbt")],
          rewards=[reward_item("minecraft:chest", 4), reward_xp(10)],
          deps=["quarry_card"], icon="minecraft:chest"),

    quest("clearing", 10, 1, "&7Bau eine Räumende Karte",
          subtitle="Luft statt Erde.",
          description=[
              "Die Steinbruchkarte, umringt von acht &6Glasblöcken&r. Sie lässt Luft zurück. Gut für Keller, Halle oder Becken.",
              "",
              "Mit acht Erdblöcken drumherum wird sie wieder zur normalen Karte.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_clear", 1)],
          rewards=[reward_item("minecraft:glass", 16), reward_xp(5)],
          deps=["first_dig"], icon="rftoolsbuilder:shape_card_quarry_clear"),

    quest("void", 12.5, 1, "&8Bau eine Leerenkarte",
          subtitle="Weg damit.",
          description=[
              "&6Formkarte&r, &6Obsidian&r, &6schwarzer Farbstoff&r. Sie löscht alle Blöcke im Bereich und kostet nur &edie Hälfte&r des Stroms.",
              "",
              "Gut zum Einebnen eines Bergs. Für Erz nimm lieber die Steinbruchkarte.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_void", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(5)],
          deps=["clearing"], icon="rftoolsbuilder:shape_card_void", optional=True),

    quest("fortune", 10, 3, "&aBau eine Glückskarte",
          subtitle="Mehr Erz pro Block.",
          description=[
              "Die Steinbruchkarte in die Mitte, &6Dimensionsscherben&r in die Ecken, dazu &6Ghast-Träne&r, &6Smaragd&r, &6Diamant&r und &6Redstone&r. Sie baut ab wie eine Spitzhacke mit Glück.",
              "",
              "Jeder Block kostet &edoppelt&r so viel Strom. Dimensionsscherben findest du als Erz in allen drei Dimensionen.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_fortune", 1)],
          rewards=[reward_item("rftoolsbase:dimensionalshard", 16), reward_xp(10)],
          deps=["first_dig"], icon="rftoolsbuilder:shape_card_quarry_fortune"),

    quest("silk", 12.5, 3, "&bBau eine Behutsamkeitskarte",
          subtitle="Erze als Block.",
          description=[
              "Steinbruchkarte, &6Dimensionsscherben&r, &6Diamanten&r und ein &6Netherstern&r. Jeder Block kommt zurück, wie er war.",
              "",
              "&edreimal&r so viel Strom. Lohnt sich, wenn du Erzblöcke in Mekanism vervierfachst. Beide Karten gibt es auch räumend.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_silk", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(10)],
          deps=["fortune"], icon="rftoolsbuilder:shape_card_quarry_silk", optional=True),

    quest("pump", 7.5, 4, "&9Bau eine Pumpkarte",
          subtitle="Wasser und Lava aus dem Bereich.",
          description=[
              "Die &6Formkarte&r in die Mitte, oben ein &6Wassereimer&r, unten ein &6Lavaeimer&r, links und rechts ein leerer &6Eimer&r, &6Redstone&r in die Ecken.",
              "",
              "Der Builder saugt damit Flüssigkeiten aus dem Bereich. Jede kostet 300 RF. Gut für einen Lavasee im Nether.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_pump", 1)],
          rewards=[reward_item("minecraft:bucket", 4), reward_xp(5)],
          deps=["first_dig"], icon="rftoolsbuilder:shape_card_pump", optional=True),

    quest("infuser", 5, 4, "&dInfundier den Builder",
          subtitle="Scherben für Tempo.",
          description=[
              "Leg den Builder mit &6Dimensionsscherben&r in den &6Machine Infuser&r von RFTools Base. Er wird Stück für Stück infundiert.",
              "",
              "Voll ist er nach &e256 Scherben&r. Dann braucht er weniger Strom und gräbt bis zu &e20&r Blöcke pro Tick mehr. Der Infuser zieht 600 RF/t.",
          ],
          tasks=[task_item("rftoolsbase:machine_infuser", 1), task_item("rftoolsbase:dimensionalshard", 64)],
          rewards=[reward_item("rftoolsbase:dimensionalshard", 32), reward_xp(10)],
          deps=["quarry_card"], icon="rftoolsbase:machine_infuser", optional=True),

    # ---- Quarry Plus ----------------------------------------------------------------
    quest("markers", 0, 8, "&9Steck einen Bereich mit Markern ab",
          subtitle="Ein Rechteck auf dem Boden.",
          description=[
              "&6Marker Plus:&r Glowstone und Lapis um eine Redstone-Fackel. Setz einen an jede Ecke des Bereichs und klick sie an, bis sie sich verbinden. Der Chat sagt, ob es geklappt hat.",
              "",
              "&6Quarry Plus&r arbeitet wie die alten BuildCraft-Steinbrüche: Rahmen um den Bereich, dann Schicht für Schicht nach unten.",
          ],
          tasks=[task_item("quarryplus:marker", 4)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["welcome"], icon="quarryplus:marker"),

    quest("chunk_marker", 0, 10, "&9Bau einen Chunk Marker",
          subtitle="Ein Block statt vier.",
          description=[
              "Oben drei &6Redstone&r, darunter drei &6Marker&r: ein &6Chunk Marker&r. Drei grüne Farbstoffe über drei Markern geben einen &6Flexible Marker&r.",
              "",
              "Bei beiden stellst du den Bereich im Fenster ein. Der Chunk Destroyer braucht einen davon.",
          ],
          tasks=[task_item("quarryplus:chunk_marker", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["markers"], icon="quarryplus:chunk_marker", optional=True),

    quest("quarry", 2.5, 8, "&9&lBau einen Quarry Plus",
          subtitle="Rahmen, Kopf, Loch.",
          description=[
              "&6Eisen&r, &6Obsidian&r, zwei &6Diamantspitzhacken&r, ein &6Spender&r, ein &6Redstone-Block&r und ein &6Marker&r.",
              "",
              "Stell ihn neben einen verbundenen Marker, dann übernimmt er den Bereich. Strom über FE-Kabel, die Beute geht an eine Truhe oder ein Rohr daneben.",
              "",
              "&cAchtung:&r Liegt ein Chunk eines anderen Teams im Bereich, bleibt er stehen.",
          ],
          tasks=[task_item("quarryplus:quarry", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["markers"], icon="quarryplus:quarry", size=1.75, shape="gear"),

    quest("y_setter", 5, 10, "&7Stell die Tiefe ein",
          subtitle="Y Setter und StatusChecker.",
          description=[
              "&6Quarry Y Setter:&r drei Glas oben, darunter &6Lapis, Marker, Lapis&r. Damit legst du fest, wie tief er gräbt. &6StatusChecker:&r dasselbe mit Eisen statt Lapis, er zeigt, was die Maschine gerade tut.",
              "",
              "Für Diamanten reicht es, bis knapp über das Grundgestein zu graben.",
          ],
          tasks=[task_item("quarryplus:y_setter", 1), task_item("quarryplus:status_checker", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["quarry"], icon="quarryplus:y_setter", optional=True),

    quest("mover", 5, 8, "&dVerzauber den Steinbruch",
          subtitle="Daher der Name.",
          description=[
              "Der &6Enchantment Mover&r (Ambosse, Obsidian, Eisen, Gold, Diamant, ein Marker) überträgt Verzauberungen von einer &6Diamantspitzhacke&r auf die Maschine.",
              "",
              "&6Effizienz&r macht ihn schneller, &6Haltbarkeit&r spart Strom, &6Glück&r und &6Behutsamkeit&r wirken wie an der Spitzhacke. Verzauber eine Spitzhacke so hoch du kannst und schieb eine nach der anderen hinüber.",
          ],
          tasks=[task_item("quarryplus:mover", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(10)],
          deps=["quarry"], icon="quarryplus:mover"),

    quest("modules", 7.5, 7, "&7Bau ein Void Module",
          subtitle="Was er sofort wegwirft.",
          description=[
              "Zwei &6Bücher&r, eine &6Enderperle&r und ein &6Marker&r, formlos. Rechtsklick öffnet seine Liste. Was darin steht, wirft der Steinbruch sofort weg.",
              "",
              "Bruchstein, Erde, Kies und Tiefenschiefer gehören hinein, sonst ist jede Truhe in Minuten voll.",
          ],
          tasks=[task_item("quarryplus:filter_module", 1)],
          rewards=[reward_item("minecraft:book", 4), reward_xp(5)],
          deps=["mover"], icon="quarryplus:filter_module"),

    quest("exp", 7.5, 9, "&aBau ein Exp Collect Module",
          subtitle="Die Erfahrung aus dem Erz.",
          description=[
              "Oben &6Enderperle, Trank, Enderperle&r, in der Mitte &6Marker, Heuballen, Trank&r, unten &6Goldblock, Heuballen, Goldblock&r.",
              "",
              "Es sammelt die Erfahrung, die abgebaute Erze fallen lassen.",
          ],
          tasks=[task_item("quarryplus:exp_module", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(10)],
          deps=["mover"], icon="quarryplus:exp_module", optional=True),

    quest("repeat", 10, 7, "&5Bau ein Faster Work Module",
          subtitle="Drachenatem für den Motor.",
          description=[
              "Im Rezept stecken &6Amethyst&r, &6Prismarinsplitter&r, ein &6Marker&r und &6Drachenatem&r.",
              "",
              "Drachenatem fängst du mit einer leeren Flasche aus der lila Wolke des Enderdrachen. Mehr Tempo heißt mehr Strom pro Sekunde, prüf deine Leitung.",
          ],
          tasks=[task_item("quarryplus:repeat_tick_module", 1)],
          rewards=[reward_item("minecraft:dragon_breath", 2), reward_xp(10)],
          deps=["modules"], icon="quarryplus:repeat_tick_module"),

    quest("bedrock", 10, 9, "&8Bau ein Remove Bedrock Module",
          subtitle="Durch den Boden der Welt.",
          description=[
              "Oben drei &6Obsidian&r, darunter zweimal &6Diamantblock, Marker, Diamantblock&r.",
              "",
              "Damit gräbt er auch durch das Grundgestein. Denk an alle, die unter dir im Nether oder in der Mining-Dimension bauen: das Loch bleibt.",
          ],
          tasks=[task_item("quarryplus:remove_bedrock_module", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(10)],
          deps=["exp"], icon="quarryplus:remove_bedrock_module", optional=True),

    quest("destroyer", 12.5, 8, "&6&lBau den Chunk Destroyer",
          subtitle="Ganze Chunks bis zum Grund.",
          description=[
              "Zwei &6Quarry Plus&r, &6Diamantblöcke&r, &6Smaragdblöcke&r, &6Enderaugen&r, ein &6Netherstern&r und ein &6Drachenkopf&r. Den Kopf findest du auf den Endschiffen.",
              "",
              "Den Bereich steckst du mit Chunk Marker oder Flexible Marker ab, im Fenster startest du ihn. Er ist teuer im Strom, plan eine eigene Leitung.",
              "",
              "&eKronwerke:&r Draconium gibt es nur im End. Ein Steinbruch auf einer abgelegenen Endinsel bringt Erz in Mengen für die &e1 000 Draconiumbarren&r von Stufe 4. Die Hauptinsel bleibt in Ruhe.",
          ],
          tasks=[task_item("quarryplus:adv_quarry", 1), task_item("draconicevolution:draconium_ingot", 64)],
          rewards=[reward_table("s4_rare"), reward_item("draconicevolution:draconium_ingot", 8), reward_xp(30)],
          deps=["repeat", "chunk_marker"], icon="quarryplus:adv_quarry", size=2.5, shape="gear"),

    # ---- Andere Wege --------------------------------------------------------------
    quest("miner", 0, 13.5, "&7Kennst du den Digitalen Miner?",
          subtitle="Mekanism sucht gezielt nach Erz.",
          description=[
              "Der &6Digitale Miner&r aus Stufe 3 baut nur ab, was in seinem Filter steht, und lässt den Rest liegen. Kein Loch, kein Rahmen.",
              "",
              "Rezept, Filter und Upgrades: Kapitel &dMekanism: Fortgeschritten&r. Er kennt kein Glück, also zurück in die Erzleiter damit.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="mekanism:digital_miner", optional=True),

    quest("coe", 2.5, 13.5, "&7Kennst du die Bohrmaschine?",
          subtitle="Create Ore Excavation, Erz ohne Ende.",
          description=[
              "Die &6Bohrmaschine&r steht über einer Erzader, bekommt einen Bohrer und Rotation und fördert Roherz, solange sie dreht. Die Adern sind auf Kronwerke unerschöpflich.",
              "",
              "Aufbau und Eisenbohrer: Kapitel &6Create: Erweiterungen&r. Hier kommt die Stufe-4-Seite dazu.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="createoreexcavation:drill", optional=True),

    quest("coe_netherite", 5, 13.5, "&6Bau einen Netheritbohrer",
          subtitle="Für Netherit- und Diamantadern.",
          description=[
              "&6Diamantbohrer:&r ein Eisenbohrer mit &6Diamanten&r und einem &6Diamantblock&r. Am Schmiedetisch wird er mit Netherit zum &6Netheritbohrer&r.",
              "",
              "Nur der Netheritbohrer öffnet zwei Adern: &6Gehärteter Diamant&r (1 024 SU, 500 mB Lava, alle 20 Sekunden ein Rohdiamant, 10 Prozent Chance auf einen Diamanten dazu) und &6Netherit&r im Nether (2 048 SU, 1 000 mB Lava, alle 200 Sekunden, 20 Prozent Antiker Schutt).",
          ],
          tasks=[task_item("createoreexcavation:netherite_drill", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(15)],
          deps=["coe"], icon="createoreexcavation:netherite_drill"),

    quest("oritech", 7.5, 13.5, "&7Kennst du den Zerstörer?",
          subtitle="Oritech gräbt unter einem Rahmen.",
          description=[
              "Der &6Zerstörer Block&r von Oritech fährt auf einem Rahmen bis 64 Blöcke Seitenlänge und baut die Schicht darunter ab. Mit dem Mine-Add-On wird er zum Steinbruch.",
              "",
              "Rahmen, Zerstörer und Add-Ons: Kapitel &6Oritech&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="oritech:destroyer_block", optional=True),

    # ---- Drumherum ------------------------------------------------------------------
    quest("chunkload", 0, 17, "&eHalt den Steinbruch geladen",
          subtitle="Kein Spieler, kein Steinbruch.",
          description=[
              "Öffne mit &eM&r die Karte, beanspruche den Chunk der Maschine und ihres Lagers und lade ihn zwangsweise (Umschalt und Linksklick). Jedes Team hat dafür höchstens &e25&r Chunks.",
              "",
              "Nicht den ganzen Abbaubereich nehmen. Steht ein ME-Netz am Steinbruch, hält der &6Raumanker&r aus dem Kapitel Applied Energistics 2: Fortgeschritten das ganze Netz wach.",
          ],
          tasks=[task_checkmark("Ich habe den Chunk meines Steinbruchs beansprucht und zwangsgeladen")],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(5)],
          deps=["quarry"], icon="minecraft:map"),

    quest("power", 2.5, 17, "&cLeg Strom zum Steinbruch",
          subtitle="Steinbrüche sind hungrig.",
          description=[
              "Bring den Strom über &6Elite-Universalkabel&r von Mekanism, einen Energie-P2P-Tunnel von AE2 (kostet 2,5 Prozent) oder einen Generator vor Ort. Ein Energiewürfel direkt an der Maschine puffert Spitzen.",
              "",
              "Ein Builder mit Glückskarte oder ein Quarry Plus mit Effizienz V frisst mehr als die meisten Maschinen deiner Basis.",
          ],
          tasks=[task_item("mekanism:elite_universal_cable", 16)],
          rewards=[reward_item("mekanism:alloy_reinforced", 8), reward_xp(5)],
          deps=["quarry"], icon="mekanism:elite_universal_cable"),
]

images = [
    head("title", "Steinbrüche", 0, -2.4, height=1.5, kind="title", colour="brass"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.1, height=0.55, kind="note", colour="end"),
    head("builder", "RFTools Builder", 2.5, 0.0, colour="stone"),
    head("quarryplus", "Quarry Plus", 0, 6.4, colour="water"),
    head("other", "Andere Wege", 0, 12.0, colour="brass"),
    head("around", "Drumherum", 0, 15.5, colour="fire"),
]

chapter(C, "Steinbrüche", "quarryplus:quarry", "tech", quests, shape="square", order=37, stage=4,
        subtitle=["Stufe 4: der RFTools Builder, Quarry Plus, die anderen Wege und alles, was sie am Laufen hält."],
        images=images)
