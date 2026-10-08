"""Applied Energistics 2 in stage 4, one step per quest: 64k and 256k cells (sky ingot and
draconium) for items, fluids and FE, matter balls and singularities, the quantum ring, link and
bridge plus the quantum bridge card, MEGA Cells up to 4M with its providers, energy cell and
crafting CPU, spatial pylons, port, cells and the anchor, the Advanced AE reaction chamber,
shattered singularities, quantum alloy and processors, the advanced IO bus and provider, and
the stage 4 machines of Extended AE. Continues ae2.py. Recipes follow
kubejs/server_scripts/kronwerke/ae2.js. MEGA 16M and up, bulk cells, the quantum computer and
the quantum armor are stage 5 and text only."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp, banner)

C = "ae2_advanced"


def head(name, text, left, y, height=0.9, kind="section", colour="water"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Große Zellen ------------------------------------------------------------
    quest("welcome", 0, 1, "&b&lBau eine 64k-Komponente",
          subtitle="Der erste Schritt über 16k hinaus.",
          description=[
              "&eRezept auf Kronwerke:&r Glowstone-Staub in die Ecken, ein Kalkulationsprozessor oben, drei 16k-Komponenten links, rechts und unten, ein &6Himmelsbarren&r von Nature's Aura in die Mitte statt des Quarzglases.",
              "",
              "Dieses Kapitel setzt &eApplied Energistics 2&r fort. Mit &6Stufe 4, dem Sternwerk&r, öffnen 64k und 256k, die Quantenbrücke, Raumspeicher, &6MEGA Cells&r bis 4M, &6Advanced AE&r ohne Quantencomputer und die Ex-Maschinen von &6Extended AE&r.",
              "",
              "&cStufe 5:&r MEGA 16M bis 256M, die Bulk-Zelle, die Kompressionskarte, der Quantencomputer und die Quantenrüstung.",
          ],
          tasks=[task_item("ae2:cell_component_64k", 1)],
          rewards=[reward_item("ae2:calculation_processor", 4), reward_table("s4_common"), reward_xp(10)],
          icon="ae2:item_storage_cell_64k", size=2.0, shape="hexagon"),

    quest("cell_64k", 2.5, 0, "&bBau eine 64k-Zelle",
          subtitle="520 192 Stück einer Sorte.",
          description=[
              "Komponente und &6ME-Speichergehäuse&r an der Werkbank. Eine Einheit und die Komponente ergeben einen &664k-Fertigungsspeicher&r für deine CPU.",
              "",
              "Eine 64k-Zelle fasst &e520 192&r Stück einer Sorte, &e266 240&r bei 63 Typen. Volle 16k-Zellen rüstest du an der Werkbank auf, der Inhalt bleibt.",
          ],
          tasks=[task_item("ae2:item_storage_cell_64k", 1), task_item("ae2:64k_crafting_storage", 1)],
          rewards=[reward_item("ae2:crafting_unit", 2), reward_xp(8)],
          deps=["welcome"], icon="ae2:item_storage_cell_64k"),

    quest("cell_256k", 5, 0, "&b&lBau eine 256k-Zelle",
          subtitle="Draconium im Lager.",
          description=[
              "&eRezept auf Kronwerke:&r Himmelssteinstaub in die Ecken, Kalkulationsprozessor oben, drei 64k-Komponenten links, rechts und unten, ein &6Draconiumbarren&r in die Mitte. Draconium gibt es nur im End.",
              "",
              "Eine 256k-Zelle fasst &e2 080 768&r Stück einer Sorte. Mit einer Einheit wird die Komponente zum 256k-Fertigungsspeicher.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 4 &e1 000 Draconiumbarren&r. Jeder Barren in einer Zelle fehlt dort. Bau so groß, wie du wirklich brauchst.",
          ],
          tasks=[task_item("ae2:item_storage_cell_256k", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 2), reward_table("s4_uncommon"), reward_xp(12)],
          deps=["cell_64k"], icon="ae2:item_storage_cell_256k"),

    quest("fluid_big", 2.5, 2, "&9Lager Flüssigkeit in 64k",
          subtitle="Dieselbe Komponente, ein anderes Gehäuse.",
          description=[
              "Eine 64k-Komponente im &6ME-Flüssigkeitsspeicherzellengehäuse&r gibt die &664k-Flüssigkeitszelle&r. Mit dem Chemiegehäuse von Applied Mekanistics wird es eine Chemiezelle.",
              "",
              "Flüssigkeiten zählen &e8 Eimer pro Byte&r. Eine 64k-Flüssigkeitszelle fasst also über eine halbe Million Eimer einer Sorte.",
          ],
          tasks=[task_item("ae2:fluid_storage_cell_64k", 1)],
          rewards=[reward_item("minecraft:bucket", 4), reward_xp(6)],
          deps=["welcome"], icon="ae2:fluid_storage_cell_64k", section="cells"),

    quest("fe_big", 5, 2, "&cLager Strom in 64k",
          subtitle="Applied Flux bis 4M.",
          description=[
              "&664k-Energiekomponente:&r Fluixstaub in die Ecken, ein &6Energieprozessor&r oben, drei 16k-Energiekomponenten, polarisiertes Quarzglas in die Mitte. Gehäuse: Quarzglas, Redstone, Isolierharz.",
              "",
              "FE-Zellen gibt es jetzt bis &64M&r. Bei 1 048 576 FE pro Byte hält eine 64k-Zelle gut 68 Milliarden FE.",
          ],
          tasks=[task_item("appflux:fe_64k_cell", 1)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(6)],
          deps=["welcome"], icon="appflux:fe_64k_cell", section="cells"),

    # ---- Singularitäten und Quantenbrücke -------------------------------------
    quest("matter", 0, 6, "&7Mach Materiebälle",
          subtitle="Der Mülleimer, der etwas zurückgibt.",
          description=[
              "Der &6Materiekondensator&r (Eisen, Glas, Fluixstaub) vernichtet alles, was hineingeht. Im Modus &eMaterieball&r werden je &e256 Gegenstände&r zu einem &6Materieball&r. Leg eine Speicherkomponente in seinen Komponentenplatz, sonst hat er keinen Puffer.",
              "",
              "Was hineingeht, ist egal. Bruchstein, Erde, Netherrack zählen gleich. Ein Steinbruch und ein Exportbus füttern ihn ohne Pause.",
          ],
          tasks=[task_item("ae2:condenser", 1), task_item("ae2:matter_ball", 64)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(5)],
          deps=["welcome"], icon="ae2:matter_ball"),

    quest("singularity", 2.5, 6, "&5&lPress eine Singularität",
          subtitle="256 000 Gegenstände in einer Kugel.",
          description=[
              "Kondensator auf Modus &eSingularität&r, eine &664k-Komponente&r oder größer in den Komponentenplatz, dann &e256 000 Gegenstände&r hinein. Mit 16k reicht der Puffer nicht, darum gibt es Singularitäten erst jetzt.",
              "",
              "&eSchneller:&r Die &6Reaktionskammer&r von Advanced AE macht aus &e64 Materiebällen&r, 100 mB Lava und einer Million AE eine Singularität. Das sind nur gut 16 000 Gegenstände.",
              "",
              "Singularitäten brauchst du für die Quantenbrücke, die Akkumulationspresse, die Quantenlegierung und das Einrichtungsset der drahtlosen Verbinder.",
          ],
          tasks=[task_item("ae2:singularity", 2)],
          rewards=[reward_item("ae2:matter_ball", 32), reward_table("s4_common"), reward_xp(10)],
          deps=["matter"], icon="ae2:singularity", size=1.5, shape="hexagon"),

    quest("entangled", 5, 6, "&dSpreng sie zu einem Paar",
          subtitle="Ein Knall, zwei Hälften.",
          description=[
              "Wirf eine &6Singularität&r und eine &6Enderperle&r (oder Enderstaub) zusammen auf den Boden und sprenge sie. Ein Creeper reicht schon.",
              "",
              "Heraus kommen immer &ezwei Quantenverschränkte Singularitäten&r, die zusammengehören. Nur dieses Paar verbindet zwei Brücken. Benenne jedes Paar sofort am Amboss, zum Beispiel &7\"Basis Nether\"&r.",
          ],
          tasks=[task_item("ae2:quantum_entangled_singularity", 2)],
          rewards=[reward_item("minecraft:tnt", 4), reward_xp(6)],
          deps=["singularity"], icon="ae2:quantum_entangled_singularity"),

    quest("quantum_ring", 7.5, 5, "&bBau Quantentunnelringe",
          subtitle="Acht pro Brückenseite.",
          description=[
              "&6ME-Quantentunnelring:&r Eisen, Logikprozessoren, ein Konstruktionsprozessor, eine Energiezelle und ein schlaues dichtes Kabel. &6ME-Quantentunnelkammer:&r Quarzglas mit vier Fluixperlen.",
              "",
              "Eine Brückenseite ist ein flaches 3 x 3: die Kammer in der Mitte, acht Ringe drumherum. Du brauchst also &e16 Ringe&r und &ezwei Kammern&r.",
          ],
          tasks=[task_item("ae2:quantum_ring", 16), task_item("ae2:quantum_link", 2)],
          rewards=[reward_item("ae2:fluix_pearl", 4), reward_xp(8)],
          deps=["singularity"], icon="ae2:quantum_ring"),

    quest("bridge", 10, 6, "&b&lVerbinde zwei Orte mit einer Quantenbrücke",
          subtitle="Ein dichtes Kabel durch alle Dimensionen.",
          description=[
              "Bau beide 3 x 3 auf und leg in jede Kammer eine Hälfte des verschränkten Paares. Die Brücke trägt dann &e32 Kanäle&r über jede Entfernung, auch aus dem Nether oder dem End.",
              "",
              "Nur die vier Ringe an den Seiten nehmen Kabel an, die Ecken nicht. &cBeide Seiten müssen geladen sein.&r Am fernen Ende hilft ein &6Raumanker&r, siehe Raumspeicher.",
          ],
          tasks=[task_item("ae2:quantum_ring", 16), task_item("ae2:quantum_link", 2), task_item("ae2:quantum_entangled_singularity", 2)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["entangled", "quantum_ring"], icon="ae2:quantum_link", size=1.75, shape="gear"),

    quest("quantum_card", 12.5, 6, "&dBau eine Quantenbrückenkarte",
          subtitle="Die drahtlose Konsole ohne Reichweitengrenze.",
          description=[
              "Vier &6Quantentunnelringe&r in die Ecken, eine &6Fortgeschrittene Karte&r in die Mitte, eine &6Quantentunnelkammer&r unten in die Mitte.",
              "",
              "Die Karte von AE2 Wireless Terminals lässt drahtlose Konsolen sich über eine Quantenbrücke verbinden, ohne Grenze der Reichweite.",
          ],
          tasks=[task_item("ae2wtlib:quantum_bridge_card", 1)],
          rewards=[reward_item("ae2:wireless_booster", 2), reward_xp(8)],
          deps=["bridge"], icon="ae2wtlib:quantum_bridge_card", optional=True),

    # ---- MEGA Cells --------------------------------------------------------------
    quest("sky_steel", 0, 11, "&8Mach Himmelsstahl in Lava",
          subtitle="Eisen, Certus und Himmelsstein.",
          description=[
              "Wirf einen &6Geladenen Certusquarzkristall&r, einen &6Eisenbarren&r und einen &6Himmelsstein&r zusammen in &cLava&r. Heraus kommen zwei &6Himmelsstahlbarren&r.",
              "",
              "Mit Kupfer statt Eisen wird es &6Himmelsbronze&r für MEGA-Flüssigkeitszellen, mit Osmium &6Himmelsosmium&r für Chemiezellen. Der Engpass bleibt der geladene Certus aus Imbuement-Kammer oder Energizing Orb.",
          ],
          tasks=[task_item("megacells:sky_steel_ingot", 16)],
          rewards=[reward_item("ae2:sky_stone_block", 16), reward_xp(6)],
          deps=["cell_256k"], icon="megacells:sky_steel_ingot"),

    quest("accumulation", 2.5, 11, "&eBau Akkumulationsprozessoren",
          subtitle="Eine Presse aus einer Singularität.",
          description=[
              "&ePresse:&r Kalkulationsdruck oben, Konstruktionsdruck unten, eine &6Singularität&r in die Mitte der Gravurmaschine. Kopieren geht danach mit einem Eisenblock.",
              "&eProzessor:&r Himmelsstahl unter der Presse, dann &6Fluixstaub&r in die Mitte und Gedrucktes Silizium unten.",
              "",
              "Jedes MEGA-Gerät braucht diesen Prozessor.",
          ],
          tasks=[task_item("megacells:accumulation_processor_press", 1), task_item("megacells:accumulation_processor", 8)],
          rewards=[reward_item("ae2:fluix_dust", 16), reward_xp(10)],
          deps=["sky_steel", "singularity"], icon="megacells:accumulation_processor"),

    quest("mega_1m", 5, 10, "&6&lBau die erste 1M-Zelle",
          subtitle="Tausend k in einer Zelle.",
          description=[
              "&eRezept auf Kronwerke:&r Himmelssteinstaub in die Ecken, ein Akkumulationsprozessor oben, drei 256k-Komponenten, ein &6Draconiumbarren&r in die Mitte. Gehäuse: polarisiertes Quarzglas oben, Himmelssteinstaub an den Seiten, drei Himmelsstahlbarren unten.",
              "",
              "Die 63 Typen bleiben. Große Zellen lohnen sich für wenige Sorten in riesigen Mengen: Bruchstein, Erze, alles aus dem Steinbruch.",
          ],
          tasks=[task_item("megacells:mega_item_cell_housing", 1), task_item("megacells:item_storage_cell_1m", 1)],
          rewards=[reward_item("megacells:sky_steel_ingot", 8), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["accumulation"], icon="megacells:item_storage_cell_1m"),

    quest("mega_provider", 5, 12, "&eRüste Provider auf MEGA auf",
          subtitle="Doppelt so viele Plätze.",
          description=[
              "Formlos: &6Schablonen-Provider&r und &6Akkumulationsprozessor&r gibt den &6MEGA-Provider&r, &6ME-Schnittstelle&r und Prozessor die &6MEGA-Schnittstelle&r.",
              "",
              "Beide haben doppelt so viele Plätze wie das Original. Der MEGA-Provider nimmt nur Verarbeitungsschablonen.",
          ],
          tasks=[task_item("megacells:mega_pattern_provider", 1)],
          rewards=[reward_item("ae2:blank_pattern", 16), reward_xp(8)],
          deps=["accumulation"], icon="megacells:mega_pattern_provider"),

    quest("mega_energy", 7.5, 12, "&eBau eine Superdichte Energiezelle",
          subtitle="12,8 Millionen AE Puffer.",
          description=[
              "Acht &6Dichte Energiezellen&r um einen &6Akkumulationsprozessor&r.",
              "",
              "Sie hält so viel wie acht dichte Zellen in einem Block. Raumspeicher und Reaktionskammer ziehen ihren Strom auf einen Schlag, dafür ist sie da.",
          ],
          tasks=[task_item("megacells:mega_energy_cell", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_xp(8)],
          deps=["mega_provider"], icon="megacells:mega_energy_cell"),

    quest("mega_crafting", 7.5, 10, "&8Bau eine MEGA-Fertigungs-CPU",
          subtitle="Größerer Speicher, mehr Threads.",
          description=[
              "&6MEGA-Fertigungseinheit:&r vier Einheiten, zwei Logikprozessoren, zwei schlaue Kabel, ein Akkumulationsprozessor. Mit einer 1M- oder 4M-Komponente wird sie zum großen Speicher, mit einem Konstruktionsprozessor zum &6MEGA-Co-Prozessor&r.",
              "",
              "Damit plant eine CPU viele Elite-Schaltkreise auf einmal, ohne dass die Zwischenprodukte den Speicher sprengen.",
          ],
          tasks=[task_item("megacells:mega_crafting_unit", 1), task_item("megacells:mega_crafting_accelerator", 1)],
          rewards=[reward_item("ae2:crafting_unit", 4), reward_xp(10)],
          deps=["mega_1m"], icon="megacells:mega_crafting_accelerator", optional=True),

    quest("mega_4m", 10, 11, "&6&lFüll das Lager des Sternwerks",
          subtitle="4M, das Größte vor dem Chaoswerk.",
          description=[
              "&eRezept auf Kronwerke:&r Enderstaub in die Ecken, ein Akkumulationsprozessor oben, drei 1M-Komponenten, ein &6Draconiumbarren&r in die Mitte. Dazu 16 Elite-Steuerschaltkreise aus deiner CPU.",
              "",
              "In einer 4M-Zelle stecken Dutzende Prozessoren, mehrere Singularitäten und vier Draconiumbarren. &cStufe 5:&r 16M bis 256M und die Bulk-Zelle brauchen Erwachtes Draconium.",
              "",
              "&eKronwerke:&r &e\"Licht des Drachen\"&r will &e150 Elite-Steuerschaltkreise&r und &e1 000 Draconiumbarren&r. Schreib Schablonen für die Elite-Schaltkreise und lass die CPU arbeiten.",
          ],
          tasks=[task_item("megacells:item_storage_cell_4m", 1), task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_table("s4_rare"), reward_item("draconicevolution:draconium_ingot", 8), reward_xp(30)],
          deps=["mega_1m", "mega_energy"], icon="megacells:item_storage_cell_4m", size=2.5, shape="gear"),

    # ---- Raumspeicher -----------------------------------------------------------
    quest("spatial", 0, 15.5, "&3Stell Raumpylone auf",
          subtitle="Die Hülle um ein Stück Welt.",
          description=[
              "&6Raumpylon:&r Quarzglas, Glaskabel, Fluixstaub, Fluixkristall. Bau damit eine Hülle um den Bereich, den du ausschneiden willst. Der Raum ist die Hülle minus einen Block nach innen.",
              "",
              "Jede Pylonenreihe muss mindestens zwei Blöcke lang sein und braucht einen Kanal. Je mehr der Hülle du füllst, desto effizienter. Ein eigenes Unternetz ist am einfachsten.",
          ],
          tasks=[task_item("ae2:spatial_pylon", 16)],
          rewards=[reward_item("ae2:fluix_crystal", 16), reward_xp(5)],
          deps=["welcome"], icon="ae2:spatial_pylon"),

    quest("spatial_port", 2.5, 15.5, "&3Bau einen IO-Raumport",
          subtitle="Der Knopf, der die Welt tauscht.",
          description=[
              "Glas, Glaskabel, ein &6ME-IO-Port&r, Eisen und ein Konstruktionsprozessor. Er hängt im selben Netz wie die Pylone, pro Netz geht nur ein Aufbau.",
              "",
              "Zelle hinein, Redstone-Impuls, und der Inhalt der Pylone tauscht mit dem Raum in der Zelle. Der Port zieht den Strom auf einen Schlag.",
          ],
          tasks=[task_item("ae2:spatial_io_port", 1)],
          rewards=[reward_item("ae2:engineering_processor", 2), reward_xp(6)],
          deps=["spatial"], icon="ae2:spatial_io_port"),

    quest("spatial_cell", 5, 15.5, "&3Bau eine Raumspeicherzelle",
          subtitle="Einmal benutzt, für immer festgelegt.",
          description=[
              "&62³-Komponente:&r Glowstone, vier Fluixperlen, ein Konstruktionsprozessor. Vier 2³ ergeben eine &616³&r, vier 16³ eine &6128³&r. Mit einem Gehäuse wird daraus eine Zelle.",
              "",
              "&cAchtung:&r Eine benutzte Zelle behält ihre Maße für immer. Alles im Bereich wird mitgenommen, auch du. Steh nie zwischen den Pylonen, wenn jemand den Knopf drückt.",
              "",
              "So holst du zum Beispiel einen &6Makellosen Certusquarzknospenblock&r aus einem Meteoriten in deine Basis.",
          ],
          tasks=[task_item("ae2:spatial_storage_cell_16", 1)],
          rewards=[reward_item("ae2:fluix_pearl", 4), reward_xp(8)],
          deps=["spatial_port"], icon="ae2:spatial_storage_cell_16"),

    quest("anchor", 7.5, 15.5, "&3&lSetz einen Raumanker",
          subtitle="Das Netz bleibt wach.",
          description=[
              "Drei Raumpylone oben, Glaskabel links und rechts, eine &6128³-Raumkomponente&r in der Mitte, Eisen und ein Konstruktionsprozessor unten.",
              "",
              "Der Anker lädt jeden Chunk, in dem ein Teil seines Netzes liegt. Ein Kabel über die Chunkgrenze reicht. Über Quantenbrücken wirkt er weiter, aber nicht über Dimensionen: das Netz im Nether braucht einen eigenen.",
              "",
              "Er braucht &d80 AE/t&r plus etwas mehr für jeden Chunk. Er gibt auch Zufallsticks, Certus wächst also weiter.",
          ],
          tasks=[task_item("ae2:spatial_anchor", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_table("s4_common"), reward_xp(10)],
          deps=["spatial_cell"], icon="ae2:spatial_anchor"),

    # ---- Advanced AE ------------------------------------------------------------
    quest("reaction", 0, 20, "&5&lBau eine Reaktionskammer",
          subtitle="Wasser und Lava, nur mit Strom.",
          description=[
              "Materiekondensator, Vibrationskammer, Fluixstaub, Glowstone und ein Eimer ergeben die &6Reaktionskammer&r von Advanced AE.",
              "",
              "Sie macht 64 Fluix, 64 Himmelsstahl, 64 Entro oder eine Singularität aus 64 Materiebällen, je mit einer Flüssigkeit und &d100 000 bis 1 Million AE&r pro Rezept.",
              "",
              "&eKronwerke:&r Geladenen Certus macht sie hier nicht. Häng sie als Block an einen Provider, dann zieht sie direkt aus dem Netz, und stell dichte Energiezellen dazu.",
          ],
          tasks=[task_item("advanced_ae:reaction_chamber", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="advanced_ae:reaction_chamber", size=1.5, shape="hexagon"),

    quest("shattered", 2.5, 19, "&dZerbrich eine Singularität",
          subtitle="Der erste Schritt zur Quantenlegierung.",
          description=[
              "In der Reaktionskammer: eine &6Singularität&r, zwei Enderstaub, zwei Himmelssteinstaub und etwas Lava ergeben zwei &6Zerbrochene Singularitäten&r.",
              "",
              "Die Gravurmaschine (oder der Brecher von Mekanism) mahlt sie zu &6Quanteninfundiertem Staub&r.",
          ],
          tasks=[task_item("advanced_ae:shattered_singularity", 4), task_item("advanced_ae:quantum_infused_dust", 2)],
          rewards=[reward_item("ae2:singularity", 1), reward_xp(8)],
          deps=["reaction", "singularity"], icon="advanced_ae:shattered_singularity"),

    quest("quantum_alloy", 5, 19, "&dGieß Quantenlegierung",
          subtitle="Mehr als sechs Singularitäten pro Barren.",
          description=[
              "Ein Quanteninfundierter Staub und 4 000 mB Wasser ergeben in der Kammer 1 000 mB &6Quanteninfusion&r. Daraus mit vier Kupferbarren, vier Zerbrochenen Singularitäten und &evier Singularitäten&r ein &6Quantenlegierungsbarren&r.",
              "",
              "Lass den Kondensator Tag und Nacht laufen.",
          ],
          tasks=[task_item("advanced_ae:quantum_alloy", 2)],
          rewards=[reward_item("ae2:singularity", 2), reward_xp(10)],
          deps=["shattered"], icon="advanced_ae:quantum_alloy"),

    quest("quantum_processor", 7.5, 19, "&dBau Quantenprozessoren",
          subtitle="Die vierte Presse.",
          description=[
              "&6Quantenpresse:&r Logikdruck oben, Konstruktionsdruck unten, eine Zerbrochene Singularität in die Mitte. Quantenlegierung unter der Presse, dann mit Redstone und Gedrucktem Silizium fertig pressen.",
              "",
              "&cStufe 5:&r Der &6Quantencomputer&r (CPU ohne Grenze für gleichzeitige Aufträge) und die &6Quantenrüstung&r brauchen viele davon. Wer jetzt hortet, baut sie dann sofort.",
          ],
          tasks=[task_item("advanced_ae:quantum_processor", 4)],
          rewards=[reward_item("ae2:printed_silicon", 16), reward_table("s4_uncommon"), reward_xp(12)],
          deps=["quantum_alloy"], icon="advanced_ae:quantum_processor"),

    quest("adv_io_bus", 10, 19, "&dBau einen Erweiterten IO-Bus",
          subtitle="Import und Export in einem Teil.",
          description=[
              "Erst der &6ME Import Export Bus&r: Importbus, Logikprozessor, Exportbus in einer Reihe. Dann Beschleunigungskarten in die Ecken, Quantenprozessoren oben, in der Mitte und unten, links der Import Export Bus, rechts ein &6ME Stock Export Bus&r.",
              "",
              "Der &6Erweiterte IO-Bus&r bewegt achtmal so viel wie ein Exportbus.",
          ],
          tasks=[task_item("advanced_ae:advanced_io_bus_part", 1)],
          rewards=[reward_item("ae2:speed_card", 4), reward_xp(10)],
          deps=["quantum_processor"], icon="advanced_ae:advanced_io_bus_part", optional=True),

    quest("adv_provider", 2.5, 21, "&5Bau einen gerichteten Provider",
          subtitle="Jede Zutat auf ihre Seite.",
          description=[
              "&6Advanced Pattern Provider:&r Schablonen-Provider, Redstone, Enderperle und Logikprozessor. Mit einem Ex-Provider wird es die große Version mit 36 Plätzen.",
              "",
              "Leg eine Verarbeitungsschablone in den &6Advanced Pattern Encoder&r (Rechtsklick in der Hand), wähl für jede Zutat eine Seite und nimm die neue Schablone heraus. Kein Rohrgewirr mehr an Mekanism-Maschinen.",
          ],
          tasks=[task_item("advanced_ae:small_adv_pattern_provider", 1), task_item("advanced_ae:adv_pattern_encoder", 1)],
          rewards=[reward_item("ae2:blank_pattern", 16), reward_xp(6)],
          deps=["reaction"], icon="advanced_ae:adv_pattern_provider"),

    # ---- Extended AE ------------------------------------------------------------
    quest("ex_machines", 0, 25, "&3&lBau ein Erweitertes Laufwerk",
          subtitle="Zwanzig Zellen statt zehn.",
          description=[
              "Im Crystal Assembler: ein &6ME-Laufwerk&r, zwei Glaskabel, eine Kapazitätskarte und ein &6Concurrent Processor&r gibt das &6ME Extended Drive&r. Der &6ME Extended Pattern Provider&r hat viel mehr Plätze als ein normaler.",
              "",
              "Die Upgrade-Gegenstände von Extended AE tauschen ein stehendes Gerät per Schleich-Rechtsklick gegen seine Ex-Version, Einstellungen und Inhalt bleiben.",
          ],
          tasks=[task_item("extendedae:ex_drive", 1), task_item("extendedae:ex_pattern_provider", 1)],
          rewards=[reward_item("extendedae:concurrent_processor", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="extendedae:ex_drive", size=1.5, shape="hexagon"),

    quest("ex_inscriber", 2.5, 24, "&3Bau eine Erweiterte Gravurmaschine",
          subtitle="Vier Gravuren auf einmal.",
          description=[
              "Im Crystal Assembler: eine Gravurmaschine, drei Kapazitätskarten und ein Concurrent Processor.",
              "",
              "Die &6Extended Inscriber&r arbeitet vier Gravuren gleichzeitig. Dazu gibt es den &6Extended Molecular Assembler&r (acht Aufträge zugleich) und den &6ME Extended IO Port&r (achtmal so schnell).",
          ],
          tasks=[task_item("extendedae:ex_inscriber", 1)],
          rewards=[reward_item("ae2:printed_silicon", 16), reward_xp(8)],
          deps=["ex_machines"], icon="extendedae:ex_inscriber"),

    quest("matrix", 5, 24, "&3Bau eine Assembler-Matrix",
          subtitle="Ein Multiblock statt hundert Assembler.",
          description=[
              "Ein Quader von 3 bis 7 Blöcken pro Kante: Kanten aus &6Assembler Matrix Frame&r, Seiten aus Wall oder Glass, innen die Kerne. Mindestens ein &6Pattern Core&r (36 Werkbankschablonen) und ein &6Craft Core&r (acht Aufträge).",
              "",
              "&6Speed Cores&r machen sie schneller, ab fünf ist volle Geschwindigkeit erreicht. Leuchten die Linien am Rahmen blau, ist sie fertig. Spart viele Kanäle.",
          ],
          tasks=[task_item("extendedae:assembler_matrix_pattern", 1), task_item("extendedae:assembler_matrix_crafter", 1)],
          rewards=[reward_item("extendedae:assembler_matrix_frame", 8), reward_xp(10)],
          deps=["ex_inscriber"], icon="extendedae:assembler_matrix_crafter"),

    quest("wireless", 2.5, 26, "&3Verbinde Netze drahtlos",
          subtitle="Kabel durch die Luft.",
          description=[
              "Der Crystal Assembler macht zwei &6ME Wireless Connector&r aus Maschinenrahmen, schlauen dichten Kabeln, Drahtlosempfängern und Verstärkern. Mit dem &6ME Wireless Setup Kit&r (braucht eine Singularität) klickst du nacheinander beide an.",
              "",
              "Nur in derselben Dimension. Je weiter, desto mehr Strom, Energiekarten senken ihn um je 10 Prozent. Der &6ME Wireless Hub&r verbindet bis zu acht Verbinder und braucht eine Quantentunnelkammer.",
          ],
          tasks=[task_item("extendedae:wireless_connect", 2), task_item("extendedae:wireless_tool", 1)],
          rewards=[reward_item("ae2:wireless_booster", 2), reward_xp(6)],
          deps=["ex_machines"], icon="extendedae:wireless_connect"),

    # ---- Neue Quests -------------------------------------------------------------
    quest("cell_dock", 7.5, 1, "&7Setz ein ME Cell Dock",
          subtitle="Eine Zelle, flach am Kabel.",
          description=[
              "Eisen, Kupfer, Eisen oben, ein Glaskabel darunter in die Mitte. Das &6ME Cell Dock&r von MEGA Cells hält genau eine Zelle.",
              "",
              "Es ist wie eine kleine ME-Truhe ohne Konsole, aber ein flaches Kabelteil: mehrere Docks passen an dasselbe Kabelstück. Praktisch als Puffer in einem kleinen Unternetz.",
          ],
          tasks=[task_item("megacells:cell_dock", 1)],
          rewards=[reward_item("ae2:fluix_glass_cable", 16), reward_xp(4)],
          deps=["cell_64k"], icon="megacells:cell_dock", optional=True),

    quest("fluid_1m", 12.5, 10, "&9Bau eine MEGA-Flüssigkeitszelle",
          subtitle="Himmelsbronze statt Himmelsstahl.",
          description=[
              "&6MEGA-Flüssigkeitszellengehäuse:&r polarisiertes Quarzglas, Himmelssteinstaub, polarisiertes Quarzglas oben, Himmelssteinstaub an den Seiten, drei &6Himmelsbronzebarren&r unten. Mit einer &61M-Komponente&r wird es die &61M MEGA Fluid Storage Cell&r.",
              "",
              "Himmelsbronze machst du wie Himmelsstahl, nur mit Kupfer statt Eisen in der Lava. Wie jede Flüssigkeitszelle hält sie &e5 Typen&r.",
          ],
          tasks=[task_item("megacells:fluid_storage_cell_1m", 1)],
          rewards=[reward_item("megacells:sky_steel_ingot", 4), reward_xp(8)],
          deps=["mega_1m"], icon="megacells:fluid_storage_cell_1m"),

    quest("radioactive", 12.5, 12, "&aLager Atommüll im Netz",
          subtitle="Die Zelle, die nur Strahlendes nimmt.",
          description=[
              "&6MEGA Radioactive Storage Component:&r Himmelssteinstaub in die Ecken, ein Akkumulationsprozessor oben, zwei &6Tonnen für radioaktiven Abfall&r links und rechts, polarisiertes Quarzglas in der Mitte, eine 256k-Komponente unten. Für die Zelle kommen &6Reaktorglas&r, Himmelssteinstaub, &6HDPE-Platten&r und ein &6Polonium-Pellet&r dazu.",
              "",
              "Normale Chemiezellen nehmen keine radioaktiven Stoffe. Diese Zelle nimmt nur sie: Atommüll, Polonium, Plutonium. Sie hält einen Typ, den du vorher an der Speicherzellenwerkbank einstellst, bis &d2 048 Eimer&r.",
              "",
              "&cAchtung:&r Sie braucht &d250 AE/t&r im Laufwerk. Verbrauchten Atommüll nimmt sie nicht.",
          ],
          tasks=[task_item("megacells:radioactive_chemical_cell", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["accumulation"], icon="megacells:radioactive_chemical_cell", optional=True),

    quest("greater_card", 10, 12.5, "&eBau eine Greater Energy Card",
          subtitle="Größerer Akku für alles Tragbare.",
          description=[
              "Formlos aus einer &6Fortgeschrittenen Karte&r und einer &6Superdichten Energiezelle&r.",
              "",
              "Sie passt in tragbare Zellen und drahtlose Konsolen wie die normale Energiekarte, nur mit viel mehr Puffer. Tragbare MEGA-Zellen nehmen nur diese Karte.",
          ],
          tasks=[task_item("megacells:greater_energy_card", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_xp(6)],
          deps=["mega_energy"], icon="megacells:greater_energy_card", optional=True),

    quest("throughput", 12.5, 19, "&dMiss deinen Durchsatz",
          subtitle="Wie schnell wächst der Bestand?",
          description=[
              "&6ME Throughput Monitor:&r formlos aus einem &6ME-Speichermonitor&r und einem Kalkulationsprozessor.",
              "",
              "Er zeigt wie der Speichermonitor einen Gegenstand, dazu aber, wie schnell sich dessen Menge ändert: pro Sekunde, pro Minute oder pro zehn Minuten. So siehst du, ob deine Erzverarbeitung mithält oder eine Farm schwächelt.",
          ],
          tasks=[task_item("advanced_ae:throughput_monitor", 1)],
          rewards=[reward_item("ae2:calculation_processor", 2), reward_xp(5)],
          deps=["reaction"], icon="advanced_ae:throughput_monitor", optional=True),

    quest("infinity_cells", 5, 26, "&3Bau unendliche Zellen",
          subtitle="Bruchstein und Wasser ohne Ende.",
          description=[
              "&6ME Infinity Cobblestone Cell:&r Quarzglas, Lavaeimer, Quarzglas oben, Wassereimer, 16k-Komponente, Wassereimer in der Mitte, drei Diamanten unten. Die &6ME Infinity Water Cell&r nimmt einen Wassereimer statt der Lava.",
              "",
              "Im Laufwerk gibt sie unbegrenzt Bruchstein oder Wasser ab und schluckt beides ohne Ende. Keine Steinfarm, keine Wasserquelle mehr für Maschinen, die das brauchen.",
          ],
          tasks=[task_item("extendedae:infinity_cobblestone_cell", 1), task_item("extendedae:infinity_water_cell", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(8)],
          deps=["ex_machines"], icon="extendedae:infinity_cobblestone_cell"),

    quest("ex_assembler", 7.5, 24, "&3Bau einen Extended Molecular Assembler",
          subtitle="Acht Aufträge, doppelt so schnell.",
          description=[
              "Im Crystal Assembler: vier &6Molekularassembler&r, vier Concurrent Processors, vier Fluixstaub, drei Konstruktionsprozessoren und eine Beschleunigungskarte.",
              "",
              "Er arbeitet acht Aufträge gleichzeitig (wenn die CPU genug Prozessoreinheiten hat) und doppelt so schnell wie ein normaler. Schablonen legst du nicht direkt hinein, er bekommt sie nur von einem Provider.",
          ],
          tasks=[task_item("extendedae:ex_molecular_assembler", 1)],
          rewards=[reward_item("ae2:crafting_accelerator", 2), reward_xp(8)],
          deps=["ex_inscriber"], icon="extendedae:ex_molecular_assembler"),

    quest("oversize", 2.5, 27, "&3Bau ein ME Oversize Interface",
          subtitle="1 024 Stück pro Platz.",
          description=[
              "Im Crystal Assembler: ein &6ME Extended Interface&r, ein &6ME Ingredient Buffer&r (Eisen, 1k-Komponenten, Quarzglas), zwei Concurrent Processors und je zwei Annihilations- und Formationskerne.",
              "",
              "Es hat so viele Plätze wie das Extended Interface, aber jeder hält das &d16-fache&r: 1 024 Gegenstände statt 64. Ideal als Vorrat neben Maschinen, die große Mengen auf einmal fressen.",
          ],
          tasks=[task_item("extendedae:oversize_interface", 1)],
          rewards=[reward_item("extendedae:concurrent_processor", 2), reward_xp(8)],
          deps=["ex_machines"], icon="extendedae:oversize_interface", optional=True),

    quest("ex_buses", 7.5, 26, "&3Bau erweiterte Busse",
          subtitle="Achtmal so schnell.",
          description=[
              "Im Crystal Assembler: ein Importbus (oder Exportbus), drei Beschleunigungskarten, zwei Kolben und ein Annihilationskern (beim Export ein Formationskern).",
              "",
              "Die &6ME Extended Import Bus&r und &6Export Bus&r bewegen &d8-mal&r so viel wie die normalen und haben mehr Kartenplätze. Genau richtig für den Steinbruch, der in dein Netz kippt.",
          ],
          tasks=[task_item("extendedae:ex_import_bus_part", 1), task_item("extendedae:ex_export_bus_part", 1)],
          rewards=[reward_item("ae2:speed_card", 4), reward_xp(8)],
          deps=["ex_machines"], icon="extendedae:ex_import_bus_part"),
]

images = [
    head("title", "Applied Energistics 2: Fortgeschritten", 0, -3.6, height=1.2, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -2.3, height=0.55, kind="note", colour="end"),
    head("cells", "Große Zellen", 2.0, -1.3, colour="water"),
    head("singularity", "Singularitäten und Quantenbrücke", 0, 3.9, colour="end"),
    head("mega", "MEGA Cells", 0, 8.7, colour="brass"),
    head("spatial", "Raumspeicher", 0, 14.0, colour="water"),
    head("advanced", "Advanced AE", 0, 17.7, colour="magic"),
    head("extended", "Extended AE", 0, 23.0, colour="water"),
]

chapter(C, "Applied Energistics 2: Fortgeschritten", "megacells:item_storage_cell_1m", "tech", quests,
        shape="square", order=36, stage=4,
        subtitle=["Stufe 4: große Zellen, Quantenbrücke, Raumspeicher, MEGA Cells und Advanced AE."],
        images=images)
