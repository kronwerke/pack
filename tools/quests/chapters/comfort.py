"""Comfort in stage 1: the small mods that make the day easier. Simple Magnets, Item Collectors
(advanced collector is stage 2 and only mentioned), Pylons (harvester; infusion, interdiction,
expulsion and protection are stage 2 and only mentioned), FTB Chunks claims and chunk loading,
JourneyMap, JEI, Jade, FTB Ultimine, Simple Voice Chat, Corpse, Trash Cans, Inventory Tweak and
Crafting Tweaks. Numbers follow the server configs in config/. Waystones has its own chapter.
Cobweb in the mod list is only the Crystal Nest library and has nothing for players; Mouse Tweaks
and Xaero are not in the pack."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "comfort"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Start ------------------------------------------------------------------
    quest("welcome", 0, 6, "&6&lRichte dir den Alltag ein",
          subtitle="Kleine Mods, große Erleichterung.",
          description=[
              "Neben den großen Mods stecken im Pack ein Dutzend kleine, die jeden Tag ein paar Minuten sparen: ein &6Magnet&r, ein &6Sammler&r für Farmen, &6Claims&r und &6Chunkloading&r, zwei Karten, JEI, Jade, Ultimine, der Sprachchat, dein Körper nach dem Tod, Mülltonnen und ein Sortierknopf fürs Inventar.",
              "",
              "Dieses Kapitel geht sie einzeln durch, mit einer Zeile dazu, wie du sie benutzt. Nichts davon ist Pflicht, aber wer die Abschnitte &eKarte&r und &eWissen&r kennt, kommt im Rest des Buchs schneller voran.",
              "",
              "Alles hier ist ab &eStufe 1&r offen. Was in Stufe 2 dazukommt, steht als Hinweis dabei.",
          ],
          tasks=[task_checkmark("Los geht's")],
          rewards=[reward_table("s1_common")],
          icon="simplemagnets:basicmagnet", size=2.0, shape="hexagon"),

    # ---- Sammeln -------------------------------------------------------------------
    quest("magnet", 3, 0, "&bBau einen Magneten",
          subtitle="Nie wieder bücken.",
          description=[
              "&eRezept:&r fünf &6Eisenbarren&r (die ganze linke Spalte sowie oben und unten in der Mitte), oben rechts ein &6Lapislazuli&r, in der Mitte eine &6Enderperle&r, unten rechts ein &6Redstone&r. Ein &6Einfacher Magnet&r.",
              "",
              "Er liegt irgendwo im Inventar und zieht Gegenstände und Erfahrung bis &e5 Blöcke&r weit zu dir. &eRechtsklick&r schaltet ihn an und aus, ein Ton und eine Meldung bestätigen es.",
              "",
              "&eTipp:&r Schalt ihn aus, bevor du an fremden Farmen oder Werfern vorbeiläufst. Sonst steckt plötzlich der Ertrag deines Nachbarn in deiner Tasche.",
          ],
          tasks=[task_item("simplemagnets:basicmagnet", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(3)],
          deps=["welcome"], icon="simplemagnets:basicmagnet"),

    quest("magnet_adv", 6, -1.2, "&bBau den Fortgeschrittenen Magneten",
          subtitle="Weiter, mit Filter, und Erfahrung nach Wunsch.",
          description=[
              "&eRezept:&r vier &6Goldbarren&r oben und unten in den beiden linken Spalten, oben rechts &6Lapislazuli&r, in der mittleren Reihe dein &6Einfacher Magnet&r, ein &6Enderauge&r und ein &6Diamant&r, unten rechts &6Redstone&r.",
              "",
              "Er zieht &e8 Blöcke&r weit, im Fenster stellst du 3 bis 11 ein. Gegenstände und Erfahrung schaltest du getrennt, und der &6Filter&r mit Whitelist oder Blacklist lässt zum Beispiel Bruchstein liegen.",
              "",
              "&cHinweis:&r Das Enderauge braucht Lohenstaub, und den gibt es erst mit dem Nether in &eStufe 2&r.",
          ],
          tasks=[task_item("simplemagnets:advancedmagnet", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["magnet"], icon="simplemagnets:advancedmagnet", optional=True),

    quest("coil", 6, 1.2, "&7Schütz deine Farm vor Magneten",
          subtitle="Die Entmagnetisierungsspule.",
          description=[
              "&eRezept:&r ein &6Goldbarren&r oben in der Mitte, zwei &6Redstone&r links und rechts darunter, vier &6Eisenbarren&r in der Mitte und der unteren Reihe. Eine &6Einfache Entmagnetisierungsspule&r.",
              "",
              "In &e2 Blöcken&r um die Spule (einstellbar 1 bis 3) zieht kein Magnet mehr. Stell sie an den Sammelpunkt deiner Farm, dann bleibt der Ertrag im Trichter, auch wenn jemand mit Magnet vorbeiläuft. Ihr Bereich wird angezeigt, wenn du sie anschaust.",
              "",
              "Die &6Fortgeschrittene Spule&r (Glowstone, Redstone, Gold um die einfache) reicht 3 Blöcke, einstellbar bis 5, und hat einen Filter. Glowstone kommt mit dem Nether in Stufe 2.",
          ],
          tasks=[task_item("simplemagnets:basic_demagnetization_coil", 1)],
          rewards=[reward_item("minecraft:redstone", 8), reward_xp(3)],
          deps=["magnet"], icon="simplemagnets:basic_demagnetization_coil", optional=True),

    quest("collector", 9, 0, "&aStell einen Sammler an die Farm",
          subtitle="Was fällt, landet in der Truhe.",
          description=[
              "&eRezept:&r eine &6Enderperle&r oben in der Mitte, darunter ein &6Obsidian&r, unten drei &6Obsidian&r. Ein &6Einfacher Sammler&r von Item Collectors.",
              "",
              "Setz ihn direkt an eine Truhe, ein Fass oder eine Maschine. Er hebt alles auf, was in seinem Bereich liegt, und legt es in den Block, an dem er hängt. Im Fenster stellst du die Reichweite ein, bis &e5 Blöcke&r in jede Richtung, für jede Achse getrennt.",
              "",
              "Unter einer Hühnerfarm, neben dem Zuckerrohr mit Beobachter oder hinter einem Create-Bohrer spart er dir einen ganzen Trichterboden.",
              "",
              "&cAusblick:&r Der &6Fortgeschrittene Sammler&r (Enderauge, Sammler, drei Obsidian) reicht 7 Blöcke und hat einen Filter. Er öffnet mit &eStufe 2&r.",
          ],
          tasks=[task_item("itemcollectors:basic_collector", 1)],
          rewards=[reward_item("minecraft:obsidian", 4), reward_table("s1_common")],
          deps=["magnet"], icon="itemcollectors:basic_collector"),

    # ---- Pylonen -------------------------------------------------------------------
    quest("harvester", 12.5, 0, "&eBau den Erntepylon",
          subtitle="Ein Feld, das sich selbst erntet.",
          description=[
              "&eRezept:&r drei &6Quarzstufen&r oben, &6Eisengitter&r, &6Heuballen&r, &6Eisengitter&r in der Mitte, drei &6Polierter Schwarzstein&r unten. Ein &6Erntepylon&r.",
              "",
              "Stell ihn in oder über den Wasserblock deines Feldes, eine &6Truhe&r direkt darüber und eine &6Hacke&r in den Pylon. Alle &e3 Sekunden&r erntet er reife Pflanzen im eingestellten Bereich, pflanzt nach und legt den Ertrag in die Truhe. Jede Ernte kostet die Hacke einen Punkt Haltbarkeit.",
              "",
              "&cHinweis:&r Quarz und Schwarzstein kommen aus dem Nether. Der Pylon ist in Stufe 1 freigegeben, bauen kannst du ihn aber erst mit &eStufe 2&r. Sammle bis dahin den Heuballen und die Gitter.",
              "",
              "Die Hacke lässt sich nicht per Rohr nachfüllen. Eine unzerbrechliche Hacke von Silent Gear oder einfach ein Stapel Steinhacken daneben hilft.",
          ],
          tasks=[task_item("pylons:harvester_pylon", 1)],
          rewards=[reward_item("minecraft:bread", 16), reward_table("s1_uncommon")],
          deps=["collector"], icon="pylons:harvester_pylon", optional=True),

    quest("pylons", 15.5, 0, "&dLies, was die anderen Pylonen tun",
          subtitle="Vier Pylonen für Stufe 2.",
          description=[
              "Alle vier haben dasselbe Rezept wie der Erntepylon, nur der Block in der Mitte ist ein anderer. Sie öffnen mit &eStufe 2&r.",
              "",
              "&6Infusionspylon&r (Smaragdblock): Lad einen &6Trankfilter&r mit einem Trankeffekt auf, indem du ihn mit aktivem Effekt rechtsklickst, insgesamt eine Stunde Effektdauer. Danach gibt dir der Pylon den Effekt überall, egal wie weit du weg bist. Bis Stärke IV, keine Absorption.",
              "",
              "&6Interdiktionspylon&r (Netheritblock): verhindert Mobspawns in einem Chunkbereich, Filter per &6Mobfilter&r. &6Vertreibungspylon&r (Diamantblock): wirft fremde Spieler aus bis zu 2 Chunks um den Pylon, nur in der Oberwelt. &6Schutzpylon&r (Honigwabenblock): verhindert, dass du selbst Blöcke oder Tiere aus dem Filter kaputt machst.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["harvester"], icon="pylons:potion_filter", optional=True),

    # ---- Karte und Claims --------------------------------------------------------
    quest("claims", 3, 5, "&6Sichere deine Basis",
          subtitle="FTB Chunks: Claims mit der Maus ziehen.",
          description=[
              "Drück &eM&r für die Karte, dann &eC&r für die Claim-Ansicht. &eLinke Maustaste&r über die Chunks ziehen beansprucht sie, &erechte&r gibt sie frei. Dein Team hat bis zu &e500 Chunks&r.",
              "",
              "In deinen Chunks können nur du, dein Team und deine Verbündeten Blöcke abbauen, setzen und Truhen öffnen. Creeper und Ghasts sprengen dort nichts, Endermen klauen nichts. &cPvP bleibt an&r, Claims machen dich nicht unverwundbar.",
              "",
              "&eTipp:&r Verbündete trägst du in den Team-Einstellungen ein. Wer eine Maschine mit Fake-Spieler aufstellt (ein Router mit Breaker-Modul), muss &eFake-Spieler erlauben&r oder dem Router ein Sicherheits-Upgrade geben, sonst darf er in deinem Claim nichts.",
          ],
          tasks=[task_checkmark("Basis beansprucht")],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["welcome"], icon="minecraft:iron_door"),

    quest("chunkload", 6, 5, "&6Halt deine Farm am Laufen",
          subtitle="Chunkloading, solange einer von euch da ist.",
          description=[
              "In der Claim-Ansicht ziehst du mit &eShift und linker Maustaste&r über beanspruchte Chunks, um sie zu laden, mit &eShift und rechter&r lädst du sie wieder aus. Geladene Chunks werden auf der Karte eigens markiert. Bis zu &e25 Chunks&r pro Team.",
              "",
              "Geladen heißt: Maschinen, Farmen und Rohre laufen dort weiter, auch wenn niemand in der Nähe ist. Auf Kronwerke gilt aber: Sie laufen nur, solange &ejemand aus deinem Team online&r ist. Loggt sich der letzte aus, steht die Farm bis zum nächsten Login.",
              "",
              "Mit dem &eMausrad&r über einem geladenen Chunk stellst du ein, wann das Laden von selbst endet. Für einen Nachtlauf des Brass-Mixers genügt das.",
          ],
          tasks=[task_checkmark("Chunks geladen")],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["claims"], icon="minecraft:clock"),

    quest("journeymap", 9, 5, "&aFind dich zurecht",
          subtitle="JourneyMap, Wegpunkte und zwei Minikarten.",
          description=[
              "Drück &eJ&r für die große Karte von &6JourneyMap&r, &eB&r setzt einen Wegpunkt dort, wo du stehst, &eN&r öffnet die Wegpunktliste. Wegpunkte leuchten in der Welt als Säule, mit Namen und Entfernung.",
              "",
              "Beim Tod legt JourneyMap von selbst einen Wegpunkt an. Mit der Karte von FTB Chunks (&eM&r) kannst du Wegpunkte außerdem mit deinem Team oder dem ganzen Server teilen.",
              "",
              "&eTipp:&r Beide Mods bringen eine Minikarte mit, zwei sind eine zu viel. Schalt eine in den Einstellungen ab, zum Beispiel die von FTB Chunks über den Knopf &eMinikarte umschalten&r in den Tastenbelegungen.",
          ],
          tasks=[task_checkmark("Wegpunkt gesetzt")],
          rewards=[reward_item("minecraft:compass", 1), reward_xp(3)],
          deps=["claims"], icon="minecraft:filled_map"),

    # ---- Wissen ------------------------------------------------------------------
    quest("jei_lookup", 3, 9.5, "&eSchlag ein Rezept nach",
          subtitle="JEI: R, U und die Suche.",
          description=[
              "Fahr mit der Maus über einen Gegenstand, im Inventar oder in der Liste rechts, und drück &eR&r für seine Rezepte oder &eU&r für alles, was man damit macht. &eEsc&r oder Rücktaste bringt dich zurück.",
              "",
              "Unten rechts ist das &eSuchfeld&r. &e@create&r zeigt nur Dinge aus Create, &e$ingots&r alles mit dem Tag Barren. Im Rezeptfenster legt der Knopf &e+&r die Zutaten direkt in die Werkbank, wenn du sie dabeihast, mit Shift gleich einen ganzen Stapel.",
              "",
              "Oben im Rezeptfenster stehen Reiter: Werkbank, Ofen, Mixer, Infusionsanlage, Manabecken. Jede Maschine im Pack hat ihren eigenen Reiter, und die Pfeile wechseln zwischen mehreren Rezepten.",
          ],
          tasks=[task_checkmark("Nachgeschlagen")],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="minecraft:crafting_table"),

    quest("jei_bookmarks", 6, 8.5, "&eSetz Lesezeichen",
          subtitle="Deine Einkaufsliste links im Inventar.",
          description=[
              "Fahr über einen Gegenstand und drück &eA&r. Er landet in der Lesezeichenliste &elinks&r im Inventar, wieder A löscht ihn. Im Rezeptfenster gibt es außerdem ein Lesezeichen für das &eganze Rezept&r, dann siehst du die Zutaten ohne Nachschlagen.",
              "",
              "Vor einem großen Bau: alle Maschinen als Lesezeichen setzen, dann Zutat für Zutat abarbeiten. &eStrg und O&r blendet JEI ganz aus, wenn es im Weg ist.",
          ],
          tasks=[task_checkmark("Lesezeichen gesetzt")],
          rewards=[reward_xp(3)],
          deps=["jei_lookup"], icon="minecraft:book"),

    quest("jei_stages", 6, 10.5, "&eSchau in die nächste Stufe",
          subtitle="Gesperrt heißt sichtbar, nicht herstellbar.",
          description=[
              "JEI zeigt dir auch die Rezepte aller späteren Stufen. Der &eTooltip&r eines gesperrten Gegenstands sagt, mit welcher Stufe er öffnet. Du kannst ihn tragen und lagern, aber nicht halten, anlegen, setzen oder herstellen.",
              "",
              "Nutz das zum Vorausplanen: Zink, Osmium, Lebeholz und Quellsteine kannst du in Stufe 1 schon sammeln, damit dein Messingwerk am ersten Abend von Stufe 2 läuft.",
              "",
              "&eKronwerke:&r Was eine Stufe öffnet und was der Obelisk dafür will, steht im Kapitel &6Hier geht's los&r unter &eFünf Stufen&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["jei_lookup"], icon="minecraft:spyglass"),

    quest("jade", 9, 9.5, "&eLies den Block vor dir",
          subtitle="Jade zeigt, was du anschaust.",
          description=[
              "&6Jade&r blendet oben am Bildschirm ein, worauf du schaust: Name, Mod, bei Öfen und Maschinen den &eFortschritt&r, bei Tanks und Batterien den &eFüllstand&r, bei Truhen den Inhalt, bei Pflanzen die Reife, bei Mobs die Lebenspunkte.",
              "",
              "Halt &eShift&r gedrückt, dann zeigt Jade mehr Details. Welche Zeilen erscheinen, stellst du im Jade-Menü ein, die Taste dafür findest du in den Tastenbelegungen unter Jade.",
              "",
              "&eTipp:&r Jade verrät auch, welches Werkzeug ein Block braucht, und ob deine Spitzhacke dafür reicht.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(3)],
          deps=["jei_lookup"], icon="minecraft:knowledge_book"),

    # ---- Alltag --------------------------------------------------------------------
    quest("ultimine", 3, 14, "&6Grab mit Ultimine",
          subtitle="Halte die Taste, nimm die ganze Ader.",
          description=[
              "Halt &e`&r gedrückt (die Taste links neben der 1), schau auf einen Block und bau ihn ab. Alle passenden Nachbarblöcke gehen mit, bis zu &e64&r auf einmal. Das kostet Hunger, &e20-mal&r so viel wie ein normaler Block, also iss vorher.",
              "",
              "Mit gedrückter Taste und &eShift und Mausrad&r (oder Pfeiltasten) wechselst du die Form: &eFormlos&r für Adern und Bäume, &eKleiner Tunnel&r, &eGroßer Tunnel 3x3&r, &eKleines Quadrat 3x3&r, &eStollen&r und &eFluchttunnel&r nach oben.",
              "",
              "Ultimine kann noch mehr: Mit Taste und &eRechtsklick&r entrindet die Axt mehrere Stämme, die Hacke pflügt eine ganze Fläche, die Schaufel macht Pfade, und reife Pflanzen erntest du reihenweise. Eine einzelne Pflanze erntest du einfach mit Rechtsklick.",
              "",
              "&eKronwerke:&r Auf diesem Server darf &ejede Herkunft&r ultiminen. Neo Origins könnte das an eine Kraft binden, aber keine Herkunft im Pack hat so eine Kraft, also bleibt es für alle offen.",
          ],
          tasks=[task_checkmark("Ader abgebaut")],
          rewards=[reward_item("minecraft:cooked_beef", 8), reward_xp(5)],
          deps=["welcome"], icon="minecraft:iron_pickaxe"),

    quest("voice", 6, 13, "&6Sprich mit deinen Nachbarn",
          subtitle="Simple Voice Chat, nach Entfernung.",
          description=[
              "Drück &eV&r für das Menü von &6Simple Voice Chat&r: Mikrofon wählen, Lautstärke, Push-to-Talk oder Sprachaktivierung. Wer bis &e48 Blöcke&r entfernt ist, hört dich, leiser mit der Entfernung. Flüstern reicht 24 Blöcke.",
              "",
              "Im selben Menü legst du eine &6Gruppe&r an oder trittst einer bei. Gruppenmitglieder hören sich überall, auch über Dimensionen hinweg. Ein Symbol am Bildschirmrand zeigt, wer gerade spricht, und Aufnahmen über das Menü sind auf dem Server erlaubt.",
          ],
          tasks=[task_checkmark("Eingerichtet")],
          rewards=[reward_xp(3)],
          deps=["ultimine"], icon="minecraft:note_block", optional=True),

    quest("corpse", 6, 15, "&cHol deine Sachen zurück",
          subtitle="Dein Körper bleibt liegen, der Wegpunkt zeigt hin.",
          description=[
              "Stirbst du, bleibt ein &6Körper&r mit deiner ganzen Ausrüstung liegen. Lauf zurück, &eRechtsklick&r öffnet ihn wie eine Truhe. Der Wegpunkt von JourneyMap führt dich hin, und mit &eU&r öffnest du den &6Todesverlauf&r mit Ort, Zeit und Dimension jedes Todes.",
              "",
              "Ein leerer Körper verschwindet nach 30 Sekunden, ein voller nie. Nach einer Stunde wird er zum Skelett, der Inhalt bleibt.",
              "",
              "&cAchtung:&r Auf Kronwerke kann &ejeder&r deinen Körper öffnen. Wer in der Minendimension stirbt, sollte sich beeilen oder einen Freund fragen.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["ultimine"], icon="minecraft:skeleton_skull"),

    quest("trash", 9, 13, "&7Wirf weg, was stört",
          subtitle="Drei Mülltonnen, mit Filter und Rückgängig.",
          description=[
              "&eRezept:&r drei &6Stein&r oben, &6Bruchstein&r an den Seiten und unten, eine &6Truhe&r in der Mitte. Eine &6Mülltonne für Gegenstände&r.",
              "",
              "Alles, was du hineinlegst, ist weg. Fast: Der Knopf &eGelöschte anzeigen&r zeigt die letzten Gegenstände, und du bekommst sie zurück. Ein &6Filter&r mit neun Plätzen und Whitelist oder Blacklist macht sie zum Überlauf am Ende eines Rohrs: nur Bruchstein darf hinein.",
              "",
              "Dieselbe Form mit einem &6Eimer&r in der Mitte vernichtet Flüssigkeiten und Gase, mit einem &6Redstone&r Strom, mit einstellbarer Höchstrate als Lasttest für Generatoren. Alle drei zusammen ergeben die &6Ultimative Mülltonne&r.",
          ],
          tasks=[task_item("trashcans:item_trash_can", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["ultimine"], icon="trashcans:item_trash_can"),

    quest("sort", 9, 15, "&7Räum dein Inventar auf",
          subtitle="Inventory Tweak und Crafting Tweaks.",
          description=[
              "Drück im Inventar oder in einer offenen Truhe &eB&r, und &6Inventory Tweak&r sortiert nach Art, Name oder Seltenheit, je nach Einstellung. Fällt ein Werkzeug unter &e10 Prozent&r Haltbarkeit, warnt es dich mit Text und Ton.",
              "",
              "&6Crafting Tweaks&r setzt drei kleine Knöpfe neben die Werkbank: &eDrehen&r, &eAusgleichen&r (verteilt Stapel gleichmäßig) und &eLeeren&r. Rechtsklick auf das Ergebnis stellt gleich einen ganzen Stapel her.",
              "",
              "&eTipp:&r B ist auch die Wegpunkttaste von JourneyMap. Die stört nicht, weil sie nur außerhalb von Menüs greift.",
          ],
          tasks=[task_checkmark("Sortiert")],
          rewards=[reward_xp(3)],
          deps=["ultimine"], icon="minecraft:chest"),

    quest("done", 13, 14, "&6&lAlles eingerichtet",
          subtitle="Magnet, Sammler, Mülltonne, Claim.",
          description=[
              "Ein &6Magnet&r in der Tasche, ein &6Sammler&r an der ersten Farm, eine &6Mülltonne&r am Lager, die Basis beansprucht und ein Wegpunkt gesetzt. Damit bist du schneller als die meisten, die hier anfangen.",
              "",
              "Was jetzt kommt, steht in den großen Kapiteln: Create, Ars Nouveau, Botania, das Lager. Und wenn du vergisst, wie etwas geht: &eR&r in JEI.",
          ],
          tasks=[task_item("simplemagnets:basicmagnet", 1), task_item("itemcollectors:basic_collector", 1),
                 task_item("trashcans:item_trash_can", 1)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["collector", "trash", "chunkload"], icon="minecraft:diamond", size=2.0, shape="gear"),
]

images = [
    banner("comfort/title", "Komfort", 7.5, -4.5, height=1.75, kind="title", colour="brass"),
    banner("comfort/collect", "Sammeln", 6, -2.7, height=0.9, colour="water"),
    banner("comfort/pylons", "Pylonen", 14, -2.7, height=0.9, colour="magic"),
    banner("comfort/map", "Karte und Claims", 6, 3.3, height=0.9, colour="nature"),
    banner("comfort/knowledge", "Wissen", 6, 7.1, height=0.9, colour="stone"),
    banner("comfort/daily", "Alltag", 7, 11.6, height=0.9, colour="brass"),
]

chapter(C, "Komfort", "simplemagnets:basicmagnet", "storage", quests, shape="circle", order=55, stage=1,
        subtitle=["Stufe 1: die kleinen Mods, die den Tag leichter machen."], images=images)
