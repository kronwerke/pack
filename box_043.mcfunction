# 043 immersive/hammer
#area -4 144 15 169
fill -4 64 144 15 91 169 minecraft:air
fill -4 60 144 15 62 169 minecraft:stone
fill -4 63 144 15 63 169 minecraft:light_gray_concrete
fill 0 64 150 15 79 150 minecraft:light_gray_concrete
fill 0 64 150 0 79 163 minecraft:light_gray_concrete
setblock 1 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
fill 10 64 150 10 79 163 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 153 none
setblock 5 64 157 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 157.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
