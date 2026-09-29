// The Ultimate Mining Dimension ships its only recipe in data/.../recipes/, a folder
// Minecraft 1.21 no longer reads, and that recipe needs a netherite ingot, which is
// stage 2. This one works in stage 1: two diamonds, a gold block, two sticks.
ServerEvents.recipes(event => {
  event.shaped('ultimate_mining_dimension:ultimate_mining_dimension', [
    'DGD',
    ' S ',
    ' S '
  ], {
    D: 'minecraft:diamond',
    G: 'minecraft:gold_block',
    S: 'minecraft:stick'
  }).id('kronwerke:mining_dimension_pickaxe')
})
