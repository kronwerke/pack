# 060 mekanism/ethene
fill 45 63 108 56 63 121 minecraft:light_gray_concrete
fill 45 64 108 56 71 108 minecraft:light_gray_concrete
fill 45 64 108 45 71 121 minecraft:light_gray_concrete
setblock 46 64 120 minecraft:air
setblock 46 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 47 64 120 minecraft:air
setblock 47 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
summon text_display 50.5 71 113.5 {text:'[{"text": "060  ", "color": "gold"}, {"text": "mekanism/ethene", "color": "gray"}, {"text": "\\nMach Ethen in der Druckreaktionskammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 47 64 111 mekanism:pressurized_reaction_chamber
setblock 54 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"mekanism:substrate",count:16},{Slot:1b,id:"mekanism:configurator",count:1}]}
