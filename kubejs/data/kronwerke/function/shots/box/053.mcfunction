# 053 create_trains/junction
fill 201 63 77 216 63 90 minecraft:light_gray_concrete
fill 201 64 77 216 71 77 minecraft:light_gray_concrete
fill 201 64 77 201 71 90 minecraft:light_gray_concrete
setblock 202 64 89 minecraft:air
setblock 202 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "create_trains"}','{"text": "junction"}','{"text": ""}']}}
setblock 203 64 89 minecraft:air
setblock 203 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain and entry"}','{"text": "signals at a"}','{"text": "junction,"}','{"text": "goggles overlay"}']}}
setblock 204 64 89 minecraft:air
setblock 204 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Weiche legen,"}','{"text": "Ketten- und"}','{"text": "Einfahrtssignale"}','{"text": ""}']}}
summon text_display 208.5 71 82.5 {text:'[{"text": "053  ", "color": "gold"}, {"text": "create_trains/junction", "color": "gray"}, {"text": "\\nSicher eine Kreuzung", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 214 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:track",count:64},{Slot:1b,id:"create:track_signal",count:4},{Slot:2b,id:"create:goggles",count:1}]}
