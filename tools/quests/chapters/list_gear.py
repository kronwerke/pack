"""Checklist: tools, weapons, armour and mobility, one line per item, grouped by stage.
Stage 1 entries ask for the item, everything later is a checkmark that only names the item.
Numbers come from the mod jars and the server configs (Silent Gear material JSONs, Mekanism
tools-materials-startup.toml, JDT GooTier, MA ModItemTier, Botania tiers, backpack server config).
Every section points to the chapter that explains the mod."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner)

C = "list_gear"

# Column x positions for the eight entries of a row, and the row spacing.
COLS = [3.0, 5.5, 8.0, 10.5, 13.0, 15.5, 18.0, 20.5]
ROW = 2.0

def entry(name, col, row, y0, title, subtitle, lines, task, icon, deps, rewards=None):
    """One checklist line: title is the action, subtitle the result, lines the facts."""
    return quest(name, COLS[col], y0 + row * ROW, title,
                 subtitle=subtitle, description=list(lines), tasks=[task],
                 rewards=rewards or [reward_xp(2)], deps=deps, icon=icon)

S1, S2, S3, S4, S5 = 0.0, 8.0, 16.0, 24.0, 32.0

quests = [
    # ---- Stufe 1: Steinwerk ----------------------------------------------------------------------
    quest("s1", 0, S1 + 1, "&7&lRüste dich für Stufe 1",
          subtitle="Eisen, Diamant, Teile und ein Rucksack.",
          description=[
              "Diese Liste zeigt, welches Werkzeug, welche Waffe, welche Rüstung und welche Flughilfe sich in jeder Stufe lohnt: ein Haken pro Stück, dazu Zahlen und das Kapitel, in dem das Rezept steht.",
              "",
              "In Stufe 1 ist Diamant das Ziel, und Silent Gear macht aus wenig Eisen schon ein gutes Werkzeug. Alles in diesem Abschnitt ist eine echte Aufgabe, ab Stufe 2 sind es Haken.",
              "",
              "&eKronwerke:&r Gesperrte Ausrüstung kannst du tragen, aber nicht anlegen. Der Tooltip nennt die Stufe.",
          ],
          tasks=[task_item("minecraft:iron_pickaxe", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_table("s1_common")],
          icon="minecraft:iron_pickaxe", size=2.0, shape="hexagon"),

    entry("v_diamond", 0, 0, S1, "&bSteig auf Diamant um", "Die Spitzhacke, die alles abbaut.",
          ["Drei &6Diamanten&r über zwei Stöcken. Diamanterz liegt tief, am meisten um Y -58, und die Minendimension (Kapitel Erkundung) ist voll davon.",
           "",
           "1 561 Haltbarkeit statt 250, Tempo 8 statt 6, baut Obsidian ab. Die Diamantrüstung gibt 20 Punkte statt 15, dazu Zähigkeit 2 pro Teil."],
          task_item("minecraft:diamond_pickaxe", 1), "minecraft:diamond_pickaxe", ["s1"],
          [reward_item("minecraft:diamond", 1), reward_xp(3)]),

    entry("sg_pick", 1, 0, S1, "&7Bau eine Spitzhacke aus Teilen", "Silent Gear: Kopf, Stiel, Spitze.",
          ["Spitzhacke-Blaupause plus drei &6Eisenbarren&r ergibt den Kopf, dazu ein Stiel. Eine &6Diamantspitze&r (Spitze-Blaupause plus ein Diamant) gibt +256 Haltbarkeit und die Diamant-Abbaustufe.",
           "",
           "Eisenkopf: 250 Haltbarkeit, Tempo 6, Biegsam III. Kaputte Teile tauschst du einzeln, siehe Kapitel &6Silent Gear&r."],
          task_item("silentgear:pickaxe", 1), "silentgear:pickaxe", ["s1"]),

    entry("sg_hammer", 2, 0, S1, "&7Grab Tunnel mit dem Hammer", "Silent Gear: 3x3 schon in Stufe 1.",
          ["Hammer-Blaupause (6 Blaues Papier, 1 Stock) plus &6sechs Eisenbarren&r ergibt den Kopf. Sehnen-Verbindung und Ledergriff gleichen den Verschleiß aus.",
           "",
           "Baut 3x3 ab, nutzt sich pro Block ab. Für Adern nimm &6Ultimine&r, für Tunnel den Hammer."],
          task_item("silentgear:hammer", 1), "silentgear:hammer", ["s1"]),

    entry("ma_inferium", 3, 0, S1, "&aVeredle Diamant mit Inferium", "Mystical Agriculture: 2 000 Haltbarkeit.",
          ["&6Diamantwerkzeug&r in die Mitte, 2 Inferiumbarren links und rechts, 2 Inferium-Edelsteine oben und unten, an der Werkbank.",
           "",
           "2 000 Haltbarkeit, Tempo 9, +4 Schaden statt +3. Die Rüstung gibt 21 statt 20. Kapitel &aMystical Agriculture&r."],
          task_item("mysticalagriculture:inferium_pickaxe", 1), "mysticalagriculture:inferium_pickaxe", ["s1"]),

    entry("ars_sword", 4, 0, S1, "&dVerzaubere ein Schwert mit Quelle", "Ars Nouveau: ein Zauber auf jedem Treffer.",
          ["&6Diamantschwert&r in den Bezaubernden Apparat, auf die Podeste ein Diamant, 2 Goldblöcke und 2 Quelljuwelenblöcke. Für das &6Zauberschild&r: Schild, 2 Goldblöcke, 2 Quelljuwelenblöcke.",
           "",
           "Das Zauberschwert trägt einen Zauber, den du am Tisch des Schreibers einschreibst, und wirkt ihn bei jedem Treffer. Kapitel &dArs Nouveau&r."],
          task_item("ars_nouveau:enchanters_sword", 1), "ars_nouveau:enchanters_sword", ["s1"]),

    entry("irons_wizard", 5, 0, S1, "&5Zieh die Zaubererrobe an", "Iron's Spells: 125 Mana pro Teil.",
          ["&6Arcane Cloth&r aus Arcane Essence und Wolle, dann Hut, Robe, Hose und Schuhe im Lederrüstungsmuster. Kapitel &5Iron's Spells 'n Spellbooks&r.",
           "",
           "Jedes Teil +125 Mana und +5 Prozent Zauberkraft, Schutz wie Diamant (3, 8, 6, 3). Mit einer Rune wird daraus Schulrüstung mit +10 Prozent für ihre Schule."],
          task_item("irons_spellbooks:wizard_hat", 1), "irons_spellbooks:wizard_hat", ["s1"]),

    entry("apo_rare", 6, 0, S1, "&9Trag ein Rare-Item", "Apotheosis: Affixe auf Waffe und Rüstung.",
          ["Affix-Beute fällt von Monstern und liegt in Truhen. Trag vier Affix-Rüstungsteile und eine Affix-Waffe, dann öffnet die Weltstufe &6Frontier&r mit mehr Uncommon und Rare.",
           "",
           "Rare: zwei Attributboni, ein Effekt, bis zu zwei Sockel für Edelsteine, 10 bis 25 Prozent weniger Verschleiß. Kapitel &6Apotheosis&r."],
          task_checkmark("Ein Rare-Item getragen"), "apotheosis:gem", ["s1"]),

    entry("boss_overworld", 7, 0, S1, "&cHol dir eine Bosswaffe", "Cataclysm: Alter Speer, Soul Render, Gezeitenklauen.",
          ["&6Alter Speer&r: 4 Altmetallbarren vom Ancient Remnant, 9,5 Schaden, Linksklick schießt einen Sandsturm. &6Soul Render&r: 3 Cursium von Maledictus und 2 Schwarzstahl, 15 Schaden.",
           "",
           "&6Gezeitenklauen&r lässt der Leviathan fallen: Enterhaken und Tentakelschlag für 8. Wie die Kämpfe laufen, steht im Kapitel &cBosse der Oberwelt&r."],
          task_checkmark("Eine Bosswaffe in der Hand"), "cataclysm:ancient_spear", ["s1"]),

    entry("backpack", 0, 1, S1, "&6Näh einen Rucksack", "Sophisticated Backpacks: 27 Plätze auf dem Rücken.",
          ["Leder, Faden und eine Truhe an der Werkbank. Die &6Upgrade-Basis&r (Leder, Eisen, Faden) wird zu Pickup, Magnet und Werkzeugtausch. Kapitel &6Lager&r.",
           "",
           "Lederrucksack: 27 Plätze, 1 Upgrade. Kupfer (45) und Eisen (54, 2 Upgrades) kommen in Stufe 2, Gold und Diamant in Stufe 3, Netherit in Stufe 4."],
          task_item("sophisticatedbackpacks:backpack", 1), "sophisticatedbackpacks:backpack", ["s1"]),

    entry("ultimine", 1, 1, S1, "&6Räum eine Ader mit Ultimine", "FTB Ultimine: bis zu 64 Blöcke pro Schlag.",
          ["Halt &e`&r gedrückt (links neben der 1), schau auf einen Block, bau ab. Mit Shift und Mausrad wechselst du die Form: Ader, Tunnel 3x3, Stollen.",
           "",
           "Kostet 20-mal so viel Hunger wie ein Block, also iss vorher. Jede Herkunft darf das. Kapitel &6Komfort&r."],
          task_checkmark("Eine Ader auf einmal abgebaut"), "minecraft:iron_pickaxe", ["s1"]),

    entry("mining_dim", 2, 1, S1, "&6Bau die Verzauberte Spitzhacke", "Der Schlüssel zur Minendimension.",
          ["&eRezept auf Kronwerke:&r 2 Diamanten und ein Goldblock oben, 2 Stöcke darunter. Damit zündest du einen Rahmen aus Eisenblöcken.",
           "",
           "Dahinter liegt eine zweite Welt nur zum Graben, voller Erz und Höhlen. Kapitel &6Erkundung&r."],
          task_item("ultimate_mining_dimension:ultimate_mining_dimension", 1), "ultimate_mining_dimension:ultimate_mining_dimension", ["s1"]),

    # ---- Stufe 2: Messingwerk --------------------------------------------------------------------
    quest("s2", 0, S2 + 1, "&6&lRüste dich für Stufe 2",
          subtitle="Netherit, Nether-Metalle, der erste Jetpack.",
          description=[
              "Mit dem Nether kommen Netherit, die Nether-Metalle von Silent Gear und Just Dire Things, Stahl von Mekanism und Terrastahl. Und der erste Flug: der Jetpack von Mekanism.",
              "",
              "Ab hier sind die Einträge Haken. Hak ab, was du hast, die Belohnung ist klein, die Übersicht das Ziel.",
          ],
          tasks=[task_checkmark("Stufe 2 ist offen")],
          rewards=[reward_table("s1_common")],
          deps=["s1"], icon="minecraft:gold_ingot", size=1.75, shape="hexagon"),

    entry("v_netherite", 0, 0, S2, "&8Schmiede Netherit", "Vier Platten, vier Gold, ein Barren.",
          ["Antiker Schrott aus dem Nether um Y 15, im Ofen zu Netheritplatten, vier davon plus vier Gold. Am Schmiedetisch mit der Vorlage aus Bastionen auf Diamantausrüstung. Kapitel &cDer Nether&r.",
           "",
           "2 031 Haltbarkeit, Tempo 9, +1 Schaden, verbrennt nicht in Lava. Rüstung: Zähigkeit 3 und Rückstoßwiderstand pro Teil. Silent Gear nimmt Netherit als &6Beschichtung&r am Schmiedetisch."],
          task_checkmark("Netheritwerkzeug in der Hand"), "minecraft:diamond_sword", ["s2"]),

    entry("sg_crimson", 1, 0, S2, "&cSchmiede Purpur-Eisen", "Silent Gear: Tempo 10 aus dem Nether.",
          ["&6Purpur-Eisenerz&r im Netherrack und Schwarzstein, Rohes Purpur-Eisen im Ofen schmelzen. Kopf aus drei Barren wie bei Eisen.",
           "",
           "420 Haltbarkeit, Tempo 10, +3 Schaden, Biegsam III, Hart II, Hitzebeständig IV. Als Spitze +224 Haltbarkeit und Feurig. Kapitel &6Silent Gear&r."],
          task_checkmark("Purpur-Eisen-Werkzeug gebaut"), "silentgear:pickaxe_head", ["s2"]),

    entry("sg_crimson_steel", 2, 0, S2, "&cLegiere Purpur-Stahl", "Silent Gear: das Endgame-Metall des Nethers.",
          ["An der Werkbank: 4 &6Purpur-Eisen&r, 2 Lohenruten, 1 Magmacreme ergeben 1 Barren. In der &6Alloy Forge&r (Purpur-Stahl, Schwarzstein, Eisenblock): ein Block Purpur-Eisen, 2 Lohenruten, Magmacreme ergeben 3.",
           "",
           "2 400 Haltbarkeit, Tempo 15, +6 Schaden, Rüstung 22 mit Zähigkeit 10, Flammenwächter (Feuerschutz im ganzen Satz). &6Lohengold&r (Gold und 4 Lohenstaub) hält nur 69, gräbt aber mit Tempo 15 und taugt als Spitze."],
          task_checkmark("Purpur-Stahl-Werkzeug gebaut"), "silentgear:hammer_head", ["s2"]),

    entry("mek_paxel", 3, 0, S2, "&7Bau die Stahlpaxel", "Mekanism Tools: drei Werkzeuge, 1 000 Haltbarkeit.",
          ["Stahlspitzhacke, Stahlaxt und Stahlschaufel mit zwei Stöcken ergeben die &6Stahlpaxel&r. Stahl kommt aus der Infusionsanlage, Kapitel &5Mekanism&r.",
           "",
           "1 000 Haltbarkeit, Tempo 8, 8 Schaden. &6Raffiniertes Glowstone&r gräbt mit Tempo 15, hält aber nur 768. Stahlrüstung: 20 Punkte, Zähigkeit 2."],
          task_checkmark("Stahlpaxel gebaut"), "minecraft:iron_axe", ["s2"]),

    entry("mek_jetpack", 4, 0, S2, "&bFlieg mit dem Jetpack", "Mekanism: der erste Flug des Packs.",
          ["Oben Stahl, Einfacher Schaltkreis, Stahl, in der Mitte Zinn, &6Einfacher Chemietank&r, Zinn, unten Zinn. Füllen mit &bWasserstoff&r aus dem Elektrolyseur (Wasser und Strom).",
           "",
           "Fasst 24 000 mB. Taste für den Modus: Normal, Schweben, Aus. Die &6Free Runners&r (2 Schaltkreise, 2 Infundierte Legierungen, 2 Energietabletts) fangen Fallschaden ab und steigen Blöcke hoch."],
          task_checkmark("Mit dem Jetpack geflogen"), "minecraft:feather", ["s2"]),

    entry("jdt_ferricore", 5, 0, S2, "&7Schmiede Ferricore", "Just Dire Things: Werkzeug mit Upgrades.",
          ["Eisen im Goo-Block zu Ferricore, drei Barren über zwei Stöcken. Upgrades am Schmiedetisch: Erzadern, Erzsuche, Baumfällen, Mob Scanner. Kapitel &aJust Dire Things&r.",
           "",
           "500 Haltbarkeit, Tempo 7, +2,5 Schaden, Eisen-Abbaustufe. Die Rüstung nimmt Step Assist, Sprung und Laufgeschwindigkeit."],
          task_checkmark("Ferricore-Werkzeug mit Upgrade"), "minecraft:iron_ingot", ["s2"]),

    entry("jdt_blazegold", 6, 0, S2, "&6Steig auf Blazegold um", "Just Dire Things: 3x3 und Auto-Schmelzen.",
          ["Blazegold Upgrade Template (5 Blazegold um ein Blank Upgrade) am Schmiedetisch auf das Ferricore-Stück, die Upgrades bleiben drin.",
           "",
           "1 440 Haltbarkeit, Tempo 12, +3 Schaden, Diamant-Abbaustufe. Neu: Hammer 3x3, Auto Smelter, Cauterize Wounds für die Rüstung. Dazu die &6Portal Gun&r (5 Blazegold, Enderauge)."],
          task_checkmark("Blazegold-Werkzeug gebaut"), "minecraft:gold_nugget", ["s2"]),

    entry("bot_manasteel", 7, 0, S2, "&bBau Manastahl-Ausrüstung", "Botania: repariert sich mit Mana.",
          ["Manastahl und Lebeholzzweige in den Eisenmustern. Manastahl kommt aus dem Ritual des Waldes oder dem Becken, Kapitel &aBotania: Runen&r.",
           "",
           "300 Haltbarkeit, Tempo 6,2, Diamant-Abbaustufe. Rüstung 15 wie Eisen, Verzauberbarkeit 18. Alles heilt sich aus einer Manatafel im Inventar."],
          task_checkmark("Manastahl-Werkzeug gebaut"), "botania:mana_diamond", ["s2"]),

    entry("bot_terra", 0, 1, S2, "&aSchmiede Terrastahl", "Botania: Terraklinge und Terra-Zerschmetterer.",
          ["Terrastahl von der Agglomerationsplatte. &6Terraklinge&r: 2 Barren, ein Lebeholzzweig. &6Terra-Zerschmetterer&r: Spitzhacke aus Terrastahl, die im Becken Mana schluckt.",
           "",
           "2 300 Haltbarkeit, Tempo 9, +4 Schaden, Netherit-Stufe. Rüstung 20 mit Zähigkeit 3. Die Klinge schießt Strahlen, der Zerschmetterer gräbt ab Rang B Flächen, der &6Terra-Fäller&r ganze Bäume."],
          task_checkmark("Terrastahl-Ausrüstung getragen"), "botania:livingwood_bow", ["s2"]),

    entry("ma_prudentium", 1, 1, S2, "&aVeredle auf Prudentium", "Mystical Agriculture: 2 800 Haltbarkeit.",
          ["Inferium-Werkzeug in die Mitte, 2 Prudentiumbarren und 2 Prudentium-Edelsteine drumherum. Verzauberungen bleiben.",
           "",
           "2 800 Haltbarkeit, Tempo 11, +6 Schaden. Mit dem &6Basteltisch&r (Soulium) setzt du jetzt Augmente ein. Dasselbe Muster noch zweimal: Tertium in Stufe 3 (4 000, Tempo 14, +9), Imperium in Stufe 4 (6 000, Tempo 19, +13)."],
          task_checkmark("Prudentium-Werkzeug gebaut"), "mysticalagriculture:inferium_essence", ["s2"]),

    entry("aether_gloves", 2, 1, S2, "&fZieh Handschuhe an", "Aether: ein fünfter Rüstungsslot.",
          ["Der Aether öffnet mit dem Nether. &6Handschuhe&r aus Leder, Eisen, Gold, Diamant oder Zanit im Schmuckslot geben Rüstungspunkte dazu.",
           "",
           "&6Zanit-Werkzeug&r wird schneller, je mehr es abgenutzt ist. &6Heiligstein&r wirft beim Graben Ambrosiumsplitter ab. Gravitit kommt in Stufe 3."],
          task_checkmark("Handschuhe getragen"), "minecraft:leather", ["s2"]),

    entry("irons_anvil", 3, 1, S2, "&5Setz eine Upgrade-Kugel ein", "Iron's Spells: Arcane Anvil und Pyromancer.",
          ["Der &6Arcane Anvil&r (Amethystblöcke, Diamant, Amboss) nimmt Rüstung plus &6Upgrade Orb&r: bis zu 3 Upgrades für Mana, Abklingzeit, Schutz oder eine Schule. Kugeln brauchen Mithril und Cinder Essence aus dem Nether.",
           "",
           "Die &cPyromancer&r-Rüstung braucht die Fire Rune aus Lohenruten. Epic Ink mit Diamant- und Netheritbuch kommt in Stufe 3, Legendary und Drachenhaut in Stufe 4. Kapitel &5Iron's Spells 'n Spellbooks&r."],
          task_checkmark("Rüstung aufgewertet"), "minecraft:amethyst_shard", ["s2"]),

    entry("boss_nether", 4, 1, S2, "&cTrag Ignitium", "Cataclysm im Nether: Ignis und die Monstrosität.",
          ["&cIgnis&r lässt &6Ignitium&r fallen. Vorlage: Netherit-Schmiedevorlage, 4 Lohenstaub, 4 Netherziegel. Damit wird Netheritrüstung am Schmiedetisch zu Ignitiumrüstung.",
           "",
           "&6The Incinerator&r: Netheritschwert, 2 Ignitium, 4 Lohenruten. &6Bulwark of the Flame&r: Schild, 2 Ignitium, 2 Lohenruten, 4 Netherziegel. Die &cNetherit-Monstrosität&r lässt die &6Infernal Forge&r fallen."],
          task_checkmark("Ignitium-Stück getragen"), "minecraft:shield", ["s2"]),

    entry("backpack_iron", 5, 1, S2, "&6Rüste den Rucksack auf", "Kupfer und Eisen: 45 und 54 Plätze.",
          ["Rucksack in die Mitte, Kupferbarren oder Eisenbarren drumherum, an der Werkbank. Der Inhalt bleibt drin.",
           "",
           "Kupfer: 45 Plätze, 1 Upgrade. Eisen: 54 Plätze, 2 Upgrades. Stufe 3 bringt Gold (81, 3) und Diamant (108, 5) mit Inception und Everlasting Upgrade, Stufe 4 Netherit (120, 7). Kapitel &6Lager&r."],
          task_checkmark("Eisenrucksack getragen"), "sophisticatedbackpacks:backpack", ["s2"]),

    # ---- Stufe 3: Stahlwerk ----------------------------------------------------------------------
    quest("s3", 0, S3 + 1, "&f&lRüste dich für Stufe 3",
          subtitle="Raffiniertes Obsidian, Elementium, Flugrituale.",
          description=[
              "Stufe 3 bringt die Mitte der Leiter: Raffiniertes Obsidian von Mekanism, Celestigem, Elementium, Seelenstahl, Gravitit aus den Aether-Dungeons und drei neue Wege zu fliegen.",
              "",
              "Dazu die Abbaumaschinen: Mining Gadget, Bohrmaschine, Digitaler Miner.",
          ],
          tasks=[task_checkmark("Stufe 3 ist offen")],
          rewards=[reward_table("s1_common")],
          deps=["s2"], icon="minecraft:iron_block", size=1.75, shape="hexagon"),

    entry("mek_obsidian", 0, 0, S3, "&5Bau Raffiniertes Obsidian", "Mekanism Tools: 8 192 Haltbarkeit.",
          ["Obsidianstaub aus dem Zerkleinerer, mit Diamant infundiert, geschmolzen. Werkzeug und Rüstung wie Eisen. Kapitel &5Mekanism: Fortgeschritten&r.",
           "",
           "Werkzeug 4 096, Paxel 8 192 Haltbarkeit, Tempo 12, 8 Schaden. Rüstung 31 Punkte (6, 12, 8, 5), Zähigkeit 5. Das stärkste Rüstungsmetall vor der MekaSuit."],
          task_checkmark("Raffiniertes Obsidian getragen"), "minecraft:obsidian", ["s3"]),

    entry("mek_disassembler", 1, 0, S3, "&bBau den Atomic Disassembler", "Mekanism: ein Werkzeug mit Strom.",
          ["Infundierte Legierung, Energietablett, Infundierte Legierung oben, Legierung, &6Atomlegierung&r, Legierung in der Mitte, Raffiniertes Obsidian unten.",
           "",
           "Spitzhacke, Schaufel, Axt und Schwert in einem, läuft mit Strom statt Haltbarkeit. Modus-Taste: Normal, Langsam, Schnell, Aderabbau. In Stufe 4 wird daraus das Meka-Werkzeug."],
          task_checkmark("Disassembler gebaut"), "minecraft:redstone", ["s3"]),

    entry("mek_teleporter", 2, 0, S3, "&dTrag einen Teleporter in der Tasche", "Mekanism: Portable Teleporter.",
          ["Energietablett oben und unten, Schaltkreis, &6Teleportationskern&r, Schaltkreis in der Mitte. Der Kern braucht Atomlegierung.",
           "",
           "Teleportiert dich zu jedem Teleporter deiner Frequenz, überall auf dem Server. Kapitel &5Mekanism: Fortgeschritten&r. Ohne Strom geht das &6Tempad&r (Stufe 3): Orte speichern, Rechtsklick öffnet ein Portal dorthin."],
          task_checkmark("Teleportiert"), "minecraft:ender_pearl", ["s3"]),

    entry("jdt_celestigem", 3, 0, S3, "&bSchleif Celestigem", "Just Dire Things: 5x5 und Voidshift.",
          ["VoidShimmer Goo (mit Chorusfrucht oder Enderperlen geweckt) macht aus Diamantblöcken &6Celestigem&r. Template am Schmiedetisch wie bei Blazegold.",
           "",
           "1 561 Haltbarkeit, Tempo 10, +4 Schaden. Hammer 5x5, Drops-Teleporter, der &6Celestigem-Paxel&r und der &6Voidshift Wand&r, der dich dorthin bringt, wohin du schaust."],
          task_checkmark("Celestigem-Werkzeug gebaut"), "minecraft:diamond", ["s3"]),

    entry("bot_elementium", 4, 0, S3, "&dBau Elementium-Werkzeug", "Botania: Werkzeuge mit Eigenheiten.",
          ["2 Manastahl im Elfenportal ergeben 1 &6Elementium&r, Werkzeuge mit Traumholzzweigen. Kapitel &aBotania: Alfheim&r.",
           "",
           "720 Haltbarkeit, Diamant-Abbaustufe. Spitzhacke vernichtet Bruchstein und Schutt, Schaufel nimmt ganze Kiessäulen, Axt köpft. Rüstung 15 wie Manastahl, ruft Feen gegen Angreifer."],
          task_checkmark("Elementium-Werkzeug gebaut"), "botania:mana_diamond", ["s3"]),

    entry("malum", 5, 0, S3, "&5Schmiede Seelenstahl", "Malum: Waffen, die die Seele treffen.",
          ["Eisenbarren auf dem Geisteraltar mit 4 Refined Soulstone, 3 Wicked, 1 Earthen, 1 Arcane ergibt &6Soul Stained Steel&r. Kapitel &5Malum&r.",
           "",
           "Werkzeug und die &6Seelenstahl-Sense&r treffen Körper und Seele zugleich und ernten Spirit Arcana. Die Rüstung hat eigene Rezepte, weil reiner Seelenstahl auch deine Seele berührt."],
          task_checkmark("Seelenstahl-Waffe gebaut"), "minecraft:bone", ["s3"]),

    entry("aether_gravitite", 6, 0, S3, "&dSchmiede Gravitit", "Aether: Dungeon-Beute und schwebende Blöcke.",
          ["&6Gravitit&r aus dem Aether am Altar verzaubern, dann Werkzeug und Rüstung. Rüstung: höher springen, kein Fallschaden. Werkzeug: Rechtsklick lässt Blöcke schweben.",
           "",
           "&6Valkyrienlanze&r aus dem Silberdungeon, &6Phönixrüstung&r aus dem Golddungeon (geh damit ins Wasser) und &6Neptunrüstung&r sind Beute, keine Rezepte."],
          task_checkmark("Gravitit getragen"), "minecraft:feather", ["s3"]),

    entry("undergarden", 7, 0, S3, "&2Hol die Vergessene Spitzhacke", "Undergarden: Cloggrum, Froststahl, Vergessen.",
          ["&6Cloggrum&r reicht für alle Erze, &6Froststahl&r-Waffen verlangsamen. Am Schmiedetisch: Vorlage, Cloggrumwerkzeug, Vergessener Barren vom Vergessenen Wächter.",
           "",
           "Vergessenes Werkzeug baut alle Undergarden-Blöcke anderthalbmal so schnell ab und ist der einzige Schlüssel zum Furchtfels über den Tiefen. Kapitel &2Der Undergarden&r."],
          task_checkmark("Vergessene Spitzhacke in der Hand"), "minecraft:deepslate", ["s3"]),

    entry("ars_robes", 0, 1, S3, "&dNäh Magierroben", "Ars Nouveau: Arkanist und Kampfmagier.",
          ["Eisenrüstung oder Diamantrüstung mit 4 Magieblütenfasern im Bezaubernden Apparat. Eisen wird Arkanist, Diamant Kampfmagier. Kapitel &dArs Nouveau: Meister&r.",
           "",
           "Alle Roben erhöhen die Manaregeneration und nehmen Fäden am Änderungstisch. Erste Aufwertung: 2 Lohenruten und 2 500 Quelle pro Teil."],
          task_checkmark("Robe getragen"), "ars_nouveau:novice_spell_book", ["s3"]),

    entry("ars_flight", 1, 1, S3, "&dFlieg mit dem Ritual", "Ars Nouveau: Flug wie im Kreativmodus.",
          ["Ritual-Kohlenbecken mit der Tafel &6Ritual: Flug&r (Ärgerlicher Archwood-Stamm, 3 Wilden-Flügel, 2 Diamanten, Enderperle). Quellgläser daneben.",
           "",
           "Wer in der Nähe springt, bekommt den Effekt Flug und fliegt frei, solange das Ritual Quelle hat. Die beste Baustellen-Flughilfe des Packs."],
          task_checkmark("Mit dem Ritual geflogen"), "ars_nouveau:source_gem", ["s3"]),

    entry("rending_gale", 2, 1, S3, "&bFlieg mit der Rending Gale", "Reliquary: Fliegen in Blickrichtung.",
          ["Die &6Rending Gale&r (Reliquary, Stufe 3) hält dich in der Luft, solange du Rechtsklick hältst, und fliegt dorthin, wo du hinschaust. Shift und Mausrad wechseln den Modus.",
           "",
           "Kein sanfter Fall: Richtung Boden gedrückt halten, sonst tut die Landung weh. Sie stößt und zieht auch Mobs und ruft bei Gewitter Blitze. Kapitel &5Reliquary&r."],
          task_checkmark("Mit der Rending Gale geflogen"), "minecraft:phantom_membrane", ["s3"]),

    entry("oritech", 3, 1, S3, "&eZieh die Exo-Rüstung an", "Oritech: Jetpack mit Strom oder Turbofuel.",
          ["Oritech öffnet in Stufe 3. Der &6Jetpack&r fliegt mit Strom oder Turbofuel, mit Turbofuel schneller. Die &6Exo-Rüstung&r: Stiefel ohne Fallschaden, Hose mit mehr Tempo, Brust lädt deine Stromgeräte.",
           "",
           "&6Exo-Jetpack&r und &6Jetpack-Elytra&r kombinieren beides. Kapitel &eOritech&r."],
          task_checkmark("Exo-Teil getragen"), "minecraft:copper_ingot", ["s3"]),

    entry("mining_gadget", 4, 1, S3, "&bBau das Mining Gadget", "Mining Gadgets: ein Laser statt einer Spitzhacke.",
          ["Das &6Mining Gadget&r speichert 1 000 000 FE und braucht 200 FE pro Block. Am &6Modification Table&r steckst du Upgrades hinein.",
           "",
           "Reichweite, Größe 3x3, Glück oder Behutsamkeit, Magnet, Müll-Löschen, Licht setzen, Lava einfrieren. Batterie 1 bis 3 bringen 2, 5 und 10 Millionen FE, Stufe 3 der Upgrades kommt in Stufe 4."],
          task_checkmark("Mining Gadget gebaut"), "minecraft:redstone_torch", ["s3"]),

    entry("drilling", 5, 1, S3, "&7Stell eine Bohrmaschine auf", "Create Ore Excavation: Erz ohne Ende.",
          ["&6Erzadern-Finder&r zeigt die Ader unter dem Chunk, die &6Bohrmaschine&r (Messing, Robuste Bleche, Präzisionsgetriebe, Mechanischer Bohrer) mit &6Eisenbohrer&r fördert Roherz, solange sie dreht.",
           "",
           "Adern sind auf Kronwerke unerschöpflich. Diamant- und Netheritbohrer kommen in Stufe 4. Kapitel &6Create: Erweiterungen&r. Der &6Digitale Miner&r von Mekanism gräbt daneben ganze Gebiete leer."],
          task_checkmark("Bohrmaschine läuft"), "create:andesite_alloy", ["s3"]),

    # ---- Stufe 4: Sternwerk ----------------------------------------------------------------------
    quest("s4", 0, S4 + 1, "&d&lRüste dich für Stufe 4",
          subtitle="Elytren, MekaSuit, Wyvern und Eclipse.",
          description=[
              "Mit dem End kommen die Elytren und damit das Create-Jetpack, die Seelenelytra und das Wyvern-Flugmodul. Mekanism baut die MekaSuit, Just Dire Things die Eclipse-Rüstung, die fliegt.",
              "",
              "Auch die End-Metalle von Silent Gear liegen erst jetzt im Boden.",
          ],
          tasks=[task_checkmark("Stufe 4 ist offen")],
          rewards=[reward_table("s1_uncommon")],
          deps=["s3"], icon="minecraft:ender_pearl", size=1.75, shape="hexagon"),

    entry("v_elytra", 0, 0, S4, "&5Hol dir Elytren", "Vanilla: an der Wand eines Endschiffs.",
          ["Ein Paar pro Endschiff, bewacht von Shulkern. Brustplatz, springen, im Fall noch einmal springen, Feuerwerksraketen geben Schub. Kapitel &5Das End&r.",
           "",
           "432 Haltbarkeit, Reparatur mit Phantomhaut. Jede Elytra ist eine Zutat: Create-Jetpack, HDPE-Elytra, Seelenelytra, Wyvern-Flugmodul, Gleiten-Glyphe. Hol lieber mehrere."],
          task_checkmark("Elytren getragen"), "minecraft:phantom_membrane", ["s4"]),

    entry("create_jetpack", 1, 0, S4, "&6Bau das Create-Jetpack", "Create Jetpack: 450 Sekunden Druckluft.",
          ["In den Handwerkseinheiten: &6Kupfer-Rückentank&r in der Mitte, &5Elytra&r darunter, 2 Präzisionsgetriebe, Welle, 4 Schächte, 6 Messingbleche. Kapitel &6Create: Erweiterungen&r.",
           "",
           "Eine Füllung: 450 Sekunden Flug oder 900 Sekunden Schweben, Laden an jeder Welle. Sprung steigt, Schleichen sinkt, G schaltet, H schwebt. Mit Netherit-Tank wird es das Netherit-Jetpack."],
          task_checkmark("Mit dem Create-Jetpack geflogen"), "create:copper_backtank", ["s4"]),

    entry("mekasuit", 2, 0, S4, "&bZieh die MekaSuit an", "Mekanism: Netherit mit Strom und Modulen.",
          ["Pro Teil: Netheritteil in der Mitte, HDPE-Platten, ein Ultimativer Schaltkreis, 2 Polonium Pellets und eine Induktionszelle. Module in der &6Modifikationsstation&r. Kapitel &5Mekanism: Elite&r.",
           "",
           "Module: Jetpack, Nachtsicht, Servomotor, Magnet, Strahlenschutz, Energie. Die starken brauchen Polonium. Die Rüstung läuft mit Strom und schützt, solange sie geladen ist."],
          task_checkmark("MekaSuit getragen"), "minecraft:diamond_chestplate", ["s4"]),

    entry("meka_tool", 3, 0, S4, "&bBau das Meka-Werkzeug", "Mekanism: ein Werkzeug für alles, mit Modulen.",
          ["Ultimative Schaltkreise, Konfigurator, HDPE-Platten, der &6Atomic Disassembler&r in der Mitte, unten 2 Polonium Pellets und eine Induktionszelle.",
           "",
           "Spitzhacke, Axt, Schaufel, Hacke, Schwert. Module: Abbaubeschleunigung, Behutsamkeit oder Glück, Aderabbau, in Stufe 5 Teleportation mit Antimaterie."],
          task_checkmark("Meka-Werkzeug gebaut"), "minecraft:diamond_axe", ["s4"]),

    entry("jdt_eclipse", 4, 0, S4, "&8Schmiede Eclipse Alloy", "Just Dire Things: 7x7 und Flug.",
          ["Shadowpulse Goo (Sculk) macht aus Netheritblöcken &6Eclipse Alloy&r. Template am Schmiedetisch wie immer.",
           "",
           "2 561 Haltbarkeit, Tempo 16, +5 Schaden, Netherit-Stufe. Hammer 7x7, die Rüstung fliegt und schützt vor Lava. Dazu Zeitkristalle, Time Wand und die &6Portal Gun V2&r."],
          task_checkmark("Eclipse-Werkzeug gebaut"), "minecraft:sculk", ["s4"]),

    entry("wyvern", 5, 0, S4, "&dFusioniere Wyvern-Ausrüstung", "Draconic Evolution: Strom statt Haltbarkeit.",
          ["Fusion mit 6 Wyvern-Injektoren: Diamantwerkzeug als Katalysator, dazu Draconiumkern, 2 Draconiumbarren, 2 Relaiskristalle, Wyvern-Energiekontroller, 8 Millionen Energie. Kapitel &5Draconic Evolution&r.",
           "",
           "Geht nicht kaputt, lädt mit Strom. Module: AOE, Speed, Damage, Auto Feed, Undying. Die &6Wyvern-Brustplatte&r trägt einen Energieschild und mit Elytra und Rakete das &6Flugmodul&r."],
          task_checkmark("Wyvern-Stück gebaut"), "minecraft:diamond_sword", ["s4"]),

    entry("tiara", 6, 0, S4, "&bSetz die Flügel-Tiara auf", "Botania: 30 Sekunden Flug mit Mana.",
          ["3 &dGaia-Seelen&r oben, Elementium, Gaia-Seele, Elementium in der Mitte, Feder, Reine Ender-Essenz, Feder unten. Kapitel &aBotania: Gaia&r.",
           "",
           "Fliegt mit Mana aus dem Inventar, nach etwa 30 Sekunden am Stück ist die Leiste leer. Sprint-Stoß alle 2 Sekunden, Gleiten beim Schleichen ohne Fallschaden. Quarz tauscht die Flügel."],
          task_checkmark("Mit der Tiara geflogen"), "botania:mana_diamond", ["s4"]),

    entry("sg_end", 7, 0, S4, "&bSchmiede Azur-Elektrum und Tyrann-Stahl", "Silent Gear: die Metalle aus dem End.",
          ["&6Azur-Silbererz&r liegt im Endstein, 8 Adern pro Chunk zwischen Y 16 und 92. Block Azur-Silber, 2 Gold, Enderperle in der Alloy Forge ergibt 3 &6Azur-Elektrum&r.",
           "",
           "Azur-Elektrum: 1 259 Haltbarkeit, Tempo 29, +7, Leicht IV, Beschleunigung. &6Tyrann-Stahl&r (Purpur-Stahl, Azur-Elektrum, zerstoßene Shulkerschale, Netheritschrott ergeben 4): 3 652 Haltbarkeit, Tempo 18, +8, Rüstung 25 mit Zähigkeit 12, Leerenwächter."],
          task_checkmark("End-Metall verbaut"), "silentgear:paxel_head", ["s4"]),

    entry("pnc_armor", 0, 1, S4, "&7Trag die Pneumatikrüstung", "PneumaticCraft: Upgrades in jedem Teil.",
          ["Helm, Brust, Hose und Stiefel aus Komprimiertem Eisen und Druckluftteilen, geladen mit Luft. Jedes Teil nimmt Upgrade-Karten. Die einfache Rüstung aus Komprimiertem Eisen und der Presslufthammer gehen schon ab Stufe 2.",
           "",
           "Jet-Boots-Upgrade in den Stiefeln zum Fliegen, Nachtsicht und Mob-Tracker im Helm, Magnet und Ladegerät in der Brust. Die &6Minigun&r öffnet ebenfalls in Stufe 4."],
          task_checkmark("Pneumatikrüstung getragen"), "minecraft:iron_chestplate", ["s4"]),

    entry("warden", 1, 1, S4, "&3Schmiede Wardenrüstung", "Deeper and Darker: Netherit und Echo.",
          ["&6Verstärkte Echoscherbe&r: 4 Warden-Panzer, 4 Phantomhaut, eine Echoscherbe. Mit der Warden-Vorlage (Kopie: 7 Diamanten, Sculk) am Schmiedetisch auf Netheritausrüstung.",
           "",
           "&6Seelenelytra&r: Elytra, Seelenkristall, Sculk-Knochen, Seelenstaub. &6Sonorous Staff&r aus dem Herz der Tiefe vom Warden. Eine Stufe früher gibt es &6Resonarium&r aus der Otherside als Platte auf Diamantausrüstung."],
          task_checkmark("Warden-Stück getragen"), "minecraft:echo_shard", ["s4"]),

    entry("ars_sorcerer", 2, 1, S4, "&6Näh die Zaubererrobe", "Ars Nouveau: Goldrüstung, die besten Fäden.",
          ["Goldrüstung mit 4 Magieblütenfasern im Apparat ergibt die &6Zaubererrobe&r. Zweite Aufwertung: 2 Enderperlen, Chorusfrucht, 5 000 Quelle pro Teil. Kapitel &dArs Nouveau: Episch&r.",
           "",
           "Der &6Faden des Gleitens&r (leerer Faden, 2 Luftessenzen, Elytra) braucht einen Platz der Größe 3 und gleitet wie Elytren, der Brustplatz bleibt frei."],
          task_checkmark("Zaubererrobe getragen"), "ars_nouveau:novice_spell_book", ["s4"]),

    entry("apo_mythic", 3, 1, S4, "&6Trag Mythic", "Apotheosis: vier Attribute, zwei Effekte.",
          ["Der große &6Reforging Table&r (Netheritbarren, 2 Arcane Sands, 3 Netherziegel, Stufe 3) schmiedet Epic für 30 Level und Mythic für 50 Level, 3 Godforged Pearls und 5 Siegel. Der &6Augmenting Table&r (Netherstern, 2 Godforged Pearls) verbessert einen Affix um 25 Prozent.",
           "",
           "Mythic: vier Attribute, zwei Effekte, eine Fähigkeit, selten Unzerstörbarkeit. Kapitel &6Apotheosis&r."],
          task_checkmark("Mythic-Item getragen"), "apotheosis:gem", ["s4"]),

    entry("boss_end", 4, 1, S4, "&5Erbeute den Panzerhandschuh", "Cataclysm im End: Wächter und Golem.",
          ["Der &cEnder-Wächter&r lässt den &6Gauntlet of Guard&r fallen, der &cEnder-Golem&r einen &6Void Core&r für die &6Void Forge&r.",
           "",
           "Im Nether vorher: der &cHarbinger&r braucht einen Netherstern und gibt Witherit für den &6Mechanischen Fusionsamboss&r, der Bosswaffen verschmilzt. Kapitel &cBosse der Oberwelt&r."],
          task_checkmark("End-Bosswaffe in der Hand"), "minecraft:ender_pearl", ["s4"]),

    entry("starlight", 5, 1, S4, "&bBau eine Sternensense", "Eternal Starlight: Sense und Hammer.",
          ["Eternal Starlight öffnet mit dem End. &6Sensen&r aus Glacite oder Thermal Springstone sind eine eigene Waffenart, &6Hämmer&r lösen bei vollen kritischen Treffern einen Spezialangriff aus.",
           "",
           "Zubehör legst du wie in ein Bündel in die Waffe. Kapitel &bEternal Starlight&r. Der &6Netheritrucksack&r (120 Plätze, 7 Upgrades) kommt ebenfalls in Stufe 4."],
          task_checkmark("Sternensense gebaut"), "minecraft:amethyst_shard", ["s4"]),

    # ---- Stufe 5: Chaoswerk ----------------------------------------------------------------------
    quest("s5", 0, S5 + 1, "&c&lRüste dich für Stufe 5",
          subtitle="Drakonisch, Chaotisch, Supremium.",
          description=[
              "Das Ende der Leiter. Draconic Evolution macht aus Wyvern Drakonisch und Chaotisch, Mystical Agriculture wird unzerstörbar.",
              "",
              "Alles hier ist für den Chaoswächter gedacht. Wer Erwachte Blöcke für den Obelisken spart, lässt den Stab weg.",
          ],
          tasks=[task_checkmark("Stufe 5 ist offen")],
          rewards=[reward_table("s1_uncommon")],
          deps=["s4"], icon="minecraft:diamond_block", size=1.75, shape="hexagon"),

    entry("draconic", 0, 0, S5, "&dFusioniere Drakonisch", "Draconic Evolution: Schild, Flug, Untod.",
          ["Wyvern-Stück als Katalysator, 8 Injektoren mit 4 Netherit, Wyvernkern, 2 Erwachten Barren, Drakonischem Energiekern, 32 Millionen OP. Kapitel &5Draconic: Erwacht und Chaos&r.",
           "",
           "Die &6Drakonische Brustplatte&r mit Schildkapazität, Flug und Untod-Modul ist die Rüstung für den Chaoswächter. Der &6Drakonische Bogen&r schmilzt seinen Schild von 16 000 am schnellsten."],
          task_checkmark("Drakonisches Stück gebaut"), "minecraft:bow", ["s5"]),

    entry("chaotic", 1, 0, S5, "&8Fusioniere Chaotisch", "Draconic Evolution: das letzte Werkzeug.",
          ["Drakonisches Stück, 6 Erwachte Draconiumbarren, Chaotischer Kern, Chaotischer Energiekern, 128 Millionen OP.",
           "",
           "Chaotische Waffen knacken die Kristalle eines Chaoswächters direkt. Für weitere Inseln wird der Kampf damit deutlich leichter."],
          task_checkmark("Chaotisches Stück gebaut"), "minecraft:obsidian", ["s5"]),

    entry("ma_supremium", 2, 0, S5, "&cVeredle auf Supremium", "Mystical Agriculture: unzerstörbar.",
          ["Imperium-Werkzeug in die Mitte, 2 Supremiumbarren und 2 Supremium-Edelsteine drumherum. Erwachtes Supremium kommt aus dem Erweckungsaltar.",
           "",
           "Supremium: unzerstörbar, Tempo 25, +20 Schaden. Erwachtes Supremium: Tempo 30, +25 Schaden. Die Rüstung nimmt Augmente wie Flug und Nachtsicht."],
          task_checkmark("Supremium-Werkzeug gebaut"), "mysticalagriculture:inferium_essence", ["s5"]),

    quest("done", COLS[4], S5, "&6&lVoll ausgerüstet",
          subtitle="Von der Eisenspitzhacke bis zum Drakonischen Bogen.",
          description=[
              "Wer diese Liste von oben bis unten abgehakt hat, hat jede Werkzeugleiter des Packs einmal gesehen. Für den Chaoswächter zählt am Ende: Schild, Flug, Untod und ein schneller Bogen.",
              "",
              "&eKronwerke:&r Ausrüstung kostet Material, das auch der Obelisk will. Rüste die Leute zuerst aus, die für den Server kämpfen.",
          ],
          tasks=[task_checkmark("Liste durch")],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["draconic", "chaotic", "ma_supremium"], icon="minecraft:diamond_chestplate", size=2.0, shape="gear"),
]

images = [
    banner("list_gear/title", "Werkzeug und Rüstung", 10, -4.2, height=1.75, kind="title", colour="brass"),
    banner("list_gear/s1", "Stufe 1: Steinwerk", 11.75, S1 - 1.6, height=0.9, colour="stone"),
    banner("list_gear/s2", "Stufe 2: Messingwerk", 11.75, S2 - 1.6, height=0.9, colour="brass"),
    banner("list_gear/s3", "Stufe 3: Stahlwerk", 11.75, S3 - 1.6, height=0.9, colour="water"),
    banner("list_gear/s4", "Stufe 4: Sternwerk", 11.75, S4 - 1.6, height=0.9, colour="end"),
    banner("list_gear/s5", "Stufe 5: Chaoswerk", 11.75, S5 - 1.6, height=0.9, colour="fire"),
]

chapter(C, "Checkliste: Werkzeug und Rüstung", "minecraft:diamond_pickaxe", "lists", quests, shape="circle",
        order=69, stage=1,
        subtitle=["Werkzeug, Waffen, Rüstung und Flughilfen, ein Haken pro Stück, nach Stufen."], images=images)
