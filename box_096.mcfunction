# 096 deeper_darker/portal, resonarium
#area 49 277 77 302
fill 49 64 277 77 91 302 minecraft:air
fill 49 60 277 77 62 302 minecraft:stone
fill 49 63 277 77 63 302 minecraft:light_gray_concrete
fill 53 64 283 77 79 283 minecraft:light_gray_concrete
fill 53 64 283 53 79 296 minecraft:light_gray_concrete
setblock 54 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 55 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 62 64 283 62 79 296 minecraft:light_gray_concrete
setblock 56 65 288 minecraft:reinforced_deepslate
setblock 56 66 288 minecraft:reinforced_deepslate
setblock 56 67 288 minecraft:reinforced_deepslate
setblock 57 64 288 minecraft:reinforced_deepslate
setblock 57 68 288 minecraft:reinforced_deepslate
setblock 58 64 288 minecraft:reinforced_deepslate
setblock 58 68 288 minecraft:reinforced_deepslate
setblock 59 65 288 minecraft:reinforced_deepslate
setblock 59 66 288 minecraft:reinforced_deepslate
setblock 59 67 288 minecraft:reinforced_deepslate
fill 57 65 288 58 67 288 deeperdarker:otherside_portal[axis=x]
execute if block 57 66 288 deeperdarker:otherside_portal
setblock 63 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 64 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 72 64 283 72 79 296 minecraft:light_gray_concrete
summon armor_stand 67.5 64 288.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
