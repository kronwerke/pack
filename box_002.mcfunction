# 002 create/depot
#area 12 -6 31 19
fill 12 64 -6 31 91 19 minecraft:air
fill 12 60 -6 31 62 19 minecraft:stone
fill 12 63 -6 31 63 19 minecraft:light_gray_concrete
fill 16 64 0 31 79 0 minecraft:light_gray_concrete
fill 16 64 0 16 79 13 minecraft:light_gray_concrete
setblock 17 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "002"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 18 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
summon text_display 21.5 71 5.5 {text:'[{"text": "002  ", "color": "gold"}, {"text": "create/depot", "color": "gray"}, {"text": "\\nStell ein Depot unter die Presse", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 26 64 0 26 79 9 minecraft:light_gray_concrete
setblock 21 64 5 create:depot
setblock 21 66 5 create:mechanical_press[facing=south]
fill 20 64 4 22 67 4 create:andesite_casing
setblock 21 66 4 create:andesite_encased_shaft[axis=z]
setblock 21 66 3 create:creative_motor[facing=south]{ScrollValue:32}
kw testworld use 21 64 5 up minecraft:iron_ingot
