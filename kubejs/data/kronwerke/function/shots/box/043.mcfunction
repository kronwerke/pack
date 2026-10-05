# 043 create_brass/arm
fill 405 63 52 416 63 65 minecraft:light_gray_concrete
fill 405 64 52 416 71 52 minecraft:light_gray_concrete
fill 405 64 52 405 71 65 minecraft:light_gray_concrete
setblock 406 64 64 minecraft:air
setblock 406 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 407 64 64 minecraft:air
setblock 407 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": "Arm: Truhe als"}']}}
setblock 408 64 64 minecraft:air
setblock 408 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Eingang,"}','{"text": "Brenner als"}','{"text": "Ziel"}','{"text": ""}']}}
summon text_display 410.5 71 57.5 {text:'[{"text": "043  ", "color": "gold"}, {"text": "create_brass/arm", "color": "gray"}, {"text": "\\nLass den Mechanischen Arm greifen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 409 64 57 create:mechanical_arm
setblock 411 64 57 create:blaze_burner
setblock 407 64 57 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
