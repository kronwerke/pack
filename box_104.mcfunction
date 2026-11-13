# 104 immersive/coke_oven
#area 11 181 30 206
fill 11 64 181 30 91 206 minecraft:air
fill 11 60 181 30 62 206 minecraft:stone
fill 11 63 181 30 63 206 minecraft:light_gray_concrete
fill 15 64 187 30 79 187 minecraft:light_gray_concrete
fill 15 64 187 15 79 200 minecraft:light_gray_concrete
setblock 16 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 187 25 79 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 190 none
kw testworld use 20 65 192 south immersiveengineering:hammer
execute unless block 20 65 192 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
