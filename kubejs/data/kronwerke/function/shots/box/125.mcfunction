# 125 botania_runes/plate_base
fill 188 63 186 199 63 199 minecraft:light_gray_concrete
fill 188 64 186 199 71 186 minecraft:light_gray_concrete
fill 188 64 186 188 71 199 minecraft:light_gray_concrete
setblock 189 64 198 minecraft:air
setblock 189 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 190 64 198 minecraft:air
setblock 190 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
summon text_display 193.5 71 191.5 {text:'[{"text": "125  ", "color": "gold"}, {"text": "botania_runes/plate_base", "color": "gray"}, {"text": "\\nLeg das Fundament", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:terra_plate 191 64 189 none
setblock 197 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:mana_spark",count:4},{Slot:1b,id:"botania:manasteel_ingot",count:1},{Slot:2b,id:"botania:mana_pearl",count:1},{Slot:3b,id:"botania:mana_diamond",count:1}]}
