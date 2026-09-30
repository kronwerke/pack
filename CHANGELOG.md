# Changelog

## 0.1.0

First assembly. 222 mods on NeoForge 21.1.252, boots on a dedicated server. No quests, no stages, no balancing yet.

## 0.2.0

- Botania from the upstream 1.21.1 porting branch, built in `kronwerke/botania` and referenced by URL.
- Draconic Evolution as the endgame, NuclearCraft Neoteric, RFTools Builder and Additional Enchanted Miner for digging, Ultimate Mining Dimension.
- Neo Origins.
- Productive Bees from CurseForge (13.14.0), Botania refuses older versions.

## 0.3.0

- Chapters stage files for stages 2 to 5 under `kubejs/data/kronwerke/chapters/stages/`, checked against the mod jars with `tools/check_stages.py`.
- The five community goals for Kronwerke Core in `config/kronwerke/goals.json`.
- CI refreshes the packwiz index and commits it when it changed.

## 0.4.0

- The stage 1 quest book: Start Here, Create, Ars Nouveau, Botania, Food and Farming, Storage, Silent Gear and Exploration. 92 quests.
- Crates per stage. The stage 1 crates only hold stage 1 items; the old ones handed out brass, Mekanism steel and AE2 parts on day one.
- `tools/quests/check_quest_stages.py` fails when a quest or crate uses an item before its stage opens. `check_items.py` also knows items that have no lang entry.
- CI builds the quest book from `tools/quests/` and commits it with the index.
- The Imbuement Chamber is open from stage 1. It is the only way to make Source Gems, and the stage 1 goal asks for them.
- The Mining Dimension key (Enchanted Pickaxe) has a working recipe: its own sits in a folder 1.21 does not read and needs netherite.

## 0.5.0

- The stage 2 quest book: The Nether, Create: Brass, Create: Trains, Mekanism, Immersive Engineering, Botania: Runes, Ars Nouveau: Mage, Occultism and Hexerei. 88 quests, and a Brass, Steel and Terrasteel crate that only hold stage 2 items.
- Tech and magic tied together in `kubejs/server_scripts/tech_and_magic.js`: the empty blaze burner needs two Source Gems, the metallurgic infuser two manasteel ingots, the terrestrial agglomeration plate two brass casings.
- Stage 3 now locks what the design always kept for it: the Mekanism elite tier, the digital miner, teleporters, the quantum entangloporter and the injection and purification chambers. The antiprotonic nucleosynthesizer waits for stage 5.

## 0.5.1

- LuckPerms is gone. Its NeoForge build for 1.21.1 (5.4.140) fails to set up a joining player in time, the join is refused with "Invalid player data", and there is no newer build for 1.21.1. Operator levels cover what the server needs.
- TabTPS is gone. When a join fails, it throws on the quit event for a player it never saw, and that took the whole server down. spark still shows TPS.
- Kronwerke Core 0.4.0: `/kw admin bypass`, a quiet console for RCON, old logs deleted after 30 days.
- CI commits as Elchi.
