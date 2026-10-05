# 051 create_trains/conductor
fill 159 63 77 176 63 90 minecraft:light_gray_concrete
fill 159 64 77 176 71 77 minecraft:light_gray_concrete
fill 159 64 77 159 71 90 minecraft:light_gray_concrete
setblock 160 64 89 minecraft:air
setblock 160 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "051"}','{"text": "create_trains"}','{"text": "conductor"}','{"text": ""}']}}
setblock 161 64 89 minecraft:air
setblock 161 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blaze burner"}','{"text": "sitting as"}','{"text": "conductor"}','{"text": "Gleis entlang Z"}']}}
setblock 162 64 89 minecraft:air
setblock 162 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen, Station"}','{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}']}}
summon text_display 167.5 71 82.5 {text:'[{"text": "051  ", "color": "gold"}, {"text": "create_trains/conductor", "color": "gray"}, {"text": "\\nSetz einen Schaffner ein", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 160 63 82 174 63 82 minecraft:gravel
fill 160 64 82 174 64 82 create:track[shape=xo]
setblock 167 64 83 create:track_station
setblock 174 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
