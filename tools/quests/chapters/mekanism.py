"""Mekanism in stage 2: osmium, the metallurgic infuser (with manasteel), the infuse types,
alloys, the basic control circuit (electron tube and redstone), steel and the steel casing
(andesite alloy), the basic machines that are not part of the ore ladder, power (heat, wind,
solar, bio and gas burning generators, ethene from the pressurized reaction chamber), fluid
and chemical handling (pipes, tanks, rotary condensentrator, dynamic tank, jetpack), a
checklist of every stage 2 gas and every upgrade, the basic factories, logistics and the
steel line. Ore processing lives in mekanism_ores.py. Numbers come from the Mekanism jars and
config/Mekanism (FE = J / 2.5). Recipes follow kubejs/server_scripts/kronwerke/tech.js and
tech_and_magic.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mekanism"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def gas(name, x, y, title, subtitle, lines, icon, deps=("gas_hydrogen",)):
    """One line of the gas checklist: what makes it, what needs it."""
    return quest(name, x, y, title, subtitle=subtitle, description=lines,
                 tasks=[task_checkmark("Abgehakt")], rewards=[reward_xp(2)],
                 deps=list(deps), icon=icon, optional=True)


def upgrade(name, x, title, subtitle, lines, item_id, reward):
    """One line of the upgrade checklist."""
    return quest(name, x, 19, title, subtitle=subtitle, description=lines,
                 tasks=[task_item(item_id, 1)], rewards=reward,
                 deps=["alloy"] if name == "upgrades" else ["upgrades"], icon=item_id)


def factory(name, x, title, subtitle, lines, item_id):
    """One line of the basic factory checklist."""
    return quest(name, x, 22, title, subtitle=subtitle, description=lines,
                 tasks=[task_item(item_id, 1)],
                 rewards=[reward_item("mekanism:basic_control_circuit", 2), reward_xp(3)],
                 deps=["factory"], icon=item_id, optional=True)


quests = [
    # ---- Osmium und Mana ---------------------------------------------------------------
    quest("welcome", 0, 1, "&5&lGrab Osmium aus",
          subtitle="Das Metall, aus dem Mekanism gebaut ist.",
          description=[
              "Bau &68 Rohes Osmium&r ab. Die großen Adern sitzen im Gebirge über &eY 72&r, mittlere zwischen Y -32 und Y 56, kleine überall unter Y 64.",
              "",
              "&5Mekanism&r ist der große Technikmod von Kronwerke: Maschinen mit Strom, Gase in Schläuchen, am Ende Fusion und Antimaterie. Fast jedes Teil davon enthält Osmium.",
              "",
              "&eStufe 2:&r Grundmaschinen, Generatoren, Stahl, Tanks. &cSpäter:&r Fortgeschritten in Stufe 3, Elite und Fusion in Stufe 4, Antimaterie in Stufe 5. Der Tooltip eines Gegenstands sagt dir, wann er öffnet.",
          ],
          tasks=[task_item("mekanism:raw_osmium", 8)],
          rewards=[reward_item("mekanism:raw_osmium", 16), reward_table("s2_common")],
          icon="mekanism:ingot_osmium", size=2.0, shape="hexagon"),

    quest("osmium", 2.5, 0, "&7Schmilz 32 Osmiumbarren",
          subtitle="Genug für Infusionsanlage, Generator und Schaltkreise.",
          description=[
              "&6Rohes Osmium&r in den Ofen oder Schmelzofen, &e32 Barren&r heraus.",
              "",
              "Nimm eine Spitzhacke mit &6Glück&r mit. Später holt die Erzleiter aus jedem Rohen Erz mehr, siehe Kapitel &5Mekanism: Erz Schritt für Schritt&r.",
          ],
          tasks=[task_item("mekanism:ingot_osmium", 32)],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["welcome"]),

    quest("manasteel", 2.5, 2, "&bHol dir zwei Manastahlbarren",
          subtitle="Die erste Maschine braucht Mana.",
          description=[
              "Zwei &6Manastahlbarren&r aus Botania. Der erste kommt aus dem &aRitual des Waldes&r (vier Infused Iron, zwei Lebeholzzweige, ein Manadiamant, ein Gold Leaf um einen Eichensetzling, gibt vier), danach aus dem &aManabecken&r: Infused Iron für 3 000 Mana.",
              "",
              "Wie beides geht, steht im Kapitel &aBotania: Runen&r. Kein eigenes Becken? Frag einen Magier, zwei Barren sind schnell getauscht.",
          ],
          tasks=[task_item("botania:manasteel_ingot", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["welcome"], icon="botania:manasteel_ingot"),

    quest("infuser", 5, 1, "&9&lBau die Metallurgische Infusionsanlage",
          subtitle="Die erste Maschine, das Herz von Mekanism.",
          description=[
              "&eRezept auf Kronwerke:&r oben Eisen, Ofen, Eisen. Mitte Redstone, &6Osmiumbarren&r, Redstone. Unten &6Manastahl&r, Ofen, &6Manastahl&r.",
              "",
              "Sie drückt einen &eInfusionsstoff&r (Kohlenstoff, Redstone, später Diamant und Obsidian) in einen Gegenstand. Daraus werden Stahl, Legierungen und Schaltkreise. Sie braucht &d20 FE/t&r, die liefert gleich der Wärmegenerator.",
              "",
              "&cAchtung:&r Ein Infusionsstoff bleibt im Tank, bis er verbraucht ist. Zum Wechseln leerst du ihn mit dem Knopf unter dem Balken.",
          ],
          tasks=[task_item("mekanism:metallurgic_infuser", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_table("s2_common"), reward_xp(10)],
          deps=["osmium", "manasteel"], icon="mekanism:metallurgic_infuser", size=2.0, shape="gear"),

    # ---- Legierungen und Stahl --------------------------------------------------------
    quest("infusion", 7.5, 1, "&8Füll Kohlenstoff ein",
          subtitle="Kohle links rein, der Balken steigt.",
          description=[
              "Leg &6Kohle&r in den linken Slot der Infusionsanlage. &eKohlenstoff:&r Kohle 10 mB, Holzkohle 20 mB, Kohleblock 90 mB, Holzkohleblock 180 mB, Angereicherter Kohlenstoff 80 mB.",
              "",
              "&eRedstone:&r Staub 10 mB, Block 90 mB, Angereichertes Redstone 80 mB. Die meisten Rezepte brauchen 10 mB pro Stück, der Schaltkreis 20 mB.",
          ],
          tasks=[task_checkmark("Kohlenstoff ist im Tank")],
          rewards=[reward_item("minecraft:coal_block", 4)],
          deps=["infuser"], icon="mekanism:enriched_carbon"),

    quest("enriched_iron", 10, 0, "&7Reichere Eisen an",
          subtitle="Der erste Schritt zum Stahl.",
          description=[
              "&6Eisenbarren&r oder &6Eisenstaub&r in die Mitte, &e10 mB Kohlenstoff&r: ein &6Angereichertes Eisen&r.",
              "",
              "Es ist ein Zwischenprodukt für den Stahlstaub. Mach gleich einen Stapel, auch das Reaktorglas der Fusion braucht es später.",
          ],
          tasks=[task_item("mekanism:enriched_iron", 8)],
          rewards=[reward_item("minecraft:iron_ingot", 16)],
          deps=["infusion"]),

    quest("steel", 12.5, 0, "&8&lMach Stahl",
          subtitle="Eisen, Kohlenstoff, noch einmal Kohlenstoff.",
          description=[
              "&6Angereichertes Eisen&r mit &e10 mB Kohlenstoff&r gibt &6Stahlstaub&r. Im Ofen wird er zum &6Stahlbarren&r, im Schmelzofen doppelt so schnell.",
              "",
              "Stahl steckt in jedem Gehäuse, Kabel und Rohr. &eKronwerke:&r Das Ziel von Stufe 3 will &e4 000 Stahlbarren&r. Stahl aus dem Hochofen von Immersive Engineering zählt genauso.",
              "",
              img(item_texture("mekanism:ingot_steel"), 32, 32),
          ],
          tasks=[task_item("mekanism:dust_steel", 1), task_item("mekanism:ingot_steel", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 32), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["enriched_iron"], icon="mekanism:ingot_steel", size=1.75, shape="hexagon"),

    quest("casing", 15, 0, "&7&lBau Stahlgehäuse",
          subtitle="Der Rumpf jeder Maschine.",
          description=[
              "&eRezept auf Kronwerke:&r vier &6Stahlbarren&r in die Ecken, vier &6Andesitlegierungen&r an die Seiten, ein &6Osmiumbarren&r in die Mitte. Die Legierung ersetzt das Glas.",
              "",
              "Ab hier ist fast jede Maschine ein Stahlgehäuse plus Schaltkreise und das, was sie besonders macht. Ein Create-Mixer macht aus Andesit und Nugget gleich zwei Legierungen.",
          ],
          tasks=[task_item("mekanism:steel_casing", 4)],
          rewards=[reward_item("create:andesite_alloy", 16), reward_table("s2_common"), reward_xp(5)],
          deps=["steel"], icon="mekanism:steel_casing", size=2.0, shape="gear"),

    quest("tools", 17.5, 0, "&7Schmied dir eine Stahlspitzhacke",
          subtitle="Mekanism Tools: haltbarer als Eisen.",
          description=[
              "Drei &6Stahlbarren&r und zwei Stöcke, wie jede Spitzhacke. Mekanism Tools hat ganze Sätze aus Osmium, Bronze, Stahl, Glowstone und Obsidian.",
              "",
              "Praktisch ist die &6Paxel&r: Spitzhacke, Axt und Schaufel in einem, aus den drei Werkzeugen und zwei Barren.",
          ],
          tasks=[task_item("mekanismtools:steel_pickaxe", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 8)],
          deps=["steel"], optional=True),

    quest("paxel", 17.5, 2, "&7Bau eine Stahlpaxel",
          subtitle="Drei Werkzeuge, ein Slot.",
          description=[
              "Leg &6Stahlaxt&r, &6Stahlspitzhacke&r und &6Stahlschaufel&r nebeneinander in die obere Reihe, darunter zwei &6Eisenbarren&r als Stiel. Heraus kommt die &6Stahlpaxel&r.",
              "",
              "Sie baut Stein, Holz und Erde gleich schnell ab, du wechselst beim Graben nie mehr das Werkzeug. Verzaubern kannst du sie wie jede Spitzhacke.",
              "",
              "Paxel gibt es für jedes Material von Mekanism Tools, auch für Holz, Stein, Eisen, Diamant und Netherit.",
          ],
          tasks=[task_item("mekanismtools:steel_paxel", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 8), reward_xp(5)],
          deps=["tools"], icon="mekanismtools:steel_paxel", optional=True),

    quest("tube", 7.5, 3, "&6Hol dir Elektronenröhren",
          subtitle="Mekanism denkt mit Create-Röhren.",
          description=[
              "Eine &6Elektronenröhre&r ist &6Polierter Rosenquarz&r auf einem &6Eisenblech&r. Rosenquarz macht der Mixer aus Netherquarz und acht Redstone, poliert wird mit Schmirgelpapier.",
              "",
              "Alles dazu steht im Kapitel &6Create: Messing&r. Kein Create? Tausch Osmium oder Stahl gegen einen Stapel Röhren.",
          ],
          tasks=[task_item("create:electron_tube", 4)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(3)],
          deps=["infuser"], icon="create:electron_tube"),

    quest("circuit", 10, 2, "&aInfundier einen Steuerschaltkreis",
          subtitle="Eine Röhre, getränkt in Redstone.",
          description=[
              "&eRezept auf Kronwerke:&r eine &6Elektronenröhre&r mit &e20 mB Redstone&r in der Infusionsanlage gibt einen &6Einfachen Steuerschaltkreis&r. Andere Wege gibt es nicht.",
              "",
              "Jede Maschine nach der Infusionsanlage braucht welche. Ein Dutzend Vorrat spart viele Wechsel des Infusionsstoffs.",
              "",
              "&cAusblick:&r Der Fortgeschrittene Schaltkreis kommt in Stufe 3 mit Gedrucktem Silizium aus AE2, der Elite-Schaltkreis in Stufe 4 mit Draconiumstaub.",
          ],
          tasks=[task_item("mekanism:basic_control_circuit", 4)],
          rewards=[reward_item("mekanism:ingot_osmium", 16), reward_item("minecraft:redstone_block", 2)],
          deps=["infusion", "tube"]),

    quest("alloy", 10, 4, "&cMach Infundierte Legierung",
          subtitle="Kupfer, das Redstone geschluckt hat.",
          description=[
              "Ein &6Kupferbarren&r mit &e10 mB Redstone&r gibt eine &6Infundierte Legierung&r.",
              "",
              "Sie steckt im Energietablett, in den Upgrades, im Elektrolyseur, in der Pumpe und in fast jedem Generator. Kupfer hast du genug, mach einen Stapel.",
          ],
          tasks=[task_item("mekanism:alloy_infused", 8)],
          rewards=[reward_item("minecraft:copper_ingot", 24)],
          deps=["infusion"]),

    quest("tin_bronze", 12.5, 4, "&6Legier Bronze",
          subtitle="Drei Kupfer, ein Hauch Zinn.",
          description=[
              "&6Zinnstaub&r gibt 10 mB Zinn, &6Angereichertes Zinn&r 80 mB. Drei &6Kupferbarren&r mit &e10 mB Zinn&r werden zu vier &6Bronzebarren&r.",
              "",
              "Bronze und Zinn brauchen Basismodule der MekaSuit, Jetpack, Feldflasche und Solarneutronenaktivator. Zinnerz liegt in der ganzen Oberwelt.",
          ],
          tasks=[task_item("mekanism:ingot_bronze", 8)],
          rewards=[reward_item("minecraft:copper_ingot", 24)],
          deps=["alloy"], icon="mekanism:ingot_bronze", optional=True),

    quest("other_ores", 15, 4, "&7Leg eine Kiste für Blei und Salz an",
          subtitle="Heute nebensächlich, morgen gesucht.",
          description=[
              "Sammle beim Graben &6Blei&r, &6Uran&r, &6Fluorit&r und &6Salzblöcke&r (in Ton unter Wasser) in einer eigenen Kiste. Für den Haken: acht Bleibarren.",
              "",
              "&6Blei&r brauchen Reaktorglas, QIO und Strahlenschutz, &6Fluorit&r der Kristallisator, &6Salz&r wird zu Sole und Chlor. &6Uran&r erst in Stufe 5.",
          ],
          tasks=[task_item("mekanism:ingot_lead", 8)],
          rewards=[reward_item("mekanism:block_salt", 4), reward_xp(5)],
          deps=["tin_bronze"], icon="mekanism:ingot_lead", optional=True),

    # ---- Grundmaschinen ---------------------------------------------------------------
    quest("enrichment", 0, 8, "&d&lBau eine Anreicherungskammer",
          subtitle="Für Erz, aber auch für Kohlenstoff.",
          description=[
              "&eRezept:&r Stahlgehäuse in die Mitte, Eisen links und rechts, Schaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Was sie mit Erz macht, steht im Kapitel &5Mekanism: Erz Schritt für Schritt&r. Hier brauchst du sie für Angereicherten Kohlenstoff, Redstone und Diamant, die achtmal so viel Infusionsstoff geben.",
          ],
          tasks=[task_item("mekanism:enrichment_chamber", 1)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_table("s2_common"), reward_xp(5)],
          deps=["casing"], icon="mekanism:enrichment_chamber", size=1.5, shape="hexagon"),

    quest("enriched_carbon", 2.5, 7, "&8Reichere Kohle an",
          subtitle="Achtmal so viel aus einer Kohle.",
          description=[
              "&6Kohle&r durch die Anreicherungskammer: &6Angereicherter Kohlenstoff&r, der in der Infusionsanlage &e80 mB&r gibt statt 10.",
              "",
              "Ein Stapel Kohle reicht so für über 250 Stahlbarren statt 32. Schick die Kohle deiner Stahlstraße immer erst durch die Kammer.",
          ],
          tasks=[task_item("mekanism:enriched_carbon", 16)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["enrichment"]),

    quest("crusher", 2.5, 9, "&4Bau einen Zerkleinerer",
          subtitle="Mahlt mit den Rädern von Create.",
          description=[
              "&eRezept auf Kronwerke:&r Stahlgehäuse in die Mitte, links und rechts ein &6Mahlwerkrad&r statt der Lavaeimer, Schaltkreise oben und unten, Redstone in die Ecken.",
              "",
              "Er macht Barren zu Staub, Bruchstein zu Kies, Obsidian zu vier Obsidianstaub (Stufe 3 braucht den). Pflanzen und Essen werden zu &6Bio-Brennstoff&r, ein Apfel zu zwei.",
              "",
              "&eNether-Tipp:&r Eine Lohenrute gibt hier vier Lohenstaub statt zwei.",
          ],
          tasks=[task_item("mekanism:crusher", 1)],
          rewards=[reward_item("mekanism:ingot_osmium", 16), reward_xp(5)],
          deps=["enrichment"]),

    quest("sawmill", 5, 9, "&eBau ein Präzisionssägewerk",
          subtitle="Sechs Bretter pro Stamm.",
          description=[
              "Stahlgehäuse, Schaltkreise, Eisen und Bretter. Ein Stamm wird zu &esechs Brettern&r statt vier, dazu ab und zu &6Sägemehl&r.",
              "",
              "Treppen, Türen und Truhen zerlegt es wieder in Holz. Sägemehl wird zur Kartonschachtel, mit der du Blöcke samt Inhalt umziehst.",
          ],
          tasks=[task_item("mekanism:precision_sawmill", 1)],
          rewards=[reward_item("minecraft:oak_log", 32)],
          deps=["crusher"], optional=True),

    quest("cardboard", 5, 10.5, "&eFalte eine Kartonschachtel",
          subtitle="Umziehen, ohne auszuräumen.",
          description=[
              "Vier &6Sägespäne&r aus dem Präzisionssägewerk im Quadrat ergeben eine &6Kartonschachtel&r.",
              "",
              "&eSchleichen und Rechtsklick&r auf einen Block packt ihn samt Inhalt ein: eine volle Truhe, eine Maschine mitten in der Arbeit. Setz die Schachtel woanders ab, und der Block steht dort wieder, mit allem, was drin war.",
              "",
              "Betten, Türen, Prüfungsspawner und Tresore lassen sich nicht einpacken.",
          ],
          tasks=[task_item("mekanism:cardboard_box", 2)],
          rewards=[reward_item("minecraft:oak_log", 16), reward_xp(3)],
          deps=["sawmill"], icon="mekanism:cardboard_box", optional=True),

    quest("seismic", 0, 10.5, "&6Hör in den Boden",
          subtitle="Seismischer Vibrator und Lesegerät.",
          description=[
              "&6Seismischer Vibrator:&r oben Zinn, Lapislazuli, Zinn, Mitte Schaltkreis, &6Stahlgehäuse&r, Schaltkreis, unten drei Zinn. &6Seismisches Lesegerät:&r Stahl rundherum, oben in der Mitte Lapislazuli, in der Mitte ein &6Energietablett&r.",
              "",
              "Stell den Vibrator auf und gib ihm Strom. Er bringt seinen ganzen Chunk zum Schwingen. Stell dich in denselben Chunk und benutz das geladene Lesegerät: Es zeigt dir jeden Block der Säule unter dir bis zum Grundgestein, mit der Häufigkeit jeder Sorte.",
              "",
              "So weißt du vor dem ersten Spatenstich, ob unter der Basis Osmium, Diamant oder nur Stein liegt.",
          ],
          tasks=[task_item("mekanism:seismic_vibrator", 1), task_item("mekanism:seismic_reader", 1)],
          rewards=[reward_item("mekanism:ingot_tin", 8), reward_xp(5)],
          deps=["enrichment"], icon="mekanism:seismic_vibrator", optional=True),

    # ---- Energie ----------------------------------------------------------------------
    quest("heat_gen", 8, 8, "&6&lBau einen Wärmegenerator",
          subtitle="Strom aus allem, was brennt.",
          description=[
              "&eRezept:&r oben drei Eisen, Mitte Bretter, Osmium, Bretter, unten Kupfer, Ofen, Kupfer.",
              "",
              "Mit Brennstoff &d80 FE/t&r. Jede angrenzende &bLavaquelle&r gibt &d12 FE/t&r dazu, ohne dass sie verbraucht wird, im Nether noch einmal 40 FE/t. Das reicht für drei bis vier Grundmaschinen.",
              "",
              "Stell ihn direkt neben die Infusionsanlage, Strom geht auch ohne Kabel hinüber.",
          ],
          tasks=[task_item("mekanismgenerators:heat_generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(5)],
          deps=["osmium"], icon="mekanismgenerators:heat_generator", size=1.5, shape="hexagon"),

    quest("cables", 10.5, 7, "&aLeg Universalkabel",
          subtitle="Strom von hier nach da.",
          description=[
              "Zwei &6Stahlbarren&r mit Redstone dazwischen geben acht &6Einfache Universalkabel&r. Sie tragen &d3 200 FE/t&r.",
              "",
              "Kabel verbinden sich mit allem, was Strom nimmt oder gibt. Mit dem Konfigurator stellst du eine Seite auf &eKeine&r, wenn sie nicht verbinden soll.",
          ],
          tasks=[task_item("mekanism:basic_universal_cable", 16)],
          rewards=[reward_item("mekanism:basic_universal_cable", 16)],
          deps=["heat_gen", "steel"]),

    quest("tablet", 10.5, 9, "&aBau Energietabletts",
          subtitle="Eine Batterie für die Tasche.",
          description=[
              "Redstone, Gold und &6Infundierte Legierung&r ergeben ein &6Energietablett&r. Es lädt in jedem Energieslot.",
              "",
              "Vor allem ist es Zutat: Energie-Würfel, Wind- und Solargenerator, Rotationskondensator, Laser und Induktionszellen brauchen es.",
          ],
          tasks=[task_item("mekanism:energy_tablet", 2)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["heat_gen", "alloy"]),

    quest("cube", 13, 8, "&aStell einen Energie-Würfel auf",
          subtitle="1,6 Millionen FE Puffer.",
          description=[
              "Zwei Energietabletts, zwei Eisen, vier Redstone, ein Stahlgehäuse in der Mitte. Er speichert &d1,6 Millionen FE&r und gibt &d1 600 FE/t&r ab.",
              "",
              "Eine Seite ist Ausgang, die anderen Eingang. Dreh den Ausgang zur Maschinenleitung, die Generatoren an eine Eingangsseite.",
          ],
          tasks=[task_item("mekanism:basic_energy_cube", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["cables", "tablet"], icon="mekanism:basic_energy_cube"),

    quest("wind", 15.5, 7, "&bStell einen Windgenerator hoch",
          subtitle="Je höher, desto mehr.",
          description=[
              "Osmium, Infundierte Legierung, zwei Energietabletts und ein Schaltkreis. Er liefert &d24 FE/t&r ab Y 24 und mehr, je höher er steht, bis &d192 FE/t&r.",
              "",
              "Er ragt mehrere Blöcke hoch und braucht freien Raum. Ein paar auf einem Gipfel, per Kabel am Würfel, ersetzen einen Kohlevorrat.",
          ],
          tasks=[task_item("mekanismgenerators:wind_generator", 1)],
          rewards=[reward_item("mekanism:basic_universal_cable", 16), reward_xp(5)],
          deps=["cube"], optional=True),

    quest("solar", 15.5, 9, "&eLeg Solargeneratoren aufs Dach",
          subtitle="Klein, leise, nur tagsüber.",
          description=[
              "Drei &6Solarmodule&r (Glasscheiben, Redstone, Legierung, Osmium) über Legierung, Eisen, Osmium und einem Energietablett. &d20 FE/t&r bei Tag und freiem Himmel.",
              "",
              "Vier davon werden in Stufe 3 zum Erweiterten Solargenerator mit 120 FE/t.",
          ],
          tasks=[task_item("mekanismgenerators:solar_generator", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 4)],
          deps=["cube"], optional=True),

    quest("bio_gen", 18, 9, "&aVerbrenn Bio-Brennstoff",
          subtitle="140 FE/t aus Ernteresten.",
          description=[
              "&6Biogenerator:&r Redstone, Legierung, Bio-Brennstoff, ein Schaltkreis und Eisen. Er verbrennt &6Bio-Brennstoff&r aus dem Zerkleinerer und liefert &d140 FE/t&r.",
              "",
              "Eine Weizen- oder Kartoffelfarm vor dem Zerkleinerer, und er läuft ohne Kohle.",
          ],
          tasks=[task_item("mekanismgenerators:bio_generator", 1), task_item("mekanism:bio_fuel", 32)],
          rewards=[reward_item("minecraft:wheat_seeds", 16), reward_xp(5)],
          deps=["cube", "crusher"], optional=True),

    quest("gas_gen", 18, 7, "&bVerbrenn Wasserstoff",
          subtitle="Der Gasverbrennende Generator.",
          description=[
              "&eRezept:&r Osmium in die Ecken, Legierung oben und unten, Stahlgehäuse links und rechts, ein &6Elektrolytischer Kern&r in die Mitte.",
              "",
              "Er verbrennt Gas aus seinem Tank. &bWasserstoff&r kommt aus dem Elektrolyseur (Kapitel &5Mekanism: Erz Schritt für Schritt&r), aber das Spalten kostet mehr Strom, als der Wasserstoff zurückgibt.",
              "",
              "Lohnend wird er mit &bEthen&r aus der nächsten Quest, oder mit Wasserstoff, der sowieso übrig ist.",
          ],
          tasks=[task_item("mekanismgenerators:gas_burning_generator", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_xp(5)],
          deps=["cube"], icon="mekanismgenerators:gas_burning_generator"),

    quest("chargepad", 13, 10, "&aStell dich auf ein Ladepad",
          subtitle="Laden im Vorbeigehen.",
          description=[
              "Drei &6Polierte Schwarzsteindruckplatten&r oben, darunter Stahl, &6Energietablett&r, Stahl.",
              "",
              "Häng es per Kabel an deinen Würfel. Wer darauf steht, bekommt alles mit Stromspeicher im Inventar und in der Rüstung geladen, egal aus welchem Mod. Später parkt hier auch der Robit.",
              "",
              "Leg es vor die Tür der Werkstatt, dann ist das Tablett jedes Mal voll, wenn du hinausgehst.",
          ],
          tasks=[task_item("mekanism:chargepad", 1)],
          rewards=[reward_item("minecraft:polished_blackstone_pressure_plate", 3), reward_xp(3)],
          deps=["cube"], icon="mekanism:chargepad", optional=True),

    quest("free_runners", 10.5, 10.5, "&bZieh Freiläufer an",
          subtitle="Kein Fallschaden, keine Stufe zu hoch.",
          description=[
              "Schaltkreise oben links und rechts, darunter zwei &6Infundierte Legierungen&r, unten zwei &6Energietabletts&r, die Mitte bleibt frei.",
              "",
              "Die Stiefel laufen mit Strom: Du steigst ohne Springen eine Stufe hoch, und Fallschaden schlucken sie ganz, solange Strom drin ist. Pro halbem Herz kostet das &e50 J&r, voll fassen sie &e64 000 J&r.",
              "",
              "&eGepanzerte Freiläufer:&r ein Stahlblock oben, Diamantstaub links und rechts der Freiläufer, unten zwei Bronzebarren. Dazu &d3&r Rüstung.",
          ],
          tasks=[task_item("mekanism:free_runners", 1)],
          rewards=[reward_item("mekanism:energy_tablet", 1), reward_xp(5)],
          deps=["tablet"], icon="mekanism:free_runners", optional=True),

    quest("ethene", 20.5, 8, "&e&lMach Ethen in der Druckreaktionskammer",
          subtitle="Bio-Brennstoff, Wasser, Wasserstoff.",
          description=[
              "&6Druckreaktionskammer:&r oben Stahl, Legierung, Stahl, Mitte Schaltkreis, Anreicherungskammer, Schaltkreis, unten Chemikalienbehälter, Dynamischer Tank, Chemikalienbehälter.",
              "",
              "&e2 Bio-Brennstoff + 10 mB Wasser + 100 mB Wasserstoff&r geben &e100 mB Ethen&r und ein &6Substrat&r. Ethen im Gasgenerator ist die stärkste Stromquelle von Stufe 2.",
              "",
              "Dieselbe Kammer macht aus Kohle, Wasser und Sauerstoff Wasserstoff und Schwefelstaub, und später HDPE für die MekaSuit.",
          ],
          tasks=[task_item("mekanism:pressurized_reaction_chamber", 1), task_item("mekanism:substrate", 4)],
          rewards=[reward_item("mekanism:bio_fuel", 64), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["gas_gen", "bio_gen"], icon="mekanism:pressurized_reaction_chamber", size=1.5, shape="hexagon"),

    # ---- Flüssigkeiten und Gase -------------------------------------------------------
    quest("pipes", 0, 13, "&bLeg Rohrleitungen und stell einen Tank auf",
          subtitle="Wenn es fließt, gehört es ins Rohr.",
          description=[
              "Zwei Stahl und ein Eimer geben acht &6Einfache Rohrleitungen&r (250 mB pro Zug). Der &6Einfache Flüssigkeitsbehälter&r (Redstone und Eisen) fasst &e32 000 mB&r.",
              "",
              "Der Tank behält seinen Inhalt beim Abbauen. Ein Tank Lava neben dem Wärmegenerator ist eine gute Reserve.",
          ],
          tasks=[task_item("mekanism:basic_mechanical_pipe", 8), task_item("mekanism:basic_fluid_tank", 1)],
          rewards=[reward_item("minecraft:bucket", 4)],
          deps=["casing"], icon="mekanism:basic_fluid_tank"),

    quest("chem_tank", 2.5, 13, "&bBau einen Chemikalienbehälter",
          subtitle="Gase gehören nicht in Rohre.",
          description=[
              "Vier &6Osmiumbarren&r an die Seiten, Redstone in die Ecken: ein &6Einfacher Chemikalienbehälter&r für &e64 000 mB&r Gas. Zwei Stahl und Glas geben acht &6Druckschläuche&r.",
              "",
              "Gase laufen nur in Druckschläuchen, Flüssigkeiten nur in Rohrleitungen. Ein Behälter kann sein Gas mit dem Knopf im Fenster ablassen, wenn du es nicht brauchst.",
          ],
          tasks=[task_item("mekanism:basic_chemical_tank", 1), task_item("mekanism:basic_pressurized_tube", 8)],
          rewards=[reward_item("mekanism:basic_pressurized_tube", 8), reward_xp(3)],
          deps=["pipes"], icon="mekanism:basic_chemical_tank"),

    quest("rotary", 5, 13, "&bBau einen Rotationskondensator",
          subtitle="Aus Gas wird Flüssigkeit und zurück.",
          description=[
              "Glas in die Ecken, Schaltkreise oben und unten, links ein Chemikalienbehälter, in der Mitte ein Energietablett, rechts ein Flüssigkeitsbehälter.",
              "",
              "Ein Schalter im Fenster wählt die Richtung: &eKondensieren&r macht aus Gas Flüssigkeit 1 zu 1 (in Eimer füllbar), &eDekondensieren&r macht aus Wasser Wasserdampf oder aus flüssigem Gas wieder Gas.",
          ],
          tasks=[task_item("mekanism:rotary_condensentrator", 1)],
          rewards=[reward_item("minecraft:bucket", 4), reward_xp(3)],
          deps=["chem_tank"], icon="mekanism:rotary_condensentrator"),

    quest("dynamic_tank", 7.5, 13, "&9&lBau einen Dynamischen Tank",
          subtitle="Ein Multiblock für ganze Seen.",
          description=[
              "Vier Stahl um einen Eimer geben vier &6Dynamische Tanks&r, vier davon um einen Schaltkreis zwei &6Dynamische Ventile&r. Bau einen hohlen Quader, mindestens 3 mal 3 mal 3, Wände auch aus Strukturglas.",
              "",
              "Rohre und Schläuche docken an die Ventile. Er hält eine Flüssigkeit oder ein Gas, laut Server-Config &e350 000 mB Flüssigkeit&r pro Block Volumen.",
          ],
          tasks=[task_item("mekanism:dynamic_tank", 24), task_item("mekanism:dynamic_valve", 2)],
          rewards=[reward_item("mekanism:ingot_steel", 16), reward_table("s2_common"), reward_xp(8)],
          deps=["chem_tank"], icon="mekanism:dynamic_valve", size=1.5, shape="hexagon"),

    quest("jetpack", 10, 13, "&eFlieg mit Wasserstoff",
          subtitle="Das Jetpack von Mekanism.",
          description=[
              "Oben Stahl, Schaltkreis, Stahl, Mitte Zinn, Chemikalienbehälter, Zinn, unten Zinn. Es fasst &e24 000 mB Wasserstoff&r.",
              "",
              "Füllen: in den Itemslot eines Chemikalienbehälters voller Wasserstoff legen. Es hat die Modi normal und schweben.",
          ],
          tasks=[task_item("mekanism:jetpack", 1)],
          rewards=[reward_item("mekanism:ingot_bronze", 8), reward_xp(5)],
          deps=["chem_tank"], optional=True),

    quest("jetpack_armored", 5, 14.75, "&ePanzer dein Jetpack",
          subtitle="Fliegen, ohne die Brustplatte abzulegen.",
          description=[
              "Oben links und rechts &6Diamantstaub&r, in der Mitte Bronze, &6Stahlblock&r, Bronze, unten in der Mitte dein &6Jetpack&r. Der Wasserstoff im Tank bleibt erhalten.",
              "",
              "Das Jetpack sitzt im Brustplatz, also trägst du damit keine Rüstung. Das &6Gepanzerte Jetpack&r bringt &d8&r Rüstung und &d2&r Härte mit, so viel wie eine Diamantbrustplatte.",
              "",
              "Diamantstaub macht der Zerkleinerer aus einem Diamanten.",
          ],
          tasks=[task_item("mekanism:jetpack_armored", 1)],
          rewards=[reward_item("mekanism:ingot_bronze", 8), reward_xp(5)],
          deps=["jetpack"], icon="mekanism:jetpack_armored", optional=True),

    quest("scuba", 7.5, 14.75, "&bTauch mit Sauerstoff",
          subtitle="Tauchermaske und Taucherflasche.",
          description=[
              "&6Tauchermaske:&r oben Stahl, Mitte Glas, Schaltkreis, Glas, unten links und rechts Stahl. &6Taucherflasche:&r oben ein Schaltkreis, Mitte Legierung, &6Einfacher Chemikalienbehälter&r, Legierung, unten drei Stahl.",
              "",
              "Die Flasche fasst &e24 000 mB Sauerstoff&r. Füllen wie beim Jetpack: in den Itemslot eines Chemikalienbehälters voller Sauerstoff legen. Den Sauerstoff liefert der Elektrolyseur.",
              "",
              "Zieh beides an und schalte die Flasche ein. Solange Sauerstoff drin ist, ertrinkst du nicht. Ideal für Ozeanmonumente und Salz unter Wasser.",
          ],
          tasks=[task_item("mekanism:scuba_mask", 1), task_item("mekanism:scuba_tank", 1)],
          rewards=[reward_item("minecraft:prismarine_shard", 8), reward_xp(5)],
          deps=["chem_tank"], icon="mekanism:scuba_mask", optional=True),

    # ---- Gase -------------------------------------------------------------------------
    gas("gas_hydrogen", 13.5, 13, "&fWasserstoff",
        "Elektrolyseur: Wasser zu Wasserstoff und Sauerstoff.",
        ["&eMacht ihn:&r der Elektrolyseur aus &e2 mB Wasser&r (2 mB Wasserstoff, 1 mB Sauerstoff). Die Druckreaktionskammer macht ihn aus Kohle, Wasser und Sauerstoff.",
         "&eBraucht ihn:&r Gasgenerator, Jetpack, Ethen, Chlorwasserstoff."],
        "mekanism:hydrogen_bucket", deps=("chem_tank",)),
    gas("gas_oxygen", 15.5, 13, "&fSauerstoff",
        "Fällt beim Wasserspalten mit an.",
        ["&eMacht ihn:&r der Elektrolyseur, 1 mB pro 2 mB Wasser. Ein Feuerstein im Chemikalien-Slot gibt 10 mB.",
         "&eBraucht ihn:&r Klärkammer (3x Erz), Tauchermaske, Schwefeltrioxid."],
        "mekanism:oxygen_bucket"),
    gas("gas_brine", 17.5, 13, "&fSole",
        "Salz im Oxidierer.",
        ["&eMacht sie:&r der Chemische Oxidierer aus Salz, 15 mB pro Stück. Ab Stufe 3 die Wärmeverdampfungsanlage aus Wasser, 10 zu 1.",
         "&eBraucht sie:&r der Elektrolyseur für Chlor, die Verdampfungsanlage für Lithium."],
        "mekanism:brine_bucket"),
    gas("gas_chlorine", 19.5, 13, "&fChlor",
        "Sole im Elektrolyseur.",
        ["&eMacht es:&r der Elektrolyseur aus &e10 mB Sole&r: 1 mB Chlor und 1 mB Natrium.",
         "&eBraucht es:&r der Chemische Injektor für Chlorwasserstoff."],
        "mekanism:chlorine_bucket", deps=("gas_brine",)),
    gas("gas_sodium", 13.5, 14.75, "&fNatrium",
        "Der Rest beim Chlor.",
        ["&eMacht es:&r der Elektrolyseur, nebenbei zum Chlor.",
         "&eBraucht es:&r in Stufe 2 niemand. Lass es ab oder sammle es, der Spaltreaktor in Stufe 5 kühlt damit."],
        "mekanism:sodium_bucket", deps=("gas_chlorine",)),
    gas("gas_hcl", 15.5, 14.75, "&fChlorwasserstoff",
        "Wasserstoff plus Chlor.",
        ["&eMacht ihn:&r der Chemische Injektor aus 1 mB Wasserstoff und 1 mB Chlor. Salz direkt in die Injektionskammer gibt 2 mB.",
         "&eBraucht ihn:&r die Injektionskammer, Erz 4x in Stufe 4."],
        "mekanism:hydrogen_chloride_bucket", deps=("gas_chlorine",)),
    gas("gas_so2", 17.5, 14.75, "&fSchwefeldioxid",
        "Schwefelstaub im Oxidierer.",
        ["&eMacht es:&r der Chemische Oxidierer, 100 mB pro Schwefelstaub. Schwefel gibt die Druckreaktionskammer aus Kohle.",
         "&eBraucht es:&r der Injektor für Schwefeltrioxid."],
        "mekanism:sulfur_dioxide_bucket"),
    gas("gas_so3", 19.5, 14.75, "&fSchwefeltrioxid",
        "Dioxid plus Sauerstoff.",
        ["&eMacht es:&r der Chemische Injektor aus 2 mB Schwefeldioxid und 1 mB Sauerstoff, gibt 2 mB.",
         "&eBraucht es:&r der Injektor für Schwefelsäure."],
        "mekanism:sulfur_trioxide_bucket", deps=("gas_so2",)),
    gas("gas_vapor", 13.5, 16.5, "&fWasserdampf",
        "Wasser im Rotationskondensator.",
        ["&eMacht ihn:&r der Rotationskondensator im Modus Dekondensieren aus Wasser, 1 zu 1.",
         "&eBraucht ihn:&r der Injektor für Schwefelsäure."],
        "minecraft:water_bucket"),
    gas("gas_acid", 15.5, 16.5, "&fSchwefelsäure",
        "Trioxid plus Wasserdampf.",
        ["&eMacht sie:&r der Chemische Injektor aus je 1 mB Schwefeltrioxid und Wasserdampf. Schwefelstaub direkt in die Auflösungskammer gibt 2 mB.",
         "&eBraucht sie:&r die Auflösungskammer, Erz 5x in Stufe 4."],
        "mekanism:sulfuric_acid_bucket", deps=("gas_so3", "gas_vapor")),
    gas("gas_ethene", 17.5, 16.5, "&fEthen",
        "Aus der Druckreaktionskammer.",
        ["&eMacht es:&r die Druckreaktionskammer aus Bio-Brennstoff, Wasser und Wasserstoff.",
         "&eBraucht es:&r der Gasgenerator, und ab Stufe 3 das Substrat für HDPE."],
        "mekanism:ethene_bucket"),

    # ---- Upgrades ---------------------------------------------------------------------
    upgrade("upgrades", 0, "&bBau ein Geschwindigkeitsupgrade",
            "Schneller, aber hungriger.",
            ["Glas oben und unten, Infundierte Legierung links und rechts, &6Osmiumstaub&r in die Mitte. Bis zu 8 pro Maschine, acht machen sie &ezehnmal&r so schnell.",
             "",
             "Rechnung und Mischung mit Energie-Upgrades: Kapitel &5Mekanism: Erz Schritt für Schritt&r."],
            "mekanism:upgrade_speed", [reward_item("mekanism:alloy_infused", 4), reward_xp(3)]),
    upgrade("up_energy", 2, "&aBau ein Energie-Upgrade",
            "Weniger Strom pro Tick.",
            ["Wie das Geschwindigkeitsupgrade, mit &6Goldstaub&r in der Mitte. Acht senken den Verbrauch auf ein Zehntel und vergrößern den Puffer."],
            "mekanism:upgrade_energy", [reward_item("mekanism:alloy_infused", 4), reward_xp(3)]),
    upgrade("up_chemical", 4, "&8Bau ein Chemie-Upgrade",
            "Weniger Gas pro Vorgang.",
            ["Mit &6Eisenstaub&r in der Mitte. Senkt den Gasverbrauch von Klärkammer, Injektionskammer und Auflösungskammer, den Geschwindigkeitsupgrades hochtreiben."],
            "mekanism:upgrade_chemical", [reward_item("mekanism:alloy_infused", 4), reward_xp(3)]),
    upgrade("up_filter", 6, "&bBau ein Filter-Upgrade",
            "Schweres Wasser aus der Pumpe.",
            ["Mit &6Zinnstaub&r in der Mitte. In der Elektrischen Pumpe holt es aus jedem Wasserblock &e10 mB Schweres Wasser&r. Das wird in Stufe 4 zu Deuterium für die Fusion."],
            "mekanism:upgrade_filter", [reward_item("mekanism:dust_tin", 4), reward_xp(3)]),
    upgrade("up_muffling", 8, "&7Bau ein Dämpfungsupgrade",
            "Ruhe in der Fabrikhalle.",
            ["Vier Wolle um einen Barren oder Ziegel. Es macht Maschinen leiser, mehr nicht. Für Streamer mit vielen Maschinen neben dem Mikrofon Gold wert."],
            "mekanism:upgrade_muffling", [reward_item("minecraft:white_wool", 8), reward_xp(3)]),
    upgrade("up_anchor", 10, "&dBau ein Ankerupgrade",
            "Die Maschine läuft, auch wenn du weg bist.",
            ["Glas, Legierung und &6Diamantstaub&r in der Mitte. Es hält den Chunk der Maschine geladen. Ideal für den Digitalen Miner in Stufe 3."],
            "mekanism:upgrade_anchor", [reward_item("minecraft:diamond", 1), reward_xp(3)]),
    upgrade("up_stone", 12, "&7Bau ein Steingenerator-Upgrade",
            "Stein aus dem Nichts.",
            ["Glas, Legierung, ein Wasser- und ein Lavaeimer. Es erzeugt Stein oder Bruchstein, wo eine Maschine ihn braucht, zum Beispiel im Kombinierer, der in Stufe 4 aus Rohem Erz und Bruchstein Erzblöcke baut."],
            "mekanism:upgrade_stone_generator", [reward_item("minecraft:lava_bucket", 1), reward_xp(3)]),

    # ---- Logistik und Ausbau ----------------------------------------------------------
    quest("configurator", 0, 23, "&3Bau einen Konfigurator",
          subtitle="Das Werkzeug jedes Technikers.",
          description=[
              "Zwei Eisen, Osmium und Stahl. &eShift und Mausrad&r wechselt den Modus.",
              "",
              "&eModi:&r Seiten konfigurieren, Inhalt auswerfen, Blöcke drehen, Schraubenschlüssel (baut Maschinen samt Inhalt ab).",
              "",
              "&eSeitenkonfiguration:&r Reiter oben links im Fenster. Eingang rot, Ausgang blau, und &eAuto-Auswurf&r schiebt Fertiges von selbst weiter.",
          ],
          tasks=[task_item("mekanism:configurator", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 8)],
          deps=["casing"]),

    quest("transporter", 2.5, 23, "&eLeg Logistiktransporter",
          subtitle="Gegenstände auf Wanderschaft.",
          description=[
              "Zwei Stahl und ein Schaltkreis geben acht &6Einfache Logistiktransporter&r.",
              "",
              "Sie ziehen nichts von selbst aus einer Kiste: entweder Auto-Auswurf an der Maschine oder die Transporterseite mit dem Konfigurator auf &eZiehen&r. Eingefärbte Transporter verbinden sich nur mit gleicher Farbe.",
          ],
          tasks=[task_item("mekanism:basic_logistical_transporter", 16)],
          rewards=[reward_item("mekanism:basic_logistical_transporter", 8)],
          deps=["configurator"]),

    quest("config_card", 0, 25, "&3Kopier Einstellungen mit der Konfigurationskarte",
          subtitle="Einmal einstellen, zehnmal einfügen.",
          description=[
              "Vier &6Infundierte Legierungen&r im Kreuz um einen &6Einfachen Steuerschaltkreis&r.",
              "",
              "&eSchleichen und Rechtsklick&r auf eine fertig eingestellte Maschine liest Seitenkonfiguration und Auto-Auswurf ein. &eRechtsklick&r auf die nächste Maschine gleicher Art schreibt alles hinein. Schleichen und Rechtsklick in die Luft leert die Karte.",
              "",
              "Bei einer Reihe aus fünf Fabriken spart das jedes Mal fünf Fenster voller Farbklötze.",
          ],
          tasks=[task_item("mekanism:configuration_card", 1)],
          rewards=[reward_item("mekanism:alloy_infused", 4), reward_xp(3)],
          deps=["configurator"], icon="mekanism:configuration_card", optional=True),

    quest("personal_chest", 0, 27, "&3Stell eine Persönliche Truhe auf",
          subtitle="54 Plätze, die nur dir gehören.",
          description=[
              "Oben Stahl, Glas, Stahl, Mitte Truhe, Schaltkreis, Truhe, unten drei Stahl.",
              "",
              "Sie hat &e54&r Plätze wie eine große Truhe. Wer sie öffnen darf, stellst du im Sicherheitsreiter ein. Abgebaut behält sie ihren Inhalt, und als Gegenstand öffnest du sie mit Rechtsklick direkt aus dem Inventar: ein Rucksack.",
              "",
              "Der Chemische Oxidierer und später Robit und QIO brauchen sie als Zutat.",
          ],
          tasks=[task_item("mekanism:personal_chest", 1)],
          rewards=[reward_item("minecraft:chest", 4), reward_xp(3)],
          deps=["configurator"], icon="mekanism:personal_chest", optional=True),

    quest("sorter", 2.5, 25, "&eStell einen Logistischen Sortierer auf",
          subtitle="Filtert aus Kisten in Transporter.",
          description=[
              "Eisen rundherum, oben ein Kolben, in der Mitte ein Schaltkreis. Er zieht nach Filtern aus der Kiste hinter ihm und schiebt in den Transporter vor ihm.",
              "",
              "Zwei davon stecken im Digitalen Miner aus Stufe 3.",
          ],
          tasks=[task_item("mekanism:logistical_sorter", 1)],
          rewards=[reward_item("minecraft:piston", 2), reward_xp(3)],
          deps=["transporter"], optional=True),

    quest("bin", 5, 25, "&eStell eine Tonne hin",
          subtitle="4 096 Stück einer Sorte.",
          description=[
              "Stein, Redstone und ein Schaltkreis. Die &6Einfache Tonne&r fasst &e4 096&r Stück einer Sorte, Linksklick nimmt, Rechtsklick legt hinein.",
              "",
              "Als Puffer am Anfang einer Straße ideal. Die besseren Tonnen fassen 8 192, 32 768 und 262 144.",
          ],
          tasks=[task_item("mekanism:basic_bin", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64)],
          deps=["transporter"], optional=True),

    quest("factory", 5, 23, "&a&lBau deine erste Fabrik",
          subtitle="Drei Plätze statt einem.",
          description=[
              "&6Einfacher Stufen Installateur:&r Redstone in die Ecken, Schaltkreise oben und unten, Eisen links und rechts, ein Brett in die Mitte. Rechtsklick auf eine Maschine macht sie zur &6Einfachen Fabrik&r.",
              "",
              "Eine Fabrik arbeitet an &edrei&r Gegenständen gleichzeitig. Der Pfeilknopf im Fenster verteilt Stapel auf alle Plätze. Danach: Fortschrittlich 5 Plätze (Stufe 3), Elite 7 und Ultimativ 9 (Stufe 4).",
          ],
          tasks=[task_item("mekanism:basic_tier_installer", 1)],
          rewards=[reward_item("mekanism:basic_control_circuit", 4), reward_table("s2_common")],
          deps=["transporter"], icon="mekanism:basic_tier_installer", size=1.5, shape="hexagon"),

    factory("f_smelting", 7.5, "&aEinfache Schmelzfabrik", "Drei Öfen in einem.",
            ["Der Energiegeladene Schmelzer mit Installateur, oder an der Werkbank: der Schmelzer in der Mitte des Installateur-Musters."],
            "mekanism:basic_smelting_factory"),
    factory("f_crushing", 9.5, "&aEinfache Brecherfabrik", "Drei Zerkleinerer in einem.",
            ["Der Zerkleinerer mit Installateur. Gut für Bio-Brennstoff und Obsidianstaub."],
            "mekanism:basic_crushing_factory"),
    factory("f_infusing", 11.5, "&aEinfache Infusionsfabrik", "Drei Stahlplätze.",
            ["Die Infusionsanlage mit Installateur. Alle drei Plätze teilen sich einen Tank Infusionsstoff, also eine Fabrik pro Stoff."],
            "mekanism:basic_infusing_factory"),
    factory("f_sawing", 13.5, "&aEinfache Sägefabrik", "Drei Sägen.",
            ["Das Präzisionssägewerk mit Installateur. Für Holzfarmen, die Bretter in Mengen brauchen."],
            "mekanism:basic_sawing_factory"),

    quest("oredict", 7.5, 27, "&3Vereinheitliche Metalle",
          subtitle="Kupfer ist Kupfer, egal aus welchem Mod.",
          description=[
              "Erst das &6Lexikon&r: ein Schaltkreis über einem Buch. Dann das &6Erz-Diagnosegerät&r (Oredictionificator): oben Stahl, Glasscheibe, Stahl, Mitte Schaltkreis, Lexikon, Schaltkreis, unten Stahl, Truhe, Stahl.",
              "",
              "Gib ihm einen Filter mit einem Tag, etwa &ec:ingots/copper&r, und wähl mit den Pfeilen, welcher Barren herauskommen soll. Alles mit diesem Tag wird dann in genau diese Sorte getauscht. Mit dem Lexikon in der Hand siehst du per Rechtsklick die Tags jedes Gegenstands.",
              "",
              "&eErlaubt sind auf Kronwerke:&r Staub, Barren, Nuggets, Erze, Rohes Erz und Speicherblöcke. Hinter die Stahlstraße gestellt, landen Stahl aus Immersive Engineering und Stahl aus Mekanism als eine Sorte in der Kiste.",
          ],
          tasks=[task_item("mekanism:oredictionificator", 1)],
          rewards=[reward_item("mekanism:basic_control_circuit", 2), reward_xp(5)],
          deps=["sorter"], icon="mekanism:oredictionificator", optional=True),

    quest("assemblicator", 7.5, 25, "&3Lass den Formelfertigungsfabrikator craften",
          subtitle="Die erste Autocrafting-Maschine von Mekanism.",
          description=[
              "Stahl, ein Crafter, Schaltkreise, ein Stahlgehäuse und eine Truhe. Eine &6Fertigungsformel&r (Papier und Schaltkreis) speichert ein Rezept.",
              "",
              "Leg das Rezept ins Raster, die Formel in ihren Slot, und er craftet mit Strom aus seinem Vorrat, so lange Zutaten nachkommen. Ideal für Stahlgehäuse am laufenden Band.",
          ],
          tasks=[task_item("mekanism:formulaic_assemblicator", 1), task_item("mekanism:crafting_formula", 1)],
          rewards=[reward_item("minecraft:paper", 16), reward_xp(5)],
          deps=["factory"], optional=True),

    quest("ore_line", 16, 23.5, "&5&lBau die Stahlstraße",
          subtitle="Eisen rein, Stahl raus, ohne Handgriff.",
          description=[
              "Kiste mit Eisen, Transporter zur &6Infusionsfabrik&r mit Kohlenstoff (Angereichertes Eisen), weiter zur zweiten Infusionsfabrik (Stahlstaub), weiter zur Schmelzfabrik, dann in die Kiste. Überall Auto-Auswurf, Strom über Kabel.",
              "",
              "Eine Anreicherungskammer davor macht Kohle zu Angereichertem Kohlenstoff. Das Eisen liefert die Erzstraße aus dem Kapitel &5Mekanism: Erz Schritt für Schritt&r.",
              "",
              "&eKronwerke:&r Stell eine Kiste an den Obelisken und häng sie hinten an. Was hineinfällt, zählt für dich zu den 4 000 Stahlbarren von Stufe 3.",
          ],
          tasks=[task_item("mekanism:basic_infusing_factory", 2), task_item("mekanism:ingot_steel", 64)],
          rewards=[reward_table("s2_rare"), reward_item("mekanism:basic_control_circuit", 4), reward_xp(20)],
          deps=["factory", "enriched_carbon"], icon="mekanism:ingot_steel", size=2.5, shape="gear"),

    quest("outlook", 19, 23.5, "&dSchau auf Stufe 3",
          subtitle="Was hinter dem Stahlziel wartet.",
          description=[
              "Mit Stufe 3 öffnet das Kapitel &5Mekanism: Fortgeschritten&r: Fortgeschrittener Schaltkreis (mit Gedrucktem Silizium aus AE2), Teleporter, Digitaler Miner, Industrieturbine, Wärmeverdampfung und die fortschrittliche Stufe.",
              "",
              "Das Ziel von Stufe 3 will Stahl, Fortgeschrittene Schaltkreise und Stahlkerne. Jede Stahlstraße, die jetzt läuft, bringt den Server hin.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(10)],
          deps=["ore_line"], icon="mekanism:steel_casing", optional=True),
]

images = [
    head("title", "Mekanism", 0, -4, height=1.75, kind="title"),
    head("osmium", "Osmium und Mana", 0, -1.8, colour="magic"),
    head("steel", "Legierungen und Stahl", 7.5, -1.8, colour="stone"),
    head("machines", "Grundmaschinen", 0, 5.6, colour="brass"),
    head("power", "Energie", 8, 5.6, colour="fire"),
    head("fluids", "Flüssigkeiten und Gase", 0, 11.2, colour="water"),
    head("gases", "Jedes Gas", 13, 11.2, colour="water"),
    head("upgrades", "Upgrades", 0, 17.4, colour="stone"),
    head("logistics", "Logistik und Ausbau", 0, 20.6, colour="brass"),
]

chapter(C, "Mekanism", "mekanism:metallurgic_infuser", "tech", quests, shape="square", order=10, stage=2,
        subtitle=["Stufe 2: Osmium, Stahl, Generatoren, Tanks, Gase und die ersten Fabriken."], images=images)
