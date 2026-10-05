# 162 hexerei/willow_broom
fill 330 63 242 341 63 255 minecraft:light_gray_concrete
fill 330 64 242 341 71 242 minecraft:light_gray_concrete
fill 330 64 242 330 71 255 minecraft:light_gray_concrete
setblock 331 64 254 minecraft:air
setblock 331 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162"}','{"text": "hexerei"}','{"text": "willow_broom"}','{"text": ""}']}}
setblock 332 64 254 minecraft:air
setblock 332 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "flying on a"}','{"text": "broom, plus the"}','{"text": "broom menu"}','{"text": "Auf dem Besen"}']}}
setblock 333 64 254 minecraft:air
setblock 333 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fliegen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 335.5 71 247.5 {text:'[{"text": "162  ", "color": "gold"}, {"text": "hexerei/willow_broom", "color": "gray"}, {"text": "\\nFlieg mit einem Weidenbesen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 339 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"hexerei:willow_broom",count:1}]}
