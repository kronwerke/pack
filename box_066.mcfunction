# 066 ars_master/alteration
#area 227 88 246 113
fill 227 64 88 246 91 113 minecraft:air
fill 227 60 88 246 62 113 minecraft:stone
fill 227 63 88 246 63 113 minecraft:light_gray_concrete
fill 231 64 94 246 79 94 minecraft:light_gray_concrete
fill 231 64 94 231 79 107 minecraft:light_gray_concrete
setblock 232 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 233 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 241 64 94 241 79 107 minecraft:light_gray_concrete
kw testworld use 235 63 99 up ars_nouveau:alteration_table
summon armor_stand 238.5 64 99.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
