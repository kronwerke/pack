# 048 create_trains/station
fill 96 63 77 113 63 90 minecraft:light_gray_concrete
fill 96 64 77 113 71 77 minecraft:light_gray_concrete
fill 96 64 77 96 71 90 minecraft:light_gray_concrete
setblock 97 64 89 minecraft:air
setblock 97 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 98 64 89 minecraft:air
setblock 98 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": "Gleis entlang Z"}']}}
setblock 99 64 89 minecraft:air
setblock 99 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen, Station"}','{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}']}}
summon text_display 104.5 71 82.5 {text:'[{"text": "048  ", "color": "gold"}, {"text": "create_trains/station", "color": "gray"}, {"text": "\\nBau einen Bahnhof", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 97 63 82 111 63 82 minecraft:gravel
fill 97 64 82 111 64 82 create:track[shape=xo]
setblock 104 64 83 create:track_station
setblock 111 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
