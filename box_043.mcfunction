# 043 mekanism_elite/mekasuit
#area 210 65 229 90
fill 210 64 65 229 91 90 minecraft:air
fill 210 60 65 229 62 90 minecraft:stone
fill 210 63 65 229 63 90 minecraft:light_gray_concrete
fill 214 64 71 229 79 71 minecraft:light_gray_concrete
fill 214 64 71 214 79 84 minecraft:light_gray_concrete
setblock 215 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 216 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 224 64 71 224 79 84 minecraft:light_gray_concrete
summon armor_stand 218.5 64 76.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 220 64 76 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
