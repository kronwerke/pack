# 038 ars_epic/el_armor
#area 126 67 145 92
fill 126 64 67 145 91 92 minecraft:air
fill 126 60 67 145 62 92 minecraft:stone
fill 126 63 67 145 63 92 minecraft:light_gray_concrete
fill 130 64 73 145 79 73 minecraft:light_gray_concrete
fill 130 64 73 130 79 86 minecraft:light_gray_concrete
setblock 131 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 132 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 140 64 73 140 79 86 minecraft:light_gray_concrete
summon armor_stand 135.5 64 78.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
