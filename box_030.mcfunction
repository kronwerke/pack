# 030 create_trains/station
#area 264 42 285 67
fill 264 64 42 285 91 67 minecraft:air
fill 264 60 42 285 62 67 minecraft:stone
fill 264 63 42 285 63 67 minecraft:light_gray_concrete
fill 268 64 48 285 79 48 minecraft:light_gray_concrete
fill 268 64 48 268 79 61 minecraft:light_gray_concrete
setblock 269 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 270 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 280 64 48 280 79 61 minecraft:light_gray_concrete
fill 270 64 53 278 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 274 64 55 create:track_station
setblock 272 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 276 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 272 66 53 276 66 53 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
