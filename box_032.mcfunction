# 032 create_brass/boiler
#area 250 44 269 76
fill 250 64 44 269 93 76 minecraft:air
fill 250 60 44 269 62 76 minecraft:stone
fill 250 63 44 269 63 76 minecraft:light_gray_concrete
fill 254 64 50 269 81 50 minecraft:light_gray_concrete
fill 254 64 50 254 81 70 minecraft:light_gray_concrete
setblock 255 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "create_brass"}','{"text": "boiler"}','{"text": ""}']}}
setblock 256 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a four engine"}','{"text": "boiler with the"}','{"text": "goggles boiler"}','{"text": "overlay"}']}}
fill 264 64 50 264 81 70 minecraft:light_gray_concrete
kw testworld place shots:create/steam_engine 256 63 52 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
