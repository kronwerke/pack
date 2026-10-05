# 050 create_trains/drive
fill 138 63 77 155 63 90 minecraft:light_gray_concrete
fill 138 64 77 155 71 77 minecraft:light_gray_concrete
fill 138 64 77 138 71 90 minecraft:light_gray_concrete
setblock 139 64 89 minecraft:air
setblock 139 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "create_trains"}','{"text": "drive"}','{"text": ""}']}}
setblock 140 64 89 minecraft:air
setblock 140 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the driver\'s"}','{"text": "view from the"}','{"text": "controls"}','{"text": "Gleis entlang Z"}']}}
setblock 141 64 89 minecraft:air
setblock 141 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen, Station"}','{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}']}}
summon text_display 146.5 71 82.5 {text:'[{"text": "050  ", "color": "gold"}, {"text": "create_trains/drive", "color": "gray"}, {"text": "\\nFahr von Hand", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 139 63 82 153 63 82 minecraft:gravel
fill 139 64 82 153 64 82 create:track[shape=xo]
setblock 146 64 83 create:track_station
setblock 153 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
