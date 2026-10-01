"""Occultism in stage 3: the Afrit and Marid binding books, the infused pickaxe and iesnium,
spirit miners and the dimensional mineshaft, orange chalk and the unbound Afrit for afrit
essence (the stage 3 magic goal), red chalk, Abras' Conjure and the Afrit workers, Sevira's
Permanent Confinement, the magic storage, black chalk and the unbound Marid. The Marid miner
and smelter need dragon's breath and wait for stage 4. Continues occultism.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "occultism_afrit"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Iesnium --------------------------------------------------------------------
    quest("afrit_book", 0, 0, "&cBook of Binding: Afrit",
          subtitle="Ein Name, der brennt.",
          description=[
              "Mit &6Stufe 3&r öffnen die beiden höchsten Geisterklassen, die du rufen kannst: die &cAfrit&r und die &9Marid&r. Afrit stellen die großen Artefakte her und arbeiten schneller als jeder Djinni. Marid sind die stärksten Geister überhaupt, und das Dictionary rät, sie nur in Gruppen zu rufen.",
              "",
              "Das Bindungsbuch für einen Afrit entsteht wie die alten: &6Taboo Book&r, &6Purified Ink&r und &6Awakened Feather&r, diesmal mit &e4 gelbem Farbstoff&r. Danach craftest du es zusammen mit dem &6Dictionary of Spirits&r, das einen wahren Namen hineinschreibt.",
              "",
              pic("occultism:book_of_binding_bound_afrit"),
              "",
              "&eKronwerke:&r Das Magieziel von Stufe 3 will &e150 Afrit-Essenzen&r. Jede einzelne ist ein Afrit, den jemand gerufen und besiegt hat. Dazu stecken zwei Essenzen in jedem &dElfenstern&r.",
          ],
          tasks=[task_item("occultism:book_of_binding_bound_afrit", 2)],
          rewards=[reward_item("minecraft:yellow_dye", 8), reward_table("s3_common")],
          icon="occultism:book_of_binding_bound_afrit", size=2.0, shape="hexagon"),

    quest("infused_pickaxe", 2.6, 0, "&6Infused Pickaxe",
          subtitle="Ein Djinni im Edelstein bricht, was keine Spitzhacke bricht.",
          description=[
              "&6Iesnium&r, das Metall der Afrit, lässt sich mit keiner normalen Spitzhacke abbauen. Der erste Weg ist die &6Infused Pickaxe&r.",
              "",
              "&e1.&r Drei &dSpirit Attuned Gems&r in einer Reihe ergeben einen &6Spirit Attuned Pickaxe Head&r. Die Edelsteine bekommst du, wenn du Diamanten in Spiritfire wirfst.",
              "&e2.&r In &5Strigeor's Higher Binding&r legst du den Kopf, &e2 Stöcke&r und &e2 Silberbarren&r in die Schalen und startest mit einem gebundenen Djinni-Buch.",
              "",
              "Die Spitzhacke ist sehr zerbrechlich. Sie soll nur das erste Iesnium holen, aus dem du dir eine haltbare &6Iesnium Pickaxe&r baust.",
          ],
          tasks=[task_item("occultism:infused_pickaxe", 1)],
          rewards=[reward_item("minecraft:diamond", 3), reward_xp(5)],
          deps=["afrit_book"], icon="occultism:infused_pickaxe"),

    quest("iesnium", 5.2, 0, "&6Iesnium",
          subtitle="Ein Erz, das wie Netherrack aussieht.",
          description=[
              "&6Iesnium-Erz&r liegt im &cNether&r und sieht für das bloße Auge aus wie Netherrack. Sehen kannst du es nur, wenn du die &6Otherworld Goggles&r trägst.",
              "",
              "&eSo findest du es:&r Klick schleichend mit der &6Divination Rod&r auf Netherrack, dann ist sie auf Iesnium eingestellt. Halt Rechtsklick gedrückt, bis die Rute fertig ist: der nächste Fund leuchtet durch die Wände. Je mehr Violett an den Kristallen, desto näher.",
              "",
              "&eDie Brille:&r Eine &6Spirit Attuned Gem&r in 8 Glasscheiben ergibt Linsen. In &5Eziveus' Spectral Compulsion&r mit 2 Silberbarren, einem Goldbarren und dem Foliot-Buch werden sie zu &6Infused Lenses&r. Mit einem Linsenrahmen (Otherstone und Silber) und 2 Leder ist die Brille fertig.",
              "",
              "Abgebaut gibt das Erz &6Raw Iesnium&r, das du zu Barren schmilzt. Drei Barren und zwei Stöcke ergeben die &6Iesnium Pickaxe&r, die nicht mehr kaputtgeht.",
          ],
          tasks=[task_item("occultism:iesnium_ingot", 12)],
          rewards=[reward_item("minecraft:netherrack", 32), reward_table("s3_common")],
          deps=["infused_pickaxe"], icon="occultism:iesnium_ingot", size=1.5, shape="square"),

    quest("mineshaft", 7.8, 0, "&6Dimensional Mineshaft",
          subtitle="Geister, die für dich ins Bergwerk gehen.",
          description=[
              "Geister können in einer eigenen Bergbau-Dimension für dich graben, ganz ohne Lag. Du brauchst dafür drei Dinge:",
              "",
              "&e1.&r Eine &6Magic Lamp&r (Silber um einen Spirit Attuned Gem). In Eziveus' Spectral Compulsion wird sie mit einer Iesnium Pickaxe, einem Eisenbarren und Kies zum &dFoliot Miner&r.",
              "&e2.&r In Strigeor's Higher Binding wird daraus mit einer weiteren Iesnium Pickaxe, einem Goldbarren, Lapis und einem &dSpirit Attuned Crystal&r (vier Gems im Quadrat) der &dDjinni Miner&r. Er holt gezielt Erze.",
              "&e3.&r Der &6Dimensional Mineshaft&r selbst, ebenfalls in Strigeor's: 4 Otherstone, ein Goldbarren, ein Iesniumblock und ein Spirit Attuned Crystal.",
              "",
              "Die Lampe kommt oben in den Mineshaft, die Erze kommen unten heraus. Leer ihn regelmäßig mit einem Trichter, sonst wirft er Funde weg. Die Lampe nutzt sich ab.",
          ],
          tasks=[task_item("occultism:dimensional_mineshaft", 1), task_item("occultism:miner_djinni_ores", 1)],
          rewards=[reward_item("occultism:iesnium_ingot", 3), reward_xp(10)],
          deps=["iesnium"], icon="occultism:dimensional_mineshaft"),

    quest("storage", 7.8, -2.2, "&6Magischer Speicher",
          subtitle="Ein Lager in einer eigenen Dimension.",
          description=[
              "Der &6Storage Actuator&r von Occultism ist ein Lager für sehr viele Items in einem Block. Er besteht aus zwei Teilen:",
              "",
              "&e1.&r Die &6Dimensional Matrix&r: 3 Quarzblöcke und eine Enderperle in Strigeor's Higher Binding mit dem Djinni-Buch.",
              "&e2.&r Die &6Storage Actuator Base&r: ein Otherstone-Sockel, 2 Kupferbarren und ein Goldbarren in Eziveus' Spectral Compulsion mit dem Foliot-Buch.",
              "",
              "Die Matrix über die Basis an der Werkbank, fertig. Er fasst &e128 Itemsorten&r und &e256 000 Items&r. &6Storage Stabilizers&r im Umkreis von 5 Blöcken, die auf die Matrix zeigen, machen ihn größer. Den Stabilisator Tier 3 bindest du mit einem Afrit (Goldblock, Totem, Spirit Attuned Crystal, Afrit-Essenz), er fasst 256 weitere Sorten.",
          ],
          tasks=[task_item("occultism:storage_controller", 1)],
          rewards=[reward_item("minecraft:quartz_block", 8), reward_xp(5)],
          deps=["mineshaft"], icon="occultism:storage_controller", optional=True),

    # ---- Afrit-Essenz ------------------------------------------------------------------
    quest("orange_chalk", 2.6, 3, "&6Orange Chalk",
          subtitle="Süß und warm: ein Köder für Afrit.",
          description=[
              "Afrit lassen sich von Limettenkreide beeindrucken, folgen ihr aber nicht. Sie brauchen &6Orange Chalk&r.",
              "",
              "&6Impure White Chalk&r mit &6Cursed Honey&r, &6Leuchtbeeren&r und &6Lohenstaub&r ergibt unreine orange Kreide, Spiritfire macht sie rein.",
              "",
              "&eCursed Honey&r gibt es nur von einer &5Possessed Bee&r: In &5Ihagan's Enthrallment&r legst du Honigwabe, Honigblock, Honigflasche und Honigwabenblock in die Schalen, startest mit dem Djinni-Buch und opferst ein &eHuhn&r. Die Biene ist giftig und ruft Verstärkung, also mit Rüstung kommen.",
              "",
              "&eTipp:&r Das nächste Pentakel braucht 40 orange Zeichen. Mach gleich mehrere Stück Kreide.",
          ],
          tasks=[task_item("occultism:chalk_orange", 3)],
          rewards=[reward_item("minecraft:glow_berries", 16)],
          deps=["afrit_book"], icon="occultism:chalk_orange"),

    quest("kandar", 5.2, 3, "&5Kandar's Open Conjure",
          subtitle="Ein absichtlich unvollständiges Pentakel.",
          description=[
              "&5Kandar's Open Conjure&r ruft einen Afrit, ohne ihn zu binden. Es braucht keine rote Kreide, kann den Afrit dafür aber auch nicht kontrollieren. Er kommt nur, um zu kämpfen.",
              "",
              "Das Pentakel auf 17x17 Blöcken: &e40 orange&r und &e36 limettengrüne&r Zeichen, &e16 Fundamentzeichen&r (Weiß, Hellgrau, Grau oder Schwarz), &e8 dunkle Fundamentzeichen&r (Grau oder Schwarz), &e8 Skelettschädel&r und &e8 Kerzen&r.",
              "",
              "&6Graue Kreide&r ist unreine weiße Kreide mit &6Gray Paste&r aus Strigeor's Higher Binding.",
              "",
              "&eTipp:&r Lass die Vorschau aus dem Dictionary in der Welt stehen und zeichne mit der Apprentice Ritual Satchel nach. Zeichen für Zeichen geht es so viel schneller.",
          ],
          tasks=[task_checkmark("Pentakel gezeichnet")],
          rewards=[reward_item("occultism:large_candle", 8), reward_xp(5)],
          deps=["orange_chalk"], icon="minecraft:skeleton_skull"),

    quest("unbound_afrit", 7.8, 3, "&cUnbound Afrit",
          subtitle="Ruf ihn, besieg ihn, nimm seine Essenz.",
          description=[
              "In die Schalen kommen &eNetherrack&r, ein &6Iesniumbarren&r, ein &eFeuerzeug&r und &eSchwarzpulver&r. Klick mit dem gebundenen Afrit-Buch auf die goldene Schale, und wenn die grauen Partikel erscheinen, opferst du eine &eKuh&r in der Nähe.",
              "",
              "Dann steht ein ungebundener &cAfrit&r vor dir, und er ist wütend. Er ist ein Feuergeist, also helfen &eFeuerresistenz&r, gute Rüstung und Freunde. Besiegt lässt er &cAfrit-Essenz&r fallen.",
              "",
              pic("occultism:afrit_essence"),
              "",
              "Jeder besiegte Afrit lässt mindestens eine Essenz fallen. Mit &ePlünderung&r auf der Waffe sind es oft mehr, mit Plünderung III bis zu vier.",
          ],
          tasks=[task_item("occultism:afrit_essence", 1)],
          rewards=[reward_item("minecraft:magma_cream", 4),
                   reward_table("s3_uncommon")],
          deps=["kandar", "iesnium"], icon="occultism:afrit_essence", size=1.75, shape="diamond"),

    quest("essence_line", 7.8, 6, "&cAfrit-Essenz für den Obelisken",
          subtitle="Hundertfünfzig Essenzen für den Server.",
          description=[
              "&eKronwerke:&r Das Ziel will &e150 Afrit-Essenzen&r (die Menge passt sich der Spielerzahl an), dazu je zwei für die acht &dElfensterne&r. Hinter jeder Essenz steht ein gerufener und besiegter Afrit. Das ist Arbeit für viele.",
              "",
              "&eWas hilft:&r",
              "&e1.&r Eine &eKuhfarm&r direkt neben dem Pentakel. Jeder Ruf kostet eine Kuh.",
              "&e2.&r Ein Iesniumbarren pro Ruf. Ein Djinni Crusher verdreifacht dein Iesnium-Erz, ein Afrit Crusher vervierfacht es.",
              "&e3.&r Eine Waffe mit &ePlünderung III&r. Sie bringt pro Kampf bis zu drei Essenzen zusätzlich.",
              "&e4.&r Ein fest aufgebautes Pentakel, das stehen bleibt. Wer kämpft, wechselt sich ab.",
              "",
              "Bring die Essenzen zum &6Obelisken&r an der Spawn, per Rechtsklick oder über eine Truhe daneben.",
          ],
          tasks=[task_item("occultism:afrit_essence", 16)],
          rewards=[reward_item("occultism:iesnium_ingot", 8), reward_table("s3_uncommon")],
          deps=["unbound_afrit"], icon="occultism:afrit_essence"),

    # ---- Gebundene Afrit -------------------------------------------------------------------
    quest("red_chalk", 10.4, 3, "&cRed Chalk",
          subtitle="Kreide aus der Essenz der Afrit selbst.",
          description=[
              "&6Impure White Chalk&r mit einer &cAfrit-Essenz&r, einer &6Fackellilie&r und &6Redstone&r ergibt unreine rote Kreide. Spiritfire reinigt sie.",
              "",
              "Die &6Fackellilie&r wächst aus Fackellilien-Samen, die der &eSchnüffler&r ausgräbt. Ein Schnüffler-Ei findest du in verdächtigem Sand in Ozeanruinen. Pflanz die Samen gleich an, du wirst viele brauchen.",
              "",
              "Rote Kreide verbindet ihre Zeichen direkt mit den Afrit. Erst mit ihr kannst du einen Afrit &egebunden&r rufen, der für dich arbeitet.",
          ],
          tasks=[task_item("occultism:chalk_red", 2)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["unbound_afrit"], icon="occultism:chalk_red"),

    quest("abras", 13, 3, "&5Abras' Conjure: Afrit Crusher",
          subtitle="Ein Erz, vier Staub.",
          description=[
              "&5Abras' Conjure&r ruft einen gebundenen Afrit. Es ist Kandar's Pentakel mit &e16 roten&r Zeichen dazu und &e4 Spirit Attuned Crystals&r: 40 orange, 16 rot, 36 limettengrün, 16 Fundament, 8 dunkles Fundament, 8 Skelettschädel, 8 Kerzen.",
              "",
              "Der &dAfrit Crusher&r: &6Iesnium-&r, &6Smaragd-&r, &6Lapis-&r, &6Amethyst-&r und &6Obsidianstaub&r in die Schalen, Afrit-Buch auf die Schale. Er macht aus &eeinem Erz vier Staub&r und ist schneller als der Djinni.",
              "",
              "Im selben Pentakel: der &dAfrit Smelter&r (Lohenrute, Lavaeimer, Magmablock, rote Netherziegel, Seelenlagerfeuer), der in einem Zehntel der Zeit schmilzt, der &dAfrit Crystallizer&r und zwei Wettergeister: &eRegen&r (Sand, getrockneter Seetang, Kaktus, toter Busch, eine Kuh als Opfer) und &eGewitter&r (Knochen, 2 Schwarzpulver, Ghast-Träne, eine Kuh).",
          ],
          tasks=[task_checkmark("Afrit Crusher beschworen")],
          rewards=[reward_item("minecraft:raw_iron", 32), reward_table("s3_uncommon"), reward_xp(10)],
          deps=["red_chalk"], icon="occultism:book_of_binding_afrit"),

    quest("afrit_miner", 10.4, 0, "&dAfrit Miner",
          subtitle="Tiefer graben, schneller, mit weniger Verschleiß.",
          description=[
              "Afrit bindest du in Gegenstände mit &5Sevira's Permanent Confinement&r: &e60 violette&r, &e20 limettengrüne&r, &e16 orange&r und &e12 rote&r Zeichen, &e8 Fundament&r, &e8 dunkles Fundament&r, &e8 Spirit Attuned Crystals&r, &e8 Skelettschädel&r und &e8 Kerzen&r.",
              "",
              "Der &dAfrit Miner&r entsteht darin aus deinem &dDjinni Miner&r, einer Iesnium Pickaxe, einem Spirit Attuned Crystal, einer &cAfrit-Essenz&r, einem &eEchosplitter&r und &eWeinendem Obsidian&r. Er gräbt schneller, findet auch Tiefenschiefer-Erze und nutzt die Lampe langsamer ab.",
              "",
              "Den Echosplitter findest du in den Truhen der Antiken Städte tief unter der Erde.",
          ],
          tasks=[task_item("occultism:miner_afrit_deeps", 1)],
          rewards=[reward_item("minecraft:crying_obsidian", 4), reward_xp(10)],
          deps=["mineshaft", "red_chalk"], icon="occultism:miner_afrit_deeps"),

    quest("satchel", 13, 0, "&6Artisanal Ritual Satchel",
          subtitle="Ein ganzes Pentakel mit einem Klick.",
          description=[
              "Lege in Sevira's Permanent Confinement deine &6Apprentice Ritual Satchel&r, eine &cAfrit-Essenz&r und &e4 Enderperlen&r in die Schalen. Der Inhalt der alten Tasche bleibt erhalten.",
              "",
              "Der Afrit in der neuen Tasche zeichnet das ganze Pentakel auf einmal, sobald alle Kreiden, Kerzen, Kristalle und Schädel darin liegen. Ein Rechtsklick mit der Tasche auf die goldene Schale eines fertigen Pentakels räumt alles wieder ein.",
              "",
              "&eTipp:&r Bei 17x17 großen Pentakeln wie Kandar's spart das jedes Mal Minuten. Gerade für die vielen Afrit-Rufe lohnt sie sich.",
          ],
          tasks=[task_item("occultism:ritual_satchel_t2", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 8)],
          deps=["afrit_miner"], icon="occultism:ritual_satchel_t2", optional=True),

    # ---- Marid ---------------------------------------------------------------------------
    quest("black_chalk", 10.4, 6, "&8Black Chalk",
          subtitle="Das härteste Fundament.",
          description=[
              "Marid brauchen &8Black Chalk&r. Zuerst stellst du in &5Sevira's Permanent Confinement&r mit dem Afrit-Buch &6Witherite Dust&r her: &6Netheritstaub&r, ein &6Witherskelettschädel&r, &6Schwarzsteinstaub&r und eine &6Wither-Rose&r ergeben drei Staub.",
              "",
              "Netheritstaub und Schwarzsteinstaub macht dein Crusher aus einem Netheritbarren und aus Schwarzstein. Wither-Rosen wachsen dort, wo der Wither etwas getötet hat.",
              "",
              "&6Impure White Chalk&r mit &e3 Witherite Dust&r ergibt unreine schwarze Kreide, Spiritfire reinigt sie. Schwarze Kreide zählt überall als Fundament, auch dort, wo kein Weiß erlaubt ist.",
          ],
          tasks=[task_item("occultism:chalk_black", 1)],
          rewards=[reward_item("minecraft:wither_rose", 2), reward_xp(5)],
          deps=["red_chalk"], icon="occultism:chalk_black"),

    quest("unbound_marid", 13, 6, "&9Unbound Marid",
          subtitle="Der stärkste Geist, den du rufen kannst.",
          description=[
              "Das Bindungsbuch für Marid entsteht wie das der Afrit, mit &e4 grünem Farbstoff&r.",
              "",
              "Das Pentakel ist &5Tibira's Attraction&r: &e40 orange&r, &e16 rote&r und &e36 limettengrüne&r Zeichen, &e8 schwarze&r, &e16 Fundament&r, &e4 Witherskelettschädel&r, &e8 Skelettschädel&r, &e4 Spirit Attuned Crystals&r und &e8 Kerzen&r.",
              "",
              "In die Schalen: ein &bAquisitor&r (Conduit), &bPrismarinkristalle&r, ein &bPrismarinsplitter&r und eine &fGhast-Träne&r. Nach dem Start benutzt du einen &bDreizack&r auf der goldenen Schale. Der Marid kommt aggressiv, und das Dictionary meint es ernst: Ruft ihn zu mehreren.",
              "",
              "Besiegt lässt er &9Marid-Essenz&r fallen, mit Plünderung mehr.",
          ],
          tasks=[task_item("occultism:marid_essence", 1)],
          rewards=[reward_item("minecraft:prismarine_crystals", 16), reward_table("s3_uncommon")],
          deps=["black_chalk"], icon="occultism:marid_essence"),

    quest("master", 15.6, 6, "&9Meister der Anderswelt",
          subtitle="Afrit arbeiten für dich, Marid hören auf deinen Namen.",
          description=[
              "Aus &9Marid-Essenz&r, unreiner weißer Kreide, &eLapisstaub&r und einer &eRöhrenkoralle&r entsteht &9Blue Chalk&r. Damit zeichnest du &5Fatma's Incentivized Attraction&r (21x21) und rufst gebundene Marid.",
              "",
              "Der &dMarid Crusher&r macht aus &eeinem Erz sechs Staub&r. Er will einen Diamantblock, einen Iesniumblock, einen Smaragdblock, einen Netheritblock und eine Ghast-Träne. &5Uphyxes Inverted Tower&r bindet Marid in Gegenstände, etwa den Speicher-Stabilisator der Stufe 4 oder den Iesnium-Amboss.",
              "",
              "Der Marid Miner und der Marid Smelter brauchen Drachenatem aus dem End. Die kommen in Stufe 4.",
              "",
              "&eKronwerke:&r Bis dahin zählt jede Afrit-Essenz. Halte das Pentakel bereit und ruf Afrit, so oft du kannst.",
          ],
          tasks=[task_item("occultism:chalk_blue", 1), task_item("occultism:afrit_essence", 8)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["unbound_marid", "abras"], icon="occultism:chalk_blue", size=2.5, shape="gear"),
]

images = [
    banner("occultism_afrit/title", "Occultism: Afrit und Marid", 7.8, -4.6, height=1.8, kind="title", colour="fire"),
    banner("occultism_afrit/iesnium", "Iesnium", 2.6, -1.6, height=0.9, colour="magic"),
    banner("occultism_afrit/essenz", "Afrit-Essenz", -0.5, 3.0, height=0.9, colour="fire"),
    banner("occultism_afrit/gebunden", "Gebundene Afrit", 13, -1.6, height=0.9, colour="fire"),
    banner("occultism_afrit/marid", "Marid", 12.4, 4.5, height=0.9, colour="water"),
]

chapter(C, "Occultism: Afrit und Marid", "occultism:afrit_essence", "magic", quests, shape="circle", order=26,
        stage=3, subtitle=["Stufe 3. Iesnium, Afrit-Essenz, gebundene Afrit und die Marid."], images=images)
