"""Powah in stage 3: dielectric parts, the energizing orb (Kronwerke: mana diamond) and its rods,
charged certus (Kronwerke: 2 per craft), energized steel and the crystals up to spirited, the
generators, cables and energy cells. Nitro is stage 4 and only mentioned. Numbers follow the
server's config/powah.json5; the orb recipe follows kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import (chapter, quest, task_item, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "powah"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Grundlagen -----------------------------------------------------------------
    quest("welcome", 0, 1.5, "&b&lPowah",
          subtitle="Strom in Stufen, vom Starter bis Spirited.",
          description=[
              "&6Powah&r ist auf Kronwerke ab Stufe 3 offen. Es baut Generatoren, Kabel und Speicher in Stufen: &7Starter&r, &fBasic&r, &8Hardened&r, &6Blazing&r, &bNiotic&r und &aSpirited&r. Jede Stufe macht und trägt deutlich mehr Strom als die vorige. Die letzte Stufe, &cNitro&r, kommt in Stufe 4.",
              "",
              "Das Besondere ist die &6Energizing Orb&r: eine Kugel, die Gegenstände mit Strom auflädt und dabei in neue Materialien verwandelt. Damit machst du hier Kristalle, Energiestahl und für die AE2-Spieler &6Geladenen Certus-Quarz&r.",
              "",
              "Alles beginnt mit &6Dielectric Paste&r. Drei Kohle oder Holzkohle, zwei Ton und ein Lavaeimer ergeben 24 Stück. Mit Lohenstaub statt Lava (zwei Kohle, ein Ton, ein Lohenstaub) sind es 16, ganz ohne Eimer.",
              "",
              img(item_texture("powah:dielectric_paste"), 32, 32),
          ],
          tasks=[task_item("powah:dielectric_paste", 32)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_table("s3_common"), reward_xp(5)],
          icon="powah:dielectric_paste", size=2.0, shape="hexagon"),

    quest("casing", 2.75, 0, "&7Stäbe und Gehäuse",
          subtitle="Das Gerippe jeder Powah-Maschine.",
          description=[
              "Paste und Eisengitter ergeben je acht &6Dielectric Rods&r, senkrecht oder waagerecht, je nachdem, wie du sie legst: Paste links und rechts von einer Spalte Gitter gibt senkrechte, Paste über und unter einer Reihe Gitter gibt waagerechte.",
              "",
              "Das &6Dielectric Casing&r baust du aus vier Eisenbarren in den Ecken, zwei waagerechten Stäben oben und unten und zwei senkrechten links und rechts. Die Mitte bleibt leer.",
              "",
              "Fast jeder Block von Powah hat so ein Gehäuse im Rezept. Mach gleich ein paar mehr.",
          ],
          tasks=[task_item("powah:dielectric_casing", 4)],
          rewards=[reward_item("minecraft:iron_bars", 16)],
          deps=["welcome"], icon="powah:dielectric_casing"),

    quest("capacitors", 2.75, 3, "&7Kondensatoren",
          subtitle="Die Stufe steckt im Kondensator.",
          description=[
              "Vier Eisenbarren, zwei Paste und ein Redstone-Block ergeben vier &6Basic Capacitors&r. Einer davon zerfällt an der Werkbank in zwei &6Tiny&r, zwei zusammen ergeben einen &6Large&r.",
              "",
              "&eSo funktionieren die Stufen:&r Für die Starter-Stufe nimmst du Tiny-Kondensatoren, für Basic die normalen. Für Hardened, Blazing, Niotic und Spirited baust du je einen eigenen Kondensator aus einem Large, Paste und dem Material der Stufe: Energiestahl, Blazing-, Niotic- oder Spirited-Kristall.",
              "",
              "Eine höhere Maschine baust du fast immer aus der Maschine der Stufe darunter, dem Gehäuse und den Kondensatoren der neuen Stufe. Du verlierst beim Aufrüsten also nichts.",
          ],
          tasks=[task_item("powah:capacitor_basic", 4), task_item("powah:capacitor_basic_tiny", 2)],
          rewards=[reward_item("minecraft:redstone_block", 4)],
          deps=["welcome"], icon="powah:capacitor_basic"),

    quest("orb", 5.5, 1.5, "&d&lEnergizing Orb",
          subtitle="Ohne Mana kein Strom.",
          description=[
              "Die &6Energizing Orb&r lädt Gegenstände mit Strom, bis sie sich verwandeln. Sie selbst braucht keinen Strom, den liefern die Stäbe im nächsten Schritt.",
              "",
              "&eRezept auf Kronwerke:&r oben Glas, ein &bManadiamant&r aus Botania, Glas. In der Mitte Glas, das Dielectric Casing, Glas. Unten drei waagerechte Dielectric Rods. Im Original sitzt oben nur Glas, auf Kronwerke braucht die Strom-Mod Mana zum Start.",
              "",
              "Einen Manadiamanten macht jeder Botaniker im Manabecken aus einem Diamanten. Frag im Chat, falls du kein Becken hast.",
              "",
              "&eBedienung:&r Öffne die Kugel und leg die Zutaten hinein. Was sie damit machen kann, zeigt JEI unter &eEnergizing&r, mit der nötigen Strommenge.",
          ],
          tasks=[task_item("powah:energizing_orb", 1)],
          rewards=[reward_item("botania:mana_diamond", 1), reward_table("s3_common"), reward_xp(10)],
          deps=["casing"], icon="powah:energizing_orb", size=2.0, shape="gear"),

    quest("rods", 8.25, 1.5, "&eEnergizing Rods",
          subtitle="Die Stäbe bringen den Strom.",
          description=[
              "Ein &6Energizing Rod (Starter)&r ist ein Netherquarz oben, zwei Tiny-Kondensatoren links und rechts vom Dielectric Casing und ein senkrechter Dielectric Rod unten.",
              "",
              "&eSo baust du die Anlage:&r Stell die Stäbe im Umkreis von &e4 Blöcken&r um die Kugel. Jeder Stab braucht Strom von unten, also stell ihn auf ein Kabel, eine Energiezelle oder einen Generator. Falls ein Stab nicht mitarbeitet, verbinde ihn mit der Kugel über den &6Wrench&r im Modus &eLink&r.",
              "",
              "&eWie schnell:&r Ein Starter-Stab gibt 100 FE pro Tick an die Kugel. Mehrere Stäbe arbeiten zusammen, bessere Stäbe schaffen viel mehr: Basic 400, Hardened 1 000, Blazing 4 000, Niotic 10 000, Spirited 40 000 FE/t.",
          ],
          tasks=[task_item("powah:energizing_rod_starter", 2)],
          rewards=[reward_item("powah:capacitor_basic", 4), reward_xp(5)],
          deps=["orb"], icon="powah:energizing_rod_starter"),

    # ---- Energetisieren -------------------------------------------------------------
    quest("certus", 11, 0, "&bGeladener Certus-Quarz",
          subtitle="Der Einstieg in AE2, zwei auf einmal.",
          description=[
              "&eRezept auf Kronwerke:&r Ein &6Certus-Quarzkristall&r und ein Redstone in der Kugel ergeben für 20 000 FE &ezwei&r Geladene Certus-Quarzkristalle. Der Auflader von AE2 und alle anderen Wege sind entfernt.",
              "",
              "Der zweite Weg führt über die Magie: Die Imbuement-Kammer von Ars Nouveau lädt einen Kristall für 2 000 Quelle, mit Redstone und Glowstone auf den Sockeln. Das gibt aber nur einen pro Durchgang.",
              "",
              "Geladener Certus ist der Anfang von Fluix und damit von jedem ME-Netzwerk. Wer eine Kugel hat, kann den Lagerbauern viel Arbeit abnehmen.",
          ],
          tasks=[task_item("ae2:charged_certus_quartz_crystal", 16)],
          rewards=[reward_item("ae2:certus_quartz_crystal", 16), reward_xp(5)],
          deps=["rods"], icon="ae2:charged_certus_quartz_crystal"),

    quest("steel", 11, 2.5, "&7Energiestahl",
          subtitle="Eisen und Gold, aufgeladen.",
          description=[
              "Ein Eisenbarren und ein Goldbarren werden in der Kugel für 10 000 FE zu zwei &6Energized Steel&r.",
              "",
              img(item_texture("powah:steel_energized"), 32, 32),
              "",
              "Energiestahl ist das Material der &8Hardened&r-Stufe: Hardened-Kondensatoren, Hardened-Kabel, Hardened-Zellen und Generatoren. Mach dir einen Stapel.",
          ],
          tasks=[task_item("powah:steel_energized", 16)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:iron_ingot", 8)],
          deps=["rods"], icon="powah:steel_energized"),

    quest("blazing", 13.5, 2.5, "&6Blazing-Kristall",
          subtitle="Eine Lohenrute voller Strom.",
          description=[
              "Eine &6Lohenrute&r, oder vier Lohenstaub, ergibt in der Kugel für 120 000 FE einen &6Blazing Crystal&r. Mit einem einzelnen Starter-Stab dauert das eine Minute, mit ein paar besseren Stäben nur Sekunden.",
              "",
              img(item_texture("powah:crystal_blazing"), 32, 32),
              "",
              "Die Kristalle sind das Material der &6Blazing&r-Stufe. Lohenruten holst du aus der Netherfestung oder vom Lohenspawner, und die Create-Leute haben oft welche über.",
          ],
          tasks=[task_item("powah:crystal_blazing", 8)],
          rewards=[reward_item("minecraft:blaze_rod", 8), reward_table("s3_common")],
          deps=["steel"], icon="powah:crystal_blazing"),

    quest("niotic", 16, 2.5, "&bNiotic-Kristall",
          subtitle="Ein Diamant, dreihunderttausend FE.",
          description=[
              "Ein &bDiamant&r ergibt für 300 000 FE einen &6Niotic Crystal&r. Spätestens jetzt lohnen sich Hardened- oder Blazing-Stäbe an der Kugel.",
              "",
              img(item_texture("powah:crystal_niotic"), 32, 32),
              "",
              "Niotic-Kondensatoren bekommst du nur einen pro Rezept, nicht zwei wie bei Hardened und Blazing. Plane also ein paar Diamanten mehr ein.",
          ],
          tasks=[task_item("powah:crystal_niotic", 4)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(10)],
          deps=["blazing"], icon="powah:crystal_niotic"),

    quest("spirited", 18.5, 2.5, "&aSpirited-Kristall",
          subtitle="Die letzte Stufe in Stufe 3.",
          description=[
              "Ein &aSmaragd&r ergibt für 1 000 000 FE einen &6Spirited Crystal&r. Das ist das obere Ende von Powah auf Kronwerke, bis Stufe 4 öffnet.",
              "",
              "&cAusblick:&r Der &cNitro-Kristall&r braucht einen Netherstern, zwei Redstone-Blöcke und einen Block aus Blazing-Kristallen und kostet 20 Millionen FE. Er und alles aus Nitro kommen in Stufe 4.",
          ],
          tasks=[task_item("powah:crystal_spirited", 2)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(10)],
          deps=["niotic"], icon="powah:crystal_spirited", optional=True),

    quest("rod_upgrade", 13.5, 4.5, "&8Bessere Stäbe",
          subtitle="Mehr FE pro Tick an der Kugel.",
          description=[
              "Jeder höhere Stab entsteht aus dem Stab darunter: oben ein &6Quarzblock&r, links und rechts die Kondensatoren der neuen Stufe, in der Mitte ein Dielectric Casing, unten der alte Stab.",
              "",
              "Ein &8Hardened&r-Stab gibt zehnmal so viel Strom wie ein Starter-Stab. Bei Kristallen mit 120 000 FE und mehr macht das aus Minuten Sekunden. Denk daran, dass die Leitung zu den Stäben das auch tragen muss.",
          ],
          tasks=[task_item("powah:energizing_rod_hardened", 1)],
          rewards=[reward_item("minecraft:quartz_block", 4)],
          deps=["steel"], icon="powah:energizing_rod_hardened"),

    # ---- Strom erzeugen -------------------------------------------------------------
    quest("furnator", 0, 8.5, "&6Furnator",
          subtitle="Kohle rein, Strom raus.",
          description=[
              "Der &6Furnator&r verbrennt alles, was im Ofen brennt. &eRezept (Starter):&r oben drei Paste, in der Mitte zwei Tiny-Kondensatoren links und rechts vom Dielectric Casing, unten Paste, Ofen, Paste.",
              "",
              "Jeder Brennstoff gibt 30 FE pro Brennzeit-Tick, ein Stück Kohle also 48 000 FE, egal welche Stufe. Höhere Stufen verbrennen nur schneller: Starter 20, Basic 80, Hardened 200, Blazing 800, Niotic 2 000, Spirited 8 000 FE/t.",
              "",
              "Der &6Magmator&r ist das gleiche für &cLava&r und andere heiße Flüssigkeiten, mit einem Eimer statt dem Ofen im Rezept und den gleichen Werten. Neben einer Lavapumpe aus dem Nether läuft er ohne Pause.",
          ],
          tasks=[task_item("powah:furnator_starter", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(5)],
          deps=["welcome"], icon="powah:furnator_starter", size=1.5, shape="hexagon"),

    quest("solar", 2.75, 10, "&eSolar und Thermo",
          subtitle="Strom ohne Brennstoff.",
          description=[
              "Das &6Solar Panel&r braucht freien Himmel und liefert tagsüber Starter 20, Basic 60, Hardened 100, Blazing 200, Niotic 400 und Spirited 800 FE/t. Mit einer &6Lens of Ender&r sieht es durch Blöcke über sich hindurch. Die Photoelectric Pane im Rezept ist eine Glasscheibe mit Lapis und Paste.",
              "",
              "Der &6Thermo Generator&r hat die gleichen Werte, steht aber auf einer Wärmequelle wie Lava oder Magma und braucht ein Kühlmittel, zum Beispiel Wasser. JEI zeigt unter &eHeat Sources&r und &eCoolants&r, was geht.",
          ],
          tasks=[task_item("powah:solar_panel_starter", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16)],
          deps=["furnator"], icon="powah:solar_panel_starter", optional=True),

    quest("gen_tiers", 2.75, 7, "&8Generatoren aufrüsten",
          subtitle="Vom Starter zum Hardened.",
          description=[
              "Ein Starter-Furnator ist schwach. Aufgerüstet wird er an der Werkbank: der alte Generator unten in die Mitte, das Dielectric Casing darüber, die Kondensatoren der neuen Stufe links und rechts, der Rest mit Eisen (Basic), Energiestahl (Hardened) oder Blazing-Kristallen (Blazing).",
              "",
              "Ein &8Hardened Furnator&r macht zehnmal so viel wie der Starter. Für Basic brauchst du nur Eisen und normale Kondensatoren, für Hardened den Energiestahl aus der Kugel.",
          ],
          tasks=[task_item("powah:furnator_hardened", 1)],
          rewards=[reward_item("powah:steel_energized", 8)],
          deps=["furnator"], icon="powah:furnator_hardened"),

    quest("reactor", 8.25, 8.5, "&a&lReaktor",
          subtitle="Uraninit, gekühlt.",
          description=[
              "Der &6Reaktor&r ist der stärkste Generator von Powah. &eSo baust du ihn:&r Nimm &e36 Reaktorblöcke&r der gleichen Stufe in die Hand und setz einen ab. Der Reaktor baut sich auf einer freien Fläche von 3 mal 3 Blöcken, 4 Blöcke hoch, von selbst auf.",
              "",
              "&eRezept (Starter):&r vier &6Uraninit&r in die Ecken, vier Tiny-Kondensatoren an die Seiten, ein Dielectric Casing in die Mitte, ergibt vier Blöcke.",
              "",
              "&eUraninit:&r Uraninit-Erz liegt unterhalb von Y 64 (arm), Y 20 (normal) und Y 0 (dicht). Rohes Uraninit gibt in der Kugel zwei Uraninit für 2 000 FE. Auch Uranbarren aus Mekanism werden in der Kugel zu Uraninit.",
              "",
              "&eBetrieb:&r Uraninit ist der Brennstoff, Kohle und Redstone in den Nebenslots steigern die Leistung. Kühl ihn mit Wasser und festen Kühlmitteln wie Eis oder &bTrockeneis&r (zwei Blaueis in der Kugel). Im Auto-Modus hält er an, wenn er voll ist, und startet wieder unter 70 Prozent. Ein Starter-Reaktor schafft bis zu 250 FE/t, ein Blazing-Reaktor bis zu 10 000.",
          ],
          tasks=[task_item("powah:reactor_starter", 36)],
          rewards=[reward_item("powah:uraninite", 16), reward_table("s3_uncommon"), reward_xp(15)],
          deps=["rods"], icon="powah:reactor_starter", size=1.75, shape="hexagon"),

    # ---- Leiten und Speichern -------------------------------------------------------
    quest("cables", 0, 13, "&eKabel und Wrench",
          subtitle="Strom von hier nach da.",
          description=[
              "Sechs waagerechte Dielectric Rods, zwei Eisennuggets und ein Tiny-Kondensator ergeben zwölf &6Energy Cables (Starter)&r. Basic-Kabel baust du aus Starter-Kabeln, Stäben und einem Basic-Kondensator.",
              "",
              "&eWie viel sie tragen:&r Starter 500, Basic 2 000, Hardened 5 000, Blazing 20 000, Niotic 50 000, Spirited 200 000 FE/t.",
              "",
              "Den &6Wrench&r baust du aus zwei Eisenbarren und drei Paste. Er hat drei Modi, der aktuelle steht im Tooltip: &eConfig&r stellt an einer Kabelseite ein, ob sie zieht, schiebt oder nichts tut, &eLink&r verbindet Kugel und Stäbe, &eRotate&r dreht Blöcke.",
          ],
          tasks=[task_item("powah:energy_cable_basic", 12), task_item("powah:wrench", 1)],
          rewards=[reward_item("powah:dielectric_paste", 16)],
          deps=["furnator"], icon="powah:energy_cable_basic"),

    quest("cells", 2.75, 13, "&aEnergiezellen",
          subtitle="Ein Puffer für die ganze Basis.",
          description=[
              "Die &6Energy Cell (Basic)&r speichert 4 Millionen FE: Eisen in die Ecken, Basic-Kondensatoren an die Seiten, das Casing in die Mitte. Höhere Zellen baust du aus zwei Zellen der Stufe darunter, zwei neuen Kondensatoren und dem Material der Stufe.",
              "",
              "&eSpeicher:&r Starter 1, Basic 4, Hardened 10, Blazing 40, Niotic 100, Spirited 400 Millionen FE.",
              "",
              "&eEnder-Zellen:&r Mit einem &6Ender Core&r (Enderauge, Casing und Tiny-Kondensator in der Kugel) baust du Ender Cells. Sie teilen sich einen Speicher auf einem Kanal, egal wo sie stehen. Shift-Klick mit einer Energiezelle oder Batterie im Fenster einer Ender Cell vergrößert diesen Speicher.",
          ],
          tasks=[task_item("powah:energy_cell_basic", 1)],
          rewards=[reward_item("powah:capacitor_basic", 4), reward_xp(5)],
          deps=["cables"], icon="powah:energy_cell_basic"),

    quest("power_plant", 6.5, 13.5, "&6&lDas Kraftwerk",
          subtitle="Blazing-Strom für die Stahlstraßen.",
          description=[
              "Zeit für ein richtiges Kraftwerk: ein &6Blazing Furnator&r (Blazing-Kristalle, Blazing-Kondensatoren, Casing und ein Hardened Furnator) und eine &6Blazing Energy Cell&r als Puffer.",
              "",
              "Ein Blazing Furnator macht 800 FE/t, gut das Vierzigfache des Starters. Füttere ihn mit Kohleblöcken oder Holzkohle aus einer Baumfarm, oder setz gleich auf mehrere Reaktoren.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 3, &6Der Ofen schläft nie&r, will tausende Stahlbarren und Fortschrittliche Steuerschaltkreise. Hinter jeder Stahlstraße mit Dreifach-Erz, Infusionsanlagen und Fabriken steht ein Kraftwerk. Wenn dein Strom übrig ist, leg ein Kabel zum Nachbarn.",
          ],
          tasks=[task_item("powah:furnator_blazing", 1), task_item("powah:energy_cell_blazing", 1)],
          rewards=[reward_table("s3_rare"), reward_item("powah:crystal_blazing", 8), reward_xp(20)],
          deps=["cells", "gen_tiers", "blazing"], icon="powah:furnator_blazing", size=2.5, shape="gear"),
]

images = [
    head("title", "Powah", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 3: Stahlwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("energizing", "Energetisieren", 10.4, -1.4, colour="magic"),
    head("generators", "Strom erzeugen", 0.9, 5.4, colour="fire"),
    head("storage", "Leiten und Speichern", 0.9, 11.4, colour="water"),
]

chapter(C, "Powah", "powah:energizing_orb", "tech", quests, shape="circle", order=20, stage=3,
        subtitle=["Stufe 3: Energizing Orb, Kristalle bis Spirited, Generatoren, Kabel und Energiezellen."],
        images=images)
