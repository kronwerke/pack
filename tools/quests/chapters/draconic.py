"""Draconic Evolution in stage 4: draconium from the End (dust, ingots, blocks), the draconium
core, fusion crafting (core, draconium and wyvern injectors), the energy core with its
stabilizers (Kronwerke: a Gaia spirit each) and pylons, the wyvern core, wyvern tools, armor and
modules, the dislocator, the generator and the grinder, and the stage 4 tech goal (1 000
draconium ingots, elite circuits). Awakened and chaotic tiers are stage 5 and text only.
Recipes follow the Draconic Evolution jar and kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img)

C = "draconic"


def pic(path, size=32):
    """A Draconic Evolution item texture inside a quest text."""
    return img(f"draconicevolution:textures/item/{path}.png", size, size)


quests = [
    # ---- Draconium ----------------------------------------------------------------
    quest("dust", 0, 0, "&5&lDraconium",
          subtitle="Ein lila Erz, das nur im End wächst.",
          description=[
              "Mit &6Stufe 4 (Sternwerk)&r öffnet sich das End, und mit ihm &5Draconic Evolution&r. Alles in diesem Kapitel beginnt mit einem Erz: &5Ender-Draconiumerz&r.",
              "",
              pic("components/draconium_dust"),
              "",
              "&eWo:&r Nur im End, im Endstein zwischen Höhe 0 und 70, in Adern bis zu acht Blöcken. Auf der Hauptinsel und auf den äußeren Inseln. Die Erze in Oberwelt und Nether sind auf Kronwerke abgeschaltet.",
              "",
              "&eWas es fallen lässt:&r 2 bis 4 &5Draconiumstaub&r, Glück erhöht die Menge. Mit Behutsamkeit bekommst du das Erz selbst, das im Ofen nur einen Barren gibt. Bau also mit &6Glück III&r ab.",
              "",
              "&eWas noch wartet:&r die erwachte Stufe (Awakened Draconium, Draconic-Werkzeuge) und die chaotische Stufe kommen in Stufe 5.",
          ],
          tasks=[task_item("draconicevolution:draconium_dust", 16)],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_table("s4_common"), reward_xp(10)],
          icon="draconicevolution:draconium_dust", size=2.0, shape="hexagon"),

    quest("ingot", 2.75, 0, "&5Draconiumbarren",
          subtitle="Staub in den Ofen.",
          description=[
              "Ein &5Draconiumstaub&r schmilzt im Ofen zu einem &5Draconiumbarren&r. Neun Barren ergeben einen &5Draconiumblock&r, neun Nuggets einen Barren.",
              "",
              pic("components/draconium_ingot"),
              "",
              "Barren brauchst du ab jetzt überall: im Draconiumkern, in den Kernen der Wyvern-Stufe, im Energiekern und seinen Pylonen. Und die Lagerleute brauchen sie auch: &eRezept auf Kronwerke:&r die 256k-Komponente von AE2 und die MEGA-Komponenten für 1M und 4M haben je einen Draconiumbarren in der Mitte.",
          ],
          tasks=[task_item("draconicevolution:draconium_ingot", 32)],
          rewards=[reward_item("minecraft:diamond", 4), reward_xp(5)],
          deps=["dust"], icon="draconicevolution:draconium_ingot"),

    quest("elite", 2.75, -2.5, "&dElite-Steuerschaltkreis",
          subtitle="Draconium für Mekanism.",
          description=[
              "&eRezept auf Kronwerke:&r Ein &dElite-Steuerschaltkreis&r von Mekanism braucht &e2 Fortschrittliche Steuerschaltkreise&r, &e2 Verstärkte Legierung&r und &e1 Draconiumstaub&r. Alle anderen Wege zu diesem Schaltkreis gibt es nicht mehr.",
              "",
              "Damit hängt die ganze Elite-Stufe von Mekanism am End: Elite-Fabriken, die Injektionskammer und die Vervierfachung. Bring den Technikern also Staub mit, wenn du im End bist.",
              "",
              "&eKronwerke:&r Der Obelisk will in Stufe 4 &e150 Elite-Steuerschaltkreise&r im Technik-Pfeiler.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 4)],
          rewards=[reward_item("draconicevolution:draconium_dust", 8), reward_table("s4_common")],
          deps=["dust"], icon="mekanism:elite_control_circuit"),

    quest("core", 5.25, 0, "&5Draconiumkern",
          subtitle="Das Bauteil für fast alles.",
          description=[
              "Der &5Draconiumkern&r (Draconium Core) steckt in fast jedem Block dieser Mod.",
              "",
              pic("components/draconium_core"),
              "",
              "&eRezept:&r Draconiumbarren in die vier Ecken, Gold an die vier Seiten, ein Diamant in die Mitte.",
              "",
              "Mach dir gleich einen kleinen Vorrat. Fusionskern, Injektoren, Generator, Pylonen, Partikelgenerator und die Kerne der Wyvern-Stufe brauchen alle einen oder mehrere davon.",
          ],
          tasks=[task_item("draconicevolution:draconium_core", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 16), reward_xp(5)],
          deps=["ingot"], icon="draconicevolution:draconium_core", size=1.5, shape="square"),

    # ---- Nuetzliches --------------------------------------------------------------
    quest("dislocator", 2.75, 2.5, "&bDislocator",
          subtitle="Ein Sprung zurück zu einem festen Ort.",
          description=[
              "Der &bDislocator&r: Lohenstaub in die Ecken, Draconiumstaub an die Seiten, ein Enderauge in die Mitte.",
              "",
              pic("dislocator"),
              "",
              "&eSo geht's:&r Schleichen und Rechtsklick speichert deinen Ort, deine Blickrichtung und die Dimension. Danach bringt dich ein Rechtsklick dorthin zurück. Er hat nur eine begrenzte Zahl an Ladungen.",
              "",
              "Der &bFortgeschrittene Dislocator&r entsteht in der Fusion (Wyvern-Stufe) aus diesem Dislocator, Enderperlen, Draconiumbarren und einem Wyvern-Kern. Er merkt sich eine ganze Liste von Orten und tankt Enderperlen als Treibstoff.",
              "",
              "&eUnd der Item-Dislocator:&r Redstone, zwei Draconiumbarren, Eisen und ein Dislocator ergeben einen Magneten, der Items zu dir zieht. Eine Taste schaltet ihn an und aus.",
          ],
          tasks=[task_item("draconicevolution:dislocator", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["dust"], icon="draconicevolution:dislocator", optional=True),

    quest("generator", 5.25, 2.5, "&6Generator",
          subtitle="Ein Ofen, der Strom macht.",
          description=[
              "Der &6Generator&r von Draconic Evolution: Netherziegel in die Ecken, Eisen an die Seiten, ein Ofen in die Mitte und ein Draconiumkern unten in die Mitte.",
              "",
              "Er verbrennt alles, was auch im Ofen brennt, und macht daraus Strom. Im Fenster stellst du die Betriebsart ein: &eEco&r und &eEco Plus&r holen mehr aus dem Brennstoff, geben aber weniger Leistung, &ePerformance&r und &eOverdrive&r geben mehr Leistung und verbrauchen den Brennstoff schneller.",
              "",
              "Für die Fusion und den Energiekern brauchst du viel mehr Strom, als ein Generator liefert. Als Anfang oder als Notstrom taugt er aber.",
          ],
          tasks=[task_item("draconicevolution:generator", 1)],
          rewards=[reward_item("minecraft:coal_block", 8)],
          deps=["core"], icon="draconicevolution:generator", optional=True),

    quest("grinder", 5.25, 5, "&cMob-Grinder",
          subtitle="Tötet Monster in einem Bereich.",
          description=[
              "Der &cMob-Grinder&r: Eisen in die Ecken, oben ein Draconiumbarren, links und rechts ein Diamantschwert, in der Mitte ein &dWyvern-Energiekontroller&r und unten ein beliebiger Kopf.",
              "",
              "Mit Strom tötet er Monster in seinem Bereich. Wie groß der ist, stellst du im Fenster ein, &eShow AOE&r zeigt ihn an. In einen eigenen Slot kannst du eine Waffe legen, ihre Verzauberungen wirken dann mit.",
              "",
              "&eCollect Items&r sammelt die Beute ein und schiebt sie in ein Inventar daneben. &eCollect XP&r speichert die Erfahrung im Grinder, du holst sie dir mit einem Klick ab.",
              "",
              "&eTipp:&r Unter einem Mob-Spawner oder hinter einer Spawnfarm erspart er dir das Schlagen.",
          ],
          tasks=[task_item("draconicevolution:grinder", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16)],
          deps=["generator", "w_energy"], icon="draconicevolution:grinder", optional=True),

    # ---- Fusion -------------------------------------------------------------------
    quest("crafting_core", 7.75, 0, "&dFusionskern",
          subtitle="Die Werkbank von Draconic Evolution.",
          description=[
              "Die stärksten Dinge dieser Mod entstehen nicht an der Werkbank, sondern in der &dFusion&r. Ihr Herz ist der &dFusionskern&r (Fusion Crafting Core).",
              "",
              "&eRezept:&r Lapislazuliblöcke in die Ecken, Diamanten an die Seiten, ein Draconiumkern in die Mitte.",
              "",
              "&eSo funktioniert die Fusion:&r Der Kern bekommt den &eKatalysator&r, das Hauptteil, das verwandelt wird, zum Beispiel eine Diamantspitzhacke. Um ihn herum stehen &eInjektoren&r, jeder mit genau einer Zutat. Die Injektoren bekommen den &eStrom&r, nicht der Kern. Im Fenster des Kerns drückst du auf &eCraft&r, die Injektoren laden sich auf und schießen ihre Zutaten in den Kern.",
          ],
          tasks=[task_item("draconicevolution:crafting_core", 1)],
          rewards=[reward_item("minecraft:lapis_block", 4), reward_xp(5)],
          deps=["core"], icon="draconicevolution:crafting_core"),

    quest("injectors", 7.75, 2.5, "&dDraconium-Injektoren",
          subtitle="Jeder hält eine Zutat.",
          description=[
              "Ein &dDraconium-Fusionsinjektor&r: oben Diamant, Draconiumkern, Diamant, in der Mitte Stein, Eisenblock, Stein, unten drei Stein.",
              "",
              "&eSo stellst du sie auf:&r Jeder Injektor zeigt mit seiner Spitze in Richtung Kern. Direkt neben dem Kern geht es nicht, dann meldet der Kern &e\"One or more injectors are too close!\"&r. Lass also etwas Platz.",
              "",
              "Ein Rezept braucht so viele Injektoren, wie es Zutaten hat. Für den Wyvern-Injektor sind es acht. Jeder Injektor braucht Strom, also führ ein Kabel von Mekanism oder Powah an jeden heran.",
              "",
              "Die &eStufe&r des Rezepts steht im Fenster des Kerns. Ist sie höher als deine Injektoren, sagt er &e\"Injector tier too low\"&r.",
          ],
          tasks=[task_item("draconicevolution:basic_crafting_injector", 8)],
          rewards=[reward_item("minecraft:iron_block", 4), reward_table("s4_common")],
          deps=["crafting_core"], icon="draconicevolution:basic_crafting_injector"),

    quest("w_core", 10.25, 0, "&dWyvern-Kern",
          subtitle="Ein Netherstern im Draconium.",
          description=[
              "Der &dWyvern-Kern&r ist die nächste Stufe. &eRezept:&r Draconiumbarren in die Ecken, &e4 Draconiumkerne&r an die Seiten und ein &eNetherstern&r in die Mitte.",
              "",
              pic("components/wyvern_core"),
              "",
              "Jeder Wyvern-Kern kostet also einen &5Wither&r. Den Wither könnt ihr seit Stufe 2 beschwören, und mit Wyvern-Ausrüstung wird er später leichter. Für den Anfang brauchst du zwei Kerne: einen für den Wyvern-Injektor und einen für den Energiekern.",
          ],
          tasks=[task_item("draconicevolution:wyvern_core", 2)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_xp(10)],
          deps=["crafting_core"], icon="draconicevolution:wyvern_core"),

    quest("w_injector", 10.25, 2.5, "&dWyvern-Injektoren",
          subtitle="Die erste Fusion.",
          description=[
              "Der &dWyvern-Fusionsinjektor&r ist deine erste Fusion. Katalysator im Kern: ein &eDraconium-Injektor&r. In acht Injektoren: &e1 Wyvern-Kern&r, &e2 Draconiumkerne&r, &e4 Diamanten&r und &e1 Draconiumblock&r. Das kostet 32 000 Energie.",
              "",
              "Die Wyvern-Werkzeuge und die Wyvern-Rüstung sind Rezepte der Wyvern-Stufe. Dafür brauchst du &esechs Wyvern-Injektoren&r, für den Wyvern-Kondensator acht. Fehlen welche, meldet der Kern &e\"Not enough wyvern tier injectors\"&r.",
              "",
              "&eTipp:&r Ein Wyvern-Injektor kann auch Rezepte der Draconium-Stufe. Wenn du genug hast, kannst du die alten Injektoren also ganz ersetzen.",
          ],
          tasks=[task_item("draconicevolution:wyvern_crafting_injector", 6)],
          rewards=[reward_item("minecraft:diamond", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["injectors", "w_core"], icon="draconicevolution:wyvern_crafting_injector", size=1.5, shape="diamond"),

    # ---- Der Energiekern ----------------------------------------------------------
    quest("w_energy", 7.75, -2.5, "&cWyvern-Energiekontroller",
          subtitle="Ein Kern, der Strom speichert.",
          description=[
              "Der &cWyvern-Energiekontroller&r (Wyvern Energy Core): Draconiumbarren in die Ecken, Redstoneblöcke an die Seiten, ein Draconiumkern in die Mitte.",
              "",
              pic("components/wyvern_energy_core"),
              "",
              "Er steckt im Energiekern, im Mob-Grinder, in den Relaiskristallen und in jedem Wyvern-Werkzeug. Du brauchst also viele davon.",
          ],
          tasks=[task_item("draconicevolution:wyvern_energy_core", 2)],
          rewards=[reward_item("minecraft:redstone_block", 8)],
          deps=["core"], icon="draconicevolution:wyvern_energy_core"),

    quest("energy_core", 10.25, -3.75, "&c&lEnergiekern",
          subtitle="Ein Stromspeicher, der mit dir wächst.",
          description=[
              "Der &cEnergiekern&r (Energy Core) ist der große Stromspeicher von Draconic Evolution. &eRezept:&r oben und unten je drei Draconiumbarren, in der Mitte zwei Wyvern-Energiekontroller und ein Wyvern-Kern.",
              "",
              "Der Kern allein ist &eStufe 1&r. Öffne sein Fenster, stell mit &eTier Up&r die Stufe ein, die du bauen willst, und schalte &eToggle Build Guide&r an. Dann zeigt er dir, wo die Blöcke hingehören:",
              "&eStufe 2:&r 6 Draconiumblöcke an die sechs Seiten.",
              "&eStufe 3:&r ein voller Würfel aus 26 Draconiumblöcken um den Kern.",
              "&eStufe 4 bis 7:&r größere Kugeln aus Redstoneblöcken innen und Draconiumblöcken außen.",
              "&eStufe 8&r braucht Erwachte Draconiumblöcke, die kommen erst in Stufe 5.",
              "",
              "Steht alles, fehlen noch die Stabilisatoren. Erst dann lässt sich der Kern mit &eActivate&r einschalten.",
          ],
          tasks=[task_item("draconicevolution:energy_core", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["w_energy", "w_core"], icon="draconicevolution:energy_core", size=1.75, shape="hexagon"),

    quest("stabilizer", 12.75, -3.75, "&cStabilisatoren und Gaia",
          subtitle="Der Drachenspeicher braucht Gaia.",
          description=[
              "Ein Energiekern läuft nur mit &evier Stabilisatoren&r. Sie stehen in einer Ebene auf vier Seiten des Kerns, genau in Linie mit seiner Mitte und ein Stück außerhalb seiner Blöcke, und zeigen auf ihn. Ist etwas falsch, meldet das Fenster &e\"Stabilizer configuration invalid\"&r.",
              "",
              "Zuerst den &cPartikelgenerator&r: Redstoneblöcke in die Ecken, Lohenruten an die Seiten, ein Draconiumkern in die Mitte.",
              "",
              "&eRezept auf Kronwerke:&r Der &cStabilisator&r braucht oben in der Mitte eine &aGaia-Seele&r von Botania, dazu Diamanten in die vier Ecken und den Partikelgenerator in die Mitte. Vier Stabilisatoren sind vier Gaia-Seelen, und die gibt es nur vom &aWächter von Gaia&r. Fragt die Magier, die bekämpfen ihn in dieser Stufe sowieso.",
              "",
              "Bei den großen Stufen verlangt der Kern stattdessen &eFortgeschrittene Stabilisatoren&r, das zeigt sein Fenster dann an.",
          ],
          tasks=[task_item("draconicevolution:energy_core_stabilizer", 4)],
          rewards=[reward_item("minecraft:diamond", 8), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["energy_core"], icon="draconicevolution:energy_core_stabilizer", size=1.5, shape="diamond"),

    quest("tiers", 15.25, -2.5, "&cEin größerer Kern",
          subtitle="Draconiumblöcke um den Kern.",
          description=[
              "Für Stufe 3 brauchst du &e26 Draconiumblöcke&r, also 234 Barren. Jede Stufe darüber speichert ein Vielfaches und braucht deutlich mehr Blöcke.",
              "",
              "&eSo baust du um:&r Kern deaktivieren, im Fenster eine Stufe höher stellen, die Bauanleitung anzeigen lassen und die neuen Blöcke setzen. Die Stabilisatoren müssen dann eventuell weiter nach außen.",
              "",
              "&eTipp:&r Draconiumblöcke, die im Kern verbaut sind, zählen nicht für den Obelisken. Plant gemeinsam, wie viel Draconium in Kerne geht und wie viel abgegeben wird.",
          ],
          tasks=[task_item("draconicevolution:draconium_block", 26)],
          rewards=[reward_item("minecraft:redstone_block", 16), reward_xp(10)],
          deps=["stabilizer"], icon="draconicevolution:draconium_block", optional=True),

    quest("pylon", 15.25, -5, "&cEnergiepylonen",
          subtitle="Rein in den Kern, raus aus dem Kern.",
          description=[
              "Strom kommt nicht über Kabel direkt in den Kern, sondern über &cEnergiepylonen&r. &eRezept:&r Draconiumbarren in die Ecken, oben ein Enderauge, an den Seiten Smaragde, in der Mitte ein Draconiumkern, unten ein Diamant. Das ergibt zwei Pylonen.",
              "",
              "&eSo geht's:&r Stell den Pylon in die Nähe des Kerns und setz einen &eGlasblock&r direkt darüber oder darunter. Ein Pylon nimmt entweder Strom auf oder gibt ihn ab, die Richtung schaltest du am Pylon um. Kabel aus deinen Generatoren an den einen, Kabel zu deinen Maschinen an den anderen.",
              "",
              "Mit einem Komparator am Pylon bekommst du ein Redstone-Signal, das zeigt, wie voll der Kern ist.",
          ],
          tasks=[task_item("draconicevolution:energy_pylon", 2)],
          rewards=[reward_item("minecraft:emerald", 8), reward_xp(5)],
          deps=["stabilizer"], icon="draconicevolution:energy_pylon"),

    # ---- Wyvern-Ausruestung -------------------------------------------------------
    quest("relay", 12.75, 2.5, "&bRelaiskristalle",
          subtitle="Ein Zwischenteil für die Wyvern-Rezepte.",
          description=[
              "Ein &bEinfacher Energie-Relaiskristall&r: vier Diamanten um einen Wyvern-Energiekontroller, das ergibt vier Kristalle.",
              "",
              "Jedes Wyvern-Werkzeug und die Wyvern-Rüstung brauchen zwei davon. Eigentlich sind die Kristalle ein kabelloses Stromnetz: Mit dem &bKristallbinder&r verbindest du sie miteinander, und Strom springt von Kristall zu Kristall. Für den Anfang brauchst du sie aber nur als Zutat.",
          ],
          tasks=[task_item("draconicevolution:basic_relay_crystal", 4)],
          rewards=[reward_item("minecraft:diamond", 4)],
          deps=["w_injector", "w_energy"], icon="draconicevolution:basic_relay_crystal"),

    quest("tools", 15.25, 1.25, "&d&lWyvern-Werkzeuge",
          subtitle="Werkzeuge mit Strom und Modulen.",
          description=[
              "Jedes Wyvern-Werkzeug entsteht in der Fusion mit sechs Wyvern-Injektoren. Katalysator: das passende &eDiamantwerkzeug&r (Spitzhacke, Axt, Schaufel, Hacke, Schwert) oder ein &eBogen&r. In die Injektoren: &e1 Draconiumkern&r, &e2 Draconiumbarren&r, &e2 Relaiskristalle&r und &e1 Wyvern-Energiekontroller&r. Jedes kostet 8 Millionen Energie.",
              "",
              "Die Werkzeuge laufen mit Strom und gehen nicht kaputt. Lade sie in einem Ladegerät deiner Wahl auf oder mit dem &dWyvern-Kondensator&r (Fusion aus einem Wyvern-Kern, vier Wyvern-Energiekontrollern und vier Draconiumbarren, acht Injektoren).",
              "",
              "Eine eigene Taste (in den Steuerungseinstellungen unter Draconic Evolution, &eTool Modules&r) öffnet das &eModul-Raster&r des Werkzeugs. Dort steckst du Module hinein, die es stärker machen.",
          ],
          tasks=[task_item("draconicevolution:wyvern_pickaxe", 1)],
          rewards=[reward_item("draconicevolution:draconium_core", 2), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["relay"], icon="draconicevolution:wyvern_pickaxe", size=1.75, shape="gear"),

    quest("armor", 17.75, 2.5, "&dWyvern-Brustplatte",
          subtitle="Ein Schild aus Energie.",
          description=[
              "Die &dWyvern-Brustplatte&r entsteht wie die Werkzeuge: Katalysator eine &eDiamantbrustplatte&r, dazu Draconiumkern, zwei Draconiumbarren, zwei Relaiskristalle und ein Wyvern-Energiekontroller.",
              "",
              "Sie ist das einzige Rüstungsteil der Wyvern-Stufe, und sie trägt einen &eSchild&r, der Schaden mit Strom abfängt. Wie stark er ist, bestimmen die Module darin.",
              "",
              "&eGute erste Module:&r &eWyvern Shield Capacity&r (Draconiumbarren, Netherit-Bruchstücke, Glowstone) für einen größeren Schild, &eWyvern Flight&r (mit einer &5Elytra&r und einer Feuerwerksrakete) zum Fliegen, &eWyvern Energy&r für mehr Speicher.",
          ],
          tasks=[task_item("draconicevolution:wyvern_chestpiece", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_xp(10)],
          deps=["relay"], icon="draconicevolution:wyvern_chestpiece"),

    quest("modules", 17.75, 0, "&dModule",
          subtitle="Kleine Bausteine für große Werkzeuge.",
          description=[
              "Jedes Modul beginnt mit einem &dModulkern&r: Eisen in die Ecken, Redstone oben und unten, Gold links und rechts, ein Draconiumbarren in die Mitte.",
              "",
              "Aus ihm werden die Module, zum Beispiel &eAOE&r (baut mehrere Blöcke auf einmal ab), &eSpeed&r, &eDamage&r, &eSelective Incineration&r (vernichtet Schutt beim Abbauen), &eAuto Feed&r, &eNight Vision&r oder &eUndying&r (rettet dich einmal vor dem Tod). Die Rezepte stehen in JEI.",
              "",
              "Module der Wyvern-Stufe passen in Wyvern-Werkzeuge. Die Draconic- und Chaos-Module für die nächsten Stufen kommen in Stufe 5.",
          ],
          tasks=[task_item("draconicevolution:module_core", 4)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 4)],
          deps=["tools"], icon="draconicevolution:module_core", optional=True),

    # ---- Fuer den Obelisken -------------------------------------------------------
    quest("goal", 20.25, -3.75, "&5&lLicht des Drachen",
          subtitle="Tausend Barren für den Obelisken.",
          description=[
              "&eKronwerke:&r Das Technikziel von Stufe 4 heißt &e1 000 Draconiumbarren&r und &e150 Elite-Steuerschaltkreise&r. Jeder Elite-Schaltkreis braucht einen Draconiumstaub, also kommt alles aus dem End.",
              "",
              "&eSo wird daraus eine Straße:&r",
              "&e1.&r Mit Glück III abbauen. Ein Erz gibt dann im Schnitt etwa viereinhalb Staub statt drei.",
              "&e2.&r Den Staub mit einem Förderband oder Trichter in Öfen oder einen Energiegeladenen Schmelzer von Mekanism schicken.",
              "&e3.&r Den Endstein, der dabei anfällt, nicht wegwerfen: Die Magier brauchen ihn für Reine Ender-Essenz.",
              "&e4.&r Die Barren in der Truhe am Obelisken abgeben, nicht in Kernen verbauen.",
              "",
              "Erst wenn auch die Magier ihr Ziel haben (128 Gaia-Seelen und 30 Mystische Stäbe), öffnet &6Stufe 5 (Chaoswerk)&r.",
          ],
          tasks=[task_item("draconicevolution:draconium_ingot", 256), task_item("mekanism:elite_control_circuit", 16)],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["tiers", "pylon"], icon="draconicevolution:draconium_block", size=2.0, shape="gear"),

    quest("outlook", 22.75, -3.75, "&8Erwacht und Chaos",
          subtitle="Was in Stufe 5 kommt.",
          description=[
              "Draconic Evolution hat noch zwei Stufen über Wyvern. Beide kommen in &6Stufe 5 (Chaoswerk)&r:",
              "",
              "&6Erwachtes Draconium&r (Awakened Draconium): &eRezept auf Kronwerke:&r Fusion aus vier Draconiumblöcken im Kern, dazu vier Draconiumkerne, ein &5Drachenherz&r und zwei &aGaia-Seelenbarren&r in den Injektoren. Ergibt vier Erwachte Draconiumblöcke. Das Drachenherz lässt der Enderdrache fallen, heb dir also eines auf, wenn ihr ihn besiegt.",
              "Daraus werden die &6Draconic-Werkzeuge&r und die &6Draconic-Rüstung&r, Stufe 8 des Energiekerns und der Draconic-Reaktor.",
              "",
              "&4Chaos&r: Die Chaos-Splitter liegen beim &4Chaoswächter&r auf seiner Insel im End. Der Kampf gegen ihn ist das Finale der Season, live auf jedem Stream.",
              "",
              "&eKronwerke:&r Das Technikziel von Stufe 5 will &e64 Erwachte Draconiumblöcke&r. Draconium, das ihr jetzt übrig habt, ist also nicht verschwendet.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["goal"], icon="draconicevolution:draconium_core", optional=True),
]

images = [
    banner("draconic/title", "Draconic Evolution", 11.5, -8.4, height=1.8, kind="title", colour="magic"),
    banner("draconic/draconium", "Draconium", 1.4, -4.2, height=0.9, colour="magic"),
    banner("draconic/fusion", "Fusion", 9.0, 4.1, height=0.9, colour="brass"),
    banner("draconic/kern", "Der Energiekern", 10.25, -6.0, height=0.9, colour="brass"),
    banner("draconic/wyvern", "Wyvern-Ausrüstung", 15.5, 4.3, height=0.9, colour="magic"),
    banner("draconic/nuetzlich", "Nützliches", 1.6, 6.3, height=0.9, colour="brass"),
    banner("draconic/obelisk", "Für den Obelisken", 21.5, -6.0, height=0.9, colour="magic"),
]

chapter(C, "Draconic Evolution", "draconicevolution:draconium_core", "tech", quests, shape="circle", order=38, stage=4,
        subtitle=["Stufe 4. Draconium aus dem End, Fusion, der Energiekern und die Wyvern-Stufe."], images=images)
