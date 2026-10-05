# 052 create_trains/schedule
fill 180 63 77 197 63 90 minecraft:light_gray_concrete
fill 180 64 77 197 71 77 minecraft:light_gray_concrete
fill 180 64 77 180 71 90 minecraft:light_gray_concrete
setblock 181 64 89 minecraft:air
setblock 181 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "create_trains"}','{"text": "schedule"}','{"text": ""}']}}
setblock 182 64 89 minecraft:air
setblock 182 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the schedule"}','{"text": "screen with"}','{"text": "conditions"}','{"text": "Gleis entlang Z"}']}}
setblock 183 64 89 minecraft:air
setblock 183 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen, Station"}','{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}']}}
summon text_display 188.5 71 82.5 {text:'[{"text": "052  ", "color": "gold"}, {"text": "create_trains/schedule", "color": "gray"}, {"text": "\\nSchreib einen Fahrplan", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 181 63 82 195 63 82 minecraft:gravel
fill 181 64 82 195 64 82 create:track[shape=xo]
setblock 188 64 83 create:track_station
setblock 195 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
