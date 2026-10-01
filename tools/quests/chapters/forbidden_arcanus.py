"""Forbidden and Arcanus in stage 2: arcane crystals, darkstone, mundabitur dust and deorum, the
Hephaestus Forge (a smithing table on a 9x9 darkstone base, awakened with mundabitur dust), its
pedestals, obelisks and the blacksmith gavel, the four essences (aureal, souls, blood, experience),
the first rituals up to the tier 2 upgrade, the Clibano, obsidiansteel and the obsidian skull,
edelwood, dark matter and stellarite. Numbers come from the mod jar (2.6.1): block patterns, ritual
JSONs, HephaestusForgeLevel and the loot tables. Forge tier 3 opens in stage 3, tiers 4 and 5 and the
Draco Arcanus gear in stage 4; they are only mentioned. The mod has no German lang file, so item
names are given as the game shows them."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "forbidden_arcanus"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Arkankristalle --------------------------------------------------------
    quest("crystals", 0, 1, "&d&lGrab Arcane Crystals aus",
          subtitle="Der Kristall, aus dem alles hier gemacht ist.",
          description=[
              "&6Arcane Crystal Ore&r liegt in der Oberwelt zwischen &eY -40 und Y 14&r, am dichtesten um Y -13. Die Adern sind klein (bis 5 Blöcke), drei pro Chunk. Jeder Block gibt einen &6Arcane Crystal&r, mit Glück mehr.",
              "",
              pic("forbidden_arcanus:arcane_crystal"),
              "",
              "&5Forbidden and Arcanus&r öffnet komplett mit &6Stufe 2&r: die Hephaestus Forge bis Stufe 2, der Clibano, Edelholz, Obsidianschädel. Nur die &eForge-Stufe 3&r wartet bis Stufe 3, die Stufen 4 und 5 und die Draco-Arcanus-Rüstung bis Stufe 4.",
              "",
              "&eKronwerke:&r Für das Obelisk-Ziel zählt hier nichts direkt. Dieses Kapitel ist ein Seitenweg für alle, die Rituale und seltsame Werkzeuge mögen.",
          ],
          tasks=[task_item("forbidden_arcanus:arcane_crystal", 8)],
          rewards=[reward_item("forbidden_arcanus:arcane_crystal", 8), reward_table("s2_common")],
          icon="forbidden_arcanus:arcane_crystal", size=2.0, shape="hexagon"),

    quest("dust", 2.5, 0, "&dBrenne Arcane Crystal Dust",
          subtitle="Kristall in den Ofen, Staub heraus.",
          description=[
              "Ein &6Arcane Crystal&r im Ofen wird in 7,5 Sekunden zu &6Arcane Crystal Dust&r, im Schmelzofen in der halben Zeit.",
              "",
              "Der Staub steckt in fast jedem Rezept dieses Kapitels: Mundabitur Dust, Deorum, Aureal Bottle, Arcane Bone Meal (ein Staub und vier Knochenmehl ergeben vier). Brenn gleich einen Stapel.",
          ],
          tasks=[task_item("forbidden_arcanus:arcane_crystal_dust", 8)],
          rewards=[reward_item("forbidden_arcanus:arcane_crystal", 8), reward_xp(3)],
          deps=["crystals"]),

    quest("darkstone", 2.5, 2, "&8Finde Darkstone",
          subtitle="Der schwarze Stein knapp über dem Grundgestein.",
          description=[
              "&6Darkstone&r liegt ganz unten, in den &e13 Blöcken über dem Grundgestein&r (Y -64 bis Y -51), in großen Adern bis 20 Blöcke, 28 pro Chunk. Vier Darkstone im Quadrat ergeben vier &6Polished Darkstone&r.",
              "",
              "Die Hephaestus Forge braucht &e48 Polished Darkstone&r für den Boden, dazu etwa 20 weitere für die verzierten Blöcke und je drei pro Podest. Ein Stapel Darkstone reicht knapp, zwei sind bequem.",
              "",
              "&eTipp:&r Darkstone ersetzt auch Steinziegel: Polished Darkstone Bricks, Platten, Treppen, Mauern, alles an der Werkbank oder im Steinsäger.",
          ],
          tasks=[task_item("forbidden_arcanus:polished_darkstone", 64)],
          rewards=[reward_item("forbidden_arcanus:polished_darkstone", 32), reward_xp(3)],
          deps=["crystals"], icon="forbidden_arcanus:polished_darkstone"),

    quest("mundabitur", 5, 0, "&cMisch Mundabitur Dust",
          subtitle="Der Staub, der Strukturen zum Leben erweckt.",
          description=[
              "Formlos an der Werkbank: &6Arcane Crystal Dust&r, &6Redstone&r, &6Lohenstaub&r, &6Knochenmehl&r, eine &6Phantomhaut&r und &6Schwarzpulver&r ergeben &e4 Mundabitur Dust&r.",
              "",
              "Mit Mundabitur Dust erweckst du die drei Bauwerke der Mod: Rechtsklick auf den Schmiedetisch der Hephaestus Forge, auf den Arcane Crystal Obelisk und auf den Clibano Core. Dazu steckt er in jedem Deorum-Barren.",
              "",
              "&cAchtung:&r Rechtsklick auf einen Creeper lädt ihn auf wie ein Blitz. Nicht aus Versehen machen.",
              "",
              "&eTipp:&r Phantomhäute sind der Engpass. Wer drei Nächte nicht schläft, bekommt Besuch, und Phantome lassen sich gut vom Dach aus abschießen.",
          ],
          tasks=[task_item("forbidden_arcanus:mundabitur_dust", 4)],
          rewards=[reward_item("minecraft:phantom_membrane", 2), reward_item("minecraft:gunpowder", 8), reward_xp(5)],
          deps=["dust"], icon="forbidden_arcanus:mundabitur_dust"),

    quest("deorum", 7.5, 0, "&6Schmiede Deorum",
          subtitle="Gold, das Magie leitet.",
          description=[
              "Ein &6Goldbarren&r in die Mitte, links und rechts je ein &6Mundabitur Dust&r, oben und unten je ein &6Arcane Crystal Dust&r, &6Holzkohle&r in die vier Ecken: ein &6Deorum Ingot&r.",
              "",
              pic("forbidden_arcanus:deorum_ingot"),
              "",
              "Deorum ist das Edelmetall der Mod. Ein Barren macht aus acht Polished Darkstone acht &6Arcane Polished Darkstone&r, neun Deorum Nuggets vergolden neun verzierte Blöcke, und der Magic Wand und der Spectral Eye Amulet brauchen es ebenfalls.",
              "",
              "&eRechnung:&r Für die Schmiede mit vier Podesten und zwei Obelisken brauchst du etwa &e5 Deorum&r, also 10 Mundabitur Dust und 10 Arcane Crystal Dust.",
          ],
          tasks=[task_item("forbidden_arcanus:deorum_ingot", 5)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("forbidden_arcanus:mundabitur_dust", 4), reward_table("s2_common")],
          deps=["mundabitur"], icon="forbidden_arcanus:deorum_ingot", size=1.5, shape="square"),

    quest("runes", 5, 2, "&3Brich Runic Stone",
          subtitle="Steine mit Zeichen drauf.",
          description=[
              "&6Runic Stone&r ist seltenes Gestein mit leuchtenden Zeichen, unterhalb von &eY 2&r, am häufigsten unterhalb von Y -20, auch als Runic Deepslate und Runic Darkstone. Abgebaut gibt es eine &6Rune&r, mit Glück mehr. Mit Behutsamkeit bleibt der Stein ganz und lässt sich im Ofen zur Rune brennen.",
              "",
              pic("forbidden_arcanus:rune"),
              "",
              "Runen brauchst du für das &6Test Tube&r (Glasflasche und Rune), den &6Quantum Core&r und &6Runic Glass&r (acht Glas um eine Rune). Vier Runen reichen fürs Erste.",
          ],
          tasks=[task_item("forbidden_arcanus:rune", 4)],
          rewards=[reward_item("forbidden_arcanus:rune", 2), reward_xp(3)],
          deps=["darkstone"], icon="forbidden_arcanus:rune", optional=True),

    quest("stellarite", 7.5, 2, "&eFinde Stella Arcanum",
          subtitle="Ein Stern im Stein, und er explodiert.",
          description=[
              "&6Stella Arcanum&r ist ein seltenes Erz zwischen &eY -44 und Y 42&r, zwei winzige Adern pro Chunk. Baust du es ohne &6Behutsamkeit&r ab, &cexplodiert&r es mit Radius 3 und macht Blockschaden, lässt aber ein &6Stellarite Piece&r fallen.",
              "",
              pic("forbidden_arcanus:stellarite_piece"),
              "",
              "Mit Behutsamkeit nimmst du den Block mit und baust ihn zu Hause ab, wo die Explosion nichts kaputt macht. Neun Pieces ergeben einen &6Stellarite Block&r.",
              "",
              "&eAusblick:&r Stellarite brauchst du für die &eForge-Stufe 4&r (vier Pieces), die Eternal Stella und den Boss Catcher. Das alles kommt in Stufe 3 und 4, sammle es trotzdem jetzt schon.",
          ],
          tasks=[task_item("forbidden_arcanus:stellarite_piece", 1)],
          rewards=[reward_item("forbidden_arcanus:stellarite_piece", 1), reward_table("s2_common")],
          deps=["darkstone"], icon="forbidden_arcanus:stellarite_piece"),

    # ---- Die Hephaistos-Schmiede ----------------------------------------------
    quest("base", 10.5, 1, "&7Lege den Boden der Schmiede",
          subtitle="9 mal 9 Darkstone mit Gold und Kristall.",
          description=[
              "Der Boden ist ein &e9 mal 9 Quadrat&r, an jeder Ecke fehlen der Eckblock und je zwei Blöcke daneben: &e48 Polished Darkstone&r, &e9 Gilded Chiseled Polished Darkstone&r und &e4 Chiseled Arcane Polished Darkstone&r.",
              "",
              "&6Chiseled Polished Darkstone&r: zwei Polished Darkstone Slabs übereinander. Formlos mit einem &6Deorum Nugget&r wird daraus die vergoldete Version. &6Chiseled Arcane Polished Darkstone&r: zwei Arcane Polished Darkstone Slabs übereinander.",
              "",
              "&eSo liegen sie:&r Ein vergoldeter Block in der Mitte, die vier arkanen Blöcke direkt neben ihm (Nord, Süd, Ost, West). Die acht anderen vergoldeten Blöcke bilden einen Ring: je einer auf den vier Achsen drei Blöcke von der Mitte, je einer auf den vier Diagonalen zwei Blöcke schräg von der Mitte. Alles dazwischen Polished Darkstone.",
              "",
              img("forbidden_arcanus:textures/block/gilded_chiseled_polished_darkstone.png", 32, 32),
              "",
              "&eTipp:&r Ponder zeigt den Bau Schritt für Schritt: Halte die Hephaestus Forge in JEI mit der Maus und drück &eW&r.",
          ],
          tasks=[task_item("forbidden_arcanus:gilded_chiseled_polished_darkstone", 9),
                 task_item("forbidden_arcanus:chiseled_arcane_polished_darkstone", 4)],
          rewards=[reward_item("forbidden_arcanus:polished_darkstone", 16), reward_table("s2_common"), reward_xp(5)],
          deps=["deorum", "darkstone"], icon="forbidden_arcanus:gilded_chiseled_polished_darkstone", size=1.5, shape="square"),

    quest("awaken", 13, 1, "&c&lErwecke die Hephaestus Forge",
          subtitle="Ein Schmiedetisch, ein Staub, ein Blitz.",
          description=[
              "Stell einen &6Schmiedetisch&r auf den vergoldeten Block in der Mitte. Die acht Felder über den äußeren vergoldeten Blöcken müssen frei sein. Rechtsklick mit &6Mundabitur Dust&r auf den Schmiedetisch, ein roter Blitz schlägt ein, und die &6Hephaestus Forge&r steht.",
              "",
              "&eSo liest du das Fenster:&r In der Mitte liegt der &6Hauptgegenstand&r des Rituals. Darunter vier Slots für die Essenzen: &dAureal&r, &bSeelen&r, &cBlut&r und &aErfahrung&r, mit Balken daneben. Dazu vier Slots für Verstärker-Relikte, auf Stufe 1 ist nur der erste offen, jede weitere Stufe schaltet einen frei. Stufe 1 fasst &e1 000 Aureal, 10 Seelen, 10 000 Blut und 900 Erfahrung&r.",
              "",
              "&cAchtung:&r Die Schmiede prüft alle vier Sekunden ihren Boden. Fehlt ein Block, geht sie aus und nimmt nichts mehr an. Sie lässt sich mit der Spitzhacke abbauen und auf einem neuen Boden wieder setzen.",
          ],
          tasks=[task_checkmark("Die Schmiede steht und ist aktiv")],
          rewards=[reward_item("forbidden_arcanus:mundabitur_dust", 4), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["base", "mundabitur"], icon="forbidden_arcanus:hephaestus_forge_tier_1", size=2.0, shape="gear"),

    quest("pedestals", 15.5, 0, "&7Stell Darkstone Pedestals auf",
          subtitle="Hier liegen die Zutaten eines Rituals.",
          description=[
              "Ein &6Darkstone Pedestal&r: oben drei &6Arcane Polished Darkstone Slabs&r, in der Mitte ein &6Arcane Polished Darkstone Pillar&r (zwei Arcane Polished Darkstone übereinander), unten drei &6Polished Darkstone&r.",
              "",
              "Podeste gehören auf die &eacht äußeren vergoldeten Blöcke&r. Rechtsklick mit einem Gegenstand legt genau einen darauf, Rechtsklick mit leerer Hand nimmt ihn wieder. Die Schmiede sieht jedes Podest im Umkreis von &e4 Blöcken&r.",
              "",
              "Vier Podeste reichen für jedes Ritual bis Stufe 2. Die übrigen vier Plätze sind für Obelisken da.",
          ],
          tasks=[task_item("forbidden_arcanus:darkstone_pedestal", 4)],
          rewards=[reward_item("forbidden_arcanus:deorum_ingot", 2), reward_xp(5)],
          deps=["awaken"], icon="forbidden_arcanus:darkstone_pedestal"),

    quest("obelisks", 15.5, 2, "&dErrichte Arcane Crystal Obelisks",
          subtitle="Aureal, das von selbst tropft.",
          description=[
              "Ein Obelisk ist ein Turm aus drei Blöcken: unten ein &6Arcane Polished Darkstone&r, darauf &e2 Arcane Crystal Blocks&r (je neun Kristalle). Rechtsklick mit &6Mundabitur Dust&r auf den Turm macht daraus einen &6Arcane Crystal Obelisk&r.",
              "",
              "Der Obelisk arbeitet nur, wenn er auf &6Gilded Chiseled Polished Darkstone&r steht, also auf einem der acht äußeren Plätze der Schmiede. Dort gibt er der Schmiede im Umkreis von 4 Blöcken alle &e5 Sekunden 1 Aureal&r. Vier Obelisken füllen Stufe 1 in etwa 20 Minuten.",
              "",
              "&eTipp:&r Der fertige Obelisk lässt sich abbauen und als ganzer Block neu setzen, du brauchst den Staub nur einmal.",
          ],
          tasks=[task_item("forbidden_arcanus:arcane_crystal_block", 4)],
          rewards=[reward_item("forbidden_arcanus:arcane_crystal", 16), reward_table("s2_common"), reward_xp(5)],
          deps=["awaken"], icon="forbidden_arcanus:arcane_crystal_obelisk"),

    quest("gavel", 18, 1, "&7Baue einen Blacksmith Gavel",
          subtitle="Der Hammer, der ein Ritual startet.",
          description=[
              "Erst der Kopf: &e5 Tonklumpen&r in T-Form, drei oben, zwei darunter versetzt, ergeben einen &6Blacksmith Gavel Head&r. Dann der Hammer wie eine Spitzhacke: &6Eisenbarren&r, Kopf, Eisenbarren oben, Eisen, Stock, Eisen in der Mitte, Stock unten: ein &6Iron Blacksmith Gavel&r.",
              "",
              "Rechtsklick mit dem Gavel auf die Schmiede startet das Ritual, wenn Zutaten und Essenzen passen. Das kostet &e50 Haltbarkeit&r, der Eisenhammer schafft also 5 Rituale, der Diamanthammer 31.",
              "",
              "&eNebenbei:&r Der Gavel ist eine echte Spitzhacke, und beim Abbauen von Erz verdoppelt er mit &e30 Prozent&r Chance die Drops (nicht mit Behutsamkeit).",
          ],
          tasks=[task_item("forbidden_arcanus:iron_blacksmith_gavel", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_item("minecraft:clay_ball", 10), reward_xp(5)],
          deps=["awaken"], icon="forbidden_arcanus:iron_blacksmith_gavel"),

    # ---- Essenzen --------------------------------------------------------------
    quest("blood", 10.5, 7, "&cZapf Blut und Erfahrung",
          subtitle="Zwei Essenzen, die man sich erkämpft.",
          description=[
              "&cBlut:&r Jedes Lebewesen, das im Umkreis von &e5 Blöcken&r um die Schmiede Schaden nimmt, gibt ihr &e20 Blut pro Lebenspunkt&r. Ein Zombie mit 20 Lebenspunkten sind 400 Blut. Eine kleine Mobfalle neben der Schmiede füllt den Balken von selbst.",
              "",
              "Unterwegs: Halte ein &6Test Tube&r (Glasflasche und Rune) in der &eZweithand&r und schlag mit der Haupthand zu. Es wird zum Blood Test Tube und sammelt 20 Blut pro Schadenspunkt, bis 3 000. In den Blutslot gelegt läuft es mit 10 pro Tick in die Schmiede.",
              "",
              "&aErfahrung:&r Eine &6Erfahrungsflasche&r im Erfahrungsslot gibt 15. Verzauberte Gegenstände oder Bücher geben ihre Verzauberungen ab (Flüche bleiben) und liefern zwischen der Hälfte und dem vollen Wert ihrer Mindestkosten als Essenz.",
          ],
          tasks=[task_item("forbidden_arcanus:test_tube", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 4), reward_xp(5)],
          deps=["awaken"], icon="forbidden_arcanus:test_tube"),

    quest("souls", 13, 7, "&bFang Seelen",
          subtitle="Lost Souls, Seelensand und ein Extraktor.",
          description=[
              "&6Lost Souls&r sind kleine bleiche Geister, die überall in der Oberwelt auftauchen, oft zu zweit oder dritt. Jede lässt eine &6Soul&r fallen, und eine Soul ist &e1 Seele&r in der Schmiede.",
              "",
              "Der &6Soul Extractor&r (ein Utrem Jar oben links, darunter zwei Netherziegel und ein Quarzblock, unten ein Netherquarz) zieht aus &6Seelensand&r eine Soul: Rechtsklick halten, der Sand wird zu Soulless Sand. Das Utrem Jar sind acht Glas um ein Edelwood Plank, bis dahin leihst du dir eins oder sammelst von Hand.",
              "",
              "&eZehnfach:&r Rechtsklick mit einer &6Aureal Bottle&r auf eine Lost Soul macht eine &6Enchanted Lost Soul&r daraus. Ihre &6Enchanted Soul&r zählt &e10 Seelen&r und ist der beste Brennstoff für den Clibano.",
          ],
          tasks=[task_item("forbidden_arcanus:soul", 10)],
          rewards=[reward_item("forbidden_arcanus:soul", 5), reward_table("s2_common"), reward_xp(5)],
          deps=["awaken"], icon="forbidden_arcanus:soul"),

    quest("aureal", 15.5, 7, "&dBraue Aureal Bottles",
          subtitle="Die Essenz, die auch du selbst trägst.",
          description=[
              "Acht &6Arcane Crystal Dust&r um einen &6Trank der Regeneration II&r ergeben eine &6Aureal Bottle&r. Im Aureal-Slot gibt sie &e35 Aureal&r, getrunken füllt sie dein eigenes Aureal um 35 (du trägst höchstens 100).",
              "",
              "Dein eigenes Aureal brauchst du für den &6Magic Wand&r (Edelwood Stick, Deorum Ingot, Arcane Crystal diagonal): 1,5 Sekunden aufladen, ein Geschoss für 5 Aureal und 5 magischen Schaden. Und für den Quantum Catcher, siehe Rituale.",
              "",
              "&eTipp:&r Für die Schmiede sind Obelisken billiger. Flaschen lohnen sich, wenn ein Ritual gerade 100 Aureal zu wenig hat.",
          ],
          tasks=[task_item("forbidden_arcanus:aureal_bottle", 1)],
          rewards=[reward_item("forbidden_arcanus:arcane_crystal_dust", 8), reward_item("minecraft:glowstone_dust", 4), reward_xp(5)],
          deps=["obelisks"], icon="forbidden_arcanus:aureal_bottle"),

    # ---- Rituale ---------------------------------------------------------------
    quest("quantum", 18, 7, "&5&lDas erste Ritual: Quantum Catcher",
          subtitle="Ein Mob in der Tasche.",
          description=[
              "&eHauptgegenstand:&r ein &6Quantum Core&r (Rune, Feuerstein und Mundabitur Dust formlos) in der Mitte der Schmiede. &eAuf den Podesten:&r &e4 Spawner Scrap&r. &eEssenzen:&r 200 Aureal, 1 200 Blut, 155 Erfahrung, 5 Seelen. Dann Rechtsklick mit dem Gavel.",
              "",
              "&6Spawner Scrap&r fällt, wenn du einen &6Spawner&r ohne Behutsamkeit abbaust, einer pro Spawner. Vier Spawner also, Verliese und Minen durchsuchen.",
              "",
              "Ein Ritual dauert &e25 Sekunden&r. Erscheint über der Schmiede ein Zeichen, passt alles. Die Podeste leeren sich, das Ergebnis liegt im Hauptslot.",
              "",
              "Der &6Quantum Catcher&r fängt mit Rechtsklick ein Tier oder Monster und setzt es mit Rechtsklick auf den Boden wieder aus. Das kostet &edein eigenes Aureal&r: so viel wie die maximale Lebenskraft des Wesens, bei Tieren die Hälfte. Spieler und Dorfbewohner gehen nicht.",
          ],
          tasks=[task_item("forbidden_arcanus:quantum_catcher", 1)],
          rewards=[reward_item("forbidden_arcanus:aureal_bottle", 2), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["gavel", "aureal"], icon="forbidden_arcanus:quantum_catcher", size=1.75, shape="hexagon"),

    quest("tier2", 20.5, 7, "&c&lHeb die Schmiede auf Stufe 2",
          subtitle="Mehr Platz für Essenzen, neue Rituale.",
          description=[
              "&eHauptgegenstand:&r ein &6Edelwood Plank&r. &eAuf den Podesten:&r &e4 Arcane Crystal&r und &e4 Spawner Scrap&r. &eEssenzen:&r 500 Aureal, 6 000 Blut, 10 Seelen. Die Schmiede muss genau Stufe 1 haben.",
              "",
              "Danach fasst sie &e3 000 Aureal, 50 Seelen, 15 000 Blut und 1 350 Erfahrung&r, und der zweite Verstärker-Slot geht auf. Stufe 2 schaltet das Terrastomp Prism frei.",
              "",
              "&eKronwerke:&r Die &eStufe 3 der Schmiede&r (4 Arcane Crystal, 4 Deorum, 1 000 Aureal, 9 000 Blut, 50 Seelen auf einem Chiseled Polished Darkstone) ist bis &6Stufe 3&r des Servers gesperrt, Stufe 4 und 5 bis Stufe 4.",
          ],
          tasks=[task_item("forbidden_arcanus:edelwood_planks", 1), task_item("forbidden_arcanus:spawner_scrap", 4),
                 task_checkmark("Die Schmiede zeigt Stufe 2")],
          rewards=[reward_table("s2_rare"), reward_item("forbidden_arcanus:deorum_ingot", 4), reward_xp(20)],
          deps=["quantum", "edelwood"], icon="forbidden_arcanus:hephaestus_forge_tier_2", size=2.5, shape="gear"),

    quest("terrastomp", 23, 6, "&2Terrastomp Prism",
          subtitle="Ein Werkzeug, das ganze Flächen abbaut.",
          description=[
              "&eStufe 2, mit Elementarium im Verstärker-Slot.&r Hauptgegenstand ein &6Diamantblock&r, auf den Podesten &e2 Feuerstein, 2 Tropfsteinblöcke, 2 Tropfsteinspitzen&r. Essenzen: 300 Aureal, 1 500 Blut, 9 Seelen.",
              "",
              "Das Prisma kommt auf den &6Schmiedetisch&r: Vorlage ist das &6Smithing Template&r der Mod (acht Darkstone um eine Netherit-Vorlage), dazu dein Werkzeug und das Prisma. Das Werkzeug bekommt &6Demolishing&r und baut 3 mal 3 Blöcke auf einmal ab.",
              "",
              "Genauso gehen Smelter Prism (Fiery, schmilzt Erz beim Abbau, braucht ebenfalls Elementarium) und Ferrognetic Mixture (Magnetized). Die Mixture macht per Rechtsklick auch ein Podest magnetisch, dann sammelt es Gegenstände von selbst ein.",
          ],
          tasks=[task_item("forbidden_arcanus:terrastomp_prism", 1)],
          rewards=[reward_item("minecraft:diamond", 4), reward_table("s2_uncommon")],
          deps=["tier2"], icon="forbidden_arcanus:terrastomp_prism", optional=True),

    quest("enhancers", 23, 8, "&6Verstärker-Relikte",
          subtitle="Was in die zwei oberen Slots gehört.",
          description=[
              "Relikte findet man, nicht craftet man. Sie liegen in den oberen Slots der Schmiede und ändern, was sie kann:",
              "",
              "&6Artisan Relic&r (Schmiedetruhen in Dörfern, oder vom Wandernden Händler für 18 Smaragde): Rituale kosten nur &e75 Prozent Erfahrung&r. Im Clibano erlaubt es Legierungen wie Obsidiansteel.",
              "&6Crimson Stone&r (Plünderer-Außenposten): Rituale brauchen nur &ehalb so viele Seelen&r.",
              "&6Elementarium&r (Dschungeltempel, Wüstentempel, Ozeanruinen): schaltet die Prismen frei.",
              "&6Maledictus Pact&r (Bastionsschatz) und &6Divine Pact&r: verfluchte und göttliche Gegenstände, erst für die hohen Stufen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:emerald", 6)],
          deps=["tier2"], icon="forbidden_arcanus:artisan_relic", optional=True),

    quest("outlook", 25.5, 7, "&dAusblick auf Stufe 3 und 4",
          subtitle="Was hinter der zweiten Stufe wartet.",
          description=[
              "Mit &6Stufe 3&r des Servers öffnet die &eForge-Stufe 3&r: 5 000 Aureal, 100 Seelen, 30 000 Blut. Dazu die &6Eternal Stella&r (ein Diamant, drei Xpetrified Orbs und ein Stellarite Piece), die Werkzeuge unzerstörbar macht, der &6Quantum Injector&r und das Sea Prism.",
              "",
              "In &6Stufe 4&r folgen die Forge-Stufen 4 und 5 (Stellarite, Runen, Sculk-Katalysatoren, zwei Dark Nether Stars), die &6Draco Arcanus&r-Rüstung aus Netheritrüstung, Drachenschuppen und Obsidiansteel, und darüber die Tyr-Rüstung.",
              "",
              "Drachenschuppen gibt es nur vom Enderdrachen und aus Endsiedlungen. Bis dahin: Stellarite und Obsidiansteel horten.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(10)],
          deps=["tier2"], icon="forbidden_arcanus:dark_nether_star", optional=True),

    # ---- Edelholz und Dunkle Materie ------------------------------------------
    quest("clibano", 13, 13, "&6Baue den Clibano",
          subtitle="Ein Hochofen, der mit Seelen heizt.",
          description=[
              "Ein &6Clibano Core&r sind acht &6Darkstone&r um einen &6Schmelzofen&r. Dann der Bau: ein &e3 mal 3 mal 3 Würfel&r aus &6Polished Darkstone Bricks&r, an den acht Ecken &6Polished Darkstone&r, innen hohl, und der Core sitzt in der Mitte einer Seitenwand. Rechtsklick mit &6Mundabitur Dust&r auf den Core.",
              "",
              "Der Clibano schmilzt Erze und Roherze wie ein Schmelzofen in 5 Sekunden. Eine &6Soul&r im Seelenslot macht &bSeelenfeuer&r, 1,5 mal so schnell, eine &6Enchanted Soul&r &dverzaubertes Feuer&r, 2,5 mal so schnell.",
              "",
              "&eRückstände:&r Bei jedem dritten Erz bleibt ein Rest der Sorte im Clibano. Neun Reste ergeben einen ganzen Block, Eisenblock, Kupferblock oder Arcane Crystal Block. Das ist die Erzvermehrung der Mod.",
          ],
          tasks=[task_item("forbidden_arcanus:clibano_core", 1)],
          rewards=[reward_item("forbidden_arcanus:polished_darkstone", 32), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["souls"], icon="forbidden_arcanus:clibano_core", size=1.5, shape="hexagon"),

    quest("obsidiansteel", 15.5, 13, "&8Schmilz Obsidiansteel",
          subtitle="Roheisen und Obsidian in einem Feuer.",
          description=[
              "Leg ein &6Artisan Relic&r in den Verstärker-Slot des Clibano. Dann nimmt er zwei Zutaten auf einmal: &6Roheisen&r und &6Obsidian&r werden zu einem &6Obsidiansteel Ingot&r.",
              "",
              pic("forbidden_arcanus:obsidiansteel_ingot"),
              "",
              "Obsidiansteel steckt in den Obsidianschädeln, im Corrupti Dust, im Dark Nether Star und in der Draco-Arcanus-Rüstung. Ohne Relikt gibt es kein Obsidiansteel, also Dorfschmieden plündern oder den Wandernden Händler abpassen.",
          ],
          tasks=[task_item("forbidden_arcanus:obsidiansteel_ingot", 8)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["clibano"], icon="forbidden_arcanus:obsidiansteel_ingot"),

    quest("skull", 18, 14, "&8Setz den Obsidian Skull auf",
          subtitle="Feuerresistenz, die Risse bekommt.",
          description=[
              "Acht &6Obsidiansteel Ingots&r um einen &6Skelettschädel&r ergeben den &6Obsidian Skull&r. Als Helm getragen gibt er dauerhaft &eFeuerresistenz&r.",
              "",
              "Aber: Solange du &cbrennst&r, bekommt er alle 8 bis 13 Sekunden einen Riss: Obsidian Skull, Cracked, Fragmented, Fading, und dann bleibt ein nackter Skelettschädel. Zwei Obsidiansteel an der Werkbank reparieren jede Stufe um eine zurück.",
              "",
              "Für Lavaseen im Nether ist das ein Rettungsring, nicht mehr. Wer dauerhaft Feuerresistenz will, braucht den Eternal Obsidian Skull aus den höheren Stufen.",
          ],
          tasks=[task_item("forbidden_arcanus:obsidian_skull", 1)],
          rewards=[reward_item("forbidden_arcanus:obsidiansteel_ingot", 4), reward_xp(5)],
          deps=["obsidiansteel"], icon="forbidden_arcanus:obsidian_skull", optional=True),

    quest("edelwood", 18, 12, "&2Zieh Edelwood",
          subtitle="Ein Baum aus einer verdorbenen Seele.",
          description=[
              "&6Corrupti Dust&r (Obsidiansteel Ingot, Lohenstaub, Netherwarze, Arcane Crystal Dust und ein Ender Pearl Fragment formlos, ergibt vier) auf eine &6Lost Soul&r macht eine &6Corrupt Lost Soul&r, die eine &6Corrupt Soul&r fallen lässt. Rechtsklick damit auf einen &6Eichensetzling&r oder &6Toten Busch&r: &6Growing Edelwood&r.",
              "",
              "Das wächst bei Licht 9 zu einem knorrigen Stamm von 2 bis 4 &6Edelwood Logs&r mit einem geschnitzten Gesicht oben, Knochenmehl hilft mit 45 Prozent. Die Äste geben &6Edelwood Sticks&r. Ein Stamm ergibt nur &e2 Edelwood Planks&r. Der Wandernde Händler verkauft Growing Edelwood auch für 6 Smaragde.",
              "",
              "&eEigenheiten:&r Ein Stamm im Regen füllt sich mit Wasser. Ab und zu wird ein Stamm ölig, dann gibt eine Glasflasche &6Edelwood Oil&r (zwei schwarze Farbstoffe). Der &6Edelwood Bucket&r aus fünf Planks fasst &e4 Eimer&r, aber mit Lava verkohlt er irgendwann in der Tasche.",
          ],
          tasks=[task_item("forbidden_arcanus:edelwood_log", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_table("s2_common"), reward_xp(10)],
          deps=["obsidiansteel"], icon="forbidden_arcanus:edelwood_log"),

    quest("dark_matter", 20.5, 12, "&5Brenne Dark Matter",
          subtitle="Ein Scheit Edelholz wird zur Finsternis.",
          description=[
              "Ein &6Edelwood Log&r im Ofen wird in 20 Sekunden zu &6Dark Matter&r. Allein ist es nur ein Klumpen, aber wirf es zusammen mit einem &6Corrupti Dust&r auf den Boden, auf ein freies Feld: ein &6Black Hole&r entsteht.",
              "",
              "Das Schwarze Loch zieht im Umkreis von &e5 Blöcken&r Gegenstände, Pfeile und Erfahrungskugeln an. Was in die Mitte gerät, nimmt 4 Schaden pro Tick. Aus je &e60 Erfahrungspunkten&r spuckt es einen &6Xpetrified Orb&r aus: Rechtsklick gibt 91 Erfahrungspunkte, oder er liefert 91 Erfahrung in der Schmiede.",
              "",
              "&eTipp:&r Ein Schwarzes Loch neben einer Mobfalle ist ein Erfahrungsspeicher. Drei Orbs braucht später die Eternal Stella.",
          ],
          tasks=[task_item("forbidden_arcanus:dark_matter", 1)],
          rewards=[reward_item("forbidden_arcanus:edelwood_log", 4), reward_xp(5)],
          deps=["edelwood"], icon="forbidden_arcanus:dark_matter"),

    quest("dark_star", 20.5, 14, "&5Dark Nether Star",
          subtitle="Für die späten Stufen der Schmiede.",
          description=[
              "Ein &6Netherstern&r mit vier &6Obsidiansteel Ingots&r an den Seiten ergibt einen &6Dark Nether Star&r. Zwei davon braucht die &eForge-Stufe 5&r, und die kommt erst mit Stufe 4 des Servers.",
              "",
              "Ein weiterer Netherstern mit drei Fäden, einem Enderauge und zwei Deorum wird zum &6Spectral Eye Amulet&r, das sich per Rechtsklick ein- und ausschaltet.",
              "",
              "Wer den Wither ohnehin für Beacons legt, baut den Stern jetzt nebenbei. Alle anderen warten.",
          ],
          tasks=[task_item("forbidden_arcanus:dark_nether_star", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["skull"], icon="forbidden_arcanus:dark_nether_star", optional=True),
]

images = [
    banner("forbidden_arcanus/title", "Forbidden and Arcanus", 12, -5.4, height=1.75, kind="title", colour="magic"),
    banner("forbidden_arcanus/kristalle", "Arkankristalle", 3.7, -2.7, height=0.9, colour="magic"),
    banner("forbidden_arcanus/schmiede", "Die Hephaistos-Schmiede", 14.2, -2.7, height=0.9, colour="fire"),
    banner("forbidden_arcanus/essenzen", "Essenzen", 13, 4.8, height=0.9, colour="magic"),
    banner("forbidden_arcanus/rituale", "Rituale", 21.7, 4.8, height=0.9, colour="fire"),
    banner("forbidden_arcanus/edelholz", "Edelholz und Dunkle Materie", 17, 10.3, height=0.9, colour="stone"),
]

chapter(C, "Forbidden and Arcanus", "forbidden_arcanus:hephaestus_forge_tier_1", "magic", quests, shape="circle",
        order=52, stage=2,
        subtitle=["Stufe 2. Arkankristalle, die Hephaestus Forge und ihre Rituale, der Clibano und Edelholz."],
        images=images)
