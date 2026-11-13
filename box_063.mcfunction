# 063 ars_epic/el_armor
#area 240 88 259 113
fill 240 64 88 259 91 113 minecraft:air
fill 240 60 88 259 62 113 minecraft:stone
fill 240 63 88 259 63 113 minecraft:light_gray_concrete
fill 244 64 94 259 79 94 minecraft:light_gray_concrete
fill 244 64 94 244 79 107 minecraft:light_gray_concrete
setblock 245 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 246 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 254 64 94 254 79 107 minecraft:light_gray_concrete
summon armor_stand 249.5 64 99.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
