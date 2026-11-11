# 011 ars_nouveau/apparatus
#area -4 34 15 59
fill -4 64 34 15 91 59 minecraft:air
fill -4 60 34 15 62 59 minecraft:stone
fill -4 63 34 15 63 59 minecraft:light_gray_concrete
fill 0 64 40 15 79 40 minecraft:light_gray_concrete
fill 0 64 40 0 79 53 minecraft:light_gray_concrete
setblock 1 64 52 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "ars_nouveau"}','{"text": "apparatus"}','{"text": ""}']}}
setblock 2 64 52 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "core, apparatus"}','{"text": "and pedestals"}','{"text": "in range"}','{"text": ""}']}}
summon text_display 5.5 71 45.5 {text:'[{"text": "011  ", "color": "gold"}, {"text": "ars_nouveau/apparatus", "color": "gray"}, {"text": "\\nBau den Bezaubernden Apparat", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 40 10 79 53 minecraft:light_gray_concrete
setblock 5 64 45 ars_nouveau:arcane_core[facing=up]
setblock 5 65 45 ars_nouveau:enchanting_apparatus[facing=up]
setblock 3 64 43 ars_nouveau:arcane_pedestal[facing=up]
setblock 5 64 42 ars_nouveau:arcane_pedestal[facing=up]
setblock 7 64 43 ars_nouveau:arcane_pedestal[facing=up]
setblock 2 64 45 ars_nouveau:arcane_pedestal[facing=up]
setblock 8 64 45 ars_nouveau:arcane_pedestal[facing=up]
setblock 3 64 47 ars_nouveau:arcane_pedestal[facing=up]
setblock 7 64 47 ars_nouveau:arcane_pedestal[facing=up]
setblock 8 64 48 ars_nouveau:source_jar[fill=11]{source:10000}
