"""Industrial Foregoing in stage 3, one step per quest: the pity frame, latex from logs, the
latex processing unit, dry rubber, plastic, gears, the dissolution chamber and the four machine
frame tiers (latex, pink slime, ether gas), addons, the pitiful and biofuel generators, plant
and mob automation, the ore laser base with laser drill and lenses, the ore meat chain
(washing factory, fermentation station, fluid sieving machine), conveyors and transporters,
and four checklists of every machine with its power use. Numbers come from the recipes, the
in-jar Patchouli manual and config/industrialforegoing. Kronwerke changes no Industrial
Foregoing recipe."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "industrial"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Latex und Kunststoff ------------------------------------------------
    quest("welcome", 0, 1, "&a&lBau zwei Primitive Maschinengehäuse",
          subtitle="Das Gehäuse der ersten Maschinen.",
          description=[
              "Vier &6Stämme&r in die Ecken, vier &6Eisenbarren&r an die Seiten, ein &6Redstoneblock&r in die Mitte ergeben ein &6Primitives Maschinengehäuse&r.",
              "",
              "&aIndustrial Foregoing&r baut Maschinen, die Felder ernten, Tiere versorgen, Mobs verarbeiten und mit dem Laser Erz bohren. Der Mod öffnet mit &6Stufe 3&r. Jede Maschine sitzt in einem von vier Gehäusen: Primitiv, Einfach, Fortschrittlich, Überlegen.",
              "",
              "Ein Buch, ein Redstone und ein Erdblock formlos ergeben das &6Industrial Foregoing: Handbuch&r.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_pity", 2)],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_table("s3_common")],
          icon="industrialforegoing:machine_frame_pity", size=2.0, shape="hexagon"),

    quest("extractor", 2.5, 0, "&6Bau einen Flüssigkeitsextraktor",
          subtitle="Er zapft Latex aus einem Stamm.",
          description=[
              "Eisen, &6Wägeplatte (Gold)&r, Eisen oben, &6Bruchstein&r, Primitives Gehäuse, Bruchstein in der Mitte, Eisen, &6Kolben&r, Eisen unten.",
              "",
              "Vorderseite an einen &6Stamm&r stellen. Er zieht &6Latex&r heraus: &eAkazie und Mangrove 4 mB&r pro Vorgang, Kirsche und Schwarzeiche 3, Eiche, Birke, Fichte und Tropenholz 2, alle anderen Stämme 1. Der Stamm wird erst entrindet, dann verbraucht.",
              "",
              "Strom ist freiwillig, &d500 FE&r pro Vorgang machen ihn schneller. Mehrere Extraktoren dürfen denselben Stamm anzapfen.",
          ],
          tasks=[task_item("industrialforegoing:fluid_extractor", 2)],
          rewards=[reward_item("minecraft:oak_log", 32)],
          deps=["welcome"]),

    quest("latex", 5, 0, "&6Füll einen Eimer Latex",
          subtitle="Der Rohstoff für Gummi.",
          description=[
              "Lass die Extraktoren laufen, bis &e1 000 mB Latex&r zusammen sind, und füll sie in einen Eimer. Jeder Extraktor hat einen Tank für 1 000 mB.",
              "",
              "Latex brauchst du für Gummi, für das Einfache Gehäuse, für Laserlinsen und für alle Addons. Ein Kreis aus vier bis acht Extraktoren um eine Säule aus Stämmen ist ein guter Anfang.",
          ],
          tasks=[task_item("industrialforegoing:latex_bucket", 1)],
          rewards=[reward_item("minecraft:bucket", 2), reward_item("minecraft:birch_log", 32)],
          deps=["extractor"], icon="industrialforegoing:latex_bucket"),

    quest("latex_unit", 7.5, 0, "&eBau eine Latexverarbeitungsmaschine",
          subtitle="Latex und Wasser werden Gummi.",
          description=[
              "Eisen in die Ecken, ein &6Redstoneblock&r oben, &6Eimer&r links und rechts, ein &6Ofen&r unten, das Primitive Gehäuse in der Mitte.",
              "",
              "Sie macht aus &e750 mB Latex&r und &e500 mB Wasser&r einen &6Gummiklumpen&r und zieht &d20 FE/t&r. Stell sie direkt an die Extraktoren und gib ihr eine Wasserquelle.",
          ],
          tasks=[task_item("industrialforegoing:latex_processing_unit", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(5)],
          deps=["latex"], icon="industrialforegoing:latex_processing_unit"),

    quest("dryrubber", 10, 0, "&eMach Gummiklumpen",
          subtitle="Der Vorgänger von Kunststoff.",
          description=[
              "Lass die Latexverarbeitung laufen, bis &e16 Gummiklumpen&r fertig sind.",
              "",
              "Jeder Klumpen kostet 750 mB Latex. Bei 1 bis 4 mB pro Extraktorvorgang ist der Extraktor der Engpass, nicht die Maschine. Mehr Extraktoren an Akazie oder Mangrove, mehr Gummi.",
          ],
          tasks=[task_item("industrialforegoing:dryrubber", 16)],
          rewards=[reward_item("industrialforegoing:latex_bucket", 1), reward_xp(5)],
          deps=["latex_unit"], icon="industrialforegoing:dryrubber"),

    quest("plastic", 12.5, 0, "&f&lSchmilz Gummi zu Kunststoff",
          subtitle="Das Material, aus dem dieser Mod gebaut ist.",
          description=[
              "Ein &6Gummiklumpen&r im Ofen ergibt einen &6Kunststoff&r.",
              "",
              "Fast jede Maschine braucht zwei bis vier, ein Förderband-Rezept sechs. Ein Stapel ist ein gutes erstes Ziel, lass die Extraktoren Tag und Nacht laufen.",
              "",
              "&eGut zu wissen:&r Die &6Plastikplatte&r aus Oritech zählt in allen Rezepten dieses Mods ebenfalls als Kunststoff.",
              "",
              pic("industrialforegoing:plastic"),
          ],
          tasks=[task_item("industrialforegoing:plastic", 32)],
          rewards=[reward_item("industrialforegoing:plastic", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["dryrubber"], size=1.5, shape="hexagon"),

    quest("pitiful", 2.5, 2, "&cStell einen Primitiven Heizgenerator auf",
          subtitle="30 FE/t aus Kohle, mehr nicht.",
          description=[
              "&6Bruchstein&r in die Ecken, ein &6Goldbarren&r oben, &6Eisengitter&r links und rechts, ein &6Ofen&r unten, das Primitive Gehäuse in der Mitte.",
              "",
              "Er verbrennt alles, was im Ofen brennt, für &d30 FE/t&r, Puffer 100 000 FE. Er verbrennt auch weiter, wenn der Puffer voll ist. Für den Anfang reicht er, später ersetzt ihn der Biogenerator.",
          ],
          tasks=[task_item("industrialforegoing:pitiful_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 4)],
          deps=["welcome"]),

    quest("gears", 5, 2, "&7Bau Zahnräder aus Eisen, Gold und Diamant",
          subtitle="Vier Stück im Kreuz, ein Zahnrad.",
          description=[
              "Vier &6Eisenbarren&r im Kreuz, Mitte frei, ergeben ein &6Eisenzahnrad&r. Genauso mit vier &6Goldbarren&r und vier &6Diamanten&r.",
              "",
              "Eisen geht in Sämaschine und Abwassermaschinen, Gold in Erntemaschine und Laserbohrer, Diamant in Auflösungsapparat, Bioreaktor und alle Laserbasen.",
          ],
          tasks=[task_item("industrialforegoing:iron_gear", 2), task_item("industrialforegoing:gold_gear", 2), task_item("industrialforegoing:diamond_gear", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["welcome"], icon="industrialforegoing:diamond_gear"),

    # ---- Gehäuse -------------------------------------------------------------
    quest("dissolution", 0, 5.5, "&9Bau einen Auflösungsapparat",
          subtitle="Bis zu acht Zutaten und eine Flüssigkeit.",
          description=[
              "Kunststoff, &6Holztruhe&r, Kunststoff oben, &6Eimer&r, Primitives Gehäuse, Eimer in der Mitte, &6Goldbarren&r, &6Diamantzahnrad&r, Goldbarren unten.",
              "",
              "Der Zusammenbautisch des Mods: bis zu &eacht Gegenstände&r und &eeine Flüssigkeit&r, formlos. Gehäuse, Linsen, Addons und Pinke Schleimbarren entstehen hier. Er zieht &d90 FE/t&r.",
          ],
          tasks=[task_item("industrialforegoing:dissolution_chamber", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["plastic", "gears"]),

    quest("frame_simple", 2.5, 5.5, "&7Bau ein Einfaches Maschinengehäuse",
          subtitle="Gehäuse Stufe 2, mit Latex.",
          description=[
              "Im Auflösungsapparat: zwei &6Kunststoff&r, ein &6Primitives Gehäuse&r, zwei &6Netherziegel&r, zwei &6Eisenbarren&r, ein &6Goldzahnrad&r und &e250 mB Latex&r.",
              "",
              "Laserbohrer, Düngemaschine, Hydrokultur-Beet, Fermentationsstation und Fischmaschine sitzen in diesem Gehäuse. Mach gleich zwei.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_simple", 2)],
          rewards=[reward_item("minecraft:nether_bricks", 16), reward_table("s3_common"), reward_xp(10)],
          deps=["dissolution"], size=1.5, shape="square"),

    quest("slaughter", 5, 5.5, "&dFang Pinken Schleim auf",
          subtitle="Der Industrielle Schlachter.",
          description=[
              "Kunststoff, &6Goldzahnrad&r, Kunststoff oben, &6Eisenschwerter&r links und rechts vom Primitiven Gehäuse, &6Eisenäxte&r und Redstone unten ergeben den &6Industriellen Schlachter&r.",
              "",
              "Er tötet Tiere und Mobs in seinem Bereich, ohne Beute und Erfahrung, für &d400 FE&r pro Vorgang. Heraus kommen &6Flüssigfleisch&r und &dPinker Schleim&r. Friedliche Tiere geben mehr Schleim.",
              "",
              "Eine Hühnerfarm mit einem Tierfütterer daneben reicht für den Anfang.",
          ],
          tasks=[task_item("industrialforegoing:mob_slaughter_factory", 1), task_item("industrialforegoing:pink_slime_bucket", 1)],
          rewards=[reward_item("minecraft:egg", 16), reward_xp(5)],
          deps=["frame_simple", "mit"], icon="industrialforegoing:mob_slaughter_factory"),

    quest("frame_adv", 7.5, 5.5, "&6Bau ein Fortschrittliches Maschinengehäuse",
          subtitle="Gehäuse Stufe 3, mit Pinkem Schleim.",
          description=[
              "Im Auflösungsapparat: zwei &6Kunststoff&r, ein &6Einfaches Gehäuse&r, zwei &6Netheritplatten&r, zwei &6Goldbarren&r, ein &6Diamantzahnrad&r und &e500 mB Pinker Schleim&r.",
              "",
              "Netheritplatten schmilzt du aus Antikem Schrott im Nether. Erz-Laserbasis, Monsterschnetzler, Monsterspawner, Waschfabrik und die Verzauberungsmaschinen brauchen dieses Gehäuse.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_advanced", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 1), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["slaughter"], size=1.5, shape="square"),

    quest("fluid_laser", 10, 5.5, "&5Bohr Ethergas aus einem Wither",
          subtitle="Flüssigkeits-Laserbasis über einem Wither.",
          description=[
              "&6Flüssigkeits-Laserbasis:&r wie die Erz-Laserbasis, nur mit &6Eimern&r statt Eisenerz. Eine &6Lila Laserlinse&r hinein, ein Laserbohrer daneben, direkt darunter ein &cWither&r.",
              "",
              "Jeder Vorgang gibt &e10 mB Ethergas&r. Den Wither hältst du in einer Stasiskammer fest. Dieselbe Basis bohrt mit Oranger Linse im Nether Lava und mit Schwarzer Linse über Ozean oder Wüste Öl für PneumaticCraft.",
          ],
          tasks=[task_item("industrialforegoing:fluid_laser_base", 1), task_item("industrialforegoing:ether_gas_bucket", 1)],
          rewards=[reward_item("minecraft:soul_sand", 8), reward_xp(20)],
          deps=["frame_adv", "laser_drill"], icon="industrialforegoing:ether_gas_bucket"),

    quest("frame_supreme", 12.5, 5.5, "&5&lBau ein Überlegenes Maschinengehäuse",
          subtitle="Gehäuse Stufe 4, mit Ethergas.",
          description=[
              "Im Auflösungsapparat: zwei &6Kunststoff&r, ein &6Fortschrittliches Gehäuse&r, zwei &6Netheritbarren&r, zwei &6Diamanten&r, ein &6Diamantzahnrad&r und &e135 mB Ethergas&r.",
              "",
              "Der &6Witherfabrikator&r sitzt darin und baut mit drei Witherskeletschädeln und vier Seelensand selbst einen Wither, für &d20 000 FE&r pro Vorgang. Damit läuft das Ethergas ohne dich.",
          ],
          tasks=[task_item("industrialforegoing:machine_frame_supreme", 1)],
          rewards=[reward_item("minecraft:netherite_ingot", 1), reward_table("s3_uncommon"), reward_xp(25)],
          deps=["fluid_laser"], size=1.5, shape="square"),

    quest("addons", 2.5, 7.5, "&9Steck Addons in deine Maschinen",
          subtitle="Schneller, sparsamer, mehr pro Vorgang.",
          description=[
              "Im Auflösungsapparat mit &e1 000 mB Latex&r, je zwei &6Redstone&r, zwei &6Glasscheiben&r, zwei &6Goldzahnräder&r und: zwei &6Zucker&r für Geschwindigkeit, zwei &6Lohenruten&r für Effizienz, &6Ofen&r und &6Werkbank&r für Verarbeitung.",
              "",
              "Geschwindigkeit: der Fortschritt läuft +1 pro Tick schneller. Verarbeitung: +1 Vorgang je Durchlauf. Stufe 2, mit Diamantzahnrädern statt Gold, gibt +2. &6Reichweite&r (Glas, Redstone und vier Bruchstein, Lapis und so weiter bis Stufe 11) vergrößert den Arbeitsbereich um 1 je Stufe.",
          ],
          tasks=[task_item("industrialforegoing:speed_addon_tier_1", 1), task_item("industrialforegoing:efficiency_addon_tier_1", 1)],
          rewards=[reward_item("minecraft:sugar", 16), reward_item("minecraft:blaze_rod", 4), reward_xp(10)],
          deps=["dissolution"], icon="industrialforegoing:speed_addon_tier_1"),

    # ---- Felder und Strom ----------------------------------------------------
    quest("sower", 0, 10.5, "&2Stell eine Sämaschine auf",
          subtitle="Pflanzt Samen und Setzlinge.",
          description=[
              "Kunststoff, &6Blumentopf&r, Kunststoff oben, &6Kolben&r links und rechts vom Primitiven Gehäuse, &6Eisenzahnräder&r und Redstone unten.",
              "",
              "Ihre neun Plätze sind farbig, jede Farbe gehört zu einem Neuntel des Feldes, wie die Markierung oben auf der Maschine zeigt. &d1 000 FE&r pro Vorgang.",
          ],
          tasks=[task_item("industrialforegoing:plant_sower", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["plastic", "gears"], icon="industrialforegoing:plant_sower"),

    quest("gatherer", 2.5, 10.5, "&2Stell eine Erntemaschine auf",
          subtitle="Erntet Felder und fällt ganze Bäume.",
          description=[
              "Kunststoff, &6Eisenhacke&r, Kunststoff oben, &6Eisenäxte&r links und rechts vom Primitiven Gehäuse, &6Goldzahnräder&r und Redstone unten.",
              "",
              "Sie erntet reife Pflanzen und fällt Bäume mit allem, was daran hängt, &d400 FE&r pro Vorgang. Dabei fällt &6Schlamm&r an. Mit etwas Ethergas pflanzt sie gleich wieder nach.",
              "",
              "&eKronwerke:&r Ein Baumfeld aus Sämaschine und Erntemaschine liefert Stämme für die Extraktoren und Holzkohle für Stahl.",
          ],
          tasks=[task_item("industrialforegoing:plant_gatherer", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 16), reward_xp(5)],
          deps=["sower"], icon="industrialforegoing:plant_gatherer"),

    quest("sewer", 5, 10.5, "&6Sammel Gülle und mach Dünger",
          subtitle="Was Tiere hinterlassen.",
          description=[
              "&6Güllesammler:&r Kunststoff, Eimer, Kunststoff oben, Ziegel um das Primitive Gehäuse, Eisenzahnrad unten. Er sammelt &6Gülle&r von Tieren und macht aus Erfahrungskugeln &aEssenz&r.",
              "",
              "Der &6Güllekomposter&r (&d40 FE/t&r) macht aus Gülle &6Dünger&r. Der geht in die Düngemaschine oder das Hydrokultur-Beet.",
          ],
          tasks=[task_item("industrialforegoing:sewer", 1), task_item("industrialforegoing:fertilizer", 16)],
          rewards=[reward_item("minecraft:wheat", 32)],
          deps=["gatherer"], icon="industrialforegoing:fertilizer", optional=True),

    quest("bio", 2.5, 12.5, "&dBetreib einen Biogenerator",
          subtitle="160 FE/t aus Samen und Setzlingen.",
          description=[
              "&6Bioreaktor:&r Kunststoff, Diamantzahnrad, Kunststoff oben, Schleimbälle ums Gehäuse, Ziegel, Zucker, Ziegel unten. &6Biogenerator:&r Kunststoff, Ofen, Kunststoff oben, Kolben ums Gehäuse, Goldzahnrad, Kolben, Goldzahnrad unten.",
              "",
              "Der Reaktor macht aus Wasser und Samen, Setzlingen, Farbstoffen und Köpfen &dBiokraftstoff&r. Eine Sorte gibt 80 mB pro Stück, vier verschiedene je 110 mB. Der Generator macht daraus &d160 FE/t&r und hört auf, wenn sein Puffer von 1 Million voll ist.",
          ],
          tasks=[task_item("industrialforegoing:bioreactor", 1), task_item("industrialforegoing:biofuel_generator", 1)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["gatherer"], icon="industrialforegoing:biofuel_generator"),

    # ---- Mobs ----------------------------------------------------------------
    quest("mit", 7.5, 10.5, "&5Bau ein Mobfanggerät",
          subtitle="Ein Mob zum Mitnehmen.",
          description=[
              "Vier &6Kunststoff&r im Kreuz um eine &6Ghastträne&r ergeben das &6Mobfanggerät&r.",
              "",
              "Rechtsklick auf ein Tier steckt es hinein, Rechtsklick auf den Boden lässt es frei. So bringst du Kühe in den Stall, und der Monsterspawner braucht einen gefangenen Mob als Vorlage.",
          ],
          tasks=[task_item("industrialforegoing:mob_imprisonment_tool", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 1)],
          deps=["plastic"]),

    quest("crusher", 10, 10.5, "&cStell einen Monsterschnetzler auf",
          subtitle="Beute und Essenz ohne Schwert.",
          description=[
              "Kunststoff, &6Eisenschwert&r, Kunststoff oben, &6Bücher&r links und rechts vom &6Fortschrittlichen Gehäuse&r, Goldzahnräder und Redstone unten.",
              "",
              "Er tötet Mobs, als hätte ein Spieler zugeschlagen: Beute plus &aEssenz&r, &d50 FE&r pro Vorgang. Im zweiten Modus gibt es statt Essenz Beute mit zufälligem Glück. Essenz füllt Verzauberungsmaschinen, und der Auflösungsapparat macht aus 250 mB eine Erfahrungsflasche.",
          ],
          tasks=[task_item("industrialforegoing:mob_crusher", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(10)],
          deps=["frame_adv"], optional=True),

    quest("duplicator", 12.5, 10.5, "&cStell einen Monsterspawner auf",
          subtitle="Ein gefangener Mob, beliebig viele Kopien.",
          description=[
              "Kunststoff, &6Netherwarze&r, Kunststoff oben, &6Magmacreme&r links und rechts vom Fortschrittlichen Gehäuse, &6Smaragde&r und Redstone unten.",
              "",
              "Ein Mobfanggerät mit Mob hinein, dazu &aEssenz&r und &d5 000 FE&r pro Vorgang. Er spawnt Kopien um sich herum und hört auf, wenn zu viele in der Nähe sind. Mit dem Monsterschnetzler daneben ist das eine Mobfarm ohne Spawner.",
          ],
          tasks=[task_item("industrialforegoing:mob_duplicator", 1)],
          rewards=[reward_item("minecraft:emerald", 8), reward_xp(15)],
          deps=["crusher"], optional=True),

    # ---- Laserbohrer ---------------------------------------------------------
    quest("laser_drill", 0, 15.3, "&cBau zwei Laserbohrer",
          subtitle="Sie laden jede Laserbasis in Reichweite.",
          description=[
              "Kunststoff, &6Diamantzahnrad&r, Kunststoff oben, &6Kolben&r links und rechts vom &6Einfachen Gehäuse&r, &6Goldzahnräder&r und Redstone unten.",
              "",
              "Ein Bohrer mit Strom, &d1 000 FE&r pro Vorgang, lädt die erste Erz- oder Flüssigkeits-Laserbasis in seinem Arbeitsbereich. Mehrere Bohrer um eine Basis machen sie schneller.",
          ],
          tasks=[task_item("industrialforegoing:laser_drill", 2)],
          rewards=[reward_item("minecraft:piston", 4), reward_xp(10)],
          deps=["frame_simple"], icon="industrialforegoing:laser_drill"),

    quest("laser", 2.75, 15.3, "&c&lBau eine Erz-Laserbasis",
          subtitle="Erze ohne Bergbau.",
          description=[
              "Kunststoff, &6Diamantspitzhacke&r, Kunststoff oben, &6Eisenerz&r links und rechts vom &6Fortschrittlichen Gehäuse&r, &6Diamantzahnräder&r und Redstone unten.",
              "",
              "Voll geladen von den Laserbohrern erzeugt sie ein Erz. Jedes Erz hat ein Gewicht je nach Biom und eingestellter Tiefe: Rohes Eisen zwischen Y 5 und 68 Gewicht 20, sonst 3. JEI zeigt alle Werte.",
              "",
              "&eKronwerke:&r Ein Laser auf Eisen ist die bequemste Eisenquelle des Packs. Hinter einer Erzverdreifachung wird daraus Stahl für das Ziel &6Der Ofen schläft nie&r.",
          ],
          tasks=[task_item("industrialforegoing:ore_laser_base", 1)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:raw_iron", 64), reward_xp(25)],
          deps=["frame_adv", "laser_drill"], icon="industrialforegoing:ore_laser_base", size=2.5, shape="gear"),

    quest("lens", 5.5, 15.3, "&6Setz eine Laserlinse ein",
          subtitle="Sag dem Laser, was du willst.",
          description=[
              "Im Auflösungsapparat: vier &6Glasscheiben&r, ein &6Farbstoff&r und &e250 mB Latex&r ergeben eine &6Laserlinse&r in der Farbe des Farbstoffs.",
              "",
              "In der Basis hebt sie das Gewicht ihres Erzes stark an und wird nicht verbraucht. &6Braun&r Eisen, &6Orange&r Kupfer, &6Gelb&r Gold, &6Hellgrau&r Osmium, &6Schwarz&r Kohle, &6Hellgrün&r Uran. Die übrigen zeigt JEI.",
          ],
          tasks=[task_item("industrialforegoing:brown_laser_lens", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_xp(10)],
          deps=["laser"], optional=True),

    # ---- Erzfleisch ----------------------------------------------------------
    quest("washing", 8.5, 15.3, "&4Bau eine Waschfabrik",
          subtitle="Erz und Flüssigfleisch werden Rohes Erzfleisch.",
          description=[
              "&6Pinke Schleimbarren&r oben links und rechts, ein &6Fleischfütterer&r oben in der Mitte, Kunststoff ums &6Fortschrittliche Gehäuse&r, Diamantzahnräder und ein Ofen unten. Pinker Schleimbarren: zwei Eisen, zwei Gold und 1 000 mB Pinker Schleim im Auflösungsapparat.",
              "",
              "&eRein:&r ein Erz und &6Flüssigfleisch&r vom Schlachter. &eRaus:&r &6Rohes Erzfleisch&r dieses Erzes. Sie zieht &d60 FE/t&r.",
          ],
          tasks=[task_item("industrialforegoing:washing_factory", 1)],
          rewards=[reward_item("industrialforegoing:meat_bucket", 1), reward_xp(10)],
          deps=["frame_adv"], icon="industrialforegoing:washing_factory"),

    quest("fermentation", 11, 15.3, "&4Lass Erzfleisch gären",
          subtitle="Länger gären, mehr Ausbeute.",
          description=[
              "Kunststoff in die Ecken, &6Stämme&r an die Seiten, ein &6Goldzahnrad&r in die Mitte, das &6Einfache Gehäuse&r unten ergeben die &6Fermentationsstation&r.",
              "",
              "&eRein:&r Rohes Erzfleisch. Sie versiegelt, sobald der eingestellte Füllstand erreicht ist, und gärt. &eRaus:&r Fermentiertes Erzfleisch: doppelt nach 5 Sekunden, dreifach nach 45, vierfach nach 2 Minuten, fünffach nach 5 Minuten. &d40 FE/t&r.",
          ],
          tasks=[task_item("industrialforegoing:fermentation_station", 1)],
          rewards=[reward_item("minecraft:oak_log", 16), reward_xp(10)],
          deps=["washing"], icon="industrialforegoing:fermentation_station"),

    quest("sieving", 13.5, 15.3, "&4&lSieb Erzstaub aus dem Fleisch",
          subtitle="Fermentiertes Erzfleisch und Sand werden Staub.",
          description=[
              "Kunststoff, &6Pinker Schleimball&r, Kunststoff oben, drei &6Eisengitter&r in der Mitte, &6Goldzahnräder&r ums &6Fortschrittliche Gehäuse&r unten.",
              "",
              "&eRein:&r Fermentiertes Erzfleisch und &6Sand&r. &eRaus:&r Staub des Erzes, mit dem alles angefangen hat. &d40 FE/t&r. Den Staub schmilzt du im Ofen zu Barren.",
              "",
              "Pinker Schleimball: eine Glasscheibe und 300 mB Pinker Schleim im Auflösungsapparat.",
          ],
          tasks=[task_item("industrialforegoing:fluid_sieving_machine", 1)],
          rewards=[reward_item("minecraft:sand", 64), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["fermentation"], icon="industrialforegoing:fluid_sieving_machine", size=1.5, shape="hexagon"),

    # ---- Transport -----------------------------------------------------------
    quest("conveyor", 0, 19, "&eLeg Förderbänder",
          subtitle="Gegenstände, Mobs und Flüssigkeiten auf Reisen.",
          description=[
              "Sechs &6Kunststoff&r, zwei &6Eisen&r und ein &6Redstone&r ergeben sechs &6Förderbänder&r.",
              "",
              "Sie tragen Gegenstände und Tiere bergauf und bergab. Upgrades per Rechtsklick: Herausziehen, Einfügen, Erkennen, Abwerfen, Hochschleudern, Aufteilen, Blinken. Fast alle lassen sich filtern.",
          ],
          tasks=[task_item("industrialforegoing:conveyor", 12)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["plastic"]),

    quest("transporters", 2.5, 19, "&bVerbinde zwei Inventare mit Transportern",
          subtitle="Von Block zu Block.",
          description=[
              "Redstone in die Ecken, eine &6Enderperle&r oben, &6Gold&r links und rechts (&6Lapis&r für Flüssigkeiten; Trichter statt Gold und Spender statt Kolben für den Weltentransporter), ein &6Kolben&r unten, das Primitive Gehäuse in der Mitte. Das ergibt zwei.",
              "",
              "Ein Transporter auf der Seite, aus der gezogen wird, einer auf der Seite, in die eingefügt wird. Rechtsklick auf die Mitte wechselt die Richtung, im Fenster filterst du.",
          ],
          tasks=[task_item("industrialforegoing:item_transporter_type", 2), task_item("industrialforegoing:fluid_transporter_type", 2)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["conveyor"], icon="industrialforegoing:item_transporter_type"),

    # ---- Checklisten ---------------------------------------------------------
    quest("list_core", 6, 19, "&6&lHak die Grundmaschinen ab",
          subtitle="Latex, Strom und Werkstatt, mit Stromverbrauch.",
          description=[
              "&6Flüssigkeitsextraktor:&r Primitiv, 500 FE pro Vorgang, freiwillig.",
              "&6Latexverarbeitung:&r Primitiv, 20 FE/t. &6Auflösungsapparat:&r Primitiv, 90 FE/t.",
              "&6Primitiver Heizgenerator:&r Primitiv, liefert 30 FE/t.",
              "&6Bioreaktor:&r Primitiv, 400 FE pro Vorgang. &6Biogenerator:&r Primitiv, liefert 160 FE/t.",
              "&6Schlammraffinerie:&r Primitiv, 40 FE/t, verarbeitet den Schlamm der Erntemaschine.",
              "&6Farbmischer:&r Primitiv, 30 FE/t. &6Material-StoneWork-Fabrik:&r Fortschrittlich, 60 FE/t, Bruchstein aus Wasser und Lava.",
          ],
          tasks=[task_item("industrialforegoing:fluid_extractor", 1), task_item("industrialforegoing:latex_processing_unit", 1),
                 task_item("industrialforegoing:dissolution_chamber", 1), task_item("industrialforegoing:pitiful_generator", 1),
                 task_item("industrialforegoing:bioreactor", 1), task_item("industrialforegoing:biofuel_generator", 1),
                 task_item("industrialforegoing:sludge_refiner", 1), task_item("industrialforegoing:dye_mixer", 1),
                 task_item("industrialforegoing:material_stonework_factory", 1)],
          rewards=[reward_item("industrialforegoing:plastic", 16), reward_xp(15)],
          deps=["transporters", "bio"], icon="industrialforegoing:dissolution_chamber", size=1.5, shape="gear"),

    quest("list_farm", 8.5, 19, "&6&lHak die Feld- und Tiermaschinen ab",
          subtitle="Pflanzen und Tiere, mit Stromverbrauch.",
          description=[
              "&6Sämaschine:&r Primitiv, 1 000 FE pro Vorgang. &6Erntemaschine:&r Primitiv, 400 FE.",
              "&6Düngemaschine:&r Einfach, 1 000 FE. &6Hydrokultur-Beet:&r Einfach, 1 000 FE.",
              "&6Güllesammler:&r Primitiv, 10 FE. &6Güllekomposter:&r Primitiv, 40 FE/t.",
              "&6Tierfütterer:&r Primitiv, 400 FE. &6Tierfarmer:&r Primitiv, 400 FE, schert und melkt.",
              "&6Tierbabyseparator:&r Primitiv, 400 FE. &6Fischmaschine:&r Einfach, 5 000 FE.",
          ],
          tasks=[task_item("industrialforegoing:plant_sower", 1), task_item("industrialforegoing:plant_gatherer", 1),
                 task_item("industrialforegoing:plant_fertilizer", 1), task_item("industrialforegoing:hydroponic_bed", 1),
                 task_item("industrialforegoing:sewer", 1), task_item("industrialforegoing:sewage_composter", 1),
                 task_item("industrialforegoing:animal_feeder", 1), task_item("industrialforegoing:animal_rancher", 1),
                 task_item("industrialforegoing:animal_baby_separator", 1), task_item("industrialforegoing:marine_fisher", 1)],
          rewards=[reward_item("minecraft:bone_meal", 64), reward_xp(15)],
          deps=["list_core"], icon="industrialforegoing:plant_gatherer", size=1.5, shape="gear"),

    quest("list_mobs", 11, 19, "&6&lHak die Mob- und Verzauberungsmaschinen ab",
          subtitle="Mobs, Essenz und Bücher, mit Stromverbrauch.",
          description=[
              "&6Industrieller Schlachter:&r Primitiv, 400 FE pro Vorgang. &6Monsterschnetzler:&r Fortschrittlich, 50 FE.",
              "&6Monsterspawner:&r Fortschrittlich, 5 000 FE. &6Mobdetektor:&r Einfach, 400 FE.",
              "&6Stasiskammer:&r Fortschrittlich, 1 000 FE, friert Mobs ein und heilt sie.",
              "&6Verzauberungsextraktor, -applikator, -fabrik, -sortierer:&r Fortschrittlich, je 40 FE/t.",
              "&6Witherfabrikator:&r Überlegen, 20 000 FE.",
          ],
          tasks=[task_item("industrialforegoing:mob_slaughter_factory", 1), task_item("industrialforegoing:mob_crusher", 1),
                 task_item("industrialforegoing:mob_duplicator", 1), task_item("industrialforegoing:mob_detector", 1),
                 task_item("industrialforegoing:stasis_chamber", 1), task_item("industrialforegoing:enchantment_extractor", 1),
                 task_item("industrialforegoing:enchantment_applicator", 1), task_item("industrialforegoing:enchantment_factory", 1),
                 task_item("industrialforegoing:enchantment_sorter", 1), task_item("industrialforegoing:wither_builder", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 32), reward_xp(20)],
          deps=["list_farm"], icon="industrialforegoing:mob_crusher", size=1.5, shape="gear"),

    quest("list_resources", 13.5, 19, "&6&lHak die Rohstoffmaschinen ab",
          subtitle="Erz, Flüssigkeiten und Blöcke, mit Stromverbrauch.",
          description=[
              "&6Laserbohrer:&r Einfach, 1 000 FE pro Vorgang. Erz- und Flüssigkeits-Laserbasis: Fortschrittlich, ohne eigenen Strom.",
              "&6Waschfabrik:&r Fortschrittlich, 60 FE/t. &6Fermentationsstation:&r Einfach, 40 FE/t. &6Flüssigkeitssiebmaschine:&r Fortschrittlich, 40 FE/t.",
              "&6Blockbrecher, Blockplatzierer, Flüssigkeitskollektor, Flüssigkeitsplatzierer, Wassergenerator:&r Primitiv, je 1 000 FE pro Vorgang.",
              "&6Heizgenerator&r (Resourceful Furnace): Primitiv, 40 FE/t, drei Öfen in einem, 2 mB Essenz pro Stück. &6Sporenzüchter:&r Primitiv, 40 FE/t.",
          ],
          tasks=[task_item("industrialforegoing:laser_drill", 1), task_item("industrialforegoing:ore_laser_base", 1),
                 task_item("industrialforegoing:fluid_laser_base", 1), task_item("industrialforegoing:washing_factory", 1),
                 task_item("industrialforegoing:fermentation_station", 1), task_item("industrialforegoing:fluid_sieving_machine", 1),
                 task_item("industrialforegoing:block_breaker", 1), task_item("industrialforegoing:block_placer", 1),
                 task_item("industrialforegoing:fluid_collector", 1), task_item("industrialforegoing:fluid_placer", 1),
                 task_item("industrialforegoing:water_condensator", 1), task_item("industrialforegoing:resourceful_furnace", 1),
                 task_item("industrialforegoing:spores_recreator", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_table("s3_uncommon"), reward_xp(25)],
          deps=["list_mobs"], icon="industrialforegoing:ore_laser_base", size=1.5, shape="gear"),
]

images = [
    head("title", "Industrial Foregoing", 0, -2.6, height=1.6, kind="title", colour="nature"),
    head("latex", "Latex und Kunststoff", 0, -1.1, colour="stone"),
    head("frames", "Gehäuse", 0, 4.0, colour="brass"),
    head("fields", "Felder und Strom", 0, 9.0, colour="nature"),
    head("mobs", "Mobs", 7.0, 9.0, colour="fire"),
    head("laser", "Laserbohrer", 0, 13.5, colour="brass"),
    head("meat", "Erzfleisch", 8.0, 13.5, colour="fire"),
    head("transport", "Transport", 0, 17.5, colour="water"),
    head("lists", "Checklisten", 5.5, 17.5, colour="stone"),
]

chapter(C, "Industrial Foregoing", "industrialforegoing:plastic", "tech", quests, shape="square", order=22, stage=3,
        subtitle=["Stufe 3: Latex und Kunststoff, vier Gehäuse, Felder, Mobs, Laser und Erzfleisch."], images=images)
