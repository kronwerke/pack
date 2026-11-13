# 105 immersive/hammer
#area -4 181 15 206
fill -4 64 181 15 91 206 minecraft:air
fill -4 60 181 15 62 206 minecraft:stone
fill -4 63 181 15 63 206 minecraft:light_gray_concrete
fill 0 64 187 15 79 187 minecraft:light_gray_concrete
fill 0 64 187 0 79 200 minecraft:light_gray_concrete
setblock 1 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 187 10 79 200 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 190 none
setblock 5 64 194 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 194.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
