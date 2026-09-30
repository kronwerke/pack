"""Ars Nouveau in stage 2: the Mage's Spell Book and the tier 2 glyphs, Source Relays, the Ritual
Brazier with the rituals that are open (awakening, flight, disintegration, warping, the island
rituals and Summon Wilden are stage 3), familiars, turrets, warp scrolls, the Wixie, and the
places where Ars meets Create: the Kronwerke blaze burner recipe, Ars Technica's calibrated
precision mechanism and Source Motor. Tier 3 glyphs and the Archmage book are stage 3."""
from ftbq import (chapter, quest, task_item, task_checkmark, reward_item, reward_table,
                  reward_xp, banner, img, item_texture)

C = "ars_apprentice"


def pic(item_id, size=32):
    return img(item_texture(item_id), size, size)


quests = [
    # ---- Glyphen der zweiten Stufe -------------------------------------------
    quest("welcome", 0, 0, "&dZauberbuch des Magiers",
          subtitle="Das zweite Buch: stärkere Glyphen, mehr Mana.",
          description=[
              "Mit &6Stufe 2&r öffnet sich die nächste Ebene von Ars Nouveau. Das &6Zauberbuch des Magiers&r (Mage's Spell Book) kann Glyphen der &eStufe 2&r benutzen und hebt dein maximales Mana und deine Regeneration deutlich an.",
              "",
              "Du craftest es formlos aus deinem &6Zauberbuch für Anfänger&r, &e1 Obsidian&r, &e3 Diamanten&r, &e2 Quarzblöcken&r und &e2 Lohenruten&r. Quarz und Lohenruten gibt es erst im Nether, der mit dieser Stufe geöffnet wurde. Alle gelernten Glyphen und gespeicherten Zauber wandern ins neue Buch.",
              "",
              "In diesem Kapitel lernst du die neuen Glyphen, bewegst Quelle über weite Strecken, führst &dRituale&r durch, baust &dZaubertürme&r und verbindest Ars mit &6Create&r. Die Glyphen der dritten Stufe und das Erzmagier-Buch kommen mit &6Stufe 3&r.",
          ],
          tasks=[task_item("ars_nouveau:apprentice_spell_book", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 16), reward_table("s2_common")],
          icon="ars_nouveau:apprentice_spell_book", size=2.0, shape="hexagon"),

    quest("tier2", 2.5, 0, "&dGlyphen der Stufe 2",
          subtitle="Teurer, aber sie verändern alles.",
          description=[
              "Glyphen der zweiten Stufe lernst du wie gewohnt am &6Tisch des Schreibers&r, nur mit dem neuen Buch in der Hand. Jede kostet &e55 Erfahrungspunkte&r, das sind etwa &e5 Level&r, dazu ihre Zutaten.",
              "",
              "Die wichtigsten Neuerungen sind die &aVerstärkungen&r: Fläche, Durchschlag, Dauer, Dämpfen, Glück und Behutsamkeit. Mit ihnen werden deine alten Zauber plötzlich viel mächtiger. Dazu kommen neue Effekte wie Heilen, Wachsen, Schmelzen und Explosion.",
              "",
              "&eTipp:&r Viele Rezepte brauchen Nether-Zutaten wie Lohenruten oder Netherziegel. Plane einen gemeinsamen Nether-Ausflug mit deinen Freunden.",
          ],
          tasks=[task_checkmark("Verstanden")],
          rewards=[reward_item("minecraft:experience_bottle", 16)],
          deps=["welcome"], icon="ars_nouveau:scribes_table"),

    quest("glyph_aoe", 4.7, -1.8, "&dAOE",
          subtitle="Aus einem Block werden neun.",
          description=[
              "&dAOE&r (Fläche) kostet nur einen &6Feuerwerksstern&r und ist die Glyphe, auf die alle gewartet haben. Hinter einem Effekt vergrößert sie den Bereich um den Zielblock.",
              "",
              "&eProjektil, Brechen, AOE&r baut eine 3x3-Fläche ab, mit zweimal AOE 5x5. &eBerühren, Ernte, AOE&r erntet ein ganzes Beet auf einmal.",
              "",
              "&cAchtung:&r Mit jedem AOE steigen die Kosten. Probier den Zauber erst an einem ungefährlichen Ort aus, ein 5x5-Loch unter den eigenen Füßen ist schnell gegraben.",
          ],
          tasks=[task_item("ars_nouveau:glyph_aoe", 1)],
          rewards=[reward_item("minecraft:gunpowder", 16), reward_xp(5)],
          deps=["tier2"], icon="ars_nouveau:glyph_aoe"),

    quest("glyph_pierce", 4.7, 0, "&dDurchschlag",
          subtitle="Durch die Wand und weiter.",
          description=[
              "&dDurchschlag&r (Pierce) braucht einen &6Pfeil&r und einen &6Wilden-Stachel&r. Hinter &dProjektil&r fliegt die Kugel durch ein weiteres Ziel. Hinter &dBrechen&r trifft der Effekt auch den Block dahinter.",
              "",
              "Zusammen mit AOE ergibt das Tiefe: &eProjektil, Brechen, AOE, Durchschlag, Durchschlag&r gräbt einen 3x3-Tunnel, drei Blöcke tief, mit einem einzigen Klick.",
          ],
          tasks=[task_item("ars_nouveau:glyph_pierce", 1)],
          rewards=[reward_item("minecraft:arrow", 32), reward_xp(5)],
          deps=["tier2"], icon="ars_nouveau:glyph_pierce"),

    quest("glyph_extend_time", 4.7, 1.8, "&dZeit verlängern",
          subtitle="Länger leuchten, länger fliegen.",
          description=[
              "&dZeit verlängern&r (Extend Time) kostet eine &6Uhr&r und einen &6Redstone-Block&r. Es verlängert alles mit einer Dauer: Tränkeffekte, beschworene Wesen und Buffs wie Nachtsicht oder Langsamer Fall.",
              "",
              "Das Gegenstück &dDauer verringert&r (Reduce Time) aus Uhr und Glowstonestaub macht Effekte kürzer, praktisch bei teuren Buffs, die du nur kurz brauchst.",
          ],
          tasks=[task_item("ars_nouveau:glyph_extend_time", 1)],
          rewards=[reward_item("minecraft:redstone_block", 2), reward_xp(5)],
          deps=["tier2"], icon="ars_nouveau:glyph_extend_time"),

    quest("glyph_fortune", 6.7, -1.8, "&dGlück und Extrakt",
          subtitle="Mehr Erz oder das Erz selbst.",
          description=[
              "Zwei Verstärkungen für deinen Bergbauzauber:",
              "",
              "&dGlück&r (Luck) aus einer &6Hasenpfote&r wirkt wie Glück auf einer Spitzhacke: mehr Drops von Erzen und mehr Beute von Monstern, die dein Zauber tötet.",
              "",
              "&dExtrakt&r (Extract) aus einem &6Smaragd&r wirkt wie Behutsamkeit: Brechen liefert den Block selbst.",
              "",
              "&cAchtung:&r Beide zusammen in einem Zauber gehen nicht. Mach dir zwei Varianten.",
          ],
          tasks=[task_item("ars_nouveau:glyph_fortune", 1), task_item("ars_nouveau:glyph_extract", 1)],
          rewards=[reward_item("minecraft:emerald", 4), reward_xp(5)],
          deps=["glyph_aoe"], icon="ars_nouveau:glyph_fortune"),

    quest("glyph_dampen", 6.7, 0, "&dDämpfen",
          subtitle="Manchmal ist weniger mehr.",
          description=[
              "&dDämpfen&r (Dampen) kostet nur einen &6Netherziegel&r und schwächt das Glied links davon. Klingt nutzlos, ist es aber nicht:",
              "",
              "Ein gedämpftes Magielicht ist schwächer und stört keine Monsterfallen. Gedämpftes Schmelzen benutzt Räucherofen-Rezepte, also brät es Essen statt Erz zu schmelzen. Gedämpftes Brechen baut nur weiche Blöcke ab und schont so Erze in einer Wand.",
          ],
          tasks=[task_item("ars_nouveau:glyph_dampen", 1)],
          rewards=[reward_item("minecraft:nether_brick", 16), reward_xp(3)],
          deps=["glyph_pierce"], icon="ars_nouveau:glyph_dampen", optional=True),

    quest("glyph_heal", 6.7, 1.8, "&dHeilen",
          subtitle="Endlich ein Heilzauber.",
          description=[
              "&dHeilen&r braucht eine &5Abschwörungsessenz&r, &e4 Glitzernde Melonenscheiben&r und einen &6Goldenen Apfel&r. Es heilt ein kleines Stück Gesundheit und kostet dich dafür etwas Hunger. Auf Untote angewendet macht es stattdessen magischen Schaden.",
              "",
              "&eSelbst, Heilen, Verstärken&r ist dein Notfallzauber. &eProjektil, Heilen&r heilt einen Freund aus der Ferne, sehr beliebt bei Bossen, die ihr gemeinsam angeht.",
          ],
          tasks=[task_item("ars_nouveau:glyph_heal", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1), reward_xp(5)],
          deps=["glyph_extend_time"], icon="ars_nouveau:glyph_heal"),

    quest("glyph_smelt", 8.7, -1.8, "&dSchmelzen",
          subtitle="Der Ofen in deinem Zauberbuch.",
          description=[
              "&dSchmelzen&r (Smelt) ist teuer: &cFeueressenz&r, &e4 Hochöfen&r und eine &6Lohenrute&r. Dafür schmilzt es Blöcke und Items direkt in der Welt: Sand wird zu Glas, Rohmetalle werden zu Barren.",
              "",
              "Setz es in deinen Bergbauzauber hinter Brechen: &eProjektil, Brechen, Schmelzen, Artikelabholung&r liefert gleich Barren. Mit AOE schmilzt es mehrere Items auf einmal, mit &dEmpfindlich&r nur Items und keine Blöcke.",
          ],
          tasks=[task_item("ars_nouveau:glyph_smelt", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 2), reward_xp(5)],
          deps=["glyph_fortune"], icon="ars_nouveau:glyph_smelt"),

    quest("glyph_grow", 8.7, 0, "&dWachsen",
          subtitle="Knochenmehl aus dem Buch.",
          description=[
              "&dWachsen&r (Grow) kostet eine &6Erdessenz&r, &e5 Knochenblöcke&r und &e3 Samen&r. Es lässt Pflanzen wachsen, als hättest du Knochenmehl benutzt.",
              "",
              "&eBerühren, Wachsen, AOE, AOE&r und danach &eBerühren, Ernte, AOE, AOE&r: zwei Zauber, und ein 5x5-Feld ist von Samen bis Ernte fertig.",
              "",
              "&cAchtung:&r Wie Knochenmehl bringt Wachsen dem &6Agronomischen Quellenlink&r keine Quelle.",
          ],
          tasks=[task_item("ars_nouveau:glyph_grow", 1)],
          rewards=[reward_item("minecraft:bone_block", 8), reward_xp(5)],
          deps=["glyph_dampen", "glyph_heal"], icon="ars_nouveau:glyph_grow"),

    quest("glyph_crush", 8.7, 1.8, "&dZerkleinern",
          subtitle="Stein zu Kies, Kies zu Sand.",
          description=[
              "&dZerkleinern&r (Crush) aus &6Erdessenz&r, &6Schleifstein&r und &6Kolben&r macht aus Stein Kies und aus Kies Sand, Blumen gibt es als doppelten Farbstoff zurück. Mit &dEmpfindlich&r arbeitet es auch auf Items, JEI zeigt alle Rezepte.",
              "",
              "Gegen Wesen macht es Schaden, besonders gegen schwimmende. Für Glas in großen Mengen ist &eZerkleinern, Zerkleinern, Schmelzen&r auf einen Haufen Bruchstein ziemlich elegant.",
          ],
          tasks=[task_item("ars_nouveau:glyph_crush", 1)],
          rewards=[reward_item("minecraft:sand", 32), reward_xp(3)],
          deps=["glyph_heal"], icon="ars_nouveau:glyph_crush", optional=True),

    quest("glyph_slowfall", 10.7, -1.8, "&dLangsamer Fall",
          subtitle="Wie eine Feder zu Boden.",
          description=[
              "&dLangsamer Fall&r (Slowfall) braucht &fLuftessenz&r, einen &6Wilden-Flügel&r, &e3 Federn&r, eine &6Lohenrute&r und &6Netherwarze&r. &eSelbst, Langsamer Fall, Zeit verlängern&r macht jeden Sprung von einer Klippe harmlos.",
              "",
              "&eTipp:&r Zusammen mit &dSprung&r aus der ersten Stufe wird das eine sehr schnelle Art zu reisen: springen, gleiten, springen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_slowfall", 1)],
          rewards=[reward_item("minecraft:feather", 16), reward_xp(3)],
          deps=["glyph_smelt"], icon="ars_nouveau:glyph_slowfall", optional=True),

    quest("glyph_conjure_water", 10.7, 0, "&dWasser beschwören",
          subtitle="Eine Quelle in der Hosentasche.",
          description=[
              "&dWasser beschwören&r kostet &bWasseressenz&r und einen &6Wassereimer&r. Es setzt Wasser an die Zielstelle oder löscht brennende Wesen, dich selbst eingeschlossen.",
              "",
              "Praktisch für Felder ohne Wasserleitung, zum Löschen im Nether und als Rettung, wenn du in Lava gefallen bist.",
          ],
          tasks=[task_item("ars_nouveau:glyph_conjure_water", 1)],
          rewards=[reward_item("minecraft:water_bucket", 1), reward_xp(3)],
          deps=["glyph_grow"], icon="ars_nouveau:glyph_conjure_water", optional=True),

    quest("glyph_flare", 10.7, 1.8, "&dFackel",
          subtitle="Feuer auf brennende Ziele.",
          description=[
              "&dFackel&r (Flare) braucht &cFeueressenz&r, &e2 Feuerzeuge&r, &e2 Feuerkugeln&r und eine &6Lohenrute&r. Trifft es ein Wesen oder einen Block, der schon brennt, explodieren Funken und richten Schaden in der Umgebung an.",
              "",
              "Der klassische Kampfzauber dazu: &eProjektil, Entzünden, Fackel&r. Erst anzünden, dann hochgehen lassen. Mit Verstärken und AOE wird daraus eine ernsthafte Waffe gegen Gruppen.",
          ],
          tasks=[task_item("ars_nouveau:glyph_flare", 1)],
          rewards=[reward_item("minecraft:fire_charge", 8), reward_xp(3)],
          deps=["glyph_crush"], icon="ars_nouveau:glyph_flare", optional=True),

    quest("arc_projectile", 12.7, -1.8, "&dArc Projectile",
          subtitle="Ars Elemental: eine Form, die im Bogen fliegt.",
          description=[
              "&bArs Elemental&r bringt eine neue Form der Stufe 2: &dArc Projectile&r aus &6Pfeil&r, &6Schneeball&r, &6Schleimball&r und &6Ender-Perle&r.",
              "",
              "Anders als das normale Projektil fällt diese Kugel im Bogen wie ein geworfener Trank. Jeder &dDurchschlag&r lässt sie einmal vom Boden abprallen. So erreichst du Ziele hinter Deckung oder über Mauern.",
          ],
          tasks=[task_item("ars_elemental:glyph_arc_projectile", 1)],
          rewards=[reward_item("minecraft:slime_ball", 8), reward_xp(3)],
          deps=["glyph_slowfall"], icon="ars_elemental:glyph_arc_projectile", optional=True),

    quest("spells2", 12.7, 0.6, "&dZauber für Fortgeschrittene",
          subtitle="Tunnel, Felder und Barren.",
          description=[
              "Mit den neuen Glyphen werden deine Zauber zu Werkzeugen, die jede Maschine alt aussehen lassen:",
              "",
              "&eTunnelbohrer:&r Projektil, Brechen, Verstärken, AOE, Durchschlag, Durchschlag, Artikelabholung.",
              "&eErzschmelze:&r Projektil, Brechen, Glück, Schmelzen, Artikelabholung.",
              "&eBehutsam:&r Projektil, Brechen, Extrakt, Artikelabholung.",
              "&eGärtner:&r Berühren, Wachsen, AOE, AOE.",
              "&eErntehelfer:&r Berühren, Ernte, AOE, AOE, Artikelabholung.",
              "&eSanitäter:&r Projektil, Heilen, Verstärken.",
              "",
              "Ein Zauber kann höchstens zehn Glyphen haben. Wenn es eng wird, lass eine Verstärkung weg oder teil den Zauber in zwei auf.",
          ],
          tasks=[task_checkmark("Zauberbuch aufgerüstet")],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["glyph_smelt", "glyph_grow"], icon="ars_nouveau:apprentice_spell_book", size=1.5, shape="diamond"),

    # ---- Quelle bewegen --------------------------------------------------------
    quest("relay", 0.5, 6.2, "&aQuellrelais",
          subtitle="Quelle über 30 Blöcke, ohne Gläser zu schleppen.",
          description=[
              "Bis jetzt musstest du Quelllinks, Gläser und Maschinen eng zusammenbauen. Das &6Quellrelais&r (Source Relay) ändert das. Du craftest es aus &e6 Goldbarren&r um einen &6Quelljuwelblock&r.",
              "",
              "Verbunden wird mit dem &6Dominion-Zauberstab&r: erst das Glas anklicken, aus dem das Relais saugen soll, dann das Relais. Danach das Relais anklicken und dann das Ziel, ein weiteres Relais oder ein Glas bei deinen Maschinen. Ein Relais reicht bis zu &e30 Blöcke&r weit.",
              "",
              "Schleichend mit dem Zauberstab auf ein Relais geklickt löscht seine Verbindungen. Ein Redstone-Signal schaltet es ab.",
              "",
              "&eTipp:&r Stell die Quelllinks zur Baumfarm und die Gläser an deinen Arbeitsplatz. Zwei Relais dazwischen, fertig.",
          ],
          tasks=[task_item("ars_nouveau:relay", 2)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          deps=["welcome"], icon="ars_nouveau:relay", size=1.5, shape="square"),

    quest("splitter", 2.7, 5.3, "&aQuellrelais: Splitter",
          subtitle="Eine Quelle, viele Ziele.",
          description=[
              "Das Relais im Apparat mit &e4 Quarz&r und &e4 Lapislazuli&r wird zum &6Splitter&r. Er kann aus mehreren Gläsern gleichzeitig ziehen und an mehrere Ziele liefern und teilt seinen Durchsatz gleichmäßig auf. Dazu schafft er deutlich mehr Quelle pro Sekunde als ein normales Relais.",
              "",
              "Ideal, wenn die Imbuement-Kammern, der Apparat und das Ritual-Kohlenbecken alle aus demselben Lager versorgt werden sollen.",
          ],
          tasks=[task_item("ars_nouveau:relay_splitter", 1)],
          rewards=[reward_item("minecraft:quartz", 16)],
          deps=["relay"], icon="ars_nouveau:relay_splitter"),

    quest("collector", 2.7, 7.1, "&aQuellrelais: Kollektor",
          subtitle="Sammelt ein, ohne dass du verbindest.",
          description=[
              "Mit &e4 Truhen&r auf den Podesten wird aus einem Relais der &6Kollektor&r. Er zieht Quelle automatisch aus allen Gläsern im Umkreis von &e5 Blöcken&r, auch aus solchen, die du nicht verbunden hast.",
              "",
              "Das Gegenstück ist der &6Einzahler&r (Depositor) aus &e4 Trichtern&r: er füllt alle Gläser in seiner Nähe von selbst. Kollektor an der Quelllink-Farm, Einzahler in der Werkstatt, ein Relais-Paar dazwischen, und du musst nie wieder ein Glas einzeln verbinden.",
          ],
          tasks=[task_item("ars_nouveau:relay_collector", 1), task_item("ars_nouveau:relay_deposit", 1)],
          rewards=[reward_item("minecraft:hopper", 2)],
          deps=["relay"], icon="ars_nouveau:relay_collector", optional=True),

    # ---- Rituale ---------------------------------------------------------------
    quest("brazier", 7.5, 7.0, "&aRitual-Kohlenbecken",
          subtitle="Wo die großen Zauber brennen.",
          description=[
              "Das &6Ritual-Kohlenbecken&r (Ritual Brazier) craftest du formlos aus einem &6Arkanen Podest&r, einem &6Quelljuwelblock&r und &e3 Goldbarren&r.",
              "",
              "Jedes Ritual steckt in einer eigenen &6Ritualtafel&r, die du formlos aus einem &6Archwood-Stamm&r und ein paar Zutaten craftest. Die Farbe des Stamms zeigt, zu welcher Familie das Ritual gehört. So startest du es:",
              "",
              "&e1.&r Rechtsklick mit der Tafel auf das Kohlenbecken legt das Ritual ein.",
              "&e2.&r Zusatzzutaten (etwa ein Block für das Hellsehen) wirfst du vorher auf das Becken.",
              "&e3.&r Rechtsklick mit leerer Hand startet das Ritual.",
              "",
              "Viele Rituale ziehen während der Arbeit Quelle aus Gläsern in der Nähe. Ein Redstone-Signal hält ein laufendes Ritual an. Mit einem Lichtzauber auf das Becken leuchtet es auch einfach als Deko in deiner Zauberfarbe.",
          ],
          tasks=[task_item("ars_nouveau:ritual_brazier", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_table("s2_common")],
          deps=["welcome"], icon="ars_nouveau:ritual_brazier", size=1.75, shape="square"),

    quest("ritual_harvest", 9.7, 5.2, "&aRitual: Ernte",
          subtitle="Die Felder ernten sich selbst.",
          description=[
              "Die Tafel: &aBlühender Archwood-Stamm&r, &6Erdessenz&r und eine &6Eisenhacke&r. Das Ritual wirkt die Ernte-Glyphe immer wieder auf die reifen Pflanzen rund um das Becken und kostet jedes Mal ein wenig Quelle.",
              "",
              "Steht eine Truhe direkt neben dem Kohlenbecken, landet die Ernte darin statt auf dem Boden. Zusammen mit einem Agronomischen Quellenlink im selben Feld bezahlt sich das Ritual fast von allein.",
          ],
          tasks=[task_item("ars_nouveau:ritual_harvest", 1)],
          rewards=[reward_item("minecraft:bone_meal", 32), reward_xp(5)],
          deps=["brazier"], icon="ars_nouveau:ritual_harvest"),

    quest("ritual_scrying", 9.7, 7.0, "&aRitual: Wahrsagerei",
          subtitle="Einen Block durch alle anderen sehen.",
          description=[
              "Die Tafel: &5Ärgerlicher Archwood-Stamm&r, &e3 Spinnenaugen&r, &6Glowstone&r und ein &6Quelljuwelblock&r.",
              "",
              "Wirf vor dem Start einen Block deiner Wahl auf das Becken, zum Beispiel ein Zinkerz. Danach siehst du eine Zeit lang jeden Block dieser Sorte durch die Erde: weiße Partikel sind ganz nah, grüne mittel, blaue weit weg. Eine zusätzliche &6Manipulationsessenz&r verlängert die Sicht auf 15 Minuten.",
              "",
              "&eTipp:&r Perfekt für &6Zink&r und &6Osmium&r, die ihr für Messing und Mekanism braucht.",
          ],
          tasks=[task_item("ars_nouveau:ritual_scrying", 1)],
          rewards=[reward_item("minecraft:spider_eye", 6), reward_xp(5)],
          deps=["brazier"], icon="ars_nouveau:ritual_scrying"),

    quest("ritual_fertility", 9.7, 8.8, "&aRitual: Fruchtbarkeit",
          subtitle="Die Tiere vermehren sich von selbst.",
          description=[
              "Die Tafel: &aBlühender Stamm&r, &e3 Weizen&r, ein &6Goldener Apfel&r und &e2 Lohenstaub&r. Das Ritual lässt Tiere in der Nähe regelmäßig Nachwuchs bekommen, solange es Quelle hat.",
              "",
              "Bei zwanzig oder mehr Tieren in der Nähe pausiert es. Zusammen mit einem &6Vitalic Sourcelink&r entsteht dabei sogar etwas Quelle zurück.",
          ],
          tasks=[task_item("ars_nouveau:ritual_fertility", 1)],
          rewards=[reward_item("minecraft:wheat", 32)],
          deps=["ritual_scrying"], icon="ars_nouveau:ritual_fertility", optional=True),

    quest("ritual_sanctuary", 11.7, 5.2, "&aRitual: Zufluchtsort",
          subtitle="Keine Monster mehr zu Hause.",
          description=[
              "Die Tafel: &bKaskadierender Archwood-Stamm&r, &bWasseressenz&r und eine &6Seelaterne&r. Solange das Ritual läuft, spawnen im Umkreis von &e32 Blöcken&r keine feindlichen Monster auf natürliche Weise.",
              "",
              "Jedes &6Verrottete Fleisch&r, das du vor dem Start dazugibst, vergrößert den Radius um einen Block, bis höchstens 128. Quelle kostet es nur, wenn es tatsächlich einen Spawn verhindert, und dann höchstens einmal pro Minute.",
          ],
          tasks=[task_item("ars_nouveau:ritual_sanctuary", 1)],
          rewards=[reward_item("minecraft:rotten_flesh", 32), reward_xp(5)],
          deps=["ritual_harvest"], icon="ars_nouveau:ritual_sanctuary"),

    quest("ritual_restoration", 11.7, 7.0, "&aRitual: Wiederherstellung",
          subtitle="Heilung für alle in der Nähe.",
          description=[
              "Die Tafel: &aBlühender Stamm&r, ein &6Goldener Apfel&r und &5Abschwörungsessenz&r. Das Ritual heilt Wesen in der Nähe nach und nach und schadet Untoten.",
              "",
              "Der eigentliche Schatz: &6Zombiedorfbewohner&r werden sofort geheilt, und wenn du dabei warst, gibt dir der geheilte Dorfbewohner Rabatt. Ein gutes Ritual für den Bau eines Handelszentrums.",
          ],
          tasks=[task_item("ars_nouveau:ritual_restoration", 1)],
          rewards=[reward_item("minecraft:golden_apple", 1)],
          deps=["ritual_scrying"], icon="ars_nouveau:ritual_restoration", optional=True),

    quest("ritual_forestation", 11.7, 8.8, "&aRitual: Aufforstung",
          subtitle="Ein Wald in Minuten.",
          description=[
              "Die Tafel: &aBlühender Stamm&r, eine &6Mendosteen&r und &6Erdessenz&r. Das Ritual setzt ausgewachsene Eichen und Birken in einem runden Bereich von 7x7 und düngt den Boden.",
              "",
              "Jedes Quelljuwel als Zusatz vergrößert den Radius um eins. Ein Braunpilz macht daraus Taiga mit Podsol, Leuchtbeeren einen Dschungel. Für Holzfarmen im großen Stil kaum zu schlagen.",
              "",
              "&eTipp:&r Mendosteen wächst wie die anderen Archwood-Früchte an Archwood-Bäumen.",
          ],
          tasks=[task_item("ars_nouveau:ritual_forestation", 1)],
          rewards=[reward_item("minecraft:oak_sapling", 16)],
          deps=["ritual_restoration"], icon="ars_nouveau:ritual_forestation", optional=True),

    quest("ritual_binding", 13.7, 5.2, "&aRitual: Bindung",
          subtitle="Ein Vertrauter an deiner Seite.",
          description=[
              "Die Tafel: &5Ärgerlicher Stamm&r, &6Leeres Pergament&r, &6Ender-Perle&r und &e3 Quelljuwelen&r.",
              "",
              "Führ das Ritual neben einem zahmen oder wilden &dSternbunkel&r, &dDrygmy&r, &dWirbelzweig&r oder &dWixie&r durch. Das Wesen wird zu einem &6Gebundenen Skript&r. Rechtsklick mit dem Skript, und das Wesen ist dein &dVertrauter&r.",
              "",
              "Rufen kannst du Vertraute im Zauberbuch (C) auf der Seite für Vertraute. Immer nur einer begleitet dich, und jeder hat einen eigenen Bonus. Der Sternbunkel gibt dir zum Beispiel &eTempo II&r.",
          ],
          tasks=[task_item("ars_nouveau:ritual_binding", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2), reward_xp(5)],
          deps=["ritual_sanctuary"], icon="ars_nouveau:ritual_binding"),

    quest("familiar", 15.7, 5.2, "&dSternbunkel-Vertrauter",
          subtitle="Schneller unterwegs mit einem kleinen Freund.",
          description=[
              "Binde einen Sternbunkel mit dem Ritual der Bindung. Als Vertrauter gibt er dir &eTempo II&r, und ein Goldnugget an ihn verfüttert zeigt dir für kurze Zeit Golderz durch die Wände.",
              "",
              "Die anderen Vertrauten lohnen sich auch: Der &dWirbelzweig&r halbiert die Kosten von Erd-Glyphen und macht Essen sättigender. Der &dDrygmy&r stärkt Erd-Schaden und bringt mehr Beute. Der &dWixie&r verlängert Tränke, die du nimmst.",
          ],
          tasks=[task_item("ars_nouveau:familiar_starbuncle", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(5)],
          deps=["ritual_binding"], icon="ars_nouveau:familiar_starbuncle"),

    quest("ritual_containment", 13.7, 7.0, "&aRitual: Eindämmung",
          subtitle="Ein Wesen im Glas.",
          description=[
              "Die Tafel: &5Ärgerlicher Stamm&r, &6Manipulationsessenz&r und &e3 Glasflaschen&r. Das Ritual fängt ein Wesen in der Nähe ein und steckt es in ein &6Eindämmungsglas&r (Containment Jar, aus Archwood-Stufen und Glas), das neben dem Becken steht. Wesen und Glas müssen höchstens drei Blöcke entfernt sein.",
              "",
              "Ein Wesen im Glas zählt für den Drygmy als Nachbar. Mit &bArs Ocultas&r arbeiten sogar Geister aus Occultism im Glas weiter.",
          ],
          tasks=[task_item("ars_nouveau:ritual_containment", 1), task_item("ars_nouveau:mob_jar", 1)],
          rewards=[reward_item("minecraft:glass", 16)],
          deps=["ritual_binding"], icon="ars_nouveau:mob_jar", optional=True),

    quest("ritual_cloudshaping", 13.7, 8.8, "&aRitual: Wolkenformung",
          subtitle="Wetter nach Wunsch.",
          description=[
              "Die Tafel: &bKaskadierender Stamm&r, &6Feder&r und ein &6Quelljuwelblock&r. Ohne Zusatz macht das Ritual klares Wetter, mit &6Schwarzpulver&r Regen, mit einem &6Lapisblock&r Gewitter.",
              "",
              "Die Zeit dreht &aSonnenaufgang&r (Flammender Stamm, 3 Löwenzahn, Uhr) auf Tag und &aMondfall&r (Kaskadierender Stamm, Tintenbeutel, Kohleblock, Uhr) auf Nacht. Auf einem Server mit vielen Spielern sprecht euch vorher ab, das gilt für alle.",
          ],
          tasks=[task_item("ars_nouveau:ritual_cloudshaping", 1)],
          rewards=[reward_item("minecraft:feather", 8)],
          deps=["ritual_containment"], icon="ars_nouveau:ritual_cloudshaping", optional=True),

    quest("ritual_squirrels", 15.7, 7.0, "&aRitual: Fast Squirrels",
          subtitle="Ars Elemental: Sternbunkel auf Espresso.",
          description=[
              "&bArs Elemental&r bringt eigene Rituale, die meisten brauchen &eBlitzendes Archwood&r (Flashing Archwood). Den gelben Setzling craftest du aus einem beliebigen Archwood-Setzling und einer &fLuftessenz&r.",
              "",
              "Die Tafel &6Fast Squirrels&r (Blitzender Stamm, Sternbunkel-Scherben, Zucker, Hasenpfote) gibt allen Sternbunkeln in 15 Blöcken einen langen Tempo-Schub. Deine Lieferdienste laufen dann doppelt so schnell. Ein Goldblock als Zusatz verdoppelt den Radius.",
              "",
              "Weitere Rituale von Ars Elemental: &aAttraction&r zieht Wesen an, &aRepulsion&r stößt sie ab, &aDetection&r lässt Monster im weiten Umkreis leuchten.",
          ],
          tasks=[task_item("ars_elemental:ritual_squirrels", 1)],
          rewards=[reward_item("minecraft:sugar", 16)],
          deps=["familiar"], icon="ars_elemental:ritual_squirrels", optional=True),

    quest("ritual_locate", 15.7, 8.8, "&aRitual: Locate Structure",
          subtitle="Ars Additions: der Weg zum nächsten Bauwerk.",
          description=[
              "Mit &bArs Additions&r findet das Kohlenbecken Bauwerke für dich. Crafte zuerst einen &6Wayfinder&r (Amethystsplitter in der Mitte, vier Goldbarren darum), dann die Tafel aus &5Ärgerlichem Stamm&r, &6Kompass&r, &6Quelljuwel&r und dem Wayfinder.",
              "",
              "Welches Bauwerk gesucht wird, bestimmst du über Zusätze, JEI zeigt die Liste: Dorf, Außenposten, Festung, Bastion und viele mehr. Danach zeigt dir der Wayfinder die Richtung.",
          ],
          tasks=[task_item("ars_additions:ritual_locate_structure", 1)],
          rewards=[reward_item("minecraft:compass", 1), reward_xp(3)],
          deps=["ritual_cloudshaping"], icon="ars_additions:ritual_locate_structure", optional=True),

    # ---- Automatisierung -------------------------------------------------------
    quest("turret", 0.5, 13, "&aEinfacher Zauberturm",
          subtitle="Ein Zauber auf Knopfdruck.",
          description=[
              "Der &6Einfache Zauberturm&r (Basic Spell Turret) besteht aus &e4 Quelljuwelen&r, &e4 Goldbarren&r und einem &6Redstone-Block&r. Er funktioniert wie ein Werfer: bei jedem Redstone-Impuls wirkt er einen Zauber aus seiner Vorderseite.",
              "",
              "Den Zauber gibst du ihm mit einem beschriebenen &6Zauberpergament&r. Er nimmt Zauber mit &dBerühren&r und &dProjektil&r und bezahlt sie mit Quelle aus Gläsern in der Nähe.",
              "",
              "Steht eine Truhe daneben, kann er auch &dArtikelabholung&r und &dBlock platzieren&r benutzen. Beispiele: ein Turm mit &eBerühren, Brechen&r vor einem Bruchsteingenerator, einer mit &eBerühren, Ernte, AOE&r über einem Feld, beide an einer Redstone-Uhr.",
          ],
          tasks=[task_item("ars_nouveau:basic_spell_turret", 1)],
          rewards=[reward_item("minecraft:redstone", 32), reward_table("s2_uncommon")],
          deps=["welcome"], icon="ars_nouveau:basic_spell_turret", size=1.5, shape="square"),

    quest("spell_turret", 2.7, 13, "&aVerzauberter Zauberturm",
          subtitle="Halbe Kosten, gleiche Wirkung.",
          description=[
              "Leg einen Einfachen Zauberturm in den Apparat, dazu einen &6Quelljuwelblock&r und &e2 Lohenruten&r auf die Podeste. Der &6Verzauberte Zauberturm&r wirkt Zauber zum halben Quellpreis.",
              "",
              "Für alles, was oft feuert, lohnt sich der Umbau schnell. Mit dem Dominion-Zauberstab drehst du einen Turm: erst den Turm, dann den Zielblock anklicken. Die Varianten mit Timer und frei einstellbarer Richtung kommen mit Stufe 3.",
          ],
          tasks=[task_item("ars_nouveau:spell_turret", 1)],
          rewards=[reward_item("minecraft:blaze_rod", 2), reward_xp(5)],
          deps=["turret"], icon="ars_nouveau:spell_turret"),

    quest("warp_scroll", 4.7, 12.1, "&6Warp-Schriftrolle",
          subtitle="Einmal nach Hause, bitte.",
          description=[
              "Die &6Warp-Schriftrolle&r craftest du formlos aus &e4 Lapislazuli&r, &e4 Quelljuwelen&r und einem &6Leeren Pergament&r. Benutz sie schleichend an einem Ort, um ihn zu speichern. Später bringt dich ein normaler Rechtsklick dorthin zurück, und die Rolle ist verbraucht.",
              "",
              "Die &6Stabilisierte Warp-Schriftrolle&r aus dem Apparat (Warp-Schriftrolle, 4 Lohenstaub, 2 Ender-Perlen) kannst du immer wieder benutzen. Ein Muss für jeden, der viel im Nether unterwegs ist.",
          ],
          tasks=[task_item("ars_nouveau:warp_scroll", 2)],
          rewards=[reward_item("minecraft:lapis_lazuli", 16)],
          deps=["turret"], icon="ars_nouveau:warp_scroll"),

    quest("stable_warp", 6.7, 12.1, "&6Stabilisierte Warp-Schriftrolle",
          subtitle="Heimweg ohne Verbrauch.",
          description=[
              "Die stabile Rolle hat denselben Zweck wie die einfache, verschwindet aber nicht nach der Benutzung. Speicher darin deine Basis, und du bist von jedem Ort der Welt in einem Augenblick zu Hause.",
              "",
              "&eTipp:&r Eine gespeicherte Warp-Schriftrolle lässt sich im Apparat für 1 000 Quelle kopieren. Gib deinen Freunden eine Kopie mit dem Ort eurer Gemeinschaftsbasis.",
          ],
          tasks=[task_item("ars_nouveau:stable_warp_scroll", 1)],
          rewards=[reward_item("minecraft:ender_pearl", 2)],
          deps=["warp_scroll"], icon="ars_nouveau:stable_warp_scroll", optional=True),

    quest("wixie", 4.7, 13.9, "&dWixie-Charme",
          subtitle="Eine Hexe, die für dich craftet.",
          description=[
              "Triff eine &6Hexe&r, die nur noch halbe Gesundheit hat, mit einem Zauber mit &dZerstreuen&r. Sie verschwindet und lässt &6Wixie-Scherben&r zurück. Im Apparat mit Setzling, Smaragd, Werkbank und &6Braustand&r werden sie zum &6Wixie-Charme&r.",
              "",
              "Benutz den Charme auf einem &6Kessel&r: es entsteht ein &6Wixie-Kessel&r. Klick mit dem gewünschten Item auf den Kessel, und der Wixie craftet es, sobald die Zutaten in Truhen in der Nähe liegen. Jeder Craft kostet etwas Quelle.",
              "",
              "Mit &6Trankgläsern&r (Quellglas und Abschwörungsessenz) braut der Wixie auch Tränke vollautomatisch. Die fertigen Tränke speisen einen &6Alchemistischen Quelllink&r, der Quelle aus ihnen macht.",
          ],
          tasks=[task_item("ars_nouveau:wixie_charm", 1)],
          rewards=[reward_item("minecraft:brewing_stand", 1), reward_xp(5)],
          deps=["warp_scroll"], icon="ars_nouveau:wixie_charm"),

    # ---- Technik trifft Magie --------------------------------------------------
    quest("blaze_burner", 10.5, 13, "&6Leerer Lohenbrenner",
          subtitle="Kronwerke: Messing braucht einen Magier.",
          description=[
              "Auf Kronwerke ist der &6Leere Lohenbrenner&r von Create anders: oben links und rechts sitzen &e2 Quelljuwelen&r, dazu &e4 Eisenbleche&r und ein &6Netherrack&r in der Mitte.",
              "",
              "Ohne Lohenbrenner keine Messingmischung, und ohne Messing kein Ziel von Stufe 2. Die Techniker auf dem Server brauchen also deine Juwelen. Bau selbst ein paar Brenner oder verkauf Juwelen gegen Messing, Zahnräder oder was du gerade brauchst.",
              "",
              "&eTipp:&r Eine Truhe voller Quelljuwelen an einem Treffpunkt macht dich bei allen Ingenieuren sehr beliebt.",
          ],
          tasks=[task_item("create:empty_blaze_burner", 1)],
          rewards=[reward_item("ars_nouveau:source_gem", 8), reward_xp(5)],
          deps=["welcome"], icon="create:empty_blaze_burner", size=1.25),

    quest("calibrated_mechanism", 12.5, 13, "&6Calibrated Precision Mechanism",
          subtitle="Ars Technica: Präzision trifft Magie.",
          description=[
              "&bArs Technica&r ist die Brücke zwischen Ars und Create. Sein Grundbauteil ist der &6Calibrated Precision Mechanism&r: ein &6Präzisionsmechanismus&r von Create in den Apparat, &e4 Amethystsplitter&r und &e4 Quelljuwelen&r auf die Podeste, dazu &d500 Quelle&r.",
              "",
              "Du brauchst ihn für den Source Motor, den Arcane Wrench (ein Create-Schraubenschlüssel mit Magie) und das Spy Monocle. Präzisionsmechanismen sind auch ein Teil des Stufenziels, also sprich dich mit den Create-Bauern ab.",
          ],
          tasks=[task_item("ars_technica:calibrated_precision_mechanism", 1)],
          rewards=[reward_item("minecraft:amethyst_shard", 16), reward_xp(5)],
          deps=["blaze_burner"], icon="ars_technica:calibrated_precision_mechanism"),

    quest("source_motor", 14.7, 13, "&6Source Motor",
          subtitle="Ars Technica: Quelle wird Drehung.",
          description=[
              "Der &6Source Motor&r macht aus Quelle &dRotationskraft&r für Create. Das Rezept: &e4 Messingbarren&r, &e3 Zahnräder&r, eine &6Elektronenröhre&r und der Calibrated Precision Mechanism in der Mitte.",
              "",
              "Stell ein Quellglas daneben. An den Seiten des Motors stellst du die Drehzahl ein, mit Rechtsklick auf die Front das Verhältnis von Stress-Einheiten zu Drehzahl. Mehr Kraft kostet mehr Quelle.",
              "",
              "&eTipp:&r Ein Quelllink-Garten mit Relais zum Motor ist ein Kraftwerk ohne Wasser, Wind oder Kohle.",
          ],
          tasks=[task_item("ars_technica:source_motor", 1)],
          rewards=[reward_table("s2_uncommon"), reward_xp(10)],
          deps=["calibrated_mechanism", "relay"], icon="ars_technica:source_motor", size=1.5, shape="gear"),

    quest("glyph_press", 12.5, 14.9, "&dPress",
          subtitle="Ars Technica: die Presse als Glyphe.",
          description=[
              "Die Glyphe &dPress&r ist Stufe 2 und kostet eine &6Manipulationsessenz&r und eine &6Mechanische Presse&r von Create. Sie presst Items am Zielort wie eine Presse, also Barren zu Blechen.",
              "",
              "Mit &dAOE&r presst sie mehr Items auf einmal. Mit &dExtrakt&r nimmt sie Kompaktier-Rezepte statt Pressen-Rezepte, &dSchmelzen&r dazu ergibt die beheizten Varianten. Ihre Schwester &dPolish&r schleift Items wie Sandpapier.",
          ],
          tasks=[task_item("ars_technica:glyph_press", 1)],
          rewards=[reward_item("minecraft:iron_ingot", 16), reward_xp(3)],
          deps=["calibrated_mechanism"], icon="ars_technica:glyph_press", optional=True),

    # ---- Stufenziel ------------------------------------------------------------
    quest("mage", 18.8, 9.8, "&dMeister der Quelle",
          subtitle="Quelle für die ganze Stadt.",
          description=[
              "Du bewegst Quelle über Relais, lässt Rituale deine Felder ernten und deine Basis schützen, deine Türme arbeiten auf Knopfdruck und dein Motor treibt Create an.",
              "",
              "Leg einen Vorrat an &6Quelljuwelblöcken&r an. Mit &6Stufe 3&r kommen die Glyphen der dritten Stufe, das &6Erzmagier-Zauberbuch&r, die Rituale für Flug und Verwandlung und die Magierroben, und die wollen alle Juwelen und Quelle in Mengen.",
          ],
          tasks=[task_item("ars_nouveau:source_gem_block", 16)],
          rewards=[reward_table("s2_rare"), reward_xp(15)],
          deps=["spells2", "familiar", "spell_turret", "source_motor"], icon="ars_nouveau:source_gem_block",
          size=2.5, shape="gear"),
]

images = [
    banner("ars_apprentice/title", "Ars Nouveau: Magier", 8.5, -5.8, height=1.8, kind="title", colour="magic"),
    banner("ars_apprentice/glyphen", "Glyphen der Stufe 2", 7.7, -3.6, height=0.9, colour="magic"),
    banner("ars_apprentice/quelle", "Quelle bewegen", 2.2, 3.6, height=0.9, colour="magic"),
    banner("ars_apprentice/rituale", "Rituale", 12.2, 3.6, height=0.9, colour="magic"),
    banner("ars_apprentice/automatisierung", "Automatisierung", 3.6, 10.6, height=0.9, colour="magic"),
    banner("ars_apprentice/technik", "Technik trifft Magie", 12.6, 10.9, height=0.9, colour="brass"),
    banner("ars_apprentice/ziel", "Stufenziel", 18.8, 7.4, height=0.9, colour="magic"),
]

chapter(C, "Ars Nouveau: Magier", "ars_nouveau:apprentice_spell_book", "magic", quests, shape="circle", order=12,
        stage=2, subtitle=["Stufe 2. Das zweite Buch, Relais, Rituale, Türme und Create."], images=images)
