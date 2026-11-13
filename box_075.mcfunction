# 075 ars_epic/el_armor
#area 257 118 276 143
fill 257 64 118 276 91 143 minecraft:air
fill 257 60 118 276 62 143 minecraft:stone
fill 257 63 118 276 63 143 minecraft:light_gray_concrete
fill 261 64 124 276 79 124 minecraft:light_gray_concrete
fill 261 64 124 261 79 137 minecraft:light_gray_concrete
setblock 262 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 263 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 271 64 124 271 79 137 minecraft:light_gray_concrete
summon armor_stand 266.5 64 129.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
