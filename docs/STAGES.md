# Stages

How progression in Season 2 is gated, what each stage contains, and the numbers behind the community goals. This is the design; the Chapters configs, the quest book and the goals file in Kronwerke Core are built from it.

## What we learned from other packs

- **SevTech: Ages** gates everything behind six ages and each age is unlocked by one item (a melter, a coal engine, plastic, a rocket). It works because every age has a clear theme and a clear exit. It fails for groups: one player crafts the exit item and the whole age is over for everyone, and the early ages are slow enough that people quit before the pack gets good.
- **Enigmatica 6 Expert** interweaves tech and magic through recipes: you cannot build the good machines without the magic mods and vice versa. That is the right idea for us, but E6E takes months. We have seven weeks.
- **GregTech: New Horizons** has the clearest tier ladder there is (stone, steam, LV, MV, HV...). Each tier roughly doubles what the previous one can do. Too long for us, but the "each tier doubles" rule is worth copying.
- **Create: Above and Beyond** shows that Create alone can carry the first two chapters of a pack if the goals are factory shaped ("make 64 precision mechanisms"), not item hunts.
- **All the Mods** does not gate at all, which is why experienced players reach the ATM star while newcomers are still on stone tools. Its quest book is the model for ours: one chapter per mod, a line per quest, crates as rewards.

Our answer: five stages, each with a theme, each opened by a community goal that needs tech and magic in equal parts, each with a quest book that leads through everything available in it.

## Rules

1. **A stage opens for everyone at once.** No individual unlocks. The gate is a community goal at the spawn obelisk.
2. **Every goal has two pillars, tech and magic. Both must fill.** A server that only builds machines does not progress.
3. **The last step is an event.** The obelisk stops accepting at 98 percent. The team sets a date, every streamer goes live, the last items go in on stream, the stage opens.
4. **Goals scale with the player count.** The base numbers below assume 30 active players. At stage open, the amount is set to `base * clamp(active / 30, 0.4, 1.5)`, where `active` is the number of players with more than one hour on the server in the last seven days. Then it is fixed for that stage.
5. **Each stage roughly doubles what the previous one could do.** Ore yield, energy, mana, storage, mobility.
6. **Nothing is removed, only delayed.** Every mod in the pack is reachable by the end. Cosmetic and building mods are never gated.
7. **Late joiners catch up.** When a stage opens, the quest book grants a starter kit for it. A player who joins in week four gets the kits of the stages that are already open.
8. **Vanilla is not gated,** with two exceptions: the Nether (stage 2) and the End (stage 4). Both are events.

## Timeline

Season length six to eight weeks, launch mid January 2027. Player hours per day at 30 players and 1.5 hours each: about 45.

| Stage | Name | Opens | Planned length | Player hours |
| --- | --- | --- | --- | --- |
| 1 | Steinwerk | Day 1 | 5 days | 225 |
| 2 | Messingwerk | Day 6 | 9 days | 405 |
| 3 | Stahlwerk | Day 15 | 12 days | 540 |
| 4 | Sternwerk | Day 27 | 12 days | 540 |
| 5 | Chaoswerk | Day 39 | 14 days, then the final | 630 |

Stage lengths are targets. The goal amounts are set so a server that plays normally lands within two days of them; the event date is set once the bar passes 90 percent.

## Stage 1: Steinwerk

Theme: wood, stone, water wheels, the first spells. Everyone starts here on day one.

**Open:** vanilla overworld; Create up to andesite (water wheel, millstone, press, mixer without blaze burner, belts, fans, andesite funnels and casings); Ars Nouveau novice glyphs, source jars, sourcelinks, the imbuement chamber (the only way to Source Gems, which the stage 1 goal asks for), the enchanting apparatus, Starbuncles; Botania up to the mana pool and mana spreader (no runic altar); Farmer's Delight, Farming for Blockheads, Aquaculture; Silent Gear iron tier; Sophisticated Backpacks (leather); Functional Storage (oak drawers); Waystones; Neo Origins; Apotheosis affixes up to rare; the Mining Dimension (an iron block portal lit with the Enchanted Pickaxe; the mod's own recipe never loads on 1.21.1 and needs netherite, so KubeJS adds one without it); Cataclysm and Born in Chaos overworld structures.

**Locked:** the Nether; Create brass and everything needing it; Mekanism entirely; AE2; Refined Storage; Ender IO; Industrial Foregoing; Immersive Engineering; Powah; Oritech; Ars apprentice glyphs and above; Botania runic altar and above; Occultism rituals; Theurgy; Hexerei; Eidolon; Malum; Mahou Tsukai; Iron's Spells above common; Undergarden, Eternal Starlight; Draconic Evolution; NuclearCraft.

**Goal:** Foundation of the Kronwerk.

| Pillar | Item | Base amount | Why this number |
| --- | --- | --- | --- |
| Stone | Cobblestone (any) | 40 000 | About 30 player hours of digging by hand, less with Ultimine. Everyone can contribute from minute one. |
| Tech | Andesite Alloy | 3 000 | Needs an andesite supply and a nugget supply. A player with a cobble fan line makes 200 an hour. |
| Magic | Source Gem | 1 500 | Needs source jars and the first spells to farm. Drop rate from the Ars starter progression, about 40 an hour with a small farm. |

**Quests:** Start Here (10), Create (12), Ars Nouveau (17), Botania (13), Food and Farming (10), Storage (11), Silent Gear (10), Exploration (9). 92 in total. An Origins chapter follows with the Kronwerke origins.

**Starter kit at open:** none, this is the start.

## Stage 2: Messingwerk

Theme: brass, the Nether, mana, the first machines that do work while you sleep.

**Opens with the event:** the Nether portal at spawn is lit on stream.

**Newly open:** the Nether; Create brass tier (blaze burner, brass funnels, tunnels, mechanical crafters, deployers, sequenced gearshift, trains, contraptions); Create addons (Enchantment Industry, Connected, New Age basic); Mekanism basic (metallurgic infuser, energized smelter, enrichment chamber, crusher, heat generator, basic universal cables, steel; no digital miner, no elite tier); Immersive Engineering up to the coke oven, blast furnace and windmill; Ars apprentice glyphs, source relays, the ritual brazier; Botania runic altar, elven trade (Alfheim portal), terra plate; Occultism first rituals (Foliot, Djinni); Hexerei; Silent Gear steel; Sophisticated Backpacks iron and copper; Functional Storage compacting drawers; Iron's Spells uncommon and rare.

**Still locked:** AE2; Ender IO; Industrial Foregoing; Powah; Oritech; Mekanism advanced and elite; Theurgy; Eidolon; Malum; Mahou Tsukai; Undergarden and Eternal Starlight; the End; Draconic Evolution; NuclearCraft.

**Goal:** The Brass Engine.

| Pillar | Item | Base amount | Why |
| --- | --- | --- | --- |
| Tech | Brass Ingot | 4 000 | Needs a blaze burner line and a zinc supply. A good mixer setup makes 300 an hour. |
| Tech | Precision Mechanism | 300 | The first real Create automation. Forces someone to build the sequenced gearshift line. |
| Magic | Mana Pearl | 1 500 | Needs a mana farm that runs on its own. Each pearl takes 6 000 mana in the pool, so 1 500 pearls are 9 million. |
| Magic | Terrasteel Ingot | 100 | Needs the terra plate and half a full mana pool each. Botania's stage 2 exit. |

**Quests:** Create brass (14), Create trains and contraptions (10), Mekanism basics (12), Immersive Engineering (10), Ars apprentice (10), Botania runic and elven (12), Occultism (10), Hexerei (8), The Nether (6). About 90.

Written: The Nether (6), Create: Brass (14), Create: Trains (9), Mekanism (12), Immersive Engineering (10), Botania: Runes (12), Ars Nouveau: Mage (9), Occultism (8), Hexerei (8). 88 in total. Each chapter starts with a quest that needs a stage 2 item, so the rest stays locked until the stage opens.

**Starter kit:** 16 brass ingots, 1 blaze burner, 1 source jar, 8 mana pearls.

## Stage 3: Stahlwerk

Theme: steel, ore multiplication, storage networks, rituals with consequences.

**Newly open:** Mekanism advanced and elite tier (advanced control circuit, factories, ore tripling, digital miner, teleporter; no fusion, no antimatter); AE2 (no quantum bridge, no spatial); Refined Storage and Cable Tiers; the Immersive Engineering machines built from engineering blocks (crusher, metal press, arc furnace, excavator, diesel generator); Ender IO; Industrial Foregoing; Powah up to nitro; Oritech; Refined tiers of Sophisticated (gold, diamond); Ars master glyphs; Botania gaia-side content except the fight (elementium, pixie, spectrolus); Occultism Afrit and Marid; Theurgy (its ore multiplication matches Mekanism tripling on purpose); Eidolon; Malum; Undergarden; Apotheosis epic; Iron's Spells epic.

**Still locked:** the End; Mekanism fusion, antimatter and the ultimate tier machines; AE2 quantum and spatial; Mahou Tsukai; Eternal Starlight; Gaia Guardian; Draconic Evolution; NuclearCraft.

**Goal:** The Furnace Never Sleeps.

| Pillar | Item | Base amount | Why |
| --- | --- | --- | --- |
| Tech | Steel Ingot | 8 000 | Mekanism or IE. Needs an automated coal and iron line. |
| Tech | Advanced Control Circuit | 500 | Forces Mekanism into the infusing tier. |
| Magic | Elementium Ingot | 500 | Botania's elven side, needs the Alfheim trade automated. |
| Magic | Occultism Spirit Attuned Gem | 300 | Needs rituals run at scale. |

**Quests:** Mekanism (18), AE2 (14), Ender IO (10), Industrial Foregoing (10), Powah (8), Oritech (10), Ars master (8), Botania elven (10), Occultism rituals (10), Theurgy (12), Eidolon (8), Malum (10), Undergarden (6). About 130.

**Starter kit:** 32 steel, 1 basic universal cable stack, 1 AE2 charged certus block, 4 elementium.

## Stage 4: Sternwerk

Theme: the End, the stars, the machines that eat power.

**Opens with the event:** the End portal is activated on stream. The dragon fight is the first shared boss.

**Newly open:** the End; Eternal Starlight; Mekanism ultimate tier and fusion; AE2 quantum and spatial; NuclearCraft fission; Draconic Evolution basic (draconium, energy core up to tier 4, wyvern gear); Botania Gaia Guardian; Mahou Tsukai; Ars epic; Apotheosis mythic; Iron's Spells legendary.

**Still locked:** Draconic awakened and chaos tier; NuclearCraft fusion; Mekanism antimatter.

**Goal:** Light of the Dragon.

| Pillar | Item | Base amount | Why |
| --- | --- | --- | --- |
| Tech | Elite Control Circuit | 300 | Mekanism's top circuit before ultimate. |
| Tech | Draconium Ingot | 2 000 | The End is where draconium is. Forces the End to be used, not just opened. |
| Magic | Gaia Spirit | 128 | Every Gaia fight gives 8. Sixteen fights, on stream. |
| Magic | Mahou Tsukai Mystic Staff | 30 | Each needs a mana investment from a player. Thirty players, thirty staves. |

**Quests:** The End (6), Eternal Starlight (8), Mekanism fusion (8), AE2 advanced (8), NuclearCraft fission (10), Draconic basics (10), Gaia (4), Mahou Tsukai (10), Ars epic (6). About 70.

**Starter kit:** 16 draconium ingots, 1 gaia spirit, 4 ender pearls stack.

## Stage 5: Chaoswerk

Theme: the last machines and the last fight.

**Newly open:** everything. Draconic awakened and chaos tiers, NuclearCraft fusion, Mekanism antimatter, AE2 everything.

**Goal:** The Chaos Guardian. This is not an item goal. The obelisk asks for the things that make the fight possible, and the fight itself is the finale.

| Pillar | Item | Base amount | Why |
| --- | --- | --- | --- |
| Tech | Awakened Draconium Block | 64 | The chaos tier entry. |
| Tech | Antimatter Pellet | 200 | Mekanism's endgame line running for days. |
| Magic | Gaia Spirit Ingot | 256 | Botania endgame at scale. |
| Magic | Ars Nouveau Wilden Tribute | 64 | Every one is a Wilden Chimera fight. |

When the bar hits 98 percent, the final event date is set. The last items go in, the Chaos Island is opened (the obelisk teleports everyone), the Chaos Guardian fight happens live on every stream. Killing it ends the season with a fireworks command and the season's final quest.

**Quests:** Draconic Evolution endgame (10), NuclearCraft fusion (6), Mekanism antimatter (6), The Chaos Guardian (4). About 26.

## Tech and magic tied together

Recipe changes through KubeJS so that neither side runs alone. One per stage transition at least. The stage 2 ones are in `kubejs/server_scripts/tech_and_magic.js`; the rest follow with their stages:

| Stage | Recipe | Effect |
| --- | --- | --- |
| 2 | Create Empty Blaze Burner needs 2 Ars Nouveau Source Gems | Brass needs a mage. |
| 2 | Botania Terrestrial Agglomeration Plate needs 2 Create brass casings in place of 2 lapis blocks | Terrasteel needs an engineer. |
| 2 | Mekanism Metallurgic Infuser needs 2 Botania manasteel ingots in place of 2 iron | The first Mekanism machine needs mana. |
| 3 | AE2 Controller needs an Occultism Spirit Attuned Gem | Storage networks need a ritual. |
| 3 | Theurgy ore tripling and Mekanism ore tripling yield the same, Theurgy needs no power | A pure magic base is as good as a pure tech base. |
| 3 | Malum Soul Stained Steel used in Ender IO Soul Binder | Ender IO's soul side is Malum. |
| 4 | Draconic Energy Core stabiliser needs a Gaia Spirit | The dragon's power needs Gaia. |
| 4 | Mekanism Fusion Reactor laser focus needs an Ars Nouveau Source Gem Block and a Mahou mana crystal | Fusion needs magic to start. |
| 5 | Awakened Draconium needs Gaia Spirit Ingots in the ritual | The finale needs both. |

## What the obelisk is

Any block at spawn, picked by an admin with `/kw admin obelisk set` (Kronwerke Core 0.3.0). Right click hands in the stack in your hand, sneak and right click everything that fits. A chest or barrel placed next to it becomes the feeder of whoever placed it: factories pipe into it and every two seconds the goal takes what it can use, counted for that player. That is the point of the tech pillar. `/kw deposit` stays as the fallback.

Later, with Core on the clients: a screen with both pillars, progress bars and the top contributors.

## Numbers to revisit after the beta

- Cobblestone in stage 1 and steel in stage 3 are the two amounts most likely to be wrong. The beta measures how much a normal evening produces and both get adjusted.
- If the beta shows that one pillar finishes far ahead of the other, its next stage amount goes up by the same factor.
- Stage 4 and 5 amounts are guesses until someone plays Draconic Evolution 1.21.1 for a week.
