# 038 create_trains/station
#area 359 44 380 69
fill 359 64 44 380 91 69 minecraft:air
fill 359 60 44 380 62 69 minecraft:stone
fill 359 63 44 380 63 69 minecraft:light_gray_concrete
fill 363 64 50 380 79 50 minecraft:light_gray_concrete
fill 363 64 50 363 79 63 minecraft:light_gray_concrete
setblock 364 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 365 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 375 64 50 375 79 63 minecraft:light_gray_concrete
fill 365 64 55 373 64 55 create:track[shape=xo,turn=false,waterlogged=false]
setblock 369 64 57 create:track_station
setblock 367 65 55 create:small_bogey[axis=x,waterlogged=false]
setblock 371 65 55 create:small_bogey[axis=x,waterlogged=false]
fill 367 66 55 371 66 55 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
