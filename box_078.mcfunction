# 078 immersive_heavy/hv
#area 342 177 365 202
fill 342 64 177 365 95 202 minecraft:air
fill 342 60 177 365 62 202 minecraft:stone
fill 342 63 177 365 63 202 minecraft:light_gray_concrete
fill 346 64 183 365 83 183 minecraft:light_gray_concrete
fill 346 64 183 346 83 196 minecraft:light_gray_concrete
setblock 347 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 348 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 349 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 360 64 183 360 83 196 minecraft:light_gray_concrete
kw testworld use 349 63 188 up immersiveengineering:steel_post
execute unless block 349 67 188 minecraft:air
kw testworld use 349 67 188 up immersiveengineering:connector_hv
kw testworld use 357 63 188 up immersiveengineering:steel_post
execute unless block 357 67 188 minecraft:air
kw testworld use 357 67 188 up immersiveengineering:connector_hv
kw testworld use 349 68 188 south immersiveengineering:wirecoil_steel
kw testworld use 357 68 188 south immersiveengineering:wirecoil_steel
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
