# 139 alfheim/elementium_armor
fill 15 63 205 26 63 218 minecraft:light_gray_concrete
fill 15 64 205 26 71 205 minecraft:light_gray_concrete
fill 15 64 205 15 71 218 minecraft:light_gray_concrete
setblock 16 64 217 minecraft:air
setblock 16 64 217 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 17 64 217 minecraft:air
setblock 17 64 217 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": "Elementium-Rüstung"}','{"text": "an, Mob"}']}}
setblock 18 64 217 minecraft:air
setblock 18 64 217 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "angreifen"}','{"text": "lassen"}','{"text": ""}','{"text": ""}']}}
setblock 24 64 214 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:elementium_chestplate",count:1}]}
summon minecraft:zombie 18.5 64 212.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
