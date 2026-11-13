# 147 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 317 62 342
fill -4 64 317 40 91 342 minecraft:air
fill 41 64 317 62 91 342 minecraft:air
fill -4 60 317 62 62 342 minecraft:stone
fill -4 63 317 62 63 342 minecraft:light_gray_concrete
fill 0 64 323 62 79 323 minecraft:light_gray_concrete
fill 0 64 323 0 79 336 minecraft:light_gray_concrete
setblock 1 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 323 11 79 336 minecraft:light_gray_concrete
setblock 4 64 327 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 327 up create:creative_blaze_cake
setblock 4 64 328 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 328 up create:creative_blaze_cake
setblock 5 64 327 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 327 up create:creative_blaze_cake
setblock 5 64 328 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 328 up create:creative_blaze_cake
fill 4 65 327 5 67 328 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 330 create:shaft[axis=x]
setblock 4 66 329 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 323 21 79 336 minecraft:light_gray_concrete
setblock 14 64 326 minecraft:stone_bricks
setblock 14 64 327 minecraft:stone_bricks
setblock 14 64 328 minecraft:stone_bricks
setblock 14 64 329 minecraft:stone_bricks
setblock 14 64 330 minecraft:glass
setblock 15 64 326 minecraft:stone_bricks
setblock 15 64 327 minecraft:lava
setblock 15 64 328 minecraft:lava
setblock 15 64 329 minecraft:lava
setblock 15 64 330 minecraft:glass
setblock 16 64 326 minecraft:stone_bricks
setblock 16 64 327 minecraft:lava
setblock 16 64 328 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 329 minecraft:glass
setblock 16 64 330 minecraft:glass
setblock 17 64 326 minecraft:stone_bricks
setblock 17 64 327 minecraft:lava
setblock 17 64 328 minecraft:lava
setblock 17 64 329 minecraft:lava
setblock 17 64 330 minecraft:glass
setblock 18 64 326 minecraft:stone_bricks
setblock 18 64 327 minecraft:stone_bricks
setblock 18 64 328 minecraft:stone_bricks
setblock 18 64 329 minecraft:stone_bricks
setblock 18 64 330 minecraft:glass
setblock 22 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 323 31 79 336 minecraft:light_gray_concrete
setblock 26 64 328 createaddition:alternator[facing=east]
setblock 25 64 328 create:shaft[axis=x]
setblock 24 64 328 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 328 create:andesite_casing
setblock 24 64 329 create:andesite_casing
setblock 24 64 327 create:andesite_casing
setblock 24 65 328 create:andesite_casing
setblock 32 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 323 45 79 336 minecraft:light_gray_concrete
kw testworld use 35 63 328 up mekmm:large_heat_generator
kw testworld use 41 63 328 up mekmm:large_gas_burning_generator
setblock 46 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 323 57 79 336 minecraft:light_gray_concrete
setblock 48 64 327 nuclearcraft:solar_panel_basic
setblock 50 64 327 nuclearcraft:solar_panel_advanced
setblock 52 64 327 nuclearcraft:solar_panel_du
setblock 54 64 327 nuclearcraft:solar_panel_elite
setblock 48 64 329 nuclearcraft:uranium_rtg
setblock 50 64 329 nuclearcraft:americium_rtg
setblock 52 64 329 nuclearcraft:plutonium_rtg
setblock 54 64 329 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
