"""Oritech in stage 3: nickel, steel and electrum, coils, motors and plating, the basic
generator, machine cores and pipes, the pulverizer, powered furnace, foundry, centrifuge and
plastic, the assembler, the enderic laser, the atomic forge and the frame machines, the ore
line through the fragment forge (clumps, centrifuge gems, foundry 2 gems to 3 ingots), one
quest per machine addon, the jetpack, the exo armour and the augments, and the nuclear
reactor. Kronwerke removes the foundry netherite and brass, the atomic forge control circuits
and the laser certus charging (kubejs/server_scripts/kronwerke/). Numbers come from the
Oritech 1.2.12 jar (recipes, the in-jar wiki) and config/oritech-common.toml."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp, banner)

C = "oritech"


def addon(name, x, y, title, subtitle, recipe, effect, item, reward, extra=None):
    """One checklist quest per machine addon: recipe line, effect line, one tick."""
    desc = [recipe, "", effect]
    if extra:
        desc += ["", extra]
    return quest(name, x, y, title, subtitle=subtitle, description=desc,
                 tasks=[task_item(item, 1)], rewards=reward, deps=["addons"], icon=item)


quests = [
    # ---- Nickel und Stahl ----------------------------------------------------
    quest("nickel", 0, 1, "&6&lGrab Nickel",
          subtitle="Das Metall, aus dem Oritech gebaut ist.",
          description=[
              "Grab &616 Rohes Nickel&r aus. Nickelerz liegt zwischen &eY 40&r und dem Grund der Welt, am dichtesten um &eY -12&r. Schmilz es im Ofen zu &6Nickelbarren&r.",
              "",
              "&6Oritech&r öffnet mit Stufe 3: Maschinen aus Stahl und Nickel, Laser, Rahmenmaschinen, ein Reaktor und am Ende Umbauten am eigenen Körper.",
              "",
              "&eGut zu wissen:&r Nickel aus Immersive Engineering zählt in jedem Oritech-Rezept genauso.",
          ],
          tasks=[task_item("oritech:raw_nickel", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s3_common")],
          icon="oritech:nickel_ingot", size=2.0, shape="hexagon"),

    quest("steel", 2.5, 0, "&8Mach Stahl an der Werkbank",
          subtitle="Zwei Eisen, zwei Kohle, ein Barren.",
          description=[
              "&6Eisenbarren&r oben, &6Kohle&r oder Holzkohle unten, je zwei: das gibt einen &6Stahlbarren&r.",
              "",
              "Das ist teuer. Die &6Gießerei&r macht später aus einem Eisen und einem Kohlestaub einen Barren. Alle Oritech-Rezepte nehmen jeden Stahl, auch den aus Mekanism.",
              "",
              "&eKronwerke:&r Jeder Stahlbarren zählt am Obelisken für &6Der Ofen schläft nie&r.",
          ],
          tasks=[task_item("oritech:steel_ingot", 16)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["nickel"], icon="oritech:steel_ingot"),

    quest("electrum", 2.5, 2, "&eMach Electrum",
          subtitle="Gold und Redstone werden ein Leiter.",
          description=[
              "Zwei &6Goldbarren&r oben, zwei &6Redstone&r unten ergeben einen &6Electrum Ingot&r. Die Gießerei und der erhitzte Mixer von Create machen ihn aus je einem Gold und einem Redstone.",
              "",
              "Electrum steckt in Energierohren, Gießerei, angetriebenem Ofen, Verarbeitungseinheit und Laser.",
          ],
          tasks=[task_item("oritech:electrum_ingot", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:redstone", 16)],
          deps=["nickel"]),

    quest("coils", 5, 0, "&bWickel Magnetspulen",
          subtitle="Vier Spulen aus Nickel und Stahl.",
          description=[
              "Drei &6Nickel&r oben, drei &6Stahl&r in der Mitte, drei Nickel unten ergeben &evier&r &6Magnetspulen&r.",
              "",
              "Spulen stecken im Motor, im Generator, im Ofen und in vielen Addons. Der Zusammenfüger macht später sechs aus einem Stahl, zwei Nickel und einem Kupfer.",
          ],
          tasks=[task_item("oritech:magnetic_coil", 8)],
          rewards=[reward_item("oritech:nickel_ingot", 4)],
          deps=["steel"], icon="oritech:magnetic_coil"),

    quest("plating", 5, 2, "&7Press Kupferverstärkte Platten",
          subtitle="Die Außenhaut fast jeder Maschine.",
          description=[
              "&6Stein&r in die Ecken, &6Stahl&r an die Seiten, ein &6Kupferbarren&r in die Mitte ergeben zwei &6Kupferverstärkte Platten&r.",
              "",
              "Platten tragen fast jede Maschine, jedes Addon und die Exo-Rüstung. Der Zusammenfüger macht aus zwei Stahl, einem Kupfer und einer Plastik Platte gleich acht.",
          ],
          tasks=[task_item("oritech:machine_plating_block", 8)],
          rewards=[reward_item("minecraft:copper_ingot", 16)],
          deps=["steel"], icon="oritech:machine_plating_block"),

    quest("motor", 7.5, 0, "&bBau Motoren",
          subtitle="Was sich bewegt, braucht einen Motor.",
          description=[
              "Ein &6Nickel&r oben in der Mitte, darunter zweimal &6Stahl&r, &6Magnetspule&r, Stahl ergibt einen &6Motor&r.",
              "",
              "Pulverizer, Gießerei, Zusammenfüger, Laser und Rahmenmaschinen brauchen je zwei. Im Zusammenfüger gibt es zwei Motoren aus Nickel, Stahl und zwei Spulen.",
          ],
          tasks=[task_item("oritech:motor", 4)],
          rewards=[reward_item("oritech:magnetic_coil", 4), reward_xp(5)],
          deps=["coils"], icon="oritech:motor"),

    # ---- Strom und Kerne -----------------------------------------------------
    quest("generator", 2.5, 5, "&c&lStell einen Grundlegenden Generator auf",
          subtitle="Kohle rein, 32 RF pro Tick raus.",
          description=[
              "&6Nickel&r oben und an den Seiten, ein &6Kupferbarren&r in die Mitte, unten &6Magnetspule&r, &6Ofen&r, Magnetspule.",
              "",
              "Er verbrennt alles, was im Ofen brennt, macht &e32 RF/t&r und puffert 50 000 RF. Er braucht keine Kerne und nimmt keine Addons. Zwei oder drei davon tragen Pulverizer, Ofen und Gießerei.",
          ],
          tasks=[task_item("oritech:basic_generator_block", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_table("s3_common"), reward_xp(5)],
          deps=["coils"], icon="oritech:basic_generator_block", size=1.5, shape="hexagon"),

    quest("cores", 5, 5, "&7Bau Maschinenkerne",
          subtitle="Ohne Kerne kein Multiblock.",
          description=[
              "&6Primitiver Kern:&r acht Bretter um eine Werkbank. &6Einfacher Kern:&r Kupfer oder Eisen um Lapis. &6Erweiterter Kern:&r Kohlefaser oder Nickel um Redstone.",
              "",
              "Große Maschinen wollen Kerne direkt um sich: Ofen, Zentrifuge und Laser einen, Gießerei und Zusammenfüger drei, Fragment Forge sieben, Atomic Forge acht. Fehlt einer, sagt die Maschine das.",
              "",
              "Die Güte der Kerne entscheidet, wie viele &6Addon Extender&r eine Maschine verträgt. Der Tooltip der Maschine nennt Kerne und Addon-Plätze.",
          ],
          tasks=[task_item("oritech:machine_core_1", 8), task_item("oritech:machine_core_2", 2)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["generator"], icon="oritech:machine_core_2"),

    quest("pipes", 2.5, 7, "&9Leg Rohre",
          subtitle="Strom, Gegenstände, Flüssigkeiten.",
          description=[
              "&6Energierohr:&r drei Electrum in einer Reihe, gibt sechs. &6Item Pipe:&r Bretter oben und unten, Nickel in der Mitte, gibt sechs. &6Flüssigkeitsrohr:&r Kupfer oben und unten, Silizium in der Mitte.",
              "",
              "Rechtsklick auf die Verbindung zu einer Kiste schaltet Herausziehen ein: &e8 Gegenstände alle 5 Ticks&r aus dem ersten belegten Slot. Ein &6Motor&r, per Rechtsklick ins Rohr gesetzt, zieht aus allen Slots.",
              "",
              "Energierohre tragen &e10 000 RF/t&r. Der &6Pipe Wrench&r (Stahl und Nickel) trennt einzelne Seiten.",
          ],
          tasks=[task_item("oritech:energy_pipe", 12), task_item("oritech:item_pipe", 12), task_item("oritech:wrench", 1)],
          rewards=[reward_item("oritech:electrum_ingot", 4)],
          deps=["generator", "electrum"], icon="oritech:energy_pipe"),

    # ---- Verarbeitung --------------------------------------------------------
    quest("pulverizer", 10, 0, "&7&lBau einen Pulverizer",
          subtitle="Der erste Schritt der Erzstraße.",
          description=[
              "&6Eisen&r oben und an den Seiten, &6Nickel&r in die Mitte, unten &6Motor&r, &6Kupferblock&r, Motor. Er zieht &e32 RF/t&r.",
              "",
              "Ein Rohes Eisen wird ein &6Eisenstaub&r und drei kleine, neun kleine ergeben einen ganzen: rund &e1,33 Barren&r statt einem. Ein Erzblock wird zwei Rohe Erze.",
              "",
              "Aus Kohle wird &6Kohlestaub&r, aus Quarz &6Quarzstaub&r, aus einer Enderperle acht &6Enderic Compound&r. Alle drei brauchst du gleich.",
          ],
          tasks=[task_item("oritech:pulverizer_block", 1), task_item("oritech:coal_dust", 16)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["motor", "generator"], icon="oritech:pulverizer_block", size=1.5, shape="hexagon"),

    quest("furnace", 12.5, -1, "&6Bau einen Angetriebenen Ofen",
          subtitle="Ein Ofen mit Strom statt Kohle.",
          description=[
              "Zuerst &6Silizium&r: zwei Quarzstaub und zwei Sand ergeben drei &6Rohes Silizium&r, im Ofen wird daraus Silizium. Ofen: Kupfer oben, Silizium links und rechts, Electrum in der Mitte, unten Spule, Ofen, Spule.",
              "",
              "Er schmilzt mit &e32 RF/t&r alles, was ein Ofen schmilzt, und braucht einen Maschinenkern.",
          ],
          tasks=[task_item("oritech:powered_furnace_block", 1), task_item("oritech:silicon", 8)],
          rewards=[reward_item("minecraft:sand", 32), reward_item("minecraft:quartz", 16)],
          deps=["pulverizer"], icon="oritech:powered_furnace_block"),

    quest("foundry", 12.5, 1, "&c&lBau eine Gießerei",
          subtitle="Zwei Zutaten, ein Barren, halber Preis.",
          description=[
              "&6Kupfer&r oben und an den Seiten, ein &6Motor&r in die Mitte, unten &6Electrum&r, &6Kessel&r, Electrum. Drei Kerne, &e128 RF/t&r.",
              "",
              "Ein Eisen und ein Kohlestaub geben &6Stahl&r, ein Gold und ein Redstone &6Electrum&r, ein Diamant und ein Nickel einen &6Adamant Barren&r (an der Werkbank je zwei).",
              "",
              "&eRezept auf Kronwerke:&r &6Netherit&r macht die Gießerei nicht, das bleibt beim Schmiedetisch. &6Messing&r auch nicht, das kommt nur aus dem Mixer von Create.",
              "",
              "&eKronwerke:&r Pulverizer für Kohlestaub, Gießerei dahinter, Kiste am Obelisken: fertig ist die kleine Stahlstraße.",
          ],
          tasks=[task_item("oritech:foundry_block", 1), task_item("oritech:adamant_ingot", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["pulverizer"], icon="oritech:foundry_block", size=1.5, shape="hexagon"),

    quest("centrifuge", 15, -1, "&dBau eine Zentrifuge",
          subtitle="Kohlestaub wird Kohlefaser.",
          description=[
              "Erste Zentrifuge ohne Verarbeitungseinheit: drei &6Glasflaschen&r oben, &6Kupfer&r links und rechts, ein &6Motor&r in der Mitte, unten Eisenblock, Motor, Eisenblock.",
              "",
              "Ein &6Kohlestaub&r wird &6Carbon Fibre Strands&r. Kohlefaser brauchst du für Verarbeitungseinheit, Laser und die besseren Kerne.",
          ],
          tasks=[task_item("oritech:centrifuge_block", 1), task_item("oritech:carbon_fibre_strands", 16)],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          deps=["furnace"], icon="oritech:centrifuge_block"),

    quest("plastic", 17.5, -1, "&dMach Plastik aus Weizen",
          subtitle="Fluid Addon, Wasser, ein Weizenfeld.",
          description=[
              "Setz ein &6Fluid Addon&r an die Zentrifuge (fünf Kohlefaser, ein Flüssigkeitsrohr, zwei Electrum, ein Silizium) und pump Wasser in die Zentrifuge selbst.",
              "",
              "Vier Weizen ergeben &6Packed Wheat&r. Mit &e250 mB&r Wasser wird er &6Raw Biopolymer&r, das mit &e500 mB&r Wasser eine &6Plastik Platte&r.",
              "",
              "Startet das Rezept nicht, öffne die Zentrifuge einmal nach dem Anbauen des Addons.",
          ],
          tasks=[task_item("oritech:machine_fluid_addon", 1), task_item("oritech:plastic_sheet", 16)],
          rewards=[reward_item("minecraft:wheat", 64), reward_xp(10)],
          deps=["centrifuge"], icon="oritech:plastic_sheet"),

    quest("assembler", 17.5, 1, "&9&lBau einen Zusammenfüger",
          subtitle="Vier Zutaten, ein Bauteil.",
          description=[
              "&6Kupfer&r oben, zwei &6Werker&r links und rechts, ein &6Adamant Barren&r in der Mitte, unten Motor, Hochofen, Motor. Drei Kerne, &e128 RF/t&r.",
              "",
              "Sein wichtigstes Produkt ist die &6Verarbeitungseinheit&r: Plastik, Kohlefaser, Electrum und Redstone. Die Reihenfolge in den Slots ist egal, Musteranbieter von AE2 gehen direkt.",
              "",
              "Spulen, Motoren und Platten werden hier deutlich billiger als an der Werkbank.",
          ],
          tasks=[task_item("oritech:assembler_block", 1), task_item("oritech:processing_unit", 4)],
          rewards=[reward_item("oritech:plastic_sheet", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["foundry", "plastic"], icon="oritech:assembler_block", size=1.5, shape="hexagon"),

    # ---- Laser ---------------------------------------------------------------
    quest("laser", 20.5, 1, "&5&lBau den Enderischen Laser",
          subtitle="Ein Strahl, der abbaut und Strom bringt.",
          description=[
              "&6Enderische Linse&r im Zusammenfüger: Adamant, Kohlefaser, zwei Enderic Compound. Laser: Kohlefaser, Linse, Kohlefaser oben, Motor, Electrum, Motor, unten drei Platten.",
              "",
              "Rechtsklick mit dem &6Target Designator&r auf einen Block speichert ihn, &eShift&r-Rechtsklick auf den Laser gibt ihm die Richtung. Er feuert bis &e128 Blöcke&r weit und baut alles in dieser Richtung ab, Glas durchdringt er.",
              "",
              "Auf &6Amethysthaufen&r gerichtet macht er &dFluxite&r, auf Maschinen gerichtet lädt er sie. Was nicht in sein Inventar passt, ist weg: Rohr dran.",
              "",
              "&eRezept auf Kronwerke:&r Zertifizierten Quarz lädt der Laser nicht. Das machen Ars Nouveau und die Energizing Orb von Powah.",
          ],
          tasks=[task_item("oritech:laser_arm_block", 1), task_item("oritech:target_designator", 1), task_item("oritech:fluxite", 8)],
          rewards=[reward_item("minecraft:amethyst_block", 8), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["assembler"], icon="oritech:laser_arm_block", size=2.0, shape="gear"),

    quest("atomic_forge", 23, 1, "&5Speis eine Atomic Forge",
          subtitle="Nur ein Laser kann sie laden.",
          description=[
              "&6Flux Gate&r, &6Duratium&r, Flux Gate oben, &6Plastik&r, &6Enderic Compound&r, Plastik in der Mitte, drei Platten unten. Acht Kerne drumherum, Strom &enur per Laser&r.",
              "",
              "&6Duratium&r gießt die Gießerei aus Platin und einem Netheritbarren. Die Forge macht &6Silicon Wafer&r, Uran-Gems für den Reaktor, Duratium und Reinforced Deepslate.",
              "",
              "&eRezept auf Kronwerke:&r Steuerschaltkreise von Mekanism macht sie nicht. Die gibt es nur auf dem Weg aus dem Kapitel Mekanism.",
          ],
          tasks=[task_item("oritech:atomic_forge_block", 1)],
          rewards=[reward_item("oritech:fluxite", 8), reward_xp(10)],
          deps=["laser", "fragment_forge"], icon="oritech:atomic_forge_block"),

    quest("destroyer", 23, 3.2, "&7Spann einen Rahmen mit Zerstörer",
          subtitle="Ein Arm fährt über die Fläche.",
          description=[
              "&6Maschinen-Rahmen:&r vier Eisengitter um zwei Nickel, gibt sechzehn. Leg damit ein &eleeres Rechteck&r bis &e64 Blöcke&r Seitenlänge. &6Zerstörer Block&r: Motor, Laser, Motor oben, Motor, Pulverizer, Motor, unten drei Platten.",
              "",
              "Setz den Zerstörer an den Rahmen, auch an eine Ecke. Sein Arm baut die Schicht &eunter&r dem Rahmen ab. &6Platzierer&r und &6Dünger Block&r arbeiten auf demselben Rahmen mit.",
              "",
              "Mit Ernte-Filter wird das eine Farm, mit Mine-Add-On ein Steinbruch. Beide stehen unten bei den Addons.",
          ],
          tasks=[task_item("oritech:machine_frame_block", 16), task_item("oritech:destroyer_block", 1)],
          rewards=[reward_item("oritech:motor", 2), reward_xp(5)],
          deps=["laser"], icon="oritech:destroyer_block"),

    # ---- Erzstraße -----------------------------------------------------------
    quest("platinum", 12.5, 5, "&fGrab Platin",
          subtitle="Tief unten, für das Flux Gate.",
          description=[
              "Platinerz liegt zwischen &eY -20&r und &eY -60&r. Grab &616 Rohes Platin&r und schmilz es zu Barren.",
              "",
              "Platin steckt im &6Flux Gate&r (Zusammenfüger: Verarbeitungseinheit, zwei Fluxite, ein Platinbarren) und in Duratium. Mit Flux Gates beginnt die zweite Hälfte von Oritech.",
          ],
          tasks=[task_item("oritech:raw_platinum", 16)],
          rewards=[reward_item("minecraft:raw_iron", 16)],
          deps=["pulverizer"], icon="oritech:platinum_ingot"),

    quest("fragment_forge", 15, 5, "&6&lBau die Fragment Forge",
          subtitle="Die beste Mühle von Oritech.",
          description=[
              "Fünf &6Plastik&r, ein &6Flux Gate&r in der Mitte, unten Motor, Platte, Motor. Sie braucht &esieben Kerne&r und zieht &e256 RF/t&r.",
              "",
              "Ein Erzblock wird zwei Rohe Erze und ein Rohes Erz einer Nebensorte, bei Eisen ein Rohes Nickel. Rohes Erz wird zu &6Clumps&r, das ist der nächste Schritt.",
          ],
          tasks=[task_item("oritech:flux_gate", 1), task_item("oritech:fragment_forge_block", 1)],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["platinum", "laser"], icon="oritech:fragment_forge_block", size=1.5, shape="hexagon"),

    quest("clumps", 17.5, 5, "&7Zerleg Rohes Eisen in Clumps",
          subtitle="Ein Clump, drei kleine, Nickel dazu.",
          description=[
              "Leg &6Rohes Eisen&r in die Fragment Forge. Jedes wird ein &6Iron Clump&r, drei &6Small Iron Clumps&r und drei kleine Nickel-Clumps. Neun kleine ergeben an der Werkbank einen ganzen.",
              "",
              "Mit einem &6Yield Addon&r an der Forge verdoppeln sich die Nebenprodukte, also das Nickel.",
          ],
          tasks=[task_item("oritech:iron_clump", 32)],
          rewards=[reward_item("minecraft:raw_iron", 48), reward_xp(10)],
          deps=["fragment_forge"], icon="oritech:iron_clump"),

    quest("fragment", 20.5, 5, "&6&lSchließ die Erzstraße",
          subtitle="Zwei Barren aus jedem Rohen Eisen.",
          description=[
              "Clumps in die &6Zentrifuge&r: ein Clump wird ein &6Iron Gem&r und drei kleine Nickelstäube, ganz ohne Wasser. Zwei Gems in der &6Gießerei&r werden &edrei&r Eisenbarren, im erhitzten Mixer von Create ebenso.",
              "",
              "Unterm Strich gibt ein Rohes Eisen hier &e2 Barren&r, im Pulverizer 1,33, im Ofen 1. Dazu Nickel nebenbei. Gold, Kupfer, Nickel und Platin laufen genauso.",
              "",
              "&eKronwerke:&r Mehr Eisen heißt mehr Stahl für &6Der Ofen schläft nie&r. Häng eine Gießerei mit Kohlestaub dahinter, dann wird die Erzstraße zur Stahlstraße.",
          ],
          tasks=[task_item("oritech:iron_gem", 64)],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:raw_iron", 64), reward_xp(20)],
          deps=["clumps"], icon="oritech:iron_gem", size=2.5, shape="gear"),

    # ---- Addons ---------------------------------------------------------------
    quest("addons", 0, 12, "&a&lSetz ein Speed Addon an",
          subtitle="Schneller arbeiten, mehr Strom ziehen.",
          description=[
              "Fünf &6Plastik&r, ein &6Stahl&r in der Mitte, unten Spule, Platte, Spule. Stell das Addon an einen &eAddon-Platz&r der Maschine, die Plätze nennt der Tooltip.",
              "",
              "Ein Speed Addon gibt &e+50 Prozent Tempo&r und &e20 Prozent mehr Verbrauch&r. Auf diesem Server werden Addons addiert: zwei geben +100 Prozent.",
              "",
              "Rechts stehen alle Addon-Sorten, eine pro Quest. Jede ist ein Häkchen für sich.",
          ],
          tasks=[task_item("oritech:machine_speed_addon", 1)],
          rewards=[reward_item("oritech:plastic_sheet", 8), reward_xp(5)],
          deps=["assembler"], icon="oritech:machine_speed_addon", size=1.5, shape="hexagon"),

    addon("addon_efficiency", 2.5, 10, "&aSpar Strom mit dem Efficiency Addon", "20 Prozent weniger Verbrauch.",
          "Fünf &6Plastik&r, ein &6Electrum&r in der Mitte, unten Kohlefaser, Platte, Kohlefaser.",
          "Jedes senkt den Verbrauch um &e20 Prozent&r, ohne die Maschine langsamer zu machen. Passt gut zu Speed Addons.",
          "oritech:machine_efficiency_addon", [reward_item("oritech:electrum_ingot", 2)]),
    addon("addon_capacitor", 5, 10, "&aVergrößer den Puffer", "Capacitor Addon, 2 Millionen RF mehr.",
          "Fünf &6Plastik&r, eine &6Magnetspule&r in der Mitte, unten Energite, Platte, Energite. &6Energite&r gießt die Gießerei aus Nickel und Fluxite.",
          "Jedes gibt &e2 000 000 RF&r Speicher und &e2 000 RF/t&r mehr Eingang. Für Maschinen mit vielen Speed Addons.",
          "oritech:machine_capacitor_addon", [reward_item("oritech:fluxite", 2)]),
    addon("addon_acceptor", 7.5, 10, "&aLeg einen zweiten Stromeingang", "Acceptor Addon.",
          "Fünf &6Plastik&r, ein &6Energite&r in der Mitte, unten Electrum, Platte, Electrum.",
          "Strom geht direkt ins Addon statt in die Maschine: &e500 000 RF&r Puffer, &e5 000 RF/t&r Eingang. Wenn die Maschinenseiten schon belegt sind.",
          "oritech:machine_acceptor_addon", [reward_item("oritech:electrum_ingot", 2)]),
    addon("addon_burst", 10, 10, "&aDreh kurz auf mit dem Burst Addon", "Achtfaches Tempo, 12 Sekunden lang.",
          "&6Redstone&r, &6Stahl&r, Redstone oben, Electrum, &6Metal Girder&r, Electrum in der Mitte, drei Platten unten.",
          "Die Maschine läuft &eachtmal so schnell&r, bis das Burst-Maß leer ist, je Addon 12 Sekunden. Danach läuft sie gedrosselt, bis sie abgekühlt ist. Gut für Stoßarbeit, schlecht für Dauerbetrieb.",
          "oritech:machine_burst_addon", [reward_item("minecraft:redstone", 16)]),
    addon("addon_yield", 12.5, 10, "&aHol mehr heraus mit dem Yield Addon", "Glück für Laser und Zerstörer.",
          "Fünf &6Plastik&r, eine &6Enderische Linse&r in der Mitte, unten Electrum, Platte, Electrum.",
          "An der Fragment Forge verdoppelt es die Nebenprodukte (nur eins geht dort). An Zerstörer und Laser wirkt es wie Glück, &edrei&r sind das Maximum.",
          "oritech:machine_yield_addon", [reward_item("minecraft:raw_iron", 16)]),
    addon("addon_quarry", 2.5, 12, "&aMach einen Steinbruch mit dem Mine-Add-On", "Achtmal so tief graben.",
          "Fünf &6Plastik&r, eine &6Diamantspitzhacke&r in der Mitte, unten Motor, Platte, Motor.",
          "Am Zerstörer mal acht in die Tiefe: ein Addon 8 Blöcke, zwei 64, drei 512. Am Laser wird der Strahl je Addon einen Block breiter. Nimm Speed und Efficiency dazu, sonst ist es langsam.",
          "oritech:quarry_addon", [reward_item("minecraft:diamond", 1)]),
    addon("addon_silk", 5, 12, "&aBau mit Behutsamkeit ab", "Silk Touch Addon.",
          "Fünf &6Plastik&r, eine &6Diamantspitzhacke&r in der Mitte, unten Wolle, Platte, Wolle.",
          "Zerstörer und Laser bauen Blöcke als sie selbst ab. Mit einem Yield Addon zusammen gewinnt Behutsamkeit.",
          "oritech:machine_silk_touch_addon", [reward_item("minecraft:white_wool", 8)]),
    addon("addon_crop", 7.5, 12, "&aErnte nur Reifes mit dem Ernte-Filter", "Aus dem Zerstörer wird eine Farm.",
          "Fünf &6Kohlefaser&r, eine &6Verarbeitungseinheit&r in der Mitte, unten Motor, Platte, Motor.",
          "Zerstörer und Laser überspringen unreife Pflanzen, der Laser mit Hunter Addon auch Jungtiere. Ein Rahmen über dem Feld, ein Platzierer für die Saat: fertige Farm.",
          "oritech:crop_filter_addon", [reward_item("minecraft:wheat_seeds", 16)]),
    addon("addon_hunter", 10, 12, "&aMach den Laser zur Waffe", "Hunter Addon.",
          "Fünf &6Plastik&r, ein &6Eisenschwert&r in der Mitte, unten Motor, Platte, Motor.",
          "Der Laser zielt auf Mobs statt Blöcke. &eShift&r-Rechtsklick mit dem Designator wechselt: alle Mobs, feindlich und neutral, nur feindlich. Beute landet im Laser, Erfahrung nicht.",
          "oritech:machine_hunter_addon", [reward_item("minecraft:iron_sword", 1)]),
    addon("addon_redstone", 12.5, 12, "&aSteuer per Redstone", "Control Unit Addon.",
          "Fünf &6Redstone&r, ein &6Komparator&r in der Mitte, unten Verstärker, Platte, Verstärker.",
          "Rechtsklick öffnet die Einstellung: Redstone am Addon schaltet die Maschine ab, ein Komparator liest Strom, Inventar oder Fortschritt. Der Laser kann Redstone schon von selbst.",
          "oritech:machine_redstone_addon", [reward_item("minecraft:redstone", 16)]),
    addon("addon_proxy", 2.5, 14, "&aGib einem Slot einen eigenen Zugang", "Inventory Proxy Addon.",
          "Fünf &6Kohlefaser&r, eine &6Verarbeitungseinheit&r in der Mitte, unten Truhe, Motor, Truhe.",
          "Du wählst einen Slot der Maschine, und alles, was ins Addon geht oder herauskommt, betrifft nur diesen Slot. Praktisch am Zusammenfüger.",
          "oritech:machine_inventory_proxy_addon", [reward_item("minecraft:chest", 4)]),
    addon("addon_steam", 5, 14, "&aKoch Dampf statt Strom", "Steam Boiler Addon.",
          "Fünf &6Flüssigkeitsrohre&r, ein &6Kupferbarren&r in der Mitte, unten Adamant, Platte, Adamant.",
          "Am Generator verbrennt er Brennstoff mit Wasser zu Dampf. Die &6Steam Engine&r (Generator, Spule, Electrum, Kupfer) macht daraus wieder Strom, eins zu eins.",
          "oritech:steam_boiler_addon", [reward_item("minecraft:water_bucket", 1)]),
    addon("addon_processing", 7.5, 14, "&aRechne doppelt mit der Hilfskammer", "Auxiliary Processing Chamber.",
          "Motor, &6Electrum&r, Motor oben, &6Unheilige Intelligenz&r, Komparator, Unheilige Intelligenz in der Mitte, drei Platten unten.",
          "Jede Kammer lässt die Maschine ein Rezept mehr gleichzeitig verarbeiten, für &e50 Prozent&r mehr Verbrauch. Bei langen Rezepten besser als Speed.",
          "oritech:machine_processing_addon", [reward_item("oritech:processing_unit", 2)],
          "&eKronwerke:&r Die Unheilige Intelligenz bindet der &6Seelenbinder&r von Ender IO: ein Dubioser Behälter mit der Seele eines Allays, Phantoms oder Plagegeists."),
    addon("addon_extender", 10, 14, "&aErweiter die Addon-Plätze", "Machine Addon Extender.",
          "Vier &6Einfache Maschinenkerne&r in die Ecken, &6Platten&r an die Seiten, ein &6Duratium&r in die Mitte.",
          "Der Extender sitzt an der Maschine oder an einem anderen Extender und gibt neue Plätze. Wie viele gehen, sagt die Güte der Kerne, sichtbar oben links im Fenster.",
          "oritech:machine_extender", [reward_item("oritech:machine_core_2", 2)]),

    # ---- Ausrüstung ----------------------------------------------------------
    quest("jetpack", 15.5, 11, "&eFlieg mit dem Jetpack",
          subtitle="Halte Springen, und du steigst.",
          description=[
              "Leder oben, drei &6Stahl&r in der Mitte, unten &6Lohenstaub&r, &6Redstoneblock&r, Lohenstaub. Es fasst &e100 000 RF&r und braucht &e128 RF/t&r unter Schub.",
              "",
              "Laden geht im &6Ausrüstungsladegerät&r (Stahl, Spender, Redstoneblock, Energierohre, Truhe). Dort tankst du auch &6Turbofuel&r, damit fliegt es schneller. Schweben gibt es nicht.",
              "",
              "Mit Elytra, zwei Verarbeitungseinheiten und fünf Schwarzpulver wird es zur &6Boosted Elytra&r, die beim Gleiten schiebt.",
          ],
          tasks=[task_item("oritech:jetpack", 1)],
          rewards=[reward_item("minecraft:blaze_powder", 8), reward_xp(10)],
          deps=["plastic"], icon="oritech:jetpack"),

    quest("exo", 18, 11, "&eZieh die Exo-Rüstung an",
          subtitle="Nachtsicht, Tempo, kein Fallschaden.",
          description=[
              "Alle vier Teile sind &6Platten&r in Rüstungsform. Helm mit &6Enderischer Linse&r, Hose mit &6Motor&r, Stiefel mit &6Silizium&r, Brust mit &6Fortgeschrittener Batterie&r (Electrum oben, darunter zweimal Stahl, Energite, Stahl).",
              "",
              "Helm Nachtsicht, Hose schneller laufen, Stiefel kein Fallschaden. Die Brust fasst &e5 Millionen RF&r und lädt deine Stromwerkzeuge im Inventar.",
              "",
              "Das &6Exo Jetpack&r (Ion Thruster, Brustplatte, Jetpack, kleine Tanks) fasst 5 Millionen RF und fliegt viel schneller. Siehe auch die Checkliste &eAusrüstung&r.",
          ],
          tasks=[task_item("oritech:exo_helmet", 1), task_item("oritech:exo_chestplate", 1),
                 task_item("oritech:exo_leggings", 1), task_item("oritech:exo_boots", 1)],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["jetpack", "laser"], icon="oritech:exo_chestplate"),

    quest("augments", 20.5, 11, "&dBau dich selbst um",
          subtitle="Drei Herzen mehr, aus Platten und Biostahl.",
          description=[
              "&6Cybernetic Augmentation Center:&r Dubioser Behälter, Kohlefaser, Dubioser Behälter, Motor, Truhe, Motor, drei Platten, zehn Kerne. Daneben die &6Cybernetic Research Station&r (fünf Electrum, Redstoneblock, Braustand, Platten).",
              "",
              "&6Steel-Infused Frame&r: drei Herzen mehr. Forschung 64 Platten, 32 Kohlestaub, 8 Biostahl, 10 Millionen RF, Einbau 8 Platten. &6Synthetic Muscles&r: 25 Prozent schneller, 16 Motoren, 32 Biostahl, 64 Redstone, 30 Millionen RF.",
              "",
              "&6Biostahl&r gießt die Gießerei aus Raw Biopolymer und Eisen. Den &6Dubiosen Behälter&r baut die Werkbank aus Plastik, vier Enderic Compound und zwei Adamant.",
          ],
          tasks=[task_item("oritech:augment_application_block", 1), task_item("oritech:simple_augment_station", 1)],
          rewards=[reward_item("oritech:biosteel_ingot", 8), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["exo"], icon="oritech:simple_augment_station", optional=True),

    # ---- Reaktor -------------------------------------------------------------
    quest("uranium", 15.5, 15.3, "&aMach Uranpellets",
          subtitle="Rohes Uran, Gem, Pellet.",
          description=[
              "&6Tiefenschiefer-Uranerz&r sitzt mit &6Uran-Kristallen&r in kleinen Nestern in den untersten 40 Blöcken der Welt. Pulverizer: Rohes Uran wird Uranstaub. Atomic Forge: ein Kupferstaub und zwei Uranstaub werden ein &6Uranium Gem&r.",
              "",
              "Zusammenfüger: zwei Gems, eine Plastik Platte und ein Nickel geben zwei &6Uranium Pellets&r, mit Adamant statt Nickel drei.",
              "",
              "Den Uran-Kristall zerstört der Laser zu Plutoniumstaub. Ein Plutoniumpellet brennt zehnmal so lange wie eins aus Uran.",
          ],
          tasks=[task_item("oritech:raw_uranium", 16), task_item("oritech:uranium_pellet", 8)],
          rewards=[reward_item("oritech:plastic_sheet", 8), reward_xp(10)],
          deps=["atomic_forge"], icon="oritech:uranium_pellet"),

    quest("reactor", 18, 15.3, "&a&lBau einen Kernreaktor",
          subtitle="Ein Kasten, ein Stab, viel Kühlung.",
          description=[
              "&6Reaktorwände&r (Stahl, Platten, Nickel) als Quader, der &6Controller&r in einer Wand, Rechtsklick baut zusammen. Innen &6Stäbe&r (Plastik über zwei Energite), über jedem Stab ein &6Fuel Port&r im Dach, außen ein &6Energy Port&r.",
              "",
              "Stäbe machen Hitze. &6Heat Vents&r ziehen sie ab, &6Heat Absorber&r unter einem &6Coolant Port&r mit Eis kühlen alles um sich. Alle Innenlagen müssen gleich aussehen.",
              "",
              "&cAchtung:&r Über &e2 000 Hitze&r schmilzt er nach 30 Sekunden, der sichere Modus ist auf dem Server aus. Fang mit einem Stab und vier Vents an.",
              "",
              "Jeder Energy Port gibt bis &e25 000 RF/t&r ab, der Puffer fasst 50 Millionen. Den Vergleich mit anderen Kraftwerken zeigt die Checkliste &eStrom&r.",
          ],
          tasks=[task_item("oritech:reactor_controller", 1), task_item("oritech:reactor_wall", 32),
                 task_item("oritech:reactor_rod", 1), task_item("oritech:reactor_vent", 4),
                 task_item("oritech:reactor_fuel_port", 1), task_item("oritech:reactor_energy_port", 1)],
          rewards=[reward_item("oritech:uranium_pellet", 4), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["uranium"], icon="oritech:reactor_controller", size=2.0, shape="hexagon"),
]

images = [
    banner("oritech/title", "Oritech", 11, -4.4, height=1.75, kind="title", colour="fire"),
    banner("oritech/nickel", "Nickel und Stahl", 3.75, -1.6, height=0.9, colour="stone"),
    banner("oritech/power", "Strom und Kerne", 3.75, 3.6, height=0.9, colour="brass"),
    banner("oritech/processing", "Verarbeitung", 13.75, -2.6, height=0.9, colour="brass"),
    banner("oritech/laser", "Laser", 21.75, -0.6, height=0.9, colour="end"),
    banner("oritech/ore", "Erzstraße", 16.5, 3.6, height=0.9, colour="stone"),
    banner("oritech/upgrades", "Addons", 6.25, 8.6, height=0.9, colour="magic"),
    banner("oritech/gear", "Ausrüstung", 18, 9.6, height=0.9, colour="water"),
    banner("oritech/reactor", "Reaktor", 16.75, 13.3, height=0.9, colour="nature"),
]

chapter(C, "Oritech", "oritech:laser_arm_block", "tech", quests, shape="square", order=23, stage=3,
        subtitle=["Stufe 3: Stahl und Nickel, die Erzstraße, der Laser, Addons, Exo-Rüstung und der Reaktor."],
        images=images)
