# 010 farms/cobble_drill
fill 0 63 31 13 63 44 minecraft:light_gray_concrete
fill 0 64 31 13 71 31 minecraft:light_gray_concrete
fill 0 64 31 0 71 44 minecraft:light_gray_concrete
setblock 1 64 43 minecraft:air
setblock 1 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "cobble_drill"}','{"text": ""}']}}
setblock 2 64 43 minecraft:air
setblock 2 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water and lava"}','{"text": "cobble"}','{"text": "generator with"}','{"text": "a drill and an"}']}}
setblock 3 64 43 minecraft:air
setblock 3 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "andesite"}','{"text": "funnel, belt"}','{"text": "leading away"}','{"text": ""}']}}
summon text_display 6.5 71 36.5 {text:'[{"text": "010  ", "color": "gold"}, {"text": "farms/cobble_drill", "color": "gray"}, {"text": "\\nBau einen Bruchsteingenerator", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 3 64 35 minecraft:glass
setblock 3 64 37 minecraft:glass
setblock 4 64 35 minecraft:glass
setblock 4 64 37 minecraft:glass
setblock 5 64 35 minecraft:glass
setblock 5 64 37 minecraft:glass
setblock 6 64 35 minecraft:glass
setblock 6 64 37 minecraft:glass
setblock 7 64 35 minecraft:glass
setblock 7 64 37 minecraft:glass
setblock 3 64 36 minecraft:glass
setblock 7 64 36 minecraft:glass
fill 3 63 35 7 63 37 minecraft:glass
setblock 4 64 36 minecraft:water
setblock 5 64 36 minecraft:cobblestone
setblock 6 64 36 minecraft:lava
setblock 5 64 37 minecraft:air
setblock 5 64 38 create:mechanical_drill[facing=north]
setblock 5 64 39 create:shaft[axis=z]
setblock 5 64 40 create:creative_motor[facing=north]{ScrollValue:64}
setblock 6 64 38 create:andesite_funnel[facing=north]
setblock 10 64 40 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:belt_connector",count:1}]}
