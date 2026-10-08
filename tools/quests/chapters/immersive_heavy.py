"""Immersive Engineering in stage 3: the engineering blocks open (Kronwerke: brass sheet in
the light block, precision mechanism in the heavy block) and with them every big multiblock,
one quest each with the hammer step, the block count and what goes in and out: crusher, metal
press, squeezer, bottling machine and graphite electrodes, arc furnace, fermenter, refinery
with biodiesel and the duroplast chain, diesel generator with HV wiring, mixer, assembler,
sawmill, automated workbench, excavator with survey tools, lightning rod, radio tower and
resonanz observer, then two checklists of all stage 3 multiblocks with their sizes. Block
counts come from the structure files in the jar, numbers from the recipes and
immersiveengineering-server.toml. Continues the stage 2 chapter."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item, reward_table,
                  reward_xp, banner, img)

C = "immersive_heavy"


def tex(name):
    """An Immersive Engineering item texture by its file name (they differ from the ids)."""
    return img(f"immersiveengineering:textures/item/{name}.png", 32, 32)


def mb(name, title):
    """The advancement IE grants for forming one of its multiblocks."""
    return task_advancement(f"immersiveengineering:multiblocks/{name}", title)


quests = [
    # ---- Bausteine -----------------------------------------------------------
    quest("light", 0, 6.5, "&6&lBau 16 Leichte Ingenieursbausteine",
          subtitle="Der Grundbaustein aller großen Maschinen.",
          description=[
              "Vier &6Eisenblechblöcke&r in die Ecken, vier &6Mechanische Eisenkomponenten&r an die Seiten, ein &6Messingblech&r in die Mitte ergeben vier &6Leichte Ingenieursbausteine&r.",
              "",
              "&eRezept auf Kronwerke:&r Das Messingblech von Create ersetzt den Kupferbarren. Die Bausteine öffnen mit &6Stufe 3&r, und mit ihnen alle großen Multiblöcke.",
              "",
              "Zerkleinerer und Lichtbogenofen brauchen je &e10&r, der Bagger 9. Leg gleich einen Vorrat an. Die Grundlagen aus Stufe 2 stehen im Kapitel &6Immersive Engineering&r.",
          ],
          tasks=[task_item("immersiveengineering:light_engineering", 16)],
          rewards=[reward_item("immersiveengineering:component_iron", 8), reward_table("s3_common")],
          icon="immersiveengineering:light_engineering", size=2.0, shape="hexagon"),

    quest("steel_component", 2.8, 4.3, "&7Bau Mechanische Stahlkomponenten",
          subtitle="Am Ingenieursarbeitstisch.",
          description=[
              "Mit der &6Blaupause Komponenten&r am &6Ingenieursarbeitstisch&r: zwei &6Stahlbleche&r und ein &6Kupferbarren&r ergeben eine &6Mechanische Stahlkomponente&r.",
              "",
              "Drei davon stecken in jedem Satz Schwerer Ingenieursbausteine. Tisch und Blaupause baust du wie im Stufe-2-Kapitel beschrieben.",
              "",
              tex("material_component_steel"),
          ],
          tasks=[task_item("immersiveengineering:component_steel", 6)],
          rewards=[reward_item("immersiveengineering:plate_steel", 8)],
          deps=["light"], icon="immersiveengineering:component_steel"),

    quest("heavy", 2.8, 6.5, "&8&lBau Schwere Ingenieursbausteine",
          subtitle="Stahl, Elektrum und ein Präzisionsmechanismus.",
          description=[
              "&6Stahlblechblöcke&r in die Ecken, oben in der Mitte ein &6Präzisionsmechanismus&r, links, rechts und unten je eine &6Mechanische Stahlkomponente&r, ein &6Elektrumbarren&r in die Mitte. Das ergibt vier.",
              "",
              "&eRezept auf Kronwerke:&r Der Präzisionsmechanismus von Create ersetzt eine Stahlkomponente. Die Metallpresse braucht einen, der Dieselgenerator &e13&r.",
              "",
              "&eKronwerke:&r Jeder &6Stahlkern&r, der Meilenstein von Stufe 3, braucht vier. Acht Stahlkerne will der Obelisk.",
          ],
          tasks=[task_item("immersiveengineering:heavy_engineering", 8)],
          rewards=[reward_item("immersiveengineering:component_steel", 4), reward_item("immersiveengineering:ingot_electrum", 4), reward_xp(10)],
          deps=["steel_component"], icon="immersiveengineering:heavy_engineering", size=1.75, shape="hexagon"),

    quest("parts", 0, 9.5, "&7Bau Redstone-Ingenieursbausteine",
          subtitle="Das Steuerpult jedes Multiblocks.",
          description=[
              "&6Eisenblechblöcke&r in die Ecken, &6Redstone&r an die Seiten, ein &6Kupferbarren&r in die Mitte ergeben vier &6Redstone-Ingenieursbausteine&r.",
              "",
              "Fast jeder große Multiblock hat genau einen. Ein Redstone-Signal daran hält die Maschine an, mit dem Schraubendreher drehst du das um.",
          ],
          tasks=[task_item("immersiveengineering:rs_engineering", 4)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["light"], icon="immersiveengineering:rs_engineering"),

    quest("scaffold", 2.5, 9.5, "&7Bau Stahlgerüst und Stahlzäune",
          subtitle="Die Stützen der Maschinen.",
          description=[
              "Zwei &6Stahlbarren&r übereinander ergeben vier &6Stahlstäbe&r. Drei Stahlbarren oben und drei Stäbe darunter ergeben sechs &6Stahlgerüste&r, vier Barren und zwei Stäbe drei &6Stahlzäune&r.",
              "",
              "Der Bagger allein braucht &e26&r Gerüste, der Zerkleinerer 10 Gerüste und 8 Zäune.",
          ],
          tasks=[task_item("immersiveengineering:steel_scaffolding_standard", 32), task_item("immersiveengineering:steel_fence", 8)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 16)],
          deps=["light"], icon="immersiveengineering:steel_scaffolding_standard"),

    quest("sheetmetal", 2.5, 8, "&7Bau Stahlblechblöcke",
          subtitle="Vier Stahlbleche, vier Blöcke.",
          description=[
              "Vier &6Stahlbleche&r im Kreuz ergeben vier &6Stahlblechblöcke&r. Drei davon nebeneinander ergeben sechs Stufen.",
              "",
              "Der Lichtbogenofen braucht 8 Blöcke und 14 Stufen, der Bagger 16 Blöcke. Ab der Metallpresse kommen die Bleche von selbst.",
          ],
          tasks=[task_item("immersiveengineering:sheetmetal_steel", 16)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 16)],
          deps=["scaffold"], icon="immersiveengineering:sheetmetal_steel"),

    # ---- Zum Lichtbogenofen --------------------------------------------------
    quest("crusher", 6, 0.5, "&7&lForm einen Zerkleinerer",
          subtitle="5x3x3, Erz rein, zwei Staub raus.",
          description=[
              "&e10 Leichte Ingenieursbausteine, 10 Stahlgerüste, 8 Stahlzäune, 9 Trichter, 1 Redstone-Ingenieursbaustein&r. Hammer auf den mittleren Zaun der langen Seite mit dem Redstone-Baustein.",
              "",
              "&eRein:&r oben in die Walzen. &eRaus:&r unten vorne. Erzblock gibt 2 Staub (10 Prozent Nickelstaub dazu), Rohes Erz 1 Staub plus ein Drittel Chance auf einen zweiten, Bruchstein Kies, Sandstein Sand und Nitratstaub. Strom oben an der Schulter.",
              "",
              "&cWer hineinfällt, kommt als Beute wieder heraus.&r",
          ],
          tasks=[mb("mb_crusher", "Einen Zerkleinerer formen")],
          rewards=[reward_item("immersiveengineering:coal_coke", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["light", "parts", "scaffold"], icon="immersiveengineering:crusher", size=1.5),

    quest("coke_dust", 8.5, 0.5, "&8Mahl Koks zu Koksstaub",
          subtitle="Rohstoff für Graphit und Stahl im Lichtbogenofen.",
          description=[
              "Wirf &6Koks&r in den Zerkleinerer, heraus kommt &6Koksstaub&r, eins zu eins, für 2 400 FE pro Stück.",
              "",
              "Acht Koksstaub werden in der Industriepresse zu HOP-Graphit. Im Lichtbogenofen ist Koksstaub der Zusatz, der Eisen zu Stahl macht.",
          ],
          tasks=[task_item("immersiveengineering:dust_coke", 32)],
          rewards=[reward_item("immersiveengineering:coal_coke", 32), reward_xp(5)],
          deps=["crusher"], icon="immersiveengineering:dust_coke"),

    quest("squeezer", 11, 0.5, "&eForm eine Industriepresse",
          subtitle="3x3x3, Samen rein, Pflanzenöl raus.",
          description=[
              "&e4 Holzfässer, 1 Kolben, 2 Leichte Ingenieursbausteine, 1 Redstone-Ingenieursbaustein, 6 Stahlgerüste, 3 Stahlzäune, 2 Flüssigkeitsrohre&r. Hammer auf das mittlere Fass auf der Seite des Redstone-Bausteins.",
              "",
              "&eRein:&r durch die zwei blau markierten Luken hinten. &eRaus:&r Gegenstände an der orangen Luke, Flüssigkeit darunter. &6Hanfsamen&r geben 120 mB Pflanzenöl, Weizensamen 80 mB. Holzfass: drei Behandelte Holzstufen über fünf Behandelten Brettern.",
          ],
          tasks=[mb("mb_squeezer", "Eine Industriepresse formen"), task_item("immersiveengineering:plantoil_bucket", 1)],
          rewards=[reward_item("immersiveengineering:seed", 32), reward_xp(10)],
          deps=["coke_dust"], icon="immersiveengineering:squeezer"),

    quest("hop_graphite", 13.5, 0.5, "&8Press HOP-Graphitstaub",
          subtitle="Acht Koksstaub, ein Graphit.",
          description=[
              "Acht &6Koksstaub&r in der Industriepresse ergeben einen &6HOP-Graphitstaub&r, für 19 200 FE.",
              "",
              "Vier davon werden eine Graphitelektrode, einer eine HOP-Graphitplatte für den HV-Kondensator. Für drei Elektroden brauchst du also &e96 Koksstaub&r.",
              "",
              tex("material_dust_hop_graphite"),
          ],
          tasks=[task_item("immersiveengineering:dust_hop_graphite", 12)],
          rewards=[reward_item("immersiveengineering:dust_coke", 32), reward_xp(10)],
          deps=["squeezer"], icon="immersiveengineering:dust_hop_graphite"),

    quest("press", 8.5, 1.8, "&7Form eine Metallpresse",
          subtitle="3x3x1, Barren rein, Bleche, Stäbe und Zahnräder raus.",
          description=[
              "Unten &6Stahlgerüst, Redstone-Ingenieursbaustein, Stahlgerüst&r, in der Mitte &6Förderband, Kolben, Förderband&r in dieselbe Richtung, oben auf dem Kolben ein &6Schwerer Ingenieursbaustein&r. Hammer auf den Kolben.",
              "",
              "&eFormen:&r Blaupause Formen (Eisenblech, drei blaue Farbstoffe, drei Papier) am Arbeitstisch, dann drei Stahlbleche und der Kabelschneider pro Form. Per Rechtsklick in die Presse. &eRein:&r Barren aufs Band. &eRaus:&r am Bandende, ein Stahlblech für 2 400 FE.",
          ],
          tasks=[mb("mb_metalpress", "Eine Metallpresse formen"), task_item("immersiveengineering:mold_plate", 1),
                 task_item("immersiveengineering:mold_rod", 1), task_item("immersiveengineering:plate_steel", 32)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 16), reward_xp(10)],
          deps=["heavy", "parts"], icon="immersiveengineering:metal_press"),

    quest("bottling", 16, 0.5, "&bForm eine Abfüllanlage",
          subtitle="3x3x2, Form und Flüssigkeit rein, Teil raus.",
          description=[
              "&e3 Förderbänder, 2 Flüssigkeitspumpen, 2 Eisenblechblöcke, 2 Leichte Ingenieursbausteine, 1 Redstone-Ingenieursbaustein, 3 Stahlgerüste&r. Hammer auf das mittlere Band, die Richtung zählt. Spiegeln geht.",
              "",
              "&eRein:&r Gegenstand aufs Band, Flüssigkeit in den Tank (8 Eimer). &eRaus:&r am Bandende gefüllt. Sie füllt Eimer, Flaschen, Kanister und gießt Harz und Graphit in Pressformen.",
          ],
          tasks=[task_checkmark("Abfüllanlage gebaut und geformt"), task_item("immersiveengineering:creosote_bucket", 2)],
          rewards=[reward_item("immersiveengineering:creosote_bucket", 2), reward_xp(10)],
          deps=["hop_graphite", "press"], icon="immersiveengineering:bottling_machine"),

    quest("electrode", 18.5, 0.5, "&8Gieß drei Graphitelektroden",
          subtitle="Der Ofen braucht drei, und sie verschleißen.",
          description=[
              "In der Abfüllanlage: &6Pressform: Stab&r und &e4 HOP-Graphitstaub&r aufs Band, &e1 000 mB Kreosotöl&r in den Tank. Heraus kommt eine &6Graphitelektrode&r, die Form kommt zurück.",
              "",
              "Jede Elektrode hält &e80 Minuten&r Dauerbetrieb, dann zerbricht sie. Nachlegen geht nur von Hand. Halt immer drei in Reserve.",
              "",
              tex("graphite_electrode"),
          ],
          tasks=[task_item("immersiveengineering:graphite_electrode", 3)],
          rewards=[reward_item("immersiveengineering:dust_coke", 32), reward_xp(10)],
          deps=["bottling"], icon="immersiveengineering:graphite_electrode"),

    quest("arc", 21, 0.5, "&c&lForm einen Lichtbogenofen",
          subtitle="5x5x5, Erz und Eisen rein, Barren und Stahl raus.",
          description=[
              "&e27 Verstärkte Sprengziegel, 10 Leichte und 5 Schwere Ingenieursbausteine, 8 Stahlblechblöcke, 14 Stahlblechstufen, 6 Stahlblöcke, 5 Stahlgerüste, 1 Redstone-Ingenieursbaustein, 1 Kessel&r. Hammer auf den Kessel.",
              "",
              "&eRein:&r oben drei Elektroden, links durch die Luke bis zu 12 Eingaben, rechts 4 Zusätze. &eRaus:&r vorne aus dem Becken 6 Ausgaben, hinten Schlacke. Strom über die drei Anschlüsse hinten.",
              "",
              "Erzblock gibt 2 Barren, Rohes Erz 1 plus halbe Chance auf einen zweiten. Elektrum, Constantan und Bronze schmilzt er direkt aus Staub. Messing nicht.",
          ],
          tasks=[mb("mb_arcfurnace", "Einen Lichtbogenofen formen")],
          rewards=[reward_item("immersiveengineering:graphite_electrode", 1), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["electrode", "sheetmetal"], icon="immersiveengineering:arc_furnace", size=2.0, shape="hexagon"),

    quest("arc_steel", 23.5, 0.5, "&8&lSchmilz 256 Stahl im Lichtbogenofen",
          subtitle="Zwölf Plätze gleichzeitig.",
          description=[
              "&6Eisenbarren&r als Eingabe, &6Koksstaub&r als Zusatz ergeben einen &6Stahlbarren&r und Schlacke. Pro Barren 204 800 FE in 20 Sekunden, das sind &d512 FE/t&r pro Platz, mit allen zwölf rund &d6 000 FE/t&r.",
              "",
              "Trichter oder Rohre füllen Eisen und Koksstaub von oben nach, eine Kiste vorne nimmt den Stahl. Der Zerkleinerer liefert den Koksstaub dazu.",
              "",
              "&eKronwerke:&r Das Stufenziel will &e4 000 Stahlbarren&r. Häng die Ausgabe direkt an die Kiste am Obelisken.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 256)],
          rewards=[reward_item("immersiveengineering:coal_coke", 64), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["arc"], icon="immersiveengineering:ingot_steel", size=1.5),

    # ---- Öl und Diesel -------------------------------------------------------
    quest("fermenter", 8.5, 6.5, "&eForm einen Industriefermenter",
          subtitle="3x3x3, Kartoffeln rein, Ethanol raus.",
          description=[
              "&e4 Kessel, 4 Eisenblechblöcke, 6 Stahlgerüste, 2 Leichte Ingenieursbausteine, 2 Flüssigkeitsrohre, 1 Redstone-Ingenieursbaustein&r. Hammer auf den mittleren Kessel auf der Seite des Redstone-Bausteins.",
              "",
              "&eRein:&r hinten durch die blauen Luken: Kartoffeln, Zuckerrohr, Äpfel, Melonen, Beeren, Rote Bete, Honig. &eRaus:&r Ethanol unter der orangen Luke. Eine Kartoffel gibt 80 mB für 6 400 FE.",
          ],
          tasks=[mb("mb_fermenter", "Einen Industriefermenter formen"), task_item("immersiveengineering:ethanol_bucket", 1)],
          rewards=[reward_item("minecraft:potato", 32), reward_xp(10)],
          deps=["squeezer"], icon="immersiveengineering:fermenter"),

    quest("refinery", 11, 6.5, "&6&lForm eine Raffinerie",
          subtitle="5x3x3, Pflanzenöl und Ethanol rein, Biodiesel raus.",
          description=[
              "&e16 Eisenblechblöcke, 2 Leichte und 2 Schwere Ingenieursbausteine, 1 Redstone-Ingenieursbaustein, 8 Stahlgerüste, 5 Flüssigkeitsrohre&r. Hammer auf den Schweren Baustein in der mittleren Schicht.",
              "",
              "&eRein:&r je eine Flüssigkeit an den Seiten, &6Nitratstaub&r als Katalysator von Hand (wird nicht verbraucht). &eRaus:&r vorne am orangen Anschluss. 8 mB Öl und 8 mB Ethanol geben &e16 mB Biodiesel&r.",
              "",
              "Nitratstaub fällt zu 50 Prozent, wenn der Zerkleinerer Sandstein mahlt.",
          ],
          tasks=[mb("mb_refinery", "Eine Raffinerie formen"), task_item("immersiveengineering:biodiesel_bucket", 1)],
          rewards=[reward_item("immersiveengineering:dust_saltpeter", 4), reward_table("s3_common"), reward_xp(15)],
          deps=["fermenter", "heavy"], icon="immersiveengineering:refinery", size=1.5),

    quest("generator_blocks", 13.5, 6.5, "&7Bau Generator- und Kühlerblöcke",
          subtitle="Das Innere des Dieselgenerators.",
          description=[
              "&6Generatorblock:&r Stahlblechblöcke in die Ecken, &6Elektrumspulenblöcke&r an die Seiten, eine &6Mechanische Eisenkomponente&r in die Mitte, gibt vier. &6Kühlerblock:&r Stahlblechblöcke, &6Constantanbleche&r, ein Wassereimer in der Mitte, gibt vier.",
              "",
              "Beide öffnen mit Stufe 3. Der Dieselgenerator braucht &e4 Generatorblöcke&r und &e9 Kühlerblöcke&r, der Bagger 3 Kühler.",
          ],
          tasks=[task_item("immersiveengineering:generator", 4), task_item("immersiveengineering:radiator", 12)],
          rewards=[reward_item("immersiveengineering:ingot_constantan", 8), reward_xp(10)],
          deps=["refinery"], icon="immersiveengineering:generator"),

    quest("diesel", 16, 6.5, "&c&lForm einen Dieselgenerator",
          subtitle="3x3x5, Biodiesel rein, 4 096 FE/t raus.",
          description=[
              "&e13 Schwere Ingenieursbausteine, 9 Kühlerblöcke, 4 Generatorblöcke, 6 Stahlgerüste, 5 Flüssigkeitsrohre, 1 Redstone-Ingenieursbaustein&r. Hammer auf den mittleren Generatorblock.",
              "",
              "&eRein:&r Brennstoff unten an den Ecken. &eRaus:&r &d4 096 FE/t&r an bis zu drei Anschlüsse über dem Generator. Er läuft nur, wenn jemand Strom abnimmt.",
              "",
              "Ein Eimer Biodiesel hält 250 Ticks, also gut eine Million FE. Kreosot nur 20 Ticks, Hochcetan-Biodiesel (95 zu 5 mit Stärketrank aus der Raffinerie) 275 Ticks.",
          ],
          tasks=[mb("mb_dieselgen", "Einen Dieselgenerator formen")],
          rewards=[reward_item("immersiveengineering:wirecoil_steel", 16), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["generator_blocks"], icon="immersiveengineering:diesel_generator", size=1.75, shape="hexagon"),

    quest("hv", 18.5, 6.5, "&cSpann HV-Draht",
          subtitle="32 768 FE/t über 32 Blöcke.",
          description=[
              "&6Stahlblech&r und &6Aluminiumblech&r mit dem Kabelschneider ergeben Stahl- und Aluminiumkabel. Zwei Stahlkabel und zwei Aluminiumkabel um einen Stock ergeben vier &6HV-Drahtspulen&r. &6HV-Anschlüsse&r wie LV, nur mit Aluminiumbarren.",
              "",
              "HV-Draht trägt &d32 768 FE/t&r, ein HV-Anschluss &d4 096 FE/t&r, genau die Leistung eines Dieselgenerators. Der &6HV-Trafo&r stuft direkt von HV auf LV oder MV herunter.",
              "",
              "&cHV-Draht ist nicht isolierbar.&r Häng ihn hoch.",
          ],
          tasks=[task_item("immersiveengineering:wirecoil_steel", 8), task_item("immersiveengineering:connector_hv", 4), task_item("immersiveengineering:transformer_hv", 1)],
          rewards=[reward_item("immersiveengineering:ingot_aluminum", 8), reward_xp(10)],
          deps=["diesel"], icon="immersiveengineering:wirecoil_steel"),

    # ---- Kunststoff ----------------------------------------------------------
    quest("acetaldehyde", 11, 9, "&dRaffinier Acetaldehyd",
          subtitle="Ethanol über Silber.",
          description=[
              "In der Raffinerie: &6Ethanol&r allein, mit einem &6Silberblech&r als Katalysator, ergibt &6Acetaldehyd&r, 8 mB zu 8 mB.",
              "",
              "Den Katalysator tauschst du von Hand gegen den Nitratstaub. Eine zweite Raffinerie nur für Kunststoff spart das Umlegen.",
          ],
          tasks=[task_item("immersiveengineering:acetaldehyde_bucket", 1)],
          rewards=[reward_item("immersiveengineering:plate_silver", 4), reward_xp(5)],
          deps=["refinery"], icon="immersiveengineering:acetaldehyde_bucket"),

    quest("resin", 13.5, 9, "&dMisch Phenolharz",
          subtitle="Acetaldehyd und Kreosot.",
          description=[
              "In der Raffinerie, ohne Katalysator: &e12 mB Acetaldehyd&r und &e8 mB Kreosotöl&r ergeben &e8 mB Phenolharz&r.",
              "",
              "Das Kreosot kommt aus den Koksöfen. Ein voller Koksofen mit Kohleblöcken hält eine Harzstraße gut am Laufen.",
          ],
          tasks=[task_item("immersiveengineering:phenolic_resin_bucket", 1)],
          rewards=[reward_item("immersiveengineering:creosote_bucket", 2), reward_xp(5)],
          deps=["acetaldehyde"], icon="immersiveengineering:phenolic_resin_bucket"),

    quest("duroplast", 16, 9, "&dGieß Duroplastplatten",
          subtitle="Harz in die Plattenform.",
          description=[
              "In der Abfüllanlage: &6Pressform: Platte&r aufs Band, &e250 mB Phenolharz&r in den Tank ergeben eine &6Duroplastplatte&r. Die Form kommt zurück.",
              "",
              "Duroplast isoliert und zählt als Kunststoffplatte. Duroplastblöcke ersetzen Terrakotta in Anschlüssen.",
              "",
              tex("material_plate_duroplast"),
          ],
          tasks=[task_item("immersiveengineering:plate_duroplast", 8)],
          rewards=[reward_item("immersiveengineering:phenolic_resin_bucket", 1), reward_xp(10)],
          deps=["resin", "bottling"], icon="immersiveengineering:plate_duroplast"),

    quest("electronics", 18.5, 9, "&d&lBau Fortgeschrittene Elektronik",
          subtitle="Das beste Bauteil des Mods.",
          description=[
              "Blaupause Komponenten am Arbeitstisch: eine &6Duroplastplatte&r, zwei &6Vakuumröhren&r und ein &6Aluminiumkabel&r ergeben eine &6Fortgeschrittene Elektronikkomponente&r.",
              "",
              "Sie öffnet mit Stufe 3 und steckt in Teslaspule, Railgun, Geschützturm und den Resonanz-Ingenieursbausteinen.",
              "",
              tex("material_component_electronic_adv"),
          ],
          tasks=[task_item("immersiveengineering:component_electronic_adv", 2)],
          rewards=[reward_item("immersiveengineering:electron_tube", 6), reward_xp(15)],
          deps=["duroplast"], icon="immersiveengineering:component_electronic_adv"),

    # ---- Weitere Maschinen ---------------------------------------------------
    quest("mixer", 6, 12, "&9Form einen Mischer",
          subtitle="3x3x3, Feststoffe und Wasser rein, Beton und Säure raus.",
          description=[
              "&e4 Leichte Ingenieursbausteine, 4 Eisenblechblöcke, 5 Stahlgerüste, 1 Stahlzaun, 3 Flüssigkeitsrohre, 1 Redstone-Ingenieursbaustein&r. Hammer auf den mittleren Eisenblechblock.",
              "",
              "&eRein:&r Flüssigkeit unten an der Stromversorgung, Gegenstände hinten durch zwei Luken. &eRaus:&r vorne. 2 Sand, 1 Kies, 1 Ton in 500 mB Wasser geben 500 mB &6Flüssigbeton&r, 1 Redstone in 250 mB Wasser gleich viel &6Redstonesäure&r. Auch Tränke in Tanks.",
          ],
          tasks=[mb("mb_mixer", "Einen Mischer formen")],
          rewards=[reward_item("minecraft:sand", 32), reward_item("minecraft:clay_ball", 16), reward_xp(10)],
          deps=["parts", "scaffold"], icon="immersiveengineering:mixer"),

    quest("assembler", 8.5, 12, "&9Form einen Monteur",
          subtitle="3x3x3, eine Werkbank mit drei Rezepten.",
          description=[
              "&e9 Eisenblechblöcke, 6 Eisenblechstufen, 6 Stahlgerüste, 2 Leichte und 2 Redstone-Ingenieursbausteine, 2 Förderbänder&r. Hammer auf das nach innen zeigende Förderband.",
              "",
              "&eRein:&r Zutaten und Flüssigkeiten an der Eingangsseite, 18 Lagerplätze. &eRaus:&r die fertigen Teile. Drei Rezepte der Reihe nach, das Ergebnis des ersten darf Zutat des zweiten sein. &d80 FE&r pro Teil.",
          ],
          tasks=[task_checkmark("Monteur gebaut und geformt")],
          rewards=[reward_item("immersiveengineering:conveyor_basic", 8), reward_xp(10)],
          deps=["mixer"], icon="immersiveengineering:assembler"),

    quest("sawmill", 11, 12, "&9Form ein Sägewerk",
          subtitle="5x3x3, Stämme rein, sechs Bretter und Sägemehl raus.",
          description=[
              "&e6 Leichte und 2 Schwere Ingenieursbausteine, 4 Eisenblechblöcke, 8 Stahlgerüste, 4 Förderbänder, 1 Redstone-Ingenieursbaustein&r. Hammer auf den mittleren Blechblock.",
              "",
              "&6Sägeblatt&r (Stahlbarren in die Ecken, Stahlbleche an die Seiten) hinten per Rechtsklick einsetzen. &eRein:&r Stamm aufs Band. &eRaus:&r Eiche gibt &e6 Bretter&r plus Sägemehl für 1 600 FE. Ohne Blatt kommen nur entrindete Stämme heraus.",
          ],
          tasks=[task_checkmark("Sägewerk gebaut und geformt"), task_item("immersiveengineering:sawblade", 1)],
          rewards=[reward_item("minecraft:oak_log", 32), reward_xp(10)],
          deps=["heavy", "scaffold"], icon="immersiveengineering:sawmill"),

    quest("auto_workbench", 13.5, 12, "&9Form einen Automatisierten Arbeitstisch",
          subtitle="3x2x3, Blaupause rein, fertige Teile raus.",
          description=[
              "&e4 Leichte und 2 Schwere Ingenieursbausteine, 5 Stahlgerüste, 4 Förderbänder, 2 Behandelte Holzstufen, 1 Redstone-Ingenieursbaustein&r. Hammer auf den Block, den das Handbuch zeigt.",
              "",
              "Leg eine Blaupause auf den Zeichentisch und wähl das Teil. &eRein:&r Zutaten durch die zwei blauen Luken, Strom darüber. &eRaus:&r am Ende des Bands. So laufen Stahlkomponenten und Vakuumröhren ohne dich.",
          ],
          tasks=[task_checkmark("Automatisierter Arbeitstisch gebaut und geformt")],
          rewards=[reward_item("immersiveengineering:plate_steel", 16), reward_xp(10)],
          deps=["sawmill"], icon="immersiveengineering:auto_workbench"),

    quest("survey", 16, 12, "&6Such eine Mineralader",
          subtitle="Vermessen, bohren, Kernprobe lesen.",
          description=[
              "&6Mineralvermessungswerkzeuge:&r Buch und Feder, Glasflasche, Hammer oben, drei Robustes Gewebe unten. &6Kernprobenbohrer:&r Stahlgerüste und Stahlzäune, unten zwei Leichte Ingenieursbausteine.",
              "",
              "Die Werkzeuge zeigen auf natürlichem Gestein grob, wo eine Ader liegt. Der Bohrer nimmt mit &d40 FE/t&r eine &6Kernprobe&r: welche Erze drin sind und wie gesättigt. Gesneakt platziert markiert die Probe die Ader auf einer Karte.",
          ],
          tasks=[task_item("immersiveengineering:survey_tools", 1), task_item("immersiveengineering:coresample", 1)],
          rewards=[reward_item("minecraft:map", 2), reward_xp(10)],
          deps=["light", "scaffold"], icon="immersiveengineering:survey_tools"),

    quest("excavator", 18.5, 12, "&6&lForm einen Bagger",
          subtitle="Motor 3x3x6 und Schaufelrad 7x7, Ader rein, Erz raus.",
          description=[
              "&eMotor:&r 16 Stahlblechblöcke, 9 Leichte und 4 Schwere Ingenieursbausteine, 3 Kühlerblöcke, 6 Stahlgerüste, 1 Redstone-Ingenieursbaustein. &eRad:&r 9 Stahlblöcke, 20 Stahlgerüste. Hammer auf den hinteren mittleren Schweren Baustein.",
              "",
              "&eRein:&r &d4 096 FE/t&r über die drei Anschlüsse an der Seite, ein Dieselgenerator pro Bagger. &eRaus:&r Erz hinten am Motor. Eine Ader gibt höchstens &e38 400&r Erze, je weiter weg vom Zentrum, desto mehr taubes Gestein.",
          ],
          tasks=[mb("mb_excavator", "Einen Bagger formen")],
          rewards=[reward_item("immersiveengineering:ingot_steel", 32), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["diesel", "survey"], icon="immersiveengineering:excavator", size=1.75, shape="hexagon"),

    quest("lightning_rod", 21, 12, "&eForm einen Blitzableiter",
          subtitle="3x3x3, ein Blitz gibt 16 Millionen FE.",
          description=[
              "&e8 Kupferspulenblöcke, 4 Leichte Ingenieursbausteine, 4 Stahlgerüste, 4 Behandelte Holzzäune, 4 HV-Kondensatoren, 3 Hochspannungsspulenblöcke&r, Form wie im Handbuch, dann Hammer drauf.",
              "",
              "&6HV-Kondensator:&r Aluminium, Redstonesäureeimer, Aluminium oben, Aluminiumblech, Einfacher Ingenieursbaustein, &6HOP-Graphitplatte&r unten, speichert 4 Millionen FE. Stahlzäune oben auf dem Blitzableiter erhöhen bei Gewitter die Trefferchance.",
          ],
          tasks=[task_item("immersiveengineering:capacitor_hv", 4), task_checkmark("Blitzableiter geformt")],
          rewards=[reward_item("immersiveengineering:steel_fence", 16), reward_xp(15)],
          deps=["hv", "hop_graphite"], icon="immersiveengineering:lightning_rod", optional=True),

    quest("radio_tower", 23.5, 12, "&bForm einen Funkturm",
          subtitle="5x19x6, Redstone-Signale über weite Strecken.",
          description=[
              "&e90 Beton, 76 Aluminiumblechblöcke, 16 Aluminiumblechstufen, 11 Redstone-Ingenieursbausteine, 6 Aluminiumzäune, 4 Stahlblechblöcke, 2 Kühlerblöcke, 2 Leichte Ingenieursbausteine&r. Form wie im Handbuch, dann Hammer drauf.",
              "",
              "&eRein:&r &d128 FE/t&r am linken Anschluss, ein Redstone-Signal am mittleren. &eRaus:&r dasselbe Signal an jedem Turm auf derselben Frequenz (128 bis 384 kHz) in Reichweite. Höher und freier heißt weiter.",
          ],
          tasks=[task_checkmark("Funkturm geformt")],
          rewards=[reward_item("immersiveengineering:ingot_aluminum", 16), reward_xp(10)],
          deps=["electronics", "mixer"], icon="immersiveengineering:sheetmetal_aluminum", optional=True),

    quest("resonanz", 26, 12, "&bForm einen Resonanz-Beobachter",
          subtitle="3x5x3, hält 32 Blöcke um sich herum aktiv.",
          description=[
              "&e20 Stahlgerüste, 9 Beton, 5 Stahlfenster, 4 Stahlzäune, 3 Leichte und 2 Resonanz-Ingenieursbausteine, 1 Redstone-Ingenieursbaustein, 1 Kalibrierter Sculk-Sensor&r. Resonanz-Baustein: Bleiblechblöcke, Fortgeschrittene Elektronik, ein Echosplitter.",
              "",
              "&eRein:&r &d128 FE/t&r rechts und &6Papier&r links, ein Blatt hält 60 Sekunden. &eRaus:&r Maschinen im Umkreis von etwa 32 Blöcken laufen weiter, auch wenn niemand in der Nähe ist.",
          ],
          tasks=[task_item("immersiveengineering:resonanz_engineering", 2), task_checkmark("Resonanz-Beobachter geformt")],
          rewards=[reward_item("minecraft:paper", 64), reward_xp(15)],
          deps=["radio_tower"], icon="immersiveengineering:resonanz_engineering", optional=True),

    # ---- Checklisten ---------------------------------------------------------
    quest("list_process", 8, 15.5, "&6&lHak die Verarbeitungsmaschinen ab",
          subtitle="Acht Multiblöcke aus Ingenieursbausteinen.",
          description=[
              "&6Zerkleinerer:&r 5x3x3, 38 Blöcke. Erz rein, Staub raus.",
              "&6Metallpresse:&r 3x3x1, 7 Blöcke. Barren rein, Bleche raus.",
              "&6Industriepresse:&r 3x3x3, 19 Blöcke. Samen rein, Pflanzenöl raus.",
              "&6Industriefermenter:&r 3x3x3, 19 Blöcke. Früchte rein, Ethanol raus.",
              "&6Abfüllanlage:&r 3x3x2, 13 Blöcke. Form und Flüssigkeit rein, Teil raus.",
              "&6Mischer:&r 3x3x3, 18 Blöcke. Feststoff und Wasser rein, Beton raus.",
              "&6Sägewerk:&r 5x3x3, 25 Blöcke. Stamm rein, Bretter raus.",
              "&6Monteur:&r 3x3x3, 27 Blöcke. Zutaten rein, Teile raus.",
          ],
          tasks=[mb("mb_crusher", "Zerkleinerer"), mb("mb_metalpress", "Metallpresse"), mb("mb_squeezer", "Industriepresse"),
                 mb("mb_fermenter", "Industriefermenter"), task_checkmark("Abfüllanlage"), mb("mb_mixer", "Mischer"),
                 task_checkmark("Sägewerk"), task_checkmark("Monteur")],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["assembler", "bottling"], icon="immersiveengineering:light_engineering", size=1.5, shape="gear"),

    quest("list_big", 12, 15.5, "&6&lHak die Großanlagen ab",
          subtitle="Sieben Multiblöcke für Fortgeschrittene.",
          description=[
              "&6Raffinerie:&r 5x3x3, 34 Blöcke. Öl und Ethanol rein, Biodiesel raus.",
              "&6Lichtbogenofen:&r 5x5x5, 77 Blöcke. Erz rein, Barren raus.",
              "&6Dieselgenerator:&r 3x3x5, 38 Blöcke. Biodiesel rein, 4 096 FE/t raus.",
              "&6Bagger:&r 3x7x8 mit Rad, 68 Blöcke. Strom rein, Erz raus.",
              "&6Automatisierter Arbeitstisch:&r 3x2x3, 18 Blöcke.",
              "&6Blitzableiter:&r 3x3x3, 27 Blöcke. &6Funkturm:&r 5x19x6, 207 Blöcke. &6Resonanz-Beobachter:&r 3x5x3, 45 Blöcke.",
              "",
              "Die Blöcke von Stufe 2 stehen im Kapitel &6Immersive Engineering&r.",
          ],
          tasks=[mb("mb_refinery", "Raffinerie"), mb("mb_arcfurnace", "Lichtbogenofen"), mb("mb_dieselgen", "Dieselgenerator"),
                 mb("mb_excavator", "Bagger"), task_checkmark("Automatisierter Arbeitstisch"), task_checkmark("Blitzableiter"),
                 task_checkmark("Funkturm"), task_checkmark("Resonanz-Beobachter")],
          rewards=[reward_table("s3_uncommon"), reward_xp(20)],
          deps=["excavator", "auto_workbench"], icon="immersiveengineering:heavy_engineering", size=1.5, shape="gear", section="lists"),

    # ---- Abschluss -----------------------------------------------------------
    quest("final", 26.5, 4.5, "&c&lBau ein Stahlwerk für den Server",
          subtitle="Der Ofen schläft nie.",
          description=[
              "Sammle &e1 024 Stahlbarren&r und &e32 Schwere Ingenieursbausteine&r.",
              "",
              "&eKronwerke:&r Das Stufenziel &e\"Der Ofen schläft nie\"&r will &e4 000 Stahlbarren&r, &e250 Fortgeschrittene Steuerschaltkreise&r und &e8 Stahlkerne&r. Ein Stahlkern: vier Schwere Ingenieursbausteine, ein Fortgeschrittener Steuerschaltkreis, zwei Ingenieursprozessoren aus AE2, ein Stahlgehäuse, ein Elementiumbarren.",
              "",
              "Stahl und Bausteine liefert dieses Kapitel. Stell eine Kiste neben den Obelisken und häng die Stahlstraße daran.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 1024), task_item("immersiveengineering:heavy_engineering", 32)],
          rewards=[reward_table("s3_rare"), reward_item("immersiveengineering:storage_steel", 8), reward_xp(30)],
          deps=["arc_steel", "diesel", "electronics"], icon="immersiveengineering:storage_steel", size=2.5, shape="gear"),

    # ---- neue Quests: Zum Lichtbogenofen ---------------------------------------
    quest("molds", 11, 1.8, "&7Bau weitere Pressformen",
          subtitle="Zahnräder, Draht und Blöcke aus der Presse.",
          description=[
              "Mit der &6Blaupause Formen&r am Arbeitstisch ergeben je drei &6Stahlbleche&r und der Kabelschneider eine Form: &6Zahnrad&r, &6Draht&r, &6Verpackung 2x2&r, &6Verpackung 3x3&r und &6Entpacken&r.",
              "",
              "Die Verpackungsformen pressen 4 oder 9 gleiche Gegenstände zu ihrem Block, Entpacken macht es rückgängig. So landen Barren platzsparend als Blöcke im Lager, oder Sand wird zu Sandstein.",
              "",
              "Die Zahnradform presst vier Barren zu einem Metallzahnrad für andere Mods, die Drahtform einen Barren zu zwei Kabeln, ganz ohne Kabelschneider.",
          ],
          tasks=[task_item("immersiveengineering:mold_gear", 1), task_item("immersiveengineering:mold_wire", 1),
                 task_item("immersiveengineering:mold_packing_9", 1)],
          rewards=[reward_item("immersiveengineering:plate_steel", 8), reward_xp(10)],
          deps=["press"], icon="immersiveengineering:mold_gear", optional=True),

    # ---- neue Quests: Weitere Maschinen ----------------------------------------
    quest("concrete", 6, 13, "&9Gieß Beton",
          subtitle="Hart, billig und explosionsfest.",
          description=[
              "Vier &6Sand&r, zwei &6Tonklumpen&r, zwei &6Kies&r und ein &6Wassereimer&r ergeben &e8 Beton&r. Der Mischer macht &6Flüssigbeton&r: ausgegossen fließt er wie Wasser und wird nach einer Weile fest. Wer dann darin steht, steckt fest.",
              "",
              "Ein Beton und ein &6Bleiblech&r formlos ergeben &6Bleibeton&r. Durch ihn teleportieren sich weder Endermen noch Enderperlen oder Chorusfrüchte.",
              "",
              "Der Funkturm braucht &e90 Beton&r, der Resonanz-Beobachter 9. Mit der Steinsäge wird Beton zu Ziegeln, Fliesen und Stufen.",
          ],
          tasks=[task_item("immersiveengineering:concrete", 32), task_item("immersiveengineering:concrete_leaded", 4)],
          rewards=[reward_item("minecraft:sand", 32), reward_item("minecraft:gravel", 16), reward_xp(10)],
          deps=["mixer"], icon="immersiveengineering:concrete"),

    # ---- neue Quests: Werkzeuge und Waffen -------------------------------------
    quest("drill", 8, 20.5, "&6&lBau eine Bergbaubohrmaschine",
          subtitle="Erz und Stein im Vorbeigehen, mit Biodiesel.",
          description=[
              "Zwei &6Holzgriffe&r, ein &6Schwerer Ingenieursbaustein&r und eine &6Mechanische Eisenkomponente&r ergeben die &6Bergbaubohrmaschine&r. Holzgriff: fünf Behandelte Stöcke und ein Kupferklumpen.",
              "",
              "&6Bohrkopf:&r vier Stahlbarren und ein Stahlblock ergeben den &6Stahlbohrkopf&r, mit Eisen den Eisenbohrkopf. Bohrmaschine in den &6Ingenieursarbeitstisch&r legen und den Kopf einsetzen. Der Kopf nutzt sich ab, im Amboss reparierst du ihn.",
              "",
              "Sie läuft mit &6Biodiesel&r. Füll sie an der Raffinerie, an einem Fass oder am Tank. Schleichend bohrt sie nur einen Block.",
          ],
          tasks=[task_item("immersiveengineering:drill", 1), task_item("immersiveengineering:drillhead_steel", 1)],
          rewards=[reward_item("immersiveengineering:biodiesel_bucket", 2), reward_table("s3_common"), reward_xp(15)],
          deps=["heavy", "refinery"], icon="immersiveengineering:drill", size=1.5, shape="hexagon"),

    quest("drill_upgrades", 10.5, 20.5, "&6Rüste die Bohrmaschine auf",
          subtitle="Schneller, unter Wasser, mit mehr Erz.",
          description=[
              "Alle Aufrüstungen kommen im Ingenieursarbeitstisch in die Bohrmaschine:",
              "&6Weitere Bohrer:&r zwei Stahlbarren und eine Mechanische Eisenkomponente. Schneller und mehr Schaden, bis zu dreimal.",
              "&6Druckluftbehälter:&r Eisenbleche, blauer Farbstoff, ein Flüssigkeitsrohr. Bohrt unter Wasser ohne Verlangsamung.",
              "&6Großer Panzer:&r mehr Treibstoff. &6Erweitertes Schmiersystem:&r ein Eimer Pflanzenöl im Rezept, der Kopf verschleißt langsamer.",
              "&6Gesteinserweichende Säure:&r ein Eimer Redstonesäure im Rezept, wirkt wie Glück auf Erze.",
          ],
          tasks=[task_item("immersiveengineering:toolupgrade_drill_damage", 1), task_item("immersiveengineering:toolupgrade_drill_waterproof", 1)],
          rewards=[reward_item("immersiveengineering:component_iron", 4), reward_xp(10)],
          deps=["drill"], icon="immersiveengineering:toolupgrade_drill_damage"),

    quest("jerrycan", 10.5, 22.5, "&9Pack einen Kanister ein",
          subtitle="Zehn Eimer Treibstoff zum Mitnehmen.",
          description=[
              "Vier &6Eisenbleche&r und vier &6Eimer&r ergeben den &6Kanister&r. Er fasst &e10 Eimer&r.",
              "",
              "Füll ihn an einem Fass oder Tank, aus der Welt schöpft er nicht. Kanister und Bohrmaschine zusammen in die Werkbank gelegt füllen die Bohrmaschine auf, ohne dass du zur Raffinerie musst.",
          ],
          tasks=[task_item("immersiveengineering:jerrycan", 1)],
          rewards=[reward_item("immersiveengineering:biodiesel_bucket", 2)],
          deps=["drill"], icon="immersiveengineering:jerrycan", optional=True),

    quest("buzzsaw", 13, 20.5, "&6Bau eine Kreissäge",
          subtitle="Ganze Bäume auf einmal.",
          description=[
              "Zwei &6Holzgriffe&r, zwei &6Stahlstäbe&r und ein &6Schwerer Ingenieursbaustein&r ergeben die &6Kreissäge&r. Im Ingenieursarbeitstisch setzt du ein &6Sägeblatt&r ein, getankt wird wie bei der Bohrmaschine.",
              "",
              "Sie fällt ganze Bäume, auch große Dschungelbäume. Mit dem &6Steinsägeblatt&r (Diamanten und Stahlbleche) schneidet sie Stein sauber heraus, wie mit Behutsamkeit.",
              "",
              "Der &6Klingenköcher&r trägt zwei Ersatzblätter, schleichend mit dem Mausrad wechselst du.",
          ],
          tasks=[task_item("immersiveengineering:buzzsaw", 1)],
          rewards=[reward_item("immersiveengineering:sawblade", 1), reward_xp(10)],
          deps=["drill", "sawmill"], icon="immersiveengineering:buzzsaw", optional=True),

    quest("revolver", 15.5, 20.5, "&cBau einen Revolver",
          subtitle="Fünf Teile, dann Patronen am Arbeitstisch.",
          description=[
              "&6Revolverlauf:&r Stahlbarren, Stahlstab und der Hammer. &6Revolvertrommel:&r vier Stahlbleche um einen Stahlstab. &6Revolverhammer:&r zwei Stahlbarren, Feuerstein, Stahlstab. Dazu eine &6Mechanische Stahlkomponente&r und ein &6Holzgriff&r wie bei der Bohrmaschine ergeben den &6Revolver&r.",
              "",
              "&6Patronen:&r Fünf Kupferbleche ergeben fünf &6Leere Gehäuse&r. Die &6Blaupause Patronen&r (Schießpulver, Gehäuse, Schießpulver, drei blaue Farbstoffe, drei Papier) macht am Arbeitstisch aus vier Gehäusen, Schießpulver und einem Bleiklumpen vier &6Casull-Patronen&r.",
              "",
              "Schleichend Rechtsklick öffnet die Trommel. Schüsse sind laut und locken Monster an.",
          ],
          tasks=[task_item("immersiveengineering:revolver", 1), task_item("immersiveengineering:bullet_casull", 8)],
          rewards=[reward_item("minecraft:gunpowder", 16), reward_item("immersiveengineering:empty_casing", 8), reward_xp(10)],
          deps=["steel_component", "drill"], icon="immersiveengineering:revolver", optional=True),

    quest("powerpack", 18, 20.5, "&eTrag einen Kondensator-Rucksack",
          subtitle="Strom für alles in deinen Händen.",
          description=[
              "Zwei &6Behandelte Stöcke&r, drei &6Stahlstäbe&r, zwei &6LV-Kabelanschlüsse&r, ein &6Leder&r und zwei &6Isolierte LV-Drahtspulen&r ergeben das Gestell. Im &6Ingenieursarbeitstisch&r setzt du einen &6Kondensator&r ein.",
              "",
              "Er lädt die Werkzeuge in deinen Händen und deine getragene Rüstung. Du trägst ihn als Brustteil, oder du verbindest ihn in der Werkbank mit einem Brustpanzer.",
              "",
              "Mit der &6Ladeantenne&r lädt er sich selbst, wenn du unter einer unisolierten Leitung entlang gehst.",
          ],
          tasks=[task_item("immersiveengineering:powerpack", 1)],
          rewards=[reward_item("immersiveengineering:wirecoil_copper_ins", 8), reward_xp(10)],
          deps=["light"], icon="immersiveengineering:powerpack", optional=True),

    quest("chemthrower", 13, 22.5, "&cBau einen Chemischen Werfer",
          subtitle="Er sprüht jede Flüssigkeit, auf Wunsch brennend.",
          description=[
              "Ein &6Druckluftbehälter&r, zwei &6Holzgriffe&r, ein &6Schwerer Ingenieursbaustein&r, ein &6Flüssigkeitsrohr&r und ein &6Eimer&r ergeben den &6Chemischen Werfer&r.",
              "",
              "Füll ihn mit einer Flüssigkeit oder einem Gas, Rechtsklick sprüht es. Schleichend Rechtsklick schaltet die Zündflamme: mit Kreosot oder Biodiesel wird er zum Flammenwerfer. Mit Flüssigbeton baust du schnelle Plattformen.",
              "",
              "Im Arbeitstisch: &6Großer Panzer&r für mehr Inhalt, &6Fokussierte Düse&r für mehr Reichweite, &6Multitank&r für drei Flüssigkeiten.",
          ],
          tasks=[task_item("immersiveengineering:chemthrower", 1)],
          rewards=[reward_item("immersiveengineering:creosote_bucket", 2), reward_xp(10)],
          deps=["drill_upgrades"], icon="immersiveengineering:chemthrower", optional=True),

    quest("railgun", 18, 22.5, "&d&lBau eine Railgun",
          subtitle="Stäbe mit Strom auf Höchstgeschwindigkeit.",
          description=[
              "Ein &6HV-Kondensator&r, ein &6Holzgriff&r, zwei &6Stahlbarren&r, zwei &6Elektrumspulenblöcke&r und eine &6Fortgeschrittene Elektronikkomponente&r ergeben die &6Railgun&r.",
              "",
              "Halt Rechtsklick, bis die Ladung &e99&r erreicht, dann loslassen. Sie verschießt Eisen-, Aluminium- und Stahlstäbe oder Graphitelektroden aus deinem Inventar, Lohenruten setzen Ziele in Brand.",
              "",
              "Ihr eigener Speicher ist klein. Trag dazu den Kondensator-Rucksack.",
          ],
          tasks=[task_item("immersiveengineering:railgun", 1)],
          rewards=[reward_item("immersiveengineering:stick_steel", 16), reward_table("s3_common"), reward_xp(15)],
          deps=["electronics", "powerpack"], icon="immersiveengineering:railgun", optional=True),
]

images = [
    banner("immersive_heavy/title", "Schwerindustrie", 12, -3.4, height=1.5, kind="title", colour="fire"),
    banner("immersive_heavy/blocks", "Bausteine", 1.4, 2.6, height=0.9, colour="stone"),
    banner("immersive_heavy/arc", "Zum Lichtbogenofen", 14.5, -1.4, height=0.9, colour="fire"),
    banner("immersive_heavy/fuel", "Öl und Diesel", 13.5, 4.9, height=0.9, colour="brass"),
    banner("immersive_heavy/plastic", "Kunststoff", 14.8, 7.8, height=0.8, colour="magic"),
    banner("immersive_heavy/machines", "Weitere Maschinen", 15, 10.6, height=0.9, colour="water"),
    banner("immersive_heavy/lists", "Checklisten", 10, 14.4, height=0.9, colour="stone"),
    banner("immersive_heavy/tools", "Werkzeuge und Waffen", 13, 19.3, height=0.9, colour="fire"),
]

chapter(C, "Immersive Engineering: Schwerindustrie", "immersiveengineering:heavy_engineering", "tech", quests,
        shape="square", order=31, stage=3,
        subtitle=["Stufe 3: alle großen Multiblöcke, vom Zerkleinerer bis zum Bagger."],
        images=images)
