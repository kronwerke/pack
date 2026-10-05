# 027 create/compacting
fill 121 63 48 132 63 61 minecraft:light_gray_concrete
fill 121 64 48 132 71 48 minecraft:light_gray_concrete
fill 121 64 48 121 71 61 minecraft:light_gray_concrete
setblock 122 64 60 minecraft:air
setblock 122 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create"}','{"text": "compacting"}','{"text": ""}']}}
setblock 123 64 60 minecraft:air
setblock 123 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "press over"}','{"text": "basin making"}','{"text": "andesite from"}','{"text": "flint, gravel"}']}}
setblock 124 64 60 minecraft:air
setblock 124 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "and lava"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 126 64 53 create:basin
setblock 126 66 53 create:mechanical_press[facing=east]
setblock 127 66 53 create:shaft[axis=x]
setblock 128 66 53 create:creative_motor[facing=west]{ScrollValue:64}
setblock 130 64 57 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:flint",count:32},{Slot:1b,id:"minecraft:gravel",count:32},{Slot:2b,id:"minecraft:lava_bucket",count:1}]}
