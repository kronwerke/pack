# 086 ars_master/alteration
#area 287 126 306 151
fill 287 64 126 306 91 151 minecraft:air
fill 287 60 126 306 62 151 minecraft:stone
fill 287 63 126 306 63 151 minecraft:light_gray_concrete
fill 291 64 132 306 79 132 minecraft:light_gray_concrete
fill 291 64 132 291 79 145 minecraft:light_gray_concrete
setblock 292 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "ars_master"}','{"text": "alteration"}','{"text": ""}']}}
setblock 293 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alteration"}','{"text": "table with a"}','{"text": "robe on the"}','{"text": "stand"}']}}
fill 301 64 132 301 79 145 minecraft:light_gray_concrete
kw testworld use 295 63 137 up ars_nouveau:alteration_table
summon armor_stand 298.5 64 137.5 {ArmorItems:[{id:"ars_nouveau:arcanist_boots",count:1},{id:"ars_nouveau:arcanist_leggings",count:1},{id:"ars_nouveau:arcanist_robes",count:1},{id:"ars_nouveau:arcanist_hood",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
