# 006 create/windmill
#area 12 21 35 50
fill 12 64 21 35 99 50 minecraft:air
fill 12 60 21 35 62 50 minecraft:stone
fill 12 63 21 35 63 50 minecraft:light_gray_concrete
fill 16 64 27 35 87 27 minecraft:light_gray_concrete
fill 16 64 27 16 87 44 minecraft:light_gray_concrete
setblock 17 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "006"}','{"text": "create"}','{"text": "windmill"}','{"text": ""}']}}
setblock 18 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "windmill with"}','{"text": "32 sails"}','{"text": ""}']}}
fill 30 64 27 30 87 44 minecraft:light_gray_concrete
fill 23 64 33 23 69 33 minecraft:spruce_log[axis=y]
setblock 23 70 33 create:windmill_bearing[facing=south]
setblock 23 70 34 create:white_sail[facing=south]
fill 23 71 34 24 74 34 create:white_sail[facing=south]
fill 24 69 34 27 70 34 create:white_sail[facing=south]
fill 22 66 34 23 69 34 create:white_sail[facing=south]
fill 19 70 34 22 71 34 create:white_sail[facing=south]
kw testworld use 23 70 33 south minecraft:air
