# 031 create_trains/postbox
#area 281 42 302 67
fill 281 64 42 302 91 67 minecraft:air
fill 281 60 42 302 62 67 minecraft:stone
fill 281 63 42 302 63 67 minecraft:light_gray_concrete
fill 285 64 48 302 79 48 minecraft:light_gray_concrete
fill 285 64 48 285 79 61 minecraft:light_gray_concrete
setblock 286 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 287 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 297 64 48 297 79 61 minecraft:light_gray_concrete
fill 287 64 53 295 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 291 64 55 create:track_station
setblock 293 64 55 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
