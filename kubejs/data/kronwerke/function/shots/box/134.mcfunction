# 134 alfheim/frame
fill 355 63 186 370 63 201 minecraft:light_gray_concrete
fill 355 64 186 370 71 186 minecraft:light_gray_concrete
fill 355 64 186 355 71 201 minecraft:light_gray_concrete
setblock 356 64 200 minecraft:air
setblock 356 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 357 64 200 minecraft:air
setblock 357 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
summon text_display 362.5 71 192.5 {text:'[{"text": "134  ", "color": "gold"}, {"text": "alfheim/frame", "color": "gray"}, {"text": "\\nStell Rahmen und Pylonen auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:alfheim_portal 359 64 190 none
setblock 357 64 195 botania:mana_pool
setblock 366 64 195 botania:mana_pool
setblock 357 65 195 botania:natura_pylon
setblock 366 65 195 botania:natura_pylon
setblock 368 64 197 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1},{Slot:1b,id:"botania:manasteel_block",count:8},{Slot:2b,id:"botania:livingwood",count:8}]}
