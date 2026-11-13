# 054 mekanism_elite/mekasuit
#area 225 95 244 120
fill 225 64 95 244 91 120 minecraft:air
fill 225 60 95 244 62 120 minecraft:stone
fill 225 63 95 244 63 120 minecraft:light_gray_concrete
fill 229 64 101 244 79 101 minecraft:light_gray_concrete
fill 229 64 101 229 79 114 minecraft:light_gray_concrete
setblock 230 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 231 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 239 64 101 239 79 114 minecraft:light_gray_concrete
summon armor_stand 233.5 64 106.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 235 64 106 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
