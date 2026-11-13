# 087 list_power/steam_engine, mek_heat, alternator, mekmm_large, nc_passive
#area -4 254 62 279
fill -4 64 254 40 91 279 minecraft:air
fill 41 64 254 62 91 279 minecraft:air
fill -4 60 254 62 62 279 minecraft:stone
fill -4 63 254 62 63 279 minecraft:light_gray_concrete
fill 0 64 260 62 79 260 minecraft:light_gray_concrete
fill 0 64 260 0 79 273 minecraft:light_gray_concrete
setblock 1 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 260 11 79 273 minecraft:light_gray_concrete
setblock 4 64 264 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 264 up create:creative_blaze_cake
setblock 4 64 265 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 265 up create:creative_blaze_cake
setblock 5 64 264 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 264 up create:creative_blaze_cake
setblock 5 64 265 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 265 up create:creative_blaze_cake
fill 4 65 264 5 67 265 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 267 create:shaft[axis=x]
setblock 4 66 266 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 13 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
fill 21 64 260 21 79 273 minecraft:light_gray_concrete
setblock 14 64 263 minecraft:stone_bricks
setblock 14 64 264 minecraft:stone_bricks
setblock 14 64 265 minecraft:stone_bricks
setblock 14 64 266 minecraft:stone_bricks
setblock 14 64 267 minecraft:glass
setblock 15 64 263 minecraft:stone_bricks
setblock 15 64 264 minecraft:lava
setblock 15 64 265 minecraft:lava
setblock 15 64 266 minecraft:lava
setblock 15 64 267 minecraft:glass
setblock 16 64 263 minecraft:stone_bricks
setblock 16 64 264 minecraft:lava
setblock 16 64 265 mekanismgenerators:heat_generator[facing=south]
setblock 16 64 266 minecraft:glass
setblock 16 64 267 minecraft:glass
setblock 17 64 263 minecraft:stone_bricks
setblock 17 64 264 minecraft:lava
setblock 17 64 265 minecraft:lava
setblock 17 64 266 minecraft:lava
setblock 17 64 267 minecraft:glass
setblock 18 64 263 minecraft:stone_bricks
setblock 18 64 264 minecraft:stone_bricks
setblock 18 64 265 minecraft:stone_bricks
setblock 18 64 266 minecraft:stone_bricks
setblock 18 64 267 minecraft:glass
setblock 22 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087.3"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 23 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
fill 31 64 260 31 79 273 minecraft:light_gray_concrete
setblock 26 64 265 createaddition:alternator[facing=east]
setblock 25 64 265 create:shaft[axis=x]
setblock 24 64 265 create:creative_motor[facing=east]{ScrollValue:64}
setblock 23 64 265 create:andesite_casing
setblock 24 64 266 create:andesite_casing
setblock 24 64 264 create:andesite_casing
setblock 24 65 265 create:andesite_casing
setblock 32 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087.4"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 33 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
fill 45 64 260 45 79 273 minecraft:light_gray_concrete
kw testworld use 35 63 266 up mekmm:large_heat_generator
kw testworld use 41 63 266 up mekmm:large_wind_generator
setblock 46 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087.5"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 47 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
fill 57 64 260 57 79 273 minecraft:light_gray_concrete
setblock 48 64 264 nuclearcraft:solar_panel_basic
setblock 50 64 264 nuclearcraft:solar_panel_advanced
setblock 52 64 264 nuclearcraft:solar_panel_du
setblock 54 64 264 nuclearcraft:solar_panel_elite
setblock 48 64 266 nuclearcraft:uranium_rtg
setblock 50 64 266 nuclearcraft:americium_rtg
setblock 52 64 266 nuclearcraft:plutonium_rtg
setblock 54 64 266 nuclearcraft:californium_rtg
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
