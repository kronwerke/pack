# 121 immersive/cloche
#area 82 217 101 242
fill 82 64 217 101 91 242 minecraft:air
fill 82 60 217 101 62 242 minecraft:stone
fill 82 63 217 101 63 242 minecraft:light_gray_concrete
fill 86 64 223 101 79 223 minecraft:light_gray_concrete
fill 86 64 223 86 79 236 minecraft:light_gray_concrete
setblock 87 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 88 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 96 64 223 96 79 236 minecraft:light_gray_concrete
kw testworld use 91 63 228 up immersiveengineering:cloche
data merge block 91 64 228 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
