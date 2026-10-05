# 039 create_brass/crafter
fill 339 63 52 350 63 65 minecraft:light_gray_concrete
fill 339 64 52 350 71 52 minecraft:light_gray_concrete
fill 339 64 52 339 71 65 minecraft:light_gray_concrete
setblock 340 64 64 minecraft:air
setblock 340 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 341 64 64 minecraft:air
setblock 341 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
summon text_display 344.5 71 57.5 {text:'[{"text": "039  ", "color": "gold"}, {"text": "create_brass/crafter", "color": "gray"}, {"text": "\\nStell Mechanische Handwerkseinheiten auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 343 64 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 343 65 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 343 66 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 344 64 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 344 65 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 344 66 57 create:mechanical_crafter[facing=south,pointing=right]
setblock 345 64 57 create:mechanical_crafter[facing=south,pointing=down]
setblock 345 65 57 create:mechanical_crafter[facing=south,pointing=down]
setblock 345 66 57 create:mechanical_crafter[facing=south,pointing=down]
