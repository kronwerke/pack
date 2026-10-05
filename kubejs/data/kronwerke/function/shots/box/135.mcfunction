# 135 alfheim/open
fill 374 63 186 389 63 201 minecraft:light_gray_concrete
fill 374 64 186 389 71 186 minecraft:light_gray_concrete
fill 374 64 186 374 71 201 minecraft:light_gray_concrete
setblock 375 64 200 minecraft:air
setblock 375 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 376 64 200 minecraft:air
setblock 376 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
summon text_display 381.5 71 192.5 {text:'[{"text": "135  ", "color": "gold"}, {"text": "alfheim/open", "color": "gray"}, {"text": "\\nÖffne das Portal", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:alfheim_portal 378 64 190 none
setblock 376 64 195 botania:mana_pool
setblock 385 64 195 botania:mana_pool
setblock 376 65 195 botania:natura_pylon
setblock 385 65 195 botania:natura_pylon
setblock 387 64 197 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1},{Slot:1b,id:"botania:manasteel_block",count:8},{Slot:2b,id:"botania:livingwood",count:8}]}
