# 123 immersive/kiln
#area 76 217 95 242
fill 76 64 217 95 91 242 minecraft:air
fill 76 60 217 95 62 242 minecraft:stone
fill 76 63 217 95 63 242 minecraft:light_gray_concrete
fill 80 64 223 95 79 223 minecraft:light_gray_concrete
fill 80 64 223 80 79 236 minecraft:light_gray_concrete
setblock 81 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 82 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 90 64 223 90 79 236 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 84 64 226 none
kw testworld use 85 65 227 south immersiveengineering:hammer
execute unless block 85 65 227 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
