"""NuclearCraft Neoteric (1.3.1-beta1) in stage 4: ores, the manufactory and the alloy smelter,
the component chain (plates, chassis, motor, servo, actuator), isotope separation and uranium
fuel, the fission reactor (casing, controller, fuel cells, moderators, heat sinks, ports),
fuel reprocessing, irradiation, and radiation protection from Nuclear Radiation.
The whole mod opens in stage 4. The reactor designer is left out: its analyzer has no recipe."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp, banner)

C = "nuclearcraft"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Erze und Maschinen -------------------------------------------------------
    quest("welcome", 0, 1.5, "&a&lNuclearCraft",
          subtitle="Atome spalten, mit Plan.",
          description=[
              "&aNuclearCraft&r bringt Uran, Thorium und den &6Spaltreaktor&r. Der Weg dahin ist lang: Erze, dann eine Reihe Maschinen, dann Legierungen und Bauteile, und erst dann der Reaktor. Dafür liefert ein guter Reaktor Strom ohne Pause.",
              "",
              "&eWas in Stufe 4 offen ist:&r das ganze Mod. Dieses Kapitel führt dich bis zum ersten laufenden Spaltreaktor und zur Wiederaufbereitung. Turbinen, Fusion und Teilchenbeschleuniger von NuclearCraft kannst du danach auf eigene Faust angehen.",
              "",
              "&eErster Schritt:&r die &6Manufactory&r. Blei in die Ecken, Redstone oben, Feuerstein links und rechts, ein Kolben in die Mitte, unten eine &6Coil Copper&r (vier Kupfer und zwei Eisen, siehe JEI). Die Manufactory mahlt Erze, Barren und Kohle zu Staub, mit Strom von deinem Netz.",
              "",
              "&cAchtung:&r Mit diesem Mod kommt echte &cStrahlung&r ins Spiel, über das Mod &6Nuclear Radiation&r. Uran und alles, was daraus wird, strahlt, auch in deinem Inventar und in Kisten. Lies den Abschnitt Strahlung, bevor du den ersten Stapel Uran mit dir herumträgst.",
          ],
          tasks=[task_item("nuclearcraft:manufactory", 1)],
          rewards=[reward_item("nuclearcraft:coil_copper", 4), reward_table("s4_common"), reward_xp(10)],
          icon="nuclearcraft:fission_reactor_controller", size=2.0, shape="hexagon"),

    quest("ores", 2.75, 0, "&7Erze für den Reaktor",
          subtitle="Uran, Thorium, Bor, Lithium.",
          description=[
              "NuclearCraft verteilt seine Erze in der Oberwelt zwischen Y -60 und Y 60. Für dieses Kapitel brauchst du vor allem:",
              "",
              "&6Uran&r für den Brennstoff. Rohes Uran von Mekanism geht genauso, die Manufactory nimmt beide.",
              "&6Bor&r für Ferroboron und Kontrollteile.",
              "&6Lithium&r für die zähe Legierung. Lithiumstaub von Mekanism geht auch.",
              "&6Thorium&r für einen zweiten, sanften Brennstoff.",
              "",
              "Dazu &6Blei&r in großen Mengen, für Platten und Gehäuse. Zinn, Silber, Magnesium und Kobalt liegen ebenfalls herum und werden später gebraucht.",
              "",
              "&eTipp:&r Die Manufactory macht aus einem Rohen Erz zwei Staub. Mahl Bor, Lithium und Uran also, statt sie zu schmelzen.",
          ],
          tasks=[task_item("nuclearcraft:raw_uranium", 16), task_item("nuclearcraft:raw_boron", 8),
                 task_item("nuclearcraft:raw_lithium", 8)],
          rewards=[reward_item("mekanism:ingot_lead", 16), reward_xp(5)],
          deps=["welcome"], icon="nuclearcraft:raw_uranium"),

    quest("geiger", 2.75, 3, "&eGeigerzähler und Dosimeter",
          subtitle="Hören, was du nicht siehst.",
          description=[
              "&6Geigerzähler:&r drei Eisen oben, Redstone, Glasscheibe, Redstone in der Mitte, unten Eisen, Kupfer, Eisen. Halt ihn in der Haupt- oder Nebenhand. Er klickt schneller, je stärker die Strahlung ist, und zeigt die Dosisleistung in Sv/h an.",
              "",
              "&6Dosimeter:&r Eisen oben, Glasscheiben links und rechts, ein Komparator in der Mitte, Redstone unten. Es reicht, wenn es irgendwo im Inventar liegt. Unten auf dem Bildschirm zeigt ein Balken deine gesamte Dosis.",
              "",
              "&eWas die Zahlen heißen:&r Ab 1 mSv/h oder 0,5 Sv Gesamtdosis wird dir schwach und übel. Ab 10 Sv/h oder 5 Sv Gesamtdosis nimmst du Schaden. Ab 100 Sv/h stirbst du schnell.",
          ],
          tasks=[task_item("nuclear_radiation:geiger_counter", 1), task_item("nuclear_radiation:dosimeter", 1)],
          rewards=[reward_item("nuclear_radiation:iodine_pill", 4), reward_xp(5)],
          deps=["welcome"], icon="nuclear_radiation:geiger_counter"),

    quest("basics", 5.25, 0, "&8Graphit und Grundplatten",
          subtitle="Kohle wird zu Graphit.",
          description=[
              "Fast jede Maschine von NuclearCraft steckt in &6Plate Basic&r. &eRezept:&r zwei Bleibarren und zwei &6Graphitstaub&r über Kreuz, das gibt zwei Platten.",
              "",
              "&eGraphit:&r Kohle in der Manufactory gibt Kohlenstaub, Kohlenstaub in der Manufactory gibt Graphitstaub. Im Ofen wird Graphitstaub zum &6Graphitbarren&r, und neun Barren ergeben einen &6Graphitblock&r. Den brauchst du später als Moderator im Reaktor.",
              "",
              "Leg dir gleich einen größeren Vorrat an Graphit an, er steckt in Platten, Hard Carbon und Moderatoren.",
          ],
          tasks=[task_item("nuclearcraft:graphite_dust", 16), task_item("nuclearcraft:plate_basic", 8)],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["ores"], icon="nuclearcraft:plate_basic"),

    quest("alloys", 7.75, 0, "&6Alloy Smelter und Tough Alloy",
          subtitle="Zwei Staube, zwei Barren.",
          description=[
              "Der &6Alloy Smelter&r: Plate Basic in die Ecken, Ziegel links und rechts, Redstone oben, ein Hochofen in der Mitte, unten eine Coil Copper. Er schmilzt zwei Staube zu einer Legierung.",
              "",
              "&6Ferroboron:&r Borstaub und Stahlstaub ergeben zwei Barren. Stahlstaub macht der Zerkleinerer von Mekanism aus Stahl.",
              "&6Tough Alloy:&r Ferroboronstaub (Ferroboron durch die Manufactory) und Lithiumstaub ergeben zwei Barren.",
              "",
              "Tough Alloy ist das wichtigste Metall dieses Kapitels: in Plate Advanced, Chassis, Rüstung, Kühlkörpern und den Reaktoranschlüssen. Stell den Alloy Smelter fest an eine Staublinie.",
          ],
          tasks=[task_item("nuclearcraft:alloy_smelter", 1), task_item("nuclearcraft:ferroboron_ingot", 8),
                 task_item("nuclearcraft:tough_alloy_ingot", 16)],
          rewards=[reward_item("mekanism:ingot_steel", 16), reward_table("s4_common"), reward_xp(10)],
          deps=["basics"], icon="nuclearcraft:alloy_smelter"),

    quest("parts", 10.25, 0, "&7Bauteile",
          subtitle="Chassis, Motor, Servo, Aktuator.",
          description=[
              "Aus diesen Teilen baust du alle weiteren Maschinen. Die genauen Muster zeigt JEI:",
              "",
              "&6Plate Advanced:&r zwei Plate Basic, zwei Tough Alloy und ein Redstone, das gibt zwei.",
              "&6Chassis:&r Blei in die Ecken, Stahl an die Seiten, Tough Alloy in die Mitte.",
              "&6Motor:&r Stahl, zwei Coil Copper, Eisen und Goldnuggets.",
              "&6Servo:&r Stahl, Redstone, Kupfer und zwei Ferroboron.",
              "&6Actuator:&r Stahl, ein Kolben, Kupfer und zwei Ferroboron.",
              "",
              "Stahl brauchst du hier reichlich. Deine Stahlstraße aus Stufe 3 hat also wieder zu tun.",
          ],
          tasks=[task_item("nuclearcraft:plate_advanced", 8), task_item("nuclearcraft:chassis", 2),
                 task_item("nuclearcraft:motor", 2), task_item("nuclearcraft:servo", 2),
                 task_item("nuclearcraft:actuator", 2)],
          rewards=[reward_item("mekanism:ingot_steel", 32), reward_xp(10)],
          deps=["alloys"], icon="nuclearcraft:chassis"),

    quest("isotopes", 10.25, 3, "&aIsotope Separator",
          subtitle="Zehn Staub, ein Uran-235.",
          description=[
              "Natürliches Uran ist fast nur &6Uran-238&r. Spaltbar ist das seltene &6Uran-235&r. Der &6Isotope Separator&r trennt die beiden. &eRezept:&r Plate Basic in die Ecken, Motoren oben und unten, Redstone links und rechts, ein Chassis in die Mitte.",
              "",
              "&eWas herauskommt:&r Zehn Uranstaub ergeben neun Uran-238 und ein Uran-235. Thoriumstaub wird genauso zu Thorium-232 und Thorium-230.",
              "",
              "Uranstaub macht die Manufactory, aus jedem Rohen Uran zwei Staub.",
          ],
          tasks=[task_item("nuclearcraft:isotope_separator", 1), task_item("nuclearcraft:uranium_235", 2)],
          rewards=[reward_item("nuclearcraft:raw_uranium", 16), reward_xp(10)],
          deps=["parts"], icon="nuclearcraft:isotope_separator"),

    quest("fuel", 12.75, 3, "&a&lLEU-235",
          subtitle="Der erste Brennstoff.",
          description=[
              "Brennstoff mischst du an der Werkbank. Jede Mischung aus neun Isotopen gibt &edrei&r Brennstoffe:",
              "",
              "&6LEU-235&r (schwach angereichert): ein Uran-235 und acht Uran-238. Wenig Hitze, leicht zu kühlen, der richtige Brennstoff für den ersten Reaktor.",
              "&6HEU-235&r (hoch angereichert): drei Uran-235 und sechs Uran-238. Viel mehr Strom, aber auch sechsmal so viel Hitze.",
              "&6TBU&r: ein Thorium-230 und acht Thorium-232. Sehr wenig Hitze, brennt dafür dreimal so lange.",
              "",
              "&eVarianten:&r Mit Sauerstoff im Fluid Infuser wird daraus Oxid-Brennstoff (OX). Der gibt mehr Strom und mehr Hitze. Für den Anfang reicht der normale.",
          ],
          tasks=[task_item("nuclearcraft:fuel_uranium_leu_235", 3)],
          rewards=[reward_item("nuclearcraft:uranium_238", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["isotopes"], icon="nuclearcraft:fuel_uranium_leu_235", size=1.5, shape="hexagon"),

    # ---- Der Spaltreaktor -----------------------------------------------------------
    quest("casing", 0, 7.5, "&7Gehäuse und Glas",
          subtitle="Die Hülle des Reaktors.",
          description=[
              "Für die Hülle brauchst du &6Platten&r aus Blei und Tough Alloy. Die presst der &6Pressurizer&r (Plate Advanced, Aktuatoren, Chassis, ein Amboss und Terrakotta). Bleiplatten gehen auch mit dem Ingenieurshammer von Immersive Engineering.",
              "",
              "&6Fission Reactor Casing:&r Bleiplatten in die Ecken, Plate Advanced an die Seiten, die Mitte bleibt frei. Das gibt vier.",
              "&6Fission Reactor Glass:&r ein Casing in der Mitte, Glas oben, unten, links und rechts.",
              "",
              "&eWie viel:&r Ein Reaktor ist ein Quader. Alle Kanten müssen Casing sein, die Flächen dürfen Casing oder Glas sein. Der kleinste ist 3 mal 3 mal 3 mit einem Block innen. Für 5 mal 5 mal 5 mit Platz für ein paar Zellen brauchst du 98 Blöcke Hülle.",
          ],
          tasks=[task_item("nuclearcraft:pressurizer", 1), task_item("nuclearcraft:fission_reactor_casing", 36),
                 task_item("nuclearcraft:fission_reactor_glass", 16)],
          rewards=[reward_item("mekanism:ingot_lead", 32), reward_xp(10)],
          deps=["parts"], icon="nuclearcraft:fission_reactor_casing"),

    quest("controller", 2.75, 6.5, "&b&lReaktor-Controller",
          subtitle="Ohne Controller kein Reaktor.",
          description=[
              "&eRezept:&r Casing in die Ecken, Plate Advanced oben und unten, zwei &6Basic Electric Circuits&r links und rechts, ein &6Decay Hastener&r in der Mitte.",
              "",
              "&6Decay Hastener:&r Borbarren und ein Borblock oben, Tough Alloy links und rechts, ein Zinn-Silber-Barren in der Mitte, Borbarren und ein Aktuator unten. Zinn-Silber macht der Alloy Smelter aus drei Zinnstaub und einem Silberstaub.",
              "",
              "&6Basic Electric Circuit:&r Den baut der &6Assembler&r (Plate Basic, Hard Carbon, Aktuator, Chassis, Motor) aus einer Elektrum-Platte, Bioplastik, Energetic Blend, Redstone und einer Coil Copper. Bioplastik macht die Manufactory aus zwei Zuckerrohr. Energetic Blend mischt der Assembler aus Glowstone-, Quarz-, Redstone- und Smaragdstaub.",
          ],
          tasks=[task_item("nuclearcraft:assembler", 1), task_item("nuclearcraft:basic_electric_circuit", 2),
                 task_item("nuclearcraft:fission_reactor_controller", 1)],
          rewards=[reward_item("minecraft:sugar_cane", 32), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["casing"], icon="nuclearcraft:fission_reactor_controller", size=1.5),

    quest("cells", 2.75, 8.5, "&aBrennstoffzellen und Moderatoren",
          subtitle="Wo die Spaltung passiert.",
          description=[
              "&6Fission Reactor Solid Fuel Cell:&r vier Zirkoniumbarren in die Ecken, Glas an die Seiten, die Mitte frei. &6Zirkonium&r bekommst du aus Diorit: Der &6Rock Crusher&r macht aus vier Diorit zwei Zirkoniumstaub, dazu Fluorit und Carobbiit.",
              "",
              "Jede Zelle im Reaktor erzeugt Hitze und Strom. Mehr Zellen heißt mehr von beidem, aber auch schnellerer Verbrauch.",
              "",
              "&6Moderatoren&r sind &6Graphitblöcke&r oder &6Berylliumblöcke&r direkt neben einer Zelle. Jede Seite eines Moderators an einer Zelle gibt etwa 17 Prozent mehr Strom und 33 Prozent mehr Hitze. Ein Moderator zwischen zwei Zellen zählt für beide. Beryllium kommt ebenfalls aus dem Rock Crusher, aus Andesit.",
          ],
          tasks=[task_item("nuclearcraft:rock_crusher", 1), task_item("nuclearcraft:fission_reactor_solid_fuel_cell", 2),
                 task_item("nuclearcraft:graphite_block", 4)],
          rewards=[reward_item("minecraft:diorite", 64), reward_xp(10)],
          deps=["casing"], icon="nuclearcraft:fission_reactor_solid_fuel_cell"),

    quest("heatsinks", 5.25, 8.5, "&bKühlkörper",
          subtitle="Ohne Kühlung schmilzt er.",
          description=[
              "Ein Reaktor ohne &6Kühlkörper&r (Heat Sinks) wird heißer und heißer, bis er schmilzt und explodiert. Jeder Kühlkörper nimmt pro Tick eine feste Menge Hitze weg, aber nur, wenn er nach seiner &eRegel&r steht.",
              "",
              "&6Water Heat Sink:&r kühlt 60 pro Tick und muss an mindestens eine Brennstoffzelle oder einen Moderator grenzen. Der einfachste für den Anfang. Eine Zelle mit LEU-235 macht 50 Hitze pro Tick, ohne Moderator.",
              "",
              "&eSo baust du ihn:&r Ein &6Empty Heat Sink&r (Tough Alloy, Eisengitter, ein Eimer und zwei Thermoconducting-Platten) kommt mit 1 000 mB Wasser in den &6Fluid Infuser&r.",
              "",
              "&eDie Thermoconducting-Platte&r ist der lange Teil: Extreme-Legierung (Tough Alloy und Hard Carbon im Alloy Smelter, Hard Carbon aus Graphit- und Diamantstaub) und Borarsenid, im Alloy Smelter zusammen, dann gepresst. Borarsenid kommt aus Arsen (Rock Crusher, aus Andesit) und Bor: beide im &6Melter&r schmelzen, im &6Chemical Reactor&r mischen, im &6Ingot Former&r fest werden lassen.",
              "",
              "Alle anderen Kühlkörper und ihre Regeln zeigt JEI unter &eHeat Sink Placement&r.",
          ],
          tasks=[task_item("nuclearcraft:empty_heat_sink", 1), task_item("nuclearcraft:water_heat_sink", 4)],
          rewards=[reward_item("nuclearcraft:tough_alloy_ingot", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["cells"], icon="nuclearcraft:water_heat_sink"),

    quest("reactor", 7.75, 7.5, "&a&lDer erste Spaltreaktor",
          subtitle="Zellen, Moderatoren, Kühlung, Hülle.",
          description=[
              "&eAufbau:&r Innen stellst du Zellen, Moderatoren und Kühlkörper frei auf, eine feste Form gibt es nicht. Außen kommt die Hülle aus Casing und Glas. Den &6Controller&r setzt du irgendwo in die Wand, dazu mindestens einen &6Fission Reactor Port&r (Tough-Alloy-Platten, Servos, Plate Advanced und ein Casing).",
              "",
              "&eEin guter Anfang:&r eine Zelle in der Mitte, ein oder zwei Graphitblöcke daneben, Wasser-Kühlkörper auf die übrigen Seiten. Im Fenster des Controllers siehst du Zellen, Moderatoren, Kühlkörper und die Hitze. Die Netto-Hitze muss bei null oder darunter liegen, sonst steigt sie bis zur Kernschmelze.",
              "",
              "&eStarten:&r Brennstoff kommt über den Port hinein, verbrauchter Brennstoff kommt dort wieder heraus. Gezündet wird mit einem Redstone-Signal am Controller oder am Port (dort den Redstone-Modus wählen).",
              "",
              "&eStrom oder Dampf:&r Im Energie-Modus gibt der Reaktor direkt Strom über den Port ab. Im Siede-Modus macht er aus Wasser Dampf für Turbinen.",
              "",
              "&cKernschmelze:&r Eine Explosion etwa so stark wie TNT, mitten in deinem teuren Reaktor. Bau ihn nicht unter deine Basis.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_port", 1), task_item("nuclearcraft:depleted_fuel_uranium_leu_235", 1)],
          rewards=[reward_item("nuclearcraft:fuel_uranium_leu_235", 6), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["controller", "heatsinks", "fuel"], icon="nuclearcraft:fission_reactor_port", size=2.0, shape="gear"),

    quest("reprocess", 10.25, 6.5, "&dWiederaufbereitung",
          subtitle="Aus Abfall wird Plutonium.",
          description=[
              "Verbrauchter Brennstoff ist kein Müll. Der &6Fuel Reprocessor&r (Zinn-Silber, Glowstone, Enderperlen, ein Chassis, eine Coil Copper) zerlegt ihn.",
              "",
              "&eAus einem verbrauchten LEU-235:&r vier Uran-238, je ein &6Plutonium-239&r, Plutonium-242 und Americium-243, dazu Strontium-90- und Cäsium-137-Staub.",
              "",
              "Aus Plutonium mischst du neue Brennstoffe wie &6LEP-239&r, und so weiter durch die schweren Elemente. Das Uran-238 geht zurück in deine nächste LEU-Mischung.",
              "",
              "&cVorsicht:&r Verbrauchter Brennstoff und alles, was der Reprocessor ausspuckt, strahlt stark. Lager es weit weg in Kisten, nicht im Inventar.",
          ],
          tasks=[task_item("nuclearcraft:fuel_reprocessor", 1), task_item("nuclearcraft:plutonium_239", 1)],
          rewards=[reward_item("nuclear_radiation:radaway", 2), reward_xp(10)],
          deps=["reactor"], icon="nuclearcraft:fuel_reprocessor"),

    quest("irradiation", 10.25, 8.5, "&eBestrahlung",
          subtitle="Der Reaktor als Werkzeug.",
          description=[
              "Ein laufender Reaktor kann nebenbei Stoffe umwandeln. Eine &6Bestrahlungslinie&r sind drei Blöcke in einer Reihe: Brennstoffzelle, Moderator, &6Fission Reactor Irradiation Chamber&r. Eine Kammer nimmt bis zu sechs Linien, jede macht sie schneller. Den &6Irradiator&r setzt du in die Wand, er nimmt die Gegenstände auf.",
              "",
              "&eWas er macht:&r Thoriumstaub wird zu TBP, Lithium und Bor werden bestrahlt, Siliziumwafer werden dotiert, geschmolzenes Uran-238 wird zu Uran-235. Die ganze Liste zeigt JEI.",
              "",
              "Die &6Pile-Driver Irradiation Chamber&r arbeitet fünfmal so schnell und passt an dieselbe Stelle.",
          ],
          tasks=[task_item("nuclearcraft:fission_reactor_irradiation_chamber", 1), task_item("nuclearcraft:irradiator", 1)],
          rewards=[reward_item("nuclearcraft:graphite_block", 4), reward_xp(10)],
          deps=["reactor"], icon="nuclearcraft:fission_reactor_irradiation_chamber", optional=True),

    # ---- Strahlung und Ziel ---------------------------------------------------------
    quest("hazmat", 0, 12.5, "&eSchutzanzug und Medizin",
          subtitle="Die Dosis macht das Gift.",
          description=[
              "Der &6Schutzanzug&r von Nuclear Radiation schützt gegen alle vier Arten von Strahlung. Jedes Teil ist ein Lederteil mit Phantommembranen drumherum. Der Helm hält außerdem radioaktive Gase aus der Lunge. Mehr Teile schützen mehr.",
              "",
              "&eWände:&r Blöcke zwischen dir und der Quelle schwächen die Strahlung. Dichte Blöcke wie Blei schirmen am besten ab. Im Tooltip steht, ob ein Block abschirmt.",
              "",
              "&eMedizin:&r &6Jodtabletten&r (getrockneter Seetang, Glowstone, Zucker) nehmen 0,5 Sv von deiner Gesamtdosis. &6RadAway&r (Glasflasche, Ghast-Träne, Redstone, Glowstone) nimmt 1 Sv und schützt fünf Minuten lang.",
              "",
              "An der Schmiedekanzel kannst du jede Rüstung mit &6Strahlenschutz-Platten&r verstärken, eine pro Teil.",
          ],
          tasks=[task_item("nuclear_radiation:hazmat_helmet", 1), task_item("nuclear_radiation:hazmat_chestplate", 1),
                 task_item("nuclear_radiation:hazmat_leggings", 1), task_item("nuclear_radiation:hazmat_boots", 1)],
          rewards=[reward_item("nuclear_radiation:radaway", 2), reward_item("nuclear_radiation:iodine_pill", 4), reward_xp(10)],
          deps=["geiger"], icon="nuclear_radiation:hazmat_helmet"),

    quest("goal", 5.25, 12.5, "&a&lDauerbetrieb",
          subtitle="Ein Reaktor, der nicht schmilzt.",
          description=[
              "Ein Reaktor, der wochenlang läuft, braucht drei Dinge: eine Uranstraße, die genug Brennstoff mischt, Kühlung mit Reserve und eine Kiste für den verbrauchten Brennstoff, die weit weg von dir steht.",
              "",
              "&eWie es weitergeht:&r mehr Zellen, bessere Kühlkörper, HEU-235 oder Oxid-Brennstoff. Jede Änderung prüfst du erst am Controller, bevor du gehst.",
              "",
              "&eKronwerke:&r Stufe 4 frisst Strom. Der Fusionsreaktor von Mekanism will Laserenergie zum Zünden, Draconic Evolution will Energie für seine Kerne, und in Stufe 5 läuft das SPS für die Antimaterie des Obelisken tagelang. Ein Spaltreaktor ist dafür eine gute Grundlast.",
          ],
          tasks=[task_item("nuclearcraft:depleted_fuel_uranium_leu_235", 12), task_item("nuclearcraft:fission_reactor_solid_fuel_cell", 4)],
          rewards=[reward_table("s4_rare"), reward_item("nuclearcraft:fuel_uranium_heu_235", 3), reward_xp(25)],
          deps=["reactor", "hazmat"], icon="nuclearcraft:fuel_uranium_heu_235", size=2.5, shape="gear"),
]

images = [
    head("title", "NuclearCraft", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("machines", "Erze und Maschinen", 5, -1.6, colour="nature"),
    head("reactor", "Der Spaltreaktor", 0, 5.0, colour="fire"),
    head("radiation", "Strahlung", 0, 10.6, colour="brass"),
]

chapter(C, "NuclearCraft", "nuclearcraft:fission_reactor_controller", "tech", quests, shape="square",
        order=35, stage=4,
        subtitle=["Stufe 4: Uran, die Maschinen von NuclearCraft, der Spaltreaktor und Schutz vor Strahlung."],
        images=images)
