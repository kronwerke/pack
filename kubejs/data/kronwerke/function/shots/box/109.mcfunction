# 109 ars_epic/linger
fill 397 63 148 408 63 161 minecraft:light_gray_concrete
fill 397 64 148 408 71 148 minecraft:light_gray_concrete
fill 397 64 148 397 71 161 minecraft:light_gray_concrete
setblock 398 64 160 minecraft:air
setblock 398 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109"}','{"text": "ars_epic"}','{"text": "linger"}','{"text": ""}']}}
setblock 399 64 160 minecraft:air
setblock 399 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a Linger field"}','{"text": "over mobs"}','{"text": "Linger-Zauber"}','{"text": "auf die Mobs"}']}}
summon text_display 402.5 71 153.5 {text:'[{"text": "109  ", "color": "gold"}, {"text": "ars_epic/linger", "color": "gray"}, {"text": "\\nLern Verweilen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 406 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:novice_spell_book",count:1}]}
summon minecraft:zombie 400.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:skeleton 403.5 64 155.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
