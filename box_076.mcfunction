# 076 ars_master/alteration
#area 227 122 246 147
fill 227 64 122 246 91 147 minecraft:air
fill 227 60 122 246 62 147 minecraft:stone
fill 227 63 122 246 63 147 minecraft:light_gray_concrete
fill 231 64 128 246 79 128 minecraft:light_gray_concrete
fill 231 64 128 231 79 141 minecraft:light_gray_concrete
setblock 232 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 233 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 241 64 128 241 79 141 minecraft:light_gray_concrete
kw testworld use 235 63 133 up ars_nouveau:alteration_table
summon armor_stand 238.5 64 133.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
