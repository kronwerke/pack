# 196 list_power/steam_engine, mek_heat, ie_thermo, alternator, powah_reactor, flux, mekmm_large, nc_passive, draconic_core
fill 0 63 358 99 63 377 minecraft:light_gray_concrete
fill 0 64 358 99 71 358 minecraft:light_gray_concrete
fill 0 64 358 0 71 377 minecraft:light_gray_concrete
setblock 1 64 376 minecraft:air
setblock 1 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 376 minecraft:air
setblock 2 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
place template create:gametest/fluids/steam_engine 2 64 360 none
setblock 13 64 376 minecraft:air
setblock 13 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 14 64 376 minecraft:air
setblock 14 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
setblock 14 64 362 minecraft:polished_andesite
summon item_frame 14 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:lava_bucket",count:1}}
setblock 23 64 376 minecraft:air
setblock 23 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.3"}','{"text": "list_power"}','{"text": "ie_thermo"}','{"text": ""}']}}
setblock 24 64 376 minecraft:air
setblock 24 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann Lava"}','{"text": "gegen Wasser"}','{"text": ""}','{"text": ""}']}}
setblock 24 64 362 minecraft:lightning_rod
setblock 33 64 376 minecraft:air
setblock 33 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.4"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 34 64 376 minecraft:air
setblock 34 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
setblock 34 64 362 create:cogwheel
setblock 43 64 376 minecraft:air
setblock 43 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.5"}','{"text": "list_power"}','{"text": "powah_reactor"}','{"text": ""}']}}
setblock 44 64 376 minecraft:air
setblock 44 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den"}','{"text": "Powah-Reaktor"}','{"text": ""}','{"text": ""}']}}
setblock 44 64 362 minecraft:polished_andesite
summon item_frame 44 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:water_bucket",count:1}}
setblock 53 64 376 minecraft:air
setblock 53 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.6"}','{"text": "list_power"}','{"text": "flux"}','{"text": ""}']}}
setblock 54 64 376 minecraft:air
setblock 54 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Flux-Netzwerk"}','{"text": ""}','{"text": ""}']}}
setblock 54 64 362 minecraft:polished_andesite
summon item_frame 54 64 363 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"ars_nouveau:source_gem",count:1}}
setblock 63 64 376 minecraft:air
setblock 63 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.7"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 64 64 376 minecraft:air
setblock 64 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
setblock 64 64 362 create:encased_fan
setblock 73 64 376 minecraft:air
setblock 73 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.8"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 74 64 376 minecraft:air
setblock 74 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
setblock 74 64 362 minecraft:daylight_detector
setblock 83 64 376 minecraft:air
setblock 83 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.9"}','{"text": "list_power"}','{"text": "draconic_core"}','{"text": ""}']}}
setblock 84 64 376 minecraft:air
setblock 84 64 376 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Build Guide im"}','{"text": "Kern zeigt die"}','{"text": "Hülle"}','{"text": ""}']}}
setblock 90 66 366 draconicevolution:energy_core
setblock 90 66 360 draconicevolution:energy_core_stabilizer
setblock 90 66 372 draconicevolution:energy_core_stabilizer
setblock 84 66 366 draconicevolution:energy_core_stabilizer
setblock 96 66 366 draconicevolution:energy_core_stabilizer
setblock 97 64 373 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"draconicevolution:draconium_block",count:16},{Slot:1b,id:"minecraft:redstone_block",count:16}]}
