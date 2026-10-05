# 114 botania/endo_auto
fill 15 63 186 28 63 199 minecraft:light_gray_concrete
fill 15 64 186 28 71 186 minecraft:light_gray_concrete
fill 15 64 186 15 71 199 minecraft:light_gray_concrete
setblock 16 64 198 minecraft:air
setblock 16 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "114"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 198 minecraft:air
setblock 17 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 198 minecraft:air
setblock 18 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 21.5 71 191.5 {text:'[{"text": "114  ", "color": "gold"}, {"text": "botania/endo_auto", "color": "gray"}, {"text": "\\nAutomatisiere die Kohle", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 19 64 190 botania:endoflame
setblock 21 64 190 botania:endoflame
setblock 19 64 192 botania:endoflame
setblock 21 64 192 botania:endoflame
setblock 20 64 191 botania:open_crate
setblock 20 65 191 minecraft:hopper[facing=down]
setblock 20 66 191 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal_block",count:16}]}
setblock 20 63 191 minecraft:stone_pressure_plate
setblock 24 64 191 botania:mana_spreader
setblock 24 64 194 botania:mana_pool
