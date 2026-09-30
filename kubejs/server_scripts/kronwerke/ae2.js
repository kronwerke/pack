// Applied Energistics 2 family: charged certus, the network blocks and the big cells.
// See docs/RECIPES.md, table "Applied Energistics 2".

ServerEvents.recipes(event => {
  // Charged certus quartz, the stage 3 storage entry. The charger, Crafts & Additions,
  // the Oritech laser and the Advanced AE reaction chamber all go. A mage charges the
  // first crystals in the imbuement chamber; later a Powah energizing orb does two at once.
  event.remove({ output: 'ae2:charged_certus_quartz_crystal' })
  // The output filter does not see Oritech's result field, so the laser goes by id.
  event.remove({ id: 'oritech:laser/compat/ae2/chargedquartz' })

  event.custom({
    type: 'ars_nouveau:imbuement',
    input: { item: 'ae2:certus_quartz_crystal' },
    output: { id: 'ae2:charged_certus_quartz_crystal', count: 1 },
    pedestalItems: [
      { tag: 'c:dusts/redstone' },
      { tag: 'c:dusts/glowstone' }
    ],
    source: 2000
  }).id('kronwerke:ae2/charged_certus_imbuement')

  event.custom({
    type: 'powah:energizing',
    energy: 20000,
    ingredients: [
      { item: 'ae2:certus_quartz_crystal' },
      { tag: 'c:dusts/redstone' }
    ],
    result: { id: 'ae2:charged_certus_quartz_crystal', count: 2 }
  }).id('kronwerke:ae2/charged_certus_energizing')

  // Smart cables are a comfort: four covered cables, redstone, glowstone and an
  // electron tube make four. Fluix and all sixteen colours work the same way;
  // recolouring with dyes stays as AE2 has it.
  event.remove({ id: 'ae2:network/cables/smart_fluix' })
  let kwCableColours = ['fluix', 'white', 'orange', 'magenta', 'light_blue', 'yellow', 'lime', 'pink',
    'gray', 'light_gray', 'cyan', 'purple', 'blue', 'brown', 'green', 'red', 'black']
  kwCableColours.forEach(colour => {
    event.shaped(`4x ae2:${colour}_smart_cable`, [
      'CRC',
      'GTG',
      'CRC'
    ], {
      C: `ae2:${colour}_covered_cable`,
      R: '#c:dusts/redstone',
      G: '#c:dusts/glowstone',
      T: 'create:electron_tube'
    }).id(`kronwerke:ae2/${colour}_smart_cable`)
  })

  // ME drive: storage needs Mekanism, two advanced control circuits take the place of
  // the two fluix glass cables.
  event.remove({ id: 'ae2:network/blocks/storage_drive' })
  event.shaped('ae2:drive', [
    'IEI',
    'A A',
    'IEI'
  ], {
    I: '#c:ingots/iron',
    E: 'ae2:engineering_processor',
    A: 'mekanism:advanced_control_circuit'
  }).id('kronwerke:ae2/drive')

  // ME controller: networks need a ritual. A spirit attuned gem from Occultism sits in
  // place of the top fluix crystal.
  event.remove({ id: 'ae2:network/blocks/controller' })
  event.shaped('ae2:controller', [
    'SGS',
    'FEF',
    'SFS'
  ], {
    S: 'ae2:smooth_sky_stone_block',
    G: 'occultism:spirit_attuned_gem',
    F: 'ae2:fluix_crystal',
    E: 'ae2:engineering_processor'
  }).id('kronwerke:ae2/controller')

  // Molecular assembler: autocrafting needs Create, two precision mechanisms replace
  // the annihilation and formation cores.
  event.remove({ id: 'ae2:network/crafting/molecular_assembler' })
  event.shaped('ae2:molecular_assembler', [
    'IGI',
    'PCP',
    'IGI'
  ], {
    I: '#c:ingots/iron',
    G: 'ae2:quartz_glass',
    P: 'create:precision_mechanism',
    C: 'minecraft:crafting_table'
  }).id('kronwerke:ae2/molecular_assembler')

  // Pattern provider: same idea, a precision mechanism in the empty middle slot.
  // The cable part version still converts from the block.
  event.remove({ id: 'ae2:network/blocks/pattern_providers_interface' })
  event.shaped('ae2:pattern_provider', [
    'ITI',
    'APF',
    'ITI'
  ], {
    I: '#c:ingots/iron',
    T: 'minecraft:crafting_table',
    A: 'ae2:annihilation_core',
    P: 'create:precision_mechanism',
    F: 'ae2:formation_core'
  }).id('kronwerke:ae2/pattern_provider')

  // Big cell components: each one swaps its middle glass for a material of its stage.
  // 64k takes a sky ingot, 256k to 4M a draconium ingot, and 16M and up plus the bulk
  // component an awakened draconium nugget.
  let kwComponent = (id, output, edge, processor, previous, core) => {
    event.remove({ id: id })
    event.shaped(output, [
      'aba',
      'cdc',
      'aca'
    ], {
      a: edge,
      b: processor,
      c: previous,
      d: core
    }).id(`kronwerke:ae2/${output.split(':')[1]}`)
  }
  kwComponent('ae2:network/cells/item_storage_components_cell_64k_part', 'ae2:cell_component_64k',
    '#c:dusts/glowstone', 'ae2:calculation_processor', 'ae2:cell_component_16k', 'naturesaura:sky_ingot')
  kwComponent('ae2:network/cells/item_storage_components_cell_256k_part', 'ae2:cell_component_256k',
    '#c:dusts/sky_stone', 'ae2:calculation_processor', 'ae2:cell_component_64k', 'draconicevolution:draconium_ingot')
  kwComponent('megacells:cells/cell_component_1m', 'megacells:cell_component_1m',
    'ae2:sky_dust', 'megacells:accumulation_processor', 'ae2:cell_component_256k', 'draconicevolution:draconium_ingot')
  kwComponent('megacells:cells/cell_component_4m', 'megacells:cell_component_4m',
    '#c:dusts/ender_pearl', 'megacells:accumulation_processor', 'megacells:cell_component_1m', 'draconicevolution:draconium_ingot')
  kwComponent('megacells:cells/cell_component_16m', 'megacells:cell_component_16m',
    '#c:dusts/ender_pearl', 'megacells:accumulation_processor', 'megacells:cell_component_4m', 'draconicevolution:awakened_draconium_nugget')
  kwComponent('megacells:cells/cell_component_64m', 'megacells:cell_component_64m',
    'ae2:matter_ball', 'megacells:accumulation_processor', 'megacells:cell_component_16m', 'draconicevolution:awakened_draconium_nugget')
  kwComponent('megacells:cells/cell_component_256m', 'megacells:cell_component_256m',
    'ae2:matter_ball', 'megacells:accumulation_processor', 'megacells:cell_component_64m', 'draconicevolution:awakened_draconium_nugget')

  event.remove({ id: 'megacells:crafting/bulk_cell_component' })
  event.shaped('megacells:bulk_cell_component', [
    'aba',
    'cdc',
    'aea'
  ], {
    a: 'ae2:sky_dust',
    b: 'ae2:spatial_cell_component_2',
    c: 'megacells:accumulation_processor',
    d: 'draconicevolution:awakened_draconium_nugget',
    e: 'megacells:cell_component_1m'
  }).id('kronwerke:ae2/bulk_cell_component')
})
