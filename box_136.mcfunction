# 136 deeper_darker/portal, resonarium
#area 49 298 77 323
fill 49 64 298 77 91 323 minecraft:air
fill 49 60 298 77 62 323 minecraft:stone
fill 49 63 298 77 63 323 minecraft:light_gray_concrete
fill 53 64 304 77 79 304 minecraft:light_gray_concrete
fill 53 64 304 53 79 317 minecraft:light_gray_concrete
setblock 54 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 304 62 79 317 minecraft:light_gray_concrete
setblock 56 65 309 minecraft:reinforced_deepslate
setblock 56 66 309 minecraft:reinforced_deepslate
setblock 56 67 309 minecraft:reinforced_deepslate
setblock 57 64 309 minecraft:reinforced_deepslate
setblock 57 68 309 minecraft:reinforced_deepslate
setblock 58 64 309 minecraft:reinforced_deepslate
setblock 58 68 309 minecraft:reinforced_deepslate
setblock 59 65 309 minecraft:reinforced_deepslate
setblock 59 66 309 minecraft:reinforced_deepslate
setblock 59 67 309 minecraft:reinforced_deepslate
fill 57 65 309 58 67 309 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 309 deeperdarker:otherside_portal
setblock 63 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 304 72 79 317 minecraft:light_gray_concrete
summon armor_stand 67.5 64 309.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
