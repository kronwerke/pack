# 152 deeper_darker/portal, resonarium
#area 49 334 77 359
fill 49 64 334 77 91 359 minecraft:air
fill 49 60 334 77 62 359 minecraft:stone
fill 49 63 334 77 63 359 minecraft:light_gray_concrete
fill 53 64 340 77 79 340 minecraft:light_gray_concrete
fill 53 64 340 53 79 353 minecraft:light_gray_concrete
setblock 54 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 340 62 79 353 minecraft:light_gray_concrete
setblock 56 65 345 minecraft:reinforced_deepslate
setblock 56 66 345 minecraft:reinforced_deepslate
setblock 56 67 345 minecraft:reinforced_deepslate
setblock 57 64 345 minecraft:reinforced_deepslate
setblock 57 68 345 minecraft:reinforced_deepslate
setblock 58 64 345 minecraft:reinforced_deepslate
setblock 58 68 345 minecraft:reinforced_deepslate
setblock 59 65 345 minecraft:reinforced_deepslate
setblock 59 66 345 minecraft:reinforced_deepslate
setblock 59 67 345 minecraft:reinforced_deepslate
fill 57 65 345 58 67 345 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 345 deeperdarker:otherside_portal
setblock 63 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 340 72 79 353 minecraft:light_gray_concrete
summon armor_stand 67.5 64 345.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
