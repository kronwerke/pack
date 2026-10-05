# 063 mekanism_ores/layout
fill 98 63 108 113 63 121 minecraft:light_gray_concrete
fill 98 64 108 113 71 108 minecraft:light_gray_concrete
fill 98 64 108 98 71 121 minecraft:light_gray_concrete
setblock 99 64 120 minecraft:air
setblock 99 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "mekanism_ores"}','{"text": "layout"}','{"text": ""}']}}
setblock 100 64 120 minecraft:air
setblock 100 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x line"}','{"text": "with all three"}','{"text": "transmitter"}','{"text": "types visible"}']}}
summon text_display 105.5 71 113.5 {text:'[{"text": "063  ", "color": "gold"}, {"text": "mekanism_ores/layout", "color": "gray"}, {"text": "\\nVerlege die Leitungen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 101 64 113 mekanism:purification_chamber
setblock 102 64 113 mekanism:crusher
setblock 103 64 113 mekanism:enrichment_chamber
setblock 104 64 113 mekanism:energized_smelter
setblock 101 64 115 mekanism:electrolytic_separator
setblock 103 64 115 mekanism:electric_pump
fill 101 65 113 104 65 113 mekanism:basic_logistical_transporter
fill 101 64 114 104 64 114 mekanism:basic_universal_cable
fill 102 64 115 102 64 115 mekanism:basic_pressurized_tube
