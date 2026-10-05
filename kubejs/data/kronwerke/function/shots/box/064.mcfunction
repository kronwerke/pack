# 064 mekanism_ores/tripling
fill 117 63 108 132 63 121 minecraft:light_gray_concrete
fill 117 64 108 132 71 108 minecraft:light_gray_concrete
fill 117 64 108 117 71 121 minecraft:light_gray_concrete
setblock 118 64 120 minecraft:air
setblock 118 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 119 64 120 minecraft:air
setblock 119 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 120 64 120 minecraft:air
setblock 120 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
summon text_display 124.5 71 113.5 {text:'[{"text": "064  ", "color": "gold"}, {"text": "mekanism_ores/tripling", "color": "gray"}, {"text": "\\nLass die Dreifach-Straße laufen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 120 64 113 mekanism:purification_chamber
setblock 121 64 113 mekanism:crusher
setblock 122 64 113 mekanism:enrichment_chamber
setblock 123 64 113 mekanism:energized_smelter
setblock 120 64 115 mekanism:electrolytic_separator
setblock 122 64 115 mekanism:electric_pump
fill 120 65 113 123 65 113 mekanism:basic_logistical_transporter
fill 120 64 114 123 64 114 mekanism:basic_universal_cable
fill 121 64 115 121 64 115 mekanism:basic_pressurized_tube
