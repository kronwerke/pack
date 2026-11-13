# 108 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 275 62 306
fill -4 64 275 14 115 306 minecraft:air
fill 15 64 275 33 115 306 minecraft:air
fill 34 64 275 52 115 306 minecraft:air
fill 53 64 275 62 115 306 minecraft:air
fill -4 60 275 62 62 306 minecraft:stone
fill -4 63 275 62 63 306 minecraft:light_gray_concrete
fill 0 64 281 62 103 281 minecraft:light_gray_concrete
fill 0 64 281 0 103 300 minecraft:light_gray_concrete
setblock 1 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 281 11 103 300 minecraft:light_gray_concrete
setblock 4 64 285 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 285 up create:creative_blaze_cake
setblock 4 64 286 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 286 up create:creative_blaze_cake
setblock 5 64 285 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 285 up create:creative_blaze_cake
setblock 5 64 286 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 286 up create:creative_blaze_cake
fill 4 65 285 5 67 286 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 288 create:shaft[axis=x]
setblock 4 66 287 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 281 21 103 300 minecraft:light_gray_concrete
setblock 14 64 284 minecraft:stone_bricks
setblock 14 64 285 minecraft:stone_bricks
setblock 14 64 286 minecraft:stone_bricks
setblock 14 64 287 minecraft:stone_bricks
setblock 14 64 288 minecraft:glass
setblock 15 64 284 minecraft:stone_bricks
setblock 15 64 285 minecraft:lava
setblock 15 64 286 minecraft:lava
setblock 15 64 287 minecraft:lava
setblock 15 64 288 minecraft:glass
setblock 16 64 284 minecraft:stone_bricks
setblock 16 64 285 minecraft:lava
setblock 16 64 286 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 287 minecraft:glass
setblock 16 64 288 minecraft:glass
setblock 17 64 284 minecraft:stone_bricks
setblock 17 64 285 minecraft:lava
setblock 17 64 286 minecraft:lava
setblock 17 64 287 minecraft:lava
setblock 17 64 288 minecraft:glass
setblock 18 64 284 minecraft:stone_bricks
setblock 18 64 285 minecraft:stone_bricks
setblock 18 64 286 minecraft:stone_bricks
setblock 18 64 287 minecraft:stone_bricks
setblock 18 64 288 minecraft:glass
setblock 22 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 281 31 103 300 minecraft:light_gray_concrete
setblock 26 64 286 createaddition:alternator[facing=east]
setblock 25 64 286 create:shaft[axis=x]
setblock 24 64 286 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 286 create:andesite_casing
setblock 24 64 287 create:andesite_casing
setblock 24 64 285 create:andesite_casing
setblock 24 65 286 create:andesite_casing
setblock 32 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 281 45 103 300 minecraft:light_gray_concrete
kw testworld use 35 63 285 up mekmm:large_heat_generator
kw testworld use 41 63 285 up mekmm:large_wind_generator
setblock 46 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 281 57 103 300 minecraft:light_gray_concrete
setblock 48 64 285 nuclearcraft:solar_panel_basic
setblock 50 64 285 nuclearcraft:solar_panel_advanced
setblock 52 64 285 nuclearcraft:solar_panel_du
setblock 54 64 285 nuclearcraft:solar_panel_elite
setblock 48 64 287 nuclearcraft:uranium_rtg
setblock 50 64 287 nuclearcraft:americium_rtg
setblock 52 64 287 nuclearcraft:plutonium_rtg
setblock 54 64 287 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
