"""Draconic Evolution in stage 5: awakened draconium (fusion with Gaia spirit ingots and a dragon
heart), the draconic injectors, the draconic core and energy core, draconic tools, armor and
modules, chaos shards from the Chaos Guardian's island, the chaotic tier and the draconic
reactor. Chaos shards only exist after the guardian is dead, so everything from them is optional.
Recipes follow the Draconic Evolution jar and kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import chapter, quest, task_item, reward_item, reward_table, reward_xp, banner

C = "draconic_chaos"


def head(name, text, left, y, height=0.9, kind="section", colour="end"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Erwachtes Draconium ---------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lDraconic: Erwacht und Chaos",
          subtitle="Gaias Barren für das Metall des Drachen.",
          description=[
              "Mit &6Stufe 5, dem Chaoswerk&r, öffnet Draconic Evolution seine letzten Stufen: &5Erwachtes Draconium&r, die drakonische Ausrüstung und am Ende das Chaos.",
              "",
              "Alles hier beginnt mit &5Erwachtem Draconium&r. Und das braucht auf Kronwerke die Botaniker: &eRezept auf Kronwerke:&r Zwei der sechs Draconiumkerne in der Fusion sind durch &aGaia-Geistbarren&r ersetzt.",
              "",
              "Einen &aGaia-Geistbarren&r craftest du aus einem &aTerrastahlbarren&r in der Mitte und &e4 Gaia-Geistern&r drumherum. Die Geister kommen aus den Gaia-Kämpfen von Stufe 4. Frag also früh bei den Magiern an, ob sie dir welche abgeben.",
              "",
              "&eKronwerke:&r Das Technikziel von Stufe 5 will &e64 Erwachte Draconiumblöcke&r, eine feste Zahl. Dazu kommen die Antimaterie-Pellets aus Mekanism.",
          ],
          tasks=[task_item("botania:gaia_ingot", 2)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 16), reward_table("s5_common"), reward_xp(10)],
          icon="draconicevolution:awakened_draconium_block", size=2.0, shape="hexagon"),

    quest("dragon_heart", 2.75, 0, "&cHerz des Drachen",
          subtitle="Jeder Drache lässt eins zurück.",
          description=[
              "Die Fusion für Erwachtes Draconium braucht ein &cDrachenherz&r, und das wird jedes Mal verbraucht.",
              "",
              "Ein Drachenherz gibt es, wenn der &5Enderdrache&r stirbt. Draconic Evolution lässt es über dem Ausgangsportal schweben, es verschwindet nicht von selbst. Den Drachen rufst du wie in Vanilla zurück: vier Endkristalle auf die Ränder des Ausgangsportals.",
              "",
              "&eRechnung:&r Eine Fusion ergibt 4 Erwachte Blöcke. Für die 64 Blöcke im Ziel sind das 16 Fusionen und damit &e16 Drachenkämpfe&r. Dazu kommt, was du für Werkzeug, Rüstung und Injektoren brauchst. Sprecht euch ab, wer wann den Drachen ruft, und teilt die Herzen auf.",
          ],
          tasks=[task_item("draconicevolution:dragon_heart", 1)],
          rewards=[reward_item("minecraft:end_crystal", 4), reward_xp(10)],
          deps=["welcome"]),

    quest("cores", 2.75, 3, "&9Kerne und Blöcke",
          subtitle="Das Material für eine Fusion.",
          description=[
              "Für eine Fusion brauchst du neben dem Herz und den Gaia-Barren noch:",
              "",
              "&9Draconiumkern&r: &e4 Stück&r in den Injektoren.",
              "&9Draconiumblock&r: &e4 Stück&r als Katalysator im Fusionskern.",
              "",
              "Das sind pro Fusion 36 Draconiumbarren allein für die Blöcke. Für 16 Fusionen gehen 576 Barren nur in die Katalysatoren. Wenn deine Draconium-Straße aus Stufe 4 noch läuft, lass sie weiterlaufen.",
          ],
          tasks=[task_item("draconicevolution:draconium_core", 4), task_item("draconicevolution:draconium_block", 4)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 16)],
          deps=["welcome"], icon="draconicevolution:draconium_core"),

    quest("awakened", 5.5, 1.5, "&5&lErwachtes Draconium",
          subtitle="Vier Blöcke aus einer Fusion.",
          description=[
              "&eRezept auf Kronwerke:&r Fusion mit &e4 Draconiumblöcken&r im Fusionskern. In die sieben Injektoren kommen &e4 Draconiumkerne&r, &a2 Gaia-Geistbarren&r und &c1 Drachenherz&r. Ergebnis: &54 Erwachte Draconiumblöcke&r.",
              "",
              "Die Fusion läuft auf der Stufe &bWyvern&r, du brauchst also Wyvern-Injektoren aus Stufe 4. Sie zieht &e50 Millionen OP&r. Hänge den Fusionskern deshalb an deinen Energiekern, sonst wartest du sehr lange.",
              "",
              "Ein Block ergibt 9 &5Erwachte Draconiumbarren&r, ein Barren 9 Nuggets. Die &5Nuggets&r brauchen übrigens die Speicherleute: Ab 16M hat jede MEGA-Zelle eins im Rezept.",
              "",
              "&eKronwerke:&r Jeder Block im Obelisken zählt &e50 Punkte&r. Leg dir trotzdem ein paar zur Seite, die nächsten Quests brauchen welche.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 4)],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["dragon_heart", "cores"], icon="draconicevolution:awakened_draconium_block", size=2.0, shape="gear"),

    quest("injector", 8.25, 0, "&dDrakonische Injektoren",
          subtitle="Die nächste Stufe der Fusion.",
          description=[
              "Alles Drakonische wird auf der Stufe &dDrakonisch&r fusioniert. Dafür brauchst du &dDrakonische Fusionsinjektoren&r (im Spiel Draconic Fusion Crafting Injector).",
              "",
              "&eRezept:&r Fusion mit einem &bWyvern-Injektor&r als Katalysator, dazu &e4 Diamanten&r, &e2 Wyvernkerne&r und &e1 Erwachter Draconiumblock&r.",
              "",
              "Ein drakonisches Werkzeug hat acht Zutaten, also acht Injektoren rund um den Kern. Das sind acht Erwachte Blöcke, die nicht in den Obelisken gehen. Bau sie einmal und nutze sie für alles Weitere.",
          ],
          tasks=[task_item("draconicevolution:awakened_crafting_injector", 8)],
          rewards=[reward_item("minecraft:diamond", 16), reward_xp(10)],
          deps=["awakened"], icon="draconicevolution:awakened_crafting_injector"),

    quest("awakened_core", 8.25, 3, "&dDrakonischer Kern",
          subtitle="Ein Netherstern und vier Wyvernkerne.",
          description=[
              "Der &dDrakonische Kern&r (im Spiel Draconic Core) ist das Herzstück der höheren Rezepte.",
              "",
              "&eRezept:&r Fusion auf Stufe Wyvern mit einem &eNetherstern&r als Katalysator. In die Injektoren: &e4 Wyvernkerne&r und &e4 Erwachte Draconiumbarren&r. Energie: 1 Million OP.",
              "",
              "Du brauchst ihn für den Drakonischen Stab, für den Chaotischen Kern (vier Stück) und für den Chaotischen Energiekern. Wenn ihr Wither farmt, sammelt die Sterne gleich mit.",
          ],
          tasks=[task_item("draconicevolution:awakened_core", 1)],
          rewards=[reward_item("minecraft:nether_star", 1), reward_xp(10)],
          deps=["awakened"], icon="draconicevolution:awakened_core"),

    quest("energy_core", 11, 3, "&dDrakonischer Energiekern",
          subtitle="Der Akku für drakonisches Werkzeug.",
          description=[
              "Jedes drakonische Werkzeug und jedes Rüstungsteil braucht einen &dDrakonischen Energiekern&r (im Spiel Draconic Energy Controller, nicht zu verwechseln mit dem großen Energiespeicher).",
              "",
              "&eRezept an der Werkbank:&r ein &bWyvernkern&r in der Mitte, &e4 Wyvern-Energiekerne&r an den Seiten, &e4 Erwachte Draconiumbarren&r in den Ecken.",
              "",
              "&eNoch eine Zahl:&r Die achte und letzte Stufe des großen Energiekerns braucht &e378 Erwachte Draconiumblöcke&r in ihrer Hülle. Das ist eher ein Projekt für nach der Season.",
          ],
          tasks=[task_item("draconicevolution:draconic_energy_core", 2)],
          rewards=[reward_item("draconicevolution:wyvern_core", 2), reward_xp(10)],
          deps=["awakened_core"], icon="draconicevolution:draconic_energy_core"),

    # ---- Werkzeug und Rüstung ----------------------------------------------------------
    quest("tools", 11, 8, "&dDrakonisches Werkzeug",
          subtitle="Aus Wyvern wird Drakonisch.",
          description=[
              "Jedes drakonische Werkzeug entsteht aus seinem Wyvern-Gegenstück. &eRezept:&r Fusion auf Stufe Drakonisch, das Wyvern-Werkzeug als Katalysator. In die acht Injektoren: &e4 Netheritbarren&r, &e1 Wyvernkern&r, &e2 Erwachte Draconiumbarren&r und &e1 Drakonischer Energiekern&r. Energie: 32 Millionen OP.",
              "",
              "Das gilt für Spitzhacke, Schaufel, Axt, Hacke, Schwert und Bogen. Module aus dem Wyvern-Werkzeug musst du vorher herausnehmen, wenn du sie behalten willst.",
              "",
              "&eFür den Chaoswächter&r ist der &dDrakonische Bogen&r das wichtigste Stück. Der Wächter hat einen Schild von 16 000 Punkten, und laut Draconic Evolution schmilzt der am schnellsten unter einem starken Bogen, der schnell feuert.",
          ],
          tasks=[task_item("draconicevolution:draconic_pickaxe", 1)],
          rewards=[reward_item("minecraft:netherite_ingot", 2), reward_table("s5_common"), reward_xp(15)],
          deps=["energy_core"], icon="draconicevolution:draconic_pickaxe"),

    quest("bow", 13.75, 8, "&dDrakonischer Bogen",
          subtitle="Die Waffe für das Finale.",
          description=[
              "Gleiches Rezept wie die anderen Werkzeuge, nur mit dem &bWyvern-Bogen&r als Katalysator.",
              "",
              "Rüste ihn mit Projektil-Modulen aus: Schaden, Geschwindigkeit, Genauigkeit und Durchschlag gibt es als drakonische Module. Das Schadensmodul braucht Drachenatem, Erwachte Nuggets und einen Wyvernkern.",
              "",
              "Im Kapitel &5Das Finale&r steht, warum der Bogen gegen den Chaoswächter so viel ausmacht.",
          ],
          tasks=[task_item("draconicevolution:draconic_bow", 1)],
          rewards=[reward_item("minecraft:dragon_breath", 8), reward_xp(10)],
          deps=["tools"], icon="draconicevolution:draconic_bow"),

    quest("chestpiece", 11, 11, "&dDrakonische Brustplatte",
          subtitle="Schild, Flug und ein zweites Leben.",
          description=[
              "Die Brustplatte ist bei Draconic Evolution die ganze Rüstung. &eRezept:&r wie die Werkzeuge, mit der &bWyvern-Brustplatte&r als Katalysator.",
              "",
              "Ihre Stärke liegt in den Modulen:",
              "&dSchildkapazität&r: Netherit, Erwachte Barren, ein Draconiumkern, ein Wyvernkern und das Wyvern-Modul.",
              "&dSchilderholung&r: dasselbe Muster mit dem Wyvern-Erholungsmodul.",
              "&dFlug&r: aus dem Wyvern-Flugmodul mit Trank des sanften Falls und Feuerwerk.",
              "&dUntod&r: aus dem Wyvern-Modul mit einem starken Heiltrank und einem drakonischen Schildmodul. Es fängt einen tödlichen Treffer ab.",
          ],
          tasks=[task_item("draconicevolution:draconic_chestpiece", 1)],
          rewards=[reward_item("minecraft:netherite_ingot", 2), reward_xp(15)],
          deps=["tools"], icon="draconicevolution:draconic_chestpiece"),

    quest("modules", 13.75, 11, "&dModule für den Kampf",
          subtitle="Schild zuerst.",
          description=[
              "Pack die Brustplatte mit &dSchildkapazität&r voll und setz mindestens ein &dUntod-Modul&r ein. Der Chaoswächter teilt hart aus, und jeder Treffer, den der Schild schluckt, trifft dich nicht.",
              "",
              "Den Schild lädt die Rüstung aus ihrer Energie. Ein &dDrakonisches Energiemodul&r oder ein Energie-Link zu deinem Kern hält dich länger im Kampf.",
          ],
          tasks=[task_item("draconicevolution:item_draconic_shield_capacity", 2), task_item("draconicevolution:item_draconic_undying", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["chestpiece"], icon="draconicevolution:item_draconic_shield_capacity"),

    quest("staff", 8.25, 9.5, "&dDrakonischer Stab",
          subtitle="Drei Werkzeuge in einem.",
          description=[
              "Der &dStab der Macht&r vereint Spitzhacke, Schaufel und Schwert. &eRezept:&r Fusion mit einem &dDrakonischen Kern&r als Katalysator. In die Injektoren: die drakonische Spitzhacke, Schaufel und das Schwert, ein Drakonischer Energiekern und &e6 Erwachte Draconiumbarren&r. Energie: 256 Millionen OP.",
              "",
              "Schön, aber nicht nötig. Wer Blöcke für den Obelisken sparen will, lässt ihn weg.",
          ],
          tasks=[task_item("draconicevolution:draconic_staff", 1)],
          rewards=[reward_xp(20)],
          deps=["tools"], icon="draconicevolution:draconic_staff", optional=True),

    # ---- Chaos -------------------------------------------------------------------------
    quest("chaos_shard", 14.5, 1.5, "&8&lChaosscherben",
          subtitle="Erst nach dem Kampf.",
          description=[
              "&cWichtig:&r Chaosscherben gibt es nur auf einer &5Chaosinsel&r, und erst wenn ihr Wächter tot ist. Der &5Chaoskristall&r in der Mitte der Insel lässt sich vorher nicht abbauen. Nach dem Sieg gibt er beim Abbauen &e5 Chaosscherben&r.",
              "",
              "Eine Scherbe zerfällt an der Werkbank in 9 Große Chaosfragmente, eins davon in 9 Kleine und so weiter. Umgekehrt geht es auch.",
              "",
              "&eKronwerke:&r Der Kampf gegen den Chaoswächter ist das Finale der Season. Alles ab hier gibt es also erst danach. Weitere Chaosinseln liegen im End in einem Raster von 10 000 Blöcken, jede mit einem eigenen Wächter.",
          ],
          tasks=[task_item("draconicevolution:chaos_shard", 1)],
          rewards=[reward_xp(30)],
          deps=["injector"], icon="draconicevolution:chaos_shard", size=1.5, shape="diamond", optional=True),

    quest("chaotic_core", 17.25, 0, "&8Chaotischer Kern",
          subtitle="Die Stufe über Drakonisch.",
          description=[
              "&eRezept:&r Fusion auf Stufe Drakonisch, ein &8Großes Chaosfragment&r als Katalysator. In zwölf Injektoren: &e4 Erwachte Draconiumbarren&r, &e4 Drakonische Kerne&r und &e4 Große Chaosfragmente&r. Energie: 100 Millionen OP.",
              "",
              "Für chaotische Rezepte brauchst du &8Chaotische Injektoren&r: Fusion aus einem Drakonischen Injektor mit 4 Diamanten, 4 Großen Chaosfragmenten und einem &5Drachenei&r. Auf diesem Server legt jeder Drache ein neues Ei.",
          ],
          tasks=[task_item("draconicevolution:chaotic_core", 1)],
          rewards=[reward_xp(20)],
          deps=["chaos_shard"], icon="draconicevolution:chaotic_core", optional=True),

    quest("chaotic_gear", 20, 0, "&8Chaotische Ausrüstung",
          subtitle="Das Ende der Leiter.",
          description=[
              "Chaotische Werkzeuge und die Chaotische Brustplatte entstehen aus ihren drakonischen Vorgängern. &eRezept:&r Fusion auf Stufe Chaotisch mit &e6 Erwachten Draconiumbarren&r, einem &8Chaotischen Kern&r und einem &8Chaotischen Energiekern&r. Energie: 128 Millionen OP.",
              "",
              "Den Chaotischen Energiekern craftest du aus einem Drakonischen Kern, 4 Drakonischen Energiekernen und 4 Kleinen Chaosfragmenten.",
              "",
              "Mit chaotischen Waffen lassen sich die Kristalle eines Chaoswächters direkt knacken. Für weitere Inseln wird der Kampf damit deutlich leichter.",
          ],
          tasks=[task_item("draconicevolution:chaotic_sword", 1)],
          rewards=[reward_xp(30)],
          deps=["chaotic_core"], icon="draconicevolution:chaotic_sword", optional=True),

    # ---- Der Reaktor -------------------------------------------------------------------
    quest("reactor_parts", 14.5, 5, "&6Stabilisatorteile",
          subtitle="Was schon vor dem Kampf geht.",
          description=[
              "Die Teile für die Reaktor-Stabilisatoren kannst du schon jetzt bauen:",
              "",
              "&6Innerer Rotor&r: 3 Erwachte Barren, ein Draconiumkern, 2 Draconiumbarren.",
              "&6Äußerer Rotor&r: 3 Diamanten, ein Draconiumkern, 2 Draconiumbarren.",
              "&6Rotorbaugruppe&r: 2 innere und 2 äußere Rotoren, ein Wyvernkern, 2 Draconiumbarren.",
              "&6Fokusring&r: Gold, Diamanten und 2 Wyvernkerne.",
              "&6Stabilisatorrahmen&r: 6 Eisen, ein Wyvernkern, ein Erwachter Barren.",
              "",
              "Ein Reaktor braucht &e4 Stabilisatoren&r, also von allem vier.",
          ],
          tasks=[task_item("draconicevolution:reactor_prt_rotor_full", 1), task_item("draconicevolution:reactor_prt_focus_ring", 1),
                 task_item("draconicevolution:reactor_prt_stab_frame", 1)],
          rewards=[reward_item("draconicevolution:wyvern_core", 2), reward_xp(10)],
          deps=["energy_core"], icon="draconicevolution:reactor_prt_rotor_full", optional=True),

    quest("reactor", 17.25, 5, "&c&lDer Drakonische Reaktor",
          subtitle="Viel Strom, und er kann explodieren.",
          description=[
              "&eWas du brauchst:&r einen &cReaktorkern&r (Fusion auf Stufe Chaotisch mit einer Chaosscherbe, Erwachten Barren, Draconium und 2 Großen Chaosfragmenten), &e4 Reaktor-Stabilisatoren&r (je ein Chaotischer Kern und ein Großes Fragment) und einen &eReaktor-Energieinjektor&r. Das alles gibt es erst nach dem Chaoswächter.",
              "",
              "&eSo läuft er:&r Du füllst Erwachtes Draconium als Brennstoff in den Kern. Zum Starten lädst du ihn mit Energie über den Injektor auf, dann aktivierst du ihn. Danach muss der Injektor ständig Energie in das &eEindämmungsfeld&r schieben, die Stabilisatoren geben den erzeugten Strom ab. Aus dem Brennstoff wird nach und nach Chaos.",
              "",
              "&c&lEhrlich gesagt:&r Fällt das Eindämmungsfeld auf null, explodiert der Reaktor. Auf diesem Server ist die große Explosion &cnicht abgeschaltet&r, und sie reißt einen riesigen Krater. Halte Feldstärke und Temperatur im Blick, bau ihn weit weg von allem, was dir wichtig ist, und sorg dafür, dass der Injektor auch dann noch Energie bekommt, wenn der Reaktor selbst nichts mehr liefert, zum Beispiel aus einem Energiekern.",
              "",
              "Der Reaktor hat &eSAS&r, eine halbautomatische Abschaltung, und Komparator-Ausgänge für Temperatur, Feld, Sättigung und Umwandlung. Nutze sie.",
          ],
          tasks=[task_item("draconicevolution:reactor_core", 1), task_item("draconicevolution:reactor_stabilizer", 4),
                 task_item("draconicevolution:reactor_injector", 1)],
          rewards=[reward_xp(40)],
          deps=["reactor_parts", "chaotic_core"], icon="draconicevolution:reactor_core", size=1.75, shape="gear",
          optional=True),

    # ---- Das Ziel ----------------------------------------------------------------------
    quest("goal", 5.5, 5, "&5&lVierundsechzig Blöcke",
          subtitle="Der Technik-Pfeiler des Chaoswerks.",
          description=[
              "Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r. Im Technik-Pfeiler warten &e64 Erwachte Draconiumblöcke&r, eine feste Zahl, egal wie viele ihr seid, und die Antimaterie-Pellets aus Mekanism.",
              "",
              "&eWas das heißt:&r 16 Fusionen, 16 Drachenherzen, 32 Gaia-Geistbarren und 64 Draconiumblöcke als Katalysator. Die Gaia-Barren kommen von den Magiern, deren Pfeiler sie ebenfalls will. Redet miteinander, wer wie viele bekommt.",
              "",
              "&eKronwerke:&r Stell eine Kiste neben den Obelisken und lass die Blöcke hineinlaufen, oder gib sie per Rechtsklick ab. Den Stand zeigt &e/kw goals&r.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 16)],
          rewards=[reward_table("s5_rare"), reward_xp(30)],
          deps=["awakened"], icon="draconicevolution:awakened_draconium_block", size=2.5, shape="gear"),
]

images = [
    head("title", "Draconic: Erwacht und Chaos", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("gear", "Werkzeug und Rüstung", 8, 6.6, colour="magic"),
    head("chaos", "Chaos", 14, -1.2, colour="end"),
    head("reactor", "Der Reaktor", 14, 3.6, colour="fire"),
]

chapter(C, "Draconic: Erwacht und Chaos", "draconicevolution:awakened_draconium_block", "tech", quests,
        shape="square", order=42, stage=5,
        subtitle=["Stufe 5: Erwachtes Draconium, drakonische Ausrüstung, Chaosscherben und der Reaktor."],
        images=images)
