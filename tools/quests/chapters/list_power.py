"""Checklist chapter: every way to make power in the pack (FE, Create SU, Mekanism Joules,
PneumaticCraft air, Botania mana where it converts), one line per generator, grouped by the
stage it opens in, plus the cables, cells and wireless layer. Stage 1 generators are item tasks,
everything later is a checkmark that names the block. Numbers come from the server configs
(powah.json5, Mekanism/*.toml, create-server.toml, createaddition-common.toml,
immersiveengineering-server.toml, oritech-common.toml, justdirethings-server.toml,
fluxnetworks-server.toml, pipez-server.toml, enderio/machines-common.toml,
industrialforegoing/machine-generator.toml, productivebees-server.toml, MekanismMoreMachine,
brandon3055/DraconicEvolution.cfg) and from the jars (NuclearCraft lang, Create and IE classes).
Mekanism values are given in FE (1 FE = 2.5 J)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner)

C = "list_power"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def check(name, x, y, title, subtitle, description, icon, deps, xp=2):
    """One checklist line: a checkmark, a stage 1 stand-in icon, a little xp."""
    return quest(name, x, y, title, [task_checkmark("Abgehakt")], subtitle=subtitle,
                 description=description, rewards=[reward_xp(xp)], deps=deps, icon=icon)


def have(name, x, y, title, subtitle, description, item, count, deps, rewards):
    """A stage 1 generator the player can actually hand in."""
    return quest(name, x, y, title, [task_item(item, count)], subtitle=subtitle,
                 description=description, rewards=rewards, deps=deps, icon=item)


# Band rows: stage 1 at Y1, stage 2 at Y2 and Y2 + 2, and so on.
Y1, Y2, Y3, Y4, Y5 = 3.5, 7.5, 13.5, 19.5, 23.5
X = [3, 5.5, 8, 10.5, 13, 15.5, 18, 20.5, 23]

quests = [
    # ---- Einheiten --------------------------------------------------------------------
    quest("units", 0, 0, "&6&lLies die Einheiten einmal",
          subtitle="FE, SU, Joule, bar und Mana, und wie sie zusammenhängen.",
          description=[
              "Fast alle Technikmods reden &dFE&r (Forge Energy). Was Ender IO &dµI&r nennt, Immersive Engineering &dIF&r oder Flux und Draconic &dOP&r, ist dasselbe, eins zu eins. Ein Kabel von Mod A versorgt eine Maschine von Mod B.",
              "",
              "&eMekanism&r rechnet in &dJoule&r: &e1 FE = 2,5 J&r. Alle Mekanism-Zahlen in diesem Kapitel sind schon in FE umgerechnet. &eCreate&r hat keinen Strom, sondern Rotation: &dRPM&r ist die Drehzahl, &dSU&r die Belastbarkeit. Alternator und Elektromotor übersetzen zwischen SU und FE.",
              "",
              "&ePneumaticCraft&r arbeitet mit Druckluft in &dbar&r und mL, Dynamo und Flux-Kompressor übersetzen. &eBotania&r-Mana wird im Manaflussfeld zu FE (&e1 Mana = 10 FE&r), &eNature's Aura&r kann Aura zu FE machen (20 Aura = 1 FE).",
              "",
              "Jede Zeile hier: Mod, Generator, Brennstoff, FE pro Tick, Puffer, und ab welcher Stufe. Die &eWelche Quelle wann&r-Quest am Anfang jeder Stufe sagt dir, was sich lohnt.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(3)],
          icon="create:stressometer", size=2.0, shape="hexagon"),

    # ---- Stufe 1: Rotation ---------------------------------------------------------------
    quest("s1_choice", 0, Y1, "&e&lStufe 1: Welche Quelle wann",
          subtitle="Noch kein Strom, nur Drehung.",
          description=[
              "In Stufe 1 gibt es &ckeinen FE-Generator&r. Mekanism, Immersive Engineering, Powah und alle anderen Strommods sind zu, das Manaflussfeld von Botania braucht Manastahl aus Stufe 2. Was läuft, läuft mit &6Rotation&r von Create.",
              "",
              "&e1. Wasserräder:&r acht Bretter um eine Welle, 256 SU pro Rad, beliebig viele hintereinander an einem Bach. Billig, sofort, kein Brennstoff.",
              "&e2. Windmühle:&r ein Windmühlenlager und Segel, bis 2 048 SU mit 32 Segeln. Braucht Platz, bringt dafür mehr als acht Räder.",
              "&e3. Starbuncle-Rad:&r für Ars-Spieler, 256 SU ohne Wasser und ohne Wind, nur ein Starbuncle muss hinein.",
              "",
              "Was ihr braucht: Presse 8 SU pro RPM, Mahlstein und Mixer 4, Lüfter 2. Zwei Wasserräder tragen eine Presse bei 32 RPM, siehe Kapitel &6Create&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("create:andesite_alloy", 4), reward_xp(3)],
          deps=["units"], icon="create:water_wheel", size=1.5, shape="diamond"),

    have("water_wheel", X[0], Y1, "&6Bau ein Wasserrad",
         "Create, 8 RPM, 256 SU, braucht fließendes Wasser.",
         [
             "&eRezept:&r acht &6Bretter&r um eine &6Welle&r. Stell das Rad so, dass Wasser an seinen Schaufeln vorbeifließt, die Welle zeigt zur Seite.",
             "",
             "&eCreate, Wasserrad:&r Brennstoff keiner, &d8 RPM&r, &d256 SU&r, kein Puffer. Mehrere Räder auf einer Welle addieren die SU, nicht die Drehzahl. Offen ab Stufe 1.",
         ],
         "create:water_wheel", 1, ["s1_choice"],
         [reward_item("minecraft:oak_log", 8), reward_table("s1_common")]),

    have("large_wheel", X[1], Y1, "&6Bau ein großes Wasserrad",
         "Create, 4 RPM, 512 SU, drei Blöcke groß.",
         [
             "&eRezept:&r acht &6Bretter&r um ein fertiges &6Wasserrad&r. Es ist 3 x 3 Blöcke groß und will Wasser an seinem ganzen Rand.",
             "",
             "&eCreate, Großes Wasserrad:&r Brennstoff keiner, &d4 RPM&r, &d512 SU&r. Langsam, aber doppelt so stark wie das kleine, und ein Zahnradpaar macht aus 4 RPM wieder 8.",
         ],
         "create:large_water_wheel", 1, ["s1_choice"],
         [reward_item("minecraft:oak_log", 8), reward_xp(2)]),

    have("windmill", X[2], Y1, "&6Stell eine Windmühle auf",
         "Create, 1 RPM je acht Segel, 512 SU pro RPM.",
         [
             "&eRezept:&r eine &6Holzstufe&r auf einem &6Stein&r auf einer &6Welle&r ergibt das &6Windmühlenlager&r. Häng mindestens acht &6Segel&r (Wolle oder Create-Segel) daran und klick das Lager mit Rechtsklick an.",
             "",
             "&eCreate, Windmühle:&r Brennstoff keiner, &d1 RPM pro 8 Segel&r, &d512 SU pro RPM&r. 32 Segel geben 4 RPM und &d2 048 SU&r, 128 Segel 16 RPM und 8 192 SU. Sie dreht sich auch ohne Wind und Wetter, braucht nur freien Platz.",
         ],
         "create:windmill_bearing", 1, ["s1_choice"],
         [reward_item("minecraft:white_wool", 16), reward_xp(3)]),

    have("hand_crank", X[3], Y1, "&6Dreh eine Handkurbel",
         "Create, 32 RPM, 256 SU, solange du festhältst.",
         [
             "&eRezept:&r drei &6Bretter&r in einer Reihe, eine &6Andesitlegierung&r rechts darunter. Rechtsklick gedrückt halten, und die Welle dreht sich.",
             "",
             "&eCreate, Handkurbel:&r Brennstoff deine Zeit, &d32 RPM&r, &d256 SU&r. Für die erste Presse und den Mahlstein, bevor das Wasserrad steht. Das &6Kupferventilrad&r macht dasselbe mit 8 SU pro RPM, nur langsamer.",
         ],
         "create:hand_crank", 1, ["s1_choice"],
         [reward_item("create:andesite_alloy", 2)]),

    have("starbuncle_wheel", X[4], Y1, "&dSetz ein Starbuncle-Rad",
         "Ars Creo, 16 RPM, 256 SU, ein Starbuncle läuft im Rad.",
         [
             "&eRezept:&r ein &6Starbuncle-Amulett&r und ein &6Wasserrad&r, formlos. Das Starbuncle aus dem Amulett steckt danach im Rad, setz es einfach an eine Welle.",
             "",
             "&eArs Creo, Starbuncle-Rad:&r Brennstoff keiner, &d16 RPM&r, &d16 SU pro RPM&r, also &d256 SU&r. Ein &6Goldblock&r direkt vor dem Rad treibt es auf 24 RPM und 384 SU. Es läuft im Keller, in der Wüste, überall.",
         ],
         "ars_creo:starbuncle_wheel", 1, ["s1_choice"],
         [reward_item("ars_nouveau:source_gem", 4), reward_xp(3)]),

    # ---- Stufe 2 ---------------------------------------------------------------------------
    quest("s2_choice", 0, Y2, "&e&lStufe 2: Welche Quelle wann",
          subtitle="Der erste Strom. Drei Wege, die sich lohnen.",
          description=[
              "Mit dem Nether öffnen Mekanism, Immersive Engineering, Create-Messing, Just Dire Things und Productive Bees. Ab jetzt gibt es FE.",
              "",
              "&e1. Wärmegenerator von Mekanism in Lava:&r Eisen, Osmium, Kupfer, Bretter. 80 FE/t mit Kohle, dazu 12 FE/t je Lavaseite, ohne dass die Lava weniger wird. Billig und sofort, genug für drei bis vier Grundmaschinen.",
              "&e2. Generator von Just Dire Things mit Primal Coal:&r 120 FE/t aus einem Stück, 1 Million FE Puffer, gibt 1 000 FE/t ab. Weniger Nachlegen als alles andere in dieser Stufe.",
              "&e3. Dampfkessel mit Alternator:&r Eine Dampfmaschine liefert 16 384 SU, ein Alternator macht daraus bei 256 RPM 360 FE/t. Wer schon einen Kessel für Messing hat, bekommt den Strom fast geschenkt.",
              "",
              "Für richtig viel: der &6Gasgenerator&r mit Ethen aus dem Druckreaktor, bis 72 000 FE/t. Das ist ein Projekt für das Ende der Stufe.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(3)],
          deps=["s1_choice"], icon="minecraft:furnace", size=1.5, shape="diamond"),

    check("steam_engine", X[0], Y2, "&6Heiz einen Dampfkessel an",
          "Create, Dampfmaschine, 64 RPM und 16 384 SU je Maschine.",
          [
              "&6Dampfmaschine&r an einen &6Flüssigkeitstank&r mit Wasser und &6Lohenbrennern&r darunter, eine Welle davor. Kesselstufe = das kleinste von Hitze, Wasser und Tankgröße.",
              "",
              "&eCreate, Dampfmaschine:&r Brennstoff alles, was ein Lohenbrenner frisst (Kohle, Holzkohle, Lohenkuchen, flüssiger Brennstoff mit dem Strohhalm aus Crafts & Additions). Voll versorgt &d64 RPM&r und &d16 384 SU&r pro Maschine, bis 18 Maschinen an einem Kessel. Ein Kessel ohne Brenner (passiv) gibt einer Maschine noch 16 RPM und 2 048 SU. Offen ab Stufe 2, siehe Kapitel &6Create: Messing&r.",
          ],
          "create:fluid_tank", ["s2_choice"], xp=3),

    check("diesel_engine", X[1], Y2, "&6Bau einen Dieselmotor",
          "Create Diesel Generators, 96 RPM, 4 096 bis 8 192 SU aus einem Block.",
          [
              "Pump &bBiodiesel&r, &bDiesel&r oder &bEthanol&r in den &6Dieselmotor&r, ein Eimer wird auf Kronwerke nicht angenommen. Er trinkt &e1 mB pro Sekunde&r, ein Eimer hält 16 Minuten.",
              "",
              "&eCreate Diesel Generators, Dieselmotor:&r Biodiesel &d96 RPM, 4 096 SU&r, Diesel 6 144 SU, Ethanol 2 048 SU. Der &6Große Dieselmotor&r ist stapelbar, 6 144 SU mit Biodiesel und 8 192 mit Diesel je Block. Der &6Riesen-Dieselmotor&r (224 RPM, bis 16 384 SU) kommt in Stufe 3. Offen ab Stufe 2, siehe Kapitel &6Create: Erweiterungen&r.",
          ],
          "minecraft:bucket", ["s2_choice"]),

    check("alternator", X[2], Y2, "&6Mach aus Rotation Strom",
          "Crafts & Additions, Alternator: 360 FE/t bei 256 RPM.",
          [
              "&eRezept auf Kronwerke:&r Der &6Alternator&r entsteht in den Handwerkseinheiten aus Kupferspulen, Eisenblechen, einem &6Einfachen Steuerschaltkreis&r und Andesitlegierung. Eine Welle hinein, ein Kabel oder eine Maschine daneben, fertig.",
              "",
              "&eCrafts & Additions, Alternator:&r Brennstoff Rotation. Bei 256 RPM zieht er &d16 384 SU&r und macht &d360 FE/t&r (480 mal 0,75 Wirkungsgrad), bei 64 RPM entsprechend 4 096 SU und 90 FE/t. Puffer 5 000 FE, Abgabe bis 5 000 FE/t. Der &6Elektromotor&r ist der Rückweg: bis 480 FE/t rein, bis 256 RPM und 16 384 SU raus. Offen ab Stufe 2.",
          ],
          "create:cogwheel", ["s2_choice"]),

    check("power_grid", X[3], Y2, "&6Wickle einen Power-Grid-Generator",
          "Power Grid, Volt und Ampere, per Adapter auch FE.",
          [
              "Kupplung, &6Induktionsrotor&r und &6Kollektor&r auf eine Welle, Wicklungen aus Kupferspulen daneben, einen kleinen Erregerstrom hinein. Die Ponder-Szenen (W) zeigen jeden Schritt.",
              "",
              "&ePower Grid, Generator:&r Brennstoff Rotation. Er rechnet nicht in FE, sondern in &dVolt und Ampere&r, Leistung = Spannung mal Strom, lange Drähte verlieren. Über den &6Adapter&r (Zinkblech, Kupferbleche, Legierung) versorgt er FE-Maschinen, und das &6Solarmodul&r von Power Grid liefert tagsüber Spannung ohne Welle. Offen ab Stufe 2, siehe Kapitel &6Create: Messing&r.",
          ],
          "create:copper_casing", ["s2_choice"]),

    check("mek_heat", X[4], Y2, "&6Stell einen Wärmegenerator in Lava",
          "Mekanism, 80 FE/t aus Brennstoff plus 12 FE/t je Lavaseite.",
          [
              "&eRezept:&r drei Eisen oben, Bretter links und rechts vom Osmiumbarren, unten Kupfer, Ofen, Kupfer. Leg Kohle hinein oder stell ihn in ein Lavabecken, am besten beides.",
              "",
              "&eMekanism, Wärmegenerator:&r Brennstoff alles Brennbare, &d80 FE/t&r aktiv. Jede angrenzende Lavaseite &d12 FE/t&r dazu, bis sieben Seiten, im Nether noch einmal 40 FE/t obendrauf. Ein Lavaeimer im Tank (24 000 mB) wird dagegen verbraucht. Puffer klein, Abgabe an alle Nachbarn. Offen ab Stufe 2, siehe Kapitel &6Mekanism&r.",
          ],
          "minecraft:lava_bucket", ["s2_choice"], xp=3),

    check("mek_solar_wind", X[5], Y2, "&6Bau Solar- und Windgenerator",
          "Mekanism, 20 FE/t Sonne, 24 bis 192 FE/t Wind.",
          [
              "&6Solargenerator:&r drei Solarmodule auf Infundierter Legierung, Eisen, Osmium und einem Energietablett. &6Windgenerator:&r Osmium, Legierung, zwei Energietabletts und ein Schaltkreis, braucht freien Himmel über sich.",
              "",
              "&eMekanism, Solargenerator:&r &d20 FE/t&r bei Tag und freiem Himmel, nachts und im Regen nichts. &eWindgenerator:&r &d24 FE/t&r unten ab Y 24, &d192 FE/t&r ganz oben, steigt mit der Höhe. Beide ohne Brennstoff. Offen ab Stufe 2. Der &6Erweiterte Solargenerator&r mit 120 FE/t kommt in Stufe 3.",
          ],
          "minecraft:daylight_detector", ["s2_choice"]),

    check("mek_bio", X[6], Y2, "&6Verfeuere Biobrennstoff",
          "Mekanism, Biogenerator, 140 FE/t aus Pflanzenresten.",
          [
              "&eRezept:&r Redstone, Legierung, Redstone oben, Biobrennstoff, Schaltkreis, Biobrennstoff in der Mitte, Eisen, Legierung, Eisen unten. Der &6Zerkleinerer&r macht aus Samen, Setzlingen und Pflanzen &6Biobrennstoff&r.",
              "",
              "&eMekanism, Biogenerator:&r Brennstoff Biobrennstoff (Tank 24 000 mB), &d140 FE/t&r. Eine Weizenfarm mit Erntemaschine davor, und er läuft ohne Kohle. Offen ab Stufe 2.",
          ],
          "minecraft:wheat_seeds", ["s2_choice"]),

    check("mek_gas", X[7], Y2, "&6Verbrenne Wasserstoff oder Ethen",
          "Mekanism, Gasgenerator, 80 FE/t bis 72 000 FE/t.",
          [
              "&eRezept:&r Osmium in die Ecken, Legierung oben und unten, zwei Stahlgehäuse an den Seiten, ein &6Elektrolytischer Kern&r in der Mitte. Gas kommt per Druckrohr oder Tank hinein.",
              "",
              "&eMekanism, Gasgenerator:&r &bWasserstoff&r aus dem Elektrolyseur gibt &d80 FE/t&r je mB. &bEthen&r aus dem Druckreaktor (Biobrennstoff, Wasser, Wasserstoff) gibt &d11 280 FE je mB&r. Wie viel er pro Tick verbrennt, hängt davon ab, wie voll der Tank (18 000 mB) ist: randvoll bis &d72 000 FE/t&r bei 6,4 mB Ethen pro Tick. Offen ab Stufe 2. Die stärkste Quelle vor Stufe 3, aber eine ganze Produktionskette.",
          ],
          "minecraft:glass_bottle", ["s2_choice"], xp=3),

    check("ie_dynamo", X[8], Y2, "&6Häng eine Windmühle an den Dynamo",
          "Immersive Engineering, Dynamo mit Windmühle oder Wasserrad.",
          [
              "Zuerst den &6Kinetischen Dynamo&r setzen, dann die &6Windmühle&r (acht Blätter um Eisen) oder das &6Wasserrad&r an seine Wellenseite. Strom über einen LV-Anschluss am Dynamo.",
              "",
              "&eImmersive Engineering, Dynamo:&r Brennstoff Wind oder Wasser. Die Windmühle zählt die freien Blöcke in einem 9 x 9 x 7 Raum vor sich: völlig frei und ohne Segel etwa &d17 FE/t&r, mit acht &6Segeln&r rund &d50 FE/t&r, im Gewitter etwa das Doppelte. Bis drei Wasserräder treiben einen Dynamo, je mehr fließendes Wasser, desto mehr. Offen ab Stufe 2, siehe Kapitel &6Immersive Engineering&r.",
          ],
          "create:white_sail", ["s2_choice"]),

    check("ie_thermo", X[0], Y2 + 2, "&6Spann Lava gegen Wasser",
          "Immersive Engineering, Thermoelektrischer Generator und Blitzableiter.",
          [
              "&6Thermoelektrischer Generator:&r drei Stahl oben, LV-Spule zwischen zwei Constantanblechen, unten drei Constantanbleche. Heiß auf die eine Seite, kalt gegenüber, Strom an jeder freien Seite.",
              "",
              "&eIE, Thermoelektrisch:&r Brennstoff keiner. Je gegenüberliegendem Paar Wurzel aus dem Temperaturunterschied halbiert: &bLava&r (1 300 K) gegen &bWasser&r (300 K) gibt &d15 FE/t&r, mit drei Paaren &d45 FE/t&r. Eis und Packeis sind kälter als Wasser, ein Uranblock heißer als Lava.",
              "",
              "&eIE, Blitzableiter:&r ein Sockel aus Blitzableiterblöcken mit einer Stange aus Stahlzäunen obendrauf. Ein Einschlag bringt &d16 000 000 FE&r in den Sockel, abgegeben nach und nach über die Anschlüsse. Nur bei Gewitter, dafür umsonst. Offen ab Stufe 2.",
          ],
          "minecraft:lightning_rod", ["s2_choice"]),

    check("ie_wires", X[1], Y2 + 2, "&6Zieh Draht und stell Kondensatoren",
          "Immersive Engineering: Kupfer 2 048, Elektrum 8 192, HV 32 768 FE/t.",
          [
              "&6Drahtanschluss&r an beide Enden, mit der &6Drahtspule&r in der Hand erst den einen, dann den anderen anklicken. &6Kondensatoren&r speichern und geben je Seite ab, Seiten stellst du mit dem Hammer ein.",
              "",
              "&eIE, Leitungen:&r Kupferdraht &d2 048 FE/t&r, 16 Blöcke weit, Anschluss 256 FE/t je Seite. Elektrum 8 192 FE/t, Anschluss 1 024. HV-Draht 32 768 FE/t, 32 Blöcke, Anschluss 4 096. Je länger, desto mehr Verlust (1,25 Prozent je 16 Blöcke Kupfer).",
              "",
              "&eIE, Kondensatoren:&r LV &d100 000 FE&r und 256 FE/t je Seite, MV 1 Million und 1 024, HV 4 Millionen und 4 096. Alles offen ab Stufe 2.",
          ],
          "minecraft:chain", ["s2_choice"]),

    check("jdt_gens", X[2], Y2 + 2, "&6Heiz mit Primal Coal",
          "Just Dire Things: 60 bis 240 FE/t fest, 5 000 FE/t flüssig.",
          [
              "&eRezept auf Kronwerke:&r Der &6Generator&r ist Ferricore in den Ecken, Redstone oben und unten, Kohle links und rechts, ein &6Einfacher Steuerschaltkreis&r in der Mitte. Der &6Brennstoffgenerator&r hat dort Blazegold, Redstone, Eimer und einen Schmelzofen. &6Taschengenerator&r: Rechtsklick, Kohle rein, lädt alles in deinem Inventar.",
              "",
              "&eJust Dire Things, Generator:&r 15 FE je Brenntick, vierfache Brenngeschwindigkeit. Kohle &d60 FE/t&r (24 000 FE), Primal Coal &d120 FE/t&r (72 000), Blaze Ember &d240 FE/t&r (216 000). Puffer &d1 Million FE&r, Abgabe 1 000 FE/t an alle Nachbarn.",
              "",
              "&eBrennstoffgenerator:&r flüssiger Brennstoff aus Blaze Ember, &d450 FE je mB&r, also 450 000 FE pro Eimer, Abgabe &d5 000 FE/t&r, Puffer 5 Millionen. Der &6Energiesender&r schickt 1 000 FE/t drahtlos, mit 1 Prozent Verlust je Block. Offen ab Stufe 2, siehe Kapitel &6Just Dire Things&r.",
          ],
          "minecraft:blast_furnace", ["s2_choice"], xp=3),

    check("honey", X[3], Y2 + 2, "&6Verbrenne Honig",
          "Productive Bees, Honiggenerator, 60 FE/t aus 2 mB Honig pro Tick.",
          [
              "&eRezept:&r ein &6Honigeimer&r oben, ein &6Ofen&r in der Mitte, sieben Eisenbarren. Honig kommt per Rohr, Flasche, Eimer oder Honigblock hinein.",
              "",
              "&eProductive Bees, Honiggenerator:&r Brennstoff Honig, &d2 mB pro Tick&r für &d60 FE/t&r, ein Eimer ist 30 000 FE. Ein paar Bienenstöcke mit Zentrifuge davor, und die Zuchtkammer (50 FE/t) versorgt sich selbst. Offen ab Stufe 2, siehe Kapitel &6Productive Bees&r.",
          ],
          "minecraft:honey_bottle", ["s2_choice"]),

    check("fluxfield", X[4], Y2 + 2, "&dMach aus Mana Strom",
          "Botania, Manaflussfeld, 1 Mana = 10 FE, bis 1 600 FE/t.",
          [
              "&eRezept:&r Lebestein in die Ecken, Redstoneblöcke an die Seiten, ein &6Manastahlbarren&r in die Mitte. Schieß Manastöße aus einem Verbreiter hinein, der Strom geht an alle Nachbarn.",
              "",
              "&eBotania, Manaflussfeld:&r Brennstoff Mana, &d1 Mana = 10 FE&r. Puffer 1 280 Mana, also 12 800 FE, Abgabe bis &d1 600 FE/t&r. Ein Becken mit 1 Million Mana sind 10 Millionen FE. Der Block selbst ist frei, der Manastahl im Rezept kommt mit Stufe 2. Einen Rückweg von FE zu Mana gibt es nicht.",
          ],
          "botania:livingrock", ["s2_choice"], xp=3),

    check("mek_storage", X[5], Y2 + 2, "&6Leg Universalkabel und Energie-Würfel",
          "Mekanism: 3 200 FE/t im Kabel, 1,6 Millionen FE im Würfel.",
          [
              "Zwei Stahlbarren mit Redstone dazwischen geben acht &6Einfache Universalkabel&r. Der &6Einfache Energie-Würfel&r: zwei Energietabletts, zwei Eisen, vier Redstone um ein Stahlgehäuse.",
              "",
              "&eMekanism, Einfaches Universalkabel:&r &d3 200 FE/t&r. Fortgeschritten 51 200 FE/t (Stufe 3), Elite 409 600 und Ultimativ 3 276 800 FE/t (Stufe 4). Kabel verbinden sich mit jedem FE-Gerät im Pack.",
              "",
              "&eMekanism, Einfacher Energie-Würfel:&r &d1,6 Millionen FE&r, Abgabe 1 600 FE/t. Fortgeschritten 6,4 Millionen und 6 400 FE/t (Stufe 3), Elite 25,6 Millionen und 25 600, Ultimativ 102,4 Millionen und 102 400 FE/t (Stufe 4). Die &6Induktionsmatrix&r (Gehäuse, Zellen, Anschlüsse) speichert schon mit einfachen Zellen &d3,2 Milliarden FE&r je Zelle, der einfache Anschluss schafft 102 400 FE/t. Kommt erst in Stufe 4: der Anschluss braucht Elite-Schaltkreise, die Zellen Lithiumstaub aus dem Kristallisator, siehe Kapitel &6Mekanism: Elite&r.",
          ],
          "minecraft:redstone_block", ["s2_choice"], xp=3),

    check("pipez_pipe", X[6], Y2 + 2, "&6Leg ein Stromrohr von Pipez",
          "Pipez, Energierohr, 256 FE/t ohne Upgrade, bis 131 072 mit.",
          [
              "&eRezept:&r sechs Eisenbarren oben und unten, zwei Redstoneblöcke links und rechts, ein Redstone in der Mitte. Die ziehende Seite kommt an den Generator oder Speicher, Rechtsklick mit dem Schraubenschlüssel öffnet das Menü.",
              "",
              "&ePipez, Energierohr:&r &d256 FE/t&r ohne Upgrade, Basis-Upgrade 1 024, Verbessert 8 192 (beide Stufe 2), Fortgeschritten 32 768 (Stufe 3), Ultimativ 131 072 FE/t (Stufe 4). Ein Rohr für jede Mod, siehe Kapitel &6Rohre und Router&r.",
          ],
          "minecraft:iron_bars", ["s2_choice"]),

    check("accumulator", X[7], Y2 + 2, "&6Speichere Rotation und FE bei Create",
          "Create Connected, Power Grid und Crafts & Additions: Batterien und Netzanschlüsse.",
          [
              "Die &6Kinetische Batterie&r (Präzisionsgetriebe, Messingrahmen, Eisenbleche, Redstone) nimmt Rotation auf und gibt sie später wieder ab. Die &6Batterie&r von Power Grid speichert Strom im Power-Grid-Netz, die &6Tragbare Batterie&r ist dasselbe für die Tasche.",
              "",
              "&eCrafts & Additions, Netzanschlüsse:&r der kleine &6Anschluss&r trägt &d1 000 FE/t&r über 16 Blöcke Draht, der &6Große Anschluss&r &d5 000 FE/t&r über 32 Blöcke, mit einer Kupferspule in der Hand verbindest du zwei. Der &6Modulare Akkumulator&r (2 Millionen FE je Block, bis 3 x 3 x 5 Blöcke, also 90 Millionen, je 5 000 FE/t rein und raus) kommt in Stufe 3. Offen ab Stufe 2.",
          ],
          "create:gearbox", ["s2_choice"]),

    # ---- Stufe 3 ---------------------------------------------------------------------------
    quest("s3_choice", 0, Y3, "&e&lStufe 3: Welche Quelle wann",
          subtitle="Das Stahlwerk braucht Kraftwerke.",
          description=[
              "Stufe 3 öffnet Powah, Oritech, Ender IO, Industrial Foregoing, Flux Networks, die großen IE-Maschinen und PneumaticCraft mit Strom. Die Erzverdreifachung und die Fabriken fressen tausende FE pro Tick.",
              "",
              "&e1. Powah-Reaktor:&r 36 Reaktorblöcke, Uraninit als Brennstoff, Wasser und Eis als Kühlung. Schon der Starter macht 250 FE/t, der Blazing-Reaktor &d10 000 FE/t&r, Spirited 100 000. Das beste Verhältnis von Aufwand zu Strom in dieser Stufe.",
              "&e2. Blazing Furnator:&r 800 FE/t aus Kohle, 48 000 FE je Stück, ohne Kühlung und ohne Erz. Eine Baumfarm mit Holzkohle hängt dran, fertig.",
              "&e3. IE-Dieselgenerator:&r 4 096 FE/t aus Biodiesel, wenn die Raffinerie ohnehin läuft. Ein großer Multiblock, aber nur einer.",
              "",
              "Dazu &6Flux Networks&r als Verteilung: ein Controller, Plugs an den Generatoren, Points an den Maschinen, kein Kabel mehr quer durch die Basis.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:coal_block", 4), reward_xp(3)],
          deps=["s2_choice"], icon="minecraft:redstone_torch", size=1.5, shape="diamond"),

    check("powah_fuel", X[0], Y3, "&bBau Furnator und Magmator",
          "Powah, 20 bis 8 000 FE/t je nach Stufe, 30 FE je Brenntick.",
          [
              "&6Furnator&r (Starter): drei Paste oben, zwei Tiny-Kondensatoren um ein Dielectric Casing, unten Paste, Ofen, Paste. Der &6Magmator&r hat einen Eimer statt des Ofens und trinkt Lava.",
              "",
              "&ePowah, Furnator und Magmator:&r Brennstoff alles Brennbare oder heiße Flüssigkeit, &d30 FE je Brenntick&r, eine Kohle also 48 000 FE in jeder Stufe. Erzeugung Starter &d20 FE/t&r, Basic 80, Hardened 200, Blazing 800, Niotic 2 000, Spirited 8 000. Puffer 20 000 bis 8 Millionen, Abgabe das Vierfache der Erzeugung. Offen ab Stufe 3, siehe Kapitel &6Powah&r. Nitro (40 000 FE/t) kommt in Stufe 4.",
          ],
          "minecraft:furnace", ["s3_choice"], xp=3),

    check("powah_passive", X[1], Y3, "&bLeg Solarmodule und Thermogeneratoren",
          "Powah, 20 bis 800 FE/t ohne Brennstoff.",
          [
              "Das &6Solar Panel&r braucht freien Himmel, der &6Thermo Generator&r steht auf Lava oder Magma und bekommt Wasser als Kühlmittel in den Tank. JEI zeigt unter Heat Sources, was als Wärmequelle zählt.",
              "",
              "&ePowah, Solar Panel und Thermo Generator:&r beide Starter &d20 FE/t&r, Basic 60, Hardened 100, Blazing 200, Niotic 400, Spirited 800. Das Solarmodul nur bei Tag, der Thermogenerator rund um die Uhr. Mit einer &6Lens of Ender&r sieht das Solarmodul durch Blöcke über sich. Offen ab Stufe 3.",
          ],
          "minecraft:daylight_detector", ["s3_choice"]),

    check("powah_reactor", X[2], Y3, "&bZünde den Powah-Reaktor",
          "Powah, 250 bis 100 000 FE/t aus Uraninit.",
          [
              "Nimm &636 Reaktorblöcke&r einer Stufe in die Hand und setz einen ab, der 3 x 3 x 4 Reaktor baut sich selbst. &6Uraninit&r hinein, Wasser und Eis oder Trockeneis zum Kühlen, Kohle und Redstone in die Nebenslots für mehr Leistung.",
              "",
              "&ePowah, Reaktor:&r Brennstoff Uraninit (Erz unter Y 64, Mekanism-Uran in der Kugel). Erzeugung Starter &d250 FE/t&r, Basic 1 000, Hardened 2 500, Blazing 10 000, Niotic 25 000, Spirited 100 000. Puffer 250 000 bis 100 Millionen. Offen ab Stufe 3, Nitro (500 000 FE/t) in Stufe 4.",
          ],
          "minecraft:water_bucket", ["s3_choice"], xp=3),

    check("powah_storage", X[3], Y3, "&bVerkabel mit Powah",
          "Powah: Kabel 500 bis 200 000 FE/t, Zellen 1 bis 400 Millionen FE.",
          [
              "Sechs Dielectric Rods, zwei Eisennuggets und ein Tiny-Kondensator geben zwölf &6Energy Cables&r. Die &6Energy Cell&r: Eisen in die Ecken, Kondensatoren an die Seiten, Casing in die Mitte. Seiten stellst du mit dem &6Wrench&r ein.",
              "",
              "&ePowah, Kabel:&r Starter &d500 FE/t&r, Basic 2 000, Hardened 5 000, Blazing 20 000, Niotic 50 000, Spirited 200 000. &eEnergy Cell:&r Starter &d1 Million FE&r, Basic 4, Hardened 10, Blazing 40, Niotic 100, Spirited 400 Millionen, Übertragung 1 000 bis 400 000 FE/t.",
              "",
              "&ePowah, drahtlos:&r &6Ender Cells&r teilen einen Speicher über Kanäle, egal wo sie stehen. Der &6Player Transmitter&r lädt mit einer Binding Card deine Werkzeuge in der Tasche, überall. Offen ab Stufe 3.",
          ],
          "minecraft:copper_block", ["s3_choice"]),

    check("mek_adv", X[4], Y3, "&5Rüste Mekanism auf Fortgeschritten",
          "Mekanism: 120 FE/t Solar, 51 200 FE/t Kabel, 6,4 Millionen FE Würfel.",
          [
              "Der &6Erweiterte Solargenerator&r: vier Solargeneratoren, Legierung, Schaltkreise und ein Eisenblock, drei Blöcke hoch. Fortgeschrittene Kabel und Würfel entstehen aus den einfachen mit Infundierter Legierung und Fortschrittlichen Schaltkreisen.",
              "",
              "&eMekanism, Erweiterter Solargenerator:&r &d120 FE/t&r bei Tag, sechsmal der kleine. &eFortgeschrittenes Universalkabel:&r &d51 200 FE/t&r. &eFortgeschrittener Energie-Würfel:&r &d6,4 Millionen FE&r, 6 400 FE/t. Fortgeschrittene Induktionszellen speichern 25,6 Milliarden FE je Zelle, der Anschluss schafft 819 200 FE/t. Wie die ganze Matrix erst ab Stufe 4.",
          ],
          "minecraft:iron_block", ["s3_choice"]),

    check("mek_turbine", X[5], Y3, "&5Bau die Industrieturbine",
          "Mekanism, Strom aus Dampf, wächst mit dem Reaktor.",
          [
              "Eine Hülle aus &6Turbinengehäuse&r (mindestens 5 x 5), innen Rotor mit Blättern, Rotationskomplex, Druckventile, darüber &6Elektromagnetische Spulen&r (eine je vier Blätter), Ventile in der Hülle für Dampf und Strom.",
              "",
              "&eMekanism, Industrieturbine:&r Brennstoff Dampf. Dampf kommt vom Thermoelektrischen Dampfkessel, aus Oritech über den Rotationskondensator, und ab Stufe 5 vom Spaltreaktor. Jeder Turbinenblock gibt 6,4 Millionen FE Puffer dazu, der Ausstoß hängt von Blättern, Spulen und Dampfmenge ab. Offen ab Stufe 3, siehe Kapitel &6Mekanism: Fortgeschritten&r.",
          ],
          "create:fluid_tank", ["s3_choice"]),

    check("oritech_gens", X[6], Y3, "&cStell die Oritech-Generatoren",
          "Oritech: 32 FE/t Basis, 64 Bio und Lava, 256 Brennstoff, 32 Solar.",
          [
              "&eRezept auf Kronwerke:&r Der &6Grundlegende Generator&r ist Nickel oben und an den Seiten, Kupfer in der Mitte, unten Spule, Andesitgehäuse, Spule, dazu Maschinenkerne um ihn herum. Bio-, Lava- und Brennstoffgenerator sind größere Multiblöcke mit Kernen.",
              "",
              "&eOritech, Generatoren:&r Grundlegender Generator &d32 FE/t&r aus allem Brennbaren, Puffer 50 000. &6Biogenerator&r &d64 FE/t&r aus Biomasse, &6Lavagenerator&r &d64 FE/t&r aus Lava, &6Brennstoffgenerator&r &d256 FE/t&r aus Öl-Brennstoff, Puffer 100 000 bis 250 000. Das &6Große Solarmodul&r &d32 FE/t&r bei Tag. Mit dem Dampfkessel-Addon machen die Generatoren statt Strom Dampf, den die &6Dampfmaschine&r eins zu eins zurück in FE wandelt. Offen ab Stufe 3, siehe Kapitel &6Oritech&r.",
          ],
          "minecraft:gold_block", ["s3_choice"]),

    check("oritech_reactor", X[7], Y3, "&cBau den Oritech-Reaktor",
          "Oritech, Kernreaktor, bis 25 000 FE/t je Energieanschluss.",
          [
              "Eine Hülle aus &6Reaktorwänden&r (bis 64 Blöcke Kantenlänge), innen &6Brennstäbe&r, &6Wärmerohre&r, &6Absorber&r und &6Lüfter&r, ein &6Controller&r und Anschlüsse für Brennstoff und Strom in der Wand.",
              "",
              "&eOritech, Reaktor:&r Brennstoff Uranstäbe, &d64 FE je Reaktorpuls&r, Puffer 50 Millionen, Abgabe &d25 000 FE/t je Energieanschluss&r. Über 2 000 Hitze schmilzt er, der sichere Modus ist auf diesem Server &caus&r. &eSpeicher:&r der &6Kleine Energiespeicher&r fasst 1 Million FE (5 000 FE/t), der &6Große&r 20 Millionen (10 000 FE/t), Oritech-&6Energierohre&r verbinden alles. Offen ab Stufe 3.",
          ],
          "minecraft:tnt", ["s3_choice"]),

    check("enderio", X[0], Y3 + 2, "&5Bau den Stirling Generator",
          "Ender IO: 40 µI/t Stirling, 4 bis 64 µI/t Photovoltaik, Kondensatorbänke.",
          [
              "&6Stirling Generator:&r Zahnrad, Ofen, Zahnrad oben, Eisen, Gehäuse der Leere, Eisen in der Mitte, Obsidian, Tiefenschiefer, Obsidian unten. Ohne &6Kondensator&r im Slot läuft er nicht.",
              "",
              "&eEnder IO, Stirling Generator:&r Brennstoff alles Brennbare, &d40 µI/t&r mit dem einfachen Kondensator, bessere Kondensatoren holen mehr aus jedem Stück heraus, Puffer 64 000. µI ist FE. &ePhotovoltaik-Module:&r Energetisch &d4 µI/t&r, Pulsierend 16, Strahlend 64, nur bei Tag.",
              "",
              "&eKondensatorbänke:&r Einfach &d500 000 µI&r, Fortgeschritten 2 Millionen, Strahlend 4 Millionen, mehrere nebeneinander werden eine. &6Energieleitungen&r liegen mit Item- und Flüssigkeitsleitungen im selben Block. Offen ab Stufe 3, siehe Kapitel &6Ender IO&r.",
          ],
          "minecraft:obsidian", ["s3_choice"]),

    check("industrial", X[1], Y3 + 2, "&aHeiz den Primitiven Heizgenerator",
          "Industrial Foregoing: 30 FE/t aus Kohle, 160 FE/t aus Biokraftstoff.",
          [
              "&6Primitiver Heizgenerator:&r Bruchstein in die Ecken, Gold oben, Eisengitter an den Seiten, Ofen unten, das Pity-Maschinengehäuse in die Mitte. Der &6Biokraftstoffgenerator&r braucht Biokraftstoff aus dem Bioreaktor.",
              "",
              "&eIndustrial Foregoing, Primitiver Heizgenerator:&r Brennstoff alles Brennbare, &d30 FE/t&r, Puffer 100 000, Abgabe 1 000 FE/t. &eBiokraftstoffgenerator:&r &d160 FE/t&r aus Biokraftstoff (Tank 4 000 mB), Puffer 1 Million, hört auf, wenn er voll ist. Offen ab Stufe 3, siehe Kapitel &6Industrial Foregoing&r.",
          ],
          "minecraft:cobblestone", ["s3_choice"]),

    check("id_coal", X[2], Y3 + 2, "&aStell den Kohlegenerator",
          "Integrated Dynamics, 20 FE/t, dazu die Energiebatterie.",
          [
              "Eine &6Energiebatterie&r und ein &6Ofen&r formlos ergeben den &6Kohlegenerator&r. Kohle hinein, Strom an die Nachbarn oder ins Integrated-Netz.",
              "",
              "&eIntegrated Dynamics, Kohlegenerator:&r Brennstoff alles Brennbare, &d20 FE/t&r. Die &6Energiebatterie&r speichert &d1 Million FE&r und gibt mindestens 2 000 FE/t ab. Beides ist eher für das eigene Kabelnetz von Integrated Dynamics gedacht als für ein Kraftwerk. Offen ab Stufe 3.",
          ],
          "minecraft:coal", ["s3_choice"]),

    check("ie_diesel", X[3], Y3 + 2, "&6Form den Dieselgenerator",
          "Immersive Engineering, 4 096 FE/t aus Biodiesel.",
          [
              "13 Schwere Ingenieursbausteine, 9 Kühler, 4 Generatorblöcke, Stahlgerüste, Rohre und ein Redstone-Baustein, 3 x 3 x 5, geformt am mittleren Generatorblock. Brennstoff unten in die Ecken, Strom an bis zu drei Anschlüssen oben.",
              "",
              "&eIE, Dieselgenerator:&r Brennstoff Biodiesel, Hochcetan-Biodiesel oder zur Not Kreosotöl, &d4 096 FE/t&r, verteilt auf die Anschlüsse, läuft nur, wenn jemand Strom abnimmt. HV-Draht ist Pflicht. Der Generatorblock öffnet mit Stufe 3, siehe Kapitel &6Immersive Engineering: Schwerindustrie&r.",
          ],
          "minecraft:bucket", ["s3_choice"], xp=3),

    check("huge_diesel", X[4], Y3 + 2, "&6Bau den Riesen-Dieselmotor",
          "Create Diesel Generators, 224 RPM, bis 16 384 SU.",
          [
              "Der &6Riesen-Dieselmotor&r ist ein großer Multiblock aus Motorteilen, der wie der kleine mit Diesel oder Biodiesel per Rohr gefüllt wird. Ein &6Turbolader&r verdoppelt seine Drehzahl.",
              "",
              "&eCreate Diesel Generators, Riesen-Dieselmotor:&r &d224 RPM&r und bis &d16 384 SU&r, so viel wie eine voll versorgte Dampfmaschine, aber bei dreieinhalbfacher Drehzahl. Dazu kommen in Stufe 3 die &6Pumpjacks&r für Rohöl und der &6Destillationsturm&r für Diesel. Offen ab Stufe 3.",
          ],
          "create:large_cogwheel", ["s3_choice"]),

    check("pnc", X[5], Y3 + 2, "&bÜbersetze Druckluft und FE",
          "PneumaticCraft: Dynamo 40 FE/t aus Luft, Flux-Kompressor 40 FE/t zu Luft.",
          [
              "&ePneumatischer Dynamo (Kronwerke):&r ein Fortgeschrittenes Druckrohr oben, Zahnräder aus Druckeisen um einen Druckeisenbarren, unten Druckeisen, &6Einfacher Steuerschaltkreis&r, Druckeisen. &eFlux-Kompressor (Kronwerke):&r Redstone, Zahnrad, Schaltkreis, Redstoneblock, Turbinenrotor, Druckrohr, Redstone, Schmelzofen, Schaltkreis.",
              "",
              "&ePneumaticCraft, Pneumatischer Dynamo:&r Brennstoff Druckluft, &d100 mL Luft = 40 FE&r, &d40 FE/t&r ohne Upgrades, Abgabe 80 FE/t. &eFlux-Kompressor:&r &d100 FE = 40 mL Luft&r, verbraucht 40 FE/t, Puffer 100 000. Beide müssen gekühlt werden, sonst sinkt der Wirkungsgrad. &eRezept auf Kronwerke:&r beide brauchen den Mekanism-Schaltkreis statt der gedruckten Platine. Offen ab Stufe 3.",
          ],
          "minecraft:piston", ["s3_choice"]),

    check("flux", X[6], Y3 + 2, "&dBau ein Flux-Netzwerk",
          "Flux Networks, Strom ohne Kabel, 800 000 FE/t je Punkt.",
          [
              "&6Flux-Staub:&r Redstone auf einen &6Obsidian&r fallen lassen, der auf Grundgestein steht. &eFlux-Kern (Kronwerke):&r Staub in die Ecken, Obsidian an die Seiten, ein &6Quellenedelstein&r in der Mitte. &eController (Kronwerke):&r Fluxblöcke, Staub, Kern oben und ein &6Fortschrittlicher Steuerschaltkreis&r in der Mitte.",
              "",
              "&eFlux Networks:&r Ein &6Flux Plug&r nimmt Strom aus Generatoren und Speichern, ein &6Flux Point&r gibt ihn an Maschinen ab, überall auf der Welt, auch in anderen Dimensionen, bis &d800 000 FE/t&r je Gerät. Der &6Controller&r lädt außerdem deine Werkzeuge drahtlos. Jeder Spieler hat bis zu 5 Netze, Chunks werden auf Wunsch geladen.",
              "",
              "&eSpeicher:&r &6Basic Flux Storage&r &d2 Millionen FE&r, 20 000 FE/t. Herculean 16 Millionen und 120 000 FE/t (Stufe 4), Gargantuan 128 Millionen und 720 000 FE/t (Stufe 5). Mekanism-Kabel tauschen mit Flux ohne Limit. Offen ab Stufe 3.",
          ],
          "ars_nouveau:source_gem", ["s3_choice"], xp=3),

    check("aura_rf", X[7], Y3 + 2, "&aWandle Aura in Strom",
          "Nature's Aura, RF-Umwandler, 20 Aura = 1 FE.",
          [
              "&eRezept:&r Redstoneblöcke in die Ecken, ein &6Token der Furcht&r oben, ein &6Token des Zorns&r unten, zwei &6Himmelsbarren&r an den Seiten, ein &6Umwandlungskatalysator&r in der Mitte.",
              "",
              "&eNature's Aura, RF-Umwandler:&r Brennstoff Aura aus der Umgebung, &d20 Aura = 1 FE&r. Er leert die Gegend spürbar, also nur neben starken Aura-Generatoren betreiben. Eher ein Notstrom für Magier als ein Kraftwerk. Offen ab Stufe 3 mit dem Himmelsbarren.",
          ],
          "minecraft:sunflower", ["s3_choice"]),

    # ---- Stufe 4 ---------------------------------------------------------------------------
    quest("s4_choice", 0, Y4, "&e&lStufe 4: Welche Quelle wann",
          subtitle="Das End ist offen, die Maschinen fressen Strom.",
          description=[
              "Stufe 4 bringt Powah Nitro, Mekanism Elite und Ultimativ mit der Fusion, NuclearCraft, Draconic Evolution und die großen Generatoren von Mekanism More Machine.",
              "",
              "&e1. Nitro-Reaktor von Powah:&r &d500 000 FE/t&r aus Uraninit. Nitro-Kristalle brauchen einen Netherstern und 20 Millionen FE je Kristall in der Kugel, danach läuft er wie der kleine.",
              "&e2. RTGs von NuclearCraft:&r kein Brennstoff, keine Kühlung, nie aus. Uran 112, Plutonium 1 792, Californium &d4 096 FE/t&r, Block für Block.",
              "&e3. Fusionsreaktor von Mekanism:&r D-T-Treibstoff aus Wasser, gezündet mit dem Laser, läuft dann für Tage. Das Kraftwerk für die Antimaterie in Stufe 5.",
              "",
              "Speicher: der &6Draconic-Energiekern&r fasst ab 45,5 Millionen FE und wächst in sieben Stufen bis 2,14 Billionen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(3)],
          deps=["s3_choice"], icon="minecraft:amethyst_block", size=1.5, shape="diamond"),

    check("powah_nitro", X[0], Y4, "&bRüste Powah auf Nitro",
          "Powah Nitro: 40 000 FE/t Furnator, 500 000 FE/t Reaktor, 2 Milliarden FE Zelle.",
          [
              "Ein &6Nitro-Kristall&r entsteht in der Kugel aus Netherstern, zwei Redstoneblöcken und einem Block Blazing-Kristalle für 20 Millionen FE. Daraus Kondensatoren, dann wie gewohnt aufrüsten.",
              "",
              "&ePowah, Nitro:&r Furnator und Magmator &d40 000 FE/t&r, Solar und Thermo 2 000 FE/t, Reaktor &d500 000 FE/t&r (Puffer 500 Millionen). Nitro-Kabel 1 Million FE/t, Nitro Energy Cell &d2 Milliarden FE&r mit 2 Millionen FE/t. Offen ab Stufe 4.",
          ],
          "minecraft:diamond_block", ["s4_choice"]),

    check("mek_ultimate", X[1], Y4, "&5Rüste Mekanism auf Elite und Ultimativ",
          "Mekanism: bis 3 276 800 FE/t im Kabel, 102,4 Millionen FE im Würfel.",
          [
              "Elite- und Ultimativ-Kabel, Würfel und Induktionszellen entstehen aus den fortgeschrittenen mit Verstärkter und Atomlegierung und den Elite- und Ultimativ-Schaltkreisen.",
              "",
              "&eMekanism, Elite:&r Kabel &d409 600 FE/t&r, Würfel 25,6 Millionen FE mit 25 600 FE/t, Induktionszelle 204,8 Milliarden FE, Anschluss 6,5 Millionen FE/t. &eUltimativ:&r Kabel &d3 276 800 FE/t&r, Würfel &d102,4 Millionen FE&r mit 102 400 FE/t, Induktionszelle &d1,6 Billionen FE&r, Anschluss 52,4 Millionen FE/t. Offen ab Stufe 4, siehe Kapitel &6Mekanism: Elite&r.",
          ],
          "minecraft:emerald_block", ["s4_choice"]),

    check("mek_fusion", X[2], Y4, "&5Zünde den Fusionsreaktor",
          "Mekanism, Fusion: D-T-Treibstoff, Laser, Strom oder Dampf.",
          [
              "Rauten aus &6Reaktorrahmen&r (Polonium-Pellets im Rezept), Reaktorglas, Anschlüsse, die &6Laser-Fokusmatrix&r (Kronwerke: Quellenedelsteinblock) und der Controller oben. Hohlraum mit D-T-Treibstoff in den Controller, Laserverstärker auf die Matrix, zünden.",
              "",
              "&eMekanism, Fusionsreaktor:&r Brennstoff Deuterium und Tritium aus Wasser (Elektrolyseur, Solar-Neutronenaktivator). Strom direkt über die Anschlüsse, oder mit Wasser Dampf für die Industrieturbine, damit noch mehr. Puffer 400 Millionen FE. Je höher die Einspritzrate, desto mehr Strom, die Zahl hängt von Rate und Kühlung ab. &eRezept auf Kronwerke:&r die Fokusmatrix braucht einen Quellenedelsteinblock. Offen ab Stufe 4, siehe Kapitel &6Mekanism: Elite&r.",
          ],
          "minecraft:sea_lantern", ["s4_choice"], xp=3),

    check("mekmm_large", X[3], Y4, "&5Stell die großen Generatoren",
          "Mekanism More Machine: 400 FE/t plus Lava, bis 1,5 Millionen FE/t Wind.",
          [
              "Der &6Große Wärmegenerator&r und der &6Große Windgenerator&r sind die Riesenversionen der Mekanism-Generatoren, der &6Große Gasgenerator&r hat einen Tank von 180 000 mB. Alle drei große Blöcke, der Windgenerator darf keinen zweiten direkt neben sich haben.",
              "",
              "&eMekanism More Machine, Großer Wärmegenerator:&r &d400 FE/t&r aus Brennstoff, &d140 FE/t je Lavaseite&r, bis 81 Seiten, im Nether 300 FE/t extra, Tank 240 000 mB. &eGroßer Windgenerator:&r &d900 000 FE/t&r unten, &d1 500 000 FE/t&r ganz oben, ohne Brennstoff. Der stärkste Dauerläufer ohne Brennstoff im Pack. Offen ab Stufe 4. Der &6Solar-Wärmegenerator&r (Reflektoren heizen Kühlmittel) ist schon ab Stufe 3 offen.",
          ],
          "create:encased_fan", ["s4_choice"], xp=3),

    check("nc_passive", X[4], Y4, "&aLeg Solarzellen und RTGs",
          "NuclearCraft: 28 bis 1 792 FE/t Sonne, 112 bis 4 096 FE/t RTG, für immer.",
          [
              "Die &6Solarzellen&r brauchen Himmel über sich, die &6RTGs&r nur einen Platz und ein Kabel. Beide laufen, bis du sie abbaust. RTGs strahlen, also Geigerzähler und Abstand.",
              "",
              "&eNuclearCraft, Solarzellen:&r Basic &d28 FE/t&r, Advanced 112, DU 448, Elite &d1 792 FE/t&r, nur bei Tag. &eRTGs:&r Uran &d112 FE/t&r, Americium 448, Plutonium 1 792, Californium &d4 096 FE/t&r, Tag und Nacht, ohne Brennstoff und ohne Kühlung. Americium, Plutonium und Californium kommen aus abgebranntem Brennstoff. &eBatterien:&r Lithium-Ionen-Batterien in vier Stufen als Puffer. Offen ab Stufe 4, siehe Kapitel &6NuclearCraft&r.",
          ],
          "minecraft:daylight_detector", ["s4_choice"]),

    check("nc_fission", X[5], Y4, "&aFahr den NuclearCraft-Spaltreaktor an",
          "NuclearCraft: Spaltreaktor, Dampfturbine, Zerfallsgenerator.",
          [
              "Hülle aus Casing und Glas, innen frei gesetzte &6Brennstoffzellen&r, Moderatoren und Kühlkörper, ein &6Controller&r und ein &6Port&r in der Wand. Netto-Hitze auf null, Redstone-Signal zündet. Im Energie-Modus kommt Strom aus dem Port, im Siede-Modus Dampf für die &6Dampfturbine&r.",
              "",
              "&eNuclearCraft, Spaltreaktor:&r Brennstoff LEU-235 und andere Brennstoffe, Ausstoß hängt von Zellen und Moderatoren ab. Kernschmelze etwa wie TNT. &eDampfturbine:&r ein Multiblock mit Rotorblättern und Spulen, 5 bis 17 Blöcke Kante, 2 000 mB Dampf je Blatt, Strom aus dem Dampf des Reaktors. &eZerfallsgenerator:&r Strom aus radioaktiven Blöcken daneben, die er langsam zu Blei zerfallen lässt. Offen ab Stufe 4, siehe Kapitel &6NuclearCraft&r.",
          ],
          "minecraft:tnt", ["s4_choice"], xp=3),

    check("draconic_gen", X[6], Y4, "&5Bau den Draconic-Generator",
          "Draconic Evolution, 5 bis 300 FE/t, je nach Modus.",
          [
              "&eRezept:&r Netherziegel in die Ecken, Eisen an die Seiten, ein Ofen in die Mitte, ein &6Draconiumkern&r unten in die Mitte. Im Fenster wählst du den Modus.",
              "",
              "&eDraconic Evolution, Generator:&r Brennstoff alles Brennbare. Eco Plus &d5 FE/t&r (50 FE je Brenntick, also 80 000 aus einer Kohle), Eco 20 FE/t, Normal &d40 FE/t&r, Performance 80 FE/t, Overdrive &d300 FE/t&r (5 FE je Brenntick). Kein Kraftwerk, aber ein sparsamer Notstrom. Offen ab Stufe 4, siehe Kapitel &6Draconic Evolution&r.",
          ],
          "minecraft:furnace", ["s4_choice"]),

    check("draconic_core", X[7], Y4, "&cBau den Energiekern",
          "Draconic Evolution, 45,5 Millionen bis 2,14 Billionen FE, Stufe 8 ohne Grenze.",
          [
              "&6Energiekern&r: Draconiumbarren oben und unten, zwei Wyvern-Energiekontroller und ein Wyvern-Kern. Tier Up und Build Guide im Fenster zeigen die Hülle aus Draconium- und Redstoneblöcken, vier &6Stabilisatoren&r (Kronwerke: ein Gaia-Geist) rundherum, dann Activate.",
              "",
              "&eDraconic Evolution, Energiekern:&r Stufe 1 &d45,5 Millionen FE&r, 2: 273 Millionen, 3: 1,64 Milliarden, 4: 9,88 Milliarden, 5: 59,3 Milliarden, 6: 356 Milliarden, 7: &d2,14 Billionen&r, Stufe 8 ohne Grenze, aber mit Erwachtem Draconium (Stufe 5). &6Energiepylonen&r bringen den Strom hinein und heraus. &eRezept auf Kronwerke:&r der Stabilisator braucht einen Gaia-Geist. Offen ab Stufe 4.",
          ],
          "minecraft:redstone_block", ["s4_choice"], xp=3),

    # ---- Stufe 5 ---------------------------------------------------------------------------
    quest("s5_choice", 0, Y5, "&e&lStufe 5: Welche Quelle wann",
          subtitle="Alles offen. Der Strom für hundert Pellets.",
          description=[
              "Stufe 5 öffnet den Spaltreaktor von Mekanism, den Drakonischen Reaktor und den Gargantuan-Speicher von Flux. Das Ziel am Obelisken, 100 Antimaterie-Pellets, braucht eine Billion Joule je Pellet, also 400 Milliarden FE.",
              "",
              "&e1. Spaltreaktor plus Industrieturbine:&r Spaltbrennstoff aus Uran, Wasser rein, Dampf raus, die Turbine aus Stufe 3 macht daraus Strom. Der Atommüll daraus ist zugleich der Rohstoff für Polonium und Plutonium.",
              "&e2. Fusionsreaktor aus Stufe 4&r auf hoher Einspritzrate mit Dampf in eine zweite Turbine, wenn der Spaltreaktor dir zu heiß ist.",
              "&e3. Drakonischer Reaktor:&r der größte Ausstoß im Pack, aber er explodiert, wenn das Feld fällt. Nur mit Energiekern als Rücklage für den Injektor.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(3)],
          deps=["s4_choice"], icon="minecraft:sculk_catalyst", size=1.5, shape="diamond"),

    check("mek_fission", X[0], Y5, "&5Fahr den Spaltreaktor an",
          "Mekanism, Spaltreaktor: Wasser zu Dampf, Dampf zu Strom in der Turbine.",
          [
              "Ein Kasten aus &6Kernreaktorgehäuse&r, innen Säulen aus &6Brennstäben&r mit je einem &6Steuerstab&r obendrauf, &6Schnittstellen&r für Brennstoff, Kühlmittel, Dampf und Abfall in der Wand. Starten mit 0,1 mB pro Tick.",
              "",
              "&eMekanism, Spaltreaktor:&r Brennstoff Spaltbrennstoff, &d1 Million Joule Hitze je mB&r, also 400 000 FE, umgesetzt über Wasser und Dampf in der &6Industrieturbine&r. Brennrate und Turbinengröße bestimmen den Ausstoß. Kernschmelzen sind auf diesem Server &can&r, Radius 8 Blöcke, Strahlung mal fünfzig. Offen ab Stufe 5, siehe Kapitel &6Mekanism: Antimaterie&r.",
          ],
          "minecraft:water_bucket", ["s5_choice"], xp=3),

    check("draconic_reactor", X[1], Y5, "&cStarte den Drakonischen Reaktor",
          "Draconic Evolution, Reaktor: riesiger Ausstoß, riesige Explosion.",
          [
              "&6Reaktorkern&r, vier &6Stabilisatoren&r und ein &6Energieinjektor&r, alles erst nach dem Chaoswächter. Erwachtes Draconium als Brennstoff, mit dem Injektor aufladen, aktivieren, dann das Eindämmungsfeld dauerhaft füttern.",
              "",
              "&eDraconic Evolution, Reaktor:&r Brennstoff Erwachtes Draconium, aus dem nach und nach Chaos wird. Der Ausstoß steigt mit Temperatur und Sättigung in die Millionen FE/t, der Injektor braucht dafür ständig einen Teil zurück. Fällt das Feld auf null, reißt die Explosion einen Krater, die große Explosion ist hier &cnicht abgeschaltet&r. Offen ab Stufe 5, siehe Kapitel &6Draconic: Erwacht und Chaos&r.",
          ],
          "minecraft:tnt", ["s5_choice"], xp=3),

    check("flux_gargantuan", X[2], Y5, "&dStell den Gargantuan Flux Storage",
          "Flux Networks, 128 Millionen FE, 720 000 FE/t.",
          [
              "Der &6Gargantuan Flux Storage&r ist die größte Flux-Zelle, gebaut aus dem Herculean-Speicher und Fluxblöcken. Er hängt direkt im Netz, ohne Plug und Point.",
              "",
              "&eFlux Networks, Gargantuan:&r &d128 Millionen FE&r, &d720 000 FE/t&r rein und raus, drahtlos über das Netz. Für den Draconic-Energiekern zu klein, als Puffer zwischen Reaktor und Fabrik genau richtig. Offen ab Stufe 5.",
          ],
          "minecraft:lapis_block", ["s5_choice"]),

    quest("summary", X[4], Y5, "&6&lZieh Bilanz",
          subtitle="Jede Quelle im Pack kennst du jetzt beim Namen.",
          description=[
              "Von 256 SU am Bach bis zu Reaktoren, die Millionen FE pro Tick machen: alles, was in Kronwerke Strom oder Rotation erzeugt, steht in diesem Kapitel. Hak ab, was du gebaut hast, und schau vor jeder neuen Stufe hier nach, bevor du Kabel ziehst.",
              "",
              "&eDie Faustregel:&r Stufe 1 Wasserräder, Stufe 2 Wärmegenerator und Dampf, Stufe 3 Powah-Reaktor und Flux, Stufe 4 Nitro, RTGs und Fusion, Stufe 5 Spaltung und Turbine. Wer eine Stufe früher mehr will, baut Ethen.",
              "",
              "&eKronwerke-Rezepte in diesem Kapitel:&r Flux-Kern (Quellenedelstein) und Flux-Controller (Fortschrittlicher Schaltkreis), Pneumatischer Dynamo und Flux-Kompressor (Einfacher Schaltkreis), die Laser-Fokusmatrix der Fusion (Quellenedelsteinblock) und der Energiekern-Stabilisator (Gaia-Geist). Alles andere ist wie in den Mods.",
          ],
          tasks=[task_checkmark("Alles gesehen")],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["s5_choice", "s4_choice", "s3_choice", "s2_choice", "s1_choice"],
          icon="create:speedometer", size=2.0, shape="gear"),
]

images = [
    head("title", "Checkliste: Strom", -1, -2.6, height=1.6, kind="title"),
    head("s1", "Stufe 1: Rotation", -1, Y1 - 1.4, colour="stone"),
    head("s2", "Stufe 2: Der erste Strom", -1, Y2 - 1.4, colour="fire"),
    head("s3", "Stufe 3: Kraftwerke", -1, Y3 - 1.4, colour="brass"),
    head("s4", "Stufe 4: Reaktoren", -1, Y4 - 1.4, colour="magic"),
    head("s5", "Stufe 5: Spaltung und Chaos", -1, Y5 - 1.4, colour="end"),
]

chapter(C, "Checkliste: Strom", "create:water_wheel", "lists", quests, shape="square", order=68, stage=1,
        subtitle=["Jeder Generator des Packs, eine Zeile, ein Haken. Nach Stufen sortiert."], images=images)
