# 027 mekanism_elite/mekasuit
#area 177 44 196 69
fill 177 64 44 196 91 69 minecraft:air
fill 177 60 44 196 62 69 minecraft:stone
fill 177 63 44 196 63 69 minecraft:light_gray_concrete
fill 181 64 50 196 79 50 minecraft:light_gray_concrete
fill 181 64 50 181 79 63 minecraft:light_gray_concrete
setblock 182 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 183 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 191 64 50 191 79 63 minecraft:light_gray_concrete
summon armor_stand 185.5 64 55.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 187 64 55 mekanism:modification_station[facing=south]
