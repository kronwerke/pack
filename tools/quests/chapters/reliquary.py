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
              "Vier &6Fertile Essence&r in die Ecken, vier &6Netherstern&r an die Seiten, ein &6Rosenstrauch&r in die Mitte ergeben die &6Witherless Rose&r. Fertile Essence ist Rib Bone, Catalyzing Gland, grüner Farbstoff und Slime Pearl in der Werkbank.",
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
          deps=["slime_pearl"], icon="reliquary:lantern_of_paranoia"),

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
]

images = [
    banner("reliquary/title", "Reliquary", 5.0, -5.0, height=1.8, kind="title", colour="magic"),
    banner("reliquary/tropfen", "Die Tropfen", 4.8, -3.0, height=0.9, colour="magic"),
    banner("reliquary/schutz", "Schutz", 1.0, 3.0, height=0.9, colour="nature"),
    banner("reliquary/werkzeug", "Werkzeug", 7.0, 3.0, height=0.9, colour="brass"),
]

chapter(C, "Reliquary", "reliquary:void_tear", "magic", quests, shape="circle", order=51, stage=2,
        subtitle=["Stufe 2. Seltene Tropfen, Mob Charms, Stäbe und die Void Tear."], images=images)
