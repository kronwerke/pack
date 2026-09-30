"""Hexerei in stage 2 (the whole mod opens with stage 2): the Book of Shadows, herbs and the witch
woods, the Mixing Cauldron with tallow, candles, blood and the useful cauldron crafts, the drying
rack, sage and the Pestle and Mortar, the three brooms and their brushes, crows and owls."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "hexerei"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Hexenkunst ------------------------------------------------------------
    quest("welcome", 0, 0, "&2Book of Shadows",
          subtitle="Hexerei auf die alte Art.",
          description=[
              "&2Hexerei&r ist Hexenkunst zum Anfassen: Kräuter sammeln, trocknen, zerstoßen, im Kessel mischen, Kerzen ziehen und am Ende auf einem Besen davonfliegen. Die ganze Mod öffnet mit &6Stufe 2&r.",
              "",
              "Dein Handbuch ist das &6Book of Shadows&r. Du craftest es aus einem &6Buch&r, &e2 Leder&r, einem &6Sage Seed&r und etwas Schmelzbarem für Talg: &6Animal Fat&r, eine Kerze oder eine Honigwabe. Sage Seeds findest du wie Weizensamen beim Abbauen von Gras.",
              "",
              "Leg das Buch auf einen &6Altar&r, dann kannst du stehend darin blättern. Über jedem Item im Buch zeigt dir eine Taste das Rezept in JEI.",
          ],
          tasks=[task_item("hexerei:book_of_shadows", 1)],
          rewards=[reward_item("hexerei:sage_seed", 8), reward_table("s2_common")],
          icon="hexerei:book_of_shadows", size=2.0, shape="hexagon"),

    quest("animal_fat", 2.5, -1, "&6Animal Fat",
          subtitle="Rohstoff für Talg und Kerzen.",
          description=[
              "&6Animal Fat&r lassen &6Kühe&r, &6Schweine&r und &6Schafe&r fallen, Plünderung erhöht die Menge. Im Mischkessel wird es zu &6Talg&r geschmolzen, und aus Talg ziehst du Kerzen.",
              "",
              "&eTipp:&r Wer ohnehin eine Tierfarm betreibt, sammelt das Fett nebenbei. Honigwaben und alte Kerzen lassen sich genauso zu Talg schmelzen.",
          ],
          tasks=[task_item("hexerei:animal_fat", 8)],
          rewards=[reward_item("minecraft:leather", 4)],
          deps=["welcome"], icon="hexerei:animal_fat"),

    quest("altar", 2.5, 1.2, "&6Altar",
          subtitle="Ein Pult für dein Buch.",
          description=[
              "Der &6Altar&r ist ein Pult aus &e3 Stufen&r und &e4 Planken&r aus Mahagoni, Weide oder Zaubernuss. Leg das Book of Shadows darauf, und es liegt offen zum Lesen da. Schleichend mit Rechtsklick nimmst du es wieder mit.",
              "",
              "Andere Items stellt der Altar schön aus, und brennende Kerzen in der Nähe schweben um ihn herum. Ein echter Blickfang für die Hexenhütte.",
          ],
          tasks=[task_item("hexerei:book_of_shadows_altar", 1)],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="hexerei:book_of_shadows_altar", optional=True),

    quest("dowsing", 4.5, -1, "&6Dowsing Rod",
          subtitle="Der Weg zum Sumpf.",
          description=[
              "Die Kräuter und Bäume von Hexerei wachsen vor allem in &2Sümpfen&r und &2Dschungeln&r. Die &6Dowsing Rod&r aus &e5 Stöcken&r und einem &6Laubblock&r findet sie für dich.",
              "",
              "Schleichend mit Rechtsklick wechselst du zwischen Sumpf und Dschungel, ein normaler Rechtsklick sucht ein neues Ziel. Sehen die Blätter an der Rute gesund aus, gehst du in die richtige Richtung, werden sie welk, bist du falsch.",
          ],
          tasks=[task_item("hexerei:dowsing_rod", 1)],
          rewards=[reward_item("minecraft:compass", 1)],
          deps=["welcome"], icon="hexerei:dowsing_rod"),

    quest("herbs", 6.5, -1, "&2Wilde Kräuter",
          subtitle="Alraune, Tollkirsche, Beifuß und Ampfer.",
          description=[
              "Vier Kräuter wachsen wild: &6Mandrake&r (Alraune), &6Belladonna&r (Tollkirsche), &6Mugwort&r (Beifuß) und &6Yellow Dock&r (Krauser Ampfer). Du findest sie vor allem in Sümpfen und Dschungeln.",
              "",
              pic("hexerei:mandrake_root"),
              "",
              "Ausgewachsene Pflanzen erntest du mit Rechtsklick wie Süßbeeren, dann wachsen sie nach. Je nach Pflanze gibt es Blüten, Blätter, Wurzeln oder Beeren. Grab dir ein paar Pflanzen aus und setz sie in einen Kräutergarten vor deiner Hütte.",
              "",
              "&cAchtung:&r Belladonna ist giftig. Iss die Beeren nicht roh.",
          ],
          tasks=[task_item("hexerei:mandrake_root", 4), task_item("hexerei:belladonna_berries", 4),
                 task_item("hexerei:mugwort_flowers", 4), task_item("hexerei:yellow_dock_flowers", 4)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["dowsing"], icon="hexerei:mandrake_flowers"),

    quest("woods", 6.5, 1.2, "&2Hexenhölzer",
          subtitle="Weide, Mahagoni und Zaubernuss.",
          description=[
              "Drei Holzsorten gehören zu Hexerei: &6Willow&r (Weide) wächst in Sümpfen, &6Mahogany&r in Dschungeln und &6Witch Hazel&r (Zaubernuss) in Birkenwäldern. Aus jeder Sorte wird später ein eigener Besen.",
              "",
              "Die Stämme brauchst du für die Besen, die Planken für Altar, Truhen, Kurier-Depots und die Hexenflöte. Nimm Setzlinge mit, dann musst du nicht jedes Mal in den Sumpf.",
          ],
          tasks=[task_item("hexerei:willow_log", 8), task_item("hexerei:mahogany_log", 8)],
          rewards=[reward_item("minecraft:iron_axe", 1)],
          deps=["dowsing"], icon="hexerei:willow_log"),

    quest("selenite", 4.5, 1.2, "&6Selenite Shard",
          subtitle="Kristalle unter dem Sumpf.",
          description=[
              "Unter Sümpfen und Dschungeln liegen &6Selenit-Geoden&r. Brich die Cluster ab, dann bekommst du &6Selenite Shards&r.",
              "",
              "Selenit dient als Sockel für Kerzen und steckt in der Netherit-Spitze für Besen. Hübsch sieht es obendrein aus.",
          ],
          tasks=[task_item("hexerei:selenite_shard", 4)],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="hexerei:selenite_shard", optional=True),

    # ---- Der Mischkessel -------------------------------------------------------
    quest("cauldron", 0.5, 6, "&2Mixing Cauldron",
          subtitle="Wo jedes Hexenrezept endet.",
          description=[
              "Der &6Mixing Cauldron&r ist das wichtigste Werkzeug einer Hexe: ein normaler &6Kessel&r mit &e5 Eisenbarren&r und &e2 Fackeln&r darüber.",
              "",
              "So funktioniert er: Er fasst bis zu &b2 Eimer&r einer Flüssigkeit, Wasser, Lava oder Talg. Die festen Zutaten wirfst du von oben hinein, schiebst sie per Trichter hinein oder legst sie in seine Oberfläche. Stimmt alles, mischt er das Ergebnis von selbst.",
              "",
              "Viele Rezepte wollen &eHitze&r: Stell ein Feuer, Lagerfeuer, einen Magmablock oder Lava direkt unter den Kessel. Im Menü zeigt dir ein Klick in die Mitte alle Rezepte in JEI.",
              "",
              "&eTipp:&r Bau zwei Kessel, einen für Wasser und einen beheizten für Lava. Dann musst du nicht ständig umfüllen.",
          ],
          tasks=[task_item("hexerei:mixing_cauldron", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_item("minecraft:lava_bucket", 1)],
          deps=["welcome"], icon="hexerei:mixing_cauldron", size=1.75, shape="square"),

    quest("tallow", 2.7, 5.2, "&6Talg",
          subtitle="Fett schmelzen im Kessel.",
          description=[
              "Füll den Kessel mit Wasser, heiz ihn von unten und wirf &e8 Animal Fat&r (oder Kerzen und Honigwaben) hinein. Das Wasser wird zu flüssigem &6Talg&r.",
              "",
              "Eine Glasflasche am Kessel füllt eine &6Bottle of Tallow&r ab, mit einer Flasche Talg füllst du ihn auch wieder auf. So bewahrst du Talg auf, ohne einen Kessel zu blockieren.",
          ],
          tasks=[task_item("hexerei:tallow_bottle", 2)],
          rewards=[reward_item("minecraft:glass_bottle", 8)],
          deps=["cauldron", "animal_fat"], icon="hexerei:tallow_bottle"),

    quest("dipper", 4.7, 5.2, "&6Candle Dipper",
          subtitle="Kerzenziehen wie früher.",
          description=[
              "Der &6Candle Dipper&r entsteht im Kessel mit Lava: &e5 Eisenbarren&r und &e3 Eisennuggets&r. Schleichend mit Rechtsklick setzt du ihn oben auf einen Kessel.",
              "",
              "Ist der Kessel mit Talg gefüllt, gibst du dem Dipper bis zu &e3 Fäden&r. Er taucht sie immer wieder ein, bis fertige Kerzen daran hängen. Mit leerer Hand nimmst du sie ab.",
              "",
              "Der Dipper kann mehr als Kerzen: Mit einem Trank im Kessel tränkt er fertige Kerzen, die dann beim Brennen ihren Effekt an alle in der Nähe geben.",
          ],
          tasks=[task_item("hexerei:candle_dipper", 1)],
          rewards=[reward_item("minecraft:string", 16)],
          deps=["tallow"], icon="hexerei:candle_dipper"),

    quest("candles", 6.7, 5.2, "&6Candle",
          subtitle="Licht und Magie in einem.",
          description=[
              "Hexerei-Kerzen lassen sich färben und stapeln, bis zu &e4 Kerzen&r passen in einen Block. Angezündet mit einem Feuerzeug brennen sie etwa &e35 Minuten&r.",
              "",
              "Mit einem Trank getränkt geben sie beim Brennen Effekte wie Regeneration, Tempo oder Nachtsicht an alle in der Nähe, mit einer &6Mindful Trance Blend&r aus dem Mörser noch mehr. Mit Planken, Selenit oder einem Redstone-Block im Crafting-Feld bekommen sie einen Sockel.",
              "",
              "&eTipp:&r Stell ein paar brennende Kerzen neben deinen Altar, dann schweben sie um das Buch herum.",
          ],
          tasks=[task_item("hexerei:candle", 8)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_xp(5)],
          deps=["dipper"], icon="hexerei:candle"),

    quest("blood", 2.7, 7, "&4Blood Sigil",
          subtitle="Ein Opfer, das weh tut.",
          description=[
              "Das &6Blood Sigil&r mischst du im beheizten Lavakessel aus &e4 Redstone&r und &e4 Polierten Schwarzstein&r aus dem Nether. Leg es in den Sigil-Platz oben links im Kesselmenü.",
              "",
              "Dann springst du &edreimal&r in den Kessel. Jeder Sprung kostet dich etwas Blut, am Ende ist genug für eine &6Bottle of Blood&r darin. Eine Glasflasche füllt es ab.",
              "",
              pic("hexerei:blood_bottle"),
              "",
              "Blut ist die Hauptzutat aller Besen. Getrunken gibt eine Flasche übrigens Absorption.",
              "",
              "&cAchtung:&r Spring nicht mit wenig Leben in den Kessel.",
          ],
          tasks=[task_item("hexerei:blood_sigil", 1), task_item("hexerei:blood_bottle", 3)],
          rewards=[reward_item("minecraft:cooked_beef", 8), reward_xp(5)],
          deps=["cauldron"], icon="hexerei:blood_sigil"),

    quest("herb_jar", 4.7, 7, "&6Herb Jar",
          subtitle="1 024 Kräuter in einem Glas.",
          description=[
              "&e8 Sand&r in einem beheizten Lavakessel ergeben ein &6Herb Jar&r. Es fasst bis zu &e1 024&r Stück von einem einzigen Item.",
              "",
              "Linksklick auf die Vorderseite nimmt ein Item heraus, schleichend einen ganzen Stapel. Rechtsklick auf eine andere Seite öffnet das Menü. Mit dem Krähen-Knopf im Menü sortieren deine Krähen passende Items von selbst hinein.",
          ],
          tasks=[task_item("hexerei:herb_jar", 4)],
          rewards=[reward_item("minecraft:sand", 16)],
          deps=["cauldron"], icon="hexerei:herb_jar", optional=True),

    quest("coffer", 6.7, 7, "&6Coffer",
          subtitle="Eine Truhe für Hexen und Krähen.",
          description=[
              "Die &6Coffer&r mischst du im Wasserkessel aus &e5 Mahagoniplanken&r und &e3 Goldbarren&r. Schleichend mit Rechtsklick stellst du sie ab, Schlagen hebt sie samt Inhalt wieder auf.",
              "",
              "Ihr Menü hat rechts einen &eKrähen-Knopf&r. Ist er an, bringen Krähen im Sammelmodus alle herumliegenden Items zu ihr, die schon in der Coffer liegen. Sie lässt sich färben und mit einem Namen in wechselnden Farben leuchten.",
          ],
          tasks=[task_item("hexerei:coffer", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 3)],
          deps=["cauldron"], icon="hexerei:coffer", optional=True),

    quest("satchel", 4.7, 8.8, "&6Small Satchel",
          subtitle="Gepäck für den Besen.",
          description=[
              "Der &6Small Satchel&r entsteht im Wasserkessel aus &e6 Leder&r, einem &6Faden&r und einem &6Goldnugget&r. Im Satchel-Platz eines Besens gibt er dir &e9 zusätzliche Plätze&r. Medium und Large Satchel legen jeweils neun weitere drauf.",
              "",
              "&eTipp:&r Pack Ersatzbürsten in die Tasche. Auf langen Flügen nutzt sich die Bürste ab, und ohne Bürste fliegt kein Besen.",
          ],
          tasks=[task_item("hexerei:small_satchel", 1)],
          rewards=[reward_item("minecraft:leather", 8)],
          deps=["herb_jar"], icon="hexerei:small_satchel", optional=True),

    quest("witch_armor", 6.7, 8.8, "&5Witch's Outfit",
          subtitle="Hut, Robe und Stiefel.",
          description=[
              "Aus &e2 schwarzem Farbstoff&r, &e4 Leder&r und &e2 Fäden&r mischst du im Wasserkessel &e2 Infused Fabric&r. Daraus craftest du den &6Witch's Hat&r, die &6Witch's Robe&r und die &6Witch's Boots&r wie normale Rüstung.",
              "",
              "Das komplette Set gibt dir ein paar Vorteile, und jedes Teil lässt sich färben. Benannt wechselt es sogar die Farbe. Ein Hut aus Pilzen ist auch drin, für die, die es rustikal mögen.",
          ],
          tasks=[task_item("hexerei:witch_helmet", 1), task_item("hexerei:witch_chestplate", 1),
                 task_item("hexerei:witch_boots", 1)],
          rewards=[reward_item("minecraft:black_dye", 8), reward_xp(5)],
          deps=["coffer"], icon="hexerei:witch_helmet", optional=True),

    # ---- Kraeuterkunde ---------------------------------------------------------
    quest("drying_rack", 10, 5.2, "&6Drying Rack",
          subtitle="Kräuter brauchen Zeit.",
          description=[
              "Das einfache &6Drying Rack&r craftest du aus einem &6Faden&r, &e2 Stöcken&r und einer &6Holzstufe&r, die hübschen Varianten aus Weide, Mahagoni oder Zaubernuss aus Knöpfen, einem Stock und Stufen.",
              "",
              "Es hat drei Plätze mit je bis zu drei Items. Rechtsklick hängt auf, was du in der Hand hältst. Fertig getrocknete Items nimmst du mit einfachem Rechtsklick ab. Trichter können das Gestell auch automatisch füllen und leeren.",
              "",
              "&eTipp:&r &6Verrottetes Fleisch&r trocknet hier zu Leder, und nasse Schwämme werden wieder trocken.",
          ],
          tasks=[task_item("hexerei:herb_drying_rack", 1)],
          rewards=[reward_item("minecraft:string", 8)],
          deps=["herbs"], icon="hexerei:herb_drying_rack"),

    quest("dried_herbs", 12, 5.2, "&6Getrocknete Kräuter",
          subtitle="Getrocknet halten sie ewig.",
          description=[
              "Blüten und Blätter aller vier Kräuter lassen sich trocknen. Getrocknete Kräuter stecken in stärkeren Rezepten, zum Beispiel im Replacer Satchel und im Ankh-Amulett für Krähen.",
              "",
              "Häng ein paar &6Mandrake Flowers&r auf und schau zu, wie sie sich langsam verfärben.",
          ],
          tasks=[task_item("hexerei:dried_mandrake_flowers", 4)],
          rewards=[reward_xp(3)],
          deps=["drying_rack"], icon="hexerei:dried_mandrake_flowers"),

    quest("sage", 10, 7, "&2Sage",
          subtitle="Das Kraut gegen böse Geister.",
          description=[
              "&6Sage Seeds&r pflanzt du auf Ackerland wie Weizen. Die reife Pflanze gibt &6Sage&r und neue Samen.",
              "",
              pic("hexerei:sage"),
              "",
              "Salbei reinigt einen Ort von bösen Geistern, und das ist wörtlich gemeint: gebündelt, getrocknet und angezündet hält er Monster fern. Außerdem steckt er im Seed Mixture für Krähen und in der Mindful Trance Blend.",
          ],
          tasks=[task_item("hexerei:sage", 16)],
          rewards=[reward_item("hexerei:sage_seed", 16)],
          deps=["drying_rack"], icon="hexerei:sage"),

    quest("sage_bundle", 12, 7, "&6Dried Sage Bundle",
          subtitle="Gebündelt und getrocknet.",
          description=[
              "&e8 Sage&r um einen &6Faden&r ergeben ein &6Sage Bundle&r. Frisch ist es noch nutzlos, häng es auf das Drying Rack. Nach einer Weile ist es ein &6Dried Sage Bundle&r, bereit zum Verbrennen.",
          ],
          tasks=[task_item("hexerei:dried_sage_bundle", 2)],
          rewards=[reward_item("minecraft:string", 8)],
          deps=["sage"], icon="hexerei:dried_sage_bundle"),

    quest("sage_plate", 14, 7, "&2Sage Burning Plate",
          subtitle="Keine Monster rund ums Haus.",
          description=[
              "Die &6Sage Burning Plate&r mischst du aus &e8 Goldbarren&r im beheizten Lavakessel. Rechtsklick mit einem &6Dried Sage Bundle&r legt es auf die Platte, ein Feuerzeug zündet es an.",
              "",
              "Solange es brennt, spawnen im Umkreis von &e48 Blöcken&r keine Monster auf natürliche Weise. Das Bündel verbrennt langsam, halte ein paar Ersatzbündel bereit. Rechtsklick mit leerer Hand wechselt die Rauchanzeige, einer der Modi zeigt dir die Reichweite als Rauchring.",
              "",
              "&eTipp:&r Eine Platte in der Mitte eurer Siedlung schützt gleich mehrere Häuser.",
          ],
          tasks=[task_item("hexerei:sage_burning_plate", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["sage_bundle", "cauldron"], icon="hexerei:sage_burning_plate", size=1.5, shape="diamond"),

    quest("mortar", 14, 5.2, "&6Pestle and Mortar",
          subtitle="Erst zerstoßen, dann zaubern.",
          description=[
              "&6Pestle and Mortar&r mischst du im beheizten Lavakessel aus &e5 Stein&r, &e2 Eisenbarren&r und einem &6Netherquarz&r.",
              "",
              "Rechtsklick legt ein Item hinein, schleichend einen ganzen Stapel. Sind alle Zutaten eines Rezepts drin, zerstößt der Mörser sie von selbst. Schleichend mit leerer Hand holst du Zutaten wieder heraus, solange er noch nicht angefangen hat.",
              "",
              "&eTipp:&r Fünf Belladonna-Beeren ergeben vier schwarze Farbstoffe, praktisch für Infused Fabric und die Tinte von Occultism.",
          ],
          tasks=[task_item("hexerei:pestle_and_mortar", 1)],
          rewards=[reward_item("minecraft:quartz", 8)],
          deps=["dried_herbs", "cauldron"], icon="hexerei:pestle_and_mortar"),

    quest("seed_mixture", 16, 5.2, "&6Seed Mixture",
          subtitle="Ein Leckerbissen für Krähen.",
          description=[
              "Im Mörser: je ein &6Weizen-, Kürbis-, Melonen-&r und &6Rote-Bete-Samen&r und ein &6Sage Seed&r. Heraus kommt &6Seed Mixture&r, das Lieblingsfutter der Krähen und der Schlüssel, um sie zu zähmen.",
          ],
          tasks=[task_item("hexerei:seed_mixture", 4)],
          rewards=[reward_item("minecraft:wheat_seeds", 16)],
          deps=["mortar"], icon="hexerei:seed_mixture"),

    quest("mindful_blend", 16, 7, "&6Mindful Trance Blend",
          subtitle="Für Kerzen, die mehr können.",
          description=[
              "Im Mörser: &6Belladonna Flowers&r, &e3 Belladonna Berries&r und &6Sage&r. Die &6Mindful Trance Blend&r craftest du mit einer Kerze zusammen, und die Kerze bekommt einen besonderen Effekt, solange sie brennt.",
              "",
              "Probier aus, wie sie sich neben einem Altar und anderen Tränke-Kerzen macht.",
          ],
          tasks=[task_item("hexerei:mindful_trance_blend", 1)],
          rewards=[reward_xp(3)],
          deps=["mortar", "candles"], icon="hexerei:mindful_trance_blend", optional=True),

    # ---- Besen -----------------------------------------------------------------
    quest("broom_brush", 0.5, 12.5, "&6Broom Brush",
          subtitle="Ohne Bürste kein Flug.",
          description=[
              "Die Bürste lässt einen Besen fliegen. Im Wasserkessel mischst du aus &e2 Mandrake Roots&r, &e4 Weizen&r, &6Mugwort Leaves&r und &6Yellow Dock Leaves&r eine &6Wet Broom Brush&r. Auf dem Drying Rack wird sie zur fertigen &6Broom Brush&r.",
              "",
              "Jeder neue Besen hat schon eine Bürste. Beim Fliegen nutzt sie sich ab und zerbricht irgendwann, deshalb brauchst du Ersatz. Bürsten lassen sich mit Haltbarkeit und Reparatur verzaubern.",
          ],
          tasks=[task_item("hexerei:broom_brush", 2)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["drying_rack", "cauldron"], icon="hexerei:broom_brush"),

    quest("willow_broom", 2.8, 12.5, "&2Willow Broom",
          subtitle="Flieg!",
          description=[
              "Der &6Willow Broom&r ist der einfachste Besen. Im Wasserkessel: &6Bottle of Blood&r, &e2 Willow Logs&r, &e2 Goldblöcke&r, &e2 Weizen&r und eine &6Mandrake Root&r.",
              "",
              "Rechtsklick auf den Besen setzt dich darauf, und los geht es. Er ist langsamer als die anderen, aber zum Bauen und für kurze Strecken ideal. Schleichend mit Rechtsklick öffnest du sein Inventar mit drei Plätzen: Bürste, Satchel und ein Platz für Zubehör.",
              "",
              "&eTipp:&r Besen haben einen &eSchwebemodus&r. Ist er an, fällt der Besen nicht herunter, wenn du absteigst, und du kannst auf ihm stehen wie auf einer kleinen Plattform. Ist er aus, gleitet er mit dir sicher zu Boden, wenn du mitten in der Luft abspringst.",
          ],
          tasks=[task_item("hexerei:willow_broom", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["broom_brush", "blood", "woods"], icon="hexerei:willow_broom", size=2.0, shape="diamond"),

    quest("enhanced_brush", 5.2, 11.6, "&6Enhanced Broom Brush",
          subtitle="Doppelt so lange in der Luft.",
          description=[
              "Die &6Enhanced Broom Brush&r hält doppelt so lange wie die normale. Im Wasserkessel mischst du deine Bürste mit &6Belladonna Flowers&r, &6Belladonna Berries&r, &e2 Mandrake Roots&r, &6Mandrake Flowers&r, &6Mugwort Flowers&r und &6Yellow Dock Flowers&r, danach auf das Drying Rack.",
              "",
              "Die &6Moon Dust Brush&r (mit Mondstaub aus Redstone und Glowstonestaub) ist noch dazu schneller, vor allem bei Vollmond.",
          ],
          tasks=[task_item("hexerei:herb_enhanced_broom_brush", 1)],
          rewards=[reward_xp(5)],
          deps=["willow_broom"], icon="hexerei:herb_enhanced_broom_brush", optional=True),

    quest("witch_hazel_broom", 5.2, 13.4, "&2Witch Hazel Broom",
          subtitle="Der goldene Mittelweg.",
          description=[
              "Der &6Witch Hazel Broom&r ist schneller als der aus Weide und braucht kein Netherit: ein &6Diamant&r, &e2 Witch Hazel Logs&r, &e2 Bottles of Blood&r, &e2 Weizen&r und eine &6Mandrake Root&r im Wasserkessel.",
          ],
          tasks=[task_item("hexerei:witch_hazel_broom", 1)],
          rewards=[reward_item("minecraft:diamond", 1)],
          deps=["willow_broom"], icon="hexerei:witch_hazel_broom", optional=True),

    quest("mahogany_broom", 7.6, 12.5, "&2Mahogany Broom",
          subtitle="Der schnellste Besen am Himmel.",
          description=[
              "Der &6Mahogany Broom&r ist der schnellste der drei. Er braucht einen &6Netheritbarren&r, &e2 Mahogany Logs&r, &e2 Bottles of Blood&r, &e2 Weizen&r und eine &6Mandrake Root&r.",
              "",
              "Als Item ist er feuerfest wie Netherit, er verbrennt also nicht in Lava. Beim Fliegen durch Lava schützt dich das allerdings nicht, dafür gibt es die teure &6Broom Netherite Tip&r im Zubehörplatz.",
              "",
              "&eTipp:&r Für die Kurierwege zwischen euren Basen ist nichts schneller.",
          ],
          tasks=[task_item("hexerei:mahogany_broom", 1)],
          rewards=[reward_table("s2_rare"), reward_xp(10)],
          deps=["willow_broom"], icon="hexerei:mahogany_broom", size=1.5, shape="diamond"),

    # ---- Vertraute -------------------------------------------------------------
    quest("crow", 12, 12.5, "&8Krähen",
          subtitle="Klein, schwarz und hilfsbereit.",
          description=[
              "Wilde &8Krähen&r zähmst du mit &6Seed Mixture&r. Wirf das Futter auf den Boden, dann fliegen sie herbei, und die Chance ist größer als beim direkten Füttern. Du kannst beliebig viele Krähen halten.",
              "",
              pic("hexerei:crow_flute"),
              "",
              "Rechtsklick auf eine Krähe wechselt ihren Befehl: &eFolgen&r (sie setzt sich auf deine Schulter), &eSitzen&r, &eUmherstreifen&r und &eHelfen&r. Beim Helfen sammelt sie Items in eine Coffer, erntet und pflanzt Felder neu oder stiehlt Dorfbewohnern etwas aus der Tasche.",
              "",
              "Mit der &6Crow Flute&r (3 Mahagoniplanken, 2 Farbstoffe) steuerst du alle Krähen in der Nähe auf einmal und legst Schlafplätze fest.",
          ],
          tasks=[task_item("hexerei:crow_flute", 1)],
          rewards=[reward_item("hexerei:seed_mixture", 8), reward_xp(5)],
          deps=["seed_mixture"], icon="hexerei:crow_flute", size=1.5),

    quest("crow_amulet", 14, 12.5, "&6Crow Blank Amulet",
          subtitle="Schmuck für den gefiederten Freund.",
          description=[
              "Im beheizten Lavakessel: eine &6Mandrake Root&r, &e5 Goldnuggets&r und &e2 Goldbarren&r. Das &6Crow Blank Amulet&r legst du einer Krähe um.",
              "",
              "Mit getrockneten Kräutern, Leuchtbeeren und einem &6Totem der Unsterblichkeit&r in einem Trank-Kessel wird daraus das &6Crow Ankh Amulet&r, das deine Krähe wie ein Totem vor dem Tod bewahrt.",
          ],
          tasks=[task_item("hexerei:crow_blank_amulet", 1)],
          rewards=[reward_item("minecraft:gold_nugget", 18)],
          deps=["crow"], icon="hexerei:crow_blank_amulet", optional=True),

    quest("owl", 12, 14.4, "&6Eulenpost",
          subtitle="Briefe und Pakete für deine Freunde.",
          description=[
              "&6Eulen&r zähmst du mit rohem &6Kabeljau&r oder &6Lachs&r, am besten auf den Boden geworfen. Eine gezähmte Eule trägt Post.",
              "",
              "Ein &6Courier Letter&r (Papier und Tintenbeutel) trägt eine Nachricht, ein &6Courier Package&r (4 Papier und eine Holzstufe) bis zu &e5 Items&r. Beschreiben oder packen, versiegeln, dann mit dem Brief auf deine Eule klicken und einen Empfänger wählen: einen Spieler oder ein &6Courier Depot&r, den Briefkasten aus Hexerei-Planken.",
              "",
              "&eTipp:&r Auf einem Server mit vielen Basen ist das die schönste Art, Freunden ein paar Quelljuwelen oder Messingbarren zu schicken.",
          ],
          tasks=[task_item("hexerei:courier_package", 1), task_item("hexerei:willow_courier_depot", 1)],
          rewards=[reward_item("minecraft:cod", 8), reward_xp(5)],
          deps=["crow"], icon="hexerei:courier_package", optional=True),

    # ---- Ziel ------------------------------------------------------------------
    quest("witch_house", 19, 9.5, "&2Ein Hexenhaus",
          subtitle="Kerzen, Kräuter, ein Besen an der Tür.",
          description=[
              "Kräuter hängen zum Trocknen, der Kessel dampft, Salbei hält die Monster fern, Krähen räumen auf und ein Besen lehnt an der Tür. Das ist eine richtige Hexenhütte.",
              "",
              "Zieh noch ein paar Kerzen für die Nachbarn, dann flieg los und hilf den Botania- und Ars-Leuten mit Mana-Perlen und Juwelen für den Obelisken. Hexerei selbst hat keinen Platz im Stufenziel, aber wer schnell fliegt, ist bei jedem Transport vorne dabei.",
          ],
          tasks=[task_item("hexerei:candle", 16), task_item("hexerei:dried_sage_bundle", 4)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["sage_plate", "mahogany_broom", "crow"], icon="hexerei:mixing_cauldron", size=2.5, shape="gear"),
]

images = [
    banner("hexerei/title", "Hexerei", 6.5, -4.4, height=1.8, kind="title", colour="magic"),
    banner("hexerei/hexenkunst", "Hexenkunst", 4.5, -2.6, height=0.9, colour="magic"),
    banner("hexerei/kessel", "Der Mischkessel", 3.7, 3.6, height=0.9, colour="magic"),
    banner("hexerei/kraeuter", "Kräuterkunde", 13, 3.6, height=0.9, colour="nature"),
    banner("hexerei/besen", "Besen", 4.1, 10.4, height=0.9, colour="magic"),
    banner("hexerei/vertraute", "Vertraute", 13, 10.4, height=0.9, colour="magic"),
]

chapter(C, "Hexerei", "hexerei:mixing_cauldron", "magic", quests, shape="circle", order=16, stage=2,
        subtitle=["Stufe 2. Kräuter, Kessel, Kerzen und Besen."], images=images)
