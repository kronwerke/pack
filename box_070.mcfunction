# 070 immersive/coke_oven
#area 11 177 30 202
fill 11 64 177 30 91 202 minecraft:air
fill 11 60 177 30 62 202 minecraft:stone
fill 11 63 177 30 63 202 minecraft:light_gray_concrete
fill 15 64 183 30 79 183 minecraft:light_gray_concrete
fill 15 64 183 15 79 196 minecraft:light_gray_concrete
setblock 16 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 183 25 79 196 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 186 none
kw testworld use 20 65 188 south immersiveengineering:hammer
execute unless block 20 65 188 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
