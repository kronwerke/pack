# 126 botania_runes/terrasteel
fill 203 63 186 214 63 199 minecraft:light_gray_concrete
fill 203 64 186 214 71 186 minecraft:light_gray_concrete
fill 203 64 186 203 71 199 minecraft:light_gray_concrete
setblock 204 64 198 minecraft:air
setblock 204 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 205 64 198 minecraft:air
setblock 205 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
summon text_display 208.5 71 191.5 {text:'[{"text": "126  ", "color": "gold"}, {"text": "botania_runes/terrasteel", "color": "gray"}, {"text": "\\nSchmied Terrastahl", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:terra_plate 206 64 189 none
setblock 212 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:mana_spark",count:4},{Slot:1b,id:"botania:manasteel_ingot",count:1},{Slot:2b,id:"botania:mana_pearl",count:1},{Slot:3b,id:"botania:mana_diamond",count:1}]}
