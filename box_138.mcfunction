# 138 immersive/kiln
#area 76 219 95 244
fill 76 64 219 95 91 244 minecraft:air
fill 76 60 219 95 62 244 minecraft:stone
fill 76 63 219 95 63 244 minecraft:light_gray_concrete
fill 80 64 225 95 79 225 minecraft:light_gray_concrete
fill 80 64 225 80 79 238 minecraft:light_gray_concrete
setblock 81 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 82 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": ""}','{"text": ""}']}}
fill 90 64 225 90 79 238 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/alloy_smelter 84 64 228 none
kw testworld use 85 65 229 south immersiveengineering:hammer
execute unless block 85 65 229 immersiveengineering:alloybrick
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
