"""The Undergarden, opened with stage 3: the catalyst and the stone brick portal, the biomes,
food and the slingshot, the four ores one step each (cloggrum, froststeel, utherium, regalium),
the Rotspawn and the Utheric infection, checklists of every ore with its Y range and every mob
with its drop, the catacombs with the Forgotten Guardian and the forgotten gear, and the Depths
with rogdorium, the infuser and the denizens. Facts come from the mod jar (worldgen, loot
tables, recipes, lang, advancements). The dimension runs from Y -64 to Y 127."""
from ftbq import (chapter, quest, task_item, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "undergarden"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Anreise -------------------------------------------------------------
    quest("catalyst", 0, 0, "&2&lBau den Katalysator",
          subtitle="Der Schlüssel zum Undergarden.",
          description=[
              "&eRezept auf Kronwerke:&r &64 Stahlbarren&r in die Ecken, &64 Stein&r an die Seiten, &61 Enderperle&r in die Mitte. Das ergibt den &6Katalysator&r.",
              "",
              pic("undergarden:catalyst"),
              "",
              "Der &2Undergarden&r ist eine dunkle Dimension voller Pilze, Moderwesen und neuer Erze. Er ist ab &eStufe 3&r offen.",
          ],
          tasks=[task_item("undergarden:catalyst", 1)],
          rewards=[reward_item("minecraft:stone_bricks", 16), reward_table("s3_common")],
          icon="undergarden:catalyst", size=2.0, shape="hexagon"),

    quest("arrival", 2.5, 0, "&2&lSteig hinunter",
          subtitle="Rahmen aus Steinziegeln, Katalysator drauf.",
          description=[
              "Bau einen Rahmen wie ein Netherportal, aber aus &6Steinziegeln&r. Rechtsklick mit dem &6Katalysator&r auf den Rahmen öffnet das Portal. Geh hindurch.",
              "",
              "Rissige, bemooste und gemeißelte Steinziegel gehen auch, ebenso Tiefschieferziegel und Tiefschieferfliesen.",
              "",
              "&eDrüben:&r ewige Nacht, Monster überall, wo kein Blocklicht hinkommt. &eBetten funktionieren&r, stell gleich eines ans Portal. Ein Block hier sind &e4 Blöcke&r in der Oberwelt.",
          ],
          tasks=[task_dimension("undergarden:undergarden")],
          rewards=[reward_item("minecraft:torch", 64), reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["catalyst"], icon="undergarden:depthrock", size=1.75, shape="hexagon"),

    # ---- Ueberleben ----------------------------------------------------------
    quest("food", 5, -5, "&aPflück Unterbohnen",
          subtitle="Das erste Essen hier unten.",
          description=[
              "&6Unterbohnenbüsche&r stehen am Boden. Abbauen gibt &6Unterbohnen&r. Im Ofen werden daraus &6Geröstete Unterbohnen&r, die mehr sättigen.",
              "",
              "&eNoch mehr Essen:&r &6Schlafffrüchte&r hängen an den leuchtenden Schlaffranken an der Decke, &6Blasenbeeren&r wachsen an Büschen. Verrottete Blasenbeeren nicht essen, die sind zum Werfen.",
          ],
          tasks=[task_item("undergarden:underbeans", 16)],
          rewards=[reward_item("undergarden:roasted_underbeans", 8), reward_xp(3)],
          deps=["arrival"], icon="undergarden:underbeans"),

    quest("gourd", 7.5, -5, "&5Pflanz Düsterkürbisse",
          subtitle="Ein Feld, das dich satt hält.",
          description=[
              "&6Düsterkürbisse&r liegen lila im Gras. Ein Kürbis an der Werkbank gibt &64 Düsterkürbiskerne&r. Pflanz sie wie Kürbiskerne.",
              "",
              "Aus dem Kürbis werden auch Kuchen und der &6Geschnitzte Düsterkürbis&r. Den brauchst du später für den Vergessenen Diener.",
          ],
          tasks=[task_item("undergarden:gloomgourd", 4), task_advancement("undergarden:undergarden/plant_gloomgourd", "Düsterkürbiskerne pflanzen")],
          rewards=[reward_item("undergarden:gloomgourd_seeds", 4), reward_xp(4)],
          deps=["food"], icon="undergarden:gloomgourd"),

    quest("meat", 10, -5, "&6Brat ein Bewohnersteak",
          subtitle="Fleisch und Leder vom Bewohner.",
          description=[
              "&6Bewohner&r sind die großen, ruhigen Tiere des Undergarden. Sie lassen &6Rohes Bewohnerfleisch&r und Leder fallen. Im Ofen wird daraus ein &6Bewohnersteak&r.",
              "",
              "Einen gesattelten Bewohner kannst du reiten und mit einer &6Unterbohne am Stock&r lenken. Die hüpfenden &6Gloomper&r geben Gloomperbeine und Leder.",
          ],
          tasks=[task_item("undergarden:dweller_steak", 8)],
          rewards=[reward_item("undergarden:underbean_on_a_stick", 1), reward_xp(5)],
          deps=["gourd"], icon="undergarden:dweller_steak"),

    quest("slingshot", 12.5, -5, "&6Bau eine Schleuder",
          subtitle="Kiesel als Munition, überall zu finden.",
          description=[
              "Werkbank: &6Stöcke&r im Rahmen, oben in der Mitte ein &6Verdrehter Zweig&r. Die Zweige fallen aus dem Laub der Wackelholzbäume.",
              "",
              "Munition sind &6Tiefkieselsteine&r vom Boden, Skintlingschleimbälle (machen das Ziel klebrig), verrottete Blasenbeeren (explodieren) und Grongelchen.",
              "",
              "Aus Verdrehten Zweigen und Stöcken wird außerdem Gerüst, 6 Stück pro Rezept.",
          ],
          tasks=[task_item("undergarden:slingshot", 1), task_item("undergarden:depthrock_pebble", 32)],
          rewards=[reward_item("undergarden:depthrock_pebble", 32), reward_xp(5)],
          deps=["meat", "b_forest"], icon="undergarden:slingshot"),

    quest("rotspawn", 5, -2.5, "&4Erleg die Moderwesen",
          subtitle="Die eigentlichen Monster hier unten.",
          description=[
              "Töte &65 Moderlinge&r und sammle &68 Utherische Scherben&r. Alle Moderwesen lassen Scherben fallen.",
              "",
              "&cUtherische Infektion:&r Jeder Treffer eines Moderwesens steckt dich weiter an. Wird sie zu stark, wird es lebensgefährlich. Bleib auf Abstand und lauf nicht in Gruppen hinein.",
              "",
              "Gegenmittel ist &6Rogdorium&r aus den Tiefen, siehe unten.",
          ],
          tasks=[task_kill("undergarden:rotling", 5), task_item("undergarden:utheric_shard", 8)],
          rewards=[reward_item("minecraft:arrow", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["arrival"], icon="undergarden:utheric_shard"),

    quest("shard_torch", 7.5, -2.5, "&bBau Scherbenfackeln",
          subtitle="Licht, das zurückbeißt.",
          description=[
              "Werkbank: eine &6Utherische Scherbe&r auf einen &6Stock&r ergibt eine &6Scherbenfackel&r.",
              "",
              "Sie leuchtet wie eine Fackel und schadet Moderwesen in ihrer Nähe. Ein Ring davon um Portal, Bett und Schacht, und es wird ruhiger.",
          ],
          tasks=[task_item("undergarden:shard_torch", 8)],
          rewards=[reward_item("undergarden:utheric_shard", 4), reward_xp(3)],
          deps=["rotspawn"], icon="undergarden:shard_torch"),

    # ---- Biome ---------------------------------------------------------------
    quest("b_forest", 2.5, 5, "&2Durchquer die Wälder",
          subtitle="Smogstiel, Wackelholz und Grongel.",
          description=[
              "Fäll &616 Smogstielstämme&r. Das ist das Bauholz des Undergarden.",
              "",
              "&eDie Waldbiome:&r &6Smogstielwald&r, &6Dichter Wald&r, &6Wackelholzwald&r, &6Grongelwucher&r und die &6Smogtürme&r mit ihren rauchenden Schlitzen. Im &6Vergessenen Feld&r stehen die Katakomben.",
          ],
          tasks=[task_item("undergarden:smogstem_log", 16)],
          rewards=[reward_item("minecraft:torch", 32), reward_xp(4)],
          deps=["arrival"], icon="undergarden:smogstem_log"),

    quest("b_bogs", 5, 5, "&5Lauf durch die Pilzmoore",
          subtitle="Riesenpilze in vier Farben.",
          description=[
              "Sammle je einen &6Indigopilz&r und einen &6Blutpilz&r aus den Mooren.",
              "",
              "&eDie Moore:&r &6Indigopilzmoor&r, &6Blutpilzmoor&r, &6Tintenpilzmoor&r, &6Schleierpilzmoor&r und der &6Puffpilzwald&r. Aus den Pilzen werden Farbstoffe und Suppen.",
          ],
          tasks=[task_item("undergarden:indigo_mushroom", 1), task_item("undergarden:blood_mushroom", 1)],
          rewards=[reward_item("minecraft:bowl", 8), reward_xp(4)],
          deps=["b_forest"], icon="undergarden:indigo_mushroom"),

    quest("b_cold", 7.5, 5, "&bFind die Frostfelder",
          subtitle="Schlotterstein, und darin Froststahl.",
          description=[
              "Bau &632 Schlotterstein&r ab. Er liegt in den kalten Biomen: &6Frostfelder&r, &6Eisiger Smogstielwald&r und &6Eisiger See&r.",
              "",
              "Nur im Schlotterstein steckt &6Froststahl&r. Merk dir den Ort.",
          ],
          tasks=[task_item("undergarden:shiverstone", 32)],
          rewards=[reward_item("minecraft:packed_ice", 8), reward_xp(4)],
          deps=["b_bogs"], icon="undergarden:shiverstone"),

    quest("b_seas", 10, 5, "&3Fang einen Gwibbling",
          subtitle="Die Meere des Undergarden.",
          description=[
              "Fang einen &6Gwibbling&r mit einem Wassereimer. Gwibblinge schwimmen in den Meeren.",
              "",
              "&eDie Meere:&r &6Alter See&r, &6Toter See&r und &6Eisiger See&r. Dort wächst &6Glitzerseetang&r, den du braten kannst. Gebratener Gwibbling ist gutes Essen.",
          ],
          tasks=[task_item("undergarden:gwibling_bucket", 1)],
          rewards=[reward_item("undergarden:cooked_gwibling", 8), reward_xp(4)],
          deps=["b_cold"], icon="undergarden:gwibling_bucket", optional=True),

    # ---- Erze ----------------------------------------------------------------
    quest("cloggrum", 5, 0, "&7&lSchmelz Cloggrum",
          subtitle="Das Eisen des Undergarden.",
          description=[
              "Bau &6Cloggrumerz&r ab (Tiefstein oder Schlotterstein, &eY -64 bis 64&r, unten am meisten). Es gibt &6Rohcloggrum&r, im Ofen wird daraus ein &6Cloggrumbarren&r.",
              "",
              pic("undergarden:cloggrum_ingot"),
              "",
              "Aus Cloggrum werden Werkzeug, Rüstung, Schild, Eimer, Laternen und Gitter. Die &6Mampfer&r lassen Cloggrum- und Froststahlklumpen fallen.",
          ],
          tasks=[task_item("undergarden:raw_cloggrum", 16), task_item("undergarden:cloggrum_ingot", 16)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(5)],
          deps=["arrival"], icon="undergarden:cloggrum_ingot", size=1.5),

    quest("cloggrum_gear", 7.5, 0, "&7Bau eine Cloggrumspitzhacke",
          subtitle="Heb sie auf, sie wird später aufgewertet.",
          description=[
              "Werkbank: &63 Cloggrumbarren&r und &62 Stöcke&r wie eine Eisenspitzhacke. Dazu ein &6Cloggrumharnisch&r aus 8 Barren.",
              "",
              "&eWarum aufheben:&r Später wertest du die Spitzhacke am Schmiedetisch zur &6Vergessenen Spitzhacke&r auf. Nur die baut Furchtfels ab.",
              "",
              "Cloggrumstiefel haben einen Vorteil: Skintlingschleim bremst dich mit ihnen nicht.",
          ],
          tasks=[task_item("undergarden:cloggrum_pickaxe", 1), task_item("undergarden:cloggrum_chestplate", 1)],
          rewards=[reward_item("undergarden:cloggrum_ingot", 8), reward_xp(6)],
          deps=["cloggrum"], icon="undergarden:cloggrum_pickaxe"),

    quest("froststeel", 10, 0, "&bSchmelz Froststahl",
          subtitle="Nur im Schlotterstein der kalten Biome.",
          description=[
              "Bau &6Froststahlerz&r im Schlotterstein ab (&eY -64 bis 64&r, nur in kalten Biomen). Es gibt &6Rohfroststahl&r, im Ofen einen &6Froststahlbarren&r.",
              "",
              pic("undergarden:froststeel_ingot"),
          ],
          tasks=[task_item("undergarden:raw_froststeel", 8), task_item("undergarden:froststeel_ingot", 8)],
          rewards=[reward_item("minecraft:packed_ice", 8), reward_xp(7)],
          deps=["cloggrum_gear", "b_cold"], icon="undergarden:froststeel_ingot"),

    quest("froststeel_gear", 12.5, 0, "&bSchmiede ein Froststahlschwert",
          subtitle="Jeder Treffer bremst das Ziel.",
          description=[
              "Werkbank: &62 Froststahlbarren&r über &61 Stock&r ergeben das &6Froststahlschwert&r.",
              "",
              "Froststahlwaffen verlangsamen jedes Ziel, das sie treffen. Gegen schnelle Gegner ist das viel wert. Rüstung und Werkzeug gibt es auch aus Froststahl.",
          ],
          tasks=[task_item("undergarden:froststeel_sword", 1)],
          rewards=[reward_item("undergarden:froststeel_ingot", 4), reward_xp(8)],
          deps=["froststeel"], icon="undergarden:froststeel_sword"),

    quest("utherium", 10, 2.2, "&cGrab Utheriumerz",
          subtitle="Tief unten, und noch nicht fertig.",
          description=[
              "Bau &6Utheriumerz&r unter &eY 32&r ab. Es gibt einen &6Utherischen Haufen&r, keinen fertigen Kristall. &69 Utherische Scherben&r ergeben ebenfalls einen Haufen.",
              "",
              "Zum &6Utheriumkristall&r wird der Haufen erst im &6Infusionstisch&r, und den baust du mit Rogdorium aus den Tiefen. Sammle schon einmal.",
          ],
          tasks=[task_item("undergarden:utheric_cluster", 4)],
          rewards=[reward_item("undergarden:utheric_shard", 9), reward_xp(9)],
          deps=["cloggrum_gear"], icon="undergarden:utheric_cluster"),

    quest("regalium", 12.5, 2.2, "&eFind Regalium",
          subtitle="Selten und ganz unten.",
          description=[
              "Bau &6Regaliumerz&r zwischen &eY 0 und Y 12&r ab, nur 3 kleine Adern pro Chunk. Es gibt &6Regaliumkristalle&r.",
              "",
              "Regalium ist kein Werkzeugmetall. Es ist die Währung der Steingeborenen, 9 Kristalle ergeben einen Block.",
          ],
          tasks=[task_item("undergarden:regalium_crystal", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(10)],
          deps=["utherium"], icon="undergarden:regalium_crystal"),

    quest("stoneborn", 15, 2.2, "&8Handel mit einem Steingeborenen",
          subtitle="Händler aus Stein, bezahlt wird mit Regalium.",
          description=[
              "Rechtsklick auf einen &6Steingeborenen&r öffnet den Handel. Bezahlt wird mit &6Regaliumkristallen&r.",
              "",
              "&cGreif sie nicht an:&r Sie schlagen hart zu, und wer einen tötet, bekommt nur 3 bis 6 Tiefkieselsteine.",
          ],
          tasks=[task_advancement("undergarden:undergarden/stoneborn_trade", "Mit einem Steingeborenen handeln")],
          rewards=[reward_item("undergarden:regalium_crystal", 4), reward_xp(5)],
          deps=["regalium"], icon="undergarden:depthrock_pebble", optional=True),

    quest("ore_list", 15, 0, "&7&lCheckliste: Erze",
          subtitle="Jedes Erz des Undergarden mit Höhe.",
          description=[
              "Hak jedes Erz einmal ab. Die Welt geht von &eY -64&r bis &eY 127&r.",
              "",
              "&6Kohle:&r Y 0 bis 127, sehr häufig.",
              "&6Eisen:&r Y 63 bis 127, oben unter der Decke am meisten.",
              "&6Gold:&r Y 95 bis 127. &6Diamant:&r Y 111 bis 127, ganz oben.",
              "&6Cloggrum:&r Y -64 bis 64, unten am meisten. &6Froststahl:&r gleich, nur Schlotterstein.",
              "&6Utherium:&r Y -64 bis 32. &6Regalium:&r Y 0 bis 12.",
              "&6Rogdorium:&r Y -64 bis 0, nur im Furchtfels der Tiefen.",
          ],
          tasks=[task_item("undergarden:depthrock_coal_ore", 1), task_item("undergarden:raw_cloggrum", 1),
                 task_item("undergarden:raw_froststeel", 1), task_item("undergarden:utheric_cluster", 1),
                 task_item("undergarden:regalium_crystal", 1), task_item("undergarden:rogdorium", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["froststeel", "regalium"], icon="undergarden:depthrock_coal_ore"),

    # ---- Mobs ----------------------------------------------------------------
    quest("mobs_rot", 10, -2.5, "&4Checkliste: Moderwesen",
          subtitle="Alle vier Arten, alle geben Scherben.",
          description=[
              "Erleg jede Art einmal. Jede lässt &6Utherische Scherben&r fallen.",
              "",
              "&6Moderling:&r klein und schwach.",
              "&6Moderläufer:&r schnell und groß.",
              "&6Moderbiest:&r schwer, hält viel aus.",
              "&6Moderspeier:&r spuckt aus der Entfernung.",
          ],
          tasks=[task_kill("undergarden:rotling", 1), task_kill("undergarden:rotwalker", 1),
                 task_kill("undergarden:rotbeast", 1), task_kill("undergarden:rotbelcher", 1)],
          rewards=[reward_item("undergarden:shard_torch", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["shard_torch"], icon="undergarden:utheric_shard"),

    quest("mobs_animals", 12.5, -2.5, "&aCheckliste: Tiere",
          subtitle="Jedes Tier mit seiner Beute.",
          description=[
              "Ein Haken pro Beute:",
              "",
              "&6Bewohner&r und &6Großer Bewohner:&r Rohes Bewohnerfleisch, Leder.",
              "&6Gloomper:&r Rohes Gloomperbein, Leder.",
              "&6Gwibbling:&r Roher Gwibbling, Knochenmehl.",
              "&6Mog:&r Mogmoos, Tiefkiesel. &6S'Mog:&r Blauer Mogmoos.",
              "&6Skintling:&r Skintlingschleimball. &6Mampfer:&r Cloggrum- und Froststahlklumpen.",
          ],
          tasks=[task_item("undergarden:raw_dweller_meat", 1), task_item("undergarden:raw_gloomper_leg", 1),
                 task_item("undergarden:raw_gwibling", 1), task_item("undergarden:mogmoss", 1),
                 task_item("undergarden:blue_mogmoss", 1), task_item("undergarden:goo_ball", 1),
                 task_item("undergarden:froststeel_nugget", 1)],
          rewards=[reward_item("undergarden:dweller_steak", 8), reward_xp(8)],
          deps=["meat"], icon="undergarden:raw_gloomper_leg"),

    quest("mobs_other", 15, -2.5, "&8Checkliste: Andere Gestalten",
          subtitle="Was sonst noch im Dunkeln läuft.",
          description=[
              "&6Rohling:&r Rohlingstoßzahn, daraus wird Knochenmehl.",
              "&6Verschollener:&r trägt Cloggrumwaffen, mit Glück eine Kampfaxt.",
              "&6Splugie:&r Tiefkiesel. &6Nargoyle&r und &6Gwibb:&r keine Beute.",
              "&6Einwohner:&r Geheimnisvolle Maske, nur in den Tiefen.",
              "&6Steingeborener:&r Tiefkiesel, besser mit ihm handeln.",
              "&6Vergessener Wächter:&r Vergessene Klumpen, siehe Katakomben.",
          ],
          tasks=[task_item("undergarden:brute_tusk", 1), task_kill("undergarden:forgotten", 1),
                 task_kill("undergarden:sploogie", 1), task_kill("undergarden:nargoyle", 1),
                 task_kill("undergarden:gwib", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["mobs_rot"], icon="undergarden:brute_tusk"),

    # ---- Katakomben ----------------------------------------------------------
    quest("catacombs", 5, 8.5, "&8&lBetritt die Katakomben",
          subtitle="Vergessene Hallen unter dem Vergessenen Feld.",
          description=[
              "Finde eine &6Katakombe&r: lange Gänge aus Tiefsteinziegeln mit Grabkammern und Altären. Geh hinein.",
              "",
              "&eIn den Truhen:&r Cloggrum- und Froststahlklumpen, Regalium, Scherben, Vergessene Klumpen und die &6Schmiedevorlage&r für die Vergessene Aufwertung. Nimm jede Vorlage mit.",
              "",
              "Hier wandern die &6Verschollenen&r. Geh mit voller Rüstung hinein und markier den Rückweg.",
          ],
          tasks=[task_advancement("undergarden:undergarden/catacombs", "Katakomben betreten")],
          rewards=[reward_item("minecraft:torch", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["cloggrum_gear"], icon="undergarden:depthrock_bricks", size=1.5, shape="hexagon"),

    quest("guardian", 7.5, 8.5, "&4&lBesiege den Vergessenen Wächter",
          subtitle="Der Boss der Katakomben.",
          description=[
              "Tief in den Katakomben steht der &4Vergessene Wächter&r, ein Koloss aus altem Metall. Erleg ihn, am besten zu zweit oder zu dritt.",
              "",
              "&eBeute:&r Nur wenn ein Spieler ihn tötet, fallen &e4 bis 16&r &6Vergessene Klumpen&r.",
              "",
              "&eKronwerke:&r Ein guter Anlass für einen gemeinsamen Ausflug auf Stream. Wer eine Katakombe findet, teilt die Koordinaten im Chat.",
          ],
          tasks=[task_kill("undergarden:forgotten_guardian", 1)],
          rewards=[reward_item("undergarden:forgotten_nugget", 9), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["catacombs"], icon="undergarden:forgotten_nugget", size=1.75, shape="diamond"),

    quest("forgotten_ingot", 10, 8.5, "&dSchmiede einen Vergessenen Barren",
          subtitle="Neun Klumpen, ein Barren.",
          description=[
              "Werkbank: &69 Vergessene Klumpen&r ergeben &61 Vergessenen Barren&r.",
              "",
              pic("undergarden:forgotten_ingot"),
              "",
              "Jeder Barren ist eine Aufwertung. Die Spitzhacke ist Pflicht, alles andere kommt danach.",
          ],
          tasks=[task_item("undergarden:forgotten_ingot", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(10)],
          deps=["guardian"], icon="undergarden:forgotten_ingot"),

    quest("forgotten", 12.5, 8.5, "&dWerte die Spitzhacke auf",
          subtitle="Der Schlüssel zu den Tiefen.",
          description=[
              "Schmiedetisch: &6Schmiedevorlage&r, &6Cloggrumspitzhacke&r, &6Vergessener Barren&r. Heraus kommt die &6Vergessene Spitzhacke&r.",
              "",
              "Nur Vergessenes Werkzeug baut den &6Furchtfels&r am Boden ab, darunter liegen die Tiefen. Vergessene Werkzeuge bauen Blöcke des Undergarden &e1,5-mal&r so schnell ab.",
              "",
              "&eVorlage kopieren:&r Vorlage, 7 Diamanten und 1 Tiefstein ergeben 2 Vorlagen.",
          ],
          tasks=[task_item("undergarden:forgotten_pickaxe", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(12)],
          deps=["forgotten_ingot"], icon="undergarden:forgotten_pickaxe"),

    quest("forgotten_arms", 15, 8.5, "&dSchmiede Vergessene Waffen",
          subtitle="Schwert und Kampfaxt.",
          description=[
              "Gleicher Weg am Schmiedetisch: Vorlage, &6Cloggrumschwert&r und Vergessener Barren ergeben das &6Vergessene Schwert&r.",
              "",
              "Vergessene Waffen machen gegen Undergarden-Mobs (außer Bossen) &e1,5-mal&r so viel Schaden. Die &6Vergessene Kampfaxt&r braucht eine Cloggrumkampfaxt, die nur Verschollene fallen lassen.",
              "",
              "Alle sechs zusammen sind ein Fortschritt: Axt, Kampfaxt, Hacke, Spitzhacke, Schaufel, Schwert.",
          ],
          tasks=[task_item("undergarden:forgotten_sword", 1)],
          rewards=[reward_item("undergarden:forgotten_nugget", 9), reward_xp(12)],
          deps=["forgotten"], icon="undergarden:forgotten_sword", optional=True),

    quest("minion", 12.5, 10.7, "&dRuf einen Vergessenen Diener",
          subtitle="Ein Wachposten wie ein Eisengolem.",
          description=[
              "Setz einen &6Geschnitzten Düsterkürbis&r auf einen &6Block aus Vergessenem Metall&r. Der Block kostet 9 Vergessene Barren.",
              "",
              "Der &6Vergessene Diener&r verteidigt seinen Platz mit Geschossen. Teuer, aber ein schöner Wächter fürs Portal.",
          ],
          tasks=[task_advancement("undergarden:undergarden/summon_minion", "Einen Vergessenen Diener erschaffen")],
          rewards=[reward_item("undergarden:forgotten_nugget", 9), reward_xp(10)],
          deps=["forgotten_ingot"], icon="undergarden:carved_gloomgourd", optional=True),

    # ---- Tiefen --------------------------------------------------------------
    quest("depths", 12.5, 13, "&5&lBrich in die Tiefen durch",
          subtitle="Unter dem Furchtfels.",
          description=[
              "Grab dich mit der Vergessenen Spitzhacke durch den &6Furchtfels&r am Boden der Welt. Darunter liegen die &5Tiefen&r und die &5Infizierten Tiefen&r. Bau &68 Rogdorium&r ab.",
              "",
              "&cDie Luft ist schlecht:&r Der Aufenthalt allein treibt die Utherische Infektion hoch, in den Infizierten Tiefen schneller. Bleib nicht länger als nötig.",
              "",
              "&6Rogdoriumerz&r liegt im Furchtfels von &eY -64 bis 0&r.",
          ],
          tasks=[task_advancement("undergarden:undergarden/enter_depths", "Die Tiefen betreten"), task_item("undergarden:rogdorium", 8)],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["forgotten"], icon="undergarden:rogdorium", size=1.75, shape="hexagon"),

    quest("cure", 10, 13, "&aDräng die Infektion zurück",
          subtitle="Rogdorium ist das Gegenmittel.",
          description=[
              "Iss ein Stück &6Rogdorium&r oder einen &6Rogdoriumklumpen&r, wenn die Infektion steigt. Ein Rogdorium ergibt 9 Klumpen.",
              "",
              "Der Effekt &6Reinheit&r senkt die Infektion jede Sekunde ein Stück. Trag auf jeder Tour ein paar Klumpen bei dir.",
          ],
          tasks=[task_advancement("undergarden:undergarden/cure_utheric_infection", "Die Infektion zurückdrängen")],
          rewards=[reward_item("undergarden:rogdorium", 4), reward_xp(5)],
          deps=["depths"], icon="undergarden:rogdorium_nugget"),

    quest("infuser", 15, 13, "&dBau den Infusionstisch",
          subtitle="Aus Haufen werden Kristalle.",
          description=[
              "Werkbank: &65 Furchtfels&r, &61 Rogdorium&r und &61 Utherischer Haufen&r ergeben den &6Infusionstisch&r. Er läuft mit Rogdorium.",
              "",
              "&eWofür:&r Ein Utherischer Haufen wird darin in 10 Sekunden zum &6Utheriumkristall&r. Rüstung kannst du darin mit Rogdorium infundieren.",
          ],
          tasks=[task_item("undergarden:infuser", 1), task_item("undergarden:utherium_crystal", 8)],
          rewards=[reward_item("undergarden:utheric_cluster", 4), reward_xp(15)],
          deps=["depths", "utherium"], icon="undergarden:infuser", size=1.5),

    quest("utherium_gear", 17.5, 13, "&cSchmiede ein Utheriumschwert",
          subtitle="Die Waffe gegen Moderwesen.",
          description=[
              "Werkbank: &62 Utheriumkristalle&r über &61 Stock&r ergeben das &6Utheriumschwert&r.",
              "",
              pic("undergarden:utherium_crystal"),
              "",
              "Utheriumwaffen machen gegen Moderwesen &e1,5-mal&r so viel Schaden. Werkzeug und Rüstung aus Utherium gibt es auch. Alte Utheriumteile werden im Hochofen wieder zu Kristallen.",
          ],
          tasks=[task_item("undergarden:utherium_sword", 1)],
          rewards=[reward_item("undergarden:utherium_crystal", 4), reward_xp(15)],
          deps=["infuser"], icon="undergarden:utherium_sword"),

    quest("denizen", 12.5, 15.2, "&6Find ein Einwohnercamp",
          subtitle="Die Bewohner der Tiefen.",
          description=[
              "In den Tiefen leben die &6Einwohner&r in Lagern mit Lagerfeuer. Finde eines.",
              "",
              "&cZerstör nicht ihr Lagerfeuer:&r Das bringt alle in der Nähe gegen dich auf.",
              "",
              "In den Truhen der Camps liegen Geheimnisvolle Masken und Totems. Einen Totem machst du auch selbst: eine Uralte Wurzel 10 Sekunden in den Infusionstisch.",
          ],
          tasks=[task_advancement("undergarden:undergarden/enter_denizen_camp", "Ein Einwohnercamp finden")],
          rewards=[reward_item("undergarden:rogdorium", 4), reward_xp(10)],
          deps=["depths"], icon="undergarden:denizen_mask", optional=True),

    # ---- Abschluss -----------------------------------------------------------
    quest("collection", 20, 6, "&2&lSammle die Schätze der Tiefe",
          subtitle="Von jedem Erz einen Block.",
          description=[
              "Je ein Block aus &6Cloggrum&r, &6Froststahl&r, &6Utherium&r, &6Regalium&r und &6Rogdorium&r, jeweils aus 9 Barren oder Kristallen.",
              "",
              "&eKronwerke:&r Der Undergarden hat sehr viel &6Kohle&r im Tiefstein. Kohle wird im Koksofen zu Koks, und Koks braucht jeder Hochofen für den Stahl. Für die &e4.000 Stahlbarren&r des Stufenziels \"Der Ofen schläft nie\" ist das ein guter zweiter Bergbauplatz.",
          ],
          tasks=[task_item("undergarden:cloggrum_block", 1), task_item("undergarden:froststeel_block", 1),
                 task_item("undergarden:utherium_block", 1), task_item("undergarden:regalium_block", 1),
                 task_item("undergarden:rogdorium_block", 1)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:diamond", 4), reward_xp(25)],
          deps=["utherium_gear", "ore_list"], icon="undergarden:utherium_block", size=2.5, shape="gear"),
]

images = [
    banner("undergarden/title", "Der Undergarden", 10, -8.6, height=1.75, kind="title", colour="nature"),
    banner("undergarden/arrival", "Anreise", 1.25, -1.6, height=0.9, colour="nature"),
    banner("undergarden/survival", "Überleben", 8.75, -6.5, height=0.9, colour="stone"),
    banner("undergarden/ores", "Erze", 11.25, -1.1, height=0.9, colour="stone"),
    banner("undergarden/biomes", "Biome", 6.25, 3.8, height=0.9, colour="nature"),
    banner("undergarden/catacombs", "Katakomben", 10, 7.2, height=0.9, colour="stone"),
    banner("undergarden/depths", "Die Tiefen", 13.75, 11.7, height=0.9, colour="magic"),
]

chapter(C, "Der Undergarden", "undergarden:catalyst", "world", quests, shape="circle", order=30, stage=3,
        subtitle=["Stufe 3: Katalysator und Portal, vier neue Erze, die Moderwesen, die Katakomben und der Weg in die Tiefen."],
        images=images)
