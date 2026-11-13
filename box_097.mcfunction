# 097 alfheim/elementium_armor
#area 302 139 321 164
fill 302 64 139 321 91 164 minecraft:air
fill 302 60 139 321 62 164 minecraft:stone
fill 302 63 139 321 63 164 minecraft:light_gray_concrete
fill 306 64 145 321 79 145 minecraft:light_gray_concrete
fill 306 64 145 306 79 158 minecraft:light_gray_concrete
setblock 307 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 308 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 316 64 145 316 79 158 minecraft:light_gray_concrete
summon armor_stand 310.5 64 150.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 313.5 65 150.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
