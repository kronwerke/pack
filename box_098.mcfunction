# 098 alfheim/elementium_armor
#area 317 145 336 170
fill 317 64 145 336 91 170 minecraft:air
fill 317 60 145 336 62 170 minecraft:stone
fill 317 63 145 336 63 170 minecraft:light_gray_concrete
fill 321 64 151 336 79 151 minecraft:light_gray_concrete
fill 321 64 151 321 79 164 minecraft:light_gray_concrete
setblock 322 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 323 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 331 64 151 331 79 164 minecraft:light_gray_concrete
summon armor_stand 325.5 64 156.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 328.5 65 156.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
