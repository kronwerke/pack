# 033 create_brass/alternator
#area 314 42 331 65
fill 314 64 42 331 91 65 minecraft:air
fill 314 60 42 331 62 65 minecraft:stone
fill 314 63 42 331 63 65 minecraft:light_gray_concrete
fill 318 64 48 331 79 48 minecraft:light_gray_concrete
fill 318 64 48 318 79 59 minecraft:light_gray_concrete
setblock 319 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "create_brass"}','{"text": "alternator"}','{"text": ""}']}}
setblock 320 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "steam engine"}','{"text": "driving an"}','{"text": "alternator with"}','{"text": "connectors"}']}}
fill 326 64 48 326 79 59 minecraft:light_gray_concrete
kw testworld place shots:createaddition/alternator 320 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
