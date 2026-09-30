# Origins and Roles

How Kronwerke uses Neo Origins, and why each choice looks the way it does. Every player picks one **Herkunft** (origin) and one **Rolle** (role) on first join. The mod's generic list of about 60 origins and 20 classes is replaced by nine origins and seven roles that belong to this world.

## Principles

1. **Fewer, better choices.** Nine origins, seven roles. Each one says in its first sentence where it comes from in Kronwerke and what it is for.
2. **Every origin has a real downside.** Something a player notices every session, not a footnote. The upsides are sized against it.
3. **Nothing skips progression.** No flight (not even in stage 4), no extra ore, no bonus output on goal items, no way to make a stage item early. Powers make you faster or tougher at what you are already allowed to do.
4. **Origins shape how you play, roles shape what you do for the server.** Roles are lighter (three small bonuses, no downside) and each one points at a pillar of the obelisk goals.
5. **Two origins for newcomers.** Kronbürger and Mühlenkind have low impact and nothing to manage.
6. **Nobody progresses alone.** Several downsides are there so players need each other: the Aurakind needs friends in the Nether, the Tiefgräber avoids the daytime surface, the Kronbürger heals best with others around.

## How it is wired

| What | Where |
| --- | --- |
| Layer replacements | `kubejs/data/neoorigins/origins/origin_layers/origin.json` and `class.json`, both with `"replace": true` |
| Origins and roles | `kubejs/data/kronwerke/origins/origins/*.json` (roles are prefixed `rolle_`) |
| Powers | `kubejs/data/kronwerke/origins/powers/*.json` (role powers are prefixed `rolle_`) |
| Texts | `kubejs/assets/kronwerke/lang/de_de.json` (main) and `en_us.json` (fallback) |

- Neo Origins merges layer files from all datapacks by appending origins. A layer file with `"replace": true` overwrites the earlier definition instead, so the two files above leave only the Kronwerke entries in `neoorigins:origin` and `neoorigins:class`. The built-in origins still load (the orb and `/neoorigins set` can reach them) but are no longer offered.
- The layers get new names through `kronwerke.layer.origin` (Herkunft / Origin) and `kronwerke.layer.class` (Rolle / Role); the picker shows "Wähle deine Herkunft" and "Wähle deine Rolle".
- Text keys follow the mod's convention: `origins.kronwerke.<id>.name` / `.description` for origins and roles, `power.kronwerke.<power>.name` / `.description` for powers. Power JSONs carry no `name` field; the picker finds the key by the power id.
- Only power types, conditions, actions and fields that exist in Neo Origins 2.2.29 are used. Attribute ids (Ars Nouveau `ars_nouveau:ars_nouveau.perk.max_mana` and `.mana_regen`, Iron's Spells `irons_spellbooks:max_mana`, `neoforge:swim_speed`, `minecraft:generic.oxygen_bonus`) were checked against the registry on the test server.

## Herkunft (origins)

### Kronbürger (Crown Citizen)

Icon: Waystone. Impact: low. The default pick for newcomers: grew up in the town around the obelisk.

| Power | Effect | Why |
| --- | --- | --- |
| Gemeinsinn | Regeneration I while another player is within 16 blocks and you have been out of combat for 5 seconds. | The theme of the season as a power. Rewards playing together without making solo play worse than vanilla. |
| Zupackende Hände | Hunger drains 15 percent slower. | Small, always useful, nothing to learn. |
| Heimweh (downside) | Hunger drains 30 percent faster outside the Overworld (Nether, End, Mining Dimension and every other dimension). | Net 10 percent faster away from home. Noticeable on long Nether and End trips, harmless in the base. |

### Mühlenkind (Millchild)

Icon: Water Wheel. Impact: low. The second newcomer pick: grew up under the water wheels of the Steinwerk.

| Power | Effect | Why |
| --- | --- | --- |
| Flussatem | +2 oxygen bonus (air lasts about three times as long). | Building water wheels, locks and river foundations in stage 1. |
| Stromschwimmer | Swims 30 percent faster. | Same. |
| Nasse Hände | No mining penalty under water. | Same. No extra drops. |
| Trockene Kehle (downside) | Slowness I and Hunger I in biomes with a base temperature of 1.5 or more (desert, savanna, badlands, the Nether) unless standing in water. | Makes the Nether (stage 2) a place to visit with others, and deserts a detour. |

### Tiefgräber (Deepdigger)

Icon: the Mining Dimension's enchanted pickaxe. Impact: medium. From the tunnels of the Mining Dimension.

| Power | Effect | Why |
| --- | --- | --- |
| Stollenaugen | Night vision, toggled with the Night Vision key (default K). | The classic miner perk. |
| Hauerhand | Breaks pickaxe blocks 25 percent faster. | Speed only. No Fortune, no extra ore, so the ore economy is untouched. |
| Heimat unter Tage | Haste I in the Mining Dimension. | Ties the origin to a place that opens on day one. |
| Lichtscheu (downside) | Weakness I and Slowness I in daytime under open sky. A helmet does not help. | Real every day: the Tiefgräber builds under a roof or works at night. Uses `daytime` plus `exposed_to_sky` instead of the mod's sun check, which a helmet would cancel. |

### Messingblut (Brassblood)

Icon: Brass Ingot. Impact: medium. Born in the forges of the Messingwerk.

| Power | Effect | Why |
| --- | --- | --- |
| Hitzefest | Half damage from everything in `#minecraft:is_fire` (fire, lava, burning). | The Nether pioneer for stage 2: blaze powder feeds brass, and brass is the stage 2 goal. Lava is still deadly, just slower. |
| Schmiedeglut | Haste I while within 5 blocks of a furnace, blast furnace, smoker, Iron Furnaces furnace, blaze burner or campfire (checked once per second). | Rewards the forge corner of a base. |
| Rostig (downside) | Slowness I and Mining Fatigue I in water and in rain. | Rain hits everywhere in the Overworld, so this is felt often. |

### Aurakind (Aurachild)

Icon: Natural Altar. Impact: medium. Grew up next to a Nature's Aura altar.

| Power | Effect | Why |
| --- | --- | --- |
| Waldatem | Heals half a heart every 4 seconds in forest, taiga and jungle biomes. | Nature magic without touching crops. |
| Kräuterblut | Immune to Poison. | Small, thematic. |
| Naturglück | +1 Luck. | Better fishing and chest loot, no ore. |
| Fern der Wurzeln (downside) | Weakness I and Mining Fatigue I in the Nether and the End. | Stage 2 and stage 4 are exactly where others have to dig for the Aurakind. |

Deliberately not used: crop growth acceleration and extra bone meal. Neo Origins' growth power and its extra bone meal applications both call `performBonemeal` directly, which bypasses Mystical Agriculture's "no bone meal" rule on resource crops. That would be free ore essence.

### Quellgeborene (Sourceborn)

Icon: Source Gem. Impact: medium. Born at an Ars Nouveau source.

| Power | Effect | Why |
| --- | --- | --- |
| Tiefe Quelle | +50 Ars Nouveau max mana (base is 100). | About the value of Mana Boost II. More spells, not new spells: glyph tiers stay gated. |
| Zaubersinn | +50 Iron's Spells max mana (base is 100). | Same for the second spell system. |
| Zarter Leib (downside) | One heart less. | The mage is fragile. |
| Kein Eisen am Leib (downside) | Cannot wear iron, gold, diamond or netherite armor (the `neoorigins:heavy_armor` tag). | Mage robes and leather only. Modded armor is not in the tag unless the owner adds it in `config/neoorigins/gameplay.toml` (`armor_classes.heavy_armor`). |

### Runenträger (Runebearer)

Icon: Rune of Earth. Impact: medium. The obelisk's runes are burned into the skin. The tank.

| Power | Effect | Why |
| --- | --- | --- |
| Runenhaut | +2 natural armor. | Boss fights: Afrits, the dragon, Gaia, the Chaos Guardian. |
| Bannzeichen | 30 percent less damage from `#minecraft:witch_resistant_to` (magic, indirect magic, thorns, sonic boom). | Fits the rune theme; useful against witches, Gaia and spell mobs. |
| Standfest | +0.25 knockback resistance. | Holds the line. |
| Schwere Zeichen (downside) | 10 percent slower movement. | Felt on every walk. |

### Sternensplitter (Starshard)

Icon: Blue Starlight Crystal Shard (Eternal Starlight, stage 4). Impact: high. Carries a shard of the Sternwerk.

| Power | Effect | Why |
| --- | --- | --- |
| Sternensprung | Active: teleport to the block you look at, up to 16 blocks, 10 second cooldown, costs 2 hunger. Does not pass through walls. | Short range ender pearl. Mobility without flight. |
| Sternenstaub | Half fall damage. | Pairs with the jump. Chosen over slow falling, which with the jump would come close to gliding. |
| Endblick | Endermen do not get angry when looked at. | Flavor for the End in stage 4. |
| Splitterleib (downside) | Two hearts less. | The biggest health cut of all origins, for the most mobile one. |

### Chaosgezeichnete (Chaosmarked)

Icon: Chaos Shard. Impact: high. Marked by the chaos at the end of all stages. The fighter.

| Power | Effect | Why |
| --- | --- | --- |
| Chaosfunke | +2 attack damage. | Straight damage for streamers who want to fight. |
| Zehrendes Chaos | Heals one heart on every kill. | Sustain in a fight. |
| Unstet (downside) | Natural regeneration from food at half speed. | Between fights the Chaosgezeichnete heals slowly and leans on potions or a Kronbürger nearby. |

## Rolle (roles)

Roles have no downside and stay small. Each one names the part of the obelisk goals it helps with.

| Role | Icon | Powers | Goal it serves |
| --- | --- | --- | --- |
| Ingenieur (Engineer) | Wrench | Starts with a Create wrench. +1 cogwheel per hand-crafted cogwheel. Half damage from Create machines (crushing wheels, saws, drills, rollers, trains, fans). | The tech pillar: andesite alloy (stage 1), precision mechanisms eat cogwheels (stage 2). |
| Arkanist (Arcanist) | Novice Spell Book | +1 Ars Nouveau mana regeneration per second (base 5). Potions last 25 percent longer. Starts with a novice spell book. | The magic pillar: source gems, mana pearls, runes. |
| Baumeister (Builder) | Andesite Casing | Breaks overworld base stone 30 percent faster. +1.5 block reach. 40 percent less fall damage. | Stage 1 asks for 20 000 cobblestone; building the town. |
| Entdecker (Explorer) | Nature's Compass | Hunger drains 20 percent slower. 5 percent faster walking. Starts with a Nature's Compass. | Finding biomes, structures and the resources the town lacks. |
| Hüter (Keeper) | Shield | +2 armor. +1 heart. Weakness I for 4 seconds on undead it hits. | Afrit rituals (stage 3), the dragon and Gaia (stage 4), the Chaos Guardian. |
| Versorger (Provider) | Cooking Pot | 30 percent chance of twins when breeding. Food crafted or taken from a furnace or smoker gives +1 hunger and +0.5 saturation. Immune to the Hunger and Nausea effects. | Feeding thirty players over seven weeks. |
| Händler (Trader) | Bounty Board | About 15 percent cheaper villager trades. +1 Luck. Nine extra inventory slots, opened with the ability key, dropped on death. | Trading and hauling goods between bases. |

Deliberately not used for roles: the mod's `trade_availability` (villagers restock constantly, which turns any trading hall into endless diamond gear), `rare_wandering_loot` (wandering traders can offer elytra and nether stars), and `crop_harvest_bonus` (doubles Mystical Agriculture essence).

## Balance at a glance

| Origin | Impact | Upsides | Downside |
| --- | --- | --- | --- |
| Kronbürger | low | Regen near friends, less hunger | More hunger outside the Overworld |
| Mühlenkind | low | Air, swim speed, underwater mining | Slow and hungry in hot biomes |
| Tiefgräber | medium | Night vision, faster pickaxe, Haste in the Mining Dimension | Weak and slow in daylight under open sky |
| Messingblut | medium | Half fire damage, Haste at the forge | Slow and fatigued in water and rain |
| Aurakind | medium | Forest healing, poison immunity, Luck | Weak and fatigued in Nether and End |
| Quellgeborene | medium | +50 mana in Ars Nouveau and Iron's Spells | One heart less, no heavy armor |
| Runenträger | medium | Armor, magic resistance, knockback resistance | 10 percent slower |
| Sternensplitter | high | Short teleport, half fall damage, enderman calm | Two hearts less |
| Chaosgezeichnete | high | +2 damage, heal on kill | Half natural regeneration |

## Notes for the owner

- **Evolution.** Neo Origins' kill-based evolution (`config/neoorigins/gameplay.toml`, `[evolution] enabled = true`) is on. The Kronwerke origins have no `tier_powers`, so evolving does nothing for them, but players still get the English "You may evolve" prompt after 1 000 kills. Setting `enabled = false` there removes it. Evolution tiers were left out on purpose: they add health for mob kills, independent of the stages.
- **Duplicate ids.** Neo Origins also scans `data/<namespace>/origins/` for Origins-format files, so every Kronwerke origin shows up a second time as `kronwerke:origins/<id>` in `/neoorigins list` and in command suggestions. Those copies are in no layer and never offered; use the short ids (`kronwerke:tiefgraeber`) with `/neoorigins set`.
- **Server-side names.** `/neoorigins list` prints translation keys for the Kronwerke entries because the server does not read `kubejs/assets`. Clients show the German or English text.
- **Tuning.** All numbers live in the power JSONs and can be changed by hand; a `/reload` applies them. If a value is changed, update the matching description in both lang files.
