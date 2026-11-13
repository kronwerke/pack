# 034 create_trains/station
#area 344 42 365 67
fill 344 64 42 365 91 67 minecraft:air
fill 344 60 42 365 62 67 minecraft:stone
fill 344 63 42 365 63 67 minecraft:light_gray_concrete
fill 348 64 48 365 79 48 minecraft:light_gray_concrete
fill 348 64 48 348 79 61 minecraft:light_gray_concrete
setblock 349 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 350 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 360 64 48 360 79 61 minecraft:light_gray_concrete
fill 350 64 53 358 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 354 64 55 create:track_station
setblock 352 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 356 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 352 66 53 356 66 53 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
