# 116 botania/manastar
fill 47 63 186 58 63 199 minecraft:light_gray_concrete
fill 47 64 186 58 71 186 minecraft:light_gray_concrete
fill 47 64 186 47 71 199 minecraft:light_gray_concrete
setblock 48 64 198 minecraft:air
setblock 48 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 49 64 198 minecraft:air
setblock 49 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
summon text_display 52.5 71 191.5 {text:'[{"text": "116  ", "color": "gold"}, {"text": "botania/manastar", "color": "gray"}, {"text": "\\nPflanz einen Manastern", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 52 65 191 botania:mana_pool
setblock 52 64 191 botania:mana_void
setblock 52 65 188 botania:mana_spreader
setblock 54 65 191 botania:manastar
setblock 50 64 191 botania:endoflame
setblock 56 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1}]}
