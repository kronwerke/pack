# 012 farms/crops_harvester
fill 34 63 31 47 63 46 minecraft:light_gray_concrete
fill 34 64 31 47 71 31 minecraft:light_gray_concrete
fill 34 64 31 34 71 46 minecraft:light_gray_concrete
setblock 35 64 45 minecraft:air
setblock 35 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "farms"}','{"text": "crops_harvester"}','{"text": ""}']}}
setblock 36 64 45 minecraft:air
setblock 36 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "bearing with"}','{"text": "two harvesters"}','{"text": "and a chest"}','{"text": "sweeping a"}']}}
setblock 37 64 45 minecraft:air
setblock 37 64 45 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "round wheat"}','{"text": "field"}','{"text": ""}','{"text": ""}']}}
summon text_display 40.5 71 37.5 {text:'[{"text": "012  ", "color": "gold"}, {"text": "farms/crops_harvester", "color": "gray"}, {"text": "\\nBau eine Erntemaschine", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 36 63 33 44 63 41 minecraft:farmland
fill 36 64 33 44 64 41 minecraft:wheat[age=7]
setblock 40 62 37 minecraft:stone
setblock 40 63 37 minecraft:water
setblock 40 64 37 create:mechanical_bearing[facing=up]
fill 40 65 37 43 65 37 create:andesite_casing
setblock 41 65 38 create:mechanical_harvester[facing=south]
setblock 43 65 38 create:mechanical_harvester[facing=south]
setblock 42 65 36 minecraft:chest
