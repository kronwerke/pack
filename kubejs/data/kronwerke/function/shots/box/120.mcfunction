# 120 botania_runes/mana_pearl
fill 111 63 186 122 63 199 minecraft:light_gray_concrete
fill 111 64 186 122 71 186 minecraft:light_gray_concrete
fill 111 64 186 111 71 199 minecraft:light_gray_concrete
setblock 112 64 198 minecraft:air
setblock 112 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 198 minecraft:air
setblock 113 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
summon text_display 116.5 71 191.5 {text:'[{"text": "120  ", "color": "gold"}, {"text": "botania_runes/mana_pearl", "color": "gray"}, {"text": "\\nInfundiere Manaperlen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 116 64 191 create:brass_casing
setblock 116 65 191 botania:mana_pool
setblock 116 65 188 botania:mana_spreader
