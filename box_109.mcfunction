# 109 immersive_heavy/hv, survey
#area 383 179 416 204
fill 383 64 179 416 95 204 minecraft:air
fill 383 60 179 416 62 204 minecraft:stone
fill 383 63 179 416 63 204 minecraft:light_gray_concrete
fill 387 64 185 416 83 185 minecraft:light_gray_concrete
fill 387 64 185 387 83 198 minecraft:light_gray_concrete
setblock 388 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 389 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 390 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 401 64 185 401 83 198 minecraft:light_gray_concrete
kw testworld use 390 63 190 up immersiveengineering:steel_post
execute unless block 390 67 190 minecraft:air
kw testworld use 390 67 190 up immersiveengineering:connector_hv
kw testworld use 398 63 190 up immersiveengineering:steel_post
execute unless block 398 67 190 minecraft:air
kw testworld use 398 67 190 up immersiveengineering:connector_hv
kw testworld use 390 68 190 south immersiveengineering:wirecoil_steel
kw testworld use 398 68 190 south immersiveengineering:wirecoil_steel
setblock 402 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109.2"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 403 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 411 64 185 411 83 198 minecraft:light_gray_concrete
kw testworld use 406 63 190 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
