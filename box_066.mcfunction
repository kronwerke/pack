# 066 immersive/hammer
#area -4 158 15 183
fill -4 64 158 15 91 183 minecraft:air
fill -4 60 158 15 62 183 minecraft:stone
fill -4 63 158 15 63 183 minecraft:light_gray_concrete
fill 0 64 164 15 79 164 minecraft:light_gray_concrete
fill 0 64 164 0 79 177 minecraft:light_gray_concrete
setblock 1 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "066"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 176 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 164 10 79 177 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 167 none
setblock 5 64 171 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 171.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
