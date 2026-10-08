"""Botania in stage 3, the elven side: the gateway (core, natura pylons, mana to open), every
trade one quest (dreamwood, elven quartz, alfglass, elementium in ingots and blocks, pixie dust,
dragonstone), the elven lexicon, the flowers that need pixie dust, the elven spreader and the
conjuration catalyst, the elementium tools and armour with the pixies and the great fairy ring,
the crystal bow, ender essence (diluted from endermen, pure from the pure daisy on end stone,
which leaves cobbled deepslate), Corporea, and the stage 3 magic goal: 400 elementium ingots
and the Elfenstern milestone. The Gaia guardian and everything from it is stage 4 (gaia.py)."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "alfheim"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Das Elfenportal ------------------------------------------------------
    quest("core", 0, 0, "&a&lBau das Elfenportal-Herzstück",
          subtitle="Das Herz des Tors nach Alfheim.",
          description=[
              "Werkbank: &66 Lebeholzstämme&r an den Seiten, &63 Terrastahlklumpen&r in der mittleren Spalte. Ein Terrastahlbarren ergibt 9 Klumpen.",
              "",
              img("botania:textures/block/elven_gateway_core.png", 32, 32),
              "",
              "Mit &6Stufe 3 (Stahlwerk)&r öffnet sich Alfheim. Hinein kommst du nicht, aber die Elfen handeln: Du wirfst etwas durch das Portal, sie werfen etwas Besseres zurück.",
              "",
              "&eKronwerke:&r Das Magieziel von Stufe 3 sind &e400 Elementiumbarren&r, &e150 Afrit-Essenz&r und &e8 Elfensterne&r. Der Handel muss also automatisch laufen.",
          ],
          tasks=[task_item("botania:elven_gateway_core", 1)],
          rewards=[reward_item("botania:livingwood_log", 16), reward_table("s3_common")],
          icon="botania:elven_gateway_core", size=2.0, shape="hexagon"),

    quest("frame", 2.5, 0, "&aStell Rahmen und Pylonen auf",
          subtitle="Lebeholz, Glanz und zwei volle Becken.",
          description=[
              "Rahmen: &68 Lebeholz&r und &63 Schimmerndes Lebeholz&r, das Herzstück unten in der Mitte. Dazu &62 Manabecken&r mit je einem &aNaturapylon&r darauf, im Umkreis von 5 Blöcken.",
              "",
              "&6Schimmerndes Lebeholz:&r Lebeholzstamm und Glowstonestaub. &6Naturapylon:&r Manapylon, 3 Terrastahlklumpen, 1 Enderauge.",
              "",
              "Die Lexica zeigt den Rahmen als Vorschau, die du in die Welt projizieren kannst. Bau Block für Block nach.",
          ],
          tasks=[task_item("botania:natura_pylon", 2), task_item("botania:glimmering_livingwood_log", 3)],
          rewards=[reward_item("minecraft:ender_eye", 2), reward_xp(5)],
          deps=["core"], icon="botania:natura_pylon"),

    quest("open", 5, 0, "&a&lÖffne das Portal",
          subtitle="Ein Klick mit dem Stab, und die Mitte leuchtet.",
          description=[
              "Rechtsklick mit dem &aStab des Waldes&r auf das Herzstück. Das Öffnen kostet &d200 000 Mana&r aus den Becken mit Pylon.",
              "",
              "&eSo handelst du:&r Wirf die Ware hinein, das Ergebnis fliegt heraus. &eJeder Tausch kostet 500 Mana&r. Wird ein Becken leer, schließt sich das Portal.",
              "",
              "&cNiemals Brot hineinwerfen.&r Die Elfen mögen kein Brot, und das Portal explodiert.",
          ],
          tasks=[task_advancement("botania:main/elf_portal_open", "Ein Portal nach Alfheim öffnen")],
          rewards=[reward_item("botania:mana_diamond", 2), reward_table("s3_common")],
          deps=["frame"], icon="botania:wand_of_the_forest", size=1.75, shape="diamond"),

    quest("lexicon", 5, 2.4, "&aSchick die Lexica zu den Elfen",
          subtitle="Das Buch kommt dicker zurück.",
          description=[
              "Wirf deine &aLexica Botania&r durch das Portal. Die Elfen schreiben ihr Wissen hinein und schicken sie zurück.",
              "",
              "Danach stehen Elfenmetalle, neue Blumen, Corporea und Elfenwerkzeug im Buch, mit Rezepten.",
          ],
          tasks=[task_advancement("botania:main/elf_lexicon_pickup", "Die Elfen-Lexica zurückbekommen")],
          rewards=[reward_xp(5)],
          deps=["open"], icon="botania:lexica_botania"),

    # ---- Der Handel ---------------------------------------------------------
    quest("dreamwood", 7.5, 0, "&6Tausch Lebeholz gegen Traumholz",
          subtitle="Der erste und billigste Tausch.",
          description=[
              "Wirf &6Lebeholzstämme&r ins Portal. Für jeden kommt ein &6Traumholzstamm&r zurück, für jedes Lebeholz ein Traumholz.",
              "",
              img("botania:textures/block/dreamwood_log.png", 32, 32),
              "",
              "Traumholz leitet Mana besser als Lebeholz. Du brauchst es für den Elfen-Manaverbreiter und die Traumholzzweige.",
          ],
          tasks=[task_item("botania:dreamwood_log", 16)],
          rewards=[reward_item("botania:livingwood_log", 16), reward_xp(3)],
          deps=["open"], icon="botania:dreamwood_log"),

    quest("wand_elven", 12.5, 1.2, "&6Schnitz Traumholzzweige",
          subtitle="Griffe für alles Elfische.",
          description=[
              "Werkbank: &62 Traumholzstämme&r übereinander ergeben &61 Traumholzzweig&r.",
              "",
              "Zweige stecken in den Elementiumwerkzeugen und im &6Stab des Elfenwaldes&r (3 Zweige, 2 Blütenblätter), der Elfenvariante des Stabs des Waldes.",
          ],
          tasks=[task_item("botania:dreamwood_twig", 4)],
          rewards=[reward_item("botania:dreamwood_log", 8), reward_xp(3)],
          deps=["dreamwood"], icon="botania:dreamwood_twig"),

    quest("elven_quartz", 2.5, 2.4, "&aTausch Quarz gegen Elfenquarz",
          subtitle="Grüner Quarz zum Bauen.",
          description=[
              "Wirf &6Netherquarz&r ins Portal. Pro Stück kommt ein &6Elfenquarz&r zurück.",
              "",
              "Elfenquarz ist reine Deko: Blöcke, Säulen, Ziegel und Stufen in Grün. Ein guter Test mit billiger Ware.",
          ],
          tasks=[task_item("botania:elven_quartz", 8)],
          rewards=[reward_item("minecraft:quartz", 8), reward_xp(3)],
          deps=["open"], icon="botania:elven_quartz", optional=True),

    quest("alfglass", 7.5, 1.2, "&bTausch Managlas gegen Elfenglas",
          subtitle="Daraus werden die Elfenglasflaschen.",
          description=[
              "Wirf &6Managlas&r ins Portal. Pro Block kommt ein &6Elfenglas&r zurück.",
              "",
              "Elfenglas ist sehr klar und sein Muster ändert sich je nach Platz. Wichtiger: Aus ihm werden die Flaschen für Ender-Essenz.",
          ],
          tasks=[task_item("botania:alfglass", 6)],
          rewards=[reward_item("botania:managlass", 6), reward_xp(4)],
          deps=["open"], icon="botania:alfglass"),

    quest("elementium", 10, 0, "&d&lTausch Manastahl gegen Elementium",
          subtitle="Zwei Manastahl rein, ein Elementium raus.",
          description=[
              "Wirf &62 Manastahlbarren&r ins Portal, es kommt &61 Elementiumbarren&r zurück.",
              "",
              pic("botania:elementium_ingot"),
              "",
              "Elementium brauchst du für Elfen-Verbreiter, Zauberkatalysator, Elfenwerkzeug und die Ingenieure je einen Barren für ihren &6Stahlkern&r, den Technik-Meilenstein dieser Stufe.",
          ],
          tasks=[task_item("botania:elementium_ingot", 8)],
          rewards=[reward_item("botania:manasteel_ingot", 8), reward_table("s3_uncommon")],
          deps=["dreamwood"], icon="botania:elementium_ingot", size=1.5, shape="square"),

    quest("elementium_block", 12.5, 0, "&dTausch ganze Blöcke",
          subtitle="Ein Tausch, neun Barren.",
          description=[
              "Wirf &62 Manastahlblöcke&r ins Portal, es kommt &61 Elementiumblock&r zurück, also 9 Barren in einem Tausch.",
              "",
              "&eWarum:&r Jeder Tausch kostet 500 Mana, egal wie groß. Blöcke sparen Mana. Ein Barren und ein Block zusammen geben 5 Barren.",
          ],
          tasks=[task_item("botania:elementium_block", 2)],
          rewards=[reward_item("botania:manasteel_block", 2), reward_xp(8)],
          deps=["elementium"], icon="botania:elementium_block"),

    quest("pixie", 10, 1.2, "&dTausch Manaperlen gegen Feenstaub",
          subtitle="Eine Perle wird zu Staub, der funkelt.",
          description=[
              "Wirf &6Manaperlen&r ins Portal. Für jede kommt ein &dFeenstaub&r zurück.",
              "",
              pic("botania:pixie_dust"),
              "",
              "Feenstaub steckt in den neuen Blumen, im Corporea-Funken, im Zauberkatalysator, im Großen Feenring und zweimal in jedem &dElfenstern&r. Die Perlenfabrik aus Stufe 2 (Messinggehäuse unter dem Becken) läuft einfach weiter.",
          ],
          tasks=[task_item("botania:pixie_dust", 8)],
          rewards=[reward_item("botania:mana_pearl", 4), reward_xp(5)],
          deps=["dreamwood"], icon="botania:pixie_dust"),

    quest("dragonstone", 10, 2.4, "&dTausch Manadiamanten gegen Drachenstein",
          subtitle="Aus Manadiamant wird ein rosa Juwel.",
          description=[
              "Wirf &6Manadiamanten&r ins Portal. Für jeden kommt ein &dDrachenstein&r zurück, für einen Manadiamantblock ein Drachensteinblock.",
              "",
              pic("botania:dragonstone"),
              "",
              "Drachenstein brauchst du für Corporea, den Kristallbogen und viermal für jeden &dElfenstern&r. Gaia-Rüstung und Gaia-Verbreiter kommen erst in Stufe 4.",
          ],
          tasks=[task_item("botania:dragonstone", 8)],
          rewards=[reward_item("botania:mana_diamond", 4), reward_xp(6)],
          deps=["dreamwood"], icon="botania:dragonstone"),

    # ---- Neue Blumen ----------------------------------------------------------
    quest("orechid", 15, 0, "&6Pflanz eine Erchidee",
          subtitle="Aus Stein wird Erz.",
          description=[
              "Apotheke: &62 graue&r, &61 gelbes&r, &61 grünes&r, &61 rotes&r Blütenblatt, &6Rune des Hochmuts&r, &6Rune der Gier&r, &6Redstone-Wurzel&r, &6Feenstaub&r.",
              "",
              "Mit Mana verwandelt sie &eStein&r in ihrer Nähe nach und nach in Erze. Ein Mechanischer Bohrer baut die Erze ab, ein Einsatzgerät setzt neuen Stein.",
              "",
              "Die &6Flammende Erchidee&r macht dasselbe mit Netherrack, aber nur im Nether.",
          ],
          tasks=[task_item("botania:orechid", 1)],
          rewards=[reward_item("botania:redstone_root", 4), reward_xp(6)],
          deps=["pixie"], icon="botania:orechid"),

    quest("kekimurus", 15, 1.2, "&6Pflanz einen Kekimurus",
          subtitle="Kuchen wird zu Mana.",
          description=[
              "Apotheke: &62 weiße&r, &62 orange&r, &62 braune&r Blütenblätter, &6Rune der Völlerei&r, &6Feenstaub&r.",
              "",
              "Er frisst &eKuchen&r, die neben ihm stehen, Stück für Stück. Eine Kuchenfabrik mit Mechanischen Handwerkern von Create macht daraus eine starke Manaquelle.",
          ],
          tasks=[task_item("botania:kekimurus", 1)],
          rewards=[reward_item("minecraft:cake", 4), reward_xp(6)],
          deps=["pixie"], icon="botania:kekimurus"),

    quest("rafflowsia", 10, 4.8, "&6Pflanz eine Rafflorsie",
          subtitle="Frisst Blumen, je bunter, desto besser.",
          description=[
              "Apotheke: &62 lila&r, &62 grüne&r, &61 schwarzes&r Blütenblatt, &6Rune der Erde&r, &6Rune des Hochmuts&r, &6Feenstaub&r.",
              "",
              "Sie frisst Blumen aus der Apotheke, die du um sie pflanzt. Je mehr verschiedene hintereinander, desto mehr Mana.",
          ],
          tasks=[task_item("botania:rafflowsia", 1)],
          rewards=[reward_item("botania:redstone_root", 2), reward_xp(6)],
          deps=["pixie"], icon="botania:rafflowsia", optional=True, section="blumen"),

    quest("spectrolus", 12.5, 4.8, "&6Pflanz eine Spektrole",
          subtitle="Frisst Wolle in der richtigen Farbe.",
          description=[
              "Apotheke: &62 rote&r, &62 grüne&r, &62 blaue&r, &62 weiße&r Blütenblätter, &6Rune des Winters&r, &6Rune der Luft&r, &6Feenstaub&r.",
              "",
              "Sie frisst &eWolle&r in der Farbe, die sie gerade will, dann die nächste Farbe im Kreis. Der Lebenzahn braucht eine Gaia-Seele und kommt in Stufe 4.",
          ],
          tasks=[task_item("botania:spectrolus", 1)],
          rewards=[reward_item("minecraft:white_wool", 16), reward_xp(6)],
          deps=["pixie"], icon="botania:spectrolus", optional=True, section="blumen"),

    # ---- Elfenwerkzeug --------------------------------------------------------
    quest("spreader", 2.5, 7.6, "&6Bau Elfen-Manaverbreiter",
          subtitle="Mehr Mana, schneller, weiter.",
          description=[
              "Werkbank: oben und unten je &63 Traumholzstämme&r, in der Mitte &61 Elementiumbarren&r und &61 Blütenblatt&r.",
              "",
              "Er schießt größere Manastöße, schneller und weiter, und verliert unterwegs weniger. Tausch die Verbreiter an deinen besten Blumen aus, dann bleiben die Becken am Portal voll.",
          ],
          tasks=[task_item("botania:elven_mana_spreader", 4)],
          rewards=[reward_item("botania:dreamwood_log", 16), reward_xp(6)],
          deps=["elementium"], icon="botania:elven_mana_spreader"),

    quest("conjuration", 5, 7.6, "&6Bau den Zauberkatalysator",
          subtitle="Das Becken verdoppelt Rohstoffe.",
          description=[
              "Werkbank: &61 Alchemiekatalysator&r in der Mitte, &63 Elementiumbarren&r, &61 Feenstaub&r, &64 Lebestein&r drumherum.",
              "",
              "Unter ein Manabecken gestellt, macht das Becken aus &eRedstone&r, &eGlowstonestaub&r, &eQuarz&r, &eKohle&r, Schnee, Netherrack, Seelensand, Kies, Laub oder Gras jeweils zwei.",
          ],
          tasks=[task_item("botania:conjuration_catalyst", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(6)],
          deps=["elementium"], icon="botania:conjuration_catalyst"),

    quest("elementium_gear", 5, 8.8, "&6Bau eine Elementiumspitzhacke",
          subtitle="Werkzeug, das Schutt vernichtet.",
          description=[
              "Werkbank: &63 Elementiumbarren&r und &62 Traumholzzweige&r wie eine Eisenspitzhacke.",
              "",
              "&eSpitzhacke:&r vernichtet Bruchstein, Erde, Netherrack und ähnlichen Schutt beim Abbauen. &eSchaufel:&r baut eine Säule Kies oder Sand auf einmal ab. &eAxt:&r schlägt manchmal Köpfe ab. &eHacke:&r macht Ackerland sofort feucht.",
          ],
          tasks=[task_item("botania:elementium_pickaxe", 1)],
          rewards=[reward_item("botania:elementium_ingot", 3), reward_xp(8)],
          deps=["wand_elven", "conjuration"], icon="botania:elementium_pickaxe"),

    quest("elementium_armor", 5, 10, "&6Trag Elementiumrüstung",
          subtitle="Feen kämpfen für dich.",
          description=[
              "Werkbank: Elementiumbarren in Rüstungsform, &624 Barren&r für alle vier Teile.",
              "",
              "Sie schützt wie Manastahl und repariert sich mit Mana aus deinem Inventar. Wirst du getroffen, erscheint manchmal eine &dFee&r und greift den Angreifer an. Je mehr Teile, desto öfter.",
          ],
          tasks=[task_item("botania:elementium_helmet", 1), task_item("botania:elementium_chestplate", 1),
                 task_item("botania:elementium_leggings", 1), task_item("botania:elementium_boots", 1)],
          rewards=[reward_item("botania:elementium_ingot", 4), reward_xp(10)],
          deps=["elementium_gear"], icon="botania:elementium_chestplate"),

    quest("fairy_ring", 5, 11.2, "&dSteck den Großen Feenring an",
          subtitle="Mehr Feen bei jedem Treffer.",
          description=[
              "Werkbank: &61 Feenstaub&r und &64 Elementiumbarren&r ergeben den &6Großen Feenring&r. Leg ihn in einen Schmuckplatz.",
              "",
              "Er erhöht die Chance, dass bei einem Treffer eine Fee erscheint, auch ohne Elementiumrüstung. Zusammen mit der Rüstung am stärksten.",
          ],
          tasks=[task_item("botania:great_fairy_ring", 1)],
          rewards=[reward_item("botania:pixie_dust", 4), reward_xp(8)],
          deps=["elementium_armor"], icon="botania:great_fairy_ring", optional=True),

    quest("crystal_bow", 10, 3.6, "&dSpann den Kristallbogen",
          subtitle="Pfeile aus Mana.",
          description=[
              "Werkbank: &62 Drachensteine&r, &63 Manainfundierte Fäden&r, &61 Lebeholzzweig&r. Das ergibt den &6Kristallbogen&r.",
              "",
              "Er zaubert Pfeile aus Mana wie mit Unendlichkeit und repariert sich mit Mana.",
          ],
          tasks=[task_item("botania:crystal_bow", 1)],
          rewards=[reward_item("botania:dragonstone", 2), reward_xp(8)],
          deps=["dragonstone"], icon="botania:crystal_bow", optional=True, section="werkzeug"),

    # ---- Ender-Essenz und Corporea -------------------------------------------
    quest("flask", 7.5, 7.6, "&bBlas Elfenglasflaschen",
          subtitle="Leere Flaschen für die Essenz.",
          description=[
              "Werkbank: &63 Elfenglas&r in V-Form ergeben &63 Elfenglasflaschen&r.",
              "",
              "Mit einer leeren Flasche fängst du Ender-Essenz ein: Rechtsklick auf die kleine Wolke, bevor sie verfliegt. Ein Werfer vor der Wolke macht das auch.",
          ],
          tasks=[task_item("botania:alfglass_flask", 6)],
          rewards=[reward_item("botania:alfglass", 3), reward_xp(4)],
          deps=["alfglass"], icon="botania:alfglass_flask"),

    quest("ender_essence", 10, 7.6, "&5Zapf Endermen ab",
          subtitle="Verdünnte Ender-Essenz mit dem Seelendolch.",
          description=[
              "Werkbank: &6Manaperle&r, &6Manastahlbarren&r und &6Lebeholzzweig&r übereinander ergeben den &6Seelendolch&r. Triff einen &5Enderman&r damit und fang die Wolke mit einer Elfenglasflasche.",
              "",
              "Außerhalb des End gibt das nur &5Verdünnte Ender-Essenz&r. Für Corporea-Funken und den Corporea-Trichter reicht sie.",
          ],
          tasks=[task_item("botania:diluted_ender_essence", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(5)],
          deps=["flask"], icon="botania:diluted_ender_essence"),

    quest("pure_essence", 12.5, 7.6, "&5Reinige Endstein",
          subtitle="Das Gänseblümchen macht Tiefschiefer und reine Essenz.",
          description=[
              "Stell &6Endstein&r um ein &6Reines Gänseblümchen&r. Es macht daraus &6Bruchtiefschiefer&r und lässt dabei eine Wolke &5Reine Ender-Essenz&r frei. Fang sie mit einer Elfenglasflasche.",
              "",
              "&eEndstein ohne End:&r Der &5Possessed Endermite&r aus Occultism lässt Endstein fallen. Eine Flasche Reine Essenz auf Stein geworfen macht wieder Endstein, damit schließt sich der Kreis.",
          ],
          tasks=[task_item("botania:pure_ender_essence", 4)],
          rewards=[reward_item("minecraft:cobbled_deepslate", 16), reward_xp(8)],
          deps=["flask"], icon="botania:pure_ender_essence"),

    quest("corporea_spark", 7.5, 8.8, "&dBau Corporea-Funken",
          subtitle="Funken, die Items statt Mana tragen.",
          description=[
              "Werkbank: &6Manafunke&r, &6Feenstaub&r und &6Ender-Essenz&r ergeben &64 Corporea-Funken&r. Ein Funke und ein Drachenstein ergeben den &6Corporea-Hauptfunken&r.",
              "",
              "Setz einen Funken auf jede Truhe, die zum Netz gehört. Funken verbinden sich im Umkreis von etwa 8 Blöcken. Jedes Netz braucht &egenau einen&r Hauptfunken.",
              "",
              "Gefärbte Funken bilden getrennte Netze. Corporea-Blöcke tragen Funken ohne Truhe und verlängern das Netz.",
          ],
          tasks=[task_item("botania:corporea_spark", 4), task_item("botania:master_corporea_spark", 1)],
          rewards=[reward_item("botania:mana_spark", 4), reward_xp(6)],
          deps=["ender_essence", "pixie", "dragonstone"], icon="botania:corporea_spark"),

    quest("corporea_funnel", 10, 8.8, "&dBau einen Corporea-Trichter",
          subtitle="Items auf Redstone-Signal.",
          description=[
              "Werkbank: &67 Corporea-Blöcke&r, &61 Ender-Essenz&r, &61 Redstone&r. Das ergibt den &6Corporea-Trichter&r.",
              "",
              "Bei einem Redstone-Signal holt er ein Item aus dem Netz in das Inventar darunter. Welches, bestimmt ein Rahmen am Trichter, die Drehung die Menge (1, 2, 4 bis 64).",
              "",
              "&eTipp:&r Trichter über einem Werfer, der ins Portal zielt, liefert Ware direkt aus dem Lager in den Handel.",
          ],
          tasks=[task_item("botania:corporea_funnel", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_table("s3_common")],
          deps=["corporea_spark"], icon="botania:corporea_funnel"),

    quest("corporea_index", 12.5, 8.8, "&dBau einen Corporea-Index",
          subtitle="Items auf Zuruf im Chat.",
          description=[
              "Werkbank: &62 Reine Ender-Essenz&r, &64 Obsidian&r, &61 Corporea-Block&r, &62 Drachensteine&r.",
              "",
              "Steh davor und schreib in den Chat, zum Beispiel &e\"64 cobblestone\"&r. Die Items fallen vor dir heraus. Im Inventar geht es auch mit der Maus auf einem Item und der Corporea-Taste.",
          ],
          tasks=[task_item("botania:corporea_index", 1)],
          rewards=[reward_item("botania:corporea_spark", 4), reward_xp(10)],
          deps=["corporea_funnel", "pure_essence"], icon="botania:corporea_index"),

    # ---- Fuer den Obelisken ---------------------------------------------------
    quest("elementium_line", 17.5, 7.6, "&dBau eine Elementium-Straße",
          subtitle="Der Handel muss automatisch laufen.",
          description=[
              "Sammle &664 Elementiumbarren&r aus einer automatischen Linie: Manastahl kommt aus dem Becken, wird zu Blöcken gepresst, Blöcke fliegen ins Portal, eine Trichtermalve sammelt das Elementium ein.",
              "",
              "&eKronwerke:&r Das Ziel will &e400 Elementiumbarren&r (Menge passt sich der Spielerzahl an), also &e800 Manastahlbarren&r. Der Obelisk will Barren, die Blöcke also vorher wieder zerlegen.",
              "",
              "Halt die Becken am Portal mit Elfen-Verbreitern und starken Blumen voll. Jeder Tausch kostet 500 Mana.",
          ],
          tasks=[task_item("botania:elementium_ingot", 64)],
          rewards=[reward_item("botania:manasteel_block", 4), reward_table("s3_uncommon")],
          deps=["elementium_block", "spreader"], icon="botania:elementium_block"),

    quest("elven_star", 20, 7.6, "&d&lBau einen Elfenstern",
          subtitle="Der Meilenstein der Magie in Stufe 3.",
          description=[
              "Werkbank: Ecken &d4 Drachensteine&r, oben und unten &d2 Feenstaub&r, links und rechts &c2 Afrit-Essenz&r, Mitte &71 Verstärkte Legierung&r.",
              "",
              img("kronwerke:textures/item/elven_star.png", 32, 32),
              "",
              "Afrit-Essenz kommt von einem besiegten Afrit aus Occultism, die Verstärkte Legierung aus dem Metallurgischen Infusionierer von Mekanism. Frag die Techniker.",
              "",
              "&eKronwerke:&r Der Obelisk will &e8 Elfensterne&r, dazu 400 Elementium und 150 Afrit-Essenz. Ist auch die Technik voll, öffnet &6Stufe 4 (Sternwerk)&r mit dem End und dem Gaia-Wächter.",
          ],
          tasks=[task_item("kronwerke:elven_star", 1)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["elementium_line"], icon="kronwerke:elven_star", size=2.0, shape="gear"),
    # ---- Neu: Nebenquests ------------------------------------------------
    quest("crafty_crate", 7.5, 2.4, "&6Bau eine Schlaue Kiste",
          subtitle="Eine Werkbank, die Trichter versteht.",
          description=[
              "&6Schlaue Kiste&r: oben Traumholzbretter, &6Werkbank&r, Traumholzbretter, darunter links und rechts je zwei Traumholzbretter. &6Herstellungsplatzhalter&r: formlos Werkbank und Lebestein ergeben &e32&r.",
              "",
              "Die Kiste füllt ihre 9 Plätze von links oben nach rechts unten. Ein Platzhalter steht für ein leeres Feld. Sind alle 9 Plätze belegt, craftet sie sofort und wirft Ergebnis, Platzhalter und Reste aus.",
              "",
              "Ein Rechtsklick mit dem Stab des Waldes craftet sofort und wirft den Inhalt aus, das kann auch ein Werfer mit dem Stab. Muster auf der Kiste sperren feste Felder wie Platzhalter.",
          ],
          tasks=[task_item("botania:crafty_crate", 1), task_item("botania:crafting_placeholder", 32)],
          rewards=[reward_item("botania:dreamwood_planks", 16), reward_xp(6)],
          deps=["dreamwood"], icon="botania:crafty_crate", optional=True, section="corporea"),

    quest("red_string", 7.5, 10, "&5Spann Rotfaden",
          subtitle="Blöcke über Entfernung verbinden.",
          description=[
              "&6Rotfaden&r: formlos &6Faden&r, &6Redstoneblock&r, &6Feenstaub&r und &5Reine Ender-Essenz&r. &6Rotfadenbehälter&r: &e7 Lebestein&r, eine Truhe in der Mitte, rechts daneben der Rotfaden.",
              "",
              "Jeder Rotfaden-Block bindet sich an den nächsten passenden Block, auf den er zeigt, bis etwa &e8 Blöcke&r weit und durch Wände. Der Behälter gibt alles, was hineinkommt, an das gebundene Inventar weiter, von derselben Seite.",
              "",
              "Dazu gibt es Werfer, Nährer (Knochenmehl auf Distanz), Komparator, Täuscher (eine Blume wirkt an einer anderen Stelle) und Abfänger. Mit dem Stab des Waldes in der Hand siehst du die Fäden.",
          ],
          tasks=[task_item("botania:red_string", 2), task_item("botania:red_stringed_container", 1)],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_xp(6)],
          deps=["pure_essence"], icon="botania:red_string", optional=True),

    quest("resolute_ivy", 10, 10, "&5Bind Entschlossenen Efeu an",
          subtitle="Ein Gegenstand, den du beim Tod behältst.",
          description=[
              "Formlos: &6Feenstaub&r, &6Ranke&r und &5Reine Ender-Essenz&r.",
              "",
              "Leg den Efeu zusammen mit einem Gegenstand in die Werkbank. Stirbst du, bleibt dieser Gegenstand in deinem Inventar, der Efeu wird dabei verbraucht.",
              "",
              "Nicht für Dinge, die beim Craften etwas zurücklassen, etwa einen Wassereimer. Für Terraklinge und Elementiumrüstung lohnt es sich.",
          ],
          tasks=[task_item("botania:resolute_ivy", 2)],
          rewards=[reward_item("minecraft:vine", 8), reward_xp(5)],
          deps=["pure_essence"], icon="botania:resolute_ivy", optional=True),

    quest("slime_bottle", 12.5, 10, "&bFüll Schleim in eine Flasche",
          subtitle="Ein Schleimchunk-Finder.",
          description=[
              "Oben Elementium, &6Elfenglas&r, Elementium, Mitte Elementium, &6Schleimball&r, Elementium, unten Mitte Elementium.",
              "",
              "In einem Bereich, in dem unterirdisch Schleime spawnen, erwacht der Schleim in der Flasche und hüpft herum. So findest du Schleimchunks für eine Schleimfarm oder für die &6Narglibbe&r.",
          ],
          tasks=[task_item("botania:slime_in_a_bottle", 1)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_xp(4)],
          deps=["flask"], icon="botania:slime_in_a_bottle", optional=True),

    quest("orechid_ignem", 17.5, 0, "&6Pflanz eine Flammende Erchidee",
          subtitle="Nether-Erze aus Netherrack.",
          description=[
              "Apotheke: &62 rote&r, &62 weiße&r, &61 rosa&r Blütenblatt, &6Rune des Hochmuts&r, &6Rune der Gier&r, &6Redstone-Wurzel&r, &6Feenstaub&r.",
              "",
              "Sie wandelt &eNetherrack&r in ihrer Nähe mit Mana nach und nach in Nether-Erze um. Sie arbeitet nur im &cNether&r, also bring Becken und Verbreiter mit.",
          ],
          tasks=[task_item("botania:orechid_ignem", 1)],
          rewards=[reward_item("minecraft:netherrack", 32), reward_xp(6)],
          deps=["orechid"], icon="botania:orechid_ignem", optional=True),

    quest("entropinnyum", 17.5, 1.2, "&6Pflanz ein Entropinnyum",
          subtitle="TNT wird zu Mana.",
          description=[
              "Apotheke: &62 rote&r, &62 graue&r, &62 weiße&r Blütenblätter, &6Rune des Zorns&r, &6Rune des Feuers&r.",
              "",
              "Zündest du TNT auf festem Boden neben ihr, schluckt sie die ganze Explosion und macht Mana daraus, ohne Schaden. Das klappt nur, solange ihr Speicher leer ist. Sonst knallt es wie immer.",
              "",
              "&cAchtung:&r Verdoppeltes TNT mag sie nicht, dann sinkt die Ausbeute stark. Eine TNT-Straße mit echtem Sand und Schwarzpulver ist die Lexica-Aufgabe dazu.",
          ],
          tasks=[task_item("botania:entropinnyum", 1)],
          rewards=[reward_item("minecraft:tnt", 4), reward_xp(6)],
          deps=["kekimurus"], icon="botania:entropinnyum", optional=True),

    quest("loonium", 20, 0, "&6Pflanz ein Loonium",
          subtitle="Schatzbeute gegen Mana, mit Wächtern.",
          description=[
              "Apotheke: &64 grüne&r, &61 graues&r Blütenblatt, &6Runen der Trägheit, Völlerei und des Neides&r, &6Redstone-Wurzel&r, &6Feenstaub&r.",
              "",
              "Für viel Mana ruft das Loonium Beute herbei, wie aus einem Verlies. Jedes Teil trägt aber ein besonders starkes Monster, das du erst besiegen musst.",
              "",
              "Steht es in einem großen Bauwerk, etwa einer Festung oder einem Tempel, gibt es die Beute dieses Bauwerks.",
          ],
          tasks=[task_item("botania:loonium", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(6)],
          deps=["orechid"], icon="botania:loonium", optional=True),

    quest("elven_lenses", 12.5, 2.4, "&dSchleif Elfenlinsen",
          subtitle="Linsen, die teleportieren und zielen.",
          description=[
              "&eVerzerrungslinse&r: formlos Manalinse und Feenstaub. Trifft der Stoß ein Kraftrelais, springt er zu dessen Ziel. Hinter einer Bohrlinse kombiniert schickt sie abgebaute Blöcke zum Verbreiter zurück.",
              "&eAuslöserlinse&r: formlos Manalinse, Stolperdrahthaken und Elementium. Der Verbreiter feuert nur, wenn der Stoß ein Wesen oder einen Spieler treffen würde.",
              "",
              "Dazu kommen Umleitung, Feier, Leuchtsignal und Farbschleuder, alle in der Lexica.",
          ],
          tasks=[task_item("botania:warp_lens", 1), task_item("botania:tripwire_lens", 1)],
          rewards=[reward_item("botania:pixie_dust", 2), reward_xp(5)],
          deps=["pixie"], icon="botania:warp_lens", optional=True, section="werkzeug"),

    quest("spark_augments", 12.5, 3.6, "&dPass deine Funken an",
          subtitle="Mana zwischen Becken lenken.",
          description=[
              "Jede formlos aus &6Feenstaub&r, &6Manastahl&r und einer Rune: &eDispersiv&r (Wasser) lädt Mana-Gegenstände von Spielern in der Nähe, &eDominant&r (Feuer) zieht Mana aus Becken mit normalen Funken, &eRezessiv&r (Erde) verteilt sein Mana an die anderen, &eIsoliert&r (Luft) hält sich aus allem heraus.",
              "",
              "Anpassungen gehen nur auf Funken über Manabecken, eine pro Funken.",
              "",
              "Der &6Funken-Bastler&r (2 Elementium, 3 Lebestein, Redstone) neben einem Becken tauscht bei einem Redstone-Signal seine Anpassung mit der eines Funkens.",
          ],
          tasks=[task_item("botania:spark_augment_dominant", 1), task_item("botania:spark_augment_recessive", 1),
                 task_item("botania:spark_augment_dispersive", 1)],
          rewards=[reward_item("botania:pixie_dust", 2), reward_xp(5)],
          deps=["elementium"], icon="botania:spark_augment_dominant", optional=True, section="werkzeug"),

    quest("world_seed", 7.5, 3.6, "&dPflanz einen Weltsamen",
          subtitle="Ein Sprung zurück zur Spawn.",
          description=[
              "&6Grasblock&r, darunter &6Weizensamen&r, darunter &6Drachenstein&r. Das ergibt &e4 Weltsamen&r.",
              "",
              "Rechtsklick bringt dich sofort zum Spawnpunkt der Welt, wenn du mindestens &e24 Blöcke&r davon entfernt bist. Der Samen wird dabei verbraucht.",
              "",
              "&eKronwerke:&r Am Spawn steht der Obelisk. Mit ein paar Samen in der Tasche ist der Weg zum Abgeben kurz.",
          ],
          tasks=[task_item("botania:world_seed", 4)],
          rewards=[reward_item("minecraft:wheat_seeds", 16), reward_xp(4)],
          deps=["dragonstone"], icon="botania:world_seed", optional=True, section="werkzeug"),

]

images = [
    banner("alfheim/title", "Botania: Alfheim", 10, -8.2, height=1.8, kind="title", colour="nature"),
    banner("alfheim/portal", "Das Elfenportal", 3.75, -1.4, height=0.9, colour="nature"),
    banner("alfheim/handel", "Der Handel", 10, -1.4, height=0.9, colour="magic"),
    banner("alfheim/blumen", "Neue Blumen", 17.5, -1.4, height=0.9, colour="nature"),
    banner("alfheim/werkzeug", "Elfenwerkzeug", 3.75, 6.2, height=0.9, colour="nature"),
    banner("alfheim/corporea", "Ender-Essenz und Corporea", 10, 6.2, height=0.9, colour="magic"),
    banner("alfheim/obelisk", "Für den Obelisken", 18.75, 6.2, height=0.9, colour="magic"),
]

chapter(C, "Botania: Alfheim", "botania:elven_gateway_core", "magic", quests, shape="circle", order=24, stage=3,
        subtitle=["Stufe 3. Das Elfenportal, jeder Tausch, Elementium, Feen, Ender-Essenz, Corporea und der Elfenstern."], images=images)
