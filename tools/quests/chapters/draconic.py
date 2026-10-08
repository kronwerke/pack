"""Draconic Evolution in stage 4, one step per quest: draconium from the End (dust, ingots,
blocks), the draconium core, the dislocator and magnet, generator and grinder, fusion crafting
(core, draconium injectors, wyvern core, wyvern injectors as the first fusion, capacitor,
advanced dislocator), the energy core (wyvern energy core, particle generator, stabilizers with
a Gaia spirit each on Kronwerke, pylons) and its tiers 2 to 7 as a checklist with capacities,
the wyvern tools, chestpiece and modules, and the stage 4 tech goal. Awakened and chaotic tiers
are stage 5 (chapter draconic_chaos). Recipes from the Draconic Evolution jar and
kubejs/server_scripts/kronwerke/tech.js; core sizes from data/draconicevolution/multiblocks,
capacities and fusion timings from config/brandon3055/DraconicEvolution.cfg."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img)

C = "draconic"


def pic(path, size=32):
    """A Draconic Evolution item texture inside a quest text."""
    return img(f"draconicevolution:textures/item/{path}.png", size, size)


def head(name, text, left, y, height=0.9, kind="section", colour="magic"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def tier(name, x, y, title, sub, blocks, cap, deps, extra=(), reward=None, task=None):
    """One energy core tier as a checklist quest."""
    return quest(name, x, y, title, subtitle=sub,
                 description=[
                     f"Kern deaktivieren, im Fenster mit &eTier Up&r eine Stufe höher stellen, &eToggle Build Guide&r an und die Blöcke setzen: {blocks}",
                     "",
                     f"&eSpeicher:&r {cap}",
                     *extra,
                 ],
                 tasks=[task or task_checkmark("Kern auf dieser Stufe aktiv")],
                 rewards=reward or [reward_xp(10)],
                 deps=deps, icon="draconicevolution:energy_core", optional=True)


quests = [
    # ---- Draconium ----------------------------------------------------------------
    quest("dust", 0, 1.5, "&5&lBau Draconium im End ab",
          subtitle="Das lila Erz gibt es nur im End.",
          description=[
              "Grab im End nach &5Ender-Draconiumerz&r, im Endstein zwischen Höhe 0 und 70, in Adern bis acht Blöcke. Nimm eine Spitzhacke mit &6Glück III&r mit.",
              "",
              pic("components/draconium_dust"),
              "",
              "Ein Erz gibt 2 bis 4 &5Draconiumstaub&r, mit Glück III im Schnitt etwa 4,5. Mit Behutsamkeit bekommst du nur das Erz, und das gibt im Ofen einen einzigen Barren.",
              "",
              "&eKronwerke:&r Die Erze in Oberwelt und Nether sind abgeschaltet. Erwacht und Chaos stehen im Kapitel &5Draconic: Erwacht und Chaos&r und kommen in Stufe 5.",
          ],
          tasks=[task_item("draconicevolution:draconium_dust", 16)],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_table("s4_common"), reward_xp(10)],
          icon="draconicevolution:draconium_dust", size=2.0, shape="hexagon"),

    quest("ingot", 2.5, 0.5, "&5Schmilz Draconiumbarren",
          subtitle="Ein Staub, ein Barren.",
          description=[
              "Leg &5Draconiumstaub&r in einen Ofen oder einen Energiegeladenen Schmelzer. Ein Staub wird ein &5Draconiumbarren&r.",
              "",
              pic("components/draconium_ingot"),
              "",
              "&eRezept auf Kronwerke:&r Die 256k-Komponente von AE2 und die MEGA-Komponenten für 1M und 4M haben je einen Draconiumbarren in der Mitte. Bring den Lagerleuten also welche mit.",
          ],
          tasks=[task_item("draconicevolution:draconium_ingot", 32)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(5)],
          deps=["dust"], icon="draconicevolution:draconium_ingot"),

    quest("elite", 2.5, 2.5, "&dBau einen Elite-Steuerschaltkreis",
          subtitle="Draconium für Mekanism.",
          description=[
              "&eRezept auf Kronwerke:&r &62 Fortschrittliche Steuerschaltkreise&r, &62 Verstärkte Legierung&r und &61 Draconiumstaub&r. Einen anderen Weg gibt es nicht.",
              "",
              "Damit hängt die ganze Elite-Stufe von Mekanism am End. Was du damit baust, steht im Kapitel &dMekanism: Elite&r.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 4 &e150 Elite-Steuerschaltkreise&r im Technik-Pfeiler.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 4)],
          rewards=[reward_item("draconicevolution:draconium_dust", 8), reward_table("s4_common")],
          deps=["dust"], icon="mekanism:elite_control_circuit"),

    quest("block", 5, 0.5, "&5Press Draconiumblöcke",
          subtitle="Neun Barren, ein Block.",
          description=[
              "Neun &5Draconiumbarren&r an der Werkbank ergeben einen &5Draconiumblock&r. Zurück geht es genauso.",
              "",
              "Blöcke brauchst du für den Wyvern-Injektor (einen pro Stück) und als Hülle des Energiekerns. Schon Stufe 3 des Kerns frisst 26 Blöcke, also 234 Barren.",
          ],
          tasks=[task_item("draconicevolution:draconium_block", 4)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 9), reward_xp(5)],
          deps=["ingot"], icon="draconicevolution:draconium_block"),

    quest("core", 5, 2.5, "&5&lBau einen Draconiumkern",
          subtitle="Das Bauteil für fast alles.",
          description=[
              "&6Draconiumbarren&r in die vier Ecken, &6Deepsilver&r aus Eternal Starlight an die vier Seiten, ein &6Diamant&r in die Mitte.",
              "",
              pic("components/draconium_core"),
              "",
              "Fusionskern, Injektoren, Generator, Pylonen, Partikelgenerator und alle Kerne der Wyvern-Stufe brauchen einen oder mehrere davon. Mach gleich acht.",
          ],
          tasks=[task_item("draconicevolution:draconium_core", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 16), reward_xp(5)],
          deps=["ingot"], icon="draconicevolution:draconium_core", size=1.5, shape="square"),

    # ---- Nuetzliches --------------------------------------------------------------
    quest("dislocator", 0, 6, "&bBau einen Dislocator",
          subtitle="Ein Sprung zurück an einen festen Ort.",
          description=[
              "&6Lohenstaub&r in die Ecken, &6Draconiumstaub&r an die Seiten, eine &6Verstärkte Echoscherbe&r aus Deeper and Darker in die Mitte.",
              "",
              "Schleichen und Rechtsklick speichert Ort, Blickrichtung und Dimension. Danach bringt dich ein Rechtsklick dorthin zurück. Er hat nur eine begrenzte Zahl an Ladungen.",
          ],
          tasks=[task_item("draconicevolution:dislocator", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["dust"], icon="draconicevolution:dislocator", optional=True),

    quest("magnet", 2.5, 6, "&bBau einen Item-Magneten",
          subtitle="Was am Boden liegt, kommt zu dir.",
          description=[
              "Oben zwei &6Redstone&r, in der Mitte zwei &6Draconiumbarren&r links und rechts, unten &6Eisen&r, &6Dislocator&r, &6Eisen&r.",
              "",
              "Der &bItem-Dislocator&r zieht Gegenstände in deiner Nähe zu dir. Eine Taste schaltet ihn an und aus, praktisch an der Monsterfarm oder beim Abbauen im End.",
          ],
          tasks=[task_item("draconicevolution:magnet", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["dislocator"], icon="draconicevolution:magnet", optional=True),

    quest("generator", 5, 6, "&6Bau einen Generator",
          subtitle="Ein Ofen, der Strom macht.",
          description=[
              "&6Netherziegel&r in die Ecken, &6Eisen&r an die Seiten, ein &6Ofen&r in die Mitte, ein &6Draconiumkern&r unten in die Mitte.",
              "",
              "Er verbrennt alles, was im Ofen brennt. &eEco&r und &eEco Plus&r holen mehr aus dem Brennstoff, &ePerformance&r und &eOverdrive&r geben mehr Leistung. Für Fusion und Energiekern reicht er nicht, als Notstrom schon.",
          ],
          tasks=[task_item("draconicevolution:generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8)],
          deps=["core"], icon="draconicevolution:generator", optional=True),

    quest("grinder", 7.5, 6, "&cBau einen Mob-Grinder",
          subtitle="Tötet Monster in einem Bereich.",
          description=[
              "&6Eisen&r in die Ecken, oben ein &6Draconiumbarren&r, links und rechts ein &6Diamantschwert&r, in der Mitte ein &6Wyvern-Energiekontroller&r, unten ein beliebiger &6Kopf&r.",
              "",
              "Mit Strom tötet er Monster in seinem Bereich, &eShow AOE&r zeigt ihn. Er braucht &e80 Energie pro Lebenspunkt&r des Monsters. Eine Waffe im Slot bringt ihre Verzauberungen mit.",
              "",
              "&eCollect Items&r schiebt die Beute in ein Inventar daneben, &eCollect XP&r speichert die Erfahrung. Unter einen Spawner gestellt erspart er dir das Schlagen.",
          ],
          tasks=[task_item("draconicevolution:grinder", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16)],
          deps=["generator", "w_energy"], icon="draconicevolution:grinder", optional=True),

    quest("adv_dislocator", 10, 6, "&bFusionier einen Fortgeschrittenen Dislocator",
          subtitle="Viele Orte und kurze Sprünge.",
          description=[
              "Fusion, Stufe Wyvern: &6Dislocator&r im Kern, in acht Injektoren &63 Enderperlen&r, &64 Draconiumbarren&r und &61 Wyvern-Kern&r. Kostet 1 Million Energie.",
              "",
              "Er merkt sich eine ganze Liste von Orten und tankt Enderperlen. Dazu kann er &ekurz springen&r: bis 32 Blöcke weit, eine Perle reicht für 4 Sprünge.",
          ],
          tasks=[task_item("draconicevolution:advanced_dislocator", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_xp(5)],
          deps=["dislocator", "w_injector"], icon="draconicevolution:advanced_dislocator", optional=True),

    # ---- Fusion -------------------------------------------------------------------
    quest("crafting_core", 0, 10.5, "&dBau einen Fusionskern",
          subtitle="Die Werkbank von Draconic Evolution.",
          description=[
              "&eRezept auf Kronwerke:&r &6Quelljuwelblöcke&r von Ars Nouveau in die Ecken, &6Diamanten&r an die Seiten, ein &6Draconiumkern&r in die Mitte.",
              "",
              "In den Kern kommt der &eKatalysator&r, das Teil, das verwandelt wird. Um ihn herum stehen &eInjektoren&r mit je einer Zutat. Den Strom bekommen die Injektoren, nicht der Kern. Im Fenster des Kerns drückst du auf &eCraft&r.",
          ],
          tasks=[task_item("draconicevolution:crafting_core", 1)],
          rewards=[reward_item("ars_nouveau:source_gem_block", 4), reward_xp(5)],
          deps=["core"], icon="draconicevolution:crafting_core"),

    quest("injectors", 2.5, 10.5, "&dStell acht Draconium-Injektoren auf",
          subtitle="Jeder hält eine Zutat.",
          description=[
              "Oben &6Diamant, Draconiumkern, Diamant&r, in der Mitte &6Stein, Eisenblock, Stein&r, unten drei &6Stein&r.",
              "",
              "Jeder Injektor zeigt mit der Spitze zum Kern, &emindestens 2&r und &ehöchstens 16 Blöcke&r entfernt. Zu nah meldet der Kern &e\"One or more injectors are too close!\"&r. Jeder Injektor braucht ein Stromkabel.",
              "",
              "Ein Rezept braucht so viele Injektoren, wie es Zutaten hat. Mit Draconium-Injektoren lädt eine Fusion 15 Sekunden und craftet 15 Sekunden.",
          ],
          tasks=[task_item("draconicevolution:basic_crafting_injector", 8)],
          rewards=[reward_item("minecraft:iron_block", 4), reward_table("s4_common")],
          deps=["crafting_core"], icon="draconicevolution:basic_crafting_injector"),

    quest("w_core", 5, 9.6, "&dBau einen Wyvern-Kern",
          subtitle="Ein Netherstern im Draconium.",
          description=[
              "&6Draconiumbarren&r in die Ecken, &64 Draconiumkerne&r an die Seiten, ein &6Netherstern&r in die Mitte.",
              "",
              pic("components/wyvern_core"),
              "",
              "Jeder Kern kostet einen &5Wither&r. Für den Anfang brauchst du zwei: einen für den Wyvern-Injektor, einen für den Energiekern.",
          ],
          tasks=[task_item("draconicevolution:wyvern_core", 2)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_xp(10)],
          deps=["core"], icon="draconicevolution:wyvern_core"),

    quest("w_injector", 5, 11.5, "&d&lFusionier einen Wyvern-Injektor",
          subtitle="Deine erste Fusion.",
          description=[
              "Katalysator: ein &6Draconium-Injektor&r. In acht Injektoren: &61 Wyvern-Kern&r, &62 Draconiumkerne&r, &64 Diamanten&r, &61 Draconiumblock&r. Kostet 32 000 Energie.",
              "",
              "Wyvern-Werkzeuge und die Brustplatte brauchen &esechs&r Wyvern-Injektoren, der Kondensator acht. Fehlen welche, meldet der Kern &e\"Not enough wyvern tier injectors\"&r.",
              "",
              "Ein Wyvern-Injektor kann auch alle Draconium-Rezepte und lädt schneller (11 statt 15 Sekunden). Mit acht kannst du die alten ganz ersetzen.",
          ],
          tasks=[task_item("draconicevolution:wyvern_crafting_injector", 6)],
          rewards=[reward_item("minecraft:diamond", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["injectors", "w_core"], icon="draconicevolution:wyvern_crafting_injector", size=1.5, shape="diamond"),

    quest("w_capacitor", 7.5, 11.5, "&dFusionier einen Wyvern-Kondensator",
          subtitle="Ein Akku für Werkzeug und Rüstung.",
          description=[
              "Katalysator: ein &6Wyvern-Kern&r. In acht Injektoren: &64 Wyvern-Energiekontroller&r und &64 Draconiumbarren&r. Kostet 8 Millionen Energie.",
              "",
              "Er lädt Werkzeuge und Rüstung in deinem Inventar. Lade ihn selbst an einem Pylon oder einer Ladestation auf.",
          ],
          tasks=[task_item("draconicevolution:wyvern_capacitor", 1)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(10)],
          deps=["w_injector", "w_energy"], icon="draconicevolution:wyvern_capacitor", optional=True),

    # ---- Der Energiekern ----------------------------------------------------------
    quest("w_energy", 0, 16, "&cBau Wyvern-Energiekontroller",
          subtitle="Das Herz jedes Akkus.",
          description=[
              "&6Draconiumbarren&r in die Ecken, &6Redstoneblöcke&r an die Seiten, ein &6Draconiumkern&r in die Mitte.",
              "",
              pic("components/wyvern_energy_core"),
              "",
              "Er steckt im Energiekern (zwei), im Mob-Grinder, in den Relaiskristallen und in jedem Wyvern-Werkzeug. Mach mehr, als du denkst.",
          ],
          tasks=[task_item("draconicevolution:wyvern_energy_core", 2)],
          rewards=[reward_item("minecraft:redstone_block", 8)],
          deps=["core"], icon="draconicevolution:wyvern_energy_core"),

    quest("energy_core", 2.5, 16, "&c&lBau den Energiekern",
          subtitle="Stufe 1 speichert 45,5 Millionen.",
          description=[
              "Oben und unten je drei &6Draconiumbarren&r, in der Mitte &6Wyvern-Energiekontroller, Wyvern-Kern, Wyvern-Energiekontroller&r.",
              "",
              "Der Block allein ist &eStufe 1&r und speichert &e45 500 000&r Energie. Er läuft erst mit vier Stabilisatoren, die kommen als Nächstes.",
          ],
          tasks=[task_item("draconicevolution:energy_core", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["w_energy", "w_core"], icon="draconicevolution:energy_core", size=1.75, shape="hexagon"),

    quest("particle", 2.5, 14, "&cBau Partikelgeneratoren",
          subtitle="Einer pro Stabilisator.",
          description=[
              "&6Redstoneblöcke&r in die Ecken, &6Lohenruten&r an die Seiten, ein &6Draconiumkern&r in die Mitte.",
              "",
              "Vier Stück, für jeden Stabilisator einen. Die Lohenruten holst du aus dem Nether.",
          ],
          tasks=[task_item("draconicevolution:particle_generator", 4)],
          rewards=[reward_item("minecraft:blaze_rod", 8), reward_xp(5)],
          deps=["core"], icon="draconicevolution:particle_generator"),

    quest("stabilizer", 5, 15, "&c&lBau vier Stabilisatoren mit Gaia",
          subtitle="Der Drachenspeicher braucht Gaia.",
          description=[
              "&eRezept auf Kronwerke:&r oben in der Mitte eine &aGaia-Seele&r, &6Diamanten&r in die vier Ecken, der &6Partikelgenerator&r in die Mitte.",
              "",
              "Vier Stabilisatoren sind vier Gaia-Seelen. Die gibt es nur vom &aWächter von Gaia&r: jeder Spieler im Kampf bekommt 6, wer den letzten Schlag setzt, 8. Ein Kampf mit den Magiern reicht also.",
              "",
              "&eAufstellen:&r in einer Ebene auf vier Seiten des Kerns, genau in Linie mit seiner Mitte, außerhalb seiner Blöcke, zum Kern zeigend. Falsch meldet &e\"Stabilizer configuration invalid\"&r. Dann &eActivate&r.",
          ],
          tasks=[task_item("draconicevolution:energy_core_stabilizer", 4)],
          rewards=[reward_item("minecraft:diamond", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["particle", "energy_core"], icon="draconicevolution:energy_core_stabilizer", size=1.5, shape="diamond"),

    quest("pylon", 7.5, 14, "&cSetz zwei Energiepylonen",
          subtitle="Rein in den Kern, raus aus dem Kern.",
          description=[
              "&6Draconiumbarren&r in die Ecken, oben ein &6Enderauge&r, an den Seiten &6Smaragde&r, in der Mitte ein &6Draconiumkern&r, unten ein &6Diamant&r. Gibt zwei.",
              "",
              "Stell den Pylon in die Nähe des Kerns und setz einen &eGlasblock&r direkt darüber oder darunter. Ein Pylon nimmt Strom auf oder gibt ihn ab, die Richtung schaltest du am Pylon um. Ein Komparator daran zeigt, wie voll der Kern ist.",
          ],
          tasks=[task_item("draconicevolution:energy_pylon", 2)],
          rewards=[reward_item("minecraft:emerald", 8), reward_xp(5)],
          deps=["stabilizer"], icon="draconicevolution:energy_pylon"),

    tier("tier2", 7.5, 16, "&cKern Stufe 2", "6 Blöcke, 273 Millionen.",
         "&66 Draconiumblöcke&r, einer an jede Seite des Kerns.", "&e273 000 000&r Energie.", ["stabilizer"],
         task=task_item("draconicevolution:draconium_block", 6),
         reward=[reward_item("minecraft:redstone_block", 8), reward_xp(10)]),
    tier("tiers", 10, 16, "&cKern Stufe 3", "26 Blöcke, 1,64 Milliarden.",
         "&626 Draconiumblöcke&r als voller Würfel um den Kern.", "&e1 640 000 000&r Energie.", ["tier2"],
         extra=("", "&eTipp:&r Blöcke im Kern zählen nicht für den Obelisken. Plant gemeinsam, wie viel Draconium in Kerne geht."),
         task=task_item("draconicevolution:draconium_block", 26),
         reward=[reward_item("minecraft:redstone_block", 16), reward_xp(15)]),
    tier("tier4", 12.5, 16, "&cKern Stufe 4", "54 und 26 Blöcke, 9,88 Milliarden.",
         "&654 Draconiumblöcke&r außen, &626 Redstoneblöcke&r innen.", "&e9 880 000 000&r Energie.", ["tiers"],
         reward=[reward_item("minecraft:redstone_block", 16), reward_xp(15)]),
    tier("tier5", 15, 16, "&cKern Stufe 5", "90 und 80 Blöcke, 59,3 Milliarden.",
         "&690 Draconiumblöcke&r und &680 Redstoneblöcke&r.", "&e59 300 000 000&r Energie.", ["tier4"],
         extra=("", "Ab den großen Stufen verlangt das Fenster &e(Advanced stabilizers required)&r. Was dafür zu bauen ist, zeigt dann die Bauanleitung."),
         reward=[reward_item("draconicevolution:draconium_block", 4), reward_xp(20)]),
    tier("tier6", 17.5, 16, "&cKern Stufe 6", "150 und 178 Blöcke, 356 Milliarden.",
         "&6150 Draconiumblöcke&r und &6178 Redstoneblöcke&r.", "&e356 000 000 000&r Energie.", ["tier5"],
         reward=[reward_item("draconicevolution:draconium_block", 8), reward_xp(25)]),
    tier("tier7", 20, 16, "&cKern Stufe 7", "210 und 328 Blöcke, 2,14 Billionen.",
         "&6210 Draconiumblöcke&r und &6328 Redstoneblöcke&r.", "&e2 140 000 000 000&r Energie.", ["tier6"],
         extra=("", "Stufe 8 braucht 378 Erwachte und 786 normale Draconiumblöcke und hat keine Grenze mehr. Sie kommt in Stufe 5."),
         reward=[reward_item("draconicevolution:draconium_block", 16), reward_xp(30)]),

    # ---- Wyvern-Ausruestung -------------------------------------------------------
    quest("relay", 0, 21, "&bBau Relaiskristalle",
          subtitle="Ein Zwischenteil für Wyvern-Rezepte.",
          description=[
              "Vier &6Diamanten&r im Plus um einen &6Wyvern-Energiekontroller&r. Gibt vier &bEinfache Relaiskristalle&r.",
              "",
              "Jedes Wyvern-Werkzeug und die Brustplatte brauchen zwei. Eigentlich sind die Kristalle ein kabelloses Stromnetz, das du mit dem Kristallbinder verknüpfst. Hier brauchst du sie nur als Zutat.",
          ],
          tasks=[task_item("draconicevolution:basic_relay_crystal", 4)],
          rewards=[reward_item("minecraft:diamond", 4)],
          deps=["w_injector", "w_energy"], icon="draconicevolution:basic_relay_crystal"),

    quest("tools", 2.5, 21, "&d&lFusionier eine Wyvern-Spitzhacke",
          subtitle="Werkzeug mit Strom und Modulen.",
          description=[
              "Sechs Wyvern-Injektoren. Katalysator: eine &6Diamantspitzhacke&r. In die Injektoren: &61 Draconiumkern&r, &62 Draconiumbarren&r, &62 Relaiskristalle&r, &61 Wyvern-Energiekontroller&r. Kostet 8 Millionen Energie.",
              "",
              "Sie läuft mit Strom und geht nicht kaputt. Die Taste &eTool Modules&r (Steuerung, Draconic Evolution) öffnet ihr Modul-Raster.",
          ],
          tasks=[task_item("draconicevolution:wyvern_pickaxe", 1)],
          rewards=[reward_item("draconicevolution:draconium_core", 2), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["relay"], icon="draconicevolution:wyvern_pickaxe", size=1.75, shape="gear"),

    quest("sword", 5, 20, "&dFusionier ein Wyvern-Schwert",
          subtitle="Gleiches Rezept, Diamantschwert im Kern.",
          description=[
              "Wie die Spitzhacke, nur mit einem &6Diamantschwert&r als Katalysator. Axt, Schaufel und Hacke gehen genauso mit dem passenden Diamantwerkzeug.",
              "",
              "Mit Schadensmodulen ist es für den Rest von Stufe 4 deine Waffe.",
          ],
          tasks=[task_item("draconicevolution:wyvern_sword", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_xp(10)],
          deps=["tools"], icon="draconicevolution:wyvern_sword", optional=True),

    quest("bow", 7.5, 20, "&dFusionier einen Wyvern-Bogen",
          subtitle="Mit einem normalen Bogen im Kern.",
          description=[
              "Wie die Spitzhacke, nur mit einem &6Bogen&r als Katalysator.",
              "",
              "Der Bogen ist die Vorstufe zum Drakonischen Bogen aus Stufe 5, der Waffe gegen den Chaoswächter. Projektil-Module für Schaden, Tempo und Genauigkeit gibt es schon in der Wyvern-Stufe.",
          ],
          tasks=[task_item("draconicevolution:wyvern_bow", 1)],
          rewards=[reward_item("minecraft:arrow", 64), reward_xp(10)],
          deps=["sword"], icon="draconicevolution:wyvern_bow", optional=True),

    quest("armor", 2.5, 23, "&dFusionier die Wyvern-Brustplatte",
          subtitle="Ein Schild aus Energie.",
          description=[
              "Wie die Werkzeuge, mit einer &6Diamantbrustplatte&r als Katalysator.",
              "",
              "Sie ist das einzige Rüstungsteil der Wyvern-Stufe und trägt einen &eSchild&r, der Schaden mit Strom abfängt. Wie stark, bestimmen die Module darin.",
          ],
          tasks=[task_item("draconicevolution:wyvern_chestpiece", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_xp(10)],
          deps=["relay"], icon="draconicevolution:wyvern_chestpiece"),

    quest("modules", 5, 22, "&dBau Modulkerne",
          subtitle="Die Grundlage jedes Moduls.",
          description=[
              "&6Eisen&r in die Ecken, &6Redstone&r oben und unten, &6Gold&r links und rechts, ein &6Draconiumbarren&r in die Mitte.",
              "",
              "Aus ihm werden die Module: AOE, Speed, Damage, Junk Filter, Night Vision, Undying und mehr. Die Rezepte zeigt JEI. Wyvern-Module passen in Wyvern-Ausrüstung.",
          ],
          tasks=[task_item("draconicevolution:module_core", 4)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 4)],
          deps=["tools"], icon="draconicevolution:module_core", optional=True),

    quest("shield_mod", 5, 24, "&dBau ein Wyvern-Schildmodul",
          subtitle="Ein größerer Schild.",
          description=[
              "&6Draconiumbarren&r in die Ecken, &6Netherit-Bruchstücke&r oben und unten, &6Glowstonestaub&r links und rechts, ein &6Modulkern&r in die Mitte.",
              "",
              "Steck es in die Brustplatte. Fünf kleine ergeben über ein Rezept mit Draconiumkernen ein großes, und ein großes lässt sich wieder in fünf zerlegen.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_shield_capacity", 1)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_xp(5)],
          deps=["armor", "modules"], icon="draconicevolution:item_wyvern_shield_capacity", optional=True),

    quest("flight", 7.5, 24, "&dBau ein Wyvern-Flugmodul",
          subtitle="Fliegen ohne Elytra auf dem Rücken.",
          description=[
              "&6Draconiumbarren&r in die Ecken, oben eine &6Elytra&r, unten eine &6Feuerwerksrakete&r, links und rechts ein &6Draconiumkern&r, in der Mitte ein &6Modulkern&r.",
              "",
              "In der Brustplatte lässt es dich fliegen. Die Elytra findest du auf den Endschiffen.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_flight", 1)],
          rewards=[reward_item("minecraft:firework_rocket", 16), reward_xp(10)],
          deps=["shield_mod"], icon="draconicevolution:item_wyvern_flight", optional=True),

    # ---- Fuer den Obelisken -------------------------------------------------------
    quest("goal", 10, 21, "&5&lBring Licht des Drachen zum Obelisken",
          subtitle="Tausend Barren für den Technik-Pfeiler.",
          description=[
              "Leite &6Draconiumbarren&r und &6Elite-Steuerschaltkreise&r in eine Kiste am Obelisken. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eKronwerke:&r Das Technikziel von Stufe 4 heißt &e1 000 Draconiumbarren&r und &e150 Elite-Steuerschaltkreise&r. Der Magie-Pfeiler will 128 Gaia-Seelen und 30 Mystische Stäbe.",
              "",
              "&eStraße:&r mit Glück III abbauen, Staub per Trichter in Öfen oder einen Schmelzer, Barren direkt in die Kiste. Den Endstein aufheben, die Magier brauchen ihn. Steinbrüche im End: Kapitel &6Steinbrüche&r.",
          ],
          tasks=[task_item("draconicevolution:draconium_ingot", 256), task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["tiers", "pylon", "tools"], icon="draconicevolution:draconium_block", size=2.0, shape="gear"),

    quest("outlook", 12.5, 21, "&8Schau auf Erwacht und Chaos",
          subtitle="Was in Stufe 5 kommt.",
          description=[
              "&eRezept auf Kronwerke:&r &6Erwachtes Draconium&r ist eine Fusion aus 4 Draconiumblöcken, 4 Draconiumkernen, einem &5Drachenherz&r und &a2 Gaia-Seelenbarren&r. Heb dir Drachenherzen auf.",
              "",
              "Dazu Drakonische Ausrüstung, Stufe 8 des Kerns, der Reaktor und der Chaoswächter. Alles im Kapitel &5Draconic: Erwacht und Chaos&r. Das Ziel von Stufe 5 will &e64 Erwachte Draconiumblöcke&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["goal"], icon="draconicevolution:draconium_core", optional=True),

    # ---- Nuetzliches, neu ---------------------------------------------------------
    quest("player_dislocator", 0, 7.5, "&bBau einen Spieler-Dislocator",
          subtitle="Ein Sprung zu deinem Mitspieler.",
          description=[
              "Formlos: ein &6Dislocator&r, ein &6Draconiumkern&r und eine &6Ghast-Träne&r. Mit zwei Dislocatoren statt einem wird es die Punkt-zu-Punkt-Version, die zwei Dislocatoren miteinander verbindet.",
              "",
              "Rechtsklick bindet ihn an dich. Gib ihn einem Mitspieler: Mit einem Rechtsklick landet er bei dir, solange du online bist. Die Zahl der Sprünge ist begrenzt.",
              "",
              "Praktisch, wenn jemand im End verloren geht oder die Gruppe sich vor einem Kampf sammelt.",
          ],
          tasks=[task_item("draconicevolution:player_dislocator_unbound", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 2), reward_xp(5)],
          deps=["dislocator"], icon="draconicevolution:player_dislocator_unbound", optional=True),

    quest("disenchanter", 2.5, 7.5, "&dBau einen Entzauberer",
          subtitle="Verzauberungen zurück aufs Buch.",
          description=[
              "&6Smaragde&r oben links und rechts, ein &6Draconiumkern&r oben in der Mitte, zwei &6Verzauberte Bücher&r links und rechts, ein &6Zaubertisch&r in die Mitte, drei &6Bücherregale&r unten.",
              "",
              "Leg ein verzaubertes Teil und Bücher hinein und wähl eine Verzauberung. Sie wandert auf ein Buch, das kostet &eErfahrungslevel&r. So rettest du Verzauberungen von alter Ausrüstung, bevor du sie zur Wyvern-Ausrüstung fusionierst.",
          ],
          tasks=[task_item("draconicevolution:disenchanter", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(5)],
          deps=["core"], icon="draconicevolution:disenchanter", optional=True),

    quest("celestial", 5, 7.5, "&eBau einen Himmelsmanipulator",
          subtitle="Tag, Nacht und Wetter auf Knopfdruck.",
          description=[
              "&6Redstoneblöcke&r oben links und rechts, eine &6Uhr&r oben in der Mitte, &6Draconiumbarren&r links und rechts, ein &5Drachenei&r in die Mitte, unten &6Eisen, Wyvern-Kern, Eisen&r.",
              "",
              "Mit Strom springt er zu Sonnenaufgang, Mittag, Sonnenuntergang oder Mitternacht, oder er macht Regen, Gewitter oder klaren Himmel. Das Ei bekommst du von jedem Drachen neu.",
          ],
          tasks=[task_item("draconicevolution:celestial_manipulator", 1)],
          rewards=[reward_item("minecraft:clock", 1), reward_xp(8)],
          deps=["w_core"], icon="draconicevolution:celestial_manipulator", optional=True),

    quest("chest", 7.5, 7.5, "&6Fusionier eine Draconiumtruhe",
          subtitle="Eine riesige Truhe mit eigenem Ofen.",
          description=[
              "Fusion, Stufe Draconium: eine &6Truhe&r im Kern. In zehn Injektoren: &65 Öfen&r, &62 Draconiumkerne&r, &62 Werkbänke&r und &61 Draconiumblock&r. Kostet 2 Millionen Energie.",
              "",
              "Sie fasst weit mehr als eine Doppeltruhe und hat einen eingebauten Ofen mit Strom. &eAuto-Smelt&r schickt alles Schmelzbare hinein, oder nur das, was schon geschmolzen wird. Die Farbe stellst du im Fenster ein.",
          ],
          tasks=[task_item("draconicevolution:draconium_chest", 1)],
          rewards=[reward_item("minecraft:coal_block", 8), reward_xp(8)],
          deps=["injectors"], icon="draconicevolution:draconium_chest", optional=True),

    quest("crystals", 5, 13.5, "&bVerteil Strom ohne Kabel",
          subtitle="Kristallbinder und Energiekristalle.",
          description=[
              "&6Kristallbinder:&r ein &6Draconiumkern&r unten links, ein &6Lohenstab&r in die Mitte, Draconiumbarren daneben und darüber, ein &6Diamant&r oben rechts. Ein Relaiskristall formlos gibt zwei &6E/A-Kristalle&r.",
              "",
              "Setz einen E/A-Kristall an den Pylon, einen an die Maschine. Schleich-Rechtsklick mit dem Binder auf den ersten, dann Rechtsklick auf den zweiten: Der Strom fließt durch die Luft. Relaiskristalle verteilen weiter, ein &6Drahtloser Kristall&r versorgt Blöcke ganz ohne Kristall daran.",
          ],
          tasks=[task_item("draconicevolution:crystal_binder", 1), task_item("draconicevolution:basic_io_crystal", 2)],
          rewards=[reward_item("draconicevolution:basic_relay_crystal", 2), reward_xp(8)],
          deps=["pylon", "relay"], icon="draconicevolution:crystal_binder", optional=True),

    # ---- Module -------------------------------------------------------------------
    quest("mod_energy", 0, 27.5, "&dBau ein Wyvern-Energiemodul",
          subtitle="Mehr Akku für Werkzeug und Rüstung.",
          description=[
              "&6Energiemodul:&r sechs &6Redstoneblöcke&r oben und unten, Eisen, Modulkern, Eisen in der Mitte. &6Wyvern-Energiemodul:&r sechs Draconiumbarren oben und unten, Energiemodul, Draconiumkern, Energiemodul in der Mitte.",
              "",
              "Das einfache Modul speichert &d1 Million&r, das Wyvern-Modul &d4 Millionen&r Energie. Jedes Modul braucht Strom, also kommt das hier zuerst in jedes Raster.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_energy", 1)],
          rewards=[reward_item("minecraft:redstone_block", 8), reward_xp(6)],
          deps=["modules"], icon="draconicevolution:item_wyvern_energy"),

    quest("mod_aoe", 2.5, 27.5, "&dBau ein Wyvern-AOE-Modul",
          subtitle="5 x 5 auf einen Schlag.",
          description=[
              "&6AOE-Modul:&r Kolben in die Ecken, Draconiumbarren oben und unten, Draconiumkerne links und rechts, ein Modulkern in die Mitte. Zwei davon mit einem &6Wyvern-Kern&r, vier Draconiumbarren und zwei &6Netherit-Bruchstücken&r ergeben das Wyvern-Modul.",
              "",
              "Das einfache Modul baut &e3 x 3&r ab, das Wyvern-Modul &e5 x 5&r. Die Größe stellst du im Werkzeug ein. Der &eAOE Safe Mode&r bricht ab, sobald eine Maschine im Bereich steht.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_aoe", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_xp(8)],
          deps=["mod_energy"], icon="draconicevolution:item_wyvern_aoe"),

    quest("mod_junk", 5, 27.5, "&dHalte dein Inventar sauber",
          subtitle="Verbrennen oder in die Endertruhe.",
          description=[
              "&6Selektive Verbrennung:&r Draconiumbarren in die Ecken, ein &6Lavaeimer&r oben, Draconiumkerne links und rechts, Modulkern in die Mitte, Redstone unten. Was du im Filter einstellst, wird beim Aufheben verbrannt: Bruchstein, Erde, Endstein.",
              "",
              "&6Ender-Sammelmodul:&r Enderaugen in die Ecken, ein Draconiumkern oben, Draconiumbarren links und rechts, Modulkern in die Mitte, eine &6Endertruhe&r unten. Abgebautes landet direkt in deiner Endertruhe.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_junk_filter", 1)],
          rewards=[reward_item("minecraft:lava_bucket", 1), reward_xp(5)],
          deps=["mod_energy"], icon="draconicevolution:item_wyvern_junk_filter", optional=True),

    quest("mod_tree", 7.5, 27.5, "&dFäll ganze Bäume",
          subtitle="Der Wyvern-Baumfäller für die Axt.",
          description=[
              "Draconiumbarren in die Ecken, &6Diamantäxte&r oben und unten, Draconiumkerne links und rechts, ein Modulkern in die Mitte. Fusionier dazu eine &6Wyvern-Axt&r wie die Spitzhacke, mit einer Diamantaxt im Kern.",
              "",
              "Rechte Maustaste auf einem Baum gedrückt halten fällt ihn ganz. Das Modul reicht &e16 Blöcke&r weit und schafft &e5 Blöcke pro Sekunde&r. Blätter nimmt es mit, wenn du es einstellst.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_tree_harvest", 1), task_item("draconicevolution:wyvern_axe", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(8)],
          deps=["mod_energy", "tools"], icon="draconicevolution:item_wyvern_tree_harvest", optional=True),

    quest("mod_undying", 10, 27.5, "&dBau ein Wyvern-Untod-Modul",
          subtitle="Ein zweites Leben in der Brustplatte.",
          description=[
              "Draconiumbarren in die Ecken, ein &6Totem der Unsterblichkeit&r oben, Draconiumkerne links und rechts, Modulkern in die Mitte, ein &6Wyvern-Schildmodul&r unten.",
              "",
              "Ein tödlicher Treffer löst es aus: &d6 Lebenspunkte&r zurück, &d2 Sekunden&r unverwundbar und ein kräftiger Schildschub. Danach lädt es &d120 Sekunden&r lang mit 5 Millionen Energie nach.",
              "",
              "Es ist auch die Zutat für das drakonische Untod-Modul aus Stufe 5.",
          ],
          tasks=[task_item("draconicevolution:item_wyvern_undying", 1)],
          rewards=[reward_item("minecraft:totem_of_undying", 1), reward_table("s4_common"), reward_xp(10)],
          deps=["shield_mod", "mod_energy"], icon="draconicevolution:item_wyvern_undying"),
]

images = [
    head("title", "Draconic Evolution", 0, -2.6, height=1.6, kind="title"),
    head("stage", "Stufe 4: Sternwerk", 0, -1.2, height=0.55, kind="note", colour="stone"),
    head("draconium", "Draconium", 3.6, -0.6),
    head("nuetzlich", "Nützliches", 0, 4.6, colour="brass"),
    head("fusion", "Fusion", 0, 9.1, colour="brass"),
    head("kern", "Der Energiekern", 0, 13.0, colour="fire"),
    head("tiers", "Kernstufen", 10, 14.6, colour="fire"),
    head("wyvern", "Wyvern-Ausrüstung", 0, 18.9),
    head("obelisk", "Für den Obelisken", 10, 18.9, colour="brass"),
    head("module", "Module", 0, 25.8),
]

chapter(C, "Draconic Evolution", "draconicevolution:draconium_core", "tech", quests, shape="circle", order=38, stage=4,
        subtitle=["Stufe 4. Draconium aus dem End, Fusion Schritt für Schritt, der Energiekern und die Wyvern-Stufe."],
        images=images)
