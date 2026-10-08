"""Malum in stage 3 (the whole mod opens with stage 3): soulstone and runewood, the crude scythe,
the eight spirit arcana as a checklist with the mobs that drop them (data/malum/spirit_data), the
spirit altar with hex ash, hallowed gold, spirit jars, runewood obelisks and arcane charcoal, soul
stained steel with its tools and scythe and the Ender IO soul binder it feeds on Kronwerke
(kubejs tech.js), soulwoven silk and soul hunter armor, the spirit crucible with alchemical calx,
the impetus, metal nodes and the first ring, and totem magic with the rite of healing and the
rite of quickening. Infusion numbers from recipe/spirit_infusion in the malum 1.8.2 jar."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner)

C = "malum"


def spirit(name, x, y, title, colour_name, item, sources, use, deps=("spirits",)):
    """One spirit arcana of the checklist: who drops it, what it is for."""
    return quest(name, x, y, title, subtitle=f"{colour_name} Arcana.",
                 description=[sources, "", use],
                 tasks=[task_item(item, 8)],
                 rewards=[reward_item(item, 4), reward_xp(3)],
                 deps=list(deps), icon=item, shape="square")


quests = [
    # ---- Seelen ernten ---------------------------------------------------------
    quest("welcome", 0, 0, "&5&lSchlag die Encyclopedia Arcana auf",
          subtitle="Magie aus zerbrochenen Seelen.",
          description=[
              "Ein &6Buch&r und ein &6Refined Soulstone&r, formlos.",
              "",
              "&5Malum&r arbeitet mit Seelen. Was mit der richtigen Klinge stirbt, lässt &dSpirit Arcana&r fallen. Damit infundierst du Items, schmiedest Metalle und baust Totems. Die Mod öffnet mit &6Stufe 3&r.",
              "",
              "&6Soulstone&r ist ein häufiges Erz. Das rohe Stück gibt im Ofen Refined Soulstone.",
          ],
          tasks=[task_item("malum:encyclopedia_arcana", 1)],
          rewards=[reward_item("malum:raw_soulstone", 8), reward_table("s3_common")],
          icon="malum:encyclopedia_arcana", size=2.0, shape="hexagon"),

    quest("soulstone", 2.5, -1, "&7Bau Soulstone ab",
          subtitle="Stein, der halb in einer anderen Welt steckt.",
          description=[
              "Bau &6Soulstone-Erz&r ab und schmilz das rohe Stück.",
              "",
              "Leg einen Vorrat an. Seelenstahl will vier Refined Soulstone pro Barren, der Impetus und die bessere Sense auch je vier.",
          ],
          tasks=[task_item("malum:refined_soulstone", 32)],
          rewards=[reward_item("malum:raw_soulstone", 16), reward_xp(3)],
          deps=["welcome"], icon="malum:refined_soulstone"),

    quest("runewood", 2.5, 1, "&6Fäll Runewood",
          subtitle="Eiche, vollgesogen mit Magie.",
          description=[
              "Runewood erkennst du an den orange-gelben Blättern, vor allem auf großen Ebenen. Pflanz Setzlinge zu Hause an.",
              "",
              "Daraus: Geisteraltar, Ablagen, Obelisken und Totems. &eTipp:&r Klebrige Stellen am Stamm geben entrindet &6Runic Sap&r in die Flasche.",
          ],
          tasks=[task_item("malum:runewood_log", 16)],
          rewards=[reward_item("malum:runewood_sapling", 4), reward_xp(3)],
          deps=["welcome"], icon="malum:runewood_sapling"),

    quest("scythe", 5, -1, "&5Schmiede eine Crude Scythe",
          subtitle="Eine Klinge, die auch die Seele trifft.",
          description=[
              "Oben &6zwei Eisenbarren&r und ein &6Refined Soulstone&r. Darunter ein Stock und ein Eisenbarren, unten links ein Stock.",
              "",
              "Nur was mit der Sense stirbt, lässt Arcana fallen. Sie schlägt auch seitlich mit. Halt sie griffbereit in der Hotbar.",
          ],
          tasks=[task_item("malum:crude_scythe", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 4), reward_xp(4)],
          deps=["soulstone"], icon="malum:crude_scythe"),

    quest("spirits", 7.5, -1, "&dErnte die ersten Arcana",
          subtitle="Sacred, Wicked, Arcane.",
          description=[
              "Mit der Sense: &6Schweine&r und &6Hühner&r für &eSacred&r, &6Zombies&r für &5Wicked&r, &6Skelette&r und &6Hexen&r für &dArcane&r.",
              "",
              "Diese drei brauchst du zuerst: Hex Ash, Hallowed Gold, Seelenstahl. Die anderen fünf stehen rechts als Checkliste.",
          ],
          tasks=[task_item("malum:sacred_spirit", 8), task_item("malum:wicked_spirit", 8),
                 task_item("malum:arcane_spirit", 8)],
          rewards=[reward_item("minecraft:gunpowder", 8), reward_xp(5)],
          deps=["scythe"], icon="malum:arcane_spirit"),

    # ---- Die acht Arcana (Checkliste) -----------------------------------------------
    spirit("sp_earthen", 10, -2.5, "&6Earthen", "Erdige",
           "malum:earthen_spirit",
           "&6Kühe&r, &6Schafe&r und &6Zombies&r geben je eins, ein &6Eisengolem&r fünf.",
           "Für Seelenstahl, Calx, Impetus und die Rüstung."),
    spirit("sp_infernal", 12.5, -2.5, "&cInfernal", "Höllische",
           "malum:infernal_spirit",
           "&6Creeper&r geben drei, &6Blazes&r drei, Piglins und Zombie-Piglins zwei.",
           "Für den Spirit Crucible, Arcane Charcoal und den Rite of Quickening."),
    spirit("sp_aerial", 10, -0.5, "&fAerial", "Luftige",
           "malum:aerial_spirit",
           "&6Spinnen&r, &6Hühner&r, &6Fledermäuse&r und &6Kaninchen&r. Phantome geben drei.",
           "Für Obelisken, Soulwoven Silk und Totembasen."),
    spirit("sp_aqueous", 12.5, -0.5, "&bAqueous", "Wässrige",
           "malum:aqueous_spirit",
           "&6Ertrunkene&r und &6Tintenfische&r geben zwei, Fische eins, &6Wächter&r drei.",
           "Für Calx, den Spirit Crucible und den Impetus."),
    spirit("sp_eldritch", 15, -1.5, "&5Eldritch", "Unheimliche",
           "malum:eldritch_spirit",
           "&6Endermen&r geben drei, Endermites eins, ein &6Verwüster&r vier.",
           "Die seltenste Sorte. Für Totembasen und den Rite of Quickening.",
           deps=("sp_earthen", "sp_infernal", "sp_aerial", "sp_aqueous")),

    # ---- Der Geisteraltar --------------------------------------------------------
    quest("altar", 0, 5, "&6&lBau einen Spirit Altar",
          subtitle="Arcana fließen in ein Item.",
          description=[
              "Oben ein &6Refined Soulstone&r, Mitte &6Arcane Gold&r aus Eidolon, &6Runewood-Brett, Arcane Gold&r, unten drei &6Runewood-Bretter&r. Dazu &6Runewood Item Stands&r: drei Stufen über drei Brettern, gibt zwei.",
              "",
              "Haupt-Item und Arcana auf den Altar, Nebenzutaten auf Stands im Umkreis von &e4 Blöcken&r. Dann wartest du.",
          ],
          tasks=[task_item("malum:spirit_altar", 1), task_item("malum:runewood_item_stand", 4)],
          rewards=[reward_item("malum:runewood_planks", 16), reward_xp(5)],
          deps=["spirits", "runewood"], icon="malum:spirit_altar", size=1.5, shape="diamond"),

    quest("hex_ash", 2.5, 5, "&7Infundier Hex Ash",
          subtitle="Die Grundzutat für fast alles.",
          description=[
              "&6Schwarzpulver&r auf den Altar und &e1 Arcane&r dazu: Hex Ash.",
              "",
              "Steckt in Totembasen, Spirit Crucible, Impetus und der besseren Sense. Mach einen Stapel.",
          ],
          tasks=[task_item("malum:hex_ash", 16)],
          rewards=[reward_item("minecraft:gunpowder", 16), reward_xp(4)],
          deps=["altar"], icon="malum:hex_ash"),

    quest("hallowed_gold", 5, 5, "&eWeih Hallowed Gold",
          subtitle="Ein Leiter für Arcana.",
          description=[
              "Ein &6Goldbarren&r auf den Altar, &e4 Quarz&r auf die Stands, dazu &e2 Sacred&r und &e1 Arcane&r.",
              "",
              "Arcana gleiten durch Hallowed Gold wie Strom durch Kupfer. Es steckt in Spirit Jars, Obelisken und Schmuck.",
          ],
          tasks=[task_item("malum:hallowed_gold_ingot", 4)],
          rewards=[reward_item("minecraft:quartz", 16), reward_xp(5)],
          deps=["hex_ash"], icon="malum:hallowed_gold_ingot"),

    quest("spirit_jar", 5, 7.2, "&7Füll Spirit Jars",
          subtitle="Ordnung für die Kristalle.",
          description=[
              "Ein &6Hallowed Gold&r über einem &6Glas&r.",
              "",
              "Jedes Glas fasst nahezu unbegrenzt viele Arcana, aber nur eine Sorte. Acht Gläser neben dem Altar halten das Inventar frei.",
          ],
          tasks=[task_item("malum:spirit_jar", 4)],
          rewards=[reward_item("minecraft:glass", 8)],
          deps=["hallowed_gold"], icon="malum:spirit_jar", optional=True),

    quest("obelisk", 7.5, 7.2, "&eStell Runewood-Obelisken auf",
          subtitle="Der Altar wird schneller.",
          description=[
              "&6Zwei Runewood-Bretter&r auf den Altar, &6zwei Hallowed Gold&r auf die Stands, dazu &e16 Aerial&r und &e8 Sacred&r.",
              "",
              "Bis zu &evier&r Obelisken in der Nähe beschleunigen jede Infusion. Ein Stapel Hex Ash dauert sonst Minuten.",
          ],
          tasks=[task_item("malum:runewood_obelisk", 2)],
          rewards=[reward_item("malum:aerial_spirit", 16), reward_xp(6)],
          deps=["spirit_jar", "sp_aerial"], icon="malum:runewood_obelisk"),

    quest("charcoal", 2.5, 7.2, "&7Infundier Arcane Charcoal",
          subtitle="Brennt länger als Holzkohle.",
          description=[
              "&6Vier Kohle&r oder Holzkohle auf den Altar, &e1 Arcane&r und &e2 Infernal&r: vier Arcane Charcoal.",
              "",
              "Ein besserer Brennstoff für Öfen und Feuerschalen, zum Beispiel für Theurgy.",
          ],
          tasks=[task_item("malum:arcane_charcoal", 8)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(4)],
          deps=["hex_ash", "sp_infernal"], icon="malum:arcane_charcoal", optional=True),

    quest("soul_steel", 7.5, 5, "&5&lSchmiede Soul Stained Steel",
          subtitle="Ein Metall in zwei Welten.",
          description=[
              "Ein &6Eisenbarren&r auf den Altar, &e4 Refined Soulstone&r auf die Stands, dazu &e3 Wicked&r, &e1 Earthen&r und &e1 Arcane&r.",
              "",
              "Alles aus Seelenstahl trifft die Seele mit: Werkzeug, Waffen, die bessere Sense.",
              "",
              "&eKronwerke:&r Der &6Soul Binder&r von Ender IO braucht hier &e4 Seelenstahl&r statt Soularium. Die Seelen-Seite von Ender IO kommt von Malum.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 8)],
          rewards=[reward_table("s3_uncommon"), reward_xp(10)],
          deps=["hex_ash", "sp_earthen"], icon="malum:soul_stained_steel_ingot", size=1.75, shape="diamond"),

    quest("soul_tools", 10, 4, "&7Schmiede Seelenstahl-Werkzeug",
          subtitle="Ernten mit jeder Klinge.",
          description=[
              "Wie Vanilla-Werkzeug: drei &6Seelenstahl&r und zwei Stöcke für die Spitzhacke, zwei und einer fürs Schwert.",
              "",
              "Seelenstahl-Waffen lassen auch ohne Sense Arcana fallen.",
          ],
          tasks=[task_item("malum:soul_stained_steel_sword", 1)],
          rewards=[reward_item("malum:wicked_spirit", 8), reward_xp(5)],
          deps=["soul_steel"], icon="malum:soul_stained_steel_sword", optional=True),

    quest("soul_scythe", 10, 6, "&5Verbessere die Sense",
          subtitle="Die alte Sense, aber stärker.",
          description=[
              "&6Crude Scythe&r auf den Altar, auf die Stands &e4 Seelenstahl&r, &e2 Hex Ash&r und &e4 Refined Soulstone&r. Dazu &e16 Earthen&r, &e8 Wicked&r und &e8 Arcane&r.",
              "",
              "Verzauberungen bleiben. Sie schlägt härter, hält länger und erntet weiter Arcana.",
          ],
          tasks=[task_item("malum:soul_stained_steel_scythe", 1)],
          rewards=[reward_item("malum:earthen_spirit", 16), reward_xp(7)],
          deps=["soul_steel"], icon="malum:soul_stained_steel_scythe"),

    quest("soul_binder", 12.5, 5, "&3Bring Seelenstahl zu Ender IO",
          subtitle="Der Soul Binder auf Kronwerke.",
          description=[
              "&eRezept auf Kronwerke:&r vier &6Seelenstahl&r in den Ecken, oben ein leeres &6Soul Vial&r, Mitte &6Energized Gear, Ensouled Chassis, Energized Gear&r, unten ein &6Z-Logic Controller&r.",
              "",
              "Der Soul Binder macht Spawner-Rezepte und Seelen-Items von Ender IO. Bau ihn selbst oder bring den Tech-Leuten die Barren.",
          ],
          tasks=[task_item("enderio:soul_binder", 1)],
          rewards=[reward_item("malum:soul_stained_steel_ingot", 4), reward_xp(8)],
          deps=["soul_steel"], icon="enderio:soul_binder", optional=True),

    quest("silk", 0, 9.5, "&7Web Soulwoven Silk",
          subtitle="Stoff für Seelenjäger.",
          description=[
              "&6Zwei Wolle&r auf den Altar, &6zwei Fäden&r auf die Stands, dazu &e3 Aerial&r und &e3 Earthen&r.",
              "",
              "Steckt in der Soul-Hunter-Rüstung und im Soulwoven Pouch.",
          ],
          tasks=[task_item("malum:soulwoven_silk", 4)],
          rewards=[reward_item("minecraft:white_wool", 8), reward_xp(4)],
          deps=["hex_ash", "sp_aerial"], icon="malum:soulwoven_silk", optional=True),

    quest("soul_hunter", 2.5, 9.5, "&7Kleid dich als Seelenjäger",
          subtitle="Leichte Rüstung aus Seidentuch.",
          description=[
              "Ein &6Lederhelm&r auf den Altar, auf die Stands &e4 Soulwoven Silk&r, &e4 Refined Soulstone&r, &e2 Leder&r, dazu &e8 Aerial&r und &e8 Earthen&r. Robe, Hose, Stiefel genauso.",
              "",
              "Seelenstahl als Rüstung berührt die eigene Seele. Das Seidentuch ist der Ausweg.",
          ],
          tasks=[task_item("malum:soul_hunter_cloak", 1)],
          rewards=[reward_item("minecraft:leather", 8), reward_xp(5)],
          deps=["silk"], icon="malum:soul_hunter_cloak", optional=True),

    # ---- Tiegel und Fokus --------------------------------------------------------
    quest("rocks", 0, 13, "&7Infundier Twisted und Tainted Rock",
          subtitle="Zwei Steine mit entgegengesetzter Ladung.",
          description=[
              "&e16 Stein&r auf den Altar. Mit &e1 Wicked&r und &e1 Arcane&r: &6Twisted Rock&r. Mit &e1 Sacred&r und &e1 Arcane&r: &6Tainted Rock&r. Je 16 Stück.",
              "",
              "Zusammen bilden sie den Spirit Crucible.",
          ],
          tasks=[task_item("malum:twisted_rock", 16), task_item("malum:tainted_rock", 16)],
          rewards=[reward_item("minecraft:stone", 64), reward_xp(4)],
          deps=["hex_ash"], icon="malum:twisted_rock"),

    quest("crucible", 2.5, 13, "&cBau den Spirit Crucible",
          subtitle="Arcana bündeln statt einfüllen.",
          description=[
              "Ein &6Ofen&r auf den Altar, auf die Stands &e8 Twisted Rock&r, &e8 Tainted Rock&r und &e2 Hex Ash&r, dazu &e8 Infernal&r und &e8 Aqueous&r.",
              "",
              "Im Crucible steckt ein Katalysator, um den Arcana gebündelt werden. Jeder Durchgang kostet ihn Haltbarkeit.",
          ],
          tasks=[task_item("malum:spirit_crucible", 1)],
          rewards=[reward_item("malum:infernal_spirit", 8), reward_xp(6)],
          deps=["rocks", "sp_aqueous"], icon="malum:spirit_crucible"),

    quest("calx", 0, 15.2, "&6Infundier Alchemical Calx",
          subtitle="Ton, aber magisch.",
          description=[
              "&e4 Tonklumpen&r auf den Altar, je &e2 Arcane&r, &e2 Earthen&r und &e2 Aqueous&r: vier Calx.",
              "",
              "Die Basis für Impetus, Ringe und viele Bauteile.",
          ],
          tasks=[task_item("malum:alchemical_calx", 4)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_xp(4)],
          deps=["rocks"], icon="malum:alchemical_calx"),

    quest("impetus", 5, 14, "&6Infundier einen Alchemical Impetus",
          subtitle="Der Katalysator für den Crucible.",
          description=[
              "&e4 Calx&r auf den Altar, auf die Stands &e4 Refined Soulstone&r und &e2 Hex Ash&r, dazu &e4 Arcane&r und &e4 Earthen&r.",
              "",
              "Im Crucible mit unterschiedlichen Arcana entstehen daraus Pulver und Reagenzien, JEI zeigt welche.",
          ],
          tasks=[task_item("malum:alchemical_impetus", 1)],
          rewards=[reward_item("malum:arcane_spirit", 8), reward_xp(7)],
          deps=["crucible", "calx"], icon="malum:alchemical_impetus"),

    quest("nodes", 7.5, 14, "&6Fokussier Iron Nodes",
          subtitle="Erz ohne Spitzhacke.",
          description=[
              "&6Iron Impetus&r: Impetus auf den Altar, &e6 Eisenbarren&r, &e4 Schwarzpulver&r und &e1 Cthonic Gold&r auf die Stands, je &e8 Earthen, Infernal, Aqueous&r. In den Crucible mit &e2 Earthen&r und &e2 Infernal&r.",
              "",
              "Pro Durchgang &edrei Iron Nodes&r, der Impetus verliert 2 Haltbarkeit. Nodes schmilzt du zu Nuggets. Kupfer, Gold, Blei, Osmium und mehr haben eigene Impetus.",
              "",
              "&6Cthonic Gold&r ist ein seltenes Erz tief im Tiefenschiefer, nahe an Goldadern.",
          ],
          tasks=[task_item("malum:iron_node", 6)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(8)],
          deps=["impetus"], icon="malum:iron_node", optional=True),

    quest("ring", 2.5, 15.2, "&dSchmied einen Heilring",
          subtitle="Ring of Curative Talent.",
          description=[
              "&6Gilded Ring&r (Hallowed Gold und Leder) auf den Altar. Auf die Stands &e4 Living Flesh&r, &e4 Calx&r, &e1 Ghast Tear&r. Dazu &e16 Sacred&r und &e16 Arcane&r.",
              "",
              "Jedes Mal, wenn du Arcana aufsammelst, heilt er dich ein Stück. Living Flesh: vier Verrottetes Fleisch, 2 Sacred, 2 Wicked.",
          ],
          tasks=[task_item("malum:ring_of_curative_talent", 1)],
          rewards=[reward_item("malum:sacred_spirit", 16), reward_xp(7)],
          deps=["calx", "hallowed_gold"], icon="malum:ring_of_curative_talent", optional=True),

    # ---- Totems und Riten --------------------------------------------------------
    quest("totem_base", 15, 4, "&2Infundier Totembasen",
          subtitle="Der Fuß jedes Totems.",
          description=[
              "&e4 Runewood Logs&r auf den Altar, &e6 Runewood-Bretter&r und &e2 Hex Ash&r auf die Stands, dazu je &e2 Aerial, Aqueous, Earthen, Infernal, Eldritch&r. Gibt vier.",
              "",
              "Eldritch ist die schwierigste Sorte. Endermen geben am verlässlichsten welches.",
          ],
          tasks=[task_item("malum:runewood_totem_base", 4)],
          rewards=[reward_item("malum:runewood_log", 16), reward_xp(6)],
          deps=["hallowed_gold", "sp_eldritch"], icon="malum:runewood_totem_base"),

    quest("healing_rite", 17.5, 4, "&2Zünde den Rite of Healing",
          subtitle="Ein Totem, das Wunden schließt.",
          description=[
              "Runewood Logs senkrecht auf die Basis. Rechtsklick mit einem Arcana schnitzt eine Rune: ein &dArcane&r und zwei &eSacred&r. Rechtsklick auf die Basis startet.",
              "",
              "Alle in der Nähe heilen langsam. Eine Axt kratzt falsche Runen ab. Der &6Totemic Staff&r (zwei Stöcke, ein Runewood-Brett) zeigt die Reichweite.",
          ],
          tasks=[task_item("malum:totemic_staff", 1), task_checkmark("Rite of Healing gestartet")],
          rewards=[reward_item("malum:sacred_spirit", 16), reward_xp(7)],
          deps=["totem_base"], icon="malum:sacred_spirit"),

    quest("quickening", 17.5, 6.2, "&cZünde den Rite of Quickening",
          subtitle="Der Ofen schläft nie.",
          description=[
              "Vier Runen: &5Eldritch&r, &dArcane&r und zwei &cInfernal&r, aber auf einem Totem aus &6Soulwood&r. Auf Runenholz geben dieselben Runen den &eRite of Smelting&r, der Blöcke unter dem Funken schmilzt.",
              "",
              "Der Ritus webt einen &eRite Locus&r, einen wandernden Funken. Öfen, Hochöfen und Räucheröfen, über die er kommt, schmelzen schneller. Der Brennstoff reicht dabei genauso weit wie sonst.",
              "",
              "Soulwood bekommst du mit dem &eUnchained Rite&r, er verwandelt Runenholz. Die Totembasis machst du aus Soulwood in der Geistinfusion.",
              "",
              "&eKronwerke:&r Stell ein Quickening-Totem in eure Ofenhalle. Das passt zum Stufenziel \"Der Ofen schläft nie\".",
          ],
          tasks=[task_checkmark("Rite of Quickening gestartet")],
          rewards=[reward_item("malum:infernal_spirit", 16), reward_item("minecraft:coal_block", 8), reward_xp(10)],
          deps=["healing_rite"], icon="malum:infernal_spirit"),

    # ---- Ziel --------------------------------------------------------------------
    quest("soulsmith", 15, 10, "&5&lWerd zum Seelenschmied",
          subtitle="Ernten, infundieren, schmieden.",
          description=[
              "16 &6Seelenstahl&r und 8 &6Hallowed Gold&r im Inventar.",
              "",
              "Du erntest Seelen, infundierst am Altar, bündelst im Crucible und lässt Totems arbeiten.",
              "",
              "&eKronwerke:&r Seelenstahl ist das Bindeglied zu Ender IO. Leg einen Vorrat an, die Tech-Leute fragen bestimmt.",
          ],
          tasks=[task_item("malum:soul_stained_steel_ingot", 16), task_item("malum:hallowed_gold_ingot", 8)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["soul_scythe", "impetus", "quickening"], icon="malum:soul_stained_steel_ingot", size=2.5, shape="gear"),

    # ---- Neue Quests -------------------------------------------------------------
    quest("pouch", 5, 9.5, "&7Näh einen Soulwoven Pouch",
          subtitle="Arcana landen nicht mehr im Inventar.",
          description=[
              "Ein &6Faden&r über einer &6Soulwoven Silk&r.",
              "",
              "Der Beutel funktioniert wie ein Bündel, schnappt sich aber jedes Arcana, das du aufsammelst. Magische Items nehmen darin weniger Platz ein. Nach ein paar Stunden Ernten mit der Sense dankt dir dein Inventar.",
          ],
          tasks=[task_item("malum:soulwoven_pouch", 1)],
          rewards=[reward_item("malum:soulwoven_silk", 2), reward_xp(4)],
          deps=["silk"], icon="malum:soulwoven_pouch", optional=True),

    quest("brilliance", 10, 8.2, "&bBau Brilliance ab",
          subtitle="Erfahrung, zu Stein geworden.",
          description=[
              "&6Brilliant Stone&r ist ein seltenes Erz in kleinen Nestern unter Tage, auch als Tiefenschiefer-Variante. Abgebaut gibt es &6Raw Brilliance&r, Glück wirkt.",
              "",
              "Damit baust du den &6Brilliant Obelisk&r: &e2 Runewood-Bretter&r auf den Altar, &e2 Raw Brilliance&r auf die Stands, dazu &e16 Aerial&r und &e8 Aqueous&r.",
              "",
              "Neben einem Zaubertisch zählt ein Brilliant Obelisk wie &dfünf Bücherregale&r. Zwei bis drei davon ersetzen eine ganze Bibliothek.",
          ],
          tasks=[task_item("malum:brilliant_obelisk", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(6)],
          deps=["obelisk"], icon="malum:brilliant_obelisk", optional=True),

    quest("esoteric_spoils", 7.5, 9.5, "&5Infundier den Ring of Esoteric Spoils",
          subtitle="Ein Arcana mehr pro Seele.",
          description=[
              "&6Ornate Ring&r: ein &6Seelenstahl&r oben links, &e4 Leder&r als Ring darum.",
              "Den Ring auf den Altar, &e8 Refined Soulstone&r auf die Stands, dazu je &e8 Wicked&r, &e8 Arcane&r und &e8 Eldritch&r.",
              "",
              "Getragen gibt jede zerbrochene Seele ein zusätzliches Arcana. Lohnt sich vor allem bei seltenen Sorten wie Eldritch.",
          ],
          tasks=[task_item("malum:ring_of_esoteric_spoils", 1)],
          rewards=[reward_item("malum:eldritch_spirit", 8), reward_xp(8)],
          deps=["soul_steel", "sp_eldritch"], icon="malum:ring_of_esoteric_spoils"),

    quest("prospector", 10, 10, "&6Infundier den Belt of the Prospector",
          subtitle="Explosionen mit Glück III.",
          description=[
              "&6Gilded Belt&r: &e3 Leder&r oben, darunter Hallowed Gold, Refined Soulstone, Hallowed Gold, unten ein Hallowed Gold.",
              "Den Gürtel auf den Altar, auf die Stands &6Cthonic Gold&r und je &e4&r Rohes Gold, Eisen und Kupfer. Dazu &e32 Earthen&r, &e32 Infernal&r und &e16 Arcane&r.",
              "",
              "Jede Explosion, die du auslöst, wirkt wie Glück III. Wertvolle Funde geben dir außerdem &eAvarice&r: Jede Stufe bringt &d10 Prozent&r Chance auf eine zusätzliche Glücksstufe beim Abbauen.",
          ],
          tasks=[task_item("malum:belt_of_the_prospector", 1)],
          rewards=[reward_item("minecraft:tnt", 8), reward_xp(8)],
          deps=["hallowed_gold", "nodes"], icon="malum:belt_of_the_prospector", optional=True),

    quest("repair_pylon", 7.5, 16, "&6Infundier einen Repair Pylon",
          subtitle="Reparieren mit Arcana statt Erfahrung.",
          description=[
              "Einen &6Tainted Rock Item Pedestal&r (Steinsäge) auf den Altar, auf die Stands je &e8 Tainted&r und &e8 Twisted Rock&r. Dazu je &e16 Sacred, Aerial, Aqueous&r und &e16 Infernal&r.",
              "",
              "Gib dem Pylon Arcana und das passende Reparaturmaterial. Er sucht beschädigte Items auf Ablagen, Stands und im Crucible in der Nähe und repariert sie ohne Erfahrung: normale Werkzeuge zur Hälfte, Malum-Ausrüstung zu drei Vierteln.",
              "",
              "So hält auch dein Impetus länger.",
          ],
          tasks=[task_item("malum:repair_pylon", 1)],
          rewards=[reward_item("malum:sacred_spirit", 16), reward_xp(8)],
          deps=["impetus"], icon="malum:repair_pylon"),

    quest("catalyzer", 10, 14, "&cInfundier einen Spirit Catalyzer",
          subtitle="Der Crucible wird schneller.",
          description=[
              "Zuerst &6Ether&r: &e4 Glowstonestaub&r auf den Altar, ein &6Blazing Quartz&r (Netherz) auf einen Stand, dazu &e2 Infernal&r und &e1 Arcane&r. Gibt zwei.",
              "Dann einen &6Twisted Rock Item Pedestal&r auf den Altar, &e4 Twisted&r, &e4 Tainted Rock&r und ein Ether auf die Stands, dazu &e8 Infernal&r und &e8 Aerial&r.",
              "",
              "Stell den Catalyzer neben den Crucible: Er heizt den Katalysator und beschleunigt das Bündeln. Dafür verschleißt der Impetus etwas schneller, also gleich mit Repair Pylon kombinieren.",
          ],
          tasks=[task_item("malum:spirit_catalyzer", 1)],
          rewards=[reward_item("malum:infernal_spirit", 16), reward_xp(8)],
          deps=["impetus"], icon="malum:spirit_catalyzer", optional=True),

    quest("rite_combat", 20, 4, "&2Zünde Kampfauren",
          subtitle="Rite of the Stone Ward und Burning Fervor.",
          description=[
              "Beide auf einer &6Runewood&r-Totembasis, drei Runen:",
              "&eStone Ward:&r ein &dArcane&r, zwei &6Earthen&r. Du nimmst &d20 Prozent&r weniger Schaden, ohne Rüstung doppelt so viel.",
              "&eBurning Fervor:&r ein &dArcane&r, zwei &cInfernal&r. Angriffs- und Abbautempo steigen um &d40 Prozent&r.",
              "",
              "Ein Fervor-Totem neben der Baustelle oder am Steinbruch spart viel Zeit.",
          ],
          tasks=[task_checkmark("Einen der beiden Riten gestartet")],
          rewards=[reward_item("malum:earthen_spirit", 16), reward_xp(6)],
          deps=["healing_rite"], icon="malum:earthen_spirit", optional=True),

    quest("rite_motion", 20, 6.2, "&2Zünde Bewegungsauren",
          subtitle="Rite of the Howling Gale und Flowing Grasp.",
          description=[
              "Beide auf einer &6Runewood&r-Totembasis, drei Runen:",
              "&eHowling Gale:&r ein &dArcane&r, zwei &fAerial&r. Lauf- und Angriffstempo &d+40 Prozent&r.",
              "&eFlowing Grasp:&r ein &dArcane&r, zwei &bAqueous&r. Reichweite und Aufsammelradius &d+40 Prozent&r.",
              "",
              "Flowing Grasp im Lager oder an der Baustelle: Du erreichst Truhen und Blöcke von weiter weg.",
          ],
          tasks=[task_checkmark("Einen der beiden Riten gestartet")],
          rewards=[reward_item("malum:aerial_spirit", 16), reward_xp(6)],
          deps=["healing_rite"], icon="malum:aerial_spirit", optional=True),

    quest("rite_nurturing", 22.5, 4, "&2Zünde den Rite of Nurturing",
          subtitle="Tiere wachsen schneller.",
          description=[
              "Ein großer Ritus mit vier Runen: &5Eldritch&r, &dArcane&r und zwei &eSacred&r, auf Runewood.",
              "",
              "Tiere in der Nähe altern bei jedem Puls um &d25 Sekunden&r. Jungtiere wachsen schneller, Hühner legen öfter Eier, Schafe fressen öfter Gras, Bienen bestäuben schneller.",
              "",
              "Ein Totem mitten in der Tierfarm lohnt sich.",
          ],
          tasks=[task_checkmark("Rite of Nurturing gestartet")],
          rewards=[reward_item("minecraft:wheat", 32), reward_xp(8)],
          deps=["healing_rite"], icon="malum:sacred_spirit", optional=True),

    quest("rite_soaking", 22.5, 6.2, "&2Zünde den Rite of Soaking",
          subtitle="Ein Funke, der Felder wachsen lässt.",
          description=[
              "Ein großer Ritus mit vier Runen: &5Eldritch&r, &dArcane&r und zwei &bAqueous&r, auf Runewood.",
              "",
              "Der Ritus webt einen &eRite Locus&r. Über Feldfrüchten lässt er die Zeit schneller laufen, andere Pflanzen wachsen wie mit Knochenmehl. Über Ackerland wirkt er auf die Pflanze darauf.",
          ],
          tasks=[task_checkmark("Rite of Soaking gestartet")],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(8)],
          deps=["healing_rite"], icon="malum:aqueous_spirit", optional=True),
]

images = [
    banner("malum/title", "Malum", 6, -5.2, height=1.8, kind="title", colour="magic"),
    banner("malum/ernten", "Seelen ernten", 4, -3.3, height=0.9, colour="magic"),
    banner("malum/arcana", "Die acht Arcana", 12.5, -4, height=0.9, colour="nature"),
    banner("malum/altar", "Der Geisteraltar", 5, 3, height=0.9, colour="magic"),
    banner("malum/totems", "Totems und Riten", 16.25, 2.3, height=0.9, colour="nature"),
    banner("malum/tiegel", "Tiegel und Fokus", 3.75, 11.3, height=0.9, colour="fire"),
]

chapter(C, "Malum", "malum:spirit_altar", "magic", quests, shape="circle", order=29, stage=3,
        subtitle=["Stufe 3. Seelen ernten, acht Arcana, Altar, Crucible und Totems."], images=images)
