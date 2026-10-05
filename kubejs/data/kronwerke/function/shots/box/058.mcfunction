# 058 mekanism/configurator
fill 15 63 108 26 63 121 minecraft:light_gray_concrete
fill 15 64 108 26 71 108 minecraft:light_gray_concrete
fill 15 64 108 15 71 121 minecraft:light_gray_concrete
setblock 16 64 120 minecraft:air
setblock 16 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "mekanism"}','{"text": "configurator"}','{"text": ""}']}}
setblock 17 64 120 minecraft:air
setblock 17 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "side"}','{"text": "configuration"}','{"text": "tab with auto"}','{"text": "eject"}']}}
setblock 18 64 120 minecraft:air
setblock 18 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Seitenkonfiguration,"}','{"text": "Auto-Eject"}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 113.5 {text:'[{"text": "058  ", "color": "gold"}, {"text": "mekanism/configurator", "color": "gray"}, {"text": "\\nBau einen Konfigurator", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 17 64 111 mekanism:enrichment_chamber
setblock 24 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:configurator",count:1}]}
