# 028 create/washing
fill 136 63 52 149 63 65 minecraft:light_gray_concrete
fill 136 64 52 149 71 52 minecraft:light_gray_concrete
fill 136 64 52 136 71 65 minecraft:light_gray_concrete
setblock 137 64 64 minecraft:air
setblock 137 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 138 64 64 minecraft:air
setblock 138 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
summon text_display 142.5 71 57.5 {text:'[{"text": "028  ", "color": "gold"}, {"text": "create/washing", "color": "gray"}, {"text": "\\nWasch Kies zu Eisen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/sand_washing 138 64 54 none
