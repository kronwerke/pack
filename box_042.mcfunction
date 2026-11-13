# 042 create_trains/postbox
#area 61 68 82 93
fill 61 64 68 82 91 93 minecraft:air
fill 61 60 68 82 62 93 minecraft:stone
fill 61 63 68 82 63 93 minecraft:light_gray_concrete
fill 65 64 74 82 79 74 minecraft:light_gray_concrete
fill 65 64 74 65 79 87 minecraft:light_gray_concrete
setblock 66 64 86 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 67 64 86 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 77 64 74 77 79 87 minecraft:light_gray_concrete
fill 67 64 79 75 64 79 create:track[shape=xo,turn=false,waterlogged=false]
setblock 71 64 81 create:track_station
setblock 73 64 81 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
