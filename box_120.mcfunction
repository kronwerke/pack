# 120 immersive/cloche
#area 82 211 101 236
fill 82 64 211 101 91 236 minecraft:air
fill 82 60 211 101 62 236 minecraft:stone
fill 82 63 211 101 63 236 minecraft:light_gray_concrete
fill 86 64 217 101 79 217 minecraft:light_gray_concrete
fill 86 64 217 86 79 230 minecraft:light_gray_concrete
setblock 87 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "120"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 88 64 229 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 96 64 217 96 79 230 minecraft:light_gray_concrete
kw testworld use 91 63 222 up immersiveengineering:cloche
data merge block 91 64 222 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
