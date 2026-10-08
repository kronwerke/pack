"""Building in stage 1: FramedBlocks (frames, camo, the framing saw and its tools), Chipped
(the six workbenches and the chisel), Supplementaries (sconces, timber frames, rope, shelves,
sacks, signs, locks), Create's decorative parts (copycats, andesite alloy decor, copper roofing)
and tips for a streamer's base (claims, chunk loading, lighting). Building Gadgets 2, the
schematicannon, the wand of symmetry and the extendo grip are stage 2, the copy paste gadget and
Mining Gadgets stage 3; they are only mentioned. The framing saw takes andesite alloy on Kronwerke (links.js)."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "building"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Rahmenblöcke ------------------------------------------------------------
    quest("cube", 0, 1, "&6&lZimmere Rahmenblöcke",
          subtitle="Ein Block, der aussieht wie jeder andere.",
          description=[
              "&eRezept:&r vier &6Bretter&r in die Ecken, vier &6Stöcke&r an die Seiten, die Mitte bleibt leer. Das ergibt vier &6Rahmenblöcke&r (Framed Cubes).",
              "",
              "&6FramedBlocks&r ist der Baumod für alles, was Vanilla nicht hat: Schrägen, Ecken, Säulen, Türen und über 200 weitere Formen. Jede Form ist zuerst ein nackter Holzrahmen. Ihr Aussehen bekommt sie erst, wenn du einen Block darauf anwendest.",
              "",
              "Rahmenblöcke sind nicht gesperrt. Der ganze Mod steht dir von der ersten Minute an offen, egal welche Stufe der Server gerade hat.",
          ],
          tasks=[task_item("framedblocks:framed_cube", 16)],
          rewards=[reward_item("minecraft:oak_log", 16), reward_table("s1_common")],
          icon="framedblocks:framed_cube", size=2.0, shape="hexagon"),

    quest("camo", 2.5, 0, "&6Tarne einen Rahmen",
          subtitle="Rechtsklick mit einem Block, fertig.",
          description=[
              "Stell einen &6Rahmenblock&r auf und klick ihn mit einem beliebigen &6Vollblock&r an. Der Block wird verbraucht, und der Rahmen sieht ab jetzt aus wie er. Mit dem &6Rahmenhammer&r (zwei Rahmenblöcke, zwei Stöcke) holst du die Tarnung wieder heraus.",
              "",
              pic("framedblocks:framed_hammer"),
              "",
              "&eLicht ab Stufe 2:&r Klick einen getarnten Rahmen mit &6Glowstone-Staub&r an, und er leuchtet mit Lichtstärke 15, ohne dass sich sein Aussehen ändert. Glowstone kommt aus dem Nether, der mit Stufe 2 öffnet. Bis dahin: eine Rahmenlaterne aus der Säge.",
              "",
              "Blöcke mit Inventar (Truhen, Öfen) gehen nicht als Tarnung. Doppelte Formen wie die Doppelstufe nehmen zwei Tarnungen, eine pro Hälfte.",
          ],
          tasks=[task_item("framedblocks:framed_hammer", 1)],
          rewards=[reward_item("minecraft:torch", 16)],
          deps=["cube"], icon="framedblocks:framed_hammer"),

    quest("saw", 2.5, 2, "&6&lBau eine Rahmensäge",
          subtitle="Doppelt so viele Formen aus demselben Holz.",
          description=[
              "&eRezept auf Kronwerke:&r eine &6Andesitlegierung&r über drei &6Rahmenblöcken&r ergibt die &6Rahmensäge&r (Framing Saw). Rechtsklick öffnet sie: links die Rahmenblöcke hinein, rechts die Form aussuchen, das Suchfeld hilft bei über 200 Einträgen.",
              "",
              "Die Säge rechnet in &eMaterialwert&r: Ein Rahmenblock ist 6 144 wert, eine Schräge 3 072, eine Stufe 3 072, eine Ecksäule 1 536. Aus einem Rahmenblock werden also zwei Schrägen oder vier Ecksäulen, ohne Rest.",
              "",
              "An der Werkbank bekommst du aus drei Rahmenblöcken drei Schrägen, in der Säge sechs. Treppen: sechs Blöcke für vier an der Werkbank, drei Blöcke für vier in der Säge. Eine Tür kostet an der Werkbank zwei Blöcke, in der Säge einen halben.",
              "",
              "Manche Formen brauchen eine Zutat dazu, die Säge zeigt sie an: Fackeln Kohle, Druckplatten Eisen oder Gold, die Laterne eine Fackel, der Rahmen-Trichter eine Truhe.",
              "",
              "&eAusblick:&r Die &6Angetriebene Rahmensäge&r (dazu zwei Redstone) arbeitet von selbst, braucht aber 50 FE/t. Strom gibt es ab &6Stufe 2&r.",
          ],
          tasks=[task_item("framedblocks:framing_saw", 1)],
          rewards=[reward_item("framedblocks:framed_cube", 32), reward_table("s1_common"), reward_xp(5)],
          deps=["cube"], icon="framedblocks:framing_saw", size=1.75, shape="gear"),

    quest("shapes", 5, 2, "&6Bau mit Schrägen",
          subtitle="Dächer, die wie Dächer aussehen.",
          description=[
              "Säge 16 &6Rahmenschrägen&r (Framed Slopes) und tarne sie mit dem Block deines Dachs. Eine Schräge sitzt wie eine Treppe, nur ohne Absatz, und schließt mit den &6Eckschrägen&r (innen und außen) zu einem glatten Dach.",
              "",
              "&eSetzen:&r Die Richtung hängt davon ab, wo du auf den Block klickst, ob oben oder unten und von welcher Seite. Mit dem &6Schraubenschlüssel&r aus Rahmenblöcken (nächste Quest) drehst du eine falsch gesetzte Schräge, statt sie abzubauen.",
              "",
              "Lohnende Formen für den Anfang: &6Schrägplatte&r für flache Dächer, &6Säule&r und &6Ecksäule&r für Fachwerk, &6Halbtreppe&r für Fensterbänke, &6Rahmenzaun&r und &6Rahmenwand&r, die sich wie Vanilla verbinden.",
          ],
          tasks=[task_item("framedblocks:framed_slope", 16)],
          rewards=[reward_item("framedblocks:framed_cube", 16), reward_xp(3)],
          deps=["saw"], icon="framedblocks:framed_slope"),

    quest("tools", 5, 0, "&6Nimm das Rahmenwerkzeug",
          subtitle="Drehen, sperren, kopieren.",
          description=[
              "Vier kleine Werkzeuge, jedes aus Stöcken und einem oder zwei &6Rahmenblöcken&r: der &6Schraubenschlüssel&r dreht einen gesetzten Rahmen, der &6Schraubendreher&r dreht die Tarnung darauf (Stämme längs oder quer), der &6Rahmenschlüssel&r (dazu zwei Eisenklumpen) sperrt den Zustand eines Blocks, damit sich Zäune und Wände nicht mehr neu verbinden.",
              "",
              pic("framedblocks:framed_wrench"), pic("framedblocks:framed_blueprint"),
              "",
              "Der &6Bauplan&r (vier Rahmenblöcke um ein Papier) kopiert mit Schleichen und Rechtsklick einen fertigen Rahmen samt Tarnung. Danach setzt du mit Rechtsklick Kopien, solange du Rahmen und Tarnblöcke im Inventar hast. Der Tooltip zeigt, was fehlt.",
              "",
              "&eTipp:&r Die &6Rahmenaxt&r (zwei Eisenbarren, zwei Rahmenblöcke) baut Rahmen ab, ohne die Tarnung einzeln fallen zu lassen. Umbauen geht damit ohne Sortierarbeit.",
          ],
          tasks=[task_item("framedblocks:framed_wrench", 1), task_item("framedblocks:framed_blueprint", 1)],
          rewards=[reward_item("minecraft:paper", 8), reward_xp(3)],
          deps=["camo"], icon="framedblocks:framed_blueprint"),

    quest("specials", 7.5, 1, "&6Verstärke und verstecke",
          subtitle="Rahmen, die mehr können als aussehen.",
          description=[
              "&6Rahmenverstärkung&r: vier &6Obsidian&r in die Ecken, vier Stöcke an die Seiten, ein Rahmenblock in die Mitte ergibt 16 Stück. Klick damit einen Rahmen an, und er hält Explosionen aus wie Obsidian, sieht aber weiter aus wie Holz oder Stein.",
              "",
              pic("framedblocks:framed_reinforcement"),
              "",
              "Weitere Formen mit Zutat in der Säge: das &6Einwegfenster&r (dazu getöntes Glas) ist von einer Seite durchsichtig, nur du als Setzer stellst die Seite ein. Die &6Rahmentruhe&r ist eine getarnte Truhe, der &6Rahmen-Trichter&r ein getarnter Trichter, die &6Rahmenlaterne&r eine getarnte Lichtquelle.",
          ],
          tasks=[task_item("framedblocks:framed_reinforcement", 16)],
          rewards=[reward_item("minecraft:obsidian", 4)],
          deps=["tools", "shapes"], icon="framedblocks:framed_reinforcement", optional=True),

    # ---- Chipped -----------------------------------------------------------------
    quest("doors", 7.5, -0.5, "&6Bau Türen, die nicht auffallen",
          subtitle="Rahmentür und Rahmenfalltür, getarnt wie die Wand.",
          description=[
              "Die &6Rahmentür&r kommt aus der Rahmensäge, die &6Rahmenfalltür&r aus sechs &6Rahmenstufen&r in zwei Reihen an der Werkbank. Tarn sie mit demselben Block wie die Wand daneben, und der Eingang verschwindet fast.",
              "",
              "Es gibt beides auch in Eisen, das sich nur mit Redstone öffnet. Für einen versteckten Lagerraum hinter der Bücherwand genau das Richtige.",
          ],
          tasks=[task_item("framedblocks:framed_door", 1), task_item("framedblocks:framed_trapdoor", 1)],
          rewards=[reward_item("framedblocks:framed_cube", 8), reward_xp(3)],
          deps=["shapes"], icon="framedblocks:framed_door"),

    quest("pillars", 7.5, 2.5, "&6Stell Säulen auf",
          subtitle="Eckpfeiler, Säulen und Sockel.",
          description=[
              "Zwei &6Rahmenblöcke&r übereinander ergeben vier &6Ecksäulen&r. Eine Ecksäule allein in die Werkbank wird zur &6Rahmensäule&r, die in der Mitte des Blocks steht. Sockel und halbe Säulen kommen aus der Säge.",
              "",
              "Getarnt mit Quarz, Steinziegeln oder poliertem Andesit werden daraus Säulengänge, Zaunpfosten oder schlanke Stützen unter einem Vordach.",
          ],
          tasks=[task_item("framedblocks:framed_pillar", 4)],
          rewards=[reward_item("minecraft:stone_bricks", 16), reward_xp(3)],
          deps=["shapes"], icon="framedblocks:framed_pillar", optional=True),

    quest("mason", 0, 6, "&7&lBau einen Steinmetztisch",
          subtitle="Über 60 Varianten aus jedem Stein.",
          description=[
              "&eRezept:&r oben drei &6Ziegel&r, in der Mitte Eisenbarren, &6Werkbank&r, Eisenbarren, unten drei &6Holzstämme&r. Das ist der &6Steinmetztisch&r (Mason Table) von &6Chipped&r.",
              "",
              "&eSo geht es:&r Leg einen Stein hinein, zum Beispiel Stein, Bruchstein, Tiefenschiefer oder Ziegelsteine. Rechts erscheinen alle Varianten, 62 bei Stein, 66 bei Bruchstein, 65 bei Ziegeln. Klick eine an, dann &eCraft&r für einen oder &eCraft All&r für den ganzen Stapel. Jede Variante tauscht eins zu eins und lässt sich wieder zurückwandeln.",
              "",
              "Die Vorschau zeigt den Block einzeln, als 2x2 oder als waagerechte oder senkrechte Reihe, damit du siehst, wie Muster zusammenlaufen.",
              "",
              "&eKronwerke:&r Chipped ändert nur das Aussehen. Für den Obelisken zählt &6Bruchstein&r in jeder Variante gleich, das Ziel von Stufe 1 will 20 000 davon.",
          ],
          tasks=[task_item("chipped:mason_table", 1)],
          rewards=[reward_item("minecraft:stone_bricks", 32), reward_table("s1_common")],
          icon="chipped:mason_table", size=1.5, shape="hexagon"),

    quest("carpenter", 2.5, 5, "&6Bau einen Zimmermannstisch",
          subtitle="Holz in 38 Mustern.",
          description=[
              "&eRezept:&r oben links eine &6Eisenaxt&r, oben rechts ein Eisenbarren, in der Mitte Bretter, &6Werkbank&r, Bretter, unten drei Bretter. Der &6Zimmermannstisch&r (Carpenters Table) macht aus Brettern, Stämmen, Türen, Falltüren, Leitern, Fässern und Bücherregalen neue Varianten.",
              "",
              "Eichenbretter allein haben 38 Muster, jeder Stamm elf. Besonders praktisch: Türen und Falltüren mit Fenstern, die zu deinem Holz passen.",
          ],
          tasks=[task_item("chipped:carpenters_table", 1)],
          rewards=[reward_item("minecraft:oak_planks", 32)],
          deps=["mason"], icon="chipped:carpenters_table"),

    quest("benches", 2.5, 7, "&6Stell die anderen Werkbänke auf",
          subtitle="Glas, Wolle, Lampen, Pflanzen.",
          description=[
              "Chipped hat sechs Werkbänke, jede für eine Blockfamilie. Alle brauchen eine &6Werkbank&r in der Mitte:",
              "",
              "&6Glasbläser&r (Eisen, Glas, Ziegelsteine, ein &6Schmelzofen&r unten): 21 Glasvarianten und ihre Scheiben, auch gefärbt.",
              "&6Webstuhltisch&r (drei Wolle, zwei Stöcke, drei Stämme): Wolle und Teppiche, 20 Muster pro Farbe.",
              "&6Bastlertisch&r (zwei Redstone-Fackeln, Redstone, Eisen, zwei Stämme): Laternen, Seelenlaternen, Redstone-Lampen, Eisengitter.",
              "&6Botanikertisch&r (drei Blumentöpfe, zwei Holzstufen, zwei Stöcke): Laub, Erde, Lehm, Pilze, Eis.",
              "&6Alchemietisch&r (Braustand oben, Zaubertisch unten, Holzstufen): Erz- und Edelsteinblöcke, Glowstone, Amethyst.",
          ],
          tasks=[task_item("chipped:glassblower", 1)],
          rewards=[reward_item("minecraft:glass", 32)],
          deps=["mason"], icon="chipped:glassblower"),

    quest("chisel", 5, 6, "&6Schnitz einen Meißel",
          subtitle="Der Steinmetztisch für die Hosentasche.",
          description=[
              "Ein &6Steinmetztisch&r und ein &6Eisenbarren&r formlos ergeben den &6Meißel&r. Rechtsklick in der Hand öffnet dieselbe Oberfläche wie der Tisch, überall, auch auf dem Gerüst in 40 Blöcken Höhe.",
              "",
              pic("chipped:chisel"), pic("chipped:saw"),
              "",
              "Genauso gibt es die &6Säge&r aus dem Zimmermannstisch, die &6Nadeln&r aus dem Webstuhltisch (mit einem Stock), das &6Multimeter&r aus dem Bastlertisch (mit Redstone), die &6Gießkanne&r aus dem Botanikertisch (mit einem Eimer) und das &6Alchemiebuch&r aus dem Alchemietisch (mit einem Buch).",
          ],
          tasks=[task_item("chipped:chisel", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(5)],
          deps=["carpenter", "benches"], icon="chipped:chisel", size=1.5),

    # ---- Supplementaries -------------------------------------------------------------
    quest("sconce", 0, 11, "&e&lHäng Wandfackeln auf",
          subtitle="Licht, das nicht aus dem Boden ragt.",
          description=[
              "&eRezept:&r eine &6Fackel&r zwischen zwei &6Eisenklumpen&r, ein dritter Klumpen darunter ergibt eine &6Wandfackel&r (Sconce). Sie hängt an der Wand oder steht auf dem Boden und leuchtet wie eine Fackel, nur ohne den Stiel im Weg.",
              "",
              pic("supplementaries:sconce"),
              "",
              "&6Supplementaries&r ist der Mod für den Kleinkram, der eine Basis bewohnt aussehen lässt. Für Licht gibt es dazu den &6Kerzenständer&r (Kerze auf Eisenbarren), der sich stapeln lässt, und die &6Seelen-Wandfackel&r mit Seelenfackel.",
          ],
          tasks=[task_item("supplementaries:sconce", 8)],
          rewards=[reward_item("minecraft:torch", 32), reward_table("s1_common")],
          icon="supplementaries:sconce", size=1.5, shape="hexagon"),

    quest("timber", 2.5, 10, "&6Bau Fachwerk",
          subtitle="Balken und Lehm, wie im Dorf.",
          description=[
              "Vier &6Stöcke&r in Rautenform ergeben einen &6Fachwerkrahmen&r (Timber Frame). Stell ihn auf und klick ihn mit einem &6Vollblock&r an, der Block füllt den Rahmen und die Balken bleiben sichtbar. Vier Stöcke diagonal ergeben die &6Strebe&r, vier Stöcke in den Ecken das &6Kreuz&r.",
              "",
              "Die passende Füllung ist &6Lehmputz&r (Daub): ein &6Lehmklumpen&r und ein &6Stroh&r im 2x2-Schachbrett ergeben zwei Stück. Stroh kommt von Farmer's Delight, Weizen oder Flachs gehen auch. Lehmputz mit vier Stöcken drumherum ist gleich der fertige Fachwerkblock.",
              "",
              "&eTipp:&r Rahmen aus FramedBlocks und Fachwerk aus Supplementaries vertragen sich. Ein Fachwerkhaus mit Rahmenschrägen als Dach ist in einer Stunde gebaut.",
          ],
          tasks=[task_item("supplementaries:timber_frame", 8), task_item("supplementaries:daub", 8)],
          rewards=[reward_item("minecraft:clay_ball", 16), reward_xp(3)],
          deps=["sconce"], icon="supplementaries:timber_frame"),

    quest("rope", 2.5, 12, "&6Knüpf Seile",
          subtitle="Rauf, runter und über den Abgrund.",
          description=[
              "Drei &6Flachs&r übereinander oder drei &6Fäden&r diagonal ergeben drei &6Seile&r. Häng sie an einen Block, und sie fallen nach unten, so weit du Seile hast. Du kletterst daran wie an einer Leiter, und sie lassen sich auch waagerecht von Pfosten zu Pfosten spannen.",
              "",
              pic("supplementaries:flax"),
              "",
              "&6Flachs&r wächst wild in der Welt, und seine Samen liegen in Truhen von Minen, Verliesen und Schiffswracks. Angebaut wächst er zwei Blöcke hoch und gibt Flachs und neue Samen.",
          ],
          tasks=[task_item("supplementaries:rope", 16)],
          rewards=[reward_item("supplementaries:flax_seeds", 4), reward_item("minecraft:string", 8)],
          deps=["sconce"], icon="supplementaries:rope"),

    quest("shelves", 5, 10, "&6Stell Regale und Tafeln auf",
          subtitle="Zeig, was du hast.",
          description=[
              "Drei &6Holzstufen&r in einer Reihe ergeben zwei &6Regale&r (Item Shelf). Sie hängen an der Wand, und jedes zeigt einen Gegenstand, den du darauf legst. Das &6Schwarze Brett&r (acht Bretter um ein Papier) zeigt den Text eines Buches oder eine Karte.",
              "",
              "Auf der &6Tafel&r (zwei Holzstufen, zwei Schwarzstein, ein weißer Farbstoff oder Quarz, ergibt zwei) zeichnest du Pixel für Pixel. Mit einer Honigwabe wird die Zeichnung fest, dann kann niemand mehr darüber malen.",
              "",
              "&eFür den Stream:&r Ein Schwarzes Brett mit den Koordinaten der Basis, der Wegsteine und der Farmen spart dir die Frage im Chat.",
          ],
          tasks=[task_item("supplementaries:item_shelf", 4), task_item("supplementaries:notice_board", 1)],
          rewards=[reward_item("minecraft:paper", 8), reward_item("minecraft:book", 2)],
          deps=["timber"], icon="supplementaries:notice_board"),

    quest("sack", 5, 12, "&6Näh einen Sack",
          subtitle="Neun Plätze, die du mitnehmen kannst.",
          description=[
              "Sieben &6Flachs&r (oder Weizen, oder Leinwand aus Farmer's Delight) um einen &6Faden&r oben in der Mitte ergeben einen &6Sack&r. Er hat neun Plätze, lässt sich als Block aufstellen und behält seinen Inhalt, wenn du ihn abbaust.",
              "",
              "&cAchtung:&r Säcke sind schwer. Mit mehr als zwei Säcken im Inventar wirst du langsamer, mit mehr als vier noch langsamer. Ein Sack für die Ernte, einer für Baumaterial, mehr nicht.",
          ],
          tasks=[task_item("supplementaries:sack", 1)],
          rewards=[reward_item("minecraft:wheat", 16)],
          deps=["rope"], icon="supplementaries:sack"),

    quest("signs", 7.5, 10, "&6Weise den Weg",
          subtitle="Wegweiser und Fahnen für den Server.",
          description=[
              "Ein &6Schild&r formlos ergibt zwei &6Wegweiser&r (Way Signs). Häng sie an einen Zaunpfosten, beschrifte sie und dreh den Pfeil mit Rechtsklick in die Richtung, in die er zeigen soll. Zwei Wegweiser passen an denselben Pfosten, einer oben, einer unten.",
              "",
              "Sechs &6Wolle&r über einem Stock ergeben eine &6Fahne&r. Sie hängt an der Wand, nimmt Bannermuster an und weht im Wind. Auf einem Fahnenmast über der Basis sieht jeder Besucher, wessen Claim er betritt.",
          ],
          tasks=[task_item("supplementaries:way_sign_oak", 2)],
          rewards=[reward_item("minecraft:oak_sign", 4)],
          deps=["shelves"], icon="supplementaries:way_sign_oak", optional=True),

    quest("lock", 7.5, 12, "&6Schließ ab",
          subtitle="Ein Schloss, zu dem nur dein Schlüssel passt.",
          description=[
              "Der &6Schlossblock&r besteht aus vier &6Eisenbarren&r in den Ecken, vier Brettern und einem Redstone in der Mitte. Der &6Schlüssel&r aus einem &6Goldbarren&r über zwei Goldklumpen wird mit einem Namen am Amboss zum passenden Schlüssel: Schlossblock und Schlüssel müssen gleich heißen.",
              "",
              pic("supplementaries:key"),
              "",
              "Rechtsklick mit dem richtigen Schlüssel gibt ein Redstone-Signal, zum Beispiel an eine Eisentür. Türen, Falltüren und Zauntore lassen sich mit einem benannten Schlüssel ebenfalls sperren. Innerhalb deines Claims ist das Deko, am Serverrand ist es nützlich.",
          ],
          tasks=[task_item("supplementaries:lock_block", 1), task_item("supplementaries:key", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 4)],
          deps=["sack"], icon="supplementaries:lock_block", optional=True),

    quest("flower_box", 7.5, 14, "&aPflanz einen Blumenkasten",
          subtitle="Blumen am Fenster, nicht nur auf der Wiese.",
          description=[
              "&eRezept:&r in der mittleren Reihe &6Holzstufe&r, &6Erde&r, &6Holzstufe&r, darunter drei Holzstufen. Das ergibt zwei &6Blumenkästen&r.",
              "",
              "Stell sie unter ein Fenster oder auf eine Mauer und setz kleine Blumen hinein. Ein paar Kästen bringen mehr Farbe an ein Haus als jede Fassade.",
          ],
          tasks=[task_item("supplementaries:flower_box", 2)],
          rewards=[reward_item("minecraft:poppy", 4), reward_item("minecraft:dandelion", 4)],
          deps=["timber"], icon="supplementaries:flower_box"),

    quest("candles", 10, 10, "&eStell Kerzenständer auf",
          subtitle="Warmes Licht für Tisch und Wand.",
          description=[
              "&eRezept:&r eine &6Kerze&r über einem &6Eisenbarren&r. Mit einer gefärbten Kerze bekommst du einen Kerzenständer in deren Farbe.",
              "",
              "Stell ihn auf den Tisch oder häng ihn an die Wand und zünde ihn mit Feuerstein und Stahl an. Weniger hell als eine Fackel, dafür sieht ein Speisesaal damit nach Burg aus und nicht nach Mine.",
          ],
          tasks=[task_item("supplementaries:candle_holder", 2)],
          rewards=[reward_item("minecraft:candle", 4), reward_xp(2)],
          deps=["sconce"], icon="supplementaries:candle_holder", optional=True),

    quest("awning", 10, 14, "&aSpann eine Markise",
          subtitle="Ein Stoffdach über Marktstand und Tür.",
          description=[
              "&eRezept:&r drei &6Flachs&r oben, darunter links und rechts ein &6Stock&r. Das ergibt zwei &6Markisen&r, mit Farbstoff färbst du sie ein.",
              "",
              "Über Tür und Fenster, als Dach über einem Marktstand oder als Sonnensegel auf der Terrasse. Den Flachs kennst du schon von den Seilen.",
          ],
          tasks=[task_item("supplementaries:awning", 2)],
          rewards=[reward_item("supplementaries:flax_seeds", 4), reward_xp(2)],
          deps=["rope"], icon="supplementaries:awning", optional=True),

    quest("iron_gate", 10, 12, "&7Setz ein Eisentor",
          subtitle="Ein Tor, das zu Eisengittern passt.",
          description=[
              "&eRezept:&r in zwei Reihen übereinander je &6Eisenklumpen&r, &6Eisenbarren&r, &6Eisenklumpen&r. Das ergibt zwei &6Eisentore&r.",
              "",
              "Ein Tor aus Eisen statt Holz, passend zu Eisengittern und Andesitgittern. Gut für Ställe, Kerker und die Einfahrt zur Fabrik.",
          ],
          tasks=[task_item("supplementaries:iron_gate", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 4)],
          deps=["lock"], icon="supplementaries:iron_gate", optional=True),

    # ---- Create-Bauteile ---------------------------------------------------------
    quest("copycats", 11, 1, "&6&lSchneide Copycats aus Zink",
          subtitle="Platten und Stufen, die jeden Block nachmachen.",
          description=[
              "Leg einen &6Zinkbarren&r in den &6Steinschneider&r: vier &6Copycat-Platten&r oder vier &6Copycat-Stufen&r. Klick sie mit einem Block an, und sie nehmen sein Aussehen an, genau wie Rahmenblöcke, nur in Create-Form.",
              "",
              pic("create:zinc_ingot"),
              "",
              "&6Copycats+&r erweitert das: ein Zinkbarren wird im Steinschneider zu einem &6Copycat-Block&r, zwei Stufen, vier Balken oder vier Wellen, dazu Treppen, Zäune, Mauern, Laufstege und Türen. Vier Zahnräder mit einem Zinkbarren ergeben vier Copycat-Zahnräder, die sich tarnen und trotzdem drehen.",
              "",
              "&eWann Rahmen, wann Copycat:&r FramedBlocks hat mehr Formen. Copycats sind dünn, brauchen kein Holz und bewegen sich auf Create-Kontraptionen mit.",
          ],
          tasks=[task_item("create:copycat_panel", 8)],
          rewards=[reward_item("create:zinc_ingot", 8), reward_table("s1_common")],
          icon="create:copycat_panel", size=1.5, shape="gear"),

    quest("alloy_decor", 13.5, 0, "&6Schneide Gerüst und Träger",
          subtitle="Industrie-Look aus Andesitlegierung.",
          description=[
              "Eine &6Andesitlegierung&r wird im &6Steinschneider&r zu zwei &6Andesitgerüsten&r, zwei &6Andesitleitern&r oder vier &6Andesitgittern&r. Drei &6Eisenbleche&r über drei Legierungen ergeben acht &6Metallträger&r, die sich zu Fachwerk aus Stahl verbinden.",
              "",
              "Fenster gibt es für jedes Holz: ein Glas zwischen drei Brettern ergibt zwei &6Holzfenster&r. &6Gerahmtes Glas&r kommt aus dem Steinschneider aus Glas, als Block oder Scheibe, dazu Glasfliesen und die senkrechte Variante.",
              "",
              "&eKronwerke:&r Jede Legierung im Steinschneider ist eine weniger für den Obelisken. Das Ziel von Stufe 1 will 1 500 davon. Der Mixer macht aus einem Andesit und einem Eisenklumpen zwei Legierungen, die Werkbank nur eine. Wer dekorieren will, baut vorher die Mixer-Linie aus dem Create-Kapitel.",
          ],
          tasks=[task_item("create:metal_girder", 8), task_item("create:oak_window", 4)],
          rewards=[reward_item("create:andesite_alloy", 8), reward_xp(3)],
          deps=["copycats"], icon="create:metal_girder"),

    quest("copycat_plus", 16, 1, "&6Bau mit Copycat-Blöcken",
          subtitle="Copycats+: ganze Blöcke, Treppen und Balken.",
          description=[
              "Aus dem &6Steinschneider&r kommen mit einem Zinkbarren auch die Formen von &6Copycats+&r. Zwei &6Copycat-Stufen&r übereinander ergeben einen &6Copycat-Block&r.",
              "",
              "Tarn ihn wie jede Copycat mit einem Rechtsklick. Copycat-Blöcke auf einer Kontraption bewegen sich mit und behalten ihr Aussehen, ideal für Tore und Zugbrücken mit Create.",
          ],
          tasks=[task_item("copycats:copycat_block", 4)],
          rewards=[reward_item("create:zinc_ingot", 4), reward_xp(3)],
          deps=["copycats"], icon="copycats:copycat_block"),

    quest("roofing", 13.5, 2, "&6Deck mit Kupfer",
          subtitle="Schindeln, die grün werden.",
          description=[
              "Ein &6Kupferbarren&r im &6Steinschneider&r ergibt zwei &6Kupferschindeln&r oder zwei &6Kupferfliesen&r, jeweils mit Treppen und Stufen. Ein &6Eisenbarren&r wird zu zwei &6Industrieeisen&r, dem dunklen Block für Maschinenhallen.",
              "",
              "Kupferschindeln oxidieren wie Kupferblöcke: erst orange, dann braun, dann grün. Mit einer &6Honigwabe&r wachst du sie in der Farbe, die dir gefällt, mit der Axt kratzt du eine Stufe wieder ab.",
          ],
          tasks=[task_item("create:copper_shingles", 16)],
          rewards=[reward_item("minecraft:copper_ingot", 16), reward_item("minecraft:honeycomb", 4)],
          deps=["copycats"], icon="create:copper_shingles", optional=True),

    # ---- Für die Basis -----------------------------------------------------------
    quest("claims", 11, 5, "&aSichere deine Basis",
          subtitle="Claims, Chunkgrenzen und was geladen bleibt.",
          description=[
              "Öffne mit &eM&r die Karte von &6FTB Chunks&r und zieh mit gedrückter linker Maustaste über die Chunks deiner Basis. Ein Team kann bis zu &e500 Chunks&r beanspruchen, mehr als genug. Wie Teams gehen, steht im Startkapitel unter Claims.",
              "",
              "&eChunkgrenzen:&r &eF3 und G&r blendet sie ein. Bau Maschinenreihen so, dass sie nicht über eine Grenze laufen. Wenn der Nachbarchunk gerade nicht geladen ist, steht die halbe Anlage still, und Förderbänder oder Rohre über der Grenze stauen.",
              "",
              "&eLaden:&r Mit Schleichen und Linksklick auf der Karte lädst du bis zu &e25 Chunks&r dauerhaft. Auf Kronwerke bleiben sie auch geladen, wenn dein ganzes Team offline ist. Farmen laufen also über Nacht weiter.",
          ],
          tasks=[task_checkmark("Basis gesichert")],
          rewards=[reward_item("minecraft:torch", 16), reward_xp(3)],
          icon="minecraft:filled_map"),

    quest("lighting", 11, 7, "&eLeuchte alles aus",
          subtitle="Kein Creeper im Stream-Hintergrund.",
          description=[
              "Feindliche Mobs spawnen seit 1.18 nur noch bei &eLichtstärke 0&r. Eine Fackel leuchtet mit 14 und verliert pro Block eins. Alle &e12 Blöcke&r eine Fackel in jede Richtung, und auf dem Boden dazwischen spawnt nichts mehr.",
              "",
              "Hübscher als Fackeln: &6Wandfackeln&r und &6Kerzenständer&r aus Supplementaries, &6Laternen&r in 32 Chipped-Varianten, die &6Rahmenlaterne&r aus der Säge. Ab Stufe 2 kommt Glowstone dazu: ein getarnter Rahmenblock mit &6Glowstone-Staub&r leuchtet mit Lichtstärke 15 und sieht aus wie vorher.",
              "",
              "&eUnterwegs:&r &6Dynamic Lights&r ist im Pack. Eine Fackel in der Hand oder in der Nebenhand leuchtet beim Laufen, auch in der Mine. Das ist nur Anzeige auf deinem Bildschirm, Mobs hält es nicht ab.",
          ],
          tasks=[task_checkmark("Ausgeleuchtet")],
          rewards=[reward_item("minecraft:lantern", 8), reward_item("minecraft:torch", 16)],
          deps=["claims"], icon="minecraft:lantern"),

    quest("flag", 11, 9, "&aHiss deine Flagge",
          subtitle="Zeig, wem die Basis gehört.",
          description=[
              "&eRezept:&r sechs &6Wolle&r in zwei Reihen, darunter links ein &6Stock&r. Das ergibt eine &6Flagge&r in der Farbe der Wolle, alle 16 Farben gehen.",
              "",
              "Setz sie an eine Wand oder auf einen Pfosten, dort weht sie im Wind. Eine Reihe Flaggen in Teamfarbe macht deine Basis auf jedem Stream sofort erkennbar.",
          ],
          tasks=[task_item("supplementaries:flag_white", 1)],
          rewards=[reward_item("minecraft:white_wool", 12), reward_xp(2)],
          deps=["lighting"], icon="supplementaries:flag_white"),

    quest("gadgets", 13.5, 5, "&dAusblick: Building Gadgets",
          subtitle="Kommt in Stufe 2.",
          description=[
              "&6Building Gadgets 2&r öffnet mit &6Stufe 2&r. Der &6Baugadget&r (Eisen, Redstone, zwei Diamanten, Lapislazuli) setzt ganze Wände, Böden und Säulen aus deinem Inventar mit einem Klick, bis zu 32 Blöcke weit. Der &6Tauschgadget&r ersetzt eine Fläche durch einen anderen Block, der &6Abrissgadget&r (mit Enderperlen) räumt einen Bereich leer.",
              "",
              pic("buildinggadgets2:gadget_building"),
              "",
              "Alle Gadgets laufen mit Strom, den es ebenfalls erst ab Stufe 2 gibt. Der &6Kopiergadget&r (mit Smaragden) und der &6Vorlagenverwalter&r für gespeicherte Bauten kommen in &6Stufe 3&r. Bis dahin: Hand, Rahmensäge und Meißel.",
              "",
              "&6Mining Gadgets&r (Stufe 3) gehören dazu: ein Laser, der Tunnel in jeder Größe gräbt. Mehr dazu im Kapitel &6Logistik&r.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(3)],
          deps=["claims"], icon="minecraft:lapis_lazuli", optional=True),

    quest("schematics", 13.5, 7, "&dAusblick: Baupläne",
          subtitle="Der Bauplantisch jetzt, die Kanone in Stufe 2.",
          description=[
              "Der &6Bauplantisch&r von Create (Holzstufen und glatter Stein) ist schon offen. Mit &6Bauplan und Feder&r markierst du ein Gebäude, speicherst es als Datei und lädst es am Tisch wieder hoch. So sicherst du heute schon, was du gebaut hast.",
              "",
              "Die &6Bauplankanone&r, die den Plan Block für Block aufbaut, öffnet mit &6Stufe 2&r, sie braucht Messing und ein Präzisionsgetriebe. Alles dazu im Kapitel &6Create: Messing&r.",
              "",
              "Ebenfalls Stufe 2: der &6Symmetriestab&r, der jeden gesetzten Block gespiegelt setzt, und der &6Extendo Griff&r für Reichweite beim Bauen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(3)],
          deps=["lighting"], icon="create:schematic_table", optional=True),

    # ---- Abschluss ---------------------------------------------------------------
    quest("showcase", 13.5, 11, "&6&lBau die Stream-Basis",
          subtitle="Rahmen, Copycats und Licht für ein Haus, das man zeigen kann.",
          description=[
              "Zeit für ein richtiges Gebäude. Sammle &664 Rahmenblöcke&r, &616 Copycat-Platten&r und &616 Wandfackeln&r, dann hast du Dach, Fassade und Licht für ein Haus, das im Stream etwas hermacht.",
              "",
              "&eEin Plan, der funktioniert:&r Fachwerk oder Metallträger als Gerüst, Chipped-Varianten für Wände und Boden, Rahmenschrägen als Dach, Copycat-Platten als dünne Verkleidung, Wandfackeln alle zwölf Blöcke. Alles in geclaimten Chunks, alles innerhalb einer Chunkgrenze, wo Maschinen stehen sollen.",
              "",
              "&eKronwerke:&r Was beim Bauen an &6Bruchstein&r anfällt, gehört in die Kiste am Obelisken. 20 000 Stück sind das Ziel von Stufe 1, und ein Bauabend bringt leicht ein paar Tausend.",
          ],
          tasks=[task_item("framedblocks:framed_cube", 64), task_item("create:copycat_panel", 16),
                 task_item("supplementaries:sconce", 16)],
          rewards=[reward_table("s1_rare"), reward_item("framedblocks:framed_cube", 64), reward_xp(15)],
          deps=["saw", "chisel", "sconce", "copycats", "lighting"],
          icon="framedblocks:framed_slope", size=2.5, shape="gear"),
]

images = [
    banner("building/title", "Bauen", 7, -4.6, height=1.8, kind="title", colour="stone"),
    banner("building/frames", "Rahmenblöcke", 3.75, -1.7, height=0.9, colour="brass"),
    banner("building/chipped", "Chipped", 2.5, 3.6, height=0.9, colour="stone"),
    banner("building/supplementaries", "Supplementaries", 3.75, 8.6, height=0.9, colour="nature"),
    banner("building/create", "Create-Bauteile", 12.25, -1.7, height=0.9, colour="brass"),
    banner("building/base", "Für die Basis", 12.25, 3.6, height=0.9, colour="water"),
]

chapter(C, "Bauen", "framedblocks:framing_saw", "storage", quests, shape="circle", order=58,
        subtitle=["Rahmenblöcke, Chipped, Supplementaries, Create-Bauteile und Tipps für die Basis."],
        images=images)
