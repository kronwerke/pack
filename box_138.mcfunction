# 138 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 307 62 332
fill -4 64 307 40 91 332 minecraft:air
fill 41 64 307 62 91 332 minecraft:air
fill -4 60 307 62 62 332 minecraft:stone
fill -4 63 307 62 63 332 minecraft:light_gray_concrete
fill 0 64 313 62 79 313 minecraft:light_gray_concrete
fill 0 64 313 0 79 326 minecraft:light_gray_concrete
setblock 1 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 313 11 79 326 minecraft:light_gray_concrete
setblock 4 64 317 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 317 up create:creative_blaze_cake
setblock 4 64 318 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 318 up create:creative_blaze_cake
setblock 5 64 317 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 317 up create:creative_blaze_cake
setblock 5 64 318 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 318 up create:creative_blaze_cake
fill 4 65 317 5 67 318 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 320 create:shaft[axis=x]
setblock 4 66 319 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 313 21 79 326 minecraft:light_gray_concrete
setblock 14 64 316 minecraft:stone_bricks
setblock 14 64 317 minecraft:stone_bricks
setblock 14 64 318 minecraft:stone_bricks
setblock 14 64 319 minecraft:stone_bricks
setblock 14 64 320 minecraft:glass
setblock 15 64 316 minecraft:stone_bricks
setblock 15 64 317 minecraft:lava
setblock 15 64 318 minecraft:lava
setblock 15 64 319 minecraft:lava
setblock 15 64 320 minecraft:glass
setblock 16 64 316 minecraft:stone_bricks
setblock 16 64 317 minecraft:lava
setblock 16 64 318 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 319 minecraft:glass
setblock 16 64 320 minecraft:glass
setblock 17 64 316 minecraft:stone_bricks
setblock 17 64 317 minecraft:lava
setblock 17 64 318 minecraft:lava
setblock 17 64 319 minecraft:lava
setblock 17 64 320 minecraft:glass
setblock 18 64 316 minecraft:stone_bricks
setblock 18 64 317 minecraft:stone_bricks
setblock 18 64 318 minecraft:stone_bricks
setblock 18 64 319 minecraft:stone_bricks
setblock 18 64 320 minecraft:glass
setblock 22 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 313 31 79 326 minecraft:light_gray_concrete
setblock 26 64 318 createaddition:alternator[facing=east]
setblock 25 64 318 create:shaft[axis=x]
setblock 24 64 318 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 318 create:andesite_casing
setblock 24 64 319 create:andesite_casing
setblock 24 64 317 create:andesite_casing
setblock 24 65 318 create:andesite_casing
setblock 32 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 313 45 79 326 minecraft:light_gray_concrete
kw testworld use 35 63 318 up mekmm:large_heat_generator
kw testworld use 41 63 318 up mekmm:large_gas_burning_generator
setblock 46 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 313 57 79 326 minecraft:light_gray_concrete
setblock 48 64 317 nuclearcraft:solar_panel_basic
setblock 50 64 317 nuclearcraft:solar_panel_advanced
setblock 52 64 317 nuclearcraft:solar_panel_du
setblock 54 64 317 nuclearcraft:solar_panel_elite
setblock 48 64 319 nuclearcraft:uranium_rtg
setblock 50 64 319 nuclearcraft:americium_rtg
setblock 52 64 319 nuclearcraft:plutonium_rtg
setblock 54 64 319 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
