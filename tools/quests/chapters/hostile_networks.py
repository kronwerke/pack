"""Hostile Neural Networks, stage 2: the deep learner and the model framework, attuning a model
to a mob, the tiers faulty / basic / advanced / superior / self aware with their kill counts
(6, 12, 30, 50 from model_tiers/*.json), and which mobs are worth modelling in this pack.
The simulation chamber, prediction matrix and generalized predictions open in stage 3, the
loot fabricator, end prediction and data center in stage 4; both are described in checkmark
quests only. Numbers come from the HNN 6.5.1 jar (sim_cost in FE/t, 240 ticks per inference,
300 per training run, loot fab 256 FE/t and 60 ticks, data center 25 models at 1.5x cost) and
from config/hostilenetworks.cfg. Kronwerke recipes: kubejs/server_scripts/kronwerke/added.js."""
from ftbq import (chapter, quest, task_item, task_kill, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "hostile_networks"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Daten sammeln ------------------------------------------------------
    quest("deep_learner", 0, 1, "&3&lBau einen Deep Learner",
          subtitle="Eine Mobfarm, die keine Mobs braucht.",
          description=[
              "&eRezept:&r oben &6Obsidian&r, &6Redstone-Verstärker&r, Obsidian. Mitte Verstärker, &6Glasscheibe&r, Verstärker. Unten Obsidian, &6Redstone&r, Obsidian.",
              "",
              "&3Hostile Neural Networks&r baut Monsterdrops am Computer nach. Du tötest einen Mob ein paar Dutzend Mal, der &6Deep Learner&r lernt dabei, wie der Mob funktioniert, und später simuliert eine Maschine den Kampf und wirft die Drops aus. Ohne Spawner, ohne Dunkelheit, ohne Lag.",
              "",
              "&eDer Weg in drei Stufen:&r In &6Stufe 2&r sammelst du Daten, das ist langsam und Handarbeit. In &6Stufe 3&r simuliert die &6Simulationskammer&r mit Strom. In &6Stufe 4&r macht der &6Loot-Fabrikator&r aus den Simulationen echte Gegenstände, und das &6Rechenzentrum&r schafft tausende pro Minute.",
              "",
              "Der Deep Learner ist dein Lehrbuch. Er fasst &e4 Datenmodelle&r und muss beim Töten nur irgendwo im Inventar liegen, in der Zweithand oder im eigenen Curio-Slot.",
          ],
          tasks=[task_item("hostilenetworks:deep_learner", 1)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_table("s2_common")],
          icon="hostilenetworks:deep_learner", size=2.0, shape="hexagon"),

    quest("framework", 2.5, 0, "&7Bau ein Modellgerüst",
          subtitle="Ein leerer Chip, der noch nichts weiß.",
          description=[
              "&eRezept:&r oben &6Tonklumpen&r, &6Redstone-Verstärker&r, Tonklumpen. Mitte &6Redstone&r, &6Glatter Stein&r, Redstone. Unten Tonklumpen, &6Goldbarren&r, Tonklumpen.",
              "",
              pic("hostilenetworks:blank_data_model"),
              "",
              "Das &6Model Framework&r ist ein Datenmodell ohne Mob. Erst wenn du es auf ein Monster richtest, weiß es, was es lernen soll. Bau gleich drei oder vier, du wirst mehr als ein Modell wollen.",
          ],
          tasks=[task_item("hostilenetworks:blank_data_model", 2)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_xp(3)],
          deps=["deep_learner"], icon="hostilenetworks:blank_data_model"),

    quest("learner_gui", 2.5, 2, "&7Lies den Deep Learner",
          subtitle="Was die Anzeige dir sagt.",
          description=[
              "Rechtsklick mit dem &6Deep Learner&r in der Hand öffnet ihn. Links liegen die vier Modellplätze, in der Mitte dreht sich der Mob, rechts steht alles Wichtige: &eModel Tier&r, &eModel Accuracy&r und &eUpgrades to ... in N kills&r.",
              "",
              "Liegt ein Modell im Learner, zeigt dir ein kleines &6HUD&r oben links im Spiel, wie viele Kills bis zur nächsten Stufe fehlen. Du musst den Learner dafür nicht offen haben.",
              "",
              "&cWichtig:&r Es zählt nur, was &edu&r tötest. Schwert, Bogen, Zauber, alles mit deinem Namen dran. Eine Mobfarm, die ohne dich tötet, bringt dem Modell nichts.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["deep_learner"], icon="minecraft:spyglass"),

    quest("attune", 5, 1, "&a&lRichte das Gerüst auf einen Mob",
          subtitle="Rechtsklick, und der Chip kennt sein Ziel.",
          description=[
              "Nimm das &6Model Framework&r in die Hand und &eklick mit rechts auf einen lebenden Mob&r. Im Chat steht dann &aSuccessfully constructed a ... Data Model&r, und du hältst ein &6Datenmodell&r für genau diese Mobart.",
              "",
              "Leg das Modell in den &6Deep Learner&r. Es startet als &8Faulty&r mit null Daten. Ab jetzt bringt jeder Kill dieser Mobart Daten, solange der Learner bei dir ist.",
              "",
              "&eVarianten zählen mit:&r Wüstenzombies und Dorfbewohnerzombies füllen das Zombie-Modell, Eiswanderer und Sumpfskelette das Skelett-Modell. Steht im Chat &cNo known models exist&r, gibt es für diesen Mob kein Modell. Die Liste steht im Abschnitt darunter.",
          ],
          tasks=[task_item("hostilenetworks:data_model", 1)],
          rewards=[reward_item("hostilenetworks:blank_data_model", 1), reward_table("s2_common"), reward_xp(5)],
          deps=["framework", "learner_gui"], icon="hostilenetworks:blank_data_model", size=1.5, shape="diamond"),

    quest("tier_basic", 7.5, 1, "&aBring ein Modell auf Basic",
          subtitle="Sechs Kills, und der Chip fängt an zu denken.",
          description=[
              "Töte &e6 Zombies&r mit dem Learner im Inventar. Das Zombie-Modell ist das beste Übungsmodell: Zombies gibt es überall, und später liefert jede Zombie-Vorhersage &6acht Eisenbarren&r.",
              "",
              "Ein &8Faulty&r-Modell gibt &e1 Datenpunkt pro Kill&r und wird bei &e6 Datenpunkten&r zu &aBasic&r. Die Zahlen gelten für jede Mobart gleich, nur der Enderdrache und der Mimic haben eigene.",
              "",
              "Erst ab &aBasic&r nimmt die Simulationskammer das Modell überhaupt an. Faulty heißt: zu wenig Daten, die Kammer verweigert den Start.",
          ],
          tasks=[task_kill("minecraft:zombie", 6)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["attune"], icon="minecraft:rotten_flesh"),

    quest("tier_advanced", 9.5, 1, "&9Bring ein Modell auf Advanced",
          subtitle="Zwölf weitere Kills.",
          description=[
              "Ein &aBasic&r-Modell gibt &e4 Datenpunkte pro Kill&r und wird bei &e54 Datenpunkten&r zu &9Advanced&r. Das sind &e12 Kills&r nach Basic, insgesamt also 18.",
              "",
              "Die &eGenauigkeit&r (Accuracy) steigt dabei stufenlos: Basic beginnt bei 5 Prozent, Advanced bei 22 Prozent. Sie entscheidet später, wie oft eine Simulation eine echte Vorhersage abwirft.",
          ],
          tasks=[task_kill("minecraft:zombie", 12)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s2_common"), reward_xp(8)],
          deps=["tier_basic"], icon="minecraft:iron_ingot"),

    quest("tier_superior", 11.5, 1, "&dBring ein Modell auf Superior",
          subtitle="Dreißig Kills, jetzt wird es ernst.",
          description=[
              "Ein &9Advanced&r-Modell gibt &e10 Datenpunkte pro Kill&r und wird bei &e354 Datenpunkten&r zu &dSuperior&r. Das sind &e30 Kills&r, insgesamt 48.",
              "",
              "Superior startet mit &e65 Prozent&r Genauigkeit. Ab hier lohnt sich ein Modell schon richtig in der Kammer: zwei von drei Simulationen bringen eine Vorhersage.",
              "",
              "&eTipp:&r Ein Schwert mit Plünderung ändert nichts an den Daten, aber es gibt dir nebenbei mehr Drops. Spawner in Verliesen und Minenschächten sind die schnellste Quelle für Zombies und Skelette.",
          ],
          tasks=[task_kill("minecraft:zombie", 30)],
          rewards=[reward_item("minecraft:iron_ingot", 24), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["tier_advanced"], icon="minecraft:iron_block"),

    quest("tier_self_aware", 14, 1, "&6&lBring ein Modell auf Self Aware",
          subtitle="Fünfzig Kills, und das Modell weiß alles.",
          description=[
              "Ein &dSuperior&r-Modell gibt &e18 Datenpunkte pro Kill&r und ist bei &e1.254 Datenpunkten&r fertig: &6Self Aware&r. Das sind &e50 Kills&r, insgesamt 98 für ein komplettes Modell.",
              "",
              "Self Aware heißt &e100 Prozent Genauigkeit&r. Jede Simulation liefert eine Vorhersage, nichts geht mehr verloren, und nur Self-Aware-Modelle dürfen später ins Rechenzentrum.",
              "",
              "Das ist die Handarbeit, von der im ersten Quest die Rede war. Etwa 100 Kills pro Mobart, einmal. Danach arbeitet die Technik für dich, für immer.",
          ],
          tasks=[task_kill("minecraft:zombie", 50)],
          rewards=[reward_table("s2_rare"), reward_item("hostilenetworks:blank_data_model", 2), reward_xp(20)],
          deps=["tier_superior"], icon="minecraft:golden_apple", size=2.0, shape="gear"),

    quest("accuracy", 16.5, 1, "&eVerstehe die Genauigkeit",
          subtitle="Warum die letzten 50 Kills die wichtigsten sind.",
          description=[
              "Die &eGenauigkeit&r ist die Chance, dass eine Simulation eine &6Vorhersage&r für den Mob abwirft. Basic 5 Prozent, Advanced 22, Superior 65, Self Aware 100. Dazwischen steigt sie mit jedem Datenpunkt ein Stück.",
              "",
              "Ein Basic-Modell braucht also im Schnitt 20 Simulationen, jede 12 Sekunden lang und mit vollem Strom, für eine einzige Vorhersage. Ein Self-Aware-Modell braucht eine. Trainier fertig, bevor du Strom verbrennst.",
              "",
              "Auf Kronwerke ist das gewollt: Wer in Stufe 2 die Kills sammelt, hat in Stufe 3 die beste Kammer auf dem Server.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["tier_self_aware"], icon="minecraft:ender_eye", optional=True),

    # ---- Welche Modelle lohnen sich -------------------------------------------
    quest("models_overview", 0, 6.5, "&3Kenne die Modelle im Pack",
          subtitle="Was es gibt, und was es kostet.",
          description=[
              "Jedes Modell hat einen festen &dStromverbrauch pro Tick&r in der Simulationskammer. Je gefährlicher der Mob, desto teurer:",
              "",
              "&e64 FE/t:&r Kuh, Schaf, Huhn, Schwein. &e128 FE/t:&r Zombie, Skelett, Creeper, Spinne, Schleim, Ertrunkener, Phantom. &e256 FE/t:&r Lohe, Ghast, Magmawürfel, Zombifizierter Piglin, Hoglin, Hexe, Wächter, Breeze, Wilden.",
              "&e512 FE/t:&r Enderman, Shulker, Diener (Vindicator). &e768 FE/t:&r Witherskelett. &e1.024 FE/t:&r Eisengolem, Magier (Evoker), Großer Wächter. &e2.560 FE/t:&r Wither, Warden, Mimic. &e4.096 FE/t:&r Enderdrache.",
              "",
              "&cKein Modell&r haben die Bosse von Cataclysm, Fledermaus und Tintenfisch zählen nur als Spielerei. Die Erzmodelle des Mods sind auf dem Server abgeschaltet.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["attune"], icon="minecraft:book", size=1.5, shape="hexagon"),

    quest("wither_skeleton", 3, 5.5, "&8Lerne das Witherskelett",
          subtitle="Schädel ohne Plünderung III.",
          description=[
              "Töte &e18 Witherskelette&r in einer Netherfestung mit dem Learner im Inventar. Das bringt ein frisches Modell bis &9Advanced&r.",
              "",
              "Das Modell ist mit &d768 FE/t&r teuer, aber jede Vorhersage wird im Fabrikator wahlweise zu &63 Witherskelettschädeln&r, 24 Knochen oder 32 Kohle. Drei Schädel pro Simulation statt 2,5 Prozent pro Kill: so wird der Wither planbar.",
              "",
              "&eKronwerke:&r Wie du sicher in die Festung kommst, steht im Kapitel &cDer Nether&r.",
          ],
          tasks=[task_kill("minecraft:wither_skeleton", 18)],
          rewards=[reward_item("minecraft:bone", 16), reward_item("minecraft:coal", 16), reward_xp(8)],
          deps=["models_overview"], icon="minecraft:wither_skeleton_skull"),

    quest("blaze", 3, 7.5, "&6Lerne die Lohe",
          subtitle="Sechzehn Ruten pro Vorhersage.",
          description=[
              "Töte &e18 Lohen&r am Spawner mit dem Learner im Inventar. Du bist dort ohnehin für Create.",
              "",
              "Das Lohen-Modell kostet &d256 FE/t&r, und eine Vorhersage wird im Fabrikator zu &616 Lohenruten&r. Schon in Stufe 3 ergeben zwei &6Nether-Vorhersagen&r und ein Knochen an der Werkbank eine Rute, ganz ohne Fabrikator.",
              "",
              "&eKronwerke:&r Messing braucht Lohenstaub, und das Messingziel am Obelisken verlangt 2.000 Barren. Ein fertiges Lohen-Modell ist der bequemste Nachschub, den es gibt.",
          ],
          tasks=[task_kill("minecraft:blaze", 18)],
          rewards=[reward_item("minecraft:blaze_rod", 6), reward_table("s2_common"), reward_xp(8)],
          deps=["models_overview"], icon="minecraft:blaze_rod"),

    quest("enderman", 5.5, 5.5, "&5Lerne den Enderman",
          subtitle="Perlen, ohne ins End zu müssen.",
          description=[
              "Töte &e18 Endermen&r mit dem Learner im Inventar. Nachts in der Oberwelt, oder gleich dutzendweise im Warzenwald des Nethers.",
              "",
              "Das Modell kostet &d512 FE/t&r. Jede Vorhersage wird zu &616 Enderperlen&r oder einem Enderkristall. Die Grundvorhersage dieses Modells ist allerdings eine &5Ender-Vorhersage&r, und die ist bis &6Stufe 4&r gesperrt. Lohnt sich also erst mit dem End.",
          ],
          tasks=[task_kill("minecraft:enderman", 18)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(8)],
          deps=["models_overview"], icon="minecraft:ender_pearl"),

    quest("ghast", 5.5, 7.5, "&fLerne den Ghast",
          subtitle="Tränen für die Regeneration.",
          description=[
              "Töte &e6 Ghasts&r mit dem Learner im Inventar, am besten mit dem Bogen über der Lavasee. Sechs Kills machen das Modell gerade Basic.",
              "",
              "Das Modell kostet &d256 FE/t&r. Eine Vorhersage wird zu &616 Ghast-Tränen&r oder 32 Schwarzpulver. Tränen braucht jeder Trank der Regeneration und der Endkristall.",
          ],
          tasks=[task_kill("minecraft:ghast", 6)],
          rewards=[reward_item("minecraft:ghast_tear", 2), reward_xp(5)],
          deps=["models_overview"], icon="minecraft:ghast_tear", optional=True),

    quest("witch", 8, 5.5, "&5Lerne die Hexe",
          subtitle="Redstone und Glowstone aus dem Sumpf.",
          description=[
              "Töte &e12 Hexen&r mit dem Learner im Inventar. Sumpfhütten, Überfälle und Dörfer bei Nacht sind die Plätze dafür.",
              "",
              "Das Hexen-Modell kostet &d256 FE/t&r und ist das vielseitigste: eine Vorhersage wird zu &616 Redstone&r, 16 Glowstonestaub, 32 Zucker, 32 Stöcken, 16 Spinnenaugen oder 16 Glasflaschen, ganz wie du es im Fabrikator einstellst.",
          ],
          tasks=[task_kill("minecraft:witch", 12)],
          rewards=[reward_item("minecraft:redstone", 16), reward_item("minecraft:glowstone_dust", 8), reward_xp(5)],
          deps=["models_overview"], icon="minecraft:glowstone_dust", optional=True),

    quest("wilden", 8, 7.5, "&aLerne die Wilden",
          subtitle="Für die Magier: Horn, Stachel und Flügel.",
          description=[
              "Töte &e6 Wilden&r von Ars Nouveau mit dem Learner im Inventar. Jäger, Pirscher und Wächter füllen zusammen ein Modell.",
              "",
              "Das Modell kostet &d256 FE/t&r. Eine Vorhersage wird zu &616 Wilden-Hörnern&r, 16 Stacheln oder 16 Flügeln. Wer Ars spielt, weiß, wie viele Flügel ein Zauberbuch frisst.",
          ],
          tasks=[task_kill("ars_nouveau:wilden_hunter", 6)],
          rewards=[reward_item("ars_nouveau:wilden_horn", 2), reward_xp(5)],
          deps=["models_overview"], icon="ars_nouveau:wilden_horn", optional=True),

    quest("mimic", 10.5, 5.5, "&eLerne den Mimic",
          subtitle="Das seltenste Modell, und das lohnendste.",
          description=[
              "Richte ein Gerüst auf einen &6Mimic&r von Artifacts und töte ihn. Mimics tarnen sich als Truhen in Verliesen und Minenschächten und springen dich an, wenn du sie öffnest.",
              "",
              "Der Mimic hat eigene Zahlen: &e30 Kills&r bis Basic, dann je 30 bis Advanced und Superior, &e36&r bis Self Aware, insgesamt 126. Das Modell kostet &d2.560 FE/t&r.",
              "",
              "Dafür wird jede Vorhersage zu einem &6Artefakt deiner Wahl&r: Kreuzkette, Kraftschuhe, Nachtsichtbrille, Wolke in der Flasche, alles, was der Mod hat. Kein anderes Modell gibt dir Ausrüstung.",
          ],
          tasks=[task_kill("artifacts:mimic", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["models_overview"], icon="minecraft:chest", optional=True),

    quest("bosses", 10.5, 7.5, "&cBosse als Modell",
          subtitle="Wither, Warden und Drache, aber nicht Cataclysm.",
          description=[
              "Auch der &8Wither&r (2.560 FE/t, ein &6Netherstern&r pro Vorhersage), der &3Warden&r (2.560 FE/t, Echo-Scherben, Sculk-Katalysatoren, das Herz der Tiefe) und der &5Enderdrache&r (4.096 FE/t, Drachenatem oder ein Drachenei) haben Modelle.",
              "",
              "Der Drache hat eigene Zahlen: 2 Kills bis Basic, 4 bis Advanced, 10 bis Superior, 20 bis Self Aware. Wither und Warden brauchen die üblichen 98. Das wird ein Serverprojekt für Stufe 4.",
              "",
              "&cDie Bosse von Cataclysm&r haben kein Datenmodell. Ihre Drops gibt es nur im Kampf, siehe Kapitel &cBosse der Oberwelt&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["models_overview"], icon="minecraft:wither_skeleton_skull", optional=True),

    # ---- Stufe 3: Simulieren --------------------------------------------------
    quest("sim_chamber", 0, 12.5, "&b&lDie Simulationskammer",
          subtitle="Kommt in Stufe 3. Hier kämpft der Computer für dich.",
          description=[
              "&eRezept auf Kronwerke:&r oben eine &6Glasscheibe&r. Mitte &6Enderperle&r, &6Quelljuwelblock&r aus Ars Nouveau, Enderperle. Unten &6Lapislazuli&r, &6Komparator&r, Lapislazuli. Der Juwelblock ersetzt den Obsidian des Originals.",
              "",
              "Die &6Simulation Chamber&r nimmt ein &6Datenmodell&r (mindestens Basic), eine &6Vorhersagematrix&r und &dStrom&r, und spielt den Kampf gegen den Mob nach. Sie speichert bis zu &d2 Millionen FE&r.",
              "",
              "&eIm Fenster:&r links der Modellslot, darunter die Matrix. Rechts zwei Ausgänge, einer für die Grundvorhersage, einer für die Mob-Vorhersage. Die Textzeilen in der Mitte zeigen, was die Kammer gerade tut, und warum sie stehen bleibt.",
              "",
              "&cStufe 3:&r Die Kammer öffnet mit dem Stahlwerk. Bis dahin: Modelle trainieren und Quelljuwelen sammeln.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_item("minecraft:lapis_lazuli", 8)],
          deps=["tier_basic"], icon="minecraft:comparator", size=1.5, shape="hexagon"),

    quest("matrix", 2.5, 11.5, "&bDie Vorhersagematrix",
          subtitle="Kommt in Stufe 3. Das Papier, auf das die Kammer schreibt.",
          description=[
              "&eRezept:&r ein &6Eisenbarren&r oben links, ein &6Goldbarren&r unten rechts, ein &6Tonklumpen&r in der Mitte und vier &6Glasscheiben&r auf den freien Feldern dazwischen. Ergibt &e16 Prediction Matrix&r.",
              "",
              "Jede Simulation verbraucht genau &eeine Matrix&r. Ein Tonklumpen reicht also für 16 Simulationen, ein Stapel Ton für tausend. Teuer sind eher die Glasscheiben: vier pro Rezept.",
              "",
              "Der Ausgang für die Grundvorhersage und der für die Mob-Vorhersage müssen frei sein, sonst startet die Kammer nicht. Ein Trichter oder Rohr an der Kammer löst das.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("minecraft:glass_pane", 16), reward_item("minecraft:gold_ingot", 2)],
          deps=["sim_chamber"], icon="minecraft:clay_ball"),

    quest("clay", 2.5, 13.5, "&bTon und Glas am Band",
          subtitle="Kommt in Stufe 3. Matrizen nie wieder von Hand.",
          description=[
              "&eTon:&r Create wäscht &6Sand&r unter einem Ventilator mit Wasser zu Tonklumpen (25 Prozent). Die Anreicherungskammer von Mekanism macht aus &6Schlamm&r Tonblöcke und aus einem Tonblock vier Klumpen. Ein Bohrer von Create auf einer Tonader im Fluss geht auch.",
              "",
              "&eGlas:&r Sand im Schmelzer, sechs Glas werden an der Werkbank zu 16 Scheiben. Ein Mechanischer Handwerker oder eine AE2-Autocraft-Vorlage baut dir dann Matrizen auf Vorrat.",
              "",
              "Für ein Rechenzentrum in Stufe 4 brauchst du etwa &e100 Matrizen pro Minute&r. Plan die Linie jetzt, dann steht sie, wenn es so weit ist.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("minecraft:clay_ball", 32), reward_item("minecraft:sand", 32)],
          deps=["sim_chamber"], icon="minecraft:clay", optional=True),

    quest("simulation", 5, 12.5, "&b&lWas eine Simulation ist",
          subtitle="Kommt in Stufe 3. Zwölf Sekunden, eine Matrix, zwei Ausgänge.",
          description=[
              "Eine Simulation dauert &e12 Sekunden&r und frisst die ganze Zeit den Stromwert des Modells: ein Zombie &d128 FE/t&r, also rund 31.000 FE pro Durchlauf, ein Witherskelett &d768 FE/t&r, also rund 184.000 FE.",
              "",
              "&eAusgang 1, immer:&r eine &6Generalisierte Vorhersage&r. Oberwelt-Mobs geben die &aOverworld Prediction&r, Nether-Mobs die &cNether Prediction&r, Enderman, Shulker, Wither und Mimic die &5Ender Prediction&r (Stufe 4).",
              "",
              "&eAusgang 2, mit Glück:&r eine &6Vorhersage des Mobs&r, zum Beispiel &6Blaze Prediction&r. Die Chance ist die Genauigkeit des Modells. Diese Vorhersage ist das, was der Loot-Fabrikator in Stufe 4 zu Drops macht.",
              "",
              "&eRedstone:&r Mit dem Knopf im Fenster stellst du ein, ob ein Signal die Kammer anhält oder startet. So kann ein Komparator am Ausgangslager sie bremsen, wenn genug da ist.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_table("s2_common"), reward_xp(8)],
          deps=["sim_chamber", "matrix"], icon="minecraft:ender_eye", size=1.5, shape="diamond"),

    quest("training", 7.5, 11.5, "&bDer Trainingsmodus",
          subtitle="Kommt in Stufe 3. Die Kammer lernt, aber langsam.",
          description=[
              "Der Knopf mit der Erfahrungsflasche schaltet die Kammer auf &6Training&r: eine Simulation dauert dann &e15 Sekunden&r, kostet &e120 Prozent&r Strom, gibt &ekeine Ausgabe&r und bringt dem Modell &e1 Datenpunkt&r.",
              "",
              "Rechne nach: Ein Kill bringt 4 bis 18 Datenpunkte, das Training einen in 15 Sekunden. Von Basic bis Self Aware wären das über fünf Stunden Strom. Trainieren lohnt sich nur für Mobs, an die du nicht herankommst, oder für die letzten paar Punkte.",
              "",
              "Der normale Modus heißt &6Inference&r (das Enderauge). Dort gibt es Ausgaben, aber das Modell lernt nichts dazu.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("minecraft:experience_bottle", 4)],
          deps=["simulation"], icon="minecraft:experience_bottle", optional=True),

    quest("generalized", 7.5, 13.5, "&aVorhersagen ohne Fabrikator",
          subtitle="Kommt in Stufe 3. Die Werkbank reicht für den Anfang.",
          description=[
              "Die &6Generalisierten Vorhersagen&r aus Ausgang 1 kannst du schon in Stufe 3 an der Werkbank verwerten, ohne Loot-Fabrikator:",
              "",
              "&e4 Overworld Prediction + 1 Verrottetes Fleisch = 8 Eisenbarren.&r &e1 Overworld Prediction + 1 Knochenmehl = 22 Knochen.&r &e2 Nether Prediction + 1 Knochen = 1 Lohenrute.&r &e1 Nether Prediction + Glowstonestaub + Eisenbarren = 6 Goldbarren.&r",
              "",
              "Vier Overworld Predictions um ein Netherrack ergeben eine Nether Prediction, vier Nether Predictions um einen Endstein eine Ender Prediction.",
              "",
              "&eKronwerke:&r Das Stahlziel von Stufe 3 heißt 4.000 Stahlbarren. Ein Zombie-Modell gibt alle 48 Sekunden acht Eisen, egal wie gut es trainiert ist. Mit Self Aware kommen die Zombie-Vorhersagen für den Fabrikator noch obendrauf.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_item("minecraft:bone_meal", 16)],
          deps=["simulation"], icon="minecraft:iron_ingot"),

    quest("power", 10, 12.5, "&dStrom für die Kammer",
          subtitle="Kommt in Stufe 3. Ein Netz, viele Kammern.",
          description=[
              "Eine Kammer zieht nur, solange sie simuliert, aber dann richtig: &d128 FE/t&r für einen Zombie sind sechs Wärmegeneratoren, &d768 FE/t&r für ein Witherskelett ein kleines Kraftwerk. Der Puffer von 2 Millionen FE fängt Spitzen ab, ersetzt aber keine Quelle.",
              "",
              "Leg die Kammern an &eeine Leitung&r. In Stufe 3 öffnet &6Flux Networks&r: ein Flux Plug am Generator, ein Flux Point an jeder Kammer, keine Kabel durch die Halle. Wie das geht, steht im Kapitel &6Flux Networks&r, Stromquellen im Kapitel &6Powah&r.",
              "",
              "&eRechenhilfe:&r Stromwert mal 240 ist der Verbrauch pro Simulation. Stromwert mal Kammern ist, was dein Netz liefern muss, wenn alle laufen.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_item("mekanism:basic_universal_cable", 8), reward_xp(5)],
          deps=["simulation"], icon="mekanism:basic_energy_cube"),

    quest("scaling", 12.5, 12.5, "&d&lViele Kammern, ein Modell je Kammer",
          subtitle="Kommt in Stufe 3. So wird aus einem Chip eine Fabrik.",
          description=[
              "Eine Kammer, ein Modell, fünf Simulationen pro Minute. Mehr geht nur mit &emehr Kammern&r, und das ist auch der Plan: Kammern sind billig, Modelle kopierst du nicht, aber zehn Zombie-Modelle sind zehnmal 98 Kills.",
              "",
              "&eBeispiel:&r Zehn Kammern mit Self-Aware-Zombies ziehen 1.280 FE/t, verbrauchen 50 Matrizen pro Minute und werfen 50 Overworld Predictions und 50 Zombie Predictions ab. Das sind an der Werkbank 100 Eisen pro Minute, im Fabrikator noch einmal 400.",
              "",
              "&eLogistik:&r Matrizen per Rohr oder Transporter in jede Kammer, beide Ausgänge in eine gemeinsame Kiste, die Kiste an die Werkbank-Automatik oder ans AE2-Netz. Eine Reihe Kammern an einer Wand, Flux Points dahinter, fertig.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 3")],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["power"], icon="minecraft:hopper", size=1.5, shape="gear"),

    # ---- Stufe 4: Fabrizieren -------------------------------------------------
    quest("loot_fab", 0, 18.5, "&6&lDer Loot-Fabrikator",
          subtitle="Kommt in Stufe 4. Aus der Vorhersage wird der Drop.",
          description=[
              "&eRezept auf Kronwerke:&r oben ein &6Netheritbarren&r. Mitte &6Diamant&r, &6Obsidian&r, Diamant. Unten &6Goldbarren&r, &6Engineering-Prozessor&r aus AE2, Goldbarren. Der Prozessor ersetzt den Komparator des Originals.",
              "",
              "Der &6Loot Fabricator&r nimmt eine &6Mob-Vorhersage&r und macht in &e3 Sekunden&r für &d256 FE/t&r daraus einen Stapel Drops. Welchen, wählst du im Fenster: Links die Vorhersage, in der Mitte die Liste der möglichen Drops, Klick auf einen setzt ihn fest.",
              "",
              "&eZwei Modi:&r &6Fixed&r macht immer den gewählten Drop. &6Queue&r arbeitet eine Reihenfolge ab, die du anklickst. Er speichert 1 Million FE.",
              "",
              "&cStufe 4:&r Netherit und der Prozessor sind kein Problem, aber der Fabrikator selbst ist bis zum Sternwerk gesperrt.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:diamond", 1)],
          deps=["simulation"], icon="minecraft:anvil", size=1.5, shape="hexagon"),

    quest("drops", 2.5, 17.5, "&6Was aus einer Vorhersage wird",
          subtitle="Kommt in Stufe 4. Immer ein ganzer Stapel.",
          description=[
              "Jede Vorhersage ergibt &eeinen&r der Drops ihres Modells, und zwar in Mengen, die sich lohnen:",
              "",
              "&eZombie:&r 64 Verrottetes Fleisch, &68 Eisen&r, 16 Karotten oder 16 Kartoffeln. &eSkelett:&r 32 Pfeile, 24 Knochen oder 4 Schädel. &eCreeper:&r 32 Schwarzpulver oder 4 Köpfe. &eSpinne:&r 32 Fäden, 16 Augen oder 4 Spinnweben.",
              "&eLohe:&r &616 Lohenruten&r. &eWitherskelett:&r &63 Schädel&r, 24 Knochen oder 32 Kohle. &eEnderman:&r 16 Enderperlen oder ein Endkristall. &eEisengolem:&r 32 Eisen. &eMagier:&r 2 Totems der Unsterblichkeit oder 16 Smaragde.",
              "",
              "Mit Reliquary, EvilCraft und Deeper and Darker im Pack kommen deren Mobteile dazu: Verwitterte Rippe, Geschmolzener Kern, Enderträne, Herz der Tiefe. Der Tooltip des Modells listet alles auf, halt Shift.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_item("minecraft:gunpowder", 16), reward_item("minecraft:bone", 16)],
          deps=["loot_fab"], icon="minecraft:blaze_rod"),

    quest("directive", 2.5, 19.5, "&6Die Fabrikationsanweisung",
          subtitle="Kommt in Stufe 4. Einstellungen zum Mitnehmen.",
          description=[
              "&eRezept:&r eine &6Generalisierte Vorhersage&r oben, &6Papier&r, &6Vorhersagematrix&r, Papier in der Mitte, Papier unten.",
              "",
              "Die &6Fabrication Directive&r speichert, welcher Drop für welches Modell gewählt ist. &eRechtsklick&r auf einen Fabrikator kopiert seine Auswahl, &eShift-Rechtsklick&r auf einen anderen überträgt sie. Für zehn Fabrikatoren oder das Rechenzentrum sparst du dir damit das Durchklicken.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_item("minecraft:paper", 16)],
          deps=["loot_fab"], icon="minecraft:paper", optional=True),

    quest("data_center", 5, 18.5, "&5&lDas Rechenzentrum",
          subtitle="Kommt in Stufe 4. 25 Modelle, ein Block, tausende Drops.",
          description=[
              "&eRezept:&r oben &6Echo-Scherbe&r, &6Netherstern&r, Echo-Scherbe. Mitte &6Simulationskammer&r, Obsidian, &6Loot-Fabrikator&r. Unten drei &6Obsidian&r.",
              "",
              "Das &6Data Center&r braucht eine Hülle von &e7 mal 7 mal 7&r Blöcken, innen hohl: der &6Boden aus Obsidian&r, &6Wände und Decke aus schwarzem Glas&r. Der Controller ersetzt einen Block der untersten Wandreihe und schaut nach außen.",
              "",
              "Innen liegt ein Raster von 5 mal 5 Plätzen für &e25 Self-Aware-Modelle&r und vier Eingänge für Matrizen. Jedes Modell macht alle &e15 Sekunden&r eine Simulation und wirft &edirekt den Drop&r aus, Simulation und Fabrikator in einem. Was, bestimmt seine Fabrikationsanweisung.",
              "",
              "Der Preis: jedes Modell kostet &e150 Prozent&r seines Stromwerts, 25 Zombies also 4.800 FE/t, 25 Lohen 9.600 FE/t. Der Puffer fasst 8 Millionen FE.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_item("minecraft:obsidian", 16), reward_item("minecraft:black_stained_glass", 32), reward_xp(10)],
          deps=["loot_fab", "scaling"], icon="minecraft:black_stained_glass", size=1.75, shape="hexagon"),

    quest("io_port", 7.5, 17.5, "&5Der IO-Port",
          subtitle="Kommt in Stufe 4. Die Steckdose in der Glaswand.",
          description=[
              "&eRezept:&r &6Eisenbarren&r in die Ecken, &6schwarzes Glas&r an die Seiten, ein &6Redstoneblock&r in die Mitte.",
              "",
              "Der &6Data Center IO Port&r ersetzt einen beliebigen Wand- oder Deckenblock der Hülle. &eRechtsklick&r schaltet seinen Modus: &dEnergy&r nimmt Strom, &6Models&r die Modelle, &aInputs&r die Matrizen, &eOutputs&r gibt die Drops heraus.",
              "",
              "Vier Ports, einer pro Modus, und du musst die Hülle nie wieder öffnen. Rohre an Inputs und Outputs, ein Flux Point an Energy, fertig.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_item("minecraft:iron_ingot", 8)],
          deps=["data_center"], icon="minecraft:redstone_block"),

    quest("throughput", 7.5, 19.5, "&5Tausende pro Minute",
          subtitle="Kommt in Stufe 4. Die Rechnung am Ende.",
          description=[
              "25 Modelle, alle 15 Sekunden ein Stapel: das sind &e100 Stapel pro Minute&r. Mit 25 Lohen-Modellen &61.600 Lohenruten&r pro Minute, mit Witherskeletten 3.200 Kohle oder 300 Schädel, mit Zombies 800 Eisen.",
              "",
              "Dafür braucht das Zentrum &e100 Matrizen pro Minute&r, also sechs Tonklumpen, sechs Eisen, sechs Gold und 25 Glasscheiben, und zwischen 4.800 und 28.800 FE/t. Beides plant man, bevor man den Netherstern verbaut.",
              "",
              "Und das war der Weg: 98 Kills pro Modell in Stufe 2, Kammern an einem Stromnetz in Stufe 3, und in Stufe 4 ersetzt ein Glaswürfel jede Mobfarm des Servers.",
          ],
          tasks=[task_checkmark("Verstanden, kommt in Stufe 4")],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["data_center"], icon="minecraft:nether_star"),

    quest("models_more", 10.5, 18.5, "&3Trainiere jetzt für später",
          subtitle="Vier Modelle im Learner, bevor Stufe 3 kommt.",
          description=[
              "Du weißt jetzt, was auf dich zukommt. Der beste Zeitpunkt für die Kills ist &ejetzt&r, solange du ohnehin im Nether und in den Verliesen unterwegs bist.",
              "",
              "Bau &e4 Modellgerüste&r, richte sie auf Zombie, Lohe, Witherskelett und einen Mob deiner Wahl, und lass den Learner einfach im Inventar. Nach ein paar Abenden sind alle vier Self Aware, und in Stufe 3 stehst du mit vier fertigen Modellen vor der ersten Kammer.",
          ],
          tasks=[task_item("hostilenetworks:blank_data_model", 4)],
          rewards=[reward_item("hostilenetworks:deep_learner", 1), reward_table("s2_common"), reward_xp(10)],
          deps=["throughput"], icon="hostilenetworks:deep_learner", shape="diamond"),
]

images = [
    banner("hostile_networks/title", "Hostile Neural Networks", 8, -4.5, height=1.75, kind="title", colour="water"),
    banner("hostile_networks/learn", "Daten sammeln", 8, -2.2, height=0.9, colour="stone"),
    banner("hostile_networks/models", "Welche Modelle lohnen sich", 5.5, 3.9, height=0.9, colour="fire"),
    banner("hostile_networks/simulate", "Stufe 3: Simulieren", 6, 9.9, height=0.9, colour="water"),
    banner("hostile_networks/fabricate", "Stufe 4: Fabrizieren", 5.5, 15.9, height=0.9, colour="end"),
]

chapter(C, "Hostile Neural Networks", "hostilenetworks:deep_learner", "tech", quests, shape="circle", order=63, stage=2,
        subtitle=["Stufe 2: Monster lernen, später simulieren und fabrizieren. Die Mobfarm, die keine Mobs braucht."],
        images=images)
