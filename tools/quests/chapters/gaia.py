"""Botania in stage 4: the Ritual of Gaia (gaia pylons, an active beacon, a terrasteel ingot,
the arena rules from the Lexica), fighting the Gaia Guardian alone or together, Gaia spirits
(6 per fighter, 8 for the killing blow), the things made from them (gaia spreader, Flugel tiara,
dandelifeon, trinkets), the starcaller and the stage 4 magic goal of 128 Gaia spirits.
Continues alfheim.py. The Gaia spirit ingot, Gaia II and the relics are stage 5 and text only."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "gaia"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Vorbereitung ---------------------------------------------------------
    quest("pylon", 0, 0, "&dGaiapylonen",
          subtitle="Vier Pylonen für ein Ritual der Elfen.",
          description=[
              "Mit &6Stufe 4 (Sternwerk)&r öffnet Botania seine letzte Prüfung: das &dRitual von Gaia&r. Am Ende steht ein Kampf gegen den &dWächter von Gaia&r, und seine Beute, die &dGaia-Seelen&r, öffnen die stärksten Dinge der Mod.",
              "",
              "Für den Altar brauchst du &e4 Gaiapylonen&r. &eRezept:&r ein &aManapylon&r in der Mitte, ein &dElementiumbarren&r links und rechts, ein &dFeenstaub&r oben und unten.",
              "",
              pic("botania:gaia_spirit"),
              "",
              "&eWas noch wartet:&r Der &dGaia-Seelenbarren&r, das Ritual von Gaia II und die Relikte der Asen kommen in Stufe 5.",
          ],
          tasks=[task_item("botania:gaia_pylon", 4)],
          rewards=[reward_item("botania:pixie_dust", 4), reward_table("s4_common"), reward_xp(10)],
          icon="botania:gaia_pylon", size=2.0, shape="hexagon"),

    quest("beacon", 2.75, -1.25, "&bEin aktiver Beacon",
          subtitle="Der Beacon wird zum Altar.",
          description=[
              "Die Mitte des Rituals ist ein &bBeacon&r, der aktiv ist, also auf einer fertigen Pyramide steht und leuchtet. Eine Pyramide der ersten Stufe (3x3 Blöcke aus Eisen, Gold, Smaragd, Diamant oder Netherit) reicht.",
              "",
              "Den Netherstern für den Beacon bekommst du vom &5Wither&r. Den Effekt des Beacons kannst du vergessen, während des Kampfes schaltet der Wächter ihn ab.",
          ],
          tasks=[task_item("minecraft:beacon", 1)],
          rewards=[reward_item("minecraft:iron_block", 9)],
          deps=["pylon"], icon="minecraft:beacon"),

    quest("terrasteel", 2.75, 1.25, "&aDas Opfer",
          subtitle="Ein Terrastahlbarren pro Kampf.",
          description=[
              "Jedes Ritual kostet einen &aTerrastahlbarren&r. Den gibst du dem Beacon, und er wird dabei verbraucht.",
              "",
              pic("botania:terrasteel_ingot"),
              "",
              "Die Terra-Platte aus Stufe 2 läuft also am besten weiter. Für sechzehn Kämpfe brauchst du sechzehn Barren, und für die Gaia-Seelenbarren in Stufe 5 noch viel mehr.",
          ],
          tasks=[task_item("botania:terrasteel_ingot", 4)],
          rewards=[reward_item("botania:mana_pearl", 4)],
          deps=["pylon"], icon="botania:terrasteel_ingot"),

    quest("arena", 5.25, 0, "&dDie Arena",
          subtitle="Ein freier Platz, sonst nimmt der Beacon nichts an.",
          description=[
              "So muss der Ritualplatz aussehen, nach der &aLexica Botania&r (Ritual von Gaia) und dem Spiel selbst:",
              "",
              "&eDie Pylonen:&r Je ein Gaiapylon steht &e4 Blöcke diagonal&r vom Beacon entfernt und &e1 Block höher&r, also auf den Positionen 4 vor, 4 zur Seite, 1 nach oben, in alle vier Richtungen. Stimmt das nicht, meldet der Beacon, dass die Pylonen falsch stehen.",
              "",
              "&eDer Platz:&r Um den Beacon braucht es eine freie, ebene Fläche mit etwa &e12 Blöcken Radius&r. Keine Blöcke im Weg und keine großen Löcher im Boden, sonst nimmt der Beacon das Opfer nicht an. Bau also nicht in einer Höhle oder auf einer schmalen Insel.",
              "",
              "&eDas Starten:&r Schleichend mit dem Terrastahlbarren auf den Beacon rechtsklicken, einen Schritt zurück, und der Wächter erscheint. Das muss ein echter Spieler tun, kein Einsatzgerät und kein Fake-Spieler.",
              "",
              "&eTipp:&r Bau die Arena fest an einem Ort und lass sie stehen. Alle Kämpfe auf dem Server können dann dort laufen.",
          ],
          tasks=[task_checkmark("Die Arena steht")],
          rewards=[reward_xp(5)],
          deps=["beacon", "terrasteel"], icon="minecraft:beacon"),

    quest("gear", 5.25, 2.5, "&aAusrüstung",
          subtitle="Er ist schwerer als der Wither.",
          description=[
              "Die Lexica rät zu verzauberter &dElementiumrüstung&r, einer &aTerraklinge&r und dazu Tränken und Schmuck. Das ist ein guter Anfang.",
              "",
              "&eWas sonst hilft:&r",
              "&6Goldene Äpfel&r und Heiltränke, Botania-Tränke aus der Brauerei (Stärke, Regeneration, Widerstand),",
              "Schmuck wie der &6Große Feenring&r oder der &6Ring der Magnetisierung&r, um Beute einzusammeln,",
              "und alles, was ihr aus anderen Mods habt, zum Beispiel Rüstung aus Silent Gear oder Artefakte.",
              "",
              "&eWichtig:&r Der Wächter nimmt pro Treffer höchstens 32 Schaden. Eine Waffe, die einmal riesig zuschlägt, bringt hier also weniger als viele schnelle Treffer.",
          ],
          tasks=[task_item("botania:terra_blade", 1), task_item("botania:elementium_chestplate", 1)],
          rewards=[reward_item("minecraft:golden_apple", 4), reward_xp(5)],
          deps=["arena"], icon="botania:terra_blade"),

    # ---- Der Kampf ------------------------------------------------------------
    quest("behaviour", 7.75, -2.5, "&5Was er tut",
          subtitle="Bleib weg vom Lila.",
          description=[
              "Der Wächter von Gaia hat &e320 Lebenspunkte&r, wenn du allein kämpfst. Kämpfen mehrere, kommt für jeden Spieler ein Viertel dazu: zu zweit sind es 480, zu viert 640.",
              "",
              "&eWas dich erwartet:&r",
              "Er &eteleportiert&r sich ständig durch die Arena und schießt &dlila Geschosse&r auf dich.",
              "Er legt &dlila Fallen&r auf den Boden. Wo es lila wird, gehst du weg. Die Lexica sagt es selbst: Halte dich vom Lila fern.",
              "Zwischendurch ruft er &eWellen von Monstern&r herbei. Räum sie schnell weg, sonst wirst du eingekreist.",
              "Wer die Arena verlassen will, wird zurückgeholt. Weglaufen geht nicht.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["arena"], icon="botania:gaia_head"),

    quest("fight", 7.75, 0, "&d&lDer Wächter von Gaia",
          subtitle="Der erste Kampf.",
          description=[
              "Besiege den &dWächter von Gaia&r. Am Ende lässt er &dGaia-Seelen&r fallen:",
              "",
              pic("botania:gaia_spirit"),
              "",
              "&eJeder, der mitgekämpft hat, bekommt 6&r Gaia-Seelen. &eWer den letzten Treffer setzt, bekommt 8&r. Ab und zu fällt dazu eine Schallplatte.",
              "",
              "Wer ohne jede Rüstung gewinnt, bekommt den Fortschritt &eMythologia's End&r. Das ist nur für Leute, die es wissen wollen.",
          ],
          tasks=[task_item("botania:gaia_spirit", 6)],
          rewards=[reward_item("botania:terrasteel_ingot", 2), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["gear", "behaviour"], icon="botania:gaia_spirit", size=2.0, shape="gear"),

    quest("together", 10.25, -2.5, "&dGemeinsam kämpfen",
          subtitle="Mehr Leute, mehr Seelen.",
          description=[
              "Das Ritual zählt, wie viele Spieler in der Nähe sind, wenn es beginnt. Jeder weitere Spieler macht den Wächter stärker, gibt aber auch jedem Kämpfer seine eigene Beute.",
              "",
              "&eSo lohnt es sich:&r Zu viert hat der Wächter doppelt so viele Lebenspunkte wie allein, aber es fallen &e6 Seelen für jeden&r und &e8 für den letzten Treffer&r. Zusammen sind das 26 statt 8.",
              "",
              "Mehr als fünf Spieler sind keine gute Idee, sagt die Lexica. Dann wird es zu unübersichtlich.",
              "",
              "&eKronwerke:&r Die Kämpfe für den Obelisken laufen &elive auf Stream&r. Verabredet euch, baut die Arena vorher fertig und bringt genug Terrastahl mit.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["fight"], icon="botania:gaia_spirit"),

    quest("head", 10.25, 2.5, "&5Der Kopf des Wächters",
          subtitle="Eine Trophäe, nur mit Elementium.",
          description=[
              "Triffst du den Wächter mit einer &dElementiumaxt&r zum letzten Mal, lässt er manchmal seinen &5Kopf&r fallen. Die Chance ist klein, Plünderung erhöht sie.",
              "",
              "Der Kopf hat keinen Nutzen, außer an der Wand zu hängen und allen zu zeigen, dass du dabei warst.",
          ],
          tasks=[task_item("botania:gaia_head", 1)],
          rewards=[reward_xp(10)],
          deps=["fight"], icon="botania:gaia_head", optional=True),

    quest("spirits", 10.25, 0, "&dGaia-Seelen sammeln",
          subtitle="Die Währung dieser Stufe.",
          description=[
              "Fast alles in diesem Kapitel kostet eine oder mehrere &dGaia-Seelen&r. Dazu kommen die Techniker: &eRezept auf Kronwerke:&r Jeder &cStabilisator&r für den Energiekern von Draconic Evolution braucht eine Gaia-Seele, und ein Kern braucht vier davon.",
              "",
              "Leg also nach jedem Kampf ein paar Seelen zur Seite, bevor alles im Obelisken landet.",
          ],
          tasks=[task_item("botania:gaia_spirit", 24)],
          rewards=[reward_item("botania:terrasteel_ingot", 4), reward_table("s4_common")],
          deps=["fight"], icon="botania:gaia_spirit"),

    # ---- Aus Gaia-Seelen -------------------------------------------------------
    quest("spreader", 12.75, -2.5, "&dGaia-Manaverbreiter",
          subtitle="Der beste Verbreiter der Mod.",
          description=[
              "Ein &6Elfen-Manaverbreiter&r, ein &dDrachenstein&r und eine &dGaia-Seele&r, formlos an der Werkbank, ergeben den &dGaia-Manaverbreiter&r.",
              "",
              "Er schießt größere Manastöße, weiter und mit weniger Verlust als alle anderen. Weil jeder Stoß größer ist, schießt er dafür seltener.",
              "",
              "&eTipp:&r An einer starken Blume wie dem Lebenzahn oder an der Strecke zu einem weit entfernten Becken lohnt er sich am meisten.",
          ],
          tasks=[task_item("botania:gaia_mana_spreader", 1)],
          rewards=[reward_item("botania:dragonstone", 2)],
          deps=["spirits"], icon="botania:gaia_mana_spreader"),

    quest("tiara", 12.75, 0, "&b&lFlügel-Tiara",
          subtitle="Fliegen mit Mana.",
          description=[
              "Die &bFlügel-Tiara&r: oben drei &dGaia-Seelen&r, in der Mitte Elementium, eine Gaia-Seele und Elementium, unten Feder, &5Reine Ender-Essenz&r und Feder.",
              "",
              pic("botania:flugel_tiara"),
              "",
              "Im Schmuckslot getragen lässt sie dich mit Mana fliegen, aber nicht endlos: Nach etwa dreißig Sekunden am Stück ist die Flugleiste leer. Dazu kannst du einen &eSprint-Stoß&r nach vorn machen (Sprinttaste, wenn du nicht schon sprintest) und &egleiten&r, indem du im Fallen schleichst. Gleiten schützt vor Fallschaden.",
              "",
              "Mit verschiedenen Quarzsorten an der Werkbank bekommt die Tiara andere Flügel.",
          ],
          tasks=[task_item("botania:flugel_tiara", 1)],
          rewards=[reward_item("botania:mana_pearl", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["spirits"], icon="botania:flugel_tiara", size=1.5, shape="diamond"),

    quest("dandelifeon", 12.75, 2.5, "&aLebenzahn",
          subtitle="Conways Spiel des Lebens, in Mana.",
          description=[
              "Der &aLebenzahn&r (Dandelifeon) ist die stärkste Manablume von Botania, und die schwierigste. &eRezept in der Apotheke:&r 2 lila, 1 hellgrünes und 1 grünes Blütenblatt, die &5Runen von Wasser, Feuer, Erde und Luft&r, eine &6Redstone-Wurzel&r und eine &dGaia-Seele&r.",
              "",
              "&eSo funktioniert er:&r Um die Blume liegt ein Feld aus 25 mal 25 Blöcken. &eZellblöcke&r (aus Kaktus, Karotte, Kartoffel und Roter Bete) sind lebende Zellen. Mit einem Redstone-Signal rechnet die Blume zweimal pro Sekunde einen Schritt nach den Regeln von Conways Spiel des Lebens. Zellen, die in das 3x3-Feld um die Blume wachsen, werden zu Mana, und je älter sie sind, desto mehr.",
              "",
              "Die Lexica erklärt alle Regeln. Ein gutes Startmuster findet ihr, wenn ihr ein wenig probiert.",
          ],
          tasks=[task_item("botania:dandelifeon", 1)],
          rewards=[reward_item("botania:redstone_root", 4), reward_xp(5)],
          deps=["spirits"], icon="botania:dandelifeon", optional=True),

    quest("trinkets", 15.25, -1.25, "&6Schmuck und Umhänge",
          subtitle="Kleine Dinge mit großer Wirkung.",
          description=[
              "Mit Gaia-Seelen werden aus vielen alten Schmuckstücken bessere:",
              "",
              "&6Umhang der Tugend&r blockt einen Treffer ganz, &6Umhang der Sünde&r gibt den Schaden an Monster in der Nähe zurück, &6Umhang der Balance&r teilt ihn zwischen dir und dem Angreifer. Danach brauchen sie zehn Sekunden Pause.",
              "&6Karmesin-Anhänger&r (aus dem Pyroklastanhänger): Feuer und Lava machen dir nichts mehr.",
              "&6Nimbus-Amulett&r (aus dem Zirrus-Amulett) und &6Schärpe des Weltreisenden&r (aus der Schärpe des Reisenden): höher springen und schneller laufen.",
              "&6Zauber der Diva&r: Monster, die dich treffen, gehen auf andere Monster los.",
              "&6Schwarzloch-Talisman&r: speichert fast unbegrenzt viele Blöcke einer Sorte.",
              "&6Weltgestalter-Astrolab&r: setzt viele Blöcke auf einmal.",
              "",
              "Die Rezepte stehen in JEI und in der Lexica.",
          ],
          tasks=[task_item("botania:cloak_of_virtue", 1)],
          rewards=[reward_item("minecraft:white_wool", 8)],
          deps=["tiara"], icon="botania:cloak_of_virtue", optional=True),

    quest("starcaller", 15.25, 1.25, "&eSternrufer",
          subtitle="Ein Schwert, das Sterne fallen lässt.",
          description=[
              "Der &eSternrufer&r (Starcaller) entsteht aus einer &aTerraklinge&r, zwei &5Reinen Ender-Essenzen&r, einem &dDrachenstein&r und einem &dElementiumbarren&r. Verzauberungen auf der Terraklinge gehen dabei verloren.",
              "",
              "Bei jedem Schwung fällt ein Stern vom Himmel auf die Stelle, die du ansiehst. Sein Bruder, der &eDonnerrufer&r (mit einem Manadiamanten statt des Drachensteins), schlägt Blitze, die von Monster zu Monster springen.",
          ],
          tasks=[task_item("botania:starcaller", 1)],
          rewards=[reward_item("botania:pure_ender_essence", 2)],
          deps=["tiara"], icon="botania:starcaller", optional=True),

    # ---- Fuer den Obelisken ------------------------------------------------------
    quest("goal", 17.75, 0, "&d&lLicht des Drachen",
          subtitle="128 Gaia-Seelen für den Obelisken.",
          description=[
              "&eKronwerke:&r Das Magieziel von Stufe 4 will &e128 Gaia-Seelen&r (eine feste Zahl) und &e30 Mystische Stäbe&r aus Mahou Tsukai.",
              "",
              "Gerechnet ist mit acht Seelen pro Kampf, also &esechzehn Kämpfe&r, alle live auf Stream. Kämpft ihr zu mehreren, bringt jeder Kampf mehr, dafür hält der Wächter auch mehr aus.",
              "",
              "&eSo klappt es:&r",
              "&e1.&r Eine feste Arena, die alle kennen.",
              "&e2.&r Ein Vorrat an Terrastahl, einer pro Kampf.",
              "&e3.&r Seelen, die nicht in Ausrüstung oder Stabilisatoren gehen, direkt in die Truhe am Obelisken.",
              "",
              "Erst wenn auch die Techniker ihr Draconium und ihre Elite-Schaltkreise abgegeben haben, öffnet &6Stufe 5 (Chaoswerk)&r.",
          ],
          tasks=[task_item("botania:gaia_spirit", 64)],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["spreader", "tiara"], icon="botania:gaia_spirit", size=2.0, shape="gear"),

    quest("outlook", 20.25, 0, "&8Gaia II",
          subtitle="Was in Stufe 5 kommt.",
          description=[
              "Vier Gaia-Seelen um einen Terrastahlbarren ergeben einen &dGaia-Seelenbarren&r. Die Lexica nennt ihn nutzlos, weil sich die beiden Kräfte gegenseitig aufheben. Opferst du ihn aber dem Beacon statt Terrastahl, beginnt das &dRitual von Gaia II&r mit einem stärkeren Wächter.",
              "",
              "Der gibt deutlich mehr Seelen (10 für jeden, 16 für den letzten Treffer), dazu Runen, Manastahl, Manaperlen, Manadiamanten, Lotusblüten, ein Vermächtnis der Alten und einen &6Schicksalswürfel&r. Der Würfel gibt eines der &6Relikte der Asen&r.",
              "",
              "&cDas alles kommt in Stufe 5:&r Der Gaia-Seelenbarren ist bis dahin gesperrt. Dann will der Obelisk &e128 Gaia-Seelenbarren&r, und die Techniker brauchen je zwei für ihr Erwachtes Draconium.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["goal"], icon="botania:terrasteel_ingot", optional=True),
]

images = [
    banner("gaia/title", "Botania: Gaia", 9, -5.6, height=1.8, kind="title", colour="nature"),
    banner("gaia/vorbereitung", "Vorbereitung", 2.6, -3.0, height=0.9, colour="nature"),
    banner("gaia/kampf", "Der Kampf", 9.0, 4.0, height=0.9, colour="magic"),
    banner("gaia/seelen", "Aus Gaia-Seelen", 14.0, -3.9, height=0.9, colour="nature"),
    banner("gaia/obelisk", "Für den Obelisken", 19.0, -1.9, height=0.9, colour="magic"),
]

chapter(C, "Botania: Gaia", "botania:gaia_spirit", "magic", quests, shape="circle", order=39, stage=4,
        subtitle=["Stufe 4. Das Ritual von Gaia, der Wächter und was aus seinen Seelen wird."], images=images)
