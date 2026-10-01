"""Theurgy in stage 3 (the whole mod opens with stage 3): the pyromantic brazier, sal ammoniac,
the three principles from the liquefaction cauldron, calcination oven and distiller, the
incubator and ore multiplication (on purpose as strong as Mekanism's ore tripling), cheap salt
from strata, caloric flux, divination rods, and the transformation chain: reformation,
fermentation (transmutation) and digestion (exaltation)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "theurgy"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Spagyrik --------------------------------------------------------------
    quest("welcome", 0, 0, "&dTheurgy",
          subtitle="Zerlegen, reinigen, neu zusammensetzen.",
          description=[
              "&dTheurgy&r ist Alchemie im alten Sinn. Jedes Ding besteht aus drei Prinzipien: &6Salt&r ist der Körper, &6Sulfur&r die Seele und &6Mercury&r die Energie. Du trennst sie, reinigst sie und setzt sie wieder zusammen. Das nennt sich &5Spagyrik&r.",
              "",
              "Der praktische Teil: Aus einem &6Raw Iron&r werden drei Eisenbarren. Später verwandelst du sogar ein Material in ein anderes, Lapis in Quarz oder Eisen in Gold.",
              "",
              "Dein Handbuch ist &6The Hermetica&r, formlos gecraftet aus einem &6Buch&r und &e2 Sand&r. Fast jedes Gerät steht auf einem &6Pyromantic Brazier&r, einer Feuerschale aus &e5 Kupferbarren&r und &e4 Stein&r. Gefüttert wird sie mit normalem Ofenbrennstoff.",
              "",
              "Theurgy öffnet komplett mit &6Stufe 3&r. Bau gleich vier Feuerschalen, so viele brauchst du für die ersten Geräte.",
          ],
          tasks=[task_item("theurgy:pyromantic_brazier", 4)],
          rewards=[reward_item("minecraft:coal", 32), reward_xp(5)],
          icon="theurgy:pyromantic_brazier", size=2.0, shape="hexagon"),

    quest("sal_ammoniac", 2.5, -1, "&bSal Ammoniac",
          subtitle="Das Lösungsmittel der Alchemisten.",
          description=[
              "Bevor du Sulfur gewinnen kannst, brauchst du ein Lösungsmittel: flüssiges &bSal Ammoniac&r.",
              "",
              "Stell den &6Sal Ammoniac Accumulator&r (Stein, Eisen, Stöcke) auf den &6Sal Ammoniac Tank&r (Eisen, Kupfer, Stöcke) und füll oben bis zu zehn Eimer Wasser ein. Von allein wird aus 1 000 mB Wasser nur 100 mB Sal Ammoniac. Wirfst du einen &6Sal Ammoniac Crystal&r hinein, löst er sich auf und macht aus einem ganzen Eimer Wasser einen ganzen Eimer Sal Ammoniac.",
              "",
              "Die Kristalle baust du als Erz unter Tage ab. Den fertigen &6Sal Ammoniac Bucket&r holst du mit einem leeren Eimer aus dem Tank.",
          ],
          tasks=[task_item("theurgy:sal_ammoniac_bucket", 1)],
          rewards=[reward_item("theurgy:sal_ammoniac_crystal", 4), reward_xp(3)],
          deps=["welcome"], icon="theurgy:sal_ammoniac_tank"),

    quest("liquefaction", 4.5, -1, "&6Sulfur: Liquefaction Cauldron",
          subtitle="Die Seele der Dinge, gleich mehrfach.",
          description=[
              "Der &6Liquefaction Cauldron&r ist ein Kessel mit &e5 Kupferbarren&r und &e3 Stein&r. Stell ihn auf eine Feuerschale, füll ihn mit dem Sal Ammoniac Bucket und klick ihn mit dem Item an, aus dem du Sulfur willst. Dann Brennstoff in die Schale.",
              "",
              "Hier passiert die Vermehrung: Ein &6Raw Iron&r gibt &e3 Iron Sulfur&r, ein ganzer Erzblock sogar &e5&r, ein Barren nur einen. Jeder Vorgang kostet 10 mB Sal Ammoniac, ein Eimer reicht also für hundert Stück.",
              "",
              "Mit leerer Hand holst du das Sulfur wieder heraus. Blasen im Kessel heißt: er arbeitet.",
          ],
          tasks=[task_item("theurgy:alchemical_sulfur_iron", 9)],
          rewards=[reward_item("minecraft:raw_iron", 16), reward_xp(5)],
          deps=["sal_ammoniac"], icon="theurgy:liquefaction_cauldron"),

    quest("calcination", 2.5, 1.2, "&6Salt: Calcination Oven",
          subtitle="Der Körper eines Minerals.",
          description=[
              "Der &6Calcination Oven&r ist ein &6Kupferblock&r mit &e4 Eisenbarren&r im Kreuz. Auf die Feuerschale stellen, mit dem Material anklicken, heizen. Erze, Rohmetalle und Barren geben &6Mineral Salt&r.",
              "",
              "Für Metalle und Edelsteine brauchst du immer Mineral Salt. Ein Rohstück gibt aber nur ein Salz, und du brauchst drei pro Rohstück. Wie du Salz aus billigem Stein machst, steht weiter unten bei &6Strata Salt&r.",
          ],
          tasks=[task_item("theurgy:alchemical_salt_mineral", 4)],
          rewards=[reward_item("minecraft:charcoal", 16)],
          deps=["welcome"], icon="theurgy:calcination_oven"),

    quest("distiller", 4.5, 1.2, "&6Mercury: Distiller",
          subtitle="Die Energie, kristallisiert.",
          description=[
              "Der &6Distiller&r ist ein &6Kupferblock&r mit &e3 Eisenbarren&r auf &e3 Stein&r. Auch er braucht eine Feuerschale. Fast alles gibt &6Mercury Shards&r, je wertvoller, desto mehr: Ein Raw Iron gibt fünf Shards, zehn Bruchstein oder drei Feldfrüchte geben einen.",
              "",
              "Du brauchst einen Shard pro Barren. Bruchstein ist also eine gute, billige Quelle, und Theurgy-Geräte nehmen Items auch per Trichter an.",
          ],
          tasks=[task_item("theurgy:mercury_shard", 16)],
          rewards=[reward_item("minecraft:cobblestone", 64)],
          deps=["welcome"], icon="theurgy:distiller"),

    quest("incubator", 6.5, 0, "&6Incubator",
          subtitle="Drei Prinzipien werden wieder eins.",
          description=[
              "Der &6Incubator&r (Bretter, Gold, Kupfer, Stein) setzt Salt, Sulfur und Mercury wieder zu einem Item zusammen. Er steht auf einer Feuerschale, und direkt daneben stehen seine drei Gefäße.",
              "",
              "Die &6Salt Vessel&r, &6Sulfur Vessel&r und &6Mercury Vessel&r sind je &e4 Kupferbarren&r auf &e3 Stein&r, oben in der Mitte steckt ein beliebiges Salz, Sulfur oder Mercury. Mit Rechtsklick füllst du jedes Gefäß mit seinem Prinzip.",
          ],
          tasks=[task_item("theurgy:incubator", 1), task_item("theurgy:incubator_salt_vessel", 1),
                 task_item("theurgy:incubator_sulfur_vessel", 1), task_item("theurgy:incubator_mercury_vessel", 1)],
          rewards=[reward_item("theurgy:pyromantic_brazier", 1), reward_xp(5)],
          deps=["liquefaction", "calcination", "distiller"], icon="theurgy:incubator"),

    quest("ore_mult", 8.7, 0, "&dDrei Barren aus einem Erz",
          subtitle="Was der Ofen verschwendet, holst du zurück.",
          description=[
              "Füll die Gefäße mit &6Iron Sulfur&r, &6Mineral Salt&r und &6Mercury Shards&r und heiz den Incubator an. Jedes Set aus einem Sulfur, einem Salz und einem Shard gibt einen Eisenbarren. Aus einem Raw Iron werden so drei Barren.",
              "",
              "Das klappt mit fast jedem Erz im Pack: Kupfer, Gold, Osmium, Zinn, Blei, Zink und mehr. Welche gehen, zeigt dir JEI beim Liquefaction Cauldron.",
              "",
              "&eKronwerke:&r Theurgys Erzvermehrung ist mit Absicht so stark wie Mekanisms Verdreifachung, nur mit Feuer statt Strom. Das Stahlwerk will &e4 000 Stahl&r, und jeder Stahlbarren beginnt als Eisen. Wer drei Incubators laufen lässt, versorgt die Hochöfen von halb Kronwerke. Bietet euer Eisen am Spawn an.",
          ],
          tasks=[task_checkmark("Barren aus Sulfur, Salt und Mercury gemacht")],
          rewards=[reward_table("s3_uncommon"), reward_item("minecraft:raw_iron", 32), reward_xp(10)],
          deps=["incubator"], icon="minecraft:iron_ingot", size=1.75, shape="diamond"),

    # ---- Salz, Quecksilber, Wärme ------------------------------------------------
    quest("strata", 0.5, 5.5, "&6Strata Salt",
          subtitle="Salz aus Bruchstein.",
          description=[
              "Mineral Salt aus Erz zu machen frisst genau das Erz, das du vermehren willst. Besser: &6Bruchstein&r, Erde, Sand oder Ton in den Calcination Oven. Das gibt &6Strata Salt&r.",
              "",
              "Fünf Strata Salt noch einmal kalziniert ergeben ein &6Mineral Salt&r. Also fünf Bruchstein für jeden Barren, und Bruchstein hat jeder Server mehr als genug.",
              "",
              "&eTipp:&r Ein zweiter Calcination Oven, der nur Bruchstein frisst und per Trichter versorgt wird, hält deinen Incubator dauerhaft mit Salz satt.",
          ],
          tasks=[task_item("theurgy:alchemical_salt_strata", 20)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(3)],
          deps=["ore_mult"], icon="theurgy:alchemical_salt_strata"),

    quest("catalyst", 2.5, 5.5, "&bMercury Catalyst",
          subtitle="Aus Shards wird Fluss.",
          description=[
              "Der &6Mercury Catalyst&r (Eisen, Gold, ein Quarzblock und ein Mercury) verwandelt &6Mercury Shards&r langsam in &bMercury Flux&r. Klick ihn mit Shards an, seine Seiten werden immer blauer, je voller er ist.",
              "",
              "Mercury Flux ist die Energie für alles Weitere: Wärme ohne Kohle und die Umwandlung von Sulfur. Die Geräte, die Flux brauchen, setzt du direkt auf den Katalysator. Ein Redstone-Signal hält die Ausgabe an, die Shards werden trotzdem weiter umgewandelt.",
          ],
          tasks=[task_item("theurgy:mercury_catalyst", 1)],
          rewards=[reward_item("theurgy:mercury_shard", 16)],
          deps=["ore_mult"], icon="theurgy:mercury_catalyst"),

    quest("caloric", 4.5, 5.5, "&cCaloric Flux Emitter",
          subtitle="Wärme ohne Kohle.",
          description=[
              "Kohle in Feuerschalen nachzufüllen nennt das Buch \"barbarisch\". Der &6Caloric Flux Emitter&r (ein Lagerfeuer, zwei Goldbarren, ein Mercury, drei Stein) heizt ein Gerät aus bis zu &e8 Blöcken&r Entfernung.",
              "",
              "Klick mit dem Emitter das Gerät an, das er heizen soll, bis es leuchtet. Dann setz ihn auf einen Mercury Catalyst. Solange der Flux liefert, bleibt das Gerät heiß, ganz ohne Feuerschale darunter.",
          ],
          tasks=[task_item("theurgy:caloric_flux_emitter", 2)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["catalyst"], icon="theurgy:caloric_flux_emitter"),

    quest("divination", 0.5, 7.7, "&6Divination Rod",
          subtitle="Eine Wünschelrute für Erze.",
          description=[
              "Die &6Glass Divination Rod&r ist aus Glas und Stöcken schnell gemacht. Schleichend auf einen Block geklickt, wird sie auf ihn eingestimmt. Rechtsklick gedrückt halten lässt sie suchen, und ein einfacher Rechtsklick danach zeigt dir den letzten Fund, ohne Haltbarkeit zu kosten.",
              "",
              "Die Glasrute findet häufige Erze wie Eisen und Kohle. Für Gold brauchst du die &6Iron Rod&r mit Amethyst, für Diamanten noch bessere. Ruten mit eingebautem Sulfur halten viel länger, sind dafür fest auf ein Erz eingestellt.",
          ],
          tasks=[task_item("theurgy:divination_rod_t1", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 8)],
          deps=["strata"], icon="theurgy:divination_rod_t1", optional=True),

    # ---- Umwandlung --------------------------------------------------------------
    quest("array", 0.5, 11.5, "&6Reformation Array",
          subtitle="Pedestale, ein Emitter, ein Katalysator.",
          description=[
              "Die Reformation läuft in einem lockeren Aufbau ohne feste Form, alles nur wenige Blöcke auseinander:",
              "",
              "&6Source Pedestal&r: hier liegt das Sulfur, das verbraucht wird. Mach gleich zwei oder mehr.",
              "&6Target Pedestal&r: hier liegt das Sulfur, von dem du mehr willst. Es wird nicht verbraucht.",
              "&6Result Pedestal&r: hier landet das Ergebnis.",
              "",
              "Der &6Sulfuric Flux Emitter&r (Sal Ammoniac Crystal, Gold, ein Sulfur, Stein) steuert alles. Klick jedes Pedestal mit ihm an und setz ihn dann auf einen Mercury Catalyst. Ein Rechtsklick auf den gesetzten Emitter zeigt, ob alles verbunden ist.",
          ],
          tasks=[task_item("theurgy:reformation_source_pedestal", 2), task_item("theurgy:reformation_target_pedestal", 1),
                 task_item("theurgy:reformation_result_pedestal", 1), task_item("theurgy:sulfuric_flux_emitter", 1)],
          rewards=[reward_item("minecraft:blackstone", 16), reward_xp(5)],
          deps=["catalyst"], icon="theurgy:sulfuric_flux_emitter"),

    quest("reformation", 2.5, 11.5, "&5Reformation",
          subtitle="Lapis wird zu Quarz.",
          description=[
              "Sulfur gleicher &eArt&r (etwa Edelstein) und gleicher &eStufe&r (etwa häufig) lässt sich ineinander umwandeln. Das klassische Beispiel: &6Lapis Sulfur&r auf ein Source Pedestal, ein &6Quartz Sulfur&r aufs Target Pedestal. Der Emitter wandelt eins zu eins um, das Quartz Sulfur auf dem Target bleibt erhalten.",
              "",
              "Leuchtende Kugeln über den Pedestalen zeigen, wo Sulfur liegt, Partikel vom Emitter zeigen, dass er arbeitet. Solange Flux und Quell-Sulfur da sind, läuft es weiter.",
              "",
              "&eTipp:&r Auf demselben Weg wird Lapis auch zu &6Certus Quartz&r für die AE2-Leute. JEI zeigt dir beim Ziel-Sulfur alle möglichen Quellen.",
          ],
          tasks=[task_item("theurgy:alchemical_sulfur_quartz", 4)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["array"], icon="theurgy:alchemical_sulfur_quartz"),

    quest("fermentation", 4.5, 11.5, "&6Fermentation Vat",
          subtitle="Sulfur wird formbar.",
          description=[
              "Sulfur wehrt sich gegen große Veränderungen. Formbarer ist &6Alchemical Niter&r, das für eine ganze Gruppe steht, etwa \"häufige Edelsteine\" statt \"Quarz\".",
              "",
              "Die &6Fermentation Vat&r (Kupfer, ein Kupferblock, ein Fass, ein Sulfur) macht daraus Niter. Klick sie mit einem Sulfur, einem &6Wassereimer&r und &6Zucker&r oder einer Feldfrucht an. Dann schleichend mit leerer Hand anklicken, die Wanne schließt sich und gärt. Öffnet sie sich wieder, ist sie fertig.",
              "",
              "Aus Quartz Sulfur wird so &6Common Gems Niter&r.",
          ],
          tasks=[task_item("theurgy:alchemical_niter_gems_common", 2)],
          rewards=[reward_item("minecraft:sugar", 32), reward_xp(5)],
          deps=["reformation"], icon="theurgy:fermentation_vat"),

    quest("transmutation", 6.5, 11.5, "&5Transmutation",
          subtitle="Edelstein wird zu Metall.",
          description=[
              "Mit Niter wechselst du die Art. Common Gems Niter als Quelle, ein Common Metals Niter als Ziel, und die Reformation macht aus Edelstein-Niter Metall-Niter. Im zweiten Schritt wird dieses Niter auf ein Iron Sulfur reformiert.",
              "",
              "Den Wechselkurs bestimmt die Art: Zwei Metalle sind ein Edelstein wert, zwei sonstige Minerale ein Metall. JEI zeigt dir für jedes Rezept, wie viele Quellen nötig sind.",
              "",
              "Für das Ziel brauchst du zwei Iron Sulfur: eins wird zu Niter vergoren, eins bleibt auf dem Target Pedestal für den letzten Schritt.",
          ],
          tasks=[task_item("theurgy:alchemical_niter_metals_common", 4)],
          rewards=[reward_item("theurgy:alchemical_sulfur_iron", 8), reward_xp(5)],
          deps=["fermentation"], icon="theurgy:alchemical_niter_metals_common"),

    quest("purified_gold", 6.5, 13.7, "&6Purified Gold",
          subtitle="Der Katalysator für die Verdauung.",
          description=[
              "Für den Stufenwechsel brauchst du eine &6Digestion Vat&r: ein &6Decorated Pot&r mit zwei Goldbarren, einem Sal Ammoniac Crystal und Sandstein.",
              "",
              "Erstes Rezept darin: ein &6Goldbarren&r, ein beliebiges &6Alchemical Salt&r und ein &6Wassereimer&r. Wie bei der Gärung schleichend mit leerer Hand schließen und warten. Heraus kommt &6Purified Gold&r.",
          ],
          tasks=[task_item("theurgy:digestion_vat", 1), task_item("theurgy:purified_gold", 2)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["transmutation"], icon="theurgy:purified_gold"),

    quest("exaltation", 8.7, 12.6, "&5Exaltation",
          subtitle="Eisen wird zu Gold.",
          description=[
              "Der Stufenwechsel ist teuer: &e4 Common Metals Niter&r, ein &6Sal Ammoniac Bucket&r und ein &6Purified Gold&r in der Digestion Vat ergeben &e1 Rare Metals Niter&r. In die Gegenrichtung geht es ohne Gold, eins wird zu vier.",
              "",
              "Das Rare Metals Niter reformierst du dann mit einem Gold Sulfur auf dem Target Pedestal zu &6Gold Sulfur&r, und der Incubator macht Gold daraus.",
              "",
              "Damit kannst du im Prinzip alles aus allem machen. Holzkohle zählt als Mineral, aus Bäumen wird also Gold, wenn du lange genug dranbleibst.",
          ],
          tasks=[task_item("theurgy:alchemical_niter_metals_rare", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["purified_gold"], icon="theurgy:digestion_vat", size=1.5, shape="diamond"),

    # ---- Ziel --------------------------------------------------------------------
    quest("magnum_opus", 13, 6.5, "&dMagnum Opus",
          subtitle="Jedes Material aus jedem anderen.",
          description=[
              "Du vermehrst Erze, machst Salz aus Bruchstein, heizt mit Flux statt Kohle und verwandelst Lapis in Quarz und Eisen in Gold. Das Buch nennt das den ersten Schritt des Großen Werks.",
              "",
              "&eKronwerke:&r Der Ofen schläft nie, und deiner auch nicht. Lass die Incubators durchlaufen und bring das Eisen zu den Stahlwerkern. Jeder Barren, der nicht im Ofen verloren geht, ist ein Schritt näher an den 4 000 Stahl für das Stufenziel.",
          ],
          tasks=[task_item("theurgy:alchemical_sulfur_iron", 64), task_item("theurgy:alchemical_sulfur_gold", 4)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["ore_mult", "exaltation"], icon="theurgy:incubator", size=2.5, shape="gear"),
]

images = [
    banner("theurgy/title", "Theurgy", 4.5, -4.4, height=1.8, kind="title", colour="magic"),
    banner("theurgy/spagyrik", "Spagyrik", 4.5, -2.5, height=0.9, colour="magic"),
    banner("theurgy/waerme", "Salz, Quecksilber, Wärme", 2.5, 3.9, height=0.9, colour="fire"),
    banner("theurgy/umwandlung", "Umwandlung", 4.5, 9.9, height=0.9, colour="nature"),
]

chapter(C, "Theurgy", "theurgy:incubator", "magic", quests, shape="circle", order=27, stage=3,
        subtitle=["Stufe 3. Spagyrik, Erzvermehrung und Umwandlung."], images=images)
