// Tech and magic tied together: a few key machines need something from the other side,
// so a server that only builds machines, or only casts spells, gets stuck. The table in
// docs/STAGES.md lists them all; this file holds the ones for stage 2.

ServerEvents.recipes(event => {
  // Brass needs a mage: the blaze burner is what makes brass in the mixer, and its
  // shell now needs two Source Gems from the Ars Nouveau imbuement chamber.
  event.remove({ id: 'create:crafting/kinetics/empty_blaze_burner' })
  event.shaped('create:empty_blaze_burner', [
    'GIG',
    'INI',
    ' I '
  ], {
    G: 'ars_nouveau:source_gem',
    I: '#c:plates/iron',
    N: '#c:netherracks'
  }).id('kronwerke:empty_blaze_burner')

  // The first Mekanism machine needs mana: manasteel from a Botania mana pool in
  // place of the bottom iron.
  event.remove({ id: 'mekanism:metallurgic_infuser' })
  event.shaped('mekanism:metallurgic_infuser', [
    'I#I',
    'ROR',
    'M#M'
  ], {
    I: '#c:ingots/iron',
    '#': 'minecraft:furnace',
    R: '#c:dusts/redstone',
    O: '#c:ingots/osmium',
    M: '#c:ingots/manasteel'
  }).id('kronwerke:metallurgic_infuser')

  // Terrasteel needs an engineer: the terrestrial agglomeration plate takes two brass
  // casings from Create in place of two of its lapis blocks.
  event.remove({ id: 'botania:terrestrial_agglomeration_plate' })
  event.shaped('botania:terrestrial_agglomeration_plate', [
    'CLC',
    'WMF',
    'XYZ'
  ], {
    C: 'create:brass_casing',
    L: '#c:storage_blocks/lapis',
    W: 'botania:rune_of_water',
    F: 'botania:rune_of_fire',
    X: 'botania:rune_of_earth',
    Y: 'botania:rune_of_mana',
    Z: 'botania:rune_of_air',
    M: 'botania:mana_quartz_block'
  }).id('kronwerke:terrestrial_agglomeration_plate')
})
