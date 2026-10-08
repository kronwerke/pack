"""Ars Nouveau in stage 3: the Summon Wilden ritual and the Wilden Chimera, the Wither for its
nether star, the Archmage Spell Book and every tier 3 glyph that does not need End materials
(Ars Nouveau, Ars Elemental, Ars Additions, Ars Technica), Ars Elemental's Mark of Mastery and
the major foci, the focus of summoning, and what else opens with stage 3: the flight, awakening,
disintegration, warping and island rituals, Amethyst Golem and Bookwyrm, the adjustable and timer
turrets, the Arcanist and Battlemage robes with the first upgrade, the alteration table and threads,
charged certus quartz for AE2 and Ars Technica's Mark of Technomancy. Sorcerer robes, the tier 3
armor upgrade and the glyphs that need dragon's breath or elytra are stage 4 (ars_epic.py)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_master"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="magic"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Die Chimäre ------------------------------------------------------------------
    quest("wilden_ritual", 0, 1.5, "&5&lMach die Tafel Beschwöre Wilden",
          subtitle="Der Weg zum Erzmagier führt durch einen Bosskampf.",
          description=[
              "Formlos: &5Ärgerlicher Archwood-Stamm&r, &e3 Wilden-Teile&r (Stachel, Horn, Flügel, gemischt), &9Lapisblock&r.",
              "",
              "Ohne Zusätze ruft das Ritual eine Gruppe Wilden. Wirf je einen &eStachel&r, ein &eHorn&r und einen &eFlügel&r auf das Becken, dann kommt die &5Wilden-Chimäre&r. Nur sie gibt den &5Wilden-Tribut&r für das Erzmagier-Buch.",
          ],
          tasks=[task_item("ars_nouveau:ritual_wilden_summon", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 16), reward_table("s3_common")],
          icon="ars_nouveau:ritual_wilden_summon", size=2.0, shape="hexagon"),

    quest("tribute", 2.5, 1.5, "&5Besieg die Wilden-Chimäre",
          subtitle="Stachel, Horn und Flügel in einem Körper.",
          description=[
              "Ritual draußen auf freiem Feld starten. &cBeim Erscheinen zerstört die Chimäre die Blöcke rund um das Becken&r, ihr Sturzflug auf diesem Server ebenso.",
              "",
              "Laut Handbuch ein Kampf für Magier mit Stufe-2-Zaubern und guter Ausrüstung. Sie widersteht Kälte. Geht zu zweit oder dritt, nehmt Heilen, Langsamer Fall und Zerstreuen mit.",
              "",
              pic("ars_nouveau:wilden_tribute"),
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 1)],
          rewards=[reward_item("minecraft:golden_apple", 2), reward_table("s3_uncommon")],
          deps=["wilden_ritual"], icon="ars_nouveau:wilden_tribute", size=1.25),

    quest("mark_of_mastery", 2.5, -0.5, "&6Teil den Tribut in Male",
          subtitle="Ars Elemental: ein Tribut, fünf Male der Meisterschaft.",
          description=[
              "In der Kammer: &5Wilden-Tribut&r hinein, alle &e8 Essenzen&r auf die Podeste (Erde, Feuer, Wasser, Luft, Abschwörung, Beschwörung, Manipulation, Anima), &d10 000 Quelle&r. Ergibt &e5 Male&r.",
              "",
              "Male brauchst du für die großen Foki, die Elementar-Rüstungen ab Stufe 4 und die Glyphe Abwehr aufheben.",
          ],
          tasks=[task_item("ars_elemental:mark_of_mastery", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 2), reward_xp(5)],
          deps=["tribute"], icon="ars_elemental:mark_of_mastery", optional=True),

    quest("major_focus", 5, -0.5, "&6Schleif einen großen Fokus",
          subtitle="Ars Elemental: Meister einer Schule.",
          description=[
              "Im Apparat: &6Kleiner Fokus&r in die Mitte, ein &6Mal der Meisterschaft&r aufs Podest, &d5 000 Quelle&r.",
              "",
              "Der große Fokus verstärkt seine Schule, ohne die anderen zu schwächen. &cFeuer&r: Zauberschaden II, solange du brennst. &bWasser&r: Mana-Regeneration, wenn du nass bist. &fLuft&r: Mana-Regeneration über Y 200. &aErde&r: Mana-Regeneration unter Y 0.",
              "",
              "Mit Verzaubertem Zauberturm, 3 Essenzen und dem Fokus in der Kammer (&d5 000 Quelle&r) entsteht ein Elementar-Turm: 65 Prozent billiger für Zauber seiner Schule.",
          ],
          tasks=[task_item("ars_elemental:fire_focus", 1)],
          rewards=[reward_item("minecraft:gold_block", 2), reward_xp(5)],
          deps=["mark_of_mastery"], icon="ars_elemental:fire_focus", optional=True),

    quest("summon_focus", 2.5, 3.5, "&6Bau den Fokus der Beschwörung",
          subtitle="Stärkere Beschwörungen, mit einem Tribut.",
          description=[
              "Im Apparat: &6Quelljuwelblock&r in die Mitte, &6Wilden-Horn&r, &6-Stachel&r, &6-Flügel&r, &5Wilden-Tribut&r, &6Goldbarren&r auf die Podeste.",
              "",
              "Beschworene Wesen halten länger, sind stärker und schneller. Selbst-Zauber wirken als Kopie auch auf sie. Ars Elemental macht daraus mit 2 Wither-Rosen, Witherskelettschädel und Anima den &6Fokus der Nekromantie&r: deine Beschwörungen stehen einmal wieder auf.",
          ],
          tasks=[task_item("ars_nouveau:summon_focus", 1)],
          rewards=[reward_item("minecraft:bone_block", 4), reward_xp(5)],
          deps=["tribute"], icon="ars_nouveau:summon_focus", optional=True),

    quest("nether_star", 5, 1.5, "&fHol einen Netherstern",
          subtitle="Auch der Wither muss fallen.",
          description=[
              "&e4 Seelensand&r in T-Form, &e3 Witherskelettschädel&r obendrauf.",
              "",
              "&cDer Wither zerstört Blöcke.&r Ruf ihn tief unter der Erde oder weit weg von Basen, am besten zu mehreren. Ein Wither gibt einen Stern. Schädel gibt es in Netherfestungen, gezielt auch mit einem Witherskelett-Modell aus Hostile Neural Networks.",
          ],
          tasks=[task_item("minecraft:nether_star", 1)],
          rewards=[reward_item("minecraft:soul_sand", 4), reward_xp(10)],
          deps=["tribute"], icon="minecraft:nether_star"),

    quest("archmage_book", 7.5, 1.5, "&d&lBau das Erzmagier-Zauberbuch",
          subtitle="Das dritte Buch: Glyphen der Stufe 3.",
          description=[
              "Formlos: &6Zauberbuch des Magiers&r, &e3 Enderperlen&r, &e2 Smaragde&r, &6Totem der Unsterblichkeit&r, &fNetherstern&r, &5Wilden-Tribut&r.",
              "",
              "Nur damit lernst und benutzt du &dGlyphen der Stufe 3&r, je &e160 Erfahrungspunkte&r am Tisch. Noch einmal &e+50&r Mana und &e+1&r pro Sekunde.",
              "",
              "Verweilen, Wand und Gleiten brauchen Drachenatem oder Elytren und kommen in Stufe 4.",
          ],
          tasks=[task_item("ars_nouveau:archmage_spell_book", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_table("s3_uncommon")],
          deps=["nether_star"], icon="ars_nouveau:archmage_spell_book", size=2.0, shape="diamond"),

    # ---- Glyphen der Stufe 3 -------------------------------------------------------
    quest("glyph_blink", 10, -1, "&dLern Blinzeln und Immateriell",
          subtitle="Teleport und durch Wände gehen.",
          description=[
              "&dBlinzeln&r: &6Manipulationsessenz&r, &e4 Enderperlen&r. &dImmateriell&r: Manipulationsessenz, &e3 Phantomhäute&r, &e2 Enderperlen&r.",
              "",
              "&eSelbst, Blinzeln&r springt nach vorn, &eProjektil, Blinzeln&r an den Einschlag. Mit einer Warp-Schriftrolle in der Zweithand schickst du getroffene Wesen dorthin. Immateriell macht Blöcke kurz zu Luft, sie kommen danach zurück.",
          ],
          tasks=[task_item("ars_nouveau:glyph_blink", 1), task_item("ars_nouveau:glyph_intangible", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_blink"),

    quest("glyph_lightning", 10, 1, "&dLern Blitz",
          subtitle="Ein Gewitter aus dem Zauberbuch.",
          description=[
              "Am Tisch: &fLuftessenz&r, &e3 Blitzableiter&r, &bHerz des Meeres&r.",
              "",
              "Ruft einen Blitz. Getroffene bekommen &eSchock&r, der bis Stufe III wächst und weiteren Blitzschaden verstärkt. Nasse Gegner trifft es härter. &eProjektil, Blitz, Verstärken&r ist simpel und stark.",
          ],
          tasks=[task_item("ars_nouveau:glyph_lightning", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_lightning"),

    quest("glyph_burst", 10, 3, "&dLern Platzen",
          subtitle="Alles in einer Kugel um das Ziel.",
          description=[
              "Am Tisch: &6Manipulationsessenz&r, &e5 TNT&r, &6Feuerwerksstern&r.",
              "",
              "Wirkt den Rest des Zaubers auf alles in einer Kugel um das Ziel. AOE vergrößert sie, Empfindlich trifft Blöcke, Dämpfen macht sie hohl. &eProjektil, Platzen, Blitz&r gegen Gruppen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_burst", 1)],
          rewards=[reward_item("minecraft:tnt", 4), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_burst"),

    quest("technica", 10, 5, "&dLern Obliterate und Superheat",
          subtitle="Ars Technica: die Meisterglyphen für Create.",
          description=[
              "&dObliterate&r: &6Manipulationsessenz&r, &6Amboss&r, &6Diamantblock&r. &dSuperheat&r: &e3 Feueressenzen&r, &6Lohenrute&r, &6Lohenkuchen&r.",
              "",
              "Obliterate schlägt mit einem arkanen Hammer zu, mit Empfindlich verarbeitet es Items wie Brechräder. Superheat macht aus Fuse ein überhitztes Mischen. Ein Zauberturm über einem Depot von Create ist eine kleine Fabrik.",
          ],
          tasks=[task_item("ars_technica:glyph_obliterate", 1), task_item("ars_technica:glyph_superheat", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["glyph_burst"], icon="ars_technica:glyph_obliterate"),

    quest("glyph_split", 12.5, -1, "&dLern Teilen und Orbit",
          subtitle="Ein Zauber, viele Kugeln.",
          description=[
              "&dTeilen&r: &6Splitter&r (das Relais), &6Wilden-Stachel&r, &6Steinsäge&r. &dOrbit&r: &6Kompass&r, &6Enderauge&r, &6Lohenrute&r.",
              "",
              "Teilen verschießt mehrere Projektile mit dem ganzen Zauber. Orbit ist eine Form: drei Kugeln kreisen um dich und treffen alles, was zu nah kommt, mit Empfindlich auch Blöcke.",
          ],
          tasks=[task_item("ars_nouveau:glyph_split", 1), task_item("ars_nouveau:glyph_orbit", 1)],
          rewards=[reward_item("minecraft:stonecutter", 1), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_split"),

    quest("glyph_summon", 12.5, 1, "&dLern die Beschwörungen",
          subtitle="Checkliste Stufe 3: Verbündete aus dem Nichts.",
          description=[
              "Alle mit &6Beschwörungsessenz&r:",
              "&dVex beschwören&r (Totem der Unsterblichkeit): drei Vexe kämpfen eine Weile.",
              "&dUntote beschwören&r (Knochen, Witherskelettschädel): Skelette, Verstärken gibt bessere Waffen.",
              "&dReißzähne&r (2 Prismarinsplitter, Totem): Fangzähne wie beim Magier. &dLockvogel&r (4 Rüstungsständer): eine Kopie von dir, die Monster anzieht.",
          ],
          tasks=[task_item("ars_nouveau:glyph_summon_vex", 1), task_item("ars_nouveau:glyph_summon_undead", 1),
                 task_item("ars_nouveau:glyph_fangs", 1), task_item("ars_nouveau:glyph_summon_decoy", 1)],
          rewards=[reward_item("minecraft:totem_of_undying", 1), reward_xp(6)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_summon_vex"),

    quest("glyph_hex", 12.5, 3, "&dLern Verhexen, Verdorren und Zurückspulen",
          subtitle="Checkliste Stufe 3: Flüche und Zeit.",
          description=[
              "&dVerhexen&r (Abschwörungsessenz, Fermentiertes Spinnenauge, 3 Lohenruten, Wither-Rose): mehr Schaden unter Gift, Wither oder Feuer, halbe Heilung und Mana-Regeneration.",
              "&dVerdorren&r (Abschwörungsessenz, 3 Witherskelettschädel): Wither-Effekt.",
              "&dZurückspulen&r (Manipulationsessenz, 3 Uhren): setzt ein Wesen an frühere Orte und Gesundheit zurück.",
          ],
          tasks=[task_item("ars_nouveau:glyph_hex", 1), task_item("ars_nouveau:glyph_wither", 1),
                 task_item("ars_nouveau:rewind", 1)],
          rewards=[reward_item("minecraft:clock", 1), reward_xp(6)],
          deps=["archmage_book"], icon="ars_nouveau:glyph_hex"),

    quest("additions_t3", 12.5, 5, "&dLern Mark, Recall und Retaliate",
          subtitle="Ars Additions: Ziele merken und vergelten.",
          description=[
              "&dMark&r (Manipulationsessenz, Enderperle, Eindämmungsglas, Tafel Eindämmung): speichert das Ziel in einem &6Unstable Reliquary&r in der Zweithand.",
              "&dRecall&r (Beschwörungsessenz, Enderperle, Schriftrolle des Sehers, Auge des Zauberers): wirkt den Zauber auf das gespeicherte Ziel.",
              "&dRetaliate&r (Netheritschwert, Verzaubertes Buch): trifft den, der dich in den letzten 5 Sekunden verletzt hat.",
          ],
          tasks=[task_item("ars_additions:glyph_mark", 1), task_item("ars_additions:glyph_recall", 1),
                 task_item("ars_additions:glyph_retaliate", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["glyph_hex"], icon="ars_additions:glyph_mark", optional=True),

    quest("el_fire", 15, -1, "&dLern die Feuer-Glyphen von Ars Elemental",
          subtitle="Checkliste Stufe 3: Ars Elemental, Feuer.",
          description=[
              "&dAusbrennen&r (Feuer- und Abschwörungsessenz, Lohenstaub, Ghast-Träne): etwas Feuerschaden, entfernt dafür alle Effekte, die Milch heilt.",
              "&dFeuersbrunst&r (Schwarzpulver, Feueressenz, Bombengranat, Netheritplatten): brennende Ziele explodieren und stecken andere an.",
              "&dRaserei&r (Feueressenz, Anima, Wilden-Horn, Roter Teppich, Fermentiertes Spinnenauge): das Ziel greift alles in der Nähe an.",
          ],
          tasks=[task_item("ars_elemental:glyph_cauterize", 1), task_item("ars_elemental:glyph_conflagrate", 1),
                 task_item("ars_elemental:glyph_rage", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 2), reward_xp(5)],
          deps=["archmage_book"], icon="ars_elemental:glyph_conflagrate", optional=True),

    quest("el_water", 15, 1, "&dLern die Wasser-Glyphen von Ars Elemental",
          subtitle="Checkliste Stufe 3: Ars Elemental, Wasser.",
          description=[
              "&dKavitation&r (Wasseressenz, Herz des Meeres, Kugelfisch, Schwamm): ein Ziel in einer Blase implodiert, Schaden im Umkreis.",
              "&dWasserstrahl&r (Wasser- und Manipulationsessenz, Prismarinsplitter, Wilden-Stachel, Böenrute): durchschlägt das nächste Ziel und ignoriert Rüstung.",
              "&dOxidieren&r (Wasser-, Luft- und Abschwörungsessenz, Oxidiertes Kupfer): senkt die Rüstung des Ziels.",
          ],
          tasks=[task_item("ars_elemental:glyph_cavitate", 1), task_item("ars_elemental:glyph_water_jet", 1),
                 task_item("ars_elemental:glyph_oxidize", 1)],
          rewards=[reward_item("minecraft:sponge", 1), reward_xp(5)],
          deps=["el_fire"], icon="ars_elemental:glyph_water_jet", optional=True),

    quest("el_homing", 15, 3, "&dLern Zielsuche und Lebensband",
          subtitle="Checkliste Stufe 3: Ars Elemental, Form und Anima.",
          description=[
              "&dZielsuchendes Projektil&r (Netherstern, Manipulationsessenz, Wünschelrute, Enderauge): sucht sich das nächste Wesen. &dZielsuche weitergeben&r (Manipulationsessenz, die Glyphe): schießt den Rest des Zaubers als Zielsuche neu ab.",
              "&dLebensband&r (Leine, Anima, Sculk-Sensor): dein Schaden und seine Heilung werden geteilt.",
              "&dAbwehr aufheben&r (Netherstern, 2 Male der Meisterschaft, Netheritblock): das Ziel verliert seine Unverwundbarkeit nach Treffern.",
          ],
          tasks=[task_item("ars_elemental:glyph_homing_projectile", 1), task_item("ars_elemental:glyph_propagator_homing", 1),
                 task_item("ars_elemental:glyph_life_link", 1)],
          rewards=[reward_item("minecraft:ender_eye", 2), reward_xp(6)],
          deps=["el_water"], icon="ars_elemental:glyph_homing_projectile", optional=True),

    quest("archmage", 18.5, 2, "&d&lWerde Erzmagier",
          subtitle="Bereit für die Sterne.",
          description=[
              "Leg &e32 Quelljuwelblöcke&r auf Vorrat und bau einen Zauber mit Glyphen der Stufe 3.",
              "",
              "Mit &6Stufe 4&r kommen Roben des Zauberers, die dritte Rüstungsstufe, das Leereprisma und die Glyphen mit Drachenatem. Weiter im Kapitel &dArs Nouveau: Episch&r.",
              "",
              "&eKronwerke:&r Der Obelisk will auf der Magieseite Elementium, Afrit-Essenz und Elfensterne. Deine Kammern laden den Certus-Quarz der Techniker, und mit Blitz und Platzen bist du die beste Begleitung bei jeder Afrit-Beschwörung.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 32),
                 task_checkmark("Einen Zauber mit Glyphen der Stufe 3 gebaut")],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["technica", "glyph_split", "glyph_summon", "glyph_lightning"], icon="ars_nouveau:archmage_spell_book",
          size=2.5, shape="gear"),

    # ---- Neu im Stahlwerk ---------------------------------------------------------------
    quest("stahlwerk", 0, 9.5, "&aSchau, was Stufe 3 bei Ars öffnet",
          subtitle="Rituale, Türme und Roben ohne Erzmagier-Buch.",
          description=[
              "Mit dem Stahlwerk öffnen auch ohne neues Buch: die Rituale &aFlug&r, &aErwachen&r, &aZerfall&r, &aVerziehen&r und die zwei &aInseln&r, der &aVerstellbare&r und der &aTimer-Zauberturm&r, die Roben von &6Arkanist&r und &6Kampfmagier&r.",
              "",
              "Dazu von Ars Additions &aArcane Permanence&r (Kaskadierender Stamm, Netherstern, Quelljuwel, Erdessenz): lädt die Chunks um das Becken, solange Quelle fließt.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("ars_nouveau:source_gem", 8)],
          deps=["wilden_ritual"], icon="ars_nouveau:ritual_brazier"),

    quest("ritual_flight", 2.5, 8.5, "&aMach die Tafel Flug",
          subtitle="Fliegen wie im Kreativmodus, solange die Quelle reicht.",
          description=[
              "&5Ärgerlicher Stamm&r, &e3 Wilden-Flügel&r, &e2 Diamanten&r, &6Enderperle&r. Ars Elemental kennt eine zweite Tafel: Blitzender Stamm, Wilden-Flügel, 2 Diamanten, Feder.",
              "",
              "Spieler in der Nähe bekommen beim Springen den Effekt &eFlug&r, und das Ritual frischt ihn auf, solange sie in der Nähe bleiben. Jedes Mal kostet es Quelle aus den Gläsern.",
          ],
          tasks=[task_item("ars_nouveau:ritual_flight", 1)],
          rewards=[reward_item("ars_nouveau:wilden_wing", 2), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:ritual_flight"),

    quest("ritual_disintegration", 2.5, 10.5, "&aMach die Tafel Zerfall",
          subtitle="Monster werden zu Erfahrung.",
          description=[
              "&cFlammender Stamm&r, &e3 Goldschwerter&r, &e3 Bücher&r.",
              "",
              "Monster in der Nähe zerfallen zu &6Erfahrungsjuwelen&r mit doppelter Erfahrung, ohne Beute. Jedes kostet etwas Quelle. Am Ausgang einer Monsterfarm die schnellste Quelle für die 160 Punkte jeder Glyphe der Stufe 3.",
          ],
          tasks=[task_item("ars_nouveau:ritual_disintegration", 1)],
          rewards=[reward_item("ars_nouveau:greater_experience_gem", 2), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:ritual_disintegration"),

    quest("ritual_awakening", 5, 8.5, "&aMach die Tafel Erwachen",
          subtitle="Wächter aus Bäumen, Golems aus Amethyst.",
          description=[
              "&aBlühender Stamm&r, je ein Setzling der &e4 Archwood-Farben&r, &e4 Quelljuwelen&r.",
              "",
              "Archwood-Bäume in der Nähe werden zu &dWaldläufern&r, die einen Ort bewachen (Dominion-Zauberstab: erst den Läufer, dann den Block). Ihre Farbe bestimmt den Zauber: Fackel, Einfrieren, Schaden mit Schlinge oder Verhexen mit Verdorren.",
          ],
          tasks=[task_item("ars_nouveau:ritual_awakening", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_xp(5)],
          deps=["ritual_flight"], icon="ars_nouveau:ritual_awakening"),

    quest("golem_bookwyrm", 7.5, 8.5, "&dWeck Amethyst-Golem und Bücherwurm",
          subtitle="Juwelen-Nachschub und ein Lager für alles.",
          description=[
              "Erwachen neben &6Knospendem Amethyst&r gibt einen &6Amethyst-Golem-Charme&r. Mit &6Buch und Feder&r als Zusatz gibt es &6Bücherwurm-Charmes&r.",
              "",
              "Der Golem erntet Amethyst in &e10 Blöcken&r um sein Zuhause, macht Amethystblöcke zu Knospendem Amethyst und lässt Knospen schneller wachsen. Der Bücherwurm erweitert das &6Aufbewahrungspult&r (Pult, 4 Truhen): je Wurm &e8&r verbundene Inventare mehr, bis &e30 Blöcke&r weit.",
          ],
          tasks=[task_item("ars_nouveau:amethyst_golem_charm", 1), task_item("ars_nouveau:bookwyrm_charm", 1)],
          rewards=[reward_item("minecraft:amethyst_block", 4), reward_xp(6)],
          deps=["ritual_awakening"], icon="ars_nouveau:amethyst_golem_charm"),

    quest("islands_warping", 5, 10.5, "&aMach Verziehen und die Inseln",
          subtitle="Checkliste: Reisen und Gelände.",
          description=[
              "&aVerziehen&r (Ärgerlicher Stamm, Warp-Schriftrolle): bringt alle Wesen in der Nähe zum Ort auf einer zusätzlich eingelegten Rolle.",
              "&aInsel: Ebene&r (Blühender Stamm, Grasblock, Erdessenz) und &aInsel: Wüste&r (Flammender Stamm, Sand, Erdessenz): eine runde Insel mit Radius 7, jedes Quelljuwel +1. Frostaya macht Schnee, Terrakotta Tafelberge.",
          ],
          tasks=[task_item("ars_nouveau:ritual_warping", 1), task_item("ars_nouveau:ritual_conjure_island_plains", 1),
                 task_item("ars_nouveau:ritual_conjure_island_desert", 1)],
          rewards=[reward_item("minecraft:grass_block", 16), reward_xp(4)],
          deps=["ritual_disintegration"], icon="ars_nouveau:ritual_conjure_island_plains", optional=True),

    quest("turrets", 7.5, 10.5, "&aBau Timer- und Verstellbaren Zauberturm",
          subtitle="Türme, die von selbst feuern und überall hinzielen.",
          description=[
              "&aVerstellbar&r: formlos aus einem Einfachen Zauberturm, ausgerichtet mit dem Dominion-Zauberstab. &aTimer&r: Einfacher Zauberturm mit &6Uhr&r im Apparat.",
              "",
              "Der Timer feuert von selbst, ab Werk jede Sekunde. Rechtsklick länger, Schlag kürzer, schleichend in 10-Sekunden-Schritten. Projektil, Berühren, Empfindlich und Redstone-Signal kosten ihn nichts.",
          ],
          tasks=[task_item("ars_nouveau:timer_spell_turret", 1), task_item("ars_nouveau:rotating_spell_turret", 1)],
          rewards=[reward_item("minecraft:clock", 2), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:timer_spell_turret"),

    # ---- Roben und Fäden ------------------------------------------------------------------
    quest("robes", 0, 14.5, "&6Näh die Roben des Arkanisten",
          subtitle="Rüstung, die Mana schenkt.",
          description=[
              "Im Apparat: ein &6Eisen-Rüstungsteil&r in die Mitte, &e4 Magieblütenfasern&r auf die Podeste. Aus &6Diamant&r werden die Teile des &6Kampfmagiers&r.",
              "",
              "Alle Roben geben Mana-Regeneration. Der Kampfmagier schützt mehr, der Arkanist hat bessere Fadenplätze. Die Quellgeborene darf beide tragen.",
          ],
          tasks=[task_item("ars_nouveau:arcanist_robes", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 8), reward_xp(5)],
          deps=["stahlwerk"], icon="ars_nouveau:arcanist_robes"),

    quest("armor_upgrade", 2.5, 14.5, "&6Werte ein Rüstungsteil auf",
          subtitle="Stufe 2 der Robe: 2 Lohenruten, 2 500 Quelle.",
          description=[
              "Im Apparat: Robenteil in die Mitte, &e2 Lohenruten&r auf die Podeste, &d2 500 Quelle&r.",
              "",
              "Jede Stufe hebt die Mana-Regeneration und gibt mehr und größere Fadenplätze. Die dritte Stufe braucht Chorusfrüchte und kommt mit Stufe 4.",
          ],
          tasks=[task_checkmark("Ein Robenteil auf Stufe 2 gebracht")],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_xp(5)],
          deps=["robes"], icon="minecraft:blaze_rod"),

    quest("alteration", 5, 14.5, "&aBau einen Änderungstisch",
          subtitle="Fäden in die Robe nähen.",
          description=[
              "&6Änderungstisch&r: Tisch des Schreibers mit &e4 Magieblütenfasern&r im Kreuz. &6Leerer Faden&r: oben und unten je 3 Fasern, Mitte 3 Goldnuggets.",
              "",
              "Robe auf den Ständer, Faden auf die Tafel, Robe abnehmen. Gleiche Fäden auf zwei Teilen bringen nichts.",
          ],
          tasks=[task_item("ars_nouveau:alteration_table", 1), task_item("ars_nouveau:blank_thread", 2)],
          rewards=[reward_item("minecraft:gold_nugget", 18), reward_xp(4)],
          deps=["armor_upgrade"], icon="ars_nouveau:alteration_table"),

    quest("threads_fight", 7.5, 13.5, "&6Näh Fäden für den Kampf",
          subtitle="Checkliste: alle Fäden kommen aus dem Apparat.",
          description=[
              "&6Zauberkraft&r (alle 7 Essenzen, Magebloom): mehr Zauberschaden je Stufe.",
              "&6Lebensentzug&r (Mendosteen, Sculk-Katalysator, 2 Abschwörungsessenzen): 20 Prozent des Zauberschadens heilt dich.",
              "&6Anzündholz&r (Magmacreme, Feueressenz, Feuerkugel) und &6Chillen&r (Blaues Eis, 2 Wasseressenzen, Pulverschneeeimer): Brennen oder Frieren vor jedem Treffer.",
              "&6Abwehr&r (8 Magieblütenfasern): weniger Magieschaden.",
          ],
          tasks=[task_item("ars_nouveau:thread_spellpower", 1), task_item("ars_nouveau:thread_life_drain", 1),
                 task_item("ars_nouveau:thread_kindling", 1), task_item("ars_nouveau:thread_warding", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 2), reward_xp(6)],
          deps=["alteration"], icon="ars_nouveau:thread_spellpower", optional=True),

    quest("threads_daily", 7.5, 15.5, "&6Näh Fäden für den Alltag",
          subtitle="Checkliste: Mana, Reparatur, Bewegung.",
          description=[
              "&6Magische Kapazität&r (3 Quellbeeren, 3 Magebloom): &e+10&r Prozent Mana je Stufe.",
              "&6Reparieren&r (Amboss, 2 Manipulationsessenzen): repariert alle Magierausrüstung mit Mana.",
              "&6Feder&r (4 Federn, 2 Abschwörungsessenzen): weniger Fallschaden. &6Hoher Schritt&r (3 Luftessenzen): ein Block mehr Stufenhöhe.",
              "Die Helfer-Fäden aus je 3 Scherben: &6Sternbunkel&r 20 Prozent schneller, &6Wirbelzweig&r mehr Sättigung, &6Wixie&r längere Tränke, &6Drygmy&r mehr Beute.",
          ],
          tasks=[task_item("ars_nouveau:thread_magic_capacity", 1), task_item("ars_nouveau:thread_repairing", 1),
                 task_item("ars_nouveau:thread_feather", 1), task_item("ars_nouveau:thread_starbuncle", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 16), reward_xp(6)],
          deps=["alteration"], icon="ars_nouveau:thread_magic_capacity", optional=True),

    # ---- Für die Techniker --------------------------------------------------------------
    quest("charged_certus", 0, 19, "&bLade Certus-Quarz",
          subtitle="Kronwerke: das ME-Netz braucht einen Magier.",
          description=[
              "&eRezept auf Kronwerke:&r &bCertus-Quarzkristall&r in die Kammer, &eRedstone&r und &eGlowstonestaub&r auf die Podeste, &d2 000 Quelle&r. Ein geladener Kristall.",
              "",
              img("ae2:textures/item/certus_quartz_crystal_charged.png", 32, 32),
              "",
              "Ohne geladenen Certus kein Fluix und kein ME-Netz. Die Energizing Orb von Powah macht später zwei pro Durchgang, aber den Anfang macht die Kammer. Mehrere Kammern am Relais-Netz und ein Trichter machen dich zum wichtigsten Lieferanten.",
          ],
          tasks=[task_item("ae2:charged_certus_quartz_crystal", 16)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 16), reward_table("s3_uncommon")],
          deps=["stahlwerk"], icon="ae2:charged_certus_quartz_crystal", size=1.25),

    quest("mark_technomancy", 2.5, 19, "&6Präg Male der Technomantie",
          subtitle="Ars Technica: ein Tribut, fünf Male für Technik-Roben.",
          description=[
              "Im Apparat: &5Wilden-Tribut&r in die Mitte, &6Präzisionsmechanismus&r, &6Calibrated Precision Mechanism&r, &6Manipulationsessenz&r, Eisen, Kupfer, Zink, Messing- und Goldblech auf die Podeste, &d10 000 Quelle&r. Ergibt &e5 Male&r.",
              "",
              "Mit Mal, Netherit und Messing werden Roben der dritten Stufe zu Technomancer, Machinaguard oder Artificer. Die dritte Stufe gibt es erst mit Stufe 4, sammle die Male jetzt.",
          ],
          tasks=[task_item("ars_technica:mark_of_technomancy", 1)],
          rewards=[reward_item("create:brass_ingot", 8), reward_xp(5)],
          deps=["tribute", "charged_certus"], icon="ars_technica:mark_of_technomancy", optional=True),
    # ---- Neu: Nebenquests -------------------------------------------------------------
    quest("ring_greater", 7.5, 3.5, "&6Schmied den Ring des größeren Rabatts",
          subtitle="Noch billigere Zauber für das große Buch.",
          description=[
              "Im Apparat: &6Ring des geringeren Rabatts&r in die Mitte, &e4 Diamanten&r, &e2 Lohenruten&r und &e2 Quelljuwelen&r auf die Podeste.",
              "",
              "Der große Ring senkt die Kosten jedes Zaubers noch etwas mehr als der kleine. Mit den langen Zaubern des Erzmagier-Buchs merkst du das bei jedem Wirken.",
          ],
          tasks=[task_item("ars_nouveau:ring_of_greater_discount", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["archmage_book"], icon="ars_nouveau:ring_of_greater_discount", optional=True),

    quest("source_spawner", 2.5, 5, "&6Bau einen Source Spawner",
          subtitle="Ars Additions: ein Spawner, der mit Quelle läuft.",
          description=[
              "Im Apparat: &6Drygmy-Charme&r in die Mitte, &6Fokus der Beschwörung&r und &6Beschwörungsessenz&r auf die Podeste.",
              "",
              "Der Spawner schaut in die &6Eindämmungsgläser&r in seiner Nähe und erzeugt dieselben Wesen. Jedes Wesen kostet Quelle aus Gläsern daneben, je nach Art unterschiedlich viel.",
              "",
              "Ein Redstone-Signal schaltet ihn ab, ein Komparator liest seinen Fortschritt.",
          ],
          tasks=[task_item("ars_additions:source_spawner", 1)],
          rewards=[reward_item("ars_nouveau:conjuration_essence", 2), reward_table("s3_common")],
          deps=["summon_focus"], icon="ars_additions:source_spawner", optional=True),

    quest("reliquary", 12.5, 6, "&6Füll ein Unstable Reliquary",
          subtitle="Ars Additions: das Ziel für Mark und Recall.",
          description=[
              "Im Apparat: &6Eindämmungsglas&r in die Mitte, &6Beschwörungsessenz&r, &6Manipulationsessenz&r und &6Enderperle&r auf die Podeste.",
              "",
              "Halt das Reliquary in der Zweithand und wirk einen Zauber mit &dMark&r: es merkt sich das Wesen oder den Ort. Ein Zauber mit &dRecall&r wirkt dann genau dort, egal wo du stehst.",
          ],
          tasks=[task_item("ars_additions:unstable_reliquary", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["additions_t3"], icon="ars_additions:unstable_reliquary", optional=True),

    quest("storage_lectern", 10, 8.5, "&aBau ein Aufbewahrungspult",
          subtitle="Alle Truhen in einem Fenster.",
          description=[
              "Im Apparat: &6Pult&r in die Mitte, &e4 Truhen&r auf die Podeste.",
              "",
              "Dominion-Zauberstab: erst die Truhe, dann das Pult. Am Pult siehst du alle verbundenen Inventare zusammen, nimmst heraus und craftest direkt aus ihnen. Inventare dürfen bis &e30 Blöcke&r entfernt sein.",
              "",
              "Wie viele Inventare passen, bestimmen die &dBücherwürmer&r: jeder Bücherwurm-Charme auf das Pult erlaubt &e8&r mehr. Eine unverbundene Truhe direkt am Pult wird zum Eingang, alles darin wandert ins Lager.",
          ],
          tasks=[task_item("ars_nouveau:storage_lectern", 1)],
          rewards=[reward_item("minecraft:chest", 4), reward_xp(5)],
          deps=["golem_bookwyrm"], icon="ars_nouveau:storage_lectern"),

    quest("repository", 12.5, 8.5, "&aBau Repositories und einen Katalog",
          subtitle="Das Lager, das zum Pult passt.",
          description=[
              "&6Repository&r: &e4 Archwood-Stämme&r im Kreuz, &e4 Goldnuggets&r in den Ecken, die Mitte frei. &6Repository Catalog&r: formlos Repository und Magieblütenfaser.",
              "",
              "Ein Repository fasst so viel wie eine Doppeltruhe und behält beim Abbauen seinen Namen. Benannte Inventare bekommen im Pult einen eigenen &eReiter&r.",
              "",
              "Der Katalog verwaltet eine Kette aneinander gesetzter Repositories wie ein einziges Inventar und ist dabei sparsam für den Server. Für große Lager ist er besser als viele einzelne Truhen am Pult.",
          ],
          tasks=[task_item("ars_nouveau:repository", 4), task_item("ars_nouveau:repository_controller", 1)],
          rewards=[reward_item("ars_nouveau:archwood_planks", 32), reward_xp(5)],
          deps=["storage_lectern"], icon="ars_nouveau:repository", optional=True),

    quest("el_turret", 10, 10.5, "&aBau einen Elementar-Turm",
          subtitle="Ars Elemental: der große Fokus im Turm.",
          description=[
              "In der Imbuement-Kammer: &6Verzauberter Zauberturm&r hinein, &e3 Essenzen&r eines Elements und der passende &6große Fokus&r auf die Podeste, &d5 000 Quelle&r.",
              "",
              "Der Turm löst die Kombos seines Fokus aus, und Zauber mit einer Glyphe seiner Schule kosten ihn &e65 Prozent&r weniger Quelle. Ein &dFlashjack&r kann ihn kapern und damit selbst auf Gegner zielen.",
          ],
          tasks=[task_item("ars_elemental:fire_turret", 1)],
          rewards=[reward_item("ars_nouveau:fire_essence", 3), reward_xp(6)],
          deps=["turrets", "major_focus"], icon="ars_elemental:fire_turret", optional=True),

    quest("threads_travel", 10, 15.5, "&6Näh Fäden für Reisen",
          subtitle="Checkliste: tauchen, springen, stehen bleiben.",
          description=[
              "&6Tiefe&r (3 Fische, Kugelfisch, 2 Wasseressenzen): unter Wasser geht dir die Luft viel langsamer aus. In einem Platz der Stufe 3 gar nicht mehr, und du schwimmst schneller.",
              "&6Höhen&r (Spinnenauge, 3 Kaninchenfelle, 2 Luftessenzen): höher springen, tiefer fallen ohne Schaden.",
              "&6Amethyst-Golem&r (3 Obsidian): &e15 Prozent&r Rückstoßresistenz je Stufe.",
              "&6Reach&r von Ars Additions (3 Alakarkinos-Token, 3 Manipulationsessenzen): &e+1&r Reichweite für Blöcke und Wesen je Stufe.",
          ],
          tasks=[task_item("ars_nouveau:thread_depths", 1), task_item("ars_nouveau:thread_heights", 1),
                 task_item("ars_nouveau:thread_amethyst_golem", 1), task_item("ars_additions:thread_reach", 1)],
          rewards=[reward_item("ars_nouveau:magebloom_fiber", 16), reward_xp(6)],
          deps=["alteration"], icon="ars_nouveau:thread_depths", optional=True),

    quest("threads_elemental", 10, 13.5, "&6Näh Fäden der Elemente",
          subtitle="Checkliste: Feuer, Sporen, Blitz und Beschwörung.",
          description=[
              "&6Selbstverbrennung&r (3 Feueressenzen): brennst du beim Zaubern, erlischt das Feuer und du bekommst Selbstverbrennung. Feuerzauber machen dann mehr Schaden und halten länger.",
              "&6Spores&r (Ars Elemental: 2 Erdessenzen, Sporenblüte, Spinnenauge): Schadenszauber vergiften das Ziel oder machen es hungrig.",
              "&6Shocking&r (2 Luftessenzen, Blitzableiter, Flashpine): Schadenszauber schocken das Ziel kurz vorher.",
              "&6Summoning&r (2 Beschwörungsessenzen, Echoscherbe, 2 Wilden-Teile): &e10 Prozent&r weniger Beschwörungskrankheit je Stufe, ab Stufe 2 stärkere Beschwörungen.",
          ],
          tasks=[task_item("ars_nouveau:thread_immolation", 1), task_item("ars_elemental:thread_spore", 1),
                 task_item("ars_elemental:thread_shock", 1), task_item("ars_elemental:thread_summon", 1)],
          rewards=[reward_item("ars_nouveau:fire_essence", 2), reward_xp(6)],
          deps=["alteration"], icon="ars_nouveau:thread_immolation", optional=True),

    quest("prism_lenses", 17.5, 3, "&dSchleif Linsen für das Prisma",
          subtitle="Ars Elemental: Prismen, die Zauber umbauen.",
          description=[
              "Linsen kommen auf das &6Fortgeschrittene Prisma&r und ändern, was es mit Projektilen macht. Die meisten entstehen in der Imbuement-Kammer: &6Quarz&r hinein, &6Manipulationsessenz&r und eine Glyphe auf die Podeste, &d2 000 Quelle&r. Die Glyphe bleibt dabei liegen.",
              "",
              "&eZielsuche&r (Zielsuchendes Projektil) und &eBogen&r (Arc Projectile) machen das Projektil zielsuchend oder bogenförmig. &eBeschleunigen&r und &eVerlangsamen&r ändern sein Tempo, &eDurchschlag&r gibt ihm Durchschlag gegen Quelle.",
              "",
              "Die &6Chaining Prism Lens&r (Apparat: Quarz, Manipulationsessenz, Quelljuwelblock, Leeres Pergament) wird am Tisch beschrieben und hängt ihre Glyphen an jedes Projektil, das durchfliegt. Das kostet Quelle je nach Zauber.",
          ],
          tasks=[task_item("ars_elemental:homing_prism_lens", 1), task_item("ars_elemental:chaining_prism_lens", 1)],
          rewards=[reward_item("minecraft:quartz", 16), reward_xp(5)],
          deps=["el_homing"], icon="ars_elemental:homing_prism_lens", optional=True),

    quest("ruined_portal", 2.5, 11.5, "&aFinde ein verfallenes Warp-Portal",
          subtitle="Ars Additions: ein altes Tor mit Fahrkarte.",
          description=[
              "Verfallene Warp-Portale stehen dort, wo auch normale Ruinenportale vorkommen. Neben dem Portal steht eine Truhe mit Quellstein, Kodex-Seiten und einer &6Explorer's Warp Scroll&r.",
              "",
              "Die Schriftrolle sucht sich ein Ziel in der Nähe: einen Tempel, eine Festung, eine Antike Stätte, einen Wilden-Bau, einen Nexus-Turm oder eine Arkane Bibliothek. Ist der Rahmen beschädigt, setz ihn wieder instand. Dann wirf die Rolle hinein, und das Portal öffnet sich ohne Quelle.",
              "",
              "Die &6Codex Entry&r aus der Truhe bringt dir beim Benutzen eine zufällige Glyphe bei.",
          ],
          tasks=[task_item("ars_additions:exploration_warp_scroll", 1)],
          rewards=[reward_item("ars_nouveau:sourcestone", 16), reward_table("s3_common")],
          deps=["islands_warping"], icon="ars_additions:exploration_warp_scroll", optional=True),

]

images = [
    banner("ars_master/title", "Ars Nouveau: Meister", 9, -4.4, height=1.8, kind="title", colour="magic"),
    head("chimaere", "Die Chimäre", 0, -2.2, colour="fire"),
    banner("ars_master/glyphen", "Glyphen der Stufe 3", 12.5, -2.4, height=0.9, colour="magic"),
    head("stahlwerk", "Neu im Stahlwerk", 0, 7.0, colour="nature"),
    head("roben", "Roben und Fäden", 0, 12.4, colour="brass"),
    head("technik", "Für die Techniker", 0, 17.4, colour="water"),
]

chapter(C, "Ars Nouveau: Meister", "ars_nouveau:archmage_spell_book", "magic", quests, shape="circle", order=25,
        stage=3, subtitle=["Stufe 3. Die Chimäre, das Erzmagier-Buch, Glyphen der Stufe 3, Rituale und Roben."],
        images=images)
