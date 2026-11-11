# 009 immersive/coke_oven
#area 11 48 30 73
fill 11 64 48 30 91 73 minecraft:air
fill 11 60 48 30 62 73 minecraft:stone
fill 11 63 48 30 63 73 minecraft:light_gray_concrete
fill 15 64 54 30 79 54 minecraft:light_gray_concrete
fill 15 64 54 15 79 67 minecraft:light_gray_concrete
setblock 16 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "009"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 66 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 59.5 {text:'[{"text": "009  ", "color": "gold"}, {"text": "immersive/coke_oven", "color": "gray"}, {"text": "\\nForm einen Koksofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 54 25 79 63 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 58 none
kw testworld use 20 65 60 south immersiveengineering:hammer
execute unless block 20 65 60 immersiveengineering:cokebrick
