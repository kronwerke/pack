# 115 immersive/kiln
#area 51 211 70 236
fill 51 64 211 70 91 236 minecraft:air
fill 51 60 211 70 62 236 minecraft:stone
fill 51 63 211 70 63 236 minecraft:light_gray_concrete
fill 55 64 217 70 79 217 minecraft:light_gray_concrete
fill 55 64 217 55 79 230 minecraft:light_gray_concrete
setblock 56 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 217 65 79 230 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 220 none
kw testworld use 60 65 221 south immersiveengineering:hammer
execute unless block 60 65 221 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
