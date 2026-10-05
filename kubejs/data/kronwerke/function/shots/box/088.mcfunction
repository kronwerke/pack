# 088 ars_nouveau/scribes_table
fill 70 63 148 81 63 161 minecraft:light_gray_concrete
fill 70 64 148 81 71 148 minecraft:light_gray_concrete
fill 70 64 148 70 71 161 minecraft:light_gray_concrete
setblock 71 64 160 minecraft:air
setblock 71 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "ars_nouveau"}','{"text": "scribes_table"}','{"text": ""}']}}
setblock 72 64 160 minecraft:air
setblock 72 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the glyph"}','{"text": "selection"}','{"text": "screen with"}','{"text": "ingredients"}']}}
setblock 73 64 160 minecraft:air
setblock 73 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over the table"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 75.5 71 153.5 {text:'[{"text": "088  ", "color": "gold"}, {"text": "ars_nouveau/scribes_table", "color": "gray"}, {"text": "\\nBau den Tisch des Schreibers", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 72 64 151 ars_nouveau:scribes_table
setblock 79 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:novice_spell_book",count:1},{Slot:1b,id:"ars_nouveau:blank_parchment",count:8}]}
