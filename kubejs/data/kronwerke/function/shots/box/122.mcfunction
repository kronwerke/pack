# 122 botania_runes/runic_altar
fill 141 63 186 152 63 199 minecraft:light_gray_concrete
fill 141 64 186 152 71 186 minecraft:light_gray_concrete
fill 141 64 186 141 71 199 minecraft:light_gray_concrete
setblock 142 64 198 minecraft:air
setblock 142 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122"}','{"text": "botania_runes"}','{"text": "runic_altar"}','{"text": ""}']}}
setblock 143 64 198 minecraft:air
setblock 143 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "altar with"}','{"text": "ingredients, a"}','{"text": "spreader aimed"}','{"text": "at it, wand HUD"}']}}
summon text_display 146.5 71 191.5 {text:'[{"text": "122  ", "color": "gold"}, {"text": "botania_runes/runic_altar", "color": "gray"}, {"text": "\\nBau den Runenaltar", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 146 64 191 botania:runic_altar
setblock 146 64 188 botania:mana_spreader
setblock 146 64 194 botania:mana_pool
setblock 150 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1},{Slot:1b,id:"botania:manasteel_ingot",count:4},{Slot:2b,id:"botania:mana_powder",count:4},{Slot:3b,id:"botania:livingrock",count:1}]}
