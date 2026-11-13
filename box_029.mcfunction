# 029 create_trains/postbox
#area 266 42 287 67
fill 266 64 42 287 91 67 minecraft:air
fill 266 60 42 287 62 67 minecraft:stone
fill 266 63 42 287 63 67 minecraft:light_gray_concrete
fill 270 64 48 287 79 48 minecraft:light_gray_concrete
fill 270 64 48 270 79 61 minecraft:light_gray_concrete
setblock 271 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 272 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 282 64 48 282 79 61 minecraft:light_gray_concrete
fill 272 64 53 280 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 276 64 55 create:track_station
setblock 278 64 55 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
