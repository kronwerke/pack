# 034 ars_epic/el_armor
#area 103 67 122 92
fill 103 64 67 122 91 92 minecraft:air
fill 103 60 67 122 62 92 minecraft:stone
fill 103 63 67 122 63 92 minecraft:light_gray_concrete
fill 107 64 73 122 79 73 minecraft:light_gray_concrete
fill 107 64 73 107 79 86 minecraft:light_gray_concrete
setblock 108 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "ars_epic"}','{"text": "el_armor"}','{"text": ""}']}}
setblock 109 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a full"}','{"text": "elemental robe"}','{"text": "set"}','{"text": ""}']}}
fill 117 64 73 117 79 86 minecraft:light_gray_concrete
summon armor_stand 112.5 64 78.5 {ArmorItems:[{id:"ars_elemental:fire_boots",count:1},{id:"ars_elemental:fire_leggings",count:1},{id:"ars_elemental:fire_robes",count:1},{id:"ars_elemental:fire_hat",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
