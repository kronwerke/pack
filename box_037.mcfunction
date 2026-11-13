# 037 mekanism_elite/mekasuit
#area 192 65 211 90
fill 192 64 65 211 91 90 minecraft:air
fill 192 60 65 211 62 90 minecraft:stone
fill 192 63 65 211 63 90 minecraft:light_gray_concrete
fill 196 64 71 211 79 71 minecraft:light_gray_concrete
fill 196 64 71 196 79 84 minecraft:light_gray_concrete
setblock 197 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "mekanism_elite"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 198 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "full MekaSuit"}','{"text": "at the"}','{"text": "modification"}','{"text": "station"}']}}
fill 206 64 71 206 79 84 minecraft:light_gray_concrete
summon armor_stand 200.5 64 76.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 202 64 76 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
