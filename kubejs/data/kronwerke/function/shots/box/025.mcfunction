# 025 create/mixer
fill 87 63 52 98 63 65 minecraft:light_gray_concrete
fill 87 64 52 98 71 52 minecraft:light_gray_concrete
fill 87 64 52 87 71 65 minecraft:light_gray_concrete
setblock 88 64 64 minecraft:air
setblock 88 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 89 64 64 minecraft:air
setblock 89 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
summon text_display 92.5 71 57.5 {text:'[{"text": "025  ", "color": "gold"}, {"text": "create/mixer", "color": "gray"}, {"text": "\\nBau den Mechanischen Mixer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 92 64 57 create:basin
setblock 92 66 57 create:mechanical_mixer
setblock 93 66 57 create:shaft[axis=x]
setblock 94 66 57 create:creative_motor[facing=west]{ScrollValue:64}
