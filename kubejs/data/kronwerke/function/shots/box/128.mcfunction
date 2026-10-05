# 128 botania_runes/rune_core
fill 233 63 186 244 63 199 minecraft:light_gray_concrete
fill 233 64 186 244 71 186 minecraft:light_gray_concrete
fill 233 64 186 233 71 199 minecraft:light_gray_concrete
setblock 234 64 198 minecraft:air
setblock 234 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128"}','{"text": "botania_runes"}','{"text": "rune_core"}','{"text": ""}']}}
setblock 235 64 198 minecraft:air
setblock 235 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the crafting"}','{"text": "grid"}','{"text": ""}','{"text": ""}']}}
summon text_display 238.5 71 191.5 {text:'[{"text": "128  ", "color": "gold"}, {"text": "botania_runes/rune_core", "color": "gray"}, {"text": "\\nCrafte einen Runenkern", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 235 64 189 minecraft:crafting_table
setblock 242 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:rune_of_mana",count:1}]}
