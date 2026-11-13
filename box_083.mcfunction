# 083 list_power/steam_engine, ie_thermo, powah_reactor
#area -4 250 36 275
fill -4 64 250 36 93 275 minecraft:air
fill -4 60 250 36 62 275 minecraft:stone
fill -4 63 250 36 63 275 minecraft:light_gray_concrete
fill 0 64 256 36 81 256 minecraft:light_gray_concrete
fill 0 64 256 0 81 269 minecraft:light_gray_concrete
setblock 1 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 256 11 81 269 minecraft:light_gray_concrete
setblock 4 64 260 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 260 up create:creative_blaze_cake
setblock 4 64 261 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 261 up create:creative_blaze_cake
setblock 5 64 260 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 260 up create:creative_blaze_cake
setblock 5 64 261 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 261 up create:creative_blaze_cake
fill 4 65 260 5 67 261 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 263 create:shaft[axis=x]
setblock 4 66 262 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.2"}','{"text": "list_power"}','{"text": "ie_thermo"}','{"text": ""}']}}
setblock 13 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann Lava"}','{"text": "gegen Wasser"}','{"text": ""}','{"text": ""}']}}
fill 21 64 256 21 81 269 minecraft:light_gray_concrete
setblock 15 64 261 minecraft:magma_block
setblock 16 64 261 immersiveengineering:thermoelectric_generator
setblock 17 64 261 minecraft:blue_ice
kw testworld use 16 64 261 up immersiveengineering:connector_lv
setblock 22 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.3"}','{"text": "list_power"}','{"text": "powah_reactor"}','{"text": ""}']}}
setblock 23 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den"}','{"text": "Powah-Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 31 64 256 31 81 269 minecraft:light_gray_concrete
setblock 26 64 261 powah:reactor_starter[core=true]
