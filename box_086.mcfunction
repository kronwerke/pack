# 086 alfheim/elementium_armor
#area 302 109 321 134
fill 302 64 109 321 91 134 minecraft:air
fill 302 60 109 321 62 134 minecraft:stone
fill 302 63 109 321 63 134 minecraft:light_gray_concrete
fill 306 64 115 321 79 115 minecraft:light_gray_concrete
fill 306 64 115 306 79 128 minecraft:light_gray_concrete
setblock 307 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 308 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 316 64 115 316 79 128 minecraft:light_gray_concrete
summon armor_stand 310.5 64 120.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 313.5 65 120.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
