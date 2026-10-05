# 032 create/cobble_gen
fill 202 63 52 213 63 65 minecraft:light_gray_concrete
fill 202 64 52 213 71 52 minecraft:light_gray_concrete
fill 202 64 52 202 71 65 minecraft:light_gray_concrete
setblock 203 64 64 minecraft:air
setblock 203 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 204 64 64 minecraft:air
setblock 204 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
summon text_display 207.5 71 57.5 {text:'[{"text": "032  ", "color": "gold"}, {"text": "create/cobble_gen", "color": "gray"}, {"text": "\\nBau einen Bruchsteingenerator", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 205 64 56 minecraft:glass
setblock 205 64 58 minecraft:glass
setblock 206 64 56 minecraft:glass
setblock 206 64 58 minecraft:glass
setblock 207 64 56 minecraft:glass
setblock 207 64 58 minecraft:glass
setblock 208 64 56 minecraft:glass
setblock 208 64 58 minecraft:glass
setblock 209 64 56 minecraft:glass
setblock 209 64 58 minecraft:glass
setblock 205 64 57 minecraft:glass
setblock 209 64 57 minecraft:glass
fill 205 63 56 209 63 58 minecraft:glass
setblock 206 64 57 minecraft:water
setblock 207 64 57 minecraft:cobblestone
setblock 208 64 57 minecraft:lava
setblock 207 64 58 create:mechanical_drill[facing=north]
setblock 207 64 59 create:shaft[axis=z]
setblock 207 64 60 create:creative_motor[facing=north]{ScrollValue:64}
