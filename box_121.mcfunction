# 121 immersive/cloche
#area 82 215 101 240
fill 82 64 215 101 91 240 minecraft:air
fill 82 60 215 101 62 240 minecraft:stone
fill 82 63 215 101 63 240 minecraft:light_gray_concrete
fill 86 64 221 101 79 221 minecraft:light_gray_concrete
fill 86 64 221 86 79 234 minecraft:light_gray_concrete
setblock 87 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 88 64 233 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 96 64 221 96 79 234 minecraft:light_gray_concrete
kw testworld use 91 63 226 up immersiveengineering:cloche
data merge block 91 64 226 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
