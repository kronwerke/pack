# 021 create/water_wheel
fill 15 63 52 28 63 65 minecraft:light_gray_concrete
fill 15 64 52 28 71 52 minecraft:light_gray_concrete
fill 15 64 52 15 71 65 minecraft:light_gray_concrete
setblock 16 64 64 minecraft:air
setblock 16 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 17 64 64 minecraft:air
setblock 17 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 18 64 64 minecraft:air
setblock 18 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 21.5 71 57.5 {text:'[{"text": "021  ", "color": "gold"}, {"text": "create/water_wheel", "color": "gray"}, {"text": "\\nStell ein Wasserrad in den Bach", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 18 65 57 create:water_wheel[facing=east]
setblock 19 65 57 create:water_wheel[facing=east]
setblock 20 65 57 create:water_wheel[facing=east]
setblock 21 65 57 create:water_wheel[facing=east]
fill 17 64 56 23 64 58 minecraft:stone
fill 17 67 56 22 67 58 minecraft:stone
fill 17 68 56 22 68 58 minecraft:stone
fill 18 68 57 21 68 57 minecraft:water
setblock 22 65 57 create:shaft[axis=x]
