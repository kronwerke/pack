# 078 ars_master/alteration
#area 242 124 261 149
fill 242 64 124 261 91 149 minecraft:air
fill 242 60 124 261 62 149 minecraft:stone
fill 242 63 124 261 63 149 minecraft:light_gray_concrete
fill 246 64 130 261 79 130 minecraft:light_gray_concrete
fill 246 64 130 246 79 143 minecraft:light_gray_concrete
setblock 247 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 248 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 256 64 130 256 79 143 minecraft:light_gray_concrete
kw testworld use 250 63 135 up ars_nouveau:alteration_table
summon armor_stand 253.5 64 135.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
