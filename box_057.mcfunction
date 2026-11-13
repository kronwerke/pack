# 057 mekanism_elite/mekasuit
#area 240 95 259 120
fill 240 64 95 259 91 120 minecraft:air
fill 240 60 95 259 62 120 minecraft:stone
fill 240 63 95 259 63 120 minecraft:light_gray_concrete
fill 244 64 101 259 79 101 minecraft:light_gray_concrete
fill 244 64 101 244 79 114 minecraft:light_gray_concrete
setblock 245 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 246 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 254 64 101 254 79 114 minecraft:light_gray_concrete
summon armor_stand 248.5 64 106.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 250 64 106 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
