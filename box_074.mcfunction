# 074 list_power/steam_engine
#area -4 231 16 256
fill -4 64 231 16 91 256 minecraft:air
fill -4 60 231 16 62 256 minecraft:stone
fill -4 63 231 16 63 256 minecraft:light_gray_concrete
fill 0 64 237 16 79 237 minecraft:light_gray_concrete
fill 0 64 237 0 79 250 minecraft:light_gray_concrete
setblock 1 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 237 11 79 250 minecraft:light_gray_concrete
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
