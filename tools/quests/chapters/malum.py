"""Malum in stage 3 (the whole mod opens with stage 3): soulstone and runewood, the crude scythe
and spirit harvesting, the spirit altar with hex ash, hallowed gold and soul stained steel (which
feeds the Ender IO soul binder), the spirit jar, the spirit crucible with the alchemical impetus
and metal nodes, and totem magic with the rite of healing and the rite of quickening."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "malum"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Seelen ernten ---------------------------------------------------------
    quest("welcome", 0, 0, "&5Encyclopedia Arcana",
          subtitle="Magie aus zerbrochenen Seelen.",
          description=[
              "&5Malum&r arbeitet mit Seelen. Wer ein Wesen mit der richtigen Klinge tötet, zerschlägt seine Seele, und die Stücke fallen als &dSpirit Arcana&r heraus, kleine farbige Kristalle. Mit ihnen infundierst du Items, schmiedest Metalle und baust Totems. Die ganze Mod öffnet mit &6Stufe 3&r.",
              "",
              "Dein Handbuch ist die &6Encyclopedia Arcana&r, formlos aus einem &6Buch&r und einem &6Refined Soulstone&r.",
              "",
              pic("malum:encyclopedia_arcana"),
              "",
              "&6Soulstone&r ist ein häufiges Erz zwischen Y 100 und ganz unten. Das rohe Stück gibt im Ofen zwei Refined Soulstone.",
          ],
          tasks=[task_item("malum:encyclopedia_arcana", 1)],
          rewards=[reward_item("malum:raw_soulstone", 8), reward_xp(5)],
          icon="malum:encyclopedia_arcana", size=2.0, shape="hexagon"),

    quest("soulstone", 2.5, -1, "&5Soulstone",
          subtitle="Stein, der halb in einer anderen Welt steckt.",
          description=[
              "Gereinigter &6Soulstone&r ist nicht ganz in dieser Welt, er schwingt mit Seelen mit. Darum steckt er in der Sense, im Altar und im Seelenstahl.",
              "",
              "Bau gleich einen ordentlichen Vorrat ab. Allein Soul Stained Steel will vier Stück pro Barren.",
          ],
          tasks=[task_item("malum:refined_soulstone", 32)],
          rewards=[reward_item("malum:raw_soulstone", 16)],
          deps=["welcome"], icon="malum:refined_soulstone"),

    quest("runewood", 2.5, 1.2, "&6Runewood",
          subtitle="Eiche, vollgesogen mit Magie.",
          description=[
              "&6Runewood&r wächst vor allem auf großen Ebenen, seltener in Wäldern. Du erkennst die Bäume an den orange-gelben Blättern.",
              "",
              "Aus Runewood baust du den Geisteraltar, die Ablagen drumherum und später die Totems. Pflanz ein paar Setzlinge zu Hause an, du brauchst mehr Holz, als ein Baum hergibt.",
              "",
              "&eTipp:&r Manche Stämme haben eine klebrige Stelle. Entrindest du sie, kannst du &6Runic Sap&r in eine Flasche füllen, ein heilendes Getränk.",
          ],
          tasks=[task_item("malum:runewood_log", 16)],
          rewards=[reward_item("malum:runewood_sapling", 4)],
          deps=["welcome"], icon="malum:runewood_sapling"),

    quest("scythe", 4.5, -1, "&5Crude Scythe",
          subtitle="Eine Klinge, die auch die Seele trifft.",
          description=[
              "Die &6Crude Scythe&r ist aus &e3 Eisenbarren&r, zwei Stöcken und einem &6Refined Soulstone&r. Der lange Schwung trifft erst den Körper und dann die Seele, bevor sie sich auflöst, und sie schlägt auch seitlich mit.",
              "",
              "Nur was mit der Sense stirbt, lässt Spirit Arcana fallen. Ein normales Schwert reicht dafür nicht. Häng sie also griffbereit in die Hotbar.",
          ],
          tasks=[task_item("malum:crude_scythe", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 4), reward_xp(3)],
          deps=["soulstone"], icon="malum:crude_scythe"),

    quest("spirits", 6.5, 0, "&dSpirit Arcana",
          subtitle="Jede Seele hat ihre Farbe.",
          description=[
              "Welche Arcana ein Wesen fallen lässt, hängt von seiner Natur ab:",
              "",
              "&eSacred&r: friedliche Tiere wie Schweine, Kühe, Schafe, Hühner.",
              "&5Wicked&r: Zombies, Hexen, Spinnen und andere Bösartige.",
              "&dArcane&r: Skelette, Hexen, Phantome, alles Magische.",
              "&6Earthen&r: Zombies, Kühe, Schafe.",
              "&cInfernal&r: Creeper, Blazes und fast alles aus dem Nether.",
              "&fAerial&r: Spinnen, Hühner, Phantome.",
              "&bAqueous&r: Ertrunkene, Tintenfische, Fische.",
              "&5Eldritch&r: selten, etwa von Endermen.",
              "",
              "Fang mit Sacred, Wicked und Arcane an, die brauchst du zuerst.",
          ],
          tasks=[task_item("malum:sacred_spirit", 8), task_item("malum:wicked_spirit", 8),
                 task_item("malum:arcane_spirit", 8)],
          rewards=[reward_item("minecraft:gunpowder", 8), reward_xp(5)],
          deps=["scythe"], icon="malum:arcane_spirit"),

    quest("altar", 8.7, 0, "&6Spirit Altar",
          subtitle="Arcana fließen in ein Item.",
          description=[
              "Der &6Spirit Altar&r ist ein &6Refined Soulstone&r über &e2 Goldbarren&r und &e4 Runewood-Brettern&r. Leg das Haupt-Item darauf und dazu die nötigen Spirit Arcana, beides mit Rechtsklick.",
              "",
              "Braucht ein Rezept weitere Zutaten, kommen sie auf &6Runewood Item Stands&r oder &6Item Pedestals&r im Umkreis von &e4 Blöcken&r. Sobald alles da ist, fließen die Arcana in das Item, die Nebenzutaten werden hineingezogen, und am Ende liegt das Ergebnis da. Ziemlich langsam, aber du musst nichts tun.",
          ],
          tasks=[task_item("malum:spirit_altar", 1), task_item("malum:runewood_item_stand", 4)],
          rewards=[reward_item("malum:runewood_planks", 16), reward_xp(5)],
          deps=["spirits", "runewood"], icon="malum:spirit_altar", size=1.5, shape="diamond"),

    # ---- Der Geisteraltar --------------------------------------------------------
    quest("hex_ash", 0.5, 5.5, "&6Hex Ash",
          subtitle="Die Grundzutat für fast alles.",
          description=[
              "Die erste Infusion: &6Schwarzpulver&r auf den Altar und &e1 Arcane&r dazu. Heraus kommt &6Hex Ash&r.",
              "",
              "Hex Ash steckt in Totembasen, im Spirit Crucible, in der verbesserten Sense und vielen Rezepten später. Mach gleich einen Stapel.",
          ],
          tasks=[task_item("malum:hex_ash", 16)],
          rewards=[reward_item("minecraft:gunpowder", 16)],
          deps=["altar"], icon="malum:hex_ash"),

    quest("hallowed_gold", 2.5, 5.5, "&eHallowed Gold",
          subtitle="Ein Leiter für Arcana.",
          description=[
              "Ein &6Goldbarren&r auf dem Altar, &e4 Quarz&r auf den Ablagen, dazu &e2 Sacred&r und &e1 Arcane&r. Das Ergebnis ist &eHallowed Gold&r.",
              "",
              "Arcana gleiten durch Hallowed Gold wie Strom durch Kupfer. Es steckt in Spirit Jars, in den Runewood-Obelisken, die den Altar beschleunigen, und in Schmuck, der dich wie leichte Rüstung schützt.",
          ],
          tasks=[task_item("malum:hallowed_gold_ingot", 4)],
          rewards=[reward_item("minecraft:quartz", 16), reward_xp(5)],
          deps=["hex_ash"], icon="malum:hallowed_gold_ingot"),

    quest("spirit_jar", 2.5, 7.7, "&6Spirit Jar",
          subtitle="Ordnung für die Kristalle.",
          description=[
              "Ein &6Spirit Jar&r ist ein Hallowed-Gold-Barren über Glas. Jedes Glas fasst nahezu unbegrenzt viele Arcana, aber nur eine Sorte.",
              "",
              "Stell dir acht Gläser neben den Altar, eins für jede Sorte, dann bleibt das Inventar frei.",
          ],
          tasks=[task_item("malum:spirit_jar", 4)],
          rewards=[reward_item("minecraft:glass", 8)],
          deps=["hallowed_gold"], icon="malum:spirit_jar", optional=True),

    quest("soul_steel", 4.7, 6.6, "&5Soul Stained Steel",
          subtitle="Ein Metall in zwei Welten.",
          description=[
              "Ein &6Eisenbarren&r auf dem Altar, &e4 Refined Soulstone&r auf den Ablagen, dazu &e3 Wicked&r, &e1 Earthen&r und &e1 Arcane&r. Heraus kommt &5Soul Stained Steel&r, ein Stahl, der zugleich in dieser Welt und außerhalb steckt.",
              "",
              "Alles daraus trifft die Seele mit: Werkzeuge, Waffen, die bessere Sense. Rüstung aus reinem Seelenstahl berührt allerdings auch deine eigene Seele, darum gibt es dafür eigene Rezepte.",
              "",
              "&eKronwerke:&r Der &6Soul Binder&r von Ender IO braucht auf Kronwerke Seelenstahl statt Soularium. Die Seelen-Seite von Ender IO kommt also von Malum. Bring den Tech-Leuten ein paar Barren, dann können sie Mob-Spawner und Seelen-Rezepte bauen.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 8)],
          rewards=[reward_table("s3_uncommon"), reward_xp(10)],
          deps=["hex_ash", "soulstone"], icon="malum:soul_stained_steel_ingot", size=1.75, shape="diamond"),

    quest("soul_scythe", 6.9, 5.5, "&5Soul Stained Steel Scythe",
          subtitle="Die alte Sense, aber besser.",
          description=[
              "Die &6Crude Scythe&r auf den Altar, auf die Ablagen &e4 Soul Stained Steel&r, &e2 Hex Ash&r und &e4 Refined Soulstone&r. Dazu &e16 Earthen&r, &e8 Wicked&r und &e8 Arcane&r.",
              "",
              "Verzauberungen der alten Sense bleiben erhalten. Die neue schlägt härter und hält länger, und sie erntet weiterhin Arcana.",
          ],
          tasks=[task_item("malum:soul_stained_steel_scythe", 1)],
          rewards=[reward_item("malum:earthen_spirit", 16), reward_xp(5)],
          deps=["soul_steel"], icon="malum:soul_stained_steel_scythe", optional=True),

    # ---- Tiegel und Fokus --------------------------------------------------------
    quest("rocks", 0.5, 11.5, "&7Twisted und Tainted Rock",
          subtitle="Zwei Steine mit entgegengesetzter Ladung.",
          description=[
              "Auf dem Altar: &e16 Stein&r mit &e1 Wicked&r und &e1 Arcane&r werden zu &6Twisted Rock&r, mit &e1 Sacred&r und &e1 Arcane&r zu &6Tainted Rock&r. Je 16 Stück pro Durchgang.",
              "",
              "Die beiden Steine ziehen Arcana in entgegengesetzte Richtungen. Zusammen bilden sie den Spirit Crucible.",
          ],
          tasks=[task_item("malum:twisted_rock", 16), task_item("malum:tainted_rock", 16)],
          rewards=[reward_item("minecraft:stone", 64)],
          deps=["hex_ash"], icon="malum:twisted_rock"),

    quest("crucible", 2.5, 11.5, "&cSpirit Crucible",
          subtitle="Arcana bündeln statt einfüllen.",
          description=[
              "Der &6Spirit Crucible&r ist ein infundierter &6Ofen&r: auf die Ablagen &e8 Twisted Rock&r, &e8 Tainted Rock&r und &e2 Hex Ash&r, dazu &e8 Infernal&r und &e8 Aqueous&r.",
              "",
              "Im Crucible steckt ein Katalysator, um den herum Arcana gebündelt werden. Mit jedem Durchgang verliert der Katalysator etwas Haltbarkeit. Gehen die Werkzeuge kaputt, repariert sie später ein &6Repair Pylon&r gegen Arcana.",
          ],
          tasks=[task_item("malum:spirit_crucible", 1)],
          rewards=[reward_item("malum:infernal_spirit", 8), reward_xp(5)],
          deps=["rocks"], icon="malum:spirit_crucible"),

    quest("calx", 0.5, 13.7, "&6Alchemical Calx",
          subtitle="Ton, aber magisch.",
          description=[
              "&e4 Tonklumpen&r auf dem Altar, dazu je &e2 Arcane&r, &e2 Earthen&r und &e2 Aqueous&r ergeben &e4 Alchemical Calx&r. Unter starkem Druck fest, unter leichtem weich wie Talg.",
              "",
              "Calx ist die Basis für den Alchemical Impetus.",
          ],
          tasks=[task_item("malum:alchemical_calx", 4)],
          rewards=[reward_item("minecraft:clay_ball", 16)],
          deps=["rocks"], icon="malum:alchemical_calx"),

    quest("impetus", 4.5, 12.6, "&6Alchemical Impetus",
          subtitle="Der Katalysator für den Crucible.",
          description=[
              "&e4 Alchemical Calx&r auf den Altar, auf die Ablagen &e4 Refined Soulstone&r und &e2 Hex Ash&r, dazu &e4 Arcane&r und &e4 Earthen&r.",
              "",
              "In den Crucible gelegt und mit unterschiedlichen Arcana gefüttert, entstehen daraus verschiedene Pulver und Reagenzien. Was genau, zeigt dir JEI beim Crucible.",
          ],
          tasks=[task_item("malum:alchemical_impetus", 1)],
          rewards=[reward_item("malum:arcane_spirit", 8), reward_xp(5)],
          deps=["crucible", "calx"], icon="malum:alchemical_impetus"),

    quest("nodes", 6.7, 12.6, "&6Metal Nodes",
          subtitle="Erz ohne Spitzhacke.",
          description=[
              "Für Metalle wird der Impetus umgebaut. Der &6Iron Impetus&r: Alchemical Impetus auf den Altar, &e6 Eisenbarren&r, &e4 Schwarzpulver&r und ein &6Cthonic Gold&r auf die Ablagen, dazu je &e8 Earthen&r, &e8 Infernal&r und &e8 Aqueous&r.",
              "",
              "&6Cthonic Gold&r ist ein seltenes Erz im Tiefenschiefer zwischen Y 0 und Y -48, eng an Goldadern.",
              "",
              "Im Crucible mit &e2 Earthen&r und &e2 Infernal&r macht der Iron Impetus &e3 Iron Nodes&r und verliert dabei Haltbarkeit. Eine Node gibt im Ofen Nuggets für zwei Drittel eines Barrens. Nicht schnell, aber besser, als jeden Barren zu graben. Andere Metalle haben ihren eigenen Impetus.",
          ],
          tasks=[task_item("malum:iron_node", 6)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["impetus"], icon="malum:iron_node", optional=True),

    # ---- Totems und Riten --------------------------------------------------------
    quest("totem_base", 11, 5.5, "&2Runewood Totem Base",
          subtitle="Der Fuß jedes Totems.",
          description=[
              "Totems brauchen alle fünf Elementar-Arcana. Auf den Altar &e4 Runewood Logs&r, auf die Ablagen &e6 Runewood-Bretter&r und &e2 Hex Ash&r, dazu je &e2 Aerial&r, &e2 Aqueous&r, &e2 Earthen&r, &e2 Infernal&r und &e2 Eldritch&r. Das gibt vier Totembasen.",
              "",
              "Eldritch ist die schwierigste Sorte. Endermen geben am verlässlichsten welches.",
          ],
          tasks=[task_item("malum:runewood_totem_base", 4)],
          rewards=[reward_item("malum:runewood_log", 16), reward_xp(5)],
          deps=["hallowed_gold"], icon="malum:runewood_totem_base"),

    quest("healing_rite", 13, 5.5, "&2Rite of Healing",
          subtitle="Ein Totem, das Wunden schließt.",
          description=[
              "Stell Runewood Logs senkrecht auf die Totembasis. Rechtsklick mit einem Spirit Arcana auf die Seite eines Stamms schnitzt eine &eRune&r hinein und verbraucht den Kristall. Mit einer Axt kratzt du eine falsche Rune wieder ab.",
              "",
              "Ein einfacher Ritus braucht drei Runen: ein &dArcane&r und zwei seines Elements. Mit &dArcane&r und zwei &eSacred&r wird das der &2Rite of Healing&r, der alle in der Nähe langsam heilt. Die Encyclopedia zeigt dir die genaue Anordnung.",
              "",
              "Rechtsklick auf die Basis startet den Ritus, noch ein Rechtsklick beendet ihn. Mit dem &6Totemic Staff&r (Stöcke und ein Runewood-Brett) in der Hand siehst du, wie weit ein Totem reicht.",
          ],
          tasks=[task_item("malum:totemic_staff", 1), task_checkmark("Rite of Healing gestartet")],
          rewards=[reward_item("malum:sacred_spirit", 16), reward_xp(5)],
          deps=["totem_base"], icon="malum:sacred_spirit"),

    quest("quickening", 13, 7.7, "&cRite of Quickening",
          subtitle="Der Ofen schläft nie.",
          description=[
              "Ein fortgeschrittener Ritus braucht vier Runen: &5Eldritch&r, &dArcane&r und zwei seines Elements. Mit zwei &cInfernal&r wird das der &cRite of Quickening&r.",
              "",
              "Der Ritus webt einen &eRite Locus&r, einen Funken, der durch die Gegend wandert. Kommt er über einen Ofen, Hochofen oder Räucherofen, schmilzt dieser deutlich schneller. Der Brennstoffverbrauch bleibt im Verhältnis gleich.",
              "",
              "&eKronwerke:&r Das Stufenziel heißt \"Der Ofen schläft nie\". Stell ein Quickening-Totem in eure Ofenhalle, und eure Öfen laufen schneller.",
          ],
          tasks=[task_checkmark("Rite of Quickening gestartet")],
          rewards=[reward_item("malum:infernal_spirit", 16), reward_item("minecraft:coal_block", 8), reward_xp(10)],
          deps=["healing_rite"], icon="malum:infernal_spirit"),

    # ---- Ziel --------------------------------------------------------------------
    quest("soulsmith", 17, 9.5, "&5Seelenschmied",
          subtitle="Ernten, infundieren, schmieden.",
          description=[
              "Du erntest Seelen mit der Sense, infundierst am Altar, bündelst im Crucible und lässt Totems für dich arbeiten. Das ist das Handwerk von Malum.",
              "",
              "&eKronwerke:&r Seelenstahl ist das Bindeglied zu Ender IO, Hallowed Gold zu den besseren Totems und Riten. Leg einen Vorrat an, die Tech-Leute fragen bestimmt.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 16), task_item("malum:hallowed_gold_ingot", 8)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["soul_steel", "impetus", "quickening"], icon="malum:soul_stained_steel_ingot", size=2.5, shape="gear"),
]

images = [
    banner("malum/title", "Malum", 4.5, -4.4, height=1.8, kind="title", colour="magic"),
    banner("malum/ernten", "Seelen ernten", 4.5, -2.5, height=0.9, colour="magic"),
    banner("malum/altar", "Der Geisteraltar", 3.7, 3.9, height=0.9, colour="magic"),
    banner("malum/totems", "Totems und Riten", 12, 3.9, height=0.9, colour="nature"),
    banner("malum/tiegel", "Tiegel und Fokus", 3.5, 9.9, height=0.9, colour="fire"),
]

chapter(C, "Malum", "malum:spirit_altar", "magic", quests, shape="circle", order=29, stage=3,
        subtitle=["Stufe 3. Seelen ernten, Altar, Crucible und Totems."], images=images)
