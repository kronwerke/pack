# 012 botania/pure_daisy
#area -4 53 15 78
fill -4 64 53 15 91 78 minecraft:air
fill -4 60 53 15 62 78 minecraft:stone
fill -4 63 53 15 63 78 minecraft:light_gray_concrete
fill 0 64 59 15 79 59 minecraft:light_gray_concrete
fill 0 64 59 0 79 72 minecraft:light_gray_concrete
setblock 1 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 71 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
summon text_display 5.5 71 64.5 {text:'[{"text": "012  ", "color": "gold"}, {"text": "botania/pure_daisy", "color": "gray"}, {"text": "\\nPflanz ein Reines Gänseblümchen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 59 10 79 72 minecraft:light_gray_concrete
setblock 5 63 64 minecraft:grass_block
setblock 5 64 64 botania:pure_daisy
setblock 4 64 63 minecraft:stone
setblock 5 64 63 botania:livingrock
setblock 6 64 63 minecraft:stone
setblock 4 64 64 minecraft:oak_log[axis=y]
setblock 6 64 64 botania:livingwood_log[axis=y]
setblock 4 64 65 botania:livingrock
setblock 5 64 65 minecraft:stone
setblock 6 64 65 botania:livingrock
