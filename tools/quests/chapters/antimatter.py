"""Mekanism in stage 5: the fission reactor and its fuel line, radiation, nuclear waste into
polonium and plutonium, the SPS and antimatter pellets (the tech goal wants 100), the
antiprotonic nucleosynthesizer and the Mekanism MoreMachine replicators. A short section
"Die Millionen" covers MEGA 16M to 256M cells, the bulk cell and the Advanced AE quantum
computer. Numbers come from the jars and config/Mekanism; cell recipes from kronwerke/ae2.js."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp, banner

C = "antimatter"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Kernspaltung ------------------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lMekanism: Antimaterie",
          subtitle="Das letzte Kapitel von Mekanism.",
          description=[
              "Mit &6Stufe 5, dem Chaoswerk&r, öffnet Mekanism den &6Spaltreaktor&r, Polonium, Plutonium, den &6Superkritischen Phasenschieber&r (SPS) und die Antimaterie.",
              "",
              "Der erste Schritt ist das &6Kernreaktorgehäuse&r: ein Stahlgehäuse in der Mitte, 4 Bleibarren drumherum, gibt 4 Stück. Ein Reaktor braucht viele davon, die Hülle ist ein geschlossener Kasten.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler von Stufe 5 will neben 64 Erwachten Draconiumblöcken &e100 Antimaterie-Pellets&r (die Zahl wächst mit der Spielerzahl). Jedes zählt 30 Punkte. Am Ende dieses Kapitels siehst du, warum das die größte Fabrik der Season wird.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_casing", 16)],
          rewards=[reward_item("mekanism:ingot_lead", 32), reward_table("s5_common"), reward_xp(10)],
          icon="mekanismgenerators:fission_reactor_casing", size=2.0, shape="hexagon"),

    quest("fuel", 2.75, 0, "&aSpaltbrennstoff",
          subtitle="Von Uran zu Brennstoff in fünf Schritten.",
          description=[
              "Der Reaktor verbrennt &aSpaltbrennstoff&r (Fissile Fuel). Die Kette:",
              "",
              "&e1.&r Uranbarren in der Anreicherungskammer zu &eGelbkuchen Uran&r, zwei pro Barren.",
              "&e2.&r Gelbkuchen im &eChemischen Oxidierer&r zu Uranoxid.",
              "&e3.&r &eFlusssäure&r in der &eChemischen Auflösungskammer&r aus Fluorit und Schwefelsäure. Schwefelsäure machst du aus Schwefeldioxid, Sauerstoff und Wasserdampf im Chemischen Injektor.",
              "&e4.&r Uranoxid und Flusssäure im &eChemischen Injektor&r zu Uranhexafluorid.",
              "&e5.&r Uranhexafluorid in der &eIsotopenzentrifuge&r zu Spaltbrennstoff, 1 zu 1.",
              "",
              "Zentrifuge und Auflösungskammer brauchen Elite- und Ultimative Schaltkreise. Die hast du aus Stufe 4.",
          ],
          tasks=[task_item("mekanism:isotopic_centrifuge", 1), task_item("mekanism:chemical_dissolution_chamber", 1)],
          rewards=[reward_item("mekanism:yellow_cake_uranium", 16), reward_xp(10)],
          deps=["welcome"], icon="mekanism:isotopic_centrifuge"),

    quest("assemblies", 2.75, 3, "&7Brennstäbe und Steuerstäbe",
          subtitle="Das Innere des Reaktors.",
          description=[
              "&6Kernbrennstoffbaugruppe&r (Fuel Assembly): Blei, Stahl und ein Einfacher Chemietank. Sie stehen als Säulen im Reaktor und lassen sich stapeln.",
              "&6Kontrollstabbaugruppe&r: Blei, Stahl und ein Elite-Schaltkreis. Auf jede Säule kommt oben genau eine.",
              "",
              "Jede Baugruppe erhöht die mögliche Brennrate und den Platz für Brennstoff und Abfall. Lass zwischen den Säulen Luft, das Kühlmittel braucht Oberfläche. Wie gut gekühlt wird, zeigt der Reaktor als Siedeeffizienz an.",
          ],
          tasks=[task_item("mekanismgenerators:fission_fuel_assembly", 4), task_item("mekanismgenerators:control_rod_assembly", 1)],
          rewards=[reward_item("mekanism:ingot_steel", 32)],
          deps=["welcome"], icon="mekanismgenerators:fission_fuel_assembly"),

    quest("reactor", 5.5, 1.5, "&6&lDer Spaltreaktor",
          subtitle="Wärme, Dampf und Atommüll.",
          description=[
              "&eDer Aufbau:&r ein geschlossener Kasten aus Kernreaktorgehäuse, innen die Säulen aus Brennstäben mit je einem Steuerstab obendrauf. In die Hülle setzt du &6Kernreaktor-Schnittstellen&r (2 pro Rezept, aus Gehäuse und einem Elite-Schaltkreis) für Brennstoff, Kühlmittel, Dampf und Abfall. Mit dem Konfigurator stellst du ihren Modus um.",
              "",
              "&eKühlung:&r Wasser wird zu Dampf. Den Dampf schickst du in die &6Industrieturbine&r aus Stufe 3. Jetzt hat sie endlich die Dampfquelle, für die sie gebaut wurde.",
              "",
              "&eLangsam anfangen:&r Der Reaktor startet mit 0,1 mB pro Tick. Erhöhe die Brennrate erst, wenn Kühlung und Turbine mithalten.",
              "",
              "&c&lEhrlich gesagt:&r Kernschmelzen sind auf diesem Server &caktiv&r. Wird der Reaktor zu heiß, nimmt er Schaden. Über 100 Prozent Schaden kann er explodieren, und dabei wird seine Strahlung um das Fünfzigfache verstärkt in die Gegend verteilt. Ein übervoller Abfalltank schadet ihm ebenfalls. Die Explosion hat einen Radius von 8 Blöcken. Die Gründe sind immer dieselben: zu wenig Kühlmittel, Dampf, der nicht abfließt, oder Abfall, der nicht abgepumpt wird.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_port", 4)],
          rewards=[reward_item("mekanismgenerators:fission_reactor_casing", 16), reward_table("s5_common"), reward_xp(20)],
          deps=["fuel", "assemblies"], icon="mekanismgenerators:fission_reactor_port", size=2.0, shape="gear"),

    quest("logic", 5.5, 4.5, "&cDer Not-Aus",
          subtitle="Der Logik-Adapter rettet deine Basis.",
          description=[
              "Der &6Kernreaktor-Logik-Adapter&r ist ein Gehäuse mit Redstone drumherum. Er sitzt in der Hülle und kann den Reaktor per Redstone abschalten, zum Beispiel bei zu hoher Temperatur oder sobald er Schaden nimmt.",
              "",
              "Stell ihn so ein, dass er den Reaktor stoppt, bevor etwas schiefgeht, und teste das einmal mit kleiner Brennrate. Das ist die wichtigste Viertelstunde in diesem Kapitel.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_logic_adapter", 1)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(10)],
          deps=["reactor"], icon="mekanismgenerators:fission_reactor_logic_adapter"),

    quest("radiation", 2.75, 6, "&eStrahlung",
          subtitle="Mekanism-Strahlung ist auf diesem Server an.",
          description=[
              "Atommüll, Polonium und Plutonium strahlen. Läuft ein Rohr leck oder fliegt ein Tank in die Luft, verseucht die Strahlung die Gegend und macht dich krank.",
              "",
              "&eWas hilft:&r ein &eGeigerzähler&r zeigt die Strahlung um dich, ein &eDosimeter&r die Dosis, die du schon abbekommen hast. Der &eSchutzanzug&r (Hazmat) schützt beim Arbeiten am Reaktor. Überschüssigen Abfall lagerst du in der &eTonne für radioaktiven Abfall&r, die ihn langsam abbaut.",
          ],
          tasks=[task_item("mekanism:geiger_counter", 1), task_item("mekanism:radioactive_waste_barrel", 2)],
          rewards=[reward_item("mekanism:hazmat_mask", 1), reward_item("mekanism:hazmat_gown", 1)],
          deps=["logic"], icon="mekanism:geiger_counter", optional=True),

    # ---- Polonium und Plutonium -----------------------------------------------------------
    quest("waste", 8.25, 1.5, "&2Atommüll",
          subtitle="Was der Reaktor übrig lässt, ist der Rohstoff.",
          description=[
              "Jedes mB Spaltbrennstoff wird zu einem mB &2Atommüll&r. Den pumpst du aus der Abfall-Schnittstelle ab, und er geht in zwei Richtungen:",
              "",
              "&eSolarneutronenaktivator&r: 10 mB Atommüll zu 1 mB &bPolonium&r. Er braucht freien Himmel und arbeitet bei Tag.",
              "&eIsotopenzentrifuge&r: 10 mB Atommüll zu 1 mB &cPlutonium&r.",
              "",
              "Für die Antimaterie willst du vor allem Polonium. Stell viele Aktivatoren auf, ein einzelner kommt nicht hinterher.",
          ],
          tasks=[task_item("mekanism:solar_neutron_activator", 4)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_xp(10)],
          deps=["reactor"], icon="mekanism:solar_neutron_activator"),

    quest("polonium", 11, 0, "&bPolonium-Pellets",
          subtitle="Für Gehäuse und Spulen.",
          description=[
              "In der &eDruckreaktionskammer&r: 1 000 mB &bPolonium&r, 1 000 mB Wasser und 1 Fluoritstaub ergeben ein &bPolonium-Pellet&r. Als Rest bleibt verbrauchter Atommüll.",
              "",
              "Pellets brauchst du für das SPS-Gehäuse (4 pro Block) und die Hochaufgeladene Spule (3). Das eigentliche Polonium für die Antimaterie bleibt Gas und läuft direkt ins SPS.",
          ],
          tasks=[task_item("mekanism:pellet_polonium", 8)],
          rewards=[reward_item("mekanism:dust_fluorite", 16), reward_xp(10)],
          deps=["waste"], icon="mekanism:pellet_polonium"),

    quest("plutonium", 11, 3, "&cPlutonium-Pellets",
          subtitle="Brennstoff, der sich selbst nachliefert.",
          description=[
              "Gleiches Rezept wie Polonium, nur mit &cPlutonium&r: 1 000 mB, Wasser und ein Fluoritstaub in der Druckreaktionskammer.",
              "",
              "&eWozu:&r Jedes SPS-Gehäuse braucht ein &cPlutonium-Pellet&r in der Mitte. Und Plutonium lässt sich zurück in Brennstoff verwandeln: In der &eChemischen Injektionskammer&r mit Chlorwasserstoff wird ein Pellet zu 4 Wiederverarbeiteten Spaltungs-Fragmenten, jedes davon im Oxidierer zu 2 000 mB Spaltbrennstoff.",
          ],
          tasks=[task_item("mekanism:pellet_plutonium", 4)],
          rewards=[reward_item("mekanism:dust_fluorite", 16), reward_xp(10)],
          deps=["waste"], icon="mekanism:pellet_plutonium"),

    # ---- Das SPS -----------------------------------------------------------------------
    quest("sps_casing", 13.75, 3, "&dSPS-Gehäuse",
          subtitle="Vier Polonium und ein Plutonium pro Block.",
          description=[
              "&6SPS-Gehäuse&r: 4 HDPE-Platten in den Ecken, 4 &bPolonium-Pellets&r an den Seiten, ein &cPlutonium-Pellet&r in der Mitte.",
              "&6SPS-Port&r: 4 Gehäuse um einen Ultimativen Schaltkreis.",
              "",
              "Das SPS ist ein Multiblock aus Gehäusen mit Ports in der Hülle. Ports nehmen Polonium an und geben Antimaterie ab, die Spulen an den Ports bringen den Strom. Mit dem Konfigurator schaltest du ihren Modus um.",
          ],
          tasks=[task_item("mekanism:sps_casing", 8), task_item("mekanism:sps_port", 2)],
          rewards=[reward_item("mekanism:hdpe_sheet", 16), reward_xp(10)],
          deps=["polonium", "plutonium"], icon="mekanism:sps_casing"),

    quest("coil", 13.75, 0, "&dHochaufgeladene Spule",
          subtitle="Hier kommt der Strom hinein.",
          description=[
              "&eRezept:&r 3 Kupferbarren oben, ein &eLaser&r zwischen 2 Ultimativen Schaltkreisen, unten 3 &bPolonium-Pellets&r.",
              "",
              "Die Spule muss direkt an einem SPS-Port sitzen, sonst formt sich das SPS nicht. Über sie fließt der Strom hinein, und davon braucht das SPS sehr viel.",
          ],
          tasks=[task_item("mekanism:supercharged_coil", 1)],
          rewards=[reward_item("mekanism:ultimate_control_circuit", 2), reward_xp(10)],
          deps=["polonium"], icon="mekanism:supercharged_coil"),

    quest("sps", 16.5, 1.5, "&5&lSuperkritischer Phasenschieber",
          subtitle="Aus Polonium wird Antimaterie.",
          description=[
              "Das SPS verwandelt &bPolonium&r in &5Antimaterie&r. Die Zahlen aus der Konfiguration dieses Servers:",
              "",
              "&e1 000 mB Polonium&r ergeben &e1 mB Antimaterie&r.",
              "Jedes mB Polonium kostet &e1 Million Joule&r.",
              "Ein Pellet sind &e1 000 mB Antimaterie&r.",
              "",
              "&eFür ein einziges Pellet&r brauchst du also 1 000 000 mB Polonium, dafür 10 000 000 mB Atommüll, und eine Billion Joule Strom. Mal hundert für das Ziel.",
              "",
              "Das heißt: mehrere Spaltreaktoren, eine lange Reihe Aktivatoren, und Strom aus allem, was ihr habt. Fusion aus Stufe 4 hilft, ebenso Powah und die Turbinen.",
          ],
          tasks=[task_checkmark("Mein SPS ist geformt und läuft")],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["sps_casing", "coil"], icon="mekanism:sps_port", size=2.0, shape="gear"),

    quest("pellet", 19.25, 1.5, "&5Das erste Pellet",
          subtitle="1 000 mB in den Kristallisator.",
          description=[
              "Die Antimaterie aus dem SPS ist ein Gas. Der &eChemische Kristallisator&r macht aus 1 000 mB davon ein &5Antimaterie-Pellet&r.",
              "",
              "Umgekehrt geht es auch: Der Oxidierer macht aus einem Pellet wieder 1 000 mB Gas. So kannst du Antimaterie lagern und später für den Kernsynthesizer verwenden.",
          ],
          tasks=[task_item("mekanism:pellet_antimatter", 1)],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["sps"], icon="mekanism:pellet_antimatter"),

    # ---- Was Antimaterie kann ---------------------------------------------------------------
    quest("nucleosynthesizer", 22, 0, "&dAntiprotonischer Kernsynthesizer",
          subtitle="Kohle zu Diamant, Ei zu Drachenei.",
          description=[
              "&eRezept:&r ein Stahlgehäuse in der Mitte, 2 &5Antimaterie-Pellets&r links und rechts, 2 Ultimative Schaltkreise oben und unten, 4 Atomlegierungen in den Ecken.",
              "",
              "Er verwandelt Gegenstände mit ein paar mB Antimaterie: Kohle wird zu Diamant, ein Ei zum Drachenei, Eisen, Lapis, Redstone, Quarz, Glowstone, Smaragd und einige seltene Dinge wie Echoscherben oder ein Herz des Meeres. Ein Diamant kostet 4 mB.",
              "",
              "Die zwei Pellets für den Bau fehlen dem Obelisken. Überlegt euch, ob ihr ihn wirklich braucht.",
          ],
          tasks=[task_item("mekanism:antiprotonic_nucleosynthesizer", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 8), reward_xp(15)],
          deps=["pellet"], icon="mekanism:antiprotonic_nucleosynthesizer", optional=True),

    quest("replicator", 22, 3, "&3Replikatoren",
          subtitle="Mekanism MoreMachine kopiert Dinge.",
          description=[
              "Der Kernsynthesizer macht aus &e64 Leeren Kristallen&r und 2 mB Antimaterie eine &3UU-Materie&r. Sie ist die Zutat für die drei &3Replikatoren&r aus Mekanism MoreMachine: für Gegenstände, Flüssigkeiten und Chemikalien. Jeder braucht eine UU-Materie, Atomlegierung, 2 Ultimative Schaltkreise und ein Stahlgehäuse.",
              "",
              "Im Betrieb frisst der Replikator UU-Materie als Chemikalie (der Oxidierer macht aus einem Stück 500 mB) und macht daraus Kopien.",
              "",
              "&eRezept auf Kronwerke:&r Der Gegenstands-Replikator kopiert nur noch &eSteine&r und &eErze&r (je 1 mB UU-Materie), &eStämme&r (4 mB), &eBretter&r (1 mB) sowie &eEisen-, Kupfer- und Goldbarren&r (je 5 mB). Andere Barren kopiert er nicht.",
              "",
              "Der &3Große Kernsynthesizer&r aus MoreMachine ist auch offen, er braucht zwei Antimaterie-Pellets und einen Robit.",
          ],
          tasks=[task_item("mekmm:replicator", 1)],
          rewards=[reward_xp(15)],
          deps=["pellet"], icon="mekmm:replicator", optional=True),

    quest("goal", 19.25, 5, "&5&lHundert Pellets",
          subtitle="Die Antimaterie für den Obelisken.",
          description=[
              "Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r. Im Technik-Pfeiler stehen &e64 Erwachte Draconiumblöcke&r und &e100 Antimaterie-Pellets&r. Die Pellet-Zahl wächst mit der Zahl der Spieler.",
              "",
              "&eWas das heißt:&r Eine Antimaterie-Fabrik, die tagelang läuft. Mehrere Reaktoren teilen sich die Arbeit, und jedes Pellet zählt, egal wer ihn baut. Tut euch zusammen: Einer betreibt die Reaktoren, einer die Aktivatoren, einer das Kraftwerk.",
              "",
              "&eKronwerke:&r Stell eine Kiste neben den Obelisken und lass den Kristallisator direkt hineinlaufen. Den Stand zeigt &e/kw goals&r.",
          ],
          tasks=[task_item("mekanism:pellet_antimatter", 4)],
          rewards=[reward_table("s5_rare"), reward_xp(30)],
          deps=["pellet"], icon="mekanism:pellet_antimatter", size=2.5, shape="gear"),

    # ---- Die Millionen -----------------------------------------------------------------------
    quest("mega_16m", 8.25, 8.5, "&b16M MEGA-Zellen",
          subtitle="Speicher braucht jetzt Erwachtes Draconium.",
          description=[
              "Ab Stufe 5 gehen die MEGA-Zellen über 4M hinaus: 16M, 64M und 256M.",
              "",
              "&eRezept auf Kronwerke:&r Die &b16M-Komponente&r ist 3 4M-Komponenten, ein &eAkkumulationsprozessor&r oben, Enderperlenstaub in den Ecken und in der Mitte ein &5Erwachtes Draconiumnugget&r. Die 64M- und 256M-Komponenten bauen genauso auf der vorigen auf, mit Materiebällen in den Ecken und wieder einem Erwachten Nugget.",
              "",
              "Die Zelle selbst craftest du wie immer aus Komponente und MEGA-Gehäuse.",
          ],
          tasks=[task_item("megacells:cell_component_16m", 1)],
          rewards=[reward_item("megacells:accumulation_processor", 4), reward_xp(10)],
          icon="megacells:cell_component_16m"),

    quest("mega_256m", 11, 8.5, "&b256M",
          subtitle="Für den Rest der Season genug Platz.",
          description=[
              "Eine &b256M-Komponente&r braucht drei 64M-Komponenten, und jede davon drei 16M. Zusammen sind das 13 Erwachte Nuggets und 27 4M-Komponenten.",
              "",
              "Rechne vorher nach, ob du den Platz wirklich brauchst. Ein Laufwerk voller 16M-Zellen trägt schon sehr viel.",
          ],
          tasks=[task_item("megacells:item_storage_cell_256m", 1)],
          rewards=[reward_xp(15)],
          deps=["mega_16m"], icon="megacells:item_storage_cell_256m", optional=True),

    quest("bulk", 8.25, 11.5, "&bBulk-Zelle",
          subtitle="Eine Sorte, so viel du willst.",
          description=[
              "Die &bMEGA-Bulk-Zelle&r speichert nur eine einzige Sorte, davon aber praktisch beliebig viel. Ideal für Bruchstein, Draconium oder alles, was in Massen anfällt.",
              "",
              "&eRezept auf Kronwerke:&r Die Bulk-Komponente braucht eine 1M-Komponente, eine Räumliche Komponente 16³, 2 Akkumulationsprozessoren, Himmelssteinstaub und ein &5Erwachtes Draconiumnugget&r. Die Zelle dazu: Vibrierendes Quarzglas, Himmelssteinstaub und 3 Netheritbarren.",
              "",
              "Die &bKomprimierungskarte&r (Erweiterte Karte und Materieball) lässt die Bulk-Zelle zwischen Barren, Blöcken und Nuggets umrechnen.",
          ],
          tasks=[task_item("megacells:bulk_item_cell", 1)],
          rewards=[reward_item("ae2:sky_dust", 16), reward_xp(10)],
          deps=["mega_16m"], icon="megacells:bulk_item_cell", optional=True),

    quest("quantum", 11, 11.5, "&dDer Quantencomputer",
          subtitle="Advanced AE für riesige Bestellungen.",
          description=[
              "Der &dQuantencomputer&r von Advanced AE ist eine Crafting-CPU als Multiblock. Die Außenschicht besteht aus &dQuantencomputer-Strukturglas&r, innen sitzen Kern, Einheiten, Speicher und Beschleuniger. Auf diesem Server ist er höchstens 7 mal 7 mal 7 groß.",
              "",
              "Jeder &dBeschleuniger&r bringt 8 Threads. Ein &dMulti-Threader&r vervierfacht sie, ein &dDatenverschränker&r vervierfacht seinen Speicher, jeweils höchstens einer pro Computer.",
              "",
              "Die Teile brauchen Singularitäten und Zersplitterte Singularitäten aus der Reaktionskammer von Advanced AE, und Parallelprozessoren aus ExtendedAE. Der Speicher braucht 256k-Komponenten und Quantenprozessoren.",
          ],
          tasks=[task_item("advanced_ae:quantum_core", 1), task_item("advanced_ae:quantum_structure", 16)],
          rewards=[reward_item("ae2:singularity", 4), reward_xp(15)],
          deps=["mega_16m"], icon="advanced_ae:quantum_core", optional=True),
]

images = [
    head("title", "Mekanism: Antimaterie", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("waste", "Atommüll", 7.6, -1.4, colour="nature"),
    head("sps", "Das SPS", 13.2, -1.4, colour="magic"),
    head("use", "Was Antimaterie kann", 18.8, -1.4, colour="end"),
    head("millions", "Die Millionen", 7.6, 6.9, colour="water"),
]

chapter(C, "Mekanism: Antimaterie", "mekanism:pellet_antimatter", "tech", quests, shape="square",
        order=43, stage=5,
        subtitle=["Stufe 5: Spaltreaktor, Polonium und Plutonium, das SPS, Antimaterie und die Millionen im ME-Netz."],
        images=images)
