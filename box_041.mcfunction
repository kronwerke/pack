# 041 create_trains/postbox
#area 39 68 60 93
fill 39 64 68 60 91 93 minecraft:air
fill 39 60 68 60 62 93 minecraft:stone
fill 39 63 68 60 63 93 minecraft:light_gray_concrete
fill 43 64 74 60 79 74 minecraft:light_gray_concrete
fill 43 64 74 43 79 87 minecraft:light_gray_concrete
setblock 44 64 86 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 45 64 86 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 55 64 74 55 79 87 minecraft:light_gray_concrete
fill 45 64 79 53 64 79 create:track[shape=xo,turn=false,waterlogged=false]
setblock 49 64 81 create:track_station
setblock 51 64 81 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
