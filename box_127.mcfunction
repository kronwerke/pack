# 127 immersive_heavy/hv, survey
#area 383 217 416 242
fill 383 64 217 416 95 242 minecraft:air
fill 383 60 217 416 62 242 minecraft:stone
fill 383 63 217 416 63 242 minecraft:light_gray_concrete
fill 387 64 223 416 83 223 minecraft:light_gray_concrete
fill 387 64 223 387 83 236 minecraft:light_gray_concrete
setblock 388 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 389 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 390 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 401 64 223 401 83 236 minecraft:light_gray_concrete
kw testworld use 390 63 228 up immersiveengineering:steel_post
execute unless block 390 67 228 minecraft:air
kw testworld use 390 67 228 up immersiveengineering:connector_hv
kw testworld use 398 63 228 up immersiveengineering:steel_post
execute unless block 398 67 228 minecraft:air
kw testworld use 398 67 228 up immersiveengineering:connector_hv
kw testworld use 390 68 228 south immersiveengineering:wirecoil_steel
kw testworld use 398 68 228 south immersiveengineering:wirecoil_steel
setblock 402 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.2"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 403 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 411 64 223 411 83 236 minecraft:light_gray_concrete
kw testworld use 406 63 228 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
