# 027 immersive/coke_oven
#area 11 113 30 138
fill 11 64 113 30 91 138 minecraft:air
fill 11 60 113 30 62 138 minecraft:stone
fill 11 63 113 30 63 138 minecraft:light_gray_concrete
fill 15 64 119 30 79 119 minecraft:light_gray_concrete
fill 15 64 119 15 79 132 minecraft:light_gray_concrete
setblock 16 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 124.5 {text:'[{"text": "027  ", "color": "gold"}, {"text": "immersive/coke_oven", "color": "gray"}, {"text": "\\nForm einen Koksofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 119 25 79 132 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 122 none
kw testworld use 20 65 124 south immersiveengineering:hammer
execute unless block 20 65 124 immersiveengineering:cokebrick
