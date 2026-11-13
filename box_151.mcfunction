# 151 deeper_darker/portal, resonarium
#area 49 330 77 355
fill 49 64 330 77 91 355 minecraft:air
fill 49 60 330 77 62 355 minecraft:stone
fill 49 63 330 77 63 355 minecraft:light_gray_concrete
fill 53 64 336 77 79 336 minecraft:light_gray_concrete
fill 53 64 336 53 79 349 minecraft:light_gray_concrete
setblock 54 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 336 62 79 349 minecraft:light_gray_concrete
setblock 56 65 341 minecraft:reinforced_deepslate
setblock 56 66 341 minecraft:reinforced_deepslate
setblock 56 67 341 minecraft:reinforced_deepslate
setblock 57 64 341 minecraft:reinforced_deepslate
setblock 57 68 341 minecraft:reinforced_deepslate
setblock 58 64 341 minecraft:reinforced_deepslate
setblock 58 68 341 minecraft:reinforced_deepslate
setblock 59 65 341 minecraft:reinforced_deepslate
setblock 59 66 341 minecraft:reinforced_deepslate
setblock 59 67 341 minecraft:reinforced_deepslate
fill 57 65 341 58 67 341 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 341 deeperdarker:otherside_portal
setblock 63 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 336 72 79 349 minecraft:light_gray_concrete
summon armor_stand 67.5 64 341.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
