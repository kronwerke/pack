"""Eternal Starlight: opened with stage 4. The Gatekeeper and the Orb of Prophecy, the portal,
the biomes and what each one gives, the ores and gear, and the three bosses in the
dimension (Starlight Golem, Permafrost, Lunar Monstrosity)."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "eternal_starlight"

quests = [
    # ---- Der Weg hinein ------------------------------------------------------
    quest("orb", 0, 5, "&b&lDer Torwächter",
          subtitle="Wer hinein will, muss sich beweisen.",
          description=[
              "&bEternal Starlight&r ist eine eigene Dimension unter einem Himmel voller Sterne. Mit &eStufe 4&r ist sie offen.",
              "",
              "&eDie Portalruinen:&r In der Oberwelt stehen kleine Ruinen mit einem Rahmen aus &6Chiseled Voidstone&r. Es gibt sie in mehreren Varianten: in Ebenen und Savannen, in Wäldern, in Wüsten, im Dschungel und in kalten Biomen.",
              "",
              "&eDer Gatekeeper:&r In jeder Ruine wartet ein &bTorwächter&r. Sprich ihn mit Rechtsklick an und wähle &eChallenge&r. Er fragt noch einmal nach, ob du wirklich bereit bist, dann beginnt der Kampf. Er pariert Angriffe und wirft mit Feuerbällen, also komm mit guter Rüstung und Essen.",
              "",
              "&eDer Lohn:&r Wer ihn zum ersten Mal besiegt, bekommt das Buch der Dimension und die &bOrb of Prophecy&r. Handeln will er erst mit dir, wenn du dich im Kampf bewiesen hast.",
              "",
              img(item_texture("eternal_starlight:orb_of_prophecy"), 32, 32),
          ],
          tasks=[task_item("eternal_starlight:orb_of_prophecy", 1)],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          icon="eternal_starlight:orb_of_prophecy", size=2.0, shape="hexagon"),

    quest("portal", 2.8, 5, "&bUnter dem Sternenhimmel",
          subtitle="Die Kugel auf den Rahmen.",
          description=[
              "Benutze die &bOrb of Prophecy&r am Portalrahmen aus &6Chiseled Voidstone&r, und das Portal öffnet sich.",
              "",
              "&eDrüben&r ist es immer Nacht. Monster spawnen fast überall, die häufigsten sind &6Nightfall Spiders&r und &6Lonestar Skeletons&r, die die Klingen ihrer Schwerter werfen. Leg dir gleich am Portal einen sicheren Raum an.",
              "",
              "&eWeitere Kugeln:&r Eine neue Orb of Prophecy baust du an der Werkbank aus fünf &6Blue Starlight Crystal Shards&r und vier &6Glas&r. Die Kristalle findest du in der Dimension selbst, vor allem in der Kristallwüste.",
          ],
          tasks=[task_dimension("eternal_starlight:starlight")],
          rewards=[reward_item("minecraft:torch", 64), reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["orb"], icon="eternal_starlight:chiseled_voidstone", size=1.75, shape="hexagon"),

    quest("seeking_eye", 2.8, 7.8, "&dSeeking Eye",
          subtitle="Zeigt dir den Weg.",
          description=[
              "Das &dSeeking Eye&r öffnet eine Sternenkarte. Dort wählst du ein Bauwerk oder ein Biom aus, und das Auge schwebt neben dir her und zeigt in die richtige Richtung.",
              "",
              "Klick es an, um es zurückzuholen. Dabei kann es zerbrechen.",
              "",
              "&eRezept:&r Acht &6Starlight Flowers&r um eine Enderperle ergeben gleich sechzehn Augen. Der Gatekeeper und die Bosse lassen auch welche fallen.",
          ],
          tasks=[task_item("eternal_starlight:seeking_eye", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["portal"], icon="eternal_starlight:seeking_eye", optional=True),

    # ---- Die Biome -----------------------------------------------------------
    quest("forests", 6, 2, "&aDie Sternenwälder",
          subtitle="Lunar-Bäume und Feuervögel.",
          description=[
              "Der größte Teil der Dimension sind Wälder, Ebenen und Taiga: &6Starlight Forest&r, &6Dense Forest&r, &6Umbral Plains&r, &6Glimmer Scrubland&r, &6Scarlet Forest&r und &6Starlight Taiga&r. Hier stehen die hohen &6Lunar&r-Bäume.",
              "",
              "&eStarfire Birds:&r Ihre Nester sitzen in den Kronen der Lunar-Bäume. Leg Samen hinein, dann belohnen sie dich, unter anderem mit &6Starfire&r. Starfire wirfst du als Waffe, damit verbesserst du Thermal-Springstone-Ausrüstung, und auf Twilight Sand geworfen wird daraus &6Flowglaze&r.",
              "",
              "&eNocturnal Millet:&r Das Getreide der Dimension. Die Samen stecken im Thioquarz am Ufer des Ether River.",
          ],
          tasks=[task_item("eternal_starlight:lunar_log", 16)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(5)],
          deps=["portal"], icon="eternal_starlight:lunar_log"),

    quest("torreya", 8.5, 2, "&6Torreya und Amaramber",
          subtitle="Harz, das Monster fernhält.",
          description=[
              "Im &6Torreya Forest&r wachsen Torreya-Bäume. Wenn du ihre Stämme mit der Axt entrindest, fällt manchmal &6Raw Amaramber&r ab, ein Harz. Auch ein abgebautes Torreya-Lagerfeuer gibt welches.",
              "",
              "&eWarum das zählt:&r In dieser Dimension halten brennende Amaramber-Kerzen, Amaramber-Laternen, Torreya-Lagerfeuer und Amaramber-Feuer feindliche Monster in der Nähe vom Spawnen ab. Amaramber-Feuer bekommst du, wenn du einen Block aus Raw Amaramber mit dem Feuerzeug anzündest.",
              "",
              "Für eine Basis in der Dimension ist das Gold wert.",
          ],
          tasks=[task_item("eternal_starlight:raw_amaramber", 9)],
          rewards=[reward_xp(10)],
          deps=["forests"], icon="eternal_starlight:raw_amaramber"),

    quest("desert", 6, 4.5, "&bDie Kristallwüste",
          subtitle="Kristalle und hungrige Zähne.",
          description=[
              "Die &6Crystallized Desert&r ist voller blauer und roter &bStarlight-Kristalle&r. Baust du die Kristallhaufen ab, bekommst du Splitter, unter anderem die &6Blue Starlight Crystal Shards&r für neue Orbs of Prophecy.",
              "",
              "&eThirst Walker:&r Sie schleichen sich an, beißen zu und rennen weg. Blockst du den Biss mit einem Schild, verlieren sie einen Zahn. Mit dem &6Tooth of Hunger&r baust du den &6Dagger of Hunger&r, der durch Treffer satt und schärfer wird, und den &6Crystalborn Catalyst&r.",
              "",
              "&eUnter der Wüste&r jagen &6Crystallized Moths&r mit Schallwellen, die kein Schild aufhält. Mit genug Fleisch kannst du sie zähmen.",
          ],
          tasks=[task_item("eternal_starlight:blue_starlight_crystal_shard", 16), task_item("eternal_starlight:tooth_of_hunger", 1)],
          rewards=[reward_item("minecraft:glass", 16), reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:blue_starlight_crystal_shard"),

    quest("swamp", 6, 7, "&2Der Dunkle Sumpf",
          subtitle="Malarit und die Stranghouls.",
          description=[
              "Der &6Dark Swamp&r ist das einzige Biom mit &6Malarite&r-Erz. Malarit wird zu Waffen, Werkzeugen und Pfeilen.",
              "",
              "&eStranghouls:&r Diese Wesen leben hier in eigenen Höhlen. Mit Malarit kannst du mit ihnen tauschen, und für eine Schüssel &6Pungency Stew&r kämpfen sie einen Tag lang für dich. Aber: Wer schwer verletzt in ihrer Nähe herumsteht, sieht für sie aus wie Futter. Silberwaffen fürchten sie.",
              "",
              "&ePungency Fruit&r wächst überall im Sumpf. Sie riecht nach Knoblauch und taugt auch als Waffe.",
          ],
          tasks=[task_item("eternal_starlight:malarite", 8)],
          rewards=[reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:malarite"),

    quest("permafrost_forest", 8.5, 7, "&fDer ewige Frost",
          subtitle="Glacite, Hirsche und Yetis.",
          description=[
              "Im &6Starlight Permafrost Forest&r und auf den &6Permafrost Peaks&r liegt &fGlacite&r. Im Ofen wird es zu &6Glacite Shards&r, aus denen du Rüstung, Werkzeug, Pfeile und Frostbomben baust.",
              "",
              "&eAurora Deer:&r Greifen an, wenn man sie angreift. Lenkst du einen wütenden Hirsch gegen harten Stein, fällt sein Geweih ab. Das ist direkt eine Waffe.",
              "",
              "&eYetis&r kannst du scheren, die Wolle gibt Teppiche und Betten. Unter dem Wald liegt eine Schicht aus &6Ashen Snow&r.",
          ],
          tasks=[task_item("eternal_starlight:glacite_shard", 8)],
          rewards=[reward_xp(10)],
          deps=["swamp"], icon="eternal_starlight:glacite_shard"),

    quest("meteor", 3.5, 1.5, "&eSternschnuppen",
          subtitle="Erz vom Himmel.",
          description=[
              "Manchmal gibt es in der Dimension einen &eMeteorschauer&r. Kleine Meteore sind nur schön, große schlagen ein und hinterlassen Erz an der Einschlagstelle. Dazu gehört &6Raw Aethersent&r, das zu &6Aethersent-Barren&r schmilzt.",
              "",
              "&eCreteors&r fallen mit den Meteoren herunter, sternförmige Creeper. Ihr Leder taugt für Ausrüstung.",
              "",
              "&eSchutz:&r Ein &6Aethersent Golem&r (ein geschnitzter Lunaris-Kaktus auf einem Aethersent-Block) schießt Meteore ab, bevor sie deine Basis treffen. Mit einer &6Aetherstrike Rocket&r löst du selbst einen Schauer aus.",
          ],
          tasks=[task_item("eternal_starlight:aethersent_ingot", 4)],
          rewards=[reward_xp(10)],
          deps=["portal"], icon="eternal_starlight:aethersent_ingot", optional=True),

    # ---- Erze und Ausrüstung -------------------------------------------------
    quest("ores", 11.5, 3, "&7Erze unter den Sternen",
          subtitle="Deepsilver, Starlit Diamond, Starcore.",
          description=[
              "Unter der Oberfläche liegen &6Voidstone&r und &6Grimstone&r statt Stein. Darin findest du in fast allen Biomen:",
              "",
              "&6Deepsilver:&r Das Eisen der Dimension. Rüstung, Werkzeug, ein Schild und sogar Eimer und Kessel.",
              "&6Starlit Diamond:&r Werkzeug und Rüstung aus Sternendiamant.",
              "&6Starcore:&r Für Lampen und leuchtende Blöcke, und zusammen mit Glacite für Frostbomben.",
              "",
              "Auch Redstone und &6Saltpeter&r gibt es hier. Alles wird im Ofen oder Schmelzofen geschmolzen.",
          ],
          tasks=[task_item("eternal_starlight:deepsilver_ingot", 16), task_item("eternal_starlight:starlit_diamond", 4)],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          deps=["torreya", "desert"], icon="eternal_starlight:starlit_diamond", size=1.5),

    quest("springstone", 11.5, 6, "&cThermal Springstone",
          subtitle="Aus den heißen Quellen.",
          description=[
              "An den &cheißen Quellen&r der Dimension findest du &6Thermal Springstone&r. Im Ofen wird daraus ein Barren.",
              "",
              "Daraus baust du Rüstung, Werkzeuge, eine Sense und einen Hammer. Am Schmiedetisch wird der Hammer mit einer &6Starfire Upgrade Smithing Template&r und &6Starfire&r zum Starfire-Hammer, genauso die Sense.",
              "",
              "&eTipp:&r Die riesigen Pflanzen dort zerstört nur Feuer.",
          ],
          tasks=[task_item("eternal_starlight:thermal_springstone_ingot", 8)],
          rewards=[reward_xp(10)],
          deps=["permafrost_forest"], icon="eternal_starlight:thermal_springstone_ingot"),

    quest("weapons", 14, 4.5, "&dSense und Hammer",
          subtitle="Waffen mit Eigenheiten.",
          description=[
              "Eternal Starlight hat eigene Waffenarten:",
              "",
              "&6Sensen&r gibt es aus mehreren Materialien: Glacite, Thermal Springstone und andere. Sie sind eine eigene Waffenart neben Schwert und Axt.",
              "&6Hämmer&r lösen einen Spezialangriff aus, wenn du mit voller Kraft einen kritischen Treffer landest.",
              "",
              "&eZubehör:&r Manche Dinge lassen sich mit Ausrüstung verbinden, um ihr Eigenschaften zu geben. Du legst sie wie in ein Bündel hinein und nimmst sie genauso wieder heraus. Geht das Teil kaputt, ist das Zubehör weg.",
              "",
              "Bau dir eine Sense aus einem Material deiner Wahl.",
          ],
          tasks=[task_advancement("eternal_starlight:obtain_scythe", "Eine Sense bauen")],
          rewards=[reward_item("eternal_starlight:thermal_springstone_ingot", 4), reward_xp(10)],
          deps=["ores", "springstone"], icon="eternal_starlight:thermal_springstone_scythe"),

    # ---- Bosse ---------------------------------------------------------------
    quest("golem", 17, 2, "&6&lStarlight Golem",
          subtitle="Der Wächter der Golemschmiede.",
          description=[
              "In den Wäldern und Ebenen stehen alte &6Golemschmieden&r (Golem Forge) aus oxidiertem Golemstahl. Im Boss-Raum wartet der &6Starlight Golem&r.",
              "",
              "&eSo geht der Kampf:&r Sein Schild ist unzerstörbar. Er bewegt sich nicht, aber er wird heiß und muss sich zwischendurch aufladen. Dann schaltest du die &eEnergieblöcke&r in der Nähe ab, und sein Schild fällt. Mit einer &6Frozen Tube&r beworfen geht er schneller in den Ladezustand.",
              "",
              "&eBeute:&r Oxidierter &6Golemstahl&r, der im Ofen zu blankem Golemstahl wird, ein &6Energy Sword&r und ein oxidierter Legierungsofen.",
          ],
          tasks=[task_kill("eternal_starlight:starlight_golem", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["weapons"], icon="eternal_starlight:golem_steel_ingot", size=1.75, shape="hexagon"),

    quest("permafrost", 17, 4.5, "&b&lPermafrost",
          subtitle="Die letzte Kühlanlage.",
          description=[
              "In einem eigenen Raum der Golemschmiede steht der &bPermafrost&r, eine Kühlanlage aus mehreren Freezes. Er spuckt eisigen Speichel, der den Boden gefrieren lässt, und wirft Frozen Tubes in alle Richtungen.",
              "",
              "&eTipp:&r Schon die kleinen &6Freezes&r in der Schmiede verursachen Erfrierungen. Kälteschützende Rüstung hilft gegen ihre Angriffe.",
              "",
              "&eBeute:&r &6Coldsnap&r, Frozen Tubes und Golemstahl.",
          ],
          tasks=[task_kill("eternal_starlight:permafrost", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["weapons"], icon="eternal_starlight:frozen_tube", size=1.75, shape="hexagon"),

    quest("monstrosity", 17, 7, "&5&lLunar Monstrosity",
          subtitle="Im verfluchten Garten.",
          description=[
              "Der &5Cursed Garden&r ist ein Heckenlabyrinth voller &6Tangled&r, gebunden an die Lunar-Ranke. In der Mitte wartet die &5Lunar Monstrosity&r.",
              "",
              "&eFeuer:&r Ihre Haut ist so zäh, dass die meisten Waffen kaum Schaden machen. Erst wenn du sie anzündest, wird sie verwundbar. Sie bleibt meist an einem Ort, gräbt sich aber manchmal ein und taucht bei dir wieder auf.",
              "",
              "&eDie Tangled&r hinterlassen nach dem Tod einen &6Tangled Skull&r, der durch Wände fliegt und beim Tod explodiert. Waffen, die eine ganze Fläche treffen, wie Peitschen oder &6Sonar Bombs&r, sind hier am besten.",
              "",
              "&eBeute:&r Der &6Crescent Spear&r, der &6Moonring Bow&r, der &6Wand of Teleportation&r und mehr.",
          ],
          tasks=[task_kill("eternal_starlight:lunar_monstrosity", 1)],
          rewards=[reward_table("s4_uncommon"), reward_xp(20)],
          deps=["weapons"], icon="eternal_starlight:crescent_spear", size=1.75, shape="hexagon"),

    quest("explorer", 19.8, 4.5, "&b&lUnter einer Million Sterne",
          subtitle="Die Dimension gehört dir.",
          description=[
              "Golem, Permafrost und Monstrosity sind besiegt. Du kennst die Wälder, die Kristallwüste, den Sumpf und den Frost.",
              "",
              "Alle drei Bosse lassen sich erneut bekämpfen. Für eine Gruppe aus Stufe 4 ist die Beute ein guter Weg zu starker Ausrüstung, bevor es gegen den Gaia-Wächter geht.",
              "",
              "&eKronwerke:&r Für das Stufenziel zählt hier nichts direkt. Aber wer hier seine Ausrüstung holt, kämpft besser im End und bei den Gaia-Kämpfen auf Stream.",
          ],
          tasks=[task_item("eternal_starlight:golem_steel_ingot", 8), task_item("eternal_starlight:deepsilver_ingot", 32)],
          rewards=[reward_table("s4_rare"), reward_xp(25)],
          deps=["golem", "permafrost", "monstrosity"], icon="eternal_starlight:orb_of_prophecy", size=2.5, shape="gear"),
]

images = [
    banner("eternal_starlight/title", "Eternal Starlight", 10, -1.2, height=1.75, kind="title", colour="water"),
    banner("eternal_starlight/entry", "Der Weg hinein", 1.4, 3.0, height=0.9, colour="water"),
    banner("eternal_starlight/biomes", "Die Biome", 7.25, 0.4, height=0.9, colour="nature"),
    banner("eternal_starlight/gear", "Erze und Ausrüstung", 12.75, 1.3, height=0.9, colour="stone"),
    banner("eternal_starlight/bosses", "Bosse", 17, 0.4, height=0.9, colour="magic"),
]

chapter(C, "Eternal Starlight", "eternal_starlight:orb_of_prophecy", "world", quests, shape="circle", order=33, stage=4,
        subtitle=["Stufe 4. Der Torwächter, das Portal, die Biome, Erze und die drei Bosse der Sternendimension."],
        images=images)
