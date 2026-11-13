# 112 alfheim/elementium_armor
#area 377 147 396 172
fill 377 64 147 396 91 172 minecraft:air
fill 377 60 147 396 62 172 minecraft:stone
fill 377 63 147 396 63 172 minecraft:light_gray_concrete
fill 381 64 153 396 79 153 minecraft:light_gray_concrete
fill 381 64 153 381 79 166 minecraft:light_gray_concrete
setblock 382 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 383 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 391 64 153 391 79 166 minecraft:light_gray_concrete
summon armor_stand 385.5 64 158.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 388.5 65 158.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
