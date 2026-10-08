"""Food and farming in stage 1: Farmer's Delight (knives, wild crops, cutting board, stove, cooking
pot, rich soil, the first meals and feasts), Farming for Blockheads (fertilizers, trough, nest,
market) and Aquaculture (rods, hooks, worm farm, fillets, neptunium). Cooking for Blockheads,
Botany Pots and the best meals are in cooking.py; this chapter points there. Recipes come from
the FarmersDelight 1.3.4 and FarmingForBlockheads 21.1.14 jars."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "food"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    quest("welcome", 0, 3, "&6&lIss besser als Brot",
          subtitle="Wer gut isst, gräbt länger.",
          description=[
              "Bau ein &6Feuersteinküchenmesser&r, einen &6Herd&r und einen &6Kochtopf&r. Damit kochst du Suppen und Mahlzeiten, die lange satt machen.",
              "",
              "&6Farmer's Delight&r ist die Küche, &6Farming for Blockheads&r hilft bei Feldern und Tieren, &6Aquaculture&r macht Angeln zum Hobby.",
              "",
              "&eTipp:&r AppleSkin zeigt im Tooltip jeder Nahrung Hunger und Sättigung. Küchenmöbel, Pflanztöpfe und die besten Gerichte stehen im Kapitel &6Kochen&r.",
          ],
          tasks=[task_checkmark("Ich habe Hunger")],
          rewards=[reward_item("minecraft:bread", 16), reward_table("s1_common")],
          icon="farmersdelight:cooking_pot", size=2.5, shape="hexagon"),

    # ---- Grundlagen -----------------------------------------------------------
    quest("f_knife", 4.5, -7, "&6Bau ein Feuersteinküchenmesser",
          subtitle="Das wichtigste Werkzeug der Küche.",
          description=[
              "Ein &6Feuerstein&r über einem &6Stock&r.",
              "",
              "Mit dem Messer schneidest du am Schneidebrett, erntest Stroh von Gras und Weizen und schneidest Kuchen in Stücke. Schweine, die du damit erlegst, lassen Schinken fallen.",
          ],
          tasks=[task_item("farmersdelight:flint_knife", 1)],
          rewards=[reward_item("minecraft:bread", 8)],
          deps=["welcome"], icon="farmersdelight:flint_knife", size=1.5),

    quest("f_iron_knife", 4.5, -9.5, "&7Schmiede ein Eisenküchenmesser",
          subtitle="Hält länger, schneidet schneller.",
          description=[
              "Ein &6Eisenbarren&r über einem &6Stock&r. Mit Gold oder Diamant geht es genauso.",
              "",
              "Ein abgenutztes Eisen- oder Goldmesser schmilzt im Ofen zu einem Nugget.",
          ],
          tasks=[task_item("farmersdelight:iron_knife", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 2)],
          deps=["f_knife"], icon="farmersdelight:iron_knife", optional=True),

    quest("f_straw", 7, -8, "&6Ernte Stroh mit dem Messer",
          subtitle="Mit dem Messer durchs hohe Gras.",
          description=[
              "Brich mit dem Messer in der Hand &6Gras&r, &6Weizen&r oder &6Reis&r ab. Du bekommst zusätzlich &6Stroh&r.",
              "",
              "Zwei Stroh übereinander: vier Strohseile. Vier Stroh im Quadrat: ein Leinenstoff. Neun Stroh: ein Strohballen. Und Stroh steckt im Kompost.",
          ],
          tasks=[task_item("farmersdelight:straw", 16)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["f_knife"], icon="farmersdelight:straw"),

    quest("f_cutting_board", 7, -6, "&6Bau ein Schneidebrett",
          subtitle="Mehr aus jeder Zutat holen.",
          description=[
              "Zwei &6Stöcke&r links, vier &6Bretter&r rechts daneben.",
              "",
              "Leg eine Zutat mit Rechtsklick darauf und klick mit dem Werkzeug. Messer: Kohl wird Kohlblätter, Rindfleisch Hackfleisch, Reisrispen Reis und Stroh. Axt: Stämme werden entrindet und geben Rinde.",
          ],
          tasks=[task_item("farmersdelight:cutting_board", 1)],
          rewards=[reward_item("minecraft:beef", 8)],
          deps=["f_knife"], icon="farmersdelight:cutting_board"),

    quest("f_wild", 9, -8, "&aPflück wilde Tomaten",
          subtitle="Wo es warm ist.",
          description=[
              "Brich einen wilden &6Tomatenstrauch&r ab. Du bekommst Tomaten und &6Tomatensamen&r.",
              "",
              "Tomaten klettern an Strohseilen hoch und tragen auf der ganzen Höhe Früchte. Du brauchst sie für Sauce, Salat und Burger.",
          ],
          tasks=[task_item("farmersdelight:tomato", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["f_straw", "f_cutting_board"], icon="farmersdelight:tomato"),

    quest("f_wild_cabbage", 9, -6, "&aPflück wilden Weißkohl",
          subtitle="An der Küste.",
          description=[
              "&6Wildweißkohl&r und &6Wildrüben&r wachsen an Stränden. Abbrechen gibt Kohl und &6Weißkohlsamen&r.",
              "",
              "Am Schneidebrett wird ein Kohl zu Kohlblättern. Kohl zählt als Blattgemüse für Suppen und Salate.",
          ],
          tasks=[task_item("farmersdelight:cabbage", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["f_straw", "f_cutting_board"], icon="farmersdelight:cabbage"),

    quest("f_wild_onion", 11, -7, "&aGrab wilde Zwiebeln aus",
          subtitle="In gemäßigten Gegenden.",
          description=[
              "&6Wildzwiebeln&r, &6Wildkarotten&r und &6Wildkartoffeln&r wachsen in gemäßigten Biomen. Zwiebeln setzt du direkt wieder ein.",
              "",
              "Zwiebeln stecken in gebratenem Reis, Burgern, Eintöpfen und fast jeder großen Mahlzeit.",
          ],
          tasks=[task_item("farmersdelight:onion", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(2)],
          deps=["f_wild", "f_wild_cabbage"], icon="farmersdelight:onion"),

    quest("f_rice", 13, -8, "&6Pflanz Reis ins Wasser",
          subtitle="Wächst mit nassen Füßen.",
          description=[
              "Setz &6Reis&r in Wasser, das genau einen Block tief ist, mit Erde darunter. Wildreis findest du in Sümpfen und an Flussufern.",
              "",
              "Oben wachsen &6Reisrispen&r. Am Schneidebrett werden sie mit dem Messer zu Reis und Stroh.",
          ],
          tasks=[task_item("farmersdelight:rice", 8)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(2)],
          deps=["f_wild_onion"], icon="farmersdelight:rice"),

    quest("f_rope", 13, -6, "&7Dreh Strohseile",
          subtitle="Tomaten klettern gern.",
          description=[
              "Zwei &6Stroh&r übereinander ergeben &evier Strohseile&r.",
              "",
              "Seile über einer Tomatenrebe lassen sie hochklettern. Du kletterst selbst daran in Schächte, und vier Seile werden ein &6Sicherheitsnetz&r gegen Stürze.",
          ],
          tasks=[task_item("farmersdelight:rope", 8)],
          rewards=[reward_item("farmersdelight:tomato_seeds", 4)],
          deps=["f_wild_onion"], icon="farmersdelight:rope", optional=True),

    quest("f_cuts", 15, -7, "&6Zerleg Fleisch und Fisch",
          subtitle="Ein Kotelett, zwei Streifen Speck.",
          description=[
              "Leg rohes Fleisch oder Fisch aufs &6Schneidebrett&r und klick mit dem Messer darauf. Ein &6Schweinekotelett&r gibt zwei &6Roher Speck&r, ein &6Kabeljau&r zwei &6Kabeljauscheiben&r und ein Knochenmehl. Hähnchen und Hammel werden ebenso zu Stücken.",
              "",
              "Die Stücke brauchst du für Sandwiches, Wraps und Spieße. &eTipp:&r Ein Messer mit &6Glück&r erhöht pro Stufe um &d10 Prozent&r die Chance auf seltene Ergebnisse am Brett.",
          ],
          tasks=[task_item("farmersdelight:bacon", 4)],
          rewards=[reward_item("minecraft:porkchop", 8)],
          deps=["f_cutting_board"], icon="farmersdelight:bacon"),

    quest("f_board_dispenser", 17, -7, "&7Lass den Werfer schneiden",
          subtitle="Das Schneidebrett ohne deine Hand.",
          description=[
              "Stell einen &6Werfer&r vor das Schneidebrett und leg ein &6Messer&r hinein. Jedes Redstone-Signal benutzt das Messer auf dem, was gerade auf dem Brett liegt.",
              "",
              "Mit einer Axt im Werfer entrindet er Stämme auf dem Brett und wirft die Rinde ab.",
          ],
          tasks=[task_item("minecraft:dispenser", 1)],
          rewards=[reward_item("minecraft:redstone", 8), reward_xp(3)],
          deps=["f_cuts"], icon="minecraft:dispenser", optional=True),

    # ---- Kochen ----------------------------------------------------------------
    quest("f_stove", 4.5, 0, "&6Bau einen Herd",
          subtitle="Hitze für die ganze Küche.",
          description=[
              "Oben drei &6Eisenbarren&r. Mitte &6Ziegelsteine&r links und rechts. Unten Ziegelsteine, &6Lagerfeuer&r, Ziegelsteine.",
              "",
              "Er brät bis zu sechs Stücke ohne Brennstoff und ist die beste Hitzequelle für Topf und Pfanne. Lagerfeuer, Lava oder ein Magmablock gehen auch.",
          ],
          tasks=[task_item("farmersdelight:stove", 1)],
          rewards=[reward_item("minecraft:coal", 8)],
          deps=["welcome"], icon="farmersdelight:stove", size=1.5),

    quest("f_pot", 7, 0, "&6&lStell einen Kochtopf auf",
          subtitle="Suppen, Eintöpfe und Mahlzeiten.",
          description=[
              "Oben &6Ziegel, Holzschaufel, Ziegel&r. Mitte &6Eisenbarren, Wassereimer, Eisenbarren&r. Unten drei &6Eisenbarren&r. Auf den Herd stellen.",
              "",
              "Links bis zu sechs Zutaten, daneben der Behälter, meist eine &6Schüssel&r. Fertige Portionen bleiben im Topf, bis du sie holst.",
              "",
              "Du kannst den Topf mit Inhalt abbauen und woanders wieder aufstellen.",
          ],
          tasks=[task_item("farmersdelight:cooking_pot", 1)],
          rewards=[reward_item("minecraft:bowl", 16), reward_xp(3)],
          deps=["f_stove"], icon="farmersdelight:cooking_pot", size=1.75, shape="hexagon"),

    quest("f_skillet", 7, 2.4, "&7Schmiede eine Bratpfanne",
          subtitle="Braten auf dem Herd oder in der Hand.",
          description=[
              "Vier &6Eisenbarren&r im Quadrat oben rechts, ein &6Ziegel&r unten links als Griff.",
              "",
              "Auf der Hitzequelle brät sie wie ein kleiner Ofen. In der Hand über einer Hitzequelle geht es auch. Nebenbei eine ordentliche Schlagwaffe.",
          ],
          tasks=[task_item("farmersdelight:skillet", 1)],
          rewards=[reward_item("minecraft:egg", 8)],
          deps=["f_stove"], icon="farmersdelight:skillet", optional=True),

    quest("f_soup", 9.5, -1, "&6Koch eine Gemüsesuppe",
          subtitle="Deine erste richtige Mahlzeit.",
          description=[
              "In den Topf: &6Karotte&r, &6Kartoffel&r, &6Rote Bete&r und &6Weißkohl&r oder ein Kohlblatt. Dazu eine Schüssel.",
              "",
              "Ein Topf kocht mehrere Portionen nacheinander, wenn du genug Zutaten hineinlegst.",
          ],
          tasks=[task_item("farmersdelight:vegetable_soup", 4)],
          rewards=[reward_table("s1_common")],
          deps=["f_pot", "f_wild_cabbage"], icon="farmersdelight:vegetable_soup"),

    quest("f_sauce", 9.5, 1, "&6Koch Tomatensauce",
          subtitle="Grundlage für Nudeln und Eintopf.",
          description=[
              "Zwei &6Tomaten&r in den Topf, eine Schüssel dazu.",
              "",
              "Sie steckt in Nudeln mit Fleischbällchen, Nudeln mit Hammelkotelett und im Fischeintopf.",
          ],
          tasks=[task_item("farmersdelight:tomato_sauce", 2)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["f_pot", "f_wild"], icon="farmersdelight:tomato_sauce"),

    quest("f_stew", 12, -1, "&6Koch einen Rindfleischeintopf",
          subtitle="Deftig und wärmend.",
          description=[
              "Rohes &6Rindfleisch&r, eine &6Karotte&r und eine &6Kartoffel&r in den Topf, dazu eine Schüssel.",
              "",
              "Suppen und Eintöpfe geben meist den Effekt &dKomfort&r, siehe die Quest dahinter.",
          ],
          tasks=[task_item("farmersdelight:beef_stew", 2)],
          rewards=[reward_item("minecraft:carrot", 16)],
          deps=["f_soup"], icon="farmersdelight:beef_stew"),

    quest("f_rice_cooked", 12, 1, "&6Koch Reis",
          subtitle="Die Beilage zu allem.",
          description=[
              "&6Reis&r in den Topf, dazu eine Schüssel.",
              "",
              "Mit &6Ei, Karotte und Zwiebel&r wird Reis im Topf zu &6Gebratenem Reis&r, einer vollen Mahlzeit. Gekochter Reis steckt auch in Steak mit Kartoffeln.",
          ],
          tasks=[task_item("farmersdelight:cooked_rice", 4)],
          rewards=[reward_item("minecraft:egg", 8)],
          deps=["f_sauce", "f_rice"], icon="farmersdelight:cooked_rice"),

    quest("f_steak", 14.5, -2.2, "&6Richte Steak mit Kartoffeln an",
          subtitle="Ohne Topf, aus dem Raster.",
          description=[
              "Formlos: &6Ofenkartoffel&r, &6gebratenes Rindfleisch&r, &6Schüssel&r, &6Zwiebel&r und &6gekochter Reis&r.",
              "",
              "Eine große Mahlzeit, die den Effekt Gesättigt gibt.",
          ],
          tasks=[task_item("farmersdelight:steak_and_potatoes", 1)],
          rewards=[reward_item("minecraft:baked_potato", 8), reward_xp(3)],
          deps=["f_rice_cooked"], icon="farmersdelight:steak_and_potatoes"),

    quest("f_effects", 14.5, 0, "&dVerstehe Gesättigt und Komfort",
          subtitle="Warum gutes Essen mehr kann.",
          description=[
              "&dGesättigt&r: die Hungerleiste sinkt nicht, solange du nicht über Sättigung heilst. &dKomfort&r: du regenerierst Leben, egal wie hungrig du bist.",
              "",
              "Suppen und Eintöpfe geben meist Komfort, große Mahlzeiten meist Gesättigt. Die Dauer steht im Tooltip.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["f_stew", "f_rice_cooked"], icon="farmersdelight:fried_rice"),

    quest("f_soups", 9.5, -2.6, "&6Stapel deine Suppen",
          subtitle="Pilzsuppe zu sechzehnt.",
          description=[
              "Mit Farmer's Delight stapeln sich &6Pilzsuppe&r, &6Rote-Bete-Suppe&r und &6Kaninchenragout&r bis &d16&r, wie die Mahlzeiten aus Farmer's Delight. Dazu geben sie &dGesättigt&r, und das Kaninchenragout macht deutlich mehr satt als in Vanilla.",
              "",
              "Pilze wachsen in der Pilzkolonie, Kaninchen findest du in Wüsten und Schneegebieten.",
          ],
          tasks=[task_item("minecraft:mushroom_stew", 8)],
          rewards=[reward_item("minecraft:bowl", 8)],
          deps=["f_soup"], icon="minecraft:mushroom_stew", optional=True),

    quest("f_cocoa", 17, -2.2, "&6Koch heiße Schokolade",
          subtitle="Ein Getränk gegen schlechte Effekte.",
          description=[
              "In den Topf: eine &6Milchflasche&r, &6Zucker&r und zwei &6Kakaobohnen&r.",
              "",
              "&6Heiße Schokolade&r löscht einen negativen Statuseffekt, etwa Gift oder Langsamkeit. Eine &6Milchflasche&r löscht einen beliebigen Effekt, &6Melonensaft&r heilt ein wenig sofort. Gut für die Höhle und nach einem Bosskampf.",
          ],
          tasks=[task_item("farmersdelight:hot_cocoa", 2)],
          rewards=[reward_item("minecraft:cocoa_beans", 8), reward_xp(3)],
          deps=["f_pot"], icon="farmersdelight:hot_cocoa"),

    quest("f_dough", 12, 3, "&7Knete einen Teigball",
          subtitle="Der Anfang jeder Nudel.",
          description=[
              "Drei &6Weizen&r und ein &6Ei&r, formlos: &edrei Teigbälle&r. Mit Weizen und einem Wassereimer geht es auch.",
              "",
              "Am Schneidebrett schneidet das Messer daraus &6Rohe Nudeln&r. Nudelgerichte stehen im Kapitel &6Kochen&r.",
          ],
          tasks=[task_item("farmersdelight:wheat_dough", 3)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["f_sauce"], icon="farmersdelight:wheat_dough", optional=True),

    quest("f_dumplings", 14.5, 3.4, "&6Füll Teigtaschen",
          subtitle="Zwei Portionen aus einem Topf.",
          description=[
              "In den Topf: ein &6Teigball&r, &6Weißkohl&r, eine &6Zwiebel&r und rohes Hähnchen, Schweinefleisch, Rindfleisch oder ein &6Brauner Pilz&r. Heraus kommen &ezwei&r Teigtaschen.",
              "",
              "Die Pilzvariante kommt ganz ohne Tiere aus. Teigtaschen brauchen keine Schüssel, du isst sie direkt.",
          ],
          tasks=[task_item("farmersdelight:dumplings", 4)],
          rewards=[reward_item("minecraft:wheat", 16), reward_xp(3)],
          deps=["f_dough"], icon="farmersdelight:dumplings"),

    quest("f_burger", 14.5, 2.4, "&6Bau einen Hamburger",
          subtitle="Hackfleisch, Bulette, Brötchen.",
          description=[
              "Formlos: &6Brot&r, &6Rindfleischbulette&r, &6Kohlblatt&r, &6Tomate&r und &6Zwiebel&r.",
              "",
              "Die Bulette brätst du im Ofen aus &6Hackfleisch&r, das das Messer am Schneidebrett aus rohem Rindfleisch schneidet.",
          ],
          tasks=[task_item("farmersdelight:hamburger", 1)],
          rewards=[reward_item("minecraft:beef", 8), reward_xp(3)],
          deps=["f_effects"], icon="farmersdelight:hamburger"),

    quest("f_feast", 17, 0, "&6Tisch ein Backhähnchen auf",
          subtitle="Ein Festmahl für alle.",
          description=[
              "Formlos: &6gebratenes Hähnchen&r, zwei &6Ofenkartoffeln&r, zwei &6Karotten&r, &6Zwiebel&r, &6Ei&r, &6Brot&r und &6Schüssel&r.",
              "",
              "Ein Festmahl stellst du als Block auf den Tisch, und jeder holt sich mit einer Schüssel eine Portion. Hirtenkuchen und Honigglasierter Schinken gehen genauso.",
          ],
          tasks=[task_item("farmersdelight:roast_chicken_block", 1)],
          rewards=[reward_table("s1_common"), reward_xp(4)],
          deps=["f_effects"], icon="farmersdelight:roast_chicken_block"),

    quest("f_pie", 17, 2.4, "&7Back einen Apfelkuchen",
          subtitle="Für den süßen Zahn.",
          description=[
              "&6Kuchenkruste&r: Weizen, Milchflasche, Weizen, darunter ein Weizen. Darauf Äpfel, Zucker und Weizen: der &6Apfelkuchen&r.",
              "",
              "Stell ihn hin und schneide Stücke mit dem Messer ab. Vier Milchflaschen kommen aus einem Milcheimer und vier Glasflaschen.",
          ],
          tasks=[task_item("farmersdelight:apple_pie", 1)],
          rewards=[reward_item("minecraft:apple", 8)],
          deps=["f_effects"], icon="farmersdelight:apple_pie", optional=True),

    quest("f_chocolate_pie", 19.5, 2.4, "&7Back einen Schokokuchen",
          subtitle="Kakao, Milch, Zucker, Kruste.",
          description=[
              "Oben drei &6Kakaobohnen&r, in der Mitte drei &6Milchflaschen&r, unten &6Zucker&r, &6Kuchenkruste&r, &6Zucker&r.",
              "",
              "Wie der Apfelkuchen ein Block für den Tisch. Das Messer schneidet ihn in Stücke, vier Stücke im Quadrat ergeben wieder einen ganzen Kuchen.",
          ],
          tasks=[task_item("farmersdelight:chocolate_pie", 1)],
          rewards=[reward_item("minecraft:sugar", 8)],
          deps=["f_pie"], icon="farmersdelight:chocolate_pie", optional=True),

    # ---- Anbau -----------------------------------------------------------------
    quest("f_bark", 4.5, 6, "&6Schäl Baumrinde",
          subtitle="Stamm, Axt, Schneidebrett.",
          description=[
              "Leg einen &6Holzstamm&r aufs Schneidebrett und klick mit einer &6Axt&r. Du bekommst den entrindeten Stamm und &6Baumrinde&r.",
              "",
              "Rinde ist die Hauptzutat für Organischen Kompost.",
          ],
          tasks=[task_item("farmersdelight:tree_bark", 8)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["welcome"], icon="farmersdelight:tree_bark"),

    quest("f_compost", 7, 6, "&6Misch Organischen Kompost",
          subtitle="Erde, Stroh, Rinde, Knochenmehl.",
          description=[
              "Formlos: eine &6Erde&r, zwei &6Stroh&r, zwei &6Knochenmehl&r, vier &6Baumrinde&r. Oder Erde, zwei Stroh, zwei Verrottetes Fleisch und vier Knochenmehl.",
              "",
              "Als Block hingestellt zersetzt er sich mit der Zeit zu Reichhaltiger Erde.",
          ],
          tasks=[task_item("farmersdelight:organic_compost", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["f_bark"], icon="farmersdelight:organic_compost"),

    quest("f_rich_soil", 9, 6, "&6&lMach Reichhaltige Erde",
          subtitle="Hier wächst alles schneller.",
          description=[
              "Stell Kompost hin und warte. Pilze, Podsol, Myzel oder weiterer Kompost in der Nähe beschleunigen das.",
              "",
              "Pflanzen auf Reichhaltiger Erde wachsen schneller. Mit der Hacke wird sie zu Reichhaltigem Ackerboden.",
          ],
          tasks=[task_item("farmersdelight:rich_soil", 8)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["f_compost"], icon="farmersdelight:rich_soil", size=1.5),

    quest("f_colony", 11, 7.5, "&7Züchte eine Pilzkolonie",
          subtitle="Pilze ohne Ende.",
          description=[
              "Setz einen braunen oder roten Pilz auf Reichhaltige Erde. Er wächst zu einer &6Pilzkolonie&r.",
              "",
              "Eine ausgewachsene Kolonie erntest du mit der &6Schere&r, danach wächst sie weiter.",
          ],
          tasks=[task_item("farmersdelight:brown_mushroom_colony", 1)],
          rewards=[reward_item("minecraft:red_mushroom", 8)],
          deps=["f_rich_soil"], icon="farmersdelight:brown_mushroom_colony", optional=True),

    quest("f_fertilizer", 11, 4.6, "&cStreu Roten Dünger",
          subtitle="Pflanzen wachsen schneller.",
          description=[
              "Oben drei &6rote Farbstoffe&r, Mitte &6Goldnugget, Weizensamen, Goldnugget&r, unten drei &6Knochenmehl&r: vier Dünger.",
              "",
              "Klick damit auf Ackerboden. Er wird zu gedüngtem Ackerland, auf dem alles schneller wächst.",
          ],
          tasks=[task_item("farmingforblockheads:red_fertilizer", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 8)],
          deps=["f_rich_soil"], icon="farmingforblockheads:red_fertilizer"),

    quest("f_fert_green", 13, 4.6, "&aStreu Grünen Dünger",
          subtitle="Mehr Ertrag pro Ernte.",
          description=[
              "Oben drei &6grüne Farbstoffe&r, Mitte &6Goldnugget, Weizensamen, Goldnugget&r, unten drei &6Weizen&r: vier Dünger.",
              "",
              "Gedüngtes Ackerland mit Grün gibt mehr Ertrag. Beide Dünger zusammen ergeben das beste Feld.",
          ],
          tasks=[task_item("farmingforblockheads:green_fertilizer", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 8)],
          deps=["f_fertilizer"], icon="farmingforblockheads:green_fertilizer", optional=True),

    quest("f_fert_yellow", 13, 6.4, "&eStreu Gelben Dünger",
          subtitle="Kein Zertrampeln mehr.",
          description=[
              "Oben drei &6gelbe Farbstoffe&r, Mitte &6Goldnugget, Weizensamen, Goldnugget&r, unten drei &6Erde&r: vier Dünger.",
              "",
              "Das Feld wird stabil und lässt sich nicht mehr zertrampeln.",
          ],
          tasks=[task_item("farmingforblockheads:yellow_fertilizer", 4)],
          rewards=[reward_item("minecraft:gold_nugget", 8)],
          deps=["f_fertilizer"], icon="farmingforblockheads:yellow_fertilizer", optional=True),

    quest("f_crates", 15, 7, "&7Pack Gemüse in Kisten",
          subtitle="Ordnung im Vorratsraum.",
          description=[
              "Neun &6Tomaten&r im Raster ergeben eine &6Tomatenkiste&r. Mit Zwiebeln, Kohl, Karotten, Kartoffeln und Roter Bete genauso.",
              "",
              "Aus der Kiste bekommst du die neun jederzeit zurück. Spart Platz und sieht gut aus.",
          ],
          tasks=[task_item("farmersdelight:tomato_crate", 1)],
          rewards=[reward_xp(3)],
          deps=["f_fertilizer"], icon="farmersdelight:tomato_crate", optional=True),

    # ---- Tiere und Markt -------------------------------------------------------
    quest("f_trough", 4.5, 12, "&6Bau einen Futtertrog",
          subtitle="Die Tiere füttern sich selbst.",
          description=[
              "Bretter, ein &6Heuballen&r und eine &6Goldene Karotte&r, siehe JEI. Füll ihn mit Weizen, Karotten oder Samen.",
              "",
              "Tiere in der Nähe fressen daraus und vermehren sich von selbst. Leder, Fleisch und Wolle kommen nebenbei.",
          ],
          tasks=[task_item("farmingforblockheads:feeding_trough", 1)],
          rewards=[reward_item("minecraft:wheat", 32)],
          deps=["welcome"], icon="farmingforblockheads:feeding_trough", size=1.5),

    quest("f_nest", 7, 11, "&7Bau ein Hühnernest",
          subtitle="Eier einsammeln lassen.",
          description=[
              "Ein &6Heuballen&r zwischen zwei &6Brettern&r.",
              "",
              "Hühner in der Nähe legen ihre Eier hinein statt ins Gras. Eier brauchst du für Teig, Gebratenen Reis und Backhähnchen.",
          ],
          tasks=[task_item("farmingforblockheads:chicken_nest", 1)],
          rewards=[reward_item("minecraft:egg", 8)],
          deps=["f_trough"], icon="farmingforblockheads:chicken_nest"),

    quest("f_market", 7, 13, "&6Stell einen Markt auf",
          subtitle="Samen und Setzlinge für Smaragde.",
          description=[
              "Bretter und eine &6Rote Wolle&r oben, &6Holzstämme&r als Gestell, siehe JEI.",
              "",
              "Der Markt verkauft Samen, Setzlinge, Blumen und Dünger gegen Smaragde, auch die wilden Pflanzen von Farmer's Delight.",
              "",
              "&eRezept auf Kronwerke:&r Er verkauft auch die Productive-Trees-Hybriden der Generationen 1 bis 3 für 1, 2 und 4 Smaragde, siehe Kapitel Kochen.",
          ],
          tasks=[task_item("farmingforblockheads:market", 1)],
          rewards=[reward_item("minecraft:emerald", 8), reward_xp(3)],
          deps=["f_trough"], icon="farmingforblockheads:market"),

    quest("f_ham", 9.5, 11, "&7Jag Schinken mit dem Messer",
          subtitle="Mit dem Messer auf die Jagd.",
          description=[
              "Erleg ein &6Schwein&r mit einem Küchenmesser. Es lässt &6Schinken&r fallen.",
              "",
              "Im Räucherofen wird daraus Räucherschinken für den Honigglasierten Schinken. Am Schneidebrett gibt Schinken Schweinefleisch und einen Knochen.",
          ],
          tasks=[task_item("farmersdelight:ham", 1)],
          rewards=[reward_item("minecraft:porkchop", 8)],
          deps=["f_nest"], icon="farmersdelight:ham", optional=True),

    quest("f_dog_food", 12, 11, "&7Koch Hundefutter",
          subtitle="Für deinen besten Freund.",
          description=[
              "In den Topf: &6Verrottetes Fleisch&r, &6Knochenmehl&r, rohes Fleisch und &6Reis&r.",
              "",
              "Ein gezähmter Wolf, der es frisst, bekommt für eine Weile Effekte. Welche, steht im Tooltip.",
          ],
          tasks=[task_item("farmersdelight:dog_food", 1)],
          rewards=[reward_item("minecraft:bone", 8)],
          deps=["f_ham"], icon="farmersdelight:dog_food", optional=True),

    quest("f_horse_feed", 9.5, 13, "&7Misch Pferdefutter",
          subtitle="Für schnelle Reisen.",
          description=[
              "Ein &6Heuballen&r oder Reisballen, zwei &6Äpfel&r und eine &6Goldene Karotte&r, siehe JEI.",
              "",
              "Ein gezähmtes Reittier bekommt davon für eine Weile Effekte, die der Tooltip auflistet.",
          ],
          tasks=[task_item("farmersdelight:horse_feed", 1)],
          rewards=[reward_item("minecraft:apple", 8)],
          deps=["f_market"], icon="farmersdelight:horse_feed", optional=True),

    # ---- Fischerei -------------------------------------------------------------
    quest("f_rod", 4.5, 18, "&6Bau eine Eisen-Angelrute",
          subtitle="Neue Fische, neue Ruten.",
          description=[
              "Zwei &6Eisenbleche&r aus der Create-Presse, zwei &6Fäden&r und ein &6Stock&r, siehe JEI.",
              "",
              "Aquaculture bringt Dutzende Fische mit eigenem Lebensraum. Schleichen und Rechtsklick mit der Rute öffnet ihre Plätze für Haken, Köder, Leine und Schwimmer.",
          ],
          tasks=[task_item("aquaculture:iron_fishing_rod", 1)],
          rewards=[reward_item("minecraft:cod", 8)],
          deps=["welcome"], icon="aquaculture:iron_fishing_rod", size=1.5),

    quest("f_hook", 7, 17, "&7Bieg einen Haken",
          subtitle="Der richtige Haken für jeden Fang.",
          description=[
              "Der &6Eisen-Haken&r entsteht aus Eisennuggets. Mit Gold, Federn, Redstone oder mehr Eisen drumherum wird er zum Gold-, Light-, Redstone- oder Heavy-Haken.",
              "",
              "Jeder Haken ändert etwas am Angeln, der Tooltip sagt was. Setz ihn in die Rute ein.",
          ],
          tasks=[task_item("aquaculture:iron_hook", 1)],
          rewards=[reward_item("minecraft:iron_nugget", 16)],
          deps=["f_rod"], icon="aquaculture:iron_hook"),

    quest("f_worm_farm", 7, 19, "&7Bau eine Wurmfarm",
          subtitle="Köder aus Küchenresten.",
          description=[
              "Zäune, ein Block &6Erde&r und Bretter, siehe JEI. Füll sie mit Pflanzenresten.",
              "",
              "Mit der Zeit kommen &6Würmer&r heraus. In die Rute eingesetzt beißen die Fische schneller an.",
          ],
          tasks=[task_item("aquaculture:worm_farm", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["f_rod"], icon="aquaculture:worm_farm"),

    quest("f_fillet", 9.5, 18, "&6Filetier einen Fisch",
          subtitle="Mehr Essen aus jedem Fisch.",
          description=[
              "Ein &6Eisen-Filetmesser&r aus zwei Eisenbarren und einem Stock. Messer und Fisch zusammen in die Werkbank: &6Rohes Fischfilet&r.",
              "",
              "Große Fische geben mehr Filets. &6Gräten&r, die du manchmal herausziehst, werden in der Werkbank zu Knochenmehl.",
          ],
          tasks=[task_item("aquaculture:iron_fillet_knife", 1), task_item("aquaculture:fish_fillet_raw", 4)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["f_hook", "f_worm_farm"], icon="aquaculture:iron_fillet_knife"),

    quest("f_tackle", 12, 17, "&7Bau eine Angelkiste",
          subtitle="Alles an einem Platz.",
          description=[
              "Eine &6Truhe&r, Eisenbarren, ein &6Eisenblock&r und oben grüner Farbstoff, Seetang oder Algen, siehe JEI.",
              "",
              "Sie hält Haken, Köder, Leinen und Schwimmer zusammen, und du rüstest darin die Rute aus.",
          ],
          tasks=[task_item("aquaculture:tackle_box", 1)],
          rewards=[reward_xp(3)],
          deps=["f_fillet"], icon="aquaculture:tackle_box", optional=True),

    quest("f_sushi", 12, 19, "&7Roll Sushi",
          subtitle="Roh, aber lecker.",
          description=[
              "Ein &6Rohes Fischfilet&r und &6Seetang&r, siehe JEI.",
              "",
              "Schnell gemacht und ein Snack für unterwegs.",
          ],
          tasks=[task_item("aquaculture:sushi", 4)],
          rewards=[reward_xp(3)],
          deps=["f_fillet"], icon="aquaculture:sushi", optional=True),

    quest("f_neptunium", 14.5, 18, "&bAngle Neptunium",
          subtitle="Ein seltener Fang aus der Tiefe.",
          description=[
              "Angeln, angeln, angeln. Mit Glück ziehst du &bNeptunium&r als Nugget heraus oder in der Schatzkiste &6Neptune's Bounty&r.",
              "",
              "Aus Neptunium-Barren entstehen Werkzeug, Rüstung und die beste Angelrute von Aquaculture.",
          ],
          tasks=[task_item("aquaculture:neptunium_ingot", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["f_tackle"], icon="aquaculture:neptunium_ingot", optional=True),

    quest("f_neptunium_hoe", 17, 17, "&bSchmiede eine Neptunium-Hacke",
          subtitle="Ackerland, das nie austrocknet.",
          description=[
              "Zwei &6Neptuniumbarren&r und zwei &6Stöcke&r, geformt wie jede Hacke.",
              "",
              "Ackerland, das du mit ihr pflügst, &ebleibt feucht&r, auch ohne Wasser in der Nähe. So legst du Felder an, wo es dir passt, etwa auf dem Dach oder in einer Höhle.",
          ],
          tasks=[task_item("aquaculture:neptunium_hoe", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 16), reward_xp(4)],
          deps=["f_neptunium"], icon="aquaculture:neptunium_hoe", optional=True),

    quest("f_neptunium_armor", 17, 19, "&bTauch mit Neptunium-Rüstung",
          subtitle="Atmen, sehen und schwimmen unter Wasser.",
          description=[
              "Jedes Teil wird wie Eisenrüstung aus &6Neptuniumbarren&r gebaut und hat eine eigene Wirkung unter Wasser: Der &6Helm&r verbessert die Sicht, die &6Brustplatte&r lässt dich atmen, die &6Beinlinge&r machen dich schwerelos, die &6Schuhe&r schneller beim Schwimmen.",
              "",
              "Neptunium-Spitzhacke und Schaufel graben unter Wasser ohne Verlangsamung, Schwert und Axt treffen dort härter. Für Ozeanmonumente und versunkene Schiffe genau das Richtige.",
          ],
          tasks=[task_item("aquaculture:neptunium_chestplate", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["f_neptunium"], icon="aquaculture:neptunium_chestplate", optional=True),

    quest("f_treasure", 4.5, 20, "&7Öffne einen Fang aus der Tiefe",
          subtitle="Nicht alles am Haken ist ein Fisch.",
          description=[
              "Beim Angeln ziehst du ab und zu eine &6Box&r, ein &6Schließfach&r oder eine &6Schatztruhe&r aus dem Wasser. &eRechtsklick&r öffnet sie, darin liegt Beute.",
              "",
              "Dazu kommen Treibholz, Algen, Gräten und Blechdosen. Treibholz gibt Bretter, Gräten geben Knochenmehl.",
          ],
          tasks=[task_item("aquaculture:box", 1)],
          rewards=[reward_item("minecraft:string", 8), reward_xp(3)],
          deps=["f_rod"], icon="aquaculture:treasure_chest", optional=True),

    # ---- Abschluss -------------------------------------------------------------
    quest("f_pantry", 20, 6, "&6&lFüll die Speisekammer",
          subtitle="Kochen für die ganze Basis.",
          description=[
              "Acht &6Gemüsesuppen&r, acht &6Rindfleischeintöpfe&r und acht &6Gebratener Reis&r.",
              "",
              "Damit hält jeder Abend in der Mine bis zum Schluss. Weiter geht es im Kapitel &6Kochen&r: Küche, Pflanztöpfe und die besten Gerichte.",
              "",
              "In Stufe 2 verbindet &6Create Central Kitchen&r die Küche mit Blaze-Brenner, Mechanischem Arm und Deployer.",
          ],
          tasks=[task_item("farmersdelight:vegetable_soup", 8), task_item("farmersdelight:beef_stew", 8),
                 task_item("farmersdelight:fried_rice", 8)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["f_effects", "f_rich_soil", "f_market", "f_fillet"],
          icon="farmersdelight:fried_rice", size=2.5, shape="gear"),
]

images = [
    banner("food/title", "Essen", 0, -2.4, height=1.8, kind="title", colour="nature"),
    banner("food/basics", "Grundlagen", 8.5, -11, height=0.9, colour="nature"),
    banner("food/cooking", "Kochen", 10.5, -3.6, height=0.9, colour="fire"),
    banner("food/farming", "Anbau", 7, 4.2, height=0.9, colour="nature"),
    banner("food/animals", "Tiere und Markt", 8, 9.6, height=0.9, colour="brass"),
    banner("food/fishing", "Fischerei", 9, 15.6, height=0.9, colour="water"),
]

chapter(C, "Essen und Landwirtschaft", "farmersdelight:cooking_pot", "world", quests, shape="circle", order=4,
        subtitle=["Messer, Kochtopf, reichhaltige Erde, Dünger, Tiere und Fischerei."],
        images=images)
