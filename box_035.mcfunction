# 035 create_brass/alternator
#area 314 44 331 67
fill 314 64 44 331 91 67 minecraft:air
fill 314 60 44 331 62 67 minecraft:stone
fill 314 63 44 331 63 67 minecraft:light_gray_concrete
fill 318 64 50 331 79 50 minecraft:light_gray_concrete
fill 318 64 50 318 79 61 minecraft:light_gray_concrete
setblock 319 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_brass"}','{"text": "alternator"}','{"text": ""}']}}
setblock 320 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "steam engine"}','{"text": "driving an"}','{"text": "alternator with"}','{"text": "connectors"}']}}
fill 326 64 50 326 79 61 minecraft:light_gray_concrete
kw testworld place shots:createaddition/alternator 320 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
