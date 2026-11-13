# 140 immersive/cloche
#area 107 219 126 244
fill 107 64 219 126 91 244 minecraft:air
fill 107 60 219 126 62 244 minecraft:stone
fill 107 63 219 126 63 244 minecraft:light_gray_concrete
fill 111 64 225 126 79 225 minecraft:light_gray_concrete
fill 111 64 225 111 79 238 minecraft:light_gray_concrete
setblock 112 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 113 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 121 64 225 121 79 238 minecraft:light_gray_concrete
kw testworld use 116 63 230 up immersiveengineering:cloche
data merge block 116 64 230 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
