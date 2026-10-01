"""Botania in stage 4: the Ritual of Gaia (gaia pylons, an active beacon, a terrasteel ingot,
the arena rules from the Lexica and GaiaGuardianEntity: 320 HP, damage cap 32, arena radius 12),
fighting the Gaia Guardian alone or together, Gaia spirits (6 per fighter, 8 for the killing blow,
loot_table/gaia_guardian/reward.json), the things made from them (gaia spreader, Flugel tiara,
dandelifeon, shulk me not, the Gaia baubles as a checklist, talisman, astrolabe, starcaller,
thundercaller) and the stage 4 magic goal of 128 Gaia spirits. Continues alfheim.py. The Gaia
spirit ingot, Gaia II and the relics are stage 5 and text only."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item,
                  reward_table, reward_xp, banner, img, item_texture)

C = "gaia"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Vorbereitung ---------------------------------------------------------
    quest("pylon", 0, 0, "&dBau vier Gaiapylonen",
          subtitle="Der Altar für das Ritual der Elfen.",
          description=[
              "Ein &aManapylon&r in der Mitte, &dElementiumbarren&r links und rechts, &dFeenstaub&r oben und unten. Du brauchst &e4&r davon.",
              "",
              pic("botania:gaia_spirit"),
              "",
              "Mit &6Stufe 4 (Sternwerk)&r öffnet das &dRitual von Gaia&r. Am Ende steht der &dWächter von Gaia&r, und seine &dGaia-Seelen&r öffnen die stärksten Dinge von Botania.",
              "",
              "&eKommt in Stufe 5:&r Gaia-Seelenbarren, Ritual von Gaia II, Relikte der Asen.",
          ],
          tasks=[task_item("botania:gaia_pylon", 4)],
          rewards=[reward_item("botania:pixie_dust", 4), reward_table("s4_common"), reward_xp(10)],
          icon="botania:gaia_pylon", size=2.0, shape="hexagon"),

    quest("beacon", 2.75, -1.25, "&bStell einen aktiven Beacon auf",
          subtitle="Der Beacon wird zum Altar.",
          description=[
              "Ein &bBeacon&r auf einer fertigen Pyramide, mindestens 3x3 aus Eisen, Gold, Smaragd, Diamant oder Netherit. Er muss leuchten.",
              "",
              "Den Netherstern gibt der &5Wither&r, siehe Kapitel &aBosse&r. Den Effekt schaltet der Wächter während des Kampfes ab.",
          ],
          tasks=[task_item("minecraft:beacon", 1)],
          rewards=[reward_item("minecraft:iron_block", 9)],
          deps=["pylon"], icon="minecraft:beacon"),

    quest("terrasteel", 2.75, 1.25, "&aLeg Terrastahl als Opfer bereit",
          subtitle="Ein Barren pro Kampf.",
          description=[
              "Jedes Ritual kostet einen &aTerrastahlbarren&r, der Beacon verbraucht ihn.",
              "",
              pic("botania:terrasteel_ingot"),
              "",
              "Lass die Terraplatte aus Stufe 2 weiterlaufen. Sechzehn Kämpfe für den Obelisken sind sechzehn Barren.",
          ],
          tasks=[task_item("botania:terrasteel_ingot", 4)],
          rewards=[reward_item("botania:mana_pearl", 4)],
          deps=["pylon"], icon="botania:terrasteel_ingot"),

    quest("arena", 5.25, 0, "&dBau die Arena",
          subtitle="Ein freier Platz, sonst nimmt der Beacon nichts an.",
          description=[
              "Je ein Gaiapylon &e4 Blöcke diagonal&r vom Beacon und &e1 Block höher&r, in alle vier Richtungen. Rundherum eine freie, ebene Fläche mit &e12 Blöcken Radius&r, ohne Blöcke im Weg und ohne Löcher.",
              "",
              "&eStarten:&r Schleich-Rechtsklick mit dem Terrastahlbarren auf den Beacon, einen Schritt zurück. Das muss ein echter Spieler tun, kein Einsatzgerät.",
              "",
              "&eTipp:&r Bau eine feste Arena für den ganzen Server und lass sie stehen.",
          ],
          tasks=[task_checkmark("Die Arena steht")],
          rewards=[reward_xp(5)],
          deps=["beacon", "terrasteel"], icon="minecraft:beacon"),

    quest("gear", 5.25, 2.5, "&aRüste dich aus",
          subtitle="Er ist schwerer als der Wither.",
          description=[
              "Die Lexica rät zu verzauberter &dElementiumrüstung&r und einer &aTerraklinge&r, dazu Gebräue und Schmuck.",
              "",
              "Goldene Äpfel, Heiltränke, Stärke und Widerstand aus der Brauerei helfen. Der Wächter nimmt pro Treffer höchstens &e32 Schaden&r, viele schnelle Treffer schlagen einen großen.",
          ],
          tasks=[task_item("botania:terra_blade", 1), task_item("botania:elementium_chestplate", 1)],
          rewards=[reward_item("minecraft:golden_apple", 4), reward_xp(5)],
          deps=["arena"], icon="botania:terra_blade"),

    # ---- Der Kampf ------------------------------------------------------------
    quest("behaviour", 7.75, -2.5, "&5Lern, was er tut",
          subtitle="Bleib weg vom Lila.",
          description=[
              "Allein hat er &e320 Lebenspunkte&r, jeder weitere Spieler bringt ein Viertel dazu: zu zweit 480, zu viert 640.",
              "",
              "Er &eteleportiert&r sich durch die Arena, schießt &dlila Geschosse&r, legt &dlila Fallen&r auf den Boden und ruft &eWellen von Monstern&r. Wer die Arena verlässt, wird zurückgeholt.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["arena"], icon="botania:gaia_head"),

    quest("fight", 7.75, 0, "&d&lBesiege den Wächter von Gaia",
          subtitle="Der erste Kampf.",
          description=[
              "Starte das Ritual und gewinne. &eJeder Mitkämpfer bekommt 6&r Gaia-Seelen, &ewer den letzten Treffer setzt, 8&r. Mit 20 Prozent fällt eine Schallplatte dazu.",
              "",
              pic("botania:gaia_spirit"),
          ],
          tasks=[task_item("botania:gaia_spirit", 6)],
          rewards=[reward_item("botania:terrasteel_ingot", 2), reward_table("s4_uncommon"), reward_xp(15)],
          deps=["gear", "behaviour"], icon="botania:gaia_spirit", size=2.0, shape="gear"),

    quest("no_armor", 7.75, 2.5, "&5Gewinn ohne Rüstung",
          subtitle="Mythologia's End, nur für Wahnsinnige.",
          description=[
              "Besiege den Wächter ohne ein einziges Rüstungsteil. Das gibt den Fortschritt &eMythologia's End&r.",
              "",
              "Kein Vorteil, nur Ehre. Mach es live, sonst glaubt es dir niemand.",
          ],
          tasks=[task_advancement("botania:challenge/gaia_guardian_no_armor", "Den Wächter ohne Rüstung besiegen")],
          rewards=[reward_item("minecraft:enchanted_golden_apple", 1), reward_xp(20)],
          deps=["fight"], optional=True, icon="botania:gaia_head"),

    quest("together", 10.25, -2.5, "&dKämpf gemeinsam",
          subtitle="Mehr Leute, mehr Seelen.",
          description=[
              "Das Ritual zählt die Spieler beim Start. Zu viert hat er doppelt so viel Leben, aber es fallen 6 für jeden und 8 für den letzten Treffer, zusammen &e26 statt 8&r.",
              "",
              "Mehr als fünf rät die Lexica ab, dann wird es zu chaotisch.",
              "",
              "&eKronwerke:&r Die Kämpfe für den Obelisken laufen live auf Stream. Arena fertig bauen, Terrastahl mitbringen.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["fight"], icon="botania:gaia_spirit"),

    quest("head", 10.25, 2.5, "&5Hol dir seinen Kopf",
          subtitle="Eine Trophäe, nur mit der Elementiumaxt.",
          description=[
              "Letzter Treffer mit einer &dElementiumaxt&r: etwa &e7,7 Prozent&r Chance auf den Kopf, mit Plünderung I 15,4 Prozent, jede weitere Stufe 7,7 mehr.",
              "",
              "Nutzlos, aber an der Wand sieht jeder, dass du dabei warst.",
          ],
          tasks=[task_item("botania:gaia_head", 1)],
          rewards=[reward_xp(10)],
          deps=["fight"], icon="botania:gaia_head", optional=True),

    quest("spirits", 10.25, 0, "&dSammle Gaia-Seelen",
          subtitle="Die Währung dieser Stufe.",
          description=[
              "Sammle &e24 Gaia-Seelen&r. Fast alles hier kostet eine oder mehrere.",
              "",
              "&eRezept auf Kronwerke:&r Jeder &cStabilisator&r für den Energiekern von Draconic Evolution braucht eine Gaia-Seele, ein Kern vier. Siehe Kapitel &5Draconic Evolution&r.",
          ],
          tasks=[task_item("botania:gaia_spirit", 24)],
          rewards=[reward_item("botania:terrasteel_ingot", 4), reward_table("s4_common")],
          deps=["fight"], icon="botania:gaia_spirit"),

    # ---- Aus Gaia-Seelen -------------------------------------------------------
    quest("spreader", 12.75, -2.5, "&dBau einen Gaia-Manaverbreiter",
          subtitle="Der beste Verbreiter der Mod.",
          description=[
              "&6Elfen-Manaverbreiter&r, &dDrachenstein&r und &dGaia-Seele&r, formlos.",
              "",
              "Größere Stöße, weiter, mit weniger Verlust, dafür seltener. An der stärksten Blume oder auf langen Strecken.",
          ],
          tasks=[task_item("botania:gaia_mana_spreader", 1)],
          rewards=[reward_item("botania:dragonstone", 2)],
          deps=["spirits"], icon="botania:gaia_mana_spreader"),

    quest("tiara", 12.75, 0, "&b&lCrafte die Flügel-Tiara",
          subtitle="Fliegen mit Mana.",
          description=[
              "Oben drei &dGaia-Seelen&r, Mitte Elementium, Gaia-Seele, Elementium, unten Feder, &5Reine Ender-Essenz&r, Feder.",
              "",
              pic("botania:flugel_tiara"),
              "",
              "Im Kopfplatz fliegst du mit Mana, etwa &e30 Sekunden&r am Stück. Sprinttaste ohne Sprint gibt einen Stoß (alle 2 s), Schleichen im Fall lässt dich gleiten, ohne Fallschaden.",
              "",
              "&eReine Ender-Essenz:&r Im End gibt der Seelendolch an Endermen die reine Form, siehe &aBotania: Alfheim&r.",
          ],
          tasks=[task_item("botania:flugel_tiara", 1)],
          rewards=[reward_item("botania:mana_pearl", 4), reward_table("s4_uncommon"), reward_xp(10)],
          deps=["spirits"], icon="botania:flugel_tiara", size=1.5, shape="diamond"),

    quest("tiara_wings", 15.25, 0, "&bGib der Tiara Flügel",
          subtitle="Jede Quarzsorte, ein Flügelpaar.",
          description=[
              "Tiara plus eine &6Quarzsorte&r an der Werkbank ändert die Flügel. Jederzeit wieder tauschbar.",
              "",
              "Die Quarzsorten stehen in der Lexica unter Dekorative Blöcke, Elfenquarz tauschen dir die Elfen gegen Netherquarz.",
          ],
          tasks=[task_advancement("botania:main/tiara_wings", "Der Tiara Flügel geben")],
          rewards=[reward_item("minecraft:quartz", 16), reward_xp(5)],
          deps=["tiara"], optional=True, icon="botania:flugel_tiara"),

    quest("dandelifeon", 12.75, 2.5, "&aPflanz einen Lebenzahn",
          subtitle="Conways Spiel des Lebens, in Mana.",
          description=[
              "Apotheke: &e2 violette, 1 hellgrünes, 1 grünes&r Blütenblatt, Runen von &eWasser, Feuer, Erde, Luft&r, &6Redstone-Wurzel&r, &dGaia-Seele&r.",
              "",
              "Um ihn liegt ein Feld von &e25x25&r. Mit Redstone-Signal rechnet er zweimal pro Sekunde einen Schritt: Zellen mit 2 oder 3 Nachbarn überleben, leere mit genau 3 werden lebendig.",
              "",
              "Zellen, die ins 3x3 um die Blume wachsen, werden zu &d60 Mana mal Alter&r, Alter höchstens 100.",
          ],
          tasks=[task_item("botania:dandelifeon", 1)],
          rewards=[reward_item("botania:redstone_root", 4), reward_xp(5)],
          deps=["spirits"], icon="botania:dandelifeon", optional=True),

    quest("cells", 12.75, 4.6, "&aCrafte Zellblöcke",
          subtitle="Die Spielsteine des Lebenzahns.",
          description=[
              "&e3 Kaktus&r, &e1 Rote Bete&r, &e1 Karotte&r, &e1 Kartoffel&r. Leg sie als Startmuster ins Feld.",
              "",
              "Zellblöcke sind zerbrechlich, geben abgebaut nichts zurück und lassen sich nicht schieben. Zwei Lebenzähne mit überlappenden Feldern töten die Zellen dazwischen.",
          ],
          tasks=[task_item("botania:cellular_block", 32)],
          rewards=[reward_item("minecraft:cactus", 32)],
          deps=["dandelifeon"], optional=True, icon="botania:cellular_block"),

    quest("shulk", 15.25, 4.8, "&aPflanz ein Shulk Mein Nicht",
          subtitle="75 000 Mana pro Treffer.",
          description=[
              "Apotheke: &e2 violette, 2 magenta, 1 hellgraues&r Blütenblatt, &dGaia-Seele&r, Runen des &5Neids&r und des &5Zorns&r.",
              "",
              "Trifft ein Shulker-Geschoss ein Monster in ihrem Umkreis, sterben beide und es gibt &d75 000 Mana&r. Ihr Puffer muss dafür leer sein. Beute und Erfahrung gehen verloren.",
          ],
          tasks=[task_item("botania:shulk_me_not", 1)],
          rewards=[reward_item("minecraft:shulker_shell", 2), reward_xp(5)],
          deps=["dandelifeon"], optional=True, icon="botania:shulk_me_not"),

    quest("trinkets", 15.25, -1.6, "&6Näh die Umhänge des Urteils",
          subtitle="Drei Umhänge, je eine Gaia-Seele.",
          description=[
              "&6Umhang der Tugend&r (4 weiße Wolle, 4 Glowstonestaub): blockt einen Treffer ganz.",
              "&6Umhang der Sünde&r (4 schwarze Wolle, 4 Redstone): gibt den Schaden an Monster in der Nähe weiter.",
              "&6Umhang der Balance&r (4 hellgraue Wolle, 4 Smaragde): teilt den Schaden mit dem Angreifer.",
              "",
              "Nach dem Auslösen brauchen sie zehn Sekunden Pause.",
          ],
          tasks=[task_item("botania:cloak_of_virtue", 1), task_item("botania:cloak_of_sin", 1),
                 task_item("botania:cloak_of_balance", 1)],
          rewards=[reward_item("minecraft:white_wool", 8), reward_xp(5)],
          deps=["tiara"], optional=True, icon="botania:cloak_of_virtue"),

    quest("gaia_pendants", 15.25, -3.2, "&6Veredle deinen Schmuck mit Gaia",
          subtitle="Vier Upgrades, eine Zeile pro Stück.",
          description=[
              "&6Karmesin-Anhänger&r (Pyroklastanhänger, 5 Lohenruten, 2 Netherziegel, Gaia-Seele): immun gegen Feuer und Lava.",
              "&6Nimbus-Amulett&r (Zirrus-Amulett, 4 Ghast-Tränen, Elementium, 2 Wolle, Gaia-Seele): dreifacher Sprung.",
              "&6Schärpe des Weltreisenden&r (Schärpe des Reisenden, 2 Elementium, Gaia-Seele): viel schneller.",
              "&6Zauber der Diva&r (2 Gaia-Seelen, 3 Gold, Winziger Planet, Rune des Hochmuts): Monster, die dich treffen, gehen auf andere Monster los.",
          ],
          tasks=[task_item("botania:crimson_pendant", 1), task_item("botania:nimbus_amulet", 1),
                 task_item("botania:globetrotters_sash", 1), task_item("botania:charm_of_the_diva", 1)],
          rewards=[reward_item("botania:elementium_ingot", 4), reward_table("s4_uncommon")],
          deps=["trinkets"], optional=True, icon="botania:crimson_pendant"),

    quest("elven_rings", 17.75, -3.2, "&6Trag die Elfenringe",
          subtitle="Zwei Ringe aus Elementium.",
          description=[
              "&6Großer Feenring&r (Feenstaub, 4 Elementium): ruft öfter eine Fee, wenn du getroffen wirst.",
              "&6Ring der großen Reichweite&r (Rune des Hochmuts, 4 Elementium): etwa 3 Blöcke mehr Reichweite.",
              "",
              "Die Relikte Ring des Thor, Loki und Odin gibt nur der Schicksalswürfel aus Gaia II, Stufe 5.",
          ],
          tasks=[task_item("botania:great_fairy_ring", 1), task_item("botania:ring_of_far_reach", 1)],
          rewards=[reward_item("botania:pixie_dust", 4), reward_xp(5)],
          deps=["gaia_pendants"], optional=True, icon="botania:great_fairy_ring"),

    quest("black_hole", 17.75, -1.6, "&5Crafte einen Schwarzloch-Talisman",
          subtitle="Fast unbegrenzt viele Blöcke einer Sorte.",
          description=[
              "Gaia-Seele oben, Elementium, &5Reine Ender-Essenz&r, Elementium in der Mitte, Elementium unten.",
              "",
              "Rechtsklick auf einen Block legt die Sorte fest, Schleich-Rechtsklick in die Luft schaltet ihn an. Dann saugt er diese Blöcke aus deinem Inventar. Rechtsklick setzt sie wieder.",
          ],
          tasks=[task_item("botania:black_hole_talisman", 1)],
          rewards=[reward_item("minecraft:cobblestone", 64), reward_xp(5)],
          deps=["trinkets"], optional=True, icon="botania:black_hole_talisman"),

    quest("astrolabe", 20.25, -1.6, "&6Bau ein Weltgestalter-Astrolab",
          subtitle="Viele Blöcke auf einmal setzen.",
          description=[
              "&e5 Elementium&r, &e2 Gaia-Seelen&r, &e1 Traumholzstamm&r.",
              "",
              "Schleich-Rechtsklick auf einen Block wählt ihn, Schleich-Rechtsklick in die Luft die Menge. Rechtsklick baut die Vorschau mit Mana und Blöcken aus deinem Inventar, auch aus dem Schwarzloch-Talisman.",
          ],
          tasks=[task_item("botania:worldshapers_astrolabe", 1)],
          rewards=[reward_item("botania:dreamwood_log", 16), reward_xp(5)],
          deps=["black_hole"], optional=True, icon="botania:worldshapers_astrolabe"),

    quest("starcaller", 15.25, 1.6, "&eSchmied den Sternrufer",
          subtitle="Ein Schwert, das Sterne fallen lässt.",
          description=[
              "&aTerraklinge&r, &e2 Reine Ender-Essenz&r, &dDrachenstein&r, &dElementiumbarren&r. Verzauberungen der Klinge gehen verloren.",
              "",
              "Bei jedem Schwung fällt ein Stern auf die Stelle, die du ansiehst.",
          ],
          tasks=[task_item("botania:starcaller", 1)],
          rewards=[reward_item("botania:pure_ender_essence", 2)],
          deps=["tiara"], icon="botania:starcaller", optional=True),

    quest("thundercaller", 15.25, 3.2, "&eSchmied den Donnerrufer",
          subtitle="Blitze, die von Monster zu Monster springen.",
          description=[
              "&aTerraklinge&r, &e2 Reine Ender-Essenz&r, &bManadiamant&r, &dElementiumbarren&r.",
              "",
              "Ein Treffer in einer Menge löst eine Blitzkette aus, die feindliche Mobs in der Nähe trifft.",
          ],
          tasks=[task_item("botania:thundercaller", 1)],
          rewards=[reward_item("botania:mana_diamond", 2)],
          deps=["starcaller"], icon="botania:thundercaller", optional=True),

    # ---- Fuer den Obelisken ------------------------------------------------------
    quest("goal", 17.75, 0, "&d&lLiefer Seelen für das Licht des Drachen",
          subtitle="128 Gaia-Seelen für den Obelisken.",
          description=[
              "Sammle &e64 Gaia-Seelen&r für den Obelisken. Das Ziel will &e128&r (feste Zahl) und &e30 Mystische Stäbe&r aus Mahou Tsukai.",
              "",
              "Mit acht Seelen pro Kampf sind das &esechzehn Kämpfe&r, alle live. Feste Arena, ein Terrastahl pro Kampf, Seelen direkt in die Truhe am Obelisken.",
              "",
              "Sind auch Draconium und Elite-Schaltkreise der Techniker drin, öffnet &6Stufe 5 (Chaoswerk)&r.",
          ],
          tasks=[task_item("botania:gaia_spirit", 64)],
          rewards=[reward_table("s4_rare"), reward_xp(20)],
          deps=["spreader", "tiara"], icon="botania:gaia_spirit", size=2.0, shape="gear"),

    quest("outlook", 20.25, 0, "&8Schau auf Gaia II",
          subtitle="Was in Stufe 5 kommt.",
          description=[
              "Vier Gaia-Seelen um einen Terrastahlbarren ergeben den &dGaia-Seelenbarren&r. Dem Beacon geopfert startet er das &dRitual von Gaia II&r mit einem stärkeren Wächter.",
              "",
              "Der gibt 10 Seelen für jeden, 16 für den letzten Treffer, dazu Runen, Manastahl, Manaperlen, Lotusblüten und einen &6Schicksalswürfel&r für eines der Relikte der Asen.",
              "",
              "&cKommt in Stufe 5:&r Dann will der Obelisk &e128 Gaia-Seelenbarren&r, und die Techniker brauchen sie für Erwachtes Draconium.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["goal"], icon="botania:terrasteel_ingot", optional=True),
]

images = [
    banner("gaia/title", "Botania: Gaia", 9, -6.2, height=1.8, kind="title", colour="nature"),
    banner("gaia/vorbereitung", "Vorbereitung", 2.6, -3.0, height=0.9, colour="nature"),
    banner("gaia/kampf", "Der Kampf", 9.0, 4.0, height=0.9, colour="magic"),
    banner("gaia/seelen", "Aus Gaia-Seelen", 15.25, -4.6, height=0.9, colour="nature"),
    banner("gaia/obelisk", "Für den Obelisken", 19.2, 1.8, height=0.9, colour="magic"),
]

chapter(C, "Botania: Gaia", "botania:gaia_spirit", "magic", quests, shape="circle", order=39, stage=4,
        subtitle=["Stufe 4. Das Ritual von Gaia, der Wächter und was aus seinen Seelen wird."], images=images)
