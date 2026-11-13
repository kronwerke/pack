# 093 immersive/cloche
#area 82 179 101 204
fill 82 64 179 101 91 204 minecraft:air
fill 82 60 179 101 62 204 minecraft:stone
fill 82 63 179 101 63 204 minecraft:light_gray_concrete
fill 86 64 185 101 79 185 minecraft:light_gray_concrete
fill 86 64 185 86 79 198 minecraft:light_gray_concrete
setblock 87 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "immersive"}','{"text": "cloche"}','{"text": ""}']}}
setblock 88 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a garden cloche"}','{"text": "growing hemp"}','{"text": ""}','{"text": ""}']}}
fill 96 64 185 96 79 198 minecraft:light_gray_concrete
kw testworld use 91 63 190 up immersiveengineering:cloche
data merge block 91 64 190 {Items:[{Slot:0b,id:"minecraft:dirt",count:1},{Slot:1b,id:"immersiveengineering:seed",count:1}],energy:16000,tank:{Fluid:{id:"minecraft:water",amount:4000}}}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
