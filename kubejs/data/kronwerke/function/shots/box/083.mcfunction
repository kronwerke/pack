# 083 antimatter/wind
fill 0 63 129 11 63 142 minecraft:light_gray_concrete
fill 0 64 129 11 71 129 minecraft:light_gray_concrete
fill 0 64 129 0 71 142 minecraft:light_gray_concrete
setblock 1 64 141 minecraft:air
setblock 1 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "antimatter"}','{"text": "wind"}','{"text": ""}']}}
setblock 2 64 141 minecraft:air
setblock 2 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the large wind"}','{"text": "generator"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 134.5 {text:'[{"text": "083  ", "color": "gold"}, {"text": "antimatter/wind", "color": "gray"}, {"text": "\\nStell einen Großen Windgenerator auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 5 64 134 mekanismgenerators:wind_generator
