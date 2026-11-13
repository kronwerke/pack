# 062 ars_master/alteration
#area 225 88 244 113
fill 225 64 88 244 91 113 minecraft:air
fill 225 60 88 244 62 113 minecraft:stone
fill 225 63 88 244 63 113 minecraft:light_gray_concrete
fill 229 64 94 244 79 94 minecraft:light_gray_concrete
fill 229 64 94 229 79 107 minecraft:light_gray_concrete
setblock 230 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 231 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 239 64 94 239 79 107 minecraft:light_gray_concrete
kw testworld use 233 63 99 up ars_nouveau:alteration_table
summon armor_stand 236.5 64 99.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
