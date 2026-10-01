// The mods added in 0.8.0: PneumaticCraft, Flux Networks, Hostile Neural Networks,
// Productive Trees, Deeper and Darker, and the Productive Bees shortcut around brass.
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
  // Four cores per craft, as in the mod's own recipe.
  event.shaped('4x fluxnetworks:flux_core', [
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

  // Productive Trees ships its pollen sifter recipe only when Productive Bees is absent.
  // Breeding by hand should work without bees, so the sifter gets its recipe back.
  event.shaped('productivetrees:pollen_sifter', [
    '#S#',
    'IBI',
    '###'
  ], {
    '#': '#minecraft:planks',
    S: 'minecraft:sticky_piston',
    I: '#c:ingots/iron',
    B: 'minecraft:brush'
  }).id('kronwerke:added/pollen_sifter')

  // Reinforced deepslate frames the Otherside portal. Vanilla never drops it and the only
  // recipe in the pack is an Occultism ritual that eats a warden per block. Steel, deepslate
  // and an echo shard make two, so the stage 3 dimension is reachable in stage 3.
  event.shaped('2x minecraft:reinforced_deepslate', [
    'DSD',
    'SES',
    'DSD'
  ], {
    D: 'minecraft:deepslate',
    S: '#c:ingots/steel',
    E: 'minecraft:echo_shard'
  }).id('kronwerke:added/reinforced_deepslate')

  // The brass bee would hand out the stage 2 milestone metal for free once a single bee
  // exists. Its comb gives nothing in the centrifuge; the bee itself stays as a curiosity.
  event.remove({ id: 'productivebees:centrifuge/alloys/honeycomb_brass' })

  // Cataclysm's structure eyes all need an eye of ender, which needs blaze powder from the
  // Nether. The overworld bosses are meant for stage 1 and 2, so each overworld eye gets a
  // second recipe: a source gem where the eye of ender sat, and an ender pearl in one slot.
  const P = 'minecraft:ender_pearl'
  const G = 'ars_nouveau:source_gem'
  event.shaped('cataclysm:desert_eye', ['gCE', 'DSG', 'PCB'], {
    g: 'minecraft:gold_ingot', C: 'minecraft:chiseled_sandstone', E: 'minecraft:emerald',
    D: 'minecraft:dead_bush', S: G, G: 'minecraft:cactus', P: P, B: 'minecraft:bone'
  }).id('kronwerke:added/cataclysm_desert_eye')
  event.shaped('cataclysm:cursed_eye', ['gBg', 'MSM', 'gPg'], {
    g: 'minecraft:gold_ingot', B: 'minecraft:bone', M: 'minecraft:phantom_membrane', S: G, P: P
  }).id('kronwerke:added/cataclysm_cursed_eye')
  event.shaped('cataclysm:abyss_eye', ['#P#', 'OSO', '#O#'], {
    '#': 'minecraft:crying_obsidian', O: 'minecraft:obsidian', S: G, P: P
  }).id('kronwerke:added/cataclysm_abyss_eye')
  event.shaped('cataclysm:mech_eye', ['#P#', 'iSi', '#i#'], {
    '#': 'minecraft:redstone_block', i: 'minecraft:iron_ingot', S: G, P: P
  }).id('kronwerke:added/cataclysm_mech_eye')
  event.shaped('cataclysm:storm_eye', ['#L#', 'DSD', 'CPC'], {
    '#': 'minecraft:prismarine_shard', L: 'minecraft:lightning_rod', D: 'minecraft:diamond',
    S: G, C: 'minecraft:prismarine_crystals', P: P
  }).id('kronwerke:added/cataclysm_storm_eye')
})
