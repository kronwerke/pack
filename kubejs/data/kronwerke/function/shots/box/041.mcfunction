# 041 create_brass/blaze_cake
fill 371 63 52 384 63 65 minecraft:light_gray_concrete
fill 371 64 52 384 71 52 minecraft:light_gray_concrete
fill 371 64 52 371 71 65 minecraft:light_gray_concrete
setblock 372 64 64 minecraft:air
setblock 372 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 373 64 64 minecraft:air
setblock 373 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
summon text_display 377.5 71 57.5 {text:'[{"text": "041  ", "color": "gold"}, {"text": "create_brass/blaze_cake", "color": "gray"}, {"text": "\\nBack einen Lohenkuchen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 374 64 57 create:basin
setblock 374 66 57 create:mechanical_press[facing=east]
setblock 378 64 57 create:depot
setblock 378 66 57 create:spout
setblock 378 67 57 create:fluid_tank
setblock 375 66 57 create:creative_motor[facing=west]{ScrollValue:64}
