"""Exploration in stage 1: the map and Nature's Compass, villages and bounties, waystones and their
items, the mining world (a server of its own: the Grubenrahmen portal of Kronwerke Core,
kubejs/server_scripts/grubenrahmen.js, reset every three days), and a checklist of the overworld structures of the pack: Lootr, Artifacts
campsites and mimics, the YUNG's mods, Towns and Towers, Dungeons and Taverns (with the quest
trader of the taverns), When Dungeons Arise, Formations Overworld and Explorify. Bosses point to
bosses.py, affix gear to apotheosis.py, the other dimensions to list_dimensions.py and their own
chapters. Costs from waystones-common.toml, campsite numbers from artifacts/general.toml."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "exploration"
FRAME = "kronwerke:grubenrahmen"
MINING_ADV = "kronwerke:minenwelt"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    quest("welcome", 0, 0, "&6&lZieh los und erkunde",
          subtitle="Die Welt ist größer und seltsamer als in Vanilla.",
          description=[
              "Hak ab und zieh los. Die Quests hier zeigen dir, wie du dich zurechtfindest, schnell reist, in der Minenwelt gräbst und was in den Bauwerken wartet.",
              "",
              "&6Terralith&r und &6Biomes O' Plenty&r bringen Dutzende neue Biome, &6Tectonic&r höhere Berge und tiefere Täler. Dazwischen stehen Bauwerke aus einem Dutzend Mods.",
              "",
              "&eGut zu wissen:&r Beute in Bauwerken gibt es für jeden Spieler einzeln. Wer als Zweiter kommt, geht nicht leer aus.",
          ],
          tasks=[task_checkmark("Ab nach draußen")],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_table("s1_common")],
          icon="minecraft:filled_map", size=2.5, shape="hexagon"),

    # ---- Orientierung ---------------------------------------------------------
    quest("e_map", 4.5, -8, "&6Öffne die Karte",
          subtitle="Nie wieder verlaufen.",
          description=[
              "Drück &eM&r für die Karte von &6FTB Chunks&r oder &eJ&r für JourneyMap. Beide zeichnen alles auf, was du gesehen hast.",
              "",
              "Setz dir &eWegpunkte&r an Basis, Erzfunden, Dörfern und Portalen. Mit &eF3&r siehst du deine Koordinaten, schreib sie auf, bevor du irgendwo hinabsteigst.",
          ],
          tasks=[task_checkmark("Karte angeschaut")],
          rewards=[reward_item("minecraft:bread", 8)],
          deps=["welcome"], icon="minecraft:map"),

    quest("e_biomes", 6.5, -8, "&aLies die Biomnamen",
          subtitle="Jedes Biom hat seine eigenen Pflanzen.",
          description=[
              "Lauf in ein neues Biom und lies den Namen, den &6Traveler's Titles&r einblendet.",
              "",
              "Neue Biome heißt neue Hölzer, Blumen und Pflanzen. Botania braucht Blumen in allen Farben, Farmer's Delight wilde Pflanzen: Tomaten im Warmen, Reis im seichten Wasser, Kohl an der Küste.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["e_map"], icon="minecraft:oak_sapling"),

    quest("e_compass", 8.5, -8, "&6Bau den Kompass der Natur",
          subtitle="Er zeigt dir den Weg zu jedem Biom.",
          description=[
              "Ein &6Kompass&r in der Mitte, &64 Holzstämme&r an den Seiten, &64 Setzlinge&r in den Ecken ergeben den &6Kompass der Natur&r.",
              "",
              "Rechtsklick öffnet die Liste aller Biome. Wähl eines, und er zeigt Richtung, Entfernung und Koordinaten des nächsten. Er nutzt sich nicht ab.",
          ],
          tasks=[task_item("naturescompass:naturescompass", 1)],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["e_biomes"], icon="naturescompass:naturescompass"),

    quest("e_archwood", 10.5, -8, "&dFinde einen Archwood-Wald",
          subtitle="Bunte Bäume voller Magie.",
          description=[
              "Such mit dem Kompass der Natur einen &dArchwood-Wald&r und hak ab, wenn du drin stehst.",
              "",
              "Die Bäume wachsen in vier Farben, jede gehört zu einer Schule von Ars Nouveau. Kein Wald in der Nähe? Am &6Markt&r von Farming for Blockheads kostet jeder Setzling einen Smaragd.",
          ],
          tasks=[task_checkmark("Gefunden")],
          rewards=[reward_item("minecraft:emerald", 4)],
          deps=["e_compass"], icon="ars_nouveau:blue_archwood_sapling"),

    quest("e_village", 12.5, -8, "&6Finde ein Dorf",
          subtitle="Handel, Betten und oft ein Wegstein.",
          description=[
              "Finde ein Dorf und hak ab. Dorfbewohner handeln mit &6Smaragden&r, die du für Warpstein, Markt und Tavernen brauchst.",
              "",
              "Viele Dörfer haben einen &6Wegstein&r und eine &6Belohnungstafel&r. Bau nicht mitten hinein und lass die Bewohner am Leben, mit ihnen handelt auch der Rest des Servers.",
          ],
          tasks=[task_checkmark("Ein Dorf gefunden")],
          rewards=[reward_item("minecraft:emerald", 4)],
          deps=["e_compass"], icon="minecraft:emerald"),

    quest("e_bounty", 14.5, -8, "&6Erfüll einen Auftrag",
          subtitle="Die Belohnungstafel zahlt in Smaragden.",
          description=[
              "Rechtsklick auf eine &6Belohnungstafel&r, nimm einen Auftrag, sammle, was verlangt wird, und klick die Tafel damit wieder an.",
              "",
              "Aufträge haben eine Frist. Ein &6Dekret&r legt fest, welche Art Aufträge eine Tafel anbietet. Keine Tafel im Dorf? Bau eine aus Eichenbrettern, Eichenstämmen, Papier und einem Diamanten.",
          ],
          tasks=[task_advancement("bountiful:bountiful/bounty_complete", "Einen Auftrag erfüllt")],
          rewards=[reward_table("s1_common")],
          deps=["e_village"], icon="bountiful:bountyboard"),

    # ---- Reisen ---------------------------------------------------------------
    quest("e_waystone_find", 4.5, -2.5, "&6Aktiviere einen Wegstein",
          subtitle="Einmal anklicken, immer wieder hinreisen.",
          description=[
              "Rechtsklick auf einen &6Wegstein&r aktiviert ihn. Von jedem Wegstein reist du zu allen, die du schon aktiviert hast.",
              "",
              "&eKosten auf Kronwerke:&r 1 Level pro 100 Blöcke, höchstens 27, in eine andere Dimension immer 27. Wilde Wegsteine stehen etwa alle 25 Chunks und in Dörfern. Aktiviere auch den am Spawn.",
          ],
          tasks=[task_checkmark("Einen Wegstein aktiviert")],
          rewards=[reward_item("waystones:warp_dust", 4)],
          deps=["welcome"], icon="waystones:waystone", size=1.5),

    quest("e_warp_dust", 7, -3.5, "&6Mach Warppulver",
          subtitle="Der Stoff, aus dem die Reisen sind.",
          description=[
              "Eine &6Enderperle&r und eine &6Amethystscherbe&r ergeben &e4 Warppulver&r.",
              "",
              pic("waystones:warp_dust"),
              "",
              "Perlen lassen Endermen fallen, Amethyst wächst in den Geoden tief unten. Das Pulver steckt im Warpstein und in der Warpplatte.",
          ],
          tasks=[task_item("waystones:warp_dust", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["e_waystone_find"], icon="waystones:warp_dust"),

    quest("e_warp_stone", 9, -3.5, "&6Bau einen Warpstein",
          subtitle="Reisen von überall aus.",
          description=[
              "Ein &6Smaragd&r in der Mitte, &64 Enderperlen&r an den Seiten, &64 Quelljuwelen&r aus Ars Nouveau in den Ecken ergeben den &6Warpstein&r.",
              "",
              pic("waystones:warp_stone"),
              "",
              "Halt Rechtsklick, bis er geladen ist, dann wählst du einen aktivierten Wegstein. Danach braucht er eine Abklingzeit, sie steht im Tooltip.",
          ],
          tasks=[task_item("waystones:warp_stone", 1)],
          rewards=[reward_item("waystones:return_scroll", 2)],
          deps=["e_warp_dust"], icon="waystones:warp_stone"),

    quest("e_own_waystone", 11, -3.5, "&6Stell einen Wegstein an die Basis",
          subtitle="Dein Zuhause, einen Klick entfernt.",
          description=[
              "Ein &6Warpstein&r in der Mitte, &63 Steinziegel&r darüber und daneben, &63 Obsidian&r als Sockel ergeben einen &6Wegstein&r.",
              "",
              "Gib ihm einen Namen, den andere wiedererkennen. Es gibt ihn auch bemoost, aus Sandstein, Tiefenschiefer und mehr, JEI zeigt alle Varianten.",
          ],
          tasks=[task_item("waystones:waystone", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(3)],
          deps=["e_warp_stone"], icon="waystones:waystone"),

    quest("e_return_scroll", 7, -1.5, "&6Pack eine Rückkehr-Schriftrolle ein",
          subtitle="Der schnelle Weg zurück, kostenlos.",
          description=[
              "&62 Goldnuggets&r, ein &6Tintenbeutel&r und &63 Papier&r ergeben drei &6Rückkehr-Schriftrollen&r. Jede bringt dich einmal zum nächsten aktivierten Wegstein.",
              "",
              pic("waystones:return_scroll"),
              "",
              "Reisen mit Schriftrollen kosten auf Kronwerke keine Level. Eine gehört in jede Tasche, die in eine Höhle geht.",
          ],
          tasks=[task_item("waystones:return_scroll", 1)],
          rewards=[reward_item("minecraft:paper", 6)],
          deps=["e_waystone_find"], icon="waystones:return_scroll"),

    quest("e_warp_scroll", 9, -1.5, "&6Schreib eine Warp-Schriftrolle",
          subtitle="Einmal reisen, freie Zielwahl.",
          description=[
              "Goldnuggets, ein Tintenbeutel, eine &6Enderperle&r und Papier ergeben drei &6Warp-Schriftrollen&r. Jede öffnet einmal die Auswahl aller deiner Wegsteine.",
              "",
              pic("waystones:warp_scroll"),
              "",
              "Praktisch, solange der Warpstein fehlt oder abklingt.",
          ],
          tasks=[task_item("waystones:warp_scroll", 1)],
          rewards=[reward_item("minecraft:paper", 6), reward_xp(3)],
          deps=["e_return_scroll"], icon="waystones:warp_scroll"),

    quest("e_sharestone", 11, -1.5, "&6Verbinde euch mit Teilsteinen",
          subtitle="Ein Netz für alle in einer Farbe.",
          description=[
              "&63 Steinziegel&r, &62 Farbstoffe&r, ein &6Warpstein&r und &63 Obsidian&r ergeben einen &6Teilstein&r.",
              "",
              "Alle Teilsteine derselben Farbe sind verbunden, und jeder Spieler kann sie benutzen. Gut für ein Team oder die Strecke zwischen euren Basen und dem Spawn.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["e_warp_scroll"], icon="waystones:purple_sharestone", optional=True),

    quest("e_warp_plate", 13, -1.5, "&6Leg zwei Warpplatten",
          subtitle="Draufstellen und weg.",
          description=[
              "Bau &e2 Warpplatten&r. Leg einen &6Ruhenden Splitter&r (2 Warppulver, Feuerstein) in die erste, nimm den eingestellten Splitter heraus und leg ihn in die zweite.",
              "",
              "Ab dann bringt dich jede Platte zur anderen, kostenlos. Gut für feste Wege, etwa von der Basis zur Mine.",
          ],
          tasks=[task_item("waystones:warp_plate", 2)],
          rewards=[reward_item("waystones:warp_dust", 4), reward_xp(5)],
          deps=["e_sharestone"], icon="waystones:warp_plate", optional=True),

    # ---- Minenwelt -----------------------------------------------------------
    quest("e_pickaxe", 4.5, 3, "&6Bau zehn Grubenrahmen",
          subtitle="Der Rahmen für das Tor zur Minenwelt.",
          description=[
              "&eRezept:&r &64 Andesit-Gehäuse&r, &64 Infundiertes Eisen&r und ein &6Quellstein&r in der Mitte ergeben &e2 Grubenrahmen&r. Für ein Portal brauchst du &e10&r.",
              "",
              "Die &6Minenwelt&r ist eine eigene Welt zum Graben. Dort darfst du Löcher machen, so viel du willst, und die Oberwelt bleibt schön.",
          ],
          tasks=[task_item(FRAME, 10)],
          rewards=[reward_item("minecraft:iron_block", 2)],
          deps=["welcome"], icon=FRAME, size=1.5),

    quest("e_frame", 7, 3, "&6Entzünde das Minenportal",
          subtitle="Wie ein Netherportal, nur aus Grubenrahmen.",
          description=[
              "Bau einen Rahmen aus &6Grubenrahmen&r, 4 breit und 5 hoch, innen 2 mal 3 frei. Ohne Ecken reichen &e10&r. Größer geht auch, bis 21 mal 21.",
              "",
              "Dann Rechtsklick mit einem &6Quellstein&r auf die Innenseite, und das Portal leuchtet blau. Bau es in oder neben deiner Basis: wer zurückkommt, steht vor genau diesem Portal.",
          ],
          tasks=[task_item("ars_nouveau:source_gem", 1)],
          rewards=[reward_item("minecraft:torch", 32)],
          deps=["e_pickaxe"], icon="ars_nouveau:source_gem"),

    quest("e_enter", 9, 3, "&6&lReise in die Minenwelt",
          subtitle="Stell dich einen Moment ins Portal.",
          description=[
              "Bleib kurz im Portal stehen, bis das Licht dich holt. Du kommst auf dem Ankunftsplatz der Minenwelt an, das Portal dort bringt dich zurück zu deinem.",
              "",
              "Dein Inventar, deine Enderkiste und deine Rucksäcke reisen mit. Was du durchs Portal wirfst, kommt auf der anderen Seite heraus.",
          ],
          tasks=[task_advancement(MINING_ADV)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["e_frame"], icon="minecraft:iron_pickaxe", size=1.5, shape="hexagon"),

    quest("e_dangers", 11, 2, "&cMerk dir die Regeln der Minenwelt",
          subtitle="Alle drei Tage ist sie neu.",
          description=[
              "Die Minenwelt wird &calle drei Tage um 4:45 Uhr&r zurückgesetzt. Die Tabliste zählt herunter, im Chat wird vorher gewarnt. Wer dann drüben ist, reist mit allem, was er trägt, nach Hause.",
              "",
              "&cWas in der Minenwelt steht, ist danach weg:&r Maschinen, Kisten, Steinbrüche, dein Körper nach einem Tod. Bring deine Beute rechtzeitig heim.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:torch", 32)],
          deps=["e_enter"], icon="minecraft:skeleton_skull"),

    quest("e_ores", 11, 4, "&6Bau Eisen in Massen ab",
          subtitle="Die Mine ist zum Leerräumen da.",
          description=[
              "Bau &e64 Rohes Eisen&r ab. Mit &6Ultimine&r räumst du ganze Adern auf einmal.",
              "",
              "Eisen brauchst du ständig: Create-Teile, Eimer, Kochtopf, Silent Gear, Eisennuggets für die Andesitlegierung. Nimm Kupfer gleich mit.",
          ],
          tasks=[task_item("minecraft:raw_iron", 64)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["e_enter"], icon="minecraft:raw_iron"),

    quest("e_cobble", 13, 2, "&7Grab Stein für den Obelisken",
          subtitle="Jeder Gang zählt für den ganzen Server.",
          description=[
              "Bring &e512 Bruchstein&r mit. Sneak und Rechtsklick auf den Obelisken, und alles aus deinem Inventar ist drin.",
              "",
              "&eKronwerke:&r Die Stein-Säule der Stufe 1 will &e20 000 Bruchstein&r. Sammel ihn in einer Truhe am Portal und bring ihn gebündelt zum Spawn.",
          ],
          tasks=[task_item("minecraft:cobblestone", 512)],
          rewards=[reward_table("s1_common")],
          deps=["e_dangers"], icon="minecraft:cobblestone"),

    quest("e_diamonds", 13, 4, "&bFinde Diamanten",
          subtitle="Tief unten wird es glitzern.",
          description=[
              "Grab ganz unten, knapp über dem Grundgestein, bis du &e8 Diamanten&r hast. Ultimine nimmt die ganze Ader auf einen Schlag.",
              "",
              "Diamanten brauchst du für Zaubertisch, Obsidian, Silent Gear und einige Zaubergeräte.",
          ],
          tasks=[task_item("minecraft:diamond", 8)],
          rewards=[reward_xp(8)],
          deps=["e_ores"], icon="minecraft:diamond", optional=True),

    quest("e_veins", 11, 6, "&6Finde eine große Erzader",
          subtitle="Kupfer bei Granit, Eisen bei Tuff.",
          description=[
              "Grab eine große &6Erzader&r an und bring einen &6Rohkupferblock&r mit. Die Adern ziehen sich als lange Bänder durch den Stein, auch in der Minenwelt.",
              "",
              "&eKupferadern&r liegen zwischen Y 0 und 50 in Granit, &eEisenadern&r zwischen Y -60 und -8 in Tuff. Darin stecken Erz und ganze Rohblöcke.",
          ],
          tasks=[task_item("minecraft:raw_copper_block", 1)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["e_ores"], icon="minecraft:raw_copper_block", optional=True),

    quest("e_mine_waystone", 15, 2, "&6Finde den Heimweg",
          subtitle="Das Portal am Ankunftsplatz bringt dich zu deinem.",
          description=[
              "Der Heimweg führt immer durchs &6Portal am Ankunftsplatz&r, oder durch jedes Minenportal, das du drüben selbst baust. Du kommst vor dem Portal heraus, durch das du gegangen bist.",
              "",
              "Ein &6Wegstein&r in der Minenwelt verbindet nur Orte in der Minenwelt und ist beim nächsten Reset weg. Deine Wegsteine zuhause bleiben dir erhalten.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("waystones:return_scroll", 3), reward_xp(5)],
          deps=["e_cobble"], icon="waystones:waystone", optional=True),

    # ---- Bauwerke ---------------------------------------------------------------
    quest("e_structures", 4.5, 14.5, "&6&lErkunde Bauwerke",
          subtitle="Überall wartet etwas.",
          description=[
              "Schau dir einen Ort erst von außen an, bevor du hineinstürmst, und hak ab.",
              "",
              "Rechts findest du eine Checkliste der Bauwerke im Pack, Mod für Mod. Fast überall stehen Truhen, manche Orte sind harmlos, andere bewacht.",
          ],
          tasks=[task_checkmark("Losgezogen")],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["welcome"], icon="minecraft:mossy_stone_bricks", size=1.5, shape="hexagon"),

    quest("e_lootr", 7, 11, "&6Lass die Kisten stehen",
          subtitle="Jede Truhe, für jeden Spieler neu.",
          description=[
              "Öffne eine Truhe in einem Bauwerk und &cbau sie nicht ab&r. Dank &6Lootr&r hat sie für jeden Spieler ihren eigenen Inhalt.",
              "",
              "Du siehst an der Truhe, ob du sie schon geöffnet hast. Wer sie abbaut, nimmt allen nach ihm die Beute weg. Auch Fässer, Loren mit Truhe und Rahmen mit Elytren arbeiten so.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_structures"], icon="minecraft:chest"),

    quest("e_brush", 9, 11, "&6Pinsle verdächtigen Sand ab",
          subtitle="Archäologie in Ruinen und Tempeln.",
          description=[
              "Bau einen &6Pinsel&r (Feder, Kupferbarren, Stock) und pinsle &6Verdächtigen Sand&r oder Kies in einer Ruine ab.",
              "",
              "Neben Tonscherben steckt mit &e6,25 Prozent&r ein Artefakt darin. Dungeons and Taverns und die Pyramide von Cataclysm haben eigene Archäologie.",
          ],
          tasks=[task_item("minecraft:brush", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8), reward_xp(3)],
          deps=["e_lootr"], icon="minecraft:brush"),

    quest("e_artifacts", 11, 11, "&6Trag ein Artefakt",
          subtitle="Kleine Schätze mit großer Wirkung.",
          description=[
              "Leg ein &6Artefakt&r in einen der eigenen Plätze neben der Rüstung. Das Menü dafür öffnest du über den Knopf im Inventar.",
              "",
              "&6Laufschuhe&r machen schneller, die &6Wolke in einer Flasche&r gibt einen Doppelsprung, der &6Schnorchel&r Luft unter Wasser, die &6Nachtsichtbrille&r Licht in der Nacht. Selten trägt ein Zombie, Skelett oder Piglin eines.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_brush"], icon="artifacts:running_shoes"),

    quest("e_campsite", 13, 11, "&6Finde ein Höhlenlager",
          subtitle="Verlassene Lager tief unter der Erde.",
          description=[
              "Finde ein &6Höhlenlager&r von Artifacts und hak ab. Es liegt in Höhlen zwischen &eY -60 und 40&r, mit Licht und einer Truhe.",
              "",
              "In der Truhe liegen oft Artefakte. &cAber:&r Etwa jede dritte Truhe in einem Lager ist ein Mimic (nächste Quest).",
          ],
          tasks=[task_checkmark("Ein Höhlenlager gefunden")],
          rewards=[reward_item("minecraft:torch", 16), reward_xp(3)],
          deps=["e_artifacts"], icon="minecraft:lantern"),

    quest("e_mimic", 15, 11, "&cBesiege einen Mimic",
          subtitle="Manche Truhen beißen zurück.",
          description=[
              "Erleg einen &cMimic&r. Er sieht aus wie eine Truhe, bis du sie öffnen willst, und schlägt dann hart zu.",
              "",
              "Wer ihn besiegt, bekommt ein Artefakt. Schlag die Truhe eines Höhlenlagers zur Probe einmal an, bevor du sie öffnest.",
          ],
          tasks=[task_kill("artifacts:mimic", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["e_campsite"], icon="artifacts:mimic_spawn_egg", optional=True),

    # YUNG's
    quest("e_yung_dungeon", 7, 13.5, "&8Räum ein Verlies aus",
          subtitle="YUNG's Better Dungeons: Skelette, Zombies, Spinnen.",
          description=[
              "Finde ein Verlies von &6YUNG's Better Dungeons&r und hak ab: Skelett-Verliese, Zombie-Verliese, Spinnenhöhlen oder kleine Verliese.",
              "",
              "Jedes hat Spawner. Lass sie stehen, wenn du eine Farm planst, oder hol sie dir mit Apotheosis (Kapitel &6Apotheosis&r und &6Erste Farmen&r).",
          ],
          tasks=[task_checkmark("Ein Verlies gefunden")],
          rewards=[reward_item("minecraft:bone", 16), reward_xp(3)],
          deps=["e_structures"], icon="minecraft:cracked_stone_bricks"),

    quest("e_yung_mineshaft", 9, 13.5, "&8Lauf durch eine Mine",
          subtitle="YUNG's Better Mineshafts: jedes Biom baut anders.",
          description=[
              "Finde eine alte Mine und hak ab. &6YUNG's Better Mineshafts&r baut sie je nach Biom aus anderem Holz und Stein, mit Erzadern, Lagern und Loren.",
              "",
              "Die Loren mit Truhe sind Lootr-Loren. Höhlen formt &6YUNG's Better Caves&r um, rechne also mit großen Hallen und tiefen Spalten.",
          ],
          tasks=[task_checkmark("Eine Mine gefunden")],
          rewards=[reward_item("minecraft:rail", 16), reward_xp(3)],
          deps=["e_yung_dungeon"], icon="minecraft:rail"),

    quest("e_yung_temples", 11, 13.5, "&eLös einen Tempel",
          subtitle="Wüste, Dschungel, Sumpf: YUNG's baut alle neu.",
          description=[
              "Finde einen Wüstentempel, Dschungeltempel oder eine Hexenhütte und hak ab. &6YUNG's Better Desert Temples&r, &6Jungle Temples&r und &6Witch Huts&r machen daraus große Anlagen.",
              "",
              "Rechne mit Fallen, Rätseln und Gegnern. Geh langsam und schau auf den Boden.",
          ],
          tasks=[task_checkmark("Einen Tempel gefunden")],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["e_yung_mineshaft"], icon="minecraft:chiseled_sandstone"),

    quest("e_yung_ocean", 13, 13.5, "&3Tauch zu einem Ozeanmonument",
          subtitle="Größer, und die Ältesten Wächter warten.",
          description=[
              "Finde ein &6Ozeanmonument&r und hak ab. &6YUNG's Better Ocean Monuments&r baut es größer und abwechslungsreicher.",
              "",
              "Nimm Tränke der Wasseratmung, Milch gegen die Ermüdung der Ältesten Wächter und Türen für Luftblasen mit. Schwämme und Prismarin sind die Beute.",
          ],
          tasks=[task_checkmark("Ein Ozeanmonument gefunden")],
          rewards=[reward_item("minecraft:prismarine_bricks", 16), reward_xp(5)],
          deps=["e_yung_temples"], icon="minecraft:prismarine_bricks", optional=True),

    quest("e_yung_stronghold", 15, 13.5, "&5Finde eine Festung",
          subtitle="YUNG's Better Strongholds, tief unter der Erde.",
          description=[
              "Stolper über eine &6Festung&r und hak ab. &6YUNG's Better Strongholds&r baut sie größer, mit Bibliotheken, Gefängnissen und Fallen.",
              "",
              "Gezielt findest du sie erst mit Enderaugen, und die brauchen Lohenstaub aus dem Nether (Stufe 2). Das Endportal darin öffnet erst in Stufe 4.",
          ],
          tasks=[task_checkmark("Eine Festung gefunden")],
          rewards=[reward_item("minecraft:book", 4), reward_xp(5)],
          deps=["e_yung_ocean"], icon="minecraft:chiseled_stone_bricks", optional=True),

    # Villages and taverns
    quest("e_tnt_village", 7, 16, "&6Besuch ein Dorf von Towns and Towers",
          subtitle="Jedes Biom hat seinen eigenen Dorfstil.",
          description=[
              "Finde ein Dorf in einem Biom, das in Vanilla keines hat, und hak ab: Strand, Birkenwald, Blumenwald, Dschungel, Wiese, Pilzinsel, Sumpf, Tafelberge und mehr.",
              "",
              "&6Towns and Towers&r gibt jedem davon eigene Häuser. Sogar auf dem Ozean steht eines.",
          ],
          tasks=[task_checkmark("Ein neues Dorf gefunden")],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(3)],
          deps=["e_structures"], icon="minecraft:bell"),

    quest("e_tnt_outpost", 9, 16, "&cRäum einen Plünderer-Außenposten",
          subtitle="Außenposten in jedem Biom.",
          description=[
              "Finde einen &6Plünderer-Außenposten&r und hak ab. Towns and Towers baut ihn in jedem Biom anders, von Tafelberg bis Schneehang.",
              "",
              "Armbrustschützen treffen weit. Geh mit Schild, und lass das Banner des Hauptmanns liegen, wenn du keinen Überfall auf dein Dorf willst.",
          ],
          tasks=[task_checkmark("Einen Außenposten gefunden")],
          rewards=[reward_item("minecraft:arrow", 32), reward_xp(3)],
          deps=["e_tnt_village"], icon="minecraft:crossbow"),

    quest("e_dnt_tavern", 11, 16, "&6Kauf eine Karte in der Taverne",
          subtitle="14 Smaragde und ein Kompass, einmal pro Taverne.",
          description=[
              "Geh in eine &6Taverne&r von Dungeons and Taverns. Ein Dorfbewohner dort tauscht &e14 Smaragde&r und einen &6Kompass&r einmalig gegen eine Karte zu einem Bauwerk.",
              "",
              "Die Karte führt zu Krypten, Ruinen, einer antiken Stadt und anderen Orten der Mod. Tavernen gibt es in elf Stilen, von Eiche bis Mangrove.",
          ],
          tasks=[task_checkmark("Eine Taverne gefunden")],
          rewards=[reward_item("minecraft:emerald", 8), reward_xp(5)],
          deps=["e_tnt_outpost"], icon="minecraft:compass"),

    quest("e_dnt_crypts", 13, 16, "&8Wag dich in eine Krypta",
          subtitle="Die Verliese von Dungeons and Taverns.",
          description=[
              "Finde eines dieser Bauwerke und hak ab: &6Creeping Crypt&r, &6Undead Crypt&r, &6Stray Fort&r, &6Illager Manor&r, Illager-Versteck, &6Toxic Lair&r, Dschungel- oder Wüstenruinen.",
              "",
              "Das sind echte Verliese voller Gegner. Geht zu zweit und nehmt Rückkehr-Schriftrollen mit.",
          ],
          tasks=[task_checkmark("Ein Verlies von Dungeons and Taverns gefunden")],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["e_dnt_tavern"], icon="minecraft:zombie_head"),

    quest("e_dnt_towers", 15, 16, "&6Steig auf einen Feuerwachturm",
          subtitle="Aussicht und Truhen in neun Holzarten.",
          description=[
              "Klettere auf einen &6Feuerwachturm&r von Dungeons and Taverns und hak ab. Es gibt ihn in neun Biomstilen, von Birke bis Mangrove.",
              "",
              "Von oben siehst du weit. Dazu baut die Mod Brunnen, Bunker, ein Dreizack-Denkmal und kleine Kampfschreine in fünf Stufen.",
          ],
          tasks=[task_checkmark("Einen Feuerwachturm bestiegen")],
          rewards=[reward_item("minecraft:spyglass", 1), reward_xp(3)],
          deps=["e_dnt_crypts"], icon="minecraft:spyglass", optional=True),

    # When Dungeons Arise and the small ones
    quest("e_arise_land", 7, 18.5, "&4Erobere einen großen Dungeon",
          subtitle="When Dungeons Arise baut riesig.",
          description=[
              "Finde einen Dungeon von &6When Dungeons Arise&r an Land und hak ab: Gießerei, Pestanstalt, Mechanisches Nest, Keep Kayra im Sumpf, Shiraz-Palast in der Wüste, Thornborn-Türme, Illager-Festung oder Windmühle, Banditendorf, Kloster.",
              "",
              "Mehrere Etagen, viele Gegner, gute Truhen. Ein Abend für eine Gruppe.",
          ],
          tasks=[task_checkmark("Einen Dungeon von When Dungeons Arise gefunden")],
          rewards=[reward_table("s1_uncommon"), reward_xp(8)],
          deps=["e_structures"], icon="minecraft:iron_bars"),

    quest("e_arise_sea", 9, 18.5, "&3Entere ein Schiff",
          subtitle="Piraten, Illager und ein Seeungeheuer.",
          description=[
              "Finde ein Bauwerk von When Dungeons Arise auf dem Meer und hak ab: Untotes Piratenschiff, Illager-Korsar oder Galeere, die &6Typhon&r, einen Leuchtturm oder eine Fischerhütte.",
              "",
              "Ein Boot und Blöcke zum Hochbauen helfen beim Entern.",
          ],
          tasks=[task_checkmark("Ein Bauwerk auf dem Meer gefunden")],
          rewards=[reward_item("minecraft:cooked_cod", 16), reward_xp(5)],
          deps=["e_arise_land"], icon="minecraft:oak_boat", optional=True),

    quest("e_arise_sky", 11, 18.5, "&bErreich ein Himmelsbauwerk",
          subtitle="Luftschiffe und Festungen über den Wolken.",
          description=[
              "Erreich ein schwebendes Bauwerk von When Dungeons Arise und hak ab: ein kleines Luftschiff oder eine der drei Himmelsfestungen (Heavenly Rider, Challenger, Conqueror).",
              "",
              "Sie hängen hoch über Ebenen, Wäldern und Wüsten. Bau dir eine Säule hinauf und nimm Federfall oder einen Wassereimer mit.",
          ],
          tasks=[task_checkmark("Ein Himmelsbauwerk erreicht")],
          rewards=[reward_item("minecraft:feather", 16), reward_xp(5)],
          deps=["e_arise_sea"], icon="minecraft:feather", optional=True),

    quest("e_formations", 13, 18.5, "&aSammle kleine Funde",
          subtitle="Formations Overworld und Explorify.",
          description=[
              "Finde ein kleines Bauwerk von &6Formations Overworld&r oder &6Explorify&r und hak ab.",
              "",
              "&eFormations:&r Hütten, Statuen, Brunnen, Friedhöfe, Eispaläste, ein Hobbit-Loch, Meteoriten. &eExplorify:&r Mausoleen, Bauernhöfe, Wüstenschreine, Wegweiser, eine Siedlung im Dunkelwald und eine Pyramide in den Tafelbergen.",
          ],
          tasks=[task_checkmark("Einen kleinen Fund gemacht")],
          rewards=[reward_item("minecraft:bread", 16), reward_xp(3)],
          deps=["e_arise_land"], icon="minecraft:mossy_cobblestone"),

    quest("e_dangerous", 15, 18.5, "&cKenn die gefährlichen Orte",
          subtitle="Arenen für echte Bosse. Nicht allein.",
          description=[
              "Lies das Kapitel &cBosse der Oberwelt&r, bevor du eine Pyramide in der Wüste, ein Gefängnis im Schnee, eine versunkene Stadt, eine alte Fabrik oder eine Akropolis über dem Meer betrittst.",
              "",
              "Dort stehen die fünf Bosse von L_Ender's Cataclysm in der richtigen Reihenfolge, dazu die dunklen Türme von Born in Chaos und die Kreaturen von Mowzie's Mobs.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["e_formations"], icon="minecraft:skeleton_skull"),

    # ---- Neu: Reisen ------------------------------------------------------------
    quest("e_bound_scroll", 15, -3.5, "&6Binde eine Schriftrolle an einen Wegstein",
          subtitle="Immer zum selben Ziel, ohne Level.",
          description=[
              "&62 Goldnuggets&r, eine &6Feder&r und &63 Papier&r ergeben drei &6Leere Schriftrollen&r. Rechtsklick mit einer davon auf einen Wegstein, und sie wird zur &6Gebundenen Schriftrolle&r.",
              "",
              pic("waystones:bound_scroll"),
              "",
              "Sie bringt dich einmal genau zu diesem Wegstein, ohne Auswahl und wie alle Schriftrollen ohne Levelkosten. Binde ein paar an deine Basis und gib sie Freunden mit.",
          ],
          tasks=[task_item("waystones:bound_scroll", 1)],
          rewards=[reward_item("minecraft:feather", 8), reward_xp(3)],
          deps=["e_return_scroll"], icon="waystones:bound_scroll"),

    # ---- Neu: Minenwelt ---------------------------------------------------------
    quest("e_altimeter", 11, 0.5, "&6Bau einen Höhenmesser",
          subtitle="Wie tief bist du gerade?",
          description=[
              "&64 Kupferbarren&r um einen &6Redstone&r ergeben den &6Höhenmesser&r von Supplementaries. Ein Klick zeigt deine Höhe als Y-Wert.",
              "",
              "Praktisch beim Erzsuchen: Diamanten liegen ganz unten, Kupferadern zwischen Y 0 und 50, Eisenadern zwischen Y -60 und -8.",
          ],
          tasks=[task_item("supplementaries:altimeter", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8)],
          deps=["e_enter"], icon="supplementaries:altimeter", optional=True),

    quest("e_slice_map", 13, 0.5, "&6Zeichne eine Schichtkarte",
          subtitle="Eine Karte für unter der Erde.",
          description=[
              "Ein &6Höhenmesser&r und eine leere &6Karte&r ergeben eine &6Schichtkarte&r. Sie zeigt die Welt als Schnitt auf der Höhe, auf der du sie aufziehst, mit allen Höhlen und Gängen.",
              "",
              pic("supplementaries:slice_map"),
              "",
              "Sie deckt nur ein Viertel der Fläche einer normalen Karte ab. Zieh sie in deiner Grubenebene auf, dann siehst du, wo du schon warst.",
          ],
          tasks=[task_item("supplementaries:slice_map", 1)],
          rewards=[reward_item("minecraft:paper", 8), reward_xp(3)],
          deps=["e_altimeter"], icon="supplementaries:slice_map", optional=True),

    # ---- Neu: Bauwerke ---------------------------------------------------------
    quest("e_quiver", 7, 23.5, "&6Erbeute einen Köcher",
          subtitle="Sechs Stapel Pfeile in einem Platz.",
          description=[
              "Manche Skelette tragen einen &6Köcher&r auf dem Rücken. Erleg eines davon und nimm ihn mit. Je schwieriger die Gegend, desto öfter siehst du sie.",
              "",
              "Der Köcher fasst &d6&r Stapel Pfeile, auch Trankpfeile. Aufgesammelte Pfeile wandern von selbst hinein, die Sorte zum Schießen wählst du mit der Köcher-Taste.",
          ],
          tasks=[task_item("supplementaries:quiver", 1)],
          rewards=[reward_item("minecraft:arrow", 32), reward_xp(3)],
          deps=["e_lootr"], icon="supplementaries:quiver", optional=True),

    quest("e_trial_chamber", 7, 21, "&6Hol dir einen Prüfungsschlüssel",
          subtitle="Prüfungskammern liegen tief im Stein.",
          description=[
              "Finde eine &6Prüfungskammer&r aus Kupfer und Tuff und besiege die Wellen eines &6Prüfungs-Spawners&r. Er wirft dabei einen &6Prüfungsschlüssel&r aus.",
              "",
              "Mit dem Schlüssel öffnest du einen &6Tresor&r der Kammer. Jeder Tresor gibt jedem Spieler einmal Beute, also lohnt sich die Kammer auch zu mehreren.",
          ],
          tasks=[task_item("minecraft:trial_key", 1)],
          rewards=[reward_table("s1_common"), reward_xp(5)],
          deps=["e_structures"], icon="minecraft:trial_key"),

    quest("e_breeze", 9, 21, "&bBesiege eine Böe",
          subtitle="Der Wächter der Prüfungskammern.",
          description=[
              "Erleg eine &bBöe&r. Sie springt herum und schießt &6Windkugeln&r, die dich zurückstoßen. Pfeile lenkt sie ab, also geh nah heran.",
              "",
              "Sie lässt &6Böenruten&r fallen. Vier &6Windkugeln&r aus einer Rute kannst du selbst werfen: auf den Boden geworfen schleudern sie dich hoch.",
          ],
          tasks=[task_kill("minecraft:breeze", 1)],
          rewards=[reward_item("minecraft:wind_charge", 8), reward_xp(5)],
          deps=["e_trial_chamber"], icon="minecraft:breeze_rod"),

    quest("e_mace", 11, 21, "&5Schmiede einen Streitkolben",
          subtitle="Je tiefer der Fall, desto härter der Schlag.",
          description=[
              "Ein &6Schwerer Kern&r über einer &6Böenrute&r ergibt den &6Streitkolben&r. Sein Schaden wächst mit der Fallhöhe, und ein Treffer aus dem Sprung fängt deinen Sturz ab.",
              "",
              "Den Kern gibt es nur in &5Unheilvollen Tresoren&r. Trink eine &6Unheilvolle Flasche&r, die Hauptleute von Plündererbanden fallen lassen, und betritt dann eine Prüfungskammer. Die Spawner werden härter und werfen &5Unheilvolle Prüfungsschlüssel&r aus.",
              "",
              "Zusammen mit Windkugeln wird er zur gefährlichsten Nahkampfwaffe der Oberwelt.",
          ],
          tasks=[task_item("minecraft:mace", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(10)],
          deps=["e_breeze"], icon="minecraft:mace", optional=True),

    quest("e_evoker", 13, 21, "&cBesiege einen Magier",
          subtitle="Er trägt ein Totem der Unsterblichkeit.",
          description=[
              "Erleg einen &cMagier&r. Er wohnt in Waldanwesen und kommt in den späteren Wellen eines Überfalls auf ein Dorf.",
              "",
              "Weich seinen Fangzähnen aus dem Boden aus und töte die Plagegeister zuerst. Er lässt immer ein &6Totem der Unsterblichkeit&r fallen. Halt es in der zweiten Hand, und es rettet dich einmal vor dem Tod.",
          ],
          tasks=[task_kill("minecraft:evoker", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(8)],
          deps=["e_dnt_crypts"], icon="minecraft:totem_of_undying"),

    quest("e_elder_guardian", 13, 23.5, "&3Besiege einen Großen Wächter",
          subtitle="Drei wachen über jedes Ozeanmonument.",
          description=[
              "Erleg einen &3Großen Wächter&r im Ozeanmonument. Jedes Monument hat drei, und solange einer lebt, lähmt er dich immer wieder mit Abbaulähmung.",
              "",
              "Jeder lässt einen &6Nassen Schwamm&r fallen. Erst wenn alle drei tot sind, kannst du das Monument in Ruhe ausräumen.",
          ],
          tasks=[task_kill("minecraft:elder_guardian", 1)],
          rewards=[reward_item("minecraft:prismarine_shard", 16), reward_xp(8)],
          deps=["e_yung_ocean"], icon="minecraft:wet_sponge", optional=True),

    quest("e_heart_sea", 15, 23.5, "&bGrab ein Herz des Meeres aus",
          subtitle="Folge der Schatzkarte zum Kreuz.",
          description=[
              "In Schiffswracks und Ozeanruinen liegen &6Schatzkarten&r. Folge ihr bis zum roten Kreuz und grab dort nach der vergrabenen Truhe. Darin liegt immer ein &6Herz des Meeres&r.",
              "",
              "Acht &6Nautilusschalen&r um das Herz ergeben einen &6Aquisator&r. In einem Rahmen aus Prismarin gibt er dir unter Wasser Atem, Sicht und schnelleres Abbauen.",
          ],
          tasks=[task_item("minecraft:heart_of_the_sea", 1)],
          rewards=[reward_item("minecraft:nautilus_shell", 2), reward_xp(5)],
          deps=["e_yung_ocean"], icon="minecraft:heart_of_the_sea", optional=True),

    # ---- Weiter ------------------------------------------------------------------
    quest("a_affix", 17.5, 11, "&6Lern Beute mit Affixen kennen",
          subtitle="Kein Schwert gleicht dem anderen.",
          description=[
              "Viele Waffen und Rüstungen aus Truhen und von Monstern tragen &6Affixe&r aus Apotheosis. Die Namensfarbe zeigt die Seltenheit: &7Common&r, &aUncommon&r, &9Rare&r, &5Epic&r, &6Mythic&r.",
              "",
              "Edelsteine, Sockel, Zerlegen, Umschmieden und Weltstufen stehen im Kapitel &6Apotheosis&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_mimic"], icon="minecraft:iron_sword"),

    quest("e_dimensions", 17.5, 4, "&5Schau, welche Welten noch kommen",
          subtitle="Sechs Dimensionen öffnen mit den Stufen.",
          description=[
              "Die Minenwelt ist offen. Die anderen Welten kommen mit den Stufen: &cNether&r und &bAether&r in Stufe 2, &2Undergarden&r und &3Otherside&r in Stufe 3, &5End&r und &bEternal Starlight&r in Stufe 4.",
              "",
              "Jedes Portal in drei Zeilen steht in der &6Checkliste: Dimensionen und Reisen&r, jede Welt hat ihr eigenes Kapitel: &cDer Nether&r, &bDer Aether&r, &2Der Undergarden&r, &3Deeper and Darker&r, &5Das End&r, &bEternal Starlight&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(3)],
          deps=["e_mine_waystone"], icon="minecraft:obsidian"),

    # ---- Abschluss ------------------------------------------------------------
    quest("e_explorer", 20, 7.5, "&6&lWerd zum Entdecker",
          subtitle="Hin und wieder zurück.",
          description=[
              "Hak ab, wenn du Biome findest, zwischen Wegsteinen reist, in der Minenwelt gräbst und weißt, welche Bauwerke wohin gehören.",
              "",
              "Der &cNether&r öffnet sich mit Stufe 2 live auf Stream durch das Portal am Spawn. Leg dir bis dahin einen Vorrat an Essen, Fackeln und Eisen an.",
          ],
          tasks=[task_checkmark("Ich war unterwegs")],
          rewards=[reward_table("s1_rare"), reward_xp(15)],
          deps=["e_bounty", "e_own_waystone", "e_cobble", "e_dangerous", "a_affix"],
          icon="minecraft:compass", size=2.5, shape="gear"),
]

images = [
    banner("exploration/title", "Erkundung", 0, -5, height=1.8, kind="title", colour="nature"),
    banner("exploration/orientation", "Orientierung", 9.5, -9.8, height=0.9, colour="nature"),
    banner("exploration/travel", "Reisen", 9, -5.3, height=0.9, colour="magic"),
    banner("exploration/mine", "Minenwelt", 9, 0.6, height=0.9, colour="stone"),
    banner("exploration/structures", "Bauwerke und Beute", 11, 9.2, height=0.9, colour="fire"),
    banner("exploration/onward", "Weiter", 17.5, 2.2, height=0.9, colour="brass"),
]

chapter(C, "Erkundung", "minecraft:filled_map", "world", quests, shape="circle", order=7,
        subtitle=["Biome, Wegsteine, die Minenwelt und die Bauwerke der Oberwelt."],
        images=images)
