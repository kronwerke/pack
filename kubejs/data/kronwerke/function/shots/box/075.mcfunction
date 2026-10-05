# 075 mekanism_elite/induction_matrix
fill 298 63 108 309 63 121 minecraft:light_gray_concrete
fill 298 64 108 309 71 108 minecraft:light_gray_concrete
fill 298 64 108 298 71 121 minecraft:light_gray_concrete
setblock 299 64 120 minecraft:air
setblock 299 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "mekanism_elite"}','{"text": "induction_matrix"}','{"text": ""}']}}
setblock 300 64 120 minecraft:air
setblock 300 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "matrix with"}','{"text": "cells and"}','{"text": "providers"}','{"text": "behind glass,"}']}}
setblock 301 64 120 minecraft:air
setblock 301 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "port GUI"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 303.5 71 113.5 {text:'[{"text": "075  ", "color": "gold"}, {"text": "mekanism_elite/induction_matrix", "color": "gray"}, {"text": "\\nSetz die Induktionsmatrix zusammen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 301 64 111 305 68 115 mekanism:induction_casing
fill 302 65 112 304 67 114 mekanism:basic_induction_cell
setblock 303 66 113 mekanism:basic_induction_provider
fill 301 65 115 305 67 115 mekanism:structural_glass
setblock 303 64 115 mekanism:induction_port
