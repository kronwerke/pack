# 116 immersive/coke_oven
#area 11 211 30 236
fill 11 64 211 30 91 236 minecraft:air
fill 11 60 211 30 62 236 minecraft:stone
fill 11 63 211 30 63 236 minecraft:light_gray_concrete
fill 15 64 217 30 79 217 minecraft:light_gray_concrete
fill 15 64 217 15 79 230 minecraft:light_gray_concrete
setblock 16 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 217 25 79 230 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 220 none
kw testworld use 20 65 222 south immersiveengineering:hammer
execute unless block 20 65 222 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
