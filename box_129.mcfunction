# 129 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 277 62 302
fill -4 64 277 40 91 302 minecraft:air
fill 41 64 277 62 91 302 minecraft:air
fill -4 60 277 62 62 302 minecraft:stone
fill -4 63 277 62 63 302 minecraft:light_gray_concrete
fill 0 64 283 62 79 283 minecraft:light_gray_concrete
fill 0 64 283 0 79 296 minecraft:light_gray_concrete
setblock 1 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 283 11 79 296 minecraft:light_gray_concrete
setblock 4 64 287 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 287 up create:creative_blaze_cake
setblock 4 64 288 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 288 up create:creative_blaze_cake
setblock 5 64 287 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 287 up create:creative_blaze_cake
setblock 5 64 288 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 288 up create:creative_blaze_cake
fill 4 65 287 5 67 288 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 290 create:shaft[axis=x]
setblock 4 66 289 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 283 21 79 296 minecraft:light_gray_concrete
setblock 14 64 286 minecraft:stone_bricks
setblock 14 64 287 minecraft:stone_bricks
setblock 14 64 288 minecraft:stone_bricks
setblock 14 64 289 minecraft:stone_bricks
setblock 14 64 290 minecraft:glass
setblock 15 64 286 minecraft:stone_bricks
setblock 15 64 287 minecraft:lava
setblock 15 64 288 minecraft:lava
setblock 15 64 289 minecraft:lava
setblock 15 64 290 minecraft:glass
setblock 16 64 286 minecraft:stone_bricks
setblock 16 64 287 minecraft:lava
setblock 16 64 288 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 289 minecraft:glass
setblock 16 64 290 minecraft:glass
setblock 17 64 286 minecraft:stone_bricks
setblock 17 64 287 minecraft:lava
setblock 17 64 288 minecraft:lava
setblock 17 64 289 minecraft:lava
setblock 17 64 290 minecraft:glass
setblock 18 64 286 minecraft:stone_bricks
setblock 18 64 287 minecraft:stone_bricks
setblock 18 64 288 minecraft:stone_bricks
setblock 18 64 289 minecraft:stone_bricks
setblock 18 64 290 minecraft:glass
setblock 22 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 283 31 79 296 minecraft:light_gray_concrete
setblock 26 64 288 createaddition:alternator[facing=east]
setblock 25 64 288 create:shaft[axis=x]
setblock 24 64 288 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 288 create:andesite_casing
setblock 24 64 289 create:andesite_casing
setblock 24 64 287 create:andesite_casing
setblock 24 65 288 create:andesite_casing
setblock 32 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 283 45 79 296 minecraft:light_gray_concrete
kw testworld use 35 63 288 up mekmm:large_heat_generator
kw testworld use 41 63 288 up mekmm:large_gas_burning_generator
setblock 46 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 283 57 79 296 minecraft:light_gray_concrete
setblock 48 64 287 nuclearcraft:solar_panel_basic
setblock 50 64 287 nuclearcraft:solar_panel_advanced
setblock 52 64 287 nuclearcraft:solar_panel_du
setblock 54 64 287 nuclearcraft:solar_panel_elite
setblock 48 64 289 nuclearcraft:uranium_rtg
setblock 50 64 289 nuclearcraft:americium_rtg
setblock 52 64 289 nuclearcraft:plutonium_rtg
setblock 54 64 289 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
