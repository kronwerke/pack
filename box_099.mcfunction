# 099 immersive_heavy/hv, survey
#area 373 179 406 204
fill 373 64 179 406 95 204 minecraft:air
fill 373 60 179 406 62 204 minecraft:stone
fill 373 63 179 406 63 204 minecraft:light_gray_concrete
fill 377 64 185 406 83 185 minecraft:light_gray_concrete
fill 377 64 185 377 83 198 minecraft:light_gray_concrete
setblock 378 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 379 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 380 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 391 64 185 391 83 198 minecraft:light_gray_concrete
kw testworld use 380 63 190 up immersiveengineering:steel_post
execute unless block 380 67 190 minecraft:air
kw testworld use 380 67 190 up immersiveengineering:connector_hv
kw testworld use 388 63 190 up immersiveengineering:steel_post
execute unless block 388 67 190 minecraft:air
kw testworld use 388 67 190 up immersiveengineering:connector_hv
kw testworld use 380 68 190 south immersiveengineering:wirecoil_steel
kw testworld use 388 68 190 south immersiveengineering:wirecoil_steel
setblock 392 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.2"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 393 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 401 64 185 401 83 198 minecraft:light_gray_concrete
kw testworld use 396 63 190 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
