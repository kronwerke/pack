# 126 immersive_heavy/hv, survey
#area 383 211 416 236
fill 383 64 211 416 95 236 minecraft:air
fill 383 60 211 416 62 236 minecraft:stone
fill 383 63 211 416 63 236 minecraft:light_gray_concrete
fill 387 64 217 416 83 217 minecraft:light_gray_concrete
fill 387 64 217 387 83 230 minecraft:light_gray_concrete
setblock 388 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 389 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 390 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 401 64 217 401 83 230 minecraft:light_gray_concrete
kw testworld use 390 63 222 up immersiveengineering:steel_post
execute unless block 390 67 222 minecraft:air
kw testworld use 390 67 222 up immersiveengineering:connector_hv
kw testworld use 398 63 222 up immersiveengineering:steel_post
execute unless block 398 67 222 minecraft:air
kw testworld use 398 67 222 up immersiveengineering:connector_hv
kw testworld use 390 68 222 south immersiveengineering:wirecoil_steel
kw testworld use 398 68 222 south immersiveengineering:wirecoil_steel
setblock 402 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.2"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 403 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 411 64 217 411 83 230 minecraft:light_gray_concrete
kw testworld use 406 63 222 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
