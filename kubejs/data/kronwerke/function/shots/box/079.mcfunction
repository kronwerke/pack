# 079 mekanism_elite/mekasuit
fill 360 63 108 371 63 121 minecraft:light_gray_concrete
fill 360 64 108 371 71 108 minecraft:light_gray_concrete
fill 360 64 108 360 71 121 minecraft:light_gray_concrete
setblock 361 64 120 minecraft:air
setblock 361 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 362 64 120 minecraft:air
setblock 362 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
summon text_display 365.5 71 113.5 {text:'[{"text": "079  ", "color": "gold"}, {"text": "mekanism_elite/mekasuit", "color": "gray"}, {"text": "\\nZieh die MekaSuit an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 365 64 112 mekanism:modification_station
summon armor_stand 365.5 64 114.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],HandItems:[{id:"mekanism:meka_tool",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
