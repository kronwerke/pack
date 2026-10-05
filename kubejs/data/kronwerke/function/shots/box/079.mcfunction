# 079 mekanism_elite/mekasuit
fill 360 63 90 371 63 103 minecraft:light_gray_concrete
fill 360 64 90 371 71 90 minecraft:light_gray_concrete
fill 360 64 90 360 71 103 minecraft:light_gray_concrete
setblock 361 64 102 minecraft:air
setblock 361 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 362 64 102 minecraft:air
setblock 362 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
setblock 365 64 94 mekanism:modification_station
summon armor_stand 365.5 64 96.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],HandItems:[{id:"mekanism:meka_tool",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
