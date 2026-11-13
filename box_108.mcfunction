# 108 immersive/kiln
#area 51 181 70 206
fill 51 64 181 70 91 206 minecraft:air
fill 51 60 181 70 62 206 minecraft:stone
fill 51 63 181 70 63 206 minecraft:light_gray_concrete
fill 55 64 187 70 79 187 minecraft:light_gray_concrete
fill 55 64 187 55 79 200 minecraft:light_gray_concrete
setblock 56 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 57 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 65 64 187 65 79 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 59 64 190 none
kw testworld use 60 65 191 south immersiveengineering:hammer
execute unless block 60 65 191 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
