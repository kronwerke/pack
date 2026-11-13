# 116 immersive/hammer
#area -4 217 15 242
fill -4 64 217 15 91 242 minecraft:air
fill -4 60 217 15 62 242 minecraft:stone
fill -4 63 217 15 63 242 minecraft:light_gray_concrete
fill 0 64 223 15 79 223 minecraft:light_gray_concrete
fill 0 64 223 0 79 236 minecraft:light_gray_concrete
setblock 1 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 223 10 79 236 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 226 none
setblock 5 64 230 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 230.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
