"""Draconic Evolution in stage 5, one step per quest: Gaia spirit ingots, dragon hearts, the
catalysts, awakened draconium (Kronwerke fusion with two Gaia ingots), ingots and nuggets, the
draconic injectors, core and energy controller, draconic tools, bow, chestpiece and modules,
the staff, then the Chaos Guardian fight in three steps (island, crystals, guardian) with the
numbers from config/brandon3055/DraconicEvolution.cfg, chaos shards and fragments, the chaotic
injector, core and gear, the reactor and the stage 5 tech goal. Recipes from the Draconic
Evolution jar and kubejs/server_scripts/kronwerke/tech.js."""
from ftbq import chapter, quest, task_item, task_checkmark, task_kill, reward_item, reward_table, reward_xp, banner

C = "draconic_chaos"


def head(name, text, left, y, height=0.9, kind="section", colour="end"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Erwachtes Draconium ---------------------------------------------------------
    quest("welcome", 0, 1.5, "&5&lSchmiede zwei Gaia-Seelenbarren",
          subtitle="Die Botaniker liefern das Metall des Drachen.",
          description=[
              "Ein &6Terrastahlbarren&r in die Mitte, &64 Gaia-Seelen&r oben, unten, links und rechts. Ergibt einen &aGaia-Seelenbarren&r.",
              "",
              "&eRezept auf Kronwerke:&r Jede Fusion für Erwachtes Draconium braucht zwei davon, also acht Gaia-Seelen. Die kommen aus den Gaia-Kämpfen, frag früh bei den Magiern an.",
              "",
              "&eKronwerke:&r Das Technikziel von Stufe 5 will &e64 Erwachte Draconiumblöcke&r und Antimaterie-Pellets. Der Magie-Pfeiler will selbst 128 Gaia-Seelenbarren, teilt also gerecht.",
          ],
          tasks=[task_item("botania:gaia_ingot", 2)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 16), reward_table("s5_common"), reward_xp(10)],
          icon="botania:gaia_ingot", size=2.0, shape="hexagon"),

    quest("dragon_heart", 2.5, 0, "&cHol ein Drachenherz",
          subtitle="Jeder Drache lässt eins zurück.",
          description=[
              "Ruf den &5Enderdrachen&r zurück: vier &6Endkristalle&r auf die Ränder des Ausgangsportals. Stirbt er, schwebt ein &cDrachenherz&r über dem Portal. Es verschwindet nicht.",
              "",
              "Jeder Drache bringt dazu etwa 64 Draconiumstaub und auf diesem Server jedes Mal ein neues &5Drachenei&r.",
              "",
              "&eRechnung:&r 64 Blöcke im Ziel sind 16 Fusionen, also &e16 Drachenkämpfe&r. Sprecht ab, wer wann den Drachen ruft.",
          ],
          tasks=[task_item("draconicevolution:dragon_heart", 1)],
          rewards=[reward_item("minecraft:end_crystal", 4), reward_xp(10)],
          deps=["welcome"]),

    quest("cores", 2.5, 1.75, "&9Leg vier Draconiumkerne bereit",
          subtitle="Die Zutaten für eine Fusion.",
          description=[
              "Vier &6Draconiumkerne&r: Draconiumbarren in die Ecken, Gold an die Seiten, Diamant in die Mitte. Sie kommen in die Injektoren.",
              "",
              "Pro Fusion also vier Kerne, zwei Gaia-Barren und ein Herz: sieben Injektoren der Wyvern-Stufe.",
          ],
          tasks=[task_item("draconicevolution:draconium_core", 4)],
          rewards=[reward_item("minecraft:gold_ingot", 16)],
          deps=["welcome"], icon="draconicevolution:draconium_core"),

    quest("blocks", 2.5, 3.5, "&9Leg vier Draconiumblöcke bereit",
          subtitle="Der Katalysator.",
          description=[
              "Vier &6Draconiumblöcke&r kommen als Stapel in den Fusionskern. Das sind 36 Barren pro Fusion, für das ganze Ziel 576.",
              "",
              "Läuft deine Draconium-Straße aus Stufe 4 noch, lass sie weiterlaufen.",
          ],
          tasks=[task_item("draconicevolution:draconium_block", 4)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 16)],
          deps=["welcome"], icon="draconicevolution:draconium_block"),

    quest("awakened", 5, 1.75, "&5&lFusionier Erwachtes Draconium",
          subtitle="Vier Blöcke aus einer Fusion.",
          description=[
              "&eRezept auf Kronwerke:&r &64 Draconiumblöcke&r im Kern. In sieben Wyvern-Injektoren: &64 Draconiumkerne&r, &a2 Gaia-Seelenbarren&r, &c1 Drachenherz&r. Ergibt &54 Erwachte Draconiumblöcke&r.",
              "",
              "Die Fusion zieht &e50 Millionen&r Energie. Häng die Injektoren an deinen Energiekern, sonst wartest du lange.",
              "",
              "&eKronwerke:&r Jeder Block im Obelisken zählt 50 Punkte. Leg trotzdem ein paar zur Seite, die nächsten Quests brauchen welche.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 4)],
          rewards=[reward_table("s5_common"), reward_xp(20)],
          deps=["dragon_heart", "cores", "blocks"], icon="draconicevolution:awakened_draconium_block", size=2.0, shape="gear"),

    quest("awakened_ingot", 7.5, 1.75, "&5Teil einen Block in Barren",
          subtitle="Neun Barren, neun Nuggets.",
          description=[
              "Ein &5Erwachter Draconiumblock&r an der Werkbank gibt 9 &5Erwachte Barren&r, ein Barren 9 &5Nuggets&r.",
              "",
              "Barren gehen in Kerne, Werkzeuge und Module. Die Nuggets brauchen die Speicherleute: ab 16M hat jede MEGA-Komponente eines im Rezept.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_ingot", 9)],
          rewards=[reward_xp(10)],
          deps=["awakened"], icon="draconicevolution:awakened_draconium_ingot"),

    # ---- Drakonisch ------------------------------------------------------------------
    quest("injector", 10, 0.5, "&dFusionier Drakonische Injektoren",
          subtitle="Die nächste Stufe der Fusion.",
          description=[
              "Wyvern-Stufe. Katalysator: ein &6Wyvern-Injektor&r. In sieben Injektoren: &64 Diamanten&r, &62 Wyvern-Kerne&r, &61 Erwachter Draconiumblock&r. Kostet 256 000 Energie.",
              "",
              "Drakonische Werkzeuge haben acht Zutaten, du brauchst also acht. Ein drakonischer Injektor lädt in 7 Sekunden statt 11.",
          ],
          tasks=[task_item("draconicevolution:awakened_crafting_injector", 8)],
          rewards=[reward_item("minecraft:diamond", 16), reward_xp(10)],
          deps=["awakened_ingot"], icon="draconicevolution:awakened_crafting_injector"),

    quest("awakened_core", 10, 3, "&dFusionier einen Drakonischen Kern",
          subtitle="Ein Netherstern und vier Wyvern-Kerne.",
          description=[
              "Wyvern-Stufe. Katalysator: ein &6Netherstern&r. In acht Injektoren: &64 Wyvern-Kerne&r und &64 Erwachte Barren&r. Kostet 1 Million Energie.",
              "",
              "Du brauchst ihn für den Stab, für Module, für den Chaotischen Kern (vier) und den Chaotischen Energiekern. Sammelt die Sterne gleich mit, wenn ihr Wither farmt.",
          ],
          tasks=[task_item("draconicevolution:awakened_core", 1)],
          rewards=[reward_item("minecraft:nether_star", 1), reward_xp(10)],
          deps=["awakened_ingot"], icon="draconicevolution:awakened_core"),

    quest("energy_core", 12.5, 3, "&dBau einen Drakonischen Energiekontroller",
          subtitle="Der Akku für drakonisches Werkzeug.",
          description=[
              "An der Werkbank: ein &6Wyvern-Kern&r in der Mitte, &64 Wyvern-Energiekontroller&r an den Seiten, &64 Erwachte Barren&r in den Ecken.",
              "",
              "Jedes drakonische Werkzeug und die Brustplatte brauchen einen. Nicht verwechseln mit dem großen Energiekern: dessen Stufe 8 will 378 Erwachte und 786 normale Draconiumblöcke und speichert ohne Grenze.",
          ],
          tasks=[task_item("draconicevolution:draconic_energy_core", 2)],
          rewards=[reward_item("draconicevolution:wyvern_core", 2), reward_xp(10)],
          deps=["awakened_core"], icon="draconicevolution:draconic_energy_core"),

    quest("tools", 12.5, 6, "&d&lFusionier eine Drakonische Spitzhacke",
          subtitle="Aus Wyvern wird Drakonisch.",
          description=[
              "Drakonische Stufe. Katalysator: die &6Wyvern-Spitzhacke&r. In acht Injektoren: &64 Netheritbarren&r, &61 Wyvern-Kern&r, &62 Erwachte Barren&r, &61 Drakonischer Energiekontroller&r. Kostet 32 Millionen Energie.",
              "",
              "Schaufel, Axt, Hacke, Schwert und Bogen gehen genauso aus ihrem Wyvern-Gegenstück. Nimm die Module vorher heraus, wenn du sie behalten willst.",
          ],
          tasks=[task_item("draconicevolution:draconic_pickaxe", 1)],
          rewards=[reward_item("minecraft:netherite_ingot", 2), reward_table("s5_common"), reward_xp(15)],
          deps=["energy_core", "injector"], icon="draconicevolution:draconic_pickaxe", size=1.5, shape="gear"),

    quest("bow", 15, 5, "&dFusionier den Drakonischen Bogen",
          subtitle="Die Waffe für das Finale.",
          description=[
              "Wie die Spitzhacke, mit dem &6Wyvern-Bogen&r als Katalysator.",
              "",
              "Rüste ihn mit drakonischen Projektil-Modulen aus. Das Schadensmodul: Drachenatem, Erwachte Nuggets, ein Wyvern-Kern und das Wyvern-Schadensmodul.",
              "",
              "Der Schild des Chaoswächters schmilzt laut Draconic Evolution am schnellsten unter einem starken Bogen, der schnell feuert.",
          ],
          tasks=[task_item("draconicevolution:draconic_bow", 1)],
          rewards=[reward_item("minecraft:dragon_breath", 8), reward_xp(10)],
          deps=["tools"], icon="draconicevolution:draconic_bow"),

    quest("chestpiece", 15, 7, "&dFusionier die Drakonische Brustplatte",
          subtitle="Schild, Flug und ein zweites Leben.",
          description=[
              "Wie die Werkzeuge, mit der &6Wyvern-Brustplatte&r als Katalysator.",
              "",
              "Sie ist die ganze Rüstung. Ihre Stärke kommt aus den Modulen der nächsten Quests.",
          ],
          tasks=[task_item("draconicevolution:draconic_chestpiece", 1)],
          rewards=[reward_item("minecraft:netherite_ingot", 2), reward_xp(15)],
          deps=["tools"], icon="draconicevolution:draconic_chestpiece"),

    quest("shield_mod", 17.5, 6, "&dBau Drakonische Schildmodule",
          subtitle="Schild zuerst.",
          description=[
              "&6Netheritbarren&r in die Ecken, oben ein &6Draconiumkern&r, unten ein &6Wyvern-Kern&r, links und rechts &6Erwachte Barren&r, in der Mitte das &6Wyvern-Schildmodul&r.",
              "",
              "Pack die Brustplatte damit voll. Jeder Treffer, den der Schild schluckt, trifft dich nicht.",
          ],
          tasks=[task_item("draconicevolution:item_draconic_shield_capacity", 2)],
          rewards=[reward_item("minecraft:netherite_ingot", 1), reward_xp(10)],
          deps=["chestpiece"], icon="draconicevolution:item_draconic_shield_capacity"),

    quest("modules", 17.5, 8, "&dBau ein Drakonisches Untod-Modul",
          subtitle="Fängt einen tödlichen Treffer ab.",
          description=[
              "&6Erwachte Barren&r in die Ecken, oben ein &6Trank&r, unten ein &6Drakonisches Schildmodul&r, links und rechts ein &6Wyvern-Kern&r, in der Mitte das &6Wyvern-Untod-Modul&r. Das Wyvern-Modul braucht ein Totem der Unsterblichkeit.",
              "",
              "Mindestens eins gehört für den Chaoswächter in die Brustplatte.",
          ],
          tasks=[task_item("draconicevolution:item_draconic_undying", 1)],
          rewards=[reward_table("s5_common"), reward_xp(10)],
          deps=["shield_mod"], icon="draconicevolution:item_draconic_undying"),

    quest("flight", 20, 7, "&dBau ein Drakonisches Flugmodul",
          subtitle="Besser fliegen.",
          description=[
              "&6Erwachte Barren&r in die Ecken, oben ein &6Trank&r, unten eine &6Feuerwerksrakete&r, links und rechts ein &6Wyvern-Kern&r, in der Mitte das &6Wyvern-Flugmodul&r.",
              "",
              "Die Chaosinsel ist groß, und der Wächter fliegt.",
          ],
          tasks=[task_item("draconicevolution:item_draconic_flight", 1)],
          rewards=[reward_item("minecraft:firework_rocket", 32), reward_xp(10)],
          deps=["chestpiece"], icon="draconicevolution:item_draconic_flight", optional=True),

    quest("staff", 15, 9, "&dFusionier den Stab der Macht",
          subtitle="Drei Werkzeuge in einem.",
          description=[
              "Drakonische Stufe. Katalysator: ein &6Drakonischer Kern&r. In die Injektoren: drakonische &6Spitzhacke, Schaufel und Schwert&r, ein &6Drakonischer Energiekontroller&r, &66 Erwachte Barren&r. Kostet 256 Millionen Energie.",
              "",
              "Schön, aber nicht nötig. Wer Blöcke für den Obelisken sparen will, lässt ihn weg.",
          ],
          tasks=[task_item("draconicevolution:draconic_staff", 1)],
          rewards=[reward_xp(20)],
          deps=["tools"], icon="draconicevolution:draconic_staff", optional=True),

    # ---- Der Chaoswaechter -----------------------------------------------------------
    quest("find_island", 0, 12.5, "&8Finde die Chaosinsel",
          subtitle="Der Ort des Finales.",
          description=[
              "Die &5Chaosinseln&r liegen im End in einem Raster von &e10 000 Blöcken&r, jede etwa 160 Blöcke im Radius, mit dem &5Chaoskristall&r auf Höhe 80. Für das Finale bringt der Obelisk alle hin.",
              "",
              "Der Kristall lässt sich nicht abbauen, solange der Wächter lebt.",
          ],
          tasks=[task_checkmark("Ich stehe auf der Chaosinsel")],
          rewards=[reward_item("minecraft:golden_apple", 4), reward_xp(10)],
          deps=["awakened"], icon="minecraft:end_stone", shape="diamond"),

    quest("crystals", 2.5, 12.5, "&8Brich einen Wächterkristall",
          subtitle="Phase eins: die Kristalle.",
          description=[
              "Die &5Wächterkristalle&r rund um die Insel schützen den Wächter. Jeder hat einen Schild von &e512&r. Trifft ihn ein Angriff des Wächters selbst, ist der Schild &e10 Sekunden&r instabil. Dann zuschlagen.",
              "",
              "Also: Wächter zum Kristall locken, ausweichen, Kristall zerschlagen. Chaotische Waffen brechen die Schilde direkt, aber die gibt es erst nach dem ersten Sieg.",
          ],
          tasks=[task_kill("draconicevolution:guardian_crystal", 1)],
          rewards=[reward_item("minecraft:golden_apple", 4), reward_xp(15)],
          deps=["find_island"], icon="minecraft:end_crystal"),

    quest("guardian", 5, 12.5, "&4&lBesiege den Chaoswächter",
          subtitle="Das Finale der Season.",
          description=[
              "Sind die Kristalle weg, hat der Wächter noch einen Schild von &e16 000&r und darunter &e1 000 Leben&r. Den Schild kann man beliebig schnell treffen: drakonische Bögen mit Schadens- und Tempomodulen, alle gleichzeitig.",
              "",
              "Volle Schildmodule, ein Untod-Modul und Flug gehören an jeden, der mitkämpft.",
              "",
              "&eKronwerke:&r Der Kampf läuft live auf jedem Stream. Wer ihn besiegt, beendet die Season.",
          ],
          tasks=[task_kill("draconicevolution:draconic_guardian", 1)],
          rewards=[reward_table("s5_rare"), reward_xp(50)],
          deps=["crystals", "bow"], icon="draconicevolution:chaos_shard", size=2.0, shape="gear"),

    quest("chaos_shard", 7.5, 12.5, "&8Bau den Chaoskristall ab",
          subtitle="Fünf Scherben pro Kristall.",
          description=[
              "Nach dem Sieg lässt sich der &5Chaoskristall&r in der Mitte der Insel abbauen. Er gibt &e5 Chaosscherben&r.",
              "",
              "Weitere Inseln liegen 10 000 Blöcke weiter, jede mit einem eigenen Wächter.",
          ],
          tasks=[task_item("draconicevolution:chaos_shard", 1)],
          rewards=[reward_xp(30)],
          deps=["guardian"], icon="draconicevolution:chaos_shard", optional=True),

    quest("fragments", 10, 12.5, "&8Zerteil eine Chaosscherbe",
          subtitle="Groß, klein, winzig.",
          description=[
              "An der Werkbank wird eine &5Chaosscherbe&r zu 9 &5Großen Chaosfragmenten&r, eins davon zu 9 &5Kleinen&r, eins davon zu 9 &5Winzigen&r. Zurück geht es genauso.",
              "",
              "Große Fragmente brauchst du für Injektoren und Kerne, kleine für Module und den Chaotischen Energiekern.",
          ],
          tasks=[task_item("draconicevolution:large_chaos_frag", 9)],
          rewards=[reward_xp(15)],
          deps=["chaos_shard"], icon="draconicevolution:large_chaos_frag", optional=True),

    quest("chaotic_injector", 12.5, 11.5, "&8Fusionier Chaotische Injektoren",
          subtitle="Die letzte Stufe der Fusion.",
          description=[
              "Drakonische Stufe. Katalysator: ein &6Drakonischer Injektor&r. In neun Injektoren: &64 Diamanten&r, &64 Große Chaosfragmente&r, ein &5Drachenei&r. Kostet 8 Millionen Energie.",
              "",
              "Ein chaotischer Injektor lädt in 3 Sekunden. Das Drachenei gibt es bei jedem Drachen neu.",
          ],
          tasks=[task_item("draconicevolution:chaotic_crafting_injector", 1)],
          rewards=[reward_xp(20)],
          deps=["fragments"], icon="draconicevolution:chaotic_crafting_injector", optional=True),

    quest("chaotic_core", 12.5, 13.5, "&8Fusionier einen Chaotischen Kern",
          subtitle="Die Stufe über Drakonisch.",
          description=[
              "Drakonische Stufe. Katalysator: ein &6Großes Chaosfragment&r. In zwölf Injektoren: &64 Erwachte Barren&r, &64 Drakonische Kerne&r, &64 Große Chaosfragmente&r. Kostet 100 Millionen Energie.",
          ],
          tasks=[task_item("draconicevolution:chaotic_core", 1)],
          rewards=[reward_xp(20)],
          deps=["fragments"], icon="draconicevolution:chaotic_core", optional=True),

    quest("chaotic_gear", 15, 12.5, "&8Fusionier chaotische Ausrüstung",
          subtitle="Das Ende der Leiter.",
          description=[
              "Chaotische Stufe. Katalysator: das drakonische Teil. In acht Injektoren: &66 Erwachte Barren&r, ein &6Chaotischer Kern&r, ein &6Chaotischer Energiekern&r. Kostet 128 Millionen Energie.",
              "",
              "&6Chaotischer Energiekern:&r kleine Chaosfragmente in die Ecken, 4 Drakonische Energiekontroller an die Seiten, ein Drakonischer Kern in die Mitte. Mit chaotischen Waffen werden weitere Wächter viel leichter.",
          ],
          tasks=[task_item("draconicevolution:chaotic_sword", 1)],
          rewards=[reward_xp(30)],
          deps=["chaotic_injector", "chaotic_core"], icon="draconicevolution:chaotic_sword", optional=True),

    # ---- Der Reaktor -------------------------------------------------------------------
    quest("reactor_parts", 0, 17, "&6Bau die Stabilisatorteile",
          subtitle="Was schon vor dem Kampf geht.",
          description=[
              "&6Innerer Rotor&r: 3 Erwachte Barren, ein Draconiumkern, 2 Draconiumbarren. &6Äußerer Rotor&r: dasselbe mit 3 Diamanten. &6Rotorbaugruppe&r: 2 innere, 2 äußere Rotoren, ein Wyvern-Kern, 2 Draconiumbarren.",
              "&6Fokusring&r: Gold, Diamanten, 2 Wyvern-Kerne. &6Stabilisatorrahmen&r: 6 Eisen, ein Wyvern-Kern, ein Erwachter Barren.",
              "",
              "Ein Reaktor braucht 4 Stabilisatoren, also von allem vier.",
          ],
          tasks=[task_item("draconicevolution:reactor_prt_rotor_full", 1), task_item("draconicevolution:reactor_prt_focus_ring", 1),
                 task_item("draconicevolution:reactor_prt_stab_frame", 1)],
          rewards=[reward_item("draconicevolution:wyvern_core", 2), reward_xp(10)],
          deps=["energy_core"], icon="draconicevolution:reactor_prt_rotor_full", optional=True),

    quest("reactor", 2.5, 17, "&c&lBau den Drakonischen Reaktor",
          subtitle="Viel Strom, und er kann explodieren.",
          description=[
              "&6Reaktorkern&r: Fusion, chaotisch, Chaosscherbe im Kern. &6Stabilisator&r: Fusion um den Rahmen mit Rotorbaugruppe, Fokusring, Drakonischem Energiekontroller, 3 Erwachten Barren, Chaotischem Kern und Großem Fragment, viermal. Dazu ein &6Reaktor-Energieinjektor&r.",
              "",
              "Erwachtes Draconium ist der Brennstoff. Der Injektor lädt den Kern zum Start und hält danach das &eEindämmungsfeld&r. Die Stabilisatoren geben den Strom ab.",
              "",
              "&c&lEhrlich:&r Fällt das Feld auf null, explodiert er. Die große Explosion ist auf diesem Server &cnicht abgeschaltet&r. Bau ihn weit weg, und speise den Injektor aus einem Energiekern. SAS und Komparator-Ausgänge nutzen.",
          ],
          tasks=[task_item("draconicevolution:reactor_core", 1), task_item("draconicevolution:reactor_stabilizer", 4),
                 task_item("draconicevolution:reactor_injector", 1)],
          rewards=[reward_xp(40)],
          deps=["reactor_parts", "chaotic_core"], icon="draconicevolution:reactor_core", size=1.75, shape="gear",
          optional=True),

    # ---- Das Ziel ----------------------------------------------------------------------
    quest("goal", 5, 17, "&5&lBring 64 Blöcke zum Obelisken",
          subtitle="Der Technik-Pfeiler des Chaoswerks.",
          description=[
              "Leite &5Erwachte Draconiumblöcke&r in eine Kiste am Obelisken. Den Stand zeigt &e/kw goals&r.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 5 heißt &5Der Chaoswächter&r: &e64 Erwachte Draconiumblöcke&r (fest) und die Antimaterie-Pellets aus Mekanism. Das sind 16 Fusionen, 16 Drachenherzen, 32 Gaia-Seelenbarren.",
              "",
              "Bei 98 Prozent wird der Termin für das Finale gesetzt.",
          ],
          tasks=[task_item("draconicevolution:awakened_draconium_block", 16)],
          rewards=[reward_table("s5_rare"), reward_xp(30)],
          deps=["awakened"], icon="draconicevolution:awakened_draconium_block", size=2.5, shape="gear"),
]

images = [
    head("title", "Draconic: Erwacht und Chaos", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 5: Chaoswerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("gear", "Drakonisch", 10, -1.0, colour="magic"),
    head("fight", "Der Chaoswächter", 0, 10.6, colour="fire"),
    head("reactor", "Reaktor und Ziel", 0, 15.2, colour="brass"),
]

chapter(C, "Draconic: Erwacht und Chaos", "draconicevolution:awakened_draconium_block", "tech", quests,
        shape="square", order=42, stage=5,
        subtitle=["Stufe 5: Erwachtes Draconium, drakonische Ausrüstung, der Chaoswächter und der Reaktor."],
        images=images)
