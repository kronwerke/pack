"""Botania in stage 3: the elven gateway (core, natura pylons, 200 000 mana to open), the trade
with Alfheim (dreamwood, elementium, pixie dust, dragonstone), the elven lexicon, the flowers and
tools that need elven materials (orechid, kekimurus, elven spreader, conjuration catalyst,
elementium gear), ender essence and Corporea, and the stage 3 magic goal: 400 elementium ingots
and the Elfenstern milestone. The Gaia guardian and everything from it is stage 4."""
from ftbq import (chapter, quest, task_item, task_advancement, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "alfheim"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Das Elfenportal ------------------------------------------------------
    quest("core", 0, 0, "&aElfenportal-Herzstück",
          subtitle="Das Stahlwerk öffnet das Tor nach Alfheim.",
          description=[
              "Mit &6Stufe 3 (Stahlwerk)&r öffnet sich Alfheim. Die Elfen leben in ihrer eigenen Welt und lassen keinen Menschen hinein, aber sie handeln mit dir: Du wirfst Dinge durch ein Portal, und sie werfen etwas Besseres zurück.",
              "",
              "Das Herz des Portals ist das &aElfenportal-Herzstück&r (Elven Gateway Core). Du craftest es aus &e6 Lebeholzstämmen&r an den Seiten und &e3 Terrastahlklumpen&r in der mittleren Spalte. Ein Terrastahlbarren ergibt neun Klumpen, du brauchst also nur einen Barren.",
              "",
              img("botania:textures/block/elven_gateway_core.png", 32, 32),
              "",
              "&eKronwerke:&r Das Magieziel von Stufe 3 heißt &e400 Elementiumbarren&r, &e150 Afrit-Essenz&r und &e8 Elfensterne&r. Der Handel mit Alfheim muss also automatisch laufen. Dieses Kapitel zeigt dir, wie.",
          ],
          tasks=[task_item("botania:elven_gateway_core", 1)],
          rewards=[reward_item("botania:livingwood_log", 16), reward_table("s3_common")],
          icon="botania:elven_gateway_core", size=2.0, shape="hexagon"),

    quest("frame", 2.6, 0, "&aRahmen und Pylonen",
          subtitle="Lebeholz, ein wenig Glanz und zwei volle Becken.",
          description=[
              "Das Portal ist ein aufrechter Rahmen. Du brauchst &e8 Lebeholz&r (jede Variante, auch Stämme oder entrindet) und &e3 Schimmerndes Lebeholz&r, dazu das Herzstück unten in der Mitte. Schimmerndes Lebeholz ist ein Lebeholzstamm mit Glowstonestaub an der Werkbank.",
              "",
              "Die Lexica zeigt den Rahmen auf der Seite zu Alfheim als Vorschau, die du in die Welt projizieren kannst. Bau Block für Block nach, dann passt alles.",
              "",
              "Dazu kommen mindestens &e2 Manabecken&r mit je einem &aNaturapylon&r direkt darüber, alle im Umkreis von 5 Blöcken um das Herzstück. Ein Naturapylon ist ein Manapylon mit &e3 Terrastahlklumpen&r und einem &eEnderauge&r.",
              "",
              "&eTipp:&r Die Becken sollten voll sein und es bleiben. Das Portal zieht gleichmäßig aus allen Becken mit Pylon, und wenn eines leer ist, schließt es sich.",
          ],
          tasks=[task_item("botania:natura_pylon", 2), task_item("botania:glimmering_livingwood_log", 3)],
          rewards=[reward_item("minecraft:ender_eye", 2), reward_xp(5)],
          deps=["core"], icon="botania:natura_pylon"),

    quest("open", 5.2, 0, "&aDas Portal öffnet sich",
          subtitle="200 000 Mana für einen Blick nach Alfheim.",
          description=[
              "Steht alles, klickst du mit dem &aStab des Waldes&r auf das Herzstück. Das Öffnen kostet einmalig &d200 000 Mana&r aus den Becken mit Pylon, danach leuchtet die Mitte des Rahmens.",
              "",
              "So handelst du: Wirf die Ware in das Portal. Sobald die Elfen ein passendes Angebot haben, fliegt das Ergebnis wieder heraus. &eJeder Tausch kostet 500 Mana&r, die Becken müssen also weiter gefüllt werden. Was die Elfen nicht kennen, behalten sie als Geschenk.",
              "",
              "&cAchtung:&r Wirf niemals &cBrot&r hinein. Die Elfen mögen kein Brot, und das Portal explodiert.",
              "",
              "&eTipp:&r Ein Werfer, ein Create-Förderband oder ein Trichter vor dem Portal bringt die Ware hinein, eine Trichtermalve davor sammelt das Ergebnis wieder ein.",
          ],
          tasks=[task_advancement("botania:main/elf_portal_open", "Ein Portal nach Alfheim öffnen")],
          rewards=[reward_item("botania:mana_diamond", 2), reward_table("s3_common")],
          deps=["frame"], icon="botania:wand_of_the_forest", size=1.75, shape="diamond"),

    quest("lexicon", 5.2, 2.4, "&aDie Lexica für die Elfen",
          subtitle="Ein Buch auf Reisen.",
          description=[
              "Wirf deine &aLexica Botania&r durch das Portal. Die Elfen lesen sie, schreiben ihr Wissen hinein und schicken sie zurück. Danach stehen dir viele neue Seiten offen: die Elfenmetalle, neue Blumen, Corporea und die Elfenwerkzeuge.",
              "",
              "Alles, was in diesem Kapitel kommt, steht dann auch in deinem Buch, mit Rezepten und Bildern.",
          ],
          tasks=[task_advancement("botania:main/elf_lexicon_pickup", "Die Elfen-Lexica zurückbekommen")],
          rewards=[reward_xp(5)],
          deps=["open"], icon="botania:lexica_botania"),

    # ---- Der Handel ---------------------------------------------------------
    quest("dreamwood", 7.8, 0, "&6Traumholz",
          subtitle="Der erste Tausch, und der billigste.",
          description=[
              "Für jeden &6Lebeholzstamm&r bekommst du einen &6Traumholzstamm&r, für jedes Lebeholz ein Traumholz. Ein guter erster Test, ob dein Portal richtig läuft.",
              "",
              img("botania:textures/block/dreamwood_log.png", 32, 32),
              "",
              "Traumholz leitet Mana besser als Lebeholz. Du brauchst es für den &6Elfen-Manaverbreiter&r, und zwei Stämme übereinander ergeben &6Traumholzzweige&r für den &6Stab des Elfenwaldes&r und die Elementiumwerkzeuge.",
          ],
          tasks=[task_item("botania:dreamwood_log", 16)],
          rewards=[reward_item("botania:livingwood_log", 16)],
          deps=["open"], icon="botania:dreamwood_log"),

    quest("elementium", 10.4, 0, "&dElementium",
          subtitle="Zwei Manastahl rein, ein Elementium raus.",
          description=[
              "Das wichtigste Angebot der Elfen: &e2 Manastahlbarren&r ergeben &e1 Elementiumbarren&r, &e2 Manastahlblöcke&r einen &dElementiumblock&r.",
              "",
              pic("botania:elementium_ingot"),
              "",
              "&eSpar Mana mit Blöcken:&r Jeder Tausch kostet 500 Mana, egal wie groß. Zwei Blöcke ergeben neun Barren in einem einzigen Tausch. Eine gemischte Ladung aus einem Barren und einem Block gibt fünf Barren.",
              "",
              "Elementium brauchst du für den Elfen-Manaverbreiter, die Erchidee, den Zauberkatalysator und die Elementiumwerkzeuge. Die Ingenieure brauchen je einen Barren für ihren &6Stahlkern&r, den Technik-Meilenstein dieser Stufe.",
          ],
          tasks=[task_item("botania:elementium_ingot", 8)],
          rewards=[reward_item("botania:manasteel_ingot", 8), reward_table("s3_uncommon")],
          deps=["dreamwood"], icon="botania:elementium_ingot", size=1.5, shape="square"),

    quest("pixie", 10.4, -2.4, "&dFeenstaub",
          subtitle="Eine Manaperle wird zu Staub, der funkelt.",
          description=[
              "Für jede &bManaperle&r geben dir die Elfen einen &dFeenstaub&r (Pixie Dust).",
              "",
              pic("botania:pixie_dust"),
              "",
              "Feenstaub steckt in den neuen Blumen, im Corporea-Funken, im Zauberkatalysator und im Großen Feenring. Und jeder &dElfenstern&r braucht zwei davon.",
              "",
              "&eTipp:&r Die Perlenfabrik aus Stufe 2 mit dem Messinggehäuse unter dem Becken läuft hier einfach weiter. Ein Förderband von dort zum Portal, und der Staub kommt von selbst.",
          ],
          tasks=[task_item("botania:pixie_dust", 8)],
          rewards=[reward_item("botania:mana_pearl", 4)],
          deps=["dreamwood"], icon="botania:pixie_dust"),

    quest("dragonstone", 10.4, 2.4, "&dDrachenstein",
          subtitle="Aus Manadiamant wird ein rosa Juwel.",
          description=[
              "Ein &bManadiamant&r wird im Portal zum &dDrachenstein&r, ein Manadiamantblock zum Drachensteinblock.",
              "",
              pic("botania:dragonstone"),
              "",
              "Drachenstein brauchst du für den Corporea-Hauptfunken und den Corporea-Index, für den &6Kristallbogen&r (zwei Drachensteine, ein Lebeholzzweig, drei Manafäden), der Pfeile aus Mana zaubert, und vier davon für jeden &dElfenstern&r.",
              "",
              "Die Gaia-Rüstung und der Gaia-Verbreiter brauchen ebenfalls Drachenstein, die kommen aber erst in Stufe 4.",
          ],
          tasks=[task_item("botania:dragonstone", 8)],
          rewards=[reward_item("botania:mana_diamond", 4)],
          deps=["dreamwood"], icon="botania:dragonstone"),

    # ---- Neue Blumen ----------------------------------------------------------
    quest("orechid", 13, -3.4, "&6Erchidee",
          subtitle="Aus Stein wird Erz.",
          description=[
              "Die &6Erchidee&r (Orechid) braucht &e2 graue&r, &e1 gelbes&r, &e1 grünes&r und &e1 rotes&r Blütenblatt, die &5Runen des Hochmuts und der Gier&r, eine &6Redstone-Wurzel&r und einen &dFeenstaub&r.",
              "",
              "Mit Mana aus einem Becken verwandelt sie &eStein&r in ihrer Nähe nach und nach in Erze. Seltene Erze kommen seltener. Ein Mechanischer Bohrer von Create baut die fertigen Erze ab, ein Einsatzgerät setzt neuen Stein, und die Blume arbeitet von allein weiter.",
              "",
              "Die &6Flammende Erchidee&r macht dasselbe mit Netherrack und Nether-Erzen, arbeitet aber nur im Nether.",
          ],
          tasks=[task_item("botania:orechid", 1)],
          rewards=[reward_item("botania:redstone_root", 4), reward_xp(5)],
          deps=["pixie"], icon="botania:orechid"),

    quest("kekimurus", 13, -1.6, "&6Kekimurus und Freunde",
          subtitle="Kuchen, Blumen und Wolle werden zu Mana.",
          description=[
              "Mit Feenstaub öffnen sich neue Manablumen. Jede will etwas anderes:",
              "",
              "&6Kekimurus&r (&e2 weiß, 2 orange, 2 braun&r, Rune der Völlerei, Feenstaub): frisst &eKuchen&r, die du neben ihr abstellst, Stück für Stück. Eine Kuchenfabrik mit Mechanischen Handwerkern von Create macht daraus eine starke Manaquelle.",
              "&6Rafflorsie&r (Rafflowsia, &e2 lila, 2 grün, 1 schwarz&r, Runen der Erde und des Hochmuts, Feenstaub): frisst Blumen aus der Apotheke, die du um sie pflanzt. Je mehr verschiedene, desto mehr Mana.",
              "&6Spektrole&r (Spectrolus, &e2 rot, 2 grün, 2 blau, 2 weiß&r, Runen des Winters und der Luft, Feenstaub): frisst &eWolle&r in der Farbe, die sie gerade will, dann die nächste Farbe im Kreis.",
              "",
              "Der &6Lebenzahn&r (Dandelifeon) braucht eine Gaia-Seele und kommt in Stufe 4.",
          ],
          tasks=[task_item("botania:kekimurus", 1)],
          rewards=[reward_item("minecraft:cake", 4), reward_xp(5)],
          deps=["pixie"], icon="botania:kekimurus", optional=True),

    # ---- Elfenwerkzeug --------------------------------------------------------
    quest("spreader", 13, 0, "&6Elfen-Manaverbreiter",
          subtitle="Mehr Mana, schneller, weiter.",
          description=[
              "Der &6Elfen-Manaverbreiter&r wird wie der normale gebaut, nur mit &eTraumholz&r statt Lebeholz und einem &dElementiumbarren&r statt Gold: oben und unten je drei Traumholzstämme, in der Mitte Elementium und ein Blütenblatt.",
              "",
              "Er schießt größere Manastöße, schneller und weiter, und verliert unterwegs weniger. Aus ihm lässt sich allerdings kein Impuls-Verbreiter machen.",
              "",
              "&eTipp:&r Tausch die Verbreiter an deinen besten Blumen aus. Die Becken am Portal füllen sich dann spürbar schneller.",
          ],
          tasks=[task_item("botania:elven_mana_spreader", 4)],
          rewards=[reward_item("botania:dreamwood_log", 16), reward_xp(5)],
          deps=["elementium"], icon="botania:elven_mana_spreader"),

    quest("conjuration", 13, 1.6, "&6Zauberkatalysator",
          subtitle="Rohstoffe aus reinem Mana.",
          description=[
              "Der &6Zauberkatalysator&r (Conjuration Catalyst) ist ein &6Alchemiekatalysator&r aus Stufe 2 mit &e3 Elementiumbarren&r, &e1 Feenstaub&r und &e4 Lebestein&r drumherum.",
              "",
              "Stell ihn unter ein Manabecken, und das Becken verdoppelt einfache Rohstoffe: Wirf &eRedstone&r, &eGlowstonestaub&r, &eQuarz&r, &eKohle&r, Schnee, Netherrack, Seelensand, Kies, Laub oder Gras hinein, und es kommen zwei heraus.",
              "",
              "&eTipp:&r Redstone und Glowstone brauchst du jetzt ständig, zum Beispiel für geladenen Certus-Quarz in der Imbuement-Kammer.",
          ],
          tasks=[task_item("botania:conjuration_catalyst", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(5)],
          deps=["elementium"], icon="botania:conjuration_catalyst"),

    quest("elementium_gear", 13, 3.2, "&6Elementiumwerkzeug",
          subtitle="Werkzeuge mit Eigenheiten.",
          description=[
              "Elementiumwerkzeuge craftest du mit &eTraumholzzweigen&r wie Eisenwerkzeuge. Jedes hat eine besondere Fähigkeit:",
              "",
              "&eSpitzhacke:&r vernichtet Bruchstein, Erde, Netherrack und ähnlichen Schutt beim Abbauen, nur Erze und gute Blöcke bleiben übrig. Schleichend bleibt manches erhalten.",
              "&eSchaufel:&r baut eine ganze Säule Kies oder Sand auf einmal ab.",
              "&eAxt:&r schlägt Monstern und Spielern manchmal den Kopf ab, Plünderung erhöht die Chance.",
              "&eHacke:&r macht Ackerland sofort feucht.",
              "",
              "Die Elementiumrüstung schützt wie Manastahl, heilt sich mit Mana und ruft manchmal eine &dFee&r, die deinen Angreifer jagt. Der &6Große Feenring&r (Feenstaub und Elementium) macht das häufiger.",
          ],
          tasks=[task_item("botania:elementium_pickaxe", 1)],
          rewards=[reward_item("botania:elementium_ingot", 3)],
          deps=["elementium"], icon="botania:elementium_pickaxe", optional=True),

    # ---- Corporea -------------------------------------------------------------
    quest("ender_essence", 7.8, 2.4, "&5Ender-Essenz",
          subtitle="Eine Wolke aus dem End, in einer Flasche.",
          description=[
              "Corporea braucht &5Ender-Essenz&r. Ins End kommst du erst in Stufe 4, aber es geht auch so:",
              "",
              "&e1.&r Tausch &6Managlas&r gegen &6Elfenglas&r. Drei Elfenglas in V-Form ergeben drei leere &6Elfenglasflaschen&r.",
              "&e2.&r Crafte einen &6Seelendolch&r (Soulscribe): eine Manaperle, ein Manastahlbarren und ein Lebeholzzweig übereinander.",
              "&e3.&r Triff einen &5Enderman&r mit dem Dolch. Er stößt eine kleine Wolke aus, die schnell verfliegt. Rechtsklick mit der leeren Flasche auf die Wolke, und du hast &5Verdünnte Ender-Essenz&r.",
              "",
              "&5Reine Ender-Essenz&r entsteht, wenn das Reine Gänseblümchen &eEndstein&r umwandelt. Endstein bekommst du jetzt schon vom &5Possessed Endermite&r aus Occultism. Eine Flasche reine Essenz auf Stein geworfen macht wieder Endstein daraus.",
          ],
          tasks=[task_item("botania:diluted_ender_essence", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["dreamwood"], icon="botania:diluted_ender_essence"),

    quest("corporea_spark", 7.8, 5.2, "&dCorporea-Funke",
          subtitle="Funken, die Items statt Mana tragen.",
          description=[
              "Ein &6Manafunke&r, ein &dFeenstaub&r und eine &5Ender-Essenz&r ergeben &e4 Corporea-Funken&r. Mit einem &dDrachenstein&r wird einer davon zum &dCorporea-Hauptfunken&r.",
              "",
              "So funktioniert es: Setz einen Funken auf jede Truhe, die zum Netz gehören soll. Funken verbinden sich mit allen anderen im Umkreis von etwa acht Blöcken, und das Netz kann beliebig weit reichen. Jedes Netz braucht &egenau einen&r Hauptfunken.",
              "",
              "Ein Funke sieht die Truhe unter sich, kann aber nichts hineinlegen. Dafür nimmst du Trichter oder Förderbänder. Mit Farbstoff gefärbte Funken bilden getrennte Netze. &6Corporea-Blöcke&r aus Lebesteinziegeln tragen Funken ohne Truhe und verlängern so dein Netz.",
          ],
          tasks=[task_item("botania:corporea_spark", 4), task_item("botania:master_corporea_spark", 1)],
          rewards=[reward_item("botania:mana_spark", 4), reward_xp(5)],
          deps=["ender_essence"], icon="botania:corporea_spark"),

    quest("corporea_funnel", 10.4, 5.2, "&dCorporea-Trichter und Index",
          subtitle="Items auf Zuruf.",
          description=[
              "Der &6Corporea-Trichter&r (7 Corporea-Blöcke, Ender-Essenz, Redstone) holt bei einem Redstone-Signal ein Item aus dem Netz und schiebt es in das Inventar ein bis zwei Blöcke darunter. Welches Item, bestimmst du mit einem Rahmen am Trichter, die Drehung des Rahmens die Menge (1, 2, 4, 8 bis 64).",
              "",
              "Der &6Corporea-Index&r (2 Reine Ender-Essenz, 4 Obsidian, ein Corporea-Block und 2 Drachensteine) hört auf den Chat. Steh davor und schreib zum Beispiel &e\"64 cobblestone\"&r oder &e\"iron...\"&r, und die Items fallen vor dir heraus. Du kannst auch im Inventar mit der Maus auf ein Item zeigen und die Corporea-Taste drücken.",
              "",
              "&eTipp:&r Ein Corporea-Trichter über einem Spender, der ins Portal zielt, liefert die Ware für den Handel direkt aus dem Lager.",
          ],
          tasks=[task_item("botania:corporea_funnel", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_table("s3_common")],
          deps=["corporea_spark", "dragonstone"], icon="botania:corporea_funnel"),

    # ---- Fuer den Obelisken ---------------------------------------------------
    quest("elementium_line", 15.6, 0, "&dElementium am Fließband",
          subtitle="Der Handel mit Alfheim muss automatisch laufen.",
          description=[
              "&eKronwerke:&r Das Ziel will &e400 Elementiumbarren&r (die Menge passt sich der Spielerzahl an). Das sind &e800 Manastahlbarren&r. Von Hand wirfst du das nicht durch.",
              "",
              "&eSo wird daraus eine Fabrik:&r",
              "&e1.&r Eisen auf den &aNatural Altar&r, Infused Iron ins Manabecken, Manastahl kommt heraus. Ein Create-Förderband verbindet alles.",
              "&e2.&r Neun Barren zum Block pressen, mit einer Mechanischen Presse über einem Becken von Create, und &eBlöcke&r ins Portal werfen. Ein Tausch für neun Barren statt viereinhalb.",
              "&e3.&r Eine Trichtermalve am Portal sammelt die Elementiumblöcke ein, eine Truhe am Obelisken nimmt sie an. Der Obelisk will Barren, also die Blöcke vorher wieder zerlegen.",
              "&e4.&r Die Becken am Portal mit Elfen-Verbreitern und starken Blumen voll halten. Jeder Tausch kostet 500 Mana.",
          ],
          tasks=[task_item("botania:elementium_ingot", 64)],
          rewards=[reward_item("botania:manasteel_block", 4), reward_table("s3_uncommon")],
          deps=["spreader"], icon="botania:elementium_block"),

    quest("elven_star", 18.2, 0, "&dElfenstern",
          subtitle="Der Meilenstein der Magie in Stufe 3.",
          description=[
              "Der &dElfenstern&r ist der Magie-Meilenstein von Stufe 3. In ihm kommen Alfheim, Occultism und Mekanism zusammen.",
              "",
              img("kronwerke:textures/item/elven_star.png", 32, 32),
              "",
              "&eRezept an der Werkbank:&r",
              "Oben: &dDrachenstein&r, &dFeenstaub&r, &dDrachenstein&r.",
              "Mitte: &cAfrit-Essenz&r, &7Verstärkte Legierung&r, &cAfrit-Essenz&r.",
              "Unten: &dDrachenstein&r, &dFeenstaub&r, &dDrachenstein&r.",
              "",
              "Ein Stern kostet also vier Drachensteine, zwei Feenstaub, zwei &cAfrit-Essenzen&r (jede ein besiegter Afrit aus Occultism) und eine &7Verstärkte Legierung&r (Reinforced Alloy) aus dem Metallurgischen Infusionierer von Mekanism. Die bekommst du von den Technikern, oder du baust sie dir selbst.",
              "",
              "&eKronwerke:&r Der Obelisk will &e8 Elfensterne&r, eine feste Zahl. Jeder zählt auf der Leiste sehr viel. Dazu kommen die &e400 Elementiumbarren&r und &e150 Afrit-Essenzen&r. Erst wenn auch die Technikseite voll ist, öffnet &6Stufe 4 (Sternwerk)&r mit dem End und dem Gaia-Wächter.",
          ],
          tasks=[task_item("kronwerke:elven_star", 1)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["elementium_line"], icon="kronwerke:elven_star", size=2.0, shape="gear"),
]

images = [
    banner("alfheim/title", "Botania: Alfheim", 9, -6.6, height=1.8, kind="title", colour="nature"),
    banner("alfheim/portal", "Das Elfenportal", 2.6, -1.8, height=0.9, colour="nature"),
    banner("alfheim/handel", "Der Handel", 8.6, -3.7, height=0.9, colour="magic"),
    banner("alfheim/blumen", "Neue Blumen", 13.2, -4.6, height=0.9, colour="nature"),
    banner("alfheim/werkzeug", "Elfenwerkzeug", 16.4, 2.6, height=0.9, colour="nature"),
    banner("alfheim/corporea", "Corporea", 5.0, 5.2, height=0.9, colour="magic"),
    banner("alfheim/obelisk", "Für den Obelisken", 16.9, -1.6, height=0.9, colour="magic"),
]

chapter(C, "Botania: Alfheim", "botania:elven_gateway_core", "magic", quests, shape="circle", order=24, stage=3,
        subtitle=["Stufe 3. Das Elfenportal, Elementium, Corporea und der Elfenstern."], images=images)
