# 052 immersive/kiln
#area 51 158 70 183
fill 51 64 158 70 91 183 minecraft:air
fill 51 60 158 70 62 183 minecraft:stone
fill 51 63 158 70 63 183 minecraft:light_gray_concrete
fill 55 64 164 70 79 164 minecraft:light_gray_concrete
fill 55 64 164 55 79 177 minecraft:light_gray_concrete
setblock 56 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 164 65 79 177 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 167 none
kw testworld use 60 65 168 south immersiveengineering:hammer
execute unless block 60 65 168 immersiveengineering:alloybrick
