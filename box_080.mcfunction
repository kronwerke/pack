# 080 ars_epic/el_armor
#area 272 124 291 149
fill 272 64 124 291 91 149 minecraft:air
fill 272 60 124 291 62 149 minecraft:stone
fill 272 63 124 291 63 149 minecraft:light_gray_concrete
fill 276 64 130 291 79 130 minecraft:light_gray_concrete
fill 276 64 130 276 79 143 minecraft:light_gray_concrete
setblock 277 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 278 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 286 64 130 286 79 143 minecraft:light_gray_concrete
summon armor_stand 281.5 64 135.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
