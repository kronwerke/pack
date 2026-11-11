# 007 botania_runes/plate_base
#area -4 51 15 76
fill -4 64 51 15 91 76 minecraft:air
fill -4 60 51 15 62 76 minecraft:stone
fill -4 63 51 15 63 76 minecraft:light_gray_concrete
fill 0 64 57 15 79 57 minecraft:light_gray_concrete
fill 0 64 57 0 79 70 minecraft:light_gray_concrete
setblock 1 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "007"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 2 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
summon text_display 5.5 71 62.5 {text:'[{"text": "007  ", "color": "gold"}, {"text": "botania_runes/plate_base", "color": "gray"}, {"text": "\\nLeg das Fundament", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 57 10 79 66 minecraft:light_gray_concrete
setblock 4 64 61 botania:livingrock
setblock 4 64 62 minecraft:lapis_block
setblock 4 64 63 botania:livingrock
setblock 5 64 61 minecraft:lapis_block
setblock 5 64 62 botania:livingrock
setblock 5 64 63 minecraft:lapis_block
setblock 6 64 61 botania:livingrock
setblock 6 64 62 minecraft:lapis_block
setblock 6 64 63 botania:livingrock
setblock 5 65 62 botania:terrestrial_agglomeration_plate
