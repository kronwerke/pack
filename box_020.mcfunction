# 020 immersive/coke_oven
#area 11 111 30 136
fill 11 64 111 30 91 136 minecraft:air
fill 11 60 111 30 62 136 minecraft:stone
fill 11 63 111 30 63 136 minecraft:light_gray_concrete
fill 15 64 117 30 79 117 minecraft:light_gray_concrete
fill 15 64 117 15 79 130 minecraft:light_gray_concrete
setblock 16 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "immersive"}','{"text": "coke_oven"}','{"text": ""}']}}
setblock 17 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "formed coke"}','{"text": "oven with GUI,"}','{"text": "the bucket"}','{"text": "slot, a pump"}']}}
setblock 18 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "with pipes"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 20.5 71 122.5 {text:'[{"text": "020  ", "color": "gold"}, {"text": "immersive/coke_oven", "color": "gray"}, {"text": "\\nForm einen Koksofen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 117 25 79 126 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/coke_oven 19 64 121 none
kw testworld use 20 65 123 south immersiveengineering:hammer
execute unless block 20 65 123 immersiveengineering:cokebrick
