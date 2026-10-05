# 115 botania/pool
fill 32 63 186 43 63 199 minecraft:light_gray_concrete
fill 32 64 186 43 71 186 minecraft:light_gray_concrete
fill 32 64 186 32 71 199 minecraft:light_gray_concrete
setblock 33 64 198 minecraft:air
setblock 33 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115"}','{"text": "botania"}','{"text": "pool"}','{"text": ""}']}}
setblock 34 64 198 minecraft:air
setblock 34 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full pool"}','{"text": "with a spreader"}','{"text": "beam, wand in"}','{"text": "hand"}']}}
summon text_display 37.5 71 191.5 {text:'[{"text": "115  ", "color": "gold"}, {"text": "botania/pool", "color": "gray"}, {"text": "\\nBau ein Manabecken", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 37 65 191 botania:mana_pool
setblock 37 64 191 botania:mana_void
setblock 37 65 188 botania:mana_spreader
setblock 39 65 191 botania:manastar
setblock 35 64 191 botania:endoflame
setblock 41 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1}]}
