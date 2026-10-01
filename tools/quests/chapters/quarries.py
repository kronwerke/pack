"""Quarries in stage 4: the RFTools Builder with shape cards (quarry, clearing, fortune, silk,
void) and the machine infuser, Quarry Plus (Additional Enchanted Miner, mod id quarryplus)
with markers, the enchantment mover, modules and the Chunk Destroyer, plus chunk loading,
power and the server goal. Builder numbers come from the server config rftoolsbuilder-server.toml."""
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
    quest("welcome", 0, 2, "&6&lSteinbrüche",
          subtitle="Graben, ohne selbst zu graben.",
          description=[
              "Mit &6Stufe 4, dem Sternwerk&r, öffnen zwei Mods, die ganze Gebiete abbauen: der &6Builder&r von RFTools Builder und &6Quarry Plus&r (die Mod heißt auch Additional Enchanted Miner).",
              "",
              "Der &6Builder&r ist ein Werkzeugkasten. Mit einer Formkarte baut er ab, pumpt, räumt weg oder setzt Blöcke. Er gräbt schnell, aber ohne Verzauberungen nur so, wie die Karte es sagt.",
              "",
              "&eRezept:&r ein &6Machine Frame&r von RFTools Base in die Mitte, Ziegelblöcke in die Ecken, oben eine Enderperle, an den Seiten und unten Redstone.",
              "",
              "&eStrom:&r Der Builder speichert 1 000 000 RF und nimmt bis zu &d20 000 RF/t&r an. Ein abgebauter Block kostet ab 300 RF, je nach Härte mehr.",
          ],
          tasks=[task_item("rftoolsbuilder:builder", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_table("s4_common"), reward_xp(10)],
          icon="rftoolsbuilder:builder", size=2.0, shape="hexagon"),

    quest("shape_card", 2.5, 2, "&7Formkarten",
          subtitle="Sag dem Builder, wo.",
          description=[
              "Die &6Shape Card&r (Papier, Ziegel, Eisen, Redstone) beschreibt einen Bereich. In ihrem Fenster stellst du Form (Quader, Kugel, Zylinder und mehr), Größe und Abstand zum Builder ein.",
              "",
              "&eMarkieren geht schneller:&r Mit der Karte in der Hand Schleich-Rechtsklick auf den Builder, dann Rechtsklick auf zwei gegenüberliegende Ecken des Bereichs. Danach steckst du die Karte in den Builder.",
              "",
              "Ein Bereich darf bis zu &e512&r Blöcke pro Seite groß sein und bis zu &e260&r Blöcke vom Builder entfernt liegen. Die leere Karte selbst baut nichts ab, sie ist die Grundlage für alle anderen.",
              "",
              "Der &6Composer&r setzt mehrere Formen zu einer zusammen, dreht und spiegelt sie. Für einen Steinbruch brauchst du ihn nicht.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_def", 2)],
          rewards=[reward_item("minecraft:paper", 16), reward_xp(5)],
          deps=["welcome"], icon="rftoolsbuilder:shape_card_def"),

    quest("quarry_card", 5, 2, "&6&lSteinbruchkarte",
          subtitle="Der Builder wird zum Bagger.",
          description=[
              "Formkarte, Diamantspitzhacke, Diamantschaufel, Eisen und Redstone ergeben die &6Shape Card (Quarry)&r. Damit baut der Builder alles im Bereich ab und setzt an jede Stelle einen Erdblock. So bleibt kein riesiges Loch zurück.",
              "",
              "&eWohin mit der Beute:&r Stell eine Truhe oder ein Fass direkt an den Builder. Besser ist ein Speicherbus oder Importbus von AE2 daran, dann geht alles gleich ins Netz.",
              "",
              "&eTempo:&r Grundwert sind &e8 Blöcke pro Tick&r, solange der Strom reicht. Auf diesem Server lädt der Builder beim Abbauen selbst die Chunks, in denen er gerade gräbt. Sein eigener Chunk muss aber geladen sein.",
              "",
              "&cAchtung:&r Er baut auch Blöcke mit Inhalt ab, Truhen, Maschinen und Spawner eingeschlossen. Prüf den Bereich, bevor du startest, und grab nie in fremden Basen.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_table("s4_common"), reward_xp(10)],
          deps=["shape_card"], icon="rftoolsbuilder:shape_card_quarry", size=1.5, shape="hexagon"),

    quest("clearing", 7.5, 1, "&7Räumende Karte",
          subtitle="Luft statt Erde.",
          description=[
              "Die Steinbruchkarte, umringt von acht Glasblöcken, wird zur &6Shape Card (Clearing Quarry)&r. Sie lässt Luft zurück statt Erde. Gut für einen Keller, eine Halle oder ein Becken.",
              "",
              "Willst du zurück zur Erde, umring die räumende Karte mit acht Erdblöcken.",
              "",
              "Für Flüssigkeiten gibt es eigene Karten: die &6Pumpkarte&r saugt Wasser und Lava aus dem Bereich, die Karte für flüssige Blöcke setzt welche hinein.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_clear", 1)],
          rewards=[reward_item("minecraft:glass", 16), reward_xp(5)],
          deps=["quarry_card"], icon="rftoolsbuilder:shape_card_quarry_clear"),

    quest("fortune", 7.5, 3, "&aGlück im Steinbruch",
          subtitle="Mehr Erz pro Block.",
          description=[
              "Die &6Shape Card (Fortune Quarry)&r baut ab, als hättest du eine Spitzhacke mit Glück. Rezept: die Steinbruchkarte in der Mitte, &6Dimensionsscherben&r von RFTools Base in den Ecken, dazu Ghast-Träne, Smaragd, Diamant und Redstone.",
              "",
              "Dimensionsscherben findest du als Erz in allen drei Dimensionen.",
              "",
              "&eKosten:&r Jeder Block braucht hier &edoppelt&r so viel Strom wie mit der normalen Karte.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_fortune", 1)],
          rewards=[reward_item("rftoolsbase:dimensionalshard", 16), reward_xp(10)],
          deps=["quarry_card"], icon="rftoolsbuilder:shape_card_quarry_fortune"),

    quest("silk", 10, 3, "&bBehutsamer Steinbruch",
          subtitle="Erze als Block.",
          description=[
              "Die &6Shape Card (Silk Quarry)&r gibt jeden Block so zurück, wie er war, also Erze als Erzblöcke. Das lohnt sich, wenn du sie mit Mekanism verdreifachst oder vervierfachst.",
              "",
              "&eRezept:&r Steinbruchkarte, Dimensionsscherben, Diamanten und ein &6Netherstern&r.",
              "",
              "&eKosten:&r &edreimal&r so viel Strom pro Block. Es gibt beide Karten auch in der räumenden Version.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_quarry_silk", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(10)],
          deps=["fortune"], icon="rftoolsbuilder:shape_card_quarry_silk", optional=True),

    quest("void", 10, 1, "&8Leerenkarte",
          subtitle="Weg damit.",
          description=[
              "Die &6Shape Card (Void)&r (Formkarte, Obsidian, schwarzer Farbstoff) löscht alle Blöcke im Bereich, ohne etwas zurückzugeben. Sie kostet nur &edie Hälfte&r des Stroms.",
              "",
              "Gut zum Einebnen eines Bergs, wenn dich der Stein nicht interessiert. Für Erz nimm lieber eine Steinbruchkarte und wirf Bruchstein über einen Kondensator weg, dann gibt er dir noch Materiebälle.",
          ],
          tasks=[task_item("rftoolsbuilder:shape_card_void", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(5)],
          deps=["clearing"], icon="rftoolsbuilder:shape_card_void", optional=True),

    quest("infuser", 5, 4.25, "&dInfusion",
          subtitle="Scherben für Tempo.",
          description=[
              "Der &6Machine Infuser&r von RFTools Base verbessert Maschinen mit &6Dimensionsscherben&r. Leg den Builder und die Scherben hinein, und er wird Stück für Stück infundiert.",
              "",
              "Ein voll infundierter Builder braucht weniger Strom und gräbt schneller: Zu den 8 Blöcken pro Tick kommen bis zu &e20&r dazu. Voll ist er nach &e256 Scherben&r.",
              "",
              "Der Infuser selbst braucht 600 RF/t, solange er arbeitet.",
          ],
          tasks=[task_item("rftoolsbase:machine_infuser", 1), task_item("rftoolsbase:dimensionalshard", 64)],
          rewards=[reward_item("rftoolsbase:dimensionalshard", 32), reward_xp(10)],
          deps=["quarry_card"], icon="rftoolsbase:machine_infuser", optional=True),

    # ---- Quarry Plus ----------------------------------------------------------------
    quest("markers", 0, 8, "&9Marker Plus",
          subtitle="Ein Rechteck auf dem Boden.",
          description=[
              "&6Quarry Plus&r arbeitet wie die alten BuildCraft-Steinbrüche: Du steckst einen Bereich ab, die Maschine baut einen Rahmen und gräbt darin bis nach unten.",
              "",
              "&6Marker Plus&r (Glowstone, Lapis, Redstone-Fackel) setzt du an die Ecken des Bereichs und klickst sie an, bis sie sich verbinden. Der Chat sagt dir, ob es geklappt hat.",
              "",
              "Aus drei Markern und Redstone wird ein &6Chunk Marker&r, mit grünem Farbstoff ein &6Flexible Marker&r. Bei beiden stellst du den Bereich im Fenster ein statt mit mehreren Blöcken.",
          ],
          tasks=[task_item("quarryplus:marker", 4)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["welcome"], icon="quarryplus:marker"),

    quest("quarry", 2.5, 8, "&9&lQuarry Plus",
          subtitle="Rahmen, Kopf, Loch.",
          description=[
              "Der &6Quarry Plus&r braucht Eisen, Obsidian, zwei Diamantspitzhacken, einen Spender, einen Redstone-Block und einen Marker.",
              "",
              "Stell ihn direkt neben einen verbundenen Marker, dann übernimmt er dessen Bereich. Er baut zuerst einen Rahmen und gräbt dann mit seinem Kopf Schicht für Schicht nach unten. Die Beute gibt er an eine Truhe oder ein Rohr neben sich weiter.",
              "",
              "&eStrom:&r Er nimmt FE über Kabel an und braucht für Rahmen, Kopfbewegung und jeden Block Energie. Mit dem &6Quarry Y Setter&r legst du fest, wie tief er gräbt, mit dem &6StatusChecker&r siehst du, was er gerade tut.",
              "",
              "&cAchtung:&r Liegt ein Chunk im Bereich, den ein anderes Team beansprucht hat, bleibt er stehen.",
          ],
          tasks=[task_item("quarryplus:quarry", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["markers"], icon="quarryplus:quarry", size=1.75, shape="gear"),

    quest("mover", 5, 7, "&dVerzauberte Maschinen",
          subtitle="Daher der Name.",
          description=[
              "Quarry Plus wird erst mit Verzauberungen richtig gut. Der &6Enchantment Mover&r (Ambosse, Obsidian, Eisen, Gold, Diamant und ein Marker) überträgt sie von einer verzauberten &6Diamantspitzhacke&r auf die Maschine.",
              "",
              "&eWas geht:&r &6Effizienz&r macht ihn schneller, &6Haltbarkeit&r spart Strom, &6Glück&r und &6Behutsamkeit&r wirken wie an der Spitzhacke.",
              "",
              "&eTipp:&r Verzauber eine Spitzhacke so hoch, wie du kannst. Dann leg sie zusammen mit dem Steinbruch in den Mover und schieb eine Verzauberung nach der anderen hinüber.",
          ],
          tasks=[task_item("quarryplus:mover", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(10)],
          deps=["quarry"], icon="quarryplus:mover"),

    quest("modules", 5, 9, "&7Module",
          subtitle="Was er wegwirft und was er mitnimmt.",
          description=[
              "Module erweitern den Steinbruch.",
              "",
              "&6Void Module&r (zwei Bücher, Enderperle, Marker): Mit Rechtsklick öffnest du seine Liste. Was darin steht, wirft der Steinbruch sofort weg. Bruchstein, Erde, Kies und Tiefenschiefer gehören hinein, sonst ist jede Truhe in Minuten voll.",
              "",
              "&6Quarry Exp Collect Module&r sammelt die Erfahrung aus abgebauten Erzen. &6Quarry Pump Module&r pumpt Flüssigkeiten im Bereich ab. &6Remove Bedrock Module&r (Diamantblöcke, Obsidian) lässt ihn auch durch das Grundgestein graben.",
          ],
          tasks=[task_item("quarryplus:filter_module", 1)],
          rewards=[reward_item("minecraft:book", 4), reward_xp(5)],
          deps=["quarry"], icon="quarryplus:filter_module"),

    quest("repeat", 7.5, 9, "&5Faster Work Module",
          subtitle="Drachenatem für den Motor.",
          description=[
              "Das &6Faster Work Module&r lässt die Maschine schneller arbeiten. Im Rezept stecken Amethyst, Prismarinsplitter, ein Marker und &6Drachenatem&r.",
              "",
              "Drachenatem fängst du mit einer leeren Glasflasche aus der lila Wolke, die der Enderdrache ausspuckt. Auf diesem Server kämpft ihr gemeinsam gegen ihn, also nimm Flaschen mit.",
              "",
              "Mehr Tempo heißt auch mehr Strom pro Sekunde. Prüf vorher, ob deine Leitung das hergibt.",
          ],
          tasks=[task_item("quarryplus:repeat_tick_module", 1)],
          rewards=[reward_item("minecraft:dragon_breath", 2), reward_xp(10)],
          deps=["modules"], icon="quarryplus:repeat_tick_module"),

    quest("destroyer", 10, 8, "&6&lChunk Destroyer",
          subtitle="Ganze Chunks bis zum Grund.",
          description=[
              "Der &6Chunk Destroyer&r ist die große Schwester des Quarry Plus und für Bereiche gemacht, die über viele Chunks gehen.",
              "",
              "&eRezept:&r zwei Quarry Plus, Diamantblöcke, Smaragdblöcke, Enderaugen, ein &6Netherstern&r und ein &6Drachenkopf&r. Den Kopf findest du auf den Endschiffen in den Endstädten.",
              "",
              "Den Bereich steckst du mit einem &6Chunk Marker&r oder &6Flexible Marker&r ab. In seinem Fenster startest du ihn und kannst einstellen, ob er Chunk für Chunk arbeitet. Er ist teuer im Strom, plane eine eigene Leitung ein.",
              "",
              "&eKronwerke:&r Draconium gibt es nur noch im End. Ein Steinbruch auf einer abgelegenen Endinsel bringt Draconiumerz in Mengen, und der Obelisk will in Stufe 4 &e1 000 Draconiumbarren&r. Lass die Hauptinsel in Ruhe, dort kämpft der Server gegen den Drachen.",
          ],
          tasks=[task_item("quarryplus:adv_quarry", 1), task_item("draconicevolution:draconium_ingot", 64)],
          rewards=[reward_table("s4_rare"), reward_item("draconicevolution:draconium_ingot", 8), reward_xp(30)],
          deps=["mover", "repeat"], icon="quarryplus:adv_quarry", size=2.5, shape="gear"),

    # ---- Drumherum ------------------------------------------------------------------
    quest("chunkload", 2.5, 12, "&eGeladen bleiben",
          subtitle="Kein Spieler, kein Steinbruch.",
          description=[
              "Jede Maschine arbeitet nur, solange ihr Chunk geladen ist. Gehst du weg, steht der Steinbruch.",
              "",
              "&eFTB Chunks:&r Öffne mit &eM&r die Karte und beanspruche die Chunks deines Steinbruchs. Beanspruchte Chunks kannst du zusätzlich zwangsladen, mit gedrückter Umschalttaste und Linksklick. Jedes Team hat dafür höchstens &e25&r Chunks. Nimm nur den Chunk der Maschine und ihres Lagers, nicht den ganzen Abbaubereich.",
              "",
              "Der Builder lädt den Chunk, in dem er gerade gräbt, selbst. Steht ein ME-Netz am Steinbruch, hält der &6Raumanker&r aus dem Kapitel AE2: Fortgeschritten das ganze Netz wach.",
          ],
          tasks=[task_checkmark("Ich habe den Chunk meines Steinbruchs beansprucht und zwangsgeladen")],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(5)],
          deps=["quarry"], icon="minecraft:map"),

    quest("power", 5, 12, "&cStrom heranschaffen",
          subtitle="Steinbrüche sind hungrig.",
          description=[
              "Ein Builder mit Glückskarte oder ein Quarry Plus mit Effizienz V frisst mehr Strom als die meisten Maschinen deiner Basis.",
              "",
              "Steht der Steinbruch weit weg, bring den Strom über &6Elite-Universalkabel&r von Mekanism, einen Energie-P2P-Tunnel von AE2 (der kostet 2,5 Prozent) oder einen eigenen Generator vor Ort. Ein Energiewürfel direkt an der Maschine puffert Spitzen ab.",
              "",
              "&eTipp:&r Powah-Reaktoren oder ein Mekanism-Fusionsreaktor in Stufe 4 liefern genug für mehrere Steinbrüche gleichzeitig.",
          ],
          tasks=[task_item("mekanism:elite_universal_cable", 16)],
          rewards=[reward_item("mekanism:alloy_reinforced", 8), reward_xp(5)],
          deps=["quarry"], icon="mekanism:elite_universal_cable"),
]

images = [
    head("title", "Steinbrüche", 0, -2.4, height=1.5, kind="title", colour="brass"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.1, height=0.55, kind="note", colour="end"),
    head("builder", "RFTools Builder", 1.6, 0.2, colour="stone"),
    head("quarryplus", "Quarry Plus", -0.6, 6.4, colour="water"),
    head("around", "Drumherum", 1.6, 10.6, colour="fire"),
]

chapter(C, "Steinbrüche", "quarryplus:quarry", "tech", quests, shape="square", order=37, stage=4,
        subtitle=["Stufe 4: der RFTools Builder, Quarry Plus und alles, was sie am Laufen hält."],
        images=images)
