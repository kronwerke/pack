# 004 start_here/s_locked
fill 63 63 6 74 63 19 minecraft:light_gray_concrete
fill 63 64 6 74 71 6 minecraft:light_gray_concrete
fill 63 64 6 63 71 19 minecraft:light_gray_concrete
setblock 64 64 18 minecraft:air
setblock 64 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "004"}','{"text": "start_here"}','{"text": "s_locked"}','{"text": ""}']}}
setblock 65 64 18 minecraft:air
setblock 65 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a veiled \\"???\\""}','{"text": "item with its"}','{"text": "three tooltip"}','{"text": "lines, and JEI"}']}}
setblock 66 64 18 minecraft:air
setblock 66 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with veiled"}','{"text": "stage 2 items"}','{"text": "Gesperrte Items"}','{"text": "im Inventar"}']}}
setblock 67 64 18 minecraft:air
setblock 67 64 18 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "zeigen, JEI"}','{"text": "offen"}','{"text": ""}','{"text": ""}']}}
summon text_display 68.5 71 11.5 {text:'[{"text": "004  ", "color": "gold"}, {"text": "start_here/s_locked", "color": "gray"}, {"text": "\\nErkenne gesperrte Gegenstände", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 65 64 9 minecraft:crafting_table
setblock 72 64 15 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:steel_casing",count:1},{Slot:1b,id:"botania:terrasteel_ingot",count:1},{Slot:2b,id:"ae2:controller",count:1}]}
