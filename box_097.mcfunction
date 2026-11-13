# 097 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 273 62 298
fill -4 64 273 40 91 298 minecraft:air
fill 41 64 273 62 91 298 minecraft:air
fill -4 60 273 62 62 298 minecraft:stone
fill -4 63 273 62 63 298 minecraft:light_gray_concrete
fill 0 64 279 62 79 279 minecraft:light_gray_concrete
fill 0 64 279 0 79 292 minecraft:light_gray_concrete
setblock 1 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 279 11 79 292 minecraft:light_gray_concrete
setblock 4 64 283 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 283 up create:creative_blaze_cake
setblock 4 64 284 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 284 up create:creative_blaze_cake
setblock 5 64 283 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 283 up create:creative_blaze_cake
setblock 5 64 284 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 284 up create:creative_blaze_cake
fill 4 65 283 5 67 284 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 286 create:shaft[axis=x]
setblock 4 66 285 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 279 21 79 292 minecraft:light_gray_concrete
setblock 14 64 282 minecraft:stone_bricks
setblock 14 64 283 minecraft:stone_bricks
setblock 14 64 284 minecraft:stone_bricks
setblock 14 64 285 minecraft:stone_bricks
setblock 14 64 286 minecraft:glass
setblock 15 64 282 minecraft:stone_bricks
setblock 15 64 283 minecraft:lava
setblock 15 64 284 minecraft:lava
setblock 15 64 285 minecraft:lava
setblock 15 64 286 minecraft:glass
setblock 16 64 282 minecraft:stone_bricks
setblock 16 64 283 minecraft:lava
setblock 16 64 284 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 285 minecraft:glass
setblock 16 64 286 minecraft:glass
setblock 17 64 282 minecraft:stone_bricks
setblock 17 64 283 minecraft:lava
setblock 17 64 284 minecraft:lava
setblock 17 64 285 minecraft:lava
setblock 17 64 286 minecraft:glass
setblock 18 64 282 minecraft:stone_bricks
setblock 18 64 283 minecraft:stone_bricks
setblock 18 64 284 minecraft:stone_bricks
setblock 18 64 285 minecraft:stone_bricks
setblock 18 64 286 minecraft:glass
setblock 22 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 279 31 79 292 minecraft:light_gray_concrete
setblock 26 64 284 createaddition:alternator[facing=east]
setblock 25 64 284 create:shaft[axis=x]
setblock 24 64 284 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 284 create:andesite_casing
setblock 24 64 285 create:andesite_casing
setblock 24 64 283 create:andesite_casing
setblock 24 65 284 create:andesite_casing
setblock 32 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 279 45 79 292 minecraft:light_gray_concrete
kw testworld use 35 63 285 up mekmm:large_heat_generator
kw testworld use 41 63 285 up mekmm:large_wind_generator
setblock 46 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 279 57 79 292 minecraft:light_gray_concrete
setblock 48 64 283 nuclearcraft:solar_panel_basic
setblock 50 64 283 nuclearcraft:solar_panel_advanced
setblock 52 64 283 nuclearcraft:solar_panel_du
setblock 54 64 283 nuclearcraft:solar_panel_elite
setblock 48 64 285 nuclearcraft:uranium_rtg
setblock 50 64 285 nuclearcraft:americium_rtg
setblock 52 64 285 nuclearcraft:plutonium_rtg
setblock 54 64 285 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
