"""Occultism in stage 3: the Afrit book, the infused pickaxe, goggles and iesnium, the spirit
miners and the dimensional mineshaft, the magic storage and its stabilizers, orange chalk and
the possessed bee, Kandar's Opened Conjure and the unbound Afrit for afrit essence (the stage 3
magic goal), red chalk, Abras' Conjure and its jobs, Sevira's Permanent Confinement, Odus' and
Posuc's Convocations, Osorin's Unbound Calling with the reinforced deepslate ritual (one of two
routes on Kronwerke), black chalk, the unbound Marid and Fatma's Incentivized Attraction.
Dragon's breath rituals (Marid miner and smelter, possessed shulker, dragonyst dust) and
Ronaza's Contact wait for stage 4 and are only named. Continues occultism.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "occultism_afrit"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Iesnium und Bergbau --------------------------------------------------------
    quest("afrit_book", 0, 0, "&c&lBind einen Afrit-Namen",
          subtitle="Ein Name, der brennt.",
          description=[
              "&6Taboo Book&r, &6Purified Ink&r, &6Awakened Feather&r und &e4 gelber Farbstoff&r ergeben das &6Book of Binding: Afrit&r.",
              "Dann formlos mit dem &6Dictionary of Spirits&r binden, wie bei Foliot und Djinni.",
              "",
              pic("occultism:book_of_binding_bound_afrit"),
              "",
              "Mit &6Stufe 3&r öffnen die zwei höchsten Ränge: &cAfrit&r für große Artefakte und starke Besessenheit, &9Marid&r als stärkste Geister überhaupt. Das Dictionary rät, Marid nur in Gruppen zu rufen.",
              "",
              "&eKronwerke:&r Das Magieziel von Stufe 3 will &e150 Afrit-Essenzen&r. Jede ist ein gerufener und besiegter Afrit. Dazu stecken zwei Essenzen in jedem &dElfenstern&r.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_afrit", 2)],
          rewards=[reward_item("minecraft:yellow_dye", 8), reward_table("s3_common")],
          icon="occultism:book_of_binding_bound_afrit", size=2.0, shape="hexagon"),

    quest("goggles", 2.4, -2.2, "&6Bau die Otherworld Goggles",
          subtitle="Sieh, was in Netherrack steckt.",
          description=[
              "&e8 Glasscheiben&r um einen &bSpirit Attuned Gem&r ergeben &6Lenses&r. In Eziveus' Spectral Compulsion mit &e2 Silber-&r und &e1 Goldbarren&r (Foliot-Buch) werden sie zu &6Infused Lenses&r.",
              "Linsen unten, &6Lens Frame&r (6 Otherstone, 2 Silber) darüber, &e3 Leder&r dazu: die Brille.",
              "",
              "Die Brille gibt dauerhaften Third Eye ohne Nebenwirkungen. Du siehst damit Iesnium-Erz im Netherrack. Abbauen kannst du es nur mit einer Infused oder Iesnium Pickaxe.",
          ],
          tasks=[task_item("occultism:otherworld_goggles", 1)],
          rewards=[reward_item("occultism:silver_ingot", 4), reward_xp(5)],
          deps=["afrit_book"], icon="occultism:otherworld_goggles"),

    quest("infused_pickaxe", 2.4, 0, "&6Binde eine Infused Pickaxe",
          subtitle="Ein Djinni im Edelstein bricht Iesnium.",
          description=[
              "&5Pentakel:&r Strigeor's Higher Binding.",
              "&6Schalen:&r ein &6Spirit Attuned Pickaxe Head&r (3 Gems in einer Reihe), &e2 Stöcke&r, &e2 Silberbarren&r.",
              "&cOpfer:&r keins. Start mit dem Djinni-Buch, 150 Sekunden.",
              "",
              "Die Spitzhacke ist sehr zerbrechlich. Sie soll nur das erste Iesnium holen, aus dem du eine haltbare Iesnium Pickaxe baust.",
          ],
          tasks=[task_item("occultism:infused_pickaxe", 1)],
          rewards=[reward_item("minecraft:diamond", 3), reward_xp(5)],
          deps=["afrit_book"], icon="occultism:infused_pickaxe"),

    quest("iesnium", 4.8, 0, "&6&lBau Iesnium ab",
          subtitle="Ein Erz, das wie Netherrack aussieht.",
          description=[
              "Stell die &6Divination Rod&r schleichend auf &6Netherrack&r ein, halt im Nether Rechtsklick und folg dem Leuchten. Mit Brille siehst du das Erz, mit der Infused Pickaxe baust du es ab.",
              "",
              "Das Erz gibt &6Raw Iesnium&r, Glück wirkt. Im Ofen wird es zu Barren. Mit Behutsamkeit fällt ein stabilisiertes Erz, das jede Spitzhacke abbaut, wenn es wieder steht.",
              "",
              "&eTipp:&r Ein Crusher macht aus Rohem Iesnium Staub: der Djinni drei, der Afrit vier pro Stück.",
          ],
          tasks=[task_item("occultism:iesnium_ingot", 12)],
          rewards=[reward_item("minecraft:netherrack", 32), reward_table("s3_common")],
          deps=["infused_pickaxe", "goggles"], icon="occultism:iesnium_ingot", size=1.5, shape="square"),

    quest("iesnium_pick", 7.2, 0, "&6Schmied eine Iesnium Pickaxe",
          subtitle="Die Spitzhacke, die bleibt.",
          description=[
              "&e3 Iesniumbarren&r oben, &e2 Stöcke&r darunter, wie jede Spitzhacke.",
              "",
              "Sie baut Iesnium und andere Otherworld-Erze ab und hält lange. Du brauchst noch drei weitere für die Bergbau-Geister: Foliot, Djinni und Afrit Miner fressen je eine.",
          ],
          tasks=[task_item("occultism:iesnium_pickaxe", 1)],
          rewards=[reward_item("occultism:iesnium_ingot", 3)],
          deps=["iesnium"], icon="occultism:iesnium_pickaxe"),

    quest("foliot_miner", 9.6, 0, "&6Binde einen Foliot Miner",
          subtitle="Ein Geist in der Zauberlampe.",
          description=[
              "&5Pentakel:&r Eziveus' Spectral Compulsion.",
              "&6Schalen:&r eine &6Magic Lamp&r (5 Silber um einen Spirit Attuned Gem), eine &6Iesnium Pickaxe&r, ein &6Eisenbarren&r, &6Kies&r.",
              "&cOpfer:&r keins. Start mit dem Foliot-Buch.",
              "",
              "Der Foliot gräbt ziellos und bringt alles, was er findet. Er ist langsam, schont dafür die Lampe. Ohne Mineshaft tut er nichts, also gleich weiter.",
          ],
          tasks=[task_item("occultism:miner_foliot_unspecialized", 1)],
          rewards=[reward_item("occultism:silver_ingot", 5)],
          deps=["iesnium_pick"], icon="occultism:miner_foliot_unspecialized"),

    quest("mineshaft", 12, 0, "&6&lBau den Dimensional Mineshaft",
          subtitle="Geister graben für dich, ohne Lag.",
          description=[
              "&5Pentakel:&r Strigeor's Higher Binding, beide mit dem Djinni-Buch, kein Opfer.",
              "&6Mineshaft:&r &e4 Otherstone&r, Goldbarren, &6Iesniumblock&r, &bSpirit Attuned Crystal&r.",
              "&6Djinni Miner:&r Foliot Miner, Iesnium Pickaxe, Goldbarren, Lapis, Spirit Attuned Crystal.",
              "",
              "Die Lampe kommt in den Mineshaft, die Funde kommen unten heraus. Der Djinni sucht gezielt Erze und nutzt die Lampe schneller ab als der Foliot. Leer den Mineshaft mit einem Trichter, sonst wirft er Funde weg.",
          ],
          tasks=[task_item("occultism:dimensional_mineshaft", 1), task_item("occultism:miner_djinni_ores", 1)],
          rewards=[reward_item("occultism:iesnium_ingot", 3), reward_table("s3_common"), reward_xp(10)],
          deps=["foliot_miner"], icon="occultism:dimensional_mineshaft"),

    quest("storage", 6, -2.2, "&6Bau den Storage Actuator",
          subtitle="Ein Lager in einer eigenen Dimension.",
          description=[
              "&6Dimensional Matrix:&r &e3 Quarzblöcke&r, Enderperle in Strigeor's Higher Binding (Djinni-Buch).",
              "&6Storage Actuator Base:&r Otherstone Pedestal, &e2 Kupfer&r, Gold in Eziveus' Spectral Compulsion (Foliot-Buch).",
              "Die Matrix über die Basis an der Werkbank, fertig.",
              "",
              "Er fasst &e128 Itemsorten&r und &e256 000 Items&r, insgesamt. Rohre und Trichter arbeiten mit ihm wie mit einer Shulkerkiste. Abgebaut behält er alles.",
              "",
              "&eTipp:&r Zum Herausholen nimm einen Foliot Transporter statt eines Filterrohrs, das schont den Server.",
          ],
          tasks=[task_item("occultism:storage_controller", 1)],
          rewards=[reward_item("minecraft:quartz_block", 8), reward_xp(5)],
          deps=["goggles"], icon="occultism:storage_controller", optional=True),

    quest("stabilizers", 8.4, -2.2, "&6Bau Speicherstabilisatoren",
          subtitle="Mehr Platz im Lager.",
          description=[
              "&6Stufe 1:&r Pedestal-Stabilisator, Kupferblock, Lohenstaub, Spirit Attuned Gem (Eziveus). &6Stufe 2:&r Stufe 1, Silberblock, Ghast-Träne, 2 Gems (Strigeor).",
              "&6Stufe 3:&r Stufe 2, Goldblock, Totem der Unsterblichkeit, Spirit Attuned Crystal, Afrit-Essenz (Sevira's Permanent Confinement).",
              "Sie zeigen auf die Matrix, höchstens &e5 Blöcke&r entfernt, in gerader Linie.",
              "",
              "Jeder Stabilisator legt drauf: Stufe 1 &e64 Sorten&r und 512 000 Items, Stufe 2 &e128&r und 1 024 000, Stufe 3 &e256&r und 2 048 000. Stufe 4 bindest du mit einem Marid (Uphyxes Inverted Tower).",
          ],
          tasks=[task_item("occultism:storage_stabilizer_tier2", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 2)],
          deps=["storage"], icon="occultism:storage_stabilizer_tier2", optional=True),

    # ---- Afrit-Essenz ------------------------------------------------------------------
    quest("possessed_bee", 0, 3.2, "&5Ruf eine Possessed Bee",
          subtitle="Der einzige Weg zu Cursed Honey.",
          description=[
              "&5Pentakel:&r Ihagan's Enthrallment.",
              "&6Schalen:&r &6Honigwabe&r, &6Honigblock&r, &6Honigflasche&r, &6Honigwabenblock&r.",
              "&cOpfer:&r ein &6Huhn&r. Start mit dem Djinni-Buch.",
              "",
              "Die Biene vergiftet immer, sticht schneller und ruft Verstärkung. Komm mit Rüstung. Besiegt lässt sie &6Cursed Honey&r fallen, die Zutat der orangen Kreide.",
          ],
          tasks=[task_item("occultism:cursed_honey", 3)],
          rewards=[reward_item("minecraft:honey_bottle", 4)],
          deps=["afrit_book"], icon="occultism:cursed_honey"),

    quest("orange_chalk", 2.4, 3.2, "&6Misch orange Kreide",
          subtitle="Ein süßer Köder für Afrit.",
          description=[
              "&6Impure White Chalk&r, &6Cursed Honey&r, &6Leuchtbeeren&r und &6Lohenstaub&r formlos, dann in Spiritfire.",
              "",
              "Afrit lassen sich von Limette beeindrucken, folgen ihr aber nicht. Orange lockt sie. Das nächste Pentakel braucht &e40 orange Zeichen&r, mach gleich drei Stück Kreide.",
          ],
          tasks=[task_item("occultism:chalk_orange", 3)],
          rewards=[reward_item("minecraft:glow_berries", 16)],
          deps=["possessed_bee"], icon="occultism:chalk_orange"),

    quest("kandar", 4.8, 3.2, "&5Zeichne Kandar's Opened Conjure",
          subtitle="Ein absichtlich offenes Pentakel.",
          description=[
              "&5Kandar's Opened Conjure&r, 17x17: &e40 orange&r, &e36 limettengrüne&r, &e16 Fundament&r (Weiß, Hellgrau, Grau, Schwarz) und &e8 dunkle&r Zeichen (Grau oder Schwarz), &e8 Skelettschädel&r, &e8 Kerzen&r.",
              "&7Gray Chalk&r ist unreine weiße Kreide mit Gray Paste, in Spiritfire gereinigt.",
              "",
              "Es ruft einen Afrit ohne rote Kreide, kann ihn aber nicht kontrollieren. Er kommt nur, um zu kämpfen. Lass das Pentakel stehen, du brauchst es hunderte Male.",
          ],
          tasks=[task_checkmark("Kandar's Opened Conjure gezeichnet")],
          rewards=[reward_item("occultism:large_candle", 8), reward_xp(5)],
          deps=["orange_chalk"], icon="minecraft:skeleton_skull"),

    quest("unbound_afrit", 7.2, 3.2, "&c&lBesieg einen Unbound Afrit",
          subtitle="Ruf ihn, schlag ihn, nimm seine Essenz.",
          description=[
              "&5Pentakel:&r Kandar's Opened Conjure.",
              "&6Schalen:&r &6Netherrack&r, ein &6Iesniumbarren&r, ein &6Feuerzeug&r, &6Schwarzpulver&r.",
              "&cOpfer:&r eine &6Kuh&r. Start mit dem Afrit-Buch, 150 Sekunden.",
              "",
              pic("occultism:afrit_essence"),
              "",
              "Der Afrit ist ein wütender Feuergeist. &eFeuerresistenz&r, gute Rüstung und Freunde helfen. Besiegt lässt er eine &cAfrit-Essenz&r fallen, mit Plünderung III bis zu drei mehr.",
          ],
          tasks=[task_item("occultism:afrit_essence", 1)],
          rewards=[reward_item("minecraft:magma_cream", 4), reward_table("s3_uncommon")],
          deps=["kandar", "iesnium"], icon="occultism:afrit_essence", size=1.75, shape="diamond"),

    quest("essence_line", 7.2, 5, "&cLiefer Afrit-Essenz an den Obelisken",
          subtitle="Hundertfünfzig Essenzen für den Server.",
          description=[
              "Bring &e16 Afrit-Essenzen&r zusammen. Pro Ruf: eine Kuh, ein Iesniumbarren, Netherrack, Feuerzeug, Schwarzpulver.",
              "Abgabe am &6Obelisken&r an der Spawn, per Rechtsklick oder über eine Truhe daneben.",
              "",
              "&eKronwerke:&r Das Ziel will &e150 Essenzen&r (die Menge passt sich der Spielerzahl an), jede 10 Punkte. Die acht Elfensterne brauchen weitere 16.",
              "",
              "&eWas hilft:&r eine Kuhfarm neben dem Pentakel, eine Waffe mit Plünderung III, ein Afrit Crusher für mehr Iesnium, und Leute, die sich beim Kämpfen abwechseln.",
          ],
          tasks=[task_item("occultism:afrit_essence", 16)],
          rewards=[reward_item("occultism:iesnium_ingot", 8), reward_table("s3_uncommon")],
          deps=["unbound_afrit"], icon="occultism:afrit_essence"),

    quest("odus", 4.8, 5, "&5Zeichne Odus' Open Convocation",
          subtitle="Afrit-Besessenheit ohne rote Kreide.",
          description=[
              "&5Odus' Open Convocation&r, 17x17: &e24 gelbe&r, &e12 limettengrüne&r, &e8 orange&r, &e8 dunkle&r und &e4 weiße&r Zeichen, &e8 Schädel&r, &e8 Kerzen&r, &e4 Spirit Attuned Crystals&r.",
              "&6Zombifizierter Piglin:&r Vergoldeter Schwarzstein, Wirrpilz, Karmesinpilz, Netherquarz, &cOpfer:&r Schwein. Afrit-Buch.",
              "&6Wächter:&r Tropenfisch, Seegras, Lapisblock, Schildkrötenschuppe, Wassereimer, &cOpfer:&r ein Fisch.",
              "",
              "Der Piglin lässt &6Demonic Meat&r fallen. Gegessen gibt es Feuerresistenz, drei davon machen rosa Kreide für Osorin's Unbound Calling.",
          ],
          tasks=[task_item("occultism:demonic_meat", 3)],
          rewards=[reward_item("minecraft:porkchop", 8), reward_xp(5)],
          deps=["kandar"], icon="occultism:demonic_meat"),

    # ---- Gebundene Afrit -------------------------------------------------------------------
    quest("red_chalk", 9.6, 3.2, "&cMisch rote Kreide",
          subtitle="Kreide aus der Essenz der Afrit selbst.",
          description=[
              "&6Impure White Chalk&r, eine &cAfrit-Essenz&r, eine &6Fackellilie&r und &6Redstone&r formlos, dann in Spiritfire.",
              "",
              "Fackellilien wachsen aus Samen, die der &eSchnüffler&r ausgräbt. Schnüffler-Eier gibt es in verdächtigem Sand der Warmen Ozeanruinen. Pflanz die Samen gleich an.",
              "",
              "Erst rote Kreide bindet einen Afrit, der für dich arbeitet.",
          ],
          tasks=[task_item("occultism:chalk_red", 2)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["unbound_afrit"], icon="occultism:chalk_red"),

    quest("abras", 12, 3.2, "&5Ruf einen Afrit Crusher",
          subtitle="Abras' Conjure: ein Erz, vier Staub.",
          description=[
              "&5Pentakel:&r Abras' Conjure, 17x17: Kandar's Kreis plus &e16 rote&r Zeichen und &e4 Spirit Attuned Crystals&r.",
              "&6Schalen:&r &6Iesnium-&r, &6Smaragd-&r, &6Lapis-&r, &6Amethyst-&r und &6Obsidianstaub&r.",
              "&cOpfer:&r keins. Start mit dem Afrit-Buch, 180 Sekunden.",
              "",
              "Er macht aus &eeinem Erz vier Staub&r und braucht nur halb so lange wie der Djinni. Iesnium-Erz gibt jetzt vier Barren statt einem.",
          ],
          tasks=[task_checkmark("Afrit Crusher beschworen")],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["red_chalk"], icon="occultism:book_of_binding_afrit"),

    quest("afrit_smelter", 14.4, 3.2, "&5Ruf einen Afrit Smelter",
          subtitle="Schmelzen in einem Zehntel der Zeit.",
          description=[
              "&5Pentakel:&r Abras' Conjure.",
              "&6Schalen:&r &6Lohenrute&r, &6Lavaeimer&r, &6Magmablock&r, &6rote Netherziegel&r, &6Seelenlagerfeuer&r.",
              "&cOpfer:&r keins. Start mit dem Afrit-Buch, 180 Sekunden.",
              "",
              "Er schmilzt alles in einem Zehntel der Ofenzeit, ohne Brennstoff. Im selben Pentakel: der &dAfrit Crystallizer&r (Gray Paste, Lapisblock, Amethystblock, Quarzblock, Tropfsteinblock), der zerkleinerte Blöcke wieder zusammensetzt.",
          ],
          tasks=[task_checkmark("Afrit Smelter beschworen")],
          rewards=[reward_item("minecraft:magma_block", 8), reward_xp(5)],
          deps=["abras"], icon="minecraft:magma_block"),

    quest("afrit_weather", 14.4, 4.8, "&5Ruf Regen oder Gewitter",
          subtitle="Afrit machen Wetter.",
          description=[
              "&5Pentakel:&r Abras' Conjure, beide mit dem Afrit-Buch und einer &6Kuh&r als Opfer, 90 Sekunden.",
              "&6Regen:&r Sand, getrockneter Seetang, Kaktus, toter Busch.",
              "&6Gewitter:&r Knochen, &e2 Schwarzpulver&r, Ghast-Träne.",
              "",
              "Der Geist ändert das Wetter einmal und verschwindet. Gewitter braucht ihr für geladene Creeper und manche Mobfarmen. Sagt vorher im Chat Bescheid.",
          ],
          tasks=[task_checkmark("Regen oder Gewitter gerufen")],
          rewards=[reward_item("minecraft:lightning_rod", 2)],
          deps=["abras"], icon="minecraft:lightning_rod", optional=True),

    quest("posuc", 12, 5, "&5Zeichne Posuc's Convocation",
          subtitle="Afrit in Wächtern, Hoglins und Wardens.",
          description=[
              "&5Posuc's Convocation&r: Odus' Kreis plus &e8 rote&r Zeichen. Alles mit dem Afrit-Buch.",
              "&6Warden:&r &e6 Sculk&r, &cOpfer:&r Kuh. Lässt mindestens &e6 Echosplitter&r fallen. &6Hoglin:&r Netheritschrott, Leder, 2 Netherrack, 3 Schweinefleisch, Crystal, Opfer Schwein.",
              "&6Großer Wächter:&r 2 Prismarinziegel, 2 dunkler Prismarin, Seelaterne, Wassereimer, Smaragd, Opfer Fisch. &6Guardian-Vertrauter:&r 4 Diamanten, 2 Goldäpfel, Opfer Dorfbewohner.",
              "",
              "Der Guardian-Vertraute opfert ein Glied, wenn du sterben würdest. Der besessene Shulker braucht Drachenatem und kommt in Stufe 4.",
          ],
          tasks=[task_item("minecraft:echo_shard", 6)],
          rewards=[reward_item("minecraft:sculk", 12), reward_xp(5)],
          deps=["abras"], icon="minecraft:echo_shard", optional=True),

    quest("sevira", 12, 1.6, "&5Zeichne Sevira's Permanent Confinement",
          subtitle="Das Pentakel für Afrit-Gegenstände.",
          description=[
              "&5Sevira's Permanent Confinement&r, 17x17: &e60 violette&r, &e20 limettengrüne&r, &e16 orange&r, &e12 rote&r, &e8 Fundament-&r und &e8 dunkle Zeichen, &e8 Crystals&r, &e8 Schädel&r, &e8 Kerzen&r.",
              "Gestartet wird mit dem Afrit-Buch, 300 Sekunden pro Ritual.",
              "",
              "&eWas es macht:&r Afrit Miner, Artisanal Satchel, Stabilisator Stufe 3, Witherite Dust, Iesnium-Ritualschale, Iesnium-Fleischermesser, Dimensional Battlefield. Mit &e3 Otherworld Essence&r und einem Gem repariert es Werkzeuge, Rüstung und Miner.",
          ],
          tasks=[task_checkmark("Sevira's Permanent Confinement gezeichnet")],
          rewards=[reward_item("occultism:spirit_attuned_crystal", 2), reward_xp(5)],
          deps=["red_chalk"], icon="occultism:chalk_red"),

    quest("afrit_miner", 14.4, 0, "&6Binde einen Afrit Miner",
          subtitle="Tiefer graben, mit weniger Verschleiß.",
          description=[
              "&5Pentakel:&r Sevira's Permanent Confinement.",
              "&6Schalen:&r &6Djinni Miner&r, &6Iesnium Pickaxe&r, &bSpirit Attuned Crystal&r, &cAfrit-Essenz&r, &6Echosplitter&r, &6Weinender Obsidian&r.",
              "&cOpfer:&r keins. Start mit dem Afrit-Buch.",
              "",
              "Er gräbt schneller, findet auch Tiefenschiefer-Erze und nutzt die Lampe langsamer ab. Echosplitter gibt der besessene Warden aus Posuc's Convocation, oder die Truhen der Antiken Städte.",
          ],
          tasks=[task_item("occultism:miner_afrit_deeps", 1)],
          rewards=[reward_item("minecraft:crying_obsidian", 4), reward_xp(10)],
          deps=["mineshaft", "sevira"], icon="occultism:miner_afrit_deeps"),

    quest("satchel", 16.8, 1.6, "&6Binde die Artisanal Ritual Satchel",
          subtitle="Ein ganzes Pentakel mit einem Klick.",
          description=[
              "&5Pentakel:&r Sevira's Permanent Confinement.",
              "&6Schalen:&r deine &6Apprentice Ritual Satchel&r, eine &cAfrit-Essenz&r, &e4 Enderperlen&r. Der Inhalt bleibt erhalten.",
              "&cOpfer:&r keins. Start mit dem Afrit-Buch, 180 Sekunden.",
              "",
              "Liegen alle Kreiden, Kerzen, Crystals und Schädel darin, zeichnet der Afrit das ganze Pentakel auf einmal. Rechtsklick auf die goldene Schale eines fertigen Pentakels räumt alles wieder ein. Für die vielen Kandar-Rufe spart das jedes Mal Minuten.",
          ],
          tasks=[task_item("occultism:ritual_satchel_t2", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["sevira"], icon="occultism:ritual_satchel_t2", optional=True),

    # ---- Wilde Geister ----------------------------------------------------------------
    quest("osorin", 4.8, 6.8, "&5Zeichne Osorin's Unbound Calling",
          subtitle="Kein Schutz, nur Ruf.",
          description=[
              "&5Osorin's Unbound Calling&r, 13x13: &e16 rosa&r, &e16 hellblaue&r und &e16 grüne&r Zeichen, keine Kerzen, keine Schädel.",
              "&6Rosa:&r unreine Kreide, 3 Demonic Meat. &6Hellblau:&r unreine Kreide, Eis-, Packeis- und Blaueisstaub (Djinni Crusher). &6Grün:&r unreine Kreide, Nature Paste.",
              "",
              "Wilde Geister brauchen kein Bindungsbuch, das Startitem ist je Ritual ein anderes. &eWilde Jagd&r: Kupfer-, Silber-, Goldblock, Diamant, Netherrack, Seelensand, Start Skelettschädel, Opfer Dorfbewohner. Sie bringt Witherskelettschädel.",
              "",
              "Dazu Horden (Husk, Ertrunkener, geladener Creeper, Silberfisch), Breeze, Illager mit Totem, Bienennest, Glocke, Knospender Amethyst und Pferderüstungen.",
          ],
          tasks=[task_checkmark("Osorin's Unbound Calling gezeichnet")],
          rewards=[reward_item("minecraft:blue_ice", 8), reward_xp(5)],
          deps=["odus"], icon="minecraft:blue_ice", optional=True),

    quest("reinforced_deepslate", 7.2, 6.8, "&8Mach Verstärkten Tiefenschiefer",
          subtitle="Zwei Wege zum Rahmen der Otherside.",
          description=[
              "&eRezept auf Kronwerke:&r &e4 Tiefenschiefer&r, &e4 Stahlbarren&r und ein &6Echosplitter&r ergeben &e2&r Verstärkten Tiefenschiefer.",
              "&5Ritual:&r Osorin's Unbound Calling, Schalen &e4 Eisengitter&r, &e4 Obsidian&r, &e1 Iesniumbarren&r, Start mit &6Tiefenschiefer&r, &cOpfer:&r ein &6Warden&r. Ein Block pro Ritual.",
              "",
              "Ein besessener Warden aus Posuc's Convocation zählt als Opfer. Das Ritual lohnt sich trotzdem nur, wenn ihr keinen Stahl habt. Der Block rahmt das Portal zur Otherside, siehe Kapitel &5Deeper and Darker&r.",
          ],
          tasks=[task_item("minecraft:reinforced_deepslate", 4)],
          rewards=[reward_item("minecraft:echo_shard", 2), reward_xp(5)],
          deps=["osorin"], icon="minecraft:reinforced_deepslate"),

    # ---- Marid ---------------------------------------------------------------------------
    quest("black_chalk", 9.6, 6.8, "&8Misch schwarze Kreide",
          subtitle="Das härteste Fundament.",
          description=[
              "&5Sevira's Permanent Confinement&r: &6Netheritstaub&r, &6Witherskelettschädel&r, &6Schwarzsteinstaub&r, &6Wither-Rose&r ergeben &e3 Witherite Dust&r (Afrit-Buch).",
              "&6Impure White Chalk&r mit &e3 Witherite Dust&r, dann in Spiritfire.",
              "",
              "Netherit- und Schwarzsteinstaub macht dein Crusher. Wither-Rosen wachsen, wo der Wither etwas getötet hat. Schwarz zählt überall als Fundament.",
          ],
          tasks=[task_item("occultism:chalk_black", 1)],
          rewards=[reward_item("minecraft:wither_rose", 2), reward_xp(5)],
          deps=["red_chalk"], icon="occultism:chalk_black"),

    quest("unbound_marid", 12, 6.8, "&9&lBesieg einen Unbound Marid",
          subtitle="Der stärkste Geist, den du rufen kannst.",
          description=[
              "&5Pentakel:&r Tibira's Attraction: Abras' Kreis plus &e8 schwarze&r Zeichen und &e4 Witherskelettschädel&r.",
              "&6Schalen:&r &6Aquisitor&r, &6Prismarinkristalle&r, &6Prismarinscherbe&r, &6Ghast-Träne&r. Marid-Buch (&e4 grüner Farbstoff&r).",
              "&cStart:&r bei grauen Partikeln einen &6Dreizack&r auf der goldenen Schale benutzen. 210 Sekunden.",
              "",
              "Der Marid kommt aggressiv. Ruft ihn zu mehreren. Besiegt lässt er &9Marid-Essenz&r fallen, mit Plünderung mehr.",
          ],
          tasks=[task_item("occultism:marid_essence", 1)],
          rewards=[reward_item("minecraft:prismarine_crystals", 16), reward_table("s3_uncommon")],
          deps=["black_chalk"], icon="occultism:marid_essence"),

    quest("marid_crusher", 14.4, 6.8, "&9Ruf einen Marid Crusher",
          subtitle="Fatma's Incentivized Attraction: ein Erz, sechs Staub.",
          description=[
              "&9Blue Chalk:&r unreine Kreide, Marid-Essenz, Lapisstaub, Röhrenkoralle. &5Fatma's Incentivized Attraction&r, 21x21: &e60 blaue&r, 40 orange, 36 Limette, 16 rot, 16 Fundament, 8 schwarz, 8 Crystals, 8 Schädel, 4 Witherschädel, 8 Kerzen.",
              "&6Schalen:&r &6Diamant-&r, &6Iesnium-&r, &6Smaragd-&r und &6Netheritblock&r, &6Ghast-Träne&r. Marid-Buch, 240 Sekunden, kein Opfer.",
              "",
              "Er macht aus &eeinem Erz sechs Staub&r und braucht nur 30 Prozent der Djinni-Zeit. Der Marid Crystallizer (Gray Paste, Iesniumblock, Knospender Amethyst, Seelaterne, Sculk-Katalysator) wandelt sogar Obsidian in Weinenden Obsidian.",
          ],
          tasks=[task_item("occultism:chalk_blue", 1)],
          rewards=[reward_item("minecraft:raw_gold", 32), reward_xp(10)],
          deps=["unbound_marid"], icon="occultism:chalk_blue"),

    quest("master", 17, 6.8, "&9&lWerd Meister der Anderswelt",
          subtitle="Afrit arbeiten für dich, Marid hören auf deinen Namen.",
          description=[
              "Halte &e8 Afrit-Essenzen&r und eine &9Blue Chalk&r bereit. Damit bist du durch alles, was Stufe 3 bei Occultism bietet.",
              "",
              "&5Uphyxes Inverted Tower&r (21x21, 88 violette Zeichen) bindet Marid in Gegenstände: den Stabilisator Stufe 4 und den Iesnium-Amboss, der nie kaputtgeht und die Hälfte der Stufen zahlt. In &5Xeovrenth Adjure&r wird ein Iesnium-Golem gerufen.",
              "",
              "&cStufe 4:&r Marid Smelter, Marid Miner, Drachenstaub, besessener Shulker und Ronaza's Contact brauchen Drachenatem und das End.",
              "",
              "&eKronwerke:&r Bis dahin zählt jede Afrit-Essenz für den Obelisken.",
          ],
          tasks=[task_item("occultism:chalk_blue", 1), task_item("occultism:afrit_essence", 8)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["marid_crusher", "afrit_smelter"], icon="occultism:chalk_blue", size=2.5, shape="gear"),
]

images = [
    banner("occultism_afrit/title", "Occultism: Afrit und Marid", 7.8, -4.8, height=1.8, kind="title", colour="fire"),
    banner("occultism_afrit/iesnium", "Iesnium und Bergbau", 9.6, -3.3, height=0.8, colour="magic"),
    banner("occultism_afrit/essenz", "Afrit-Essenz", 3.6, 1.6, height=0.8, colour="fire"),
    banner("occultism_afrit/gebunden", "Gebundene Afrit", 16.8, -1.0, height=0.8, colour="fire"),
    banner("occultism_afrit/wild", "Wilde Geister", 2.0, 8.4, height=0.8, colour="nature"),
    banner("occultism_afrit/marid", "Marid", 12, 8.4, height=0.8, colour="water"),
]

chapter(C, "Occultism: Afrit und Marid", "occultism:afrit_essence", "magic", quests, shape="circle", order=26,
        stage=3, subtitle=["Stufe 3. Iesnium, Afrit-Essenz, gebundene Afrit und die Marid."], images=images)
