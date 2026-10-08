# Loot and mobs

What the world gives and how hard it hits back. Chests and mob drops get mod items on top of what they had; hostile mobs get tougher with every stage. Generated parts come from `tools/loot/build.py` (loot) and the `mobs` section of `config/kronwerke-common.toml` (Kronwerke Core).

## Chests

Every chest table of a structure (vanilla, YUNG's, Dungeons Arise, Nova Structures, Cataclysm, the Aether, Deeper and Darker, the Undergarden, Eternal Starlight and the magic mods' own) keeps its loot and rolls one of four pools on top, through NeoForge global loot modifiers. Lootr fills each player's copy from the same table, so everyone gets their own roll. Items of later stages are in on purpose: they can be carried and stored, not used, until their stage opens, and they show what is coming.

Tables are sorted by name: treasure, boss, reward, vault, library, temple, stronghold, mansion and the like are rare; nether and end structures have their own pool; everything else is common. Sub-tables that mods inject into others are left out, so nothing rolls twice.

### Common (1 to 2 rolls, nothing in 30 of every 100)

| Item | Weight | Count |
| --- | --- | --- |
| `create:andesite_alloy` | 10 | 2 to 6 |
| `create:zinc_ingot` | 6 | 1 to 3 |
| `create:cogwheel` | 6 | 1 to 4 |
| `ars_nouveau:source_gem` | 8 | 1 to 3 |
| `naturesaura:gold_leaf` | 6 | 1 to 4 |
| `irons_spellbooks:arcane_essence` | 6 | 1 to 4 |
| `mysticalagriculture:inferium_essence` | 8 | 2 to 8 |
| `silentgear:blueprint_paper` | 4 | 2 to 6 |
| `botania:mana_powder` | 5 | 1 to 4 |
| `occultism:silver_ingot` | 4 | 1 to 3 |
| `sophisticatedbackpacks:upgrade_base` | 3 | 1 |
| `create:brass_ingot` | 2 | 1 to 3 |
| `mekanism:ingot_osmium` | 2 | 1 to 3 |

### Rare (1 to 3 rolls, nothing in 10 of every 79)

| Item | Weight | Count |
| --- | --- | --- |
| `create:brass_ingot` | 8 | 2 to 6 |
| `create:precision_mechanism` | 3 | 1 |
| `create:electron_tube` | 4 | 1 to 3 |
| `mekanism:ingot_osmium` | 6 | 2 to 6 |
| `mekanism:basic_control_circuit` | 4 | 1 to 2 |
| `botania:manasteel_ingot` | 6 | 1 to 4 |
| `botania:mana_pearl` | 3 | 1 |
| `naturesaura:infused_iron` | 6 | 2 to 5 |
| `irons_spellbooks:arcane_essence` | 6 | 3 to 8 |
| `mysticalagriculture:prosperity_shard` | 5 | 2 to 5 |
| `forbidden_arcanus:arcane_crystal` | 4 | 1 to 3 |
| `occultism:spirit_attuned_gem` | 3 | 1 |
| `ae2:certus_quartz_crystal` | 4 | 2 to 5 |
| `eidolon_repraised:soul_shard` | 3 | 1 to 3 |
| `malum:raw_soulstone` | 3 | 1 to 3 |
| `draconicevolution:draconium_dust` | 1 | 1 to 2 |

### Nether (1 to 2 rolls, nothing in 15 of every 44)

| Item | Weight | Count |
| --- | --- | --- |
| `create:brass_ingot` | 6 | 1 to 4 |
| `evilcraft:dark_gem` | 6 | 1 to 4 |
| `forbidden_arcanus:arcane_crystal` | 5 | 1 to 3 |
| `justdirethings:raw_blazegold` | 5 | 1 to 3 |
| `create:blaze_cake` | 2 | 1 |
| `powah:uraninite` | 3 | 2 to 5 |
| `mekanism:ingot_refined_glowstone` | 2 | 1 to 2 |

### End (1 to 2 rolls, nothing in 10 of every 28)

| Item | Weight | Count |
| --- | --- | --- |
| `draconicevolution:draconium_dust` | 6 | 2 to 6 |
| `mekanism:ingot_refined_obsidian` | 4 | 1 to 3 |
| `botania:pixie_dust` | 4 | 1 to 3 |
| `ae2:singularity` | 1 | 1 |
| `justdirethings:celestigem` | 3 | 1 to 2 |

## Mob drops

Killed by a player, with Looting adding to the chance.

| Mob | Item | Chance | Per Looting level |
| --- | --- | --- | --- |
| every hostile mob | `irons_spellbooks:arcane_essence` | 4 % | +2 % |
| `witch` | `hexerei:mandrake_root` | 25 % | +10 % |
| `zombie` | `create:zinc_nugget` | 10 % | +5 % |
| `husk` | `create:zinc_nugget` | 12 % | +5 % |
| `zombie` | `create:copper_nugget` | 12 % | +5 % |
| `enderman` | `ae2:certus_quartz_dust` | 6 % | +3 % |
| `wither_skeleton` | `evilcraft:dark_gem` | 12 % | +5 % |
| `blaze` | `justdirethings:raw_blazegold` | 8 % | +4 % |
| `drowned` | `aquaculture:neptunium_nugget` | 3 % | +2 % |

Arcane essence from every hostile mob is the main change: Iron's Spells stalled without it, and fighting is now a source.

## Mobs grow with the stages

Kronwerke Core gives every hostile mob that enters a world the modifiers of the open stage (main counts the completed goals; side worlds learn it over the bus). Bosses on the boss list are left to the group scaling.

| Stage | Health | Damage | Armor |
| --- | --- | --- | --- |
| 1 | base | base | base |
| 2 | +30 % | +20 % | +2 |
| 3 | +70 % | +45 % | +4 |
| 4 | +120 % | +75 % | +7 |
| 5 | +180 % | +110 % | +10 |

Some mobs only spawn naturally from a stage on (spawners and structures are not touched): Eidolon's wraith and zombie brute from stage 3 with the mod; Iron's Spells' necromancer from 2; Born in Chaos's dread hounds, dire hound leader, mother spider, fallen chaos knight, Sir Pumpkinhead, missioner, demoman skeleton and phantom creeper from 2, and the nightmare stalker, lifestealer, Krampus and his henchmen, the supreme bonescaller and the spirit of chaos from 3; Mowzie's naga from 3.

Born in Chaos had 45 percent of all hostile spawn weight in the overworld, more than vanilla. Only 55 percent of its natural spawns happen now, which brings it to about a third.
