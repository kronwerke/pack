# 078 ars_epic/el_armor
#area 257 122 276 147
fill 257 64 122 276 91 147 minecraft:air
fill 257 60 122 276 62 147 minecraft:stone
fill 257 63 122 276 63 147 minecraft:light_gray_concrete
fill 261 64 128 276 79 128 minecraft:light_gray_concrete
fill 261 64 128 261 79 141 minecraft:light_gray_concrete
setblock 262 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 263 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 271 64 128 271 79 141 minecraft:light_gray_concrete
summon armor_stand 266.5 64 133.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
