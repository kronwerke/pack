# 042 ars_epic/el_armor
#area 120 86 139 111
fill 120 64 86 139 91 111 minecraft:air
fill 120 60 86 139 62 111 minecraft:stone
fill 120 63 86 139 63 111 minecraft:light_gray_concrete
fill 124 64 92 139 79 92 minecraft:light_gray_concrete
fill 124 64 92 124 79 105 minecraft:light_gray_concrete
setblock 125 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 126 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 134 64 92 134 79 105 minecraft:light_gray_concrete
summon armor_stand 129.5 64 97.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
