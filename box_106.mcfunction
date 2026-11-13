# 106 deeper_darker/portal, resonarium
#area 49 296 77 321
fill 49 64 296 77 91 321 minecraft:air
fill 49 60 296 77 62 321 minecraft:stone
fill 49 63 296 77 63 321 minecraft:light_gray_concrete
fill 53 64 302 77 79 302 minecraft:light_gray_concrete
fill 53 64 302 53 79 315 minecraft:light_gray_concrete
setblock 54 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 302 62 79 315 minecraft:light_gray_concrete
setblock 56 65 307 minecraft:reinforced_deepslate
setblock 56 66 307 minecraft:reinforced_deepslate
setblock 56 67 307 minecraft:reinforced_deepslate
setblock 57 64 307 minecraft:reinforced_deepslate
setblock 57 68 307 minecraft:reinforced_deepslate
setblock 58 64 307 minecraft:reinforced_deepslate
setblock 58 68 307 minecraft:reinforced_deepslate
setblock 59 65 307 minecraft:reinforced_deepslate
setblock 59 66 307 minecraft:reinforced_deepslate
setblock 59 67 307 minecraft:reinforced_deepslate
fill 57 65 307 58 67 307 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 307 deeperdarker:otherside_portal
setblock 63 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 302 72 79 315 minecraft:light_gray_concrete
summon armor_stand 67.5 64 307.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
