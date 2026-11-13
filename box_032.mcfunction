# 032 create_trains/postbox
#area 298 42 319 67
fill 298 64 42 319 91 67 minecraft:air
fill 298 60 42 319 62 67 minecraft:stone
fill 298 63 42 319 63 67 minecraft:light_gray_concrete
fill 302 64 48 319 79 48 minecraft:light_gray_concrete
fill 302 64 48 302 79 61 minecraft:light_gray_concrete
setblock 303 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 304 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 314 64 48 314 79 61 minecraft:light_gray_concrete
fill 304 64 53 312 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 308 64 55 create:track_station
setblock 310 64 55 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
