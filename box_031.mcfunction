# 031 mekanism_elite/mekasuit
#area 177 63 196 88
fill 177 64 63 196 91 88 minecraft:air
fill 177 60 63 196 62 88 minecraft:stone
fill 177 63 63 196 63 88 minecraft:light_gray_concrete
fill 181 64 69 196 79 69 minecraft:light_gray_concrete
fill 181 64 69 181 79 82 minecraft:light_gray_concrete
setblock 182 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 183 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 191 64 69 191 79 82 minecraft:light_gray_concrete
summon armor_stand 185.5 64 74.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 187 64 74 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
