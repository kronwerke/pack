# 047 create_trains/unprocessed_sheet
fill 81 63 77 92 63 90 minecraft:light_gray_concrete
fill 81 64 77 92 71 77 minecraft:light_gray_concrete
fill 81 64 77 81 71 90 minecraft:light_gray_concrete
setblock 82 64 89 minecraft:air
setblock 82 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "create_trains"}','{"text": "unprocessed_sheet"}','{"text": ""}']}}
setblock 83 64 89 minecraft:air
setblock 83 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spout pouring"}','{"text": "lava on"}','{"text": "powdered"}','{"text": "obsidian"}']}}
summon text_display 86.5 71 82.5 {text:'[{"text": "047  ", "color": "gold"}, {"text": "create_trains/unprocessed_sheet", "color": "gray"}, {"text": "\\nGieß Lava auf das Pulver", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 86 64 82 create:depot
setblock 86 66 82 create:spout
setblock 86 67 82 create:creative_fluid_tank
setblock 90 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:powdered_obsidian",count:16},{Slot:1b,id:"minecraft:lava_bucket",count:1}]}
