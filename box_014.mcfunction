# 014 create/windmill
#area 12 42 35 71
fill 12 64 42 35 99 71 minecraft:air
fill 12 60 42 35 62 71 minecraft:stone
fill 12 63 42 35 63 71 minecraft:light_gray_concrete
fill 16 64 48 35 87 48 minecraft:light_gray_concrete
fill 16 64 48 16 87 65 minecraft:light_gray_concrete
setblock 17 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create"}','{"text": "windmill"}','{"text": ""}']}}
setblock 18 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "windmill with"}','{"text": "32 sails"}','{"text": ""}']}}
fill 30 64 48 30 87 65 minecraft:light_gray_concrete
fill 23 64 54 23 69 54 minecraft:spruce_log[axis=y]
setblock 23 70 54 create:windmill_bearing[facing=south]
setblock 23 70 55 create:white_sail[facing=south]
fill 23 71 55 24 74 55 create:white_sail[facing=south]
fill 24 69 55 27 70 55 create:white_sail[facing=south]
fill 22 66 55 23 69 55 create:white_sail[facing=south]
fill 19 70 55 22 71 55 create:white_sail[facing=south]
kw testworld use 23 70 54 south minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
