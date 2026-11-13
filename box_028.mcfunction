# 028 create_trains/station
#area 249 42 270 67
fill 249 64 42 270 91 67 minecraft:air
fill 249 60 42 270 62 67 minecraft:stone
fill 249 63 42 270 63 67 minecraft:light_gray_concrete
fill 253 64 48 270 79 48 minecraft:light_gray_concrete
fill 253 64 48 253 79 61 minecraft:light_gray_concrete
setblock 254 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 255 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": ""}']}}
fill 265 64 48 265 79 61 minecraft:light_gray_concrete
fill 255 64 53 263 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 259 64 55 create:track_station
setblock 257 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 261 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 257 66 53 261 66 53 create:railway_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
