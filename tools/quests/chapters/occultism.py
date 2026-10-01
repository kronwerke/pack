"""Occultism in stage 2: Demon's Dream, Spiritfire and the Otherworld materials, white chalk,
the first ritual (Aviar's Circle and the Foliot Crusher), the Foliot workers, the new chalks and
pentacles up to the Djinni (Hedyrin's Lure, Eziveus, Ophyx, Strigeor) and the Ars Ocultas altar.
Books of binding, pentacles, bowls and white, yellow, purple and red chalk are locked until
stage 2 (stage2.json); Afrit, Marid, the spirit attuned gem, iesnium, dimensional storage and the
miners are stage 3. The first quests (Demon's Dream, Spiritfire) use items that are already open
in stage 1 and hand out no stage 2 crates; the white chalk quest is the gate."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_kill, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "occultism"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Den Schleier lueften ------------------------------------------------
    quest("welcome", 0, 0, "&5Occultism",
          subtitle="Geister aus der Anderswelt, gebunden in deinen Dienst.",
          description=[
              "&5Occultism&r ruft &dGeister&r aus der &5Anderswelt&r (The Other Place) herbei und lässt sie für dich arbeiten: Erz zerkleinern, Holz fällen, Items tragen, schmelzen und später sogar ganze Lager verwalten.",
              "",
              "Dein Handbuch ist das &6Dictionary of Spirits&r. Du craftest es formlos aus einem &6Buch&r und &6Demon's Dream Seeds&r, die du beim Abbauen von Gras findest. Das Buch erklärt jedes Ritual Schritt für Schritt und zeigt die Pentakel sogar als Vorschau in der Welt.",
              "",
              pic("occultism:dictionary_of_spirits"),
              "",
              "Die Vorbereitungen am Anfang dieses Kapitels gehen schon jetzt. Die eigentlichen Rituale mit Kreide, Schalen und Bindungsbüchern öffnen mit &6Stufe 2&r, &cAfrit&r und &9Marid&r mit &6Stufe 3&r. Gesperrte Items kannst du tragen, der Tooltip sagt dir, ab wann sie funktionieren.",
          ],
          tasks=[task_item("occultism:dictionary_of_spirits", 1)],
          rewards=[reward_item("occultism:datura_seeds", 8), reward_xp(3)],
          icon="occultism:dictionary_of_spirits", size=2.0, shape="hexagon"),

    quest("datura", 2.5, -1, "&6Demon's Dream",
          subtitle="Eine Frucht, die den dritten Blick öffnet.",
          description=[
              "Pflanz die &6Demon's Dream Seeds&r auf Ackerland wie Weizen. Die reife Pflanze gibt &6Demon's Dream Fruit&r und neue Samen.",
              "",
              pic("occultism:datura"),
              "",
              "Die Frucht hat drei Aufgaben: Sie ist der Zündstoff für &dSpiritfire&r, sie heilt Geister (Rechtsklick auf einen Geist), und gegessen schenkt sie dir mit etwas Glück den &5Third Eye&r. Mit dem dritten Blick siehst du, wo die Anderswelt in unsere hineinragt.",
              "",
              "&eTipp:&r Leg gleich ein kleines Feld an. Du wirst viele Früchte brauchen.",
          ],
          tasks=[task_item("occultism:datura", 8)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["welcome"], icon="occultism:datura"),

    quest("third_eye", 2.5, 1.2, "&5Third Eye",
          subtitle="Mit anderen Augen sehen.",
          description=[
              "Neun Früchte oder Samen im Crafting-Feld ergeben &6Demon's Dream Essence&r. Getrunken gibt sie dir den &5Third Eye&r garantiert und für längere Zeit, allerdings mit Nebenwirkungen, guten wie schlechten.",
              "",
              "Nur der &5Third Eye&r aus Demon's Dream lässt dich &6Otherworld Logs&r und &6Otherstone&r abbauen. Ohne ihn liefert ein Otherworld-Baum nur Eichenholz.",
              "",
              "In Spiritfire geworfen wird die Essenz zu &6Otherworld Essence&r, einer gereinigten Form ohne schlechte Nebenwirkungen.",
          ],
          tasks=[task_item("occultism:demons_dream_essence", 1)],
          rewards=[reward_item("occultism:datura_seeds", 8)],
          deps=["datura"], icon="occultism:demons_dream_essence", optional=True),

    quest("spirit_fire", 4.5, -1, "&dSpiritfire",
          subtitle="Ein Feuer, das nicht verbrennt, sondern verwandelt.",
          description=[
              "Wirf eine &6Demon's Dream Fruit&r auf den Boden und zünde sie mit einem &6Feuerzeug&r an. Die Flamme wird zu &dSpiritfire&r. Es verletzt keine Lebewesen und verbrennt auch keine Items, es verwandelt sie.",
              "",
              "Die ersten Rezepte: &6Andesit&r wird zu &6Otherstone&r, &6Diorit&r zu Otherrock, ein &6Eichensetzling&r zu einem Otherworld-Setzling, &6Federn&r, &6schwarzer Farbstoff&r und &6Bücher&r werden zu den Zutaten der Bindungsbücher. Wirf die Items einfach hinein und sammle das Ergebnis wieder auf.",
              "",
              "&cAchtung:&r Das Feuer erlischt nach einer Weile. Halt ein paar Früchte bereit, oder bau dir ein &6Spirit Campfire&r.",
          ],
          tasks=[task_item("occultism:otherstone", 16)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_xp(3)],
          deps=["datura"], icon="occultism:otherstone"),

    quest("spirit_campfire", 4.5, 1.2, "&6Spirit Campfire",
          subtitle="Spiritfire, das nicht ausgeht.",
          description=[
              "Das &6Spirit Campfire&r craftest du wie ein Lagerfeuer, nur mit einer &6Demon's Dream Fruit&r statt Kohle. Es brennt dauerhaft mit Spiritfire.",
              "",
              "Stell eine &6Sacrificial Bowl&r darauf, dann verwandelt sich jedes Item, das du in die Schale legst, sofort. Ein Trichter oder ein Förderband in die Schale macht daraus eine kleine Fabrik für Otherstone oder gereinigte Kreide.",
          ],
          tasks=[task_item("occultism:spirit_campfire", 1)],
          rewards=[reward_item("occultism:datura", 8)],
          deps=["spirit_fire"], icon="occultism:spirit_campfire", optional=True),

    quest("otherworld_tree", 6.5, -1, "&6Otherworld Logs",
          subtitle="Bäume, die wie Eichen aussehen.",
          description=[
              "Wirf einen &6Eichensetzling&r in Spiritfire, und er wird zum &6Unstable Otherworld Sapling&r. Pflanz ihn ein: Es wächst ein Baum, der wie eine Eiche aussieht.",
              "",
              "Erst mit dem &5Third Eye&r siehst du seine wahre Gestalt und kannst &6Otherworld Logs&r und Blätter abbauen. Ohne ihn fallen nur Eichenstämme heraus. Aus den Blättern fallen neue Otherworld-Setzlinge, aber nur wenn du sie von Hand abbaust.",
              "",
              "&eTipp:&r Später tauscht ein &dFoliot-Händler&r deine instabilen Setzlinge gegen stabile, deren Bäume jeder ohne Third Eye fällen kann.",
          ],
          tasks=[task_item("occultism:otherworld_log", 16)],
          rewards=[reward_item("minecraft:oak_sapling", 8), reward_xp(3)],
          deps=["spirit_fire"], icon="occultism:otherworld_log"),

    quest("ashes", 8.5, -1, "&6Otherworld Ashes",
          subtitle="Asche aus der Anderswelt.",
          description=[
              "Wirf &6Otherworld Logs&r in Spiritfire, und sie zerfallen zu &6Otherworld Ashes&r. Die Asche ist eine der beiden Grundzutaten jeder Kreide.",
          ],
          tasks=[task_item("occultism:otherworld_ashes", 8)],
          rewards=[reward_xp(3)],
          deps=["otherworld_tree"], icon="occultism:otherworld_ashes"),

    quest("burnt_otherstone", 6.5, 1.2, "&6Burnt Otherstone",
          subtitle="Zweimal durch den Ofen.",
          description=[
              "Die zweite Grundzutat der Kreide entsteht im Ofen: &6Otherstone&r geschmolzen ergibt &6Polished Otherstone&r, der noch einmal geschmolzen wird zu &6Burnt Otherstone&r.",
              "",
              "&eTipp:&r Leg einfach einen ganzen Stapel Otherstone in einen Ofen und die Ergebnisse gleich in einen zweiten. Otherstone brauchst du auch für die Opferschalen, also nimm genug.",
          ],
          tasks=[task_item("occultism:burnt_otherstone", 8)],
          rewards=[reward_item("minecraft:coal", 16)],
          deps=["spirit_fire"], icon="occultism:burnt_otherstone"),

    quest("impure_chalk", 10.5, 0, "&6Impure White Chalk",
          subtitle="Fast fertig, aber noch nicht rein.",
          description=[
              "Im Crafting-Feld legst du &e3 Burnt Otherstone&r in eine Spalte und &e3 Otherworld Ashes&r in die Spalte daneben. Heraus kommt &6Impure White Chalk&r.",
              "",
              "Unreine Kreide ist auch die Basis aller anderen Kreidefarben: Sie wird mit weiteren Zutaten zu gelber, violetter, hellgrauer oder limettenfarbener unreiner Kreide gecraftet und am Ende immer in Spiritfire gereinigt.",
          ],
          tasks=[task_item("occultism:chalk_white_impure", 2)],
          rewards=[reward_xp(5)],
          deps=["ashes", "burnt_otherstone"], icon="occultism:chalk_white_impure"),

    quest("white_chalk", 12.5, 0, "&fWhite Chalk",
          subtitle="Das Werkzeug jedes Beschwörers.",
          description=[
              "Wirf die unreine Kreide in Spiritfire, und du hältst &fWhite Chalk&r in der Hand. Diese Kreide öffnet mit &6Stufe 2&r, vorher kannst du sie tragen, aber nicht benutzen.",
              "",
              "Rechtsklick mit Kreide auf einen Block zeichnet ein Zeichen darauf. Mehrmaliges Klicken wechselt das Symbol, aber für Rituale zählt nur die &eFarbe&r und die &ePosition&r der Zeichen, nie das Symbol. Jede Kreide hat eine begrenzte Haltbarkeit.",
              "",
              "Die Muster aus Kreide, Kerzen und später Schädeln heißen &5Pentakel&r. Jedes Ritual braucht ein bestimmtes Pentakel, das Dictionary zeigt dir auf jeder Ritualseite oben einen blauen Link zum passenden Pentakel und eine Vorschau in der Welt.",
          ],
          tasks=[task_item("occultism:chalk_white", 2)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["impure_chalk"], icon="occultism:chalk_white", size=1.75, shape="diamond"),

    # ---- Das erste Ritual ------------------------------------------------------
    quest("tallow", 0.5, 5.5, "&6Butcher Knife",
          subtitle="Talg für Kerzen.",
          description=[
              "Das &6Butcher Knife&r craftest du aus zwei &6Eisenbarren&r und drei &6Stöcken&r. Erlegst du damit große Tiere wie Schweine, Kühe oder Schafe, lassen sie &6Tallow&r fallen.",
              "",
              "Aus Talg werden Kerzen, und fast jedes Pentakel braucht Kerzen, um den Geist stabil zu halten.",
          ],
          tasks=[task_item("occultism:butcher_knife", 1), task_item("occultism:tallow", 8)],
          rewards=[reward_item("minecraft:string", 16)],
          deps=["white_chalk"], icon="occultism:butcher_knife"),

    quest("candles", 2.5, 5.5, "&6Large Candle",
          subtitle="Licht für die Anderswelt.",
          description=[
              "Eine &6Large Candle&r ist ein &6Faden&r über einem &6Tallow&r. Kerzen stabilisieren fast jedes Pentakel. Normale Kerzen aus Minecraft oder aus anderen Mods zählen übrigens genauso.",
              "",
              "Große Kerzen wirken für den Zaubertisch wie Bücherregale, und mit einem Farbstoff im Crafting-Feld bekommst du sie in allen 16 Farben. Für das erste Pentakel brauchst du vier.",
          ],
          tasks=[task_item("occultism:large_candle", 4)],
          rewards=[reward_item("occultism:tallow", 8)],
          deps=["tallow"], icon="occultism:large_candle"),

    quest("bowls", 0.5, 7.5, "&6Sacrificial Bowl",
          subtitle="Hier liegen die Opfergaben.",
          description=[
              "Eine &6Sacrificial Bowl&r craftest du aus &e5 Otherstone&r in U-Form. In diese Schalen legst du die Zutaten eines Rituals, mit Rechtsklick hinein, mit Rechtsklick wieder heraus.",
              "",
              "Ein Ritual braucht &emindestens vier&r Schalen im Umkreis von &e8 Blöcken&r um die Mitte. Wo genau sie stehen, ist egal. Mit einem Kupfer- oder Silberbarren im Crafting-Feld bekommst du hübschere Varianten mit derselben Funktion.",
              "",
              "&eTipp:&r Bau gleich acht. Größere Rituale haben mehr Zutaten.",
          ],
          tasks=[task_item("occultism:sacrificial_bowl", 4)],
          rewards=[reward_item("occultism:otherstone", 16)],
          deps=["white_chalk"], icon="occultism:sacrificial_bowl"),

    quest("golden_bowl", 2.5, 7.5, "&6Golden Ritual Bowl",
          subtitle="Die Mitte jedes Pentakels.",
          description=[
              "Die &6Golden Ritual Bowl&r ist eine Opferschale mit &e8 Goldbarren&r drumherum. Sie steht immer in der Mitte des Pentakels.",
              "",
              "Rechtsklick mit dem Aktivierungsitem, meist einem gebundenen Bindungsbuch, startet das Ritual. Statt mit der Hand geht das auch per Trichter oder Rohr in die Schale. Eine Opferschale kopfüber darüber (bis drei Blöcke hoch) fängt das Ergebnis auf, statt es fallen zu lassen.",
              "",
              "Die goldene Schale gibt je nach Zustand ein Redstone-Signal: 1 heißt, das Ritual wartet auf ein Opfer, 2 wartet auf ein benutztes Item, 8 läuft.",
          ],
          tasks=[task_item("occultism:golden_sacrificial_bowl", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8)],
          deps=["bowls"], icon="occultism:golden_sacrificial_bowl"),

    quest("book_parts", 4.5, 5.5, "&6Zutaten des Bindungsbuchs",
          subtitle="Feder, Tinte, Buch, alles aus Spiritfire.",
          description=[
              "Um einen Geist zu rufen, brauchst du seinen Namen, geschrieben in ein &6Book of Binding&r. Die drei Zutaten entstehen alle in Spiritfire:",
              "",
              "&6Awakened Feather&r aus einer Feder.",
              "&6Purified Ink&r aus schwarzem Farbstoff.",
              "&6Taboo Book&r aus einem normalen Buch.",
              "",
              "&eTipp:&r Schwarzen Farbstoff bekommst du aus Tintenbeuteln oder Hexerei-Beeren. Mach von allem gleich mehrere, jedes Ritual verbraucht ein Buch.",
          ],
          tasks=[task_item("occultism:awakened_feather", 1), task_item("occultism:purified_ink", 1),
                 task_item("occultism:taboo_book", 1)],
          rewards=[reward_item("minecraft:book", 4), reward_item("minecraft:feather", 8)],
          deps=["white_chalk"], icon="occultism:taboo_book"),

    quest("book_foliot", 6.5, 5.5, "&6Book of Binding: Foliot",
          subtitle="Ein Name auf Papier ist eine Leine.",
          description=[
              "Crafte &6Taboo Book&r, &6Purified Ink&r und &6Awakened Feather&r mit &e4 blauem Farbstoff&r zum &6Book of Binding: Foliot&r. Blau steht für Foliot, Violett später für Djinni.",
              "",
              pic("occultism:book_of_binding_bound_foliot"),
              "",
              "Dann crafte das Buch zusammen mit dem &6Dictionary of Spirits&r. Das Dictionary schreibt einen wahren Namen hinein und bleibt dabei erhalten. Heraus kommt das gebundene Buch, der Schlüssel zum Ritual. Welcher Name drin steht, ist egal, nur die Rangstufe des Geistes zählt.",
              "",
              "&eTipp:&r Mehrere Bücher auf einmal bindest du, wenn du sie in ein Gemeißeltes Bücherregal stellst und schleichend mit dem Dictionary darauf klickst.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_foliot", 2)],
          rewards=[reward_item("minecraft:blue_dye", 8), reward_xp(5)],
          deps=["book_parts"], icon="occultism:book_of_binding_bound_foliot"),

    quest("silver", 4.5, 7.5, "&6Silver",
          subtitle="Das Metall, das Geister respektieren.",
          description=[
              "&6Silbererz&r liegt in der Oberwelt, auch in Tiefenschiefer, und reichlich in der Bergbau-Dimension. Rohsilber schmilzt im Ofen zu &6Silver Ingots&r.",
              "",
              "Das erste Ritual will einen Silberbarren, und später steckt Silber in Schalen, Kreide, Taschen und Seelensteinen. Leg dir einen Vorrat an.",
          ],
          tasks=[task_item("occultism:silver_ingot", 8)],
          rewards=[reward_item("occultism:raw_silver", 8)],
          deps=["white_chalk"], icon="occultism:silver_ingot"),

    quest("aviar", 8.5, 6.5, "&5Aviar's Circle",
          subtitle="Das erste Pentakel.",
          description=[
              "Stell die &6Golden Ritual Bowl&r auf eine freie Fläche und zeichne ringsum &5Aviar's Circle&r: &e24 Zeichen White Chalk&r in einem Kreis mit Kreuz, dazu &e4 Kerzen&r diagonal neben der Mitte. Das Dictionary zeigt dir das Muster, per Vorschau sogar direkt in der Welt.",
              "",
              "Stell mindestens vier &6Sacrificial Bowls&r in die Nähe. Dieses Pentakel ruft &dFoliot&r herbei, die schwächsten Geister: Brecher, Schmelzer, Holzfäller, Bauern, Träger und Händler.",
              "",
              "&eTipp:&r Graue Partikel an der goldenen Schale bedeuten, dass das Ritual auf etwas wartet, meist auf ein Opfertier oder ein benutztes Item. Schau im Dictionary auf der Ritualseite nach.",
          ],
          tasks=[task_checkmark("Pentakel gezeichnet")],
          rewards=[reward_item("occultism:large_candle", 4), reward_xp(5)],
          deps=["candles", "golden_bowl", "book_foliot"], icon="occultism:chalk_white"),

    quest("foliot_crusher", 10.7, 6.5, "&dFoliot Crusher",
          subtitle="Dein erster Geist: ein Erzbrecher.",
          description=[
              "Leg je einen &6Eisen-, Gold-, Kupfer-&r und &6Silberbarren&r in die Opferschalen und klick mit dem gebundenen &6Book of Binding: Foliot&r auf die goldene Schale. Nach einer Minute steht ein &dFoliot Crusher&r vor dir.",
              "",
              "Er hebt passende Erze auf, die du in seine Nähe wirfst, und macht aus &eeinem Erz zwei Staub&r. Den Staub schmilzt du im Ofen zu Barren, das verdoppelt deine Ausbeute. Funken und ein Knirschen zeigen, dass er arbeitet.",
              "",
              "Foliot altern nicht und bleiben für immer, solange ihnen nichts passiert. Verletzt heilst du sie mit einer Demon's Dream Fruit.",
              "",
              "&eTipp:&r Mit einem &dFoliot Transporter&r, der aus einer Truhe nachfüllt, und einem &dFoliot Janitor&r, der die Staubhaufen einsammelt, läuft der Brecher von selbst.",
          ],
          tasks=[task_checkmark("Foliot Crusher beschworen")],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["aviar", "silver"], icon="occultism:book_of_binding_foliot", size=1.75, shape="diamond"),

    # ---- Foliot bei der Arbeit -------------------------------------------------
    quest("foliot_smelter", 13.2, 5.3, "&dFoliot Smelter",
          subtitle="Ein Ofen ohne Brennstoff.",
          description=[
              "Mit &6Kohle&r, einem &6Ofen&r und einem &6Lagerfeuer&r in den Schalen ruft Aviar's Circle einen &dFoliot Smelter&r. Er nimmt Items auf, die du ihm hinwirfst, und schmilzt sie wie ein Ofen, nur ohne Brennstoff.",
              "",
              "Er ist so schnell wie ein normaler Ofen. Der Djinni-Schmelzer später schafft das doppelte Tempo.",
          ],
          tasks=[task_checkmark("Foliot Smelter beschworen")],
          rewards=[reward_item("minecraft:coal", 16)],
          deps=["foliot_crusher"], icon="minecraft:furnace", optional=True),

    quest("foliot_transporter", 13.2, 7.7, "&dFoliot Transporter",
          subtitle="Ein Träger, der nie müde wird.",
          description=[
              "Zutaten: &6Lore&r, &6Truhe&r, &6Werfer&r und &6Trichter&r. Mit dem Transporter erscheint ein &6Book of Calling&r, mit dem du ihm Befehle gibst.",
              "",
              "Schleichend mit dem Buch auf eine Truhe geklickt legt fest, woher er nimmt, genauso legst du das Ziel fest. Er kann auch in die Inventare anderer Geister liefern, zum Beispiel Erz direkt an den Crusher.",
              "",
              "&cAchtung:&r Standardmäßig steht er auf &eWhitelist&r und bewegt gar nichts. Öffne mit schleichendem Klick auf ihn das Menü und trag die Items ein, die er tragen soll.",
          ],
          tasks=[task_item("occultism:book_of_calling_foliot_transport_items", 1)],
          rewards=[reward_item("minecraft:chest", 4), reward_xp(5)],
          deps=["foliot_crusher"], icon="occultism:book_of_calling_foliot_transport_items"),

    quest("foliot_janitor", 15.2, 7.7, "&dFoliot Janitor",
          subtitle="Er räumt hinter den anderen auf.",
          description=[
              "Zutaten: &6Chalk Brush&r (Bretter, Wolle und Faden), &6Truhe&r, &6Werfer&r und &6Trichter&r. Der &dJanitor&r sammelt herumliegende Items ein und bringt sie in eine Zieltruhe.",
              "",
              "Stell ihn neben deinen Crusher, trag den Staub in seine Erlaubt-Liste ein, und die Staubhaufen wandern von selbst in die Truhe. Auch er startet auf Whitelist.",
              "",
              "Der Chalk Brush selbst ist nützlich: Rechtsklick damit entfernt Kreidezeichen schnell wieder.",
          ],
          tasks=[task_item("occultism:book_of_calling_foliot_cleaner", 1)],
          rewards=[reward_item("minecraft:hopper", 2)],
          deps=["foliot_transporter"], icon="occultism:book_of_calling_foliot_cleaner", optional=True),

    quest("sapling_trader", 15.2, 5.3, "&dOtherworld Sapling Trader",
          subtitle="Stabile Setzlinge für alle.",
          description=[
              "Mit vier verschiedenen Setzlingen in den Schalen (Eiche, Birke, Fichte, Tropenbaum) ruft Aviar's Circle einen Händler-Foliot. Wirf ihm &6Unstable Otherworld Saplings&r hin, und er gibt dir &6Stabile Otherworld Saplings&r zurück.",
              "",
              "Deren Bäume kann jeder ohne Third Eye fällen, und sie geben wieder stabile Setzlinge. Damit ist dein Nachschub an Otherworld Logs für immer gesichert.",
              "",
              "&cAchtung:&r Händler-Geister leiden unter &eEssence Decay&r und verschwinden nach einiger Zeit. Tausch also gleich einen ganzen Stapel.",
          ],
          tasks=[task_item("occultism:otherworld_sapling", 4)],
          rewards=[reward_item("minecraft:oak_sapling", 16), reward_xp(5)],
          deps=["foliot_crusher"], icon="occultism:otherworld_sapling"),

    quest("foliot_lumberjack", 17.2, 5.3, "&dFoliot Lumberjack",
          subtitle="Holz fällen, Setzlinge pflanzen, alles allein.",
          description=[
              "Zutaten: ein &6Stable Otherworld Sapling&r, dazu Eichen-, Birken- und Fichtensetzling und eine &6Axt&r. Mit dem Holzfäller erscheint sein Book of Calling.",
              "",
              "Leg mit dem Buch seinen Arbeitsbereich und eine Abgabetruhe fest. Er fällt alle Bäume im Bereich, bringt das Holz in die Truhe und pflanzt die Setzlinge wieder ein.",
              "",
              "&eTipp:&r Wenn er nach dem Leerfällen ein paar Minuten Pause macht, ist das Absicht und spart Rechenzeit auf dem Server.",
          ],
          tasks=[task_item("occultism:book_of_calling_foliot_lumberjack", 1)],
          rewards=[reward_item("minecraft:iron_axe", 1), reward_xp(5)],
          deps=["sapling_trader"], icon="occultism:book_of_calling_foliot_lumberjack", optional=True),

    quest("foliot_farmer", 17.2, 7.7, "&dFoliot Farmer",
          subtitle="Ernten und neu säen.",
          description=[
              "Zutaten: &6Demon's Dream Fruit&r, &6Weizen&r, &6Karotte&r, &6Kartoffel&r und eine &6Hacke&r. Der &dFarmer&r erntet reife Pflanzen in seinem Arbeitsbereich, pflanzt neu und bringt die Ernte in eine Truhe, beides stellst du mit seinem Book of Calling ein.",
          ],
          tasks=[task_item("occultism:book_of_calling_foliot_farmer", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 32)],
          deps=["foliot_janitor"], icon="occultism:book_of_calling_foliot_farmer", optional=True),

    quest("ars_ocultas", 19.2, 6.5, "&6Sacrificial Altar",
          subtitle="Ars Ocultas: Opfer aus Quelle.",
          description=[
              "&bArs Ocultas&r verbindet Occultism mit &dArs Nouveau&r. Im Bezaubernden Apparat wird eine &6Golden Ritual Bowl&r mit &e4 Silberbarren&r, &e2 Quellstein&r, einem &6Drygmy-Scherben&r und einem &6Eindämmungsglas&r zum &6Sacrificial Altar&r, dazu 5 000 Quelle.",
              "",
              "Der Altar kommt unter die goldene Schale. Verlangt ein Ritual ein Tieropfer und steht ein Eindämmungsglas mit dem passenden Tier in der Nähe, bezahlt der Altar das Opfer mit Quelle aus einem Quellglas, und das Tier bleibt am Leben.",
              "",
              "Außerdem können Geister wie dein Crusher in einem Eindämmungsglas weiterarbeiten. Items gibst du per Trichter hinein, die Ergebnisse landen in Inventaren daneben.",
          ],
          tasks=[task_item("ars_ocultas:altar", 1)],
          rewards=[reward_item("occultism:silver_ingot", 4), reward_xp(5)],
          deps=["foliot_crusher"], icon="ars_ocultas:altar", optional=True),

    # ---- Neue Kreiden ----------------------------------------------------------
    quest("yellow_chalk", 0.5, 12.5, "&eYellow Chalk",
          subtitle="Gold und Glowstone für Besessenheit.",
          description=[
              "Für die nächsten Pentakel brauchst du Kreide in anderen Farben. Die erste ist &eYellow Chalk&r: &6Impure White Chalk&r mit &6Glowstonestaub&r aus dem Nether und &e2 Goldstaub&r vom Crusher, danach in Spiritfire reinigen.",
              "",
              "Gelb ist die Farbe der &5Besessenheit&r: Mit ihr zeichnest du &5Hedyrin's Lure&r, das Pentakel, in dem ein Foliot in ein Lebewesen fährt. Besessene Wesen lassen seltene Beute viel häufiger fallen.",
          ],
          tasks=[task_item("occultism:chalk_gold", 1)],
          rewards=[reward_item("minecraft:glowstone_dust", 8)],
          deps=["foliot_crusher"], icon="occultism:chalk_gold"),

    quest("endermite", 2.5, 12.5, "&5Possessed Endermite",
          subtitle="Endstein, ohne ins End zu reisen.",
          description=[
              "Zeichne &5Hedyrin's Lure&r: &e12 weiße&r und &e4 gelbe&r Zeichen und &e4 Kerzen&r. Leg je zwei &6Erde&r und &6Stein&r in die Schalen und starte mit dem Foliot-Buch.",
              "",
              "Wenn die grauen Partikel erscheinen, wirf ein &6Ei&r in die Nähe. Ein Endermite erscheint, ein Foliot fährt in ihn, reist ins End und kommt zurück. Besiegt lässt er immer &6Endstein&r fallen.",
              "",
              "Das End öffnet auf Kronwerke erst mit &6Stufe 4&r. Bis dahin ist dieser Endermite der bequemste Weg zu Endstein für die violette Kreide.",
          ],
          tasks=[task_kill("occultism:possessed_endermite", 2)],
          rewards=[reward_item("minecraft:egg", 16), reward_xp(5)],
          deps=["yellow_chalk"], icon="minecraft:egg"),

    quest("skeleton", 2.5, 14.5, "&5Possessed Skeleton",
          subtitle="Schädel für stärkere Pentakel.",
          description=[
              "Ebenfalls in Hedyrin's Lure: &e4 Knochen&r in die Schalen, Foliot-Buch auf die Schale, und wenn die grauen Partikel kommen, opferst du ein &6Huhn&r in der Nähe des Pentakels.",
              "",
              "Das &5Possessed Skeleton&r brennt nicht in der Sonne und lässt immer einen &6Skelettschädel&r fallen. Die Pentakel für Djinni brauchen vier bis acht davon.",
          ],
          tasks=[task_item("minecraft:skeleton_skull", 4)],
          rewards=[reward_item("minecraft:bone", 16), reward_xp(5)],
          deps=["endermite"], icon="minecraft:skeleton_skull"),

    quest("familiars", 0.5, 14.5, "&dVertraute",
          subtitle="Kleine Geister als Begleiter.",
          description=[
              "Hedyrin's Lure ruft auch die ersten &dVertrauten&r: Geister in Tiergestalt, die dich begleiten und Boni geben. Der &dGreedy Familiar&r (Truhe, Eisenblock, Werfer, Trichter, dazu ein Zombie als Opfer) sammelt Items für dich ein. Der &dBeaver&r fällt kleine Bäume, der &dDeer&r lässt dich höher springen, der &dBlacksmith&r repariert und verbessert andere Vertraute.",
              "",
              "Mit dem Djinni kommen weitere dazu. Im &6Familiar Ring&r trägst du einen Vertrauten später als Schmuckstück.",
          ],
          tasks=[task_checkmark("Einen Vertrauten gerufen")],
          rewards=[reward_item("minecraft:iron_block", 1), reward_xp(5)],
          deps=["yellow_chalk"], icon="minecraft:chest", optional=True),

    quest("purple_chalk", 4.5, 12.5, "&5Purple Chalk",
          subtitle="Die Kreide der Bindung.",
          description=[
              "Lass den Crusher &6Endstein&r und &6Obsidian&r zu Staub machen. &6Impure White Chalk&r mit &e1 Endsteinstaub&r und &e2 Obsidianstaub&r ergibt unreine violette Kreide, Spiritfire macht sie rein.",
              "",
              "Violett ist die Farbe der &5Bindung&r (Infusion): Mit ihr bindest du Geister in Gegenstände. Das erste Pentakel dafür ist &5Eziveus' Spectral Compulsion&r.",
          ],
          tasks=[task_item("occultism:chalk_purple", 1)],
          rewards=[reward_item("minecraft:obsidian", 4)],
          deps=["endermite"], icon="occultism:chalk_purple"),

    quest("eziveus", 6.5, 12.5, "&5Eziveus' Spectral Compulsion",
          subtitle="Geister in Gegenstände binden.",
          description=[
              "Das Pentakel: &e16 weiße&r und &e12 violette&r Zeichen und &e8 Kerzen&r. Aktiviert wird es wie gewohnt mit einem gebundenen Foliot-Buch, heraus kommt aber kein Geist, sondern ein &6Gegenstand&r mit einem gebundenen Foliot darin.",
              "",
              "Was du hier machen kannst: &6Research Fragment Dust&r für die Limettenkreide, &6Nature Paste&r für die grüne Kreide, die &6Fragile Soul Gem&r (Eisen, Ei, Glas), die &6Surprisingly Substantial Satchel&r, eine Tasche mit viel Platz, und die &6Apprentice Ritual Satchel&r, die Pentakel für dich zeichnet.",
          ],
          tasks=[task_checkmark("Pentakel gezeichnet")],
          rewards=[reward_item("occultism:large_candle", 4), reward_xp(5)],
          deps=["purple_chalk"], icon="occultism:chalk_purple"),

    quest("research_dust", 8.5, 12.5, "&6Research Fragment Dust",
          subtitle="Wissen, zu Staub zermahlen.",
          description=[
              "In Eziveus' Spectral Compulsion: &6Smaragdstaub&r (vom Crusher) und &e2 Erfahrungsfläschchen&r in die Schalen, gebundenes Foliot-Buch auf die goldene Schale.",
              "",
              "Der Staub ist die Hauptzutat der &aLime Chalk&r, und die brauchst du für jedes Djinni-Pentakel. Mach gleich ein paar.",
          ],
          tasks=[task_item("occultism:research_fragment_dust", 2)],
          rewards=[reward_item("minecraft:experience_bottle", 8)],
          deps=["eziveus"], icon="occultism:research_fragment_dust"),

    quest("satchel", 6.5, 14.5, "&6Apprentice Ritual Satchel",
          subtitle="Pentakel zeichnen ohne Kopfzerbrechen.",
          description=[
              "In Eziveus' Spectral Compulsion: &6Trichter&r, &6Werfer&r, &e2 Wolle&r, &e2 Leder&r, &6Faden&r und ein &6Silberbarren&r. Ein Foliot zieht in die Tasche ein und hilft dir beim Zeichnen.",
              "",
              "Pack Kreiden, Kerzen und Schädel hinein. Wähl im Dictionary über das Augensymbol ein Pentakel als Vorschau, setz es mit dem Buch in der Welt fest, und jeder Rechtsklick mit der Tasche auf ein Vorschauzeichen setzt automatisch das richtige Teil. Die große Tasche, die alles auf einmal zeichnet, kommt mit Stufe 3.",
          ],
          tasks=[task_item("occultism:ritual_satchel_t1", 1)],
          rewards=[reward_item("minecraft:leather", 8)],
          deps=["eziveus"], icon="occultism:ritual_satchel_t1", optional=True),

    quest("nature_paste", 8.5, 14.5, "&6Nature Paste",
          subtitle="Grün für die wilden Geister.",
          description=[
              "Drei &6Laubblöcke&r, drei &6Setzlinge&r und drei &6Samen&r in Eziveus' Spectral Compulsion ergeben &6Nature Paste&r. Mit unreiner weißer Kreide wird daraus grüne Kreide.",
              "",
              "Grün ruft &dwilde Geister&r ohne Bindungsbuch. Für die Pentakel dazu brauchst du aber noch Kreiden, die erst mit Stufe 3 erreichbar sind. Nebenbei macht Nature Paste aus Bruchstein bemoosten Bruchstein, praktisch für den Drygmy von Ars Nouveau.",
          ],
          tasks=[task_item("occultism:nature_paste", 2)],
          rewards=[reward_item("minecraft:mossy_cobblestone", 8)],
          deps=["research_dust"], icon="occultism:nature_paste", optional=True),

    quest("lime_chalk", 10.5, 12.5, "&aLime Chalk",
          subtitle="Die Farbe der Djinni.",
          description=[
              "&6Impure White Chalk&r mit &6Research Fragment Dust&r, &6Smaragdstaub&r und einem &6Schleimball&r, danach in Spiritfire: &aLime Chalk&r.",
              "",
              "Limettengrün gibt einem Pentakel die Rufkraft, die ein &dDjinni&r braucht. In &5Ophyx' Calling&r stecken gleich 36 Zeichen davon, also plane mehrere Stück Kreide ein.",
          ],
          tasks=[task_item("occultism:chalk_lime", 2)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_xp(5)],
          deps=["research_dust"], icon="occultism:chalk_lime"),

    quest("light_gray_chalk", 10.5, 14.5, "&7Light Gray Chalk",
          subtitle="Ein Fundament ohne Weiß.",
          description=[
              "Djinni-Pentakel haben einige Stellen, an denen weiße Kreide nicht genügt: dort muss eine &eFundamentkreide ohne Weiß&r hin, also Hellgrau, Grau oder Schwarz. Hellgrau ist die einfachste.",
              "",
              "&6Impure White Chalk&r mit &6Silberstaub&r, &6Eisenstaub&r und &6Kalzitstaub&r, alle drei vom Crusher, ergibt unreine hellgraue Kreide. Spiritfire reinigt sie.",
          ],
          tasks=[task_item("occultism:chalk_light_gray", 1)],
          rewards=[reward_item("minecraft:calcite", 16)],
          deps=["lime_chalk"], icon="occultism:chalk_light_gray"),

    # ---- Djinni ----------------------------------------------------------------
    quest("book_djinni", 13.2, 12.5, "&6Book of Binding: Djinni",
          subtitle="Ein stärkerer Name.",
          description=[
              "Das Bindungsbuch für einen &dDjinni&r entsteht wie das Foliot-Buch, nur mit &e4 violettem Farbstoff&r statt blauem. Binde es wie gewohnt mit dem Dictionary.",
              "",
              "Djinni sind die am häufigsten gerufene Klasse: klüger und stärker als Foliot, gut für anspruchsvollere Arbeit, für Besessenheit stärkerer Wesen und für wertvollere Bindungen.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_djinni", 2)],
          rewards=[reward_item("minecraft:purple_dye", 8), reward_xp(5)],
          deps=["lime_chalk"], icon="occultism:book_of_binding_bound_djinni"),

    quest("ophyx", 15.2, 12.5, "&5Ophyx' Calling",
          subtitle="Das Pentakel für Djinni.",
          description=[
              "Ein großes Pentakel auf einer Fläche von 13x13: &e36 limettengrüne&r Zeichen im äußeren Ring, &e16 weiße&r und &e8 hellgraue&r innen, &e8 Kerzen&r und &e4 Skelettschädel&r. Nimm dir die Vorschau im Dictionary zu Hilfe, oder lass die Ritual Satchel zeichnen.",
              "",
              "Die Schädel geben dem Kreis die Rufkraft für die Djinni, die Kerzen halten ihn stabil. Ab hier rufst du mit dem gebundenen Djinni-Buch einen Djinni herbei.",
          ],
          tasks=[task_checkmark("Pentakel gezeichnet")],
          rewards=[reward_item("occultism:large_candle", 8), reward_xp(5)],
          deps=["book_djinni", "light_gray_chalk", "skeleton"], icon="occultism:chalk_lime"),

    quest("djinni_crusher", 17.4, 12.5, "&dDjinni Crusher",
          subtitle="Schneller, besser, drei statt zwei.",
          description=[
              "Die Zutaten sind Staub statt Barren: je ein &6Eisen-, Gold-, Kupfer-&r und &6Silberstaub&r. Dann das gebundene Djinni-Buch auf die goldene Schale.",
              "",
              "Der &dDjinni Crusher&r ist schneller als der Foliot und macht aus &eeinem Erz drei Staub&r. Er kann außerdem Eis zerkleinern, ohne dass es schmilzt. Ersetz deinen Foliot Crusher, oder lass beide nebeneinander arbeiten.",
              "",
              "Afrit (vier Staub pro Erz) und Marid (sechs) kommen mit &6Stufe 3&r.",
          ],
          tasks=[task_checkmark("Djinni Crusher beschworen")],
          rewards=[reward_item("minecraft:raw_gold", 32), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["ophyx"], icon="occultism:book_of_binding_djinni", size=1.75, shape="diamond"),

    quest("djinni_time", 19.4, 11.6, "&dZeit und Wetter",
          subtitle="Djinni, die den Himmel verstellen.",
          description=[
              "Ophyx' Calling ruft auch Djinni, die einmal etwas an der Welt ändern und dann verschwinden:",
              "",
              "&eTag:&r Fackel, Setzling, Weizen, gelber Farbstoff.",
              "&eNacht:&r Schwarzpulver, verrottetes Fleisch, Knochen, schwarzer Farbstoff.",
              "&eKlares Wetter:&r Rote Bete, Karotte, Kartoffel, Weizen.",
              "",
              "Dazu der &dDjinni Smelter&r (Feuerkugel, Hochofen, Räucherofen, Feuerzeug), der doppelt so schnell schmilzt wie ein Ofen. Sprecht Zeit und Wetter auf dem Server ab, sie gelten für alle.",
          ],
          tasks=[task_checkmark("Einen Djinni-Dienst genutzt")],
          rewards=[reward_item("minecraft:clock", 1)],
          deps=["djinni_crusher"], icon="minecraft:clock", optional=True),

    quest("soul_gem", 15.2, 14.5, "&6Soul Gem",
          subtitle="Ein Wesen in der Hosentasche.",
          description=[
              "Das nächste Pentakel ist &5Strigeor's Higher Binding&r: &e32 violette&r, &e20 limettengrüne&r, &e8 weiße&r und &e8 hellgraue&r Zeichen, &e8 Kerzen&r und &e8 Skelettschädel&r. Es bindet Djinni in Gegenstände.",
              "",
              "Die &6Soul Gem&r entsteht darin aus einem Diamanten, je einem Kupfer-, Silber- und Goldbarren, einer &6Fragile Soul Gem&r (aus Eziveus) und drei Seelensand. Rechtsklick auf ein Wesen fängt es ein, noch ein Rechtsklick lässt es wieder frei. Bosse passen nicht hinein.",
              "",
              "Damit transportierst du Tiere, Dorfbewohner oder Geister, ohne sie über Land zu führen.",
          ],
          tasks=[task_item("occultism:soul_gem", 1)],
          rewards=[reward_item("minecraft:soul_sand", 8), reward_xp(5)],
          deps=["djinni_crusher"], icon="occultism:soul_gem"),

    quest("familiar_ring", 17.4, 15.4, "&6Familiar Ring",
          subtitle="Ein Vertrauter als Schmuckstück.",
          description=[
              "In Strigeor's Higher Binding: eine &6Soul Gem&r, &e2 Gold-&r und &e2 Silberbarren&r. Heraus kommt der &6Familiar Ring&r.",
              "",
              "Fang deinen Vertrauten mit dem Ring ein und trag ihn als Curio. Der Vertraute gibt dir seinen Bonus, ohne neben dir herzulaufen. Gibst du den Ring einem Freund, wird der Vertraute beim Freilassen seiner.",
              "",
              "In &5Ihagan's Enthrallment&r (Gelb, Limette, Hellgrau, Schädel) rufst du stärkere Vertraute: die Fledermaus für Nachtsicht, den Beholder, die Chimäre oder den Fairy. Und eine &5Possessed Bee&r lässt &6Cursed Honey&r fallen, eine Zutat für Stufe 3.",
          ],
          tasks=[task_item("occultism:familiar_ring", 1)],
          rewards=[reward_item("occultism:silver_ingot", 4), reward_xp(5)],
          deps=["soul_gem"], icon="occultism:familiar_ring", optional=True),

    quest("gray_paste", 19.4, 13.7, "&6Gray Paste",
          subtitle="Staub wird wieder zu Stein.",
          description=[
              "In Strigeor's Higher Binding: &6Schwarzpulver&r, &6Ton&r, &6Phantomhaut&r und &6grauer Farbstoff&r. Die &6Gray Paste&r setzt Staub wieder zu Blöcken zusammen: Amethyst, Obsidian, Kalzit, Eis und mehr, JEI zeigt alles.",
              "",
              "Phantomhaut bekommst du auch von einem &5Possessed Phantom&r aus Hedyrin's Lure. Gray Paste steckt außerdem im &dDjinni Crystallizer&r, der aus Staub wieder Edelsteine wachsen lässt.",
          ],
          tasks=[task_item("occultism:gray_paste", 2)],
          rewards=[reward_item("minecraft:clay_ball", 16)],
          deps=["djinni_crusher"], icon="occultism:gray_paste", optional=True),

    # ---- Ziel ------------------------------------------------------------------
    quest("summoner", 22, 9.5, "&5Ein Beschwörer",
          subtitle="Geister arbeiten, während du schläfst.",
          description=[
              "Crusher, Schmelzer, Träger und Holzfäller arbeiten für dich, du kennst vier Pentakel und rufst Djinni aus der Anderswelt. Leg dir einen Vorrat an gebundenen Büchern und Limettenkreide an.",
              "",
              "Mit &6Stufe 3&r öffnen die &cAfrit&r und die &9Marid&r, der &6Spirit Attuned Gem&r, das Iesnium aus dem Nether, die Bergbau-Geister und das dimensionale Lager. Das Ziel von Stufe 3 verlangt 150 &6Afrit-Essenzen&r, jede von einem beschworenen und besiegten Afrit. Dafür brauchst du dann alles, was du hier gelernt hast.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_djinni", 4), task_item("occultism:chalk_lime", 2)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["djinni_crusher", "soul_gem"], icon="occultism:golden_sacrificial_bowl", size=2.5, shape="gear"),
]

images = [
    banner("occultism/title", "Occultism", 6.5, -4.4, height=1.8, kind="title", colour="magic"),
    banner("occultism/schleier", "Den Schleier lüften", 7.5, -2.5, height=0.9, colour="magic"),
    banner("occultism/ritual", "Das erste Ritual", 4.8, 3.8, height=0.9, colour="magic"),
    banner("occultism/foliot", "Foliot bei der Arbeit", 16.2, 3.8, height=0.9, colour="magic"),
    banner("occultism/kreiden", "Neue Kreiden", 5.5, 10.6, height=0.9, colour="magic"),
    banner("occultism/djinni", "Djinni", 16.3, 10.6, height=0.9, colour="magic"),
]

chapter(C, "Occultism", "occultism:dictionary_of_spirits", "magic", quests, shape="circle", order=13, stage=2,
        subtitle=["Stufe 2. Spiritfire, Kreide, Foliot und Djinni."], images=images)
