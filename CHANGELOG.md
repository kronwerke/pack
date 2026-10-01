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

## 0.5.2

- Kronwerke Core 0.4.1, now on clients as well: Chapters hid every locked item in JEI with a call of its own, which kept the client busy for about ten minutes after joining until the server timed it out. Core batches those calls.

## 0.5.3

- Kronwerke Core 0.4.2: joining no longer freezes. After 0.4.1 Chapters still spent about eight minutes looking up every recipe that makes a locked item or fluid, to hide it in JEI. Core skips those lookups. Locked things stay out of JEI's list and the server still refuses to make them.

## 0.5.4

- Kronwerke Core 0.5.0: locked items can be picked up and carried again, but not held, worn or used; the action bar and the tooltip say which stage they belong to.
- No Chat Restrictions: chat works for accounts whose Microsoft settings block it.
- Traveler's Titles no longer shows a title on every biome change; dimension titles stay.
- Stage 3 now also locks what the design keeps for it: the Mekanism advanced tier (the stage 3 goal asks for advanced control circuits), the Immersive Engineering machines built from engineering blocks, Refined Storage and Cable Tiers, and dreamwood from the Alfheim trade.

## 0.5.5

- The quest book is rewritten in German and much deeper: 673 quests in 17 chapters instead of 180, step by step in the style of All the Mods, with chapter titles and section headings on the quest canvas.
- The text lives in `config/ftbquests/quests/lang/` (de_de, and en_us as the fallback for every other language). The lettering is rendered by `tools/quests/banners.py` in Big Shoulders Display into `kubejs/assets/kronwerke/textures/quests/`, which KubeJS hands to the clients. `tools/quests/check_images.py` checks every picture against the mod jars.
- Chapter groups and crates have German names.
- `docs/STAGES.md`: stage 3 lists Refined Storage and the engineering-block machines, and the mana pearl goal is 9 million mana, not 750 000.

## 0.6.0

- Recipes tie the mods together, slow at first and built for automation later: about a hundred changes in `kubejs/server_scripts/kronwerke/`, listed with their reasons in `docs/RECIPES.md`. Brass is a milestone (one ingot per blaze powder in a heated mixer, two in a superheated one), the precision mechanism takes five loops and only 60 percent come out, charged certus comes from the imbuement chamber or Powah's energizing orb, smart cables need an electron tube, the first manasteel comes from a Nature's Aura ritual, mana pearls need a brass casing under the pool, Mekanism's circuits need Create, AE2 and the End, and the big AE2 and MEGA cells need draconium.
- Stages are generated: `tools/stages/spec.py` says which stage every item belongs to and `tools/stages/build.py` writes the Chapters files as plain item lists. Chapters opens an item as soon as any stage lists it, so "@mekanism" in stage 2 had opened the advanced, elite and ultimate tiers, the digital miner and the QIO in stage 2. CI checks that the files match the spec.
- Every mod in the pack now has a stage, including the new addons and the ones that had none (Pipez, Modular Routers, LaserIO, XNet, Integrated Dynamics, Productive Bees, Productive Metalworks, Just Dire Things, Mystical Agriculture tiers, Iron Furnaces tiers, Sophisticated tiers, EvilCraft, Forbidden and Arcanus, Reliquary). The Mekanism elite tier moves to stage 4, Alfheim to stage 3, the spirit attuned gem to stage 2.
- New addons: Advanced AE, MEGA Cells, Applied Flux, Mekanism More Machine, Create Ore Excavation, Steam 'n' Rails, Create Diesel Generators and Create: Power Grid. Create: New Age is gone, Power Grid replaces it.
- Community goals ask for less bulk and add six milestone items, one per pillar in stages 1 to 3 (`kubejs/startup_scripts/milestones.js`). Milestones do not scale with the player count and are worth many points on the bar (Kronwerke Core 0.6.0).
- Draconium ore only generates in the End.
- The server console is much quieter: from 721 errors and 283 warnings at start to 5 and 240, by fixing the broken data of other mods rather than hiding it. Details in `docs/CONSOLE.md`.
- The quest book follows the new recipes and stages, with a Power Grid line and quests for the milestones.
- Neo Origins offers Kronwerke's own choices: nine origins (Herkunft) and seven roles (Rolle) instead of the generic forty, each with a real downside and none that flies or skips a stage (`docs/ORIGINS.md`). The kill counting evolution is off.

## Unreleased

- New mods: PneumaticCraft: Repressurized, Flux Networks, Hostile Neural Networks, The Aether, Deeper and Darker, Productive Trees, Botany Pots and Botany Trees, Cooking for Blockheads, FramedBlocks, Chipped, Pylons, Item Collectors, Ranged Pumps, Simple Magnets, Cobweb. 250 mod files. All staged in `tools/stages/spec.py`: the Aether opens with the Nether, the Otherside with the Undergarden, PneumaticCraft and the deep learner start in stage 2, Flux Networks, drones and the simulation chamber in stage 3, the loot fabricator and the pneumatic armor in stage 4.
- Six recipes tie the new mods in (`kubejs/server_scripts/kronwerke/added.js`, reasons in `docs/RECIPES.md`): the flux compressor, the dynamo and the Flux controller take Mekanism circuits, the drone a precision mechanism, the Flux core a source gem, the simulation chamber a source gem block, the loot fabricator an engineering processor.
- PneumaticCraft's heat entry for Botania's blaze block points at a block that exists in the pack's Botania build.
- The item registry (`tools/stages/items.txt`) has 32 306 items now.

## 0.7.0

- The quest book for stages 4 and 5: thirteen chapters, about 235 quests. The End, Eternal Starlight, Mekanism elite with fusion and the MekaSuit, NuclearCraft, AE2 advanced with MEGA, quarries (RFTools Builder, Quarry Plus), Draconic Evolution, Botania Gaia, Mahou Tsukai, Ars Nouveau epic; then Draconic awakened and chaos, Mekanism antimatter with the millions of AE2, and the finale. Crates for both stages.
- Polonium pellets open in stage 4: the fusion reactor frame needs them, and NuclearCraft makes polonium there. MekaSuit and Meka-Tool become craftable with them. Bound dislocators open with the unbound ones in stage 4.
- The Mekanism More Machine replicators no longer copy every ingot (including the Gaia spirit and awakened draconium ingots of the stage 5 goal) or multiply fissile fuel and antimatter.
- Summoning a Mahou Tsukai Mystic Staff costs 2 000 mana instead of 100; the stage 4 goal asks for thirty of them.
- The quest book for stage 3: fifteen chapters, about 280 quests. Applied Energistics 2, Logistics (Integrated Dynamics, XNet, LaserIO, Compact Machines, Mining Gadgets), Mekanism advanced, Powah, Ender IO, Industrial Foregoing, Oritech, Immersive Engineering heavy industry, Botania Alfheim, Ars Nouveau master, Occultism Afrit and Marid, Theurgy, Eidolon, Malum and the Undergarden. Stage 3 crates `s3_common`, `s3_uncommon`, `s3_rare`.
- Atomic alloy and the robit open in stage 3, so the teleporter and the digital miner, which the design promises for stage 3, can be built there. The quantum entangloporter and the 4x and 5x ore machines move to stage 4, where the elite and ultimate circuits they need open.
- Compact Machines can be crafted: its room templates and machine recipes ship in a built-in datapack that new worlds leave disabled, so the pack carries them in `kubejs/data/compactmachines/`.
- The Oritech foundry no longer makes netherite from one gold and one scrap.
- Quest texts: the stage 3 goal in the Occultism chapter names afrit essence, as the goal does; four chapter openings read less like a brochure.
