// Magic family: Botania, Nature's Aura and Occultism lean on each other and on brass.
// See the Magic table in docs/RECIPES.md.

ServerEvents.recipes(event => {
  // Manasteel: no more dipping plain iron into a pool. The first ingots come from a
  // ritual of the forest, the mass route is a pool fed with infused iron from the altar.
  event.remove({ id: 'botania:mana_infusion/manasteel_ingot' })
  event.remove({ id: 'mysticalagriculture:essence/botania/manasteel_ingot' })

  event.custom({
    type: 'naturesaura:tree_ritual',
    ingredients: [
      { item: 'naturesaura:infused_iron' },
      { item: 'naturesaura:infused_iron' },
      { item: 'naturesaura:infused_iron' },
      { item: 'naturesaura:infused_iron' },
      { item: 'botania:livingwood_twig' },
      { item: 'botania:livingwood_twig' },
      { item: 'botania:mana_diamond' },
      { item: 'naturesaura:gold_leaf' }
    ],
    sapling: { item: 'minecraft:oak_sapling' },
    output: { id: 'botania:manasteel_ingot', count: 4 },
    time: 300
  }).id('kronwerke:magic/manasteel_ritual')

  event.custom({
    type: 'botania:mana_infusion',
    input: { item: 'naturesaura:infused_iron' },
    mana: 3000,
    output: { id: 'botania:manasteel_ingot', count: 1 }
  }).id('kronwerke:magic/manasteel_from_infused_iron')

  // Manasteel block: only from ingots now, the iron block pool route goes.
  event.remove({ id: 'botania:mana_infusion/manasteel_block' })

  // Mana pearl: the pool needs a brass casing underneath, so the pearl waits for brass.
  event.remove({ id: 'botania:mana_infusion/mana_pearl' })
  event.custom({
    type: 'botania:mana_infusion',
    catalyst: { type: 'botania:block', block: 'create:brass_casing' },
    input: { item: 'minecraft:ender_pearl' },
    mana: 6000,
    output: { id: 'botania:mana_pearl', count: 1 }
  }).id('kronwerke:magic/mana_pearl')

  // Spirit attuned gem: spirit fire only, the Ars Ocultas apparatus shortcut goes.
  event.remove({ id: 'ars_ocultas:spirit_attuned_gem' })

  // Runic altar: a brass ingot in place of the middle livingrock on top.
  event.remove({ id: 'botania:runic_altar' })
  event.shaped('botania:runic_altar', [
    'SBS',
    'SPS'
  ], {
    S: 'botania:livingrock',
    B: '#c:ingots/brass',
    P: '#botania:mana_gems'
  }).id('kronwerke:magic/runic_altar')
})
