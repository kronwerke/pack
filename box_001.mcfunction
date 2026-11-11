# 001 botania_runes/plate_base
#area -4 -6 15 19
fill -4 64 -6 15 91 19 minecraft:air
fill -4 60 -6 15 62 19 minecraft:stone
fill -4 63 -6 15 63 19 minecraft:light_gray_concrete
fill 0 64 0 15 79 0 minecraft:light_gray_concrete
fill 0 64 0 0 79 13 minecraft:light_gray_concrete
setblock 1 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "001"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 2 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
summon text_display 5.5 71 5.5 {text:'[{"text": "001  ", "color": "gold"}, {"text": "botania_runes/plate_base", "color": "gray"}, {"text": "\\nLeg das Fundament", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 0 10 79 9 minecraft:light_gray_concrete
setblock 4 64 4 botania:livingrock
setblock 4 64 5 minecraft:lapis_block
setblock 4 64 6 botania:livingrock
setblock 5 64 4 minecraft:lapis_block
setblock 5 64 5 botania:livingrock
setblock 5 64 6 minecraft:lapis_block
setblock 6 64 4 botania:livingrock
setblock 6 64 5 minecraft:lapis_block
setblock 6 64 6 botania:livingrock
setblock 5 65 5 botania:terrestrial_agglomeration_plate
