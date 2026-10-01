"""Create in stage 2 (Messingwerk): the blaze burner with its Source Gem recipe, brass, electron
tubes, deployers, the precision mechanism (the Kronwerke sequence on a brass sheet, one quest per
step), mechanical crafters, crushing wheels and blaze cakes, steam, brass logistics, the brass
contraptions, the Messingherz milestone, and the Create addons that create_addons.py builds on:
Enchantment Industry basics, Power Grid (one quest per generator part), Crafts & Additions and the
first Create Connected parts. Recipes follow kubejs/server_scripts/kronwerke/create.js and
tech_and_magic.js; stress numbers come from create-server.toml and powergrid-server.toml.
Trains are in create_trains.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create_brass"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


# Column A starts at x 0, column B at x 19.
A, B = 0, 19

quests = [
    # ---- Messing ----------------------------------------------------------------
    quest("welcome", A, 3, "&6&lHol dir den ersten Messingbarren",
          subtitle="Stufe 2 ist offen, Create bekommt seine zweite Hälfte.",
          description=[
              "Nimm einen &6Messingbarren&r aus dem Starterpaket der Stufe oder misch ihn selbst. Wie das geht, zeigen die nächsten Quests.",
              "",
              "Alles mit Messingrahmen kann mehr als die Andesit-Maschinen: filtern, zählen, Rezepte jeder Größe herstellen. Züge stehen in &6Create: Züge&r, Weichen, Dieselmotoren und weitere Addons in &6Create: Addons&r.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler will &62 000 Messingbarren&r und &6150 Präzisionsgetriebe&r (für 30 Spieler), dazu &68 Messingherzen&r. &e/kw goals&r zeigt den Stand.",
          ],
          tasks=[task_item("create:brass_ingot", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          icon="create:brass_ingot", size=2.0, shape="hexagon"),

    quest("zinc", A + 2.5, 1.5, "&6Horte Kupfer und Zink",
          subtitle="Zwei Teile Kupfer, ein Teil Zink.",
          description=[
              "Sammle &664 Zinkbarren&r und &6128 Kupferbarren&r. Jeder Messingbarren kostet zwei Kupfer und ein Zink.",
              pic("create:zinc_ingot"),
              "Die Mining Dimension ist dafür ideal, dort bleibt die Landschaft um die Basen heil. Wer nur Zink hortet, steht am Mixer mit leerer Kupferkiste da.",
          ],
          tasks=[task_item("create:zinc_ingot", 64), task_item("minecraft:copper_ingot", 128)],
          rewards=[reward_item("create:raw_zinc", 32), reward_xp(3)],
          deps=["welcome"]),

    quest("source_gems", A + 2.5, 3, "&dBesorg zwei Quelljuwelen",
          subtitle="Ohne Magie kein Lohenbrenner.",
          description=[
              "Hol dir zwei &dQuelljuwelen&r aus der &aImbuement-Kammer&r von Ars Nouveau, selbst gemacht oder von einem Magier.",
              pic("ars_nouveau:source_gem"),
              "&eRezept auf Kronwerke:&r Das Gehäuse des Lohenbrenners braucht zwei Quelljuwelen. Zwei Juwelen gegen ein paar Messingbarren ist ein fairer Tausch.",
          ],
          tasks=[task_item("ars_nouveau:source_gem", 2)],
          rewards=[reward_item("minecraft:amethyst_shard", 8), reward_xp(3)],
          deps=["welcome"]),

    quest("nether", A + 2.5, 4.5, "&cHol Netherrack und Quarz",
          subtitle="Der Nether liefert, was Messing braucht.",
          description=[
              "Bring &616 Netherrack&r und &68 Netherquarz&r aus dem Nether mit. Netherrack steckt im Brenner, Quarz im Rosenquarz.",
              "",
              "Lohen und ihre Ruten findest du in &cNetherfestungen&r. Nimm Feuerresistenz mit, Lohen schießen Feuerbälle. Mehr im Kapitel &6Der Nether&r.",
          ],
          tasks=[task_item("minecraft:netherrack", 16), task_item("minecraft:quartz", 8)],
          rewards=[reward_table("s2_common"), reward_xp(3)],
          deps=["welcome"], icon="minecraft:netherrack"),

    quest("empty_burner", A + 5, 3.75, "&6Bau einen Leeren Lohenbrenner",
          subtitle="Ein Käfig für eine Lohe, mit Magie verschlossen.",
          description=[
              "&eRezept auf Kronwerke:&r Oben Quelljuwel, Eisenblech, Quelljuwel. Mitte Eisenblech, &6Netherrack&r, Eisenblech. Unten nur ein Eisenblech.",
              "",
              "Also vier &6Eisenbleche&r, ein Netherrack und zwei &dQuelljuwelen&r. JEI zeigt das geänderte Rezept.",
          ],
          tasks=[task_item("create:empty_blaze_burner", 1)],
          rewards=[reward_item("create:iron_sheet", 8), reward_xp(3)],
          deps=["source_gems", "nether"], icon="create:empty_blaze_burner", size=1.5),

    quest("blaze_burner", A + 7.5, 3.75, "&6Fang eine Lohe ein",
          subtitle="Der Lohenbrenner heizt für dich.",
          description=[
              "Rechtsklicke eine &6Lohe&r mit dem leeren Brenner in der Hand, auch direkt am Spawner in der Festung. Du hältst einen &6Lohenbrenner&r.",
              "",
              "Unter einem Becken glimmt er nur. Mit Ofenbrennstoff (Kohle, Holz) ist er &cerhitzt&r, mit einem &6Lohenkuchen&r eine Weile &cüberhitzt&r. Eine Schleuse oder ein Arm füttert ihn.",
          ],
          tasks=[task_item("create:blaze_burner", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_table("s2_common")],
          deps=["empty_burner"], icon="create:blaze_burner", size=2.0, shape="hexagon"),

    quest("blaze_powder", A + 5, 5.5, "&6Mach Lohenstaub",
          subtitle="Der Preis für das erste Messing.",
          description=[
              "Eine &6Lohenrute&r an der Werkbank gibt zwei &6Lohenstaub&r. Ruten lassen Lohen in Netherfestungen fallen.",
              "",
              "Zwischen &6Mahlwerkrädern&r gibt eine Rute drei Staub, mit 25 Prozent Chance drei mehr. Der Mahlstein mahlt keine Ruten.",
          ],
          tasks=[task_item("minecraft:blaze_powder", 16)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_xp(3)],
          deps=["nether"], icon="minecraft:blaze_powder"),

    quest("brass_mixing", A + 10, 3, "&6Misch Messing im heißen Becken",
          subtitle="Kupfer, Zink und ein Hauch Lohe.",
          description=[
              "Von unten: &6Lohenbrenner&r mit Kohle, &6Becken&r, ein Block Luft, &6Mechanischer Mixer&r. Hinein: &6zwei Kupferbarren&r, &6ein Zinkbarren&r, &6ein Lohenstaub&r.",
              pic("create:brass_ingot"),
              "&eRezept auf Kronwerke:&r Das ergibt &eeinen&r Messingbarren. Andere Wege (Legierungsofen, Gießerei, Oritech, Messingbiene) machen kein Messing mehr.",
              "",
              "&cBleibt der Mixer stehen?&r Glimmt der Brenner nur, fehlt Brennstoff. Fehlt eine der drei Zutaten, rührt er nicht.",
          ],
          tasks=[task_item("create:brass_ingot", 64)],
          rewards=[reward_item("minecraft:copper_ingot", 32), reward_item("create:zinc_ingot", 16), reward_xp(5)],
          deps=["blaze_burner", "zinc", "blaze_powder"], icon="create:brass_ingot", size=2.0, shape="gear"),

    quest("brass_casing", A + 12.5, 2, "&6Ummantel Holz mit Messing",
          subtitle="Der Messingrahmen, Gerüst jeder schlauen Maschine.",
          description=[
              "Rechtsklicke einen gesetzten, entrindeten Stamm mit einem &6Messingbarren&r: er wird zum &6Messingrahmen&r.",
              "",
              "&eKronwerke:&r Die Botaniker brauchen ihn: die Terraplatte will zwei, Manaperlen entstehen nur über einem Messingrahmen, der Runenaltar will einen Messingbarren. Beide Pfeiler müssen voll werden.",
          ],
          tasks=[task_item("create:brass_casing", 16)],
          rewards=[reward_item("minecraft:stripped_oak_log", 16), reward_xp(3)],
          deps=["brass_mixing"]),

    quest("brass_sheet", A + 12.5, 4, "&6Press Messingbleche",
          subtitle="Die Grundlage für Hand und Getriebe.",
          description=[
              "Leg &6Messingbarren&r unter die Presse. Jeder wird zu einem &6Messingblech&r.",
              "",
              "Jedes Präzisionsgetriebe beginnt auf einem Messingblech. Eine eigene Presse nur für Messing lohnt sich.",
          ],
          tasks=[task_item("create:brass_sheet", 16)],
          rewards=[reward_item("create:brass_ingot", 8), reward_xp(3)],
          deps=["brass_mixing"]),

    # ---- Präzision ----------------------------------------------------------------
    quest("rose_quartz", A, 9.25, "&6Färb Quarz zu Rosenquarz",
          subtitle="Ein Quarz, acht Redstone.",
          description=[
              "Ein &6Netherquarz&r und acht &6Redstone&r im Handwerksraster ergeben einen &6Rosenquarz&r.",
          ],
          tasks=[task_item("create:rose_quartz", 8)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(3)],
          deps=["nether"]),

    quest("polish", A + 2.5, 9.25, "&6Polier Rosenquarz",
          subtitle="Schmirgelpapier in die Hand.",
          description=[
              "&6Schmirgelpapier&r (Papier und Sand) in die Haupthand, &6Rosenquarz&r in die Nebenhand, rechte Maustaste halten. Heraus kommt &6Polierter Rosenquarz&r.",
              pic("create:polished_rose_quartz"),
              "Am Band erledigt das ein Einsatzgerät mit Schmirgelpapier, oder der Schleifstein aus Enchantment Industry.",
          ],
          tasks=[task_item("create:polished_rose_quartz", 8)],
          rewards=[reward_item("create:sand_paper", 4), reward_xp(3)],
          deps=["rose_quartz"]),

    quest("electron_tube", A + 5, 9.25, "&6Bau Elektronenröhren",
          subtitle="Die Logik in jeder Messingmaschine.",
          description=[
              "&6Polierter Rosenquarz&r über einem &6Eisenblech&r ergibt eine &6Elektronenröhre&r.",
              pic("create:electron_tube"),
              "Sie steckt in Einsatzgerät, Messingschleuse, Zugsignal und Anzeigetafel. Jede Runde des Präzisionsgetriebes frisst eine, und Mekanism macht seinen ersten Schaltkreis daraus.",
          ],
          tasks=[task_item("create:electron_tube", 16)],
          rewards=[reward_item("create:iron_sheet", 16), reward_xp(4)],
          deps=["polish"]),

    quest("brass_hand", A + 5, 7.75, "&6Form eine Messing Hand",
          subtitle="Finger aus Blech.",
          description=[
              "Vier &6Messingbleche&r und eine &6Andesitlegierung&r ergeben eine &6Messing Hand&r: Legierung oben, drei Bleche in der Mitte, eins unten.",
              pic("create:brass_hand"),
          ],
          tasks=[task_item("create:brass_hand", 3)],
          rewards=[reward_item("create:brass_sheet", 4), reward_xp(4)],
          deps=["brass_sheet"]),

    quest("deployer", A + 7.5, 8.5, "&6Bau drei Einsatzgeräte",
          subtitle="Eine Hand, die benutzt, was sie hält.",
          description=[
              "&6Elektronenröhre&r, &6Andesitgehäuse&r und &6Messing Hand&r untereinander ergeben das &6Einsatzgerät&r. Es tut mit seinem Item, was ein Spieler täte.",
              "",
              "Über Depot oder Band wendet es sein Item auf alles darunter an: Schmirgelpapier auf Rosenquarz, Bretter auf Wellen für Zahnräder. JEI listet alles unter &eEinsetzen&r. Es kostet &d4 SU pro RPM&r.",
              "",
              "Für die Präzisionslinie brauchst du drei: Zahnrad, Röhre, Klumpen.",
          ],
          tasks=[task_item("create:deployer", 3)],
          rewards=[reward_item("create:andesite_alloy", 32), reward_table("s2_common")],
          deps=["electron_tube", "brass_hand"], icon="create:deployer", size=1.75, shape="gear"),

    quest("incomplete", A + 10, 8.5, "&6Lass ein Blech eine Runde drehen",
          subtitle="Sequenzielle Montage, Schritt für Schritt.",
          description=[
              "Ein &6Messingblech&r aufs Band. Einsatzgerät 1 setzt ein &6Zahnrad&r ein, Einsatzgerät 2 eine &6Elektronenröhre&r, Einsatzgerät 3 einen &6Eisenklumpen&r, dann stampft eine &6Presse&r.",
              pic("create:incomplete_precision_mechanism"),
              "&eRezept auf Kronwerke:&r Danach ist es ein &6Unfertiges Präzisionsgetriebe&r. Es muss &efünf Runden&r durch dieselbe Strecke. Gib jedem Einsatzgerät per Filter nur sein Teil.",
          ],
          tasks=[task_item("create:incomplete_precision_mechanism", 1)],
          rewards=[reward_item("create:electron_tube", 4), reward_xp(4)],
          deps=["deployer"]),

    quest("precision", A + 12.5, 8.5, "&6&lBau ein Präzisionsgetriebe",
          subtitle="Fünf Runden, dann fällt es vom Band.",
          description=[
              "Führ das Band im Kreis, dann drehen unfertige Teile ihre fünf Runden von selbst. Fertige Getriebe zieht eine Schleuse mit Filter ab.",
              pic("create:precision_mechanism"),
              "&eRezept auf Kronwerke:&r Nur &e60 Prozent&r werden ein Getriebe. Sonst Schrott: &6Messingklumpen&r (25 Prozent) oder ein &6Zahnrad&r (15 Prozent).",
              "",
              "Im Schnitt kostet ein Getriebe &e1,7 Messingbleche&r und je gut &eacht&r Zahnräder, Röhren und Eisenklumpen. Die Röhren sind der Engpass.",
          ],
          tasks=[task_item("create:precision_mechanism", 8)],
          rewards=[reward_item("create:electron_tube", 16), reward_table("s2_uncommon")],
          deps=["incomplete"], icon="create:precision_mechanism", size=2.0, shape="gear"),

    quest("precision_line", A + 15, 8.5, "&6Lass die Präzisionslinie laufen",
          subtitle="Getriebe am laufenden Band.",
          description=[
              "Automatisier alle Zutaten: eine Presse für Messingbleche, ein Einsatzgerät setzt Bretter auf Wellen für Zahnräder, Eisenklumpen aus der Erzwäsche, Röhren aus der Röhrenlinie.",
              "",
              "Schleusen füllen die Einsatzgeräte nach, der Schrott läuft zurück, die Getriebe gehen in eine Kiste oder gleich in den Einspeiser am Obelisken.",
              "",
              "&eKronwerke:&r 150 für den Obelisken, eins pro Messingherz, und viele Maschinen anderer Mods wollen welche: AE2-Assembler, IE-Schwerbaustein, die PneumaticCraft-Drohne.",
          ],
          tasks=[task_item("create:precision_mechanism", 64)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["precision"]),

    quest("crafter", A + 12.5, 10.75, "&6Stell Mechanische Handwerkseinheiten auf",
          subtitle="Rezepte bis 9 x 9 Felder.",
          description=[
              "&eRezept auf Kronwerke:&r &6Präzisionsgetriebe&r, &6Messingrahmen&r und &6Werkbank&r untereinander ergeben drei &6Mechanische Handwerkseinheiten&r.",
              "",
              "Stell sie als Raster auf, eine pro Rezeptfeld, und richte ihre Pfeile mit dem Schraubenschlüssel auf eine Ausgabe-Einheit. Zutaten rein, Rotation drauf, bei vollen Feldern legen sie los.",
              "",
              "Leere Felder deckst du mit einer &6Handwerkseinheit Slot Abdeckung&r ab. Sie kosten &d2 SU pro RPM&r.",
          ],
          tasks=[task_item("create:mechanical_crafter", 9)],
          rewards=[reward_item("create:electron_tube", 8), reward_table("s2_common")],
          deps=["precision"]),

    quest("tube_line", A + 15, 10.75, "&6Bau eine Röhrenlinie",
          subtitle="Der Engpass, automatisch.",
          description=[
              "Rosenquarz aufs Band, ein &6Einsatzgerät&r mit Schmirgelpapier poliert ihn, zwei &6Handwerkseinheiten&r übereinander setzen ihn auf ein Eisenblech.",
              "",
              "Pro Präzisionsgetriebe brauchst du im Schnitt über acht Röhren. Ohne diese Linie steht die Präzisionslinie bald still.",
          ],
          tasks=[task_item("create:electron_tube", 128)],
          rewards=[reward_item("minecraft:quartz", 32), reward_table("s2_uncommon")],
          deps=["crafter"], icon="create:electron_tube"),

    quest("crushing_wheel", A + 12.5, 12.75, "&6Bau Mahlwerkräder",
          subtitle="Zerkleinern mit Bonus.",
          description=[
              "Ein 5 x 5 Rezept für die Handwerkseinheiten: &616 Andesitlegierungen&r, &64 Bretter&r, &61 Stein&r ergeben zwei &6Mahlwerkräder&r.",
              "",
              "Zwei Räder mit einem Block Abstand, drehend &eaufeinander zu&r. Was oben hineinfällt, wird zermahlen. Jedes Rad kostet &d8 SU pro RPM&r, zwei bei 64 RPM also 1 024 SU.",
              "",
              "&cVorsicht:&r Sie verletzen auch dich. Mekanisms Zerkleinerer braucht auf Kronwerke ebenfalls ein Mahlwerkrad.",
          ],
          tasks=[task_item("create:crushing_wheel", 2)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_xp(4)],
          deps=["crafter"]),

    quest("ore_processing", A + 15, 12.75, "&6Zerkleinere und wasch Erz",
          subtitle="Klumpen plus Beigaben.",
          description=[
              "&6Rohzink&r zwischen den Rädern wird zu &6Zerkleinertem Rohzink&r (75 Prozent Chance auf einen Erfahrungsklumpen). Gewaschen gibt es &e9 Zinkklumpen&r und mit 25 Prozent Schießpulver.",
              pic("create:crushed_raw_zinc"),
              "Rohkupfer gibt gewaschen Ton dazu, Roheisen Redstone. Mit Behutsamkeit abgebaute Erzblöcke geben 1,75 Zerkleinerte Erze.",
          ],
          tasks=[task_item("create:crushed_raw_zinc", 32)],
          rewards=[reward_table("s2_common"), reward_xp(4)],
          deps=["crushing_wheel"]),

    quest("cinder_flour", A + 10, 12.75, "&6Mahl Netherrack zu Aschenmehl",
          subtitle="Der erste Schritt zum Lohenkuchen.",
          description=[
              "Wirf &6Netherrack&r zwischen die Mahlwerkräder. Jeder Block gibt ein &6Aschenmehl&r, mit 50 Prozent ein zweites.",
              "",
              "Der Mahlstein mahlt kein Netherrack, dafür brauchst du die Räder.",
          ],
          tasks=[task_item("create:cinder_flour", 16)],
          rewards=[reward_item("minecraft:netherrack", 64), reward_xp(4)],
          deps=["crushing_wheel"]),

    quest("blaze_cake", A + 10, 14.5, "&6Back einen Lohenkuchen",
          subtitle="Überhitzt heißt doppeltes Messing.",
          description=[
              "Presse über Becken: &6Aschenmehl&r, &6Zucker&r und ein &6Ei&r ergeben die &6Lohenkuchenbasis&r. Ein &6Ausguss&r füllt &b250 mB Lava&r hinein: fertig ist der &6Lohenkuchen&r.",
              pic("create:blaze_cake"),
              "Gib ihn dem Brenner, und er ist eine Weile &cüberhitzt&r. Ein Arm oder eine Schleuse legt nach.",
          ],
          tasks=[task_item("create:blaze_cake", 4)],
          rewards=[reward_item("minecraft:egg", 16), reward_item("minecraft:sugar", 16), reward_xp(5)],
          deps=["cinder_flour"], icon="create:blaze_cake"),

    quest("brass_superheated", A + 12.5, 14.5, "&6Misch Messing überhitzt",
          subtitle="Zwei Barren pro Rezept, kein Staub.",
          description=[
              "Ein Mixer über einem Becken, darunter ein Lohenbrenner, der mit Kuchen &cüberhitzt&r bleibt. &6Zwei Kupfer&r und &6ein Zink&r ergeben &ezwei Messingbarren&r.",
              "",
              "&eRezept auf Kronwerke:&r Erhitzt machen 2 000 Kupfer und 1 000 Zink nur 1 000 Barren und fressen 1 000 Lohenstaub. Überhitzt werden daraus 2 000 Barren.",
              "",
              "Zwei oder drei Mixer aus einem gemeinsamen Tresor sind ein guter Anfang für das Obelisk-Ziel.",
          ],
          tasks=[task_item("create:brass_ingot", 256)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["blaze_cake"], icon="create:blaze_burner", size=1.5),

    # ---- Messing-Logistik -------------------------------------------------------
    quest("brass_funnel", A, 19, "&6Filter mit der Messingschleuse",
          subtitle="Ein Item, eine Stückzahl.",
          description=[
              "&6Elektronenröhre&r, &6Messingbarren&r und &6getrockneter Seetang&r untereinander ergeben zwei &6Messingschleusen&r.",
              "",
              "Sie hat ein &eFilterfeld&r für ein Item oder einen Filter und eine einstellbare &eStückzahl&r. Ein &6Attribut Filter&r (Messingklumpen und Wolle) filtert nach Eigenschaften, etwa alles Verzauberte.",
          ],
          tasks=[task_item("create:brass_funnel", 4)],
          rewards=[reward_item("create:brass_ingot", 16), reward_xp(3)],
          deps=["electron_tube"]),

    quest("brass_tunnel", A + 2.5, 18, "&6Sortier mit dem Messingtunnel",
          subtitle="Aufteilen, reihum oder synchron.",
          description=[
              "&6Elektronenröhre&r, zwei &6Messingbarren&r und zwei &6getrockneter Seetang&r ergeben zwei &6Messingtunnel&r. Setz sie oben auf ein Band.",
              "",
              "Am Wertefeld wählst du: aufteilen, reihum, zum nächsten Ausgang, zufällig oder synchron. Mit Filter schickt er nur bestimmte Items zur Seite.",
          ],
          tasks=[task_item("create:brass_tunnel", 4)],
          rewards=[reward_item("minecraft:dried_kelp", 16), reward_xp(3)],
          deps=["brass_funnel"]),

    quest("smart_chute", A + 2.5, 20, "&6Bau einen Schlauen Schacht",
          subtitle="Ein Schacht mit Filter.",
          description=[
              "&6Messingblech&r, &6Schacht&r und &6Elektronenröhre&r untereinander ergeben den &6Schlauen Schacht&r. Er lässt nur durch, was seinem Filter entspricht, in der Menge, die du einstellst.",
          ],
          tasks=[task_item("create:smart_chute", 2)],
          rewards=[reward_xp(3)],
          deps=["brass_funnel"], optional=True),

    quest("arm", A + 5, 19, "&6Lass den Mechanischen Arm greifen",
          subtitle="Nimmt hier, legt dort.",
          description=[
              "Drei &6Messingbleche&r, &6Andesitlegierung&r, &6Präzisionsgetriebe&r und &6Messingrahmen&r ergeben den &6Mechanischen Arm&r. Klick vor dem Setzen seine Ziele an: einmal &eEingabe&r, zweimal &eAusgabe&r.",
              "",
              "Er reicht &e5 Blöcke&r weit und bedient Depots, Bänder, Kisten, Becken, Lohenbrenner und Handwerkseinheiten. Er kostet &d2 SU pro RPM&r.",
          ],
          tasks=[task_item("create:mechanical_arm", 1)],
          rewards=[reward_item("create:brass_ingot", 16), reward_table("s2_common")],
          deps=["brass_funnel", "precision"], icon="create:mechanical_arm", size=1.5),

    quest("observer", A + 7.5, 18, "&6Lass Redstone Items erkennen",
          subtitle="Schlauer Beobachter und Schwellwert-Schalter.",
          description=[
              "&6Elektronenröhre&r, &6Messingrahmen&r und &6Beobachter&r ergeben den &6Schlauen Beobachter&r. Mit &6Komparator&r statt Beobachter wird es der &6Schwellwert-Schalter&r.",
              "",
              "Der Beobachter meldet ein bestimmtes Item, der Schalter schaltet ein, wenn ein Lager über einen Füllstand steigt, und aus, wenn es darunter fällt. Mit einer Kupplung hält die Anlage bei vollem Lager.",
          ],
          tasks=[task_item("create:content_observer", 1), task_item("create:stockpile_switch", 1)],
          rewards=[reward_xp(3)],
          deps=["arm"], optional=True),

    quest("display", A + 7.5, 20, "&6Schreib Zahlen an die Wand",
          subtitle="Anzeige-Link und Anzeigetafel.",
          description=[
              "Ein &6Sender&r auf einem &6Messingrahmen&r ergibt den &6Anzeige-Link&r. &6Legierung, Röhre, Legierung&r ergeben zwei &6Anzeigetafeln&r.",
              "",
              "Klick mit dem Link erst das Ziel an, dann setz ihn an die Quelle, bis &e64 Blöcke&r entfernt. Füllstände, SU oder Abfahrtszeiten erscheinen auf der Tafel.",
          ],
          tasks=[task_item("create:display_link", 1), task_item("create:display_board", 4)],
          rewards=[reward_xp(3)],
          deps=["arm"], optional=True),

    quest("factory_gauge", A + 10, 19, "&6Lass die Fabrik selbst bestellen",
          subtitle="Die Fabrikanzeige.",
          description=[
              "Eine &6Lagerverbindung&r und ein &6Präzisionsgetriebe&r ergeben zwei &6Fabrikanzeigen&r. Stimm sie auf dein Lagernetz ab und setz sie an die Maschine, die ein Item herstellt.",
              "",
              "Stell das Item und den Vorrat ein. Fällt er darunter, bestellt die Anzeige die Zutaten aus dem Netz und schickt sie per Paket. Mehrere Anzeigen verbunden ergeben ganze Ketten.",
          ],
          tasks=[task_item("create:factory_gauge", 2)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["arm"], icon="create:factory_gauge", size=1.5),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("brass_heart", A + 3, 25, "&6Bau ein Messingherz",
          subtitle="Der Meilenstein des Messingwerks.",
          description=[
              "Oben &6Messingrahmen&r, &6Präzisionsgetriebe&r, Messingrahmen. Mitte &6Elektronenröhre&r, &cRune des Feuers&r, Elektronenröhre. Unten Messingrahmen, &6Lohenbrenner&r, Messingrahmen.",
              img("kronwerke:textures/item/brass_heart.png", 32, 32),
              "Die Feuerrune macht ein Botaniker am Runenaltar (Kapitel &aBotania: Runen&r). Tausch sie gegen Messingrahmen.",
              "",
              "&eKronwerke:&r Der Obelisk will &e8 Messingherzen&r, fest für jede Spielerzahl. Jedes zählt so viel wie 300 Messingbarren. Er nimmt sie nur, solange das Ziel von Stufe 2 aktiv ist.",
          ],
          tasks=[task_item("kronwerke:brass_heart", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["precision"], icon="kronwerke:brass_heart", size=1.75, shape="gear"),

    quest("brass_engine", A + 7, 25, "&6&lFütter den Obelisken mit Messing",
          subtitle="Das Ziel von Stufe 2: Die Messingmaschine.",
          description=[
              "Liefere &6256 Messingbarren&r und &632 Präzisionsgetriebe&r. Ein &eEinspeiser&r (Kiste oder Fass direkt am Obelisken) zieht alle zwei Sekunden ein, was er brauchen kann.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler will 2 000 Barren, 150 Getriebe und 8 Herzen. Dafür brauchst du mehrere überhitzte Mixer, Kupfer und Zink aus Mahlwerk und Wäsche, eine Röhrenlinie und mindestens eine Präzisionslinie.",
              "",
              "Die Magier brauchen deine Messingrahmen, du ihre Quelljuwelen und Feuerrunen. Bei 98 Prozent hält der Obelisk an, die letzte Ladung geht gemeinsam auf den Streams hinein.",
          ],
          tasks=[task_item("create:brass_ingot", 256), task_item("create:precision_mechanism", 32)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["precision_line", "brass_superheated", "brass_heart"], icon="create:precision_mechanism", size=2.5, shape="gear"),

    # ---- Dampf (column B) -----------------------------------------------------------
    quest("steam_engine", B, 2.75, "&6Bau eine Dampfmaschine",
          subtitle="Richtig viel Kraft aus Wasser und Hitze.",
          description=[
              "&6Goldblech&r, &6Andesitlegierung&r und &6Kupferblock&r untereinander ergeben die &6Dampfmaschine&r. Setz sie an einen Kessel aus mindestens &e4 Flüssigkeitstanks&r mit &bWasser&r und &6Lohenbrennern&r darunter.",
              "",
              "Klick sie mit einer &6Welle&r an, das ist ihr Ausgang. Eine voll versorgte Maschine trägt &d1 024 SU pro RPM&r, 32-mal so viel wie ein Wasserrad.",
          ],
          tasks=[task_item("create:steam_engine", 2), task_item("create:fluid_tank", 4)],
          rewards=[reward_item("minecraft:coal_block", 16), reward_table("s2_uncommon")],
          deps=["brass_casing"], icon="create:steam_engine", size=1.75, shape="gear"),

    quest("boiler", B + 2.5, 1.75, "&6Bau ein Kesselkraftwerk",
          subtitle="Jede Kesselstufe trägt eine Maschine mehr.",
          description=[
              "Stell &64 Dampfmaschinen&r an einen großen Kessel und &64 Lohenbrenner&r darunter. Die Ingenieursbrille zeigt die &eKesselstufe&r und was fehlt: Hitze, Wasser oder Größe.",
              "",
              "Jeder erhitzte Brenner zählt eine Stufe Hitze, ein überhitzter zwei. Der kleinste der drei Werte bestimmt die Stufe, und jede Stufe lässt eine Maschine mehr voll laufen.",
              "",
              "&cHäufiger Fehler:&r zu wenig Wasser. Eine langsame Pumpe reicht nur für kleine Stufen.",
          ],
          tasks=[task_item("create:steam_engine", 4), task_item("create:blaze_burner", 4)],
          rewards=[reward_table("s2_uncommon"), reward_xp(6)],
          deps=["steam_engine"]),

    quest("whistle", B + 2.5, 3.75, "&6Lass die Dampfpfeife tuten",
          subtitle="Fabriksirene oder Orgel.",
          description=[
              "&6Goldblech&r über &6Kupferbarren&r ergibt die &6Dampfpfeife&r. Setz sie auf einen beheizten Kessel und gib ihr ein Redstone-Signal.",
              "",
              "Weitere Pfeifen auf die gesetzte gesteckt machen den Ton tiefer, der Schraubenschlüssel wechselt zwischen 3 Oktaven.",
          ],
          tasks=[task_item("create:steam_whistle", 1)],
          rewards=[reward_xp(3)],
          deps=["steam_engine"], optional=True),

    quest("speed_controller", B + 5, 1.75, "&6Stell die Drehzahl genau ein",
          subtitle="Der Rotationsgeschwindigkeitsregler.",
          description=[
              "Ein &6Präzisionsgetriebe&r auf einem &6Messingrahmen&r ergibt den &6Rotationsgeschwindigkeitsregler&r. Er stellt ein großes Zahnrad über ihm per Wertefeld auf bis zu 256 RPM, in beide Richtungen.",
              "",
              "Mehr Drehzahl heißt mehr Verbrauch aus derselben Belastbarkeit.",
          ],
          tasks=[task_item("create:rotation_speed_controller", 1)],
          rewards=[reward_xp(4)],
          deps=["boiler"]),

    quest("sequenced_gearshift", B + 5, 3.75, "&6Programmier eine Drehung",
          subtitle="Die Sequenzielle Gangschaltung.",
          description=[
              "&6Messingrahmen&r, &6Zahnrad&r und &6Elektronenröhre&r ergeben die &6Sequenzielle Gangschaltung&r. Bei Redstone spielt sie bis zu fünf Befehle ab: drehen um einen Winkel, Kolben um Blöcke bewegen, warten, umkehren.",
              "",
              "Ein Aufzug fährt genau drei Stockwerke, ein Tor öffnet sich um 90 Grad.",
          ],
          tasks=[task_item("create:sequenced_gearshift", 1)],
          rewards=[reward_xp(3)],
          deps=["steam_engine"], optional=True),

    # ---- Kontraptionen (column B) -------------------------------------------------------
    quest("schematics", B, 9, "&6Bau mit der Bauplankanone",
          subtitle="Ganze Gebäude Block für Block.",
          description=[
              "&6Bauplantisch&r (Holzstufen, glatter Stein), &6Leere Baupläne&r (Papier, hellblauer Farbstoff), &6Bauplankanone&r (zwei Eisenblöcke, Stämme, glatter Stein, Werfer).",
              pic("create:schematic"),
              "Mit &6Bauplan und Feder&r speicherst du ein Gebäude, am Tisch lädst du Dateien aus deinem Ordner &eschematics&r hoch. Die Kanone baut es aus Kisten nach, ein Schwarzpulver reicht für 400 Blöcke.",
          ],
          tasks=[task_item("create:schematic_table", 1), task_item("create:schematicannon", 1)],
          rewards=[reward_item("minecraft:gunpowder", 32), reward_xp(5)],
          deps=["brass_casing"], icon="create:schematicannon", size=1.5),

    quest("contraption_controls", B + 2.5, 8, "&6Steuer eine Kontraption",
          subtitle="Werkzeuge an und aus, auch während der Fahrt.",
          description=[
              "&6Knopf&r, &6Andesitgehäuse&r und &6Elektronenröhre&r ergeben die &6Vorrichtungs-Steuerung&r. Auf einer Kontraption schaltet sie die Werkzeuge, mit Filter nur eine Sorte.",
              "",
              "Die &6Fernsteuerung&r (sechs Holzknöpfe um eine Redstone-Verbindung) funkt pro Taste auf eigener Frequenz.",
          ],
          tasks=[task_item("create:contraption_controls", 1), task_item("create:linked_controller", 1)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("elevator", B + 2.5, 10, "&6Bau einen Aufzug",
          subtitle="Die Aufzug-Seilrolle hält an Stockwerken.",
          description=[
              "&6Messingrahmen&r, &6getrockneter Seetangblock&r und &6Eisenblech&r ergeben die &6Aufzug-Seilrolle&r. Stockwerke markierst du mit &6Redstone-Kontakten&r am Schacht.",
              "",
              "Eine Vorrichtungs-Steuerung in der Kabine wird zur Stockwerkswahl. Die Rolle kostet &d4 SU pro RPM&r.",
          ],
          tasks=[task_item("create:elevator_pulley", 1)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("cart_assembler", B + 5, 8, "&6Setz eine Kontraption auf Schienen",
          subtitle="Der Lorenmonteur.",
          description=[
              "Zwei &6Andesitlegierungen&r, &6Redstone&r und zwei &6Stämme&r ergeben den &6Lorenmonteur&r. Fährt eine Lore mit Redstone-Signal darüber, nimmt sie die angeklebten Blöcke mit.",
              "",
              "Die &6Steuerungsschiene&r (Gold, Stock, Elektronenröhre, sechs Stück) regelt ihr Tempo per Signalstärke. Für kurze Wege im Bergwerk günstiger als ein Zug.",
          ],
          tasks=[task_item("create:cart_assembler", 1), task_item("create:controller_rail", 6)],
          rewards=[reward_item("minecraft:rail", 32), reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("roller", B + 5, 10, "&6Pflaster eine Trasse",
          subtitle="Die Mechanische Walze.",
          description=[
              "&6Elektronenröhre&r, &6Andesitgehäuse&r und &6Mahlwerkrad&r untereinander ergeben die &6Mechanische Walze&r. Vorn an einer Kontraption räumt sie den Weg und pflastert mit dem Block aus ihrem Filter.",
              "",
              "Sie füllt Löcher bis 12 Blöcke tief. Ein Zug mit zwei Walzen ebnet seine eigene Trasse.",
          ],
          tasks=[task_item("create:mechanical_roller", 2)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("potato_cannon", B + 7.5, 9, "&6Schieß mit Kartoffeln",
          subtitle="Das Werkzeug, das niemand braucht und jeder will.",
          description=[
              "Handwerkseinheiten-Rezept: &6Andesitlegierung&r, &6Präzisionsgetriebe&r, drei &6Flüssigkeitsrohre&r, zwei &6Kupferbarren&r. Die Luft kommt aus dem Kupfer-Rückentank.",
              pic("create:potato_cannon"),
              "Ebenfalls aus den Handwerkseinheiten: &6Extendo Griff&r für mehr Reichweite und &6Symmetriestab&r, der jeden gesetzten Block spiegelt.",
          ],
          tasks=[task_item("create:potato_cannon", 1)],
          rewards=[reward_item("minecraft:baked_potato", 32), reward_xp(3)],
          deps=["schematics"], optional=True),

    # ---- Addons (column B) ------------------------------------------------------------
    quest("addons", B, 14.5, "&dSchau dir die Create-Addons an",
          subtitle="Was es zu Create sonst noch gibt.",
          description=[
              "Hier: &6Enchantment Industry&r (Erfahrung als Flüssigkeit), &6Power Grid&r (Stromkreise mit Volt und Ampere), &6Crafts & Additions&r (FE aus Rotation) und die ersten Teile von &6Create Connected&r.",
              "",
              "Weichen, Kuppler, Dieselmotoren, Spawnflüssigkeiten und der Rest stehen in &6Create: Addons&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["brass_casing"], icon="create:brass_casing", size=1.5, shape="hexagon"),

    # Enchantment Industry
    quest("grindstone", B + 2.5, 14.5, "&5Schleif Erfahrung ab",
          subtitle="Enchantment Industry: der Mechanische Schleifstein.",
          description=[
              "Acht &6Andesitlegierungen&r um eine &6Welle&r ergeben den &6Mechanischen Schleifstein&r. Klick damit einen &6Abfluss&r an (wird zum Schleifsteinabfluss) und setz einen zweiten obendrauf.",
              "",
              "Erfahrungsklumpen werden zu &bFlüssiger Erfahrung&r, verzauberte Items verlieren ihre Verzauberung an den Abfluss. Nebenbei poliert er Rosenquarz.",
          ],
          tasks=[task_item("create_enchantment_industry:mechanical_grindstone", 2)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(5)],
          deps=["addons"]),

    quest("blaze_enchanter", B + 5, 14.5, "&5Lass eine Lohe verzaubern",
          subtitle="Der Lohen-Verzauberer.",
          description=[
              "Am &6Schmiedetisch&r: &6Lohenbrenner&r, &6Zaubertisch&r und die Schmiedevorlage für das Lohen-Upgrade. Die erste Vorlage liegt in Kisten von Netherfestungen und Bastionen.",
              "",
              "Er verzaubert mit &bFlüssiger Erfahrung&r statt Leveln, ohne Lapis, bis Stufe 30. Mehr dazu in &6Create: Addons&r.",
          ],
          tasks=[task_item("create_enchantment_industry:blaze_enchanter", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["grindstone"]),

    quest("printer", B + 7.5, 14.5, "&5Druck Bücher",
          subtitle="Kopien mit Flüssiger Erfahrung.",
          description=[
              "&6Messingblech&r, &6Ausguss&r und &6Eisenblock&r ergeben den &6Drucker&r. Er kopiert beschriebene Bücher, verzauberte Bücher und Bannermuster auf Rohlinge, die unter ihm durchlaufen.",
              "",
              "Verzauberte Bücher kosten viel Erfahrung, aber eine gute Verzauberung reicht dann für den ganzen Server.",
          ],
          tasks=[task_item("create_enchantment_industry:printer", 1)],
          rewards=[reward_item("minecraft:book", 16), reward_xp(3)],
          deps=["blaze_enchanter"], optional=True),

    # Create: Power Grid, row 1 left to right
    quest("pg_wire", B + 2.5, 18, "&3Schneid Kupferdraht",
          subtitle="Power Grid: Strom im geschlossenen Kreis.",
          description=[
              "Ein &6Kupferblech&r durch die &6Mechanische Säge&r ergibt vier &6Kupferdraht&r. Klick mit Draht eine Klemme an, dann die nächste.",
              "",
              "Power Grid rechnet mit &dVolt&r, &dAmpere&r und &dOhm&r. Strom fließt nur im &egeschlossenen Kreis&r: jedes Gerät hat Plus und Minus, und es braucht Hin- und Rückweg.",
              "",
              "Lange Drähte haben mehr Widerstand, die verlorene Leistung wird Wärme, zu viel davon lässt den Draht durchglühen. Ein &6Verbinder&r (drei Kupferklumpen, Legierung) ist ein Pfosten zum Aufhängen.",
          ],
          tasks=[task_item("powergrid:wire", 16), task_item("powergrid:wire_connector", 4)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(3)],
          deps=["addons"], icon="powergrid:wire"),

    quest("pg_coil", B + 5, 18, "&3Wickel eine Kupferspule",
          subtitle="Steckt in Generator, Motor und Magnet.",
          description=[
              "Vier &6Kupferdraht&r, zwei &6Karton&r und ein &6Stock&r ergeben eine &6Kupferspule&r.",
              img("powergrid:textures/item/copper_coil.png", 32, 32),
              "Du brauchst viele: der Rotor will vier, der Elektromagnet fünf, der Motor sechs.",
          ],
          tasks=[task_item("powergrid:copper_coil", 8)],
          rewards=[reward_item("create:cardboard", 16), reward_xp(3)],
          deps=["pg_wire"], icon="powergrid:copper_coil"),

    quest("pg_casing", B + 7.5, 18, "&3Mach ein Leitfähiges Gehäuse",
          subtitle="Zink auf Andesitgehäuse.",
          description=[
              "Rechtsklicke ein &6Andesitgehäuse&r mit einem &6Zinkbarren&r, oder lass es ein Einsatzgerät tun. Es wird zum &6Leitfähigen Gehäuse&r.",
              "",
              "Es steckt in Adapter, Elektromagnet, Motor, Messgeräten und Generatorgehäuse.",
          ],
          tasks=[task_item("powergrid:conductive_casing", 4)],
          rewards=[reward_item("create:zinc_ingot", 8), reward_xp(4)],
          deps=["pg_coil"], icon="powergrid:conductive_casing"),

    quest("pg_adapter", B + 10, 18, "&3Setz einen Adapter",
          subtitle="Klemmen für Geräte ohne Klemmen.",
          description=[
              "Ein &6Zinkblech&r über zwei &6Kupferblechen&r und einer &6Andesitlegierung&r ergibt den &6Adapter&r. Das Zinkblech presst die Presse aus einem Zinkbarren.",
              "",
              "Er gibt Geräten ohne eigene Klemmen einen Anschluss und speist auch FE-Maschinen, etwa die von Mekanism, aus deinem Netz.",
          ],
          tasks=[task_item("powergrid:device_connector", 2)],
          rewards=[reward_item("create:copper_sheet", 8), reward_xp(4)],
          deps=["pg_casing"], icon="powergrid:device_connector"),

    # Power Grid, row 2 right to left
    quest("pg_clutch", B + 10, 19.75, "&3Kuppel den Generator an",
          subtitle="Die Generator-Kupplung, 32 SU pro RPM.",
          description=[
              "Eine Create-&6Kupplung&r und eine &6Andesitlegierung&r ergeben die &6Generator-Kupplung&r. Sie ist die Basis jedes Generators und sitzt an deiner Antriebswelle.",
              "",
              "Sie koppelt Netz und Generatorwelle nur schwach, ein Redstone-Signal ändert die Stärke. Sie kostet &d32 SU pro RPM&r.",
          ],
          tasks=[task_item("powergrid:generator_clutch", 1)],
          rewards=[reward_item("create:andesite_alloy", 16), reward_xp(4)],
          deps=["pg_adapter"], icon="powergrid:generator_clutch"),

    quest("pg_rotor", B + 7.5, 19.75, "&3Bau einen Induktionsrotor",
          subtitle="Die drehende Masse, 32 SU pro RPM.",
          description=[
              "Handwerkseinheiten-Rezept: vier &6Andesitlegierungen&r, vier &6Kupferspulen&r, eine &6Welle&r ergeben den &6Generator-Induktionsrotor&r. Setz ihn hinter die Kupplung.",
              "",
              "Rotoren erzeugen Strom, wenn sie sich im Magnetfeld drehen. Bis zu &e8&r Rotorteile pro Generator, jeder kostet &d32 SU pro RPM&r.",
          ],
          tasks=[task_item("powergrid:generator_induction_rotor", 1)],
          rewards=[reward_item("powergrid:copper_coil", 4), reward_xp(5)],
          deps=["pg_clutch"], icon="powergrid:generator_induction_rotor"),

    quest("pg_winding", B + 5, 19.75, "&3Leg Wicklungen um den Rotor",
          subtitle="Der Ständer erzeugt das Magnetfeld.",
          description=[
              "Leg &6Wellen&r neben den Rotor und klick zwei davon mit einer &6Kupferspule&r an: daraus wird eine &6Wicklung&r. Nebeneinander liegende Wicklungen schalten sich in Reihe.",
              "",
              "Ein &6Generatorgehäuse&r (Eisenbleche, Kupferblech, Leitfähiges Gehäuse) verbindet Wicklungen um die Ecke.",
          ],
          tasks=[task_checkmark("Wicklungen gelegt"), task_item("powergrid:generator_housing", 2)],
          rewards=[reward_item("powergrid:copper_coil", 4), reward_xp(5)],
          deps=["pg_rotor"], icon="powergrid:generator_housing"),

    quest("pg_generator", B + 2.5, 19.75, "&3&lSchließ den Kollektor an",
          subtitle="Der Generator liefert Spannung.",
          description=[
              "Handwerkseinheiten-Rezept: &6Pins&r (zwei Kupferklumpen), zwei &6Kohle&r, &6Kupferblech&r, zwei &6Andesitlegierungen&r, &6Welle&r und &6Andesitgehäuse&r ergeben den &6Generator-Kollektor&r. Er kommt ans Ende des Rotors, 8 SU pro RPM.",
              "",
              "An seine Klemmen kommt die Last. Damit Strom entsteht, braucht der Ständer einen &dErregerstrom&r, etwa über einen Adapter aus einer anderen Quelle.",
              "",
              "Die Ponder-Szenen (&eW&r) zeigen den Aufbau. Hände weg vom drehenden Rotor.",
          ],
          tasks=[task_item("powergrid:generator_commutator", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["pg_winding"], icon="powergrid:generator_commutator", size=1.5, shape="gear"),

    # Power Grid, row 3 left to right
    quest("pg_rheostat", B + 2.5, 21.5, "&3Lass den Generator sich selbst erregen",
          subtitle="Ohne fremde Stromquelle, mit Rheostat.",
          description=[
              "&6Rheostat&r: Kohle, Welle, fünf &6Widerstandsspulen&r (vier Eisendraht und ein Stock) und ein Leitfähiges Gehäuse. Verdrahte Kollektor und Wicklungen Plus an Plus, Minus an Minus, mit dem Rheostat dazwischen.",
              "",
              "Das klappt nur in einer Drehrichtung, mit passendem Widerstand und bei genug Drehzahl. Der Rheostat stellt den Widerstand per Rotation ein.",
          ],
          tasks=[task_item("powergrid:rheostat", 1)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(5)],
          deps=["pg_generator"], icon="powergrid:rheostat"),

    quest("pg_magnet", B + 5, 21.5, "&3Magnetisier Andesitlegierung",
          subtitle="Der Elektromagnet macht Magnete.",
          description=[
              "&6Leitfähiges Gehäuse&r, fünf &6Kupferspulen&r und ein &6Eisenblech&r ergeben den &6Elektromagneten&r. Mit Strom magnetisiert er &6Andesitlegierung&r auf einem Depot oder Band darunter.",
              img("powergrid:textures/item/magnet.png", 32, 32),
              "Deshalb kommt der Motor erst nach dem Generator.",
          ],
          tasks=[task_item("powergrid:electromagnet", 1), task_item("powergrid:magnet", 2)],
          rewards=[reward_item("create:andesite_alloy", 16), reward_xp(5)],
          deps=["pg_rheostat"], icon="powergrid:magnet"),

    quest("pg_motor", B + 7.5, 21.5, "&3Treib eine Welle mit Strom an",
          subtitle="Der Elektromotor, 64 SU pro RPM.",
          description=[
              "Handwerkseinheiten-Rezept: vier &6Eisenbleche&r, sechs &6Kupferspulen&r, zwei &6Magnete&r, eine &6Welle&r und ein &6Leitfähiges Gehäuse&r ergeben den &6Elektromotor&r.",
              "",
              "Seine Drehzahl hängt von der Spannung ab, er trägt &d64 SU pro RPM&r. So treibt ein Kraftwerk am Fluss über Drähte eine Fabrik am anderen Ende der Basis an.",
              "",
              "Mit einem &6Präzisionsgetriebe&r wird er zum &6Konstanten Geschwindigkeitsmotor&r: feste Drehzahl, die Spannung bestimmt Last und Richtung.",
          ],
          tasks=[task_item("powergrid:electric_motor", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(6)],
          deps=["pg_magnet"], icon="powergrid:electric_motor"),

    quest("pg_measure", B + 10, 21.5, "&3Miss Spannung und Strom",
          subtitle="Wer misst, versteht sein Netz.",
          description=[
              "&6Kompass&r, &6Kupferspule&r und &6Leitfähiges Gehäuse&r ergeben den &6Spannungsmesser&r. Allein ins Raster gelegt wird er zum &6Strommesser&r, beide zusammen zum &6Wattmeter&r.",
              "",
              "Der Strommesser sitzt in Reihe im Kreis. So siehst du, ob der Generator unter Last einbricht oder ein Draht zu viel trägt.",
          ],
          tasks=[task_item("powergrid:voltage_gauge", 1), task_item("powergrid:current_gauge", 1)],
          rewards=[reward_xp(5)],
          deps=["pg_motor"], icon="powergrid:voltage_gauge", optional=True),

    # Create Crafts & Additions
    quest("rolling_mill", B + 2.5, 24.5, "&6Walz Draht und Ruten",
          subtitle="Crafts & Additions: das Walzwerk.",
          description=[
              "Eisenbleche, Wellen, Legierung und Andesitgehäuse ergeben das &6Walzwerk&r (8 SU pro RPM). Ein Kupferbarren wird zu zwei &6Kupferruten&r, ein Kupferblech zu zwei &6Kupferkabeln&r.",
              "",
              "Vier Kupferkabel um eine &6leere Spule&r (Eisenbleche und Eisenrute, 24 Stück) ergeben eine &6Kupferspule&r.",
          ],
          tasks=[task_item("createaddition:rolling_mill", 1), task_item("createaddition:copper_spool", 2)],
          rewards=[reward_item("minecraft:copper_ingot", 32), reward_xp(3)],
          deps=["addons"]),

    quest("alternator", B + 5, 24.5, "&6Mach FE aus Rotation",
          subtitle="Der Alternator.",
          description=[
              "Handwerkseinheiten-Rezept: vier &6Kupferspulen&r, Eisenbleche, eine &6Eisenrute&r und zwei &6Andesitlegierungen&r ergeben den &6Alternator&r.",
              "",
              "Bei 256 RPM liefert er &d360 FE pro Tick&r und zieht dabei &d16 384 SU&r. Ein Kessel mit Alternator ist ein solides erstes Kraftwerk für Mekanism.",
              "",
              "&6Netzanschlüsse&r (Kupferrute, Legierung, Schleimball) verbindest du mit einer Kupferspule. Den Akku dieses Addons gibt es erst in Stufe 3, puffern kannst du vorher mit einem Energiewürfel von Mekanism.",
          ],
          tasks=[task_item("createaddition:alternator", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["rolling_mill"], icon="createaddition:alternator"),

    quest("electric_motor", B + 7.5, 24.5, "&6Mach Rotation aus FE",
          subtitle="Der Elektromotor von Crafts & Additions.",
          description=[
              "Handwerkseinheiten-Rezept mit &6Messingblechen&r, &6Kupferspulen&r, &6Eisenrute&r, Legierung und einem &6Kondensator&r (Zink- und Kupferblech mit Redstonefackel).",
              "",
              "Er dreht einstellbar bis 256 RPM, trägt bis zu 16 384 SU und braucht bei voller Drehzahl &d480 FE pro Tick&r. So läuft ein Mixer auch ohne Bach.",
          ],
          tasks=[task_item("createaddition:electric_motor", 1)],
          rewards=[reward_xp(5)],
          deps=["alternator"]),

    quest("tesla_coil", B + 10, 24.5, "&6Lad Items mit der Teslaspule",
          subtitle="Strom für Items auf dem Band.",
          description=[
              "Handwerkseinheiten-Rezept mit Kupferspulen, Kondensatoren, Messingrahmen, Messingblechen und einer Elektronenröhre. Sie lädt Items auf Depot oder Band darunter mit FE.",
              "",
              "Aus einem &6Goldbarren&r wird mit 36 000 FE ein &6Electrumbarren&r. Ein Lohenbrenner mit &6Strohhalm&r (Papier oder Bambus im Walzwerk) verbrennt flüssige Brennstoffe.",
          ],
          tasks=[task_item("createaddition:tesla_coil", 1)],
          rewards=[reward_xp(3)],
          deps=["electric_motor"], optional=True),

    # Create Connected and more
    quest("fan_catalyst", B + 2.5, 27, "&6Wasch ohne Wasserblock",
          subtitle="Create Connected: Lüfter-Katalysatoren.",
          description=[
              "Ein &6Leerer Lüfter Katalysator&r (Messingbarren und Eisengitter) kommt vor den Lüfter. Rechtsklick mit Wassereimer, Lavaeimer oder Seelensand macht ihn waschend, schmelzend oder spukend.",
              "",
              "Kein Wasser, das wegläuft, keine Lava, die etwas anzündet. Weitere Katalysatoren stehen in &6Create: Addons&r.",
          ],
          tasks=[task_item("create_connected:empty_fan_catalyst", 1)],
          rewards=[reward_xp(3)],
          deps=["addons"]),

    quest("connected_parts", B + 5, 27, "&6Bau ein Kurbelrad",
          subtitle="Create Connected: Kleinteile.",
          description=[
              "Eine &6Handkurbel&r und ein &6Zahnrad&r ergeben das &6Kurbelrad&r, eine Kurbel, die mit Zahnrädern daneben kämmt.",
              "",
              "Dazu gibt es &6Bremse&r, &6Zentrifugal Kupplung&r, &6Kinetische Batterie&r, &6Item Silo&r und &6Flüssigkeitsgefäß&r. JEI zeigt alle Rezepte.",
          ],
          tasks=[task_item("create_connected:crank_wheel", 1)],
          rewards=[reward_xp(3)],
          deps=["fan_catalyst"], optional=True),

    quest("spawner", B + 7.5, 27, "&6Bau den Mechanical Spawner",
          subtitle="Mobs aus Flüssigkeit.",
          description=[
              "Handwerkseinheiten-Rezept: Messingbarren, Messingbleche, Eisengitter, ein &6Smaragd&r und eine Welle. Pump &bSpawnflüssigkeit&r hinein und gib ihm Rotation.",
              "",
              "Wie die Flüssigkeiten gemischt werden, steht in &6Create: Addons&r.",
          ],
          tasks=[task_item("create_mechanical_spawner:mechanical_spawner", 1)],
          rewards=[reward_xp(5)],
          deps=["fan_catalyst"], optional=True),
]

images = [
    head("title", "Create: Messing", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 2: Messingwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("brass", "Messing", A - 0.6, 0.1),
    head("precision", "Präzision", A - 0.6, 6.4),
    head("logistics", "Messing-Logistik", A - 0.6, 16.4),
    head("goal", "Das Ziel", A + 1.8, 22.6),
    head("steam", "Dampf", B - 0.6, 0.1),
    head("contraptions", "Kontraptionen", B - 0.6, 6.4),
    head("addons", "Addons", B - 0.6, 12.2),
    head("note_cei", "Enchantment Industry", B + 1.9, 13.4, height=0.5, kind="note", colour="magic"),
    head("note_pg", "Power Grid", B + 1.9, 16.9, height=0.5, kind="note", colour="water"),
    head("note_cca", "Crafts & Additions", B + 1.9, 23.4, height=0.5, kind="note", colour="fire"),
    head("note_cc", "Connected und mehr", B + 1.9, 25.9, height=0.5, kind="note", colour="stone"),
]
images[0]["x"] = 15
images[1]["x"] = 15

chapter(C, "Create: Messing", "create:brass_casing", "tech", quests, shape="gear", order=9, stage=2,
        subtitle=["Stufe 2: Lohenbrenner, Messing, Präzisionsgetriebe, das Messingherz und die Create-Addons."], images=images)
