# 033 create/tree_farm
fill 217 63 52 232 63 65 minecraft:light_gray_concrete
fill 217 64 52 232 71 52 minecraft:light_gray_concrete
fill 217 64 52 217 71 65 minecraft:light_gray_concrete
setblock 218 64 64 minecraft:air
setblock 218 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "create"}','{"text": "tree_farm"}','{"text": ""}']}}
setblock 219 64 64 minecraft:air
setblock 219 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "radial chassis"}','{"text": "saw wheel"}','{"text": "cutting a row"}','{"text": "of trees"}']}}
setblock 220 64 64 minecraft:air
setblock 220 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lager oder"}','{"text": "Kolben davor,"}','{"text": "Kleber auf das"}','{"text": "Chassis"}']}}
summon text_display 224.5 71 57.5 {text:'[{"text": "033  ", "color": "gold"}, {"text": "create/tree_farm", "color": "gray"}, {"text": "\\nFäll Bäume mit einem Sägerad", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 221 64 55 221 67 55 minecraft:oak_log
fill 220 67 54 222 68 56 minecraft:oak_leaves[persistent=true]
fill 223 64 55 223 67 55 minecraft:oak_log
fill 222 67 54 224 68 56 minecraft:oak_leaves[persistent=true]
fill 225 64 55 225 67 55 minecraft:oak_log
fill 224 67 54 226 68 56 minecraft:oak_leaves[persistent=true]
fill 227 64 55 227 67 55 minecraft:oak_log
fill 226 67 54 228 68 56 minecraft:oak_leaves[persistent=true]
fill 220 64 57 228 64 57 create:radial_chassis[axis=x]
setblock 221 64 56 create:mechanical_saw[facing=north]
setblock 223 64 56 create:mechanical_saw[facing=north]
setblock 225 64 56 create:mechanical_saw[facing=north]
setblock 227 64 56 create:mechanical_saw[facing=north]
