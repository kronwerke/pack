"""Ars Nouveau in stage 4: dragon's breath and the tier 3 glyphs that need End materials (Linger,
Wall, Glide), the void prism, the sorcerer robes, the second armor upgrade (chorus fruit) and the
gliding thread, the addons that use End materials (Ars Additions ender source jar, charms and the
locate structure ritual, Ars Elemental's slipstream elevator), and the Wilden Chimera in depth,
whose tributes are the stage 5 magic goal (64, fixed). Continues ars_master.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_epic"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Glyphen aus dem End -------------------------------------------------------
    quest("breath", 0, 0, "&5Drachenatem",
          subtitle="Was im Erzmagier-Buch noch fehlt.",
          description=[
              "Mit &6Stufe 4 (Sternwerk)&r ist das End offen, und damit fehlen dem &dErzmagier-Zauberbuch&r nur noch drei Glyphen der Stufe 3: &dVerweilen&r, &dWand&r und &dGleiten&r. Dazu kommen die Roben des Zauberers, die zweite Rüstungsaufwertung und einiges aus den Ars-Erweiterungen.",
              "",
              "&5Drachenatem&r füllst du mit leeren Glasflaschen ab. Der Enderdrache spuckt Feuerbälle, die am Boden eine lila Wolke hinterlassen. Klick mit einer Flasche in die Wolke.",
              "",
              pic("minecraft:dragon_breath"),
              "",
              "Ist der Drache schon besiegt, kann man ihn mit &e4 Endkristallen&r auf dem Rand des Ausgangsportals neu rufen. Sprecht euch ab und bringt viele Flaschen mit. Auch die &6Verweilende Flakon-Kanone&r (Lingering Flask Cannon: Splash-Flakon-Kanone, Drachenatem und 2 Luftessenzen im Bezaubernden Apparat) braucht welchen.",
          ],
          tasks=[task_item("minecraft:dragon_breath", 4)],
          rewards=[reward_item("minecraft:glass_bottle", 16), reward_table("s4_common")],
          icon="minecraft:dragon_breath", size=2.0, shape="hexagon"),

    quest("linger", 3.0, -2.2, "&dVerweilen",
          subtitle="Ein Feld, das immer wieder zaubert.",
          description=[
              "&dVerweilen&r (Linger) kostet am Tisch des Schreibers &e160 Erfahrungspunkte&r, eine &6Manipulationsessenz&r, einen &5Drachenatem&r, einen &bDiamantblock&r und &e2 Lohenruten&r.",
              "",
              "Es ist eine Form, die am Ziel ein Feld erzeugt. Eine kurze Zeit lang wirkt das Feld den Rest des Zaubers immer wieder auf alle Wesen darin.",
              "",
              "&dAOE&r macht das Feld größer, &dBeschleunigen&r lässt es öfter zaubern, &dZeit verlängern&r hält es länger, &dDämpfen&r ignoriert die Schwerkraft. Mit &dEmpfindlich&r trifft es Blöcke statt Wesen.",
              "",
              "Beispiel: &eProjektil, Verweilen, Verdorren&r mitten in eine Gruppe Endermen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_linger", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 4)],
          deps=["breath"], icon="ars_nouveau:glyph_linger"),

    quest("wall", 3.0, 0, "&dWand",
          subtitle="Eine Mauer aus Magie.",
          description=[
              "&dWand&r (Wall) hat genau dasselbe Rezept wie Verweilen: Manipulationsessenz, Drachenatem, Diamantblock und 2 Lohenruten, dazu &e160 Erfahrungspunkte&r.",
              "",
              "Statt eines runden Feldes entsteht eine Wand, die eine Weile stehen bleibt und den Rest des Zaubers auf alle Wesen wirkt, die durch sie hindurchgehen. Die Augmente funktionieren wie bei Verweilen.",
              "",
              "Beispiel: &eWand, Entzünden, Zeit verlängern&r quer über einen Gang, und alles, was durchläuft, brennt.",
          ],
          tasks=[task_item("ars_nouveau:glyph_wall", 1)],
          rewards=[reward_item("ars_nouveau:manipulation_essence", 2)],
          deps=["breath"], icon="ars_nouveau:glyph_wall"),

    quest("glide", 3.0, 2.2, "&dGleiten",
          subtitle="Elytren aus dem Zauberbuch.",
          description=[
              "&dGleiten&r (Glide) braucht eine &fLuftessenz&r, ein Paar &5Elytren&r und &e3 Diamanten&r, dazu &e160 Erfahrungspunkte&r.",
              "",
              "Elytren hängen in den Endschiffen bei den Endstädten auf den äußeren Inseln, bewacht von Shulkern. Für die Glyphe geht ein Paar verloren, also hol lieber zwei.",
              "",
              "&eSelbst, Gleiten&r gibt dir den Effekt Gleiten, mit dem du fliegst, als hättest du Elytren an. &dZeit verlängern&r macht ihn länger. Mit Feuerwerksraketen kommst du damit weit.",
          ],
          tasks=[task_item("ars_nouveau:glyph_glide", 1)],
          rewards=[reward_item("minecraft:firework_rocket", 16)],
          deps=["breath"], icon="ars_nouveau:glyph_glide"),

    quest("void_prism", 5.6, 0, "&5Leereprisma",
          subtitle="Hier kommt kein Zauber durch.",
          description=[
              "Das &5Leereprisma&r (Void Prism) ist ein Zauberprisma, umringt von &e8 Obsidian&r.",
              "",
              "Ein normales Prisma lenkt Projektilzauber in die Richtung, in die es zeigt. Das Leereprisma vernichtet jeden Projektilzauber, der hindurchfliegt.",
              "",
              "&eTipp:&r Leereprismen vor deinen Fenstern schützen dich vor fremden Zaubertürmen und vor Freunden, die mit Platzen und Blitz nicht so genau zielen.",
          ],
          tasks=[task_item("ars_nouveau:void_prism", 1)],
          rewards=[reward_item("minecraft:obsidian", 8)],
          deps=["wall"], icon="ars_nouveau:void_prism", optional=True),

    # ---- Erweiterungen ----------------------------------------------------------------
    quest("ender_jar", 5.6, -2.2, "&bEnder-Quellglas",
          subtitle="Ars Additions: eine Quelle für alle Orte.",
          description=[
              "Das &bEnder-Quellglas&r entsteht im &aBezaubernden Apparat&r aus einem Quellglas mit &e4 Enderperlen&r und &e4 geplatzten Chorusfrüchten&r auf den Podesten.",
              "",
              "Alle Ender-Quellgläser, die du aufstellst, teilen sich einen gemeinsamen Vorrat an Quelle. Füll eins in deiner Quelllink-Farm, und ein zweites in deiner Außenbasis oder im End hat dieselbe Quelle.",
              "",
              "Geplatzte Chorusfrüchte bekommst du, wenn du Chorusfrüchte im Ofen brätst.",
          ],
          tasks=[task_item("ars_additions:ender_source_jar", 2)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 4)],
          deps=["linger"], icon="ars_additions:ender_source_jar"),

    quest("elevator", 8.2, -2.2, "&bWindstrom-Aufzug",
          subtitle="Ars Elemental: schweben statt Treppen.",
          description=[
              "Der &bWindstrom-Aufzug&r (Slipstream Current Elevator) ist ein &6Goldblock&r im Bezaubernden Apparat, auf den Podesten &e4 Luftessenzen&r, ein &eWilden-Flügel&r und &e2 Shulkerschalen&r.",
              "",
              "Der Block erzeugt einen Aufwind, der Wesen darüber schweben lässt. Schleichst du, sinkst du langsam herab. Mehrere Aufzüge übereinander reichen höher. Solange jemand im Aufwind ist, zieht der Block Quelle.",
              "",
              "Es gibt auch Varianten für Wasser und Lava. Für die Luft braucht es Shulkerschalen aus den Endstädten.",
          ],
          tasks=[task_item("ars_elemental:air_upstream", 1)],
          rewards=[reward_item("minecraft:shulker_shell", 2)],
          deps=["ender_jar"], icon="ars_elemental:air_upstream", optional=True),

    quest("locate", 5.6, 2.2, "&aRitual: Struktur finden",
          subtitle="Ars Additions: der Weg zur nächsten Endstadt.",
          description=[
              "Die Ritualtafel &aStruktur finden&r craftest du formlos aus einem &5Ärgerlichen Archwood-Stamm&r, einem &eKompass&r, einem &dQuelljuwel&r und einem &eWegfinder&r (Amethystscherbe, umgeben von 4 Goldbarren).",
              "",
              "Welche Struktur das Ritual sucht, bestimmt der Zusatz auf dem Kohlenbecken. Mit einem &5Purpurblock&r sucht es eine &5Endstadt&r. Führ das Ritual am besten im End auf einer der äußeren Inseln durch. Der Wegfinder zeigt dir danach, wie weit es noch ist.",
              "",
              "Endstädte heißt: Elytren, Shulkerschalen und Purpur. Alles, was dieses Kapitel braucht.",
          ],
          tasks=[task_item("ars_additions:ritual_locate_structure", 1), task_item("minecraft:purpur_block", 4)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_xp(5)],
          deps=["glide"], icon="ars_additions:ritual_locate_structure"),

    quest("charms", 8.2, 2.2, "&bAmulette für das End",
          subtitle="Ars Additions: zwei Retter im Inventar.",
          description=[
              "Ars Additions hat &bAmulette&r (Charms), die in einen Curio-Platz kommen und eine bestimmte Zahl an Ladungen haben. Leer legst du sie in eine &aImbuement-Kammer&r, dort laden sie sich mit Quelle wieder auf.",
              "",
              "Zwei davon gehören in jedes Gepäck für das End:",
              "&bAmulett der Leerenrettung&r (Glasflasche, stabile Warp-Schriftrolle, Endsteinziegel): Fällst du in die Leere, bringt es dich zum letzten sicheren Ort zurück.",
              "&bAmulett der Enderruhe&r (Glasflasche, Kürbis, Chorusfrucht): Endermen werden nicht wütend, wenn du sie ansiehst.",
              "",
              "Beide entstehen im Bezaubernden Apparat mit der Flasche in der Mitte.",
          ],
          tasks=[task_item("ars_additions:void_protection_charm", 1)],
          rewards=[reward_item("minecraft:end_stone_bricks", 8), reward_table("s4_common")],
          deps=["locate"], icon="ars_additions:void_protection_charm"),

    # ---- Die Zauberer-Roben ------------------------------------------------------------
    quest("sorcerer", 0, 4.6, "&6Roben des Zauberers",
          subtitle="Wenig Schutz, die stärksten Fäden.",
          description=[
              "Die Roben des &6Zauberers&r (Sorcerer) entstehen wie die anderen Magierroben im &aBezaubernden Apparat&r, diesmal aus &6Goldrüstung&r: ein Goldteil in die Mitte, &e4 Magieblütenfasern&r auf die Podeste.",
              "",
              "Der Zauberer schützt am wenigsten, hat aber die besten Plätze für Fäden. Brustteil und Hose haben schon ohne Aufwertung einen Platz der Größe 2. Der Kampfmagier ist das Gegenteil, der Arkanist liegt dazwischen.",
              "",
              "Fäden wirken nur einmal pro Rüstungsset, gleiche Fäden auf zwei Teilen bringen nichts. Verteil sie also klug.",
          ],
          tasks=[task_item("ars_nouveau:sorcerer_hood", 1), task_item("ars_nouveau:sorcerer_robes", 1),
                 task_item("ars_nouveau:sorcerer_leggings", 1), task_item("ars_nouveau:sorcerer_boots", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 16), reward_table("s4_common")],
          deps=["breath"], icon="ars_nouveau:sorcerer_robes"),

    quest("upgrade", 3.0, 4.6, "&6Die höchste Rüstungsstufe",
          subtitle="Chorusfrüchte und 5 000 Quelle pro Teil.",
          description=[
              "Magierroben haben drei Stufen. Die erste Aufwertung kennst du aus dem Stahlwerk: 2 Lohenruten und 2 500 Quelle.",
              "",
              "Die zweite bringt die Rüstung auf die höchste Stufe. Leg das Rüstungsteil in den &aBezaubernden Apparat&r, auf die Podeste &e2 Enderperlen&r und &e1 Chorusfrucht&r, und der Apparat zieht &d5 000 Quelle&r.",
              "",
              "Jede Stufe erhöht die Manaregeneration und gibt mehr und größere Fadenplätze. Das voll aufgewertete Wickeltuch des Zauberers hat zwei Plätze der Größe 2 und einen der Größe 3.",
              "",
              "Für ein ganzes Set brauchst du also &d20 000 Quelle&r. Gut, dass du im Meister-Kapitel einen Vorrat angelegt hast.",
          ],
          tasks=[task_item("minecraft:chorus_fruit", 4),
                 task_checkmark("Ein Rüstungsteil auf die höchste Stufe gebracht")],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(10)],
          deps=["sorcerer"], icon="minecraft:chorus_fruit"),

    quest("thread", 5.6, 4.6, "&6Faden des Gleitens",
          subtitle="Elytren, eingenäht.",
          description=[
              "Der &6Faden des Gleitens&r entsteht im Bezaubernden Apparat aus einem leeren Faden, &e2 Luftessenzen&r und einem Paar &5Elytren&r.",
              "",
              "Mit ihm gleitest du, als würdest du Elytren tragen, und dein Brustplatz bleibt frei für die Rüstung. Er braucht aber einen Fadenplatz der &eGröße 3&r. Den haben zum Beispiel das Wickeltuch und die Hose des Zauberers nach der ersten Aufwertung.",
              "",
              "Fäden setzt du am &6Änderungstisch&r ein: Rüstung auf den Ständer, Faden auf die Tafel.",
          ],
          tasks=[task_item("ars_nouveau:thread_gliding", 1)],
          rewards=[reward_item("ars_nouveau:air_essence", 4)],
          deps=["upgrade", "glide"], icon="ars_nouveau:thread_gliding"),

    # ---- Die Chimäre --------------------------------------------------------------------
    quest("parts", 0, 7.4, "&5Sechs Teile pro Kampf",
          subtitle="Stachel, Horn und Flügel, und zwar doppelt.",
          description=[
              "Die &5Wilden-Chimäre&r kennst du aus dem Meister-Kapitel. In Stufe 5 wird sie zur Hauptaufgabe der Magier, also lohnt es sich, sie jetzt richtig zu lernen.",
              "",
              "Jeder Kampf braucht &e6 Wilden-Teile&r: drei für die Ritualtafel &5Beschwöre Wilden&r (mit Ärgerlichem Archwood-Stamm und Lapisblock) und je einen &eStachel&r, ein &eHorn&r und einen &eFlügel&r als Zusatz auf dem Kohlenbecken.",
              "",
              "&eWilden-Hörner&r lassen die &eJäger&r fallen, &eFlügel&r die &ePirscher&r, beide in Wäldern rund um Wilden-Baue. &eStacheln&r kommen von den &eVerteidigern&r, und die leben nur in kalten Biomen.",
              "",
              "&eTipp:&r Leg ein Lager an und füll es nach jeder Nacht auf. Für die Stacheln lohnt sich ein Wegstein im Schnee.",
          ],
          tasks=[task_item("ars_nouveau:wilden_spike", 4), task_item("ars_nouveau:wilden_horn", 4),
                 task_item("ars_nouveau:wilden_wing", 4)],
          rewards=[reward_item("minecraft:lapis_block", 4), reward_table("s4_common")],
          deps=["sorcerer"], icon="ars_nouveau:wilden_spike"),

    quest("phases", 3.0, 7.4, "&5Vier Phasen",
          subtitle="Was die Chimäre im Kampf tut.",
          description=[
              "Die Chimäre hat &c1 000 Lebenspunkte&r, aufgeteilt in vier Viertel. Jedes Mal, wenn ein Viertel weg ist, hält sie an, ist kurz unverwundbar und wächst. Ihr wachsen in zufälliger Reihenfolge &eFlügel&r, &eStacheln&r und &eHörner&r, bis sie in der letzten Phase alles hat.",
              "",
              "&eFlügel:&r Sie fliegt auf und stürzt sich herab. Der Sturzflug zerstört auf diesem Server Blöcke.",
              "&eStacheln:&r Sie verschießt Stacheln und rollt sich ein. &cEingerollt nimmt sie keinen Schaden&r, und wer in drei Blöcken Nähe zuschlägt, wird gestochen. Dann Abstand halten und warten.",
              "&eHörner:&r Sie nimmt Anlauf und rammt dich.",
              "",
              "Dazu ruft sie Verstärkung und gerät in Raserei. Lava macht ihr nichts aus, im Gegenteil, darin wird sie schneller und zäher. Auch Ertrinken und Ersticken schaden ihr nicht. Kälte wirkt schwächer. Durch ein Portal kannst du sie nicht locken.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:golden_apple", 4)],
          deps=["parts"], icon="ars_nouveau:ritual_wilden_summon"),

    quest("hunt", 5.6, 7.4, "&5Chimärenjagd",
          subtitle="Übung für Stufe 5.",
          description=[
              "Gute Vorbereitung für den Kampf:",
              "&e1.&r Ein freies, flaches Feld weit weg von Basen. Das Ritual zerstört die Blöcke ums Kohlenbecken, der Sturzflug auch.",
              "&e2.&r Keine Lava in der Nähe.",
              "&e3.&r Fernkampf: &eProjektil, Blitz, Verstärken&r, Verweilen-Felder, Bögen. So stehst du nie in den Stacheln.",
              "&e4.&r Gleiten oder der Faden des Gleitens, um dem Rammen und dem Sturzflug auszuweichen.",
              "",
              "Besiegt lässt sie einen &5Wilden-Tribut&r fallen. Der Tribut liegt länger herum als normale Beute, aber heb ihn trotzdem gleich auf.",
              "",
              "Neben dem Obelisken wollen auch andere Rezepte Tribute: das Erzmagier-Buch, das Mal der Meisterschaft, Mark of Technomancy und die dritte Stufe der Verzauberung Spellweave von Ars Additions.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 4)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 8), reward_table("s4_uncommon")],
          deps=["phases"], icon="ars_nouveau:wilden_tribute"),

    quest("epic", 9.2, 6.0, "&dEpischer Magier",
          subtitle="Alles bereit für den Chaoswächter.",
          description=[
              "Du hast alle Glyphen der Stufe 3, die volle Rüstung des Zauberers und weißt, wie die Chimäre kämpft.",
              "",
              "&eKronwerke:&r In dieser Stufe will der Obelisk auf der Magieseite &e128 Gaia-Geister&r und &e30 Mystische Stäbe&r von Mahou Tsukai. Beim Gaia-Wächter helfen deine neuen Glyphen: Ein Feld aus Verweilen oder eine Wand hält die Monster fern, die er ruft.",
              "",
              "In &6Stufe 5 (Chaoswerk)&r will der Obelisk dann &e64 Wilden-Tribute&r, eine feste Zahl, jeder ein Chimärenkampf. Wer jetzt schon Teile sammelt und übt, macht das später an wenigen Abenden.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 8),
                 task_checkmark("Einen Zauber mit Verweilen oder Wand im Kampf benutzt")],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["hunt", "thread"], icon="ars_nouveau:wilden_tribute", size=2.5, shape="gear"),
]

images = [
    banner("ars_epic/title", "Ars Nouveau: Episch", 4.6, -5.4, height=1.8, kind="title", colour="end"),
    banner("ars_epic/glyphen", "Glyphen aus dem End", 1.6, -3.6, height=0.9, colour="magic"),
    banner("ars_epic/erweiterungen", "Erweiterungen", 8.2, -3.6, height=0.9, colour="water"),
    banner("ars_epic/roben", "Die Zauberer-Roben", 2.8, 3.4, height=0.9, colour="brass"),
    banner("ars_epic/chimaere", "Die Chimäre", 2.8, 6.1, height=0.9, colour="fire"),
]

chapter(C, "Ars Nouveau: Episch", "ars_nouveau:glyph_linger", "magic", quests, shape="circle", order=41,
        stage=4, subtitle=["Stufe 4. Glyphen aus dem End, die Roben des Zauberers und die Chimäre im Detail."],
        images=images)
