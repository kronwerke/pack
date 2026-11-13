# 082 list_gear/mekasuit
#area 58 290 77 315
fill 58 64 290 77 91 315 minecraft:air
fill 58 60 290 77 62 315 minecraft:stone
fill 58 63 290 77 63 315 minecraft:light_gray_concrete
fill 62 64 296 77 79 296 minecraft:light_gray_concrete
fill 62 64 296 62 79 309 minecraft:light_gray_concrete
setblock 63 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "list_gear"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 64 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "MekaSuit an"}','{"text": ""}','{"text": ""}']}}
fill 72 64 296 72 79 309 minecraft:light_gray_concrete
summon armor_stand 66.5 64 301.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 68 64 301 mekanism:modification_station[facing=south]
