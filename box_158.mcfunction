# 158 deeper_darker/portal, transmitter, resonarium, stalker, echo_shard
#area 228 340 288 367
fill 228 64 340 268 91 367 minecraft:air
fill 269 64 340 288 91 367 minecraft:air
fill 228 60 340 288 62 367 minecraft:stone
fill 228 63 340 288 63 367 minecraft:light_gray_concrete
fill 232 64 346 288 79 346 minecraft:light_gray_concrete
fill 232 64 346 232 79 361 minecraft:light_gray_concrete
setblock 233 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.1"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 234 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 241 64 346 241 79 361 minecraft:light_gray_concrete
setblock 235 65 351 minecraft:reinforced_deepslate
setblock 235 66 351 minecraft:reinforced_deepslate
setblock 235 67 351 minecraft:reinforced_deepslate
setblock 236 64 351 minecraft:reinforced_deepslate
setblock 236 68 351 minecraft:reinforced_deepslate
setblock 237 64 351 minecraft:reinforced_deepslate
setblock 237 68 351 minecraft:reinforced_deepslate
setblock 238 65 351 minecraft:reinforced_deepslate
setblock 238 66 351 minecraft:reinforced_deepslate
setblock 238 67 351 minecraft:reinforced_deepslate
fill 236 65 351 237 67 351 deeperdarker:otherside_portal[axis=x]
execute if block 236 66 351 deeperdarker:otherside_portal
setblock 242 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.2"}','{"text": "deeper_darker"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 243 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde einen"}','{"text": "Sculksender"}','{"text": ""}','{"text": ""}']}}
fill 251 64 346 251 79 361 minecraft:light_gray_concrete
setblock 246 64 351 minecraft:smooth_stone_slab
summon item_display 246.5 65.4 351.5 {item:{id:"deeperdarker:sculk_transmitter",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 252 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.3"}','{"text": "deeper_darker"}','{"text": "resonarium"}','{"text": ""}']}}
setblock 253 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schmiede"}','{"text": "Resonarium"}','{"text": ""}','{"text": ""}']}}
fill 261 64 346 261 79 361 minecraft:light_gray_concrete
summon armor_stand 256.5 64 351.5 {ArmorItems:[{id:"deeperdarker:resonarium_boots",count:1},{id:"deeperdarker:resonarium_leggings",count:1},{id:"deeperdarker:resonarium_chestplate",count:1},{id:"deeperdarker:resonarium_helmet",count:1}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 262 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.4"}','{"text": "deeper_darker"}','{"text": "stalker"}','{"text": ""}']}}
setblock 263 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Beobachter"}','{"text": ""}','{"text": ""}']}}
fill 273 64 346 273 79 361 minecraft:light_gray_concrete
summon deeperdarker:stalker 267.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 274 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.5"}','{"text": "deeper_darker"}','{"text": "echo_shard"}','{"text": ""}']}}
setblock 275 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verstärke eine"}','{"text": "Echoscherbe"}','{"text": ""}','{"text": ""}']}}
fill 283 64 346 283 79 361 minecraft:light_gray_concrete
setblock 277 64 351 minecraft:smooth_stone_slab
summon item_display 277.5 64.95 351.5 {item:{id:"deeperdarker:reinforced_echo_shard",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 279 64 351 minecraft:smooth_stone_slab
summon item_display 279.5 64.95 351.5 {item:{id:"deeperdarker:ancient_compass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
