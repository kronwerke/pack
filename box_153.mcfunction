# 153 deeper_darker/portal, resonarium, stalker, echo_shard
#area 110 336 160 363
fill 110 64 336 150 91 363 minecraft:air
fill 151 64 336 160 91 363 minecraft:air
fill 110 60 336 160 62 363 minecraft:stone
fill 110 63 336 160 63 363 minecraft:light_gray_concrete
fill 114 64 342 160 79 342 minecraft:light_gray_concrete
fill 114 64 342 114 79 357 minecraft:light_gray_concrete
setblock 115 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 116 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 123 64 342 123 79 357 minecraft:light_gray_concrete
setblock 117 65 347 minecraft:reinforced_deepslate
setblock 117 66 347 minecraft:reinforced_deepslate
setblock 117 67 347 minecraft:reinforced_deepslate
setblock 118 64 347 minecraft:reinforced_deepslate
setblock 118 68 347 minecraft:reinforced_deepslate
setblock 119 64 347 minecraft:reinforced_deepslate
setblock 119 68 347 minecraft:reinforced_deepslate
setblock 120 65 347 minecraft:reinforced_deepslate
setblock 120 66 347 minecraft:reinforced_deepslate
setblock 120 67 347 minecraft:reinforced_deepslate
fill 118 65 347 119 67 347 deeperdarker:otherside_portal[axis=x]
execute if block 118 66 347 deeperdarker:otherside_portal
setblock 124 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 125 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 133 64 342 133 79 357 minecraft:light_gray_concrete
summon armor_stand 128.5 64 347.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 134 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.3"}','{"text": "deeper_darker"}','{"text": "stalker"}','{"text": ""}']}}
setblock 135 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Beobachter"}','{"text": ""}','{"text": ""}']}}
fill 145 64 342 145 79 357 minecraft:light_gray_concrete
summon deeperdarker:stalker 139.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 146 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.4"}','{"text": "deeper_darker"}','{"text": "echo_shard"}','{"text": ""}']}}
setblock 147 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verstärke eine"}','{"text": "Echoscherbe"}','{"text": ""}','{"text": ""}']}}
fill 155 64 342 155 79 357 minecraft:light_gray_concrete
setblock 149 64 347 minecraft:smooth_stone_slab
summon item_display 149.5 64.95 347.5 {item:{id:"deeperdarker:reinforced_echo_shard",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 151 64 347 minecraft:smooth_stone_slab
summon item_display 151.5 64.95 347.5 {item:{id:"deeperdarker:ancient_compass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
