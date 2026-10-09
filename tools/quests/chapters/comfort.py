"""Comfort in stage 1: the small mods that make the day easier. Simple Magnets, Item Collectors
(advanced collector is stage 2 and only mentioned), Pylons (harvester; infusion, interdiction,
expulsion and protection are stage 2 and only mentioned), FTB Chunks claims and chunk loading,
JourneyMap, JEI, Jade, FTB Ultimine, Simple Voice Chat, Corpse, Trash Cans, Inventory Tweak and
Crafting Tweaks. Numbers follow the server configs in config/. Waystones has its own chapter.
Cobweb in the mod list is only the Crystal Nest library and has nothing for players; Xaero is not
in the pack (JourneyMap is). Mouse Tweaks is in the pack and covered in the tips chapter."""
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

    quest("magnet_charm", 4.5, 1.5, "&bSteck den Magneten in den Schmuckplatz",
          subtitle="Er wirkt auch dort, und das Inventar bleibt frei.",
          description=[
              "Drück &eG&r für deine &6Schmuckplätze&r. Der Magnet passt in den Platz &eAnhänger&r und zieht von dort genauso wie aus dem Inventar.",
              "",
              "So kann ihn Ultimine nicht aus Versehen mit Bruchstein zuschütten, und ein voller Rucksack verdrängt ihn nicht. Ein- und ausschalten geht weiter mit &eAlt+M&r.",
          ],
          tasks=[task_checkmark("Magnet angelegt")],
          rewards=[reward_xp(3)],
          deps=["magnet"], icon="simplemagnets:basicmagnet", optional=True),

    # ---- Pylonen -------------------------------------------------------------------
    quest("harvester", 12.5, 0, "&dLies, was der Erntepylon tut",
          subtitle="Ein Feld, das sich selbst erntet, ab Stufe 2.",
          description=[
              "&eRezept:&r drei &6Quarzstufen&r oben, &6Eisengitter&r, &6Heuballen&r, &6Eisengitter&r in der Mitte, drei &6Polierter Schwarzstein&r unten. Ein &6Erntepylon&r.",
              "",
              "Stell ihn in oder über den Wasserblock deines Feldes, eine &6Truhe&r direkt darüber und eine &6Hacke&r in den Pylon. Alle &e3 Sekunden&r erntet er reife Pflanzen im eingestellten Bereich, pflanzt nach und legt den Ertrag in die Truhe. Jede Ernte kostet die Hacke einen Punkt Haltbarkeit.",
              "",
              "&cHinweis:&r Quarz und Schwarzstein kommen aus dem Nether, der Pylon öffnet mit &eStufe 2&r. Sammle bis dahin den Heuballen und die Gitter. In Stufe 1 ernten der Trichter-Pflanztopf und die Create-Erntemaschine, siehe Kapitel Erste Farmen.",
              "",
              "Die Hacke lässt sich nicht per Rohr nachfüllen. Eine unzerbrechliche Hacke von Silent Gear oder einfach ein Stapel Steinhacken daneben hilft.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["collector"], icon="minecraft:hay_block", optional=True),

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
              "Geladen heißt: Maschinen, Farmen und Rohre laufen dort weiter, auch wenn niemand in der Nähe ist. Auf Kronwerke laufen sie auch, wenn &edein ganzes Team offline&r ist. Die Farm arbeitet über Nacht weiter.",
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

    quest("ping", 12, 5, "&aZeig deinem Team den Weg",
          subtitle="Ping Wheel: ein Klick, ein Zeichen in der Welt.",
          description=[
              "Ein Klick mit dem &eMausrad&r (mittlere Maustaste) setzt einen &6Ping&r dort, wo du hinschaust. Alle in der Nähe sehen ihn als Zeichen in der Welt, mit Entfernung, und am Bildschirmrand zeigt ein Pfeil die Richtung.",
              "",
              "Ein Ping hält &e7 Sekunden&r. Zielst du auf einen Gegenstand am Boden, zeigt er dessen Symbol. Ideal für \"Hier ist die Ader\" oder \"Pass auf, Creeper\".",
              "",
              "&eTipp:&r In den Einstellungen von Ping Wheel stellst du einen &eKanal&r ein. Dann sehen nur Spieler mit demselben Kanal deine Pings.",
          ],
          tasks=[task_checkmark("Gepingt")],
          rewards=[reward_xp(3)],
          deps=["journeymap"], icon="minecraft:target"),

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
              "Drück &eAlt+V&r für das Menü von &6Simple Voice Chat&r: Mikrofon wählen, Lautstärke, Push-to-Talk oder Sprachaktivierung. Wer bis &e48 Blöcke&r entfernt ist, hört dich, leiser mit der Entfernung. Flüstern reicht 24 Blöcke.",
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
              "Klick im Inventar oder in einer offenen Truhe mit dem &eMausrad&r (mittlere Maustaste), und &6Inventory Tweak&r sortiert nach Art, Name oder Seltenheit, je nach Einstellung. Fällt ein Werkzeug unter &e10 Prozent&r Haltbarkeit, warnt es dich mit Text und Ton.",
              "",
              "&6Crafting Tweaks&r setzt drei kleine Knöpfe neben die Werkbank: &eDrehen&r, &eAusgleichen&r (verteilt Stapel gleichmäßig) und &eLeeren&r. Rechtsklick auf das Ergebnis stellt gleich einen ganzen Stapel her.",
              "",
              "&eTipp:&r B ist auch die Wegpunkttaste von JourneyMap. Die stört nicht, weil sie nur außerhalb von Menüs greift.",
          ],
          tasks=[task_checkmark("Sortiert")],
          rewards=[reward_xp(3)],
          deps=["ultimine"], icon="minecraft:chest"),

    quest("compress", 12, 15.5, "&7Press Barren mit einer Taste",
          subtitle="Crafting Tweaks: verdichten und nachfüllen.",
          description=[
              "Im Fenster der Werkbank fährst du mit der Maus über einen Stapel &6Barren&r und drückst &eK&r: &6Crafting Tweaks&r presst ihn zu Blöcken. &eStrg+K&r presst nur einen Block, &eShift+K&r alles dieser Sorte.",
              "",
              "&eTab&r füllt das Raster wieder mit dem letzten Rezept, &eStrg+Tab&r nur einmal. Praktisch, wenn du dreißig Mal dasselbe herstellst.",
          ],
          tasks=[task_checkmark("Verdichtet")],
          rewards=[reward_item("minecraft:iron_ingot", 9), reward_xp(3)],
          deps=["sort"], icon="minecraft:iron_block"),

    quest("wrench", 12, 12.5, "&7Dreh Blöcke mit dem Schraubenschlüssel",
          subtitle="Treppe falsch herum? Nicht abbauen.",
          description=[
              "&eRezept:&r vier &6Kupferbarren&r: zwei oben an den Ecken, zwei untereinander in der Mitte darunter. Der &6Schraubenschlüssel&r von Supplementaries.",
              "",
              "&eRechtsklick&r auf einen Block dreht ihn. Treppen, Stämme, Truhen, Trichter: alles, was eine Richtung hat. Gerade beim Bauen und an Trichterketten spart das viel Abbauen und neu Setzen.",
              "",
              "Den &6Schraubenschlüssel&r von Create brauchst du trotzdem für Create-Blöcke. Beide nebeneinander in der Leiste schaden nicht.",
          ],
          tasks=[task_item("supplementaries:wrench", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8), reward_xp(3)],
          deps=["trash"], icon="supplementaries:wrench"),

    quest("cage", 15, 12.5, "&7Trag ein Tier im Käfig",
          subtitle="Kühe umziehen, ohne Leine und Weizen.",
          description=[
              "&eRezept:&r drei &6Eisenbarren&r oben, zwei &6Eisengitter&r an den Seiten, drei &6Holzstufen&r unten. Ein &6Mobkäfig&r.",
              "",
              "Mit dem Käfig in der Hand klickst du ein Tier an, und es sitzt drin. Ein Rechtsklick auf den Boden lässt es dort wieder frei. Mit &eShift&r stellst du den Käfig samt Tier als Block auf.",
              "",
              "Zähmbare Tiere wie Wölfe und Katzen müssen erst gezähmt sein. Passt ein Wesen nicht hinein, sagt dir das der Käfig.",
          ],
          tasks=[task_item("supplementaries:cage", 1)],
          rewards=[reward_item("minecraft:wheat", 16), reward_xp(3)],
          deps=["wrench"], icon="supplementaries:cage", optional=True),

    quest("jar", 15, 14, "&7Füll ein Gefäß",
          subtitle="Flüssigkeit, Kekse und kleine Wesen im Glas.",
          description=[
              "&eRezept:&r Glas oben links und rechts, eine &6Holzstufe&r oben in der Mitte, Glas an den Seiten und unten. Ein &6Gefäß&r von Supplementaries.",
              "",
              "Es nimmt Flüssigkeiten aus Flaschen, Eimern und Schüsseln auf, dazu Kekse und kleine Wesen. Abgebaut behält es seinen Inhalt. Ein Gefäß mit Honig, Milch oder Wasser auf dem Regal ist zugleich Vorrat und Deko.",
          ],
          tasks=[task_item("supplementaries:jar", 1)],
          rewards=[reward_item("minecraft:glass", 8), reward_xp(2)],
          deps=["cage"], icon="supplementaries:jar", optional=True),

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

    # ---- Rasten -------------------------------------------------------------------
    quest("sleeping_bag", 3, 19, "&6Näh einen Schlafsack",
          subtitle="Die Nacht überspringen, wo du gerade bist.",
          description=[
              "&eRezept:&r drei &6Wolle&r senkrecht übereinander. Ein &6Schlafsack&r von Comforts, gefärbt wird er wie ein Bett mit Farbstoff.",
              "",
              "Setz ihn ab, und du legst dich sofort hinein. Er geht nur &enachts&r und setzt deinen Spawnpunkt &enicht&r um. Dein Bett zu Hause bleibt also dein Zuhause.",
              "",
              "Wer ihn benutzt, hält auch die &6Phantome&r fern, genau wie mit einem Bett.",
          ],
          tasks=[task_item("comforts:sleeping_bag_white", 1)],
          rewards=[reward_item("minecraft:white_wool", 6), reward_xp(3)],
          deps=["welcome"], icon="comforts:sleeping_bag_white"),

    quest("hammock", 6, 18, "&6Häng eine Hängematte auf",
          subtitle="Den Tag verschlafen, bis es dunkel ist.",
          description=[
              "&eRezept:&r ein &6Stock&r oben und unten in der Mitte, dazwischen &6Faden&r, &6Wolle&r, &6Faden&r: der &6Hängemattenstoff&r. Dazu zweimal &6Seil und Nägel&r (ein Eisenbarren und ein Seil von Supplementaries ergeben zwei).",
              "",
              "Die beiden Nägel kommen an zwei gegenüberliegende Wände, der Stoff dazwischen. Die Hängematte geht nur &etagsüber&r und schläft bis zum Abend, das Gegenstück zum Schlafsack.",
              "",
              "Praktisch, wenn deine Farm Monster braucht oder du lieber nachts gräbst.",
          ],
          tasks=[task_item("comforts:hammock_white", 1), task_item("comforts:rope_and_nail", 2)],
          rewards=[reward_item("minecraft:string", 8), reward_xp(3)],
          deps=["sleeping_bag"], icon="comforts:hammock_white", optional=True),

    quest("campfire", 6, 20, "&6Wärm dich am Lagerfeuer",
          subtitle="Ein brennendes Feuer heilt alle in der Nähe.",
          description=[
              "Ein brennendes &6Lagerfeuer&r gibt jedem Spieler in &e16 Blöcken&r Umkreis &eRegeneration I&r für &e60 Sekunden&r. Das kommt von &6Healing Campfire&r und wird alle zwei Sekunden aufgefrischt.",
              "",
              "Ein &6Seelenlagerfeuer&r wirkt genauso, Tiere in der Nähe heilt es auch. Ist das Feuer aus, passiert nichts.",
              "",
              "&eTipp:&r Eins in der Mitte der Basis, eins am Eingang zur Mine. Nach einem Kampf stellst du dich kurz daneben, statt dein Essen zu verbrauchen.",
          ],
          tasks=[task_item("minecraft:campfire", 1)],
          rewards=[reward_item("minecraft:charcoal", 8), reward_xp(3)],
          deps=["sleeping_bag"], icon="minecraft:campfire"),

    quest("lunch_basket", 9, 20, "&6Pack einen Picknickkorb",
          subtitle="Sechs Stapel Essen in einem Platz.",
          description=[
              "&eRezept:&r ein &6Bambus&r oben in der Mitte, Bambus links und rechts in der Mitte, ein &6Teppich&r in der Mitte, drei Bambus unten. Der &6Picknickkorb&r von Supplementaries.",
              "",
              "Er fasst &e6 Stapel&r Essen und belegt nur einen Platz im Inventar. Mit der &eAngriffstaste&r schaltest du ihn zwischen offen und geschlossen, aus einem offenen Korb isst du direkt.",
              "",
              "Abgestellt ist er auch ein Block, gut für den Tisch in der Küche.",
          ],
          tasks=[task_item("supplementaries:lunch_basket", 1)],
          rewards=[reward_item("minecraft:bamboo", 16), reward_item("minecraft:baked_potato", 16)],
          deps=["campfire"], icon="supplementaries:lunch_basket"),
]

images = []

images = [
    banner("comfort/title", "Komfort", 7.5, -4.5, height=1.75, kind="title", colour="brass"),
    banner("comfort/collect", "Sammeln", 6, -2.7, height=0.9, colour="water"),
    banner("comfort/pylons", "Pylonen", 14, -2.7, height=0.9, colour="magic"),
    banner("comfort/map", "Karte und Claims", 6, 3.3, height=0.9, colour="nature"),
    banner("comfort/knowledge", "Wissen", 6, 7.1, height=0.9, colour="stone"),
    banner("comfort/daily", "Alltag", 7, 11.6, height=0.9, colour="brass"),
    banner("comfort/rest", "Rasten", 6, 16.8, height=0.9, colour="nature"),
]

chapter(C, "Komfort", "simplemagnets:basicmagnet", "storage", quests, shape="circle", order=55, stage=1,
        subtitle=["Stufe 1: die kleinen Mods, die den Tag leichter machen."], images=images)
