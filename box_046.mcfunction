# 046 mekanism_elite/mekasuit
#area 225 65 244 90
fill 225 64 65 244 91 90 minecraft:air
fill 225 60 65 244 62 90 minecraft:stone
fill 225 63 65 244 63 90 minecraft:light_gray_concrete
fill 229 64 71 244 79 71 minecraft:light_gray_concrete
fill 229 64 71 229 79 84 minecraft:light_gray_concrete
setblock 230 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 231 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 239 64 71 239 79 84 minecraft:light_gray_concrete
summon armor_stand 233.5 64 76.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 235 64 76 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
