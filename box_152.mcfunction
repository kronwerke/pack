# 152 deeper_darker/portal, resonarium
#area 49 336 77 361
fill 49 64 336 77 91 361 minecraft:air
fill 49 60 336 77 62 361 minecraft:stone
fill 49 63 336 77 63 361 minecraft:light_gray_concrete
fill 53 64 342 77 79 342 minecraft:light_gray_concrete
fill 53 64 342 53 79 355 minecraft:light_gray_concrete
setblock 54 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 342 62 79 355 minecraft:light_gray_concrete
setblock 56 65 347 minecraft:reinforced_deepslate
setblock 56 66 347 minecraft:reinforced_deepslate
setblock 56 67 347 minecraft:reinforced_deepslate
setblock 57 64 347 minecraft:reinforced_deepslate
setblock 57 68 347 minecraft:reinforced_deepslate
setblock 58 64 347 minecraft:reinforced_deepslate
setblock 58 68 347 minecraft:reinforced_deepslate
setblock 59 65 347 minecraft:reinforced_deepslate
setblock 59 66 347 minecraft:reinforced_deepslate
setblock 59 67 347 minecraft:reinforced_deepslate
fill 57 65 347 58 67 347 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 347 deeperdarker:otherside_portal
setblock 63 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 342 72 79 355 minecraft:light_gray_concrete
summon armor_stand 67.5 64 347.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
