# 030 create_brass/boiler
#area 250 42 269 74
fill 250 64 42 269 93 74 minecraft:air
fill 250 60 42 269 62 74 minecraft:stone
fill 250 63 42 269 63 74 minecraft:light_gray_concrete
fill 254 64 48 269 81 48 minecraft:light_gray_concrete
fill 254 64 48 254 81 68 minecraft:light_gray_concrete
setblock 255 64 67 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create_brass"}','{"text": "boiler"}','{"text": ""}']}}
setblock 256 64 67 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a four engine"}','{"text": "boiler with the"}','{"text": "goggles boiler"}','{"text": "overlay"}']}}
fill 264 64 48 264 81 68 minecraft:light_gray_concrete
kw testworld place shots:create/steam_engine 256 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
