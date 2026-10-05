# 037 create_brass/incomplete
fill 301 63 52 316 63 65 minecraft:light_gray_concrete
fill 301 64 52 316 71 52 minecraft:light_gray_concrete
fill 301 64 52 301 71 65 minecraft:light_gray_concrete
setblock 302 64 64 minecraft:air
setblock 302 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "create_brass"}','{"text": "incomplete"}','{"text": ""}']}}
setblock 303 64 64 minecraft:air
setblock 303 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "belt with three"}','{"text": "deployers"}','{"text": "(cogwheel,"}','{"text": "tube, nugget)"}']}}
setblock 304 64 64 minecraft:air
setblock 304 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and a press"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 308.5 71 57.5 {text:'[{"text": "037  ", "color": "gold"}, {"text": "create_brass/incomplete", "color": "gray"}, {"text": "\\nLass ein Blech eine Runde drehen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/precision_mechanism_crafting 303 64 54 none
