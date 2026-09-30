"""Create in stage 2 (Messingwerk): the blaze burner with its Source Gem recipe, brass, electron
tubes, deployers, mechanical crafters, precision mechanisms, steam, brass logistics, the brass
contraptions and the Create addons of the pack (Enchantment Industry, New Age, Crafts &
Additions, Connected, Mechanical Spawner). Trains are in create_trains.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create_brass"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


# Column A starts at x 0, column B at x 16.5.
A, B = 0, 16.5

quests = [
    # ---- Messing ----------------------------------------------------------------
    quest("welcome", A, 3, "&6&lDas Messingwerk",
          subtitle="Stufe 2 ist offen. Jetzt wird Create richtig schlau.",
          description=[
              "Mit dem Event am Obelisken hat sich &6Stufe 2, das Messingwerk&r, geöffnet: der Nether ist frei, und Create bekommt seine zweite Hälfte. Alles mit einem Messingrahmen kann mehr als die Andesit-Maschinen: filtern, zählen, sortieren, bauen und Rezepte in jeder Größe herstellen.",
              "",
              "Dieses Kapitel führt dich vom ersten Lohenbrenner über Messing, Elektronenröhren und Einsatzgeräte bis zum &6Präzisionsgetriebe&r. Dazu kommen Dampfkraft, die Messing-Logistik, neue Kontraptionen und die Create-Addons des Servers. Züge haben ihr eigenes Kapitel, &6Create: Züge&r.",
              "",
              "&eDas Ziel dieser Stufe:&r Der Obelisk will im Technik-Pfeiler &64 000 Messingbarren&r und &6300 Präzisionsgetriebe&r, gerechnet für 30 aktive Spieler. Wie du am besten einzahlst, steht ganz unten im Abschnitt &6Das Ziel&r. Den Stand zeigt dir &e/kw goals&r.",
              "",
              "Das Starterpaket dieser Stufe mit ein paar Messingbarren und einem Lohenbrenner hilft über die ersten Schritte. Auf Dauer brauchst du aber deine eigene Messinglinie.",
          ],
          tasks=[task_item("create:brass_ingot", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          icon="create:brass_ingot", size=2.0, shape="hexagon"),

    quest("zinc", A + 2.5, 1.5, "&6Zink in Mengen",
          subtitle="Die eine Hälfte jedes Messingbarrens.",
          description=[
              "Messing ist halb Kupfer, halb Zink, und das Obelisk-Ziel will tausende Barren. Zeit, Zink ernsthaft abzubauen: &6Zinkerz&r steckt in der Oberwelt im Stein, &6Tiefenschiefer-Zinkerz&r weiter unten. Die Mining Dimension ist dafür ideal, dort durchlöcherst du nicht die Landschaft rund um die Basen.",
              img(item_texture("create:zinc_ingot"), 32, 32),
              "Sobald du &6Mahlwerkräder&r hast (Abschnitt Präzision), zerkleinerst du &6Rohzink&r mit Bonus-Chance zu &6Zerkleinertem Rohzink&r. Gewaschen gibt das Zinkklumpen, geschmolzen Barren. So holst du aus jedem Erz deutlich mehr heraus als im Ofen.",
          ],
          tasks=[task_item("create:zinc_ingot", 64)],
          rewards=[reward_item("create:raw_zinc", 32), reward_xp(3)],
          deps=["welcome"]),

    quest("source_gems", A + 2.5, 3.25, "&dZwei Quelljuwelen",
          subtitle="Ohne Magie kein Messing.",
          description=[
              "Auf Kronwerke hängen Technik und Magie zusammen. Der &6Lohenbrenner&r ist das einzige, was einen Mixer heiß genug für Messing macht, und das Rezept seines leeren Gehäuses wurde geändert: es braucht jetzt zusätzlich &dzwei Quelljuwelen&r aus Ars Nouveau.",
              img(item_texture("ars_nouveau:source_gem"), 32, 32),
              "Quelljuwelen entstehen in der &aImbuement-Kammer&r von Ars Nouveau: ein Amethystsplitter oder Lapislazuli hinein, &dQuelle&r aus einem Quellglas in der Nähe, und nach einer Weile liegt ein Juwel darin. Wie das geht, steht im Kapitel &6Ars Nouveau&r.",
              "",
              "Du bist kein Magier? Frag einen! Zwei Juwelen pro Lohenbrenner sind ein fairer Tausch gegen ein paar Messingbarren. Genau so ist Kronwerke gedacht: kein Pfeiler des Obelisk-Ziels füllt sich allein.",
          ],
          tasks=[task_item("ars_nouveau:source_gem", 2)],
          rewards=[reward_item("minecraft:amethyst_shard", 8), reward_xp(3)],
          deps=["welcome"]),

    quest("nether", A + 2.5, 5, "&cAb in den Nether",
          subtitle="Netherrack, Lohen und Quarz.",
          description=[
              "Seit dem Event ist der Nether offen. Für Create holst du dort drei Dinge: &6Netherrack&r für das Lohenbrenner-Gehäuse, eine lebende &6Lohe&r zum Einfangen und &6Netherquarz&r für Rosenquarz und Elektronenröhren.",
              "",
              "Lohen findest du in &cNetherfestungen&r, meist rund um ihre Spawner. Nimm Feuerresistenz mit und halte Abstand: Lohen schießen Feuerbälle.",
              "",
              "Alles Weitere zum Nether steht im Kapitel &6Der Nether&r.",
          ],
          tasks=[task_item("minecraft:netherrack", 16), task_item("minecraft:quartz", 8)],
          rewards=[reward_table("s2_common"), reward_xp(3)],
          deps=["welcome"], icon="minecraft:netherrack"),

    quest("empty_burner", A + 5, 4.1, "&6Leerer Lohenbrenner",
          subtitle="Ein Käfig für eine Lohe, mit Magie verschlossen.",
          description=[
              "Das geänderte Rezept für den &6Leeren Lohenbrenner&r:",
              "Oben: &dQuelljuwel&r, &6Eisenblech&r, &dQuelljuwel&r",
              "Mitte: &6Eisenblech&r, &6Netherrack&r, &6Eisenblech&r",
              "Unten: leer, &6Eisenblech&r, leer",
              "",
              "Also vier Eisenbleche, ein Netherrack und zwei Quelljuwelen. JEI zeigt dir das geänderte Rezept, nicht mehr das alte aus Create.",
              "",
              "Ein leerer Lohenbrenner heizt noch nichts. Im nächsten Schritt kommt die Lohe hinein.",
          ],
          tasks=[task_item("create:empty_blaze_burner", 1)],
          rewards=[reward_item("create:iron_sheet", 8), reward_xp(3)],
          deps=["source_gems", "nether"], icon="create:empty_blaze_burner", size=1.5),

    quest("blaze_burner", A + 7.5, 4.1, "&6Lohenbrenner",
          subtitle="Eine Lohe, die für dich heizt.",
          description=[
              "Geh mit dem leeren Lohenbrenner in der Hand zu einer &6Lohe&r und rechtsklicke sie: sie wird eingefangen, und du hältst einen &6Lohenbrenner&r. Das klappt auch direkt an einem Lohen-Spawner in einer Netherfestung.",
              "",
              "Stell den Brenner unter ein &6Becken&r. Ohne Futter glimmt er nur. Mit Brennstoff, den auch ein Ofen nimmt (Kohle, Holzkohle, Holz), wird er &cerhitzt&r und liefert Hitze für alle Rezepte mit dem Hinweis Erhitzt in JEI. Mit einem &6Lohenkuchen&r ist er für eine Weile &cüberhitzt&r.",
              "",
              "Eine Schleuse oder ein Mechanischer Arm füttert ihn automatisch. Lohenbrenner heizen außerdem Dampfkessel, und mit Enchantment Industry werden sie sogar zu Verzauberern.",
          ],
          tasks=[task_item("create:blaze_burner", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_table("s2_common")],
          deps=["empty_burner"], icon="create:blaze_burner", size=2.0, shape="hexagon"),

    quest("brass_mixing", A + 10, 2.75, "&6Messing mischen",
          subtitle="Kupfer und Zink, heiß gerührt.",
          description=[
              "Von unten nach oben: &6Lohenbrenner&r, darauf das &6Becken&r, ein Block Luft, darüber der &6Mechanische Mixer&r. Ein &6Kupferbarren&r und ein &6Zinkbarren&r im erhitzten Becken ergeben &6zwei Messingbarren&r.",
              img(item_texture("create:brass_ingot"), 32, 32),
              "Für den Dauerbetrieb: Kupfer und Zink kommen über Schleusen oder ein Band ins Becken, eine Schleuse an der Beckenseite holt das Messing heraus, und eine weitere hält den Brenner mit Kohle bei Laune. Ein gut versorgter Mixer schafft ein paar hundert Barren in der Stunde.",
              "",
              "&cBleibt der Mixer stehen?&r Schau mit der Ingenieursbrille auf den Brenner: glimmt er nur, fehlt Brennstoff. Und jeder Mixer braucht sein eigenes Becken und seinen eigenen Brenner.",
          ],
          tasks=[task_item("create:brass_ingot", 64)],
          rewards=[reward_item("minecraft:copper_ingot", 32), reward_item("create:zinc_ingot", 32), reward_xp(5)],
          deps=["blaze_burner", "zinc"], icon="create:brass_ingot", size=2.0, shape="gear"),

    quest("blaze_cake", A + 10, 5.5, "&6Lohenkuchen",
          subtitle="Superheiß, für kurze Zeit.",
          description=[
              "&6Netherrack&r zwischen Mahlwerkrädern ergibt &6Aschenmehl&r. Eine Presse über einem Becken verdichtet Aschenmehl, Zucker und ein Ei zur &6Lohenkuchenbasis&r, und ein Ausguss füllt 250 mB &bLava&r hinein: fertig ist der &6Lohenkuchen&r.",
              img(item_texture("create:blaze_cake"), 32, 32),
              "Gib ihn dem Lohenbrenner, und er ist eine Weile &cüberhitzt&r. Das brauchen einige Rezepte in JEI, zum Beispiel Lava aus Bruchstein im Mixer. Ein Mechanischer Arm kann Kuchen automatisch nachlegen.",
          ],
          tasks=[task_item("create:blaze_cake", 4)],
          rewards=[reward_item("minecraft:egg", 16), reward_item("minecraft:sugar", 16)],
          deps=["blaze_burner"], optional=True),

    quest("brass_casing", A + 12.5, 2.75, "&6Messingrahmen",
          subtitle="Das Gerüst jeder schlauen Maschine.",
          description=[
              "Wie gehabt: rechtsklicke einen gesetzten, entrindeten Stamm mit einem &6Messingbarren&r. Der &6Messingrahmen&r steckt in Mechanischen Handwerkseinheiten, im Mechanischen Arm, Drehzahlregler, Anzeige-Link und vielem mehr.",
              "",
              "&dBotania&r-Spieler werden dich danach fragen: auf Kronwerke braucht die &aTerrestrische Agglomerationsplatte&r zwei Messingrahmen statt zwei Lapisblöcken. Ohne sie gibt es kein Terrastahl, und Terrastahl ist die Magie-Hälfte dieses Obelisk-Ziels. Gib ein paar Rahmen ab, der Server braucht beide Pfeiler.",
          ],
          tasks=[task_item("create:brass_casing", 16)],
          rewards=[reward_item("minecraft:stripped_oak_log", 16), reward_xp(3)],
          deps=["brass_mixing"]),

    # ---- Präzision ----------------------------------------------------------------
    quest("rose_quartz", A, 10.5, "&6Rosenquarz",
          subtitle="Quarz, rot gefärbt, glatt poliert.",
          description=[
              "Ein &6Netherquarz&r und acht &6Redstone&r im Handwerksraster ergeben &6Rosenquarz&r. Poliert wird er mit &6Schmirgelpapier&r (Papier und Sand): Schmirgelpapier in die Haupthand, Rosenquarz in die Nebenhand, und die rechte Maustaste gedrückt halten. Am Fließband erledigt das ein Einsatzgerät mit Schmirgelpapier.",
              img(item_texture("create:polished_rose_quartz"), 32, 32),
              "Polierter Rosenquarz ist die Hälfte jeder Elektronenröhre. Wer den Mechanischen Schleifstein aus Enchantment Industry hat, poliert damit ganz ohne Papierverbrauch.",
          ],
          tasks=[task_item("create:polished_rose_quartz", 8)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(3)],
          deps=["nether"]),

    quest("electron_tube", A + 2.5, 10.5, "&6Elektronenröhre",
          subtitle="Die Logik in jeder Messingmaschine.",
          description=[
              "Polierter Rosenquarz auf einem &6Eisenblech&r ergibt eine &6Elektronenröhre&r. Sie steckt in Einsatzgeräten, Handwerkseinheiten, Messingschleusen und -tunneln, Zugsignalen, Anzeigetafeln und vielen Addon-Maschinen.",
              img(item_texture("create:electron_tube"), 32, 32),
              "Du wirst sehr viele brauchen. Richte früh eine kleine Linie ein: Rosenquarz aufs Band, ein Einsatzgerät mit Schmirgelpapier poliert ihn, und eine Handwerkseinheit setzt die Röhre zusammen.",
          ],
          tasks=[task_item("create:electron_tube", 16)],
          rewards=[reward_item("create:iron_sheet", 16), reward_xp(3)],
          deps=["rose_quartz"]),

    quest("brass_hand", A + 5, 9.25, "&6Messing Hand",
          subtitle="Finger aus Blech.",
          description=[
              "Presse Messingbarren zu &6Messingblechen&r. Vier Bleche und eine Andesitlegierung ergeben eine &6Messing Hand&r, das Herzstück des Einsatzgeräts.",
              img(item_texture("create:brass_hand"), 32, 32),
              "Messingbleche brauchst du auch für den Mechanischen Arm, den Schlauen Schacht und etliche Addons. Eine eigene Presse nur für Messing lohnt sich.",
          ],
          tasks=[task_item("create:brass_hand", 2)],
          rewards=[reward_item("create:brass_sheet", 4), reward_xp(2)],
          deps=["brass_mixing"]),

    quest("deployer", A + 7.5, 11, "&6Einsatzgerät",
          subtitle="Eine Hand, die benutzt, was sie hält.",
          description=[
              "Elektronenröhre, Andesitgehäuse und Messing Hand ergeben das &6Einsatzgerät&r. Es tut mit dem Item in seiner Hand, was ein Spieler tun würde: Blöcke setzen, Items benutzen, zuschlagen, Kühe melken. Das Item gibst du ihm per Rechtsklick oder per Schleuse.",
              "",
              "Über einem Depot oder Band wendet es sein Item auf alles an, was darunter liegt: Legierung auf Stämme für Andesitgehäuse, Schmirgelpapier auf Rosenquarz, Bretter auf Wellen für Zahnräder. JEI listet alle Rezepte unter &eEinsetzen&r.",
              "",
              "Mit dem Schraubenschlüssel schaltest du zwischen &eBenutzen&r und &eSchlagen&r um, im Filterfeld legst du fest, was es annimmt. Es kostet 4 SU pro RPM.",
              "",
              "Das Einsatzgerät ist das Herz der &esequenziellen Montage&r und damit dein Weg zum Präzisionsgetriebe.",
          ],
          tasks=[task_item("create:deployer", 2)],
          rewards=[reward_item("create:andesite_alloy", 32), reward_table("s2_common")],
          deps=["electron_tube", "brass_hand"], icon="create:deployer", size=1.75, shape="gear"),

    quest("crafter", A + 2.5, 12.75, "&6Mechanische Handwerkseinheit",
          subtitle="Rezepte, größer als die Werkbank.",
          description=[
              "Elektronenröhre, &6Messingrahmen&r und Werkbank ergeben drei &6Mechanische Handwerkseinheiten&r. Stell sie als Raster auf, eine pro Rezeptfeld, und verbinde sie mit dem Schraubenschlüssel: die Pfeile auf ihnen müssen alle zu einer Ausgabe-Einheit führen.",
              "",
              "Leg die Zutaten hinein, von Hand oder per Schleuse, und gib dem Raster Rotation. Sind alle Felder belegt, legen sie los. Felder, die leer bleiben sollen, deckst du mit einer &6Handwerkseinheit Slot Abdeckung&r (drei Messingklumpen) ab; ein Redstone-Impuls startet ein Rezept auch unvollständig.",
              "",
              "Manche Rezepte gibt es nur hier, bis 9 x 9 Felder groß: &6Mahlwerkräder&r, die Kartoffelkanone, der Mechanical Spawner und die Maschinen aus Crafts & Additions. Handwerkseinheiten kosten 2 SU pro RPM.",
          ],
          tasks=[task_item("create:mechanical_crafter", 9)],
          rewards=[reward_item("create:electron_tube", 4), reward_xp(3)],
          deps=["electron_tube"]),

    quest("crushing_wheel", A + 5, 13.25, "&6Mahlwerkräder",
          subtitle="Mehr aus jedem Erz.",
          description=[
              "Das &6Mahlwerkrad&r ist dein erstes großes Rezept für die Handwerkseinheiten: 5 x 5 Felder aus Andesitlegierung, Brettern und Stein, zwei Räder auf einmal. Stell zwei Räder mit einem Block Abstand nebeneinander und treib sie so an, dass sie sich &eaufeinander zu&r drehen.",
              "",
              "Was oben zwischen die Räder fällt, wird zermahlen. Aus &6Roherz&r wird &6Zerkleinertes Erz&r mit einer Chance auf ein zweites und einen &6Erfahrungsklumpen&r. Netherrack wird zu Aschenmehl, Obsidian zu Pulverisiertem Obsidian für die Züge.",
              "",
              "&cVorsicht:&r Mahlwerkräder verletzen alles, was hineinfällt, auch dich. Jedes Rad kostet 8 SU pro RPM, zwei Räder bei 64 RPM also 1 024 SU. Ein Fall für die Dampfmaschine.",
          ],
          tasks=[task_item("create:crushing_wheel", 2)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_xp(3)],
          deps=["crafter"]),

    quest("ore_processing", A + 7.5, 13.5, "&6Erzverarbeitung",
          subtitle="Zerkleinern, waschen, schmelzen.",
          description=[
              "&6Zerkleinertes Erz&r schmilzt im Ofen oder vor einem Lüfter mit Lava zu Barren. Noch besser: wasch es mit einem Lüfter durch Wasser. Aus einem Zerkleinerten Roheisen werden neun Eisenklumpen und mit Glück Redstone dazu; andere Erze haben ihre eigenen Beigaben, JEI zeigt sie unter &eWaschen&r.",
              img(item_texture("create:crushed_raw_iron"), 32, 32),
              "Unterm Strich holst du so aus einem Erz im Schnitt deutlich mehr als einen Barren. Mekanism kann später noch mehr, aber für Zink und Kupfer, die Zutaten für Messing, ist die Create-Linie unschlagbar einfach.",
          ],
          tasks=[task_item("create:crushed_raw_zinc", 32)],
          rewards=[reward_table("s2_common"), reward_xp(3)],
          deps=["crushing_wheel"]),

    quest("precision", A + 10, 11, "&6Präzisionsgetriebe",
          subtitle="Deine erste sequenzielle Montage.",
          description=[
              "Das &6Präzisionsgetriebe&r entsteht durch &esequenzielle Montage&r: ein Item durchläuft mehrere Arbeitsschritte in fester Reihenfolge, immer wieder, bis es fertig ist.",
              "",
              "Der Ablauf: ein &6Goldblech&r kommt aufs Band. Das erste Einsatzgerät setzt ein &6Zahnrad&r ein, das zweite ein &6Großes Zahnrad&r, das dritte einen &6Eisenklumpen&r. Danach ist es ein &6Unfertiges Präzisionsgetriebe&r, das noch viermal durch dieselbe Strecke muss, fünf Runden insgesamt.",
              img(item_texture("create:incomplete_precision_mechanism"), 32, 32),
              "Führ das Band im Kreis, dann drehen unfertige Teile von selbst ihre Runden. Am Ende kommt in rund acht von zehn Fällen ein Präzisionsgetriebe heraus, sonst Reste wie Goldbleche oder Zahnräder, die du wieder einspeist.",
              "",
              "&6Tipp:&r In JEI siehst du jeden Schritt. Gib jedem Einsatzgerät per Filter nur sein eigenes Teil, dann verwechselt keins die Zutaten.",
          ],
          tasks=[task_item("create:precision_mechanism", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 16), reward_table("s2_uncommon")],
          deps=["deployer"], icon="create:precision_mechanism", size=2.0, shape="gear"),

    quest("precision_line", A + 12.5, 11, "&6Die Präzisionslinie",
          subtitle="Getriebe am laufenden Band.",
          description=[
              "Ein Präzisionsgetriebe von Hand ist ein Erfolgserlebnis. Das Obelisk-Ziel will aber &6300&r davon, und viele Maschinen brauchen sie ebenfalls: Mechanischer Arm, Drehzahlregler, Zugsteuerung, Fabrikanzeige.",
              "",
              "Automatisiere alle Zutaten: eine Presse macht Goldbleche, ein Einsatzgerät setzt Bretter auf Wellen für die Zahnräder, die Eisenklumpen kommen aus der Erzwäsche. Schleusen füllen die Einsatzgeräte nach, und die fertigen Getriebe landen in einer Kiste, oder gleich im Einspeiser am Obelisken.",
          ],
          tasks=[task_item("create:precision_mechanism", 64)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["precision"]),

    # ---- Messing-Logistik -------------------------------------------------------
    quest("brass_funnel", A, 18.75, "&6Messingschleuse und -tunnel",
          subtitle="Filter auf allem.",
          description=[
              "Die &6Messingschleuse&r (Elektronenröhre, Messingbarren, getrockneter Seetang) kann alles, was die Andesitschleuse kann, und mehr: ein &eFilterfeld&r für ein Item oder einen Listenfilter, und eine genaue &eStückzahl&r, die sie auf einmal bewegt.",
              "",
              "Der &6Messingtunnel&r sitzt auf einem Förderband und verteilt Items auf Bänder und Schleusen daneben. Den Modus stellst du am Wertefeld ein: aufteilen, reihum, zum nächsten Ausgang, zufällig oder synchron. Mit einem Filter schickt er nur bestimmte Items zur Seite.",
              "",
              "Ein &6Attribut Filter&r (Messingklumpen und Wolle) filtert nach Eigenschaften statt nach Namen, etwa alles, was sich waschen lässt, oder alles Verzauberte.",
          ],
          tasks=[task_item("create:brass_funnel", 4), task_item("create:brass_tunnel", 4)],
          rewards=[reward_item("create:brass_ingot", 16), reward_xp(3)],
          deps=["electron_tube"]),

    quest("smart_chute", A + 2.5, 17.75, "&6Schlauer Schacht",
          subtitle="Ein Schacht mit Filter.",
          description=[
              "Der &6Schlaue Schacht&r (Messingblech, Schacht, Elektronenröhre) lässt nur durch, was seinem Filter entspricht, und in der Menge, die du einstellst. Er zieht auch Items aus einem Lager über ihm.",
              "",
              "Perfekt, um aus einer großen Kiste genau das herauszuholen, was eine Maschine darunter braucht.",
          ],
          tasks=[task_item("create:smart_chute", 2)],
          rewards=[reward_xp(3)],
          deps=["brass_funnel"], optional=True),

    quest("arm", A + 2.5, 19.75, "&6Mechanischer Arm",
          subtitle="Nimmt hier, legt dort.",
          description=[
              "Der &6Mechanische Arm&r (Messingbleche, Andesitlegierung, Präzisionsgetriebe, Messingrahmen) greift Items an einer Stelle und legt sie an einer anderen ab. Bevor du ihn setzt, rechtsklickst du mit ihm in der Hand die Blöcke, von denen er nehmen soll (&eEingabe&r) und auf die er legen soll (&eAusgabe&r); ein zweiter Klick auf denselben Block wechselt zwischen beiden.",
              "",
              "Er reicht 5 Blöcke weit und bedient Depots, Bänder, Kisten, Becken, Lohenbrenner, Einsatzgeräte und Handwerkseinheiten. Am Wertefeld wählst du, ob er seine Ziele reihum oder der Reihe nach bedient.",
              "",
              "Ein Arm ersetzt oft ein halbes Dutzend Schleusen und Bänder, besonders in engen Anlagen. Er kostet 2 SU pro RPM.",
          ],
          tasks=[task_item("create:mechanical_arm", 1)],
          rewards=[reward_item("create:brass_ingot", 16), reward_table("s2_common")],
          deps=["brass_funnel", "precision"], icon="create:mechanical_arm", size=1.5),

    quest("observer", A + 5, 17.75, "&6Schlauer Beobachter und Schwellwert-Schalter",
          subtitle="Redstone, das Items versteht.",
          description=[
              "Der &6Schlaue Beobachter&r (Messingrahmen, Beobachter, Elektronenröhre) gibt ein Redstone-Signal, wenn ein bestimmtes Item an ihm vorbeikommt oder in dem Lager vor ihm liegt.",
              "",
              "Der &6Schwellwert-Schalter&r (Messingrahmen, Komparator, Elektronenröhre) schaltet ein, wenn ein Lager oder Tank über einen oberen Füllstand steigt, und erst wieder aus, wenn er unter einen unteren fällt.",
              "",
              "Zusammen mit einer Kupplung hältst du so eine Anlage an, wenn das Lager voll ist, und startest sie wieder, sobald Platz ist.",
          ],
          tasks=[task_item("create:content_observer", 1), task_item("create:stockpile_switch", 1)],
          rewards=[reward_xp(3)],
          deps=["brass_funnel"], optional=True),

    quest("display", A + 5, 19.75, "&6Anzeige-Link und Anzeigetafel",
          subtitle="Zahlen an die Wand.",
          description=[
              "Ein &6Anzeige-Link&r (Sender auf Messingrahmen) liest Informationen aus dem Block, an dem er hängt, und schreibt sie auf eine &6Anzeigetafel&r (Elektronenröhre und zwei Andesitlegierungen), ein Schild oder eine Nixie-Röhre in bis zu 64 Blöcken Entfernung. Klick erst mit dem Link auf das Ziel, dann setz ihn an die Quelle.",
              "",
              "Füllstände von Tresoren, Drehzahl und Belastung, die Uhrzeit oder im Zugkapitel die Abfahrtszeiten am Bahnhof: alles auf einer großen Tafel. Anzeigetafeln wachsen zusammen, wenn du sie nebeneinander setzt.",
          ],
          tasks=[task_item("create:display_link", 1), task_item("create:display_board", 4)],
          rewards=[reward_xp(3)],
          deps=["arm"], optional=True),

    quest("factory_gauge", A + 7.5, 18.75, "&6Fabrikanzeige",
          subtitle="Die Fabrik, die sich selbst bestellt.",
          description=[
              "Das Paketsystem aus Stufe 1 bekommt ein Gehirn. Eine &6Lagerverbindung&r und ein &6Präzisionsgetriebe&r ergeben zwei &6Fabrikanzeigen&r.",
              "",
              "Stimm die Anzeige auf dein Lagernetz ab (vor dem Setzen eine Lagerverbindung damit anklicken) und setz sie an die Maschine, die ein bestimmtes Item herstellt. Dann stellst du ein, welches Item das ist und wie viel davon vorrätig sein soll. Fällt der Vorrat darunter, bestellt die Anzeige die Zutaten aus dem Netz und schickt sie per Paket an die Maschine.",
              "",
              "Mehrere Anzeigen lassen sich miteinander verbinden, dann gibt die eine ihr Zwischenprodukt an die nächste weiter. So entstehen ganze Produktionsketten, die nur arbeiten, wenn etwas gebraucht wird. Die Ponder-Ansicht (&eW&r) zeigt das Zusammenspiel am besten.",
          ],
          tasks=[task_item("create:factory_gauge", 2)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["arm"], icon="create:factory_gauge", size=1.5),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("brass_engine", A + 8, 25.5, "&6&lDie Messingmaschine",
          subtitle="Füttere den Obelisken.",
          description=[
              "Das Obelisk-Ziel von Stufe 2 heißt &6Die Messingmaschine&r. Im Technik-Pfeiler will es &64 000 Messingbarren&r und &6300 Präzisionsgetriebe&r, gerechnet für 30 aktive Spieler. Im Magie-Pfeiler warten Manaperlen und Terrastahl aus Botania, und beide Pfeiler müssen voll werden.",
              "",
              "Das heißt: mehrere Messing-Mixer, die rund um die Uhr laufen, eine Zink- und Kupferversorgung aus Mahlwerk und Wäsche, und mindestens eine Präzisionslinie. Stell einen &eEinspeiser&r auf, eine Kiste oder ein Fass direkt am Obelisken, und leite deine Ausgabe dorthin: per Band, Kette, Paket oder Zug. Der Obelisk holt sich alle zwei Sekunden, was er brauchen kann, und schreibt es dir gut.",
              "",
              "Und vergiss die Magier nicht: sie brauchen deine Messingrahmen für die Terrestrische Agglomerationsplatte, du brauchst ihre Quelljuwelen für die Lohenbrenner. Bei 98 Prozent hält der Obelisk an, die letzte Ladung geht gemeinsam auf den Streams hinein, und &6Stufe 3, das Stahlwerk&r, öffnet sich.",
          ],
          tasks=[task_item("create:brass_ingot", 256), task_item("create:precision_mechanism", 32)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["precision_line"], icon="create:precision_mechanism", size=2.5, shape="gear"),

    # ---- Dampf (column B) -----------------------------------------------------------
    quest("steam_engine", B, 2.75, "&6Dampfmaschine",
          subtitle="Richtig viel Kraft.",
          description=[
              "Ein Dampfkessel ist ein &6Flüssigkeitstank&r mit &6Lohenbrennern&r darunter, &bWasser&r darin und einer oder mehreren &6Dampfmaschinen&r (Goldblech, Andesitlegierung, Kupferblock) an seinen Seiten. Vor jede Dampfmaschine gehört eine Welle, über die sie ihre Kraft abgibt.",
              "",
              "Wie stark der Kessel ist, zeigt dir die Ingenieursbrille als &eKesselstufe&r. Sie hängt von drei Dingen ab: Hitze (jeder erhitzte Brenner zählt eins, ein überhitzter zwei), Wasser (Pumpen, je schneller, desto mehr) und Größe des Tanks. Der kleinste der drei Werte bestimmt die Stufe.",
              "",
              "Create rechnet für eine voll versorgte Dampfmaschine mit &d1 024 SU pro RPM&r, das 32-fache eines Wasserrads.",
              "",
              "&cHäufiger Fehler:&r Zu wenig Wasser. Eine langsame Pumpe reicht nur für eine kleine Kesselstufe.",
          ],
          tasks=[task_item("create:steam_engine", 2), task_item("create:fluid_tank", 4)],
          rewards=[reward_item("minecraft:coal_block", 16), reward_table("s2_uncommon")],
          deps=["brass_casing"], icon="create:steam_engine", size=1.75, shape="gear"),

    quest("boiler", B + 2.5, 1.75, "&6Das Kraftwerk",
          subtitle="Ein Kessel für die ganze Basis.",
          description=[
              "Ein großer Kessel mit mehreren Dampfmaschinen ersetzt ganze Felder voller Wasserräder. Bau einen Tank mit 3 x 3 Blöcken Grundfläche und mehreren Blöcken Höhe, stell unter jedes Feld seines Bodens einen Lohenbrenner und versorge alle über ein Band oder einen Arm mit Brennstoff.",
              "",
              "Die Brille zeigt dir am Tank, was ihm zur nächsten Stufe fehlt: mehr Hitze, mehr Wasser oder mehr Volumen.",
              "",
              "Kohle aus einer Mine ist ein Anfang. Holzkohle aus einer Baumfarm mit Säge und Lüfter macht das Kraftwerk unabhängig, und wer es ganz bequem mag, heizt mit dem Lohenbrenner mit Strohhalm aus Crafts & Additions flüssig.",
          ],
          tasks=[task_item("create:steam_engine", 4), task_item("create:blaze_burner", 4)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["steam_engine"]),

    quest("whistle", B + 2.5, 3.75, "&6Dampfpfeife",
          subtitle="Tuuut.",
          description=[
              "Die &6Dampfpfeife&r (Goldblech und Kupferbarren) sitzt an einem Kessel und pfeift, solange sie ein Redstone-Signal bekommt. Mehrere übereinander ergeben tiefere Töne, und mit dem Schraubenschlüssel stimmst du sie.",
              "",
              "Ein Kessel, eine Handvoll Pfeifen und ein paar Redstone-Verbindungen: fertig ist die Fabriksirene zum Schichtwechsel, oder eine kleine Orgel für den Stream.",
          ],
          tasks=[task_item("create:steam_whistle", 1)],
          rewards=[reward_xp(3)],
          deps=["steam_engine"], optional=True),

    quest("speed_controller", B + 5, 1.75, "&6Drehzahlregler",
          subtitle="Genau die Drehzahl, die du willst.",
          description=[
              "Der &6Rotationsgeschwindigkeitsregler&r (Präzisionsgetriebe auf Messingrahmen) stellt die Drehzahl eines großen Zahnrads über ihm per Wertefeld exakt ein, bis 256 RPM in beide Richtungen. Seine eigene Rotation bekommt er über die Welle an seiner Seite.",
              "",
              "Damit laufen Maschinen genau so schnell, wie sie sollen, statt mit Zahnradpaaren zu raten. Denk daran: höhere Drehzahl heißt mehr Verbrauch aus derselben Belastbarkeit.",
          ],
          tasks=[task_item("create:rotation_speed_controller", 1)],
          rewards=[reward_xp(3)],
          deps=["boiler"]),

    quest("sequenced_gearshift", B + 5, 3.75, "&6Sequenzielle Gangschaltung",
          subtitle="Kleine Programme für Rotation.",
          description=[
              "Die &6Sequenzielle Gangschaltung&r (Messingrahmen, Zahnrad, Elektronenröhre) spielt bei einem Redstone-Signal ein kleines Programm ab: um einen Winkel drehen, einen Kolben oder Flaschenzug um eine Anzahl Blöcke bewegen, warten, andersherum drehen. Bis zu fünf Befehle hintereinander.",
              "",
              "Damit fährt ein Aufzug genau drei Stockwerke, ein Tor öffnet sich um 90 Grad, oder ein Bohrkopf rückt jede Runde einen Block vor.",
          ],
          tasks=[task_item("create:sequenced_gearshift", 1)],
          rewards=[reward_xp(3)],
          deps=["steam_engine"], optional=True),

    # ---- Kontraptionen (column B) -------------------------------------------------------
    quest("schematics", B, 9.5, "&6Baupläne und Bauplankanone",
          subtitle="Ganze Gebäude auf Knopfdruck.",
          description=[
              "Es beginnt am &6Bauplantisch&r (Holzstufen und glatter Stein) mit &6Leeren Bauplänen&r (Papier und hellblauer Farbstoff). Mit &6Bauplan und Feder&r markierst du ein Gebäude in der Welt und speicherst es als Datei. Baupläne aus deinem eigenen Ordner &eschematics&r lädst du am Bauplantisch auf den Server hoch.",
              img(item_texture("create:schematic"), 32, 32),
              "Die &6Bauplankanone&r (Eisenblöcke, Stämme, glatter Stein, Werfer) baut einen Bauplan dann Block für Block nach. Sie verschießt &6Schwarzpulver&r und nimmt die Blöcke aus Kisten, die an ihr stehen. Fehlt etwas, sagt sie dir, was.",
              "",
              "Ideal für Streams: eine Fabrikhalle in Ruhe im Einzelspieler planen, hochladen, und die Kanone setzt sie in wenigen Minuten auf.",
          ],
          tasks=[task_item("create:schematic_table", 1), task_item("create:schematicannon", 1)],
          rewards=[reward_item("minecraft:gunpowder", 32), reward_xp(5)],
          deps=["brass_casing"], icon="create:schematicannon", size=1.5),

    quest("contraption_controls", B + 2.5, 8.75, "&6Steuerung und Fernbedienung",
          subtitle="Werkzeuge an, Werkzeuge aus.",
          description=[
              "Die &6Vorrichtungs-Steuerung&r (Knopf, Andesitgehäuse, Elektronenröhre) sitzt auf einer Kontraption und schaltet ihre Werkzeuge ein oder aus, auch während der Fahrt. Mit einem Filter wirkt sie nur auf eine Sorte, etwa nur auf die Bohrer.",
              "",
              "Die &6Fernsteuerung&r (Holzknöpfe und eine Redstone-Verbindung) ist ein Gamecontroller für Redstone-Verbindungen: jede Taste funkt auf ihrer eigenen Frequenz. Auf einem Lesepult an einer Kontraption steuerst du damit fahrende Maschinen von innen.",
          ],
          tasks=[task_item("create:contraption_controls", 1), task_item("create:linked_controller", 1)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("elevator", B + 2.5, 10.75, "&6Aufzug-Seilrolle",
          subtitle="Ein richtiger Aufzug.",
          description=[
              "Die &6Aufzug-Seilrolle&r (Messingrahmen, getrockneter Seetangblock, Eisenblech) ist der große Bruder des Flaschenzugs. Sie fährt eine Kabine zwischen Stockwerken, die du mit &6Redstone-Kontakten&r am Schacht markierst. Eine Vorrichtungs-Steuerung in der Kabine wird zur Stockwerkswahl.",
              "",
              "Passend dazu: das &6Uhrwerk-Lager&r (Holzstufe, Messingrahmen, Elektronenröhre) dreht Stunden- und Minutenzeiger einer echten Uhr, zum Beispiel am Turm neben dem Obelisken.",
          ],
          tasks=[task_item("create:elevator_pulley", 1)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("cart_assembler", B + 5, 8.75, "&6Loren-Kontraptionen",
          subtitle="Kontraptionen auf Schienen.",
          description=[
              "Der &6Lorenmonteur&r (Legierung, Redstone, Stämme) liegt als Schiene im Gleis. Fährt eine Lore darüber, während er ein Redstone-Signal bekommt, nimmt sie die angeklebten Blöcke mit: ein fahrender Bohrer, eine Erntemaschine auf Schienen. Die &6Steuerungsschiene&r (Gold, Stock, Elektronenröhre) regelt ihr Tempo per Signalstärke.",
              "",
              "Für lange Strecken sind die Züge aus &6Create: Züge&r die bessere Wahl, aber für kurze Wege im Bergwerk ist eine Lore mit Bohrer unschlagbar günstig.",
          ],
          tasks=[task_item("create:cart_assembler", 1), task_item("create:controller_rail", 6)],
          rewards=[reward_item("minecraft:rail", 32), reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("roller", B + 5, 10.75, "&6Mechanische Walze",
          subtitle="Straßen bauen im Vorbeifahren.",
          description=[
              "Die &6Mechanische Walze&r (Elektronenröhre, Andesitgehäuse, Mahlwerkrad) sitzt vorn an einer Kontraption oder einem Zug. Sie räumt den Weg frei, füllt Löcher und pflastert den Boden mit dem Block aus ihrem Filterfeld. Die Blöcke nimmt sie aus Lagern auf der Kontraption.",
              "",
              "Ein Zug mit zwei Walzen vorn ebnet seine eigene Trasse, auf der du danach die Gleise verlegst.",
          ],
          tasks=[task_item("create:mechanical_roller", 2)],
          rewards=[reward_xp(3)],
          deps=["schematics"], optional=True),

    quest("potato_cannon", B + 7.5, 9.75, "&6Kartoffelkanone",
          subtitle="Das Werkzeug, das niemand braucht und jeder will.",
          description=[
              "Die &6Kartoffelkanone&r ist ein Rezept für die Handwerkseinheiten: Andesitlegierung, Präzisionsgetriebe, Flüssigkeitsrohre und Kupfer. Sie verschießt Kartoffeln und fast jedes andere Essen, jedes mit eigener Wirkung, und bezieht ihre Druckluft aus dem &6Kupfer-Rückentank&r auf deinem Rücken.",
              img(item_texture("create:potato_cannon"), 32, 32),
              "Ebenfalls aus der Handwerkseinheit: der &6Extendo Griff&r verlängert deine Reichweite, und der &6Symmetriestab&r spiegelt beim Bauen jeden Block, den du setzt.",
          ],
          tasks=[task_item("create:potato_cannon", 1)],
          rewards=[reward_item("minecraft:baked_potato", 32), reward_xp(3)],
          deps=["schematics"], optional=True),

    # ---- Addons (column B) ------------------------------------------------------------
    quest("addons", B, 20.5, "&dDie Create-Addons",
          subtitle="Was es zu Create sonst noch gibt.",
          description=[
              "Auf Kronwerke laufen mehrere Erweiterungen für Create. Die meisten öffnen mit dieser Stufe, weil sie auf Messing, Elektronenröhren oder Lohenbrennern aufbauen:",
              "&6Create: Enchantment Industry&r: Erfahrung als Flüssigkeit, Verzaubern und Schmieden mit Lohen, Bücher drucken.",
              "&6Create: New Age&r: Strom aus Rotation mit Spulen und Magneten, Motoren und Aufladen.",
              "&6Create Crafts & Additions&r: Walzwerk, Alternator, Elektromotor, Kabel, Akkus, Teslaspule und flüssige Brennstoffe.",
              "&6Create Connected&r: Kleinteile wie Bremse, Kurbelrad, Lüfter-Katalysatoren, Kinetische Batterie und Copycat-Blöcke.",
              "&6Create Mechanical Spawner&r: Mobs aus einer Flüssigkeit.",
              "",
              "Außerdem gibt es &6Create Jetpack&r (braucht Elytren, also frühestens Stufe 4) und &6Copycats+&r für Deko-Blöcke aus Zink, die das Aussehen jedes anderen Blocks annehmen.",
              "",
              "&eGut zu wissen:&r Strom aus Create-Addons in &dFE&r versteht auch Mekanism, das in dieser Stufe öffnet. Eine Dampfmaschine mit Alternator kann deine ersten Mekanism-Maschinen versorgen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["brass_casing"], icon="create:brass_casing", size=1.5, shape="hexagon"),

    # Enchantment Industry
    quest("grindstone", B + 2.5, 16, "&6Mechanischer Schleifstein",
          subtitle="Enchantment Industry: Erfahrung zum Abfüllen.",
          description=[
              "Acht Andesitlegierungen um eine Welle ergeben den &6Mechanischen Schleifstein&r. Rechtsklicke damit einen &6Abfluss&r: er wird zum &6Schleifsteinabfluss&r. Setz einen zweiten Schleifstein obendrauf und treib ihn an.",
              "",
              "Was darauf landet, wird geschliffen: &6Erfahrungsklumpen&r aus dem Mahlwerk werden zu &bFlüssiger Erfahrung&r, verzauberte Items verlieren ihre Verzauberungen, und die Erfahrung daraus fließt ebenfalls in den Abfluss. Nebenbei poliert er wie Schmirgelpapier, zum Beispiel Rosenquarz.",
              "",
              "Deine eigenen Level zahlst du an einer &6Erfahrungsluke&r ein und ab: Rechtsklick speichert, Schleichen und Rechtsklick holt sie zurück. Sie entsteht, wenn du einen Block Gehärtete Erfahrung auf eine Fluid Hatch anwendest, die aus einem Abfluss und einem Kupferbarren gebaut wird.",
          ],
          tasks=[task_item("create_enchantment_industry:mechanical_grindstone", 2)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(5)],
          deps=["addons"]),

    quest("blaze_enchanter", B + 5, 16, "&6Lohen-Verzaubrerer",
          subtitle="Eine Lohe, die verzaubert.",
          description=[
              "Der &6Lohen-Verzaubrerer&r entsteht am Schmiedetisch aus einem &6Lohenbrenner&r, einem &6Zaubertisch&r und einer &6Schmiedevorlage&r für das Lohen-Upgrade. Die erste Vorlage findest du in Kisten von &cNetherfestungen&r und &cBastionsruinen&r; weitere kopierst du mit Lohenruten und Netherrack wie andere Schmiedevorlagen.",
              "",
              "Er verzaubert wie ein Zaubertisch, aber mit &bFlüssiger Erfahrung&r statt deiner Level und ohne Lapis, bis Stufe 30. Das Level stellst du am Wertefeld ein. Mit einem Item im Filterfeld erzeugt er &6Verzauberungsvorlagen&r, die genau die Verzauberungen tragen, die zu diesem Item passen.",
              "",
              "Sein Bruder, der &6Lohen-Schmied&r (Lohenbrenner, Amboss, Vorlage), vereint Verzauberungen wie ein Amboss, aber ohne steigende Reparaturkosten, und überträgt Vorlagen auf Werkzeug und Rüstung.",
          ],
          tasks=[task_item("create_enchantment_industry:blaze_enchanter", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["grindstone"]),

    quest("printer", B + 7.5, 16, "&6Drucker",
          subtitle="Bücher kopieren, am Fließband.",
          description=[
              "Der &6Drucker&r (Messingblech, Ausguss, Eisenblock) kopiert mit &bFlüssiger Erfahrung&r den Inhalt eines Buchs: beschriebene Bücher, verzauberte Bücher, Bannermuster. Die Vorlage gibst du ihm, die Rohlinge laufen darunter auf dem Band durch.",
              "",
              "Verzauberte Bücher zu kopieren kostet viel Erfahrung, aber eine einzige gute Verzauberung reicht dann für den ganzen Server.",
          ],
          tasks=[task_item("create_enchantment_industry:printer", 1)],
          rewards=[reward_item("minecraft:book", 16), reward_xp(3)],
          deps=["blaze_enchanter"], optional=True),

    # Create: New Age
    quest("na_generator", B + 2.5, 19, "&6Strom aus Rotation",
          subtitle="Create: New Age: Spulen, Magnete, Bürsten.",
          description=[
              "Create: New Age macht aus Rotation Strom. Das Herz ist die &6Generator Coil&r (acht Kupferbarren um einen Andesitlegierungsblock). Dreht sie sich und ist von &6Magneten&r umgeben, erzeugt sie Energie. &6Carbon Brushes&r (Legierung, Kohle, Welle) am Ende der Spulen nehmen den Strom ab.",
              "",
              "Den Anfang macht der &6Redstone Magnet&r (Eisenklumpen um einen Redstoneblock), stärkere Magnete folgen mit überladenem Metall. Je stärker die Magnete rundherum, desto mehr der eingesetzten SU wird zu Strom, desto mehr SU zieht die Spule aber auch.",
              "",
              "Leitungen legst du mit &6Copper Wire&r (Kupferblech in der Säge) zwischen &6Electrical Connectors&r (Legierung und Kupferklumpen). Ein Connector im Modus &ePull&r (Schraubenschlüssel) holt Energie aus Blöcken anderer Mods.",
          ],
          tasks=[task_item("create_new_age:generator_coil", 1), task_item("create_new_age:carbon_brushes", 1),
                 task_item("create_new_age:redstone_magnet", 4)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["addons"], icon="create_new_age:generator_coil"),

    quest("na_motor", B + 5, 19, "&6Basic Motor",
          subtitle="Strom zurück in Rotation.",
          description=[
              "Der &6Basic Motor&r (Eisenklumpen, Andesitgehäuse, Welle und ein &6Magnetite Block&r) macht aus Strom wieder Rotation. Die Drehzahl stellst du mit dem Schraubenschlüssel ein, die Belastbarkeit bleibt dabei gleich. Ein Redstone-Signal schaltet ihn ab.",
              "",
              "&6Magnetite Blocks&r kannst du nicht herstellen: sie liegen als eigene Adern im Stein der Oberwelt, zwischen Höhe -20 und 60. Halte beim Graben die Augen offen.",
              "",
              "Motoren lohnen sich, wenn Kraft an einem Ort entsteht und an einem anderen gebraucht wird. Ein Kabel ist einfacher als eine hundert Blöcke lange Welle.",
          ],
          tasks=[task_item("create_new_age:basic_motor", 1)],
          rewards=[reward_xp(5)],
          deps=["na_generator"]),

    quest("na_energiser", B + 7.5, 19, "&6Basic Energiser",
          subtitle="Aufladen mit Strom.",
          description=[
              "Der &6Basic Energiser&r (Andesitgehäuse und Blitzableiter) arbeitet wie eine Presse über einem Depot oder Band, nur mit Strom und Rotation: er lädt Items auf. Aus einem Eisenbarren wird &6Overcharged Iron&r, aus Gold &6Overcharged Gold&r. Daraus entstehen stärkere Magnete und Kabel.",
              img(item_texture("create_new_age:overcharged_iron"), 32, 32),
              "Überladenes Eisen steckt auch im &6Heater&r, der einen Dampfkessel mit Wärme statt mit Kohle heizt. Die Wärme liefern Solar-Heizplatten oder der Stirling Engine des Addons.",
          ],
          tasks=[task_item("create_new_age:basic_energiser", 1), task_item("create_new_age:overcharged_iron", 4)],
          rewards=[reward_xp(3)],
          deps=["na_motor"], optional=True),

    # Create Crafts & Additions
    quest("rolling_mill", B + 2.5, 22, "&6Walzwerk",
          subtitle="Crafts & Additions: Ruten und Kabel.",
          description=[
              "Das &6Walzwerk&r (Eisenbleche, Wellen, Legierung, Andesitgehäuse) walzt Barren zu &6Ruten&r und Bleche zu &6Kabeln&r: aus einem Kupferbarren werden zwei Kupferruten, aus einem Kupferblech zwei Kupferkabel. Items gibst du oben hinein, per Hand, Schleuse oder Band.",
              "",
              "Kabel wickelst du auf eine &6leere Spule&r (Eisenbleche und Eisenrute) zur &6Kupferspule&r. Spulen, Ruten und &6Kondensatoren&r (Kupfer- und Zinkblech mit einer Redstonefackel) sind die Bauteile aller Maschinen dieses Addons.",
          ],
          tasks=[task_item("createaddition:rolling_mill", 1), task_item("createaddition:copper_spool", 2)],
          rewards=[reward_item("minecraft:copper_ingot", 32), reward_xp(3)],
          deps=["addons"]),

    quest("alternator", B + 5, 22, "&6Alternator",
          subtitle="Rotation rein, FE raus.",
          description=[
              "Der &6Alternator&r ist ein Rezept für die Handwerkseinheiten: Kupferspulen, Eisenbleche, eine Eisenrute und Andesitlegierung. Treib ihn mit einer Welle an, und er erzeugt &dFE&r, die Energie, die auch Mekanism und viele andere Mods verstehen.",
              "",
              "Je höher die Drehzahl, desto mehr Strom, und desto mehr SU zieht er aus dem Netz. Eine Dampfmaschine mit Alternator ist ein solides erstes Kraftwerk für &6Mekanism&r.",
              "",
              "Den Strom verteilst du über &6Netzanschlüsse&r (Kupferrute, Legierung, Schleimball): mit einer Kupferspule in der Hand verbindest du zwei Anschlüsse. Ein &6Akkumulator&r puffert ihn für die Nacht.",
          ],
          tasks=[task_item("createaddition:alternator", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["rolling_mill"], icon="createaddition:alternator"),

    quest("electric_motor", B + 7.5, 22, "&6Elektromotor",
          subtitle="FE rein, Rotation raus.",
          description=[
              "Der &6Elektromotor&r ist das Gegenstück zum Alternator, ebenfalls aus der Handwerkseinheit, mit Messingblechen und einem Kondensator. Er verbraucht FE und liefert Rotation mit einstellbarer Drehzahl.",
              "",
              "So läuft ein Mixer oder eine Presse auch dort, wo kein Bach fließt und keine Windmühle Platz hat: der Strom kommt per Kabel, zum Beispiel aus einem Mekanism-Generator.",
          ],
          tasks=[task_item("createaddition:electric_motor", 1)],
          rewards=[reward_xp(5)],
          deps=["alternator"]),

    quest("tesla_coil", B + 10, 22, "&6Teslaspule",
          subtitle="Laden und elektrifizieren.",
          description=[
              "Die &6Teslaspule&r (Handwerkseinheiten-Rezept mit Spulen, Kondensatoren, Messing und Elektronenröhre) lädt Items auf einem Depot oder Band darunter mit FE: Akkus und Werkzeuge anderer Mods, und aus &6Goldbarren&r wird &6Electrumbarren&r.",
              "",
              "Gut zu wissen: gibst du einem Lohenbrenner einen &6Strohhalm&r (Papier oder Bambus im Walzwerk), wird er zum &6Lohenbrenner mit Strohhalm&r. Der verbrennt flüssige Brennstoffe wie &bSamenöl&r oder &bBiobrennstoff&r und hält einen Dampfkessel ganz ohne Kohle am Laufen.",
          ],
          tasks=[task_item("createaddition:tesla_coil", 1)],
          rewards=[reward_xp(3)],
          deps=["electric_motor"], optional=True),

    # Create Connected and more
    quest("fan_catalyst", B + 2.5, 25, "&6Lüfter-Katalysatoren",
          subtitle="Create Connected: Waschen ohne Wasserblock.",
          description=[
              "Ein &6Leerer Lüfter Katalysator&r (Messingbarren und Eisengitter) kommt vor einen Lüfter, dorthin, wo sonst Wasser oder Lava steht. Rechtsklicke ihn mit einem &bWassereimer&r, einem &cLavaeimer&r oder mit &6Seelensand&r, und er wird zum Waschenden, Schmelzenden oder Spukenden Lüfter Katalysator.",
              "",
              "Der Vorteil: kein Wasser, das wegläuft, keine Lava, die etwas anzündet, und es sieht ordentlich aus. Mit dem Spukenden Katalysator klappt jetzt auch das &eHeimsuchen&r, JEI zeigt, was sich damit verwandeln lässt.",
          ],
          tasks=[task_item("create_connected:empty_fan_catalyst", 1)],
          rewards=[reward_xp(3)],
          deps=["addons"]),

    quest("connected_parts", B + 5, 25, "&6Kleinteile aus Create Connected",
          subtitle="Bremse, Kurbelrad, Batterie.",
          description=[
              "Create Connected ergänzt viele praktische Teile, hier eine Auswahl:",
              "&6Kurbelrad&r: eine Handkurbel mit Zahnkranz, die mit Zahnrädern daneben kämmt.",
              "&6Bremse&r: hält eine Welle bei Redstone-Signal fest, statt sie nur abzukoppeln.",
              "&6Zentrifugal Kupplung&r: kuppelt erst ab einer eingestellten Drehzahl ein.",
              "&6Paralleles Getriebe&r: ein Getriebe mit großem Zahnrad für versetzte Achsen.",
              "&6Kinetische Batterie&r (Präzisionsgetriebe, Messingrahmen, Eisenbleche, Redstone): speichert Rotation und gibt sie später wieder ab.",
              "&6Item Silo&r und &6Flüssigkeitsgefäß&r: Tresor und Tank in anderer Ausrichtung.",
          ],
          tasks=[task_item("create_connected:crank_wheel", 1)],
          rewards=[reward_xp(3)],
          deps=["fan_catalyst"], optional=True),

    quest("spawner", B + 7.5, 25, "&6Mechanical Spawner",
          subtitle="Mobs aus der Flüssigkeit.",
          description=[
              "Der &6Mechanical Spawner&r ist ein großes Rezept für die Handwerkseinheiten aus Messing, Eisengittern und einem Smaragd. Pumpst du &bSpawn Fluid&r hinein und gibst ihm Rotation, lässt er Mobs entstehen.",
              "",
              "Das zufällige Spawn Fluid mischt ein erhitzter Mixer aus &bFlüssiger Erfahrung&r und Wasser, oder aus Lohenrute, Enderperle und Wasser. Für bestimmte Mobs gibt es eigene Sorten, JEI zeigt die Rezepte. Eine Mobfarm ohne Spawner, gleich neben deinem Lager.",
          ],
          tasks=[task_item("create_mechanical_spawner:mechanical_spawner", 1)],
          rewards=[reward_xp(5)],
          deps=["fan_catalyst"], optional=True),
]

images = [
    head("title", "Create: Messing", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 2: Messingwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("brass", "Messing", A - 0.6, 0.1),
    head("precision", "Präzision", A - 0.6, 8),
    head("logistics", "Messing-Logistik", A - 0.6, 16.3),
    head("goal", "Das Ziel", A + 6.65, 23),
    head("steam", "Dampf", B - 0.6, 0.1),
    head("contraptions", "Kontraptionen", B - 0.6, 7),
    head("addons", "Addons", B - 0.6, 13.1),
    head("note_cei", "Enchantment Industry", B + 1.9, 14.85, height=0.5, kind="note", colour="magic"),
    head("note_cna", "New Age", B + 1.9, 17.85, height=0.5, kind="note", colour="water"),
    head("note_cca", "Crafts & Additions", B + 1.9, 20.85, height=0.5, kind="note", colour="fire"),
    head("note_cc", "Connected und mehr", B + 1.9, 23.85, height=0.5, kind="note", colour="stone"),
]
images[0]["x"] = 13.5
images[1]["x"] = 13.5

chapter(C, "Create: Messing", "create:brass_casing", "tech", quests, shape="gear", order=9, stage=2,
        subtitle=["Stufe 2: Lohenbrenner, Messing, Präzisionsgetriebe und die Create-Addons."], images=images)
