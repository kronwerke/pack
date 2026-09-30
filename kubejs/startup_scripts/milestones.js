// The milestone items of the community goals. Each one is crafted from the best of its stage,
// tech and magic together, and goes into the obelisk. See docs/STAGES.md.

StartupEvents.registry('item', event => {
  let milestone = (id, rarity) => event.create('kronwerke:' + id)
    .maxStackSize(16)
    .rarity(rarity)
    .texture('kronwerke:item/' + id)
    .tooltip(Text.translate('item.kronwerke.' + id + '.tooltip').gray())

  milestone('stone_gearbox', 'common')
  milestone('source_keystone', 'common')
  milestone('brass_heart', 'uncommon')
  milestone('rune_core', 'uncommon')
  milestone('steel_core', 'rare')
  milestone('elven_star', 'rare').glow(true)
})
