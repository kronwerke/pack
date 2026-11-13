# 153 deeper_darker/portal, transmitter, resonarium, stalker, echo_shard
#area 228 336 288 363
fill 228 64 336 268 91 363 minecraft:air
fill 269 64 336 288 91 363 minecraft:air
fill 228 60 336 288 62 363 minecraft:stone
fill 228 63 336 288 63 363 minecraft:light_gray_concrete
fill 232 64 342 288 79 342 minecraft:light_gray_concrete
fill 232 64 342 232 79 357 minecraft:light_gray_concrete
setblock 233 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 234 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 241 64 342 241 79 357 minecraft:light_gray_concrete
setblock 235 65 347 minecraft:reinforced_deepslate
setblock 235 66 347 minecraft:reinforced_deepslate
setblock 235 67 347 minecraft:reinforced_deepslate
setblock 236 64 347 minecraft:reinforced_deepslate
setblock 236 68 347 minecraft:reinforced_deepslate
setblock 237 64 347 minecraft:reinforced_deepslate
setblock 237 68 347 minecraft:reinforced_deepslate
setblock 238 65 347 minecraft:reinforced_deepslate
setblock 238 66 347 minecraft:reinforced_deepslate
setblock 238 67 347 minecraft:reinforced_deepslate
fill 236 65 347 237 67 347 deeperdarker:otherside_portal[axis=x]
execute if block 236 66 347 deeperdarker:otherside_portal
setblock 242 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "deeper_darker"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 243 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde einen"}','{"text": "Sculksender"}','{"text": ""}','{"text": ""}']}}
fill 251 64 342 251 79 357 minecraft:light_gray_concrete
setblock 246 64 347 minecraft:smooth_stone_slab
summon item_display 246.5 65.4 347.5 {item:{id:"deeperdarker:sculk_transmitter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 252 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.3"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 253 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 261 64 342 261 79 357 minecraft:light_gray_concrete
summon armor_stand 256.5 64 347.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 262 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.4"}','{"text": "deeper_darker"}','{"text": "stalker"}','{"text": ""}']}}
setblock 263 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Beobachter"}','{"text": ""}','{"text": ""}']}}
fill 273 64 342 273 79 357 minecraft:light_gray_concrete
summon deeperdarker:stalker 267.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 274 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.5"}','{"text": "deeper_darker"}','{"text": "echo_shard"}','{"text": ""}']}}
setblock 275 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verstärke eine"}','{"text": "Echoscherbe"}','{"text": ""}','{"text": ""}']}}
fill 283 64 342 283 79 357 minecraft:light_gray_concrete
setblock 277 64 347 minecraft:smooth_stone_slab
summon item_display 277.5 64.95 347.5 {item:{id:"deeperdarker:reinforced_echo_shard",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 279 64 347 minecraft:smooth_stone_slab
summon item_display 279.5 64.95 347.5 {item:{id:"deeperdarker:ancient_compass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
