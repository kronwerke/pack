"""Applied Energistics 2 in stage 3, one step per quest: meteorites and presses, charged certus
(imbuement or energizing orb), fluix and certus growth, the inscriber and each processor, the
drive, the first network, cells 1k to 16k, the controller and channels, buses and cards,
wireless, autocrafting step by step, every P2P tunnel type, checklists of every device and
every cell size, plus Extended AE and Applied Flux as far as stage 3 allows. Recipes follow
kubejs/server_scripts/kronwerke/ae2.js; facts come from the AE2 19.2 guide in the jar.
64k and up, quantum, spatial, MEGA and Advanced AE are stage 4 (ae2_advanced.py).
Refined Storage has its own chapter; list_transport.py only points here."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner)

C = "ae2"


def head(name, text, left, y, height=0.9, kind="section", colour="water"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def p2p(name, x, y, item, title, line, attune):
    """One line of the P2P checklist."""
    return quest(name, x, y, title, subtitle=line,
                 description=[f"Rechtsklick mit {attune} auf einen platzierten &6ME P2P-Tunnel&r, und er wird zu diesem Typ. Abbauen gibt dir den Tunnel als eigenen Gegenstand."],
                 tasks=[task_item(item, 1)], rewards=[reward_xp(3)], deps=["p2p"], icon=item)


quests = [
    # ---- Meteoriten und Certus ---------------------------------------------
    quest("welcome", 0, 1, "&b&lBau einen Meteoritenkompass",
          subtitle="Er zeigt zum nächsten Meteoriten.",
          description=[
              "Bau ein &6Ladegerät&r (Eisen rundum, ein &6Kupferbarren&r oben in der Mitte, rechts offen) und leg einen normalen &6Kompass&r hinein. Strom kommt über ein Kabel oder eine &6Holzkurbel&r obendrauf (drei Stöcke, ein Kupferbarren), die du von Hand drehst.",
              "",
              "&bApplied Energistics 2&r speichert Gegenstände als Daten auf &6Speicherzellen&r. Ein Kabelnetz verbindet Zellen, Konsolen und Maschinen, und später baut das Netz Dinge selbst.",
              "",
              "&eIn Stufe 3 offen:&r Zellen bis &616k&r, Controller, Busse, P2P, Drahtlos, Autocrafting, dazu &6Extended AE&r, &6Applied Flux&r und &6Applied Mekanistics&r. &cStufe 4:&r 64k und größer, Quantenbrücke, Raumspeicher, MEGA und Advanced AE, siehe Kapitel &bAE2: Fortgeschritten&r.",
              "",
              "Lieber ohne Kanäle und Typen? Das Kapitel &3Refined Storage&r ist die einfachere Alternative.",
          ],
          tasks=[task_item("ae2:meteorite_compass", 1)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 8), reward_table("s3_common")],
          icon="ae2:controller", size=2.0, shape="hexagon"),

    quest("meteorite", 2.5, 0, "&7Finde einen Meteoriten",
          subtitle="Ein Krater aus Himmelsstein mit Certus drin.",
          description=[
              "Folg dem Kompass und grab dich in den Krater. Nimm &616 Certusquarzkristalle&r und &616 Himmelsstein&r mit. Im Ofen wird Himmelsstein zum &6Himmelssteinblock&r für den Controller.",
              "",
              "&cAchtung:&r Einen &6Makellosen Certusquarzknospenblock&r nie abbauen. Selbst mit Behutsamkeit wird er unrein, und makellos bekommst du ihn nicht zurück. Lass ihn stehen und ernte die Cluster daran.",
          ],
          tasks=[task_item("ae2:certus_quartz_crystal", 16), task_item("ae2:sky_stone_block", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["welcome"], icon="ae2:sky_stone_block"),

    quest("presses", 5, 0, "&7Hol die vier Pressen",
          subtitle="Einmal finden, für immer kopieren.",
          description=[
              "Ganz in der Mitte des Meteoriten steht der &6Mysteriöse Würfel&r. Bau ihn ab, dann hast du alle vier Pressen: &6Silizium&r, &6Logik&r, &6Kalkulation&r und &6Konstruktion&r.",
              "",
              "Mehr Meteoriten brauchst du nie: Die Gravurmaschine kopiert eine Presse, wenn du sie oben einlegst und einen &6Eisenblock&r in die Mitte. So bekommt auch dein Mitspieler einen Satz.",
          ],
          tasks=[task_item("ae2:silicon_press", 1), task_item("ae2:logic_processor_press", 1),
                 task_item("ae2:calculation_processor_press", 1), task_item("ae2:engineering_processor_press", 1)],
          rewards=[reward_item("minecraft:iron_block", 2), reward_xp(8)],
          deps=["meteorite"], icon="ae2:mysterious_cube"),

    quest("charged", 2.5, 2, "&e&lLade Certusquarz auf",
          subtitle="Erst ein Magier, später ein Kraftwerk.",
          description=[
              "&eRezept auf Kronwerke, Weg 1:&r &6Imbuement-Kammer&r von Ars Nouveau, ein &6Certusquarzkristall&r hinein, zwei Sockel daneben mit &6Redstone-Staub&r und &6Glowstone-Staub&r. &d2 000 Quelle&r pro Kristall.",
              "&eRezept auf Kronwerke, Weg 2:&r &6Energizing Orb&r von Powah, ein Kristall und ein Redstone ergeben für &d20 000 FE&r gleich &ezwei&r geladene Kristalle.",
              "",
              "Das Ladegerät lädt auf Kronwerke keinen Certus, und auch die Abkürzungen anderer Mods sind weg. Der Orb braucht hier einen Manadiamanten von Botania, siehe Kapitel &cPowah&r.",
              "",
              "Das Starterpaket von Stufe 3 enthält acht geladene Kristalle. Spar sie für Fluix.",
          ],
          tasks=[task_item("ae2:charged_certus_quartz_crystal", 8)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["welcome"], icon="ae2:charged_certus_quartz_crystal", size=1.5, shape="hexagon"),

    quest("fluix", 5, 2, "&5Mach Fluix im Wasser",
          subtitle="Drei Zutaten rein, zwei Kristalle raus.",
          description=[
              "Wirf einen &6Geladenen Certusquarzkristall&r, ein &6Redstone&r und einen &6Netherquarz&r zusammen in Wasser. Nach ein paar Sekunden liegen dort &ezwei Fluixkristalle&r.",
              "",
              "Derselbe Trick vermehrt Certus: ein geladener Kristall und ein &6Certusquarzstaub&r im Wasser ergeben zwei normale Kristalle.",
              "",
              "Fluix steckt in Kabeln, Kernen, Controller und Wachstumsbeschleuniger. Netherquarz brauchst du in Mengen, nimm Glück auf die Spitzhacke.",
          ],
          tasks=[task_item("ae2:fluix_crystal", 16)],
          rewards=[reward_item("minecraft:quartz", 32), reward_xp(5)],
          deps=["charged"], icon="ae2:fluix_crystal"),

    quest("growth", 7.5, 2, "&aZüchte Certus",
          subtitle="Wie Amethyst, nur mit Strom schneller.",
          description=[
              "Wirf einen &6Certusquarzblock&r mit einem geladenen Kristall ins Wasser, das gibt einen beschädigten &6Knospenblock&r. Stell zwei &6Wachstumsbeschleuniger&r daneben (Eisen, Glaskabel, Quarzglas, Fluixblock in der Mitte).",
              "",
              "Jeder weitere geladene Kristall im Wasser hebt den Knospenblock eine Stufe, bis unrein. Jede gewachsene Knospe kann ihn eine Stufe zurückwerfen. Ein fertiger Cluster gibt vier Kristalle, Glück hilft.",
              "",
              "Der Beschleuniger nimmt FE oder AE oben und unten, zur Not reicht eine Holzkurbel.",
          ],
          tasks=[task_item("ae2:growth_accelerator", 2)],
          rewards=[reward_item("ae2:charged_certus_quartz_crystal", 4), reward_xp(8)],
          deps=["fluix"], icon="ae2:flawed_budding_quartz"),

    # ---- Prozessoren -----------------------------------------------------------
    quest("inscriber", 0, 5.5, "&7Bau eine Gravurmaschine",
          subtitle="Sie presst, druckt und mahlt.",
          description=[
              "&6Eisen&r rundherum, je eine &6Mechanische Presse&r aus Create oben und unten in der Mitte, ein &6Kupferbarren&r links in der Mitte, rechts bleibt frei.",
              "",
              "&eSo liest du das Fenster:&r oben und unten die Pressen, in die Mitte das Material. Ohne Presse mahlt sie: Certus zu Certusquarzstaub, Enderperlen zu Enderstaub, Himmelsstein zu Himmelssteinstaub.",
              "",
              "Strom (FE oder AE) kommt per Kabel. Mit &6Beschleunigungskarten&r arbeitet sie schneller.",
          ],
          tasks=[task_item("ae2:inscriber", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["presses"], icon="ae2:inscriber"),

    quest("silicon", 2.5, 5.5, "&8Druck Silizium",
          subtitle="Das Bauteil, auf das Mekanism wartet.",
          description=[
              "Certusquarz in der Gravurmaschine zu &6Certusquarzstaub&r mahlen, im Ofen zu &6Silizium&r schmelzen, unter dem &6Siliziumdruck&r zu &6Gedrucktem Silizium&r pressen.",
              "",
              "&eRezept auf Kronwerke:&r Der &6Fortgeschrittene Steuerschaltkreis&r von Mekanism ist ein Einfacher Steuerschaltkreis, zwei Infundierte Legierungen und ein &6Gedrucktes Silizium&r an der Werkbank. Einen anderen Weg gibt es nicht.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 3, &e\"Der Ofen schläft nie\"&r, will &e250 Fortgeschrittene Steuerschaltkreise&r.",
          ],
          tasks=[task_item("ae2:printed_silicon", 16)],
          rewards=[reward_item("mekanism:alloy_infused", 8), reward_xp(5)],
          deps=["inscriber"], icon="ae2:printed_silicon"),

    quest("logic_proc", 5, 4.5, "&eBau einen Logikprozessor",
          subtitle="Gold, dann Redstone und Silizium.",
          description=[
              "&6Goldbarren&r unter dem Logikdruck gibt einen gedruckten Logikschaltkreis. Den legst du oben ein, &6Redstone&r in die Mitte, &6Gedrucktes Silizium&r unten: fertig ist der &6Logikprozessor&r.",
              "",
              "Logikprozessoren stecken in Zellen, Konsolen und den Formations- und Annihilationskernen.",
          ],
          tasks=[task_item("ae2:logic_processor", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["silicon"], icon="ae2:logic_processor"),

    quest("calc_proc", 5, 6.5, "&bBau einen Kalkulationsprozessor",
          subtitle="Certus unter der Kalkulationspresse.",
          description=[
              "&6Certusquarzkristall&r unter dem Kalkulationsdruck, dann wie beim Logikprozessor mit &6Redstone&r und &6Gedrucktem Silizium&r fertig pressen.",
              "",
              "Kalkulationsprozessoren brauchst du für 4k- und 16k-Zellen, Karten, Fertigungseinheiten und den Zugangspunkt.",
          ],
          tasks=[task_item("ae2:calculation_processor", 8)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 16), reward_xp(6)],
          deps=["silicon"], icon="ae2:calculation_processor"),

    quest("processors", 7.5, 5.5, "&b&lBau Konstruktionsprozessoren",
          subtitle="Der teuerste der drei, und der wichtigste.",
          description=[
              "&6Diamant&r unter dem Konstruktionsdruck, dann mit &6Redstone&r und &6Gedrucktem Silizium&r fertig pressen.",
              "",
              "Konstruktionsprozessoren stecken im ME-Laufwerk, im Controller, in P2P-Tunneln und in der Schablonenkonsole.",
              "",
              "&eKronwerke:&r Der Meilenstein &6Stahlkern&r für Stufe 3 braucht zwei Konstruktionsprozessoren pro Stück, acht Stahlkerne will der Obelisk sehen.",
          ],
          tasks=[task_item("ae2:engineering_processor", 8)],
          rewards=[reward_item("minecraft:diamond", 4), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["logic_proc", "calc_proc"], icon="ae2:engineering_processor", size=1.75, shape="gear"),

    # ---- Das ME-Netz -----------------------------------------------------------
    quest("drive", 0, 10, "&3Bau ein ME-Laufwerk",
          subtitle="Zehn Plätze für Speicherzellen.",
          description=[
              "&eRezept auf Kronwerke:&r Eisen in die Ecken, &6Konstruktionsprozessoren&r oben und unten, zwei &6Fortgeschrittene Steuerschaltkreise&r von Mekanism links und rechts, die Mitte bleibt frei.",
              "",
              "Die Schaltkreise ersetzen die Fluix-Glaskabel des Originals: Lagernetze brauchen Mekanism. Das Laufwerk hält bis zu &e10 Zellen&r und braucht einen Kanal.",
          ],
          tasks=[task_item("ae2:drive", 1)],
          rewards=[reward_item("mekanism:advanced_control_circuit", 2), reward_xp(8)],
          deps=["processors"], icon="ae2:drive"),

    quest("network", 2.5, 10, "&b&lSchließ dein erstes Netz an",
          subtitle="Laufwerk, Strom, Konsole, Kabel.",
          description=[
              "Bau einen &6Energieakzeptor&r (Eisen in die Ecken, Quarzglas an die Seiten, Kupfer in die Mitte) und eine &6ME-Konsole&r (formlos: Formationskern, Annihilationskern, Leuchtfeld, Logikprozessor). Verbinde alles mit &6Fluix-Glaskabeln&r (Quarzfaser und zwei Fluix gibt vier).",
              "",
              "Der Akzeptor wandelt &d2 FE in 1 AE&r. Eine &6Energiezelle&r (200 000 AE) daneben fängt Stromspitzen beim Einlagern ab, sonst startet das Netz kurz neu.",
              "",
              "Ohne Controller ist das Netz &ead hoc&r und trägt höchstens &e8 Geräte&r mit Kanal. Beim neunten geht alles aus.",
          ],
          tasks=[task_item("ae2:energy_acceptor", 1), task_item("ae2:terminal", 1), task_item("ae2:fluix_glass_cable", 16)],
          rewards=[reward_item("ae2:fluix_covered_cable", 16), reward_table("s3_common"), reward_xp(10)],
          deps=["drive"], icon="ae2:terminal", size=1.75, shape="hexagon"),

    quest("cell_1k", 5, 9, "&7Bau eine 1k-Zelle",
          subtitle="1 024 Bytes, 63 Typen.",
          description=[
              "&6Komponente:&r Logikprozessor in die Mitte, Certus an die Seiten, Redstone in die Ecken. &6Gehäuse:&r Quarzglas, Redstone, Eisen und Kupfer. Beides zusammen an der Werkbank gibt die Zelle.",
              "",
              "&eSo rechnet eine Zelle:&r Jeder Typ kostet vorab Bytes, danach brauchen acht Gegenstände ein Byte. Eine 1k-Zelle fasst &e8 128&r Stück einer Sorte oder &e4 160&r, wenn alle 63 Typen belegt sind.",
              "",
              "Kaputte Werkzeuge aus der Mobfarm gehören nicht hinein: jede Haltbarkeit ist ein eigener Typ. Leere Zellen zerlegst du mit Schleichen und Rechtsklick.",
          ],
          tasks=[task_item("ae2:item_storage_cell_1k", 2)],
          rewards=[reward_item("ae2:item_cell_housing", 2), reward_xp(5)],
          deps=["network"], icon="ae2:item_storage_cell_1k"),

    quest("cell_4k", 7.5, 9, "&9Rüste auf 4k auf",
          subtitle="Viermal so viel Platz, gleiche Typen.",
          description=[
              "&64k-Komponente:&r Redstone in die Ecken, ein Kalkulationsprozessor oben, drei 1k-Komponenten links, rechts und unten, Quarzglas in die Mitte.",
              "",
              "Eine 4k-Zelle fasst &e32 512&r Stück einer Sorte, &e16 640&r bei 63 Typen. Volle Zelle und größere Komponente an der Werkbank tauschen die Komponente, der Inhalt bleibt.",
          ],
          tasks=[task_item("ae2:item_storage_cell_4k", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(6)],
          deps=["cell_1k"], icon="ae2:item_storage_cell_4k"),

    quest("cell_16k", 10, 9, "&b&lBau eine 16k-Zelle",
          subtitle="Das Größte, was Stufe 3 hergibt.",
          description=[
              "&616k-Komponente:&r wie die 4k-Komponente, nur mit &6Glowstone-Staub&r in den Ecken und drei 4k-Komponenten.",
              "",
              "Eine 16k-Zelle fasst &e130 048&r Stück einer Sorte, &e66 560&r bei 63 Typen. Für viele Sorten in kleinen Mengen sind mehrere kleine Zellen besser, die Typen pro Zelle bleiben immer 63.",
              "",
              "&cAusblick:&r 64k braucht auf Kronwerke einen &6Himmelsbarren&r von Nature's Aura, 256k einen Draconiumbarren. Beides kommt in Stufe 4.",
          ],
          tasks=[task_item("ae2:item_storage_cell_16k", 1)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_table("s3_uncommon"), reward_xp(8)],
          deps=["cell_4k"], icon="ae2:item_storage_cell_16k"),

    quest("controller", 5, 11, "&5&lBau einen ME-Controller",
          subtitle="Netze brauchen ein Ritual.",
          description=[
              "&eRezept auf Kronwerke:&r &6Himmelssteinblöcke&r in die vier Ecken, ein &6Spirit Attuned Gem&r von Occultism oben in die Mitte, &6Fluixkristalle&r links, rechts und unten in der Mitte, ein &6Konstruktionsprozessor&r ins Zentrum.",
              "",
              "Das Juwel machst du aus Lapis im Geisterfeuer, siehe Kapitel &5Occultism&r. Jede Seite des Controllers gibt &e32 Kanäle&r aus.",
              "",
              "&eRegeln:&r ein Controller pro Netz, er darf aus mehreren Blöcken bestehen, alles in 7 x 7 x 7. Er braucht &d6 AE/t&r pro Block. Wird ein Block rot, stimmt die Form nicht.",
          ],
          tasks=[task_item("ae2:controller", 1)],
          rewards=[reward_item("ae2:fluix_crystal", 16), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["network"], icon="ae2:controller", size=1.75, shape="gear"),

    quest("channels", 7.5, 11, "&e&lVerstehe Kanäle",
          subtitle="8 pro Kabel, 32 pro dichtem Kabel.",
          description=[
              "Fast jedes Gerät braucht einen &eKanal&r. Ein normales Kabel trägt &e8&r, ein &6dichtes Kabel&r (vier verdeckte Kabel) trägt &e32&r. Bau wie einen Baum: dichte Kabel als Äste vom Controller, normale Kabel als Zweige, höchstens acht Geräte pro Zweig.",
              "",
              "Kanäle laufen vom Controller den kürzesten Weg, erst durch dichte, dann durch normale Kabel. Ist dieser Weg voll, bleiben Geräte dunkel, auch wenn daneben ein leeres Kabel liegt.",
              "",
              "&6Schlaue Kabel&r zeigen mit Streifen, wie viele Kanäle durch sie laufen. &eRezept auf Kronwerke:&r vier verdeckte Kabel in die Ecken, Redstone oben und unten, Glowstone links und rechts, eine &6Elektronenröhre&r von Create in die Mitte, gibt vier.",
              "",
              "&cAchtung:&r Kabelfarben haben nichts mit Kanälen zu tun. Zwei Kabel verschiedener Farbe verbinden sich nur nicht.",
          ],
          tasks=[task_item("ae2:fluix_smart_cable", 16), task_item("ae2:fluix_covered_dense_cable", 4)],
          rewards=[reward_item("create:electron_tube", 8), reward_xp(8)],
          deps=["controller"], icon="ae2:fluix_smart_cable", size=1.5, shape="hexagon"),

    quest("buses", 10, 11, "&6Setz Import- und Exportbus",
          subtitle="Rein ins Netz, raus aus dem Netz.",
          description=[
              "&6Importbus:&r Annihilationskern oben, darunter Eisen, Kolben, Eisen. &6Exportbus:&r Eisen, Formationskern, Eisen, darunter ein Kolben. Beide sitzen auf einem Kabel und schauen auf einen Block.",
              "",
              "Der Importbus zieht alles aus dem Inventar vor sich ins Netz, der Exportbus schiebt eingestellte Gegenstände hinaus. Zusammen automatisieren sie einen Ofen: Export oben hinein, Import unten heraus.",
              "",
              "Ohne Karten bewegen sie wenig, siehe nächste Quest.",
          ],
          tasks=[task_item("ae2:import_bus", 1), task_item("ae2:export_bus", 1)],
          rewards=[reward_item("minecraft:piston", 8), reward_xp(6)],
          deps=["channels"], icon="ae2:import_bus"),

    quest("cards", 12.5, 10, "&dSteck Karten in die Busse",
          subtitle="Schneller, mehr Filter, mehr Logik.",
          description=[
              "&6Basiskarte:&r Gold, Eisen, Redstone und ein Kalkulationsprozessor, gibt zwei. Mit Diamant statt Gold wird es die &6Fortgeschrittene Karte&r. Daraus formlos: &6Beschleunigungskarte&r (Fortgeschrittene Karte und Fluix), &6Kapazitätskarte&r (Basiskarte und Certus).",
              "",
              "Beschleunigung macht Busse, Gravurmaschine und Assembler schneller. Kapazität gibt Bussen mehr Filterplätze. &6Redstone-&r, &6Ungenauigkeits-&r und &6Umkehrungskarte&r regeln den Rest.",
          ],
          tasks=[task_item("ae2:speed_card", 2), task_item("ae2:capacity_card", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(6)],
          deps=["buses"], icon="ae2:speed_card"),

    quest("storage_bus", 12.5, 12, "&6Häng eine Schubladenwand ans Netz",
          subtitle="Der Speicherbus macht Kisten zu Zellen.",
          description=[
              "&6ME-Speicherbus:&r formlos aus einer &6ME-Schnittstelle&r und zwei &6Kolben&r. Setz ihn auf ein Kabel vor eine Truhe, ein Fass oder eine Schublade.",
              "",
              "Was in dem Block liegt, siehst du in der Konsole, und das Netz legt dort hinein. Schubladen zählen keine Typen, eine Schubladenwand mit Speicherbus ist oft besser als eine Zelle. Wie du die Wand baust, steht im Kapitel &6Lager&r.",
          ],
          tasks=[task_item("ae2:storage_bus", 1)],
          rewards=[reward_item("functionalstorage:oak_4", 4), reward_xp(6)],
          deps=["buses"], icon="ae2:storage_bus"),

    quest("wireless", 7.5, 13, "&bGeh drahtlos",
          subtitle="Das Lager in der Tasche.",
          description=[
              "&6Drahtloser Zugangspunkt:&r Drahtlosempfänger, Kalkulationsprozessor, Glaskabel übereinander. &6Drahtlose Fertigungskonsole:&r Empfänger, Fertigungskonsole, Dichte Energiezelle übereinander. Leg die Konsole in den Platz oben rechts im Zugangspunkt, dann ist sie verbunden.",
              "",
              "&6Drahtlosverstärker&r im Zugangspunkt erhöhen Reichweite und Stromverbrauch. Aufladen geht im Ladegerät.",
              "",
              "&6AE2 Wireless Terminals&r legt mehrere drahtlose Konsolen zur &6Universalkonsole&r zusammen, die &6Magnetkarte&r darin zieht Gegenstände in der Nähe ins Netz.",
          ],
          tasks=[task_item("ae2:wireless_access_point", 1), task_item("ae2:wireless_crafting_terminal", 1)],
          rewards=[reward_item("ae2:dense_energy_cell", 1), reward_xp(10)],
          deps=["channels"], icon="ae2:wireless_crafting_terminal"),

    # ---- Autocrafting ----------------------------------------------------------
    quest("pattern_terminal", 0, 17, "&aBau eine Schablonenkonsole",
          subtitle="Hier schreibst du Rezepte auf.",
          description=[
              "Erst die &6ME-Fertigungskonsole&r (formlos: ME-Konsole, Werkbank, Kalkulationsprozessor), daraus mit einem &6Konstruktionsprozessor&r die &6ME-Schablonenkonsole&r. &6Leere Schablonen&r: Quarzglas, Glowstone, Certus, Eisen und Kupfer, gibt zwei.",
              "",
              "Autocrafting braucht drei Dinge: einen Auftrag, eine &6Fertigungs-CPU&r und einen &6Schablonen-Provider&r mit Schablone. Die nächsten Quests bauen sie Schritt für Schritt.",
          ],
          tasks=[task_item("ae2:pattern_encoding_terminal", 1), task_item("ae2:blank_pattern", 8)],
          rewards=[reward_item("ae2:blank_pattern", 8), reward_xp(5)],
          deps=["network"], icon="ae2:pattern_encoding_terminal"),

    quest("first_pattern", 2.5, 17, "&aSchreib eine Fertigungsschablone",
          subtitle="Ein Werkbankrezept auf Papier.",
          description=[
              "In der Schablonenkonsole Modus &eFertigung&r wählen, das Rezept ins Raster legen (aus JEI mit dem Plus), leere Schablone einlegen, Pfeil drücken. Heraus kommt eine &6Fertigungsschablone&r.",
              "",
              "Fang mit etwas Einfachem an, zum Beispiel Holz zu Brettern. Eine Schablone darf auch 8 Bruchstein zu 8 Stein sagen, dann arbeitet die Maschine in größeren Schritten.",
          ],
          tasks=[task_item("ae2:crafting_pattern", 1)],
          rewards=[reward_xp(5)],
          deps=["pattern_terminal"], icon="ae2:crafting_pattern"),

    quest("provider", 5, 17, "&aBau einen Schablonen-Provider",
          subtitle="Er schickt die Zutaten los.",
          description=[
              "&eRezept auf Kronwerke:&r Eisen in die Ecken, Werkbänke oben und unten, Annihilationskern links, ein &6Präzisionsgetriebe&r von Create in die Mitte, Formationskern rechts.",
              "",
              "Der Provider schiebt die Zutaten einer Schablone in den Block daneben und nimmt das Ergebnis wieder an. Er braucht einen Kanal. Leg deine Fertigungsschablone hinein.",
          ],
          tasks=[task_item("ae2:pattern_provider", 1)],
          rewards=[reward_item("create:precision_mechanism", 1), reward_xp(6)],
          deps=["first_pattern"], icon="ae2:pattern_provider"),

    quest("autocraft", 7.5, 17, "&a&lStell einen Molekularassembler daneben",
          subtitle="Werkbankrezepte ganz ohne Hände.",
          description=[
              "&eRezept auf Kronwerke:&r Eisen in die Ecken, Quarzglas oben und unten, zwei &6Präzisionsgetriebe&r links und rechts, eine &6Werkbank&r in die Mitte. Setz ihn direkt an den Provider.",
              "",
              "Der Provider schickt Zutaten und Rezept hinüber, der Assembler craftet und gibt das Ergebnis zurück. Ein Provider kann mehrere Assembler ringsum bedienen. &6Beschleunigungskarten&r machen ihn schneller.",
              "",
              "Autocrafting gibt es auf Kronwerke nur mit Create.",
          ],
          tasks=[task_item("ae2:molecular_assembler", 1)],
          rewards=[reward_item("create:precision_mechanism", 2), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["provider"], icon="ae2:molecular_assembler", size=1.75, shape="gear"),

    quest("cpu", 10, 16, "&7Bau eine Fertigungs-CPU",
          subtitle="Sie plant den Auftrag.",
          description=[
              "&6Fertigungseinheit:&r Eisen in die Ecken, Kalkulationsprozessoren oben und unten, Glaskabel an den Seiten, Logikprozessor in die Mitte. Einheit plus 1k-Komponente gibt einen &61k-Fertigungsspeicher&r, Einheit plus Konstruktionsprozessor eine &6Prozessoreinheit&r.",
              "",
              "Die CPU ist ein volles Rechteck ohne Lücken, mit mindestens einem Speicher. Prozessoreinheiten machen sie schneller. Eine CPU, ein Auftrag zur Zeit.",
              "",
              "&eBestellen:&r In der Konsole auf etwas klicken, das eine Schablone hat. Liegt es schon auf Lager, nimm die Mausrad-Taste.",
          ],
          tasks=[task_item("ae2:1k_crafting_storage", 1), task_item("ae2:crafting_accelerator", 1)],
          rewards=[reward_item("ae2:crafting_unit", 2), reward_xp(8)],
          deps=["autocraft"], icon="ae2:1k_crafting_storage"),

    quest("processing_pattern", 10, 18, "&aLass eine Maschine für dich arbeiten",
          subtitle="Verarbeitungsschablone an der Gravurmaschine.",
          description=[
              "In der Schablonenkonsole Modus &eVerarbeitung&r: oben &6Silizium&r, unten &6Gedrucktes Silizium&r als Ergebnis. Schablone in einen Provider, der direkt an einer Gravurmaschine mit Siliziumdruck sitzt.",
              "",
              "Das Ergebnis muss zurück ins Netz. Am einfachsten schiebt die Maschine es zurück in den Provider (Auto-Ausgabe oder ein Rohr), sonst nimm einen Importbus.",
              "",
              "So geht es mit jedem Ofen, jeder Mekanism-Maschine und jedem Mixer.",
          ],
          tasks=[task_item("ae2:processing_pattern", 1)],
          rewards=[reward_item("ae2:printed_silicon", 8), reward_xp(8)],
          deps=["autocraft"], icon="ae2:processing_pattern"),

    quest("crafting_card", 12.5, 17, "&aHalt einen Vorrat",
          subtitle="Die Fertigungskarte bestellt nach.",
          description=[
              "&6Fertigungskarte:&r formlos aus Basiskarte und Werkbank. Steck sie in einen Exportbus, stell den Gegenstand ein, und fehlt er im Netz, bestellt der Bus ihn selbst.",
              "",
              "Der &6ME-Füllstandsemitter&r (formlos: Redstonefackel und Kalkulationsprozessor) gibt Redstone, sobald ein Bestand unter eine Zahl fällt. Mit Fertigungskarte kann er sogar eine Farm einschalten, die ohne Zutaten arbeitet.",
          ],
          tasks=[task_item("ae2:crafting_card", 1), task_item("ae2:level_emitter", 1)],
          rewards=[reward_item("ae2:crafting_accelerator", 1), reward_xp(8)],
          deps=["cpu", "processing_pattern", "cards"], icon="ae2:crafting_card"),

    quest("factory", 15, 17, "&6&lBau die Schaltkreisfabrik",
          subtitle="Der Ofen schläft nie, die Gravurmaschine auch nicht.",
          description=[
              "Verarbeitungsschablonen für Gedrucktes Silizium (Gravurmaschine), Infundierte Legierung und Einfache Steuerschaltkreise (zwei Infusionsanlagen), eine Fertigungsschablone im Assembler für den &6Fortgeschrittenen Steuerschaltkreis&r. Bestell 64 Stück.",
              "",
              "Ein Exportbus mit Fertigungskarte an einer Kiste neben dem Obelisken hält den Vorrat. Wer viel Silizium braucht, baut den &6Circuit Slicer&r von Extended AE weiter unten.",
              "",
              "&eKronwerke:&r &e\"Der Ofen schläft nie\"&r will &e250 Fortgeschrittene Steuerschaltkreise&r, &e4 000 Stahlbarren&r und &e8 Stahlkerne&r. Was in die Kiste am Obelisken fällt, zählt für den, der sie hingestellt hat.",
          ],
          tasks=[task_item("mekanism:advanced_control_circuit", 64), task_item("ae2:engineering_processor", 16)],
          rewards=[reward_table("s3_rare"), reward_item("ae2:cell_component_16k", 1), reward_xp(25)],
          deps=["crafting_card"], icon="mekanism:advanced_control_circuit", size=2.5, shape="gear"),

    # ---- P2P-Tunnel --------------------------------------------------------------
    quest("p2p", 0, 22, "&d&lBau einen ME P2P-Tunnel",
          subtitle="Ein Portal zwischen zwei Blockseiten.",
          description=[
              "Eisen oben und an den Seiten, ein &6Konstruktionsprozessor&r in der Mitte, drei Fluix unten. Verbinden mit der &6Speicherkarte&r: Schleich-Rechtsklick auf den Eingang, Rechtsklick auf jeden Ausgang.",
              "",
              "Der Klassiker: Ein ME-Tunnel braucht selbst einen Kanal, trägt aber alle 32 Kanäle des dichten Kabels an seinem Eingang. So bringst du viele Kanäle durch ein dünnes Kabel. ME-Tunnel lassen sich nicht ineinander schachteln.",
              "",
              "Andere Typen machst du per Rechtsklick auf einen platzierten Tunnel, siehe die Liste daneben.",
          ],
          tasks=[task_item("ae2:me_p2p_tunnel", 2), task_item("ae2:memory_card", 1)],
          rewards=[reward_item("ae2:engineering_processor", 2), reward_xp(8)],
          deps=["channels"], icon="ae2:me_p2p_tunnel", size=1.5, shape="hexagon"),

    p2p("p2p_item", 2.5, 21, "ae2:item_p2p_tunnel", "Bau einen Item-Tunnel",
        "Gegenstände von einer Blockseite zur anderen.", "einer &6Truhe&r, einem &6Trichter&r oder einem Bus"),
    p2p("p2p_fluid", 4.5, 21, "ae2:fluid_p2p_tunnel", "Bau einen Flüssigkeits-Tunnel",
        "Flüssigkeiten ohne Rohr.", "einem &6Eimer&r"),
    p2p("p2p_fe", 6.5, 21, "ae2:fe_p2p_tunnel", "Bau einen FE-Tunnel",
        "Strom ohne Kabel, kostet 2,5 Prozent.", "einer &6Energiezelle&r oder einem &6Energieakzeptor&r"),
    p2p("p2p_redstone", 2.5, 23, "ae2:redstone_p2p_tunnel", "Bau einen Redstone-Tunnel",
        "Ein Signal quer durch die Basis.", "&6Redstone&r, einem &6Hebel&r oder einer &6Redstonefackel&r"),
    p2p("p2p_light", 4.5, 23, "ae2:light_p2p_tunnel", "Bau einen Licht-Tunnel",
        "Licht von hier nach dort.", "einer &6Fackel&r oder &6Glowstone&r"),
    p2p("p2p_chemical", 6.5, 23, "appmek:chemical_p2p_tunnel", "Bau einen Chemie-Tunnel",
        "Mekanism-Gase ohne Druckrohr (Applied Mekanistics).", "einem &6Chemikalientank&r von Mekanism"),

    # ---- Geräte und Zellen -------------------------------------------------------
    quest("interface", 10, 22, "&6Bau eine ME-Schnittstelle",
          subtitle="Eine Kiste, die sich selbst füllt.",
          description=[
              "Eisen in die Ecken, Glas oben und unten, Annihilationskern links, Formationskern rechts.",
              "",
              "Stell in den oberen Plätzen ein, was sie vorrätig halten soll, dann füllt sie sich aus dem Netz. Was du hineinschiebst und nicht eingestellt ist, wandert ins Netz. Sie braucht einen Kanal und ist die Zutat für den Speicherbus.",
          ],
          tasks=[task_item("ae2:interface", 1)],
          rewards=[reward_item("ae2:formation_core", 2), reward_xp(5)],
          deps=["buses"], icon="ae2:interface"),

    quest("list_devices", 12.5, 21, "&7Kenne jedes AE2-Gerät",
          subtitle="Eine Zeile pro Gerät.",
          description=[
              "&6Controller&r: Herz des Netzes, 32 Kanäle pro Seite. &6Energieakzeptor&r: 2 FE zu 1 AE. &6Energiezelle&r und &6Dichte Energiezelle&r: 200 000 und 1,6 Mio. AE Puffer. &6Vibrationskammer&r: Brennstoff zu 40 AE/t.",
              "&6ME-Laufwerk&r: 10 Zellen. &6ME-Truhe&r: eine Zelle mit eigener Konsole. &6ME-IO-Port&r: füllt oder leert Zellen. &6Speicherzellenwerkbank&r: Zellen filtern und mit Karten bestücken.",
              "&6Konsole&r, &6Fertigungskonsole&r, &6Schablonenkonsole&r, &6Schablonen-Zugriffskonsole&r: schauen, craften, Rezepte schreiben, Provider verwalten. &6Speichermonitor&r und &6Konversionsmonitor&r: zeigen eine Menge, der zweite tauscht auch.",
              "&6Import-&r, &6Export-&r und &6Speicherbus&r: rein, raus, fremde Kisten. &6Formations-&r und &6Annihilationsfeld&r: Blöcke setzen und abbauen. &6Füllstandsemitter&r: Redstone nach Bestand, ohne Kanal. &6Schaltbarer Bus&r: Kabel per Redstone trennen.",
              "&6Schnittstelle&r: Kiste mit Vorrat. &6Schablonen-Provider&r und &6Molekularassembler&r: Autocrafting. &6Gravurmaschine&r, &6Ladegerät&r, &6Wachstumsbeschleuniger&r, &6Materiekondensator&r: Maschinen. &6P2P-Tunnel&r und &6Zugangspunkt&r: Verbindungen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["network"], icon="ae2:network_tool", section="devices"),

    quest("list_cells", 12.5, 23, "&7Kenne jede Zellengröße",
          subtitle="Was wann öffnet, und was hineinpasst.",
          description=[
              "&61k&r: 8 128 Stück einer Sorte. &64k&r: 32 512. &616k&r: 130 048. Alle drei in Stufe 3, dazu Flüssigkeitszellen (8 Eimer pro Byte), Chemiezellen von Applied Mekanistics und FE-Zellen von Applied Flux in denselben Größen.",
              "&664k&r: 520 192, Himmelsbarren in der Komponente, Stufe 4. &6256k&r: 2 080 768, Draconium, Stufe 4.",
              "&6MEGA 1M&r und &64M&r: Draconium und Akkumulationsprozessor, Stufe 4. &6MEGA 16M&r bis &6256M&r und die &6Bulk-Zelle&r: Erwachtes Draconium, Stufe 5.",
              "Jede Zelle, egal wie groß, hat &e63 Typen&r. Die großen Zellen stehen im Kapitel &bAE2: Fortgeschritten&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["cell_16k"], icon="ae2:item_cell_housing", section="devices"),

    # ---- Extended AE -------------------------------------------------------------
    quest("entro", 0, 27, "&3Züchte Entro",
          subtitle="Fluix mit Enderstaub.",
          description=[
              "&6Entro Seed&r: Sand, drei Enderstaub, zwei Redstone, zwei Glowstone, ein Himmelssteinstaub. Rechtsklick damit auf einen &6Fluixblock&r macht einen &6Budding Fully Entroized Fluix&r, auf dem Entro-Knospen wachsen.",
              "",
              "Der Block verbraucht sich und wird am Ende zum Certusquarzblock, im Schnitt nach etwa zehn Kristallen. Abgebaut gibt er einen &6Entro Dust&r. Entro Dust und Fluix im Wasser ergeben einen Entro Crystal, Entro Dust mit Gold und Lapis einen &6Entro Infused Ingot&r.",
          ],
          tasks=[task_item("extendedae:entro_crystal", 16)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(5)],
          deps=["fluix"], icon="extendedae:entro_crystal"),

    quest("crystal_assembler", 2.5, 27, "&3Bau einen Crystal Assembler",
          subtitle="Rezepte, die nicht auf die Werkbank passen.",
          description=[
              "&6Extended Machine Frame&r: vier Entro Infused Ingots, Kupfer, Eisen, Quarzglas. Rahmen, Fertigungskonsole, zwei Logikprozessoren, zwei Glaskabel und ein Himmelssteintank ergeben den &6Crystal Assembler&r.",
              "",
              "Er ersetzt das Werfen ins Wasser: aus je vier geladenem Certus, Redstone und Netherquarz mit Wasser macht er acht Fluix. Die Seite mit dem Bildschirm verbindet sich nicht mit dem Netz.",
              "",
              "&eIn Stufe 3 offen:&r &6Crystal Fixer&r (repariert Knospenblöcke), &6Circuit Slicer&r, &6Tag-&r und &6Mod Storage Bus&r, &6Threshold Level Emitter&r, &6Pattern Modifier&r, &6ME Void Cell&r. &cStufe 4:&r die Ex-Maschinen.",
          ],
          tasks=[task_item("extendedae:machine_frame", 1), task_item("extendedae:crystal_assembler", 1)],
          rewards=[reward_item("ae2:fluix_block", 4), reward_table("s3_common"), reward_xp(10)],
          deps=["entro"], icon="extendedae:crystal_assembler"),

    quest("circuit_cutter", 5, 27, "&3Bau einen Circuit Slicer",
          subtitle="Neun Platten aus einem Block.",
          description=[
              "Im Crystal Assembler: Maschinenrahmen, acht Konstruktionsprozessoren, alle vier Pressen, eine &6Inscriber Concurrent Press&r (drei Enderaugen, vier Entro Crystals, Siliziumdruck) und eine Steinsäge.",
              "",
              "Ein &6Siliziumblock&r gibt neun Gedruckte Silizium, ein Goldblock neun Logikschaltkreise, ein Diamantblock neun Konstruktionsschaltkreise, ein Certusquarzblock vier Kalkulationsschaltkreise. Die schnellste Siliziumquelle in Stufe 3.",
          ],
          tasks=[task_item("extendedae:circuit_cutter", 1)],
          rewards=[reward_item("minecraft:gold_block", 2), reward_xp(12)],
          deps=["crystal_assembler"], icon="extendedae:circuit_cutter", optional=True),

    # ---- Applied Flux -------------------------------------------------------------
    quest("flux_crystal", 9, 27, "&cMach Energieprozessoren",
          subtitle="Strom braucht einen eigenen Prozessor.",
          description=[
              "&6Redstone-Block&r, Fluixkristall und Glowstone-Staub ins Wasser gibt zwei &6Redstone-Kristalle&r, im Ladegerät werden sie geladen. Ein Eisenblock im Ladegerät wird zum &6Energiedruck&r.",
              "",
              "Geladenen Redstone-Kristall unter dem Energiedruck, dann wie jeden Prozessor mit Redstone und Gedrucktem Silizium fertig pressen.",
          ],
          tasks=[task_item("appflux:charged_redstone", 8), task_item("appflux:energy_processor", 4)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(6)],
          deps=["processors"], icon="appflux:energy_processor"),

    quest("flux_cell", 11.5, 27, "&c&lSpeicher Strom in Zellen",
          subtitle="Ein Akku, der ins Laufwerk passt.",
          description=[
              "&6FE-Zellengehäuse&r mit &6gehärtetem Isolierharz&r (Wassereimer, zwei Kakteen, Knochenmehl, Silizium, Schleimball, Glowstone, im Ofen gehärtet). Komponente: Logikprozessor mit Redstone-Kristallen und Certusquarzstaub.",
              "",
              "Pro Byte passen &d1 048 576 FE&r hinein, die 1k-Zelle schluckt also rund eine Milliarde FE. Der &6Flux Accessor&r ist die Steckdose: Strom rein über Kabel, Strom raus an Maschinen daneben. Die &6Induktionskarte&r macht dasselbe aus Schnittstelle oder Provider.",
              "",
              "&eKronwerke:&r Der gespeicherte Strom versorgt nicht das ME-Netz selbst, dafür bleibt der Energieakzeptor. Zellen bis 16k in Stufe 3.",
          ],
          tasks=[task_item("appflux:fe_1k_cell", 1), task_item("appflux:flux_accessor", 1)],
          rewards=[reward_item("ae2:energy_cell", 1), reward_table("s3_common"), reward_xp(10)],
          deps=["flux_crystal"], icon="appflux:fe_1k_cell"),

    # ---- Neue Quests -------------------------------------------------------------
    quest("fluix_tools", 7.5, 0, "&5Schmiede eine Fluix-Spitzhacke",
          subtitle="Eisen, nur dreimal so haltbar.",
          description=[
              "&6Fluix-Upgrade:&r formlos aus Papier und einem Fluixkristall. Am Schmiedetisch kommen Vorlage, eine &6Quarzspitzhacke&r (Certus oder Netherquarz) und ein &6Fluixblock&r zusammen.",
              "",
              "Fluix-Werkzeuge sind wie Eisen, halten aber dreimal so lange und schlagen etwas fester zu. Jedes wirkt, als hätte es mindestens &eGlück I&r oder &ePlünderung I&r, ganz ohne Zaubertisch.",
              "",
              "Genau richtig für Netherquarz, den du für Fluix in Mengen brauchst.",
          ],
          tasks=[task_item("ae2:fluix_pickaxe", 1)],
          rewards=[reward_item("ae2:fluix_crystal", 8), reward_xp(5)],
          deps=["fluix"], icon="ae2:fluix_pickaxe", optional=True),

    quest("resonance", 2.5, 12, "&eBau einen Kristallresonanzgenerator",
          subtitle="Strom ohne Brennstoff.",
          description=[
              "Kupfer oben und an den Seiten, ein &6Fluixblock&r oben in der Mitte, ein &6Geladener Certusquarzkristall&r in die Mitte, drei Eisen unten.",
              "",
              "Er gibt dem Netz &d20 AE/t&r, ohne dass du je etwas nachfüllst. Mehr als einer pro Netz geht nicht, die Schwingungen stören sich, sogar durch Quarzfaser hindurch.",
              "",
              "Für ein kleines Netz reicht das im Leerlauf. Wer mehr braucht, bleibt beim Energieakzeptor.",
          ],
          tasks=[task_item("ae2:crystal_resonance_generator", 1)],
          rewards=[reward_item("ae2:charged_certus_quartz_crystal", 2), reward_xp(6)],
          deps=["network"], icon="ae2:crystal_resonance_generator"),

    quest("fluid_cell", 5, 13, "&9Lager Flüssigkeiten ein",
          subtitle="Eimer brauchst du keine mehr.",
          description=[
              "&6Flüssigkeitszellengehäuse&r und eine &61k-Komponente&r an der Werkbank ergeben die &61k-ME-Flüssigkeitsspeicherzelle&r. Sie kommt ins Laufwerk wie jede Zelle.",
              "",
              "Eine Flüssigkeitszelle hält nur &e5 Typen&r, dafür passen &d8 Eimer&r in ein Byte. Lava, Wasser und Öl landen so direkt im Netz, abfüllen geht in der Konsole mit einem Eimer oder Tank.",
              "",
              "&eApplied Mekanistics:&r Mit einem &6Chemiezellengehäuse&r (Quarzglas, Redstone, drei Osmiumbarren unten) und derselben Komponente speicherst du Mekanism-Gase.",
          ],
          tasks=[task_item("ae2:fluid_storage_cell_1k", 1)],
          rewards=[reward_item("ae2:cell_component_1k", 1), reward_xp(5)],
          deps=["cell_1k"], icon="ae2:fluid_storage_cell_1k"),

    quest("cell_workbench", 15, 10, "&dPartitioniere eine Zelle",
          subtitle="Eine Zelle nur für Erze.",
          description=[
              "&6Speicherzellenwerkbank:&r Wolle, Kalkulationsprozessor, Wolle oben, Eisen, Truhe, Eisen in der Mitte, drei Eisen unten.",
              "",
              "Leg eine Zelle hinein und zieh die Gegenstände, die sie nehmen soll, aus JEI in die Filterplätze. Danach landet nur noch das darin. Ein Knopf übernimmt den aktuellen Inhalt als Filter.",
              "",
              "Karten kommen auch hier in die Zelle: die &6Gleichmäßige-Verteilungskarte&r teilt den Platz auf alle Typen auf, die &6Overflow Zerstörungskarte&r löscht, was nicht mehr passt. Die nur mit Filter benutzen.",
          ],
          tasks=[task_item("ae2:cell_workbench", 1)],
          rewards=[reward_item("ae2:basic_card", 2), reward_xp(5)],
          deps=["cards"], icon="ae2:cell_workbench"),

    quest("io_port", 15, 22, "&6Bau einen ME-IO-Port",
          subtitle="Zellen in Sekunden füllen oder leeren.",
          description=[
              "Drei Glas oben, ME-Laufwerk, Glaskabel, ME-Laufwerk in der Mitte, Eisen, Logikprozessor, Eisen unten.",
              "",
              "Der Pfeil in der Mitte stellt die Richtung ein: aus der Zelle ins Netz oder aus dem Netz in die Zelle. Fertige Zellen wandern in die Ausgabeplätze. So ziehst du eine volle 1k-Zelle auf eine 16k-Zelle um.",
              "",
              "&6Beschleunigungskarten&r bewegen mehr pro Schritt, die &6Redstone-Karte&r schaltet ihn per Signal.",
          ],
          tasks=[task_item("ae2:io_port", 1)],
          rewards=[reward_item("ae2:speed_card", 1), reward_xp(6)],
          deps=["cell_4k"], icon="ae2:io_port"),

    quest("planes", 15, 21, "&6Setz Formations- und Annihilationsfeld",
          subtitle="Das Netz baut ab und setzt Blöcke.",
          description=[
              "&6Annihilationsfeld:&r drei Fluix oben, Eisen, Annihilationskern, Eisen darunter. &6Formationsfeld:&r genauso mit Formationskern.",
              "",
              "Das Annihilationsfeld baut den Block vor sich ab und nimmt Gegenstände auf, die es berührt. Es nimmt Spitzhacken-Verzauberungen an: Glück, Behutsamkeit und Effizienz wirken. Es baut nur ab, was das Netz auch speichern kann, also filterst du über eine partitionierte Zelle im Unternetz.",
              "",
              "Das Formationsfeld setzt Blöcke oder wirft Gegenstände aus, die das Netz hineinschiebt. Zusammen mit einem Importbus wird daraus eine Steinfarm ohne Hände.",
              "",
              "&cAchtung:&r Beide arbeiten als Fake-Spieler. Erlaube das in deinem Claim.",
          ],
          tasks=[task_item("ae2:annihilation_plane", 1), task_item("ae2:formation_plane", 1)],
          rewards=[reward_item("ae2:annihilation_core", 2), reward_xp(6)],
          deps=["interface"], icon="ae2:annihilation_plane"),

    quest("cpu_monitor", 12.5, 15.5, "&7Vergrößer deine CPU",
          subtitle="Mehr Speicher, und sehen, was sie tut.",
          description=[
              "&64k-Fertigungsspeicher:&r Fertigungseinheit und 4k-Komponente formlos. Größere Speicher erlauben Aufträge mit mehr Zutaten und Zwischenschritten.",
              "",
              "&6Fertigungsmonitor:&r Fertigungseinheit und &6ME-Speichermonitor&r formlos. In die CPU eingebaut, zeigt er den laufenden Auftrag.",
              "",
              "Die CPU bleibt ein volles Rechteck. Füllst du Lücken mit Fertigungseinheiten, darf sie jede Form haben.",
          ],
          tasks=[task_item("ae2:4k_crafting_storage", 1), task_item("ae2:crafting_monitor", 1)],
          rewards=[reward_item("ae2:crafting_unit", 2), reward_xp(6)],
          deps=["cpu"], icon="ae2:crafting_monitor"),

    quest("pattern_access", 5, 18.5, "&aBau eine Schablonen-Zugriffskonsole",
          subtitle="Alle Provider in einem Fenster.",
          description=[
              "Formlos aus einem &6Leuchtfeld&r, einem &6Konstruktionsprozessor&r und einem &6Schablonen-Provider&r.",
              "",
              "Steht eine Wand aus Providern und Assemblern dicht an dicht, kommst du an die mittleren nicht mehr heran. Die Konsole zeigt jeden Provider im Netz, und du legst Schablonen direkt hinein.",
          ],
          tasks=[task_item("ae2:pattern_access_terminal", 1)],
          rewards=[reward_item("ae2:blank_pattern", 4), reward_xp(5)],
          deps=["provider"], icon="ae2:pattern_access_terminal"),

    quest("crystal_fixer", 2.5, 28.5, "&3Repariere Knospenblöcke",
          subtitle="Der Crystal Fixer macht Certus wieder makellos.",
          description=[
              "Im Crystal Assembler: ein &6Extended Machine Frame&r, vier Certusquarz und zwei Quarzfasern.",
              "",
              "Setz ihn so, dass seine Vorderseite auf einen &6Certusquarzknospenblock&r zeigt, und gib ihm Strom. Rechtsklick mit &6Geladenem Certusquarzkristall&r füllt ihn auf. Er repariert den Knospenblock und hebt ihn Stufe um Stufe an.",
              "",
              "So wächst deine Certusfarm ohne Nachwerfen ins Wasser.",
          ],
          tasks=[task_item("extendedae:crystal_fixer", 1)],
          rewards=[reward_item("ae2:charged_certus_quartz_crystal", 4), reward_xp(8)],
          deps=["crystal_assembler"], icon="extendedae:crystal_fixer", optional=True),

    quest("tag_storage_bus", 5, 28.5, "&3Filter nach Tags",
          subtitle="Ein Speicherbus, der Tags lesen kann.",
          description=[
              "&6ME Tag Storage Bus:&r Logikprozessor oben, Redstone, Speicherbus, Redstone in der Mitte, ein Buch unten.",
              "",
              "Statt einzelner Gegenstände gibst du einen Tag ein, Sternchen sind erlaubt. &ec:raw_materials/*&r schickt alle Roherze in die Kiste dahinter, &ec:ingots/* | c:gems/*&r alle Barren und Edelsteine: &e|&r heißt oder.",
          ],
          tasks=[task_item("extendedae:tag_storage_bus", 1)],
          rewards=[reward_item("ae2:logic_processor", 2), reward_xp(5)],
          deps=["storage_bus"], icon="extendedae:tag_storage_bus", optional=True),
]

images = [
    head("title", "Applied Energistics 2", 0, -3.2, height=1.5, kind="title"),
    head("certus", "Meteoriten und Certus", 0, -1.4, colour="water"),
    head("processors", "Prozessoren", 0, 3.4, colour="brass"),
    head("network", "Das ME-Netz", 0, 7.6, colour="water"),
    head("autocrafting", "Autocrafting, Schritt für Schritt", 0, 14.6, colour="brass"),
    head("p2p", "P2P-Tunnel", 0, 19.6, colour="magic"),
    head("devices", "Geräte und Zellen", 9.6, 19.6, colour="stone"),
    head("extended", "Extended AE", 0, 25.4, colour="water"),
    head("flux", "Applied Flux", 8.6, 25.4, colour="fire"),
]

chapter(C, "Applied Energistics 2", "ae2:controller", "tech", quests, shape="square", order=17, stage=3,
        subtitle=["Stufe 3: Meteoriten, Prozessoren, das ME-Netz bis 16k und Autocrafting."], images=images)
