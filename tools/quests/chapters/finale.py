"""The season finale in stage 5: the goal "Der Chaoswächter" with its four items, the 98 percent
hold and the final event, getting ready for the Chaos Guardian (gear checklist and what the fight
looks like, from Draconic Evolution's config and entity data), the trip to the Chaos Island
(the team brings everyone there by hand), the fight live on every stream, and the last quest of the season."""
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
    quest("start", 0, 1.5, "&5&lDas Finale",
          subtitle="Der letzte Obelisk, der letzte Kampf.",
          description=[
              "Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r. Diesmal schaltet der Obelisk keine neue Stufe frei. Er will die Dinge, die den Endkampf möglich machen, und danach kommt der Kampf selbst.",
              "",
              "&eTechnik:&r &e64 Erwachte Draconiumblöcke&r (fest) und &e100 Antimaterie-Pellets&r.",
              "&eMagie:&r &e128 Gaia-Geistbarren&r und &e64 Wilden-Tribute&r (fest).",
              "",
              "Der Gaia-Geistbarren ist das Bindeglied: Die Magier brauchen ihn für ihren Pfeiler, die Techniker für jede Fusion von Erwachtem Draconium. Ein Barren ist ein Terrastahlbarren mit 4 Gaia-Geistern drumherum.",
          ],
          tasks=[task_item("botania:gaia_ingot", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          icon="draconicevolution:chaos_shard", size=2.0, shape="hexagon"),

    quest("tech", 2.75, 0, "&6Der Technik-Pfeiler",
          subtitle="Fusion und Antimaterie.",
          description=[
              "&5Erwachtes Draconium&r: 16 Fusionen mit je einem Drachenherz und 2 Gaia-Geistbarren. Alles dazu im Kapitel &5Draconic: Erwacht und Chaos&r.",
              "",
              "&5Antimaterie&r: Spaltreaktor, Polonium, das SPS. Ein Pellet braucht eine Million mB Polonium. Alles dazu im Kapitel &5Mekanism: Antimaterie&r.",
              "",
              "Jeder Block zählt 50 Punkte, jedes Pellet 30.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 1), task_item("mekanism:pellet_antimatter", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["start"], icon="draconicevolution:awakened_draconium_block"),

    quest("magic", 2.75, 3, "&dDer Magie-Pfeiler",
          subtitle="Gaia und die Wilden.",
          description=[
              "&aGaia-Geistbarren&r: 128 Stück, dazu die Barren für die Draconium-Fusionen. Jeder Gaia-Kampf bringt Geister, plant also weitere Kämpfe ein.",
              "",
              "&5Wilden-Tribut&r: 64 Stück, eine feste Zahl. Jeder Tribut ist ein Kampf gegen die &5Wilden-Chimäre&r aus dem Ritual Beschwöre Wilden. Verabredet euch zu zweit oder zu dritt, das geht schneller und sicherer.",
              "",
              "Jeder Barren zählt 25 Punkte, jeder Tribut 50.",
          ],
          tasks=[task_item("botania:gaia_ingot", 4), task_item("ars_nouveau:wilden_tribute", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["start"], icon="ars_nouveau:wilden_tribute"),

    quest("hold", 5.5, 1.5, "&c98 Prozent",
          subtitle="Das letzte Stück machen alle zusammen.",
          description=[
              "Wie bei jeder Stufe hält der Obelisk bei &e98 Prozent&r an und nimmt nichts mehr an. Dann wird der Termin für das Finale festgelegt. Er steht zuerst im Discord.",
              "",
              "Am Abend des Finales gehen alle Streamer gemeinsam live. Die letzten Gegenstände wandern zusammen in den Obelisken, und dann bringt das Team alle auf die Chaosinsel.",
              "",
              "&eTipp:&r Bis dahin hast du Zeit, dich auszurüsten. Die nächsten Quests sagen dir, womit.",
          ],
          tasks=[task_checkmark("Ich bin beim Finale dabei")],
          rewards=[reward_xp(5)],
          deps=["tech", "magic"], icon="minecraft:beacon", size=1.75, shape="gear"),

    # ---- Bereit machen -------------------------------------------------------------------
    quest("gear", 8.25, 0, "&dDie Ausrüstung",
          subtitle="Eine Liste, die du abhaken solltest.",
          description=[
              "Der Kampf findet in der Luft und über dem Abgrund statt. Was du brauchst:",
              "",
              "&eFlug:&r Elytra oder das Flugmodul in einer Draconic-Brustplatte. Ohne Flug erreichst du den Wächter kaum.",
              "&eSchild:&r Eine Brustplatte mit vielen Schildmodulen, dazu Schilderholung. Der Schild schluckt die Treffer, bevor sie dich erreichen.",
              "&eZweites Leben:&r ein Untod-Modul oder Totems der Unsterblichkeit.",
              "&eFernkampf:&r ein starker Bogen mit Schadens- und Geschwindigkeitsmodulen. Der Schild des Wächters hat 16 000 Punkte, und Draconic Evolution sagt selbst, dass ein schneller, starker Bogen ihn am besten schmilzt.",
          ],
          tasks=[task_checkmark("Ich kann fliegen"), task_checkmark("Mein Schild ist voll ausgebaut"),
                 task_checkmark("Ich habe ein zweites Leben dabei"), task_checkmark("Mein Bogen ist bereit")],
          rewards=[reward_item("minecraft:firework_rocket", 64), reward_xp(10)],
          deps=["hold"], icon="draconicevolution:draconic_chestpiece"),

    quest("supplies", 11, 0, "&eVorräte",
          subtitle="Was in die Taschen gehört.",
          description=[
              "&eTotems&r: Wer kein Untod-Modul hat, nimmt mehrere mit.",
              "&eEssen&r: Goldene Karotten oder was dich am längsten satt hält.",
              "&eRückweg&r: Die Chaosinsel liegt Tausende Blöcke vom Zentrum des End entfernt. Wer stirbt, wacht an seinem Spawnpunkt auf. Speicher dir die Insel in einem &eFortgeschrittenen Dislokator&r, dann bist du schnell zurück. Er läuft mit Enderperlen.",
              "&eBlöcke&r: ein Stapel zum Brücken und Abdecken.",
          ],
          tasks=[task_item("minecraft:totem_of_undying", 2), task_item("draconicevolution:advanced_dislocator", 1),
                 task_item("minecraft:ender_pearl", 16)],
          rewards=[reward_item("minecraft:golden_carrot", 32), reward_xp(10)],
          deps=["gear"], icon="draconicevolution:advanced_dislocator"),

    quest("fight_info", 8.25, 3, "&cWas dich erwartet",
          subtitle="Der Kampf, wie Draconic Evolution ihn baut.",
          description=[
              "&eDie Insel:&r In der Mitte steht der &5Chaoskristall&r, rundherum schweben die &5Wächterkristalle&r. Der Kampf beginnt, sobald ein Spieler ankommt.",
              "",
              "&eErst die Kristalle:&r Solange Wächterkristalle stehen, kommst du nicht an den Schild des Wächters heran. Der Schild der Kristalle hält normalen Waffen stand. Er wird nur instabil, wenn der Wächter selbst den Kristall trifft, dann bleibt er etwa &e10 Sekunden&r offen. Lockt also seine Angriffe auf einen Kristall und schlagt dann zu.",
              "",
              "&eDann der Wächter:&r Erst sein Schild mit &e16 000&r Punkten, dann &e1 000&r Lebenspunkte. Die Leiste oben zeigt, wie viele Kristalle noch stehen und wie viel Schild er hat.",
              "",
              "&eSeine Angriffe:&r Er stürzt sich auf Spieler, feuert einen Laserstrahl, bombardiert aus der Luft mit Geschossen, löst Schockwellen aus und lädt sich für stärkere Angriffe auf. Dazu können &5Wächter-Wither&r erscheinen. Bleib in Bewegung und steh nicht mit anderen auf einem Haufen.",
          ],
          tasks=[task_checkmark("Gelesen und verstanden")],
          rewards=[reward_xp(5)],
          deps=["hold"], icon="minecraft:end_crystal"),

    # ---- Der Kampf -----------------------------------------------------------------------
    quest("trip", 13.75, 1.5, "&5Die Reise zur Insel",
          subtitle="Alle zusammen, auf ein Zeichen.",
          description=[
              "Wenn das Event am Abend des Finales beginnt, bringt das Team alle Spieler gemeinsam auf die &5Chaosinsel&r. Niemand muss sie vorher suchen, und niemand ist früher dort als die anderen. Sei pünktlich online und halte deine Ausrüstung im Inventar bereit.",
              "",
              "Die Insel ist groß, rund 160 Blöcke im Radius, mit dem Chaoskristall auf Höhe 80 in ihrer Mitte. Wenn du ankommst, speichere sie sofort im Dislokator.",
              "",
              "&cBitte:&r Flieg nicht vorher allein hin. Der Kampf startet, sobald jemand ankommt, und er gehört allen.",
          ],
          tasks=[task_dimension("minecraft:the_end")],
          rewards=[reward_xp(10)],
          deps=["gear", "fight_info"], icon="minecraft:end_portal_frame", size=1.5),

    quest("fight", 16.5, 1.5, "&4&lDer Chaoswächter",
          subtitle="Live auf jedem Stream.",
          description=[
              "Das ist der Kampf, auf den die ganze Season hinausläuft. Alle Streamer sind live, jeder sieht ihn aus seiner eigenen Sicht.",
              "",
              "&eAblauf:&r Kristalle knacken, während der Wächter auf sie feuert. Dann den Schild herunterschießen, dann die letzten 1 000 Lebenspunkte.",
              "",
              "Wer stirbt, kommt per Dislokator zurück. Gebt einander Deckung, sagt im Sprachkanal an, welcher Kristall offen ist, und bleibt zusammen, bis er fällt.",
              "",
              "Den letzten Treffer landet nur einer. Darum hakst du diese Quest selbst ab, wenn der Wächter tot ist und du dabei warst.",
          ],
          tasks=[task_checkmark("Der Chaoswächter ist besiegt, und ich war dabei")],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["trip"], icon="draconicevolution:chaos_shard", size=2.5, shape="gear"),

    quest("last_hit", 16.5, 4.5, "&4Der letzte Treffer",
          subtitle="Nur einer bekommt ihn.",
          description=[
              "Für den, der den Chaoswächter tatsächlich erlegt. Alle anderen dürfen diese Quest getrost leer lassen.",
          ],
          tasks=[task_kill("draconicevolution:draconic_guardian", 1)],
          rewards=[reward_xp(10)],
          deps=["trip"], icon="minecraft:dragon_head", optional=True),

    quest("end", 20.25, 1.5, "&5&lDas Ende der Season",
          subtitle="Danke fürs Mitspielen.",
          description=[
              "Der Chaoswächter ist tot, und mit ihm endet &6Kronwerke Season 2&r. Das Feuerwerk steigt.",
              "",
              "Auf der Insel bleibt noch etwas: Der &5Chaoskristall&r lässt sich jetzt abbauen und gibt &e5 Chaosscherben&r. Der Wächter selbst hinterlässt ein Drachenherz. Wer daraus etwas baut, schreibt das letzte Kapitel dieser Welt.",
              "",
              "Von Bruchstein und Wasserrädern bis zur Antimaterie und dem Chaos: Das habt ihr zusammen gebaut. Danke an alle, die mitgespielt, zugeschaut und geholfen haben.",
          ],
          tasks=[task_checkmark("Die Season ist geschafft")],
          rewards=[reward_table("s5_rare"), reward_xp(50)],
          deps=["fight"], icon="minecraft:dragon_egg", size=3.0, shape="hexagon"),
]

images = [
    head("title", "Das Finale", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("ready", "Bereit machen", 7.6, -1.4, colour="magic"),
    head("fight", "Der Kampf", 13.2, -1.4, colour="fire"),
]

chapter(C, "Das Finale", "draconicevolution:chaos_shard", "start", quests, shape="circle", order=44, stage=5,
        subtitle=["Stufe 5: das letzte Ziel, der Chaoswächter und das Ende der Season."],
        images=images)
