"""Industrial Foregoing in stage 3: latex from logs, dry rubber and plastic, the machine frames
up to advanced (the dissolution chamber with latex and pink slime), the pitiful and biofuel
generators, plant and mob automation, the ore laser base with the laser drill and lenses, and
the conveyors and transporters. Kronwerke changes no Industrial Foregoing recipe. Numbers come
from the in-jar manual and config/industrialforegoing."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "industrial"

quests = [
    # ---- Latex und Plastik ---------------------------------------------------
    quest("welcome", 0, 1, "&a&lIndustrial Foregoing",
          subtitle="Fabriken, die Felder, Tiere und Erze übernehmen.",
          description=[
              "&aIndustrial Foregoing&r baut Maschinen, die dir Arbeit abnehmen: Felder ernten, Bäume fällen, Tiere scheren, Mobs verarbeiten und am Ende mit einem Laser Erze aus dem Nichts bohren. Der Mod ist mit Stufe 3 offen.",
              "",
              "Fast jede Maschine sitzt in einem &6Maschinengehäuse&r. Das erste, das &6Primitive Maschinengehäuse&r, baust du an der Werkbank: vier Stämme in die Ecken, vier Eisenbarren an die Seiten, ein Redstoneblock in die Mitte.",
              "",
              "Der Weg durch dieses Kapitel: Latex aus Holz, daraus Gummi und &6Kunststoff&r, dann bessere Gehäuse und die großen Maschinen. Im Spiel gibt es das &6Industrial Foregoing: Handbuch&r, ein Buch mit allen Maschinen.",
              "",
              "Bau dir zuerst zwei Primitive Gehäuse.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_pity", 2)],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_table("s3_common")],
          icon="industrialforegoing:machine_frame_pity", size=2.0, shape="hexagon"),

    quest("extractor", 2.6, 0, "&6Flüssigkeitsextraktor",
          subtitle="Er zapft Bäume an.",
          description=[
              "&eRezept:&r oben Eisen, eine leichte Wägeplatte (Gold), Eisen, in der Mitte Bruchstein, Primitives Gehäuse, Bruchstein, unten Eisen, Kolben, Eisen.",
              "",
              "Stell den Extraktor mit der Vorderseite vor einen &6Stamm&r. Er zieht &6Latex&r heraus, schält dabei zuerst die Rinde ab und verbraucht den Stamm am Ende ganz. Ein Eichenstamm gibt pro Durchgang 2 mB, andere Hölzer andere Mengen, JEI zeigt sie.",
              "",
              "Mehrere Extraktoren können denselben Stamm anzapfen. Strom ist freiwillig, macht ihn aber schneller. Am besten baust du einen kleinen Kreis aus Extraktoren um eine Säule aus Stämmen.",
          ],
          tasks=[task_item("industrialforegoing:fluid_extractor", 2)],
          rewards=[reward_item("minecraft:oak_log", 32)],
          deps=["welcome"]),

    quest("pitiful", 2.6, 2, "&cPrimitiver Heizgenerator",
          subtitle="Der Name sagt alles.",
          description=[
              "Der &6Pitiful Generator&r heißt im deutschen Spiel &6Primitiver Heizgenerator&r. Er verbrennt Kohle und alles andere, was im Ofen brennt, und liefert &d30 FE/t&r.",
              "",
              "Er ist mit Absicht schlecht: Er verbrennt seinen Brennstoff auch dann weiter, wenn sein Speicher voll ist. Für den Anfang reicht er, ersetz ihn aber bald durch den Biogenerator oder Strom aus einem anderen Mod.",
              "",
              "&eRezept:&r Bruchstein in die Ecken, Goldbarren oben, Eisengitter links und rechts, ein Ofen unten, das Primitive Gehäuse in der Mitte.",
          ],
          tasks=[task_item("industrialforegoing:pitiful_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 4)],
          deps=["welcome"]),

    quest("latex_unit", 5.2, 0, "&eLatexverarbeitung",
          subtitle="Aus Milch wird Gummi.",
          description=[
              "Die &6Latexverarbeitungsmaschine&r macht aus &e750 mB Latex&r und &e500 mB Wasser&r einen &6Gummiklumpen&r. Sie braucht 20 FE/t.",
              "",
              "&eRezept:&r Eisen in die Ecken, ein Redstoneblock oben, Eimer links und rechts, ein Ofen unten, das Primitive Gehäuse in der Mitte.",
              "",
              "Stell sie direkt an die Extraktoren oder verbinde sie mit Rohren, und gib ihr eine Wasserquelle. Ein Unendlich-Wasser-Becken mit einer Pumpe aus einem anderen Mod tut es genauso.",
          ],
          tasks=[task_item("industrialforegoing:latex_processing_unit", 1), task_item("industrialforegoing:dryrubber", 4)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(5)],
          deps=["extractor"], icon="industrialforegoing:dryrubber"),

    quest("plastic", 7.8, 0, "&f&lKunststoff",
          subtitle="Das Material, aus dem dieser Mod gebaut ist.",
          description=[
              "Schmilz einen &6Gummiklumpen&r im Ofen, heraus kommt &6Kunststoff&r. Fast jede Maschine ab hier braucht zwei bis vier Stück.",
              "",
              "Ein Stapel Kunststoff ist kein schlechtes Ziel. Lass die Extraktoren am besten Tag und Nacht laufen.",
              "",
              "&eGut zu wissen:&r Die Plastik Platte aus &6Oritech&r zählt für Industrial Foregoing ebenfalls als Kunststoff. Wer dort schon eine Zentrifuge hat, kann damit aushelfen.",
              "",
              img(item_texture("industrialforegoing:plastic"), 32, 32),
          ],
          tasks=[task_item("industrialforegoing:plastic", 16)],
          rewards=[reward_item("industrialforegoing:plastic", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["latex_unit"], size=1.5, shape="hexagon"),

    # ---- Gehäuse -------------------------------------------------------------
    quest("dissolution", 10.4, 0, "&9Auflösungsapparat",
          subtitle="Bis zu acht Zutaten und eine Flüssigkeit.",
          description=[
              "Der &6Auflösungsapparat&r (Dissolution Chamber) ist der Zusammenbautisch des Mods. Er nimmt bis zu &eacht Gegenstände&r und &eeine Flüssigkeit&r und macht daraus Gehäuse, Laserlinsen, Addons und mehr. Die Rezepte sind formlos, die Slots egal.",
              "",
              "&eRezept:&r Kunststoff oben links und rechts, eine Holztruhe oben in der Mitte, Eimer links und rechts, Goldbarren unten in den Ecken, ein &6Diamantzahnrad&r unten in der Mitte, das Primitive Gehäuse in der Mitte. Zahnräder baust du aus vier Barren oder Diamanten im Kreis.",
              "",
              "Hier entstehen auch die &6Geschwindigkeits- und Effizienz-Addons&r. Ein Addon kommt per Rechtsklick in eine Maschine und macht sie schneller oder sparsamer.",
          ],
          tasks=[task_item("industrialforegoing:dissolution_chamber", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["plastic"]),

    quest("frame_simple", 13, 0, "&7Einfaches Maschinengehäuse",
          subtitle="Die zweite Stufe.",
          description=[
              "Im Auflösungsapparat: zwei Kunststoff, ein Primitives Gehäuse, zwei &6Netherziegel&r, zwei Eisenbarren und ein &6Goldzahnrad&r, dazu &e250 mB Latex&r.",
              "",
              "Laserbohrer, Düngemaschine, Hydrokultur-Beet und Fermentationsstation sitzen in diesem Gehäuse. Mach gleich zwei.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_simple", 2)],
          rewards=[reward_item("minecraft:nether_bricks", 16), reward_table("s3_common")],
          deps=["dissolution"], size=1.5, shape="square"),

    # ---- Felder und Strom ----------------------------------------------------
    quest("sower", 7.8, 4.6, "&2Säen und Ernten",
          subtitle="Ein Feld, das sich selbst bestellt.",
          description=[
              "Die &6Sämaschine&r pflanzt Samen und Setzlinge in ihrem Arbeitsbereich. Ihre neun Slots sind farbig markiert, und jede Farbe gehört zu einem Neuntel des Feldes, wie die Markierungen oben auf der Maschine zeigen.",
              "",
              "Die &6Erntemaschine&r erntet reife Pflanzen und fällt ganze Bäume samt Blättern. Dabei entsteht etwas &6Schlamm&r, den die Schlammraffinerie zu nützlichen Dingen verarbeitet.",
              "",
              "Die &6Düngemaschine&r gibt Knochenmehl oder Dünger auf die Pflanzen. Vorsicht bei Pflanzen, die nie fertig werden, an denen bleibt sie hängen.",
              "",
              "&eKronwerke:&r Ein Baumfeld mit Sämaschine und Erntemaschine liefert Stämme für die Extraktoren und Holzkohle für Stahl ohne Ende.",
          ],
          tasks=[task_item("industrialforegoing:plant_sower", 1), task_item("industrialforegoing:plant_gatherer", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["plastic"], icon="industrialforegoing:plant_gatherer"),

    quest("sewer", 5.2, 4.6, "&6Gülle und Dünger",
          subtitle="Was Tiere hinterlassen.",
          description=[
              "Der &6Güllesammler&r sammelt &6Gülle&r von Tieren in seinem Bereich und wandelt Erfahrungskugeln in &aEssenz&r um. Der &6Güllekomposter&r macht aus Gülle &6Dünger&r, der wie Knochenmehl wirkt.",
              "",
              "Dünger geht in die Düngemaschine. So düngt ein Stall voller Kühe dein Feld nebenan.",
          ],
          tasks=[task_item("industrialforegoing:sewer", 1), task_item("industrialforegoing:fertilizer", 16)],
          rewards=[reward_item("minecraft:wheat", 32)],
          deps=["sower"], icon="industrialforegoing:fertilizer", optional=True),

    quest("bio", 7.8, 6.4, "&dBiokraftstoff",
          subtitle="Strom aus Samen und Setzlingen.",
          description=[
              "Der &6Bioreaktor&r macht aus Wasser und Pflanzenzeug &dBiokraftstoff&r: Samen, Setzlinge, Farbstoffe und, ganz ehrlich, auch Köpfe. Je mehr &everschiedene&r Sorten gleichzeitig drin sind, desto mehr kommt pro Stück heraus. Eine Sorte allein gibt 80 mB, vier verschiedene geben je 110 mB.",
              "",
              "Der &6Biogenerator&r verbrennt den Kraftstoff zu &d160 FE/t&r und hört auf, sobald sein Speicher voll ist. Er verschwendet also nichts.",
              "",
              "Zusammen mit der Erntemaschine ist das ein Kraftwerk, das sich selbst versorgt.",
          ],
          tasks=[task_item("industrialforegoing:bioreactor", 1), task_item("industrialforegoing:biofuel_generator", 1)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["sower"], icon="industrialforegoing:biofuel_generator"),

    # ---- Mobs ----------------------------------------------------------------
    quest("mit", 10.4, 4.6, "&5Mobfanggerät",
          subtitle="Ein Mob zum Mitnehmen.",
          description=[
              "Vier Kunststoff um eine &6Ghastträne&r ergeben das &6Mobfanggerät&r. Rechtsklick auf ein Tier oder einen Mob steckt es hinein, Rechtsklick auf den Boden lässt es wieder heraus.",
              "",
              "So bringst du Kühe und Schafe in deine Ställe. Mit einem gefangenen Mob kannst du außerdem die Erkennungs- und Schleuder-Upgrades der Förderbänder auf genau diese Mobart filtern.",
          ],
          tasks=[task_item("industrialforegoing:mob_imprisonment_tool", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 1)],
          deps=["plastic"]),

    quest("slaughter", 13, 4.6, "&dPinker Schleim",
          subtitle="Der Industrielle Schlachter.",
          description=[
              "Der &6Industrielle Schlachter&r tötet Mobs und Tiere in seinem Bereich und macht daraus &6Flüssigfleisch&r und &dPinken Schleim&r. Die Tiere lassen dabei weder Beute noch Erfahrung fallen. Friedliche Tiere geben mehr Schleim als Monster.",
              "",
              "Pinken Schleim brauchst du für das nächste Gehäuse: Im Auflösungsapparat werden daraus Pinke Schleimbälle (eine Glasscheibe und 300 mB) und der &6Pinke Schleimbarren&r (zwei Eisen, zwei Gold, 1 000 mB).",
              "",
              "Eine kleine Hühnerfarm mit einem Tierfütterer daneben reicht für den Anfang.",
          ],
          tasks=[task_item("industrialforegoing:mob_slaughter_factory", 1), task_item("industrialforegoing:pink_slime_bucket", 1)],
          rewards=[reward_item("minecraft:egg", 16)],
          deps=["mit"], icon="industrialforegoing:mob_slaughter_factory"),

    quest("frame_adv", 15.6, 4.6, "&6Fortschrittliches Maschinengehäuse",
          subtitle="Das Gehäuse für die großen Maschinen.",
          description=[
              "Im Auflösungsapparat: zwei Kunststoff, ein Einfaches Gehäuse, zwei &6Netheritplatten&r, zwei Goldbarren und ein Diamantzahnrad, dazu &e500 mB Pinker Schleim&r.",
              "",
              "Die Netheritplatten holst du aus Antikem Schrott im Nether. Für die Erz-Laserbasis, den Monsterschnetzler und den Monsterspawner führt kein Weg daran vorbei.",
              "",
              "&cAusblick:&r Das &6Überlegene Gehäuse&r braucht Netheritbarren und &6Ethergas&r, das nur entsteht, wenn eine Flüssigkeits-Laserbasis über einem Wither arbeitet. Das ist ein Projekt für später.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_advanced", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 1), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["slaughter", "frame_simple"], size=1.5, shape="square"),

    quest("crusher", 15.6, 6.6, "&cMonsterschnetzler",
          subtitle="Beute und Essenz ohne Schwert.",
          description=[
              "Der &6Monsterschnetzler&r (Mob Crusher) tötet Mobs, als hätte ein Spieler zugeschlagen: Du bekommst ihre Beute und dazu &aEssenz&r, flüssige Erfahrung. In einem zweiten Modus gibt es statt Essenz Beute mit zufälligen Stufen von Glück.",
              "",
              "Stell ihn an eine Mobfarm. Essenz füllt den Verzauberungsapplikator und die Verzauberungsfabrik, und sie zählt auch als Erfahrungsflüssigkeit für den Seelenbinder von Ender IO.",
          ],
          tasks=[task_item("industrialforegoing:mob_crusher", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16)],
          deps=["frame_adv"], optional=True),

    # ---- Laserbohrer ---------------------------------------------------------
    quest("laser", 18.6, 2.4, "&c&lErz-Laserbasis",
          subtitle="Erze ohne Bergbau.",
          description=[
              "Die &6Erz-Laserbasis&r erzeugt Erze aus dem Nichts. &eRezept:&r Kunststoff oben links und rechts, eine Diamantspitzhacke oben in der Mitte, Eisenerz links und rechts, das Fortschrittliche Gehäuse in der Mitte, Diamantzahnräder unten links und rechts, Redstone unten in der Mitte.",
              "",
              "Allein tut sie nichts. Sie braucht &6Laserbohrer&r (Einfaches Gehäuse, Kunststoff, Diamantzahnrad, Kolben, Goldzahnräder, Redstone). Ein Laserbohrer mit Strom, &d1 000 FE&r pro Arbeitsschritt, lädt die erste Laserbasis in seinem Arbeitsbereich auf. Mehrere Bohrer um eine Basis machen sie schneller.",
              "",
              "&eWas herauskommt:&r Jedes Erz hat ein Gewicht, das vom Biom und von der eingestellten Abbautiefe abhängt. Eisen hat zwischen Y 5 und Y 68 ein hohes Gewicht. Die genauen Werte zeigt JEI.",
              "",
              "&eKronwerke:&r Ein Laser auf Eisen ist die bequemste Eisenquelle des Packs. Hinter einer Erzverdopplung oder Erzverdreifachung wird daraus ein Strom von Stahl für das Ziel &6Der Ofen schläft nie&r.",
          ],
          tasks=[task_item("industrialforegoing:ore_laser_base", 1), task_item("industrialforegoing:laser_drill", 2)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:raw_iron", 64), reward_xp(20)],
          deps=["frame_adv"], icon="industrialforegoing:ore_laser_base", size=2.5, shape="gear"),

    quest("lens", 21.4, 3.4, "&6Laserlinsen",
          subtitle="Sag dem Laser, was du willst.",
          description=[
              "Eine &6Laserlinse&r in der Laserbasis erhöht das Gewicht eines Erzes deutlich, sie wird dabei nicht verbraucht. Die Farbe entscheidet: &6Braun&r für Eisen, andere Farben für andere Erze, JEI zeigt die Zuordnung.",
              "",
              "Linsen macht der Auflösungsapparat aus vier Glasscheiben, einem Farbstoff und 250 mB Latex.",
          ],
          tasks=[task_item("industrialforegoing:brown_laser_lens", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32)],
          deps=["laser"], optional=True),

    # ---- Transport -----------------------------------------------------------
    quest("conveyor", 10.4, -2, "&eFörderband",
          subtitle="Gegenstände, Mobs und Flüssigkeiten auf Reisen.",
          description=[
              "Sechs Kunststoff, zwei Eisen und ein Redstone ergeben sechs &6Förderbänder&r. Sie tragen Gegenstände und Tiere, auch bergauf und bergab, und Flüssigkeiten auf ebener Strecke.",
              "",
              "&eUpgrades&r kommen per Rechtsklick auf das Band: Herausziehen aus einer Kiste, Einfügen in eine Kiste, Erkennen, Abwerfen, Hochschleudern, Aufteilen. Fast alle lassen sich im Fenster filtern.",
              "",
              "Glowstein macht ein Band sehr schnell, Kunststoff verhindert, dass du die Gegenstände darauf einsammelst.",
          ],
          tasks=[task_item("industrialforegoing:conveyor", 12)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["plastic"]),

    quest("transporters", 13, -2, "&bTransporter",
          subtitle="Von Block zu Block.",
          description=[
              "&6Gegenstands-&r und &6Flüssigkeitstransporter&r verbinden zwei Inventare, die einen Block auseinander liegen. Ein Transporter sitzt an der Seite, aus der gezogen wird, ein zweiter an der Seite, in die eingefügt wird.",
              "",
              "Rechtsklick auf die Mitte wechselt zwischen Einfügen und Herausziehen. Im Fenster filterst du, Schleichen und Rechtsklick nimmt einen Transporter wieder ab. Geschwindigkeits- und Effizienz-Addons beschleunigen ihn.",
              "",
              "&eRezept:&r Redstone in die Ecken, eine Enderperle oben, Gold (oder Lapis für Flüssigkeiten) links und rechts, ein Kolben unten, das Primitive Gehäuse in der Mitte. Das ergibt zwei.",
          ],
          tasks=[task_item("industrialforegoing:item_transporter_type", 2), task_item("industrialforegoing:fluid_transporter_type", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["conveyor"], icon="industrialforegoing:item_transporter_type"),
]

images = [
    banner("industrial/title", "Industrial Foregoing", 9, -5.2, height=1.6, kind="title", colour="nature"),
    banner("industrial/latex", "Latex und Plastik", 3.8, -1.5, height=0.9, colour="stone"),
    banner("industrial/transport", "Transport", 11.7, -3.4, height=0.9, colour="water"),
    banner("industrial/fields", "Felder und Strom", 4.4, 3.2, height=0.9, colour="nature"),
    banner("industrial/mobs", "Mobs", 13, 3.2, height=0.9, colour="fire"),
    banner("industrial/laser", "Laserbohrer", 19.4, 0.3, height=0.9, colour="brass"),
]

chapter(C, "Industrial Foregoing", "industrialforegoing:plastic", "tech", quests, shape="square", order=22, stage=3,
        subtitle=["Stufe 3: Latex und Kunststoff, Gehäuse, Felder, Mobs und der Laserbohrer."], images=images)
