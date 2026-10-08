"""EvilCraft in stage 2 (the whole mod opens with stage 2): dark gems, the blood extractor and the
first dark power gem, hardened blood shards and the blood infusion core, the blood infuser, the
undead tree, spiked plates and the sanguinary pedestal as a blood farm, the promises of tenacity
that unlock the higher infuser recipes, the purifier, dark blood bricks and the spirit furnace,
vengeance spirits with ring, focus and box of eternal closure, the dark temple with its
environmental accumulator, and the vein sword and the broom. Garmonbozia and everything made from
it needs chorus fruit from the End and is only mentioned as stage 4."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item,
                  reward_table, reward_xp, banner, img, item_texture)

C = "evilcraft"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Dunkle Edelsteine -----------------------------------------------------
    quest("dark_gem", 0, 0, "&5Grab Dark Gems aus",
          subtitle="Das dunkle Erz, mit dem alles anfängt.",
          description=[
              "&5EvilCraft&r ist Magie mit &4Blut&r: Du zapfst es Monstern ab, lagerst es in Tanks und drückst es in Edelsteine, Maschinen und Werkzeuge. Die ganze Mod öffnet mit &6Stufe 2&r.",
              "",
              "Der Rohstoff ist &6Dark Ore&r. Es liegt überall unterhalb von &eY 66&r, am ehesten dort, wo auch Redstone liegt, und braucht mindestens eine &6Eisenspitzhacke&r. Jedes Erz gibt 4 bis 5 &6Dark Gems&r.",
              "",
              pic("evilcraft:dark_gem"),
              "",
              "&eTipp:&r Nimm &6Glück&r mit. Nur mit Glück fallen zusätzlich &6Crushed Dark Gems&r, und die brauchst du für Ringe, Besen und die Box of Eternal Closure. Es gibt keinen anderen Weg, an das Pulver zu kommen.",
          ],
          tasks=[task_item("evilcraft:dark_gem", 16)],
          rewards=[reward_item("evilcraft:dark_gem", 8), reward_table("s2_common")],
          icon="evilcraft:dark_gem", size=2.0, shape="hexagon"),

    quest("origins", 2.8, -1.2, "&5Hol dir das Buch",
          subtitle="Origins of Darkness, das Handbuch der Mod.",
          description=[
              "Craft einen &6Darkened Apple&r aus einem &6Apfel&r und einem &6Dark Gem&r und füttere ihn an ein Tier. Das Tier stirbt, an der Stelle bleibt eine lila Anomalie. Wirf ein &6Buch&r hinein, und heraus kommt &6Origins of Darkness&r.",
              "",
              "Das Buch erklärt jedes Rezept und jede Maschine der Mod und ist mit JEI verknüpft. Es liegt auch manchmal in Verlieskisten.",
          ],
          tasks=[task_item("evilcraft:origins_of_darkness", 1)],
          rewards=[reward_item("minecraft:apple", 8), reward_xp(3)],
          deps=["dark_gem"], icon="evilcraft:origins_of_darkness"),

    quest("dark_tank", 2.8, 1.2, "&5Bau einen Dark Tank",
          subtitle="16 Eimer in einem Block.",
          description=[
              "Ein &6Dark Gem&r oben und unten, ein &6Glas&r in der Mitte, links und rechts ein &6Dark Metal Ingot&r aus Born in Chaos ergeben einen &6Dark Tank&r. Er fasst &e16 Eimer&r und behält seinen Inhalt, wenn du ihn abbaust.",
              "",
              "Leg mehrere Tanks zusammen in die Werkbank, dann wird daraus ein Tank mit der Summe aller Kapazitäten. Mit Dark Blocks und Eisenblöcken statt Edelsteinen und Barren gibt es gleich einen großen Tank.",
              "",
              "&eHandgriffe:&r Rechtsklick auf den gesetzten Tank schaltet ihn lila, dann füllt er alles unter sich. Shift-Rechtsklick in die Luft mit dem Tank in der Hand schaltet Auto-Supply ein: Er füllt dann jeden passenden Behälter, den du in der Hand hältst.",
          ],
          tasks=[task_item("evilcraft:dark_tank", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["dark_gem"], icon="evilcraft:dark_tank"),

    quest("temple", 5.2, -1.2, "&5Finde einen Dark Temple",
          subtitle="Wetter in Flaschen, Wasser ohne Ende.",
          description=[
              "&6Dark Temples&r stehen in fast jedem Oberwelt-Biom, in der Mitte ein &6Environmental Accumulator&r. Craft einen &6Weather Container&r (Dark Gem, Glasflasche, Zucker in einer Reihe) und wirf ihn auf den Accumulator: Er saugt das aktuelle Wetter in die Flasche und dreht das Wetter dabei um.",
              "",
              "Bei klarem Himmel bekommst du einen &6Clear&r-Container und es fängt an zu regnen, bei Regen einen &6Rain&r-Container, bei Gewitter &6Lightning&r. Zwischen zwei Durchgängen braucht der Tempel 60 Sekunden Pause, und er verdirbt langsam das Biom um sich herum.",
              "",
              "&eLohnt sich:&r Ein Rain-Container mit 7 Glasscheiben und einem Dark Block ergibt 4 &6Eternal Water&r, eine unendliche Wasserquelle als Block. Mit 3 Dark Gems statt der Scheiben werden es 4 &6Buckets of Eternal Water&r. Lightning-Container verstärken die Inverted Potentia für die Mace of Distortion.",
          ],
          tasks=[task_item("evilcraft:weather_container", 1)],
          rewards=[reward_item("evilcraft:bucket_eternal_water", 1), reward_xp(5)],
          deps=["origins"], icon="evilcraft:environmental_accumulator"),

    # ---- Rachegeister ------------------------------------------------------------
    quest("ring", 8.0, 0, "&dBau einen Vengeance Ring",
          subtitle="Mach die Geister sichtbar.",
          description=[
              "Vier &6Crushed Dark Gems&r in die Ecken, vier &6Eisenbarren&r an die Seiten ergeben den &6Vengeance Ring&r. Trägst du ihn im Inventar, siehst du &dVengeance Spirits&r: lila Geister, die manchmal entstehen, wenn ein Monster stirbt.",
              "",
              "Die Geister folgen dir und tun bei Berührung ein wenig Schaden, dann lösen sie sich auf. Shift-Rechtsklick schaltet den Ring scharf: Du bekommst Buffs, aber er lockt und reizt alle Geister im Umkreis von 10 Blöcken. Die meisten davon sind verzerrte Schwärme ohne erkennbares Wesen.",
              "",
              "&eSchutz:&r Ein &6Burning Gem Stone&r (ein Dark Block im Ofen) im Inventar wandelt Geisterschaden in Hunger um. Ein Burning Gem Stone plus ein Dark Stick ergeben 4 &6Gemstone Torches&r, die im Umkreis von 15 Blöcken keinen Geist mehr entstehen lassen.",
          ],
          tasks=[task_item("evilcraft:vengeance_ring", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["dark_gem"], icon="evilcraft:vengeance_ring"),

    quest("focus", 10.4, 0, "&dBau einen Vengeance Focus",
          subtitle="Ein Strahl, der Geister einfriert.",
          description=[
              "Leg den &6Vengeance Ring&r in die Mitte, vier &6Eisenbarren&r an die Seiten und vier &6Crushed Dark Gems&r in die Ecken. Der &6Vengeance Focus&r schießt mit Rechtsklick einen Strahl, der Geister an Ort und Stelle einfriert.",
              "",
              "Eingefrorene Geister kannst du fangen, dazu kommst du im nächsten Schritt.",
          ],
          tasks=[task_item("evilcraft:vengeance_focus", 1)],
          rewards=[reward_item("evilcraft:dark_gem_crushed", 8), reward_xp(5)],
          deps=["ring"], icon="evilcraft:vengeance_focus"),

    quest("box", 12.8, 0, "&dBau eine Box of Eternal Closure",
          subtitle="Ein Gefängnis für einen Geist.",
          description=[
              "Sechs &6Crushed Dark Gems&r oben und unten, zwei &6Tränke der Schwäche&r links und rechts und eine &6Endertruhe&r in der Mitte ergeben die &6Box of Eternal Closure&r. Fertige Boxen mit alten Geistern liegen auch in Verlieskisten, Minenschächten und Festungsbibliotheken.",
              "",
              "&eSo fängst du:&r Stell die leere Box hin, frier einen Geist mit dem Focus ein, der höchstens 10 Blöcke entfernt ist. Die Box zieht ihn zu sich und schließt den Deckel. Der Name des Geists steht danach im Tooltip.",
              "",
              "Welche Geister es gibt, bestimmst du selbst: Töte Zombies, dann entstehen Zombiegeister, töte Blazes im Nether, dann Blazegeister. Jeder Geist hat die Eigenschaften und Drops seines alten Körpers, und genau das nutzt der Spirit Furnace.",
          ],
          tasks=[task_item("evilcraft:box_of_eternal_closure", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["focus"], icon="evilcraft:box_of_eternal_closure"),

    # ---- Blut --------------------------------------------------------------------
    quest("extractor", 0, 5, "&4Bau einen Blood Extractor",
          subtitle="Blut sammeln, Blut setzen.",
          description=[
              "Drei &6Spikes&r oben, ein &6Glas&r in der Mitte, ein &6Dark Gem&r unten ergeben den &6Blood Extractor&r. Spikes sind ein Dark Gem über einem Eisenbarren, das ergibt gleich 16.",
              "",
              "Der Extractor fasst &e5.000 mB&r und füllt sich von selbst, solange er im Inventar liegt und du Monster tötest: pro Lebenspunkt (ein halbes Herz) 5 bis 40 mB, ein Zombie mit 20 Lebenspunkten bringt also 100 bis 800 mB. Stirbt etwas durch einen Sturz, bleibt ein &4Blood Stain&r am Boden, den du mit Shift-Rechtsklick einsaugst.",
              "",
              "Rechtsklick setzt einen Eimer Blut in die Welt. Mehrere Extractors oder Extractor und Dark Tank zusammen in der Werkbank ergeben einen größeren Extractor.",
          ],
          tasks=[task_item("evilcraft:blood_extractor", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["dark_tank"], icon="evilcraft:blood_extractor"),

    quest("power_gem", 2.4, 5, "&4Mach einen Dark Power Gem",
          subtitle="Ein Edelstein, der Blut geschluckt hat.",
          description=[
              "Setz mit dem Extractor &e5 Eimer Blut&r so, dass fünf Quellblöcke nebeneinander stehen. Wirf einen &6Dark Gem&r in die Mitte des Beckens, und er wird zum &6Dark Power Gem&r.",
              "",
              pic("evilcraft:dark_power_gem"),
              "",
              "Das musst du nur einmal von Hand machen. Sobald der Blood Infuser steht, kostet ein Power Gem dort nur noch 250 mB. Power Gems stecken im Infusion Core, in den Promises, im Vein Sword und in der Blood Pearl of Teleportation.",
          ],
          tasks=[task_item("evilcraft:dark_power_gem", 1)],
          rewards=[reward_item("evilcraft:dark_gem", 8), reward_xp(3)],
          deps=["extractor"], icon="evilcraft:dark_power_gem"),

    quest("shards", 4.8, 5, "&4Sammle Hardened Blood Shards",
          subtitle="Getrocknetes Blut, zerschlagen.",
          description=[
              "Blut, das in der Welt steht, trocknet mit der Zeit zu &6Hardened Blood&r. Zerschlag es mit &6Feuerzeug&r, dann fallen &6Hardened Blood Shards&r. Mit Spitzhacke oder Faust wird es nur wieder flüssig.",
              "",
              "Schneller: Bau einen Hardened-Blood-Block mit &6Behutsamkeit&r ab und brenn ihn im Ofen, das gibt gleich &e9 Shards&r. Für den ersten Infusion Core brauchst du 8.",
              "",
              "&eTipp:&r In Verlies-, Dorf- und Festungskisten liegt oft &6Condensed Blood&r. Jedes Stück gibt in einer Blutmaschine einen halben Eimer.",
          ],
          tasks=[task_item("evilcraft:hardened_blood_shard", 8)],
          rewards=[reward_table("s2_common")],
          deps=["power_gem"], icon="evilcraft:hardened_blood_shard"),

    quest("core", 7.2, 5, "&4Bau einen Blood Infusion Core",
          subtitle="Das Herz jeder Blutmaschine.",
          description=[
              "Acht &6Hardened Blood Shards&r um einen &6Dark Power Gem&r ergeben den &6Blood Infusion Core&r. Jede Maschine dieses Kapitels hat einen in der Mitte: Infuser, Purifier, Spirit Furnace, Pedestal-Zubehör und Anhänger.",
              "",
              pic("evilcraft:blood_infusion_core"),
              "",
              "Die einfachste Maschine mit Core ist die &6Blood Chest&r: acht Bretter drumherum. Werkzeuge darin baden in Blut und reparieren sich, 5 mB pro Haltbarkeitspunkt. Ganz selten fangen sie sich dabei einen &cFluch des Zerbrechens&r ein, den der Purifier später wieder entfernt.",
          ],
          tasks=[task_item("evilcraft:blood_infusion_core", 1)],
          rewards=[reward_item("evilcraft:dark_power_gem", 4), reward_xp(5)],
          deps=["shards"], icon="evilcraft:blood_infusion_core", size=1.5, shape="hexagon"),

    quest("infuser", 9.8, 5, "&4&lBau den Blood Infuser",
          subtitle="Blut hinein, etwas Neues heraus.",
          description=[
              "Acht &6Darkstone&r um einen &6Blood Infusion Core&r ergeben den &6Blood Infuser&r. Sein Tank fasst &e10 Eimer&r. Links kommt ein Behälter hinein, der den Tank füllt oder sich daraus füllt, in der Mitte der Gegenstand, rechts das Ergebnis.",
              "",
              "Ohne Upgrades kann er wenig, aber das Wichtige: &6Dark Gem&r plus 250 mB wird in 10 Sekunden zum &6Dark Power Gem&r, ein Dark Block mit 2.250 mB zum Power-Gem-Block, ein &6Toter Busch&r mit 800 mB zum &6Undead Sapling&r. Alles andere braucht Promises, dazu gleich mehr.",
              "",
              "Ein Redstone-Signal hält die Maschine an. Dark Tanks oder Rohre anderer Mods füllen den Tank von allen Seiten.",
          ],
          tasks=[task_item("evilcraft:blood_infuser", 1)],
          rewards=[reward_item("evilcraft:bucket_blood", 4), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["core"], icon="evilcraft:blood_infuser", size=2.0, shape="gear"),

    quest("undead_tree", 12.6, 5, "&4Züchte einen Undead Tree",
          subtitle="Dark Sticks für Werkzeuge und Besen.",
          description=[
              "Leg einen &6Setzling&r mit einer &6Schere&r in die Werkbank, das gibt einen &6Toten Busch&r. Infundiere ihn mit 800 mB zum &6Undead Sapling&r und pflanz ihn. Der Baum wächst wie jeder andere.",
              "",
              "Ein &6Undead Log&r wird zu 4 &6Undead Planks&r. Ein &6Dark Gem&r über zwei Planken ergibt 4 &6Dark Sticks&r, der Stiel für Vein Sword, Kineticator, Besen und Gemstone Torch.",
              "",
              "&eTipp:&r Unter dem Laub eines Undead Tree sammeln sich mit der Zeit kleine Blutflecken. Ein Sanguinary Pedestal daneben trinkt sie von selbst.",
          ],
          tasks=[task_item("evilcraft:dark_stick", 8)],
          rewards=[reward_item("evilcraft:dark_stick", 8), reward_xp(5)],
          deps=["infuser"], icon="evilcraft:dark_stick"),

    # ---- Werkzeug ----------------------------------------------------------------
    quest("vein_sword", 16, 4, "&cSchmiede ein Vein Sword",
          subtitle="Doppelt so viel Blut pro Kill.",
          description=[
              "Zwei &6Dark Power Gems&r übereinander, darunter ein &6Dark Stick&r zwischen zwei &6Spikes&r ergeben das &6Vein Sword&r. Es kommt fertig mit &ePlünderung II&r.",
              "",
              "Tötest du damit, bekommt der Blood Extractor im Inventar &edoppelt so viel Blut&r. Die Haltbarkeit ist mit 32 Schlägen winzig, also leg es zwischendurch in die Blood Chest. Es ist ein Werkzeug zum Blutsammeln, kein Kampfschwert.",
          ],
          tasks=[task_item("evilcraft:vein_sword", 1)],
          rewards=[reward_item("evilcraft:dark_spike", 16), reward_xp(5)],
          deps=["undead_tree"], icon="evilcraft:vein_sword", optional=True),

    quest("broom", 16, 6.2, "&cBau einen Besen",
          subtitle="Fliegen mit Blut im Tank.",
          description=[
              "Ein Besen besteht aus drei Teilen. &6Bare Rod&r: ein Dark Stick oben und unten, in der Mitte Crushed Dark Gem, Dark Stick, Crushed Dark Gem. &6Bare Brush&r: drei Crushed Dark Gems über zwei Dark Sticks. &6Bare Cap&r: Crushed Dark Gem, Dark Gem, Crushed Dark Gem in einer Reihe.",
              "",
              "Veredle jedes Teil mit einem Material, zum Beispiel Rod mit zwei Brettern, Brush mit drei Federn, Cap mit zwei Dark Gems. Der Tooltip zeigt, was das Teil dem Besen gibt. Rod, Brush und Cap zusammen in der Werkbank ergeben den &6Broom&r.",
              "",
              "Füll ihn im Blood Infuser mit Blut, setz dich mit Rechtsklick drauf und flieg. Ohne Blut wird er sehr langsam. Alte Besen liegen auch in Verlieskisten.",
          ],
          tasks=[task_item("evilcraft:broom", 1)],
          rewards=[reward_table("s2_common"), reward_xp(8)],
          deps=["undead_tree"], icon="evilcraft:broom", optional=True),

    # ---- Blutfarm ----------------------------------------------------------------
    quest("spiked_plate", 0, 10, "&4Bau eine Spiked Plate",
          subtitle="Eine Druckplatte, die zubeißt.",
          description=[
              "Drei &6Spikes&r über einer &6schweren Druckplatte&r ergeben die &6Spiked Plate&r. Jedes Monster, das darüber läuft, bekommt &e4 Schaden&r pro Treffer, Spieler nicht. Die Drops zählen wie bei einem Spieler-Kill, also mit allem, was sonst nur von Hand fällt.",
              "",
              "Solange sie beißt, gibt die Platte ein Redstone-Signal ab. Eine Reihe davon am Ende einer Mobfalle ersetzt den Spieler mit dem Schwert.",
          ],
          tasks=[task_item("evilcraft:spiked_plate", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["extractor"], icon="evilcraft:spiked_plate"),

    quest("pedestal", 2.4, 10, "&4Bau ein Sanguinary Pedestal",
          subtitle="Blut sammeln ohne Hand anzulegen.",
          description=[
              "Drei &6Dark Gems&r oben, ein &6Dark Block&r in der Mitte, drei &6Dark Gems&r unten ergeben das &6Sanguinary Pedestal&r. Es saugt alle Blood Stains im Umkreis von 2 Blöcken ein, fasst 10 Eimer und drückt 100 mB pro Tick in jeden Tank daneben.",
              "",
              "Setz eine &6Spiked Plate&r obendrauf: Jedes Monster, das die Platte tötet, gibt sein Blut direkt ins Pedestal, 40 mB pro Lebenspunkt. Ein Zombie bringt so 800 mB, ohne dass du dabei bist.",
              "",
              "Das &6Powered Sanguinary Pedestal&r (fünf Dark Power Gems, ein Power-Gem-Block, das alte Pedestal) reicht 4 Blöcke weit und holt anderthalbmal so viel aus jedem Fleck.",
              "",
              "&eKronwerke:&r Die Promises weiter unten verlangen 10, 40 und 160 Eimer Blut. Bau diese Farm, bevor du dort anfängst.",
          ],
          tasks=[task_item("evilcraft:sanguinary_pedestal_0", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(8)],
          deps=["spiked_plate", "power_gem"], icon="evilcraft:sanguinary_pedestal_0", size=1.5, shape="hexagon"),

    # ---- Versprechen -------------------------------------------------------------
    quest("tier1", 9.8, 10, "&6Mach eine Promise of Tenacity I",
          subtitle="Der Infuser hält, was er verspricht.",
          description=[
              "Drei &6Dark Power Gems&r in einem V ergeben eine &6Bowl of Empty Promises&r. Mit zwei &6Crushed Dark Gems&r wird sie zur &6Dusted&r-Schale, und 5 Eimer Blut im Infuser machen daraus eine &6Bowl of Promises&r.",
              "",
              "Dazu ein &6Promise Acceptor&r: ein &6Eisenblock&r mit 10 Eimern im Infuser. Schale, Acceptor und ein &6Spinnenauge&r in der Werkbank ergeben die &6Promise of Tenacity I&r. Steck sie in einen Upgrade-Slot des Infusers.",
              "",
              "&eWas das bringt:&r Der Tank verdoppelt sich und Stufe-1-Rezepte öffnen: Buch wird zum &6Blook&r, Fauliges Fleisch zu Leder, Kohle zu &6Blood Waxed Coal&r, eine &6Potentia Sphere&r (Redstone, Glowstone, Schleimball, Lapis) für 2 Eimer zur &6Enderperle&r.",
              "",
              "Hat der Infuser erst Stufe 1, gibt es auf demselben Weg mit einem Redstone-Block statt dem Spinnenauge die &6Promise of Velocity&r (schneller), mit einem Lapisblock die &6Promise of Productivity&r (weniger Blut).",
              "",
              "&eKronwerke:&r Für die Manaperlen im Stufenziel braucht Botania Enderperlen. Zwei Eimer Blut pro Perle sind oft billiger als eine Nacht Endermen jagen.",
          ],
          tasks=[task_item("evilcraft:promise_tier_1", 1)],
          rewards=[reward_table("s2_common"), reward_item("evilcraft:dark_power_gem", 8), reward_xp(8)],
          deps=["infuser"], icon="evilcraft:promise_tier_1"),

    quest("tier2", 12.2, 10, "&6Mach eine Promise of Tenacity II",
          subtitle="40 Eimer Blut für einen Goldblock.",
          description=[
              "Eine &6Bowl of Promises&r aus dem Stufe-1-Infuser, ein &6Goldblock&r mit &e40 Eimern&r Blut im Infuser und eine &6Enderperle&r ergeben die &6Promise of Tenacity II&r.",
              "",
              "Stufe 2 öffnet die Rezepte für den Spirit Furnace: &6Dark Brick&r plus 1 Eimer wird zum &6Dark Blood Brick&r, &6Undead Planks&r plus 1 Eimer zu &6Reinforced Undead Planks&r für die Colossal Blood Chest. Dazu Fauliges Fleisch zu 8 Spinnenaugen, Bruchstein zu Netherrack und &6Dull Dust&r (Zucker und Schießpulver) zu Redstone.",
          ],
          tasks=[task_item("evilcraft:promise_tier_2", 1)],
          rewards=[reward_table("s2_uncommon"), reward_item("minecraft:gold_ingot", 8), reward_xp(10)],
          deps=["tier1"], icon="evilcraft:promise_tier_2"),

    quest("tier3", 14.6, 10, "&6Mach eine Promise of Tenacity III",
          subtitle="160 Eimer Blut für einen Diamantblock.",
          description=[
              "Eine &6Bowl of Promises&r aus dem Stufe-2-Infuser, ein &6Diamantblock&r mit &e160 Eimern&r Blut und ein &6Enderauge&r ergeben die &6Promise of Tenacity III&r. Das ist die höchste Stufe.",
              "",
              "Stufe 3 macht aus einem &6Knochen&r für 2,5 Eimer eine &6Lohenrute&r, aus Sand Seelensand, aus Weizensamen Netherwarzen und aus einer &6Ghastträne&r für 10 Eimer eine &6Corrupted Tear&r. Die Träne mit 6 Gold und 2 Dark Gems ergibt zwei &6Entangled Chalices&r, die überall denselben Inhalt haben.",
              "",
              "&eKronwerke:&r Lohenruten aus Knochen heißt Lohenstaub für Messing, ohne in den Nether zu müssen. &cAusblick:&r &6Garmonbozia&r braucht Essenz getöteter Geister, und der Focus dafür braucht Chorusfrucht aus dem End. Das kommt in &6Stufe 4&r.",
          ],
          tasks=[task_item("evilcraft:promise_tier_3", 1)],
          rewards=[reward_table("s2_uncommon"), reward_item("minecraft:diamond", 4), reward_xp(15)],
          deps=["tier2"], icon="evilcraft:promise_tier_3", optional=True),

    # ---- Blutmaschinen -----------------------------------------------------------
    quest("purifier", 9.8, 15, "&4Bau einen Purifier",
          subtitle="Flüche weg, Verzauberungen ins Buch.",
          description=[
              "Zwei &6Hardened Blood Shards&r in die oberen Ecken, ein &6Blood Infusion Core&r in die Mitte, ein &6Dark Block&r darunter, links und rechts vom Core und in die unteren Ecken je ein &6Dark Gem&r ergeben den &6Purifier&r. Die obere Mitte bleibt leer. Er fasst 3 Eimer Blut.",
              "",
              "&eDrei Handgriffe:&r Verfluchtes Werkzeug plus 1 Eimer entfernt den Fluch. Verzauberter Gegenstand plus &6Blook&r bei vollem Becken zieht eine zufällige Verzauberung ins Buch, für 3 Eimer. Leere Flasche bei vollem Becken nimmt einem Wesen, das im Purifier steht, einen Trankeffekt ab.",
              "",
              "Außerdem macht er Monsterköpfe wieder rückgängig, die der Infuser weiterverwandelt hat (Skelettschädel zu Zombiekopf zu Creeperkopf zu Witherskelettschädel).",
          ],
          tasks=[task_item("evilcraft:purifier", 1), task_item("evilcraft:blook", 1)],
          rewards=[reward_item("minecraft:book", 8), reward_xp(8)],
          deps=["tier1"], icon="evilcraft:purifier", section="maschinen"),

    quest("bricks", 12.2, 15, "&4Infundiere Dark Blood Bricks",
          subtitle="Die Wände, aus denen kein Geist entkommt.",
          description=[
              "Vier &6Steinziegel&r um einen &6Dark Block&r ergeben 4 &6Dark Bricks&r. Jeder Brick mit &e1 Eimer Blut&r im Infuser (Stufe 2) wird zum &6Dark Blood Brick&r.",
              "",
              "Der Spirit Furnace für einen Zombie ist ein hohler Kasten von 3 mal 3 Blöcken Grundfläche und 4 Blöcken Höhe, innen 1 mal 1 mal 2 frei. Das sind 34 Blöcke, einer davon der Furnace selbst, also &e33 Dark Blood Bricks&r und 33 Eimer Blut.",
          ],
          tasks=[task_item("evilcraft:dark_blood_brick", 32)],
          rewards=[reward_item("evilcraft:dark_blood_brick", 4), reward_xp(8)],
          deps=["tier2"], icon="evilcraft:dark_blood_brick"),

    quest("spirit_furnace", 14.6, 15, "&4&lBau den Spirit Furnace",
          subtitle="Geister wiederbeleben und sofort kochen.",
          description=[
              "Vier &6Dark Blood Bricks&r um einen &6Blood Infusion Core&r ergeben den &6Spirit Furnace&r. Setz ihn irgendwo in die Wand des Brick-Kastens. Stimmt der Aufbau, glüht der Kasten rot.",
              "",
              "Leg eine volle &6Box of Eternal Closure&r in den Box-Slot und gib Blut in den Tank (10 Eimer). Der Furnace belebt den Geist im Inneren und kocht ihn sofort: &e25 mB pro Tick&r, 10 Ticks pro Lebenspunkt. Ein Zombie dauert 10 Sekunden und kostet 5 Eimer, die Drops landen im Inventar des Furnace. Die Box bleibt voll und wird nie leer.",
              "",
              "Große Mobs brauchen einen größeren Kasten, bis zu 9 mal 9. Ein Dorfbewohner gibt mit 20 Prozent einen Smaragd. Trichter oder Rohre holen die Drops aus jeder Seite.",
          ],
          tasks=[task_item("evilcraft:spirit_furnace", 1)],
          rewards=[reward_table("s2_uncommon"), reward_item("evilcraft:bucket_blood", 8), reward_xp(12)],
          deps=["bricks"], icon="evilcraft:spirit_furnace", size=2.0, shape="hexagon"),

    quest("cook", 17.6, 15, "&5&lKoch den ersten Geist",
          subtitle="Eine Mobfarm, die nie Nachschub braucht.",
          description=[
              "Jetzt alles zusammen: Töte ein Monster, dessen Drops du willst, frier den Geist mit dem &6Vengeance Focus&r ein und lass ihn von einer &6Box of Eternal Closure&r schlucken. Box in den &6Spirit Furnace&r, Blut aus dem &6Sanguinary Pedestal&r dazu, fertig.",
              "",
              "&eWas sich lohnt:&r Ein &6Blaze&r-Geist liefert Lohenruten und damit Lohenstaub für jedes Messing im Stufenziel. Ein &6Enderman&r-Geist liefert Enderperlen für die Manaperlen. Ein &6Witherskelett&r-Geist lässt ab und zu einen Schädel fallen, ohne dass jemand durch die Festung rennt.",
              "",
              "&eKronwerke:&r Beide Ziele der Stufe 2, Messing und Manaperlen, hängen an Lohenstaub und Enderperlen. Eine Geisterküche mit zwei Boxen versorgt die Technik- und die Magieseite gleichzeitig.",
          ],
          tasks=[task_advancement("evilcraft:closure", "Einen Rachegeist in einer Box of Eternal Closure fangen"),
                 task_checkmark("Der erste Geist ist gekocht")],
          rewards=[reward_table("s2_rare"), reward_item("evilcraft:dark_power_gem", 16), reward_xp(20)],
          deps=["spirit_furnace", "box"], icon="evilcraft:box_of_eternal_closure", size=2.5, shape="gear"),

    # ---- Neue Quests -------------------------------------------------------------
    quest("exalted_crafter", 5.2, 1.2, "&5Bau einen Exalted Crafter",
          subtitle="Die Werkbank für die Hosentasche.",
          description=[
              "Oben Gold, &6Werkbank&r, Gold. In der Mitte Crushed Dark Gem, &6Endertruhe&r, Crushed Dark Gem. Unten Gold, Eisen, Gold.",
              "",
              "Rechtsklick öffnet ein Crafting-Feld, wo immer du bist, dazu den Inhalt deiner &6Endertruhe&r. Mit einer normalen &6Truhe&r statt der Endertruhe bekommst du den &6Wooden Exalted Crafter&r mit eigenem Inventar. Er lässt sich auch auf eine Taste legen.",
              "",
              "&eTipp:&r Schlägt ein Blitz in den Crafter ein, wird er unzerstörbar und verschwindet nicht mehr, wenn er am Boden liegt.",
          ],
          tasks=[task_item("evilcraft:exalted_crafter", 1)],
          rewards=[reward_item("evilcraft:dark_gem_crushed", 4), reward_xp(4)],
          deps=["origins"], icon="evilcraft:exalted_crafter", optional=True),

    quest("blood_pearl", 2.4, 6.8, "&4Bau eine Blood Pearl of Teleportation",
          subtitle="Eine Enderperle, die zurückkommt.",
          description=[
              "&e5 Enderperlen&r in die Ecken und die Mitte, &e4 Dark Power Gems&r an die Seiten.",
              "",
              "Die Perle hat einen eigenen Bluttank, den du im linken Platz des Blood Infuser füllst. Dann wirfst du sie wie eine Enderperle, nur dass sie nicht verbraucht wird. Jeder Wurf kostet etwas Blut.",
          ],
          tasks=[task_item("evilcraft:blood_pearl_of_teleportation", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 4), reward_xp(5)],
          deps=["power_gem"], icon="evilcraft:blood_pearl_of_teleportation", optional=True),

    quest("blood_chest", 7.2, 6.8, "&4Bau eine Blood Chest",
          subtitle="Werkzeuge baden in Blut.",
          description=[
              "&e8 Bretter&r um einen &6Blood Infusion Core&r.",
              "",
              "Leg beschädigte Werkzeuge hinein und füll den Tank mit Blut. Sie reparieren sich langsam, &e5 mB&r pro Haltbarkeitspunkt. Ganz selten fangen sie sich dabei einen &cFluch des Zerbrechens&r ein, den der Purifier wieder entfernt.",
              "",
              "Gut für das Vein Sword mit seinen 32 Schlägen.",
          ],
          tasks=[task_item("evilcraft:blood_chest", 1)],
          rewards=[reward_item("evilcraft:bucket_blood", 2), reward_xp(4)],
          deps=["core"], icon="evilcraft:blood_chest"),

    quest("pendant", 9.8, 6.8, "&4Knüpf ein Invigorating Pendant",
          subtitle="Schlechte Effekte weg, gegen Blut.",
          description=[
              "&6Golden String&r: Faden und Goldnugget, formlos. Dann &e3 Golden Strings&r als Bogen oben, darunter Crushed Dark Gem, &6Blood Infusion Core&r, Crushed Dark Gem.",
              "",
              "Im Inventar entfernt der Anhänger jeden schlechten Trankeffekt und kostet dafür Blut aus seinem Tank, schlimmere Effekte mehr. Er löscht sogar Feuer an dir, schwimm aber trotzdem nicht in Lava.",
          ],
          tasks=[task_item("evilcraft:invigorating_pendant", 1)],
          rewards=[reward_item("minecraft:gold_nugget", 9), reward_xp(5)],
          deps=["core"], icon="evilcraft:invigorating_pendant", optional=True),

    quest("vengeance_pickaxe", 18.4, 4, "&cSchmiede eine Vengeance Pickaxe",
          subtitle="Glück V, frisch aus der Werkbank.",
          description=[
              "Oben Hardened Blood Shard, &6Diamant&r, Hardened Blood Shard. In der Mitte Diamant, &6Dark Stick&r, Diamant. Unten ein Dark Stick.",
              "",
              "Sie kommt fertig mit &eGlück V&r und &eVengeance III&r. Dafür hält sie nicht lange, und beim Abbauen können Vengeance Spirits entstehen. Heb sie für Diamanten, Smaragde und andere Glückserze auf, und repariere sie in der Blood Chest.",
          ],
          tasks=[task_item("evilcraft:vengeance_pickaxe", 1)],
          rewards=[reward_item("minecraft:diamond", 2), reward_table("s2_common"), reward_xp(8)],
          deps=["undead_tree", "shards"], icon="evilcraft:vengeance_pickaxe"),

    quest("kineticator", 18.4, 6.2, "&cBau einen Kineticator",
          subtitle="Ein Magnet für Items und Erfahrung.",
          description=[
              "&6Blood Orb&r: &e4 Glas&r um einen Eisenbarren, dann im Infuser (Stufe 1) mit &e10 Eimern&r Blut füllen.",
              "Kineticator: oben rechts Blood Infusion Core und Dark Stick, Mitte Gold, Blood Orb, Gold, unten Dark Stick und &6Diamant&r.",
              "",
              "Schleichend Rechtsklick schaltet ihn an, Rechtsklick ändert den Radius. Er zieht Items und Erfahrungskugeln zu dir, nahe kosten fast kein Blut, ferne etwas mehr. Umgekehrt gecraftet stößt er sie ab.",
          ],
          tasks=[task_item("evilcraft:kineticator", 1)],
          rewards=[reward_item("evilcraft:dark_stick", 4), reward_xp(8)],
          deps=["undead_tree", "tier1"], icon="evilcraft:kineticator", optional=True),

    quest("mace", 20.8, 4, "&cSchwing die Mace of Distortion",
          subtitle="Eine Druckwelle aus Blut.",
          description=[
              "&6Inverted Potentia&r: &e4 Dark Gems&r um eine &6Potentia Sphere&r. Wirf sie bei &eGewitter&r auf den Environmental Accumulator eines Dark Temple, dann wird sie zur &6Empowered Inverted Potentia&r.",
              "Mace: zwei Dark Power Gems, die Empowered Potentia oben rechts, zwei Dark Sticks als Stiel.",
              "",
              "Rechtsklick halten baut eine Kugel auf, loslassen stößt alle Wesen darin weg und verletzt sie, solange Blut im Tank ist. Schleichend Rechtsklick wählt die Stärke, höhere kosten mehr Blut.",
          ],
          tasks=[task_item("evilcraft:mace_of_distortion", 1)],
          rewards=[reward_item("evilcraft:dark_power_gem", 4), reward_xp(8)],
          deps=["undead_tree", "temple"], icon="evilcraft:mace_of_distortion", optional=True),

    quest("necromancer_staff", 20.8, 6.2, "&cBau einen Necromancer Staff",
          subtitle="Zombies, die für dich kämpfen.",
          description=[
              "Oben Dark Power Gem, ein beliebiger &6Kopf&r oder Schädel, Dark Power Gem. Mitte Spike, &6Empowered Inverted Potentia&r, Spike. Unten ein Dark Stick.",
              "",
              "Der Stab ruft eine Gruppe Zombies, die für eine Weile das Wesen angreifen, das du ins Visier nimmst. Praktisch gegen Gruppen und als Ablenkung im Bosskampf.",
          ],
          tasks=[task_item("evilcraft:necromancer_staff", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 16), reward_xp(8)],
          deps=["mace"], icon="evilcraft:necromancer_staff", optional=True),

    quest("effortless_ring", 9.8, 11.8, "&6Schmied einen Effortless Ring",
          subtitle="Schneller laufen, höher springen.",
          description=[
              "Oben links eine &6Promise of Velocity&r, daneben Gold. Mitte Eisen, &6Promise of Productivity&r, Eisen. Unten Gold.",
              "",
              "Liegt der Ring irgendwo im Inventar, läufst du schneller, springst höher und steigst ganze Blöcke hoch. Schleichend unterdrückst du die Stufenhilfe.",
          ],
          tasks=[task_item("evilcraft:effortless_ring", 1)],
          rewards=[reward_item("minecraft:sugar", 16), reward_xp(6)],
          deps=["tier1"], icon="evilcraft:effortless_ring", optional=True),

    quest("colossal_chest", 12.2, 16.8, "&4Bau die Colossal Blood Chest",
          subtitle="Reparieren im großen Stil.",
          description=[
              "&6Reinforced Undead Planks&r: Undead Planks mit &e1 Eimer&r Blut im Infuser (Stufe 2). Die Truhe selbst: &e4&r davon um einen &6Blood Infusion Core&r.",
              "",
              "Bau einen hohlen Würfel von 3 mal 3 mal 3 aus Reinforced Undead Planks und setz die Colossal Blood Chest an eine Stelle in der Wand. Das sind &e25 Planken&r plus die Truhe.",
              "",
              "Sie fasst viel mehr, ist schneller, nimmt &6Promises&r an und fängt sich keine Flüche ein. Je mehr Items gleichzeitig darin liegen, desto sparsamer geht sie mit Blut um.",
          ],
          tasks=[task_item("evilcraft:colossal_blood_chest", 1)],
          rewards=[reward_item("evilcraft:bucket_blood", 4), reward_table("s2_uncommon"), reward_xp(10)],
          deps=["tier2", "undead_tree", "blood_chest"], icon="evilcraft:colossal_blood_chest", optional=True),

    quest("reanimator", 14.6, 16.8, "&5Bau einen Spirit Reanimator",
          subtitle="Aus Geistern werden Spawn-Eier.",
          description=[
              "Bruchstein rundherum, oben ein Eisenbarren, in der Mitte ein &6Blood Infusion Core&r, unten ein &6Eisenblock&r.",
              "",
              "Leg eine volle &6Box of Eternal Closure&r, ein &6Ei&r und Blut hinein. Der Reanimator steckt den Geist in das Ei, heraus kommt ein &6Spawn-Ei&r seines Mobs. Der Geist ist danach verbraucht, also nur ein Ei pro Geist.",
              "",
              "Manche Mobs weigern sich, ins Ei zu gehen. Deren Geister sind verloren.",
          ],
          tasks=[task_item("evilcraft:spirit_reanimator", 1)],
          rewards=[reward_item("minecraft:egg", 16), reward_xp(8)],
          deps=["box", "core"], icon="evilcraft:spirit_reanimator", optional=True),
]

images = [
    banner("evilcraft/title", "EvilCraft", 8.0, -5.0, height=1.8, kind="title", colour="magic"),
    banner("evilcraft/edelsteine", "Dunkle Edelsteine", 2.8, -3.0, height=0.9, colour="magic"),
    banner("evilcraft/geister", "Rachegeister", 10.4, -3.0, height=0.9, colour="end"),
    banner("evilcraft/blut", "Blut", 6.0, 3.0, height=0.9, colour="fire"),
    banner("evilcraft/werkzeug", "Werkzeug", 16.0, 2.2, height=0.9, colour="stone"),
    banner("evilcraft/blutfarm", "Blutfarm", 1.2, 8.0, height=0.9, colour="fire"),
    banner("evilcraft/versprechen", "Versprechen", 12.2, 8.0, height=0.9, colour="brass"),
    banner("evilcraft/maschinen", "Blutmaschinen", 12.2, 13.0, height=0.9, colour="fire"),
]

chapter(C, "EvilCraft", "evilcraft:blood_infuser", "magic", quests, shape="circle", order=50, stage=2,
        subtitle=["Stufe 2. Dunkle Edelsteine, Blut, der Infuser und die Geisterküche."], images=images)
