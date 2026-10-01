"""Theurgy in stage 3 (the whole mod opens with stage 3), one alchemical step per quest: the
pyromantic brazier, sal ammoniac ore, tank and accumulator, the three principles from the
liquefaction cauldron, calcination oven and distiller, the incubator and its vessels, ore
multiplication (on purpose as strong as Mekanism's ore tripling), strata salt in two steps,
crystallized water, caloric flux, divination rods, mercurial logistics as the first automation,
and the transformation chain: reformation, fermentation (transmutation) and digestion
(exaltation). Recipes and numbers from the theurgy 1.76.1 jar (recipes, worldgen, Hermetica)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner)

C = "theurgy"


quests = [
    # ---- Spagyrik --------------------------------------------------------------
    quest("welcome", 0, 0, "&d&lBau vier Feuerschalen",
          subtitle="Jedes Gerät steht auf einer.",
          description=[
              "&6Pyromantic Brazier&r: fünf &6Kupferbarren&r und vier &6Stein&r, siehe JEI. Gefüttert wird sie mit normalem Ofenbrennstoff.",
              "",
              "&dTheurgy&r trennt Dinge in drei Prinzipien: &6Salt&r (Körper), &6Sulfur&r (Seele) und &6Mercury&r (Energie). Dann setzt du sie wieder zusammen, aus einem Raw Iron werden so drei Barren.",
              "",
              "Das Handbuch &6The Hermetica&r: ein &6Buch&r und zwei &6Sand&r, formlos. Die ganze Mod öffnet mit &6Stufe 3&r.",
          ],
          tasks=[task_item("theurgy:pyromantic_brazier", 4)],
          rewards=[reward_item("minecraft:coal", 32), reward_table("s3_common")],
          icon="theurgy:pyromantic_brazier", size=2.0, shape="hexagon"),

    quest("sal_ore", 2.5, -2, "&7Bau Sal-Ammoniac-Erz ab",
          subtitle="Kristalle für das Lösungsmittel.",
          description=[
              "&6Sal-Ammoniac-Erz&r liegt in der Oberwelt zwischen Y -64 und Y 200, auch als Tiefenschiefer-Variante. Abbauen gibt &6Sal Ammoniac Crystal&r.",
              "",
              "Ein Kristall macht im Akkumulator aus einem Eimer Wasser einen ganzen Eimer Lösungsmittel statt nur 100 mB.",
          ],
          tasks=[task_item("theurgy:sal_ammoniac_crystal", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 4), reward_xp(3)],
          deps=["welcome"], icon="theurgy:sal_ammoniac_ore"),

    quest("sal_tank", 5, -2, "&7Stell Tank und Akkumulator auf",
          subtitle="Der Akkumulator sitzt oben drauf.",
          description=[
              "&6Tank&r: Eisen, Kupfer, Eisen in zwei Reihen, unten Stock, Kupfer, Stock. &6Akkumulator&r: drei Stein, drei Eisen, zwei Stöcke. Akkumulator auf den Tank.",
              "",
              "Füll Wasser mit dem Eimer in den Akkumulator. Blaue Blasen heißt, er arbeitet, gelbe heißt, mit Kristall.",
          ],
          tasks=[task_item("theurgy:sal_ammoniac_tank", 1), task_item("theurgy:sal_ammoniac_accumulator", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(3)],
          deps=["sal_ore"], icon="theurgy:sal_ammoniac_tank"),

    quest("sal_ammoniac", 7.5, -2, "&bZapf einen Eimer Sal Ammoniac",
          subtitle="Das Lösungsmittel der Alchemisten.",
          description=[
              "Wirf einen &6Sal Ammoniac Crystal&r in den Akkumulator und warte. Dann holst du mit einem leeren Eimer &6Sal Ammoniac&r aus dem Tank.",
              "",
              "Ohne Kristall gibt 1 000 mB Wasser nur &e100 mB&r. Mit Kristall &e1 000 mB&r.",
          ],
          tasks=[task_item("theurgy:sal_ammoniac_bucket", 1)],
          rewards=[reward_item("theurgy:sal_ammoniac_crystal", 4), reward_xp(4)],
          deps=["sal_tank"], icon="theurgy:sal_ammoniac_bucket"),

    quest("liquefaction", 10, -2, "&6Löse Sulfur aus Raw Iron",
          subtitle="Hier passiert die Vermehrung.",
          description=[
              "&6Liquefaction Cauldron&r: Kupfer, Kessel, Kupfer über drei Stein, auf die Feuerschale. Sal Ammoniac hinein, mit &6Raw Iron&r anklicken, heizen.",
              "",
              "Ein Raw Iron gibt &e3 Iron Sulfur&r, ein Erzblock &e5&r, ein Barren nur einen. Jeder Vorgang kostet 10 mB Sal Ammoniac, ein Eimer reicht für hundert.",
          ],
          tasks=[task_item("theurgy:liquefaction_cauldron", 1), task_item("theurgy:alchemical_sulfur_iron", 9)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["sal_ammoniac"], icon="theurgy:liquefaction_cauldron"),

    quest("calcination", 2.5, 0.5, "&6Brenn Mineral Salt",
          subtitle="Der Körper eines Minerals.",
          description=[
              "&6Calcination Oven&r: ein Kupferblock mit vier Eisenbarren im Kreuz, auf die Feuerschale. Mit Erz, Rohmetall oder Barren anklicken, heizen.",
              "",
              "Heraus kommt &6Mineral Salt&r. Ein Rohstück gibt nur ein Salz, du brauchst drei pro Rohstück. Billiger geht es mit Strata Salt weiter unten.",
          ],
          tasks=[task_item("theurgy:calcination_oven", 1), task_item("theurgy:alchemical_salt_mineral", 4)],
          rewards=[reward_item("minecraft:charcoal", 16), reward_xp(3)],
          deps=["welcome"], icon="theurgy:calcination_oven"),

    quest("distiller", 5, 0.5, "&6Destillier Mercury Shards",
          subtitle="Die Energie, kristallisiert.",
          description=[
              "&6Distiller&r: ein Kupferblock mit drei Eisenbarren auf drei Stein, auf die Feuerschale. Mit fast allem anklicken.",
              "",
              "Ein Raw Iron gibt fünf Shards, zehn Bruchstein oder drei Feldfrüchte einen. Du brauchst einen Shard pro Barren. Alle Geräte nehmen auch per Trichter.",
          ],
          tasks=[task_item("theurgy:distiller", 1), task_item("theurgy:mercury_shard", 16)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["welcome"], icon="theurgy:distiller"),

    quest("incubator", 7.5, 0.5, "&6Bau einen Incubator",
          subtitle="Wo die drei Prinzipien wieder eins werden.",
          description=[
              "Oben &6Brett, Stein, Brett&r, Mitte drei &6Goldbarren&r, unten &6Stein, Kupfer, Stein&r. Auf eine Feuerschale.",
              "",
              "Allein tut er nichts. Er braucht die drei Gefäße direkt daneben, nächste Quest.",
          ],
          tasks=[task_item("theurgy:incubator", 1)],
          rewards=[reward_item("theurgy:pyromantic_brazier", 1), reward_xp(4)],
          deps=["calcination", "distiller"], icon="theurgy:incubator"),

    quest("vessels", 10, 0.5, "&6Stell die drei Gefäße auf",
          subtitle="Salt, Sulfur, Mercury.",
          description=[
              "Jedes Gefäß: vier &6Kupferbarren&r auf drei &6Stein&r, oben in der Mitte ein Salt, ein Sulfur oder ein Mercury. Alle drei direkt neben den Incubator.",
              "",
              "Mit Rechtsklick füllst du jedes Gefäß mit seinem Prinzip, ein Trichter geht auch.",
          ],
          tasks=[task_item("theurgy:incubator_salt_vessel", 1), task_item("theurgy:incubator_sulfur_vessel", 1),
                 task_item("theurgy:incubator_mercury_vessel", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 12), reward_xp(5)],
          deps=["incubator", "liquefaction"], icon="theurgy:incubator_sulfur_vessel"),

    quest("ore_mult", 12.5, 0.5, "&d&lMach drei Barren aus einem Erz",
          subtitle="Was der Ofen verschwendet, holst du zurück.",
          description=[
              "&6Iron Sulfur&r, &6Mineral Salt&r und &6Mercury Shards&r in die Gefäße, heizen. Ein Sulfur, ein Salz und ein Shard geben einen Eisenbarren.",
              "",
              "Das geht mit fast jedem Erz im Pack: Kupfer, Gold, Osmium, Zinn, Blei, Zink und mehr. JEI zeigt beim Liquefaction Cauldron, welche.",
              "",
              "&eKronwerke:&r Mit Absicht so stark wie Mekanisms Verdreifachung, nur mit Feuer statt Strom. Das Stufenziel will &e4 000 Stahl&r, und jeder Stahlbarren beginnt als Eisen.",
          ],
          tasks=[task_checkmark("Barren aus Sulfur, Salt und Mercury gemacht")],
          rewards=[reward_table("s3_uncommon"), reward_item("minecraft:raw_iron", 32), reward_xp(10)],
          deps=["vessels"], icon="minecraft:iron_ingot", size=1.75, shape="diamond"),

    # ---- Salz, Quecksilber, Wärme ------------------------------------------------
    quest("strata", 0, 5, "&6Brenn Strata Salt aus Bruchstein",
          subtitle="Salz, ohne Erz zu opfern.",
          description=[
              "&6Bruchstein&r, Erde, Sand oder Ton in den Calcination Oven: &6Strata Salt&r, eins pro Block.",
              "",
              "&eTipp:&r Ein zweiter Ofen, den ein Trichter nur mit Bruchstein füttert, hält den Incubator dauerhaft mit Salz satt.",
          ],
          tasks=[task_item("theurgy:alchemical_salt_strata", 20)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["ore_mult"], icon="theurgy:alchemical_salt_strata"),

    quest("strata_mineral", 2.5, 5, "&6Brenn Strata zu Mineral Salt",
          subtitle="Fünf Bruchstein für einen Barren.",
          description=[
              "&efünf Strata Salt&r noch einmal in den Calcination Oven: &eein Mineral Salt&r.",
              "",
              "Damit kostet dich das Salz pro Barren fünf Bruchstein statt eines Drittels Erz.",
          ],
          tasks=[task_item("theurgy:alchemical_salt_mineral", 8)],
          rewards=[reward_item("minecraft:raw_iron", 8), reward_xp(4)],
          deps=["strata"], icon="theurgy:alchemical_salt_mineral"),

    quest("crystal_water", 0, 7.2, "&7Kristallisier Wasser",
          subtitle="Ein Eimer Wasser zum Mitnehmen.",
          description=[
              "Ein beliebiges &6Alchemical Salt&r und ein &6Wassereimer&r, formlos: &6Crystallized Water&r. Mit einem Lavaeimer: Crystallized Lava.",
              "",
              "Im Akkumulator löst sich der Kristall wieder zu &e1 000 mB&r Wasser oder Lava auf.",
          ],
          tasks=[task_item("theurgy:crystallized_water", 2)],
          rewards=[reward_item("minecraft:bucket", 2), reward_xp(3)],
          deps=["strata"], icon="theurgy:crystallized_water", optional=True),

    quest("catalyst", 5, 5, "&bBau einen Mercury Catalyst",
          subtitle="Aus Shards wird Fluss.",
          description=[
              "Oben &6Eisen, Mercury, Eisen&r. Mitte &6Gold, Quarzblock, Gold&r. Unten &6Eisen, Gold, Eisen&r.",
              "",
              "Klick ihn mit Shards an. Er wandelt sie langsam in &bMercury Flux&r, die Seiten werden blauer, je voller er ist. Ein Redstone-Signal hält die Ausgabe an.",
          ],
          tasks=[task_item("theurgy:mercury_catalyst", 1)],
          rewards=[reward_item("theurgy:mercury_shard", 16), reward_xp(4)],
          deps=["ore_mult"], icon="theurgy:mercury_catalyst"),

    quest("caloric", 7.5, 5, "&cHeiz ohne Kohle",
          subtitle="Caloric Flux Emitter.",
          description=[
              "&6Caloric Flux Emitter&r: ein &6Lagerfeuer&r (oder Lavaeimer), zwei Goldbarren, ein Mercury, drei Stein, siehe JEI.",
              "",
              "Klick mit dem Emitter das Gerät an, bis es leuchtet, und setz ihn auf einen Mercury Catalyst. Er heizt bis &e8 Blöcke&r weit, solange Flux da ist.",
          ],
          tasks=[task_item("theurgy:caloric_flux_emitter", 2)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["catalyst"], icon="theurgy:caloric_flux_emitter"),

    quest("divination", 2.5, 7.2, "&7Bau eine Glas-Wünschelrute",
          subtitle="Findet häufige Erze.",
          description=[
              "Zwei &6Glas&r und drei &6Stöcke&r diagonal, siehe JEI.",
              "",
              "Schleichend auf einen Block klicken stimmt sie ein. Rechtsklick halten sucht, ein kurzer Rechtsklick zeigt den letzten Fund ohne Haltbarkeit. Findet Eisen und Kohle.",
          ],
          tasks=[task_item("theurgy:divination_rod_t1", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 8)],
          deps=["strata"], icon="theurgy:divination_rod_t1", optional=True),

    quest("divination2", 5, 7.2, "&7Bau eine Amethyst-Wünschelrute",
          subtitle="Für seltenere Erze.",
          description=[
              "Wie die Glasrute, mit einem &6Amethystsplitter&r in der Mitte und einem &6Goldnugget&r oben rechts.",
              "",
              "Findet auch Gold. Die Diamant-Stufe braucht Quarz und Diamant, die beste Blaze-Rute und Netheritschrott. Mit Sulfur gebaute Ruten sind fest auf eine Erzgruppe eingestellt.",
          ],
          tasks=[task_item("theurgy:divination_rod_t2", 1)],
          rewards=[reward_item("minecraft:gold_nugget", 9), reward_xp(3)],
          deps=["divination"], icon="theurgy:divination_rod_t2", optional=True),

    # ---- Logistik ----------------------------------------------------------------
    quest("wand", 10, 5, "&bBau einen Mercurial Wand",
          subtitle="Das Werkzeug für die Logistik.",
          description=[
              "Drei &6Stöcke&r diagonal, dazu &6Kupfer&r in der Mitte und ein &6Mercury Shard&r oben rechts.",
              "",
              "Der Stab schaltet Logistik-Blöcke an und aus und wählt die Seite, in die sie schieben oder aus der sie ziehen.",
          ],
          tasks=[task_item("theurgy:mercurial_wand", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 8), reward_xp(3)],
          deps=["catalyst"], icon="theurgy:mercurial_wand"),

    quest("logistics", 12.5, 5, "&bSetz Extraktor und Inserter",
          subtitle="Quecksilber trägt Gegenstände.",
          description=[
              "&6Extraktor&r: Kupfer über Mercury Shard. &6Inserter&r: Mercury Shard über Kupfer. Rechtsklick auf einen Block mit Inventar setzt sie an.",
              "",
              "Der Extraktor (rotes Band) zieht aus seinem Block, der Inserter (grünes Band) schiebt hinein. Für Flüssigkeiten gibt es beide mit blauem Farbstoff.",
          ],
          tasks=[task_item("theurgy:logistics_item_extractor", 2), task_item("theurgy:logistics_item_inserter", 2)],
          rewards=[reward_item("theurgy:mercury_shard", 16), reward_xp(4)],
          deps=["wand"], icon="theurgy:logistics_item_extractor"),

    quest("wire", 12.5, 7.2, "&bVerbinde sie mit Kupferdraht",
          subtitle="Ein Netz, so lang du willst.",
          description=[
              "&6Kupfer, Mercury Shard, Kupfer&r in einer Reihe: zehn Drähte. Rechtsklick auf einen Logistik-Block, dann auf den nächsten.",
              "",
              "Alles, was verbunden ist, ist ein Netz. Mehrere Inserter bekommen der Reihe nach. Ein &6Connection Node&r (Mercury, Eisen, drei Ziegel, gibt drei) überbrückt lange Wege.",
          ],
          tasks=[task_item("theurgy:copper_wire", 10)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(4)],
          deps=["logistics"], icon="theurgy:copper_wire"),

    quest("auto_incubator", 15, 6, "&d&lAutomatisier den Incubator",
          subtitle="Die erste Anlage, die allein läuft.",
          description=[
              "Extraktoren an die Ausgabe von Cauldron, Ofen und Distiller, Inserter an die drei Gefäße, alles mit Draht verbunden. Eine Truhe mit Raw Iron am Anfang, eine am Ende.",
              "",
              "Mit &6List Filter&r (acht Papier um einen Shard, gibt neun) bestimmst du, welcher Inserter was bekommt.",
              "",
              "&eKronwerke:&r So läuft Eisen für die Stahlwerker auch, wenn du offline bist.",
          ],
          tasks=[task_checkmark("Ein Incubator läuft ohne mich")],
          rewards=[reward_table("s3_uncommon"), reward_xp(10)],
          deps=["wire", "caloric"], icon="theurgy:list_filter", size=1.5, shape="diamond"),

    # ---- Umwandlung --------------------------------------------------------------
    quest("array", 0, 11.5, "&6Stell drei Pedestale auf",
          subtitle="Quelle, Ziel, Ergebnis.",
          description=[
              "&6Source Pedestal&r: hier liegt das Sulfur, das verbraucht wird. &6Target Pedestal&r: das Sulfur, von dem du mehr willst, es bleibt. &6Result Pedestal&r: hier landet das Ergebnis.",
              "",
              "Kein fester Aufbau, alles nur wenige Blöcke auseinander. Rezepte in JEI.",
          ],
          tasks=[task_item("theurgy:reformation_source_pedestal", 2), task_item("theurgy:reformation_target_pedestal", 1),
                 task_item("theurgy:reformation_result_pedestal", 1)],
          rewards=[reward_item("minecraft:blackstone", 16), reward_xp(4)],
          deps=["catalyst"], icon="theurgy:reformation_target_pedestal"),

    quest("flux_emitter", 2.5, 11.5, "&6Verbinde den Sulfuric Flux Emitter",
          subtitle="Er steuert die Reformation.",
          description=[
              "Sal Ammoniac Crystal, Gold, ein Sulfur und Stein, siehe JEI. Klick jedes Pedestal mit ihm an und setz ihn dann auf einen Mercury Catalyst.",
              "",
              "Ein Rechtsklick auf den gesetzten Emitter zeigt, ob alles verbunden ist.",
          ],
          tasks=[task_item("theurgy:sulfuric_flux_emitter", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["array"], icon="theurgy:sulfuric_flux_emitter"),

    quest("reformation", 5, 11.5, "&5Reformier Lapis zu Quarz",
          subtitle="Gleiche Art, gleiche Stufe, eins zu eins.",
          description=[
              "&6Lapis Sulfur&r auf ein Source Pedestal, ein &6Quartz Sulfur&r aufs Target Pedestal. Der Emitter wandelt eins zu eins, das Ziel-Sulfur bleibt liegen.",
              "",
              "So wird Lapis auch zu &6Certus Quartz&r für AE2. JEI zeigt beim Ziel-Sulfur alle Quellen.",
          ],
          tasks=[task_item("theurgy:alchemical_sulfur_quartz", 4)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(6)],
          deps=["flux_emitter"], icon="theurgy:alchemical_sulfur_quartz"),

    quest("fermentation", 7.5, 11.5, "&6Vergär Sulfur zu Niter",
          subtitle="Sulfur wird formbar.",
          description=[
              "&6Fermentation Vat&r: Kupfer, Kupferblock, Fass, Sulfur. Mit Sulfur, &6Sal Ammoniac Bucket&r und &6Zucker&r oder einer Feldfrucht anklicken, schleichend mit leerer Hand schließen.",
              "",
              "Öffnet sie sich wieder, ist sie fertig. Aus Quartz Sulfur wird &6Common Gems Niter&r, das für eine ganze Gruppe steht.",
          ],
          tasks=[task_item("theurgy:fermentation_vat", 1), task_item("theurgy:alchemical_niter_gems_common", 2)],
          rewards=[reward_item("minecraft:sugar", 32), reward_xp(6)],
          deps=["reformation"], icon="theurgy:fermentation_vat"),

    quest("starter", 7.5, 13.7, "&7Setz einen Gärstarter an",
          subtitle="Weniger Zucker pro Niter.",
          description=[
              "In die Fermentation Vat: &6Sal Ammoniac Bucket&r, &6Zucker&r und eine Feldfrucht. Heraus kommt ein großer Stapel &6Fermentation Starter&r.",
              "",
              "Ein Starter ersetzt pro Gärung den Zucker oder die Feldfrucht.",
          ],
          tasks=[task_item("theurgy:fermentation_starter", 8)],
          rewards=[reward_item("minecraft:sugar_cane", 16), reward_xp(3)],
          deps=["fermentation"], icon="theurgy:fermentation_starter", optional=True),

    quest("transmutation", 10, 11.5, "&5Wandle Edelstein in Metall",
          subtitle="Mit Niter wechselst du die Art.",
          description=[
              "&6Common Gems Niter&r als Quelle, ein &6Common Metals Niter&r als Ziel. Das Ergebnis reformierst du mit einem Iron Sulfur auf dem Target zu Iron Sulfur.",
              "",
              "Zwei Metalle sind einen Edelstein wert, zwei sonstige Minerale ein Metall. JEI zeigt, wie viele Quellen nötig sind.",
          ],
          tasks=[task_item("theurgy:alchemical_niter_metals_common", 4)],
          rewards=[reward_item("theurgy:alchemical_sulfur_iron", 8), reward_xp(7)],
          deps=["fermentation"], icon="theurgy:alchemical_niter_metals_common"),

    quest("purified_gold", 10, 13.7, "&6Reinige Gold",
          subtitle="Der Katalysator für die Verdauung.",
          description=[
              "&6Digestion Vat&r: ein Decorated Pot mit zwei Goldbarren, einem Sal Ammoniac Crystal und Sandstein. Darin: &6Goldbarren&r, ein &6Alchemical Salt&r, ein &6Wassereimer&r, schleichend schließen.",
              "",
              "Heraus kommt &6Purified Gold&r.",
          ],
          tasks=[task_item("theurgy:digestion_vat", 1), task_item("theurgy:purified_gold", 2)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(7)],
          deps=["transmutation"], icon="theurgy:purified_gold"),

    quest("exaltation", 12.5, 12.6, "&5Erheb Eisen zu Gold",
          subtitle="Der Stufenwechsel.",
          description=[
              "In die Digestion Vat: &e4 Common Metals Niter&r, ein &6Sal Ammoniac Bucket&r und ein &6Purified Gold&r. Heraus kommt &e1 Rare Metals Niter&r.",
              "",
              "Reformier es mit einem Gold Sulfur auf dem Target zu &6Gold Sulfur&r, der Incubator macht Gold daraus. Abwärts geht es ohne Gold, eins wird zu vier.",
          ],
          tasks=[task_item("theurgy:alchemical_niter_metals_rare", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["purified_gold"], icon="theurgy:digestion_vat", size=1.5, shape="diamond"),

    # ---- Ziel --------------------------------------------------------------------
    quest("magnum_opus", 17.5, 9, "&d&lVollende das Magnum Opus",
          subtitle="Jedes Material aus jedem anderen.",
          description=[
              "64 &6Iron Sulfur&r und 4 &6Gold Sulfur&r im Inventar.",
              "",
              "Du vermehrst Erze, machst Salz aus Bruchstein, heizt mit Flux und verwandelst Lapis in Quarz und Eisen in Gold.",
              "",
              "&eKronwerke:&r Lass die Incubators durchlaufen und bring das Eisen zu den Stahlwerkern. Jeder Barren, der nicht im Ofen verloren geht, zählt für die 4 000 Stahl.",
          ],
          tasks=[task_item("theurgy:alchemical_sulfur_iron", 64), task_item("theurgy:alchemical_sulfur_gold", 4)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["auto_incubator", "exaltation"], icon="theurgy:incubator", size=2.5, shape="gear"),
]

images = [
    banner("theurgy/title", "Theurgy", 6, -5.6, height=1.8, kind="title", colour="magic"),
    banner("theurgy/spagyrik", "Spagyrik", 6, -3.7, height=0.9, colour="magic"),
    banner("theurgy/waerme", "Salz, Quecksilber, Wärme", 3.5, 3.3, height=0.9, colour="fire"),
    banner("theurgy/logistik", "Logistik", 12.5, 3.3, height=0.9, colour="water"),
    banner("theurgy/umwandlung", "Umwandlung", 6, 9.8, height=0.9, colour="nature"),
]

chapter(C, "Theurgy", "theurgy:incubator", "magic", quests, shape="circle", order=27, stage=3,
        subtitle=["Stufe 3. Spagyrik, Erzvermehrung, Logistik und Umwandlung."], images=images)
