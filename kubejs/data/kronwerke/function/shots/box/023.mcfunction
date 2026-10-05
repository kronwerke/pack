# 023 create/stress
fill 55 63 52 68 63 65 minecraft:light_gray_concrete
fill 55 64 52 68 71 52 minecraft:light_gray_concrete
fill 55 64 52 55 71 65 minecraft:light_gray_concrete
setblock 56 64 64 minecraft:air
setblock 56 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create"}','{"text": "stress"}','{"text": ""}']}}
setblock 57 64 64 minecraft:air
setblock 57 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "goggles overlay"}','{"text": "on an"}','{"text": "overstressed"}','{"text": "network"}']}}
setblock 58 64 64 minecraft:air
setblock 58 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brille auf,"}','{"text": "Netz ist"}','{"text": "überlastet"}','{"text": ""}']}}
summon text_display 61.5 71 57.5 {text:'[{"text": "023  ", "color": "gold"}, {"text": "create/stress", "color": "gray"}, {"text": "\\nVersteh RPM und SU", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 57 64 57 create:creative_motor[facing=east]{ScrollValue:16}
fill 58 64 57 64 64 57 create:shaft[axis=x]
setblock 59 64 58 create:millstone
setblock 61 64 58 create:millstone
setblock 63 64 58 create:millstone
setblock 66 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:goggles",count:1}]}
