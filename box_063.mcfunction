# 063 mekanism_elite/mekasuit
#area 291 97 310 122
fill 291 64 97 310 91 122 minecraft:air
fill 291 60 97 310 62 122 minecraft:stone
fill 291 63 97 310 63 122 minecraft:light_gray_concrete
fill 295 64 103 310 79 103 minecraft:light_gray_concrete
fill 295 64 103 295 79 116 minecraft:light_gray_concrete
setblock 296 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 297 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 305 64 103 305 79 116 minecraft:light_gray_concrete
summon armor_stand 299.5 64 108.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 301 64 108 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
