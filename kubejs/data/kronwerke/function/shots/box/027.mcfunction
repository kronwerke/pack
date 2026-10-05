# 027 create/compacting
fill 121 63 52 132 63 65 minecraft:light_gray_concrete
fill 121 64 52 132 71 52 minecraft:light_gray_concrete
fill 121 64 52 121 71 65 minecraft:light_gray_concrete
setblock 122 64 64 minecraft:air
setblock 122 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 123 64 64 minecraft:air
setblock 123 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 124 64 64 minecraft:air
setblock 124 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 126.5 71 57.5 {text:'[{"text": "027  ", "color": "gold"}, {"text": "create/compacting", "color": "gray"}, {"text": "\\nVerdichte Andesit", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 126 64 57 create:basin
setblock 126 66 57 create:mechanical_press[facing=east]
setblock 127 66 57 create:shaft[axis=x]
setblock 128 66 57 create:creative_motor[facing=west]{ScrollValue:64}
setblock 130 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:flint",count:32},{Slot:1b,id:"minecraft:gravel",count:32},{Slot:2b,id:"minecraft:lava_bucket",count:1}]}
