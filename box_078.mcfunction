# 078 immersive_heavy/hv
#area 370 177 393 202
fill 370 64 177 393 95 202 minecraft:air
fill 370 60 177 393 62 202 minecraft:stone
fill 370 63 177 393 63 202 minecraft:light_gray_concrete
fill 374 64 183 393 83 183 minecraft:light_gray_concrete
fill 374 64 183 374 83 196 minecraft:light_gray_concrete
setblock 375 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 376 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 377 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 388 64 183 388 83 196 minecraft:light_gray_concrete
kw testworld use 377 63 188 up immersiveengineering:steel_post
execute unless block 377 67 188 minecraft:air
kw testworld use 377 67 188 up immersiveengineering:connector_hv
kw testworld use 385 63 188 up immersiveengineering:steel_post
execute unless block 385 67 188 minecraft:air
kw testworld use 385 67 188 up immersiveengineering:connector_hv
kw testworld use 377 68 188 south immersiveengineering:wirecoil_steel
kw testworld use 385 68 188 south immersiveengineering:wirecoil_steel
