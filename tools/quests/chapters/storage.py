"""Storage in stage 1, the practical first-week chapter: Sophisticated Backpacks (leather backpack
and its upgrades), Functional Storage (wooden, framed and fluid drawers and their upgrades),
Sophisticated Storage (barrels and chests up to iron, upgrades, the storage controller, I/O),
the Create item vault, trash cans and the sack. Copper and iron backpacks, compacting drawers,
drawer storage upgrades and gold chests open in stage 2, gold and diamond backpacks, diamond
chests and AE2 in stage 3; the outlook quest names them. Numbers come from the mods' recipes,
lang files and config/sophisticated*-server.toml. Kronwerke changes none of these recipes.
Drawer controllers and AE2 storage buses are in ae2.py, the overview in list_transport.py."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table, reward_xp,
                  banner)

C = "storage"


def head(name, text, left, y, height=0.9, kind="section", colour="stone"):
    """A banner whose left edge sits at x = left."""
    b = banner(f"{C}/{name}", text, 0, y, height=height, kind=kind, colour=colour)
    b["x"] = round(left + b["width"] / 2, 2)
    return b


quests = [
    # ---- Rucksäcke (Sophisticated Backpacks) ------------------------------------------------
    quest("welcome", 0, 1, "&6&lNäh einen Rucksack",
          subtitle="Dein Lager zum Mitnehmen.",
          description=[
              "&6Holztruhe&r in die Mitte, &6vier Leder&r (eins oben, drei unten), &6vier Fäden&r an die Seiten und oben in die Ecken.",
              "",
              "Der Lederrucksack hat &e27 Plätze&r und &eeinen Upgrade-Platz&r. Öffnen mit Rechtsklick in der Hand oder mit &eB&r, solange er im Inventar steckt. Schleich-Rechtsklick auf den Boden stellt ihn ab, der Inhalt bleibt drin. Farbstoffe im Handwerksraster färben ihn.",
              "",
              "Dieses Kapitel ist deine erste Woche: Rucksack, Schubladenwand, aufwertbare Fässer, ein Tresor für Create. &cKronwerke:&r Kupfer- und Eisenrucksack öffnen in Stufe 2, Gold und Diamant in Stufe 3, Netherit in Stufe 4. Der Tooltip sagt, welche Stufe fehlt.",
          ],
          tasks=[task_item("sophisticatedbackpacks:backpack", 1)],
          rewards=[reward_item("minecraft:leather", 8), reward_item("minecraft:string", 8), reward_table("s1_common")],
          icon="sophisticatedbackpacks:backpack", size=2.0, shape="hexagon"),

    quest("upgrade_base", 2.5, 0, "Bau eine Upgrade-Basis",
          subtitle="Jedes Rucksack-Upgrade beginnt hier.",
          description=[
              "&6Leder&r in die Mitte, &6vier Eisenbarren&r an die Seiten, &6vier Fäden&r in die Ecken.",
              "",
              "Upgrades stecken links neben dem Rucksackinventar. Der Lederrucksack hat nur einen Platz, du tauschst sie also je nach Tag: Bergbau, Bauen, Farmen.",
              "",
              "&6Tipp:&r Sophisticated Storage hat eine eigene Upgrade-Basis für Truhen. Achte in JEI darauf, welche Mod im Rezept steht.",
          ],
          tasks=[task_item("sophisticatedbackpacks:upgrade_base", 2)],
          rewards=[reward_item("minecraft:string", 16), reward_item("minecraft:iron_ingot", 4)],
          deps=["welcome"], icon="sophisticatedbackpacks:upgrade_base"),

    quest("pickup", 4.5, 0, "Bau ein Pickup-Upgrade",
          subtitle="Was du aufhebst, landet im Rucksack.",
          description=[
              "Ein &6Klebriger Kolben&r oben, &6Faden&r links und rechts der Upgrade-Basis, &6drei Redstone&r unten.",
              "",
              "Der Filter hat &e9 Plätze&r. Whitelist heißt nur diese Items, Blacklist alles außer diesen. Ein leerer Filter auf Blacklist nimmt alles.",
              "",
              "&6Tipp:&r Erze, Kohle und Rohmetalle auf die Whitelist, dann bleibt der Bruchstein im Inventar und geht mit &e/kw deposit&r direkt an den Obelisken.",
          ],
          tasks=[task_item("sophisticatedbackpacks:pickup_upgrade", 1)],
          rewards=[reward_item("minecraft:slime_ball", 4), reward_xp(3)],
          deps=["upgrade_base"], icon="sophisticatedbackpacks:pickup_upgrade"),

    quest("magnet", 6.5, 0, "Bau ein Magnet-Upgrade",
          subtitle="Zieht Items in der Nähe zu dir.",
          description=[
              "Das &6Pickup-Upgrade&r in die Mitte, &6zwei Enderperlen&r in die oberen Ecken, &6drei Eisenbarren&r oben und an den Seiten, unten &6Redstone&r links und &6Lapislazuli&r rechts.",
              "",
              "Kann alles, was das Pickup-Upgrade kann, und zieht Items aus &e3 Blöcken&r Umkreis heran. Perfekt mit FTB Ultimine.",
              "",
              "&cAchtung:&r Er zieht auch, was ein Mitspieler fallen lässt. Beim Tauschen im Upgrade-Tab ausschalten.",
          ],
          tasks=[task_item("sophisticatedbackpacks:magnet_upgrade", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_table("s1_common")],
          deps=["pickup"], icon="sophisticatedbackpacks:magnet_upgrade"),

    quest("deposit", 8.5, 0, "Bau ein Lager-Upgrade",
          subtitle="Ein Klick, und der Rucksack ist leer.",
          description=[
              "Ein &6Kolben&r oben, &6zwei Eisenbarren&r neben der Upgrade-Basis, unten &6Redstone&r, eine &6Holztruhe&r und &6Redstone&r.",
              "",
              "Rucksack in die Hand, &eSchleich-Rechtsklick&r auf eine Truhe, ein Fass oder eine Schublade, und die passenden Items wandern hinein. Im Filter stellst du ein, dass nur abgegeben wird, was dort schon liegt.",
          ],
          tasks=[task_item("sophisticatedbackpacks:deposit_upgrade", 1)],
          rewards=[reward_item("minecraft:redstone", 16), reward_xp(3)],
          deps=["magnet"], icon="sophisticatedbackpacks:deposit_upgrade"),

    quest("stack_starter", 10.5, 0, "Bau ein Stack-Upgrade der Starterstufe",
          subtitle="Mehr pro Platz, ohne größeren Rucksack.",
          description=[
              "Die Upgrade-Basis in die Mitte, &6acht Kupferblöcke&r drumherum.",
              "",
              "Stack-Upgrades ändern nicht die Zahl der Plätze, sondern wie viel in &ejeden&r passt. Die Starterstufe nimmt das &e1,5-fache&r, aus 64 Stein pro Platz werden 96.",
              "",
              "&cAchtung:&r Herausnehmen geht nur, wenn danach noch alles passt. Beim Lederrucksack belegt es den einzigen Platz.",
          ],
          tasks=[task_item("sophisticatedbackpacks:stack_upgrade_starter_tier", 1)],
          rewards=[reward_item("minecraft:copper_block", 4), reward_table("s1_uncommon")],
          deps=["deposit"], icon="sophisticatedbackpacks:stack_upgrade_starter_tier"),

    quest("bp_stack_1", 12.5, 0, "Verdopple jeden Platz",
          subtitle="Stack-Upgrade Stufe 1 aus Eisen.",
          description=[
              "Die Upgrade-Basis in die Mitte, &6acht Eisenblöcke&r drumherum.",
              "",
              "Jeder Platz fasst das &eDoppelte&r, 128 Stein statt 64. Teuer in Stufe 1, aber der Lederrucksack wird damit so groß wie zwei Truhen. Stufe 2 (vierfach) kommt mit dem Messingwerk.",
          ],
          tasks=[task_item("sophisticatedbackpacks:stack_upgrade_tier_1", 1)],
          rewards=[reward_item("minecraft:iron_block", 2), reward_xp(8)],
          deps=["stack_starter"], icon="sophisticatedbackpacks:stack_upgrade_tier_1", optional=True),

    quest("crafting", 2.5, 2, "Bau ein Werkbank-Upgrade",
          subtitle="Eine Werkbank, die du immer dabei hast.",
          description=[
              "Eine &6Werkbank&r oben, &6zwei Eisenbarren&r neben der Upgrade-Basis, eine &6Truhe&r unten.",
              "",
              "Ein 3x3-Raster in einem eigenen Tab, das direkt auf den Rucksackinhalt zugreift. JEI-Rezepte legst du mit dem Plus hinein.",
          ],
          tasks=[task_item("sophisticatedbackpacks:crafting_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["upgrade_base"], icon="sophisticatedbackpacks:crafting_upgrade", optional=True),

    quest("void", 4.5, 2, "Bau ein Leere-Upgrade",
          subtitle="Löscht, was du nicht haben willst.",
          description=[
              "Eine &6Enderperle&r oben, &6drei Obsidian&r um die Upgrade-Basis, &6zwei Redstone&r unten in die Ecken.",
              "",
              "Was im Filter steht, wird beim Ankommen vernichtet. Gut für Erde, Kies, Diorit.",
              "",
              "&cAchtung:&r Bruchstein gehört nicht hinein. Der Obelisk braucht für Stufe 1 &e20 000 Bruchstein&r vom ganzen Server. Gib ihn mit &e/kw deposit&r ab.",
          ],
          tasks=[task_item("sophisticatedbackpacks:void_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["pickup"], icon="sophisticatedbackpacks:void_upgrade", optional=True),

    quest("feeding", 6.5, 2, "Bau ein Futter-Upgrade",
          subtitle="Essen, ohne daran zu denken.",
          description=[
              "Eine &6Goldene Karotte&r oben, links ein &6Goldener Apfel&r, rechts eine &6Glitzernde Melonenscheibe&r, unten eine &6Enderperle&r, die Upgrade-Basis in die Mitte.",
              "",
              "Es füttert dich aus dem Rucksack, sobald du Hunger hast, und wählt Essen, das nicht verschwendet wird. Ein paar Stapel aus Farmer's Delight halten lange.",
          ],
          tasks=[task_item("sophisticatedbackpacks:feeding_upgrade", 1)],
          rewards=[reward_item("minecraft:cooked_beef", 16)],
          deps=["magnet"], icon="sophisticatedbackpacks:feeding_upgrade", optional=True),

    quest("restock", 8.5, 2, "Bau ein Auffüll-Upgrade",
          subtitle="Holt Vorräte aus der Kiste.",
          description=[
              "Wie das Lager-Upgrade, nur mit einem &6Klebrigen Kolben&r oben.",
              "",
              "Rucksack in der Hand, &eSchleich-Rechtsklick&r auf eine Kiste, und was im Filter steht, wandert in den Rucksack. Vor dem Bauen: Fackeln, Stufen und Baublöcke mit einem Klick einpacken.",
          ],
          tasks=[task_item("sophisticatedbackpacks:restock_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["deposit"], icon="sophisticatedbackpacks:restock_upgrade", optional=True),

    quest("tool_swapper", 10.5, 2, "Bau ein Werkzeugtausch-Upgrade",
          subtitle="Immer das richtige Werkzeug in der Hand.",
          description=[
              "Oben &6Redstone, Holzschwert, Redstone&r, Mitte &6Holzspitzhacke, Upgrade-Basis, Holzaxt&r, unten &6Eisen, Holzschaufel, Eisen&r.",
              "",
              "Schlägst du auf einen Block, nimmt es das passende Werkzeug aus dem Rucksack in die Hand: Spitzhacke, Axt, Schaufel, Schwert. Klappt auch mit Silent Gear.",
          ],
          tasks=[task_item("sophisticatedbackpacks:tool_swapper_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["stack_starter"], icon="sophisticatedbackpacks:tool_swapper_upgrade", optional=True),

    quest("bp_smelting", 2.5, 3.8, "Schmilz im Rucksack",
          subtitle="Ein Ofen, der mitläuft.",
          description=[
              "Redstone in die Ecken, Eisen oben, links und rechts, ein &6Ofen&r unten, die Upgrade-Basis in die Mitte.",
              "",
              "Im eigenen Tab liegen Eingang, Brennstoff und Ausgang wie in einem Ofen, gleich schnell. Rohes Eisen schmilzt so auf dem Heimweg.",
          ],
          tasks=[task_item("sophisticatedbackpacks:smelting_upgrade", 1)],
          rewards=[reward_item("minecraft:coal", 16), reward_xp(3)],
          deps=["crafting"], icon="sophisticatedbackpacks:smelting_upgrade", optional=True),

    quest("bp_compacting", 4.5, 3.8, "Pack Kleinkram zusammen",
          subtitle="Das Kompaktier-Upgrade.",
          description=[
              "Eisen in die oberen Ecken, &6vier Kolben&r um die Upgrade-Basis, Redstone in die unteren Ecken.",
              "",
              "Es presst Items, die ein 2x2-Rezept haben, sofort zum Block zusammen, zum Beispiel Tonklumpen oder Quarz. 3x3-Rezepte wie Nuggets zu Barren kann erst die fortgeschrittene Version aus Stufe 2.",
          ],
          tasks=[task_item("sophisticatedbackpacks:compacting_upgrade", 1)],
          rewards=[reward_item("minecraft:piston", 2), reward_xp(3)],
          deps=["void"], icon="sophisticatedbackpacks:compacting_upgrade", optional=True),

    quest("bp_tank", 6.5, 3.8, "Trag Flüssigkeit im Rucksack",
          subtitle="Das Tank-Upgrade.",
          description=[
              "Die Upgrade-Basis in die Mitte, &6acht Glas&r drumherum.",
              "",
              "Ein Tank im Rucksack, den du mit Eimern füllst und leerst. Zusammen mit dem &6Pump-Upgrade&r (Glas, Eimer, Kolben, Klebriger Kolben) saugt er Flüssigkeit auf oder legt sie ab.",
          ],
          tasks=[task_item("sophisticatedbackpacks:tank_upgrade", 1)],
          rewards=[reward_item("minecraft:bucket", 2), reward_xp(3)],
          deps=["feeding"], icon="sophisticatedbackpacks:tank_upgrade", optional=True),

    quest("bp_list", 8.5, 3.8, "Kenne jedes Rucksack-Upgrade",
          subtitle="Eine Zeile pro Upgrade.",
          description=[
              "&6Pickup&r hebt auf, &6Magnet&r zieht heran, &6Filter&r regelt, was Trichter hinein dürfen, &6Lager&r leert in Kisten, &6Auffüllen&r holt aus Kisten, &6Refill&r füllt die Hotbar nach.",
              "&6Leere&r löscht, &6Futter&r füttert, &6Werkbank&r und &6Steinsäge&r craften, &6Schmelzen&r, &6Räuchern&r, &6Hochofen&r und ihre Auto-Versionen garen, &6Kompaktieren&r presst zusammen.",
              "&6Tank&r und &6Pumpe&r für Flüssigkeit, &6Batterie&r für Strom, &6XP-Pumpe&r für Erfahrung, &6Amboss&r und &6Schmiedetisch&r zum Mitnehmen, &6Jukebox&r spielt Platten, &6Werkzeugtausch&r wählt das Werkzeug.",
              "&6Stack-Upgrades&r: Starter 1,5-fach und I zweifach ab Stufe 1, II vierfach ab Stufe 2, III achtfach ab Stufe 3, IV sechzehnfach ab Stufe 4. Fortgeschrittene Upgrades öffnen in Stufe 2, &6Inception&r und &6Everlasting&r in Stufe 3.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["restock"], icon="sophisticatedbackpacks:filter_upgrade", optional=True),

    # ---- Schubladen (Functional Storage) -----------------------------------------------------
    quest("drawers", 0, 8.5, "&6&lBau eine Schublade",
          subtitle="Tausende einer Sorte in einem Block.",
          description=[
              "Eine &6Holztruhe&r in die Mitte, &6acht Bretter&r drumherum. Jede Holzsorte geht, sie ändert nur das Aussehen.",
              "",
              "Die 1x1-Schublade speichert genau &eeine Sorte&r, davon &e32 Stapel&r, also 2 048 Bruchstein. &eRechtsklick&r legt hinein, &eDoppelklick&r alles Passende aus dem Inventar, &eLinksklick&r nimmt eins, &eSchleich-Linksklick&r einen Stapel.",
              "",
              "&cAchtung:&r Jeder Schlag auf die Front holt Items heraus. Zum Abbauen mit der Axt auf die Seite schlagen, der Inhalt bleibt drin.",
          ],
          tasks=[task_item("functionalstorage:oak_1", 4)],
          rewards=[reward_item("minecraft:oak_log", 32), reward_table("s1_common")],
          icon="functionalstorage:oak_1", size=1.75, shape="rsquare"),

    quest("drawers_2", 2.5, 7.5, "Bau eine 1x2-Schublade",
          subtitle="Zwei Sorten, eine Front.",
          description=[
              "&6Zwei Holztruhen&r oben und unten in der Mitte, &6sieben Bretter&r drumherum. Gibt &ezwei&r Schubladen.",
              "",
              "Zwei Fächer übereinander mit je &e16 Stapeln&r. Gut für Paare: Kohle und Holzkohle, Eisen- und Kupferbarren, Samen und Weizen.",
          ],
          tasks=[task_item("functionalstorage:oak_2", 2)],
          rewards=[reward_item("minecraft:chest", 2)],
          deps=["drawers"], icon="functionalstorage:oak_2"),

    quest("drawers_4", 4.5, 7.5, "Bau eine Schubladenwand",
          subtitle="2x2-Schubladen für die bunte Mischung.",
          description=[
              "&6Vier Holztruhen&r in die Ecken, &6fünf Bretter&r dazwischen. Gibt &evier&r Schubladen.",
              "",
              "Vier Fächer mit je &e8 Stapeln&r, die beste Wahl für viele Sorten: Erze, Barren, Farbstoffe, Mob-Drops. Mit dem Lager-Upgrade im Rucksack räumst du die Wand mit einem Klick pro Schublade ein.",
          ],
          tasks=[task_item("functionalstorage:oak_4", 4)],
          rewards=[reward_item("minecraft:chest", 4), reward_xp(3)],
          deps=["drawers_2"], icon="functionalstorage:oak_4"),

    quest("config_tool", 6.5, 7.5, "Sperr eine Schublade",
          subtitle="Das Configuration Tool.",
          description=[
              "&6Fünf Papier&r, &6zwei Goldbarren&r, eine &6Schublade&r und ein &6Smaragd&r.",
              "",
              "Eine gesperrte Schublade merkt sich ihre Sorte auch leer, so landet nie etwas Falsches in der Eisen-Schublade. &eSchleich-Rechtsklick in die Luft&r wechselt den Modus (Sperren, Mengen, Items, Upgrades, Füllstand), &eRechtsklick&r auf die Schublade wendet ihn an.",
          ],
          tasks=[task_item("functionalstorage:configuration_tool", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["drawers_4"], icon="functionalstorage:configuration_tool"),

    quest("puller", 8.5, 7.5, "Lass die Schublade selbst ziehen",
          subtitle="Das Puller Upgrade.",
          description=[
              "&6Sechs Stein&r, ein &6Trichter&r oben, eine &6Schublade&r in der Mitte, &6Redstone&r unten. Die Schublade wird verbraucht.",
              "",
              "Rechtsklick mit dem Upgrade auf die Schublade setzt es ein. Es zieht &e4 Items alle 4 Ticks&r aus dem Block auf einer Seite. Die Seite wählst du im Menü (Rechtsklick auf den Rahmen) per Rechtsklick auf das Upgrade.",
          ],
          tasks=[task_item("functionalstorage:puller_upgrade", 1)],
          rewards=[reward_item("minecraft:hopper", 2)],
          deps=["config_tool"], icon="functionalstorage:puller_upgrade"),

    quest("pusher", 10.5, 7.5, "Lass die Schublade selbst schieben",
          subtitle="Das Pusher Upgrade.",
          description=[
              "&6Sechs Stein&r, &6Redstone&r oben, eine &6Schublade&r in der Mitte, ein &6Trichter&r unten.",
              "",
              "Es schiebt so schnell, wie der Puller zieht, in den Block daneben. Eine Schublade voll Kohle versorgt so Öfen oder ein Förderband. Create-Trichter gehen auch ohne Upgrade, Schubladen sind normale Inventare.",
          ],
          tasks=[task_item("functionalstorage:pusher_upgrade", 1)],
          rewards=[reward_item("create:andesite_alloy", 16), reward_xp(5)],
          deps=["puller"], icon="functionalstorage:pusher_upgrade"),

    quest("redstone_upgrade", 12.5, 7.5, "Lass die Schublade melden",
          subtitle="Das Redstone Upgrade.",
          description=[
              "&6Vier Redstone&r in die Ecken, &6zwei Redstoneblöcke&r oben und unten, &6zwei Komparatoren&r an den Seiten, eine &6Schublade&r in die Mitte.",
              "",
              "Die Schublade gibt ein Signal aus, das mit dem Füllstand steigt. Damit schaltest du eine Create-Anlage über eine Kupplung ab, sobald das Lager voll ist.",
          ],
          tasks=[task_item("functionalstorage:redstone_upgrade", 1)],
          rewards=[reward_item("minecraft:redstone", 16)],
          deps=["pusher"], icon="functionalstorage:redstone_upgrade", optional=True),

    quest("framed", 2.5, 9.5, "Verkleide eine Schublade",
          subtitle="Framed Drawers in deinem Baustil.",
          description=[
              "Eine &6Holztruhe&r umgeben von &6acht Eisennuggets&r.",
              "",
              "Zum Verkleiden im Raster: erster Platz der Block für außen, zweiter für innen, dritter die Schublade, ein vierter Block färbt die Leisten. Passt zu Andesit-Gehäusen oder Steinziegeln.",
          ],
          tasks=[task_item("functionalstorage:framed_1", 1)],
          rewards=[reward_item("minecraft:iron_nugget", 16)],
          deps=["drawers_2"], icon="functionalstorage:framed_1", optional=True),

    quest("fluid", 4.5, 9.5, "Bau eine Flüssigkeitsschublade",
          subtitle="Eine Sorte Flüssigkeit pro Fach.",
          description=[
              "Ein &6Eimer&r in der Mitte, &6acht Bretter&r drumherum. 1x2 und 2x2 gibt es mit zwei und vier Eimern.",
              "",
              "Eimer in der Hand und Rechtsklick füllt oder leert sie. Create-Rohre können sie ebenfalls füllen und leeren.",
          ],
          tasks=[task_item("functionalstorage:fluid_1", 1)],
          rewards=[reward_item("minecraft:bucket", 2)],
          deps=["drawers_4"], icon="functionalstorage:fluid_1", optional=True),

    quest("water_gen", 4.5, 11.3, "Mach Wasser aus dem Nichts",
          subtitle="Das Water Generator Upgrade.",
          description=[
              "&6Sechs Stein&r, &6zwei Wassereimer&r oben und unten, ein leerer &6Eimer&r in der Mitte. In eine Flüssigkeitsschublade gesetzt, füllt sie sich mit &bWasser&r.",
              "",
              "Ein Rohr daran liefert Wasser für Waschanlage, Mixer oder Beton, ganz ohne Quelle im Boden.",
          ],
          tasks=[task_item("functionalstorage:water_generator_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["fluid"], icon="functionalstorage:water_generator_upgrade", optional=True),

    quest("drawer_void", 6.5, 9.5, "Lass volle Schubladen löschen",
          subtitle="Das Void Upgrade.",
          description=[
              "Eine &6Schublade&r in der Mitte, &6acht Obsidian&r drumherum.",
              "",
              "Die Schublade nimmt weiter an, wenn sie voll ist, und löscht den Überschuss. Keine Förderstrecke verstopft mehr. Hinter einer Bruchsteinmaschine bleibt sie bei 2 048, bring den Vorrat vorher zum Obelisken.",
          ],
          tasks=[task_item("functionalstorage:void_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["config_tool"], icon="functionalstorage:void_upgrade", optional=True),

    quest("collector", 8.5, 9.5, "Sammel Items vom Boden",
          subtitle="Das Collector Upgrade.",
          description=[
              "&6Vier Stein&r in die Ecken, &6zwei Trichter&r oben und unten, &6zwei Redstone&r an den Seiten, eine &6Schublade&r in die Mitte.",
              "",
              "Es saugt Items auf, die vor der eingestellten Seite liegen. Gut unter Kakteen, Zuckerrohr oder einer Mob-Falle.",
          ],
          tasks=[task_item("functionalstorage:collector_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["puller"], icon="functionalstorage:collector_upgrade", optional=True),

    quest("drawer_dripping", 10.5, 9.5, "Lass Lava tropfen",
          subtitle="Dripping und Obsidian Generator Upgrade.",
          description=[
              "&6Dripping Upgrade:&r Stein rundum, ein &6Spitzer Tropfstein&r oben, ein &6Kessel&r in der Mitte, ein &6Lavaeimer&r unten. Vier Dripping Upgrades und ein Water Generator Upgrade ergeben formlos das &6Obsidian Generator Upgrade&r.",
              "",
              "Wie beim Wasser füllt sich die Schublade von selbst. Obsidian brauchst du für das Leere-Upgrade und das Void Upgrade.",
          ],
          tasks=[task_item("functionalstorage:dripping_upgrade", 1)],
          rewards=[reward_item("minecraft:obsidian", 4), reward_xp(5)],
          deps=["water_gen", "collector"], icon="functionalstorage:dripping_upgrade", optional=True),

    # ---- Truhen und Fässer (Sophisticated Storage) ------------------------------------------
    quest("barrel", 0, 15.5, "&6&lBau ein aufwertbares Fass",
          subtitle="Aufwerten statt ersetzen.",
          description=[
              "&6Sechs Bretter&r, &6zwei Holzstufen&r oben und unten in der Mitte, ein &6Hebel&r in die Mitte. Es übernimmt das Aussehen der Holzsorte.",
              "",
              "&e27 Plätze&r und &eein Upgrade-Platz&r. Der große Vorteil: Du wertest es &edirekt in der Welt&r auf, Block und Inhalt bleiben stehen. Fässer lassen sich in jede Richtung drehen und aneinanderbauen.",
          ],
          tasks=[task_item("sophisticatedstorage:barrel", 2)],
          rewards=[reward_item("minecraft:lever", 4), reward_table("s1_common")],
          icon="sophisticatedstorage:barrel", size=1.75, shape="rsquare"),

    quest("copper_tier", 2.5, 14.5, "Werte auf Kupfer auf",
          subtitle="Kupfer ist genau dafür da.",
          description=[
              "&6Acht Kupferbarren&r um einen &6Hebel&r: das &6Basic to Copper Tier Upgrade&r. Rechtsklick damit auf das platzierte Fass, fertig.",
              "",
              "Aus 27 Plätzen werden &e45&r, der Inhalt bleibt. Mit Create-Erzverarbeitung hast du Kupfer in Mengen.",
          ],
          tasks=[task_item("sophisticatedstorage:basic_to_copper_tier_upgrade", 1)],
          rewards=[reward_item("minecraft:copper_ingot", 16)],
          deps=["barrel"], icon="sophisticatedstorage:basic_to_copper_tier_upgrade"),

    quest("iron_tier", 4.5, 14.5, "Werte auf Eisen auf",
          subtitle="54 Plätze und ein zweiter Upgrade-Platz.",
          description=[
              "&6Copper to Iron Tier Upgrade:&r &6vier Eisenbleche&r aus der Create-Presse um einen &6Hebel&r. Oder direkt im Raster: ein Fass in die Mitte, acht Eisenbarren drumherum.",
              "",
              "&e54 Plätze&r, &ezwei Upgrade-Plätze&r. Eisen ist das Beste in Stufe 1. Gold (81 Plätze, 3 Upgrades) kommt in Stufe 2, Diamant (108, 4) in Stufe 3, Netherit (132, 5) in Stufe 4.",
          ],
          tasks=[task_item("sophisticatedstorage:iron_barrel", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(5)],
          deps=["copper_tier"], icon="sophisticatedstorage:basic_to_iron_tier_upgrade"),

    quest("storage_upgrade_base", 6.5, 14.5, "Bau eine Upgrade-Basis für Truhen",
          subtitle="Nicht dieselbe wie beim Rucksack.",
          description=[
              "&6Fünf Bretter&r und &6vier Eisenbarren&r im Schachbrettmuster.",
              "",
              "Truhen und Fässer nehmen fast dieselben Upgrades wie der Rucksack. Ein fertiges Upgrade lässt sich zwischen Rucksack und Lager umbauen, JEI zeigt die Rezepte.",
          ],
          tasks=[task_item("sophisticatedstorage:upgrade_base", 2)],
          rewards=[reward_item("minecraft:iron_ingot", 8)],
          deps=["iron_tier"], icon="sophisticatedstorage:upgrade_base"),

    quest("storage_stack", 8.5, 14.5, "Verdopple ein Fass mit Holz",
          subtitle="Stack-Upgrade Stufe 1 für Truhen.",
          description=[
              "Die Upgrade-Basis in die Mitte, &6acht Stämme&r drumherum.",
              "",
              "Jeder Platz fasst das &eDoppelte&r. Ein Eisenfass mit diesem Upgrade hält so viel wie vier Truhen. Höchstens &ezwei Stack-Upgrades&r pro Truhe oder Fass.",
          ],
          tasks=[task_item("sophisticatedstorage:stack_upgrade_tier_1", 1)],
          rewards=[reward_item("minecraft:oak_log", 32), reward_xp(5)],
          deps=["storage_upgrade_base"], icon="sophisticatedstorage:stack_upgrade_tier_1"),

    quest("hopper", 10.5, 14.5, "Bau einen Trichter ins Fass",
          subtitle="Das Trichter-Upgrade.",
          description=[
              "Ein &6Trichter&r oben, &6zwei Eisenbarren&r neben der Upgrade-Basis, &6drei Redstone&r unten.",
              "",
              "Es zieht aus dem Block &eüber&r dem Lager und schiebt in den Block &edarunter&r, jede Richtung mit eigenem Filter. Unter einer Farm sammelt es die Ernte, und nur die Samen gehen weiter nach unten.",
          ],
          tasks=[task_item("sophisticatedstorage:hopper_upgrade", 1)],
          rewards=[reward_item("minecraft:hopper", 2), reward_xp(3)],
          deps=["storage_stack"], icon="sophisticatedstorage:hopper_upgrade"),

    quest("controller", 12.5, 14.5, "&6Bau einen Lagerkern",
          subtitle="Viele Truhen, ein Zugang.",
          description=[
              "&6Vier Stein&r in die Ecken, &6zwei Komparatoren&r oben und unten, &6zwei Bretter&r an den Seiten, ein Sophisticated-Fass oder eine -Truhe der Holzstufe in die Mitte.",
              "",
              "Alle Truhen und Fässer, die ihn oder einander berühren, werden ein Lager. Rechtsklick mit einem Item legt es passend ab, Trichter und Rohre am Kern verteilen auf den Verbund. &6Storage Connector&r (Stöcke und Bretter, gibt vier) überbrücken Lücken.",
              "",
              "Ein echtes Netz mit Suche bringt erst &bApplied Energistics 2&r in Stufe 3.",
          ],
          tasks=[task_item("sophisticatedstorage:controller", 1)],
          rewards=[reward_item("minecraft:comparator", 2), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["hopper"], icon="sophisticatedstorage:controller", size=1.5, shape="hexagon"),

    quest("chest", 2.5, 16.5, "Bau eine aufwertbare Truhe",
          subtitle="Wie das Fass, nur als Truhe.",
          description=[
              "&6Acht Bretter&r um einen &6Hebel&r, oder eine Vanilla-Truhe und ein Hebel.",
              "",
              "Zwei nebeneinander werden eine &eDoppeltruhe&r. Fässer stapeln sich platzsparender, Truhen sehen in Wohnräumen schöner aus.",
          ],
          tasks=[task_item("sophisticatedstorage:chest", 1)],
          rewards=[reward_item("minecraft:oak_planks", 32)],
          deps=["barrel"], icon="sophisticatedstorage:chest", optional=True),

    quest("basic_tier", 4.5, 16.5, "Wandle Vanilla-Truhen um",
          subtitle="Mit Inhalt, ohne Ausräumen.",
          description=[
              "Ein &6Hebel&r in der Mitte, &6vier Stöcke&r oben, unten und an den Seiten: das &6Basic Tier Upgrade&r.",
              "",
              "Rechtsklick auf eine platzierte Vanilla-Truhe oder ein Vanilla-Fass macht die Sophisticated-Version daraus, alles bleibt drin. Danach geht es weiter auf Kupfer und Eisen.",
          ],
          tasks=[task_item("sophisticatedstorage:basic_tier_upgrade", 1)],
          rewards=[reward_xp(3)],
          deps=["copper_tier"], icon="sophisticatedstorage:basic_tier_upgrade", optional=True),

    quest("limited_barrel", 6.5, 16.5, "Bau ein Eingeschränktes Fass",
          subtitle="Schublade oder Fass? Beides.",
          description=[
              "Bretter, Holzstufen und ein Hebel, je nach Variante in anderem Muster, JEI zeigt alle vier.",
              "",
              "&6I&r: ein Fach mit &e32 Stapeln&r. &6II&r: zwei mit je 16. &6III&r: drei mit je 10. &6IV&r: vier mit je 8. Anders als Functional Storage lassen sie sich auf Kupfer und Eisen aufwerten und nehmen Sophisticated-Upgrades.",
          ],
          tasks=[task_item("sophisticatedstorage:limited_barrel_1", 1)],
          rewards=[reward_xp(3)],
          deps=["storage_stack"], icon="sophisticatedstorage:limited_barrel_1", optional=True),

    quest("stack_plus", 8.5, 16.5, "Verdreifache ein Fass mit Kupfer",
          subtitle="Stack-Upgrade Stufe 1 Plus.",
          description=[
              "Das &6Stack-Upgrade Stufe 1&r in die Mitte, Kupferbarren oben und an den Seiten, unten Kupferblock, Kupferbarren, Kupferblock.",
              "",
              "Aus doppelt wird &edreifach&r: ein Eisenfass hält dann 54 mal drei Stapel. Stufe 2 (vierfach) öffnet mit dem Messingwerk.",
          ],
          tasks=[task_item("sophisticatedstorage:stack_upgrade_tier_1_plus", 1)],
          rewards=[reward_item("minecraft:copper_block", 4), reward_xp(5)],
          deps=["storage_stack"], icon="sophisticatedstorage:stack_upgrade_tier_1_plus", optional=True),

    quest("storage_io", 12.5, 16.5, "Häng Rohre an den Verbund",
          subtitle="Storage Input, Output und I/O.",
          description=[
              "&6Storage I/O:&r Stein in die Ecken, Bretter oben und unten, links ein Repeater, rechts ein Goldbarren, ein Fass der Holzstufe in die Mitte. &6Input&r und &6Output&r sind dasselbe mit Repeater und Gold oben und unten.",
              "",
              "In den Verbund am Lagerkern gesetzt, nimmt der I/O Items von Rohren an und gibt sie ab. Input nur hinein, Output nur heraus, beide schonen den Server.",
          ],
          tasks=[task_item("sophisticatedstorage:storage_io", 1)],
          rewards=[reward_item("minecraft:gold_ingot", 4), reward_xp(5)],
          deps=["controller"], icon="sophisticatedstorage:storage_io", optional=True),

    quest("storage_link", 14.5, 15.5, "Verbinde ein entferntes Fass",
          subtitle="Die Lagerverbindung.",
          description=[
              "&6Lagerverbindung:&r Enderperle und Brett oben, Repeater und Stein unten. Oder formlos: Lagerkern und Enderperle gibt drei.",
              "",
              "Mit dem &6Lagerwerkzeug&r (Enderperle, Eisenbarren, Redstonefackel, zwei Stöcke) erst den Lagerkern, dann die Verbindung anklicken. So hängt ein Truhenblock in einem anderen Raum am selben Kern.",
          ],
          tasks=[task_item("sophisticatedstorage:storage_link", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["controller"], icon="sophisticatedstorage:storage_link", optional=True),

    quest("packing_tape", 2.5, 18.3, "Zieh um, ohne auszuräumen",
          subtitle="Packband.",
          description=[
              "Formlos: &6ein Schleimball&r und &6ein Papier&r.",
              "",
              "Rechtsklick mit dem Band auf eine volle Truhe, dann abbauen. Sie fällt als ein Item samt Inhalt heraus. Eine Rolle hält mehrere Einsätze, der Tooltip zeigt den Rest.",
          ],
          tasks=[task_item("sophisticatedstorage:packing_tape", 1)],
          rewards=[reward_item("minecraft:slime_ball", 2)],
          deps=["chest"], icon="sophisticatedstorage:packing_tape", optional=True),

    quest("tiers", 6.5, 18.3, "Kenne jede Truhenstufe",
          subtitle="Plätze und Upgrade-Plätze auf einen Blick.",
          description=[
              "&6Holz&r: 27 Plätze, 1 Upgrade. &6Kupfer&r: 45, 1. &6Eisen&r: 54, 2. Alle drei in Stufe 1.",
              "&6Gold&r: 81, 3, Stufe 2. &6Diamant&r: 108, 4, Stufe 3. &6Netherit&r: 132, 5, Stufe 4.",
              "&6Stack-Upgrades für Truhen&r: I zweifach und I Plus dreifach ab Stufe 1, II vierfach ab Stufe 2, III achtfach ab Stufe 3, IV sechzehnfach ab Stufe 4, V zweiunddreißigfach ab Stufe 5.",
              "Rucksäcke: Leder 27 und 1, Kupfer 45 und 1, Eisen 54 und 2 (Stufe 2), Gold 81 und 3, Diamant 108 und 5 (Stufe 3), Netherit 120 und 7 (Stufe 4).",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(5)],
          deps=["iron_tier"], icon="sophisticatedstorage:iron_barrel", optional=True),

    # ---- Create-Tresor -----------------------------------------------------------------------
    quest("vault", 0, 22, "&6Bau einen Tresor",
          subtitle="Das Lager am Ende der Create-Straße.",
          description=[
              "&6Eisenblech&r, ein &6Holzfass&r, &6Eisenblech&r übereinander.",
              "",
              "Ein &6Tresor&r von Create fasst &e20 Stapel pro Block&r. Hinein und heraus geht es nur mit Trichtern, Bändern, Armen oder Rohren, von Hand nicht. Ein Komparator daran meldet den Füllstand.",
          ],
          tasks=[task_item("create:item_vault", 1)],
          rewards=[reward_item("create:iron_sheet", 4), reward_xp(3)],
          deps=["barrel"], icon="create:item_vault", size=1.5, shape="rsquare"),

    quest("vault_big", 2.5, 22, "Bau einen großen Tresor",
          subtitle="Bis zu 81 Blöcke, ein Inventar.",
          description=[
              "Stell Tresore aneinander, sie verschmelzen zu einem. Grundfläche bis &e3 x 3&r, Länge bis dreimal die Breite. Das sind bis zu 81 Blöcke und &e1 620 Stapel&r in einem Inventar.",
              "",
              "Ein Andesit-Trichter oben füllt ihn vom Förderband, einer unten holt heraus. Kein Filter, also ein Tresor pro Straße.",
          ],
          tasks=[task_item("create:item_vault", 9)],
          rewards=[reward_item("create:andesite_alloy", 16), reward_table("s1_uncommon"), reward_xp(5)],
          deps=["vault"], icon="create:item_vault"),

    # ---- Aufräumen ---------------------------------------------------------------------------
    quest("trash", 0, 25.5, "Bau einen Mülleimer",
          subtitle="Was hineinfällt, ist weg.",
          description=[
              "&6Drei Stein&r oben, eine &6Holztruhe&r in der Mitte, &6fünf Bruchstein&r drumherum: die &6Item Trash Can&r.",
              "",
              "Sie löscht alles, was hineinkommt, per Hand, Trichter oder Förderband. Ihr Filter hat &e9 Plätze&r als Whitelist oder Blacklist.",
              "",
              "&cAchtung:&r Bruchstein vorher abgeben, der Obelisk braucht ihn. &e/kw deposit all&r gibt alles ab, was das Ziel brauchen kann.",
          ],
          tasks=[task_item("trashcans:item_trash_can", 1)],
          rewards=[reward_xp(3), reward_table("s1_common")],
          icon="trashcans:item_trash_can", size=1.5, shape="rsquare"),

    quest("liquid_trash", 2.5, 25.5, "Bau einen Flüssigkeitsmüll",
          subtitle="Für überschüssiges Wasser und Lava.",
          description=[
              "Wie der Mülleimer, nur mit einem &6Eimer&r statt der Truhe.",
              "",
              "Nützlich, wenn eine Create-Anlage mehr pumpt, als du brauchst. Eigener Filter für bis zu 9 Flüssigkeiten.",
          ],
          tasks=[task_item("trashcans:liquid_trash_can", 1)],
          rewards=[reward_xp(3)],
          deps=["trash"], icon="trashcans:liquid_trash_can", optional=True),

    quest("ultimate_trash", 4.5, 25.5, "Bau den Alles-Müll",
          subtitle="Item, Flüssigkeit und Strom in einem.",
          description=[
              "&6Energy Trash Can&r: wie der Mülleimer, nur mit Redstone statt der Truhe. Item-, Fluid- und Energy Trash Can formlos zusammen ergeben die &6Ultimate Trash Can&r.",
              "",
              "Ein Block, der alles schluckt. Praktisch hinter einer Anlage, die Gegenstände und Flüssigkeit zugleich ausspuckt.",
          ],
          tasks=[task_item("trashcans:ultimate_trash_can", 1)],
          rewards=[reward_xp(3)],
          deps=["liquid_trash"], icon="trashcans:ultimate_trash_can", optional=True),

    quest("sack", 6.5, 25.5, "Näh einen Sack",
          subtitle="Neun Plätze, und schwer.",
          description=[
              "Ein &6Faden&r oben in der Mitte, &6sieben Flachs&r drumherum. Flachs wächst wild, die Samen kannst du anbauen.",
              "",
              "Der &6Sack&r von Supplementaries hat &e9 Plätze&r und lässt sich als Block abstellen. Wer mehr als zwei trägt, wird langsamer.",
          ],
          tasks=[task_item("supplementaries:sack", 1)],
          rewards=[reward_item("minecraft:string", 8)],
          deps=["trash"], icon="supplementaries:sack", optional=True),

    # ---- Ziel und Ausblick ---------------------------------------------------------------------
    quest("organised", 17, 9, "&6&lBring Ordnung ins Kronwerk",
          subtitle="Eine Basis, in der man Dinge wiederfindet.",
          description=[
              "Zeig acht 2x2-Schubladen, zwei Eisenfässer, einen Lagerkern und einen Tresor.",
              "",
              "Damit hast du alle Säulen eines guten Lagers: einen &6Rucksack&r mit dem Upgrade für deinen Tag, eine &6Schubladenwand&r für Massenware, &6aufgewertete Fässer&r am &6Lagerkern&r für den Rest und einen &6Tresor&r am Ende der Create-Straße. Die Basis ist bereit für das, was Create ausspuckt.",
          ],
          tasks=[task_item("functionalstorage:oak_4", 8), task_item("sophisticatedstorage:iron_barrel", 2),
                 task_item("sophisticatedstorage:controller", 1), task_item("create:item_vault", 1)],
          rewards=[reward_table("s1_rare"), reward_xp(10)],
          deps=["stack_starter", "pusher", "controller", "vault"], icon="sophisticatedstorage:iron_barrel",
          size=2.5, shape="gear"),

    quest("outlook", 17, 12.5, "Lies, was die nächsten Stufen bringen",
          subtitle="Mehr Platz mit jeder Stufe.",
          description=[
              "&6Stufe 2:&r Kupfer- und Eisenrucksack, die &6Compacting Drawer&r (Nuggets, Barren und Blöcke in einem), Kupfer- und Gold-Upgrades für Schubladen, Goldtruhen und -fässer, fortgeschrittene Rucksack-Upgrades. Mit Netherquarz der &6Storage Controller&r von Functional Storage, der alle Schubladen im Umkreis von 8 Blöcken an einer Front sammelt.",
              "",
              "&6Stufe 3:&r Gold- und Diamantrucksack, Diamanttruhen, die &6Ender Drawer&r, und &bApplied Energistics 2&r oder &3Refined Storage&r mit Suche und Autocrafting.",
              "",
              "Gesperrte Items zeigen im Tooltip, wann sie öffnen. Sammeln darfst du sie schon.",
          ],
          tasks=[task_checkmark("Gelesen")],
          rewards=[reward_xp(3)],
          deps=["organised"], icon="minecraft:chest", optional=True),
]

images = [
    head("title", "Lager und Ordnung", 0, -3.6, height=1.5, kind="title"),
    head("backpacks", "Rucksäcke", 2.0, -1.4, colour="brass"),
    head("drawers", "Schubladen", 0, 6.0, colour="nature"),
    head("chests", "Truhen und Fässer", 0, 13.0, colour="stone"),
    head("vault", "Create-Tresor", 0, 20.4, colour="brass"),
    head("cleanup", "Aufräumen", 0, 23.9, colour="stone"),
    head("goal", "Ziel", 16.2, 6.8, colour="brass"),
]

chapter(C, "Lager", "sophisticatedbackpacks:backpack", "storage", quests, shape="circle", order=5,
        subtitle=["Rucksäcke, Schubladen, Truhen und Tresore für die erste Woche."], images=images)
