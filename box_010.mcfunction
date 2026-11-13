# 010 create/windmill
#area 12 40 35 69
fill 12 64 40 35 99 69 minecraft:air
fill 12 60 40 35 62 69 minecraft:stone
fill 12 63 40 35 63 69 minecraft:light_gray_concrete
fill 16 64 46 35 87 46 minecraft:light_gray_concrete
fill 16 64 46 16 87 63 minecraft:light_gray_concrete
setblock 17 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "create"}','{"text": "windmill"}','{"text": ""}']}}
setblock 18 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "windmill with"}','{"text": "32 sails"}','{"text": ""}']}}
fill 30 64 46 30 87 63 minecraft:light_gray_concrete
fill 23 64 52 23 69 52 minecraft:spruce_log[axis=y]
setblock 23 70 52 create:windmill_bearing[facing=south]
setblock 23 70 53 create:white_sail[facing=south]
fill 23 71 53 24 74 53 create:white_sail[facing=south]
fill 24 69 53 27 70 53 create:white_sail[facing=south]
fill 22 66 53 23 69 53 create:white_sail[facing=south]
fill 19 70 53 22 71 53 create:white_sail[facing=south]
kw testworld use 23 70 52 south minecraft:air
