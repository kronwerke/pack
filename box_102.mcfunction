# 102 list_gear/mek_jetpack, mekasuit
#area 103 311 132 336
fill 103 64 311 132 91 336 minecraft:air
fill 103 60 311 132 62 336 minecraft:stone
fill 103 63 311 132 63 336 minecraft:light_gray_concrete
fill 107 64 317 132 79 317 minecraft:light_gray_concrete
fill 107 64 317 107 79 330 minecraft:light_gray_concrete
setblock 108 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.1"}','{"text": "list_gear"}','{"text": "mek_jetpack"}','{"text": ""}']}}
setblock 109 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flieg mit dem"}','{"text": "Jetpack"}','{"text": ""}','{"text": ""}']}}
fill 117 64 317 117 79 330 minecraft:light_gray_concrete
summon armor_stand 112.5 64 322.5 {ArmorItems:[{},{},{id:"mekanism:jetpack",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 118 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.2"}','{"text": "list_gear"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 119 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "MekaSuit an"}','{"text": ""}','{"text": ""}']}}
fill 127 64 317 127 79 330 minecraft:light_gray_concrete
summon armor_stand 121.5 64 322.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 123 64 322 mekanism:modification_station[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
