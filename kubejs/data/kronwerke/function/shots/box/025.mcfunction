# 025 create/mixer
fill 87 63 48 98 63 61 minecraft:light_gray_concrete
fill 87 64 48 98 71 48 minecraft:light_gray_concrete
fill 87 64 48 87 71 61 minecraft:light_gray_concrete
setblock 88 64 60 minecraft:air
setblock 88 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create"}','{"text": "mixer"}','{"text": ""}']}}
setblock 89 64 60 minecraft:air
setblock 89 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer, one"}','{"text": "block of air,"}','{"text": "basin"}','{"text": ""}']}}
setblock 92 64 53 create:basin
setblock 92 66 53 create:mechanical_mixer
setblock 93 66 53 create:shaft[axis=x]
setblock 94 66 53 create:creative_motor[facing=west]{ScrollValue:64}
