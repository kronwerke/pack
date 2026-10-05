# 040 create_brass/crushing_wheel
fill 354 63 52 367 63 65 minecraft:light_gray_concrete
fill 354 64 52 367 71 52 minecraft:light_gray_concrete
fill 354 64 52 354 71 65 minecraft:light_gray_concrete
setblock 355 64 64 minecraft:air
setblock 355 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 356 64 64 minecraft:air
setblock 356 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 357 64 64 minecraft:air
setblock 357 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 360.5 71 57.5 {text:'[{"text": "040  ", "color": "gold"}, {"text": "create_brass/crushing_wheel", "color": "gray"}, {"text": "\\nBau Mahlwerkräder", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/crushing_wheel_crafting 356 64 54 none
