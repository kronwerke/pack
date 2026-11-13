# 056 ars_master/alteration
#area 180 88 199 113
fill 180 64 88 199 91 113 minecraft:air
fill 180 60 88 199 62 113 minecraft:stone
fill 180 63 88 199 63 113 minecraft:light_gray_concrete
fill 184 64 94 199 79 94 minecraft:light_gray_concrete
fill 184 64 94 184 79 107 minecraft:light_gray_concrete
setblock 185 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "056"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 186 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 194 64 94 194 79 107 minecraft:light_gray_concrete
kw testworld use 188 63 99 up ars_nouveau:alteration_table
summon armor_stand 191.5 64 99.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
