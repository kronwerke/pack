# 037 immersive/coke_oven
#area 11 144 30 169
fill 11 64 144 30 91 169 minecraft:air
fill 11 60 144 30 62 169 minecraft:stone
fill 11 63 144 30 63 169 minecraft:light_gray_concrete
fill 15 64 150 30 79 150 minecraft:light_gray_concrete
fill 15 64 150 15 79 163 minecraft:light_gray_concrete
setblock 16 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 150 25 79 163 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 153 none
kw testworld use 20 65 155 south immersiveengineering:hammer
execute unless block 20 65 155 immersiveengineering:cokebrick
