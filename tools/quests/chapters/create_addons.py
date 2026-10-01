"""The Create addons of stage 2 that have no chapter of their own yet: Steam 'n' Rails beyond the
trains chapter (switches, couplers, semaphores, conductors, fuel tanks, bogeys, special tracks),
Create Connected beyond the parts in create_brass.py (control chip, pulse generator, inventory
bridge, kinetic bridge, gearboxes), Create: Dragons Plus (liquid dye, bulk fan processing, fluid
hatch), Enchantment Industry beyond grindstone, enchanter and printer (templates, forger, cake,
infuser), Create Mechanical Spawner (spawn fluids, loot collector) and Create Diesel Generators
(ethanol, biodiesel, engines, oil scanner). Create Ore Excavation and the jetpack are notes for
stages 3 and 4. Recipes and numbers come from the mod jars and the server configs."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "create_addons"


def head(name, text, left, y, height=0.9, kind="section", colour="brass"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


# Column A starts at x 0, column B at x 17.
A, B = 0, 17

quests = [
    # ---- Steam 'n' Rails (column A) ---------------------------------------------
    quest("welcome", A, 1, "&6&lStell eine Weiche",
          subtitle="Steam 'n' Rails: Weichen, die du selbst schaltest.",
          description=[
              "&eRezept:&r Hebel oben, &6Andesitgehäuse&r in der Mitte, &6Zahnrad&r unten ergeben eine &6Andesit-Weiche&r. Rechtsklicke damit erst ein Gleis mit Abzweigung, dann setz sie bis zu 64 Blöcke daneben ab.",
              "",
              "Rechtsklick stellt die Weiche nach rechts, Schleichen und Rechtsklick nach links. Ein Redstone-Signal stellt sie ebenfalls, ein Signal von unten sperrt sie. Ein Komparator liest 1 für links, 0 für geradeaus und 2 für rechts.",
              "",
              "Dieses Kapitel sammelt die Create-Addons, die noch kein eigenes Kapitel haben: den Rest von &6Steam 'n' Rails&r, Create Connected, Dragons Plus, Enchantment Industry, den Mechanical Spawner und die &6Dieselmotoren&r. Alles davon ist mit &6Stufe 2&r offen. Die Grundlagen stehen in &6Create: Messing&r und &6Create: Züge&r.",
          ],
          tasks=[task_item("railways:track_switch_andesite", 1)],
          rewards=[reward_item("create:track", 32), reward_table("s2_common")],
          icon="railways:track_switch_andesite", size=2.0, shape="hexagon"),

    quest("brass_switch", A + 2.5, 0, "&6Bau eine Messing-Weiche",
          subtitle="Weichen, die auch Fahrplanzüge stellen.",
          description=[
              "&eRezept:&r Hebel oben, &6Messingrahmen&r in der Mitte, &6Präzisionsgetriebe&r unten ergeben eine &6Messing-Weiche&r. Setzen wie die Andesit-Weiche: Gleis anklicken, daneben abstellen.",
              "",
              "Im Wertefeld &eSchaltmodus&r legst du fest, ob die Weiche nur für handgesteuerte Züge gilt oder auch für Züge nach Fahrplan. Wer selbst fährt, kann eine Messing-Weiche schon beim Heranfahren aus dem Zug heraus umstellen.",
              "",
              "Ein &6Anzeige-Link&r an der Weiche schreibt ihre Stellung (geradeaus, links, rechts) auf eine Anzeigetafel.",
          ],
          tasks=[task_item("railways:track_switch_brass", 1)],
          rewards=[reward_item("create:brass_ingot", 8), reward_xp(3)],
          deps=["welcome"]),

    quest("coupler", A + 2.5, 2, "&6Setz einen Zugkuppler",
          subtitle="Wagen an- und abhängen, ohne den Zug zu zerlegen.",
          description=[
              "&eRezept:&r &6Eisenblech&r oben, &6Redstone&r in der Mitte, &6Zugrahmen&r unten ergeben einen &6Zugkuppler&r. Rechtsklicke damit ein Gleis und setz ihn daneben ab, wie einen Bahnhof.",
              "",
              "Der Kuppler markiert zwei Punkte auf dem Gleis. Steht über jedem Punkt die Mitte eines Drehgestells, beide Wagen in dieselbe Richtung, dann hängt ein &cRedstone-Signal&r die Züge zusammen oder trennt sie. Mit dem Schraubenschlüssel wechselst du zwischen Kuppeln, Entkuppeln und beidem, Scrollen mit dem Schlüssel ändert den Abstand der beiden Punkte.",
              "",
              "&eTipp:&r Ein Bahnhof direkt davor hilft beim Ausrichten. So wechselt ein Güterzug seine Wagen am Bahnsteig, während die Lok weiterfährt. Die Ponder-Ansicht (&eW&r) zeigt den ganzen Ablauf.",
          ],
          tasks=[task_item("railways:track_coupler", 1)],
          rewards=[reward_item("create:railway_casing", 4), reward_xp(3)],
          deps=["welcome"]),

    quest("semaphore", A + 5, 2, "&6Häng Semaphoren auf",
          subtitle="Signale, die man von weitem sieht.",
          description=[
              "&eRezept:&r zwei &6Eisenbleche&r oben und unten, in der Mitte Zaun, &6Andesitgehäuse&r und &6Elektronenröhre&r ergeben vier &6Semaphoren&r. Setz einen Mast aus Zäunen oder Metallträgern über ein &6Zugsignal&r und häng die Semaphore daran.",
              "",
              "Die Semaphore zeigt mit Flügel und Licht den Zustand des Signals unter dem Mast, frei oder belegt. Vor einem Kreuzungssignal mit mehreren Ausfahrten kannst du eine zweite Semaphore darüber setzen: die untere schließt, sobald einer der Wege blockiert ist, die obere erst, wenn alle blockiert sind.",
              "",
              "Rein optisch, aber auf einem Bahnhof mit sechs Gleisen sieht man so von der Lok aus, was los ist.",
          ],
          tasks=[task_item("railways:semaphore", 4)],
          rewards=[reward_item("create:electron_tube", 2), reward_xp(3)],
          deps=["welcome"]),

    quest("conductor", A + 5, 0, "&6Stell einen Schaffner ein",
          subtitle="Eine Mütze, ein Andesitgehäuse, ein Mitarbeiter.",
          description=[
              "Die &6Schaffnermütze&r entsteht durch &esequenzielle Montage&r: ein Block &6Wolle&r aufs Band, eine &6Mechanische Säge&r schneidet ihn zu, ein Einsatzgerät setzt ein &6Präzisionsgetriebe&r ein, ein zweites einen &6Faden&r. Jede Wollfarbe gibt eine eigene Mütze.",
              "",
              "Rechtsklicke mit der Mütze ein gesetztes &6Andesitgehäuse&r: daraus wird ein &6Schaffner&r. Setz ihn auf den Sitz vor der Zugsteuerung und gib ihm den Fahrplan, dann fährt er wie eine Lohe oder ein Dorfbewohner, nur dass er nicht wegläuft.",
              "",
              "Schaffner drücken Knöpfe und kippen Hebel, sobald du sie anschaust, bis 16 Blöcke weit. Trägst du selbst eine Mütze in einer anderen Farbe, lassen sie es. Eine &6Werkzeugkiste&r von Create funktioniert auf ihnen wie bei dir.",
          ],
          tasks=[task_item("railways:white_conductor_cap", 1)],
          rewards=[reward_item("minecraft:white_wool", 8), reward_table("s2_common")],
          deps=["coupler"], icon="railways:white_conductor_cap", size=1.5),

    quest("whistle", A + 7.5, 0, "&6Pfeif den Zug herbei",
          subtitle="Schaffnerpfeife und Fernlinse.",
          description=[
              "Ein &6Kupferbarren&r und ein &6Messingklumpen&r ergeben die &6Schaffnerpfeife&r. Rechtsklicke damit deinen Schaffner, der auf einem Zug sitzt, dann ist sie an ihn gebunden. Rechtsklick auf ein Gleis oder einen Bahnhof, und der Zug kommt dorthin.",
              img(item_texture("railways:conductor_whistle"), 32, 32),
              "Ein Einsatzgerät mit der Pfeife kann einen Zug an einen Bahnhof rufen, und ein Klick in die Luft bricht die Fahrt wieder ab.",
              "",
              "Die &6Fernlinse&r (Präzisionsgetriebe, Enderauge, Messingblech) bindest du an einen Schaffner mit &6Ingenieursbrille&r. Danach siehst du durch seine Augen, auch wenn der Zug am anderen Ende der Karte ist.",
          ],
          tasks=[task_item("railways:conductor_whistle", 1), task_item("railways:remote_lens", 1)],
          rewards=[reward_item("create:track", 32), reward_xp(5)],
          deps=["conductor"], icon="railways:conductor_whistle"),

    quest("fuel", A + 7.5, 2, "&6Tank Diesel in den Zug",
          subtitle="Mit Brennstoff fahren Züge 40 statt 28 Blöcke pro Sekunde.",
          description=[
              "&eRezept:&r &6Robustes Blech&r oben, &6Flüssigkeitstank&r in der Mitte, &6Robustes Blech&r unten ergeben einen &6Treibstofftank&r. &6Zugrahmen&r und &6Schacht&r ergeben die &6Portable Treibstoffschnittstelle&r, die den Tank am Bahnhof befüllt, so wie die Flüssigkeitsschnittstelle einen Tankwagen.",
              "",
              "Ein Zug, der Brennstoff verbrennt, fährt mit &e40 statt 28 Blöcken pro Sekunde&r und 20 statt 14 in Kurven. Ohne Treibstofftank geht das auch mit einer Kiste voll Kohle auf dem Zug, der Tank nimmt stattdessen &bDiesel&r und &bBiodiesel&r aus den Dieselmotoren weiter unten in diesem Kapitel.",
              "",
              "Auf Kronwerke brauchen Züge keinen Brennstoff, um überhaupt zu fahren. Der Tank ist ein Turbo, kein Zwang. Wasser nimmt er nicht an.",
          ],
          tasks=[task_item("railways:fuel_tank", 1), task_item("railways:portable_fuel_interface", 1)],
          rewards=[reward_item("create:sturdy_sheet", 4), reward_xp(5)],
          deps=["semaphore"], icon="railways:fuel_tank"),

    quest("bogeys", A + 10, 1, "&6Bau eine richtige Lok",
          subtitle="Drehgestelle in allen Größen, Kessel und Schlote.",
          description=[
              "Halte einen &6Zugrahmen&r in der Hand und drück &eAlt&r: das &6Drehgestell-Menü&r öffnet sich. Dort wählst du den Stil, der beim Klick aufs Gleis gesetzt wird: einfache Achsen, Doppel- und Dreifachachsen, große Lokfahrwerke mit bis zu sechs Achsen, dazu Favoriten.",
              "",
              "Es gibt drei Spurweiten. Normale Gleise tragen die Standard-Drehgestelle, &eschmale&r und &ebreite&r Gleise entstehen wie normale durch sequenzielle Montage und haben eigene Fahrwerke. Phantomgleise passen zu allen.",
              "",
              "&eFür die Optik:&r Ein &6Eisenblock&r im Steinschneider ergibt acht &6Locometal&r, aus dem Lokkessel, Rauchkammern, Türen und Leitern gebaut werden. &6Schlote&r (Eisenbleche um ein Lagerfeuer) rauchen auf der Fahrt, mit Farbstoff bunt, mit Seelensand blau. Mit &eAlt&r wechselst du bei vielen dieser Blöcke die Variante.",
          ],
          tasks=[task_item("railways:riveted_locometal", 8), task_item("railways:smokestack_streamlined", 1)],
          rewards=[reward_item("minecraft:iron_block", 2), reward_xp(5)],
          deps=["fuel", "whistle"], icon="railways:smokestack_streamlined", size=1.5),

    quest("tracks", A + 12.5, 1, "&6Verleg eine Einschienenbahn",
          subtitle="Monorail, Endergleis, Phantomgleis.",
          description=[
              "&6Einschienengleis&r entsteht durch sequenzielle Montage: ein &6Metallträger&r aufs Band, ein Einsatzgerät setzt eine &6Metallstrebe&r, eines ein &6Eisenblech&r, eine Presse drückt, sechs Gleise pro Träger. Darauf fährt ein eigenes Monorail-Drehgestell, das du wie gewohnt mit dem Zugrahmen aufs Gleis klickst. Die Schiene kann auch über dem Zug hängen.",
              "",
              "&6Phantomgleise&r (Phantomhaut, Eisen, 32 Stück pro Haut) sind unsichtbar, solange du keins in der Hand hast, und passen zu jeder Spurweite. &6Endergleise&r aus Endsteinziegelstufen kommen mit dem End in Stufe 4. &6Gleise ohne Schwellen&r gibt es für Brücken aus Metallträgern.",
              "",
              "&eTipp:&r Rechtsklick mit einer Stufe auf ein Gleis setzt sie als Verkleidung darunter. Schnee und Moos gehen auch.",
          ],
          tasks=[task_item("railways:track_monorail", 12)],
          rewards=[reward_item("create:metal_girder", 16), reward_xp(5)],
          deps=["bogeys"], icon="railways:track_monorail", optional=True),

    # ---- Create Connected (column A) --------------------------------------------
    quest("gearboxes", A, 8, "&6Bau ein Messing-Getriebe",
          subtitle="Create Connected: Getriebe, die mehr können.",
          description=[
              "Vier &6Zahnräder&r um einen &6Drehzahlregler&r ergeben ein &6Messing-Getriebe&r. Jede seiner vier Seiten lässt sich mit dem Schraubenschlüssel einzeln auf vorwärts oder rückwärts stellen.",
              "",
              "Das &66-Wege-Getriebe&r (Andesitgehäuse, drei Zahnräder und zwei große Zahnräder, oder ein Getriebe plus zwei große Zahnräder) hat Wellen an allen sechs Seiten, oben und unten mit halber Drehzahl. Der &6Kreuzverbinder&r (vier Wellen um ein Getriebe) führt zwei Wellen unabhängig voneinander durch denselben Block.",
              "",
              "Dazu kommen das &6Armaturenbrett&r (Anzeigetafel auf Messingrahmen), eine kleine Anzeige mit vier Zeilen, deren Inhalt Spieler auf einem Sitz davor als Einblendung sehen, und der &6Messingschacht&r, der 64 Items auf einmal bewegt.",
          ],
          tasks=[task_item("create_connected:brass_gearbox", 1), task_item("create_connected:six_way_gearbox", 1)],
          rewards=[reward_item("create:cogwheel", 8), reward_table("s2_common")],
          deps=["welcome"], icon="create_connected:brass_gearbox", size=1.5),

    quest("control_chip", A + 2.5, 7, "&6Fertige einen Steuerchip",
          subtitle="Drei Runden auf einem Goldblech.",
          description=[
              "Der &6Steuerchip&r entsteht durch sequenzielle Montage wie das Präzisionsgetriebe: ein &6Goldblech&r aufs Band, ein Einsatzgerät setzt eine &6Elektronenröhre&r, eines &6Redstone&r, eine Presse drückt. &eDrei Runden&r, dann ist er fertig.",
              img(item_texture("create_connected:control_chip"), 32, 32),
              "In 80 Prozent der Fälle kommt ein Chip heraus, sonst Redstone, eine Röhre oder ein Goldblech zurück, selten etwas anderes. Deutlich gnädiger als die 60 Prozent des Präzisionsgetriebes.",
              "",
              "Der Chip steckt im Sequenziellen Impulsgeber. Eine bestehende Präzisionslinie baust du mit einem Filterwechsel schnell darauf um.",
          ],
          tasks=[task_item("create_connected:control_chip", 2)],
          rewards=[reward_item("create:golden_sheet", 8), reward_xp(5)],
          deps=["gearboxes"], icon="create_connected:control_chip"),

    quest("pulse_generator", A + 5, 7, "&6Programmiere Redstone",
          subtitle="Sequenzieller Impulsgeber und Funk-Sender.",
          description=[
              "&eRezept:&r zwei &6Elektronenröhren&r links, &6Steuerchip&r oben Mitte, &6Messingblech&r in der Mitte, &6Redstone-Fackel&r rechts, unten drei Stein ergeben den &6Sequenziellen Impulsgeber&r.",
              "",
              "Rechtsklick öffnet sein Programm: eine zeitlich geordnete Liste von Signalen, die er abspielt, sobald von hinten ein Signal kommt. Danach wartet er auf das nächste. Ein Signal von der Seite bricht ab, ein Komparator liest den Fortschritt. Damit öffnet ein Knopf erst das Tor, dann die Schranke, dann die Lampe, in genau der Reihenfolge.",
              "",
              "Der &6Funk-Sender&r ist eine umgewandelte Redstone-Verbindung: Rechtsklick auf einen Hebel, Knopf oder analogen Hebel, und dessen Signal wird kabellos bis 128 Blöcke weit an Empfänger derselben Frequenz gefunkt. Honigwabe wachst ihn gegen Fehlklicks, die Axt löst das Wachs wieder.",
          ],
          tasks=[task_item("create_connected:sequenced_pulse_generator", 1), task_item("create_connected:linked_transmitter", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(5)],
          deps=["control_chip"], icon="create_connected:sequenced_pulse_generator"),

    quest("inventory_bridge", A + 2.5, 9, "&6Verbinde zwei Lager",
          subtitle="Lagerzugang und Lagerbrücke.",
          description=[
              "&eRezept:&r &6Messingrahmen&r oben, &6Schacht&r in der Mitte, &6Elektronenröhre&r unten ergeben zwei &6Lagerzugänge&r. Zwei Lagerzugänge zusammen sind eine &6Lagerbrücke&r.",
              "",
              "Ein &6Lagerzugang&r an einer Kiste oder einem Tresor verlängert das Lager um einen Block: Schleusen, Arme und Schächte am Zugang arbeiten, als hingen sie direkt an der Kiste. Mehrere Zugänge pro Lager gehen, hintereinander nicht. Ein Redstone-Signal schaltet ihn ab.",
              "",
              "Die &6Lagerbrücke&r zwischen zwei Kisten macht aus beiden einen Zugriffspunkt. Ihre zwei Filterfelder legen fest, welches Item auf welche Seite geht. Was zu keinem Filter passt, nimmt sie nicht an. Für enge Fabriken ein Segen.",
          ],
          tasks=[task_item("create_connected:inventory_access_port", 2), task_item("create_connected:inventory_bridge", 1)],
          rewards=[reward_item("create:brass_casing", 2), reward_xp(5)],
          deps=["gearboxes"], icon="create_connected:inventory_bridge"),

    quest("kinetic_bridge", A + 5, 9, "&6Sichere dein Netz ab",
          subtitle="Kinetische Brücke, Überlastkupplung, Scherstift.",
          description=[
              "&eRezept:&r &6Messingrahmen&r oben und unten, &6Welle&r, &6Kupplung&r, &6Welle&r in der Mitte ergeben die &6Kinetische Brücke&r. Sie gibt eine feste Menge Belastbarkeit, die du im Wertefeld einstellst, von einem Wellennetz an ein zweites weiter und hält beide getrennt: ist das eine überlastet, läuft das andere weiter.",
              "",
              "Die &6Überlastkupplung&r (Andesitgehäuse, Welle, Eisenblech, Elektronenröhre) kuppelt nach einer einstellbaren Verzögerung aus, sobald das Netz überlastet ist, und mit dem Schraubenschlüssel wieder ein. Der &6Scherstift&r ist eine Welle aus der Mechanischen Säge: er bricht bei Überlast ein einziges Mal und schützt so den Rest.",
              "",
              "&eTipp:&r Eine Überlastkupplung vor der Brücke gibt die Belastbarkeit frei, die eine überlastete Brücke sonst weiter verbrauchen würde. Die Ponder-Szene rechnet es vor.",
          ],
          tasks=[task_item("create_connected:kinetic_bridge", 1), task_item("create_connected:overstress_clutch", 1),
                 task_item("create_connected:shear_pin", 2)],
          rewards=[reward_item("create:shaft", 16), reward_table("s2_common")],
          deps=["gearboxes"], icon="create_connected:kinetic_bridge"),

    # ---- Dragons Plus (column A) ------------------------------------------------
    quest("liquid_dye", A, 14, "&dMisch flüssigen Farbstoff",
          subtitle="Create: Dragons Plus. Ein Farbstoff, 250 mB Wasser.",
          description=[
              "Ein &6Farbstoff&r und &b250 mB Wasser&r im &6Mixer&r ergeben &d250 mB flüssigen Farbstoff&r in dieser Farbe. Erhitzt zurückgemischt wird aus 250 mB wieder ein Farbstoff-Item.",
              "",
              "Was in den Farbstoff fällt, wird gefärbt: Items ebenso wie Tiere und Spieler. Trifft flüssiger Farbstoff auf &cLava&r, entsteht &6Beton&r in derselben Farbe. Ein Eimer davon ist eine Zutat für die Lüfter-Katalysatoren von Create Connected.",
              "",
              "Die Flasche &dDrachenatem&r wird mit Dragons Plus ebenfalls zur Flüssigkeit, 250 mB pro Flasche, aber Drachenatem gibt es erst mit dem End in Stufe 4.",
          ],
          tasks=[task_checkmark("Flüssigen Farbstoff gemischt")],
          rewards=[reward_item("minecraft:white_dye", 16), reward_xp(3)],
          deps=["welcome"], icon="create_dragons_plus:white_dye_bucket", shape="diamond"),

    quest("bulk_fan", A + 2.5, 14, "&dFärbe und friere mit dem Lüfter",
          subtitle="Vier neue Lüfter-Verfahren.",
          description=[
              "Ein &6Ummantelter Lüfter&r, der durch &dflüssigen Farbstoff&r bläst, färbt alles im Luftstrom: Wolle, Glas, Betonpulver und alles andere, was sich an der Werkbank färben lässt, dazu Tiere und Rüstung. Ordentlicher geht es mit dem &6Leeren Lüfter-Katalysator&r aus Create Connected und einem Eimer Farbstoff darauf.",
              "",
              "Ein Lüfter durch &bPulverschnee&r (oder der Katalysator mit einem Pulverschnee-Eimer) &efriert&r: Eis wird zu Packeis, Packeis zu Blaueis, Magmacreme zu Schleim und eine Lohenrute zu einer Böenrute. Der Katalysator mit &6Sand&r &eschleift&r wie Schmirgelpapier, zum Beispiel Rosenquarz für Elektronenröhren, ohne dass ein Einsatzgerät Papier verbraucht.",
              "",
              "Das vierte Verfahren, &5Enden&r hinter einem Drachenkopf (Bruchstein zu Endstein, Apfel zu Chorusfrucht, Leder zu Phantomhaut), kommt in Stufe 4.",
          ],
          tasks=[task_item("create_connected:fan_freezing_catalyst", 1), task_item("create_connected:fan_sanding_catalyst", 1)],
          rewards=[reward_item("minecraft:packed_ice", 16), reward_table("s2_common")],
          deps=["liquid_dye"], icon="create_connected:fan_freezing_catalyst", size=1.5),

    quest("fluid_hatch", A + 5, 14, "&dSetz eine Flüssigkeitsluke",
          subtitle="Eimer rein, Eimer raus, ohne Rohr.",
          description=[
              "Ein &6Kupferbarren&r und ein &6Abfluss&r ergeben die &6Flüssigkeitsluke&r. Setz sie an einen Tank: Rechtsklick mit einem vollen Eimer leert ihn in den Tank, Schleichen und Rechtsklick füllt den Eimer aus dem Tank. Geht mit jedem Behälter, auch Flaschen und Kanistern.",
              "",
              "Rechtsklickst du eine gesetzte Luke mit einem &6Erfahrungsblock&r (neun Erfahrungsklumpen aus dem Mahlwerk), wird sie zur &6Erfahrungsluke&r von Enchantment Industry: Rechtsklick zahlt deine Level als flüssige Erfahrung in den Tank ein, Schleichen und Rechtsklick holt sie zurück. Wie viel pro Klick, stellst du am Wertefeld ein.",
              "",
              "Die &6Erfahrungslaterne&r (Erfahrungsblock, Schwamm, Kupferrahmen) saugt Erfahrungskugeln und Erfahrung von Spielern in der Nähe auf und speichert 1 000 mB, auch auf einer Kontraption.",
          ],
          tasks=[task_item("create_dragons_plus:fluid_hatch", 1), task_item("create_enchantment_industry:experience_hatch", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(5)],
          deps=["liquid_dye"], icon="create_enchantment_industry:experience_hatch"),

    # ---- Enchantment Industry (column B) ----------------------------------------
    quest("enchanting_template", B, 1, "&5Press eine Verzauberungsvorlage",
          subtitle="Enchantment Industry: Verzauberungen als Item.",
          description=[
              "Eine &6Mechanische Presse&r drückt einen &6Erfahrungsblock&r zur leeren &6Verzauberungsvorlage&r. Der Erfahrungsblock entsteht aus neun Erfahrungsklumpen oder aus &b27 mB flüssiger Erfahrung&r, verdichtet von einer Presse über einem Becken.",
              img(item_texture("create_enchantment_industry:enchanting_template"), 32, 32),
              "Eine Vorlage trägt eine Verzauberung wie ein Buch, aber Maschinen können sie lesen und schreiben: der &6Lohen-Verzauberer&r aus &6Create: Messing&r füllt sie, der &6Lohen-Schmied&r im nächsten Schritt überträgt sie auf Werkzeug und Rüstung oder zieht Verzauberungen von Items ab.",
              "",
              "Flüssige Erfahrung bekommst du am Mechanischen Schleifstein aus Erfahrungsklumpen, aus der Erfahrungsluke oder aus Erfahrungsflaschen (10 mB pro Flasche am Abfluss).",
          ],
          tasks=[task_item("create_enchantment_industry:enchanting_template", 2)],
          rewards=[reward_item("create:experience_nugget", 16), reward_xp(5)],
          deps=["welcome"], icon="create_enchantment_industry:enchanting_template", size=1.5),

    quest("blaze_forger", B + 2.5, 0, "&5Bau den Lohen-Schmied",
          subtitle="Ein Amboss, der nie teurer wird.",
          description=[
              "Am &6Schmiedetisch&r: die &6Lohen-Upgrade-Schmiedevorlage&r, ein &6Lohenbrenner&r und ein &6Amboss&r ergeben den &6Lohen-Schmied&r. Die Vorlage ist dieselbe wie beim Lohen-Verzauberer, woher sie kommt, steht in &6Create: Messing&r. Der Lohenbrenner braucht auf Kronwerke zwei Quelljuwelen.",
              "",
              "Gib ihm per Rohr &bflüssige Erfahrung&r (Tank 4 000 mB). Im Normalmodus vereint er Verzauberungen zweier gleicher Items wie ein Amboss, aber ohne steigende Reparaturkosten. Am Seitenfeld schaltest du um: &eAnwenden&r überträgt eine Verzauberungsvorlage auf ein Item, &eExtrahieren&r zieht eine Verzauberung von Werkzeug, Buch oder Vorlage auf eine leere Vorlage.",
              "",
              "Ein &6Mechanischer Arm&r legt Items ein, füttert Erfahrung nach und nimmt das Ergebnis heraus. So wird aus einer Kiste alter Zauberbücher ein Lager sortierter Vorlagen.",
          ],
          tasks=[task_item("create_enchantment_industry:blaze_forger", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["enchanting_template"], icon="create_enchantment_industry:blaze_forger", size=1.75, shape="gear"),

    quest("experience_cake", B + 2.5, 2, "&5Back einen Zauberkuchen",
          subtitle="Super-Verzaubern bis Stufe 60, mit Blitzableiter.",
          description=[
              "Ein &6Ei&r, &6Zucker&r und &6Lapislazuli&r, von der Presse über einem Becken verdichtet, ergeben die &6Kuchenbasis&r. Ein &6Ausguss&r füllt &b1 000 mB flüssige Erfahrung&r hinein: fertig ist der &6Zauberkuchen&r.",
              img(item_texture("create_enchantment_industry:experience_cake"), 32, 32),
              "Gib ihn einem Lohen-Verzauberer oder Lohen-Schmied, und die Lohe brodelt: &eSuper-Verzaubern&r. Der Verzauberer geht dann bis &eStufe 60&r statt 30 und erzeugt auch Schatzverzauberungen, der Schmied vereint Verzauberungen über die normale Höchststufe hinaus, sogar sich widersprechende. Beide nehmen in diesem Zustand nur &6Super-Verzauberungsvorlagen&r an: gepresst aus einem &6Super-Erfahrungsblock&r, den ein Blitz aus einem Erfahrungsblock macht.",
              "",
              "&cWichtig:&r Super-Verzaubern zieht Blitze an. Stell einen &6Blitzableiter&r daneben, sonst trifft es die Maschine. Überdachen geht auch, bringt aber Flüche oder Reparaturkosten.",
          ],
          tasks=[task_item("create_enchantment_industry:experience_cake", 1)],
          rewards=[reward_item("minecraft:lightning_rod", 2), reward_item("minecraft:lapis_lazuli", 16)],
          deps=["enchanting_template"], icon="create_enchantment_industry:experience_cake", optional=True),

    quest("infuser", B + 5, 1, "&5Bau den Infusor",
          subtitle="Apotheosis-Infusion am Fließband.",
          description=[
              "&eRezept:&r &6Messingblech&r oben, &6Ausguss&r in der Mitte, drei &6Nixie-Röhren&r unten ergeben den &6Infusor&r. Setz ihn über ein &6Becken&r und gib ihm &bflüssige Erfahrung&r.",
              "",
              "Er macht die Infusionsrezepte von &dApotheosis&r automatisch, die sonst am Zaubertisch laufen. Wie der Zaubertisch braucht er Bücherregale rundherum für die Werte Eterna, Quanta und Arcana, die Obergrenzen der Rezepte darf er ignorieren.",
              "",
              "Der &6Edelsteinschneider&r (Amethyst, Messing, Edelsteinstaub) wertet Apotheosis-Edelsteine auf einem Band oder Depot auf und braucht einen Tank Kristallessenz zwei Blöcke unter sich. Das &6Messing-Bücherregal&r, das die Werte frei einstellt, braucht ein Perlenregal aus dem End und kommt in Stufe 4.",
          ],
          tasks=[task_item("create_enchantment_industry:infuser", 1)],
          rewards=[reward_item("create:nixie_tube", 2), reward_table("s2_common")],
          deps=["blaze_forger"], icon="create_enchantment_industry:infuser"),

    # ---- Mechanical Spawner (column B) ------------------------------------------
    quest("spawn_fluid", B, 7, "&cMisch Spawnflüssigkeit",
          subtitle="Create Mechanical Spawner: Erfahrung und Wasser, erhitzt.",
          description=[
              "Im &cerhitzten&r Mixer ergeben &b500 mB flüssige Erfahrung&r und &b500 mB Wasser&r einen Eimer &6Zufällige Spawnflüssigkeit&r. Ohne Erfahrung geht es auch: eine &6Lohenrute&r, eine &6Enderperle&r und 250 mB Wasser ergeben erhitzt 250 mB.",
              img(item_texture("create_mechanical_spawner:spawn_fluid_random_bucket"), 32, 32),
              "Der &6Mechanical Spawner&r (Rezept für die Handwerkseinheiten, siehe &6Create: Messing&r) verbraucht &e100 mB pro Mob&r und braucht mindestens &e100 RPM&r von unten. Flüssigkeit kommt von jeder waagerechten Seite hinein, sein Tank fasst 1 000 mB. Mit der zufälligen Sorte spawnt er irgendein Tier oder Monster.",
              "",
              "Er kostet 16 SU pro RPM, bei 100 RPM also 1 600 SU. Ein Fall für Dampf oder Diesel.",
          ],
          tasks=[task_item("create_mechanical_spawner:spawn_fluid_random_bucket", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 4), reward_xp(5)],
          deps=["welcome"], icon="create_mechanical_spawner:spawn_fluid_random_bucket", size=1.5),

    quest("mob_fluids", B + 2.5, 6, "&cBestimme den Mob",
          subtitle="Eine Zutat macht aus Zufall eine Sorte.",
          description=[
              "&e100 mB zufällige Spawnflüssigkeit&r und eine Zutat ergeben im Mixer &e250 mB&r einer festen Sorte: &6Verrottetes Fleisch&r für Zombies, &6Knochen&r für Skelette, &6Schwarzpulver&r für Creeper, &6Leder und Weizen&r für Kühe, &6Smaragd&r für Dorfbewohner.",
              "",
              "Manche brauchen Hitze: &6Lohenrute&r für Lohen und &6Enderperle&r für Endermen im erhitzten, &6Smaragd und Buch&r für Magier im überhitzten Becken. JEI listet alle Sorten unter Mixen.",
              "",
              "&eKronwerke:&r Eine Lohenfarm aus dem Spawner liefert die Lohenruten für den Lohenstaub im Messing, ganz ohne Festung.",
          ],
          tasks=[task_item("create_mechanical_spawner:spawn_fluid_zombie_bucket", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 16), reward_xp(5)],
          deps=["spawn_fluid"], icon="create_mechanical_spawner:spawn_fluid_zombie_bucket"),

    quest("loot_collector", B + 2.5, 8, "&cBau einen Beutesammler",
          subtitle="Die Beute ohne den Mob.",
          description=[
              "Der &6Beutesammler&r ist ein 5 x 5 Rezept für die Handwerkseinheiten: &6Messingbarren&r in den Ecken und an den Seiten, &6Messingbleche&r oben und unten, &6Eisengitter&r innen und ein &6Fass&r in der Mitte.",
              "",
              "Stell ihn an den Spawnpunkt des Spawners (am Wertefeld stellst du ein, wie hoch über dem Spawner der liegt). Dann erscheint kein Mob mehr, sondern seine Beute landet direkt im Sammler, 8 Stapel Platz. Ein Gegenstandstresor von Create geht als Sammler ebenfalls. Kein Kampf, kein Lärm, keine Creeper-Löcher.",
              "",
              "Der &6Verstärkte Messingrahmen&r (Eisenblock auf einen Messingrahmen anwenden) und das &6Dunkle Rahmenglas&r (Rahmenglas und Kohle) sind die passenden Blöcke für einen gesicherten Spawnraum.",
          ],
          tasks=[task_item("create_mechanical_spawner:loot_collector", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["spawn_fluid"], icon="create_mechanical_spawner:loot_collector", size=1.5),

    # ---- Diesel (column B) ------------------------------------------------------
    quest("ethanol", B, 13, "&6Vergäre Ethanol",
          subtitle="Create Diesel Generators: Zucker und Knochenmehl.",
          description=[
              "Drei &6Andesitlegierungen&r und eine &6Uhr&r ergeben den &6Beckendeckel&r. Setz ihn auf ein &6Becken&r: &6Zucker&r, &6Äpfel&r, &6Kartoffeln&r oder &6Zuckerrohr&r mit &6Knochenmehl&r vergären darin zu &b200 mB Ethanol&r. Ohne Mixer, ohne Hitze.",
              "",
              "Mehr bringt der &6Massenfermenter&r (zwei Andesitlegierungen und ein Fass): dieselben Zutaten ergeben &b400 mB&r. Er macht außerdem aus vier Zuckerrohr und Wasser Zellstoff für Karton und aus &6Bruchstein&r &c50 mB Lava&r, ein unendlicher Lavatropf aus dem Bruchsteingenerator.",
              "",
              "&6Pflanzenöl&r ist die zweite Hälfte des Biodiesels: eine Presse über einem Becken verdichtet &6Samen&r zu &b100 mB&r. Eine Weizenfarm mit Erntemaschine liefert beides, Zucker aus Zuckerrohr und Samen aus dem Weizen.",
          ],
          tasks=[task_item("createdieselgenerators:basin_lid", 1), task_item("createdieselgenerators:bulk_fermenter", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_item("minecraft:sugar", 16)],
          deps=["welcome"], icon="createdieselgenerators:bulk_fermenter", size=1.5),

    quest("biodiesel", B + 2.5, 13, "&6Misch Biodiesel",
          subtitle="Öl und Ethanol, eins zu eins.",
          description=[
              "&b100 mB Pflanzenöl&r und &b100 mB Ethanol&r ergeben im Mixer &b200 mB Biodiesel&r, ohne Hitze. Er ist der Brennstoff für die Dieselmotoren im nächsten Schritt und für die Treibstofftanks der Züge.",
              img(item_texture("createdieselgenerators:biodiesel_bucket"), 32, 32),
              "Der &6Kanister&r (Andesitlegierung, Eisenbleche, Fass) fasst 4 000 mB, behält seinen Inhalt beim Abbauen und wird am Ausguss befüllt. Das &6Ölfass&r (zwei Eisenbleche und ein Fass) ist ein Tank, der auch liegend geht.",
              "",
              "Der Biodiesel von Immersive Engineering brennt in den Motoren genauso. Und der &6Lohenbrenner mit Strohhalm&r aus Crafts & Additions heizt mit einem Eimer Biodiesel &e20 Minuten&r lang, also auch Dampfkessel.",
          ],
          tasks=[task_item("createdieselgenerators:biodiesel_bucket", 1)],
          rewards=[reward_item("createdieselgenerators:canister", 1), reward_xp(5)],
          deps=["ethanol"], icon="createdieselgenerators:biodiesel_bucket"),

    quest("diesel_engine", B + 5, 13, "&6&lBau einen Dieselmotor",
          subtitle="96 RPM und 4 096 SU aus einem Block.",
          description=[
              "&eRezept:&r &6Feuerzeug&r oben, zwei &6Motorkolben&r links und rechts von einem &6Messingblock&r, unten zwei &6polierte Schwarzsteinstufen&r mit einem &6Flüssigkeitstank&r dazwischen. Ein Motorkolben entsteht aus Andesitlegierung, Welle und Zinkklumpen schräg, zwei Stück pro Rezept.",
              img(item_texture("createdieselgenerators:engine_piston"), 32, 32),
              "Pump Brennstoff hinein, Eimer nimmt er auf Kronwerke nicht. Mit &bBiodiesel&r läuft er mit &e96 RPM&r und &e4 096 SU&r, mit &bDiesel&r 6 144 SU, mit Ethanol 2 048 SU, und er trinkt dabei &e1 mB pro Sekunde&r. Ein Eimer hält also 16 Minuten. Ein Redstone-Signal hält ihn an, ein analoger Hebel regelt ihn.",
              "",
              "&eUpgrades:&r Der &6Turbolader&r (Propeller, Rohr, Zink, Eisenbleche, Andesit) verdoppelt die Drehzahl bei gleichem Verbrauch, der &6Schalldämpfer&r (Wolle, Rohr, Eisenbleche) macht ihn leise. Rechtsklick auf den Motor baut sie an.",
              "",
              "&eKronwerke:&r Zum Vergleich trägt ein Wasserrad 256 SU. Ein Dieselmotor treibt einen Messing-Mixer samt Presse und Einsatzgeräten einer Präzisionslinie allein an, und das auf einem einzigen Block.",
          ],
          tasks=[task_item("createdieselgenerators:diesel_engine", 1)],
          rewards=[reward_item("createdieselgenerators:engine_turbocharger", 1), reward_table("s2_uncommon"), reward_xp(8)],
          deps=["biodiesel"], icon="createdieselgenerators:diesel_engine", size=1.75, shape="gear"),

    quest("modular_engine", B + 7.5, 13, "&6&lDas Dieselkraftwerk",
          subtitle="Modulare Motoren, gestapelt.",
          description=[
              "&eRezept:&r &6Andesitlegierung&r oben, &6Dieselmotor&r zwischen zwei &6Messingblechen&r, &6polierte Schwarzsteinstufe&r unten ergeben den &6Modularen Dieselmotor&r.",
              "",
              "Er arbeitet wie der normale Motor, aber du kannst mehrere &eaufeinanderstapeln&r. Jeder Block im Stapel bringt seine Belastbarkeit ein: einer schafft mit Biodiesel &e6 144 SU&r, mit Diesel 8 192 SU, vier Stück entsprechend das Vierfache, alle mit 96 RPM an einer Welle. Jeder frisst seinen eigenen Liter pro Sekunde, also plane die Biodiesel-Linie groß genug.",
              "",
              "&eSo wird es ein Kraftwerk:&r Zuckerrohr- und Weizenfarm, Massenfermenter und Presse für Öl, ein Mixer für Biodiesel, ein Tank, und daran der Motorstapel. Alles ohne Lohenbrenner, ohne Kohle, ohne Wasserrad-Wald.",
              "",
              "Der &6Riesen-Dieselmotor&r mit 224 RPM und bis zu 16 384 SU öffnet in Stufe 3.",
          ],
          tasks=[task_item("createdieselgenerators:large_diesel_engine", 2)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["diesel_engine"], icon="createdieselgenerators:large_diesel_engine", size=2.5, shape="gear"),

    quest("oil_scanner", B + 5, 15, "&6Such nach Öl",
          subtitle="Der Ölscanner zeigt, was unter dem Chunk liegt.",
          description=[
              "&eRezept:&r &6Andesitlegierung&r, &6Uhr&r, &6Andesitlegierung&r oben, zwei &6Eisenbleche&r um einen &6Eisenbarren&r in der Mitte, ein &6Eisenbarren&r unten ergeben den &6Ölscanner&r. Rechtsklick, kurz warten, und er sagt dir, ob unter diesem Chunk &ckein Öl&r, &eein bisschen&r, &aviel&r oder ein &bunerschöpflicher&r Vorrat liegt. Zu hoch oben funktioniert er nicht.",
              "",
              "Manche Biome haben mehr Öl als andere. Wer jetzt die ergiebigen Chunks nahe der Basis findet und markiert, spart sich später die Suche.",
              "",
              "&eStufe 3:&r Dann öffnen &6Pumpjack&r (Lager, Kurbel, Kopf und ein Rohr bis zum Grundgestein), der &6Destillationsturm&r (ein Steuergerät auf einem mindestens drei Blöcke hohen Tank, erhitzt) und der &6Riesen-Dieselmotor&r. 100 mB Rohöl werden zu 50 mB &bDiesel&r und 50 mB &bBenzin&r, überhitzt zu je 75 mB. Rohöl mit Kies und Sand ergibt im erhitzten Mixer außerdem Asphalt.",
          ],
          tasks=[task_item("createdieselgenerators:oil_scanner", 1)],
          rewards=[reward_item("minecraft:clock", 1), reward_xp(5)],
          deps=["diesel_engine"], icon="createdieselgenerators:oil_scanner"),

    # ---- Ausblick (column B) ----------------------------------------------------
    quest("ore_excavation", B + 5, 18, "&7Erzadern anbohren",
          subtitle="Create Ore Excavation kommt in Stufe 3.",
          description=[
              "Mit &6Stufe 3&r öffnet &6Create Ore Excavation&r. Der &6Erzadern-Finder&r (Enderauge, Amethyst, Redstone-Erz, Stöcke) zeigt an, welche Ader unter einem Chunk liegt: Kohle, Kupfer, Eisen, Gold, Zink, Redstone, Lapis, Diamant, Smaragd, dazu Quarz, Glowstone und Netherit im Nether sowie Wasser.",
              "",
              "Die &6Bohrmaschine&r (5 x 5 Rezept aus Messing, Robusten Blechen, Präzisionsgetrieben und einem Mechanischen Bohrer) steht auf festem Boden über der Ader, bekommt einen &6Eisenbohrer&r und Rotation und fördert dann Roherz, zum Beispiel alle 30 Sekunden ein Roheisen bei 256 SU. Die Adern sind auf Kronwerke unerschöpflich. Diamant- und Netheritbohrer kommen in Stufe 4.",
              "",
              "&eKronwerke:&r Das Ziel von Stufe 3 will 4 000 Stahlbarren. Eine Bohrmaschine auf einer Eisenader, die Tag und Nacht fördert, ist der ruhigste Weg dorthin.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["oil_scanner"], icon="create:mechanical_drill", shape="diamond", optional=True),

    quest("jetpack", B + 7.5, 18, "&7Mit Druckluft fliegen",
          subtitle="Create Jetpack braucht eine Elytra, also Stufe 4.",
          description=[
              "Das &6Jetpack&r ist ein Rezept für die Handwerkseinheiten: ein &6Kupfer-Rückentank&r in der Mitte, eine &6Elytra&r darunter, zwei &6Präzisionsgetriebe&r, eine Welle, vier Schächte und sechs &6Messingbleche&r drumherum. Die Elytra gibt es erst im End, und das öffnet mit &6Stufe 4&r.",
              "",
              "Es fliegt mit der Druckluft des Rückentanks, die du wie gewohnt an einer Welle auflädst: &eSprung&r steigt, &eSchleichen&r sinkt, &eG&r schaltet den Motor, &eH&r den Schwebemodus. Eine Füllung reicht für 450 Sekunden Flug oder 900 Sekunden Schweben. Mit Netherit-Rückentank oder am Schmiedetisch mit Netherit wird es zum &6Netherit-Jetpack&r.",
              "",
              "Bis dahin: Rückentank und Tauchausrüstung aus &6Create&r Stufe 1 lohnen sich jetzt schon, und der Rückentank ist später die Hälfte des Rezepts.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["ore_excavation"], icon="create:copper_backtank", shape="diamond", optional=True),
]

images = [
    head("title", "Create: Erweiterungen", 0, -3.6, height=1.6, kind="title"),
    head("stage", "Stufe 2: Messingwerk", 0, -2.2, height=0.55, kind="note", colour="stone"),
    head("rails", "Steam 'n' Rails", A - 0.6, -1.2),
    head("connected", "Create Connected", A - 0.6, 5.5),
    head("dragons", "Dragons Plus", A - 0.6, 12.1, colour="magic"),
    head("enchant", "Enchantment Industry", B - 0.6, -1.2, colour="magic"),
    head("spawner", "Mechanical Spawner", B - 0.6, 4.5, colour="fire"),
    head("diesel", "Diesel", B - 0.6, 10.9, colour="fire"),
    head("outlook", "Ausblick", B + 3.9, 16.4, colour="stone"),
]
images[0]["x"] = 13.5
images[1]["x"] = 13.5

chapter(C, "Create: Erweiterungen", "railways:track_switch_brass", "tech", quests, shape="gear", order=56, stage=2,
        subtitle=["Stufe 2: Steam 'n' Rails, Connected, Dragons Plus, Enchantment Industry, Mechanical Spawner und Dieselmotoren."],
        images=images)
