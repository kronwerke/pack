# 044 create_trains/postbox
#area 61 70 82 95
fill 61 64 70 82 91 95 minecraft:air
fill 61 60 70 82 62 95 minecraft:stone
fill 61 63 70 82 63 95 minecraft:light_gray_concrete
fill 65 64 76 82 79 76 minecraft:light_gray_concrete
fill 65 64 76 65 79 89 minecraft:light_gray_concrete
setblock 66 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 67 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
fill 77 64 76 77 79 89 minecraft:light_gray_concrete
fill 67 64 81 75 64 81 create:track[shape=xo,turn=false,waterlogged=false]
setblock 71 64 83 create:track_station
setblock 73 64 83 create:white_postbox[facing=south,open=false,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
