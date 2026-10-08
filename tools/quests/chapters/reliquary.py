"""Reliquary in stage 2: the rare mob drops (zombie heart, rib bone, slime pearl, bat wing, molten
core, nebulous heart) as a checklist, mob charms and the pedestal, the witherless rose, the lantern
of paranoia, the coin of fortune and the hero's medallion, the void tear, the altar of light, the
sojourner's staff and the ender staff with wraith nodes. The tome of alkahestry, the rending gale,
the two chalices and the touchstone of Midas open in stage 3 and are only mentioned. Reliquary has
no German translation, so item names stay English."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner, img, item_texture)

C = "reliquary"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


def drop(name, x, y, item_id, title, subtitle, text, reward, deps=("welcome",)):
    """One checklist quest per mob drop: one item, one tick."""
    return quest(name, x, y, title, subtitle=subtitle, description=[text],
                 tasks=[task_item(item_id, 1)], rewards=[reward_item(*reward), reward_xp(2)],
                 deps=list(deps), icon=item_id)


quests = [
    # ---- Die Tropfen -------------------------------------------------------------
    quest("welcome", 0, 0, "&6Erschlag Monster mit Plünderung",
          subtitle="Jedes Monster trägt ein seltenes Teil in sich.",
          description=[
              "&6Reliquary&r baut seine Werkzeuge aus seltenen Teilen, die Monster beim Tod fallen lassen: ein &6Zombie Heart&r, ein &6Rib Bone&r vom Skelett, ein &6Nebulous Heart&r vom Enderman. Die ganze Mod öffnet mit &6Stufe 2&r.",
              "",
              "Die Chance ist klein: &e2 Prozent&r ohne Verzauberung, mit &6Plünderung III&r 11 Prozent. Noch besser ist die eigene Verzauberung &6Severing&r aus dem Zaubertisch: Severing III gibt 32 Prozent, Severing V 52. Es zählt nur, was du selbst tötest.",
              "",
              "&eTipp:&r Das &6Magicbane&r (zwei Nebulous Hearts, ein Gold, ein Eisen) ist ein kleines Schwert, das mit jeder Verzauberung stärker wird und selbst eine höhere Chance auf diese Teile hat.",
              "",
              "Für den Anfang: Hol dir ein &6Zombie Heart&r.",
          ],
          tasks=[task_item("reliquary:zombie_heart", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 8), reward_table("s2_common")],
          icon="reliquary:zombie_heart", size=2.0, shape="hexagon"),

    drop("rib_bone", 2.8, -1.2, "reliquary:rib_bone", "&7Rib Bone", "Vom Skelett.",
         "Skelette und Streuner lassen ein &6Rib Bone&r fallen. Du brauchst es für die &6Fertile Essence&r und damit für die Witherless Rose.",
         ("minecraft:bone", 8)),
    drop("slime_pearl", 2.8, 1.2, "reliquary:slime_pearl", "&aSlime Pearl", "Vom Schleim.",
         "Schleime lassen eine &6Slime Pearl&r fallen. Sie steckt in der Void Tear, der Lantern of Paranoia, dem Coin of Fortune und der Fertile Essence.",
         ("minecraft:slime_ball", 8)),
    drop("catalyzing_gland", 4.8, -1.2, "reliquary:catalyzing_gland", "&aCatalyzing Gland", "Vom Creeper oder Ghast.",
         "Creeper und Ghasts lassen eine &6Catalyzing Gland&r fallen. Sie steckt im Altar of Light, in der Fertile Essence und in der Holy Hand Grenade.",
         ("minecraft:gunpowder", 8), deps=("rib_bone",)),
    drop("bat_wing", 4.8, 1.2, "reliquary:bat_wing", "&8Bat Wing", "Von der Fledermaus.",
         "Fledermäuse lassen einen &6Bat Wing&r fallen. Du brauchst ihn für den Coin of Fortune, den Ender Staff und die Angelic Feather. Fledermäuse hängen in dunklen Höhlen, Plünderung hilft auch hier.",
         ("minecraft:feather", 8), deps=("slime_pearl",)),
    drop("molten_core", 6.8, -1.2, "reliquary:molten_core", "&cMolten Core", "Vom Blaze oder Magmawürfel.",
         "Blazes (3 Prozent) und Magmawürfel lassen einen &6Molten Core&r fallen. Er steckt in Sojourner's Staff, Lantern of Paranoia und Infernal Claw. Zwei Molten Cores in der Werkbank ergeben 4 Lohenruten.",
         ("minecraft:blaze_rod", 2), deps=("catalyzing_gland",)),
    drop("nebulous_heart", 6.8, 1.2, "reliquary:nebulous_heart", "&5Nebulous Heart", "Vom Enderman.",
         "Endermen lassen ein &6Nebulous Heart&r fallen, das wichtigste Teil der Mod: Void Tear, Ender Staff, Altar, Magicbane und Hero's Medallion brauchen es. Eines in der Werkbank ergibt 3 Enderperlen.",
         ("minecraft:ender_pearl", 4), deps=("bat_wing",)),

    # ---- Schutz ------------------------------------------------------------------
    quest("mob_charm", 0, 5, "&aBau einen Mob Charm",
          subtitle="Eine Mobart, die dich nicht mehr sieht.",
          description=[
              "Ein &6Mob Charm&r braucht fünf &6Mob Charm Fragments&r derselben Art, dazu Leder oben und Faden in der Mitte: Fragment, Leder, Fragment in der ersten Reihe, Fragment, Faden, Fragment in der zweiten, Fragment, leer, Fragment in der dritten.",
              "",
              "Fragmente fallen mit 1 zu 60 beim Töten, oder du craftest sie aus den Drops: sechs &6Zombie Hearts&r um Fauliges Fleisch, Knochen, Fauliges Fleisch ergeben ein Zombie-Fragment, sechs &6Rib Bones&r um Knochen, Feuerstein, Knochen ein Skelett-Fragment. Jede Art hat so ein Rezept.",
              "",
              "Mit dem Charm im Inventar greift dich diese Mobart nicht mehr an. Jeder Kill der Art kostet 1 von &e80 Haltbarkeit&r. Der &6Charm Belt&r (drei Leder, fünf Fragmente) trägt alle Charms zusammen in einem Slot.",
          ],
          tasks=[task_item("reliquary:mob_charm", 1)],
          rewards=[reward_item("minecraft:leather", 8), reward_xp(5)],
          deps=["welcome"], icon="reliquary:mob_charm"),

    quest("pedestal", 0, 7.6, "&aBau ein Pedestal",
          subtitle="Der Sockel, der Dinge für dich benutzt.",
          description=[
              "Erst das &6Passive Pedestal&r: ein Teppich oben, zwei Goldklumpen um einen Quarzblock, drei Quarzstufen unten. Dann vier &6Diamanten&r in die Ecken um das Passive Pedestal, das ergibt das richtige &6Pedestal&r. Die Teppichfarbe bestimmt die Farbe.",
              "",
              "Was im Pedestal liegt, arbeitet: ein &6Mob Charm&r schützt alle Spieler im Umkreis von &e21 Blöcken&r, ein Schwert schlägt 5 Blöcke weit, eine Schere schert Schafe, ein Eimer schöpft, eine Angel angelt, Redstone gibt ein Signal.",
              "",
              "&eTipp:&r Ein Pedestal mit Creeper Charm neben der Basis, und niemand sprengt mehr die Fassade.",
          ],
          tasks=[task_item("reliquary:pedestals/white_pedestal", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["mob_charm"], icon="reliquary:pedestals/white_pedestal"),

    quest("witherless_rose", 2.4, 7.6, "&dPflück eine Witherless Rose",
          subtitle="Nie wieder Wither-Effekt.",
          description=[
              "Vier &6Fertile Essence&r in die Ecken, vier &6Netherstern&r an die Seiten, ein &6Rosenstrauch&r in die Mitte ergeben die &6Witherless Rose&r. Fertile Essence ist Rib Bone, Catalyzing Gland, eine &6Mandrake Root&r aus Hexerei und Slime Pearl in der Werkbank.",
              "",
              "Mit der Rose im Inventar trifft dich der &5Wither&r-Effekt nicht mehr, egal ob von Witherskeletten, dem Wither selbst oder Pfeilen. Vier Nethersterne sind ein Preis, den sich eine Gruppe teilt: Wer den Wither ohnehin farmt, hat sie.",
              "",
              "&eAuch gut:&r Drei Fertile Essence plus eine Seerose ergeben das &6Lilypad of Fertility&r, das Pflanzen im Umkreis von 4 Blöcken alle 10 Sekunden wachsen lässt.",
          ],
          tasks=[task_item("reliquary:witherless_rose", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["mob_charm"], icon="reliquary:witherless_rose", optional=True),

    # ---- Werkzeug ----------------------------------------------------------------
    quest("lantern", 2.8, 5, "&eBau eine Lantern of Paranoia",
          subtitle="Fackeln setzen, ohne hinzusehen.",
          description=[
              "Eisen, &6Slime Pearl&r, Eisen oben, Glas, &6Molten Core&r, Glas in der Mitte, ein Eisen unten ergeben die &6Lantern of Paranoia&r. Shift-Rechtsklick schaltet sie an.",
              "",
              "Dann setzt sie von selbst &6Fackeln&r aus deinem Inventar an jede dunkle Stelle im Umkreis von &e6 Blöcken&r. Beim Höhlengraben, auf der Baustelle oder im Mobfarm-Umfeld bleibt nichts mehr finster. Sie nimmt auch Fackeln aus einem Sojourner's Staff im Inventar.",
          ],
          tasks=[task_item("reliquary:lantern_of_paranoia", 1)],
          rewards=[reward_item("minecraft:torch", 64), reward_xp(5)],
          deps=["slime_pearl"], icon="reliquary:lantern_of_paranoia", section="werkzeug"),

    quest("fortune_coin", 4.8, 5, "&eBau einen Coin of Fortune",
          subtitle="Items und Erfahrung kommen von allein.",
          description=[
              "&6Nebulous Heart&r, Goldklumpen, &6Slime Pearl&r und &6Bat Wing&r formlos in die Werkbank ergeben den &6Coin of Fortune&r. Shift-Rechtsklick schaltet ihn an.",
              "",
              "Aktiv zieht er alle Items und Erfahrungskugeln im Umkreis von &e5 Blöcken&r zu dir. Hältst du Rechtsklick, saugt er &e15 Blöcke&r weit. Für Mobfarmen, Erntefelder und das Ausräumen von Creeperlöchern.",
          ],
          tasks=[task_item("reliquary:fortune_coin", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["bat_wing"], icon="reliquary:fortune_coin"),

    quest("void_tear", 6.8, 5, "&5Mach eine Void Tear",
          subtitle="Eine Sorte, fast ohne Ende.",
          description=[
              "&6Ghastträne&r, &6Nebulous Heart&r, &6Slime Pearl&r und ein &6Lapislazuli&r formlos ergeben die &6Void Tear&r. Sie hält von einer Sorte praktisch unbegrenzt viel.",
              "",
              "Rechtsklick mit der leeren Träne auf eine Kiste saugt eine Sorte heraus, Rechtsklick mit der vollen Träne leert sie in die Kiste. Passende Items, die du aufhebst, wandern direkt hinein. Shift-Mausrad wechselt den Modus: &eEMPTY&r nimmt alle Stapel aus dem Inventar, &eSTACK&r hält immer einen Stapel bereit, &eFILL&r füllt das Inventar.",
              "",
              "Die Träne ist außerdem Zutat für Sojourner's Staff, Ender Staff, Harvest Rod, Ice Magus Rod und die Infernal Tear, die Items zu Erfahrung verbrennt.",
          ],
          tasks=[task_item("reliquary:void_tear", 1)],
          rewards=[reward_table("s2_common"), reward_xp(5)],
          deps=["nebulous_heart"], icon="reliquary:void_tear", size=1.5, shape="hexagon"),

    quest("altar", 9.2, 5, "&eBau einen Altar of Light",
          subtitle="Aus Redstone wächst Glowstone.",
          description=[
              "&6Obsidian&r, &6Redstone-Lampe&r, &6Nebulous Heart&r und &6Catalyzing Gland&r formlos ergeben den &6Altar of Light&r. Stell ihn unter freien Himmel und gib ihm mit Rechtsklick &e3 Redstone&r.",
              "",
              "Nachts arbeitet er, und nach 15 bis 25 Minuten erscheint ein &6Glowstone-Block&r über ihm. Abbauen, neues Redstone hinein, weiter. Solange er arbeitet, leuchtet er selbst mit Lichtstärke 16.",
              "",
              "&cAusblick:&r Der &6Tome of Alkahestry&r, der Items mit Redstone-Ladung verdoppelt, braucht einen Witherskelettschädel und viele Tropfen und öffnet erst mit &6Stufe 3&r. Der Altar ist sein Einstieg, und Glowstone ist bis dahin auch so wertvoll.",
          ],
          tasks=[task_item("reliquary:alkahestry_altar", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_xp(5)],
          deps=["nebulous_heart"], icon="reliquary:alkahestry_altar"),

    quest("hero_medallion", 4.8, 9.4, "&eBau ein Hero's Medallion",
          subtitle="Erfahrung aufheben für später.",
          description=[
              "&6Nebulous Heart&r, &6Coin of Fortune&r, &6Witch Hat&r und &6Infernal Tear&r formlos ergeben das &6Hero's Medallion&r. Den Witch Hat lassen Hexen fallen, die Infernal Tear ist Void Tear, Witch Hat, Molten Core und Infernal Claw.",
              "",
              "Das Medaillon speichert deine Erfahrungslevel und gibt sie mit Rechtsklick zurück. Shift-Mausrad stellt ein, wie viele Level es dir lässt. Stirbst du, ist die Erfahrung im Medaillon noch da.",
          ],
          tasks=[task_item("reliquary:hero_medallion", 1)],
          rewards=[reward_item("minecraft:experience_bottle", 16), reward_xp(8)],
          deps=["fortune_coin"], icon="reliquary:hero_medallion", optional=True),

    quest("sojourner", 6.8, 9.4, "&eBau einen Sojourner's Staff",
          subtitle="1.500 Fackeln in einem Stab.",
          description=[
              "&6Molten Core&r, &6Goldbarren&r, &6Lohenrute&r und &6Void Tear&r formlos ergeben den &6Sojourner's Staff&r. Er zieht Fackeln, Laternen, Seelenfackeln, Glowstone und ähnliche Lichter aus deinem Inventar in sich, bis zu &e1.500 pro Sorte&r.",
              "",
              "Rechtsklick setzt das gewählte Licht dort, wohin du zielst, bis zu &e30 Blöcke&r weit. Je 6 Blöcke Entfernung kostet das eine Fackel extra. Shift-Mausrad wechselt die Sorte.",
          ],
          tasks=[task_item("reliquary:sojourner_staff", 1)],
          rewards=[reward_item("minecraft:torch", 64), reward_table("s2_common"), reward_xp(8)],
          deps=["void_tear", "molten_core"], icon="reliquary:sojourner_staff"),

    quest("ender_staff", 9.2, 9.4, "&5Bau einen Ender Staff",
          subtitle="Perlen werfen und nach Hause springen.",
          description=[
              "Oben Bat Wing und &6Enderauge&r, in der Mitte &6Nebulous Heart&r, &6Void Tear&r, Bat Wing, unten Stock und Nebulous Heart ergeben den &6Ender Staff&r. Er speichert bis zu &e250 Enderperlen&r aus deinem Inventar.",
              "",
              "Shift-Mausrad wechselt den Modus: &eCast&r wirft eine Perle, &eLong Cast&r wirft weiter, &eBind&r merkt sich eine &6Wraith Node&r (Nebulous Heart plus Smaragd, als Block gesetzt), &eNode Warp&r springt nach 3 Sekunden Rechtsklick dorthin. Jeder Sprung kostet eine Perle.",
              "",
              "&eKronwerke:&r Eine Wraith Node am Obelisken, und jede Lieferung fürs Stufenziel ist einen Rechtsklick entfernt.",
          ],
          tasks=[task_item("reliquary:ender_staff", 1), task_item("reliquary:wraith_node", 1)],
          rewards=[reward_table("s2_rare"), reward_item("minecraft:ender_pearl", 16), reward_xp(15)],
          deps=["void_tear"], icon="reliquary:ender_staff", size=2.0, shape="gear"),

    quest("outlook", 11.6, 7.2, "&dAusblick auf Stufe 3",
          subtitle="Was Reliquary noch zurückhält.",
          description=[
              "Mit &6Stufe 3&r öffnen die großen Reliquien: der &6Tome of Alkahestry&r verdoppelt Eisen, Gold, Diamanten und vieles mehr gegen Redstone-Ladung. Die &6Rending Gale&r (Bat Wings, Eye of the Storm von einem geladenen Creeper, Void Tear) lässt dich fliegen, Mobs wegstoßen und bei Regen Blitze werfen.",
              "",
              "Dazu der &6Emperor's Chalice&r als unendlicher Wassereimer, der &6Infernal Chalice&r, der Lava speichert und dich vor Lava schützt, und der &6Touchstone of Midas&r, der Goldwerkzeug mit Glowstone repariert. Alles davon braucht eine Void Tear, also leg schon einmal zwei zur Seite.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["altar"], icon="reliquary:void_tear", optional=True),

    # ---- Schutz: neue Quests ---------------------------------------------------------
    quest("angelic_feather", 1.2, 6.2, "&fBau eine Angelic Feather",
          subtitle="Fallschaden kostet nur noch Hunger.",
          description=[
              "Eine &6Feder&r, ein &6Nebulous Heart&r, ein &6Bat Wing&r und eine &6Fertile Essence&r formlos ergeben die &6Angelic Feather&r. Fertile Essence ist Rib Bone, Catalyzing Gland, &6Mandrake Root&r aus Hexerei und Slime Pearl.",
              "",
              "Im Inventar fängt sie Fallschaden ab und zieht dir dafür Hunger ab. Dazu springst du etwas höher.",
          ],
          tasks=[task_item("reliquary:angelic_feather", 1)],
          rewards=[reward_item("minecraft:cooked_beef", 16), reward_xp(5)],
          deps=["mob_charm", "bat_wing"], icon="reliquary:angelic_feather"),

    quest("phoenix_down", 1.2, 8.6, "&6Mach ein Phoenix Down",
          subtitle="Ein zweites Leben in der Tasche.",
          description=[
              "Zuerst die &6Angelheart Vial&r: Glasscheibe, &6Milcheimer&r, Glasscheibe oben, Glasscheibe, &6Infernal Claw&r, Glasscheibe in der Mitte, Fertile Essence, Glasscheibe, Fertile Essence unten. Sie bewahrt dich einmal vor dem Tod, heilt &e25 Prozent&r deines Lebens, entfernt schlechte Effekte und zerbricht.",
              "",
              "Drei Angelheart Vials und eine &6Angelic Feather&r formlos ergeben das &6Phoenix Down&r. Es holt dich mit vollem Leben zurück, gibt kurz Resistenz und Regeneration und wird danach wieder zur Angelic Feather. Solange es ganz ist, wirkt es auch wie die Feder.",
              "",
              "Die Infernal Claw ist Leder, Molten Core, Rib Bone und Slime Pearl.",
          ],
          tasks=[task_item("reliquary:phoenix_down", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["angelic_feather"], icon="reliquary:phoenix_down"),

    quest("kraken_shell", 1.6, 6.8, "&3Bau eine Kraken Shell",
          subtitle="Nie mehr ertrinken.",
          description=[
              "Tintenfische lassen einen &6Squid Beak&r fallen. Drei davon und eine &6Slime Pearl&r ergeben ein &6Kraken Shell Fragment&r, drei Fragmente und ein &6Nebulous Heart&r die &6Kraken Shell&r.",
              "",
              "Im Inventar nimmt sie dir den Schaden durch Ertrinken ab und zieht dafür Hunger. Für Tauchgänge zu Ozeanmonumenten und Unterwasserbasen.",
          ],
          tasks=[task_item("reliquary:kraken_shell", 1)],
          rewards=[reward_item("minecraft:ink_sac", 8), reward_xp(5)],
          deps=["mob_charm", "slime_pearl"], icon="reliquary:kraken_shell", optional=True),

    quest("infernal_claws", 0.6, 6.8, "&cBau Infernal Claws",
          subtitle="Feuer kostet Hunger statt Leben.",
          description=[
              "Eine &6Infernal Claw&r ist Leder, &6Molten Core&r, &6Rib Bone&r und &6Slime Pearl&r formlos. Drei Claws und eine Slime Pearl ergeben die &6Infernal Claws&r.",
              "",
              "Im Inventar fangen sie Feuerschaden ab und kosten dafür ein wenig Hunger. Brennen und Feuerblöcke werden harmlos. &cLava&r schützen sie nicht.",
              "",
              "&eAusblick:&r Die Claws stecken auch im &6Pyromancer's Staff&r, der Feuerbälle von Blaze und Ghast schießt.",
          ],
          tasks=[task_item("reliquary:infernal_claws", 1)],
          rewards=[reward_item("minecraft:blaze_powder", 8), reward_xp(5)],
          deps=["mob_charm", "molten_core"], icon="reliquary:infernal_claws"),

    quest("twilight_cloak", 0.4, 6.2, "&8Näh einen Twilight Cloak",
          subtitle="Im Dunkeln sieht dich niemand.",
          description=[
              "&6Crimson Cloth&r ist rote Wolle, schwarze Wolle und zwei &6Nebulous Hearts&r. Eisen, Cloth, Eisen oben, darunter zweimal schwarze Wolle, Cloth, schwarze Wolle ergeben den &6Twilight Cloak&r.",
              "",
              "Shift-Rechtsklick schaltet ihn an. Dann bist du bei Lichtstärke &e4&r oder weniger unsichtbar, und Monster können dich nicht anvisieren, auch wenn du sie schlägst.",
              "",
              "&eTipp:&r In unbeleuchteten Höhlen und im Deep Dark gehst du so an allem vorbei.",
          ],
          tasks=[task_item("reliquary:twilight_cloak", 1)],
          rewards=[reward_item("minecraft:black_wool", 8), reward_xp(5)],
          deps=["mob_charm", "nebulous_heart"], icon="reliquary:twilight_cloak", optional=True),

    quest("interdiction_torch", 0.6, 8.0, "&eStell eine Interdiction Torch auf",
          subtitle="Eine Fackel, die Monster wegschiebt.",
          description=[
              "&6Bat Wing&r, &6Lohenrute&r, &6Molten Core&r und &6Nebulous Heart&r formlos ergeben die &6Interdiction Torch&r.",
              "",
              "Gesetzt schiebt sie Monster im Umkreis von &e5 Blöcken&r von sich weg. Eine an der Tür, und nichts drängt mehr nach drinnen. Pfeile hält sie nicht auf.",
          ],
          tasks=[task_item("reliquary:interdiction_torch", 1)],
          rewards=[reward_item("minecraft:torch", 32), reward_xp(5)],
          deps=["mob_charm", "molten_core"], icon="reliquary:interdiction_torch"),

    # ---- Werkzeug: neue Quests -------------------------------------------------------
    quest("harvest_rod", 7.6, 6.2, "&aBau einen Harvest Rod",
          subtitle="Knochenmehl, Saat und Hacke in einem Stab.",
          description=[
              "Rosenstrauch und &6Fertile Essence&r oben, &6Ranken&r, &6Void Tear&r, Rosenstrauch in der Mitte, Stock und Ranken unten ergeben den &6Harvest Rod&r.",
              "",
              "Er nimmt bis zu &e250 Knochenmehl&r und je 250 von jeder Saat aus deinem Inventar auf. Shift-Mausrad wechselt den Modus: Knochenmehl, Pflanzen, Hacke. Rechtsklick wirkt auf einen Block, Rechtsklick halten auf die ganze Fläche um dich. Beim Abbauen erntet er die Pflanzen im Umkreis mit.",
              "",
              "&eTipp:&r In einem &6Pedestal&r erntet, düngt und pflanzt er ein Feld im Umkreis von &e4 Blöcken&r von allein.",
          ],
          tasks=[task_item("reliquary:harvest_rod", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["void_tear"], icon="reliquary:harvest_rod"),

    quest("destruction_catalyst", 8.2, 6.8, "&cBau einen Destruction Catalyst",
          subtitle="Erde und Stein weg, Erze bleiben.",
          description=[
              "Die &6Infernal Tear&r ist Void Tear, Witch Hat, Molten Core und Infernal Claw. Mit &6Feuerzeug&r, &6Molten Core&r und &6Catalyzing Gland&r formlos wird daraus der &6Destruction Catalyst&r.",
              "",
              "Er lädt sich mit Schwarzpulver aus dem Inventar, bis zu &e250&r, und jeder Rechtsklick kostet &e3&r. Dann sprengt er einen Würfel aus gewöhnlichen Blöcken wie Erde, Kies, Bruchstein und Stein frei, ohne Drops. Erze und alles andere bleiben stehen.",
              "",
              "&eTipp:&r Ideal, um Erzadern freizulegen, ohne das Inventar mit Bruchstein zu füllen.",
          ],
          tasks=[task_item("reliquary:destruction_catalyst", 1)],
          rewards=[reward_item("minecraft:gunpowder", 32), reward_xp(8)],
          deps=["void_tear"], icon="reliquary:destruction_catalyst", optional=True),

    quest("mortar", 9.8, 6.2, "&dMahl eine Potion Essence",
          subtitle="Reliquarys eigene Tränke.",
          description=[
              "Der &6Apothecary Mortar&r ist Catalyzing Gland, Quarzblock, Catalyzing Gland oben, Quarzblock, Catalyzing Gland, Quarzblock in der Mitte und drei Quarzblöcke unten. Darin mahlst du zwei oder drei Zutaten zu einer &6Potion Essence&r.",
              "",
              "Jede Zutat trägt passive Wirkungen. Haben zwei Zutaten eine Wirkung gemeinsam, steckt sie in der Essenz: &6Zucker&r (Tempo, Eile) und &6Goldklumpen&r (Stärke, Eile) ergeben Eile.",
              "",
              "Gebraut wird im &6Apothecary Cauldron&r (Hexerei-Mischkessel mit Reliquary-Teilen): Feuer darunter, Wasser hinein, Essenz und Netherwarze dazu, abfüllen mit &6Condensed Potion Vials&r aus Glasscheiben. Bis zu 3 Redstone verlängern, bis zu 2 Glowstone verstärken.",
          ],
          tasks=[task_item("reliquary:apothecary_mortar", 1)],
          rewards=[reward_item("minecraft:quartz", 16), reward_xp(5)],
          deps=["altar", "catalyzing_gland"], icon="reliquary:apothecary_mortar", optional=True),

    quest("glowing_water", 10.4, 6.8, "&eFüll Glowing Water ab",
          subtitle="Wurfwasser gegen Untote.",
          description=[
              "Eine &6Condensed Potion Vial&r (fünf Glasscheiben), ein &6Wassereimer&r, &6Leuchtsteinstaub&r, &6Schwarzpulver&r und &6Netherwarze&r formlos ergeben &6Glowing Water&r.",
              "",
              "Geworfen trifft es alle Untoten im Umkreis wie ein Wurftrank. Zombies, Skelette und Zombifizierte Piglins fallen schnell.",
              "",
              "&eAuch gut:&r Drei Brote plus Glowing Water ergeben drei &6Glowing Bread&r, das den Hunger auf einen Bissen ganz füllt. Mit Goldklumpen, TNT und Catalyzing Gland werden daraus vier &6Holy Hand Grenades&r.",
          ],
          tasks=[task_item("reliquary:glowing_water", 2)],
          rewards=[reward_item("minecraft:glowstone_dust", 16), reward_xp(5)],
          deps=["mortar"], icon="reliquary:glowing_water", optional=True),

    # ---- Waffen ----------------------------------------------------------------------
    quest("handgun", 14.0, 5.0, "&7Bau den Hunter's Handgun",
          subtitle="Eine Pistole aus Monsterteilen.",
          description=[
              "Drei Teile, alle mit Eisen: &6Barrel Assembly&r (zwei Nebulous Hearts, Magmacreme), &6Hammer Assembly&r (Steinknopf, Lohenrute, Molten Core) und &6Grip Assembly&r (Magmacreme, leeres Magazin). Mit Eisen und einer &6Slime Pearl&r wird daraus der &6Hunter's Handgun&r.",
              "",
              "Munition: Feuerstein, zwei Goldklumpen und Schwarzpulver ergeben 8 &6Neutral Shots&r. Acht davon um ein &6Empty Magazine&r (Eisen, Glas, Stein) ergeben ein volles Magazin.",
              "",
              "Rechtsklick schießt, Rechtsklick halten lädt nach. Rückstoß, Nachladen und Feuerrate werden mit deinem Erfahrungslevel besser, ab Level &e20&r ist das Maximum erreicht.",
          ],
          tasks=[task_item("reliquary:handgun", 1), task_item("reliquary:magazines/neutral_magazine", 1)],
          rewards=[reward_table("s2_common"), reward_item("minecraft:gunpowder", 16), reward_xp(8)],
          deps=["molten_core", "nebulous_heart"], icon="reliquary:handgun"),

    quest("seeker_magazine", 16.0, 5.0, "&9Lade Seeker Shots",
          subtitle="Munition, die ihr Ziel selbst findet.",
          description=[
              "&6Lapislazuli&r, zwei Goldklumpen und Schwarzpulver ergeben 8 &6Seeker Shots&r. Sie fliegen dem nächsten Gegner hinterher, daneben schießen ist kaum möglich.",
              "",
              "Weitere Sorten: &6Exorcism Shots&r (8 Neutral Shots und ein Zombie Heart) machen gewaltigen Schaden an Untoten, &6Blaze Shots&r (Lohenpulver, Lohenrute, zwei Goldklumpen) setzen in Brand, helfen aber nicht gegen feuerfeste Gegner.",
              "",
              "&eTipp:&r Leere Hülsen bleiben nach dem Schuss übrig, sammle sie auf.",
          ],
          tasks=[task_item("reliquary:magazines/seeker_magazine", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16), reward_xp(5)],
          deps=["handgun"], icon="reliquary:magazines/seeker_magazine", optional=True),

    quest("ice_magus_rod", 14.0, 7.0, "&bBau einen Ice Magus Rod",
          subtitle="Schneebälle, die wirklich wehtun.",
          description=[
              "Den &6Frozen Core&r lässt ein &fSchneegolem&r fallen, also bau einen und erschlag ihn. Diamant und Frozen Core oben, &6Void Tear&r und Diamant in der Mitte, Eisen unten links ergeben den &6Ice Magus Rod&r.",
              "",
              "Shift-Rechtsklick saugt bis zu &e250 Schneebälle&r aus dem Inventar. Jeder Schuss macht &d2&r Schaden, &d+2&r gegen feuerfeste Mobs und &d+4&r gegen Blazes. Für den Nether genau richtig.",
          ],
          tasks=[task_item("reliquary:ice_magus_rod", 1)],
          rewards=[reward_item("minecraft:snowball", 16), reward_xp(5)],
          deps=["void_tear"], icon="reliquary:ice_magus_rod"),

    quest("glacial_staff", 16.0, 7.0, "&bSteig auf den Glacial Staff um",
          subtitle="Wasser und Lava gefrieren unter dir.",
          description=[
              "Erst die &6Shears of Winter&r: Frozen Core, Schere und zwei Diamanten formlos. Rechtsklick halten schert Schafe und reißt Laub im Umkreis ab.",
              "",
              "Ice Magus Rod, Void Tear, Frozen Core und Shears of Winter formlos ergeben den &6Glacial Staff&r. Er schießt stärkere Schneebälle (&d3&r Schaden, &d+3&r gegen feuerfeste Mobs, &d+6&r gegen Blazes) und macht unter dir Wasser zu Packeis und Lava zu Obsidian.",
              "",
              "Die Blöcke tauen wieder auf, sobald du weit genug weg bist. Über Lavaseen im Nether läufst du damit trocken.",
          ],
          tasks=[task_item("reliquary:glacial_staff", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["ice_magus_rod"], icon="reliquary:glacial_staff", optional=True),
]

images = [
    banner("reliquary/title", "Reliquary", 5.0, -5.0, height=1.8, kind="title", colour="magic"),
    banner("reliquary/tropfen", "Die Tropfen", 4.8, -3.0, height=0.9, colour="magic"),
    banner("reliquary/schutz", "Schutz", 1.0, 3.0, height=0.9, colour="nature"),
    banner("reliquary/werkzeug", "Werkzeug", 7.0, 3.0, height=0.9, colour="brass"),
    banner("reliquary/waffen", "Waffen", 15.0, 3.0, height=0.9, colour="fire"),
]

chapter(C, "Reliquary", "reliquary:void_tear", "magic", quests, shape="circle", order=51, stage=2,
        subtitle=["Stufe 2. Seltene Tropfen, Mob Charms, Stäbe und die Void Tear."], images=images)
