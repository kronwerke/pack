# 110 ars_epic/elevator
fill 0 63 167 11 63 180 minecraft:light_gray_concrete
fill 0 64 167 11 71 167 minecraft:light_gray_concrete
fill 0 64 167 0 71 180 minecraft:light_gray_concrete
setblock 1 64 179 minecraft:air
setblock 1 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "ars_epic"}','{"text": "elevator"}','{"text": ""}']}}
setblock 2 64 179 minecraft:air
setblock 2 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "slipstream"}','{"text": "elevator in use"}','{"text": "Slipstream-Aufzug"}','{"text": "im Spiel"}']}}
setblock 3 64 179 minecraft:air
setblock 3 64 179 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "zaubern"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 172.5 {text:'[{"text": "110  ", "color": "gold"}, {"text": "ars_epic/elevator", "color": "gray"}, {"text": "\\nBau einen Windstrom-Aufzug", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 9 64 176 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"ars_nouveau:novice_spell_book",count:1}]}
