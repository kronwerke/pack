"""Ars Nouveau in stage 2: the Mage's Spell Book and every tier 2 glyph (Ars Nouveau, Ars
Elemental, the Ars Technica glyphs that open with brass), source relays, the ritual brazier with
every ritual that is open in stage 2 (Ars Nouveau, Ars Elemental, Ars Additions' locate
structure), the familiars that come from the Ritual of Binding, turrets, prisms, warp scrolls,
the Wixie and potion automation, the stage 2 charms and Ars Elemental blocks, and where Ars meets
Create: the Kronwerke blaze burner, Ars Technica's calibrated mechanism and source motor.
Awakening, flight, disintegration, warping, the island rituals, the adjustable and timer turrets
and tier 3 glyphs are stage 3 (ars_master.py)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_apprentice"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="magic"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Das zweite Buch ------------------------------------------------------------
    quest("welcome", 0, 2, "&d&lBau das Zauberbuch des Magiers",
          subtitle="Das zweite Buch: Glyphen der Stufe 2, mehr Mana.",
          description=[
              "Formlos: &6Zauberbuch für Anfänger&r, &e1 Obsidian&r, &e3 Diamanten&r, &e2 Quarzblöcke&r, &e2 Lohenruten&r. Glyphen und gespeicherte Zauber wandern mit.",
              "",
              "Das &6Zauberbuch des Magiers&r kann Glyphen der &eStufe 2&r benutzen und gibt &e+50&r Mana und &e+1&r pro Sekunde. Quarz und Lohenruten gibt es erst im Nether.",
              "",
              "Dieses Kapitel: neue Glyphen, Quelle über weite Strecken, Rituale, Vertraute, Türme und Create.",
          ],
          tasks=[task_item("ars_nouveau:apprentice_spell_book", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          icon="ars_nouveau:apprentice_spell_book", size=2.0, shape="hexagon"),

    quest("tier2", 2.5, 2, "&dLern, was Stufe 2 kostet",
          subtitle="55 Erfahrungspunkte pro Glyphe.",
          description=[
              "Gleicher Tisch, neues Buch in der Hand. Jede Glyphe der Stufe 2 kostet &e55 Erfahrungspunkte&r, etwa &e5 Level&r, dazu ihre Zutaten.",
              "",
              "Die großen Neuerungen sind die Verstärkungen: Fläche, Durchschlag, Dauer, Dämpfen, Glück, Extrakt. Damit werden deine alten Zauber zu Werkzeugen. Viele Rezepte wollen Nether-Zutaten, plant einen gemeinsamen Ausflug.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:experience_bottle", 8)],
          deps=["welcome"], icon="ars_nouveau:scribes_table"),

    quest("glyph_aoe", 5, 0, "&dLern AOE",
          subtitle="Aus einem Block werden neun.",
          description=[
              "Am Tisch: ein &6Feuerwerksstern&r.",
              "",
              "Vergrößert den Bereich um das Ziel. &eProjektil, Brechen, AOE&r baut 3x3 ab, zweimal AOE 5x5. Jedes AOE kostet mehr Mana, probier es nicht unter deinen Füßen aus.",
          ],
          tasks=[task_item("ars_nouveau:glyph_aoe", 1)],
          rewards=[reward_item("minecraft:gunpowder", 8), reward_xp(4)],
          deps=["tier2"], icon="ars_nouveau:glyph_aoe"),

    quest("glyph_pierce", 5, 2, "&dLern Durchschlag",
          subtitle="Durch die Wand und weiter.",
          description=[
              "Am Tisch: &6Pfeil&r und &6Wilden-Stachel&r.",
              "",
              "Hinter Projektil fliegt die Kugel ein Ziel weiter, hinter Brechen trifft sie auch den Block dahinter. &eProjektil, Brechen, AOE, Durchschlag, Durchschlag&r gräbt einen 3x3-Tunnel, drei Blöcke tief.",
          ],
          tasks=[task_item("ars_nouveau:glyph_pierce", 1)],
          rewards=[reward_item("minecraft:arrow", 16), reward_xp(4)],
          deps=["tier2"], icon="ars_nouveau:glyph_pierce"),

    quest("glyph_extend_time", 5, 4, "&dLern Zeit verlängern und verkürzen",
          subtitle="Länger leuchten, kürzer warten.",
          description=[
              "&dZeit verlängern&r: &6Uhr&r und &6Redstoneblock&r. &dDauer verringert&r: &6Uhr&r und &6Glowstonestaub&r.",
              "",
              "Verlängern streckt Tränke, Beschwörungen und Buffs. Verkürzen macht Verzögerung und Redstone-Signal kürzer und teure Buffs billiger.",
          ],
          tasks=[task_item("ars_nouveau:glyph_extend_time", 1), task_item("ars_nouveau:glyph_duration_down", 1)],
          rewards=[reward_item("minecraft:redstone_block", 1), reward_xp(4)],
          deps=["tier2"], icon="ars_nouveau:glyph_extend_time"),

    quest("glyph_fortune", 7.5, 0, "&dLern Glück und Extrakt",
          subtitle="Mehr Erz, oder das Erz selbst.",
          description=[
              "&dGlück&r: eine &6Hasenpfote&r. &dExtrakt&r: ein &6Smaragd&r.",
              "",
              "Glück wirkt wie Glück auf der Spitzhacke, auch auf Beute von Monstern, bis 4 Mal hinter Brechen. Extrakt wirkt wie Behutsamkeit. &cBeide zusammen gehen nicht&r, mach dir zwei Zauber.",
          ],
          tasks=[task_item("ars_nouveau:glyph_fortune", 1), task_item("ars_nouveau:glyph_extract", 1)],
          rewards=[reward_item("minecraft:emerald", 2), reward_xp(5)],
          deps=["glyph_aoe"], icon="ars_nouveau:glyph_fortune"),

    quest("glyph_dampen", 7.5, 2, "&dLern Dämpfen",
          subtitle="Manchmal ist weniger mehr.",
          description=[
              "Am Tisch: ein &6Netherziegel&r.",
              "",
              "Schwächt das Glied links davon. Gedämpftes Magielicht ist schwächer, gedämpftes Schmelzen brät Essen statt Erz, mit Platzen wird die Kugel hohl.",
          ],
          tasks=[task_item("ars_nouveau:glyph_dampen", 1)],
          rewards=[reward_item("minecraft:nether_brick", 8), reward_xp(3)],
          deps=["glyph_pierce"], icon="ars_nouveau:glyph_dampen", optional=True),

    quest("glyph_heal", 7.5, 4, "&dLern Heilen",
          subtitle="Endlich ein Heilzauber.",
          description=[
              "Am Tisch: &5Abschwörungsessenz&r, &e4 Glitzernde Melonenscheiben&r, &6Goldener Apfel&r.",
              "",
              "Heilt ein Stück und kostet dich Hunger. Untote nehmen den gleichen Betrag als Schaden. &eSelbst, Heilen, Verstärken&r für dich, &eProjektil, Heilen&r für Freunde.",
          ],
          tasks=[task_item("ars_nouveau:glyph_heal", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(5)],
          deps=["glyph_extend_time"], icon="ars_nouveau:glyph_heal"),

    quest("glyph_smelt", 10, 0, "&dLern Schmelzen",
          subtitle="Der Ofen im Zauberbuch.",
          description=[
              "Am Tisch: &cFeueressenz&r, &e4 Hochöfen&r, &6Lohenrute&r.",
              "",
              "Schmilzt Blöcke und Items in der Welt. &eProjektil, Brechen, Schmelzen, Artikelabholung&r liefert gleich Barren. Mit AOE mehr auf einmal, mit Verstärken härtere Blöcke.",
          ],
          tasks=[task_item("ars_nouveau:glyph_smelt", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 2), reward_xp(5)],
          deps=["glyph_fortune"], icon="ars_nouveau:glyph_smelt"),

    quest("glyph_grow", 10, 2, "&dLern Wachsen",
          subtitle="Knochenmehl aus dem Buch.",
          description=[
              "Am Tisch: &6Erdessenz&r, &e5 Knochenblöcke&r, &e3 Samen&r.",
              "",
              "&eBerühren, Wachsen, AOE, AOE&r und dann &eBerühren, Ernte, AOE, AOE&r: ein 5x5-Feld von Samen bis Ernte. Wie Knochenmehl bringt es dem Agronomischen Link nichts.",
          ],
          tasks=[task_item("ars_nouveau:glyph_grow", 1)],
          rewards=[reward_item("minecraft:bone_block", 4), reward_xp(5)],
          deps=["glyph_dampen", "glyph_heal"], icon="ars_nouveau:glyph_grow"),

    quest("glyph_crush", 10, 4, "&dLern Zerkleinern",
          subtitle="Stein zu Kies, Kies zu Sand.",
          description=[
              "Am Tisch: &6Erdessenz&r, &6Schleifstein&r, &6Kolben&r.",
              "",
              "Macht Stein zu Kies, Kies zu Sand, Blumen zu doppeltem Farbstoff, mit Empfindlich auch Items. Gegen schwimmende Wesen besonders stark.",
          ],
          tasks=[task_item("ars_nouveau:glyph_crush", 1)],
          rewards=[reward_item("minecraft:sand", 16), reward_xp(3)],
          deps=["glyph_heal"], icon="ars_nouveau:glyph_crush", optional=True),

    quest("glyph_slowfall", 12.5, 0, "&dLern Langsamer Fall",
          subtitle="Wie eine Feder zu Boden.",
          description=[
              "Am Tisch: &fLuftessenz&r, &6Wilden-Flügel&r, &e3 Federn&r, &6Lohenrute&r, &6Netherwarze&r.",
              "",
              "&eSelbst, Langsamer Fall, Zeit verlängern&r macht jeden Sprung harmlos. Mit Sprung aus Stufe 1 reist du so: springen, gleiten, springen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_slowfall", 1)],
          rewards=[reward_item("minecraft:feather", 8), reward_xp(3)],
          deps=["glyph_smelt"], icon="ars_nouveau:glyph_slowfall", optional=True),

    quest("glyph_conjure_water", 12.5, 2, "&dLern Wasser beschwören",
          subtitle="Eine Quelle in der Hosentasche.",
          description=[
              "Am Tisch: &bWasseressenz&r und &6Wassereimer&r.",
              "",
              "Setzt Wasser am Ziel oder löscht brennende Wesen, dich eingeschlossen. Im Nether die Rettung nach dem Sturz in die Lava.",
          ],
          tasks=[task_item("ars_nouveau:glyph_conjure_water", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(3)],
          deps=["glyph_grow"], icon="ars_nouveau:glyph_conjure_water", optional=True),

    quest("glyph_flare", 12.5, 4, "&dLern Fackel",
          subtitle="Feuer auf brennende Ziele.",
          description=[
              "Am Tisch: &cFeueressenz&r, &e2 Feuerzeuge&r, &e2 Feuerkugeln&r, &6Lohenrute&r.",
              "",
              "Trifft es etwas Brennendes, explodieren Funken und treffen alles in der Nähe. &eProjektil, Entzünden, Fackel&r ist der klassische Kampfzauber.",
          ],
          tasks=[task_item("ars_nouveau:glyph_flare", 1)],
          rewards=[reward_item("minecraft:fire_charge", 4), reward_xp(3)],
          deps=["glyph_crush"], icon="ars_nouveau:glyph_flare", optional=True),

    quest("arc_projectile", 15, 0, "&dLern Arc Projectile",
          subtitle="Ars Elemental: eine Form, die im Bogen fliegt.",
          description=[
              "Am Tisch: &6Pfeil&r, &6Schneeball&r, &6Schleimball&r, &6Enderperle&r.",
              "",
              "Fliegt im Bogen wie ein geworfener Trank. Jeder Durchschlag lässt es einmal vom Boden abprallen. Gut für Ziele hinter Mauern.",
          ],
          tasks=[task_item("ars_elemental:glyph_arc_projectile", 1)],
          rewards=[reward_item("minecraft:slime_ball", 4), reward_xp(3)],
          deps=["glyph_slowfall"], icon="ars_elemental:glyph_arc_projectile", optional=True),

    quest("spells2", 15, 2.5, "&d&lRüste dein Zauberbuch auf",
          subtitle="Tunnel, Felder und Barren.",
          description=[
              "&eTunnel:&r Projektil, Brechen, Verstärken, AOE, Durchschlag, Durchschlag, Artikelabholung. &eErz:&r Projektil, Brechen, Glück, Schmelzen, Artikelabholung.",
              "&eGarten:&r Berühren, Wachsen, AOE, AOE. &eErnte:&r Berühren, Ernte, AOE, AOE, Artikelabholung. &eSanitäter:&r Projektil, Heilen, Verstärken.",
              "",
              "Ein Zauber hat höchstens zehn Glyphen. Wird es eng, teil ihn auf oder nimm einen Zauberstab.",
          ],
          tasks=[task_checkmark("Zauberbuch aufgerüstet")],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["glyph_smelt", "glyph_grow"], icon="ars_nouveau:apprentice_spell_book", size=1.5, shape="diamond"),

    quest("t2_motion", 5, 6.5, "&dLern die Bewegungs-Glyphen",
          subtitle="Checkliste Stufe 2: schneller, langsamer, schwerer.",
          description=[
              "&dBeschleunigen&r (Antriebsschiene, Zucker, Uhr): Projektile fliegen schneller.",
              "&dVerlangsamen&r (Seelensand, Spinnweben, Uhr): Projektile fliegen langsamer.",
              "&dSchwere&r (Luftessenz, 2 Ambosse, 3 Federn): Blöcke und Wesen fallen, mit Zeit verlängern doppelter Fallschaden.",
              "&dAustausch&r (Manipulationsessenz, Smaragdblock, 2 Enderperlen): tauscht Blöcke gegen die aus deiner Hotbar.",
          ],
          tasks=[task_item("ars_nouveau:glyph_accelerate", 1), task_item("ars_nouveau:glyph_decelerate", 1),
                 task_item("ars_nouveau:glyph_gravity", 1), task_item("ars_nouveau:glyph_exchange", 1)],
          rewards=[reward_item("minecraft:emerald", 2), reward_xp(4)],
          deps=["glyph_extend_time"], icon="ars_nouveau:glyph_accelerate"),

    quest("t2_fight", 7.5, 6.5, "&dLern die Kampf-Glyphen",
          subtitle="Checkliste Stufe 2: Knall und Kälte.",
          description=[
              "&dExplosion&r (Feueressenz, 3 TNT, Feuerkugel): AOE macht sie größer, Verstärken stärker.",
              "&dFeuerwerk&r (Feueressenz, 2 Raketen, Feuerwerksstern): eine Rakete am Ziel.",
              "&dWindscherung&r (Luftessenz, 3 Eisenschwerter): Schaden an Zielen in der Luft, mehr je höher, bis 10 Blöcke.",
              "&dKälteeinbruch&r (Wasseressenz, Pulverschneeeimer, Eis): Schadensstoß gegen langsame, nasse oder gefrorene Ziele.",
          ],
          tasks=[task_item("ars_nouveau:glyph_explosion", 1), task_item("ars_nouveau:glyph_firework", 1),
                 task_item("ars_nouveau:glyph_wind_shear", 1), task_item("ars_nouveau:glyph_cold_snap", 1)],
          rewards=[reward_item("minecraft:tnt", 4), reward_xp(4)],
          deps=["glyph_flare"], icon="ars_nouveau:glyph_explosion"),

    quest("t2_util", 10, 6.5, "&dLern die Hilfs-Glyphen",
          subtitle="Checkliste Stufe 2: alles für unterwegs.",
          description=[
              "&dEnder-Inventar&r (Manipulationsessenz, Endertruhe): öffnet deine Endertruhe überall.",
              "&dName&r (Manipulationsessenz, Namensschild): benennt das Ziel nach dem Zauber.",
              "&dSinnesmagie&r (Abschwörungsessenz, Wünschelrute, Sternbunkel-Scherben): magische Wesen in 75 Blöcken leuchten.",
              "&dUnsichtbarkeit&r (Abschwörungsessenz, Fermentiertes Spinnenauge, Lohenrute). &dEinflößen&r (Abschwörungsessenz, Glasflasche, Lohenrute): gibt dem Ziel den Trank aus deiner Flasche.",
              "&dBlock animieren&r (Beschwörungsessenz, 3 Obsidian): ein Block kämpft für dich.",
          ],
          tasks=[task_item("ars_nouveau:glyph_ender_inventory", 1), task_item("ars_nouveau:glyph_name", 1),
                 task_item("ars_nouveau:glyph_sense_magic", 1), task_item("ars_nouveau:glyph_invisibility", 1),
                 task_item("ars_nouveau:glyph_infuse", 1), task_item("ars_nouveau:glyph_animate_block", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(5)],
          deps=["tier2"], icon="ars_nouveau:glyph_ender_inventory"),

    quest("el_water", 12.5, 6.5, "&dLern Wasser und Luft von Ars Elemental",
          subtitle="Checkliste Stufe 2: Ars Elemental, Teil 1.",
          description=[
              "&dNasses Grab&r (Seetang, Prismarinsplitter, Wasseressenz): das Ziel ertrinkt an Land.",
              "&dGeysir&r (Feuer- und Wasseressenz, Magmablock, Windkugel): schleudert Wesen nach oben.",
              "&dNebelwolke&r (Wasser- und Luftessenz, Phantomhaut, Blaues Eis): Monster verlieren ihr Ziel.",
              "&dManablase&r (Herz des Meeres, Prismarinsplitter, Bastionsfrucht, Wasseressenz): Schild, der Schaden mit Mana abfängt.",
              "&dRutschen&r (Wasser- und Abschwörungsessenz, Schleimball, Eis). &dEntladung&r (Blitzableiter, Flashpine, Luftessenz): Schaden an geschockten Zielen.",
          ],
          tasks=[task_item("ars_elemental:glyph_watery_grave", 1), task_item("ars_elemental:glyph_geyser", 1),
                 task_item("ars_elemental:glyph_mist", 1), task_item("ars_elemental:glyph_bubble_shield", 1),
                 task_item("ars_elemental:glyph_slip_feet", 1), task_item("ars_elemental:glyph_discharge", 1)],
          rewards=[reward_item("minecraft:prismarine_shard", 8), reward_xp(5)],
          deps=["arc_projectile"], icon="ars_elemental:glyph_bubble_shield", optional=True),

    quest("el_earth", 15, 6.5, "&dLern Erde und Beschwörung von Ars Elemental",
          subtitle="Checkliste Stufe 2: Ars Elemental, Teil 2.",
          description=[
              "&dGiftsporen&r (Sporenblüte, Roter Pilz, Erdessenz): Sporen springen auf vergiftete Ziele über.",
              "&dVergiften&r (Giftige Kartoffel, Fermentiertes Spinnenauge, Seltsame Suppe): Gift, das sich zu Gift steigert.",
              "&dStachel&r (Spitzer Tropfstein, Netheritbarren, Erdessenz): ein Tropfsteinstachel aus dem Boden.",
              "&dBienen beschwören&r (Erd- und Beschwörungsessenz, Magebloom, Honigwabe), &dSchleime beschwören&r (Wasser- und Beschwörungsessenz, 2 Schleimbälle): je drei Kämpfer.",
          ],
          tasks=[task_item("ars_elemental:glyph_poison_spores", 1), task_item("ars_elemental:glyph_envenom", 1),
                 task_item("ars_elemental:glyph_spike", 1), task_item("ars_elemental:glyph_summon_bee", 1),
                 task_item("ars_elemental:glyph_summon_slime", 1)],
          rewards=[reward_item("minecraft:honeycomb", 4), reward_xp(5)],
          deps=["el_water"], icon="ars_elemental:glyph_poison_spores", optional=True),

    quest("el_anima", 17.5, 6.5, "&dMach Anima-Essenz",
          subtitle="Ars Elemental: die achte Essenz und ihre Glyphen.",
          description=[
              "In der Kammer: Quelljuwel hinein, &6Witherskelettschädel&r, &6Knochenmehl&r, &6Goldener Apfel&r auf die Podeste, &d3 000 Quelle&r.",
              "",
              "Glyphen damit: &dZähmen&r (Anima, Goldene Karotte, Quellbeerkuchen, Kuchen) macht Gegner zu Verbündeten auf Zeit. &dPhantomgriff&r (Anima, 2 Phantomhäute) heilt Untote und zehrt Lebende aus. &dArc weitergeben&r (Manipulationsessenz, Arc Projectile) schießt den Rest des Zaubers neu ab.",
          ],
          tasks=[task_item("sauce:anima_essence", 1), task_item("ars_elemental:glyph_charm", 1),
                 task_item("ars_elemental:glyph_phantom_grasp", 1), task_item("ars_elemental:glyph_propagator_arc", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(5)],
          deps=["el_earth"], icon="sauce:anima_essence", optional=True),

    # ---- Quelle bewegen -------------------------------------------------------------
    quest("relay", 0, 10.5, "&a&lBau ein Quellrelais",
          subtitle="Quelle über 30 Blöcke, ohne Gläser zu schleppen.",
          description=[
              "&e6 Goldbarren&r an den Seiten, ein &6Quelljuwelblock&r in der Mitte, oben und unten Mitte frei.",
              "",
              "Dominion-Zauberstab: erst das Glas, dann das Relais, dann das Relais, dann das Ziel (Glas oder nächstes Relais). Reichweite &e30 Blöcke&r. Schleichend klicken löscht, Redstone schaltet ab.",
              "",
              "&eTipp:&r Links an die Baumfarm, Gläser an den Arbeitsplatz, zwei Relais dazwischen.",
          ],
          tasks=[task_item("ars_nouveau:relay", 2)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          deps=["welcome"], icon="ars_nouveau:relay", size=1.5, shape="square"),

    quest("splitter", 2.5, 9.5, "&aBau einen Splitter",
          subtitle="Eine Quelle, viele Ziele.",
          description=[
              "Im Apparat: Relais mit &e4 Quarz&r und &e4 Lapislazuli&r.",
              "",
              "Zieht aus mehreren Gläsern und liefert an mehrere Ziele, mit deutlich mehr Durchsatz als ein Relais. Ars Elemental macht daraus mit 2 Wasseressenzen und 2 Diamanten das Wasser-Relais mit mehr Speicher und Durchsatz.",
          ],
          tasks=[task_item("ars_nouveau:relay_splitter", 1)],
          rewards=[reward_item("minecraft:quartz", 8), reward_xp(4)],
          deps=["relay"], icon="ars_nouveau:relay_splitter"),

    quest("collector", 2.5, 11.5, "&aBau Kollektor und Einzahler",
          subtitle="Nie wieder jedes Glas einzeln verbinden.",
          description=[
              "Im Apparat: Relais mit &e4 Truhen&r wird der &6Kollektor&r, mit &e4 Trichtern&r der &6Einzahler&r.",
              "",
              "Der Kollektor saugt aus allen Gläsern in &e5 Blöcken&r, der Einzahler füllt alle Gläser in &e5 Blöcken&r. Kollektor an der Link-Farm, Einzahler in der Werkstatt, fertig.",
              "",
              "Das &6Warper-Relais&r für endlose Strecken braucht Chorusfrüchte und kommt mit Stufe 4.",
          ],
          tasks=[task_item("ars_nouveau:relay_collector", 1), task_item("ars_nouveau:relay_deposit", 1)],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(5)],
          deps=["relay"], icon="ars_nouveau:relay_collector"),

    # ---- Rituale ---------------------------------------------------------------------
    quest("brazier", 0, 17, "&a&lBau das Ritual-Kohlenbecken",
          subtitle="Wo die großen Zauber brennen.",
          description=[
              "Formlos: &6Arkanes Podest&r, &6Quelljuwelblock&r, &e3 Goldbarren&r.",
              "",
              "Jedes Ritual ist eine &6Ritualtafel&r aus einem farbigen Archwood-Stamm und Zutaten. Tafel auf das Becken, Zusätze daraufwerfen, mit leerer Hand starten. Quelle kommt aus Gläsern in der Nähe, Redstone hält es an.",
          ],
          tasks=[task_item("ars_nouveau:ritual_brazier", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          deps=["welcome"], icon="ars_nouveau:ritual_brazier", size=1.75, shape="square"),

    quest("ritual_harvest", 2.5, 15, "&aMach die Tafel Ernte",
          subtitle="Die Felder ernten sich selbst.",
          description=[
              "&aBlühender Stamm&r, &6Erdessenz&r, &6Eisenhacke&r.",
              "",
              "Wirkt Ernte immer wieder auf reife Pflanzen in der Nähe, gegen ein wenig Quelle pro Runde. Eine Truhe direkt am Becken nimmt die Ernte auf.",
          ],
          tasks=[task_item("ars_nouveau:ritual_harvest", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(4)],
          deps=["brazier"], icon="ars_nouveau:ritual_harvest"),

    quest("ritual_scrying", 2.5, 17, "&aMach die Tafel Wahrsagerei",
          subtitle="Einen Block durch alle anderen sehen.",
          description=[
              "&5Ärgerlicher Stamm&r, &e3 Spinnenaugen&r, &6Glowstone&r, &6Quelljuwelblock&r.",
              "",
              "Vor dem Start einen Block auf das Becken werfen, etwa Zinkerz. Danach siehst du jeden Block dieser Sorte durch die Erde: weiß nah, grün mittel, blau weit. Mit einer Manipulationsessenz dazu &e15 Minuten&r lang.",
          ],
          tasks=[task_item("ars_nouveau:ritual_scrying", 1)],
          rewards=[reward_item("minecraft:spider_eye", 4), reward_xp(4)],
          deps=["brazier"], icon="ars_nouveau:ritual_scrying"),

    quest("ritual_fertility", 2.5, 19, "&aMach die Tafel Fruchtbarkeit",
          subtitle="Die Tiere vermehren sich von selbst.",
          description=[
              "&aBlühender Stamm&r, &e3 Weizen&r, &6Goldener Apfel&r, &e2 Lohenstaub&r.",
              "",
              "Lässt Tiere in der Nähe regelmäßig Junge bekommen, solange Quelle da ist. Ab &e20 Tieren&r in der Nähe pausiert es. Mit einem Vitalic-Link daneben kommt Quelle zurück.",
          ],
          tasks=[task_item("ars_nouveau:ritual_fertility", 1)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["ritual_scrying"], icon="ars_nouveau:ritual_fertility", optional=True),

    quest("ritual_sanctuary", 5, 15, "&aMach die Tafel Zufluchtsort",
          subtitle="Keine Monster mehr zu Hause.",
          description=[
              "&bKaskadierender Stamm&r, &bWasseressenz&r, &6Seelaterne&r.",
              "",
              "Im Umkreis von &e32 Blöcken&r spawnen keine feindlichen Monster natürlich. Jedes Verrottete Fleisch als Zusatz gibt &e+1&r Block, bis &e128&r. Quelle kostet es nur, wenn es einen Spawn verhindert, höchstens einmal pro Minute.",
          ],
          tasks=[task_item("ars_nouveau:ritual_sanctuary", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 16), reward_xp(5)],
          deps=["ritual_harvest"], icon="ars_nouveau:ritual_sanctuary"),

    quest("ritual_restoration", 5, 17, "&aMach die Tafel Wiederherstellung",
          subtitle="Heilung für alle in der Nähe.",
          description=[
              "&aBlühender Stamm&r, &6Goldener Apfel&r, &5Abschwörungsessenz&r.",
              "",
              "Heilt Wesen in der Nähe nach und nach und schadet Untoten. &6Zombiedorfbewohner&r werden sofort geheilt und geben dir Rabatt, wenn du dabei warst.",
          ],
          tasks=[task_item("ars_nouveau:ritual_restoration", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["ritual_scrying"], icon="ars_nouveau:ritual_restoration", optional=True),

    quest("ritual_forestation", 5, 19, "&aMach die Tafel Aufforstung",
          subtitle="Ein Wald in Minuten.",
          description=[
              "&aBlühender Stamm&r, &6Mendosteen&r, &6Erdessenz&r.",
              "",
              "Setzt ausgewachsene Eichen und Birken in einem runden 7x7-Bereich und düngt. Jedes Quelljuwel als Zusatz gibt +1 Radius, ein Braunpilz macht Taiga, Leuchtbeeren Dschungel. Mendosteen wächst an Archwood-Bäumen.",
          ],
          tasks=[task_item("ars_nouveau:ritual_forestation", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 8)],
          deps=["ritual_restoration"], icon="ars_nouveau:ritual_forestation", optional=True),

    quest("ritual_binding", 7.5, 15, "&aMach die Tafel Bindung",
          subtitle="Ein Helfer wird zum Vertrauten.",
          description=[
              "&5Ärgerlicher Stamm&r, &6Leeres Pergament&r, &6Enderperle&r, &e3 Quelljuwelen&r.",
              "",
              "Neben einem Sternbunkel, Drygmy, Wirbelzweig oder Wixie starten. Das Wesen wird zum &6Gebundenen Skript&r, Rechtsklick damit macht es zu deinem Vertrauten. Rufen kannst du ihn im Zauberbuch, immer nur einen.",
          ],
          tasks=[task_item("ars_nouveau:ritual_binding", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(5)],
          deps=["ritual_sanctuary"], icon="ars_nouveau:ritual_binding"),

    quest("familiar", 10, 15, "&dBinde einen Sternbunkel",
          subtitle="Tempo II von einem kleinen Freund.",
          description=[
              "Bindung neben einem Sternbunkel, dann das Skript benutzen.",
              "",
              "Als Vertrauter gibt er dir &eTempo II&r. Ein Goldnugget an ihn verfüttert zeigt dir kurz Golderz durch die Wände.",
          ],
          tasks=[task_item("ars_nouveau:familiar_starbuncle", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["ritual_binding"], icon="ars_nouveau:familiar_starbuncle"),

    quest("familiar_more", 12.5, 15, "&dBinde die anderen Vertrauten",
          subtitle="Checkliste: Wirbelzweig, Drygmy, Wixie.",
          description=[
              "&dWirbelzweig&r: Erd-Glyphen kosten die Hälfte, Essen sättigt mehr.",
              "&dDrygmy&r: &e+2&r Schaden für Erd-Zauber, Chance auf mehr Beute.",
              "&dWixie&r: deine Tränke wirken länger, im Kampf wirft er schädliche Tränke auf Gegner.",
              "",
              "Amethyst-Golem und Bücherwurm kommen mit dem Ritual Erwachen in Stufe 3.",
          ],
          tasks=[task_item("ars_nouveau:familiar_whirlisprig", 1), task_item("ars_nouveau:familiar_drygmy", 1),
                 task_item("ars_nouveau:familiar_wixie", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 1), reward_xp(5)],
          deps=["familiar", "wixie"], icon="ars_nouveau:familiar_whirlisprig", optional=True),

    quest("el_familiars", 15, 15, "&dBinde die Elementar-Vertrauten",
          subtitle="Ars Elemental: Sirene, Flashjack, Flarecannon.",
          description=[
              "&dSirene&r: &e+2&r Wasserschaden, Gunst des Delfins II im Wasser.",
              "&dFlashjack&r: &e+2&r Blitzschaden, Bewegungszauber 20 Prozent billiger. Flashpine verfüttert gibt Tempo und Nachtsicht.",
              "&dFlarecannon&r: &e+2&r Feuerschaden, Projektilzauber 20 Prozent billiger. Charme im Apparat: Magmablock, 2 Feueressenzen, Netheritplatten, 2 Netherziegel.",
          ],
          tasks=[task_item("ars_elemental:siren_familiar", 1), task_item("ars_elemental:flashjack_familiar", 1),
                 task_item("ars_elemental:firenando_familiar", 1)],
          rewards=[reward_item("minecraft:magma_cream", 4), reward_xp(5)],
          deps=["familiar"], icon="ars_elemental:firenando_charm", optional=True),

    quest("ritual_containment", 7.5, 17, "&aMach die Tafel Eindämmung",
          subtitle="Ein Wesen im Glas.",
          description=[
              "&5Ärgerlicher Stamm&r, &6Manipulationsessenz&r, &e3 Glasflaschen&r. Das &6Eindämmungsglas&r: oben 3 Archwood-Stufen, dann Glas im Rahmen.",
              "",
              "Fängt ein Wesen in &e3 Blöcken&r Umkreis und steckt es in ein Glas daneben. Wesen im Glas zählen für den Drygmy als Nachbarn.",
          ],
          tasks=[task_item("ars_nouveau:ritual_containment", 1), task_item("ars_nouveau:mob_jar", 1)],
          rewards=[reward_item("minecraft:glass", 8)],
          deps=["ritual_binding"], icon="ars_nouveau:mob_jar", optional=True),

    quest("ritual_cloudshaping", 10, 17, "&aMach die Tafel Wolkenformung",
          subtitle="Wetter nach Wunsch.",
          description=[
              "&bKaskadierender Stamm&r, &6Feder&r, &6Quelljuwelblock&r.",
              "",
              "Ohne Zusatz klares Wetter, mit Schwarzpulver Regen, mit einem Lapisblock Gewitter. Sprecht euch ab, das Wetter gilt für alle.",
          ],
          tasks=[task_item("ars_nouveau:ritual_cloudshaping", 1)],
          rewards=[reward_item("minecraft:feather", 8)],
          deps=["ritual_containment"], icon="ars_nouveau:ritual_cloudshaping", optional=True),

    quest("ritual_time", 12.5, 17, "&aMach Sonnenaufgang und Mondfall",
          subtitle="Tag oder Nacht auf Knopfdruck.",
          description=[
              "&aSonnenaufgang&r: Flammender Stamm, 3 Löwenzahn, Uhr (oder Flammender Stamm und Sonnenblume). &aMondfall&r: Kaskadierender Stamm, Tintenbeutel, Kohleblock, Uhr (oder Kaskadierender Stamm und Wilden-Flügel).",
              "",
              "Stellt die Zeit auf Tag oder Nacht. Mondfall ist der schnellste Weg zu Wilden und Hexen.",
          ],
          tasks=[task_item("ars_nouveau:ritual_sunrise", 1), task_item("ars_nouveau:ritual_moonfall", 1)],
          rewards=[reward_item("minecraft:clock", 1), reward_xp(3)],
          deps=["ritual_cloudshaping"], icon="ars_nouveau:ritual_sunrise", optional=True),

    quest("ritual_locate", 15, 17, "&aMach die Tafel Struktur finden",
          subtitle="Ars Additions: der Weg zum nächsten Bauwerk.",
          description=[
              "&6Wayfinder&r: Amethystsplitter in der Mitte, 4 Goldbarren im Kreuz. Tafel: &5Ärgerlicher Stamm&r, &6Kompass&r, &6Quelljuwel&r, Wayfinder.",
              "",
              "Der Zusatz wählt das Ziel: Netherziegel Festung, Polierte Schwarzsteinziegel Bastion, Smaragd Außenposten, Bemooster Bruchstein Dschungeltempel, Sandstein Wüstentempel, Tiefenschieferziegel Antike Stadt, Quelljuwel Wilden-Bau. Der Wayfinder zeigt danach den Weg.",
          ],
          tasks=[task_item("ars_additions:ritual_locate_structure", 1)],
          rewards=[reward_item("minecraft:compass", 1), reward_xp(3)],
          deps=["ritual_time"], icon="ars_additions:ritual_locate_structure", optional=True),

    quest("ritual_flowering", 7.5, 19, "&aMach Blüte und Überwucherung",
          subtitle="Blumen und Knochenmehl ohne Hand.",
          description=[
              "&aBlüte&r: Blühender Stamm, 3 Mohn, 3 Löwenzahn, Erdessenz. &aÜberwucherung&r: Blühender Stamm, 3 Magebloom, 2 Erdessenzen.",
              "",
              "Blüte füllt die Umgebung mit Blumen und Gras, jedes Quelljuwel +1 Radius. Überwucherung düngt Blöcke in der Nähe, mit einem Knochenblock lässt sie stattdessen Tierbabys schneller wachsen.",
          ],
          tasks=[task_item("ars_nouveau:ritual_flowering", 1), task_item("ars_nouveau:ritual_overgrowth", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(3)],
          deps=["ritual_forestation"], icon="ars_nouveau:ritual_overgrowth", optional=True),

    quest("ritual_small", 10, 19, "&aMach die vier kleinen Rituale",
          subtitle="Checkliste: Tiere, Überfall, Graben, Schwere.",
          description=[
              "&aTiere beschwören&r (Ärgerlicher Stamm, 3 magische Scherben, Lapisblock): Tiere des Bioms erscheinen.",
              "&aHerausforderung&r (Ärgerlicher Stamm, Smaragdblock, Tintenbeutel): startet in einem Dorf einen Überfall.",
              "&aGraben&r (Blühender Stamm, Eisenspitzhacke, Kohleblock): vier Löcher bis zum Grundgestein.",
              "&aSchwere&r (Blühender Stamm, Luft- und Erdessenz, Feder, Amboss): zwingt Spieler in der Nähe auf den Boden.",
          ],
          tasks=[task_item("ars_nouveau:ritual_animal_summon", 1), task_item("ars_nouveau:ritual_challenge", 1),
                 task_item("ars_nouveau:ritual_burrowing", 1), task_item("ars_nouveau:ritual_gravity", 1)],
          rewards=[reward_item("minecraft:emerald", 2), reward_xp(4)],
          deps=["ritual_flowering"], icon="ars_nouveau:ritual_burrowing", optional=True),

    quest("ritual_squirrels", 12.5, 19, "&aMach die Tafel Fast Squirrels",
          subtitle="Ars Elemental: Sternbunkel auf Espresso.",
          description=[
              "&eBlitzender Archwood-Stamm&r, Sternbunkel-Scherben, Zucker, Hasenpfote. Den gelben Setzling gibt es formlos aus einem Archwood-Setzling und Luftessenz.",
              "",
              "Alle Sternbunkel in &e15 Blöcken&r bekommen lange Tempo, alle 30 Sekunden aufgefrischt. Ein Goldblock als Zusatz verdoppelt den Radius.",
          ],
          tasks=[task_item("ars_elemental:ritual_squirrels", 1)],
          rewards=[reward_item("minecraft:sugar", 8)],
          deps=["familiar"], icon="ars_elemental:ritual_squirrels", optional=True),

    quest("el_rituals", 15, 19, "&aMach die Wächter-Rituale",
          subtitle="Ars Elemental: Checkliste für die Basis.",
          description=[
              "&aAnziehung&r (Blühender Stamm, 2 Eisenbarren, Erdessenz): zieht Wesen in &e8 Blöcken&r zum Becken.",
              "&aAbstoßung&r (Blitzender Stamm, 2 Luftessenzen, Kolben): stößt Wesen in &e15 Blöcken&r weg, mit Knochen nur Untote.",
              "&aEntdeckung&r (Blitzender Stamm, 2 Spinnenaugen, Glowstonestaub, Quelljuwelblock): Monster in &e128 Blöcken&r leuchten 10 Minuten.",
              "&aZapping&r (Blitzender Stamm, Luftessenz, 2 Diamanten, Blitzableiter, Quelljuwelblock): Blitze auf alles, was sich nähert.",
          ],
          tasks=[task_item("ars_elemental:ritual_attraction", 1), task_item("ars_elemental:ritual_repulsion", 1),
                 task_item("ars_elemental:ritual_detection", 1), task_item("ars_elemental:ritual_tesla_coil", 1)],
          rewards=[reward_item("minecraft:lightning_rod", 2), reward_xp(4)],
          deps=["ritual_squirrels"], icon="ars_elemental:ritual_detection", optional=True),

    quest("el_archwood", 17.5, 19, "&aMach die Archwood-Rituale",
          subtitle="Ars Elemental: Wald, Insel und Bienen.",
          description=[
              "&aArchwood-Aufforstung&r (Archwood-Stamm, Tafel Aufforstung, 4 Essenzen Erde, Wasser, Feuer, Luft): setzt Archwood-Bäume und düngt.",
              "&aInsel beschwören: Archwood-Wald&r (Archwood-Stamm, Abschwörungs- und Beschwörungsessenz): eine runde Insel mit Radius 7.",
              "&aBestäubung&r (Blühender Stamm, 2 Honigwaben, 2 Blumen, Erdessenz): Bienen sammeln schneller Nektar.",
          ],
          tasks=[task_item("ars_elemental:ritual_archwood_forestation", 1), task_item("ars_elemental:ritual_archwood_forest", 1),
                 task_item("ars_elemental:ritual_pollination", 1)],
          rewards=[reward_item("ars_elemental:yellow_archwood_sapling", 4), reward_xp(4)],
          deps=["el_rituals", "ritual_forestation"], icon="ars_elemental:ritual_archwood_forest", optional=True),

    # ---- Automatisierung ----------------------------------------------------------------
    quest("turret", 0, 24, "&a&lBau einen Einfachen Zauberturm",
          subtitle="Ein Zauber auf Redstone-Impuls.",
          description=[
              "Oben &e3 Quelljuwelen&r, Mitte Quelljuwel, &6Redstoneblock&r, Goldbarren, unten &e3 Goldbarren&r.",
              "",
              "Wirkt bei jedem Impuls den Zauber aus einem beschriebenen &6Pergament&r, mit Berühren oder Projektil, bezahlt mit Quelle aus Gläsern. Mit Truhe daneben gehen auch Artikelabholung und Block platzieren.",
              "",
              "Beispiel: &eBerühren, Brechen&r vor einem Bruchsteingenerator an einer Redstone-Uhr.",
          ],
          tasks=[task_item("ars_nouveau:basic_spell_turret", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_table("s2_uncommon")],
          deps=["welcome"], icon="ars_nouveau:basic_spell_turret", size=1.5, shape="square"),

    quest("spell_turret", 2.5, 23, "&aVerzaubere den Turm",
          subtitle="Halbe Kosten, gleiche Wirkung.",
          description=[
              "Im Apparat: Einfacher Zauberturm, &6Quelljuwelblock&r und &e2 Lohenruten&r.",
              "",
              "Der &6Verzauberte Zauberturm&r wirkt zum halben Quellpreis. Mit einem großen Fokus von Ars Elemental wird er ab Stufe 3 zum Elementar-Turm.",
          ],
          tasks=[task_item("ars_nouveau:spell_turret", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 2), reward_xp(5)],
          deps=["turret"], icon="ars_nouveau:spell_turret"),

    quest("prisms", 5, 23, "&aLenk Zauber mit Prismen",
          subtitle="Checkliste: Prisma, Fortgeschrittenes Prisma, Spiegel.",
          description=[
              "&6Zauberprisma&r: Ecken Gold, Seiten Archwood-Planken, Mitte Quarzblock. Lenkt Projektilzauber in seine Blickrichtung.",
              "&6Fortgeschrittenes Prisma&r (Ars Elemental): Prisma mit 4 Quarz und 4 Quelljuwelen, per Dominion-Zauberstab auf einen Block ausgerichtet, mit Linsen.",
              "&6Zauberspiegel&r (Ars Elemental, im Apparat aus Quelljuwelblock, 2 Archwood-Stämmen, 2 Quarz, 2 Gold, ergibt 2): wirft Projektile im Spiegelwinkel zurück.",
          ],
          tasks=[task_item("ars_nouveau:spell_prism", 1), task_item("ars_elemental:advanced_prism", 1),
                 task_item("ars_elemental:spell_mirror", 1)],
          rewards=[reward_item("minecraft:quartz", 8), reward_xp(4)],
          deps=["spell_turret"], icon="ars_nouveau:spell_prism", optional=True),

    quest("warp_scroll", 2.5, 25, "&6Schreib eine Warp-Schriftrolle",
          subtitle="Einmal nach Hause, bitte.",
          description=[
              "Formlos: &e4 Lapislazuli&r, &e4 Quelljuwelen&r, &6Leeres Pergament&r.",
              "",
              "Schleichend benutzen speichert den Ort, normal benutzen bringt dich hin und verbraucht die Rolle. Nicht über Dimensionen hinweg.",
          ],
          tasks=[task_item("ars_nouveau:warp_scroll", 2)],
          rewards=[reward_item("minecraft:lapis_lazuli", 8), reward_xp(3)],
          deps=["turret"], icon="ars_nouveau:warp_scroll"),

    quest("stable_warp", 5, 25, "&6Stabilisier die Schriftrolle",
          subtitle="Heimweg ohne Verbrauch.",
          description=[
              "Im Apparat: Warp-Schriftrolle, &e4 Lohenstaub&r, &e2 Enderperlen&r.",
              "",
              "Bleibt nach dem Benutzen erhalten. Eine beschriebene Rolle kopiert der Apparat für &d1 000 Quelle&r, gib Freunden eine mit eurer Gemeinschaftsbasis.",
          ],
          tasks=[task_item("ars_nouveau:stable_warp_scroll", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(4)],
          deps=["warp_scroll"], icon="ars_nouveau:stable_warp_scroll", optional=True),

    quest("wixie", 7.5, 24, "&dRuf einen Wixie",
          subtitle="Eine Hexe, die für dich craftet.",
          description=[
              "&dZerstreuen&r auf eine Hexe mit höchstens halber Gesundheit gibt &6Wixie-Scherben&r. Im Apparat mit Setzling, Smaragd, Werkbank und &6Braustand&r wird daraus der Charme.",
              "",
              "Charme auf einen &6Kessel&r: der &6Wixie-Kessel&r. Klick mit dem Wunsch-Item darauf, er craftet aus Truhen in der Nähe, jeder Craft kostet etwas Quelle. Podeste am Kessel geben ihm mehrere Rezepte im Wechsel.",
          ],
          tasks=[task_item("ars_nouveau:wixie_charm", 1)],
          rewards=[reward_item("minecraft:brewing_stand", 1), reward_xp(5)],
          deps=["turret"], icon="ars_nouveau:wixie_charm"),

    quest("potions", 10, 24, "&dLass den Wixie Tränke brauen",
          subtitle="Tränke automatisch, und Quelle daraus.",
          description=[
              "&6Trankglas&r: formlos Quellglas und Abschwörungsessenz. Leeres Trankglas neben den Kessel, Kessel mit einem Seltsamen Trank anklicken, Netherwarze in eine Truhe daneben.",
              "",
              "Der Wixie füllt &e3 Dosen&r pro Durchgang ins Glas. Der &6Alchemistische Quelllink&r (Braustand statt Lavaeimer) macht Quelle aus Tränken in Gläsern daneben, komplexe Tränke geben mehr.",
          ],
          tasks=[task_item("ars_nouveau:potion_jar", 1), task_item("ars_nouveau:alchemical_sourcelink", 1)],
          rewards=[reward_item("minecraft:nether_wart", 8), reward_xp(5)],
          deps=["wixie"], icon="ars_nouveau:potion_jar", optional=True),

    quest("charms2", 12.5, 24, "&6Füll die Nether-Charms",
          subtitle="Ars Additions: Checkliste für den Nether.",
          description=[
              "Alle im Apparat mit &6Glasflasche&r in der Mitte:",
              "&6Charm of Emberward&r (Magmacreme, Lavaeimer, Feuerzeug): durch Feuer gehen, in Lava schwimmen.",
              "&6Charm of Gilded Friendship&r (volle Goldrüstung, Vergoldeter Schwarzstein): Piglin-Barbaren bleiben ruhig.",
              "&6Charm of Decay's End&r (Wither-Rose, Witherskelettschädel, Milcheimer): schützt vor Wither.",
          ],
          tasks=[task_item("ars_additions:fire_resistance_charm", 1), task_item("ars_additions:golden_charm", 1),
                 task_item("ars_additions:wither_protection_charm", 1)],
          rewards=[reward_item("minecraft:magma_cream", 4), reward_xp(5)],
          deps=["wixie"], icon="ars_additions:fire_resistance_charm", optional=True),

    quest("caster_bag", 15, 24, "&6Bau Tasche und Aufzüge",
          subtitle="Ars Elemental: Spellcaster Bag und Strömungsaufzüge.",
          description=[
              "&6Spellcaster Bag&r: Trinkets Pouch mit 2 Manipulationsessenzen, 2 Lohenstaub, 2 Goldblöcken. Größer und färbbar.",
              "&6Blasenaufzug&r: Seelensand mit Luft- und Wasseressenz, 4 Prismarinsplitter. Hebt Wesen im Wasser wie eine Blasensäule.",
              "&6Magma-Aufzug&r: Seelensand mit Luft- und Feueressenz, 4 Magmablöcke. Trägt dich durch Lava nach oben, mit Feuerresistenz. Schleichen lässt dich sinken.",
          ],
          tasks=[task_item("ars_elemental:caster_bag", 1), task_item("ars_elemental:water_upstream", 1)],
          rewards=[reward_item("minecraft:soul_sand", 4), reward_xp(4)],
          deps=["charms2"], icon="ars_elemental:caster_bag", optional=True),

    # ---- Technik trifft Magie --------------------------------------------------------
    quest("blaze_burner", 0, 29, "&6Bau einen Leeren Lohenbrenner",
          subtitle="Kronwerke: Messing braucht einen Magier.",
          description=[
              "&eRezept auf Kronwerke:&r oben Quelljuwel, Eisenblech, Quelljuwel. Mitte Eisenblech, &6Netherrack&r, Eisenblech. Unten Mitte ein Eisenblech.",
              "",
              "Ohne Lohenbrenner kein Messing, ohne Messing kein Ziel von Stufe 2. Die Techniker brauchen deine Juwelen: bau Brenner oder tausch Juwelen gegen Messing.",
          ],
          tasks=[task_item("create:empty_blaze_burner", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_xp(5)],
          deps=["welcome"], icon="create:empty_blaze_burner", size=1.25),

    quest("calibrated_mechanism", 2.5, 29, "&6Kalibrier einen Präzisionsmechanismus",
          subtitle="Ars Technica: Präzision trifft Magie.",
          description=[
              "Im Apparat: &6Präzisionsmechanismus&r von Create in die Mitte, &e4 Amethystsplitter&r und &e4 Quelljuwelen&r auf die Podeste, &d500 Quelle&r.",
              "",
              "Der &6Calibrated Precision Mechanism&r steckt im Source Motor, im Spy Monocle und im Arcane Wrench (Create-Schraubenschlüssel mit Gold und Manipulationsessenz). Präzisionsmechanismen sind auch ein Stufenziel, sprich dich mit den Create-Bauern ab.",
          ],
          tasks=[task_item("ars_technica:calibrated_precision_mechanism", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 8), reward_xp(5)],
          deps=["blaze_burner"], icon="ars_technica:calibrated_precision_mechanism"),

    quest("source_motor", 5, 29, "&6Bau einen Source Motor",
          subtitle="Ars Technica: Quelle wird Drehung.",
          description=[
              "Ecken und unten Mitte &6Messingbarren&r, oben Mitte &6Elektronenröhre&r, links und rechts &6Zahnrad&r, Mitte der kalibrierte Mechanismus.",
              "",
              "Macht aus Quelle aus einem Glas daneben Rotationskraft für Create. Seiten stellen die Drehzahl, die Front das Verhältnis von Last zu Drehzahl. Mehr Kraft kostet mehr Quelle.",
          ],
          tasks=[task_item("ars_technica:source_motor", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["calibrated_mechanism", "relay"], icon="ars_technica:source_motor", size=1.5, shape="gear"),

    quest("glyph_press", 2.5, 31, "&dLern Press",
          subtitle="Ars Technica: die Presse als Glyphe.",
          description=[
              "Am Tisch, Stufe 2: &6Manipulationsessenz&r und &6Mechanische Presse&r.",
              "",
              "Presst Items am Boden wie eine Presse, Barren zu Blechen. Mit AOE mehr auf einmal, mit Extrakt Verdichten statt Pressen, mit Schmelzen beheizt.",
          ],
          tasks=[task_item("ars_technica:glyph_press", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["calibrated_mechanism"], icon="ars_technica:glyph_press", optional=True),

    quest("tech_glyphs", 5, 31, "&dLern die Create-Glyphen",
          subtitle="Ars Technica: Checkliste Stufe 2.",
          description=[
              "&dFuse&r (Manipulationsessenz, Feueressenz, 3 Lohenruten): mischt Items wie ein Mixer, nimmt Flüssigkeiten aus Tanks daneben.",
              "&dPolish&r (Manipulationsessenz, Sandpapier): schleift Items. &dWhirl&r (Manipulationsessenz, 3 Luftessenzen): ein Wirbel wie ein Ventilator, mit Wasser, Fackel, Schmelzen oder Verhexen als Verarbeitung.",
              "&dCarve&r (Manipulationsessenz, Werkbank, Bruchsteintreppe, -stufe, -mauer): sägt Stein und Holz zu Treppen. &dInsert&r (2 Truhen): legt Items in Behälter. &dApply&r (Manipulationsessenz, Messinghand): benutzt dein Zweithand-Item wie ein Einsatzgerät.",
          ],
          tasks=[task_item("ars_technica:glyph_fuse", 1), task_item("ars_technica:glyph_polish", 1),
                 task_item("ars_technica:glyph_whirl", 1), task_item("ars_technica:glyph_carve", 1),
                 task_item("ars_technica:glyph_insert", 1), task_item("ars_technica:glyph_apply", 1)],
          rewards=[reward_item("create:brass_ingot", 4), reward_xp(5)],
          deps=["glyph_press"], icon="ars_technica:glyph_fuse", optional=True),

    # ---- Stufenziel ---------------------------------------------------------------------
    quest("mage", 20, 15, "&d&lWerde Meister der Quelle",
          subtitle="Quelle für die ganze Stadt.",
          description=[
              "Leg &e16 Quelljuwelblöcke&r auf Vorrat.",
              "",
              "Relais tragen Quelle, Rituale ernten und schützen, Türme feuern, ein Motor treibt Create. Mit &6Stufe 3&r kommen das Erzmagier-Buch, Flug, Erwachen und die Roben. Weiter im Kapitel &dArs Nouveau: Meister&r.",
              "",
              "&eKronwerke:&r Die Magie-Säule von Stufe 2 sind Manaperlen und Terrastahl aus Botania. Bring deine Quelljuwelen zu den Ingenieuren, sie brauchen sie für jeden Lohenbrenner.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 16)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["spells2", "familiar", "spell_turret", "source_motor"], icon="ars_nouveau:source_gem_block",
          size=2.5, shape="gear"),
]

images = [
    banner("ars_apprentice/title", "Ars Nouveau: Magier", 10, -2.4, height=1.8, kind="title", colour="magic"),
    head("glyphen", "Glyphen der Stufe 2", 18, 0.6),
    head("quelle", "Quelle bewegen", 0, 7.9),
    head("rituale", "Rituale und Vertraute", 0, 13.6),
    head("automatisierung", "Automatisierung", 0, 21.6),
    head("technik", "Technik trifft Magie", 0, 27.6, colour="brass"),
    banner("ars_apprentice/ziel", "Stufenziel", 20, 13.2, height=0.9, colour="magic"),
]

chapter(C, "Ars Nouveau: Magier", "ars_nouveau:apprentice_spell_book", "magic", quests, shape="circle", order=12,
        stage=2, subtitle=["Stufe 2. Das zweite Buch, Relais, Rituale, Vertraute, Türme und Create."], images=images)
