# 116 immersive/hammer
#area -4 215 15 240
fill -4 64 215 15 91 240 minecraft:air
fill -4 60 215 15 62 240 minecraft:stone
fill -4 63 215 15 63 240 minecraft:light_gray_concrete
fill 0 64 221 15 79 221 minecraft:light_gray_concrete
fill 0 64 221 0 79 234 minecraft:light_gray_concrete
setblock 1 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 221 10 79 234 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 224 none
setblock 5 64 228 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 228.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
