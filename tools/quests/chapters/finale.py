"""The season finale in stage 5: the goal "Der Chaoswächter" one pillar item per quest (Gaia
ingot, awakened draconium, antimatter pellet, Wilden tribute), the 98 percent hold, getting
ready for the Chaos Guardian (gear checklist, supplies, voice group, what the fight looks like,
from Draconic Evolution's config and entity data), the trip to the Chaos Island (the team
brings everyone there by hand, there is no teleport), the fight live on every stream, the
chaos shards and the last quest of the season."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_kill, task_dimension, reward_item, reward_table,
                  reward_xp, banner)

C = "finale"


def head(name, text, left, y, height=0.9, kind="section", colour="end"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Das letzte Ziel -----------------------------------------------------------------
    quest("start", 0, 1.5, "&5&lSchmiede einen Gaia-Geistbarren",
          subtitle="Der Barren, den beide Säulen brauchen.",
          description=[
              "Ein &6Terrastahlbarren&r in die Mitte, &a4 Gaia-Geister&r oben, unten, links und rechts. Heraus kommt ein &aGaia-Geistbarren&r.",
              "",
              "Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r. Es öffnet keine Stufe mehr, es will die Dinge, die den Endkampf möglich machen:",
              "&6Technik:&r &e64 Erwachte Draconiumblöcke&r (fest) und &e100 Antimaterie-Pellets&r.",
              "&dMagie:&r &e128 Gaia-Geistbarren&r und &e64 Wilden-Tribute&r (fest).",
              "",
              "Der Gaia-Geistbarren ist das Bindeglied: Die Magier geben ihn ab, die Techniker brauchen ihn für jede Fusion von Erwachtem Draconium.",
          ],
          tasks=[task_item("botania:gaia_ingot", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          icon="botania:gaia_ingot", size=2.0, shape="hexagon"),

    # ---- Technik -------------------------------------------------------------------------
    quest("tech", 2.75, -0.5, "&6Fusioniere Erwachtes Draconium",
          subtitle="Vier Blöcke aus einer Fusion.",
          description=[
              "&e4 Draconiumblöcke&r in den Fusionskern, in die sieben Wyvern-Injektoren &e4 Draconiumkerne&r, &a2 Gaia-Geistbarren&r und &c1 Drachenherz&r. Ergebnis: &54 Erwachte Draconiumblöcke&r für 50 Millionen OP.",
              "",
              "Für 64 Blöcke sind das &e16 Fusionen&r, also 16 Drachenherzen und 32 Gaia-Geistbarren. Jeder Block zählt am Obelisken 50 Punkte.",
              "",
              "Alles zur Fusion im Kapitel &5Draconic: Erwacht und Chaos&r.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 4)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["start"], icon="draconicevolution:awakened_draconium_block"),

    quest("t_pellet", 5.25, -0.5, "&6Kristallisiere ein Antimaterie-Pellet",
          subtitle="1 000 mB Antimaterie, ein Pellet.",
          description=[
              "Das &6SPS&r macht aus &e1 000 mB Polonium&r &e1 mB Antimaterie&r. Der &6Chemische Kristallisator&r macht aus 1 000 mB Antimaterie ein &5Pellet&r.",
              "",
              "Ein Pellet braucht also eine Million mB Polonium. Hundert davon will der Obelisk, jedes zählt 30 Punkte. Das heißt: mehrere Spaltreaktoren und Strom aus allem, was ihr habt.",
              "",
              "Alles dazu im Kapitel &5Mekanism: Antimaterie&r.",
          ],
          tasks=[task_item("mekanism:pellet_antimatter", 1)],
          rewards=[reward_table("s5_common"), reward_xp(15)],
          deps=["tech"], icon="mekanism:pellet_antimatter"),

    # ---- Magie ---------------------------------------------------------------------------
    quest("magic", 2.75, 3.5, "&dPlant die Gaia-Kämpfe",
          subtitle="Rund 640 Geister, das sind viele Abende.",
          description=[
              "Verabredet feste Abende für Kämpfe gegen die &aGaia-Wächterin&r. Jeder Spieler im Kampf bekommt &e6 Gaia-Geister&r, wer den letzten Treffer landet, &e8&r.",
              "",
              "Die Rechnung: 128 Barren für den Obelisken und 32 für die Fusionen sind 160 Barren, also &e640 Gaia-Geister&r. Mit vier Leuten pro Kampf sind das gut 25 Kämpfe.",
              "",
              "Jeder abgegebene Barren zählt 25 Punkte. Die Kämpfe stehen im Kapitel &aBotania: Gaia&r.",
          ],
          tasks=[task_item("botania:gaia_ingot", 8)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["start"], icon="botania:gaia_spirit"),

    quest("m_tribute", 5.25, 3.5, "&dBezwinge eine Wilden-Chimäre",
          subtitle="Ein Kampf, ein Tribut.",
          description=[
              "Ritual &6Beschwöre Wilden&r am Kohlenbecken auf einem freien Feld, die &5Wilden-Chimäre&r besiegen, den &5Wilden-Tribut&r aufheben.",
              "",
              "&e64 Tribute&r will der Obelisk, eine feste Zahl, jeder zählt 50 Punkte. Verabredet euch zu zweit oder zu dritt, das geht schneller und sicherer.",
              "",
              "Wie die Chimäre kämpft, steht im Kapitel &dArs Nouveau: Episch&r.",
          ],
          tasks=[task_item("ars_nouveau:wilden_tribute", 1)],
          rewards=[reward_table("s5_common"), reward_xp(15)],
          deps=["magic"], icon="ars_nouveau:wilden_tribute"),

    quest("hold", 8, 1.5, "&cWarte auf den Termin",
          subtitle="Bei 98 Prozent ist Schluss, bis alle da sind.",
          description=[
              "Bei &e98 Prozent&r nimmt der Obelisk nichts mehr an. Dann legt das Team den Termin für das Finale fest, er steht zuerst im &9Discord&r.",
              "",
              "Am Abend des Finales gehen alle Streamer gemeinsam live, die letzten Gegenstände wandern zusammen in den Obelisken, und dann geht es zur Chaosinsel.",
              "",
              "&eTipp:&r Bis dahin hast du Zeit, dich auszurüsten. Die nächsten Quests sagen dir, womit.",
          ],
          tasks=[task_checkmark("Ich bin beim Finale dabei")],
          rewards=[reward_xp(5)],
          deps=["t_pellet", "m_tribute"], icon="minecraft:beacon", size=1.75, shape="gear"),

    # ---- Bereit machen -------------------------------------------------------------------
    quest("gear", 10.75, -0.5, "&dHak deine Ausrüstung ab",
          subtitle="Vier Dinge, ohne die du nicht hinfliegst.",
          description=[
              "&eFlug:&r Elytra oder das Flugmodul in einer Draconic-Brustplatte.",
              "&eSchild:&r eine Brustplatte mit vielen Schildmodulen und Schilderholung.",
              "&eZweites Leben:&r ein Untod-Modul oder Totems der Unsterblichkeit.",
              "&eFernkampf:&r ein starker Bogen mit Schadens- und Geschwindigkeitsmodulen.",
              "",
              "Der Kampf findet in der Luft und über dem Abgrund statt. Der Schild des Wächters hat &e16 000&r Punkte, und Draconic Evolution sagt selbst, dass ein schneller, starker Bogen ihn am besten schmilzt.",
          ],
          tasks=[task_checkmark("Ich kann fliegen"), task_checkmark("Mein Schild ist voll ausgebaut"),
                 task_checkmark("Ich habe ein zweites Leben dabei"), task_checkmark("Mein Bogen ist bereit")],
          rewards=[reward_item("minecraft:firework_rocket", 64), reward_xp(10)],
          deps=["hold"], icon="draconicevolution:draconic_chestpiece"),

    quest("supplies", 13.25, -0.5, "&ePack deine Taschen",
          subtitle="Totems, Essen, ein Dislokator, Blöcke.",
          description=[
              "&e2 Totems&r, wenn du kein Untod-Modul hast. Goldene Karotten. Ein Stapel Blöcke zum Brücken. Ein &6Fortgeschrittener Dislokator&r mit &e16 Enderperlen&r.",
              "",
              "Die Chaosinsel liegt Tausende Blöcke vom Zentrum des End entfernt. Wer stirbt, wacht an seinem Spawnpunkt auf. Speicher die Insel gleich bei der Ankunft im Dislokator, dann bist du schnell zurück.",
          ],
          tasks=[task_item("minecraft:totem_of_undying", 2), task_item("draconicevolution:advanced_dislocator", 1),
                 task_item("minecraft:ender_pearl", 16)],
          rewards=[reward_item("minecraft:golden_carrot", 32), reward_xp(10)],
          deps=["gear"], icon="draconicevolution:advanced_dislocator"),

    quest("g_voice", 13.25, 1.5, "&eTritt der Sprachgruppe bei",
          subtitle="Über die ganze Insel hören, wer was ansagt.",
          description=[
              "&eV&r öffnet das Menü von Simple Voice Chat. Tritt der &eGruppe&r bei, die das Team für das Finale anlegt. In einer Gruppe hörst du die anderen über jede Entfernung.",
              "",
              "Ohne Gruppe reicht deine Stimme nur 48 Blöcke, und die Insel ist viel größer. Prüf vorher, ob dein Mikrofon stumm ist (oft die Taste &eM&r, siehe &6Tipps und Tricks&r).",
          ],
          tasks=[task_checkmark("Ich bin in der Gruppe")],
          rewards=[reward_xp(5)],
          deps=["hold"], icon="minecraft:note_block"),

    quest("fight_info", 10.75, 3.5, "&cLies, was dich erwartet",
          subtitle="Der Kampf, wie Draconic Evolution ihn baut.",
          description=[
              "Erst die &5Wächterkristalle&r, dann sein Schild mit &e16 000&r Punkten, dann &e1 000&r Lebenspunkte. Die Leiste oben zeigt, wie viele Kristalle noch stehen und wie viel Schild er hat.",
              "",
              "&eDie Kristalle:&r Ihr Schild hält normalen Waffen stand. Er wird nur instabil, wenn der Wächter selbst den Kristall trifft, dann bleibt er etwa &e10 Sekunden&r offen.",
              "",
              "&eSeine Angriffe:&r Sturzflug, Laserstrahl, Bomben aus der Luft, Schockwellen, aufgeladene Angriffe. Dazu können &5Wächter-Wither&r erscheinen. Bleib in Bewegung und steh nicht mit anderen auf einem Haufen.",
          ],
          tasks=[task_checkmark("Gelesen und verstanden")],
          rewards=[reward_xp(5)],
          deps=["hold"], icon="minecraft:end_crystal"),

    # ---- Der Kampf -----------------------------------------------------------------------
    quest("trip", 16, 1.5, "&5Komm mit zur Insel",
          subtitle="Alle zusammen, auf ein Zeichen.",
          description=[
              "Sei zur Startzeit am &eTreffpunkt&r, den das Team im Discord ansagt, mit der Ausrüstung im Inventar. Das Team führt euch selbst zur &5Chaosinsel&r, es gibt keinen Teleport am Obelisken.",
              "",
              "Die Insel hat rund 160 Blöcke Radius, der Chaoskristall steht in der Mitte auf Höhe 80. Speicher sie sofort im Dislokator.",
              "",
              "&cBitte:&r Flieg nicht vorher allein hin. Der Kampf startet, sobald jemand ankommt, und er gehört allen.",
          ],
          tasks=[task_dimension("minecraft:the_end")],
          rewards=[reward_xp(10)],
          deps=["supplies", "g_voice", "fight_info"], icon="minecraft:end_portal_frame", size=1.5),

    quest("f_crystals", 18.75, 0, "&5Knackt die Wächterkristalle",
          subtitle="Lockt seine Angriffe auf einen Kristall, dann zuschlagen.",
          description=[
              "Stell dich so, dass der Wächter beim Angriff auf dich einen &5Wächterkristall&r trifft. Ist dessen Schild instabil, habt ihr &e10 Sekunden&r: alle auf diesen Kristall.",
              "",
              "Sagt im Sprachkanal an, welcher Kristall offen ist. Solange einer steht, kommt ihr an den Schild des Wächters nicht heran.",
          ],
          tasks=[task_checkmark("Alle Kristalle sind zerstört")],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["trip"], icon="minecraft:end_crystal"),

    quest("fight", 18.75, 3, "&4&lBesiegt den Chaoswächter",
          subtitle="Live auf jedem Stream.",
          description=[
              "Schild herunterschießen, dann die letzten &e1 000&r Lebenspunkte. Wer stirbt, kommt per Dislokator zurück. Bleibt zusammen, bis er fällt.",
              "",
              "Alle Streamer sind live, jeder sieht den Kampf aus seiner eigenen Sicht. Den letzten Treffer landet nur einer, darum hakst du diese Quest selbst ab, wenn der Wächter tot ist und du dabei warst.",
          ],
          tasks=[task_checkmark("Der Chaoswächter ist besiegt, und ich war dabei")],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["f_crystals"], icon="draconicevolution:chaos_shard", size=2.5, shape="gear"),

    quest("last_hit", 18.75, 6, "&4Lande den letzten Treffer",
          subtitle="Nur einer bekommt ihn.",
          description=[
              "Für den, der den Chaoswächter tatsächlich erlegt. Alle anderen dürfen diese Quest getrost leer lassen.",
          ],
          tasks=[task_kill("draconicevolution:draconic_guardian", 1)],
          rewards=[reward_xp(10)],
          deps=["trip"], icon="minecraft:dragon_head", optional=True),

    quest("f_shards", 21.5, 5, "&8Bau den Chaoskristall ab",
          subtitle="Fünf Chaosscherben, erst nach dem Sieg.",
          description=[
              "Ist der Wächter tot, lässt sich der &5Chaoskristall&r in der Mitte der Insel abbauen. Er gibt &e5 Chaosscherben&r, der Wächter selbst ein Drachenherz.",
              "",
              "Was man aus den Scherben baut, steht im Kapitel &5Draconic: Erwacht und Chaos&r. Wer daraus etwas baut, schreibt das letzte Kapitel dieser Welt.",
          ],
          tasks=[task_item("draconicevolution:chaos_shard", 1)],
          rewards=[reward_xp(15)],
          deps=["fight"], icon="draconicevolution:chaos_shard", optional=True),

    quest("end", 23, 3, "&5&lFeiert das Ende der Season",
          subtitle="Danke fürs Mitspielen.",
          description=[
              "Der Chaoswächter ist tot, und mit ihm endet &6Kronwerke Season 2&r. Das Feuerwerk steigt.",
              "",
              "Von Bruchstein und Wasserrädern bis zur Antimaterie und dem Chaos: Das habt ihr zusammen gebaut. Danke an alle, die mitgespielt, zugeschaut und geholfen haben.",
          ],
          tasks=[task_checkmark("Die Season ist geschafft")],
          rewards=[reward_table("s5_rare"), reward_xp(50)],
          deps=["fight"], icon="minecraft:dragon_egg", size=3.0, shape="hexagon"),
]

images = [
    head("title", "Das Finale", -1, -4.4, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", -1, -3.1, height=0.55, kind="note", colour="stone"),
    head("goal", "Das letzte Ziel", 2.3, -1.9, colour="brass"),
    head("ready", "Bereit machen", 10.1, -1.9, colour="magic"),
    head("fight", "Der Kampf", 15.6, -1.9, colour="fire"),
]

chapter(C, "Das Finale", "draconicevolution:chaos_shard", "start", quests, shape="circle", order=44, stage=5,
        subtitle=["Stufe 5: das letzte Ziel, der Chaoswächter und das Ende der Season."],
        images=images)
