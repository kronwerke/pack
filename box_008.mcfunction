# 008 immersive/hammer
#area -4 48 15 73
fill -4 64 48 15 91 73 minecraft:air
fill -4 60 48 15 62 73 minecraft:stone
fill -4 63 48 15 63 73 minecraft:light_gray_concrete
fill 0 64 54 15 79 54 minecraft:light_gray_concrete
fill 0 64 54 0 79 67 minecraft:light_gray_concrete
setblock 1 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "008"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
summon text_display 5.5 71 59.5 {text:'[{"text": "008  ", "color": "gold"}, {"text": "immersive/hammer", "color": "gray"}, {"text": "\\nBau einen Ingenieurshammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 54 10 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 57 none
setblock 5 64 61 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 61.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
