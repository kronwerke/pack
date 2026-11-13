# 117 immersive/coke_oven
#area 11 217 30 242
fill 11 64 217 30 91 242 minecraft:air
fill 11 60 217 30 62 242 minecraft:stone
fill 11 63 217 30 63 242 minecraft:light_gray_concrete
fill 15 64 223 30 79 223 minecraft:light_gray_concrete
fill 15 64 223 15 79 236 minecraft:light_gray_concrete
setblock 16 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 223 25 79 236 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 226 none
kw testworld use 20 65 228 south immersiveengineering:hammer
execute unless block 20 65 228 immersiveengineering:cokebrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
