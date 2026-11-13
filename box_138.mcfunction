# 138 deeper_darker/portal, resonarium
#area 49 300 77 325
fill 49 64 300 77 91 325 minecraft:air
fill 49 60 300 77 62 325 minecraft:stone
fill 49 63 300 77 63 325 minecraft:light_gray_concrete
fill 53 64 306 77 79 306 minecraft:light_gray_concrete
fill 53 64 306 53 79 319 minecraft:light_gray_concrete
setblock 54 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 306 62 79 319 minecraft:light_gray_concrete
setblock 56 65 311 minecraft:reinforced_deepslate
setblock 56 66 311 minecraft:reinforced_deepslate
setblock 56 67 311 minecraft:reinforced_deepslate
setblock 57 64 311 minecraft:reinforced_deepslate
setblock 57 68 311 minecraft:reinforced_deepslate
setblock 58 64 311 minecraft:reinforced_deepslate
setblock 58 68 311 minecraft:reinforced_deepslate
setblock 59 65 311 minecraft:reinforced_deepslate
setblock 59 66 311 minecraft:reinforced_deepslate
setblock 59 67 311 minecraft:reinforced_deepslate
fill 57 65 311 58 67 311 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 311 deeperdarker:otherside_portal
setblock 63 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 306 72 79 319 minecraft:light_gray_concrete
summon armor_stand 67.5 64 311.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
