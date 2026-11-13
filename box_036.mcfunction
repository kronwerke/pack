# 036 create_trains/station
#area 359 42 380 67
fill 359 64 42 380 91 67 minecraft:air
fill 359 60 42 380 62 67 minecraft:stone
fill 359 63 42 380 63 67 minecraft:light_gray_concrete
fill 363 64 48 380 79 48 minecraft:light_gray_concrete
fill 363 64 48 363 79 61 minecraft:light_gray_concrete
setblock 364 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 365 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 375 64 48 375 79 61 minecraft:light_gray_concrete
fill 365 64 53 373 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 369 64 55 create:track_station
setblock 367 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 371 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 367 66 53 371 66 53 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
