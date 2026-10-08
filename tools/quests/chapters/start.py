"""Start here: the first quests take a new player from spawn to a claimed base and the first
obelisk deposit (no vanilla tutorial, the players know Minecraft), then the obelisk (hand in, /kw, feeders, pillars, scaling, the 98
percent hold), the Nature's Aura steps behind both stage 1 milestones (brilliant fiber, gold leaf,
ritual of the forest, token of joy, natural altar, infused iron), the five stages and locked items,
the server, and a hub that points to every stage 1 chapter. Rules from docs/STAGES.md and
config/kronwerke/goals.json, lock texts from the Kronwerke Core 0.6.0 lang file, Nature's Aura
recipes and the altar multiblock from its jar. Questbook, JEI, map, team and death basics live in
tips.py, automated farms in farms.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "start_here"

DAY = -8          # row of the first steps
P1, P2 = 27.5, 30  # the two columns of chapter links

quests = [
    # ---- Die ersten Schritte ---------------------------------------------------------
    quest("welcome", 0, 3, "&6Fang hier an",
          subtitle="Sechs kurze Schritte bis zur ersten Abgabe am Obelisken.",
          description=[
              "Folge der Reihe oben von links nach rechts: Basis sichern, Bruchstein sammeln, zum Obelisken, abgeben. Minecraft kennst du, hier geht es nur um das, was auf Kronwerke anders ist.",
              "",
              "&6Kronwerke Season 2&r: rund dreißig Leute, eine Welt, fünf &6Stufen&r. Jede Stufe öffnet sich für alle, sobald der Server am &6Obelisken&r am Spawn ein gemeinsames Ziel gefüllt hat.",
              "",
              "Fertige Quests klickst du an und holst dir die Belohnung. Wie das Buch, JEI und die Karte funktionieren, steht im Kapitel &6Tipps und Tricks&r.",
          ],
          tasks=[task_checkmark("Los geht's")],
          rewards=[reward_item("minecraft:bread", 16), reward_table("s1_common")],
          icon="ftbquests:book", size=2.5, shape="hexagon"),

    quest("v_claim", 3.5, DAY, "&6Sichere deine Basis",
          subtitle="M, dann C, dann über die Chunks ziehen.",
          description=[
              "Such dir einen Platz, bau was Festes hin und sichere es: &eM&r öffnet die Karte, &eC&r die Claim-Ansicht. Mit gedrückter &elinker Maustaste&r über die Chunks deiner Basis ziehen.",
              "",
              "In deinen Chunks kann niemand außer deinem Team abbauen oder Truhen öffnen. Wie viele Chunks du hast und wie du sie dauerhaft lädst, steht im Kapitel &6Tipps und Tricks&r.",
              "",
              "Nachts ziehen neben Zombies und Skeletten die Kreaturen aus &6Born in Chaos&r herum, und einige sind zäh. Licht und Wände helfen wie immer.",
          ],
          tasks=[task_checkmark("Meine Basis ist gesichert")],
          rewards=[reward_table("s1_common")],
          deps=["welcome"], icon="minecraft:filled_map"),

    quest("d_stone", 5.5, DAY, "&7Sammle 64 Bruchstein",
          subtitle="Dein erster Stapel für den Obelisken.",
          description=[
              "Wirf keinen Bruchstein weg. Der Obelisk will in Stufe 1 &e20 000 Stück&r vom ganzen Server, und jede Sorte zählt: normaler, bemooster und Bruchtiefenschiefer.",
              "",
              "&eTipp:&r Halte &e`&r (links neben der 1) beim Abbauen, dann nimmt &6Ultimine&r eine ganze Reihe auf einmal mit.",
          ],
          tasks=[task_item("minecraft:cobblestone", 64)],
          rewards=[reward_xp(3)],
          deps=["v_claim"], icon="minecraft:cobblestone"),

    quest("o_find", 7.5, DAY, "&6Geh zum Obelisken",
          subtitle="Er steht am Spawn.",
          description=[
              "Der &6Obelisk&r steht am Weltspawn. Weißt du nicht mehr, wo das ist: Am Spawn steht ein &6Wegstein&r, und jeder aktivierte Wegstein bringt dich dorthin zurück.",
              "",
              "Oben am Bildschirm zeigt dir eine &eBossleiste&r das aktive Ziel und wie weit es ist. Die siehst du überall, nicht nur am Obelisken.",
          ],
          tasks=[task_checkmark("Ich stehe vor dem Obelisken")],
          rewards=[reward_item("waystones:warp_dust", 4)],
          deps=["d_stone"], icon="minecraft:lodestone"),

    quest("o_handin", 9.5, DAY, "&eGib deinen Bruchstein ab",
          subtitle="Stapel in die Hand, Rechtsklick auf den Obelisken.",
          description=[
              "Halte den Bruchstein in der Hand und mach einen &eRechtsklick&r auf den Obelisken. Der ganze Stapel geht hinein und wird dir gutgeschrieben.",
              "",
              "&eSchleichen und Rechtsklick&r gibt alles aus deinem Inventar ab, was das Ziel gerade braucht. Was es nicht braucht, bleibt bei dir. Abgaben ab 64 Stück stehen im Chat.",
          ],
          tasks=[task_checkmark("Abgegeben")],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["o_find"], icon="minecraft:cobblestone", size=1.5, shape="gear"),

    quest("d_iron", 11.5, DAY, "&6Schmilz 16 Eisen",
          subtitle="Das Metall, das in jeder Mod steckt.",
          description=[
              "Eisen steckt in den Teilen für Create, den ersten Zauber-Geräten, dem Kochtopf und dem Werkzeug von Silent Gear. Eisennuggets und Andesit ergeben &6Andesitlegierung&r, das Material der Technik-Säule am Obelisken.",
              "",
              "Andesit-Gehäuse, Infundiertes Eisen und ein Quellstein ergeben den &6Grubenrahmen&r, das Tor zur &6Minenwelt&r. Alles dazu im Kapitel &6Erkundung&r.",
          ],
          tasks=[task_item("minecraft:iron_ingot", 16)],
          rewards=[reward_item("minecraft:coal", 16)],
          deps=["d_stone"], icon="minecraft:iron_ingot"),

    quest("d_done", 13.5, DAY, "&6Schaff den ersten Tag",
          subtitle="Basis, Eisen und die erste Abgabe.",
          description=[
              "Du hast eine gesicherte Basis, Eisen und schon etwas am Obelisken abgegeben. Das ist mehr, als die meisten nach dem ersten Abend haben.",
              "",
              "Ab hier gibt es keinen festen Pfad mehr. Unten erklärt dieses Kapitel den Obelisken und die Stufen genauer, rechts bei &eDeine Wege&r findest du alle Kapitel von Stufe 1.",
          ],
          tasks=[task_checkmark("Geschafft")],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["d_iron", "o_handin"], icon="minecraft:clock", size=1.5, shape="gear"),

    quest("d_waystone", 7.5, -7, "&6Aktiviere den Wegstein am Spawn",
          subtitle="Damit du immer zurückfindest.",
          description=[
              "Am Spawn steht ein &6Wegstein&r. Ein &eRechtsklick&r aktiviert ihn für dich. Ab dann bringt dich jeder Wegstein, den du kennst, mit einem Klick hierher zurück.",
              "",
              "Die Reise kostet etwas Erfahrung, je weiter, desto mehr. Mehr dazu im Kapitel &6Tipps und Tricks&r.",
          ],
          tasks=[task_checkmark("Aktiviert")],
          rewards=[reward_xp(3)],
          deps=["o_find"], icon="waystones:waystone", optional=True),

    quest("d_backpack", 5.5, -7, "&6Näh dir einen Rucksack",
          subtitle="Mehr Platz für den ersten Ausflug.",
          description=[
              "Oben Faden, Leder, Faden. In der Mitte Faden, eine &6Truhe&r, Faden. Unten drei Leder. Heraus kommt ein &6Rucksack&r mit &d27&r Feldern, so viel wie eine Truhe.",
              "",
              "Trag ihn auf dem Rücken oder in der Hand, &eB&r öffnet ihn. Wie du ihn später vergrößerst, steht im Kapitel &6Lager&r.",
          ],
          tasks=[task_item("sophisticatedbackpacks:backpack", 1)],
          rewards=[reward_item("minecraft:leather", 4), reward_xp(3)],
          deps=["d_stone"], icon="sophisticatedbackpacks:backpack", optional=True),

    # ---- Der Obelisk -----------------------------------------------------------------
    quest("o_obelisk", 4.5, 0, "&6Lies die Bossleiste",
          subtitle="Ein Ziel, mehrere Säulen, alle müssen voll werden.",
          description=[
              "Die &eBossleiste&r oben zeigt das aktive Ziel. In Stufe 1 heißt es &6Das Fundament des Kronwerks&r und hat drei Säulen: &7Stein&r, &6Technik&r und &dMagie&r.",
              "",
              "Die Stufe öffnet sich erst, wenn &ealle&r Säulen voll sind. Ein Server, der nur Maschinen baut oder nur zaubert, kommt nicht weiter.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="minecraft:lodestone", size=1.75, shape="diamond"),

    quest("o_commands", 6.75, -1, "&6Tipp /kw goals",
          subtitle="Jede Säule, jede Zahl.",
          description=[
              "&e/kw goals&r zeigt alle Ziele und wie weit jede Säule ist. &e/kw top&r zeigt, wer bisher am meisten beigetragen hat.",
              "",
              "Klickst du mit etwas auf den Obelisken, das er nicht braucht, sagt er dir im Chat, was er gerade will.",
          ],
          tasks=[task_checkmark("Ausprobiert")],
          rewards=[reward_xp(3)],
          deps=["o_obelisk"], icon="minecraft:command_block"),

    quest("o_deposit", 6.75, 1, "&6Tipp /kw deposit",
          subtitle="Abgeben, falls der Rechtsklick nicht klappt.",
          description=[
              "&e/kw deposit&r gibt den Stapel in deiner Hand ab, &e/kw deposit all&r alles aus dem Inventar, was das aktuelle Ziel nimmt.",
              "",
              "Das ist der Ausweichweg. Am Obelisken selbst geht es mit Rechtsklick und Schleichen schneller.",
          ],
          tasks=[task_checkmark("Ausprobiert")],
          rewards=[reward_xp(3)],
          deps=["o_obelisk"], icon="minecraft:hopper"),

    quest("o_feeder", 9, 0, "&6Stell einen Zubringer auf",
          subtitle="Eine Truhe am Obelisken, die für dich einzahlt.",
          description=[
              "Stell eine &6Truhe&r oder ein &6Fass&r höchstens &e3 Blöcke&r vom Obelisken entfernt auf. Sie wird dein &6Zubringer&r: Alle &e2 Sekunden&r nimmt das Ziel heraus, was es braucht, und schreibt es dir gut.",
              "",
              "Jeder Spieler hat höchstens &ezwei&r Zubringer, ein dritter zählt nicht. Gezählt wird für den, der die Truhe aufgestellt hat, also leg nichts hinein, was du behalten willst.",
          ],
          tasks=[task_item("minecraft:barrel", 1)],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(3)],
          deps=["o_commands", "o_deposit"], icon="minecraft:barrel"),

    quest("o_farm", 11.25, 0, "&6Schließ eine Farm an",
          subtitle="Der Beitrag wächst, während du redest.",
          description=[
              "Leite Bruchstein, Andesitlegierung oder Quelljuwelen per Trichter, Förderband oder Schleuse in deinen Zubringer. Ab dann zahlt deine Fabrik selbst ein.",
              "",
              "Wie man einen Bruchsteingenerator, eine Legierungsstraße oder eine Juwelenanlage baut, zeigt das Kapitel &6Erste Farmen&r.",
          ],
          tasks=[task_checkmark("Meine Farm zahlt ein")],
          rewards=[reward_table("s1_common"), reward_xp(5)],
          deps=["o_feeder"], icon="minecraft:hopper"),

    quest("o_stone", 13.5, -1.5, "&7Füll die Stein-Säule",
          subtitle="20 000 Bruchstein.",
          description=[
              "Jede Sorte &6Bruchstein&r zählt, je ein Punkt. Die Säule für alle: Jeder hilft ab der ersten Minute, ohne Maschinen und Zauber.",
              "",
              "Am schnellsten geht es mit Ultimine in der Minenwelt oder mit einem Bruchsteingenerator am Zubringer.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(2)],
          deps=["o_farm"], icon="minecraft:cobblestone"),

    quest("o_tech", 13.5, 0, "&6Füll die Technik-Säule",
          subtitle="1 500 Andesitlegierung und 12 Steinwerk-Getriebe.",
          description=[
              "&6Andesitlegierung&r: 2 &6Andesit&r und 2 &6Eisennuggets&r (oder Zinknuggets) schräg an der Werkbank, gibt eine.",
              "",
              img(item_texture("create:andesite_alloy"), 32, 32),
              "",
              "&eRezept auf Kronwerke:&r Der &6Mechanische Mixer&r macht aus 1 Andesit und 1 Nugget &ezwei&r Legierungen, braucht also ein Viertel des Materials. Jede Legierung zählt 2 Punkte. Siehe Kapitel &6Create&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(2)],
          deps=["o_farm"], icon="create:andesite_alloy"),

    quest("o_magic", 13.5, 1.5, "&dFüll die Magie-Säule",
          subtitle="800 Quelljuwelen und 12 Quellschlusssteine.",
          description=[
              "&6Quelljuwelen&r gibt es nur aus der &aImbuement-Kammer&r: Amethyst hinein, ein &6Quellglas&r mit &dSource&r daneben.",
              "",
              img(item_texture("ars_nouveau:source_gem"), 32, 32),
              "",
              "Jedes Juwel zählt 4 Punkte. Eine kleine Anlage mit Quellenlink liefert ein paar Dutzend in der Stunde, auch per Zubringer. Siehe Kapitel &dArs Nouveau&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(2)],
          deps=["o_farm"], icon="ars_nouveau:source_gem"),

    quest("o_scale", 16, 0, "&6Prüf die echten Mengen",
          subtitle="Mehr Spieler, größere Ziele.",
          description=[
              "Die Zahlen gelten für &e30 aktive Spieler&r. Aktiv ist, wer in den letzten 7 Tagen mehr als eine Stunde gespielt hat. Beim Öffnen einer Stufe wird die Menge mit diesem Anteil multipliziert, mindestens 0,4, höchstens 1,5, und bleibt dann fest.",
              "",
              "&eAusnahme:&r Die 12 Steinwerk-Getriebe und 12 Quellschlusssteine bleiben immer gleich. Was gerade gilt, zeigen &e/kw goals&r und die Statusseite auf der Website.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(2)],
          deps=["o_stone", "o_tech", "o_magic"], icon="minecraft:comparator"),

    quest("o_event", 18.5, 0, "&cSei beim Finale dabei",
          subtitle="Bei 98 Prozent ist Schluss, bis alle da sind.",
          description=[
              "Bei &e98 Prozent&r nimmt der Obelisk nichts mehr an. Das Team legt einen Termin fest, alle Streamer gehen live, die letzten Gegenstände wandern zusammen hinein, und die nächste Stufe öffnet &efür alle gleichzeitig&r.",
              "",
              "Den Termin erfährst du im &9Discord&r. Halte dir einen kleinen Vorrat zurück, damit du beim Finale selbst etwas einwerfen kannst.",
          ],
          tasks=[task_checkmark("Ich bin dabei")],
          rewards=[reward_table("s1_common"), reward_xp(5)],
          deps=["o_scale"], icon="minecraft:beacon", size=1.75, shape="gear"),

    # ---- Die Meilensteine ------------------------------------------------------------
    quest("m_fiber", 4.5, 4.5, "&aMach Brilliant Fiber",
          subtitle="Der erste Schritt in Nature's Aura.",
          description=[
              "4 &6Laub&r in die Ecken, 4 &6Goldnuggets&r an die Seiten, &6Gras&r in die Mitte: 4 &6Brilliant Fiber&r.",
              "",
              "Beide Meilensteine von Stufe 1 brauchen &aNature's Aura&r: das Getriebe &6Infused Iron&r, der Schlussstein &6Gold Leaf&r. Diese Reihe führt dich in sechs Schritten dorthin.",
              "",
              "Das &6Book of Natural Aura&r (2 Papier, Leder, ein Setzling) erklärt jeden Schritt mit Bild.",
          ],
          tasks=[task_item("naturesaura:gold_fiber", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 9), reward_xp(3)],
          deps=["o_obelisk"], icon="naturesaura:gold_fiber"),

    quest("m_goldleaf", 6.75, 4.5, "&aErnte Gold Leaf",
          subtitle="Ein Baum, der mit der Zeit golden wird.",
          description=[
              "Setz die &6Brilliant Fiber&r in die Krone eines Baums. Mit der Zeit werden die Blätter golden. Ganz goldene Blätter lassen beim Abbauen &6Gold Leaf&r fallen.",
              "",
              "Ein goldenes Blatt gibt mit 75 Prozent Chance ein Gold Leaf. Behalte den Baum, du brauchst Gold Leaf für jeden der nächsten Schritte und für den Quellschlussstein.",
          ],
          tasks=[task_item("naturesaura:gold_leaf", 8)],
          rewards=[reward_xp(4)],
          deps=["m_fiber"], icon="naturesaura:gold_leaf"),

    quest("m_ritual", 9, 4.5, "&aBereite das Ritual des Waldes vor",
          subtitle="Goldpulver im Kreis, Ständer drumherum.",
          description=[
              "Ein Gold Leaf gibt 2 &6Gold Powder&r. Leg &e16&r davon als Ring um einen freien Platz, wie im Buch gezeigt. Außen herum bis zu 8 &6Wooden Stands&r (Gold Leaf auf einem Stamm).",
              "",
              "Auf die Ständer kommen die Zutaten, in die Mitte ein &6Setzling&r. Wächst er (Knochenmehl hilft), frisst das Ritual Baum und Zutaten und lässt das Ergebnis liegen. Es braucht jedes Mal die richtige Setzlingsart.",
          ],
          tasks=[task_item("naturesaura:wood_stand", 6), task_item("naturesaura:gold_powder", 16)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(4)],
          deps=["m_goldleaf"], icon="naturesaura:wood_stand"),

    quest("m_token", 11.25, 4.5, "&aMach Token of Joy",
          subtitle="Sonnenlicht in der Flasche, dann das erste Ritual.",
          description=[
              "&6Bottle and Cork&r (Glasflasche und ein Brett), damit in der Oberwelt in die Luft klicken: &6Bottled Sunlight&r. Auf die Ständer: Bottled Sunlight, Gold Leaf, eine Blume, ein Apfel, eine Fackel, ein Eisenbarren. In die Mitte ein &6Eichensetzling&r.",
              "",
              "Das Ritual gibt &e2 Token of Joy&r. Einen brauchst du für den Altar.",
          ],
          tasks=[task_item("naturesaura:token_joy", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 4), reward_xp(4)],
          deps=["m_ritual"], icon="naturesaura:token_joy"),

    quest("m_altar", 13.5, 4.5, "&aBau den Natural Altar",
          subtitle="Ein Ritual für den Altar, ein Bauwerk drumherum.",
          description=[
              "Ritual des Waldes mit einem &6Eichensetzling&r: 3 &6Lebestein&r (Livingrock, aus Botanias Pure Daisy), ein Gold Leaf, ein Goldbarren und ein Token of Joy. Heraus kommt der &6Natural Altar&r.",
              "",
              "Der Altar arbeitet nur in seinem Bauwerk aus Steinziegeln, Brettern, gemeißelten Steinziegeln und &6Golden Stone Bricks&r (Steinziegel und Brilliant Fiber). Das Buch zeigt den Aufbau Schicht für Schicht.",
          ],
          tasks=[task_item("naturesaura:nature_altar", 1)],
          rewards=[reward_item("minecraft:stone_bricks", 32), reward_table("s1_common")],
          deps=["m_token"], icon="naturesaura:nature_altar"),

    quest("m_infused", 15.75, 4.5, "&aVeredle Eisen zu Infused Iron",
          subtitle="Einen Eisenbarren auf den Altar legen, warten.",
          description=[
              "Leg einen &6Eisenbarren&r auf den fertigen Altar. Hat er genug Aura gesammelt (&e15 000&r pro Barren), wird daraus &6Infused Iron&r. Ein Eisenblock geht genauso.",
              "",
              "Der Altar zieht die Aura langsam aus der Umgebung, bis dort keine mehr ist. Wird er langsam, ist die Gegend leer. Infused Iron brauchst du später auch für Manastahl in Botania.",
          ],
          tasks=[task_item("naturesaura:infused_iron", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["m_altar"], icon="naturesaura:infused_iron"),

    quest("m_gearbox", 18, 4.5, "&6Bau ein Steinwerk-Getriebe",
          subtitle="Der Meilenstein der Technik-Säule.",
          description=[
              "Oben: &6Andesitgehäuse&r, &6Großes Zahnrad&r, &6Andesitgehäuse&r. Mitte: &6Mechanische Presse&r, &6Infused Iron&r, &6Mahlstein&r. Unten: &6Andesitgehäuse&r, &6Wasserrad&r, &6Andesitgehäuse&r.",
              "",
              img("kronwerke:textures/item/stone_gearbox.png", 32, 32),
              "",
              "Der Obelisk will &e12&r, eine feste Zahl. Eines zählt &e250 Punkte&r, so viel wie 125 Andesitlegierungen. Die zwölf tragen etwa die Hälfte der Technik-Säule.",
              "",
              "&cWichtig:&r Meilensteine nimmt der Obelisk nur, solange ihr Ziel aktiv ist. In Stufe 2 folgen &6Messingherz&r und &6Runenkern&r, je &e8&r.",
          ],
          tasks=[task_item("kronwerke:stone_gearbox", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(8)],
          deps=["m_infused", "o_tech"], icon="kronwerke:stone_gearbox", size=1.25, shape="gear"),

    quest("m_keystone", 15.75, 6.75, "&dBau einen Quellschlussstein",
          subtitle="Der Meilenstein der Magie-Säule.",
          description=[
              "Oben: &6Quelljuwelblock&r, &6Quellglas&r, &6Quelljuwelblock&r. Mitte: &bManadiamant&r, &6Andesitlegierung&r, &bManadiamant&r. Unten: &6Quelljuwelblock&r, &6Gold Leaf&r, &6Quelljuwelblock&r.",
              "",
              img("kronwerke:textures/item/source_keystone.png", 32, 32),
              "",
              "Die &bManadiamanten&r infundierst du im Manabecken von Botania, je &d10 000 Mana&r. Das Gold Leaf kommt von deinem goldenen Baum.",
              "",
              "Der Obelisk will &e12&r, fest. Einer zählt &e250 Punkte&r, so viel wie gut 60 Quelljuwelen. Die zwölf tragen fast die Hälfte der Magie-Säule.",
          ],
          tasks=[task_item("kronwerke:source_keystone", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(8)],
          deps=["m_goldleaf", "o_magic"], icon="kronwerke:source_keystone", size=1.25, shape="gear"),

    quest("m_gearparts", 17, 5, "&6Sammle die Teile für das Getriebe",
          subtitle="Alles aus Create, bis auf das Infused Iron.",
          description=[
              "Für ein &6Steinwerk-Getriebe&r brauchst du neben dem &6Infused Iron&r vier &6Andesitgehäuse&r, ein &6Großes Zahnrad&r, eine &6Mechanische Presse&r, einen &6Mahlstein&r und ein &6Wasserrad&r.",
              "",
              "Alles davon gibt es mit Create in Stufe 1. Das Kapitel &6Create&r zeigt dir jedes Teil, und Presse und Mahlstein kannst du gleich für deine Andesitstraße nutzen, bevor sie im Getriebe landen.",
          ],
          tasks=[task_item("create:andesite_casing", 4), task_item("create:large_cogwheel", 1),
                 task_item("create:mechanical_press", 1), task_item("create:millstone", 1),
                 task_item("create:water_wheel", 1)],
          rewards=[reward_item("create:andesite_alloy", 8), reward_xp(4)],
          deps=["o_tech"], icon="create:andesite_casing", section="milestones"),

    quest("m_livingrock", 12.5, 6, "&aMach Lebestein",
          subtitle="Der Altar braucht drei davon.",
          description=[
              "&6Lebestein&r macht das &6Reine Gänseblümchen&r aus Botania: Stell Stein rund um die Blume, nach einer Weile wird er zu Lebestein.",
              "",
              "Für den &6Natural Altar&r brauchst du drei. Wie du das Gänseblümchen bekommst, steht im Kapitel &aBotania&r ganz am Anfang.",
          ],
          tasks=[task_item("botania:livingrock", 3)],
          rewards=[reward_item("minecraft:stone", 16), reward_xp(3)],
          deps=["m_token"], icon="botania:livingrock"),

    quest("m_manadiamond", 14, 6, "&bInfundiere zwei Manadiamanten",
          subtitle="Ein Diamant ins volle Manabecken.",
          description=[
              "Wirf einen &6Diamanten&r in ein &6Manabecken&r mit mindestens &d10 000 Mana&r. Er wird zum &bManadiamanten&r.",
              "",
              "Der &6Quellschlussstein&r braucht zwei davon. Wie du Mana erzeugst und ins Becken leitest, steht im Kapitel &aBotania&r.",
          ],
          tasks=[task_item("botania:mana_diamond", 2)],
          rewards=[reward_xp(5)],
          deps=["o_magic"], icon="botania:mana_diamond"),

    quest("m_keyparts", 17.5, 6, "&dSammle die Teile für den Schlussstein",
          subtitle="Vier Juwelblöcke und ein Quellglas.",
          description=[
              "Ein &6Quelljuwelblock&r sind vier &6Quelljuwelen&r im Quadrat. Oder du legst einen &6Amethystblock&r in die &aImbuement-Kammer&r, das kostet &d2 000 Source&r und spart dir die vier Juwelen.",
              "",
              "Das &6Quellglas&r: oben und unten je drei &6Archwood-Platten&r, an den Seiten Glas. Mit Manadiamanten, Andesitlegierung und Gold Leaf hast du dann alles für den &6Quellschlussstein&r.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 4), task_item("ars_nouveau:source_jar", 1)],
          rewards=[reward_xp(5)],
          deps=["m_manadiamond"], icon="ars_nouveau:source_gem_block"),

    # ---- Stufen und Sperren ----------------------------------------------------------
    quest("s_stages", 4.5, 11, "&6Lerne die fünf Stufen",
          subtitle="Eine nach der anderen, für alle zugleich.",
          description=[
              "&7Steinwerk&r, &6Messingwerk&r, &fStahlwerk&r, &dSternwerk&r, &cChaoswerk&r. Jede öffnet sich über ein Ziel am Obelisken und kann ungefähr doppelt so viel wie die davor.",
              "",
              "Nichts wird aus dem Pack entfernt, manches kommt nur später. Vanilla ist offen, bis auf den &cNether&r (Stufe 2) und das &dEnde&r (Stufe 4). Beide öffnen mit einem Event.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["o_obelisk"], icon="minecraft:stone_bricks", size=1.75, shape="hexagon"),

    quest("s_1", 7, 9.75, "&7Stufe 1: Steinwerk",
          subtitle="Holz, Stein, Wasserräder, die ersten Zauber.",
          description=[
              "Hier bist du. Offen: Oberwelt und Minendimension, Create bis Andesit (Wasserrad, Mahlstein, Presse, Mixer ohne Hitze, Förderbänder, Lüfter), Ars Nouveau für Anfänger, Botania bis zum Manabecken, Nature's Aura, Mystical Agriculture Inferium.",
              "",
              "Dazu Farmer's Delight, Aquaculture, Silent Gear bis Eisen, Lederrucksäcke, Holzschubladen, Wegsteine und Apotheosis. Das Ziel will Bruchstein, Andesitlegierung und Quelljuwelen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["s_stages"], icon="minecraft:cobblestone"),

    quest("s_2", 9, 9.75, "&6Stufe 2: Messingwerk",
          subtitle="Messing, der Nether, die ersten Maschinen.",
          description=[
              "Beginnt mit einem Event: Das &cNetherportal am Spawn&r wird live auf Stream entzündet.",
              "",
              "Dann Messing und Lohenbrenner, Züge und Kontraptionen, Mekanism und Immersive Engineering für den Anfang, Runenaltar und Terrastahl, Lehrlings-Glyphen, die ersten Geister in Occultism, Hexerei und Productive Bees.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["s_1"], icon="minecraft:netherrack"),

    quest("s_3", 11, 9.75, "&fStufe 3: Stahlwerk",
          subtitle="Stahl, Erzvervielfachung, Rituale.",
          description=[
              "Stahl in Mengen, Erzverdreifachung, Lagernetzwerke mit Applied Energistics und Refined Storage, Alfheim, Afrit und Marid, Maschinen, die rund um die Uhr laufen.",
              "",
              "Eine reine Magie-Basis vervielfacht Erz hier genauso gut wie eine reine Tech-Basis.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["s_2"], icon="minecraft:iron_block"),

    quest("s_4", 13, 9.75, "&dStufe 4: Sternwerk",
          subtitle="Das Ende, die Sterne, der Drache.",
          description=[
              "Das &dEnde&r öffnet mit einem Event, der Enderdrache ist der erste Boss, den der Server gemeinsam bekämpft.",
              "",
              "Danach Fusion, Draconic Evolution, die Gaia-Wächterin und Mahou Tsukai.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["s_3"], icon="minecraft:ender_eye"),

    quest("s_5", 15, 9.75, "&cStufe 5: Chaoswerk",
          subtitle="Die letzten Maschinen und der letzte Kampf.",
          description=[
              "Alles, was noch fehlt, öffnet. Der Obelisk will diesmal das, was den Endkampf möglich macht.",
              "",
              "Das Finale ist der Kampf gegen den &cChaos Guardian&r, live auf allen Streams. Siehe Kapitel &5Das Finale&r, sobald Stufe 5 offen ist.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(2)],
          deps=["s_4"], icon="minecraft:dragon_head"),

    quest("s_locked", 7, 12.25, "&cErkenne gesperrte Gegenstände",
          subtitle="Einstecken geht, benutzen noch nicht.",
          description=[
              "Ein Gegenstand einer späteren Stufe heißt im Tooltip &7???&r, darunter &cÖffnet in Stufe 2 (Messingwerk).&r und &8Einstecken geht, benutzen noch nicht.&r Aufheben und lagern darfst du ihn, halten, anziehen, platzieren und herstellen nicht.",
              "",
              "In JEI siehst du nur die &enächste&r Stufe, verhüllt, aber mit Rezept. Spätere Stufen bleiben ganz unsichtbar. Zink für Messing kannst du also schon jetzt einlagern.",
              "",
              "Mehr dazu im Kapitel &6Tipps und Tricks&r.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["s_stages"], icon="minecraft:barrier"),

    quest("s_latejoin", 9, 12.25, "&aHol dir dein Starterpaket",
          subtitle="Wer später kommt, fängt nicht bei null an.",
          description=[
              "Wer später einsteigt, bekommt die &6Starterpakete&r aller Stufen, die schon offen sind. Mit Stufe 2 sind das 16 Messingbarren, ein Lohenbrenner, ein Quellglas und 8 Manaperlen.",
              "",
              "So bist du gleich bei den anderen dabei. Wer Hilfe braucht, fragt im Chat oder im Sprachchat.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(2)],
          deps=["s_locked"], icon="minecraft:chest"),

    quest("s_ties", 11, 12.25, "&dSprich dich mit der anderen Seite ab",
          subtitle="Technik braucht Magie, Magie braucht Technik.",
          description=[
              "Einige Rezepte binden die Seiten aneinander. Schon in Stufe 1: das Getriebe braucht &6Infused Iron&r, der Schlussstein &bManadiamanten&r und &6Andesitlegierung&r.",
              "",
              "Ab Stufe 2: Der &6Lohenbrenner&r braucht 2 &6Quelljuwelen&r, der Runenaltar einen &6Messingbarren&r, &6Manaperlen&r ein &6Messinggehäuse&r unter dem Becken, die Infusionsanlage von Mekanism &6Manastahl&r.",
              "",
              "Die betroffenen Quests nennen das Rezept jeweils als &eRezept auf Kronwerke&r. Klärt früh, wer was übernimmt.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_table("s1_common")],
          deps=["s_latejoin"], icon="minecraft:amethyst_shard"),

    quest("s_zinc", 13, 11.5, "&6Lager Zink für Stufe 2 ein",
          subtitle="Wer vorsorgt, baut am ersten Tag Messing.",
          description=[
              "&6Zinkerz&r findest du schon jetzt beim Graben. Messing aus Kupfer und Zink öffnet zwar erst in Stufe 2, das Zink darfst du aber jetzt abbauen und einlagern.",
              "",
              "Ein paar Stapel &6Rohzink&r in der Truhe, und am Tag der Öffnung bist du gleich dabei.",
          ],
          tasks=[task_item("create:raw_zinc", 32)],
          rewards=[reward_xp(5)],
          deps=["s_locked"], icon="create:raw_zinc", optional=True),

    # ---- Auf dem Server --------------------------------------------------------------
    quest("v_discord", 4.5, 17, "&9Tritt dem Discord bei",
          subtitle="Hier wird die Season organisiert.",
          description=[
              "Auf den Server kommst du über den &9Discord&r: Captcha lösen, dann gibt dir ein Streamer einen Platz auf der Whitelist. &cWer den Discord verlässt, fliegt auch von der Whitelist.&r",
              "",
              "Wer schon in &6Season 1&r dabei war, nutzt im Discord &e/link&r mit seinem Minecraft-Namen und bekommt zwei eigene Plätze für Freunde.",
              "",
              "Termine für die Finale der Stufen und Events stehen dort zuerst.",
          ],
          tasks=[task_checkmark("Bin im Discord")],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="minecraft:bell", size=1.5),

    quest("v_website", 7, 16, "&6Schau auf die Website",
          subtitle="kronwerke.elchi.dev",
          description=[
              "Auf &ekronwerke.elchi.dev&r stehen die Stufen, die Modliste, eine Installationsanleitung, die häufigsten Fragen und eine &eLive-Statusseite&r mit den Zielen.",
              "",
              "Die Statusseite zeigt den Obelisken auch, wenn du gerade nicht online bist.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(3)],
          deps=["v_discord"], icon="minecraft:map"),

    quest("v_origin", 7, 18, "&6Wähl Herkunft und Rolle",
          subtitle="Wer du bist, ändert, wie du spielst.",
          description=[
              "Beim ersten Betreten wählst du eine &6Herkunft&r und eine &6Rolle&r. Neu im Modpack? &6Kronbürger&r und &6Mühlenkind&r sind einfach zu spielen.",
              "",
              "Jede Herkunft hat echte Stärken und eine echte Schwäche. Die Rolle (&6Ingenieur&r, &6Arkanist&r, &6Baumeister&r, &6Entdecker&r, &6Hüter&r, &6Versorger&r, &6Händler&r) gibt kleine Boni passend zu einer Säule. Eine Gruppe mit verschiedenen Rollen kommt schneller voran.",
              "",
              "Keine Herkunft kann fliegen oder überspringt eine Stufe. &eO&r zeigt dir deine Kräfte, mehr in &6Tipps und Tricks&r.",
          ],
          tasks=[task_checkmark("Herkunft und Rolle stehen")],
          rewards=[reward_xp(3)],
          deps=["v_discord"], icon="minecraft:player_head"),

    quest("v_tips", 9.5, 16, "&6Lies Tipps und Tricks",
          subtitle="Questbuch, JEI, Karte, Team, Sprachchat, Tod.",
          description=[
              "Öffne links im Buch das Kapitel &6Tipps und Tricks&r. Dort steht, wie du Belohnungen einsammelst, Rezepte findest, ein Team gründest, den Sprachchat einrichtest und deine Sachen nach dem Tod zurückholst.",
              "",
              "Wer noch nie ein Modpack gespielt hat, liest es ganz. Alle anderen schauen wenigstens auf die &eTasten&r, einige sind doppelt belegt.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(3)],
          deps=["v_website", "v_origin"], icon="minecraft:knowledge_book"),

    quest("v_farms", 9.5, 18, "&6Lies Erste Farmen",
          subtitle="Die Basis arbeitet, während du redest.",
          description=[
              "Öffne das Kapitel &6Erste Farmen&r. Eine Farm pro Quest: Bruchstein, Holz, Weizen, Tiere, Monster, Lava und Mana, alles mit Stufe-1-Mitteln.",
              "",
              "Jede davon kann direkt in deinen Zubringer am Obelisken liefern.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(3)],
          deps=["v_tips"], icon="minecraft:hopper"),

    quest("v_ultimine", 12, 16, "&6Bau mit Ultimine ab",
          subtitle="Eine ganze Ader auf einmal.",
          description=[
              "Halte &e`&r (links neben der 1) gedrückt, während du einen Block abbaust. Alle passenden Blöcke daneben gehen mit: Erzadern, Bäume, eine Reihe Stein.",
              "",
              "Das kostet Hunger, nimm Essen mit. Für die Stein-Säule ist Ultimine dein bester Freund.",
          ],
          tasks=[task_checkmark("Ausprobiert")],
          rewards=[reward_item("minecraft:cooked_beef", 8)],
          deps=["v_tips"], icon="minecraft:diamond_pickaxe"),

    quest("v_sleep", 12, 18, "&6Bau einen Schlafsack",
          subtitle="Unterwegs schlafen, ohne den Spawnpunkt zu verlieren.",
          description=[
              "3 Wolle übereinander: ein &6Schlafsack&r aus Comforts. Damit überspringst du unterwegs die Nacht, dein Spawnpunkt bleibt am Bett.",
              "",
              "Die &6Hängematte&r (Wolle, Faden, Stöcke) macht dasselbe für den Tag. Jede Farbe geht.",
          ],
          tasks=[task_checkmark("Habe einen")],
          rewards=[reward_item("minecraft:cooked_beef", 8)],
          deps=["v_ultimine"], icon="comforts:sleeping_bag_red", optional=True),

    # ---- Deine Wege ------------------------------------------------------------------
    quest("p_hub", 24.5, 2, "&6Such dir einen Weg aus",
          subtitle="Alle Kapitel von Stufe 1, nach Gruppen.",
          description=[
              "Links im Buch stehen die Kapitel in Gruppen: &6Technik&r, &dMagie&r, &aWelt und Erkundung&r, &6Lager und Werkzeug&r und &6Checklisten&r. Rechts von hier ist jedes Kapitel von Stufe 1 ein Haken.",
              "",
              "Die Säulen brauchen &eTechnik und Magie&r. Kannst du dich nicht entscheiden, frag in die Runde, was gerade fehlt. Kapitel späterer Stufen erscheinen, sobald die Stufe offen ist.",
          ],
          tasks=[task_checkmark("Zeig her")],
          rewards=[reward_xp(3)],
          deps=["d_done", "o_event"], icon="minecraft:compass", size=1.75, shape="hexagon"),

    quest("p_create", P1, -4, "&6Öffne Create",
          subtitle="Drehung, Förderbänder, Andesitlegierung.",
          description=[
              "Wasserrad, Wellen und Zahnräder treiben Mahlstein, Presse und Mixer. In Stufe 1 geht es bis Andesit, und genau das füllt die Technik-Säule.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="create:large_cogwheel"),

    quest("p_ars", P1, -2, "&dÖffne Ars Nouveau",
          subtitle="Zauber aus Glyphen, Quelle, Quelljuwelen.",
          description=[
              "Zauber selbst zusammensetzen, Quellgläser, Sternbunkel und die &aImbuement-Kammer&r, der einzige Weg zu Quelljuwelen für die Magie-Säule.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="ars_nouveau:novice_spell_book"),

    quest("p_botania", P1, 0, "&aÖffne Botania",
          subtitle="Blumen, die Mana machen.",
          description=[
              "Reines Gänseblümchen, erzeugende Blumen, Manaverbreiter, Manabecken. In Stufe 1 bis zum Becken, genug für die Manadiamanten im Quellschlussstein.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="botania:pure_daisy"),

    quest("p_mystical", P1, 2, "&aÖffne Mystical Agriculture",
          subtitle="Rohstoffe vom Feld.",
          description=[
              "Inferium, der Infusionsaltar und die ersten Rohstoffsamen. Steinsamen und Feuersamen helfen der Stein-Säule und der Andesitstraße.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="mysticalagriculture:inferium_essence"),

    quest("p_food", P1, 4, "&6Öffne Essen und Landwirtschaft",
          subtitle="Messer, Kochtopf, Felder, Fischerei.",
          description=[
              "Farmer's Delight, Farming for Blockheads und Aquaculture: Mahlzeiten, die lange satt machen, reichhaltige Erde, Tiere und Angeln.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="farmersdelight:cooking_pot"),

    quest("p_cooking", P1, 6, "&6Öffne Kochen",
          subtitle="Die Blockhead-Küche und die besten Mahlzeiten.",
          description=[
              "Kochtisch, Pflanztöpfe und die Mahlzeiten mit der meisten Sättigung. Eine Küche spart dir auf langen Streams viele Wege.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="cookingforblockheads:cooking_table"),

    quest("p_trees", P1, 8, "&aÖffne Productive Trees",
          subtitle="163 Baumarten, Obst, Nüsse, Holz.",
          description=[
              "Bäume vom Markt, Obst und Nüsse, Sägewerk und Kreuzungen. Die Hybriden kaufst du hier am Markt von Farming for Blockheads.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="productivetrees:hazel_sapling"),

    quest("p_irons", P1, 10, "&dÖffne Iron's Spells",
          subtitle="Schriftrollen, Tinte, die ersten Zauber.",
          description=[
              "Schriftrollen, gewöhnliche Tinte und der erste Zauberer. Eine zweite Magie neben Ars Nouveau, die in Stufe 1 schon losgeht.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="irons_spellbooks:copper_spell_book"),

    quest("p_explore", P2, -4, "&6Öffne Erkundung",
          subtitle="Biome, Wegsteine, die Minendimension.",
          description=[
              "Neue Biome, Wegsteine, Bauwerke voller Beute und die Minendimension zum Graben ohne Löcher in der Landschaft.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="minecraft:filled_map"),

    quest("p_bosses", P2, -2, "&cÖffne Bosse der Oberwelt",
          subtitle="Cataclysm, Born in Chaos, Mowzie's Mobs.",
          description=[
              "Die Bosse der Oberwelt in der Reihenfolge, in der man sie schafft. Geht zu zweit oder zu dritt.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="cataclysm:ancient_remnant_spawn_egg"),

    quest("p_storage", P2, 0, "&6Öffne Lager",
          subtitle="Rucksäcke, Schubladen, Truhen.",
          description=[
              "Bruchstein, Erz und Zutaten müssen irgendwohin: Rucksäcke aus Sophisticated Backpacks, Schubladen aus Functional Storage und größere Truhen.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="sophisticatedbackpacks:backpack"),

    quest("p_silent", P2, 2, "&6Öffne Silent Gear",
          subtitle="Werkzeug aus Einzelteilen.",
          description=[
              "Werkzeug, Waffen und Rüstung aus Teilen, deren Material die Werte bestimmt. Schon die Eisenstufe schlägt jedes Vanilla-Eisenwerkzeug.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="silentgear:pickaxe"),

    quest("p_apotheosis", P2, 4, "&6Öffne Apotheosis",
          subtitle="Affixe, Edelsteine, Umschmieden.",
          description=[
              "Beute mit zufälligen Affixen, Edelsteine in Sockeln, der Zaubertisch und Spawner. In Stufe 1 bis zur Seltenheit Selten.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="apotheosis:salvaging_table"),

    quest("p_comfort", P2, 6, "&6Öffne Komfort und Bauen",
          subtitle="Die kleinen Mods, die den Tag leichter machen.",
          description=[
              "&6Komfort&r: Magnete und andere kleine Helfer. &6Bauen&r: Rahmenblöcke, Chipped, Supplementaries und Tipps für eine Basis, die auf dem Stream gut aussieht.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="simplemagnets:basicmagnet"),

    quest("p_lists", P2, 8, "&6Öffne die Checklisten",
          subtitle="Jeder Generator, jedes Werkzeug, jeder Weg.",
          description=[
              "Strom, Werkzeug und Rüstung, Transport und Lager, Dimensionen und Reisen: eine Zeile pro Ding, ein Haken, nach Stufen sortiert. Zum Nachschlagen, nicht zum Durcharbeiten.",
          ],
          tasks=[task_checkmark("Angeschaut")],
          rewards=[reward_xp(2)],
          deps=["p_hub"], icon="minecraft:writable_book"),

    quest("p_ready", 33.5, 2, "&6Leg los",
          subtitle="Technik, Magie oder beides. Der Server braucht beides.",
          description=[
              "Du weißt jetzt, wie Kronwerke funktioniert: Der Server arbeitet gemeinsam auf den Obelisken hin, jede Stufe öffnet sich für alle, und dieses Buch zeigt dir den Weg durch jedes Kapitel.",
              "",
              "Früher oder später schaust du ohnehin in die drei großen Kapitel: &6Create&r, &dArs Nouveau&r und &aBotania&r. Viel Spaß in den Kronwerken.",
          ],
          tasks=[task_checkmark("Auf geht's")],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["p_create", "p_ars", "p_botania", "p_storage", "p_silent", "p_food", "p_explore"],
          icon="minecraft:recovery_compass", size=2.5, shape="gear"),
]

images = [
    banner("start_here/title", "Kronwerke", 0, -2.2, height=1.8, kind="title", colour="brass"),
    banner("start_here/season", "Season 2", 0, 5.2, height=0.7, kind="note", colour="stone"),
    banner("start_here/day", "Die ersten Schritte", 11.5, -9.8, height=0.9, colour="nature"),
    banner("start_here/obelisk", "Der Obelisk", 11.25, -3.2, height=0.9, colour="stone"),
    banner("start_here/milestones", "Die Meilensteine", 11.25, 3.1, height=0.9, colour="magic"),
    banner("start_here/stages", "Stufen und Sperren", 10, 8.2, height=0.9, colour="brass"),
    banner("start_here/server", "Auf dem Server", 8.25, 14.5, height=0.9, colour="water"),
    banner("start_here/paths", "Deine Wege", 28.75, -5.6, height=0.9, colour="magic"),
]

chapter(C, "Hier geht's los", "ftbquests:book", "start", quests, shape="circle", order=0,
        subtitle=["Von Spawn bis zur ersten Abgabe in zehn Schritten, dann Obelisk, Meilensteine, Stufen und alle Kapitel von Stufe 1."],
        images=images)
