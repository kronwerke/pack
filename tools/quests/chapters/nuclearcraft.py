"""NuclearCraft Neoteric (1.3.1-beta1) in stage 4, one machine or part per quest: the
manufactory, ores, graphite, basic plates, the alloy smelter, ferroboron and tough alloy, the
parts (advanced plate, chassis, motor, servo, actuator), isotope separation and LEU-235, then
the fission reactor step by step (pressurizer and casing, decay hastener, assembler and basic
electric circuit, controller, rock crusher and fuel cells, moderators, thermoconducting plate
and heat sinks, port, first start), reprocessing, irradiation, and radiation protection from
Nuclear Radiation. The reactor designer needs an analyzer, which has no recipe in this
version. Recipes and numbers from the NuclearCraft jar (recipe/, recipe/fission_reactor)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp, banner)

C = "nuclearcraft"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Erze und Maschinen -------------------------------------------------------
    quest("welcome", 0, 1.5, "&a&lBau eine Manufactory",
          subtitle="Die Mühle von NuclearCraft.",
          description=[
              "&6Blei&r in die Ecken, &6Redstone&r oben, &6Feuerstein&r links und rechts, ein &6Kolben&r in die Mitte, unten eine &6Coil Copper&r (vier Kupfer, zwei Eisen).",
              "",
              "Sie mahlt Erze, Barren und Kohle zu Staub, mit Strom aus deinem Netz. NuclearCraft öffnet in &6Stufe 4&r ganz. Dieses Kapitel führt bis zum ersten laufenden Spaltreaktor.",
              "",
              "&cAchtung:&r Mit &6Nuclear Radiation&r strahlt Uran, auch im Inventar und in Kisten. Lies den Abschnitt Strahlung, bevor du Stapel davon herumträgst.",
          ],
          tasks=[task_item("nuclearcraft:manufactory", 1)],
          rewards=[reward_item("nuclearcraft:coil_copper", 4), reward_table("s4_common"), reward_xp(10)],
          icon="nuclearcraft:manufactory", size=2.0, shape="hexagon"),

    quest("ores", 2.5, 0.5, "&7Bau Uran, Bor und Lithium ab",
          subtitle="Die Erze für den Reaktor.",
          description=[
              "Die Erze liegen in der Oberwelt zwischen Höhe -60 und 60. &6Uran&r für Brennstoff, &6Bor&r für Ferroboron, &6Lithium&r für die zähe Legierung. &6Thorium&r ist ein zweiter, sanfter Brennstoff.",
              "",
              "Rohes Uran und Lithiumstaub von Mekanism gehen auch. Mahl Rohes Erz in der Manufactory, ein Erz gibt zwei Staub. Blei brauchst du in großen Mengen.",
          ],
          tasks=[task_item("nuclearcraft:raw_uranium", 16), task_item("nuclearcraft:raw_boron", 8),
                 task_item("nuclearcraft:raw_lithium", 8)],
          rewards=[reward_item("mekanism:ingot_lead", 16), reward_xp(5)],
          deps=["welcome"], icon="nuclearcraft:raw_uranium"),

    quest("graphite", 2.5, 2.5, "&8Mahl Kohle zu Graphit",
          subtitle="Zweimal durch die Manufactory.",
          description=[
              "Kohle in der Manufactory gibt Kohlenstaub, Kohlenstaub gibt &6Graphitstaub&r. Im Ofen wird daraus ein &6Graphitbarren&r, neun Barren ein &6Graphitblock&r.",
              "",
              "Graphit steckt in Platten, Hard Carbon und den Moderatoren des Reaktors. Leg einen großen Vorrat an.",
          ],
          tasks=[task_item("nuclearcraft:graphite_dust", 16)],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["welcome"], icon="nuclearcraft:graphite_dust"),

    quest("basics", 5, 2.5, "&8Leg Plate Basic",
          subtitle="Die Grundplatte fast jeder Maschine.",
          description=[
              "Zwei &6Bleibarren&r und zwei &6Graphitstaub&r über Kreuz. Gibt zwei &6Plate Basic&r.",
          ],
          tasks=[task_item("nuclearcraft:plate_basic", 8)],
          rewards=[reward_item("mekanism:ingot_lead", 16), reward_xp(5)],
          deps=["graphite"], icon="nuclearcraft:plate_basic"),

    quest("alloys", 7.5, 2.5, "&6Bau einen Alloy Smelter",
          subtitle="Zwei Staube, eine Legierung.",
          description=[
              "&6Plate Basic&r in die Ecken, &6Ziegel&r links und rechts, &6Redstone&r oben, ein &6Hochofen&r in die Mitte, unten eine &6Coil Copper&r.",
              "",
              "Er schmilzt zwei Staube zu einer Legierung. Stell ihn fest an eine Staublinie, du brauchst ihn für das ganze Kapitel.",
          ],
          tasks=[task_item("nuclearcraft:alloy_smelter", 1)],
          rewards=[reward_item("minecraft:bricks", 16), reward_xp(5)],
          deps=["basics"], icon="nuclearcraft:alloy_smelter"),

    quest("ferroboron", 10, 1.5, "&6Schmilz Ferroboron",
          subtitle="Bor und Stahl.",
          description=[
              "&6Borstaub&r und &6Stahlstaub&r im Alloy Smelter ergeben zwei &6Ferroboronbarren&r. Stahlstaub macht der Zerkleinerer von Mekanism aus Stahl.",
              "",
              "Ferroboron steckt in Servo und Aktuator und ist die Vorstufe der zähen Legierung.",
          ],
          tasks=[task_item("nuclearcraft:ferroboron_ingot", 8)],
          rewards=[reward_item("mekanism:ingot_steel", 8), reward_xp(5)],
          deps=["alloys", "ores"], icon="nuclearcraft:ferroboron_ingot"),

    quest("tough", 12.5, 1.5, "&6Schmilz Tough Alloy",
          subtitle="Das wichtigste Metall des Kapitels.",
          description=[
              "Ferroboron durch die Manufactory zu Staub, dann &6Ferroboronstaub&r und &6Lithiumstaub&r im Alloy Smelter. Gibt zwei &6Tough Alloy&r.",
              "",
              "Sie steckt in Plate Advanced, Chassis, Rüstung, Kühlkörpern und den Reaktoranschlüssen.",
          ],
          tasks=[task_item("nuclearcraft:tough_alloy_ingot", 16)],
          rewards=[reward_item("mekanism:ingot_steel", 16), reward_table("s4_common"), reward_xp(10)],
          deps=["ferroboron"], icon="nuclearcraft:tough_alloy_ingot"),

    # ---- Bauteile -----------------------------------------------------------------
    quest("plate_adv", 0, 6, "&7Bau Plate Advanced",
          subtitle="Die bessere Platte.",
          description=[
              "Oben und unten eine &6Plate Basic&r, in der Mitte &6Tough Alloy, Redstone, Tough Alloy&r. Gibt zwei.",
          ],
          tasks=[task_item("nuclearcraft:plate_advanced", 8)],
          rewards=[reward_item("nuclearcraft:plate_basic", 4), reward_xp(5)],
          deps=["tough"], icon="nuclearcraft:plate_advanced"),

    quest("parts", 2.5, 6, "&7Bau ein Chassis",
          subtitle="Der Rahmen jeder Maschine.",
          description=[
              "&6Blei&r in die Ecken, &6Stahl&r an die Seiten, &6Tough Alloy&r in die Mitte.",
              "",
              "Stahl brauchst du hier reichlich. Deine Stahlstraße aus Stufe 3 hat wieder zu tun.",
          ],
          tasks=[task_item("nuclearcraft:chassis", 2)],
          rewards=[reward_item("mekanism:ingot_steel", 16), reward_xp(5)],
          deps=["plate_adv"], icon="nuclearcraft:chassis"),

    quest("motor", 5, 6, "&7Bau einen Motor",
          subtitle="Dreht in Separator, Assembler und Crusher.",
          description=[
              "Oben und unten &6Stahl, Stahl, Goldnugget&r, in der Mitte &6Coil Copper, Coil Copper, Eisen&r.",
          ],
          tasks=[task_item("nuclearcraft:motor", 2)],
          rewards=[reward_item("nuclearcraft:coil_copper", 4), reward_xp(5)],
          deps=["parts"], icon="nuclearcraft:motor"),

    quest("servo", 7.5, 6, "&7Bau einen Servo",
          subtitle="Für Port, Melter und Chemical Reactor.",
          description=[
              "Oben zwei &6Ferroboron&r links und rechts, in der Mitte &6Redstone, Stahl, Redstone&r, unten &6Stahl, Kupfer, Stahl&r.",
          ],
          tasks=[task_item("nuclearcraft:servo", 2)],
          rewards=[reward_item("nuclearcraft:ferroboron_ingot", 4), reward_xp(5)],
          deps=["motor"], icon="nuclearcraft:servo"),

    quest("actuator", 10, 6, "&7Bau einen Aktuator",
          subtitle="Für Pressurizer, Assembler und Hastener.",
          description=[
              "Oben rechts &6Stahl&r, in der Mitte &6Ferroboron&r und ein &6Kolben&r, unten &6Kupfer&r und &6Ferroboron&r. Die genaue Lage zeigt JEI.",
          ],
          tasks=[task_item("nuclearcraft:actuator", 2)],
          rewards=[reward_item("nuclearcraft:ferroboron_ingot", 4), reward_xp(5)],
          deps=["servo"], icon="nuclearcraft:actuator"),

    quest("isotopes", 12.5, 6, "&aTrenn Uran im Isotope Separator",
          subtitle="Zehn Staub, ein Uran-235.",
          description=[
              "&6Plate Basic&r in die Ecken, &6Motoren&r oben und unten, &6Redstone&r links und rechts, ein &6Chassis&r in die Mitte.",
              "",
              "Zehn Uranstaub ergeben neun &6Uran-238&r und ein &6Uran-235&r. Thoriumstaub wird zu Thorium-232 und Thorium-230.",
          ],
          tasks=[task_item("nuclearcraft:isotope_separator", 1), task_item("nuclearcraft:uranium_235", 2)],
          rewards=[reward_item("nuclearcraft:raw_uranium", 16), reward_xp(10)],
          deps=["actuator"], icon="nuclearcraft:isotope_separator"),

    quest("fuel", 15, 6, "&a&lMisch LEU-235",
          subtitle="Der erste Brennstoff.",
          description=[
              "Ein &6Uran-235&r und acht &6Uran-238&r an der Werkbank. Gibt drei &6LEU-235&r.",
              "",
              "Ein Stück brennt &e4 Minuten&r, macht &e50 Hitze&r und &e240 Strom pro Tick&r. &6HEU-235&r (drei zu sechs) macht viel mehr Hitze, &6TBU&r aus Thorium sehr wenig. Mit Sauerstoff im Fluid Infuser wird daraus Oxid-Brennstoff, mehr Strom, mehr Hitze.",
          ],
          tasks=[task_item("nuclearcraft:fuel_uranium_leu_235", 3)],
          rewards=[reward_item("nuclearcraft:uranium_238", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["isotopes"], icon="nuclearcraft:fuel_uranium_leu_235", size=1.5, shape="hexagon"),

    # ---- Der Spaltreaktor -----------------------------------------------------------
    quest("pressurizer", 0, 10, "&7Bau einen Pressurizer",
          subtitle="Er presst Platten.",
          description=[
              "&6Plate Advanced&r in die Ecken, oben &6Terrakotta&r, &6Aktuatoren&r links und rechts, ein &6Chassis&r in die Mitte, unten ein &6Amboss&r.",
              "",
              "Er presst Barren zu Platten: Blei für die Hülle, Tough Alloy für den Port. Bleiplatten gehen auch mit dem Ingenieurshammer von Immersive Engineering.",
          ],
          tasks=[task_item("nuclearcraft:pressurizer", 1)],
          rewards=[reward_item("mekanism:ingot_lead", 32), reward_xp(10)],
          deps=["actuator"], icon="nuclearcraft:pressurizer"),

    quest("casing", 2.5, 10, "&7Bau Gehäuse und Glas",
          subtitle="Die Hülle des Reaktors.",
          description=[
              "&6Casing:&r Bleiplatten in die Ecken, Plate Advanced an die Seiten, Mitte frei. Gibt vier. &6Glass:&r ein Casing, Glas oben, unten, links und rechts.",
              "",
              "Der Reaktor ist ein Quader. Alle Kanten Casing, die Flächen Casing oder Glas. Der kleinste ist 3 mal 3 mal 3. Für 5 mal 5 mal 5 brauchst du 98 Blöcke Hülle.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_casing", 36), task_item("nuclearcraft:fission_reactor_glass", 16)],
          rewards=[reward_item("mekanism:ingot_lead", 32), reward_xp(10)],
          deps=["pressurizer"], icon="nuclearcraft:fission_reactor_casing"),

    quest("hastener", 5, 9, "&bBau einen Decay Hastener",
          subtitle="Das Herz des Controllers.",
          description=[
              "Oben &6Borbarren, Borblock, Borbarren&r, in der Mitte &6Tough Alloy, Zinn-Silber, Tough Alloy&r, unten &6Borbarren, Aktuator, Borbarren&r.",
              "",
              "&6Zinn-Silber&r macht der Alloy Smelter aus drei Zinnstaub und einem Silberstaub.",
          ],
          tasks=[task_item("nuclearcraft:decay_hastener", 1)],
          rewards=[reward_item("nuclearcraft:raw_boron", 8), reward_xp(10)],
          deps=["casing"], icon="nuclearcraft:decay_hastener"),

    quest("assembler", 5, 11, "&bBau einen Assembler",
          subtitle="Er baut die Schaltkreise.",
          description=[
              "&6Plate Basic&r in die Ecken, oben &6Hard Carbon&r, &6Aktuatoren&r links und rechts, ein &6Chassis&r in die Mitte, unten ein &6Motor&r.",
              "",
              "&6Hard Carbon&r schmilzt der Alloy Smelter aus Graphit- und Diamantstaub.",
          ],
          tasks=[task_item("nuclearcraft:assembler", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(10)],
          deps=["casing"], icon="nuclearcraft:assembler"),

    quest("circuit", 7.5, 11, "&bBau Basic Electric Circuits",
          subtitle="Zwei für den Controller.",
          description=[
              "Im Assembler: eine &6Elektrum-Platte&r, &6Bioplastik&r, &6Energetic Blend&r, &6Redstone&r und eine &6Coil Copper&r.",
              "",
              "&6Bioplastik&r macht die Manufactory aus zwei Zuckerrohr. &6Energetic Blend&r mischt der Assembler aus Glowstone-, Quarz-, Redstone- und Smaragdstaub.",
          ],
          tasks=[task_item("nuclearcraft:basic_electric_circuit", 2)],
          rewards=[reward_item("minecraft:sugar_cane", 32), reward_xp(10)],
          deps=["assembler"], icon="nuclearcraft:basic_electric_circuit"),

    quest("controller", 10, 10, "&b&lBau den Reaktor-Controller",
          subtitle="Ohne Controller kein Reaktor.",
          description=[
              "&6Casing&r in die Ecken, &6Plate Advanced&r oben und unten, zwei &6Basic Electric Circuits&r links und rechts, der &6Decay Hastener&r in die Mitte.",
              "",
              "Er sitzt in der Wand und zeigt Zellen, Moderatoren, Kühlkörper und Hitze. Den &6Fission Reactor Designer&r gibt es nicht: er braucht einen &cAnalyzer&r, und der hat in dieser Version kein Rezept. Plane also im Controller.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_controller", 1)],
          rewards=[reward_item("nuclearcraft:plate_advanced", 4), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["hastener", "circuit"], icon="nuclearcraft:fission_reactor_controller", size=1.5),

    quest("rock_crusher", 0, 13, "&7Bau einen Rock Crusher",
          subtitle="Zirkonium, Beryllium und Arsen aus Gestein.",
          description=[
              "&6Plate Advanced&r in die Ecken, oben ein &6Motor&r, &6Aktuatoren&r links und rechts, ein &6Chassis&r in die Mitte, unten &6Tough Alloy&r.",
              "",
              "Aus vier &6Diorit&r werden zwei Zirkoniumstaub, dazu Fluorit und Carobbiit. Aus &6Andesit&r kommen Beryllium und Arsen.",
          ],
          tasks=[task_item("nuclearcraft:rock_crusher", 1)],
          rewards=[reward_item("minecraft:diorite", 64), reward_xp(10)],
          deps=["parts"], icon="nuclearcraft:rock_crusher"),

    quest("cells", 2.5, 13, "&aBau Brennstoffzellen",
          subtitle="Wo die Spaltung passiert.",
          description=[
              "Vier &6Zirkoniumbarren&r in die Ecken, &6Glas&r an die Seiten, Mitte frei. Gibt eine &6Solid Fuel Cell&r.",
              "",
              "Jede Zelle im Reaktor macht Hitze und Strom. Mehr Zellen heißt mehr von beidem und schnelleren Verbrauch.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_solid_fuel_cell", 2)],
          rewards=[reward_item("minecraft:glass", 16), reward_xp(10)],
          deps=["rock_crusher"], icon="nuclearcraft:fission_reactor_solid_fuel_cell"),

    quest("moderator", 5, 13, "&aSetz Graphitblöcke als Moderator",
          subtitle="Mehr Strom, mehr Hitze.",
          description=[
              "&6Graphitblöcke&r oder &6Berylliumblöcke&r direkt neben einer Zelle sind &6Moderatoren&r.",
              "",
              "Jede Moderatorseite an einer Zelle gibt etwa &e17 Prozent mehr Strom&r und &e33 Prozent mehr Hitze&r. Einer zwischen zwei Zellen zählt für beide.",
          ],
          tasks=[task_item("nuclearcraft:graphite_block", 4)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(5)],
          deps=["cells"], icon="nuclearcraft:graphite_block"),

    quest("thermo", 7.5, 13, "&bPress Thermoconducting-Platten",
          subtitle="Der lange Weg zur Kühlung.",
          description=[
              "&6Extreme-Legierung&r (Tough Alloy und Hard Carbon) und &6Borarsenid&r im Alloy Smelter, dann im Pressurizer zur Platte.",
              "",
              "&6Borarsenid:&r Arsen (Rock Crusher, aus Andesit) und Bor im &6Melter&r schmelzen, im &6Chemical Reactor&r mischen, im &6Ingot Former&r fest werden lassen.",
          ],
          tasks=[task_item("nuclearcraft:thermoconducting_plate", 2)],
          rewards=[reward_item("nuclearcraft:tough_alloy_ingot", 8), reward_xp(10)],
          deps=["rock_crusher", "alloys"], icon="nuclearcraft:thermoconducting_plate"),

    quest("heatsinks", 10, 13, "&bBau Wasser-Kühlkörper",
          subtitle="Ohne Kühlung schmilzt er.",
          description=[
              "&6Empty Heat Sink:&r Tough Alloy in die Ecken, &6Thermoconducting-Platten&r oben und unten, &6Eisengitter, Eimer, Eisengitter&r in der Mitte. Dann mit &e1 000 mB Wasser&r in den &6Fluid Infuser&r.",
              "",
              "Ein &6Water Heat Sink&r kühlt &e60 pro Tick&r, wenn er an eine Zelle oder einen Moderator grenzt. Eine LEU-Zelle ohne Moderator macht 50. Alle Regeln zeigt JEI unter &eHeat Sink Placement&r.",
          ],
          tasks=[task_item("nuclearcraft:empty_heat_sink", 1), task_item("nuclearcraft:water_heat_sink", 4)],
          rewards=[reward_item("nuclearcraft:tough_alloy_ingot", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["thermo"], icon="nuclearcraft:water_heat_sink"),

    quest("port", 12.5, 10, "&7Bau einen Reaktor-Port",
          subtitle="Brennstoff rein, Strom raus.",
          description=[
              "&6Tough-Alloy-Platten&r in die Ecken, &6Plate Advanced&r oben und unten, &6Servos&r links und rechts, ein &6Casing&r in die Mitte.",
              "",
              "Über den Port kommt Brennstoff hinein und verbrauchter heraus. Im Energie-Modus gibt er Strom ab, im Siede-Modus macht der Reaktor Dampf für Turbinen.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_port", 1)],
          rewards=[reward_item("nuclearcraft:servo", 2), reward_xp(10)],
          deps=["controller"], icon="nuclearcraft:fission_reactor_port"),

    quest("reactor", 15, 11.5, "&a&lStarte den ersten Spaltreaktor",
          subtitle="Zellen, Moderatoren, Kühlung, Hülle.",
          description=[
              "Innen eine Zelle in der Mitte, ein oder zwei Graphitblöcke daneben, Wasser-Kühlkörper auf die übrigen Seiten. Außen Hülle, Controller und Port in die Wand. LEU in den Port, Redstone-Signal an Controller oder Port.",
              "",
              "Die Netto-Hitze im Controller muss bei null oder darunter liegen, sonst steigt sie bis zur Kernschmelze.",
              "",
              "&cKernschmelze:&r eine Explosion etwa wie TNT, mitten im Reaktor. Bau ihn nicht unter deine Basis.",
          ],
          tasks=[task_item("nuclearcraft:depleted_fuel_uranium_leu_235", 1)],
          rewards=[reward_item("nuclearcraft:fuel_uranium_leu_235", 6), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["port", "heatsinks", "moderator", "fuel"], icon="nuclearcraft:fission_reactor_controller", size=2.0, shape="gear"),

    quest("reprocess", 17.5, 10.5, "&dBereite verbrauchten Brennstoff auf",
          subtitle="Aus Abfall wird Plutonium.",
          description=[
              "&6Fuel Reprocessor:&r Zinn-Silber in die Ecken, oben &6Glowstonestaub&r, &6Enderperlen&r links und rechts, ein &6Chassis&r in die Mitte, unten eine &6Coil Copper&r.",
              "",
              "Ein verbrauchtes LEU-235 gibt vier Uran-238, je ein &6Plutonium-239&r, Plutonium-242 und Americium-243, dazu Strontium und Cäsium. Das Uran-238 geht zurück in die nächste Mischung.",
              "",
              "&cVorsicht:&r Alles davon strahlt stark. In Kisten weit weg lagern, nicht im Inventar.",
          ],
          tasks=[task_item("nuclearcraft:fuel_reprocessor", 1), task_item("nuclearcraft:plutonium_239", 1)],
          rewards=[reward_item("nuclear_radiation:radaway", 2), reward_xp(10)],
          deps=["reactor"], icon="nuclearcraft:fuel_reprocessor"),

    quest("irradiation", 17.5, 12.5, "&eBestrahl Stoffe im Reaktor",
          subtitle="Der Reaktor als Werkzeug.",
          description=[
              "&6Irradiation Chamber:&r Borplatten in die Ecken, Plate Advanced oben und unten, Servos links und rechts, eine Truhe in die Mitte. Eine &6Bestrahlungslinie&r ist Zelle, Moderator, Kammer in einer Reihe, bis zu sechs pro Kammer.",
              "",
              "Den &6Irradiator&r (mit Magnesiumdiborid-Spulen) setzt du in die Wand. Thoriumstaub wird zu TBP, Bismut zu Polonium. Der Weg zu Polonium-Pellets für Mekanism steht im Kapitel &dMekanism: Elite&r.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_irradiation_chamber", 1), task_item("nuclearcraft:irradiator", 1)],
          rewards=[reward_item("nuclearcraft:graphite_block", 4), reward_xp(10)],
          deps=["reactor"], icon="nuclearcraft:fission_reactor_irradiation_chamber", optional=True),

    # ---- Strahlung und Ziel ---------------------------------------------------------
    quest("geiger", 0, 17, "&eBau Geigerzähler und Dosimeter",
          subtitle="Hören, was du nicht siehst.",
          description=[
              "&6Geigerzähler:&r drei Eisen oben, Redstone, Glasscheibe, Redstone, unten Eisen, Kupfer, Eisen. In der Hand klickt er schneller, je stärker die Strahlung, und zeigt Sv/h. &6Dosimeter:&r Eisen oben, Glasscheiben links und rechts, Komparator, Redstone unten. Im Inventar zeigt ein Balken deine Dosis.",
              "",
              "Ab 1 mSv/h oder 0,5 Sv Gesamtdosis wird dir übel. Ab 10 Sv/h oder 5 Sv nimmst du Schaden. Ab 100 Sv/h stirbst du schnell.",
          ],
          tasks=[task_item("nuclear_radiation:geiger_counter", 1), task_item("nuclear_radiation:dosimeter", 1)],
          rewards=[reward_item("nuclear_radiation:iodine_pill", 4), reward_xp(5)],
          deps=["welcome"], icon="nuclear_radiation:geiger_counter"),

    quest("hazmat", 2.5, 17, "&eZieh den Schutzanzug an",
          subtitle="Vier Teile, vier Strahlenarten.",
          description=[
              "Jedes Teil ist ein &6Lederteil&r mit &6Phantommembranen&r drumherum. Der Helm hält radioaktive Gase aus der Lunge. Mehr Teile schützen mehr.",
              "",
              "Blöcke zwischen dir und der Quelle schirmen ab, dichte wie Blei am besten. An der Schmiede verstärkst du jede Rüstung mit einer &6Strahlenschutz-Platte&r pro Teil.",
          ],
          tasks=[task_item("nuclear_radiation:hazmat_helmet", 1), task_item("nuclear_radiation:hazmat_chestplate", 1),
                 task_item("nuclear_radiation:hazmat_leggings", 1), task_item("nuclear_radiation:hazmat_boots", 1)],
          rewards=[reward_item("nuclear_radiation:radaway", 2), reward_xp(10)],
          deps=["geiger"], icon="nuclear_radiation:hazmat_helmet"),

    quest("medicine", 5, 17, "&eLeg Medizin bereit",
          subtitle="Gegen die Dosis, die du schon hast.",
          description=[
              "&6Jodtabletten&r (getrockneter Seetang, Glowstone, Zucker) nehmen 0,5 Sv von deiner Dosis. &6RadAway&r (Glasflasche, Ghast-Träne, Redstone, Glowstone) nimmt 1 Sv und schützt fünf Minuten.",
          ],
          tasks=[task_item("nuclear_radiation:iodine_pill", 4), task_item("nuclear_radiation:radaway", 2)],
          rewards=[reward_item("nuclear_radiation:radaway", 2), reward_item("nuclear_radiation:iodine_pill", 4), reward_xp(10)],
          deps=["hazmat"], icon="nuclear_radiation:radaway"),

    quest("goal", 8, 17, "&a&lHalt den Reaktor im Dauerbetrieb",
          subtitle="Ein Reaktor, der nicht schmilzt.",
          description=[
              "Uranstraße, Kühlung mit Reserve, eine Kiste für den verbrauchten Brennstoff weit weg von dir. Jede Änderung erst am Controller prüfen, dann gehen.",
              "",
              "Danach: mehr Zellen, bessere Kühlkörper, HEU-235 oder Oxid-Brennstoff.",
              "",
              "&eKronwerke:&r Stufe 4 frisst Strom: Fusion zünden, Draconic-Kerne füllen, und in Stufe 5 läuft das SPS für die Antimaterie des Obelisken tagelang. Ein Spaltreaktor ist eine gute Grundlast.",
          ],
          tasks=[task_item("nuclearcraft:depleted_fuel_uranium_leu_235", 12), task_item("nuclearcraft:fission_reactor_solid_fuel_cell", 4)],
          rewards=[reward_table("s4_rare"), reward_item("nuclearcraft:fuel_uranium_heu_235", 3), reward_xp(25)],
          deps=["reactor", "medicine"], icon="nuclearcraft:fuel_uranium_heu_235", size=2.5, shape="gear"),

    # ---- neue Quests: Erze und Maschinen ---------------------------------------
    quest("upgrades", 15, 0.5, "&9Rüste Maschinen mit Upgrades auf",
          subtitle="Schneller, oder sparsamer, oder beides.",
          description=[
              "&6Speed Upgrade:&r vier Lapisstaub und vier Redstonestaub um eine &6Schwere Wägeplatte&r. &6Energy Upgrade:&r vier Obsidianstaub und vier Quarzstaub um eine &6Leichte Wägeplatte&r. Die Staube mahlt die Manufactory.",
              "",
              "Die meisten Maschinen haben seitlich zwei Upgrade-Plätze: der erste nimmt Energy Upgrades, der zweite Speed Upgrades, bis 64 pro Platz. Jedes Speed Upgrade macht die Maschine schneller, der Stromverbrauch wächst aber im Quadrat.",
              "",
              "Energy Upgrades ziehen diesen Mehrverbrauch wieder ab und vergrößern den Puffer. Misch beide, statt nur auf Tempo zu gehen.",
          ],
          tasks=[task_item("nuclearcraft:speed_upgrade", 4), task_item("nuclearcraft:energy_upgrade", 4)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_item("minecraft:redstone", 16), reward_xp(10)],
          deps=["graphite"], icon="nuclearcraft:speed_upgrade"),

    quest("solar", 15, 2.5, "&eStell Solarpanels auf",
          subtitle="28 FE pro Tick, einfach so.",
          description=[
              "&6Solar Panel Basic:&r Lapis, Glasscheibe, Lapis oben, &6Schwere Wägeplatte&r, Lapis, Schwere Wägeplatte in der Mitte, &6Coil Copper&r, &6Tageslichtsensor&r, Coil Copper unten.",
              "",
              "Es macht &e28 FE/t&r, solange es Tag ist und der Himmel frei. Drei davon mit vier &6Plate Advanced&r, Quarzstaub und einer Coil Copper ergeben ein &6Solar Panel Advanced&r mit &e112 FE/t&r.",
              "",
              "Die Stufen darüber, DU und Elite, schaffen 448 und 1 792 FE/t.",
          ],
          tasks=[task_item("nuclearcraft:solar_panel_basic", 2)],
          rewards=[reward_item("minecraft:daylight_detector", 2), reward_xp(10)],
          deps=["welcome"], icon="nuclearcraft:solar_panel_basic"),

    quest("nuclear_furnace", 10, 3.2, "&cBau einen Nuclear Furnace",
          subtitle="Ein Ofen, der Uran verbrennt.",
          description=[
              "&6Plate Basic&r in die Ecken, &6Eisenbarren&r an die Seiten, ein &6Ofen&r in die Mitte ergeben den &6Nuclear Furnace&r.",
              "",
              "Er schmilzt schnell und verbrennt &6Uranbarren&r als Brennstoff statt Kohle. Laut NuclearCraft für einen Ofen erstaunlich sicher.",
          ],
          tasks=[task_item("nuclearcraft:nuclear_furnace", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_xp(5)],
          deps=["basics", "ores"], icon="nuclearcraft:nuclear_furnace", optional=True),

    # ---- neue Quests: Bauteile -------------------------------------------------
    quest("tough_armor", 17.5, 6, "&7Schmied eine Tough-Rüstung",
          subtitle="Vier Teile aus Tough Alloy.",
          description=[
              "&6Tough Alloy&r in der Form der Eisenrüstung ergibt &6Tough Helmet&r, &6Tough Chestplate&r, &6Tough Leggings&r und &6Tough Boots&r, zusammen &e24 Barren&r.",
              "",
              "Jedes Teil nimmt an der Schmiede eine Strahlenschutz-Platte von Nuclear Radiation auf, siehe Abschnitt Strahlung.",
          ],
          tasks=[task_item("nuclearcraft:tough_helmet", 1), task_item("nuclearcraft:tough_chestplate", 1),
                 task_item("nuclearcraft:tough_leggings", 1), task_item("nuclearcraft:tough_boots", 1)],
          rewards=[reward_item("nuclearcraft:tough_alloy_ingot", 8), reward_xp(10)],
          deps=["tough"], icon="nuclearcraft:tough_chestplate", optional=True),

    # ---- neue Quests: Der Spaltreaktor -----------------------------------------
    quest("redstone_sink", 12.5, 14.5, "&bBau einen Redstone-Kühlkörper",
          subtitle="Der nächste Kühlkörper nach Wasser.",
          description=[
              "Ein &6Empty Heat Sink&r mit vier &6Redstonestaub&r im Kreuz ergibt einen &6Redstone Heat Sink&r.",
              "",
              "Jede Sorte Kühlkörper hat ihre eigene Kühlrate und eigene Regeln, wo sie sitzen darf. Der Tooltip zeigt die Rate in H/t, JEI unter &eHeat Sink Placement&r die Regel. Mit mehreren Sorten kühlst du dichtere Reaktoren.",
          ],
          tasks=[task_item("nuclearcraft:redstone_heat_sink", 4)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_xp(10)],
          deps=["heatsinks"], icon="nuclearcraft:redstone_heat_sink"),

    quest("turbine", 15, 9.5, "&bBau eine Steam Turbine",
          subtitle="Dampf aus dem Reaktor wird Strom.",
          description=[
              "&6Plate Advanced&r in die Ecken, ein &6Kessel&r oben, &6Coil Copper&r links und rechts, ein &6Chassis&r in die Mitte, ein &6Ofen&r unten ergeben die &6Steam Turbine&r.",
              "",
              "Stellst du den Reaktor-Port auf den Siede-Modus, macht der Reaktor Dampf statt Strom. Die Turbine wandelt diesen Dampf in Strom um. Für große Anlagen gibt es die Turbine auch als Multiblock.",
          ],
          tasks=[task_item("nuclearcraft:steam_turbine", 1)],
          rewards=[reward_item("nuclearcraft:coil_copper", 4), reward_xp(10)],
          deps=["port"], icon="nuclearcraft:steam_turbine", optional=True),

    quest("heu", 20, 11.5, "&cMisch HEU-235",
          subtitle="Mehr Uran-235, mehr Hitze.",
          description=[
              "Drei &6Uran-235&r und sechs &6Uran-238&r an der Werkbank ergeben drei &6HEU-235&r. Thorium-Brennstoff &6TBU&r: ein Thorium-230 und acht Thorium-232 geben drei.",
              "",
              "HEU macht viel mehr Hitze als LEU. Erst wenn deine Kühlung mit Reserve läuft, lohnt sich der Wechsel. Im Controller siehst du sofort, ob die Netto-Hitze noch bei null bleibt.",
          ],
          tasks=[task_item("nuclearcraft:fuel_uranium_heu_235", 3)],
          rewards=[reward_item("nuclearcraft:uranium_238", 8), reward_xp(10)],
          deps=["reactor"], icon="nuclearcraft:fuel_uranium_heu_235"),

    # ---- neue Quests: Strahlung ------------------------------------------------
    quest("shielding", 2.5, 19, "&eVerstärk deine Rüstung gegen Strahlung",
          subtitle="Eine Platte pro Teil, an der Schmiede.",
          description=[
              "&6Light Radiation Shielding:&r Kupfer, Leder, Kupfer oben, Eisennugget, Tonklumpen, Eisennugget in der Mitte, Kupfer, Leder, Kupfer unten, gibt vier. &6Medium:&r Eisen, Lapis, Eisen um einen Goldblock, gibt zwei.",
              "",
              "Am &6Schmiedetisch&r: Rüstungsteil in den Basisplatz, Platte dazu. Das geht mit jeder Rüstung. Leicht gibt &e2 Prozent&r Schutz, Mittel 4, Schwer 7, Dicht 12. Jedes Teil nimmt eine Platte.",
          ],
          tasks=[task_item("nuclear_radiation:rad_shielding_light", 4), task_item("nuclear_radiation:rad_shielding_medium", 2)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(10)],
          deps=["hazmat"], icon="nuclear_radiation:rad_shielding_light"),

    quest("prussian", 5, 19, "&eMisch Preußischblau und Schutztrank",
          subtitle="Vorbeugen statt heilen.",
          description=[
              "&6Preußischblau:&r ein Lapislazuli und zwei Eisennuggets. Es nimmt sofort &e1 Sv&r Dosis und spült zwei Minuten lang Cäsium aus dem Körper.",
              "",
              "&6Rad-Protection Potion:&r Glasflasche, Jodtablette und Preußischblau. Kein Abzug, aber fünf Minuten lang bis zu &e95 Prozent&r weniger neue Dosis. Trink ihn, bevor du an den Reaktor gehst.",
          ],
          tasks=[task_item("nuclear_radiation:prussian_blue", 4), task_item("nuclear_radiation:rad_protection_potion", 2)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(10)],
          deps=["medicine"], icon="nuclear_radiation:prussian_blue"),
]

images = [
    head("title", "NuclearCraft", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("machines", "Erze und Maschinen", 5, -0.6, colour="nature"),
    head("parts", "Bauteile", 3.5, 4.4, colour="brass"),
    head("reactor", "Der Spaltreaktor", 0, 7.7, colour="fire"),
    head("radiation", "Strahlung", 0, 15.2, colour="brass"),
]

chapter(C, "NuclearCraft", "nuclearcraft:fission_reactor_controller", "tech", quests, shape="square",
        order=35, stage=4,
        subtitle=["Stufe 4: Uran, die Maschinen von NuclearCraft, der Spaltreaktor Schritt für Schritt und Schutz vor Strahlung."],
        images=images)
