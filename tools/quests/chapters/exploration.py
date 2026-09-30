"""Erkundung: Orientierung, Wegsteine, die Minendimension, Bauwerke mit ihrer Beute und
Ausrüstung mit Affixen aus Apotheosis. Alles in der Oberwelt; der Nether ist Stufe 2."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "exploration"
MINING = "ultimate_mining_dimension:ultimate_mining_dimension"

quests = [
    quest("welcome", 0, 3, "&6Erkundung",
          subtitle="Die Welt ist größer und seltsamer als in Vanilla.",
          description=[
              "Die Oberwelt der Kronwerke ist neu gewürfelt: &6Terralith&r und &6Biomes O' Plenty&r bringen Dutzende neue Biome, &6Tectonic&r formt höhere Berge und tiefere Täler. Dazwischen stehen Dörfer, Türme, Verliese, Ruinen und ein paar Orte, die du besser nicht allein besuchst.",
              "",
              "Dieses Kapitel zeigt dir, wie du dich zurechtfindest, wie du mit &6Wegsteinen&r schnell reist, wie du in die &6Minendimension&r kommst, was in den Bauwerken wartet und was es mit der Ausrüstung mit &6Affixen&r auf sich hat.",
              "",
              "&eGut zu wissen:&r Beute in Bauwerken gibt es für jeden Spieler einzeln. Wer als Zweiter ankommt, geht nicht leer aus.",
          ],
          tasks=[task_checkmark("Ab nach draußen")],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_table("s1_common")],
          icon="minecraft:filled_map", size=2.5, shape="hexagon"),

    # ---- Orientierung ---------------------------------------------------------
    quest("e_map", 4.5, -7, "&6Die Karte",
          subtitle="Nie wieder verlaufen.",
          description=[
              "Mit &eM&r öffnest du die große Karte von &6FTB Chunks&r. Sie zeichnet alles auf, was du gesehen hast, und auf ihr beanspruchst du auch deine Chunks. Wer lieber mit JourneyMap arbeitet, öffnet sie mit &eJ&r.",
              "",
              "Setz dir &eWegpunkte&r: an deiner Basis, an Erzfunden, an Dörfern, am Portal zur Minendimension. Das spart dir später viel Sucherei.",
              "",
              "&eTipp:&r Mit &eF3&r siehst du deine genauen Koordinaten. Schreib sie dir auf, bevor du irgendwo hinabsteigst.",
          ],
          tasks=[task_checkmark("Karte angeschaut")],
          rewards=[reward_item("minecraft:bread", 8)],
          deps=["welcome"], icon="minecraft:map"),

    quest("e_biomes", 6.5, -7, "&aNeue Welten",
          subtitle="Jedes Biom hat seine eigenen Schätze.",
          description=[
              "Wenn du ein neues Biom betrittst, blendet &6Traveler's Titles&r seinen Namen ein. So merkst du schnell, wie viele es davon gibt.",
              "",
              "Neue Biome heißt auch neue Hölzer, Blumen und Pflanzen. Für Botania brauchst du Blumen in allen Farben, für Farmer's Delight wilde Pflanzen, die nur in bestimmten Gegenden wachsen: Tomaten mögen es warm, Reis wächst im seichten Wasser, Kohl findest du an der Küste.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_item("minecraft:bone_meal", 16)],
          deps=["e_map"], icon="minecraft:oak_sapling"),

    quest("e_compass", 8.5, -7, "&6Kompass der Natur",
          subtitle="Zeigt dir den Weg zu jedem Biom.",
          description=[
              "Der &6Kompass der Natur&r findet jedes Biom für dich. Das Rezept: ein normaler &6Kompass&r in der Mitte, vier &6Holzstämme&r an den Seiten und vier &6Setzlinge&r in den Ecken.",
              "",
              "Rechtsklick öffnet die Liste aller Biome. Wähl eines aus, und der Kompass zeigt auf das nächstgelegene und sagt dir, wie weit es entfernt ist.",
              "",
              "&eTipp:&r Die klassische erste Suche ist der &dArchwood-Wald&r für Ars Nouveau.",
          ],
          tasks=[task_item("naturescompass:naturescompass", 1)],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["e_biomes"], icon="naturescompass:naturescompass"),

    quest("e_archwood", 10.5, -7, "&dArchwood-Wald",
          subtitle="Bunte Bäume voller Magie.",
          description=[
              "Im &dArchwood-Wald&r wachsen Bäume in vier Farben, und jede Farbe gehört zu einer Schule der Magie von Ars Nouveau. Ihr Holz, ihre Setzlinge und die Früchte daran brauchst du für viele Zauber-Geräte.",
              "",
              "Findest du keinen Archwood-Wald in der Nähe, kannst du die Setzlinge auch am &6Markt&r von Farming for Blockheads kaufen, jeweils für einen Smaragd. Mehr dazu im Kapitel &6Essen und Landwirtschaft&r.",
          ],
          tasks=[task_checkmark("Gefunden")],
          rewards=[reward_item("minecraft:emerald", 4)],
          deps=["e_compass"], icon="ars_nouveau:blue_archwood_sapling"),

    quest("e_village", 12.5, -7, "&6Dörfer",
          subtitle="Handel, Betten und ein Wegstein.",
          description=[
              "Dörfer sind die erste gute Adresse auf jeder Reise. Die Dorfbewohner handeln mit &6Smaragden&r, und die brauchst du öfter, als du denkst: für den Warpstein, für den Markt und für manche Tauschgeschäfte.",
              "",
              "In vielen Dörfern steht außerdem ein &6Wegstein&r. Aktivier ihn, dann kommst du jederzeit wieder hin. Einige Dörfer haben auch eine &6Belohnungstafel&r mit Aufträgen.",
              "",
              "&eTipp:&r Bau nicht mitten im Dorf, und lass die Bewohner am Leben. Mit ihnen handelt auch der Rest des Servers.",
          ],
          tasks=[task_checkmark("Ein Dorf gefunden")],
          rewards=[reward_item("minecraft:emerald", 4)],
          deps=["e_compass"], icon="minecraft:emerald"),

    quest("e_bounty", 14.5, -7, "&6Belohnungstafel",
          subtitle="Aufträge gegen Belohnung.",
          description=[
              "An einer &6Belohnungstafel&r aus Bountiful hängen Aufträge: Bring dies, besiege jenes, und das in einer bestimmten Zeit. Rechtsklick auf die Tafel zeigt dir die Angebote. Nimm dir einen Auftrag, sammle, was verlangt wird, und klick die Tafel damit erneut an, um ihn abzuschließen.",
              "",
              "Die Belohnungen sind oft Smaragde und nützliche Gegenstände. Mit einem &6Dekret&r legst du fest, welche Art Aufträge eine Tafel anbietet.",
              "",
              "Findest du keine Tafel, bau dir selbst eine: Eichenbretter, Eichenstämme, Papier und ein Diamant.",
          ],
          tasks=[task_advancement("bountiful:bountiful/bounty_complete", "Einen Auftrag erfüllt")],
          rewards=[reward_table("s1_common")],
          deps=["e_village"], icon="bountiful:bountyboard"),

    # ---- Reisen ---------------------------------------------------------------
    quest("e_waystone_find", 4.5, 0, "&6Wegsteine",
          subtitle="Einmal aktivieren, immer wieder hinreisen.",
          description=[
              "&6Wegsteine&r stehen in Dörfern und hier und da in der Wildnis. Ein Rechtsklick aktiviert einen Wegstein für dich. Ab dann kannst du von jedem Wegstein aus zu allen reisen, die du schon aktiviert hast.",
              "",
              "Die Reise kann Erfahrung kosten, je nachdem, wie weit sie geht. Was ein Ziel kostet, steht im Auswahlmenü direkt daneben.",
              "",
              "&eTipp:&r Aktiviere jeden Wegstein, an dem du vorbeikommst. Auch der am Spawn gehört dazu, dann bist du mit einem Klick beim Obelisken.",
          ],
          tasks=[task_checkmark("Einen Wegstein aktiviert")],
          rewards=[reward_item("waystones:warp_dust", 4)],
          deps=["welcome"], icon="waystones:waystone", size=1.5),

    quest("e_warp_dust", 7, -1, "&6Warppulver",
          subtitle="Der Stoff, aus dem die Reisen sind.",
          description=[
              img(item_texture("waystones:warp_dust"), 32, 32),
              "",
              "Eine &6Enderperle&r und eine &6Amethystscherbe&r ergeben vier &6Warppulver&r. Enderperlen lassen Endermen fallen, die nachts überall herumlaufen. Amethyst wächst in den Geoden tief unter der Erde.",
              "",
              "Warppulver steckt im Warpstein, in der Warpplatte und in einigen anderen Reise-Gegenständen.",
          ],
          tasks=[task_item("waystones:warp_dust", 4)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["e_waystone_find"], icon="waystones:warp_dust"),

    quest("e_warp_stone", 9, -1, "&6Warpstein",
          subtitle="Reisen von überall aus.",
          description=[
              img(item_texture("waystones:warp_stone"), 32, 32),
              "",
              "Der &6Warpstein&r bringt dich von überall zu jedem Wegstein, den du aktiviert hast. Rezept: ein &6Smaragd&r in der Mitte, vier &6Enderperlen&r an den Seiten und vier &6Amethystscherben&r in den Ecken.",
              "",
              "Halte Rechtsklick gedrückt, bis er aufgeladen ist, dann wählst du dein Ziel. Danach braucht er eine Weile, bis er wieder bereit ist. Die Abklingzeit steht im Tooltip.",
          ],
          tasks=[task_item("waystones:warp_stone", 1)],
          rewards=[reward_item("waystones:return_scroll", 2)],
          deps=["e_warp_dust"], icon="waystones:warp_stone"),

    quest("e_own_waystone", 11, -1, "&6Dein eigener Wegstein",
          subtitle="Einer gehört an deine Basis.",
          description=[
              "Einen eigenen &6Wegstein&r baust du aus einem &6Warpstein&r in der Mitte, drei &6Steinziegeln&r darüber und daneben und drei &6Obsidian&r als Sockel.",
              "",
              "Stell ihn an deine Basis und gib ihm einen Namen, den andere wiedererkennen. Dann ist dein Zuhause von überall nur einen Klick entfernt.",
              "",
              "Es gibt ihn auch in anderen Looks: bemoost, aus Sandstein, Tiefenschiefer, Prismarin und mehr. JEI zeigt dir alle Varianten.",
          ],
          tasks=[task_item("waystones:waystone", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["e_warp_stone"], icon="waystones:waystone"),

    quest("e_return_scroll", 7, 1, "&6Rückkehr-Schriftrolle",
          subtitle="Der schnelle Weg zurück.",
          description=[
              img(item_texture("waystones:return_scroll"), 32, 32),
              "",
              "Aus zwei &6Goldnuggets&r, einem &6Tintenbeutel&r und drei &6Papier&r werden drei &6Rückkehr-Schriftrollen&r. Jede bringt dich einmal zum nächstgelegenen Wegstein, den du schon aktiviert hast.",
              "",
              "Pack immer eine ein, wenn du in eine Höhle oder ein Bauwerk gehst. Sie ist billiger als ein Warpstein und rettet dich, wenn es brenzlig wird.",
          ],
          tasks=[task_item("waystones:return_scroll", 1)],
          rewards=[reward_item("minecraft:paper", 6)],
          deps=["e_waystone_find"], icon="waystones:return_scroll"),

    quest("e_warp_scroll", 9, 1, "&6Warp-Schriftrolle",
          subtitle="Einmal reisen, freie Zielwahl.",
          description=[
              img(item_texture("waystones:warp_scroll"), 32, 32),
              "",
              "Die &6Warp-Schriftrolle&r ist wie ein Warpstein zum Wegwerfen: Sie öffnet einmal das Auswahlmenü aller deiner Wegsteine. Rezept: Goldnuggets, ein Tintenbeutel, eine Enderperle und Papier, ergibt drei Stück.",
              "",
              "Praktisch, solange du noch keinen Warpstein hast oder er gerade abklingt.",
          ],
          tasks=[task_item("waystones:warp_scroll", 1)],
          rewards=[reward_xp(3)],
          deps=["e_return_scroll"], icon="waystones:warp_scroll"),

    quest("e_sharestone", 11, 1, "&6Teilsteine",
          subtitle="Ein Netz für alle.",
          description=[
              "&6Teilsteine&r gibt es in allen Farben. Alle Teilsteine derselben Farbe sind miteinander verbunden, und jeder Spieler kann sie benutzen.",
              "",
              "Rezept: drei Steinziegel, zwei Farbstoffe, ein Warpstein und drei Obsidian. Ideal für ein Team oder für eine Verbindung zwischen euren Basen und dem Spawn.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_warp_scroll"], icon="waystones:purple_sharestone", optional=True),

    quest("e_warp_plate", 13, 1, "&6Warpplatte",
          subtitle="Draufstellen und weg.",
          description=[
              "Zwei &6Warpplatten&r bilden ein Paar. Leg einen &6Ruhenden Splitter&r (zwei Warppulver und ein Feuerstein) in die erste Platte, dann wird er zu einem &6eingestellten Splitter&r. Den bringst du zur zweiten Platte.",
              "",
              "Ab dann bringt dich jede Platte zur anderen, sobald du darauf stehst. Gut für feste Wege, etwa von der Basis zur Mine.",
          ],
          tasks=[task_item("waystones:warp_plate", 2)],
          rewards=[reward_item("waystones:warp_dust", 4)],
          deps=["e_sharestone"], icon="waystones:warp_plate", optional=True),

    # ---- Minendimension -------------------------------------------------------
    quest("e_pickaxe", 4.5, 6, "&6Verzauberte Spitzhacke",
          subtitle="Der Schlüssel zur Minendimension.",
          description=[
              "Die &6Minendimension&r ist eine zweite Welt zum Graben: Stein, Erz und Höhlen, und niemand stört sich an Löchern. Hier baust du ab, so viel du willst, und die Oberwelt bleibt schön.",
              "",
              "Der Schlüssel ist die &6Verzauberte Spitzhacke&r. &cGeändertes Rezept:&r Das Originalrezept des Mods braucht Netherit und lädt auf dieser Version ohnehin nicht. In den Kronwerken baust du sie aus zwei &6Diamanten&r und einem &6Goldblock&r in der oberen Reihe und zwei &6Stöcken&r darunter in der Mitte.",
          ],
          tasks=[task_item(MINING, 1)],
          rewards=[reward_item("minecraft:iron_block", 2)],
          deps=["welcome"], icon=MINING, size=1.5),

    quest("e_frame", 7, 6, "&6Der Rahmen",
          subtitle="Wie ein Netherportal, nur aus Eisen.",
          description=[
              "Das Portal baust du wie ein Netherportal, aber aus &6Eisenblöcken&r: vier Blöcke breit, fünf hoch, innen zwei mal drei frei. Die Ecken darfst du weglassen, dann reichen zehn Eisenblöcke.",
              "",
              "Dann klickst du mit der &6Verzauberten Spitzhacke&r auf die Innenseite des Rahmens, und das Portal öffnet sich.",
              "",
              "&eTipp:&r Bau das Portal an einer Stelle, die du leicht wiederfindest, am besten in oder neben deiner Basis.",
          ],
          tasks=[task_item("minecraft:iron_block", 10)],
          rewards=[reward_item("minecraft:torch", 32)],
          deps=["e_pickaxe"], icon="minecraft:iron_block"),

    quest("e_enter", 9, 6, "&6Ab in die Mine",
          subtitle="Tritt hindurch.",
          description=[
              "Auf der anderen Seite entsteht ein Portal zurück. Die Sonne scheint dort nie, es bleibt immer dämmrig.",
              "",
              "Nimm &6Fackeln&r, Essen und etwas zum Bauen mit. Erz gibt es hier wie in der Oberwelt, auch die großen Erzadern aus Kupfer und Eisen, nur nimmt dir hier niemand die Löcher übel.",
          ],
          tasks=[task_dimension(MINING)],
          rewards=[reward_table("s1_uncommon")],
          deps=["e_frame"], icon="minecraft:iron_pickaxe", size=1.5),

    quest("e_dangers", 11, 5, "&cUnter Tage",
          subtitle="Was du dort unten wissen musst.",
          description=[
              "&cBetten explodieren&r in der Minendimension, und Seelenanker funktionieren nicht. Du kannst dort also keinen Spawnpunkt setzen.",
              "",
              "Wenn du stirbst, bleibt dein Körper mit allen Sachen dort unten liegen. Merk dir, wo das Portal ist, und nimm eine Rückkehr-Schriftrolle mit.",
              "",
              "Monster erscheinen überall, wo es dunkel ist. Leuchte deine Gänge gut aus, dann hast du Ruhe.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:torch", 32)],
          deps=["e_enter"], icon="minecraft:skeleton_skull"),

    quest("e_ores", 11, 7, "&6Erz in Massen",
          subtitle="Die Mine ist zum Leerräumen da.",
          description=[
              "Mit &6Ultimine&r räumst du hier ganze Adern auf einmal ab. Eisen brauchst du ständig: für Create-Teile, Eimer, den Kochtopf, Silent Gear und nicht zuletzt für Eisennuggets in der Andesitlegierung.",
              "",
              "&eTipp:&r Bring Kupfer gleich mit. Create macht daraus Kupferbleche und Rohre, und Kupfer steckt auch im Salvaging Table von Apotheosis.",
          ],
          tasks=[task_item("minecraft:raw_iron", 64)],
          rewards=[reward_item("minecraft:coal", 32)],
          deps=["e_enter"], icon="minecraft:raw_iron"),

    quest("e_cobble", 13, 5, "&7Stein für den Obelisken",
          subtitle="Graben für den ganzen Server.",
          description=[
              "Jeder Gang, den du hier gräbst, spuckt Bruchstein aus, und die Stein-Säule am Obelisken will &e40 000&r davon.",
              "",
              "Sammle ihn in einem Rucksack oder einer Truhe am Portal und bring ihn gebündelt zum Spawn. Schleichen und Rechtsklick auf den Obelisken, und alles ist drin.",
          ],
          tasks=[task_item("minecraft:cobblestone", 512)],
          rewards=[reward_table("s1_common")],
          deps=["e_dangers"], icon="minecraft:cobblestone"),

    quest("e_diamonds", 13, 7, "&bDiamanten",
          subtitle="Tief unten wird es glitzern.",
          description=[
              "Diamanten liegen ganz unten, knapp über dem Grundgestein. Du brauchst sie für die Verzauberte Spitzhacke, Obsidian, den Zaubertisch, Silent Gear und einige Zauber-Geräte.",
              "",
              "Ultimine hilft auch hier: Eine ganze Diamantader auf einen Schlag.",
          ],
          tasks=[task_item("minecraft:diamond", 8)],
          rewards=[reward_xp(5)],
          deps=["e_ores"], icon="minecraft:diamond", optional=True),

    # ---- Bauwerke und Beute ---------------------------------------------------
    quest("e_structures", 4.5, 12, "&6Bauwerke",
          subtitle="Überall wartet etwas.",
          description=[
              "Die Welt steckt voller Bauwerke aus mehreren Mods: bessere Verliese, Minenschächte, Festungen, Tempel und Hexenhütten von &6YUNG's&r, riesige Gebäude aus &6When Dungeons Arise&r, neue Dörfer und Türme aus &6Towns and Towers&r, Tavernen aus &6Dungeons and Taverns&r und kleinere Funde aus &6Formations&r und &6Explorify&r.",
              "",
              "Fast überall stehen Kisten mit Beute. Manche Bauwerke sind harmlos, andere werden bewacht. Schau dir einen Ort erst von außen an, bevor du hineinstürmst.",
          ],
          tasks=[task_checkmark("Losgezogen")],
          rewards=[reward_item("minecraft:bread", 16)],
          deps=["welcome"], icon="minecraft:mossy_stone_bricks", size=1.5),

    quest("e_lootr", 7, 11, "&6Beute für alle",
          subtitle="Jede Kiste, für jeden Spieler neu.",
          description=[
              "Dank &6Lootr&r hat jede Kiste in einem Bauwerk für jeden Spieler ihren eigenen Inhalt. Du siehst an der Kiste, ob du sie schon geöffnet hast.",
              "",
              "Deshalb gilt: &cLass die Kisten stehen.&r Wer sie abbaut, nimmt allen, die nach ihm kommen, die Beute weg.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_structures"], icon="minecraft:chest"),

    quest("e_dangerous", 9, 11, "&cGefährliche Orte",
          subtitle="Nicht allein hingehen.",
          description=[
              "Einige Bauwerke sind Arenen für echte Endgegner. &6L_Ender's Cataclysm&r versteckt zum Beispiel &cThe Harbinger&r in einer alten Fabrik, den &cAncient Remnant&r in einer verfluchten Pyramide in der Wüste und &cThe Leviathan&r in einer versunkenen Stadt im Meer.",
              "",
              "Dazu kommen die dunklen Türme und Clownwagen aus &6Born in Chaos&r und die Kreaturen aus &6Mowzie's Mobs&r, etwa der gepanzerte Ferrous Wroughtnaut in seiner Kammer.",
              "",
              "Geht zu mehreren, nehmt Essen, gute Rüstung und eine Rückkehr-Schriftrolle mit. Ein Wegpunkt am Eingang hilft, falls ihr eure Körper einsammeln müsst.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["e_lootr"], icon="minecraft:skeleton_skull"),

    quest("e_artifacts", 7, 13, "&6Artefakte",
          subtitle="Kleine Schätze mit großer Wirkung.",
          description=[
              "In Kisten und bei manchen Gegnern findest du &6Artefakte&r: Schmuck und Kleidung mit einem besonderen Effekt. Die &6Laufschuhe&r machen dich schneller, die &6Wolke in einer Flasche&r schenkt dir einen Doppelsprung, der &6Schnorchel&r lässt dich unter Wasser atmen, die &6Nachtsichtbrille&r macht die Nacht zum Tag.",
              "",
              "Artefakte trägst du in eigenen Plätzen neben der Rüstung. Das Menü dafür öffnest du über den Knopf in deinem Inventar.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_structures"], icon="artifacts:running_shoes"),

    quest("e_mimic", 9, 13, "&cNicht jede Truhe ist eine Truhe",
          subtitle="Manche beißen zurück.",
          description=[
              "Ab und zu ist eine Truhe in Wahrheit ein &cMimic&r. Er sieht harmlos aus, bis du ihn öffnen willst, und dann schlägt er hart zu. Besonders gern wartet er in kleinen Lagern tief in den Höhlen.",
              "",
              "Wer ihn besiegt, bekommt ein Artefakt als Beute.",
          ],
          tasks=[task_kill("artifacts:mimic", 1)],
          rewards=[reward_table("s1_uncommon")],
          deps=["e_artifacts"], icon="artifacts:mimic_spawn_egg", optional=True),

    # ---- Apotheosis -----------------------------------------------------------
    quest("a_affix", 4.5, 18, "&6Beute mit Affixen",
          subtitle="Kein Schwert gleicht dem anderen.",
          description=[
              "Waffen, Werkzeug und Rüstung von Monstern und aus Kisten tragen oft zufällige &6Affixe&r aus Apotheosis: mehr Schaden, Lebensraub, schnelleres Abbauen, zusätzliche Rüstung und vieles mehr.",
              "",
              "Die Farbe des Namens zeigt die Seltenheit: &7Common&r, &aUncommon&r, &9Rare&r, &5Epic&r und &6Mythic&r. Je seltener, desto mehr und desto stärkere Affixe. Apotheosis hat keine deutschen Namen, darum stehen sie hier auf Englisch.",
              "",
              "Manche Monster tragen selbst solche Ausrüstung und sind entsprechend zäh. Ihr Drop lohnt sich aber meistens.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_xp(3)],
          deps=["e_structures"], icon="minecraft:iron_sword", size=1.5),

    quest("a_chronicle", 7, 19, "&6Chronicle of Shadows",
          subtitle="Das Handbuch zu Apotheosis.",
          description=[
              "Ein &6Buch&r und ein &6Goldbarren&r ergeben das &6Chronicle of Shadows&r, das Handbuch zu Apotheosis. Darin stehen alle Affixe, Edelsteine und Tische im Detail.",
              "",
              "Apotheosis kennt außerdem &6Weltstufen&r (World Tiers): Je höher die Stufe, desto stärker die Monster und desto besser die Beute. Das Menü dazu erreichst du über eine eigene Taste, die du in den Steuerungseinstellungen unter Apotheosis findest.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(3)],
          deps=["a_affix"], icon="minecraft:book", optional=True),

    quest("a_gems", 7, 17, "&dEdelsteine und Sockel",
          subtitle="Mach deine Ausrüstung zu deiner eigenen.",
          description=[
              "Manche Ausrüstung hat &6Sockel&r, und manche Monster lassen &dEdelsteine&r fallen. Einen Edelstein setzt du am &6Schmiedetisch&r ein: Gegenstand links, Edelstein rechts. Jeder Edelstein wirkt je nach Gegenstand anders, der Tooltip verrät dir, wie.",
              "",
              "Edelsteine gibt es in sechs Reinheiten, von &7Cracked&r bis &6Perfect&r. Je reiner, desto stärker.",
              "",
              "&cAchtung:&r Einen eingesetzten Edelstein wieder herauszuholen ist teuer. Überleg dir vorher gut, wohin er soll.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("apotheosis:gem_dust", 4)],
          deps=["a_affix"], icon="minecraft:emerald"),

    quest("a_salvage", 9, 17, "&6Salvaging Table",
          subtitle="Aus Beute werden Materialien.",
          description=[
              "Ausrüstung, die du nicht brauchst, zerlegst du im &6Salvaging Table&r. Rezept: drei &6Kupferbarren&r oben, in der Mitte &6Eisenspitzhacke&r, &6Schmiedetisch&r und &6Eisenaxt&r, unten zwei &6Gem Dust&r mit einem &6Lavaeimer&r dazwischen.",
              "",
              "Aus Gegenständen mit Affixen werden &6Seltenheitsmaterialien&r: Common gibt &6Mysterious Scrap Metal&r, Uncommon gibt &6Timeworn Fabric&r, Rare gibt &6Luminous Crystal Shard&r. Edelsteine werden zu &6Gem Dust&r, und normale Eisen- oder Diamantausrüstung gibt einen Teil ihres Materials zurück.",
              "",
              "Die Materialien brauchst du zum Schleifen von Edelsteinen und zum Umschmieden.",
          ],
          tasks=[task_item("apotheosis:salvaging_table", 1)],
          rewards=[reward_table("s1_common"), reward_xp(5)],
          deps=["a_gems"], icon="apotheosis:salvaging_table"),

    quest("a_gem_cutting", 11, 17, "&6Gem Cutting Table",
          subtitle="Reinere Edelsteine.",
          description=[
              "Am &6Gem Cutting Table&r hebst du einen Edelstein auf die nächste Reinheit. Rezept: eine &6Schere&r zwischen zwei &6Glatten Steinen&r, darunter Bretter und ein &6Gem Dust&r in der Mitte.",
              "",
              "Jede Stufe kostet &6Gem Dust&r und Seltenheitsmaterialien, und je höher die Reinheit, desto mehr. Was genau ein Schritt braucht, zeigt dir JEI.",
          ],
          tasks=[task_item("apotheosis:gem_cutting_table", 1)],
          rewards=[reward_item("apotheosis:gem_dust", 4)],
          deps=["a_salvage"], icon="apotheosis:gem_cutting_table", optional=True),

    quest("a_sigil", 11, 19, "&6Sigil of Socketing",
          subtitle="Ein Sockel mehr.",
          description=[
              "Acht &6Tiefenschiefer&r um einen &6Gem Dust&r ergeben acht &6Gem-Fused Slate&r. Daraus, mit weiterem Gem Dust, einem &6Schwarzpulver&r und einer &6Amethystscherbe&r, entstehen drei &6Sigils of Socketing&r.",
              "",
              "Ein Siegel fügt einem Gegenstand am &6Schmiedetisch&r einen Sockel hinzu, bis zu zwei auf diesem Weg. So bekommt auch deine Lieblingswaffe Platz für einen Edelstein.",
          ],
          tasks=[task_item("apotheosis:sigil_of_socketing", 1)],
          rewards=[reward_xp(5)],
          deps=["a_salvage"], icon="apotheosis:sigil_of_socketing"),

    quest("a_reforge", 13, 18, "&6Simple Reforging Table",
          subtitle="Neu würfeln, bis es passt.",
          description=[
              "Am &6Simple Reforging Table&r würfelst du die Affixe eines Gegenstands neu. Rezept: ein &6Eisenbarren&r oben, &6Zaubertisch&r zwischen zwei &6Gem Dust&r, drei &6Glatte Steine&r als Sockel.",
              "",
              "Umschmieden kostet Erfahrung und Seltenheitsmaterialien, bei &9Rare&r zusätzlich zwei &6Sigils of Rebirth&r (Gem-Fused Slate und Gem Dust). Der einfache Tisch schafft Gegenstände bis &9Rare&r.",
          ],
          tasks=[task_item("apotheosis:simple_reforging_table", 1)],
          rewards=[reward_table("s1_uncommon")],
          deps=["a_gem_cutting", "a_sigil"], icon="apotheosis:simple_reforging_table", optional=True),

    # ---- Abschluss ------------------------------------------------------------
    quest("e_explorer", 18.5, 5, "&6Entdecker",
          subtitle="Hin und wieder zurück.",
          description=[
              "Du findest jedes Biom, reist zwischen Wegsteinen, gräbst in einer Welt, die dafür gemacht ist, und weißt, was Beute mit Affixen wert ist.",
              "",
              "Der &cNether&r öffnet sich mit Stufe 2, live auf Stream, durch das Portal am Spawn. Leg dir bis dahin einen Vorrat an Essen, Fackeln und Eisen an. Wer vorbereitet ist, hat am ersten Abend den meisten Spaß.",
          ],
          tasks=[task_checkmark("Ich war unterwegs")],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["e_bounty", "e_own_waystone", "e_cobble", "e_dangerous", "a_salvage"],
          icon="minecraft:compass", size=2.5, shape="gear"),
]

images = [
    banner("exploration/title", "Erkundung", 0, -2.4, height=1.8, kind="title", colour="nature"),
    banner("exploration/orientation", "Orientierung", 9.5, -8.8, height=0.9, colour="nature"),
    banner("exploration/travel", "Reisen", 9, -2.8, height=0.9, colour="magic"),
    banner("exploration/mine", "Minendimension", 9, 3.6, height=0.9, colour="stone"),
    banner("exploration/structures", "Bauwerke und Beute", 7, 9.4, height=0.9, colour="fire"),
    banner("exploration/apotheosis", "Apotheosis", 9, 15.4, height=0.9, colour="brass"),
]

chapter(C, "Erkundung", "minecraft:filled_map", "world", quests, shape="circle", order=7,
        subtitle=["Biome, Wegsteine, die Minendimension, Bauwerke und Beute mit Affixen."],
        images=images)
