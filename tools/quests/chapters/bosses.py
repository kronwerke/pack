"""The overworld bosses in stage 1: the five L_Ender's Cataclysm structures of the overworld in
the order a group can take them (cursed pyramid and frosted prison with stage 1 gear, sunken
city with stage 2 gear, ancient factory needs a nether star from stage 2, acropolis with stage 3
gear), each boss with a preparation and a kill quest, their drops and what they make; the Born
in Chaos night mobs, dark metal and the dark tower; Mowzie's Mobs. Boss numbers come from the
entity classes and cataclysm-common.toml, drops from the loot tables. Ignis, the Netherite
Monstrosity and the Ender Guardian belong to the Nether and End chapters and are only named."""
from ftbq import (chapter, quest, task_item, task_kill, task_advancement, task_checkmark,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "bosses"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Vorbereitung -------------------------------------------------------
    quest("welcome", 0, 0, "&c&lBosse der Oberwelt",
          subtitle="Fünf Bauwerke, fünf Bosse, in der richtigen Reihenfolge.",
          description=[
              "&6L_Ender's Cataclysm&r stellt fünf Bauwerke in die Oberwelt, und in jedem wartet ein Boss mit 390 bis 450 Lebenspunkten. Kein Boss zählt für den Obelisken. Ihre Beute macht dich aber stärker, und darum geht es hier.",
              "",
              "&eDie Reihenfolge in diesem Kapitel:&r",
              "&e1.&r Wüste, &6Verfluchte Pyramide&r: Ancient Remnant. Geht mit Diamantrüstung aus Stufe 1.",
              "&e2.&r Schneeebene, &6Frosted Prison&r: Maledictus. Geht ebenfalls mit Stufe 1, zu mehreren.",
              "&e3.&r Tiefsee, &6Sunken City&r: The Leviathan. Besser mit Ausrüstung aus Stufe 2.",
              "&e4.&r Untergrund, &6Ancient Factory&r: The Harbinger. Braucht einen Netherstern, also Stufe 2.",
              "&e5.&r Himmel über dem warmen Meer, &6Akropolis&r: Scylla. Nimm Ausrüstung aus Stufe 3 mit.",
              "",
              "Dazu kommen die Nachtmonster aus &6Born in Chaos&r und die Kreaturen aus &6Mowzie's Mobs&r, unten im Kapitel. Die Zauberer aus &dIron's Spells&r (Pyromancer, Necromancer, der Dead King) haben ihr eigenes Kapitel.",
              "",
              "&cIgnis&r und die &cNetherite Monstrosity&r stehen im Kapitel &cDer Nether&r, der &cEnder Guardian&r im Kapitel &5Das End&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(3)],
          icon="cataclysm:ancient_remnant_spawn_egg", size=2.0, shape="hexagon"),

    quest("rules", 2.5, -1.3, "&eLern die Regeln der Bosse",
          subtitle="Große Schläge bringen nichts, Ausdauer schon.",
          description=[
              "Jeder Cataclysm-Boss hat drei Grenzen: Ein Treffer macht höchstens &e20 bis 22 Schaden&r, pro Sekunde kommen höchstens &e13 bis 15 Schaden&r durch, und wer weiter als &e12 bis 38 Blöcke&r weg steht, macht fast keinen Schaden mehr.",
              "",
              "Das heißt: Ein Schwert mit Schärfe V und Kritischen Treffern ist so gut wie ein verzaubertes Eisenschwert, solange du ständig triffst. Mehrere Spieler zählen aber jeder für sich. Zu fünft fällt ein Boss fünfmal so schnell.",
              "",
              "Lässt du den Boss allein, heilt er sich mit &e25 Lebenspunkten&r pro Heilung wieder hoch. Also nicht zum Nachladen nach Hause laufen, sondern Vorräte mitbringen.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["welcome"], icon="minecraft:iron_sword"),

    quest("gear", 2.5, 1.3, "&ePack die Bosskiste",
          subtitle="Schild, Goldäpfel und ein Weg zurück.",
          description=[
              "Für jeden Bosskampf: ein &6Schild&r, mindestens &62 Goldäpfel&r, ein Stapel Essen, Pfeile und eine &6Rückkehr-Schriftrolle&r von Waystones. Ein Wegpunkt am Eingang des Bauwerks spart den langen Rückweg.",
              "",
              "&eRüstung:&r Diamant mit Schutz IV ist für Pyramide und Gefängnis genug. Apotheosis gibt dir bis Stufe 1 seltene Affixe auf Waffen und Rüstung, die Zahlen im Tooltip lohnen einen Blick.",
              "",
              "&eZu mehreren:&r Einer hält mit dem Schild den Blick des Bosses, die anderen schlagen von der Seite. Wer heilt, steht hinten. Ein Ars-Zauber &eProjektil, Heilen&r heilt aus der Ferne.",
          ],
          tasks=[task_item("minecraft:shield", 1), task_item("minecraft:golden_apple", 2)],
          rewards=[reward_item("minecraft:arrow", 32), reward_table("s1_common")],
          deps=["welcome"], icon="minecraft:shield"),

    # ---- Die verfluchte Pyramide --------------------------------------------
    quest("desert_find", 5.5, 0, "&6Finde die verfluchte Pyramide",
          subtitle="Eine große Pyramide in der Wüste, bewacht von Koboleton.",
          description=[
              "Die &6Verfluchte Pyramide&r steht in der &eWüste&r (nur im Biom Wüste). Such von einem hohen Punkt aus oder nimm den &6Naturkompass&r, der das nächste Wüstenbiom zeigt.",
              "",
              "Rundherum leben &cKoboleton&r (25 Lebenspunkte, schnell). Sie klauen dir Gegenstände aus der Hand und rennen weg. &6Klebrige Handschuhe&r (Faden, Leder, Schleimball, Hasenfell, formlos) verhindern das. Sie lassen Koboleton-Knochen und selten Altmetall fallen.",
              "",
              "In der Pyramide gibt es Fallen aus Sandstein: fallende Blöcke, Feuer und Giftpfeile. Geh langsam und nicht als Gruppe durch enge Gänge. Die Kisten unten enthalten &6Altmetall&r, manchmal einen &6Unzerbrechlichen Schädel&r oder ein &6Lebens-Ankh&r.",
              "",
              "Ab Stufe 2 craftest du das &6Wüstenauge&r (Enderauge in der Mitte, Gold, gemeißelter Sandstein, Smaragd, toter Busch, Kaktus, verrottetes Fleisch, Knochen). Es fliegt wie ein Enderauge zur nächsten Pyramide.",
          ],
          tasks=[task_advancement("cataclysm:find_cursed_pyramid", "Die verfluchte Pyramide finden")],
          rewards=[reward_item("cataclysm:sticky_gloves", 1), reward_xp(5)],
          deps=["gear"], icon="minecraft:sandstone"),

    quest("desert_minibosses", 8, -1.3, "&6Besiege Wadjet und den Kobolediator",
          subtitle="Die beiden Wächter der Pyramide.",
          description=[
              "Zwei Zwischenbosse bewachen die Gänge: &cWadjet&r, die Kobra (150 Lebenspunkte, 11 Schaden, ruft Sandstürme für 6 und Steinsäulen für 11), und der &cKobolediator&r (180 Lebenspunkte, Rüstung 10, 14 Schaden).",
              "",
              "Wadjet lässt &e2 bis 4 Altmetallbarren&r fallen, der Kobolediator seinen &6Schädel&r, &e3 bis 5 Koboleton-Knochen&r und &e1 bis 3 Altmetallbarren&r.",
              "",
              "Daraus wird die &6Knochenreptil-Rüstung&r: Helm aus dem Kobolediator-Schädel, 2 Altmetall und 2 Knochen; Brustplatte aus 4 Altmetall und 4 Knochen. Härte 2,5 und Rückstoßwiderstand, ein guter Schritt vor dem großen Kampf.",
          ],
          tasks=[task_kill("cataclysm:wadjet", 1), task_kill("cataclysm:kobolediator", 1)],
          rewards=[reward_item("cataclysm:koboleton_bone", 4), reward_item("minecraft:golden_apple", 1), reward_xp(10)],
          deps=["desert_find"], icon="cataclysm:kobolediator_skull"),

    quest("remnant_prep", 8, 1.3, "&6Weck den Ancient Remnant",
          subtitle="Eine Kette aus dem Sand, dann ein Rechtsklick.",
          description=[
              "Bürste den &6Verdächtigen Sand&r in der Pyramide mit einem &6Pinsel&r (Feder, Kupferbarren, Stock). Darin liegt die &6Halskette der Wüste&r. Unten in der großen Halle schläft der &cAncient Remnant&r. Rechtsklick mit der Kette auf ihn, und er wacht auf.",
              "",
              pic("cataclysm:necklace_of_the_desert"),
              "",
              "Die Kette wird dabei verbraucht. Solange er schläft, kannst du in Ruhe die Halle ausleuchten, Wegpunkt setzen und alle versammeln. Erst wecken, wenn alle bereit sind.",
          ],
          tasks=[task_item("cataclysm:necklace_of_the_desert", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s1_common")],
          deps=["desert_find"], icon="cataclysm:necklace_of_the_desert"),

    quest("remnant_kill", 10.5, 0, "&c&lBesiege den Ancient Remnant",
          subtitle="450 Lebenspunkte, Panzer aus Altmetall.",
          description=[
              "Der &cAncient Remnant&r hat &e450 Lebenspunkte&r, Rüstung 12 und schlägt für 25. Sein Ansturm nimmt dir &e10 Prozent&r deiner maximalen Lebenspunkte, Erdbeben und Steinsäulen machen je 11. Treffer über 21 werden gekappt, mehr als 14 Schaden pro Sekunde kommen nicht durch, und ab 14 Blöcken Abstand bist du zu weit weg.",
              "",
              "&eSo geht es:&r Bleib nah dran und seitlich. Beim Ansturm zur Seite springen, gegen den Wüstensturm hinter eine Säule. Wenn er in die Wand rennt, ist er kurz benommen, dann draufhauen.",
              "",
              "&eBeute:&r &6Sandsturm in einer Flasche&r (Rechtsklick ruft zwei kreisende Sandstürme), &6Remnant-Schädel&r (ruft einen Modern Remnant, zähmbar mit einem Schnüffler-Ei) und ein &6Altmetallblock&r, also 9 Barren. Daraus wird der &6Alte Speer&r (4 Barren, Linksklick schießt einen Sandsturm, 9,5 Schaden).",
              "",
              "An seinem Platz erscheint ein &6Boss-Wiederbeleber&r. Rechtsklick mit einem &6Wüstenauge&r (ab Stufe 2) darauf, und der Kampf geht von vorn los.",
          ],
          tasks=[task_kill("cataclysm:ancient_remnant", 1)],
          rewards=[reward_table("s1_uncommon"), reward_item("cataclysm:ancient_metal_ingot", 4), reward_xp(20)],
          deps=["remnant_prep"], icon="cataclysm:sandstorm_in_a_bottle", size=1.5, shape="diamond"),

    # ---- Das frostige Gefaengnis --------------------------------------------
    quest("prison_find", 13.5, 0, "&bFinde das Frosted Prison",
          subtitle="Ein Gefängnis im Schnee voller Draugr.",
          description=[
              "Das &6Frosted Prison&r steht in der &eSchneeebene&r (Biom Snowy Plains). In derselben Gegend findest du verlassene Dörfer, Tempel und Türme mit &6Schwarzstahl&r und &6Stabilen Stiefeln&r (laufen über Pulverschnee) in den Kisten.",
              "",
              "Drinnen warten &cDraugr&r (28 Lebenspunkte, Rüstung 3), Elite-Draugr und Königliche Draugr. Sie lassen &6Schwarzstahl-Nuggets&r fallen, von deiner Hand getötet manchmal einen Barren. Neun Nuggets ergeben einen &6Schwarzstahlbarren&r.",
              "",
              "Aus Schwarzstahl craftest du Werkzeug wie aus Eisen: &6Schwarzstahlschwert&r (2 Barren, Stock) und die &6Schwarzstahl-Tartsche&r, ein Schild aus Barren, 4 Nuggets und 4 Brettern. Heb mindestens &e4 Barren&r auf, du brauchst sie für die Waffen aus Cursium.",
              "",
              "Ab Stufe 2 führt dich das &6Fluchauge&r hierher: Enderauge, Gold, Knochen, 2 Phantomhäute, verrottetes Fleisch.",
          ],
          tasks=[task_advancement("cataclysm:find_frosted_prison", "Das Frosted Prison finden")],
          rewards=[reward_item("cataclysm:black_steel_ingot", 2), reward_xp(5)],
          deps=["remnant_kill"], icon="cataclysm:frosted_stone_bricks"),

    quest("aptrgangr", 16, 0, "&bHol den Schlüssel vom Aptrgangr",
          subtitle="Ein großer Draugr, ein seltsamer Schlüssel, ein Siegeltor.",
          description=[
              "Der &cAptrgangr&r (160 Lebenspunkte, Rüstung 10, 18 Schaden, wirft Axtklingen für 8) lässt den &6Seltsamen Schlüssel&r fallen. Damit öffnest du das &6Tor des Siegels&r unten im Gefängnis.",
              "",
              pic("cataclysm:strange_key"),
              "",
              "Er schlägt langsam, aber hart. Weich nach hinten aus, wenn er die Axt hebt, und schlag zu, während er sie wieder hochzieht. Dazu gibt es 1 bis 2 Schwarzstahlbarren und 2 bis 4 Nuggets.",
          ],
          tasks=[task_kill("cataclysm:aptrgangr", 1), task_item("cataclysm:strange_key", 1)],
          rewards=[reward_item("cataclysm:black_steel_ingot", 4), reward_xp(10)],
          deps=["prison_find"], icon="cataclysm:strange_key"),

    quest("maledictus_kill", 18.5, 0, "&c&lBesiege Maledictus",
          subtitle="Der verfluchte Ritter hinter dem Siegeltor.",
          description=[
              "Hinter dem Tor steht der &6Verfluchte Grabstein&r. Rechtsklick ruft &cMaledictus&r: &e420 Lebenspunkte&r, Rüstung 10, 13 Schaden im Nahkampf, Phantomhellebarden für 11, Phantompfeile für 5. Sein Sturzflug kostet dich 10 Prozent deiner Lebenspunkte, der Flächenschlag 15.",
              "",
              "&eSo geht es:&r Er greift in festen Mustern an, jedes Muster hat eine Pause am Ende. Schild hoch, Pfeile und Hellebarden abwarten, dann drei bis vier Schläge. Treffer über 20 werden gekappt, mehr als 13 pro Sekunde zählen nicht.",
              "",
              "&eBeute:&r &e3 bis 4 Cursium-Barren&r. Mit Schwarzstahl werden daraus sofort Waffen: &6Fluchbogen&r (2 Cursium, 1 Schwarzstahl, 3 Faden, schießt drei Phantompfeile), &6Soul Render&r (3 Cursium, 2 Schwarzstahl, 15 Schaden, Ansturm und Hellebardenspirale) und &6The Annihilator&r (2 Cursium, 1 Schwarzstahl, hohe kritische Treffer, aufladbar).",
              "",
              "Die &6Cursium-Rüstung&r braucht Netheritrüstung und eine Cursium-Vorlage, die kommt in Stufe 2. Der Grabstein ruft Maledictus nach einer Minute wieder.",
          ],
          tasks=[task_kill("cataclysm:maledictus", 1)],
          rewards=[reward_table("s1_uncommon"), reward_item("cataclysm:cursium_ingot", 1), reward_xp(20)],
          deps=["aptrgangr"], icon="cataclysm:cursium_ingot", size=1.5, shape="diamond"),

    # ---- Die versunkene Stadt -----------------------------------------------
    quest("city_find", 21.5, 0, "&3Finde die versunkene Stadt",
          subtitle="Ab hier wird Ausrüstung aus Stufe 2 empfohlen.",
          description=[
              "Die &6Sunken City&r liegt auf dem Grund der &eTiefsee&r (Deep Ocean, auch kalt, lauwarm und gefroren). Nimm Wasseratmung, einen &6Schnorchel&r aus den Artefakten oder einen Schildkrötenpanzer mit, und Türen zum Luftholen.",
              "",
              "Darin leben &cDeeplings&r (26 Lebenspunkte), Brutes (60), Angler, Priester und Hexer. &cPriester und Hexer&r lassen ein &6Athame&r fallen, das brauchst du für das Opfer. Der &cCoralssus&r (160 Lebenspunkte) gibt einen &6Korallenbrocken&r, der &cKorallengolem&r Korallensplitter, vier davon sind eine &6Kristallkoralle&r.",
              "",
              "Im Tempel steht der &6Altar des Amethysts&r. Lege &6Amethystkrabbenfleisch&r darauf, nach sechs Sekunden ist es gesegnet und macht dich immun gegen Dunkelheit und die Angst der Tiefe. Die &cAmethystkrabbe&r (200 Lebenspunkte) lebt im Amethystnest in den üppigen Höhlen um Y 0 und lässt 4 bis 10 Fleisch fallen.",
              "",
              "Ab Stufe 2 zeigt das &6Abgrundauge&r (Enderauge, 4 Obsidian, 4 weinender Obsidian) den Weg.",
          ],
          tasks=[task_advancement("cataclysm:find_sunken_city", "Die versunkene Stadt finden")],
          rewards=[reward_item("minecraft:nautilus_shell", 2), reward_xp(5)],
          deps=["maledictus_kill"], icon="minecraft:dark_prismarine"),

    quest("sacrifice", 24, 0, "&3Crafte das Opfer der Tiefe",
          subtitle="Neun Dinge, formlos, und der Altar des Abgrunds.",
          description=[
              "Das &6Abgrundopfer&r (Abyssal Sacrifice) craftest du formlos aus &6Nautilusschale&r, &6Athame&r, &6Kristallkoralle&r oder Korallenbrocken, &6Herz des Meeres&r, Diamantblock, Smaragdblock, Eisenblock, Goldblock und Amethystblock.",
              "",
              pic("cataclysm:abyssal_sacrifice"),
              "",
              "Leg es auf den &6Altar des Abgrunds&r in der untersten Halle der Stadt. Dann erscheint der Leviathan. Für jeden weiteren Kampf brauchst du ein neues Opfer, einen Wiederbeleber gibt es hier nicht.",
              "",
              "&eTipp:&r Das Herz des Meeres liegt in Schatzkisten, die Karte dazu bekommst du von Kartografen oder aus Schiffswracks. Gesegnetes Krabbenfleisch essen, bevor du das Opfer ablegst.",
          ],
          tasks=[task_item("cataclysm:abyssal_sacrifice", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s1_common")],
          deps=["city_find"], icon="cataclysm:abyssal_sacrifice"),

    quest("leviathan_kill", 26.5, 0, "&c&lBesiege den Leviathan",
          subtitle="400 Lebenspunkte, und nur im Wasser verwundbar.",
          description=[
              "&cThe Leviathan&r hat &e400 Lebenspunkte&r und Rüstung 10. Sein Biss macht 15 plus 10 Prozent deiner Lebenspunkte, der Abgrundstrahl 10 plus 10 Prozent, Risse und Kugeln 10 und 4. Er legt &eDunkelheit&r auf dich. Außerhalb des Wassers ist er unverwundbar, du musst zu ihm hinunter.",
              "",
              "&eSo geht es:&r Gesegnetes Krabbenfleisch gegen die Dunkelheit, Wasseratmung, Delphingunst oder Tiefenschnelle für Tempo. Bleib dicht an seinem Körper, nicht vor dem Maul. Treffer über 20 werden gekappt, 15 pro Sekunde maximal, Reichweite 38 Blöcke.",
              "",
              "&eBeute:&r &6Gezeitenklauen&r (Rechtsklick wirft einen Enterhaken, Linksklick einen Tentakel für Schaden, 8 Schaden) und ein &6Abgrundei&r. Aus dem Ei schlüpft ein kleiner Leviathan, der dir folgt und im Eimer mitkommt.",
          ],
          tasks=[task_kill("cataclysm:the_leviathan", 1)],
          rewards=[reward_table("s1_uncommon"), reward_item("minecraft:diamond", 4), reward_xp(25)],
          deps=["sacrifice"], icon="cataclysm:tidal_claws", size=1.5, shape="diamond"),

    # ---- Die alte Fabrik ------------------------------------------------------
    quest("factory_find", 13.5, 5, "&7Finde die alte Fabrik",
          subtitle="Eine Fabrik tief unter der Erde, um Y minus 30.",
          description=[
              "Die &6Ancient Factory&r liegt um &eY minus 30&r unter jedem Biom. Große Höhlen und Schluchten legen ihre Wände frei, sonst hilft ab Stufe 2 das &6Mechanische Auge&r (Enderauge, 4 Eisenbarren, 4 Redstoneblöcke).",
              "",
              "Drinnen patrouillieren &cWatcher&r (25 Lebenspunkte, 5 Schaden, lassen Eisen und Redstone fallen) und &cProwler&r (160 Lebenspunkte, Rüstung 10, 14 Schaden, Zielsuchraketen für 5 und ein Todeslaser für 5 plus 5 Prozent). Ein Prowler gibt &e5 bis 7 Eisen&r und &e5 bis 9 Redstone&r.",
              "",
              "&cAchtung:&r Die &6EMP-Blöcke&r in den Hallen schalten Redstone in der Nähe ab. Türen mit Druckplatten funktionieren dort nicht, nimm Zauntore.",
          ],
          tasks=[task_advancement("cataclysm:find_ancient_factory", "Die alte Fabrik finden")],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(5)],
          deps=["maledictus_kill"], icon="cataclysm:mech_eye"),

    quest("harbinger_kill", 16, 5, "&c&lWeck den Harbinger und zerstör ihn",
          subtitle="Ein Netherstern weckt die Maschine. Stufe 2.",
          description=[
              "Irgendwo in der Fabrik steht &cThe Harbinger&r still und wartet. Rechtsklick mit einem &6Netherstern&r weckt ihn. Der Stern kommt vom Wither, also erst in Stufe 2, wenn der Nether offen ist.",
              "",
              "Er hat &e390 Lebenspunkte&r, Rüstung 12 und fliegt. Witherraketen machen 8, Laser 5, der Todeslaser 5 plus 5 Prozent, der Ansturm 6 Prozent. Jeder Treffer heilt ihn um 5, dazu heilt er 2 von selbst. Treffer über 22 werden gekappt, 14 pro Sekunde, Reichweite 35 Blöcke. Ein Bogen lohnt sich hier.",
              "",
              "&eBeute:&r ein &6Witheritblock&r, also 9 Barren. Daraus baust du den &6Mechanischen Fusionsamboss&r (6 Witherit, 2 Redstoneblöcke, Amboss), der Bosswaffen miteinander verschmilzt, zum Beispiel den Fluchbogen mit dem Sandsturm zum &6Zorn der Wüste&r. Dazu die &6Laser-Gatling&r (2 Witherit, lädt mit Redstone nach), der &6Fleischschredder&r (2 Witherit) und die &6Wither-Schulterwaffe&r (2 Witherit, Schießpulver, Redstoneblock).",
              "",
              "Der Wiederbeleber nimmt ein &6Mechanisches Auge&r.",
          ],
          tasks=[task_kill("cataclysm:the_harbinger", 1)],
          rewards=[reward_table("s1_uncommon"), reward_item("minecraft:redstone_block", 4), reward_xp(25)],
          deps=["factory_find"], icon="cataclysm:witherite_ingot", size=1.5, shape="diamond"),

    # ---- Die Akropolis --------------------------------------------------------
    quest("acropolis_find", 21.5, 5, "&9Finde die Akropolis",
          subtitle="Eine Stadt am Himmel, in Y 200 über dem warmen Meer.",
          description=[
              "Die &6Akropolis&r schwebt in &eY 200&r über dem &ewarmen Meer&r (Biom Warm Ocean). Von unten siehst du sie bei klarem Himmel. Hinauf kommst du mit Wassereimer und Blöcken, ab Stufe 2 mit dem &6Sturmauge&r (Enderauge, 2 Diamanten, 2 Prismarinscherben, 2 Prismarinkristalle, Blitzableiter, Wassereimer).",
              "",
              "Oben leben &cUrchinkin&r (12 Lebenspunkte), &cCindaria&r (60), &cHippocamtus&r (85, Rüstung 15) und Oktopusse, die Ertrunkene steuern. Fast alle lassen &6Lacrima&r fallen. Die &cClawdian&r (225 Lebenspunkte, Rüstung 12, 16 Schaden, gekappt wie ein Boss) geben eine &6Chitinklaue&r und 5 bis 8 Lacrima.",
              "",
              "Aus 4 Lacrima, einem Goldbarren und 4 Goldnuggets wird der &6Azurblaue Seeschild&r. Für diese Gegner solltest du Ausrüstung aus Stufe 3 tragen, zum Beispiel Stahl von Silent Gear oder die Magierroben.",
          ],
          tasks=[task_advancement("cataclysm:find_acropolis", "Die Akropolis finden")],
          rewards=[reward_item("cataclysm:lacrima", 4), reward_xp(5)],
          deps=["leviathan_kill"], icon="cataclysm:azure_seastone_bricks"),

    quest("scylla_kill", 24, 5, "&c&lBesiege Scylla",
          subtitle="Die Sturmkaiserin ruft Blitze und ändert das Wetter.",
          description=[
              "&cScylla&r hat &e390 Lebenspunkte&r, Rüstung 12 und schlägt für 18. Ihr Speer macht 14, Blitzsturm 10 und 4 in der Fläche, ihre Schlangen und der Anker 16, der Wirbel 7 Prozent deiner Lebenspunkte. Sobald sie wach ist, zieht ein Gewitter auf.",
              "",
              "&eSo geht es:&r Nah dran bleiben, die Reichweitengrenze liegt bei nur 12 Blöcken. Wenn sie den Anker hebt, raus aus der Linie. Treffer über 21 werden gekappt, 13 pro Sekunde.",
              "",
              "&eBeute:&r &e8 bis 16 Lacrima&r und &e3 bis 4 Sturmessenzen&r. Zwei Essenzen und drei Lacrima ergeben &6Astrape&r (Rechtsklick schießt einen Blitzspeer, 10,5 Schaden) oder &6Ceraunus&r (ein Anker mit 16 Schaden, werfbar, schleichend Wellen in Fächerform).",
              "",
              "Der Wiederbeleber nimmt ein &6Sturmauge&r.",
          ],
          tasks=[task_kill("cataclysm:scylla", 1)],
          rewards=[reward_table("s1_uncommon"), reward_item("cataclysm:lacrima", 8), reward_xp(30)],
          deps=["acropolis_find"], icon="cataclysm:essence_of_the_storm", size=1.5, shape="diamond"),

    quest("cataclysmfarer", 27.5, 5, "&c&lFünf Bosse, fünf Siege",
          subtitle="Alle Bosse der Oberwelt sind gefallen.",
          description=[
              "Remnant, Maledictus, Leviathan, Harbinger und Scylla liegen hinter dir. Der Rest von Cataclysm wartet in anderen Welten: &cIgnis&r in der Burning Arena und die &cNetherite Monstrosity&r in der Soul Black Smith im Nether (Stufe 2), der &cEnder Guardian&r in der Ruined Citadel im End (Stufe 4).",
              "",
              "Ignis lässt &6Ignitium&r fallen, drei Barren pro Kampf, für die Ignitium-Rüstung und den Incinerator. Die Monstrosity gibt die &6Höllenschmiede&r, eine Spitzhacke, die mit Rechtsklick den Boden sprengt. Wer alle acht besiegt, ist der Cataclysmfarer.",
              "",
              "Jeder Wiederbeleber ruft seinen Boss beliebig oft zurück, mit dem passenden Auge. So kommt ihr zu mehr Witherit und Sturmessenz für die ganze Gruppe.",
          ],
          tasks=[task_checkmark("Alle fünf Bosse der Oberwelt besiegt")],
          rewards=[reward_table("s1_rare"), reward_xp(30)],
          deps=["scylla_kill", "harbinger_kill"], icon="cataclysm:music_disc_the_cataclysmfarer", size=2.0, shape="hexagon"),

    # ---- Born in Chaos ----------------------------------------------------------
    quest("bic_night", 0, 9, "&8Sammle Dunkelmetall",
          subtitle="Die Nacht gehört Born in Chaos.",
          description=[
              "Nachts kommen die Monster aus &6Born in Chaos&r: &cZombie-Schläger&r (60 Lebenspunkte, schleudern dich weg), &cSkelett-Drescher&r (50, Rüstung 10, Hammerschlag für 8 mit viel Rückstoß), &cTürritter&r (30, Rüstung 7), &cKnochenrufer&r, die kleine Skelette rufen, und &cGefallene Chaosritter&r (40 Lebenspunkte, Rüstung 20).",
              "",
              "Viele von ihnen lassen &6Dunkelmetallstücke&r fallen, der Chaosritter 4 bis 7 auf einmal. Sammle &e9 Stück&r, mehr dazu im nächsten Quest.",
              "",
              "&cAchtung:&r Ein &cGeist des Chaos&r kann in einen normalen Mob fahren und ihn besessen machen. Siehst du im Chat &c\"Something is chasing you\"&r, jagt dich ein &cNightmare Stalker&r. Zu Hause bleiben hilft nicht, er kommt.",
          ],
          tasks=[task_item("born_in_chaos_v1:pieceofdarkmetal", 9)],
          rewards=[reward_table("s1_common"), reward_xp(5)],
          deps=["welcome"], icon="born_in_chaos_v1:pieceofdarkmetal", size=1.5),

    quest("dark_metal", 2.5, 9, "&8Schmilz Dunkelmetall",
          subtitle="Neun Stücke, ein Haufen, ein Barren.",
          description=[
              "&e9 Dunkelmetallstücke&r ergeben einen &6Dunkelmetallhaufen&r, und der wird im &6Schmelzofen&r zum &6Dunkelmetallbarren&r. Einzelne Stücke werden im Schmelzofen zu Nuggets, neun Nuggets sind ein Barren.",
              "",
              "Jede Waffe braucht einen &6Knochengriff&r: Knochen, Dunkelmetallnugget und eine &6Dunkelrute&r übereinander. Dunkelruten (1 bis 2) lässt der &cDunkle Wirbel&r fallen, ein schwebender Geist mit 35 Lebenspunkten.",
              "",
              "&6Geschärftes Dunkelmetallschwert&r (2 Barren, Griff): mehr Schaden gegen Untote. &6Große Schnitteraxt&r (4 Barren, 2 Griffe): jeder Kill in Folge steigert deine Raserei, bis fünfmal. Den &6Schädelbrecher&r (Sprungangriffe betäuben) lässt nur der Skelett-Drescher fallen, und das sehr selten.",
              "",
              "Die &6Dunkelmetall-Rüstung&r braucht Netheritrüstung und eine Vorlage, die etwa jeder zwanzigste Chaosritter fallen lässt. Das ist Stufe 2.",
          ],
          tasks=[task_item("born_in_chaos_v1:dark_metal_ingot", 2)],
          rewards=[reward_item("born_in_chaos_v1:pieceofdarkmetal", 9), reward_xp(10)],
          deps=["bic_night"], icon="born_in_chaos_v1:dark_metal_ingot"),

    quest("dark_tower", 5, 8, "&8Räum den dunklen Turm",
          subtitle="Der Oberste Knochenrufer und sein Orb.",
          description=[
              "Der &6Dunkle Turm&r steht in Wäldern, Ebenen und Taigas. Drinnen: Spawner, Knochenrufer, Skelett-Drescher und ganz oben der &cOberste Knochenrufer&r (65 Lebenspunkte, dann eine zweite Form mit 60).",
              "",
              "Er lässt immer den &6Orb des Beschwörers&r fallen, dazu meist Chaossamen, etwa jeder sechste Kampf ein &6Todestotem&r (in der Hand rettet es vor dem Tod und gibt Stärke, kostet Sättigung) und etwa jeder siebte den &6Stab der magischen Pfeile&r.",
              "",
              "Mit dem Orb baust du den &6Knochenruferstab&r: 2 Dunkelmetallnuggets, der Orb, 2 Knochen, ein &6Zerbrochener Schädel&r und ein Knochengriff. Er ruft kleine Skelette, die für dich kämpfen.",
          ],
          tasks=[task_advancement("born_in_chaos_v1:dismantledto_bones", "Den Obersten Knochenrufer besiegen")],
          rewards=[reward_table("s1_uncommon"), reward_xp(15)],
          deps=["dark_metal"], icon="born_in_chaos_v1:shattered_skull"),

    quest("hounds", 5, 10, "&8Besiege den Anführer der Höllenhunde",
          subtitle="Der Hügel der Hunde in der Wüste.",
          description=[
              "Der &6Hügel der Hunde&r liegt in der Wüste. &cSchreckenshunde&r (17 Lebenspunkte, 5 Schaden) jagen im Rudel, und irgendwo dazwischen läuft der &cAnführer&r mit &e100 Lebenspunkten&r und 10 Schaden.",
              "",
              "Er lässt &e1 bis 3 Fangzähne&r fallen, dazu 3 bis 6 Monsterhaut und 4 bis 8 Monsterfleisch. Aus 4 Fangzähnen, einer schweren Druckplatte und einem Eisenbarren wird die &6Hundefalle&r, die hält Monster fest.",
              "",
              "&eTipp:&r Hunde kommen von allen Seiten. Stell dich mit dem Rücken an eine Wand, oder lass sie durch eine Tür kommen.",
          ],
          tasks=[task_kill("born_in_chaos_v1:dire_hound_leader", 1)],
          rewards=[reward_item("minecraft:cooked_beef", 8), reward_xp(10)],
          deps=["dark_metal"], icon="minecraft:bone"),

    quest("nightmare", 7.5, 8, "&8Stell dich dem Nightmare Stalker",
          subtitle="Er jagt dich. Also dreh dich um.",
          description=[
              "Der &cNightmare Stalker&r (70 Lebenspunkte, 7 Schaden, schnell und schwer wegzustoßen) sucht sich einen Spieler aus und verfolgt ihn. Kämpf bei Licht und mit dem Rücken zur Wand, er greift von hinten an.",
              "",
              "Er lässt eine &6Albtraumklaue&r fallen, dazu Monsterhaut oder Dunkelmetall, und etwa jeder elfte seinen &6Schädel&r. Zwei Klauen, ein Dunkelmetallbarren und ein Knochengriff ergeben die &6Albtraumsense&r: Angriffe heilen dich, verdorren das Ziel und sperren seine Magie.",
              "",
              "Aus Monsterhaut und Dunkelmetall wird die &6Albtraumrüstung&r (Robe: 2 Barren und 6 Haut), die Maske braucht den Schädel. Im Dunkeln läufst du damit schneller, und dunkle Waffen werden stärker.",
          ],
          tasks=[task_kill("born_in_chaos_v1:nightmare_stalker", 1)],
          rewards=[reward_item("born_in_chaos_v1:monster_skin", 4), reward_xp(15)],
          deps=["dark_metal"], icon="minecraft:leather"),

    quest("lifestealer", 7.5, 10, "&8Besiege den Lifestealer",
          subtitle="Ein Mantel, darunter etwas anderes.",
          description=[
              "Der &cLifestealer&r hat &e100 Lebenspunkte&r und Rüstung 16. Er läuft nachts umher und zeigt sein wahres Gesicht erst im Kampf. Sein Griff saugt dir Leben ab, halt ihn mit dem Schild auf Abstand.",
              "",
              "Er lässt &e3 bis 5 Lifestealer-Knochen&r fallen, 7 bis 10 Dunkelmetallstücke und 3 bis 5 &6Chaossamen&r. Zwei Knochen und ein &6Knochenherz&r (4 Knochen um einen verschmolzenen Knochen) ergeben das &6Dunkle Atrium&r: eine Stunde &eDunkler Schutz&r, der dich einmal vor dem Tod rettet.",
              "",
              "Chaossamen brauchst du auch für das Todestotem und um die Dunkelmetall-Vorlage zu vervielfachen.",
          ],
          tasks=[task_advancement("born_in_chaos_v1:horror_underthe_mantle", "Den Lifestealer besiegen")],
          rewards=[reward_table("s1_uncommon"), reward_xp(15)],
          deps=["dark_metal"], icon="born_in_chaos_v1:great_reaper_axe"),

    # ---- Weitere Gefahren -------------------------------------------------------
    quest("wroughtnaut", -3, 9, "&7Besiege den Ferrous Wroughtnaut",
          subtitle="Eine Rüstung ohne Lücke, außer am Rücken.",
          description=[
              "Der &cFerrous Wroughtnaut&r aus &6Mowzie's Mobs&r steht in einer Kammer unter der Erde und wacht erst auf, wenn du nah kommst. Von vorn prallt alles ab. Weich seiner Axt aus und schlag in den &eRücken&r, am besten wenn die Axt im Boden steckt.",
              "",
              "Er hat nur &e40 Lebenspunkte&r, trifft aber für 30. Ein Fehler kostet dich mit Eisenrüstung fast alles, mit Diamant die Hälfte. Goldapfel vorher essen.",
              "",
              "&eBeute:&r &6Wrought Helm&r (unzerstörbar) und die &6Axt der tausend Metalle&r: unzerstörbar, Rechtsklick schlägt im Bogen, schleichend rammst du sie in den Boden für eine Stoßwelle.",
          ],
          tasks=[task_kill("mowziesmobs:ferrous_wroughtnaut", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(20)],
          deps=["welcome"], icon="mowziesmobs:wrought_helmet"),

    quest("frostmaw", -3, 11.5, "&bJag den Frostmaw",
          subtitle="Oder stiehl ihm den Kristall im Schlaf.",
          description=[
              "Der &cFrostmaw&r schläft in offenen Schneegebieten, nicht in Wald oder Taiga. Er hat &e250 Lebenspunkte&r, schlägt für 10 und friert dich mit seinem Atem ein. Wach wird er, wenn du zu nah kommst, oder wenn du ihn angreifst.",
              "",
              "Du hast zwei Wege: Schleich dich im Schlaf heran und nimm den &6Eiskristall&r aus seiner Pranke, oder kämpf, mit Abstand zu seinem Eisatem und zu mehreren.",
              "",
              "Der &6Eiskristall&r schleudert mit gehaltenem Rechtsklick einen eisigen Wirbelsturm und lädt sich im Inventar wieder auf. Weitere Bosse von Mowzie: &cUmvuthi&r, der Sonnenvogel (150 Lebenspunkte) im Hain der Umvuthana in der Savanne, und &cTongbi&r, der Bildhauer (140), in seinem Kloster auf den Berggipfeln.",
          ],
          tasks=[task_kill("mowziesmobs:frostmaw", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(20)],
          deps=["wroughtnaut"], icon="mowziesmobs:ice_crystal"),
]

images = [
    banner("bosses/title", "Bosse der Oberwelt", 13, -5.6, height=1.8, kind="title", colour="fire"),
    banner("bosses/prep", "Vorbereitung", 1.2, -3, height=0.9, colour="stone"),
    banner("bosses/pyramid", "Die verfluchte Pyramide", 8, -3, height=0.9, colour="brass"),
    banner("bosses/prison", "Das frostige Gefängnis", 16, -3, height=0.9, colour="water"),
    banner("bosses/city", "Die versunkene Stadt", 24, -3, height=0.9, colour="water"),
    banner("bosses/factory", "Die alte Fabrik", 14.75, 3, height=0.9, colour="stone"),
    banner("bosses/acropolis", "Die Akropolis", 22.75, 3, height=0.9, colour="magic"),
    banner("bosses/chaos", "Born in Chaos", 3.75, 7, height=0.9, colour="end"),
    banner("bosses/others", "Weitere Gefahren", -3, 7, height=0.9, colour="stone"),
]

chapter(C, "Bosse der Oberwelt", "cataclysm:ancient_remnant_spawn_egg", "world", quests, shape="circle", order=57, stage=1,
        subtitle=["Stufe 1. Cataclysm, Born in Chaos und Mowzie's Mobs in der Oberwelt, in der Reihenfolge, in der man sie schafft."],
        images=images)
