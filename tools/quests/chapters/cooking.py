"""Cooking in stage 1, the part food.py does not cover: Cooking for Blockheads (the recipe
books, the multiblock kitchen with cooking table, counters, sink, oven, fridge, the milk jar and
the cow in a jar), Botany Pots with Botany Trees, the basics of Productive Trees (sawmill,
pollination with bees, the pollen sifter, nuts; hybrids and the loot saplings as a note) and a
checklist of the meals with the highest saturation in the pack. Food values are read from the
mod classes (hunger x saturation modifier x 2 is what AppleSkin shows). Farmer's Delight's own
tools, crops and the first meals are in food.py and are not repeated here."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "cooking"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def meal(name, x, y, title, item, recipe, deps=("stuffed_pumpkin",), reward=None):
    """One line of the checklist: a 14 hunger, 21 saturation meal."""
    return quest(name, x, y, title,
                 subtitle="14 Hunger, 21 Sättigung.",
                 description=[recipe, "", pic(item)],
                 tasks=[task_item(item, 4)],
                 rewards=[reward or reward_xp(3)],
                 deps=list(deps), icon=item, optional=True)


quests = [
    # ---- Die Küche -----------------------------------------------------------------
    quest("book", 0, 1, "&6&lBacke das Kochbuch",
          subtitle="Ein Buch im Ofen, und du siehst, was du kochen kannst.",
          description=[
              "Leg ein &6Buch&r in den &6Ofen&r. Heraus kommt &6Cooking for Blockheads I&r, das Kochbuch. Rechtsklick öffnet es: Es zeigt dir jedes Essen, das du mit dem Inhalt deines Inventars gerade machen kannst, Vanilla und alle Mods zusammen.",
              "",
              pic("cookingforblockheads:recipe_book"),
              "",
              "Das Buch allein craftet noch nichts, es zeigt nur. Klick ein Gericht an, und du siehst das Rezept. Oben kannst du nach Name, Hunger oder &eSättigung&r sortieren, das ist die schnellste Art, die besten Mahlzeiten zu finden.",
              "",
              "Dasselbe Buch formlos in die Werkbank gelegt wird zur &6NoFilter-Ausgabe&r, die alle Rezepte zeigt, auch die, für die dir noch Zutaten fehlen.",
          ],
          tasks=[task_item("cookingforblockheads:recipe_book", 1)],
          rewards=[reward_item("minecraft:book", 2), reward_table("s1_common")],
          icon="cookingforblockheads:recipe_book", size=2.0, shape="hexagon"),

    quest("book2", 2.5, 1, "&6Mach das Kochbuch zum Werkzeug",
          subtitle="Band II craftet aus deinem Inventar.",
          description=[
              "&eRezept:&r das &6Kochbuch I&r in die Mitte, eine &6Werkbank&r links und rechts, ein &6Diamant&r oben und unten. Das ist &6Cooking for Blockheads II&r.",
              "",
              pic("cookingforblockheads:crafting_book"),
              "",
              "Band II zeigt nicht nur, er craftet: Klick ein Gericht an, und es wird aus deinem Inventar gemacht, Shift-Klick macht einen ganzen Stapel. Für alles, was an der Werkbank entsteht, brauchst du damit keine Werkbank mehr.",
          ],
          tasks=[task_item("cookingforblockheads:crafting_book", 1)],
          rewards=[reward_item("minecraft:diamond", 1), reward_xp(5)],
          deps=["book"], icon="cookingforblockheads:crafting_book"),

    quest("table", 5, 1, "&6&lBau einen Kochtisch",
          subtitle="Das Herz der Küche, die aus Blöcken besteht.",
          description=[
              "&eRezept:&r oben drei &6Stein&r, in der Mitte Terrakotta, &6Kochbuch II&r, Terrakotta, unten drei &6Terrakotta&r. Der &6Kochtisch&r (Cooking Table) ist das Buch als Block, und er benutzt alles, was an ihm hängt.",
              "",
              "&eSo funktioniert die Küche:&r Jeder Küchenblock, der den Kochtisch oder einen anderen Küchenblock berührt, gehört dazu. Der Tisch nimmt Zutaten aus Theken, Schränken und Kühlschränken, Wasser aus dem Spülbecken, Milch aus dem Milchglas, Werkzeug vom Werkzeugregal und brät im Backofen. Du klickst nur noch das Gericht an.",
              "",
              "Der &6Küchenverbinder&r (drei Stein, sechs Terrakotta) führt die Küche um Ecken, der &6Küchenboden&r (zwei Kohleblöcke, zwei Quarzblöcke im Schachbrett, ergibt zwölf) verbindet Blöcke, die auf ihm stehen, über Abstand.",
              "",
              "&eTipp:&r Stell den &6Kochtopf&r von Farmer's Delight an die Küche. Dann kocht der Tisch auch Suppen und Eintöpfe aus dem Kapitel Essen, solange der Topf auf seiner Hitzequelle steht.",
          ],
          tasks=[task_item("cookingforblockheads:cooking_table", 1)],
          rewards=[reward_item("minecraft:terracotta", 16), reward_table("s1_common"), reward_xp(5)],
          deps=["book2"], icon="cookingforblockheads:cooking_table", size=1.75, shape="gear"),

    quest("counters", 7.5, 0, "&6Stell Theken und Schränke auf",
          subtitle="Vorräte, die der Kochtisch sieht.",
          description=[
              "Die &6Küchentheke&r (Counter) ist das Kochtisch-Rezept mit einer &6Truhe&r statt des Buchs: drei Stein, Terrakotta, Truhe, Terrakotta, drei Terrakotta. Der &6Küchenschrank&r (Cabinet) sind fünf Terrakotta um eine Truhe, er hängt an die Wand über die Küchenzeile.",
              "",
              "Beide lagern Zutaten, und der Kochtisch greift direkt hinein. Eine Reihe Theken mit Weizen, Zucker, Eiern, Gemüse und Fleisch, und du kochst, ohne je eine Truhe zu öffnen.",
              "",
              "Alle Küchenblöcke lassen sich mit &6Farbstoff&r einfärben, 16 Farben, formlos an der Werkbank. Mit &6Knochenmehl&r wird ein gefärbter Block wieder weiß.",
          ],
          tasks=[task_item("cookingforblockheads:counter", 2), task_item("cookingforblockheads:cabinet", 1)],
          rewards=[reward_item("minecraft:terracotta", 16)],
          deps=["table"], icon="cookingforblockheads:counter"),

    quest("sink", 7.5, 2, "&6Bau ein Spülbecken",
          subtitle="Wasser ohne Ende.",
          description=[
              "&eRezept:&r oben drei &6Eisenbarren&r, in der Mitte Terrakotta, &6Wassereimer&r, Terrakotta, unten drei Terrakotta. Das &6Spülbecken&r liefert unendlich Wasser: Rechtsklick mit einem Eimer oder einer Glasflasche füllt sie, und der Kochtisch nimmt Wasser für alle Rezepte, die welches brauchen.",
              "",
              "Ohne Spülbecken müsstest du für jeden Kuchen und jede Suppe einen Eimer schleppen. Mit ihr ist Wasser in der Küche einfach da.",
          ],
          tasks=[task_item("cookingforblockheads:sink", 1)],
          rewards=[reward_item("minecraft:bucket", 2), reward_item("minecraft:glass_bottle", 8)],
          deps=["table"], icon="cookingforblockheads:sink"),

    quest("oven", 10, 0, "&6Bau einen Backofen",
          subtitle="Brät nur Essen, dafür neun Stücke auf einmal.",
          description=[
              "&eRezept:&r oben drei &6Schwarzes Glas&r, in der Mitte Eisenbarren, &6Ofen&r, Eisenbarren, unten drei Eisenbarren. Der &6Backofen&r nimmt nur Essen, kein Erz, und gart bis zu neun Stücke gleichzeitig: drei Eingänge, neun Garplätze, drei Ausgänge.",
              "",
              "Er brennt mit allem, was auch der Ofen frisst, aber Brennstoff hält im Backofen nur ein &eDrittel&r so lange. Kohleblöcke statt Kohle, dann musst du seltener nachlegen.",
              "",
              "Steht er an der Küche, brät der Kochtisch damit: Fleisch, Kartoffeln, Fisch und alles, was im Kochbuch einen Ofen verlangt.",
              "",
              "&eAusblick:&r Die &6Heizeinheit&r (drei Eisenklumpen, zwei Eisen, Komparator) heizt den Backofen mit Strom statt Kohle. Strom gibt es ab &6Stufe 2&r.",
          ],
          tasks=[task_item("cookingforblockheads:white_oven", 1)],
          rewards=[reward_item("minecraft:coal_block", 4), reward_xp(3)],
          deps=["counters"], icon="cookingforblockheads:white_oven"),

    quest("fridge", 10, 2, "&6Stell einen Kühlschrank auf",
          subtitle="Zutaten mit Tür, und ein Upgrade, das nie leer wird.",
          description=[
              "Eine &6Truhe&r und eine &6Eisentür&r formlos ergeben den &6Kühlschrank&r. Er lagert Zutaten wie eine Küchentheke, nur mit Tür, und zwei Kühlschränke übereinander werden zu einem großen.",
              "",
              "Zwei Upgrades stecken in den Kühlschrank: Die &6Konservierungskammer&r (drei Redstone, zwei Eisen, Komparator) sorgt dafür, dass der letzte Gegenstand eines Platzes nie verbraucht wird. Ein Ei, ein Zucker, eine Milch bleiben also immer liegen, und das Kochbuch zeigt die Rezepte weiter an. Die &6Eiseinheit&r (drei Schneebälle, zwei Eisen, Komparator) liefert Schnee und Eis für Rezepte.",
          ],
          tasks=[task_item("cookingforblockheads:white_fridge", 1), task_item("cookingforblockheads:preservation_chamber", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 6), reward_table("s1_common")],
          deps=["counters"], icon="cookingforblockheads:white_fridge"),

    quest("cow", 12.5, 2, "&6Sperr eine Kuh ins Glas",
          subtitle="Milch ohne Eimer, für immer.",
          description=[
              "Bau zuerst ein &6Milchglas&r: Glas rundherum, ein Brett oben in der Mitte, ein &6Milcheimer&r in der Mitte. An der Küche liefert es Milch für Kuchen, Suppen und alles mit Milch im Rezept.",
              "",
              "Dann die &6Kuh im Glas&r: Stell das Milchglas auf, lock eine &6Kuh&r so, dass sie darauf steht, und lass einen &6Amboss&r auf sie fallen. Die Kuh verschwindet im Glas und gibt dort &e1 mB Milch pro Tick&r, ein Eimer voll alle 50 Sekunden, solange der Chunk geladen ist.",
              "",
              "Die Kuh muss genau auf dem Glas stehen, nicht daneben. Ein Zaun rundherum und Weizen in der Hand helfen beim Positionieren.",
          ],
          tasks=[task_item("cookingforblockheads:milk_jar", 1), task_item("cookingforblockheads:cow_jar", 1)],
          rewards=[reward_item("minecraft:milk_bucket", 1), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["fridge"], icon="cookingforblockheads:cow_jar", size=1.5, shape="diamond"),

    quest("gadgets", 12.5, 0, "&6Häng den Kleinkram auf",
          subtitle="Toaster, Fruchtkorb, Gewürzregal, Werkzeugregal.",
          description=[
              "Der &6Toaster&r (Steinknopf oben rechts, Eisenfalltür zwischen zwei Eisen, Lavaeimer zwischen zwei Eisen) macht aus Brot Toast. Der &6Fruchtkorb&r (Holzstufe, Holzdruckplatte, Holzstufe) lagert Obst, das &6Gewürzregal&r (zwei Holzstufen) Zutaten, beide sichtbar an der Wand.",
              "",
              "Das &6Werkzeugregal&r (drei Holzstufen, zwei Eisenklumpen) hält Werkzeuge, auch das &6Küchenmesser&r von Farmer's Delight, und der Kochtisch benutzt es von dort. Das &6Schneidebrett&r (Eisenaxt über einer Holzstufe) ist die Blockhead-Version für Rezepte, die eines verlangen.",
              "",
              "Alles davon zählt zur Küche, wenn es die anderen Blöcke berührt.",
          ],
          tasks=[task_item("cookingforblockheads:tool_rack", 1), task_item("cookingforblockheads:spice_rack", 1)],
          rewards=[reward_item("minecraft:bread", 8)],
          deps=["oven"], icon="cookingforblockheads:toaster", optional=True),

    # ---- Blumentöpfe --------------------------------------------------------------
    quest("pot", 0, 6, "&a&lTöpfere einen Pflanztopf",
          subtitle="Ein Feld in einem Block.",
          description=[
              "&eRezept:&r vier &6Terrakotta&r um einen &6Blumentopf&r (oben links und rechts, in der Mitte links und rechts, eine unten). Das ist der &6Pflanztopf&r (Botany Pot).",
              "",
              "Rechtsklick mit &6Erde&r setzt den Boden, Rechtsklick mit &6Samen&r die Pflanze. Sie wächst ohne Wasser, Licht oder Platz, und mit Rechtsklick erntest du, die Pflanze bleibt stehen. Weizen, Karotten, Kartoffeln, Zuckerrohr, Kaktus, Pilze, Blumen, Seegras, Netherwarze, alles geht.",
              "",
              "Töpfe gibt es aus jeder Terrakotta-Farbe, aus Beton und aus Ziegelarten, immer nach demselben Rezept. Jade und der Tooltip zeigen dir, welche Pflanze welchen Boden will und wie lange sie braucht.",
          ],
          tasks=[task_item("botanypots:terracotta_botany_pot", 2)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_table("s1_common")],
          icon="botanypots:terracotta_botany_pot", size=1.5, shape="hexagon"),

    quest("hopper_pot", 2.5, 5, "&aMach den Topf zum Trichter",
          subtitle="Erntet von selbst in die Kiste darunter.",
          description=[
              "Ein &6Pflanztopf&r und ein &6Trichter&r formlos ergeben den &6Trichter-Pflanztopf&r. Oder gleich beim Töpfern: der Trichter oben in die Mitte statt der leeren Stelle.",
              "",
              "Er erntet reife Pflanzen von selbst und wirft die Ernte in das Inventar unter sich: eine Truhe, ein Fass, eine Schublade oder ein Create-Förderband. Samen pflanzt er nicht nach, das muss er auch nicht, die Pflanze bleibt ja stehen.",
              "",
              "Eine Reihe Trichter-Töpfe über einer Reihe Schubladen ist die kleinste Farm, die es gibt, und sie passt in jede Küche.",
          ],
          tasks=[task_item("botanypots:terracotta_hopper_botany_pot", 4)],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(5)],
          deps=["pot"], icon="botanypots:terracotta_hopper_botany_pot"),

    quest("soil", 2.5, 7, "&aWähl Boden und Werkzeug",
          subtitle="Schneller wachsen, mehr ernten.",
          description=[
              "Der Boden entscheidet, was wächst und wie schnell. &6Reichhaltige Erde&r aus Farmer's Delight wächst 10 Prozent schneller als Erde, Sand ist für Kaktus und Zuckerrohr, Seelensand für Netherwarze, Wasser (ein Wassereimer) für Seegras und Seetang.",
              "",
              "&eWerkzeugplatz:&r Leg ein Werkzeug in den Topf. &6Effizienz&r darauf macht die Pflanze pro Stufe 5 Prozent schneller, eine &6Schere&r bringt Blätter von Bäumen, Behutsamkeit zählt wie beim Abbauen. Das Werkzeug nutzt sich dabei ab.",
              "",
              "&6Knochenmehl&r auf den Topf bringt 400 bis 600 Ticks Wachstum, also 20 bis 30 Sekunden auf einen Schlag.",
              "",
              "Auch die Pflanzen aus Farmer's Delight gehen: Tomatensamen, Weißkohlsamen, Zwiebeln, Reis und die Pilzkolonien.",
          ],
          tasks=[task_item("farmersdelight:rich_soil", 4)],
          rewards=[reward_item("farmersdelight:rich_soil", 8), reward_item("minecraft:bone_meal", 16)],
          deps=["pot"], icon="farmersdelight:rich_soil"),

    quest("trees", 5, 6, "&aPflanz einen Baum in den Topf",
          subtitle="Botany Trees: Holz alle zwei Minuten.",
          description=[
              "Setz einen &6Eichensetzling&r auf Erde in einen Pflanztopf. Nach &e2 Minuten&r ist der Baum reif und gibt &e1 bis 4 Eichenstämme&r, dazu mit je 5 Prozent einen Setzling oder einen Apfel. Mit einer Schere im Werkzeugplatz kommen Blätter dazu.",
              "",
              "Das geht mit jedem Setzling im Pack: alle Vanilla-Bäume, die &dArchwood-Bäume&r von Ars Nouveau, die Bäume aus Biomes O' Plenty, Hexerei und Malum. Ein Trichter-Topf mit Setzling über einer Schublade ist eine Holzfarm ohne Sägen und ohne Kontraption.",
              "",
              "&eKronwerke:&r Holzkohle für die Create-Spieler, Bretter für Andesitgehäuse, Stämme für Mekanism-Stahl später: Holz braucht jeder, und vier Töpfe laufen leise neben der Küche.",
          ],
          tasks=[task_item("minecraft:oak_log", 32)],
          rewards=[reward_item("minecraft:oak_sapling", 8), reward_table("s1_common"), reward_xp(5)],
          deps=["hopper_pot", "soil"], icon="minecraft:oak_sapling", size=1.5),

    # ---- Productive Trees -------------------------------------------------------------
    quest("sawmill", 0, 11, "&6&lBau ein Sägewerk",
          subtitle="Sechs Bretter und Sägemehl aus jedem Stamm.",
          description=[
              "&eRezept:&r oben Bretter, &6Steinschneider&r, Bretter, in der Mitte drei &6Eisenbarren&r, unten drei Bretter. Das &6Sägewerk&r von &6Productive Trees&r braucht keinen Strom: Stamm hinein, warten, fertig.",
              "",
              "Jeder Stamm wird zu &e6 Brettern&r statt 4 an der Werkbank, dazu &e2 Sägemehl&r. Acht Sägemehl um einen Wassereimer ergeben zwei &6Papier&r, ein Buch mit einem Sägemehl das Handbuch des Mods.",
              "",
              pic("productivetrees:sawdust"),
              "",
              "Dazu gehört der &6Entrinder&r (Stripper), der mit einer Axt im Inneren Stämme entrindet, auch stapelweise. &6Zeit-Upgrades&r von Productive Lib machen beide Maschinen schneller.",
          ],
          tasks=[task_item("productivetrees:sawmill", 1)],
          rewards=[reward_item("minecraft:oak_log", 16), reward_table("s1_common"), reward_xp(5)],
          icon="productivetrees:sawmill", size=1.5, shape="hexagon"),

    quest("bees", 2.5, 10, "&eLass Bienen Bäume kreuzen",
          subtitle="Eiche und Birke ergeben Buche oder Linde.",
          description=[
              "Pflanz eine &6Eiche&r und eine &6Birke&r so, dass Blätter von beiden höchstens &e4 Blöcke&r von einem &6Bienennest&r oder &6Bienenstock&r entfernt sind, und setz Blumen daneben. Jedes Mal, wenn eine Biene von einer Blume heimkommt, versucht sie, ein Blatt in der Nähe zu bestäuben.",
              "",
              "Eiche und Birke ergeben mit 50 Prozent eine &6Buche&r oder mit 55 Prozent eine &6Silberlinde&r. Weitere Paare aus Vanilla-Bäumen: Fichte und Birke die &6Europäische Lärche&r (10 Prozent), Schwarzeiche und Tropenbaum &6Teak&r (40), Tropenbaum und Kirsche &6Kakao&r (35), Kirsche und Eiche den &6Red-Delicious-Apfelbaum&r (10).",
              "",
              "Bestäubte Blätter erkennst du mit dem &6Fernrohr&r. Aus ihnen kommt der Setzling der neuen Art. Pflanz ihn, und du hast einen Baum, den es in dieser Welt sonst nirgends gibt.",
          ],
          tasks=[task_item("productivetrees:beech_sapling", 1)],
          rewards=[reward_item("minecraft:birch_sapling", 4), reward_item("minecraft:oak_sapling", 4), reward_xp(5)],
          deps=["sawmill"], icon="minecraft:bee_nest"),

    quest("sifter", 2.5, 12, "&eSieb Pollen aus Blättern",
          subtitle="Kreuzen ohne Bienen.",
          description=[
              "&eRezept auf Kronwerke:&r oben Bretter, &6Klebriger Kolben&r, Bretter, in der Mitte Eisenbarren, &6Pinsel&r, Eisenbarren, unten drei Bretter. Die Mod lässt das Rezept weg, sobald Productive Bees dabei ist, Kronwerke gibt es zurück. Der &6Pollensieber&r holt aus Blättern &6Pollen&r der jeweiligen Baumart heraus.",
              "",
              pic("productivetrees:pollen"),
              "",
              "Klick mit dem Pollen auf ein Blatt eines anderen Baums, und es ist bestäubt, als wäre eine Biene da gewesen. JEI zeigt unter &eBaumbestäubung&r, welcher Pollen auf welches Blatt gehört. So kreuzt du gezielt, auch unter Tage und ohne Blumenwiese.",
          ],
          tasks=[task_item("productivetrees:pollen_sifter", 1)],
          rewards=[reward_item("minecraft:brush", 1), reward_xp(3)],
          deps=["sawmill"], icon="productivetrees:pollen_sifter"),

    quest("nuts", 5, 11, "&6Ernte Nüsse und Obst",
          subtitle="Bäume, die mehr geben als Holz.",
          description=[
              "Die &6Buche&r trägt &6Bucheckern&r, drei pro reifem Blatt, und der Red-Delicious-Apfelbaum zwei &6Äpfel&r. Früchte reifen an den Blättern, du siehst es an der Farbe, und mit Rechtsklick pflückst du sie, der Baum bleibt stehen.",
              "",
              "Nüsse schmeckst du im Ofen oder Räucherofen zu &6Gerösteten Bucheckern&r, Hasel-, Wal-, Pekannüssen und mehr, je nach Baum. Neun Nüsse werden zu einer Kiste, die sich als ganze rösten lässt.",
              "",
              "Insgesamt tragen 83 der Baumarten Obst oder Nüsse: Zitronen, Bananen, Kirschen, Pflaumen, Mandeln, Kaffee. Jede davon ist ein Setzling, den du erst kreuzen musst.",
          ],
          tasks=[task_item("productivetrees:roasted_beechnut", 8)],
          rewards=[reward_item("minecraft:apple", 8), reward_table("s1_common")],
          deps=["bees"], icon="productivetrees:roasted_beechnut"),

    quest("hybrids", 7.5, 11, "&dAusblick: Hybriden und Fundstücke",
          subtitle="148 Kreuzungen, sechs Setzlinge aus Truhen.",
          description=[
              "Productive Trees hat &e148 Kreuzungen&r und 163 Baumarten. Fast jede neue Art ist ein Elternteil für die nächste: Buche und Birke ergeben die Erle, und so weiter bis zu Mahagoni, Ebenholz, Zuckerahorn und dem Gummibaum. JEI unter Baumbestäubung ist dein Stammbaum.",
              "",
              "Sechs Setzlinge wachsen nicht aus Kreuzungen, sondern liegen in Truhen: &6Blue Yonder&r in Schiffswrack-Schatztruhen, &6Flickering Sun&r in Wüstentempeln, &6Firecracker&r in Antiken Städten, &6Brown Amber&r beim Ausgraben in kalten Ozeanruinen. &6Black Ember&r (Bastionen) kommt mit dem Nether in Stufe 2, &6Soul Tree&r (Endsiedlungen) mit dem End in Stufe 4.",
              "",
              "&eStufe 2:&r &6Productive Bees&r öffnet. Ein fortgeschrittener Bienenstock mit dem &6Pollensieb-Upgrade&r sammelt Pollen nebenbei, und die &6Allergie-Biene&r ist darauf spezialisiert.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["nuts", "sifter"], icon="productivetrees:pollen", optional=True),

    # ---- Die besten Mahlzeiten ------------------------------------------------------
    quest("stuffed_pumpkin", 10.5, 6.5, "&6&lTisch den gefüllten Kürbis auf",
          subtitle="Das stärkste Essen im Pack, und ein Überblick, was sonst noch satt macht.",
          description=[
              "Leg in den &6Kochtopf&r: &6Reis&r, &6Zwiebel&r, &6Brauner Pilz&r, &6Kartoffel&r, eine &6Beere&r und ein weiteres Gemüse, als Behälter einen ganzen &6Kürbis&r. Nach 20 Sekunden kommt der &6Gefüllte Kürbis&r heraus, ein Festmahl-Block, aus dem jeder mit einer Schüssel Portionen holt.",
              "",
              pic("farmersdelight:stuffed_pumpkin"),
              "",
              "&eDie Spitze:&r 14 Hunger und 21 Sättigung bringen alle Festmahl-Portionen (Gefüllter Kürbis, Backhähnchen, Hirtenkuchen, Honigglasierter Schinken, Gleaming Salad), dazu Gemüsenudeln, Pasta mit Tintenfischtinte, Kürbissuppe, Nudelsuppe, Gebackener Kabeljaueintopf, Gebratene Hammelkoteletts, Gegrillter Lachs und der Kanincheneintopf, den Farmer's Delight aufwertet.",
              "",
              "&eZum Vergleich:&r Gemüsesuppe, Rindfleischeintopf und Gebratener Reis bringen 12 Hunger und 19,2 Sättigung, der Hamburger 11 und 17,6, Steak 8 und 12,8, die Goldene Karotte 6 und 14,4. Der Quellbeerenkuchen von Ars Nouveau liegt bei 9 und 16,2, der Honigapfel von Create bei 8 und 12,8.",
              "",
              "Die Quests daneben sind eine Checkliste: je vier Portionen der sieben Spitzengerichte, die nicht schon im Kapitel Essen stehen. Der Kochtisch mit vollen Schränken macht das zu einem Klick pro Gericht.",
          ],
          tasks=[task_item("farmersdelight:stuffed_pumpkin_block", 1)],
          rewards=[reward_table("s1_rare"), reward_item("minecraft:bowl", 16), reward_xp(15)],
          deps=["table", "trees", "nuts"], icon="farmersdelight:stuffed_pumpkin_block", size=2.5, shape="gear"),

    meal("m_noodles", 13.5, 4.5, "&6Koch Gemüsenudeln", "farmersdelight:vegetable_noodles",
         "Kochtopf: &6Karotte&r, ein &6Pilz&r, &6Rohe Nudeln&r, ein Blattgemüse (Kohl oder Kohlblatt) und ein weiteres Gemüse, Schüssel.",
         reward=reward_item("farmersdelight:raw_pasta", 8)),

    meal("m_squid", 13.5, 6, "&6Koch Pasta mit Tintenfischtinte", "farmersdelight:squid_ink_pasta",
         "Kochtopf: ein &6roher Fisch&r (Kabeljau oder Lachs), &6Rohe Nudeln&r, &6Tomate&r und ein &6Tintenbeutel&r, Schüssel."),

    meal("m_pumpkin", 13.5, 7.5, "&6Koch Kürbissuppe", "farmersdelight:pumpkin_soup",
         "Kochtopf: &6Kürbisscheibe&r, ein Blattgemüse, &6rohes Schweinefleisch&r und &6Milch&r, Schüssel. Die Kürbisscheibe schneidest du am Schneidebrett.",
         reward=reward_item("minecraft:pumpkin", 4)),

    meal("m_noodle_soup", 13.5, 9, "&6Koch Nudelsuppe", "farmersdelight:noodle_soup",
         "Kochtopf: &6Rohe Nudeln&r, ein &6Ei&r, &6Getrockneter Seetang&r und &6rohes Schweinefleisch&r, Schüssel."),

    meal("m_cod", 16, 4.5, "&6Koch Kabeljaueintopf", "farmersdelight:baked_cod_stew",
         "Kochtopf: &6Roher Kabeljau&r, &6Kartoffel&r, ein &6Ei&r und eine &6Tomate&r, Schüssel.",
         reward=reward_item("minecraft:cod", 8)),

    meal("m_mutton", 16, 6, "&6Richte Hammelkoteletts an", "farmersdelight:roasted_mutton_chops",
         "Werkbank, formlos: &6Gebratene Hammelkoteletts&r, &6Rote Bete&r, &6Gekochter Reis&r, &6Tomate&r und eine Schüssel. Koteletts schneidest du mit dem Messer aus Hammelfleisch und brätst sie im Ofen.",
         reward=reward_table("s1_common")),

    meal("m_salmon", 16, 7.5, "&6Richte gegrillten Lachs an", "farmersdelight:grilled_salmon",
         "Werkbank, formlos: &6Gebratener Lachs&r, &6Süßbeeren&r, &6Weißkohl&r, &6Zwiebel&r und eine Schüssel.",
         reward=reward_item("minecraft:sweet_berries", 8)),
]

images = [
    banner("cooking/title", "Kochen", 7, -4.6, height=1.8, kind="title", colour="fire"),
    banner("cooking/kitchen", "Die Küche", 6.25, -1.7, height=0.9, colour="fire"),
    banner("cooking/pots", "Blumentöpfe", 2.5, 3.6, height=0.9, colour="nature"),
    banner("cooking/trees", "Productive Trees", 3.75, 8.6, height=0.9, colour="nature"),
    banner("cooking/meals", "Die besten Mahlzeiten", 13.5, 2.8, height=0.9, colour="brass"),
]

chapter(C, "Kochen", "cookingforblockheads:cooking_table", "world", quests, shape="circle", order=59,
        subtitle=["Die Blockhead-Küche, Pflanztöpfe, Productive Trees und die Mahlzeiten mit der meisten Sättigung."],
        images=images)
