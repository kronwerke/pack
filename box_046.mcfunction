# 046 immersive/kiln
#area 51 144 70 169
fill 51 64 144 70 91 169 minecraft:air
fill 51 60 144 70 62 169 minecraft:stone
fill 51 63 144 70 63 169 minecraft:light_gray_concrete
fill 55 64 150 70 79 150 minecraft:light_gray_concrete
fill 55 64 150 55 79 163 minecraft:light_gray_concrete
setblock 56 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 150 65 79 163 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 153 none
kw testworld use 60 65 154 south immersiveengineering:hammer
execute unless block 60 65 154 immersiveengineering:alloybrick
