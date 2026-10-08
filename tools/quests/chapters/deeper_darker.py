"""Deeper and Darker: opened with stage 3. The deep dark and the ancient city as the way in
(sculk, the warden, the Kronwerke reinforced deepslate recipe, the portal lit with a heart of
the deep, reinforced echo shards), the
Otherside with its four biomes, sculk stone, gloomslate and echo wood, the sculk mobs and
their drops, the ancient temple with the sculk transmitter, soul dust and soul crystals,
resonarium gear. Warden gear, soul elytra and the sonorous staff are stage 4 and only named."""
from ftbq import (chapter, quest, task_item, task_dimension, task_kill, task_advancement,
                  task_checkmark, reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "deeper_darker"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Der Weg hinunter ------------------------------------------------------
    quest("deep_dark", 0, 6.5, "&8&lFinde die Tiefe Dunkelheit",
          subtitle="Wo kein Monster spawnt und trotzdem alles still ist.",
          description=[
              "Die &8Tiefe Dunkelheit&r liegt tief unter Bergen, meist unter &eY 0&r. Du erkennst sie am dunkelblauen &6Sculk&r auf dem Boden, an den zuckenden &6Sculk-Sensoren&r und daran, dass hier nichts spawnt.",
              "",
              "&eSo bewegst du dich:&r Sensoren hören jeden Schritt, jeden Block, jede Truhe. Geh &6schleichend&r, lauf auf &6Wolle&r und bau keine Blöcke ab, die du nicht brauchst. Ein Wollblock vor einem Sensor schluckt die Schwingung.",
              "",
              "Das ist der Einstieg in dieses Kapitel: Aus der Tiefen Dunkelheit kommt alles, was du für den Weg in die &5Anderwelt&r brauchst.",
          ],
          tasks=[task_advancement("deeperdarker:main/root", "Die Tiefe Dunkelheit betreten")],
          rewards=[reward_item("minecraft:white_wool", 16), reward_xp(5)],
          icon="minecraft:sculk", size=2.0, shape="hexagon"),

    quest("sculk", 3, 3.5, "&3Ernte Sculk",
          subtitle="Mit der Hacke, nicht mit der Spitzhacke.",
          description=[
              "&6Sculk&r baust du mit einer &6Hacke&r ab, er gibt Erfahrung. &6Sensoren&r, &6Kreischer&r und &6Katalysatoren&r bekommst du nur mit &eBehutsamkeit&r heil heraus.",
              "",
              "&eKatalysatoren&r lassen Sculk wachsen: Stirbt ein Monster in ihrer Nähe, breitet er sich aus und setzt neue Sensoren und Kreischer. Kreischer, die so entstehen, können einen Wärter rufen.",
              "",
              "Sculk brauchst du später, um Schmiedevorlagen aus der Anderwelt zu kopieren.",
          ],
          tasks=[task_item("minecraft:sculk", 16), task_item("minecraft:sculk_sensor", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(5)],
          deps=["deep_dark"], icon="minecraft:sculk_sensor"),

    quest("ancient_city", 3, 6.5, "&8Finde eine Antike Stadt",
          subtitle="Truhen, Scherben, Schmiedevorlagen.",
          description=[
              "In manchen Tiefen Dunkelheiten steht eine &6Antike Stadt&r aus Tiefenschiefer, mit einem großen Rahmen aus &6Verstärktem Tiefenschiefer&r in der Mitte. Folge den Seelenlaternen, die Stadt liegt meist in der Mitte des Bioms.",
              "",
              "&eIn den Truhen:&r &6Echoscherben&r, Plattenbruchstücke, Bücher mit Flinkes Schleichen, und von Deeper and Darker die &6Resonarium-Schmiedevorlage&r (etwa jede zweite Truhe), der &6Wärterpanzer&r (jede fünfte) und die &6Wärter-Schmiedevorlage&r für Stufe 4.",
              "",
              "&eEchoscherben&r brauchst du gleich für den Portalrahmen, nimm alle mit. Occultism kann sie auch herstellen, aus Grauer Paste und Echostaub.",
              "",
              "&eKronwerke:&r Hier liegt auch der &6Echosplitter&r für den Afrit Miner, siehe Kapitel Occultism: Afrit und Marid. Ein Ausflug lohnt sich doppelt.",
          ],
          tasks=[task_advancement("deeperdarker:main/find_ancient_city", "Eine Antike Stadt finden"),
                 task_item("minecraft:echo_shard", 4)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["deep_dark"], icon="minecraft:echo_shard", size=1.5),

    quest("warden", 3, 9.5, "&4&lErlege den Wärter",
          subtitle="Dreimal kreischen, dann kommt er.",
          description=[
              "Ein &6Sculk-Kreischer&r, der dreimal ausgelöst wird, holt den &4Wärter&r aus dem Boden. Er ist blind, hört und riecht dich aber, hat &e500 Lebenspunkte&r und sein &cSchallangriff&r geht durch jede Rüstung.",
              "",
              "&eBeute:&r Ein &6Sculk-Katalysator&r, &e1 bis 3 Wärterpanzer&r und ein &6Herz der Tiefen&r. Das Herz zündet das Portal in die Anderwelt, aus dem Panzer werden Verstärkte Echoscherben und der Antike Kompass.",
              "",
              "&eTipps:&r Kämpf aus der Distanz und mit Höhe, er klettert nicht. Wer ihn nicht bekämpfen will, lockt ihn mit einem geworfenen Schneeball weg. Geht zu zweit oder zu dritt, Zuschauer sind hier gern gesehen.",
          ],
          tasks=[task_kill("minecraft:warden", 1), task_item("deeperdarker:heart_of_the_deep", 1)],
          rewards=[reward_table("s3_uncommon"), reward_item("minecraft:golden_apple", 4), reward_xp(25)],
          deps=["ancient_city"], icon="deeperdarker:heart_of_the_deep", size=1.75, shape="diamond"),

    quest("echo_shard", 6, 9.5, "&bVerstärke eine Echoscherbe",
          subtitle="Panzer und Phantomhaut um eine Scherbe.",
          description=[
              "Eine &6Echoscherbe&r in die Mitte, &e4 Wärterpanzer&r an die Seiten, &e4 Phantomhäute&r in die Ecken: eine &6Verstärkte Echoscherbe&r. Ein Wärter gibt also höchstens für eine Scherbe her.",
              "",
              "&eWofür:&r In Stufe 4 ist sie der Zusatz, der am Schmiedetisch aus Netherit die Wärterrüstung macht. Jetzt schon nützlich: Ein &6Kompass&r mit 4 Wärterpanzern wird zum &6Antiken Kompass&r, der zur nächsten Antiken Stadt zeigt.",
          ],
          tasks=[task_item("deeperdarker:reinforced_echo_shard", 1), task_item("deeperdarker:ancient_compass", 1)],
          rewards=[reward_item("minecraft:phantom_membrane", 4), reward_xp(15)],
          deps=["warden"], icon="deeperdarker:reinforced_echo_shard"),

    quest("portal", 6, 6.5, "&5&lBau das Portal zur Anderwelt",
          subtitle="Verstärkter Tiefenschiefer und ein Herz.",
          description=[
              "&eDer Rahmen:&r Wie ein Netherportal, aber aus &6Verstärktem Tiefenschiefer&r. Innen mindestens &e2 breit und 3 hoch&r, die Ecken bleiben frei, das sind &e10 Blöcke&r.",
              "",
              "&eRezept auf Kronwerke:&r &e4 Tiefenschiefer&r in die Ecken, &e4 Stahlbarren&r an die Seiten, eine &6Echoscherbe&r in die Mitte, das ergibt &e2 Verstärkten Tiefenschiefer&r. Fünfmal craften, und der Rahmen steht. Der Rahmen in der Antiken Stadt lässt sich nicht abbauen.",
              "",
              "&eZünden:&r Klick mit dem &6Herz der Tiefen&r in der Hand auf den Rahmen. Das Herz wird dabei verbraucht, ein Herz pro Portal.",
              "",
              "&eDer andere Weg:&r Occultism macht den Block auch im Ritual (Pentakel Contact Wild Spirit) aus 4 Eisengittern, 4 Obsidian und einem Iesniumbarren, allerdings mit einem &cWärter als Opfer&r pro Block. Siehe Kapitel Occultism: Afrit und Marid.",
          ],
          tasks=[task_item("minecraft:reinforced_deepslate", 10)],
          rewards=[reward_item("minecraft:echo_shard", 2), reward_table("s3_common")],
          deps=["warden"], icon="minecraft:reinforced_deepslate", size=1.75, shape="hexagon"),

    quest("arrival", 9, 6.5, "&5Geh hinüber",
          subtitle="Immer Mitternacht, immer eine Decke über dir.",
          description=[
              "Geh durch das Portal. Drüben baut dir das Spiel ein Gegenstück aus Verstärktem Tiefenschiefer, &e6 breit und 3 hoch&r.",
              "",
              "&eWas anders ist:&r Die &5Anderwelt&r hat eine Decke und keinen Himmel, die Welt ist &e128 Blöcke&r hoch und es ist immer Mitternacht. Monster spawnen überall unter &eLichtlevel 7&r, also nimm Fackeln mit. &6Betten&r funktionieren.",
              "",
              "Ein Block hier ist ein Block in der Oberwelt, als Abkürzung taugt sie also nicht. Dafür liegen unter dem Sculk dieselben Erze wie zu Hause, siehe weiter unten.",
          ],
          tasks=[task_dimension("deeperdarker:otherside")],
          rewards=[reward_item("minecraft:torch", 64), reward_item("minecraft:cooked_beef", 16), reward_xp(10)],
          deps=["portal"], icon="deeperdarker:sculk_stone", size=1.75, shape="hexagon"),

    # ---- Die Biome ---------------------------------------------------------------
    quest("deeplands", 12, 1.5, "&3Durchquere die Tiefenlande",
          subtitle="Säulen aus Sculkgestein, und Phantome ohne Schlafmangel.",
          description=[
              "Die &3Tiefenlande&r sind das Hauptbiom: Säulen aus &6Sculkgestein&r, Sculkranken, Sensoren, und an den Wänden der leuchtende &6Sculkglanz&r.",
              "",
              "&eWer hier wohnt:&r Sculk-Schnapper, Zerschmetterte, &6Sculk-Hundertfüßer&r (20 Lebenspunkte, lassen Fäden fallen) und &cPhantome&r, auch wenn du geschlafen hast. Hier stehen auch die Antiken Tempel.",
          ],
          tasks=[task_item("deeperdarker:sculk_gleam", 4)],
          rewards=[reward_item("minecraft:phantom_membrane", 2), reward_xp(5)],
          deps=["arrival"], icon="deeperdarker:sculk_gleam"),

    quest("echoing_forest", 14.5, 1.5, "&2Finde den Hallenden Wald",
          subtitle="Echobäume auf Echoboden.",
          description=[
              "Im &2Hallenden Wald&r wachsen &6Echobäume&r auf &6Echoboden&r. Fäll ein paar Stämme, aus einem Stamm werden vier Bretter.",
              "",
              "Hier sind die &6Zerschmetterten&r am dichtesten. Halt dich an die Baumkronen, wenn es eng wird.",
          ],
          tasks=[task_item("deeperdarker:echo_log", 8)],
          rewards=[reward_item("deeperdarker:echo_sapling", 2), reward_xp(5)],
          deps=["arrival"], icon="deeperdarker:echo_log"),

    quest("blooming_caverns", 17, 1.5, "&dFinde die Blühenden Höhlen",
          subtitle="Das einzige Biom mit Wasser und Essen.",
          description=[
              "Die &dBlühenden Höhlen&r sind hell: &6Blühendes Moos&r, leuchtende Blumen und Gras, Tümpel mit &6Anglerfischen&r. An den &6Leuchtenden Ranken&r hängen &6Blütenbeeren&r, die du mit Rechtsklick pflückst.",
              "",
              "&eEssen:&r Beeren roh, Anglerfisch gebraten. Es ist das einzige Biom, in dem du dich hier unten satt essen kannst.",
              "",
              "&eAchtung:&r Der &6Schlamm&r (Sludge) lebt hier, ein Schleim aus Sculk. Die kleinsten lassen &6Resonarium&r fallen, siehe unten.",
          ],
          tasks=[task_item("deeperdarker:bloom_berries", 8), task_item("deeperdarker:cooked_angler_fish", 2)],
          rewards=[reward_item("deeperdarker:blooming_moss_block", 8), reward_xp(5)],
          deps=["arrival"], icon="deeperdarker:bloom_berries"),

    quest("overcast_columns", 19.5, 1.5, "&7Finde die Bewölkten Säulen",
          subtitle="Düsterschiefer, Geysire und Bernstein.",
          description=[
              "Die &7Bewölkten Säulen&r bestehen aus &6Düsterschiefer&r, mit Magma, Seelensand und &6Düsterem Sculk&r am Boden. Hier spawnt kein Monster von selbst.",
              "",
              "Zwischen den Säulen steckt &6Kristallisierter Bernstein&r. Darin ist etwas eingeschlossen, mal ein Gegenstand (Amethyst, Diamant, Smaragd, verzauberte Stiefel), mal ein &cSculk-Egel&r. Mit &eBehutsamkeit&r nimmst du ihn mit, der Tooltip verrät den Inhalt. Ohne kommt der Inhalt heraus.",
              "",
              "Jeder hundertste Fleck Düsterer Sculk ist ein &6Düsterer Geysir&r. Er ist heiß, 2000 Grad für PneumaticCraft, falls du eine Wärmequelle suchst.",
          ],
          tasks=[task_item("deeperdarker:cobbled_gloomslate", 16)],
          rewards=[reward_item("deeperdarker:crystallized_amber", 1), reward_xp(5)],
          deps=["arrival"], icon="deeperdarker:gloomslate"),

    quest("explore_all", 22, 1.5, "&bEchoortung",
          subtitle="Alle vier Biome gesehen.",
          description=[
              "Sieh dir alle vier Biome der Anderwelt an: &3Tiefenlande&r, &2Hallender Wald&r, &dBlühende Höhlen&r und &7Bewölkte Säulen&r.",
              "",
              "Die Biome liegen in großen Flächen nebeneinander, lauf eine Richtung lange genug, dann kommt das nächste.",
          ],
          tasks=[task_advancement("deeperdarker:main/explore_otherside", "Alle Biome der Anderwelt besuchen")],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["deeplands", "echoing_forest", "blooming_caverns", "overcast_columns"],
          icon="minecraft:recovery_compass", size=1.5, shape="diamond"),

    # ---- Stein und Holz ----------------------------------------------------------
    quest("stone", 12, 6.5, "&7Verarbeite Sculkgestein und Düsterschiefer",
          subtitle="Bruchstein brennen, dann Ziegel, Fliesen, Poliert, Geschnitten, Glatt.",
          description=[
              "&6Sculkgestein&r bricht zu &6Bruchsculkgestein&r, &6Düsterschiefer&r zu &6Bruchdüsterschiefer&r. Im Ofen wird daraus wieder der ganze Block. Alle Varianten gibt es am &6Steinschneider&r.",
              "",
              "&eErze:&r In beiden Steinen stecken Kohle, Eisen, Kupfer, Gold, Redstone, Lapis, Smaragd und Diamant, genau wie zu Hause. Die &6Zerkleinerungsräder&r von Create und der Mekanism-Anreicherer kennen sie.",
              "",
              "&eMekanism:&r Der &6Anreicherer&r macht aus Bruchstein den Stein, aus Fliesen Ziegel, aus Ziegeln Poliert und aus Poliert Geschnitten. Praktisch für große Mengen Baustoff.",
          ],
          tasks=[task_item("deeperdarker:sculk_stone", 32), task_item("deeperdarker:gloomslate", 32)],
          rewards=[reward_item("deeperdarker:sculk_stone_bricks", 32), reward_xp(5)],
          deps=["arrival"], icon="deeperdarker:sculk_stone_bricks"),

    quest("light", 14.5, 6.5, "&eBau eine Düsterschieferlampe",
          subtitle="Vier Düsterschiefer um einen Sculkglanz.",
          description=[
              "&6Sculkglanz&r leuchtet von allein, du findest ihn an den Wänden der Tiefenlande und im Hallenden Wald. Vier &6Düsterschiefer&r darum ergeben eine &6Düsterschieferlampe&r, die zur Welt hier unten passt.",
              "",
              "Im Steinschneider gibt es für Sculkgestein und Düsterschiefer je zwei Dutzend Formen. Wer in der Anderwelt baut, baut aus dem, was da ist.",
          ],
          tasks=[task_item("deeperdarker:gloomslate_light", 4)],
          rewards=[reward_item("deeperdarker:sculk_gleam", 8), reward_xp(5)],
          deps=["stone"], icon="deeperdarker:gloomslate_light"),

    quest("echo_wood", 17, 6.5, "&2Pflanze Echoholz",
          subtitle="Bretter, Boote, Türen, und ein Setzling aus dem Laub.",
          description=[
              "Ein &6Echostamm&r ergibt vier &6Echoholzbretter&r. Daraus gibt es den ganzen Satz: Treppen, Zaun, Tür, Falltür, Schilder und ein &6Echoholzboot&r für die Tümpel.",
              "",
              "&eSetzlinge:&r &6Echolaub&r lässt beim Abbauen einen &6Echosetzling&r fallen, etwa jedes zwanzigste Mal, mit Glück öfter. Der Baum wächst auch in der Oberwelt. Mit der Schere nimmst du das Laub selbst mit.",
          ],
          tasks=[task_item("deeperdarker:echo_planks", 32), task_item("deeperdarker:echo_sapling", 1)],
          rewards=[reward_item("deeperdarker:echo_boat", 1), reward_xp(5)],
          deps=["echoing_forest"], icon="deeperdarker:echo_planks", section="stone"),

    quest("gleam_gel", 19.5, 6.5, "&eKratz Glanzgel ab",
          subtitle="Schere an den Porösen Sculkglanz.",
          description=[
              "An den Sculkglanz-Klumpen sitzt &6Poröser Sculkglanz&r. Mit der &6Schere&r kratzt du &6Glanzgel&r ab, und der Block füllt sich wieder.",
              "",
              "&eWofür:&r Mit Glanzgel &ezähmst&r du Sculk-Schnapper, siehe unten. Ein &6Seltsamer Trank&r plus Glanzgel wird zum &6Trank der Leuchtkraft&r. Neun Gel ergeben einen &6Glanzgelblock&r, der einen Sturz abfängt.",
          ],
          tasks=[task_item("deeperdarker:gleam_gel", 8)],
          rewards=[reward_item("minecraft:shears", 1), reward_xp(5)],
          deps=["deeplands"], icon="deeperdarker:gleam_gel", section="stone"),

    # ---- Die Sculk-Monster -------------------------------------------------------
    quest("snapper", 12, 11, "&3Zähme einen Sculk-Schnapper",
          subtitle="Ein Hund aus Sculk, der Bücher ausgräbt.",
          description=[
              "Der &6Sculk-Schnapper&r ist klein, schnell und beißt (&e12 Lebenspunkte, 3 Schaden&r). Er lässt &6Seelenstaub&r fallen. Mit &6Glanzgel&r in der Hand &ezähmst&r du ihn wie einen Wolf.",
              "",
              "&eWarum sich das lohnt:&r Ein gezähmter Schnapper schnüffelt im Boden und gräbt &6verzauberte Bücher&r aus, bis zu &e8 Stück&r pro Tier. Er folgt dir und kämpft mit.",
          ],
          tasks=[task_kill("deeperdarker:sculk_snapper", 5), task_item("deeperdarker:soul_dust", 4)],
          rewards=[reward_item("deeperdarker:gleam_gel", 4), reward_xp(10)],
          deps=["arrival"], icon="deeperdarker:sculk_snapper_spawn_egg"),

    quest("shattered", 14.5, 11, "&8Zerschlag die Zerschmetterten",
          subtitle="Sie hören dich, bevor sie dich sehen.",
          description=[
              "Die &6Zerschmetterten&r sind die Fußsoldaten der Anderwelt: &e50 Lebenspunkte, 6 Schaden&r, etwas Rüstung, langsam. Sie reagieren auf &eSchwingungen&r wie ein Sculk-Sensor, Schleichen hilft.",
              "",
              "&eBeute:&r &e1 bis 3 Sculkknochen&r. Die brauchst du für die Seelenelytren und den Schallstab aus Stufe 4, sammle sie also schon.",
              "",
              "&eVerzauberung:&r &6Sculk-Bann&r auf dem Schwert macht mehr Schaden gegen alle Sculk-Monster, auch gegen den Wärter.",
          ],
          tasks=[task_kill("deeperdarker:shattered", 5), task_item("deeperdarker:sculk_bone", 8)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["arrival"], icon="deeperdarker:sculk_bone"),

    quest("infested", 17, 11, "&cBrich Befallenen Sculk auf",
          subtitle="Egel oder ein Wurm, beides unangenehm.",
          description=[
              "&6Befallener Sculk&r sieht aus wie normaler Sculk und steckt in Adern im Sculkgestein. Brichst du ihn ohne Behutsamkeit, wirst du zurückgestoßen und heraus kommen &6Sculk-Egel&r oder ein &4Shriek-Wurm&r.",
              "",
              "&eSculk-Egel:&r Winzig, &e4 Lebenspunkte&r, in Gruppen. Sie lassen &6Seelenstaub&r fallen. Mit &eBehutsamkeit&r bekommst du statt dessen einfach Sculk.",
          ],
          tasks=[task_kill("deeperdarker:sculk_leech", 8)],
          rewards=[reward_item("deeperdarker:soul_dust", 4), reward_xp(10)],
          deps=["shattered"], icon="deeperdarker:infested_sculk"),

    quest("shriek_worm", 19.5, 11, "&4&lErlege einen Shriek-Wurm",
          subtitle="Er kommt aus dem Boden und bleibt dort stehen.",
          description=[
              "Der &4Shriek-Wurm&r steigt aus Befallenem Sculk auf, kreischt und schlägt zu, wer in Reichweite steht: &e100 Lebenspunkte, 7 Schaden&r. Er bewegt sich nicht vom Fleck.",
              "",
              "&eTaktik:&r Zwei Schritte zurück und mit dem Bogen arbeiten. Er lässt nichts fallen, aber er zählt für den Sculk-Jäger am Ende des Kapitels.",
          ],
          tasks=[task_kill("deeperdarker:shriek_worm", 1)],
          rewards=[reward_table("s3_uncommon"), reward_xp(20)],
          deps=["infested"], icon="deeperdarker:shriek_worm_spawn_egg", size=1.5, shape="diamond"),

    quest("sludge", 22, 11, "&aJage Schlamm",
          subtitle="Die kleinsten lassen Resonarium fallen.",
          description=[
              "&6Schlamm&r lebt in den Blühenden Höhlen und teilt sich beim Tod wie ein Schleim. Nur die &ekleinste Größe&r lässt &6Resonarium&r fallen, 0 bis 1 Stück, mit Plünderung mehr.",
              "",
              "Resonarium ist das einzige neue Metall der Anderwelt und der Weg zu Werkzeug und Rüstung, die dem Wärter standhalten. Sammle fleißig, eine Platte braucht vier.",
          ],
          tasks=[task_kill("deeperdarker:sludge", 10), task_item("deeperdarker:resonarium", 4)],
          rewards=[reward_item("deeperdarker:resonarium", 2), reward_xp(10)],
          deps=["blooming_caverns"], icon="deeperdarker:resonarium"),

    # ---- Der Antike Tempel -------------------------------------------------------
    quest("temple", 15, 15, "&5&lFinde einen Antiken Tempel",
          subtitle="Fliesen, Vasen und Kreischer, die rufen können.",
          description=[
              "Der &6Antike Tempel&r steht in den Tiefenlanden: Hallen aus Sculkgesteinfliesen, ein Keller mit Thronsaal, ein Oberbau mit Brunnen. Überall &6Sensoren&r, &6Antike Vasen&r und &cKreischer, die einen Wärter rufen können&r. Schleichen.",
              "",
              "&eIn den Truhen:&r Echoscherben, Seelenstaub, Sculkknochen, Kristallisierter Bernstein, Diamanten, Namensschilder, Resonarium-Vorlagen, mit Glück ein Seelenkristall. Irgendwo gibt es einen &6Geheimgang&r mit einer Truhe, in der immer ein &6Sculksender&r liegt.",
              "",
              "&eVasen:&r Darin sind Sand, Fäden, Gold, manchmal ein Goldapfel oder Diamanten. Jede sechste Vase ist &cunecht&r, und aus jeder dritten unechten steigt ein &4Beobachter&r. Zerschlag Vasen also nur mit freiem Rücken.",
          ],
          tasks=[task_advancement("deeperdarker:main/find_ancient_temple", "Einen Antiken Tempel betreten")],
          rewards=[reward_table("s3_uncommon"), reward_item("minecraft:torch", 32), reward_xp(15)],
          deps=["deeplands"], icon="deeperdarker:sculk_stone_tiles", size=1.75, shape="hexagon"),

    quest("stalker", 18, 15, "&4&lBesiege den Beobachter",
          subtitle="Der größte Gegner der Anderwelt.",
          description=[
              "Der &4Beobachter&r (Stalker) ist drei Blöcke hoch, hat &e200 Lebenspunkte&r, Rüstung und schlägt mit &c22 Schaden&r zu. Wenn er dich trifft, lässt er &6Sculk-Egel&r auf dich los. Er kommt aus unechten Vasen im Tempel.",
              "",
              "&eBeute:&r Ein &6Seelenkristall&r, mit Plünderung bis zu drei. Den Kristall brauchst du für den Trank der Sculk-Affinität und für die Seelenelytren aus Stufe 4.",
              "",
              "&eTipps:&r Volle Diamantrüstung, Goldäpfel, und zerschlag die Vasen eine nach der anderen. Zu zweit ist er machbar, zu dritt bequem.",
          ],
          tasks=[task_kill("deeperdarker:stalker", 1), task_item("deeperdarker:soul_crystal", 1)],
          rewards=[reward_table("s3_uncommon"), reward_item("minecraft:golden_apple", 4), reward_xp(25)],
          deps=["temple"], icon="deeperdarker:soul_crystal", size=1.75, shape="diamond"),

    quest("transmitter", 21, 15, "&bVerbinde einen Sculksender",
          subtitle="Deine Truhe, von überall aus.",
          description=[
              "Den &6Sculksender&r findest du in der Geheimtruhe des Antiken Tempels. &eRechtsklick auf eine Truhe&r, ein Fass, einen Ofen, eine Werkbank, einen Amboss oder einen Zaubertisch verbindet ihn. &eRechtsklick in die Luft&r öffnet den verbundenen Block, egal wo du bist, auch aus einer anderen Dimension.",
              "",
              "Der Tooltip zeigt Position und Dimension. Mit einem Farbstoff färbst du ihn, so unterscheidest du mehrere. Ist der Chunk nicht geladen, meldet er das und passiert nichts.",
              "",
              "&eKronwerke:&r Eine Truhe neben dem Obelisken, ein Sender in der Tasche, und du lieferst Zielgegenstände ab, ohne nach Hause zu laufen.",
          ],
          tasks=[task_advancement("deeperdarker:main/obtain_sculk_transmitter", "Einen Sculksender bekommen")],
          rewards=[reward_item("minecraft:ender_chest", 1), reward_xp(15)],
          deps=["temple"], icon="deeperdarker:sculk_transmitter", size=1.5),

    # ---- Seelen und Resonarium ---------------------------------------------------
    quest("soul_dust", 15, 19, "&bBraue Sculk-Affinität",
          subtitle="Die Sculk-Welt hört dich nicht mehr.",
          description=[
              "&6Seltsamer Trank&r plus &6Seelenkristall&r, oder &6Trank der Unsichtbarkeit&r plus &6Seelenstaub&r, ergibt den &6Trank der Sculk-Affinität&r. Redstone verlängert ihn.",
              "",
              "&eWirkung:&r Solange er läuft, nehmen Sculk-Sensoren, Kreischer und der Wärter deine Schwingungen nicht wahr. Für Antike Städte und Tempel ist das der wichtigste Trank im Pack.",
              "",
              "&eAußerdem:&r Vier &6Seelenstaub&r um ein Glas ergeben zwei &6Schalldichtes Glas&r.",
          ],
          tasks=[task_item("deeperdarker:soul_dust", 16), task_item("deeperdarker:soundproof_glass", 4)],
          rewards=[reward_item("minecraft:glass_bottle", 6), reward_item("minecraft:redstone", 8), reward_xp(10)],
          deps=["infested"], icon="deeperdarker:soul_dust", section="souls"),

    quest("resonarium", 18, 19, "&6&lSchmiede Resonarium",
          subtitle="Die Rüstung gegen den Schallangriff.",
          description=[
              "Eine &6Resonariumplatte&r entsteht formlos aus &e4 Resonarium&r und &e4 Hornschilden&r (Schildkröte oder Gürteltier). Am &6Schmiedetisch&r machst du mit der &6Resonarium-Schmiedevorlage&r aus einem &eDiamantwerkzeug oder einer Diamantrüstung&r das Resonarium-Gegenstück.",
              "",
              "&eDie Vorlage&r liegt in Antiken Städten, Festungsgängen und Prüfungskammern, und in den Tempeltruhen. Kopieren: 7 Diamanten, die Vorlage und ein Resonarium ergeben zwei.",
              "",
              "&eWarum:&r Jedes Teil &6Resonariumrüstung&r fängt ein Viertel von dem Schaden ab, der sonst durch Rüstung geht, etwa der &cSchallangriff des Wärters&r. Mit allen vier Teilen bleibt davon nichts übrig. Die Rüstung nutzt sich dabei ab.",
              "",
              pic("deeperdarker:resonarium"),
          ],
          tasks=[task_item("deeperdarker:resonarium_plate", 2), task_item("deeperdarker:resonarium_chestplate", 1)],
          rewards=[reward_table("s3_uncommon"), reward_item("deeperdarker:resonarium", 4), reward_xp(20)],
          deps=["sludge", "temple"], icon="deeperdarker:resonarium_chestplate", size=1.75),

    quest("slayer", 21, 19, "&4&lSculk-Jäger",
          subtitle="Von jedem Sculk-Monster eines.",
          description=[
              "Erlege je eines von allem, was hier unten lebt: &6Anglerfisch&r, &6Phantom&r, &6Sculk-Hundertfüßer&r, &6Sculk-Egel&r, &6Sculk-Schnapper&r, &6Zerschmetterter&r, &6Shriek-Wurm&r, &6Beobachter&r und den &4Wärter&r.",
              "",
              "Den Wärter kannst du hier unten holen: Die Kreischer in den Antiken Tempeln dürfen ihn rufen. Oder du nimmst den aus der Oberwelt, der zählt genauso.",
              "",
              "&eKronwerke:&r Das Stufenziel von Stufe 3 braucht &e150 Afrit-Essenz&r, jede Beschwörung ein Kampf. Wer hier unten Übung mit Beobachtern hat, lacht über Afrits.",
          ],
          tasks=[task_advancement("deeperdarker:main/kill_all_sculk_mobs", "Von jedem Sculk-Monster eines erlegen")],
          rewards=[reward_table("s3_rare"), reward_item("minecraft:diamond", 4), reward_xp(30)],
          deps=["stalker", "shriek_worm", "snapper"], icon="deeperdarker:sculk_bone", size=2.5, shape="gear"),

    # ---- Ausblick Stufe 4 --------------------------------------------------------
    quest("outlook", 24, 15, "&5Ausblick: Die Wärterrüstung",
          subtitle="Kommt in Stufe 4.",
          description=[
              "Mit &eStufe 4&r kommt die Rüstung aus dem Wärter: Mit der &6Wärter-Schmiedevorlage&r aus der Antiken Stadt oder der Tempel-Geheimtruhe wird am Schmiedetisch aus &eNetherit&r plus einer &6Verstärkten Echoscherbe&r die &6Wärterrüstung&r und das Wärterwerkzeug. Die Vorlage kopierst du mit 7 Diamanten und einem Sculk.",
              "",
              "&6Wärterstiefel&r dämpfen deine Schritte, Sensoren hören sie nicht. Die &6Seelenelytren&r (Elytren, Seelenkristall, 2 Seelenstaub, 4 Sculkknochen) haben einen Schub mit 30 Sekunden Abklingzeit. Der &6Schallstab&r (Herz der Tiefen, 2 Seelenkristalle, 2 Sculkknochen) feuert aufgeladen den Schallangriff des Wärters.",
              "",
              "Sammle also schon jetzt Verstärkte Echoscherben, Sculkknochen, Seelenstaub, Seelenkristalle und ein zweites Herz. Die Rezepte brauchen nichts, was du nicht schon aus diesem Kapitel kennst.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:phantom_membrane", 4)],
          deps=["stalker"], icon="deeperdarker:reinforced_echo_shard", optional=True),
    # ---- Neu ------------------------------------------------------------------
    quest("dd_catalyst", 0, 9.5, "&3Stell einen Sculk-Katalysator auf",
          subtitle="Wo etwas stirbt, wächst Sculk.",
          description=[
              "Der Wärter lässt immer einen &6Sculk-Katalysator&r fallen, manchmal liegt einer in den Truhen der Antiken Stadt.",
              "",
              "Stirbt ein Mob in seiner Nähe, breitet sich Sculk aus, um so mehr, je mehr Erfahrung der Mob gegeben hätte. Sculk baust du mit einer Hacke schnell ab, und ohne Behutsamkeit gibt jeder Block Erfahrung. Stell ihn an deine Mobfarm.",
          ],
          tasks=[task_item("minecraft:sculk_catalyst", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_xp(5)],
          deps=["warden"], icon="minecraft:sculk_catalyst", optional=True),

    quest("dd_disc", 0, 6.5, "&8Setz die Schallplatte 5 zusammen",
          subtitle="Neun Bruchstücke aus der Antiken Stadt.",
          description=[
              "In den Truhen der Antiken Städte liegen &6Plattenbruchstücke&r. Neun davon ergeben die &6Schallplatte 5&r.",
              "",
              "Lootr gibt dir jede Truhe einzeln, also lohnt es sich, eine Stadt ganz auszuräumen. Dabei findest du auch Bücher mit &eHuschen&r, Echoscherben und Verzauberte Goldene Äpfel.",
          ],
          tasks=[task_item("minecraft:music_disc_5", 1)],
          rewards=[reward_item("minecraft:echo_shard", 2), reward_xp(10)],
          deps=["ancient_city"], icon="minecraft:music_disc_5", optional=True),

    quest("dd_ores", 22, 6.5, "&bGrab Diamanten in der Anderwelt",
          subtitle="Alle Erze, nur in anderem Gestein.",
          description=[
              "Bring &e8 Diamanten&r aus der Anderwelt mit. Im &6Sculkgestein&r und im &6Düsterschiefer&r stecken dieselben Erze wie oben: Kohle, Eisen, Kupfer, Gold, Redstone, Lapis, Smaragd und Diamant.",
              "",
              "Die Höhlen sind riesig und offen, die Erze liegen oft frei an den Wänden. Leise gehen: Wo Sensoren stehen, sind auch Kreischer nicht weit.",
          ],
          tasks=[task_item("minecraft:diamond", 8)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(10)],
          deps=["stone"], icon="deeperdarker:gloomslate_diamond_ore", optional=True),

    quest("dd_centipede", 12, 9.5, "&3Erleg Sculk-Hundertfüßer",
          subtitle="Lang, flink und voller Fäden.",
          description=[
              "Erleg &e3 Sculk-Hundertfüßer&r. Sie krabbeln durch die &6Tiefenlande&r und lassen &6Fäden&r fallen.",
              "",
              "Fäden sind hier unten knapp. Für Bögen, Wolle und die Seelenelytren später brauchst du sie trotzdem.",
          ],
          tasks=[task_kill("deeperdarker:sculk_centipede", 3)],
          rewards=[reward_item("minecraft:string", 16), reward_xp(5)],
          deps=["snapper"], icon="minecraft:string", optional=True),

    quest("dd_sculk_smite", 14.5, 9.5, "&bLern den Sculk-Bann",
          subtitle="Eine Schwertverzauberung nur gegen Sculk.",
          description=[
              "Am Zaubertisch kann ein Schwert &eSculk-Bann&r bekommen: pro Stufe &d2,5&r Schaden mehr gegen alle Sculk-Wesen, bis Stufe &d5&r. Das schließt Schärfe und Bann aus.",
              "",
              "Es trifft Zerschmetterte, Beobachter, Shriek-Würmer und auch den &4Wärter&r. Den brauchst du: &eKronwerke Core&r gibt Mobs in Stufe 3 &d70 Prozent&r mehr Leben, aus 500 werden 850 Lebenspunkte.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["shattered"], icon="minecraft:enchanted_book", optional=True),

    quest("dd_carapace", 17, 13.5, "&8Sammle Wärterpanzer",
          subtitle="Für Echoscherben und die Rüstung in Stufe 4.",
          description=[
              "Sammle &e4 Wärterpanzer&r. Neben dem Wärter selbst liegen sie in den Truhen des Antiken Tempels und in &6Antiken Vasen&r.",
              "",
              "Aus Panzer und Phantomhaut werden &6Verstärkte Echoscherben&r. Jedes Teil der Wärterrüstung in Stufe 4 braucht eine, also leg schon jetzt einen Vorrat an.",
          ],
          tasks=[task_item("deeperdarker:warden_carapace", 4)],
          rewards=[reward_item("minecraft:phantom_membrane", 4), reward_xp(10)],
          deps=["temple"], icon="deeperdarker:warden_carapace"),

    quest("dd_soul_crystals", 21, 13.5, "&bLeg Seelenkristalle zurück",
          subtitle="Jeder Beobachter gibt einen.",
          description=[
              "Sammle &e3 Seelenkristalle&r. Jeder &4Beobachter&r lässt einen fallen, ganz selten liegt einer in einer Tempeltruhe.",
              "",
              "In Stufe 4 brauchst du einen für die &6Seelenelytren&r und zwei für den &6Schallstab&r. Wer jetzt Beobachter jagt, steht dann nicht mit leeren Händen da.",
          ],
          tasks=[task_item("deeperdarker:soul_crystal", 3)],
          rewards=[reward_table("s3_uncommon"), reward_xp(15)],
          deps=["stalker"], icon="deeperdarker:soul_crystal", optional=True),

    quest("dd_resonarium_set", 21, 17.5, "&6&lTrag die volle Resonariumrüstung",
          subtitle="Vier Teile, kein Schallangriff kommt mehr durch.",
          description=[
              "Mach auch &6Helm&r, &6Beinschutz&r und &6Stiefel&r aus Resonarium: jedes Teil eine Diamantrüstung, eine Resonariumplatte und eine Vorlage am Schmiedetisch.",
              "",
              "Mit allen vier Teilen fängt die Rüstung den Schaden ab, der sonst durch jede Rüstung geht, auch den &cSchallangriff des Wärters&r. Sie nutzt sich dabei ab, nimm Reparatur oder Ersatzplatten mit.",
          ],
          tasks=[task_item("deeperdarker:resonarium_helmet", 1), task_item("deeperdarker:resonarium_leggings", 1), task_item("deeperdarker:resonarium_boots", 1)],
          rewards=[reward_table("s3_rare"), reward_xp(20)],
          deps=["resonarium"], icon="deeperdarker:resonarium_helmet", optional=True),

]

images = [
    banner("deeper_darker/title", "Deeper and Darker", 11, -3.2, height=1.75, kind="title", colour="end"),
    banner("deeper_darker/way", "Der Weg hinunter", 3, 5.2, height=0.9, colour="stone"),
    banner("deeper_darker/biomes", "Die Biome", 15.5, 0, height=0.9, colour="end"),
    banner("deeper_darker/stone", "Stein und Holz", 16, 4.4, height=0.9, colour="stone"),
    banner("deeper_darker/mobs", "Die Sculk-Monster", 16, 8.9, height=0.9, colour="fire"),
    banner("deeper_darker/temple", "Der Antike Tempel", 19, 12.9, height=0.9, colour="magic"),
    banner("deeper_darker/souls", "Seelen und Resonarium", 18, 17, height=0.9, colour="magic"),
]

chapter(C, "Deeper and Darker", "deeperdarker:sculk_transmitter", "world", quests, shape="circle", order=65, stage=3,
        subtitle=["Stufe 3: Die Tiefe Dunkelheit, der Wärter und das Portal, die Anderwelt mit ihren vier Biomen, die Sculk-Monster und Resonarium."],
        images=images)
