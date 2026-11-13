# 017 create/windmill
#area 12 44 35 73
fill 12 64 44 35 99 73 minecraft:air
fill 12 60 44 35 62 73 minecraft:stone
fill 12 63 44 35 63 73 minecraft:light_gray_concrete
fill 16 64 50 35 87 50 minecraft:light_gray_concrete
fill 16 64 50 16 87 67 minecraft:light_gray_concrete
setblock 17 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "create"}','{"text": "windmill"}','{"text": ""}']}}
setblock 18 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "windmill with"}','{"text": "32 sails"}','{"text": ""}']}}
fill 30 64 50 30 87 67 minecraft:light_gray_concrete
fill 23 64 56 23 69 56 minecraft:spruce_log[axis=y]
setblock 23 70 56 create:windmill_bearing[facing=south]
setblock 23 70 57 create:white_sail[facing=south]
fill 23 71 57 24 74 57 create:white_sail[facing=south]
fill 24 69 57 27 70 57 create:white_sail[facing=south]
fill 22 66 57 23 69 57 create:white_sail[facing=south]
fill 19 70 57 22 71 57 create:white_sail[facing=south]
kw testworld use 23 70 56 south minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
