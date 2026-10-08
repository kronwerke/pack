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


def ritual(name, x, y, title, subtitle, recipe, effect, icon, deps=("soul_shard",), section=None):
    """One brazier ritual of the checklist: recipe line, effect line, one tick."""
    return quest(name, x, y, title, subtitle=subtitle,
                 description=[recipe, "", effect],
                 tasks=[task_checkmark("Ritual ausgeführt")],
                 rewards=[reward_item("eidolon_repraised:soul_shard", 2), reward_xp(3)],
                 deps=list(deps), icon=icon, shape="square", optional=True, section=section)


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
              "Erst &6zwei Redstone&r und &6zwei Lapis&r. Dann &6vier Soul Shards&r und zweimal rühren. Zum Schluss ein &6Seelenkristall&r (Soul Crystal) aus Deeper and Darker.",
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
           "Tagsüber gezündet, spult es die Zeit vor bis zum Sonnenuntergang.", "minecraft:black_dye", section="rituale"),
    ritual("r_allure", 10, 3, "&aLock Tiere an", "Ritual of Alluring.",
           "&6Rosenstrauch&r auf die Brazier. Auf die Hände: &6Goldener Apfel&r, zwei &6roter Farbstoff&r, zwei &6Soul Shards&r.",
           "Friedliche Tiere aus großer Entfernung laufen langsam zur Brazier.", "minecraft:rose_bush", section="rituale"),
    ritual("r_repelling", 12.5, 3, "&cVertreib Monster", "Ritual of Repelling.",
           "&6Nautilusschale&r auf die Brazier. Auf die Hände: &6Eisenbarren&r, &6Leder&r, &6Quarz&r, zwei &6Soul Shards&r.",
           "Monster in einem großen Umkreis werden vertrieben.", "minecraft:nautilus_shell"),
    ritual("r_purify", 15, 1.5, "&fReinige Zombie-Dorfbewohner", "Ritual of Purifying.",
           "&6Glitzernde Melonenscheibe&r auf die Brazier. Auf die Hände: zwei &6Enchanted Ash&r, ein &6Heiltrank&r, zwei &6Soul Shards&r.",
           "Heilt Zombie-Dorfbewohner in der Nähe. Zombie-Piglins und Zoglins werden wieder normal.", "minecraft:glistering_melon_slice", section="rituale"),
    ritual("r_deceit", 15, 3, "&2Täusch die Dorfbewohner", "Ritual of Deceit.",
           "&6Smaragd&r auf die Brazier. Auf die Hände: &6Smaragd&r, &6Fermentiertes Spinnenauge&r, ein &6Pilz&r, zwei &6Soul Shards&r.",
           "Dorfbewohner vergessen schneller, was du ihnen angetan hast.", "minecraft:emerald", section="rituale"),
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
              "Eine &6Pewter Inlay&r oben, drei &6violette Teppiche&r, drei &6Runewood-Bretter&r aus Malum. Pewter Inlay: vier Pewter im Kreis, gibt zwei.",
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
          deps=["worktable"], icon="eidolon_repraised:athame", optional=True, section="werkzeuge"),

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

    # ---- Ausruestung ---------------------------------------------------------------
    quest("apothecary", 2.5, 2, "&6Bau einen Apothecary Stand",
          subtitle="Brauen ohne Lohenstaub.",
          description=[
              "Ein &6Stock&r oben in der Mitte, &e3 Pewter&r in der Reihe darunter.",
              "",
              "Der Stand braut Tränke wie ein Braustand, braucht aber keinen &6Lohenstaub&r als Brennstoff. Praktisch, solange du noch keine Lohenfarm hast. Den Heiltrank für das Ritual of Purifying und den Schadenstrank für die Sanguine-Rituale machst du gleich hier.",
          ],
          tasks=[task_item("eidolon_repraised:wooden_brewing_stand", 1)],
          rewards=[reward_item("minecraft:nether_wart", 8), reward_xp(3)],
          deps=["pewter"], icon="eidolon_repraised:wooden_brewing_stand", optional=True, section="ausruestung"),

    quest("censer", 5, 8.2, "&6Zünde einen Censer an",
          subtitle="Räucherwerk für Altar und Kampf.",
          description=[
              "&6Censer&r: &6Arcane Gold&r oben, &e2 Silberbarren&r links und rechts, unten Arcane Gold, Pewter, Arcane Gold.",
              "&6Restoration Incense&r, formlos: &6Merammer Resin&r (Merammer Root), &6Oanna Bloom&r, &6Rosa Blütenblätter&r, &6Glitzernde Melonenscheibe&r.",
              "",
              "Füll den Censer und zünde ihn an. Restoration heilt Lebende in der Nähe und schadet Untoten. Im Crucible kochst du weitere Sorten: Tough für mehr Rüstung, Bloodlust für mehr Nahkampfschaden, Soul Harvest für mehr Beute und Erfahrung.",
              "",
              "Auf dem Altar gibt der Censer &e+2 Capacity&r.",
          ],
          tasks=[task_item("eidolon_repraised:censer", 1), task_item("eidolon_repraised:restoration_incense", 2)],
          rewards=[reward_item("minecraft:glistering_melon_slice", 4), reward_xp(5)],
          deps=["athame", "alchemy"], icon="eidolon_repraised:censer", optional=True, section="ausruestung"),

    quest("void_amulet", 0, 15.5, "&5Schmied ein Void Amulet",
          subtitle="Pfeile verschwinden einfach.",
          description=[
              "&6Basic Amulet&r: &e3 Faden&r im Bogen, ein &6Arcane Gold&r unten.",
              "Worktable: Pewter oben, &e2 Pewter Inlay&r an die Seiten, das Basic Amulet in die Mitte, &6Obsidian&r unten, &e2 Soul Shards&r in die Extraplätze.",
              "",
              "Getragen fängt das Amulett ein Geschoss ab, das dich treffen würde. Danach lädt es etwa &d10 Sekunden&r nach. Skelette und Blaze verlieren viel von ihrem Schrecken.",
          ],
          tasks=[task_item("eidolon_repraised:void_amulet", 1)],
          rewards=[reward_item("eidolon_repraised:soul_shard", 4), reward_xp(6)],
          deps=["worktable", "alchemy"], icon="eidolon_repraised:void_amulet"),

    quest("warded_mail", 2.5, 15.5, "&5Weih ein Warded Mail",
          subtitle="Schutz gegen Magie.",
          description=[
              "Worktable: &6Eisenbrustplatte&r in die Mitte, ein &6Soul Shard&r darüber, &e3 Enchanted Ash&r links, rechts und unten, &e4 Pewter Inlay&r in die Extraplätze.",
              "",
              "Das Kettenhemd trägst du unter deiner Rüstung als Curio. Dann hält deine Rüstung auch Magieschaden ab, der sonst durch sie hindurchgeht. Gut gegen Hexen, Evoker und magische Bosse.",
          ],
          tasks=[task_item("eidolon_repraised:warded_mail", 1)],
          rewards=[reward_item("eidolon_repraised:pewter_inlay", 4), reward_xp(6)],
          deps=["worktable", "crucible"], icon="eidolon_repraised:warded_mail", optional=True),

    quest("gravity_belt", 5, 15.5, "&5Schnall dir den Gravity Belt um",
          subtitle="Fallen wie eine Feder.",
          description=[
              "&6Basic Belt&r: &e4 Leder&r als Raute. &6Calx of End&r: Enderperle und Enchanted Ash in den kochenden Crucible, gibt zwei.",
              "Worktable: Enderperle oben, &e2 Federn&r neben dem Gürtel, &6Lesser Soul Gem&r unten. Extra: &e2 Calx of End&r und &e2 Pewter Inlay&r.",
              "",
              "Der Gürtel bremst jeden Fall stark ab, und Fallschaden sinkt auf ein &dViertel&r. Wer viel in Höhlen und auf Türmen baut, nimmt ihn zuerst.",
          ],
          tasks=[task_item("eidolon_repraised:gravity_belt", 1)],
          rewards=[reward_item("minecraft:feather", 16), reward_xp(6)],
          deps=["worktable", "soul_gem"], icon="eidolon_repraised:gravity_belt"),

    quest("reversal_pick", 7.5, 15.5, "&5Schmied die Pickaxe of Inversion",
          subtitle="Je härter der Block, desto schneller.",
          description=[
              "Worktable: oben &6Obsidian&r, &6Weinender Obsidian&r, Obsidian. Darunter Pewter, dann eine Pewter Inlay als Griff.",
              "Extra: &6Enderperle&r, &6Lesser Soul Gem&r und &e2 Soul Shards&r.",
              "",
              "Diese Spitzhacke dreht die Härte um: Harte Blöcke wie &6Obsidian&r brechen schnell, weiche wie Erde oder Sand bremsen sie. Nimm sie für Obsidian und Tiefenschiefer, nicht für Erde.",
          ],
          tasks=[task_item("eidolon_repraised:reversal_pick", 1)],
          rewards=[reward_item("minecraft:obsidian", 16), reward_xp(6)],
          deps=["worktable", "soul_gem"], icon="eidolon_repraised:reversal_pick", optional=True),

    quest("bonechill_wand", 10, 15.5, "&bBau einen Bonechill Wand",
          subtitle="Wer getroffen wird, heilt nicht mehr.",
          description=[
              "&6Wraith Heart&r: &5Wraiths&r lassen es selten fallen, nur wenn du sie selbst besiegst. Plünderung hilft.",
              "Worktable: Wraith Heart oben rechts, &e2 Pewter&r und ein &6Stock&r diagonal, Pewter Inlay unten links. Extra: &6Lesser Soul Gem&r und &e3 Knochenmehl&r.",
              "",
              "Der Stab verflucht das Ziel mit eisigem Griff: Wie bei den Krallen eines Wraith regeneriert es keine Lebenspunkte mehr. Leere Stäbe lädst du mit einem Soul Gem auf der Brazier wieder auf.",
          ],
          tasks=[task_item("eidolon_repraised:bonechill_wand", 1)],
          rewards=[reward_item("minecraft:bone_meal", 16), reward_xp(8)],
          deps=["soul_gem", "worktable"], icon="eidolon_repraised:bonechill_wand", optional=True),

    quest("soulfire_wand", 12.5, 15.5, "&dBau den Soulfire Wand",
          subtitle="Die Kraft des Shadow Gem in deiner Hand.",
          description=[
              "Worktable: &6Shadow Gem&r oben rechts, &e2 Arcane Gold&r und ein &6Stock&r diagonal, Gold Inlay unten links. Extra: &6Lesser Soul Gem&r und &e3 Lohenstaub&r.",
              "",
              "Ein Schwung schießt helle Energieblitze, die fast jedem Ziel ordentlich Schaden machen. Deine erste echte Fernkampfwaffe aus Eidolon.",
          ],
          tasks=[task_item("eidolon_repraised:soulfire_wand", 1)],
          rewards=[reward_item("minecraft:blaze_powder", 8), reward_table("s3_common"), reward_xp(10)],
          deps=["necromancer"], icon="eidolon_repraised:soulfire_wand", section="ausruestung"),

    quest("warlock_cloak", 15, 15.5, "&5Näh einen Warlock's Cloak",
          subtitle="Halber Schaden von Magie und Wither.",
          description=[
              "&6Wicked Weave&r: &e8 weiße Wolle&r um einen &6Shadow Gem&r, extra ein &6Unholy Symbol&r und &6blauer Farbstoff&r. Das gibt &e8&r Stück.",
              "&6Warlock's Cloak&r: &e7 Wicked Weave&r in Brustplattenform, extra &e2 Soul Shards&r.",
              "",
              "Der Umhang halbiert Magie- und Witherschaden. Der Hut gibt &d50 Prozent&r mehr Magie- und Witherschaden, die Stiefel machen dich immun gegen Langsamkeit.",
          ],
          tasks=[task_item("eidolon_repraised:warlock_cloak", 1)],
          rewards=[reward_item("minecraft:white_wool", 16), reward_xp(10)],
          deps=["necromancer"], icon="eidolon_repraised:warlock_cloak", optional=True, section="ausruestung"),

    quest("sapping_sword", 17.5, 15.5, "&cWeih ein Sword of Sapping",
          subtitle="Ein Schwert, das Leben stiehlt.",
          description=[
              "&6Eisenschwert&r auf die Brazier. Auf die Stone Hands: &6Shadow Gem&r, &e2 Soul Shards&r, &e2 Netherwarzen&r, &6Ghast-Träne&r. In einen &6Necrotic Focus&r: ein &6Schadenstrank&r.",
              "",
              "Das Ritual verlangt außerdem &d10 Herzen&r Leben in der Nähe: Stell ein paar Tiere daneben, sie werden verbraucht.",
              "",
              "Das Schwert macht zusätzlich Witherschaden, und dieser Schaden heilt dich. Verzauberungen des Eisenschwerts bleiben erhalten.",
          ],
          tasks=[task_item("eidolon_repraised:sapping_sword", 1)],
          rewards=[reward_item("minecraft:ghast_tear", 2), reward_xp(10)],
          deps=["necromancer"], icon="eidolon_repraised:sapping_sword", optional=True, section="ausruestung"),
]

images = [
    banner("eidolon/title", "Eidolon", 5, -4.6, height=1.8, kind="title", colour="magic"),
    banner("eidolon/seelen", "Pewter und Seelen", 5, -2.7, height=0.9, colour="magic"),
    banner("eidolon/rituale", "Rituale", 13.75, -0.2, height=0.9, colour="fire"),
    banner("eidolon/altar", "Altar und Gebet", 7.5, 4.4, height=0.9, colour="fire"),
    banner("eidolon/werkzeuge", "Werkzeuge", 4, 9.9, height=0.9, colour="magic"),
    banner("eidolon/ausruestung", "Ausrüstung und Waffen", 4, 13.9, height=0.9, colour="fire"),
]

chapter(C, "Eidolon", "eidolon_repraised:codex", "magic", quests, shape="circle", order=28, stage=3,
        subtitle=["Stufe 3. Seelen, Rituale, Zeichen, Gebete und ein dunkler Patron."], images=images)
