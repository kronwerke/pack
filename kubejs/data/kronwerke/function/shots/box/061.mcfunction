# 061 mekanism/ore_line
fill 60 63 108 75 63 121 minecraft:light_gray_concrete
fill 60 64 108 75 71 108 minecraft:light_gray_concrete
fill 60 64 108 60 71 121 minecraft:light_gray_concrete
setblock 61 64 120 minecraft:air
setblock 61 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "mekanism"}','{"text": "ore_line"}','{"text": ""}']}}
setblock 62 64 120 minecraft:air
setblock 62 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the steel line"}','{"text": "from enrichment"}','{"text": "chamber to the"}','{"text": "obelisk chest"}']}}
summon text_display 67.5 71 113.5 {text:'[{"text": "061  ", "color": "gold"}, {"text": "mekanism/ore_line", "color": "gray"}, {"text": "\\nBau die Stahlstraße", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 62 64 113 minecraft:chest
setblock 64 64 113 mekanism:enrichment_chamber
setblock 65 64 113 mekanism:energized_smelter
setblock 67 64 113 minecraft:chest
fill 62 65 113 67 65 113 mekanism:basic_logistical_transporter
fill 63 64 114 66 64 114 mekanism:basic_universal_cable
setblock 62 64 115 mekanism:creative_energy_cube
