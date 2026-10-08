"""Mystical Agriculture in stage 1: inferium essence and prosperity shards, inferium seeds and
essence farmland, the growth accelerator, watering cans and mystical fertilizer, the infusion
altar with its eight pedestals, the first resource seeds (tier 1 and the four elemental ones),
essence tools and what Mystical Agradditions adds at the inferium tier. Prudentium opens in
stage 2, tertium in 3, imperium and the awakening altar in 4, supremium in 5; those are only
named. Resource crops ignore bone meal, that is the mod's own rule and nothing in the pack
overrides it. Numbers come from the mod jar and mysticalagriculture-common.toml."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "mystical_agriculture"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


# Every resource seed whose infusion recipe needs only inferium essence: the tier 1 crops and
# the four elemental crops. Everything from coal upwards needs prudentium essence (stage 2).
# (quest name, seed id, German crop name, material text, reward item, reward count)
SEEDS = [
    ("seed_stone", "mysticalagriculture:stone_seeds", "Stein",
     "Material: &e4 Stein&r (geschmolzen, kein Bruchstein).", "minecraft:stone", 32),
    ("seed_deepslate", "mysticalagriculture:deepslate_seeds", "Tiefenschiefer",
     "Material: &e4 Tiefenschiefer&r (geschmolzen aus Bruchtiefenschiefer).", "minecraft:deepslate", 32),
    ("seed_dirt", "mysticalagriculture:dirt_seeds", "Erde",
     "Material: &e4 Erde&r.", "minecraft:dirt", 32),
    ("seed_earth", "mysticalagriculture:earth_seeds", "Erde (Element)",
     "Material: &e4 Erd-Agglomerat&r (Gras, Kies, Erde, Ton).", "minecraft:clay_ball", 16),
    ("seed_wood", "mysticalagriculture:wood_seeds", "Holz",
     "Material: &e4 Stämme&r, jede Holzart.", "minecraft:oak_log", 16),
    ("seed_fire", "mysticalagriculture:fire_seeds", "Feuer",
     "Material: &e4 Feuer-Agglomerat&r (Lavaeimer, Kies, Erde, Ton).", "minecraft:lava_bucket", 1),
    ("seed_ice", "mysticalagriculture:ice_seeds", "Eis",
     "Material: &e4 Eis&r, mit Behutsamkeit aus einem kalten Biom.", "minecraft:ice", 16),
    ("seed_water", "mysticalagriculture:water_seeds", "Wasser",
     "Material: &e4 Wasser-Agglomerat&r (Wassereimer, Kies, Erde, Ton).", "minecraft:bucket", 2),
    ("seed_inferium", "mysticalagriculture:inferium_seeds", "Inferium",
     "Kein Altar: &e8 Inferiumessenz&r um ein Weizenkorn an der Werkbank.", "mysticalagriculture:inferium_essence", 8),
    ("seed_air", "mysticalagriculture:air_seeds", "Luft",
     "Material: &e4 Luft-Agglomerat&r (Glasflasche, Kies, Erde, Ton).", "minecraft:glass_bottle", 8),
]


def seed_quest(i, name, seed_id, crop, material, reward, count):
    """Two columns of five: the left column hangs on the header, the right on its row neighbour."""
    row, col = divmod(i, 2)
    deps = ["all_seeds"] if col == 0 else [SEEDS[i - 1][0]]
    return quest(name, 27.5 + 2.5 * col, -3 + 2 * row, f"Samen: {crop}",
                 subtitle="Ein Samen, ein Haken.",
                 description=[
                     material,
                     "",
                     "Dazu &e4 Inferiumessenz&r und eine &6Prosperiumsamenbasis&r im Infusionsaltar." if name != "seed_inferium"
                     else "Inferiumsamen wachsen auf jedem Ackerland. Auf Inferium-Ackerland gibt es eine Chance auf einen zweiten Samen.",
                 ],
                 tasks=[task_item(seed_id, 1)],
                 rewards=[reward_item(reward, count), reward_xp(2)],
                 deps=deps, icon=seed_id)


quests = [
    # ---- Inferium ------------------------------------------------------------
    quest("welcome", 0, 1, "&a&lSammle Inferiumessenz",
          subtitle="Die Essenz, aus der dieser Mod gemacht ist.",
          description=[
              "&aMystical Agriculture&r lässt dich Rohstoffe anbauen: Stein, Erde, Holz, später Erze und sogar Monster. Alles beginnt mit &6Inferiumessenz&r. Du bekommst sie auf drei Wegen: aus &6Inferiumerz&r, von Mobs und vom Feld.",
              "",
              pic("mysticalagriculture:inferium_essence"),
              "",
              "&eErz:&r Inferiumerz liegt zwischen &eY -32 und 64&r, bis zu 16 Adern pro Chunk, und wirft direkt &e2 bis 4 Essenz&r ab. Glück zählt. &eMobs:&r Jedes Tier und jedes Monster lässt mit &e20 Prozent&r Chance eine Essenz fallen.",
              "",
              "&eWas in Stufe 1 offen ist:&r alles mit Inferium: Samen, Ackerland, Wachstumsbeschleuniger, Infusionsaltar, Gießkanne, Werkzeug und die Samen der ersten Stufe. &cPrudentium&r und alles darüber kommt mit den späteren Stufen.",
              "",
              "&eTipp:&r Ein Buch und eine Essenz ergeben den &6Guide&r des Mods, mit jedem Rezept zum Nachschlagen.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_essence", 8)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 8), reward_table("s1_common")],
          icon="mysticalagriculture:inferium_essence", size=2.0, shape="hexagon"),

    quest("inferium_seeds", 2.5, 0, "&aPflanze Inferiumsamen",
          subtitle="Essenz, die nachwächst.",
          description=[
              "&e8 Inferiumessenz&r rund um ein &6Weizenkorn&r ergeben &6Inferiumsamen&r. Pflanz sie auf Ackerland wie Weizen, jede Ernte gibt &e1 Essenz&r und den Samen zurück.",
              "",
              "Fang mit vier Samen an und pflanz jede Essenz wieder ein, bis das Feld voll ist. 8 Essenz sind ein Samen, also lohnt es sich, früh anzufangen und erst später zu ernten.",
              "",
              "&cAchtung:&r &6Knochenmehl wirkt nicht&r auf Inferium und auf keiner anderen Essenzpflanze. Das ist eine Regel des Mods, und auf Kronwerke gilt sie ohne Ausnahme. Was stattdessen hilft, steht beim Mystischen Dünger.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_seeds", 4)],
          rewards=[reward_item("minecraft:wheat_seeds", 8), reward_item("mysticalagriculture:inferium_essence", 8)],
          deps=["welcome"], icon="mysticalagriculture:inferium_seeds"),

    quest("farmland", 2.5, 2, "&aMach Inferium-Ackerland",
          subtitle="Der Boden entscheidet über den zweiten Samen.",
          description=[
              "&6Rechtsklick&r mit einer &6Inferiumessenz&r auf normales Ackerland macht daraus &6Inferium-Ackerland&r. Oder: Essenz und Ackerland formlos an der Werkbank, oder Hacke, Essenz und Erde.",
              "",
              "Auf gewöhnlichem Ackerland lässt eine Essenzpflanze nie einen zweiten Samen fallen. Auf Essenz-Ackerland gibt es &e10 Prozent&r Chance, auf dem passenden Ackerland der eigenen Stufe noch einmal &e10 Prozent&r dazu. Für alles in diesem Kapitel heißt das: &e20 Prozent&r auf Inferium-Ackerland.",
              "",
              "Mehr Essenz pro Ernte bringt erst höheres Ackerland, und das kommt mit &cStufe 2&r.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_farmland", 9)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 12), reward_xp(3)],
          deps=["inferium_seeds"], icon="mysticalagriculture:inferium_farmland"),

    quest("fertilizer", 5, 0, "&eStell Mystischen Dünger her",
          subtitle="Der Ersatz für Knochenmehl.",
          description=[
              "&e4 Knochenmehl&r, &e4 Inferiumessenz&r und &e1 Diamant&r in der Mitte ergeben &e4 Mystischen Dünger&r. Er lässt jede Pflanze &esofort&r auswachsen, auch Essenzpflanzen und Setzlinge.",
              "",
              pic("mysticalagriculture:mystical_fertilizer"),
              "",
              "Jede Essenzpflanze außer Inferium lässt beim Ernten mit &e10 Prozent&r eine &6Düngeressenz&r fallen. Die wirkt wie Knochenmehl, nur eben auch auf Essenzpflanzen, und mit 4 Düngeressenz statt Knochenmehl ergibt das Rezept &e8 Dünger&r statt 4.",
              "",
              "&eTipp:&r Dünger ist für den Start einer neuen Sorte gedacht, nicht für den Dauerbetrieb. Für das Feld nimmst du Wachstumsbeschleuniger und Gießkanne.",
          ],
          tasks=[task_item("mysticalagriculture:mystical_fertilizer", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_item("mysticalagriculture:inferium_essence", 8)],
          deps=["inferium_seeds"], icon="mysticalagriculture:mystical_fertilizer"),

    quest("watering_can", 5, 2, "&bBau eine Gießkanne",
          subtitle="Wachstum per Hand, drei mal drei Felder.",
          description=[
              "&e4 Eisenbarren&r, eine &6Schüssel&r in der Mitte und ein &6Knochenmehl&r oben in der Mitte ergeben die &6Gießkanne&r. Fülle sie mit Rechtsklick auf Wasser.",
              "",
              pic("mysticalagriculture:watering_can"),
              "",
              "Halt die rechte Maustaste über dem Feld gedrückt: Die Kanne gießt &e3 mal 3&r Felder und gibt jeder Pflanze darin bei jedem Tick eine &e25 Prozent&r Chance auf einen Wachstumsschub. Das wirkt auch auf Essenzpflanzen, anders als Knochenmehl.",
              "",
              "Das Wasser geht nie aus, nur deine Geduld. Die Inferium-Gießkanne im Abschnitt Prosperium gießt größer und kann von allein laufen.",
          ],
          tasks=[task_item("mysticalagriculture:watering_can", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["farmland"], icon="mysticalagriculture:watering_can"),

    # ---- Prosperium ----------------------------------------------------------
    quest("prosperity", 0, 7, "&fGrab Prosperiumsplitter aus",
          subtitle="Das zweite Grundmaterial.",
          description=[
              "&6Prosperiumerz&r liegt tief, zwischen &eY -60 und 24&r, bis zu 12 Adern pro Chunk. Es wirft &e1 bis 4 Prosperiumsplitter&r ab, mit Glück mehr.",
              "",
              pic("mysticalagriculture:prosperity_shard"),
              "",
              "Splitter stecken in allem, was nicht Essenz ist: in der Samenbasis für den Altar, im Infusionskristall, in Barren und Edelsteinen für Werkzeug und Wachstumsbeschleuniger. Ein Stapel reicht für dieses Kapitel locker.",
          ],
          tasks=[task_item("mysticalagriculture:prosperity_shard", 16)],
          rewards=[reward_item("mysticalagriculture:prosperity_shard", 16), reward_table("s1_common")],
          deps=["welcome"], icon="mysticalagriculture:prosperity_shard"),

    quest("prosperity_ingot", 2.5, 6, "&fFass Eisen in Prosperium",
          subtitle="Ein Barren mit vier Splittern drumherum.",
          description=[
              "Ein &6Eisenbarren&r mit &e4 Prosperiumsplittern&r an den vier Seiten ergibt einen &6Prosperiumbarren&r.",
              "",
              "Er ist die Vorstufe jedes Essenzbarrens. Mach gleich ein paar auf Vorrat: zwei stecken im ersten Werkzeug, vier in der Inferium-Gießkanne.",
          ],
          tasks=[task_item("mysticalagriculture:prosperity_ingot", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["prosperity"], icon="mysticalagriculture:prosperity_ingot"),

    quest("inferium_ingot", 5, 6, "&aVeredle zu Inferiumbarren",
          subtitle="Ein Prosperiumbarren schluckt zwei Essenz.",
          description=[
              "Ein &6Prosperiumbarren&r und &e2 Inferiumessenz&r formlos an der Werkbank ergeben einen &6Inferiumbarren&r.",
              "",
              pic("mysticalagriculture:inferium_ingot"),
              "",
              "Inferiumbarren sitzen links und rechts in jedem Inferiumwerkzeug und in jeder Rüstung, und sie reparieren das Werkzeug später im Amboss. Ein fertiges Inferiumwerkzeug wird in &cStufe 2&r mit Prudentiumbarren und Prudentium-Edelsteinen weiter aufgerüstet und behält dabei seine Verzauberungen.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_ingot", 4)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 16), reward_xp(3)],
          deps=["prosperity_ingot"], icon="mysticalagriculture:inferium_ingot"),

    quest("inferium_gemstone", 2.5, 8, "&bSchleif Inferium-Edelsteine",
          subtitle="Ein Diamant, vier Splitter, zwei Essenz.",
          description=[
              "Ein &6Diamant&r mit &e4 Prosperiumsplittern&r ergibt einen &6Prosperium-Edelstein&r. Der wird mit &e2 Inferiumessenz&r formlos zum &6Inferium-Edelstein&r.",
              "",
              pic("mysticalagriculture:inferium_gemstone"),
              "",
              "Edelsteine sitzen oben und unten in jedem Inferiumwerkzeug und in der Mitte jedes Wachstumsbeschleuniger-Rezepts. Drei Diamanten reichen für den Anfang: zwei für das erste Werkzeug, einer für drei Beschleuniger.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_gemstone", 2)],
          rewards=[reward_item("minecraft:diamond", 1), reward_item("mysticalagriculture:prosperity_shard", 8)],
          deps=["prosperity"], icon="mysticalagriculture:inferium_gemstone"),

    quest("accelerator", 5, 8, "&aLeg Wachstumsbeschleuniger unter das Feld",
          subtitle="Alle zehn Sekunden ein Wachstumstick, ohne dass du dabei bist.",
          description=[
              "&eRezept auf Kronwerke:&r &e4 Inferiumessenz&r in die Ecken, &e4 Andesitlegierungen&r an die Seiten und ein &6Inferium-Edelstein&r in die Mitte ergeben &e3 Inferium-Wachstumsbeschleuniger&r.",
              "",
              "Ein Beschleuniger gibt der &eersten Pflanze über sich&r alle &e10 Sekunden&r einen zufälligen Wachstumstick. Der Inferium-Beschleuniger reicht &e9 Blöcke&r nach oben, und du kannst beliebig viele übereinander stapeln: unter jedem Feldblock eine Säule aus Beschleunigern, und jeder zählt.",
              "",
              "&eSo baust du:&r Ackerland, darunter die Beschleuniger. Ein Beschleuniger darf auf einem anderen stehen, alle in der Säule wirken auf dieselbe Pflanze. Vier bis sechs pro Feld sind ein guter Anfang, mehr geht immer.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_growth_accelerator", 9)],
          rewards=[reward_item("mysticalagriculture:inferium_growth_accelerator", 3), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["inferium_gemstone"], icon="mysticalagriculture:inferium_growth_accelerator", size=1.5, shape="hexagon"),

    quest("inferium_watering_can", 7.5, 8.5, "&bRüste die Gießkanne auf",
          subtitle="Fünf mal fünf, und sie gießt allein.",
          description=[
              "Die &6Gießkanne&r in die Mitte, &e4 Inferiumbarren&r links, rechts, oben und unten, &e4 Mystischen Dünger&r in die Ecken: fertig ist die &6Inferium-Gießkanne&r.",
              "",
              "Sie gießt &e5 mal 5&r Felder mit &e30 Prozent&r Chance pro Tick statt 25. Und sie kann &eautomatisch&r gießen: Shift und Rechtsklick in die Luft schaltet das um, dann gießt sie, solange du sie in der Hand hältst und auf das Feld schaust.",
              "",
              "&eTipp:&r Stell dich mit der Kanne in die Mitte eines 5 mal 5 Feldes und lass sie laufen, während du im Chat bist. Zusammen mit den Beschleunigern darunter ist das Feld in Minuten reif.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_watering_can", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 24), reward_xp(5)],
          deps=["inferium_ingot", "watering_can"], icon="mysticalagriculture:inferium_watering_can"),

    # ---- Infusionsaltar --------------------------------------------------------
    quest("altar", 10, 1, "&d&lBau den Infusionsaltar",
          subtitle="Hier entstehen alle Samen.",
          description=[
              "&e2 Quelljuwelen&r oben links und rechts, &e1 rote Wolle&r oben in der Mitte, darunter ein Stein in der Mitte und drei Steine in der unteren Reihe: der &6Infusionsaltar&r.",
              "",
              "Der Altar ist eine Mehrblockstruktur: ein Altar und &e8 Infusionssockel&r drumherum. Stell den Altar auf, dann zeigt er dir mit Markierungen, wo die Sockel hingehören: &e3 Blöcke&r entfernt in jede Himmelsrichtung und &e2 Blöcke&r entfernt in jede Diagonale. Alles auf einer Höhe.",
              "",
              "Jedes Samenrezept ist gleich aufgebaut: die Samenbasis in den Altar, auf die Sockel abwechselnd &e4 Essenz&r und &e4 Material&r. Dann aktivieren, mit dem Zauberstab oder einem Redstone-Signal.",
          ],
          tasks=[task_item("mysticalagriculture:infusion_altar", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_table("s1_common")],
          deps=["welcome"], icon="mysticalagriculture:infusion_altar", size=1.75, shape="hexagon"),

    quest("pedestals", 12.5, 0, "&dStell acht Sockel auf",
          subtitle="Zwei Goldbleche und ein Stück Wolle pro Sockel.",
          description=[
              "Ein &6Infusionssockel&r ist der Altar ohne Fuß: &e2 Goldbleche&r aus der Create-Presse, &e1 rote Wolle&r dazwischen, darunter &e2 Stein&r übereinander. Du brauchst &e8&r, also insgesamt 16 Goldbleche, 8 Wolle und 16 Stein.",
              "",
              "Ein Sockel nimmt genau einen Gegenstand, Rechtsklick legt hinein und holt wieder heraus. Für die Übersicht: Essenz auf die vier geraden Sockel, Material auf die vier schrägen, oder umgekehrt.",
              "",
              "&eTipp:&r Rote Wolle färbst du aus weißer Wolle mit rotem Farbstoff aus Mohn oder roten Blütenblättern von Botania.",
          ],
          tasks=[task_item("mysticalagriculture:infusion_pedestal", 8)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_item("minecraft:red_wool", 4)],
          deps=["altar"], icon="mysticalagriculture:infusion_pedestal"),

    quest("wand", 12.5, 2, "&dSchnitz einen Zauberstab",
          subtitle="Ein Klick, und der Altar arbeitet.",
          description=[
              "Eine &6Inferiumessenz&r oben rechts, ein &6Stock&r in der Mitte und ein &6Stein&r unten links ergeben den &6Zauberstab&r.",
              "",
              pic("mysticalagriculture:wand"),
              "",
              "Rechtsklick mit dem Stab auf den gefüllten Altar startet die Infusion. Die Sockel schicken ihre Gegenstände nacheinander in den Altar, und am Ende liegt der Samen darin. Ein Knopf oder Hebel am Altar tut dasselbe, der Stab ist aber praktischer.",
          ],
          tasks=[task_item("mysticalagriculture:wand", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 8)],
          deps=["altar"], icon="mysticalagriculture:wand"),

    quest("seed_base", 15, 0, "&fCrafte eine Samenbasis",
          subtitle="Ein Weizenkorn in Prosperium.",
          description=[
              "Ein &6Weizenkorn&r mit &e4 Prosperiumsplittern&r an den Seiten ergibt eine &6Prosperiumsamenbasis&r. Sie ist der Kern jedes Samens aus dem Altar.",
              "",
              pic("mysticalagriculture:prosperity_seed_base"),
              "",
              "Jeder Samen frisst eine Basis, also 4 Splitter. Mach einen kleinen Vorrat, dann musst du für die Checkliste am Ende des Kapitels nicht ständig zurück an die Werkbank.",
              "",
              "&cAusblick:&r Die &6Seelensamenbasis&r für Tier- und Monstersamen braucht Soulium, und das öffnet erst mit &cStufe 2&r.",
          ],
          tasks=[task_item("mysticalagriculture:prosperity_seed_base", 2)],
          rewards=[reward_item("mysticalagriculture:prosperity_shard", 8), reward_item("minecraft:wheat_seeds", 4)],
          deps=["pedestals"], icon="mysticalagriculture:prosperity_seed_base"),

    quest("first_seed", 17.5, 1, "&6&lInfundiere Steinsamen",
          subtitle="Dein erster Rohstoff vom Feld.",
          description=[
              "Die &6Prosperiumsamenbasis&r in den Altar. Auf die Sockel im Wechsel &e4 Inferiumessenz&r und &e4 Stein&r (geschmolzener Stein, kein Bruchstein). Zauberstab auf den Altar, fertig sind die &6Steinsamen&r.",
              "",
              "Steinsamen wachsen wie Weizen und geben &6Steinessenz&r. &e8 Steinessenz&r im Ring ergeben &e24 Bruchstein&r, 8 Steinessenz mit einer Kohleessenz in der Mitte 20 Stein, die kommt aber erst in Stufe 2.",
              "",
              "&eKronwerke:&r Das Steinziel am Obelisken verlangt &e20 000 Bruchstein&r. Ein Feld Steinsamen mit Beschleunigern darunter liefert ohne Spitzhacke mit, und jeder Bruchstein zählt.",
              "",
              "Alle Samen, die du jetzt schon bauen kannst, stehen in der &eCheckliste&r rechts.",
          ],
          tasks=[task_item("mysticalagriculture:stone_seeds", 1)],
          rewards=[reward_item("mysticalagriculture:stone_seeds", 1), reward_table("s1_uncommon"), reward_xp(10)],
          deps=["seed_base", "wand"], icon="mysticalagriculture:stone_seeds", size=2.0, shape="diamond"),

    quest("infusion_crystal", 20, 0, "&dSchleif einen Infusionskristall",
          subtitle="Das Werkzeug für die nächste Essenzstufe.",
          description=[
              "&e4 Prosperiumsplitter&r an die Seiten, &e4 Inferiumessenz&r in die Ecken und ein &6Diamant&r in die Mitte ergeben den &6Infusionskristall&r. Er hat &e1 000 Ladungen&r.",
              "",
              pic("mysticalagriculture:infusion_crystal"),
              "",
              "Der Kristall verdichtet Essenz: &e4 Inferiumessenz&r um den Kristall ergeben &e1 Prudentiumessenz&r, und so geht es Stufe für Stufe weiter. &cPrudentium&r ist aber bis &cStufe 2&r gesperrt, du kannst den Kristall jetzt bauen und dann sofort loslegen, sobald das Messingwerk öffnet.",
              "",
              "Der &6Meister-Infusionskristall&r ohne Verschleiß braucht Supremium und kommt ganz zum Schluss in Stufe 5.",
          ],
          tasks=[task_item("mysticalagriculture:infusion_crystal", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_essence", 16), reward_xp(5)],
          deps=["first_seed"], icon="mysticalagriculture:infusion_crystal"),

    quest("agglomeratio", 20, 2, "&bMisch die Agglomerate",
          subtitle="Luft, Erde, Wasser und Feuer in Lehm gepresst.",
          description=[
              "Ein &6Agglomerat&r ist ein Zwei-mal-zwei-Rezept: oben links das Element, oben rechts &6Kies&r, unten links &6Erde&r, unten rechts ein &6Tonklumpen&r. Als Element nimmst du eine &eGlasflasche&r (Luft), &eGras&r (Erde), einen &eWassereimer&r oder einen &eLavaeimer&r (Feuer).",
              "",
              "Vier Agglomerate einer Sorte sind das Material für den jeweiligen &eElementsamen&r im Altar, zusammen mit 4 Inferiumessenz. Wasser- und Feueressenz haben jetzt schon Rezepte, Luft und Erde sammelst du für den &6Erweckungsaltar&r in &cStufe 4&r.",
          ],
          tasks=[task_item("mysticalagriculture:water_agglomeratio", 4)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_item("minecraft:gravel", 16)],
          deps=["first_seed"], icon="mysticalagriculture:water_agglomeratio"),

    quest("essence_crafting", 22.5, 1, "&6Verarbeite Essenz zu Blöcken",
          subtitle="Was man aus den Samen der Stufe 1 bauen kann.",
          description=[
              "Jede Essenz hat ihre Rezepte an der Werkbank, der Guide und JEI zeigen sie alle. Die wichtigsten für Stufe 1:",
              "",
              img("mysticalagriculture:textures/item/essence/stone_essence.png", 32, 32),
              "",
              "&eSteinessenz:&r 8 im Ring ergeben 24 Bruchstein, 2 Stein- und 2 Erdessenz 16 Kies.",
              "&eErdessenz:&r 8 im Ring ergeben 24 Erde, 2 Erd- und 2 Wasseressenz 24 Ton.",
              "&eHolzessenz:&r 3 in einer Reihe ergeben 16 Eichenstämme, andere Muster andere Holzarten.",
              "&eEisessenz:&r 8 im Ring ergeben 24 Eis, 9 ergeben 20 Packeis.",
              "&eTiefenschieferessenz:&r 8 im Ring ergeben 24 Bruchtiefenschiefer.",
              "&eWasseressenz:&r 4 um einen Eimer ergeben einen Wassereimer, 1 in 8 Betonpulver ergibt 8 Beton.",
              "&eFeueressenz:&r 4 um einen Eimer ergeben einen &6Lavaeimer&r, 2 Feuer- und 2 Erdessenz 16 Sand, 2 Stein- und 2 Feueressenz 8 Feuerstein.",
              "",
              "&eKronwerke:&r Lava aus Feuersamen ist eine unendliche Brennstoffquelle für Iron Furnaces und später für den Wärmegenerator von Mekanism, ganz ohne Nether.",
          ],
          tasks=[task_item("mysticalagriculture:stone_essence", 16)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_table("s1_common"), reward_xp(5)],
          deps=["first_seed"], icon="mysticalagriculture:stone_essence"),

    # ---- Essenzwerkzeug --------------------------------------------------------
    quest("essence_tool", 10, 7, "&aVeredle ein Diamantwerkzeug",
          subtitle="Mehr Haltbarkeit, mehr Tempo, ein Augment-Platz.",
          description=[
              "Ein &6Diamantwerkzeug&r in die Mitte, &e2 Inferiumbarren&r links und rechts, &e2 Inferium-Edelsteine&r oben und unten: ein &6Inferiumwerkzeug&r. Das geht mit Spitzhacke, Axt, Schaufel, Hacke und Schwert aus Diamant, und genauso mit einer normalen Schere, einem Bogen, einer Armbrust oder einer Angel.",
              "",
              img("mysticalagriculture:textures/item/gear/inferium_pickaxe.png", 32, 32),
              "",
              "Inferium hat &e2 000 Haltbarkeit&r statt 1 561, gräbt mit Tempo 9 statt 8 und schlägt einen Punkt härter. Repariert wird im Amboss mit Inferiumbarren. Das Werkzeug behält beim späteren Upgrade auf Prudentium seine Verzauberungen.",
              "",
              "Jedes Essenzwerkzeug hat &e1 Platz für ein Augment&r (Glück, Absorption, Pfad-Fläche). Augmente baust du jetzt schon aus Splittern, Eisen und Essenz, aber der &6Basteltisch&r zum Einsetzen braucht Soulium und kommt in &cStufe 2&r.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_pickaxe", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_ingot", 2), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["inferium_ingot"], icon="mysticalagriculture:inferium_pickaxe", size=1.5, shape="hexagon"),

    quest("essence_armor", 12.5, 6, "&aVeredle ein Rüstungsteil",
          subtitle="Diamantrüstung mit Inferium.",
          description=[
              "Genauso wie beim Werkzeug: ein &6Diamantrüstungsteil&r in die Mitte, &e2 Inferiumbarren&r links und rechts, &e2 Inferium-Edelsteine&r oben und unten.",
              "",
              "Inferiumrüstung hält länger als Diamant (Faktor 40 statt 33) und gibt im ganzen Satz &e21 Rüstungspunkte&r statt 20, bei gleicher Härte. Repariert wird mit Inferiumbarren, und jedes Teil hat einen Augment-Platz für Stufe 2. Die &6Inferiumbrustplatte&r ist der beste Anfang, sie fängt den meisten Schaden.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_chestplate", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_ingot", 2), reward_xp(5)],
          deps=["essence_tool"], icon="mysticalagriculture:inferium_chestplate", optional=True),

    quest("inferium_scythe", 12.5, 8, "&aBau eine Sense",
          subtitle="Sieben mal sieben Felder mit einem Klick.",
          description=[
              "&e2 Diamanten&r oben links und in der Mitte, &e3 Stöcke&r diagonal von oben rechts nach unten links: die &6Diamantsense&r. Mit 2 Inferiumbarren und 2 Edelsteinen wird daraus die &6Inferiumsense&r.",
              "",
              img("mysticalagriculture:textures/item/gear/inferium_scythe.png", 32, 32),
              "",
              "&6Rechtsklick&r auf das Feld erntet alle reifen Pflanzen im Umkreis, &e7 mal 7&r Felder, ohne sie auszureißen. Der Samen bleibt stehen, nur der Ertrag fällt. Das ist das Werkzeug für jede Essenzfarm, und nebenbei eine Waffe mit Flächenschlag.",
              "",
              "Die &6Sichel&r (3 Diamanten im Bogen, ein Stock unten links) ist der Gegenpart: Sie mäht Gras, Laub und Pflanzen im Umkreis weg. Die Prudentiumsense erntet 9 mal 9, ab Stufe 2.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_scythe", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_xp(5)],
          deps=["essence_tool"], icon="mysticalagriculture:inferium_scythe"),

    quest("paxel", 15, 7, "&aBau eine Inferium-Paxel",
          subtitle="Mystical Agradditions: drei Werkzeuge in einem.",
          description=[
              "&6Inferiumaxt&r, &6Inferiumspitzhacke&r und &6Inferiumschaufel&r nebeneinander in die obere Reihe, darunter &e2 Stöcke&r übereinander: die &6Inferium-Paxel&r von &aMystical Agradditions&r.",
              "",
              "Die Paxel gräbt Stein, Holz und Erde mit einem Werkzeug und spart zwei Plätze in der Leiste. Sie kostet drei fertige Inferiumwerkzeuge, also 6 Barren und 6 Edelsteine. Wer eine Paxel hat, braucht die drei Einzelwerkzeuge nicht mehr.",
          ],
          tasks=[task_item("mysticalagradditions:inferium_paxel", 1)],
          rewards=[reward_item("mysticalagriculture:inferium_ingot", 4), reward_table("s1_uncommon"), reward_xp(8)],
          deps=["essence_tool"], icon="mysticalagradditions:inferium_paxel"),

    # ---- Agradditions ----------------------------------------------------------
    quest("inferium_coal", 20, 6, "&8Press Inferiumkohle",
          subtitle="Mystical Agradditions: Kohle mit Essenz.",
          description=[
              "Eine &6Kohle&r und &e2 Inferiumessenz&r formlos ergeben &6Inferiumkohle&r. Sie brennt &e120 Sekunden&r, normale Kohle 80. Neun davon ergeben einen &6Inferiumkohleblock&r.",
              "",
              "Lohnt sich nur, wenn Essenz vom Feld im Überfluss kommt. Die höheren Essenzkohlen brennen jeweils doppelt so lang wie die vorige und kommen mit ihren Stufen.",
              "",
              "&cAusblick:&r Agradditions legt auch &6Inferium- und Prosperiumerz&r in den Nether und ins End. Der Nether öffnet mit Stufe 2, das End mit Stufe 4.",
          ],
          tasks=[task_item("mysticalagradditions:inferium_coal", 8)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(3)],
          deps=["essence_crafting"], icon="mysticalagradditions:inferium_coal", optional=True),

    quest("inferium_apple", 20, 8, "&cIss einen Inferiumapfel",
          subtitle="Mystical Agradditions: ein Goldapfel mit Nachschlag.",
          description=[
              "Ein &6Goldener Apfel&r mit &e4 Inferiumessenz&r an den vier Seiten ergibt einen &6Inferiumapfel&r.",
              "",
              "Er füllt &e6 Hunger&r und gibt &eAbsorption&r für &e3 Minuten&r. Die Äpfel der höheren Stufen legen Schnelligkeit, Resistenz und mehr obendrauf. Ein guter Snack vor einem Dungeon, wenn die Essenz übrig ist.",
          ],
          tasks=[task_item("mysticalagradditions:inferium_apple", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(3)],
          deps=["essence_crafting"], icon="mysticalagradditions:inferium_apple", optional=True),

    # ---- Die Essenzfarm --------------------------------------------------------
    quest("farm", 12.5, 11.5, "&a&lLeg eine Essenzfarm an",
          subtitle="Beschleuniger unten, Essenz-Ackerland, Sense in der Hand.",
          description=[
              "Jetzt alles zusammen. &eSo sieht eine Farm aus:&r ein Feld &6Inferium-Ackerland&r, unter jedem Block eine Säule &6Wachstumsbeschleuniger&r, darauf Inferiumsamen und deine Rohstoffsamen. Die &6Inferium-Gießkanne&r läuft, und alle paar Minuten klickst du einmal mit der &6Sense&r durch.",
              "",
              "&eRechnung:&r 9 mal 9 Felder Inferium mit vier Beschleunigern darunter liefern pro Durchgang 81 Essenz. Das sind zehn neue Samen oder zwanzig Prudentiumessenz, sobald Stufe 2 offen ist. Je früher die Farm steht, desto mehr hast du dann.",
              "",
              "&eTipp:&r Wasser braucht Ackerland weiterhin, höchstens 4 Blöcke entfernt. Eine Wasserrinne durch die Mitte des Feldes reicht. Mit Create aus dem Technik-Kapitel kann später eine Erntemaschine die Sense ersetzen.",
          ],
          tasks=[task_item("mysticalagriculture:inferium_essence", 256), task_item("mysticalagriculture:inferium_growth_accelerator", 16)],
          rewards=[reward_table("s1_rare"), reward_item("mysticalagriculture:inferium_block", 2), reward_xp(20)],
          deps=["inferium_watering_can", "inferium_scythe"], icon="mysticalagriculture:inferium_block", size=2.5, shape="gear"),

    quest("outlook", 16, 11.5, "&dLies, was in den nächsten Stufen kommt",
          subtitle="Fünf Essenzen, fünf Stufen.",
          description=[
              "Mystical Agriculture wächst mit dem Server. &cStufe 2:&r &6Prudentium&r mit Kohle-, Natur-, Farbstoff- und Tiersamen, &6Soulium&r mit Seelendolch und Seelenurnen, der &6Ernter&r, der Samenrecycler und der Verzauberer.",
              "",
              "&cStufe 3:&r &6Tertium&r, und damit Eisen, Kupfer, Redstone, Obsidian und die Monstersamen. &cStufe 4:&r &6Imperium&r mit Gold, Lapis und Erfahrung, dazu der &6Erweckungsaltar&r, in dem deine Luft-, Erd-, Wasser- und Feueressenz gebraucht wird. &cStufe 5:&r &6Supremium&r, Diamant, Smaragd, Netherit und die Insanium-Samen von Agradditions.",
              "",
              "&eRezept auf Kronwerke:&r Das Essenzrezept für &6Manastahl&r ist entfernt. Manastahl kommt hier nur aus Botania und Nature's Aura, nicht vom Feld.",
              "",
              "Gesperrte Essenz kannst du lagern, aber nicht verarbeiten, der Tooltip verrät die Stufe. Alles, was du in Stufe 1 anbaust, bleibt und zählt weiter.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["farm"], icon="mysticalagriculture:infusion_crystal", optional=True),

    # ---- Checkliste: Samen der Stufe 1 ----------------------------------------
    quest("all_seeds", 25, 1, "&6&lSammle alle Samen der Stufe 1",
          subtitle="Zehn Sorten, zehn Haken.",
          description=[
              "Mit Inferiumessenz allein lassen sich &e10 Samen&r bauen: Inferium an der Werkbank und neun Sorten im Infusionsaltar, immer mit 4 Inferiumessenz, 4 Material und einer Prosperiumsamenbasis.",
              "",
              "Jeder Samen rechts ist ein Haken. Du musst ihn nur einmal in der Hand gehabt haben. Was die Essenz danach kann, steht bei Essenz zu Blöcken, die Elementsamen werden erst in Stufe 4 wirklich wichtig.",
              "",
              "Alle anderen Samen, ab Kohle aufwärts, brauchen Prudentiumessenz oder höher und kommen mit ihren Stufen.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("mysticalagriculture:prosperity_seed_base", 4), reward_item("mysticalagriculture:inferium_essence", 16)],
          deps=["essence_crafting"], icon="mysticalagriculture:prosperity_seed_base", size=1.5, shape="hexagon"),
] + [seed_quest(i, *s) for i, s in enumerate(SEEDS)]

images = [
    banner("mystical_agriculture/title", "Mystical Agriculture", 15, -6.3, height=1.75, kind="title", colour="nature"),
    banner("mystical_agriculture/inferium", "Inferium", 3.5, -2.7, height=0.9, colour="nature"),
    banner("mystical_agriculture/prosperity", "Prosperium", 3.5, 4.3, height=0.9, colour="stone"),
    banner("mystical_agriculture/altar", "Infusionsaltar", 16.5, -2.7, height=0.9, colour="magic"),
    banner("mystical_agriculture/tools", "Essenzwerkzeug", 12.5, 4.3, height=0.9, colour="nature"),
    banner("mystical_agriculture/agradditions", "Agradditions", 20, 4.3, height=0.9, colour="fire"),
    banner("mystical_agriculture/farm", "Die Essenzfarm", 14.2, 9.7, height=0.9, colour="nature"),
    banner("mystical_agriculture/checklist", "Checkliste: Samen der Stufe 1", 28.75, -4.8, height=0.9, colour="brass"),
]

chapter(C, "Mystical Agriculture", "mysticalagriculture:inferium_essence", "world", quests, shape="circle",
        order=45, stage=1,
        subtitle=["Stufe 1: Inferium, der Infusionsaltar und die ersten Rohstoffsamen."], images=images)
