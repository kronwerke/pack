# 117 immersive/coke_oven
#area 11 215 30 240
fill 11 64 215 30 91 240 minecraft:air
fill 11 60 215 30 62 240 minecraft:stone
fill 11 63 215 30 63 240 minecraft:light_gray_concrete
fill 15 64 221 30 79 221 minecraft:light_gray_concrete
fill 15 64 221 15 79 234 minecraft:light_gray_concrete
setblock 16 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 221 25 79 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 224 none
kw testworld use 20 65 226 south immersiveengineering:hammer
execute unless block 20 65 226 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
