"""Applied Energistics 2 in stage 4: 64k and 256k cells (sky ingot and draconium), matter
balls and singularities, the quantum network bridge, spatial storage and the spatial anchor,
MEGA Cells up to 4M, the Advanced AE reaction chamber, quantum alloy and processors and the
advanced pattern provider, plus the stage 4 machines of Extended AE. Continues ae2.py.
Recipes follow kubejs/server_scripts/kronwerke/ae2.js. MEGA 16M and up, bulk cells, the
quantum computer and the quantum armor are stage 5 and text only."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp, banner)

C = "ae2_advanced"


def head(name, text, left, y, height=0.9, kind="section", colour="water"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Große Zellen und MEGA ------------------------------------------------
    quest("welcome", 0, 4.5, "&b&lAE2: Fortgeschritten",
          subtitle="Mehr Bytes, mehr Kanäle, mehr Raum.",
          description=[
              "Mit &6Stufe 4, dem Sternwerk&r, öffnet Applied Energistics 2 seine zweite Hälfte. Das Kapitel setzt da an, wo &eApplied Energistics 2&r aufgehört hat.",
              "",
              "&eWas jetzt offen ist:&r Zellen mit &664k&r und &6256k&r, die &6Quantenbrücke&r, &6Raumspeicher&r (Spatial IO) und der &6Raumanker&r, &6MEGA Cells&r bis &64M&r, &6Advanced AE&r ohne Quantencomputer und Rüstung, die Ex-Maschinen von &6Extended AE&r und Applied-Flux-Zellen bis 4M.",
              "",
              "&cWas noch wartet:&r MEGA 16M bis 256M, die Bulk-Zelle, die Kompressionskarte, der &6Quantencomputer&r und die &6Quantenrüstung&r von Advanced AE kommen in Stufe 5.",
              "",
              "&eErster Schritt:&r die &664k-ME-Speicherkomponente&r. &eRezept auf Kronwerke:&r Glowstone-Staub in die Ecken, ein Kalkulationsprozessor oben, drei 16k-Komponenten links, rechts und unten, und in die Mitte ein &6Himmelsbarren&r von Nature's Aura statt des Quarzglases.",
          ],
          tasks=[task_item("ae2:cell_component_64k", 1)],
          rewards=[reward_item("ae2:calculation_processor", 4), reward_table("s4_common"), reward_xp(10)],
          icon="ae2:item_storage_cell_64k", size=2.0, shape="hexagon"),

    quest("cell_256k", 2.5, 1, "&b256k-Zellen",
          subtitle="Draconium im Lager.",
          description=[
              "Aus der 64k-Komponente wird mit einem Gehäuse eine &664k-Zelle&r, und vier 64k-Komponenten führen zur &6256k-Komponente&r.",
              "",
              "&eRezept auf Kronwerke:&r Himmelssteinstaub in die Ecken, Kalkulationsprozessor oben, drei 64k-Komponenten, und in die Mitte ein &6Draconiumbarren&r. Draconium gibt es nur im End.",
              "",
              "Die 64k- und 256k-Komponenten passen auch zu einer &6Fertigungseinheit&r: Einheit und Komponente an der Werkbank ergeben einen 64k- oder 256k-Fertigungsspeicher für deine CPU.",
              "",
              "&eApplied Flux:&r FE-Zellen gibt es jetzt bis &64M&r. Eine 256k-FE-Zelle hält mehr Strom, als ein ganzes Mekanism-Netz braucht.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 4 &e1 000 Draconiumbarren&r. Jeder Barren in einer Zelle fehlt dort. Bau so groß, wie du wirklich brauchst.",
          ],
          tasks=[task_item("ae2:item_storage_cell_64k", 1), task_item("ae2:item_storage_cell_256k", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 2), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["welcome"], icon="ae2:item_storage_cell_256k"),

    quest("sky_steel", 5, 0, "&8Himmelsstahl",
          subtitle="Eisen, Certus und Himmelsstein in Lava.",
          description=[
              "&6MEGA Cells&r braucht ein eigenes Metall. Wirf einen &6Geladenen Certusquarzkristall&r, einen &6Eisenbarren&r und einen &6Himmelssteinblock&r zusammen in &cLava&r, dann liegen dort zwei &6Himmelsstahlbarren&r.",
              "",
              "Dasselbe mit Kupfer statt Eisen gibt &6Himmelsbronze&r für Flüssigkeitszellen, mit Osmium &6Himmelsosmium&r für Chemikalienzellen.",
              "",
              "Der Engpass ist wie immer der geladene Certus. Auf Kronwerke kommt er nur aus der Imbuement-Kammer oder dem Energizing Orb. Nimm Lava aus einem Tank oder einer Quelle, die nichts anderes verbrennt, und sammle die Barren mit einem Trichter ein.",
          ],
          tasks=[task_item("megacells:sky_steel_ingot", 16)],
          rewards=[reward_item("ae2:sky_stone_block", 16), reward_xp(5)],
          deps=["cell_256k"], icon="megacells:sky_steel_ingot"),

    quest("accumulation", 7.5, 0, "&eAkkumulationsprozessor",
          subtitle="Eine Presse aus einer Singularität.",
          description=[
              "Jedes MEGA-Gerät braucht den &6Akkumulationsprozessor&r.",
              "",
              "&eDie Presse:&r In die Gravurmaschine kommt oben der Kalkulationsdruck, unten der Konstruktionsdruck und in die Mitte eine &6Singularität&r. Heraus kommt die &6Akkumulationspresse&r. Wie die anderen Pressen kopierst du sie danach mit einem Eisenblock.",
              "",
              "&eDer Prozessor:&r Himmelsstahl unter der neuen Presse ergibt den gedruckten Schaltkreis. Den presst du mit &6Fluixstaub&r in der Mitte und Gedrucktem Silizium unten fertig.",
              "",
              "Mit dem Prozessor wird aus einem Schablonen-Provider oder einer Schnittstelle an der Werkbank die MEGA-Version mit doppelt so vielen Plätzen. Der MEGA-Provider nimmt allerdings nur Verarbeitungsschablonen.",
          ],
          tasks=[task_item("megacells:accumulation_processor_press", 1), task_item("megacells:accumulation_processor", 8)],
          rewards=[reward_item("ae2:fluix_dust", 16), reward_xp(10)],
          deps=["sky_steel", "singularity"], icon="megacells:accumulation_processor"),

    quest("mega_1m", 10, 0, "&6&lDie erste 1M-Zelle",
          subtitle="Tausend k in einer Zelle.",
          description=[
              "Die &61M-Komponente&r ist eine 256k-Komponente mit dem Akkumulationsprozessor weitergebaut.",
              "",
              "&eRezept auf Kronwerke:&r Himmelssteinstaub in die Ecken, ein Akkumulationsprozessor oben, drei 256k-Komponenten, ein &6Draconiumbarren&r in die Mitte statt des polarisierten Quarzglases.",
              "",
              "Die Zelle selbst braucht ein &6MEGA-Gehäuse&r: polarisiertes Quarzglas oben in den Ecken, Himmelssteinstaub an den Seiten, unten drei Himmelsstahlbarren.",
              "",
              "Die 63 Typen pro Zelle bleiben. Große Zellen lohnen sich für wenige Sorten in riesigen Mengen: Bruchstein, Erze, alles aus dem Steinbruch.",
          ],
          tasks=[task_item("megacells:mega_item_cell_housing", 1), task_item("megacells:item_storage_cell_1m", 1)],
          rewards=[reward_item("megacells:sky_steel_ingot", 8), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["accumulation", "cell_256k"], icon="megacells:item_storage_cell_1m"),

    quest("mega_crafting", 12.5, -1, "&8MEGA-Fertigungs-CPU",
          subtitle="Vier Threads pro Block.",
          description=[
              "Die &6MEGA-Fertigungseinheit&r (vier normale Einheiten, zwei Logikprozessoren, zwei schlaue Kabel und ein Akkumulationsprozessor) ist die Basis der großen CPUs.",
              "",
              "Mit einer 1M- oder 4M-Komponente wird daraus ein großer Fertigungsspeicher. Mit einem Konstruktionsprozessor wird daraus ein &6MEGA-Co-Prozessor&r, der &evier&r Threads statt einem bringt.",
              "",
              "Für die Schaltkreisstraße heißt das: eine CPU, die viele Elite-Schaltkreise auf einmal plant, ohne dass die Zwischenprodukte den Speicher sprengen.",
          ],
          tasks=[task_item("megacells:mega_crafting_unit", 1), task_item("megacells:mega_crafting_accelerator", 1)],
          rewards=[reward_item("ae2:crafting_unit", 4), reward_xp(10)],
          deps=["mega_1m"], icon="megacells:mega_crafting_accelerator", optional=True),

    quest("mega_4m", 12.75, 1.75, "&6&lDas Lager des Sternwerks",
          subtitle="4M, das Größte vor dem Chaoswerk.",
          description=[
              "Vier 1M-Komponenten werden zur &64M-Komponente&r.",
              "",
              "&eRezept auf Kronwerke:&r Enderstaub in die Ecken, ein Akkumulationsprozessor oben, drei 1M-Komponenten, und wieder ein &6Draconiumbarren&r in die Mitte.",
              "",
              "In einer einzigen 4M-Zelle stecken damit Dutzende Prozessoren, mehrere Singularitäten und vier Draconiumbarren. Sie ist der Beweis, dass deine Gravurmaschinen, deine Singularitäten und dein Weg ins End laufen.",
              "",
              "&cAusblick:&r 16M bis 256M, die Bulk-Zelle und die Kompressionskarte brauchen einen &6Erwachten Draconiumnugget&r und kommen in Stufe 5.",
              "",
              "&eKronwerke:&r Das Ziel &e\"Licht des Drachen\"&r verlangt auf der Technikseite &e150 Elite-Steuerschaltkreise&r und &e1 000 Draconiumbarren&r. Schreib Schablonen für die Elite-Schaltkreise und lass deine MEGA-CPU den Rest erledigen.",
          ],
          tasks=[task_item("megacells:item_storage_cell_4m", 1), task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_table("s4_rare"), reward_item("draconicevolution:draconium_ingot", 8), reward_xp(30)],
          deps=["mega_1m"], icon="megacells:item_storage_cell_4m", size=2.5, shape="gear"),

    # ---- Singularitäten und Quantenbrücke -------------------------------------
    quest("matter", 2.5, 4.5, "&7Materiebälle",
          subtitle="Der Mülleimer, der etwas zurückgibt.",
          description=[
              "Der &6Materiekondensator&r (Eisen, Glas, Fluixstaub) vernichtet alles, was hineingeht. Er hat drei Modi: Mülleimer, Materiebälle und Singularitäten.",
              "",
              "Im Modus Materieball werden je &e256 Gegenstände&r zu einem &6Materieball&r. Dafür braucht der Kondensator eine Speicherkomponente in seinem Komponentenplatz, sonst hat er keinen Puffer.",
              "",
              "Was du hineinwirfst, ist egal. Bruchstein, Erde, Netherrack, alles zählt gleich. Ein Steinbruch und ein Exportbus füttern ihn ohne Pause.",
          ],
          tasks=[task_item("ae2:condenser", 1), task_item("ae2:matter_ball", 64)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(5)],
          deps=["welcome"], icon="ae2:matter_ball"),

    quest("singularity", 5, 4.5, "&5&lSingularität",
          subtitle="256 000 Gegenstände in einer Kugel.",
          description=[
              "Im Modus Singularität frisst der Kondensator &e256 000 Gegenstände&r für eine &6Singularität&r. Das schafft er nur mit einer &664k-Komponente&r oder größer im Komponentenplatz, darum gibt es Singularitäten erst jetzt.",
              "",
              "&eDer schnelle Weg:&r Die &6Reaktionskammer&r von Advanced AE (unten im Kapitel) macht aus &e64 Materiebällen&r, 100 mB Lava und einer Million AE eine Singularität. Das sind nur gut 16 000 Gegenstände.",
              "",
              "Singularitäten brauchst du für die Quantenbrücke, die Akkumulationspresse von MEGA, die Quantenlegierung von Advanced AE und das Einrichtungsset der drahtlosen Verbinder.",
          ],
          tasks=[task_item("ae2:singularity", 2)],
          rewards=[reward_item("ae2:matter_ball", 32), reward_table("s4_common"), reward_xp(10)],
          deps=["matter"], icon="ae2:singularity", size=1.5, shape="hexagon"),

    quest("entangled", 7.5, 4.5, "&dVerschränkt",
          subtitle="Ein Knall, zwei Hälften.",
          description=[
              "Eine &6Quantenverschränkte Singularität&r entsteht durch eine Explosion. Wirf eine Singularität und eine &6Enderperle&r (oder Enderstaub) zusammen auf den Boden und sprenge sie, ein Creeper reicht schon.",
              "",
              "Heraus kommen immer &ezwei&r Singularitäten, die zusammengehören. Nur dieses Paar verbindet zwei Quantenbrücken miteinander.",
              "",
              "&eTipp:&r Benenne jedes Paar sofort am Amboss, zum Beispiel &7\"Basis Nether\"&r. Zwei einzelne Singularitäten aus verschiedenen Explosionen passen nicht zusammen.",
          ],
          tasks=[task_item("ae2:quantum_entangled_singularity", 2)],
          rewards=[reward_item("minecraft:tnt", 4), reward_xp(5)],
          deps=["singularity"], icon="ae2:quantum_entangled_singularity"),

    quest("bridge", 10, 4.5, "&b&lQuantenbrücke",
          subtitle="Ein dichtes Kabel durch alle Dimensionen.",
          description=[
              "Eine &6Quantenbrücke&r besteht aus einer &6ME-Quantentunnelkammer&r in der Mitte und acht &6ME-Quantentunnelringen&r drumherum, also ein flaches 3 x 3. Du brauchst zwei davon, eine an jedem Ende.",
              "",
              "&eRezepte:&r Der Ring ist Eisen, Logikprozessoren, ein Konstruktionsprozessor, eine Energiezelle und ein schlaues dichtes Kabel. Die Kammer ist Quarzglas mit vier Fluixperlen.",
              "",
              "In jede Kammer kommt eine Hälfte eines verschränkten Paares. Dann trägt die Brücke &e32 Kanäle&r über jede Entfernung, auch vom Nether oder aus dem End in deine Basis. Nur die vier Ringe an den Seiten nehmen Kabel an, die Ecken nicht.",
              "",
              "&cWichtig:&r Beide Seiten müssen geladen sein. Am fernen Ende hilft ein &6Raumanker&r (Abschnitt Raumspeicher).",
          ],
          tasks=[task_item("ae2:quantum_ring", 16), task_item("ae2:quantum_link", 2)],
          rewards=[reward_item("ae2:fluix_pearl", 4), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["entangled"], icon="ae2:quantum_link", size=1.75, shape="gear"),

    # ---- Raumspeicher -----------------------------------------------------------
    quest("spatial", 3.75, 8, "&3Raumpylone",
          subtitle="Ein Stück Welt ausschneiden.",
          description=[
              "Mit &6Spatial IO&r schneidest du einen Quader aus der Welt aus und tauschst ihn gegen einen gleich großen Quader in einer eigenen Speicherdimension. So ziehst du zum Beispiel einen &6Makellosen Certusquarzknospenblock&r aus einem Meteoriten in deine Basis.",
              "",
              "&eAufbau:&r Die &6Raumpylone&r (Quarzglas, Glaskabel, Fluixstaub, Fluixkristall) bilden eine Hülle um den Bereich. Der eigentliche Raum ist die Hülle minus einen Block nach innen. Jede Pylonenreihe muss mindestens zwei Blöcke lang sein und braucht einen Kanal. Je mehr der Hülle du füllst, desto effizienter wird es.",
              "",
              "Dazu kommt der &6IO-Raumport&r (Glas, Glaskabel, ME-IO-Port, Eisen, Konstruktionsprozessor). Alles muss im selben Netz hängen, und pro Netz geht nur ein Aufbau. Ein eigenes Unternetz ist am einfachsten.",
          ],
          tasks=[task_item("ae2:spatial_pylon", 16), task_item("ae2:spatial_io_port", 1)],
          rewards=[reward_item("ae2:fluix_crystal", 16), reward_xp(5)],
          deps=["welcome"], icon="ae2:spatial_pylon"),

    quest("spatial_cell", 6.25, 8, "&3Raumspeicherzellen",
          subtitle="Einmal benutzt, für immer festgelegt.",
          description=[
              "Die &62³-Raumkomponente&r ist Glowstone, vier Fluixperlen und ein Konstruktionsprozessor. Vier davon ergeben eine &616³-Komponente&r, vier 16³ eine &6128³-Komponente&r. Mit einem Gehäuse wird daraus eine Zelle.",
              "",
              "&eSo geht es:&r Zelle in den IO-Raumport, Redstone-Impuls, und der Inhalt der Pylone tauscht mit dem Raum in der Zelle. Der Port zieht den Strom auf einen Schlag, große Räume brauchen sehr viel AE. Die &6MEGA-Energiezelle&r (acht dichte Energiezellen um einen Akkumulationsprozessor) hält 12,8 Millionen AE und eignet sich als Puffer.",
              "",
              "&cAchtung:&r Eine benutzte Zelle behält ihre Maße für immer und lässt sich nicht zurücksetzen. Alles im Bereich wird mitgenommen, auch du. Steh nie zwischen den Pylonen, wenn jemand den Knopf drückt.",
          ],
          tasks=[task_item("ae2:spatial_storage_cell_16", 1)],
          rewards=[reward_item("ae2:fluix_pearl", 4), reward_xp(10)],
          deps=["spatial"], icon="ae2:spatial_storage_cell_16"),

    quest("anchor", 8.75, 8, "&3&lRaumanker",
          subtitle="Das Netz bleibt wach.",
          description=[
              "Ein ME-Netz arbeitet nur, solange seine Chunks geladen sind. Der &6Raumanker&r lädt jeden Chunk, in dem ein Teil seines Netzes liegt. Ein Kabel über die Chunkgrenze reicht, um den nächsten Chunk mitzunehmen.",
              "",
              "&eRezept:&r drei Raumpylone oben, Glaskabel links und rechts, eine &6128³-Raumkomponente&r in der Mitte, Eisen und ein Konstruktionsprozessor unten.",
              "",
              "Über Quantenbrücken wirkt er weiter, aber nicht über Dimensionen. Steht das andere Ende im Nether, braucht auch das Netz dort einen Anker. Auf diesem Server sorgt er auch für Zufallsticks, Pflanzen und Certus wachsen also weiter.",
              "",
              "Er braucht &d80 AE/t&r plus etwas mehr für jeden weiteren Chunk. Halte deine Netze kompakt.",
          ],
          tasks=[task_item("ae2:spatial_anchor", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_table("s4_common"), reward_xp(10)],
          deps=["spatial_cell"], icon="ae2:spatial_anchor"),

    # ---- Advanced AE ------------------------------------------------------------
    quest("reaction", 2.5, 11.5, "&5&lReaktionskammer",
          subtitle="Wasser, Strom und viel Geduld weniger.",
          description=[
              "Die &6Reaktionskammer&r von Advanced AE erzwingt Reaktionen, die sonst in Wasser oder Lava passieren, mit einer Flüssigkeit und sehr viel Strom. Sie wird aus einem Materiekondensator, einer Vibrationskammer, Fluixstaub, Glowstone und einem Eimer gebaut.",
              "",
              "&eWas sie kann:&r 64 Fluix aus je 16 geladenem Certus, Redstone und Netherquarz, 64 Himmelsstahl aus je 16 geladenem Certus, Eisen und Himmelsstein, 64 Entro aus Entro Dust und Fluix, und eine Singularität aus 64 Materiebällen.",
              "",
              "&eKronwerke:&r Geladenen Certus macht sie hier nicht. Den gibt es weiter nur aus der Imbuement-Kammer und dem Energizing Orb.",
              "",
              "&eStrom:&r Eine Kammer zieht pro Rezept 100 000 bis eine Million AE. Häng sie an einen Schablonen-Provider als Block, dann zieht sie direkt aus dem Netz, und stell dichte Energiezellen dazu. Externer Strom über Kabel geht auch.",
          ],
          tasks=[task_item("advanced_ae:reaction_chamber", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="advanced_ae:reaction_chamber", size=1.5, shape="hexagon"),

    quest("quantum_alloy", 5, 11.5, "&dQuantenlegierung",
          subtitle="Zerbrochene Singularitäten.",
          description=[
              "In der Reaktionskammer wird eine Singularität mit zwei Enderstaub, zwei Himmelssteinstaub und etwas Lava zu zwei &6Zerbrochenen Singularitäten&r.",
              "",
              "Die Gravurmaschine (oder der Brecher von Mekanism) mahlt sie zu &6Quanteninfundiertem Staub&r. Ein Staub und 4 000 mB Wasser ergeben in der Kammer 1 000 mB &6Quanteninfusion&r.",
              "",
              "Aus 1 000 mB Quanteninfusion, vier Kupferbarren, vier Zerbrochenen Singularitäten und &evier Singularitäten&r wird ein &6Quantenlegierungsbarren&r. Jeder Barren kostet also mehr als sechs Singularitäten. Lass den Kondensator Tag und Nacht laufen.",
          ],
          tasks=[task_item("advanced_ae:shattered_singularity", 4), task_item("advanced_ae:quantum_alloy", 2)],
          rewards=[reward_item("ae2:singularity", 2), reward_xp(10)],
          deps=["reaction", "singularity"], icon="advanced_ae:quantum_alloy"),

    quest("quantum_processor", 7.5, 11.5, "&dQuantenprozessor",
          subtitle="Der vierte Druck.",
          description=[
              "Die &6Quantenpresse&r entsteht in der Gravurmaschine aus Logikdruck oben, Konstruktionsdruck unten und einer Zerbrochenen Singularität in der Mitte.",
              "",
              "Quantenlegierung unter der Presse ergibt den gedruckten Schaltkreis, und den presst du wie jeden Prozessor mit Redstone und Gedrucktem Silizium fertig.",
              "",
              "Quantenprozessoren stecken im &6Erweiterten IO-Bus&r (Import- und Exportbus in einem, achtmal so schnell wie ein Exportbus) und später in fast allem, was Stufe 5 bringt.",
              "",
              "&cAusblick:&r Der &6Quantencomputer&r, eine CPU ohne Grenze für gleichzeitige Aufträge, und die &6Quantenrüstung&r mit Flug, Magnet und Nachladen aus dem Netz kommen in Stufe 5. Wer jetzt Quantenlegierung und Prozessoren hortet, baut sie dann sofort.",
          ],
          tasks=[task_item("advanced_ae:quantum_processor", 4)],
          rewards=[reward_item("ae2:printed_silicon", 16), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["quantum_alloy"], icon="advanced_ae:quantum_processor"),

    quest("adv_provider", 2.5, 13.5, "&5Gerichteter Provider",
          subtitle="Jede Zutat auf ihre Seite.",
          description=[
              "Der &6ME Advanced Pattern Provider&r schickt jede Zutat einer Schablone an eine Seite der Maschine, die du festlegst. Kein Rohrgewirr mehr für Maschinen mit Seitenkonfiguration. Mekanism lässt grüßen.",
              "",
              "&eRezept:&r Schablonen-Provider, Redstone, Enderperle und Logikprozessor an der Werkbank. Mit einem Ex-Provider statt des normalen bekommst du die große Version mit 36 Plätzen.",
              "",
              "&eSo geht es:&r Leg eine fertige Verarbeitungsschablone in den &6Advanced Pattern Encoder&r (Rechtsklick in der Hand). Dort wählst du für jede Zutat eine Seite und nimmst die erweiterte Schablone heraus. In normalen Providern verhält sie sich wie eine normale Schablone.",
              "",
              "Die Upgrade-Karten machen aus einem stehenden Provider einen erweiterten, ohne dass du ihn abbauen musst.",
          ],
          tasks=[task_item("advanced_ae:small_adv_pattern_provider", 1), task_item("advanced_ae:adv_pattern_encoder", 1)],
          rewards=[reward_item("ae2:blank_pattern", 16), reward_xp(5)],
          deps=["reaction"], icon="advanced_ae:adv_pattern_provider"),

    # ---- Extended AE ------------------------------------------------------------
    quest("ex_machines", 0, 17, "&3&lEx-Maschinen",
          subtitle="Alles doppelt, alles schneller.",
          description=[
              "Mit Stufe 4 baut der &6Crystal Assembler&r die großen Maschinen von Extended AE. Fast alle brauchen &6Concurrent Processors&r aus Stufe 3.",
              "",
              "&6ME Extended Drive&r: ein Laufwerk mit 20 statt 10 Zellen. &6ME Extended Pattern Provider&r und &6ME Extended Interface&r: viel mehr Plätze in einem Block. &6Extended Inscriber&r: vier Gravuren gleichzeitig, ideal für Silizium. &6Extended Molecular Assembler&r: acht Aufträge zugleich und doppelt so schnell. &6ME Extended IO Port&r: achtmal so schnell wie der normale.",
              "",
              "Die Upgrade-Gegenstände von Extended AE tauschen ein stehendes Gerät per Schleich-Rechtsklick gegen seine Ex-Version, Einstellungen und Inhalt bleiben.",
          ],
          tasks=[task_item("extendedae:ex_drive", 1), task_item("extendedae:ex_pattern_provider", 1)],
          rewards=[reward_item("extendedae:concurrent_processor", 4), reward_table("s4_common"), reward_xp(10)],
          deps=["welcome"], icon="extendedae:ex_drive", size=1.5, shape="hexagon"),

    quest("matrix", 2.5, 16, "&3Assembler-Matrix",
          subtitle="Ein Multiblock statt hundert Assembler.",
          description=[
              "Die &6Assembler Matrix&r ist Schablonen-Provider und Molekularassembler in einem großen Quader, 3 bis 7 Blöcke pro Kante, ganz gefüllt.",
              "",
              "&eAufbau:&r Kanten aus &6Assembler Matrix Frame&r, Seitenflächen aus Wall oder Glass, innen die Kerne. Ein &6Pattern Core&r hält 36 Werkbankschablonen, ein &6Craft Core&r rechnet acht Aufträge gleichzeitig, &6Speed Cores&r machen ihn schneller, ab fünf ist volle Geschwindigkeit erreicht. Mindestens ein Pattern Core und ein Craft Core müssen drin sein.",
              "",
              "Die Kerne baut der Crystal Assembler mit Leuchtfarbbällen. Leuchten die Linien am Rahmen blau, ist die Matrix fertig. Sie spart dir viele Kanäle, weil nicht jeder Assembler einen eigenen Provider braucht.",
          ],
          tasks=[task_item("extendedae:assembler_matrix_pattern", 1), task_item("extendedae:assembler_matrix_crafter", 1)],
          rewards=[reward_item("extendedae:assembler_matrix_frame", 8), reward_xp(10)],
          deps=["ex_machines"], icon="extendedae:assembler_matrix_crafter"),

    quest("wireless", 2.5, 18, "&3Drahtlose Verbinder",
          subtitle="Kabel durch die Luft.",
          description=[
              "Der &6ME Wireless Connector&r verbindet zwei Netzteile ohne Kabel, aber nur in derselben Dimension und mit begrenzter Reichweite. Der Crystal Assembler macht zwei Stück aus einem Maschinenrahmen, schlauen dichten Kabeln, Drahtlosempfängern und Drahtlosverstärkern.",
              "",
              "&eVerbinden:&r Mit dem &6ME Wireless Setup Kit&r klickst du nacheinander beide Verbinder an. Schleich-Klick löscht die Auswahl. Das Kit braucht im Crystal Assembler eine &6Singularität&r.",
              "",
              "Je weiter auseinander, desto mehr Strom, und nicht gleichmäßig. Energiekarten senken den Verbrauch um je 10 Prozent. Der &6ME Wireless Hub&r verbindet bis zu acht Verbinder und braucht eine Quantentunnelkammer.",
          ],
          tasks=[task_item("extendedae:wireless_connect", 2), task_item("extendedae:wireless_tool", 1)],
          rewards=[reward_item("ae2:wireless_booster", 2), reward_xp(5)],
          deps=["ex_machines"], icon="extendedae:wireless_connect"),
]

images = [
    head("title", "Applied Energistics 2: Fortgeschritten", 0, -3.6, height=1.2, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -2.3, height=0.55, kind="note", colour="end"),
    head("cells", "Große Zellen und MEGA", 3.6, -1.3, colour="water"),
    head("singularity", "Singularitäten und Quantenbrücke", 1.6, 3.1, colour="end"),
    head("spatial", "Raumspeicher", 3.6, 6.7, colour="water"),
    head("advanced", "Advanced AE", 1.6, 10.1, colour="magic"),
    head("extended", "Extended AE", -0.6, 14.9, colour="water"),
]

chapter(C, "Applied Energistics 2: Fortgeschritten", "megacells:item_storage_cell_1m", "tech", quests,
        shape="square", order=36, stage=4,
        subtitle=["Stufe 4: große Zellen, Quantenbrücke, Raumspeicher, MEGA Cells und Advanced AE."],
        images=images)
