# 048 create_trains/station
fill 96 63 69 113 63 82 minecraft:light_gray_concrete
fill 96 64 69 113 71 69 minecraft:light_gray_concrete
fill 96 64 69 96 71 82 minecraft:light_gray_concrete
setblock 97 64 81 minecraft:air
setblock 97 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "create_trains"}','{"text": "station"}','{"text": ""}']}}
setblock 98 64 81 minecraft:air
setblock 98 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "station in"}','{"text": "assembly mode"}','{"text": "with bogeys"}','{"text": "Gleis entlang Z"}']}}
setblock 99 64 81 minecraft:air
setblock 99 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "ziehen, Station"}','{"text": "im"}','{"text": "Montagemodus,"}','{"text": "Drehgestelle"}']}}
fill 97 63 74 111 63 74 minecraft:gravel
fill 97 64 74 111 64 74 create:track[shape=xo]
setblock 104 64 75 create:track_station
setblock 111 64 78 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:32},{Slot:1b,id:"create:railway_casing",count:1},{Slot:2b,id:"create:small_bogey",count:1},{Slot:3b,id:"create:controls",count:1},{Slot:4b,id:"create:schedule",count:1},{Slot:5b,id:"create:blaze_burner",count:1},{Slot:6b,id:"create:andesite_casing",count:16},{Slot:7b,id:"create:wrench",count:1}]}
