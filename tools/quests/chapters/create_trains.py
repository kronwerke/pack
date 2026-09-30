"""Create trains in stage 2 (Messingwerk): track by sequenced assembly, sturdy sheets, train
casing, stations, bogeys, controls, schedules and conductors, signals, cargo, and a line to the
obelisk at spawn."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create_trains"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


# Column A starts at x 0, column B at x 17.
A, B = 0, 17

quests = [
    # ---- Gleise ------------------------------------------------------------------
    quest("welcome", A, 3, "&6&lZüge",
          subtitle="Der schnellste Weg über eine große Karte.",
          description=[
              "Create-Züge sind echte Kontraptionen: sie fahren auf eigenen Gleisen, tragen Blöcke, Kisten und Tanks und folgen einem Fahrplan, ganz ohne Fahrer. Auf einem Server mit dreißig Basen sind sie das Rückgrat für Handel, Rohstoffe und den Weg zum Obelisken.",
              "",
              "&6Gleise&r entstehen durch &esequenzielle Montage&r: eine Steinstufe, glatte Steinstufe oder Andesitstufe kommt aufs Band, zwei Einsatzgeräte setzen je einen Eisen- oder Zinkklumpen darauf, eine Presse drückt alles fest. Einsatzgeräte und Montage lernst du im Kapitel &6Create: Messing&r.",
              img(item_texture("create:track"), 32, 32),
              "Züge brauchen weder Treibstoff noch Rotation. Einmal gebaut, fahren sie bis zu 28 Blöcke pro Sekunde, in Kurven halb so schnell.",
          ],
          tasks=[task_item("create:track", 16)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          icon="create:track", size=2.0, shape="hexagon"),

    quest("laying", A + 2.5, 2, "&6Gleise verlegen",
          subtitle="Klick, Klick, Kurve.",
          description=[
              "Setz ein erstes Gleisstück, rechtsklicke es mit weiteren Gleisen in der Hand und klick dann auf den Punkt, wo die Strecke enden soll. Create zeigt dir vorher eine Vorschau: grün heißt machbar, rot heißt zu steil oder zu eng. Kurven, Steigungen und S-Kurven formt es von selbst; hältst du dabei die Sprinttaste, wird die Kurve so weit wie möglich.",
              "",
              "Ein Abschnitt darf bis zu 32 Blöcke lang sein und verbraucht Gleise nach seiner Länge. Danach setzt du am letzten Ende wieder an. Setzt du mitten auf einer bestehenden Strecke an, entsteht eine Abzweigung mit Weiche. Blöcke in der Nebenhand werden automatisch als Unterbau unter die Gleise gepflastert.",
              "",
              "&6Tipp:&r Plane großzügig. Enge Kurven bremsen, und fahrende Züge verletzen Spieler und Mobs, die auf dem Gleis stehen. Bahnübergänge mitten durch die Basis sind keine gute Idee.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["welcome"], icon="create:track", shape="diamond"),

    quest("track_factory", A + 2.5, 4, "&6Gleise am Fließband",
          subtitle="Eine Strecke braucht Hunderte.",
          description=[
              "Eine Strecke quer über die Karte verschlingt Gleise zu Hunderten. Bau dir eine eigene Linie: Stufen aus einer Säge, die Stein schneidet, aufs Band, zwei Einsatzgeräte mit Klumpen, eine Presse, Ausgabe in eine Kiste. Die Klumpen kommen aus der Erzwäsche oder aus Zinkbarren.",
              "",
              "Anders als beim Präzisionsgetriebe geht hier nichts schief: jede Stufe wird zu einem Gleis.",
          ],
          tasks=[task_item("create:track", 256)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["welcome"]),

    quest("nether_line", A + 5, 2, "&cNetherbahn",
          subtitle="Acht Blöcke Oberwelt pro Block Nether.",
          description=[
              "Gleise können durch ein &cNetherportal&r führen. Verleg das Gleis bis ins Portal hinein, und Create setzt die Strecke auf der anderen Seite fort. Weil ein Block im Nether acht Blöcken in der Oberwelt entspricht, verbindet eine kurze Netherstrecke weit entfernte Basen.",
              "",
              "Sichere die Strecke im Nether gut ab. Ghasts und Piglins halten nichts von Fahrplänen.",
          ],
          tasks=[task_checkmark("Eine Netherbahn gebaut")],
          rewards=[reward_xp(5)],
          deps=["laying"], icon="minecraft:obsidian", optional=True),

    # ---- Züge ------------------------------------------------------------------------
    quest("powder", A, 9.5, "&6Pulverisierter Obsidian",
          subtitle="Obsidian, fein gemahlen.",
          description=[
              "Für die Zugteile brauchst du &6Robuste Bleche&r, und die beginnen mit &6Pulverisiertem Obsidian&r. Wirf &6Obsidian&r zwischen zwei &6Mahlwerkräder&r: jeder Block gibt ein Pulver, und oft bleibt der Obsidian dabei ganz und geht noch einmal durch.",
              img(item_texture("create:powdered_obsidian"), 32, 32),
              "Obsidian entsteht, wo Wasser auf eine Lavaquelle fließt. Zum Abbauen brauchst du eine Diamantspitzhacke.",
          ],
          tasks=[task_item("create:powdered_obsidian", 8)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(3)],
          deps=["welcome"]),

    quest("sturdy_sheet", A + 2.5, 9.5, "&6Robustes Blech",
          subtitle="Obsidian, Lava, zweimal pressen.",
          description=[
              "Das &6Robuste Blech&r entsteht wieder durch sequenzielle Montage, diesmal in einer einzigen Runde: Pulverisierter Obsidian aufs Band, ein &6Ausguss&r gießt 500 mB &bLava&r darauf, dann presst eine Presse zweimal. Zwei Pressen hintereinander über dem Band sind am einfachsten.",
              img(item_texture("create:sturdy_sheet"), 32, 32),
              "Robuste Bleche stecken in jedem Zugrahmen und in den Fahrplänen.",
          ],
          tasks=[task_item("create:sturdy_sheet", 8)],
          rewards=[reward_item("minecraft:lava_bucket", 1), reward_xp(3)],
          deps=["powder"]),

    quest("casing", A + 5, 9.5, "&6Zugrahmen",
          subtitle="Aus diesem Rahmen ist jeder Zug gebaut.",
          description=[
              "Rechtsklicke einen gesetzten &6Messingrahmen&r mit einem &6Robusten Blech&r, und er wird zum &6Zugrahmen&r. Ein Einsatzgerät erledigt das auch am Fließband.",
              "",
              "Aus dem Zugrahmen entstehen Bahnhof, Signale, Zugbeobachter, Türen und die Zugsteuerung. Direkt aufs Gleis geklickt wird er zum &6Drehgestell&r, dem Fahrwerk jedes Zugs.",
          ],
          tasks=[task_item("create:railway_casing", 8)],
          rewards=[reward_item("create:brass_casing", 4), reward_xp(3)],
          deps=["sturdy_sheet"], icon="create:railway_casing", size=1.5),

    quest("station", A + 7.5, 8.5, "&6Bahnhof",
          subtitle="Hier wird gebaut, hier wird gehalten.",
          description=[
              "Ein Zugrahmen und ein Kompass ergeben zwei &6Bahnhöfe&r. Rechtsklicke mit dem Bahnhof in der Hand ein gerades Gleisstück und setz ihn dann daneben ab.",
              "",
              "Im Menü des Bahnhofs gibst du ihm einen Namen, den später die Fahrpläne benutzen. Hier schaltest du auch in den &eMontagemodus&r: dann wird das Gleis vor dem Bahnhof zur Baustelle für einen neuen Zug, bis zu 128 Blöcke lang.",
          ],
          tasks=[task_item("create:track_station", 2)],
          rewards=[reward_item("minecraft:compass", 2), reward_xp(3)],
          deps=["casing"]),

    quest("bogey", A + 7.5, 10.5, "&6Drehgestelle",
          subtitle="Die Räder unter dem Zug.",
          description=[
              "Im Montagemodus rechtsklickst du mit einem &6Zugrahmen&r das Gleis vor dem Bahnhof: dort entsteht ein &6Drehgestell&r. Mit dem Schraubenschlüssel wechselst du zwischen kleinem und großem Drehgestell.",
              "",
              "Ein kurzer Wagen kommt mit einem Drehgestell aus, längere brauchen zwei, vorn und hinten. Bis zu 20 Drehgestelle darf ein Zug haben.",
              "",
              "Alles, was du auf die Drehgestelle baust, fährt später mit. Klebe es mit &6Sekundenkleber&r fest, sonst bleibt es beim Zusammenbau am Bahnsteig stehen.",
          ],
          tasks=[task_checkmark("Drehgestell gesetzt")],
          rewards=[reward_item("create:super_glue", 2), reward_xp(3)],
          deps=["station"], icon="create:railway_casing"),

    quest("controls", A + 10, 9.5, "&6Zugsteuerung",
          subtitle="Der Führerstand.",
          description=[
              "Ein Hebel, ein Zugrahmen und ein &6Präzisionsgetriebe&r ergeben die &6Zugsteuerung&r. Setz sie auf deinen Zug, mit der Front in die Richtung, in die er fahren soll. Ohne Zugsteuerung lässt sich ein Zug nicht zusammenbauen.",
              "",
              "Soll er in beide Richtungen fahren, bekommt jedes Ende eine eigene Zugsteuerung, jeweils nach außen gerichtet.",
              "",
              "Ein &6Sitz&r direkt vor der Steuerung ist der Platz für den Schaffner, der später nach Fahrplan fährt.",
          ],
          tasks=[task_item("create:controls", 1)],
          rewards=[reward_table("s2_common"), reward_xp(3)],
          deps=["station", "bogey"], icon="create:controls", size=1.5),

    quest("first_train", A + 12.5, 9.5, "&6&lDein erster Zug",
          subtitle="Alles einsteigen!",
          description=[
              "So bringst du ihn auf die Schiene:",
              "&e1.&r Bahnhof in den Montagemodus schalten.",
              "&e2.&r Drehgestelle aufs Gleis davor setzen.",
              "&e3.&r Den Zug darauf bauen: Wagen, Sitze, Kisten, was du magst, und die &6Zugsteuerung&r nicht vergessen.",
              "&e4.&r Alles mit &6Sekundenkleber&r verbinden.",
              "&e5.&r Im Bahnhofsmenü den Zug zusammenbauen lassen.",
              "",
              "Dann rechtsklickst du die Zugsteuerung und fährst mit &eW&r und &eS&r, an Weichen wählst du mit &eA&r und &eD&r die Richtung. Das Mausrad begrenzt die Höchstgeschwindigkeit, und mit gedrückter &eLeertaste&r hält der Zug am nächsten Bahnhof. Schleichen beendet das Fahren. Von Hand fährt der Zug etwas langsamer als nach Fahrplan.",
              "",
              "An einem anderen Bahnhof im Montagemodus zerlegst du den Zug wieder in Blöcke, zum Umbauen oder Verlängern.",
          ],
          tasks=[task_checkmark("Zug gebaut und gefahren")],
          rewards=[reward_item("create:track", 64), reward_xp(10)],
          deps=["controls"], icon="create:controls", size=2.0, shape="diamond"),

    quest("doors", A + 12.5, 12, "&6Zugtüren",
          subtitle="Rein und raus, ohne zu klettern.",
          description=[
              "Eine Holztür und ein Zugrahmen ergeben eine &6Zugtür&r, eine Falltür und ein Zugrahmen eine &6Zugfalltür&r. Sie gleiten zur Seite, statt aufzuschwingen, und passen damit in schmale Wagen.",
              img(item_texture("create:train_door"), 32, 32),
              "Deko am Zug ist ausdrücklich erwünscht: ein schöner Zug ist die Visitenkarte deiner Basis auf dem Stream.",
          ],
          tasks=[task_item("create:train_door", 2)],
          rewards=[reward_xp(3)],
          deps=["first_train"], optional=True),

    # ---- Fahrplan (column B) ---------------------------------------------------------
    quest("schedule", B, 2.5, "&6Zugfahrplan",
          subtitle="Er fährt, während du woanders bist.",
          description=[
              "Ein Robustes Blech und Papier ergeben vier &6Zugfahrpläne&r. Im Fahrplan legst du Einträge an: &eFahre zu Bahnhof X&r, und darunter die Bedingung, wann es weitergeht: nach einer Wartezeit, zu einer Tageszeit, bei einem Redstone-Signal, wenn die Fracht voll ist, oder wenn sich an der Fracht eine Weile nichts mehr bewegt hat.",
              img(item_texture("create:schedule"), 32, 32),
              "Mit &eWiederholen&r springt der Plan am Ende wieder an den Anfang. Ein Bahnhofsname mit &e*&r passt auf mehrere Bahnhöfe: &eMine*&r fährt zur nächsten freien Station, deren Name mit Mine beginnt.",
          ],
          tasks=[task_item("create:schedule", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(3)],
          deps=["first_train"], icon="create:schedule", size=1.5),

    quest("conductor", B + 2.5, 2.5, "&6Der Schaffner",
          subtitle="Jemand muss ja fahren.",
          description=[
              "Nach Fahrplan fährt ein Zug nur, wenn ein &eSchaffner&r an der Zugsteuerung sitzt. Das kann jeder Mob sein, der auf einem Sitz direkt vor der Steuerung sitzt, ein Dorfbewohner zum Beispiel, oder ein &6Lohenbrenner&r an derselben Stelle. Einen Mob an der Leine setzt du bequem auf den Sitz, indem du den Sitz anklickst. Die Lohe ist der beliebteste Schaffner: sie braucht nichts und läuft nicht weg.",
              "",
              "Rechtsklicke den Schaffner mit dem Fahrplan in der Hand, und er übernimmt. Du kannst ihm den Fahrplan jederzeit wieder abnehmen, und solange er fährt, fährst du einfach mit.",
          ],
          tasks=[task_checkmark("Schaffner eingesetzt")],
          rewards=[reward_xp(5)],
          deps=["schedule"], icon="create:blaze_burner"),

    quest("auto_line", B + 5, 2.5, "&6Die erste Linie",
          subtitle="Zwei Bahnhöfe, ein Fahrplan, kein Fahrer.",
          description=[
              "Zeit für eine Linie, die ganz allein fährt: zwei Bahnhöfe, ein Zug mit Schaffner und ein Fahrplan mit zwei Einträgen und &eWiederholen&r. Nimm als Bedingung zum Beispiel &eWarte 20 Sekunden&r, damit Mitfahrer in Ruhe ein- und aussteigen können.",
              "",
              "Soll die Linie zu einem Nachbarn oder zum Spawn führen? Sprecht euch ab. Ein gemeinsames Netz mit sauber benannten Bahnhöfen hilft allen, und die Strecke zum Obelisken wird am Ende die meistbefahrene des Servers.",
          ],
          tasks=[task_checkmark("Die Linie läuft")],
          rewards=[reward_item("create:track", 64), reward_xp(5)],
          deps=["conductor"], icon="create:track_station", size=1.5),

    quest("display", B + 7.5, 2.5, "&6Abfahrtstafel",
          subtitle="Wann kommt der nächste Zug?",
          description=[
              "Setz einen &6Anzeige-Link&r an den Bahnhof und richte ihn auf eine &6Anzeigetafel&r. Im Menü des Links wählst du die Zuginformationen, und die Tafel zeigt, welcher Zug wann ankommt und wohin er fährt, wie auf einem echten Bahnsteig.",
              "",
              "Wie Anzeige-Link und Anzeigetafel gebaut werden, steht im Kapitel &6Create: Messing&r.",
          ],
          tasks=[task_item("create:display_link", 1), task_item("create:display_board", 6)],
          rewards=[reward_xp(3)],
          deps=["auto_line"], optional=True),

    # ---- Signale (column B) ----------------------------------------------------------
    quest("signal", B, 8, "&6Zugsignale",
          subtitle="Mehrere Züge, keine Unfälle.",
          description=[
              "Ein Zugrahmen und eine Elektronenröhre ergeben vier &6Zugsignale&r. Wie den Bahnhof klickst du ein Signal erst aufs Gleis und setzt es dann daneben ab. Signale teilen die Strecke in &eAbschnitte&r: ein Zug fährt nur in einen Abschnitt ein, in dem gerade kein anderer ist.",
              "",
              "Sobald zwei Züge dieselbe Strecke nutzen, brauchst du Signale. Setz sie vor jeden Abschnitt, auf zweigleisigen Strecken für jede Fahrtrichtung eines.",
          ],
          tasks=[task_item("create:track_signal", 4)],
          rewards=[reward_item("create:electron_tube", 4), reward_xp(3)],
          deps=["first_train"], icon="create:track_signal"),

    quest("junction", B + 2.5, 8, "&6Kreuzungen und Weichen",
          subtitle="Wo sich Strecken treffen.",
          description=[
              "Ein Signal hat zwei Betriebsarten, die du mit dem Schraubenschlüssel wechselst. Das &eEinfahrtssignal&r lässt einen Zug in den nächsten Abschnitt, sobald der frei ist. Das &eKreuzungssignal&r lässt ihn erst los, wenn auch der Weg durch die Kreuzung bis zum nächsten Signal frei ist.",
              "",
              "Vor Weichen und Kreuzungen gehören Kreuzungssignale, sonst bleibt ein Zug mitten auf der Kreuzung stehen und blockiert alle anderen. Faustregel: Kreuzungssignal davor, Einfahrtssignal dahinter.",
              "",
              "Mit der Ingenieursbrille siehst du an einem Signal, welcher Abschnitt dahinter liegt und ob er gerade belegt ist.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["signal"], icon="create:track_signal", shape="diamond"),

    quest("observer", B + 5, 8, "&6Zugbeobachter",
          subtitle="Redstone, wenn ein Zug vorbeikommt.",
          description=[
              "Ein Zugrahmen und eine Druckplatte ergeben zwei &6Zugbeobachter&r. Aufs Gleis gesetzt wie ein Signal, gibt er ein Redstone-Signal, solange ein Zug über ihm ist. Mit einem Filter reagiert er nur auf Züge, die ein bestimmtes Item geladen haben.",
              "",
              "Damit schließt du Schranken, läutest eine Glocke am Bahnsteig oder startest eine Verladeanlage, sobald der Güterzug da ist.",
          ],
          tasks=[task_item("create:track_observer", 2)],
          rewards=[reward_xp(3)],
          deps=["junction"], optional=True),

    # ---- Fracht (column B) -----------------------------------------------------------
    quest("cargo", B, 13.5, "&6Fracht laden",
          subtitle="Portable Schnittstellen am Bahnsteig.",
          description=[
              "Güterzüge laden mit denselben &6Portablen Lagerschnittstellen&r, die du aus Stufe 1 kennst. Eine sitzt am Wagen, eine am Bahnsteig, und wenn der Zug hält, zeigen beide aufeinander. Kisten, Fässer oder &6Gegenstandstresore&r auf dem Zug sind das Frachtlager.",
              "",
              "Hält der Zug, tauschen die Schnittstellen Items aus. Eine Schleuse an der festen Schnittstelle entlädt in dein Lager oder befüllt den Zug aus deinem Lager, je nachdem, wie herum sie sitzt.",
          ],
          tasks=[task_item("create:portable_storage_interface", 4), task_item("create:item_vault", 2)],
          rewards=[reward_table("s2_uncommon"), reward_xp(3)],
          deps=["first_train"], icon="create:portable_storage_interface", size=1.5),

    quest("fluid_cargo", B, 15.75, "&bFlüssige Fracht",
          subtitle="Tankwagen.",
          description=[
              "Die &6Portable Flüssigkeitsschnittstelle&r (Kupferrahmen und Schacht) macht dasselbe für Flüssigkeiten: Tanks auf dem Zug, eine Schnittstelle am Wagen, eine am Bahnsteig und eine Pumpe an der festen Seite.",
              "",
              "So bringt ein Tankzug Lava vom Nether-Bahnhof zu deinen Lüftern oder Wasser zum Dampfkessel.",
          ],
          tasks=[task_item("create:portable_fluid_interface", 2), task_item("create:fluid_tank", 4)],
          rewards=[reward_xp(3)],
          deps=["cargo"], optional=True),

    quest("freight", B + 2.5, 13.5, "&6Der Güterzug",
          subtitle="Rohstoffe fahren von selbst.",
          description=[
              "Kombiniere alles: ein Zug mit Frachtlager und Schnittstellen, ein Fahrplan mit zwei Bahnhöfen. Als Bedingung nimmst du &eFracht untätig&r: der Zug wartet, bis sich eine Weile nichts mehr bewegt hat, also bis Be- oder Entladen fertig ist, und fährt dann los.",
              "",
              "So speist eine Mine am Rand der Karte deine Fabrik im Zentrum, oder dein Zink- und Kupferbergwerk die Messing-Mixer.",
          ],
          tasks=[task_checkmark("Der Güterzug fährt")],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["cargo", "auto_line"], icon="create:item_vault"),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("obelisk_line", B + 5.5, 20, "&6&lDie Obelisk-Linie",
          subtitle="Alle Wege führen zum Spawn.",
          description=[
              "Der Obelisk steht am Spawn, und seine Ziele wollen große Mengen: &6Messingbarren&r und &6Präzisionsgetriebe&r in dieser Stufe, Stahl und mehr in den nächsten. Eine Bahnlinie von deiner Fabrik zum Spawn macht das Einzahlen bequem.",
              "",
              "Ein Bahnhof am Spawn, ein Güterzug, der dort hält, und eine Schleuse, die aus der Portablen Lagerschnittstelle direkt in deinen &eEinspeiser&r lädt: eine Kiste oder ein Fass, das du selbst neben den Obelisken gestellt hast. Alle zwei Sekunden holt sich der Obelisk daraus, was er braucht, und schreibt es dir gut.",
              "",
              "Sprecht euch ab, wie der Bahnhof am Spawn aussehen soll. Ein gemeinsamer Hauptbahnhof mit mehreren Gleisen und Kreuzungssignalen ist für dreißig Spieler viel schöner als dreißig einzelne Stummelgleise.",
          ],
          tasks=[task_item("create:track", 512), task_item("create:track_station", 2)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["freight", "junction"], icon="create:track_station", size=2.5, shape="gear"),
]

images = [
    head("title", "Create: Züge", 0, -3, height=1.6, kind="title"),
    head("stage", "Stufe 2: Messingwerk", 0, -1.6, height=0.55, kind="note", colour="stone"),
    head("track", "Gleise", A - 0.6, 0.1),
    head("trains", "Züge", A - 0.6, 7),
    head("schedule", "Fahrplan", B - 0.6, 0.1),
    head("signals", "Signale", B - 0.6, 5.8),
    head("cargo", "Fracht", B - 0.6, 11.3),
    head("goal", "Das Ziel", B + 4.15, 17.6),
]
images[0]["x"] = 12.5
images[1]["x"] = 12.5

chapter(C, "Create: Züge", "create:controls", "tech", quests, shape="gear", order=15, stage=2,
        subtitle=["Stufe 2: Gleise, Bahnhöfe und Züge, die von selbst fahren."], images=images)
