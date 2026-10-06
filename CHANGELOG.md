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

## 0.8.0

Needs a new world: the stage files, the quest ids and the goal data changed.

- FTB Chunks keeps force loaded chunks loaded while the whole team is offline (`config/ftbchunks-world.snbt`), so farms run overnight.

- The last sixteen older chapters rewritten too: Create (three), Undergarden, Eternal Starlight, Alfheim, Silent Gear, food, Theurgy, Eidolon, Malum, Draconic Evolution (two), antimatter, NuclearCraft, quarries and Mahou Tsukai. The whole book is in the short format now: 74 chapters, 2 820 quests.
- Kronwerke Core 0.6.2: FTB Quests failed to load the book once it passed about twelve thousand objects; it loads now at any size.
- Conflict free default keys (`config/defaultoptions/keybindings.txt`, reasons in `docs/KEYS.md`): origin skills on Z, X, C and Alt+R, the Ars wheel on V, Iron's Spells cast on Ctrl+V, the voice chat menu on Alt+V, and about fifty rarely used mod keys moved to Alt, Ctrl or Shift. The quest texts name the new keys.
- Silent Gear's azure silver, azure electrum and tyrian steel are stage 4, since azure ore only generates in end stone.
- Twenty-eight of the older chapters rewritten for streamers: action titles, the recipe first, one step per quest, checklists where a mod has many parallel things. Start and Finale, Mekanism, Ars Nouveau, Botania, Occultism and Hexerei, Immersive Engineering and Industrial Foregoing, Oritech, Powah and Ender IO, AE2, logistics and storage, the Nether, the End and exploration. Numbers that were wrong in the old text are corrected from the jars. 2 593 quests.
- Thirteen more chapters: PneumaticCraft (two), Flux Networks, Hostile Neural Networks, Der Aether, Deeper and Darker, Productive Trees with every crossing as a checklist, Mekanism: Erz Schritt für Schritt, Erste Farmen, and four checklists in a new group Checklisten: Strom, Werkzeug und Rüstung, Transport und Lager, Dimensionen und Reisen. 74 chapters, 2 168 quests.
- Stage corrections from writing the chapters: the heart of the deep and the warden carapace open in stage 3 so the Otherside portal can be lit in its own stage; the Flügel tiara, the Create jetpack and Mekanism's HDPE elytra are stage 4 (their recipes need Gaia spirits or an elytra); the atomic disassembler is stage 3, the harvester pylon and the Mystical Agriculture tinkering table stage 2, Cable Tiers mega devices stage 4, and the Mekanism More Machine large wind generator stage 5, since it alone makes more power than the nitro and fusion reactors together.
- Recipes: the Flux core yields four per craft again; the Productive Trees pollen sifter gets its recipe back; reinforced deepslate can be crafted from deepslate, steel and an echo shard; the Productive Bees brass comb gives nothing in the centrifuge.
- Occultism's enchanting stats for Apothic Enchanting are shipped under the path the current Apothic Enchanting reads, so the spirit attuned crystal and the large candles count at the enchanting table again.
- `config/pneumaticcraft-common.toml` ships with security station hacking off.
- More stage corrections: the spirit attuned gem is stage 2 as RECIPES.md says; Mekanism machines that need advanced circuits (osmium compressor, teleporter frame, thermal evaporation, boiler valve, painting machine, flamethrower) are stage 3, those that need elite or ultimate circuits or lithium (combiner, solar neutron activator, the induction matrix, dimensional stabilizer, pigment mixer, modification station, the More Machine presser, planting station and gas collector) are stage 4.
- Cataclysm's overworld structure eyes (desert, cursed, abyss, mech, storm) get a second recipe with a source gem and an ender pearl instead of the eye of ender, so the stage 1 bosses can be found in stage 1.
- Default Options (keybinding and option defaults), FancyMenu, Drippy Loading Screen with Konkrete and Melody, all client side, for the Kronwerke title and loading screens.
- Kronwerke Core 0.6.1: no whitelist in singleplayer, and server list scanners no longer spam the log.
- WorldEdit is out. At server start it builds a state map for every block, and with FramedBlocks and the other new mods that blocked the server thread for nine minutes and ran a 3.6 GB heap out of memory. 249 mod files.
- The Farming for Blockheads market sells the Productive Trees hybrids of generations 1 to 3 and the mutation saplings, 1 to 4 emeralds by generation (`kubejs/data/kronwerke/market_presets`, `kubejs/data/kronwerke/recipe/market/productivetrees`). The mod's trees do not generate in the world, so this is the way in; the later generations, the glowing trees and the loot saplings stay with breeding and loot.
- Sixteen new chapters close the gaps for mods that had none: Mystical Agriculture, Productive Bees with Metalworks, Just Dire Things, Iron's Spells 'n Spellbooks, Apotheosis with the Apothic mods, EvilCraft, Reliquary, Forbidden and Arcanus, Refined Storage with Cable Tiers, Rohre und Router (Pipez, Modular Routers, Ranged Pumps), Komfort, Create: Erweiterungen (Steam 'n' Rails, Connected, Dragons Plus, Enchantment Industry, Mechanical Spawner, Diesel Generators), Bosse der Oberwelt (Cataclysm, Born in Chaos, Mowzie's Mobs), Tipps und Tricks, Bauen and Kochen. 61 chapters, 1 636 quests. Every number in them comes from the jars and the server configs.
- The new chapters use a shorter format: the title is the action, the subtitle the result, the first paragraph the recipe or the handful of steps, then a line or two on why. Checklists for seeds, bees, spells and meals sit at the end of their chapters.
- New mods: PneumaticCraft: Repressurized, Flux Networks, Hostile Neural Networks, The Aether, Deeper and Darker, Productive Trees, Botany Pots and Botany Trees, Cooking for Blockheads, FramedBlocks, Chipped, Pylons, Item Collectors, Ranged Pumps, Simple Magnets, Cobweb. All staged in `tools/stages/spec.py`: the Aether opens with the Nether, the Otherside with the Undergarden, PneumaticCraft and the deep learner start in stage 2, Flux Networks, drones and the simulation chamber in stage 3, the loot fabricator and the pneumatic armor in stage 4.
- Six recipes tie the new mods in (`kubejs/server_scripts/kronwerke/added.js`, reasons in `docs/RECIPES.md`): the flux compressor, the dynamo and the Flux controller take Mekanism circuits, the drone a precision mechanism, the Flux core a source gem, the simulation chamber a source gem block, the loot fabricator an engineering processor.
- PneumaticCraft's heat entry for Botania's blaze block points at a block that exists in the pack's Botania build.
- The item registry (`tools/stages/items.txt`) has 32 306 items now.

## 0.8.1

- Cross links: 25 recipes take one part from another mod of their stage (andesite alloy, circuits, brass, source gems, mana pearls), and Iron's Spells ink and the Forbidden and Arcanus artisan relic get recipes. Reasons in `docs/RECIPES.md`, the quest texts name the new recipes.

## 0.9.0

- Quest book: FTB Quests reads ids with Long.parseLong, so every id starting with 8 to F was replaced with a random one on load. That cut the lang keys and the dependencies of about half the chapters ("Unnamed" chapters, "Checkmark" quests, missing groups). Ids now start with 1 to 7. Chapters are laid out from the dependency graph (`tools/quests/layout.py`): one band per heading, columns by depth, tall columns wrap, checklists as a grid, lines into another band hidden. The start chapter goes from a claimed base to the first obelisk deposit without crafting table, furnace or bed quests; the players know Minecraft.
- Kronwerke Core 0.7.2: the obelisk block (four blocks tall, crystal on top, unbreakable; an operator places it and it registers itself), a waystone and warp dust for every player on the first join, dimensions locked by stage (Nether and Aether with stage 2, Undergarden and Otherside with 3, End, Starlight and Reality Marble with 4), spawn protection 96 blocks around the world spawn, ranks in the tab list and above heads, German messages, items shown by name.
- Goals in `config/kronwerke/goals.json` are German: Das Fundament des Kronwerks, Das Messingwerk, Der Ofen schläft nie, Das Licht des Drachen, Der Chaoswächter.
- Nautical Ranks (by seavitas) ships in `resourcepacks/`, repacked with a 1.21.1 pack format, and is on by default through Default Options. Core uses its glyphs for the rank badges.
- Healing Campfire.
- Voice chat uses the server port (`port=-1` in `config/voicechat/voicechat-server.properties`): the host forwards one port, and UDP 24454 never reached the server.
- The guide books of every mod are stage 1.

## 0.9.1

- Kronwerke Core 0.7.3: the streamer menu (`/kw menu`, also `/kw invite` without a name) with heads, online dots and a field to invite, and a German `/kw` help with clickable lines.

## 0.10.0

- The Mining Dimension is a flat world 500 blocks deep (bedrock at the bottom, deepslate up to y 160, stone up to y 435), full of ore: 36 ore features from vanilla and the mods, from coal to thorium, spread over the whole depth (`kubejs/data/kronwerke/worldgen`). The build limit there is 512.
- The Overworld build limit is 608 (`kubejs/data/minecraft/dimension_type/overworld.json`).
- Compact Machines is out: pocket dimensions cost more performance than they give. Its quests and the room templates are gone.
- Incendium (eight Nether biomes, structures and bosses) and Nether Depths Upgrade (lava fishing and Nether fish).
- Origins: the downsides are trades instead of nuisances. No Slowness and no Mining Fatigue anywhere: the Mühlenkind has a heart less and burns twice as hard, the Tiefgräber takes 50 percent more damage in daylight and breaks deepslate in one hit, the Messingblut has a heart less and takes double magic damage, the Aurakind takes more damage in Nether and End, the Runenträger takes double fall damage, the Chaosgezeichnete is hunted by every monster within 32 blocks.
- Iron's Spells: the loot spell books are staged like the tier they match (evoker, blaze, druidic, villager, ice, rotten, cursed doll with gold in stage 2; the necronomicon and the archevoker's logbook in stage 3).
- Default Options sets GUI scale 2, master volume 50 percent and music 5 percent. Core 0.8.0 asks for the language after the first join.
- Kronwerke Core 0.8.0: the obelisk is a build ten blocks tall with a beacon style beam (`/kw admin obelisk build`), machines feed it through the intake block (`kronwerke:obelisk_intake`, recipe in `kubejs/server_scripts/kronwerke/obelisk.js`), the zone around it (8 blocks) is open for pipes inside the spawn protection. The Core config ships in `config/kronwerke-common.toml`.
- Voice chat on UDP 19132.
- Blocks that survive every explosion: bedrock, end portal frames and portals, reinforced deepslate, the Cataclysm altars and boss respawners (`spawn.blastProof` in the Core config).

## 0.10.1

- Loot crates work: the reward tables carried the crate under the wrong key, so a quest's crate opened to nothing. A crate now gives three rolls (rare: two) of its table.
- Trims: Elytra Trims, More Armor Trims (13 new patterns), Tool Trims (weapons and tools on the smithing table) and Trims Expanded (more materials, glow ink among them).
- Kronwerke Core 0.8.1: `/kw` opens the hub with the goals and buttons, `/kw team` the team screen for slots and moving players between streamers.
- Kronwerke Core 0.8.2: bosses grow with the group (more health and damage per player nearby; with two or more players lightning, shockwaves and a rage), the Chaos Guardian fight is explained once to a player who comes close, and `/kw testworld` takes operators into the screenshot world.
- The screenshot world: `kronwerke:testworld` is a void dimension with one grey concrete box per scene and a sign for each; `/kw testworld` builds it on the first visit.

## 0.10.2

- Radiation: the career dose from Nuclear Radiation gave permanent Weakness, Mining Fatigue and Bad Luck after half a sievert and faded at a rate that never mattered. The stages now start at 1, 3, 6 and 10 Sv, the dose fades 300 times faster (about 0.3 Sv per hour), and the warning band for ambient radiation starts at 10 instead of 1 mSv/h. An operator clears a player with `/nr clear <name>`.
- Spawner loop closed: a silk touched spawner (Apothic Spawners) also dropped Ender IO's broken spawner, so one spawner gave both items on every break. Ender IO's drop is off; a broken spawner is crafted from a spawner instead (1:1) and the soul binder gives it its mob as before.
- Tiefgräber: Tiefenschlag covers every deepslate ore, modded ones included (`#c:ores_in_ground/deepslate` plus the Mekanism and NuclearCraft ores without the tag).
- The class skill (the Händler's bag, among others) is pinned to H in the default keys.

## 0.11.0

- Loot rewards in quests work: FTB Quests reads the table id as a number and the book wrote it as text, so every loot reward had no table and gave nothing.
- Terrain: the overworld really goes up to y 608 now. Tectonic set the height from its own config (320) and overrode the pack's dimension type; `config/tectonic.json` has min_y -64 and max_y 608, twice the vertical scale with a boost for mountains, deeper oceans, wider mountain ranges and rivers, and snow further up. Only chunks generated from now on get the new terrain.
- The test world is filled: one box per line of `docs/SCREENSHOTS.md` with the scene for each shot, generated by `tools/shots/build.py`. The signs face the path.
- Kronwerke Core 0.9.0: the admin panel (`/kw admin`), the season start (`/kw admin season start`), a taller obelisk with pedestals and the leaderboard wall, and screens whose text fits. The feeder zone around the obelisk is 10 blocks.

## 0.11.1

- The test world is whole again: every water and lava source sits in a basin, the obelisk scene builds the real obelisk, empty scenes have a stage with glow frames and a label, the wither scene shows a skull instead of a live wither, and the crystals stand on obsidian over bedrock.
- The quest book has its own theme: a dark stone background in a gold frame, Kronwerke colours for open, started, done and locked quests, redrawn quest shapes with a rim, softer dependency lines in gold once a quest is done. Hubs with more than four follow-up quests and quests with more than three requirements hide their lines, so chapters stop looking like spiderwebs. The Create chapters use circles instead of gears by default, and chapter titles sit on a plate.

## 0.11.2

- Kronwerke Core 0.10.0: every screen on one frame with a brass border, tooltips and a grow-in; the hub with the stages as a path of rings and the selected stage with icons, counts and bars; the admin panel with a tab rail and player heads; the whitelist screen and the language question in the same look.
- The test world no longer summons the Draconic guardian crystal or a dragon in automatic scenes; such scenes get a note instead.

## 0.11.3

- Kronwerke Core 0.11.0: the crystal floats and turns above the obelisk with three shards circling it, coloured by the goal (cyan to gold as it fills, purple on hold, gold when done) and flaring on every deposit; animated rune bands, glowing motes and sparks.
- Connected textures for the obelisk through Athena: the steps of the plinth read as one slab each with a brass rim, the trunk as one monolith with a brass seam only at its outline. The tiles come from `tools/textures/ctm.py`; the models are written by a client script into KubeJS's last virtual pack, since `kubejs/assets` sits below the mods in the resource pack order and cannot override a mod's model.

## 0.11.4

- Kronwerke Core 0.13.0: the obelisk grows a tier with every completed stage (its own glowing blocks), the completion rite with the sky torn open into a galaxy for everyone, the great beam, shockwave and veil shaders, deposits answered by size, hum, slumber, daily streaks, rune particles, fog by tier, aurora and half gravity on the plinth from the fourth stage. `/kw admin obelisk rite` rehearses the rite, `/kw admin obelisk tier <n>` previews a tier.

## 0.11.5

- Kronwerke Core 0.13.1: the obelisk's own sounds (hum, riser, tear, fanfare), the personal ledger by sneaking with an empty hand, the item flying into the trunk on a hand deposit, the awakening title when the hold is lifted, a third rune band at the third stage.

## 0.11.6

- Kronwerke Core 0.13.2: the rite tears the sky first and the beam comes out of the tear, the burst runs in slow motion with a flash, the crystal leans towards whoever comes close, `bossBarRadius` in the config.

## 0.11.7

- Kronwerke Core 0.13.3: ambient particles on every tier block, a shard that visits the pedestals every few minutes, `tier` and `slumbering` in the season json.

## 0.11.8

- Kronwerke Core 0.14.0: the obelisk seen from far away (signal into the sky, rune rings on the pavement, the rite beam across the map), a fuller torn sky with two star bands and six planets.

## 0.11.9

- Kronwerke Core 0.14.1: the thin sky above the obelisk between rites, the pylons firing into the crystal during the intake, cracks of light at the burst.

## 0.11.10

- Kronwerke Core 0.15.0: paving, flagstone and shard blocks for the grounds, the masonry textures drawn again.
- The connected textures of the plinth and the trunk carry detail inside the surface now: slabs with a grout cross on top of the plinth, two courses on its sides, chisel marks on the trunk.

## 0.11.11

- Kronwerke Core 0.15.1: the obelisk notices the players (gaze flare and whisper, crowd chord, whispers about the pillar furthest behind), the arch stone drawn again.

## 0.11.12

- Kronwerke Core 0.15.2: the gift flies from the hand to the crystal, the amount rises from it, a ring of light runs over the pavement.

## 0.11.13

- Kronwerke Core 0.15.3: the sleeping stone puts its lights out, the first gift after a day of sleep wakes them ring by ring; `/kw admin obelisk sleep` for previews.

## 0.11.14

- Kronwerke Core 0.15.4: gauges above the pedestals show each pillar as a column of light, the weakest one flickering.

## 0.11.15

- Kronwerke Core 0.15.5: the champion of each pillar on its pedestal as a head, the gauge as a hollow column.
