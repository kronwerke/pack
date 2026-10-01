"""Eidolon Repraised in stage 3 (the whole mod opens with stage 3): the Ars Ecclesia codex,
pewter, the crucible, the brazier rituals and soul shards, arcane gold and the lesser soul gem,
altars, effigies, signs from the witch, prayers, the goblet sacrifice, the worktable, the unholy
symbol, the stone altar and elder statue, the reaper scythe and the soul enchanter."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "eidolon"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Pewter und Seelen -----------------------------------------------------
    quest("welcome", 0, 0, "&5Ars Ecclesia",
          subtitle="Ein Buch über Seelen, Götter und Untote.",
          description=[
              "&5Eidolon&r ist düstere Magie: Seelensplitter aus Untoten, Rituale an der Feuerschale, Gebete an einem Altar und am Ende Werkzeuge, die Seelen ernten. Die ganze Mod öffnet mit &6Stufe 3&r.",
              "",
              "Dein Handbuch ist die &6Ars Ecclesia&r, formlos aus einem &6Buch&r und &6verrottetem Fleisch&r. Darin stehen alle Rezepte, und im Kapitel &eSigns&r singst du später deine Gesänge.",
              "",
              pic("eidolon_repraised:codex"),
              "",
              "Pass gut auf das Buch auf. Es wird im Lauf der Zeit selbst zu einem Teil deiner Magie.",
          ],
          tasks=[task_item("eidolon_repraised:codex", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 16), reward_xp(5)],
          icon="eidolon_repraised:codex", size=2.0, shape="hexagon"),

    quest("pewter", 2.2, 0, "&7Pewter",
          subtitle="Ein Metall, das Magie nicht stört.",
          description=[
              "&7Pewter&r ist eine Bleilegierung, völlig träge gegenüber Magie. Darum baut Eidolon fast alle Geräte daraus.",
              "",
              "Ein &6Bleibarren&r und ein &6Eisenbarren&r ergeben formlos &e2 Pewter Blend&r, die du im Ofen zu Barren schmilzt. Welches Blei du nimmst, ist egal: das von Eidolon, Mekanism oder aus der Bergbau-Dimension zählt alles.",
          ],
          tasks=[task_item("eidolon_repraised:pewter_ingot", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["welcome"], icon="eidolon_repraised:pewter_ingot"),

    quest("crucible", 4.4, -1, "&6Crucible",
          subtitle="Alchemie in mehreren Schritten.",
          description=[
              "Der &6Crucible&r ist ein Kessel aus &e7 Pewter&r. Stell ihn über eine Wärmequelle wie ein Lagerfeuer, füll ihn mit Wasser und warte, bis es kocht.",
              "",
              "Rezepte haben mehrere Schritte. Wirf die Zutaten des ersten Schritts hinein, und sobald sich die Farbe des Wassers ändert, kommt der nächste Schritt. Steht bei einem Schritt \"stir\", rührst du mit Rechtsklick und leerer Hand so oft wie angegeben.",
              "",
              "Ein einfacher Anfang ist &6Sulfur&r: Kohle und &6Enchanted Ash&r in einem Schritt. Enchanted Ash schmilzt du im Ofen aus Knochen.",
          ],
          tasks=[task_item("eidolon_repraised:crucible", 1)],
          rewards=[reward_item("minecraft:bone", 16), reward_xp(3)],
          deps=["pewter"], icon="eidolon_repraised:crucible"),

    quest("brazier", 4.4, 1.2, "&6Brazier und Stone Hands",
          subtitle="Der Ort für Rituale.",
          description=[
              "Die &6Brazier&r ist eine Feuerschale aus &e3 Pewter&r, einem &6Kohleblock&r und zwei Stöcken. Jedes Ritual beginnt so: Ein Item oben auf die Brazier legen und sie mit einem &6Feuerzeug&r anzünden. Mit leerer Hand löschst du sie wieder und beendest damit laufende Rituale.",
              "",
              "Weitere Zutaten liegen auf &6Stone Hands&r (Steinstufen und Stein) rund um die Brazier. Manche Rituale wollen ein Item in einem &6Necrotic Focus&r, das steht dann auf der Ritualseite.",
          ],
          tasks=[task_item("eidolon_repraised:brazier", 1), task_item("eidolon_repraised:stone_hand", 4)],
          rewards=[reward_item("minecraft:flint_and_steel", 1)],
          deps=["pewter"], icon="eidolon_repraised:brazier"),

    quest("soul_shard", 6.6, 1.2, "&dSoul Shards",
          subtitle="Kristallisierte Seelen.",
          description=[
              "Das erste Ritual ist die &5Crystallization&r: &6Knochenmehl&r auf die Brazier, je ein &6Redstone&r auf zwei Stone Hands, anzünden. Wenn das Ritual seine letzte Zutat verbraucht, vernichtet es alle Untoten in der Nähe und lässt &dSoul Shards&r an ihrer Stelle zurück.",
              "",
              "Du brauchst also Untote in Reichweite. Bau die Brazier nachts im Freien auf, oder fang ein paar Zombies in einer Grube daneben.",
              "",
              "Soul Shards brauchst du ab jetzt überall: für Arcane Gold, Seelensteine, den Stone Altar und weitere Rituale.",
          ],
          tasks=[task_item("eidolon_repraised:soul_shard", 8)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["brazier"], icon="eidolon_repraised:soul_shard"),

    quest("alchemy", 8.8, 0, "&6Arcane Gold und Soul Gem",
          subtitle="Zwei Rezepte für den Kessel.",
          description=[
              "&6Arcane Gold&r: zuerst &e2 Redstone&r und einen &6Soul Shard&r in den kochenden Crucible, dann &e2 Goldbarren&r. Heraus kommen zwei Barren Arcane Gold, stabiler und magisch leitfähiger als normales Gold.",
              "",
              "&6Lesser Soul Gem&r: &e2 Redstone&r und &e2 Lapis&r, dann &e4 Soul Shards&r und zweimal rühren, zum Schluss ein &6Quarz&r. Der Seelenstein steckt in Gürteln, Zauberstäben und anderen besseren Gegenständen.",
          ],
          tasks=[task_item("eidolon_repraised:arcane_gold_ingot", 6), task_item("eidolon_repraised:lesser_soul_gem", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["crucible", "soul_shard"], icon="eidolon_repraised:arcane_gold_ingot"),

    # ---- Altar und Gebet ---------------------------------------------------------
    quest("altar", 0.5, 5.5, "&6Altar und Straw Effigy",
          subtitle="Ein Ort, an dem man dich hört.",
          description=[
              "Ein &6Wooden Altar&r (Holzstufen über Brettern, ergibt drei) kann jede Form und Größe haben. Oben drauf gehört ein Bildnis, für den Anfang die &6Straw Effigy&r aus &e5 Weizen&r.",
              "",
              "Was du sonst noch auf den Altar stellst, macht ihn stärker. Kerzen und andere Lichter, Schädel von Untoten und seltene Kräuter im Topf erhöhen &ePower&r und &eCapacity&r. Pro Sorte zählt jeweils nur das beste Stück.",
          ],
          tasks=[task_item("eidolon_repraised:wooden_altar", 3), task_item("eidolon_repraised:straw_effigy", 1)],
          rewards=[reward_item("minecraft:candle", 4), reward_xp(3)],
          deps=["welcome"], icon="eidolon_repraised:straw_effigy"),

    quest("wicked_sign", 2.5, 5.5, "&5Das Wicked Sign",
          subtitle="Eine Hexe zeigt dir den Weg.",
          description=[
              "Gesänge bestehen aus &5Zeichen&r, und das erste lernst du von jemandem, der sich mit Magie auskennt. Wirf deinen Codex einer &5Hexe&r vor die Füße. Sie hebt ihn auf, schreibt das &5Wicked Sign&r hinein und gibt ihn dir zurück.",
              "",
              "Wer den Weg des Lichts gehen will, wirft das Buch stattdessen einem Kleriker zu und lernt das &eSacred Sign&r. Dieses Kapitel folgt dem dunklen Weg, der helle funktioniert genauso mit seinen eigenen Gesängen.",
              "",
              "&cAchtung:&r Hexen werfen Tränke. Trink vorher einen Heiltrank oder halt Abstand.",
          ],
          tasks=[task_checkmark("Wicked Sign gelernt")],
          rewards=[reward_item("minecraft:glass_bottle", 8), reward_xp(5)],
          deps=["altar"], icon="eidolon_repraised:unholy_symbol"),

    quest("prayer", 4.5, 5.5, "&5Dark Prayer",
          subtitle="Dreimal Wicked, einmal am Tag.",
          description=[
              "Öffne den Codex im Kapitel &eSigns&r, wähl dreimal das &5Wicked Sign&r und sing den Gesang vor deinem Altar mit Bildnis. Das ist das &5Dark Prayer&r an den dunklen Herrn.",
              "",
              "Jedes Gebet geht nur einmal am Tag, und jedes bringt dir etwas Gunst. Dein Patron gibt dir dafür &bMana&r, mit dem du Gesänge sprechen kannst. Wie viel du bekommst, hängt von der Power des Altars ab, wie viel du halten kannst, von seiner Capacity.",
              "",
              "Mit wachsender Gunst schenkt dir der Patron neue Zeichen, darunter &5Blood&r und &5Soul&r. Probier jeden neuen Ritus mindestens einmal aus, manchmal öffnet erst das die nächste Stufe.",
          ],
          tasks=[task_checkmark("Zum ersten Mal gebetet")],
          rewards=[reward_xp(5)],
          deps=["wicked_sign"], icon="eidolon_repraised:codex"),

    quest("goblet", 6.5, 5.5, "&cGoblet",
          subtitle="Blut für den dunklen Herrn.",
          description=[
              "Der &6Goblet&r besteht aus &e4 Arcane Gold&r. Stell ihn auf den Altar, das allein erhöht schon die Capacity um zwei.",
              "",
              "Töte ein Tier direkt über dem Kelch, dann füllt er sich mit Blut. Sing jetzt &5Wicked, Blood, Wicked&r vor dem Altar. Opfer sind dem Patron viel wert, gehen aber auch nur einmal am Tag.",
          ],
          tasks=[task_item("eidolon_repraised:goblet", 1),
                 task_advancement("eidolon_repraised:sacrifice", "Ein Tieropfer dargebracht")],
          rewards=[reward_item("minecraft:wheat", 32), reward_xp(5)],
          deps=["prayer", "alchemy"], icon="eidolon_repraised:goblet"),

    quest("worktable", 2.5, 7.7, "&6Worktable",
          subtitle="Eine Werkbank mit vier Extraplätzen.",
          description=[
              "Die &6Worktable&r ist eine &6Pewter Inlay&r über &e3 violettem Teppich&r und &e3 Brettern&r. Sie arbeitet wie eine normale Werkbank, hat aber vier zusätzliche Plätze für magische Zutaten. Viele bessere Rezepte von Eidolon gehen nur hier.",
              "",
              "Pewter Inlays craftest du aus vier Pewter-Barren im Kreis, du brauchst sie öfter.",
          ],
          tasks=[task_item("eidolon_repraised:worktable", 1)],
          rewards=[reward_item("eidolon_repraised:pewter_inlay", 4)],
          deps=["pewter"], icon="eidolon_repraised:worktable"),

    quest("unholy_symbol", 6.5, 7.7, "&5Unholy Symbol",
          subtitle="Touch of Darkness.",
          description=[
              "Sobald du das &5Soul Sign&r kennst, lernst du den Gesang &5Touch of Darkness&r: Wicked, Soul, Wicked, Soul. Sing ihn, während du auf ein Item am Boden schaust.",
              "",
              "Auf eine &6Pewter Inlay&r gesungen, wird daraus das &5Unholy Symbol&r, das Zeichen deines Patrons. Auf eine Waffe gesungen, macht sie eine Weile Wither-Schaden.",
              "",
              "Das Symbol ist die Zutat für die besseren Werkzeuge und für das Bildnis auf dem Stone Altar.",
          ],
          tasks=[task_item("eidolon_repraised:unholy_symbol", 2)],
          rewards=[reward_item("eidolon_repraised:pewter_inlay", 2), reward_xp(5)],
          deps=["goblet", "worktable"], icon="eidolon_repraised:unholy_symbol"),

    quest("stone_altar", 8.8, 6.6, "&5Stone Altar und Elder Statue",
          subtitle="Für die mächtigeren Riten.",
          description=[
              "Der &6Stone Altar&r kommt aus der Worktable: Glatte Steinstufen, Stein und eine Pewter Inlay, dazu ein &6Soul Shard&r in einem der Extraplätze. Er funktioniert wie der Holzaltar, erlaubt aber stärkere Riten.",
              "",
              "Statt der Strohfigur kommt die &6Elder Statue&r darauf, aus Stein und glattem Stein mit deinem &5Unholy Symbol&r und einer &6Gold Inlay&r in den Extraplätzen.",
              "",
              "Erst auf dem Stone Altar mit Elder Statue gehen die großen Riten: ein Dorfbewohner als Opfer oder einen Dorfbewohner in einen Zombie verwandeln. Der helle Weg heilt dort Zombie-Dorfbewohner.",
          ],
          tasks=[task_item("eidolon_repraised:stone_altar", 3), task_item("eidolon_repraised:unholy_effigy", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["unholy_symbol"], icon="eidolon_repraised:unholy_effigy", size=1.5, shape="diamond"),

    # ---- Werkzeuge ---------------------------------------------------------------
    quest("reaper_scythe", 0.5, 11.5, "&5Reaper Scythe",
          subtitle="Seelen ernten ohne Ritual.",
          description=[
              "Die &6Reaper Scythe&r entsteht an der Worktable aus &e3 Pewter&r und zwei Stöcken. In die Extraplätze kommen dein &5Unholy Symbol&r, zwei &6Tattered Cloth&r und ein &6Soul Shard&r.",
              "",
              "Tattered Cloth lassen &5Wraiths&r fallen, schwebende untote Geister. Ihre Krallen geben dir &bChilled&r, damit heilst du gar nicht mehr, solange der Effekt läuft.",
              "",
              "Was die Sense tötet, wenn es untot ist, hinterlässt keinen Körper, sondern Soul Shards. Viel bequemer als jedes Mal ein Ritual.",
          ],
          tasks=[task_item("eidolon_repraised:reaper_scythe", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(5)],
          deps=["unholy_symbol"], icon="eidolon_repraised:reaper_scythe"),

    quest("soul_enchanter", 2.5, 11.5, "&dSoul Enchanter",
          subtitle="Verzaubern ohne Glücksspiel.",
          description=[
              "Der &6Soul Enchanter&r kommt aus der Worktable: ein Buch, &e2 Arcane Gold&r und &e4 Obsidian&r, dazu &e2 Diamanten&r und &e2 Gold Inlays&r in den Extraplätzen.",
              "",
              "Er gibt immer genau eine Verzauberung auf Stufe I oder hebt eine vorhandene um eine Stufe an, auch auf bereits verzauberten Items. Dafür kostet jeder Schritt Level und Soul Shards. Langsam, aber du bestimmst, was draufkommt.",
          ],
          tasks=[task_item("eidolon_repraised:soul_enchanter", 1)],
          rewards=[reward_item("eidolon_repraised:soul_shard", 8), reward_xp(10)],
          deps=["worktable", "alchemy"], icon="eidolon_repraised:soul_enchanter"),

    # ---- Ziel --------------------------------------------------------------------
    quest("necromancer", 13, 6.5, "&5Diener des dunklen Herrn",
          subtitle="Gunst, Seelen und ein Schattenstein.",
          description=[
              "Du betest täglich, opferst im Kelch und erntest Seelen mit der Sense. Der nächste Schritt ist der &5Shadow Gem&r, der Kern der Zauberstäbe und des Wicked Weave für die Warlock-Rüstung.",
              "",
              "Rezept im Crucible: zuerst Kohle, dann eine &6Ghast Tear&r und &6Death Essence&r mit einmal Rühren, dann zwei Soul Shards und noch eine Death Essence mit einmal Rühren, zum Schluss ein Diamant. Death Essence kochst du aus einem &6Zombie Heart&r, das die stärkeren &6Zombie Brutes&r fallen lassen.",
              "",
              "&eKronwerke:&r Eidolon steht nicht im Stufenziel. Aber wer gegen Afrits kämpft, um Afrit Essence für den Spawn zu holen, freut sich über einen Soul Enchanter in der Nähe.",
          ],
          tasks=[task_item("eidolon_repraised:shadow_gem", 1), task_item("eidolon_repraised:soul_shard", 32)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["stone_altar", "reaper_scythe", "soul_enchanter"], icon="eidolon_repraised:shadow_gem", size=2.5, shape="gear"),
]

images = [
    banner("eidolon/title", "Eidolon", 4.4, -4.4, height=1.8, kind="title", colour="magic"),
    banner("eidolon/seelen", "Pewter und Seelen", 4.4, -2.5, height=0.9, colour="magic"),
    banner("eidolon/altar", "Altar und Gebet", 4.6, 3.9, height=0.9, colour="fire"),
    banner("eidolon/werkzeuge", "Werkzeuge", 1.5, 9.9, height=0.9, colour="magic"),
]

chapter(C, "Eidolon", "eidolon_repraised:codex", "magic", quests, shape="circle", order=28, stage=3,
        subtitle=["Stufe 3. Seelen, Rituale, Gebete und ein dunkler Patron."], images=images)
