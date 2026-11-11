# 001 create/water_wheel
#area -4 -6 16 19
fill -4 64 -6 16 91 19 minecraft:air
fill -4 60 -6 16 62 19 minecraft:stone
fill -4 63 -6 16 63 19 minecraft:light_gray_concrete
fill 0 64 0 16 79 0 minecraft:light_gray_concrete
fill 0 64 0 0 79 13 minecraft:light_gray_concrete
setblock 1 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "001"}','{"text": "create"}','{"text": "water_wheel"}','{"text": ""}']}}
setblock 2 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "four water"}','{"text": "wheels in a row"}','{"text": "with water over"}','{"text": "the paddles"}']}}
setblock 3 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "from above"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 6.0 71 5.5 {text:'[{"text": "001  ", "color": "gold"}, {"text": "create/water_wheel", "color": "gray"}, {"text": "\\nStell ein Wasserrad in den Bach", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 11 64 0 11 79 13 minecraft:light_gray_concrete
setblock 4 65 5 create:water_wheel[facing=east]
setblock 4 63 4 minecraft:air
setblock 5 65 5 create:water_wheel[facing=east]
setblock 5 63 4 minecraft:air
setblock 6 65 5 create:water_wheel[facing=east]
setblock 6 63 4 minecraft:air
setblock 7 65 5 create:water_wheel[facing=east]
setblock 7 63 4 minecraft:air
setblock 3 64 5 create:andesite_casing
setblock 3 65 5 create:andesite_encased_shaft[axis=x]
setblock 8 64 5 create:andesite_casing
setblock 8 65 5 create:andesite_encased_shaft[axis=x]
fill 3 66 3 8 66 4 minecraft:spruce_planks
fill 4 66 5 7 66 5 minecraft:spruce_trapdoor[facing=south,half=bottom,open=true]
fill 4 66 4 7 66 4 minecraft:water
