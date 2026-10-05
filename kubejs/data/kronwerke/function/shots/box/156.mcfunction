# 156 hexerei/herbs
fill 240 63 242 251 63 255 minecraft:light_gray_concrete
fill 240 64 242 251 71 242 minecraft:light_gray_concrete
fill 240 64 242 240 71 255 minecraft:light_gray_concrete
setblock 241 64 254 minecraft:air
setblock 241 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156"}','{"text": "hexerei"}','{"text": "herbs"}','{"text": ""}']}}
setblock 242 64 254 minecraft:air
setblock 242 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "herb garden"}','{"text": "with all four"}','{"text": "plants grown"}','{"text": ""}']}}
summon text_display 245.5 71 247.5 {text:'[{"text": "156  ", "color": "gold"}, {"text": "hexerei/herbs", "color": "gray"}, {"text": "\\nGrab die vier Hexenkräuter aus", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 242 63 245 248 63 248 minecraft:farmland
fill 242 64 245 242 64 248 hexerei:mandrake_plant[age=3]
fill 244 64 245 244 64 248 hexerei:belladonna_plant[age=3]
fill 246 64 245 246 64 248 hexerei:mugwort_bush[age=3,half=lower]
fill 246 65 245 246 65 248 hexerei:mugwort_bush[age=3,half=upper]
fill 248 64 245 248 64 248 hexerei:yellow_dock_bush[age=3,half=lower]
fill 248 65 245 248 65 248 hexerei:yellow_dock_bush[age=3,half=upper]
