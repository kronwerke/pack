"""Eidolon Repraised in stage 3 (the whole mod opens with stage 3): the codex, pewter, the
crucible, arcane gold and the lesser soul gem one step each, the brazier and the crystallization
ritual, the other brazier rituals as a checklist (daylight, moonlight, alluring, repelling,
purifying, deceit, lesser summoning), the altar, effigy and signs (wicked, blood, soul) with the
chants that need them, the goblet sacrifice, worktable, unholy symbol, stone altar and elder
statue, the athame and its herbs, death essence, the reaper scythe, the soul enchanter and the
shadow gem. Recipes from the eidolon_repraised 0.5.0.4 jar (recipe/rituals, crucible, chant)."""
from ftbq import (chapter, quest, task_item, task_checkmark, task_advancement, reward_item, reward_table,
                  reward_xp, banner)

C = "eidolon"


def ritual(name, x, y, title, subtitle, recipe, effect, icon, deps=("soul_shard",)):
    """One brazier ritual of the checklist: recipe line, effect line, one tick."""
    return quest(name, x, y, title, subtitle=subtitle,
                 description=[recipe, "", effect],
                 tasks=[task_checkmark("Ritual ausgeführt")],
                 rewards=[reward_item("eidolon_repraised:soul_shard", 2), reward_xp(3)],
                 deps=list(deps), icon=icon, shape="square", optional=True)


quests = [
    # ---- Pewter und Seelen -----------------------------------------------------
    quest("welcome", 0, 0, "&5&lSchreib dir den Codex",
          subtitle="Ein Buch über Seelen, Götter und Untote.",
          description=[
              "&6Ein Buch&r und &6Verrottetes Fleisch&r, formlos: die &6Ars Ecclesia&r.",
              "",
              "&5Eidolon&r ist düstere Magie: Seelensplitter aus Untoten, Rituale an der Feuerschale, Gebete am Altar und Werkzeuge, die Seelen ernten. Die ganze Mod öffnet mit &6Stufe 3&r.",
              "",
              "Im Kapitel &eSigns&r des Codex singst du später deine Gesänge. Pass gut auf das Buch auf.",
          ],
          tasks=[task_item("eidolon_repraised:codex", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 16), reward_table("s3_common")],
          icon="eidolon_repraised:codex", size=2.0, shape="hexagon"),

    quest("pewter", 2.5, 0, "&7Schmilz Pewter",
          subtitle="Ein Metall, das Magie nicht stört.",
          description=[
              "Ein &6Bleibarren&r und ein &6Eisenbarren&r, formlos: &ezwei Pewter Blend&r. Im Ofen werden sie zu Barren.",
              "",
              "Jedes Blei zählt: das von Eidolon, Mekanism oder aus der Bergbau-Dimension. Fast alle Geräte der Mod sind aus Pewter.",
          ],
          tasks=[task_item("eidolon_repraised:pewter_ingot", 16)],
          rewards=[reward_item("minecraft:iron_ingot", 8), reward_xp(3)],
          deps=["welcome"], icon="eidolon_repraised:pewter_ingot"),

    quest("crucible", 5, -1, "&6Setz einen Crucible auf",
          subtitle="Alchemie in mehreren Schritten.",
          description=[
              "Sieben &6Pewter&r in Kesselform. Über ein Lagerfeuer stellen, mit Wasser füllen, warten bis es kocht.",
              "",
              "Wirf die Zutaten des ersten Schritts hinein. Ändert sich die Farbe, kommt der nächste. Steht \"stir\" dabei, rührst du mit leerer Hand so oft wie angegeben.",
              "",
              "Zum Üben: &6Kohle&r und &6Enchanted Ash&r (Knochen im Ofen) ergeben zwei Sulfur.",
          ],
          tasks=[task_item("eidolon_repraised:crucible", 1)],
          rewards=[reward_item("minecraft:bone", 16), reward_xp(3)],
          deps=["pewter"], icon="eidolon_repraised:crucible"),

    quest("brazier", 5, 1, "&6Bau Brazier und Stone Hands",
          subtitle="Der Ort für Rituale.",
          description=[
              "&6Brazier&r: drei &6Pewter&r oben, ein &6Kohleblock&r darunter, zwei Stöcke als Beine. &6Stone Hand&r: Steinstufen und Stein, siehe JEI.",
              "",
              "Ritual: Item auf die Brazier, weitere Zutaten auf Stone Hands drumherum, mit dem &6Feuerzeug&r anzünden. Leere Hand löscht sie und beendet das Ritual.",
          ],
          tasks=[task_item("eidolon_repraised:brazier", 1), task_item("eidolon_repraised:stone_hand", 4)],
          rewards=[reward_item("minecraft:flint_and_steel", 1), reward_xp(3)],
          deps=["pewter"], icon="eidolon_repraised:brazier"),

    quest("soul_shard", 7.5, 1, "&dKristallisier Seelen",
          subtitle="Das Ritual der Kristallisation.",
          description=[
              "&6Knochenmehl&r auf die Brazier, je ein &6Redstone&r auf zwei Stone Hands, anzünden.",
              "",
              "Wenn das Ritual die letzte Zutat verbraucht, vernichtet es alle Untoten in der Nähe und lässt &dSoul Shards&r zurück. Bau es nachts auf oder fang Zombies in einer Grube daneben.",
          ],
          tasks=[task_item("eidolon_repraised:soul_shard", 8)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(5)],
          deps=["brazier"], icon="eidolon_repraised:soul_shard"),

    quest("alchemy", 7.5, -1, "&6Koch Arcane Gold",
          subtitle="Zwei Schritte im Kessel.",
          description=[
              "Erst &6zwei Redstone&r und einen &6Soul Shard&r in den kochenden Crucible, dann &6zwei Goldbarren&r. Heraus kommen &ezwei&r Arcane Gold.",
              "",
              "Daraus: Goblet, Gold Inlay, Soul Enchanter und die Ringe und Amulette.",
          ],
          tasks=[task_item("eidolon_repraised:arcane_gold_ingot", 6)],
          rewards=[reward_item("minecraft:gold_ingot", 8), reward_xp(5)],
          deps=["crucible", "soul_shard"], icon="eidolon_repraised:arcane_gold_ingot"),

    quest("soul_gem", 10, -1, "&dKoch einen Lesser Soul Gem",
          subtitle="Drei Schritte, zweimal rühren.",
          description=[
              "Erst &6zwei Redstone&r und &6zwei Lapis&r. Dann &6vier Soul Shards&r und zweimal rühren. Zum Schluss ein &6Quarz&r.",
              "",
              "Der Seelenstein steckt in Zauberstäben und im Sanguine Amulet. Mit einem Soul Gem auf der Brazier lädst du leere Stäbe wieder auf.",
          ],
          tasks=[task_item("eidolon_repraised:lesser_soul_gem", 1)],
          rewards=[reward_item("minecraft:lapis_lazuli", 8), reward_xp(6)],
          deps=["alchemy"], icon="eidolon_repraised:lesser_soul_gem"),

    # ---- Rituale (Checkliste) -----------------------------------------------------
    ritual("r_daylight", 10, 1.5, "&eRuf den Tag herbei", "Ritual of Daylight.",
           "&6Sonnenblume&r auf die Brazier. Auf die Hände: &6Holzkohle&r, &6Weizensamen&r, zwei &6Soul Shards&r.",
           "Nachts gezündet, spult es die Zeit vor, bis die Sonne aufgeht.", "minecraft:sunflower"),
    ritual("r_moonlight", 12.5, 1.5, "&9Ruf die Nacht herbei", "Ritual of Moonlight.",
           "&6Schwarzer Farbstoff&r auf die Brazier. Auf die Hände: &6Schneeball&r, &6Spinnenauge&r, zwei &6Soul Shards&r.",
           "Tagsüber gezündet, spult es die Zeit vor bis zum Sonnenuntergang.", "minecraft:black_dye"),
    ritual("r_allure", 10, 3, "&aLock Tiere an", "Ritual of Alluring.",
           "&6Rosenstrauch&r auf die Brazier. Auf die Hände: &6Goldener Apfel&r, zwei &6roter Farbstoff&r, zwei &6Soul Shards&r.",
           "Friedliche Tiere aus großer Entfernung laufen langsam zur Brazier.", "minecraft:rose_bush"),
    ritual("r_repelling", 12.5, 3, "&cVertreib Monster", "Ritual of Repelling.",
           "&6Nautilusschale&r auf die Brazier. Auf die Hände: &6Eisenbarren&r, &6Leder&r, &6Quarz&r, zwei &6Soul Shards&r.",
           "Monster in einem großen Umkreis werden vertrieben.", "minecraft:nautilus_shell"),
    ritual("r_purify", 15, 1.5, "&fReinige Zombie-Dorfbewohner", "Ritual of Purifying.",
           "&6Glitzernde Melonenscheibe&r auf die Brazier. Auf die Hände: zwei &6Enchanted Ash&r, ein &6Heiltrank&r, zwei &6Soul Shards&r.",
           "Heilt Zombie-Dorfbewohner in der Nähe. Zombie-Piglins und Zoglins werden wieder normal.", "minecraft:glistering_melon_slice"),
    ritual("r_deceit", 15, 3, "&2Täusch die Dorfbewohner", "Ritual of Deceit.",
           "&6Smaragd&r auf die Brazier. Auf die Hände: &6Smaragd&r, &6Fermentiertes Spinnenauge&r, ein &6Pilz&r, zwei &6Soul Shards&r.",
           "Dorfbewohner vergessen schneller, was du ihnen angetan hast.", "minecraft:emerald"),
    ritual("r_summon", 17.5, 2.25, "&8Beschwör einen Zombie", "Lesser Summoning.",
           "&6Holzkohle&r auf die Brazier. Auf die Hände: &6Soul Shard&r und &6Verrottetes Fleisch&r. Ein Verrottetes Fleisch in einen &6Necrotic Focus&r.",
           "Ein Zombie erscheint auf der Brazier. Mit Knochen ein Skelett, mit Phantomhaut ein Phantom, mit Seelensand im Fokus ein Witherskelett.",
           "minecraft:rotten_flesh", deps=("r_daylight", "r_repelling")),

    # ---- Altar und Gebet ---------------------------------------------------------
    quest("altar", 0, 6, "&6Bau einen Altar mit Bildnis",
          subtitle="Ein Ort, an dem man dich hört.",
          description=[
              "&6Wooden Altar&r: Holzstufen über Brettern, gibt drei. &6Straw Effigy&r: fünf Weizen im Kreuz. Bildnis oben drauf.",
              "",
              "Kerzen, Schädel von Untoten und seltene Kräuter im Topf auf dem Altar erhöhen &ePower&r und &eCapacity&r. Pro Sorte zählt nur das beste Stück.",
          ],
          tasks=[task_item("eidolon_repraised:wooden_altar", 3), task_item("eidolon_repraised:straw_effigy", 1)],
          rewards=[reward_item("minecraft:candle", 4), reward_xp(3)],
          deps=["welcome"], icon="eidolon_repraised:straw_effigy"),

    quest("wicked_sign", 2.5, 6, "&5Lern das Wicked Sign",
          subtitle="Eine Hexe zeigt dir den Weg.",
          description=[
              "Wirf deinen &6Codex&r einer &5Hexe&r vor die Füße. Sie schreibt das &5Wicked Sign&r hinein und gibt ihn zurück.",
              "",
              "Den hellen Weg lernst du, wenn du das Buch einem &eKleriker&r zuwirfst: das Sacred Sign. Dieses Kapitel folgt dem dunklen Weg.",
              "",
              "&cAchtung:&r Hexen werfen Tränke. Halt einen Heiltrank bereit.",
          ],
          tasks=[task_checkmark("Wicked Sign gelernt")],
          rewards=[reward_item("minecraft:glass_bottle", 8), reward_xp(5)],
          deps=["altar"], icon="eidolon_repraised:unholy_symbol"),

    quest("prayer", 5, 6, "&5Bete zum dunklen Herrn",
          subtitle="Dreimal Wicked, einmal am Tag.",
          description=[
              "Codex, Kapitel &eSigns&r: dreimal &5Wicked&r wählen und vor dem Altar mit Bildnis singen. Das ist das &5Dark Prayer&r.",
              "",
              "Jedes Gebet geht einmal am Tag und bringt Gunst. Dein Patron gibt dafür &bMana&r für Gesänge, die Power des Altars bestimmt wie viel, die Capacity wie viel du hältst.",
          ],
          tasks=[task_checkmark("Zum ersten Mal gebetet")],
          rewards=[reward_xp(6)],
          deps=["wicked_sign"], icon="eidolon_repraised:codex"),

    quest("sign_blood", 7.5, 6, "&cEmpfang das Blood Sign",
          subtitle="Ein Geschenk für treue Gebete.",
          description=[
              "Bete jeden Tag. Mit wachsender Gunst schenkt dir der Patron das &cBlood Sign&r, das Zeichen der Lebenskraft.",
              "",
              "Probier jeden neuen Ritus mindestens einmal aus. Manchmal öffnet erst das die nächste Stufe.",
          ],
          tasks=[task_checkmark("Blood Sign gelernt")],
          rewards=[reward_xp(6)],
          deps=["prayer"], icon="minecraft:redstone"),

    quest("goblet", 10, 6, "&cOpfer im Goblet",
          subtitle="Blut für den dunklen Herrn.",
          description=[
              "&6Goblet&r: vier &6Arcane Gold&r. Auf den Altar stellen, das gibt +2 Capacity. Töte ein Tier direkt darüber, dann sing &5Wicked, Blood, Wicked&r.",
              "",
              "Opfer sind dem Patron viel wert, gehen aber auch nur einmal am Tag.",
          ],
          tasks=[task_item("eidolon_repraised:goblet", 1),
                 task_advancement("eidolon_repraised:sacrifice", "Ein Tieropfer dargebracht")],
          rewards=[reward_item("minecraft:wheat", 32), reward_xp(7)],
          deps=["sign_blood", "alchemy"], icon="eidolon_repraised:goblet"),

    quest("sign_soul", 12.5, 6, "&dEmpfang das Soul Sign",
          subtitle="Das Zeichen, das Seelen bindet.",
          description=[
              "Bete und opfere weiter. Mit genug Gunst bekommst du das &dSoul Sign&r.",
              "",
              "Damit kennst du &5Touch of Darkness&r (Wicked, Soul, Wicked, Soul). Die Gesänge mit Flame, Winter oder Death stehen im Codex, sobald du die Zeichen hast.",
          ],
          tasks=[task_checkmark("Soul Sign gelernt")],
          rewards=[reward_xp(7)],
          deps=["goblet"], icon="eidolon_repraised:soul_shard"),

    quest("worktable", 2.5, 8.2, "&6Bau einen Worktable",
          subtitle="Eine Werkbank mit vier Extraplätzen.",
          description=[
              "Eine &6Pewter Inlay&r oben, drei &6violette Teppiche&r, drei &6Bretter&r. Pewter Inlay: vier Pewter im Kreis, gibt zwei.",
              "",
              "Arbeitet wie eine Werkbank, hat aber vier Plätze für magische Zutaten. Viele bessere Rezepte gehen nur hier.",
          ],
          tasks=[task_item("eidolon_repraised:worktable", 1)],
          rewards=[reward_item("eidolon_repraised:pewter_inlay", 4), reward_xp(4)],
          deps=["pewter", "altar"], icon="eidolon_repraised:worktable"),

    quest("unholy_symbol", 15, 6, "&5Weih ein Unholy Symbol",
          subtitle="Touch of Darkness.",
          description=[
              "Leg eine &6Pewter Inlay&r auf den Boden, schau sie an und sing &5Wicked, Soul, Wicked, Soul&r. Sie wird zum &5Unholy Symbol&r.",
              "",
              "Auf eine Waffe gesungen macht sie eine Weile Wither-Schaden. Das Symbol steckt in Sense, Elder Statue und Wicked Weave.",
          ],
          tasks=[task_item("eidolon_repraised:unholy_symbol", 2)],
          rewards=[reward_item("eidolon_repraised:pewter_inlay", 2), reward_xp(8)],
          deps=["sign_soul", "worktable"], icon="eidolon_repraised:unholy_symbol"),

    quest("stone_altar", 17.5, 6, "&5Bau Stone Altar und Elder Statue",
          subtitle="Für die mächtigeren Riten.",
          description=[
              "Worktable: &6Stone Altar&r aus glatten Steinstufen, Stein, Pewter Inlay, Soul Shard im Extraplatz (gibt drei). &6Elder Statue&r aus Stein und glattem Stein, Unholy Symbol und Gold Inlay extra.",
              "",
              "Erst hier gehen die großen Riten: ein Dorfbewohner als Opfer oder in einen Zombie verwandelt. Der helle Weg heilt hier Zombie-Dorfbewohner.",
          ],
          tasks=[task_item("eidolon_repraised:stone_altar", 3), task_item("eidolon_repraised:unholy_effigy", 1)],
          rewards=[reward_table("s3_common"), reward_xp(10)],
          deps=["unholy_symbol"], icon="eidolon_repraised:unholy_effigy", size=1.5, shape="diamond"),

    # ---- Werkzeuge ---------------------------------------------------------------
    quest("athame", 0, 11.5, "&7Ernte Kräuter mit dem Athame",
          subtitle="Seltene Pflanzen für Altar und Räucherwerk.",
          description=[
              "Worktable: Pewter, Pewter Inlay, Enderperle diagonal, dazu &6Goldnugget&r und &6Silbernugget&r extra.",
              "",
              "Klick mit dem Athame auf Pflanzen: Farn gibt Avennian Sprig, Margerite oder Maiglöckchen Merammer Root, Seerose Oanna Bloom, Dschungellaub Sildrian Seed, Nether-Pilze Mirecap.",
          ],
          tasks=[task_item("eidolon_repraised:athame", 1)],
          rewards=[reward_item("minecraft:fern", 8), reward_xp(4)],
          deps=["worktable"], icon="eidolon_repraised:athame", optional=True),

    quest("death_essence", 2.5, 11.5, "&8Koch Death Essence",
          subtitle="Aus dem Herz eines Zombie Brute.",
          description=[
              "Crucible: &6Zombie Heart&r und &6Verrottetes Fleisch&r. Dann zweimal &6Knochenmehl&r und zweimal rühren. Zum Schluss &6Holzkohle&r: vier Death Essence.",
              "",
              "Das Herz lassen die stärkeren &6Zombie Brutes&r fallen.",
          ],
          tasks=[task_item("eidolon_repraised:death_essence", 4)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(6)],
          deps=["soul_gem"], icon="eidolon_repraised:death_essence"),

    quest("reaper_scythe", 5, 11.5, "&5Schmiede die Reaper Scythe",
          subtitle="Seelen ernten ohne Ritual.",
          description=[
              "Worktable: drei &6Pewter&r und zwei Stöcke, extra &5Unholy Symbol&r, zwei &6Tattered Cloth&r und ein &6Soul Shard&r.",
              "",
              "Tattered Cloth lassen &5Wraiths&r fallen. Ihre Krallen geben Chilled, dann heilst du nicht. Was die Sense tötet und untot ist, hinterlässt Soul Shards.",
          ],
          tasks=[task_item("eidolon_repraised:reaper_scythe", 1)],
          rewards=[reward_item("eidolon_repraised:soul_shard", 8), reward_xp(8)],
          deps=["unholy_symbol"], icon="eidolon_repraised:reaper_scythe"),

    quest("soul_enchanter", 7.5, 11.5, "&dBau einen Soul Enchanter",
          subtitle="Verzaubern ohne Glücksspiel.",
          description=[
              "Worktable: Buch, zwei &6Arcane Gold&r, vier &6Obsidian&r, extra zwei &6Diamanten&r und zwei &6Gold Inlays&r.",
              "",
              "Er gibt genau eine Verzauberung auf Stufe I oder hebt eine vorhandene um eins, auch auf verzauberten Items. Jeder Schritt kostet Level und Soul Shards.",
          ],
          tasks=[task_item("eidolon_repraised:soul_enchanter", 1)],
          rewards=[reward_item("eidolon_repraised:soul_shard", 8), reward_xp(10)],
          deps=["worktable", "alchemy"], icon="eidolon_repraised:soul_enchanter"),

    # ---- Ziel --------------------------------------------------------------------
    quest("necromancer", 12.5, 11.5, "&5&lKoch einen Shadow Gem",
          subtitle="Gunst, Seelen und ein Schattenstein.",
          description=[
              "Crucible: &6Kohle&r. Dann &6Ghast Tear&r und &6Death Essence&r, einmal rühren. Dann zwei &6Soul Shards&r und eine Death Essence, einmal rühren. Zum Schluss ein &6Diamant&r.",
              "",
              "Der Shadow Gem ist der Kern des Soulfire Wand und des Wicked Weave für die Warlock-Rüstung.",
              "",
              "&eKronwerke:&r Eidolon steht nicht im Stufenziel. Wer gegen Afrits kämpft, freut sich aber über einen Soul Enchanter in der Nähe.",
          ],
          tasks=[task_item("eidolon_repraised:shadow_gem", 1), task_item("eidolon_repraised:soul_shard", 32)],
          rewards=[reward_table("s3_rare"), reward_xp(15)],
          deps=["stone_altar", "reaper_scythe", "soul_enchanter", "death_essence"],
          icon="eidolon_repraised:shadow_gem", size=2.5, shape="gear"),
]

images = [
    banner("eidolon/title", "Eidolon", 5, -4.6, height=1.8, kind="title", colour="magic"),
    banner("eidolon/seelen", "Pewter und Seelen", 5, -2.7, height=0.9, colour="magic"),
    banner("eidolon/rituale", "Rituale", 13.75, -0.2, height=0.9, colour="fire"),
    banner("eidolon/altar", "Altar und Gebet", 7.5, 4.4, height=0.9, colour="fire"),
    banner("eidolon/werkzeuge", "Werkzeuge", 4, 9.9, height=0.9, colour="magic"),
]

chapter(C, "Eidolon", "eidolon_repraised:codex", "magic", quests, shape="circle", order=28, stage=3,
        subtitle=["Stufe 3. Seelen, Rituale, Zeichen, Gebete und ein dunkler Patron."], images=images)
