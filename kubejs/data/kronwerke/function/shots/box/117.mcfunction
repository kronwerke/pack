# 117 botania/mana_void
fill 62 63 186 73 63 199 minecraft:light_gray_concrete
fill 62 64 186 73 71 186 minecraft:light_gray_concrete
fill 62 64 186 62 71 199 minecraft:light_gray_concrete
setblock 63 64 198 minecraft:air
setblock 63 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117"}','{"text": "botania"}','{"text": "mana_void"}','{"text": ""}']}}
setblock 64 64 198 minecraft:air
setblock 64 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mana void"}','{"text": "under a pool"}','{"text": ""}','{"text": ""}']}}
summon text_display 67.5 71 191.5 {text:'[{"text": "117  ", "color": "gold"}, {"text": "botania/mana_void", "color": "gray"}, {"text": "\\nBau eine Manaleere", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 67 65 191 botania:mana_pool
setblock 67 64 191 botania:mana_void
setblock 67 65 188 botania:mana_spreader
setblock 69 65 191 botania:manastar
setblock 65 64 191 botania:endoflame
setblock 71 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1}]}
