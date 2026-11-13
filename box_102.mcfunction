# 102 list_gear/mekasuit
#area 83 311 102 336
fill 83 64 311 102 91 336 minecraft:air
fill 83 60 311 102 62 336 minecraft:stone
fill 83 63 311 102 63 336 minecraft:light_gray_concrete
fill 87 64 317 102 79 317 minecraft:light_gray_concrete
fill 87 64 317 87 79 330 minecraft:light_gray_concrete
setblock 88 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102"}','{"text": "list_gear"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 89 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "MekaSuit an"}','{"text": ""}','{"text": ""}']}}
fill 97 64 317 97 79 330 minecraft:light_gray_concrete
summon armor_stand 91.5 64 322.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 93 64 322 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
