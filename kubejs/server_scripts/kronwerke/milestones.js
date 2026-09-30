// Milestone items for the community goals. Crafting only: Chapters refuses to craft an item
// of a stage that is not open yet, so nobody can build them ahead of time.

ServerEvents.recipes(event => {
  // Stage 1: Create's andesite age, with infused iron from the Nature's Aura altar
  event.shaped('kronwerke:stone_gearbox', [
    'ALA',
    'PIM',
    'AWA'
  ], {
    A: 'create:andesite_casing',
    L: 'create:large_cogwheel',
    P: 'create:mechanical_press',
    I: 'naturesaura:infused_iron',
    M: 'create:millstone',
    W: 'create:water_wheel'
  }).id('kronwerke:milestones/stone_gearbox')

  // Stage 1: source from Ars Nouveau, mana diamonds from Botania, gold leaf from Nature's Aura
  event.shaped('kronwerke:source_keystone', [
    'SJS',
    'DAD',
    'SGS'
  ], {
    S: 'ars_nouveau:source_gem_block',
    J: 'ars_nouveau:source_jar',
    D: 'botania:mana_diamond',
    A: 'create:andesite_alloy',
    G: 'naturesaura:gold_leaf'
  }).id('kronwerke:milestones/source_keystone')

  // Stage 2: the brass tier around a blaze burner, with a fire rune for the flame
  event.shaped('kronwerke:brass_heart', [
    'CPC',
    'ERE',
    'CBC'
  ], {
    C: 'create:brass_casing',
    P: 'create:precision_mechanism',
    E: 'create:electron_tube',
    R: 'botania:rune_of_fire',
    B: 'create:blaze_burner'
  }).id('kronwerke:milestones/brass_heart')

  // Stage 2: the four element runes around terrasteel, held together with brass
  event.shaped('kronwerke:rune_core', [
    'WPA',
    'BTB',
    'FPE'
  ], {
    W: 'botania:rune_of_water',
    A: 'botania:rune_of_air',
    F: 'botania:rune_of_fire',
    E: 'botania:rune_of_earth',
    P: 'botania:mana_pearl',
    B: '#c:plates/brass',
    T: 'botania:terrasteel_ingot'
  }).id('kronwerke:milestones/rune_core')

  // Stage 3: Mekanism circuits, AE2 processors and IE's heavy engineering, with elven metal
  event.shaped('kronwerke:steel_core', [
    'HCH',
    'PSP',
    'HEH'
  ], {
    H: 'immersiveengineering:heavy_engineering',
    C: 'mekanism:advanced_control_circuit',
    P: 'ae2:engineering_processor',
    S: 'mekanism:steel_casing',
    E: 'botania:elementium_ingot'
  }).id('kronwerke:milestones/steel_core')

  // Stage 3: Alfheim's dragonstone and pixie dust, afrit essence from Occultism, reinforced alloy
  event.shaped('kronwerke:elven_star', [
    'DXD',
    'ARA',
    'DXD'
  ], {
    D: 'botania:dragonstone',
    X: 'botania:pixie_dust',
    A: 'occultism:afrit_essence',
    R: 'mekanism:alloy_reinforced'
  }).id('kronwerke:milestones/elven_star')
})
