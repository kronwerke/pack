# 046 create_trains/welcome
fill 62 63 77 77 63 90 minecraft:light_gray_concrete
fill 62 64 77 77 71 77 minecraft:light_gray_concrete
fill 62 64 77 62 71 90 minecraft:light_gray_concrete
setblock 63 64 89 minecraft:air
setblock 63 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "create_trains"}','{"text": "welcome"}','{"text": ""}']}}
setblock 64 64 89 minecraft:air
setblock 64 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the track"}','{"text": "assembly belt"}','{"text": ""}','{"text": ""}']}}
summon text_display 69.5 71 82.5 {text:'[{"text": "046  ", "color": "gold"}, {"text": "create_trains/welcome", "color": "gray"}, {"text": "\\nMontier deine ersten Gleise", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/track_crafting 64 64 79 none
