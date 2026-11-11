# 038 immersive/kiln
#area 26 144 45 169
fill 26 64 144 45 91 169 minecraft:air
fill 26 60 144 45 62 169 minecraft:stone
fill 26 63 144 45 63 169 minecraft:light_gray_concrete
fill 30 64 150 45 79 150 minecraft:light_gray_concrete
fill 30 64 150 30 79 163 minecraft:light_gray_concrete
setblock 31 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 32 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 40 64 150 40 79 163 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 34 64 153 none
kw testworld use 35 65 154 south immersiveengineering:hammer
execute unless block 35 65 154 immersiveengineering:alloybrick
