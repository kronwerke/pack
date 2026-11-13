# 076 ars_master/alteration
#area 227 118 246 143
fill 227 64 118 246 91 143 minecraft:air
fill 227 60 118 246 62 143 minecraft:stone
fill 227 63 118 246 63 143 minecraft:light_gray_concrete
fill 231 64 124 246 79 124 minecraft:light_gray_concrete
fill 231 64 124 231 79 137 minecraft:light_gray_concrete
setblock 232 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 233 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 241 64 124 241 79 137 minecraft:light_gray_concrete
kw testworld use 235 63 129 up ars_nouveau:alteration_table
summon armor_stand 238.5 64 129.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
