# 135 immersive/coke_oven, pump
#area 11 219 40 244
fill 11 64 219 40 91 244 minecraft:air
fill 11 60 219 40 62 244 minecraft:stone
fill 11 63 219 40 63 244 minecraft:light_gray_concrete
fill 15 64 225 40 79 225 minecraft:light_gray_concrete
fill 15 64 225 15 79 238 minecraft:light_gray_concrete
setblock 16 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.1"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 225 25 79 238 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 228 none
kw testworld use 20 65 230 south immersiveengineering:hammer
execute unless block 20 65 230 immersiveengineering:cokebrick
setblock 26 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.2"}','{"text": "immersive"}','{"text": "pump"}','{"text": ""}']}}
setblock 27 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Pump das"}','{"text": "Kreosot ab"}','{"text": ""}','{"text": ""}']}}
fill 35 64 225 35 79 238 minecraft:light_gray_concrete
setblock 29 64 230 minecraft:smooth_stone_slab
summon item_display 29.5 64.95 230.5 {item:{id:"immersiveengineering:fluid_pump",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 31 64 230 minecraft:smooth_stone_slab
summon item_display 31.5 64.95 230.5 {item:{id:"immersiveengineering:fluid_pipe",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
