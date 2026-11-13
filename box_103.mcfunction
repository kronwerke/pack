# 103 immersive/kiln
#area 51 179 70 204
fill 51 64 179 70 91 204 minecraft:air
fill 51 60 179 70 62 204 minecraft:stone
fill 51 63 179 70 63 204 minecraft:light_gray_concrete
fill 55 64 185 70 79 185 minecraft:light_gray_concrete
fill 55 64 185 55 79 198 minecraft:light_gray_concrete
setblock 56 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 185 65 79 198 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 188 none
kw testworld use 60 65 189 south immersiveengineering:hammer
execute unless block 60 65 189 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
