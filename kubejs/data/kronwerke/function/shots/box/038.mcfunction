# 038 create_brass/precision
fill 320 63 52 335 63 65 minecraft:light_gray_concrete
fill 320 64 52 335 71 52 minecraft:light_gray_concrete
fill 320 64 52 320 71 65 minecraft:light_gray_concrete
setblock 321 64 64 minecraft:air
setblock 321 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "create_brass"}','{"text": "precision"}','{"text": ""}']}}
setblock 322 64 64 minecraft:air
setblock 322 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the looped"}','{"text": "precision"}','{"text": "mechanism belt"}','{"text": "Schleife:"}']}}
setblock 323 64 64 minecraft:air
setblock 323 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Riemen zurück"}','{"text": "zum Anfang"}','{"text": ""}','{"text": ""}']}}
summon text_display 327.5 71 57.5 {text:'[{"text": "038  ", "color": "gold"}, {"text": "create_brass/precision", "color": "gray"}, {"text": "\\nBau ein Präzisionsgetriebe", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/precision_mechanism_crafting 322 64 54 none
