# 029 create/belt
fill 153 63 52 164 63 65 minecraft:light_gray_concrete
fill 153 64 52 164 71 52 minecraft:light_gray_concrete
fill 153 64 52 153 71 65 minecraft:light_gray_concrete
setblock 154 64 64 minecraft:air
setblock 154 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create"}','{"text": "belt"}','{"text": ""}']}}
setblock 155 64 64 minecraft:air
setblock 155 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt between"}','{"text": "two shafts"}','{"text": "Riemen zwischen"}','{"text": "die zwei Wellen"}']}}
setblock 156 64 64 minecraft:air
setblock 156 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 158.5 71 57.5 {text:'[{"text": "029  ", "color": "gold"}, {"text": "create/belt", "color": "gray"}, {"text": "\\nSpann ein Förderband", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 155 64 55 create:shaft[axis=x]
setblock 157 64 55 create:shaft[axis=x]
setblock 162 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:belt_connector",count:1}]}
