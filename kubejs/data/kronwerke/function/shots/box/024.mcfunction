# 024 create/depot
fill 72 63 52 83 63 65 minecraft:light_gray_concrete
fill 72 64 52 83 71 52 minecraft:light_gray_concrete
fill 72 64 52 72 71 65 minecraft:light_gray_concrete
setblock 73 64 64 minecraft:air
setblock 73 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 74 64 64 minecraft:air
setblock 74 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
summon text_display 77.5 71 57.5 {text:'[{"text": "024  ", "color": "gold"}, {"text": "create/depot", "color": "gray"}, {"text": "\\nStell ein Depot unter die Presse", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 77 64 57 create:depot
setblock 77 66 57 create:mechanical_press[facing=east]
setblock 78 66 57 create:shaft[axis=x]
setblock 79 66 57 create:creative_motor[facing=west]{ScrollValue:64}
setblock 81 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:iron_ingot",count:32}]}
