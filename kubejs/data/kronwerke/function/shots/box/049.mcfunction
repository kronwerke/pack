# 049 create_trains/first_train
fill 117 63 77 134 63 90 minecraft:light_gray_concrete
fill 117 64 77 134 71 77 minecraft:light_gray_concrete
fill 117 64 77 117 71 90 minecraft:light_gray_concrete
setblock 118 64 89 minecraft:air
setblock 118 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "049"}','{"text": "create_trains"}','{"text": "first_train"}','{"text": ""}']}}
setblock 119 64 89 minecraft:air
setblock 119 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a finished"}','{"text": "small train"}','{"text": "Gleis entlang Z"}','{"text": "ziehen, Station"}']}}
setblock 120 64 89 minecraft:air
setblock 120 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}','{"text": ""}']}}
summon text_display 125.5 71 82.5 {text:'[{"text": "049  ", "color": "gold"}, {"text": "create_trains/first_train", "color": "gray"}, {"text": "\\nBau deinen ersten Zug", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 118 63 82 132 63 82 minecraft:gravel
fill 118 64 82 132 64 82 create:track[shape=xo]
setblock 125 64 83 create:track_station
setblock 132 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
