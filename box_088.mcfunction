# 088 ars_epic/el_armor
#area 317 126 336 151
fill 317 64 126 336 91 151 minecraft:air
fill 317 60 126 336 62 151 minecraft:stone
fill 317 63 126 336 63 151 minecraft:light_gray_concrete
fill 321 64 132 336 79 132 minecraft:light_gray_concrete
fill 321 64 132 321 79 145 minecraft:light_gray_concrete
setblock 322 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 323 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 331 64 132 331 79 145 minecraft:light_gray_concrete
summon armor_stand 326.5 64 137.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
