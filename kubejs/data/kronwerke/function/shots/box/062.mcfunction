# 062 mekanism_ores/line2
fill 79 63 108 94 63 121 minecraft:light_gray_concrete
fill 79 64 108 94 71 108 minecraft:light_gray_concrete
fill 79 64 108 79 71 121 minecraft:light_gray_concrete
setblock 80 64 120 minecraft:air
setblock 80 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 81 64 120 minecraft:air
setblock 81 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 82 64 120 minecraft:air
setblock 82 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
summon text_display 86.5 71 113.5 {text:'[{"text": "062  ", "color": "gold"}, {"text": "mekanism_ores/line2", "color": "gray"}, {"text": "\\nStell die Zweifach-Straße auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 81 64 113 minecraft:chest
setblock 83 64 113 mekanism:enrichment_chamber
setblock 84 64 113 mekanism:energized_smelter
setblock 86 64 113 minecraft:chest
fill 81 65 113 86 65 113 mekanism:basic_logistical_transporter
fill 82 64 114 85 64 114 mekanism:basic_universal_cable
setblock 81 64 115 mekanism:creative_energy_cube
