# 119 immersive/kiln
#area 51 217 70 242
fill 51 64 217 70 91 242 minecraft:air
fill 51 60 217 70 62 242 minecraft:stone
fill 51 63 217 70 63 242 minecraft:light_gray_concrete
fill 55 64 223 70 79 223 minecraft:light_gray_concrete
fill 55 64 223 55 79 236 minecraft:light_gray_concrete
setblock 56 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 223 65 79 236 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 226 none
kw testworld use 60 65 227 south immersiveengineering:hammer
execute unless block 60 65 227 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
