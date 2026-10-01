"""Immersive Engineering in stage 3: the engineering blocks open, and with them the big
multiblocks. Crusher and metal press, the graphite electrode chain to the arc furnace,
plant oil and ethanol to biodiesel and the diesel generator, duroplast and advanced
electronics, mixer, assembler and the excavator. Continues the stage 2 chapter."""
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
    quest("light", 0, 6.5, "&6&lSchwerindustrie",
          subtitle="Jetzt geht es um die großen Maschinen.",
          description=[
              "Mit &eStufe 3&r öffnen sich die &6Ingenieursbausteine&r, und mit ihnen alle großen Multiblöcke von Immersive Engineering: Zerkleinerer, Metallpresse, Lichtbogenofen, Raffinerie, Dieselgenerator, Bagger und mehr. Gebaut und geformt wird wie bisher: Blöcke aufstellen, mit dem &6Ingenieurshammer&r auf den richtigen Block schlagen. Das Handbuch zeigt dir jede Struktur Schicht für Schicht.",
              "",
              "&eLeichter Ingenieursbaustein:&r Auf Kronwerke steckt Create darin. Vier &6Eisenblechblöcke&r in die Ecken, vier &6Mechanische Eisenkomponenten&r an die Seiten und ein &6Messingblech&r in die Mitte ergeben vier Stück.",
              "",
              "Fast jeder Multiblock in diesem Kapitel braucht welche, der Zerkleinerer und der Lichtbogenofen je zehn. Mach gleich einen Vorrat.",
          ],
          tasks=[task_item("immersiveengineering:light_engineering", 16)],
          rewards=[reward_item("immersiveengineering:component_iron", 8), reward_table("s3_common")],
          icon="immersiveengineering:light_engineering", size=2.0, shape="hexagon"),

    quest("heavy", 2.8, 6.5, "&8&lSchwerer Ingenieursbaustein",
          subtitle="Stahl, Elektrum und ein Präzisionsmechanismus.",
          description=[
              "Der &6Schwere Ingenieursbaustein&r ist das Herz der großen Maschinen. Auf Kronwerke: &6Stahlblechblöcke&r in die vier Ecken, oben in die Mitte ein &6Präzisionsmechanismus&r von Create, links, rechts und unten je eine &6Mechanische Stahlkomponente&r, in die Mitte ein &6Elektrumbarren&r. Das ergibt vier.",
              "",
              "Die Stahlkomponente machst du am &6Ingenieursarbeitstisch&r mit der Blaupause für Komponenten aus zwei Stahlblechen und einem Kupferbarren.",
              "",
              "&eKronwerke:&r In jedem &6Stahlkern&r, dem Meilenstein von Stufe 3, stecken vier Schwere Ingenieursbausteine. Acht Stahlkerne will der Obelisk.",
          ],
          tasks=[task_item("immersiveengineering:heavy_engineering", 8)],
          rewards=[reward_item("immersiveengineering:component_steel", 4), reward_item("immersiveengineering:ingot_electrum", 4), reward_xp(10)],
          deps=["light"], icon="immersiveengineering:heavy_engineering", size=1.75, shape="hexagon"),

    quest("parts", 0, 9.5, "&7Gerüst, Blech und Redstone",
          subtitle="Was sonst noch in jedem Multiblock steckt.",
          description=[
              "&6Redstone-Ingenieursbaustein:&r Eisenblechblöcke in die Ecken, Redstone an die Seiten, ein Kupferbarren in die Mitte ergeben vier. Fast jeder Multiblock hat genau einen davon, das ist sein Steuerpult für Redstone.",
              "",
              "&6Stahlgerüst&r stützt die Maschinen. Drei Stahlbarren oben, drei Stahlstäbe darunter ergeben sechs.",
              "",
              "&6Stahlblechblöcke&r entstehen aus vier Stahlblechen. Der Lichtbogenofen und der Bagger brauchen sie in großer Zahl.",
          ],
          tasks=[task_item("immersiveengineering:rs_engineering", 4), task_item("immersiveengineering:steel_scaffolding_standard", 32),
                 task_item("immersiveengineering:sheetmetal_steel", 16)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 16), reward_item("minecraft:redstone", 16)],
          deps=["light"], icon="immersiveengineering:rs_engineering"),

    # ---- Lichtbogenofen ------------------------------------------------------
    quest("crusher", 6, 0.5, "&7&lZerkleinerer",
          subtitle="Aus einem Erz werden zwei Staub.",
          description=[
              "Der &6Zerkleinerer&r ist fünf Blöcke lang, drei breit und drei hoch. Du brauchst &e10 Leichte Ingenieursbausteine&r, &e10 Stahlgerüste&r, &e8 Stahlzäune&r, &e9 Trichter&r und einen Redstone-Ingenieursbaustein. Geformt wird am mittleren Zaun der langen Seite mit dem Redstone-Baustein.",
              "",
              "&eWas er kann:&r Ein Erzblock wird zu zwei Staub, Rohmetall zu einem Staub mit einer Chance auf einen zweiten. Bruchstein wird zu Kies, Sandstein zu Sand und &6Nitratstaub&r, &6Koks&r zu &6Koksstaub&r. Den Koksstaub brauchst du gleich für den Lichtbogenofen.",
              "",
              "Strom kommt oben an der Schulter hinein, Gegenstände wirfst du in die Walzen. &cWer hineinfällt, kommt als Beute wieder heraus.&r",
          ],
          tasks=[mb("mb_crusher", "Einen Zerkleinerer formen"), task_item("immersiveengineering:dust_coke", 16)],
          rewards=[reward_item("immersiveengineering:coal_coke", 32), reward_table("s3_common"), reward_xp(10)],
          deps=["light"], icon="immersiveengineering:crusher", size=1.5),

    quest("press", 6, 3, "&7Metallpresse",
          subtitle="Bleche, Stäbe und Zahnräder am Fließband.",
          description=[
              "Die &6Metallpresse&r ist drei Blöcke breit und drei hoch, aber nur einen tief. Unten Stahlgerüst, Redstone-Ingenieursbaustein, Stahlgerüst. In der Mitte Förderband, &6Kolben&r, Förderband, beide Bänder in dieselbe Richtung. Oben auf den Kolben ein &6Schwerer Ingenieursbaustein&r. Geformt wird am Kolben.",
              "",
              "&eFormen:&r Ohne Pressform tut sie nichts. Die Formen machst du am &6Ingenieursarbeitstisch&r mit der Blaupause für Formen und setzt sie per Rechtsklick ein. Platte, Stab, Draht, Zahnrad, dazu Formen zum Verpacken in Blöcke.",
              "",
              "Ein Stahlbarren wird zu einem Stahlblech. Das ist der Nachschub für alle Stahlblechblöcke dieses Kapitels.",
          ],
          tasks=[mb("mb_metalpress", "Eine Metallpresse formen"), task_item("immersiveengineering:plate_steel", 32)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 16), reward_xp(10)],
          deps=["heavy"], icon="immersiveengineering:metal_press"),

    quest("squeezer", 8.5, 0.5, "&eIndustriepresse",
          subtitle="Pflanzenöl und HOP-Graphit.",
          description=[
              "Die &6Industriepresse&r ist ein Würfel aus drei mal drei mal drei Blöcken: &e4 Holzfässer&r, ein Kolben, 2 Leichte Ingenieursbausteine, ein Redstone-Ingenieursbaustein, 6 Stahlgerüste, 3 Stahlzäune und 2 Flüssigkeitsrohre. Geformt wird an einem der Fässer, auf der Seite, auf der der Redstone-Baustein steht.",
              "",
              "&eZwei Aufgaben:&r Samen werden zu &6Pflanzenöl&r, Hanfsamen geben am meisten. Und acht &6Koksstaub&r werden zu einem &6HOP-Graphitstaub&r, dem Rohstoff für die Elektroden des Lichtbogenofens.",
              "",
              tex("material_dust_hop_graphite"),
          ],
          tasks=[mb("mb_squeezer", "Eine Industriepresse formen"), task_item("immersiveengineering:dust_hop_graphite", 4)],
          rewards=[reward_item("immersiveengineering:seed", 16), reward_xp(5)],
          deps=["crusher"], icon="immersiveengineering:squeezer"),

    quest("bottling", 11, 0.5, "&bAbfüllanlage",
          subtitle="Flüssigkeit in Formen gießen.",
          description=[
              "Die &6Abfüllanlage&r ist drei breit, drei hoch und zwei tief: &e3 Förderbänder&r in einer Reihe, 2 Flüssigkeitspumpen, 2 Eisenblechblöcke, 2 Leichte Ingenieursbausteine, ein Redstone-Ingenieursbaustein und 3 Stahlgerüste. Geformt wird am mittleren Förderband, die Richtung der Bänder ist wichtig. Spiegeln darfst du sie.",
              "",
              "Sie füllt Eimer, Flaschen und Kanister und gießt Flüssigkeiten in Pressformen. Für die nächste Quest brauchst du die &6Pressform: Stab&r und eine Ladung &6Kreosotöl&r aus dem Koksofen.",
          ],
          tasks=[task_checkmark("Abfüllanlage gebaut und geformt"), task_item("immersiveengineering:mold_rod", 1)],
          rewards=[reward_item("immersiveengineering:creosote_bucket", 2), reward_xp(5)],
          deps=["squeezer", "press"], icon="immersiveengineering:bottling_machine"),

    quest("electrode", 13.5, 0.5, "&8Graphitelektroden",
          subtitle="Drei Stück, und sie verschleißen.",
          description=[
              "In der Abfüllanlage ergeben die &6Pressform: Stab&r, &6vier HOP-Graphitstaub&r und &6ein Eimer Kreosotöl&r eine &6Graphitelektrode&r. Die Form bekommst du zurück.",
              "",
              "Der Lichtbogenofen braucht &edrei Elektroden&r. Jede hält etwa &e80 Minuten&r Dauerbetrieb, dann zerbricht sie. Nachlegen musst du von Hand, das geht nicht automatisch. Halt immer drei in Reserve.",
              "",
              tex("graphite_electrode"),
          ],
          tasks=[task_item("immersiveengineering:graphite_electrode", 3)],
          rewards=[reward_item("immersiveengineering:dust_coke", 16), reward_xp(10)],
          deps=["bottling"], icon="immersiveengineering:graphite_electrode"),

    quest("arc", 16, 0.5, "&c&lLichtbogenofen",
          subtitle="Kein Reaktor. Aber fast so groß.",
          description=[
              "Der &6Lichtbogenofen&r ist fünf mal fünf mal fünf Blöcke groß. Du brauchst: &e27 Verstärkte Sprengziegel&r für die Wanne, &e10 Leichte&r und &e5 Schwere Ingenieursbausteine&r, &e8 Stahlblechblöcke&r, &e14 Stahlblechblockstufen&r, &e6 Stahlblöcke&r, &e5 Stahlgerüste&r, einen Redstone-Ingenieursbaustein und einen &6Kessel&r. Geformt wird am Kessel.",
              "",
              "&eBedienung:&r Oben kommen die drei Elektroden hinein. Links zwölf Eingabeplätze, rechts vier für Zusätze wie Koksstaub. Unten sechs Ausgaben und ein Platz für Schlacke. Eingaben gehen durch die linke Luke oben, Zusätze durch die rechte. Strom kommt über die drei Anschlüsse hinten, die Barren kommen vorne aus dem Becken.",
              "",
              "&eErze:&r Ein Erzblock wird zu zwei Barren, Rohmetall zu einem mit halber Chance auf einen zweiten. Legierungen wie Elektrum, Konstantan und Bronze schmilzt er direkt aus Staub oder Barren. Messing nicht, das bleibt beim Mixer von Create.",
          ],
          tasks=[mb("mb_arcfurnace", "Einen Lichtbogenofen formen")],
          rewards=[reward_item("immersiveengineering:graphite_electrode", 1), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["electrode"], icon="immersiveengineering:arc_furnace", size=2.0, shape="hexagon"),

    quest("arc_steel", 19, 0.5, "&8&lStahl am laufenden Band",
          subtitle="Der Ofen schläft nie.",
          description=[
              "Ein &6Eisenbarren&r als Eingabe und &6Koksstaub&r als Zusatz ergeben im Lichtbogenofen einen &6Stahlbarren&r und etwas Schlacke. Zwölf Plätze laufen gleichzeitig, das ist schneller als jeder Hochofen.",
              "",
              "Mit Trichtern oder Rohren füllst du Eisen und Koksstaub von oben nach, eine Kiste vorne am Becken nimmt den Stahl auf. Der Zerkleinerer liefert den Koksstaub dazu.",
              "",
              "&eKronwerke:&r Das Stufenziel will &e4.000 Stahlbarren&r, und Stahl aus dem Lichtbogenofen zählt genauso wie jeder andere.",
              "",
              tex("metal_ingot_steel"),
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 256)],
          rewards=[reward_item("immersiveengineering:coal_coke", 64), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["arc"], icon="immersiveengineering:ingot_steel", size=1.5),

    # ---- Öl und Diesel -------------------------------------------------------
    quest("fermenter", 8.5, 5.5, "&eIndustriefermenter",
          subtitle="Kartoffeln werden zu Ethanol.",
          description=[
              "Der &6Industriefermenter&r ist fast genauso gebaut wie die Industriepresse, nur mit &e4 Kesseln&r statt der Fässer und &e4 Eisenblechblöcken&r oben statt Kolben und Zäunen. Geformt wird an einem der Kessel, auf der Seite, auf der der Redstone-Baustein steht.",
              "",
              "Er macht &6Ethanol&r aus Kartoffeln, Zuckerrohr, Äpfeln, Melonen, Beeren, Roter Bete und Honig. Eine Kartoffelfarm mit Erntemaschine hält ihn ständig beschäftigt.",
          ],
          tasks=[mb("mb_fermenter", "Einen Industriefermenter formen"), task_item("immersiveengineering:ethanol_bucket", 1)],
          rewards=[reward_item("minecraft:potato", 32), reward_xp(5)],
          deps=["squeezer"], icon="immersiveengineering:fermenter"),

    quest("refinery", 11, 5.5, "&6&lRaffinerie",
          subtitle="Öl und Ethanol werden Biodiesel.",
          description=[
              "Die &6Raffinerie&r ist fünf lang, drei breit und drei hoch: &e16 Eisenblechblöcke&r, 2 Leichte und 2 Schwere Ingenieursbausteine, ein Redstone-Ingenieursbaustein, 8 Stahlgerüste und 5 Flüssigkeitsrohre. Geformt wird am Schweren Ingenieursbaustein in der mittleren Schicht.",
              "",
              "&eBiodiesel:&r Gleich viel &6Pflanzenöl&r und &6Ethanol&r ergeben doppelt so viel Biodiesel. Dafür braucht sie einen Katalysator: &6Nitratstaub&r, den der Zerkleinerer aus Sandstein holt. Den Katalysator legst du von Hand ein, er wird nicht verbraucht.",
              "",
              "Die Flüssigkeiten kommen seitlich hinein, das Ergebnis vorne am orange markierten Anschluss heraus.",
          ],
          tasks=[mb("mb_refinery", "Eine Raffinerie formen"), task_item("immersiveengineering:biodiesel_bucket", 1)],
          rewards=[reward_item("immersiveengineering:dust_saltpeter", 4), reward_table("s3_common"), reward_xp(15)],
          deps=["fermenter", "squeezer"], icon="immersiveengineering:refinery", size=1.5),

    quest("diesel", 13.5, 5.5, "&c&lDieselgenerator",
          subtitle="Echte Hochspannung.",
          description=[
              "Der &6Dieselgenerator&r ist drei breit, drei hoch und fünf lang: &e13 Schwere Ingenieursbausteine&r, &e9 Kühlerblöcke&r, &e4 Generatorblöcke&r, 6 Stahlgerüste, 5 Flüssigkeitsrohre und ein Redstone-Ingenieursbaustein. Geformt wird am mittleren Generatorblock.",
              "",
              "&eLeistung:&r &e4.096 Flux pro Tick&r, verteilt auf bis zu drei Anschlüsse über dem Generator. Er läuft nur, wenn jemand den Strom abnimmt. Für so viel Leistung brauchst du HV-Leitungen.",
              "",
              "&eTreibstoff:&r Kreosotöl geht zur Not, Biodiesel hält mehr als zwölfmal so lange. Mischt du in der Raffinerie Biodiesel mit etwas flüssigem Stärketrank, entsteht &6Hochcetan-Biodiesel&r, der noch ein Viertel länger brennt.",
          ],
          tasks=[mb("mb_dieselgen", "Einen Dieselgenerator formen")],
          rewards=[reward_item("immersiveengineering:wirecoil_steel", 16), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["refinery"], icon="immersiveengineering:diesel_generator", size=1.75, shape="hexagon"),

    quest("electronics", 11, 8.3, "&dDuroplast und Elektronik",
          subtitle="Kunststoff aus der Raffinerie.",
          description=[
              "&eDer Weg zum Kunststoff:&r In der Raffinerie wird Ethanol mit einem &6Silberblech&r als Katalysator zu &6Acetaldehyd&r. Acetaldehyd und Kreosotöl ergeben &6Phenolharz&r. In der Abfüllanlage gießt du das Harz in die Pressform: Platte und bekommst &6Duroplastplatten&r.",
              "",
              "Am Ingenieursarbeitstisch werden eine Duroplastplatte, zwei &6Vakuumröhren&r und ein &6Aluminiumkabel&r zur &6Fortgeschrittenen Elektronikkomponente&r. Die gibt es erst ab Stufe 3, und die besseren Maschinen von Immersive Engineering wie die Teslaspule brauchen sie.",
              "",
              tex("material_component_electronic_adv"),
          ],
          tasks=[task_item("immersiveengineering:plate_duroplast", 4), task_item("immersiveengineering:component_electronic_adv", 2)],
          rewards=[reward_item("immersiveengineering:electron_tube", 4), reward_xp(15)],
          deps=["refinery"], icon="immersiveengineering:component_electronic_adv"),

    # ---- Weitere Maschinen ---------------------------------------------------
    quest("mixer", 6, 11.5, "&9Mischer",
          subtitle="Beton, Tränke und Säure.",
          description=[
              "Der &6Mischer&r ist drei mal drei mal drei: &e4 Leichte Ingenieursbausteine&r, 4 Eisenblechblöcke, 5 Stahlgerüste, ein Stahlzaun, 3 Flüssigkeitsrohre und ein Redstone-Ingenieursbaustein. Geformt wird am mittleren Eisenblechblock.",
              "",
              "Er löst Feststoffe in Flüssigkeiten. Zwei Sand, ein Kies und ein Ton in Wasser ergeben &6Flüssigbeton&r. Redstone in Wasser wird &6Redstonesäure&r für die Akkus, und mit den richtigen Zutaten mischt er ganze Tanks voller &6Tränke&r, die du in der Abfüllanlage in Flaschen füllst.",
          ],
          tasks=[mb("mb_mixer", "Einen Mischer formen")],
          rewards=[reward_item("minecraft:sand", 32), reward_item("minecraft:clay_ball", 16), reward_xp(10)],
          deps=["parts"], icon="immersiveengineering:mixer"),

    quest("assembler", 8.5, 11.5, "&9Monteur",
          subtitle="Eine Werkbank, die selbst arbeitet.",
          description=[
              "Der &6Monteur&r ist drei mal drei mal drei: &e9 Eisenblechblöcke&r, 6 Eisenblechblockstufen, 6 Stahlgerüste, 2 Leichte und 2 Redstone-Ingenieursbausteine und &e2 Förderbänder&r. Geformt wird am nach innen zeigenden Förderband.",
              "",
              "Er speichert drei Rezepte und arbeitet sie der Reihe nach ab, das Ergebnis des ersten darf Zutat des zweiten sein. In seine drei Tanks kannst du Flüssigkeiten pumpen, die dann Eimer in Rezepten ersetzen.",
          ],
          tasks=[task_checkmark("Monteur gebaut und geformt")],
          rewards=[reward_item("immersiveengineering:conveyor_basic", 8), reward_xp(10)],
          deps=["mixer"], icon="immersiveengineering:assembler", optional=True),

    quest("excavator", 13.5, 11.5, "&6&lBagger",
          subtitle="Erzadern, die keine Spitzhacke erreicht.",
          description=[
              "Tief im Gestein liegen &6Mineraladern&r. Mit den &6Mineralvermessungswerkzeugen&r findest du ihre Spur, ein &6Kernprobenbohrer&r verrät dir genau, was drin ist und wie ergiebig die Ader ist.",
              "",
              "&eDer Bagger&r besteht aus zwei Teilen. Der Motor ist drei breit, drei hoch und sechs lang: &e16 Stahlblechblöcke&r, &e9 Leichte&r und &e4 Schwere Ingenieursbausteine&r, 3 Kühlerblöcke, 6 Stahlgerüste und ein Redstone-Ingenieursbaustein. Das Schaufelrad ist sieben mal sieben, aus &e9 Stahlblöcken&r und &e20 Stahlgerüsten&r. Geformt wird alles zusammen am hinteren mittleren Schweren Ingenieursbaustein.",
              "",
              "Er frisst &e4.096 Flux pro Tick&r, ein Dieselgenerator pro Bagger ist also Pflicht. Eine Ader gibt höchstens 38.400 Erze her.",
          ],
          tasks=[mb("mb_excavator", "Einen Bagger formen"), task_item("immersiveengineering:coresample", 1)],
          rewards=[reward_item("immersiveengineering:ingot_steel", 32), reward_table("s3_uncommon"), reward_xp(20)],
          deps=["diesel"], icon="immersiveengineering:excavator", size=1.75, shape="hexagon"),

    # ---- Abschluss -----------------------------------------------------------
    quest("final", 19, 6, "&c&lDer Ofen schläft nie",
          subtitle="Ein Stahlwerk für den ganzen Server.",
          description=[
              "Lichtbogenofen, Dieselgenerator, Raffinerie: Du hast jetzt alles, was Immersive Engineering an Schwerindustrie kennt. Zeit, es laufen zu lassen.",
              "",
              "&eKronwerke:&r Das Stufenziel &e\"Der Ofen schläft nie\"&r will &e4.000 Stahlbarren&r, &e250 Fortgeschrittene Steuerschaltkreise&r aus Mekanism und &e8 Stahlkerne&r. Jeder Stahlkern braucht vier Schwere Ingenieursbausteine, einen Fortgeschrittenen Steuerschaltkreis, zwei Ingenieursprozessoren aus AE2, ein Stahlgehäuse und einen Elementiumbarren. Den Stahl und die Bausteine kann dieses Kapitel liefern. Stell eine Kiste neben den Obelisken und häng deine Stahlstraße daran.",
          ],
          tasks=[task_item("immersiveengineering:ingot_steel", 1024), task_item("immersiveengineering:heavy_engineering", 32)],
          rewards=[reward_table("s3_rare"), reward_item("immersiveengineering:storage_steel", 8), reward_xp(30)],
          deps=["arc_steel", "diesel", "electronics"], icon="immersiveengineering:storage_steel", size=2.5, shape="gear"),
]

images = [
    banner("immersive_heavy/title", "Schwerindustrie", 10, -3.4, height=1.5, kind="title", colour="fire"),
    banner("immersive_heavy/blocks", "Bausteine", -0.5, 3.6, height=0.9, colour="stone"),
    banner("immersive_heavy/arc", "Lichtbogenofen", 12.5, -1.4, height=0.9, colour="fire"),
    banner("immersive_heavy/fuel", "Öl und Diesel", 13.8, 3.3, height=0.9, colour="brass"),
    banner("immersive_heavy/machines", "Weitere Maschinen", 8.5, 9.9, height=0.9, colour="water"),
]

chapter(C, "Immersive Engineering: Schwerindustrie", "immersiveengineering:heavy_engineering", "tech", quests,
        shape="square", order=31, stage=3,
        subtitle=["Stufe 3: Zerkleinerer, Lichtbogenofen, Biodiesel, Dieselgenerator und Bagger."],
        images=images)
