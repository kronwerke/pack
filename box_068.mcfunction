# 068 ars_epic/el_armor
#area 257 88 276 113
fill 257 64 88 276 91 113 minecraft:air
fill 257 60 88 276 62 113 minecraft:stone
fill 257 63 88 276 63 113 minecraft:light_gray_concrete
fill 261 64 94 276 79 94 minecraft:light_gray_concrete
fill 261 64 94 261 79 107 minecraft:light_gray_concrete
setblock 262 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 263 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 271 64 94 271 79 107 minecraft:light_gray_concrete
summon armor_stand 266.5 64 99.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
