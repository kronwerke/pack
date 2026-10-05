# 169 immersive/blast_furnace, improved_form
fill 80 63 273 101 63 286 minecraft:light_gray_concrete
fill 80 64 273 101 71 273 minecraft:light_gray_concrete
fill 80 64 273 80 71 286 minecraft:light_gray_concrete
setblock 81 64 285 minecraft:air
setblock 81 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "169.1"}','{"text": "immersive"}','{"text": "blast_furnace"}','{"text": ""}']}}
setblock 82 64 285 minecraft:air
setblock 82 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crude blast"}','{"text": "furnace GUI,"}','{"text": "improved"}','{"text": "furnace with"}']}}
setblock 83 64 285 minecraft:air
setblock 83 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hopper and"}','{"text": "preheaters"}','{"text": "Mit dem Hammer"}','{"text": "formen"}']}}
summon text_display 85.5 71 278.5 {text:'[{"text": "169.1  ", "color": "gold"}, {"text": "immersive/blast_furnace", "color": "gray"}, {"text": "\\nForm einen Roh-Hochofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/blast_furnace 82 64 275 none
setblock 89 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
setblock 91 64 285 minecraft:air
setblock 91 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "169.2"}','{"text": "immersive"}','{"text": "improved_form"}','{"text": ""}']}}
setblock 92 64 285 minecraft:air
setblock 92 64 285 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mit dem Hammer"}','{"text": "formen"}','{"text": ""}','{"text": ""}']}}
summon text_display 95.5 71 278.5 {text:'[{"text": "169.2  ", "color": "gold"}, {"text": "immersive/improved_form", "color": "gray"}, {"text": "\\nForm einen Verbesserten Hochofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template immersiveengineering:multiblocks/improved_blast_furnace 92 64 275 none
setblock 99 64 282 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
