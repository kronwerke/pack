# 125 immersive/cloche
#area 107 217 126 242
fill 107 64 217 126 91 242 minecraft:air
fill 107 60 217 126 62 242 minecraft:stone
fill 107 63 217 126 63 242 minecraft:light_gray_concrete
fill 111 64 223 126 79 223 minecraft:light_gray_concrete
fill 111 64 223 111 79 236 minecraft:light_gray_concrete
setblock 112 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 113 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 121 64 223 121 79 236 minecraft:light_gray_concrete
kw testworld use 116 63 228 up immersiveengineering:cloche
data merge block 116 64 228 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
