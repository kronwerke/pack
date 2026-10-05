# 179 immersive_heavy/hv, duroplast, survey
fill 177 63 292 214 63 305 minecraft:light_gray_concrete
fill 177 64 292 214 71 292 minecraft:light_gray_concrete
fill 177 64 292 177 71 305 minecraft:light_gray_concrete
setblock 178 64 304 minecraft:air
setblock 178 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "179.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 179 64 304 minecraft:air
setblock 179 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 180 64 304 minecraft:air
setblock 180 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
summon text_display 185.5 71 297.5 {text:'[{"text": "179.1  ", "color": "gold"}, {"text": "immersive_heavy/hv", "color": "gray"}, {"text": "\\nSpann HV-Draht", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 179 64 297 179 67 297 immersiveengineering:steel_post
setblock 179 68 297 immersiveengineering:connector_hv
fill 190 64 297 190 67 297 immersiveengineering:steel_post
setblock 190 68 297 immersiveengineering:connector_hv
setblock 192 64 301 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:wirecoil_steel",count:8}]}
setblock 194 64 304 minecraft:air
setblock 194 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "179.2"}','{"text": "immersive_heavy"}','{"text": "duroplast"}','{"text": ""}']}}
setblock 195 64 304 minecraft:air
setblock 195 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}','{"text": ""}']}}
summon text_display 198.5 71 297.5 {text:'[{"text": "179.2  ", "color": "gold"}, {"text": "immersive_heavy/duroplast", "color": "gray"}, {"text": "\\nGieß Duroplastplatten", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/bottling_machine 195 64 294 none
setblock 202 64 301 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 204 64 304 minecraft:air
setblock 204 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "179.3"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 205 64 304 minecraft:air
setblock 205 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Kernprobe auf"}','{"text": "den Boden legen"}','{"text": ""}','{"text": ""}']}}
summon text_display 208.5 71 297.5 {text:'[{"text": "179.3  ", "color": "gold"}, {"text": "immersive_heavy/survey", "color": "gray"}, {"text": "\\nSuch eine Mineralader", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 212 64 301 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:coresample",count:1}]}
