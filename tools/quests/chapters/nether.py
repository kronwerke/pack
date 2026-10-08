"""The Nether in stage 2: the stage event lights the portal at spawn for everyone. Arrival and
gear, the resources (quartz, glowstone, magma, gold, the mod ores), the biomes, the mobs and their
drops, the fortresses with blazes and the Wither, the bastions with bartering and netherite, the
structures of Dungeons and Taverns and Formations Nether, and the two L_Ender's Cataclysm bosses
in the order to take them (Ignis in the Burning Arena, then the Netherite Monstrosity in the Soul
Black Smith). Boss numbers from the entity classes and cataclysm-common.toml, drops from the loot
tables, recipes from the jars and kubejs/server_scripts/tech_and_magic.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "nether"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Ankunft -------------------------------------------------------------
    quest("welcome", 0, 0, "&c&lBetritt den Nether",
          subtitle="Das Portal am Spawn ist seit dem Event für alle offen.",
          description=[
              "Geh durch das &6Portal am Spawn&r. Es wurde mit dem Event zu &eStufe 2&r auf Stream entzündet, seitdem ist der Nether für alle offen.",
              "",
              "Fast jede Maschine dieser Stufe braucht etwas von hier: &6Lohenruten&r für den Lohenbrenner, &6Netherquarz&r für Elektronenröhren, &6Leuchtstein&r für das Aether-Portal, &6Magma&r und Netherziegel für den Hochofen.",
              "",
              "&cLies die nächste Quest, bevor du durchgehst.&r Wer in einen Lavasee fällt, verliert alles, was er dabei hat.",
          ],
          tasks=[task_dimension("minecraft:the_nether")],
          rewards=[reward_item("minecraft:fire_charge", 4), reward_table("s2_common"), reward_xp(5)],
          icon="minecraft:netherrack", size=2.0, shape="hexagon"),

    quest("gear", 2.5, 0, "&6Rüste dich für den Nether aus",
          subtitle="Gold am Kopf, Schild in der Hand, Bruchstein im Gepäck.",
          description=[
              "Bring einen &6Goldhelm&r und einen &6Schild&r mit. Mit einem Teil Goldrüstung lassen dich die Piglins in Ruhe, der Schild fängt Feuerbälle der Ghasts ab.",
              "",
              "&eDazu:&r einen Stapel &6Bruchstein&r. Netherrack zerbricht bei Ghast-Explosionen, Bruchstein hält. Mit einem gut getimten Schlag schickst du einen Feuerball zurück.",
              "",
              "&cKein Bett:&r Im Nether explodiert es. Piglins werden trotz Gold wütend, wenn du vor ihren Augen Gold abbaust oder ihre Truhen öffnest.",
          ],
          tasks=[task_item("minecraft:golden_helmet", 1), task_item("minecraft:shield", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_item("minecraft:gold_ingot", 4)],
          deps=["welcome"], icon="minecraft:golden_helmet", size=1.5),

    quest("portal", 0, 2.5, "&5Bau ein eigenes Portal",
          subtitle="Zehn Obsidian und ein Feuerzeug.",
          description=[
              "Das Portal am Spawn teilen sich alle. Ein eigenes an der Basis spart den Weg, und jeder Block im Nether zählt oben wie acht.",
              "",
              "Bau eine Hütte aus Bruchstein um die Gegenseite, damit Ghasts sie nicht ausschießen, und hab immer ein zweites Feuerzeug dabei. Die Ghasts aus &6Born in Chaos&r und &6Cataclysm&r sind nicht die einzigen Gäste dort.",
          ],
          tasks=[task_item("minecraft:obsidian", 10), task_item("minecraft:flint_and_steel", 1)],
          rewards=[reward_item("minecraft:obsidian", 4), reward_xp(5)],
          deps=["welcome"], icon="minecraft:flint_and_steel"),

    quest("fast_travel", 0, 4.5, "&dReise durch den Nether",
          subtitle="Ein Block hier sind acht Blöcke oben.",
          description=[
              "Teil die Oberwelt-Koordinaten deines Ziels durch &e8&r, geh im Nether dorthin und bau dort ein Portal. Ein Block im Nether zählt oben wie acht.",
              "",
              "Ein gemeinsamer Tunnel aus Bruchstein auf Y 100 bis 120 ist meist ruhiger als die Ebene unten. Sprich dich mit den anderen ab, dann wird der Server klein.",
              "",
              "Die Quest ist erledigt, wenn du so &e7 000 Oberwelt-Blöcke&r am Stück zurücklegst.",
          ],
          tasks=[task_advancement("minecraft:nether/fast_travel", "Durch den Nether reisen")],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(10)],
          deps=["portal"], icon="minecraft:compass", optional=True),

    quest("waystone", 2.5, 2.5, "&bStell einen Wegstein in den Nether",
          subtitle="Innerhalb des Nethers billig, zwischen den Welten teuer.",
          description=[
              "Stell einen &6Wegstein&r an einen sicheren Ort, zum Beispiel neben dein Portal oder an eine Festung.",
              "",
              "&eKosten auf Kronwerke:&r Innerhalb einer Dimension 1 Level pro 100 Blöcke, ein Sprung in eine andere Dimension &e27 Level&r. Zwischen Oberwelt und Nether ist das Portal also billiger.",
              "",
              "Wilde Wegsteine gibt es auch im Nether, etwa alle 25 Chunks einen.",
          ],
          tasks=[task_item("waystones:waystone", 1)],
          rewards=[reward_item("waystones:warp_dust", 8)],
          deps=["welcome"], icon="waystones:waystone", optional=True),

    # ---- Rohstoffe -----------------------------------------------------------
    quest("netherrack", 6, -1.5, "&4Bau Netherrack ab",
          subtitle="Davon gibt es mehr als genug.",
          description=[
              "Bau &e64 Netherrack&r ab. Im Ofen wird er zu &6Netherziegeln&r, in jedem &6Leeren Lohenbrenner&r steckt ein Block.",
              "",
              "Netherziegel brauchst du für die Sprengziegel des Hochofens von Immersive Engineering. Eine Mühle von Create mahlt Netherrack zu Aschenmehl.",
              "",
              "Angezündet brennt Netherrack ewig. Ein guter Kamin.",
          ],
          tasks=[task_item("minecraft:netherrack", 64)],
          rewards=[reward_item("minecraft:coal", 16)],
          deps=["gear"], icon="minecraft:netherrack"),

    quest("quartz", 7.5, -1.5, "&fBau Netherquarz ab",
          subtitle="Weiß in jeder Wand.",
          description=[
              "Bau &6Netherquarzerz&r ab, bis du &e32 Netherquarz&r hast. Glück auf der Spitzhacke bringt mehr pro Erz.",
              "",
              pic("minecraft:quartz"),
              "",
              "Quarz ist der Anfang der Elektronik von Create, dazu Komparatoren, Beobachter und Quarzblöcke.",
          ],
          tasks=[task_item("minecraft:quartz", 32)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["netherrack"]),

    quest("rose_quartz", 10, -1.5, "&dMach Elektronenröhren",
          subtitle="Quarz mit Redstone, poliert, auf Eisenblech.",
          description=[
              "&6Netherquarz&r und &68 Redstone&r ergeben &6Rosenquarz&r. Mit &6Schmirgelpapier&r polierst du ihn, poliert auf einem &6Eisenblech&r wird er zur &6Elektronenröhre&r.",
              "",
              "Elektronenröhren stecken in allem, was bei Create Signale verarbeitet: Mechanischer Arm, Smarte Rutsche, Anzeigeverbindung. Auf Kronwerke auch im ersten Schaltkreis von Mekanism und in den smarten Kabeln von AE2.",
          ],
          tasks=[task_item("create:rose_quartz", 8), task_item("create:electron_tube", 2)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(5)],
          deps=["quartz"], icon="create:electron_tube"),

    quest("glowstone", 7.5, 0, "&eSammle Leuchtstein",
          subtitle="Er hängt an der Decke, oft über Lava.",
          description=[
              "Schlag &6Leuchtstein&r von der Decke, bis du &e32 Leuchtsteinstaub&r hast. Ohne Behutsamkeit gibt jeder Block 2 bis 4 Staub.",
              "",
              "&cBau erst eine Plattform darunter.&r Die Klumpen hängen gern über Lavaseen.",
              "",
              "Leuchtstein ist Licht, Trankverstärker, Brennstoff für den &6Seelenanker&r und der Rahmen des &bAether-Portals&r (Kapitel &bDer Aether&r).",
          ],
          tasks=[task_item("minecraft:glowstone_dust", 32)],
          rewards=[reward_item("minecraft:glowstone_dust", 16)],
          deps=["netherrack"]),

    quest("gold", 10, 0, "&6Schürf Nethergold",
          subtitle="Glitzernd im Netherrack.",
          description=[
              "Bau &6Nethergolderz&r ab, bis du &e64 Goldnuggets&r hast. Glück bringt mehr pro Erz, 9 Nuggets sind ein Barren.",
              "",
              pic("minecraft:gold_nugget"),
              "",
              "Gold ist hier unten Währung: Piglins tauschen dagegen allerhand (Abschnitt Bastionen).",
          ],
          tasks=[task_item("minecraft:gold_nugget", 64)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["netherrack"], icon="minecraft:gold_nugget"),

    quest("magma", 7.5, 1.5, "&6Hol Magma",
          subtitle="Heiß unter den Füßen.",
          description=[
              "Sammle &e9 Magmablöcke&r an Lavaseen oder in den Basaltdeltas und &e4 Magmacreme&r von den hüpfenden &6Magmawürfeln&r.",
              "",
              "Magmacreme ist die Zutat für den &6Trank der Feuerresistenz&r, vier davon ergeben einen Magmablock. Neun Magmablöcke stecken in den Sprengziegeln eines Hochofens.",
              "",
              "Auf Magma verbrennst du dich, außer beim Schleichen.",
          ],
          tasks=[task_item("minecraft:magma_block", 9), task_item("minecraft:magma_cream", 4)],
          rewards=[reward_item("minecraft:slime_ball", 4)],
          deps=["netherrack"], icon="minecraft:magma_cream"),

    quest("mod_ores", 10, 1.5, "&5Finde Purpur-Eisen",
          subtitle="Das Erz von Silent Gear wächst nur im Nether.",
          description=[
              "Bau &6Purpur-Eisenerz&r ab, bis du &e8 Rohes Purpur-Eisen&r hast. Geschmolzen ist es die nächste Materialstufe für Silent Gear (Kapitel &6Silent Gear&r).",
              "",
              "&eWas sonst im Nether liegt:&r die Gesteinsschichten von Create mit &6Scoria&r und &6Scorchia&r, &6Dimensionsscherben&r von RFTools (die brauchst du ab Stufe 3) und die Erze aus der nächsten Quest.",
          ],
          tasks=[task_item("silentgear:raw_crimson_iron", 8)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["netherrack"], icon="silentgear:raw_crimson_iron"),

    quest("r_soulstone", 12.5, 1.5, "&8Grab Seelenstein",
          subtitle="Mystical Agriculture hat den Nether mit Erz gefüllt.",
          description=[
              "Bau &e16 Seelenstein&r ab. Er ist ein eigenes Gestein von Mystical Agriculture und liegt im ganzen Nether.",
              "",
              "Dazu findest du hier &6Nether-Inferiumerz&r und &6Nether-Prosperiumerz&r, dieselben Splitter und Essenzen wie in der Oberwelt, nur in Netherrack. Was du damit machst, steht im Kapitel &6Mystical Agriculture&r.",
          ],
          tasks=[task_item("mysticalagriculture:soulstone", 16)],
          rewards=[reward_item("mysticalagriculture:prosperity_shard", 8), reward_xp(5)],
          deps=["mod_ores"], icon="mysticalagriculture:soulstone"),

    # ---- Biome ---------------------------------------------------------------
    quest("b_crimson", 0, 9, "&cFäll Karmesinstiele",
          subtitle="Karmesinwald: rote Pilzbäume, Hoglins und Piglins.",
          description=[
              "Fäll &e16 Karmesinstiele&r im &6Karmesinwald&r. Das Holz brennt nicht und ist ein gutes Bauholz.",
              "",
              "Hier leben &6Hoglins&r und Piglins. Die leuchtenden &6Schroomlichter&r in den Kronen sind helles Licht ohne Strom.",
          ],
          tasks=[task_item("minecraft:crimson_stem", 16)],
          rewards=[reward_item("minecraft:bone_meal", 8)],
          deps=["gear"], icon="minecraft:crimson_stem"),

    quest("b_warped", 2.5, 9, "&3Fäll Wirrstiele",
          subtitle="Wirrwald: türkise Bäume, Endermen, der ruhigste Ort hier.",
          description=[
              "Fäll &e16 Wirrstiele&r im &6Wirrwald&r. Auch dieses Holz brennt nicht.",
              "",
              "Im Wirrwald laufen fast nur &6Endermen&r herum. Für eine Basis im Nether ist das der sicherste Ort, und die Enderperlen nimmst du gleich mit.",
          ],
          tasks=[task_item("minecraft:warped_stem", 16)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["b_crimson"], icon="minecraft:warped_stem"),

    quest("b_soul", 0, 11, "&8Schaufel Seelensand",
          subtitle="Seelensandtal: langsam, offen und voller Skelette.",
          description=[
              "Schaufel &e16 Seelensand&r im &6Seelensandtal&r. Auf Seelensand wachsen Netherwarzen, und er gehört unter den Wither.",
              "",
              "Seelensand bremst dich. Skelette und Ghasts sehen dich hier von weit her, also zügig arbeiten und Deckung suchen.",
          ],
          tasks=[task_item("minecraft:soul_sand", 16)],
          rewards=[reward_item("minecraft:arrow", 16)],
          deps=["b_crimson"], icon="minecraft:soul_sand"),

    quest("b_basalt", 2.5, 11, "&7Bau Basalt ab",
          subtitle="Basaltdeltas: zerklüftet, voller Magmawürfel.",
          description=[
              "Bau &e32 Basalt&r in den &6Basaltdeltas&r ab. Schwarzstein liegt gleich daneben.",
              "",
              "Der Boden ist ein Gewirr aus Spitzen und Lavalöchern. Langsam gehen, Blöcke setzen, und die Magmawürfel aus der Ferne erledigen.",
          ],
          tasks=[task_item("minecraft:basalt", 32)],
          rewards=[reward_item("minecraft:magma_cream", 2)],
          deps=["b_soul"], icon="minecraft:basalt"),

    quest("biomes", 5, 10, "&c&lBesuche alle fünf Biome",
          subtitle="Netherödnis, Karmesin, Wirr, Seelensand, Basalt.",
          description=[
              "Betritt jedes der fünf Nether-Biome einmal. Die &6Netherödnis&r kennst du schon, sie ist das rote Land mit Ghasts, Quarz und Gold.",
              "",
              "Erledigt sich über den Fortschritt &eHeiße Touristenziele&r. Die Biome von Biomes O' Plenty zählen dafür nicht.",
          ],
          tasks=[task_advancement("minecraft:nether/explore_nether", "Alle Nether-Biome besuchen")],
          rewards=[reward_table("s2_common"), reward_xp(10)],
          deps=["b_warped", "b_basalt"], icon="minecraft:warped_fungus", size=1.5, shape="hexagon"),

    quest("bop", 7.5, 11, "&dFinde die Kristalline Kluft",
          subtitle="Biomes O' Plenty bringt fünf eigene Nether-Biome.",
          description=[
              "Bring &e4 Rosenquarzbrocken&r aus der &6Kristallinen Kluft&r mit. Sie sind ein Baustoff, nicht der Rosenquarz von Create.",
              "",
              "&eDie anderen:&r &6Unterholz&r (Höllenrinden-Wälder), &6Eingeweidehalde&r (Blöcke aus Fleisch, harmlos), &6Verdorrter Abgrund&r (sehr tiefe Schluchten) und &6Ausbrechendes Inferno&r (Lava, Feuer, Schwefel, nur mit Feuerresistenz).",
          ],
          tasks=[task_item("biomesoplenty:rose_quartz_chunk", 4)],
          rewards=[reward_xp(10)],
          deps=["biomes"], icon="biomesoplenty:rose_quartz_chunk", optional=True),

    # ---- Mobs ----------------------------------------------------------------
    quest("m_ghast", 0, 14, "&fHol eine Ghastträne",
          subtitle="Der Ghast weint, wenn er fällt.",
          description=[
              "Erleg Ghasts, bis du &e2 Ghasttränen&r hast. Am leichtesten mit dem Bogen, oder du schlägst ihre Feuerbälle zurück.",
              "",
              "Die Träne fällt gern in Lava. Kämpf über festem Boden. Du brauchst sie für Tränke der Regeneration und in Stufe 4 für die &5Endkristalle&r, mit denen der Drache neu erscheint.",
          ],
          tasks=[task_item("minecraft:ghast_tear", 2)],
          rewards=[reward_item("minecraft:arrow", 32), reward_xp(5)],
          deps=["gear"], icon="minecraft:ghast_tear"),

    quest("m_hoglin", 2.5, 14, "&cJag einen Hoglin",
          subtitle="Schweinefleisch und Leder im Nether.",
          description=[
              "Erleg &e3 Hoglins&r im Karmesinwald. Sie lassen Schweinefleisch und Leder fallen und sind die einzige echte Nahrungsquelle hier unten.",
              "",
              "Hoglins stoßen dich weit weg, auch über Klippen. &6Wirrpilze&r schrecken sie ab: Ein paar davon an deinem Lager halten sie fern.",
          ],
          tasks=[task_kill("minecraft:hoglin", 3)],
          rewards=[reward_item("minecraft:cooked_porkchop", 8)],
          deps=["b_crimson"], icon="minecraft:porkchop", section="mobs"),

    quest("m_strider", 5, 14, "&dReite einen Schreiter",
          subtitle="Über die Lavaseen statt außen herum.",
          description=[
              "Setz einem &6Schreiter&r einen &6Sattel&r auf und lenk ihn mit einer &6Wirrpilzrute&r (Angel plus Wirrpilz). So überquerst du ganze Lavaseen.",
              "",
              "Schreiter laufen auf Lava herum, oft in Gruppen. Sättel findest du in Festungen und Bastionen.",
          ],
          tasks=[task_advancement("minecraft:nether/ride_strider", "Einen Schreiter reiten")],
          rewards=[reward_item("minecraft:saddle", 1), reward_xp(5)],
          deps=["biomes"], icon="minecraft:warped_fungus_on_a_stick", optional=True, section="mobs"),

    quest("n_return_ghast", 0, 16, "&fSchick den Feuerball zurück",
          subtitle="Mit seinen eigenen Waffen geschlagen.",
          description=[
              "Erleg einen &6Ghast&r mit seinem eigenen Feuerball. Schlag den Feuerball im richtigen Moment mit der Hand, dem Schwert oder einem Pfeil, und er fliegt zurück.",
              "",
              "Ein Treffer reicht für einen Ghast. Das klappt besser als jeder Bogen auf diese Entfernung.",
          ],
          tasks=[task_advancement("minecraft:nether/return_to_sender", "Einen Ghast mit einem Feuerball erlegen")],
          rewards=[reward_item("minecraft:ghast_tear", 1), reward_xp(5)],
          deps=["m_ghast"], icon="minecraft:fire_charge", optional=True),

    quest("n_soul_lantern", 7.5, 14, "&3Halte Piglins mit Seelenfeuer fern",
          subtitle="Was blau brennt, meiden sie.",
          description=[
              "Kohle, ein Stock und &6Seelensand&r ergeben &6Seelenfackeln&r. Acht Eisennuggets um eine Fackel ergeben eine &6Seelenlaterne&r.",
              "",
              "Piglins meiden Seelenfeuer, Seelenfackeln, Seelenlaternen und Seelenlagerfeuer. Hoglins meiden Wirrpilze. Stell beides an dein Netherportal und um deinen Stützpunkt, dann bleibt es ruhiger.",
          ],
          tasks=[task_item("minecraft:soul_lantern", 4)],
          rewards=[reward_item("minecraft:soul_torch", 16), reward_xp(3)],
          deps=["b_soul"], icon="minecraft:soul_lantern", optional=True, section="mobs"),

    quest("n_froglight", 5, 16, "&6Füttere einen Frosch mit Magma",
          subtitle="Was er frisst, wird zu Licht.",
          description=[
              "Bring einen &6Frosch&r in den Nether, am einfachsten in einem Boot durch das Portal. Frisst er einen kleinen &6Magmawürfel&r, bleibt ein &6Froschlicht&r liegen.",
              "",
              "Die Farbe hängt vom Frosch ab: der orange Frosch aus dem Sumpf macht &6Ockerfarbenes Froschlicht&r, der grüne aus kalten Biomen grünes, der weiße aus warmen Biomen perlmuttfarbenes. Froschlicht ist eine helle Lichtquelle, die gut aussieht.",
          ],
          tasks=[task_item("minecraft:ochre_froglight", 1)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_xp(5)],
          deps=["magma"], icon="minecraft:ochre_froglight", optional=True, section="mobs"),

    # ---- Festungen -----------------------------------------------------------
    quest("fortress", 15, 0, "&4&lFinde eine Netherfestung",
          subtitle="Dunkle Ziegel, lange Brücken, Lohen.",
          description=[
              "Such eine &6Netherfestung&r und bring &e16 Netherziegel&r heraus. Halte von oben Ausschau nach dunklen Mauern über den Lavaseen.",
              "",
              "Auf Kronwerke baut &eYUNG's Better Nether Fortresses&r sie größer und verwinkelter, mit eigenen Räumen für die Spawner. Teil die Koordinaten im Chat.",
              "",
              "&cGefahren:&r Lohen, Witherskelette (die vergiften dich mit Wither) und Ghasts in den großen Hallen.",
          ],
          tasks=[task_item("minecraft:nether_bricks", 16)],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_table("s2_common")],
          deps=["gear"], icon="minecraft:nether_bricks", size=1.5, shape="hexagon"),

    quest("blaze", 17.5, 0, "&6&lErleg Lohen",
          subtitle="Der Rohstoff, um den sich diese Stufe dreht.",
          description=[
              "Erleg &e5 Lohen&r an ihrem Spawner und bring &e8 Lohenruten&r mit. Jede Lohe lässt bis zu eine Rute fallen, Plünderung mehr.",
              "",
              pic("minecraft:blaze_rod"),
              "",
              "Ein Schild blockt die Feuerkugeln, Schneebälle machen Lohen Schaden. Stell dich so, dass sie zu dir kommen. Der Zerkleinerer von Mekanism macht aus einer Rute 4 Lohenstaub statt 2.",
              "",
              "&cLass den Spawner stehen.&r Du brauchst ihn für Nachschub und für die lebende Lohe der nächsten Quest.",
          ],
          tasks=[task_kill("minecraft:blaze", 5), task_item("minecraft:blaze_rod", 8)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["fortress"], icon="minecraft:blaze_rod", size=1.75, shape="diamond"),

    quest("blaze_burner", 20, 0, "&6&lFang eine Lohe ein",
          subtitle="Eine Lohe im Käfig, und Create wird heiß.",
          description=[
              "Geh mit einem &6Leeren Lohenbrenner&r in der Hand zum Spawner und rechtsklick eine lebende &6Lohe&r. Sie landet im Käfig, und du hast einen &6Lohenbrenner&r.",
              "",
              "&eRezept auf Kronwerke:&r Der Leere Lohenbrenner braucht oben &62 Quelljuwelen&r aus Ars Nouveau mit einem Eisenblech dazwischen, in der Mitte Netherrack zwischen zwei Eisenblechen, unten ein Eisenblech.",
              "",
              "Unter einem Becken heizt er den Mixer für &6Messing&r. Wie es weitergeht, steht im Kapitel &6Create: Messing&r.",
          ],
          tasks=[task_item("create:blaze_burner", 1)],
          rewards=[reward_item("create:brass_ingot", 8), reward_table("s2_uncommon"), reward_xp(12)],
          deps=["blaze"], icon="create:blaze_burner", size=2.0, shape="gear"),

    quest("wart", 17.5, 2, "&4Ernte Netherwarzen",
          subtitle="Die Grundlage jedes Tranks.",
          description=[
              "Nimm &e8 Netherwarzen&r aus den Treppenhäusern und Gärten der Festung mit.",
              "",
              "Zuhause wachsen sie auf &6Seelensand&r, ohne Licht und ohne Wasser, auch in der Oberwelt. Ein kleines Feld reicht für alle Tränke.",
          ],
          tasks=[task_item("minecraft:nether_wart", 8)],
          rewards=[reward_item("minecraft:soul_sand", 8)],
          deps=["fortress"]),

    quest("brewing", 20, 2, "&cBrau Feuerresistenz",
          subtitle="Lava wird zum Badewasser.",
          description=[
              "Bau einen &6Braustand&r (Lohenrute, 3 Bruchstein). Wasserflasche plus &6Netherwarze&r, dann &6Magmacreme&r, ergibt den &6Trank der Feuerresistenz&r.",
              "",
              "Er hält 3 Minuten, mit Redstone 8. Der Braustand läuft mit Lohenstaub. Für jede längere Tour gehört ein Stapel davon in die Tasche.",
          ],
          tasks=[task_item("minecraft:brewing_stand", 1)],
          rewards=[reward_item("minecraft:glass_bottle", 6), reward_item("minecraft:blaze_powder", 4)],
          deps=["wart"], icon="minecraft:brewing_stand"),

    quest("wither_skull", 15, 2, "&8Sammle Witherskelettschädel",
          subtitle="Selten, und besser im Schrank.",
          description=[
              "Erleg Witherskelette, bis einer seinen &6Schädel&r fallen lässt. Plünderung hilft.",
              "",
              "Drei Schädel auf Seelensand beschwören den &cWither&r. Heb sie auf, bis der Server gemeinsam bereit ist (nächste Quest).",
          ],
          tasks=[task_item("minecraft:wither_skeleton_skull", 1)],
          rewards=[reward_item("minecraft:bone_block", 8), reward_xp(10)],
          deps=["fortress"], icon="minecraft:wither_skeleton_skull", optional=True),

    quest("f_wither", 15, 4, "&8&lBesiege den Wither",
          subtitle="Drei Schädel, vier Seelensand, ein Netherstern.",
          description=[
              "Stell &64 Seelensand&r als T auf und setz &63 Witherskelettschädel&r obendrauf. Der &cWither&r erscheint, explodiert und fliegt los. Er lässt einen &6Netherstern&r fallen.",
              "",
              "&cWeit weg von jeder Basis&r, am besten tief unter der Erde, wo er sich nicht frei bewegen kann. Ab halber Gesundheit wehrt er Pfeile ab, dann hilft nur das Schwert.",
              "",
              "&eWofür:&r das Leuchtfeuer und der Weckruf für &cThe Harbinger&r (Kapitel &cBosse der Oberwelt&r). Mit Mystical Agradditions lässt er zu 35 Prozent eine &6Verdorrende Seele&r fallen, drei davon ergeben drei neue Schädel.",
          ],
          tasks=[task_item("minecraft:nether_star", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s2_rare"), reward_xp(25)],
          deps=["wither_skull"], icon="minecraft:nether_star", size=1.5, shape="diamond", optional=True),

    # ---- Bastionen -----------------------------------------------------------
    quest("barter", 15, 9, "&eTausch mit einem Piglin",
          subtitle="Wirf einen Barren, sieh, was kommt.",
          description=[
              "Wirf einem &6Piglin&r einen &6Goldbarren&r zu. Nach ein paar Sekunden wirft er dir etwas zurück.",
              "",
              "&eWas es gibt:&r Enderperlen, Feuerresistenz, Obsidian, Weinender Obsidian, Faden, Quarz, Leder, Seelensand, Eisennuggets, Spektralpfeile, selten ein Buch mit Seelenläufer.",
              "",
              "&eTipp:&r Ein Piglin in einem Boot hinter Glas, ein Trichter darunter, und du hast eine kleine Tauschfabrik.",
          ],
          tasks=[task_advancement("minecraft:nether/distract_piglin", "Einen Piglin mit Gold ablenken")],
          rewards=[reward_item("minecraft:ender_pearl", 4)],
          deps=["gold"], icon="minecraft:gold_ingot"),

    quest("bastion", 17.5, 9, "&8&lPlünder eine Bastion",
          subtitle="Die Festung der Piglins.",
          description=[
              "Finde eine &6Bastionsruine&r aus Schwarzstein und bring einen &6Golddurchzogenen Schwarzstein&r mit.",
              "",
              "Drin leben Piglins, die &6Piglin-Barbaren&r (Gold lenkt sie nicht ab) und Hoglins in Ställen. Jede Truhe macht die Piglins wütend, auch mit Goldrüstung.",
              "",
              "In den Truhen: Gold, Diamantausrüstung, Antiker Schrott und die &6Schmiedevorlage&r für Netherit. Dank Lootr hat jeder Spieler seine eigene Beute.",
          ],
          tasks=[task_item("minecraft:gilded_blackstone", 1)],
          rewards=[reward_item("minecraft:gold_block", 2), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["barter"], icon="minecraft:gilded_blackstone", size=1.5, shape="hexagon"),

    quest("debris", 20, 9, "&4&lGrab Antiken Schrott",
          subtitle="Tief unten, feuerfest, jede Mühe wert.",
          description=[
              "Grab auf &eY 15&r lange Tunnel und bau &e4 Antiken Schrott&r ab. Er leuchtet nicht, ist sprengfest und schwimmt als Gegenstand auf Lava.",
              "",
              "Schneller geht es mit TNT: Netherrack fliegt weg, der Schrott bleibt liegen. Abstand halten und gegen Lava sichern.",
              "",
              "Im Ofen wird jeder Block zu einer &6Netheritplatte&r.",
          ],
          tasks=[task_item("minecraft:ancient_debris", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_table("s2_rare"), reward_xp(15)],
          deps=["bastion"], icon="minecraft:ancient_debris", size=1.75, shape="diamond"),

    quest("netherite", 22.5, 9, "&8Schmiede einen Netheritbarren",
          subtitle="Vier Platten, vier Gold, ein Barren.",
          description=[
              "&64 Netheritplatten&r und &64 Goldbarren&r ergeben einen &6Netheritbarren&r. Am Schmiedetisch wird Diamantausrüstung mit Barren und &6Schmiedevorlage&r zu Netherit.",
              "",
              "Die Vorlage liegt in Bastionen. &e7 Diamanten&r, ein Netherrack und eine Vorlage ergeben zwei Vorlagen.",
              "",
              "Netheritrüstung brauchst du für die Bossrüstungen weiter unten.",
          ],
          tasks=[task_item("minecraft:netherite_ingot", 1)],
          rewards=[reward_xp(20)],
          deps=["debris"], icon="minecraft:netherite_ingot", optional=True),

    quest("n_respawn_anchor", 20, 7.5, "&5Bau einen Seelenanker",
          subtitle="Ein Bett, das im Nether nicht explodiert.",
          description=[
              "&66 Weinender Obsidian&r und &63 Leuchtstein&r ergeben einen &6Seelenanker&r. Weinenden Obsidian tauschen dir die Piglins gegen Gold.",
              "",
              "Lade ihn mit Leuchtsteinblöcken auf, bis zu &d4&r Ladungen, und klick ihn an. Stirbst du, wachst du im Nether neben ihm auf, jede Wiedergeburt kostet eine Ladung.",
              "",
              "&cAchtung:&r In der Oberwelt explodiert er beim Benutzen, genau wie ein Bett im Nether.",
          ],
          tasks=[task_item("minecraft:respawn_anchor", 1)],
          rewards=[reward_item("minecraft:glowstone", 8), reward_xp(5)],
          deps=["barter"], icon="minecraft:respawn_anchor"),

    quest("n_piglin_brute", 17.5, 7.5, "&cBesiege einen Piglin-Barbaren",
          subtitle="Ihn beeindruckt kein Gold.",
          description=[
              "Erleg einen &cPiglin-Barbaren&r. Sie bewachen die Bastionen mit goldenen Äxten, greifen dich trotz Goldrüstung an und kommen nicht wieder, wenn sie tot sind.",
              "",
              "&eKronwerke:&r Ab Stufe 2 haben feindliche Mobs &d30 Prozent&r mehr Leben, &d20 Prozent&r mehr Schaden und &d2&r Rüstungspunkte dazu. Ein Barbar haut entsprechend hart zu, geh mit Schild und guter Rüstung.",
          ],
          tasks=[task_kill("minecraft:piglin_brute", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(8)],
          deps=["bastion"], icon="minecraft:golden_axe"),

    quest("n_lava_rod", 22.5, 7.5, "&6Angle in der Lava",
          subtitle="Nether Depths Upgrade: Fische, die im Feuer leben.",
          description=[
              "&63 Lohenruten&r, &62 Netheritplatten&r und &62 Ketten&r ergeben eine &6Lava-Angel&r. Mit ihr angelst du in den Lavaseen des Nethers.",
              "",
              "Was anbeißt, kommt als lebender Fisch heraus: &6Searing Cod&r, &6Bonefish&r, &6Glowdine&r, Lava-Kugelfische und mehr. Manche Arten leben nur in bestimmten Biomen, etwa der &6Soul Sucker&r im Seelensandtal.",
              "",
              "Eine Schere am &6Fortress Grouper&r gibt Platten, am &6Eyeball Fish&r ein Auge. Auge und Lohenstaub ergeben ein Enderauge, ganz ohne Enderperle.",
          ],
          tasks=[task_item("netherdepthsupgrade:lava_fishing_rod", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_xp(5)],
          deps=["debris", "blaze"], icon="netherdepthsupgrade:lava_fishing_rod", optional=True),

    quest("n_netherite_pick", 25, 9, "&8Rüste eine Spitzhacke auf Netherit auf",
          subtitle="Die beste Spitzhacke aus Vanilla.",
          description=[
              "Leg am &6Schmiedetisch&r eine &6Schmiedevorlage&r, eine &6Diamantspitzhacke&r und einen &6Netheritbarren&r ein. Verzauberungen bleiben erhalten.",
              "",
              "Netheritwerkzeug hält länger, baut schneller ab und verbrennt nicht, wenn es in Lava fällt. Kopier die Vorlage, bevor du die letzte verbrauchst.",
          ],
          tasks=[task_item("minecraft:netherite_pickaxe", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["netherite"], icon="minecraft:netherite_pickaxe", optional=True),

    quest("n_lodestone", 25, 7.5, "&8Stell einen Leitstein an dein Portal",
          subtitle="Ein Kompass, der auch im Nether zeigt.",
          description=[
              "&68 Gemeißelte Steinziegel&r um einen &6Netheritbarren&r ergeben einen &6Leitstein&r. Rechtsklick mit einem &6Kompass&r darauf, und er wird zum Leitstein-Kompass.",
              "",
              "Ein normaler Kompass dreht sich im Nether nur im Kreis. Der Leitstein-Kompass zeigt immer zu seinem Leitstein, solange du in derselben Dimension bist. Stell einen neben dein Netherportal, und du findest immer zurück.",
          ],
          tasks=[task_item("minecraft:lodestone", 1)],
          rewards=[reward_item("minecraft:compass", 2), reward_xp(5)],
          deps=["netherite"], icon="minecraft:lodestone", optional=True),

    # ---- Bauwerke ------------------------------------------------------------
    quest("structures", 10, 9, "&6Finde ein Bauwerk von Dungeons and Taverns",
          subtitle="Burgen, Häfen und Türme in jedem Biom.",
          description=[
              "Finde eines dieser Bauwerke und hak ab: &6Netherburg&r (Nether Keep), &6Hafen&r an einem Lavasee, &6Piglin-Donjon&r, Piglin-Außenposten und Piglin-Lager, oder einen &6Skelett-Turm&r.",
              "",
              "Skelett-Türme und Skelett-Lager gibt es in vier Stilen, je nach Biom: Ödnis, Karmesin, Wirr und Seelensand. Alle Truhen sind Lootr-Truhen, also für jeden Spieler neu.",
          ],
          tasks=[task_checkmark("Ein Bauwerk von Dungeons and Taverns gefunden")],
          rewards=[reward_table("s2_common"), reward_xp(10)],
          deps=["biomes"], icon="minecraft:chiseled_polished_blackstone", size=1.5),

    quest("s_formations", 10, 11, "&6Finde ein Bauwerk von Formations Nether",
          subtitle="Kleine Funde überall im Nether.",
          description=[
              "Finde eines der kleinen Bauwerke von &6Formations Nether&r und hak ab.",
              "",
              "&eDarunter:&r Basalthütten, eine Schwarzstein-Burg, Quarzspitzen, Obsidiansäulen, kleine Lava-Arenen und Lavaschreine, ein Netherwarzenfeld, ein Altar mit Seelenanker und ein Kletterparcours. Einige haben Beute.",
          ],
          tasks=[task_checkmark("Ein Bauwerk von Formations Nether gefunden")],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["structures"], icon="minecraft:polished_blackstone_bricks", optional=True),

    # ---- Bosse ---------------------------------------------------------------
    quest("bosses", 10, 15, "&4&lPlan die Bosse des Nethers",
          subtitle="Erst Ignis, dann die Monstrosity.",
          description=[
              "&6L_Ender's Cataclysm&r hat zwei Bosse im Nether. Nimm sie in dieser Reihenfolge: &cIgnis&r (450 Leben) in der &6Burning Arena&r, dann die &cNetherite Monstrosity&r (600 Leben) in der &6Soul Black Smith&r.",
              "",
              "Wie bei allen Cataclysm-Bossen ist Schaden pro Treffer und pro Sekunde gedeckelt, und wer zu weit weg steht, trifft kaum. Zu mehreren fallen sie viel schneller. Die Regeln stehen im Kapitel &cBosse der Oberwelt&r.",
              "",
              "&eKronwerke:&r Ein Bosskampf ist ein guter gemeinsamer Stream-Abend. Wer eine Arena findet, sagt im Chat Bescheid.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(5)],
          deps=["structures"], icon="minecraft:blaze_powder", size=1.5, shape="hexagon"),

    quest("ig_find", 12.5, 14, "&6Finde die Burning Arena",
          subtitle="Ein brennendes Kolosseum in der Netherödnis.",
          description=[
              "Craft ein &6Flammenauge&r und wirf es wie ein Enderauge: oben &63 Lohenstaub&r, Mitte &6Netheritplatte, Enderauge, Netheritplatte&r, unten &63 Seelensand&r.",
              "",
              "Es fliegt zur nächsten &6Burning Arena&r. Die steht nur in der &eNetherödnis&r. Folg ihm, bis du drin bist.",
          ],
          tasks=[task_advancement("cataclysm:find_burning_arena", "Die Burning Arena finden")],
          rewards=[reward_item("minecraft:blaze_powder", 8), reward_xp(10)],
          deps=["bosses"], icon="cataclysm:flame_eye"),

    quest("ig_revenant", 15, 14, "&6Hol Brennende Asche",
          subtitle="Der Ignited Revenant trägt den Schlüssel.",
          description=[
              "Erleg einen &6Ignited Revenant&r in der Arena. Er lässt &6Brennende Asche&r fallen, den Schlüssel für Ignis.",
              "",
              "Er hat &e80 Leben&r und Rüstung 12, schießt brennende Knochen und speit Asche. Schild hoch und dranbleiben.",
              "",
              "&eZweiter Weg:&r 4 &6Sterbende Glut&r ergeben eine Asche. Die Glut lassen Ignited Berserker fallen, und die erscheinen erst, wenn Ignis besiegt ist.",
          ],
          tasks=[task_kill("cataclysm:ignited_revenant", 1), task_item("cataclysm:burning_ashes", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(10)],
          deps=["ig_find"], icon="cataclysm:burning_ashes"),

    quest("ig_kill", 17.5, 14, "&c&lBesiege Ignis",
          subtitle="Asche auf den Altar, und das Feuer steht auf.",
          description=[
              "Leg die &6Brennende Asche&r auf den &6Altar des Feuers&r in der Arena. &cIgnis&r erscheint: &e450 Leben&r, Rüstung 10, schwere Schwertschläge und Feuerbälle.",
              "",
              "Treffer über 20 werden gekappt, mehr als 14 pro Sekunde kommen nicht durch, und ab 15 Blöcken Abstand machst du kaum Schaden. Er heilt sich an seinen Treffern. Feuerresistenz, Goldäpfel und viele Leute.",
              "",
              "&eBeute:&r &e3 Ignitiumbarren&r, mit 10 Prozent eine Schallplatte. Danach erwachen in den Netherfestungen die Ignited Berserker.",
          ],
          tasks=[task_kill("cataclysm:ignis", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s2_rare"), reward_xp(30)],
          deps=["ig_revenant"], icon="cataclysm:ignitium_ingot", size=2.0, shape="diamond"),

    quest("ig_gear", 20, 14, "&6Schmiede Ignitium-Ausrüstung",
          subtitle="Netherit wird zu Ignitium.",
          description=[
              "Die &6Ignitium-Vorlage&r: Netherit-Schmiedevorlage in der Mitte, &64 Lohenstaub&r an den Seiten, &64 Netherziegelblöcke&r in den Ecken. Am Schmiedetisch macht sie mit einem Ignitiumbarren aus Netheritrüstung Ignitiumrüstung.",
              "",
              "&eDie Teile:&r Helm mit Glutmal auf Tastendruck, Brustplatte (später mit Elytra kombinierbar), Hose mit Flammenreflex, Stiefel, mit denen du über Lava gehst.",
              "",
              "&eWaffen:&r &6Bollwerk der Flamme&r (Schild, 2 Ignitium, 2 Lohenruten, 4 Netherziegel), &6Incinerator&r (Netheritschwert, 2 Ignitium, 4 Lohenruten), &6Lodernde Griffe&r (8 Netherziegel um ein Ignitium).",
          ],
          tasks=[task_item("cataclysm:ignitium_upgrade_smithing_template", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 8), reward_xp(10)],
          deps=["ig_kill"], icon="cataclysm:ignitium_helmet", optional=True),

    quest("nm_find", 17.5, 16.5, "&6Finde die Soul Black Smith",
          subtitle="Eine verlassene Schmiede, in der etwas schläft.",
          description=[
              "Craft ein &6Monströses Auge&r: &64 Lavaeimer&r in den Ecken, oben und unten &6Netheritplatte&r, links und rechts &6Schwarzstein&r, ein &6Enderauge&r in der Mitte. Wirf es und folg ihm.",
              "",
              "Die Schmiede steht in Netherödnis, Karmesinwald, Wirrwald oder Seelensandtal. Die Platten holst du aus Antikem Schrott.",
          ],
          tasks=[task_advancement("cataclysm:find_soul_black_smith", "Die Soul Black Smith finden")],
          rewards=[reward_item("minecraft:lava_bucket", 1), reward_xp(10)],
          deps=["ig_kill", "debris"], icon="cataclysm:monstrous_eye"),

    quest("nm_kill", 20, 16.5, "&c&lBesiege die Netherite Monstrosity",
          subtitle="Die Kriegsmaschine des Nethers.",
          description=[
              "Weck die &cNetherite Monstrosity&r in der Schmiede und besiege sie: &e600 Leben&r, Rüstung 12, Lavabomben, Flammenstrahl und Leuchtbomben.",
              "",
              "Kappung: 25 pro Treffer, 20 pro Sekunde, ab 18 Blöcken kaum Schaden. Feuerresistenz ist Pflicht, Netheritrüstung oder Ignitium dringend empfohlen.",
              "",
              "&eBeute:&r die &6Höllenschmiede&r, das &6Monströse Horn&r und &e16 bis 24 Lavazellen&r. Für einen zweiten Kampf nimmt der Boss-Wiederbeleber ein Monströses Auge.",
          ],
          tasks=[task_kill("cataclysm:netherite_monstrosity", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_table("s2_rare"), reward_xp(40)],
          deps=["nm_find"], icon="cataclysm:infernal_forge", size=2.0, shape="diamond"),

    quest("nm_gear", 22.5, 16.5, "&6Nutz die Beute der Monstrosity",
          subtitle="Ein Helm, eine Spitzhacke und ein Haustier.",
          description=[
              "&6Monströser Helm:&r Netherithelm, Monströses Horn und Netherit-Vorlage am Schmiedetisch. Unter halber Gesundheit stößt er alles in der Nähe weg und gibt Verteidigung und Regeneration.",
              "",
              "&6Höllenschmiede:&r eine Spitzhacke, die mit Rechtsklick den Boden sprengt. Mit einem Leerenkern aus dem End wird sie später zur Leerenschmiede.",
              "",
              "&6Netherit-Abbild:&r Netheritbarren, Redstoneblock, Totem, 2 Gold und 4 Netherziegel. Es ruft eine kleine Monstrosity, die du mit Lavazellen zähmst.",
          ],
          tasks=[task_item("cataclysm:monstrous_helm", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_xp(15)],
          deps=["nm_kill"], icon="cataclysm:monstrous_helm", optional=True),

    # ---- Abschluss -----------------------------------------------------------
    quest("supply", 23, 4.5, "&c&lLeg einen Nether-Vorrat an",
          subtitle="Genug für eine ganze Stufe.",
          description=[
              "Bring &e16 Lohenruten&r, &e64 Netherquarz&r und &e32 Leuchtsteinstaub&r zusammen. Das hält eine Weile.",
              "",
              "Ruten für weitere Lohenbrenner und Braustände, Quarz für Elektronenröhren, Leuchtstein für Licht und das Aether-Portal.",
              "",
              "&eKronwerke:&r Das Ziel der Stufe will &e2 000 Messingbarren&r, und jeder Mixer mit Messing braucht einen Lohenbrenner. Wer mehr Lohen fängt, als er braucht, gibt sie weiter.",
          ],
          tasks=[task_item("minecraft:blaze_rod", 16), task_item("minecraft:quartz", 64), task_item("minecraft:glowstone_dust", 32)],
          rewards=[reward_table("s2_rare"), reward_item("minecraft:blaze_rod", 8), reward_xp(20)],
          deps=["blaze_burner", "rose_quartz", "brewing"], icon="minecraft:blaze_powder", size=2.5, shape="gear"),
]

images = [
    banner("nether/title", "Der Nether", 11, -5, height=1.75, kind="title", colour="fire"),
    banner("nether/arrival", "Ankunft", 1.25, -2.6, height=0.9, colour="fire"),
    banner("nether/resources", "Rohstoffe", 8.75, -2.6, height=0.9, colour="fire"),
    banner("nether/fortresses", "Festungen", 17.5, -2.6, height=0.9, colour="fire"),
    banner("nether/biomes", "Biome", 2.5, 7.2, height=0.9, colour="fire"),
    banner("nether/mobs", "Mobs", 2.5, 12.6, height=0.9, colour="fire"),
    banner("nether/structures", "Bauwerke", 10, 7.2, height=0.9, colour="stone"),
    banner("nether/bastions", "Bastionen", 18.75, 7.2, height=0.9, colour="fire"),
    banner("nether/bosses", "Bosse", 16.25, 12.4, height=0.9, colour="fire"),
]

chapter(C, "Der Nether", "minecraft:netherrack", "world", quests, shape="circle", order=8, stage=2,
        subtitle=["Stufe 2: hinein, Rohstoffe, Biome, Festungen, Bastionen und die Bosse Ignis und Netherite Monstrosity."],
        images=images)
