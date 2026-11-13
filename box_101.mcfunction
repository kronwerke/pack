# 101 list_gear/mekasuit
#area 83 309 102 334
fill 83 64 309 102 91 334 minecraft:air
fill 83 60 309 102 62 334 minecraft:stone
fill 83 63 309 102 63 334 minecraft:light_gray_concrete
fill 87 64 315 102 79 315 minecraft:light_gray_concrete
fill 87 64 315 87 79 328 minecraft:light_gray_concrete
setblock 88 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "list_gear"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 89 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "MekaSuit an"}','{"text": ""}','{"text": ""}']}}
fill 97 64 315 97 79 328 minecraft:light_gray_concrete
summon armor_stand 91.5 64 320.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 93 64 320 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
