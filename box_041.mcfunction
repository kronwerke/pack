# 041 ars_epic/el_armor
#area 122 86 141 111
fill 122 64 86 141 91 111 minecraft:air
fill 122 60 86 141 62 111 minecraft:stone
fill 122 63 86 141 63 111 minecraft:light_gray_concrete
fill 126 64 92 141 79 92 minecraft:light_gray_concrete
fill 126 64 92 126 79 105 minecraft:light_gray_concrete
setblock 127 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 128 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 136 64 92 136 79 105 minecraft:light_gray_concrete
summon armor_stand 131.5 64 97.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
