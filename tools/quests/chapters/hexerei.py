"""Hexerei in stage 2 (the whole mod opens with stage 2): the Book of Shadows, the four wild
herbs one by one, the witch woods, the Mixing Cauldron with tallow, candles, blood, potions and
the cauldron crafts, the drying rack, sage and the Pestle and Mortar, every potion a candle can
carry (checklist), the brooms with all brushes and tips, crows and owls. Numbers come from the
recipe jsons, the Book of Shadows text and config/Hexerei-common.toml."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "hexerei"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Hexenkunst ------------------------------------------------------------
    quest("welcome", 0, 0, "&2&lSchlag das Book of Shadows auf",
          subtitle="Hexerei auf die alte Art.",
          description=[
              "&6Buch&r in die Mitte, &e2 Leder&r oben und unten, links etwas Schmelzbares (&6Animal Fat&r, Kerze oder Honigwabe), rechts ein &6Sage Seed&r. Das ist das &6Book of Shadows&r.",
              "Sage Seeds findest du wie Weizensamen beim Abbauen von Gras.",
              "",
              "&2Hexerei&r ist Hexenkunst zum Anfassen: Kräuter sammeln, trocknen, zerstoßen, im Kessel mischen, Kerzen ziehen und auf einem Besen davonfliegen. Die ganze Mod öffnet mit &6Stufe 2&r.",
              "",
              "Im Buch zeigt eine Taste über jedem Item das Rezept in JEI. Lesezeichen setzt du oben links.",
          ],
          tasks=[task_item("hexerei:book_of_shadows", 1)],
          rewards=[reward_item("hexerei:sage_seed", 8), reward_table("s2_common")],
          icon="hexerei:book_of_shadows", size=2.0, shape="hexagon"),

    quest("animal_fat", 2.5, -1.8, "&6Sammel Animal Fat",
          subtitle="Rohstoff für Talg und Kerzen.",
          description=[
              "&6Kühe&r, &6Schweine&r und &6Schafe&r lassen &6Animal Fat&r fallen, Plünderung erhöht die Menge.",
              "",
              "Im beheizten Kessel wird es zu Talg, aus Talg ziehst du Kerzen. Honigwaben und alte Kerzen schmelzen genauso. Wer eine Tierfarm hat, sammelt das Fett nebenbei.",
          ],
          tasks=[task_item("hexerei:animal_fat", 8)],
          rewards=[reward_item("minecraft:leather", 4)],
          deps=["welcome"], icon="hexerei:animal_fat"),

    quest("altar", 2.5, 2.0, "&6Bau einen Altar",
          subtitle="Ein Pult für dein Buch.",
          description=[
              "&e3 Stufen&r oben, &e4 Planken&r darunter als zwei Beine, aus Mahagoni, Weide oder Zaubernuss. Das ist der &6Altar&r.",
              "",
              "Leg das Book of Shadows darauf, dann liest du es im Stehen. Andere Items stellt er aus. Brennende Kerzen in der Nähe schweben um ihn herum.",
          ],
          tasks=[task_item("hexerei:book_of_shadows_altar", 1)],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="hexerei:book_of_shadows_altar", optional=True),

    quest("dowsing", 4.5, -1, "&6Bau eine Dowsing Rod",
          subtitle="Der Weg zum Sumpf.",
          description=[
              "&e5 Stöcke&r um einen &6Laubblock&r ergeben die &6Dowsing Rod&r.",
              "",
              "Schleichend Rechtsklick wechselt zwischen Sumpf und Dschungel, Rechtsklick sucht ein neues Ziel. Gesunde Blätter an der Rute heißen: richtige Richtung. Welke heißen: falsch.",
          ],
          tasks=[task_item("hexerei:dowsing_rod", 1)],
          rewards=[reward_item("minecraft:compass", 1)],
          deps=["welcome"], icon="hexerei:dowsing_rod"),

    quest("selenite", 4.5, 1.2, "&6Brich Selenit ab",
          subtitle="Kristalle unter dem Sumpf.",
          description=[
              "Unter Sümpfen liegen &6Selenit-Geoden&r. Brich die Cluster ab, dann bekommst du &6Selenite Shards&r.",
              "",
              "Selenit wird Sockel für Kerzen und steckt in der Netherit-Spitze für Besen.",
          ],
          tasks=[task_item("hexerei:selenite_shard", 4)],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="hexerei:selenite_shard", optional=True),

    quest("herbs", 6.5, -1, "&2Grab die vier Hexenkräuter aus",
          subtitle="Alraune, Tollkirsche, Beifuß, Ampfer.",
          description=[
              "Im &2Sumpf&r wachsen &6Mandrake&r, &6Belladonna&r, &6Mugwort&r und &6Yellow Dock&r wild. Bau je eine Pflanze ab und nimm sie mit.",
              "",
              pic("hexerei:mandrake_root"),
              "",
              "Setz sie in einen Kräutergarten vor deiner Hütte. Ausgewachsen erntest du sie mit Rechtsklick wie Süßbeeren, dann wachsen sie nach. Die vier Quests rechts sind die Checkliste: was jede Pflanze gibt und wofür.",
          ],
          tasks=[task_item("hexerei:mandrake_plant", 1), task_item("hexerei:belladonna_plant", 1),
                 task_item("hexerei:mugwort_bush", 1), task_item("hexerei:yellow_dock_bush", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["dowsing"], icon="hexerei:mandrake_flowers"),

    quest("herb_mandrake", 8.7, -2.6, "&2Ernte Mandrake",
          subtitle="Wurzel und Blüte.",
          description=[
              "Rechtsklick auf die reife &6Mandrake&r gibt &6Mandrake Root&r und &6Mandrake Flowers&r.",
              "",
              "Die Wurzel steckt in jeder Besenbürste, jedem Besen und dem Krähen-Amulett. Die Blüten brauchst du für die Enhanced und die Moon Dust Brush.",
          ],
          tasks=[task_item("hexerei:mandrake_root", 8), task_item("hexerei:mandrake_flowers", 4)],
          rewards=[reward_item("minecraft:bone_meal", 8)],
          deps=["herbs"], icon="hexerei:mandrake_root"),

    quest("herb_belladonna", 8.7, -1.4, "&5Ernte Belladonna",
          subtitle="Giftige Beeren, nützliche Blüten.",
          description=[
              "Rechtsklick auf die reife &6Belladonna&r gibt &6Belladonna Berries&r und &6Belladonna Flowers&r.",
              "",
              "Im Mörser werden &e5 Beeren&r zu &e4 schwarzem Farbstoff&r. Beeren und Blüten ergeben die Mindful Trance Blend. &cAchtung:&r Roh gegessen sind die Beeren giftig.",
          ],
          tasks=[task_item("hexerei:belladonna_berries", 8), task_item("hexerei:belladonna_flowers", 2)],
          rewards=[reward_item("minecraft:bone_meal", 8)],
          deps=["herbs"], icon="hexerei:belladonna_berries"),

    quest("herb_mugwort", 8.7, -0.2, "&aErnte Mugwort",
          subtitle="Blätter und Blüten.",
          description=[
              "Rechtsklick auf den reifen &6Mugwort&r gibt &6Mugwort Leaves&r und &6Mugwort Flowers&r.",
              "",
              "Die Blätter stecken in der normalen Besenbürste, die Blüten in der Enhanced Brush. Getrocknet gehören beide ins Krähen-Ankh.",
          ],
          tasks=[task_item("hexerei:mugwort_leaves", 4), task_item("hexerei:mugwort_flowers", 2)],
          rewards=[reward_item("minecraft:bone_meal", 8)],
          deps=["herbs"], icon="hexerei:mugwort_flowers"),

    quest("herb_yellow_dock", 8.7, 1.0, "&eErnte Yellow Dock",
          subtitle="Der letzte Busch im Garten.",
          description=[
              "Rechtsklick auf den reifen &6Yellow Dock&r gibt &6Yellow Dock Leaves&r und &6Yellow Dock Flowers&r.",
              "",
              "Wie beim Mugwort: Blätter in die normale Bürste, Blüten in die Enhanced Brush, getrocknet beide ins Krähen-Ankh und in die Replacer Satchel.",
          ],
          tasks=[task_item("hexerei:yellow_dock_leaves", 4), task_item("hexerei:yellow_dock_flowers", 2)],
          rewards=[reward_item("minecraft:bone_meal", 8)],
          deps=["herbs"], icon="hexerei:yellow_dock_flowers"),

    quest("woods", 6.5, 1.2, "&2Fäll Hexenholz",
          subtitle="Weide, Mahagoni und Zaubernuss.",
          description=[
              "&6Willow&r wächst in Sümpfen, &6Mahogany&r im Dschungel und Bambusdschungel, &6Witch Hazel&r im Birkenwald. Fäll von Weide und Mahagoni je 8 Stämme.",
              "",
              "Aus jeder Sorte wird ein eigener Besen. Die Planken brauchst du für Altar, Coffer, Krähenflöte und Kurier-Depots. Nimm Setzlinge mit.",
          ],
          tasks=[task_item("hexerei:willow_log", 8), task_item("hexerei:mahogany_log", 8)],
          rewards=[reward_item("minecraft:iron_axe", 1)],
          deps=["dowsing"], icon="hexerei:willow_log"),

    # ---- Der Mischkessel -------------------------------------------------------
    quest("cauldron", 0.5, 6, "&2&lBau den Mixing Cauldron",
          subtitle="Wo jedes Hexenrezept endet.",
          description=[
              "&e5 Infused Iron&r aus Nature's Aura als U, ein &6Kessel&r in die Mitte, &e2 Fackeln&r oben links und rechts. Das ist der &6Mixing Cauldron&r.",
              "",
              "Er fasst bis zu &b2 Eimer&r Flüssigkeit: Wasser, Lava, Talg, Blut oder Trank. Feste Zutaten wirfst du oben hinein, schiebst sie per Trichter hinein oder legst sie ins Menü. Stimmt alles, mischt er von selbst.",
              "",
              "&eHitze:&r Viele Rezepte wollen Feuer, Lagerfeuer, Magma oder Lava direkt darunter. Bau zwei Kessel, einen mit Wasser und einen beheizten mit Lava.",
          ],
          tasks=[task_item("hexerei:mixing_cauldron", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_item("minecraft:lava_bucket", 1)],
          deps=["welcome"], icon="hexerei:mixing_cauldron", size=1.75, shape="square"),

    quest("tallow", 2.7, 5.2, "&6Schmilz Talg",
          subtitle="Fett wird Flüssigkeit.",
          description=[
              "Kessel mit Wasser füllen, von unten heizen, &e8 Animal Fat&r (oder Kerzen und Honigwaben) hinein. Das Wasser wird flüssiger &6Talg&r.",
              "",
              "Eine Glasflasche füllt eine &6Bottle of Tallow&r ab (250 mB), eine volle Flasche kippt den Talg wieder hinein.",
          ],
          tasks=[task_item("hexerei:tallow_bottle", 2)],
          rewards=[reward_item("minecraft:glass_bottle", 8)],
          deps=["cauldron"], icon="hexerei:tallow_bottle"),

    quest("dipper", 4.7, 5.2, "&6Bau einen Candle Dipper",
          subtitle="Kerzenziehen wie früher.",
          description=[
              "Im Kessel mit Lava: &e5 Eisenbarren&r und &e3 Eisennuggets&r. Heraus kommt der &6Candle Dipper&r.",
              "",
              "Schleichend Rechtsklick setzt ihn oben auf den Kessel. Er hat drei Plätze für je ein Item und taucht es in die Flüssigkeit darunter, bis das Rezept fertig ist.",
          ],
          tasks=[task_item("hexerei:candle_dipper", 1)],
          rewards=[reward_item("minecraft:string", 16)],
          deps=["tallow"], icon="hexerei:candle_dipper"),

    quest("candles", 6.7, 5.2, "&6Zieh acht Kerzen",
          subtitle="Licht und Magie in einem.",
          description=[
              "Talg im Kessel, Dipper darauf, &e3 Fäden&r an den Dipper. Jeder Faden wird mit &e50 mB&r Talg zur &6Kerze&r. Mit leerer Hand nimmst du sie ab.",
              "",
              "Bis zu &e4 Kerzen&r passen in einen Block, angezündet brennen sie etwa &e35 Minuten&r. Mit Planken, Selenit oder einem Redstone-Block im Crafting-Feld bekommen sie einen Sockel.",
          ],
          tasks=[task_item("hexerei:candle", 8)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_xp(5)],
          deps=["dipper"], icon="hexerei:candle"),

    quest("candelabra", 8.7, 5.2, "&6Bau einen Kandelaber",
          subtitle="Kerzen, die nie ausgehen.",
          description=[
              "Im Wasserkessel: eine &6Kette&r, &e4 Kerzen&r, &e3 Eisenbarren&r. Das ist der &6Candelabra&r.",
              "",
              "Anders als einzelne Kerzen geht er nie aus. Er steht auf einem Block oder hängt darunter, auch an Ketten.",
          ],
          tasks=[task_item("hexerei:candelabra", 1)],
          rewards=[reward_item("minecraft:chain", 4)],
          deps=["candles"], icon="hexerei:candelabra", optional=True),

    quest("potion_brew", 8.7, 11.4, "&5Füll einen Trank in den Kessel",
          subtitle="Der Kessel braut und tränkt.",
          description=[
              "Kipp Trankflaschen in einen Kessel (eine Flasche sind &e250 mB&r) oder brau im beheizten Kessel bis zu &e2 Eimer&r Trank auf einmal.",
              "",
              "Steckt eine Kerze im Dipper über einem Trank, taucht er sie &e3 Mal&r ein, &e100 mB&r pro Kerze. Brennend gibt sie den Effekt an alle in der Nähe. Die fünf Quests darunter sind die Checkliste aller Kerzentränke.",
          ],
          tasks=[task_checkmark("Einen Trank in den Kessel gefüllt")],
          rewards=[reward_item("minecraft:glass_bottle", 8), reward_xp(5)],
          deps=["candles"], icon="minecraft:potion"),

    quest("blood", 2.7, 7, "&4Zapf Blut ab",
          subtitle="Ein Opfer, das weh tut.",
          description=[
              "Im beheizten Lavakessel: &e4 Redstone&r und &e4 Polierter Schwarzstein&r ergeben das &6Blood Sigil&r. Leg es in den Sigil-Platz oben links im Kesselmenü.",
              "Spring &edreimal&r in den Kessel, dann ist genug für eine &6Bottle of Blood&r darin. Eine Glasflasche füllt sie ab.",
              "",
              pic("hexerei:blood_bottle"),
              "",
              "Blut ist die Hauptzutat aller Besen. &cAchtung:&r Jeder Sprung kostet Leben, spring nicht halbtot hinein.",
          ],
          tasks=[task_item("hexerei:blood_sigil", 1), task_item("hexerei:blood_bottle", 3)],
          rewards=[reward_item("minecraft:cooked_beef", 8), reward_xp(5)],
          deps=["cauldron"], icon="hexerei:blood_sigil"),

    quest("herb_jar", 4.7, 7, "&6Brenn ein Herb Jar",
          subtitle="1 024 Kräuter in einem Glas.",
          description=[
              "&e8 Sand&r im beheizten Lavakessel ergeben ein &6Herb Jar&r. Es fasst bis zu &e1 024&r Stück einer Sorte.",
              "",
              "&eKronwerke:&r Die Gläser nehmen nur Kräuter (Config). Das Menü öffnest du mit Rechtsklick auf jede Seite außer vorn, vorn schleichend mit leerer Hand. Mit dem Krähen-Knopf sortieren Krähen passende Items hinein.",
          ],
          tasks=[task_item("hexerei:herb_jar", 4)],
          rewards=[reward_item("minecraft:sand", 16)],
          deps=["blood"], icon="hexerei:herb_jar", optional=True),

    quest("coffer", 6.7, 7, "&6Bau eine Coffer",
          subtitle="Eine Truhe für Hexen und Krähen.",
          description=[
              "Im Wasserkessel: &e5 Mahagoniplanken&r und &e3 Goldbarren&r. Das ist die &6Coffer&r.",
              "",
              "Schlagen hebt sie samt Inhalt auf. Ist der Krähen-Knopf im Menü an, bringen sammelnde Krähen alles zu ihr, was schon in der Coffer liegt. Färben und Umbenennen geht wie bei Lederrüstung.",
          ],
          tasks=[task_item("hexerei:coffer", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 3)],
          deps=["herb_jar"], icon="hexerei:coffer", optional=True),

    quest("satchel", 4.7, 8.8, "&6Näh eine Small Satchel",
          subtitle="Gepäck für den Besen.",
          description=[
              "Im Wasserkessel: &e6 Leder&r, ein &6Faden&r, ein &6Goldnugget&r. Die &6Small Satchel&r gibt einem Besen &e9 Plätze&r.",
              "",
              "&6Medium&r (Small Satchel, 6 Leder, Faden) gibt 18, &6Large&r (Small und Medium Satchel, 2 Leder, 4 Fäden) gibt 27. Pack Ersatzbürsten hinein, ohne Bürste fliegt kein Besen.",
          ],
          tasks=[task_item("hexerei:small_satchel", 1)],
          rewards=[reward_item("minecraft:leather", 8)],
          deps=["herb_jar"], icon="hexerei:small_satchel", optional=True),

    quest("witch_armor", 6.7, 8.8, "&5Näh das Hexenkostüm",
          subtitle="Hut, Robe und Stiefel.",
          description=[
              "Im Wasserkessel: &e2 schwarzer Farbstoff&r, &e4 Leder&r, &e2 Fäden&r ergeben &e2 Infused Fabric&r.",
              "Hut aus &e5&r, Robe aus &e7&r, Stiefel aus &e4&r Stoff, geformt wie normale Rüstung. Das sind 16 Stoff, also acht Mischungen.",
              "",
              "Das ganze Set gibt ein paar Vorteile. Jedes Teil lässt sich färben, benannt wechselt es die Farbe.",
          ],
          tasks=[task_item("hexerei:witch_helmet", 1), task_item("hexerei:witch_chestplate", 1),
                 task_item("hexerei:witch_boots", 1)],
          rewards=[reward_item("minecraft:black_dye", 8), reward_xp(5)],
          deps=["coffer"], icon="hexerei:witch_helmet", optional=True),

    quest("crystal_ball", -1.5, 7.5, "&bSchmilz eine Kristallkugel",
          subtitle="Wie steht der Mond?",
          description=[
              "Im beheizten Lavakessel: ein &6Diamant&r, &e6 Glas&r, ein &6Stein&r. Das ist die &6Crystal Ball&r.",
              "",
              "Sie zeigt die Mondphase, tagsüber die Sonne. Praktisch für die Moon Dust Brush, die bei Vollmond am schnellsten fliegt.",
          ],
          tasks=[task_item("hexerei:crystal_ball", 1)],
          rewards=[reward_item("minecraft:glass", 16)],
          deps=["cauldron"], icon="hexerei:crystal_ball", optional=True),

    # ---- Kraeuterkunde ---------------------------------------------------------
    quest("drying_rack", 11, 5.2, "&6Bau ein Drying Rack",
          subtitle="Kräuter brauchen Zeit.",
          description=[
              "Ein &6Faden&r oben, &e2 Stöcke&r und eine &6Holzstufe&r darunter. Das ist das &6Drying Rack&r.",
              "",
              "Drei Plätze mit je bis zu drei Items. Rechtsklick hängt auf, Rechtsklick nimmt Fertiges ab. Trichter füllen und leeren es auch. Verrottetes Fleisch trocknet hier zu &6Leder&r, nasse Schwämme werden trocken.",
          ],
          tasks=[task_item("hexerei:herb_drying_rack", 1)],
          rewards=[reward_item("minecraft:string", 8)],
          deps=["herbs"], icon="hexerei:herb_drying_rack"),

    quest("dried_herbs", 13, 5.2, "&6Trockne Kräuter",
          subtitle="Getrocknet halten sie ewig.",
          description=[
              "Häng &6Mandrake Flowers&r auf. Nach &e100 Sekunden&r sind sie getrocknet. Das gilt für alle Blüten und Blätter der vier Kräuter und für Salbei.",
              "",
              "Getrocknete Kräuter stecken in der Replacer Satchel und im Krähen-Ankh.",
          ],
          tasks=[task_item("hexerei:dried_mandrake_flowers", 4)],
          rewards=[reward_xp(3)],
          deps=["drying_rack"], icon="hexerei:dried_mandrake_flowers"),

    quest("mortar", 15, 5.2, "&6Bau Pestle and Mortar",
          subtitle="Erst zerstoßen, dann zaubern.",
          description=[
              "Im beheizten Lavakessel: &e5 Stein&r, &e2 Eisenbarren&r, ein &6Netherquarz&r.",
              "",
              "Rechtsklick legt ein Item hinein, schleichend einen Stapel. Sind alle Zutaten eines Rezepts drin, zerstößt er sie von selbst und du kannst nichts mehr herausnehmen. Fünf Belladonna-Beeren werden so zu vier schwarzen Farbstoffen.",
          ],
          tasks=[task_item("hexerei:pestle_and_mortar", 1)],
          rewards=[reward_item("minecraft:quartz", 8)],
          deps=["dried_herbs"], icon="hexerei:pestle_and_mortar"),

    quest("mindful_blend", 17, 5.2, "&6Misch die Mindful Trance Blend",
          subtitle="Kräuter für die Kerze.",
          description=[
              "Im Mörser: &6Belladonna Flowers&r, &e3 Belladonna Berries&r, &6Sage&r.",
              "",
              "Formlos mit einer Kerze gecraftet bekommt die Kerze den Effekt &aWachstum&r. Brennend lässt sie Pflanzen in der Nähe schneller wachsen.",
          ],
          tasks=[task_item("hexerei:mindful_trance_blend", 1)],
          rewards=[reward_xp(3)],
          deps=["mortar"], icon="hexerei:mindful_trance_blend", optional=True),

    quest("sage", 11, 7, "&2Bau Salbei an",
          subtitle="Das Kraut gegen Monster.",
          description=[
              "&6Sage Seeds&r pflanzt du auf Ackerland wie Weizen. Reif gibt die Pflanze &6Sage&r und neue Samen.",
              "",
              pic("hexerei:sage"),
              "",
              "Gebündelt, getrocknet und angezündet hält Salbei Monster fern. Außerdem steckt er in der Mindful Trance Blend.",
          ],
          tasks=[task_item("hexerei:sage", 16)],
          rewards=[reward_item("hexerei:sage_seed", 16)],
          deps=["drying_rack"], icon="hexerei:sage"),

    quest("sage_bundle", 13, 7, "&6Bind und trockne ein Salbeibündel",
          subtitle="Brennstoff für die Räucherplatte.",
          description=[
              "&e8 Sage&r um einen &6Faden&r ergeben ein &6Sage Bundle&r. Häng es auf das Drying Rack, nach &e200 Sekunden&r ist es ein &6Dried Sage Bundle&r.",
          ],
          tasks=[task_item("hexerei:dried_sage_bundle", 2)],
          rewards=[reward_item("minecraft:string", 8)],
          deps=["sage"], icon="hexerei:dried_sage_bundle"),

    quest("sage_plate", 15, 7, "&2&lStell eine Sage Burning Plate auf",
          subtitle="Keine Monster rund ums Haus.",
          description=[
              "Im beheizten Lavakessel: &e8 Goldbarren&r. Rechtsklick mit einem &6Dried Sage Bundle&r legt es auf die Platte, ein Feuerzeug zündet es an.",
              "",
              "Solange es brennt, spawnen im Umkreis von &e48 Blöcken&r keine Monster natürlich. Rechtsklick mit leerer Hand stellt den Rauch um, ein Modus zeigt die Reichweite.",
              "",
              "&eTipp:&r Eine Platte in der Mitte eurer Siedlung schützt gleich mehrere Häuser.",
          ],
          tasks=[task_item("hexerei:sage_burning_plate", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["sage_bundle"], icon="hexerei:sage_burning_plate", size=1.5, shape="diamond"),

    quest("seed_mixture", 17, 7, "&6Misch Seed Mixture",
          subtitle="Ein Leckerbissen für Krähen.",
          description=[
              "Im Mörser: je ein &6Weizen-, Kürbis-, Melonen-&r und &6Rote-Bete-Samen&r und ein &6Sage Seed&r.",
              "",
              "Die &6Seed Mixture&r ist das Lieblingsfutter der Krähen und der Weg, sie zu zähmen.",
          ],
          tasks=[task_item("hexerei:seed_mixture", 4)],
          rewards=[reward_item("minecraft:wheat_seeds", 16)],
          deps=["mortar"], icon="hexerei:seed_mixture"),

    # ---- Kerzentraenke (Checkliste) --------------------------------------------
    quest("candle_combat", 10.7, 11.4, "&cTränk Kerzen für den Kampf",
          subtitle="Stärke, Regeneration, Heilung.",
          description=[
              "&eStärke&r: Trank der Stärke. &eRegeneration&r: Trank der Regeneration. &eSofortheilung&r: Trank der Heilung.",
              "",
              "Stell sie dort auf, wo ihr kämpft oder euch sammelt: an der Afrit-Arena, am Boss-Spawn, in der Farm.",
          ],
          tasks=[task_checkmark("Eine Kampfkerze getränkt")],
          rewards=[reward_item("hexerei:candle", 4)],
          deps=["potion_brew"], icon="minecraft:blaze_powder"),

    quest("candle_move", 12.7, 11.4, "&bTränk Kerzen für Bewegung",
          subtitle="Tempo, Sprungkraft, Sanfter Fall.",
          description=[
              "&eTempo&r: Trank der Schnelligkeit. &eSprungkraft&r: verstärkter Sprungtrank (Stufe II). &eSanfter Fall&r: Trank des sanften Falls.",
              "",
              "Eine Sanfter-Fall-Kerze am Rand einer hohen Baustelle rettet Leben.",
          ],
          tasks=[task_checkmark("Eine Bewegungskerze getränkt")],
          rewards=[reward_item("minecraft:sugar", 8)],
          deps=["potion_brew"], icon="minecraft:sugar"),

    quest("candle_senses", 14.7, 11.4, "&eTränk Kerzen für Wasser und Feuer",
          subtitle="Feuerresistenz und Wasseratmung.",
          description=[
              "&eFeuerresistenz&r: Trank der Feuerresistenz. &eWasseratmung&r: Trank der Unterwasseratmung.",
              "",
              "Die Feuerkerze gehört neben die Lava-Kessel und ins Nether-Lager, die Wasserkerze an die Unterwasserbaustelle. Eine Nachtsicht-Kerze gibt es in dieser Version nicht, ihr Rezept macht ebenfalls Wasseratmung.",
          ],
          tasks=[task_checkmark("Eine Feuer- oder Wasserkerze getränkt")],
          rewards=[reward_item("minecraft:magma_cream", 2)],
          deps=["potion_brew"], icon="minecraft:magma_cream"),

    quest("candle_luck", 16.7, 11.4, "&aTränk eine Sonnenkerze",
          subtitle="Regen, Regen, geh weg.",
          description=[
              "&eSonnenschein&r: Dickflüssiger Trank (Wasserflasche plus Glowstonestaub). &eGlück&r: Trank des Glücks.",
              "",
              "Die Sonnenkerze hat einen eigenen Hexerei-Effekt gegen Regen. Den Glückstrank kann man nicht brauen, er stammt nur aus Truhen oder anderen Mods.",
          ],
          tasks=[task_checkmark("Eine Sonnen- oder Glückskerze getränkt")],
          rewards=[reward_item("minecraft:glowstone_dust", 8)],
          deps=["potion_brew"], icon="minecraft:glowstone_dust"),

    quest("candle_harm", 18.7, 11.4, "&4Tränk Kerzen gegen Feinde",
          subtitle="Gift, Langsamkeit, Schaden.",
          description=[
              "&eGift&r: Trank der Vergiftung. &eLangsamkeit&r: Trank der Langsamkeit. &eSofortschaden&r: Trank des Schadens.",
              "",
              "&cAchtung:&r Die Kerze wirkt auf alle in der Nähe, auch auf dich. Stell sie in eine Mobfalle, nicht ins Wohnzimmer.",
          ],
          tasks=[task_checkmark("Eine Fallenkerze getränkt")],
          rewards=[reward_item("minecraft:fermented_spider_eye", 2)],
          deps=["potion_brew"], icon="minecraft:fermented_spider_eye", optional=True),

    # ---- Besen -----------------------------------------------------------------
    quest("broom_brush", 0.5, 15.5, "&6Binde eine Besenbürste",
          subtitle="Ohne Bürste kein Flug.",
          description=[
              "Im Wasserkessel: &e2 Mandrake Roots&r, &e4 Weizen&r, &6Mugwort Leaves&r, &6Yellow Dock Leaves&r ergeben eine &6Wet Broom Brush&r.",
              "Auf dem Drying Rack trocknet sie in &e50 Sekunden&r zur &6Broom Brush&r.",
              "",
              "Jeder neue Besen hat schon eine Bürste. Sie hält &e100&r Haltbarkeit und nutzt sich beim Fliegen ab. Haltbarkeit und Reparatur lassen sich auf Bürsten verzaubern.",
          ],
          tasks=[task_item("hexerei:broom_brush", 2)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["cauldron"], icon="hexerei:broom_brush"),

    quest("willow_broom", 2.8, 15.5, "&2&lFlieg mit einem Weidenbesen",
          subtitle="Flieg!",
          description=[
              "Im Wasserkessel: &6Bottle of Blood&r, &e2 Willow Logs&r, &e2 Goldblöcke&r, &e2 Weizen&r, eine &6Mandrake Root&r.",
              "",
              "Setz den Besen ab wie ein Boot, Rechtsklick setzt dich darauf. Er ist der langsamste, gut zum Bauen. Schleichend Rechtsklick öffnet drei Plätze: Zubehör, Satchel, Bürste.",
              "",
              "&eTipp:&r Im &eSchwebemodus&r bleibt der Besen in der Luft, wenn du absteigst. Ohne ihn gleitet er mit dir zu Boden.",
          ],
          tasks=[task_item("hexerei:willow_broom", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["broom_brush", "blood"], icon="hexerei:willow_broom", size=2.0, shape="diamond"),

    quest("enhanced_brush", 5.2, 14.6, "&6Binde eine Enhanced Brush",
          subtitle="Doppelt so lange in der Luft.",
          description=[
              "Im Wasserkessel (1 500 mB): deine &6Broom Brush&r, &6Belladonna Flowers&r und &6Berries&r, &e2 Mandrake Roots&r, &6Mandrake&r-, &6Mugwort&r- und &6Yellow Dock Flowers&r.",
              "Auf dem Drying Rack trocknet sie in &e2 Minuten&r.",
              "",
              "Sie hält &e200&r statt 100, also doppelt so lange.",
          ],
          tasks=[task_item("hexerei:herb_enhanced_broom_brush", 1)],
          rewards=[reward_xp(5)],
          deps=["willow_broom"], icon="hexerei:herb_enhanced_broom_brush", optional=True),

    quest("moon_brush", 7.6, 13.9, "&9Binde eine Moon Dust Brush",
          subtitle="Schneller, vor allem bei Vollmond.",
          description=[
              "&6Mondstaub:&r &e4 Redstone&r und &e4 Glowstonestaub&r im Wasserkessel ergeben &e4 Moon Dust&r.",
              "&6Bürste:&r Enhanced Brush, &e4 Moon Dust&r, &e2 Mandrake Roots&r, &6Mandrake Flowers&r im Wasserkessel, dann 60 Sekunden trocknen.",
              "",
              "Sie hält wie die Enhanced Brush &e200&r, macht den Besen aber schneller, am meisten bei Vollmond.",
          ],
          tasks=[task_item("hexerei:moon_dust_brush", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["enhanced_brush"], icon="hexerei:moon_dust_brush", optional=True),

    quest("witch_hazel_broom", 5.2, 16.4, "&2Bau einen Zaubernussbesen",
          subtitle="Der goldene Mittelweg.",
          description=[
              "Im Wasserkessel: ein &6Diamant&r, &e2 Witch Hazel Logs&r, &e2 Bottles of Blood&r, &e2 Weizen&r, eine &6Mandrake Root&r.",
              "",
              "Schneller als Weide, langsamer als Mahagoni, und ohne Netherit.",
          ],
          tasks=[task_item("hexerei:witch_hazel_broom", 1)],
          rewards=[reward_item("minecraft:diamond", 1)],
          deps=["willow_broom"], icon="hexerei:witch_hazel_broom", optional=True),

    quest("mahogany_broom", 7.6, 15.5, "&2&lBau einen Mahagonibesen",
          subtitle="Der schnellste Besen am Himmel.",
          description=[
              "Im Wasserkessel: ein &6Netheritbarren&r, &e2 Mahogany Logs&r, &e2 Bottles of Blood&r, &e2 Weizen&r, eine &6Mandrake Root&r.",
              "",
              "Der schnellste der drei. Als Item ist er feuerfest wie Netherit. Beim Fliegen durch Lava schützt dich das nicht, dafür gibt es die Netherit-Spitze.",
          ],
          tasks=[task_item("hexerei:mahogany_broom", 1)],
          rewards=[reward_table("s2_rare"), reward_xp(10)],
          deps=["willow_broom"], icon="hexerei:mahogany_broom", size=1.5, shape="diamond"),

    quest("broom_tips", 9.8, 15.5, "&6Steck eine Spitze an den Besen",
          subtitle="Durch Lava oder unter Wasser.",
          description=[
              "&6Netherite Tip:&r Selenit, &e3 Netheritbarren&r, &e4 Netheritschrott&r im beheizten Kessel mit &e2 Eimern Lava&r. Fliegt durch Lava und Feuer, &e200&r Haltbarkeit.",
              "&6Waterproof Tip:&r Aquisitor, &e4 dunkler Prismarin&r, &e2 Prismarinscherben&r, Prismarin im Wasserkessel. Du bleibst unter Wasser sitzen, &e800&r Haltbarkeit.",
              "Beide gehören in den Zubehörplatz.",
          ],
          tasks=[task_checkmark("Eine Besenspitze gebaut")],
          rewards=[reward_item("minecraft:prismarine_shard", 8)],
          deps=["mahogany_broom"], icon="hexerei:broom_netherite_tip", optional=True),

    # ---- Vertraute -------------------------------------------------------------
    quest("crow", 19, 7, "&8Zähm eine Krähe",
          subtitle="Klein, schwarz und hilfsbereit.",
          description=[
              "Krähen leben in Wäldern. Wirf &6Seed Mixture&r auf den Boden, dann fliegen sie herbei, und die Chance ist höher als beim Füttern aus der Hand. Bau dazu die &6Crow Flute&r: &e3 Mahagoniplanken&r und &e2 Farbstoffe&r.",
              "",
              pic("hexerei:crow_flute"),
              "",
              "Rechtsklick wechselt den Befehl: Folgen, Sitzen, Umherstreifen, Helfen. Beim Helfen sammelt die Krähe Items in Coffer oder Herb Jar, erntet Felder oder stiehlt Dorfbewohnern etwas (alle 90 Sekunden).",
              "",
              "Die Flöte steuert alle Krähen in der Nähe oder bis zu 9 ausgewählte und setzt Schlafplätze.",
          ],
          tasks=[task_item("hexerei:crow_flute", 1)],
          rewards=[reward_item("hexerei:seed_mixture", 8), reward_xp(5)],
          deps=["seed_mixture"], icon="hexerei:crow_flute", size=1.5),

    quest("crow_amulet", 21, 7, "&6Schmied ein Krähen-Amulett",
          subtitle="Schmuck, der Leben rettet.",
          description=[
              "Im beheizten Lavakessel: eine &6Mandrake Root&r, &e5 Goldnuggets&r, &e2 Goldbarren&r. Das &6Crow Blank Amulet&r legst du einer Krähe um.",
              "",
              "In einem Kessel mit &e250 mB&r Regenerationstrank wird es mit getrockneten Mugwort- und Yellow-Dock-Kräutern, &e2 Leuchtbeeren&r und einem &6Totem der Unsterblichkeit&r zum &6Crow Ankh Amulet&r. Das rettet deine Krähe wie ein Totem.",
          ],
          tasks=[task_item("hexerei:crow_blank_amulet", 1)],
          rewards=[reward_item("minecraft:gold_nugget", 18)],
          deps=["crow"], icon="hexerei:crow_blank_amulet", optional=True),

    quest("owl", 21, 5.2, "&6Schick Eulenpost",
          subtitle="Briefe und Pakete für Freunde.",
          description=[
              "Eulen leben im Dunklen Eichenwald. Zähm sie mit rohem &6Kabeljau&r oder &6Lachs&r, am besten auf den Boden geworfen.",
              "&6Courier Package:&r 4 Papier und eine Holzstufe, fasst &e5 Items&r. &6Courier Letter:&r Papier und Tintenbeutel. Versiegeln, auf die Eule klicken, Empfänger wählen.",
              "",
              "Empfänger ist ein Spieler oder ein &6Courier Depot&r, der Briefkasten aus Hexerei-Planken. Auf einem Server mit vielen Basen der schönste Weg, Freunden etwas zu schicken.",
          ],
          tasks=[task_item("hexerei:courier_package", 1), task_item("hexerei:willow_courier_depot", 1)],
          rewards=[reward_item("minecraft:cod", 8), reward_xp(5)],
          deps=["crow"], icon="hexerei:courier_package", optional=True),

    # ---- Ziel ------------------------------------------------------------------
    quest("witch_house", 21, 8.8, "&2&lRichte ein Hexenhaus ein",
          subtitle="Kerzen, Kräuter, ein Besen an der Tür.",
          description=[
              "Halte &e16 Kerzen&r und &e4 getrocknete Salbeibündel&r bereit. Dann ist deine Hütte fertig: Kräuter am Rack, Kessel am Dampfen, Salbei gegen Monster, Krähen beim Aufräumen.",
              "",
              "Hexerei hat keinen Platz im Stufenziel. Aber wer schnell fliegt, ist bei jedem Transport vorne, und Kerzen mit Regeneration oder Tempo helfen bei jeder Gemeinschaftsfarm.",
          ],
          tasks=[task_item("hexerei:candle", 16), task_item("hexerei:dried_sage_bundle", 4)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["sage_plate", "broom_tips", "crow_amulet"], icon="hexerei:mixing_cauldron", size=2.5, shape="gear"),

    # ---- Neue Quests -------------------------------------------------------------
    quest("woodcutter", 6.5, 2.6, "&6Bau einen Woodcutter",
          subtitle="Die Steinsäge für Holz.",
          description=[
              "Ein &6Eisenbarren&r oben, darunter Planke, &6Andesit&r, Planke. Die Planken bestimmen die Sorte: Weide, Mahagoni oder Zaubernuss.",
              "",
              "Er schneidet Holz und Planken wie eine Steinsäge: verbundene Plankenmuster, die es nur hier gibt, und Treppen, Stufen und mehr mit weniger Verschnitt als an der Werkbank.",
          ],
          tasks=[task_item("hexerei:willow_woodcutter", 1)],
          rewards=[reward_item("hexerei:willow_planks", 16), reward_xp(3)],
          deps=["woods"], icon="hexerei:willow_woodcutter", optional=True),

    quest("book_of_colors", 4.5, 2.6, "&dMal im Book of Colors",
          subtitle="Eigene Bilder an der Wand.",
          description=[
              "&6Buch&r in die Mitte, &e2 Leder&r oben und unten, &e4 Farbstoffe&r in die Ecken, links &6Belladonna Berries&r, rechts etwas Schmelzbares wie Animal Fat oder eine Kerze.",
              "",
              "Im Buch malst du auf den Seiten, auf dem Altar oder in der Hand. Eine &6Canvas&r (ein &6Gemälde&r, &e4 Dried Sage&r drumherum) überträgt einen Ausschnitt: Rechtsklick auf ein Bild im Buch, Bereich ziehen, Fenster schließen. Dann hängst du sie auf wie ein Gemälde.",
              "",
              "Schilder für Shops, Wappen für die Basis, ein Porträt der Krähe: alles selbst gemalt.",
          ],
          tasks=[task_item("hexerei:book_of_colors", 1), task_item("hexerei:book_canvas", 1)],
          rewards=[reward_item("minecraft:painting", 2), reward_xp(3)],
          deps=["herb_belladonna", "dried_herbs"], icon="hexerei:book_of_colors", optional=True),

    quest("large_satchel", 2.7, 8.8, "&6Näh eine Large Satchel",
          subtitle="27 Plätze am Besen.",
          description=[
              "&6Medium Satchel:&r Small Satchel, &e6 Leder&r und ein &6Faden&r im Wasserkessel (500 mB). &6Large Satchel:&r Small und Medium Satchel, &e2 Leder&r, &e4 Fäden&r, ebenfalls Wasser.",
              "",
              "Die große Tasche gibt dem Besen &e27 Plätze&r. Sie kommt in den Satchel-Platz, also nur eine Tasche pro Besen.",
          ],
          tasks=[task_item("hexerei:large_satchel", 1)],
          rewards=[reward_item("minecraft:leather", 8), reward_xp(4)],
          deps=["satchel"], icon="hexerei:large_satchel", optional=True),

    quest("replacer_satchel", 0.5, 16.6, "&6Misch eine Replacer Satchel",
          subtitle="Die Bürste wechselt sich selbst.",
          description=[
              "Im Kessel mit &e1 000 mB&r Dickflüssigem Trank (Wasserflasche plus Glowstonestaub): eine &6Medium Satchel&r, getrocknete &6Mandrake-, Belladonna-, Mugwort-&r und &6Yellow-Dock-Blüten&r, eine &6Broom Brush&r und &e2 Enderperlen&r.",
              "",
              "So groß wie die Medium Satchel. Bricht die aktive Bürste, setzt der Besen die Bürste oben links aus der Tasche ein. Auf langen Flügen fällst du nie wieder vom Himmel.",
          ],
          tasks=[task_item("hexerei:replacer_satchel", 1)],
          rewards=[reward_item("hexerei:broom_brush", 2), reward_xp(5)],
          deps=["willow_broom", "dried_herbs"], icon="hexerei:replacer_satchel"),

    quest("ender_satchel", 2.8, 16.6, "&5Misch eine Ender Satchel",
          subtitle="Der Besen trägt deine Endertruhe.",
          description=[
              "Im beheizten Kessel mit &e500 mB Lava&r: eine &6Medium Satchel&r, &e6 Obsidian&r und ein &6Enderauge&r.",
              "",
              "Öffnest du das Besen-Inventar, öffnet sich deine Endertruhe. Was du unterwegs findest, liegt damit gleich sicher zu Hause.",
          ],
          tasks=[task_item("hexerei:ender_satchel", 1)],
          rewards=[reward_item("minecraft:obsidian", 6), reward_xp(5)],
          deps=["willow_broom"], icon="hexerei:ender_satchel", optional=True),

    quest("broom_whistle", 9.8, 16.6, "&6Schnitz eine Besenpfeife",
          subtitle="Der Besen kommt, wenn du rufst.",
          description=[
              "&6Steinknopf&r oben in der Mitte, &e3 Mahagoniplanken&r rechts davon und darunter, &6Bambus&r unten links. Das ist die &6Broom Whistle&r.",
              "",
              "Leg Pfeife und Besen zusammen ins Crafting-Feld, dann ist sie gebunden. Rechtsklick ruft den Besen herbei, wenn er in Reichweite ist. Noch einmal allein ins Crafting-Feld gelegt löst sie die Bindung.",
          ],
          tasks=[task_item("hexerei:broom_whistle", 1)],
          rewards=[reward_item("minecraft:bamboo", 8), reward_xp(3)],
          deps=["willow_broom"], icon="hexerei:broom_whistle", optional=True),

    quest("broom_seat", 7.6, 16.6, "&6Bau einen Besensitz",
          subtitle="Zu zweit fliegen.",
          description=[
              "&6Infused Fabric Block:&r eine &6Infused Fabric&r und &e7 Wolle&r im Wasserkessel (250 mB), gibt acht.",
              "&6Broom Seat:&r Small Satchel, &e2 Fäden&r, &e3 Leder&r, &e2 Infused Fabric Blocks&r im Wasserkessel (500 mB).",
              "",
              "Der Sitz kommt in den Satchel-Platz. Ein zweiter Spieler kann aufsteigen und mitfliegen. Sitzt du allein, sitzt du darauf und schaust nach vorn.",
          ],
          tasks=[task_item("hexerei:broom_seat", 1)],
          rewards=[reward_item("minecraft:white_wool", 8), reward_xp(4)],
          deps=["willow_broom", "witch_armor"], icon="hexerei:broom_seat", optional=True),

    quest("entangled_coffer", 8.7, 7.0, "&5Verschränk zwei Coffers",
          subtitle="Zwei Truhen, ein Inhalt.",
          description=[
              "Im beheizten Kessel mit &e1 000 mB&r Trank der Schnelligkeit: eine &6Coffer&r, eine &6Echoscherbe&r, &e2 Enderaugen&r, &e4 Moon Dust&r. Heraus kommen &e2&r Entangled Coffers.",
              "",
              "Beide teilen sich ein Inventar, egal wo sie stehen. Eine in die Basis, eine an die Farm oder zum Nachbarn: Was du in die eine legst, liegt auch in der anderen.",
          ],
          tasks=[task_item("hexerei:entangled_coffer", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_table("s2_common"), reward_xp(8)],
          deps=["coffer", "moon_brush"], icon="hexerei:entangled_coffer", optional=True),

    quest("crow_ankh", 23, 7, "&6Weih ein Crow Ankh Amulet",
          subtitle="Ein Totem für deine Krähe.",
          description=[
              "Kessel mit &e250 mB&r Trank der Regeneration: das &6Crow Blank Amulet&r, getrocknete &6Mugwort-&r und &6Yellow-Dock&r-Blätter und Blüten, &e2 Leuchtbeeren&r, ein &6Totem der Unsterblichkeit&r.",
              "",
              "Leg es deiner Krähe um. Würde sie sterben, rettet das Amulett sie wie ein Totem.",
          ],
          tasks=[task_item("hexerei:crow_ankh_amulet", 1)],
          rewards=[reward_item("minecraft:glow_berries", 8), reward_xp(5)],
          deps=["crow_amulet", "dried_herbs"], icon="hexerei:crow_ankh_amulet", optional=True),
]

images = [
    banner("hexerei/title", "Hexerei", 4.5, -4.6, height=1.8, kind="title", colour="magic"),
    banner("hexerei/hexenkunst", "Hexenkunst", 4.5, -2.8, height=0.9, colour="magic"),
    banner("hexerei/kessel", "Der Mischkessel", 3.7, 3.6, height=0.9, colour="magic"),
    banner("hexerei/kraeuter", "Kräuterkunde", 14, 3.6, height=0.9, colour="nature"),
    banner("hexerei/kerzen", "Kerzentränke", 12.7, 10.2, height=0.8, colour="fire"),
    banner("hexerei/besen", "Besen", 5.2, 12.6, height=0.9, colour="magic"),
    banner("hexerei/vertraute", "Vertraute", 20, 3.6, height=0.9, colour="magic"),
]

chapter(C, "Hexerei", "hexerei:mixing_cauldron", "magic", quests, shape="circle", order=16, stage=2,
        subtitle=["Stufe 2. Kräuter, Kessel, Kerzen und Besen."], images=images)
