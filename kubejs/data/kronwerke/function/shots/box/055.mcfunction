# 055 create_trains/postbox
fill 235 63 77 246 63 90 minecraft:light_gray_concrete
fill 235 64 77 246 71 77 minecraft:light_gray_concrete
fill 235 64 77 235 71 90 minecraft:light_gray_concrete
setblock 236 64 89 minecraft:air
setblock 236 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "create_trains"}','{"text": "postbox"}','{"text": ""}']}}
setblock 237 64 89 minecraft:air
setblock 237 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a postbox next"}','{"text": "to a station"}','{"text": ""}','{"text": ""}']}}
summon text_display 240.5 71 82.5 {text:'[{"text": "055  ", "color": "gold"}, {"text": "create_trains/postbox", "color": "gray"}, {"text": "\\nSchick Pakete per Zug", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 236 63 81 244 63 81 minecraft:gravel
fill 236 64 81 244 64 81 create:track[shape=xo]
setblock 240 64 82 create:track_station
setblock 241 64 82 create:white_postbox
