"""Oritech in stage 3: nickel, steel, coils and motors, the basic generator and pipes, the
pulverizer, powered furnace, foundry, centrifuge (carbon fibre, plastic) and assembler, the
enderic laser with the target designator, frame machines, addons, the first augments and the
fragment forge ore line. Kronwerke removes the foundry brass, the atomic forge circuits and the
laser certus charging (kubejs/server_scripts/kronwerke/). Numbers follow config/oritech-common."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "oritech"

quests = [
    # ---- Nickel und Stahl ----------------------------------------------------
    quest("nickel", 0, 1, "&6&lOritech",
          subtitle="Maschinen, Laser und ein Körper aus Stahl.",
          description=[
              "&6Oritech&r ist ein großer Technikmod mit Multiblock-Maschinen, Lasern, Robotarmen und am Ende kybernetischen Verbesserungen für deinen eigenen Körper. Mit Stufe 3 ist der Mod offen.",
              "",
              "Das Metall von Oritech ist &6Nickel&r. Nickelerz liegt tief, zwischen Y 40 und dem Grund der Welt, am häufigsten um Y -12. Schmilz das Rohe Nickel im Ofen.",
              "",
              "&eGut zu wissen:&r Nickelbarren aus Immersive Engineering zählen in allen Oritech-Rezepten genauso. Wer davon noch eine Kiste hat, spart sich den ersten Ausflug.",
              "",
              "Für den Anfang: Grab &616 Rohes Nickel&r aus.",
          ],
          tasks=[task_item("oritech:raw_nickel", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s3_common")],
          icon="oritech:nickel_ingot", size=2.0, shape="hexagon"),

    quest("steel", 2.6, 0, "&8Stahl von Oritech",
          subtitle="Eisen und Kohle, sogar an der Werkbank.",
          description=[
              "Oritech hat einen eigenen Stahl, und den gibt es schon an der Werkbank: zwei &6Eisenbarren&r oben, zwei &6Kohle&r oder Holzkohle unten ergeben einen &6Stahlbarren&r.",
              "",
              "Das ist teuer, zwei Eisen für einen Barren. Die &6Gießerei&r weiter rechts macht aus einem Eisen und einem Kohlestaub einen Barren, also doppelt so viel. Alle Oritech-Rezepte nehmen übrigens jeden Stahl, auch den aus Mekanism.",
              "",
              "&eKronwerke:&r Stahl von Oritech zählt am Obelisken wie jeder andere Stahl für das Ziel &6Der Ofen schläft nie&r.",
          ],
          tasks=[task_item("oritech:steel_ingot", 16), task_item("oritech:nickel_ingot", 16)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["nickel"], icon="oritech:steel_ingot"),

    quest("electrum", 2.6, 2, "&eElectrum",
          subtitle="Gold und Redstone.",
          description=[
              "Zwei &6Goldbarren&r oben und zwei &6Redstone&r unten ergeben an der Werkbank einen &6Electrum Ingot&r. In der Gießerei bekommst du einen Barren schon aus einem Gold und einem Redstone.",
              "",
              "Electrum steckt in Energierohren, im angetriebenen Ofen, in der Gießerei und im Enderischen Laser.",
          ],
          tasks=[task_item("oritech:electrum_ingot", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:redstone", 16)],
          deps=["nickel"]),

    quest("coils", 5.2, 0, "&bSpulen, Motoren und Platten",
          subtitle="Die drei Bauteile jeder Maschine.",
          description=[
              "&eMagnetspule:&r Nickel in die obere und untere Reihe, Stahl in die Mitte, das ergibt vier Spulen.",
              "&eMotor:&r ein Nickel oben in der Mitte, darunter zweimal Stahl, Spule, Stahl.",
              "&eKupferverstärkte Platte:&r Stein in die Ecken, Stahl an die Seiten, ein Kupferbarren in die Mitte, das ergibt zwei.",
              "",
              "Fast jede Maschine ab hier braucht Motoren und Platten. Später baut der Zusammenfüger Spulen und Motoren deutlich günstiger.",
          ],
          tasks=[task_item("oritech:magnetic_coil", 8), task_item("oritech:motor", 4), task_item("oritech:machine_plating_block", 8)],
          rewards=[reward_item("oritech:nickel_ingot", 8), reward_xp(5)],
          deps=["steel"], icon="oritech:motor"),

    # ---- Energie -------------------------------------------------------------
    quest("generator", 5.2, 2.4, "&c&lGrundlegender Generator",
          subtitle="Brennstoff rein, Strom raus.",
          description=[
              "&eRezept:&r Nickel in die obere Reihe und an die Seiten, ein Kupferbarren in die Mitte, unten Spule, Ofen, Spule. Der Generator verbrennt, was auch im Ofen brennt.",
              "",
              "&eMultiblöcke:&r Viele Oritech-Maschinen brauchen &6Maschinenkerne&r um sich herum. Halte &eStrg&r über dem Gegenstand, dann nennt der Tooltip die Zahl der nötigen Kerne und die Addon-Plätze. Fehlt ein Kern, meldet die Maschine, dass sie nicht zusammengebaut ist.",
              "",
              "Der einfachste Kern ist der &6Primitive Maschinenkern&r: acht Bretter um eine Werkbank. Bessere Kerne (Kupfer um Lapis, Kohlefaser um Redstone und so weiter) erlauben mehr Addon-Erweiterungen.",
          ],
          tasks=[task_item("oritech:basic_generator_block", 1), task_item("oritech:machine_core_1", 4)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["coils", "electrum"], icon="oritech:basic_generator_block", size=1.75, shape="gear"),

    quest("pipes", 7.8, 2.4, "&9Rohre",
          subtitle="Strom, Gegenstände, Flüssigkeiten.",
          description=[
              "&eEnergierohr:&r drei Electrum in einer Reihe ergeben sechs.",
              "&eItem Pipe:&r Bretter oben und unten, Nickel in der Mitte, ebenfalls sechs.",
              "&eFlüssigkeitsrohr:&r Kupfer oben und unten, Silizium in der Mitte.",
              "",
              "Ein Rechtsklick auf die Verbindung eines Gegenstandsrohrs schaltet das Herausziehen ein. Es zieht dann aus dem ersten belegten Slot und liefert in das nächste freie Inventar. Klickst du die Verbindung mit einem &6Motor&r an, zieht sie aus allen Slots.",
              "",
              "Den &6Pipe Wrench&r (Stahl und Nickel) brauchst du, um Rohrseiten einzustellen.",
          ],
          tasks=[task_item("oritech:energy_pipe", 12), task_item("oritech:item_pipe", 12)],
          rewards=[reward_item("oritech:electrum_ingot", 4)],
          deps=["generator"], icon="oritech:energy_pipe"),

    # ---- Verarbeitung --------------------------------------------------------
    quest("pulverizer", 7.8, 0, "&7Pulverizer",
          subtitle="Mahlt Erze, Kohle und Quarz.",
          description=[
              "&eRezept:&r Eisen in die obere Reihe und an die Seiten, Nickel in die Mitte, unten Motor, Kupferblock, Motor. Er braucht 32 RF/t.",
              "",
              "&eWas er macht:&r Ein Erzblock wird zu zwei Rohen Erzen. Ein Rohes Eisen wird zu einem Eisenstaub und drei kleinen Staubhäufchen, neun kleine ergeben einen ganzen. Aus Kohle wird &6Kohlestaub&r, aus Quarz &6Quarzstaub&r, aus einer Enderperle acht &6Enderic Compound&r.",
              "",
              "Kohlestaub brauchst du für Stahl in der Gießerei und für Kohlefaser in der Zentrifuge, Quarzstaub für Silizium.",
          ],
          tasks=[task_item("oritech:pulverizer_block", 1), task_item("oritech:coal_dust", 16)],
          rewards=[reward_item("minecraft:raw_iron", 16)],
          deps=["coils"], icon="oritech:pulverizer_block"),

    quest("furnace", 10.4, -1.2, "&6Angetriebener Ofen",
          subtitle="Ein Ofen mit Silizium.",
          description=[
              "&eSilizium:&r zwei Quarzstaub und zwei Sand ergeben drei &6Rohes Silizium&r, im Ofen geschmolzen wird daraus &6Silizium&r.",
              "",
              "&eRezept:&r Kupfer in die obere Reihe, Silizium links und rechts, Electrum in die Mitte, unten Spule, Ofen, Spule.",
              "",
              "Der &6angetriebene Ofen&r schmilzt alles, was ein Ofen schmilzt, mit Strom statt Kohle.",
          ],
          tasks=[task_item("oritech:powered_furnace_block", 1), task_item("oritech:silicon", 8)],
          rewards=[reward_item("minecraft:sand", 32), reward_item("minecraft:quartz", 16)],
          deps=["pulverizer"], icon="oritech:powered_furnace_block"),

    quest("foundry", 10.4, 0.8, "&c&lGießerei",
          subtitle="Zwei Zutaten, ein Barren.",
          description=[
              "&eRezept:&r Kupfer in die obere Reihe und an die Seiten, ein Motor in die Mitte, unten Electrum, Kessel, Electrum.",
              "",
              "Die &6Gießerei&r legiert zwei Zutaten. Ein Eisen und ein Kohlestaub geben einen &6Stahlbarren&r, ein Gold und ein Redstone einen Electrum, ein Diamant und ein Nickel einen &6Adamant Barren&r. &eRezept auf Kronwerke:&r Netherit macht sie hier nicht, das bleibt beim Schmiedetisch.",
              "",
              "&eRezept auf Kronwerke:&r Messing gibt es in der Gießerei nicht. Messing kommt auf Kronwerke nur aus dem Mixer von Create.",
              "",
              "&eKronwerke:&r Eine Gießerei mit Pulverizer davor ist eine kleine Stahlstraße: Kohle wird zu Staub, Staub und Eisen werden zu Stahl. Häng eine Kiste am Obelisken dahinter, und jeder Barren zählt für dich.",
          ],
          tasks=[task_item("oritech:foundry_block", 1), task_item("oritech:adamant_ingot", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["pulverizer"], icon="oritech:foundry_block", size=1.75, shape="hexagon"),

    quest("centrifuge", 13, -1.2, "&dZentrifuge und Plastik",
          subtitle="Kohlefaser, Biopolymer, Plastik.",
          description=[
              "Für die erste &6Zentrifuge&r gibt es ein zweites Rezept ohne Verarbeitungseinheiten: drei Glasflaschen oben, Kupfer links und rechts, ein Motor in der Mitte, unten Eisenblock, Motor, Eisenblock.",
              "",
              "&eKohlefaser:&r Kohlestaub in der Zentrifuge ergibt &6Carbon Fibre Strands&r.",
              "&eFlüssigkeiten:&r Mit einem &6Fluid Addon&r an ihrem Addon-Platz verarbeitet die Zentrifuge auch Flüssigkeiten. Das Addon sind fünf Kohlefasern, ein Flüssigkeitsrohr, zwei Electrum und ein Silizium.",
              "&ePlastik:&r Vier Weizen ergeben einen Packed Wheat. Mit 250 mB Wasser wird er in der Zentrifuge zu &6Raw Biopolymer&r, und das mit 500 mB Wasser zu einer &6Plastik Platte&r.",
              "",
              "Plastik brauchen die Verarbeitungseinheit, Batterien, Addons und vieles mehr. Ein Weizenfeld und eine Wasserquelle sind ab hier Pflicht.",
          ],
          tasks=[task_item("oritech:centrifuge_block", 1), task_item("oritech:machine_fluid_addon", 1), task_item("oritech:plastic_sheet", 8)],
          rewards=[reward_item("minecraft:wheat", 64), reward_xp(10)],
          deps=["furnace"], icon="oritech:plastic_sheet"),

    quest("assembler", 13, 0.8, "&9Zusammenfüger",
          subtitle="Bauteile aus vier Zutaten.",
          description=[
              "&eRezept:&r Kupfer in die obere Reihe, zwei &6Werker&r aus Vanilla links und rechts, ein Adamant Barren in die Mitte, unten Motor, Hochofen, Motor.",
              "",
              "Der &6Zusammenfüger&r baut Bauteile aus vier Zutaten. Die wichtigste ist die &6Verarbeitungseinheit&r: Plastik, Kohlefaser, Electrum und Redstone.",
              "",
              "Außerdem macht er Spulen und Motoren billiger als die Werkbank: sechs Spulen aus Stahl, zwei Nickel und Kupfer, zwei Motoren aus Nickel, Stahl und zwei Spulen.",
          ],
          tasks=[task_item("oritech:assembler_block", 1), task_item("oritech:processing_unit", 4)],
          rewards=[reward_item("oritech:plastic_sheet", 8), reward_xp(10)],
          deps=["foundry", "centrifuge"], icon="oritech:assembler_block"),

    # ---- Laser und Rahmen ----------------------------------------------------
    quest("laser", 15.6, 0.8, "&5&lEnderischer Laser",
          subtitle="Ein Strahl, der abbaut und Strom bringt.",
          description=[
              "&eEnderische Linse:&r im Zusammenfüger aus einem Adamant Barren, einer Kohlefaser und zwei Enderic Compound. &eLaser:&r Kohlefaser oben links und rechts, die Linse oben in der Mitte, Motoren an den Seiten, Electrum in der Mitte, drei Kupferverstärkte Platten unten. Er kann auch an Wänden und Decken hängen.",
              "",
              "&eZielen:&r Baue den &6Target Designator&r (drei Verarbeitungseinheiten, Plastik, Electrum, zwei Stahl). Rechtsklick auf den Zielblock speichert die Position, Rechtsklick auf den Laser überträgt sie. Die Reichweite ist 128 Blöcke.",
              "",
              "&eWas er tut:&r Er baut Blöcke am Ziel ab und versorgt Maschinen mit Strom, die nur per Laser laufen, etwa die &6Atomic Forge&r. Aus gewachsenen Amethystclustern macht er &dFluxite&r.",
              "",
              "&eRezept auf Kronwerke:&r Zertifizierten Quarz lädt der Laser hier nicht. Den laden Ars Nouveau und der Energizing Orb von Powah. Auch die Steuerschaltkreise von Mekanism kommen nicht aus der Atomic Forge.",
          ],
          tasks=[task_item("oritech:laser_arm_block", 1), task_item("oritech:target_designator", 1)],
          rewards=[reward_item("minecraft:amethyst_block", 8), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["assembler"], icon="oritech:laser_arm_block", size=2.0, shape="gear"),

    quest("destroyer", 18.6, 0.8, "&7Rahmenmaschinen",
          subtitle="Ein Arm, der über die Fläche fährt.",
          description=[
              "Zerstörer Block, Platzierer Block und Dünger Block sind &eRahmenmaschinen&r. Hinter ihnen brauchen sie ein &eleeres Rechteck&r aus &6Maschinen-Rahmen&r. Darin fährt ihr Arm hin und her und arbeitet die Fläche Block für Block ab. Fehlt der Rahmen, sagt dir die Maschine das.",
              "",
              "&eMaschinen-Rahmen:&r zwei Nickel und drei Eisengitter ergeben sechzehn Stück. Der Tooltip zeigt, wie groß ein Rahmen höchstens sein darf.",
              "",
              "Der &6Zerstörer Block&r baut die Blöcke in seinem Rahmen ab. Mit einem &6Quarry Addon&r wird sein Arbeitsbereich größer, mit einem Crop Filter Addon erntet er nur reife Pflanzen. &eRezept:&r Motoren in die Ecken oben und an die Seiten, ein Enderischer Laser oben in der Mitte, ein Pulverizer in der Mitte, drei Platten unten.",
          ],
          tasks=[task_item("oritech:machine_frame_block", 16), task_item("oritech:destroyer_block", 1)],
          rewards=[reward_item("oritech:motor", 2), reward_xp(5)],
          deps=["laser"], icon="oritech:destroyer_block", optional=True),

    # ---- Ausbau --------------------------------------------------------------
    quest("addons", 10.4, 3.6, "&aAddons",
          subtitle="Schneller, sparsamer, mehr.",
          description=[
              "Viele Oritech-Maschinen haben &eAddon-Plätze&r an ihren Seiten. Ein Addon ist ein Block, den du an einen dieser Plätze stellst. Halte &eStrg&r über der Maschine im Inventar, dann nennt der Tooltip ihre Addon-Plätze.",
              "",
              "&eSpeed Addon:&r fünf Plastik, ein Stahl, unten Spule, Platte, Spule. Mehr Tempo, mehr Verbrauch.",
              "&eEfficiency Addon:&r fünf Plastik, ein Electrum, unten Kohlefaser, Platte, Kohlefaser. Weniger Verbrauch.",
              "",
              "Wer mehr Addons will, als eine Maschine Plätze hat, setzt einen &6Machine Addon Extender&r dazwischen. Wie viele Extender gehen, hängt von der Qualität der Maschinenkerne ab.",
          ],
          tasks=[task_item("oritech:machine_speed_addon", 1), task_item("oritech:machine_efficiency_addon", 1)],
          rewards=[reward_item("oritech:plastic_sheet", 8)],
          deps=["assembler"], icon="oritech:machine_speed_addon"),

    quest("augments", 13, 3.6, "&dKybernetik",
          subtitle="Der erste Umbau am eigenen Körper.",
          description=[
              "Das &6Cybernetic Augmentation Center&r baut dir Verbesserungen ein und wieder aus. &eRezept:&r oben Dubious Container, Kohlefaser, Dubious Container, in der Mitte Motor, Truhe, Motor, unten drei Platten. Den &6Dubious Container&r baut die Werkbank aus Plastik, vier Enderic Compound und zwei Adamant Barren.",
              "",
              "Erforscht wird an einer &6Cybernetic Research Station&r (fünf Electrum, ein Redstoneblock, unten Platte, Braustand, Platte). Sie steht auf einem der Stationsplätze am Center, ähnlich wie ein Addon.",
              "",
              "&eDie ersten Augments:&r &6Steel-Infused Frame&r gibt dir drei Herzen mehr. Ihre Forschung kostet 64 Platten, 32 Kohlestaub, 8 Biostahl und 10 Millionen RF, der Einbau noch einmal 8 Platten. &6Synthetic Muscles&r (25 Prozent schneller laufen) kosten 16 Motoren, 32 Biostahl, 64 Redstone und 30 Millionen RF.",
              "",
              "&6Biostahl&r gießt die Gießerei aus Raw Biopolymer und Eisen. Das Center fasst sehr viel Strom, ein guter Generatorpark macht sich hier bezahlt. Die fortgeschrittene und die arkane Station brauchen Duratium und Overcharged Crystals, das ist ein Ziel für später.",
          ],
          tasks=[task_item("oritech:augment_application_block", 1), task_item("oritech:simple_augment_station", 1)],
          rewards=[reward_item("oritech:biosteel_ingot", 8), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["assembler"], icon="oritech:simple_augment_station", optional=True),

    quest("fragment", 16.2, 4, "&6&lErzverarbeitung",
          subtitle="Aus einem Rohen Erz fast drei Barren.",
          description=[
              "Die &6Fragment Forge&r ist die beste Mühle von Oritech. &eRezept:&r fünf Plastik, ein &6Flux Gate&r in der Mitte, unten Motor, Platte, Motor. Das Flux Gate baut der Zusammenfüger aus einer Verarbeitungseinheit, zwei Fluxite und einem &6Platinbarren&r. Platinerz liegt tief, zwischen Y -20 und Y -60.",
              "",
              "&eDie Straße:&r Ein Erzblock wird in der Fragment Forge zu zwei Rohen Erzen und einem Rohen Nickel. Ein Rohes Eisen wird zu einem Iron Clump, drei kleinen Clumps und kleinen Nickelstücken. Die Zentrifuge mit Fluid Addon macht aus jedem Clump mit Wasser &6zwei Iron Gems&r, und jeder Gem schmilzt zu einem Eisenbarren.",
              "",
              "Unterm Strich: aus einem Rohen Eisen etwa 2,7 Barren, dazu Nickel nebenbei. Im erhitzten Mixer von Create werden aus zwei Gems sogar drei Eisenbarren.",
              "",
              "&eKronwerke:&r Mehr Eisen heißt mehr Stahl für &6Der Ofen schläft nie&r. Häng eine Gießerei an das Ende, und aus der Erzstraße wird eine Stahlstraße.",
          ],
          tasks=[task_item("oritech:fragment_forge_block", 1), task_item("oritech:iron_gem", 64)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:raw_iron", 64), reward_xp(20)],
          deps=["laser"], icon="oritech:fragment_forge_block", size=2.5, shape="gear"),
]

images = [
    banner("oritech/title", "Oritech", 9, -4.6, height=1.75, kind="title", colour="fire"),
    banner("oritech/nickel", "Nickel und Stahl", 2.4, -1.5, height=0.9, colour="stone"),
    banner("oritech/power", "Energie", 6.5, 3.9, height=0.9, colour="brass"),
    banner("oritech/processing", "Verarbeitung", 10.4, -2.8, height=0.9, colour="brass"),
    banner("oritech/laser", "Laser", 17.1, -0.9, height=0.9, colour="end"),
    banner("oritech/upgrades", "Ausbau", 11.7, 5.3, height=0.9, colour="magic"),
]

chapter(C, "Oritech", "oritech:laser_arm_block", "tech", quests, shape="square", order=23, stage=3,
        subtitle=["Stufe 3: Nickel, Stahl, die Verarbeitungsmaschinen, der Laser und die ersten Augments."],
        images=images)
