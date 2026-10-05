// Mekanism, Immersive Engineering and the other tech mods.
// See the tech table in docs/RECIPES.md for the reasons behind each change.

ServerEvents.recipes(event => {
  // Control circuits: one route per tier. Mekanism's infusing shortcuts and the
  // Oritech atomic forge compat all go.
  event.remove({ output: 'mekanism:basic_control_circuit' })
  event.remove({ output: 'mekanism:advanced_control_circuit' })
  event.remove({ output: 'mekanism:elite_control_circuit' })
  event.remove({ id: 'mekanism:control_circuit/infused_ultimate' })
  // The atomic forge lists its outputs as "results", which the output filter misses.
  for (let tier of ['basic', 'advanced', 'elite', 'ultimate']) {
    event.remove({ id: `oritech:atomicforge/compat/mekanism/${tier}_control_circuit` })
  }

  // The Oritech foundry makes netherite from one gold and one scrap, a quarter of the
  // vanilla price. Netherite stays at the smithing table.
  event.remove({ id: 'oritech:foundry/alloy/netherite' })

  // Basic circuit: an electron tube from Create infused with redstone.
  event.custom({
    type: 'mekanism:metallurgic_infusing',
    chemical_input: { amount: 20, tag: 'mekanism:redstone' },
    item_input: { count: 1, item: 'create:electron_tube' },
    output: { count: 1, id: 'mekanism:basic_control_circuit' },
    per_tick_usage: false
  }).id('kronwerke:tech/basic_control_circuit')

  // Advanced circuit needs printed silicon, so AE2's inscriber comes first.
  event.shaped('mekanism:advanced_control_circuit', [
    'ACA',
    ' P '
  ], {
    A: '#mekanism:alloys/infused',
    C: '#c:circuits/basic',
    P: 'ae2:printed_silicon'
  }).id('kronwerke:tech/advanced_control_circuit')

  // Elite circuit needs draconium dust from the End.
  event.shaped('mekanism:elite_control_circuit', [
    'CDC',
    'R R'
  ], {
    C: '#c:circuits/advanced',
    D: '#c:dusts/draconium',
    R: '#mekanism:alloys/reinforced'
  }).id('kronwerke:tech/elite_control_circuit')

  // Steel casing: andesite alloy in place of the glass.
  event.remove({ id: 'mekanism:steel_casing' })
  event.shaped('mekanism:steel_casing', [
    'SAS',
    'AOA',
    'SAS'
  ], {
    S: '#c:ingots/steel',
    A: 'create:andesite_alloy',
    O: '#c:ingots/osmium'
  }).id('kronwerke:tech/steel_casing')

  // Crusher: Create crushing wheels instead of lava buckets.
  event.remove({ id: 'mekanism:crusher' })
  event.shaped('mekanism:crusher', [
    'RCR',
    'WXW',
    'RCR'
  ], {
    R: '#c:dusts/redstone',
    C: '#c:circuits/basic',
    W: 'create:crushing_wheel',
    X: 'mekanism:steel_casing'
  }).id('kronwerke:tech/crusher')

  // Light engineering block: a brass sheet in the middle instead of the copper ingot.
  event.remove({ id: 'immersiveengineering:crafting/light_engineering' })
  event.shaped('4x immersiveengineering:light_engineering', [
    'igi',
    'gbg',
    'igi'
  ], {
    i: '#c:sheetmetals/iron',
    g: 'immersiveengineering:component_iron',
    b: '#c:plates/brass'
  }).id('kronwerke:tech/light_engineering')

  // Heavy engineering block: one steel component becomes a precision mechanism.
  event.remove({ id: 'immersiveengineering:crafting/heavy_engineering' })
  event.shaped('4x immersiveengineering:heavy_engineering', [
    'ipi',
    'geg',
    'igi'
  ], {
    i: '#c:sheetmetals/steel',
    g: 'immersiveengineering:component_steel',
    e: '#c:ingots/electrum',
    p: 'create:precision_mechanism'
  }).id('kronwerke:tech/heavy_engineering')

  // Energizing orb: a mana diamond on top.
  event.remove({ id: 'powah:crafting/energizing_orb' })
  event.shaped('powah:energizing_orb', [
    'gdg',
    'gcg',
    'rrr'
  ], {
    g: '#c:glass_blocks',
    d: 'botania:mana_diamond',
    c: 'powah:dielectric_casing',
    r: 'powah:dielectric_rod_horizontal'
  }).id('kronwerke:tech/energizing_orb')

  // Soul binder: Malum's soul stained steel instead of soularium.
  // A spawner picked up with silk touch (Apothic Spawners) is the only way to a broken
  // spawner. Ender IO's own drop is off in its config, because together with the silk
  // touch drop one spawner gave both items on every break.
  event.shapeless('enderio:broken_spawner', ['minecraft:spawner']).id('kronwerke:tech/broken_spawner')

  event.remove({ id: 'enderio:soul_binder' })
  event.shaped('enderio:soul_binder', [
    'IVI',
    'GCG',
    'IZI'
  ], {
    I: 'malum:soul_stained_steel_ingot',
    V: { type: 'enderio:empty_soul_storage', item: 'enderio:soul_vial' },
    G: '#c:gears/energized',
    C: 'enderio:ensouled_chassis',
    Z: 'enderio:z_logic_controller'
  }).id('kronwerke:tech/soul_binder')

  // Energy core stabilizer: a Gaia spirit on top.
  event.remove({ id: 'draconicevolution:machines/energy_core_stabilizer' })
  event.shaped('draconicevolution:energy_core_stabilizer', [
    'ASA',
    ' B ',
    'A A'
  ], {
    A: '#c:gems/diamond',
    S: 'botania:gaia_spirit',
    B: 'draconicevolution:particle_generator'
  }).id('kronwerke:tech/energy_core_stabilizer')

  // Laser focus matrix: fusion needs a source gem block to start.
  event.remove({ id: 'mekanismgenerators:laser_focus_matrix' })
  event.shaped('2x mekanismgenerators:laser_focus_matrix', [
    'SG ',
    'GRG',
    ' G '
  ], {
    S: 'ars_nouveau:source_gem_block',
    G: 'mekanismgenerators:reactor_glass',
    R: '#c:storage_blocks/redstone'
  }).id('kronwerke:tech/laser_focus_matrix')

  // Awakened draconium: two of the six draconium cores become Gaia ingots.
  event.remove({ id: 'draconicevolution:awakened_draconium_block' })
  let awakenedInjector = id => ({ consume: true, ingredient: { item: id } })
  event.custom({
    type: 'draconicevolution:fusion_crafting',
    catalyst: { type: 'draconicevolution:stack', count: 4, items: 'draconicevolution:draconium_block' },
    ingredients: [
      awakenedInjector('draconicevolution:draconium_core'),
      awakenedInjector('botania:gaia_ingot'),
      awakenedInjector('draconicevolution:draconium_core'),
      awakenedInjector('draconicevolution:dragon_heart'),
      awakenedInjector('draconicevolution:draconium_core'),
      awakenedInjector('botania:gaia_ingot'),
      awakenedInjector('draconicevolution:draconium_core')
    ],
    result: { count: 4, id: 'draconicevolution:awakened_draconium_block' },
    techLevel: 'wyvern',
    totalEnergy: 50000000
  }).id('kronwerke:tech/awakened_draconium_block')
})
