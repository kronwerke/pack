// The obelisk's intake: the block machines feed the obelisk through. Cheap on purpose,
// every player should have one by the end of the first evening.
ServerEvents.recipes(event => {
  event.shaped('kronwerke:obelisk_intake', [
    ' H ',
    'DAD',
    'DDD'
  ], {
    H: 'minecraft:hopper',
    D: 'minecraft:cobbled_deepslate',
    A: 'create:andesite_alloy'
  }).id('kronwerke:obelisk_intake')
})
