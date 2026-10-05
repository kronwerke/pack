# 136 alfheim/elementium_line
fill 393 63 186 408 63 201 minecraft:light_gray_concrete
fill 393 64 186 408 71 186 minecraft:light_gray_concrete
fill 393 64 186 393 71 201 minecraft:light_gray_concrete
setblock 394 64 200 minecraft:air
setblock 394 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136"}','{"text": "alfheim"}','{"text": "elementium_line"}','{"text": ""}']}}
setblock 395 64 200 minecraft:air
setblock 395 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an automated"}','{"text": "manasteel block"}','{"text": "line into the"}','{"text": "portal"}']}}
summon text_display 400.5 71 192.5 {text:'[{"text": "136  ", "color": "gold"}, {"text": "alfheim/elementium_line", "color": "gray"}, {"text": "\\nBau eine Elementium-Straße", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:alfheim_portal 397 64 190 none
setblock 395 64 195 botania:mana_pool
setblock 404 64 195 botania:mana_pool
setblock 395 65 195 botania:natura_pylon
setblock 404 65 195 botania:natura_pylon
setblock 406 64 197 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:wand_of_the_forest",count:1},{Slot:1b,id:"botania:manasteel_block",count:8},{Slot:2b,id:"botania:livingwood",count:8}]}
