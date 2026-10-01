"""Ars Nouveau in stage 3: the Summon Wilden ritual and the Wilden Chimera, the Wither for its
nether star, the Archmage Spell Book and the tier 3 glyphs, Ars Elemental's Mark of Mastery,
the Ars Technica tier 3 glyphs (Obliterate, Superheat), and what else opens with stage 3:
the flight, awakening and disintegration rituals, rotating and timer turrets, the Arcanist and
Battlemage robes, and charged certus quartz from the imbuement chamber. Sorcerer robes, the
tier 3 armor upgrade (chorus fruit) and the glyphs that need dragon's breath or elytra are stage 4."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_master"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Die Chimaere -------------------------------------------------------------
    quest("wilden_ritual", 0, 0, "&5Ritual: Beschwöre Wilden",
          subtitle="Der Weg zum Meister führt durch einen Bosskampf.",
          description=[
              "Mit &6Stufe 3&r öffnet sich die höchste Stufe, die Ars Nouveau auf Kronwerke vor dem End kennt: das &6Erzmagier-Zauberbuch&r und die &dGlyphen der Stufe 3&r. Dafür brauchst du einen &5Wilden-Tribut&r, und den gibt nur die &5Wilden-Chimäre&r.",
              "",
              "Die Ritualtafel &5Beschwöre Wilden&r craftest du formlos aus einem &5Ärgerlichen Archwood-Stamm&r, &e3 Wilden-Teilen&r (Stachel, Horn oder Flügel, beliebig gemischt) und einem &9Lapisblock&r.",
              "",
              "Ohne Zusätze ruft das Ritual für kurze Zeit eine zufällige Gruppe Wilden. Wirf vor dem Start je einen &eWilden-Stachel&r, ein &eWilden-Horn&r und einen &eWilden-Flügel&r auf das Kohlenbecken, dann erscheint stattdessen die &5Chimäre&r.",
              "",
              "In diesem Kapitel geht es außerdem um alles, was mit dem Stahlwerk bei Ars neu dazukommt: Flug, neue Rituale, Zaubertürme mit Timer, Magierroben und geladenen Certus-Quarz für die Techniker.",
          ],
          tasks=[task_item("ars_nouveau:ritual_wilden_summon", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 16), reward_table("s3_common")],
          icon="ars_nouveau:ritual_wilden_summon", size=2.0, shape="hexagon"),

    quest("tribute", 2.6, 0, "&5Wilden-Chimäre",
          subtitle="Stachel, Horn und Flügel in einem Körper.",
          description=[
              "Die &5Chimäre&r ist ein echter Boss. Sie springt, schießt Stacheln, gräbt sich ein und gerät irgendwann in Raserei. &cBeim Erscheinen zerstört sie die Blöcke rund um das Kohlenbecken&r, also führ das Ritual draußen auf freiem Feld durch und nicht in deiner Werkstatt.",
              "",
              "Geht zu zweit oder zu dritt, mit guter Rüstung, Heiltränken und deinen besten Kampfzaubern. Besiegt lässt sie einen &5Wilden-Tribut&r fallen.",
              "",
              pic("ars_nouveau:wilden_tribute"),
              "",
              "Den Tribut brauchst du für das &6Erzmagier-Zauberbuch&r, das &6Mal der Meisterschaft&r von Ars Elemental, den &6Fokus der Beschwörung&r und das &6Mark of Technomancy&r von Ars Technica. Eine Chimäre reicht also nicht lange.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s3_uncommon")],
          deps=["wilden_ritual"], icon="ars_nouveau:wilden_tribute"),

    quest("mark_of_mastery", 2.6, -2.2, "&6Mal der Meisterschaft",
          subtitle="Ars Elemental: aus einem Tribut werden fünf Male.",
          description=[
              "In der &aImbuement-Kammer&r wird ein &5Wilden-Tribut&r für &d10 000 Quelle&r zu &e5 Malen der Meisterschaft&r. Auf den Podesten liegen die acht Essenzen: Erde, Feuer, Wasser, Luft, Abschwörung, Beschwörung, Manipulation und die &6Anima-Essenz&r. Die Anima-Essenz machst du in derselben Kammer aus einem Quelljuwel mit Witherskelettschädel, Knochenmehl und Goldenem Apfel.",
              "",
              "Mit einem Mal im &aBezaubernden Apparat&r wird ein &6Kleiner Fokus&r aus Stufe 1 zum großen &6Fokus&r seines Elements, für 5 000 Quelle. Der große Fokus verstärkt und verbilligt die Glyphen seiner Schule, ohne die anderen Schulen zu schwächen, und gibt einen eigenen Bonus. Der Feuerfokus etwa schenkt dir Zauberschaden II, solange du brennst oder in Lava stehst.",
          ],
          tasks=[task_item("ars_elemental:mark_of_mastery", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 4)],
          deps=["tribute"], icon="ars_elemental:mark_of_mastery", optional=True),

    quest("nether_star", 5.2, 0, "&fNetherstern",
          subtitle="Für das Buch muss auch der Wither fallen.",
          description=[
              "Das Erzmagier-Buch verlangt einen &fNetherstern&r. Den gibt nur der &8Wither&r.",
              "",
              "Du baust ihn aus &e4 Seelensand&r in T-Form und &e3 Witherskelettschädeln&r obendrauf. Die Schädel lassen Witherskelette in Netherfestungen fallen, mit Plünderung öfter.",
              "",
              "&cAchtung:&r Der Wither zerstört Blöcke und verteilt den Wither-Effekt. Ruf ihn tief unter der Erde oder weit weg von allen Basen, am besten mit Freunden. Ein Wither gibt genau einen Stern, aber zu mehreren sammelt ihr die Schädel schneller.",
          ],
          tasks=[task_item("minecraft:nether_star", 1)],
          rewards=[reward_item("minecraft:soul_sand", 8), reward_xp(10)],
          deps=["tribute"], icon="minecraft:nether_star"),

    quest("archmage_book", 7.8, 0, "&dErzmagier-Zauberbuch",
          subtitle="Das dritte Buch: Glyphen der Stufe 3.",
          description=[
              "Das &dErzmagier-Zauberbuch&r (Archmage Spell Book) craftest du formlos aus deinem &6Zauberbuch des Magiers&r, &e3 Enderperlen&r, &e2 Smaragden&r, einem &6Totem der Unsterblichkeit&r, dem &fNetherstern&r und dem &5Wilden-Tribut&r. Alle gelernten Glyphen und gespeicherten Zauber wandern mit.",
              "",
              img("ars_nouveau:textures/item/spellbook_purple.png", 32, 32),
              "",
              "Nur mit diesem Buch kannst du &dGlyphen der Stufe 3&r lernen und benutzen. Jede kostet am Tisch des Schreibers &e160 Erfahrungspunkte&r, von null aus gerechnet etwa &e10 Level&r, dazu ihre Zutaten. Das Buch hebt außerdem dein maximales Mana und deine Regeneration noch einmal deutlich an.",
              "",
              "Drei Glyphen der Stufe 3 brauchen Drachenatem oder Elytren aus dem End: &dVerweilen&r, &dWand&r und &dGleiten&r. Die kommen in Stufe 4.",
          ],
          tasks=[task_item("ars_nouveau:archmage_spell_book", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 32), reward_table("s3_uncommon")],
          deps=["nether_star"], icon="ars_nouveau:archmage_spell_book", size=2.0, shape="diamond"),

    # ---- Glyphen der Stufe 3 -------------------------------------------------------
    quest("glyph_blink", 10.6, -3.6, "&dBlinzeln",
          subtitle="Teleport auf Knopfdruck.",
          description=[
              "&dBlinzeln&r (Blink) kostet eine &6Manipulationsessenz&r und &e4 Enderperlen&r. Es teleportiert dich an den Zielort. &eSelbst, Blinzeln&r springt ein Stück nach vorn, &eProjektil, Blinzeln&r bringt dich dorthin, wo die Kugel einschlägt. Verstärken vergrößert die Strecke.",
              "",
              "Hältst du eine beschriebene &6Warp-Schriftrolle&r in der zweiten Hand, schickt Blinzeln ein getroffenes Wesen an den Ort auf der Rolle. Zaubertürme und Runen können das auch, mit einer Rolle in einem Inventar daneben, ohne sie zu verbrauchen.",
              "",
              "Ebenfalls Stufe 3: &dImmateriell&r (Intangible, 3 Phantomhaut, 2 Enderperlen, Manipulationsessenz) macht Blöcke für kurze Zeit zu Luft. Damit gehst du durch Wände und sie schließen sich hinter dir wieder.",
          ],
          tasks=[task_item("ars_nouveau:glyph_blink", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_blink"),

    quest("glyph_lightning", 10.6, -1.8, "&dBlitz",
          subtitle="Ein Gewitter aus dem Zauberbuch.",
          description=[
              "&dBlitz&r (Lightning) braucht eine &fLuftessenz&r, &e3 Blitzableiter&r und ein &bHerz des Meeres&r. Es ruft einen Blitz an den Zielort.",
              "",
              "Getroffene Wesen bekommen den Effekt &eSchock&r, der bis Stufe III wächst und jeden weiteren Blitzschaden verstärkt. Nasse Gegner und solche, die Geräte mit Strom tragen, trifft es besonders hart.",
              "",
              "&eProjektil, Blitz, Verstärken&r ist ein einfacher und sehr starker Kampfzauber. Gegen Gruppen wird er mit &dPlatzen&r noch besser.",
          ],
          tasks=[task_item("ars_nouveau:glyph_lightning", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 16)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_lightning"),

    quest("glyph_burst", 10.6, 0, "&dPlatzen",
          subtitle="Alles in einer Kugel um das Ziel.",
          description=[
              "&dPlatzen&r (Burst) kostet eine &6Manipulationsessenz&r, &e5 TNT&r und einen &6Feuerwerksstern&r. Es wirkt den Rest des Zaubers in einer Kugel rund um das Ziel, also auf alle Wesen darin.",
              "",
              "&dAOE&r vergrößert den Radius. Mit &dEmpfindlich&r trifft es Blöcke statt Wesen, mit &dDämpfen&r nur eine hohle Kugelschale.",
              "",
              "Beispiele: &eProjektil, Platzen, Blitz&r gegen eine Gruppe Monster. &eBerühren, Platzen, Empfindlich, Brechen&r gräbt eine Kugel aus dem Berg.",
          ],
          tasks=[task_item("ars_nouveau:glyph_burst", 1)],
          rewards=[reward_item("minecraft:tnt", 8)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_burst"),

    quest("glyph_split", 10.6, 1.8, "&dTeilen",
          subtitle="Ein Zauber, viele Kugeln.",
          description=[
              "&dTeilen&r (Split) braucht einen &6Splitter&r (das Quellrelais aus Stufe 2), einen &6Wilden-Stachel&r und eine &6Steinsäge&r. Hinter &dProjektil&r verschießt es mehrere Projektile auf einmal, jedes mit dem ganzen Zauber.",
              "",
              "&dOrbit&r (Kompass, Enderauge, Lohenrute) ist eine Form der Stufe 3: drei Kugeln kreisen um dich und treffen alles, was ihnen zu nahe kommt. Mit Teilen werden es mehr, mit Empfindlich treffen sie auch Blöcke.",
          ],
          tasks=[task_item("ars_nouveau:glyph_split", 1)],
          rewards=[reward_item("minecraft:stonecutter", 1), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_split"),

    quest("glyph_summon", 10.6, 3.6, "&dBeschwörungen",
          subtitle="Verbündete aus dem Nichts.",
          description=[
              "Die Beschwörungs-Glyphen der Stufe 3 brauchen alle eine &6Beschwörungsessenz&r:",
              "",
              "&dVex beschwören&r (dazu ein Totem der Unsterblichkeit): drei Vexe kämpfen eine Weile für dich.",
              "&dUntote beschwören&r (Knochen, Witherskelettschädel): Skelette als Verbündete. Verstärken gibt ihnen bessere Schwerter, Durchschlag Bögen, Teilen macht mehr.",
              "&dReißzähne&r (2 Prismarinsplitter, Totem): Fangzähne wie beim Magier (Evoker) aus dem Waldanwesen.",
              "&dLockvogel beschwören&r (4 Rüstungsständer): eine Kopie von dir, die alle Monster auf sich zieht.",
              "",
              "Dazu passen &dVerhexen&r (Hex) und &dVerdorren&r (Wither) aus der Abschwörung. Hex lässt Gegner mehr Schaden nehmen und halbiert ihre Heilung.",
          ],
          tasks=[task_item("ars_nouveau:glyph_summon_vex", 1)],
          rewards=[reward_item("minecraft:totem_of_undying", 1)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_summon_vex"),

    quest("technica", 13.4, 0, "&6Obliterate und Superheat",
          subtitle="Ars Technica: die Meisterglyphen für Create.",
          description=[
              "&bArs Technica&r bringt zwei Glyphen der Stufe 3, die Create-Maschinen ersetzen:",
              "",
              "&dObliterate&r (Manipulationsessenz, Amboss, Diamantblock) schlägt mit einem arkanen Hammer zu. Mit &dEmpfindlich&r verarbeitet es Items wie ein Paar &6Brechräder&r, mit Glück gibt es mehr Nebenprodukte. Gegen Monster ist es eine ziemlich brutale Waffe.",
              "",
              "&dSuperheat&r (3 Feueressenz, Lohenrute, Lohenkuchen) macht aus &dFuse&r ein überhitztes Mischen und aus &dPress&r mit Extrakt ein überhitztes Verdichten, wie ein Lohenbrenner mit Kuchen.",
              "",
              "Press, Polish, Obliterate und Whirl wirken auch auf ein &6Depot&r von Create. Ein Zauberturm über einem Depot ist eine kleine Fabrik ohne Wasserrad.",
          ],
          tasks=[task_item("ars_technica:glyph_obliterate", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(5)],
          deps=["glyph_burst"], icon="ars_technica:glyph_obliterate"),

    quest("archmage", 17.0, 0, "&dErzmagier",
          subtitle="Bereit für die Sterne.",
          description=[
              "Du kämpfst mit Blitz und Platzen, springst mit Blinzeln durch die Gegend, lässt Vexe und Skelette für dich kämpfen und verarbeitest Erz mit einem Hammer aus Quelle.",
              "",
              "Leg einen großen Vorrat an &6Quelljuwelblöcken&r an. Mit &6Stufe 4&r kommen die &dSorcerer-Roben&r, die dritte Rüstungsstufe, das &dVoid Prism&r und die Glyphen, die Drachenatem brauchen. Das alles verschlingt Quelle in großen Mengen.",
              "",
              "&eKronwerke:&r Auf der Magieseite will der Obelisk in dieser Stufe Elementium aus Alfheim, Afrit-Essenz aus Occultism und Elfensterne. Hilf mit: Deine Quelle lädt den Certus-Quarz der Techniker, und mit Blitz und Platzen bist du die beste Begleitung für jede Afrit-Beschwörung.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 32),
                 task_checkmark("Einen Zauber mit Glyphen der Stufe 3 gebaut")],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["technica", "glyph_split", "glyph_summon"], icon="ars_nouveau:archmage_spell_book",
          size=2.5, shape="gear"),

    # ---- Neu im Stahlwerk ------------------------------------------------------------
    quest("stahlwerk", 0, 5.0, "&aNeu im Stahlwerk",
          subtitle="Was Ars mit Stufe 3 sonst noch öffnet.",
          description=[
              "Nicht alles in Stufe 3 braucht das Erzmagier-Buch. Mit dem Stahlwerk öffnen bei Ars auch:",
              "",
              "&e1.&r Die Rituale &aFlug&r, &aErwachen&r, &aZerfall&r, &aVerziehen&r (Warping) und die beiden &aInseln beschwören&r.",
              "&e2.&r Der &aVerstellbare Zauberturm&r und der &aTimer-Zauberturm&r.",
              "&e3.&r Die Roben des &6Arkanisten&r und des &6Kampfmagiers&r.",
              "",
              "&aVerziehen&r (Warping: Ärgerlicher Stamm und eine Warp-Schriftrolle) bringt alle Wesen in der Nähe an den Ort auf einer zusätzlich eingelegten Schriftrolle. &aInsel beschwören&r (Grasblock oder Sand mit Erdessenz) baut eine runde Insel aus Gras oder Sand mit Radius 7, jedes Quelljuwel als Zusatz macht sie um einen Block größer.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("ars_nouveau:source_gem", 8)],
          deps=["wilden_ritual"], icon="ars_nouveau:ritual_brazier"),

    quest("ritual_flight", 2.6, 3.6, "&aRitual: Flug",
          subtitle="Fliegen wie im Kreativmodus, solange die Quelle reicht.",
          description=[
              "Die Tafel: &5Ärgerlicher Archwood-Stamm&r, &e3 Wilden-Flügel&r, &e2 Diamanten&r und eine &6Enderperle&r.",
              "",
              "Solange das Ritual läuft, bekommen Spieler in der Nähe beim Springen den Effekt &eFlug&r und können eine Weile frei fliegen wie im Kreativmodus. Bist du in der Nähe, frischt das Ritual den Effekt immer wieder auf. Jedes Mal zieht es Quelle aus Gläsern in der Nähe.",
              "",
              "&eTipp:&r Ein Flugritual mitten auf der Baustelle spart viele Gerüste. Stell genug Quellgläser daneben.",
          ],
          tasks=[task_item("ars_nouveau:ritual_flight", 1)],
          rewards=[reward_item("ars_nouveau:wilden_wing", 3), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:ritual_flight"),

    quest("ritual_awakening", 5.2, 3.6, "&aErwachen und Zerfall",
          subtitle="Wächter aus Bäumen, Erfahrung aus Monstern.",
          description=[
              "&aErwachen&r (Blühender Archwood-Stamm, je ein Setzling der vier Archwood-Farben, 4 Quelljuwelen): Bäume aus Archwood in der Nähe erwachen zu &dWaldläufern&r (Weald Walker), die einen Ort gegen Monster bewachen. Knospender Amethyst wird zu &dAmethystgolems&r, die Amethyst für dich ernten.",
              "",
              "&aZerfall&r (Flammender Archwood-Stamm, 3 Goldschwerter, 3 Bücher): Monster in der Nähe zerfallen zu &6Erfahrungsjuwelen&r, die doppelt so viel Erfahrung wert sind. Beute lassen sie dabei keine fallen, und jedes Monster kostet etwas Quelle.",
              "",
              "&eTipp:&r Zerfall am Ausgang einer Monsterfarm ist die schnellste Quelle für die 160 Erfahrungspunkte jeder Glyphe der Stufe 3.",
          ],
          tasks=[task_item("ars_nouveau:ritual_awakening", 1), task_item("ars_nouveau:ritual_disintegration", 1)],
          rewards=[reward_item("ars_nouveau:greater_experience_gem", 4)],
          deps=["ritual_flight"], icon="ars_nouveau:ritual_disintegration", optional=True),

    quest("turrets", 2.6, 5.0, "&aTimer- und Verstellbarer Zauberturm",
          subtitle="Türme, die von selbst feuern und überall hinzielen.",
          description=[
              "Der &aVerstellbare Zauberturm&r entsteht formlos aus einem Einfachen Zauberturm. Mit dem &6Dominion-Zauberstab&r richtest du ihn aus: erst den Turm anklicken, dann den Zielblock. Er kann in jede Richtung zielen, auch schräg.",
              "",
              "Der &aTimer-Zauberturm&r ist ein Einfacher Zauberturm mit einer &6Uhr&r im Bezaubernden Apparat. Er feuert von selbst, am Anfang jede Sekunde. Rechtsklick verlängert die Zeit, ein Schlag verkürzt sie, schleichend geht es in Schritten von 10 Sekunden. Ein Redstone-Signal oder 0 Sekunden schalten ihn ab, mit dem Dominion-Zauberstab sperrst du die Einstellung.",
              "",
              "Projektil, Berühren, Empfindlich und Redstone kosten beim Timer-Turm keine Quelle. Ein Turm mit &eBerühren, Ernte&r über einem Feld braucht also kaum etwas.",
          ],
          tasks=[task_item("ars_nouveau:timer_spell_turret", 1), task_item("ars_nouveau:rotating_spell_turret", 1)],
          rewards=[reward_item("minecraft:clock", 2), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:timer_spell_turret"),

    quest("robes", 2.6, 6.4, "&6Roben des Arkanisten",
          subtitle="Rüstung, die Mana schenkt.",
          description=[
              "Die Magierroben entstehen im &aBezaubernden Apparat&r aus einem normalen Rüstungsteil und &e4 Magieblütenfasern&r. Aus Eisen werden die Teile des &6Arkanisten&r, aus Diamant die des &6Kampfmagiers&r. Der Kampfmagier schützt mehr, der Arkanist hat stärkere Plätze für Fäden.",
              "",
              "Alle Roben erhöhen deine Manaregeneration. Am &6Änderungstisch&r (Tisch des Schreibers mit 4 Magieblütenfasern) setzt du &6Fäden&r ein: mehr Mana, Zauberschaden, Schutz vor Magie, Selbstreparatur und vieles mehr. Leere Fäden bestehen aus 6 Magieblütenfasern und 3 Goldklumpen.",
              "",
              "Die erste Aufwertung der Rüstungsstufe kostet im Apparat &e2 Lohenruten&r und &d2 500 Quelle&r pro Teil. Die zweite braucht Chorusfrüchte aus dem End und kommt in Stufe 4.",
          ],
          tasks=[task_item("ars_nouveau:arcanist_robes", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 16)],
          deps=["stahlwerk"], icon="ars_nouveau:arcanist_robes"),

    quest("charged_certus", 0, 6.8, "&bGeladener Certus-Quarz",
          subtitle="Kronwerke: das ME-Netz braucht einen Magier.",
          description=[
              "&eKronwerke:&r Geladener Certus-Quarz aus AE2 entsteht hier nicht im Lader. Der erste Weg führt über die &aImbuement-Kammer&r: ein &bCertus-Quarzkristall&r in die Kammer, &eRedstone&r und &eGlowstonestaub&r auf die Podeste, &d2 000 Quelle&r, und heraus kommt ein geladener Kristall.",
              "",
              img("ae2:textures/item/certus_quartz_crystal_charged.png", 32, 32),
              "",
              "Ohne geladenen Certus gibt es keinen Fluix und damit kein ME-Netz. Die Techniker brauchen also deine Kammern und deine Quelle. Später kann eine Energizing Orb von Powah zwei Kristalle auf einmal laden, aber den Anfang macht die Magie.",
              "",
              "&eTipp:&r Mehrere Kammern nebeneinander, ein Relais-Netz aus deiner Quelllink-Farm und ein Trichter für die fertigen Kristalle, und du wirst zum wichtigsten Lieferanten auf dem Server.",
          ],
          tasks=[task_item("ae2:charged_certus_quartz_crystal", 16)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 16), reward_table("s3_uncommon")],
          deps=["stahlwerk"], icon="ae2:charged_certus_quartz_crystal"),
]

images = [
    banner("ars_master/title", "Ars Nouveau: Meister", 8, -6.6, height=1.8, kind="title", colour="magic"),
    banner("ars_master/chimaere", "Die Chimäre", 2.6, -3.5, height=0.9, colour="fire"),
    banner("ars_master/glyphen", "Glyphen der Stufe 3", 10.6, -5.0, height=0.9, colour="magic"),
    banner("ars_master/technica", "Ars Technica", 13.4, -1.3, height=0.9, colour="brass"),
    banner("ars_master/stahlwerk", "Neu im Stahlwerk", 3.4, 2.3, height=0.9, colour="nature"),
]

chapter(C, "Ars Nouveau: Meister", "ars_nouveau:archmage_spell_book", "magic", quests, shape="circle", order=25,
        stage=3, subtitle=["Stufe 3. Die Chimäre, das Erzmagier-Buch, Glyphen der Stufe 3 und Ars Technica."],
        images=images)
