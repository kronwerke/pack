# 087 ars_nouveau/first_spell
fill 55 63 148 66 63 161 minecraft:light_gray_concrete
fill 55 64 148 66 71 148 minecraft:light_gray_concrete
fill 55 64 148 55 71 161 minecraft:light_gray_concrete
setblock 56 64 160 minecraft:air
setblock 56 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "ars_nouveau"}','{"text": "first_spell"}','{"text": ""}']}}
setblock 57 64 160 minecraft:air
setblock 57 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the spell book"}','{"text": "GUI with"}','{"text": "Projectile and"}','{"text": "Break"}']}}
setblock 58 64 160 minecraft:air
setblock 58 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Buch offen:"}','{"text": "Projectile und"}','{"text": "Break"}','{"text": ""}']}}
summon text_display 60.5 71 153.5 {text:'[{"text": "087  ", "color": "gold"}, {"text": "ars_nouveau/first_spell", "color": "gray"}, {"text": "\\nWirk deinen ersten Zauber", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 57 64 151 ars_nouveau:scribes_table
setblock 64 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:novice_spell_book",count:1}]}
