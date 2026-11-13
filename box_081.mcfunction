# 081 list_power/steam_engine, ie_thermo, powah_reactor
#area -4 231 36 256
fill -4 64 231 36 93 256 minecraft:air
fill -4 60 231 36 62 256 minecraft:stone
fill -4 63 231 36 63 256 minecraft:light_gray_concrete
fill 0 64 237 36 81 237 minecraft:light_gray_concrete
fill 0 64 237 0 81 250 minecraft:light_gray_concrete
setblock 1 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 237 11 81 250 minecraft:light_gray_concrete
setblock 4 64 241 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 241 up create:creative_blaze_cake
setblock 4 64 242 create:blaze_burner[blaze=smouldering]
kw testworld use 4 64 242 up create:creative_blaze_cake
setblock 5 64 241 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 241 up create:creative_blaze_cake
setblock 5 64 242 create:blaze_burner[blaze=smouldering]
kw testworld use 5 64 242 up create:creative_blaze_cake
fill 4 65 241 5 67 242 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 4 66 244 create:shaft[axis=x]
setblock 4 66 243 create:steam_engine[face=wall,facing=south,waterlogged=false]
setblock 12 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.2"}','{"text": "list_power"}','{"text": "ie_thermo"}','{"text": ""}']}}
setblock 13 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann Lava"}','{"text": "gegen Wasser"}','{"text": ""}','{"text": ""}']}}
fill 21 64 237 21 81 250 minecraft:light_gray_concrete
setblock 15 64 242 minecraft:magma_block
setblock 16 64 242 immersiveengineering:thermoelectric_generator
setblock 17 64 242 minecraft:blue_ice
kw testworld use 16 64 242 up immersiveengineering:connector_lv
setblock 22 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.3"}','{"text": "list_power"}','{"text": "powah_reactor"}','{"text": ""}']}}
setblock 23 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den"}','{"text": "Powah-Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 31 64 237 31 81 250 minecraft:light_gray_concrete
setblock 26 64 242 powah:reactor_starter[core=true]
