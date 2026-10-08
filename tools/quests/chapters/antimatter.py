"""Mekanism in stage 5, one step per quest: the fuel line (yellow cake, uranium oxide,
hydrofluoric acid, uranium hexafluoride, fissile fuel), the fission reactor (casing, fuel and
control rod assemblies, ports, logic adapter), radiation, nuclear waste into polonium and
plutonium, reprocessing, the SPS (casing, port, supercharged coil), the MoreMachine large wind
generator (stage 5) as its power, antimatter pellets (the tech goal), the nucleosynthesizer,
UU matter and the replicators, and "Die Millionen" (MEGA 16M to 256M, bulk cell, quantum
computer). The induction matrix, fusion and the stage 4 machines are in mekanism_elite.py.
Numbers from the Mekanism jars, config/Mekanism and config/MekanismMoreMachine; cell recipes
from kronwerke/ae2.js."""
from ftbq import chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp, banner

C = "antimatter"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Brennstoff ------------------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lBau Kernreaktorgehäuse",
          subtitle="Die Hülle des Spaltreaktors.",
          description=[
              "Ein &6Stahlgehäuse&r in die Mitte, &64 Bleibarren&r drumherum. Gibt 4 &6Kernreaktorgehäuse&r.",
              "",
              "Mit &6Stufe 5&r öffnet Mekanism Spaltreaktor, Polonium, Plutonium, das SPS und die Antimaterie. Ein Reaktor ist ein geschlossener Kasten, rechne mit ein paar Dutzend Gehäusen.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler von Stufe 5 will &e100 Antimaterie-Pellets&r (wächst mit der Spielerzahl), jedes 30 Punkte. Induktionsmatrix und Fusion stehen im Kapitel &dMekanism: Elite&r.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_casing", 16)],
          rewards=[reward_item("mekanism:ingot_lead", 32), reward_table("s5_common"), reward_xp(10)],
          icon="mekanismgenerators:fission_reactor_casing", size=2.0, shape="hexagon"),

    quest("yellowcake", 2.5, 0, "&aReicher Uran zu Gelbkuchen an",
          subtitle="Schritt 1 von 5 zum Brennstoff.",
          description=[
              "Ein &6Uranbarren&r in der &6Anreicherungskammer&r gibt &e2 Gelbkuchen&r.",
              "",
              "Uran kommt aus der Erzleiter, siehe Kapitel &5Mekanism: Erz Schritt für Schritt&r.",
          ],
          tasks=[task_item("mekanism:yellow_cake_uranium", 16)],
          rewards=[reward_item("mekanism:ingot_uranium", 8), reward_xp(5)],
          deps=["welcome"], icon="mekanism:yellow_cake_uranium"),

    quest("oxide", 5, 0, "&aOxidier den Gelbkuchen",
          subtitle="Schritt 2: Uranoxid.",
          description=[
              "Gelbkuchen in den &6Chemischen Oxidierer&r. Ein Stück gibt &e250 mB Uranoxid&r.",
              "",
              "Häng einen Chemikalientank an den Ausgang, das Oxid wartet dort auf die Säure.",
          ],
          tasks=[task_item("mekanism:chemical_oxidizer", 1)],
          rewards=[reward_item("mekanism:yellow_cake_uranium", 8), reward_xp(5)],
          deps=["yellowcake"], icon="mekanism:chemical_oxidizer"),

    quest("hf", 7.5, 0, "&aLös Fluorit in Schwefelsäure",
          subtitle="Schritt 3: Flusssäure.",
          description=[
              "&6Fluorit&r in die &6Chemische Auflösungskammer&r, &6Schwefelsäure&r dazu. Ein Fluorit gibt &e1 000 mB Flusssäure&r, ein Fluoritblock 9 000 mB.",
              "",
              "Schwefelsäure und die Kammer kennst du aus der 5x-Straße im Kapitel &5Mekanism: Erz Schritt für Schritt&r. Fluorit kommt als Erz in der Tiefe.",
          ],
          tasks=[task_item("mekanism:chemical_dissolution_chamber", 1), task_item("mekanism:fluorite_gem", 16)],
          rewards=[reward_item("mekanism:fluorite_gem", 16), reward_xp(5)],
          deps=["oxide"], icon="mekanism:chemical_dissolution_chamber"),

    quest("uf6", 10, 0, "&aMisch Uranhexafluorid",
          subtitle="Schritt 4: Oxid und Säure.",
          description=[
              "Uranoxid und Flusssäure in den &6Chemischen Infusor&r. Je 1 mB von beiden geben &e2 mB Uranhexafluorid&r.",
              "",
              "Ein eigener Infusor nur für diese Mischung spart dir das Umstecken.",
          ],
          tasks=[task_item("mekanism:chemical_infuser", 1)],
          rewards=[reward_item("mekanism:fluorite_gem", 16), reward_xp(5)],
          deps=["hf"], icon="mekanism:chemical_infuser"),

    quest("fuel", 12.5, 0, "&a&lSchleuder Spaltbrennstoff",
          subtitle="Schritt 5: der Brennstoff.",
          description=[
              "Uranhexafluorid in die &6Isotopenzentrifuge&r. 1 mB gibt &e1 mB Spaltbrennstoff&r.",
              "",
              "Von Gelbkuchen bis Brennstoff: ein Uranbarren wird zu 1 000 mB Brennstoff. Der Reaktor verbrennt am Anfang 0,1 mB pro Tick.",
          ],
          tasks=[task_item("mekanism:isotopic_centrifuge", 1)],
          rewards=[reward_item("mekanism:yellow_cake_uranium", 16), reward_table("s5_common"), reward_xp(10)],
          deps=["uf6"], icon="mekanism:isotopic_centrifuge"),

    # ---- Der Spaltreaktor ----------------------------------------------------------------
    quest("assemblies", 2.5, 3, "&7Bau Brennstoffbaugruppen",
          subtitle="Die Säulen im Reaktor.",
          description=[
              "&6Kernbrennstoffbaugruppe:&r Blei, Stahl und ein &6Einfacher Chemietank&r. Sie stehen als Säulen im Reaktor und lassen sich stapeln.",
              "",
              "Jede Baugruppe erhöht Brennrate und Platz für Brennstoff und Abfall. Lass Luft zwischen den Säulen, das Kühlmittel braucht Oberfläche.",
          ],
          tasks=[task_item("mekanismgenerators:fission_fuel_assembly", 4)],
          rewards=[reward_item("mekanism:ingot_steel", 32)],
          deps=["welcome"], icon="mekanismgenerators:fission_fuel_assembly"),

    quest("control_rod", 5, 3, "&7Setz Steuerstäbe obendrauf",
          subtitle="Einer pro Säule.",
          description=[
              "&6Kontrollstabbaugruppe:&r Blei, Stahl und ein &6Elite-Schaltkreis&r. Auf jede Säule kommt oben genau eine.",
              "",
              "Ohne Steuerstab zählt die Säule nicht. Wie gut gekühlt wird, zeigt der Reaktor später als Siedeeffizienz.",
          ],
          tasks=[task_item("mekanismgenerators:control_rod_assembly", 1)],
          rewards=[reward_item("mekanism:elite_control_circuit", 2), reward_xp(5)],
          deps=["assemblies"], icon="mekanismgenerators:control_rod_assembly"),

    quest("ports", 7.5, 3, "&7Bau Reaktor-Schnittstellen",
          subtitle="Rein mit Brennstoff und Wasser, raus mit Dampf und Abfall.",
          description=[
              "Gehäuse und ein &6Elite-Schaltkreis&r geben zwei &6Kernreaktor-Schnittstellen&r. Du brauchst vier: Brennstoff, Kühlmittel, Dampf und Abfall.",
              "",
              "Mit dem &6Konfigurator&r schaltest du den Modus jeder Schnittstelle um.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_port", 4)],
          rewards=[reward_item("mekanismgenerators:fission_reactor_casing", 16), reward_xp(10)],
          deps=["control_rod"], icon="mekanismgenerators:fission_reactor_port"),

    quest("reactor", 10, 3, "&6&lStarte den Spaltreaktor",
          subtitle="Wärme, Dampf und Atommüll.",
          description=[
              "Kasten aus Gehäuse, innen die Säulen, Schnittstellen in die Hülle. Wasser rein, Brennstoff rein, dann mit &e0,1 mB/t&r anfangen.",
              "",
              "Wasser wird zu Dampf. Den schickst du in die &6Industrieturbine&r aus Stufe 3. Brennrate erst erhöhen, wenn Kühlung und Turbine mithalten.",
              "",
              "&c&lEhrlich:&r Kernschmelzen sind &caktiv&r. Über 100 Prozent Schaden kann er explodieren (Radius 8), und seine Strahlung wird dabei verfünfzigfacht verteilt. Ursachen: zu wenig Kühlmittel, Dampf staut sich, Abfall wird nicht abgepumpt.",
          ],
          tasks=[task_checkmark("Mein Spaltreaktor läuft")],
          rewards=[reward_item("mekanismgenerators:fission_reactor_casing", 16), reward_table("s5_common"), reward_xp(20)],
          deps=["fuel", "ports"], icon="mekanismgenerators:fission_reactor_casing", size=2.0, shape="gear"),

    quest("logic", 12.5, 3, "&cBau den Not-Aus",
          subtitle="Der Logik-Adapter rettet deine Basis.",
          description=[
              "Ein Gehäuse mit Redstone drumherum ergibt den &6Kernreaktor-Logik-Adapter&r. Setz ihn in die Hülle.",
              "",
              "Stell ihn so ein, dass er den Reaktor bei zu hoher Temperatur oder bei Schaden abschaltet, und teste das einmal mit kleiner Brennrate. Das ist die wichtigste Viertelstunde in diesem Kapitel.",
          ],
          tasks=[task_item("mekanismgenerators:fission_reactor_logic_adapter", 1)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(10)],
          deps=["reactor"], icon="mekanismgenerators:fission_reactor_logic_adapter"),

    quest("radiation", 15, 3, "&eMiss die Strahlung",
          subtitle="Mekanism-Strahlung ist an.",
          description=[
              "&6Geigerzähler&r zeigt die Strahlung um dich, das &6Dosimeter&r deine Dosis. Der &6Schutzanzug&r schützt am Reaktor. Überschüssigen Abfall lagerst du in der &6Tonne für radioaktiven Abfall&r, die ihn langsam abbaut.",
              "",
              "Läuft ein Rohr leck oder fliegt ein Tank in die Luft, verseucht die Strahlung die Gegend. Eine Quelle von 1 000 Sv/h braucht etwa zehn Stunden, bis sie abgeklungen ist.",
          ],
          tasks=[task_item("mekanism:geiger_counter", 1), task_item("mekanism:radioactive_waste_barrel", 2)],
          rewards=[reward_item("mekanism:hazmat_mask", 1), reward_item("mekanism:hazmat_gown", 1)],
          deps=["logic"], icon="mekanism:geiger_counter", optional=True),

    quest("hazmat", 17.5, 3, "&eZieh den ganzen Schutzanzug an",
          subtitle="Vier Teile Blei, ein Dosimeter.",
          description=[
              "Alle Teile sind &6Blei&r mit Farbstoff: Maske, Kittel und Hose mit orangem, die Stiefel mit schwarzem. Hose wie eine Eisenhose, Stiefel wie Eisenstiefel, je mit dem Farbstoff in der Mitte.",
              "",
              "Jedes Teil hält einen Teil der Strahlung ab, erst alle vier zusammen schützen ganz. Das &6Dosimeter&r (Blei im Kreuz um ein Redstone) zeigt per Rechtsklick, wie viel du schon abbekommen hast. Die Dosis baut sich mit der Zeit wieder ab.",
              "",
              "Wer die MekaSuit trägt, nimmt statt des Anzugs das Strahlenschutzmodul: Infundierte Legierung, ein Bleiblock, Basismodul und HDPE.",
          ],
          tasks=[task_item("mekanism:hazmat_pants", 1), task_item("mekanism:hazmat_boots", 1), task_item("mekanism:dosimeter", 1)],
          rewards=[reward_item("mekanism:ingot_lead", 16), reward_xp(5)],
          deps=["radiation"], icon="mekanism:hazmat_mask", optional=True),

    quest("sodium", 12.5, 4.5, "&bKühl mit Natrium",
          subtitle="Der Dampf entsteht im Kessel.",
          description=[
              "Statt Wasser kannst du &6Natrium&r in die Kühlmittel-Schnittstelle pumpen. Der Reaktor macht daraus &6überhitztes Natrium&r statt Dampf. Natrium kühlt besser als Wasser.",
              "",
              "Das heiße Natrium geht in den &6Thermoelektrischen Dampfkessel&r aus Stufe 3. Er nimmt es als Wärmequelle statt Widerstandsheizern, kocht Wasser zu Dampf für die Turbine und gibt das abgekühlte Natrium zurück. Ein Kreislauf ohne Verlust.",
              "",
              "Natrium fällt beim Chlor an: Sole im Elektrolyseur, siehe Kapitel &5Mekanism&r. Wer es seit Stufe 2 gesammelt hat, ist jetzt froh.",
          ],
          tasks=[task_checkmark("Natriumkreislauf läuft")],
          rewards=[reward_item("mekanism:block_salt", 16), reward_xp(10)],
          deps=["reactor"], icon="mekanism:sodium_bucket", optional=True),

    # ---- Polonium und Plutonium -----------------------------------------------------------
    quest("waste", 0, 8, "&2Aktivier Atommüll zu Polonium",
          subtitle="Was der Reaktor übrig lässt, ist der Rohstoff.",
          description=[
              "Pump den &2Atommüll&r aus der Abfall-Schnittstelle in einen &6Solarneutronenaktivator&r. &e10 mB Atommüll&r geben &e1 mB Polonium&r. Er braucht freien Himmel und arbeitet bei Tag.",
              "",
              "Jedes mB Brennstoff wird ein mB Atommüll. Für die Antimaterie willst du vor allem Polonium, stell also viele Aktivatoren auf.",
          ],
          tasks=[task_item("mekanism:solar_neutron_activator", 4)],
          rewards=[reward_item("mekanism:hdpe_sheet", 8), reward_xp(10)],
          deps=["reactor"], icon="mekanism:solar_neutron_activator"),

    quest("polonium", 2.5, 7, "&bPress Polonium-Pellets",
          subtitle="Für Gehäuse und Spulen.",
          description=[
              "In der &6Druckreaktionskammer&r: &e1 000 mB Polonium&r, 1 000 mB Wasser und 1 Fluoritstaub geben ein &bPolonium-Pellet&r. Übrig bleibt verbrauchter Atommüll.",
              "",
              "Pellets brauchst du für SPS-Gehäuse (4) und Spulen (3). Das Polonium für die Antimaterie bleibt Gas und läuft direkt ins SPS. In Stufe 4 kamen Pellets nur über NuclearCraft, siehe Kapitel &dMekanism: Elite&r.",
          ],
          tasks=[task_item("mekanism:pellet_polonium", 8)],
          rewards=[reward_item("mekanism:dust_fluorite", 16), reward_xp(10)],
          deps=["waste"], icon="mekanism:pellet_polonium"),

    quest("plutonium", 2.5, 9, "&cSchleuder Atommüll zu Plutonium",
          subtitle="Dann Pellets daraus.",
          description=[
              "In der &6Isotopenzentrifuge&r geben &e10 mB Atommüll&r &e1 mB Plutonium&r. In der Druckreaktionskammer werden 1 000 mB mit Wasser und Fluoritstaub zu einem &cPlutonium-Pellet&r.",
              "",
              "Jedes SPS-Gehäuse braucht eins in der Mitte.",
          ],
          tasks=[task_item("mekanism:pellet_plutonium", 4)],
          rewards=[reward_item("mekanism:dust_fluorite", 16), reward_xp(10)],
          deps=["waste"], icon="mekanism:pellet_plutonium"),

    quest("reprocess", 5, 9, "&cMach aus Plutonium neuen Brennstoff",
          subtitle="Ein Pellet, 8 000 mB Brennstoff.",
          description=[
              "Ein &cPlutonium-Pellet&r in die &6Chemische Injektionskammer&r mit Chlorwasserstoff gibt &e4 Wiederaufbereitete Spaltfragmente&r. Jedes wird im Oxidierer zu &e2 000 mB Spaltbrennstoff&r.",
              "",
              "So läuft der Reaktor teilweise aus seinem eigenen Abfall.",
          ],
          tasks=[task_item("mekanism:reprocessed_fissile_fragment", 4)],
          rewards=[reward_item("mekanism:pellet_plutonium", 1), reward_xp(10)],
          deps=["plutonium"], icon="mekanism:reprocessed_fissile_fragment", optional=True),

    quest("qio_hyper", 7.5, 9, "&dBau ein Hyperdichtes QIO-Laufwerk",
          subtitle="Achtmal so viel Platz.",
          description=[
              "Vier &cPlutonium-Pellets&r in die Ecken, vier normale &6QIO-Laufwerke&r an die Seiten, ein Teleportationskern in die Mitte.",
              "",
              "Es fasst &e128 000 Gegenstände&r in &e256 Sorten&r, das normale Laufwerk 16 000 in 128. Steck es in deine Laufwerk Reihe aus Stufe 4, das Netz bleibt dasselbe.",
          ],
          tasks=[task_item("mekanism:qio_drive_hyper_dense", 1)],
          rewards=[reward_item("mekanism:pellet_plutonium", 1), reward_xp(10)],
          deps=["plutonium"], icon="mekanism:qio_drive_hyper_dense", optional=True),

    quest("qio_dilating", 10, 9, "&dBau ein Zeiterweiterndes QIO-Laufwerk",
          subtitle="Eine Million Gegenstände.",
          description=[
              "Vier Plutonium-Pellets in die Ecken, vier &6Hyperdichte Laufwerke&r an die Seiten, ein &bPolonium-Pellet&r in die Mitte. Es fasst &e1 048 000 Gegenstände&r in &e1 024 Sorten&r.",
              "",
              "&eDas letzte:&r Vier Polonium-Pellets, vier Zeiterweiternde Laufwerke und ein &5Antimaterie-Pellet&r ergeben das &6Supermassive QIO-Laufwerk&r mit &e16 Milliarden&r Gegenständen in 8 192 Sorten.",
          ],
          tasks=[task_item("mekanism:qio_drive_time_dilating", 1)],
          rewards=[reward_item("mekanism:pellet_polonium", 2), reward_xp(15)],
          deps=["qio_hyper", "polonium"], icon="mekanism:qio_drive_time_dilating", optional=True),

    # ---- Das SPS -----------------------------------------------------------------------
    quest("sps_casing", 0, 12.5, "&dBau SPS-Gehäuse",
          subtitle="Vier Polonium und ein Plutonium pro Block.",
          description=[
              "&6HDPE-Platten&r in die Ecken, &6Polonium-Pellets&r an die Seiten, ein &6Plutonium-Pellet&r in die Mitte.",
              "",
              "Das SPS ist ein Multiblock aus diesen Gehäusen. Bau gleich einen Vorrat.",
          ],
          tasks=[task_item("mekanism:sps_casing", 8)],
          rewards=[reward_item("mekanism:hdpe_sheet", 16), reward_xp(10)],
          deps=["polonium", "plutonium"], icon="mekanism:sps_casing"),

    quest("sps_port", 2.5, 12.5, "&dBau SPS-Ports",
          subtitle="Polonium rein, Antimaterie raus.",
          description=[
              "4 &6SPS-Gehäuse&r um einen &6Ultimativen Schaltkreis&r ergeben einen &6SPS-Port&r.",
              "",
              "Ports sitzen in der Hülle. Mit dem Konfigurator schaltest du sie auf Eingang oder Ausgang.",
          ],
          tasks=[task_item("mekanism:sps_port", 2)],
          rewards=[reward_item("mekanism:ultimate_control_circuit", 2), reward_xp(10)],
          deps=["sps_casing"], icon="mekanism:sps_port"),

    quest("coil", 2.5, 14.5, "&dBau eine Hochaufgeladene Spule",
          subtitle="Hier kommt der Strom hinein.",
          description=[
              "Oben 3 &6Kupferbarren&r, in der Mitte ein &6Laser&r zwischen 2 &6Ultimativen Schaltkreisen&r, unten 3 &6Polonium-Pellets&r.",
              "",
              "Die Spule sitzt direkt an einem SPS-Port, sonst formt sich das SPS nicht. Über sie fließt der Strom hinein.",
          ],
          tasks=[task_item("mekanism:supercharged_coil", 1)],
          rewards=[reward_item("mekanism:ultimate_control_circuit", 2), reward_xp(10)],
          deps=["sps_casing"], icon="mekanism:supercharged_coil"),

    quest("wind", 5, 14.5, "&bStell einen Großen Windgenerator auf",
          subtitle="Mekanism MoreMachine, Stufe 5.",
          description=[
              "Sechs &6Stahlblöcke&r an die Seiten, oben in der Mitte ein &6Windgenerator&r, in der Mitte ein &6Robit&r, unten eine &6Ultimative Induktionszelle&r.",
              "",
              "Er liefert &e2 250 000 bis 3 750 000 J/t&r, also 900 000 bis 1 500 000 FE/t, und speichert 256,6 Millionen J. Ein Pellet Antimaterie kostet eine Billion J: ein Großer Windgenerator allein braucht dafür rund viereinhalb Stunden.",
          ],
          tasks=[task_item("mekmm:large_wind_generator", 1)],
          rewards=[reward_item("mekanism:block_steel", 8), reward_xp(15)],
          deps=["sps_casing"], icon="mekmm:large_wind_generator"),

    quest("sps", 5, 12.5, "&5&lForme das SPS",
          subtitle="Aus Polonium wird Antimaterie.",
          description=[
              "Gehäuse als Kasten, Ports in die Hülle, Spule an einen Port, Strom an die Spule, Polonium in den Eingangsport.",
              "",
              "&e1 000 mB Polonium&r geben &e1 mB Antimaterie&r. Jedes mB Polonium kostet &e1 Million J&r. Ein Pellet sind 1 000 mB Antimaterie, also 1 000 000 mB Polonium, 10 000 000 mB Atommüll und eine Billion J.",
              "",
              "Mehrere Spaltreaktoren, eine lange Reihe Aktivatoren und Strom aus allem, was ihr habt.",
          ],
          tasks=[task_checkmark("Mein SPS ist geformt und läuft")],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["sps_port", "coil"], icon="mekanism:sps_port", size=2.0, shape="gear"),

    quest("pellet", 7.5, 12.5, "&5Kristallisier das erste Pellet",
          subtitle="1 000 mB in den Kristallisator.",
          description=[
              "Die Antimaterie aus dem SPS ist ein Gas. Der &6Chemische Kristallisator&r macht aus &e1 000 mB&r ein &5Antimaterie-Pellet&r.",
              "",
              "Umgekehrt macht der Oxidierer aus einem Pellet wieder 1 000 mB Gas. So lagerst du Antimaterie.",
          ],
          tasks=[task_item("mekanism:pellet_antimatter", 1)],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["sps"], icon="mekanism:pellet_antimatter"),

    quest("goal", 10, 12.5, "&5&lBring Antimaterie zum Obelisken",
          subtitle="Die größte Fabrik der Season.",
          description=[
              "Lass den Kristallisator direkt in eine Kiste am Obelisken laufen. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r: &e64 Erwachte Draconiumblöcke&r und &e100 Antimaterie-Pellets&r. Teilt euch auf: einer die Reaktoren, einer die Aktivatoren, einer das Kraftwerk.",
          ],
          tasks=[task_item("mekanism:pellet_antimatter", 4)],
          rewards=[reward_table("s5_rare"), reward_xp(30)],
          deps=["pellet"], icon="mekanism:pellet_antimatter", size=2.5, shape="gear"),

    # ---- Was Antimaterie kann ---------------------------------------------------------------
    quest("nucleosynthesizer", 0, 17.5, "&dBau einen Antiprotonischen Kernsynthesizer",
          subtitle="Kohle zu Diamant, Ei zu Drachenei.",
          description=[
              "Ein &6Stahlgehäuse&r in die Mitte, 2 &6Antimaterie-Pellets&r links und rechts, 2 &6Ultimative Schaltkreise&r oben und unten, 4 &6Atomlegierungen&r in die Ecken.",
              "",
              "Er verwandelt Dinge mit ein paar mB Antimaterie: Kohle zu Diamant (4 mB), Ei zu Drachenei, dazu Eisen, Lapis, Redstone, Quarz, Glowstone, Smaragd, Echoscherben, Herz des Meeres. Die zwei Pellets fehlen dem Obelisken.",
          ],
          tasks=[task_item("mekanism:antiprotonic_nucleosynthesizer", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 8), reward_xp(15)],
          deps=["pellet"], icon="mekanism:antiprotonic_nucleosynthesizer", optional=True),

    quest("uu", 2.5, 17.5, "&3Mach UU-Materie",
          subtitle="Die Zutat der Replikatoren.",
          description=[
              "Der Kernsynthesizer macht aus &e64 Leeren Kristallen&r und 2 mB Antimaterie eine &3UU-Materie&r.",
              "",
              "Der Oxidierer macht aus einem Stück 500 mB UU-Materie als Chemikalie. Davon leben die Replikatoren.",
          ],
          tasks=[task_item("mekmm:uu_matter", 1)],
          rewards=[reward_xp(10)],
          deps=["nucleosynthesizer"], icon="mekmm:uu_matter", optional=True),

    quest("dragon_egg", 2.5, 18.75, "&5Brüte ein Drachenei aus",
          subtitle="Ein Hühnerei und 4 mB Antimaterie.",
          description=[
              "Ein &6Ei&r im Antiprotonischen Kernsynthesizer wird mit &e4 mB Antimaterie&r zum &5Drachenei&r.",
              "",
              "Dracheneier brauchst du für Rezepte von &5Draconic Evolution&r und für die Heiße Zentrifuge von &6Productive Bees&r. Wer nicht auf den nächsten Drachen warten will, brütet hier eins aus.",
          ],
          tasks=[task_item("minecraft:dragon_egg", 1)],
          rewards=[reward_item("minecraft:egg", 16), reward_xp(15)],
          deps=["nucleosynthesizer"], icon="minecraft:dragon_egg", optional=True),

    quest("grav_module", 7.5, 17.5, "&5Flieg mit Gravitationsmodulation",
          subtitle="Freier Flug in der MekaSuit.",
          description=[
              "Oben Atomlegierung, &6Netherstern&r, Atomlegierung, Mitte &6Ultimativer Induktionsanbieter&r, Basismodul, Ultimativer Induktionsanbieter, unten drei &5Antimaterie-Pellets&r.",
              "",
              "In der MekaSuit lässt es dich fliegen wie im Kreativmodus. Laut Config kostet das &d400 FE/t&r, solange du fliegst. Das Jetpack-Modul hat damit ausgedient.",
          ],
          tasks=[task_item("mekanism:module_gravitational_modulating_unit", 1)],
          rewards=[reward_item("mekanism:alloy_atomic", 4), reward_xp(20)],
          deps=["pellet"], icon="mekanism:module_gravitational_modulating_unit", optional=True, section="use"),

    quest("teleport_module", 10, 17.5, "&5Spring mit dem Meka-Werkzeug",
          subtitle="Das Teleportationsmodul.",
          description=[
              "Oben Atomlegierung, &6Teleportationskern&r, Atomlegierung, Mitte Atomlegierung, Basismodul, Atomlegierung, unten drei &5Antimaterie-Pellets&r.",
              "",
              "Im Meka-Werkzeug bringt dich ein Rechtsklick auf den Block, auf den du schaust, laut Config bis &e100 Blöcke&r weit. Quer durch die Fabrikhalle, über Schluchten, auf Dächer.",
          ],
          tasks=[task_item("mekanism:module_teleportation_unit", 1)],
          rewards=[reward_item("mekanism:teleportation_core", 2), reward_xp(15)],
          deps=["pellet"], icon="mekanism:module_teleportation_unit", optional=True, section="use"),

    quest("elytra_module", 12.5, 17.5, "&5Bau Flügel in die MekaSuit",
          subtitle="Die Elytra-Einheit.",
          description=[
              "&6HDPE Verstärkte Elytra:&r oben HDPE, Atomlegierung, HDPE, Mitte HDPE, eine &6Elytra&r aus der Endstadt, HDPE, unten zwei HDPE in die Ecken. Dann das Modul: Verstärkte Legierung um die HDPE-Elytra und das Basismodul, unten Polonium, ein &5Antimaterie-Pellet&r, Polonium.",
              "",
              "Die MekaSuit gleitet dann wie mit Elytra, ohne dass du den Brustplatz hergibst. Laut Config kostet das 12 800 FE pro Sekunde Flug.",
          ],
          tasks=[task_item("mekanism:module_elytra_unit", 1)],
          rewards=[reward_item("mekanism:hdpe_sheet", 16), reward_xp(15)],
          deps=["pellet"], icon="mekanism:module_elytra_unit", optional=True, section="use"),

    quest("replicator", 5, 17.5, "&3Bau einen Replikator",
          subtitle="Mekanism MoreMachine kopiert Dinge.",
          description=[
              "Eine &6UU-Materie&r, &6Atomlegierung&r, 2 &6Ultimative Schaltkreise&r und ein &6Stahlgehäuse&r. Es gibt ihn für Gegenstände, Flüssigkeiten und Chemikalien.",
              "",
              "&eRezept auf Kronwerke:&r Der Gegenstands-Replikator kopiert nur &eSteine&r und &eErze&r (je 1 mB), &eStämme&r (4 mB), &eBretter&r (1 mB) und &eEisen-, Kupfer- und Goldbarren&r (je 5 mB). Der Chemikalien-Replikator kopiert nichts.",
              "",
              "Der &3Große Kernsynthesizer&r aus MoreMachine ist auch offen, er braucht zwei Antimaterie-Pellets und einen Robit.",
          ],
          tasks=[task_item("mekmm:replicator", 1)],
          rewards=[reward_xp(15)],
          deps=["uu"], icon="mekmm:replicator", optional=True),

    # ---- Die Millionen -----------------------------------------------------------------------
    quest("mega_16m", 0, 21, "&bBau eine 16M-Komponente",
          subtitle="Speicher braucht Erwachtes Draconium.",
          description=[
              "&eRezept auf Kronwerke:&r 3 &64M-Komponenten&r, oben ein &6Akkumulationsprozessor&r, &6Enderperlenstaub&r in den Ecken, in der Mitte ein &5Erwachtes Draconiumnugget&r.",
              "",
              "64M und 256M bauen genauso auf der vorigen auf, mit Materiebällen in den Ecken und wieder einem Erwachten Nugget. Die Zelle craftest du aus Komponente und MEGA-Gehäuse.",
          ],
          tasks=[task_item("megacells:cell_component_16m", 1)],
          rewards=[reward_item("megacells:accumulation_processor", 4), reward_xp(10)],
          deps=["welcome"], icon="megacells:cell_component_16m"),

    quest("mega_256m", 2.5, 21, "&bBau eine 256M-Zelle",
          subtitle="Für den Rest der Season genug Platz.",
          description=[
              "Eine &6256M-Komponente&r braucht drei 64M, jede davon drei 16M. Zusammen 13 Erwachte Nuggets und 27 4M-Komponenten.",
              "",
              "Rechne vorher nach. Ein Laufwerk voller 16M-Zellen trägt schon sehr viel.",
          ],
          tasks=[task_item("megacells:item_storage_cell_256m", 1)],
          rewards=[reward_xp(15)],
          deps=["mega_16m"], icon="megacells:item_storage_cell_256m", optional=True),

    quest("bulk", 5, 21, "&bBau eine Bulk-Zelle",
          subtitle="Eine Sorte, so viel du willst.",
          description=[
              "&eRezept auf Kronwerke:&r Bulk-Komponente aus einer &61M-Komponente&r, einer &6Räumlichen Komponente 16³&r, 2 &6Akkumulationsprozessoren&r, &6Himmelssteinstaub&r und einem &5Erwachten Nugget&r. Die Zelle: Vibrierendes Quarzglas, Himmelssteinstaub, 3 Netheritbarren.",
              "",
              "Sie speichert eine einzige Sorte, davon fast beliebig viel. Die &6Komprimierungskarte&r rechnet zwischen Barren, Blöcken und Nuggets um.",
          ],
          tasks=[task_item("megacells:bulk_item_cell", 1)],
          rewards=[reward_item("ae2:sky_dust", 16), reward_xp(10)],
          deps=["mega_16m"], icon="megacells:bulk_item_cell", optional=True),

    quest("quantum", 7.5, 21, "&dBau den Quantencomputer",
          subtitle="Advanced AE für riesige Bestellungen.",
          description=[
              "Eine Crafting-CPU als Multiblock, auf diesem Server höchstens &e7 mal 7 mal 7&r. Außen &6Quantencomputer-Strukturglas&r, innen &6Kern&r, Einheiten, Speicher, Beschleuniger.",
              "",
              "Jeder Beschleuniger bringt 8 Threads. Ein Multi-Threader vervierfacht sie, ein Datenverschränker den Speicher, je einer pro Computer. Die Teile brauchen Singularitäten aus der Reaktionskammer von Advanced AE.",
          ],
          tasks=[task_item("advanced_ae:quantum_core", 1), task_item("advanced_ae:quantum_structure", 16)],
          rewards=[reward_item("ae2:singularity", 4), reward_xp(15)],
          deps=["mega_16m"], icon="advanced_ae:quantum_core", optional=True),
]

images = [
    head("title", "Mekanism: Antimaterie", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("fuel", "Brennstoff", 7.5, -1.3, colour="nature"),
    head("waste", "Atommüll", 0, 5.6, colour="nature"),
    head("sps", "Das SPS", 0, 11.0, colour="magic"),
    head("use", "Was Antimaterie kann", 0, 16.0, colour="end"),
    head("millions", "Die Millionen", 0, 19.5, colour="water"),
]

chapter(C, "Mekanism: Antimaterie", "mekanism:pellet_antimatter", "tech", quests, shape="square",
        order=43, stage=5,
        subtitle=["Stufe 5: Brennstoff, Spaltreaktor, Polonium und Plutonium, das SPS, Antimaterie und die Millionen im ME-Netz."],
        images=images)
