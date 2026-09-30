// Create family: brass, the precision mechanism and andesite alloy.
// See docs/RECIPES.md, table "Create".

ServerEvents.recipes(event => {
  // Brass ingot, the stage 2 milestone. Every other route goes (Oritech foundry,
  // Productive Metalworks casting and its copper plus zinc alloying), so brass always
  // comes out of a mixer. The first ingots cost blaze powder; a superheated line
  // fed with blaze cakes makes two per pair without it. Nugget and block crafting stay,
  // and melting brass items back into molten brass stays too.
  event.remove({ output: 'create:brass_ingot', not: [
    { id: 'create:crafting/materials/brass_ingot_from_compacting' },
    { id: 'create:crafting/materials/brass_ingot_from_decompacting' }
  ] })
  event.remove({ id: 'productivemetalworks:alloying/molten_brass' })
  // The output filter does not see Oritech's result field, so this one goes by id.
  event.remove({ id: 'oritech:foundry/alloy/compat/create/brass' })

  event.custom({
    type: 'create:mixing',
    heat_requirement: 'heated',
    ingredients: [
      { tag: 'c:ingots/copper' },
      { tag: 'c:ingots/copper' },
      { tag: 'c:ingots/zinc' },
      { item: 'minecraft:blaze_powder' }
    ],
    results: [{ id: 'create:brass_ingot', count: 1 }]
  }).id('kronwerke:create/brass_ingot_heated')

  event.custom({
    type: 'create:mixing',
    heat_requirement: 'superheated',
    ingredients: [
      { tag: 'c:ingots/copper' },
      { tag: 'c:ingots/copper' },
      { tag: 'c:ingots/zinc' }
    ],
    results: [{ id: 'create:brass_ingot', count: 2 }]
  }).id('kronwerke:create/brass_ingot_superheated')

  // Precision mechanism: built on a brass sheet now, and every loop eats an electron
  // tube. Scrap is brass nuggets and cogwheels.
  event.remove({ output: 'create:precision_mechanism' })
  let kwPrecisionStep = (type, extra) => ({
    type: type,
    ingredients: [{ item: 'create:incomplete_precision_mechanism' }].concat(extra),
    results: [{ id: 'create:incomplete_precision_mechanism' }]
  })
  event.custom({
    type: 'create:sequenced_assembly',
    ingredient: { tag: 'c:plates/brass' },
    loops: 5,
    results: [
      { id: 'create:precision_mechanism', chance: 60.0 },
      { id: 'create:brass_nugget', chance: 25.0 },
      { id: 'create:cogwheel', chance: 15.0 }
    ],
    sequence: [
      kwPrecisionStep('create:deploying', [{ item: 'create:cogwheel' }]),
      kwPrecisionStep('create:deploying', [{ item: 'create:electron_tube' }]),
      kwPrecisionStep('create:deploying', [{ tag: 'c:nuggets/iron' }]),
      kwPrecisionStep('create:pressing', [])
    ],
    transitional_item: { id: 'create:incomplete_precision_mechanism' }
  }).id('kronwerke:create/precision_mechanism')

  // Mechanical crafter: autocrafting with Create needs the milestone, so the precision
  // mechanism takes the place of the electron tube (it holds five of them anyway).
  event.remove({ id: 'create:crafting/kinetics/mechanical_crafter' })
  event.shaped('3x create:mechanical_crafter', [
    'P',
    'C',
    'R'
  ], {
    P: 'create:precision_mechanism',
    C: 'create:brass_casing',
    R: 'minecraft:crafting_table'
  }).id('kronwerke:create/mechanical_crafter')

  // Andesite alloy: hand crafting stays at one per craft, a mixer now gives two.
  event.remove({ id: 'create:mixing/andesite_alloy' })
  event.remove({ id: 'create:mixing/andesite_alloy_from_zinc' })
  event.custom({
    type: 'create:mixing',
    ingredients: [{ item: 'minecraft:andesite' }, { tag: 'c:nuggets/iron' }],
    results: [{ id: 'create:andesite_alloy', count: 2 }]
  }).id('kronwerke:create/andesite_alloy_mixing')
  event.custom({
    type: 'create:mixing',
    ingredients: [{ item: 'minecraft:andesite' }, { tag: 'c:nuggets/zinc' }],
    results: [{ id: 'create:andesite_alloy', count: 2 }]
  }).id('kronwerke:create/andesite_alloy_mixing_from_zinc')
})
