# 099 immersive/coke_oven
#area 11 179 30 204
fill 11 64 179 30 91 204 minecraft:air
fill 11 60 179 30 62 204 minecraft:stone
fill 11 63 179 30 63 204 minecraft:light_gray_concrete
fill 15 64 185 30 79 185 minecraft:light_gray_concrete
fill 15 64 185 15 79 198 minecraft:light_gray_concrete
setblock 16 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 185 25 79 198 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 188 none
kw testworld use 20 65 190 south immersiveengineering:hammer
execute unless block 20 65 190 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
