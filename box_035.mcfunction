# 035 create_trains/station
#area 342 42 363 67
fill 342 64 42 363 91 67 minecraft:air
fill 342 60 42 363 62 67 minecraft:stone
fill 342 63 42 363 63 67 minecraft:light_gray_concrete
fill 346 64 48 363 79 48 minecraft:light_gray_concrete
fill 346 64 48 346 79 61 minecraft:light_gray_concrete
setblock 347 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 348 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 358 64 48 358 79 61 minecraft:light_gray_concrete
fill 348 64 53 356 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 352 64 55 create:track_station
setblock 350 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 354 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 350 66 53 354 66 53 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
