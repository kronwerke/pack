"""Mekanism in stage 3: the advanced control circuit (AE2 printed silicon), ore tripling with
oxygen and the purification chamber, diamond infusion, reinforced alloy and refined obsidian,
atomic alloy, the teleporter, the digital miner, the advanced tier, the advanced solar generator,
the industrial turbine and the Mekanism MoreMachine CNC stamper. Continues mekanism.py. Elite and
ultimate circuits, the injection chamber, the 5x machines and the entangloporter are stage 4 and
text only.
Recipes follow kubejs/server_scripts/kronwerke/tech.js and milestones.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mekanism_advanced"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Der fortgeschrittene Schaltkreis ----------------------------------------
    quest("welcome", 0, 1.5, "&5&lMekanism: Fortgeschritten",
          subtitle="Ein Schaltkreis, der Silizium braucht.",
          description=[
              "Mit &6Stufe 3, dem Stahlwerk&r, öffnet Mekanism seine zweite Ebene. Der Schlüssel zu fast allem darin ist der &6Fortschrittliche Steuerschaltkreis&r.",
              "",
              "&eRezept auf Kronwerke:&r oben Infundierte Legierung, Einfacher Steuerschaltkreis, Infundierte Legierung, darunter in der Mitte ein &6Gedrucktes Silizium&r. Das Silizium kommt aus dem &6Inscriber&r von Applied Energistics 2 mit der Silizium-Presse. Alle anderen Wege zu diesem Schaltkreis gibt es nicht mehr.",
              "",
              img(item_texture("mekanism:advanced_control_circuit"), 32, 32),
              "",
              "&eWas jetzt offen ist:&r die Klärkammer und damit die &6Erzverdreifachung&r, Verstärkte Legierung, Raffiniertes Obsidian und Atomlegierung, Teleporter und Digitaler Miner, die fortschrittliche Stufe für Fabriken, Kabel und Speicher, der Erweiterte Solargenerator, die &6Industrieturbine&r und die ersten Maschinen von Mekanism MoreMachine.",
              "",
              "&cWas noch wartet:&r Elite- und Ultimativ-Stufe, die Vervierfachung und Verfünffachung, der Quantenverschränkungsporter, QIO und Fusion kommen in Stufe 4, Spaltreaktor, SPS und Antimaterie in Stufe 5.",
          ],
          tasks=[task_item("mekanism:advanced_control_circuit", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_table("s3_common"), reward_xp(10)],
          icon="mekanism:advanced_control_circuit", size=2.0, shape="hexagon"),

    quest("circuits", 2.75, 0, "&aSchaltkreise auf Vorrat",
          subtitle="Jede neue Maschine will zwei davon.",
          description=[
              "Klärkammer, Stufen-Installateur, Fabriken, Turbinenventile und der Stahlkern: alles in diesem Kapitel braucht &6Fortschrittliche Steuerschaltkreise&r, meist zwei oder mehr.",
              "",
              "Der Engpass ist das &6Gedruckte Silizium&r. Wenn du AE2 nicht selbst spielst, tausch mit jemandem, der einen Inscriber laufen hat. Oder bau dir die &6CNC Stamper&r aus Mekanism MoreMachine (Abschnitt MoreMachine), die drückt Silizium mit derselben Presse.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 3 auch &e250 Fortschrittliche Steuerschaltkreise&r im Technik-Pfeiler, jeder zählt acht Punkte. Ein Schaltkreisvorrat lohnt sich also doppelt.",
          ],
          tasks=[task_item("mekanism:advanced_control_circuit", 16)],
          rewards=[reward_item("mekanism:basic_control_circuit", 8), reward_item("mekanism:alloy_infused", 16)],
          deps=["welcome"]),

    # ---- Erzverdreifachung --------------------------------------------------------
    quest("oxygen", 2.75, 3, "&bSauerstoff aus Wasser",
          subtitle="Der Elektrolyseur spaltet Wasser.",
          description=[
              "Die Klärkammer braucht &bSauerstoff&r. Den macht der &6Elektrolyseur&r (Elektrolytischer Aufteiler): aus 2 mB Wasser werden 2 mB &bWasserstoff&r und 1 mB &bSauerstoff&r. Wasser bekommt er über Rohrleitungen, zum Beispiel von einer Elektrischen Pumpe in einer Wasserquelle.",
              "",
              "&eRezept:&r ein Elektrolytischer Kern in der Mitte, Infundierte Legierung links und rechts, Eisen in die Ecken, Redstone oben und unten.",
              "",
              "Wasserstoff fällt dabei doppelt so viel an wie Sauerstoff. Stell seinen Tank im Fenster auf &eAblassen&r, oder verbrenne ihn im Gasverbrennungsgenerator. Den Sauerstoff führst du mit &6Druckschläuchen&r zur Kammer.",
              "",
              "&eFür den Anfang:&r Feuerstein im Chemikalien-Slot der Klärkammer gibt je 10 mB Sauerstoff. Für eine Straße, die durchläuft, reicht das aber nicht.",
          ],
          tasks=[task_item("mekanism:electrolytic_separator", 1), task_item("mekanism:basic_pressurized_tube", 8)],
          rewards=[reward_item("mekanism:basic_pressurized_tube", 8), reward_xp(5)],
          deps=["welcome"], icon="mekanism:electrolytic_separator"),

    quest("purification", 5.25, 1.5, "&d&lKlärkammer",
          subtitle="Erz und Sauerstoff, drei Klumpen.",
          description=[
              "Die &6Klärkammer&r (im Fenster Reinigungskammer) ist das Herz der Erzverdreifachung. &eRezept:&r eine Anreicherungskammer in der Mitte, Osmium links und rechts, Fortschrittliche Steuerschaltkreise oben und unten, Infundierte Legierung in die Ecken.",
              "",
              "Sie nimmt ein Erz und Sauerstoff und macht daraus &6Klumpen&r. Solange sie arbeitet, verbraucht sie in jedem Tick Sauerstoff, also schließ den Elektrolyseur fest an. Ihr Fenster hat einen Chemikalien-Slot unten links und einen Tank daneben.",
              "",
              "Strom braucht sie mehr als die Anreicherungskammer. Ein einfacher Energie-Würfel und ein paar Generatoren reichen für den Anfang.",
          ],
          tasks=[task_item("mekanism:purification_chamber", 1)],
          rewards=[reward_item("mekanism:raw_osmium", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["oxygen"], icon="mekanism:purification_chamber", size=1.75, shape="hexagon"),

    quest("clumps", 7.75, 1.5, "&7Klumpen",
          subtitle="Der erste Schritt der Dreifach-Straße.",
          description=[
              "Gib Erze in die Klärkammer. &eWas herauskommt:&r",
              "Ein Erzblock (mit Behutsamkeit) ergibt &e3 Klumpen&r.",
              "Ein Rohes Erz ergibt &e2 Klumpen&r.",
              "Ein Block aus Rohem Erz ergibt &e18 Klumpen&r.",
              "",
              img(item_texture("mekanism:clump_iron"), 32, 32),
              "",
              "Jeder Klumpen wird am Ende ein Barren. Zum Vergleich: In der Anreicherungskammer gaben drei Rohe Erze nur vier Staub. Mit der Kammer werden daraus sechs.",
              "",
              "&eTipp:&r Bau ab jetzt mit &6Glück III&r ab. Etwa 2,2 Rohe Erze pro Block mal zwei Klumpen sind rund 4,4 Barren aus einem Erzblock, mehr als die drei aus einem Block mit Behutsamkeit.",
          ],
          tasks=[task_item("mekanism:clump_iron", 16)],
          rewards=[reward_item("minecraft:raw_iron", 32)],
          deps=["purification"]),

    quest("dirty", 10.25, 1.5, "&7Dreckiger Staub",
          subtitle="Zerkleinerer, dann Anreicherungskammer.",
          description=[
              "Ein Klumpen ist noch kein Barren. Der &6Zerkleinerer&r aus Stufe 2 macht aus jedem Klumpen einen &6Dreckigen Staub&r, die &6Anreicherungskammer&r macht daraus sauberen Staub, und der Schmelzer oder ein Ofen schmilzt ihn zum Barren.",
              "",
              "&eDie Dreifach-Straße:&r Klärkammer, Zerkleinerer, Anreicherungskammer, Energiegeladener Schmelzer. Vier Maschinen hintereinander, jede mit Auto-Auswurf zur nächsten. Die Maschinen aus deiner Verdopplungsstraße kannst du dafür weiter benutzen, die Kammer kommt einfach davor.",
              "",
              img(item_texture("mekanism:dirty_dust_iron"), 32, 32),
          ],
          tasks=[task_item("mekanism:dirty_dust_iron", 16)],
          rewards=[reward_item("mekanism:enriched_carbon", 16)],
          deps=["clumps"]),

    quest("tripling", 12.75, 1.5, "&d&lErzverdreifachung",
          subtitle="Drei Barren aus einem Erz.",
          description=[
              "Lass die Straße mit allem laufen, was du findest: &6Eisen, Kupfer, Gold, Osmium, Zinn, Blei, Uran&r. Auch &6Silber&r aus Mekanism MoreMachine geht durch die Kammer, Rohes Silber liegt in der Oberwelt.",
              "",
              "Mit Fabriken (Abschnitt Fortschrittliche Stufe) laufen Klärkammer, Zerkleinerer und Anreicherungskammer jeweils fünffach. Der Engpass ist dann meist der Sauerstoff, ein zweiter Elektrolyseur hilft.",
              "",
              "&eKronwerke:&r Für den Stahl des Obelisken braucht es Eisen in Mengen. Eine Dreifach-Straße vor der Stahlstraße bringt fünfzig Prozent mehr Eisen als die Verdopplung aus Stufe 2.",
              "",
              "&eUnd die Magier?&r Theurgy hat in Stufe 3 eine eigene Erzverdreifachung mit Alchemie, ohne Strom und genauso ergiebig. Das ist Absicht: Erz gibt es auf beiden Seiten gleich gut.",
          ],
          tasks=[task_item("mekanism:clump_copper", 32), task_item("mekanism:clump_gold", 16)],
          rewards=[reward_item("minecraft:raw_iron", 64), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["dirty"], icon="mekanism:clump_gold", size=2.0, shape="gear"),

    quest("chem_upgrade", 5.25, 3.75, "&8Chemie-Upgrade",
          subtitle="Weniger Sauerstoff pro Klumpen.",
          description=[
              "Geschwindigkeitsupgrades machen die Klärkammer schneller, sie verbraucht dann aber auch mehr Sauerstoff pro Tick. Das &6Chemical Upgrade&r (zwei Glas, zwei Infundierte Legierung, ein Eisenstaub) senkt den Chemikalienverbrauch wieder.",
              "",
              "Eine Mischung aus Geschwindigkeit und Chemie hält die Kammer schnell, ohne dass dein Elektrolyseur nicht mehr hinterherkommt.",
          ],
          tasks=[task_item("mekanism:upgrade_chemical", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 4)],
          deps=["purification"], optional=True),

    quest("outlook_4x", 15.5, 1.5, "&dVier- und Fünffach",
          subtitle="Was nach der Klärkammer kommt.",
          description=[
              "Mekanism kann noch mehr aus einem Erz holen. Die &6Chemische Injektionskammer&r macht mit Chlorwasserstoff aus einem Erz vier Scherben, das ist die Vervierfachung. Die Verfünffachung braucht Auflösungskammer, Wäscher und Kristallisierer.",
              "",
              "&cBeides kommt in Stufe 4:&r Die Injektionskammer braucht Elite-Steuerschaltkreise, die drei Maschinen der Verfünffachung Ultimative Schaltkreise. In Stufe 3 ist die Verdreifachung das Beste, was Mekanism kann.",
              "",
              "Ebenfalls in Stufe 4 kommt der &6Quantenverschränkungsporter&r. Er schickt Strom, Gegenstände, Flüssigkeiten und Chemikalien ohne Kabel an einen zweiten Porter. Bis dahin helfen Ender-Zellen von Powah und Mods wie XNet oder LaserIO.",
              "",
              "Das &6Salz&r, das du aus Stufe 2 aufgehoben hast, wird dann zu Chlorwasserstoff. Leg dir also ruhig schon einen Vorrat an.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["tripling"], icon="mekanism:shard_iron", optional=True),

    # ---- Diamant und Obsidian -----------------------------------------------------
    quest("diamond", 0, 7.5, "&bDiamant als Infusionsstoff",
          subtitle="Ein Diamant, achtzig Millibuckets.",
          description=[
              "Die Infusionsanlage kennt einen dritten Stoff: &bDiamant&r. Diamantstaub gibt 10 mB. Schickst du einen ganzen Diamanten durch die &6Anreicherungskammer&r, wird er zum &6Angereicherten Diamanten&r, und der gibt &e80 mB&r.",
              "",
              "Damit machst du in diesem Abschnitt Verstärkte Legierung (20 mB) und Raffinierten Obsidianstaub (10 mB). Ein Diamant reicht also für vier Legierungen oder acht Staub.",
          ],
          tasks=[task_item("mekanism:enriched_diamond", 4)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["welcome"], icon="mekanism:enriched_diamond"),

    quest("reinforced", 2.5, 6.5, "&bVerstärkte Legierung",
          subtitle="Infundierte Legierung, getränkt in Diamant.",
          description=[
              "Eine &6Infundierte Legierung&r mit 20 mB &bDiamant&r ergibt in der Infusionsanlage eine &6Verstärkte Legierung&r.",
              "",
              img(item_texture("mekanism:alloy_reinforced"), 32, 32),
              "",
              "In Stufe 3 brauchst du sie vor allem für andere: Der Meilenstein der Magie-Säule, der &6Elfenstern&r, will eine Verstärkte Legierung. Die Magier können sie nicht selbst machen, also bring ihnen ein paar vorbei.",
              "",
              "&cAusblick:&r Gleich im nächsten Abschnitt wird sie zur Atomlegierung, mit Stufe 4 steckt sie im Elite-Steuerschaltkreis. Ein Vorrat schadet nicht.",
          ],
          tasks=[task_item("mekanism:alloy_reinforced", 8)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_table("s3_common")],
          deps=["diamond"]),

    quest("refined_obsidian", 2.5, 8.5, "&5Raffiniertes Obsidian",
          subtitle="Staub, Diamant, Osmium.",
          description=[
              "&eSo geht es:&r Der Zerkleinerer macht aus einem Obsidian vier &6Obsidianstaub&r. In der Infusionsanlage wird jeder Staub mit 10 mB Diamant zu &6Raffiniertem Obsidianstaub&r. Den presst der &6Osmium Kompressor&r mit Osmium zum Barren, leg dazu Osmiumbarren in seinen Chemikalien-Slot.",
              "",
              img(item_texture("mekanism:ingot_refined_obsidian"), 32, 32),
              "",
              "Raffiniertes Obsidian ist das stärkste Material von Mekanism Tools, und es steckt im &6Teleporter-Rahmen&r. Als Infusionsstoff macht er aus Verstärkter Legierung die Atomlegierung.",
          ],
          tasks=[task_item("mekanism:dust_refined_obsidian", 8), task_item("mekanism:ingot_refined_obsidian", 8)],
          rewards=[reward_item("minecraft:obsidian", 16), reward_table("s3_common"), reward_xp(5)],
          deps=["diamond"], icon="mekanism:ingot_refined_obsidian"),

    quest("atomic", 5, 7.5, "&5&lAtomlegierung",
          subtitle="Verstärkte Legierung, getränkt in Obsidian.",
          description=[
              "Die &6Atomlegierung&r ist die stärkste Legierung, die du in Stufe 3 machen kannst. Eine &6Verstärkte Legierung&r mit &e40 mB Raffiniertem Obsidian&r ergibt in der Infusionsanlage eine Atomlegierung.",
              "",
              "&eDer Infusionsstoff:&r Raffinierter Obsidianstaub gibt 10 mB, du bräuchtest also vier Staub pro Legierung. Schick den Staub vorher durch die &6Anreicherungskammer&r, dann wird er zu Angereichertem Obsidian und gibt &e80 mB&r. Das reicht für zwei Legierungen.",
              "",
              "Atomlegierung steckt im &6Teleportationskern&r und im &6Robit&r, und damit in Teleporter und Digitalem Miner.",
          ],
          tasks=[task_item("mekanism:alloy_atomic", 4)],
          rewards=[reward_item("mekanism:alloy_reinforced", 4), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["reinforced", "refined_obsidian"], icon="mekanism:alloy_atomic", size=1.5, shape="hexagon"),

    quest("teleporter", 7.5, 6.5, "&dTeleporter",
          subtitle="Von Basis zu Basis in einem Schritt.",
          description=[
              "&eDer Kern:&r Vier Enderperlen in die Ecken, zwei &6Atomlegierungen&r oben und unten, zwei Goldbarren links und rechts und ein Diamant in die Mitte ergeben einen &6Teleportationskern&r.",
              "",
              "&eDer Teleporter:&r der Kern in der Mitte, vier Stahlgehäuse an den Seiten, vier Einfache Steuerschaltkreise in den Ecken.",
              "",
              "&eDer Rahmen:&r Acht Raffinierte Obsidianbarren um einen Raffinierten Glowstonebarren ergeben neun &6Teleporter-Rahmen&r. Bau damit ein Rechteck, 4 Blöcke breit und 5 hoch, mit einer Öffnung von 2 mal 3 Blöcken. Der Teleporter selbst ist einer der Rahmenblöcke.",
              "",
              "Gib beiden Teleportern im Fenster dieselbe &eFrequenz&r und versorge sie mit Strom. Jeder Sprung kostet Energie, je weiter, desto mehr.",
              "",
              "&eFür unterwegs:&r Der &6Tragbare Teleportierer&r (ein Kern, zwei Energietabletts, zwei Einfache Steuerschaltkreise) springt zu jedem Teleporter auf deiner Frequenz.",
          ],
          tasks=[task_item("mekanism:teleporter", 1), task_item("mekanism:teleporter_frame", 13)],
          rewards=[reward_item("mekanism:ingot_refined_obsidian", 8), reward_item("minecraft:ender_pearl", 4), reward_xp(10)],
          deps=["atomic"], icon="mekanism:teleporter"),

    quest("miner", 7.5, 8.75, "&6&lDigitaler Miner",
          subtitle="Er baut ab, was du ihm sagst.",
          description=[
              "Der &6Digitale Miner&r (im Spiel Digitales Abbaugerät) baut nach deinen Filtern alles in einem Radius von bis zu &e32 Blöcken&r ab, ohne dass du die Gänge selbst gräbst.",
              "",
              "&eRezept:&r oben Atomlegierung, Einfacher Steuerschaltkreis, Atomlegierung. In der Mitte ein &6Logistischer Sortierer&r, der &6Robit&r, ein Logistischer Sortierer. Unten Teleportationskern, Stahlgehäuse, Teleportationskern.",
              "&6Robit:&r oben ein Stahlbarren, in der Mitte Atomlegierung zwischen zwei Energietabletts, unten eine Persönliche Truhe zwischen zwei Raffinierten Obsidianbarren.",
              "&6Logistischer Sortierer:&r Eisen rundherum, oben in der Mitte ein Kolben, in der Mitte ein Einfacher Steuerschaltkreis.",
              "",
              "&eSo richtest du ihn ein:&r Stell Radius sowie kleinste und größte Y-Höhe ein und leg Filter an, zum Beispiel für ein Tag wie Erze. Dann Start. Ohne Upgrades braucht er 80 Ticks pro Block, Geschwindigkeitsupgrades helfen. Mit Behutsamkeit kostet jeder Block zwölfmal so viel Strom. Stell eine Kiste oder einen Transporter an seine Rückseite und schalte Auto-Auswurf ein.",
              "",
              "&eTipp:&r Mit Filter nur auf Erze und der Dreifach-Straße dahinter wird jede Ader zu Barren, ohne dass du einen Stein anfasst.",
          ],
          tasks=[task_item("mekanism:digital_miner", 1)],
          rewards=[reward_item("mekanism:upgrade_speed", 2), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["atomic"], icon="mekanism:digital_miner", size=1.75, shape="gear"),

    # ---- Fortschrittliche Stufe ---------------------------------------------------
    quest("installer", 10.25, 7.5, "&aFortgeschrittener Stufen Installateur",
          subtitle="Aus drei Plätzen werden fünf.",
          description=[
              "Der &6Fortgeschrittene Stufen Installateur&r (Infundierte Legierung, Fortschrittliche Schaltkreise, Osmium und ein Brett) hebt eine &aEinfache Fabrik&r auf die fortschrittliche Stufe. Klick ihn einfach auf die stehende Fabrik, sie behält ihren Inhalt.",
              "",
              "Eine Fortschrittliche Fabrik arbeitet an &efünf Gegenständen&r gleichzeitig statt drei. Die Elite- und die Ultimativ-Stufe mit sieben und neun Plätzen kommen in Stufe 4.",
          ],
          tasks=[task_item("mekanism:advanced_tier_installer", 1)],
          rewards=[reward_item("mekanism:advanced_control_circuit", 2), reward_table("s3_common")],
          deps=["purification"], icon="mekanism:advanced_tier_installer", size=1.5, shape="hexagon"),

    quest("adv_factory", 12.75, 6.5, "&dFortschrittliche Reinigungsfabrik",
          subtitle="Fünf Erze auf einmal.",
          description=[
              "Mach aus der Klärkammer erst mit dem Einfachen Installateur eine Fabrik, dann mit dem Fortgeschrittenen eine &6Fortschrittliche Reinigungsfabrik&r. Oder bau sie direkt an der Werkbank: die Einfache Reinigungsfabrik in der Mitte, Osmium links und rechts, Fortschrittliche Schaltkreise oben und unten, Infundierte Legierung in die Ecken.",
              "",
              "Damit sie nicht wartet, brauchen auch Zerkleinerer und Anreicherungskammer dahinter das gleiche Tempo. Mach aus allen drei Fortschrittliche Fabriken, dann trägt die Straße fünf Erze gleichzeitig.",
              "",
              "&eTipp:&r Der Knopf mit den Pfeilen im Fenster verteilt die Erze auf alle Plätze.",
          ],
          tasks=[task_item("mekanism:advanced_purifying_factory", 1)],
          rewards=[reward_item("minecraft:raw_gold", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["installer"], icon="mekanism:advanced_purifying_factory"),

    quest("adv_transmit", 12.75, 8.5, "&eFortschrittliche Leitungen",
          subtitle="Mehr Durchsatz für die größere Straße.",
          description=[
              "Acht einfache Kabel, Transporter, Rohre oder Druckschläuche um eine &6Infundierte Legierung&r ergeben acht der fortschrittlichen Sorte.",
              "",
              "&eWas sie mehr können:&r Das &6Fortschrittliche Universalkabel&r trägt sechzehnmal so viel Strom wie das einfache. Der &6Fortschrittliche Logistiktransporter&r ist doppelt so schnell und zieht 16 Gegenstände auf einmal aus einer Kiste statt einem. Druckschläuche und Rohre schaffen etwa das Vierfache.",
              "",
              "Eine Fabrikstraße mit fünf Plätzen pro Maschine braucht genau das.",
          ],
          tasks=[task_item("mekanism:advanced_universal_cable", 16), task_item("mekanism:advanced_logistical_transporter", 16)],
          rewards=[reward_item("mekanism:alloy_infused", 8)],
          deps=["installer"], icon="mekanism:advanced_universal_cable"),

    quest("adv_cube", 15.25, 7.5, "&aFortschrittlicher Energie-Würfel",
          subtitle="Viermal so viel Platz für Strom.",
          description=[
              "Der &6Fortschrittliche Energie-Würfel&r fasst viermal so viel wie der einfache und gibt viermal so schnell ab. &eRezept:&r der Einfache Energie-Würfel in der Mitte, Osmium links und rechts, Energietabletts oben und unten, Infundierte Legierung in die Ecken.",
              "",
              "Wird dir auch das zu klein, bau eine &6Induktionsmatrix&r: Induktionsgehäuse, ein Induktionsanschluss, darin Induktionszellen und -anbieter. Die fortschrittlichen Zellen und Anbieter sind jetzt offen.",
          ],
          tasks=[task_item("mekanism:advanced_energy_cube", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 2)],
          deps=["adv_transmit"], optional=True),

    # ---- Generatoren ----------------------------------------------------------------
    quest("adv_solar", 0, 13, "&eErweiterter Solargenerator",
          subtitle="Vier Solargeneratoren in einem.",
          description=[
              "Vier &6Solargeneratoren&r, zwei Infundierte Legierungen und drei Eisenbarren ergeben einen &6Erweiterten Solargenerator&r. Er liefert sechsmal so viel wie ein einzelner, aus vier gebaut ist das also ein klarer Gewinn.",
              "",
              "Er braucht etwas Platz um sich und freien Himmel. Nachts und bei Regen ruht er, ein Energie-Würfel dazwischen gleicht das aus.",
          ],
          tasks=[task_item("mekanismgenerators:advanced_solar_generator", 1)],
          rewards=[reward_item("mekanismgenerators:solar_generator", 2), reward_xp(5)],
          optional=True),

    quest("turbine_rotor", 2.75, 13, "&7Rotor und Blätter",
          subtitle="Das Innere der Turbine.",
          description=[
              "Die &6Industrieturbine&r ist der große Stromerzeuger von Mekanism. Zuerst das Innere:",
              "",
              "&6Turbinenrotor&r: Stahl und Infundierte Legierung. Die Rotoren stehen als Säule genau in der Mitte, vom Boden der Turbine nach oben.",
              "&6Rotorblatt&r: vier Stahl um eine Infundierte Legierung. Jeder Rotor trägt bis zu zwei Blätter, du setzt sie per Rechtsklick auf.",
              "&6Rotationskomplex&r: Stahl, Infundierte Legierung und zwei Fortschrittliche Schaltkreise. Er kommt oben auf den höchsten Rotor.",
          ],
          tasks=[task_item("mekanismgenerators:turbine_rotor", 2), task_item("mekanismgenerators:turbine_blade", 4),
                 task_item("mekanismgenerators:rotational_complex", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 32)],
          deps=["welcome"], icon="mekanismgenerators:turbine_blade"),

    quest("turbine", 5.5, 13, "&6&lIndustrieturbine",
          subtitle="Dampf rein, Strom raus.",
          description=[
              "&eDer Aufbau:&r Eine quadratische Hülle aus &6Turbinengehäuse&r mit ungerader Kantenlänge, die kleinste ist 5 mal 5. Strukturelles Glas darf in die Wände. In der Mitte die Rotorsäule mit dem Rotationskomplex obendrauf. Die ganze Ebene rund um den Komplex füllst du mit &6Druckventilen&r. Darüber kommen &6Elektromagnetische Spulen&r, die den Komplex und einander berühren, eine Spule für je vier Rotorblätter.",
              "",
              "&6Turbinenventile&r in der Hülle nehmen Dampf an und geben Strom ab. &6Turbinenabzüge&r gehören auf Höhe des Rotationskomplexes oder darüber. &6Sammlerkondensatoren&r über den Druckventilen machen aus Abdampf wieder Wasser.",
              "",
              "&eWoher der Dampf kommt:&r Der Thermoelektrische Dampfkessel aus Stufe 2 macht Dampf aus Wasser und Wärme. Dampf aus Oritech (Steam Boiler Addon an einem Generator) wandelt der &6Rotationskondensator&r in Mekanism-Dampf um. Die eigentliche Dampfquelle für die Turbine, der Spaltreaktor, kommt in Stufe 5. Bis dahin lernst du hier den Aufbau, und die Turbine wächst später einfach mit.",
          ],
          tasks=[task_item("mekanismgenerators:electromagnetic_coil", 1), task_item("mekanismgenerators:turbine_valve", 2),
                 task_item("mekanismgenerators:turbine_vent", 4), task_item("mekanism:pressure_disperser", 8)],
          rewards=[reward_item("mekanismgenerators:turbine_casing", 16), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["turbine_rotor"], icon="mekanismgenerators:turbine_casing", size=2.0, shape="gear"),

    # ---- Mekanism MoreMachine -----------------------------------------------------
    quest("cnc_stamper", 10.25, 13, "&3CNC Stamper",
          subtitle="Silizium drucken ohne Inscriber.",
          description=[
              "&6Mekanism MoreMachine&r bringt neue Maschinen im Mekanism-Stil. In Stufe 3 lohnt sich vor allem die &6CNC Stamper&r: ein Stahlgehäuse in der Mitte, Kolben links und rechts, Einfache Steuerschaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Sie presst mit einer Form im Formslot. Mit der &6Silizium-Presse&r aus AE2 macht sie aus Silizium &6Gedrucktes Silizium&r, genau das Teil, das jeder Fortschrittliche Steuerschaltkreis braucht. Mit den anderen AE2-Pressen druckt sie die Prozessorteile, mit den Formen von Immersive Engineering Bleche, Stangen und Drähte.",
              "",
              "&eAuch offen:&r die &6CNC Rolling Mill&r (Stahlgehäuse, Stahl, Schaltkreise, Redstone) walzt Barren zu Drähten. Für beide gibt es Fabriken. Die &6CNC Lathe&r braucht zwei Robits und geht damit auch schon. Presser und Pflanzstation brauchen Elite-Schaltkreise und kommen in Stufe 4.",
          ],
          tasks=[task_item("mekmm:cnc_stamper", 1), task_item("ae2:printed_silicon", 16)],
          rewards=[reward_item("ae2:silicon", 16), reward_table("s3_common"), reward_xp(5)],
          deps=["installer"], icon="mekmm:cnc_stamper"),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("steel_core", 10.25, 16.5, "&6Stahlkern",
          subtitle="Der Meilenstein des Stahlwerks.",
          description=[
              "Der &6Stahlkern&r ist der Meilenstein der Technik-Säule in Stufe 3. Er nimmt das Beste der Stufe aus drei Mods und ein Stück Alfheim.",
              "",
              img("kronwerke:textures/item/steel_core.png", 32, 32),
              "",
              "&eRezept an der Werkbank:&r",
              "Oben: &6Schwerer Technikblock&r, &6Fortschrittlicher Steuerschaltkreis&r, &6Schwerer Technikblock&r.",
              "Mitte: &6Technikprozessor&r, &6Stahlgehäuse&r, &6Technikprozessor&r.",
              "Unten: &6Schwerer Technikblock&r, &aElementiumbarren&r, &6Schwerer Technikblock&r.",
              "",
              "Die Schweren Technikblöcke kommen aus Immersive Engineering (auf Kronwerke mit einem Präzisionsgetriebe), die Technikprozessoren aus dem AE2-Inscriber. Das &aElementium&r tauscht ein Botaniker im Elfenportal, frag ihn.",
              "",
              "&eWie viele:&r Der Obelisk will &e8 Stahlkerne&r, jeder zählt so viel wie 400 Stahlbarren.",
          ],
          tasks=[task_item("kronwerke:steel_core", 1)],
          rewards=[reward_table("s3_uncommon"), reward_xp(10)],
          deps=["cnc_stamper"], icon="kronwerke:steel_core", size=1.75, shape="gear"),

    quest("goal", 13.25, 16.5, "&5&lDer Ofen schläft nie",
          subtitle="Füttere den Obelisken.",
          description=[
              "Das Obelisk-Ziel von Stufe 3 heißt &6Der Ofen schläft nie&r. Im Technik-Pfeiler will es &64 000 Stahlbarren&r, &6250 Fortschrittliche Steuerschaltkreise&r und &68 Stahlkerne&r. Im Magie-Pfeiler warten Elementium, Afrit-Essenz und Elfensterne, und beide Pfeiler müssen voll werden.",
              "",
              "&eWas das heißt:&r Eine Dreifach-Straße für Eisen, dahinter eine Stahlstraße mit Angereichertem Kohlenstoff, beide mit Fortschrittlichen Fabriken. Daneben eine Schaltkreislinie aus Silizium, Kupfer und Redstone. Stahl aus dem Hochofen von Immersive Engineering zählt genauso.",
              "",
              "&eKronwerke:&r Stell eine Kiste oder ein Fass direkt an den Obelisken und leite deine Ausgabe hinein. Der Obelisk holt sich alle zwei Sekunden, was er brauchen kann, und schreibt es dir gut. Den Stand zeigt &e/kw goals&r.",
              "",
              "Und denk an die Magier: Sie brauchen deine Verstärkte Legierung für die Elfensterne, du brauchst ihr Elementium für die Stahlkerne.",
          ],
          tasks=[task_item("mekanism:ingot_steel", 256), task_item("mekanism:advanced_control_circuit", 32)],
          rewards=[reward_table("s3_rare"), reward_item("mekanism:advanced_control_circuit", 4), reward_xp(20)],
          deps=["steel_core"], icon="mekanism:ingot_steel", size=2.5, shape="gear"),
]

images = [
    head("title", "Mekanism: Fortgeschritten", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 3: Stahlwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("ores", "Erzverdreifachung", 5, -0.4, colour="magic"),
    head("obsidian", "Diamant und Obsidian", 0.9, 5.2, colour="water"),
    head("advanced", "Fortschrittliche Stufe", 9.6, 5.2, colour="brass"),
    head("power", "Generatoren", 3.4, 11.2, colour="fire"),
    head("mekmm", "MoreMachine", 9.6, 11.2, colour="stone"),
    head("goal", "Das Ziel", 9.6, 14.8, colour="brass"),
]

chapter(C, "Mekanism: Fortgeschritten", "mekanism:purification_chamber", "tech", quests, shape="square",
        order=19, stage=3,
        subtitle=["Stufe 3: Erzverdreifachung, Raffiniertes Obsidian, die fortschrittliche Stufe und die Industrieturbine."],
        images=images)
