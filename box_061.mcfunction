# 061 ars_master/alteration
#area 210 88 229 113
fill 210 64 88 229 91 113 minecraft:air
fill 210 60 88 229 62 113 minecraft:stone
fill 210 63 88 229 63 113 minecraft:light_gray_concrete
fill 214 64 94 229 79 94 minecraft:light_gray_concrete
fill 214 64 94 214 79 107 minecraft:light_gray_concrete
setblock 215 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 216 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 224 64 94 224 79 107 minecraft:light_gray_concrete
kw testworld use 218 63 99 up ars_nouveau:alteration_table
summon armor_stand 221.5 64 99.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
