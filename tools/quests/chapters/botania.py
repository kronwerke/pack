"""Botania in stage 1: petals, the Pure Daisy, living blocks, the Petal Apothecary, the two open
generating flowers (Endoflame, Hydroangeas) with their numbers from the flower classes, spreaders,
pools, detector and void, mana infusion (managlass, powder, string, manaweave, diamonds, seeds),
the functional flowers without runes and the first automated farm. Manasteel, mana pearls, the
mana tablet and the runic altar are stage 2 and live in botania_runes.py. infused_iron and
manasteel_prep collect the stage 1 inputs of the Nature's Aura manasteel ritual
(kubejs/server_scripts/kronwerke/magic.js)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "botania"


def block_img(name, size=32):
    """A flower or block picture from Botania's block textures."""
    return img(f"botania:textures/block/{name}.png", size, size)


quests = [
    # ---- Erste Blueten ----------------------------------------------------
    quest("welcome", 0, 0, "&aCrafte die Lexica Botania",
          subtitle="Das Handbuch für alles, was hier wächst.",
          description=[
              "Ein &6Buch&r und ein beliebiger &6Setzling&r, formlos an der Werkbank, ergeben die &6Lexica Botania&r.",
              "",
              img(item_texture("botania:lexica_botania"), 32, 32),
              "",
              "&aBotania&r ist Technik aus Pflanzen: Blumen machen &dMana&r, &6Manaverbreiter&r schießen es durch die Luft, &6Manabecken&r speichern es und verwandeln Dinge, die du hineinwirfst.",
              "",
              "&eTipp:&r Schleich und klick mit der Lexica auf einen Botania-Block, dann springt sie zum passenden Eintrag.",
              "",
              "&eKronwerke:&r Hier geht es bis zum Manabecken. Runenaltar, Manastahl und Terrastahl öffnen mit &6Stufe 2&r, weiter im Kapitel &aBotania: Runen&r.",
          ],
          tasks=[task_item("botania:lexica_botania", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_table("s1_common")],
          icon="botania:lexica_botania", size=2.0, shape="hexagon"),

    quest("petals", 2.5, 0, "&6Pflück Mystische Blumen",
          subtitle="Sechzehn Farben, zwei Blätter pro Blume.",
          description=[
              "Mystische Blumen wachsen in fast allen Grasbiomen, du erkennst sie an den Funken. Eine Blume gibt an der Werkbank &e2 Blütenblätter&r, eine hohe &e4&r.",
              "",
              img(item_texture("botania:white_mystical_petal"), 32, 32),
              "",
              "Fast jedes Rezept in Botania ist eine Liste von Blütenblättern. Weiß brauchst du sofort, Braun, Rot und Hellgrau kurz danach.",
              "",
              "&eTipp:&r Ein Blütenblatt mit Rechtsklick auf Gras, dann Knochenmehl darauf, lässt eine hohe Blume genau dieser Farbe wachsen.",
          ],
          tasks=[task_item("botania:white_mystical_petal", 8, title="Weiße Blütenblätter")],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["welcome"], icon="botania:white_mystical_petal"),

    quest("fertilizer", 1.2, 2.2, "&6Misch Blumendünger",
          subtitle="Neue Blumen, wo du willst.",
          description=[
              "&e1 Knochenmehl&r und &e4 beliebige Farbstoffe&r, formlos, ergeben &6Blumendünger&r. Rechtsklick damit auf Gras lässt ringsum Mystische Blumen in zufälligen Farben sprießen.",
              "",
              "&eTipp:&r Leg neben der Basis ein Beet an und dünge es regelmäßig, dann musst du nicht mehr suchen.",
          ],
          tasks=[task_item("botania:floral_fertilizer", 4)],
          rewards=[reward_item("minecraft:bone_meal", 32)],
          deps=["petals"], optional=True),

    quest("pouch", 3.0, 2.2, "&6Näh einen Blumenbeutel",
          subtitle="Alle Farben in einem Inventarplatz.",
          description=[
              "&e5 Wolle&r und &e1 Blütenblatt&r ergeben den &6Blumenbeutel&r. Er hält von jeder Farbe einen Stapel Mystischer Blumen und sammelt neue automatisch ein.",
              "",
              "In der Haupthand sammelt er nichts. Schleich-Rechtsklick auf eine Truhe leert ihn hinein.",
          ],
          tasks=[task_item("botania:flower_pouch", 1)],
          rewards=[reward_xp(3)],
          deps=["petals"], optional=True),

    quest("mushrooms", 4.8, 2.2, "&6Färbe einen Pilz",
          subtitle="Ein Pilz, der als Blütenblatt zählt.",
          description=[
              "Rechtsklick mit &eFarbstoff&r auf einen braunen oder roten &6Pilz&r macht daraus einen &6Schillernden Pilz&r in dieser Farbe. Er zählt in jedem Rezept als Blütenblatt der gleichen Farbe.",
              "",
              "Tief unter der Erde findest du sie manchmal auch in kleinen Flecken.",
          ],
          tasks=[task_item("botania:white_shimmering_mushroom", 1)],
          rewards=[reward_item("minecraft:white_dye", 8)],
          deps=["petals"], optional=True, icon="botania:white_shimmering_mushroom"),

    quest("apothecary", 5, 0, "&aBau eine Blütenapotheke",
          subtitle="Hier entstehen alle besonderen Blumen.",
          description=[
              "&e6 Bruchstein&r und &e1 Blütenblatt&r ergeben die &aBlütenapotheke&r. Füll sie mit &bWasser&r, wirf die Blütenblätter des Rezepts hinein (Taste Q) und zum Schluss einen &6Samen&r. Die Blume springt heraus.",
              "",
              "Rechtsklick mit leerer Hand holt das zuletzt eingeworfene Teil zurück. Welche Blume welche Blätter braucht, zeigen Lexica und JEI.",
              "",
              "&eTipp:&r Bis zu 20 Sekunden nach einer fertigen Blume holt ein Rechtsklick mit leerer Hand (Wasser vorher nachfüllen) dieselben Zutaten aus deinem Inventar.",
              "",
              "&cAchtung:&r Mit Lava gefüllt vernichtet sie alles, was hineinfällt.",
          ],
          tasks=[task_item("botania:petal_apothecary", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 16), reward_item("minecraft:water_bucket", 1)],
          deps=["petals"], icon="botania:petal_apothecary", size=1.5, shape="square"),

    quest("pure_daisy", 7.5, 0, "&aPflanz ein Reines Gänseblümchen",
          subtitle="Ohne diese Blume geht in Botania nichts.",
          description=[
              "&e4 weiße Blütenblätter&r in der Apotheke. Pflanz es und stell Blöcke auf die &e8 Felder rundherum&r, auf derselben Höhe. Nach rund einer Minute ist alles verwandelt.",
              "",
              block_img("pure_daisy"),
              "",
              "&6Stein&r wird zu &6Lebestein&r, jeder &6Holzstamm&r zu einem &6Lebeholzstamm&r.",
              "",
              "&cAchtung:&r Es muss Stein sein, kein Bruchstein. Brenn Bruchstein im Ofen. Bau gleich zwei oder drei Gänseblümchen, du brauchst Unmengen von beidem.",
          ],
          tasks=[task_item("botania:pure_daisy", 1)],
          rewards=[reward_item("minecraft:stone", 32), reward_item("minecraft:oak_log", 16)],
          deps=["apothecary"], icon="botania:pure_daisy", size=2.0, shape="hexagon"),

    quest("daisy_more", 7.5, 2.4, "&6Reinige Tropfstein zu Calcit",
          subtitle="Das Gänseblümchen kann mehr als Lebestein.",
          description=[
              "Stell &6Tropfsteinblöcke&r um das Reine Gänseblümchen, sie werden zu &6Calcit&r.",
              "",
              "Was es sonst noch umwandelt: Eis zu Packeis, Packeis zu Blaueis, eine Wasserquelle zu Schnee, Netherrack zu Bruchstein, Seelensand zu Sand. Die beiden Nether-Blöcke gibt es ab Stufe 2.",
          ],
          tasks=[task_item("minecraft:calcite", 8)],
          rewards=[reward_item("minecraft:ice", 8)],
          deps=["pure_daisy"], optional=True, icon="minecraft:calcite"),

    quest("livingwood", 10, -1.2, "&6Sammle Lebeholz",
          subtitle="Holz, das Mana leiten kann.",
          description=[
              "Jeder Stamm am Gänseblümchen wird zum &6Lebeholzstamm&r. Jede Holzsorte geht, auch aus anderen Mods.",
              "",
              "Daraus baust du Manaverbreiter (6 Stämme), Zweige und die Bretter der Offenen Kiste. In Stufe 3 braucht das Elfenportal noch einmal acht Stämme, leg also Vorrat an.",
          ],
          tasks=[task_item("botania:livingwood_log", 16)],
          rewards=[reward_item("minecraft:oak_log", 32)],
          deps=["pure_daisy"], icon="botania:livingwood_log"),

    quest("livingrock", 10, 1.2, "&6Sammle Lebestein",
          subtitle="Der Stein für Becken und Altäre.",
          description=[
              "Stein am Gänseblümchen wird zu &6Lebestein&r. Du brauchst &e5&r für jedes Manabecken, &e4&r für den Runenaltar in Stufe 2, &e8&r für jede Manatafel.",
              "",
              "&eTipp:&r Mehrere Gänseblümchen nebeneinander, jedes mit eigenem Ring aus acht Steinen, vervielfachen die Ausbeute.",
          ],
          tasks=[task_item("botania:livingrock", 32)],
          rewards=[reward_item("minecraft:stone", 64), reward_table("s1_common")],
          deps=["pure_daisy"], icon="botania:livingrock"),

    quest("twig", 12.5, -1.2, "&6Schnitz Lebeholzzweige",
          subtitle="Zwei Stämme, ein Zweig.",
          description=[
              "&e2 Lebeholzstämme&r übereinander ergeben einen &6Lebeholzzweig&r.",
              "",
              "Zweige stecken im Stab des Waldes (3), im Lebeholzbogen (3), in jedem Manastahl-Werkzeug und zwei davon in jedem Ritual für Manastahl.",
          ],
          tasks=[task_item("botania:livingwood_twig", 6)],
          rewards=[reward_item("botania:livingwood_log", 8)],
          deps=["livingwood"], icon="botania:livingwood_twig"),

    quest("wand", 15, -1.2, "&aBau den Stab des Waldes",
          subtitle="Verbindet, dreht und misst alles in Botania.",
          description=[
              "&e3 Lebeholzzweige&r und &e2 Blütenblätter&r schräg im Crafting-Feld. Die Farben der Blätter färben den Stab.",
              "",
              img(item_texture("botania:wand_of_the_forest"), 32, 32),
              "",
              "Schleich-Rechtsklick in die Luft wechselt den Modus. &eBindemodus:&r Schleich-Klick auf einen Verbreiter, dann auf das Ziel. &eFunktionsmodus:&r Schleich-Klick dreht einen Verbreiter zur angeklickten Seite.",
              "",
              "Mit dem Stab in der Hand siehst du das Mana in Blumen, Verbreitern und Becken und die Zielstrahlen der Verbreiter.",
          ],
          tasks=[task_item("botania:wand_of_the_forest", 1)],
          rewards=[reward_item("botania:livingwood_log", 8), reward_xp(5)],
          deps=["twig"], icon="botania:wand_of_the_forest", size=1.5, shape="square"),

    quest("deco", 12.5, 1.2, "&7Bau mit Lebestein",
          subtitle="Magie darf auch gut aussehen.",
          description=[
              "Werkbank oder Steinschneider machen aus Lebestein &6Lebesteinziegel&r, polierte und bemooste Varianten, Stufen, Treppen und Mauern.",
              "",
              "Ein Garten aus hellem Lebestein mit leuchtenden Blumen dazwischen ist schnell das schönste Gebäude auf dem Server.",
          ],
          tasks=[task_item("botania:livingrock_bricks", 16)],
          rewards=[reward_item("botania:livingrock", 16)],
          deps=["livingrock"], optional=True),

    # ---- Mana erzeugen ----------------------------------------------------
    quest("gen_intro", 0, 6.5, "&aVersteh erzeugende Blumen",
          subtitle="Mana kommt aus Blumen, nicht aus Kabeln.",
          description=[
              "Erzeugende Blumen verbrauchen etwas und machen daraus &dMana&r. Sie geben es an den nächsten &6Manaverbreiter&r weiter, an den sie sich beim Pflanzen selbst binden.",
              "",
              "In Stufe 1 sind zwei offen, alle anderen brauchen Runen:",
              "&6Endoflamme&r: verbrennt Brennstoff, 1 200 Mana pro Kohle.",
              "&6Hydroangea&r: trinkt Wasser, rund 13 Mana pro Block, verwelkt nach einer Stunde.",
              "",
              "Die übrigen zwölf Blumen mit ihren Zahlen stehen im Kapitel &aBotania: Runen&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["wand"], icon="botania:endoflame"),

    quest("endoflame", 2.5, 6.5, "&6Pflanz eine Endoflamme",
          subtitle="Kohle rein, Mana raus.",
          description=[
              "Apotheke: &e2 braune&r, &e1 rotes&r, &e1 hellgraues&r Blütenblatt. Wirf Brennstoff in bis zu &e3 Blöcken&r Abstand auf den Boden, sie saugt ihn auf.",
              "",
              block_img("endoflame"),
              "",
              "Ein Stück brennt halb so lange wie im Ofen und gibt dabei &d3 Mana alle 2 Ticks&r, also 30 Mana pro Sekunde. Danach 2 Sekunden Pause. Ihr Puffer fasst 300 Mana, ist er voll, frisst sie nichts Neues.",
          ],
          tasks=[task_item("botania:endoflame", 1)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["gen_intro"], icon="botania:endoflame", size=1.5, shape="square"),

    quest("endo_fuel", 2.5, 8.7, "&6Füttere die Endoflamme",
          subtitle="Was welcher Brennstoff bringt.",
          description=[
              "Verbrenn &e32 Holzkohle&r. Holzkohle aus Baumfarm und Ofen ist der Brennstoff, der nie ausgeht.",
              "",
              "&eMana pro Stück:&r Kohle oder Holzkohle 1 200 (40 s). Kohleblock 12 000. Getrockneter Seetangblock 3 000. Stamm oder Bretter 225. Stock 75. Lohenrute 1 800 (ab Stufe 2).",
              "",
              "&cNicht:&r Lavaeimer und alles, was im Ofen etwas zurücklässt. Mehr als zwei Kohleblöcke Brennzeit auf einmal verfällt.",
          ],
          tasks=[task_item("minecraft:charcoal", 32)],
          rewards=[reward_item("minecraft:coal_block", 2)],
          deps=["endoflame"], icon="minecraft:charcoal"),

    quest("hydroangeas", 0, 8.7, "&6Pflanz eine Hydroangea",
          subtitle="Trinkt Wasser und macht daraus Mana.",
          description=[
              "Apotheke: &e2 blaue&r und &e2 türkise&r Blütenblätter. Pflanz sie in die Mitte und füll die acht Felder rundherum mit Wasserquellen, auf ihrer Höhe.",
              "",
              block_img("hydroangeas"),
              "",
              "Jeder Block gibt rund &d13 Mana&r, bei Regen 20, das Wasser fließt sofort nach. Nach &c72 000 Ticks&r (eine Stunde, drei Minecraft-Tage) verwelkt sie zu einem toten Busch.",
          ],
          tasks=[task_item("botania:hydroangeas", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_item("botania:blue_mystical_petal", 4)],
          deps=["gen_intro"], optional=True),

    quest("spreader", 5, 6.5, "&aStell einen Manaverbreiter auf",
          subtitle="Schießt Mana von A nach B.",
          description=[
              "&e6 Lebeholzstämme&r, &e1 Kupferblech&r aus der Create-Presse und &e1 Blütenblatt&r. Stell ihn höchstens 6 Blöcke von deinen Blumen auf und verbinde ihn mit dem Stab (Bindemodus) mit seinem Ziel.",
              "",
              "Er feuert, solange das Ziel Mana aufnimmt, ein neuer Stoß erst, wenn der letzte angekommen ist. Lange Wege kosten Mana, die Funken im Zielstrahl zeigen, wo der Verlust beginnt.",
              "",
              "&eTipp:&r Redstone hält ihn an. Rechtsklick mit Wolle dämpft das Geräusch, mit Gerüst bekommt er einen Rahmen, an dem Hebel halten.",
          ],
          tasks=[task_item("botania:mana_spreader", 1)],
          rewards=[reward_item("botania:livingwood_log", 8), reward_item("minecraft:copper_ingot", 4)],
          deps=["endoflame"], icon="botania:mana_spreader", size=1.75, shape="square"),

    quest("open_crate", 5, 8.7, "&6Bau eine Offene Kiste",
          subtitle="Eine Kiste mit Loch im Boden.",
          description=[
              "&e7 Lebeholzbretter&r in U-Form. Was ein Trichter hineinschiebt, fällt direkt darunter auf den Boden.",
              "",
              "Stell sie zwei Blöcke hoch neben die Endoflammen, Truhe und Trichter darüber.",
          ],
          tasks=[task_item("botania:open_crate", 1)],
          rewards=[reward_item("minecraft:hopper", 1), reward_item("minecraft:coal", 16)],
          deps=["spreader"]),

    quest("endo_auto", 7.2, 8.7, "&6Automatisiere die Kohle",
          subtitle="Die Endoflamme füttert sich selbst.",
          description=[
              "Truhe, Trichter, Offene Kiste über den Endoflammen. Eine &6Druckplatte&r unter der Abwurfstelle sperrt den Trichter, solange noch Kohle liegt, so fällt nie zu viel.",
              "",
              "Items auf dem Boden verschwinden nach fünf Minuten. Ein Create-Förderband, das über dem Beet endet, geht genauso.",
          ],
          tasks=[task_checkmark("Die Kohle fällt von selbst")],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["open_crate"], icon="minecraft:hopper"),

    # ---- Mana speichern ---------------------------------------------------
    quest("pool", 9, 6.5, "&aBau ein Manabecken",
          subtitle="Eine Million Mana an einem Ort.",
          description=[
              "&e5 Lebestein&r in U-Form. Richte den Verbreiter mit dem Stab darauf, die Blumen füllen es bis &d1 000 000 Mana&r.",
              "",
              "Wirf passende Dinge hinein, dann verwandelt das Becken sie (&eManainfusion&r). Funktionsblumen in bis zu 10 Blöcken zapfen es an, ein Verbreiter direkt daneben füllt sich daraus.",
              "",
              "&eTipp:&r Rechtsklick mit einem Blütenblatt färbt es, ein Tonklumpen wäscht die Farbe ab. Ein Komparator gibt den Füllstand aus.",
          ],
          tasks=[task_item("botania:mana_pool", 1)],
          rewards=[reward_item("botania:livingrock", 16), reward_table("s1_uncommon")],
          deps=["spreader"], icon="botania:mana_pool", size=2.5, shape="hexagon"),

    quest("diluted_pool", 9, 9.3, "&6Bau ein Verdünntes Becken",
          subtitle="Klein, billig, schnell voll.",
          description=[
              "&e5 Lebesteinstufen&r ergeben ein &6Verdünntes Manabecken&r mit &d10 000 Mana&r, einem Hundertstel.",
              "",
              "Gut als Puffer neben einer einzelnen Funktionsblume. Wo die Lexica von Manabecken spricht, ist immer das große gemeint.",
          ],
          tasks=[task_item("botania:diluted_mana_pool", 1)],
          rewards=[reward_xp(3)],
          deps=["pool"], optional=True),

    quest("manastar", 11.5, 7.7, "&6Pflanz einen Manastern",
          subtitle="Gewinn oder Verlust auf einen Blick.",
          description=[
              "Apotheke: je &e1 hellblaues, grünes, rotes und türkises&r Blütenblatt. Pflanz ihn direkt neben ein Becken.",
              "",
              "&bBlau&r: es kommt mehr herein als hinaus. &cRot&r: das Becken verliert. Der Balken des Stabs ist bei großen Becken zu grob, der Stern nicht.",
          ],
          tasks=[task_item("botania:manastar", 1)],
          rewards=[reward_item("botania:light_blue_mystical_petal", 4), reward_xp(3)],
          deps=["pool"], icon="botania:manastar"),

    quest("pulse_spreader", 11.5, 5.4, "&6Bau einen Impuls-Verbreiter",
          subtitle="Feuert nur auf Kommando.",
          description=[
              "Manaverbreiter plus &e1 Redstone&r. Er feuert bei jedem &eRedstone-Impuls&r einen Stoß, auch ohne Ziel.",
              "",
              "Mit den Manalinsen aus Stufe 2 wird er zum Werkzeug, das Blöcke abbaut oder Gegenstände schiebt.",
          ],
          tasks=[task_item("botania:pulse_mana_spreader", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["pool"], optional=True),

    quest("turntable", 13.7, 5.4, "&6Bau eine Verbreiter-Drehscheibe",
          subtitle="Ein Verbreiter, der sich dreht.",
          description=[
              "&e8 Lebeholzstämme&r um einen &eKlebrigen Kolben&r. Ein Verbreiter darauf dreht sich und verteilt seine Stöße reihum.",
              "",
              "Redstone hält sie an. Rechtsklick mit dem Stab ändert das Tempo, Schleich-Rechtsklick die Richtung.",
          ],
          tasks=[task_item("botania:spreader_turntable", 1)],
          rewards=[reward_xp(3)],
          deps=["pulse_spreader"], optional=True),

    quest("detector", 13.7, 7.7, "&6Bau einen Manasensor",
          subtitle="Redstone, wenn ein Stoß vorbeifliegt.",
          description=[
              "&e4 Redstone&r, &e4 Lebestein&r und eine &eZielscheibe&r. Stöße fliegen durch den Sensor wie durch Luft, und er gibt dabei ein Redstone-Signal.",
              "",
              "So merkst du, ob eine Leitung überhaupt Mana trägt, oder zählst Stöße mit einem Zähler.",
          ],
          tasks=[task_item("botania:mana_detector", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["manastar"], optional=True),

    quest("mana_void", 11.5, 9.9, "&6Bau eine Manaleere",
          subtitle="Ein Grab für überschüssiges Mana.",
          description=[
              "&e6 Lebestein&r und &e2 Obsidian&r. Alles Mana, das hineinfließt, verschwindet.",
              "",
              "Unter einem Becken nimmt das Becken immer an und vernichtet, was nicht mehr passt. So laufen Endoflammen weiter, statt Kohle liegen zu lassen.",
              "",
              "&cAchtung:&r In Stufe 2 gehört unter das Perlenbecken ein Messinggehäuse. Nimm für die Leere ein anderes Becken.",
          ],
          tasks=[task_item("botania:mana_void", 1)],
          rewards=[reward_item("minecraft:obsidian", 4)],
          deps=["pool"], optional=True),

    # ---- Mana-Infusion ----------------------------------------------------
    quest("managlass", 0, 13.5, "&6Infundiere Managlas",
          subtitle="Deine erste Infusion.",
          description=[
              "Wirf farbloses &6Glas&r ins Becken. Jeder Block kostet &d150 Mana&r und kommt als &6Managlas&r zurück.",
              "",
              "So geht jede Infusion: Gegenstand hinein, solange genug Mana da ist, wird Stück für Stück verwandelt. JEI zeigt unter dem Manabecken alle Rezepte mit Preis.",
              "",
              "Managlas brauchst du für Phiolen der Brauerei und als Tauschware für Alfheim in Stufe 3.",
          ],
          tasks=[task_item("botania:managlass", 8)],
          rewards=[reward_item("minecraft:glass", 32)],
          deps=["pool"], icon="botania:managlass", size=1.5, shape="square"),

    quest("mana_powder", 2.5, 13.5, "&6Mach Manapuder",
          subtitle="Staub, der nach Magie riecht.",
          description=[
              "&eFarbstoff&r (400 Mana) oder &eSchwarzpulver&r, &eRedstone&r, &eZucker&r (je 500 Mana) im Becken werden zu &6Manapuder&r.",
              "",
              "In Stufe 2 steckt in jeder der vier Elementarrunen ein Puder. Übrige Blütenblätter werden Farbstoff, Farbstoff wird Puder.",
          ],
          tasks=[task_item("botania:mana_powder", 16)],
          rewards=[reward_item("minecraft:sugar_cane", 16)],
          deps=["managlass"]),

    quest("petal_pouch", 2.5, 15.7, "&6Näh einen Blütenblattbeutel",
          subtitle="Blumen rein, Blätter raus.",
          description=[
              "Wie der Blumenbeutel, nur mit &e1 Manapuder&r in der Mitte: 5 Wolle, 1 Blütenblatt, 1 Puder.",
              "",
              "Er zerlegt eingesammelte Mystische Blumen sofort in Blütenblätter und hält auch Schillernde Pilze. Schleich-Rechtsklick schaltet das Einsammeln an und aus.",
          ],
          tasks=[task_item("botania:petal_pouch", 1)],
          rewards=[reward_xp(3)],
          deps=["mana_powder"], optional=True),

    quest("mana_string", 0, 15.7, "&6Infundiere Faden",
          subtitle="Faden, der Magie trägt.",
          description=[
              "Ein &6Faden&r im Becken wird für &d1 250 Mana&r zum &6Manainfundierten Faden&r.",
              "",
              "Daraus entstehen Managewebestoff, der Lebeholzbogen und in Stufe 2 drei Amulette. Eine Spinnenfarm liefert Nachschub.",
          ],
          tasks=[task_item("botania:mana_string", 8)],
          rewards=[reward_item("minecraft:string", 16)],
          deps=["managlass"]),

    quest("manaweave", 0, 17.9, "&6Web Managewebestoff",
          subtitle="Vier Fäden, ein Tuch.",
          description=[
              "&e4 Manainfundierte Fäden&r im Quadrat ergeben &6Managewebestoff&r.",
              "",
              "Das Tuch ist der Stoff der Magierrobe. Für die volle Robe brauchst du gut zwei Dutzend, also gut hundert Fäden.",
          ],
          tasks=[task_item("botania:manaweave_cloth", 4)],
          rewards=[reward_item("minecraft:string", 32)],
          deps=["mana_string"], optional=True),

    quest("manaweave_robe", 2.2, 17.9, "&6Schneider die Magierrobe",
          subtitle="Wenig Schutz, viel Rabatt.",
          description=[
              "Kapuze aus &e5&r, Robenoberteil aus &e8&r Managewebestoff, Hose und Stiefel genauso wie bei Leder.",
              "",
              "Schützt wenig, aber mit allen vier Teilen kosten Werkzeuge und Ruten von Botania viel weniger Mana und die Ruten werden stärker. Sie repariert sich mit Mana aus deinem Inventar, sobald du ab Stufe 2 eine Manatafel trägst.",
          ],
          tasks=[task_item("botania:manaweave_chestplate", 1)],
          rewards=[reward_xp(5)],
          deps=["manaweave"], optional=True),

    quest("livingwood_bow", -2.2, 15.7, "&6Spann einen Lebeholzbogen",
          subtitle="Ein Bogen aus lebendem Holz.",
          description=[
              "&e3 Lebeholzzweige&r und &e3 Manainfundierte Fäden&r.",
              "",
              "Hält länger als ein normaler Bogen und repariert sich mit Mana, sobald du ab Stufe 2 eine Manatafel bei dir trägst.",
          ],
          tasks=[task_item("botania:livingwood_bow", 1)],
          rewards=[reward_item("minecraft:arrow", 32)],
          deps=["mana_string"], optional=True),

    quest("mana_diamond", 5, 13.5, "&bInfundiere einen Manadiamanten",
          subtitle="10 000 Mana in einem Stein.",
          description=[
              "Ein &6Diamant&r im Becken wird für &d10 000 Mana&r zum &bManadiamanten&r. Ein Diamantblock wird für 90 000 Mana zum Manadiamantblock.",
              "",
              "&eKronwerke:&r Zwei stecken in jedem &6Quellschlussstein&r, dem Magie-Meilenstein von Stufe 1. In Stufe 2 braucht ihn das Manastahl-Ritual, jede Terrastahl-Herstellung und jede Sündenrune gleich zwei.",
              "",
              "&cDenk voraus:&r Stufe 2 will 50 Terrastahl und 8 Runenkerne, das sind rund 60 Manadiamanten. Spar dir Diamanten.",
          ],
          tasks=[task_item("botania:mana_diamond", 2)],
          rewards=[reward_item("minecraft:diamond", 2), reward_table("s1_uncommon")],
          deps=["managlass"], icon="botania:mana_diamond", size=1.5, shape="diamond"),

    quest("tiny_potato", 5, 15.7, "&6Infundiere eine Kartoffel",
          subtitle="Sie glaubt an dich.",
          description=[
              "Eine &6Kartoffel&r im Becken wird für &d1 337 Mana&r zur &6Winzigen Kartoffel&r.",
              "",
              "Sie tut nichts. Rechtsklick streichelt sie, im Amboss bekommt sie einen Namen. Jeder Botaniker braucht eine.",
          ],
          tasks=[task_item("botania:tiny_potato", 1)],
          rewards=[reward_item("minecraft:baked_potato", 8)],
          deps=["mana_diamond"], optional=True),

    quest("pasture_seeds", 7.4, 13.5, "&6Infundiere Weidesamen",
          subtitle="Gras, wo du es haben willst.",
          description=[
              "&6Kurzes Gras&r im Becken wird für &d2 500 Mana&r zu &6Weidesamen&r. Rechtsklick auf Erde, per Hand oder Werfer, lässt ringsum Gras wachsen.",
              "",
              "Blumendünger wirkt nur auf Gras, so legst du ein Beet auf nackter Erde an.",
          ],
          tasks=[task_item("botania:pasture_seeds", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["mana_diamond"], optional=True),

    quest("boreal_seeds", 7.4, 15.7, "&6Infundiere Boreale Samen",
          subtitle="Podsol und Myzel auf Bestellung.",
          description=[
              "&6Toter Busch&r für &d2 500 Mana&r ergibt &6Boreale Samen&r (Podsol), ein &6Pilz&r für &d6 500 Mana&r &6Seuchensporen&r (Myzel).",
              "",
              "&eWozu:&r Eine Blume auf Podsol greift Items auf dem Boden etwas später, auf Myzel noch später. So bestimmst du, welche Blume zuerst zugreift.",
          ],
          tasks=[task_item("botania:boreal_seeds", 1)],
          rewards=[reward_item("minecraft:dead_bush", 4)],
          deps=["pasture_seeds"], optional=True),

    # ---- Funktionsblumen --------------------------------------------------
    quest("func_intro", 11.5, 13.5, "&aVersteh Funktionsblumen",
          subtitle="Blumen, die Mana verbrauchen und arbeiten.",
          description=[
              "Funktionsblumen ziehen Mana aus dem nächsten &6Manabecken&r in bis zu &e10 Blöcken&r. Ein Verbreiter kann sie nicht direkt versorgen.",
              "",
              "Ohne Runen offen sind &6Tolldorn&r, &6Schreckdorn&r, &6Bergamute&r und &6Spulegnolie&r. Alle anderen stehen als Checkliste im Kapitel &aBotania: Runen&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["pool"], icon="botania:bellethorne"),

    quest("redstone_root", 13.7, 13.5, "&6Crafte Redstone-Wurzeln",
          subtitle="Der Schalter für deine Blumen.",
          description=[
              "&e1 Redstone&r und &e1 Farn&r oder &e1 Kurzes Gras&r, formlos.",
              "",
              "Sie steckt in fast jeder Funktionsblume. Eine Blume mit Wurzel im Rezept ruht, solange sie ein Redstone-Signal bekommt. Gras und Farne erntest du mit der Schere.",
          ],
          tasks=[task_item("botania:redstone_root", 4)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["func_intro"], icon="botania:redstone_root"),

    quest("bellethorne", 16, 12.4, "&6Pflanz einen Tolldorn",
          subtitle="Schaden an allem außer Spielern.",
          description=[
              "Apotheke: &e3 rote&r, &e2 türkise&r Blütenblätter, &e1 Redstone-Wurzel&r.",
              "",
              block_img("bellethorne"),
              "",
              "Verletzt mit Mana ständig alle Lebewesen in der Nähe, nur keine Spieler. Unter einem Spawner tötet er ohne Waffe.",
              "",
              "&cAchtung:&r Er trifft auch Tiere und Dorfbewohner. Schalte ihn per Redstone ab, wenn nötig.",
          ],
          tasks=[task_item("botania:bellethorne", 1)],
          rewards=[reward_item("botania:red_mystical_petal", 4), reward_xp(3)],
          deps=["redstone_root"], icon="botania:bellethorne"),

    quest("dreadthorne", 16, 14.6, "&6Pflanz einen Schreckdorn",
          subtitle="Nur für ausgewachsene Tiere.",
          description=[
              "Apotheke: &e3 schwarze&r, &e2 türkise&r Blütenblätter, &e1 Redstone-Wurzel&r.",
              "",
              "Verletzt nur &eausgewachsene Tiere&r, Jungtiere bleiben. Im Gehege mit Trichter darunter liefert er Fleisch und Leder von allein. Mehr Tierfarmen im Kapitel &aFarmen&r.",
          ],
          tasks=[task_item("botania:dreadthorne", 1)],
          rewards=[reward_item("botania:black_mystical_petal", 4), reward_xp(3)],
          deps=["redstone_root"], optional=True),

    quest("bergamute", 13.7, 15.7, "&6Pflanz eine Bergamute",
          subtitle="Ruhe in der Fabrik.",
          description=[
              "Apotheke: &e1 oranges&r, &e2 grüne&r Blütenblätter, &e1 Redstone-Wurzel&r.",
              "",
              "Alle Geräusche in ihrer Nähe sind nur halb so laut, mehrere Bergamuten verstärken das. Sie braucht kein Mana. Für laute Farmen und Create-Hallen, deine Zuschauer danken es dir.",
          ],
          tasks=[task_item("botania:bergamute", 1)],
          rewards=[reward_item("botania:green_mystical_petal", 4), reward_xp(3)],
          deps=["redstone_root"], optional=True),

    quest("solegnolia", 11.5, 15.7, "&6Pflanz eine Spulegnolie",
          subtitle="Eine Zone ohne Magnet.",
          description=[
              "Apotheke: &e2 braune&r, &e1 rotes&r, &e1 blaues&r Blütenblatt, &e1 Redstone-Wurzel&r. Kein Mana nötig.",
              "",
              "In ihrer Nähe zieht der &6Ring der Magnetisierung&r (ab Stufe 2) nichts an. Pflanz sie neben die Endoflammen, dann klaut dein Ring nicht die Kohle.",
          ],
          tasks=[task_item("botania:solegnolia", 1)],
          rewards=[reward_xp(3)],
          deps=["redstone_root"], optional=True),

    quest("func_outlook", 16, 16.8, "&7Schau, was mit Runen kommt",
          subtitle="Sechzehn Funktionsblumen warten auf Stufe 2.",
          description=[
              "Mit dem Runenaltar öffnen in &6Stufe 2&r: Agrarnelke, Jaded-Amarant, Trichtermalve, Rannawurzel, Helitonie, Exoflamme, Wirrbeere, Freihut, Ostermühle, Engelsblüte, Medumone, Tigerauge, Pollidisie, Tagemorphes, Cyazinthe und Vinculotos.",
              "",
              "Jede mit Rezept und Zweck als Checkliste im Kapitel &aBotania: Runen&r. Erchidee, Blasenglöckchen und ein paar andere brauchen Feenstaub aus Alfheim, siehe &aBotania: Alfheim&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["redstone_root"], optional=True, icon="botania:agricarnation"),

    # ---- Abschluss --------------------------------------------------------
    quest("farm", 18.5, 6.5, "&a&lBau eine echte Manafarm",
          subtitle="Mana, das fließt, während du etwas anderes tust.",
          description=[
              "Mindestens &e4 Endoflammen&r, &e2 Manaverbreiter&r und ein &6Manabecken&r, gefüttert über Offene Kiste oder Förderband.",
              "",
              "&eZum Planen:&r Eine Endoflamme mit Kohle bringt im Schnitt knapp 29 Mana pro Sekunde. Ein volles Becken dauert damit fast zehn Stunden, mit zehn Endoflammen eine Stunde und gut 800 Kohle.",
              "",
              "&eTipp:&r Baumfarm mit Create-Säge plus Ofen gibt Holzkohle ohne Mine. Der Manastern am Becken zeigt, ob die Farm mithält.",
          ],
          tasks=[task_item("botania:endoflame", 4), task_item("botania:mana_spreader", 2),
                 task_item("botania:mana_pool", 1)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["pool", "manastar", "endo_auto"], icon="botania:mana_spreader", size=2.0, shape="gear"),

    quest("infused_iron", 21, 8.7, "&6Veredle Eisen am Natural Altar",
          subtitle="Infused Iron, der Rohstoff für Manastahl.",
          description=[
              "Leg einen &6Eisenbarren&r auf den &aNatural Altar&r von Nature's Aura. Für &d15 000 Aura&r wird er zu &6Infused Iron&r, ein Eisenblock für 135 000 Aura zum Infused-Iron-Block.",
              "",
              "Ein Eisenbarren im Manabecken bleibt auf Kronwerke einfach liegen. Manastahl kommt ab Stufe 2 nur aus Infused Iron.",
              "",
              "&eTipp:&r Die Eisenbiene aus dem Kapitel &aBienen&r gibt Infused Iron als Wabe.",
          ],
          tasks=[task_item("naturesaura:infused_iron", 8)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["farm"], icon="naturesaura:infused_iron"),

    quest("manasteel_prep", 23.4, 8.7, "&bLeg das Ritual des Waldes bereit",
          subtitle="Am ersten Abend von Stufe 2 Manastahl.",
          description=[
              "Sammle die Zutaten für das &aRitual des Waldes&r: &e4 Infused Iron&r, &e2 Lebeholzzweige&r, &e1 Manadiamant&r, &e1 Gold Leaf&r.",
              "",
              "Ab Stufe 2 legst du sie auf Wooden Stands (Gold Leaf auf einem Stamm) um einen &6Eichensetzling&r in einem Muster aus Gold Powder. Wächst der Baum, liegen &e4 Manastahlbarren&r in der Mitte. Wie genau, steht im Kapitel &aBotania: Runen&r.",
              "",
              "&eRezept auf Kronwerke:&r Ab Stufe 2 wird Infused Iron im Becken für 3 000 Mana zu Manastahl.",
          ],
          tasks=[task_item("naturesaura:infused_iron", 4), task_item("botania:livingwood_twig", 2),
                 task_item("botania:mana_diamond", 1), task_item("naturesaura:gold_leaf", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 4), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["infused_iron"], icon="naturesaura:infused_iron", optional=True),

    quest("outlook", 21, 6.5, "&7Schau auf Stufe 2",
          subtitle="Was hinter dem Obelisken wartet.",
          description=[
              "Mit &6Stufe 2 (Messingwerk)&r geht es im Kapitel &aBotania: Runen&r weiter: Manastahl, Manaperlen (nur mit Messinggehäuse unter dem Becken), Manatafel, Runenaltar (mit Messingbarren) und Terrastahl.",
              "",
              "Das Obelisk-Ziel von Stufe 2 will &e600 Manaperlen&r, &e50 Terrastahlbarren&r und &e8 Runenkerne&r. Das sind über &d30 Millionen Mana&r. Füllt jetzt schon Becken.",
              "",
              "Das Elfenportal folgt mit Stufe 3, der Gaia-Wächter mit Stufe 4.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["farm"], icon="botania:mana_pool"),

]

images = [
    banner("botania/title", "Botania", 9, -5.2, height=1.8, kind="title", colour="nature"),
    banner("botania/blueten", "Erste Blüten", 3.5, -2.6, height=0.9, colour="nature"),
    banner("botania/erzeugen", "Mana erzeugen", 2.5, 4.6, height=0.9, colour="nature"),
    banner("botania/speichern", "Mana speichern", 11.3, 3.9, height=0.9, colour="magic"),
    banner("botania/infusion", "Manainfusion", 3.5, 11.7, height=0.9, colour="magic"),
    banner("botania/funktion", "Funktionsblumen", 13.7, 11.2, height=0.9, colour="nature"),
    banner("botania/farm", "Die Farm", 19.7, 4.6, height=0.9, colour="magic"),
]

chapter(C, "Botania", "botania:pure_daisy", "magic", quests, shape="circle", order=3,
        subtitle=["Blumen, Mana und das erste Manabecken."], images=images)
