"""Checklist: every dimension of the pack and when it opens (spec.py DIMENSIONS, STAGES.md),
one quest per dimension with the portal in three lines, then the ways to travel (waystones with
the costs from waystones-common.toml, Tempad, the Mekanism teleporter, Ars warp scrolls and
portals, Botania sashes, Ender IO travel anchors, Create trains, FTB Chunks force loading) and
the tools that find things (JourneyMap waypoints, Nature's Compass, the Cataclysm eyes, the
dowsing rod). Stage 1 chapter: item tasks only for stage 1 items, everything later is a
checkmark and points to its chapter. Portal mechanics come from the mod jars and configs."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "list_dimensions"
MINING = "ultimate_mining_dimension:ultimate_mining_dimension"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    quest("welcome", 0, 0, "&6Dimensionen und Reisen",
          subtitle="Jede Welt des Packs, jeder Weg dorthin, auf einen Blick.",
          description=[
              "Kronwerke hat neben der Oberwelt &esieben Dimensionen&r. Eine ist von Anfang an offen, die anderen kommen mit den Stufen: &6Nether&r und &6Aether&r in Stufe 2, &6Undergarden&r und &6Otherside&r in Stufe 3, &6End&r, &6Eternal Starlight&r und das &6Reality Marble&r in Stufe 4. Der Twilight Forest ist nicht im Pack.",
              "",
              "Jede Quest hier ist ein Portal in drei Zeilen: wie du es baust, was drüben wartet, was du mitnimmst. Die Einzelheiten stehen im Kapitel der Dimension, hier steht nur, was du zum Losgehen brauchst.",
              "",
              "Darunter die Reihe &eReisen&r (Wegsteine, Teleporter, Züge, Chunks) und die Reihe &eKarte&r (Wegpunkte, Kompasse, Augen). Lies, hak ab, hol die Belohnung.",
          ],
          tasks=[task_checkmark("Los geht's")],
          rewards=[reward_item("waystones:return_scroll", 2), reward_xp(2)],
          icon="minecraft:filled_map", size=2.5, shape="hexagon"),

    # ---- Stufe 1 -------------------------------------------------------------------
    quest("d_mining", 4.5, -8, "&6Öffne die Minendimension",
          subtitle="Eisenblöcke, eine Spitzhacke, Stufe 1.",
          description=[
              "&eRezept auf Kronwerke:&r Die &6Verzauberte Spitzhacke&r sind &e2 Diamanten&r und ein &6Goldblock&r in der oberen Reihe, &e2 Stöcke&r darunter in der Mitte. Das Rezept des Mods selbst lädt auf 1.21 nicht und bräuchte Netherit.",
              "",
              "&eDas Portal:&r Ein Rahmen aus &6Eisenblöcken&r wie ein Netherportal, 4 breit und 5 hoch, ohne Ecken &e10 Blöcke&r. Rechtsklick mit der Spitzhacke auf die Innenseite, und es öffnet sich.",
              "",
              "&eDrüben:&r Stein, Erz und Höhlen ohne Ende, ewige Dämmerung, und niemand stört sich an Löchern. Alles Weitere im Kapitel &aErkundung&r.",
          ],
          tasks=[task_item(MINING, 1)],
          rewards=[reward_item("minecraft:iron_block", 4), reward_xp(3)],
          deps=["welcome"], icon=MINING),

    quest("d_mining_rules", 6.5, -8, "&6Überleb in der Mine",
          subtitle="Kein Bett, kein Anker, dafür viele Fackeln.",
          description=[
              "&eMitnehmen:&r einen Stapel &6Fackeln&r, Essen, eine &6Rückkehr-Schriftrolle&r und Blöcke zum Abstützen. &eF3&r oder ein Wegpunkt am Portal, bevor du losgräbst.",
              "",
              "&cBetten explodieren&r dort unten, und Seelenanker funktionieren nicht. Stirbst du, liegt dein Körper in der Mine, und auf Kronwerke kann jeder ihn öffnen. Also zügig zurück oder einen Freund fragen.",
              "",
              "&eTipp:&r Ein &6Wegstein&r direkt neben dem Portal in der Mine spart den Rückweg zu Fuß. Er kostet dich auf dem Sprung zurück in die Oberwelt 27 Level, innerhalb der Mine aber fast nichts.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:torch", 32), reward_xp(2)],
          deps=["d_mining"], icon="minecraft:torch"),

    # ---- Stufe 2 -------------------------------------------------------------------
    quest("d_nether_event", 4.5, -4, "&cWarte auf das Nether-Event",
          subtitle="Die Stufe öffnet das Portal, nicht das Feuerzeug.",
          description=[
              "&eDie Regel:&r Der Nether ist bis &6Stufe 2 (Messingwerk)&r gesperrt, für alle gleichzeitig. Vorher kannst du Obsidian setzen und anzünden, so viel du willst, durchgehen geht nicht.",
              "",
              "&eDas Event:&r Sobald das Ziel der Stufe 1 bei 98 Prozent steht, setzt das Team einen Termin. Alle gehen live, die letzten Barren wandern in den Obelisken, und das &cNetherportal am Spawn&r wird vor laufender Kamera entzündet. Ab dann ist der Nether für alle offen.",
              "",
              "&eKronwerke:&r Hilf mit, dass es schnell geht: &eBruchstein&r, &eAndesitlegierung&r und &eQuelljuwelen&r am Obelisken bringen das Event näher. Welche Events es noch gibt, steht im Kapitel &6Tipps und Tricks&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["welcome"], icon="minecraft:bell"),

    quest("d_nether", 6.5, -4, "&cBau ein Netherportal",
          subtitle="Zehn Obsidian und ein Funke. Stufe 2.",
          description=[
              "&eDas Portal:&r Das am Spawn teilen sich alle, ein eigenes an der Basis geht ab Stufe 2 wie gewohnt.",
              "",
              "&eDrüben:&r Lohenruten für den Lohenbrenner, Netherquarz, Leuchtstein, Magma, Netherwarze, Antiker Schrott. Jeder Block im Nether zählt oben wie &eacht&r, ein Portal pro Basis macht den Server klein.",
              "",
              "&eMitnehmen:&r einen &6Goldhelm&r gegen die Piglins, einen &6Schild&r gegen Ghasts, Bruchstein für Brücken, ein zweites Feuerzeug. &cKein Bett.&r Alles Weitere im Kapitel &cDer Nether&r.",
          ],
          tasks=[task_checkmark("Portal gebaut")],
          rewards=[reward_item("minecraft:obsidian", 4), reward_item("minecraft:flint_and_steel", 1)],
          deps=["d_nether_event"], icon="minecraft:flint_and_steel"),

    quest("d_aether", 8.5, -4, "&bBau ein Aether-Portal",
          subtitle="Leuchtstein und ein Eimer Wasser. Stufe 2.",
          description=[
              "&eDas Portal:&r Ein Rahmen aus &6Leuchtstein&r, genau wie ein Netherportal, 4 breit und 5 hoch. Statt Feuer gießt du einen &6Wassereimer&r in den Rahmen, und das Portal leuchtet blau. Leuchtstein gibt es im Nether, deshalb öffnet der Aether mit ihm in &6Stufe 2&r.",
              "",
              "&eDrüben:&r schwebende Inseln, Skyroot und Holystone, Ambrosium, Zanite und Gravitit, Moas und fliegende Schweine. Drei Verliese mit drei Bossen: Bronze mit dem &6Slider&r, Silber mit der &6Walkürenkönigin&r, Gold mit dem &6Sonnengeist&r. Die Verliesausrüstung öffnet in Stufe 3.",
              "",
              "&eMitnehmen:&r Blöcke für Brücken, Essen, Pfeile. Werkzeuge aus der Oberwelt bauen Aether-Blöcke langsam ab, also gleich drüben &6Skyroot-&r und &6Holystone-Werkzeug&r machen. Beim ersten Besuch bekommst du das &6Buch der Überlieferung&r und goldene Fallschirme geschenkt. Alles Weitere im Kapitel &bDer Aether&r.",
          ],
          tasks=[task_checkmark("Portal gebaut")],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_item("minecraft:feather", 8)],
          deps=["d_nether_event"], icon="minecraft:water_bucket"),

    # ---- Stufe 3 -------------------------------------------------------------------
    quest("d_undergarden", 4.5, 0, "&2Öffne den Undergarden",
          subtitle="Steinziegel und ein Katalysator. Stufe 3.",
          description=[
              "&eDer Schlüssel:&r der &6Katalysator&r. &eRezept auf Kronwerke:&r &e4 Stahlbarren&r in den Ecken, &e4 Stein&r an den Seiten und eine &6Enderperle&r in der Mitte.",
              "&eDas Portal:&r Ein Rahmen aus &6Steinziegeln&r (auch rissig, bemoost, gemeißelt, oder Tiefschieferziegel) wie ein Netherportal, dann Rechtsklick mit dem Katalysator.",
              "",
              "&eDrüben:&r ewige Nacht, Pilze, Moderwesen, die dich anstecken, und vier Erze: &6Cloggrum&r, &6Froststahl&r, &6Utherium&r und &6Regalium&r. Betten funktionieren. Ein Block dort sind &evier&r in der Oberwelt.",
              "",
              "&eMitnehmen:&r 64 Fackeln, ein Bett, Essen, Pfeile, Rüstung. Alles Weitere im Kapitel &2Der Undergarden&r.",
          ],
          tasks=[task_checkmark("Portal gebaut")],
          rewards=[reward_item("minecraft:stone_bricks", 16), reward_xp(3)],
          deps=["welcome"], icon="minecraft:stone_bricks"),

    quest("d_otherside", 6.5, 0, "&3Öffne die Otherside",
          subtitle="Verstärkter Tiefenschiefer und das Herz der Tiefe. Stufe 3.",
          description=[
              "&eDas Portal:&r Ein Rahmen aus &6Verstärktem Tiefenschiefer&r wie ein Netherportal, 10 Blöcke ohne Ecken. Entzündet wird er mit dem &6Herz der Tiefe&r (Heart of the Deep), das der &cWarden&r fallen lässt. Ein Warden, ein Herz, ein Portal.",
              "",
              "&eRezept auf Kronwerke:&r &e4 Tiefenschiefer&r in den Ecken, &e4 Stahlbarren&r an den Seiten und eine &6Echoscherbe&r in der Mitte ergeben &e2 Verstärkten Tiefenschiefer&r. Vanilla lässt den Block in den Antiken Städten nichts droppen. Der andere Weg ist ein Occultism-Ritual, das pro Block einen Warden opfert.",
              "",
              "&eDrüben:&r Sculk, so weit das Auge reicht: Deeplands, Blooming Caverns, Echoing Forest, Overcast Columns. Erze in Sculkstein und Gloomslate, Sculk-Kriecher, Shattered, Stalker. &eMitnehmen:&r Wolle für leise Schritte, Fackeln, Rüstung. Alles Weitere im Kapitel &3Deeper and Darker&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:lantern", 8), reward_xp(3)],
          deps=["d_undergarden"], icon="minecraft:reinforced_deepslate"),

    quest("d_compact", 8.5, 0, "&dBetritt eine Compact Machine",
          subtitle="Ein Raum im Würfel. Stufe 3.",
          description=[
              "&eDie Wände:&r &e8 Polierter Tiefenschiefer&r im Ring ergeben 8 &6Compact-Machine-Wände&r. Sechs Wände, ein &6Schrumpf-&r und ein &6Vergrößerungsmodul&r und ein Kern in der Mitte ergeben die Maschine.",
              "&eDer Kern bestimmt die Größe:&r Kupfer 3, Eisen 5, Gold 7, Diamant 9, Obsidian 11, Netherit 13 Blöcke im Würfel.",
              "&eHinein:&r Rechtsklick mit dem &6Personal Shrinking Device&r (beide Module, Enderauge, Eisen, Kupfer, Glas) auf die Maschine. Damit kommst du auch wieder hinaus.",
              "",
              "&eDrüben:&r ein leerer Raum, der keinen Platz in deiner Basis kostet, mit eigenem Spawnpunkt. In dieser Version gibt es keine Tunnel: Items, Flüssigkeiten und Strom gehen nicht durch die Wand. Alles Weitere im Kapitel &6Logistik&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:polished_deepslate", 16), reward_xp(3)],
          deps=["d_undergarden"], icon="minecraft:polished_deepslate"),

    quest("d_alfheim", 10.5, 0, "&aÖffne das Tor nach Alfheim",
          subtitle="Ein Portal, durch das nur Waren gehen. Stufe 3.",
          description=[
              "&eDas Portal:&r Ein aufrechter Rahmen aus &e8 Lebeholz&r und &e3 Schimmerndem Lebeholz&r, unten in der Mitte das &6Elfenportal-Herzstück&r, dazu &e2 Manabecken&r mit &6Naturapylonen&r im Umkreis von 5 Blöcken. Rechtsklick mit dem &6Stab des Waldes&r auf das Herzstück, das Öffnen kostet &d200 000 Mana&r.",
              "",
              "&eDrüben:&r niemand. Alfheim ist keine Dimension, die du betrittst. Du wirfst Ware hinein, die Elfen werfen Besseres zurück: Traumholz, Elementium, Feenstaub, Drachenstein. Jeder Tausch kostet 500 Mana.",
              "",
              "&cNiemals Brot hineinwerfen.&r Alles Weitere im Kapitel &aBotania: Alfheim&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("botania:livingwood_log", 8), reward_xp(3)],
          deps=["d_compact"], icon="botania:livingwood_log"),

    # ---- Stufe 4 -------------------------------------------------------------------
    quest("d_end_event", 4.5, 4, "&5Warte auf das End-Event",
          subtitle="Das Endportal wird auf Stream aktiviert.",
          description=[
              "&eDie Regel:&r Das End ist bis &6Stufe 4 (Sternwerk)&r gesperrt. Festungen findest du vorher, Enderaugen kannst du einsetzen, hindurch kommst du nicht.",
              "",
              "&eDas Event:&r Wenn das Ziel der Stufe 3 bei 98 Prozent steht, gibt es einen Termin. Auf Stream wird das &5Endportal&r aktiviert, und der &5Enderdrache&r ist der erste Boss, den der ganze Server gemeinsam bekämpft. Wartet mit dem Drachen auf die anderen.",
              "",
              "&eKronwerke:&r Stufe 4 braucht Draconium, und das gibt es nur im End. Deshalb ist dieses Event das wichtigste der Season für die Techniker.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(3)],
          deps=["welcome"], icon="minecraft:ender_pearl"),

    quest("d_end", 6.5, 4, "&5Finde ein eigenes Endportal",
          subtitle="Zwölf Enderaugen und eine Festung. Stufe 4.",
          description=[
              "&eDer Weg:&r Wirf ein &6Enderauge&r (Enderperle und Lohenstaub) in die Luft, lauf hinterher, wirf das nächste. Zeigt es nach unten, grab. Auf Kronwerke sind das die großen Festungen von YUNG's Better Strongholds.",
              "&eDas Portal:&r 12 Rahmenblöcke, in jeden ein Enderauge, dann öffnet es sich. Das Portal vom Event reicht für alle, ein eigenes lohnt sich nur bei weit entfernter Basis.",
              "",
              "&eDrüben:&r Leere unter den Inseln, Endermen überall, Endsiedlungen mit Shulkern und Elytren, Chorus, Draconium. &eMitnehmen:&r geschnitzten Kürbis, Bogen und viele Pfeile, Blöcke, Wassereimer, goldene Karotten. Alles Weitere im Kapitel &5Das End&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(3)],
          deps=["d_end_event"], icon="minecraft:cracked_stone_bricks"),

    quest("d_starlight", 8.5, 4, "&bÖffne Eternal Starlight",
          subtitle="Ein Torwächter, eine Kugel, ein Rahmen. Stufe 4.",
          description=[
              "&eDas Portal:&r In der Oberwelt stehen kleine Ruinen mit einem Rahmen aus &6Chiseled Voidstone&r, in Ebenen, Wäldern, Wüsten, Dschungeln und kalten Biomen. Davor wartet der &bTorwächter&r. Rechtsklick, &eChallenge&r wählen, gewinnen.",
              "&eDer Lohn:&r die &bOrb of Prophecy&r. Benutz sie am Rahmen, und das Portal öffnet sich. Weitere Kugeln sind 5 blaue Sternenlicht-Kristallscherben und 4 Glas.",
              "",
              "&eDrüben:&r ewige Nacht unter Sternen, Lunar-Wälder, die Kristallwüste, der ewige Frost, drei Bosse. &eMitnehmen:&r gute Rüstung, Essen, Fackeln, Blöcke für einen sicheren Raum am Portal. Alles Weitere im Kapitel &bEternal Starlight&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:glass", 8), reward_xp(3)],
          deps=["d_end_event"], icon="minecraft:glass"),

    quest("d_marble", 10.5, 4, "&bBetritt das Reality Marble",
          subtitle="Eine Dimension aus einer Schriftrolle. Stufe 4.",
          description=[
              "&eDer Weg:&r Die Rolle &bPerle der Realität&r (Reality Marble) von Mahou Tsukai teleportiert dich an einen festen Ort in einer eigenen kleinen Welt voller Schwerter. Sie kostet &d4 000 Mana&r pro Benutzung.",
              "",
              "&eDrüben:&r ein Duellplatz. Schaust du beim Benutzen ein Ziel an, nimmst du es mit, und einer von euch muss sterben, damit der andere wieder herauskommt. Allein genügt es, Schaden zu nehmen, dann bist du zurück.",
              "",
              "&eMitnehmen:&r nur, was du im Kampf brauchst. Alles Weitere im Kapitel &dMahou Tsukai&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:iron_sword", 1), reward_xp(3)],
          deps=["d_starlight"], icon="minecraft:iron_sword"),

    # ---- Reisen --------------------------------------------------------------------
    quest("r_waystones", 4.5, 8.5, "&6Reise mit Wegsteinen",
          subtitle="Ein Level pro 100 Blöcke, höchstens 27.",
          description=[
              "&eSo geht es:&r Rechtsklick auf einen &6Wegstein&r aktiviert ihn. Ab dann reist du von jedem Wegstein zu jedem, den du kennst. Eigene baust du aus einem &6Warpstein&r, 3 Steinziegeln und 3 Obsidian.",
              "",
              "&eWas es kostet (Serverconfig):&r &e1 Level je 100 Blöcke&r Luftlinie, höchstens &e27&r. In eine andere Dimension immer &e27 Level&r. &eKostenlos&r sind globale Wegsteine, Warpplatten und alle Schriftrollen. Ein Warpstein lädt 1,6 Sekunden, nutzt sich ab und hat eine Abklingzeit.",
              "",
              "&eTipp:&r Für den Sprung zwischen Dimensionen ist das Portal fast immer billiger. Für den Weg zur Basis in derselben Welt ist die &6Rückkehr-Schriftrolle&r (2 Goldnuggets, Tintenbeutel, 3 Papier) unschlagbar. Alles Weitere im Kapitel &aErkundung&r.",
          ],
          tasks=[task_item("waystones:return_scroll", 1)],
          rewards=[reward_item("waystones:warp_dust", 8), reward_xp(3)],
          deps=["welcome"], icon="waystones:waystone"),

    quest("r_plates", 6.5, 8.5, "&6Verbinde zwei Orte mit Warpplatten",
          subtitle="Draufstellen, weg, und es kostet nichts.",
          description=[
              "&eSo geht es:&r Zwei &6Warpplatten&r, ein &6Ruhender Splitter&r (2 Warppulver, Feuerstein) in die erste Platte gelegt wird eingestellt, den trägst du zur zweiten. Ab dann bringt dich jede Platte zur anderen, sobald du eine Dreiviertelsekunde darauf stehst.",
              "",
              "&eWarum:&r Warpplatten kosten laut Serverconfig &ekeine Erfahrung&r, auch zwischen Dimensionen nicht. Eine Platte an der Basis, eine am Portal in der Mine oder im Nether, und du sparst dir die 27 Level jedes Mal.",
              "",
              "Angeleinte Tiere nimmt die Platte mit, Haustiere nicht.",
          ],
          tasks=[task_item("waystones:warp_plate", 2)],
          rewards=[reward_item("waystones:warp_dust", 8), reward_xp(3)],
          deps=["r_waystones"], icon="waystones:warp_plate"),

    quest("r_nether_hub", 8.5, 8.5, "&cNutze den Nether als Abkürzung",
          subtitle="Ein Block dort, acht Blöcke hier. Stufe 2.",
          description=[
              "&eSo geht es:&r Teil die Oberwelt-Koordinaten deines Ziels durch 8, geh im Nether genau dorthin und bau dort ein Portal. Die beiden Portale finden sich, wenn sie nah genug beieinander liegen.",
              "",
              "&eWarum:&r 800 Blöcke Oberwelt sind 100 Blöcke Nether. Ein gemeinsamer Tunnel aus Bruchstein auf etwa &eY 100 bis 120&r verbindet alle Basen des Servers mit dem Spawn, und Create-Gleise dürfen durch das Portal hindurch (Kapitel &6Create: Züge&r).",
              "",
              "Sprecht euch im Chat ab, wer wo baut. Der Undergarden macht dasselbe mit 4 zu 1, nur ungemütlicher.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:obsidian", 4), reward_xp(3)],
          deps=["r_waystones"], icon="minecraft:obsidian"),

    quest("r_trains", 10.5, 8.5, "&6Fahr mit dem Zug zur anderen Basis",
          subtitle="Gleise, Bahnhof, Fahrplan. Stufe 2.",
          description=[
              "&eSo geht es:&r &6Gleise&r kommen vom Fließband aus Eisen und Robustem Blech, ein &6Bahnhof&r setzt den Zug zusammen, &6Zugsteuerung&r und &6Fahrplan&r lassen ihn allein fahren. Alles im Kapitel &6Create: Züge&r.",
              "",
              "&eWarum:&r Ein Zug trägt Fracht, Flüssigkeiten und Mitspieler, kostet keine Level und fährt weiter, auch wenn die Chunks unterwegs nicht geladen sind. Für den Weg Fabrik, Spawn, Obelisk ist er der bequemste Weg.",
              "",
              "&eKronwerke:&r Ein gemeinsamer Hauptbahnhof am Spawn mit einem Gleis pro Basis ist schöner als dreißig Stummelgleise. Fragt im Chat, bevor ihr verlegt.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:rail", 16), reward_xp(3)],
          deps=["r_nether_hub"], icon="minecraft:rail"),

    quest("r_ars", 4.5, 11, "&dSchreib eine Warp-Schriftrolle",
          subtitle="Ars Nouveau: einmal nach Hause, oder ein Portal. Stufe 2.",
          description=[
              "&eSo geht es:&r Die &6Warp-Schriftrolle&r sind 4 Lapis, 4 Quelljuwelen und ein leeres Pergament, formlos. Schleich-Rechtsklick speichert den Ort, Rechtsklick bringt dich hin und verbraucht die Rolle. Die &6Stabilisierte&r Rolle aus dem Apparat hält ewig und kann die Dimension wechseln.",
              "",
              "&eDas Warp-Portal:&r Bau einen Rahmen aus &6Quellstein&r (1x1 bis 21x21, stehend oder liegend), stell ein volles &6Quellglas&r daneben und wirf eine beschriebene Rolle hinein. Das Portal bleibt stehen und kostet danach keine Quelle mehr, führt aber nur innerhalb derselben Dimension.",
              "",
              "In Stufe 3 kommt das &6Ritual der Verschiebung&r, das alle in der Nähe zum Ort auf der Rolle schickt. Alles im Kapitel &dArs Nouveau: Magier&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("ars_nouveau:source_gem", 4), reward_xp(3)],
          deps=["r_waystones"], icon="ars_nouveau:sourcestone"),

    quest("r_botania", 6.5, 11, "&aLauf und flieg mit Botania",
          subtitle="Schärpen und Stäbe statt Portale.",
          description=[
              "&eSchärpe des Reisenden&r (Stufe 2): Manastahl, Leder und die Runen der Erde und der Luft. Schneller laufen, höher springen, Stufen hochgehen wie Treppen, weniger Fallschaden, für ein Rinnsal Mana.",
              "&eSchärpe des Weltenwanderers&r (Stufe 2): Schärpe, Karte, Weidesamen, Zucker. Je länger du läufst, desto schneller wirst du.",
              "&eStab der Lüfte&r (Stufe 2): Lebeholzzweig, Feder, Rune der Luft. Schleudert dich in die Höhe.",
              "",
              "&eFlügel-Tiara&r (Stufe 4): Gaia-Seelen, Elementium, Federn und reine Ender-Essenz. Dann fliegst du mit Mana wie im Kreativmodus. Die &eGlobetrotter-Schärpe&r (Stufe 4) braucht ebenfalls eine Gaia-Seele.",
              "",
              "Alles im Kapitel &aBotania: Runen&r und &aBotania: Alfheim&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:leather", 4), reward_xp(3)],
          deps=["r_ars"], icon="minecraft:leather"),

    quest("r_tempad", 8.5, 11, "&dÖffne eine Zeittür",
          subtitle="Tempad: 1 000 Chronon pro Tür, auch zwischen Welten. Stufe 3.",
          description=[
              "&eRezept auf Kronwerke:&r Das &6Tempad&r sind 3 getöntes Glas oben, Quarz, &6Warpstaub&r und Redstonelampe in der Mitte, unten Zeitstahl, &6Chronon-Batterie&r, Zeitstahl. Es speichert Orte und öffnet eine &6Zeittür&r dorthin, Dimension egal.",
              "",
              "&eWas es kostet (Serverconfig):&r &e1 000 Chronon&r für 10 Sekunden Tür, jede weitere Sekunde 10. Das Tempad fasst 6 000, also sechs Türen. Chronon macht das &6Chronometer&r in der Hand (1 je 36 Ticks) oder das &6Metronom&r als Block (1 je 24 Ticks, 6 000 Speicher).",
              "",
              "Wer Zeitstahl und Warpstaub schon in Stufe 2 sammelt, baut sein Gerät am ersten Abend von Stufe 3. Siehe Kapitel &6Rohre und Router&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("waystones:warp_dust", 2), reward_xp(3)],
          deps=["r_ars"], icon="minecraft:clock"),

    quest("r_mekanism", 10.5, 11, "&dBau einen Teleporter",
          subtitle="Mekanism: Rahmen, Frequenz, Strom. Stufe 3.",
          description=[
              "&eSo geht es:&r Ein &6Teleportationskern&r (&eRezept auf Kronwerke:&r 4 Manaperlen, 2 Atomlegierungen, 2 Gold, Diamant) wird mit 4 Stahlgehäusen und 4 einfachen Schaltkreisen zum &6Teleporter&r. Dazu &e9 Teleporter-Rahmen&r aus raffiniertem Obsidian und Glowstone, als Rahmen 4 breit und 5 hoch, der Teleporter ist einer der Rahmenblöcke.",
              "",
              "&eWarum:&r Zwei Teleporter mit derselben &eFrequenz&r verbinden zwei Basen oder zwei Dimensionen, ohne Level und ohne Wartezeit. Nur Strom, mehr je weiter. Der &6Tragbare Teleportierer&r springt von überall zu jedem Teleporter deiner Frequenz.",
              "",
              "Alles im Kapitel &6Mekanism: Fortgeschritten&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:diamond", 1), reward_xp(3)],
          deps=["r_tempad"], icon="minecraft:diamond"),

    quest("r_enderio", 12.5, 11, "&bSetz Reiseanker",
          subtitle="Ender IO: von Anker zu Anker springen. Stufe 3.",
          description=[
              "&eSo geht es:&r Ein &6Reiseanker&r sind 4 Eisen, 4 Leitungsbinder und ein &6Pulsierender Kristall&r. Stell Anker in deiner Basis auf, schleich und schau einen anderen Anker an, und du springst hin. Der &6Stab des Reisens&r (Dunkelstahl, Enderkristall) springt mit 1 000 FE auch ins Freie, 24 Blöcke weit, 100 000 FE Speicher.",
              "",
              "&eWarum:&r Für eine große Fabrik mit mehreren Etagen und Hallen gibt es nichts Bequemeres. Anker zu Anker reicht 96 Blöcke, Stab zu Anker 192.",
              "",
              "Alles im Kapitel &6Ender IO&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["r_mekanism"], icon="minecraft:iron_block"),

    quest("r_chunks", 12.5, 8.5, "&6Lade Chunks auf dem Weg",
          subtitle="25 Chunks bleiben geladen, auch über Nacht.",
          description=[
              "&eSo geht es:&r &eM&r öffnet die Karte von FTB Chunks, &eC&r die Claim-Ansicht. Linke Maustaste ziehen beansprucht, &eShift&r und ziehen lädt dauerhaft. Dein Team hat &e500 Claims&r und &e25 geladene Chunks&r, zusammen, nicht pro Kopf.",
              "",
              "&eWas das heißt:&r Geladene Chunks laufen weiter, während du anderswo bist, auch wenn dein ganzes Team offline ist. Maschinen an einem Portal, eine Pumpe im Nether, ein Bahnhof: alles, was ohne dich arbeiten soll, braucht einen geladenen Chunk.",
              "",
              "&eTipp:&r Lad nicht die Strecke, lad die Enden. Ein Zug fährt auch durch ungeladene Chunks, der Bahnhof am Ziel muss aber geladen sein, damit die Fracht ankommt.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["r_trains"], icon="minecraft:map"),

    # ---- Karte ---------------------------------------------------------------------
    quest("k_waypoints", 4.5, 15, "&6Setz Wegpunkte",
          subtitle="JourneyMap merkt sich den Ort, du nicht.",
          description=[
              "&eSo geht es:&r &eJ&r öffnet JourneyMap. Rechtsklick auf die Karte oder &eB&r in der Welt setzt einen &6Wegpunkt&r mit Namen und Farbe, er wird dir am Horizont und auf der Minimap gezeigt. Jeder aktivierte Wegstein wird automatisch zum Wegpunkt.",
              "",
              "&eWofür:&r jedes Portal, jedes Bauwerk, jede Erzader, jeden Leichnam. Wegpunkte gelten pro Dimension, im Nether siehst du also deine Nether-Punkte.",
              "",
              "&eTipp:&r Wegpunkte lassen sich mit FTB Chunks an dein Team oder den ganzen Server teilen. So findet jeder den Hauptbahnhof.",
          ],
          tasks=[task_checkmark("Einen Wegpunkt gesetzt")],
          rewards=[reward_item("minecraft:paper", 8), reward_xp(2)],
          deps=["welcome"], icon="minecraft:filled_map"),

    quest("k_natures", 6.5, 15, "&aFinde ein Biom",
          subtitle="Der Kompass der Natur zeigt den Weg.",
          description=[
              "&eRezept:&r ein &6Kompass&r in der Mitte, 4 Holzstämme an den Seiten, 4 Setzlinge in den Ecken. Rechtsklick öffnet die Liste aller Biome, wähl eines, und der Kompass zeigt Richtung und Entfernung.",
              "",
              "&eWofür:&r den &dArchwood-Wald&r für Ars Nouveau, Wüsten und warme Meere für die Bosse von Cataclysm, kalte Biome für die Portalruinen von Eternal Starlight.",
          ],
          tasks=[task_item("naturescompass:naturescompass", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 8), reward_xp(3)],
          deps=["k_waypoints"], icon="naturescompass:naturescompass"),

    quest("k_dowsing", 8.5, 15, "&dNimm die Wünschelrute mit",
          subtitle="Amethyst und magische Wesen durch Stein sehen.",
          description=[
              "&eRezept:&r ein &6Goldbarren&r und 2 &6Archwood-Planken&r ergeben die &6Wünschelrute&r. Benutz sie, und du siehst eine Weile Amethyst und magische Wesen durch Wände hindurch. Jede Nutzung kostet Haltbarkeit.",
              "",
              "&eWofür:&r Amethyst steckt im Warppulver, also in fast jedem Reise-Gegenstand von Waystones. Eine Tour durch die Minendimension mit der Rute findet die Geoden, ohne blind zu graben.",
          ],
          tasks=[task_item("ars_nouveau:dowsing_rod", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 8), reward_xp(3)],
          deps=["k_waypoints"], icon="ars_nouveau:dowsing_rod"),

    quest("k_eyes", 10.5, 15, "&cFolge den Augen von Cataclysm",
          subtitle="Acht Augen, acht Bauwerke. Stufe 2.",
          description=[
              "Jedes Auge craftest du um ein &6Enderauge&r herum, deshalb erst in Stufe 2. Geworfen fliegt es wie ein Enderauge zum nächsten Bauwerk seiner Art:",
              "",
              "&eWüstenauge:&r verfluchte Pyramide. &eFluchauge:&r frostiges Gefängnis. &eAbgrundauge:&r versunkene Stadt. &eMechanisches Auge:&r alte Fabrik. &eSturmauge:&r Akropolis.",
              "&eFlammenauge&r und &eMonströses Auge:&r brennende Arena und Seelenschmiede, beide im Nether. &eAuge der Leere:&r die zerstörte Zitadelle im End, Stufe 4.",
              "",
              "Rezepte und Bosse im Kapitel &cBosse der Oberwelt&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(3)],
          deps=["k_natures"], icon="minecraft:spyglass"),

    quest("k_mod_compasses", 12.5, 15, "&6Kenn die Kompasse der Dimensionen",
          subtitle="Jede Welt hat ihr eigenes Suchgerät.",
          description=[
              "&eOberwelt:&r Ein &6Leitstein&r (Netheritbarren in gemeißeltem Steinziegel, Stufe 2) macht einen Kompass zum festen Zeiger auf einen Ort. Der &6Bergungskompass&r (8 Echoscherben aus antiken Städten um einen Kompass) zeigt auf deinen letzten Tod.",
              "&eOtherside:&r Der &6Antike Kompass&r (Kompass, 4 Warden-Panzer) zeigt die nächste antike Stadt. Der Panzer kommt vom Warden, Stufe 3.",
              "&eEternal Starlight:&r Das &6Seeking Eye&r (8 Starlight Flowers, Enderperle) schwebt zu Bauwerken und Biomen der Sternenwelt, Stufe 4.",
              "",
              "Einen Explorer's Compass für Bauwerke gibt es im Pack nicht. Für Bauwerke der Oberwelt nimm die Augen von Cataclysm oder frag im Chat nach Koordinaten.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:compass", 1), reward_xp(3)],
          deps=["k_eyes"], icon="minecraft:compass"),

    # ---- Abschluss -----------------------------------------------------------------
    quest("done", 17, 8.5, "&6&lAlle Wege gegangen",
          subtitle="Du weißt, wohin es geht und wie du hinkommst.",
          description=[
              "Sieben Dimensionen, vier Stufen, zwei Events, ein Dutzend Arten zu reisen. Wer diese Liste abgehakt hat, verläuft sich nicht mehr und zahlt keine 27 Level für einen Weg, den eine Warpplatte umsonst macht.",
              "",
              "&eKronwerke:&r Die Portale am Spawn gehören allen. Bau ihnen eine Hütte aus Bruchstein, lass einen Wegstein daneben stehen und erklär dem nächsten Neuen, was du hier gelesen hast.",
          ],
          tasks=[task_checkmark("Liste abgehakt")],
          rewards=[reward_table("s1_rare"), reward_item("waystones:warp_stone", 1), reward_xp(10)],
          deps=["d_mining_rules", "d_aether", "d_alfheim", "d_marble", "r_enderio", "r_chunks", "k_mod_compasses"],
          icon="waystones:waystone", size=2.0, shape="gear"),
]

images = [
    banner(f"{C}/title", "Dimensionen und Reisen", -1.5, -2.8, height=1.2, kind="title", colour="end"),
    banner(f"{C}/s1", "Stufe 1: Steinwerk", 5.5, -9.8, height=0.9, colour="stone"),
    banner(f"{C}/s2", "Stufe 2: Messingwerk", 6.5, -5.8, height=0.9, colour="fire"),
    banner(f"{C}/s3", "Stufe 3: Stahlwerk", 7.5, -1.8, height=0.9, colour="nature"),
    banner(f"{C}/s4", "Stufe 4: Sternwerk", 7.5, 2.2, height=0.9, colour="end"),
    banner(f"{C}/travel", "Reisen", 8.5, 6.7, height=0.9, colour="brass"),
    banner(f"{C}/map", "Karte", 8.5, 13.2, height=0.9, colour="water"),
]

chapter(C, "Checkliste: Dimensionen und Reisen", "minecraft:filled_map", "lists", quests, shape="circle",
        order=71, stage=1,
        subtitle=["Jede Dimension, wann sie öffnet und wie du hinkommst. Wegsteine, Teleporter, Züge, Karte."],
        images=images)
