"""The End in stage 4: the stage event activates the End portal for everyone. Arrival and gear,
the dragon as the first shared boss (crystals, fight, breath, heart, egg, scales, respawning), the
gateways and the outer islands (end cities, shulkers, elytra, chorus, the Biomes O' Plenty
biomes), the structures of Dungeons and Taverns, Explorify and When Dungeons Arise, the Ruined
Citadel of L_Ender's Cataclysm with Ender Golems, Endermapteras and the Ender Guardian, and the
resources for the stage goal (draconium, elite circuits, the big cells, the mod ores). Numbers
from the jars, cataclysm-common.toml, DraconicEvolution.cfg, mysticalagradditions-common.toml,
lootr-common.toml and kubejs/server_scripts/kronwerke."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_dimension, task_kill, task_advancement,
                  reward_item, reward_table, reward_xp, banner, img, item_texture)

C = "the_end"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Anreise -------------------------------------------------------------
    quest("arrival", 0, 0, "&5&lBetritt das End",
          subtitle="Das Portal ist seit dem Event für alle offen.",
          description=[
              "Spring in das &5Endportal&r. Es wurde mit dem Event zu &eStufe 4&r auf Stream aktiviert, seitdem ist das End für alle offen.",
              "",
              "Du landest auf einer Plattform aus Obsidian neben der Hauptinsel. &eYUNG's Better End Island&r baut die Insel um: neue Plattform, ein Turm in der Mitte, eigene Transitportale.",
              "",
              "&cUnter den Inseln ist nur Leere.&r Wer fällt, stirbt, und seine Sachen sind weg. Nimm beim ersten Mal nur mit, was du brauchst.",
          ],
          tasks=[task_dimension("minecraft:the_end")],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_table("s4_common"), reward_xp(10)],
          icon="minecraft:end_stone", size=2.0, shape="hexagon"),

    quest("prepare", 2.5, 0, "&dRüste dich für das End aus",
          subtitle="Kürbis, Bogen, Blöcke.",
          description=[
              "Pack einen &6Geschnitzten Kürbis&r, einen &6Bogen&r und &e64 Pfeile&r ein. Mit dem Kürbis auf dem Kopf greifen Endermen nicht an, wenn du sie ansiehst.",
              "",
              "&eDazu:&r einen Stapel Bruchstein für Säulen und Lücken, einen &6Wassereimer&r gegen Endermen, Goldene Karotten und Heiltränke.",
              "",
              "Der Kürbis schränkt die Sicht ein. Für den Drachenkampf tauschst du ihn gegen einen Helm.",
          ],
          tasks=[task_item("minecraft:carved_pumpkin", 1), task_item("minecraft:bow", 1), task_item("minecraft:arrow", 64)],
          rewards=[reward_item("minecraft:arrow", 64), reward_item("minecraft:golden_carrot", 16)],
          deps=["arrival"], icon="minecraft:carved_pumpkin", size=1.5),

    quest("own_portal", 0, 2.5, "&5Finde ein eigenes Endportal",
          subtitle="Zwölf Enderaugen und eine Festung.",
          description=[
              "Wirf ein &6Enderauge&r in die Luft, folg ihm, und grab dich hinunter, wenn es nach unten zeigt. Unten liegt eine &6Festung&r von &eYUNG's Better Strongholds&r. Füll die 12 Rahmenblöcke mit &e12 Enderaugen&r.",
              "",
              "Ab und zu zerbricht ein Auge. Das Portal am Spawn reicht für alle, ein eigenes lohnt sich nur, wenn deine Basis weit weg liegt.",
          ],
          tasks=[task_item("minecraft:ender_eye", 12)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(10)],
          deps=["arrival"], icon="minecraft:ender_eye", optional=True),

    quest("a_endermen", 2.5, 2.5, "&5Sammle Enderperlen",
          subtitle="Hier laufen mehr Endermen als irgendwo sonst.",
          description=[
              "Erleg &e10 Endermen&r und bring &e16 Enderperlen&r mit. Stell dich unter ein zwei Blöcke hohes Dach: Dort kommen sie nicht an dich heran.",
              "",
              "Perlen brauchst du für Enderaugen, Warppulver und Warpsteine, für Draconic Evolution und für die Transitportale der nächsten Abschnitte.",
          ],
          tasks=[task_kill("minecraft:enderman", 10), task_item("minecraft:ender_pearl", 16)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(5)],
          deps=["prepare"], icon="minecraft:ender_pearl"),

    # ---- Der Drache ----------------------------------------------------------
    quest("crystals", 5, 0, "&dZerstör die Endkristalle",
          subtitle="Erst die Kristalle, dann der Drache.",
          description=[
              "Schieß jeden &dEndkristall&r auf den Obsidiansäulen mit dem Bogen ab. Solange einer steht, heilt sich der Drache daran.",
              "",
              "Zwei Kristalle sitzen in Käfigen aus Eisengittern. Bau dich hoch, brich ein Gitter auf und schieß durch das Loch. Ein Kristall explodiert, also nicht danebenstehen.",
              "",
              "&eTipp:&r Verteilt die Säulen. Zu zehnt dauert das wenige Minuten.",
          ],
          tasks=[task_checkmark("Die Kristalle sind zerstört")],
          rewards=[reward_item("minecraft:arrow", 32), reward_xp(5)],
          deps=["prepare"], icon="minecraft:end_crystal"),

    quest("dragon", 7.5, 0, "&5&lBesiege den Enderdrachen",
          subtitle="Der erste gemeinsame Boss der Season.",
          description=[
              "Triff den &5Enderdrachen&r im Flug mit Pfeilen. Landet er auf dem Brunnen in der Mitte, ist das Schwert dran.",
              "",
              "Raus aus den violetten Wolken aus Drachenatem. Sein Kopfstoß schleudert dich weit, im schlimmsten Fall über den Rand. Betten explodieren hier wie im Nether, nur mit Abstand und Absprache.",
              "",
              "&eKronwerke:&r Der erste Kampf läuft auf Stream. Hak ab, wenn du dabei warst, den letzten Schlag landet sowieso nur einer.",
          ],
          tasks=[task_checkmark("Beim Kampf gegen den Drachen dabei")],
          rewards=[reward_table("s4_uncommon"), reward_xp(30)],
          deps=["crystals"], icon="minecraft:dragon_head", size=2.5, shape="gear"),

    quest("breath", 7.5, 2.5, "&dFüll Drachenatem ab",
          subtitle="Die violetten Wolken, in Flaschen.",
          description=[
              "Halt eine leere &6Glasflasche&r in die violetten Wolken des Drachen, bis du &e4 Drachenatem&r hast.",
              "",
              "&eWofür:&r Verweiltränke im Braustand, die Glyphen &eLinger&r und &eWall&r von Ars Nouveau, mehrere Rituale von Occultism, darunter der &6Besessene Shulker&r.",
              "",
              "Sammle schon beim ersten Kampf, danach musst du den Drachen neu beschwören.",
          ],
          tasks=[task_item("minecraft:dragon_breath", 4)],
          rewards=[reward_item("minecraft:glass_bottle", 16), reward_xp(10)],
          deps=["dragon"], icon="minecraft:dragon_breath"),

    quest("heart", 10, -1.5, "&cHeb das Drachenherz auf",
          subtitle="Eines pro Kampf, für den, der zuerst zugreift.",
          description=[
              "Nimm das &cDrachenherz&r, das jeder Drache mit &6Draconic Evolution&r fallen lässt. Es gibt eines pro Kampf, also klärt vorher, wer es bekommt.",
              "",
              "In Stufe 4 steckt es im Wyvern-Schildmodul, in &eStufe 5&r in jedem erweckten Draconium.",
              "",
              "&eRezept auf Kronwerke:&r Beim erweckten Draconium werden zwei der sechs Draconiumkerne durch &dGaia-Geistbarren&r ersetzt. Das Herz bleibt drin.",
          ],
          tasks=[task_item("draconicevolution:dragon_heart", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 4), reward_xp(10)],
          deps=["dragon"], icon="draconicevolution:dragon_heart", optional=True),

    quest("egg", 10, 0, "&5Hol das Drachenei",
          subtitle="Es will nicht angefasst werden.",
          description=[
              "Stell eine &6Fackel&r unter den Block, auf dem das &5Drachenei&r liegt, und bau den Block ab. Das Ei fällt auf die Fackel und wird zum Gegenstand.",
              "",
              "Anklicken bringt nichts, dann teleportiert es sich weg. &eAuf Kronwerke&r erscheint nach jedem Sieg ein neues Ei, nicht nur nach dem ersten.",
          ],
          tasks=[task_item("minecraft:dragon_egg", 1)],
          rewards=[reward_xp(15)],
          deps=["dragon"], icon="minecraft:dragon_egg", optional=True),

    quest("d_scales", 10, 1.5, "&dSammle Drachenschuppen",
          subtitle="Acht Schuppen pro Drache.",
          description=[
              "Heb die &e8 Drachenschuppen&r auf, die jeder Drache mit Mystical Agradditions fallen lässt.",
              "",
              "Sie gehören in die &6Drachenei-Kruste&r, die Grundlage der Drachenei-Samen. Die kommt erst in &eStufe 5&r, also leg die Schuppen beiseite.",
          ],
          tasks=[task_item("mysticalagradditions:dragon_scale", 8)],
          rewards=[reward_xp(10)],
          deps=["dragon"], icon="mysticalagradditions:dragon_scale", optional=True),

    quest("respawn", 12.5, 0, "&dBeschwör den Drachen neu",
          subtitle="Vier Kristalle auf den Rand des Portals.",
          description=[
              "Leg &64 Endkristalle&r auf den Rand des Ausgangsportals, einen an jede Seite. Ein Kristall sind &67 Glas&r, ein &6Enderauge&r und eine &6Ghastträne&r.",
              "",
              "Säulen, Kristalle und Käfige kommen zurück, der Drache erscheint, die Glocke von YUNG's Better End Island läutet.",
              "",
              "&eWarum:&r Jeder Drache bringt ein Herz, ein Ei, 8 Schuppen, Drachenatem und rund &e64 Draconiumstaub&r. Und alle, die beim ersten Mal nicht trafen, bekommen ihre Chance.",
          ],
          tasks=[task_advancement("minecraft:end/respawn_dragon", "Den Drachen neu beschwören"), task_kill("minecraft:ender_dragon", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 4), reward_table("s4_uncommon"), reward_xp(20)],
          deps=["dragon"], icon="minecraft:end_crystal", size=1.5),

    # ---- Die äußeren Inseln --------------------------------------------------
    quest("gateway", 5, 7, "&5Reise durch ein Transitportal",
          subtitle="Eine Enderperle durch das Loch.",
          description=[
              "Wirf eine &6Enderperle&r in das &5Transitportal&r am Rand der Hauptinsel. Nach jedem Sieg über den Drachen erscheint ein neues.",
              "",
              "Drüben liegen die &eäußeren Inseln&r, etwa tausend Blöcke von der Mitte. Neben deiner Landestelle entsteht ein Rückweg. Stell einen Wegstein daneben, wilde Wegsteine gibt es hier ebenfalls.",
          ],
          tasks=[task_advancement("minecraft:end/enter_end_gateway", "Durch ein Transitportal reisen")],
          rewards=[reward_item("minecraft:ender_pearl", 16), reward_xp(10)],
          deps=["dragon"], icon="minecraft:ender_pearl", size=1.5, shape="hexagon"),

    quest("end_city", 7.5, 7, "&dFinde eine Endsiedlung",
          subtitle="Lila Türme in der Leere.",
          description=[
              "Such auf den äußeren Inseln eine &dEndsiedlung&r: hohe Türme aus &6Purpur&r mit Brücken und Truhen.",
              "",
              "Die Truhen sind Lootr-Truhen, jeder bekommt seine eigene Beute, oft verzauberte Diamantausrüstung. In den Wänden sitzen Shulker. Bau Geländer, wo du kämpfst.",
          ],
          tasks=[task_advancement("minecraft:end/find_end_city", "Eine Endsiedlung finden")],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          deps=["gateway"], icon="minecraft:purpur_block"),

    quest("shulker", 10, 6, "&dMach eine Shulkerkiste",
          subtitle="Zwei Schalen, eine Truhe.",
          description=[
              "Erleg Shulker, bis du &e4 Shulkerschalen&r hast. Zwei Schalen und eine Truhe ergeben eine &6Shulkerkiste&r, die beim Abbauen ihren Inhalt behält.",
              "",
              "Ihre Geschosse lassen dich schweben. Über der Leere ist das gefährlich, denn wenn die Wirkung endet, fällst du.",
              "",
              "Shulker kommen nicht wieder. Mit Occultism machst du neue: das Afrit-Ritual &eBesessener Shulker&r (Drachenatem, Endstein, lila glasierte Keramik).",
          ],
          tasks=[task_item("minecraft:shulker_shell", 4), task_item("minecraft:shulker_box", 1)],
          rewards=[reward_item("minecraft:shulker_shell", 2), reward_xp(10)],
          deps=["end_city"], icon="minecraft:shulker_shell"),

    quest("elytra", 10, 8, "&5&lHol dir Elytren",
          subtitle="Am Bug eines Endschiffs, für jeden ein Paar.",
          description=[
              "Neben manchen Endsiedlungen schwebt ein &5Endschiff&r. Drinnen hängen &5Elytren&r im Rahmen. &eAuf Kronwerke&r macht Lootr daraus einen Rahmen pro Spieler: Jeder holt sich aus demselben Schiff sein eigenes Paar.",
              "",
              "Leg sie in den Brustplatz, spring und drück im Fallen nochmal Springen. &6Feuerwerksraketen&r geben Schub. Reparatur mit &6Phantomhaut&r oder Reparatur-Verzauberung.",
              "",
              "Das Wyvern-Flugmodul von Draconic Evolution braucht eine Elytra.",
          ],
          tasks=[task_item("minecraft:elytra", 1)],
          rewards=[reward_item("minecraft:firework_rocket", 32), reward_item("minecraft:phantom_membrane", 4), reward_xp(15)],
          deps=["end_city"], icon="minecraft:elytra", size=1.5),

    quest("chorus", 5, 9.5, "&dErnte Chorusfrüchte",
          subtitle="Die Pflanze, die teleportiert.",
          description=[
              "Brich &dChoruspflanzen&r unten ab und sammle &e16 Chorusfrüchte&r. Im Ofen werden &e8&r davon zu Geplatzten Chorusfrüchten.",
              "",
              "Vier geplatzte ergeben vier &6Purpurblöcke&r, eine mit Lohenrute einen &6Endstab&r. Gegessen teleportiert dich eine Frucht zufällig, über der Leere ein Glücksspiel.",
              "",
              "Eine &6Chorusblüte&r wächst nur auf Endstein. Ein paar Blöcke in der Basis reichen für eine Farm.",
          ],
          tasks=[task_item("minecraft:chorus_fruit", 16), task_item("minecraft:popped_chorus_fruit", 8)],
          rewards=[reward_item("minecraft:end_stone", 16), reward_xp(5)],
          deps=["gateway"], icon="minecraft:chorus_fruit"),

    quest("i_biomes", 7.5, 9.5, "&dBesuch die Biome von Biomes O' Plenty",
          subtitle="Drei neue Biome zwischen den Inseln.",
          description=[
              "Such auf den äußeren Inseln die drei End-Biome von Biomes O' Plenty und hak ab, wenn du eines betreten hast.",
              "",
              "&6Endwildnis:&r eigene Bäume und Endpflanzen. &6Endkorruption:&r Anomalien und Seen aus flüssigem Nichts. &6Endriff:&r Seepocken, tote Korallen und Gezeitentümpel.",
          ],
          tasks=[task_checkmark("Ein End-Biom von Biomes O' Plenty betreten")],
          rewards=[reward_xp(10)],
          deps=["chorus"], icon="biomesoplenty:algal_end_stone", optional=True),

    # ---- Bauwerke ------------------------------------------------------------
    quest("structures", 2.5, 7, "&6Finde ein Bauwerk der anderen Mods",
          subtitle="Mehr als Purpur auf den äußeren Inseln.",
          description=[
              "Finde eines dieser Bauwerke und hak ab: die &6Endburg&r, den &6End-Leuchtturm&r oder das &6Endschiff&r von Dungeons and Taverns, oder das &6Endschiffswrack&r von Explorify.",
              "",
              "Alle Truhen darin sind Lootr-Truhen. Die Zitadelle von Cataclysm hat ihren eigenen Abschnitt weiter unten.",
          ],
          tasks=[task_checkmark("Ein Bauwerk im End gefunden")],
          rewards=[reward_table("s4_common"), reward_xp(10)],
          deps=["gateway"], icon="minecraft:end_stone_bricks"),

    quest("st_aviary", 2.5, 9.5, "&6Finde die Voliere",
          subtitle="When Dungeons Arise baut hoch über den Inseln.",
          description=[
              "Finde die &6Aviary&r (Voliere) von When Dungeons Arise. Sie steht nur in den End-Hochländern und Mittelländern.",
              "",
              "Eine große Anlage mit vielen Etagen, Gegnern und Truhen. Geht zu mehreren und nehmt Blöcke für den Rückweg mit.",
          ],
          tasks=[task_advancement("dungeons_arise:find_aviary", "Die Aviary finden")],
          rewards=[reward_table("s4_common"), reward_xp(15)],
          deps=["structures"], icon="minecraft:feather", optional=True),

    # ---- Die Zitadelle ---------------------------------------------------------
    quest("cg_find", 5, 14, "&6Finde die Ruined Citadel",
          subtitle="Das Auge der Leere zeigt den Weg.",
          description=[
              "Craft ein &6Auge der Leere&r und wirf es: oben &6Purpursäule, Shulkerschale, Purpursäule&r, Mitte &6Endsteinziegel, Enderauge, Endsteinziegel&r, unten &6Purpurblock, Shulkerschale, Purpurblock&r.",
              "",
              "Die &6Ruined Citadel&r von Cataclysm steht nur in den End-Hochländern und Mittelländern. Darin warten Ender Golems, Endermapteras und am Ende der &cEnder Guardian&r.",
          ],
          tasks=[task_advancement("cataclysm:find_ruined_citadel", "Die Ruined Citadel finden")],
          rewards=[reward_item("minecraft:shulker_shell", 2), reward_xp(10)],
          deps=["gateway"], icon="cataclysm:void_eye", size=1.5, shape="hexagon"),

    quest("cg_golem", 7.5, 13, "&5Besiege einen Ender Golem",
          subtitle="Er bewacht die Zitadelle und lässt einen Leerenkern fallen.",
          description=[
              "Erleg einen &5Ender Golem&r. Er hat &e150 Leben&r, Rüstung 12, und beschwört Leerenrunen aus dem Boden, die 7 Schaden machen.",
              "",
              "&eBeute:&r ein &6Leerenkern&r. Rechtsklick ruft selbst Leerenrunen. Auf dem Mechanischen Fusionsamboss wird er Teil von &6Leerenschmiede&r und &6Leeren-Schulterwaffe&r (siehe Ender Guardian).",
          ],
          tasks=[task_kill("cataclysm:ender_golem", 1), task_item("cataclysm:void_core", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(15)],
          deps=["cg_find"], icon="cataclysm:void_core"),

    quest("cg_endermaptera", 7.5, 15, "&5Jag Endermapteras",
          subtitle="Käfer der Zitadelle, manche mit Kiefern.",
          description=[
              "Erleg &e5 Endermapteras&r. Sie haben nur 16 Leben, kommen aber in Gruppen.",
              "",
              "Die mit Kiefern lassen einen &6Leerenkiefer&r fallen. Ein Kiefer über einem Spektralpfeil ergibt &e2 Leerenstreupfeile&r.",
          ],
          tasks=[task_kill("cataclysm:endermaptera", 5)],
          rewards=[reward_item("minecraft:spectral_arrow", 16), reward_xp(10)],
          deps=["cg_find"], icon="cataclysm:void_jaw", optional=True),

    quest("cg_kill", 10, 14, "&c&lBesiege den Ender Guardian",
          subtitle="Der Wächter der Zitadelle.",
          description=[
              "Geh zum &6Altar der Leere&r tief in der Zitadelle. Sobald du nah genug bist, erscheint der &cEnder Guardian&r: &e333 Leben&r, Rüstung 20.",
              "",
              "Seine Schläge machen Prozente deiner Gesundheit (Aufwärtshaken und Raketenschlag 10 Prozent), dazu Leerenrunen mit 9 Schaden. Er zerschlägt Blöcke um sich. Kappung: 22 pro Treffer, 13 pro Sekunde, ab 12 Blöcken kaum Schaden, also nah ran.",
              "",
              "&eBeute:&r der &6Handschuh der Wacht&r (Rechtsklick zieht Gegner heran), mit 10 Prozent eine Schallplatte. Für einen zweiten Kampf nimmt der Boss-Wiederbeleber ein Auge der Leere.",
          ],
          tasks=[task_kill("cataclysm:ender_guardian", 1)],
          rewards=[reward_table("s4_rare"), reward_item("minecraft:golden_apple", 2), reward_xp(40)],
          deps=["cg_golem"], icon="cataclysm:gauntlet_of_guard", size=2.0, shape="diamond"),

    quest("cg_gear", 12.5, 14, "&6Verschmelz die Bosswaffen",
          subtitle="Leerenkern und Handschuh auf dem Fusionsamboss.",
          description=[
              "Am &6Mechanischen Fusionsamboss&r (6 Witherit vom Harbinger, 2 Redstoneblöcke, Amboss) verschmilzt du Bosswaffen:",
              "",
              "&6Leerenschmiede:&r Höllenschmiede der Netherite Monstrosity plus Leerenkern. &6Handschuh des Bollwerks:&r Handschuh der Wacht plus Bollwerk der Flamme von Ignis. &6Leeren-Schulterwaffe:&r Wither-Schulterwaffe plus Leerenkern.",
              "",
              "Ignis und die Monstrosity stehen im Kapitel &cDer Nether&r, der Harbinger im Kapitel &cBosse der Oberwelt&r.",
          ],
          tasks=[task_item("cataclysm:void_forge", 1)],
          rewards=[reward_item("minecraft:netherite_scrap", 2), reward_xp(20)],
          deps=["cg_kill"], icon="cataclysm:void_forge", optional=True),

    # ---- Rohstoffe -----------------------------------------------------------
    quest("draconium", 15, 0, "&5&lBau Draconium ab",
          subtitle="Es wächst nur noch im End.",
          description=[
              "Bau &6Draconiumerz&r im Endstein ab, bis du &e32 Draconiumstaub&r hast, und schmilz &e16 Barren&r. Es liegt zwischen &eY 0 und 70&r, drei Adern pro Chunk.",
              "",
              img("draconicevolution:textures/item/components/draconium_dust.png", 32, 32),
              "",
              "Ohne Behutsamkeit gibt ein Erz &e2 bis 4 Staub&r, Glück bringt mehr. Mit Behutsamkeit bekommst du nur das Erz, und das schmilzt zu einem Barren. Also lieber den Staub.",
              "",
              "&eKronwerke:&r Die Erzadern in Oberwelt und Nether sind abgeschaltet. Das Ziel will &e1 000 Draconiumbarren&r.",
          ],
          tasks=[task_item("draconicevolution:draconium_dust", 32), task_item("draconicevolution:draconium_ingot", 16)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 8), reward_table("s4_common"), reward_xp(10)],
          deps=["respawn"], icon="draconicevolution:draconium_ingot", size=2.0, shape="hexagon"),

    quest("elite_circuit", 17.5, -1.5, "&bBau Elite-Schaltkreise",
          subtitle="Mekanism braucht das End.",
          description=[
              "&eRezept auf Kronwerke:&r &62 Fortgeschrittene Schaltkreise&r, &62 Verstärkte Legierungen&r und &61 Draconiumstaub&r an der Werkbank ergeben einen &6Elite-Schaltkreis&r. Andere Rezepte gibt es nicht.",
              "",
              "Ohne ihn keine Elite-Maschinen und kein Weg zu den Ultimativen Schaltkreisen (Kapitel &bMekanism: Elite&r).",
              "",
              "&eKronwerke:&r Das Ziel will &e150 Elite-Schaltkreise&r. Bau dir eine Linie: Staub aus dem End, Legierung aus dem Metallurgischen Infusionierer.",
          ],
          tasks=[task_item("mekanism:elite_control_circuit", 4)],
          rewards=[reward_item("mekanism:alloy_reinforced", 4), reward_xp(12)],
          deps=["draconium"], icon="mekanism:elite_control_circuit"),

    quest("cells", 17.5, 1.5, "&bBau eine 256k-Komponente",
          subtitle="Draconium im Kern der großen Zellen.",
          description=[
              "&eRezept auf Kronwerke:&r Die &6256k-Komponente&r hat statt Glas einen &5Draconiumbarren&r in der Mitte, dazu einen Rechenprozessor, 3 64k-Komponenten und Himmelssteinstaub. Die MEGA-Komponenten für &61M&r und &64M&r ebenso.",
              "",
              "Die 64k-Komponente will einen Himmelsbarren von Nature's Aura. Ab 16M braucht es erwecktes Draconium, das kommt in Stufe 5.",
          ],
          tasks=[task_item("ae2:cell_component_256k", 1)],
          rewards=[reward_item("draconicevolution:draconium_ingot", 4), reward_xp(12)],
          deps=["draconium"], icon="ae2:cell_component_256k"),

    quest("r_ores", 15, 2.5, "&3Bau die anderen End-Erze ab",
          subtitle="Azursilber, Platin und Essenzen im Endstein.",
          description=[
              "Bau &e8 Rohes Azursilber&r von Silent Gear ab. Geschmolzen ist es das Material über Purpur-Eisen (Kapitel &6Silent Gear&r).",
              "",
              "&eAuch im Endstein:&r &6Platinerz&r von Oritech, End-Inferium- und End-Prosperiumerz von Mystical Agradditions, &6Dimensionsscherben&r von RFTools und Endstein-Nester von Productive Bees.",
          ],
          tasks=[task_item("silentgear:raw_azure_silver", 8)],
          rewards=[reward_item("minecraft:ender_pearl", 8), reward_xp(10)],
          deps=["draconium"], icon="silentgear:raw_azure_silver"),

    # ---- Abschluss -----------------------------------------------------------
    quest("supply", 20, 0, "&5&lFüll das Licht des Drachen",
          subtitle="Was das End für das Stufenziel hergibt.",
          description=[
              "Bring &e64 Draconiumbarren&r und &e8 Elite-Schaltkreise&r zusammen und gib sie am Obelisken ab, oder stell eine Truhe daneben.",
              "",
              "&eKronwerke:&r Die Technik-Seite des Ziels &6Licht des Drachen&r will &e1 000 Draconiumbarren&r und &e150 Elite-Schaltkreise&r, die Magie-Seite &e128 Gaia-Geister&r und &e30 Mystic Staffs&r.",
              "",
              "Ein paar Leute mit Spitzhacke im End, eine Schaltkreis-Linie zu Hause, dann füllt sich die Leiste.",
          ],
          tasks=[task_item("draconicevolution:draconium_ingot", 64), task_item("mekanism:elite_control_circuit", 8)],
          rewards=[reward_table("s4_rare"), reward_item("minecraft:ender_pearl", 16), reward_xp(25)],
          deps=["elite_circuit", "cells"], icon="minecraft:dragon_egg", size=2.5, shape="gear"),

    quest("outlook", 20, 3.5, "&dSchau, was noch kommt",
          subtitle="Eine neue Welt jetzt, die Chaosinsel später.",
          description=[
              "Mit Stufe 4 öffnet auch &bEternal Starlight&r, eine eigene Dimension mit drei Bossen (Kapitel &bEternal Starlight&r). Alle Portale auf einen Blick stehen in der &6Checkliste: Dimensionen und Reisen&r.",
              "",
              "Weit draußen im End liegt die &5Chaosinsel&r von Draconic Evolution. Zum Finale in &eStufe 5&r bringt der Obelisk alle dorthin (Kapitel &5Das Finale&r).",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["supply"], icon="minecraft:end_portal_frame", optional=True),
]

images = [
    banner("the_end/title", "Das End", 10, -5.4, height=1.75, kind="title", colour="end"),
    banner("the_end/arrival", "Anreise", 1.25, -2.4, height=0.9, colour="end"),
    banner("the_end/dragon", "Der Drache", 8.75, -3.2, height=0.9, colour="end"),
    banner("the_end/islands", "Die äußeren Inseln", 6.25, 4.9, height=0.9, colour="end"),
    banner("the_end/citadel", "Die Zitadelle", 7.5, 11.6, height=0.9, colour="end"),
    banner("the_end/tech", "Für Technik und Magie", 17.5, -3.2, height=0.9, colour="magic"),
]

chapter(C, "Das End", "minecraft:end_stone", "world", quests, shape="circle", order=32, stage=4,
        subtitle=["Stufe 4: der Drache, die äußeren Inseln, die Zitadelle mit dem Ender Guardian und das Draconium für das Stufenziel."],
        images=images)
