# 067 immersive/coke_oven
#area 11 158 30 183
fill 11 64 158 30 91 183 minecraft:air
fill 11 60 158 30 62 183 minecraft:stone
fill 11 63 158 30 63 183 minecraft:light_gray_concrete
fill 15 64 164 30 79 164 minecraft:light_gray_concrete
fill 15 64 164 15 79 177 minecraft:light_gray_concrete
setblock 16 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 164 25 79 177 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 167 none
kw testworld use 20 65 169 south immersiveengineering:hammer
execute unless block 20 65 169 immersiveengineering:cokebrick
