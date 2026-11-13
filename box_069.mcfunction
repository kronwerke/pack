# 069 immersive/hammer
#area -4 177 15 202
fill -4 64 177 15 91 202 minecraft:air
fill -4 60 177 15 62 202 minecraft:stone
fill -4 63 177 15 63 202 minecraft:light_gray_concrete
fill 0 64 183 15 79 183 minecraft:light_gray_concrete
fill 0 64 183 0 79 196 minecraft:light_gray_concrete
setblock 1 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 195 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 183 10 79 196 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 186 none
setblock 5 64 190 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 190.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
