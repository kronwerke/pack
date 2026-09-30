// Create Enchantment Industry names the experience fluids of Ender IO and Reliquary with ids
// those mods do not use, so NeoForge logs an error for each on every data load. An alias from
// the wrong id to the real fluid fixes the lookup, and the XP juice of both mods counts in
// the enchanting machines as intended.
StartupEvents.postInit(event => {
  let registries = Java.loadClass('net.minecraft.core.registries.BuiltInRegistries')
  let location = Java.loadClass('net.minecraft.resources.ResourceLocation')
  let aliases = {
    'enderio:xpjuice': 'enderio:fluid_xp_juice_still',
    'reliquary:xp_juice_still': 'reliquary:xp_still'
  }
  Object.keys(aliases).forEach(from => {
    registries.FLUID.addAlias(location.parse(from), location.parse(aliases[from]))
  })
})
