# 030 create_brass/boiler
#area 265 42 284 74
fill 265 64 42 284 93 74 minecraft:air
fill 265 60 42 284 62 74 minecraft:stone
fill 265 63 42 284 63 74 minecraft:light_gray_concrete
fill 269 64 48 284 81 48 minecraft:light_gray_concrete
fill 269 64 48 269 81 68 minecraft:light_gray_concrete
setblock 270 64 67 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create_brass"}','{"text": "boiler"}','{"text": ""}']}}
setblock 271 64 67 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a four engine"}','{"text": "boiler with the"}','{"text": "goggles boiler"}','{"text": "overlay"}']}}
fill 279 64 48 279 81 68 minecraft:light_gray_concrete
kw testworld place shots:create/steam_engine 271 63 50 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
