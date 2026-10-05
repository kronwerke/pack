"""Create trains in stage 2 (Messingwerk): track by sequenced assembly, the sturdy sheet in two
steps, train casing, stations, bogeys, controls, driving and rebuilding, schedules with a checklist
of the departure conditions, conductors, signals, cargo, postboxes, and a line to the obelisk at
spawn. Numbers come from the [trains] section of create-server.toml. Steam 'n' Rails is in
create_addons.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create_trains"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def condition(name, x, title, subtitle, line):
    """One line of the departure condition checklist."""
    return quest(name, x, 6, title, subtitle=subtitle, description=[line],
                 tasks=[task_checkmark("Ausprobiert")], rewards=[reward_xp(2)],
                 deps=["schedule"], icon="create:schedule", optional=True)


# Column A starts at x 0, column B at x 20.
A, B = 0, 20

quests = [
    # ---- Gleise ------------------------------------------------------------------
    quest("welcome", A, 3, "&6&lMontier deine ersten Gleise",
          subtitle="Züge brauchen eigene Gleise, und die kommen vom Band.",
          description=[
              "Eine &6Steinstufe&r, &6glatte Steinstufe&r oder &6Andesitstufe&r aufs Band. Zwei &6Einsatzgeräte&r setzen je einen Eisen- oder Zinkklumpen darauf, eine &6Presse&r drückt fest. Eine Runde, ein Gleis.",
              pic("create:track"),
              "Einsatzgeräte und sequenzielle Montage lernst du in &6Create: Messing&r. Züge brauchen weder Treibstoff noch Rotation und fahren bis &e28 Blöcke pro Sekunde&r, in Kurven &e14&r.",
          ],
          tasks=[task_item("create:track", 16)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          icon="create:track", size=2.0, shape="hexagon"),

    quest("laying", A + 2.5, 2, "&6Verleg eine Strecke",
          subtitle="Klick, Klick, Kurve.",
          description=[
              "Setz ein Gleis, rechtsklicke es mit Gleisen in der Hand und klick auf den Endpunkt. Die Vorschau zeigt grün für machbar, rot für zu steil oder zu eng.",
              "",
              "Ein Abschnitt ist bis zu &e32 Blöcke&r lang. Mit gedrückter Sprinttaste wird die Kurve so weit wie möglich. Blöcke in der Nebenhand werden als Unterbau gepflastert.",
              "",
              "Setzt du mitten auf einer Strecke an, entsteht eine Abzweigung. Fahrende Züge verletzen, was auf dem Gleis steht.",
          ],
          tasks=[task_checkmark("Strecke verlegt")],
          rewards=[reward_item("create:track", 16), reward_xp(3)],
          deps=["welcome"], icon="create:track", shape="diamond"),

    quest("track_factory", A + 2.5, 4, "&6Bau eine Gleisfabrik",
          subtitle="Eine Strecke braucht Hunderte.",
          description=[
              "Eine &6Säge&r schneidet Stein zu Stufen, die laufen aufs Band, zwei Einsatzgeräte mit Klumpen, eine Presse, Ausgabe in eine Kiste.",
              "",
              "Anders als beim Präzisionsgetriebe geht hier nichts schief: jede Stufe wird ein Gleis.",
          ],
          tasks=[task_item("create:track", 256)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["welcome"]),

    quest("nether_line", A + 5, 2, "&cFahr durch den Nether",
          subtitle="Ein Block Nether, acht Blöcke Oberwelt.",
          description=[
              "Verleg das Gleis bis in ein &cNetherportal&r hinein. Create setzt die Strecke auf der anderen Seite fort.",
              "",
              "Eine kurze Netherstrecke verbindet weit entfernte Basen. Sichere sie ab, Ghasts halten nichts von Fahrplänen.",
          ],
          tasks=[task_checkmark("Eine Netherbahn gebaut")],
          rewards=[reward_xp(5)],
          deps=["laying"], icon="minecraft:obsidian", optional=True),

    # ---- Züge ------------------------------------------------------------------------
    quest("powder", A, 9.5, "&6Mahl Obsidian zu Pulver",
          subtitle="Der Anfang jedes Zugrahmens.",
          description=[
              "Wirf &6Obsidian&r zwischen zwei &6Mahlwerkräder&r. Jeder Block gibt einen &6Pulverisierten Obsidian&r, und mit 75 Prozent kommt der Obsidian zurück und geht noch einmal durch.",
              pic("create:powdered_obsidian"),
              "Obsidian entsteht, wo Wasser auf eine Lavaquelle fließt. Abbauen mit Diamantspitzhacke.",
          ],
          tasks=[task_item("create:powdered_obsidian", 8)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(3)],
          deps=["welcome"]),

    quest("unprocessed_sheet", A + 2.5, 9.5, "&6Gieß Lava auf das Pulver",
          subtitle="Ein Unverarbeitetes Obsidianblatt.",
          description=[
              "Pulverisierter Obsidian aufs Depot oder Band unter einen &6Ausguss&r. Er gießt &b500 mB Lava&r darauf, heraus kommt ein &6Unverarbeitetes Obsidianblatt&r.",
              "",
              "Das ist der erste Schritt einer sequenziellen Montage. JEI zeigt die ganze Folge unter dem Robusten Blech.",
          ],
          tasks=[task_item("create:unprocessed_obsidian_sheet", 1)],
          rewards=[reward_item("minecraft:lava_bucket", 1), reward_xp(3)],
          deps=["powder"]),

    quest("sturdy_sheet", A + 5, 9.5, "&6Press es zweimal",
          subtitle="Das Robuste Blech.",
          description=[
              "Das Unverarbeitete Obsidianblatt muss zweimal unter die &6Presse&r. Zwei Pressen hintereinander über dem Band sind am einfachsten. Danach hast du ein &6Robustes Blech&r.",
              pic("create:sturdy_sheet"),
              "Robuste Bleche stecken in jedem Zugrahmen und in den Fahrplänen.",
          ],
          tasks=[task_item("create:sturdy_sheet", 8)],
          rewards=[reward_item("minecraft:obsidian", 8), reward_xp(4)],
          deps=["unprocessed_sheet"]),

    quest("casing", A + 7.5, 9.5, "&6Mach einen Zugrahmen",
          subtitle="Daraus ist jeder Zug gebaut.",
          description=[
              "Rechtsklicke einen gesetzten &6Messingrahmen&r mit einem &6Robusten Blech&r. Er wird zum &6Zugrahmen&r. Ein Einsatzgerät macht das auch am Band.",
              "",
              "Aus Zugrahmen entstehen Bahnhof, Signale, Beobachter, Türen und Zugsteuerung. Aufs Gleis geklickt wird er zum Drehgestell.",
          ],
          tasks=[task_item("create:railway_casing", 8)],
          rewards=[reward_item("create:brass_casing", 4), reward_xp(4)],
          deps=["sturdy_sheet"], icon="create:railway_casing", size=1.5),

    quest("station", A + 10, 8.5, "&6Bau einen Bahnhof",
          subtitle="Hier wird gebaut und gehalten.",
          description=[
              "Ein &6Zugrahmen&r und ein &6Kompass&r ergeben zwei &6Bahnhöfe&r. Rechtsklicke damit ein gerades Gleis und setz ihn daneben ab.",
              "",
              "Im Menü gibst du ihm einen Namen für die Fahrpläne. Im &eMontagemodus&r wird das Gleis davor zur Baustelle für einen Zug, bis &e128 Blöcke&r lang.",
          ],
          tasks=[task_item("create:track_station", 2)],
          rewards=[reward_item("minecraft:compass", 2), reward_xp(4)],
          deps=["casing"]),

    quest("bogey", A + 10, 10.5, "&6Setz Drehgestelle",
          subtitle="Die Räder unter dem Zug.",
          description=[
              "Im Montagemodus rechtsklickst du mit einem &6Zugrahmen&r das Gleis vor dem Bahnhof: dort entsteht ein &6Drehgestell&r. Der Schraubenschlüssel wechselt zwischen klein und groß.",
              "",
              "Kurze Wagen brauchen eins, längere zwei, höchstens &e20&r pro Zug. Was du darauf baust, klebst du mit &6Sekundenkleber&r fest.",
          ],
          tasks=[task_checkmark("Drehgestell gesetzt")],
          rewards=[reward_item("create:super_glue", 2), reward_xp(4)],
          deps=["station"], icon="create:railway_casing"),

    quest("controls", A + 12.5, 9.5, "&6Bau eine Zugsteuerung",
          subtitle="Der Führerstand.",
          description=[
              "&6Hebel&r, &6Zugrahmen&r und &6Präzisionsgetriebe&r untereinander ergeben die &6Zugsteuerung&r. Setz sie mit der Front in Fahrtrichtung auf den Zug. Ohne sie lässt er sich nicht zusammenbauen.",
              "",
              "Für beide Richtungen bekommt jedes Ende eine eigene. Ein &6Sitz&r direkt davor ist der Platz für den Schaffner.",
          ],
          tasks=[task_item("create:controls", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["station", "bogey"], icon="create:controls", size=1.5),

    quest("first_train", A + 15, 9.5, "&6&lBau deinen ersten Zug",
          subtitle="Alles einsteigen.",
          description=[
              "&e1.&r Bahnhof in den Montagemodus. &e2.&r Drehgestelle aufs Gleis. &e3.&r Zug darauf bauen, Zugsteuerung nicht vergessen. &e4.&r Alles verkleben. &e5.&r Im Bahnhofsmenü zusammenbauen.",
              "",
              "Wagen, Sitze, Kisten, Deko: was auf den Drehgestellen klebt, fährt mit.",
          ],
          tasks=[task_checkmark("Zug gebaut")],
          rewards=[reward_item("create:track", 64), reward_xp(8)],
          deps=["controls"], icon="create:controls", size=2.0, shape="diamond"),

    quest("drive", A + 17.5, 8.5, "&6Fahr von Hand",
          subtitle="W, S, und an Weichen A und D.",
          description=[
              "Rechtsklicke die Zugsteuerung. &eW&r und &eS&r fahren, an Weichen wählen &eA&r und &eD&r die Richtung, das Mausrad begrenzt das Tempo.",
              "",
              "Mit gedrückter &eLeertaste&r hält der Zug am nächsten Bahnhof, Schleichen beendet das Fahren. Von Hand fährt er mit &e75 Prozent&r der Fahrplan-Geschwindigkeit.",
          ],
          tasks=[task_checkmark("Gefahren")],
          rewards=[reward_xp(4)],
          deps=["first_train"], icon="minecraft:lever"),

    quest("disassemble", A + 17.5, 10.5, "&6Bau den Zug um",
          subtitle="Zerlegen, verlängern, neu zusammenbauen.",
          description=[
              "Fahr den Zug an einen Bahnhof und schalte dort den &eMontagemodus&r ein. Der Zug zerfällt wieder in Blöcke auf seinen Drehgestellen.",
              "",
              "Jetzt hängst du Wagen an, tauschst Kisten gegen Tresore oder baust eine zweite Zugsteuerung ans Ende. Dann wieder zusammenbauen.",
          ],
          tasks=[task_checkmark("Umgebaut")],
          rewards=[reward_xp(4)],
          deps=["first_train"], icon="create:track_station"),

    quest("doors", A + 15, 12, "&6Bau Zugtüren ein",
          subtitle="Rein und raus, ohne zu klettern.",
          description=[
              "Eine &6Holztür&r und ein &6Zugrahmen&r ergeben eine &6Zugtür&r, eine Falltür und ein Zugrahmen eine &6Zugfalltür&r. Sie gleiten zur Seite und passen in schmale Wagen.",
              pic("create:train_door"),
              "Ein schöner Zug ist die Visitenkarte deiner Basis auf dem Stream.",
          ],
          tasks=[task_item("create:train_door", 2)],
          rewards=[reward_xp(3)],
          deps=["first_train"], optional=True),

    # ---- Fahrplan (column B) ---------------------------------------------------------
    quest("schedule", B, 2.5, "&6Schreib einen Fahrplan",
          subtitle="Er fährt, während du woanders bist.",
          description=[
              "Ein &6Robustes Blech&r und &6Papier&r ergeben vier &6Zugfahrpläne&r. Leg Einträge an: &eFahre zu Bahnhof&r, darunter die Bedingung, wann es weitergeht.",
              pic("create:schedule"),
              "Mit &eWiederholen&r springt der Plan an den Anfang. &eMine*&r passt auf jeden freien Bahnhof, dessen Name mit Mine beginnt. &eÄndere Höchstgeschwindigkeit&r bremst den Zug auf einem Abschnitt.",
          ],
          tasks=[task_item("create:schedule", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(4)],
          deps=["first_train"], icon="create:schedule", size=1.5),

    quest("conductor", B + 2.5, 2.5, "&6Setz einen Schaffner ein",
          subtitle="Jemand muss ja fahren.",
          description=[
              "Setz einen Mob auf den Sitz vor der Zugsteuerung, oder stell einen &6Lohenbrenner&r an dieselbe Stelle. Rechtsklicke ihn mit dem Fahrplan: er übernimmt.",
              "",
              "Die Lohe ist der beliebteste Schaffner, sie braucht nichts und läuft nicht weg. Einen Mob an der Leine setzt du per Klick auf den Sitz.",
          ],
          tasks=[task_checkmark("Schaffner eingesetzt")],
          rewards=[reward_xp(5)],
          deps=["schedule"], icon="create:blaze_burner"),

    quest("auto_line", B + 5, 2.5, "&6Lass eine Linie allein fahren",
          subtitle="Zwei Bahnhöfe, ein Fahrplan, kein Fahrer.",
          description=[
              "Zwei Bahnhöfe, ein Zug mit Schaffner, ein Fahrplan mit zwei Einträgen und &eWiederholen&r. Als Bedingung etwa &eWarte 20 Sekunden&r, damit Mitfahrer in Ruhe einsteigen.",
              "",
              "Sprecht euch ab: ein gemeinsames Netz mit sauber benannten Bahnhöfen hilft allen.",
          ],
          tasks=[task_checkmark("Die Linie läuft")],
          rewards=[reward_item("create:track", 64), reward_xp(6)],
          deps=["conductor"], icon="create:track_station", size=1.5),

    quest("display", B + 7.5, 2.5, "&6Häng eine Abfahrtstafel auf",
          subtitle="Wann kommt der nächste Zug?",
          description=[
              "Setz einen &6Anzeige-Link&r an den Bahnhof und richte ihn auf eine &6Anzeigetafel&r. Wähl im Link die Zuginformationen: die Tafel zeigt, welcher Zug wann kommt und wohin er fährt.",
              "",
              "Wie Link und Tafel gebaut werden, steht in &6Create: Messing&r.",
          ],
          tasks=[task_item("create:display_link", 1), task_item("create:display_board", 6)],
          rewards=[reward_xp(3)],
          deps=["auto_line"], optional=True),

    # ---- Abfahrtsbedingungen: checklist ----------------------------------------------
    condition("cond_delay", B, "&7Festgelegte Verzögerung",
              "Warten, dann weiter.",
              "&eFestgelegte Verzögerung&r: der Zug wartet eine feste Zeit am Bahnhof, dann fährt er."),
    condition("cond_time", B + 2, "&7Tageszeit",
              "Abfahrt nach Uhr.",
              "&eTageszeit&r: der Zug fährt zu einer bestimmten Uhrzeit ab, etwa jeden Morgen zur Mine."),
    condition("cond_items", B + 4, "&7Item-Ladestand",
              "Erst voll, dann los.",
              "&eItem-Ladestand&r: der Zug wartet, bis seine Fracht eine Menge eines Items erreicht oder unterschreitet."),
    condition("cond_redstone", B + 6, "&7Redstone-Signal",
              "Losfahren auf Knopfdruck.",
              "&eBahnhof empfängt RS-Signal&r: der Zug fährt, sobald der Bahnhof ein Redstone-Signal bekommt. Ein Knopf am Bahnsteig reicht."),
    condition("cond_players", B + 8, "&7Sitzauslastung",
              "Fährt, wenn alle sitzen.",
              "&eSitzauslastung&r: der Zug wartet, bis eine Zahl Spieler auf seinen Sitzen Platz genommen hat."),

    # ---- Signale (column B) ----------------------------------------------------------
    quest("signal", B, 10, "&6Teil die Strecke mit Signalen",
          subtitle="Mehrere Züge, keine Unfälle.",
          description=[
              "Ein &6Zugrahmen&r und eine &6Elektronenröhre&r ergeben vier &6Zugsignale&r. Klick sie aufs Gleis und setz sie daneben ab.",
              "",
              "Signale teilen die Strecke in &eAbschnitte&r. Ein Zug fährt nur in einen freien Abschnitt. Auf zweigleisigen Strecken braucht jede Richtung eigene Signale.",
          ],
          tasks=[task_item("create:track_signal", 4)],
          rewards=[reward_item("create:electron_tube", 4), reward_xp(4)],
          deps=["first_train"], icon="create:track_signal"),

    quest("junction", B + 2.5, 10, "&6Sicher eine Kreuzung",
          subtitle="Einfahrtssignal und Kreuzungssignal.",
          description=[
              "Der Schraubenschlüssel stellt ein Signal um. Das &eEinfahrtssignal&r lässt einen Zug in den nächsten freien Abschnitt. Das &eKreuzungssignal&r wartet, bis der Weg bis zum übernächsten Signal frei ist.",
              "",
              "Faustregel: Kreuzungssignal vor der Weiche, Einfahrtssignal dahinter. Sonst bleibt ein Zug mitten auf der Kreuzung stehen. Die Brille zeigt, ob ein Abschnitt belegt ist.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(5)],
          deps=["signal"], icon="create:track_signal", shape="diamond"),

    quest("observer", B + 5, 10, "&6Melde vorbeifahrende Züge",
          subtitle="Der Zugbeobachter.",
          description=[
              "Ein &6Zugrahmen&r und eine &6Druckplatte&r ergeben zwei &6Zugbeobachter&r. Aufs Gleis gesetzt wie ein Signal, gibt er Redstone, solange ein Zug über ihm ist.",
              "",
              "Mit Filter reagiert er nur auf Züge mit einem bestimmten Item. Damit schließt du Schranken oder startest eine Verladeanlage.",
          ],
          tasks=[task_item("create:track_observer", 2)],
          rewards=[reward_xp(3)],
          deps=["junction"], optional=True),

    # ---- Fracht (column B) -----------------------------------------------------------
    quest("cargo", B, 14.5, "&6Lad Fracht am Bahnsteig",
          subtitle="Portable Lagerschnittstellen.",
          description=[
              "Eine &6Portable Lagerschnittstelle&r am Wagen, eine am Bahnsteig, gegenüber, wenn der Zug hält. Kisten oder &6Tresore&r auf dem Zug sind das Frachtlager.",
              "",
              "Eine Schleuse an der festen Schnittstelle entlädt ins Lager oder befüllt den Zug, je nachdem, wie herum sie sitzt.",
          ],
          tasks=[task_item("create:portable_storage_interface", 4), task_item("create:item_vault", 2)],
          rewards=[reward_table("s2_uncommon"), reward_xp(4)],
          deps=["first_train"], icon="create:portable_storage_interface", size=1.5),

    quest("fluid_cargo", B, 16.5, "&bFahr Flüssigkeiten",
          subtitle="Tankwagen.",
          description=[
              "&6Kupferrahmen&r und &6Schacht&r ergeben die &6Portable Flüssigkeitsschnittstelle&r. Tanks auf dem Zug, eine Schnittstelle am Wagen, eine am Bahnsteig, eine Pumpe an der festen Seite.",
              "",
              "So bringt ein Tankzug Lava zu deinen Lüftern oder Wasser zum Dampfkessel.",
          ],
          tasks=[task_item("create:portable_fluid_interface", 2), task_item("create:fluid_tank", 4)],
          rewards=[reward_xp(4)],
          deps=["cargo"], optional=True),

    quest("freight", B + 2.5, 14.5, "&6Lass einen Güterzug pendeln",
          subtitle="Rohstoffe fahren von selbst.",
          description=[
              "Zug mit Frachtlager und Schnittstellen, Fahrplan mit zwei Bahnhöfen, Bedingung &eKein weiterer Güteraustausch&r: der Zug fährt los, sobald Be- oder Entladen eine Weile fertig ist.",
              "",
              "So speist eine Mine am Kartenrand deine Fabrik, oder dein Zink- und Kupferbergwerk die Messing-Mixer.",
          ],
          tasks=[task_checkmark("Der Güterzug fährt")],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["cargo", "auto_line"], icon="create:item_vault"),

    quest("postbox", B + 2.5, 16.5, "&6Schick Pakete per Zug",
          subtitle="Briefkästen an den Bahnhöfen.",
          description=[
              "Farbstoff, &6Fass&r und &6Andesitlegierung&r untereinander ergeben einen &6Briefkasten&r. Rechtsklicke damit einen Bahnhof und setz ihn in der Nähe ab, dann gib ihm eine Adresse.",
              "",
              "Pakete mit fremder Adresse nimmt der nächste haltende Zug mit, passende lädt er dort ab. Im Fahrplan gibt es dafür &ePaket liefern&r und &ePaket holen&r.",
          ],
          tasks=[task_item("create:white_postbox", 2)],
          rewards=[reward_item("create:cardboard", 16), reward_xp(4)],
          deps=["cargo"], icon="create:white_postbox"),

    # ---- Das Ziel -------------------------------------------------------------------
    quest("obelisk_line", B + 6, 20.5, "&6&lFahr eine Linie zum Obelisken",
          subtitle="Alle Wege führen zum Spawn.",
          description=[
              "Ein Bahnhof am Spawn, ein Güterzug, der dort hält, und eine Schleuse, die aus der Portablen Lagerschnittstelle in deinen &eEinspeiser&r lädt. Der Obelisk zieht alle zwei Sekunden ein.",
              "",
              "&eKronwerke:&r Messingbarren und Präzisionsgetriebe in dieser Stufe, Stahl in der nächsten: die Ziele wollen große Mengen, und ein Zug bringt sie ohne Laufen.",
              "",
              "Ein gemeinsamer Hauptbahnhof mit mehreren Gleisen und Kreuzungssignalen ist für dreißig Spieler schöner als dreißig Stummelgleise.",
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
    head("conditions", "Abfahrtsbedingungen", B - 0.6, 4.6, colour="stone"),
    head("signals", "Signale", B - 0.6, 8.2),
    head("cargo", "Fracht", B - 0.6, 12.6),
    head("goal", "Das Ziel", B + 4.6, 18.2),
]
images[0]["x"] = 14
images[1]["x"] = 14

chapter(C, "Create: Züge", "create:controls", "tech", quests, shape="circle", order=15, stage=2,
        subtitle=["Stufe 2: Gleise, Bahnhöfe und Züge, die von selbst fahren."], images=images)
