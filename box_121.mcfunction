# 121 immersive/treated_wood
#area 36 217 55 242
fill 36 64 217 55 91 242 minecraft:air
fill 36 60 217 55 62 242 minecraft:stone
fill 36 63 217 55 63 242 minecraft:light_gray_concrete
fill 40 64 223 55 79 223 minecraft:light_gray_concrete
fill 40 64 223 40 79 236 minecraft:light_gray_concrete
setblock 41 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121"}','{"text": "immersive"}','{"text": "treated_wood"}','{"text": ""}']}}
setblock 42 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "planks around"}','{"text": "the creosote"}','{"text": "bucket"}','{"text": ""}']}}
fill 50 64 223 50 79 236 minecraft:light_gray_concrete
setblock 44 64 228 minecraft:smooth_stone_slab
summon item_display 44.5 64.95 228.5 {item:{id:"immersiveengineering:creosote_bucket",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 46 64 228 minecraft:smooth_stone_slab
summon item_display 46.5 64.95 228.5 {item:{id:"immersiveengineering:treated_wood_horizontal",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
