# 162 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 319 62 344
fill -4 64 319 40 91 344 minecraft:air
fill 41 64 319 62 91 344 minecraft:air
fill -4 60 319 62 62 344 minecraft:stone
fill -4 63 319 62 63 344 minecraft:light_gray_concrete
fill 0 64 325 62 79 325 minecraft:light_gray_concrete
fill 0 64 325 0 79 338 minecraft:light_gray_concrete
setblock 1 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 325 11 79 338 minecraft:light_gray_concrete
setblock 4 64 329 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 329 up create:creative_blaze_cake
setblock 4 64 330 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 330 up create:creative_blaze_cake
setblock 5 64 329 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 329 up create:creative_blaze_cake
setblock 5 64 330 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 330 up create:creative_blaze_cake
fill 4 65 329 5 67 330 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 332 create:shaft[axis=x]
setblock 4 66 331 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 325 21 79 338 minecraft:light_gray_concrete
setblock 14 64 328 minecraft:stone_bricks
setblock 14 64 329 minecraft:stone_bricks
setblock 14 64 330 minecraft:stone_bricks
setblock 14 64 331 minecraft:stone_bricks
setblock 14 64 332 minecraft:glass
setblock 15 64 328 minecraft:stone_bricks
setblock 15 64 329 minecraft:lava
setblock 15 64 330 minecraft:lava
setblock 15 64 331 minecraft:lava
setblock 15 64 332 minecraft:glass
setblock 16 64 328 minecraft:stone_bricks
setblock 16 64 329 minecraft:lava
setblock 16 64 330 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 331 minecraft:glass
setblock 16 64 332 minecraft:glass
setblock 17 64 328 minecraft:stone_bricks
setblock 17 64 329 minecraft:lava
setblock 17 64 330 minecraft:lava
setblock 17 64 331 minecraft:lava
setblock 17 64 332 minecraft:glass
setblock 18 64 328 minecraft:stone_bricks
setblock 18 64 329 minecraft:stone_bricks
setblock 18 64 330 minecraft:stone_bricks
setblock 18 64 331 minecraft:stone_bricks
setblock 18 64 332 minecraft:glass
setblock 22 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 325 31 79 338 minecraft:light_gray_concrete
setblock 26 64 330 createaddition:alternator[facing=east]
setblock 25 64 330 create:shaft[axis=x]
setblock 24 64 330 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 330 create:andesite_casing
setblock 24 64 331 create:andesite_casing
setblock 24 64 329 create:andesite_casing
setblock 24 65 330 create:andesite_casing
setblock 32 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 325 45 79 338 minecraft:light_gray_concrete
kw testworld use 35 63 330 up mekmm:large_heat_generator
kw testworld use 41 63 330 up mekmm:large_gas_burning_generator
setblock 46 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 325 57 79 338 minecraft:light_gray_concrete
setblock 48 64 329 nuclearcraft:solar_panel_basic
setblock 50 64 329 nuclearcraft:solar_panel_advanced
setblock 52 64 329 nuclearcraft:solar_panel_du
setblock 54 64 329 nuclearcraft:solar_panel_elite
setblock 48 64 331 nuclearcraft:uranium_rtg
setblock 50 64 331 nuclearcraft:americium_rtg
setblock 52 64 331 nuclearcraft:plutonium_rtg
setblock 54 64 331 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
