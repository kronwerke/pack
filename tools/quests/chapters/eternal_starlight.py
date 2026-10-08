"""Eternal Starlight, opened with stage 4: the Gatekeeper and the Orb of Prophecy, the portal,
the biomes one quest each with what they give, the ores one step each plus a checklist with Y
ranges, the scythes and the hammer, mob checklists with drops, and the three bosses in order
(Starlight Golem, Permafrost, Lunar Monstrosity), each with a preparation and a kill quest.
The mod ships no German lang file, so item names stay English. Facts come from the mod jar
(worldgen, loot tables, recipes, advancements, the in-jar book). The dimension runs from
Y -64 to Y 319."""
from ftbq import (chapter, quest, task_item, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "eternal_starlight"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Der Weg hinein ------------------------------------------------------
    quest("orb", 0, 0, "&b&lBesiege den Gatekeeper",
          subtitle="Er gibt dir die Orb of Prophecy.",
          description=[
              "Finde in der Oberwelt eine &6Portalruine&r mit einem Rahmen aus &6Chiseled Voidstone&r. Sprich den &bGatekeeper&r an, wähl &eChallenge&r und besiege ihn. Er lässt die &bOrb of Prophecy&r fallen.",
              "",
              pic("eternal_starlight:orb_of_prophecy"),
              "",
              "Er pariert Angriffe und wirft Feuerbälle. Komm mit guter Rüstung und Essen. Seine Beute: das Buch der Dimension, Glistering-Waffen, Seeking Eyes.",
              "",
              "Ruinen gibt es in Ebenen, Savannen, Wäldern, Wüsten, im Dschungel und in kalten Biomen.",
          ],
          tasks=[task_item("eternal_starlight:orb_of_prophecy", 1)],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          icon="eternal_starlight:orb_of_prophecy", size=2.0, shape="hexagon"),

    quest("portal", 2.5, 0, "&b&lÖffne das Portal",
          subtitle="Die Kugel auf den Rahmen.",
          description=[
              "Rechtsklick mit der &bOrb of Prophecy&r auf den Rahmen aus Chiseled Voidstone. Geh hindurch.",
              "",
              "&eDrüben&r ist immer Nacht. Am häufigsten sind &6Nightfall Spiders&r und &6Lonestar Skeletons&r. Bau dir am Portal einen hellen, sicheren Raum. Betten funktionieren.",
              "",
              "&eNeue Kugel:&r Werkbank, &65 Blue Starlight Crystal Shards&r als Kreuz, &64 Glas&r in die Ecken.",
          ],
          tasks=[task_dimension("eternal_starlight:starlight")],
          rewards=[reward_item("minecraft:torch", 64), reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["orb"], icon="eternal_starlight:chiseled_voidstone", size=1.75, shape="hexagon"),

    quest("seeking_eye", -1, 2, "&dFolg einem Seeking Eye",
          subtitle="Zeigt dir Bauwerke und Biome.",
          description=[
              "Werkbank: &68 Starlight Flowers&r um eine &6Enderperle&r ergeben &616 Seeking Eyes&r. Rechtsklick öffnet eine Sternenkarte, dort wählst du ein Ziel. Das Auge schwebt voraus.",
              "",
              "Klick es an, um es zurückzuholen. Dabei kann es zerbrechen. Seeker, Thirst Walker und Twilight Gaze lassen auch Augen fallen.",
          ],
          tasks=[task_item("eternal_starlight:seeking_eye", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["portal"], icon="eternal_starlight:seeking_eye"),

    # ---- Biome ---------------------------------------------------------------
    quest("forests", 5, -6, "&aFäll Lunar-Bäume",
          subtitle="Die Wälder der Sternenwelt.",
          description=[
              "Fäll &616 Lunar Logs&r. Die hohen Lunar-Bäume stehen in fast allen Wäldern.",
              "",
              "&eDie Waldbiome:&r &6Starlight Forest&r, &6Starlight Dense Forest&r, &6Umbral Plains&r, &6Glimmer Scrubland&r, &6Scarlet Forest&r, &6Starlight Taiga&r und &6Torreya Forest&r.",
          ],
          tasks=[task_item("eternal_starlight:lunar_log", 16)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(5)],
          deps=["portal"], icon="eternal_starlight:lunar_log"),

    quest("starfire", 7.5, -6, "&6Hol Starfire",
          subtitle="Ein Geschenk der Starfire Birds.",
          description=[
              "Leg &6Samen&r in ein Nest der &6Starfire Birds&r. Die Nester sitzen in den Kronen der Lunar-Bäume. Die Vögel belohnen dich, unter anderem mit &6Starfire&r.",
              "",
              "Starfire wirfst du als Waffe, damit wertest du Thermal-Springstone-Ausrüstung auf, und auf Twilight Sand geworfen entsteht &6Raw Flowglaze&r.",
          ],
          tasks=[task_advancement("eternal_starlight:put_seeds_into_starfire_bird_nest", "Samen in ein Nest legen"), task_item("eternal_starlight:starfire", 4)],
          rewards=[reward_item("minecraft:wheat_seeds", 32), reward_xp(8)],
          deps=["forests"], icon="eternal_starlight:starfire"),

    quest("torreya", 10, -6, "&6Zapf Amaramber",
          subtitle="Harz aus den Torreya-Bäumen.",
          description=[
              "Entrinde &6Torreya Logs&r mit der Axt. Manchmal fällt &6Raw Amaramber&r ab. Auch ein abgebautes Torreya-Lagerfeuer gibt welches. Sammle 9.",
              "",
              "Die Torreya-Bäume stehen nur im &6Torreya Forest&r.",
          ],
          tasks=[task_item("eternal_starlight:raw_amaramber", 9)],
          rewards=[reward_item("minecraft:string", 8), reward_xp(8)],
          deps=["forests"], icon="eternal_starlight:raw_amaramber"),

    quest("amaramber_light", 12.5, -6, "&6Stell Amaramber-Kerzen auf",
          subtitle="Licht, bei dem keine Monster spawnen.",
          description=[
              "Werkbank: &61 Faden&r über &61 Raw Amaramber&r ergibt eine &6Amaramber Candle&r. Stell sie an und zünde sie an.",
              "",
              "In dieser Dimension halten brennende Amaramber-Kerzen, Amaramber-Laternen, Torreya-Lagerfeuer und Amaramber-Feuer feindliche Monster in der Nähe vom Spawnen ab. Für eine Basis hier ist das Gold wert.",
          ],
          tasks=[task_item("eternal_starlight:amaramber_candle", 8)],
          rewards=[reward_item("eternal_starlight:raw_amaramber", 4), reward_xp(8)],
          deps=["torreya"], icon="eternal_starlight:amaramber_candle"),

    quest("desert", 5, -4, "&bPlünder die Kristallwüste",
          subtitle="Blaue und rote Starlight-Kristalle.",
          description=[
              "Bau in der &6Crystallized Desert&r Kristallhaufen ab und sammle &616 Blue Starlight Crystal Shards&r. Daraus werden neue Orbs of Prophecy.",
              "",
              "&eUnter der Wüste&r jagen &6Crystallized Moths&r mit Schallwellen, die kein Schild aufhält. Mit genug Fleisch kannst du sie zähmen.",
          ],
          tasks=[task_item("eternal_starlight:blue_starlight_crystal_shard", 16)],
          rewards=[reward_item("minecraft:glass", 16), reward_xp(8)],
          deps=["portal"], icon="eternal_starlight:blue_starlight_crystal_shard"),

    quest("dagger", 7.5, -4, "&cBau den Dagger of Hunger",
          subtitle="Ein Zahn vom Thirst Walker.",
          description=[
              "Werkbank: &62 Tooth of Hunger&r übereinander auf &61 Stock&r ergeben den &6Dagger of Hunger&r.",
              "",
              "&eDen Zahn holen:&r &6Thirst Walker&r schleichen sich in der Wüste an, beißen und rennen weg. Blockst du den Biss mit einem Schild, verlieren sie einen Zahn. Getötet lassen sie auch einen fallen.",
              "",
              "Der Dolch wird durch Treffer satt und dabei stärker.",
          ],
          tasks=[task_item("eternal_starlight:dagger_of_hunger", 1)],
          rewards=[reward_item("eternal_starlight:tooth_of_hunger", 2), reward_xp(10)],
          deps=["desert"], icon="eternal_starlight:dagger_of_hunger"),

    quest("swamp", 10, -4, "&2Grab Malarit im Sumpf",
          subtitle="Nur im Dark Swamp.",
          description=[
              "Bau &68 Malarite&r ab. Das Erz gibt es nur im &6Dark Swamp&r, von &eY -64&r bis an die Oberfläche.",
              "",
              "Malarit wird zu Waffen, Werkzeugen, Pfeilen und einem Speer. &6Pungency Fruit&r wächst überall im Sumpf, riecht nach Knoblauch und taugt auch als Waffe.",
          ],
          tasks=[task_item("eternal_starlight:malarite", 8)],
          rewards=[reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:malarite"),

    quest("stranghoul", 10, -3, "&2Heuer einen Stranghoul an",
          subtitle="Eine Schüssel Eintopf, ein Tag Begleitschutz.",
          description=[
              "Gib einem &6Stranghoul&r eine Schüssel &6Pungency Stew&r. Dann kämpft er einen Tag lang für dich.",
              "",
              "Stranghouls leben im Sumpf in eigenen Höhlen und tauschen auch gegen Malarit. Aber: Wer schwer verletzt in ihrer Nähe steht, sieht für sie aus wie Futter. Silberwaffen fürchten sie.",
          ],
          tasks=[task_advancement("eternal_starlight:hire_stranghoul", "Einen Stranghoul anheuern")],
          rewards=[reward_item("eternal_starlight:malarite", 4), reward_xp(8)],
          deps=["swamp"], icon="eternal_starlight:pungency_stew", optional=True),

    quest("permafrost_forest", 5, -3, "&fSchmelz Glacite",
          subtitle="Das Eis des ewigen Frosts.",
          description=[
              "Bau &6Glacite&r ab und schmelz es im Ofen zu &68 Glacite Shards&r. Glacite liegt im &6Starlight Permafrost Forest&r und auf den &6Permafrost Peaks&r, von &eY -64 bis 45&r.",
              "",
              "Daraus werden Rüstung (friert Angreifer ein), Werkzeug, Pfeile und mit Starcore die &6Frozen Bombs&r. Unter dem Wald liegt eine Schicht aus Ashen Snow.",
          ],
          tasks=[task_item("eternal_starlight:glacite_shard", 8)],
          rewards=[reward_item("minecraft:packed_ice", 8), reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:glacite_shard"),

    quest("meteor", 7.5, -3, "&eSammle Aethersent",
          subtitle="Erz, das vom Himmel fällt.",
          description=[
              "Warte auf einen &eMeteorschauer&r. Große Meteore schlagen ein und hinterlassen &6Raw Aethersent&r. Im Ofen wird daraus ein &6Aethersent Ingot&r. Sammle 4.",
              "",
              "Mit den Meteoren fallen &6Creteors&r herunter, sternförmige Creeper. Ein &6Aethersent Golem&r (geschnitzte Lunaris-Kaktusfrucht auf einem Aethersent-Block) schießt Meteore ab, bevor sie einschlagen.",
          ],
          tasks=[task_item("eternal_starlight:aethersent_ingot", 4)],
          rewards=[reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:aethersent_ingot", optional=True),

    # ---- Erze ----------------------------------------------------------------
    quest("deepsilver", 5, 1.5, "&7&lSchmelz Deepsilver",
          subtitle="Das Eisen der Sternenwelt.",
          description=[
              "Bau &6Deepsilver-Erz&r im Voidstone oder Grimstone ab. Es gibt &6Raw Deepsilver&r, im Ofen wird daraus ein &6Deepsilver Ingot&r.",
              "",
              pic("eternal_starlight:deepsilver_ingot"),
              "",
              "Daraus werden Rüstung, Werkzeug, Schild, Eimer und Kessel. Im Legierungsofen geben 2 Raw Deepsilver und 1 Saltpeter Powder sogar 3 Barren.",
          ],
          tasks=[task_item("eternal_starlight:raw_deepsilver", 16), task_item("eternal_starlight:deepsilver_ingot", 16)],
          rewards=[reward_table("s4_common"), reward_xp(8)],
          deps=["portal"], icon="eternal_starlight:deepsilver_ingot", size=1.5),

    quest("starlit_diamond", 7.5, 1.5, "&bBau eine Starlit-Spitzhacke",
          subtitle="Diamanten unter den Sternen.",
          description=[
              "Bau &6Starlit Diamond Ore&r ab. Werkbank: &63 Starlit Diamonds&r und &62 Stöcke&r ergeben die &6Starlit Diamond Pickaxe&r.",
              "",
              "Rüstung und Werkzeug aus Starlit Diamond sind der nächste Schritt nach Deepsilver.",
          ],
          tasks=[task_item("eternal_starlight:starlit_diamond_pickaxe", 1)],
          rewards=[reward_item("eternal_starlight:starlit_diamond", 2), reward_xp(10)],
          deps=["deepsilver"], icon="eternal_starlight:starlit_diamond_pickaxe"),

    quest("springstone", 10, 1.5, "&cSchmelz Thermal Springstone",
          subtitle="Aus den heißen Quellen.",
          description=[
              "Bau &6Thermal Springstone&r an den &cheißen Quellen&r ab und schmelz ihn zu &68 Thermal Springstone Ingots&r.",
              "",
              "Daraus werden Rüstung (zündet Angreifer an), Werkzeug, eine Sense und ein Hammer. &eTipp:&r Die riesigen Pflanzen an den Quellen zerstört nur Feuer.",
          ],
          tasks=[task_item("eternal_starlight:thermal_springstone_ingot", 8)],
          rewards=[reward_xp(10)],
          deps=["starlit_diamond"], icon="eternal_starlight:thermal_springstone_ingot"),

    quest("ore_list", 12.5, 1.5, "&7&lCheckliste: Erze",
          subtitle="Jedes Erz mit Fundort und Höhe.",
          description=[
              "Hak jedes Erz einmal ab. Die Welt geht von &eY -64&r bis &eY 319&r.",
              "",
              "&6Deepsilver, Starlit Diamond, Starcore, Redstone, Saltpeter:&r überall, Y -64 bis Oberfläche. Unter Y 0 dichter, nur Saltpeter liegt oben dichter.",
              "&6Malarite:&r nur Dark Swamp, Y -64 bis Oberfläche.",
              "&6Glacite:&r nur Permafrost-Biome, Y -64 bis 45.",
              "&6Thermal Springstone:&r an heißen Quellen. &6Aethersent:&r aus Meteoren.",
          ],
          tasks=[task_item("eternal_starlight:raw_deepsilver", 1), task_item("eternal_starlight:starlit_diamond", 1),
                 task_item("eternal_starlight:starcore", 1), task_item("eternal_starlight:saltpeter_powder", 1),
                 task_item("eternal_starlight:malarite", 1), task_item("eternal_starlight:glacite", 1),
                 task_item("eternal_starlight:thermal_springstone", 1)],
          rewards=[reward_table("s4_common"), reward_xp(12)],
          deps=["springstone", "swamp", "permafrost_forest"], icon="eternal_starlight:starcore"),

    # ---- Sensen --------------------------------------------------------------
    quest("weapons", 10, 4, "&cBau eine Springstone-Sense",
          subtitle="Die erste Sense.",
          description=[
              "Werkbank: &63 Thermal Springstone Ingots&r oben, &62 Stöcke&r darunter, wie eine Spitzhacke. Das ergibt die &6Thermal Springstone Scythe&r.",
              "",
              "Sensen sind eine eigene Waffenart neben Schwert und Axt. Zubehör legst du wie in ein Bündel hinein. Geht das Teil kaputt, ist das Zubehör weg.",
          ],
          tasks=[task_item("eternal_starlight:thermal_springstone_scythe", 1)],
          rewards=[reward_item("eternal_starlight:thermal_springstone_ingot", 4), reward_xp(10)],
          deps=["springstone"], icon="eternal_starlight:thermal_springstone_scythe"),

    quest("glacite_scythe", 7.5, 4, "&fBau eine Glacite-Sense",
          subtitle="Gleiches Muster, anderes Material.",
          description=[
              "Werkbank: &63 Glacite Shards&r oben, &62 Stöcke&r darunter ergeben die &6Glacite Scythe&r.",
          ],
          tasks=[task_item("eternal_starlight:glacite_scythe", 1)],
          rewards=[reward_item("eternal_starlight:glacite_shard", 4), reward_xp(10)],
          deps=["permafrost_forest", "weapons"], icon="eternal_starlight:glacite_scythe"),

    quest("starfire_scythe", 12.5, 4, "&6Werte zur Starfire-Sense auf",
          subtitle="Springstone plus Starfire.",
          description=[
              "Schmiedetisch: &6Starfire Upgrade Smithing Template&r, &6Thermal Springstone Scythe&r, &6Starfire&r. Heraus kommt die &6Starfire Scythe&r.",
              "",
              "Die Vorlage liegt in den Truhen der Golemschmiede und des Cursed Garden. Kopieren: Vorlage, 7 Springstone-Barren und 1 Starcore-Block ergeben 2.",
          ],
          tasks=[task_item("eternal_starlight:starfire_scythe", 1)],
          rewards=[reward_item("eternal_starlight:starfire", 4), reward_xp(15)],
          deps=["weapons", "starfire", "forge"], icon="eternal_starlight:starfire_scythe"),

    quest("flowglaze_scythe", 5, 4, "&bWerte zur Flowglaze-Sense auf",
          subtitle="Glacite plus Flowglaze.",
          description=[
              "Schmiedetisch: &6Flowglaze Upgrade Smithing Template&r, &6Glacite Scythe&r, &6Flowglaze&r. Heraus kommt die &6Flowglaze Scythe&r.",
              "",
              "&6Flowglaze:&r Wirf Starfire auf Twilight Sand, bau den entstandenen Raw Flowglaze ab und schmelz ihn im Ofen. Flowglaze-Waffen werden stärker, je öfter du dasselbe Ziel hintereinander triffst.",
              "",
              "Die Vorlage liegt in den Truhen der Golemschmiede und des Cursed Garden. Kopieren: Vorlage, 7 Glacite Shards und 1 Eternal Ice ergeben 2.",
          ],
          tasks=[task_item("eternal_starlight:flowglaze_scythe", 1)],
          rewards=[reward_item("eternal_starlight:glacite_shard", 8), reward_xp(15)],
          deps=["glacite_scythe", "starfire", "forge"], icon="eternal_starlight:flowglaze_scythe"),

    quest("hammer", 10, 6.2, "&cSchlag mit dem Hammer zu",
          subtitle="Volle Kraft, kritischer Treffer.",
          description=[
              "Werkbank: &65 Thermal Springstone Ingots&r und &62 Stöcke&r ergeben den &6Thermal Springstone Hammer&r. Lös seinen Spezialangriff aus: ein kritischer Treffer mit voller Schlagkraft, also im Fallen.",
          ],
          tasks=[task_item("eternal_starlight:thermal_springstone_hammer", 1), task_advancement("eternal_starlight:hammer_critical_hit", "Den Spezialangriff auslösen")],
          rewards=[reward_item("eternal_starlight:thermal_springstone_ingot", 4), reward_xp(10)],
          deps=["weapons"], icon="eternal_starlight:thermal_springstone_hammer", optional=True),

    # ---- Mobs ----------------------------------------------------------------
    quest("mobs_hostile", 5, 7, "&4Checkliste: Feinde",
          subtitle="Jeder Feind mit seiner Beute.",
          description=[
              "&6Nightfall Spider:&r Faden, Nightfall Spider Eye.",
              "&6Lonestar Skeleton:&r Knochen, Deepsilver Nugget.",
              "&6Seeker:&r Seeker Tentacle, Seeking Eye. &6Thirst Walker:&r Tooth of Hunger.",
              "&6Creteor:&r Creteor Hide, Schwarzpulver, Raw Aethersent. &6Gleech:&r Gleech Egg.",
              "&6Stranghoul:&r Malarite, Pungency Fruit. &6Tangled:&r Soul Dew, Ranken.",
              "&6Freeze:&r Frozen Tube, Oxidized Golem Steel Nugget.",
          ],
          tasks=[task_kill("eternal_starlight:nightfall_spider", 1), task_kill("eternal_starlight:lonestar_skeleton", 1),
                 task_kill("eternal_starlight:seeker", 1), task_kill("eternal_starlight:thirst_walker", 1),
                 task_kill("eternal_starlight:creteor", 1), task_kill("eternal_starlight:gleech", 1),
                 task_kill("eternal_starlight:tangled", 1), task_kill("eternal_starlight:freeze", 1)],
          rewards=[reward_table("s4_common"), reward_xp(15)],
          deps=["seeking_eye"], icon="eternal_starlight:nightfall_spider_eye"),

    quest("mobs_animals", 7.5, 7, "&aCheckliste: Tiere",
          subtitle="Jedes Tier mit seiner Beute.",
          description=[
              "&6Aurora Deer:&r Steak, Leder. Gegen Stein gelenkt verliert er sein Geweih.",
              "&6Yeti:&r White Yeti Fur (auch mit der Schere), Faden.",
              "&6Ratlin:&r Ratlin Meat, Leder, Cave Moss. &6Shadow Snail:&r Fleisch, Schale.",
              "&6Ent:&r Lunar Berries. &6Crystallized Moth:&r Kristallsplitter, Shivering Gel.",
              "&6Rookfish:&r Rookfish, Air Sac. &6Luminofish&r und &6Luminaris:&r sich selbst.",
              "&6Twilight Gaze:&r Seeking Eye, Knochenmehl.",
          ],
          tasks=[task_item("eternal_starlight:aurora_deer_steak", 1), task_item("eternal_starlight:white_yeti_fur", 1),
                 task_item("eternal_starlight:ratlin_meat", 1), task_item("eternal_starlight:shadow_snail_shell", 1),
                 task_item("eternal_starlight:lunar_berries", 1), task_item("eternal_starlight:shivering_gel", 1),
                 task_item("eternal_starlight:rookfish_air_sac", 1), task_item("eternal_starlight:luminofish", 1)],
          rewards=[reward_item("minecraft:golden_carrot", 16), reward_xp(12)],
          deps=["mobs_hostile"], icon="eternal_starlight:aurora_deer_steak"),

    # ---- Bosse ---------------------------------------------------------------
    quest("forge", 16, -4, "&6Find eine Golemschmiede",
          subtitle="Vorbereitung für den ersten Boss.",
          description=[
              "Folg einem Seeking Eye zu einer &6Golem Forge&r und geh hinein. Sammle unterwegs &64 Frozen Tubes&r von den &6Freezes&r.",
              "",
              "&eWarum die Tubes:&r Eine Frozen Tube auf den Starlight Golem geworfen schickt ihn schneller in den Ladezustand. Die Freezes verursachen Erfrierungen, Rüstung gegen Kälte hilft.",
          ],
          tasks=[task_advancement("eternal_starlight:enter_golem_forge", "Eine Golemschmiede betreten"), task_item("eternal_starlight:frozen_tube", 4)],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          deps=["ore_list", "seeking_eye"], icon="eternal_starlight:frozen_tube", size=1.25),

    quest("golem", 18.5, -4, "&6&lBesiege den Starlight Golem",
          subtitle="Boss 1 von 3.",
          description=[
              "Sein Schild ist unzerstörbar und er bewegt sich nicht. Wenn er überhitzt und auflädt, schalte die &eEnergy Blocks&r in der Nähe ab. Dann fällt der Schild und du schlägst zu.",
              "",
              "&eBeute:&r &6Oxidized Golem Steel Ingots&r, &6Energy Sword&r, ein oxidierter Legierungsofen und eine Rüstungsverzierung.",
          ],
          tasks=[task_kill("eternal_starlight:starlight_golem", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["forge"], icon="eternal_starlight:energy_sword", size=1.75, shape="hexagon"),

    quest("golem_steel", 21, -4, "&6Schmelz Golem Steel",
          subtitle="Aus Rost wird Stahl.",
          description=[
              "Leg die &6Oxidized Golem Steel Ingots&r in den Hochofen. Heraus kommen blanke &6Golem Steel Ingots&r.",
              "",
              "&eLegierungsofen:&r 3 Deepsilver Ingots und 2 Golem Steel Nuggets ergeben einen weiteren Golem Steel Ingot. Deepsilver, Golem Steel, Malarite und Soul Dew ergeben &6Unrealium&r.",
              "",
              "Aus Golem Steel werden Greatsword, Energy Boomerang und mit Kristallen das Crystal Greatsword.",
          ],
          tasks=[task_item("eternal_starlight:golem_steel_ingot", 4)],
          rewards=[reward_item("eternal_starlight:deepsilver_ingot", 8), reward_xp(15)],
          deps=["golem"], icon="eternal_starlight:golem_steel_ingot"),

    quest("freezes", 16, -1.5, "&bSchalte die Freezes aus",
          subtitle="Vorbereitung für den zweiten Boss.",
          description=[
              "Erleg &65 Freezes&r in der Golemschmiede. Sie bewachen den Raum des Permafrost.",
              "",
              "Ihre Treffer machen Erfrierungen. Trag Rüstung, die gegen Kälte schützt, und nimm genug Essen mit.",
          ],
          tasks=[task_kill("eternal_starlight:freeze", 5)],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["golem"], icon="eternal_starlight:oxidized_golem_steel_nugget", size=1.25),

    quest("permafrost", 18.5, -1.5, "&b&lBesiege den Permafrost",
          subtitle="Boss 2 von 3.",
          description=[
              "Der &bPermafrost&r ist eine Kühlanlage aus mehreren Freezes. Er spuckt eisigen Speichel, der den Boden gefrieren lässt, und wirft Frozen Tubes in alle Richtungen. Bleib in Bewegung.",
              "",
              "&eBeute:&r &6Coldsnap&r, Frozen Tubes und Oxidized Golem Steel Nuggets.",
          ],
          tasks=[task_kill("eternal_starlight:permafrost", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["freezes"], icon="eternal_starlight:coldsnap", size=1.75, shape="hexagon"),

    quest("garden", 16, -0.5, "&5Betritt den Cursed Garden",
          subtitle="Vorbereitung für den dritten Boss.",
          description=[
              "Finde den &5Cursed Garden&r, ein Heckenlabyrinth voller &6Tangled&r. Erleg &610 Tangled&r auf dem Weg zur Mitte.",
              "",
              "Nach dem Tod lässt ein Tangled einen &6Tangled Skull&r frei, der durch Wände fliegt und explodiert. Flächenwaffen wie Sensen und &6Sonar Bombs&r sind hier am besten.",
              "",
              "&cPflicht:&r Feuerzeug oder eine Waffe mit Verbrennung. Ohne Feuer kommst du durch die Haut des Bosses nicht durch.",
          ],
          tasks=[task_kill("eternal_starlight:tangled", 10), task_item("minecraft:flint_and_steel", 1)],
          rewards=[reward_item("eternal_starlight:soul_dew", 2), reward_xp(10)],
          deps=["permafrost"], icon="eternal_starlight:tangled_skull", size=1.25),

    quest("monstrosity", 18.5, -0.5, "&5&lBesiege die Lunar Monstrosity",
          subtitle="Boss 3 von 3.",
          description=[
              "Zünd sie an, dann wird sie verwundbar. Ohne Feuer machen die meisten Waffen kaum Schaden. Sie bleibt meist am Ort, gräbt sich aber manchmal ein und taucht bei dir auf.",
              "",
              "&eBeute:&r &6Crescent Spear&r, &6Moonring Bow&r, &6Wand of Teleportation&r, Crescent Pendant, &6Tenacious Petals&r und &6Tenacious Vines&r.",
          ],
          tasks=[task_kill("eternal_starlight:lunar_monstrosity", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["garden"], icon="eternal_starlight:crescent_spear", size=1.75, shape="hexagon"),

    quest("petal_scythe", 21, -0.5, "&dBau die Petal Scythe",
          subtitle="Die Sense aus der Beute der Monstrosity.",
          description=[
              "Werkbank: &64 Tenacious Petals&r und &62 Tenacious Vines&r ergeben die &6Petal Scythe&r. Mit Soul Dew wird aus Petals und Vines das Moonring Greatsword.",
          ],
          tasks=[task_item("eternal_starlight:petal_scythe", 1)],
          rewards=[reward_item("eternal_starlight:soul_dew", 2), reward_xp(15)],
          deps=["monstrosity"], icon="eternal_starlight:petal_scythe"),

    # ---- Abschluss -----------------------------------------------------------
    quest("explorer", 23.5, -1.5, "&b&lHerrsch unter einer Million Sternen",
          subtitle="Alle drei Bosse liegen.",
          description=[
              "Sammle &68 Golem Steel Ingots&r und &632 Deepsilver Ingots&r. Golem, Permafrost und Monstrosity sind besiegt.",
              "",
              "Alle drei Bosse lassen sich erneut bekämpfen. Die Beute ist ein guter Weg zu starker Ausrüstung vor dem Gaia-Wächter.",
              "",
              "&eKronwerke:&r Für das Stufenziel zählt hier nichts direkt. Wer hier seine Ausrüstung holt, kämpft besser im End und bei den Gaia-Kämpfen auf Stream.",
          ],
          tasks=[task_item("eternal_starlight:golem_steel_ingot", 8), task_item("eternal_starlight:deepsilver_ingot", 32)],
          rewards=[reward_table("s4_rare"), reward_xp(25)],
          deps=["golem_steel", "permafrost", "monstrosity"], icon="eternal_starlight:orb_of_prophecy", size=2.5, shape="gear"),
    # ---- Neu ------------------------------------------------------------------
    quest("es_etheric_eye", -1, 3.2, "&dBau Etheric Eyes",
          subtitle="Der schnelle Weg nach oben.",
          description=[
              "An den Ether Rivers wachsen &6Thioquartz&r-Geoden wie Amethyst. Ein &6Seeking Eye&r in der Mitte und &64 Thioquartz Shards&r an den Seiten ergeben &e4 Etheric Eyes&r.",
              "",
              "Benutz eines, und es bringt dich an die Oberfläche. Ideal, wenn du dich in den Höhlen unter dem Voidstone verlaufen hast. Aus den Shards werden auch Thioquartz-Pfeile.",
          ],
          tasks=[task_item("eternal_starlight:etheric_eye", 4)],
          rewards=[reward_item("eternal_starlight:seeking_eye", 2), reward_xp(10)],
          deps=["seeking_eye"], icon="eternal_starlight:etheric_eye", optional=True),

    quest("es_all_biomes", 12.5, -7, "&b&lErkunde alle 22 Biome",
          subtitle="Vom Kristallwüstensand bis in den Abgrund.",
          description=[
              "Betritt jedes der &d22&r Biome von Eternal Starlight, auch die Meere, die &6Ether Rivers&r, die &6Solaris Isles&r und ganz unten &6The Abyss&r.",
              "",
              "Ein &6Kompass der Natur&r findet dir die fehlenden. Für die Meere nimm ein Boot und Atemtränke mit.",
          ],
          tasks=[task_advancement("eternal_starlight:all_starlight_biomes", "Alle Biome von Eternal Starlight besucht")],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["forests", "desert", "swamp", "permafrost_forest"], icon="naturescompass:naturescompass", optional=True),

    quest("es_deepsilver_armor", 5, 0.5, "&7Trag die volle Deepsilver-Rüstung",
          subtitle="Die erste Rüstung der Sternenwelt.",
          description=[
              "Schmiede &6Helm&r, &6Harnisch&r, &6Beinschutz&r und &6Stiefel&r aus Deepsilver Ingots, wie bei Eisen. Sie macht dich gegen bestimmte schädliche Effekte immun, der Tooltip zeigt welche und ob dafür das volle Set nötig ist.",
              "",
              "&eKronwerke:&r In Stufe 4 haben feindliche Mobs &d120 Prozent&r mehr Leben, &d75 Prozent&r mehr Schaden und &d7&r Rüstungspunkte dazu, auch die Bewohner dieser Dimension. Geh nicht ohne volle Rüstung los.",
          ],
          tasks=[task_item("eternal_starlight:deepsilver_helmet", 1), task_item("eternal_starlight:deepsilver_chestplate", 1),
                 task_item("eternal_starlight:deepsilver_leggings", 1), task_item("eternal_starlight:deepsilver_boots", 1)],
          rewards=[reward_item("eternal_starlight:deepsilver_ingot", 8), reward_xp(10)],
          deps=["deepsilver"], icon="eternal_starlight:deepsilver_chestplate"),

    quest("es_glacite_armor", 10, 0.5, "&fTrag die volle Glacite-Rüstung",
          subtitle="Wer dich schlägt, friert ein.",
          description=[
              "Schmiede alle vier Teile aus &6Glacite Shards&r, wie bei Eisen. Getragen friert sie Gegner ein, die dir Schaden machen.",
              "",
              "Dazu passt der &6Glacite Shield&r: Bretter mit einem Glacite Shard oben in der Mitte. Ihn brauchst du später für den Flowglaze Shield.",
          ],
          tasks=[task_item("eternal_starlight:glacite_helmet", 1), task_item("eternal_starlight:glacite_chestplate", 1),
                 task_item("eternal_starlight:glacite_leggings", 1), task_item("eternal_starlight:glacite_boots", 1)],
          rewards=[reward_item("eternal_starlight:glacite_shard", 8), reward_xp(10)],
          deps=["permafrost_forest", "deepsilver"], icon="eternal_starlight:glacite_chestplate", optional=True),

    quest("es_springstone_armor", 12.5, 0.5, "&cTrag die volle Springstone-Rüstung",
          subtitle="Wer dich schlägt, fängt Feuer.",
          description=[
              "Schmiede alle vier Teile aus &6Thermal Springstone Ingots&r, wie bei Eisen. Getragen setzt sie Gegner in Brand, die dir Schaden machen.",
              "",
              "Gegen die &5Lunar Monstrosity&r ist Feuer Gold wert, gegen die Freezes und den Permafrost auch.",
          ],
          tasks=[task_item("eternal_starlight:thermal_springstone_helmet", 1), task_item("eternal_starlight:thermal_springstone_chestplate", 1),
                 task_item("eternal_starlight:thermal_springstone_leggings", 1), task_item("eternal_starlight:thermal_springstone_boots", 1)],
          rewards=[reward_item("eternal_starlight:thermal_springstone_ingot", 8), reward_xp(10)],
          deps=["springstone"], icon="eternal_starlight:thermal_springstone_chestplate", optional=True),

    quest("es_flowglaze_shield", 2.5, 4, "&bWerte zum Flowglaze Shield auf",
          subtitle="Ein Schild, der Geschosse zurückwirft.",
          description=[
              "Schmiedetisch: &6Flowglaze Upgrade Smithing Template&r, &6Glacite Shield&r und &6Flowglaze&r ergeben den &6Flowglaze Shield&r.",
              "",
              "Blockst du mit ihm, fliegen Pfeile und andere Geschosse zurück. Gegen Lonestar Skeletons und Fernkämpfer in den Bossarenen sehr angenehm.",
          ],
          tasks=[task_item("eternal_starlight:flowglaze_shield", 1)],
          rewards=[reward_xp(15)],
          deps=["flowglaze_scythe", "es_glacite_armor"], icon="eternal_starlight:flowglaze_shield", optional=True),

    quest("es_aethersent_golem", 2.5, -3, "&eBau einen Aethersent Golem",
          subtitle="Ein Wächter gegen Meteore.",
          description=[
              "&69 Aethersent Ingots&r ergeben einen &6Block of Aethersent&r. Stell ihn auf, schnitz eine &6Lunaris-Kaktusfrucht&r und setz sie oben drauf.",
              "",
              "Der &6Aethersent Golem&r schießt Meteore ab, bevor sie in deiner Basis einschlagen. Bei einem Meteorschauer fallen auch Creteors herunter, die explodieren wie Creeper.",
          ],
          tasks=[task_advancement("eternal_starlight:summon_aethersent_golem", "Einen Aethersent Golem gebaut")],
          rewards=[reward_item("eternal_starlight:aethersent_ingot", 4), reward_xp(15)],
          deps=["meteor"], icon="eternal_starlight:aethersent_block", optional=True),

    quest("es_moth", 7.5, 9, "&dZähm eine Crystallized Moth",
          subtitle="Ein Begleiter mit Schallwellen.",
          description=[
              "In der &6Crystallized Desert&r fliegen &6Crystallized Moths&r. Füttere eine mit genug Fleisch, bis sie zahm ist.",
              "",
              "Sie greift deine Gegner mit Schallwellen an. Ein Begleiter, der in dieser Dimension mitkämpft, ist viel wert.",
          ],
          tasks=[task_advancement("eternal_starlight:tame_crystallized_moth", "Eine Crystallized Moth gezähmt")],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["mobs_animals", "desert"], icon="eternal_starlight:blue_starlight_crystal_shard", optional=True),

]

images = [
    banner("eternal_starlight/title", "Eternal Starlight", 12, -9, height=1.75, kind="title", colour="water"),
    banner("eternal_starlight/entry", "Der Weg hinein", 1.25, -1.6, height=0.9, colour="water"),
    banner("eternal_starlight/biomes", "Die Biome", 8.75, -7.4, height=0.9, colour="nature"),
    banner("eternal_starlight/gear", "Erze", 8.75, 0.3, height=0.9, colour="stone"),
    banner("eternal_starlight/scythes", "Sensen", 8.75, 2.9, height=0.9, colour="stone"),
    banner("eternal_starlight/mobs", "Bewohner", 6.25, 5.8, height=0.9, colour="nature"),
    banner("eternal_starlight/bosses", "Bosse", 18.5, -5.6, height=0.9, colour="magic"),
]

chapter(C, "Eternal Starlight", "eternal_starlight:orb_of_prophecy", "world", quests, shape="circle", order=33, stage=4,
        subtitle=["Stufe 4. Der Gatekeeper, das Portal, die Biome, Erze, Sensen und die drei Bosse der Sternendimension."],
        images=images)
