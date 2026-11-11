# 026 immersive/hammer
#area -4 113 15 138
fill -4 64 113 15 91 138 minecraft:air
fill -4 60 113 15 62 138 minecraft:stone
fill -4 63 113 15 63 138 minecraft:light_gray_concrete
fill 0 64 119 15 79 119 minecraft:light_gray_concrete
fill 0 64 119 0 79 132 minecraft:light_gray_concrete
setblock 1 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "immersive"}','{"text": "hammer"}','{"text": ""}']}}
setblock 2 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "right-clicking"}','{"text": "a structure"}','{"text": "with the hammer"}','{"text": ""}']}}
summon text_display 5.5 71 124.5 {text:'[{"text": "026  ", "color": "gold"}, {"text": "immersive/hammer", "color": "gray"}, {"text": "\\nBau einen Ingenieurshammer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 119 10 79 132 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 4 64 122 none
setblock 5 64 126 minecraft:smooth_stone_slab
summon item_display 5.5 65.04 126.5 {item:{id:"immersiveengineering:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
