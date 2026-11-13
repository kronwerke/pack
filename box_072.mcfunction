# 072 immersive/kiln
#area 51 177 70 202
fill 51 64 177 70 91 202 minecraft:air
fill 51 60 177 70 62 202 minecraft:stone
fill 51 63 177 70 63 202 minecraft:light_gray_concrete
fill 55 64 183 70 79 183 minecraft:light_gray_concrete
fill 55 64 183 55 79 196 minecraft:light_gray_concrete
setblock 56 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 183 65 79 196 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 186 none
kw testworld use 60 65 187 south immersiveengineering:hammer
execute unless block 60 65 187 immersiveengineering:alloybrick
