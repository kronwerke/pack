// Cross links: one part from another mod in recipes that touched only their own mod.
// Each change ties a machine to a pillar of its stage. Reasons in docs/RECIPES.md.

ServerEvents.recipes(event => {
  const swap = (id, from, to) => event.replaceInput({ id: id }, from, to)

  // Stage 1: Create's andesite alloy and Ars Nouveau's source gem into the first tools.
  swap('framedblocks:framing_saw', '#c:ingots/iron', 'create:andesite_alloy')
  swap('productivetrees:sawmill', '#c:ingots/iron', 'create:andesite_alloy')
  swap('mysticalagriculture:inferium_growth_accelerator', '#c:stones', 'create:andesite_alloy')
  swap('apotheosis:salvaging_table', '#c:ingots/copper', 'create:copper_sheet')
  swap('apotheosis:simple_reforging_table', '#c:ingots/iron', 'ars_nouveau:source_gem')

  // Stage 2: generators and engines take the one circuit route of the pack.
  swap('justdirethings:generatort1', 'minecraft:blast_furnace', 'mekanism:basic_control_circuit')
  swap('createdieselgenerators:crafting/diesel_engine', 'minecraft:flint_and_steel', 'mekanism:basic_control_circuit')
  swap('createaddition:mechanical_crafting/alternator', '#c:rods/iron', 'mekanism:basic_control_circuit')
  swap('hostilenetworks:deep_learner', '#c:glass_panes', 'create:electron_tube')
  // Stage 2: Create parts where the machine already is one.
  swap('productivebees:centrifuge', 'minecraft:grindstone', 'create:millstone')
  swap('modularrouters:modular_router', '#c:ingots/iron', 'create:andesite_alloy')
  swap('rangedpumps:pump', 'minecraft:diamond_block', 'create:mechanical_pump')
  swap('pipez:improved_upgrade', '#c:ingots/gold', 'create:brass_ingot')
  swap('silentgear:alloy_forge', '#c:storage_blocks/iron', 'create:brass_casing')

  // Stage 3: Refined Storage gets the gates AE2 has, so it is no shortcut around them.
  swap('refinedstorage:controller', 'refinedstorage:advanced_processor', 'mekanism:advanced_control_circuit')
  swap('refinedstorage:disk_drive', 'refinedstorage:advanced_processor', 'mekanism:advanced_control_circuit')
  swap('refinedstorage:autocrafter', 'refinedstorage:construction_core', 'create:precision_mechanism')
  // Stage 3: the other tech mods start from Create and Mekanism.
  swap('enderio:sag_mill', 'minecraft:piston', 'create:crushing_wheel')
  swap('enderio:alloy_smelter', '#c:obsidians', 'create:brass_casing')
  swap('oritech:crafting/basicgen', '#c:player_workstations/furnaces', 'create:andesite_casing')
  swap('industrialforegoing:machine_frame_pity', '#c:storage_blocks/redstone', 'create:andesite_casing')
  swap('mininggadgets:mininggadget', '#c:dusts/redstone', 'mekanism:basic_control_circuit')
  swap('undergarden:catalyst', '#c:ingots/copper', '#c:ingots/steel')
  // Stage 3: travel needs a little magic.
  swap('mekanism:teleportation_core', '#c:ender_pearls', 'botania:mana_pearl')
  swap('tempad:tempad', '#c:ender_pearls', 'waystones:warp_dust')

  // Stage 4: fusion crafting starts from source like the fusion reactor does.
  swap('draconicevolution:machines/crafting_core', '#c:storage_blocks/lapis', 'ars_nouveau:source_gem_block')

  // Iron's Spells ink came only from chests and mages, which stalled the whole mod.
  event.shapeless('irons_spellbooks:common_ink', [
    'minecraft:glass_bottle', 'minecraft:ink_sac', 'ars_nouveau:source_gem'
  ]).id('kronwerke:links/common_ink')

  // The Artisan Relic gates the whole forge progression of Forbidden and Arcanus and was
  // loot only. Four deorum around a precision mechanism make one.
  event.shaped('forbidden_arcanus:artisan_relic', [
    ' D ',
    'DPD',
    ' D '
  ], {
    D: 'forbidden_arcanus:deorum_ingot',
    P: 'create:precision_mechanism'
  }).id('kronwerke:links/artisan_relic')
})
