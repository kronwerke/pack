# 142 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 313 62 338
fill -4 64 313 40 91 338 minecraft:air
fill 41 64 313 62 91 338 minecraft:air
fill -4 60 313 62 62 338 minecraft:stone
fill -4 63 313 62 63 338 minecraft:light_gray_concrete
fill 0 64 319 62 79 319 minecraft:light_gray_concrete
fill 0 64 319 0 79 332 minecraft:light_gray_concrete
setblock 1 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 319 11 79 332 minecraft:light_gray_concrete
setblock 4 64 323 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 323 up create:creative_blaze_cake
setblock 4 64 324 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 324 up create:creative_blaze_cake
setblock 5 64 323 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 323 up create:creative_blaze_cake
setblock 5 64 324 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 324 up create:creative_blaze_cake
fill 4 65 323 5 67 324 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 326 create:shaft[axis=x]
setblock 4 66 325 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 319 21 79 332 minecraft:light_gray_concrete
setblock 14 64 322 minecraft:stone_bricks
setblock 14 64 323 minecraft:stone_bricks
setblock 14 64 324 minecraft:stone_bricks
setblock 14 64 325 minecraft:stone_bricks
setblock 14 64 326 minecraft:glass
setblock 15 64 322 minecraft:stone_bricks
setblock 15 64 323 minecraft:lava
setblock 15 64 324 minecraft:lava
setblock 15 64 325 minecraft:lava
setblock 15 64 326 minecraft:glass
setblock 16 64 322 minecraft:stone_bricks
setblock 16 64 323 minecraft:lava
setblock 16 64 324 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 325 minecraft:glass
setblock 16 64 326 minecraft:glass
setblock 17 64 322 minecraft:stone_bricks
setblock 17 64 323 minecraft:lava
setblock 17 64 324 minecraft:lava
setblock 17 64 325 minecraft:lava
setblock 17 64 326 minecraft:glass
setblock 18 64 322 minecraft:stone_bricks
setblock 18 64 323 minecraft:stone_bricks
setblock 18 64 324 minecraft:stone_bricks
setblock 18 64 325 minecraft:stone_bricks
setblock 18 64 326 minecraft:glass
setblock 22 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 319 31 79 332 minecraft:light_gray_concrete
setblock 26 64 324 createaddition:alternator[facing=east]
setblock 25 64 324 create:shaft[axis=x]
setblock 24 64 324 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 324 create:andesite_casing
setblock 24 64 325 create:andesite_casing
setblock 24 64 323 create:andesite_casing
setblock 24 65 324 create:andesite_casing
setblock 32 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 319 45 79 332 minecraft:light_gray_concrete
kw testworld use 35 63 324 up mekmm:large_heat_generator
kw testworld use 41 63 324 up mekmm:large_gas_burning_generator
setblock 46 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 319 57 79 332 minecraft:light_gray_concrete
setblock 48 64 323 nuclearcraft:solar_panel_basic
setblock 50 64 323 nuclearcraft:solar_panel_advanced
setblock 52 64 323 nuclearcraft:solar_panel_du
setblock 54 64 323 nuclearcraft:solar_panel_elite
setblock 48 64 325 nuclearcraft:uranium_rtg
setblock 50 64 325 nuclearcraft:americium_rtg
setblock 52 64 325 nuclearcraft:plutonium_rtg
setblock 54 64 325 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
