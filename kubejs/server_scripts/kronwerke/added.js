// The mods added in 0.8.0: PneumaticCraft, Flux Networks, Hostile Neural Networks.
// See docs/RECIPES.md for the reasons behind each change.

ServerEvents.recipes(event => {
  // PneumaticCraft talks to Flux through two machines; both get the one basic circuit
  // the pack has, so the FE side of PneumaticCraft starts with Create and Mekanism.
  event.remove({ id: 'pneumaticcraft:flux_compressor' })
  event.shaped('pneumaticcraft:flux_compressor', [
    'GCP',
    'FRT',
    'GQP'
  ], {
    G: '#c:dusts/redstone',
    C: 'pneumaticcraft:compressed_iron_gear',
    P: 'mekanism:basic_control_circuit',
    F: '#c:storage_blocks/redstone',
    R: 'pneumaticcraft:turbine_rotor',
    T: 'pneumaticcraft:advanced_pressure_tube',
    Q: 'minecraft:blast_furnace'
  }).id('kronwerke:added/flux_compressor')
  event.remove({ id: 'pneumaticcraft:pneumatic_dynamo' })
  event.shaped('pneumaticcraft:pneumatic_dynamo', [
    ' T ',
    'GIG',
    'IPI'
  ], {
    T: 'pneumaticcraft:advanced_pressure_tube',
    G: 'pneumaticcraft:compressed_iron_gear',
    I: '#c:ingots/compressed_iron',
    P: 'mekanism:basic_control_circuit'
  }).id('kronwerke:added/pneumatic_dynamo')

  // A drone is a flying machine, so it carries a precision mechanism like the AE2 assembler.
  event.remove({ id: 'pneumaticcraft:drone' })
  event.shaped('pneumaticcraft:drone', [
    ' B ',
    'BPB',
    ' M '
  ], {
    B: 'pneumaticcraft:turbine_rotor',
    P: 'pneumaticcraft:printed_circuit_board',
    M: 'create:precision_mechanism'
  }).id('kronwerke:added/drone')

  // Flux Networks: the core takes a source gem instead of the eye of ender, so wireless
  // power is where magic meets tech; the controller gets the advanced circuit of its stage.
  event.remove({ id: 'fluxnetworks:flux_core' })
  event.shaped('fluxnetworks:flux_core', [
    'fof',
    'oso',
    'fof'
  ], {
    f: 'fluxnetworks:flux_dust',
    o: 'minecraft:obsidian',
    s: 'ars_nouveau:source_gem'
  }).id('kronwerke:added/flux_core')
  event.remove({ id: 'fluxnetworks:flux_controller' })
  event.shaped('fluxnetworks:flux_controller', [
    'bcb',
    'fAf',
    'bbb'
  ], {
    b: 'fluxnetworks:flux_block',
    c: 'fluxnetworks:flux_core',
    f: 'fluxnetworks:flux_dust',
    A: 'mekanism:advanced_control_circuit'
  }).id('kronwerke:added/flux_controller')

  // Hostile Neural Networks: the simulation chamber runs on a source gem block, the loot
  // fabricator needs an engineering processor, so both pillars feed the mob farm that
  // replaces mob farms.
  event.remove({ id: 'hostilenetworks:sim_chamber' })
  event.shaped('hostilenetworks:sim_chamber', [
    ' G ',
    'EOE',
    'MCM'
  ], {
    G: '#c:glass_panes',
    E: 'minecraft:ender_pearl',
    O: 'ars_nouveau:source_gem_block',
    M: '#c:gems/lapis',
    C: 'minecraft:comparator'
  }).id('kronwerke:added/sim_chamber')
  event.remove({ id: 'hostilenetworks:loot_fabricator' })
  event.shaped('hostilenetworks:loot_fabricator', [
    ' I ',
    'GOG',
    'NPN'
  ], {
    I: '#c:ingots/netherite',
    G: '#c:gems/diamond',
    O: '#c:obsidians',
    N: '#c:ingots/gold',
    P: 'ae2:engineering_processor'
  }).id('kronwerke:added/loot_fabricator')
})
