# 153 deeper_darker/portal, transmitter, resonarium, stalker, echo_shard
#area 188 336 248 363
fill 188 64 336 228 91 363 minecraft:air
fill 229 64 336 248 91 363 minecraft:air
fill 188 60 336 248 62 363 minecraft:stone
fill 188 63 336 248 63 363 minecraft:light_gray_concrete
fill 192 64 342 248 79 342 minecraft:light_gray_concrete
fill 192 64 342 192 79 357 minecraft:light_gray_concrete
setblock 193 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 194 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 201 64 342 201 79 357 minecraft:light_gray_concrete
setblock 195 65 347 minecraft:reinforced_deepslate
setblock 195 66 347 minecraft:reinforced_deepslate
setblock 195 67 347 minecraft:reinforced_deepslate
setblock 196 64 347 minecraft:reinforced_deepslate
setblock 196 68 347 minecraft:reinforced_deepslate
setblock 197 64 347 minecraft:reinforced_deepslate
setblock 197 68 347 minecraft:reinforced_deepslate
setblock 198 65 347 minecraft:reinforced_deepslate
setblock 198 66 347 minecraft:reinforced_deepslate
setblock 198 67 347 minecraft:reinforced_deepslate
fill 196 65 347 197 67 347 deeperdarker:otherside_portal[axis=x]
execute if block 196 66 347 deeperdarker:otherside_portal
setblock 202 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "deeper_darker"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 203 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde einen"}','{"text": "Sculksender"}','{"text": ""}','{"text": ""}']}}
fill 211 64 342 211 79 357 minecraft:light_gray_concrete
setblock 206 64 347 minecraft:smooth_stone_slab
summon item_display 206.5 65.4 347.5 {item:{id:"deeperdarker:sculk_transmitter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 212 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.3"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 213 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 221 64 342 221 79 357 minecraft:light_gray_concrete
summon armor_stand 216.5 64 347.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 222 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.4"}','{"text": "deeper_darker"}','{"text": "stalker"}','{"text": ""}']}}
setblock 223 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Beobachter"}','{"text": ""}','{"text": ""}']}}
fill 233 64 342 233 79 357 minecraft:light_gray_concrete
summon deeperdarker:stalker 227.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 234 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.5"}','{"text": "deeper_darker"}','{"text": "echo_shard"}','{"text": ""}']}}
setblock 235 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verstärke eine"}','{"text": "Echoscherbe"}','{"text": ""}','{"text": ""}']}}
fill 243 64 342 243 79 357 minecraft:light_gray_concrete
setblock 237 64 347 minecraft:smooth_stone_slab
summon item_display 237.5 64.95 347.5 {item:{id:"deeperdarker:reinforced_echo_shard",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 239 64 347 minecraft:smooth_stone_slab
summon item_display 239.5 64.95 347.5 {item:{id:"deeperdarker:ancient_compass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
