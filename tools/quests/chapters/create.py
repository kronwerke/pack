"""Create in stage 1 (Steinwerk): from the first andesite to an andesite alloy line for the obelisk.

Everything here is open on day one: andesite machines, water wheels and windmills, press,
millstone, mixer without heat, fans, belts, funnels, the Create 6 package logistics, pipes and
the first contraptions. Brass, the blaze burner, deployers, crafters and trains are stage 2
(create_brass.py and create_trains.py). Stress numbers come from config/create-server.toml,
recipes from the Create jar and kubejs/server_scripts/kronwerke/create.js."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def cost(name, x, y, title, subtitle, line, icon):
    """One line of the stress checklist."""
    return quest(name, x, y, title, subtitle=subtitle, description=[line],
                 tasks=[task_checkmark("Abgehakt")], rewards=[reward_xp(1)],
                 deps=["stress"], icon=icon, optional=True)


# Two columns of sections. Column A starts at x 0, column B at x 21.
A, B = 0, 21

quests = [
    # ---- Grundlagen -------------------------------------------------------
    quest("welcome", A, 2.5, "&6&lFang mit Create an",
          subtitle="Drehbewegung statt Strom: so läuft hier jede Maschine.",
          description=[
              "Halte über einem Create-Block im Inventar oder in JEI die Taste &eW&r gedrückt. Dann öffnet sich die &6Ponder&r-Ansicht, eine kleine animierte Anleitung zu genau diesem Block.",
              "",
              "Create erzeugt keinen Strom, sondern &dRotation&r. Wasserräder und Windmühlen drehen Wellen und Zahnräder, die treiben Maschinen an, die mahlen, pressen, mischen und ganze Bauwerke bewegen.",
              "",
              "&eStufe 1&r öffnet die Andesit-Hälfte: Wasserräder, Presse, Mixer ohne Hitze, Bänder, Lüfter, Rohre, Pakete und die ersten Kontraptionen. Messing, Lohenbrenner, Einsatzgeräte und Züge kommen in &6Stufe 2&r.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler des Obelisken will in dieser Stufe &61 500 Andesitlegierungen&r (für 30 Spieler) und &612 Steinwerk-Getriebe&r. Am Ende dieses Kapitels steht eine Fabrik, die beides liefert.",
          ],
          tasks=[task_checkmark("Los geht's")],
          rewards=[reward_item("create:andesite_alloy", 8), reward_table("s1_common")],
          icon="create:large_cogwheel", size=2.0, shape="hexagon"),

    quest("andesite", A + 2.5, 1.5, "&6Bau Andesit ab",
          subtitle="Der graue Stein, aus dem fast alles hier entsteht.",
          description=[
              "Grab &664 Andesit&r. Er liegt in großen Adern im Stein, oft neben Granit und Diorit. Jede Spitzhacke reicht.",
              "",
              "Du brauchst ihn zu Hunderten. Später verdichtet eine Presse über einem Becken neuen Andesit aus Feuerstein, Kies und Lava (Quest &6Verdichte Andesit&r).",
          ],
          tasks=[task_item("minecraft:andesite", 64)],
          rewards=[reward_item("minecraft:iron_nugget", 18), reward_xp(2)],
          deps=["welcome"]),

    quest("zinc", A + 2.5, 3.5, "&6Schmilz Zink",
          subtitle="Das zweite Metall von Create.",
          description=[
              "Bau &6Zinkerz&r ab (im Stein und als Tiefenschiefer-Zinkerz) und schmilz das &6Rohzink&r im Ofen. Ein Barren gibt neun &6Zinkklumpen&r.",
              pic("create:raw_zinc"),
              "Zinkklumpen gehen statt Eisenklumpen in die Andesitlegierung. Das schont dein Eisen für Bleche und Werkzeug.",
              "",
              "In Stufe 2 wird aus Zink und doppelt so viel Kupfer &6Messing&r, und der Obelisk will dann 2 000 Barren. Eine Kiste Rohzink jetzt ist ein Vorsprung später.",
          ],
          tasks=[task_item("create:raw_zinc", 16)],
          rewards=[reward_item("create:zinc_ingot", 4), reward_xp(3)],
          deps=["welcome"]),

    quest("andesite_alloy", A + 5, 2.5, "&6Misch Andesitlegierung von Hand",
          subtitle="Das Herz jeder Maschine dieser Stufe.",
          description=[
              "Zwei &6Andesit&r und zwei &6Eisenklumpen&r (oder Zinkklumpen) schräg gegenüber im 2 x 2 Raster ergeben eine &6Andesitlegierung&r.",
              pic("create:andesite_alloy"),
              "&eRezept auf Kronwerke:&r Von Hand bleibt es bei einer Legierung pro Rezept. Der &6Mechanische Mixer&r macht aus einem Andesit und einem Klumpen gleich &ezwei&r, also viermal so sparsam.",
              "",
              "Aus Legierung entstehen Wellen, Gehäuse, Schleusen und fast alles andere in diesem Kapitel.",
          ],
          tasks=[task_item("create:andesite_alloy", 32)],
          rewards=[reward_item("minecraft:iron_nugget", 32), reward_table("s1_common")],
          deps=["andesite"], icon="create:andesite_alloy", size=1.75, shape="gear"),

    quest("casing", A + 7.5, 1.5, "&6Ummantel Holz mit Legierung",
          subtitle="Andesitgehäuse, das Gerüst fast aller Maschinen.",
          description=[
              "Setz einen &6entrindeten Stamm&r ab und rechtsklicke ihn mit einer &6Andesitlegierung&r. Er wird zum &6Andesitgehäuse&r. Entrindetes Holz geht genauso.",
              "",
              "Mahlstein, Presse, Mixer, Lüfter, Getriebe, Kolben und Depot haben ein Gehäuse im Rezept. Ein Stapel Stämme im Vorrat spart Laufwege.",
              "",
              "&6Tipp:&r Mit einem Gehäuse in der Hand auf eine Welle oder ein Band geklickt, wird sie ummantelt.",
          ],
          tasks=[task_item("create:andesite_casing", 8)],
          rewards=[reward_item("minecraft:oak_log", 16), reward_xp(2)],
          deps=["andesite_alloy"]),

    quest("shaft", A + 7.5, 3.5, "&6Leg eine Welle",
          subtitle="Die einfachste Leitung für Drehbewegung.",
          description=[
              "Zwei &6Andesitlegierungen&r übereinander ergeben acht &6Wellen&r. Eine Welle gibt Rotation in gerader Linie weiter, ohne Verlust.",
              "",
              "Um die Ecke kommst du nur mit Zahnrädern oder einem Getriebe. Mit dem Schraubenschlüssel drehst du eine gesetzte Welle.",
              "",
              "&6Tipp:&r Die &6Mechanische Säge&r macht aus einer Legierung sechs Wellen, die Werkbank nur vier.",
          ],
          tasks=[task_item("create:shaft", 16)],
          rewards=[reward_item("create:andesite_alloy", 4), reward_xp(2)],
          deps=["andesite_alloy"]),

    quest("cogwheel", A + 10, 3.5, "&6Steck Zahnräder zusammen",
          subtitle="Klein und groß, und dazwischen die Drehzahl.",
          description=[
              "&6Zahnrad&r: eine Welle und ein Brett. &6Großes Zahnrad&r: eine Welle und zwei Bretter, oder ein Zahnrad und ein Brett.",
              "",
              "Zwei kleine nebeneinander geben die Drehung seitwärts weiter, die Richtung kehrt sich um. Ein großes treibt ein kleines schräg versetzt an und &everdoppelt&r dabei die Drehzahl, andersherum halbiert sie sich.",
          ],
          tasks=[task_item("create:cogwheel", 8), task_item("create:large_cogwheel", 4)],
          rewards=[reward_item("create:cogwheel", 4), reward_xp(3)],
          deps=["shaft"]),

    quest("gearbox", A + 10, 1.5, "&6Bau ein Getriebe",
          subtitle="Rotation in alle vier Richtungen.",
          description=[
              "Vier &6Zahnräder&r um ein &6Andesitgehäuse&r ergeben ein &6Getriebe&r. Es nimmt Rotation an einer Seite an und gibt sie an die anderen weiter, auch um 90 Grad.",
              "",
              "Die gegenüberliegende Seite dreht andersherum. Liegend heißt es &6Vertikales Getriebe&r, im Raster wandelst du das eine ins andere um. Getriebe kosten keine Belastbarkeit.",
          ],
          tasks=[task_item("create:gearbox", 2)],
          rewards=[reward_item("create:andesite_casing", 4), reward_xp(3)],
          deps=["cogwheel", "casing"]),

    # ---- Energie ----------------------------------------------------------
    quest("hand_crank", A, 9, "&6Dreh die Handkurbel",
          subtitle="Muskelkraft zum Ausprobieren.",
          description=[
              "Drei &6Bretter&r und eine &6Andesitlegierung&r ergeben eine &6Handkurbel&r. Halte die rechte Maustaste auf ihr: sie liefert &d32 RPM&r und &d256 SU&r.",
              "",
              "Kurbeln macht hungrig. Gut, um einen Aufbau zu testen, bevor das Wasserrad steht.",
          ],
          tasks=[task_item("create:hand_crank", 1)],
          rewards=[reward_item("minecraft:bread", 6), reward_xp(2)],
          deps=["andesite_alloy"]),

    quest("water_wheel", A + 2.5, 9, "&6Stell ein Wasserrad in den Bach",
          subtitle="Deine erste echte Kraftquelle.",
          description=[
              "Acht &6Bretter&r um eine &6Welle&r ergeben ein &6Wasserrad&r. Setz es so, dass &bfließendes Wasser&r über seine Schaufeln läuft, am besten von oben auf eine Seite.",
              "",
              "Ein Rad liefert &d8 RPM&r und &d256 SU&r (32 SU pro RPM). Mehrere Räder auf einer Welle addieren ihre SU, nicht die Drehzahl. Vier Räder an einem Bach sind ein solider Start.",
              "",
              "&cHäufiger Fehler:&r Das Wasser fließt unter dem Rad durch. Stehendes Wasser dreht nichts. Die Holzsorte ist nur Optik.",
          ],
          tasks=[task_item("create:water_wheel", 4)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_table("s1_common")],
          deps=["shaft"], icon="create:water_wheel", size=1.75, shape="gear"),

    quest("large_water_wheel", A + 5, 8, "&6Bau ein Großes Wasserrad",
          subtitle="Halbe Drehzahl, doppelte Kraft.",
          description=[
              "Ein &6Wasserrad&r und acht &6Bretter&r ergeben das &6Große Wasserrad&r, 3 x 3 Blöcke groß. Es dreht mit &d4 RPM&r und liefert &d512 SU&r (128 SU pro RPM).",
              "",
              "Die Drehzahl holst du mit Zahnrädern zurück: großes auf kleines macht 8 RPM, noch eine Stufe 16. Die SU bleiben dabei gleich.",
          ],
          tasks=[task_item("create:large_water_wheel", 1)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["water_wheel"]),

    quest("sails", A + 5, 10, "&6Näh Windmühlen-Segel",
          subtitle="Acht Segel sind das Minimum.",
          description=[
              "&6Wolle&r, zwei &6Stöcke&r und eine &6Andesitlegierung&r ergeben zwei &6Windmühlen-Segel&r. Für eine Mühle brauchst du mindestens &e8&r.",
              "",
              "Mit Farbstoff färbst du sie ein. Ohne Wolle gibt es den &6Segelrahmen&r, der genauso zählt.",
          ],
          tasks=[task_item("create:white_sail", 8)],
          rewards=[reward_item("minecraft:white_wool", 16), reward_xp(2)],
          deps=["water_wheel"]),

    quest("windmill", A + 7.5, 10, "&6Lass die Windmühle laufen",
          subtitle="Kraft ohne Wasser, nur mit Platz.",
          description=[
              "&6Windmühlenlager&r: Holzstufe, Stein, Welle. Bau die Segel vor seine Vorderseite, verbinde alles mit &6Sekundenkleber&r und rechtsklicke das Lager.",
              "",
              "Je &e8 Segel&r bringen &d1 RPM&r, und jedes RPM trägt &d512 SU&r. 32 Segel laufen mit 4 RPM und tragen 2 048 SU, so viel wie acht Wasserräder.",
              "",
              "Rund um die Segel darf nichts im Weg stehen. Die Drehrichtung stellst du am Wertefeld des Lagers ein.",
          ],
          tasks=[task_item("create:windmill_bearing", 1)],
          rewards=[reward_item("create:super_glue", 1), reward_table("s1_common")],
          deps=["sails"], icon="create:windmill_bearing", size=1.5),

    quest("stress", A + 7.5, 8, "&dVersteh RPM und SU",
          subtitle="Quellen liefern SU, Maschinen verbrauchen sie.",
          description=[
              "Jede Maschine hat einen Verbrauch pro RPM. &eVerbrauch = Wert mal Drehzahl.&r Die Presse kostet 8 SU pro RPM, bei 32 RPM also 256 SU: genau ein Wasserrad.",
              "",
              "Ist der Verbrauch größer als die Quellen liefern, ist das Netz &cüberlastet&r und alles steht. Dann hilft mehr Quelle, weniger Drehzahl oder ein zweites Netz.",
              "",
              "Ab &d30 RPM&r gilt eine Drehzahl als mittel, ab &d100&r als schnell, das Maximum ist &d256&r. Wellen, Zahnräder, Getriebe und Bänder kosten nichts. Was jede Maschine kostet, steht im Abschnitt darunter.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["water_wheel"], icon="create:stressometer", shape="diamond"),

    quest("speedometer", A + 10, 8, "&6Miss Drehzahl und Belastung",
          subtitle="Tachometer und Stressmesser.",
          description=[
              "Ein &6Kompass&r auf einem &6Andesitgehäuse&r ergibt den &6Tachometer&r. Allein ins Raster gelegt wird er zum &6Stressmesser&r und zurück.",
              "",
              "Der Tachometer zeigt die Drehzahl an seiner Stelle, der Stressmesser die freie Belastbarkeit des ganzen Netzes. Beide geben ein Redstone-Signal aus, ein Komparator liest es.",
          ],
          tasks=[task_item("create:speedometer", 1), task_item("create:stressometer", 1)],
          rewards=[reward_item("minecraft:redstone", 8), reward_xp(3)],
          deps=["stress"]),

    quest("clutch_gearshift", A + 10, 10, "&6Schalt eine Welle ab",
          subtitle="Die Kupplung trennt bei Redstone.",
          description=[
              "&6Andesitgehäuse&r, &6Welle&r und &6Redstone&r ergeben eine &6Kupplung&r. Solange sie ein &cRedstone-Signal&r bekommt, steht alles dahinter still.",
              "",
              "Alles davor läuft weiter. So hältst du eine Anlage an, ohne das ganze Netz zu stoppen.",
              "",
              "&6Tipp:&r Der &6Ummantelte Kettenriemen&r (Gehäuse und drei Eisen- oder Zinkklumpen) gibt Rotation an Kettenriemen direkt daneben weiter, auch um die Ecke.",
          ],
          tasks=[task_item("create:clutch", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(3)],
          deps=["gearbox"]),

    quest("gearshift", A + 12.5, 10, "&6Kehr die Drehrichtung um",
          subtitle="Die Gangschaltung, vor und zurück per Hebel.",
          description=[
              "&6Andesitgehäuse&r, &6Zahnrad&r und &6Redstone&r ergeben eine &6Gangschaltung&r. Mit Redstone-Signal dreht alles dahinter andersherum.",
              "",
              "Damit fahren Kolben, Flaschenzüge und Portalkräne per Hebel vor und zurück.",
          ],
          tasks=[task_item("create:gearshift", 1)],
          rewards=[reward_item("minecraft:lever", 4), reward_xp(3)],
          deps=["clutch_gearshift"]),

    # ---- Belastung: jede Maschine -----------------------------------------
    cost("cost_press", A, 13.5, "&7Presse: 8 SU pro RPM",
         "Die teuerste Maschine dieser Stufe.",
         "&6Mechanische Presse&r: &d8 SU pro RPM&r. Bei 16 RPM 128 SU, bei 32 RPM 256 SU.",
         "create:mechanical_press"),
    cost("cost_millstone", A + 2, 13.5, "&7Mahlstein: 4 SU pro RPM",
         "Mahlt bei wenig Drehzahl gemütlich.",
         "&6Mahlstein&r: &d4 SU pro RPM&r. Bei 32 RPM 128 SU, ein Wasserrad trägt also zwei.",
         "create:millstone"),
    cost("cost_mixer", A + 4, 13.5, "&7Mixer: 4 SU pro RPM",
         "Der Legierungsmacher.",
         "&6Mechanischer Mixer&r: &d4 SU pro RPM&r. Bei 64 RPM 256 SU, ein Wasserrad pro Mixer.",
         "create:mechanical_mixer"),
    cost("cost_saw", A + 6, 13.5, "&7Säge: 4 SU pro RPM",
         "Auch an einer Kontraption.",
         "&6Mechanische Säge&r: &d4 SU pro RPM&r. Bei 32 RPM 128 SU.",
         "create:mechanical_saw"),
    cost("cost_drill", A + 8, 13.5, "&7Bohrer: 4 SU pro RPM",
         "Schneller bohren heißt mehr SU.",
         "&6Mechanischer Bohrer&r: &d4 SU pro RPM&r. Vier Bohrer bei 32 RPM: 512 SU, zwei Wasserräder.",
         "create:mechanical_drill"),
    cost("cost_pump", A + 10, 13.5, "&7Pumpe: 4 SU pro RPM",
         "Mehr Drehzahl, mehr Durchfluss.",
         "&6Mechanische Pumpe&r: &d4 SU pro RPM&r. Bei 64 RPM 256 SU.",
         "create:mechanical_pump"),
    cost("cost_fan", A + 12, 13.5, "&7Lüfter: 2 SU pro RPM",
         "Der günstigste Verarbeiter.",
         "&6Ummantelter Lüfter&r: &d2 SU pro RPM&r. Bei 128 RPM 256 SU.",
         "create:encased_fan"),
    cost("cost_contraption", A + 14, 13.5, "&7Lager und Kolben: 4 SU pro RPM",
         "Kontraptionen kosten wie ein Mahlstein.",
         "&6Mechanisches Lager&r, &6Kolben&r, &6Flaschenzug&r und &6Drehtisch&r: je &d4 SU pro RPM&r. Der &6Kettenförderer&r 1, der &6Gewichtete Werfer&r 2.",
         "create:mechanical_bearing"),

    # ---- Verarbeitung -------------------------------------------------------
    quest("millstone", A, 18, "&6Mahl im Mahlstein",
          subtitle="Deine erste Maschine.",
          description=[
              "&6Zahnrad&r, &6Andesitgehäuse&r und &6Stein&r ergeben den &6Mahlstein&r. Treib ihn von der Seite oder von oben an und wirf Items oben hinein.",
              "",
              "&6Weizen&r wird zu &6Weizenmehl&r, &6Bruchstein&r zu &6Kies&r, Kies zu &6Feuerstein&r, Andesit zu Bruchstein, Blumen zu doppelt so viel Farbstoff. Alles Weitere zeigt JEI.",
              "",
              "Rechtsklick holt das Ergebnis heraus, eine Andesitschleuse an der Seite zieht es ab. Erze zerkleinern erst die Mahlwerkräder aus Stufe 2.",
          ],
          tasks=[task_item("create:millstone", 1)],
          rewards=[reward_item("minecraft:wheat", 16), reward_table("s1_common")],
          deps=["water_wheel"]),

    quest("press", A + 2.5, 18, "&6Bau die Mechanische Presse",
          subtitle="Ein Stempel für Bleche.",
          description=[
              "&6Welle&r, &6Andesitgehäuse&r und ein &6Eisenblock&r untereinander ergeben die &6Mechanische Presse&r. Rotation bekommt sie von oben oder von der Seite.",
              "",
              "Sie kostet &d8 SU pro RPM&r. Plan für eine Presse bei 32 RPM ein ganzes Wasserrad ein, besser zwei.",
          ],
          tasks=[task_item("create:mechanical_press", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["water_wheel", "casing"], icon="create:mechanical_press", size=1.5),

    quest("depot", A + 5, 18, "&6Stell ein Depot unter die Presse",
          subtitle="Die Ablage, auf die der Stempel fällt.",
          description=[
              "&6Andesitlegierung&r und &6Andesitgehäuse&r ergeben ein &6Depot&r. Setz es zwei Blöcke unter die Presse, mit einem Block Luft dazwischen.",
              "",
              "Leg ein Item per Rechtsklick darauf. Statt eines Depots geht auch ein laufendes Förderband: dann presst sie alles, was darunter durchfährt.",
          ],
          tasks=[task_item("create:depot", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["press"]),

    quest("sheets", A + 7.5, 18, "&6Press Bleche",
          subtitle="Eisen, Kupfer und Gold werden flach.",
          description=[
              "Leg &6Eisenbarren&r, &6Kupferbarren&r und &6Goldbarren&r aufs Depot unter der Presse. Jeder Barren wird zu einem Blech.",
              pic("create:iron_sheet"),
              "&6Eisenblech&r: Propeller, Rührstab, Schacht, Sekundenkleber. &6Kupferblech&r: Rohre und Tanks. &6Goldblech&r: Brille, Schraubenschlüssel, Werfer.",
          ],
          tasks=[task_item("create:iron_sheet", 16), task_item("create:copper_sheet", 8), task_item("create:golden_sheet", 4)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_table("s1_common")],
          deps=["depot"], icon="create:iron_sheet", size=1.5, shape="gear"),

    quest("whisk", A + 10, 18, "&6Bieg einen Rührstab",
          subtitle="Das Werkzeug im Mixer.",
          description=[
              "Fünf &6Eisenbleche&r und zwei &6Andesitlegierungen&r ergeben einen &6Rührstab&r: Legierung oben, Blech, Legierung, Blech in der Mitte, drei Bleche unten.",
          ],
          tasks=[task_item("create:whisk", 1)],
          rewards=[reward_item("create:iron_sheet", 4), reward_xp(3)],
          deps=["sheets"]),

    quest("basin", A + 12.5, 18, "&6Stell ein Becken auf",
          subtitle="Darin wird gemischt und verdichtet.",
          description=[
              "Fünf &6Andesitlegierungen&r in U-Form ergeben ein &6Becken&r. Es nimmt Items und Flüssigkeiten auf, von Hand, per Schacht, Schleuse oder Rohr.",
              "",
              "Über dem Becken arbeitet der Mixer oder die Presse. Das Ergebnis bleibt im Becken, bis eine Schleuse an der Seite es herausholt.",
          ],
          tasks=[task_item("create:basin", 1)],
          rewards=[reward_item("create:andesite_alloy", 8), reward_xp(3)],
          deps=["whisk"]),

    quest("mixer", A + 15, 18, "&6Bau den Mechanischen Mixer",
          subtitle="Rühren statt kneten.",
          description=[
              "&6Zahnrad&r, &6Andesitgehäuse&r und &6Rührstab&r untereinander ergeben den &6Mechanischen Mixer&r. Setz ihn zwei Blöcke über das Becken, mit einem Block Luft dazwischen.",
              "",
              "Ohne Hitze kann er: zwei Legierungen aus Andesit und Klumpen, &6Teig&r aus Mehl und Wasser, &6Zellstoff&r für Karton, &6Schlamm&r und viele formlose Rezepte.",
              "",
              "Rezepte mit &cErhitzt&r oder &cÜberhitzt&r in JEI brauchen einen &6Lohenbrenner&r unter dem Becken. Der kommt in Stufe 2, mit ihm auch Messing.",
          ],
          tasks=[task_item("create:mechanical_mixer", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["basin"], icon="create:mechanical_mixer", size=2.0, shape="gear"),

    quest("alloy_mixing", A + 17.5, 18, "&6Misch Legierung am Band",
          subtitle="Doppelte Legierung, ein Viertel des Materials.",
          description=[
              "Ein &6Andesit&r und ein &6Eisen-&r oder &6Zinkklumpen&r ins Becken: der Mixer macht &ezwei Andesitlegierungen&r daraus.",
              "",
              "So baust du es: je eine Kiste Andesit und Klumpen mit einer Andesitschleuse, die aufs Band zum Becken legt. Eine Schleuse an der Beckenseite lädt die Legierung in eine Ausgabekiste.",
              "",
              "&cStockt es?&r Meist fehlt eine Zutat, oder die Ausgabeschleuse sitzt falsch herum und das Becken ist voll.",
          ],
          tasks=[task_item("create:andesite_alloy", 256)],
          rewards=[reward_item("minecraft:andesite", 64), reward_table("s1_uncommon")],
          deps=["mixer"]),

    quest("wrench", A + 5, 20, "&6Greif zum Schraubenschlüssel",
          subtitle="Drehen, umbauen, einsammeln.",
          description=[
              "Drei &6Goldbleche&r, ein &6Zahnrad&r und ein &6Stock&r ergeben den &6Schraubenschlüssel&r. Rechtsklick dreht einen Create-Block, Schleichen und Rechtsklick hebt ihn sofort auf.",
              pic("create:wrench"),
              "Damit polst du Schleusen um und stellst Kontraptionen ein. Gehört in jede Hotbar.",
          ],
          tasks=[task_item("create:wrench", 1)],
          rewards=[reward_xp(3)],
          deps=["sheets"]),

    quest("goggles", A + 7.5, 20, "&6Setz die Ingenieursbrille auf",
          subtitle="Sieh, warum eine Anlage steht.",
          description=[
              "&6Faden&r, zwei &6Glas&r und ein &6Goldblech&r ergeben die &6Ingenieursbrille&r. Schau damit auf eine Maschine: Drehzahl, SU, Verbrauch und Tankinhalte werden eingeblendet.",
              pic("create:goggles"),
              "Ohne Brille baust du blind. Im Raster mit einem Helm kombiniert, sitzt sie fest darauf, und der Helm schützt weiter.",
          ],
          tasks=[task_item("create:goggles", 1)],
          rewards=[reward_xp(5)],
          deps=["sheets"]),

    quest("compacting", A + 12.5, 20, "&6Verdichte Andesit",
          subtitle="Andesit, der nie ausgeht.",
          description=[
              "Setz die &6Presse&r über ein &6Becken&r statt über ein Depot. Zwei &6Feuerstein&r, ein &6Kies&r und &b100 mB Lava&r werden zu einem &6Andesit&r verdichtet.",
              "",
              "Den Feuerstein liefern Mahlstein und Kieswäsche, die Lava eine Pumpe aus einem Lavasee. Über dem Becken verdichtet die Presse auch neun Barren zu einem Block.",
          ],
          tasks=[task_item("minecraft:andesite", 128)],
          rewards=[reward_item("minecraft:lava_bucket", 1), reward_table("s1_uncommon")],
          deps=["basin"], icon="minecraft:andesite"),

    quest("saw", A + 2.5, 22, "&6Säg Holz mit der Säge",
          subtitle="Mehr Bretter, und alles vom Steinschneider.",
          description=[
              "Drei &6Eisenbleche&r, ein &6Eisenbarren&r und ein &6Andesitgehäuse&r ergeben die &6Mechanische Säge&r. Nach oben zeigend verarbeitet sie, was auf ihr landet oder auf dem Band durchläuft.",
              "",
              "Stämme geben mehr Bretter als in der Werkbank, und sie kann jedes Steinschneider-Rezept. Bei mehreren Ergebnissen wählst du mit einem &6Listenfilter&r (Eisenklumpen und Wolle).",
          ],
          tasks=[task_item("create:mechanical_saw", 1)],
          rewards=[reward_item("minecraft:oak_log", 32), reward_xp(3)],
          deps=["sheets"]),

    quest("fan", A + 7.5, 22, "&6Bau einen Lüfter",
          subtitle="Wind, der Items verarbeitet.",
          description=[
              "&6Welle&r, &6Andesitgehäuse&r und &6Propeller&r (vier Eisenbleche um eine Legierung) ergeben den &6Ummantelten Lüfter&r. Er bläst oder saugt bis zu &e20 Blöcke&r weit.",
              "",
              "Ein Block direkt vor der Öffnung macht ihn zur Maschine: &bWasser&r wäscht, &cLava&r schmilzt, &6Feuer&r räuchert Essen. Seelenfeuer zum Heimsuchen braucht Seelensand aus dem Nether, also Stufe 2.",
          ],
          tasks=[task_item("create:encased_fan", 1)],
          rewards=[reward_item("minecraft:gravel", 32), reward_table("s1_common")],
          deps=["sheets"], icon="create:encased_fan", size=1.5),

    quest("washing", A + 10, 22, "&6Wasch Kies zu Eisen",
          subtitle="Eisenklumpen aus Bruchstein.",
          description=[
              "Lüfter, davor ein &bWasserblock&r, und &6Kies&r auf einem Band durch den Luftstrom. Jeder Kies gibt mit &e25 Prozent&r Feuerstein und mit &e12,5 Prozent&r einen Eisenklumpen.",
              "",
              "Mit dem Mahlstein davor, der Bruchstein zu Kies mahlt, wird Bruchstein zu Eisenklumpen: genau die Klumpen für die Legierung.",
              "",
              "Sand gibt beim Waschen Ton, roter Sand Goldklumpen, Mehl wird zu Teig.",
          ],
          tasks=[task_item("minecraft:iron_nugget", 64)],
          rewards=[reward_item("minecraft:gravel", 64), reward_xp(5)],
          deps=["fan", "millstone"]),

    quest("fan_smelting", A + 10, 24, "&6Schmilz mit dem Lüfter",
          subtitle="Ein Ofen ohne Brennstoff.",
          description=[
              "Stell &cLava&r direkt vor den Lüfter und schick Items auf einem Band durch den Strom. Sie werden geschmolzen wie im Ofen: Rohzink zu Zinkbarren, Sand zu Glas.",
              "",
              "Die Lava verbraucht sich dabei nicht. &6Feuer&r statt Lava räuchert Essen wie ein Räucherofen.",
          ],
          tasks=[task_item("create:zinc_ingot", 32)],
          rewards=[reward_item("create:raw_zinc", 16), reward_xp(3)],
          deps=["fan"], icon="minecraft:lava_bucket"),

    # ---- Item-Logistik ------------------------------------------------------
    quest("belt", A, 29, "&6Spann ein Förderband",
          subtitle="Items und Rotation auf einer Spur.",
          description=[
              "Sechs &6getrockneter Seetang&r ergeben ein &6Förderband&r. Klick damit zwei parallele Wellen nacheinander an, bis zu &e20 Blöcke&r auseinander, waagerecht oder im 45-Grad-Winkel.",
              pic("create:belt_connector"),
              "Das Band trägt Items, Mobs und Spieler und gibt die Rotation weiter. Presse und Säge arbeiten darüber im Vorbeifahren, ein Lüfter seitlich daneben.",
          ],
          tasks=[task_item("create:belt_connector", 4)],
          rewards=[reward_item("minecraft:dried_kelp_block", 4), reward_xp(3)],
          deps=["press"], icon="create:belt_connector", size=1.75, shape="gear"),

    quest("chute", A + 2.5, 28, "&6Lass Items durch einen Schacht fallen",
          subtitle="Senkrecht, schneller als ein Trichter.",
          description=[
              "Zwei &6Eisenbleche&r und ein &6Eisenbarren&r ergeben vier &6Schächte&r. Ein Schacht zieht Items aus Kisten, Mahlsteinen oder Becken darüber und lässt sie fallen.",
              "",
              "Mit einem Lüfter darunter oder darüber schiebst du Items sogar nach oben.",
              "",
              "&6Tipp:&r Der &6Gewichtete Werfer&r (Goldblech, Depot, Zahnrad) wirft Items bis zu 32 Blöcke weit auf ein Ziel, das du vor dem Absetzen anklickst.",
          ],
          tasks=[task_item("create:chute", 4)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(2)],
          deps=["belt"]),

    quest("funnel", A + 2.5, 30, "&6Häng eine Andesitschleuse an",
          subtitle="Rein ins Band, raus aus der Kiste.",
          description=[
              "Eine &6Andesitlegierung&r über einem &6getrockneten Seetang&r ergibt zwei &6Andesitschleusen&r. An Kiste, Depot oder Becken zieht sie Items heraus oder schiebt sie hinein.",
              "",
              "Die Richtung hängt davon ab, wie herum du sie setzt, der Schraubenschlüssel polt um. Sie nimmt ein Item auf einmal, ein Redstone-Signal hält sie an.",
              "",
              "Filter und Stückzahlen kann erst die Messingschleuse aus Stufe 2.",
          ],
          tasks=[task_item("create:andesite_funnel", 4)],
          rewards=[reward_item("minecraft:dried_kelp", 16), reward_xp(2)],
          deps=["belt"]),

    quest("andesite_tunnel", A + 5, 31.5, "&6Verteil Items mit einem Tunnel",
          subtitle="Ein Band versorgt mehrere Maschinen.",
          description=[
              "Zwei &6Andesitlegierungen&r über zwei &6getrocknetem Seetang&r ergeben zwei &6Andesittunnel&r. Setz einen oben auf ein Förderband.",
              "",
              "Er zweigt von durchlaufenden Stapeln einzelne Items auf Bänder oder Schleusen daneben ab. Gezielt sortieren kann erst der Messingtunnel.",
          ],
          tasks=[task_item("create:andesite_tunnel", 2)],
          rewards=[reward_xp(2)],
          deps=["funnel"], optional=True),

    quest("vault", A + 5, 29.5, "&6Bau einen Gegenstandstresor",
          subtitle="20 Stapel pro Block.",
          description=[
              "Zwei &6Eisenbleche&r um ein &6Fass&r ergeben einen &6Gegenstandstresor&r. Er fasst &e20 Stapel pro Block&r, nebeneinander gesetzte verschmelzen, bis 3 x 3 Blöcke im Querschnitt.",
              "",
              "Tresore haben keine Oberfläche. Du füllst und leerst sie mit Schleusen, Schächten, Bändern oder Paketen.",
          ],
          tasks=[task_item("create:item_vault", 4)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["funnel"]),

    quest("packager", A + 7.5, 28.5, "&6Pack ein Paket",
          subtitle="Karton, Verpacker, Adresse.",
          description=[
              "Vier &6Zuckerrohr&r, Bambus oder Setzlinge mit &b250 mB Wasser&r im Mixer ergeben &6Zellstoff&r, die Presse macht &6Karton&r daraus. Vier Karton sind ein &6Kartonblock&r.",
              pic("create:cardboard"),
              "Der &6Verpacker&r (Kartonblock, vier Eisenbarren, zwei Redstone) sitzt an einem Lager. Mit Redstone-Signal packt er den Inhalt in ein &6Paket&r, ein Paket packt er wieder aus.",
              "",
              "Ein &6Schild&r mit Namen am Verpacker gibt seinen Paketen eine &eAdresse&r.",
          ],
          tasks=[task_item("create:cardboard", 8), task_item("create:packager", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["vault", "mixer"], icon="create:packager", size=1.5),

    quest("frogport", A + 10, 28, "&6Schick Pakete per Kette",
          subtitle="Kettenförderer und Frosch.",
          description=[
              "Vier &6Andesitgehäuse&r um ein &6Großes Zahnrad&r ergeben zwei &6Kettenförderer&r. Setz sie auf angetriebene Wellen und verbinde sie mit &6Ketten&r, bis &e32 Blöcke&r weit, je Förderer bis zu vier Verbindungen.",
              "",
              "Der &6Frosch-Anschluss für Pakete&r (Schleimball, Tresor, Legierung) sitzt höchstens &e5 Blöcke&r neben der Kette. Er setzt Pakete auf und schnappt sich jedes, das an seine Adresse will.",
          ],
          tasks=[task_item("create:chain_conveyor", 2), task_item("create:package_frogport", 2)],
          rewards=[reward_item("minecraft:chain", 16), reward_xp(3)],
          deps=["packager"]),

    quest("stock", A + 10, 30, "&6Verbinde ein Lagernetz",
          subtitle="Lagerverbindung auf dem Verpacker.",
          description=[
              "Ein &6Sender&r (drei Kupferbleche, Blitzableiter, Redstone) auf einem &6Tresor&r ergibt eine &6Lagerverbindung&r. Setz sie auf einen Verpacker: das Lager dahinter gehört zum &eLagernetz&r.",
              "",
              "Weitere Verbindungen stimmst du ab, indem du vor dem Setzen eine alte damit anklickst. Das alles läuft schon in Stufe 1, ganz ohne Strom.",
          ],
          tasks=[task_item("create:stock_link", 2)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["packager"]),

    quest("stock_ticker", A + 12.5, 30, "&6Bestell am Lagerticker",
          subtitle="Ein Verkäufer liefert, was im Netz liegt.",
          description=[
              "&6Glas&r, &6Lagerverbindung&r und &6Goldbarren&r untereinander ergeben den &6Lagerticker&r. Stell ihn ins selbe Netz, daneben einen Mob auf einem &6Sitz&r (Wolle und Holzstufe).",
              "",
              "Klick den Mob an: du siehst alles im Netz und bestellst. Die Verpacker schicken die Ware an die Adresse, die du angibst.",
              "",
              "Ein &6Redstone-Anfrager&r (Redstone, Lagerverbindung, Eisenbarren) löst eine feste Bestellung bei jedem Impuls aus.",
          ],
          tasks=[task_item("create:stock_ticker", 1)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["stock"], icon="create:stock_ticker", size=1.5),

    quest("shop", A + 15, 30, "&6Eröffne einen Laden",
          subtitle="Handel zwischen Spielern ohne Chat.",
          description=[
              "Eine &6Andesitlegierung&r im Steinschneider ergibt eine &6Andesit-Tischdecke&r. Klick damit den Verkäufer am Lagerticker an, stell sie auf, leg die Ware darauf und den Preis darunter.",
              "",
              "Käufer nehmen eine &6Einkaufsliste&r und zahlen beim Verkäufer. Dein Netz verschickt die Ware, die Bezahlung landet in deinem Lager.",
          ],
          tasks=[task_item("create:andesite_table_cloth", 2)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(3)],
          deps=["stock_ticker"], optional=True),

    quest("redstone_link", A + 12.5, 28, "&6Schalt per Funk",
          subtitle="Redstone ohne Kabel, 256 Blöcke weit.",
          description=[
              "Ein &6Sender&r auf einem &6Andesitgehäuse&r ergibt zwei &6Redstone-Verbindungen&r. Gib beiden dieselben zwei Items in die Frequenzfelder.",
              "",
              "Schleichen und Rechtsklick mit leerer Hand wechselt zwischen Senden und Empfangen. So schaltest du eine Kupplung am anderen Ende der Basis.",
          ],
          tasks=[task_item("create:redstone_link", 2)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(2)],
          deps=["stock"], optional=True),

    # ---- Fluide -----------------------------------------------------------
    quest("copper_casing", B, 2.5, "&6Ummantel Holz mit Kupfer",
          subtitle="Der Kupferrahmen für alles Flüssige.",
          description=[
              "Rechtsklicke einen gesetzten, entrindeten Stamm mit einem &6Kupferbarren&r: er wird zum &6Kupferrahmen&r. Er steckt in Ausguss, Abfluss und Schlauchrolle.",
              "",
              "In Stufe 2 stecken in jedem Messingbarren zwei Kupfer. Kupfer horten lohnt sich.",
          ],
          tasks=[task_item("create:copper_casing", 4)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_xp(2)],
          deps=["sheets"]),

    quest("pipes", B + 2.5, 1.5, "&6Leg Flüssigkeitsrohre",
          subtitle="Wasser dahin, wo du es brauchst.",
          description=[
              "Zwei &6Kupferbleche&r und ein &6Kupferbarren&r ergeben vier &6Flüssigkeitsrohre&r. Sie verbinden sich selbst mit Tanks, Becken und Maschinen anderer Mods.",
              "",
              "Rohre allein bewegen nichts, dafür brauchst du eine Pumpe. Ein offenes Ende in Wasser saugt es aus der Welt. Ein &6Flüssigkeitsventil&r (Rohr und Eisenblech) sperrt die Leitung.",
          ],
          tasks=[task_item("create:fluid_pipe", 16)],
          rewards=[reward_item("minecraft:copper_ingot", 8), reward_xp(2)],
          deps=["copper_casing"]),

    quest("pump", B + 5, 2.5, "&6Pump Wasser",
          subtitle="Der Motor im Rohrnetz.",
          description=[
              "Ein &6Zahnrad&r und ein &6Rohr&r ergeben die &6Mechanische Pumpe&r. Setz sie in die Leitung und treib sie an, sie drückt bis zu &e16 Blöcke&r weit.",
              "",
              "Der Pfeil zeigt die Richtung, umgekehrte Drehung pumpt rückwärts. Je mehr RPM, desto mehr Durchfluss, bei &d4 SU pro RPM&r.",
              "",
              "&cHäufiger Fehler:&r Zwei Pumpen, die gegeneinander arbeiten.",
          ],
          tasks=[task_item("create:mechanical_pump", 1)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["pipes"], icon="create:mechanical_pump", size=1.5),

    quest("tank", B + 7.5, 1.5, "&6Füll einen Flüssigkeitstank",
          subtitle="Acht Eimer pro Block.",
          description=[
              "Zwei &6Kupferbleche&r um ein &6Fass&r ergeben einen &6Flüssigkeitstank&r mit &b8 Eimern&r pro Block. Gestapelte Tanks verschmelzen, bis 3 Blöcke breit und 32 hoch.",
              "",
              "In Stufe 2 wird ein Tank mit Lohenbrennern darunter zum Dampfkessel.",
              "",
              "&6Tipp:&r Die &6Schlauchrolle&r (Kupferrahmen, getrockneter Seetangblock, Kupferblech) saugt bis &e128 Blöcke&r tief. Ein Gewässer über &e10 000 Blöcken&r gilt als unendlich.",
          ],
          tasks=[task_item("create:fluid_tank", 4)],
          rewards=[reward_table("s1_common"), reward_xp(2)],
          deps=["pump"]),

    quest("spout", B + 7.5, 3.5, "&6Füll mit dem Ausguss",
          subtitle="Flüssigkeit in Items hinein und heraus.",
          description=[
              "&6Kupferrahmen&r über &6getrocknetem Seetang&r ergibt den &6Ausguss&r. Über einem Depot oder Band befüllt er Eimer, Flaschen und alle &eBefüllen&r-Rezepte aus JEI.",
              "",
              "Der &6Abfluss&r (Eisengitter über Kupferrahmen) leert Items, die darauf landen, ins Rohr. Andere Items lässt er durch wie ein Stück Band.",
          ],
          tasks=[task_item("create:spout", 1), task_item("create:item_drain", 1)],
          rewards=[reward_item("minecraft:glass_bottle", 16), reward_xp(3)],
          deps=["pump"]),

    quest("diving", B + 2.5, 3.5, "&6Tauch mit Druckluft",
          subtitle="Rückentank, Helm und Stiefel.",
          description=[
              "&6Kupfer-Rückentank&r (Kupferblock, Kupferbarren, Legierung, Welle), &6Kupfer-Tauchhelm&r (Kupfer und Glas), &6Kupfer-Tauchstiefel&r (Kupfer und Legierung).",
              pic("create:copper_diving_helmet"),
              "Stell den Tank auf und treib ihn an (4 SU pro RPM), bis er &e900&r Luft hat. Mit Helm und Stiefeln atmest du unter Wasser und sinkst schnell zum Grund.",
          ],
          tasks=[task_item("create:copper_backtank", 1), task_item("create:copper_diving_helmet", 1),
                 task_item("create:copper_diving_boots", 1)],
          rewards=[reward_xp(5)],
          deps=["copper_casing"], optional=True),

    # ---- Kontraptionen --------------------------------------------------------
    quest("bearing", B, 9, "&6Dreh ein Bauwerk",
          subtitle="Das Mechanische Lager macht Blöcke beweglich.",
          description=[
              "&6Holzstufe&r, &6Andesitgehäuse&r und &6Welle&r untereinander ergeben das &6Mechanische Lager&r. Rechtsklick macht die Blöcke davor zur &eKontraption&r, die sich dreht.",
              "",
              "Bohrer, Sägen und Erntemaschinen daran arbeiten während der Bewegung. Bis zu &e2 048 Blöcke&r nimmt eine Kontraption mit. Nochmal Rechtsklick setzt sie fest.",
          ],
          tasks=[task_item("create:mechanical_bearing", 1)],
          rewards=[reward_xp(3)],
          deps=["gearbox"]),

    quest("glue", B + 2.5, 8, "&6Kleb Blöcke zusammen",
          subtitle="Was verklebt ist, fährt mit.",
          description=[
              "Zwei &6Schleimbälle&r, ein &6Eisenblech&r und ein &6Eisenklumpen&r ergeben &6Sekundenkleber&r. Klick eine Ecke an, dann die gegenüberliegende: alles im Rahmen ist verklebt.",
              pic("create:super_glue"),
              "Der Block direkt vor Lager oder Kolben gehört immer dazu, alles Weitere braucht Kleber oder ein Gerüst.",
          ],
          tasks=[task_item("create:super_glue", 1)],
          rewards=[reward_item("minecraft:slime_ball", 4), reward_xp(2)],
          deps=["bearing"]),

    quest("piston", B + 2.5, 10, "&6Schieb mit dem Kolben",
          subtitle="Bis zu 64 Blöcke Hub.",
          description=[
              "&6Holzstufe&r, &6Andesitgehäuse&r und &6Kolbenverlängerungsstange&r ergeben den &6Mechanischen Kolben&r. Dahinter sitzen weitere Stangen (Bretter und Legierung, acht Stück), eine pro Block Hub.",
              "",
              "Zurück fährt er, wenn die Drehrichtung wechselt, am einfachsten mit einer Gangschaltung. Mit einem Schleimball wird er zum &6Klebrigen Kolben&r.",
          ],
          tasks=[task_item("create:mechanical_piston", 1), task_item("create:piston_extension_pole", 8)],
          rewards=[reward_xp(3)],
          deps=["bearing"]),

    quest("rope_pulley", B + 5, 8, "&6Lass einen Flaschenzug hinab",
          subtitle="Rauf und runter, 384 Blöcke tief.",
          description=[
              "&6Andesitgehäuse&r, &6Wolle&r und &6Eisenblech&r untereinander ergeben den &6Flaschenzug&r. Er hebt und senkt alles, was unten an seinem Seil klebt.",
              "",
              "Ein Lastenaufzug, eine Bergbauplattform oder ein Bohrturm, der sich Schicht für Schicht nach unten frisst. Den Aufzug mit Stockwerken gibt es in Stufe 2.",
          ],
          tasks=[task_item("create:rope_pulley", 1)],
          rewards=[reward_xp(3)],
          deps=["glue"]),

    quest("gantry", B + 5, 10, "&6Fahr auf einer Portalkranachse",
          subtitle="Geradeaus entlang einer Schiene.",
          description=[
              "&6Portalkranachse&r: Legierung, Redstone, Legierung, acht Stück. &6Portalkranwagen&r: Holzstufe, Andesitgehäuse, Zahnrad. Drehst du die Achse, fährt der Wagen mit allem, was an ihm klebt.",
              "",
              "Achsen quer am Wagen ergeben eine zweite Richtung. Ideal für Bohrer, die eine Fläche abtragen.",
          ],
          tasks=[task_item("create:gantry_shaft", 8), task_item("create:gantry_carriage", 1)],
          rewards=[reward_xp(3)],
          deps=["piston"], optional=True),

    quest("chassis", B + 7.5, 8, "&6Bau ein Gerüst",
          subtitle="Große Kontraptionen ohne Kleber an jeder Ecke.",
          description=[
              "&6Schubgerüst&r: drei Stämme mit Legierung darüber und darunter, drei Stück. &6Drehgerüst&r: Stämme im Kreuz mit Legierung links und rechts.",
              "",
              "Bestreich eine Seite mit einem &6Schleimball&r: sie nimmt alle Blöcke davor mit, bis &e16 Blöcke&r weit. So hängen ganze Sägeräder an einem Lager.",
          ],
          tasks=[task_item("create:linear_chassis", 3)],
          rewards=[reward_item("minecraft:slime_ball", 4), reward_xp(3)],
          deps=["glue"], optional=True),

    quest("tree_farm", B + 7.5, 10, "&6Fäll Bäume mit einem Sägerad",
          subtitle="Lager, Gerüst und Sägen im Kreis.",
          description=[
              "Ein &6Mechanisches Lager&r, davor ein &6Drehgerüst&r mit Schleim, ringsum &6Mechanische Sägen&r nach außen. Dreht sich das Rad durch eine Baumreihe, fällt es ganze Stämme.",
              "",
              "Die Stämme fallen zu Boden, ein Band mit Schleuse darunter sammelt sie ein. Jede Säge kostet 4 SU pro RPM mehr.",
          ],
          tasks=[task_item("minecraft:oak_log", 128)],
          rewards=[reward_item("minecraft:oak_sapling", 16), reward_xp(3)],
          deps=["chassis"], icon="create:mechanical_saw", optional=True),

    quest("drill", B, 12.5, "&6Bohr dich durch Stein",
          subtitle="Der Mechanische Bohrer.",
          description=[
              "Drei &6Andesitlegierungen&r um einen &6Eisenbarren&r, darunter ein &6Andesitgehäuse&r, ergeben den &6Mechanischen Bohrer&r. Er baut den Block vor seiner Spitze ab, solange er dreht.",
              "",
              "Fest aufgestellt ist er das Herz eines Bruchsteingenerators. An Kolben, Lager oder Portalkran wird er zum Tunnelbohrer.",
          ],
          tasks=[task_item("create:mechanical_drill", 1)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["bearing"], icon="create:mechanical_drill", size=1.5),

    quest("cobble_gen", B + 2.5, 12.5, "&6Bau einen Bruchsteingenerator",
          subtitle="Stein ohne Ende für den Obelisken.",
          description=[
              "Lava und Wasser so, dass dazwischen Bruchstein entsteht, davor ein &6Mechanischer Bohrer&r. Jeder abgebaute Stein bildet sich sofort neu, eine Schleuse sammelt ein.",
              "",
              "&eKronwerke:&r Der Stein-Pfeiler will &620 000 Bruchstein&r (für 30 Spieler). Mehrere Generatoren an einer Welle und ein Band bis zum Obelisken zahlen im Schlaf ein.",
              "",
              "Eine Kiste oder ein Fass direkt neben dem Obelisken ist ein &eEinspeiser&r: er holt sich alle zwei Sekunden, was er brauchen kann.",
          ],
          tasks=[task_item("minecraft:cobblestone", 1024)],
          rewards=[reward_table("s1_uncommon"), reward_xp(5)],
          deps=["drill"], icon="minecraft:cobblestone", size=2.0, shape="gear"),

    quest("harvester", B + 5, 12.5, "&6Ernte im Vorbeifahren",
          subtitle="Erntemaschine und Pflug.",
          description=[
              "&6Mechanische Erntemaschine&r: Legierung und Eisenbleche über einem Andesitgehäuse. Sie erntet reife Pflanzen und pflanzt neu. Der &6Mechanische Pflug&r macht Erde zu Ackerboden.",
              "",
              "Klebe beide an einen Portalkran oder Kolben, der langsam übers Feld fährt. Die Ernte landet in Kisten auf der Kontraption.",
          ],
          tasks=[task_item("create:mechanical_harvester", 2), task_item("create:mechanical_plough", 1)],
          rewards=[reward_item("minecraft:wheat_seeds", 32), reward_xp(3)],
          deps=["drill"], optional=True),

    quest("psi", B + 7.5, 12.5, "&6Lad im Vorbeifahren um",
          subtitle="Portable Lagerschnittstelle.",
          description=[
              "&6Andesitgehäuse&r und &6Schacht&r ergeben eine &6Portable Lagerschnittstelle&r. Eine sitzt auf der Kontraption, eine fest in der Welt.",
              "",
              "Stehen sie sich mit ein bis zwei Blöcken Abstand gegenüber, hält die Kontraption und tauscht Items aus. Eine Schleuse an der festen zieht sie ab. So laden in Stufe 2 auch Güterzüge.",
          ],
          tasks=[task_item("create:portable_storage_interface", 2)],
          rewards=[reward_table("s1_common"), reward_xp(3)],
          deps=["drill"]),

    # ---- Das Ziel -------------------------------------------------------------
    quest("factory", B + 2.5, 18, "&6&lBau die Andesit-Fabrik",
          subtitle="Das Steinwerk läuft von allein.",
          description=[
              "Andesit (gegraben oder verdichtet) und Klumpen (aus der Kieswäsche oder aus Zink) laufen auf Bändern zum Mixer, Wasserräder treiben alles, eine Schleuse lädt die &6Andesitlegierung&r ab.",
              "",
              "&eKronwerke:&r Der Technik-Pfeiler will &61 500 Legierungen&r (für 30 Spieler) und &e12 Steinwerk-Getriebe&r: vier Andesitgehäuse, Großes Zahnrad, Presse, Mahlstein, Wasserrad und ein Infused Iron. Jedes zählt so viel wie 125 Legierungen.",
              "",
              "&eSo zahlst du ein:&r Schleichen und Rechtsklick am Obelisken gibt alles Passende ab, ein &eEinspeiser&r daneben zieht es selbst ein. &e/kw goals&r zeigt den Stand.",
          ],
          tasks=[task_item("create:andesite_alloy", 512)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["alloy_mixing", "cobble_gen"], icon="create:andesite_alloy", size=2.5, shape="gear"),

    quest("outlook", B + 6, 18, "&6Bereite das Messingwerk vor",
          subtitle="Was Stufe 2 bringt und was du jetzt schon tun kannst.",
          description=[
              "Horte &6Kupfer&r und &6Zink&r im Verhältnis zwei zu eins und press &6Eisenbleche&r vor.",
              "",
              "&eRezept auf Kronwerke:&r Messing gibt es nur aus dem erhitzten Mixer: zwei Kupfer, ein Zink und ein &6Lohenstaub&r ergeben einen Barren. Überhitzt mit Lohenkuchen werden es zwei Barren ohne Staub.",
              "",
              "Das Gehäuse des &6Lohenbrenners&r braucht &dzwei Quelljuwelen&r aus Ars Nouveau. Stufe 2 will außerdem 150 &6Präzisionsgetriebe&r, gebaut auf Messingblech. Die Kapitel &6Create: Messing&r und &6Create: Züge&r warten.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("ars_nouveau:source_gem", 2), reward_xp(5)],
          deps=["factory"], icon="create:zinc_ingot", shape="diamond"),
]

images = [
    head("title", "Create", A + 7, -3, height=1.8, kind="title"),
    head("stage", "Stufe 1: Steinwerk", A + 7.2, -1.7, height=0.55, kind="note", colour="stone"),
    head("basics", "Grundlagen", A - 0.6, 0.2),
    head("power", "Energie", A - 0.6, 6.6),
    head("costs", "Was jede Maschine kostet", A - 0.6, 12.1, colour="stone"),
    head("processing", "Verarbeitung", A - 0.6, 16.3),
    head("logistics", "Item-Logistik", A - 0.6, 26.4),
    head("fluids", "Fluide", B - 0.6, 0.0),
    head("contraptions", "Kontraptionen", B - 0.6, 6.4),
    head("goal", "Das Ziel", B - 0.6, 15.8),
]
# centre the title over the whole canvas
images[0]["x"] = 15.5
images[1]["x"] = 15.5

chapter(C, "Create", "create:large_cogwheel", "tech", quests, shape="gear", order=1,
        subtitle=["Rotation, Förderbänder und die ersten Maschinen des Steinwerks."], images=images)
