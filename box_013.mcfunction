# 013 botania_runes/plate_base
#area 11 53 30 78
fill 11 64 53 30 91 78 minecraft:air
fill 11 60 53 30 62 78 minecraft:stone
fill 11 63 53 30 63 78 minecraft:light_gray_concrete
fill 15 64 59 30 79 59 minecraft:light_gray_concrete
fill 15 64 59 15 79 72 minecraft:light_gray_concrete
setblock 16 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "013"}','{"text": "botania_runes"}','{"text": "plate_base"}','{"text": ""}']}}
setblock 17 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 3x3 lapis"}','{"text": "and livingrock"}','{"text": "base with plate"}','{"text": "and sparks"}']}}
summon text_display 20.5 71 64.5 {text:'[{"text": "013  ", "color": "gold"}, {"text": "botania_runes/plate_base", "color": "gray"}, {"text": "\\nLeg das Fundament", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 25 64 59 25 79 72 minecraft:light_gray_concrete
setblock 19 64 63 botania:livingrock
setblock 19 64 64 minecraft:lapis_block
setblock 19 64 65 botania:livingrock
setblock 20 64 63 minecraft:lapis_block
setblock 20 64 64 botania:livingrock
setblock 20 64 65 minecraft:lapis_block
setblock 21 64 63 botania:livingrock
setblock 21 64 64 minecraft:lapis_block
setblock 21 64 65 botania:livingrock
setblock 20 65 64 botania:terrestrial_agglomeration_plate
