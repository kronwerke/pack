# 024 mekanism_elite/mekasuit
#area 127 44 146 69
fill 127 64 44 146 91 69 minecraft:air
fill 127 60 44 146 62 69 minecraft:stone
fill 127 63 44 146 63 69 minecraft:light_gray_concrete
fill 131 64 50 146 79 50 minecraft:light_gray_concrete
fill 131 64 50 131 79 63 minecraft:light_gray_concrete
setblock 132 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 133 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 141 64 50 141 79 63 minecraft:light_gray_concrete
summon armor_stand 135.5 64 55.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 137 64 55 mekanism:modification_station[facing=south]
