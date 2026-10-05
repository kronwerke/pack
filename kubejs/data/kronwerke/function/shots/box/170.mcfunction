# 170 immersive/kiln
fill 105 63 255 116 63 268 minecraft:light_gray_concrete
fill 105 64 255 116 71 255 minecraft:light_gray_concrete
fill 105 64 255 105 71 268 minecraft:light_gray_concrete
setblock 106 64 267 minecraft:air
setblock 106 64 267 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170"}','{"text": "immersive"}','{"text": "kiln"}','{"text": ""}']}}
setblock 107 64 267 minecraft:air
setblock 107 64 267 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "alloy kiln"}','{"text": "making electrum"}','{"text": "Mit dem Hammer"}','{"text": "formen"}']}}
place template immersiveengineering:multiblocks/alloy_smelter 107 64 257 none
setblock 114 64 264 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"immersiveengineering:hammer",count:1},{Slot:1b,id:"immersiveengineering:manual",count:1}]}
