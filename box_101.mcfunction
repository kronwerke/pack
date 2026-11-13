# 101 alfheim/elementium_armor
#area 334 145 353 170
fill 334 64 145 353 91 170 minecraft:air
fill 334 60 145 353 62 170 minecraft:stone
fill 334 63 145 353 63 170 minecraft:light_gray_concrete
fill 338 64 151 353 79 151 minecraft:light_gray_concrete
fill 338 64 151 338 79 164 minecraft:light_gray_concrete
setblock 339 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 340 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 348 64 151 348 79 164 minecraft:light_gray_concrete
summon armor_stand 342.5 64 156.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 345.5 65 156.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
