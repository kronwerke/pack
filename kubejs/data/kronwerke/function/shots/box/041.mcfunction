# 041 create_brass/blaze_cake
fill 357 63 48 370 63 61 minecraft:light_gray_concrete
fill 357 64 48 370 71 48 minecraft:light_gray_concrete
fill 357 64 48 357 71 61 minecraft:light_gray_concrete
setblock 358 64 60 minecraft:air
setblock 358 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "create_brass"}','{"text": "blaze_cake"}','{"text": ""}']}}
setblock 359 64 60 minecraft:air
setblock 359 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin, then"}','{"text": "spout over"}','{"text": "depot"}']}}
setblock 360 64 53 create:basin
setblock 360 66 53 create:mechanical_press[facing=east]
setblock 364 64 53 create:depot
setblock 364 66 53 create:spout
setblock 364 67 53 create:fluid_tank
setblock 361 66 53 create:creative_motor[facing=west]{ScrollValue:64}
