# 075 immersive_heavy/hv
#area 370 158 393 183
fill 370 64 158 393 95 183 minecraft:air
fill 370 60 158 393 62 183 minecraft:stone
fill 370 63 158 393 63 183 minecraft:light_gray_concrete
fill 374 64 164 393 83 164 minecraft:light_gray_concrete
fill 374 64 164 374 83 177 minecraft:light_gray_concrete
setblock 375 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 376 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 377 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 388 64 164 388 83 177 minecraft:light_gray_concrete
kw testworld use 377 63 169 up immersiveengineering:steel_post
execute unless block 377 67 169 minecraft:air
kw testworld use 377 67 169 up immersiveengineering:connector_hv
kw testworld use 385 63 169 up immersiveengineering:steel_post
execute unless block 385 67 169 minecraft:air
kw testworld use 385 67 169 up immersiveengineering:connector_hv
kw testworld use 377 68 169 south immersiveengineering:wirecoil_steel
kw testworld use 385 68 169 south immersiveengineering:wirecoil_steel
