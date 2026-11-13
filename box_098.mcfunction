# 098 alfheim/elementium_armor
#area 317 143 336 168
fill 317 64 143 336 91 168 minecraft:air
fill 317 60 143 336 62 168 minecraft:stone
fill 317 63 143 336 63 168 minecraft:light_gray_concrete
fill 321 64 149 336 79 149 minecraft:light_gray_concrete
fill 321 64 149 321 79 162 minecraft:light_gray_concrete
setblock 322 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 323 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": ""}','{"text": ""}']}}
fill 331 64 149 331 79 162 minecraft:light_gray_concrete
summon armor_stand 325.5 64 154.5 {ArmorItems:[{id:"botania:elementium_boots",count:1},{id:"botania:elementium_leggings",count:1},{id:"botania:elementium_chestplate",count:1},{id:"botania:elementium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon botania:pixie 328.5 65 154.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
