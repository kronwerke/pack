# 119 immersive/kiln
#area 51 215 70 240
fill 51 64 215 70 91 240 minecraft:air
fill 51 60 215 70 62 240 minecraft:stone
fill 51 63 215 70 63 240 minecraft:light_gray_concrete
fill 55 64 221 70 79 221 minecraft:light_gray_concrete
fill 55 64 221 55 79 234 minecraft:light_gray_concrete
setblock 56 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 221 65 79 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 224 none
kw testworld use 60 65 225 south immersiveengineering:hammer
execute unless block 60 65 225 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
