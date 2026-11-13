# 064 ars_epic/el_armor
#area 255 88 274 113
fill 255 64 88 274 91 113 minecraft:air
fill 255 60 88 274 62 113 minecraft:stone
fill 255 63 88 274 63 113 minecraft:light_gray_concrete
fill 259 64 94 274 79 94 minecraft:light_gray_concrete
fill 259 64 94 259 79 107 minecraft:light_gray_concrete
setblock 260 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 261 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 269 64 94 269 79 107 minecraft:light_gray_concrete
summon armor_stand 264.5 64 99.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
