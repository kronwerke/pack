# 015 immersive/coke_oven
#area 11 105 30 130
fill 11 64 105 30 91 130 minecraft:air
fill 11 60 105 30 62 130 minecraft:stone
fill 11 63 105 30 63 130 minecraft:light_gray_concrete
fill 15 64 111 30 79 111 minecraft:light_gray_concrete
fill 15 64 111 15 79 124 minecraft:light_gray_concrete
setblock 16 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 116.5 {text:'[{"text": "015  ", "color": "gold"}, {"text": "immersive/coke_oven", "color": "gray"}, {"text": "\\nForm einen Koksofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 111 25 79 120 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 115 none
kw testworld use 20 65 117 south immersiveengineering:hammer
execute unless block 20 65 117 immersiveengineering:cokebrick
