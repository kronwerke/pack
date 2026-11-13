# 025 mekanism_elite/mekasuit
#area 143 44 162 69
fill 143 64 44 162 91 69 minecraft:air
fill 143 60 44 162 62 69 minecraft:stone
fill 143 63 44 162 63 69 minecraft:light_gray_concrete
fill 147 64 50 162 79 50 minecraft:light_gray_concrete
fill 147 64 50 147 79 63 minecraft:light_gray_concrete
setblock 148 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 149 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 157 64 50 157 79 63 minecraft:light_gray_concrete
summon armor_stand 151.5 64 55.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 153 64 55 mekanism:modification_station[facing=south]
