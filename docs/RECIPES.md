# Recipes

How Kronwerke changes recipes, and why. The stages decide when a mod opens; the recipes decide how the mods lean on each other once they are open. Stage assignments live in `tools/stages/spec.py`, the recipe changes in `kubejs/server_scripts/kronwerke/`.

## Principles

1. **Not an expert pack.** About a hundred changed recipes in a pack of 34 000. Every change has a reason a player can see in the quest book. No recipe needs more than two mods it does not belong to.
2. **Slow first, fast later.** The first route to a key material is manual and a little painful. A second route opens a stage later and is built for automation: more output per input, but it needs machines. Nobody should hand craft a stage 4 goal.
3. **Tech and magic lean on each other.** Every stage has at least one key tech item that needs magic and one key magic item that needs tech.
4. **One way to a milestone.** When an item is a milestone (brass, charged certus, the precision mechanism), alternative routes from other mods are removed. Compat recipes that would skip a milestone go.
5. **Goal items cannot be made before their stage.** Chapters only stops players from holding locked items, not machines from making them. So the last step of every goal item is either a crafting recipe (Chapters blocks crafting a locked item) or needs a machine or input that is itself locked until that stage. The one exception is on purpose: steel opens in stage 2 and is the bulk item of stage 3, where it has to run by the thousand.

## The ladder

| Stage | Tech milestone | Magic milestone | Storage |
| --- | --- | --- | --- |
| 1 Steinwerk | Andesite alloy, water wheels | Source gems, infused iron | Drawers, copper and iron chests |
| 2 Messingwerk | Brass, precision mechanism, electron tube | Manasteel, mana pearl, terrasteel | Compacting drawers, gold chests |
| 3 Stahlwerk | Steel at scale, advanced circuits, charged certus | Elementium, afrit essence | AE2 up to 16k, Refined Storage up to 16k |
| 4 Sternwerk | Elite circuits, draconium | Gaia spirit, mystic staff | AE2 64k and 256k, MEGA up to 4M, Advanced AE patterns |
| 5 Chaoswerk | Awakened draconium, antimatter | Gaia ingot | MEGA 16M to 256M, bulk cells, the quantum computer |

## Changes by family

The id of each new recipe is `kronwerke:<family>/<name>`. "Remove all" means every recipe that outputs the item, whatever mod adds it (Oritech, Create Crafts & Additions, Advanced AE and Productive Metalworks all add shortcuts).

### Create

| Item | Change | Why |
| --- | --- | --- |
| Brass ingot | Remove all. Heated mixing: 2 copper, 1 zinc, 1 blaze powder gives 1 brass. Superheated mixing: 2 copper, 1 zinc gives 2 brass. Crafting from nuggets and blocks stays. | Brass is the stage 2 milestone. The first ingots cost blaze powder; a blaze cake line doubles the output. |
| Precision mechanism | Remove all. Sequenced assembly on a brass sheet, 5 loops: deploy cogwheel, deploy electron tube, deploy iron nugget, press. 60 percent precision mechanism, the rest brass nuggets and cogwheels as scrap. | Speed controllers, arms and schematicannons should feel earned. |
| Mechanical crafter | Needs a precision mechanism. | Autocrafting with Create needs the milestone. |
| Andesite alloy | Crafting stays 1 per craft. Mixing gives 2. | Stage 1 goal item: hand crafting is slow, a mixer line doubles it. |

### Applied Energistics 2

| Item | Change | Why |
| --- | --- | --- |
| Charged certus quartz | Remove all (charger, Crafts & Additions, Oritech laser, Advanced AE reaction chamber). Ars Nouveau imbuement: certus crystal, 2 000 source, pedestals with redstone and glowstone dust, gives 1. Powah energizing orb: certus crystal and redstone, 20 000 FE, gives 2. | The stage 3 storage entry needs a mage first, a power plant later. |
| Fluix smart cable (and the coloured ones) | 4 covered cable, 2 redstone, 2 glowstone, 1 electron tube gives 4. | Smart cables are a comfort, not a given. |
| ME drive | 2 advanced control circuits in place of 2 of its fluix. | Storage needs Mekanism's circuits. |
| ME controller | Needs a spirit attuned gem from Occultism. | Networks need a ritual. |
| Molecular assembler | 2 precision mechanisms in place of the annihilation and formation cores. | Autocrafting needs Create. |
| Pattern provider | Needs a precision mechanism. | Same. |
| 64k and 256k cell components | Need a Nature's Aura sky ingot (64k) and a draconium ingot (256k). | The big cells are stage 4. |
| MEGA 1M and 4M components | Need a draconium ingot. | Stage 4. |
| MEGA 16M and larger, bulk cell component | Need an awakened draconium nugget. | Stage 5, the millions. |

### Mekanism, Immersive Engineering and other tech

| Item | Change | Why |
| --- | --- | --- |
| Basic control circuit | Remove all. Metallurgic infusing: electron tube and 20 redstone. | Mekanism's first circuit needs Create's rose quartz and brass tier. |
| Advanced control circuit | Remove all. Crafting: basic circuit, 2 infused alloy, 1 AE2 printed silicon. | Stage 3 goal item: only craftable once AE2's inscriber is open. |
| Elite control circuit | Remove all. Crafting: 2 advanced circuits, 2 reinforced alloy, 1 draconium dust. | Stage 4 goal item: needs the End. |
| Ultimate control circuit | Remove all but Mekanism's own crafting. | Stays as it is, stage 4. |
| Steel casing | Andesite alloy in place of glass. | Andesite alloy for Mekanism. |
| Crusher | Crushing wheel from Create in place of the lava bucket. | Mekanism grinds with Create's wheels. |
| Metallurgic infuser | Manasteel (already in `tech_and_magic.js`). | |
| Light engineering block | Brass sheet in place of one copper ingot. | IE's machines need brass. |
| Heavy engineering block | A precision mechanism in place of one steel component. | IE's big machines need Create. |
| Powah energizing orb | A Botania mana diamond on top. | The power mod needs mana to start. |
| Ender IO soul binder | Malum soul stained steel. | The soul side of Ender IO is Malum. |
| Ender IO broken spawner | One spawner (picked up with silk touch) in the crafting grid. | Ender IO's own drop is off: with Apothic Spawners' silk touch drop a spawner gave both items on every break, and placing the spawner again made that a loop. The soul binder gives the broken spawner its mob as before. |
| Draconic energy core stabilizer | A Gaia spirit. | The dragon's power needs Gaia. |
| Mekanism laser focus matrix | Ars Nouveau source gem block. | Fusion needs magic to start. |
| Awakened draconium (fusion) | Gaia spirit ingots in the injectors. | The finale needs both. |
| Oritech foundry netherite | Removed. | One gold and one scrap made an ingot, a quarter of the vanilla price. |
| Mekanism More Machine replicators | The item replicator copies stones, ores, logs, planks and only iron, copper and gold ingots; the chemical replicator copies nothing (`kubejs/data/mekmm/data_maps/`). | It copied every ingot, including Gaia spirit and awakened draconium ingots of the stage 5 goal, and multiplied fissile fuel and antimatter. |
| PneumaticCraft flux compressor and pneumatic dynamo | A Mekanism basic control circuit instead of the printed circuit board. | The FE side of PneumaticCraft starts with the one circuit route of the pack. |
| PneumaticCraft drone | A precision mechanism under the circuit board. | A flying machine, like the AE2 assembler. |
| Flux Networks core | A source gem instead of the eye of ender. | Wireless power is where magic meets tech. |
| Flux Networks controller | An advanced control circuit in the middle. | The controller is the stage 3 unlock of the mod. |
| Hostile Neural Networks simulation chamber | A source gem block instead of obsidian in the middle. | Simulations run on source. |
| Hostile Neural Networks loot fabricator | An engineering processor instead of the comparator. | The fabricator is a stage 4 machine. |
| Productive Trees pollen sifter | Gets its recipe back (planks, sticky piston, iron, brush). | The mod drops the recipe when Productive Bees is installed; breeding by hand should not depend on bees. |
| Reinforced deepslate | Four deepslate, four steel ingots and an echo shard make two. | It frames the Otherside portal, vanilla never drops it, and the Occultism ritual eats a warden per block. The ritual stays as the other route. |
| Cataclysm desert, cursed, abyss, mech and storm eye | A second recipe each: a source gem where the eye of ender sits, an ender pearl in one other slot. The original recipes stay. | The eye of ender needs blaze powder from the Nether, so the overworld bosses meant for stage 1 could only be found by walking. |
| Productive Bees brass comb | No centrifuge output. | A brass bee would hand out the stage 2 milestone metal for free. The bee stays. |
| Farming for Blockheads market | Sells the Productive Trees hybrids of generations 1 to 3 and the five mutation saplings: 1, 2 and 4 emeralds by generation (`kubejs/data/kronwerke/recipe/market/productivetrees`). | The mod's trees do not generate in this version; the market is the way in. Generations 4 to 9, the glowing trees and the loot saplings stay with breeding and loot. |
| Mahou Tsukai Mystic Staff | Summoning costs 2 000 mana instead of 100 (`config/mahoutsukai-server.toml`). | The stage 4 goal asks for 30 staffs, each meant as a real investment of one mage. |

### Cross links

One part from another mod in a recipe that only used its own mod, so every machine leans on a pillar of its stage. All in `kubejs/server_scripts/kronwerke/links.js`; each swap replaces every occurrence of the old ingredient in that one recipe.

| Recipe | Change | Why |
|---|---|---|
| FramedBlocks framing saw, Productive Trees sawmill, Mystical Agriculture inferium growth accelerator | Iron or stone becomes andesite alloy | The first building and farm tools need the stage 1 tech goal item |
| Apotheosis salvaging table | Copper ingots become copper sheets | A reason to build the press early |
| Apotheosis simple reforging table | Iron ingot becomes a source gem | Reforging is magic |
| Just Dire Things coal generator, Create Diesel Generators engine, Crafts & Additions alternator | A basic control circuit | Every generator goes through the one circuit route of the pack |
| Hostile Neural Networks deep learner | Glass pane becomes an electron tube | Its only stage 2 machine touches tech |
| Productive Bees centrifuge | Grindstone becomes a millstone | A grinder from the grinding mod |
| Modular Routers router | Iron becomes andesite alloy | Logistics block on the Create base |
| Ranged Pumps pump | Diamond block becomes a mechanical pump | It is a pump |
| Pipez improved upgrade | Gold becomes brass | The stage 2 pipe tier needs the stage 2 metal |
| Silent Gear alloy forge | Iron block becomes a brass casing | The stage 2 forge sits in the brass tier |
| Refined Storage controller and disk drive | Advanced processor becomes an advanced control circuit | The same gate as the AE2 drive; Refined Storage is no way around it |
| Refined Storage autocrafter | Construction core becomes a precision mechanism | Autocrafting needs Create, as in AE2 |
| Ender IO SAG mill, alloy smelter | Piston becomes a crushing wheel, obsidian becomes a brass casing | Ender IO starts from Create like the Mekanism crusher |
| Oritech basic generator, Industrial Foregoing pity frame | A furnace or redstone block becomes an andesite casing | Their first machines start on the Create base |
| Mining Gadgets gadget (MK3) | Redstone becomes a basic control circuit | An FE tool needs the circuit |
| Undergarden catalyst | Copper becomes steel | A stage 3 portal costs a stage 3 metal |
| Mekanism teleportation core | Ender pearls become mana pearls | Teleporting is where magic helps |
| Tempad | The ender pearl becomes warp dust | The travel mods share a resource |
| Draconic fusion crafting core | Lapis blocks become source gem blocks | Fusion starts from source, like the fusion reactor |
| Iron's Spells common ink | New: glass bottle, ink sac, source gem | Ink was loot only and stalled the whole mod |
| Forbidden and Arcanus artisan relic | New: four deorum around a precision mechanism | It gated the forge progression and was loot only |

### Magic

| Item | Change | Why |
| --- | --- | --- |
| Manasteel ingot | Remove the pool recipe from iron and Mystical Agriculture's essence recipe. New first route: Nature's Aura ritual of the forest around an oak sapling with 4 infused iron, 2 livingwood twigs, 1 mana diamond and 1 gold leaf, gives 4 manasteel. Mass route: mana pool infusion of infused iron, 3 000 mana. | The first manasteel comes from a ritual, later from a pool fed by an altar. |
| Manasteel block | Pool route removed, crafting from ingots stays. | |
| Mana pearl | Mana pool infusion now needs a brass casing under the pool as catalyst. | Stage 2 goal item: the brass tier gates it, and tech meets magic. |
| Spirit attuned gem | Unlocked in stage 2. Spirit fire from lapis stays; the Ars Ocultas apparatus shortcut goes. | Occultism's stage 2 rituals need it. |
| Runic altar | A brass ingot in place of one livingrock. | Runes need an engineer. |
| Terrestrial agglomeration plate | Brass casings (already in `tech_and_magic.js`). | |
| Elven gateway core | Moves to stage 3 with the whole Alfheim trade. | Elementium is the stage 3 goal. |

### Milestones

One crafted item per pillar in stages 1 to 3, registered in `kubejs/startup_scripts/milestones.js`, recipes in `kubejs/server_scripts/kronwerke/milestones.js`, textures built by `tools/items/compose.py` from CC0 art (credits in `tools/items/sources/CREDITS.md`).

| Stage | Item | Recipe |
| --- | --- | --- |
| 1 | Steinwerk-Getriebe | Andesite casings, a large cogwheel, a mechanical press, a millstone, a water wheel, infused iron |
| 1 | Quellschlussstein | Source gem blocks, a source jar, mana diamonds, andesite alloy, gold leaf |
| 2 | Messingherz | Brass casings, a precision mechanism, electron tubes, a fire rune, a blaze burner |
| 2 | Runenkern | Water, air, fire and earth runes, mana pearls, brass plates, terrasteel |
| 3 | Stahlkern | Heavy engineering blocks, advanced control circuits, engineering processors, a steel casing, elementium |
| 3 | Elfenstern | Dragonstone, pixie dust, afrit essence, reinforced alloy |

### World generation

Draconium ore only generates in the End: the overworld and Nether ore features are switched off in `kubejs/data/draconicevolution/neoforge/biome_modifier/`. Otherwise stage 4's draconium could be mined and smelted on day one.

## Notes for writing recipes

- `event.remove({ output: ... })` misses Oritech's recipes, which list their outputs under `results`. Remove those by id.
- Scripts share one scope. Use `let` inside the event and names that do not clash across files.

## Checking

After a change, on the test server: `/reload`, then read `logs/kubejs/server.log` for errors from the file, then run the progression checker on the fresh dump:

```
python3 tools/check_progression.py /path/to/kubejs/exported/kw_recipes.json /path/to/mods kubejs/data/kronwerke/chapters/stages --goals config/kronwerke/goals.json --quests config/ftbquests/quests --report report.md
```

Every goal item must show up as reachable in its stage and nowhere in the leak list before it.

## The obelisk intake

`kronwerke:obelisk_intake` (Zubringer): a hopper over an andesite alloy between cobbled deepslate (`kubejs/server_scripts/kronwerke/obelisk.js`). Machines feed the obelisk through it, credited to the player who placed it. Cheap on purpose: everyone should have one on the first evening.

## The round of October 2026

Every mod leans on at least one other, and key materials get a slow first route and a fast later one. Generated from `tools/recipes/round.py`, which also checks every change against a dump of the running pack.

### Stage 1: the first machines of every mod need a part from another

| Recipe | Change | Why |
| --- | --- | --- |
| `ars_nouveau:imbuement_chamber` | `c:ingots/gold` becomes `create:golden_sheet` | The first Ars machine needs a press: magic starts with a little tech. |
| `ars_nouveau:enchanting_apparatus` | `c:ingots/gold` becomes `naturesaura:infused_iron` | The apparatus runs on aura iron from the Natural Altar. |
| `botania:mana_spreader` | `c:ingots/copper` becomes `create:copper_sheet` | Pressed copper for the spreader; Botania meets Create on day one. |
| `naturesaura:tree_ritual/nature_altar` | `minecraft:stone` becomes `botania:livingrock` | The Natural Altar stands on livingrock from a Pure Daisy: the two nature mods lean on each other. |
| `mysticalagriculture:infusion_altar` | `c:ingots/gold` becomes `ars_nouveau:source_gem` | Growing resources starts with source. |
| `mysticalagriculture:infusion_pedestal` | `c:ingots/gold` becomes `create:golden_sheet` | Pressed gold for the pedestals. |
| `waystones:warp_stone` | `minecraft:amethyst_shard` becomes `ars_nouveau:source_gem` | Travel is a spell: every waystone costs four source gems. |
| `irons_spellbooks:inscription_table` | `minecraft:wooden_slabs` becomes `ars_nouveau:archwood_slab` | Spell books are written on archwood. |
| `irons_spellbooks:arcane_anvil` | `minecraft:amethyst_block` becomes `ars_nouveau:source_gem_block` | The arcane anvil binds source. |
| `kronwerke:round/arcane_essence` | new: `minecraft:book`, `minecraft:lapis_lazuli`, `minecraft:glowstone_dust` to `irons_spellbooks:arcane_essence` | Arcane essence came only from loot and bees, which stalled Iron's Spells. A book imbued with lapis and glowstone gives three. |
| `occultism:crafting/golden_sacrificial_bowl` | `c:ingots/gold` becomes `create:golden_sheet` | The golden bowl is pressed gold. |
| `silentgear:material_grader` | `c:gems/quartz` becomes `ars_nouveau:source_gem` | The grader reads materials with source. |
| `ironfurnaces:furnaces/copper_furnace` | `c:ingots/copper` becomes `create:copper_sheet` | Furnaces are clad in pressed sheets. |
| `ironfurnaces:furnaces/iron_furnace` | `c:ingots/iron` becomes `create:iron_sheet` | Furnaces are clad in pressed sheets. |
| `ironfurnaces:furnaces/iron_furnace2` | `c:ingots/iron` becomes `create:iron_sheet` | Furnaces are clad in pressed sheets. |
| `sophisticatedbackpacks:iron_backpack` | `c:ingots/iron` becomes `create:iron_sheet` | Backpack tiers are plated with Create sheets. |
| `sophisticatedbackpacks:iron_backpack_from_copper` | `c:ingots/iron` becomes `create:iron_sheet` | Backpack tiers are plated with Create sheets. |
| `sophisticatedbackpacks:gold_backpack` | `c:ingots/gold` becomes `create:golden_sheet` | Backpack tiers are plated with Create sheets. |
| `sophisticatedstorage:basic_to_iron_tier_upgrade` | `c:ingots/iron` becomes `create:iron_sheet` | Storage tiers are plated with Create sheets. |
| `functionalstorage:compacting_drawer` | `minecraft:piston` becomes `create:mechanical_press` | A drawer that compacts has a press in it. |
| `functionalstorage:simple_compacting_drawer` | `minecraft:piston` becomes `create:mechanical_press` | A drawer that compacts has a press in it. |
| `functionalstorage:storage_controller` | `minecraft:comparator` becomes `create:andesite_casing` | The drawer network has a Create casing at its heart. |

### Stage 1 to 2: slow by hand, fast with heat

| Recipe | Change | Why |
| --- | --- | --- |
| `kronwerke:round/infused_iron_mixing` | new: `c:ingots/iron`, `c:ingots/iron`, `ars_nouveau:source_gem` to `naturesaura:infused_iron` | The altar makes one infused iron at a time with a lot of aura. A heated mixer with source makes two from a gem. |
| `kronwerke:round/source_gem_mixing` | new: `minecraft:amethyst_shard`, `minecraft:amethyst_shard`, `minecraft:glowstone_dust` to `ars_nouveau:source_gem` | Imbuing makes one gem for 500 source. A heated mixer makes three from two shards and glowstone. |

### Stage 2: the witch, blood and relic mods join the rest

| Recipe | Change | Why |
| --- | --- | --- |
| `hexerei:mixing_cauldron` | `minecraft:iron_ingot` becomes `naturesaura:infused_iron` | The witch's cauldron is bound with aura iron. |
| `reliquary:fertile_essence` | `c:dyes/green` becomes `hexerei:mandrake_root` | Fertility comes from the mandrake. |
| `reliquary:alkahestry_altar` | `minecraft:redstone_lamp` becomes `occultism:spirit_attuned_gem` | Alkahestry is spirit work. |
| `reliquary:apothecary_cauldron` | `minecraft:cauldron` becomes `hexerei:mixing_cauldron` | The apothecary brews in a witch's cauldron. |
| `evilcraft:crafting/blood_infuser` | `c:cobblestones` becomes `forbidden_arcanus:darkstone` | Blood work in darkstone. |
| `evilcraft:crafting/dark_tank` | `c:ingots/iron` becomes `born_in_chaos_v1:dark_metal_ingot` | The dark tank is forged from the dark metal of Born in Chaos. |
| `forbidden_arcanus:clibano_core` | `minecraft:blast_furnace` becomes `create:blaze_burner` | The clibano burns with a blaze. |
| `kronwerke:round/deorum_heated` | new: `minecraft:gold_ingot`, `forbidden_arcanus:arcane_crystal_dust`, `forbidden_arcanus:arcane_crystal_dust` to `forbidden_arcanus:deorum_ingot` | Deorum without mundabitur dust, in a heated mixer. |
| `kronwerke:round/deorum_superheated` | new: `minecraft:gold_ingot`, `forbidden_arcanus:arcane_crystal_dust` to `forbidden_arcanus:deorum_ingot` | A superheated mixer doubles deorum. |
| `pneumaticcraft:air_compressor` | `minecraft:furnace` becomes `create:blaze_burner` | Compressed air is heated by a blaze. |
| `pneumaticcraft:pressure_tube` | `c:glass_blocks` becomes `create:fluid_pipe` | Pressure tubes start from Create's pipes. |
| `justdirethings:gooblock_tier1` | `minecraft:dirt` becomes `mysticalagriculture:inferium_essence` | Goo grows from inferium. |
| `create_jetpack:jetpack` | `create:chute` becomes `aether:zanite_gemstone` | The jetpack's nozzles are zanite from the Aether. |

### Stage 3 and 4: deep magic and the far mods

| Recipe | Change | Why |
| --- | --- | --- |
| `malum:spirit_altar` | `c:ingots/gold` becomes `eidolon_repraised:arcane_gold_ingot` | Malum's altar stands on Eidolon's arcane gold. |
| `eidolon_repraised:worktable` | `minecraft:planks` becomes `malum:runewood_planks` | Eidolon's worktable is runewood. |
| `kronwerke:round/pewter_mixing` | new: `c:ingots/lead`, `c:ingots/iron` to `eidolon_repraised:pewter_blend` | Pewter blend by hand gives two, a mixer three. |
| `integrateddynamics:crafting/squeezer` | `c:storage_blocks/iron` becomes `create:mechanical_press` | The squeezer is a press. |
| `laserio:laser_connector` | `c:ingots/iron` becomes `ae2:fluix_crystal` | Lasers carry what fluix carries. |
| `xnet:controller` | `minecraft:comparator` becomes `ae2:logic_processor` | The network controller thinks with AE2's logic. |
| `rftoolsbase:machine_frame` | `c:ingots/iron` becomes `mekanism:ingot_steel` | RFTools machines start from steel. |
| `ae2:network/blocks/inscribers` | `minecraft:piston` becomes `create:mechanical_press` | The inscriber is a press. |
| `industrialforegoing:dissolution_chamber` | `minecraft:bucket` becomes `create:fluid_tank` | Dissolution in Create tanks. |
| `quarryplus:quarry` | `c:ingots/iron` becomes `eternal_starlight:deepsilver_ingot` | The quarry's frame is deepsilver from Eternal Starlight. |
| `mahoutsukai:attuner` | `minecraft:gold_ingot` becomes `botania:terrasteel_ingot` | Mahou Tsukai attunes to terrasteel. |
| `draconicevolution:components/draconium_core` | `c:ingots/gold` becomes `eternal_starlight:deepsilver_ingot` | Draconium cores are set in deepsilver. |
| `aquaculture:iron_fishing_rod` | `c:ingots/iron` becomes `create:iron_sheet` | The iron rod is pressed sheet. |
| `oritech:crafting/cooler` | `minecraft:ice` becomes `undergarden:froststeel_ingot` | Oritech's cooler holds the Undergarden's froststeel. |
| `powah:crafting/thermo_generator_basic` | `minecraft:iron_ingot` becomes `undergarden:froststeel_ingot` | A thermoelectric generator needs a cold side: froststeel. |
| `ae2:network/wireless_part` | `ae2:fluix_pearl` becomes `deeperdarker:sculk_transmitter` | AE2's wireless receiver listens through a sculk transmitter from the Otherside. |
| `eidolon_repraised:lesser_soul_gem` | `c:gems/quartz` becomes `deeperdarker:soul_crystal` | Eidolon's soul gem is cut from a soul crystal of the Otherside. |
| `draconicevolution:tools/dislocator` | `minecraft:ender_eye` becomes `deeperdarker:reinforced_echo_shard` | The dislocator remembers places with a reinforced echo shard. |

### Boss and treasure loot opens shortcuts

| Recipe | Change | Why |
| --- | --- | --- |
| `kronwerke:round/netherite_furnace_ignitium` | new: `cataclysm:ignitium_ingot`, `minecraft:magma_cream`, `c:furnaces/obsidian` to `ironfurnaces:netherite_furnace` | Who beat Ignis gets the netherite furnace without netherite: four ignitium. |
| `kronwerke:round/neptunium_diving_helmet` | new: `aquaculture:neptunium_ingot`, `create:copper_diving_helmet` to `create:netherite_diving_helmet` | Neptunium from the sea's treasure makes the diving helmet that also survives lava. |
| `kronwerke:round/neptunium_diving_boots` | new: `aquaculture:neptunium_ingot`, `create:copper_diving_boots` to `create:netherite_diving_boots` | The same for the diving boots. |

### Fast later: bulk for the stage goals once their stage is past

| Recipe | Change | Why |
| --- | --- | --- |
| `kronwerke:round/andesite_alloy_superheated` | new: `minecraft:andesite`, `minecraft:andesite`, `c:nuggets/iron` to `create:andesite_alloy` | Stage 1 hands out two per mixer run; from stage 2 a superheated mixer gives four from two andesite and one nugget. |
| `kronwerke:round/brass_alloy_smelter` | new: `c:ingots/copper`, `c:ingots/zinc` to `create:brass_ingot` | Brass is the stage 2 goal; from stage 3 the EnderIO alloy smelter makes four from three copper and a zinc. |

### Every plate on the press

| Recipe | Change | Why |
| --- | --- | --- |
| `kronwerke:round/press_thorium` | new: `c:ingots/thorium` to `nuclearcraft:thorium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_boron` | new: `c:ingots/boron` to `nuclearcraft:boron_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_tin` | new: `c:ingots/tin` to `nuclearcraft:tin_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_magnesium` | new: `c:ingots/magnesium` to `nuclearcraft:magnesium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_lithium` | new: `c:ingots/lithium` to `nuclearcraft:lithium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_cobalt` | new: `c:ingots/cobalt` to `nuclearcraft:cobalt_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_platinum` | new: `c:ingots/platinum` to `nuclearcraft:platinum_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_zirconium` | new: `c:ingots/zirconium` to `nuclearcraft:zirconium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_beryllium` | new: `c:ingots/beryllium` to `nuclearcraft:beryllium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_bronze` | new: `c:ingots/bronze` to `nuclearcraft:bronze_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_tough_alloy` | new: `c:ingots/tough_alloy` to `nuclearcraft:tough_alloy_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_palladium` | new: `c:ingots/palladium` to `nuclearcraft:palladium_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_hard_carbon` | new: `c:ingots/hard_carbon` to `nuclearcraft:hard_carbon_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_thermoconducting` | new: `c:ingots/thermoconducting` to `nuclearcraft:thermoconducting_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_extreme` | new: `c:ingots/extreme` to `nuclearcraft:extreme_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_manganese` | new: `c:ingots/manganese` to `nuclearcraft:manganese_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_sic_sic_cmc` | new: `c:ingots/sic_sic_cmc` to `nuclearcraft:sic_sic_cmc_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_hsla_steel` | new: `c:ingots/hsla_steel` to `nuclearcraft:hsla_steel_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_ferroboron` | new: `c:ingots/ferroboron` to `nuclearcraft:ferroboron_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_lithium_manganese_dioxide` | new: `c:ingots/lithium_manganese_dioxide` to `nuclearcraft:lithium_manganese_dioxide_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_graphite` | new: `c:ingots/graphite` to `nuclearcraft:graphite_plate` | NuclearCraft plates came only from its own machines; a Create press makes them one to one. |
| `kronwerke:round/press_hop_graphite` | new: `c:ingots/hop_graphite` to `immersiveengineering:plate_hop_graphite` | Immersive's graphite plate on the Create press too. |
