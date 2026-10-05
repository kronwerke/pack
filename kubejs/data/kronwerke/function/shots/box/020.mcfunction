# 020 create/welcome
fill 0 63 52 11 63 65 minecraft:light_gray_concrete
fill 0 64 52 11 71 52 minecraft:light_gray_concrete
fill 0 64 52 0 71 65 minecraft:light_gray_concrete
setblock 1 64 64 minecraft:air
setblock 1 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 64 minecraft:air
setblock 2 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Ponder view"}','{"text": "opened with W"}','{"text": "over a cogwheel"}','{"text": "W gedrückt"}']}}
setblock 3 64 64 minecraft:air
setblock 3 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "halten über dem"}','{"text": "Zahnrad"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 57.5 {text:'[{"text": "020  ", "color": "gold"}, {"text": "create/welcome", "color": "gray"}, {"text": "\\nFang mit Create an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 2 64 55 create:cogwheel[axis=y]
