# 003 create/mixer
#area 27 -6 46 19
fill 27 64 -6 46 91 19 minecraft:air
fill 27 60 -6 46 62 19 minecraft:stone
fill 27 63 -6 46 63 19 minecraft:light_gray_concrete
fill 31 64 0 46 79 0 minecraft:light_gray_concrete
fill 31 64 0 31 79 13 minecraft:light_gray_concrete
setblock 32 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "003"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 33 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
summon text_display 36.5 71 5.5 {text:'[{"text": "003  ", "color": "gold"}, {"text": "create/mixer", "color": "gray"}, {"text": "\\nBau den Mechanischen Mixer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 41 64 0 41 79 9 minecraft:light_gray_concrete
setblock 36 64 5 create:basin[facing=down]
setblock 36 66 5 create:mechanical_mixer
setblock 37 66 5 create:cogwheel[axis=y]
setblock 37 64 5 create:shaft[axis=y]
setblock 37 65 5 create:shaft[axis=y]
setblock 37 63 5 create:creative_motor[facing=up]{ScrollValue:32}
summon item 36.5 65 5.5 {Item:{id:"minecraft:andesite",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 36.5 65.3 5.5 {Item:{id:"minecraft:iron_nugget",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
