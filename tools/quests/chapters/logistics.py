"""Logistics in stage 3, one step per quest: Integrated Dynamics (menril, cables and cards,
readers, the logic programmer, writers) with Tunnels, Terminals and Crafting; XNet (controller,
connectors, advanced connectors, logic channels, routers); LaserIO (nodes, item, energy, fluid
and chemical cards, filters); Compact Machines; Mining Gadgets and its upgrades. None of these
recipes are changed by Kronwerke. Tier 3 mining gadget upgrades are stage 4 and only named.
Pipez and Modular Routers live in pipes.py, the overview of all transport in list_transport.py."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp, banner)

C = "logistics"


def head(name, text, left, y, height=0.9, kind="section", colour="water"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Start -----------------------------------------------------------------
    quest("welcome", 0, 9, "&3&lBau Squeezer und Drying Basin",
          subtitle="Der Einstieg in Integrated Dynamics.",
          description=[
              "&6Squeezer:&r Stöcke an den Seiten, ein Eisenblock oben in der Mitte, unten Bretter und ein Eisenbarren. &6Drying Basin:&r Stämme, schwarzer Farbstoff oben und unten, Eisen an den Seiten.",
              "",
              "Dieses Kapitel sammelt die Mods, die Dinge ohne Rohrsalat bewegen: &6Integrated Dynamics&r (programmierbar), &6XNet&r (alles an einem Controller), &6LaserIO&r (Laser statt Kabel), dazu &6Compact Machines&r und den &6Mining Gadget&r. Die Abschnitte gehen in beliebiger Reihenfolge.",
              "",
              "Einfache Rohre und Router stehen im Kapitel &bRohre und Router&r, ein Überblick über alles im Kapitel &6Checkliste: Transport und Lager&r.",
          ],
          tasks=[task_item("integrateddynamics:squeezer", 1), task_item("integrateddynamics:drying_basin", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_table("s3_common")],
          icon="xnet:controller", size=2.0, shape="hexagon"),

    # ---- Integrated Dynamics -------------------------------------------------
    quest("menril", 3, 0, "&9Press Menril-Harz",
          subtitle="Blaue Bäume voller Harz.",
          description=[
              "Leg einen &6Menril Log&r auf den Squeezer und spring darauf, bis er platt ist. Das gibt &d1 000 mB Menril Resin&r, das ins Drying Basin daneben fließt und zu einem &6Crystalized Menril Block&r trocknet. An der Werkbank gibt der Block neun &6Chunks&r.",
              "",
              "&6Menril-Bäume&r sind hoch und blau mit leuchtenden Blättern, am leichtesten im &6Meneglin&r-Biom. Nimm Setzlinge mit. Ein Redstone-Signal setzt den Squeezer zurück.",
          ],
          tasks=[task_item("integrateddynamics:crystalized_menril_chunk", 32)],
          rewards=[reward_item("integrateddynamics:crystalized_menril_chunk", 16), reward_xp(5)],
          deps=["welcome"], icon="integrateddynamics:menril_log"),

    quest("mechanical", 3, 2, "&9Lass Maschinen pressen",
          subtitle="Squeezer und Basin mit Strom.",
          description=[
              "&6Energy Battery:&r Menril-Chunks, zwei Menril-Blöcke und ein Redstoneblock. &6Mechanical Squeezer:&r Squeezer zwischen zwei Batterien, Diamant oben, Obsidian unten. &6Mechanical Drying Basin:&r Basin zwischen zwei Batterien, Obsidian oben und unten.",
              "",
              "Kein Springen mehr. Das mechanische Basin trocknet Menril Glass in 20 statt 200 Ticks.",
          ],
          tasks=[task_item("integrateddynamics:mechanical_squeezer", 1), task_item("integrateddynamics:mechanical_drying_basin", 1)],
          rewards=[reward_item("minecraft:obsidian", 4), reward_xp(6)],
          deps=["menril"], icon="integrateddynamics:mechanical_squeezer", optional=True),

    quest("cables", 5.5, 0, "&9Bau Logic Cables und Variable Cards",
          subtitle="Das Netz und seine Notizzettel.",
          description=[
              "&6Logic Cable:&r Menril-Chunks, zwei Stöcke und ein Redstone, gibt drei. &6Variable Card:&r acht Chunks um ein Papier, gibt 24.",
              "",
              "Kabel bilden das Netz, an das du alle Teile steckst. Eine Variable Card speichert einen Verweis auf einen Wert: eine Zahl, einen Gegenstand, eine Liste oder eine Rechenvorschrift. Aus Karten, Chunks und Kolben baust du die &6Variable Transformers&r, die in jedem Reader und Writer stecken.",
          ],
          tasks=[task_item("integrateddynamics:cable", 16), task_item("integrateddynamics:variable", 16)],
          rewards=[reward_item("minecraft:paper", 16), reward_xp(5)],
          deps=["menril"], icon="integrateddynamics:cable"),

    quest("reader", 8, 0, "&9Lies einen Wert und zeig ihn an",
          subtitle="Redstone Reader und Display Panel.",
          description=[
              "&6Redstone Reader:&r ein Redstoneblock über Redstone, Input-Transformer, Redstone. Setz ihn an ein Kabel, ziel auf eine Redstonefackel, öffne ihn und leg eine leere Variable Card in den Aspekt &eRedstone Value&r.",
              "",
              "Ein &6Display Panel&r am selben Netz zeigt den Wert, sobald die Karte darin liegt. So arbeiten alle Reader: Block, Fluid, Inventory, Entity, Machine.",
          ],
          tasks=[task_item("integrateddynamics:part_redstone_reader", 1), task_item("integrateddynamics:part_display_panel", 1)],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_xp(6)],
          deps=["cables"], icon="integrateddynamics:part_redstone_reader"),

    quest("programmer", 10.5, 0, "&9&lSchreib Karten im Logic Programmer",
          subtitle="Zahlen, Listen, Vergleiche.",
          description=[
              "&6Logic Programmer:&r formlos aus Crystalized Menril Block und Werkbank. &6Variable Store:&r Chunks, zwei Menril-Blöcke und eine Truhe.",
              "",
              "Im Programmer baust du eigene Karten: feste Zahlen, Gegenstände, Listen und Operatoren wie Addition oder Vergleich. Karten, auf die andere Karten verweisen, müssen im Netz liegen, am besten im Variable Store.",
              "",
              "Das Buch &6On the Dynamics of Integration&r erklärt alles Schritt für Schritt, mit Übungen.",
          ],
          tasks=[task_item("integrateddynamics:logic_programmer", 1), task_item("integrateddynamics:variablestore", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_table("s3_common"), reward_xp(10)],
          deps=["reader"], icon="integrateddynamics:logic_programmer", size=1.5, shape="hexagon"),

    quest("writer", 8, 2.5, "&9Schalte eine Lampe mit einer Karte",
          subtitle="Der Redstone Writer.",
          description=[
              "&6Redstone Writer:&r ein Redstoneblock über Redstone, Output-Transformer, Redstone. Leg eine Karte mit Wahr oder Falsch in den Aspekt &eBoolean&r, dann gibt er Redstone aus.",
              "",
              "Mit einer Vergleichskarte aus dem Programmer schaltet er nur, wenn eine Bedingung stimmt: Kiste voll, Tank leer, Tag oder Nacht.",
          ],
          tasks=[task_item("integrateddynamics:part_redstone_writer", 1)],
          rewards=[reward_item("minecraft:redstone_lamp", 4), reward_xp(6)],
          deps=["programmer"], icon="integrateddynamics:part_redstone_writer"),

    quest("tunnels", 13, 0, "&3Beweg Gegenstände mit Integrated Tunnels",
          subtitle="Interface, Importer, Exporter.",
          description=[
              "&6Item Interface:&r Chunks mit einer Truhe, gibt vier. Interface plus Input-Transformer ist der &6Item Importer&r, plus Output-Transformer der &6Item Exporter&r.",
              "",
              "Interfaces an Truhen machen deren Inhalt zum Lager des Netzes. Ein Importer mit leerer Variable Card holt alles aus seinem Ziel, ein Exporter liefert, was auf seiner Karte steht.",
          ],
          tasks=[task_item("integratedtunnels:part_interface_item", 2), task_item("integratedtunnels:part_exporter_item", 1),
                 task_item("integratedtunnels:part_importer_item", 1)],
          rewards=[reward_item("minecraft:chest", 8), reward_xp(6)],
          deps=["programmer"], icon="integratedtunnels:part_interface_item"),

    quest("fluid_energy", 13, 2.5, "&3Beweg Flüssigkeiten und Strom",
          subtitle="Dieselben Teile, andere Fracht.",
          description=[
              "&6Fluid Interface:&r Chunks mit einem Eimer. &6Energy Interface:&r Chunks mit einer Energy Battery. Mit Transformern werden daraus Importer und Exporter, wie bei Gegenständen.",
              "",
              "Ein Netz mit allen drei Sorten ersetzt Rohre, Kabel und Förderbänder in einer Werkstatt.",
          ],
          tasks=[task_item("integratedtunnels:part_interface_fluid", 1), task_item("integratedtunnels:part_exporter_energy", 1)],
          rewards=[reward_item("minecraft:bucket", 4), reward_xp(6)],
          deps=["tunnels"], icon="integratedtunnels:part_interface_fluid", optional=True),

    quest("terminal", 15.5, 0, "&3Bau ein Storage Terminal",
          subtitle="Alles auf einen Blick.",
          description=[
              "Glowstone, &6Menril Glass&r (Glas im Drying Basin mit 1 000 mB Harz), beide Transformer und ein Display Panel ergeben das &6Storage Terminal&r.",
              "",
              "Es zeigt alles hinter den Interfaces, mit Reitern für Gegenstände, Flüssigkeiten und Strom. Suche: Text im Namen, &e@&r nach Mod, &e#&r im Tooltip, &e$&r nach Tags. Ein Enderauge darauf schaltet einen Reiter für deine Endertruhe frei.",
          ],
          tasks=[task_item("integratedterminals:part_terminal_storage", 1)],
          rewards=[reward_item("integrateddynamics:crystalized_menril_chunk", 16), reward_xp(6)],
          deps=["tunnels"], icon="integratedterminals:part_terminal_storage"),

    quest("crafting", 18, 0, "&3Lass das Netz craften",
          subtitle="Autocrafting, selbst geschrieben.",
          description=[
              "&6Crafting Interface:&r Eisen, Werkbänke, beide Transformer und ein Menril-Block. &6Crafting Writer:&r Werkbank, Output-Transformer, Werkbank.",
              "",
              "Das Interface schaut auf eine Werkbank oder Maschine und bekommt Rezepte als Karten, die du im Programmer &eselbst&r baust. Ein grüner Haken zeigt ein gültiges Rezept. Der Writer startet Aufträge.",
              "",
              "Mehr Arbeit als bei AE2, dafür knüpfst du jeden Auftrag an eigene Bedingungen.",
          ],
          tasks=[task_item("integratedcrafting:part_interface_crafting", 1), task_item("integratedcrafting:part_crafting_writer", 1)],
          rewards=[reward_item("minecraft:crafting_table", 4), reward_xp(10)],
          deps=["terminal"], icon="integratedcrafting:part_interface_crafting", optional=True),

    quest("counter", 10.5, 2.5, "&6&lBau den Stahlzähler",
          subtitle="Wie viel fehlt noch zum Obelisken?",
          description=[
              "Ein &6Inventory Reader&r (Input-Transformer unter drei Truhen) auf eine Pufferkiste vor dem Obelisken liest mit &eInventory Count&r, was darin liegt. Die Karte ins Display Panel, und du siehst den Stand von weitem.",
              "",
              "Vergleich im Programmer mit einer festen Zahl, ein Redstone Writer schaltet eine Lampe, sobald genug Stahl bereitliegt. Ein Item Exporter schiebt den Stapel dann in die Kiste am Obelisken.",
              "",
              "&eKronwerke:&r &e\"Der Ofen schläft nie\"&r will &e4 000 Stahlbarren&r, &e250 Fortgeschrittene Steuerschaltkreise&r und &e8 Stahlkerne&r. Was in die Kiste am Obelisken fällt, zählt für den, der sie hingestellt hat.",
          ],
          tasks=[task_item("integrateddynamics:part_inventory_reader", 1), task_item("mekanism:ingot_steel", 64)],
          rewards=[reward_table("s3_rare"), reward_item("mekanism:ingot_steel", 32), reward_xp(25)],
          deps=["writer", "tunnels"], icon="integrateddynamics:part_display_panel", size=2.5, shape="gear"),

    # ---- XNet ------------------------------------------------------------------
    quest("xnet_controller", 3, 6, "&eBau einen XNet Controller",
          subtitle="Ein Block, der alles steuert.",
          description=[
              "&6Machine Frame&r von RFTools Base (Eisen, blauer Farbstoff, Goldnuggets), dazu Komparator, Repeater, Redstone, Eisen und Gold: der &6Controller&r.",
              "",
              "Er hat &e8 Kanäle&r, jeder vom Typ &6Item&r, &6Fluid&r, &6Energy&r oder &6Logic&r. Im Kanal legst du fest, welche Blöcke abgeben und welche bekommen. Strom: 1 RF/t pro aktivem Kanal, ein Kabel vom Netz reicht.",
          ],
          tasks=[task_item("rftoolsbase:machine_frame", 1), task_item("xnet:controller", 1)],
          rewards=[reward_item("minecraft:comparator", 4), reward_xp(5)],
          deps=["welcome"], icon="xnet:controller", size=1.5, shape="hexagon"),

    quest("xnet_connectors", 5.5, 6, "&eSetz Connectors und Kabel",
          subtitle="Dünn, bunt, unauffällig.",
          description=[
              "Ein &6Connector&r neben jede Maschine oder Truhe, &6Network Cables&r von dort zum Controller. Vier Farben, verschiedene Farben verbinden sich nicht, so laufen zwei Netze dicht nebeneinander.",
              "",
              "Gib jedem Connector einen Namen. Im Controller legst du einen Kanal an, klickst beim Connector auf das Feld des Kanals und stellst &eeinfügen&r oder &eherausziehen&r, Priorität und Filter ein. &6Facades&r verstecken Kabel hinter Blöcken.",
          ],
          tasks=[task_item("xnet:connector_blue", 4), task_item("xnet:netcable_blue", 32)],
          rewards=[reward_item("xnet:netcable_blue", 32), reward_xp(5)],
          deps=["xnet_controller"], icon="xnet:connector_blue"),

    quest("xnet_advanced", 8, 6, "&eRüste auf Advanced Connector auf",
          subtitle="Mehr Durchsatz, jede Seite.",
          description=[
              "Connector, Diamant, Enderperle, Redstone gibt den &6Advanced Connector&r. Stehende Connectors rüstest du mit dem &6Connector Upgrade Kit&r (Papier, Enderperle, Diamant, Redstone) per Schleich-Rechtsklick auf.",
              "",
              "Er spricht jede Seite des Blocks an, wichtig bei Mekanism-Maschinen. Bis &d100 000 RF/t&r statt 10 000 und &b5 000 mB&r pro Vorgang statt 1 000.",
              "",
              "&eKronwerke:&r Ein Energy- und ein Item-Kanal versorgen eine ganze Stahlstraße: Strom an alle Infusionsanlagen, Kohle und Eisen hinein, Stahl in die Kiste am Obelisken.",
          ],
          tasks=[task_item("xnet:advanced_connector_blue", 2)],
          rewards=[reward_item("minecraft:diamond", 2), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["xnet_connectors"], icon="xnet:advanced_connector_blue"),

    quest("xnet_logic", 10.5, 6, "&eSchalte mit einem Logic-Kanal",
          subtitle="Sensoren und Redstone im Controller.",
          description=[
              "Leg einen Kanal vom Typ &6Logic&r an. Ein Connector als &eSensor&r misst Gegenstände, Flüssigkeit, Energie oder Redstone im Block daneben und setzt eine Farbe. Ein Connector als &eOutput&r gibt bei dieser Farbe Redstone aus.",
              "",
              "Andere Kanäle hören auf diese Farben. So läuft ein Item-Kanal nur, solange der Zieltank nicht voll ist. Für reine Redstone-Signale gibt es den &6Redstone Proxy&r (Machine Frame in Redstone).",
          ],
          tasks=[task_item("xnet:redstone_proxy", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(8)],
          deps=["xnet_advanced"], icon="xnet:redstone_proxy", optional=True),

    quest("xnet_router", 13, 6, "&eVerbinde Controller mit einem Router",
          subtitle="Mehr als acht Kanäle.",
          description=[
              "&6Router:&r Machine Frame, Antriebsschienen, Komparator, Redstone, Eisen und eine Enderperle. Dazu &6Routing Cables&r (Faden, schwarzer Farbstoff, Redstone, Goldnugget, gibt 32) und ein &6Routing Connector&r am Controller.",
              "",
              "Im Controller veröffentlichst du einen Kanal, der Router reicht ihn an andere Controller weiter, bis zu &e32&r Kanäle pro Router. Der &6Wireless Router&r mit Antenne obendrauf macht das ohne Kabel.",
          ],
          tasks=[task_item("xnet:router", 1), task_item("xnet:netcable_routing", 8)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(10)],
          deps=["xnet_advanced"], icon="xnet:router"),

    # ---- LaserIO -------------------------------------------------------------
    quest("laser_node", 3, 10, "&cVerbinde zwei Laser Nodes",
          subtitle="Logistik ohne Kabel.",
          description=[
              "&6Logic Chip:&r Redstone, Goldnuggets, Ton und ein Quarzblock gibt vier Rohlinge, im Ofen gebrannt. Chip, Glas, Redstone und Eisen ergeben einen &6Laser Connector&r, Connector in Eisen und Glasscheiben einen &6Laser Node&r.",
              "",
              "Mit dem &6Laser Wrench&r klickst du einen Node an, dann einen zweiten. Höchstens &e8 Blöcke&r Abstand, für weitere Strecken setzt du Laser Connectors dazwischen. Alle verbundenen Nodes bilden ein Netz.",
          ],
          tasks=[task_item("laserio:laser_node", 2), task_item("laserio:laser_wrench", 1)],
          rewards=[reward_item("laserio:logic_chip", 4), reward_xp(5)],
          deps=["welcome"], icon="laserio:laser_node", size=1.5, shape="hexagon"),

    quest("laser_cards", 5.5, 10, "&cSteck eine Item Card",
          subtitle="Was, wohin, auf welchem Kanal.",
          description=[
              "&6Item Card:&r Redstone, Lapis, Netherquarz, ein Logic Chip und drei Goldnuggets. Öffne einen Node, wähle eine Seite und steck die Karte hinein.",
              "",
              "&eModi:&r &eExtract&r zieht aus dem Block, &eInsert&r legt hinein, &eStock&r hält einen Bestand. Karten finden sich über ihren &eKanal&r: Extract auf Kanal 0 liefert an Insert auf Kanal 0. Prioritäten und Round Robin verteilen die Last.",
          ],
          tasks=[task_item("laserio:card_item", 2)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["laser_node"], icon="laserio:card_item"),

    quest("laser_energy", 8, 9, "&cSchick Strom per Laser",
          subtitle="Bis zu einer Million FE pro Tick.",
          description=[
              "&6Energy Card:&r wie die Item Card, nur mit einem Redstoneblock statt Lapis.",
              "",
              "Eine Energy Card schafft bis zu &d1 000 000 FE/t&r. Eine Extract-Karte am Generator, Insert-Karten an jeder Maschine, fertig ist das Stromnetz ohne Kabel.",
          ],
          tasks=[task_item("laserio:card_energy", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_table("s3_common"), reward_xp(6)],
          deps=["laser_cards"], icon="laserio:card_energy"),

    quest("laser_fluid", 8, 11, "&cPump Flüssigkeit und Gas per Laser",
          subtitle="Fluid Card und Chemical Card.",
          description=[
              "&6Fluid Card:&r mit einem Eimer statt Lapis. &6Chemical Card:&r mit einem Einfachen Steuerschaltkreis von Mekanism. Die Redstone Card überträgt Signale.",
              "",
              "Die Chemical Card bewegt Mekanism-Gase wie Wasserstoff oder Chlor zwischen Maschinen, ganz ohne Druckrohre.",
          ],
          tasks=[task_item("laserio:card_fluid", 1), task_item("laserio:card_chemical", 1)],
          rewards=[reward_item("minecraft:bucket", 2), reward_xp(6)],
          deps=["laser_cards"], icon="laserio:card_fluid"),

    quest("laser_upgrades", 10.5, 10, "&cFiltere und übertakte",
          subtitle="Feiner sortieren, schneller schieben.",
          description=[
              "Der &6Basic Filter&r in einer Karte lässt nur bestimmte Gegenstände durch oder sperrt sie, dazu gibt es Filter nach Anzahl, Tag, Mod und Daten. Der &6Card Overclocker&r erhöht, wie viel eine Karte pro Vorgang bewegt, der &6Node Overclocker&r (Diamanten, Redstone, Logic Chip) macht den ganzen Node schneller.",
              "",
              "Der &6Card Holder&r trägt Karten griffbereit, der &6Card Cloner&r kopiert eine eingestellte Karte.",
          ],
          tasks=[task_item("laserio:filter_basic", 1), task_item("laserio:overclocker_card", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(8)],
          deps=["laser_energy", "laser_fluid"], icon="laserio:overclocker_card", optional=True),

    # ---- Compact Machines ------------------------------------------------------
    quest("cm_psd", 3, 14, "&dBau ein Personal Shrinking Device",
          subtitle="Klein genug, um hineinzugehen.",
          description=[
              "Acht polierte Tiefenschiefer im Kreis ergeben acht &6Compact Machine Walls&r. &6Atom Shrinking&r und &6Atom Enlarging Module&r: Knöpfe, Enderauge, Wägeplatte, Kolben (klebrig beim Shrinking Module). Beide Module mit Eisen, Kupfer, Glas und Enderauge: das &6PSD&r.",
              "",
              "Mit dem PSD betrittst und verlässt du jede Maschine.",
          ],
          tasks=[task_item("compactmachines:wall", 16), task_item("compactmachines:personal_shrinking_device", 1)],
          rewards=[reward_item("minecraft:ender_eye", 4), reward_xp(5)],
          deps=["welcome"], icon="compactmachines:personal_shrinking_device", size=1.5, shape="hexagon"),

    quest("cm_machine", 5.5, 14, "&dBetritt eine Compact Machine",
          subtitle="Innen größer als außen.",
          description=[
              "Sechs Wände, die beiden Module und ein Kern ergeben eine &6Compact Machine&r. Der Kern bestimmt die Größe: Kupfer 3, Eisen 5, Gold 7, Diamant 9, Obsidian 11, Netherit 13 Blöcke im Würfel. Eine Diamanthacke gibt einen flachen Farmraum mit Gras.",
              "",
              "Rechtsklick mit dem PSD, und du stehst drin. Baust du die Maschine ab, bleibt der Raum mit ihr verbunden.",
              "",
              "&cWichtig:&r In dieser Version gibt es keine Tunnel. Nichts geht durch die Wände. Ein Raum ist Werkstatt, Lager oder Farm, kein Teil einer Leitung.",
          ],
          tasks=[task_item("compactmachines:new_machine", 1)],
          rewards=[reward_item("compactmachines:wall", 16), reward_table("s3_common"), reward_xp(10)],
          deps=["cm_psd"], icon="compactmachines:new_machine"),

    # ---- Mining Gadgets --------------------------------------------------------
    quest("mg_gadget", 3, 18, "&bBau einen Mining Gadget",
          subtitle="Ein Laser statt einer Spitzhacke.",
          description=[
              "&6Blank Upgrade Module:&r Redstone, Lapis, Diamanten und eine Glasscheibe. Daraus mit Diamanten, Eisen, Gold und Redstone der &6Mining Gadget&r.",
              "",
              "Rechte Maustaste halten, und der Laser baut ab, worauf du zielst. Er fasst &d1 000 000 FE&r, ein Block kostet etwa 200 FE. Aufladen geht zum Beispiel im Ladeplatz eines Mekanism-Energiewürfels. Schleich-Rechtsklick öffnet Größe, Reichweite und Modus.",
          ],
          tasks=[task_item("mininggadgets:mininggadget_simple", 1)],
          rewards=[reward_item("minecraft:diamond", 3), reward_xp(5)],
          deps=["welcome"], icon="mininggadgets:mininggadget_simple", size=1.5, shape="hexagon"),

    quest("mg_upgrades", 5.5, 18, "&bBau einen Modification Table",
          subtitle="Upgrades einbauen, und gleich das erste.",
          description=[
              "&6Modification Table:&r Eisen oben und unten, Redstone und ein Blank Upgrade Module in der Mitte. &63x3-Upgrade:&r Redstoneblöcke, ein Diamantblock, Enderperlen und eine Diamantspitzhacke um ein Blank Module.",
              "",
              "Gadget in den Tisch, Upgrade auf den freien Platz ziehen. Jedes Upgrade erhöht den Stromverbrauch pro Block, schau auf den Tooltip. &65x5&r folgt aus dem 3x3.",
          ],
          tasks=[task_item("mininggadgets:modificationtable", 1), task_item("mininggadgets:upgrade_size_1", 1)],
          rewards=[reward_item("minecraft:redstone_block", 4), reward_xp(8)],
          deps=["mg_gadget"], icon="mininggadgets:modificationtable"),

    quest("mg_fortune", 8, 17.3, "&bWähl Glück oder Behutsamkeit",
          subtitle="Nur eins von beiden passt hinein.",
          description=[
              "&6Fortune I:&r Lapisblöcke und Eisenblöcke um ein Blank Module. &6Silk Touch:&r Schleimbälle, Gold und ein Goldener Apfel um ein Blank Module.",
              "",
              "Glück für Erz, Behutsamkeit für Glas und Erzblöcke. Pro Block kostet Fortune I &d30 FE&r extra, Silk Touch &d100 FE&r. &cStufe 4:&r Fortune III, 7x7, Battery III, Range III und Efficiency III.",
          ],
          tasks=[task_item("mininggadgets:upgrade_fortune_1", 1)],
          rewards=[reward_item("minecraft:lapis_block", 4), reward_table("s3_uncommon"), reward_xp(8)],
          deps=["mg_upgrades"], icon="mininggadgets:upgrade_fortune_1"),

    quest("mg_magnet", 8, 19, "&bSammle ein und wirf Müll weg",
          subtitle="Magnet und Void Junk.",
          description=[
              "&6Magnet:&r Redstone, Gold und Eisen um ein Blank Module. &6Void Junk:&r Redstone, Obsidian und Enderperlen um ein Blank Module.",
              "",
              "Der Magnet sammelt alles ein, Void Junk vernichtet Bruchstein, Erde und Co. Denk daran: Bruchstein zählt für den Obelisken nur in Stufe 1. Gegen Lava und Wasser hilft das &6Freezing&r-Upgrade.",
          ],
          tasks=[task_item("mininggadgets:upgrade_magnet", 1), task_item("mininggadgets:upgrade_void_junk", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(8)],
          deps=["mg_upgrades"], icon="mininggadgets:upgrade_magnet", optional=True),
]

images = [
    head("title", "Logistik", 0, -4, height=1.75, kind="title", colour="water"),
    head("id", "Integrated Dynamics", 3, -1.6, colour="water"),
    head("xnet", "XNet", 2.4, 4.4, colour="brass"),
    head("laserio", "LaserIO", 2.4, 8.2, colour="fire"),
    head("compact", "Compact Machines", 2.4, 12.4, colour="magic"),
    head("mining", "Mining Gadgets", 2.4, 16.2, colour="stone"),
]

chapter(C, "Logistik", "xnet:controller", "tech", quests, shape="square", order=18, stage=3,
        subtitle=["Stufe 3: Integrated Dynamics, XNet, LaserIO, Compact Machines und Mining Gadgets."], images=images)
