# 110 immersive/cloche
#area 82 181 101 206
fill 82 64 181 101 91 206 minecraft:air
fill 82 60 181 101 62 206 minecraft:stone
fill 82 63 181 101 63 206 minecraft:light_gray_concrete
fill 86 64 187 101 79 187 minecraft:light_gray_concrete
fill 86 64 187 86 79 200 minecraft:light_gray_concrete
setblock 87 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 88 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 96 64 187 96 79 200 minecraft:light_gray_concrete
kw testworld use 91 63 192 up immersiveengineering:cloche
data merge block 91 64 192 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
