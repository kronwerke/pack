# 024 create/depot
fill 72 63 48 83 63 61 minecraft:light_gray_concrete
fill 72 64 48 83 71 48 minecraft:light_gray_concrete
fill 72 64 48 72 71 61 minecraft:light_gray_concrete
setblock 73 64 60 minecraft:air
setblock 73 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create"}','{"text": "depot"}','{"text": ""}']}}
setblock 74 64 60 minecraft:air
setblock 74 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press above a"}','{"text": "depot with one"}','{"text": "block of air"}','{"text": "between"}']}}
setblock 77 64 53 create:depot
setblock 77 66 53 create:mechanical_press[facing=east]
setblock 78 66 53 create:shaft[axis=x]
setblock 79 66 53 create:creative_motor[facing=west]{ScrollValue:64}
setblock 81 64 57 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:iron_ingot",count:32}]}
