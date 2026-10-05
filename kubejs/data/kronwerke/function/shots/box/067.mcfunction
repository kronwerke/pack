# 067 mekanism_ores/full
fill 178 63 108 189 63 121 minecraft:light_gray_concrete
fill 178 64 108 189 71 108 minecraft:light_gray_concrete
fill 178 64 108 178 71 121 minecraft:light_gray_concrete
setblock 179 64 120 minecraft:air
setblock 179 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "mekanism_ores"}','{"text": "full"}','{"text": ""}']}}
setblock 180 64 120 minecraft:air
setblock 180 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a machine GUI"}','{"text": "with 8 speed"}','{"text": "and 8 energy"}','{"text": "upgrades"}']}}
setblock 181 64 120 minecraft:air
setblock 181 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "GUI mit 8 und 8"}','{"text": "Upgrades"}','{"text": ""}','{"text": ""}']}}
summon text_display 183.5 71 113.5 {text:'[{"text": "067  ", "color": "gold"}, {"text": "mekanism_ores/full", "color": "gray"}, {"text": "\\nBestück eine Maschine voll", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 180 64 111 mekanism:enrichment_chamber
setblock 187 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:upgrade_speed",count:8},{Slot:1b,id:"mekanism:upgrade_energy",count:8}]}
