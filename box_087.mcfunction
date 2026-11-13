# 087 list_gear/mekasuit
#area 83 290 102 315
fill 83 64 290 102 91 315 minecraft:air
fill 83 60 290 102 62 315 minecraft:stone
fill 83 63 290 102 63 315 minecraft:light_gray_concrete
fill 87 64 296 102 79 296 minecraft:light_gray_concrete
fill 87 64 296 87 79 309 minecraft:light_gray_concrete
setblock 88 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "list_gear"}','{"text": "mekasuit"}','{"text": ""}']}}
setblock 89 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "MekaSuit an"}','{"text": ""}','{"text": ""}']}}
fill 97 64 296 97 79 309 minecraft:light_gray_concrete
summon armor_stand 91.5 64 301.5 {ArmorItems:[{id:"mekanism:mekasuit_boots",count:1},{id:"mekanism:mekasuit_pants",count:1},{id:"mekanism:mekasuit_bodyarmor",count:1},{id:"mekanism:mekasuit_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 93 64 301 mekanism:modification_station[facing=south]
