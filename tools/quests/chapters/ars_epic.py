"""Ars Nouveau in stage 4: dragon's breath and the tier 3 glyphs that need End materials (Linger,
Wall, Glide), the void prism, the lingering flask cannon, the addons that use End materials (Ars
Additions ender source jar, End charms, locate structure for end cities, warp index; Ars Elemental
slipstream elevator and bangles; the warper relay), the sorcerer robes, the tier 3 armor upgrade
(chorus fruit), the gliding and undying threads, the Ars Elemental and Ars Technica armor sets on
tier 3 robes, and the Wilden Chimera in depth, whose tributes are the stage 5 magic goal (64,
fixed). Continues ars_master.py."""
from ftbq import (chapter, quest, task_item, task_kill, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_epic"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="magic"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Glyphen aus dem End ---------------------------------------------------------
    quest("breath", 0, 0, "&5&lFüll Drachenatem ab",
          subtitle="Was im Erzmagier-Buch noch fehlt.",
          description=[
              "Der Enderdrache spuckt Feuerbälle, die eine lila Wolke hinterlassen. Klick mit einer leeren &6Glasflasche&r in die Wolke.",
              "",
              pic("minecraft:dragon_breath"),
              "",
              "Ist der Drache tot, rufen &e4 Endkristalle&r auf dem Rand des Ausgangsportals ihn neu. Mit &6Stufe 4&r fehlen dem Erzmagier-Buch noch Verweilen, Wand und Gleiten, dazu kommen Roben des Zauberers, die dritte Rüstungsstufe und einiges aus den Erweiterungen.",
          ],
          tasks=[task_item("minecraft:dragon_breath", 4)],
          rewards=[reward_item("minecraft:glass_bottle", 16), reward_table("s4_common")],
          icon="minecraft:dragon_breath", size=2.0, shape="hexagon"),

    quest("linger", 2.5, -2, "&dLern Verweilen",
          subtitle="Ein Feld, das immer wieder zaubert.",
          description=[
              "Am Tisch, &e160 Punkte&r: &6Manipulationsessenz&r, &5Drachenatem&r, &bDiamantblock&r, &e2 Lohenruten&r.",
              "",
              "Eine Form: am Ziel entsteht ein Feld, das den Rest des Zaubers eine Weile immer wieder auf alles darin wirkt. AOE macht es größer, Beschleunigen schneller, Zeit verlängern länger, Empfindlich trifft Blöcke.",
              "",
              "&eProjektil, Verweilen, Verdorren&r mitten in eine Gruppe Endermen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_linger", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_xp(5)],
          deps=["breath"], icon="ars_nouveau:glyph_linger"),

    quest("wall", 2.5, 0, "&dLern Wand",
          subtitle="Eine Mauer aus Magie.",
          description=[
              "Am Tisch, &e160 Punkte&r: gleiches Rezept wie Verweilen.",
              "",
              "Statt eines Feldes steht eine Wand, die den Rest des Zaubers auf alles wirkt, was hindurchgeht. Die Verstärkungen wirken wie bei Verweilen. &eWand, Entzünden, Zeit verlängern&r quer über einen Gang.",
          ],
          tasks=[task_item("ars_nouveau:glyph_wall", 1)],
          rewards=[reward_item("ars_nouveau:manipulation_essence", 2), reward_xp(5)],
          deps=["breath"], icon="ars_nouveau:glyph_wall"),

    quest("glide", 2.5, 2, "&dLern Gleiten",
          subtitle="Elytren aus dem Zauberbuch.",
          description=[
              "Am Tisch, &e160 Punkte&r: &fLuftessenz&r, ein Paar &5Elytren&r, &e3 Diamanten&r.",
              "",
              "&eSelbst, Gleiten&r gibt dir den Effekt Gleiten wie mit angelegten Elytren, Zeit verlängern macht ihn länger. Elytren hängen in den Endschiffen, das Paar für die Glyphe ist weg, hol also zwei.",
          ],
          tasks=[task_item("ars_nouveau:glyph_glide", 1)],
          rewards=[reward_item("minecraft:firework_rocket", 16), reward_xp(5)],
          deps=["breath"], icon="ars_nouveau:glyph_glide"),

    quest("flask_cannon", 5, -2, "&6Bau die Verweilende Flaschenkanone",
          subtitle="Trankwolken auf Knopfdruck.",
          description=[
              "Im Apparat: &6Spritzflaschenkanone&r (Spender mit 2 Gold, 2 Lohenruten, 4 Schwarzpulver), &5Drachenatem&r, &e2 Luftessenzen&r.",
              "",
              "Verschießt Tränke aus deinen Trankflaschen als verweilende Wolke. Zusammen mit Wixie-Tränken eine gute Waffe für Gruppen.",
          ],
          tasks=[task_item("ars_nouveau:lingering_flask_cannon", 1)],
          rewards=[reward_item("minecraft:gunpowder", 8), reward_xp(4)],
          deps=["linger"], icon="ars_nouveau:lingering_flask_cannon", optional=True),

    quest("void_prism", 5, 0, "&5Bau ein Leereprisma",
          subtitle="Hier kommt kein Zauber durch.",
          description=[
              "Ein &6Zauberprisma&r umringt von &e8 Obsidian&r.",
              "",
              "Das normale Prisma lenkt Projektilzauber um, das Leereprisma vernichtet sie. Vor den Fenstern schützt es vor fremden Türmen und Freunden, die mit Platzen nicht genau zielen.",
          ],
          tasks=[task_item("ars_nouveau:void_prism", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(3)],
          deps=["wall"], icon="ars_nouveau:void_prism", optional=True),

    # ---- Erweiterungen ----------------------------------------------------------------
    quest("ender_jar", 7.5, -2, "&bBau ein Ender-Quellglas",
          subtitle="Ars Additions: eine Quelle an allen Orten.",
          description=[
              "Im Apparat: &6Quellglas&r in die Mitte, &e4 Enderperlen&r und &e4 Geplatzte Chorusfrüchte&r auf die Podeste.",
              "",
              "Alle Ender-Quellgläser teilen einen Vorrat. Füll eins an der Link-Farm, das zweite in der Außenbasis hat dieselbe Quelle. Geplatzte Chorusfrüchte kommen aus dem Ofen.",
          ],
          tasks=[task_item("ars_additions:ender_source_jar", 2)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 2), reward_xp(5)],
          deps=["linger"], icon="ars_additions:ender_source_jar"),

    quest("relay_warp", 10, -2, "&bBau ein Warper-Relais",
          subtitle="Quelle über jede Entfernung.",
          description=[
              "Im Apparat: &6Quellrelais&r mit &e4 Enderperlen&r und &e4 Geplatzten Chorusfrüchten&r.",
              "",
              "Wie ein Splitter, aber zwischen Warper-Relais ohne Reichweitengrenze. Über &e30 Blöcke&r geht ein Teil der Quelle verloren. Ars Elemental macht daraus mit 2 Luftessenzen und 2 Diamanten das Luft-Relais, das nichts mehr verliert.",
          ],
          tasks=[task_item("ars_nouveau:relay_warp", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["ender_jar"], icon="ars_nouveau:relay_warp", optional=True),

    quest("elevator", 12.5, -2, "&bBau einen Windstrom-Aufzug",
          subtitle="Ars Elemental: schweben statt Treppen.",
          description=[
              "Im Apparat: &6Goldblock&r in die Mitte, &e4 Luftessenzen&r, &6Wilden-Flügel&r, &e2 Shulkerschalen&r.",
              "",
              "Wesen darüber schweben nach oben, schleichend sinkst du langsam. Mehrere übereinander reichen höher. Solange jemand im Aufwind ist, kostet er Quelle.",
          ],
          tasks=[task_item("ars_elemental:air_upstream", 1)],
          rewards=[reward_item("minecraft:shulker_shell", 2), reward_xp(4)],
          deps=["relay_warp"], icon="ars_elemental:air_upstream", optional=True),

    quest("bangle", 7.5, 0, "&6Schmied einen Armreif",
          subtitle="Ars Elemental: Zauberschaden am Handgelenk.",
          description=[
              "Im Apparat: &6Ring des Potenzials&r in die Mitte, &6Quelljuwelblock&r, &e2 Goldblöcke&r, &5Endkristall&r auf die Podeste.",
              "",
              "Der &6Armreif des Verzauberers&r hat eine Chance, deinen Zauberschaden zu erhöhen, unzuverlässig. Auf eine Schule abgestimmt wird er stabil.",
          ],
          tasks=[task_item("ars_elemental:base_bangle", 1)],
          rewards=[reward_item("minecraft:gold_block", 2), reward_xp(5)],
          deps=["void_prism"], icon="ars_elemental:base_bangle", optional=True),

    quest("bangles", 10, 0, "&6Stimm Armreife auf die Schulen ab",
          subtitle="Ars Elemental: Checkliste der Armreife.",
          description=[
              "Armreif in den Apparat, dazu:",
              "&cFeuer&r (3 Feueressenzen, Feuerkugel): Treffer setzen in Brand. &bWasser&r (3 Wasseressenzen, Pulverschneeeimer): Treffer frieren ein.",
              "&aErde&r (3 Erdessenzen, Spinnweben): Treffer fesseln. &fLuft&r (3 Luftessenzen, Kolben): schneller, mehr Rückstoß.",
              "&dBeschwörung&r (2 Beschwörungsessenzen, Knochen, Wilden-Horn): Beschwörungen greifen dein Ziel an. &5Anima&r (2 Anima, Ghast-Träne, Wither-Rose).",
          ],
          tasks=[task_item("ars_elemental:fire_bangle", 1), task_item("ars_elemental:water_bangle", 1),
                 task_item("ars_elemental:earth_bangle", 1), task_item("ars_elemental:air_bangle", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 4), reward_xp(6)],
          deps=["bangle"], icon="ars_elemental:fire_bangle", optional=True),

    quest("locate", 5, 2, "&aFinde eine Endstadt",
          subtitle="Ars Additions: die Tafel Struktur finden mit Purpur.",
          description=[
              "Tafel aus Stufe 2: &5Ärgerlicher Stamm&r, &6Kompass&r, &6Quelljuwel&r, &6Wayfinder&r. Als Zusatz einen &5Purpurblock&r aufs Becken werfen.",
              "",
              "Am besten auf einer äußeren End-Insel starten. Der Wayfinder zeigt danach den Weg. Endstädte heißt Elytren, Shulkerschalen und Purpur, alles, was dieses Kapitel braucht.",
          ],
          tasks=[task_item("ars_additions:ritual_locate_structure", 1), task_item("minecraft:purpur_block", 4)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_xp(5)],
          deps=["glide"], icon="ars_additions:ritual_locate_structure"),

    quest("charms", 7.5, 2, "&bFüll die End-Charms",
          subtitle="Ars Additions: zwei Retter im Gepäck.",
          description=[
              "Im Apparat mit &6Glasflasche&r in der Mitte:",
              "&6Charm of Void's Salvation&r (Stabilisierte Warp-Schriftrolle, Endsteinziegel): rettet dich aus der Leere.",
              "&6Charm of Ender Serenity&r (Kürbis, Chorusfrucht): Endermen werden nicht wütend, wenn du sie ansiehst.",
              "Leer lädt die Imbuement-Kammer sie wieder auf.",
          ],
          tasks=[task_item("ars_additions:void_protection_charm", 1), task_item("ars_additions:ender_mask_charm", 1)],
          rewards=[reward_item("minecraft:end_stone_bricks", 8), reward_table("s4_common")],
          deps=["locate"], icon="ars_additions:void_protection_charm"),

    quest("charms_rare", 10, 2, "&bFüll die schweren Charms",
          subtitle="Ars Additions: Checkliste für Bosskämpfe.",
          description=[
              "&6Charm of Second Wind&r (Totem, Weinender Obsidian, Glowstone): rettet dich vor dem Tod, solange er geladen ist.",
              "&6Charm of Resonant Shield&r (Sculk, Schild, Weiße Wolle): schützt vor dem Schallschlag des Wärters.",
              "&6Charm of Unyielding Magic&r (Milcheimer, Schild, Spinnenauge, Wither-Rose): Zerstreuen nimmt dir deine Buffs nicht.",
          ],
          tasks=[task_item("ars_additions:undying_charm", 1), task_item("ars_additions:sonic_boom_protection_charm", 1),
                 task_item("ars_additions:dispel_protection_charm", 1)],
          rewards=[reward_item("minecraft:totem_of_undying", 1), reward_xp(6)],
          deps=["charms"], icon="ars_additions:undying_charm", optional=True),

    quest("warp_index", 12.5, 2, "&bBau einen Warp Index",
          subtitle="Ars Additions: dein Lager in der Tasche.",
          description=[
              "Im Apparat: &6Mundaner Gürtel&r, dazu &6Auge des Zauberers&r, &6Hellseher-Kristall&r, &6Sternbunkel-Charme&r, &6Bücherwurm-Charme&r. Das Auge: Hellseher-Kristall (Enderauge, Quelljuwel) mit 4 Lohenstaub und 4 Enderperlen.",
              "",
              "Greift aus der Ferne auf dein Aufbewahrungspult zu, in derselben Dimension. Mit Netheritbarren, Netherstern und Endertruhe wird er zum &6Stabilized Warp Index&r für alle Dimensionen.",
          ],
          tasks=[task_item("ars_additions:warp_index", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(6)],
          deps=["charms"], icon="ars_additions:warp_index", optional=True),

    # ---- Roben der dritten Stufe ------------------------------------------------------
    quest("sorcerer", 0, 6, "&6Näh die Roben des Zauberers",
          subtitle="Wenig Schutz, die stärksten Fäden.",
          description=[
              "Im Apparat: ein &6Gold-Rüstungsteil&r in die Mitte, &e4 Magieblütenfasern&r auf die Podeste.",
              "",
              "Der Zauberer schützt am wenigsten, hat aber die besten Fadenplätze: Brust und Hose haben schon ohne Aufwertung einen Platz der Größe 2. Kampfmagier ist das Gegenteil, Arkanist dazwischen.",
          ],
          tasks=[task_item("ars_nouveau:sorcerer_hood", 1), task_item("ars_nouveau:sorcerer_robes", 1),
                 task_item("ars_nouveau:sorcerer_leggings", 1), task_item("ars_nouveau:sorcerer_boots", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 16), reward_table("s4_common")],
          deps=["breath"], icon="ars_nouveau:sorcerer_robes"),

    quest("upgrade", 2.5, 6, "&6Bring eine Robe auf Stufe 3",
          subtitle="Chorusfrucht und 5 000 Quelle pro Teil.",
          description=[
              "Im Apparat: Robenteil der Stufe 2 in die Mitte, &e2 Enderperlen&r und &e1 Chorusfrucht&r auf die Podeste, &d5 000 Quelle&r.",
              "",
              "Stufe 3 gibt die meiste Mana-Regeneration und die größten Fadenplätze. Ein ganzes Set kostet von Stufe 1 an &d30 000 Quelle&r.",
          ],
          tasks=[task_item("minecraft:chorus_fruit", 4),
                 task_checkmark("Ein Robenteil auf Stufe 3 gebracht")],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(10)],
          deps=["sorcerer"], icon="minecraft:chorus_fruit"),

    quest("thread", 5, 5, "&6Näh den Faden des Gleitens",
          subtitle="Elytren, eingenäht.",
          description=[
              "Im Apparat: &6Leerer Faden&r, &e2 Luftessenzen&r, ein Paar &5Elytren&r.",
              "",
              "Du gleitest wie mit Elytren, der Brustplatz bleibt für die Robe frei. Braucht einen Fadenplatz der &eGröße 3&r.",
          ],
          tasks=[task_item("ars_nouveau:thread_gliding", 1)],
          rewards=[reward_item("ars_nouveau:air_essence", 2), reward_xp(6)],
          deps=["upgrade", "glide"], icon="ars_nouveau:thread_gliding"),

    quest("thread_undying", 5, 7, "&6Näh den Faden der Unsterblichkeit",
          subtitle="Ein Totem, das jede Nacht nachlädt.",
          description=[
              "Im Apparat: &6Leerer Faden&r, &6Totem der Unsterblichkeit&r, &6Phantomhaut&r, &e2 Abschwörungsessenzen&r.",
              "",
              "Einmal pro Schlaf rettet er dich vor dem Tod wie ein Totem. Braucht einen Fadenplatz der &eGröße 3&r, also eine Robe der Stufe 3.",
          ],
          tasks=[task_item("ars_nouveau:thread_undying", 1)],
          rewards=[reward_item("minecraft:phantom_membrane", 2), reward_xp(6)],
          deps=["upgrade"], icon="ars_nouveau:thread_undying", optional=True),

    quest("el_armor", 7.5, 6, "&6Weih eine Robe einem Element",
          subtitle="Ars Elemental: Rüstung einer Schule.",
          description=[
              "Im Apparat: ein Robenteil der &eStufe 3&r, &6Mal der Meisterschaft&r, &6Netheritbarren&r, &e2 Essenzen&r des Elements, &d7 000 Quelle&r.",
              "",
              "Jedes Teil verstärkt und verbilligt die Glyphen seiner Schule und senkt passenden Schaden, etwa Lava und Drachenatem beim Feuer. Volles Set: der abgewehrte Schaden wird zu Mana. Fäden und Verzauberungen bleiben erhalten.",
          ],
          tasks=[task_checkmark("Ein Elementar-Rüstungsteil gebaut")],
          rewards=[reward_item("ars_nouveau:source_gem_block", 4), reward_xp(8)],
          deps=["upgrade"], icon="ars_elemental:fire_robes", optional=True),

    quest("tech_armor", 10, 6, "&6Bau eine Technik-Robe",
          subtitle="Ars Technica: Technomancer, Machinaguard, Artificer.",
          description=[
              "Im Apparat: ein Robenteil der &eStufe 3&r, &6Mal der Technomantie&r, &6Netheritbarren&r, &e2 Messingbarren&r (beim Helm Messing und Ingenieursbrille), &d7 000 Quelle&r.",
              "",
              "Aus dem Arkanisten wird der Technomancer, aus dem Kampfmagier der Machinaguard, aus dem Zauberer der Artificer.",
          ],
          tasks=[task_checkmark("Ein Technik-Rüstungsteil gebaut")],
          rewards=[reward_item("create:brass_ingot", 16), reward_xp(8)],
          deps=["upgrade"], icon="ars_technica:technomancer_chestplate", optional=True),

    # ---- Die Chimäre --------------------------------------------------------------------
    quest("parts", 0, 11, "&5Sammle Teile für sechs Kämpfe",
          subtitle="Jeder Kampf frisst sechs Wilden-Teile.",
          description=[
              "Pro Chimäre: &e3 Teile&r für die Tafel &5Beschwöre Wilden&r (dazu Ärgerlicher Stamm, Lapisblock) und je ein &eStachel&r, &eHorn&r, &eFlügel&r als Zusatz.",
              "",
              "&eHörner&r von Jägern, &eFlügel&r von Pirschern, beide nachts um Wilden-Baue im Wald. &eStacheln&r nur von Verteidigern in kalten Biomen. Ein Wegstein im Schnee spart Wege. Die Tafel Struktur finden mit einem Quelljuwel zeigt den nächsten Wilden-Bau.",
          ],
          tasks=[task_item("ars_nouveau:wilden_spike", 4), task_item("ars_nouveau:wilden_horn", 4),
                 task_item("ars_nouveau:wilden_wing", 4)],
          rewards=[reward_item("minecraft:lapis_block", 4), reward_table("s4_common")],
          deps=["sorcerer"], icon="ars_nouveau:wilden_spike"),

    quest("phases", 2.5, 11, "&5Lern die vier Phasen",
          subtitle="Was die Chimäre im Kampf tut.",
          description=[
              "Bei jedem verlorenen Viertel ihrer &c1 000 Lebenspunkte&r hält sie an, ist kurz unverwundbar und bekommt Flügel, Stacheln oder Hörner, bis sie alles hat.",
              "",
              "&eFlügel:&r Sturzflug, der hier Blöcke zerstört. &eStacheln:&r Stachelbeschuss und Einrollen, &ceingerollt nimmt sie keinen Schaden&r und sticht im Nahkampf. &eHörner:&r Anlauf und Rammen.",
              "",
              "Lava macht sie stärker, Ertrinken und Ersticken schaden ihr nicht, Kälte wirkt schwächer.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:golden_apple", 2)],
          deps=["parts"], icon="ars_nouveau:ritual_wilden_summon"),

    quest("chimera_kill", 5, 11, "&5Besieg die Chimäre mit Fernkampf",
          subtitle="Abstand halten, nie in die Stacheln.",
          description=[
              "Freies, flaches Feld weit weg von Basen, keine Lava. &eProjektil, Blitz, Verstärken&r, Verweilen-Felder und Bögen halten dich auf Abstand.",
              "",
              "Gleiten oder der Faden des Gleitens helfen gegen Rammen und Sturzflug. Der Tribut liegt länger als normale Beute, aber heb ihn sofort auf.",
          ],
          tasks=[task_kill("ars_nouveau:wilden_boss", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_xp(10)],
          deps=["phases"], icon="ars_nouveau:wilden_tribute"),

    quest("hunt", 7.5, 11, "&5Sammle vier Tribute",
          subtitle="Übung für Stufe 5.",
          description=[
              "Bring &e4 Wilden-Tribute&r zusammen.",
              "",
              "Tribute wollen auch das Erzmagier-Buch, die Male der Meisterschaft und der Technomantie, der Fokus der Beschwörung und die dritte Stufe der Verzauberung Spellweave von Ars Additions. Leg früh ein Lager an.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 4)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 8), reward_table("s4_uncommon")],
          deps=["chimera_kill"], icon="ars_nouveau:wilden_tribute"),

    quest("epic", 11, 8.5, "&d&lMach dich bereit für Stufe 5",
          subtitle="Alles bereit für den Chaoswächter.",
          description=[
              "Bring &e8 Wilden-Tribute&r zusammen und benutz Verweilen oder Wand im Kampf.",
              "",
              "&eKronwerke:&r In Stufe 4 will der Obelisk auf der Magieseite &e128 Gaia-Geister&r und &e30 Mystische Stäbe&r. Gegen die Diener des Gaia-Wächters hilft ein Verweilen-Feld oder eine Wand.",
              "",
              "In &6Stufe 5&r will der Obelisk &e64 Wilden-Tribute&r, eine feste Zahl, jeder ein Chimärenkampf. Wer jetzt übt, schafft das später an wenigen Abenden.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 8),
                 task_checkmark("Einen Zauber mit Verweilen oder Wand im Kampf benutzt")],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["hunt", "thread"], icon="ars_nouveau:wilden_tribute", size=2.5, shape="gear"),
]

images = [
    banner("ars_epic/title", "Ars Nouveau: Episch", 6.5, -5.4, height=1.8, kind="title", colour="end"),
    head("glyphen", "Glyphen aus dem End", 0, -3.6),
    banner("ars_epic/erweiterungen", "Erweiterungen", 11, -3.6, height=0.9, colour="water"),
    head("roben", "Roben der dritten Stufe", 0, 4.0, colour="brass"),
    head("chimaere", "Die Chimäre", 0, 9.4, colour="fire"),
]

chapter(C, "Ars Nouveau: Episch", "ars_nouveau:glyph_linger", "magic", quests, shape="circle", order=41,
        stage=4, subtitle=["Stufe 4. Glyphen aus dem End, Roben der dritten Stufe und die Chimäre im Detail."],
        images=images)
