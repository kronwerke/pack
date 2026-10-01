"""The Undergarden: opened with stage 3. The catalyst and the portal, surviving in the dark,
the four ores (cloggrum, froststeel, utherium, regalium), the Rotspawn and the Utheric
infection, the catacombs with the Forgotten Guardian, and the Depths with rogdorium and
the infuser."""
from ftbq import (chapter, quest, task_item, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "undergarden"

quests = [
    # ---- Anreise -------------------------------------------------------------
    quest("catalyst", 0, 6.5, "&2&lDer Katalysator",
          subtitle="Kupfer, Stein und eine Enderperle.",
          description=[
              "Der &2Undergarden&r ist eine eigene Dimension tief unter der Oberwelt: dunkel, feucht, voller Pilze und Dinge, die dich fressen wollen. Mit &eStufe 3&r ist er offen.",
              "",
              "&eDer Schlüssel:&r Der &6Katalysator&r entsteht an der Werkbank. Vier &6Kupferbarren&r in die Ecken, vier &6Stein&r an die Seiten und eine &6Enderperle&r in die Mitte.",
              "",
              "&eDas Portal:&r Bau einen Rahmen wie für ein Netherportal, aber aus &6Steinziegeln&r. Rissige, bemooste und gemeißelte Steinziegel gehen auch, ebenso Tiefschieferziegel und Tiefschieferfliesen. Dann klickst du mit dem Katalysator in der Hand auf den Rahmen, und das Portal öffnet sich.",
              "",
              img(item_texture("undergarden:catalyst"), 32, 32),
          ],
          tasks=[task_item("undergarden:catalyst", 1)],
          rewards=[reward_item("minecraft:stone_bricks", 16), reward_table("s3_common")],
          icon="undergarden:catalyst", size=2.0, shape="hexagon"),

    quest("arrival", 2.8, 6.5, "&2Hinunter",
          subtitle="Hier ist immer Nacht.",
          description=[
              "Geh durch das Portal. Auf der anderen Seite entsteht ein Gegenstück, meist in einer Höhle aus &6Tiefstein&r.",
              "",
              "&eWas anders ist:&r Es gibt keinen Himmel und keine Sonne, nur schwaches Licht. Monster spawnen überall, wo kein Blocklicht hinkommt. Jede Fackel hilft, also nimm reichlich mit.",
              "",
              "&eBetten&r funktionieren hier, anders als im Nether. Stell dir gleich eines neben das Portal, dann wachst du nach einem Tod nicht in der Oberwelt auf.",
              "",
              "&eEntfernungen:&r Ein Block im Undergarden entspricht vier Blöcken in der Oberwelt. Für weite Reisen taugt er also auch, nur gemütlicher wird es dadurch nicht.",
          ],
          tasks=[task_dimension("undergarden:undergarden")],
          rewards=[reward_item("minecraft:torch", 64), reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["catalyst"], icon="undergarden:depthrock", size=1.75, shape="hexagon"),

    # ---- Überleben -----------------------------------------------------------
    quest("food", 5.5, 1.5, "&aWas man hier essen kann",
          subtitle="Bohnen, Kürbisse und Schlafffrüchte.",
          description=[
              "Kühe gibt es hier unten nicht, satt wirst du trotzdem:",
              "",
              "&6Unterbohnen&r wachsen an kleinen Büschen am Boden. Roh geht, gebraten sind sie besser.",
              "&6Düsterkürbisse&r liegen lila im Gras. Aus einem Kürbis werden Kerne zum Anpflanzen, mit einem Pilz und Glitzerseetang ein &6Düsterkürbiskuchen&r.",
              "&6Schlafffrüchte&r hängen an den leuchtenden Schlaffranken, die von der Decke baumeln.",
              "",
              "&eFleisch:&r Die großen &6Bewohner&r und die hüpfenden &6Gloomper&r lassen Fleisch und Leder fallen. Einen gesattelten Bewohner kannst du reiten und mit einer &6Unterbohne am Stock&r lenken.",
          ],
          tasks=[task_item("undergarden:underbeans", 16), task_item("undergarden:gloomgourd", 4)],
          rewards=[reward_item("undergarden:gloomgourd_seeds", 4), reward_xp(5)],
          deps=["arrival"], icon="undergarden:underbeans"),

    quest("rotspawn", 8, 1.5, "&4Moderwesen",
          subtitle="Die eigentlichen Bewohner.",
          description=[
              "Die &4Moderwesen&r sind die Monster des Undergarden: der kleine &6Moderling&r, der &6Moderläufer&r, das schwere &6Moderbiest&r und der &6Moderspeier&r, der aus der Entfernung spuckt.",
              "",
              "&cDie Utherische Infektion:&r Jeder Treffer eines Moderwesens steckt dich ein Stück weiter an. Wird die Infektion zu stark, wird es lebensgefährlich. Bleib also auf Abstand und lauf nicht in Gruppen hinein.",
              "",
              "Moderwesen lassen &6Utherische Scherben&r fallen. Die brauchst du für die nächste Quest.",
          ],
          tasks=[task_kill("undergarden:rotling", 5), task_item("undergarden:utheric_shard", 8)],
          rewards=[reward_item("minecraft:arrow", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["food"], icon="undergarden:utheric_shard"),

    quest("shard_torch", 10.5, 1.5, "&bScherbenfackel",
          subtitle="Licht, das zurückbeißt.",
          description=[
              "Eine &6Utherische Scherbe&r auf einem Stock ergibt eine &6Scherbenfackel&r. Sie leuchtet wie eine normale Fackel und fügt Moderwesen in ihrer Nähe Schaden zu.",
              "",
              "Ein paar davon um dein Portal, deinen Schlafplatz und deine Schächte, und die Nächte werden ruhiger. Die ewigen Nächte, genauer gesagt.",
          ],
          tasks=[task_item("undergarden:shard_torch", 8)],
          rewards=[reward_item("undergarden:utheric_shard", 4)],
          deps=["rotspawn"]),

    # ---- Erze ----------------------------------------------------------------
    quest("cloggrum", 5.5, 6.5, "&7&lCloggrum",
          subtitle="Das Eisen des Undergarden.",
          description=[
              "&6Cloggrum&r steckt überall im Tiefstein und im Schlotterstein, auf jeder Höhe. Das Erz liefert &6Rohcloggrum&r, im Ofen wird daraus ein Barren.",
              "",
              "Aus Cloggrum machst du Werkzeug, Rüstung, Eimer, Laternen und Gitter. Die &6Mampfer&r, kleine Gesteinsfresser, lassen manchmal Cloggrum- und Froststahlklumpen fallen.",
              "",
              img(item_texture("undergarden:cloggrum_ingot"), 32, 32),
          ],
          tasks=[task_item("undergarden:raw_cloggrum", 16), task_item("undergarden:cloggrum_ingot", 16)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(5)],
          deps=["arrival"], icon="undergarden:cloggrum_ingot", size=1.5),

    quest("cloggrum_gear", 5.5, 9, "&7Ausrüstung aus Cloggrum",
          subtitle="Bewahr die Spitzhacke gut auf.",
          description=[
              "Eine &6Cloggrumspitzhacke&r reicht für alle Erze, die du bis jetzt kennst. Behalte sie, denn später wertest du sie zu einer Vergessenen Spitzhacke auf, und nur mit der kommst du in die Tiefen.",
              "",
              "Die &6Cloggrumrüstung&r ist ein ordentlicher Schutz. Die Stiefel haben einen Vorteil: Mit ihnen bremst dich der Schleim der Skintlinge nicht.",
          ],
          tasks=[task_item("undergarden:cloggrum_pickaxe", 1), task_item("undergarden:cloggrum_chestplate", 1)],
          rewards=[reward_item("undergarden:cloggrum_ingot", 8)],
          deps=["cloggrum"], icon="undergarden:cloggrum_pickaxe"),

    quest("froststeel", 8, 6.5, "&bFroststahl",
          subtitle="Nur dort, wo es friert.",
          description=[
              "&6Froststahl&r gibt es nur im &6Schlotterstein&r der kalten Biome: in den Frostfeldern, im Eisigen Smogstielwald und am Eisigen See. Das Erz liefert &6Rohfroststahl&r.",
              "",
              "Waffen aus Froststahl verlangsamen jedes Ziel, das sie treffen. Gegen schnelle Gegner ist das viel wert.",
          ],
          tasks=[task_item("undergarden:raw_froststeel", 8), task_item("undergarden:froststeel_ingot", 8)],
          rewards=[reward_item("minecraft:packed_ice", 8), reward_xp(5)],
          deps=["cloggrum"], icon="undergarden:froststeel_ingot"),

    quest("utherium", 10.5, 6.5, "&cUtherium",
          subtitle="Tief unten, und noch nicht fertig.",
          description=[
              "&6Utheriumerz&r findest du unterhalb von &eY 32&r. Es liefert keinen fertigen Kristall, sondern einen &6Utherischen Haufen&r. Neun Utherische Scherben von Moderwesen ergeben ebenfalls einen Haufen.",
              "",
              "Zum &6Utheriumkristall&r wird der Haufen erst im &6Infusionstisch&r, und den baust du mit Rogdorium aus den Tiefen. Sammle also schon einmal, verarbeiten kannst du später.",
              "",
              "Waffen aus Utherium machen gegen Moderwesen anderthalbfachen Schaden.",
          ],
          tasks=[task_item("undergarden:utheric_cluster", 4)],
          rewards=[reward_xp(10)],
          deps=["froststeel"], icon="undergarden:utheric_cluster"),

    quest("regalium", 13, 6.5, "&eRegalium",
          subtitle="Selten, und hier unten Geld.",
          description=[
              "&6Regaliumerz&r liegt ganz unten zwischen &eY 0 und Y 12&r, nur ein paar Adern pro Chunk. Es liefert &6Regaliumkristalle&r.",
              "",
              "Für Werkzeug taugt Regalium nicht. Es ist die Währung der &6Steingeborenen&r, und neun Kristalle ergeben einen Block für deine Sammlung.",
          ],
          tasks=[task_item("undergarden:regalium_crystal", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(10)],
          deps=["utherium"], icon="undergarden:regalium_crystal"),

    quest("stoneborn", 15.5, 6.5, "&8Steingeborene",
          subtitle="Händler aus Stein.",
          description=[
              "&6Steingeborene&r sind große Gestalten aus Stein, die durch den Undergarden wandern. Mit Rechtsklick handelst du mit ihnen, bezahlt wird mit &6Regalium&r.",
              "",
              "&cGreif sie nicht an:&r Wer einen angreift, hat schnell alle in der Nähe gegen sich, und sie schlagen hart zu.",
          ],
          tasks=[task_advancement("undergarden:undergarden/stoneborn_trade", "Mit einem Steingeborenen handeln")],
          rewards=[reward_item("undergarden:regalium_crystal", 4), reward_xp(5)],
          deps=["regalium"], icon="undergarden:depthrock_pebble", optional=True),

    # ---- Katakomben und Tiefen -----------------------------------------------
    quest("catacombs", 5.5, 13.5, "&8&lDie Katakomben",
          subtitle="Vergessene Hallen.",
          description=[
              "Die &6Katakomben&r sind lange Gänge aus Tiefsteinziegeln, mit Grabkammern, Altären und Truhen. In ihnen wandern die &6Verschollenen&r, untote Gestalten mit Cloggrumwaffen. Mit Glück lassen sie eine &6Cloggrumkampfaxt&r fallen.",
              "",
              "&eIn den Truhen&r liegen Cloggrum- und Froststahlklumpen, Regalium, Utherische Scherben, Vergessene Klumpen und die &6Schmiedevorlage&r für die Vergessene Aufwertung. Die Vorlage ist das Wichtigste, nimm jede mit.",
              "",
              "Geh mit voller Ausrüstung und Essen hinein und markier dir den Rückweg.",
          ],
          tasks=[task_advancement("undergarden:undergarden/catacombs", "Katakomben betreten")],
          rewards=[reward_item("minecraft:torch", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["cloggrum_gear"], icon="undergarden:depthrock_bricks", size=1.5, shape="hexagon"),

    quest("guardian", 8, 13.5, "&4&lVergessener Wächter",
          subtitle="Der Boss der Katakomben.",
          description=[
              "Tief in den Katakomben steht der &4Vergessene Wächter&r, ein Koloss aus altem Metall. Er schlägt hart und hält viel aus. Geht am besten zu zweit oder zu dritt.",
              "",
              "&eBeute:&r Wenn ein Spieler ihn erlegt, lässt er vier bis sechzehn &6Vergessene Klumpen&r fallen. Neun Klumpen ergeben einen &6Vergessenen Barren&r.",
              "",
              "&eKronwerke:&r Ein Wächter ist ein guter Anlass für einen gemeinsamen Ausflug auf Stream. Wer eine Katakombe gefunden hat, teilt die Koordinaten im Chat.",
          ],
          tasks=[task_kill("undergarden:forgotten_guardian", 1)],
          rewards=[reward_item("undergarden:forgotten_nugget", 9), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["catacombs"], icon="undergarden:forgotten_nugget", size=1.75, shape="diamond"),

    quest("forgotten", 10.5, 13.5, "&dVergessene Spitzhacke",
          subtitle="Der Schlüssel zu den Tiefen.",
          description=[
              "Am &6Schmiedetisch&r legst du die &6Schmiedevorlage&r, ein &6Cloggrumwerkzeug&r und einen &6Vergessenen Barren&r zusammen. Heraus kommt das Vergessene Gegenstück.",
              "",
              "&eWarum das wichtig ist:&r Den &6Furchtfels&r ganz unten im Undergarden kann nur Vergessenes Werkzeug abbauen. Darunter liegen die Tiefen.",
              "",
              "Vergessene Werkzeuge bauen alle Blöcke des Undergarden anderthalbmal so schnell ab, Vergessene Waffen machen gegen seine Bewohner anderthalbfachen Schaden. Eine Vorlage kopierst du mit sieben Diamanten und einem Tiefstein, das ergibt zwei.",
          ],
          tasks=[task_item("undergarden:forgotten_ingot", 1), task_item("undergarden:forgotten_pickaxe", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(10)],
          deps=["guardian"], icon="undergarden:forgotten_pickaxe"),

    quest("depths", 13, 13.5, "&5&lDie Tiefen",
          subtitle="Unter dem Furchtfels.",
          description=[
              "Grab dich mit der Vergessenen Spitzhacke durch den &6Furchtfels&r am Boden der Welt. Darunter liegen die &5Tiefen&r und die &5Infizierten Tiefen&r.",
              "",
              "&cDie Luft ist schlecht:&r Allein der Aufenthalt in den Tiefen treibt die Utherische Infektion langsam nach oben, in den Infizierten Tiefen schneller. Bleib nicht länger als nötig.",
              "",
              "Hier wächst &6Rogdorium&r im Furchtfels. Rogdorium ist das Gegenmittel zur Infektion und der Brennstoff für den Infusionstisch.",
          ],
          tasks=[task_advancement("undergarden:undergarden/enter_depths", "Die Tiefen betreten"), task_item("undergarden:rogdorium", 8)],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["forgotten"], icon="undergarden:rogdorium", size=1.75, shape="hexagon"),

    quest("cure", 13, 16, "&aGegengift",
          subtitle="Rogdorium hält die Infektion zurück.",
          description=[
              "Wenn die Infektion steigt, iss ein Stück &6Rogdorium&r oder einen Rogdoriumklumpen. Es drängt sie zurück. Der Effekt &6Reinheit&r tut dasselbe über eine längere Zeit.",
              "",
              "Trag auf jeder Tour in die Tiefen ein paar Klumpen bei dir. Ein Barren ergibt neun davon.",
          ],
          tasks=[task_advancement("undergarden:undergarden/cure_utheric_infection", "Die Infektion zurückdrängen")],
          rewards=[reward_item("undergarden:rogdorium", 4)],
          deps=["depths"], icon="undergarden:rogdorium", optional=True),

    quest("infuser", 15.5, 13.5, "&dDer Infusionstisch",
          subtitle="Aus Haufen werden Kristalle.",
          description=[
              "Der &6Infusionstisch&r besteht aus &6Furchtfels&r, einem &6Rogdorium&r und einem &6Utherischen Haufen&r. Er läuft mit Rogdorium als Brennstoff.",
              "",
              "&eWofür:&r Er reinigt Utherische Haufen zu &6Utheriumkristallen&r, aus denen du Utheriumwerkzeug und Utheriumrüstung machst. Auch Rüstung kannst du darin mit Rogdorium infundieren.",
              "",
              img(item_texture("undergarden:utherium_crystal"), 32, 32),
          ],
          tasks=[task_item("undergarden:infuser", 1), task_item("undergarden:utherium_crystal", 8)],
          rewards=[reward_item("undergarden:utheric_cluster", 4), reward_xp(15)],
          deps=["depths", "utherium"], icon="undergarden:infuser", size=1.5),

    # ---- Abschluss -----------------------------------------------------------
    quest("collection", 19, 10, "&2&lSchätze der Tiefe",
          subtitle="Von jedem Erz einen Block.",
          description=[
              "Du kennst jetzt alles, was der Undergarden zu bieten hat. Zum Abschluss je ein Block aus &6Cloggrum&r, &6Froststahl&r, &6Utherium&r, &6Regalium&r und &6Rogdorium&r.",
              "",
              "&eKronwerke:&r Der Undergarden hat sehr viel &6Kohleerz&r im Tiefstein. Kohle wird im Koksofen zu Koks, und Koks braucht jeder Hochofen und jeder Lichtbogenofen für den Stahl. Für die &e4.000 Stahlbarren&r des Stufenziels \"Der Ofen schläft nie\" ist das ein guter zweiter Bergbauplatz.",
          ],
          tasks=[task_item("undergarden:cloggrum_block", 1), task_item("undergarden:froststeel_block", 1),
                 task_item("undergarden:utherium_block", 1), task_item("undergarden:regalium_block", 1),
                 task_item("undergarden:rogdorium_block", 1)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:diamond", 4), reward_xp(25)],
          deps=["infuser", "regalium"], icon="undergarden:utherium_block", size=2.5, shape="gear"),
]

images = [
    banner("undergarden/title", "Der Undergarden", 9, -2.6, height=1.75, kind="title", colour="nature"),
    banner("undergarden/arrival", "Anreise", 1.4, 3.6, height=0.9, colour="nature"),
    banner("undergarden/survival", "Überleben", 8, -0.4, height=0.9, colour="stone"),
    banner("undergarden/ores", "Erze", 10.5, 4.5, height=0.9, colour="stone"),
    banner("undergarden/depths", "Katakomben und Tiefen", 9.5, 11.4, height=0.9, colour="magic"),
]

chapter(C, "Der Undergarden", "undergarden:catalyst", "world", quests, shape="circle", order=30, stage=3,
        subtitle=["Stufe 3: Katalysator und Portal, vier neue Erze, die Moderwesen und der Weg in die Tiefen."],
        images=images)
