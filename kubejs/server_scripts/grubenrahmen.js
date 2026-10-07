// The Grubenrahmen, the frame of the portal to the mining world (Kronwerke Core). Stage 1,
// both pillars: Create's andesite casings, Nature's Aura's infused iron, an Ars Nouveau
// source gem. Ten frames and a source gem open a portal.
ServerEvents.recipes(event => {
  event.shaped('2x kronwerke:grubenrahmen', [
    'CIC',
    'IGI',
    'CIC'
  ], {
    C: 'create:andesite_casing',
    I: 'naturesaura:infused_iron',
    G: 'ars_nouveau:source_gem'
  }).id('kronwerke:grubenrahmen')
})
