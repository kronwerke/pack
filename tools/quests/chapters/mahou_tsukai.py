"""Mahou Tsukai in stage 4, one step per quest: hammer and compendium, the blood circle, the
dagger, the seven powdered catalysts, mortar and pestle, spell cloth, a checklist of first
scrolls (strengthening, Rho Aias, Gandr, projectile displacement, projection, familiar, damage
exchange) and Caliburn, mana storage (attuned gems, mana circuits, chronal exchange, kodoku),
Fay Sight, the Fae and the fae circuit, the Reality Marble scroll and its dimension, the
Mystic Codes and the Mystic Staff (2 000 mana on Kronwerke, 30 for the stage 4 goal).
Recipes from the jar, costs from config/mahoutsukai-server.toml."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, task_dimension,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "mahou_tsukai"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="fire"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def spell(name, x, y, title, sub, recipe, text, scroll, deps, reward):
    """One scroll of the first spells checklist."""
    return quest(name, x, y, title, subtitle=sub,
                 description=[recipe, "", text],
                 tasks=[task_item(scroll, 1)], rewards=[reward, reward_xp(5)],
                 deps=deps, icon=scroll, optional=True)


quests = [
    # ---- Der Blutkreis -------------------------------------------------------------
    quest("hammer", 0, 1, "&c&lBau Hammer und Ratgeber",
          subtitle="Magie aus Blut, Pulver und Tuch.",
          description=[
              "&6Hammer:&r oben Schnur und Bruchstein, in der Mitte Bruchstein und Stock, unten ein Stock. &6Knowledge Compendium:&r Leder, Papier, roter Farbstoff.",
              "",
              "Mahou Tsukai öffnet in &6Stufe 4&r. Keine Maschinen, keine Altäre: ein Kreis aus deinem Blut, drei Pulver hinein, fertig ist die Rolle. Der Ratgeber zeigt jeden Zauber mit den Kosten dieses Servers.",
              "",
              "&eKronwerke:&r Der Magie-Pfeiler von Stufe 4 will &e30 Mystische Stäbe&r aus diesem Kapitel, fest, und dazu 128 Gaia-Seelen von Botania.",
          ],
          tasks=[task_item("mahoutsukai:hammer", 1), task_item("mahoutsukai:guidebook", 1)],
          rewards=[reward_item("minecraft:red_dye", 8), reward_table("s4_common")],
          icon="mahoutsukai:guidebook", size=2.0, shape="hexagon"),

    quest("blood", 2.5, 0, "&cZeichne einen Blutkreis",
          subtitle="Ein Kreis auf dem Boden, und du bist Magier.",
          description=[
              "Leg in der Steuerung eine Taste für &eDraw Mahoujin&r fest. Nimm Schaden und drück &esofort danach&r die Taste, den Blick auf einen festen Block.",
              "",
              "Mit dem ersten Kreis bist du ein &cMahou Tsukai&r. Deine Manaleiste erscheint, am Anfang mit &d100 Mana&r.",
          ],
          tasks=[task_advancement("mahoutsukai:root", "Einen Blutkreis gezeichnet")],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_xp(5)],
          deps=["hammer"], icon="minecraft:redstone"),

    quest("dagger", 2.5, 2, "&cSchmiede einen Dolch",
          subtitle="Schaden auf Knopfdruck.",
          description=[
              "Oben &6Stock&r und &6Gold&r, in der Mitte &6lila Farbstoff, Eisen, Gold&r, unten &6Eisen&r und &6lila Farbstoff&r. Die genaue Lage zeigt JEI.",
              "",
              "Rechtsklick lässt dich bluten, schon hast du den Schaden für den Kreis. Der Dolch schneidet auch das Zaubertuch.",
          ],
          tasks=[task_item("mahoutsukai:dagger", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["hammer"], icon="mahoutsukai:dagger"),

    quest("catalysts", 5, 1, "&eZerschlag die sieben Pulver",
          subtitle="Jede Schule der Magie hat ihr Pulver.",
          description=[
              "Hammer und das Material an die Werkbank, der Hammer bleibt liegen. &7Eisen&r für Barrieren, &5Enderperle&r für Teleport, &bDiamant&r für Projektion, &aSmaragd&r für Tausch, &6Gold&r für Mystik, &fQuarz&r für Vertraute, &2Enderauge&r für Mystische Augen.",
          ],
          tasks=[task_item("mahoutsukai:powdered_iron", 1), task_item("mahoutsukai:powdered_gold", 1),
                 task_item("mahoutsukai:powdered_diamond", 1), task_item("mahoutsukai:powdered_emerald", 1),
                 task_item("mahoutsukai:powdered_ender", 1), task_item("mahoutsukai:powdered_eye", 1),
                 task_item("mahoutsukai:powdered_quartz", 1)],
          rewards=[reward_item("minecraft:diamond", 3), reward_table("s4_common")],
          deps=["blood", "dagger"], icon="mahoutsukai:powdered_gold"),

    quest("mortar", 7.5, 2, "&eBau Mörser und Stößel",
          subtitle="Doppelt so viel Pulver.",
          description=[
              "&6Mörser:&r zwei Ziegel über einem Diamanten. &6Stößel:&r drei Diamanten und zwei Stöcke. Beide zusammen formlos ergeben &6Mörser und Stößel&r.",
              "",
              "Statt mit dem Hammer gibt jedes Stück damit zwei Pulver. Für dreißig Stäbe zahlt sich das schnell aus.",
          ],
          tasks=[task_item("mahoutsukai:mortar_and_pestle", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["catalysts"], icon="mahoutsukai:mortar_and_pestle", optional=True),

    quest("cloth", 7.5, 0, "&eSchneid Zaubertuch",
          subtitle="Ohne Tuch keine Rolle.",
          description=[
              "&6Weiße Wolle&r und der &6Dolch&r geben 4 Zaubertücher. Der Dolch bleibt.",
              "",
              "&eSo zauberst du:&r Tuch auf den Boden, Blutkreis darauf, drei Pulver nacheinander hineinklicken. Ohne Tuch wird der Kreis ein &6Zauberkreis&r, der am Boden wirkt. Leere Hand auf einen frischen Kreis legt das letzte Rezept wieder hinein.",
          ],
          tasks=[task_item("mahoutsukai:spell_cloth", 8)],
          rewards=[reward_item("minecraft:white_wool", 8)],
          deps=["catalysts"], icon="mahoutsukai:spell_cloth"),

    # ---- Erste Rollen ---------------------------------------------------------------
    quest("strengthening", 0, 5.5, "&b&lZeichne eine Rolle der Verstärkung",
          subtitle="Die erste Schriftrolle.",
          description=[
              "&e2 Diamantpulver und 1 Eisenpulver&r auf einem Tuch.",
              "",
              "Sie verstärkt das erste Ding deiner Schnellleiste oder das in der zweiten Hand: eine Weile unzerstörbar, mehr Schaden, schnelleres Abbauen. Kostet &d50 Mana&r.",
              "",
              "&eMana wächst durch Benutzen&r wie ein Muskel. Es kommt langsam von selbst zurück, schneller mit vollem Magen. Schlafen gibt die Hälfte der Leiste auf einmal.",
          ],
          tasks=[task_item("mahoutsukai:scroll_strengthening", 1)],
          rewards=[reward_item("mahoutsukai:powdered_diamond", 4), reward_xp(5)],
          deps=["cloth"], icon="mahoutsukai:scroll_strengthening", size=1.5, shape="hexagon"),

    spell("schools", 2.5, 4.5, "&6Zeichne Rho Aias", "Ein Schild vor dir.",
          "&e2 Goldpulver, 1 Eisenpulver&r, Tuch.",
          "Ein großer Schild vor dir. Monster prallen ab, Geschosse verschwinden, schleichend kannst du selbst darauf springen. Kostet &d300 Mana&r.",
          "mahoutsukai:scroll_rho_aias", ["strengthening"], reward_item("mahoutsukai:spell_cloth", 8)),
    spell("gandr", 5, 4.5, "&6Zeichne Gandr", "Ein Fluch, der mit dir wächst.",
          "&eGold-, Smaragd- und Diamantpulver&r, Tuch.",
          "Kostet einen Anteil deiner Leiste, der Schaden wächst mit dem Mana. Deine negativen Effekte springen auf den Gegner über.",
          "mahoutsukai:scroll_gandr", ["schools"], reward_item("mahoutsukai:powdered_gold", 4)),
    spell("proj_displacement", 7.5, 4.5, "&5Zeichne Projektilverschiebung", "Zum letzten Pfeil.",
          "&e2 Enderpulver, 1 Diamantpulver&r, Tuch.",
          "Bringt dich zu dem letzten Pfeil, den du geschossen hast. Kostet &d50 Mana&r.",
          "mahoutsukai:scroll_projectile_displacement", ["gandr"], reward_item("minecraft:arrow", 32)),
    spell("projection", 2.5, 6.5, "&bZeichne Projektion", "Eine Kopie deines Werkzeugs.",
          "&e2 Diamantpulver, 1 Quarzpulver&r, Tuch.",
          "Der erste Einsatz merkt sich das Werkzeug, auf das du schaust. Jeder weitere gibt dir eine Kopie mit wenig Haltbarkeit. Kostet &d1 000 Mana&r pro Einsatz.",
          "mahoutsukai:scroll_projection", ["strengthening"], reward_item("mahoutsukai:powdered_quartz", 4)),
    spell("familiar", 5, 6.5, "&fBeschwör einen Vertrauten", "Er meldet und hält Chunks geladen.",
          "&e3 Quarzpulver&r, Tuch.",
          "Ein Begleiter meldet Spieler, Monster und Blöcke und hält die Gegend um sich geladen. Mit einem Block angeklickt meldet er nur diesen. Kostet &d200 Mana&r.",
          "mahoutsukai:scroll_summon_familiar", ["projection"], reward_item("minecraft:quartz", 16)),
    spell("damage_exchange", 7.5, 6.5, "&aZeichne Schadenstausch", "Treffer werden Mana.",
          "&e2 Smaragdpulver, 1 Eisenpulver&r, Tuch.",
          "Ein paar Treffer lang wird erlittener Schaden zu Mana. Kostet &d40 Mana&r.",
          "mahoutsukai:scroll_damage_exchange", ["familiar"], reward_item("mahoutsukai:powdered_emerald", 4)),

    quest("caliburn", 10, 5.5, "&6Zieh das Schwert aus dem See",
          subtitle="Konsolidierung der Macht.",
          description=[
              "Kreis ohne Tuch: &e2 Diamant, 1 Smaragd&r. Er erschafft einen See, jede Erweiterung kostet &d30 Mana&r. Wirf ein &everzaubertes Schwert&r hinein, für &d5 000 Mana&r kommt &6Caliburn&r zurück.",
              "",
              "Es hat den Schaden des alten Schwerts plus einen Bonus für die Verzauberungen, und Untote fliehen davor. Emrys, Nobu und Replica erklärt der Ratgeber.",
          ],
          tasks=[task_advancement("mahoutsukai:sword_in_the_lake", "Caliburn aus dem See bekommen")],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_table("s4_uncommon")],
          deps=["proj_displacement", "damage_exchange"], icon="mahoutsukai:caliburn", optional=True),

    # ---- Mana speichern -----------------------------------------------------------
    quest("gems", 0, 10.5, "&dStimm einen Diamanten ein",
          subtitle="10 000 Mana für unterwegs.",
          description=[
              "&6Einstimmer:&r Lapis in die Ecken, Gold an die Seiten, Mitte frei. Formlos mit einem &6Diamanten&r wird er zum &deingestimmten Diamanten&r.",
              "",
              "Halten und Rechtsklick füllt ihn mit deinem Mana. Zauber ziehen aus allen Edelsteinen im Inventar. Füll ihn vor dem Schlafen.",
          ],
          tasks=[task_item("mahoutsukai:attuned_diamond", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["blood"], icon="mahoutsukai:attuned_diamond"),

    quest("attuned_emerald", 2.5, 9.5, "&dStimm einen Smaragd ein",
          subtitle="5 000 Mana, billiger.",
          description=[
              "Einstimmer und ein &6Smaragd&r, formlos. Hält &d5 000 Mana&r.",
              "",
              "Zwei davon tragen einen Mystischen Stab mit Rest.",
          ],
          tasks=[task_item("mahoutsukai:attuned_emerald", 1)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(5)],
          deps=["gems"], icon="mahoutsukai:attuned_emerald", optional=True),

    quest("circuit", 2.5, 11.5, "&d&lBau einen Manaschaltkreis",
          subtitle="100 000 Mana neben der Werkbank.",
          description=[
              "&6Magitech-Manaschaltkreis:&r 6 Eisenbarren und 3 Smaragdpulver, Eisen links und rechts, Pulver in der mittleren Spalte.",
              "",
              "Er speichert &d100 000 Mana&r. Zauber in höchstens &e10 Blöcken&r ziehen daraus. Wer ihn zuerst anklickt, dem gehört er. Rechtsklick gibt Mana hinein, schleichend schaltest du ihn an und aus.",
          ],
          tasks=[task_item("mahoutsukai:mana_circuit_magitech", 1)],
          rewards=[reward_item("minecraft:emerald", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["gems"], icon="mahoutsukai:mana_circuit_magitech", size=1.5),

    quest("chronal", 5, 10.5, "&aLeg einen Chronalen Tausch",
          subtitle="Mana aus der Uhrzeit.",
          description=[
              "Kreis ohne Tuch: &e2 Smaragd, 1 Quarz&r. Zwölf Stunden rund um die Uhrzeit des Aufstellens gibt er &d10 Mana pro Sekunde&r, die anderen zwölf zieht er so viel ab.",
              "",
              "Der &aHaltbarkeitstausch&r (&e2 Smaragd, 1 Diamant&r) frisst die Haltbarkeit von Werkzeugen auf dem Kreis oder aus einer Kiste darunter. Alte Eisenwerkzeuge aus der Monsterfarm passen perfekt.",
          ],
          tasks=[task_checkmark("Ein Tauschkreis liegt neben meinem Schaltkreis")],
          rewards=[reward_item("mahoutsukai:powdered_emerald", 4), reward_xp(5)],
          deps=["circuit"], icon="mahoutsukai:powdered_emerald", optional=True),

    quest("sources", 7.5, 10.5, "&2Züchte einen Kodoku",
          subtitle="Ein Wurm voller Mana.",
          description=[
              "Erde, Karotte, Kartoffel, giftige Kartoffel, verrottetes Fleisch und Netherwarze ergeben einen &2Kodoku&r.",
              "",
              "Monster, die andere töten, sammeln Kodoku-Wert. Setz den hungrigen Wurm auf ein starkes Monster und töte es. Verbrennst du den Wurm danach, bekommen Schaltkreise in der Nähe Mana, nahe einer Leylinie mehr.",
          ],
          tasks=[task_item("mahoutsukai:kodoku", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["chronal"], icon="mahoutsukai:kodoku", optional=True),

    # ---- Leylinien und Fae --------------------------------------------------------
    quest("fay_sight", 0, 14.5, "&2Öffne die Feensicht",
          subtitle="Leylinien und die Fae.",
          description=[
              "&e3 Enderaugenpulver&r, Tuch. Kostet &d100 Mana&r und zeigt dir eine Weile &2Leylinien&r und &2Fae&r.",
              "",
              "Leylinien verbinden Punkte etwa 300 Blöcke auseinander. Nahe einer Linie kommt Mana deutlich schneller zurück. Mit Elytren an einer Linie entlang bekommst du Schub. Bau die Werkstatt auf einen Leypunkt.",
          ],
          tasks=[task_item("mahoutsukai:scroll_fay_sight", 1)],
          rewards=[reward_item("minecraft:ender_eye", 4)],
          deps=["strengthening"], icon="mahoutsukai:scroll_fay_sight"),

    quest("fae", 2.5, 14.5, "&2Sammle Feen-Essenz",
          subtitle="Was die Fae zurücklassen.",
          description=[
              "Die &2Fae&r schweben nahe Leylinien, ihr Lachen klingt wie Glöckchen. Sehen kannst du sie nur mit Feensicht. Besiegt lassen sie &2Feen-Essenz&r fallen. Mit einem Pulver lassen sie sich vermehren.",
              "",
              "Mit Essenz auf den Boden geklickt entsteht ein &2Feenkreis&r. Rollen daraus darf jeder benutzen, das Mana zahlt der Benutzer.",
              "",
              "&cAchtung:&r Iss keinen &cFeenmuffin&r, sonst meiden dich die Fae.",
          ],
          tasks=[task_item("mahoutsukai:fae_essence", 8)],
          rewards=[reward_item("mahoutsukai:powdered_eye", 4), reward_xp(5)],
          deps=["fay_sight"], icon="mahoutsukai:fae_essence"),

    quest("fae_circuit", 5, 14.5, "&2Bau einen Feen-Manaschaltkreis",
          subtitle="Derselbe Speicher, aus Essenz.",
          description=[
              "8 &6Feen-Essenzen&r um ein &6Smaragdpulver&r. Hält wie der Magitech-Schaltkreis &d100 000 Mana&r.",
              "",
              "Ein Schaltkreis, mit Feen-Essenz angeklickt, darf von allen benutzt werden. So füllen mehrere Magier einen gemeinsamen Speicher.",
          ],
          tasks=[task_item("mahoutsukai:mana_circuit", 1)],
          rewards=[reward_item("mahoutsukai:fae_essence", 4), reward_xp(10)],
          deps=["fae"], icon="mahoutsukai:mana_circuit", optional=True),

    quest("reality_marble", 7.5, 13.5, "&bZeichne die Perle der Realität",
          subtitle="Eine Welt aus Schwertern.",
          description=[
              "&e3 Diamantpulver&r, Tuch. Kostet &d4 000 Mana&r, das zahlst du aus Edelsteinen oder einem Schaltkreis.",
              "",
              "Schaust du beim Benutzen ein Wesen an, kommt es mit. Dann kommt nur einer zurück: einer muss sterben. Allein reicht es, Schaden zu nehmen, um zurückzukehren.",
          ],
          tasks=[task_item("mahoutsukai:scroll_reality_marble", 1)],
          rewards=[reward_item("minecraft:diamond_sword", 1), reward_xp(10)],
          deps=["circuit", "fay_sight"], icon="mahoutsukai:scroll_reality_marble"),

    quest("marble_visit", 10, 13.5, "&bBetritt die Perle der Realität",
          subtitle="Deine eigene Dimension.",
          description=[
              "Benutz die Rolle. Du landest an einem festen Ort in einer eigenen Dimension, in der überall Schwerter auftauchen. Sie halten nur wenige Schläge.",
              "",
              "&eTipp:&r Ein Zweikampf hier holt einen gefährlichen Gegner aus deiner Basis.",
          ],
          tasks=[task_dimension("mahoutsukai:reality_marble")],
          rewards=[reward_table("s4_uncommon"), reward_xp(15)],
          deps=["reality_marble"], icon="minecraft:iron_sword"),

    # ---- Der Mystische Stab ---------------------------------------------------------
    quest("mystic_code", 0, 18.5, "&6Näh ein Mystisches Zeichen",
          subtitle="Drei Stapel Rollen in einer Hand.",
          description=[
              "6 &6Zaubertücher&r und 3 &6Goldpulver&r. Es hält drei Stapel Rollen.",
              "",
              "Schleichend mit Rechtsklick öffnest du es, die Taste &eMystisches Zeichen wechseln&r springt zwischen den Rollen, Rechtsklick benutzt die gewählte.",
          ],
          tasks=[task_item("mahoutsukai:mystic_code", 1)],
          rewards=[reward_item("mahoutsukai:powdered_gold", 4), reward_xp(5)],
          deps=["strengthening"], icon="mahoutsukai:mystic_code"),

    quest("staff_scroll", 2.5, 17.5, "&6Zeichne Explosive Manakondensation",
          subtitle="Die Rolle für den Stab.",
          description=[
              "&e2 Goldpulver und 1 Diamantpulver&r auf einem Tuch.",
              "",
              pic("mahoutsukai:scroll_mystic_staff"),
              "",
              "Die Rolle ist an dich gebunden. Für jeden Stab gibt also ein Magier sein eigenes Mana.",
          ],
          tasks=[task_item("mahoutsukai:scroll_mystic_staff", 1)],
          rewards=[reward_item("mahoutsukai:powdered_gold", 8), reward_xp(5)],
          deps=["mystic_code"], icon="mahoutsukai:scroll_mystic_staff"),

    quest("staff", 5, 17.5, "&6&lRuf einen Mystischen Stab",
          subtitle="2 000 Mana für einen Stab.",
          description=[
              "Benutz die Rolle mit &d2 000 Mana&r in Leiste, Edelsteinen oder einem Schaltkreis in 10 Blöcken. &eRezept auf Kronwerke:&r Der Server hat die Kosten von 100 auf 2 000 angehoben.",
              "",
              "Schleichend mit Rechtsklick wechselst du die Feuerart: große Explosion (&d5 000 Mana&r, danach Gewitter), viele kleine (&d600&r pro Salve), Strahl (&d500 pro Tick&r, zerstört Blöcke).",
              "",
              "&cAchtung:&r Explosionen und Strahl zerstören die Landschaft. Nie in der Nähe von Basen. Für den Obelisken musst du ihn nicht abfeuern.",
          ],
          tasks=[task_item("mahoutsukai:mystic_staff", 1)],
          rewards=[reward_item("mahoutsukai:attuned_emerald", 1), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["staff_scroll"], icon="mahoutsukai:mystic_staff", size=1.5, shape="hexagon"),

    quest("first_sorcery", 2.5, 19.5, "&6Näh das Zeichen der Ersten Magie",
          subtitle="Rollen, die nicht verbraucht werden.",
          description=[
              "6 &6Zaubertücher&r, 2 &6Feen-Essenzen&r, 1 &6Diamantpulver&r.",
              "",
              "Wie das normale Zeichen, aber &edie Rollen darin werden nicht verbraucht&r. Dafür hat das Zeichen &e50 Haltbarkeit&r. Leg eine Rolle der Explosiven Manakondensation hinein, und jeder Rechtsklick ruft einen neuen Stab, solange das Mana reicht.",
          ],
          tasks=[task_item("mahoutsukai:mystic_code_first_sorcery", 1)],
          rewards=[reward_item("mahoutsukai:fae_essence", 4), reward_table("s4_uncommon")],
          deps=["mystic_code", "fae"], icon="mahoutsukai:mystic_code_first_sorcery"),

    quest("obelisk", 8, 18.5, "&c&lBring Stäbe zum Obelisken",
          subtitle="Dreißig Stäbe, 60 000 Mana.",
          description=[
              "Gib Stäbe einzeln am Obelisken ab oder stell eine Kiste als Zulieferer daneben. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eKronwerke:&r Das Magieziel von Stufe 4 heißt &e128 Gaia-Seelen&r und &e30 Mystische Stäbe&r, beide fest. Dreißig Stäbe sind &d60 000 Mana&r. Ein voller Schaltkreis reicht für das ganze Ziel.",
              "",
              "&eSo geht es schnell:&r Mehrere Magier füllen einen freigegebenen Schaltkreis, einer ruft mit dem Zeichen der Ersten Magie die Stäbe. Tauschkreise und Kodoku daneben, die Werkstatt auf einem Leypunkt.",
          ],
          tasks=[task_item("mahoutsukai:mystic_staff", 5),
                 task_checkmark("Mystische Stäbe am Obelisken abgegeben")],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["staff", "first_sorcery"], icon="mahoutsukai:mystic_staff", size=2.5, shape="gear"),

    # ---- Erste Rollen: weitere Rollen --------------------------------------------------
    spell("protective", 7.5, 5.5, "&5Zeichne Schutzteleport", "Pfeile treffen ins Leere.",
          "&e2 Enderpulver, 1 Eisenpulver&r, Tuch.",
          "Wenn dich ein Pfeil treffen würde, springst du stattdessen an eine zufällige Stelle in der Nähe, wie ein Enderman. Kostet &d50 Mana&r und gibt eine feste Zahl Sprünge, nicht eine feste Zeit.",
          "mahoutsukai:scroll_protective_displacement", ["proj_displacement"], reward_item("minecraft:ender_pearl", 8)),
    spell("ascension", 8.5, 4.5, "&5Zeichne Aufstieg", "Aus der Höhle an die Oberfläche.",
          "&e2 Enderpulver, 1 Goldpulver&r. Mit Tuch eine Rolle, ohne Tuch ein Kreis am Boden.",
          "Die Rolle bringt dich auf den höchsten festen Block über dir, für &d30 Mana&r. Als Kreis ohne Tuch schickt er alles nach oben, was darauf liegt oder steht, auch Items und Tiere. Ein Aufzug aus der Mine.",
          "mahoutsukai:scroll_ascension", ["proj_displacement"], reward_item("minecraft:ender_pearl", 8)),
    spell("weapon_shooter", 3.5, 6.5, "&bZeichne Waffenprojektile", "Ein Bogen, der Schwerter schießt.",
          "&e2 Diamantpulver, 1 Goldpulver&r, Tuch.",
          "Für &d100 Mana&r bekommst du den &6Bogen der Waffenprojektile&r. Er schießt Werkzeuge und Waffen aus deinem Inventar statt Pfeilen. Schleichend mit Rechtsklick schaltest du um, dann nimmt er nur projizierte Waffen und Rollen der Projektion.",
          "mahoutsukai:scroll_weapon_shooter", ["projection"], reward_item("mahoutsukai:powdered_diamond", 4)),
    spell("treasury", 4.5, 7.0, "&6Zeichne Schatzkammer-Projektion", "Ein Regen aus deinen Waffen.",
          "&e2 Diamantpulver, 1 Enderaugenpulver&r, Tuch.",
          "Die Rolle kostet &d1 000 Mana&r und gibt dir einen &6Handschuh der Schatzkammer-Projektion&r. Er schleudert Waffen und Werkzeuge aus deinem Inventar, manchen Taschen und deiner Endertruhe auf den Block, den du anschaust, &d120 Mana&r pro Waffe.",
          "mahoutsukai:scroll_treasury_projection", ["weapon_shooter"], reward_table("s4_common")),
    spell("borrowed_authority", 3.5, 4.5, "&6Zeichne Geborgte Kraft", "Stark wie ein Gott, für kurze Zeit.",
          "&e3 Goldpulver&r, Tuch.",
          "Für &d900 Mana&r wirst du kurze Zeit viel schneller und stärker. Getroffene Monster fliegen durch Wände. Sprung halten springt weiter, in der Luft gehalten bleibst du an der Fläche hängen, auf der du landest.",
          "mahoutsukai:scroll_borrowed_authority", ["schools"], reward_item("mahoutsukai:powdered_gold", 4)),

    # ---- Leylinien und Fae: Mystische Augen ------------------------------------------
    quest("binding_eyes", 2.5, 15.5, "&2Zeichne Mystische Augen der Bindung",
          subtitle="Ein Blick, und es bleibt stehen.",
          description=[
              "&e2 Enderaugenpulver, 1 Goldpulver&r auf einem Tuch. Kostet &d320 Mana&r.",
              "",
              "Danach hält Blickkontakt jedes Monster und jeden Spieler fest, den du anschaust. Spieler kommen frei, sobald sie wegsehen, Monster nicht.",
              "",
              "&eAuch aus Enderaugenpulver:&r Augen der Einsicht (&e2 Enderauge, 1 Ender&r) zeigen Inventar und Effekte eines Ziels, Augen der Schwarzen Flamme (&e2 Enderauge, 1 Diamant&r) setzen schwarzes Feuer, das Wither-Schaden macht und keine Blöcke frisst.",
          ],
          tasks=[task_item("mahoutsukai:scroll_mystic_eyes", 1)],
          rewards=[reward_item("mahoutsukai:powdered_eye", 4), reward_xp(5)],
          deps=["fay_sight"], icon="mahoutsukai:scroll_mystic_eyes", optional=True),

    # ---- Barrieren --------------------------------------------------------------------
    quest("alarm", 0, 22.5, "&7&lLeg eine Alarmbarriere",
          subtitle="Eisenpulver bewacht deine Basis.",
          description=[
              "Barrieren sind Kreise am Boden, die in einem Umkreis wirken und dabei laufend etwas Mana vom Zeichner ziehen. Alle brauchen &e2 Eisenpulver&r und ein drittes Pulver, ein Tuch ist nicht nötig. Mit Tuch wird daraus eine Rolle, mit der du die Barriere woanders hinlegst.",
              "",
              "&6Alarmbarriere:&r &e2 Eisen, 1 Quarz&r. Sie meldet dir jedes Monster und jeden Spieler, der in &e10 Blöcken&r Umkreis auftaucht, und gibt dann Komparatorsignal 15.",
              "",
              "Rechtsklick schaltet eine Barriere an und aus, ein Redstonesignal kehrt den Zustand um.",
          ],
          tasks=[task_checkmark("Eine Alarmbarriere liegt")],
          rewards=[reward_item("mahoutsukai:powdered_iron", 6), reward_xp(5)],
          deps=["catalysts"], icon="mahoutsukai:scroll_boundary_alarm"),

    quest("tangible", 2.5, 22.0, "&7Leg eine Magische Barriere",
          subtitle="Eine Wand, durch die nur du gehst.",
          description=[
              "&e2 Eisen, 1 Diamant&r. Ringsum entsteht im Umkreis von &e10 Blöcken&r eine unsichtbare Wand. Du gehst hindurch, Monster, Pfeile und andere Wesen nicht.",
              "",
              "Feste Blöcke außer Gras ersetzt sie nicht, Wasser auch nicht. Leg sie also auf ebenen Boden, dann schließt sie sauber.",
          ],
          tasks=[task_checkmark("Eine Magische Barriere steht")],
          rewards=[reward_item("mahoutsukai:powdered_diamond", 4), reward_xp(5)],
          deps=["alarm"], icon="mahoutsukai:scroll_boundary_tangible"),

    quest("displacement_boundary", 2.5, 23.0, "&5Leg eine Teleportbarriere",
          subtitle="Wer hinein will, landet draußen.",
          description=[
              "&e2 Eisen, 1 Ender&r. Wesen, die in den Umkreis von &e11 Blöcken&r wollen, landen auf der anderen Seite der Barriere. Blöcke, in denen sie ersticken würden, schiebt sie dabei weg.",
              "",
              "Ein freier Platz für den Markt oder die Werkstatt, ohne Mauern zu bauen.",
          ],
          tasks=[task_checkmark("Eine Teleportbarriere steht")],
          rewards=[reward_item("mahoutsukai:powdered_ender", 4), reward_xp(5)],
          deps=["tangible"], icon="mahoutsukai:scroll_boundary_displacement", optional=True),

    quest("drain_life", 5, 22.5, "&cLeg eine Barriere des Lebensraubs",
          subtitle="Monster zahlen mit ihrem Leben.",
          description=[
              "&e2 Eisen, 1 Smaragd&r. Im Umkreis von &e10 Blöcken&r verlieren Monster langsam Leben. Jeder Punkt geht an dich zurück: erst als Leben, dann als Hunger, dann als Mana, je nachdem, was dir fehlt.",
              "",
              "&eHinweis:&r Diese Rolle lässt sich nicht in das Zeichen der Ersten Magie legen.",
              "",
              "&eTipp:&r Neben einer Monsterfarm füllt sie deine Leiste, während du sortierst.",
          ],
          tasks=[task_checkmark("Eine Barriere des Lebensraubs steht")],
          rewards=[reward_item("mahoutsukai:powdered_emerald", 4), reward_table("s4_common"), reward_xp(5)],
          deps=["alarm"], icon="mahoutsukai:scroll_boundary_drain_life"),
]

images = [
    head("title", "Mahou Tsukai", 0, -3.4, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -2.0, height=0.55, kind="note", colour="stone"),
    head("spells", "Erste Rollen", 0, 3.3, colour="magic"),
    head("mana", "Mana speichern", 0, 8.3, colour="magic"),
    head("fae", "Leylinien und Fae", 0, 12.9, colour="nature"),
    head("staff", "Der Mystische Stab", 0, 16.1, colour="brass"),
    head("bounds", "Barrieren", 0, 20.6, colour="stone"),
]

chapter(C, "Mahou Tsukai", "mahoutsukai:mystic_staff", "magic", quests, shape="circle", order=40,
        stage=4, subtitle=["Stufe 4. Blutkreise, Pulver und Rollen, Mana, die Fae, die Perle der Realität und der Mystische Stab."],
        images=images)
