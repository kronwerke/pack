# 136 immersive/treated_wood
#area 36 219 55 244
fill 36 64 219 55 91 244 minecraft:air
fill 36 60 219 55 62 244 minecraft:stone
fill 36 63 219 55 63 244 minecraft:light_gray_concrete
fill 40 64 225 55 79 225 minecraft:light_gray_concrete
fill 40 64 225 40 79 238 minecraft:light_gray_concrete
setblock 41 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136"}','{"text": "immersive"}','{"text": "treated_wood"}','{"text": ""}']}}
setblock 42 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "planks around"}','{"text": "the creosote"}','{"text": "bucket"}','{"text": ""}']}}
fill 50 64 225 50 79 238 minecraft:light_gray_concrete
setblock 44 64 230 minecraft:smooth_stone_slab
summon item_display 44.5 64.95 230.5 {item:{id:"immersiveengineering:creosote_bucket",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 46 64 230 minecraft:smooth_stone_slab
summon item_display 46.5 64.95 230.5 {item:{id:"immersiveengineering:treated_wood_horizontal",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
