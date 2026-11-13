# 076 immersive_heavy/hv
#area 368 158 391 183
fill 368 64 158 391 95 183 minecraft:air
fill 368 60 158 391 62 183 minecraft:stone
fill 368 63 158 391 63 183 minecraft:light_gray_concrete
fill 372 64 164 391 83 164 minecraft:light_gray_concrete
fill 372 64 164 372 83 177 minecraft:light_gray_concrete
setblock 373 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 374 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 375 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 386 64 164 386 83 177 minecraft:light_gray_concrete
kw testworld use 375 63 169 up immersiveengineering:steel_post
execute unless block 375 67 169 minecraft:air
kw testworld use 375 67 169 up immersiveengineering:connector_hv
kw testworld use 383 63 169 up immersiveengineering:steel_post
execute unless block 383 67 169 minecraft:air
kw testworld use 383 67 169 up immersiveengineering:connector_hv
kw testworld use 375 68 169 south immersiveengineering:wirecoil_steel
kw testworld use 383 68 169 south immersiveengineering:wirecoil_steel
