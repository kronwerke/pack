# 018 farms/mana_endoflame
fill 130 63 31 143 63 44 minecraft:light_gray_concrete
fill 130 64 31 143 71 31 minecraft:light_gray_concrete
fill 130 64 31 130 71 44 minecraft:light_gray_concrete
setblock 131 64 43 minecraft:air
setblock 131 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "farms"}','{"text": "mana_endoflame"}','{"text": ""}']}}
setblock 132 64 43 minecraft:air
setblock 132 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Endoflame ring,"}','{"text": "spreader, open"}','{"text": "crate with"}','{"text": "hopper and"}']}}
setblock 133 64 43 minecraft:air
setblock 133 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, pressure"}','{"text": "plate"}','{"text": ""}','{"text": ""}']}}
summon text_display 136.5 71 36.5 {text:'[{"text": "018  ", "color": "gold"}, {"text": "farms/mana_endoflame", "color": "gray"}, {"text": "\\nFüttere Endoflammen mit Holzkohle", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 134 64 35 botania:endoflame
setblock 136 64 35 botania:endoflame
setblock 134 64 37 botania:endoflame
setblock 136 64 37 botania:endoflame
setblock 135 64 36 botania:open_crate
setblock 135 65 36 minecraft:hopper[facing=down]
setblock 135 66 36 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal_block",count:16}]}
setblock 135 63 36 minecraft:stone_pressure_plate
setblock 139 64 36 botania:mana_spreader
setblock 139 64 39 botania:mana_pool
