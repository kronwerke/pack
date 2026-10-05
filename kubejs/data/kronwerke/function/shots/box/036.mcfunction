# 036 create_brass/brass_mixing
fill 284 63 52 297 63 65 minecraft:light_gray_concrete
fill 284 64 52 297 71 52 minecraft:light_gray_concrete
fill 284 64 52 284 71 65 minecraft:light_gray_concrete
setblock 285 64 64 minecraft:air
setblock 285 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "create_brass"}','{"text": "brass_mixing"}','{"text": ""}']}}
setblock 286 64 64 minecraft:air
setblock 286 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "heated burner,"}','{"text": "basin and mixer"}','{"text": "stack"}','{"text": ""}']}}
summon text_display 290.5 71 57.5 {text:'[{"text": "036  ", "color": "gold"}, {"text": "create_brass/brass_mixing", "color": "gray"}, {"text": "\\nMisch Messing im heißen Becken", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/brass_mixing_2 286 64 54 none
