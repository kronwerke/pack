# 004 create/compacting
#area 42 -6 61 19
fill 42 64 -6 61 91 19 minecraft:air
fill 42 60 -6 61 62 19 minecraft:stone
fill 42 63 -6 61 63 19 minecraft:light_gray_concrete
fill 46 64 0 61 79 0 minecraft:light_gray_concrete
fill 46 64 0 46 79 13 minecraft:light_gray_concrete
setblock 47 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "004"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 48 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 49 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 51.5 71 5.5 {text:'[{"text": "004  ", "color": "gold"}, {"text": "create/compacting", "color": "gray"}, {"text": "\\nVerdichte Andesit", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 56 64 0 56 79 13 minecraft:light_gray_concrete
setblock 51 64 5 create:basin[facing=down]
setblock 51 66 5 create:mechanical_press[facing=south]
fill 50 64 4 52 67 4 create:andesite_casing
setblock 51 66 4 create:andesite_encased_shaft[axis=z]
setblock 51 66 3 create:creative_motor[facing=south]{ScrollValue:32}
summon item 51.5 65 5.5 {Item:{id:"minecraft:flint",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 51.5 65.3 5.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
kw testworld use 51 64 5 up minecraft:lava_bucket
