# 034 mekanism_elite/mekasuit
#area 192 63 211 88
fill 192 64 63 211 91 88 minecraft:air
fill 192 60 63 211 62 88 minecraft:stone
fill 192 63 63 211 63 88 minecraft:light_gray_concrete
fill 196 64 69 211 79 69 minecraft:light_gray_concrete
fill 196 64 69 196 79 82 minecraft:light_gray_concrete
setblock 197 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 198 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 206 64 69 206 79 82 minecraft:light_gray_concrete
summon armor_stand 200.5 64 74.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 202 64 74 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
